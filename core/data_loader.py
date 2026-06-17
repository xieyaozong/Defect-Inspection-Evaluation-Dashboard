from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import os
import pandas as pd
from core.annotation_parser import load_annotations
from core.evaluator import EvaluationResult, evaluate
from core.prediction_parser import load_predictions


DEFAULT_ANNOTATIONS = Path("sample_data/synthetic_annotations.json")
DEFAULT_PREDICTIONS = Path("sample_data/synthetic_predictions.json")


def load_records(
    annotations_path: Path | str | None = None,
    predictions_path: Path | str | None = None,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    annotations = Path(annotations_path or os.getenv("ANNOTATIONS_PATH", DEFAULT_ANNOTATIONS))
    predictions = Path(predictions_path or os.getenv("PREDICTIONS_PATH", DEFAULT_PREDICTIONS))
    return load_annotations(annotations), load_predictions(predictions)


def load_demo_evaluation(
    annotations_path: Path | str | None = None,
    predictions_path: Path | str | None = None,
    threshold: float = 0.5,
) -> EvaluationResult:
    annotations, predictions = load_records(annotations_path, predictions_path)
    return evaluate(annotations, predictions, threshold=threshold)
