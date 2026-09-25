#!/usr/bin/env python3
"""Match canonical chapter filenames to configured numbers and current H1 titles.

Preview by default; pass --apply to rename sources, update active references,
and retain old public URLs as Quarto aliases. Historical audit records and
the earlier one-time migration script are deliberately left unchanged.
"""

from __future__ import annotations

import argparse
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHAPTER = re.compile(r"^\s*-\s+(chapters/\S+\.qmd)\s*$", re.M)
H1 = re.compile(r"^#\s+(.+?)(?:\s+\{[^}]+\})?\s*$", re.M)
TEXT_SUFFIXES = {".qmd", ".md", ".yml", ".yaml", ".py", ".js", ".cjs", ".json", ".lua", ".scss", ".css", ".sh", ".toml"}


def plan() -> list[dict]:
    paths = CHAPTER.findall((ROOT / "_quarto-html.yml").read_text())
    if paths != CHAPTER.findall((ROOT / "_quarto-epub.yml").read_text()):
        raise ValueError("HTML and EPUB chapter orders differ.")
    rows = []
    for number, source in enumerate(paths, 1):
        text = (ROOT / source).read_text()
        match = H1.search(text)
        if not match:
            raise ValueError(f"Missing chapter title: {source}")
        title = match.group(1)
        slug = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode().lower()
        slug = re.sub(r"[^a-z0-9]+", "-", slug.replace("&", " and ")).strip("-")
        target = f"chapters/{number:02d}-{slug}.qmd"
        rows.append(dict(number=number, title=title, old=source, new=target))
    targets = [row["new"] for row in rows]
    if len(set(targets)) != len(targets):
        raise ValueError("Duplicate destination names.")
    for row in rows:
        if row["old"] != row["new"] and (ROOT / row["new"]).exists():
            raise ValueError(f"Destination already exists: {row['new']}")
    return rows


def active_files() -> list[Path]:
    files = list(ROOT.iterdir())
    for folder in ("chapters", "parts", "appendices", "scripts", "filters", ".github"):
        files.extend((ROOT / folder).rglob("*"))
    excluded = {Path(__file__).resolve(), ROOT / "scripts/rename_chapter_files.py"}
    return sorted(p for p in files if p.is_file() and p.suffix in TEXT_SUFFIXES and p not in excluded
                  and not (p.parent == ROOT and p.suffix == ".json")
                  and not (p.parent.name in {"chapters", "parts"} and p.suffix == ".md"))


def replace_paths(text: str, pattern: re.Pattern, replacements: dict) -> str:
    # Alias paths must remain historical URLs; section anchors are untouched.
    def replace(match: re.Match) -> str:
        return replacements[match.group(0)]
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            front = text[:end]
            parts = re.split(r"(^aliases:\s*\n(?:[ \t]+.*\n?)*)", front, flags=re.M)
            front = "".join(part if part.startswith("aliases:") else pattern.sub(replace, part) for part in parts)
            return front + pattern.sub(replace, text[end:])
    return pattern.sub(replace, text)


def add_alias(text: str, alias: str) -> str:
    if text.startswith("---\n"):
        end = text.index("\n---", 4)
        front = text[:end]
        if re.search(rf"^\s+-\s+{re.escape(alias)}\s*$", front, re.M):
            return text
        if re.search(r"^aliases:\s*$", front, re.M):
            front = re.sub(r"^aliases:\s*$", f"aliases:\n  - {alias}", front, count=1, flags=re.M)
        else:
            front += f"\naliases:\n  - {alias}"
        return front + text[end:]
    return f"---\naliases:\n  - {alias}\n---\n\n" + text


def remove_self_alias(text: str, canonical_name: str) -> str:
    """A restored filename is a page again, not a redirect to itself."""
    if not text.startswith("---\n"):
        return text
    end = text.index("\n---", 4)
    front = text[:end]
    pattern = re.compile(r"(^aliases:[ \t]*\n(?:[ \t]+.*(?:\n|$))*)", re.M)

    def clean(match: re.Match) -> str:
        lines = match.group(0).splitlines(keepends=True)
        return "".join(line for line in lines if line.strip() != f"- {canonical_name}")

    return pattern.sub(clean, front) + text[end:]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--record", type=Path, help="Write this migration's filename map as JSON")
    args = parser.parse_args()
    rows = plan()
    changed = [row for row in rows if row["old"] != row["new"]]
    for row in changed:
        print(f"{row['old']} -> {row['new']}")
    print(f"{len(changed)} of {len(rows)} chapter filenames need updating.")
    if not args.apply or not changed:
        return
    replacements = {}
    for row in changed:
        for suffix in (".qmd", ".html"):
            replacements[Path(row["old"]).with_suffix(suffix).name] = Path(row["new"]).with_suffix(suffix).name
    pattern = re.compile("|".join(re.escape(s) for s in sorted(replacements, key=len, reverse=True)))
    # Compute all new text before making any filesystem changes.
    updates = {}
    for path in active_files():
        old = path.read_text()
        new = replace_paths(old, pattern, replacements)
        if old != new:
            updates[path] = new
    for row in changed:
        path = ROOT / row["old"]
        updated = add_alias(updates.get(path, path.read_text()), Path(row["old"]).with_suffix(".html").name)
        updates[path] = remove_self_alias(updated, Path(row["new"]).with_suffix(".html").name)
    for path, text in updates.items():
        path.write_text(text)
    for row in changed:
        (ROOT / row["old"]).rename(ROOT / row["new"])
    if args.record:
        args.record.parent.mkdir(parents=True, exist_ok=True)
        args.record.write_text(json.dumps({"chapters": rows, "updated_files": [str(p.relative_to(ROOT)) for p in updates]}, indent=2) + "\n")
    print(f"Updated {len(updates)} active files. Existing URL aliases preserved.")


if __name__ == "__main__":
    main()
