#!/usr/bin/env python3
"""One-time migration to number chapter files by the current book order.

The migration renames the 41 canonical QMD sources, updates source/config/QA
references, and adds a Quarto alias for every former public HTML path. Former
chapters that were merged during the structural revision are retained beside
the book sources with an explicit ``retired-`` prefix.
"""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

# Ordered by the current reader-facing chapter sequence.
CHAPTER_RENAMES = {
    "01-the-choice-is-the-tip-of-the-iceberg": "01-how-decisions-should-be-made-and-how-they-actually-are",
    "02-a-rational-benchmark-not-a-portrait": "02-building-a-better-decision-alternatives-opportunity-cost-information-and-robustness",
    "05-attention-is-the-gatekeeper-of-evidence": "03-attention-what-becomes-evidence",
    "06-the-predictive-mind": "04-the-predictive-mind-perception-is-inference",
    "07-value-is-constructed": "05-valuation-how-options-become-worth-choosing",
    "08-expectations-that-become-causes": "06-expectations-when-predictions-become-causes",
    "18-the-narrator-after-the-choice": "07-the-narrator-after-choice-why-reasons-are-not-always-causes",
    "04-fast-answers-slow-inspection": "08-fast-and-frugal-thinking",
    "10-feeling-and-availability-as-shortcuts": "09-what-feels-likely-availability-affect-and-resemblance",
    "13-biases-that-protect-a-story": "10-beliefs-that-defend-themselves",
    "14-anchors-halos-decoys-and-escalation": "11-when-context-rewrites-comparison",
    "15-frames-change-the-decision": "12-framing-when-the-same-facts-become-different-decisions",
    "16-priming-and-the-active-mental-context": "13-accessibility-familiarity-and-ease",
    "12-base-rates-randomness-and-calibration": "14-base-rates-conditional-probability-and-bayesian-updating",
    "12b-samples-randomness-regression-calibration": "15-samples-randomness-regression-and-calibration",
    "39-risky-decision-making": "16-risky-decision-making-a-probability-is-not-yet-a-feeling",
    "40-prospect-theory": "17-prospect-theory-gains-and-losses-begin-at-a-reference-point",
    "41-decisions-from-experience": "18-decisions-from-experience-when-rare-events-are-not-encountered",
    "38-intertemporal-choice": "19-intertemporal-decision-making-why-later-loses-to-now",
    "42-mental-accounting": "20-mental-accounting-money-is-fungible-minds-label-it",
    "19-habits-when-decisions-move-downstairs": "21-habits-wanting-and-self-control",
    "45-subjective-well-being": "22-deciding-for-a-better-life-satisfaction-connection-and-meaning",
    "46-strategic-interdependence": "23-strategic-interdependence-the-best-move-depends-on-other-minds",
    "47-behavioral-game-theory": "24-behavioral-game-theory-equilibrium-is-a-benchmark-not-a-portrait",
    "48-cooperation-social-preferences": "25-cooperation-and-social-preferences-self-interest-is-not-the-only-payoff",
    "22-social-learning-mimicry-and-attribution": "26-social-norms-and-conformity-when-other-people-become-evidence",
    "43-behavioral-finance": "27-markets-mispricing-and-bubbles",
    "24-authority-bystanders-and-influence-triggers": "28-authority-groupthink-and-shared-responsibility",
    "37-culture-identity-social-meaning": "29-culture-and-identity-the-same-action-is-not-the-same-act",
    "25-persuasion-is-model-updating": "30-persuasion-changing-minds-means-updating-models",
    "26-why-stories-move-minds": "31-why-stories-move-minds",
    "27-building-an-evidence-aligned-story": "32-building-an-evidence-aligned-message",
    "28-communication-is-joint-inference": "33-communication-language-is-not-a-file-transfer",
    "29-the-art-of-conversation-and-repair": "34-connection-and-repair-warm-honesty-makes-truth-usable",
    "30-negotiation-is-joint-decision-making": "35-negotiation-as-joint-decision-design",
    "31-preparing-to-claim-value": "36-preparing-and-claiming-value",
    "33-interests-priorities-and-trade-offs": "37-creating-value-across-differences",
    "34-mesos-contingent-contracts-and-better-agreements": "38-designing-better-agreements",
    "21-designing-behavior": "39-behavior-design-make-the-better-action-easier",
    "36-choice-architecture": "40-choice-architecture-the-environment-gets-a-vote",
    "35-decision-hygiene": "41-decision-hygiene-build-a-process-that-can-learn",
}

RETIRED_RENAMES = {
    "03-opportunity-cost-information-and-better-options": "retired-opportunity-cost-information-and-better-options",
    "09-heuristics-the-adaptive-toolbox": "retired-heuristics-the-adaptive-toolbox",
    "11-resemblance-is-not-probability": "retired-resemblance-is-not-probability",
    "17-fluency-familiarity-and-the-feeling-of-truth": "retired-fluency-familiarity-and-the-feeling-of-truth",
    "20-wanting-craving-and-self-control": "retired-wanting-craving-and-self-control",
    "23-conformity-norms-and-social-proof": "retired-conformity-norms-and-social-proof",
    "32-anchors-concessions-and-bargaining-tactics": "retired-anchors-concessions-and-bargaining-tactics",
    "44-asset-bubbles": "retired-asset-bubbles",
}

TEXT_SUFFIXES = {".qmd", ".md", ".yml", ".yaml", ".py", ".js", ".cjs", ".json", ".csv", ".txt", ".toml"}
SKIP_TOP_LEVEL = {".git", ".quarto", "_epub", "docs", "figures", "legacy-static-build", "qa-screenshots", "tmp"}


def migration_state() -> str:
    destinations = list(CHAPTER_RENAMES.values()) + list(RETIRED_RENAMES.values())
    if len(destinations) != len(set(destinations)):
        raise SystemExit("Duplicate destination basename in migration map.")
    old_present = []
    new_present = []
    for old, new in {**CHAPTER_RENAMES, **RETIRED_RENAMES}.items():
        source = ROOT / "chapters" / f"{old}.qmd"
        target = ROOT / "chapters" / f"{new}.qmd"
        old_present.append(source.exists())
        new_present.append(target.exists())
    if all(old_present) and not any(new_present):
        return "pending"
    if not any(old_present) and all(new_present):
        return "complete"
    raise SystemExit("Chapter filename migration is in a mixed or incomplete state.")


def rename_sources() -> None:
    for old, new in {**CHAPTER_RENAMES, **RETIRED_RENAMES}.items():
        source = ROOT / "chapters" / f"{old}.qmd"
        target = ROOT / "chapters" / f"{new}.qmd"
        source.rename(target)


def should_update(path: Path) -> bool:
    relative = path.relative_to(ROOT)
    if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
        return False
    if relative.parts and relative.parts[0] in SKIP_TOP_LEVEL:
        return False
    if path.resolve() == Path(__file__).resolve():
        return False
    # These Markdown files belong to the retired hand-built edition.
    if relative.parts and relative.parts[0] in {"chapters", "parts"} and path.suffix == ".md":
        return False
    return True


def update_references() -> list[Path]:
    replacements = {**CHAPTER_RENAMES, **RETIRED_RENAMES}
    changed: list[Path] = []
    for path in sorted(ROOT.rglob("*")):
        if not should_update(path):
            continue
        try:
            original = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        revised = original
        for old, new in replacements.items():
            revised = revised.replace(old, new)
        if revised != original:
            path.write_text(revised, encoding="utf-8")
            changed.append(path)
    return changed


def add_alias(path: Path, old_stem: str) -> None:
    text = path.read_text(encoding="utf-8")
    alias = f"  - {old_stem}.html"
    if alias in text[:1000]:
        return
    metadata = f"---\naliases:\n{alias}\n---\n\n"
    if text.startswith("---\n"):
        text = text.replace("---\n", f"---\naliases:\n{alias}\n", 1)
    else:
        text = metadata + text
    path.write_text(text, encoding="utf-8")


def main() -> int:
    state = migration_state()
    if state == "complete":
        print("Chapter filename migration is already complete.")
        return 0
    rename_sources()
    changed = update_references()
    for old, new in CHAPTER_RENAMES.items():
        add_alias(ROOT / "chapters" / f"{new}.qmd", old)
    print(f"Renamed {len(CHAPTER_RENAMES)} canonical chapter sources.")
    print(f"Marked {len(RETIRED_RENAMES)} merged sources as retired.")
    print(f"Updated references in {len(changed)} text files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
