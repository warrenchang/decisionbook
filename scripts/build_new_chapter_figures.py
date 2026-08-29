#!/usr/bin/env python3
"""Build rights-safe figures added to the newer behavioral-economics chapters.

The source figures are SVG so text remains crisp in the HTML book. PNG
companions can also be generated when CairoSVG is available. Journal
screenshots are not copied: quantitative panels redraw reported values, while
conceptual panels are explicitly labelled as schematics.
"""

from __future__ import annotations

import argparse
import base64
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIGURES = ROOT / "figures"

NAVY = "#17324d"
BLUE = "#2f6f9f"
PALE_BLUE = "#eaf3f8"
ORANGE = "#c56a2d"
PALE_ORANGE = "#f7f1e8"
GREEN = "#447c55"
PALE_GREEN = "#edf4ed"
RED = "#a74343"
PALE_RED = "#fff0e9"
MUTED = "#66737f"
GRID = "#dce5ea"


def esc(value: str) -> str:
    return (
        value.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def txt(x, y, value, size=18, *, anchor="middle", weight=400, fill=NAVY,
        family="Arial, sans-serif", extra="") -> str:
    return (
        f'<text x="{x}" y="{y}" text-anchor="{anchor}" '
        f'font-family="{family}" font-size="{size}" font-weight="{weight}" '
        f'fill="{fill}" {extra}>{esc(str(value))}</text>'
    )


def rect(x, y, w, h, *, fill="#ffffff", stroke="#c8d7e2", sw=2, rx=16,
         extra="") -> str:
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
        f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}" {extra}/>'
    )


def multiline(x, y, lines, *, size=18, leading=26, anchor="middle", weight=400,
              fill=NAVY, family="Arial, sans-serif") -> str:
    out = []
    for i, line in enumerate(lines):
        out.append(txt(x, y + i * leading, line, size, anchor=anchor,
                       weight=weight, fill=fill, family=family))
    return "\n".join(out)


def document(title: str, desc: str, body: str, *, height=760) -> str:
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="{height}" viewBox="0 0 1200 {height}" role="img" aria-labelledby="title desc">
  <title id="title">{esc(title)}</title>
  <desc id="desc">{esc(desc)}</desc>
  <defs>
    <marker id="blueArrow" markerWidth="12" markerHeight="12" refX="10" refY="6" orient="auto"><path d="M0 0 L12 6 L0 12 Z" fill="{BLUE}"/></marker>
    <marker id="orangeArrow" markerWidth="12" markerHeight="12" refX="10" refY="6" orient="auto"><path d="M0 0 L12 6 L0 12 Z" fill="{ORANGE}"/></marker>
    <filter id="shadow"><feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="{NAVY}" flood-opacity="0.12"/></filter>
  </defs>
  <rect width="1200" height="{height}" fill="#ffffff"/>
{body}
</svg>
'''


def title_block(title: str, subtitle: str) -> str:
    return "\n".join([
        txt(600, 48, title, 33, weight=700, family="Georgia, serif"),
        txt(600, 80, subtitle, 18, fill=MUTED),
    ])


def euro_efficiency() -> str:
    body = [title_block(
        "The €20 note: three different efficiency claims",
        "Finding a reward is not the same as proving that prices are always right.",
    )]
    photo_path = FIGURES / "finance-euro-note-found.png"
    if not photo_path.is_file():
        raise FileNotFoundError(f"Missing supplied teaching photograph: {photo_path}")
    photo_data = base64.b64encode(photo_path.read_bytes()).decode("ascii")
    body += [
        rect(55, 145, 365, 455, fill="#f7fafc", stroke="#665b9a", sw=3, rx=26,
             extra='filter="url(#shadow)"'),
        '<defs><clipPath id="euroPhotoClip"><rect x="78" y="170" width="319" height="240" rx="16"/></clipPath></defs>',
        f'<image x="78" y="170" width="319" height="240" preserveAspectRatio="xMidYMid slice" clip-path="url(#euroPhotoClip)" href="data:image/png;base64,{photo_data}"/>',
        '<rect x="78" y="170" width="319" height="240" rx="16" fill="none" stroke="#c8d7e2" stroke-width="2"/>',
        txt(238, 448, "A €20 NOTE STILL ON THE GROUND", 17, weight=700, fill="#544981"),
        multiline(238, 480, ["Finding it required someone to notice,", "stop, and pick it up."], size=16, leading=24, fill=MUTED),
        rect(80, 540, 315, 42, fill=PALE_RED, stroke=RED, sw=2, rx=8),
        txt(237, 567, "SEARCH AND ATTENTION ARE COSTLY", 14, weight=700, fill=RED),
        '<path d="M420 372 L478 372" fill="none" stroke="%s" stroke-width="5"/>' % BLUE,
        '<path d="M478 212 L478 552" fill="none" stroke="%s" stroke-width="5"/>' % BLUE,
    ]
    boxes = [
        (520, 145, PALE_BLUE, BLUE, "1  INFORMATION MOVES QUICKLY",
         ["A specified signal can enter price", "within a short event window."],
         "Speed is an empirical claim."),
        (520, 315, PALE_GREEN, GREEN, "2  NO FREE LUNCH",
         ["A public rule does not reliably earn", "abnormal return after risk and costs."],
         "Search and implementation are costly."),
        (520, 485, PALE_ORANGE, ORANGE, "3  THE PRICE IS RIGHT",
         ["Market price equals a well-defined", "fundamental value."],
         "This is the strongest claim."),
    ]
    for x, y, fill, stroke, heading, lines, note in boxes:
        body += [
            f'<line x1="478" y1="{y + 67}" x2="{x - 4}" y2="{y + 67}" stroke="{BLUE}" stroke-width="5" marker-end="url(#blueArrow)"/>',
            rect(x, y, 625, 135, fill=fill, stroke=stroke, sw=3, rx=18,
                 extra='filter="url(#shadow)"'),
            txt(x + 28, y + 38, heading, 21, anchor="start", weight=700),
            multiline(x + 28, y + 70, lines, size=17, leading=24, anchor="start", fill=MUTED),
            txt(x + 597, y + 116, note, 14, anchor="end", weight=700, fill=stroke),
        ]
    body += [
        rect(110, 650, 980, 64, fill="#f7fafc", stroke="#c8d7e2", sw=2, rx=16),
        txt(600, 679, "The first two claims do not automatically establish the third.", 21, weight=700),
        txt(600, 703, "An opportunity may exist because discovering and exploiting it consumes attention, information, capital, and risk-bearing capacity.", 15, fill=MUTED),
    ]
    return document(
        "The €20 note and three meanings of market efficiency",
        "A photograph of a twenty-euro note left on the ground points to three separate claims: rapid information incorporation, no free lunch after risk and costs, and prices equal fundamental value. The first two claims do not imply the third.",
        "\n".join(body), height=740,
    )


def rare_event_sampling() -> str:
    body = [title_block(
        "A rare event can disappear from a small experience sample",
        "The probability of seeing no rare event after n independent draws is (1 − p)ⁿ.",
    )]
    x0, y0, w, h = 110, 150, 700, 460
    body += [rect(55, 112, 815, 540, fill="#f7fafc", stroke="#c8d7e2", sw=2, rx=18)]
    # Axes and grid.
    for q in [0, .2, .4, .6, .8, 1.0]:
        y = y0 + h * (1 - q)
        body.append(f'<line x1="{x0}" y1="{y:.1f}" x2="{x0+w}" y2="{y:.1f}" stroke="{GRID}" stroke-width="1.5"/>')
        body.append(txt(x0 - 18, y + 5, f"{int(q*100)}%", 14, anchor="end", fill=MUTED))
    for n in [0, 10, 20, 40, 60, 80, 100]:
        x = x0 + w * n / 100
        body.append(f'<line x1="{x:.1f}" y1="{y0}" x2="{x:.1f}" y2="{y0+h}" stroke="{GRID}" stroke-width="1"/>')
        body.append(txt(x, y0 + h + 27, str(n), 14, fill=MUTED))
    band_x1 = x0 + w * 11 / 100
    band_x2 = x0 + w * 19 / 100
    body += [
        f'<rect x="{band_x1:.1f}" y="{y0}" width="{band_x2-band_x1:.1f}" height="{h}" fill="#f6d9c7" opacity="0.55"/>',
        txt((band_x1 + band_x2) / 2, y0 + 25, "11–19", 13, weight=700, fill=ORANGE),
        txt(x0 + w / 2, y0 + h + 58, "Number of observations in the experience sample (n)", 17, weight=700),
        txt(35, y0 + h / 2, "Probability the rare event is absent", 17, weight=700,
            extra=f'transform="rotate(-90 35 {y0 + h/2})"'),
    ]
    for p, color, label in [(0.01, BLUE, "1% event"), (0.05, ORANGE, "5% event")]:
        points = []
        for n in range(0, 101):
            q = (1 - p) ** n
            x = x0 + w * n / 100
            y = y0 + h * (1 - q)
            points.append(f"{x:.1f},{y:.1f}")
        body.append(f'<polyline points="{" ".join(points)}" fill="none" stroke="{color}" stroke-width="6" stroke-linecap="round"/>')
        nlab = 72 if p == .01 else 38
        qlab = (1-p) ** nlab
        xlab = x0 + w * nlab / 100
        ylab = y0 + h * (1-qlab)
        body.append(txt(xlab + 8, ylab - 12, label, 17, anchor="start", weight=700, fill=color))
    body += [
        rect(900, 112, 255, 540, fill=PALE_ORANGE, stroke=ORANGE, sw=2, rx=18),
        txt(1027, 158, "At n = 15", 25, weight=700),
        txt(1027, 211, "86%", 54, weight=700, fill=BLUE),
        multiline(1027, 241, ["chance that a 1% event", "has not appeared"], size=16, leading=23, fill=MUTED),
        '<line x1="935" y1="300" x2="1120" y2="300" stroke="#d8c5aa" stroke-width="2"/>',
        txt(1027, 354, "46%", 54, weight=700, fill=ORANGE),
        multiline(1027, 384, ["chance that a 5% event", "has not appeared"], size=16, leading=23, fill=MUTED),
        rect(930, 470, 195, 125, fill="#ffffff", stroke="#c8d7e2", sw=2, rx=14),
        multiline(1027, 502, ["Absence from a sample", "is not evidence of", "impossibility."], size=17, leading=26, weight=700),
        txt(600, 700, "Mathematical derivation for independent sampling; real experience can also be selective, dependent, censored, or remembered unevenly.", 14, fill=MUTED),
    ]
    return document(
        "Probability that a rare event is absent from an experience sample",
        "Two curves show the chance that a one-percent or five-percent event has not appeared after up to one hundred independent observations. A highlighted band marks samples of eleven to nineteen observations. At fifteen observations, the absence probabilities are eighty-six percent and forty-six percent.",
        "\n".join(body), height=725,
    )


def mental_accounting_evidence() -> str:
    body = [title_block(
        "Two ways a narrow bracket changes an investment decision",
        "Original redraws of reported results; neither panel supplies a universal effect size.",
    )]
    body += [
        rect(45, 115, 540, 565, fill="#f7fafc", stroke="#c8d7e2", sw=2, rx=20),
        txt(315, 158, "Closing winners, keeping losers", 24, weight=700),
        txt(315, 188, "Odean (1998), brokerage sample", 16, fill=MUTED),
        rect(90, 235, 190, 145, fill=PALE_GREEN, stroke=GREEN, sw=3, rx=18),
        txt(185, 276, "WINNER", 22, weight=700, fill=GREEN),
        txt(185, 311, "sold", 32, weight=700),
        txt(185, 347, "account closed", 15, fill=MUTED),
        rect(350, 235, 190, 145, fill=PALE_RED, stroke=RED, sw=3, rx=18),
        txt(445, 276, "LOSER", 22, weight=700, fill=RED),
        txt(445, 311, "held", 32, weight=700),
        txt(445, 347, "loss not realized", 15, fill=MUTED),
        '<line x1="280" y1="307" x2="346" y2="307" stroke="%s" stroke-width="4" stroke-dasharray="8 7"/>' % BLUE,
        txt(315, 438, "+3.41 percentage points", 35, weight=700, fill=BLUE),
        multiline(315, 474, ["market-adjusted return of winners sold", "relative to losing positions retained", "over the following year"], size=17, leading=26, fill=MUTED),
        rect(90, 575, 450, 62, fill=PALE_ORANGE, stroke=ORANGE, sw=2, rx=14),
        txt(315, 602, "Forward-looking test", 17, weight=700, fill=ORANGE),
        txt(315, 625, "Would I buy this position today at this price?", 16, weight=700),
        rect(615, 115, 540, 565, fill="#f7fafc", stroke="#c8d7e2", sw=2, rx=20),
        txt(885, 158, "The same risk, a different horizon", 24, weight=700),
        txt(885, 188, "Benartzi & Thaler (1999)", 16, fill=MUTED),
        '<line x1="705" y1="555" x2="1080" y2="555" stroke="#8fa0ad" stroke-width="2"/>',
        '<line x1="705" y1="265" x2="705" y2="555" stroke="#8fa0ad" stroke-width="2"/>',
    ]
    # Bar heights on a 0-100 scale.
    for value, x, fill, label in [(40, 760, BLUE, "Annual return\ndistributions"), (90, 930, ORANGE, "Long-term return\ndistributions")]:
        bar_h = 2.7 * value
        body += [
            f'<rect x="{x}" y="{555-bar_h:.1f}" width="105" height="{bar_h:.1f}" rx="8" fill="{fill}"/>',
            txt(x + 52, 540 - bar_h, f"{value}%", 27, weight=700, fill=fill),
            multiline(x + 52, 585, label.split("\n"), size=17, leading=23, weight=700),
        ]
    for value in [0, 25, 50, 75, 100]:
        y = 555 - 2.7 * value
        body += [
            f'<line x1="700" y1="{y}" x2="1080" y2="{y}" stroke="{GRID}" stroke-width="1"/>',
            txt(690, y + 5, str(value), 13, anchor="end", fill=MUTED),
        ]
    body += [
        txt(640, 412, "Allocation to stocks (%)", 16, weight=700,
            extra='transform="rotate(-90 640 412)"'),
        txt(885, 654, "Evaluation frequency changes how often losses enter view.", 16, weight=700, fill=ORANGE),
        txt(600, 718, "Reported values are context-specific. Taxes, selection, information, implementation, and alternative mechanisms remain part of the audit.", 14, fill=MUTED),
    ]
    return document(
        "Mental-accounting evidence in investment decisions",
        "Two panels redraw reported investment findings. Winners sold outperformed losing positions retained by about 3.41 percentage points in market-adjusted return over the following year in Odean's brokerage sample. Participants shown annual return distributions allocated about forty percent to stocks, versus about ninety percent for long-term distributions in Benartzi and Thaler's study.",
        "\n".join(body), height=745,
    )


def event_study() -> str:
    body = [title_block(
        "An event study separates reaction from drift",
        "A schematic of the design logic behind post-earnings-announcement drift—not a reproduced effect-size estimate.",
    )]
    # Timeline.
    body += [
        rect(55, 112, 1090, 175, fill="#f7fafc", stroke="#c8d7e2", sw=2, rx=18),
        txt(600, 148, "Define the windows before reading the return path", 22, weight=700),
        '<line x1="125" y1="222" x2="1070" y2="222" stroke="%s" stroke-width="5"/>' % BLUE,
        '<rect x="165" y="195" width="360" height="54" rx="8" fill="%s" stroke="%s" stroke-width="2"/>' % (PALE_BLUE, BLUE),
        txt(345, 216, "ESTIMATION WINDOW", 16, weight=700, fill=BLUE),
        txt(345, 239, "fit the expected-return model", 14, fill=MUTED),
        '<rect x="548" y="188" width="125" height="68" rx="8" fill="%s" stroke="%s" stroke-width="3"/>' % (PALE_ORANGE, ORANGE),
        txt(610, 213, "EVENT", 17, weight=700, fill=ORANGE),
        txt(610, 239, "first public time", 13, fill=MUTED),
        '<rect x="700" y="195" width="305" height="54" rx="8" fill="%s" stroke="%s" stroke-width="2"/>' % (PALE_GREEN, GREEN),
        txt(852, 216, "POST-EVENT WINDOW", 16, weight=700, fill=GREEN),
        txt(852, 239, "test persistence or reversal", 14, fill=MUTED),
    ]
    # Schematic CAR chart.
    x0, y0, w, h = 150, 350, 760, 285
    body += [
        rect(55, 315, 900, 370, fill="#f7fafc", stroke="#c8d7e2", sw=2, rx=18),
        txt(505, 350, "Cumulative abnormal return (schematic)", 22, weight=700),
        f'<line x1="{x0}" y1="{y0+h/2}" x2="{x0+w}" y2="{y0+h/2}" stroke="#8fa0ad" stroke-width="2"/>',
        f'<line x1="{x0+300}" y1="{y0}" x2="{x0+300}" y2="{y0+h}" stroke="{ORANGE}" stroke-width="3" stroke-dasharray="8 7"/>',
        txt(x0 + 300, y0 + h + 28, "0  announcement", 15, weight=700, fill=ORANGE),
        txt(x0 + 20, y0 + h + 28, "before", 14, fill=MUTED),
        txt(x0 + 530, y0 + h + 28, "after", 14, fill=MUTED),
        f'<path d="M{x0} {y0+h/2} L{x0+300} {y0+h/2}" fill="none" stroke="{NAVY}" stroke-width="6" stroke-linecap="round"/>',
        f'<path d="M{x0+300} {y0+h/2} L{x0+320} {y0+h/2-62} C{x0+350} {y0+h/2-78} {x0+405} {y0+h/2-84} {x0+450} {y0+h/2-88} C{x0+560} {y0+h/2-105} {x0+660} {y0+h/2-135} {x0+w} {y0+h/2-150}" fill="none" stroke="{GREEN}" stroke-width="6" stroke-linecap="round"/>',
        f'<path d="M{x0+300} {y0+h/2} L{x0+320} {y0+h/2+62} C{x0+350} {y0+h/2+78} {x0+405} {y0+h/2+84} {x0+450} {y0+h/2+88} C{x0+560} {y0+h/2+105} {x0+660} {y0+h/2+135} {x0+w} {y0+h/2+150}" fill="none" stroke="{RED}" stroke-width="6" stroke-linecap="round"/>',
        f'<circle cx="{x0+300}" cy="{y0+h/2}" r="7" fill="{ORANGE}"/>',
        txt(x0 + w - 8, y0 + h/2 - 160, "positive surprise", 16, anchor="end", weight=700, fill=GREEN),
        txt(x0 + w - 8, y0 + h/2 + 176, "negative surprise", 16, anchor="end", weight=700, fill=RED),
        rect(985, 315, 160, 370, fill=PALE_ORANGE, stroke=ORANGE, sw=2, rx=18),
        txt(1065, 358, "AUDIT", 22, weight=700, fill=ORANGE),
        multiline(1065, 404, ["event time", "expected-return", "model", "confounds", "uncertainty", "tradable timing", "costs"], size=16, leading=38, weight=700),
        txt(600, 725, "A delayed separation can indicate slow updating, but also benchmark error, overlapping news, frictions, or ex-post sample construction.", 14, fill=MUTED),
    ]
    return document(
        "Event-study design and a schematic post-earnings-announcement drift",
        "A timeline distinguishes the estimation, event, and post-event windows. A schematic cumulative abnormal return chart shows an immediate reaction followed by positive or negative drift after earnings surprises. An audit lists event time, expected-return model, confounds, uncertainty, tradable timing, and costs.",
        "\n".join(body), height=750,
    )


def bubble_strategies() -> str:
    values = [
        ("Momentum traders", 36.5, ORANGE),
        ("Fundamental-value traders", 33.1, BLUE),
        ("Rational speculators", 25.4, GREEN),
        ("Other classified behavior", 5.0, "#8a7895"),
    ]
    body = [title_block(
        "A bubble can contain several strategies at once",
        "Original redraw of one experimental classification reported by Haruvy and Noussair (2006).",
    )]
    body += [rect(55, 112, 760, 540, fill="#f7fafc", stroke="#c8d7e2", sw=2, rx=18)]
    x0, maxw = 315, 435
    for i, (label, value, color) in enumerate(values):
        y = 175 + i * 108
        width = maxw * value / 40
        body += [
            txt(285, y + 32, label, 18, anchor="end", weight=700),
            f'<rect x="{x0}" y="{y}" width="{width:.1f}" height="52" rx="8" fill="{color}"/>',
            txt(x0 + width + 14, y + 34, f"{value:.1f}%", 22, anchor="start", weight=700, fill=color),
        ]
    body += [
        '<line x1="315" y1="605" x2="750" y2="605" stroke="#8fa0ad" stroke-width="2"/>',
        txt(532, 634, "Share of classified behavior", 16, weight=700),
        rect(850, 112, 305, 540, fill=PALE_ORANGE, stroke=ORANGE, sw=2, rx=18),
        txt(1002, 158, "Why the mix matters", 23, weight=700),
        rect(890, 195, 225, 82, fill="#ffffff", stroke=ORANGE, sw=2, rx=14),
        multiline(1002, 229, ["Fundamentals anchor", "some decisions."], size=17, leading=25, weight=700),
        rect(890, 300, 225, 82, fill="#ffffff", stroke=ORANGE, sw=2, rx=14),
        multiline(1002, 334, ["Momentum can reinforce", "the observed trend."], size=17, leading=25, weight=700),
        rect(890, 405, 225, 105, fill="#ffffff", stroke=ORANGE, sw=2, rx=14),
        multiline(1002, 439, ["A rational trader may", "ride a bubble while", "planning to exit first."], size=17, leading=25, weight=700),
        txt(1002, 566, "One market, different", 18, weight=700, fill=ORANGE),
        txt(1002, 591, "beliefs and horizons", 18, weight=700, fill=ORANGE),
        txt(600, 704, "The shares describe one experimental setting and classification rule; they are not population estimates of investor types.", 14, fill=MUTED),
    ]
    return document(
        "Strategy shares in an experimental asset market",
        "A horizontal bar chart shows momentum traders at 36.5 percent, fundamental-value traders at 33.1 percent, rational speculators at 25.4 percent, and other classified behavior at about 5 percent in one experimental classification. A side panel explains how different strategies can coexist in one bubble.",
        "\n".join(body), height=730,
    )


def level_k() -> str:
    levels = [
        ("LEVEL 0", "50", "random-choice anchor", "#8a7895", "#f3eff5"),
        ("LEVEL 1", "33", "⅔ of 50", BLUE, PALE_BLUE),
        ("LEVEL 2", "22", "⅔ of 33", GREEN, PALE_GREEN),
        ("LEVEL 3", "15", "⅔ of 22", ORANGE, PALE_ORANGE),
        ("EQUILIBRIUM", "0", "continued iteration", RED, PALE_RED),
    ]
    body = [title_block(
        "The ⅔ guessing game as a reasoning ladder",
        "Each step best responds to a simpler model of what other players may choose.",
    )]
    for i, (level, number, note, stroke, fill) in enumerate(levels):
        x = 40 + i * 232
        body += [
            rect(x, 170, 195, 250, fill=fill, stroke=stroke, sw=3, rx=20,
                 extra='filter="url(#shadow)"'),
            txt(x + 97, 213, level, 18, weight=700, fill=stroke),
            txt(x + 97, 304, number, 72, weight=700, fill=stroke, family="Georgia, serif"),
            txt(x + 97, 347, note, 15, weight=700, fill=MUTED),
        ]
        if i < len(levels) - 1:
            body.append(f'<line x1="{x+195}" y1="295" x2="{x+229}" y2="295" stroke="{BLUE}" stroke-width="4" marker-end="url(#blueArrow)"/>')
    body += [
        rect(80, 485, 1040, 145, fill="#f7fafc", stroke="#c8d7e2", sw=2, rx=18),
        txt(600, 525, "The observed number does not reveal the reason by itself", 22, weight=700),
        multiline(600, 558, ["The same choice can reflect a different belief, arithmetic error, anchoring, a social focal point,", "or a deeper best response. Measure beliefs and comprehension before assigning a strategic level."], size=17, leading=27, fill=MUTED),
        txt(600, 690, "The numerical ladder is the theoretical level-k illustration for a target equal to two-thirds of the group mean (Nagel, 1995).", 14, fill=MUTED),
    ]
    return document(
        "Level-k reasoning in the two-thirds guessing game",
        "Five evenly spaced boxes show a theoretical reasoning ladder from a random-choice anchor of fifty, to level-one thirty-three, level-two twenty-two, level-three fifteen, and the Nash equilibrium zero. A boundary note warns that a number does not uniquely identify beliefs or reasoning depth.",
        "\n".join(body), height=720,
    )


def social_preference_games() -> str:
    body = [title_block(
        "Change one rule, and the meaning of giving changes",
        "Game design separates strategic rejection, generosity, and the permission to take.",
    )]
    cards = [
        (45, PALE_BLUE, BLUE, "ULTIMATUM", ["Proposer offers a split", "Responder accepts or rejects", "Rejection gives both zero"],
         ["Modal offers: 40–50%", "Mean offers: 30–40%", "Offers below 20%: rejected", "about half the time"]),
        (425, PALE_GREEN, GREEN, "DICTATOR", ["Allocator chooses a split", "Recipient cannot reject", "Strategic punishment removed"],
         ["Average giving about 20%", "in one classic comparison", "Closer to 10% under", "double-blind procedures"]),
        (805, PALE_ORANGE, ORANGE, "TAKE / MENU VARIANTS", ["Allocator may give or take", "Property rights and options vary", "The action acquires new meaning"],
         ["Giving can fall when taking", "or sorting out is available", "Menu and observability are", "part of the treatment"]),
    ]
    for x, fill, stroke, heading, mechanics, evidence in cards:
        body += [
            rect(x, 120, 350, 500, fill=fill, stroke=stroke, sw=3, rx=20,
                 extra='filter="url(#shadow)"'),
            txt(x + 175, 164, heading, 22, weight=700, fill=stroke),
            rect(x + 35, 195, 280, 125, fill="#ffffff", stroke=stroke, sw=2, rx=14),
            multiline(x + 175, 230, mechanics, size=17, leading=31, weight=700),
            txt(x + 175, 364, "REPORTED PATTERN", 16, weight=700, fill=stroke),
            multiline(x + 175, 402, evidence, size=17, leading=32, fill=NAVY),
        ]
    body += [
        rect(125, 650, 950, 58, fill="#f7fafc", stroke="#c8d7e2", sw=2, rx=14),
        txt(600, 676, "Historical regularities, not human constants: stakes, anonymity, entitlement, population, culture, repetition, and procedure matter.", 15, weight=700),
        txt(600, 733, "Sources for the reported ranges: Forsythe et al. (1994), Hoffman et al. (1994), Camerer (2003), and Oosterbeek et al. (2004).", 14, fill=MUTED),
    ]
    return document(
        "Ultimatum, dictator, and take-game designs",
        "Three cards compare the mechanics and reported patterns of ultimatum, dictator, and take or menu-variant games. The historical regularities are explicitly bounded by stakes, anonymity, entitlement, population, culture, repetition, and procedure.",
        "\n".join(body), height=755,
    )


def income_wellbeing() -> str:
    body = [title_block(
        "Income and well-being: what changed across three analyses",
        "The apparent conflict becomes smaller when the measure and the position in the well-being distribution are kept visible.",
    )]
    # Shared axes for three deliberately schematic panels.
    panels = [
        (45, "2010", "Kahneman & Deaton", ["Life evaluation rose with log income.", "Emotional well-being appeared to flatten", "near a US income category around $75,000."], "plateau"),
        (425, "2021", "Killingsworth", ["Repeated experience reports showed", "experienced well-being continuing to rise", "beyond that level in the studied sample."], "rise"),
        (805, "2023", "Adversarial collaboration", ["Flattening appeared mainly among the", "least happy part of the distribution;", "other groups continued to rise."], "split"),
    ]
    for x, year, cite, lines, kind in panels:
        body += [
            rect(x, 115, 350, 500, fill="#f7fafc", stroke="#c8d7e2", sw=2, rx=20),
            txt(x + 175, 158, year, 28, weight=700, fill=BLUE),
            txt(x + 175, 187, cite, 16, weight=700, fill=MUTED),
            f'<line x1="{x+65}" y1="420" x2="{x+305}" y2="420" stroke="#8fa0ad" stroke-width="2"/>',
            f'<line x1="{x+65}" y1="240" x2="{x+65}" y2="420" stroke="#8fa0ad" stroke-width="2"/>',
            txt(x + 185, 447, "log income", 14, weight=700, fill=MUTED),
        ]
        if kind == "plateau":
            body += [
                f'<path d="M{x+70} 400 C{x+120} 345 {x+170} 305 {x+290} 272" fill="none" stroke="{BLUE}" stroke-width="5"/>',
                f'<path d="M{x+70} 395 C{x+125} 322 {x+175} 300 {x+290} 299" fill="none" stroke="{ORANGE}" stroke-width="5" stroke-dasharray="9 7"/>',
                txt(x + 285, 266, "evaluation", 13, anchor="end", weight=700, fill=BLUE),
                txt(x + 285, 318, "affect", 13, anchor="end", weight=700, fill=ORANGE),
            ]
        elif kind == "rise":
            body += [
                f'<path d="M{x+70} 398 C{x+125} 348 {x+180} 320 {x+290} 276" fill="none" stroke="{GREEN}" stroke-width="5"/>',
                txt(x + 285, 268, "experienced well-being", 13, anchor="end", weight=700, fill=GREEN),
            ]
        else:
            body += [
                f'<path d="M{x+70} 400 C{x+130} 330 {x+185} 312 {x+290} 310" fill="none" stroke="{RED}" stroke-width="5"/>',
                f'<path d="M{x+70} 395 C{x+125} 345 {x+180} 310 {x+290} 268" fill="none" stroke="{GREEN}" stroke-width="5"/>',
                txt(x + 285, 329, "least happy group", 13, anchor="end", weight=700, fill=RED),
                txt(x + 285, 260, "happier groups", 13, anchor="end", weight=700, fill=GREEN),
            ]
        body += [multiline(x + 175, 493, lines, size=15, leading=25, fill=NAVY)]
    body += [
        rect(105, 645, 990, 62, fill=PALE_ORANGE, stroke=ORANGE, sw=2, rx=15),
        txt(600, 673, "No universal magic number follows: year, prices, sample, measure, model, and distribution all matter.", 17, weight=700),
        txt(600, 730, "Curves are an evidence-synthesis schematic, not digitized effect-size estimates from the published figures.", 14, fill=MUTED),
    ]
    return document(
        "Synthesis of income and subjective well-being evidence",
        "Three schematic panels summarize the 2010 finding of rising life evaluation and flattening emotional well-being, the 2021 finding of experienced well-being rising beyond the earlier threshold, and the 2023 reconciliation showing flattening mainly among the least happy group. The figure warns against a universal income threshold.",
        "\n".join(body), height=755,
    )


FIGURE_BUILDERS = {
    "finance-euro-efficiency": euro_efficiency,
    "experience-rare-event-sampling": rare_event_sampling,
    "mental-accounting-evidence-redraw": mental_accounting_evidence,
    "finance-event-study-drift": event_study,
    "bubble-trader-strategies-redraw": bubble_strategies,
    "level-k-reasoning-ladder": level_k,
    "social-preference-games-redraw": social_preference_games,
    "income-wellbeing-evidence-synthesis": income_wellbeing,
}


def build_png(svg_path: Path, png_path: Path) -> None:
    try:
        import cairosvg
    except ImportError as exc:  # pragma: no cover - environment-specific guidance
        raise SystemExit(
            "PNG generation requires cairosvg. Install it or omit --png and use another SVG renderer."
        ) from exc
    cairosvg.svg2png(
        url=str(svg_path),
        write_to=str(png_path),
        output_width=1800,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--png", action="store_true", help="also generate EPUB PNG companions")
    args = parser.parse_args()
    FIGURES.mkdir(parents=True, exist_ok=True)
    for stem, builder in FIGURE_BUILDERS.items():
        svg_path = FIGURES / f"{stem}.svg"
        svg_path.write_text(builder(), encoding="utf-8")
        if args.png:
            build_png(svg_path, FIGURES / f"{stem}.png")
        print(svg_path.relative_to(ROOT))


if __name__ == "__main__":
    main()
