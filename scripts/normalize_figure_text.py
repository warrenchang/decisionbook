#!/usr/bin/env python3
"""Normalize text layout in the book's generated SVG diagrams.

The original figure builder centered every label independently.  Boxes that
contained more than a title and subtitle consequently acquired overlapping
text, and literal newlines in SVG ``text`` elements did not create visual line
breaks.  This script treats all direct text labels inside a generated box as a
single vertical stack, wraps them to the available width, and emits explicit
``tspan`` lines.

The three hand-authored decision-model diagrams use icon-aware placement and
are intentionally excluded; they are maintained directly in their SVG source.
"""

from __future__ import annotations

import argparse
import math
import re
import textwrap
import xml.etree.ElementTree as ET
from pathlib import Path


SVG_NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", SVG_NS)
ET.register_namespace("ev", "http://www.w3.org/2001/xml-events")
ET.register_namespace("xlink", "http://www.w3.org/1999/xlink")

ROOT = Path(__file__).resolve().parents[1]
FIGURES = ROOT / "figures"
HAND_AUTHORED = {
    "cover.svg",
    "decision-loop.svg",
    "decision-making-according-to-behavioral-evidence.svg",
    "judgment-and-decision-making-according-to-predictive-processing.svg",
}
DARK_FILLS = {"#17324d", "#0d3b86", "#0a2f68", "#052e67"}
WHITE_FILLS = {"white", "#fff", "#ffffff"}


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def number(value: str | None, default: float = 0.0) -> float:
    if value is None:
        return default
    match = re.match(r"\s*(-?\d+(?:\.\d+)?)", value)
    return float(match.group(1)) if match else default


def normalized_text(element: ET.Element) -> str:
    return re.sub(r"\s+", " ", "".join(element.itertext())).strip()


def explicit_lines(element: ET.Element) -> list[str]:
    tspans = [child for child in element if local_name(child.tag) == "tspan"]
    if tspans:
        return [normalized_text(child) for child in tspans if normalized_text(child)]
    raw = "".join(element.itertext())
    return [re.sub(r"\s+", " ", line).strip() for line in raw.splitlines() if line.strip()]


def wrap_lines(lines: list[str], max_chars: int) -> list[str]:
    wrapped: list[str] = []
    for line in lines or [""]:
        wrapped.extend(
            textwrap.wrap(
                line,
                width=max(6, max_chars),
                break_long_words=False,
                break_on_hyphens=False,
            )
            or [""]
        )
    return wrapped


def fill_of(element: ET.Element) -> str:
    return element.attrib.get("fill", "").strip().lower()


def containing_rect(
    text: ET.Element,
    rects: list[tuple[ET.Element, float, float, float, float]],
    canvas_width: float,
    canvas_height: float,
) -> tuple[ET.Element, float, float, float, float] | None:
    x = number(text.attrib.get("x"))
    y = number(text.attrib.get("y"))
    candidates = []
    for item in rects:
        _, rx, ry, rw, rh = item
        if rw >= canvas_width * 0.8 and rh >= canvas_height * 0.8:
            continue
        if rx <= x <= rx + rw and ry <= y <= ry + rh:
            candidates.append(item)
    return min(candidates, key=lambda item: item[3] * item[4]) if candidates else None


def set_text_lines(
    element: ET.Element,
    lines: list[str],
    x: float,
    first_baseline: float,
    line_height: float,
) -> None:
    element.attrib["x"] = f"{x:g}"
    element.attrib["y"] = f"{first_baseline:g}"
    element.attrib["text-anchor"] = "middle"
    element.text = None
    for child in list(element):
        element.remove(child)
    for index, line in enumerate(lines):
        tspan = ET.SubElement(element, f"{{{SVG_NS}}}tspan")
        tspan.attrib["x"] = f"{x:g}"
        tspan.attrib["dy"] = "0" if index == 0 else f"{line_height:g}"
        tspan.text = line


def normalize(path: Path, write: bool) -> dict[str, int]:
    tree = ET.parse(path)
    root = tree.getroot()
    view_box = [number(part) for part in root.attrib.get("viewBox", "0 0 1200 650").split()]
    canvas_width = view_box[2] if len(view_box) == 4 else number(root.attrib.get("width"), 1200)
    canvas_height = view_box[3] if len(view_box) == 4 else number(root.attrib.get("height"), 650)

    parent = {child: node for node in root.iter() for child in node}
    rects = [
        (
            element,
            number(element.attrib.get("x")),
            number(element.attrib.get("y")),
            number(element.attrib.get("width")),
            number(element.attrib.get("height")),
        )
        for element in root.iter()
        if local_name(element.tag) == "rect"
    ]
    texts = [element for element in root.iter() if local_name(element.tag) == "text"]
    groups: dict[ET.Element, list[ET.Element]] = {}
    rect_geometry: dict[ET.Element, tuple[float, float, float, float]] = {}
    for text in texts:
        rect = containing_rect(text, rects, canvas_width, canvas_height)
        if rect is None:
            continue
        element, x, y, width, height = rect
        groups.setdefault(element, []).append(text)
        rect_geometry[element] = (x, y, width, height)

    removed = 0
    wrapped = 0
    repositioned = 0
    for rect, group in groups.items():
        rx, ry, width, height = rect_geometry[rect]
        rect_fill = fill_of(rect)

        # Dark nodes in the old generator contained low-contrast helper labels
        # plus a second white overlay.  Keep only the accessible white layer.
        if rect_fill in DARK_FILLS and any(fill_of(text) in WHITE_FILLS for text in group):
            for text in list(group):
                if fill_of(text) not in WHITE_FILLS:
                    parent[text].remove(text)
                    group.remove(text)
                    removed += 1

        # Remove later exact duplicates, plus a later label that merely repeats
        # text already contained in an earlier label (the old wanting diagram).
        kept: list[ET.Element] = []
        for text in group:
            current = normalized_text(text).lower().strip("“”\"' ")
            duplicate = False
            for earlier in kept:
                prior = normalized_text(earlier).lower().strip("“”\"' ")
                same_size = abs(number(text.attrib.get("font-size"), 16) - number(earlier.attrib.get("font-size"), 16)) <= 2
                if current == prior or (same_size and len(current) >= 10 and current in prior):
                    duplicate = True
                    break
            if duplicate:
                parent[text].remove(text)
                removed += 1
            else:
                kept.append(text)
        group = kept
        if not group:
            continue

        blocks = []
        for text in group:
            size = number(text.attrib.get("font-size"), 16)
            max_chars = math.floor((width - 24) / max(size * 0.56, 1))
            source_lines = explicit_lines(text)
            lines = wrap_lines(source_lines, max_chars)
            wrapped += max(0, len(lines) - len(source_lines))
            blocks.append({"element": text, "size": size, "lines": lines})

        gap = 5.0
        available = max(20.0, height - 18.0)
        nominal = sum(len(block["lines"]) * block["size"] * 1.18 for block in blocks)
        nominal += gap * max(0, len(blocks) - 1)
        scale = min(1.0, available / nominal) if nominal else 1.0
        # Avoid tiny type. If a crowded box needs more room, reducing the
        # inter-paragraph gap is preferable below this threshold.
        scale = max(0.72, scale)
        if nominal * scale > available and len(blocks) > 1:
            gap = max(1.0, (available - sum(len(block["lines"]) * block["size"] * 1.18 * scale for block in blocks)) / (len(blocks) - 1))

        block_heights = [len(block["lines"]) * block["size"] * 1.18 * scale for block in blocks]
        total_height = sum(block_heights) + gap * max(0, len(blocks) - 1)
        cursor = ry + max(9.0, (height - total_height) / 2)
        for block, block_height in zip(blocks, block_heights):
            text = block["element"]
            size = block["size"] * scale
            line_height = size * 1.18
            text.attrib["font-size"] = f"{size:.2f}".rstrip("0").rstrip(".")
            baseline = cursor + size * 0.84
            set_text_lines(text, block["lines"], rx + width / 2, baseline, line_height)
            cursor += block_height + gap
            repositioned += 1

    if write:
        tree.write(path, encoding="utf-8", xml_declaration=True)
    return {"boxes": len(groups), "labels": repositioned, "removed": removed, "wraps": wrapped}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="*", type=Path)
    parser.add_argument("--check", action="store_true", help="Analyze without rewriting files.")
    args = parser.parse_args()
    paths = args.paths or sorted(path for path in FIGURES.glob("*.svg") if path.name not in HAND_AUTHORED)
    total = {"boxes": 0, "labels": 0, "removed": 0, "wraps": 0}
    for path in paths:
        stats = normalize(path, write=not args.check)
        for key, value in stats.items():
            total[key] += value
        print(f"{path.name}: {stats}")
    print(f"total: {total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
