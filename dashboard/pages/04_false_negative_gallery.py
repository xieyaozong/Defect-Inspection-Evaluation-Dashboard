from __future__ import annotations

from pathlib import Path
import sys
import streamlit as st

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from core.data_loader import load_demo_evaluation
from dashboard.components.image_gallery import render_table_gallery


st.title("False Negative Gallery")
result = load_demo_evaluation()
render_table_gallery(result.false_negatives)
