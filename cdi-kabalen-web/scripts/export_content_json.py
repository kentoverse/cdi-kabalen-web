#!/usr/bin/env python3
"""Export CSV-authored content to JSON without generating HTML."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Export site content to JSON for developer tooling.")
    parser.add_argument(
        "--csv",
        default="content/content-template.csv",
        help="Path to the CSV source authored by non-technical editors (default: content/content-template.csv).",
    )
    parser.add_argument(
        "--business",
        default="kabalian",
        help="Business identifier to export (default: kabalian).",
    )
    parser.add_argument(
        "--output",
        default="content/content-template.json",
        help="Destination JSON file (default: content/content-template.json).",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    root = Path(__file__).resolve().parent.parent
    csv_path = root / args.csv
    if not csv_path.exists():
        raise SystemExit(f"CSV source not found: {csv_path}")

    output_path = root / args.output
    output_path.parent.mkdir(parents=True, exist_ok=True)

    command = [
        sys.executable,
        str(root / "generate_pages.py"),
        str(csv_path),
        "--business",
        args.business,
        "--json",
        str(output_path),
        "--no-html",
    ]

    subprocess.run(command, check=True)


if __name__ == "__main__":
    main()
