#!/usr/bin/env python3
"""Build pipeline: CSV -> JSON -> generated HTML pages."""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path


def ensure_paths(root: Path) -> None:
    csv_path = root / "content" / "content-template.csv"
    if not csv_path.exists():
        raise SystemExit(f"Missing CSV source: {csv_path}")


def run_generator(root: Path) -> None:
    output_dir = root / "generated-pages"
    json_path = root / "build" / "content.json"

    if output_dir.exists():
        shutil.rmtree(output_dir)
    if json_path.exists():
        json_path.unlink()

    output_dir.mkdir(parents=True, exist_ok=True)
    json_path.parent.mkdir(parents=True, exist_ok=True)

    command = [
        sys.executable,
        str(root / "generate_pages.py"),
        str(root / "content" / "content-template.csv"),
        "--output",
        str(output_dir),
        "--json",
        str(json_path),
    ]
    subprocess.run(command, check=True)


def main() -> None:
    root = Path(__file__).resolve().parent.parent
    ensure_paths(root)
    run_generator(root)
    print("Static content regenerated:")
    print(f"  HTML directory: {(root / 'generated-pages').resolve()}")
    print(f"  JSON file: {(root / 'build' / 'content.json').resolve()}")


if __name__ == "__main__":
    main()
