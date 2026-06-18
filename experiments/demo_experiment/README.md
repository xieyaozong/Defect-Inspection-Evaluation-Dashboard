# Demo Experiment

This experiment uses the bundled synthetic labels, synthetic predictions, and three small CC0 metal-surface demo images documented in `sample_data/ASSET_SOURCES.md`.

Run:

```powershell
python scripts/run_evaluation.py --threshold 0.5 --output-dir experiments/demo_experiment
```

Result at threshold `0.5`:

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

Files:

| File | Purpose |
| --- | --- |
| `evaluation_report.json` | Machine-readable metrics, matches, and error lists. |
| `evaluation_report.html` | Simple offline report. |
| `matches.csv` | Per-image true label, predicted label, score, status, and image path. |
| `false_positives.csv` | Images where the model predicted a defect on a non-defect item. |
| `false_negatives.csv` | Images where the model missed a labeled defect. |
| `classification_errors.csv` | Images where the predicted defect class differs from the true class. |
| `threshold_sweep.csv` | Metrics from threshold `0.00` to `1.00` in `0.05` steps. |
