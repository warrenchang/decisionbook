#!/usr/bin/env python3
"""Build original, rights-safe figures for the research-methods appendices.

The conceptual figures explain research design and selection. The statistical figure is a deterministic
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


def vertical_steps(title: str, steps: list[tuple[str, str]], description: str) -> str:
    body = [text(350, 52, title, 34, weight=700)]
    for i, (label, question) in enumerate(steps):
        y = 90 + 135 * i
        body.extend([f'<g id="stage-{i + 1}">', rect(60, y, 580, 100, fill=PALE_BLUE if i < 4 else PALE_GREEN, stroke=BLUE if i < 4 else GREEN, sw=2), text(350, y + 39, f'{i + 1}. {label}', 30, weight=700), text(350, y + 77, question, 28), '</g>'])
        if i < len(steps) - 1:
            body.append(f'<path d="M350 {y+100} V{y+135}" fill="none" stroke="{MUTED}" stroke-width="3" marker-end="url(#arrow)"/>')
    return svg_document(title, description, '\n'.join(body), 700, 780)


def claim_to_design() -> str:
    return vertical_steps('Build a claim the study can support', [
        ('Question', 'What do we want to learn?'),
        ('Measure', 'What will count as evidence?'),
        ('Compare', 'What is the relevant alternative?'),
        ('Estimate', 'How large and how uncertain?'),
        ('Claim', 'What does this design justify?'),
    ], 'Five connected questions guide an experimental study from its question through measurement, comparison, and estimation to a defensible claim. This is a planning sequence, not a guarantee of validity.')


def selected_evidence() -> str:
    return vertical_steps('How a study becomes visible', [
        ('Question', 'Which possibilities are investigated?'),
        ('Design', 'Who and what get measured?'),
        ('Data', 'Which observations are recorded?'),
        ('Analysis', 'Which results are reported?'),
        ('Literature', 'Which findings reach readers?'),
    ], 'Five stages show how choices about questions, design, data, analysis, and publication determine what readers see. Selection can occur at every stage.')


def sampling_vs_assignment() -> str:
    body = [text(380, 52, 'Two different uses of randomness', 34, weight=700)]
    for x, center, color, fill, heading, stages in [
        (25, 195, BLUE, PALE_BLUE, 'SAMPLING', [('Population', 'Who is eligible?'), ('Sample', 'Who is selected?'), ('Population claim', 'What can we infer?')]),
        (395, 565, GREEN, PALE_GREEN, 'ASSIGNMENT', [('Study sample', 'Who takes part?'), ('Groups A and B', 'Who gets what?'), ('Causal contrast', 'What differs?')])
    ]:
        body.append(text(center, 109, heading, 30, weight=700, fill=color))
        for i, (label, question) in enumerate(stages):
            y = 140 + i * 150
            body.extend([f'<g id="{heading.lower()}-{i}">', rect(x, y, 340, 110, fill=fill, stroke=color), text(center, y+42, label, 29, weight=700), text(center, y+83, question, 28), '</g>'])
            if i < 2:
                body.append(f'<path d="M{center} {y+110} V{y+150}" stroke="{MUTED}" stroke-width="3" marker-end="url(#arrow)"/>')
    body.extend([text(380, 612, 'Inference still depends on the design', 28, weight=700), text(380, 648, 'and on how the study is carried out.', 28)])
    return svg_document('Sampling and assignment answer different questions', 'Random sampling selects people from a population and supports inference to that population under the sampling design. Random assignment allocates study participants to conditions and supports an internal causal comparison under the design and implementation assumptions.', '\n'.join(body), 760, 690)


def participant_flow() -> str:
    body = [text(380, 49, 'Follow people from assignment', 34, weight=700), text(380, 88, 'to the final comparison', 34, weight=700), rect(180, 126, 400, 82, fill=PALE_PURPLE, stroke=PURPLE), text(380, 178, 'Random assignment', 30, weight=700)]
    body += [f'<path d="M380 208 V244 H185 V284 M380 244 H575 V284" fill="none" stroke="{MUTED}" stroke-width="3" marker-end="url(#arrow)"/>']
    # Give the left branch its own arrowhead without doubling the shared stem.
    body[-1] = f'<path d="M380 208 V244 H185 V284" fill="none" stroke="{MUTED}" stroke-width="3" marker-end="url(#arrow)"/>'
    body.append(f'<path d="M380 244 H575 V284" fill="none" stroke="{MUTED}" stroke-width="3" marker-end="url(#arrow)"/>')
    for x, c, label in [(25,185,'Assigned A'),(415,575,'Assigned B')]:
        for i, (head, notes) in enumerate([(label,['Did they receive','the treatment?']), ('Outcomes',['Who was observed?']), ('Analysis',['Compare groups','as assigned.'])]):
            y = 284 + 173*i
            body.extend([f'<g id="arm-{label[-1]}-{i}">', rect(x,y,320,133,fill=PALE_GREEN if i==0 else PALE_BLUE if i==1 else PALE_ORANGE,stroke=GREEN if i==0 else BLUE if i==1 else ORANGE), text(c,y+39,head,30,weight=700), lines(c,y+79,notes,28,leading=34), '</g>'])
            if i<2:
                body.append(f'<path d="M{c} {y+133} V{y+173}" fill="none" stroke="{MUTED}" stroke-width="3" marker-end="url(#arrow)"/>')
    body.extend([text(380,825,'Track nonreceipt and missing outcomes.',28,weight=700), text(380,865,'Check whether one group affects the other.',28)])
    return svg_document('Participant flow from assignment through analysis', 'Two assigned groups are followed through receipt, outcome observation, and analysis. The comparison keeps original assignment labels; researchers must account for missing outcomes and possible effects between groups.', '\n'.join(body), 760, 910)


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

    # Plot the same simulated estimates, with explicit and shared scales.
    import io
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.ticker import PercentFormatter
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 14,
                         "svg.fonttype": "none", "svg.hashsalt": "selected-literature-20260910"})
    fig, axes = plt.subplots(2, 1, figsize=(9.6, 9.8), sharex=True, sharey=True)
    fig.subplots_adjust(left=.13, right=.97, top=.85, bottom=.13, hspace=.68)
    fig.suptitle("Selection makes noisy effects look larger", fontsize=20, weight="bold", y=.98)
    fig.text(.5,.918, "Teaching simulation: true effect = 0.20 SD", ha="center", fontsize=16)
    bins = [-.8 + .08*i for i in range(26)]
    for ax, data, color, heading in zip(axes, [rows, selected], [BLUE, ORANGE],
            [f"All {len(rows):,} studies · mean {mean_all:.3f}",
             f"{len(selected):,} visible studies · mean {mean_selected:.3f}"]):
        values = [float(r["estimate"]) for r in data]
        ax.hist(values, bins=bins, weights=[100/len(values)]*len(values), color=color, edgecolor="white")
        ax.axvline(true_effect, color=GREEN, linestyle="--", linewidth=2.5)
        ax.set_title(heading, loc="left", fontsize=16, weight="bold", pad=16)
        ax.set_xlim(-.8,1.2); ax.set_ylim(0,50)
        ax.set_xticks([-.8,-.4,0,.4,.8,1.2]); ax.set_yticks([0,25,50])
        ax.yaxis.set_major_formatter(PercentFormatter(100, decimals=0))
        ax.set_ylabel("Share of studies")
        ax.grid(axis="y", alpha=.18); ax.set_axisbelow(True)
        ax.spines[["right","top"]].set_visible(False)
        ax.tick_params(axis="both", labelsize=14)
        ax.text(.02,.90,"Dashed line: true effect",transform=ax.transAxes,fontsize=14,color=GREEN)
    axes[0].tick_params(labelbottom=True)
    axes[1].set_xlabel("Estimated effect (standard deviations)", labelpad=10)
    fig.text(.55,.493,"Reporting gate: retain only two-sided p < .05",ha="center",fontsize=16,color=RED,
             bbox={"boxstyle":"round,pad=.65", "facecolor":PALE_RED,"edgecolor":RED})
    fig.text(.5,.04,"The selected mean is 2.5 times the true effect.",ha="center",fontsize=16,weight="bold")
    buffer=io.StringIO(); fig.savefig(buffer,format="svg",metadata={"Date":None}); plt.close(fig)
    simulation_svg=buffer.getvalue().replace("DejaVu Sans", "Arial")
    simulation_svg=simulation_svg.replace('<svg ', '<svg role="img" aria-labelledby="simulation-title simulation-desc" ',1)
    start=simulation_svg.index('>',simulation_svg.index('<svg '))+1
    simulation_svg=simulation_svg[:start]+f'<title id="simulation-title">Selective reporting inflates visible effect estimates</title><desc id="simulation-desc">Two histograms show {len(rows)} simulated estimates and the {len(selected)} that pass a two-sided p less than .05 gate. Both axes share the same scales. The true effect is .20 standard deviations; the selected mean is .490. Bar heights are percentages within each displayed set.</desc>'+simulation_svg[start:]

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
    return "\n".join(line.rstrip() for line in simulation_svg.splitlines())+"\n", rows, metadata



def write_outputs() -> None:
    FIGURES.mkdir(parents=True, exist_ok=True)
    SOURCE.mkdir(parents=True, exist_ok=True)

    (FIGURES / "random-sampling-vs-assignment.svg").write_text(
        sampling_vs_assignment(), encoding="utf-8"
    )
    (FIGURES / "participant-flow-threats.svg").write_text(
        participant_flow(), encoding="utf-8"
    )
    (FIGURES / "claim-to-design-pipeline.svg").write_text(claim_to_design(), encoding="utf-8")
    (FIGURES / "selected-evidence-pipeline.svg").write_text(selected_evidence(), encoding="utf-8")
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
