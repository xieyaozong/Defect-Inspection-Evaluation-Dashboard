from __future__ import annotations

from pathlib import Path
import argparse
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from core.data_loader import load_demo_evaluation
from core.report_generator import write_report


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/demo_experiment"))
    parser.add_argument("--threshold", type=float, default=0.5)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    paths = write_report(load_demo_evaluation(threshold=args.threshold), args.output_dir)
    for path in paths.values():
        print(path)


if __name__ == "__main__":
    main()
