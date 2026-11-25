#!/usr/bin/env python3
"""Build the replacement charts for the structural revision of Decision in the Making.

Reported study values are reproduced from the chapter's existing source records.
Other numbers are teaching examples or functions specified in the chapters.
"""

from pathlib import Path
from xml.sax.saxutils import escape

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.ticker import PercentFormatter
import numpy as np


FIGURES = Path(__file__).resolve().parents[1] / "figures"
NAVY = "#183047"
TEAL = "#006d68"
BLUE = "#286184"
ORANGE = "#aa4d23"
MUTED = "#53697a"
LINE = "#dbe4e9"
PALE = "#e6f3ef"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 12,
    "text.color": NAVY,
    "axes.labelcolor": NAVY,
    "axes.titlecolor": NAVY,
    "xtick.color": MUTED,
    "ytick.color": MUTED,
    "svg.fonttype": "none",
    "svg.hashsalt": "decision-in-the-making-revision",
})


def save(figure, name, title, description):
    path = FIGURES / f"{name}.svg"
    figure.savefig(path, metadata={"Title": title, "Date": None})
    svg = path.read_text()
    end = svg.index("</title>") + len("</title>")
    path.write_text(svg[:end] + f"\n <desc>{escape(description)}</desc>" + svg[end:])
    plt.close(figure)


def style_axes(axis, direction="y"):
    axis.set_axisbelow(True)
    axis.spines[["top", "right"]].set_visible(False)
    axis.spines[["left", "bottom"]].set_color("#9eafb8")
    axis.grid(axis=direction, color=LINE, linewidth=0.7)
    axis.tick_params(length=0, pad=6)


def hiring_screen():
    """Ch. 14's two natural-frequency calculations on one common count scale."""
    pools = [(2000, "Broad pool"), (5000, "Preselected pool")]
    true_positive = [4 * eligible // 5 for eligible, _ in pools]
    false_positive = [3 * (10000 - eligible) // 10 for eligible, _ in pools]
    assert list(zip(true_positive, false_positive)) == [(1600, 2400), (4000, 1500)]
    fig, ax = plt.subplots(figsize=(5.4, 3.25))
    fig.subplots_adjust(left=0.14, right=0.94, top=0.94, bottom=0.20)
    style_axes(ax, "x")
    ax.spines["left"].set_visible(False)
    ax.set(xlim=(0, 6000), ylim=(-0.48, 1.8), xlabel="Applicants who passed the screen")
    ax.set_xticks(range(0, 6001, 1500), [f"{n:,}" for n in range(0, 6001, 1500)])
    ax.set_yticks([])
    for index, (true, false, (_, label)) in enumerate(zip(true_positive, false_positive, pools)):
        y = 1.12 - index
        ax.text(0, y + 0.32, label, weight="bold")
        ax.barh(y, true, color=TEAL, height=0.47)
        ax.barh(y, false, left=true, color=BLUE, height=0.47)
        ax.text(true / 2, y, f"{true:,}\ntrue", color="white", ha="center", va="center")
        ax.text(true + false / 2, y, f"{false:,}\nfalse", color="white", ha="center", va="center")
    save(fig, "hiring-screen-positive-pools", "How applicants pass the same screen",
         "The broad pool has 1,600 true and 2,400 false positives. The preselected pool has 4,000 true and 1,500 false positives.")


def expected_utility():
    """Ch. 16's square-root utility example, scaled in illustrative units."""
    mean_wealth = (0 + 100) / 2
    mean_utility = (0 + 10) / 2
    equivalent = mean_utility**2
    assert (mean_wealth, mean_utility, equivalent) == (50, 5, 25)
    wealth = np.linspace(0, 100, 501)
    fig, ax = plt.subplots(figsize=(5.4, 4.1))
    fig.subplots_adjust(left=0.16, right=0.95, bottom=0.18, top=0.93)
    style_axes(ax)
    ax.set(xlim=(0, 103), ylim=(0, 10.7), xlabel="Illustrative final wealth", ylabel="Utility")
    ax.set_xticks([0, 25, 50, 75, 100])
    ax.set_yticks(np.arange(0, 11, 2))
    ax.plot(wealth, np.sqrt(wealth), color=BLUE, lw=2.5)
    ax.plot([0, 100], [0, 10], color=MUTED, lw=1.2, ls="--")
    ax.hlines(5, 25, 50, color=TEAL, ls=":")
    ax.vlines([25, 50], 0, 5, color=TEAL, lw=1.05, ls=":")
    ax.scatter([25, 50], [5, 5], color=TEAL, edgecolors="white", zorder=4, s=56)
    ax.annotate("Certainty\nequivalent 25", (25, 5), xytext=(5, 7), fontsize=12)
    ax.annotate("Average utility 5", (50, 5), xytext=(52.5, 4.2), fontsize=12)
    ax.annotate("Square-root utility", (85, np.sqrt(85)), xytext=(36, 9.84), color=BLUE, fontsize=12)
    ax.hlines(1, 25, 50, color=ORANGE)
    ax.vlines([25, 50], 0.81, 1.19, color=ORANGE)
    ax.text(37.5, 1.32, "Risk premium 25", ha="center", color=ORANGE, fontsize=12)
    save(fig, "expected-utility-wealth", "Expected utility, certainty equivalent and risk premium",
         "Expected utility is 5 on the chord at average wealth 50. The utility curve reaches 5 at sure wealth 25. The difference is 25.")


def prospect_curves():
    fig, (left, right) = plt.subplots(2, 1, figsize=(5.3, 6.5))
    fig.subplots_adjust(left=0.18, right=0.94, bottom=0.09, top=0.92, hspace=0.66)
    gain = np.linspace(0, 1, 301)
    alpha = 0.88
    loss_weight = 2.25
    probability = np.linspace(0, 1, 301)
    shape = 0.61
    decision_weight = probability**shape / (probability**shape + (1-probability)**shape)**(1/shape)
    assert np.isclose(decision_weight[0], 0) and np.isclose(decision_weight[-1], 1)
    style_axes(left)
    left.set_title("Value around the reference point", loc="left", weight="bold", pad=12)
    left.axhline(0, color=MUTED, lw=1)
    left.axvline(0, color=MUTED, lw=1)
    left.plot(gain, gain**alpha, color=TEAL, lw=2.4)
    left.plot(-gain, -loss_weight * gain**alpha, color=ORANGE, lw=2.4)
    left.set(xlim=(-1.08, 1.08), ylim=(-2.45, 1.35), ylabel="Illustrative value")
    left.set_xticks([-1, 0, 1], ["Loss", "Reference", "Gain"])
    left.set_yticks([-2, -1, 0, 1])
    left.text(-0.93, 0.37, "Loss side", color=ORANGE)
    left.text(0.36, -0.42, "Gain side", color=TEAL)
    style_axes(right)
    right.set_title("Probability weighting for gains", loc="left", weight="bold", pad=12)
    right.plot(probability, probability, color=MUTED, ls="--", lw=1.2)
    right.plot(probability, decision_weight, color=TEAL, lw=2.4)
    right.set(xlim=(0, 1.02), ylim=(0, 1.02), xlabel="Objective probability", ylabel="Decision weight")
    ticks = [0, 0.25, 0.5, 0.75, 1]
    right.set_xticks(ticks)
    right.set_yticks(ticks)
    right.text(0.63, 0.87, "Equal weight", color=MUTED, ha="right")
    save(fig, "prospect-value-and-weight", "Illustrative prospect value and weighting",
         "The value function changes shape and slope at the reference point. The gain-weighting curve departs from the diagonal representing objective probability.")


def return_horizons():
    fig, ax = plt.subplots(figsize=(5.3, 3.7))
    fig.subplots_adjust(left=0.18, right=0.96, top=0.95, bottom=0.24)
    style_axes(ax)
    ax.bar([0, 1], [40, 90], width=0.50, color=[BLUE, TEAL])
    ax.set_xticks([0, 1], ["One-year\nreturn distribution", "30-year\nreturn distribution"])
    ax.set(ylim=(0, 103), ylabel="Median hypothetical stock allocation")
    ax.set_yticks([0, 25, 50, 75, 100])
    ax.yaxis.set_major_formatter(PercentFormatter(100, decimals=0))
    ax.text(0, 44, "40%", ha="center", weight="bold")
    ax.text(1, 94, "90%", ha="center", weight="bold")
    save(fig, "mental-accounting-return-horizon", "Return display and hypothetical allocation",
         "Benartzi and Thaler (1999), Study 3, report medians of 40% and 90% for the two displays, with 25 participants per group.")


def dated_choices():
    models = {
        "Exponential": lambda t: 0.95**t,
        "Hyperbolic": lambda t: 1 / (1 + 0.15*t),
        "Quasi-hyperbolic": lambda t: 1 if t == 0 else 0.70 * 0.95**t,
    }
    payments = [(12, 100), (13, 120)]
    rankings = {}
    for name, discount in models.items():
        rankings[name] = [
            max(payments, key=lambda payment: discount(payment[0] - now) * payment[1])[1]
            for now in (0, 12)
        ]
    assert list(rankings.values()) == [[120, 120], [120, 120], [120, 100]]
    fig, ax = plt.subplots(figsize=(5.3, 3.98))
    fig.subplots_adjust(left=0.055, right=0.97, bottom=0.055, top=0.96)
    ax.set(xlim=(0, 1), ylim=(0, 1))
    ax.axis("off")
    ax.text(0.0, .94, "Fixed payment dates", weight="bold", fontsize=14)
    ax.text(0.02, .81, "Month 12     €100", fontsize=13)
    ax.text(0.53, .81, "Month 13     €120", fontsize=13)
    ax.hlines(.72, 0, 1, color=LINE)
    ax.text(.57, .61, "Viewed\ntoday", va="center", ha="center", weight="bold")
    ax.text(.86, .61, "Viewed at\nmonth 12", va="center", ha="center", weight="bold")
    for i, (name, best) in enumerate(rankings.items()):
        y = .45 - i * .155
        if i == 2:
            ax.add_patch(Rectangle((0, y-.075), 1, .15, facecolor=PALE, edgecolor="none"))
        ax.text(.015, y, name, va="center", fontsize=13)
        ax.text(.57, y, f"€{best[0]}", va="center", ha="center", fontsize=14, color=TEAL)
        ax.text(.86, y, f"€{best[1]}", va="center", ha="center", fontsize=14,
                color=ORANGE if best[1] != best[0] else TEAL, weight="bold")
    save(fig, "same-payoff-two-evaluation-dates", "Model choices when the evaluation date changes",
         "Exponential and hyperbolic discounting choose 120 euros at both dates. The quasi-hyperbolic example switches from 120 to 100 euros.")


def habit_criterion():
    progress = np.linspace(0, 5.0, 501)
    fig, ax = plt.subplots(figsize=(5.3, 3.45))
    fig.subplots_adjust(left=0.16, right=0.95, bottom=0.18, top=0.92)
    style_axes(ax)
    ax.set(xlim=(0, 5), ylim=(0, 1.17), xlabel="Repeated opportunities", ylabel="Illustrative automaticity")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.plot(progress, 1-np.exp(-progress), color=BLUE, lw=2.5)
    ax.axhline(.95, color=MUTED, ls="--", lw=1.1)
    ax.scatter([-np.log(0.05)], [.95], color=TEAL, edgecolor="white", s=55, zorder=4)
    ax.text(.13, 1.01, "95% of the illustrative plateau", color=TEAL, fontsize=13)
    save(fig, "habit-plateau-criterion", "Model criterion for a learning plateau",
         "A schematic automaticity curve rises toward a plateau. A dashed line at 95% of the plateau marks the modeled criterion.")


def tone_decoding():
    """Kruger et al. (2005), Study 2. Approximate values from the existing Chapter 33 redraw."""
    values = [(78, 89, 56), (78, 91, 73)]
    fig, (email, voice) = plt.subplots(2, 1, figsize=(5.4, 5.25), sharex=True)
    fig.subplots_adjust(left=.41, right=.93, top=.91, bottom=.14, hspace=.48)
    measures = ["Sender forecast", "Receiver confidence", "Observed accuracy"]
    for ax, medium, observed in zip((email, voice), ("Email", "Voice"), values):
        style_axes(ax, "x")
        ax.set_title(medium, loc="left", weight="bold", pad=9)
        ax.set_yticks([2, 1, 0], measures)
        ax.set_xlim(0, 103)
        ax.barh([2, 1, 0], observed, height=.47, color=[BLUE, BLUE, TEAL])
        ax.axvline(50, color=MUTED, ls="--", lw=1)
        for y, value in zip([2, 1, 0], observed):
            ax.text(value + 2, y, f"{value}%", va="center", fontsize=12)
    voice.set_xticks([0, 25, 50, 75, 100])
    voice.set_xlabel("Percentage  ·  dashed line marks chance")
    save(fig, "tone-decoding-estimates", "Confidence and accuracy in decoding tone",
         "Approximate sender, receiver and observed percentages are 78, 89 and 56 for email, and 78, 91 and 73 for voice. The chance line is 50%.")


def bargaining_packages():
    """Ch. 37's hypothetical packages. Coordinates are (supplier, buyer)."""
    scores = {
        "Short, flexible": (0, 100),
        "Short, fixed": (30, 30),
        "Long, flexible": (70, 70),
        "Long, fixed": (100, 0),
    }
    minimum = (45, 40)
    assert [name for name,(s,b) in scores.items() if s >= minimum[0] and b >= minimum[1]] == ["Long, flexible"]
    fig, ax = plt.subplots(figsize=(5.3, 5.15))
    fig.subplots_adjust(left=.16, right=.974, bottom=.166, top=.963)
    style_axes(ax)
    ax.set(xlim=(-4,107), ylim=(-4,106), xlabel="Supplier’s score", ylabel="Buyer’s score")
    ticks = [0, 25, 50, 75, 100]
    ax.set_xticks(ticks)
    ax.set_yticks(ticks)
    ax.xaxis.label.set_size(16)
    ax.yaxis.label.set_size(16)
    ax.add_patch(Rectangle(minimum, 55, 60, color=PALE, linewidth=0, zorder=-1))
    ax.axvline(minimum[0], color=MUTED, ls="--", lw=1)
    ax.axhline(minimum[1], color=MUTED, ls="--", lw=1)
    ax.text(96,94,"Both can accept", ha="right", va="top", color=TEAL, weight="bold")
    ax.text(2,43,"Buyer minimum 40", va="bottom", color=MUTED)
    ax.text(48,24,"Supplier\nminimum 45", va="top", color=MUTED)
    offsets = [(9,-9,"left","top"),(-6,-9,"right","top"),(6,8,"left","bottom"),(-6,8,"right","bottom")]
    for (name, point),(dx,dy,align,vertical) in zip(scores.items(), offsets):
        color = TEAL if name == "Long, flexible" else NAVY
        ax.scatter(*point, s=76, color=color, edgecolor="white", zorder=4)
        ax.annotate(name, point, xytext=(dx,dy), textcoords="offset points", ha=align,
                    va=vertical, color=color, weight="bold" if color == TEAL else "normal")
    ax.annotate("", xy=(70,70), xytext=(30,30),
                arrowprops={"arrowstyle":"-|>", "color":TEAL, "lw":1.6, "shrinkA":7, "shrinkB":6})
    ax.text(53,52,"+40 each", va="top", color=TEAL)
    save(fig, "four-feasible-bargaining-packages", "Four feasible bargaining packages",
         "Only the long flexible package clears both thresholds. It improves both scores by 40 relative to the short fixed package.")


if __name__ == "__main__":
    for build in (hiring_screen, expected_utility, prospect_curves, return_horizons,
                  dated_choices, habit_criterion, tone_decoding, bargaining_packages):
        build()
