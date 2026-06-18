from __future__ import annotations

from core.annotation_parser import load_annotations
from core.prediction_parser import load_predictions


def test_parsers_load_sample_data() -> None:
    annotations = load_annotations("sample_data/synthetic_annotations.json")
    predictions = load_predictions("sample_data/synthetic_predictions.json")
    assert {"image_id", "label", "image_path"}.issubset(annotations.columns)
    assert {"image_id", "label", "score"}.issubset(predictions.columns)
