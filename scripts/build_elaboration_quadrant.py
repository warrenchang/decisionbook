#!/usr/bin/env python3
"""Draw a schematic of motivation and ability in message evaluation.

Petty and Brinol (2012), The Elaboration Likelihood Model, pp. 224–245.
The partitions are reading aids, not measured cutoffs or audience types.
Generate the PNG from this final SVG with render_svg_png_fallbacks.cjs.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "figures/elaboration-quadrant.svg"


def build():
    TARGET.write_text('''<svg xmlns="http://www.w3.org/2000/svg" width="780" height="690" viewBox="0 0 780 690" role="img" aria-labelledby="title desc">
  <title id="title">Motivation and ability to evaluate a message</title>
  <desc id="desc">The axes intersect at the center of the four quadrants. Ability increases to the right and motivation increases upward. High motivation with limited ability means willing but constrained; high ability with low motivation means able but less motivated. When both are low, little scrutiny is likely. When both are high, careful scrutiny is more likely. The four regions summarize continuous dimensions, not fixed audience types.</desc>
  <defs>
    <marker id="axis-tip" markerWidth="9" markerHeight="9" viewBox="0 0 9 9" refX="9" refY="4.5" orient="auto" markerUnits="userSpaceOnUse"><path d="M0 0 L9 4.5 L0 9 Z" fill="#19364d"/></marker>
  </defs>
  <rect width="780" height="690" fill="#fff"/>
  <g>
    <rect x="35" y="80" width="305" height="285" fill="#edf1f5"/>
    <rect x="340" y="80" width="305" height="285" fill="#d9eeeb"/>
    <rect x="35" y="365" width="305" height="285" fill="#f5f6f7"/>
    <rect x="340" y="365" width="305" height="285" fill="#edf1f5"/>
    <path d="M35 365 H649" fill="none" stroke="#19364d" stroke-width="3" marker-end="url(#axis-tip)"/>
    <path d="M340 650 V76" fill="none" stroke="#19364d" stroke-width="3" marker-end="url(#axis-tip)"/>
  </g>
  <g font-family="Arial, Helvetica, sans-serif" font-size="32" fill="#19364d" text-anchor="middle">
    <g font-weight="700">
      <text x="187.5" y="214"><tspan x="187.5">Willing, but</tspan><tspan x="187.5" dy="40">constrained</tspan></text>
      <text x="492.5" y="214"><tspan x="492.5">Careful scrutiny</tspan><tspan x="492.5" dy="40">more likely</tspan></text>
      <text x="187.5" y="500"><tspan x="187.5">Little scrutiny</tspan><tspan x="187.5" dy="40">likely</tspan></text>
      <text x="492.5" y="500"><tspan x="492.5">Able, but</tspan><tspan x="492.5" dy="40">less motivated</tspan></text>
    </g>
    <g font-size="30" fill="#536879">
      <text x="45" y="402" text-anchor="start">Low</text><text x="636" y="402" text-anchor="end">High</text>
      <text x="355" y="111" text-anchor="start">High</text><text x="355" y="635" text-anchor="start">Low</text>
    </g>
    <text x="340" y="43" font-weight="700">Motivation</text>
    <text x="661" y="376" font-size="30" text-anchor="start" font-weight="700">Ability</text>
  </g>
</svg>
''', encoding="utf-8")
    print(TARGET.relative_to(ROOT))


if __name__ == "__main__":
    build()
