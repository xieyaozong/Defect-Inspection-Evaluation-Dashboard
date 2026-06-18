from __future__ import annotations

from pathlib import Path
import json


ANNOTATIONS = [
    {"image_id": "part_001", "label": "scratch", "image_path": "sample_data/demo_images/scratched_metal_cc0.jpg"},
    {"image_id": "part_002", "label": "dent", "image_path": "sample_data/demo_images/scratched_metal_cc0.jpg"},
    {"image_id": "part_003", "label": "none", "image_path": "sample_data/demo_images/tempering_colors_steel_cc0.jpg"},
    {"image_id": "part_004", "label": "stain", "image_path": "sample_data/demo_images/stained_metal_cc0.jpg"},
    {"image_id": "part_005", "label": "scratch", "image_path": "sample_data/demo_images/scratched_metal_cc0.jpg"},
    {"image_id": "part_006", "label": "none", "image_path": "sample_data/demo_images/tempering_colors_steel_cc0.jpg"},
    {"image_id": "part_007", "label": "stain", "image_path": "sample_data/demo_images/stained_metal_cc0.jpg"},
    {"image_id": "part_008", "label": "dent", "image_path": "sample_data/demo_images/scratched_metal_cc0.jpg"},
]

PREDICTIONS = [
    {"image_id": "part_001", "label": "scratch", "score": 0.93},
    {"image_id": "part_002", "label": "scratch", "score": 0.64},
    {"image_id": "part_003", "label": "dent", "score": 0.78},
    {"image_id": "part_004", "label": "stain", "score": 0.42},
    {"image_id": "part_005", "label": "scratch", "score": 0.88},
    {"image_id": "part_007", "label": "stain", "score": 0.71},
    {"image_id": "part_008", "label": "dent", "score": 0.52},
]


def write_json(path: Path, records: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(records, indent=2), encoding="utf-8")


def main() -> None:
    sample_dir = Path("sample_data")
    write_json(sample_dir / "demo_annotations.json", ANNOTATIONS)
    write_json(sample_dir / "demo_predictions.json", PREDICTIONS)
    print(f"Wrote sample JSON files under {sample_dir}")
    print("Demo images are tracked separately; see sample_data/ASSET_SOURCES.md")


if __name__ == "__main__":
    main()
