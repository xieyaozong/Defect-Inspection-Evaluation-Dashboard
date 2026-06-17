from __future__ import annotations

import pandas as pd


def false_positives(matches: pd.DataFrame) -> pd.DataFrame:
    return matches[(matches["label_true"] == "none") & (matches["label_pred"] != "none")].copy()


def false_negatives(matches: pd.DataFrame) -> pd.DataFrame:
    return matches[(matches["label_true"] != "none") & (matches["label_pred"] == "none")].copy()
