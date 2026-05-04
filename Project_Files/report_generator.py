import json
import re
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Tuple


REPORTS_DIR = Path("reports")


def ensure_reports_dir() -> None:
    """Ensure the reports output directory exists."""
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)


def control_sort_key(control_id: str) -> Tuple[int, ...]:
    """Sort control IDs numerically so A.5.2 appears before A.5.10."""
    numbers = re.findall(r"\d+", str(control_id or "").strip())
    if not numbers:
        return (9999,)
    return tuple(int(part) for part in numbers)


def group_controls_by_domain(controls: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    """Group evaluated controls by domain so the detailed report remains stable."""
    grouped: Dict[str, List[Dict[str, Any]]] = defaultdict(list)

    for row in controls:
        domain = str(row.get("domain", "")).strip() or "Unknown"
        grouped[domain].append(row)

    for domain in grouped:
        grouped[domain] = sorted(
            grouped[domain],
            key=lambda item: control_sort_key(str(item.get("control_id", "")).strip()),
        )

    return dict(grouped)


def get_priority_gaps(controls: List[Dict[str, Any]], limit: int = 10) -> List[Dict[str, Any]]:
    """Return the highest-priority gaps first."""
    priority = [
        row
        for row in controls
        if str(
            row.get("llm_decision", row.get("llm_final_status", ""))
        ).strip() in {"Not Implemented", "Partially Implemented"}
    ]

    status_order = {
        "Not Implemented": 0,
        "Partially Implemented": 1,
    }

    priority.sort(
        key=lambda item: (
            status_order.get(
                str(item.get("llm_decision", item.get("llm_final_status", ""))).strip(),
                99,
            ),
            control_sort_key(str(item.get("control_id", "")).strip()),
        )
    )
    return priority[:limit]


def _clean_text(value: Any) -> str:
    """Normalize any value into a compact single-line string."""
    return " ".join(str(value or "").split()).strip()


def _truncate_text(text: str, limit: int = 220) -> str:
    """Trim long text for cleaner markdown output."""
    text = _clean_text(text)
    if len(text) <= limit:
        return text
    return text[: limit - 3].rstrip() + "..."


def _format_evidence_snippets(snippets: Any, max_items: int = 2) -> List[str]:
    """
    Keep only the top two short evidence lines for the report.
    This avoids printing long raw policy paragraphs in markdown output.
    """
    if not isinstance(snippets, list):
        return []

    cleaned: List[str] = []
    seen = set()

    for snippet in snippets:
        text = _truncate_text(snippet, limit=220)
        if not text:
            continue
        key = text.lower()
        if key in seen:
            continue
        seen.add(key)
        cleaned.append(text)
        if len(cleaned) >= max_items:
            break

    return cleaned


def build_markdown_report(report_object: Dict[str, Any]) -> str:
    """Build the final markdown report from the already-built report object."""
    framework = report_object.get("framework", "ISO 27001:2022 Annex A")
    stage1 = report_object.get("stage1", {})
    stage2 = report_object.get("stage2", [])
    stage3 = report_object.get("stage3", {})

    grouped = group_controls_by_domain(stage2)
    priority_gaps = get_priority_gaps(stage2)

    lines: List[str] = [
        "# ComlyAI: An Agentic Gap Analysis.",
        "",
        f"Framework: {framework}",
        f"Generated at: {report_object.get('generated_at', datetime.now().isoformat(timespec='seconds'))}",
        "",
        "## Overview",
        "",
        (
            "This report presents the final automated gap analysis for "
            "ISO 27001:2022 Annex A controls against the organisation's "
            "Statement of Applicability, scope context, business objectives, "
            "and available evidence."
        ),
        "",
        "## Stage 1",
        "",
        (
            "- Total number of controls available as per security framework: "
            f"{stage1.get('total_number_of_controls_available_as_per_security_framework', 0)}"
        ),
        (
            "- Total number of controls Available as per organisation's SOA: "
            f"{stage1.get('total_number_of_controls_available_as_per_organisations_soa', 0)}"
        ),
        (
            "- Total number of controls Implemented as per organisation's SOA: "
            f"{stage1.get('total_number_of_controls_implemented_as_per_organisations_soa', 0)}"
        ),
        (
            "- Total number of controls partially implemented by the organisation as per SOA: "
            f"{stage1.get('total_number_of_controls_partially_implemented_by_the_organisation_as_per_soa', 0)}"
        ),
        (
            "- Total number of controls not implemented by the organisation as per SOA: "
            f"{stage1.get('total_number_of_controls_not_implemented_by_the_organisation_as_per_soa', 0)}"
        ),
        "",
        "## Stage 3",
        "",
        f"- Total controls evaluated: {stage3.get('total_controls_evaluated', 0)}",
        f"- Applicable: {stage3.get('applicable', 0)}",
        f"- Not required: {stage3.get('not_required', 0)}",
        f"- Implemented: {stage3.get('implemented', 0)}",
        f"- Partially implemented: {stage3.get('partially_implemented', 0)}",
        f"- Not implemented: {stage3.get('not_implemented', 0)}",
        f"- LLM Decision marked not required: {stage3.get('not_required_status', 0)}",
        "",
        "## Priority Findings",
        "",
    ]

    if priority_gaps:
        for item in priority_gaps:
            lines.extend(
                [
                    f"### {item.get('control_id', '')} - {item.get('control_title', '')}",
                    "",
                    f"- Domain: {item.get('domain', '')}",
                    f"- Applicability decision: {item.get('llm_applicability_decision', '')}",
                    f"- LLM Decision: {item.get('llm_decision', item.get('llm_final_status', ''))}",
                    f"- Evidence summary: {_truncate_text(item.get('llm_evidence_summary', ''), 300)}",
                    f"- Gap note: {_truncate_text(item.get('llm_gap_note', ''), 300)}",
                    f"- Recommendation: {_truncate_text(item.get('llm_recommendation', ''), 300)}",
                    "",
                ]
            )
    else:
        lines.extend(["No priority gaps were detected.", ""])

    lines.extend(["## Domain-wise Detailed Analysis", ""])

    for domain, items in grouped.items():
        lines.extend([f"### {domain}", ""])
        for item in items:
            evidence_lines = _format_evidence_snippets(item.get("evidence_snippets", []))
            evidence_display = " | ".join(evidence_lines) if evidence_lines else "No short evidence lines available."

            lines.extend(
                [
                    f"#### {item.get('control_id', '')} - {item.get('control_title', '')}",
                    "",
                    f"- SoA applicable: {item.get('soa_applicable', '')}",
                    f"- SoA implementation status: {item.get('soa_implementationstatus', '')}",
                    f"- LLM applicability decision: {item.get('llm_applicability_decision', '')}",
                    f"- LLM Decision: {item.get('llm_decision', item.get('llm_final_status', ''))}",
                    f"- Evidence snippets: {evidence_display}",
                    f"- Evidence summary: {_truncate_text(item.get('llm_evidence_summary', ''), 300)}",
                    f"- Gap note: {_truncate_text(item.get('llm_gap_note', ''), 300)}",
                    f"- Recommendation: {_truncate_text(item.get('llm_recommendation', ''), 300)}",
                    "",
                ]
            )

    return "\n".join(lines)


def save_json_report(report_object: Dict[str, Any], basename: str) -> str:
    """Save the final report object as a timestamped JSON artifact."""
    ensure_reports_dir()
    path = REPORTS_DIR / f"{basename}.json"
    path.write_text(json.dumps(report_object, indent=2, ensure_ascii=False), encoding="utf-8")
    return str(path)


def save_markdown_report(markdown_text: str, basename: str) -> str:
    """Save the rendered markdown report."""
    ensure_reports_dir()
    path = REPORTS_DIR / f"{basename}.md"
    path.write_text(markdown_text, encoding="utf-8")
    return str(path)


def generate_reports_from_report_object(report_object: Dict[str, Any]) -> Dict[str, str]:
    """
    Generate all report artifacts from the already-built final report object.
    This keeps a single clean report-generation path.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    basename = f"complyai_gap_assessment_{timestamp}"

    markdown_text = build_markdown_report(report_object)
    json_report = save_json_report(report_object, basename)
    markdown_report = save_markdown_report(markdown_text, basename)

    return {
        "json_report": json_report,
        "markdown_report": markdown_report,
    }
