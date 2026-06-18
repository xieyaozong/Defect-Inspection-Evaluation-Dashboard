from __future__ import annotations

import streamlit as st


def render_metric_cards(metrics: dict) -> None:
    columns = st.columns(4)
    for column, key in zip(columns, ["precision", "recall", "f1", "accuracy"]):
        column.metric(key.upper(), f"{metrics.get(key, 0.0):.3f}")


def render_error_cards(metrics: dict) -> None:
    columns = st.columns(5)
    keys = ["true_positive", "false_positive", "false_negative", "misclassification", "true_negative"]
    for column, key in zip(columns, keys):
        column.metric(key.replace("_", " ").title(), int(metrics.get(key, 0)))
