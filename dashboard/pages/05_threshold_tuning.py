from __future__ import annotations

from pathlib import Path
import sys
import streamlit as st

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from core.data_loader import load_records
from core.threshold_optimizer import sweep_thresholds
from dashboard.components.charts import threshold_curve


st.title("Threshold Tuning")
annotations, predictions = load_records()
curve = sweep_thresholds(annotations, predictions)
st.plotly_chart(threshold_curve(curve), use_container_width=True)
st.dataframe(curve, use_container_width=True)
