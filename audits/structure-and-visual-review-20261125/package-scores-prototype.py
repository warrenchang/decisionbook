"""Generate the editorial prototype from the hypothetical packages in Chapter 37."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


BUYER_OUTSIDE = 40
SUPPLIER_OUTSIDE = 45
# Coordinates follow the existing figure: supplier on x, buyer on y.
PACKAGES = {
    "Short, flexible": (0, 100),
    "Short, fixed": (30, 30),
    "Long, flexible": (70, 70),
    "Long, fixed": (100, 0),
}


def dominates(candidate, reference):
    return (
        all(c >= r for c, r in zip(candidate, reference))
        and any(c > r for c, r in zip(candidate, reference))
    )


def main():
    acceptable = [
        point for point in PACKAGES.values()
        if point[0] >= SUPPLIER_OUTSIDE and point[1] >= BUYER_OUTSIDE
    ]
    dominated = [
        point for point in PACKAGES.values()
        if any(dominates(other, point) for other in PACKAGES.values())
    ]
    assert acceptable == [(70, 70)]
    assert dominated == [(30, 30)]

    navy = "#183047"
    teal = "#006d68"
    muted = "#53697a"
    plt.rcParams.update({
        "font.family": "DejaVu Sans",
        "text.color": navy,
        "axes.labelcolor": navy,
        "xtick.color": muted,
        "ytick.color": muted,
        "savefig.facecolor": "white",
    })
    figure, axis = plt.subplots(figsize=(5.3, 5.15))
    figure.subplots_adjust(left=0.16, right=0.973, bottom=0.166, top=0.963)
    axis.set(xlim=(-4, 107), ylim=(-4, 106), xlabel="Supplier’s score", ylabel="Buyer’s score")
    ticks = [0, 25, 50, 75, 100]
    axis.set_xticks(ticks)
    axis.set_yticks(ticks)
    axis.tick_params(labelsize=11.5, length=0, pad=6)
    axis.xaxis.label.set_size(16)
    axis.yaxis.label.set_size(16)
    axis.xaxis.labelpad = 13
    axis.yaxis.labelpad = 10
    axis.spines[["top", "right"]].set_visible(False)
    axis.spines[["left", "bottom"]].set_color("#9eafb8")
    axis.set_axisbelow(True)
    axis.grid(color="#e5edf0", linewidth=0.8, zorder=0)

    axis.add_patch(Rectangle(
        (SUPPLIER_OUTSIDE, BUYER_OUTSIDE), 100 - SUPPLIER_OUTSIDE,
        100 - BUYER_OUTSIDE, color="#e6f3ef", zorder=-1, linewidth=0
    ))
    axis.axhline(BUYER_OUTSIDE, linestyle=(0, (4, 3)), color=muted, linewidth=1.15)
    axis.axvline(SUPPLIER_OUTSIDE, linestyle=(0, (4, 3)), color=muted, linewidth=1.15)
    label_style = {"fontsize": 12.6, "linespacing": 1.12}
    axis.text(96, 94, "Both can accept", va="top", ha="right",
              color=teal, fontweight="bold", **label_style)
    axis.text(2, 43, "Buyer minimum 40", va="bottom", color=muted, fontsize=11.7)
    axis.text(48, 24, "Supplier\nminimum 45", va="top", color=muted, fontsize=11.7)

    offsets = [(9, -9, "left", "top"), (-6, -9, "right", "top"),
               (6, 8, "left", "bottom"), (-6, 8, "right", "bottom")]
    for (name, point), (dx, dy, ha, va) in zip(PACKAGES.items(), offsets):
        selected = point in acceptable
        axis.scatter(*point, s=80, color=teal if selected else navy,
                     edgecolor="white", linewidth=1.15, zorder=4)
        axis.annotate(name, point, xytext=(dx, dy), textcoords="offset points",
                      ha=ha, va=va, color=teal if selected else navy,
                      fontweight="bold" if selected else "normal", zorder=5, **label_style)

    axis.annotate("", xy=(70, 70), xytext=(30, 30), zorder=3,
                  arrowprops={"arrowstyle": "-|>", "color": teal, "lw": 1.6,
                              "shrinkA": 7, "shrinkB": 6, "mutation_scale": 15})
    axis.text(53, 52, "+40 each", ha="left", va="top", color=teal, fontsize=12.6)

    output = Path(__file__).with_name("package-scores-prototype.png")
    figure.savefig(output, dpi=220)
    plt.close(figure)


if __name__ == "__main__":
    main()
