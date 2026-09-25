#!/usr/bin/env python3
"""Plot the two realized states in Chapter 38's hypothetical patent case.

These are arithmetic implications of specified contract terms, not study data.
Render the finished SVG to PNG with render_svg_png_fallbacks.cjs.
"""
from pathlib import Path
from html import escape
import json

ROOT = Path(__file__).resolve().parents[1]
ASSET_VALUES = {"No approval": 20, "Approval": 120}
PACKAGES = {"D": {"upfront": -10, "bonus": 100},
            "E": {"upfront": 2, "bonus": 80}}
PAYOFFS = {
    name: {state: gross - terms["upfront"] -
           (terms["bonus"] if state == "Approval" else 0)
           for state, gross in ASSET_VALUES.items()}
    for name, terms in PACKAGES.items()
}
assert PAYOFFS == {"D": {"No approval": 30, "Approval": 30},
                   "E": {"No approval": 18, "Approval": 38}}

NAVY, BLUE, TEAL = "#183047", "#254f77", "#087e8b"
MUTED, GRID, AXIS = "#536879", "#dce3e8", "#9aabb5"
elements = [
    '<svg xmlns="http://www.w3.org/2000/svg" width="760" height="680" '
    'viewBox="0 0 760 680" role="img" aria-labelledby="title desc">',
    '<title id="title">MPharm\'s payoff in two approval states</title>',
    '<desc id="desc">Hypothetical payoffs before effort costs, in millions of dollars. '
    'Package D leaves MPharm 30 without approval and 30 with approval. '
    'Package E leaves 18 without approval and 38 with approval. '
    'Approval therefore adds zero under D and 20 under E.</desc>',
    '<rect width="760" height="680" fill="#ffffff"/>',
    '<g font-family="Arial, Helvetica, sans-serif" fill="' + NAVY + '">',
]

def text(x, y, label, size=32, anchor="start", weight="normal", color=NAVY):
    elements.append(f'<text x="{x}" y="{y}" font-size="{size}" '
                    f'text-anchor="{anchor}" font-weight="{weight}" '
                    f'fill="{color}">{escape(label)}</text>')

x0, unit = 260, 10
for name, heading_y, row_ys in [("D", 80, [145, 230]),
                               ("E", 345, [410, 495])]:
    text(42, heading_y, f"Package {name}", size=36, weight="bold")
    for tick in range(0, 41, 10):
        x = x0 + tick * unit
        elements.append(f'<line x1="{x}" y1="{row_ys[0]-32}" '
                        f'x2="{x}" y2="{row_ys[1]+32}" '
                        f'stroke="{AXIS if tick == 0 else GRID}" stroke-width="2"/>')
    for (state, value), cy, color in zip(PAYOFFS[name].items(), row_ys, [BLUE, TEAL]):
        text(x0 - 22, cy + 11, state, anchor="end")
        elements.append(f'<rect x="{x0}" y="{cy-26}" '
                        f'width="{value*unit}" height="52" fill="{color}"/>')
        # Clear the grid behind the direct value label without covering the bar.
        elements.append(f'<rect x="{x0 + value*unit + 6}" y="{cy-24}" '
                        'width="55" height="48" fill="#ffffff"/>')
        text(x0 + value * unit + 12, cy + 11, str(value), weight="bold")

elements.append(f'<line x1="{x0}" y1="550" x2="660" y2="550" '
                f'stroke="{AXIS}" stroke-width="2"/>')
for tick in range(0, 41, 10):
    x = x0 + tick * unit
    elements.append(f'<line x1="{x}" y1="550" x2="{x}" y2="558" '
                    f'stroke="{AXIS}" stroke-width="2"/>')
    text(x, 595, str(tick), anchor="middle", color=MUTED)
text(460, 645, "MPharm net payoff ($m)", anchor="middle")
elements += ['</g>', '</svg>']

path = ROOT / "figures/contract-state-payoffs.svg"
path.write_text("\n".join(elements) + "\n")
audit = ROOT / "audits/visual-readability-20260925"
audit.mkdir(parents=True, exist_ok=True)
(audit / "contract-state-data.json").write_text(json.dumps({
    "source": "Chapter 38, hypothetical MPharm case and Table tbl-mpharm-packages",
    "units": "millions of dollars",
    "gross_asset_values": ASSET_VALUES,
    "contract_terms": PACKAGES,
    "MPharm_realized_net_payoffs_before_effort_costs": PAYOFFS,
    "calculation": "asset value minus upfront payment minus approval bonus if approved",
    "boundary": "Not observed study outcomes or subjective expected gains. No effort costs or contract-induced changes in approval probability are included."
}, indent=2) + "\n")
print(path.relative_to(ROOT))
