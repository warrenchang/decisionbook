#!/usr/bin/env python3
"""Build Figure 37.2: a schematic, equally scaled Pareto frontier.

The feasible set is a hypothetical quarter disk in two separately normalized
value scores. No observations are plotted. The creation arrow improves both
scores; the claiming arrow follows the frontier at a small visual offset.
"""

from __future__ import annotations

import argparse
import math
from pathlib import Path


CAPTION = (
    "Creating value improves both parties' outcomes; claiming value changes "
    "their division along the Pareto frontier. A schematic feasible set with "
    "each party's value scaled from 0 to 100."
)
ALT = (
    "A square plot has value to the seller on the horizontal axis and value "
    "to the buyer on the vertical axis, both from 0 to 100. A downward-curving "
    "Pareto frontier bounds the shaded feasible agreements. A creating-value "
    "arrow moves northeast from an interior agreement to the frontier, "
    "improving both outcomes. A two-headed claiming-value arrow follows the "
    "frontier: more for one party means less for the other."
)

ORIGIN = (130.0, 630.0)
PLOT_SIZE = 520.0
VALUE_MAX = 100.0
CANVAS = 760


def frontier_point(degrees: float, offset: float = 0) -> tuple[float, float]:
    angle = math.radians(degrees)
    radius = PLOT_SIZE + offset
    return ORIGIN[0] + radius * math.cos(angle), ORIGIN[1] - radius * math.sin(angle)


def write_pareto_svg(path: Path) -> None:
    efficient = frontier_point(45)
    # Stop the arrowhead at the near boundary of the 8px efficient-point marker.
    arrow_tip = (efficient[0] - 8 / math.sqrt(2), efficient[1] + 8 / math.sqrt(2))
    claim_start, claim_end = frontier_point(65, 40), frontier_point(25, 40)
    leader_end = (300, ORIGIN[1] - math.sqrt(PLOT_SIZE**2 - (300 - ORIGIN[0])**2))
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{CANVAS}" height="{CANVAS}" viewBox="0 0 {CANVAS} {CANVAS}" role="img" aria-labelledby="pareto-title pareto-desc">
  <title id="pareto-title">Creating and claiming value at the Pareto frontier</title>
  <desc id="pareto-desc">{ALT}</desc>
  <defs>
    <marker id="axis-tip" markerUnits="userSpaceOnUse" markerWidth="14" markerHeight="14" viewBox="0 0 14 14" refX="14" refY="7" orient="auto"><path d="M0 0 L14 7 L0 14 Z" fill="#19364d"/></marker>
    <marker id="creation-tip" markerUnits="userSpaceOnUse" markerWidth="17" markerHeight="17" viewBox="0 0 17 17" refX="17" refY="8.5" orient="auto"><path d="M0 0 L17 8.5 L0 17 Z" fill="#19746b"/></marker>
    <marker id="claim-tip" markerUnits="userSpaceOnUse" markerWidth="16" markerHeight="16" viewBox="0 0 16 16" refX="16" refY="8" orient="auto-start-reverse"><path d="M0 0 L16 8 L0 16 Z" fill="#b65b27"/></marker>
  </defs>
  <rect width="760" height="760" fill="#fff"/>
  <g font-family="Arial, Helvetica, sans-serif" font-size="28" fill="#19364d">
    <path id="feasible-set" d="M130 630 L130 110 A520 520 0 0 1 650 630 Z" fill="#eaf4f2"/>
    <g stroke="#d0dfdf" stroke-width="1.5" stroke-dasharray="5 7">
      <path d="M390 630 V110"/>
      <path d="M130 370 H650"/>
    </g>
    <path id="frontier" d="M130 110 A520 520 0 0 1 650 630" fill="none" stroke="#19364d" stroke-width="5"/>
    <g stroke="#19364d" stroke-width="4" fill="none">
      <path id="x-axis" d="M130 630 H692" stroke-width="4" marker-end="url(#axis-tip)"/>
      <path id="y-axis" d="M130 630 V68" stroke-width="4" marker-end="url(#axis-tip)"/>
    </g>
    <g stroke="#19364d" stroke-width="2">
      <path d="M390 630 V640 M650 630 V640 M120 370 H130 M120 110 H130"/>
    </g>
    <g fill="#506476">
      <text x="113" y="662" text-anchor="end">0</text>
      <text x="390" y="673" text-anchor="middle">50</text>
      <text x="650" y="673" text-anchor="middle">100</text>
      <text x="108" y="380" text-anchor="end">50</text>
      <text x="108" y="120" text-anchor="end">100</text>
    </g>
    <text x="390" y="724" text-anchor="middle" font-size="30" font-weight="700">Value to seller</text>
    <text x="42" y="370" text-anchor="middle" font-size="30" font-weight="700" transform="rotate(-90 42 370)">Value to buyer</text>
    <text x="338" y="72" text-anchor="middle" font-weight="700">Pareto frontier</text>
    <path d="M300 86 L300 {leader_end[1]:.3f}" stroke="#19364d" stroke-width="2" fill="none"/>
    <text x="283" y="553" text-anchor="middle" fill="#506476">Feasible</text>
    <text x="283" y="587" text-anchor="middle" fill="#506476">agreements</text>
    <circle cx="270" cy="490" r="7" fill="#19746b"/>
    <path id="value-creation" d="M274.950 485.050 L{arrow_tip[0]:.3f} {arrow_tip[1]:.3f}" stroke="#19746b" stroke-width="5" fill="none" marker-end="url(#creation-tip)"/>
    <circle cx="{efficient[0]:.3f}" cy="{efficient[1]:.3f}" r="8" fill="#fff" stroke="#19364d" stroke-width="3"/>
    <g fill="#19746b" font-weight="700" text-anchor="middle">
      <text x="455" y="410">Creating</text>
      <text x="455" y="444">value</text>
    </g>
    <path id="value-claiming" d="M{claim_start[0]:.3f} {claim_start[1]:.3f} A560 560 0 0 1 {claim_end[0]:.3f} {claim_end[1]:.3f}" stroke="#b65b27" stroke-width="5" fill="none" marker-start="url(#claim-tip)" marker-end="url(#claim-tip)"/>
    <g fill="#b65b27" font-weight="700" text-anchor="middle">
      <text x="614" y="193">Claiming</text>
      <text x="614" y="227">value</text>
    </g>
  </g>
</svg>
'''
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(svg, encoding="utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parents[1] / "figures/pareto.svg")
    write_pareto_svg(parser.parse_args().output)
