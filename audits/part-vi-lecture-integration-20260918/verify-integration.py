#!/usr/bin/env python3
"""Reproduce the numerical examples and check integration-specific invariants."""
from pathlib import Path
from fractions import Fraction as F
import gzip
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
checks = []


def check(name, condition, **details):
    checks.append(dict(name=name, status="PASS" if condition else "FAIL", **details))


chapters = {n: next((ROOT / "chapters").glob(f"{n}-*.qmd")) for n in range(35, 39)}
texts = {n: p.read_text() for n, p in chapters.items()}
baseline = json.loads(gzip.decompress((HERE / "before-sources.json.gz").read_bytes()))

for item in json.loads((HERE / "source-inventory.json").read_text()):
    actual = hashlib.sha256(Path(item["path"]).read_bytes()).hexdigest()
    check("Source PDF unchanged: " + Path(item["path"]).name, actual == item["sha256"])

coverage = (HERE / "coverage.md").read_text()
for title, count in [("Understanding Negotiation", 37), ("Distributive Negotiation", 31), ("Integrative Negotiation", 30)]:
    block = coverage.split("## " + title, 1)[1].split("\n## ", 1)[0]
    pages = []
    for first, last in re.findall(r"^\| (\d+)(?:–(\d+))? \|", block, re.M):
        pages.extend(range(int(first), int(last or first) + 1))
    check("Coverage ledger: " + title, sorted(pages) == list(range(1, count + 1)), pages=len(pages))

for n, path in chapters.items():
    old = baseline[str(path.relative_to(ROOT))]
    new = texts[n]
    title = re.search(r"^# .+$", old, re.M).group()
    epigraph = re.search(r"::: \{#chapter-\d+-start.*?\n:::", old, re.S).group()
    old_ids = set(re.findall(r"\{[^}\n]*#([\w-]+)", old))
    new_ids = set(re.findall(r"\{[^}\n]*#([\w-]+)", new))
    check(f"Chapter {n}: title and epigraph preserved", title in new and epigraph in new)
    check(f"Chapter {n}: explicit anchors retained", old_ids <= new_ids, missing=sorted(old_ids - new_ids))
    # Display equations must remain within a mathematical-analysis callout.
    stack = []
    outside = []
    for line_no, line in enumerate(new.splitlines(), 1):
        fence = re.match(r"^(:{3,})(.*)$", line)
        if fence:
            if fence.group(2).strip():
                stack.append((len(fence.group(1)), "mathematical-analysis" in fence.group(2)))
            elif stack:
                stack.pop()
        if line.strip() == "$$" and not any(math for _, math in stack):
            outside.append(line_no)
    check(f"Chapter {n}: display math in optional boxes", not outside, outside_lines=outside)

# Parse the actual printed MPharm rows, and independently recompute the results.
rows = re.findall(r"^\| ([A-E]) \| ([^\n]+)\|$", texts[38], re.M)
expected_terms = {"A": (25, 0), "B": (20, 15), "C": (15, 20), "D": (-10, 100), "E": (2, 80)}
case = {}
for label, raw in rows:
    values = [F(s.strip().replace("−", "-")) for s in raw.split("|") if s.strip()]
    x, y, printed_chen, printed_mpharm = values
    chen = x + F(3, 5) * y - 20
    mpharm = F(9, 10) * (20 - x) + F(1, 10) * (120 - x - y)
    check(f"MPharm {label}: original payments and printed gains", (x, y) == expected_terms[label] and (chen, mpharm) == (printed_chen, printed_mpharm))
    check(f"MPharm {label}: subjective-gain identity", chen + mpharm == 10 + F(1, 2) * y)
    # With a common probability, transfer terms cancel.
    for p in [F(0), F(1, 10), F(3, 5), F(1)]:
        common_total = (x + p * y - 20) + ((1-p) * (20-x) + p * (120-x-y))
        assert common_total == 100 * p
    case[label] = {"upfront": float(x), "bonus": float(y), "chen_expected_gain": float(chen), "mpharm_expected_gain": float(mpharm), "mpharm_without_approval": float(20-x), "mpharm_with_approval": float(120-x-y)}
check("MPharm: all five packages present", set(case) == set(expected_terms))
check("MPharm D: no financial approval incentive", case["D"]["mpharm_without_approval"] == case["D"]["mpharm_with_approval"] == 30)
check("MPharm E: retains 20 million approval incentive", case["E"]["mpharm_without_approval"] == 18 and case["E"]["mpharm_with_approval"] == 38)
check("Tom's initial reservation salary", 1600 - 500 == 1100 and "$1,100" in texts[36])
check("House reservation price", 550000 - (410000-350000) == 490000 and "**$490,000**" in texts[36])
check("Service menu: illustrative equal margins", 650000-500000 == 635000-485000 == 150000 and "$150,000" in texts[38])
check("Midpoint example", (6000+10000)//2 == 8000 and (8000+10000)//2 == 9000)

report = {"status": "FAIL" if any(c["status"] == "FAIL" for c in checks) else "PASS", "checks": checks, "mpharm": case,
          "word_counts_including_references": {str(n): {"before": len(baseline[str(p.relative_to(ROOT))].split()), "after": len(texts[n].split())} for n, p in chapters.items()}}
(HERE / "integration-qa.json").write_text(json.dumps(report, indent=2) + "\n")
print(f"{report['status']}: {len(checks)} integration checks; 98 PDF pages accounted for.")
for c in checks:
    if c["status"] == "FAIL":
        print(c)
raise SystemExit(0 if report["status"] == "PASS" else 1)
