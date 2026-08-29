#!/usr/bin/env python3
"""Normalize EPUB navigation to a compact Part -> Chapter hierarchy.

Quarto/Pandoc writes Part pages and numbered chapters as sibling navigation
items. This postprocessor nests each numbered chapter below its Part, drops
section-level navigation and the redundant generated title-page entry, and
suppresses automatic ordered-list counters in the visible contents page. The
XHTML navigation document and EPUB 2 NCX are updated together. The operation
is idempotent so the HTML post-render hook can safely encounter an
already-normalized staged EPUB.
"""

from __future__ import annotations

import copy
import re
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


XHTML = "http://www.w3.org/1999/xhtml"
EPUB_NS = "http://www.idpf.org/2007/ops"
NCX = "http://www.daisy.org/z3986/2005/ncx/"

PART_RE = re.compile(r"^Part\s+[IVXLCDM]+\.")
CHAPTER_RE = re.compile(r"^(\d+)\s+")


def normalized_text(element: ET.Element | None) -> str:
    if element is None:
        return ""
    return " ".join("".join(element.itertext()).split())


def direct_child(element: ET.Element, tag: str) -> ET.Element | None:
    return next((child for child in element if child.tag == tag), None)


def strip_direct_children(element: ET.Element, tag: str) -> list[ET.Element]:
    removed = [child for child in list(element) if child.tag == tag]
    for child in removed:
        element.remove(child)
    return removed


def add_style(element: ET.Element, declaration: str) -> None:
    """Add an inline CSS declaration once, preserving any existing styles."""
    existing = element.get("style", "").strip()
    if declaration in existing:
        return
    separator = " " if existing and existing.endswith(";") else "; " if existing else ""
    element.set("style", f"{existing}{separator}{declaration}")


def nav_label(item: ET.Element) -> str:
    anchor = direct_child(item, f"{{{XHTML}}}a")
    span = direct_child(item, f"{{{XHTML}}}span")
    return normalized_text(anchor if anchor is not None else span)


def is_nav_title_page(item: ET.Element, book_title: str) -> bool:
    anchor = direct_child(item, f"{{{XHTML}}}a")
    href = anchor.get("href", "") if anchor is not None else ""
    return nav_label(item) == book_title and href.split("#", 1)[0].endswith("title_page.xhtml")


def nested_nav_chapters(item: ET.Element) -> list[ET.Element]:
    chapters: list[ET.Element] = []
    for ordered in [child for child in item if child.tag == f"{{{XHTML}}}ol"]:
        for nested in list(ordered):
            if nested.tag == f"{{{XHTML}}}li" and CHAPTER_RE.match(nav_label(nested)):
                chapters.append(nested)
    return chapters


def normalize_nav(data: bytes) -> tuple[bytes, list[str], list[str]]:
    ET.register_namespace("", XHTML)
    ET.register_namespace("epub", EPUB_NS)
    root = ET.fromstring(data)
    toc = next(
        (
            element
            for element in root.findall(f".//{{{XHTML}}}nav")
            if element.get(f"{{{EPUB_NS}}}type") == "toc"
        ),
        None,
    )
    if toc is None:
        raise ValueError("EPUB navigation document has no toc nav")
    ordered = direct_child(toc, f"{{{XHTML}}}ol")
    if ordered is None:
        raise ValueError("EPUB navigation toc has no ordered list")

    book_title = normalized_text(root.find(f"{{{XHTML}}}head/{{{XHTML}}}title"))

    original = [child for child in list(ordered) if child.tag == f"{{{XHTML}}}li"]
    for item in original:
        ordered.remove(item)

    part_labels: list[str] = []
    chapter_labels: list[str] = []
    current_part_list: ET.Element | None = None

    for item in original:
        label = nav_label(item)
        if is_nav_title_page(item, book_title):
            continue
        carried_chapters = nested_nav_chapters(item) if PART_RE.match(label) else []
        strip_direct_children(item, f"{{{XHTML}}}ol")

        if PART_RE.match(label):
            ordered.append(item)
            current_part_list = ET.SubElement(item, f"{{{XHTML}}}ol")
            part_labels.append(label)
            for chapter in carried_chapters:
                strip_direct_children(chapter, f"{{{XHTML}}}ol")
                current_part_list.append(chapter)
                chapter_labels.append(nav_label(chapter))
        elif CHAPTER_RE.match(label) and current_part_list is not None:
            current_part_list.append(item)
            chapter_labels.append(label)
        else:
            ordered.append(item)
            current_part_list = None

    # Some reading systems ignore an EPUB's external stylesheet when they
    # display nav.xhtml. Inline declarations prevent those systems from adding
    # their own 1., 2., 3. counters before labels that already contain chapter
    # numbers. Keep indentation; remove only the list markers.
    for element in toc.iter():
        if element.tag in (f"{{{XHTML}}}ol", f"{{{XHTML}}}li"):
            add_style(element, "list-style-type: none !important;")

    ET.indent(root, space="  ")
    return ET.tostring(root, encoding="utf-8", xml_declaration=True), part_labels, chapter_labels


def ncx_label(item: ET.Element) -> str:
    return normalized_text(item.find(f"{{{NCX}}}navLabel/{{{NCX}}}text"))


def nested_ncx_chapters(item: ET.Element) -> list[ET.Element]:
    return [
        child
        for child in item
        if child.tag == f"{{{NCX}}}navPoint" and CHAPTER_RE.match(ncx_label(child))
    ]


def is_ncx_title_page(item: ET.Element, book_title: str) -> bool:
    content = direct_child(item, f"{{{NCX}}}content")
    src = content.get("src", "") if content is not None else ""
    return ncx_label(item) == book_title and src.split("#", 1)[0].endswith("title_page.xhtml")


def normalize_ncx(data: bytes) -> bytes:
    ET.register_namespace("", NCX)
    root = ET.fromstring(data)
    nav_map = root.find(f"{{{NCX}}}navMap")
    if nav_map is None:
        raise ValueError("EPUB NCX has no navMap")

    book_title = normalized_text(root.find(f"{{{NCX}}}docTitle/{{{NCX}}}text"))

    original = [child for child in list(nav_map) if child.tag == f"{{{NCX}}}navPoint"]
    for item in original:
        nav_map.remove(item)

    current_part: ET.Element | None = None
    for item in original:
        label = ncx_label(item)
        if is_ncx_title_page(item, book_title):
            continue
        carried_chapters = nested_ncx_chapters(item) if PART_RE.match(label) else []
        strip_direct_children(item, f"{{{NCX}}}navPoint")

        if PART_RE.match(label):
            nav_map.append(item)
            current_part = item
            for chapter in carried_chapters:
                strip_direct_children(chapter, f"{{{NCX}}}navPoint")
                current_part.append(chapter)
        elif CHAPTER_RE.match(label) and current_part is not None:
            current_part.append(item)
        else:
            nav_map.append(item)
            current_part = None

    depth = root.find(f"{{{NCX}}}head/{{{NCX}}}meta[@name='dtb:depth']")
    if depth is not None:
        depth.set("content", "2")

    for position, item in enumerate(nav_map.iter(f"{{{NCX}}}navPoint"), start=1):
        item.set("id", f"navPoint-{position}")
        if "playOrder" in item.attrib:
            item.set("playOrder", str(position))

    ET.indent(root, space="  ")
    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


def normalize_epub(path: Path) -> tuple[int, int]:
    if not path.is_file():
        raise FileNotFoundError(path)

    with zipfile.ZipFile(path) as source:
        entries = [(copy.copy(info), source.read(info.filename)) for info in source.infolist()]

    by_name = {info.filename: index for index, (info, _data) in enumerate(entries)}
    for required in ("mimetype", "EPUB/nav.xhtml", "EPUB/toc.ncx"):
        if required not in by_name:
            raise ValueError(f"EPUB is missing {required}")

    nav_data, parts, chapters = normalize_nav(entries[by_name["EPUB/nav.xhtml"]][1])
    ncx_data = normalize_ncx(entries[by_name["EPUB/toc.ncx"]][1])
    entries[by_name["EPUB/nav.xhtml"]] = (entries[by_name["EPUB/nav.xhtml"]][0], nav_data)
    entries[by_name["EPUB/toc.ncx"]] = (entries[by_name["EPUB/toc.ncx"]][0], ncx_data)

    chapter_numbers = [int(match.group(1)) for label in chapters if (match := CHAPTER_RE.match(label))]
    if len(parts) != 10 or chapter_numbers != list(range(1, 49)):
        raise ValueError(
            f"Unexpected book hierarchy: {len(parts)} Parts and chapter numbers {chapter_numbers}"
        )

    temporary = path.with_name(f".{path.name}.tmp")
    with zipfile.ZipFile(temporary, "w") as target:
        mimetype_info, mimetype_data = entries[by_name["mimetype"]]
        mimetype_info.compress_type = zipfile.ZIP_STORED
        target.writestr(mimetype_info, mimetype_data)
        for info, data in entries:
            if info.filename == "mimetype":
                continue
            target.writestr(info, data)
    temporary.replace(path)
    return len(parts), len(chapters)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("epub", type=Path)
    arguments = parser.parse_args()
    part_count, chapter_count = normalize_epub(arguments.epub)
    print(f"Normalized EPUB navigation: {part_count} Parts, {chapter_count} numbered chapters")
