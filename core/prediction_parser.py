from __future__ import annotations

from pathlib import Path
import pandas as pd


def load_predictions(path: Path | str) -> pd.DataFrame:
    data = pd.read_json(path)
    required = {"image_id", "label", "score"}
    missing = required - set(data.columns)
    if missing:
        raise ValueError(f"Prediction file missing columns: {sorted(missing)}")
    columns = ["image_id", "label", "score"]
    if "image_path" in data.columns:
        columns.append("image_path")
    data = data[columns].copy()
    data["score"] = pd.to_numeric(data["score"], errors="raise")
    return data
