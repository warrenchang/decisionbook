#!/usr/bin/env python3
"""Build the two compact judgment diagrams, without touching other figures."""
from html import escape
from pathlib import Path
from reviewed_figure_cleanup import clean_svg

OUT = Path(__file__).resolve().parents[1] / "figures"


def start(height, title, description):
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="760" height="{height}" viewBox="0 0 760 {height}" role="img" aria-labelledby="title desc">',
        f'<title id="title">{escape(title)}</title><desc id="desc">{escape(description)}</desc>',
        '<defs><marker id="blue-arrow" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto" markerUnits="userSpaceOnUse"><path d="M0 0 L9 4 L0 8 Z" fill="#2f6f9f"/></marker><marker id="orange-arrow" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto" markerUnits="userSpaceOnUse"><path d="M0 0 L9 4 L0 8 Z" fill="#c56a2d"/></marker></defs>',
        f'<rect width="760" height="{height}" fill="white"/>',
    ]


def text(x, y, lines, size=28, weight=400, color="#17324d", leading=36):
    spans = ''.join(f'<tspan x="{x}" y="{y+i*leading}">{escape(line)}</tspan>' for i, line in enumerate(lines))
    return f'<text text-anchor="middle" font-family="Arial, sans-serif" font-size="{size}" font-weight="{weight}" fill="{color}">{spans}</text>'


def box(x, y, width, height, fill="#eaf3f8", stroke="#2f6f9f"):
    return f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="18" fill="{fill}" stroke="{stroke}" stroke-width="2.5"/>'


def arrow(d, color="blue"):
    stroke = "#2f6f9f" if color == "blue" else "#c56a2d"
    return f'<path d="{d}" fill="none" stroke="{stroke}" stroke-width="3" stroke-linejoin="round" stroke-linecap="round" marker-end="url(#{color}-arrow)"/>'


def processing():
    s = start(992, "System 1 and System 2", "Two families of processes are compared on the same dimensions: autonomy, common contributions, working-memory demands, typical speed and effort, and fallibility. An arrow carries a candidate answer from System 1 to System 2; a return arrow indicates possible checking or training. The families are not separate brain structures or a fixed sequence.")
    s += [text(380, 52, ["System 1 and System 2"], 36, 700), text(380, 96, ["Families of processes, not separate brain structures"], 28)]
    for x, name, fill, stroke, rows in [
        (28, "System 1", "#eaf3f8", "#2f6f9f", [
            ["Relatively", "autonomous"], ["Associations and", "learned responses"],
            ["Little demand on", "working memory"], ["Often fast and", "effortless"],
            ["Can be skilled", "or misleading"]]),
        (432, "System 2", "#f7f1e8", "#c56a2d", [
            ["Depends on", "cognitive control"], ["Holds goals,", "compares, simulates"],
            ["Requires", "working memory"], ["Often slower", "and effortful"],
            ["Can correct errors", "or rationalize them"]]),
    ]:
        s += [box(x, 137, 300, 659, fill, stroke), text(x+150, 187, [name], 32, 700)]
        for y, lines in zip([252, 362, 476, 590, 705], rows):
            s.append(text(x+150, y, lines))
    s += [arrow("M328 320 H432"), text(380, 261, ["initial", "answer"], 28, leading=34),
          arrow("M432 650 H328", "orange"), text(380, 687, ["check", "or train"], 28),
          box(38, 832, 684, 128, "#f5f8fa", "#9eb1bf"),
          text(380, 881, ["Practice can change how a task is performed.", "Neither family guarantees accuracy."], 28)]
    return clean_svg('fast-slow.svg', '\n'.join(s+['</svg>'])+'\n')


def representativeness():
    s = start(1120, "Representativeness and probability", "The representativeness heuristic uses category fit to form a quick impression. A separate probability update combines prior probability with evidence that distinguishes alternatives. Similarity can suggest a hypothesis but does not replace those comparisons.")
    s += [text(380, 54, ["Representativeness", "and probability"], 36, 700, leading=44),
          box(70, 155, 620, 135, "#f7f1e8", "#c56a2d"),
          text(380, 200, ["Representativeness"], 32, 700),
          text(380, 249, ["How closely does the case fit a category?"], 28),
          arrow("M380 290 V350", "orange"),
          box(120, 350, 520, 111, "#f7f1e8", "#c56a2d"),
          text(380, 393, ["Quick impression"], 32, 700),
          text(380, 434, ["“It fits, so it seems likely.”"], 28),
          text(380, 551, ["Probability update"], 32, 700),
          box(30, 600, 320, 174), box(410, 600, 320, 174),
          text(190, 644, ["Prior probability"], 30, 700),
          text(190, 694, ["How common is", "the category?"], 28),
          text(570, 644, ["Diagnostic evidence"], 30, 700),
          text(570, 694, ["Does this evidence", "separate alternatives?"], 28),
          '<path d="M190 774 V815 H570 V774" fill="none" stroke="#2f6f9f" stroke-width="3" stroke-linejoin="round"/>',
          arrow("M380 815 V852"),
          box(90, 852, 580, 172, "#edf4ed", "#447c55"),
          text(380, 900, ["Updated probability"], 32, 700),
          text(380, 947, ["Combine the prior with how likely", "the evidence is under each alternative."], 28),
          text(380, 1083, ["Similarity can suggest a hypothesis."], 28)]
    return clean_svg('prototype-probability.svg', '\n'.join(s+['</svg>'])+'\n')


if __name__ == "__main__":
    (OUT / "fast-slow.svg").write_text(processing())
    (OUT / "prototype-probability.svg").write_text(representativeness())
