from __future__ import annotations

import pandas as pd
import plotly.express as px


def confusion_matrix_figure(confusion: pd.DataFrame):
    return px.imshow(confusion, text_auto=True, aspect="auto", color_continuous_scale="Blues")


def threshold_curve(curve: pd.DataFrame):
    return px.line(curve, x="threshold", y=["precision", "recall", "f1"], markers=True)
