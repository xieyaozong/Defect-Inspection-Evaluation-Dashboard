from __future__ import annotations

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from core.data_loader import load_demo_evaluation
from core.report_generator import report_json


def main() -> None:
    output = Path("outputs/evaluation_report.json")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(report_json(load_demo_evaluation()), encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()
