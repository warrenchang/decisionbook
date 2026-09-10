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
    pitch=17
    parts=[f'<g id="panel-{x}"><rect x="{x}" y="125" width="390" height="420" rx="20" fill="white" stroke="#bfd0dd" stroke-width="2"/>',
           f'<text x="{x+195}" y="170" text-anchor="middle" class="head">{title}</text>',
           f'<text x="{x+195}" y="211" text-anchor="middle">{subtitle}</text>']
    colors={0:"white",1:"#236b8e",2:"#c44e52"}
    for i,value in enumerate(grid):
        r,c=divmod(i,COLS)
        parts.append(f'<circle cx="{x+50+c*pitch}" cy="{244+r*pitch}" r="6.5" fill="{colors[value]}" stroke="#8b9dab" stroke-width=".7"/>')
    parts.append(f'<text x="{x+195}" y="514" text-anchor="middle">Same-group share: {segregation_index(grid):.2f}</text></g>')
    return "\n".join(parts)


def build_svg() -> str:
    initial,after_one,final,moves=run()
    parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1400" height="665" viewBox="0 0 1400 665" role="img" aria-labelledby="title desc">',
           '<title id="title">Local moves can create separation</title>',
           '<desc id="desc">One seeded Schelling-style simulation shows the same agents initially, after one sweep, and after convergence. The mean share of same-group neighbors increases from .48 to .64 to .68. No agent seeks an aggregate segregation pattern.</desc>',
           '<style>text{font:26px Arial,Helvetica,sans-serif;fill:#183047}.head{font-size:28px;font-weight:700}</style>',
           '<defs><marker id="arrow" viewBox="0 0 10 8" markerWidth="9" markerHeight="8" refX="9" refY="4" orient="auto" markerUnits="userSpaceOnUse"><path d="M0 0L9 4L0 8Z" fill="#587189"/></marker></defs>',
           '<rect width="1400" height="665" fill="#f7f9fc"/>',
           '<text x="700" y="56" text-anchor="middle" style="font-size:36px;font-weight:700">Local moves can create separation</text>',
           '<text x="700" y="97" text-anchor="middle">One teaching run; each agent seeks at least one-third same-group neighbors.</text>',
           panel(initial,45,"1. Random start","Same population"),
           '<path d="M435 335H505" stroke="#587189" stroke-width="3" marker-end="url(#arrow)"/>',
           panel(after_one,505,"2. After one sweep",f"{moves[0]} moves"),
           '<path d="M895 335H965" stroke="#587189" stroke-width="3" marker-end="url(#arrow)"/>',
           panel(final,965,"3. No further moves",f"{len(moves)} sweeps; {sum(moves)} moves total"),
           '<circle cx="365" cy="598" r="10" fill="#236b8e"/><text x="386" y="607">Group A</text>',
           '<circle cx="555" cy="598" r="10" fill="#c44e52"/><text x="576" y="607">Group B</text>',
           '<circle cx="745" cy="598" r="10" fill="white" stroke="#8b9dab"/><text x="766" y="607">Vacancy</text>',
           '<text x="1005" y="607">Seed: 20260830</text>', '</svg>']
    return "\n".join(parts)


if __name__ == "__main__":
    OUT.write_text(build_svg())
    _,_,_,moves=run()
    print(f"{OUT}: {len(moves)} sweeps; {sum(moves)} moves")
