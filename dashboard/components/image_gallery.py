from __future__ import annotations

import pandas as pd
import streamlit as st


def render_table_gallery(records: pd.DataFrame) -> None:
    if records.empty:
        st.info("No records.")
        return
    st.dataframe(records, use_container_width=True)
