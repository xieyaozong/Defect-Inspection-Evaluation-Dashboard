from __future__ import annotations

import pandas as pd
from core.evaluator import evaluate


def test_evaluate_counts_fp_fn() -> None:
    annotations = pd.DataFrame([{"image_id": "a", "label": "scratch"}, {"image_id": "b", "label": "none"}])
    predictions = pd.DataFrame([{"image_id": "a", "label": "scratch", "score": 0.9}, {"image_id": "b", "label": "dent", "score": 0.8}])
    result = evaluate(annotations, predictions)
    assert result.metrics["accuracy"] == 0.5
    assert len(result.false_positives) == 1
