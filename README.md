# Defect Inspection Evaluation Dashboard

Streamlit dashboard and evaluation toolkit for visual-inspection AI results: false positives, false negatives, misclassifications, threshold tuning, and report export.

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

Open:

```text
http://localhost:8501
```

## Demo Experiment

The repository includes a small CC0 demo image set and synthetic labels/predictions for a reproducible local experiment.

```powershell
python scripts/run_evaluation.py --threshold 0.5 --output-dir experiments/demo_experiment
```

Current demo result at threshold `0.5`:

| Metric | Value |
| --- | ---: |
| Precision | 0.667 |
| Recall | 0.625 |
| F1 | 0.617 |
| Accuracy | 0.625 |
| True positives | 4 |
| False positives | 1 |
| False negatives | 1 |
| Misclassifications | 1 |
| True negatives | 1 |

Experiment artifacts are stored under `experiments/demo_experiment/`.

## Docker

```powershell
docker compose up --build
```

## Input Format

This MVP expects JSON files with records like:

```json
{"image_id": "part_001", "label": "scratch", "image_path": "sample_data/demo_images/scratched_metal_cc0.jpg"}
{"image_id": "part_001", "label": "scratch", "score": 0.91}
```

Ground-truth records do not need `score`. Prediction records can omit `image_path` when the annotation file already has it.

## Layout

```text
defect-inspection-evaluation-dashboard/
  dashboard/    Streamlit pages and UI components
  core/         parsers, evaluator, error analysis, threshold tuning
  sample_data/  synthetic JSON, small CC0 demo images, and asset source records
  experiments/  reproducible demo experiment outputs
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
