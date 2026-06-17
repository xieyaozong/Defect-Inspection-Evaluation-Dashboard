from __future__ import annotations

import pandas as pd
import streamlit as st


def class_filter(data: pd.DataFrame, column: str = "label") -> list[str]:
    values = sorted(str(value) for value in data[column].dropna().unique())
    return st.multiselect("Class", values, default=values)
