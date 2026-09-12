# Personally verified against source (not agent-reported)

## CORRECTNESS DEFECTS — Pass 1

### 1. Arithmetic impossibility, ch15:190
Three delay routes at 15% / 10% / 20%; text then says "the inside model gives 18 percent."
A union cannot be below its largest component. ch14:88 teaches P(A∪B)=P(A)+P(B)−P(A∩B) using the
SAME supplier/software delay example. Fix: raise 18% above 20% (≈32%), OR state that the 18% is
P(misses final date) after slack, which the text never says.

### 2. Internal contradiction, ch31:164 vs ch31:168
:164 cites Small et al. (2007): identifiable person elicited more giving than statistics.
:168 prescribes "begin with one person's story, then connect it to accurate statistics."
Small et al.'s third condition (identifiable + statistics) REDUCED giving vs identifiable alone —
the paper is about deliberative thought suppressing sympathy. The book recommends what the cited
study found counterproductive. Fix states the awkward result; it is the chapter's best material.

### 3. Iowa Gambling Task misattributed, ch06:131
"Bechara and colleagues (1997) developed the Iowa Gambling Task." The IGT was introduced in
Bechara, Damasio, Damasio & Anderson (1994, Cognition 50, 7–15). The 1997 Science paper is the
anticipatory skin-conductance follow-up. Reference list contains only the 1997 entry.

### 4. Stanovich mechanism unsupported, ch10:47
"Myside bias can appear even among intelligent and educated people BECAUSE intelligence can help
people generate better arguments for what they already believe (Stanovich et al., 2013)."
Stanovich, West & Toplak (2013) found myside bias largely INDEPENDENT of cognitive ability — a
dissociation. The causal "because" is not their finding.

### 5. Miller & Ross inverted, ch10:69
Cited for the full self-serving pattern incl. attributing failure externally. Miller & Ross (1975)
"Fact or fiction?" argued the self-enhancing (success) half was supported and the self-protective
(failure) half was NOT. Carry the existence claim on Mezulis et al. (2004); give Miller & Ross their
actual sceptical role.

### 6. Prose cross-reference points at wrong chapter, ch06:149
"The endowment effect, discussed again in *Framing: When the Same Facts Become Different Decisions*"
— ch12 contains "endowment" 0 times; ch17 contains it 8 times.
NOTE: this is a defect class my link checker cannot catch. All 170 MARKDOWN links resolve; the book
also cross-references by italic chapter title in prose, and those are unverified.

### 7. Appendix F corrections have not propagated back
- Appendix F:252 states Scheibehenne et al. found a "near-zero mean effect" for choice overload and
  links to Ch2. ch02:104 cites (Iyengar & Lepper, 2000; Scheibehenne et al., 2010; Chernev et al.,
  2015) in ONE parenthetical as if they agreed. Direct internal contradiction.
- Appendix F:253 features Watts, Duncan & Quan (2018) on the marshmallow test and links to Ch19.
  "Watts" appears in ch19 ZERO times. ch19 corrects the task using only Kidd et al. (2013).
- COUNTEREXAMPLE (do not "fix"): ch05:174 carries its stereotype-threat correction properly
  (Flore & Wicherts, 2015; Shewach et al., 2019; publication bias named). The problem is uneven
  propagation, not a systemic failure.

### 8. Prospect theory parameters without provenance, ch17:97
"estimated α=β=0.88 and λ=2.25 in their data." "Their data" = 25 graduate students
(Tversky & Kahneman 1992, Berkeley/Stanford). One clause does more debunking than the abstract
caveat the chapter already carries.

## PART OPENERS PROMISE CASES THE CHAPTERS DO NOT DELIVER (verified by count)
- Part I: "The hiring case develops along the way" → ch01=18 mentions, ch02=2, ch03=1,
  ch04=0, ch05=0, ch06=0, ch07=0. The book's signature case (built in the Preface) vanishes.
- Part V: "A recurring organizational-change example" → ch30=2, ch31–34=0.
- Part VI: "follows a supplier relationship and an employment package across four chapters" →
  supplier: ch35=11, ch36=0, ch37=12, ch38=21. ch36 runs entirely on a used-car sale.
  "employment package" essentially absent.

## CHAPTER 1 STRUCTURE (the reader's first real chapter)
- "## Six ways context enters choice" visibly contains only examples 1–3.
- Examples 4–5 sit inside ::: {.callout-note icon=false collapse=true} → default view jumps 3 → 6.
- Example 6 sits under a ### inside that callout's scope.
- Only heading-level jump in the entire book: ch01:140 (h2 → h4).
- Four stale "seven" identifiers: #seven-ways-context-enters-choice,
  #two-suggestive-cases-with-weaker-evidence, #what-the-seven-examples-establish-and-what-they-do-not,
  {#tbl-seven-context-examples}. The first is linked from concept-index.qmd:213.

## COLLAPSED SYNTHESIS TABLES (41 collapse=true callouts total)
Correct use: "Research Lens", "Research note", "Advanced research track", "Optional…".
INCORRECT use — these are synthesis/comparison tables collapsed by default:
  ch22 "Compare the six questions" (4-col table: predicted/decision/experienced/remembered utility)
  ch25 "Compare the cooperation mechanisms" (4-col)
  ch24 "Compare the three lenses" (3-col)
  ch28 "Diagnose the pathway" (3-col — the chapter's CENTRAL diagnostic, hidden, in the flattest
       chapter in the book)
  ch26 "A reference table for social cues" (4-col)
  ch01 "Two examples from commercial practice" (numbered sequence items 4–5)
Fix: collapse=false for these; keep collapse for genuine research depth.

## CROSS-REFERENCE APPARATUS IS UNUSED
- 131 of 136 tables (96%) carry {#tbl-…} but are NEVER referenced with @tbl- in prose.
- 82 of 107 figures (77%) carry {#fig-…} but are NEVER referenced with @fig- in prose.
- 51 table ids carry STALE chapter numbers from an earlier ordering (ch30 has tbl-25-1,
  tbl-25-barriers, tbl-25-model-update, tbl-25-influence-signals; ch41 has tbl-35-1, tbl-36-noise…).
- SEQUENCING: normalize the stale ids FIRST, then add the @tbl-/@fig- references. Doing it in the
  other order bakes wrong numbers into prose.

## FIGURE SYSTEM (measured)
- 80 of 109 referenced figures (73%) forced into a 900px horizontal-scroll pane below 768px by
  quarto-custom.scss. Allowlist of 23 is hand-maintained and STALE (lists context-enters-choice.svg,
  referenced nowhere; also a dead CSS rule at quarto-custom.scss:174).
- The author has already solved this. The 29 allowlisted figures follow a consistent spec:
      canvas 640–800 wide (vs 1200–1670) · aspect ≤1.5, often PORTRAIT (0.72–1.25)
      minimum font-size 24–32 (vs 16–17) · → 13–18px effective text at 390px, no sideways scroll
  Worst offenders: decision-making-according-to-behavioral-evidence 1600×700 (2.29),
  decision-loop 1670×736 (2.27), urge-wave-observation 1200×530, digital-arrow-affordance 1440×660,
  schelling-emergence 1400×665. Median scroll-pane aspect 1.67.
- 364 distinct hex colors across 126 SVGs (core palette is ~8). 7 font-family spellings for 3
  intents. Book CSS is Inter + Georgia; only 16/126 SVGs use Georgia.
- 17 orphan .svg on disk. Among them figures/natural-frequencies.svg — a natural-frequency tree
  (10,000 people / 100 diseased / 90 of 981 positives true) exactly matching ch14's section
  "## Natural frequencies make Bayes visible", which currently has NO figure.
- All 7 part-opener captions are identical boilerplate; the fig-alt carries the real content
  (the three questions). None has a {#fig-} id.
- Tooling exists for a systematic re-spec: scripts/normalize_figure_text.py (box-aware text
  wrapping), build_*_figures.py, render_svg_png_fallbacks.cjs, qa_figure_connectors.py.

## PROSE METRICS (body text only; front matter/tables/callouts/refs stripped)
BOOK MEANS: sentence 15.8w (sd 7.6) · short(≤10w) share 26.8% · hedges 24.0/1k · numbers 16.9/1k
· paragraph 48.8w.  Rhythm variance is HEALTHY — do NOT claim the prose is monotone globally.

Composite flatness (hedged + abstract + monotone + dense paragraphs):
  ch28 +6.26  ← outlier; next is +2.99
  ch30 +2.99 · ch08 +2.97 · ch07 +2.86 · ch21 +2.55 · ch35 +2.39 · ch05 +2.30 · ch01 +2.26
Most vivid (the in-book model): ch16 −7.19 · ch14 −5.66 · ch24 −3.66 · ch17 −3.55
LEAST CONCRETE: ch31 7.0 numbers/1k (the STORYTELLING chapter) · ch09 8.2 · ch02 8.6 · ch37 8.7
LONGEST PARAGRAPHS: ch28 61.0w · ch33 58.5 · ch35 57.7 · ch30 56.7

THE SMOKING GUN: ch28's only body numbers are years plus "7,700" and "51". Milgram's 26-of-40 / 65%
appears NOWHERE in the book. Darley & Latané's rates appear nowhere. ch26 links to YouTube Asch
demos but never gives Asch's figures.
BUT: ch05:151 already does it right (Yeager: 0.10 GPA points; 36% vs 33%). So the fix is "apply your
own ch05/ch16 standard to ch28/ch26/ch31", NOT a change of voice.

## VISUAL STARVATION (words per figure+table)
ch14 1942 (1 fig, 0 tables) · ch16 1670 (1 fig) · ch17 1532 (1 fig) · ch31 1364 · ch10 1160
· ch42 1074 · ch18 954 · ch13 927 · ch28 924 · ch20 905
ch16 (risky choice) and ch17 (prospect theory) — the most quantitative chapters — have ONE figure
each; ch17's single figure carries BOTH the value function and the weighting function.

## WHAT IS ALREADY EXCELLENT — do not "fix"
- Retractions/expressions of concern BOLDED in reference entries (Shu 2012; Mazar 2008;
  Ariely & Wertenbroch 2002 incl. the Sept 2026 retraction at ch19:191).
- ch05:151 growth mindset: Sisk et al. (2018) + exact Yeager effect sizes.
- ch05:174 stereotype threat: heterogeneity + publication bias named.
- ch40:204-206 nudges: Mertens vs Maier publication-bias reanalysis, plus DellaVigna & Linos
  1.4pp (nudge units) vs 8.7pp (academic). NEVER quote 8.7 without the 1.4 pair.
- ch11: decoy effect sourced to Huber, Payne & Puto (1982); Ariely (2008) explicitly labelled
  "a reported classroom demonstration".
- Ego depletion / power posing / facial feedback quarantined in Appendix F.
- 170 internal markdown links: 0 broken. 116 figure refs: 0 missing files, 0 missing alt text,
  0 duplicate ids. One heading-level jump in 195,000 words.

## ONE REAL GAP IN AN OTHERWISE EXCELLENT TREATMENT
ch11 never cites the attraction-effect replication limits (Frederick, Lee & Baskin 2014,
"The limits of attraction"; Yang & Lynn 2014) — attraction effects are hard to reproduce with real,
non-numeric attributes. The chapter is otherwise a model treatment.

## CONSISTENCY / HYGIENE
- Chapter title "Data Driven Decision Making" unhyphenated; 29 hyphenated "data-driven" elsewhere.
- how-to-use-this-book.qmd promises an "Applied Module" reading layer; exactly ONE exists (ch23:243).
- Chapters 20, 22, 27 lack a ## Core Idea.
- ~40 one-off callout classes render as undifferentiated plain notes (only .core-idea, .activity,
  .research-lens, .evidence-and-boundary-conditions have CSS).
- ch11 "Return to the product-manager search" — "product manager" appears nowhere else in the book.
- Repo debt (not book content): 36 legacy chapters/*.md, 8 chapters/retired-*.qmd, 4 orphan parts
  (part-8/9/10, applied-interlude), dead CSS rule at quarto-custom.scss:174.

## VERIFIED GENUINE ORPHAN REFERENCE ENTRIES (small tail, not systemic)
ch39 Gollwitzer (1999) — body cites only Gollwitzer & Sheeran (2006).
ch18 Hertwig & Erev (2009) — never cited in body.
Epigraph-only sources (James 1890 ch03, Bayes 1763 ch14, Bruner 1991 ch31) are LEGITIMATE.
My crude detector ran ~50% false positives (possessives "Esser's (1998)", "Fazio and colleagues
(2015)", multi-cites "(Simon, 1955, 1956)") — treat any large uncited-reference count with suspicion.
