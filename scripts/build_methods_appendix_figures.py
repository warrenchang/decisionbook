#!/usr/bin/env python3
"""Build original, rights-safe figures for the research-methods appendices.

The first two figures are conceptual schematics. The third is a deterministic
simulation of a simple two-arm study followed by a significance-only reporting
rule. The simulation outputs both the figure and its study-level data so that
the visual can be regenerated and checked independently.
"""

from __future__ import annotations

import csv
import json
import math
import random
from pathlib import Path
from xml.sax.saxutils import escape


ROOT = Path(__file__).resolve().parents[1]
FIGURES = ROOT / "figures"
SOURCE = FIGURES / "source"

NAVY = "#17324d"
BLUE = "#2f6f9f"
PALE_BLUE = "#eaf3f8"
GREEN = "#447c55"
PALE_GREEN = "#edf4ed"
ORANGE = "#c56a2d"
PALE_ORANGE = "#f7f1e8"
RED = "#a74343"
PALE_RED = "#fff0e9"
PURPLE = "#6f5aa7"
PALE_PURPLE = "#f0ecf8"
MUTED = "#5f7080"
LIGHT = "#d3dee6"
BG = "#f8fafc"


def text(x: float, y: float, value: str, size: int = 24, *, anchor: str = "middle",
         weight: int = 400, fill: str = NAVY, extra: str = "") -> str:
    return (
        f'<text x="{x}" y="{y}" text-anchor="{anchor}" '
        f'font-family="Arial, Helvetica, sans-serif" font-size="{size}" '
        f'font-weight="{weight}" fill="{fill}" {extra}>{escape(value)}</text>'
    )


def lines(x: float, y: float, values: list[str], size: int = 24, *, leading: int = 31,
          anchor: str = "middle", weight: int = 400, fill: str = NAVY) -> str:
    return "\n".join(
        text(x, y + i * leading, value, size, anchor=anchor, weight=weight, fill=fill)
        for i, value in enumerate(values)
    )


def rect(x: float, y: float, width: float, height: float, *, fill: str = "#ffffff",
         stroke: str = LIGHT, sw: float = 2, radius: int = 18) -> str:
    return (
        f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="{radius}" '
        f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
    )


def svg_document(title: str, description: str, body: str, width: int, height: int) -> str:
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
  <title id="title">{escape(title)}</title>
  <desc id="desc">{escape(description)}</desc>
  <defs>
    <marker id="arrow" viewBox="0 0 10 8" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto" markerUnits="userSpaceOnUse">
      <path d="M0.5 0.8 L9 4 L0.5 7.2 Z" fill="{MUTED}"/>
    </marker>
    <marker id="blue-arrow" viewBox="0 0 10 8" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto" markerUnits="userSpaceOnUse">
      <path d="M0.5 0.8 L9 4 L0.5 7.2 Z" fill="{BLUE}"/>
    </marker>
    <marker id="red-arrow" viewBox="0 0 10 8" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto" markerUnits="userSpaceOnUse">
      <path d="M0.5 0.8 L9 4 L0.5 7.2 Z" fill="{RED}"/>
    </marker>
  </defs>
  <rect width="{width}" height="{height}" fill="{BG}"/>
{body}
</svg>
'''


def sampling_vs_assignment() -> str:
    body: list[str] = [
        text(500, 54, "Two random processes answer different questions", 34, weight=700),
        text(500, 90, "Sampling links a sample to a population; assignment creates a causal contrast inside the study.", 21, fill=MUTED),
        rect(35, 125, 450, 575, fill="#ffffff", stroke=BLUE, sw=3, radius=24),
        rect(515, 125, 450, 575, fill="#ffffff", stroke=GREEN, sw=3, radius=24),
        text(260, 173, "RANDOM SAMPLING", 27, weight=700, fill=BLUE),
        text(740, 173, "RANDOM ASSIGNMENT", 27, weight=700, fill=GREEN),
    ]

    # Population and sampled units.
    body += [rect(83, 207, 354, 157, fill=PALE_BLUE, stroke=BLUE, sw=2)]
    body += [text(260, 239, "DEFINED POPULATION", 22, weight=700)]
    for row in range(4):
        for col in range(9):
            x = 116 + col * 36
            y = 273 + row * 23
            fill = BLUE if (row, col) in {(0, 1), (0, 6), (1, 3), (1, 8), (2, 0), (2, 5), (3, 2), (3, 7)} else "#9fbacc"
            body.append(f'<circle cx="{x}" cy="{y}" r="7" fill="{fill}"/>')
    body += [
        '<line x1="260" y1="364" x2="260" y2="407" stroke="%s" stroke-width="3" marker-end="url(#arrow)"/>' % MUTED,
        rect(105, 416, 310, 98, fill="#ffffff", stroke=BLUE, sw=2),
        text(260, 453, "PROBABILITY SAMPLE", 22, weight=700),
    ]
    for col in range(8):
        body.append(f'<circle cx="{148 + col * 32}" cy="486" r="8" fill="{BLUE}"/>')
    body += [
        '<line x1="260" y1="514" x2="260" y2="556" stroke="%s" stroke-width="3" marker-end="url(#blue-arrow)"/>' % BLUE,
        rect(87, 565, 346, 92, fill=PALE_BLUE, stroke=BLUE, sw=2),
        text(260, 600, "SUPPORTS A POPULATION CLAIM", 20, weight=700, fill=BLUE),
        text(260, 632, "under the sampling design", 20, fill=MUTED),
    ]

    # Eligible study sample and randomized conditions.
    body += [
        rect(563, 207, 354, 112, fill=PALE_GREEN, stroke=GREEN, sw=2),
        text(740, 247, "ELIGIBLE STUDY SAMPLE", 22, weight=700),
    ]
    for col in range(10):
        body.append(f'<circle cx="{596 + col * 32}" cy="284" r="8" fill="{GREEN}"/>')
    body += [
        '<line x1="740" y1="319" x2="740" y2="350" stroke="%s" stroke-width="3"/>' % MUTED,
        '<line x1="638" y1="350" x2="843" y2="350" stroke="%s" stroke-width="3"/>' % MUTED,
        '<line x1="638" y1="350" x2="638" y2="383" stroke="%s" stroke-width="3" marker-end="url(#arrow)"/>' % MUTED,
        '<line x1="843" y1="350" x2="843" y2="383" stroke="%s" stroke-width="3" marker-end="url(#arrow)"/>' % MUTED,
        rect(550, 387, 175, 126, fill=PALE_BLUE, stroke=BLUE, sw=2),
        rect(755, 387, 175, 126, fill=PALE_ORANGE, stroke=ORANGE, sw=2),
        text(638, 426, "CONDITION A", 21, weight=700, fill=BLUE),
        text(843, 426, "CONDITION B", 21, weight=700, fill=ORANGE),
        lines(638, 460, ["outcomes", "by assignment"], 19, leading=25, fill=MUTED),
        lines(843, 460, ["outcomes", "by assignment"], 19, leading=25, fill=MUTED),
        text(740, 540, "COMPARE OUTCOMES", 19, weight=700, fill=GREEN),
        rect(567, 565, 346, 92, fill=PALE_GREEN, stroke=GREEN, sw=2),
        text(740, 600, "SUPPORTS AN INTERNAL CONTRAST", 20, weight=700, fill=GREEN),
        text(740, 632, "if assignment and follow-up hold", 20, fill=MUTED),
        rect(35, 731, 930, 126, fill=PALE_RED, stroke=RED, sw=2, radius=20),
        text(500, 771, "NEITHER RANDOM PROCESS IS A UNIVERSAL REPAIR", 23, weight=700, fill=RED),
        lines(500, 807, ["Sampling alone does not identify a treatment effect. Assignment alone does not establish transportability.",
                         "Neither one by itself fixes noncompliance, missing outcomes, attrition, or interference."],
              19, leading=27, fill=NAVY),
    ]
    return svg_document(
        "Random sampling and random assignment answer different questions",
        "Two side-by-side panels distinguish random sampling from a defined population into a probability sample, which supports population claims under the sampling design, from random assignment of an eligible study sample into conditions, which supports an internal causal contrast. A boundary box explains that neither process alone fixes noncompliance, missingness, attrition, interference, or transportability.",
        "\n".join(body), 1000, 885,
    )


def participant_flow() -> str:
    body: list[str] = [
        text(500, 54, "Follow assignment all the way to analysis", 34, weight=700),
        text(500, 90, "Receipt, observation, analysis, and exposure to other arms are distinct events.", 21, fill=MUTED),
        rect(275, 124, 450, 86, fill=PALE_PURPLE, stroke=PURPLE, sw=3),
        text(500, 160, "ELIGIBLE AND RANDOMIZED", 25, weight=700, fill=PURPLE),
        text(500, 190, "assignment defines the ITT groups", 20, fill=MUTED),
        '<line x1="500" y1="210" x2="500" y2="248" stroke="%s" stroke-width="3"/>' % MUTED,
        '<line x1="250" y1="248" x2="750" y2="248" stroke="%s" stroke-width="3"/>' % MUTED,
        '<line x1="250" y1="248" x2="250" y2="296" stroke="%s" stroke-width="3" marker-end="url(#arrow)"/>' % MUTED,
        '<line x1="750" y1="248" x2="750" y2="296" stroke="%s" stroke-width="3" marker-end="url(#arrow)"/>' % MUTED,
    ]

    stages = [
        (300, "TREATMENT RECEIPT", "some may not receive A", "some may access A or miss B", PALE_GREEN, GREEN),
        (500, "OUTCOME OBSERVATION", "some outcomes may be missing", "some outcomes may be missing", PALE_BLUE, BLUE),
        (700, "ANALYSIS", "retain assignment label", "retain assignment label", PALE_ORANGE, ORANGE),
    ]
    for y, heading, left_note, right_note, fill, stroke in stages:
        body += [
            rect(70, y, 360, 128, fill=fill, stroke=stroke, sw=2),
            rect(570, y, 360, 128, fill=fill, stroke=stroke, sw=2),
            text(250, y + 39, ("ASSIGNED A" if y == 300 else heading), 21, weight=700, fill=(BLUE if y == 300 else stroke)),
            text(750, y + 39, ("ASSIGNED B" if y == 300 else heading), 21, weight=700, fill=(ORANGE if y == 300 else stroke)),
            text(250, y + 72, (heading if y == 300 else left_note), 19, weight=(700 if y == 300 else 400), fill=(GREEN if y == 300 else MUTED)),
            text(750, y + 72, (heading if y == 300 else right_note), 19, weight=(700 if y == 300 else 400), fill=(GREEN if y == 300 else MUTED)),
            text(250, y + 105, (left_note if y == 300 else ""), 18, fill=MUTED),
            text(750, y + 105, (right_note if y == 300 else ""), 18, fill=MUTED),
        ]
    # Vertical within-arm paths.
    for x in (250, 750):
        for y1, y2 in ((428, 500), (628, 700)):
            body.append(f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2 - 4}" stroke="{MUTED}" stroke-width="3" marker-end="url(#arrow)"/>')

    body += [
        # Interference is shown as cross-arm exposure, not as ordinary flow.
        '<path d="M430 375 C475 350 525 350 570 375" fill="none" stroke="%s" stroke-width="3" stroke-dasharray="9 8" marker-end="url(#red-arrow)"/>' % RED,
        '<path d="M570 410 C525 435 475 435 430 410" fill="none" stroke="%s" stroke-width="3" stroke-dasharray="9 8" marker-end="url(#red-arrow)"/>' % RED,
        text(500, 329, "SPILLOVERS", 16, weight=700, fill=RED),
        text(500, 350, "between arms", 16, fill=RED),
        # Diagnostic labels in a lower band.
        rect(45, 865, 910, 263, fill="#ffffff", stroke=LIGHT, sw=2, radius=22),
        text(500, 907, "WHAT EACH BREAK IN THE FLOW MEANS", 23, weight=700),
        rect(75, 940, 260, 145, fill=PALE_GREEN, stroke=GREEN, sw=2),
        text(205, 976, "NONCOMPLIANCE", 20, weight=700, fill=GREEN),
        lines(205, 1010, ["assignment ≠ receipt", "ITT still compares", "groups as assigned"], 18, leading=24, fill=MUTED),
        rect(370, 940, 260, 145, fill=PALE_BLUE, stroke=BLUE, sw=2),
        text(500, 976, "MISSINGNESS", 20, weight=700, fill=BLUE),
        lines(500, 1010, ["observation can depend", "on assignment or outcome", "report reasons by arm"], 18, leading=24, fill=MUTED),
        rect(665, 940, 260, 145, fill=PALE_RED, stroke=RED, sw=2),
        text(795, 976, "INTERFERENCE", 20, weight=700, fill=RED),
        lines(795, 1010, ["one unit's treatment", "changes another unit's", "outcome or exposure"], 18, leading=24, fill=MUTED),
        rect(45, 1148, 910, 102, fill=PALE_RED, stroke=RED, sw=2, radius=18),
        text(500, 1183, "NO UNIVERSALLY SAFE ATTRITION PERCENTAGE", 20, weight=700, fill=RED),
        lines(500, 1216, ["Risk depends on why outcomes are missing and how missingness relates", "to assignment and potential outcomes—not on one fixed percentage."], 18, leading=25, fill=NAVY),
    ]
    return svg_document(
        "Participant flow from assignment through analysis",
        "Two randomized arms proceed separately through treatment receipt, outcome observation, and analysis. Cross-arm dashed arrows at receipt show spillovers or interference. A lower diagnostic band distinguishes noncompliance, missingness, and interference, and states that there is no universal safe attrition threshold.",
        "\n".join(body), 1000, 1280,
    )


def normal_cdf(x: float) -> float:
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def selected_literature_simulation() -> tuple[str, list[dict[str, float | int | bool]], dict[str, float | int | str]]:
    seed = 20260830
    studies = 2000
    true_effect = 0.20
    outcome_variance = 1.0
    n_per_arm = 50
    alpha = 0.05
    z_critical = 1.959963984540054
    standard_error = math.sqrt(2.0 * outcome_variance / n_per_arm)
    threshold = z_critical * standard_error

    rng = random.Random(seed)
    rows: list[dict[str, float | int | bool]] = []
    for study in range(1, studies + 1):
        estimate = rng.gauss(true_effect, standard_error)
        z_value = estimate / standard_error
        p_value = math.erfc(abs(z_value) / math.sqrt(2.0))
        visible = p_value < alpha
        rows.append({
            "study": study,
            "estimate": estimate,
            "standard_error": standard_error,
            "z_value": z_value,
            "p_value_two_sided": p_value,
            "visible_under_rule": visible,
        })

    selected = [row for row in rows if bool(row["visible_under_rule"])]
    mean_all = sum(float(row["estimate"]) for row in rows) / len(rows)
    mean_selected = sum(float(row["estimate"]) for row in selected) / len(selected)
    type_s = sum(float(row["estimate"]) < 0 for row in selected)
    theoretical_power = (1 - normal_cdf(z_critical - true_effect / standard_error)) + normal_cdf(-z_critical - true_effect / standard_error)

    # Same x scale for the full and selected distributions.
    x_min, x_max = -0.8, 1.2
    bin_width = 0.08
    bin_count = int(round((x_max - x_min) / bin_width))

    def histogram(values: list[float]) -> list[int]:
        counts = [0] * bin_count
        for value in values:
            if value < x_min or value > x_max:
                continue
            index = min(int((value - x_min) / bin_width), bin_count - 1)
            counts[index] += 1
        return counts

    all_counts = histogram([float(row["estimate"]) for row in rows])
    selected_counts = histogram([float(row["estimate"]) for row in selected])
    all_pct = [100 * count / len(rows) for count in all_counts]
    selected_pct = [100 * count / len(selected) for count in selected_counts]
    ymax = max(max(all_pct), max(selected_pct)) * 1.18

    body: list[str] = [
        text(450, 54, "A significance gate changes the literature we see", 35, weight=700),
        text(450, 94, "Noisy estimates enter; a systematically different subset emerges.", 27, fill=MUTED),
        rect(35, 126, 830, 112, fill="#ffffff", stroke=LIGHT, sw=2),
        text(450, 165, f"TRUE EFFECT = {true_effect:.2f} SD   ·   VARIANCE = {outcome_variance:.1f}   ·   n = {n_per_arm} PER ARM", 25, weight=700),
        text(450, 205, f"α = {alpha:.2f}   ·   {studies:,} studies   ·   known-variance two-sided z test   ·   seed {seed}", 23, fill=MUTED),
        rect(45, 275, 810, 390, fill="#ffffff", stroke=BLUE, sw=3, radius=22),
        text(450, 319, "1  ALL SIMULATED ESTIMATES", 28, weight=700, fill=BLUE),
        text(450, 355, f"mean = {mean_all:.3f} across {studies:,} studies", 25, fill=MUTED),
        '<line x1="450" y1="665" x2="450" y2="707" stroke="%s" stroke-width="4" marker-end="url(#red-arrow)"/>' % RED,
        rect(200, 715, 500, 184, fill=PALE_RED, stroke=RED, sw=3, radius=22),
        text(450, 758, "2  SIGNIFICANCE / REPORTING GATE", 26, weight=700, fill=RED),
        text(450, 805, "visible only if two-sided p < .05", 27, weight=700),
        text(450, 847, f"estimate < −{threshold:.3f}  or  estimate > {threshold:.3f}", 24, fill=MUTED),
        '<line x1="450" y1="899" x2="450" y2="941" stroke="%s" stroke-width="4" marker-end="url(#red-arrow)"/>' % RED,
        rect(45, 950, 810, 390, fill="#ffffff", stroke=ORANGE, sw=3, radius=22),
        text(450, 994, "3  SELECTED VISIBLE ESTIMATES", 28, weight=700, fill=ORANGE),
        text(450, 1030, f"mean = {mean_selected:.3f} across {len(selected):,} studies", 25, fill=MUTED),
    ]

    def chart(x0: float, chart_y: float, counts_pct: list[float], bar_color: str, selected_chart: bool) -> None:
        chart_h = 180
        chart_w = 700
        body.append(f'<line x1="{x0}" y1="{chart_y + chart_h}" x2="{x0 + chart_w}" y2="{chart_y + chart_h}" stroke="{MUTED}" stroke-width="2"/>')
        for tick in (-0.8, -0.4, 0.0, 0.4, 0.8, 1.2):
            x = x0 + (tick - x_min) / (x_max - x_min) * chart_w
            body.append(f'<line x1="{x:.1f}" y1="{chart_y + chart_h}" x2="{x:.1f}" y2="{chart_y + chart_h + 8}" stroke="{MUTED}" stroke-width="2"/>')
            body.append(text(x, chart_y + chart_h + 31, f"{tick:.1f}", 21, fill=MUTED))
        body.append(text(x0 + chart_w / 2, chart_y + chart_h + 58, "estimated effect (SD units)", 23, weight=700))
        for index, pct in enumerate(counts_pct):
            left = x0 + index / bin_count * chart_w
            width = chart_w / bin_count - 1
            height = pct / ymax * chart_h
            center = x_min + (index + 0.5) * bin_width
            fill = RED if selected_chart and center < 0 else bar_color
            body.append(f'<rect x="{left:.2f}" y="{chart_y + chart_h - height:.2f}" width="{width:.2f}" height="{height:.2f}" fill="{fill}" opacity="0.88"/>')
        true_x = x0 + (true_effect - x_min) / (x_max - x_min) * chart_w
        body.append(f'<line x1="{true_x:.1f}" y1="{chart_y}" x2="{true_x:.1f}" y2="{chart_y + chart_h}" stroke="{GREEN}" stroke-width="3" stroke-dasharray="9 7"/>')
        body.append(text(true_x + 8, chart_y + 25, "true effect", 21, anchor="start", weight=700, fill=GREEN))
        if not selected_chart:
            for limit in (-threshold, threshold):
                limit_x = x0 + (limit - x_min) / (x_max - x_min) * chart_w
                body.append(f'<line x1="{limit_x:.1f}" y1="{chart_y}" x2="{limit_x:.1f}" y2="{chart_y + chart_h}" stroke="{RED}" stroke-width="2" stroke-dasharray="6 7"/>')

    chart(100, 390, all_pct, BLUE, False)
    chart(100, 1065, selected_pct, ORANGE, True)

    body += [
        rect(45, 1375, 810, 122, fill=PALE_ORANGE, stroke=ORANGE, sw=2, radius=20),
        text(450, 1413, f"{len(selected):,} of {studies:,} studies ({100 * len(selected) / studies:.1f}%) pass the reporting gate.", 23, weight=700),
        text(450, 1450, f"{type_s} selected estimates have the wrong sign; selected mean = {mean_selected / true_effect:.1f}× the truth.", 22, weight=700),
        text(450, 1482, f"Theoretical power under the declared model = {100 * theoretical_power:.1f}%.", 21, fill=NAVY),
        lines(450, 1535, ["Teaching simulation—not an estimate of any field's publication process.",
                          "Real selection can also depend on novelty, direction, outcomes,", "analyses, and editorial decisions."], 20, leading=27, fill=MUTED),
    ]

    metadata: dict[str, float | int | str] = {
        "description": "Independent two-arm normal-outcome studies represented by their difference-in-means sampling distribution; known-variance two-sided z test; visible only if p < alpha.",
        "seed": seed,
        "studies": studies,
        "true_effect_sd": true_effect,
        "outcome_variance": outcome_variance,
        "n_per_arm": n_per_arm,
        "alpha_two_sided": alpha,
        "known_standard_error": standard_error,
        "critical_z": z_critical,
        "selection_rule": "visible_under_rule = two-sided p-value < alpha",
        "selected_studies": len(selected),
        "mean_all_estimates": mean_all,
        "mean_selected_estimates": mean_selected,
        "selected_wrong_sign": type_s,
        "theoretical_power": theoretical_power,
    }
    return (
        svg_document(
            "Noisy estimates passing through a significance-only reporting gate",
            f"A deterministic simulation of {studies} independent two-arm studies with true standardized effect {true_effect}, outcome variance {outcome_variance}, {n_per_arm} observations per arm, alpha {alpha}, and seed {seed}. All estimates are noisy around the true effect. A reporting rule shows only two-sided p-values below alpha. The selected subset is smaller and has a larger mean estimate. This is a teaching simulation, not an estimate of real publication bias.",
            "\n".join(body), 900, 1610,
        ),
        rows,
        metadata,
    )


def write_outputs() -> None:
    FIGURES.mkdir(parents=True, exist_ok=True)
    SOURCE.mkdir(parents=True, exist_ok=True)

    (FIGURES / "random-sampling-vs-assignment.svg").write_text(
        sampling_vs_assignment(), encoding="utf-8"
    )
    (FIGURES / "participant-flow-threats.svg").write_text(
        participant_flow(), encoding="utf-8"
    )
    simulation_svg, rows, metadata = selected_literature_simulation()
    (FIGURES / "selected-literature-simulation.svg").write_text(
        simulation_svg, encoding="utf-8"
    )

    with (SOURCE / "selected-literature-simulation.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    (SOURCE / "selected-literature-simulation.json").write_text(
        json.dumps(metadata, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    for path in (
        FIGURES / "random-sampling-vs-assignment.svg",
        FIGURES / "participant-flow-threats.svg",
        FIGURES / "selected-literature-simulation.svg",
        SOURCE / "selected-literature-simulation.csv",
        SOURCE / "selected-literature-simulation.json",
    ):
        print(path.relative_to(ROOT))


if __name__ == "__main__":
    write_outputs()
