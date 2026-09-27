#!/usr/bin/env python3
"""Recalculate the declared teaching examples; no empirical data are modified.

Run from the repository root with Python 3. Output is written beside this script.
"""
from fractions import Fraction as F
import json
from pathlib import Path

checks = {}

# Appendix D: hypothetical changes in scores, grouped by assignment and receipt.
cells = [(5, F(22, 5)), (5, F(6, 5)), (2, F(3)), (8, F(5, 8))]
assigned = sum(n * mean for n, mean in cells[:2]) / 10
comparison = sum(n * mean for n, mean in cells[2:]) / 10
itt, first_stage = assigned - comparison, F(5, 10) - F(2, 10)
recipients = (5 * F(22, 5) + 2 * 3) / 7
nonrecipients = (5 * F(6, 5) + 8 * F(5, 8)) / 13
assert (itt, first_stage, itt / first_stage) == (F(17, 10), F(3, 10), F(17, 3))
assert recipients - nonrecipients == F(41, 13)
# The text's selected contrast compares offered recipients with comparison
# nonrecipients, not all recipients with all nonrecipients.
selected = cells[0][1] - cells[3][1]
assert selected == F(151, 40)
checks['school_meals'] = dict(itt=str(itt), first_stage=str(first_stage),
                            wald_ratio=str(itt / first_stage),
                            selected_contrast=str(selected))

# Appendix B: fixed-type population examples with positive mean weights.
for i in range(1, 100):
    p = F(i, 100)
    small, large = 3 * (1 - p), 4 * (1 - p) + p
    assert large - small == 1
    assert p * large / (p * large + (1 - p) * small) > p
    hawk, dove = 5 - 4 * p, 3 - p
    next_p = p * hawk / (p * hawk + (1 - p) * dove)
    assert (next_p > p) == (p < F(2, 3))
    assert abs(next_p - F(2, 3)) < abs(p - F(2, 3))
assert 5 - 4 * F(2, 3) == 3 - F(2, 3) == F(7, 3)
checks['evolution'] = dict(interior_grid_checks=99, hawk_share='2/3',
                           equilibrium_weight='7/3')

# Chapters 14, 16, 23 and 25: probability, inventory, lotteries and games.
assert F(9, 10) ** 5 == F(59049, 100000)
assert F(1, 2) * 80 - F(1, 2) * 20 == 30
assert F(1, 5) * 80 - F(4, 5) * 20 == 0
assert F(4, 10) * 2 + F(6, 10) * F(16, 10) == F(176, 100)
assert F(4, 10) * F(385, 100) + F(6, 10) * F(1, 10) == F(160, 100)
assert F(5, 10) * 2 + F(5, 10) * F(16, 10) == F(180, 100)
assert F(5, 10) * F(385, 100) + F(5, 10) * F(1, 10) == F(1975, 1000)
assert F(2, 3) * (F(2, 5) * 50 + F(3, 5) * F(100, 3)) == F(80, 3)
assert F(2, 3) * F(100, 3) == F(200, 9)
assert F(4, 10) * 80 == 32 and 20 + F(4, 10) * 60 == 44
checks['probability_risk_games'] = 'passed'

# Chapters 36 and 38: sharing incremental gains, and a whole-price fee cliff.
for price, cost_a, cost_b in [(50, 25, 25), (150, 50, 100), (250, 75, 175)]:
    outside_a, outside_b = max(0, 100 - price), max(0, 200 - price)
    assert cost_a + cost_b == price
    assert 100 - cost_a - outside_a == 200 - cost_b - outside_b
assert F(1, 100) * 2_000_000 == 20_000
assert F(5, 1000) * 2_100_000 == 10_500
assert 20_000 + F(5, 1000) * 100_000 == 20_500
checks['negotiation_and_contracts'] = 'passed'
checks['passed'] = True
target = Path(__file__).with_name('worked-example-checks.json')
target.write_text(json.dumps(checks, indent=2) + '\n')
print(json.dumps(checks, indent=2))
