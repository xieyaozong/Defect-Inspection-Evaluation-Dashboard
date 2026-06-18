from __future__ import annotations

from core.data_loader import load_demo_evaluation
from core.report_generator import report_json, write_report
import json

def test_report_json_contains_error_sections() -> None:
    payload = json.loads(report_json(load_demo_evaluation()))
    assert "metrics" in payload
    assert "false_positives" in payload
    assert "false_negatives" in payload
    assert "classification_errors" in payload


def test_write_report(tmp_path) -> None:
    paths = write_report(load_demo_evaluation(), tmp_path)
    assert paths["json"].exists()
    assert paths["html"].exists()
    assert paths["matches_csv"].exists()
