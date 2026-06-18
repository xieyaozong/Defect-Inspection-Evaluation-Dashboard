from __future__ import annotations

from pathlib import Path
import sys
import streamlit as st

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from core.data_loader import load_demo_evaluation
from core.report_generator import report_html, report_json


st.title("Report Export")
result = load_demo_evaluation()
st.download_button("Download JSON report", report_json(result), "evaluation_report.json", "application/json")
st.download_button("Download HTML report", report_html(result), "evaluation_report.html", "text/html")
st.download_button("Download CSV report", result.matches.to_csv(index=False), "evaluation_matches.csv", "text/csv")
