# core/standards_db.py
#
# Purpose:
#   Load ISO 27001:2022 Annex A controls from a JSON file so that
#   the rest of the project can treat controls as Python dicts.
#
# Data:
#   Expects iso27001_final.json in:
#   PROJECT/PROJECT/complyai/data/standards/iso27001_final.json
#
# Public API (stable for the project):
#   - load_iso27001_controls() -> list[dict]
#
# Each control dict MUST contain at least:
#   - "id"    (e.g. "A.5.1")
#   - "title" (short name)
#   - "text"  (full control description)

from pathlib import Path
from typing import List, Dict, Any
import json


BASE_DIR = Path(__file__).resolve().parents[1]
ISO_JSON_PATH = BASE_DIR / "data" / "standards" / "iso27001_final.json"


def load_iso27001_controls() -> List[Dict[str, Any]]:
    """
    Load all ISO 27001 Annex A controls from the JSON file.

    Returns:
        List of control dicts.
        Each control MUST have an "id" key (e.g. "A.5.1").
    """
    if not ISO_JSON_PATH.exists():
        raise FileNotFoundError(f"ISO 27001 JSON not found at: {ISO_JSON_PATH}")

    with ISO_JSON_PATH.open(encoding="utf-8") as f:
        data = json.load(f)

    # Expect the JSON to be either:
    # - a list of controls, or
    # - an object with a key like "controls" holding the list.
    if isinstance(data, list):
        controls = data
    elif isinstance(data, dict) and "controls" in data:
        controls = data["controls"]
    else:
        raise ValueError("Unexpected ISO 27001 JSON structure; "
                         "expected a list or an object with 'controls' key.")

    # Normalise minimum fields and types
    normalised = []
    for c in controls:
        cid = str(c.get("id", "")).strip()
        if not cid:
            continue  # skip any malformed entries

        normalised.append(
            {
                "id": cid,
                "title": str(c.get("title", "")).strip(),
                "text": str(
                    c.get("description", c.get("text", ""))
                ).strip(),
            }
        )

    return normalised