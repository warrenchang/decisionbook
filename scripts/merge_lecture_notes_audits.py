#!/usr/bin/env python3
"""Merge independent Lecture Notes audits and verify exact file coverage.

The source directory is treated as immutable. The script validates source paths,
sizes, and SHA-256 hashes, reconciles overlapping audit assignments, and writes
one exact-path ledger plus a human-readable reconciliation report.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import sys
from collections import Counter, defaultdict
from pathlib import Path


FIELDS = [
    "source_path",
    "source_group",
    "format",
    "size_bytes",
    "sha256",
    "slides_or_pages",
    "hidden_slides",
    "notes_present",
    "duplicate_of",
    "role",
    "content_summary",
    "examples_activities",
    "quant_claims",
    "citations_urls",
    "visuals_rights",
    "current_destination",
    "gap_status",
    "recommended_destination",
    "disposition",
    "verification_notes",
]

IDENTITY_FIELDS = {"source_path", "format", "size_bytes", "sha256"}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def normalize_path(raw: str, source_root: Path) -> str:
    path = Path(raw)
    if path.is_absolute():
        try:
            path = path.relative_to(source_root)
        except ValueError as exc:
            raise ValueError(f"Audit path is outside source root: {raw}") from exc
    normalized = path.as_posix()
    while normalized.startswith("./"):
        normalized = normalized[2:]
    if not normalized or normalized.startswith("../"):
        raise ValueError(f"Invalid relative source path: {raw}")
    return normalized


def combine_text(values: list[str]) -> str:
    unique: list[str] = []
    for value in values:
        cleaned = value.strip()
        if cleaned and cleaned not in unique:
            unique.append(cleaned)
    if not unique:
        return ""
    if len(unique) == 1:
        return unique[0]
    return " || ADDITIONAL AUDIT: ".join(unique)


def load_audits(paths: list[Path], source_root: Path) -> tuple[dict[str, list[dict[str, str]]], list[str]]:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    errors: list[str] = []
    for audit_path in paths:
        with audit_path.open(newline="", encoding="utf-8-sig") as handle:
            reader = csv.DictReader(handle)
            if reader.fieldnames != FIELDS:
                errors.append(
                    f"{audit_path}: unexpected header; expected {FIELDS}, found {reader.fieldnames}"
                )
                continue
            for line_number, row in enumerate(reader, start=2):
                try:
                    row["source_path"] = normalize_path(row["source_path"], source_root)
                except ValueError as exc:
                    errors.append(f"{audit_path}:{line_number}: {exc}")
                    continue
                row["format"] = row["format"].strip().lower()
                row["_audit_file"] = audit_path.name
                grouped[row["source_path"]].append(row)
    return grouped, errors


def reconcile(rows_by_path: dict[str, list[dict[str, str]]]) -> tuple[list[dict[str, str]], list[str], int]:
    merged: list[dict[str, str]] = []
    errors: list[str] = []
    overlap_rows = 0
    for source_path in sorted(rows_by_path):
        rows = rows_by_path[source_path]
        overlap_rows += max(0, len(rows) - 1)
        result: dict[str, str] = {"source_path": source_path}
        for field in FIELDS[1:]:
            values = [row.get(field, "") for row in rows]
            nonempty = {value.strip() for value in values if value.strip()}
            if field in IDENTITY_FIELDS and len(nonempty) > 1:
                errors.append(f"{source_path}: conflicting {field}: {sorted(nonempty)}")
            result[field] = combine_text(values)
        if len(rows) > 1:
            auditors = ", ".join(sorted({row["_audit_file"] for row in rows}))
            overlap_note = f"Overlapping assignments reconciled from: {auditors}."
            result["verification_notes"] = combine_text(
                [result["verification_notes"], overlap_note]
            )
        merged.append(result)
    return merged, errors, overlap_rows


def verify_sources(
    rows: list[dict[str, str]], source_root: Path
) -> tuple[list[str], list[str], list[str], dict[str, list[str]]]:
    actual = sorted(
        path.relative_to(source_root).as_posix()
        for path in source_root.rglob("*")
        if path.is_file()
    )
    actual_set = set(actual)
    audited_set = {row["source_path"] for row in rows}
    missing = sorted(actual_set - audited_set)
    extras = sorted(audited_set - actual_set)
    errors: list[str] = []
    hash_groups: dict[str, list[str]] = defaultdict(list)

    for row in rows:
        rel = row["source_path"]
        if rel not in actual_set:
            continue
        path = source_root / rel
        actual_size = path.stat().st_size
        if row["size_bytes"]:
            try:
                audited_size = int(row["size_bytes"])
            except ValueError:
                errors.append(f"{rel}: invalid size_bytes {row['size_bytes']!r}")
            else:
                if audited_size != actual_size:
                    errors.append(
                        f"{rel}: size changed or audit mismatch ({audited_size} != {actual_size})"
                    )
        actual_hash = sha256(path)
        if row["sha256"] and row["sha256"] != actual_hash:
            errors.append(
                f"{rel}: SHA-256 changed or audit mismatch ({row['sha256']} != {actual_hash})"
            )
        if not row["size_bytes"]:
            row["size_bytes"] = str(actual_size)
        if not row["sha256"]:
            row["sha256"] = actual_hash
        hash_groups[actual_hash].append(rel)

    duplicate_groups = {
        digest: paths for digest, paths in hash_groups.items() if len(paths) > 1
    }
    return missing, extras, errors, duplicate_groups


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        writer.writerows({field: row.get(field, "") for field in FIELDS} for row in rows)


def md_escape(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def write_report(
    path: Path,
    rows: list[dict[str, str]],
    audit_paths: list[Path],
    raw_rows: int,
    overlap_rows: int,
    missing: list[str],
    extras: list[str],
    errors: list[str],
    duplicate_groups: dict[str, list[str]],
) -> None:
    format_counts = Counter(row["format"] or "unknown" for row in rows)
    group_counts = Counter(row["source_group"] or "ungrouped" for row in rows)
    disposition_counts = Counter(row["disposition"] or "unspecified" for row in rows)
    status = "PASS" if not missing and not extras and not errors else "FAIL"

    lines = [
        "# Lecture Notes audit reconciliation",
        "",
        f"**Status: {status}**",
        "",
        "## Coverage",
        "",
        f"- Independent audit ledgers: {len(audit_paths)}",
        f"- Raw audit rows: {raw_rows}",
        f"- Overlap rows reconciled: {overlap_rows}",
        f"- Unique source files represented: {len(rows)}",
        f"- Source files missing from audits: {len(missing)}",
        f"- Audit paths not present in the source folder: {len(extras)}",
        f"- Verification errors: {len(errors)}",
        "",
        "Each unique source path appears once in the merged CSV. Overlapping assignments are reconciled without counting a file twice. Source files are verified against current byte size and SHA-256; the source directory is not modified.",
        "",
        "## Input ledgers",
        "",
    ]
    lines.extend(f"- `{audit_path}`" for audit_path in audit_paths)

    lines.extend(["", "## Format counts", "", "| Format | Files |", "| --- | ---: |"])
    lines.extend(f"| {md_escape(name)} | {count} |" for name, count in sorted(format_counts.items()))

    lines.extend(["", "## Source-group counts", "", "| Source group | Files |", "| --- | ---: |"])
    lines.extend(
        f"| {md_escape(name)} | {count} |" for name, count in sorted(group_counts.items())
    )

    lines.extend(["", "## Exact duplicate groups", ""])
    if duplicate_groups:
        for digest, paths in sorted(duplicate_groups.items(), key=lambda item: item[1]):
            lines.append(f"- `{digest}`")
            lines.extend(f"  - `{item}`" for item in paths)
    else:
        lines.append("No byte-identical source files were found.")

    lines.extend(["", "## Verification exceptions", ""])
    if not missing and not extras and not errors:
        lines.append("None.")
    else:
        lines.extend(f"- Missing: `{item}`" for item in missing)
        lines.extend(f"- Extra: `{item}`" for item in extras)
        lines.extend(f"- Error: {item}" for item in errors)

    lines.extend(
        [
            "",
            "## Rights and integration rule",
            "",
            "The audit records mixed and uncertain rights in many legacy slide assets. The book may link to an external video, reproduce public-domain or appropriately licensed material with attribution, or create an original diagram/table from verified facts or data. Cosmetic modification is not treated as a copyright workaround. Journal-result images and simulation screenshots are redrawn or independently regenerated only when their underlying values, model, parameters, and provenance can be verified.",
            "",
            "## Exact-path ledger",
            "",
            "The full twenty-field ledger is `audits/lecture-notes-coverage.csv`. The compact table below supports visual inspection; it does not replace the CSV.",
            "",
            "| # | Source path | Format | Role | Recommended destination |",
            "| ---: | --- | --- | --- | --- |",
        ]
    )
    for index, row in enumerate(rows, start=1):
        lines.append(
            "| "
            + " | ".join(
                [
                    str(index),
                    f"`{md_escape(row['source_path'])}`",
                    md_escape(row["format"]),
                    md_escape(row["role"]),
                    md_escape(row["recommended_destination"]),
                ]
            )
            + " |"
        )

    lines.extend(["", "## Disposition summary", ""])
    for disposition, count in disposition_counts.most_common():
        lines.append(f"- {count}: {disposition}")

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-root", type=Path, required=True)
    parser.add_argument("--audit", type=Path, action="append", required=True)
    parser.add_argument(
        "--output-csv", type=Path, default=Path("audits/lecture-notes-coverage.csv")
    )
    parser.add_argument(
        "--output-report",
        type=Path,
        default=Path("audits/lecture-notes-audit-reconciliation.md"),
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    source_root = args.source_root.resolve()
    audit_paths = [path.resolve() for path in args.audit]
    grouped, load_errors = load_audits(audit_paths, source_root)
    raw_rows = sum(len(rows) for rows in grouped.values())
    rows, reconcile_errors, overlap_rows = reconcile(grouped)
    missing, extras, verify_errors, duplicates = verify_sources(rows, source_root)
    errors = load_errors + reconcile_errors + verify_errors
    write_csv(args.output_csv, rows)
    write_report(
        args.output_report,
        rows,
        audit_paths,
        raw_rows,
        overlap_rows,
        missing,
        extras,
        errors,
        duplicates,
    )
    print(
        f"Merged {raw_rows} rows into {len(rows)} unique source paths; "
        f"missing={len(missing)} extras={len(extras)} errors={len(errors)}"
    )
    return 0 if not missing and not extras and not errors else 1


if __name__ == "__main__":
    sys.exit(main())
