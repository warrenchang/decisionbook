Scope and verification notes.

All three files read in full, top to bottom. I additionally checked every citation in both directions, every figure and table label against the whole manuscript, and every prose cross-reference against the named chapter's actual content.

What is already correct and should NOT be touched:
- Reference lists are complete in both directions in all three chapters: every in-text citation has an entry and every entry is cited. No orphans, no dangling citations.
- Every prose cross-reference in these three chapters names the right chapter. "Chapter 38 explains the conditions that make such terms workable" (37 L192) matches ch38's contingent-terms module; "Chapter 35 distinguished a position from the interest it protects" (37 L111) matches ch35 L67; "Chapter 36 develops preparation and claiming; Chapter 37 develops discovery" (35 L87) is accurate. The wrong-chapter error the brief mentions is not in these files.
- Ch36's winner's-curse paragraph (L124) is a genuinely good disambiguation and needs no change.
- Ch36's Tey et al. (2021) description (L203) is exemplary: seven studies, the interactive-study qualifier, the sender/recipient asymmetry, and the protective moderator, all correctly hedged. Do not flag it.
- Ch37's Pareto definition is correctly relativized to a specified feasible set, and footnote ch37-value-units correctly blocks the interpersonal-comparison error. The framing is right; only the sentence construction needs work.
- Ch37's handling of the Malhotra & Bazerman case ("report the case with identifying details changed") and of Camp David ("an official U.S. account describes") are appropriately sourced and hedged.
- Ch35's ethics callout (two tests: defensible if understood, acceptable if used against you) is the strongest short ethics passage in the part.

Two cross-file issues surfaced that need a decision outside these chapters:
1. concept-index.qmd L411 routes Informed consent to chapters/36#ch36-research-findings — an empty anchor at a section that contains no consent material. Reported as a ch36 finding; the fix may belong in the index.
2. concept-index.qmd L563 routes Overconfidence to Ch. 36, but chapter 36 never mentions overconfidence; chapter 35 does (L117, "Anchoring, overconfidence, self-serving interpretation"). L407 and L773 similarly route Inequality aversion and Social preferences to Ch. 37, which discusses neither. Not reported as findings since the fix is in the index, not in the assigned files, but worth handing to whoever audits concept-index.qmd.

Also worth noting for a later pass: chapters/retired-anchors-concessions-and-bargaining-tactics.qmd contains material that was lost rather than migrated — the Loschelder et al. (2016, 2017) too-much-precision citations (now absent from references.qmd entirely) and the named bolstering/bracketing range distinction. Both are reported as ch36 findings. It may be worth a systematic diff of the retired negotiation chapters against 35–38 to see what else was dropped.

========

Both chapters are structurally sound and voice-consistent; the dominant failure mode is the one already identified for the book — published numbers are systematically absent from the studies each chapter leans on. Chapter 38 runs 3,904 words with zero quantities anywhere in its running case (no contract value, no volumes, no dates, no named parties), and the one figure that does carry numbers (@fig-lie-cues-belief-gap, max |r| = .19) is never cross-referenced or discussed in the body. Chapter 39 reports four field experiments and two meta-analyses without a single effect size; its strongest evidence (Gollwitzer & Sheeran's d ≈ 0.65) appears only inside a collapse=true callout. Two items rise above stylistic concerns: chapter 39 recommends self-imposed deadlines as a precommitment device, which chapter 19 explicitly says the retracted Ariely and Wertenbroch (2002) study cannot support; and chapter 39's showcase mini-case changes five things at once in direct contradiction of its own one-change rule. Verified as correct and deliberately left unflagged: Bond and DePaulo's 54/47/61 percent figures and sample sizes; the Schweitzer and Croson two-study description; the perspective-taking/getting attribution to chapter 33; the defaults handoff to chapter 40; the BRAIN pointer to chapter 21; the addiction and legal-drafting footnotes. All numbers I recommend adding are flagged for verification against the source papers before printing.

========

RANKED FINDINGS — REDUNDANCY, OVERLAP, AND CROSS-REFERENCE ACCURACY (whole-book sweep)

METHOD. I extracted every chapter title, then (a) regex-matched every italic `*Chapter Title*` span against the title list, separating bare-italic prose references from markdown links; (b) extracted every bare prose "Chapter N"/"Appendix X" reference and verified by grep that the named chapter actually contains the claimed content; (c) ran an 8-gram and 10-gram cross-file duplicate detector over all 42 chapters and 6 appendices with reference sections, figure captions, and link URLs stripped; (d) counted inbound and outbound cross-links per chapter; (e) traced each named study and concept from the brief by grep across all files.

HEADLINE. Two conclusions, one reassuring and one not.

The reassuring one: the famous-study duplication the brief anticipated mostly does not exist. Asian disease appears in only two chapters; Milgram, Linda, ultimatum, Iowa Gambling, Loftus, WEIRD, organ-donation defaults, and Camp David each appear in exactly one chapter plus an index. Asch looks duplicated but is not — ch11 uses Asch (1946) on impression formation, ch26 uses Asch (1956) on line judgment, genuinely different studies. The "jam study" likewise: ch07 uses Hall et al. (2010) on choice blindness, ch40 uses Iyengar & Lepper (2000) on overload. Prisoner's Dilemma is fully developed only in ch25. The author has been disciplined about not retelling the canon.

The unwelcome one: the book's connective tissue is far thinner than its content. Across 42 chapters there are only 79 outbound chapter links, and chapters 1 and 42 carry 26 of them. TWENTY chapters have zero outbound markdown cross-links; eight of those (03, 09, 11, 14, 23, 29, 33, 36) also have zero prose "Chapter N" references. The result is a hub-and-spoke book: Chapter 1 promises everything, Chapter 42 gathers everything, and Parts II through VI read as free-standing units. Every duplication below is a symptom of the same cause — when a chapter cannot point, it re-explains.

────────────────────────────────────────
A. CONTENT DUPLICATED AT SIMILAR LENGTH
────────────────────────────────────────

1. MASLOW / KENRICK — ch06:180-198 ↔ appendix-b:53-76. HIGH. The worst case by a wide margin: 64 shared 8-grams, including the fully identical sentence "On Maslow's account, when several needs are seriously deprived, the relatively prepotent need is more likely to dominate attention." Same five need classes, same "relative prepotency" term, same Bridgman et al. (2019) pyramid correction, same shared-meal example, same Wahba & Bridwell (1976), same Tay & Diener 123-countries result, same Kenrick reorganization, same self-actualization removal with the same Kesebir and Peterson & Park rebuttals. ACCIDENTAL — ch06's only Appendix B link (line 65) points at #four-questions-not-one-cause, nowhere near this section. VERDICT: Appendix B should be the full treatment (it has the three-representation comparison table ch06 lacks); ch06 shrinks to ~3 sentences plus @fig-overlapping-motive-systems, which is the one asset Appendix B does not have.

2. ASIAN DISEASE — ch12:61 ↔ ch17:16-30. HIGH. Presented twice at full length. ch17 uses it as the opening scenario ("Imagine an outbreak expected to kill 600 people") without naming it or citing T&K at that point; ch12 names and cites it. Zero links between the two chapters in either direction. Compounding harm: the preregistered 19-country replication (Ruggeri et al. 2020, n=4,098) sits only in ch17:162, so the chapter titled *Framing* never shows the reader the replication evidence for its own flagship study. VERDICT: ch17 keeps the full presentation; ch12 shrinks to two sentences and links forward.

3. FRAMING TAXONOMY — ch12:54-61 ↔ ch17:153-158. MEDIUM, separable from #2. Two competing category systems five chapters apart: ch12 gives attribute/goal/risky-choice; ch17 gives risky-choice/attribute/goal/reference-point/substantive. Neither acknowledges the other. VERDICT: ch12 owns the taxonomy (it is the chapter named for it) and absorbs ch17's two extra categories; ch17 reduces to one deferring sentence.

4. PSYCHOLOGICAL SAFETY — ch12:105, ch28:57, ch29:248, ch41:198. MEDIUM. Defined from scratch four times, Edmondson (1999) in four separate reference lists, zero cross-links. ch29:248 and ch41:198 share the verbatim clause "It does not mean comfort, agreement, or low standards." Only ch28:57 carries the concrete grounding ("51 work teams"). VERDICT: ch28 is the full treatment; ch29 and ch41 keep their local application and link back. Note the book already does this correctly for the five groupthink pathways (ch34:242 and ch41:200 both restate the list but both link to ch28) — that is the in-house pattern to copy.

5. CHOICE OVERLOAD — ch02:104 ↔ ch40:86. MEDIUM. Five shared 8-grams; identical moderator list; identical three citations (Iyengar & Lepper 2000, Scheibehenne 2010, Chernev 2015). Division of labour is inverted: ch40 has the jam study, ch02 has only the abstract caveat and arrives 38 chapters earlier, so the reader meets the qualification before the phenomenon. VERDICT: ch40 full; ch02 becomes a one-line forward pointer and drops three citations.

6. EVOLUTIONARY / SPATIAL MODELS — ch24:125-127 ↔ appendix-b:225-251. MEDIUM. Ten shared 8-grams; the same six citations. Peculiar because ch24 *already links* to Appendix B in the same paragraph, then duplicates what it points to. VERDICT: cut ch24's last two sentences, let the existing link do its job.

7. PROCESS vs OUTCOME — ch01:200-204 ↔ ch41:281. LOW. Deliberate reinforcement and appropriate, but inconsistently executed: ch07, ch16, ch18, ch27 all link back to #outcome-is-not-process; ch41 — the practical process chapter, the one readers jump to directly — does not.

8. MINIMUM AI-USE RECORD — ch41:168-178 ↔ appendix-c:303-313. NOT A DEFECT. Ten shared 8-grams, but Appendix C is explicitly a portable standalone toolkit and closes by naming ch41. Correct by design; leave it.

9. WATCHED EYES — ch25:124 ↔ appendix-f:39. NOT A DEFECT. ch25 links to the exact Appendix F anchor. Model behaviour.

10. ERROR MANAGEMENT (ch08:88 ↔ appB:118) and DISTRIBUTED VALUE RESEARCH LENS (ch06:254 ↔ ch16:199). NOT DEFECTS. Both link correctly; ch16→ch06 even links to the precise research-lens anchor. These prove the author knows the pattern — it is applied unevenly, not absent.

────────────────────────────────────────
B. PROSE CROSS-REFERENCE ERRORS
────────────────────────────────────────

I verified every bare prose reference in the book. Results: 23 italic-title references, of which 22 are wrapped in working markdown links; 41 bare "Chapter N"/"Appendix X" prose references, of which I checked every content claim by grep.

THE ONE HARD ERROR — ch06:149: "The endowment effect, discussed again in *Framing: When the Same Facts Become Different Decisions*". Chapter 12 contains no instance of "endowment", "ownership", or Knetsch. The endowment effect is in ch17:210-216 under "### Endowment effects: giving up is not the same as owning", citing the same Kahneman et al. (1990) mug study ch06 cites. This is also the book's only bare-italic prose chapter reference not wrapped in a link — which is precisely why it rotted. Fix and link it.

VERIFIED CORRECT (do not re-report): ch01:83 and :198 → ch2 feasible set/opportunity cost ✓. ch05:51 → ch14/15 probability and calibration ✓. ch05:176 → ch29 identity and culture ✓. ch06:78 → ch13 accessibility/priming ✓. ch06:135 → ch9 affect heuristic ✓. ch06:242 → ch19 intertemporal ✓. ch08:118 → ch6 Damasio/somatic markers ✓. ch10:126 → ch15 overestimation/overplacement/overprecision and Dunning–Kruger ✓ (ch15:129 handles it carefully, with Gignac & Zajenkowski). ch13:64 → ch6 and ch9 ✓. ch31:180 → ch32 construction workflow ✓. ch32:115 → ch13 fluency ✓. ch32:157 → ch41 structured-judgment evidence ✓ (ch41:146, Meehl/Dawes/Grove). ch32:209 → ch33 ✓. ch35:87 → ch36/37/38 ✓. ch35:113 → ch38 culture, truthfulness, verification ✓ (ch38:141, :155). ch37:56 and :111 → ch36 preparation, ch35 position/interest ✓. ch37:192 → ch38 contingent terms ✓. ch38:139 → ch33 perspective-taking vs perspective-getting ✓ (ch33:89). ch39:103 → ch40 defaults ✓. ch39:199 → ch21 BRAIN classroom mnemonic ✓ (ch21:190-208). ch41:206 → ch30-40 ✓. ch42:66 → ch41 ✓. All "the next chapter" promises in ch16:112, ch16:143, ch17:123, ch23:83, ch24:156, ch27:233 resolve correctly.

SOFT / MISDESCRIBING REFERENCES:
- ch34:104 "the ask–listen–reflect–verify loop from Chapter 33" — ch33 never names a four-step loop; its only version is ch33:89 "Use perspective-getting: ask, listen, and verify" (three steps, no "reflect", not called a loop). Fix in ch33 by promoting the label, since ch34's four steps are the better procedure.
- ch12:65 "The risky-choice chapter" — ambiguous between ch16 (titled *Risky Decision-Making*) and ch17 (which actually holds the reference-point content promised). The reader cannot resolve it.
- ch12:35 "Prospect theory develops this reference dependence" — theory named, chapter not, no link.
- ch04:49 "The later chapters on expectations and probability judgment" and ch04:183 "later chapters on heuristics, belief protection, framing, and probability judgment" — four concepts, no chapter numbers, no links. Low severity but the same habit.

DEFINITION-ORDER PROBLEM: BATNA is used as a bare acronym at ch35:55 ("A deal can be worse than the BATNA") and is never expanded in ch35; the expansion arrives only at ch36:38. ZOPA is separately defined twice inside ch36 (line 44 and again at line 83, which also silently adds a third synonym, "bargaining zone").

────────────────────────────────────────
C. PAIRS THAT SHOULD CROSS-LINK AND DO NOT
────────────────────────────────────────
Each named with the host sentence where the link belongs:

- ch36:148 → ch11. "extending anchoring research on numerical judgment (Tversky & Kahneman, 1974)" cites the exact wheel-of-fortune study ch11:38 works through, and ch36's next sentence replies to ch11's insufficient-adjustment-vs-selective-accessibility debate. Both chapters have zero outbound links.
- ch11:46 → ch36. "Anchoring is not always irrational... The problem is that anchors influence judgment even when they are irrelevant, extreme, strategic, or weakly justified" — "strategic" is the first-offer case, which is ch36's whole subject.
- ch35:117 → ch11, ch15, ch10. "Anchoring, overconfidence, self-serving interpretation, reactive devaluation, and fixed-pie assumptions" names four mechanisms developed elsewhere, with no link to any of them.
- ch19:175 → appendix F. The marshmallow paragraph gives Kidd et al. (2013) but omits Watts, Duncan & Quan (2018), which Appendix F:253 documents as substantially attenuating the association. ch19 does link to Appendix F — but at line 191, for the Ariely retraction, about a different study. Closing this is the single cheapest integrity win in the sweep.
- ch12 ↔ ch17, both directions (see A2, A3).
- ch26:77 → ch11. Flag that Asch (1956) is a different program from the Asch (1946) impression work in ch11, or readers will assume a revisit.
- ch33:89 → ch38:139. ch38 links back to ch33 on perspective-getting; ch33 never points forward to where the idea becomes a negotiation procedure.
- ch14 → ch42. ch14 (base rates) has zero outbound links; ch42:61 links to ch14 but not the reverse, even though ch42's base-rate material is the applied payoff.

────────────────────────────────────────
D. WHAT IS ALREADY RIGHT
────────────────────────────────────────
The ch01:123 → ch11 decoy handoff is the model the rest of the book should follow: ch01 gives the short version and links out; ch11 supplies the full evidence with Ariely's actual counts (16/0/84 versus 68/32). Same for ch25 → Appendix F on watched eyes, ch16 → ch06 on the distributed-value research lens, ch08 → Appendix B on error management, and ch34/ch41 → ch28 on the groupthink pathways. The mechanism exists and works; it is applied to perhaps a third of the places that need it. Fixing the twenty zero-link chapters is a mechanical, low-risk pass that would do more for "easy to follow" than any amount of new prose.

Note on scope: I did not re-report the concreteness gap (missing Milgram and Asch rates), the identical part-opener captions, the missing Core Ideas in ch20/22/27, or figure/link/alt-text status, all of which the brief lists as already established. One observation that touches both briefs: ch11:38 and ch11:76 DO give exact published numbers (the 10-versus-65 wheel; 16/0/84 versus 68/32), and ch38:159 gives 206 documents, 24,483 judges, 54 percent. The book already knows how to be concrete — the omissions are localized, not systemic.

========

Read all three files in full (1,252 lines total). Absolute paths: /Users/ra25fi/Library/CloudStorage/OneDrive-AalborgUniversitet/decision_book/appendices/appendix-a-rational-choice-and-decision-analysis.qmd, .../appendix-b-evolutionary-explanations-of-value-choice-and-rationality.qmd, .../appendix-c-portable-course-tools.qmd. Findings above use repo-relative paths to match the assignment.

VERIFIED CLEAN — do not re-flag:
- Citation completeness runs both directions in A and B. Appendix A: all 9 reference entries cited in text, all 9 in-text citations have entries. Appendix B: all 42 entries cited, all ~40 in-text citations have entries. No orphans either way.
- Bibliographic details spot-checked against the literature: McNeil 1982 NEJM 306(21) 1259-1262; Huber/Payne/Puto 1982 JCR 9(1) 90-98; Frederick et al. 2009 JCR 36(4) 553-561; Edwards 1954 Psych Bull 51(4) 380-417; Simon 1955 QJE 69(1), Simon 1956 Psych Rev 63(2); Tinbergen 1963 Z. Tierpsychol 20(4); Mayr 1961 Science 134(3489); Maynard Smith & Price 1973 Nature 246; Schelling 1969 AER 59(2); Hamilton 1964 JTB 7(1); Kenrick et al. 2010 PPS 5(3); Tay & Diener 2011 JPSP 101(2); Bridgman et al. 2019 AMLE 18(1); Imhof et al. 2007 JTB 247(3). All correct. Only the vNM 1944-vs-1947 point is off, and it is minor (finding A12).
- Appendix A's mathematics is correct throughout. Checked: the finite-set sufficiency claim at line 55 (correctly restricted to finite nonempty A, with the infinite-domain caveat properly footnoted); p* = (u(c)-u(L))/(u(H)-u(L)) and the direction of preference; the w* algebra at lines 366-375 (derived independently, matches); EVPI >= 0 and 0 <= EVSI <= EVPI under the stated conditions; the discrete replicator rule in Appendix B. Do not send anyone hunting for math errors here.
- Appendix A's scale discipline is genuinely excellent and should be left alone: the ordinal/cardinal distinction is stated in a callout, re-invoked before OC(a), re-invoked again before Delta_ab, and used to block the "the gap is small" inference. Same for the footnote blocking an expected-score model from being called an expected-utility representation.
- Appendix B hedges correctly in every place I checked: error-management theory is stated as a conditional about the model rather than a finding; Rahnev's objection to resource-rational analysis is given alongside Lieder & Griffiths; the three-claims separation at lines 126-132 is the sharpest statement of the can-outperform / actually-use / evolved-because distinction I have seen in a textbook; Sapolsky's free-will conclusion is explicitly not presented as consensus, with compatibilism cited as a live alternative; the Bennett stages carry a footnote refusing the ladder-of-progress reading. None of this needs touching.
- The Schelling provenance passage (lines 245-251) is a model of what the rest of the book's simulation reporting should look like — seed, generator, grid size, agent counts, neighbourhood definition, tie-breaking, stopping rule, and the resulting move count all recorded. Worth citing internally as the house standard.
- Appendix C's internal tool anchors all resolve: the twelve #tool-* targets in @tbl-canonical-tools each exist.

CROSS-FILE PATTERN worth the parent agent's attention: the one wrong-chapter cross-reference I found is Appendix C line 313 (Chapter 41 named for a distinction that belongs to Chapter 42). Given the prompt's note that at least one such error exists, this is likely it — but the same file has a second, subtler routing failure in the same box (the AI-use record does not link back to Chapter 41's #minimum-ai-use-record, which IS its source), which suggests the two links were swapped rather than one being mistyped.

CONCRETENESS TALLY for the parent's running list of famous studies published without their numbers, from these three files: McNeil et al. 1982 (18% vs 44%) missing in Appendix A line 157 AND in Chapter 1 line 109; Huber et al. 1982 attraction-effect magnitudes missing in Appendix A line 167 AND in Chapter 11 line 74; Goldstein & Gigerenzer 2002 less-is-more result missing in Appendix B line 93; Nesse 2005 smoke-detector cost ratio missing in Appendix B line 124; Axelrod tournament entry counts and Rapoport's name missing in Appendix B line 251; Bridgman et al.'s McDermid 1960 attribution missing in Appendix B line 57. Frederick et al. 2009 is the one case where the chapter has the numbers (Ch 2 line 116: 75% to 55%, plus the Maguire 2023 meta-analysis) and the appendix dropped them — which is the more dangerous pattern, because the appendix also dropped the replication qualifier.

LARGEST SINGLE OPPORTUNITY across the three files: Appendix A is 3,245 words, twenty-nine display equations, zero figures, zero tables, one callout, and not one numeral in the running text. Threading one quantified job offer through sections 6, 7 and 8 (finding A4) plus the probability-threshold figure (A6) and the notation table (A7) would change the character of the appendix more than any other edit available in these files.

========

=====================================================================
PART 1 — THE CALLOUT TAXONOMY (primary deliverable)
=====================================================================

CENSUS (measured, not estimated). Live book = 42 chapters + 6 appendices + parts/part-1..7 + front matter, i.e. everything `_quarto-html.yml` actually builds.

  160 callout blocks. 41 distinct custom classes.
  Base types: .callout-note 136, .callout-tip 15, .callout-caution 6, .callout-important 3.

SIX classes have CSS in quarto-custom.scss, not four:
  .core-idea (L64), .activity (L65), .part-overview (L66), .loop-location (L67-70),
  .research-lens (L71-74), .evidence-and-boundary-conditions + unused alias .evidence-boundary (L75-79).

  Styled and rendering:  90 callouts  (core-idea 42, research-lens 36, activity 7, evidence-and-boundary-conditions 4, loop-location 1)
  Rendering as plain notes: 70 callouts (31 carry NO custom class; 39 carry a one-off class with no CSS)
  .part-overview: 4 uses, ALL in parts/part-8.qmd, part-9.qmd, part-10.qmd, applied-interlude.qmd — none of which appears in _quarto-html.yml. This CSS renders nowhere.

THE KEY STRUCTURAL FACT that reframes the whole problem:
30 of the ~35 one-off classes live in ONE file — appendices/appendix-c-portable-course-tools.qmd. They are not scattered chapter improvisations. They are the 30 entries of the Portable Tools appendix, each given a unique class so it can be anchored. Only NINE one-off-classed callouts exist across all 42 chapters (.watch-and-test x3, .personal-example x2, .calibration-test, .loop-location, .applied-module, .media-example, .the-final-standard).

So this is two problems, not forty:
  (A) Appendix C needs ONE type with THREE levels. The appendix ALREADY declares those levels in @tbl-tool-levels ("Quick check / Core tool / Specialized extension") and a twelve-tool canonical list — the CSS simply never renders the author's own scheme.
  (B) The 42 chapters need ~4 new types that the book currently expresses through bare callout-note/callout-tip plus inconsistent titles.

---------------------------------------------------------------------
THE CONSOLIDATED TAXONOMY — 9 types
---------------------------------------------------------------------

1. .core-idea — KEEP UNCHANGED
   Purpose: the single claim the chapter defends, stated before the argument runs.
   Use when: exactly once per chapter, immediately after the opening scenario.
   Visual (existing): left border var(--book-warm) #b95f2d, no tint, no icon.
   Coverage: 42/42 chapters. This is the book's most disciplined device — leave it alone.

2. .research-lens — KEEP, ABSORB STRAYS
   Purpose: optional depth — a formal model, a measurement detail, a live literature debate — skippable without losing the argument.
   Use when: the block answers "how do we know this?" or "what does the formal version say?", NOT "what should I do?".
   Visual (existing): border #6f5d9b, bg #f7f4fb, title in var(--book-ink) weight 750. Default collapse=true.
   Absorbs: the six bare "Research note:" / "Evidence note:" boxes at ch03:62, ch05:153, ch06:177, ch06:219, ch07:90, and appendix-b:185/199/220, appendix-a:82.

3. .evidence-boundary — KEEP, RENAME (short alias already has CSS at L76)
   Purpose: names a claim the evidence does NOT support, adjacent to a striking finding.
   Use when: a memorable result is about to be over-read (a brain region, an anomaly, a bundled redesign, a depletion story).
   Visual (existing): .callout-caution base, border #b36a43, bg #fff8f3. This is the only place .callout-caution is correct.
   Retire the 33-character name `.evidence-and-boundary-conditions` in favour of `.evidence-boundary` (both selectors already exist; delete the long one after migration).

4. .tool  (+ modifiers .tool--core / .tool--quick / .tool--extension)  — NEW, THE BIG CONSOLIDATION
   Purpose: a reusable worksheet or protocol the reader completes on their own live case, producing an inspectable artifact.
   Use when: the block has fillable slots AND names an output ("Record the forecast and a rule for resolving it").
   Do NOT use when: the block is a table you consult rather than complete (-> .reference-table), or a rule you obey (-> .standard).
   Visual: border #2b7a78 (reuse the existing .activity teal so the tool family and the lab family read as one system), bg #f2f8f7.
     .tool--core      : 5px solid left border; badge "CORE TOOL"; clipboard icon.
     .tool--quick     : 3px solid left border; badge "QUICK CHECK"; stopwatch icon.
     .tool--extension : 3px dashed left border; badge "EXTENSION"; plus icon; collapse=true by default.
   Rationale: @tbl-tool-levels already defines exactly these three levels and their expected outputs. Rendering them turns Appendix C from a 30-box wall into a navigable, self-routing reference.

5. .predict-first — NEW; the highest-value addition in this list
   Purpose: the reader commits to an answer, rating, or observation BEFORE the text reveals the result.
   Use when: the next paragraphs contain a number, outcome, or reveal that reads as obvious once seen.
   Visual: border #c9a227 (amber), bg #fffdf2, icon = circled question mark, standing label "PREDICT FIRST — write your answer before reading on". Deliberately the loudest treatment in the book; it is the only element that asks the reader to stop.
   Why it matters: the book contains ~10 of these and every one is invisible. They appear under SEVEN different titles ("Watch and test", "Calibration test", "Try the social prediction", "Watch and diagnose", "Watch for the mismatch", "Check your denominator", "Before reading on…") and FOUR different classes (.watch-and-test, .calibration-test, .media-example, none). how-to-use-this-book.qmd promises this layer — "Before reading a result, pause when invited to make a prediction" — and the reader cannot see where the invitation is.

6. .applied-module — NEW CSS (class exists, used once at ch23:243)
   Purpose: extends the chapter's mechanism into one named domain — operations, finance, clinical, classroom, media.
   Use when: the content is a DOMAIN application. Methods and theory asides belong in .research-lens.
   Visual: border var(--book-accent) #25678f, bg var(--book-panel) #f4f7fa, label "APPLIED MODULE — <domain>", collapse=true.
   This honours the front-matter promise without writing new content (see Part 3).

7. .standard — NEW
   Purpose: a short, binding rule the reader is asked to hold to — ethical, procedural, or a naming convention.
   Use when: the block states a constraint rather than an explanation or an exercise. Typically 2-4 sentences, never a table.
   Visual: .callout-important base, border var(--book-ink) #183047, bg #f4f7fa, no icon, small-caps label "STANDARD".

8. .reference-table — NEW
   Purpose: a lookup or compare grid you consult; not a task you perform.
   Use when: the block is a table with no fillable slots and no instruction to produce anything.
   Visual: border var(--book-line) #d7e0e7, NO background tint, title in var(--book-muted), collapse=true. Deliberately the quietest treatment in the system so a lookup never competes visually with an idea.

9. .author-aside — NEW
   Purpose: the author's own first-person anecdote, or a single third-party case, used as illustration and explicitly not as evidence.
   Use when: one vivid case would otherwise be mistaken for data.
   Visual: border var(--book-muted) #607080, no tint, italic standing label "ILLUSTRATION, NOT EVIDENCE".
   The book already contains the anchor `#illustration-not-evidence` (ch26:95) — this type gives that idea a visual home, and it is a genuine extension of the manuscript's scientific discipline rather than decoration.

RETIRE / RESOLVE:
  .loop-location   — PROMOTE, don't retire (see finding). One use, full CSS.
  .part-overview   — the 4 uses are in unbuilt files. Either delete the CSS or delete parts/part-8|9|10|applied-interlude.qmd.
  .activity        — SPLIT. As an end-of-chapter Practice Lab wrapper it must go (it removes the section from the TOC). Keep it for in-body mini-exercises and rename `.mini-lab` so it cannot be confused with the Practice Lab.
  .ai-decision-canvas — retire the class. The block is a two-sentence cross-reference stub pointing at ch42; make it a linked row in @tbl-canonical-tools instead.

---------------------------------------------------------------------
COMPLETE MAPPING TABLE — every existing class -> new type
---------------------------------------------------------------------

A. APPENDIX C — the twelve canonical tools -> .tool .tool--core
   .one-page-decision-journal        -> .tool .tool--core
   .decision-audit-studio            -> .tool .tool--core
   .attention-audit                  -> .tool .tool--core
   .prediction-valuation-split       -> .tool .tool--core
   .heuristic-detector               -> .tool .tool--core
   .probability-judgment-audit       -> .tool .tool--core
   .risky-choice-audit               -> .tool .tool--core
   .strategic-interdependence-map    -> .tool .tool--core
   .behavior-redesign-canvas         -> .tool .tool--core
   .verified-understanding-loop      -> .tool .tool--core
   .negotiation-preparation          -> .tool .tool--core
   .structured-judgment-pipeline     -> .tool .tool--core
   .ethical-audit                    -> .tool .tool--core  [AND add to @tbl-canonical-tools; see finding]

B. APPENDIX C — specialized extensions -> .tool .tool--extension
   .expectation-loop-map, .bias-redesign-studio, .experience-sample-audit,
   .intertemporal-most-audit, .mental-accounting-audit, .market-claim-audit,
   .well-being-measurement-audit, .choice-architecture-audit, .meso-contingency,
   .model-updating-message, .ai-use-record,
   .classroom-practice-protocols  [+ retitle "For instructors: case, video, and conversation practice"]

C. APPENDIX C — quick checks -> .tool .tool--quick
   .layered-listening, .urge-surf

D. APPENDIX C — not tools at all
   .negotiation-tactic-diagnostic -> .reference-table   (a 7-row lookup of bargaining moves; nothing to fill in)
   .mediation-arbitration         -> .reference-table   (a definitional contrast; no task)
   .ai-decision-canvas            -> RETIRE (cross-reference stub -> table row)

E. CHAPTER ONE-OFFS
   .watch-and-test  (ch03:86, ch03:133, ch10:59) -> .predict-first
   .calibration-test (ch04:202)                  -> .predict-first
   .media-example   (ch34:51)                    -> .predict-first  ["Before watching, predict what kind of help each person thinks…"]
   .personal-example (ch12:37, ch40:92)          -> .author-aside
   .applied-module  (ch23:243)                   -> .applied-module (keep; add CSS)
   .the-final-standard (ch41:38)                 -> .standard
   .loop-location   (ch21:142)                   -> .loop-location, promoted to all 42 chapters (or folded into .core-idea)
   .part-overview   (4x, unbuilt files)          -> RETIRE

F. BARE CALLOUTS (31) — assign a type
   -> .research-lens : ch03:62, ch05:153, ch06:177, ch06:219, ch07:90,
                       appendix-b:185, appendix-b:199, appendix-b:220, appendix-a:82
   -> .evidence-boundary : ch13:140 (its own anchor already says evidence-boundary),
                           ch01:137 (its own anchor already says #two-suggestive-cases-with-weaker-evidence)
   -> .reference-table : ch22:48 "Compare the six questions", ch24:48 "Compare the three lenses",
                         ch25:50 "Compare the cooperation mechanisms", ch26:46 "A reference table for social cues",
                         ch27:150 "Classification details", ch28:93 "Diagnose the pathway",
                         ch38:60 "Add an advanced module only for a diagnosed problem"
   -> .predict-first : ch14:173 "Check your denominator", ch26:94 "Try the social prediction",
                       ch37:36 "Watch and diagnose: position versus interest", ch39:222 "Optional Media Lab"
   -> .tool .tool--quick : ch06:116 "A price audit", ch29:130 "Application: make difficulty identity-safe",
                           ch34:132 "Two small practices that strengthen connection"
   -> .standard : ch16:169 "Process check: risk does not rewrite decision quality",
                  ch35:105 "Ethics is part of agreement quality",
                  ch41:260 "The same-name rule",
                  appendix-f:216 "Read the status, not just the headline"
   -> .applied-module : ch16:244 "Application box: the single-period newsvendor"

G. .activity (7) — SPLIT
   ch39:203, ch40:250, ch41:354 -> UNWRAP. Delete the callout div; leave `## Practice Lab` as a plain section.
   ch30:67, ch41:102, appendix-e:417, appendix-f:200 -> .mini-lab (renamed .activity, same teal)

RESULT: 41 classes -> 9 types. 160/160 callouts carry a type. 0 render as undifferentiated notes.

=====================================================================
PART 2 — THE TWELVE WEAKEST PRACTICE LABS, REWRITTEN
=====================================================================
Format for each rewrite: INPUT / STEPS / OUTPUT ARTIFACT / SUCCESS CHECK / TIME.
Every one of the 42 labs should carry a time budget; none currently does.

1. ch40 (thinnest in the book; group-only; no artifact named)
   INPUT: one subscription, enrolment, or appointment flow you personally used in the last month.
   STEPS: (1) screenshot or write out every step from first prompt to confirmation; (2) label each step with one of: menu, default, mapping, friction, timing, social information, exit; (3) mark the single step where an understandable intention became hardest to carry out; (4) write the causal sentence "Changing X should affect Y because mechanism Z"; (5) name one alternative instrument (boost, incentive, mandate, structural change) and one harm measure.
   OUTPUT: a labelled seven-column path map plus one causal sentence and one harm measure.
   SUCCESS CHECK: a reader who has never used the service can point to the decisive step from your map alone, and your causal sentence names a mechanism rather than restating the outcome.
   TIME: 35 minutes solo. Group exchange ("would this remain defensible if users understood it completely?") becomes an optional extension.

2. ch24 (needs a group to play five rounds)
   INPUT: the published distributions from a two-thirds-game dataset the chapter cites, or eight numbers you collect by text message from friends.
   STEPS: (1) before seeing any data, write your own number and the mean you predict; (2) compute the target; (3) classify each player's number as level-0, level-1, level-2, or deeper; (4) write three rival accounts of the spread — deeper reasoning, belief learning, imitation; (5) design one additional round or treatment on which the three accounts predict different means.
   OUTPUT: an annotated level distribution plus one discriminating treatment.
   SUCCESS CHECK: for your proposed treatment you can state the number each of the three accounts predicts, and the three numbers differ.
   TIME: 30 minutes solo; the live game becomes the classroom version.

3. ch25 (needs a partner across five rounds)
   INPUT: the chapter's payoff table and the Golden Balls episode already linked in ch25.
   STEPS: (1) write your own choice and your belief about the other player's choice before watching; (2) after the reveal, place the episode on the four-rung mechanism ladder — repetition, reputation or enforcement, social preference, norm or identity; (3) for each adjacent pair of rungs, name one observation that would separate them; (4) state which rung the episode actually supports and which it cannot.
   OUTPUT: a four-rung ladder with a separating observation on each rung boundary.
   SUCCESS CHECK: at least one rung is marked "not identified by this episode" with the reason.
   TIME: 30 minutes solo.

4. ch36 (requires a pair)
   INPUT: the used-car case as given, plus the chapter's preparation sheet fields.
   STEPS: (1) complete the seller's preparation sheet — BATNA, reservation value, target, estimated counterpart limit, evidence, opening decision, planned questions; (2) complete the BUYER's sheet from the buyer's side; (3) write the offer-and-concession transcript you would expect between those two sheets, marking each justification; (4) compute each party's surplus and mark the single move where an anchor changed an estimate.
   OUTPUT: two preparation sheets plus a self-played transcript with surplus computed for both sides.
   SUCCESS CHECK: your reservation value is defended by an arithmetic comparison to the €8,000 alternative, not asserted; and you can name one concession you made that your own sheet did not justify.
   TIME: 40 minutes solo.

5. ch37 (requires a counterpart who corrects you)
   INPUT: the supplier case and the seven issues already listed (exclusivity, volume, timing, price, investment, quality, relationship).
   STEPS: (1) allocate 100 points across the seven issues for your side; (2) allocate 100 points for the counterpart as you currently believe them to be; (3) build three packages of roughly equal value to you that trade differently; (4) for each package compute whether it beats both BATNAs; (5) write the ONE question whose answer would most change your counterpart allocation, and the revised package under each plausible answer.
   OUTPUT: two point allocations, three scored packages, one diagnostic question with two branched revisions.
   SUCCESS CHECK: the three packages differ by at least 20 points on at least two issues, and each branch of the diagnostic question leads to a different revised package.
   TIME: 35 minutes solo.

6. ch42 (four rounds, two people, a real tool, authorized data)
   INPUT: one recurring decision you personally make weekly.
   STEPS: (1) complete all eight rows of @tbl-ai-decision-canvas before touching a tool; (2) record your own forecast and provisional choice for one live case; (3) give the tool the bounded job named in the canvas and save its output verbatim; (4) classify every difference between you and the tool as evidence, probability, values, feasibility, or authority; (5) write the review date and the result that would withdraw the tool.
   OUTPUT: a completed canvas, a pre-registered human forecast, the verbatim tool output, and a classified disagreement list.
   SUCCESS CHECK: the "Tool and baseline" row names a simple rule the tool must beat, and at least one disagreement is classified as values or authority rather than evidence.
   TIME: 40 minutes solo. Round 1's two-person independence becomes the classroom version.

7. ch34 (requires an observer)
   INPUT: one genuinely low-stakes issue, written out as three sentences of what happened.
   STEPS: (1) draft the verified-understanding exchange — one ask, one paraphrase, one accepted correction; (2) draft the warm-honesty opening — observable behavior, impact, inquiry, reviewable request; (3) draft the repair — acknowledgment, responsibility, remorse, repair, changed behavior; (4) run the self-audit: highlight every clause that asserts what the other person intended, wanted, or felt.
   OUTPUT: three short drafts with motive-claims highlighted in the author's own hand.
   SUCCESS CHECK: after revision, no highlighted clause remains in the warm-honesty opening; every retained inference is phrased as a question.
   TIME: 30 minutes solo.

8. ch32 (peer feedback + 90-second delivery)
   INPUT: one research claim, policy, product, or negotiation proposal you already hold a view on.
   STEPS: (1) fill the five STORY rows; (2) in Reasons, classify the pivotal claim with @tbl-27-claim-evidence and state what the evidence does NOT establish; (3) answer the three audit questions; (4) record yourself reading the brief aloud for 90 seconds; (5) listen back once and mark the first sentence whose force exceeds its evidence.
   OUTPUT: the completed brief, a 90-second recording, and one marked over-claim with its repair.
   SUCCESS CHECK: the marked sentence, rewritten, still supports the "Yes" row.
   TIME: 35 minutes solo; the recording replaces the peer.

9. ch27 (conditional on materials the reader may not have)
   INPUT: name the one public event study the chapter already discusses, so no reader is stranded. Supply the event date, benchmark, and reported abnormal return in the lab text itself.
   STEPS: unchanged (first public time, expected-return model, windows, estimate with uncertainty, overlapping news, tradable timing, costs).
   OUTPUT: unchanged one-page audit plus the two closing sentences.
   SUCCESS CHECK: the "stronger claim the evidence does not support" names a specific quantity, not a sentiment.
   TIME: 30 minutes. Keep the reproduction extension explicitly optional and conditional — that framing is already correct.

10. ch15 (resolves in four weeks; nothing checkable today)
    Split into Part A / Part B. PART A TODAY (25 min): the full ledger — event, resolution source, probability, two reference classes, inside-view mechanism, one counter-argument, 10th/50th/90th percentiles with every adjustment from the outside view explained, and a dated update trigger. SUCCESS CHECK FOR PART A: a stranger could resolve the event without asking you a question, and every percentile adjustment has a stated reason. PART B, DATED (10 min): enter the outcome, score it, and diagnose whether the error was sampling, model, or confidence — without editing Part A.

11. ch21 (a week of recording; nothing checkable today)
    Split. PART A TODAY (20 min): steps 1-3 as written, plus a written directional prediction ("in the next seven opportunities I expect the new response on at least N"). SUCCESS CHECK FOR PART A: the prediction names a number and the recording sheet has dated rows ready. PART B, DATED (10 min): the week's tally against the prediction, plus the lapse-recovery sentence actually used.

12. ch01 (five steps, no named artifact, no success check)
    OUTPUT ARTIFACT to add: a two-column page — "How it should be made" beside "How it is being made" — with the decision loop sketched underneath and one function circled.
    SUCCESS CHECK to add: the circled function is one you could change before the decision closes, and the named evidence has a source and a date by which it could arrive.
    TIME: 30 minutes.

=====================================================================
PART 3 — THE THREE "MISSING CORE IDEA" CHAPTERS
=====================================================================
They are NOT missing. All 42 chapters contain exactly one `.core-idea` callout. Chapters 20, 22, and 27 write the heading as `## Core idea` (lowercase i) while the other 39 write `## Core Idea`. A case-sensitive grep reports them as absent. The fix is three one-character edits, not three drafts:

  chapters/20-mental-accounting-money-is-fungible-minds-label-it.qmd:33            ## Core idea -> ## Core Idea
  chapters/22-deciding-for-a-better-life-satisfaction-connection-and-meaning.qmd:34 ## Core idea -> ## Core Idea
  chapters/27-markets-mispricing-and-bubbles.qmd:26                                ## Core idea -> ## Core Idea

Their existing text is good and in voice; do not replace it.

=====================================================================
PART 4 — THE "APPLIED MODULE" DECISION
=====================================================================
Neither cut nor build. The modules already exist — eleven of them across seven chapters — under six different names, and only one carries the class:

  ch16:244  "Application box: the single-period newsvendor"          bare callout-note   [operations]
  ch16:271  "Optional theory lens: the St Petersburg puzzle"         .research-lens      [theory -> stays research-lens]
  ch19:206  "Applied Lens: compare the complete time stream"         .research-lens
  ch21:190  "Optional practice: observing an urge with BRAIN"        .research-lens
  ch23:243  "Applied module: market rules change the strategic game" .applied-module     [the only correctly classed one]
  ch25:246  "Applied Lens: measuring and enforcing social meaning"   .research-lens
  ch38:75   "Optional module 1: Reveal priorities through packages"  plain ## heading
  ch38:105  "Optional module 2: Use contingent terms…"               plain ## heading
  ch38:131  "Optional module 3: Stage disclosure and verification"   plain ## heading
  ch38:174  "Optional module 4: Negotiate the process"               plain ## heading
  ch38:187  "Optional module: when direct negotiation needs a third party"  .research-lens
  ch39:222  "Optional Media Lab"                                     bare callout-note

RECOMMENDATION: relabel, do not write. Apply `.applied-module` to ch16:244, ch19:206, ch23:243, ch25:246, ch38:187, ch39:222, and convert ch38's four plain "Optional module N" headings into `.applied-module` callouts routed from @tbl-agreement-module-routing. Leave ch16:271 and ch21:190 as `.research-lens` (theory and practice, not domain application), and demote the three "Advanced research track" boxes (ch24:123, ch25:202, ch27:238) to plain `.research-lens` titling so "track"/"lens"/"module" stop competing.
Result: 7 chapters (16, 19, 23, 25, 38, 39 and, via routing, 40) carry a visible Applied Module. The front-matter promise is kept with zero new prose.

IF the author wants 4-6 MORE, the cheapest are the ones whose material already exists elsewhere in the book:
  ch14 -> clinical screening: the 10,000-person natural-frequency tree applied to one named diagnostic test.
  ch27 -> the Palm/3Com case already in @tbl-extended-example-index, worked as a limits-to-arbitrage module.
  ch30 -> the ch01 Google-arrow case, already cross-linked to ch40, as a persuasion-versus-interface module.
  ch34 -> clinical and managerial conversation: the repair sequence under a duty-of-care constraint.
  ch03 -> safety-critical dashboards: the attention map applied to an alarm system.


========

Read all three files in full and verified claims against sources, the chapter files, and by executing code.

VERIFIED CORRECT (do not re-flag): Appendix E's worked simulation reproduces exactly — I ran the snippet with seed 20260830 and got 380/600 control, 417/600 treatment, 63.33% vs 69.5%, ITT 6.17 pp, 95% CI 0.83–11.50 pp, matching the prose. Appendix F's selected-literature simulation also checks out: with effect 0.20, SE 0.20, theoretical power is 17.0%, 328/2000 ≈ 16.4% pass the filter, and ~3 of those are expected to have the wrong sign (text says four). OSC 2015 (97%/36%/half magnitude), Camerer 2016 (11 of 18, 66%), Franco 2014 (221 studies, 40/60 percentage points), Fanelli 2009 (1.97%), Phillips 1993 (1.3–4.9 years), Watts 2018 (two thirds after controls) all match the published sources. Cross-references I spot-checked are correct, not wrong: ego depletion → Ch. 39 (Ch. 21 never mentions depletion; Ch. 39 line 175 does), Mazar → Ch. 7 (line 93), marshmallow/deadlines → Ch. 19, choice overload → Ch. 40 (line 86), stereotype threat → Ch. 5 (line 174), monkey–panda–banana and the insult study → Ch. 29. Appendix F's reference list is complete in the citation→entry direction (I checked all ~60). The retraction/expression-of-concern bolding and the dated evidence map are exemplary and I did not touch them.

CROSS-FILE PATTERNS worth the parent agent's attention:
1. Famous studies stripped of their numbers is confirmed in these files: Simmons/Nelson/Simonsohn (5%→61%, "When I'm Sixty-Four"), Button et al. (median power 21%), Iyengar & Lepper (60/40 stopping, 3%/30% buying), Carney/Cuddy/Yap vs Ranehill (n=42 vs N=200), Hagger et al. (d=0.04, CI −0.07 to 0.15), Bateson et al. (2.76×, ten weekly observations). Chapter 40 line 86 repeats the number-free jam sentence verbatim, so the fix should be applied in both places.
2. Table cross-references: all 13 table ids across the three appendices (@tbl-recurring-case-map, @tbl-extended-example-index, @tbl-linked-video-cases, @tbl-experimental-workflow, @tbl-claim-families, @tbl-evidence-designs, @tbl-claim-design-matching, @tbl-evidence-design-card, @tbl-worked-reminder-design, @tbl-credibility-questions, @tbl-research-safeguards, and both famous-findings tables) are referenced from nowhere in the manuscript. Reported once, under Appendix D.
3. Appendix D is isolated: it never mentions Appendix E or F, and Appendix E never links to F although F links to E.
4. Callout density: Appendix D has 0 callouts, Appendix E has 1 in 5,200 words, Appendix F has 2 in 5,000 words — far below the chapters. None of the four styled classes (.core-idea, .research-lens, .evidence-and-boundary-conditions) appears in any of the three.
5. Section anchors in Appendix E depend entirely on Pandoc stripping the leading "9. " from numbered headings; renumbering would silently break the concept-index deep links. Worth adding explicit {#ids} at some point.

========

WHOLE-BOOK SWEEP: POSITIONING, GAPS, AND MISSING CONTENT

Read: index.qmd, how-to-use-this-book.qmd, how-to-read-evidence.qmd, about.qmd, README.md, _quarto-html.yml, all seven parts/part-N.qmd, all 42 Core Idea blocks, appendix headings, plus targeted reads of ch03, ch06, ch08, ch14, ch15, ch26, ch28, ch30, ch40, ch41, ch42 and a 50-term coverage grep across the manuscript.

================================================================
1. THE GENUINE DIFFERENTIATOR
================================================================

It exists, it is strong, and it is never claimed.

What it is. The book decomposes any decision into six functions that can each fail separately — notice/interpret, construct options, predict consequences, value consequences, choose/commit/act, observe/learn — and then asks of every phenomenon it introduces: which function did this change? That is a genuinely different move from the field. It converts "bias" from a label into a diagnosis, which is exactly what index.qmd line 36 does with the committee's early favorite ("We might call the result an anchoring effect, a preference for familiarity, or conformity to the chair. The candidate might also have been the strongest applicant"). And because the decomposition is functional rather than topical, one argument can run unbroken from how the visual system resolves an ambiguous image (ch04) to how two firms specify a contract they can both perform (ch38) to what a city owes residents whose street the model deprioritized (ch42). No competitor sustains that.

Three supporting differentiators, all real:

(a) The arc choice -> influence -> agreement (index.qmd line 56: "The book follows an expanding journey: **choice, influence, and agreement**"). Kahneman stops at individual judgment. Cialdini starts at influence and never does judgment. Fisher & Ury / Voss / Stone-Patton-Heen start at the table. Bazerman & Moore is the closest rival on scope but has no perception/predictive-mind front end and no communication-and-repair arc. This book is the only one that earns the transition by making it a widening of the same analysis rather than a change of subject.

(b) The prediction/valuation split as load-bearing structure, not a passing distinction. It is introduced in ch01, given its own vocabulary table in how-to-use, given a chapter each (ch05, ch06), and then it pays off twice: it is the hinge of ch42's AI argument, and it is the tool that lets ch16's rain-forecast worked example show two rational actors choosing oppositely on identical information. Very few decision books can cash a first-chapter distinction that hard at the end.

(c) Evidence discipline as a teachable practice, not a disclaimer. how-to-read-evidence.qmd's six-question audit, Appendix F's evidence-status map, retractions bolded in reference lists, the Ariely-Wertenbroch retraction handled in ch19 with a date and a replication citation, and the ch40 treatment of Mertens et al. (2022) versus the Maier et al. (2022) reanalysis. This is the book's most unusual property in the whole comparison set and it is close to invisible in the front matter.

Would a reader grasp it in the first ten pages? No. The preface is excellent and does not sell. It presents the map, the vocabulary, the ethics, and the arc, and it reaches its end without one sentence a reader could repeat to a colleague explaining why this book and not Thinking, Fast and Slow. The first number and the first named study both arrive in Chapter 1, after roughly 3,000 words of front matter. Compare the positioning moves of the comparison set: Nudge tells you on page one that you are already a choice architect; Kahneman promises you a vocabulary for water-cooler diagnosis of other people's errors; Duke tells you life is poker, not chess. Each is a promise about what the reader will be able to DO. This book's promise ("The decision is already in the making") is beautiful and is about what is true, not about what the reader gains.

Drafted paragraph, to sit immediately after the master-loop figure in index.qmd (after line 26), claiming the method without naming rivals:

  "Most books about decisions choose one lens. Some catalogue the errors that intuition makes; some show how the presentation of a choice steers it; some teach you how to argue, to listen, or to bargain. Each is useful, and none of them alone will explain why a committee that ran a careful process still produced a hire nobody can defend. This book takes a different route. It treats a decision as six things that can each go right or wrong separately — what was noticed, what options existed, what was predicted, what was valued, what was done, and what was learned — and then asks of every finding in the book: which of those six did it change? That question is what makes 'anchoring' a diagnosis instead of a label, and it is what lets a single argument run from how the eye resolves an ambiguous image to how two firms design a contract they can both live with. You will not get a list of biases to memorize. You will get a place to put each one, and a test for whether it is the thing actually going wrong in front of you."

One paragraph, not three pages. It keeps the voice, and it gives the reader the sentence they are currently missing.

================================================================
2. TOPIC GAPS: VERDICT ON EACH
================================================================

I checked all fifteen named candidates plus five of my own. Most are not gaps — the book covers them, often better than the field. Four are real. I say so in both directions.

NOT A GAP — leave alone:

* Emotion/affect as a first-class input. Covered properly and in the right places: ch06 "## Emotion tells the mind what matters" carries integral vs incidental emotion, the somatic-marker hypothesis with its lesion evidence, risk-as-feelings (Loewenstein et al., 2001), the affect heuristic, and Lerner's appraisal-tendency framework with the fear/anger asymmetry; ch08 "## Emotion is part of judgment" gives the working diagnostic ("Emotion can improve the question while still giving the wrong answer"); ch09 handles affect as a substitute for probability; ch22 handles affective forecasting, impact bias, and focalism; ch34 and ch35 handle emotion in conversation and at the table. The only residue is the undefined use of "regret" (filed as a finding).

* Motivated reasoning and identity-protective cognition. ch10 is an entire chapter on it, with Kunda (1990) and Kahan (2013) named and the mechanism stated as a process risk rather than a character flaw; ch07 repeats it; ch06 adds identity-based motivation (Oyserman). Nothing to add.

* Organizational decision processes beyond ch28. This is over-served, not under-served. ch41 (7,460 words) is a full organizational-process chapter — noise audit, structured judgment pipeline, decomposition before evaluation, outside view and reference classes, independence-then-aggregate, meeting design, the decision audit, the decision journal with matched before/after fields. Add ch03's attention-architecture table, ch29's organizational culture audit, ch40's governance section, and Appendix C's Structured Judgment Pipeline. No new chapter.

* Forecasting and superforecasting practice. The substance is complete (ch15 calibration/resolution/Brier/forecast ledger; ch41 outside view, estimate-first-discuss-second, Mellers et al. 2014). Only the vocabulary is missing — filed as a small finding.

* Risk communication and numeracy. ch14 is the strongest short chapter in the book: the two-applicant-pool worked update (1,600/4,000 = 0.40, then 72.7% in a preselected pool), natural frequencies, "## Check your denominator", conjunction/disjunction. how-to-read-evidence adds the 10->12 versus 100->120 worked contrast. ch42 adds display design for uncertainty. At 2,133 words ch14 is the shortest chapter and I considered flagging it — but it is dense, worked, and efficient. Manufacturing a complaint there would be wrong.

* Deep uncertainty and ambiguity. ch16 has the Ellsberg urn as a named section with the preference pattern spelled out; ch18 line 58 defines deep uncertainty and prescribes scenarios and reversible trials (Hertwig & Wulff, 2022). Only "Knightian" is missing as a term for economics readers — one parenthetical.

* Algorithmic aversion and human-AI complementarity. Handled, and handled well: Dietvorst et al. (2015) and automation bias in ch41's Research Lens; Bigman & Gray (2018) vs Logg et al. (2019) presented as a genuine tension in ch42; and, crucially, Goh et al. (2024) — physicians with LLM access scored 76% vs 74% while the LLM alone scored 92% — which is the best available teaching case for why standalone capability is not complementarity. The problem is placement, not coverage (section 4 below).

* Scarcity/poverty and cognitive bandwidth. The book is BETTER than the field here. ch19 line 173 presents Mani et al. (2013) and Mullainathan & Shafir (2013), then states plainly that "the size and generality of this additional cognitive mechanism remain contested" and cites the Carvalho, Meier & Wang (2016) null. That is precisely the integrity the project brief says to preserve.

* Ethics of influence. Not a gap; a strength, and arguably the book's second differentiator. Fifteen chapters carry a named "## Ethics:" section, ch40 runs a ten-dimension audit table, Appendix C collects it, and the recurring standard is stated crisply ("Would the design remain defensible if the people affected understood how it worked, whose goal it served, and how to refuse it?"). The fix is to advertise it in the preface, not to add more of it.

* Expertise and when intuition is trustworthy. ch08 "## When intuition deserves trust" runs Kahneman & Klein (2009)'s three conditions as an operational procedure, and ch41 reapplies them. Complete.

* Sunk cost and escalation of commitment as its own treatment. Distributed on purpose and better for it: ch20 gives the mental-accounting mechanism ("### Close: sunk costs and the pain of closing an account"), ch07 gives the responsibility/self-image route via Staw (1976), and ch23's dollar auction presents competition neglect and escalation as COMPETING explanations that the behavior alone cannot distinguish. A dedicated chapter would flatten that. No change; just confirm the concept index routes the term to all three.

REAL GAPS — four, ranked:

1. ATTENTION ECONOMY AND DIGITAL ENVIRONMENTS. New section inside ch03 (named finding above). Largest gap in the book. ch03 lists a phone notification beside a crying baby as though both were accidents of the environment; "attention economy", "infinite scroll", "recommender" appear zero times in the chapter. The only treatment is ~250 words in ch40 plus a phrase in ch13, and nothing links them. For a 2026 decision book this is more conspicuous than any classical omission, and it is the gap most likely to be noticed by an ordinary reader rather than a specialist.

2. MORAL JUDGMENT. New section inside ch07, plus two cross-links (ch28, ch37). The book runs a demanding ethical practice in fifteen chapters while never describing how moral judgment works — "moral judgment" appears once in 42 chapters, incidentally, inside Entman's framing definition. The asymmetry is real and cheap to close in the chapter that is already about reasons that are not causes.

3. CRISIS AND TIME-PRESSURED DECISIONS. New section inside ch08. Recognition-primed decision making is never described though Klein is cited six times; "time pressure" survives mainly as a table row. ch08 already builds the four diagnostic questions that make RPD's boundary statable, so the section pays off existing apparatus rather than importing new machinery.

4. STRESS, SLEEP, AND STATE EFFECTS. New subsection inside ch41 (not ch06 — the actionable version is a process rule, not a psychology lecture). Smallest of the four. Decision quality is treated as a property of process and environment but never of the decider's current state, which is the cheapest protection available and absent from the chapter about protecting judgment.

================================================================
3. OVER-WEIGHTED CONTENT
================================================================

Little fat, and the manuscript is disciplined. Four observations, in order of confidence:

* ch06 (6,433 words) — the six-sentence anaphora list at line 173 and the 36-line Maslow research note. Recovers ~700 words with no loss; the Maslow material belongs in Appendix B, which exists for exactly the "why a value system exists" question ch06 line 41 explicitly defers. Filed as a finding.

* ch04 (5,112 words) carries three Research Lenses plus a Calibration test. The Shirl Jennings restored-sight lens (lines 185-202) is genuinely beautiful and is a single bounded case; halving it would cost the chapter nothing structural.

* ch29 (4,966 words) runs four numbered "Lens" sections, a worked application, an organizational culture audit, AND a culture-and-identity meaning audit. Three audit instruments in one chapter is one too many; the organizational culture audit (line 250) duplicates work Appendix C already collects.

* Structural rather than cuttable: ch41 + ch42 = 14,581 words, 8.8% of the book in its final two chapters. Both earn their length and I would not cut either — but it means the book's practical payload is back-loaded, which matters for a reader who abandons at Part VI.

Not cuttable but worth stating: the manuscript is remarkably free of padding. There is no chapter I would delete, and the tight chapters (ch14 at 2,133; ch35 at 2,229) are tight because they are efficient, not because they are thin. The one exception is ch28, which is short because it is underwritten (finding above).

================================================================
4. IS THE AI MATERIAL CURRENT, AND IS IT INTEGRATED?
================================================================

CURRENT: yes, and by a wide margin. ch42 carries the Stanford AI Index 2025 inference-price collapse (US$20 -> US$0.07 per million tokens for GPT-3.5-level MMLU performance, Nov 2022 to Oct 2024, >280x); Brynjolfsson et al. (2025) on 5,172 support agents (+15% issues resolved per hour, with heterogeneity noted); the MASAI trial via Gommers et al. (2026) with the randomized interval-cancer analysis reported properly (1.55 vs 1.76 per 1,000, rate ratio 0.88, 95% CI 0.65-1.18, non-inferiority margin named, sensitivity 80.5% vs 73.8%, specificity 98.5% both arms); Goh et al. (2024); NIST (2023) and OECD (2024) for definitions; and the Flint programme with its hit-rate sequence (80% model-guided -> 15% in 2018 -> ~70% after the 2019 settlement) plus a footnote conceding these are successive field phases, not randomized arms. I could not find a stale claim. The chapter also gets the harder thing right: its best teaching case (Goh) is a NEGATIVE result about complementarity, which is the correct lesson and the one most books avoid.

INTEGRATED: no. AI-term density per chapter: ch42 = 73, ch41 = 29, ch04 = 6, ch21/ch01 = 2, ch32/ch15/ch13/ch06 = 1, and zero in the remaining 24 chapters — including every chapter of Parts V and VI. The book that argues AI must be embedded in an existing decision process has quarantined AI in the last two chapters.

Chapters where an AI angle would genuinely add value — the test being that AI changes a mechanism the chapter already teaches, never that AI is topical:

* ch26 (social norms) — HIGHEST VALUE. The chapter's thesis is that agreement is informative only when judgments formed independently. Synthetic accounts and generated reviews break independence at zero marginal cost, which is not a new topic but a limiting case of the chapter's own claim. Currently discussed only in a retired, unbuilt file. ~300 words.

* ch30 (persuasion) — Costello, Pennycook & Rand (2024, Science): personalized LLM dialogue durably reducing conspiracy belief (~20%, persisting at two months) is a direct demonstration of "persuasion is model updating." Filed as a finding. ~400 words.

* ch13 (fluency) and ch32 (message building) — the same mechanism from both sides: machine-generated text raises processing fluency without raising evidential support. ch32 already has "## Fluency: power and danger"; the paragraph closes a loop the book has already opened. ~200 words each.

* ch10 (beliefs that defend themselves) — personalized retrieval as a better toolkit for motivated search; ch10 already argues that greater skill can mean better defence of a prior. ~200 words.

* ch36 (preparing and claiming value) — AI-assisted preparation (reference classes, BATNA estimation, package generation) and the asymmetry when one side has it and the other does not. This is a negotiation fact, not a technology fact. ~300 words.

* ch03 (attention) — recommender systems as the institution that allocates attention; pairs naturally with the attention-economy gap above.

* ch40 (choice architecture) — the dark-patterns paragraph already notes that personalization means "no shared interface for outsiders to inspect." One sentence naming algorithmic personalization as the reason audit is now structurally harder would sharpen it.

Total cost: roughly 1,700 words spread across seven chapters. It would move the book from "has an AI chapter" to "AI is part of the analysis," which is the position the book's own argument requires.

================================================================
5. THE SINGLE STRUCTURAL CHANGE THAT WOULD MOST IMPROVE THE BOOK
================================================================

PROPOSAL: Rebuild Chapter 28 as the book's social-decision keystone — roughly 4,000 words, opening on the hiring committee, with each of its six mechanisms given a named subsection and the field's famous numbers restored — and in the same pass wire parts/applied-interlude.qmd into the build so ch27 (markets) leaves Part IV's spine.

ARGUING FOR IT. Part IV is where the book's promise is most exposed and least delivered. It carries seven chapters, and its opener stakes everything on one scene: a team member stays quiet, "a warning can disappear from the discussion while everyone takes the silence as agreement," and the part asks "how can the team discover which one it needs to address?" The chapter that answers that question is 2,271 words — the third-shortest in a 165,000-word manuscript, shorter than ch41's treatment of meeting design alone — and it answers it with an engineering-safety vignette rather than the hiring committee the preface, how-to-use, and Part I all promise will be there. It carries Milgram, conformity, groupthink, hidden profiles, pluralistic ignorance, and diffusion of responsibility in the space most chapters give to two ideas, which is why the book's already-diagnosed concreteness problem is most acute exactly here: the most famous experiments in the field arrive with no numbers attached. Meanwhile ch27 (markets, 5,076 words) sits in the middle of that part without developing the spine, and the author has already drafted the fix — a complete applied-interlude opener with its own figure and rationale, sitting unwired in both build profiles. Doing both at once turns Part IV from seven chapters with a seam into six chapters with an argument: interdependence, behavioral game theory, cooperation, norms, groups-and-authority, culture — with markets as a clearly-signposted optional application for the finance route the reading-routes table already describes. It also closes the spine's biggest hole, since the committee currently disappears from ch17 through ch25 and from ch27 through ch40, returning only in ch41. Nothing else on my list gives this much return: it fixes the shortest chapter, the thinnest evidence, the broken case continuity, an orphaned file, and an over-long part in a single edit.

ARGUING HONESTLY AGAINST IT. The premise may be wrong in two ways. First, brevity in ch28 may be deliberate rather than negligent: the chapter's existing text is unusually careful about contested ground — it calls groupthink "a familiar but contested umbrella," cites Perry et al. (2020) on variable credibility in Milgram, Haslam & Reicher (2017) on identification as a competing explanation, Burger (2009) on the modified replication, and Fischer et al. (2011) on bystander-effect attenuation in dangerous emergencies. An author who knows this literature that well and still wrote it short may have concluded that the famous studies do not support the weight a longer chapter would place on them — and expanding the chapter, especially by restoring its famous numbers, risks lending those numbers exactly the authority the chapter's hedging was designed to withhold. Second, the interlude move has a real cost the draft opener itself concedes: calling ch27 "optional enough that readers can continue to social interaction without losing the book's causal spine" invites readers to skip it, and markets are the book's only demonstration that individual judgment aggregates into an institution that then feeds back as evidence — the single best illustration of the master loop operating above the individual. Structurally demoting it to protect Part IV's tidiness could cost more than the tidiness is worth. And both halves are the expensive kind of change: a 1,700-word chapter expansion is the largest single writing task in this whole review, at a point in the manuscript's life when the marginal return of one more strong chapter may be lower than the return of the twelve small edits listed above, which together cost about the same and touch twelve chapters instead of two.

MY RESOLUTION: do the ch28 expansion, with the hedges preserved and the numbers presented in the book's own idiom (what was measured, in what condition, with what caveat) rather than as headline facts. Treat the applied-interlude wiring as a separate, cheap decision that should be made either way, since an orphan file in the repo is worse than either outcome.