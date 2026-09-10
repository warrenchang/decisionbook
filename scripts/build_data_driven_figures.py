#!/usr/bin/env python3
"""Generate original SVGs for the Data Driven Decision Making chapter.

Run from any working directory. The two figures are hypothetical numerical
examples, not empirical estimates. The chapter uses the normative decision loop
from Figure 1.1. Parameters and assertions make the examples reproducible.
PNG fallbacks can be refreshed with scripts/render_svg_png_fallbacks.cjs.
"""

from __future__ import annotations

from pathlib import Path
from xml.etree import ElementTree as ET
from xml.sax.saxutils import escape


ROOT = Path(__file__).resolve().parents[1]
FIGURES = ROOT / "figures"
NAVY = "#17324d"
BLUE = "#2f6f9f"
GREEN = "#447c55"
ORANGE = "#c56a2d"
MUTED = "#526778"
LIGHT = "#d8e2e9"
PALE_BLUE = "#edf4f8"
PALE_GREEN = "#f0f5ef"
PALE_ORANGE = "#fbf2e9"
WIDTH = 800


def text(x, y, value, size=28, *, weight=400, fill=NAVY, anchor="middle"):
    return (
        f'<text x="{x:g}" y="{y:g}" text-anchor="{anchor}" '
        f'font-family="Arial, Helvetica, sans-serif" font-size="{size}" '
        f'font-weight="{weight}" fill="{fill}">{escape(value)}</text>'
    )


def rect(x, y, w, h, *, fill="white", stroke=LIGHT, radius=18):
    return (
        f'<rect x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}" '
        f'rx="{radius}" fill="{fill}" stroke="{stroke}" stroke-width="2"/>'
    )


def line(x1, y1, x2, y2, *, stroke=MUTED, width=3, extra=""):
    return (
        f'<line x1="{x1:g}" y1="{y1:g}" x2="{x2:g}" y2="{y2:g}" '
        f'stroke="{stroke}" stroke-width="{width}" stroke-linecap="round" {extra}/>'
    )


def path(d, *, arrow=False):
    marker = ' marker-end="url(#arrow)"' if arrow else ""
    return (
        f'<path d="{d}" fill="none" stroke="{MUTED}" stroke-width="3" '
        f'stroke-linecap="round" stroke-linejoin="round"{marker}/>'
    )


def circle(x, y, r, fill, *, stroke="white", sw=3):
    return (
        f'<circle cx="{x:g}" cy="{y:g}" r="{r:g}" fill="{fill}" '
        f'stroke="{stroke}" stroke-width="{sw}"/>'
    )


def document(title, description, body, height):
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{height}" viewBox="0 0 {WIDTH} {height}" role="img" aria-labelledby="title desc">
  <title id="title">{escape(title)}</title>
  <desc id="desc">{escape(description)}</desc>
  <defs>
    <marker id="arrow" viewBox="0 0 9 8" markerWidth="9" markerHeight="8" refX="8" refY="4" orient="auto" markerUnits="userSpaceOnUse">
      <path d="M0.5 0.5 L8 4 L0.5 7.5 Z" fill="{MUTED}"/>
    </marker>
  </defs>
  <rect width="{WIDTH}" height="{height}" fill="white"/>
{chr(10).join(body)}
</svg>
'''


def same_forecast():
    rain_probability = 0.30
    cases = [("A", 2, 8), ("B", 6, 4)]
    body = [
        text(400, 49, "One forecast, two decisions", 36, weight=700),
        rect(190, 86, 420, 94, fill=PALE_BLUE, stroke=BLUE),
        text(400, 145, "Rain probability: 30%", 32, weight=700, fill=BLUE),
    ]
    for i, (organizer, false_alarm, missed_rain) in enumerate(cases):
        threshold = false_alarm / (false_alarm + missed_rain)
        loss_move = (1 - rain_probability) * false_alarm
        loss_stay = rain_probability * missed_rain
        move = loss_move < loss_stay
        assert abs(threshold - [0.20, 0.60][i]) < 1e-12
        assert move == (i == 0)
        y = 222 + i * 300
        left, right, bar_y = 90, 710, y + 146
        threshold_x = left + threshold * (right - left)
        forecast_x = left + rain_probability * (right - left)
        color = ORANGE if move else GREEN
        body += [
            f'<g id="organizer-{organizer.lower()}">',
            rect(40, y, 720, 268, fill="white", stroke=LIGHT),
            text(70, y + 45, f"Organizer {organizer}", 32, weight=700, anchor="start"),
            text(70, y + 89, f"False alarm: {false_alarm}", 28, anchor="start"),
            text(430, y + 89, f"Missed rain: {missed_rain}", 28, anchor="start"),
            line(left, bar_y, right, bar_y, stroke=LIGHT, width=12),
            line(threshold_x, bar_y - 17, threshold_x, bar_y + 18, stroke=NAVY, width=3),
            circle(forecast_x, bar_y, 10, BLUE),
            text(forecast_x, bar_y - 25, "30%", 28, weight=700, fill=BLUE),
            text(left, bar_y + 57, "0", 28, fill=MUTED),
            text(right, bar_y + 57, "100%", 28, fill=MUTED),
            text(threshold_x, bar_y + 57, f"{threshold:.0%} threshold", 28),
            text(400, y + 244, "Move indoors" if move else "Keep outdoors", 32, weight=700, fill=color),
            '</g>',
        ]
    return document(
        "One forecast, two decisions",
        "Hypothetical error-loss example, not observed data or advice for an actual "
        "event. Both organizers forecast rain with probability 30 percent. Correct "
        "choices have zero incremental loss. A false alarm means moving indoors "
        "on a dry day; a miss means remaining outdoors in rain. Organizer A has "
        "losses 2 and 8, respectively, so the switching threshold is 2/(2+8)=20 "
        "percent. Expected losses are 1.4 for moving and 2.4 for staying: move "
        "indoors. Organizer B has losses 6 and 4, so the threshold is 60 percent. "
        "Expected losses are 4.2 for moving and 1.2 for staying: keep outdoors. "
        "The blue dot marks the shared forecast on each 0 to 100 percent strip; "
        "the vertical tick marks the organizer's switching threshold. Losses are "
        "in hypothetical common units, with risk-neutral expected-loss comparison, "
        "two actions, and two weather states. At the threshold, the actions tie.",
        body, 820,
    )


def risk_and_benefit():
    groups = [("A", 0.60, 0.55), ("B", 0.40, 0.20)]
    left, right, maximum = 170, 710, 0.70

    def pos(p):
        return left + p / maximum * (right - left)

    body = [
        text(400, 49, "Risk is not the same as benefit", 36, weight=700),
        text(400, 105, "Dropout probability", 30),
    ]
    for tick in range(8):
        x = pos(tick / 10)
        body += [
            line(x, 139, x, 505, stroke="#edf1f4", width=2),
            line(x, 505, x, 515, stroke=MUTED, width=2),
            text(x, 548, f"{tick * 10}%", 28, fill=MUTED),
        ]
    for i, (group, untreated, treated) in enumerate(groups):
        y = 203 + 180 * i
        benefit = untreated - treated
        assert abs(benefit * 100 - [5, 20][i]) < 1e-12
        body += [
            f'<g id="group-{group.lower()}">',
            text(34, y + 11, f"Group {group}", 30, weight=700, anchor="start"),
            line(pos(treated), y, pos(untreated), y, stroke=MUTED, width=5),
            circle(pos(untreated), y, 10, ORANGE),
            circle(pos(treated), y, 10, GREEN),
            text(pos(untreated), y - 31, f"{untreated:.0%} without", 28, weight=700, fill=ORANGE),
            text(pos(treated), y + 51, f"{treated:.0%} with", 28, weight=700, fill=GREEN),
            text(710, y + 92, f"Benefit: {benefit * 100:.0f} percentage points", 28, anchor="end"),
            '</g>',
        ]
    body += [
        line(left, 505, right, 505, stroke=MUTED, width=2),
        text(400, 605, "Risk ranks A first; benefit ranks B first", 32, weight=700),
    ]
    return document(
        "Risk is not the same as benefit",
        "Completely hypothetical group-average causal comparison, not empirical "
        "data or a claim that outreach is effective. Group A's dropout probability "
        "is assumed to be 60 percent without outreach and 55 percent with outreach, "
        "a reduction of 5 percentage points. Group B's probabilities are 40 percent "
        "and 20 percent, a reduction of 20 percentage points. Orange points show "
        "probabilities without outreach; green points show probabilities with "
        "outreach. The common horizontal axis runs from 0 to 70 percent. Baseline "
        "risk ranks A first, but the expected average benefit of outreach ranks B "
        "first. The benefit ranking is relevant if outreach costs, feasibility, "
        "and the value of preventing a dropout are equal; other values or "
        "constraints can change the allocation. Effects are group averages, not "
        "identified individual effects. Estimating outcomes with versus without "
        "outreach requires causal evidence; a baseline risk model alone does not "
        "supply those effects.",
        body, 642,
    )


def main():
    figures = {
        "ai-same-forecast-different-values.svg": same_forecast(),
        "ai-risk-is-not-benefit.svg": risk_and_benefit(),
    }
    for filename, svg in figures.items():
        parsed = ET.fromstring(svg)
        ids = [el.attrib["id"] for el in parsed.iter() if "id" in el.attrib]
        assert len(ids) == len(set(ids)), f"Duplicate IDs in {filename}"
        assert parsed.attrib["viewBox"].startswith("0 0 800 ")
        path_out = FIGURES / filename
        path_out.write_text(svg, encoding="utf-8")
        print(path_out.relative_to(ROOT))


if __name__ == "__main__":
    main()
