#!/usr/bin/env python3
"""Build the recurring decision-loop navigation figures as self-contained SVGs."""

from pathlib import Path
from xml.sax.saxutils import escape


OUT = Path(__file__).resolve().parents[1] / "figures"

NODES = [
    ("context", ["Context &", "information"]),
    ("notice", ["Notice &", "interpret"]),
    ("predict", ["Predict &", "value"]),
    ("construct", ["Construct", "options"]),
    ("choose", ["Choose &", "commit"]),
    ("act", ["Act"]),
    ("learn", ["Observe &", "learn"]),
]

VARIANTS = {
    "master-loop.svg": set(),
    "master-loop-part-1.svg": {"context", "notice", "predict", "construct", "choose", "act", "learn"},
    "master-loop-part-2.svg": {"notice", "predict", "learn"},
    "master-loop-part-3.svg": {"predict", "choose", "act", "learn"},
    "master-loop-interlude.svg": {"predict", "choose", "act", "learn", "social"},
    "master-loop-part-4.svg": {"construct", "choose", "act", "learn", "social"},
    "master-loop-part-5.svg": {"notice", "predict", "social"},
    "master-loop-part-6.svg": {"construct", "choose", "act", "social"},
    "master-loop-part-7.svg": {"context", "construct", "act", "learn", "social"},
}


def text_block(x: int, y: int, lines: list[str], color: str) -> str:
    first_y = y - (len(lines) - 1) * 13
    tspans = []
    for i, line in enumerate(lines):
        tspans.append(f'<tspan x="{x}" y="{first_y + i * 26}">{escape(line)}</tspan>')
    return f'<text class="node-label" fill="{color}" text-anchor="middle">{"".join(tspans)}</text>'


def render(active: set[str]) -> str:
    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="1400" height="610" viewBox="0 0 1400 610" role="img" aria-labelledby="title desc">',
        '<title id="title">The recursive decision loop and its social environment</title>',
        '<desc id="desc">Context and information feed noticing and interpretation, prediction and valuation, option construction, choice, action, and learning. Other minds, institutions, and designed environments can alter every stage.</desc>',
        '<defs>',
        '<marker id="arrow" markerWidth="10" markerHeight="10" refX="8.5" refY="3.5" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L9,3.5 L0,7 z" fill="#587189"/></marker>',
        '<marker id="arrow-accent" markerWidth="10" markerHeight="10" refX="8.5" refY="3.5" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L9,3.5 L0,7 z" fill="#c44e52"/></marker>',
        '<style>.node-label{font:600 22px -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}.small{font:500 18px -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}.outer{font:650 24px -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}.mode{font:600 18px -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}</style>',
        '</defs>',
        '<rect x="18" y="18" width="1364" height="574" rx="28" fill="#f7f9fc" stroke="#9fb2c3" stroke-width="2"/>',
    ]

    social_active = "social" in active or not active
    outer_fill = "#e9f2f7" if social_active else "#f0f3f6"
    outer_stroke = "#236b8e" if "social" in active else "#8ea5b7"
    parts.extend([
        f'<rect x="58" y="48" width="1284" height="112" rx="20" fill="{outer_fill}" stroke="{outer_stroke}" stroke-width="3"/>',
        '<text x="700" y="86" class="outer" fill="#183047" text-anchor="middle">OTHER MINDS, INSTITUTIONS, AND DESIGNED ENVIRONMENTS</text>',
        '<text x="700" y="122" class="small" fill="#4c6173" text-anchor="middle">can change what is noticed, predicted, valued, possible, chosen, reinforced, and learned</text>',
        '<path d="M700 160 L700 223" stroke="#587189" stroke-width="3" marker-end="url(#arrow)"/>',
    ])

    x0, gap, w, h, y = 55, 18, 165, 108, 226
    for idx, (key, lines) in enumerate(NODES):
        x = x0 + idx * (w + gap)
        is_active = key in active or not active
        fill = "#dceef5" if is_active else "#eef2f5"
        stroke = "#236b8e" if key in active else "#9aabb8"
        width = "4" if key in active else "2"
        text_color = "#12364a" if is_active else "#607282"
        parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="17" fill="{fill}" stroke="{stroke}" stroke-width="{width}"/>')
        parts.append(text_block(x + w // 2, y + h // 2 + 7, lines, text_color))
        if idx < len(NODES) - 1:
            x1 = x + w + 3
            x2 = x + w + gap - 5
            accent = key in active and NODES[idx + 1][0] in active
            stroke_color = "#c44e52" if accent else "#587189"
            marker = "arrow-accent" if accent else "arrow"
            sw = "4" if accent else "3"
            parts.append(f'<path d="M{x1} {y + h // 2} L{x2} {y + h // 2}" stroke="{stroke_color}" stroke-width="{sw}" marker-end="url(#{marker})"/>')

    last_x = x0 + 6 * (w + gap) + w // 2
    first_x = x0 + w // 2
    parts.append(f'<path d="M{last_x} {y+h+4} C{last_x} 398, {first_x} 398, {first_x} {y+h+4}" fill="none" stroke="#587189" stroke-width="3" marker-end="url(#arrow)"/>')
    # Keep the label below the return path so the curve never strikes through
    # the text in either browser or EPUB rasterization.
    parts.append('<text x="700" y="425" class="small" fill="#4c6173" text-anchor="middle">feedback can revise the model, the environment, or both</text>')

    modes = ["ASK", "INFLUENCE", "COORDINATE", "NEGOTIATE", "DESIGN"]
    mw, mg, mx, my = 208, 20, 140, 457
    for i, label in enumerate(modes):
        x = mx + i * (mw + mg)
        fill = "#f8e4dc" if "social" in active else "#eef2f5"
        stroke = "#c44e52" if "social" in active else "#9aabb8"
        parts.append(f'<rect x="{x}" y="{my}" width="{mw}" height="58" rx="29" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')
        parts.append(f'<text x="{x + mw/2}" y="{my+37}" class="mode" fill="#4b3a36" text-anchor="middle">{label}</text>')
    parts.append('<text x="700" y="558" class="small" fill="#607282" text-anchor="middle">interaction modes—not a required sequence</text>')
    parts.append('</svg>')
    return "\n".join(parts) + "\n"


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for filename, active in VARIANTS.items():
        (OUT / filename).write_text(render(active), encoding="utf-8")


if __name__ == "__main__":
    main()
