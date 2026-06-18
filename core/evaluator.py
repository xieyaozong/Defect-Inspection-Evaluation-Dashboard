from __future__ import annotations

from dataclasses import dataclass
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from core.confusion_matrix import build_confusion_matrix, ordered_labels
from core.error_analyzer import classification_errors, false_negatives, false_positives
import pandas as pd


@dataclass
class EvaluationResult:
    metrics: dict
    matches: pd.DataFrame
    confusion: pd.DataFrame
    false_positives: pd.DataFrame
    false_negatives: pd.DataFrame
    classification_errors: pd.DataFrame


def assign_status(row: pd.Series) -> str:
    true_label = row["label_true"]
    pred_label = row["label_pred"]
    if true_label == "none" and pred_label == "none":
        return "true_negative"
    if true_label != "none" and pred_label == true_label:
        return "true_positive"
    if true_label == "none" and pred_label != "none":
        return "false_positive"
    if true_label != "none" and pred_label == "none":
        return "false_negative"
    return "misclassification"


def merge_image_path(matches: pd.DataFrame) -> pd.Series:
    if "image_path" in matches:
        return matches["image_path"]
    true_path = matches["image_path_true"] if "image_path_true" in matches else pd.Series(index=matches.index, dtype=object)
    pred_path = matches["image_path_pred"] if "image_path_pred" in matches else pd.Series(index=matches.index, dtype=object)
    return true_path.combine_first(pred_path)


def evaluate(annotations: pd.DataFrame, predictions: pd.DataFrame, threshold: float = 0.5) -> EvaluationResult:
    filtered = predictions[predictions["score"] >= threshold].copy()
    best = filtered.sort_values("score", ascending=False).drop_duplicates("image_id")
    merged = annotations.merge(best, on="image_id", how="outer", suffixes=("_true", "_pred"))
    merged["label_true"] = merged["label_true"].fillna("none")
    merged["label_pred"] = merged["label_pred"].fillna("none")
    if "score" in merged:
        merged["score"] = merged["score"].fillna(0.0)
    merged["image_path"] = merge_image_path(merged)
    merged = merged.drop(columns=[column for column in ["image_path_true", "image_path_pred"] if column in merged])
    merged["status"] = merged.apply(assign_status, axis=1)
    labels = ordered_labels(set(merged["label_true"]) | set(merged["label_pred"]))
    status_counts = merged["status"].value_counts().to_dict()
    metrics = {
        "precision": precision_score(merged["label_true"], merged["label_pred"], labels=labels, average="macro", zero_division=0),
        "recall": recall_score(merged["label_true"], merged["label_pred"], labels=labels, average="macro", zero_division=0),
        "f1": f1_score(merged["label_true"], merged["label_pred"], labels=labels, average="macro", zero_division=0),
        "accuracy": accuracy_score(merged["label_true"], merged["label_pred"]),
        "threshold": threshold,
        "total_images": int(len(merged)),
        "true_positive": int(status_counts.get("true_positive", 0)),
        "false_positive": int(status_counts.get("false_positive", 0)),
        "false_negative": int(status_counts.get("false_negative", 0)),
        "misclassification": int(status_counts.get("misclassification", 0)),
        "true_negative": int(status_counts.get("true_negative", 0)),
    }
    return EvaluationResult(
        metrics=metrics,
        matches=merged,
        confusion=build_confusion_matrix(merged),
        false_positives=false_positives(merged),
        false_negatives=false_negatives(merged),
        classification_errors=classification_errors(merged),
    )
