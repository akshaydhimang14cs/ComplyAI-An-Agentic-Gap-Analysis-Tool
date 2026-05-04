# core/soa_loader.py
#
# Purpose:
#   Load the ABC Statement of Applicability (SoA) from Excel and expose it:
#     - as a list of row dicts
#     - as a dict keyed by controlid (e.g. "A.5.1")
#
# Data:
#   Expects abc_soa.xlsx in:
#   PROJECT/PROJECT/complyai/data/soa/abc_soa.xlsx
#
# Columns expected in the Excel sheet:
#   controlid, domain, title, applicable,
#   implementationstatus, justification, mappeddocs
#
# Public API (stable for the project):
#   - load_soa_entries() -> list[dict]
#   - soa_to_dict()      -> dict[str, dict]

from pathlib import Path
from typing import List, Dict, Any

import pandas as pd


BASE_DIR: Path = Path(__file__).resolve().parents[1]
SOA_PATH: Path = BASE_DIR / "data" / "soa" / "abc_soa.xlsx"


def load_soa_entries() -> List[Dict[str, Any]]:
    """
    Load the ABC SoA from Excel and return a list of row dicts.

    Returns:
        List of rows, each a dict with keys at least:
          controlid, domain, title, applicable,
          implementationstatus, justification, mappeddocs

        mappeddocs is normalised to a list[str] of filenames.
    """
    if not SOA_PATH.exists():
        raise FileNotFoundError(f"SoA file not found at: {SOA_PATH}")

    df = pd.read_excel(SOA_PATH)

    required_cols = [
        "controlid",
        "domain",
        "title",
        "applicable",
        "implementationstatus",
        "justification",
        "mappeddocs",
    ]
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Missing required SoA column: {col}")

    rows = df.to_dict(orient="records")

    # Normalise mapped docs into list[str]
    for row in rows:
        mapped = row.get("mappeddocs", "")
        if pd.isna(mapped):
            mapped = ""
        row["mappeddocs"] = [
            x.strip()
            for x in str(mapped).split(";")
            if x.strip()
        ]

    return rows


def soa_to_dict() -> Dict[str, Dict[str, Any]]:
    """
    Return the SoA as a dict keyed by controlid (e.g. "A.5.1").

    This is the main structure used by the gap analyzer.
    """
    rows = load_soa_entries()
    return {str(row["controlid"]).strip(): row for row in rows}
