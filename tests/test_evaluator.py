from __future__ import annotations

from core.evaluator import evaluate
import pandas as pd


def test_evaluate_counts_fp_fn() -> None:
    annotations = pd.DataFrame(
        [
            {"image_id": "a", "label": "scratch"},
            {"image_id": "b", "label": "none"},
            {"image_id": "c", "label": "dent"},
            {"image_id": "d", "label": "stain"},
        ]
    )
    predictions = pd.DataFrame(
        [
            {"image_id": "a", "label": "scratch", "score": 0.9},
            {"image_id": "b", "label": "dent", "score": 0.8},
            {"image_id": "c", "label": "scratch", "score": 0.7},
        ]
    )
    result = evaluate(annotations, predictions)
    assert result.metrics["true_positive"] == 1
    assert result.metrics["false_positive"] == 1
    assert result.metrics["false_negative"] == 1
    assert result.metrics["misclassification"] == 1
    assert len(result.false_positives) == 1
    assert len(result.false_negatives) == 1
    assert len(result.classification_errors) == 1
