from __future__ import annotations

from pathlib import Path
import sys
import streamlit as st

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from core.data_loader import load_demo_evaluation
from dashboard.components.metric_cards import render_metric_cards


st.title("Overview")
result = load_demo_evaluation()
render_metric_cards(result.metrics)
st.dataframe(result.matches, use_container_width=True)
