from __future__ import annotations

from pathlib import Path
import argparse
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from core.annotation_parser import load_annotations
from core.evaluator import evaluate
from core.prediction_parser import load_predictions
from core.report_generator import write_report
from core.threshold_optimizer import sweep_thresholds


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--annotations", type=Path, default=Path("sample_data/demo_annotations.json"))
    parser.add_argument("--predictions", type=Path, default=Path("sample_data/demo_predictions.json"))
    parser.add_argument("--threshold", type=float, default=0.5)
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/demo_experiment"))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    annotations = load_annotations(args.annotations)
    predictions = load_predictions(args.predictions)
    result = evaluate(annotations, predictions, args.threshold)
    paths = write_report(result, args.output_dir)
    curve = sweep_thresholds(annotations, predictions)
    curve_path = args.output_dir / "threshold_sweep.csv"
    curve.to_csv(curve_path, index=False)
    print(result.metrics)
    print(f"Wrote report files to {args.output_dir}")
    print(f"Wrote threshold sweep to {curve_path}")
    for path in paths.values():
        print(path)


if __name__ == "__main__":
    main()
