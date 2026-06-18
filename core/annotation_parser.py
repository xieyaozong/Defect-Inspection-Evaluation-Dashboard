from __future__ import annotations

from pathlib import Path
import pandas as pd


def load_annotations(path: Path | str) -> pd.DataFrame:
    data = pd.read_json(path)
    required = {"image_id", "label"}
    missing = required - set(data.columns)
    if missing:
        raise ValueError(f"Annotation file missing columns: {sorted(missing)}")
    columns = ["image_id", "label"]
    if "image_path" in data.columns:
        columns.append("image_path")
    return data[columns].copy()
