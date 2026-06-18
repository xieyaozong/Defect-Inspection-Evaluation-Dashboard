from __future__ import annotations

from pathlib import Path
import pandas as pd
import streamlit as st


def render_table_gallery(records: pd.DataFrame, root: Path | None = None) -> None:
    if records.empty:
        st.info("No records.")
        return

    root = root or Path.cwd()
    if "image_path" not in records.columns:
        st.dataframe(records, use_container_width=True)
        return

    columns = st.columns(3)
    for index, (_, row) in enumerate(records.reset_index(drop=True).iterrows()):
        image_path = Path(str(row.get("image_path", "")))
        if not image_path.is_absolute():
            image_path = root / image_path
        with columns[index % len(columns)]:
            if image_path.exists():
                st.image(str(image_path), use_container_width=True)
            st.caption(
                f"{row.get('image_id', '')} | true={row.get('label_true', '')} "
                f"| pred={row.get('label_pred', '')} | score={row.get('score', 0):.2f}"
            )
    st.dataframe(records, use_container_width=True)
