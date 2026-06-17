from __future__ import annotations

import pandas as pd
from sklearn.metrics import confusion_matrix


def build_confusion_matrix(matches: pd.DataFrame) -> pd.DataFrame:
    labels = sorted(set(matches["label_true"]) | set(matches["label_pred"]))
    matrix = confusion_matrix(matches["label_true"], matches["label_pred"], labels=labels)
    return pd.DataFrame(matrix, index=labels, columns=labels)
