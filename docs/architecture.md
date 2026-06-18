# Architecture

The dashboard reads labels and predictions, evaluates them in `core/`, and renders metrics, confusion matrix, FP/FN galleries, threshold curves, and export files through Streamlit.

```text
Ground Truth JSON + Prediction JSON
        ↓
Parser validation
        ↓
Threshold filtering + best prediction per image
        ↓
Evaluation status per image
        ↓
Metrics / confusion matrix / FP-FN-misclassification lists
        ↓
Dashboard + JSON / CSV / HTML reports
```
