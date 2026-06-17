from __future__ import annotations

from pathlib import Path
import argparse
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from core.annotation_parser import load_annotations
from core.evaluator import evaluate
from core.prediction_parser import load_predictions


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--annotations", type=Path, default=Path("sample_data/synthetic_annotations.json"))
    parser.add_argument("--predictions", type=Path, default=Path("sample_data/synthetic_predictions.json"))
    parser.add_argument("--threshold", type=float, default=0.5)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    result = evaluate(load_annotations(args.annotations), load_predictions(args.predictions), args.threshold)
    print(result.metrics)


if __name__ == "__main__":
    main()
