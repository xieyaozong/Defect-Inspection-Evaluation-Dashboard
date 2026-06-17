from __future__ import annotations

from core.data_loader import load_records
from core.threshold_optimizer import sweep_thresholds


def test_threshold_sweep() -> None:
    annotations, predictions = load_records()
    curve = sweep_thresholds(annotations, predictions, [0.0, 0.5, 1.0])
    assert list(curve["threshold"]) == [0.0, 0.5, 1.0]
    assert "f1" in curve.columns
