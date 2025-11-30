#!/usr/bin/env python3
"""Build Azure and GCP static bundles from the shared CSV generator."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Dict

TARGET_PATHS: Dict[str, str] = {
    "azure": "build/azure/{business}",
    "gcp": "build/gcp/{business}",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build cloud-specific static bundles.")
    parser.add_argument(
        "--business",
        default="kabalian",
        help="Business identifier to filter the CSV (default: kabalian).",
    )
    parser.add_argument(
        "--csv",
        default="content/content-template.csv",
        help="Path to the content CSV file.",
    )
    return parser.parse_args()


def clean_directory(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def copy_assets(root: Path, destination: Path) -> None:
    source_assets = root / "assets"
    target_assets = destination / "assets"
    if not source_assets.exists():
        return
    if target_assets.exists():
        shutil.rmtree(target_assets)
    shutil.copytree(source_assets, target_assets)


def build_bundle(root: Path, csv_path: Path, business: str, pattern: str) -> Path:
    output_dir = root / pattern.format(business=business)
    clean_directory(output_dir)

    json_path = output_dir / "content.json"

    command = [
        sys.executable,
        str(root / "generate_pages.py"),
        str(csv_path),
        "--business",
        business,
        "--output",
        str(output_dir),
        "--json",
        str(json_path),
    ]
    subprocess.run(command, check=True)

    copy_assets(root, output_dir)
    return output_dir


def main() -> None:
    args = parse_args()
    root = Path(__file__).resolve().parent.parent
    csv_path = root / args.csv
    if not csv_path.exists():
        raise SystemExit(f"CSV source not found: {csv_path}")

    built_paths = []
    for target, pattern in TARGET_PATHS.items():
        built_paths.append((target, build_bundle(root, csv_path, args.business, pattern)))

    print("Generated cloud bundles:")
    for target, path in built_paths:
        print(f"  {target}: {path.resolve()}")


if __name__ == "__main__":
    main()
