#!/usr/bin/env python3
"""Audit connector attachment and arrowhead proportions in book SVGs.

The book uses two arrow styles: SVG markers on paths and explicit triangle
polygons following a line.  This check recognizes both forms, extracts the
arrow tip, and measures it against rectangle, circle, polygon, and filled-path
node boundaries.  Marker-based arrows are also screened for unstable
stroke-scaled markers, oversized heads, and gaps so short that the connector
renders as an arrowhead without a visible shaft.  Axis arrows in the Pareto
plot are the only intentional free endpoints.
"""

from __future__ import annotations

import math
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIGURES = ROOT / "figures"
CONFIG = ROOT / "_quarto-html.yml"
NUMBER = re.compile(r"-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?")
TOKEN = re.compile(r"[A-Za-z]|-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?")
BOOK_SOURCE_LINE = re.compile(r"^\s*-\s+(?:part:\s+)?([^\s]+\.qmd)\s*$", re.MULTILINE)
DESKTOP_FIGURE_WIDTH = 820.0  # quarto-custom.scss: main.content max-width
MIN_SUPPORTING_TEXT_CSS_PX = 10.5
FREE_ENDPOINTS = {
    ("pareto.svg", 1120.0, 540.0),  # horizontal axis
    ("pareto.svg", 150.0, 70.0),  # vertical axis
}


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def number(value: str | None, default: float = 0.0) -> float:
    try:
        return float(value) if value is not None else default
    except ValueError:
        return default


def path_points(data: str | None) -> list[tuple[float, float]]:
    """Return successive command endpoints for the simple paths in the book."""
    tokens = TOKEN.findall(data or "")
    arity = {"M": 2, "L": 2, "H": 1, "V": 1, "C": 6, "S": 4, "Q": 4, "T": 2, "A": 7}
    points: list[tuple[float, float]] = []
    command: str | None = None
    index = 0
    x = y = 0.0
    start = (0.0, 0.0)
    while index < len(tokens):
        if tokens[index].isalpha():
            command = tokens[index]
            index += 1
        if command is None:
            break
        upper = command.upper()
        if upper == "Z":
            x, y = start
            points.append((x, y))
            command = None
            continue
        count = arity.get(upper)
        if count is None or index + count > len(tokens):
            break
        values = [float(value) for value in tokens[index : index + count]]
        index += count
        relative = command.islower()
        if upper in {"M", "L", "T"}:
            new_x, new_y = values[-2:]
            if relative:
                new_x += x
                new_y += y
        elif upper == "H":
            new_x = values[0] + (x if relative else 0.0)
            new_y = y
        elif upper == "V":
            new_x = x
            new_y = values[0] + (y if relative else 0.0)
        else:
            new_x, new_y = values[-2:]
            if relative:
                new_x += x
                new_y += y
        x, y = new_x, new_y
        points.append((x, y))
        if upper == "M":
            start = (x, y)
            command = "l" if relative else "L"
    return points


def points_attribute(value: str | None) -> list[tuple[float, float]]:
    values = [float(item) for item in NUMBER.findall(value or "")]
    return list(zip(values[::2], values[1::2]))


def segment_distance(
    point: tuple[float, float], start: tuple[float, float], end: tuple[float, float]
) -> float:
    px, py = point
    ax, ay = start
    bx, by = end
    dx, dy = bx - ax, by - ay
    if dx == 0 and dy == 0:
        return math.hypot(px - ax, py - ay)
    ratio = ((px - ax) * dx + (py - ay) * dy) / (dx * dx + dy * dy)
    ratio = max(0.0, min(1.0, ratio))
    return math.hypot(px - (ax + ratio * dx), py - (ay + ratio * dy))


def polygon_distance(point: tuple[float, float], points: list[tuple[float, float]]) -> float:
    if len(points) < 2:
        return math.inf
    segments = zip(points, points[1:] + [points[0]])
    return min(segment_distance(point, start, end) for start, end in segments)


def rectangle_distance(point: tuple[float, float], rect: tuple[float, float, float, float]) -> float:
    px, py = point
    x, y, width, height = rect
    if x <= px <= x + width and y <= py <= y + height:
        return min(px - x, x + width - px, py - y, y + height - py)
    dx = max(x - px, 0.0, px - (x + width))
    dy = max(y - py, 0.0, py - (y + height))
    return math.hypot(dx, dy)


def arrow_endpoint(element: ET.Element) -> tuple[float, float] | None:
    tag = local_name(element.tag)
    if tag == "line":
        return number(element.get("x2")), number(element.get("y2"))
    if tag in {"polyline", "polygon"}:
        points = points_attribute(element.get("points"))
        return points[-1] if points else None
    points = path_points(element.get("d"))
    return points[-1] if points else None


def arrow_startpoint(element: ET.Element) -> tuple[float, float] | None:
    tag = local_name(element.tag)
    if tag == "line":
        return number(element.get("x1")), number(element.get("y1"))
    if tag in {"polyline", "polygon"}:
        points = points_attribute(element.get("points"))
        return points[0] if points else None
    points = path_points(element.get("d"))
    return points[0] if points else None


def marker_id(value: str | None) -> str | None:
    match = re.fullmatch(r"url\(#([^)]+)\)", (value or "").strip())
    return match.group(1) if match else None


def marker_definitions(root: ET.Element) -> dict[str, ET.Element]:
    return {
        element.get("id", ""): element
        for element in root.iter()
        if local_name(element.tag) == "marker" and element.get("id")
    }


def connector_length(element: ET.Element) -> float:
    tag = local_name(element.tag)
    if tag == "line":
        start = arrow_startpoint(element)
        end = arrow_endpoint(element)
        return math.dist(start, end) if start and end else 0.0
    points = points_attribute(element.get("points")) if tag in {"polyline", "polygon"} else path_points(element.get("d"))
    return sum(math.dist(start, end) for start, end in zip(points, points[1:]))


def marker_length(marker: ET.Element, stroke_width: float) -> float:
    width = number(marker.get("markerWidth"), 3.0)
    if marker.get("markerUnits", "strokeWidth") != "userSpaceOnUse":
        width *= stroke_width
    return width


def intrinsic_width(root: ET.Element) -> float:
    values = [number(value) for value in NUMBER.findall(root.get("viewBox", ""))]
    if len(values) == 4 and values[2] > 0:
        return values[2]
    return max(number(root.get("width"), DESKTOP_FIGURE_WIDTH), 1.0)


def css_class_font_sizes(root: ET.Element) -> dict[str, float]:
    styles = "\n".join(
        element.text or ""
        for element in root.iter()
        if local_name(element.tag) == "style"
    )
    sizes: dict[str, float] = {}
    for class_name, body in re.findall(r"\.([\w-]+)\s*\{([^}]*)\}", styles):
        match = re.search(r"font-size\s*:\s*([\d.]+)px", body)
        if match is None:
            match = re.search(r"font\s*:[^;{}]*?([\d.]+)px", body)
        if match:
            sizes[class_name] = float(match.group(1))
    return sizes


def text_font_sizes(root: ET.Element) -> list[float]:
    class_sizes = css_class_font_sizes(root)
    sizes: list[float] = []
    for element in root.iter():
        if local_name(element.tag) != "text":
            continue
        candidates: list[float] = []
        direct = re.search(r"[\d.]+", element.get("font-size", ""))
        if direct:
            candidates.append(float(direct.group(0)))
        style = element.get("style", "")
        styled = re.search(r"font-size\s*:\s*([\d.]+)px", style)
        if styled:
            candidates.append(float(styled.group(1)))
        shorthand = re.search(r"(?:^|;)\s*font\s*:[^;]*?([\d.]+)px", style)
        if shorthand:
            candidates.append(float(shorthand.group(1)))
        candidates.extend(
            class_sizes[class_name]
            for class_name in element.get("class", "").split()
            if class_name in class_sizes
        )
        if candidates:
            sizes.append(min(candidates))
    return sizes


def book_figure_names() -> set[str]:
    """Return every SVG referenced by the configured HTML book sources."""
    names: set[str] = set()
    for relative in BOOK_SOURCE_LINE.findall(CONFIG.read_text(encoding="utf-8")):
        source = ROOT / relative
        names.update(
            re.findall(
                r"(?:\.\./)?figures/([^)\s]+\.svg)",
                source.read_text(encoding="utf-8"),
            )
        )
    return names


def node_shapes(root: ET.Element) -> list[tuple[str, object]]:
    shapes: list[tuple[str, object]] = []
    for element in root.iter():
        tag = local_name(element.tag)
        if tag == "rect":
            rect = tuple(number(element.get(key)) for key in ("x", "y", "width", "height"))
            x, y, width, height = rect
            if width >= 100 and height >= 50 and not (x == 0 and y == 0):
                shapes.append(("rect", rect))
        elif tag == "circle" and number(element.get("r")) >= 8:
            shapes.append(
                ("circle", (number(element.get("cx")), number(element.get("cy")), number(element.get("r"))))
            )
        elif tag == "polygon":
            points = points_attribute(element.get("points"))
            if len(points) >= 3 and max(x for x, _ in points) - min(x for x, _ in points) > 80:
                shapes.append(("polygon", points))
        elif tag == "path" and not element.get("marker-end"):
            is_node = element.get("fill", "none") not in {"", "none"} or "node" in element.get("class", "").split()
            points = path_points(element.get("d"))
            if is_node and len(points) >= 3:
                shapes.append(("polygon", points))
    return shapes


def distance_to_nodes(point: tuple[float, float], shapes: list[tuple[str, object]]) -> float:
    distances: list[float] = []
    for kind, shape in shapes:
        if kind == "rect":
            distances.append(rectangle_distance(point, shape))  # type: ignore[arg-type]
        elif kind == "circle":
            cx, cy, radius = shape  # type: ignore[misc]
            distances.append(abs(math.hypot(point[0] - cx, point[1] - cy) - radius))
        else:
            distances.append(polygon_distance(point, shape))  # type: ignore[arg-type]
    return min(distances, default=math.inf)


def explicit_arrow_lines(root: ET.Element) -> list[ET.Element]:
    """Find line elements whose following sibling is their arrowhead triangle."""
    children = list(root)
    arrows: list[ET.Element] = []
    for index, element in enumerate(children[:-1]):
        if local_name(element.tag) != "line" or local_name(children[index + 1].tag) != "polygon":
            continue
        endpoint = arrow_endpoint(element)
        triangle = points_attribute(children[index + 1].get("points"))
        if endpoint and triangle and math.dist(endpoint, triangle[0]) <= 1.0:
            arrows.append(element)
    return arrows


def audit(path: Path, tolerance: float = 14.0) -> list[str]:
    root = ET.parse(path).getroot()
    shapes = node_shapes(root)
    markers = marker_definitions(root)
    arrows = explicit_arrow_lines(root)
    arrows.extend(
        element
        for element in root.iter()
        if element.get("marker-end") and "arrowSmall" not in element.get("marker-end", "")
    )
    issues: list[str] = []
    font_sizes = text_font_sizes(root)
    if font_sizes:
        width = intrinsic_width(root)
        display_scale = min(1.0, DESKTOP_FIGURE_WIDTH / width)
        smallest_rendered = min(font_sizes) * display_scale
        if smallest_rendered < MIN_SUPPORTING_TEXT_CSS_PX:
            issues.append(
                f"smallest text renders at about {smallest_rendered:.1f}px at the {DESKTOP_FIGURE_WIDTH:.0f}px "
                f"book width (source {min(font_sizes):.1f}px on a {width:.0f}px canvas); enlarge or reflow it"
            )
    seen: set[int] = set()
    for arrow in arrows:
        if id(arrow) in seen:
            continue
        seen.add(id(arrow))
        endpoint = arrow_endpoint(arrow)
        if endpoint is None:
            issues.append("could not parse an arrow endpoint")
            continue
        key = (path.name, round(endpoint[0], 1), round(endpoint[1], 1))
        if key in FREE_ENDPOINTS:
            continue
        distance = distance_to_nodes(endpoint, shapes)
        if distance > tolerance:
            issues.append(
                f"arrow ends at ({endpoint[0]:.1f}, {endpoint[1]:.1f}), "
                f"{distance:.1f}px from the nearest node"
            )
        marker_name = marker_id(arrow.get("marker-end"))
        marker = markers.get(marker_name or "")
        if marker is None:
            continue
        stroke_width = max(number(arrow.get("stroke-width"), 1.0), 0.1)
        units = marker.get("markerUnits", "strokeWidth")
        if units != "userSpaceOnUse":
            issues.append(
                f"marker #{marker_name} uses {units} units and can grow with stroke width; "
                "use markerUnits=userSpaceOnUse"
            )
        head_length = marker_length(marker, stroke_width)
        # The visual specification targets a head about two to three stroke
        # widths long.  Allow a small tolerance for marker-box whitespace, but
        # reject the four-to-ten-times-stroke heads that dominate short links.
        if head_length > 3.5 * stroke_width:
            issues.append(
                f"marker #{marker_name} is {head_length:.1f}px long for a {stroke_width:.1f}px stroke "
                f"({head_length / stroke_width:.1f}x); reduce the arrowhead"
            )
        length = connector_length(arrow)
        if length and length < 3.0 * head_length:
            issues.append(
                f"connector is {length:.1f}px long but marker #{marker_name} is {head_length:.1f}px; "
                "leave at least two arrowhead lengths of visible shaft"
            )
    return issues


def main() -> int:
    failures = 0
    names = book_figure_names()
    for name in sorted(names):
        path = FIGURES / name
        issues = audit(path)
        if issues:
            failures += len(issues)
            for issue in issues:
                print(f"{name}: {issue}")
    if failures:
        print(f"FAILED: {failures} connector geometry issue(s)")
        return 1
    print(f"PASS: checked connector attachment and arrowhead proportions in {len(names)} reader-facing book figures")
    return 0


if __name__ == "__main__":
    sys.exit(main())
