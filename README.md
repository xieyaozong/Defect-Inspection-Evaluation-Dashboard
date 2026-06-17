# Defect Inspection Evaluation Dashboard

Evaluation dashboard for visual-inspection AI results: false positives, false negatives, threshold tuning, and report export.

## Flow

```text
Ground Truth + Prediction
  -> Evaluation Engine
  -> Precision / Recall / F1 / Confusion Matrix
  -> FP / FN Gallery
  -> Threshold Tuning
  -> HTML / CSV / JSON Report
```

## Dataset Policy

Please download MVTec AD, VisA, DeepPCB, or other public datasets from official sources. This repository does not redistribute third-party datasets.

## Run

```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
streamlit run dashboard/app.py
```

## Docker

```powershell
docker compose up --build
```

## Input Format

This MVP expects JSON files with records like:

```json
{"image_id": "part_001", "label": "scratch", "score": 0.91}
```

Ground-truth records do not need `score`.

## Layout

```text
defect-inspection-evaluation-dashboard/
  dashboard/    Streamlit pages and UI components
  core/         parsers, evaluator, error analysis, threshold tuning
  sample_data/  small synthetic JSON and local demo images
  scripts/      conversion, evaluation, sample generation, report export
  docs/         formats, metrics, FP/FN analysis, S3 notes
  infra/        AWS deployment notes
  tests/        focused checks for evaluator and parsers
```

## MVP

- Load prediction and label JSON.
- Display confusion matrix.
- Display FP / FN tables.
- Export CSV / JSON reports.
- Tune confidence threshold.
