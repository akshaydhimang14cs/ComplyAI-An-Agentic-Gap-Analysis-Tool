from pathlib import Path
from typing import Dict


# Purpose of this module:
# - Load the organisation policy and scope input files.
# - Extract short scope and business-context text used in Stage 2 prompts.
# - Keep document-loading logic in one place so the analyzer remains focused.


BASE_DIR = Path(__file__).resolve().parents[1]
POLICY_DIR = BASE_DIR / "data" / "org_inputs" / "policies"

DEFAULT_POLICY_FILE = "ISMS_Policy_ABC_corporation.txt"
DEFAULT_SCOPE_FILE = "ABC_ISMS_Scope_Statement.txt"


def load_policy_text(filename: str) -> str:
    """Load a plain-text organisational document from the policy input folder."""
    path = POLICY_DIR / filename
    if not path.exists():
        raise FileNotFoundError(f"Policy file not found: {path}")
    return path.read_text(encoding="utf-8")


def load_default_policy() -> str:
    """Load the primary ISMS policy text used as evidence source material."""
    return load_policy_text(DEFAULT_POLICY_FILE)


def load_scope_document() -> str:
    """Load the scope document used to derive scope statement and business objectives."""
    return load_policy_text(DEFAULT_SCOPE_FILE)


def _clean_text_block(text: str) -> str:
    """Normalize a document block into a compact single-line string."""
    return " ".join(text.split()).strip()


def extract_scope_statement(scope_text: str) -> str:
    """
    Extract a compact scope statement from the scope document.

    The function first looks for a section mentioning scope and otherwise falls
    back to the first meaningful block.
    """
    if not scope_text.strip():
        return ""

    blocks = [block.strip() for block in scope_text.split("\n\n") if block.strip()]
    lowered = [block.lower() for block in blocks]

    for index, block in enumerate(lowered):
        if "scope" in block:
            return _clean_text_block(blocks[index])

    return _clean_text_block(blocks[0]) if blocks else ""


def extract_business_objectives(scope_text: str) -> str:
    """
    Extract a compact business-objectives section from the scope document.

    If the document has no clear objectives section, the function falls back
    to the next meaningful paragraph so Stage 2 still gets context.
    """
    if not scope_text.strip():
        return ""

    blocks = [block.strip() for block in scope_text.split("\n\n") if block.strip()]
    lowered = [block.lower() for block in blocks]

    objective_keywords = (
        "objective",
        "objectives",
        "business objective",
        "business objectives",
        "purpose",
        "aim",
    )

    for index, block in enumerate(lowered):
        if any(keyword in block for keyword in objective_keywords):
            return _clean_text_block(blocks[index])

    if len(blocks) > 1:
        return _clean_text_block(blocks[1])

    return _clean_text_block(blocks[0]) if blocks else ""


def load_org_context() -> Dict[str, str]:
    """
    Load the full organisational context required by the analyzer.

    Returns both raw text and extracted short-form context for prompting.
    """
    policy_text = load_default_policy()
    scope_text = load_scope_document()

    return {
        "policy_text": policy_text,
        "scope_text": scope_text,
        "scope_statement": extract_scope_statement(scope_text),
        "business_objectives": extract_business_objectives(scope_text),
    }
