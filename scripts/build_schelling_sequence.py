#!/usr/bin/env python3
"""Generate a deterministic, fully declared Schelling-style teaching run."""

from __future__ import annotations

import random
from pathlib import Path


OUT = Path(__file__).resolve().parents[1] / "figures" / "schelling-emergence.svg"
SEED = 20260830
COLS = 18
ROWS = 14
VACANCY_SHARE = 0.15
MIN_SAME_SHARE = 1 / 3
MAX_SWEEPS = 25


def neighbors(index: int) -> list[int]:
    row, col = divmod(index, COLS)
    result: list[int] = []
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == dc == 0:
                continue
            rr, cc = row + dr, col + dc
            if 0 <= rr < ROWS and 0 <= cc < COLS:
                result.append(rr * COLS + cc)
    return result


def same_share(grid: list[int], index: int, group: int | None = None) -> float:
    focal = grid[index] if group is None else group
    occupied = [grid[j] for j in neighbors(index) if grid[j] != 0]
    if not occupied:
        return 1.0
    return sum(value == focal for value in occupied) / len(occupied)


def segregation_index(grid: list[int]) -> float:
    shares = [same_share(grid, i) for i, value in enumerate(grid) if value != 0]
    return sum(shares) / len(shares)


def run() -> tuple[list[int], list[int], list[int], list[int]]:
    rng = random.Random(SEED)
    cells = COLS * ROWS
    vacancies = round(cells * VACANCY_SHARE)
    occupied = cells - vacancies
    group_a = occupied // 2
    values = [0] * vacancies + [1] * group_a + [2] * (occupied - group_a)
    rng.shuffle(values)
    grid = values
    initial = grid.copy()
    moves_per_sweep: list[int] = []
    after_one = initial.copy()

    for sweep in range(MAX_SWEEPS):
        order = [i for i, value in enumerate(grid) if value != 0]
        rng.shuffle(order)
        moves = 0
        for old in order:
            group = grid[old]
            if group == 0 or same_share(grid, old) >= MIN_SAME_SHARE:
                continue
            vacancies_now = [i for i, value in enumerate(grid) if value == 0]
            satisfying: list[int] = []
            grid[old] = 0
            for new in vacancies_now:
                if same_share(grid, new, group) >= MIN_SAME_SHARE:
                    satisfying.append(new)
            if satisfying:
                new = rng.choice(satisfying)
                grid[new] = group
                moves += 1
            else:
                grid[old] = group
        moves_per_sweep.append(moves)
        if sweep == 0:
            after_one = grid.copy()
        if moves == 0:
            break
    return initial, after_one, grid.copy(), moves_per_sweep


def panel(grid: list[int], x: int, title: str, subtitle: str) -> str:
    cell = 15
    pitch = 17
    start_x = x + 22
    start_y = 226
    bits = [
        f'<rect x="{x}" y="142" width="390" height="430" rx="22" fill="#ffffff" stroke="#bfd0dd" stroke-width="2"/>',
        f'<text x="{x + 195}" y="181" class="panel" text-anchor="middle">{title}</text>',
        f'<text x="{x + 195}" y="207" class="small" text-anchor="middle">{subtitle}</text>',
    ]
    colors = {0: "#ffffff", 1: "#236b8e", 2: "#c44e52"}
    strokes = {0: "#c9d4dd", 1: "#175b7e", 2: "#a83d41"}
    for i, value in enumerate(grid):
        row, col = divmod(i, COLS)
        cx = start_x + col * pitch
        cy = start_y + row * pitch
        bits.append(
            f'<circle cx="{cx}" cy="{cy}" r="{cell / 2 - 1}" fill="{colors[value]}" '
            f'stroke="{strokes[value]}" stroke-width="1"/>'
        )
    bits.append(
        f'<text x="{x + 195}" y="538" class="metric" text-anchor="middle">'
        f'Average same-group-neighbour share: {segregation_index(grid):.2f}</text>'
    )
    return "\n".join(bits)


def build_svg() -> str:
    initial, after_one, final, moves = run()
    sweeps = len(moves)
    total_moves = sum(moves)
    stable = moves[-1] == 0 if moves else True
    final_label = f"after {sweeps} sweeps" + ("; no moves" if stable else "; stopped at limit")
    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="1400" height="810" viewBox="0 0 1400 810" role="img" aria-labelledby="title desc">',
        '<title id="title">A reproducible Schelling-style local-movement simulation</title>',
        '<desc id="desc">Three panels show a random initial population, the population after one sweep, and the final state in a declared Schelling-style model. Local moves increase the average share of same-group neighbors even though no agent seeks aggregate segregation.</desc>',
        '<defs><marker id="arrow" viewBox="0 0 10 8" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto" markerUnits="userSpaceOnUse"><path d="M0.5,0.8 L9,4 L0.5,7.2 z" fill="#587189"/></marker></defs>',
        '<style>.title{font:700 34px -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;fill:#183047}.sub{font:500 18px -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;fill:#52677a}.panel{font:700 22px -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;fill:#183047}.small{font:500 18px -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;fill:#52677a}.metric{font:650 18px -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;fill:#314b61}.foot{font:500 21px -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;fill:#52677a}.legend{font:600 18px -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;fill:#314b61}</style>',
        '<rect x="18" y="18" width="1364" height="774" rx="28" fill="#f7f9fc" stroke="#9fb2c3" stroke-width="2"/>',
        '<text x="700" y="65" class="title" text-anchor="middle">LOCAL MOVES CAN CREATE AN AGGREGATE PATTERN</text>',
        '<text x="700" y="98" class="sub" text-anchor="middle">One seeded teaching run: agents move when their same-group share is below one-third.</text>',
        panel(initial, 45, "1  RANDOM START", "same population; mixed locations"),
        '<path d="M443 357 H499" stroke="#587189" stroke-width="3" stroke-linecap="round" marker-end="url(#arrow)"/>',
        panel(after_one, 505, "2  AFTER ONE SWEEP", f"{moves[0] if moves else 0} sequential moves"),
        '<path d="M903 357 H959" stroke="#587189" stroke-width="3" stroke-linecap="round" marker-end="url(#arrow)"/>',
        panel(final, 965, "3  EMERGENT PATTERN", final_label),
        '<circle cx="411" cy="613" r="8" fill="#236b8e"/><text x="426" y="619" class="legend">Group A</text>',
        '<circle cx="516" cy="613" r="8" fill="#c44e52"/><text x="531" y="619" class="legend">Group B</text>',
        '<circle cx="621" cy="613" r="8" fill="#ffffff" stroke="#c9d4dd"/><text x="636" y="619" class="legend">Vacancy</text>',
        f'<text x="866" y="619" class="legend">Total moves: {total_moves}</text>',
        '<rect x="72" y="646" width="1256" height="118" rx="18" fill="#e9f2f7" stroke="#9fbfd0"/>',
        '<text x="700" y="674" class="foot" text-anchor="middle">18 × 14 bounded grid · 38 vacancies · 107 agents per group · Moore neighbours · minimum same-group share = 1/3</text>',
        '<text x="700" y="706" class="foot" text-anchor="middle">Each sweep shuffles occupied cells; an unsatisfied agent moves uniformly among currently satisfying vacancies.</text>',
        f'<text x="700" y="738" class="foot" text-anchor="middle">Python random.Random · seed {SEED} · one executable teaching hypothesis, not evidence about a real neighbourhood</text>',
        '</svg>',
    ]
    return "\n".join(parts) + "\n"


def main() -> None:
    OUT.write_text(build_svg(), encoding="utf-8")


if __name__ == "__main__":
    main()
