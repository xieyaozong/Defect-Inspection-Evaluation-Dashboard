from __future__ import annotations

from pathlib import Path
import sys
import streamlit as st

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from core.data_loader import load_demo_evaluation
from dashboard.components.charts import confusion_matrix_figure


st.title("Confusion Matrix")
result = load_demo_evaluation()
st.plotly_chart(confusion_matrix_figure(result.confusion), use_container_width=True)
