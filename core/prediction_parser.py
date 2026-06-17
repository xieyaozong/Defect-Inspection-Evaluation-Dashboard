from __future__ import annotations

from pathlib import Path
import pandas as pd


def load_predictions(path: Path | str) -> pd.DataFrame:
    data = pd.read_json(path)
    required = {"image_id", "label", "score"}
    missing = required - set(data.columns)
    if missing:
        raise ValueError(f"Prediction file missing columns: {sorted(missing)}")
    return data[["image_id", "label", "score"]].copy()
