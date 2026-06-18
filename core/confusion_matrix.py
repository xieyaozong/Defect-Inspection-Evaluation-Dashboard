from __future__ import annotations

from sklearn.metrics import confusion_matrix
import pandas as pd


def ordered_labels(values: set[str]) -> list[str]:
    labels = sorted(label for label in values if label != "none")
    if "none" in values:
        labels.append("none")
    return labels


def build_confusion_matrix(matches: pd.DataFrame) -> pd.DataFrame:
    labels = ordered_labels(set(matches["label_true"]) | set(matches["label_pred"]))
    matrix = confusion_matrix(matches["label_true"], matches["label_pred"], labels=labels)
    return pd.DataFrame(matrix, index=labels, columns=labels)
