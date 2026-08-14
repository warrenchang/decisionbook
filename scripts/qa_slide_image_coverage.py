#!/usr/bin/env python3
"""Validate that every raw slide-image occurrence has a reviewed disposition."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "audits" / "slide-images-raw" / "slide-image-occurrences.csv"
REVIEWED = ROOT / "audits" / "slide-images-reviewed.csv"
SUMMARY = ROOT / "audits" / "slide-images-reviewed-summary.json"

REQUIRED = {
    "occurrence_id",
    "deck",
    "slide_number",
    "hidden_slide",
    "object_id",
    "object_name",
    "sha256",
    "duplicate_group",
    "role",
    "provenance",
    "rights_status",
    "treatment",
    "destination",
    "status",
    "notes",
}

ALLOWED_ROLES = {"substantive", "decorative", "administrative", "duplicate", "empty-or-broken"}
ALLOWED_RIGHTS = {
    "author-owned",
    "public-domain",
    "open-license",
    "facts-or-data-only",
    "protected",
    "unclear",
    "not-applicable",
}
ALLOWED_TREATMENTS = {
    "embedded-author-owned",
    "embedded-public-domain",
    "embedded-open-license",
    "redrawn-data",
    "redrawn-concept",
    "original-replacement",
    "linked-original",
    "represented-in-existing-book-visual",
    "represented-in-text-or-activity",
    "duplicate-accounted",
    "decorative-omitted",
    "administrative-omitted",
    "empty-or-broken-omitted",
    "rights-blocked-omitted",
}
ALLOWED_STATUS = {"complete", "accounted"}
EMBEDDED = {"embedded-author-owned", "embedded-public-domain", "embedded-open-license"}
EMBED_RIGHTS = {"author-owned", "public-domain", "open-license"}
NON_SUBSTANTIVE_TREATMENTS = {
    "duplicate": {"duplicate-accounted"},
    "decorative": {"decorative-omitted", "duplicate-accounted"},
    "administrative": {"administrative-omitted", "duplicate-accounted"},
    "empty-or-broken": {"empty-or-broken-omitted", "duplicate-accounted"},
}


def read_csv(path: Path) -> tuple[list[dict[str, str]], set[str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return list(reader), set(reader.fieldnames or [])


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--raw", type=Path, default=RAW)
    parser.add_argument("--reviewed", type=Path, default=REVIEWED)
    parser.add_argument("--summary", type=Path, default=SUMMARY)
    args = parser.parse_args()

    errors: list[str] = []
    raw_rows, raw_fields = read_csv(args.raw)
    reviewed_rows, reviewed_fields = read_csv(args.reviewed)
    missing_fields = sorted(REQUIRED - reviewed_fields)
    if missing_fields:
        errors.append(f"Reviewed ledger lacks required columns: {', '.join(missing_fields)}")

    raw_by_id = {row["occurrence_id"]: row for row in raw_rows}
    reviewed_ids = [row.get("occurrence_id", "") for row in reviewed_rows]
    reviewed_by_id = {row.get("occurrence_id", ""): row for row in reviewed_rows if row.get("occurrence_id")}
    duplicates = sorted(value for value, count in Counter(reviewed_ids).items() if value and count > 1)
    missing = sorted(set(raw_by_id) - set(reviewed_by_id))
    extra = sorted(set(reviewed_by_id) - set(raw_by_id))
    if duplicates:
        errors.append(f"Duplicate reviewed occurrence IDs: {', '.join(duplicates[:10])}")
    if missing:
        errors.append(f"Missing reviewed occurrence IDs ({len(missing)}): {', '.join(missing[:10])}")
    if extra:
        errors.append(f"Unknown reviewed occurrence IDs ({len(extra)}): {', '.join(extra[:10])}")

    for occurrence_id, row in reviewed_by_id.items():
        raw = raw_by_id.get(occurrence_id)
        if not raw:
            continue
        for field in ("deck", "slide_number", "hidden_slide", "object_id", "sha256", "duplicate_group"):
            if row.get(field, "") != raw.get(field, ""):
                errors.append(f"{occurrence_id}: reviewed {field!r} does not match raw inventory.")
        for field in ("role", "rights_status", "treatment", "status"):
            if not row.get(field, "").strip():
                errors.append(f"{occurrence_id}: missing {field}.")
        if row.get("role") not in ALLOWED_ROLES:
            errors.append(f"{occurrence_id}: unsupported role {row.get('role')!r}.")
        if row.get("rights_status") not in ALLOWED_RIGHTS:
            errors.append(f"{occurrence_id}: unsupported rights_status {row.get('rights_status')!r}.")
        if row.get("treatment") not in ALLOWED_TREATMENTS:
            errors.append(f"{occurrence_id}: unsupported treatment {row.get('treatment')!r}.")
        if row.get("status") not in ALLOWED_STATUS:
            errors.append(f"{occurrence_id}: unsupported status {row.get('status')!r}.")
        if row.get("treatment") in EMBEDDED and row.get("rights_status") not in EMBED_RIGHTS:
            errors.append(f"{occurrence_id}: embedded treatment lacks a reusable rights status.")
        if row.get("treatment") == "redrawn-data" and row.get("rights_status") != "facts-or-data-only":
            errors.append(f"{occurrence_id}: redrawn-data must be classified as facts-or-data-only.")
        if row.get("role") == "substantive" and not row.get("destination", "").strip():
            errors.append(f"{occurrence_id}: substantive image lacks a destination or linked treatment location.")
        allowed_for_role = NON_SUBSTANTIVE_TREATMENTS.get(row.get("role", ""))
        if allowed_for_role is not None and row.get("treatment") not in allowed_for_role:
            errors.append(
                f"{occurrence_id}: role {row.get('role')!r} is inconsistent with treatment {row.get('treatment')!r}."
            )
        if row.get("role") == "substantive" and row.get("treatment") in {
            "duplicate-accounted",
            "decorative-omitted",
            "administrative-omitted",
            "empty-or-broken-omitted",
        }:
            errors.append(f"{occurrence_id}: substantive role has a non-substantive treatment.")
        if row.get("rights_status") in {"protected", "unclear"} and row.get("treatment") in EMBEDDED:
            errors.append(f"{occurrence_id}: protected/unclear source must not be embedded.")

    summary = {
        "raw_occurrences": len(raw_rows),
        "reviewed_occurrences": len(reviewed_rows),
        "exact_occurrence_coverage": not missing and not extra and not duplicates,
        "by_deck": dict(sorted(Counter(row.get("deck", "") for row in reviewed_rows).items())),
        "by_role": dict(sorted(Counter(row.get("role", "") for row in reviewed_rows).items())),
        "by_rights_status": dict(sorted(Counter(row.get("rights_status", "") for row in reviewed_rows).items())),
        "by_treatment": dict(sorted(Counter(row.get("treatment", "") for row in reviewed_rows).items())),
        "by_status": dict(sorted(Counter(row.get("status", "") for row in reviewed_rows).items())),
        "errors": errors,
    }
    args.summary.parent.mkdir(parents=True, exist_ok=True)
    args.summary.write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    if errors:
        print(f"FAIL: {len(errors)} slide-image coverage error(s).")
        for error in errors[:40]:
            print(f"- {error}")
        return 1
    print(f"PASS: all {len(raw_rows)} slide-image occurrences have valid reviewed dispositions.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
