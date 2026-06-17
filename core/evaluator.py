from __future__ import annotations

from dataclasses import dataclass
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from core.confusion_matrix import build_confusion_matrix
from core.error_analyzer import false_negatives, false_positives


@dataclass
class EvaluationResult:
    metrics: dict
    matches: pd.DataFrame
    confusion: pd.DataFrame
    false_positives: pd.DataFrame
    false_negatives: pd.DataFrame


def evaluate(annotations: pd.DataFrame, predictions: pd.DataFrame, threshold: float = 0.5) -> EvaluationResult:
    filtered = predictions[predictions["score"] >= threshold].copy()
    best = filtered.sort_values("score", ascending=False).drop_duplicates("image_id")
    merged = annotations.merge(best, on="image_id", how="outer", suffixes=("_true", "_pred"))
    merged["label_true"] = merged["label_true"].fillna("none")
    merged["label_pred"] = merged["label_pred"].fillna("none")
    labels = sorted(set(merged["label_true"]) | set(merged["label_pred"]))
    metrics = {
        "precision": precision_score(merged["label_true"], merged["label_pred"], labels=labels, average="macro", zero_division=0),
        "recall": recall_score(merged["label_true"], merged["label_pred"], labels=labels, average="macro", zero_division=0),
        "f1": f1_score(merged["label_true"], merged["label_pred"], labels=labels, average="macro", zero_division=0),
        "accuracy": accuracy_score(merged["label_true"], merged["label_pred"]),
    }
    return EvaluationResult(
        metrics=metrics,
        matches=merged,
        confusion=build_confusion_matrix(merged),
        false_positives=false_positives(merged),
        false_negatives=false_negatives(merged),
    )
