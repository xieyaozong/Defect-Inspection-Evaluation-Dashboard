from __future__ import annotations

from pathlib import Path
import os
import sys
import streamlit as st

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from core.data_loader import load_demo_evaluation
from dashboard.components.metric_cards import render_metric_cards
from dashboard.components.charts import confusion_matrix_figure


st.set_page_config(page_title="Defect Inspection Evaluation", layout="wide")
st.title("Defect Inspection Evaluation")

annotations = Path(os.getenv("ANNOTATIONS_PATH", ROOT / "sample_data" / "synthetic_annotations.json"))
predictions = Path(os.getenv("PREDICTIONS_PATH", ROOT / "sample_data" / "synthetic_predictions.json"))
threshold = st.slider("Confidence threshold", 0.0, 1.0, float(os.getenv("DEFAULT_THRESHOLD", "0.5")), 0.01)

result = load_demo_evaluation(annotations, predictions, threshold)
render_metric_cards(result.metrics)
st.plotly_chart(confusion_matrix_figure(result.confusion), use_container_width=True)

st.subheader("False Positives")
st.dataframe(result.false_positives, use_container_width=True)

st.subheader("False Negatives")
st.dataframe(result.false_negatives, use_container_width=True)
