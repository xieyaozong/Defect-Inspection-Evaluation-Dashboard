from __future__ import annotations

from pathlib import Path
from core.evaluator import EvaluationResult
import json
import pandas as pd


def frame_records(data: pd.DataFrame) -> list[dict]:
    cleaned = data.where(pd.notna(data), None)
    return cleaned.to_dict(orient="records")


def report_json(result: EvaluationResult) -> str:
    return json.dumps(
        {
            "metrics": result.metrics,
            "matches": frame_records(result.matches),
            "false_positives": frame_records(result.false_positives),
            "false_negatives": frame_records(result.false_negatives),
            "classification_errors": frame_records(result.classification_errors),
        },
        indent=2,
    )


def report_html(result: EvaluationResult) -> str:
    metrics = pd.DataFrame([result.metrics]).to_html(index=False)
    confusion = result.confusion.to_html()
    matches = result.matches.to_html(index=False)
    return "\n".join(
        [
            "<!doctype html>",
            "<html><head><meta charset='utf-8'><title>Defect Inspection Evaluation Report</title></head><body>",
            "<h1>Defect Inspection Evaluation Report</h1>",
            "<h2>Metrics</h2>",
            metrics,
            "<h2>Confusion Matrix</h2>",
            confusion,
            "<h2>Matches</h2>",
            matches,
            "</body></html>",
        ]
    )


def write_report(result: EvaluationResult, output_dir: Path | str) -> dict[str, Path]:
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "json": output / "evaluation_report.json",
        "html": output / "evaluation_report.html",
        "matches_csv": output / "matches.csv",
        "false_positives_csv": output / "false_positives.csv",
        "false_negatives_csv": output / "false_negatives.csv",
        "classification_errors_csv": output / "classification_errors.csv",
    }
    paths["json"].write_text(report_json(result), encoding="utf-8")
    paths["html"].write_text(report_html(result), encoding="utf-8")
    result.matches.to_csv(paths["matches_csv"], index=False)
    result.false_positives.to_csv(paths["false_positives_csv"], index=False)
    result.false_negatives.to_csv(paths["false_negatives_csv"], index=False)
    result.classification_errors.to_csv(paths["classification_errors_csv"], index=False)
    return paths
