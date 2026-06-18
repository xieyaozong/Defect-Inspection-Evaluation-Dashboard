from __future__ import annotations

import pandas as pd


def false_positives(matches: pd.DataFrame) -> pd.DataFrame:
    return matches[matches["status"] == "false_positive"].copy()


def false_negatives(matches: pd.DataFrame) -> pd.DataFrame:
    return matches[matches["status"] == "false_negative"].copy()


def classification_errors(matches: pd.DataFrame) -> pd.DataFrame:
    return matches[matches["status"] == "misclassification"].copy()
