#!/usr/bin/env python3
"""Build Figure 30.1: identical illustrative observations, different stories.

Run with Python 3; only the standard library is required. The fixed coordinates
are an authored teaching example, not empirical data or an extracted dataset.
The intercept and amplitude of each prescribed trend shape are fitted by
ordinary least squares to exactly the same observations. The shape itself is
held fixed, including the tapering curve's previously specified time scale.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from xml.etree import ElementTree as ET
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[1]
FIGURES = ROOT / "figures"
POINTS = [
    (0.5, 14), (1.1, 34), (1.4, 20), (1.9, 12), (2.1, 26), (2.4, 21),
    (2.6, 60), (2.8, 27), (3.0, 24), (3.4, 39), (3.7, 28), (4.0, 31),
    (4.3, 17), (4.6, 16), (5.0, 21), (5.4, 11), (5.9, 35), (6.2, 41),
    (6.7, 53), (7.0, 72), (7.3, 46), (7.6, 38), (7.7, 53), (8.0, 86),
    (8.3, 66), (8.5, 57), (8.7, 61), (8.9, 28), (9.0, 73), (9.2, 67),
    (9.5, 69), (9.7, 54),
]
WIDTH, HEIGHT = 760, 676
NAVY, MUTED, LINE, ACCENT = "#17324d", "#536879", "#becbd4", "#b65d62"
SPECS = [
    ("observations", "A. Observations", None, None),
    ("steady", "B. Steady increase", lambda x: x, "x"),
    ("accelerating", "C. Accelerating", lambda x: x*x, "x**2"),
    ("tapering", "D. Tapering off", lambda x: 1-math.exp(-x/3.5), "1-exp(-x/3.5)"),
]


def fit_curve(basis):
    """Unique OLS minimum for y = a + b*g(x), with g fixed in advance."""
    z = [basis(x) for x, _ in POINTS]
    y = [y for _, y in POINTS]
    mean_z, mean_y = math.fsum(z)/len(z), math.fsum(y)/len(y)
    denominator = math.fsum((v-mean_z)**2 for v in z)
    assert denominator > 0  # Full-rank design; squared error is strictly convex.
    b = math.fsum((u-mean_z)*(v-mean_y) for u, v in zip(z, y))/denominator
    a = mean_y-b*mean_z
    curve = lambda x: a+b*basis(x)
    residuals = [observed-curve(x) for x, observed in POINTS]
    assert b > 0  # Each displayed shape is increasing over the observed domain.
    assert abs(math.fsum(residuals)) < 1e-7
    assert abs(math.fsum(u*r for u, r in zip(z, residuals))) < 1e-6
    return curve, {
        "method": "Ordinary least squares; intercept and amplitude fitted",
        "intercept": a, "amplitude": b,
        "sum_squared_residuals": math.fsum(r*r for r in residuals),
        "sum_residuals": math.fsum(residuals),
        "points_above": sum(r > 1e-10 for r in residuals),
        "points_below": sum(r < -1e-10 for r in residuals),
        "points_on_curve": sum(abs(r) <= 1e-10 for r in residuals),
        "residuals": residuals,
    }


def text(x, y, label, size=28, *, anchor="start", weight=400, fill=MUTED):
    return (f'<text x="{x:g}" y="{y:g}" font-family="Arial, Helvetica, sans-serif" '
            f'font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" '
            f'fill="{fill}">{escape(label)}</text>')


def xy(x, y):
    return 24 + 32*x, 272 - 1.95*y


def build():
    body = [f'<rect width="{WIDTH}" height="{HEIGHT}" fill="white"/>']
    panels = []
    domain = [min(x for x, _ in POINTS), max(x for x, _ in POINTS)]
    for i, (identifier, title, basis, basis_formula) in enumerate(SPECS):
        curve, fit = fit_curve(basis) if basis is not None else (None, None)
        formula = (f"{fit['intercept']:.12g} + {fit['amplitude']:.12g}*({basis_formula})"
                   if fit else None)
        left, top = 8 + (i % 2)*384, 12 + (i // 2)*314
        panel = [f'<g id="panel-{identifier}" transform="translate({left} {top})">',
                 text(8, 32, title, 30, weight=700, fill=NAVY),
                 '<path d="M24 77 V272 H344" fill="none" '
                 f'stroke="{MUTED}" stroke-width="2.5"/>']
        if curve is not None:
            # Trace the fitted curve only over the observed x range.
            xs = [domain[0]+(domain[1]-domain[0])*j/200 for j in range(201)]
            values = [(x, curve(x)) for x in xs]
            assert all(0 <= y <= 100 for _, y in values)
            coords = [xy(x, y) for x, y in values]
            d = " ".join(("M" if j == 0 else "L") + f"{x:.3f} {y:.3f}"
                         for j, (x, y) in enumerate(coords))
            panel.append(f'<path class="interpretation" d="{d}" fill="none" '
                         f'stroke="{ACCENT}" stroke-width="4.5" '
                         'stroke-linejoin="round" stroke-linecap="round"/>')
        # Identical data and transforms in all four panels; points remain above curves.
        panel.append('<g class="observations">')
        for x, y in POINTS:
            sx, sy = xy(x, y)
            panel.append(f'<circle cx="{sx:.3f}" cy="{sy:.3f}" r="4.8" '
                         f'fill="{NAVY}" stroke="white" stroke-width="1.3"/>')
        panel += ['</g>', '</g>']
        body.extend(panel)
        panels.append({"id": identifier, "title": title, "curve_formula": formula,
                       "fixed_basis": basis_formula, "fit": fit,
                       "curve_domain": domain if fit else None,
                       "coordinates": POINTS, "x_limits": [0, 10], "y_limits": [0, 100]})
    body += [f'<path d="M20 624 H740" stroke="{LINE}" stroke-width="1.5"/>',
             text(380, 653, "Same observations. Same scales.", 29, anchor="middle", weight=700, fill=NAVY)]
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" role="img" aria-labelledby="title desc">
<title id="title">Same evidence, different stories</title>
<desc id="desc">Four panels repeat the same 32 synthetic observations on identical time and outcome axes. Panel A shows the observations alone. Panels B, C, and D show least-squares fits under prescribed steady, accelerating, and tapering trend shapes. Each fit minimizes squared vertical residuals within its shape; the fits are not claimed to have equal support.</desc>
{chr(10).join(body)}
</svg>
'''
    root = ET.fromstring(svg)
    ns = {"s": "http://www.w3.org/2000/svg"}
    groups = root.findall('.//s:g[@class="observations"]', ns)
    signatures = [[tuple(sorted(c.attrib.items())) for c in g] for g in groups]
    assert len(groups) == 4 and len(signatures[0]) == 32
    assert all(s == signatures[0] for s in signatures)
    assert all(0 < x < 10 and 0 < y < 100 for x, y in POINTS)
    # The smallest retained label remains >12px in the HTML phone column.
    assert 29 * 330.5 / WIDTH >= 12
    (FIGURES / "model-underdetermination.svg").write_text(svg)
    source = FIGURES / "source" / "model-underdetermination.json"
    source.parent.mkdir(exist_ok=True)
    source.write_text(json.dumps({
        "status": "Authored synthetic teaching example; not empirical results",
        "figure": "30.1", "curve_status": "Least-squares fitted within prescribed trend shapes; not externally validated",
        "model_assumptions": "y=a+b*g(x); g(x) is x, x**2, or 1-exp(-x/3.5). The 3.5 time scale is held fixed from the previous illustration, not optimized.",
        "panel_layout": "Two by two, read left to right then top to bottom",
        "axis_display": "Plain axis lines; titles, ticks, and tick labels omitted",
        "units": "Arbitrary time and outcome units", "panels": panels,
        "verification": {"identical_observations": True, "identical_scales": True,
                         "observations_per_panel": 32, "minimum_label_px_at_330_5px": 29*330.5/WIDTH}
    }, indent=2) + "\n")
    print("Built Figure 30.1: 4 panels, identical 32-point examples and axis scales.")


if __name__ == "__main__":
    build()
