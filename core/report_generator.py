from __future__ import annotations

import json
from core.evaluator import EvaluationResult


def report_json(result: EvaluationResult) -> str:
    return json.dumps(
        {
            "metrics": result.metrics,
            "matches": result.matches.to_dict(orient="records"),
            "false_positives": result.false_positives.to_dict(orient="records"),
            "false_negatives": result.false_negatives.to_dict(orient="records"),
        },
        indent=2,
    )
