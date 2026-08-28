#!/usr/bin/env python3
"""Merge reviewed slide-image ledger segments in raw-inventory order."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "audits" / "slide-images-raw" / "slide-image-occurrences.csv"
OUTPUT = ROOT / "audits" / "slide-images-reviewed.csv"


def read_rows(path: Path) -> tuple[list[dict[str, str]], list[str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return list(reader), list(reader.fieldnames or [])


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("segments", nargs="+", type=Path)
    parser.add_argument("--raw", type=Path, default=RAW)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()

    raw_rows, _ = read_rows(args.raw)
    reviewed: dict[str, dict[str, str]] = {}
    fields: list[str] | None = None

    for segment in args.segments:
        rows, segment_fields = read_rows(segment)
        if fields is None:
            fields = segment_fields
        elif segment_fields != fields:
            raise SystemExit(f"Ledger headers differ: {segment}")
        for row in rows:
            occurrence_id = row.get("occurrence_id", "")
            if not occurrence_id:
                raise SystemExit(f"Ledger row lacks occurrence_id: {segment}")
            if occurrence_id in reviewed:
                raise SystemExit(f"Duplicate occurrence_id across segments: {occurrence_id}")
            reviewed[occurrence_id] = row

    raw_ids = [row["occurrence_id"] for row in raw_rows]
    missing = [occurrence_id for occurrence_id in raw_ids if occurrence_id not in reviewed]
    extra = sorted(set(reviewed) - set(raw_ids))
    if missing or extra:
        raise SystemExit(
            f"Cannot merge: {len(missing)} raw occurrence(s) missing and "
            f"{len(extra)} unknown occurrence(s) supplied."
        )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(reviewed[occurrence_id] for occurrence_id in raw_ids)

    print(f"Wrote {len(raw_ids)} reviewed occurrences to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
