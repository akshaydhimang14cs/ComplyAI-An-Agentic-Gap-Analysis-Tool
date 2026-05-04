import json
import re
from collections import Counter
from typing import Any, Dict, List, Optional, Tuple

from .llm_client import ask_llm
from .org_docs import load_org_context
from .soa_loader import soa_to_dict
from .standards_db import load_iso27001_controls


# Purpose of this module:
# - Stage 1: summarize framework versus SoA coverage.
# - Stage 2: evaluate every SoA control with the LLM.
# - Stage 3: build final counts strictly from Stage 2 outputs.
#
# Locked design goals:
# - Evaluate every control present in the SoA.
# - Ask the LLM both applicability and implementation status together.
# - Keep decisions conservative when evidence is weak or generic.
# - Prevent SoA justification from being treated as direct proof of implementation.
# - Keep output stable for runner.py and report_generator.py.


def _clean_text(value: Any) -> str:
    """Convert any value to a compact single-line string."""
    return " ".join(str(value or "").split()).strip()


def _truncate_text(value: Any, max_chars: int) -> str:
    """Trim long text so prompts and reports stay compact and stable."""
    text = _clean_text(value)
    if len(text) <= max_chars:
        return text
    return text[: max_chars - 3].rstrip() + "..."


def _normalize_status_label(value: str) -> str:
    """Normalize SoA implementation status labels into the project vocabulary."""
    cleaned = _clean_text(value).lower()
    if "partial" in cleaned:
        return "Partially Implemented"
    if "not implemented" in cleaned:
        return "Not Implemented"
    if "implemented" in cleaned:
        return "Implemented"
    return "Controls unknown"


def _is_soa_applicable(soa_value: str) -> bool:
    """Interpret the SoA applicable field in a tolerant way."""
    cleaned = _clean_text(soa_value).lower()
    return cleaned in {"yes", "y", "applicable", "true"}


def stage1_summary() -> Dict[str, Any]:
    """
    Build the Stage 1 summary using the exact required output fields.
    This stage is factual only and does not use the LLM.
    """
    iso_controls = load_iso27001_controls()
    soa_dict = soa_to_dict()

    iso_ids = [str(control.get("id", "")).strip() for control in iso_controls]
    missing_controls = [control_id for control_id in iso_ids if control_id not in soa_dict]

    status_counts = Counter(
        _normalize_status_label(str(row.get("implementationstatus", "")))
        for row in soa_dict.values()
    )

    return {
        "framework": "ISO 27001:2022 Annex A",
        #"total_iso_controls": len(iso_controls),
        #"soa_unique_controls": len(soa_dict),
       
        "total_number_of_controls_available_as_per_security_framework": len(iso_controls),
        "total_number_of_controls_available_as_per_organisations_soa": len(soa_dict),
        "total_number_of_iso_controls_missing_in_soa_count": len(missing_controls),
        "total_number_of_controls_implemented_as_per_organisations_soa": status_counts.get("Implemented", 0),
        "total_number_of_controls_partially_implemented_by_the_organisation_as_per_soa": status_counts.get("Partially Implemented", 0),
        "total_number_of_controls_not_implemented_by_the_organisation_as_per_soa": status_counts.get("Not Implemented", 0),
        "soa_status_counts": {
            "Implemented": status_counts.get("Implemented", 0),
            "Partially Implemented": status_counts.get("Partially Implemented", 0),
            "Not Implemented": status_counts.get("Not Implemented", 0),
            "Controls unknown": status_counts.get("Controls unknown", 0),
        },
    }


def split_into_paragraphs(text: str) -> List[str]:
    """Split policy text into meaningful paragraph blocks for lightweight retrieval."""
    if not text:
        return []

    return [
        paragraph.strip()
        for paragraph in text.split("\n\n")
        if len(_clean_text(paragraph)) >= 40
    ]


def extract_keywords(control: Dict[str, Any], soa_row: Dict[str, Any]) -> List[str]:
    """
    Build compact retrieval keywords from the control and SoA row.
    These keywords help score policy paragraphs for relevance.
    """
    blob = " ".join(
        [
            str(control.get("id", "")),
            str(control.get("title", "")),
            str(control.get("text", "")),
            str(control.get("domain", "")),
            str(soa_row.get("title", "")),
            str(soa_row.get("justification", "")),
            " ".join(soa_row.get("mappeddocs", []))
            if isinstance(soa_row.get("mappeddocs", []), list)
            else str(soa_row.get("mappeddocs", "")),
        ]
    ).lower()

    stopwords = {
        "the", "and", "for", "with", "that", "this", "shall", "should",
        "from", "into", "have", "has", "been", "are", "is", "of", "to",
        "in", "on", "by", "be", "an", "a", "or", "as", "at", "it", "all",
        "must", "used", "using", "their", "there", "where", "which",
    }

    normalized_blob = re.sub(r"[^a-z0-9]+", " ", blob)
    tokens: List[str] = []
    seen = set()

    for word in normalized_blob.split():
        if len(word) >= 4 and word not in stopwords and word not in seen:
            seen.add(word)
            tokens.append(word)

    return tokens[:15]


def _split_into_sentences(text: str) -> List[str]:
    """Split a paragraph into short candidate sentences for concise evidence output."""
    if not text:
        return []

    raw_parts = re.split(r"(?<=[.!?])\s+|\n+|-\s+", text)
    return [_clean_text(part) for part in raw_parts if len(_clean_text(part)) >= 25]


def _score_text_relevance(text: str, keywords: List[str]) -> int:
    """Simple keyword-overlap scoring used for lightweight evidence ranking."""
    lowered = text.lower()
    return sum(1 for keyword in keywords if keyword in lowered)


def _deduplicate_preserve_order(items: List[str]) -> List[str]:
    """Remove duplicates while preserving the original order."""
    unique: List[str] = []
    seen = set()
    for item in items:
        normalized = _clean_text(item)
        if normalized and normalized not in seen:
            seen.add(normalized)
            unique.append(normalized)
    return unique


def get_relevant_policy_snippets(
    policy_text: str,
    control: Dict[str, Any],
    soa_row: Dict[str, Any],
    max_snippets: int = 2,
) -> List[str]:
    """
    Retrieve up to two short, relevant evidence snippets.
    The function scores paragraphs and then short sentences inside them.
    """
    paragraphs = split_into_paragraphs(policy_text)
    keywords = extract_keywords(control, soa_row)

    scored_sentences: List[Tuple[int, str]] = []
    for paragraph in paragraphs:
        paragraph_score = _score_text_relevance(paragraph, keywords)
        if paragraph_score <= 0:
            continue

        for sentence in _split_into_sentences(paragraph):
            sentence_score = _score_text_relevance(sentence, keywords)
            if sentence_score > 0:
                scored_sentences.append(
                    (sentence_score + paragraph_score, _truncate_text(sentence, 220))
                )

    scored_sentences.sort(key=lambda item: item[0], reverse=True)
    selected = [sentence for _, sentence in scored_sentences[: max_snippets * 3]]
    return _deduplicate_preserve_order(selected)[:max_snippets]


def build_stage2_prompt(
    control: Dict[str, Any],
    soa_row: Dict[str, Any],
    evidence_snippets: List[str],
    scope_statement: str,
    business_objectives: str,
) -> str:
    """
    Build the Stage 2 prompt.
    The prompt is intentionally conservative and asks the model to decide:
    - whether the control is Applicable or Not Required,
    - and what the implementation status is.
    """
    joined_snippets = "\n".join(f"- {snippet}" for snippet in evidence_snippets)
    if not joined_snippets:
        joined_snippets = "- No direct policy evidence snippet found for this control."

    mapped_docs = (
        ", ".join(soa_row.get("mappeddocs", []))
        if isinstance(soa_row.get("mappeddocs", []), list)
        else _clean_text(soa_row.get("mappeddocs", ""))
    )

    return f"""
You are an ISO 27001:2022 lead IT auditor performing a conservative control assessment.

Use only the information below.
Do not invent facts.
Do not copy the SoA justification into your recommendation or gap note.
Do not treat generic policy language as proof that a control is fully implemented.

You must answer both:
1. Is the control Applicable or Not Required?
2. What is the implementation status: Implemented, Partially Implemented, Not Implemented, or Not Required?

Strict decision rules:
- If the SoA marks the control as applicable and the control is clearly inside scope, do not mark it Not Required unless there is a strong explicit reason from the scope context.
- If the SoA says Partially Implemented or Not Implemented, do not upgrade to Implemented unless the evidence snippets clearly show control-specific implementation.
- If evidence is weak, generic, indirect, or absent, prefer Partially Implemented or Not Implemented.
- SoA justification may be used as context only, not as direct proof of implementation.
- recommendation must be written from an auditor point of view.
- gap_note must explain the implementation gap or state that no material gap is observed.
- evidence_summary must briefly state what evidence supported the decision.
- Return only valid JSON in one line.

Organisation context:
Scope statement: {_truncate_text(scope_statement, 350)}
Business objectives: {_truncate_text(business_objectives, 350)}

ISO control:
ID: {_clean_text(control.get("id", ""))}
Title: {_truncate_text(control.get("title", ""), 180)}
Text: {_truncate_text(control.get("text", ""), 700)}

SoA row:
Applicable: {_clean_text(soa_row.get("applicable", ""))}
Implementation status: {_clean_text(soa_row.get("implementationstatus", ""))}
Justification: {_truncate_text(soa_row.get("justification", ""), 320)}
Mapped documents: {_truncate_text(mapped_docs, 220)}

Evidence snippets:
{joined_snippets}

Return exactly this JSON shape:
{{
  "control_id": "...",
  "applicability_decision": "Applicable or Not Required",
  "llm_decision": "Implemented or Partially Implemented or Not Implemented or Not Required",
  "evidence_summary": "...",
  "gap_note": "...",
  "recommendation": "..."
}}
""".strip()


def safe_parse_llm_json(raw_response: Any) -> Dict[str, Any]:
    """Safely parse JSON returned by the LLM, even if it adds extra text."""
    if isinstance(raw_response, dict):
        return raw_response

    if raw_response is None:
        return {}

    text = str(raw_response).strip()
    if not text:
        return {}

    try:
        return json.loads(text)
    except json.JSONDecodeError:
        start = text.find("{")
        end = text.rfind("}")
        if start != -1 and end != -1 and end > start:
            try:
                return json.loads(text[start:end + 1])
            except json.JSONDecodeError:
                return {}
        return {}


def normalize_applicability(value: str) -> str:
    """Normalize applicability to the allowed report values."""
    cleaned = _clean_text(value).lower()
    return "Not Required" if "not required" in cleaned else "Applicable"


def normalize_final_status(value: str, applicability_decision: str) -> str:
    """Normalize implementation status to the allowed report values."""
    cleaned = _clean_text(value).lower()

    if applicability_decision == "Not Required":
        return "Not Required"
    if "partially" in cleaned:
        return "Partially Implemented"
    if "not implemented" in cleaned:
        return "Not Implemented"
    if "implemented" in cleaned:
        return "Implemented"
    return "Not Implemented"


def default_gap_note_for_status(final_status: str) -> str:
    """Provide a stable gap note when the LLM omits one."""
    defaults = {
        "Implemented": "No material gap observed.",
        "Partially Implemented": "The control appears to exist, but implementation coverage or supporting evidence is incomplete.",
        "Not Implemented": "The control is required, but evidence of implementation was not identified.",
        "Not Required": "The control is outside the current scope and has been treated as not required.",
    }
    return defaults.get(final_status, "Assessment requires manual review.")


def default_recommendation_for_status(final_status: str) -> str:
    """Provide a stable auditor-style recommendation when the LLM omits one."""
    defaults = {
        "Implemented": "Maintain the control and retain current supporting evidence for future audits.",
        "Partially Implemented": "Complete the remaining implementation activities and retain direct evidence that the control is operating as intended.",
        "Not Implemented": "Implement the control, define ownership, and produce direct supporting evidence of operation.",
        "Not Required": "Retain documented scope rationale supporting why this control is not required.",
    }
    return defaults.get(final_status, "Review this control manually.")


def _is_text_too_similar(left: str, right: str) -> bool:
    """Detect when two short texts are effectively the same after normalization."""
    left_clean = _clean_text(left).lower()
    right_clean = _clean_text(right).lower()
    return bool(left_clean and right_clean and left_clean == right_clean)


def _recommendation_conflicts_with_status(recommendation: str, final_status: str) -> bool:
    """
    Reject clearly contradictory recommendations.
    Example: recommendation says fully implemented while decision is partial/not implemented.
    """
    text = _clean_text(recommendation).lower()
    if not text:
        return True

    if final_status in {"Partially Implemented", "Not Implemented"}:
        if any(
            phrase in text
            for phrase in [
                "fully implemented",
                "no material gap observed",
                "no material gap is observed",
                "control is fully implemented",
            ]
        ):
            return True

    if final_status == "Not Required" and "implement" in text:
        return True

    return False


def build_evidence_summary(snippets: List[str], parsed: Dict[str, Any], soa_justification: str) -> str:
    """
    Build a short evidence summary.

    Preference order:
    1. valid LLM summary,
    2. concise snippet-based summary,
    3. fallback to SoA justification as context only.
    """
    llm_summary = _truncate_text(parsed.get("evidence_summary", ""), 260)
    if llm_summary:
        return llm_summary

    if snippets:
        joined = " | ".join(_clean_text(snippet) for snippet in snippets if _clean_text(snippet))
        return _truncate_text(joined, 260)

    if _clean_text(soa_justification):
        return _truncate_text(
            f"No direct evidence snippet was identified. Context available from SoA justification: {soa_justification}",
            260,
        )

    return "No direct supporting evidence was identified for this control."


def _has_direct_evidence(snippets: List[str]) -> bool:
    """
    Decide whether there is likely direct control evidence.
    Retrieved policy snippets are treated as stronger than SoA justification.
    """
    return bool(snippets)


def apply_decision_guardrails(
    control: Dict[str, Any],
    soa_row: Dict[str, Any],
    applicability_decision: str,
    final_status: str,
    snippets: List[str],
) -> Tuple[str, str, str]:
    """
    Apply deterministic guardrails after the LLM response.
    This protects against clearly invalid outcomes.
    """
    soa_applicable = _is_soa_applicable(str(soa_row.get("applicable", "")))
    soa_status = _normalize_status_label(str(soa_row.get("implementationstatus", "")))
    control_text = _clean_text(control.get("text", ""))
    control_title = _clean_text(control.get("title", ""))
    direct_evidence = _has_direct_evidence(snippets)

    rationale = ""

    if soa_applicable and applicability_decision == "Not Required":
        applicability_decision = "Applicable"
        rationale = (
            "Adjusted applicability to Applicable because the SoA marks this control as applicable "
            "and no strong scope-based exclusion was established."
        )
        if final_status == "Not Required":
            final_status = soa_status if soa_status != "Unknown" else "Not Implemented"

    foundational_keywords = {"policy", "policies", "isms", "access control", "risk", "classification"}
    if applicability_decision == "Not Required":
        title_blob = f"{control_title} {control_text}".lower()
        if any(keyword in title_blob for keyword in foundational_keywords) and soa_applicable:
            applicability_decision = "Applicable"
            final_status = soa_status if soa_status != "Unknown" else "Not Implemented"
            rationale = (
                "Adjusted applicability to Applicable because this is a foundational in-scope control "
                "and the SoA marks it applicable."
            )

    if applicability_decision == "Applicable":
        if soa_status == "Not Implemented" and final_status == "Implemented" and not direct_evidence:
            final_status = "Not Implemented"
            rationale = (
                "Adjusted LLM Decision to Not Implemented because the SoA marks the control "
                "Not Implemented and direct control-specific evidence was not identified."
            )
        elif soa_status == "Partially Implemented" and final_status == "Implemented" and not direct_evidence:
            final_status = "Partially Implemented"
            rationale = (
                "Adjusted LLM Decision to Partially Implemented because the SoA marks the control "
                "Partially Implemented and direct control-specific evidence was not identified."
            )
        elif soa_status == "Unknown" and final_status == "Implemented" and not direct_evidence:
            final_status = "Partially Implemented"
            rationale = (
                "Adjusted LLM Decision to Partially Implemented because implementation evidence "
                "is indirect and not control-specific."
            )

    if applicability_decision == "Not Required":
        final_status = "Not Required"

    return applicability_decision, final_status, rationale


def control_sort_key(control_id: str) -> Tuple[int, ...]:
    """Sort controls numerically so A.5.2 comes before A.5.10."""
    numbers = re.findall(r"\d+", _clean_text(control_id))
    if not numbers:
        return (9999,)
    return tuple(int(part) for part in numbers)


def build_final_record(
    cid: str,
    control: Dict[str, Any],
    soa_row: Dict[str, Any],
    parsed: Dict[str, Any],
    snippets: List[str],
) -> Dict[str, Any]:
    """
    Build one normalized Stage 2 record.
    This centralizes post-processing so the final JSON structure remains stable.
    """
    title = _clean_text(soa_row.get("title", "")) or _clean_text(control.get("title", ""))
    domain = _clean_text(soa_row.get("domain", "")) or _clean_text(control.get("domain", "")) or "Unknown"
    soa_justification = _clean_text(soa_row.get("justification", ""))

    applicability_decision = normalize_applicability(parsed.get("applicability_decision", "Applicable"))
    final_status = normalize_final_status(
        parsed.get("llm_decision", parsed.get("final_status", "")),
        applicability_decision,
    )

    applicability_decision, final_status, guardrail_note = apply_decision_guardrails(
        control=control,
        soa_row=soa_row,
        applicability_decision=applicability_decision,
        final_status=final_status,
        snippets=snippets,
    )

    gap_note = _clean_text(parsed.get("gap_note", ""))
    if not gap_note:
        gap_note = default_gap_note_for_status(final_status)
    if _is_text_too_similar(gap_note, soa_justification):
        gap_note = default_gap_note_for_status(final_status)
    if guardrail_note and final_status in {"Partially Implemented", "Not Implemented"}:
        gap_note = _truncate_text(f"{gap_note} {guardrail_note}", 300)

    recommendation = _clean_text(parsed.get("recommendation", ""))
    if (
        not recommendation
        or _is_text_too_similar(recommendation, soa_justification)
        or _recommendation_conflicts_with_status(recommendation, final_status)
    ):
        recommendation = default_recommendation_for_status(final_status)

    evidence_summary = build_evidence_summary(snippets, parsed, soa_justification)

    return {
        "control_id": cid,
        "control_title": title,
        "domain": domain,
        "control_text": _clean_text(control.get("text", "")),
        "soa_applicable": _clean_text(soa_row.get("applicable", "")),
        "soa_implementationstatus": _clean_text(soa_row.get("implementationstatus", "")),
        "soa_justification": soa_justification,
        "mapped_docs": soa_row.get("mappeddocs", []),
        "llm_applicability_decision": applicability_decision,
        "llm_decision": final_status,
        "llm_final_status": final_status,
        "llm_evidence_summary": evidence_summary,
        "llm_gap_note": gap_note,
        "llm_recommendation": recommendation,
        "evidence_snippets": [_truncate_text(snippet, 220) for snippet in snippets[:2]],
    }


def build_fallback_record(
    cid: str,
    control: Dict[str, Any],
    soa_row: Dict[str, Any],
    snippets: List[str],
    gap_note: str,
    recommendation: str,
    applicability_decision: str = "Applicable",
    final_status: str = "Not Implemented",
) -> Dict[str, Any]:
    """Build a safe fallback record when the LLM response cannot be used."""
    title = _clean_text(soa_row.get("title", "")) or _clean_text(control.get("title", ""))
    domain = _clean_text(soa_row.get("domain", "")) or _clean_text(control.get("domain", "")) or "Unknown"
    soa_justification = _clean_text(soa_row.get("justification", ""))

    applicability_decision, final_status, guardrail_note = apply_decision_guardrails(
        control=control,
        soa_row=soa_row,
        applicability_decision=applicability_decision,
        final_status=final_status,
        snippets=snippets,
    )

    combined_gap_note = _clean_text(gap_note) or default_gap_note_for_status(final_status)
    if _is_text_too_similar(combined_gap_note, soa_justification):
        combined_gap_note = default_gap_note_for_status(final_status)
    if guardrail_note:
        combined_gap_note = _truncate_text(f"{combined_gap_note} {guardrail_note}", 300)

    final_recommendation = _clean_text(recommendation)
    if (
        not final_recommendation
        or _is_text_too_similar(final_recommendation, soa_justification)
        or _recommendation_conflicts_with_status(final_recommendation, final_status)
    ):
        final_recommendation = default_recommendation_for_status(final_status)

    return {
        "control_id": cid,
        "control_title": title,
        "domain": domain,
        "control_text": _clean_text(control.get("text", "")),
        "soa_applicable": _clean_text(soa_row.get("applicable", "")),
        "soa_implementationstatus": _clean_text(soa_row.get("implementationstatus", "")),
        "soa_justification": soa_justification,
        "mapped_docs": soa_row.get("mappeddocs", []),
        "llm_applicability_decision": applicability_decision,
        "llm_decision": final_status,
        "llm_final_status": final_status,
        "llm_evidence_summary": build_evidence_summary(snippets, {}, soa_justification),
        "llm_gap_note": combined_gap_note,
        "llm_recommendation": final_recommendation,
        "evidence_snippets": [_truncate_text(snippet, 220) for snippet in snippets[:2]],
    }


def stage2_gap_analysis(max_controls: Optional[int] = None) -> List[Dict[str, Any]]:
    """
    Evaluate every control present in the SoA.

    Locked rule:
    - no pre-filtering by applicability,
    - controls marked not implemented are still evaluated,
    - the LLM decides applicability and implementation together.
    """
    iso_controls_by_id = {
        str(control.get("id", "")).strip(): control
        for control in load_iso27001_controls()
    }
    soa_dict = soa_to_dict()
    org_context = load_org_context()

    policy_text = org_context["policy_text"]
    scope_statement = org_context["scope_statement"]
    business_objectives = org_context["business_objectives"]

    results: List[Dict[str, Any]] = []
    processed = 0

    sorted_control_ids = sorted(soa_dict.keys(), key=control_sort_key)

    for cid in sorted_control_ids:
        soa_row = soa_dict[cid]
        control = iso_controls_by_id.get(cid)
        if not control:
            continue

        snippets = get_relevant_policy_snippets(
            policy_text=policy_text,
            control=control,
            soa_row=soa_row,
            max_snippets=2,
        )

        prompt = build_stage2_prompt(
            control=control,
            soa_row=soa_row,
            evidence_snippets=snippets,
            scope_statement=scope_statement,
            business_objectives=business_objectives,
        )

        try:
            raw = ask_llm(prompt)
            parsed = safe_parse_llm_json(raw)

            if parsed:
                results.append(build_final_record(cid, control, soa_row, parsed, snippets))
            else:
                results.append(
                    build_fallback_record(
                        cid=cid,
                        control=control,
                        soa_row=soa_row,
                        snippets=snippets,
                        gap_note="Unable to parse assessment output.",
                        recommendation="Review this control manually and rerun the assessment.",
                    )
                )
        except Exception:
            results.append(
                build_fallback_record(
                    cid=cid,
                    control=control,
                    soa_row=soa_row,
                    snippets=snippets,
                    gap_note="Assessment could not be completed.",
                    recommendation="Review this control manually and rerun the assessment.",
                )
            )

        processed += 1
        if max_controls is not None and processed >= max_controls:
            break

    return results


def stage3_summary_from_stage2(stage2_results: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Build Stage 3 strictly from Stage 2 evaluated results.
    This summary does not reuse Stage 1 SoA coverage counts.
    """
    return {
        "total_controls_evaluated": len(stage2_results),
        "applicable": sum(1 for row in stage2_results if row.get("llm_applicability_decision") == "Applicable"),
        "not_required": sum(1 for row in stage2_results if row.get("llm_applicability_decision") == "Not Required"),
        "implemented": sum(1 for row in stage2_results if row.get("llm_decision") == "Implemented"),
        "partially_implemented": sum(1 for row in stage2_results if row.get("llm_decision") == "Partially Implemented"),
        "not_implemented": sum(1 for row in stage2_results if row.get("llm_decision") == "Not Implemented"),
        "not_required_status": sum(1 for row in stage2_results if row.get("llm_decision") == "Not Required"),
    }


def build_final_report_object() -> Dict[str, Any]:
    """Build one consistent report object containing Stage 1, Stage 2, and Stage 3."""
    stage1 = stage1_summary()
    stage2 = stage2_gap_analysis(max_controls=None)
    stage3 = stage3_summary_from_stage2(stage2)

    return {
        "framework": stage1.get("framework", "ISO 27001:2022 Annex A"),
        "stage1": stage1,
        "stage2": stage2,
        "stage3": stage3,
    }
