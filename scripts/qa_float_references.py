#!/usr/bin/env python3
"""Check local prose references for every teaching figure and table in the book.

This is a coverage screen, not a judgment of explanatory quality. Captions,
alternative text, table cells, and examples inside code fences do not satisfy
the body-reference requirement. Keep the per-item editorial review alongside it.
"""

from __future__ import annotations

import argparse
from collections import Counter
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SOURCE_LINE = re.compile(r"^\s*-\s+(?:part:\s+)?([^\s]+\.qmd)\s*$", re.M)
LABEL = re.compile(r"(?:\{[^}\n]*#|<[^>\n]*\bid=[\"'])((?:fig|tbl)-[\w-]+)")
REFERENCE = re.compile(r"(?<![\w\\])@((?:fig|tbl)-[\w-]+)")
LEGACY = re.compile(r"^\s*\[\]\{#((?:fig|tbl)-[\w-]+)\}\s*$")
SEPARATOR = re.compile(r"\s*\|?\s*:?-{3,}:?\s*(?:\|\s*:?-{3,}:?\s*)+\|?\s*")
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}


def source_inventory(path: Path, root: Path = ROOT) -> tuple[list[dict], list[dict], list[str]]:
    text = re.sub(r"<!--.*?-->", "", path.read_text(), flags=re.S)
    lines = text.splitlines()
    definitions, legacy, body = [], [], []
    issues = []
    fence = None
    yaml = bool(lines and lines[0].strip() == "---")
    ordinary = []
    for index, line in enumerate(lines):
        if yaml:
            if index and line.strip() == "---":
                yaml = False
            ordinary.append(False)
            continue
        marker = re.match(r"^\s*(`{3,}|~{3,})", line)
        if marker:
            token = marker.group(1)[0]
            fence = None if fence == token else token if fence is None else fence
            ordinary.append(False)
            continue
        # Raw HTML can define a float, but references in a code block do not count.
        old = LEGACY.fullmatch(line)
        if old:
            legacy.append({"file": str(path.relative_to(root)), "id": old.group(1), "line": index + 1})
        else:
            for label in LABEL.findall(line):
                definitions.append({"file": str(path.relative_to(root)), "id": label, "type": label[:3], "line": index + 1})
        is_body = not fence and not re.match(r"^\s*(?:!\[|\||:|#|<|\[\]\{)", line)
        ordinary.append(not fence)
        if is_body:
            body.extend({"id": label, "line": index + 1, "text": line.strip()} for label in REFERENCE.findall(line))
        if not fence and line.lstrip().startswith("![") and "#fig-" not in line:
            if "huanren-warren-zhang-profile.png" not in line:
                issues.append(f"{path.relative_to(root)}:{index + 1}: unnumbered teaching image")
    for index, line in enumerate(lines):
        if not ordinary[index] or not SEPARATOR.fullmatch(line):
            continue
        end = index + 1
        while end < len(lines) and lines[end].strip().startswith("|"):
            end += 1
        caption = "\n".join(lines[end:end + 4])
        wrapper = "\n".join(lines[max(0, index - 4):index])
        if "#tbl-" not in caption and "#tbl-" not in wrapper:
            issues.append(f"{path.relative_to(root)}:{index + 1}: table lacks a numbered caption or wrapper")
    for item in definitions:
        item["body_references"] = [entry for entry in body if entry["id"] == item["id"]]
        item["status"] = "PASS" if item["body_references"] else "MISSING_BODY_REFERENCE"
        if not item["body_references"]:
            issues.append(f"{item['file']}:{item['line']}: {item['id']} has no local prose reference")
    return definitions, legacy, issues


class RenderedFloats(HTMLParser):
    """Read the rendered floats and references outside tables and captions."""

    def __init__(self, body_is_main: bool = False) -> None:
        super().__init__()
        self.body_is_main = body_is_main
        self.stack = []
        self.floats = set()
        self.references = []
        self.unnumbered_tables = 0
        self.unresolved = []

    def handle_starttag(self, tag, attrs):
        attr = dict(attrs)
        parent_main = any(entry[1] for entry in self.stack)
        main = parent_main or tag == "main" or (tag == "body" and self.body_is_main)
        excluded = any(entry[2] for entry in self.stack) or tag in {"figcaption", "caption", "table", "nav", "pre", "code"}
        identifier = attr.get("id", "")
        classes = attr.get("class", "").split()
        is_float = "quarto-float" in classes and re.fullmatch(r"(?:fig|tbl)-[\w-]+", identifier)
        if main and is_float:
            self.floats.add(identifier)
        if main and tag == "table" and not any(entry[3].startswith("tbl-") for entry in self.stack):
            self.unnumbered_tables += 1
        if main and tag == "a" and not excluded and "quarto-xref" in classes:
            self.references.append(attr.get("href", ""))
        if main and "quarto-unresolved-ref" in classes:
            self.unresolved.append(identifier or tag)
        if tag not in VOID:
            self.stack.append((tag, main, excluded, identifier))

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, -1, -1):
            if self.stack[index][0] == tag:
                del self.stack[index:]
                break


def audit(root: Path = ROOT, rendered: bool = False, epub_dir: Path | None = None) -> dict:
    files = list(dict.fromkeys(SOURCE_LINE.findall((root / "_quarto-html.yml").read_text())))
    items, legacy, issues, destinations = [], [], [], []
    for source in files:
        definitions, anchors, source_issues = source_inventory(root / source, root)
        items.extend(definitions)
        legacy.extend(anchors)
        issues.extend(source_issues)
        if rendered:
            target = root / "docs" / Path(source).with_suffix(".html")
            if not target.exists():
                issues.append(f"Missing rendered page: {target.relative_to(root)}")
                continue
            page = RenderedFloats()
            page.feed(target.read_text())
            local = {unquote(urlsplit(href).fragment) for href in page.references if not urlsplit(href).path or Path(urlsplit(href).path).name == target.name}
            missing = sorted(page.floats - local)
            destinations.append({"file": str(target.relative_to(root)), "float_count": len(page.floats), "missing_local_body_references": missing, "unnumbered_tables": page.unnumbered_tables, "unresolved_references": page.unresolved})
            issues.extend(f"{source}: rendered float {label} lacks local prose link" for label in missing)
            if page.unnumbered_tables or page.unresolved:
                issues.append(f"{source}: {page.unnumbered_tables} unnumbered rendered tables; {len(page.unresolved)} unresolved references")
    epub_pages = []
    if epub_dir is not None:
        pages = sorted(epub_dir.rglob("*.xhtml"))
        if not pages:
            issues.append(f"No EPUB XHTML pages found in {epub_dir}")
        for target in pages:
            page = RenderedFloats(body_is_main=True)
            page.feed(target.read_text())
            local = {unquote(urlsplit(href).fragment) for href in page.references if not urlsplit(href).path or Path(urlsplit(href).path).name == target.name}
            missing = sorted(page.floats - local)
            epub_pages.append({"file": str(target.relative_to(epub_dir)), "float_count": len(page.floats), "missing_local_body_references": missing, "unnumbered_tables": page.unnumbered_tables, "unresolved_references": page.unresolved})
            issues.extend(f"EPUB/{target.name}: rendered float {label} lacks local prose link" for label in missing)
            if page.unnumbered_tables or page.unresolved:
                issues.append(f"EPUB/{target.name}: {page.unnumbered_tables} unnumbered tables; {len(page.unresolved)} unresolved references")
    duplicates = [key for key, count in Counter(item["id"] for item in items).items() if count > 1]
    issues.extend(f"Duplicate float identifier: {key}" for key in duplicates)
    return {"status": "FAIL" if issues else "PASS", "scope": "all configured book sources", "sources": len(files), "counts": dict(Counter(item["type"] for item in items)), "floats": items, "legacy_anchors": legacy, "rendered": destinations, "epub": epub_pages, "issues": issues, "limit": "Checks reference coverage. Meaningful explanation requires the accompanying editorial review."}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rendered", action="store_true", help="also check final HTML floats and prose links")
    parser.add_argument("--epub-dir", type=Path, help="also check XHTML in an extracted final EPUB")
    parser.add_argument("--output", type=Path, default=ROOT / "audits" / "float-reference-qa.json")
    args = parser.parse_args()
    result = audit(rendered=args.rendered, epub_dir=args.epub_dir)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(f"{result['status']}: {result['sources']} sources; {result['counts']}; {len(result['issues'])} issue(s)")
    for issue in result["issues"]:
        print(issue)
    raise SystemExit(bool(result["issues"]))
