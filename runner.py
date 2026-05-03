import json
from datetime import datetime
from typing import Any, Dict, List

from core.gap_analyzer import (
    stage1_summary,
    stage2_gap_analysis,
    stage3_summary_from_stage2,
)
from core.report_generator import generate_reports_from_report_object


# Purpose of this file:
# - Execute the three locked stages in order.
# - Print Stage 1 fully, Stage 2 progress only, and Stage 3 fully.
# - Save the final report object and print the completion path.


def build_report_object(
    stage1: Dict[str, Any],
    stage2: List[Dict[str, Any]],
    stage3: Dict[str, Any],
) -> Dict[str, Any]:
    """Build the single final report object used by report generation."""
    return {
        "framework": stage1.get("framework", "ISO 27001:2022 Annex A"),
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "stage1": stage1,
        "stage2": stage2,
        "stage3": stage3,
    }


def main() -> None:
    """
    Execute the locked project flow.

    Console behavior:
    - Stage 1: print full Stage 1 output.
    - Stage 2: print only progress text.
    - Stage 3: print full Stage 3 output.
    - End: print completion message with the final result path.
    """
    print("=============== Stage 1 ===============")
    stage1 = stage1_summary()
    print(json.dumps(stage1, indent=2, ensure_ascii=False))

    print("\n=============== Stage 2 ===============")
    print("evaluating controls")
    stage2 = stage2_gap_analysis(max_controls=None)

    stage3 = stage3_summary_from_stage2(stage2)
    report_object = build_report_object(stage1=stage1, stage2=stage2, stage3=stage3)

    print("\n=============== Stage 3 ===============")
    print(json.dumps(stage3, indent=2, ensure_ascii=False))

    generated_files = generate_reports_from_report_object(report_object)
    result_file = generated_files["json_report"]

    print(f"\nevaluation completed. Kindly find the result {result_file}.")


if __name__ == "__main__":
    main()