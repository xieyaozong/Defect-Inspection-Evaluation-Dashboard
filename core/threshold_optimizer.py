from __future__ import annotations

from core.evaluator import evaluate
import pandas as pd

def sweep_thresholds(
    annotations: pd.DataFrame,
    predictions: pd.DataFrame,
    thresholds: list[float] | None = None,
) -> pd.DataFrame:
    thresholds = thresholds or [round(value / 100, 2) for value in range(0, 101, 5)]
    rows = []
    for threshold in thresholds:
        result = evaluate(annotations, predictions, threshold=threshold)
        rows.append({"threshold": threshold, **result.metrics})
    return pd.DataFrame(rows)
