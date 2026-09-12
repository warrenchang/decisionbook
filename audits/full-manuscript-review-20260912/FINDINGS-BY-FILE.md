# Full manuscript review — findings by file

Generated 2026-09-12. 824 findings across 61 files, produced by a multi-agent read of
every chapter, appendix, part opener, and front-matter file, plus whole-book sweeps for redundancy,
pedagogical apparatus, and positioning. Severity is the reviewer's; a sample was verified by hand
against the source (see REVISION-PLAN.md for which).

**Severity:** high 289, medium 457, low 78

**Dimension:** engagement 193, insight 103, clarity 99, visual 102, structure 105, consistency 100, accuracy 122

---

## `appendices/appendix-a-rational-choice-and-decision-analysis.qmd`  (14 findings)

### [HIGH · accuracy] #opportunity-cost-and-decision-margins

> prompting consumers to consider other uses of money can change purchase decisions

**Problem.** Two problems in one sentence. First, no numbers, though Chapter 2 line 116 has them. Second and more serious: the appendix presents the original 2009 single-study effect with no qualifier, while Chapter 2 line 118 and Appendix F's evidence-status map both carry the meta-analytic correction (Maguire et al., 2023: a meta-analysis of 39 experiments finding a reliable but considerably smaller effect, mainly in hypothetical decisions). A reader who reads the appendix without the chapter gets the pre-2023 version of this finding.

**Edit.** Match the parent chapter: "One hundred fifty students considering a $14.99 DVD bought it 75% of the time when the alternative was 'not buy' and 55% of the time when the alternative read 'keep the $14.99 for other purchases' (Frederick et al., 2009); a meta-analysis of 39 experiments later found the effect reliable but considerably smaller (Maguire et al., 2023)." Add Maguire et al. to this appendix's reference list, and link the sentence to Appendix F's status row so the formal appendix inherits the book's own replication discipline.  *(effort: small)*

### [HIGH · accuracy] #invariance-regularity-and-omitted-variables

> asymmetrically dominated decoy raises the choice share of a target, violating regularity

**Problem.** The attraction effect is stated as an established regularity violation with no magnitude and no boundary condition. Appendix F's evidence-status map covers the jam study and opportunity-cost neglect but contains no row for the attraction effect, and Chapter 11 presents it the same way (line 74) plus a classroom demonstration from Ariely (2008) at @fig-subscription-decoy. So the book's most systematically hedged asset — the replication appendix — silently skips the one decoy-effect literature that has had well-documented replication trouble, and this appendix asserts the effect as a bare fact in a section whose topic is exactly which axioms survive testing.

**Edit.** Add the reported magnitude from the original (Huber, Payne & Puto tested six product categories and reported target share increases of several to roughly fifteen percentage points), then add one boundary sentence: the effect is robust with stylized two-attribute numeric stimuli but has proved fragile with realistic or perceptual stimuli (Frederick, Lee & Baskin, 2014; Yang & Lynn, 2014; see Huber, Payne & Puto, 2014, for the authors' reply). Verify the exact percentages against the 1982 paper before printing them. Consider adding a row to Appendix F's map as well.  *(effort: medium)*

### [HIGH · clarity] #invariance-regularity-and-omitted-variables

> specify or measure $K$, $P$, $u$, and their response to context

**Problem.** By section 4 the reader is being asked to hold K, P, u, z, m, A and V simultaneously, with 𝒜 versus A distinguished only by typeface. The symbols are introduced across four separate sections and never collected. By section 7 a new alphabet arrives (theta, Y, p(y|theta), c(Y)) and by section 9 another (B(a,y), V_0, V_1, G(r), r). Anyone entering at a section other than the first — which is the normal way an appendix is used — must scroll backward to reconstruct the notation.

**Edit.** Add @tbl-appa-notation immediately after section 1, with columns Symbol | Name | What it stands for | First used in. Rows: 𝒜 (all actions under discussion), A (feasible set), K(z,m) (consideration set), ≽ (weak preference), V (value representation), C(A) (choice correspondence), u(o) (value over consequences), P(o|a) (beliefs), z and m (external context, internal state), b*(a) and OC(a) (best forgone alternative, opportunity cost), M(a) (decision margin), w_j and v_j (swing weight, attribute value function), theta and Y (state, signal), EVPI/EVSI/NVSI, B(a,y) (continuation action set), G(r) (net gain from one analysis step). Also state explicitly at first use that 𝒜 is the full menu under discussion and A the feasibility-checked subset, since that typographic distinction carries real load throughout.  *(effort: small)*

### [HIGH · engagement] #invariance-regularity-and-omitted-variables

> descriptions designed to express complementary versions of the same outcome information produced different preferences

**Problem.** The single most famous demonstration that description invariance fails is reported with zero numbers. "Produced different preferences" is the flattest possible rendering of a result whose whole force is the size of the gap. Chapter 1 (line 109) is only marginally better: "surgery was relatively more attractive in the survival frame," also numberless. So the book cites McNeil et al. (1982) twice and never once tells the reader how large the reversal was.

**Edit.** Add the published figures in the same sentence: pooled across the three respondent groups, the share preferring radiation therapy over surgery rose from 18% under the survival framing to 44% under the mortality framing; among physicians the shift was roughly 16% to 50%. Also state the design detail that makes it airtight — the two descriptions were arithmetically complementary (a 10% mortality rate is a 90% survival rate), so nothing about the outcome information changed. One clause, and an abstract axiom violation becomes a number a reader can repeat.  *(effort: small)*

### [HIGH · engagement] # Rational Choice and Decision Analysis

> Suppose one job offer pays more while another leaves more time and flexibility.

**Problem.** The job-offer scenario is the appendix's spine — it returns in sections 1, 3, 6, 7, 8 and 10 — and it never once acquires a number, a name, or a detail. "Pays more" and "more time and flexibility" are the same two abstractions restated six times. Across 3,245 words there is not a single numeral in the running text apart from the stray "0.63 rather than 0.61" at line 375. Every formula is stated and none is instantiated. That is the concreteness gap in its purest form, in the one file where concreteness costs nothing because the math is already there.

**Edit.** Give the two offers figures in the opening paragraph and carry them through: Offer A, a 340-person analytics firm, EUR 78,000, fixed 37-hour weeks, clear promotion ladder; Offer B, an 11-person startup, EUR 95,000 plus equity, unpredictable hours, promotion prospects the candidate puts at about 0.4 over two years. Then section 6's swing weights, section 7's EVPI/EVSI, and section 8's p* and w* all compute against the same running case, and section 10 can close by naming which of those two the analysis actually recommends and what would flip it.  *(effort: large)*

### [HIGH · engagement] #value-of-information

> one short question about flexible hours might reverse the decision

**Problem.** Section 7 is the most useful section in the appendix and the least usable. It defines V_0, V_PI, EVPI, p(y), Bayes' rule, V_Y, EVSI and NVSI across nine display equations and roughly 700 words without a single number. A reader who wants to know whether an extra week of due diligence is worth it gets notation and the instruction that "false positives, false negatives, and other ordinary signal errors belong in the likelihood." The opening promises a concrete payoff — one question reversing a decision — and then the section never performs a reversal.

**Edit.** Work the smallest possible example right after the EVSI equation, roughly 150 words plus a 2x2 payoff table: two states (promotion track / no promotion track) with prior p = 0.4; two actions; payoffs in the same declared units; one imperfect signal with p(y|theta) = 0.8 and 0.3. Show V_0, then V_PI and EVPI, then the posterior after each signal, then V_Y and EVSI, then subtract a stated c(Y) to get NVSI. End with the line that makes it stick: the question is worth asking only because EVSI exceeds its cost, and the same question about an issue that cannot change the choice is worth exactly zero however interesting the answer.  *(effort: medium)*

### [HIGH · visual] #sensitivity-and-robustness

> A precise-looking ranking can conceal a fragile recommendation

**Problem.** The appendix contains zero figures, zero tables, and exactly one callout ("Value scales") across 3,245 words and twenty-nine display equations. That is the longest figure-free and table-free stretch of formal content in the book. Section 8 in particular describes a crossing point, a plausible range, and whether the range straddles the threshold — three things that are trivially drawable and painfully hard to hold in prose.

**Edit.** Add @fig-probability-threshold beside the "Probability threshold" subsection. One panel: x-axis p from 0 to 1; y-axis expected utility; a straight rising line for action a from u(L) at p=0 to u(H) at p=1; a horizontal line at u(c) for action b; their intersection marked and labelled p*; two shaded vertical bands for a plausible range of p, one lying entirely right of p* (labelled "ranking robust — do not buy information") and one straddling it (labelled "information about p may have decision value"). A second small panel repeating the same geometry for w* in the weight-threshold subsection would cover both. This is the single highest-leverage figure addition in the appendix.  *(effort: medium)*

### [MEDIUM · clarity] #sequential-choice-and-reversibility

> Their sum requires a common cardinal, additively separable intertemporal scale

**Problem.** This one paragraph introduces a, y, B(a,y), V_0(a) and V_1(b;a,y), then stacks a cardinality requirement, an additive-separability requirement and a discounting requirement, in about 95 words, all before the equation appears. Five new objects and three scale conditions arrive in a single block, so the reader who stumbles on "additively separable intertemporal scale" loses the definitions that preceded it as well. It is the densest paragraph in the appendix.

**Edit.** Split it. One short paragraph defining the four objects, one sentence each. Then the equation. Then the scale conditions as a two-line bulleted "this expression is meaningful only if" list or a footnote, in the same style as the existing [^appa-additive-utility] footnote, which handles an equally technical caveat far more readably.  *(effort: small)*

### [MEDIUM · insight] #sequential-choice-and-reversibility

> Under this stylized metareasoning rule, conduct the step when $G(r)>0$

**Problem.** "Metareasoning" appears exactly once in the entire 195,000-word manuscript — here — undefined and uncited. Worse, this is the book's formal statement of an idea that Appendix B develops conceptually one file later as resource rationality ("Does the procedure use limited computational resources efficiently for the modeled objective and costs?", @tbl-rationality-standards, citing Lieder & Griffiths, 2020). The book states the same idea twice, in two appendices, in two vocabularies, with no link in either direction. The reader who could most use the connection is exactly the reader of both appendices.

**Edit.** Define the term in a clause ("reasoning about whether to reason further"), cite Russell & Wefald (1991) and Lieder & Griffiths (2020), and add a forward link: "Appendix B places this rule among the standards of rationality as resource rationality, and discusses what follows when the assumed costs and priors change (Rahnev, 2020)." Add the reciprocal backward link from Appendix B's resource-rationality row to this equation. That turns an orphaned equation into the formal backbone of a conceptual table.  *(effort: small)*

### [MEDIUM · structure] #what-formal-analysis-can-and-cannot-establish

> Use the equations to expose an assumption or test a recommendation.

**Problem.** The opening makes a usability promise and the closing section, 3,200 words later, is four sentences and roughly eighty words that restate the promise rather than deliver on it: the analysis "is useful if it reveals an overlooked option, a forecast that deserves checking, or a trade-off hidden inside a single score." Nowhere does the appendix tell the reader what to actually do, in what order, with a live decision. Every chapter in the book closes with a commitment ("Take it forward"); this appendix closes with a summary.

**Edit.** Replace section 10's middle paragraph with a six-step audit the reader runs on one open decision: (1) write A and list the options you excluded, with the constraint that excluded each; (2) name b*(a), the best feasible path this commitment forecloses; (3) split any single score into P and u and say which of the two your disagreement is actually about; (4) compute the p* or w* at which your ranking flips; (5) ask whether any obtainable signal would move you across that threshold, and what it costs; (6) state the scenario set over which the recommendation survives. Then close with the existing two-sentence statement about what formal analysis cannot settle.  *(effort: medium)*

### [MEDIUM · structure] #invariance-regularity-and-omitted-variables

> separate a challenge to an invariant benchmark from a variable omitted by a thin model

**Problem.** The section is titled "Invariance, regularity, and omitted variables" but the omitted-variable idea — arguably the most useful distinction in the section, since it separates "the axiom is wrong" from "your model was too thin" — appears only in the final clause of the final sentence, and is then handed off to Chapters 1 and 2. The section delivers two of the three things its heading promises.

**Edit.** Give it its own short paragraph. The defaults example is already sitting there and is the right vehicle: state formally that if effort, delay, perceived recommendation, or anticipated regret differ between opt-in and opt-out, then the two designs present different consequence vectors, so the observed difference is an omitted variable in the thin model rather than a violation of invariance — and that the test is whether the omitted consequence can be measured independently of the choice it is invoked to explain. Without that test stated, "omitted variable" becomes an unfalsifiable escape hatch, which is the opposite of the section's purpose.  *(effort: small)*

### [MEDIUM · visual] #multiattribute-value

> the importance of moving across the stated range of attribute

**Problem.** The swing-weight point is the most practically consequential idea in section 6 and probably the most commonly botched idea in applied multiattribute scoring: change the attribute range and you change what the weight means. The appendix asserts it and moves on. A reader who has ever built a weighted scoring table will nod without changing anything they do, because nothing here shows the reversal actually happening.

**Edit.** Add a compact table beside this paragraph using the running job offers: three attributes (salary, hours, learning), the declared range for each, v_j at the range endpoints, the swing weight, and each offer's weighted score — computed twice, once with the salary range set to EUR 78,000-95,000 and once with it narrowed to EUR 78,000-82,000. Show the ranking reversing with no change to either offer and no change to anyone's stated priorities. That single demonstration is worth more than the paragraph's three sentences of warning.  *(effort: medium)*

### [LOW · accuracy] #consequences-beliefs-and-expected-utility

> relies on completeness, transitivity, continuity, and independence conditions (von Neumann & Morgenstern, 1944)

**Problem.** Standard textbook shorthand, but historically imprecise in a book that is otherwise unusually careful about attribution. The axiomatic derivation of the expected-utility representation appeared in the appendix added to the 1947 second edition, not in the 1944 first edition, and the independence condition was not stated as a separate axiom by von Neumann and Morgenstern at all — it was identified as implicit in their system and formulated explicitly afterwards (Marschak, 1950; Samuelson, 1952; Malinvaud, 1952).

**Edit.** Cite the second edition (von Neumann & Morgenstern, 1947) for the axiomatization and add a half-clause: "the independence condition was made explicit in later formulations." Two words of change in the reference entry and roughly eight in the text. Cheap, and it matches the standard the manuscript sets elsewhere.  *(effort: small)*

### [LOW · consistency] #feasible-and-consideration-sets

> ## 1. Feasible and consideration sets

**Problem.** Appendix A numbers all ten of its sections; Appendices B and C number none. The numbers also do not appear in Appendix A's own anchor ids (#feasible-and-consideration-sets), and nothing in the appendix or the manuscript ever refers to a numbered section, so the numbering currently buys nothing while breaking the pattern of its two neighbours. Appendix C additionally lacks the italic subtitle line and the epub-guarded anchor block that A and B both carry.

**Edit.** Either drop the numbers, or keep them and start using them — internal pointers such as "the threshold in section 8" and "the notation of section 1" are precisely what a formal appendix needs, and their absence is why finding A7's notation table is necessary in the first place. Whichever way, apply the same convention to Appendices B and C so the three read as one set.  *(effort: small)*

---

## `appendices/appendix-b-evolutionary-explanations-of-value-choice-and-rationality.qmd`  (14 findings)

### [HIGH · engagement] #evolution-explains-not-prescribes

> Gould and Lewontin (1979) warned against treating a plausible adaptive story as sufficient evidence

**Problem.** The most famous methodological critique in evolutionary biology is cited by its conclusion and stripped of the image that made it famous. The word "spandrel" appears nowhere in the body text — only inside the reference-list title — yet the surrounding sentence asks the reader to hold "by-product," "exaptation," "developmental constraint" and "drift" as bare vocabulary. The paper's rhetorical weapons (San Marco, Pangloss, Kipling's just-so stories) are exactly the concrete hooks this abstract paragraph needs, and they are free — the citation is already there.

**Edit.** Add roughly forty words before the warning: the tapering triangular surfaces beneath the dome of San Marco are a geometric by-product of mounting a dome on rounded arches — they have to exist, whatever anyone does with them. Their mosaics were fitted in afterwards. So the beauty of the design explains nothing about why the spaces are there. Then define spandrel as the term for such a by-product, and the four-item list of alternatives that follows stops being vocabulary and becomes a checklist with a picture attached.  *(effort: small)*

### [HIGH · engagement] #rationality-has-more-than-one-benchmark

> Recognition, for example, can help when exposure genuinely covaries with the target

**Problem.** This is the less-is-more effect — the single most counterintuitive published result in the ecological-rationality literature — reduced to a definition of the recognition heuristic. The surprise is that ignorance can beat knowledge, and the sentence as written does not even hint that anything surprising happened. Goldstein and Gigerenzer (2002) is cited; its finding is not reported.

**Edit.** Report it: asked which of two American cities is larger, German students — who had never heard of many of them — performed at least as well as American students who knew them all, because recognition itself carried information the better-informed group could not use as a cue. Give the canonical pair (San Diego versus San Antonio) and the accuracy figures from the paper. Then the following sentence, "mislead when publicity is manufactured," lands as a real boundary condition on a real effect rather than a caveat attached to a definition.  *(effort: small)*

### [HIGH · engagement] #heuristics-tools-and-biases

> apparently excessive alarms **can** be optimal under specified costs and base rates

**Problem.** The sentence promises specified costs and base rates and then specifies none, in a paragraph whose entire point is that a number makes the paradox dissolve. The smoke-detector principle is memorable precisely because the arithmetic is startling and simple, and the appendix bolds "can" — signalling that the conditional matters — while withholding the condition.

**Edit.** Add Nesse's own logic in one worked line: if a response costs a small, recoverable amount and the danger it protects against costs everything, the response is worth making at probabilities far below one percent — so hundreds of false alarms per true detection is the optimum of the system, not its malfunction. Give the cost ratio Nesse uses and the resulting threshold, checked against the 2005 paper. Then add the line the section is one step short of: this reframes the felt experience of anxiety as a system operating at its designed threshold, which is a genuinely different thing from a system that is broken — and it is also why the model cannot by itself tell anyone whether to treat it.  *(effort: small)*

### [HIGH · insight] #rationality-has-more-than-one-benchmark

> Different standards and an evolutionary lens can produce different assessments of one behavior

**Problem.** The caption promises one behaviour assessed under seven standards. The table then delivers seven definitions and seven abstract failure modes, and no behaviour is ever assessed under any of them. The section even opens with the right case — "A quick choice of food might be consistent with a person's preference, sensible given limited time, and unhelpful for a long-term health goal" — covering three of the seven, and then abandons it for a taxonomy.

**Edit.** Run the opening pastry down all seven rows, either as an added column or as a paragraph following the table: coherent with the person's ranking at that moment; epistemically unobjectionable, since nothing false is believed; instrumentally poor against an endorsed health goal; procedurally appropriate, because a trivial reversible choice does not deserve analysis; ecologically a cue that once tracked scarce energy and no longer does; resource-rationally cheap and therefore defensible; and evolutionarily explicable while remaining normatively undecided. Seven verdicts on one pastry, all different, none contradictory. That paragraph is the appendix's thesis — origin is not obligation — demonstrated rather than asserted, and it is currently missing.  *(effort: medium)*

### [HIGH · structure] #four-questions-not-one-cause

> []{#tbl-tinbergen-four-questions}

**Problem.** A bare table anchor with no table under it. The id is cross-referenced nowhere in the manuscript and renders as an empty span in the built output (docs/appendices/appendix-b-evolutionary-explanations-of-value-choice-and-rationality.html line 618). Either a table was deleted and its anchor left behind, or one was planned and never written. Either way the appendix's organizing framework — the four questions the whole file rests on — is delivered as an abstract numbered list, with the pastry reattached only in the paragraph after.

**Edit.** Restore the table rather than delete the anchor, with four rows and four columns: Question | What it asks | The pastry | The evidence that answers it. Mechanism: what is happening now — blood glucose, smell, learned reward signals — answered by physiology and experiment. Ontogeny: how this person came to respond this way — answered by developmental and longitudinal evidence. Function: what recurrent problem such mechanisms may have addressed — answered by comparative, cross-cultural and modelling evidence. Phylogeny: when these capacities arose in the lineage — answered by comparative and phylogenetic evidence. That single table does three jobs at once: it fills the orphan anchor, it attaches the abstract framework to the concrete case in the same eyeful, and it previews @tbl-evolutionary-evidence at the end of the appendix.  *(effort: small)*

### [MEDIUM · accuracy] #four-questions-not-one-cause

> emphasize interaction among development, ecology, inheritance, and culture rather than a one-way chain

**Problem.** Scott-Phillips, Dickins & West (2011) is cited at line 23 in support of the proximate/ultimate grouping and Laland et al. (2011) at line 29 for interactionism, with nothing to signal that these two papers are direct opponents in the same live dispute about whether the dichotomy should be retained at all. A reader who follows both citations expecting complementary sources will find a defence and an attack. This is not a misstatement, but it is a misleading arrangement in a section whose whole purpose is to keep kinds of explanation straight.

**Edit.** Add a clause making the disagreement explicit — "whether the proximate/ultimate line should be redrawn is itself contested: Laland and colleagues (2011) argue that reciprocal causation and niche construction blur it, while Scott-Phillips and colleagues (2011) defend it as indispensable." The disagreement is more interesting than the consensus and costs one sentence, and it demonstrates the appendix's own standard: name the rival account rather than cite past it.  *(effort: small)*

### [MEDIUM · consistency] References cited in this appendix

> Kahneman, D., & Klein, G. (2009). Conditions for intuitive expertise

**Problem.** Seven of the forty-two reference entries break the house format used by the other thirty-five: no italics on journal title and volume, and no DOI. They are Gigerenzer & Gaissmaier (2011), Gigerenzer & Goldstein (1996), Goldstein & Gigerenzer (2002), Haselton & Buss (2000), Kahneman & Klein (2009), Nesse (2005), and Tversky & Kahneman (1974). Kahneman & Klein additionally uses a hyphen in "515-526" where every other entry uses an en dash. In a book that bolds retracted papers in its reference lists, an inconsistently typeset reference list reads as carelessness the manuscript has not earned.

**Edit.** Bring all seven into the house format: italicize journal title and volume number, add DOIs (all seven have them), and replace the hyphen in the Kahneman & Klein page range with an en dash. Worth a grep across the other forty-eight reference lists in the manuscript for the same seven entries, since these look like they were pasted from a common older source.  *(effort: small)*

### [MEDIUM · engagement] #maslow-and-kenrick

> later management writers turned the hierarchy into the now-standard stepped pyramid (Bridgman et al., 2019)

**Problem.** A genuinely surprising debunking — the most reproduced diagram in management education was not drawn by the man it is named after — told with no name, no date, and no publication. "Later management writers" is exactly the vague generalization that kills a surprise, and it also makes the claim uncheckable by a reader who does not chase the citation.

**Edit.** Name and date it: Bridgman and colleagues trace the first published pyramid to Charles McDermid's 1960 article in Business Horizons — seventeen years after Maslow's paper and six years before Maslow's death — and note that Maslow himself never drew one. Then the following sentence about what Maslow actually allowed (partial satisfaction, simultaneous motives, reversals) reads as a restoration of a mangled original rather than a general caution about popularization.  *(effort: small)*

### [MEDIUM · engagement] #population-model-provenance

> success in one tournament and its vulnerability under another mutation–selection process

**Problem.** The Axelrod tournament is invoked as though the reader already knows it, in a sentence whose job is to show that three different success criteria give three different answers. Without the tournament's concrete details the contrast has nothing to bite on, and the Imhof et al. (2007) reversal — which is the interesting half — reads as a bibliographic aside rather than a result.

**Edit.** Two clauses fix it: fourteen programs entered the first round-robin and sixty-two from six countries entered the second; the winner both times was the shortest program submitted, Anatol Rapoport's four-line tit-for-tat. Then state the reversal plainly: under a mutation-selection process rather than a round-robin, win-stay/lose-shift displaces it (Imhof et al., 2007). Same strategy, same payoff matrix, different selection process, opposite verdict — which is precisely the appendix's standing point that a model result is a result about its update rule.  *(effort: small)*

### [MEDIUM · engagement] #maslow-and-kenrick

> found limited support for the fixed ordering and little convincing support

**Problem.** "Limited support" and "little convincing support" tell the reader that something failed without saying what was tested or how it failed — the same flatness problem as the framing and recognition findings. The next sentence, on Tay and Diener, gives "123 countries" but no sample size, so the two central pieces of evidence in the section are one vague verdict and one half-specified design.

**Edit.** Say what failed: factor analyses did not recover five distinct need levels, and longitudinal tests did not show that satisfying one level activated the next — which is the specific prediction the staircase makes and the only one that distinguishes it from a list of needs. Then complete the Tay and Diener specification: Gallup World Poll data collected 2005-2010, roughly 60,000 respondents across 123 countries. A reader can evaluate those sentences; the current ones can only be believed or not.  *(effort: small)*

### [MEDIUM · insight] #evolutionary-mismatch

> The second account needs direct evidence about the cue, mechanism, learning history

**Problem.** The section teaches a rigorous four-part test for mismatch claims, applies element one and two to the notification case, and then declines to supply element four — the predicted consequence — which is the element that makes the hypothesis testable at all. So the section models the discipline it teaches everywhere except at the one point where a reader would want to see it finished. Care shades into evasion.

**Edit.** Run the test to completion on the notification case, marking clearly that the prediction is the author's proposal, not an established finding. Name what a mismatch account predicts that a plain reinforcement account does not — for example, that attentional capture should track the perceived social relevance of the cue rather than the reinforcement schedule, and should weaken when the cue-outcome relation is made explicit to the user — and name the comparison that would separate the two. Showing the test producing a specific, falsifiable prediction teaches the method far better than restating that the evidence is not yet in.  *(effort: medium)*

### [MEDIUM · structure] #evolutionary-valuation-audit

> the person must still decide which consequences to pursue

**Problem.** "What the evolutionary lens changes in a decision" reads as the closing section and is written as one — it returns to the Chapter 6 invitation, runs the audit table, and delivers the appendix's final claim. Then three long collapsed research notes and forty-two reference entries follow it. The appendix's conclusion is therefore buried two-thirds of the way in, and a reader who works straight through finishes on a Schelling implementation note about pseudorandom seeds.

**Edit.** Move "Optional research notes" ahead of "What the evolutionary lens changes in a decision" so the appendix ends on its argument; or leave the order and add a two-sentence close after the notes that returns to the pastry and states the one-line claim the subtitle already promises: explain where a motive came from, then decide separately what to do about it, because the first question never answers the second.  *(effort: small)*

### [MEDIUM · visual] Optional research notes

> Local moves produce more same-group clustering in one seeded teaching simulation.

**Problem.** The appendix's only figure and its best integrative asset are both hidden behind collapse="true". @tbl-bennett-five-breakthroughs links to six chapters and is the closest thing the book has to a single map of how its topics relate to one another; @fig-schelling-emergence is the only image in 5,564 words. A reader who does not expand the optional notes sees an appendix with no figure at all, and roughly 1,900 of the 5,564 words are collapsed by default — about a third of the file, including its three most vivid passages.

**Edit.** Set the Bennett note to collapse="false", or better, lift @tbl-bennett-five-breakthroughs out of the optional notes and place it under the phylogeny question in the four-questions section, where it is literally the answer to "Through what evolutionary history did the relevant capacities arise?" Keep the caveat footnote attached. The Schelling and Sapolsky notes are genuinely optional; the Bennett table is a navigation aid for the whole book and should not be one click away from invisible.  *(effort: small)*

### [LOW · clarity] #maslow-and-kenrick

> He described them as a hierarchy of **relative prepotency**.

**Problem.** A bolded technical term that is used once and never again — not in the two sentences that immediately paraphrase it, not in @tbl-maslow-popular-kenrick, not anywhere else in the manuscript. Bolding signals to the reader that this is a term to retain, and nothing in the appendix ever asks them to retain it.

**Edit.** Either define it inline and then use it — "relative prepotency: the more seriously deprived need is the likelier one to capture attention" — and put "relative prepotency" into the first cell of the Maslow column of @tbl-maslow-popular-kenrick, where it is exactly the property that distinguishes Maslow's actual claim from the pyramid; or drop the bold and the term and keep the paraphrase.  *(effort: small)*

---

## `appendices/appendix-c-portable-course-tools.qmd`  (17 findings)

### [HIGH · clarity] ## Twelve core tools {#twelve-canonical-tools}

> ## Twelve core tools {#twelve-canonical-tools}

**Problem.** The heading and @tbl-canonical-tools promise twelve tools, but the file contains thirty tool callouts. Eighteen are reachable only by scrolling: fifteen of them have no `[]{#tool-...}` anchor span at all (.expectation-loop-map, .bias-redesign-studio, .experience-sample-audit, .intertemporal-most-audit, .mental-accounting-audit, .market-claim-audit, .well-being-measurement-audit, .urge-surf, .model-updating-message, .layered-listening, .negotiation-tactic-diagnostic, .mediation-arbitration, .meso-contingency, .choice-architecture-audit, .classroom-practice-protocols), so nothing in the book can link to them.

**Edit.** Add a second routing table, 'Eighteen specialized extensions', with the same three columns (Decision task / Start with / Inspectable output), and give every tool a `[]{#tool-slug}` anchor so chapters can link directly. Then the appendix's own opening instruction — 'Add another tool only when the first reveals a question it cannot answer' — becomes operable.  *(effort: medium)*

### [HIGH · consistency] #ai-use-record

> Chapter 41 explains the distinction between prediction, valuation, intervention, and responsibility.

**Problem.** Wrong chapter. That four-way distinction is the architecture of Chapter 42, not Chapter 41: Chapter 42 contains "Separate the forecast from the value of its consequences" (#separate-prediction-and-valuation), "Predicting risk does not tell us whom an intervention will help" (#risk-is-not-treatment-benefit), and "Trust, valuation, and responsibility" (#trust-and-responsibility). Chapter 41 contains the minimum AI-use record itself (#minimum-ai-use-record) and a Research Lens on accountable judgment, but not that distinction. A reader sent to Chapter 41 for it will not find it. The sentence is also bare prose while the adjacent AI Decision Canvas box uses a proper link, so the error is invisible to a link checker.

**Edit.** Change to Chapter 42 and make it a link to #separate-prediction-and-valuation. While in this box, add the missing backward link on its source: the Minimum AI-Use Record is a distillation of Chapter 41's #minimum-ai-use-record and should point there, exactly as the One-Page Decision Journal points to Chapter 41's #what-a-decision-journal-is.  *(effort: small)*

### [HIGH · engagement] #tool-one-page-decision-journal

> The right-hand entry must answer the left-hand entry on the same row.

**Problem.** Thirty tools, 3,732 words, and not one filled-in example anywhere in the appendix. The flagship tool specifies seven row labels across two columns and never shows a single completed cell, so phrases like "resolvable forecasts with horizons" and "continue–stop–scale–revise thresholds" have to be decoded rather than imitated. Chapter 41 already contains a worked instance at #decision-journal-example and this box does not link to it — it links only to #what-a-decision-journal-is.

**Edit.** At minimum, link to Chapter 41's #decision-journal-example from this box. Better, inline a compact filled example directly beneath the table: one dated, ordinary decision with three of the seven rows completed in both columns — a real forecast with a real horizon and probability, a real threshold, and the matching after-the-outcome entry — so the reader can see what "the right-hand entry must answer the left-hand entry" looks like as text. One exemplar calibrates all thirty tools; thirty sets of instructions with no exemplar calibrate none.  *(effort: medium)*

### [HIGH · structure] #choose-a-tool-in-thirty-seconds

> A low-stakes, reversible decision with one visible weakness

**Problem.** @tbl-tool-levels defines three levels — Quick check, Core tool, Specialized extension — and then not one of the appendix's thirty tools is tagged with any of them. The strings "quick check" and "specialized extension" appear nowhere else in the file. So the reader is given a routing taxonomy and no route: a reader with fifteen minutes cannot tell that the Attention Audit is a five-minute diagnosis and the One-Page Decision Journal is a page-length record with a scheduled review, because both are presented as identical grey boxes of instructions.

**Edit.** Tag every callout title with its level and an approximate time: "Attention Audit — quick check, about 5 minutes"; "One-Page Decision Journal — core tool, about 40 minutes plus a scheduled review"; "Market Claim Audit — specialized extension." Thirty small title edits. If that is not wanted, delete @tbl-tool-levels, because as it stands the table teaches a vocabulary the appendix never speaks.  *(effort: medium)*

### [HIGH · structure] #twelve-canonical-tools

> Follow the tool link to its instructions; the final column tells you what to produce.

**Problem.** @tbl-canonical-tools routes to twelve tools and names no chapter for any of them. Across the whole appendix only two of thirty tools link to the chapter that justifies them (the journal to Chapter 41, the AI canvas to Chapter 42). Meanwhile only three files in the entire manuscript link into this appendix. So the book's practical apparatus and the evidence that earns it are almost completely disconnected in both directions: a reader who wants to know why the Heuristic Detector asks what it asks has no path back, and a reader finishing Chapter 16 is never told a Risky-Choice Audit exists.

**Edit.** Add a fourth column, "Where the evidence is," linking each of the twelve: Attention Audit to Chapter 3, Heuristic Detector to Chapters 8 and 9, Probability Judgment Audit to Chapter 14, Risky-Choice Audit to Chapters 16 and 17, Strategic Interdependence Map to Chapter 23, Behavior Redesign Canvas to Chapter 39, Verified Understanding Loop to Chapter 33, Negotiation Preparation to Chapter 36, Structured Judgment Pipeline and One-Page Decision Journal to Chapter 41, Decision Audit Studio to Chapter 41, Prediction–Valuation Split to Chapter 42. Then add the reciprocal pointer from each of those chapters' "Take it forward" sections, which is where a reader who has just finished the argument is most likely to want the worksheet.  *(effort: medium)*

### [HIGH · structure] Social and strategic decisions

> ## Social and strategic decisions

**Problem.** This section has no routing sentence — every other section in the appendix has one — and contains exactly one tool, while "Probability, risk, time, and well-being" contains seven. It nominally covers Chapters 23 through 29: strategic interdependence, behavioral game theory, cooperation and social preferences, social norms and conformity, markets and bubbles, authority and groupthink, culture and identity. Six of those seven chapters get no worksheet at all, and they include the book's most immediately actionable material — how to tell whether a norm message is advertising the wrong behaviour, and what makes a dissenting view cheap enough to voice.

**Edit.** Add a one-sentence routing intro like every other section, and add at least two tools. A Norm and Social-Proof Audit: what behaviour is actually common here, what is the reference group, which behaviour does the message make salient, and is the message advertising the undesirable behaviour as normal (Chapter 26). A Dissent and Authority Check: who in this room can say no, at what cost, who spoke first, what would have to change for the objection to be cheaper to voice, and who is accountable if it is not (Chapter 28). Both map directly onto existing chapter content and both fit the appendix's existing format of four or five prompts plus a stated output.  *(effort: medium)*

### [HIGH · structure] ## Twelve core tools

> | **Quick check** | A low-stakes, reversible decision with one visible weakness |

**Problem.** Thirty of the roughly thirty-five one-off classes live in this single file — they are not scattered chapter improvisations but the 30 entries of this appendix, each given a unique class only so it can be anchored. The file already declares the right taxonomy in @tbl-tool-levels (Quick check / Core tool / Specialized extension) and a canonical twelve, then renders all 30 identically, so the routing table is the only way to tell a core tool from an extension.

**Edit.** Collapse all 30 to one class with three modifiers: .tool--core (the 12 in @tbl-canonical-tools), .tool--quick (.layered-listening, .urge-surf), .tool--extension (the remaining 14). Render the level: 5px solid teal border + 'CORE TOOL' badge; 3px solid + 'QUICK CHECK'; 3px dashed + 'EXTENSION' + collapse=true. The appendix then self-routes and the 30-box wall becomes scannable.  *(effort: medium)*

### [HIGH · visual] #tool-one-page-decision-journal

> ::: {.callout-note .one-page-decision-journal icon=false}

**Problem.** All thirty callouts in this appendix use one-off classes with no rule in quarto-custom.scss, which styles only .core-idea, .activity, .research-lens and .evidence-and-boundary-conditions. So a 40-word urge-observation exercise, a seven-row page-length journal, a seven-row bargaining-tactics table and a six-question ethical audit all render as identical grey boxes for roughly ten screens with no visual hierarchy of any kind. This is the highest-density callout page in the book and the one where differentiation would do the most work.

**Edit.** Reuse .activity (which already has a border colour) for the short exercises, and add one .tool rule in quarto-custom.scss for the twelve core tools — a distinct left border and a slightly heavier title is enough. If the level tagging from the previous finding is adopted, key three rules to the three levels instead, so the visual weight of each box states its cost before the reader reads a word. Roughly fifteen lines of SCSS plus thirty class swaps.  *(effort: medium)*

### [MEDIUM · accuracy] Persuasion, communication, and connection

> For a short message, use **AND–BUT–THEREFORE**

**Problem.** The appendix has no reference list and attributes none of the named, attributable frameworks it teaches: the ABT structure (Randy Olson), BATNA (Fisher & Ury), multiple equivalent simultaneous offers (Medvec & Galinsky), the urge-observation exercise (Marlatt's relapse-prevention work), the Brier score (Brier, 1950). In a manuscript that bolds retractions in its reference lists and devotes an entire appendix to failed replications, an appendix that names five borrowed frameworks and credits none of them is conspicuously out of character — and it is the file most likely to be photocopied and handed out on its own.

**Edit.** Either add a short "Where these tools come from" list at the end of the appendix — one line per named framework with its source — or attach the source chapter to each tool, which the source-chapter column proposed above would largely accomplish for the twelve core tools, leaving only four or five direct attributions to add by hand.  *(effort: small)*

### [MEDIUM · clarity] #tool-probability-judgment-audit

> the Brier score is $(p-y)^2$, where $p$ is the forecast probability

**Problem.** Two problems in the appendix's only formula. First, no benchmark: a reader who computes 0.19 has no way to tell whether that is good, bad, or meaningless. Second, the instruction "score the same event" implies a single event suffices, but one squared error is almost pure noise — a confident correct call and a confident wrong call on one question say nothing about calibration. The formula is also buried at the end of a six-sentence block that already covers reference classes, natural frequencies, conjunctions and overlap.

**Edit.** Add the benchmark in the same sentence: lower is better, 0 is perfect, 1 is maximally wrong, and always forecasting 50% yields 0.25 — so a score above 0.25 means the forecasts are doing worse than a coin flip announced in advance. Then add the averaging requirement: score at least ten resolved forecasts before reading anything into the number. Consider pulling the scoring instruction into its own short paragraph so it is not the tail of an already-dense block.  *(effort: small)*

### [MEDIUM · clarity] #tbl-tactic-diagnostic

> Bogey—falsely presenting a low-priority issue as crucial—false scarcity, or a fake bottom line

**Problem.** Three distinct tactics are compressed into a single table cell with an em-dash definition interpolated in the middle of the list, so the row's grammar breaks and the parallel structure that every other row maintains (one named move, one signal, one response) collapses exactly where the table should be easiest to scan. The row's response column then has to cover all three at once, which is why it reads as a list of generic advice.

**Edit.** Split into three rows — Bogey; False scarcity; Fake bottom line — each with its own signal and its own disciplined response, and move the bogey definition into the middle column where the other rows put their explanations. If space is a concern, give Bogey its own row with the definition in column two and fold false scarcity and the fake bottom line into one row about unverifiable constraint claims.  *(effort: small)*

### [MEDIUM · consistency] Negotiation

> A **mediator** helps parties seek a voluntary agreement and ordinarily does not impose the result.

**Problem.** Every other callout in this appendix ends with something the reader produces — a record, a completed sentence, a map, a next action. This one ends with definitions and never asks the reader to do anything, which makes it a glossary entry sitting inside a tools appendix. Its own final sentence already names four things the reader must establish before choosing a process, so the tool is present in the text and simply not formatted as one.

**Edit.** Convert the final sentence into a four-line record the reader fills in before choosing a process: the neutral's authority (advisory or binding), who bears the cost, what is confidential and from whom, and whether the decision can be reviewed or appealed. Keep the definitions as the lead-in. Same word count, and the box joins the rest of the appendix.  *(effort: small)*

### [MEDIUM · consistency] Classroom extensions

> Assign an activity that serves the learning objective.

**Problem.** The appendix opens addressing an individual reader with a live decision — "Choose a tool for a decision you are working on" — and closes, with no transition whatsoever, by instructing an instructor to assign activities to a class. Reader-facing "you" becomes instructor-facing "you" between one heading and the next. The book has a separate front-matter file (how-to-use-this-book.qmd) where instructors are otherwise addressed, so a reader who has not opened that file has no idea who is being spoken to here.

**Edit.** Mark the switch in one sentence at the top of the section: "The remaining protocols are written for instructors running these ideas with a group; an individual reader can still use the debrief questions alone." Cross-link how-to-use-this-book.qmd. Also reconcile the appendix's heading, "Portable Tools," with its filename and both aliases, which say "portable course tools" — the heading dropped the word that explains why a classroom section is here at all.  *(effort: small)*

### [MEDIUM · consistency] @tbl-canonical-tools, Twelve tools table

> | Redesign an organizational decision | [Structured Judgment Pipeline]

**Problem.** how-to-use-this-book.qmd devotes a whole section to 'Use one recurring ethical audit' and links to Appendix C's Ethical Audit as the tool to apply to every message, intervention and agreement. But the Ethical Audit is not in @tbl-canonical-tools' twelve, so the one tool the front matter says to run every time is absent from the routing table a reader consults to choose a tool.

**Edit.** Add a thirteenth row: 'Check who benefits, who bears the cost, and who can refuse | Ethical Audit | Six answered questions plus the named authority to pause, correct, or end the intervention', and retitle the section 'Thirteen core tools'. Alternatively keep twelve and place the Ethical Audit above the table as a standing requirement, which matches how the front matter treats it.  *(effort: small)*

### [MEDIUM · insight] #tool-one-page-decision-journal

> Remember the rhythm: **freeze → compare → update**.

**Problem.** This is the most memorable formulation in a 3,732-word appendix and it is buried in a note beneath a seven-row table, scoped to one tool. It is in fact the organizing logic of at least four of the twelve core tools — the journal, the Decision Audit Studio, the Behavior Redesign Canvas, and the Structured Judgment Pipeline all freeze something before the outcome, compare it after, and change one thing as a result. The appendix currently has no stated through-line; it has one and does not use it.

**Edit.** Promote the rhythm into the appendix's opening paragraph as the idea that explains why worksheets help at all — the point of a record is that it cannot be revised after the outcome is known, which is exactly what memory does automatically. Then mark which tools follow the freeze/compare/update pattern, in the table or in each title. That single move gives the appendix an argument rather than an inventory, and it directly answers the opening's own question about why recognizing a bias afterwards does not prevent repeating it.  *(effort: small)*

### [MEDIUM · structure] #choose-a-tool-in-thirty-seconds

> Add another tool only when the first reveals a question it cannot answer.

**Problem.** The routing section is anchored #choose-a-tool-in-thirty-seconds, names two tools by hand, and points to a table of twelve. The appendix actually contains thirty callouts. The other eighteen — Expectation Loop Map, Bias Redesign Studio, Experience-Sample Audit, Intertemporal MOST Audit, Mental-Accounting Audit, Market Claim Audit, Well-Being Measurement Audit, One-Minute Urge Observation, Model-Updating Message, Layered Listening, Tactic Diagnostic, Mediation and Arbitration, Package and Contingency Worksheet, Choice-Architecture Audit, Minimum AI-Use Record, AI Decision Canvas, Ethical Audit, and the classroom protocols — are discoverable only by scrolling the whole file, which is exactly what a thirty-second routing section exists to prevent. Several of them (Ethical Audit, Choice-Architecture Audit, Mental-Accounting Audit) are among the appendix's strongest.

**Edit.** Add a second table of specialized extensions immediately after @tbl-canonical-tools, keyed to the question each one answers — "Am I judging this fund's returns or the story about them?" to Market Claim Audit; "Who bears the cost of this design?" to Ethical Audit; "Is this budget line protecting a goal or just a label?" to Mental-Accounting Audit. Question-first routing matches how a reader with a live problem actually searches, and it is the same device @tbl-canonical-tools already uses successfully in its first column.  *(effort: medium)*

### [LOW · structure] Persuasion, communication, and connection

> Use the Verified Understanding Loop when people may be interpreting the same words differently.

**Problem.** The routing sentence leads the section with the Verified Understanding Loop, which then appears third, behind Model-Updating Message and Layered Listening. The negotiation section gets this right ("Begin with Negotiation Preparation" and it appears first), so the inconsistency is internal to the file. A reader following the instruction scrolls past two other tools to find the one they were sent to.

**Edit.** Move the Verified Understanding Loop to the head of the section to match the routing sentence, or rewrite the sentence to describe the actual order. Also note an apparent orphan: lines 169-171 contain a double blank gap between the Market Claim Audit and the Well-Being Measurement Audit, which looks like a removed tool — worth checking against git history in case something was deleted by accident.  *(effort: small)*

---

## `appendices/appendix-d-index-of-major-course-examples.qmd`  (13 findings)

### [HIGH · insight] @tbl-extended-example-index, Chapter 26 row (line 61) and ~7 sibling rows

> The quiet hiring committee, Asch lines, and hotel towels

**Problem.** The index lists at least seven cases whose headline claim Appendix F has revised — the honesty box (Ch. 25), the hot hand (Ch. 15), the Ten Commandments result inside Ch. 7, ego depletion (Ch. 39), the jam study (Chs. 2 and 40), the marshmallow test (Ch. 19), stereotype threat (Ch. 5) — and marks none of them. An instructor picking a teaching case from this table can land on a finding the book itself has retired two appendices later. Appendix D never mentions Appendix E or F at all.

**Edit.** Add an 'Evidence status' column (or a dagger marker) that links each affected row to its entry in Appendix F's map at appendix-f-when-evidence-breaks.qmd#famous-findings-after-replication, and add one line under the intro: 'Entries marked † have a later status recorded in Appendix F; check it before teaching the case.' This turns the index from a finding aid into the book's most persuasive demonstration that it tracks its own evidence.  *(effort: medium)*

### [HIGH · structure] Second sentence of the intro (line 9), defining the third column of @tbl-extended-example-index

> **Evidence role** identifies the kind of example or study.

**Problem.** The gloss is circular, and the column it defines then carries roughly 25 non-parallel labels: 'Recurring worked case', 'Fictional worked decision', 'Controlled hypothetical treatment-choice study', 'Business anecdote used as a causal-inference exercise', 'Reported practitioner case with altered identifying details', 'Field deployment evidence and separately identified policy simulations'. A reader scanning 54 rows cannot tell which cases rest on evidence and which are teaching fiction — which is exactly the distinction this book's scientific integrity rests on, and exactly what a reader would come to this appendix to resolve.

**Edit.** Replace the gloss with a five-tier legend printed above the table — Fictional illustration / Demonstration / Controlled experiment / Field or observational study / Meta-analysis or coordinated replication — and open every Evidence role cell with one of those five labels, keeping the existing prose description after an em dash. The compound rows then read 'Fictional illustration + controlled experiment — fictional scene alongside laboratory studies', which is both honest and scannable.  *(effort: medium)*

### [HIGH · structure] Caption of @tbl-extended-example-index (line 84)

> Extended index of examples, their mechanisms, evidential roles, and primary chapter homes.

**Problem.** The index claims to cover the book's major examples but contains zero rows for power posing, the marshmallow test, the jam study, pen-in-mouth facial feedback, elderly-word priming, money priming, or the Ten Commandments study — I grepped and none of those strings appears in this file. All are named and worked in Appendix F, and all are cases a reader is far more likely to remember by situation than by concept, which is this appendix's stated entry point. Appendices A, B, C, E and F contribute no rows whatsoever.

**Edit.** Add an appendix block to @tbl-extended-example-index (or a fourth table, 'Examples in the appendices') covering every named case in Appendix F's two maps plus Appendix E's simulated clinic reminder study, with the same five columns and a home link to the appendix section. Roughly 20 rows, and they are the rows most likely to be searched.  *(effort: medium)*

### [MEDIUM · accuracy] ## Linked video cases, Reward prediction error row

> | Reward prediction error | Ch. 21 |

**Problem.** The video table and the chapters have drifted apart in three ways. (1) Two rows assign videos to Ch. 21 — the Schultz dopamine clip and the Skinner clip — but the only live chapter containing those links is Chapter 39; the other file holding them is chapters/retired-wanting-craving-and-self-control.qmd. (2) Twelve of the table's 24 links appear in no chapter at all. (3) Six videos embedded in chapters are absent from the table, so they carry no viewing question and no owner: the Princess Bride goblet scene (ch24), the Dark Knight ferry dilemma (ch25), Golden Balls and the ultimatum scene (ch25), and A Beautiful Mind (ch23).

**Edit.** Repoint the two Ch. 21 rows to Ch. 39. Add six rows for the missing chapter videos with viewing questions in the existing style — ch24: 'At which step does recursive reasoning stop adding information?'; ch25 ferry: 'Reconstruct the payoff ranking: does defection actually dominate?'; ch23: 'Which player's best response changes once the others are fixed?'. For the twelve orphan links, either place them in a chapter or move them to an 'Additional clips' block so the table's 'Primary owner' column stays truthful.  *(effort: medium)*

### [MEDIUM · consistency] @tbl-recurring-case-map, 'Hiring and selection' row (line 17)

> Chapter 41 brings these questions into a reviewable hiring process.

**Problem.** The recurring case map names chapters 1, 2, 18, 19, 20, 33, 34, 35–38, 39, 40 and 41 in plain prose with no hyperlinks, while every chapter mention in @tbl-extended-example-index directly below is a working link. The map is the appendix's first table and the one that most invites jumping between chapters, so it is the worst place to make the reader scroll and search.

**Edit.** Link every chapter mention in @tbl-recurring-case-map to its chapter file, matching the link style already used in the extended index.  *(effort: small)*

### [MEDIUM · consistency] @tbl-linked-video-cases, row 10 of 23 (line 101)

> Vivid framing in debate | Ch. 12

**Problem.** The video table is not ordered by chapter. The sequence of the Primary owner column runs 3, 3, 3, 10, 13, 26, 26, 30, 30, 12, 31, 35, 36, 37, 36, 36, 33, 37, 34, 21, 21, 39, 39 — the Ch. 12 row sits between two Ch. 30 rows, and the Ch. 36 rows are split by intervening Ch. 33 and Ch. 37 rows. As a course-prep table its main use is 'what clip goes with this week', and that use is defeated.

**Edit.** Sort the rows by chapter number ascending. If the current order encodes something (thematic grouping), say so in the intro sentence; otherwise sort.  *(effort: small)*

### [MEDIUM · consistency] Table id on line 84; same issue on lines 23 and 116

> {#tbl-extended-example-index}

**Problem.** All three tables here carry Quarto cross-reference ids, and nothing in the manuscript uses them — no @tbl-extended-example-index, @tbl-recurring-case-map or @tbl-linked-video-cases anywhere, including in this file's own prose. The same is true of all ten table ids in Appendices E and F. Quarto numbers the tables anyway, so the reader sees 'Table D.2' with no sentence that ever says 'Table D.2'.

**Edit.** Reference each table from the sentence that introduces it ('@tbl-recurring-case-map shows five cases that return…'), and point how-to-use-this-book.qmd line 77 at @tbl-extended-example-index rather than at the appendix as a whole. Apply the same pass to the ten table ids in Appendices E and F.  *(effort: small)*

### [MEDIUM · engagement] Opening line, immediately under '# Index of Major Examples' (line 9)

> Find a case here when you remember the situation more readily than the concept.

**Problem.** The whole value proposition is compressed into one abstract instruction, and the lookup is never demonstrated. The reader is told what the appendix is for but never shown it working, so the three tables arrive without a reason to trust them or a habit for using them.

**Edit.** Add three sentences after this line that walk one lookup end to end: 'You remember an eye poster above a coffee-room honesty box but not the phrase artificial surveillance cue. The extended index sends you to Chapter 25 for the mechanism; Appendix F tells you that two later meta-analyses found no reliable overall effect. The case is still worth teaching — but as an evidence-updating case, not as a nudge.' Then say in one sentence what each of the three tables is for.  *(effort: small)*

### [MEDIUM · engagement] @tbl-extended-example-index, Chapter 17 row (line 52); same pattern in the Ch. 1, Ch. 7 and Ch. 12 rows

> Outbreak programmes described as lives saved or lost

**Problem.** This is the Asian disease problem (Tversky & Kahneman, 1981), the most-cited framing demonstration in the field, and neither its usual name nor its authors appear anywhere in the row. The same holds for 'Survival versus mortality' (McNeil et al., 1982), 'the dull-task payment study' (Festinger & Carlsmith, 1959) and 'Swapped faces and tastes' (Johansson et al., 2005). An index is only as good as the terms it contains, and these are not the terms a reader holds in memory. Other rows already do this well — 'Allais, Ellsberg', 'Monty Hall', 'Linda', 'Palm/3Com', 'MASAI'.

**Edit.** Append the canonical label in parentheses to each such row: 'Outbreak programmes described as lives saved or lost (Asian disease problem; Tversky & Kahneman, 1981)'. Roughly eight rows need it, and the fix costs a phrase each.  *(effort: small)*

### [MEDIUM · engagement] Intro paragraph to the video table (line 88)

> If a link is unavailable, the question can guide a replacement scene

**Problem.** The contingency plan is good, but it cannot be executed, because the link labels identify nothing: 'Awareness example 1', 'Awareness example 2', 'Kosta scene', 'Silence example', 'Confirmation-bias example', 'Win–win illustration'. If a YouTube link rots — which the sentence anticipates — the reader cannot search for the same clip, because neither its title nor its creator is recorded. The rows that do name a source ('B. F. Skinner Foundation demonstration', 'Wolfram Schultz explanation', 'Gabriele Oettingen explanation', 'Michael Scott negotiation') show what the rest should look like.

**Edit.** Give every row the clip's actual title, creator and approximate runtime, e.g. 'Simons & Chabris selective-attention test (1:21)'. That also lets a reader judge whether a 12-minute talk fits the class before opening it. Also add the anchor link promised in the next sentence: Appendix C's matching passage is an unlabelled bold run-in, '**Case or video debrief.**' (appendix-c-portable-course-tools.qmd line 348), with no id to link to — give it one and link it here.  *(effort: small)*

### [MEDIUM · insight] Line above @tbl-recurring-case-map (line 13)

> When a case returns, look for the new question it helps answer.

**Problem.** The instruction is right and the table then lists chapters without naming the transformation the instruction promises. The genuinely interesting claim — that the same situation changes analytic identity as the book proceeds, so that the hiring case moves from 'what did I notice?' to 'what did the group do to my judgment?' to 'what does the dated record show?' — is left for the reader to infer from a column of chapter numbers.

**Edit.** Add one paragraph after @tbl-recurring-case-map naming the arc each recurring case traces (perception and evidence → social and strategic → process and environment design), and note that a case is reused precisely when the same facts admit a new analytical layer. Two or three sentences convert a lookup table into the book's argument in miniature.  *(effort: small)*

### [MEDIUM · visual] Header row of @tbl-extended-example-index (line 27)

> | Example | Mechanism | Evidence role | Chapter | Application domain |

**Problem.** Five prose columns across 54 rows makes this the book's heaviest table, and it buries the Chapter column — the one thing a reader came here for — in position four, where horizontal scrolling on a phone hides it first. 'Application domain' is the least load-bearing column and consumes the width that pushes Chapter off-screen.

**Edit.** Move Chapter to column one, fold Application domain into the Mechanism cell as a trailing italic tag, and wrap the table in a scroll container with a sticky first column. Three columns plus a sticky chapter link makes the table usable on the device most students will read it on.  *(effort: medium)*

### [LOW · clarity] @tbl-recurring-case-map, rows 1 and 4 (lines 17 and 20)

> Chapter 2 widens the alternatives and makes the trade-offs visible.

**Problem.** Chapter 2 appears in two recurring-case rows describing two different decision-makers. In 'Hiring and selection' it widens the alternatives (the employer's problem); in 'Employment or service agreement' it 'treats accepting an offer as one option among several possible actions' (the candidate's problem). The extended index resolves it — Chapter 2's case is 'Two job offers' — but the map reads as though one chapter sits on both sides of the table without acknowledging the switch.

**Edit.** Make the switch explicit and use it: 'Chapter 2 takes the candidate's side of the same encounter, which is why the alternatives it widens are not the ones the committee sees.' The perspective flip is itself a teachable point about whose alternatives get constructed.  *(effort: small)*

---

## `appendices/appendix-e-how-behavioral-evidence-is-built.qmd`  (14 findings)

### [HIGH · clarity] @tbl-experimental-workflow, Phase 1 row (line 21); term recurs on lines 200, 341, 364, 330

> define the construct, outcome, comparison, population, and estimand

**Problem.** 'Estimand' carries the appendix's central argument — it appears in the workflow table, in section 8 ('Each changes the estimand'), as a design-card field, in the worked study, and in the closing line 'states the estimand and scope before the interpretation' — and it is never defined. Every other load-bearing term gets a bold definition: construct, operationalization, reliability, validity, counterfactual problem, confounding, random sampling, random assignment, rerandomization, ITT, LATE, Type S and Type M, internal and external validity. The one term a reader most needs in order to use the design card is the one left to inference.

**Edit.** Define it at first use in section 1, in the same bold style as its siblings: '**Estimand**: the quantity the study is trying to estimate, named before any estimator is chosen — for the clinic, the effect of assignment to the new reminder on attendance within thirty days among eligible patients. The estimator is how you compute it; the estimand is what you meant.' The estimand/estimator distinction is also never drawn and belongs in the same two sentences.  *(effort: small)*

### [HIGH · engagement] Opening scenario (line 11) and throughout

> A clinic introduces a shorter appointment reminder, and attendance rises.

**Problem.** In 5,200 words this appendix does not walk through a single real study. Every illustration is invented — the clinic, the job-placement program, the scale that reads the same number, the neighboring clinic — and all eleven sources are methodological. The book's other 42 chapters are dense with named studies; the appendix that teaches how those studies are built contains none of them, so the abstractions never touch the evidence the reader has just spent the book absorbing, and @tbl-evidence-designs' six rows stay purely definitional.

**Edit.** Name one study from the book beside each row of @tbl-evidence-designs: laboratory experiment → Asch (1956), Ch. 26; field experiment → Goldstein et al. (2008) towel signs, Ch. 26; randomized experiment in a live workflow → the MASAI screening trial, Ch. 42; observational → the healthcare-cost algorithm audit, Ch. 42; natural/quasi-experiment → a case from Ch. 27's event studies; simulation → Appendix F's selected-literature simulation. Then add one `.research-lens` callout running a single real study (Goldstein et al. is short, field-based, and already in the book) through all five phases of @tbl-experimental-workflow, so the workflow is seen doing work once before the simulated clinic study arrives.  *(effort: medium)*

### [HIGH · insight] Worked study, paragraph reporting the result (line 391)

> The estimated ITT difference is **6.2 percentage points**

**Problem.** The generator sets control p = 0.65 and treatment p = 0.70 — a true effect of 5.0 percentage points — and the text never says so. I ran the snippet: it reproduces the reported 380/600 and 417/600 exactly, so the numbers are right, but the reader can only discover the true value by reading the Python. Appendix F's parallel simulation states its true effect up front ('true effect 0.20 standard deviations') and builds its whole lesson on the gap between truth and estimate. Here the gap is present (5.0 true, 6.2 estimated) and thrown away.

**Edit.** State the true effect before the estimate: 'The generator's true effect is 5.0 percentage points. The study estimated 6.2, with an interval from 0.8 to 11.5. That gap is not an error — it is what sampling variation at this sample size looks like, and it is why the interval, not the point estimate, is the result.' One sentence turns a reproducibility demo into the appendix's clearest teaching moment.  *(effort: small)*

### [HIGH · insight] Section 7, 'Plan precision before collecting outcomes' (line 175), against the worked study (lines 356-393)

> A study needs enough precision to distinguish effects that would lead to different decisions.

**Problem.** The worked study breaks the rule this section states, and the appendix does not notice. With 600 per arm and baseline attendance of 0.65, the minimum detectable effect at 80% power is about 7.6 percentage points, and power against the generator's own 5.0-point true effect is about 46% — a coin flip. Section 7 demands that a defensible design calculation declare the smallest effect of substantive interest, the plausible range, and the variance; @tbl-worked-reminder-design declares none of them and has no Precision row at all. The result: the appendix's only worked example is an underpowered study whose significant estimate overshoots the truth by 24%, which is precisely the Type M pattern section 7 and Appendix F both describe.

**Edit.** Do not fix the design — exploit it. Add the design calculation to the worked table, then add one short paragraph after the estimate: 'Note what this study could and could not distinguish. At 600 per arm it had about a 46% chance of detecting its own 5-point effect, and the smallest effect it could reliably detect was about 7.6 points. Conditional on clearing the threshold, the estimate landed at 6.2 — above the truth. This is the magnitude error Appendix F simulates, produced here by a study we designed ourselves.' Then link to Appendix F's winner's-curse section. This is the single highest-value addition available in this file.  *(effort: medium)*

### [HIGH · structure] Header row of @tbl-worked-reminder-design (line 358), compared with @tbl-evidence-design-card (lines 334-348)

> | Design-card field | Declared choice |

**Problem.** The column is labelled 'Design-card field' but does not use the design card's fields. The card has twelve (Question, Claim family, Construct, Measure, Assignment/comparison, Estimand, Threats, Precision, Analysis, Ethics, Reproducibility, Transport); the worked table has eight, silently drops Claim family, Construct, Measure, Precision, Analysis, Ethics, Reproducibility and Transport, and invents two that are not on the card ('Mechanism boundary', 'Decision rule'). The appendix's promised deliverable — 'The design card collects the decisions to make before data collection' — is therefore never shown completed, and a reader who tries to fill one in has no model.

**Edit.** Rebuild @tbl-worked-reminder-design with the card's exact twelve field names, in the card's order, every one filled: Claim family = causation (ITT); Construct = attendance as an administrative behavior, not intention; Measure = binary indicator from the booking system, thirty-day window, no self-report; Precision = 600 per arm, MDE ~7.6 points at 80% power; Analysis = difference in proportions, unpooled SE, no covariates; Ethics = administrative outcome, waiver of individual consent, no deception; Reproducibility = seed and script named below; Transport = other clinics with different booking systems, untested. Keep 'Mechanism boundary' and 'Decision rule' as two extra rows and add them to the card so the two tables match in both directions.  *(effort: medium)*

### [HIGH · visual] From line 200 through @tbl-claim-design-matching (line 328)

> @fig-participant-flow-threats prevents several losses from being collapsed into “dropout.”

**Problem.** From this sentence to the next table is about 1,300 words with no figure, table or callout — covering attrition, noncompliance and LATE, spillovers, demand effects, multiplicity, four kinds of replication, the reproducible-workflow checklist, and transport. It is the appendix's most abstract and most heavily bulleted stretch, and the reader crosses it with no visual anchor.

**Edit.** Add a transport figure beside section 12, where the argument is inherently two-sided and currently carries no image. Two columns, 'Study setting' and 'Target setting', with four aligned rows — Population, Treatment delivery, Outcome measure, Incentives and equilibrium — filled with the clinic's values on the left and the neighboring clinic's on the right; horizontal connectors between matching rows, solid where the effect modifier matches and dashed where it does not, with the dashed rows carrying the question the transport argument must answer. Caption states the takeaway rather than labelling the image: 'An effect travels only as far as its modifiers match; each dashed row is a claim the study cannot support.'  *(effort: medium)*

### [MEDIUM · accuracy] 'References cited in this appendix' (line 432, and Shadish at line 472)

> Bruhn, M., & McKenzie, D. (2009). In pursuit of balance

**Problem.** Bruhn & McKenzie (2009) and Shadish, Cook & Campbell (2002) both appear under a heading that says 'References cited in this appendix', and neither is cited anywhere in the text — I grepped the file and both strings appear only in the reference list. In a manuscript that bolds retractions in its reference lists and audits its own failed replications, an uncited entry in the methods appendix's own reference list is the kind of inconsistency a careful reader will notice.

**Edit.** Cite both where they belong rather than deleting them: Bruhn & McKenzie at the balance list in section 6 (they are the standard source for reporting standardized differences and for stratification versus post-hoc adjustment in field experiments), and Shadish, Cook & Campbell at @tbl-evidence-designs or at the internal/external validity distinction in section 12, where they are the canonical reference. If neither is wanted, delete both entries.  *(effort: small)*

### [MEDIUM · clarity] Section 8, after the LATE formula (line 233); also line 161 and line 241

> With a positive first stage no greater than one

**Problem.** Several specialist terms arrive undefined in a file that otherwise defines its vocabulary carefully. 'First stage' names the denominator E[D|Z=1] − E[D|Z=0] that was just displayed, but the connection is never made, so a reader who does not already know instrumental variables cannot map the phrase onto the equation two lines above. 'Allocation concealment' (section 6, item 1) is clinical-trial vocabulary used once and never glossed. 'Exposure mappings' (spillovers subsection) is the same.

**Edit.** Attach the term to the object the reader can see: 'the denominator above — the first stage — is the change in treatment receipt caused by assignment; when it is positive and no greater than one, the ratio has the same sign as ITT and at least its magnitude.' Gloss allocation concealment in a clause ('the people enrolling units cannot see the next assignment') and exposure mapping in a clause ('a rule stating whose treatment counts as exposure for each unit').  *(effort: small)*

### [MEDIUM · consistency] H1, line 7

> # Running an Experimental Study: From Question to Credible Evidence

**Problem.** The H1 does not match the filename (appendix-e-how-behavioral-evidence-is-built.qmd) or the way the book refers to the appendix. Appendices C, D and F all carry titles that echo their slugs; E does not, so the sidebar entry and the URL describe two different documents, and a reader who followed a link labelled 'how behavioral evidence is built' arrives at a page titled 'Running an Experimental Study'. The book also already has a front-matter chapter called 'How to Read Evidence', which makes the ambiguity worse. Every one of the twelve cross-references I found calls this file simply 'Appendix E' with no title at all.

**Edit.** Pick one and propagate it. The stronger option is to retitle the H1 to 'How Behavioral Evidence Is Built: From Question to Credible Evidence', which keeps the URL, matches the slug, pairs with 'When Evidence Breaks', and signals that the appendix serves readers of evidence as well as producers of it. Then use the title alongside 'Appendix E' in the links from how-to-read-evidence.qmd and appendix-f.  *(effort: small)*

### [MEDIUM · consistency] Closing sections (line 405), compared with Appendix F's closing

> ## Key ideas

**Problem.** Appendix E ends Key ideas → Study and practice → Activity callout. Appendix F ends Study and practice → Activity callout → the evidence-status map, with no Key ideas at all. The two research appendices are siblings, cross-reference each other, and are read consecutively, but they close differently and Appendix F's longest and most-used section arrives after what looks like the end of the appendix.

**Edit.** Give Appendix F a matching '## Key ideas' with three lines — a replication is an estimate, not a verdict; selection operates at five stages, not only at the journal; nonreplication is not evidence of misconduct — and place Key ideas before Study and practice in both files. Also consider moving Appendix F's evidence-status map above Study and practice so the practice section closes the appendix, as it does here.  *(effort: small)*

### [MEDIUM · insight] Section 10, 'Replication is estimation under a declared protocol' (line 277)

> Large replication projects in psychology and experimental economics found both replicated effects

**Problem.** This is the flattest possible statement of the book's most consequential empirical fact, and the numbers exist two files away: Appendix F gives 97% versus 36%, replication effects about half the magnitude, and 11 of 18 economics replications at 66% of the original. Appendix F links here ('as in [Appendix E]'); Appendix E never links there. A reader working through the methods appendix in order meets the replication projects as an unquantified generality and is given no route to the quantified version.

**Edit.** Either carry the headline numbers here in one clause, or make the sentence a link: '(Camerer et al., 2016; Open Science Collaboration, 2015; the numbers, and what they do and do not mean, are in [Appendix F](appendix-f-when-evidence-breaks.qmd#when-a-striking-result-becomes-less-convincing)).' Then close section 10 by sending the reader to the evidence-status map, closing the one-way cross-reference.  *(effort: small)*

### [MEDIUM · structure] Between '### 1. Turn a topic into a question and hypothesis' and '### 2. Define the construct…' (line 65)

> ### Research question check

**Problem.** The appendix runs a numbered spine from '### 1. Turn a topic into a question and hypothesis' to '### 13. Match the final sentence to the design', and this unnumbered heading sits at the same level between items 1 and 2. A reader scanning the sidebar TOC sees fourteen third-level entries with one that breaks the count and cannot be located in the sequence. The section-numbered headings are also what the concept index's deep links depend on: those anchors work only because Pandoc strips the leading '9. ', so renumbering would silently break external links.

**Edit.** Demote 'Research question check' to #### or make it a callout, so the 1–13 spine is unbroken. While editing, add explicit {#ids} to the numbered headings (e.g. {#define-question-hypothesis}) so the concept index's four deep links stop depending on Pandoc's number-stripping behavior.  *(effort: small)*

### [MEDIUM · visual] The only callout in the file, at the very end (line 417)

> ::: {.callout-tip .activity icon=false}

**Problem.** One callout in 5,200 words, and it is the last element before the references. None of the book's four styled classes (.core-idea, .activity aside, .research-lens, .evidence-and-boundary-conditions) is used earlier, even though this appendix is where boundary conditions are the explicit subject. The chapters set a rhythm the appendix abandons, so it reads as a different book.

**Edit.** Convert the 'Research question check' bullets (line 65) and the 'Ask of every causal claim' bullets (line 123) into styled callouts, and add a `.core-idea` box near the top stating the appendix's thesis in two sentences — something like 'A study earns exactly one kind of claim. The design decides which one, and the final sentence must not exceed it.' That also gives the appendix the Core Idea element the chapters have.  *(effort: small)*

### [LOW · clarity] Section 1, after the PICOT-style question template (line 55)

> Not every question needs every element in its title. The design does.

**Problem.** A compressed aphorism whose antecedent is ambiguous on first reading: 'The design does' could mean the design needs every element, or the design needs them in its title. The reader has to reread to resolve a sentence that is doing real work — it is the hinge between the question template and the rest of the appendix.

**Edit.** Split the ellipsis: 'A title need not contain every element. The design must specify all of them, whether or not the title says so.'  *(effort: small)*

---

## `appendices/appendix-f-when-evidence-breaks.qmd`  (16 findings)

### [HIGH · engagement] 'Flexible analysis creates many paths to a result', second paragraph (line 86)

> demonstrated how undisclosed flexibility can raise false-positive rates

**Problem.** The paper that named the problem is reported with no number and no demonstration. Simmons, Nelson and Simonsohn showed by simulation that four ordinary researcher degrees of freedom, used in combination, lift the false-positive rate from 5% to 61%, and then used exactly those choices to obtain a statistically significant finding that listening to 'When I'm Sixty-Four' made participants about a year and a half younger than a control song — an impossible result produced entirely by defensible-looking decisions. As written, the reader gets a proposition. With the numbers, the reader gets the shock the paper was written to produce, which is the whole point of the section.

**Edit.** Rewrite as: 'Simmons, Nelson, and Simonsohn (2011) showed by simulation that four common researcher degrees of freedom, used together, raise the false-positive rate from 5% to 61%. They then used those same choices to report, significantly, that listening to "When I'm Sixty-Four" made participants about a year and a half younger than a control song. The published report would have looked orderly.'  *(effort: small)*

### [HIGH · engagement] End of 'Underpowered studies create a selection problem' (line 78)

> Button et al. (2013) showed how low power can undermine reliability

**Problem.** The paper's headline estimate is omitted: median statistical power of roughly 21% across 49 neuroscience meta-analyses. That single number is what turns the preceding two paragraphs of reasoning about the winner's curse into a description of an actual literature, and it is the kind of finding a reader remembers for years. The sentence as written asserts that low power matters without saying how common it is.

**Edit.** 'Button et al. (2013) estimated median statistical power of about 21% across 49 neuroscience meta-analyses — that is, the typical study had roughly a one-in-five chance of detecting the effect it was looking for, a warning that applies wherever small, noisy studies pass through a significance filter.'  *(effort: small)*

### [HIGH · engagement] @tbl-famous-qualified-replication-cases, jam-study row (line 252)

> a larger display attracted more attention but a smaller display produced more purchases

**Problem.** The most famous numbers in behavioral science's most-quoted field study are missing. Iyengar and Lepper reported that 60% of passers-by stopped at the 24-jam display versus 40% at the 6-jam display, but that 3% of those at the large display bought a jar versus 30% at the small one — a tenfold difference. Without those figures the reader cannot feel why the claim swept management writing for twenty years, and therefore cannot feel the force of the near-zero meta-analytic mean that follows. Chapter 40 line 86 carries the same number-free sentence, so the omission is systematic.

**Edit.** Put the numbers in both places: '60% of passers-by stopped at the 24-jam display against 40% at the 6-jam display, but 3% of the large-display group bought a jar against 30% of the small-display group.' Then give the counterweight the same specificity: Scheibehenne, Greifeneder and Todd's meta-analysis found a mean effect near zero (d ≈ 0.02) with substantial heterogeneity. Surprise, then resolution, both with numbers.  *(effort: small)*

### [HIGH · engagement] @tbl-famous-direct-replication-cases, power-pose row (line 233)

> no effects on hormones or risk tolerance in a substantially larger sample

**Problem.** 'Substantially larger' hides the comparison that does the work: 42 participants in the original versus 200 in the replication. The row also omits the event that makes this case unique in the entire map — in 2016 the original's first author, Dana Carney, publicly stated she no longer believed the effect was real and posted her reasons. Nothing else in either table shows an original author updating on evidence, which is exactly the behavior the appendix is trying to teach.

**Edit.** Give both sample sizes ('42 participants in the original; 200 in the replication') and add one sentence: 'The original's first author later stated publicly that she no longer believed the effect was real and set out her reasons. That is what updating looks like from the inside, and it is rarer in this map than nonreplication.' This is the appendix's best available human detail and it is currently absent.  *(effort: small)*

### [HIGH · insight] Introduction to the evidence-status map (line 214)

> This map covers influential cases used in or closely related to the book.

**Problem.** All nineteen entries update in the deflationary direction. There is not one worked case of a famous effect that survived a coordinated test. Presented alone, the map trains exactly the availability bias Chapter 9 warns against, and it invites the 'it has all been debunked' reading that the appendix explicitly rejects three sections earlier when it says a replication rate is not the proportion of a field that is true. The appendix asserts that both outcomes are information and then illustrates only one.

**Edit.** Add a short third table, 'Famous findings that held up under coordinated testing', with three or four rows and the same two-column structure: anchoring replicated with large effects in Many Labs 1 (Klein et al., 2014); the Asian-disease framing effect replicated in the same project (Ch. 12 and Ch. 17); Asch-type conformity replicated across 133 studies in Bond and Smith's (1996) meta-analysis, which Chapter 26 already cites, with the cultural and period moderators it identified. A map that records survivals as carefully as failures is more authoritative, not less, and it makes the four-status framework complete.  *(effort: medium)*

### [HIGH · insight] 'A concrete update: watched eyes and the honesty box' (line 39)

> Contributions per unit consumed were nearly three times as high during eye-image weeks

**Problem.** The worked case sits two sections before 'Underpowered studies create a selection problem' and is never used there, although it is the appendix's own best illustration of that mechanism. The original comparison rests on ten alternating weekly totals in a single university coffee room — small, noisy, and selected — which is precisely the study profile the winner's-curse section describes and @fig-selected-literature-simulation simulates. The reader is given the update and the correct moral ('this is how scientific updating should work') but never the reason the original estimate was so large, so the case teaches the conclusion without the mechanism.

**Edit.** Give the case its design scale and its published ratio: 'Contributions per unit consumed were 2.76 times as high in eye-image weeks. The comparison rests on ten weekly totals from one coffee room.' Then add a pointer sentence in the winner's-curse section: 'The eye-image result is what the right-hand histogram of @fig-selected-literature-simulation looks like from the inside — a small, noisy study that cleared the threshold and was therefore the one everyone saw.' The forward and backward links cost two sentences and make the appendix argue with itself instead of in parallel.  *(effort: small)*

### [HIGH · visual] Callout immediately above the two map tables (line 217)

> Read the status, not just the headline

**Problem.** The callout defines four statuses — Not reproduced, Attenuated or conditional, Reinterpreted, Retracted or integrity-qualified — and instructs the reader to read them. Neither table has a status column. The label is buried inside the bold opening clause of each cell's prose, in wordings that do not always match the four ('Specific procedure not reproduced; broader mechanism has qualified support'; 'Not reproduced; original article retracted'; 'Reinterpreted by statistical correction, not a failed replication'). The instruction cannot be carried out by scanning, which is how a lookup table is used. The two tables are also split by a heading that does not correspond to the four statuses, so 'Reinterpreted' (hot hand) sits in the table titled 'became smaller, conditional, or different'.

**Edit.** Add a middle column, 'Status', carrying exactly one of the four defined labels per row (allow a second where genuinely dual, e.g. 'Not reproduced · Retracted'), move the prose to the last column, and sort each table by status. Then the callout's four definitions become a legend for a column that exists. This is the most-linked section of the appendix — the concept index and How to Read Evidence both point at it — so it should be the most scannable.  *(effort: medium)*

### [HIGH · visual] 'Publication bias changes what readers can see', item 6 of the disappearance list (line 106)

> a published correction or failed replication receives less attention than the original claim

**Problem.** The two map tables contain the raw material for the appendix's most striking unstated number and never compute it: the lag between a famous claim and its decisive correction. Bargh 1996 to Doyen 2012 is 16 years. Strack 1988 to Wagenmakers 2016 is 28. Ariely and Wertenbroch 2002 to the retraction dated 2 September 2026 is 24. Iyengar and Lepper 2000 to Scheibehenne et al. 2010 is 10. The reader is told corrections travel slowly and is never shown how slowly, in a file whose most important figure-shaped fact is sitting unused in two prose tables.

**Edit.** Add a dumbbell timeline beside this paragraph (or beside the status callout). Horizontal axis: year, 1985 to 2026, ticked every five years. One row per mapped finding, ordered by original publication year, labelled on the left with a three-word name ('Elderly-word priming', 'Pen in teeth', 'Jam display'). Open circle at the original publication, filled circle at the decisive update, connecting line colored by the four status labels with a legend. Right-hand margin prints the lag in years. Caption states the takeaway, not the contents: 'Corrections arrive a decade or more after the claim they revise; by then the claim has usually been taught.'  *(effort: large)*

### [MEDIUM · accuracy] Third paragraph of 'When a striking result becomes less convincing' (line 35)

> a replication rate is not the proportion of a field that is true

**Problem.** The caution is correct and the paragraph two above it gives only the one indicator the Open Science Collaboration itself warned against reading alone — 97% versus 36% significance. The project reported several: notably, 47% of original effect sizes fell inside the replication's 95% confidence interval, a materially different picture from 36%, and the two numbers together are the argument this paragraph is currently making by assertion. Nothing here is wrong; the appendix simply passes up the chance to prove its own point with the project's own data.

**Edit.** Add the second indicator where the first appears: '…compared with 36% of the replications. On a different indicator from the same project, 47% of original effect sizes fell within the replication's 95% confidence interval.' Then convert the caution into a conclusion drawn from the gap: 'Two defensible summaries of the same 100 studies differ by eleven points. That is why a replication rate is not the proportion of a field that is true.'  *(effort: small)*

### [MEDIUM · consistency] End of the reference list (line 504 onward)

> Zhong, C.-B., & Liljenquist, K. (2006). Washing away your sins

**Problem.** The list is alphabetical through Zhong and then continues with four more entries appended after Z: Mazar et al. (2008), Journal of Marketing Research (2024), Verschuere et al. (2018), and Psychological Science (2026). These are the four added when the integrity updates were written, and they are among the entries a reader is most likely to go looking for, since they carry the expression of concern and the retraction. In a reference list that deliberately bolds retraction status, misfiled entries undercut the care on display.

**Edit.** Interfile the four in alphabetical position. Also give the Journal of Marketing Research (2024) notice a parenthetical citation in the Mazar table row, which currently says 'A 2024 journal notice' with no citation marker, so the entry is technically uncited.  *(effort: small)*

### [MEDIUM · consistency] Hagger et al. (2016) entry, line 364; Hyndman & Bisin (2026) entry, line 368

> Perspectives on Psychological Science, 11(4), 546-573.

**Problem.** Two entries do not follow the list's own format. Hagger et al. (2016) and Hyndman & Bisin (2026) print the journal name without the italic markup every other entry uses, and Hagger's page range uses a hyphen where the rest of the list uses an en dash. These two entries carry the ego-depletion multilab result and the deadline replication behind the September 2026 retraction — the appendix's two most consequential updates — so they are the entries readers will actually copy.

**Edit.** Apply the list's format to both: italicize the journal titles and change 546-573 to 546–573.  *(effort: small)*

### [MEDIUM · engagement] @tbl-famous-direct-replication-cases, ego-depletion row (line 234)

> estimated a near-zero effect whose interval included zero (Hagger et al., 2016)

**Problem.** The row names three coordinated projects (Hagger 2016, Vohs 2021, Dang 2021) and reports no effect size, no interval and no sample size for any of them — in an appendix whose step 4 tells readers to 'compare estimates and intervals' and to 'ignore the temptation to reduce the pair to significant versus nonsignificant'. The row models the practice the appendix argues against. Hagger et al.'s d = 0.04 with a 95% interval of −0.07 to 0.15, across 23 laboratories and 2,141 participants, is precisely the comparison being asked for, and it makes the tension with Dang et al.'s small significant effect legible rather than merely asserted.

**Edit.** Add d and interval for Hagger et al., participant totals for Vohs et al. (36 sites) and Dang et al., and one clause naming what the disagreement between them turns on (protocol and task choice). The row then demonstrates step 4 instead of contradicting it.  *(effort: small)*

### [MEDIUM · engagement] 'Publication bias changes what readers can see', Franco et al. paragraph (line 110)

> examined 221 studies conducted through one known social-science program

**Problem.** This is the strongest piece of evidence in the appendix and it is introduced anonymously, with its own insight buried in the last sentence ('The study is especially useful because the denominator was known'). The program is TESS, Time-sharing Experiments for the Social Sciences, which approves and funds studies before any result exists — that design fact is what makes the denominator observable, and naming it lets a reader check the claim instead of taking it on trust.

**Edit.** Lead with the design: 'Almost every estimate of publication bias has to guess at the denominator. Franco, Malhotra, and Simonovits (2014) did not have to: they studied 221 experiments funded through TESS, a program that approves studies before results exist, so the full set of completed studies was observable. Studies with strong results were about 40 percentage points more likely to be published and 60 percentage points more likely to even be written up. Most of the loss happened before any journal saw the work.'  *(effort: small)*

### [MEDIUM · engagement] Opening paragraph (line 17)

> Imagine that one hundred teams test promising interventions.

**Problem.** The appendix opens on a hypothetical while holding a real event nine days old: a 2002 paper on deadlines and precommitment, taught in behavioral courses for over two decades and cited in this book's own Chapter 19, was retracted on 2 September 2026, with both authors agreeing, after a direct replication found negligible effects. The evidence map's header is dated 10 September 2026. An appendix about evidence breaking opens by asking the reader to imagine evidence breaking, with the strongest concrete instance available sitting 220 lines below in a table cell.

**Edit.** Open with the real case in three sentences — the claim, how long it was taught, the replication, the retraction date, and that both authors agreed — then pivot: 'That was one paper. Now imagine one hundred teams…' The thought experiment does more work after a reader has watched it happen once, and the date makes the appendix feel live rather than archival.  *(effort: small)*

### [MEDIUM · structure] Line 178, between the two numbered procedures

> ## Before you repeat a finding

**Problem.** A three-sentence H2 sits between 'How to interpret a replication' (eight numbered steps) and 'What to do when you find a serious problem' (seven numbered steps), breaking the pairing of the two procedures and reading as a stub. Its content is a pointer to two other documents plus one instruction, and that instruction ('Record the original comparison, the later update, and the sentence you would now be willing to teach') is the best single line in the section — it deserves a position where it will be read as a conclusion rather than as an aside.

**Edit.** Fold it into 'How to interpret a replication' as a closing step 9 — 'Write the sentence you would now be willing to teach, and keep it beside the original claim' — or move it to open the evidence-status map, which is where its instruction actually applies. Either placement removes a heading-level stub and strengthens the line.  *(effort: small)*

### [LOW · consistency] Caption of @tbl-famous-qualified-replication-cases (line 259), compared with line 244

> Famous findings revised by later evidence and analysis

**Problem.** The first map table's caption carries 'updated 10 September 2026'; the second carries no date, although both are governed by the same dated header note and both will age at the same rate. A reader who arrives at the second table by deep link — which the concept index makes likely — sees an undated evidence map.

**Edit.** Add the same dated stamp to the second caption, and repeat the date inside the status callout so it appears once per screen in the section readers link into directly.  *(effort: small)*

---

## `chapters/01-how-decisions-should-be-made-and-how-they-actually-are.qmd`  (16 findings)

### [HIGH · engagement] ### Representation and comparison → #### 1. The same treatment data, framed through survival or mortality

> surgery was relatively more attractive in the survival frame

**Problem.** The chapter's single most direct challenge to description invariance is delivered with zero numbers. "Relatively more attractive" is a statistician's phrase where the actual result is startling. I checked Chapter 12, which this passage forward-references: it never cites McNeil et al. at all, so the numbers appear nowhere in the book.

**Edit.** Put the choice shares in the sentence: in McNeil et al. (1982), radiation therapy was chosen by about 18% of respondents when outcomes were framed as survival and about 44% when the identical data were framed as mortality — same patients, same five-year numbers, same physicians among the respondents. Add the framing sentences themselves ("90 of 100 live through the post-operative period" vs "10 of 100 die during surgery") so the reader can feel that they are logically identical. Verify the exact percentages against the paper before publication.  *(effort: small)*

### [HIGH · insight] ## What the six examples reveal

> Some contextual changes alter real features of a decision

**Problem.** The chapter's sharpest analytical move — that the six examples split into two fundamentally different kinds, those that change the real decision problem (default, active motive, action path) and those that change only the representation of an unchanged problem (frame, decoy) — arrives as two flat sentences after the summary table, and the table itself does not sort the examples that way. This is the distinction that determines which normative verdict applies, and a reader can finish the section without extracting it.

**Edit.** Add a fourth column to @tbl-seven-context-examples headed "What changed: the problem or its representation?" and fill it (frame: representation; decoy: representation; default: the problem, via effort and the consequence of inaction; ad redesign: the problem, via the action path; Mars: representation of the consideration set; museum: the problem, via active values). Then promote the two flat sentences to a short lead-in stating why the distinction matters: only the representation cases are direct violations of the benchmark; the others are cases where the benchmark was fed different inputs.  *(effort: medium)*

### [HIGH · structure] ## Six ways context enters choice → collapsed callout

> Two examples from commercial practice

**Problem.** Examples 4 and 5 live inside a `collapse=true` callout. In the default collapsed state the reader sees numbered examples 1, 2, 3, then 6 — a visible numbering gap with no explanation. The callout also jumps heading levels (a `##` callout title containing `####` sub-headings), and the numbered items inside it are invisible to the table of contents while the summary table below lists all six as equals.

**Edit.** Either set `collapse=false` so the numbering is continuous, or renumber the visible examples 1–4 and present the two commercial cases inside the callout as unnumbered cases ("A right-pointing arrow…", "Mars publicity…") with a lead-in line saying they are illustrations with weaker evidence, not part of the numbered sequence. Change the section heading to "Four ways context enters choice" if you renumber, and set the callout's internal headings to `###` so levels do not jump.  *(effort: small)*

### [MEDIUM · accuracy] #### 3. Organ donation and the consequence of doing nothing

> found no average increase in deceased donation after the policy switch

**Problem.** The Dallacker et al. (2024) result is presented as the settled state of the evidence, but the earlier and widely cited cross-country work (Abadie & Gay, 2006, Journal of Health Economics) reported that presumed-consent countries had substantially higher donation rates. A reader who encounters the opposite claim elsewhere has no way to reconcile them, and the chapter loses a chance to model exactly the evidence discipline it preaches. This is a missing boundary condition rather than an error.

**Edit.** Add one sentence naming the tension and what resolves it: cross-sectional comparisons across countries (Abadie & Gay, 2006) found higher donation rates under presumed consent, while the within-country before-and-after analysis of countries that actually switched (Dallacker et al., 2024) found no average increase — the difference is that cross-sectional comparisons cannot separate the default from everything else that differs between countries. Add the Abadie & Gay reference to the list.  *(effort: small)*

### [MEDIUM · clarity] #### 1. The same treatment data, framed through survival or mortality

> The observed shift is therefore a comparatively direct challenge to

**Problem.** Two technical terms are used as though already defined. "Description invariance" is bolded here as a key term but never defined, and "regularity" appears in the next example ("contrary to regularity in standard menu-independent models") with no gloss. A first-time reader in Chapter 1 has no way to recover either.

**Edit.** Define both in place, in half a sentence each: "...a challenge to **description invariance**, the requirement that logically equivalent descriptions of the same consequences produce the same preference"; and "...contrary to **regularity**, the requirement that adding an option cannot increase the choice share of an option already on the menu." Both definitions are one clause and cost no hedging.  *(effort: small)*

### [MEDIUM · clarity] ## Practice Lab

> Choose one consequential decision that has not yet been finalized.

**Problem.** The book's first Practice Lab — the one that sets the reader's expectation for the other 41 — lists five steps but names no output artifact and no success check, unlike ch14 ('The observable output is the two natural-frequency trees'), ch16 ('The output is the completed register—not a description'), ch31 ('The output is the diagnosis'), and ch41 ('The submitted artifact is the completed pipeline'). ch02's eight-step lab has the same gap.

**Edit.** Add to ch01: 'The artifact is a two-column page — How it should be made beside How it is being made — with the decision loop sketched underneath and one function circled. It succeeds when the circled function is one you could still change before the decision closes, and the named evidence has a source and a date by which it could arrive. About 30 minutes.' Add the equivalent closing pair to ch02, ch21 and ch40.  *(effort: small)*

### [MEDIUM · consistency] ## Six ways context enters choice (heading and section IDs)

> Six ways context enters choice {#seven-ways-context-enters-choice}

**Problem.** Three stale identifiers survive from a seven-example version: `{#seven-ways-context-enters-choice}`, `{#what-the-seven-examples-establish-and-what-they-do-not}`, and `{#tbl-seven-context-examples}`. These are load-bearing — concept-index.qmd links to the first two — so they cannot simply be deleted, but the visible anchor in a reader's URL bar contradicts the heading. Separately, `{#a-functional-decision-loop}` on the heading "How decisions are actually made" is linked from concept-index.qmd under the displayed label "Ch. 1, A functional decision loop," a section title that no longer exists anywhere in the book.

**Edit.** Rename all four IDs to match their headings (`six-ways-context-enters-choice`, `what-the-six-examples-reveal`, `tbl-six-context-examples`, `how-decisions-are-actually-made`) and update the four referring lines in concept-index.qmd (lines 213, 215, 439, 595), fixing the displayed label "A functional decision loop" to "How decisions are actually made" at the same time. Also check concept-index.qmd line 9, which points "Ch. 1, Mars publicity" at `#social-meaning-accessibility-and-active-motive` — the Mars example is not in that section.  *(effort: small)*

### [MEDIUM · engagement] #### 2. The subscription option nobody chose

> yet its presence shifted choices toward the combined offer

**Problem.** The decoy example is told entirely in qualitative language ("shifted," "much more popular") when Chapter 11 already carries the exact counts. The reader meets the example here first, so the flat version is the one that forms the impression, and the punchline — a 68/32 split reverses to 16/84 because of an option nobody took — is lost.

**Edit.** Add one clause with the counts, which Chapter 11 already reports: "Sixteen of 100 chose web-only, none chose print-only, and 84 chose print-plus-web; with the print-only option removed, a comparable group split 68 web-only to 32 print-plus-web." Keep the forward reference to Chapter 11 for the mechanism.  *(effort: small)*

### [MEDIUM · engagement] #### 3. Organ donation and the consequence of doing nothing

> found large differences in stated agreement across online experimental defaults

**Problem.** "Large differences" is exactly the vague quantifier the chapter elsewhere warns against, and it wastes the most quotable number in the behavioral-defaults literature. The hedging ("stated agreement," "online experimental") is correct and should stay — it is the magnitude that is missing.

**Edit.** State it: "Johnson and Goldstein (2003) found that 42% agreed to donate under an opt-in default while 82% agreed under an opt-out default, with an active-choice condition close to the opt-out rate." Keep "stated agreement in an online experiment" as the framing clause, since the Dallacker paragraph immediately afterward does the real corrective work.  *(effort: small)*

### [MEDIUM · engagement] ## One decision, two questions

> Return to the hiring committee in the preface. At 3:17 p.m.

**Problem.** Chapter 1 opens by asking the reader to remember a scene from the preface — a section many readers skip. What returns is a timestamp and an abstraction ("Two candidates remain"), not a scene. No candidate is characterized, so the four paragraphs that follow describe a process problem with nothing concrete to attach to, and the chapter deviates from its own template, which calls for a concrete opening scenario before the Core Idea rather than a callback.

**Edit.** Restore the scene in three sentences before the first question: give the two finalists one distinguishing detail each (e.g., one arrives from a name-brand employer with a polished interview story; the other has a quieter record of shipped work and a reference nobody has called), and name one thing the committee has not done. Then ask "How should the committee decide?" The rest of the section already pays off these details — prestige, the vivid story, the uncalled reference — but currently pays off details the reader was never given.  *(effort: medium)*

### [MEDIUM · engagement] ## From a normative benchmark to descriptive predictions

> The examples below ask where the model succeeds, where its predictions fail

**Problem.** This is the third consecutive signpost in a short stretch: "The six examples that follow test those descriptive assumptions," then "For example, expressing the same outcome as survival or mortality should not reverse preference," then "The examples below ask where the model succeeds..." The section announces the examples, pre-summarizes one of them, and announces them again before any example arrives. Momentum stalls at exactly the point where the chapter should be accelerating into its evidence.

**Edit.** Cut the standalone sentence "The examples below ask where the model succeeds, where its predictions fail, and where it leaves out part of the decision," and cut the survival/mortality preview sentence (it duplicates example 1 two paragraphs later). Keep the stability-assumption paragraph, which does real work, and go straight into the examples.  *(effort: small)*

### [MEDIUM · engagement] ## Outcome is not process

> An investor may buy after one enthusiastic post and make money.

**Problem.** This is one of the chapter's most important ideas and it is carried by three hypothetical agents in three consecutive sentences — "an investor," "another," "a surgeon" — none with a name, number, or date. The surrounding paragraphs are also agentless ("Rewarding luck or punishing a defensible risk can teach the wrong lesson"). The result is a full section on a vivid topic with nothing a reader can picture.

**Edit.** Replace one of the three generic agents with a concrete, checkable case and give it two numbers. A documented option is the hiring committee itself: a hire who looked like a mistake in month three and a strong performer in year two, with the committee's own recorded forecast beside both. Alternatively use a named public case where the process record survives. Keep the other two hypotheticals as compressed parallels.  *(effort: medium)*

### [MEDIUM · visual] ## How a decision should be made (figure caption)

> A normative decision process built around the rational-choice benchmark.

**Problem.** Both of the chapter's figure captions describe the arrows rather than stating a claim. The caption for @fig-normative-decision-loop reads as a label plus a traversal of the diagram; @fig-behavioral-decision-loop's caption does the same at greater length. A reader skimming captions — which many do — learns the diagram's topology and none of its point. This matters more here than elsewhere because the two diagrams are the chapter's central contrast and the reader must grasp what the second adds to the first.

**Edit.** Lead each caption with the takeaway, then describe. First: "The benchmark specifies how the ingredients of a choice should relate once alternatives, beliefs, and values are given — it says nothing about where they come from. Information about alternatives supports prediction…" Second: "Everything the benchmark takes as given is itself produced: context shapes what information is presented, what gets selected and interpreted, and what the outcome is taken to mean. External context shapes…" This also makes the two captions readable as a pair.  *(effort: small)*

### [MEDIUM · visual] #### 1. The same treatment data, framed through survival or mortality

> The cumulative probabilities and time horizons were complementary

**Problem.** Chapter 11 gives the decoy example a dedicated figure (economist-subscription-decoy.svg) showing both menus and both choice distributions. The framing example — which the book treats as the more direct violation of the benchmark — has no figure here and none in Chapter 12 either. The two flagship demonstrations are visually unequal, and the framing one is the harder to grasp in prose because the reader must hold two complementary number sets in mind at once.

**Edit.** Add a two-panel figure: left panel shows the survival-framed data as presented to respondents (e.g. 90 of 100 survive surgery, 68 at one year, 34 at five years) with a bar for the share choosing radiation; right panel shows the complementary mortality framing of the identical data with its own bar. Label the panels "Same numbers" above and "Different choices" below. Caption should state the claim, not the layout: "Complementary descriptions of identical outcome data changed which treatment respondents preferred."  *(effort: large)*

### [LOW · insight] ## Learning goals, goal 2

> Distinguish normative, descriptive, and prescriptive questions about the same decision.

**Problem.** 'Distinguish' opens 25 of the book's 130 learning goals and appears in 24 of 42 chapters, most often as the middle goal. The underlying three-goal architecture is good — it climbs reliably from explain, through distinguish, to a production verb (Redesign 10, Produce 9, Design 7, Build 7) — but the repeated middle rung makes 42 chapters read as one template rather than 42 arguments.

**Edit.** Vary the middle rung where the chapter supports a sharper verb: Classify (ch26, ch31), Trace (ch10 already does), Attribute (ch07), Locate (ch17 on the fourfold pattern), Separate where two things are genuinely being pulled apart rather than told apart. Target roughly half the 25 instances; do not chase zero.  *(effort: medium)*

### [LOW · structure] ## Take it forward

> It would expose the assumptions that need attention while there is still time

**Problem.** "Take it forward" in this chapter closes the hiring scene but commits the reader to nothing. Compare Chapter 2's, which ends with an explicit instruction ("For your next consequential choice, start with the same practical test: name one feasible alternative you had overlooked"). Chapter 1's version is a nice landing, not a handoff.

**Edit.** Keep the chair's better question, then add one sentence directing the reader: "Before the next group decision you attend, write your own prediction and the one piece of evidence that would change it — on paper, before anyone speaks. Compare it afterward with what the room decided." That is testable and takes thirty seconds, which is the point.  *(effort: small)*

---

## `chapters/02-building-a-better-decision-alternatives-opportunity-cost-information-and-robustness.qmd`  (14 findings)

### [HIGH · accuracy] ### Generate alternatives deliberately

> Choice overload becomes more likely when alternatives are complex, preferences are uncertain

**Problem.** The moderator claim is cited to three sources as though they agreed, but Scheibehenne, Greifeneder, and Todd (2010) found a mean effect essentially indistinguishable from zero across roughly 50 experiments and reported that they could not identify reliable moderators. Only Chernev et al. (2015) supports the sentence as written. Iyengar and Lepper (2000) is the single original study whose headline result did not hold up. Appendix F (line 252) already states this correctly — "a near-zero mean effect with substantial heterogeneity" — so the chapter contradicts the book's own evidence appendix.

**Edit.** Rewrite to match Appendix F: "The best-known demonstration — more jam varieties attracting attention but producing fewer purchases (Iyengar & Lepper, 2000) — did not generalize: a meta-analysis of about 50 experiments found a mean effect near zero with wide heterogeneity (Scheibehenne et al., 2010). A later meta-analysis identified conditions under which overload does appear: complex alternatives, uncertain preferences, difficult tasks, and effort-minimizing choosers (Chernev et al., 2015)." This is also more interesting than the current sentence, because the reversal is the story.  *(effort: small)*

### [HIGH · accuracy] ## Name the opportunity cost

> found a robust but considerably smaller average effect than the original studies reported

**Problem.** Two problems in one sentence. First, "considerably smaller" is unquantified, in a chapter that elsewhere insists on inspectable numbers — the reader cannot tell whether the 75%-to-55% gap shrinks to 15 points or to 3. Second, Appendix F (line 256) reports the same meta-analysis with a boundary condition this chapter drops: the effect appears "mainly in hypothetical decisions." That boundary is directly load-bearing here, because the DVD study the chapter just described was itself hypothetical.

**Edit.** State the pooled estimate from Maguire et al. (2023) numerically, and carry over the moderator: "...found a reliable but considerably smaller pooled effect [insert the reported estimate], concentrated in hypothetical rather than consequential decisions." Then draw the practical inference the reader needs: reminding someone of a forgone use of money reliably shifts what they say they would do; whether it shifts what they actually buy is less well established.  *(effort: small)*

### [HIGH · clarity] ### Make values and trade-offs inspectable (tbl-prediction-value)

> What is expected to happen, when, and across what plausible range?

**Problem.** @tbl-prediction-value is an empty template: every cell in both option rows contains the identical string of questions. The chapter has spent 150 lines building a specific, concrete case — a student with two named offers — and then hands the reader a blank form instead of showing the tool working on that case. A reader who has never filled one of these in learns nothing about what a good entry looks like, how much detail it needs, or how uncertainty is recorded.

**Edit.** Fill the table with the student's case and keep the questions as the column headers only. E.g. Consulting row, prediction cell: "Structured training, 60–70 hour weeks in year one based on two alumni accounts and Glassdoor reports; wide uncertainty because neither source is a random sample." Valuation cell: "Income floor met; health is a threshold, not a weight — over 65 hours sustained is unacceptable." Start-up row similarly, and a third row for "negotiate start date and workload," which is the option the chapter argues she should have added. Move the generic question wording into a one-line note under the table.  *(effort: medium)*

### [HIGH · insight] ### Make values and trade-offs inspectable

> is hard to interpret until the relevant range and trade-off are specified

**Problem.** This clause contains the single most useful and least known idea in the section — that a weight is meaningless without the attribute range it applies to — and it is buried as a subordinate clause in a transitional sentence, never explained, never illustrated, and never used again. A reader will skate past it, then go build exactly the meaningless weighted table the sentence warns against. This is the chapter stopping one step short of its best point.

**Edit.** Give it its own short paragraph with a worked line: "Weighting health at 30 percent means nothing until you say 30 percent of what swing. If the two jobs differ by 45 versus 50 hours a week, health deserves little weight; if they differ by 40 versus 70, it may dominate everything else in the table. A weight is a statement about a range, not about how much you care in general — which is why weights copied from one decision to another are usually wrong." Then connect it back to the health-as-threshold sentence that follows.  *(effort: small)*

### [HIGH · visual] ## Construct the feasible set

> everything one can describe, including options that are impossible or impermissible

**Problem.** The chapter runs roughly 1,700 words from its only figure (line 44) to its first table (line 151) with no visual relief at all — across "Define the decision," "Construct the feasible set," "Name the opportunity cost," and "Separate predictions from values." The three-set distinction in this section is precisely the kind of relation prose handles badly: the text says people both miss feasible options and entertain infeasible ones, which is a two-directional relation a reader must construct mentally from a bulleted list.

**Edit.** Add a figure here: a large outer region labelled "Imaginable," containing two overlapping circles labelled "Feasible" and "Considered." Label the four regions with the student's own case — overlap = "consulting, start-up"; feasible-not-considered = "negotiated start date, staged commitment, reopened search"; considered-not-feasible = "the role she assumed was still open"; imaginable-only = "a job that does not exist." Caption states the claim: "A consistent ranking cannot recover a good alternative that never entered the comparison." This single diagram carries the section's whole argument.  *(effort: large)*

### [MEDIUM · clarity] ## Use proportionate analysis

> they search until an alternative meets an aspiration level

**Problem.** Satisficing is introduced as a bolded key term, defined abstractly, and immediately followed by a seven-row table of decision features. The reader never sees an aspiration level in operation, so the term stays verbal. This matters because satisficing is the concept that licenses everything the chapter has just told the reader not to do, and the licensing condition ("when further search costs more than it is likely to improve the decision") is exactly the judgment readers get wrong.

**Edit.** Add one concrete sentence before the table: "Setting an aspiration level means deciding in advance what counts as good enough — 'the first apartment under €1,200 within 30 minutes of campus with a real kitchen' — and taking it, rather than viewing forty more to establish that nothing better exists. The discipline is in setting the threshold honestly before searching, not in stopping early." Then note the failure mode the chapter otherwise omits: an aspiration level revised upward during search is not satisficing, it is optimizing with extra steps.  *(effort: small)*

### [MEDIUM · engagement] Opening scenario

> The consulting firm promises structured training and a familiar name

**Problem.** The chapter's protagonist is called "the student" about twenty times and is never named, never located, and never given a number. The opening has real potential — a stalled comparison table, a column nobody can fill — but with no salary, no city, no deadline, and no name, the reader tracks an argument rather than a person. Every later sentence then has to begin "The student may...", which is also the main source of the chapter's flat, agentless rhythm.

**Edit.** Name her and give the opening three numbers: a consulting offer at a stated salary, a start-up offer at a lower one with equity, and a Friday deadline. Then use her name throughout in place of "the student." This costs nothing in rigor, makes the Friday deadline in "Define the decision before solving it" and "By Friday" in the recommendation section land as callbacks rather than as new information, and lets the opportunity-cost section (below) work a real number.  *(effort: medium)*

### [MEDIUM · engagement] ## Name the opportunity cost

> the value of the best feasible alternative forgone

**Problem.** The section defines opportunity cost precisely, illustrates it with a borrowed $14.99 DVD study, and then never computes it for the case the chapter has been building. The student's own opportunity cost — the concrete thing the reader came for — is described only in the abstract ("its complete value is the opportunity cost of accepting the start-up"). The chapter teaches a calculation it never performs.

**Edit.** Add a short worked paragraph before the "If I choose this" prompt, using the numbers from the revised opening: the salary gap over two years, plus what consulting's structured training would have supplied and when, minus what the start-up's equity might return and with what probability — stated as a range, not a point. End by naming what the exercise reveals that the comparison table did not: that the cost of the start-up is not a number but a whole path, and that discovering a third feasible option would raise the cost of both offers already on the table.  *(effort: medium)*

### [MEDIUM · engagement] ## Name the opportunity cost

> One hundred and fifty students imagined deciding whether to buy a desirable DVD

**Problem.** The chapter's one empirical punch — a one-clause reminder moving purchase intent from 75% to 55% — is delivered mid-paragraph after a run-up of method description, so the surprise arrives already deflated. The paragraph currently reads: setup, sample, price, condition, result, condition, result, interpretation. The reader reaches the numbers with no reason to expect them to be interesting.

**Edit.** Invert the paragraph: lead with the finding, then explain how small the manipulation was. "Changing five words on a response option moved purchase rates by twenty percentage points. Frederick et al. (2009) offered participants a desirable DVD for $14.99. When the alternative read simply 'Do not buy,' 75% bought; when it read 'Keep the $14.99 for other purchases,' 55% did. Nothing about the DVD, the price, or the options had changed — only whether the money's other uses were easy to picture."  *(effort: small)*

### [MEDIUM · structure] ## A better decision begins before comparison

> A practical sequence for better decisions: expand the feasible set

**Problem.** Chapter 1 ends by promising that "Chapter 2 turns this account into practical work: expand the feasible set, identify what commitment would give up, and test the assumptions on which a recommendation depends." Chapter 2 never picks the handoff up — it opens on a new protagonist with no reference back, and the hiring committee, which the whole of Chapter 1 built, never appears again. The two chapters are a matched pair (diagnosis, then repair) presented as unrelated.

**Edit.** Add two sentences after the figure connecting the tools to the committee: the option the committee never discussed (extending the search) is an instance of Search; the meaning of "fit" nobody unpacked is the prediction/valuation confusion; the vote taken before anyone recorded a judgment is the missing robustness check. One paragraph makes Chapter 1's diagnosis pay off and gives the reader a second worked case at no cost in length.  *(effort: small)*

### [MEDIUM · structure] line 104, choice overload paragraph

> the task is difficult, or the chooser is trying to minimize effort

**Problem.** Choice overload's moderator list is given twice, near-verbatim (five shared 8-grams including the quoted twelve words), with the same three citations (Iyengar & Lepper 2000; Scheibehenne et al. 2010; Chernev et al. 2015) in ch02 line 104 and ch40 line 86, and no cross-link either way. The division of labour is also backwards: ch40 has the concrete anchor ("Iyengar and Lepper's jam study made choice overload vivid: a large display attracted attention, while a smaller display produced more purchases"), while ch02 — which reaches the reader 38 chapters earlier — has only the abstract moderator list and so states the caveat before the reader has met the phenomenon it qualifies.

**Edit.** Keep ch40 as the full treatment. Replace ch02 line 104's moderator sentence with a forward pointer that preserves the local point about option-set breadth: "A set can also grow too large to use; [*Choice Architecture*](40-choice-architecture-the-environment-gets-a-vote.qmd#construct-the-menu-options-order-and-overload) sets out when that happens. The aim here is a set broad enough to escape tunnel vision and structured enough to remain actionable." Drop the three duplicated citations from ch02's reference list, since ch40 carries all three.  *(effort: small)*

### [LOW · consistency] ## References cited in this chapter

> Maguire, A., Persson, E., & Tinghög, G. (2023)

**Problem.** The reference list is alphabetical except that Maguire (2023) is placed between Frederick (2009) and Iyengar (2000), apparently because it was inserted next to the Frederick entry it qualifies. Every other chapter's list is strictly alphabetical.

**Edit.** Move the Maguire entry after Keeney & Raiffa. While there, verify the Frederick et al. sample descriptor in the body text — "One hundred and fifty students" should be checked against the paper, since the published studies drew on several different populations and the student descriptor may belong to a different study in the same article.  *(effort: small)*

### [LOW · consistency] ## Learning goals

> After reading this chapter, you should be able to:

**Problem.** Forty chapters list exactly three goals; ch01 lists four, ch02 lists six, ch42 lists four. Separately, only ch01 and ch02 carry the lead-in line 'After reading this chapter, you should be able to:' — the other 40 begin the bullet list with no stem, so the goals read as fragments ('Explain inattentional blindness and change blindness.') with nothing to complete.

**Edit.** Either add the stem to all 42 or delete it from ch01 and ch02. Recommend deleting: the heading already says Learning goals and the stem costs a line in every chapter. Then reduce ch02's six goals to three by merging (constraints/feasibility into one, predictions/values into one, information/robustness into one) and ch01's four to three.  *(effort: small)*

### [LOW · structure] ## Learning goals

> Construct alternatives without treating constraints as a separate item from feasibility

**Problem.** Six learning goals where the established template uses three, and two of them are phrased as negatives about a mistake the reader has not yet made ("without treating constraints as a separate item," "without double-counting" in Ch. 1). A reader meeting these before the chapter cannot parse what is being warned against, so the goals function as a preview of the author's concerns rather than as a statement of what the reader will be able to do.

**Edit.** Reduce to three or four positively framed goals covering the chapter's actual deliverables: construct a feasible set larger than the visible menu; name the best forgone path and the information that could change the ranking; and state a recommendation as a conditional claim with its reversal threshold. Fold the constraint point into the body text where it is already explained.  *(effort: small)*

---

## `chapters/03-attention-what-becomes-evidence.qmd`  (18 findings)

### [HIGH · engagement] ## Inattentional blindness: what attention leaves out

> participants who were counting passes often failed to notice an unexpected person

**Problem.** The most famous number in cognitive psychology is replaced by "often." The chapter opens with a second-person hook that puts the reader inside the task, then resolves it with a quantifier that could mean anything from 15% to 85%. A reader who does not click the video link finishes the section without ever learning what happened.

**Edit.** State the rate: across conditions in Simons and Chabris (1999), 46% of observers failed to report the gorilla, and the miss rate was highest when the counting task was hardest. Add the detail that makes it unforgettable — the gorilla walked to the centre of the scene, faced the camera, thumped its chest, and left, on screen for about nine seconds. Verify the exact figures against the paper; the point is that the sentence must carry a number.  *(effort: small)*

### [HIGH · engagement] ## Change blindness

> people giving directions to a stranger often failed to notice when the stranger was replaced

**Problem.** The Simons and Levin (1998) study is described with its physical comedy removed and its numbers omitted. Appendix D (index of major course examples) lists this chapter's exemplar as "Invisible gorilla and the door swap" — but the door never appears in the chapter, so the book's own index promises an image the chapter does not contain. "A brief interruption" is doing a great deal of concealing work here.

**Edit.** Restore the scene and the number in two sentences: an experimenter stops a pedestrian on campus to ask directions; two workers carrying a door walk between them; behind the door the experimenter is swapped for a different person, in different clothes, of different height and build, with a different voice. Fewer than half of the pedestrians reported noticing. Then note the moderator that makes it a decision lesson rather than a stunt: detection was much higher when the experimenters belonged to the pedestrian's own social group, because that is what determines the category the observer encoded.  *(effort: small)*

### [HIGH · engagement] ## Attention under divided demand

> but also the learning of nearby students who could see the screen

**Problem.** Sana, Weston, and Cepeda (2013) is the chapter's most decision-relevant and most surprising result — that your laptop damages the learning of the person sitting behind you more than your own — and it is stated without a single number, in the middle of a three-study paragraph, in a subordinate clause. The whole multitasking section contains no quantities at all: "often learn less," "poorer academic performance," "poorer comprehension," "can impair driving performance."

**Edit.** Give this study its own two sentences with the effect sizes: multitaskers scored roughly 11% lower on a comprehension test, and students merely seated in view of a multitasking screen scored roughly 17% lower — worse than the multitaskers themselves. Then state the implication the chapter is uniquely positioned to draw and currently omits: the cost of divided attention is partly externalized onto people who made no such choice, which makes it an attention-architecture problem (a room policy) rather than a personal-discipline problem. Verify both percentages against the paper.  *(effort: small)*

### [HIGH · engagement] ## Watch and test: what did your model preserve?

> Before replaying it, write down the details you believe remained stable.

**Problem.** The book's single best engagement device — commit to an answer before the reveal — appears about ten times across 42 chapters under seven different titles ('Watch and test', 'Calibration test', 'Try the social prediction', 'Watch and diagnose', 'Watch for the mismatch', 'Check your denominator', 'Before reading on…') and four different classes (.watch-and-test, .calibration-test, .media-example, and none). how-to-use-this-book.qmd promises this layer, but the reader has no way to see where an invitation to predict begins.

**Edit.** Create .predict-first: amber border #c9a227, bg #fffdf2, circled-question icon, standing label 'PREDICT FIRST — write your answer before reading on'. Apply to ch03:86, ch03:133, ch04:202, ch10:59, ch14:173, ch26:94, ch34:51, ch37:36, ch39:222. Then extend the device to the chapters that most reward it and currently lack it — ch17 before the fourfold pattern, ch26 before the Asch rates, ch28 before the Milgram numbers, ch11 before the anchoring result.  *(effort: medium)*

### [HIGH · insight] ## Change blindness

> but every target also has a cost: it can draw attention away from something else

**Problem.** This clause states the chapter's deepest idea — that there is no free detection, so assigning a search target does not improve attention, it reallocates it and manufactures a new blind spot — and it appears once, in a subordinate clause, and is never named or developed. The chapter's design section then offers four moves without ever telling the reader that each one buys detection somewhere by spending it elsewhere. The result is that "Designing better attention" can be read as a list of improvements rather than as a set of trades.

**Edit.** Name it as a principle and place it at the head of "Designing better attention": attention is allocated, not increased, so every design choice is a trade — and the honest question is not "what are we missing?" but "what are we willing to miss?" Then make each of the four moves state its cost explicitly (assigning an anomaly role means that person is not doing the primary analysis; a second pass costs the time that would have gone into the first). This also strengthens the Practice Lab, which already asks the right question — whether a redesign improved detection "rather than merely shifting the blind spot" — but asks it without having given the reader the concept.  *(effort: medium)*

### [HIGH · insight] After '## Top-down goals and bottom-up capture' (line 44-55), before '## Attention under divided demand'

> A phone notification, a flashing advertisement, a crying baby, a sharp tone

**Problem.** This is the book's largest genuine topic gap. The attention chapter treats attention as a capacity problem and an organizational-design problem, but never as an economic one: it lists a phone notification beside a crying baby as if both were accidents of the environment. Nobody in ch3 is paying for the reader's attention. 'attention economy', 'infinite scroll', and 'recommender' appear zero times in the chapter; the only treatment anywhere is ~250 words in ch40 ('Digital architecture operates at full-path scale') and a passing phrase in ch13 about 'algorithmic exposure'. Nothing connects them, and no chapter states that the reader's default informational environment is engagement-optimized and adversarial. For a 2026 book on decisions, that omission is more conspicuous than any of the classic topics.

**Edit.** Add ~800 words as '## When your attention is the product'. Open with the business model in one sentence, then draw the distinction the chapter already has the machinery for: a cue that happens to capture attention versus a cue selected because it captures attention. Carry published numbers, which is exactly the concreteness fix the project needs: Allcott, Braghieri, Eichmeyer & Gentzkow (2020, AER) randomized 2,743 people to four weeks of Facebook deactivation — about one hour per day freed, subjective well-being up roughly 0.09 SD, and reduced post-experiment use — alongside the contested size of such effects. Close with two forward links: to ch21 for the cue-routine loop the design exploits, and to ch40's full-path audit for what to do about it.  *(effort: medium)*

### [MEDIUM · accuracy] ## Attention under divided demand

> Junco and Cotten (2012) found that multitasking with technology was associated with

**Problem.** The paragraph is careful — "associated with" for the correlational study, "experimentally varied" for Gingerich and Lineweaver — but the distinction is carried by two words a reader will not register, and the three studies are presented as a single accumulating case. The middle study (Sana et al.) is experimental but its design is not described, so the reader cannot tell that the paragraph moves from correlation to causation. Given the book's front-matter commitment to evidence literacy, this is a missed opportunity rather than an error.

**Edit.** Add a five-word design tag to each: "in a survey of 1,774 students, Junco and Cotten (2012) found that self-reported multitasking was associated with…"; "in a controlled experiment, Sana, Weston, and Cepeda (2013) assigned students to multitask or not and found…"; "Gingerich and Lineweaver (2014) experimentally varied…". Then one closing sentence: the correlational and experimental results point the same way, which is more than either supplies alone.  *(effort: small)*

### [MEDIUM · clarity] ## Practice Lab

> Audit one consequential meeting, class, dashboard, or screening process.

**Problem.** Not one of the 42 Practice Labs states a time budget. A grep for any minute or hour figure near lab, activity, exercise or studio returns nothing across all 42 chapters. The only duration anywhere is inside a title ('Ten-Minute Noise-Audit Lab', ch41:102). Readers and instructors must therefore guess whether a lab is a 15-minute exercise or a two-hour workshop, and the labs genuinely range across that whole span.

**Edit.** Append a single italic line to each lab: '*About 30 minutes, alone.*' or '*About 40 minutes; the group version adds 20.*' Suggested budgets: 20 min (ch03, ch12, ch20, ch33), 30 min (ch01, ch04, ch05, ch06, ch08, ch09, ch10, ch11, ch13, ch17, ch18, ch26, ch27, ch29, ch31, ch34, ch35, ch38), 40 min (ch02, ch07, ch14, ch15A, ch16, ch19, ch22, ch23, ch24, ch25, ch28, ch30, ch32, ch36, ch37, ch39, ch40, ch41, ch42).  *(effort: small)*

### [MEDIUM · consistency] ## References cited in this chapter

> Attwell, D., & Laughlin, S. B. (2001). An energy budget for signaling in the grey matter

**Problem.** This chapter's reference list breaks the book's formatting convention. Chapters 1 and 2 italicize journal titles and volume numbers (*Journal of Consumer Research, 36*(4)); Chapter 3 leaves almost all of them unformatted, except for three entries (Gracheva, Payne, and the italicized species name in Payne) which do follow the convention and also carry DOIs that the others lack. Alphabetical order is also broken: Gracheva et al. is placed before Gingerich and Lineweaver.

**Edit.** Apply the book's reference format to all 29 entries — italicize journal title and volume, add DOIs where the other chapters carry them — and move the Gracheva entry after Gingerich. Worth a pass across all chapters at once if this pattern recurs elsewhere in the manuscript.  *(effort: medium)*

### [MEDIUM · engagement] ## Inattentional blindness: what attention leaves out

> Eighty-three percent did not report it during the search

**Problem.** The Drew, Võ, and Wolfe (2013) paragraph reports the percentages correctly and notes the eye-tracking result — genuinely good, careful work — but omits the one detail that makes the study land: the gorilla image was about 48 times the size of the average nodule the radiologists were hunting. Without it, a reader can rationalize the miss as a small stimulus in a noisy image, which is exactly the wrong inference.

**Edit.** Add the size comparison in the same sentence that introduces the manipulation: "inserted a gorilla image roughly 48 times the size of the average nodule into the final lung scan." Then keep the existing eye-tracking sentence, which becomes far more striking once the reader knows the size — trained experts fixated something 48 times larger than their target and did not report it.  *(effort: small)*

### [MEDIUM · engagement] Opening scenario

> Follow its counting instructions, then compare what you noticed with what was present.

**Problem.** The chapter's hook depends entirely on an external YouTube link to deliver its payoff. A reader on paper, offline, or simply unwilling to stop reading gets a question with no answer, and the third paragraph resolves the setup into pure abstraction ("Doing the task well may still leave us unprepared for a decision that depends on an unexpected event") without ever saying what was in the scene. The link may also break; the chapter carries three video URLs total.

**Edit.** Keep the link as an invitation but make the text self-sufficient: after the counting question, add a line break and one short paragraph that says what happens — a person in a gorilla suit walks into the middle of the game, stops, faces the camera, thumps its chest, and walks off, and about half of viewers counting passes do not see it. The reader who clicked has still had their chance; the reader who did not now has the chapter's central image.  *(effort: small)*

### [MEDIUM · engagement] ## Available information is not complete information

> We can see a confident presenter but not long-run reliability

**Problem.** This is the best sentence in the chapter — four paired contrasts that convert an abstract epistemic point into four immediately recognizable decision failures — and it is buried in the middle of the section's longest paragraph, after the bees, snakes, elephants, and migratory birds. A reader skimming the paragraph will take away the animal sensory examples, which are charming but decision-irrelevant, and miss the sentence that does the actual work.

**Edit.** Break the paragraph and lead the new one with the four contrasts, then draw the conclusion. Consider adding a fifth pair that names the chapter's own running concern: "a quarterly revenue figure but not the customer who quietly stopped renewing." Keep the closing bolded question where it is — it is a strong section ender.  *(effort: small)*

### [MEDIUM · engagement] ## Attention under divided demand

> showed that cell phone conversations can impair driving performance

**Problem.** Two driving studies are compressed into two sentences with no quantities, and the more important of the two findings — that hands-free conversation is roughly as impairing as handheld, which contradicts most people's intuition and most road legislation — is stated as a double negative ("does not eliminate the attentional cost") rather than as the surprise it is.

**Edit.** Give the numbers and state the surprise directly: in Strayer and Johnston (2001), drivers conversing on a phone missed roughly twice as many simulated traffic signals and reacted more slowly to those they did detect, and the impairment was essentially the same whether the phone was handheld or hands-free. Then make the decision point explicit: the widespread hands-free legal exemption targets the hands, while the evidence locates the cost in attention — a case where a policy tracks the visible feature rather than the causal one.  *(effort: small)*

### [MEDIUM · engagement] ### Attention architecture: the organization chooses what can be seen

> become the meeting’s invisible gorilla

**Problem.** The cost-cutting meeting example is the chapter's best piece of transfer — it converts a laboratory demonstration into a recognizable organizational failure and closes the loop back to the opening — and it is placed after a five-row table, in the middle of the design section, where it reads as an illustration of the table rather than as the chapter's payoff. The reader has already been given the design moves and the architecture table before being shown why any of it matters in a room.

**Edit.** Move the cost-cutting scenario to the head of "Designing better attention," before the four moves, so it motivates them rather than illustrating them. Expand it by one sentence naming a consequence the narrow question produced — a supplier switch that saved a stated amount and cost a delivery window — so the invisible gorilla has a price. The architecture table then reads as the diagnosis of a failure the reader has just watched happen.  *(effort: small)*

### [MEDIUM · structure] ## Attention under divided demand (Research note callout)

> Research note: two very different information rates

**Problem.** The Zheng and Meister callout sits between this section's topic sentence about divided demand and the classroom evidence that tests it. The reader is pulled into a bits-per-second digression about sensory bandwidth, then returned with a recovery line — "The classroom provides a more direct test of divided demand" — which quietly admits the interruption. The callout's content also belongs conceptually with "Available information is not complete information," which is about the gap between what is available and what is used.

**Edit.** Move the callout (and @fig-attention-bottleneck) to the head of "Available information is not complete information," where the bandwidth contrast directly motivates the Umwelt argument, and delete the recovery sentence. The divided-demand section then runs cleanly from capacity limits to the classroom and driving evidence.  *(effort: small)*

### [MEDIUM · visual] ## Change blindness

> large changes can go unnoticed when attention is not directed to the changing feature

**Problem.** Change blindness is the one phenomenon in this chapter that genuinely cannot be conveyed in prose, and it is the only major section with no figure, table, or diagram — a stretch of about 700 words between @fig-attention-bottleneck and @fig-attention-filter that asks the reader to imagine a visual effect. The two video links do the work a book figure should be doing, and they will rot.

**Edit.** Add a diagram of the flicker paradigm rather than an attempt at the illusion itself: a horizontal sequence of four panels — scene A, blank grey field, scene A′, blank grey field — with a looping arrow underneath, and a single small caption line noting that the change in A′ is marked in the alt text but not in the figure. Beside it, a short vertical annotation explaining why the blank field defeats detection: the transient that normally captures attention is masked, so the observer must compare A′ against what was actually encoded and retained. Caption states the claim: "Detecting a change requires having encoded the changed feature — looking at the scene is not enough."  *(effort: large)*

### [LOW · consistency] ## Attention failures and design responses (table label)

> : Attention failures and design responses {#tbl-05-1}

**Problem.** A stale label from when this was Chapter 5 (confirmed by the file's alias, 05-attention-is-the-gatekeeper-of-evidence.html). It is also the only non-descriptive table ID in these three chapters — the other table in the same chapter uses {#tbl-attention-architecture} — and a positional name like tbl-05-1 risks colliding if any other chapter adopts the same scheme.

**Edit.** Rename to {#tbl-attention-failures}. I checked: no file in the repository references tbl-05-1, so the rename is safe. Worth grepping the manuscript for other tbl-NN-N labels at the same time.  *(effort: small)*

### [LOW · consistency] ## Learning goals

> - Explain inattentional blindness and change blindness.

**Problem.** This chapter's learning goals begin immediately with bullets, while Chapters 1 and 2 both open with the stem "After reading this chapter, you should be able to:". Small, but the template is otherwise followed exactly across the book, and a missing stem in Chapter 3 is where a reader would first notice inconsistency.

**Edit.** Add the stem sentence. Also consider whether the three goals cover the chapter as delivered: the second half of the chapter is substantially about attention architecture as an organizational design problem, which the third goal gestures at ("Redesign an information environment") but does not name. A fourth goal — "Audit how an agenda, metric, or role assignment allocates attention before anyone reasons" — would match what the chapter actually teaches.  *(effort: small)*

---

## `chapters/04-the-predictive-mind-perception-is-inference.qmd`  (14 findings)

### [HIGH · accuracy] ## When context changes what appears (and ### Learned context gives color a meaning)

> The context tells us what the sensory evidence is likely to mean.

**Problem.** The chapter's central empirical claim — that context changes what *appears* — is asserted without engaging the major live objection: that many demonstrated 'top-down' effects are post-perceptual (judgment, memory, response bias, or the wording of the task) rather than changes in perception itself. Firestone & Scholl's 2016 BBS target article is the standard citation for this and appears nowhere in the book; only Valenti & Firestone (2019) appears, buried in footnote ch04-color-cues. For a book whose voice is built on distinguishing what a study showed from what people infer from it, this is the one place the chapter does not apply its own standard.

**Edit.** Add a short paragraph (4-5 sentences) at the end of 'When context changes what appears', before the subsections, and promote the footnote caveat into it. Something like: 'A caution belongs here. Showing that context changes what someone *reports* does not by itself show that it changed what they *saw*. Firestone and Scholl (2016) argue that many reported top-down effects can be explained by judgment, memory, task demands, or the wording of the question rather than by altered perception. The demonstrations below are best read as evidence that interpretation depends on context; how much of that dependence sits inside vision remains contested.' Add Firestone, C., & Scholl, B. J. (2016). Cognition does not affect perception: Evaluating the evidence for 'top-down' effects. *Behavioral and Brain Sciences, 39*, e229. This strengthens rather than weakens the chapter, and it sets up the hollow-face section, where the knowledge/percept dissociation cuts the other way.  *(effort: medium)*

### [HIGH · clarity] ## Prediction, error, and precision

> Precision means estimated reliability, often formalized as inverse variance.

**Problem.** Precision-weighting is the chapter's most consequential technical idea — it is what the 'reliability is judged selectively' failure mode and the whole Calibration test depend on — and it is taught entirely in words, with 'inverse variance' introduced as bare jargon and never unpacked. A business-school reader gets no feel for how much a difference in reliability actually changes the weighting, so 'a signal treated as more reliable has greater influence' stays a slogan.

**Edit.** Add a three-line worked number immediately after the definition, using the chapter's own kitchen: 'Suppose memory places the chair at 60 cm from the wall, give or take 5 cm, while a glimpse in dim light places it at 90 cm, give or take 50 cm. Inverse variance weights these 1/25 against 1/2500 — the memory carries a hundred times the weight, and the combined estimate lands near 60 cm. Switch on the light and the glimpse tightens to give or take 3 cm; now the same eyes overturn the same memory.' This makes the later claim about selectively judged reliability land as arithmetic rather than exhortation, and it costs no accuracy.  *(effort: small)*

### [HIGH · engagement] ## When context changes what appears

> Other demonstrations use shadows, shading, or synchronized touch to show how sensory signals are organized

**Problem.** This single abstract sentence disposes of three of the most vivid demonstrations in all of perception research — Adelson's checker-shadow illusion, Ramachandran's shape-from-shading, and the rubber-hand illusion — as a citation list. The reader who does not already know them learns nothing, and the reader who does gets no payoff. It is the flattest sentence in a chapter otherwise built on demonstrations the reader performs.

**Edit.** Replace with one concrete sentence per demonstration, each naming the surprise: 'In Adelson's checkerboard, a square in shadow and a square in light print the same gray on the page, yet almost no one can see them as equal — the visual system has already corrected for the shadow it inferred (Adelson, 2000). In Ramachandran's arrays, a field of shaded discs flips from bumps to dimples when the page is turned upside down, because the interpretation assumes light comes from above (Ramachandran, 1988). In the rubber-hand illusion, watching a visible rubber hand stroked in time with your own hidden hand can make the rubber hand feel like yours (Botvinick & Cohen, 1998).' Also reorder the parenthetical citations alphabetically if they are kept in any collapsed form.  *(effort: small)*

### [HIGH · visual] ## Prediction, error, and precision (fig-predictive-processing-decision)

> A simplified predictive-processing account. Expectations and incoming signals both contribute to perception

**Problem.** @fig-predictive-processing-decision is the chapter's only conceptual diagram and the only visual that carries the machinery rather than a demonstration, yet it is never referenced in the prose — I checked every @fig- call in the file. The four other figures are all introduced and worked through. The reader arrives at an unexplained box-and-arrow diagram right after three technical terms are defined in three consecutive paragraphs.

**Edit.** Add a cross-referencing sentence that walks the loop once in the kitchen's terms, placed just before or after the figure: '@fig-predictive-processing-decision puts these terms in one loop. Your model predicts a chair at the usual spot; the incoming outline disagrees; how much that mismatch counts depends on the precision assigned to the outline; and the action it prompts — taking two steps closer — changes the evidence that arrives next.' The last clause is also the hinge into the active-inference Research Lens that follows, so this repairs a transition as well as a figure reference.  *(effort: small)*

### [MEDIUM · clarity] ## Learning goals, goal 2

> Describe priors, sensory evidence, prediction error, and precision in plain language.

**Problem.** All three of chapter 4's goals sit at the lowest cognitive level in the book — Explain, Describe, Distinguish — while the chapter actually contains a Calibration Test the reader completes and a Practice Lab that demands 'Produce a two-model test' with a discriminating observation and a branched action. 'Describe … in plain language' is the only Describe verb in 130 goals and it understates what the chapter asks for.

**Edit.** Rewrite as: (1) 'Explain perception as inference rather than recording, and say what the technical use of prediction here does not mean.' (2) 'Use priors, sensory evidence, prediction error, and precision to account for one disagreement in which two people saw the same thing differently.' (3) 'Construct a two-model test: name the observation each account predicts and the action that follows each result.' Goal 3 now names the artifact the Practice Lab actually requires.  *(effort: small)*

### [MEDIUM · consistency] ## Research Lens: Shirl Jennings and learning to see

> Research Lens: Shirl Jennings and learning to see

**Problem.** This is the only Research Lens in these two chapters — and, on a check across the book's chapters, apparently the only one anywhere — that is a bare level-2 heading rather than a ::: {.callout-note .research-lens icon=false} block. The chapter's other three Research Lenses are all callouts. Rendered, it will read as ordinary chapter body under a heading that promises a styled aside, and it loses the visual signal that this is bounded evidence rather than the main argument. Two factual details in it also warrant a check.

**Edit.** Wrap the section in ::: {.callout-note .research-lens icon=false} (collapse=false is appropriate here, since the Jennings case carries argumentative load and should stay open), keeping the existing anchor ID so cross-references survive. While editing: (a) verify 'In 1991, at age 51' — Sacks describes Virgil as fifty at the time of surgery in 'To See and Not See', so confirm which source the age comes from and reconcile; (b) replace 'then improved rapidly' with the timescale Held et al. (2011) actually report, so the reader learns how fast perceptual learning went, not merely that it did.  *(effort: small)*

### [MEDIUM · engagement] ### One drawing, two animals

> Zurich Zoo visitors tested on Easter Sunday predominantly named a rabbit

**Problem.** The sentence promises 'a striking seasonal pattern' and then withholds every number that would make it striking. 'Predominantly' does the work that percentages should do, and the reader cannot judge how large the contrast was — which also makes the subsequent failed replication harder to weigh. The sample description ('Zurich Zoo visitors') is stated without ages or n, and it is worth confirming against the original, since the replication's title ('Replication is child's play') suggests a child sample.

**Edit.** State the reported figures and sample in the sentence: '... of the N visitors tested on Easter Sunday, X% named a rabbit; of the N tested on a Sunday in October, Y% named a bird.' Verify the percentages, the n for each date, and whether participants were children, adults, or both, directly against Brugger & Brugger (1993), and mirror the same two numbers for Dudda et al. (2026) so the reader can see exactly how the replication differed rather than being told 'the evidence for a seasonal influence is mixed.'  *(effort: small)*

### [MEDIUM · engagement] Opening scenario (before ## Core Idea)

> This chapter asks how expectations help construct perception—and what allows evidence to correct it.

**Problem.** The opening is a competent but low-stakes scene — a dim kitchen, a possible chair — and it closes on a signpost announcing what the chapter will do rather than on the reason the reader should care. Nothing is at risk. Compare Chapter 3's opening, which hands the reader a task, a link, and an immediate personal failure. Here the second paragraph's most concrete sentence is an abstraction ('The difficulty is knowing when to act on what seems obvious').

**Edit.** Keep the kitchen as the tactile entry, then raise the stakes in one sentence before the Core Idea, and cut the signpost. For example, end paragraph two with a consequential instance drawn from material the chapter already owns: '...the difficulty is knowing when to act on what seems obvious. The stakes rise with the setting. A radiologist reading a scan, a driver resolving a shape at dusk, and a manager reading a quiet meeting are all doing what you just did in the kitchen: committing to an interpretation before the evidence is sufficient to compel it.' Delete 'This chapter asks how expectations help construct perception—and what allows evidence to correct it' — the Core Idea callout immediately below already says it better.  *(effort: small)*

### [MEDIUM · insight] ### A hollow face that seems to look back

> Even knowing that the mask is hollow need not make it look hollow

**Problem.** The chapter has assembled the material for its sharpest distinction and then walks past it. The hollow face shows that a prior built from a lifetime of face exposure is not overturned by explicit propositional knowledge — which is exactly the opposite of what the chapter's practical advice ('recognize what you expected') might lead a reader to hope. The sentence states the fact and moves on to lighting and stereopsis; the implication for decision-making is left implicit, and the later claim that 'an impression can remain convincing even after another observation reveals why it is misleading' is asserted without connecting it back to this asymmetry.

**Edit.** Add two sentences after the Hill & Johnston citation making the distinction explicit: 'Note which kind of expectation wins. A prior built from years of seeing faces reshapes what you see; a fact you were told thirty seconds ago does not. That asymmetry is the practical warning: telling yourself you are probably biased is a weak intervention compared with changing what you observe.' This also creates a clean bridge to the 'Action protects the model' obstacle later in the chapter and to the Calibration test's insistence that 'use less intuition' is not yet a test.  *(effort: small)*

### [MEDIUM · insight] ## When inner models help—and when they stop learning

> A radiologist sees structure in an image that a novice cannot

**Problem.** This is a clean available connection to Chapter 3, left unmade. Chapter 3 reports Drew, Vo, and Wolfe (2013): 83% of 24 radiologists missed a gorilla image inserted into lung scans while searching for nodules, and most had looked directly at it. That is the same expert prior, producing both the skill and the blindness, in the same profession — the counterintuitive implication the chapter needs and does not state.

**Edit.** Extend the sentence and cross-link: 'A radiologist sees structure in an image that a novice cannot — and, as [Chapter 3](03-attention-what-becomes-evidence.qmd) showed, the same trained search can leave a conspicuous unexpected object unreported. A model that makes the expected signal legible is also a model that assigns low precision to whatever it did not anticipate. Expertise buys interpretation at the cost of a narrower set of things that can surprise you.' Use the book's established inline link convention (as in the [Chapter 42] link later in this file).  *(effort: small)*

### [MEDIUM · visual] ## When inner models help—and when they stop learning

> The prior becomes too rigid. Ambiguous evidence is repeatedly interpreted in the expected direction.

**Problem.** This section runs roughly 1,100 words from the predictive-processing figure to the Calibration test with no figure or table, and its two adjacent lists — three obstacles, then five calibration questions — cover overlapping ground in two different formats. The reader has to hold the three failure modes in memory while reading five questions that map onto them only loosely, so the section's most usable content arrives as prose the reader cannot act from.

**Edit.** Convert both lists into one four-column table titled 'Three ways a model stops learning' with rows Rigid prior / Selective precision / Model-protecting action, and columns: What goes wrong | How it shows up in a team | Diagnostic question | Action that tests rather than protects. Populate the third column from the existing bullets ('Which observation would be more likely if my model were wrong?', 'Why am I treating one signal as reliable and another as noise?', 'What feasible action would test the model rather than protect it?') and the second column from the existing organizational examples (silence read as agreement, strategic behavior read as personality). This supplies the section's missing visual relief and turns an abstract list into the chapter's one portable tool.  *(effort: medium)*

### [LOW · engagement] ## Learning goals (closing paragraphs, before ## Two meanings of prediction)

> Predictive processing offers one influential family of models for how expectations and incoming signals

**Problem.** A one-sentence orphan paragraph that announces a topic instead of advancing one; the reader is told a family of models exists and then sent to a different section. The same habit recurs at 'This chapter concentrates on interpreting current signals. The later chapters on expectations and probability judgment ask how people forecast consequences,' where 'the later chapters' is vague in a book that elsewhere links specific chapters by number and anchor.

**Edit.** Fold the orphan sentence into the end of the preceding paragraph ('...helps make a chair a plausible interpretation. Predictive processing, discussed below, offers one influential family of models for how expectations and incoming signals interact.'). And name the chapters in the second instance: 'Chapter 5 asks when a forecast can change what it forecasts; Chapters 14 and 15 supply the probability and calibration tools' — using the inline link form already used for [Chapter 42] later in this file. Chapter 5 uses the bare 'Chapters 14 and 15' style, so at minimum make the two chapters consistent.  *(effort: small)*

### [LOW · engagement] ### Learned context gives color a meaning (Bloj et al. card)

> changing the perceived folding direction of a card changed its apparent color

**Problem.** The description is accurate but so abstract the reader cannot picture the stimulus or the surprise. 'A card' with an unspecified 'folding direction' and an unspecified color change is a summary of a demonstration rather than the demonstration. This is the third consecutive paragraph in the colour subsection with no imageable object.

**Edit.** Name the physical setup in one clause: Bloj et al. used a card folded so that a coloured face bounced light onto a white face; viewed through a pseudoscope that reversed the apparent fold, the white face no longer looked tinted, because the visual system no longer had a reason to attribute the tint to light bouncing between surfaces. State the actual colours and the direction of the change from the paper, then keep the existing closing sentence ('The familiar object and the light falling on it jointly inform the interpretation'), which is a good line currently attached to nothing concrete.  *(effort: small)*

### [LOW · visual] ## When context changes what appears (fig-perception-context-lab caption)

> Three perceptual demonstrations hold a measurable target constant while changing its context

**Problem.** The caption describes the construction of the figure but never states its takeaway, so a reader skimming captions learns what the panels contain and not what they establish. The neighbouring caption for fig-context-b13-demonstration does state a claim ('Number context invites a reading of "13," while letter context invites a reading of "B"'), which makes the inconsistency visible within a single page.

**Edit.** Lead the caption with the claim and keep the construction as the second sentence: 'Identical targets can look different when their surroundings change — and measuring the target corrects the judgment without dissolving the impression. Three panels hold a measurable target constant while changing its context: equal line shafts receive different fins, equal centre circles receive differently sized neighbours, and identical grey patches appear on dark and light fields.' The fig-alt is strong and needs no change.  *(effort: small)*

---

## `chapters/05-expectations-when-predictions-become-causes.qmd`  (15 findings)

### [HIGH · accuracy] ## Ability beliefs and performance

> Later reviews find moderate teacher expectancy effects that vary across settings

**Problem.** This misstates Jussim & Harber (2005). Their conclusion is that classroom self-fulfilling prophecies are real but typically small, that they do not reliably accumulate over time and often dissipate, that teacher expectations predict achievement mostly because they are largely accurate rather than because they create it, and that effects may be larger for stigmatized groups. 'Moderate' inverts the headline. The preceding sentences also present the original Pygmalion result without the methodological criticism it has attracted — the IQ gains were concentrated in grades 1 and 2, and the TOGA instrument produced some implausible scores at the extremes — which matters because this is the single most-cited and most-overextended finding in the chapter.

**Edit.** Rewrite as: 'Later work substantially qualified the result. Jussim and Harber (2005) concluded that teacher-expectancy self-fulfilling prophecies are real but typically small, that they tend not to accumulate and often dissipate, and that teacher expectations predict achievement largely because they are reasonably accurate rather than because they create the outcome — while noting that effects may be larger for students from stigmatized groups. The original study's gains were also concentrated in the youngest grades and rested on test scores that have been questioned.' This keeps the chapter's point (expectancy is one causal pathway among several) while removing the overstatement, and it strengthens rather than weakens the 'pair expectations with support' conclusion.  *(effort: medium)*

### [HIGH · accuracy] ## Ability beliefs and performance

> McNatt’s (2000) meta-analysis found evidence for Pygmalion effects in management contexts.

**Problem.** This sentence gives no effect size and, more importantly, no boundary condition — and the boundary conditions are the story. Eden's Pygmalion field experiments were conducted largely in the Israel Defense Forces, a highly hierarchical setting with a predominantly male, young, trainee population and unusually strong control over leader-subordinate assignment. McNatt's meta-analysis reported a substantial overall effect but with large moderators: effects were markedly stronger in military settings, stronger for men, and stronger when initial expectations of the subordinate were low. Presenting this as 'evidence for Pygmalion effects in management contexts' invites a reader to transport a military-training result into a civilian workplace, which is the generalization the meta-analysis specifically cautions against.

**Edit.** Replace with a sentence that reports the estimate and the moderators: 'McNatt (2000) meta-analysed these studies and reported a substantial average effect, but one that varied sharply by setting: it was largest in military training contexts, where much of Eden's original work was conducted, larger for men, and larger where initial expectations of the subordinate were low. Whether the same leverage is available in a civilian organization with voluntary employment and weaker control over assignment is a separate question.' Verify the reported overall d and the moderator directions against the paper before publishing the numbers. This also sets up the ethics paragraph that follows ('should not mean pressure without support') on firmer ground.  *(effort: medium)*

### [HIGH · clarity] ## Build the forecast before telling its story

> If only 35% of comparable launches reach that retention target, the team needs

**Problem.** The chapter's one extended worked example has a hole in the middle. The table asserts a 45% probability; the text then names a 35% reference-class base rate and says diagnostic evidence is needed 'before moving far from that base rate' — but the 10-point move has already been made in the table, and the reader is never shown what justified it. This is exactly the inside-view/outside-view reasoning the section is teaching, and it is the step that gets skipped. A reader who tries to do this for their own decision has no model to copy.

**Edit.** Add a short numbered walk-through after the 'Neither should automatically defeat the other' sentence, tying the two numbers together: '(1) Start at the reference class: 35% of comparable first releases held 90% of paid users at 90 days. (2) Ask what is different here and whether the difference is documented: this release ships with an onboarding flow that cut 30-day drop-off from X% to Y% in the beta, a feature absent from the comparison cases. (3) Ask what is worse here: support headcount is one person short of the comparison launches. (4) Net the two and state the move: 35% up to roughly 45%, with the range 30-60% carrying the uncertainty in both adjustments.' The specific numbers can be illustrative and labelled as such; the point is that the reader sees an adjustment being defended rather than announced.  *(effort: medium)*

### [MEDIUM · accuracy] ## Ability beliefs and performance (self-efficacy paragraph)

> Self-efficacy affects effort, persistence, resilience, emotional response, and willingness to take on challenge.

**Problem.** 'Affects' is a causal verb applied to a literature that is predominantly correlational and has a well-known reverse-causation problem: past performance is one of the strongest determinants of efficacy beliefs, so cross-sectional associations between efficacy and performance are partly performance predicting itself. The chapter is careful about exactly this elsewhere ('Nor does a predictive association establish which intervention will improve the outcome'), which makes the lapse conspicuous. There is also a genuinely counterintuitive within-person literature the chapter could use: when self-efficacy is analysed within person rather than between people, higher efficacy has sometimes predicted *lower* subsequent effort and performance, apparently through overconfidence and reduced resource allocation (Vancouver and colleagues).

**Edit.** Change 'affects' to 'is associated with' and add two sentences: 'Much of this evidence is correlational, and causation runs in both directions — past success is one of the strongest sources of efficacy beliefs, so the association partly reflects performance predicting itself. Studies that analyse change within a single person have sometimes found the opposite pattern: higher confidence on a given trial predicting lower subsequent effort, apparently because the person judged less effort to be needed.' This deepens rather than dilutes the section's actual conclusion (that belief must be paired with strategy, feedback, and support) and preserves the chapter's voice.  *(effort: small)*

### [MEDIUM · accuracy] ## Expectation in the body

> Improvement in a placebo group alone does not establish a placebo effect

**Problem.** This is the right caveat, and it is stated without the evidence that makes it decisive. The systematic reviews comparing placebo to genuine no-treatment arms (Hrobjartsson & Gotzsche, 2001 NEJM and the 2010 Cochrane update) found no significant placebo effect on binary outcomes or objective continuous outcomes, with possible modest benefits confined to continuous subjective outcomes, particularly pain and nausea. That result is the single most important boundary condition in this section — it tells the reader exactly which outcomes expectation can and cannot be expected to move — and the section currently asserts the caution without it, then proceeds to pain (the one domain where the effect survives) without noting that this is not a coincidence.

**Edit.** Add after the existing caveat sentence: 'Systematic reviews comparing placebo groups with genuine no-treatment groups sharpen this. Across many conditions, placebo interventions showed little effect on objective or binary outcomes, with the clearest effects confined to continuous self-reported outcomes such as pain (Hrobjartsson & Gotzsche, 2010). Expectation moves reported experience far more reliably than it moves disease.' Then the following 'Pain research provides one example' sentence becomes an illustration of a rule rather than a free-standing anecdote. Add the Cochrane review to the reference list.  *(effort: medium)*

### [MEDIUM · accuracy] ## Research Lens: identity changes what difficulty means

> making a negative group stereotype relevant has sometimes impaired performance by changing the meaning

**Problem.** The lens is otherwise exemplary — it names heterogeneity across populations and manipulations, flags publication bias, and cites both Flore & Wicherts and Shewach et al., which is exactly the treatment this literature needs and should not be softened. The one remaining gap is that the headline result in Steele & Aronson (1995) was obtained on scores statistically adjusted for participants' prior SAT performance. The widely circulated version of the finding drops that qualifier, which is precisely the kind of study-versus-inference slippage the book elsewhere makes a point of catching.

**Edit.** Add one clause to the Steele & Aronson mention: '(the original result was obtained on test scores adjusted for participants' prior standardized-test performance, a detail often dropped when the finding is restated)'. One sentence, no change to the lens's conclusion, and it models the reading discipline the book is teaching.  *(effort: small)*

### [MEDIUM · consistency] ## Ability beliefs and performance (Yeager follow-up)

> In the follow-up covering both lower- and higher-achieving students, advanced mathematics enrollment

**Problem.** 'The follow-up' is cited as a source in the body with no reference entry and no author-date citation. Every other empirical claim in these two chapters carries a traceable citation, and the reference lists otherwise match the body in both directions, so this is the one genuine gap. The reader cannot check the 36% versus 33% figures, and cannot tell whether they come from the 2019 Nature paper itself or from a later report of the tenth-grade course-taking outcome.

**Edit.** Either attribute the figures to Yeager et al. (2019) explicitly if they appear in that paper, or name and cite the later report of the advanced-mathematics course-taking outcome from the National Study of Learning Mindsets and add it to the reference list. While doing so, state the sign of the comparison plainly — a 3-percentage-point difference on a pre-registered secondary outcome — so the reader can weigh it against the 0.10 GPA effect rather than reading two numbers in sequence.  *(effort: small)*

### [MEDIUM · consistency] line 153, Research note: learning that an action can help

> ## Research note: learning that an action can help

**Problem.** Six boxes titled 'Research note:' or 'Evidence note:' carry no class and render plain (ch03:62, ch05:153, ch06:177, ch06:219, ch07:90, ch13:140), while three identically titled 'Research note:' boxes in ch21:172, ch21:180 and ch39:58 DO carry .research-lens and render purple. Same label, two different visual treatments, within the same book.

**Edit.** Add .research-lens to all six unclassed boxes, and standardise the title prefix. Two families only: 'Research Lens:' for optional depth and 'Evidence Boundary:' for what the evidence does not support. Retire 'Research note:' and 'Evidence note:' as separate prefixes.  *(effort: small)*

### [MEDIUM · engagement] Opening scenario (before ## Core Idea)

> A manager wants to keep the work reliable while a new employee learns the role.

**Problem.** The manager and the employee have no names, no industry, no specific task, and no artifact. Every noun is a category: 'the difficult assignments', 'every small decision', 'little room for independent work'. The chapter then returns to this pair five more times as its running case, so the abstraction compounds — by the closing 'Take it forward' the reader still has nothing to picture. The mechanism described is genuinely uncomfortable and would land much harder with one specific withheld assignment and one specific written judgment.

**Edit.** Specify the case once, in the opening, and let the later references inherit it: give the manager a role and the employee a task ('Maria runs claims processing; Dev joins in March'), name the assignment she keeps ('the quarterly reconciliation, the one task that requires deciding which exceptions to escalate'), name the approval routine ('every refund over 500 euros crosses her desk'), and end with the artifact ('In the 90-day review she types: shows little initiative.'). The final sentence's question — 'how much initiative did the job allow?' — then has something concrete to bite on. Chapter 3's opening is the in-book benchmark for this level of specificity.  *(effort: small)*

### [MEDIUM · engagement] ## When a forecast enters the causal system

> His classic example was a bank run. If enough people believe a bank

**Problem.** Merton's bank run is the founding illustration of the chapter's central idea and it is told in four flat, agentless, present-tense generalizations ('enough people believe', 'they withdraw', 'their withdrawals then create'). Merton's own telling is a scene with a named bank, a named banker, and a date, and the historical record behind it supplies real numbers. As written, a genuinely dramatic mechanism — a solvent institution destroyed by a true-because-believed rumour — reads like a definition.

**Edit.** Tell it as Merton told it, in three sentences with the specifics restored: name the bank and the banker from Merton's 1948 example, place it in 1932, and follow the sequence in real time — a rumour reaches the depositors in line, the line grows because it is growing, and a bank that was solvent at nine o'clock is insolvent by closing. Then land the chapter's point on the concrete case: 'The depositors' belief was false when they formed it and true by the time they acted on it.' If a documented Depression-era failure with usable figures is preferred, use that instead and cite it — but the generic version should go.  *(effort: small)*

### [MEDIUM · insight] ## Expectations between people

> demonstrated this kind of behavioral confirmation in a classic study

**Problem.** 'Demonstrated' presents a single 1977 laboratory study with roughly fifty dyads as settled, in a chapter that elsewhere is scrupulous about replication and single-study evidence. The chapter also passes up the argument that would actually secure the claim: behavioral confirmation is supported by the Harris & Rosenthal (1985) meta-analytic mediation work already cited earlier in this same chapter, so the point does not need to rest on Snyder et al. at all. As it stands the strongest section of the chapter's interpersonal argument is propped on its weakest evidentiary base.

**Edit.** Hedge the verb and connect the two citations: 'Snyder, Tanke, and Berscheid (1977) reported an early laboratory demonstration of behavioral confirmation...' and then add after the description: 'A single small study from 1977 would not settle much on its own. What makes the pattern credible is the accumulated mediation evidence reviewed earlier: expectancy effects travel through specific, measurable behaviors — warmth, question-asking, response opportunities, feedback — and those behaviors change what the other person does (Harris & Rosenthal, 1985).' This is a case where the more honest version of the claim is also the more persuasive one.  *(effort: small)*

### [MEDIUM · structure] ## Expectation in the body (fig-expectation-loop and tbl-08-expectation-pathways)

> In @fig-expectation-loop, one pathway may operate alone, or several may combine.

**Problem.** The four-pathway figure and the four-pathway table are the chapter's organizing device — the Practice Lab, the Core Idea, the second learning goal, and the final ethics table all depend on them — yet both sit inside a section titled 'Expectation in the body', which announces itself as being about physiology. A reader scanning headings will find the chapter's spine filed under its narrowest instance, and the placebo discussion that follows reads as a continuation of the four-pathway framework rather than as one pathway among four.

**Edit.** Promote the figure and the pathway table into a short section of their own, '## Four pathways from expectation to outcome', placed immediately after 'Diagnose the direction of the loop' and before '## Expectation in the body'. Move the opening framing sentence ('The same challenge appears in management and education, where expectations can change both a person's response and the opportunities offered to them') up into it, and let 'Expectation in the body' begin cleanly with 'A treatment supplies more than its active ingredient' as the first pathway worked in detail. This costs no new content and makes the chapter's architecture visible in the table of contents.  *(effort: medium)*

### [MEDIUM · visual] ## Ability beliefs and performance (Sisk et al.)

> Meta-analytic work finds modest, context-dependent mindset effects (Sisk et al., 2018).

**Problem.** Four separate quantitative results — Blackwell et al.'s intervention, Sisk et al.'s two meta-analyses, Yeager et al.'s 0.10 GPA effect, and the 36% versus 33% enrollment figures — arrive as running prose in two paragraphs, with the only actual numbers being the last three. The reader cannot compare them, cannot see that the effects are consistently small, and cannot see where the moderators sit. This is also the midpoint of a roughly 1,500-word stretch between the pathway table and the closing ethics table with no figure or table of any kind.

**Edit.** Replace the numbers-in-prose with a four-row table, 'What the mindset evidence shows', columns: Study | Design and scale | Reported effect | Where it was larger or smaller. Rows: Blackwell et al. (2007) — small classroom intervention study; Sisk et al. (2018) — two meta-analyses, reporting the belief-achievement correlation and the intervention effect on achievement (verify the reported r and d); Yeager et al. (2019) — national randomized trial, 0.10 GPA points among lower-achieving students, dependent on school context; the tenth-grade course-taking follow-up — 36% versus 33%. Keep the existing closing sentence ('pair beliefs about development with real opportunities, strategies, support, and feedback') as the paragraph after the table. The table makes the honest pattern — small, real, moderated — visible at a glance, which prose spread over two paragraphs cannot.  *(effort: medium)*

### [LOW · clarity] ## Build the forecast before telling its story

> Build the forecast before telling its story

**Problem.** The heading is the reader's first navigational signal in the chapter and it is opaque: 'telling its story' has no referent yet, since the reflexivity idea that gives it meaning does not arrive until the next section. A reader scanning the table of contents cannot tell that this section is about the anatomy of a consequence forecast.

**Edit.** Retitle to something that says what the section delivers and still carries the warning — for example '## First, build a forecast that can be wrong' or '## The anatomy of a consequence forecast'. If the current phrasing is kept for its rhetorical pairing with the next heading, add a one-line orientation as the section's first sentence so the heading is decoded immediately.  *(effort: small)*

### [LOW · consistency] ## Expectation in the body / ## Building truthful, supported expectations (table IDs)

> Four pathways from expectation to outcome {#tbl-08-expectation-pathways}

**Problem.** Two table IDs carry the chapter's old number: #tbl-08-expectation-pathways and #tbl-08-1, while the file is chapter 05, its footnote uses the ch05- prefix, and its other two tables use descriptive IDs (#tbl-consequence-forecast, #tbl-self-fulfilling-self-defeating). #tbl-08-1 is additionally non-descriptive. The aliases at the top of the file confirm this chapter was previously numbered 08, so these are migration leftovers. Any future cross-reference from another chapter will be pointed at a misleading anchor.

**Edit.** Rename to #tbl-expectation-pathways and #tbl-expectation-ethical-conditions, then grep the repository for the old IDs to catch any cross-references elsewhere. While in the file, consider adding actual @tbl- cross-references in the prose — none of the four tables in this chapter is referenced by ID in the body, so Quarto's numbering is doing no work for the reader.  *(effort: small)*

---

## `chapters/06-valuation-how-options-become-worth-choosing.qmd`  (22 findings)

### [HIGH · accuracy] ## Emotion tells the mind what matters

> Bechara and colleagues (1997) developed the Iowa Gambling Task to study

**Problem.** Misattribution. The Iowa Gambling Task was introduced in Bechara, Damasio, Damasio & Anderson (1994, Cognition, 50, 7–15). The 1997 Science paper cited here is the follow-up that reported anticipatory skin-conductance responses arising before participants could state the advantageous strategy — a different contribution, and the one the sentence's surrounding claims actually rest on.

**Edit.** Correct to: "Bechara, Damasio, Damasio, and Anderson (1994) introduced the Iowa Gambling Task; Bechara and colleagues (1997) then reported that anticipatory skin-conductance responses appeared before participants could articulate which decks were advantageous." Add the 1994 Cognition entry to the reference list. While there, consider adding one clause to footnote ch06-somatic-marker naming the specific challenge — Maia and McClelland (2004, PNAS) found that with more sensitive probes participants had substantially more explicit knowledge than the original design detected — since that is the precise sense in which the 1997 headline is contested.  *(effort: small)*

### [HIGH · accuracy] ## Motives change the decision landscape

> fear increased the appeal of a popular museum, whereas a mating-related context increased

**Problem.** These are subtle-prime social-psychology experiments of exactly the kind the book elsewhere treats with caution. Chapter 13 already contains the verdict — its table row reads "Large automatic behavioral effects from subtle social primes | Many prominent claims are contested or difficult to replicate" — and mating-prime effects specifically have accumulated high-powered replication failures (Shanks et al., 2015, PLoS ONE, report repeated failures to replicate romantic-prime effects on risk and conspicuous consumption). Presenting Griskevicius et al. (2006, 2009) here with no caveat makes this the least-hedged empirical passage in a chapter that is otherwise scrupulous, and it is inconsistent with the book's own position stated seven chapters later.

**Edit.** Keep the studies but add one sentence and a pointer: "These are motive-priming experiments, and effects of this family have proved difficult to replicate at high power (Shanks et al., 2015); Chapter 13 sets out the current state of that literature." Then downgrade the following sentence from "Measuring the active motive helps explain why one appeal works better than another" to a claim about design rather than established fact — e.g. "Whether an appeal works may depend on the active motive, which is why the motive has to be measured rather than assumed." Add Shanks et al. (2015) to the reference list.  *(effort: small)*

### [HIGH · accuracy] line 149, endowment effect paragraph

> discussed again in *Framing: When the Same Facts Become Different Decisions*

**Problem.** Outright prose cross-reference error. Chapter 12 (*Framing*) never mentions the endowment effect, ownership, or Kahneman/Knetsch/Thaler — grep for "endowment" in ch12 returns nothing. The endowment effect is actually developed in Chapter 17, *Prospect Theory*, at line 212 ("### Endowment effects: giving up is not the same as owning"), which cites the same Kahneman et al. (1990) mug study that ch06 cites here. A reader who follows this pointer lands in a chapter that does not contain the promised content.

**Edit.** Retarget to Chapter 17 and convert to a live markdown link so it cannot silently rot: "The endowment effect, developed in [*Prospect Theory*](17-prospect-theory-gains-and-losses-begin-at-a-reference-point.qmd#endowment-effects-giving-up-is-not-the-same-as-owning), shows that ownership can increase valuation." This is the only bare-italic prose chapter reference in the book that does not resolve — every other italic title reference is already wrapped in a working markdown link.  *(effort: small)*

### [HIGH · consistency] ## The self changes value

> discussed again in *Framing: When the Same Facts Become Different Decisions*

**Problem.** Broken cross-reference. chapters/12-framing-when-the-same-facts-become-different-decisions.qmd contains zero occurrences of "endowment". The endowment effect is actually developed in Chapter 17 (Prospect Theory), which carries the full treatment including Plott and Zeiler (2005), List (2003), and Morewedge and Giblin (2015). A reader following this pointer lands on a chapter that does not discuss the topic.

**Edit.** Repoint to Chapter 17 and use the book's linked style: "[Chapter 17](17-prospect-theory-gains-and-losses-begin-at-a-reference-point.qmd) returns to the endowment effect." Also add the boundary condition here, since the current text presents the WTA/WTP gap as settled: one clause noting that Plott and Zeiler (2005) eliminated the gap under incentive-compatible procedures with training, and List (2003) found it shrank with market experience. That costs a sentence and protects the claim.  *(effort: small)*

### [HIGH · engagement] Opening scenario (before Core Idea)

> An invitation arrives from an organization you admire.

**Problem.** The chapter's running example — the anchor the reader carries through eight sections — is entirely unspecified: no field, no city, no date, no honorarium, no named competing obligation. By the third sentence of paragraph two the scene has already dissolved into analysis ("Which priorities should guide the commitment? To answer, we need to examine what each response is valuing"), which signposts the chapter instead of letting the scene generate the question.

**Edit.** Make the invitation particular and let the costs be countable: a keynote in Lisbon on a Saturday in March, 350 people in the room, no fee, two flights and about fourteen hours of travel, three days of slide work, and your daughter's recital that same Saturday. Then cut the meta-sentence and end the second paragraph on the collision itself — e.g. "The prestige has not changed. The recital has not moved. Something else has." The abstract vocabulary (prestige, recognition, contribution) can then attach to concrete referents for the rest of the chapter.  *(effort: small)*

### [HIGH · insight] ## Price can be both an outcome and an input

> The label changed the interpretation and experience, not the wine.

**Problem.** The section stops exactly one step short of its most interesting implication. Having established that price altered reported pleasantness and mOFC response, the natural inference is not that the buyer was fooled — it is that the pleasure was real. The premium bought an experience that the cheaper label did not deliver. That collides productively with the chapter's own decision-value/experienced-value distinction (set out in the Tinbergen callout) and it makes the price audit's fourth question genuinely hard rather than rhetorical. As written, the section lets the reader settle on the comfortable reading: prices trick people.

**Edit.** Add a short closing paragraph: "Notice what this does not show. The participants were not lying about enjoying the expensive label more; the enjoyment was measured in report and in neural response alike. The price did not simulate pleasure, it produced it. That leaves a harder question than fraud: if the experience you paid for is real but manufactured by the label, is the premium worth paying? The answer depends on whether you want the experience or want the wine — which is the decision-value/experienced-value distinction again, now with a price on it." Then sharpen the audit's Counterfactual line so it asks the reader to answer that, not just to notice it.  *(effort: small)*

### [HIGH · structure] ## Context can change the price of waiting

> Research note: arousal and impatience can come apart

**Problem.** This section is the chapter's best piece of scientific reasoning — five studies, a four-way identification argument, and a table that shows how the same behavioral shift can arise from four different mechanisms — and it is entirely inside a `collapse=true` callout. In default view the section is three paragraphs: a question (€40 today or €60 in three months), a collapsed toggle, and a cue audit. The reader who does not expand never learns the answer to the question the section opens with, and tbl-contextual-cues-and-waiting (arguably the most instructive table in the chapter) never appears. The chapter has three collapsed blocks in total, which also holds the second figure behind a toggle.

**Edit.** Set this one to `collapse=false`, or better: lift the opening paragraph plus tbl-contextual-cues-and-waiting into the main flow and leave only the five-study detail collapsed. At minimum, add a sentence in the visible text that answers the €40/€60 question directly — "Across studies, the same cue can raise physiological arousal without changing the choice, and when the choice does shift, the shift is often better described as perceived time or a starting-point bias than as a changed appetite for reward" — so the section resolves for a reader who never opens the toggle.  *(effort: medium)*

### [HIGH · structure] lines 180-198, Maslow/Kenrick section

> the relatively prepotent need is more likely to dominate attention

**Problem.** The largest accidental duplication in the book. Chapter 6 lines 180-198 and Appendix B lines 53-76 (#maslow-and-kenrick) share 64 distinct 8-word sequences — the quoted sentence is verbatim identical in both. Both passages present: Maslow's five need classes in the same order, the term "relative prepotency", the Bridgman et al. (2019) pyramid-was-not-Maslow's correction, the same shared-meal example (hunger/affiliation/identity/celebration/status), Wahba & Bridwell (1976), the Tay & Diener (2011) 123-countries finding, the Kenrick et al. (2010) reorganization, and the self-actualization removal with the same Kesebir/Peterson & Park rebuttals. Chapter 6's only link to Appendix B is at line 65 and points to #four-questions-not-one-cause — nowhere near this material. So ~500 words are re-derived from scratch with no pointer in either direction.

**Edit.** Make Chapter 6 the short treatment and Appendix B the full one (Appendix B already has the superior three-column comparison table #tbl-maslow-popular-kenrick that ch06 lacks). Cut ch06 lines 184-194 to roughly three sentences — Maslow's classes, the pyramid-is-a-later-invention correction, and the overlapping-systems insight that @fig-overlapping-motive-systems illustrates — then add: "[Appendix B](../appendices/appendix-b-evolutionary-explanations-of-value-choice-and-rationality.qmd#maslow-and-kenrick) sets out the evidence and the three representations that should not be treated as equivalent." Keep @fig-overlapping-motive-systems in ch06; it is the one element Appendix B does not have.  *(effort: medium)*

### [HIGH · structure] ## Learning goals, lines 28-40

> A **utility function** represents an ordering of alternatives under stated assumptions.

**Problem.** Twelve chapters have substantive body prose orphaned under the '## Learning goals' heading with no section of its own: ch04, ch06, ch08, ch10, ch12, ch21, ch29, ch33, ch35, ch36, ch37, ch39, ch40, ch41. In rendered HTML this content is nested inside the Learning goals section, so a reader who skims goals and jumps to the first real heading silently skips a definition of utility (ch06), the bat-and-ball resolution (ch08), the BATNA and reservation-value worked answer (ch36), and the definition of shared reality (ch33).

**Edit.** Give each orphan its own `##` heading, or move it below the first real section heading. Worst cases first: ch36 (5 orphaned paragraphs including the BATNA answer), ch06 (4, including the utility-function definition), ch08 (3, including the bat-and-ball resolution), ch12 (3), ch04 (2), ch33 (2), ch35 (3), ch29 (2).  *(effort: medium)*

### [MEDIUM · accuracy] ## Automatic evaluation is a first pass, not the decision

> Liking, wanting, choice value, and habit strength can come apart

**Problem.** The liking/wanting dissociation is the least obvious claim in the table and the only one with a specific empirical origin — Berridge and Robinson's incentive-salience work — yet no citation appears anywhere in the chapter or its reference list. The chapter cites sources for far less contestable points (self-reference effect, need to belong). Chapter 21 does cite Berridge, so the gap is local rather than book-wide.

**Edit.** Add a source sentence after the table: "The liking/wanting separation comes from work on incentive salience, in which brain manipulations can change how strongly a cue pulls behavior without changing the pleasure the reward produces (Berridge & Robinson, 2003); Chapter 21 develops the implications for habit and craving." Add the reference entry.  *(effort: small)*

### [MEDIUM · clarity] ## Context can change the price of waiting

> run a **cue audit**: What in the environment is currently appetitive

**Problem.** The cue audit is six questions run together inside a single prose paragraph, while the structurally identical price audit earlier in the chapter is a bulleted callout with bolded labels (Cost / Signal / Evidence / Counterfactual). Two instruments of the same kind are presented in two different formats, and the one buried in prose is the harder of the two to actually run.

**Edit.** Convert the cue audit to the same callout form with four bolded labels: **Cue** (what in the environment is appetitive, threatening, or socially charged right now), **Integral or incidental** (is it part of what I am valuing, or spillover), **Route** (did it change the appeal, the perceived distance, the attention, or only the consistency of choice), **Portability** (would this decision survive a different cue, state, and time of day). The parallel with the price audit then becomes visible and both become usable.  *(effort: small)*

### [MEDIUM · clarity] ## Learning goals, goals 1-3

> Distinguish formal utility, psychological valuation, evolutionary fitness, and normative value.

**Problem.** Chapter 6's three goals use only Distinguish, Explain and Separate, yet the chapter contains a fillable Price Audit and a Practice Lab that produces a four-row valuation audit with a forecast to be checked independently. No goal contains a production verb, so the chapter's most demanding output is unannounced.

**Edit.** Replace goal 3 with: 'Produce a four-row valuation audit that separates integral emotional signals from incidental spillover and names one forecast to be checked independently of preference.' Keep goals 1 and 2. The same repair applies to ch11, whose goal 1 'Explain anchoring and insufficient adjustment' undersells a lab that requires collecting a pre-anchor estimate from an unexposed observer.  *(effort: small)*

### [MEDIUM · engagement] ## Learning goals (attention/gaze paragraph)

> manipulating visual attention can influence simple choices, although gaze also reflects

**Problem.** This is one of the most striking results in the valuation literature — where your eyes rest can tip a choice you believe you made on the merits — and it is delivered as an agentless, quantity-free clause with three citations stacked behind it. Nothing tells the reader what was manipulated, by how much, or how large the shift was.

**Edit.** Spend two sentences: name Armel et al.'s manipulation (relative exposure duration of two food items, with the longer-viewed item chosen more often) and give the shift in percentage points from the paper; then give Krajbich et al.'s headline (the last-fixated item is chosen at a rate far above chance) as the correlational counterweight that justifies the existing "although gaze also reflects emerging preference" hedge. The hedge becomes meaningful only once the reader knows how big the effect being hedged is.  *(effort: small)*

### [MEDIUM · engagement] ## Motives change the decision landscape

> A frightened person values safety differently from a relaxed person.

**Problem.** Six consecutive sentences with an identical syntactic frame ("A [state] person values [X] differently from a [contrast] person"), followed by two short flat summary sentences. The rhythm flattens into a chant, and not one of the six carries a concrete instance, a number, or a person. The genuinely vivid material — Read and van Leeuwen's finding that current hunger changes what people choose for a future week — arrives thirty-six lines later and is itself stated without its design or numbers.

**Edit.** Keep two of the six contrasts, cut the rest, and land the paragraph on one worked instance. Pull Read and van Leeuwen forward and give it its design: participants chose snacks to be delivered a week later, and whether they were hungry *at the moment of choosing* shifted what they picked for a future self who would not be hungry — with the percentages from the paper. One documented case does more than six symmetrical sentences, and it sets up the hot-cold empathy gap that follows.  *(effort: small)*

### [MEDIUM · engagement] ## Price can be both an outcome and an input

> In a small fMRI experiment, Plassmann and colleagues (2008) served the same wines

**Problem.** Three consecutive study descriptions with no numbers in any of them: "a small fMRI experiment", "bought the same energy drink at a discount", "a scarce supply increased desirability." These are studies with memorable, citable specifics, and the specifics are what make the effect feel real rather than asserted. "Small" is doing work that a sample size would do better.

**Edit.** Put the figures in the sentences. Plassmann: state the sample size (about twenty participants), the price pairs used on the labels ($5 versus $45, $10 versus $90), and the design detail that carries the argument — the *same* wine appeared twice under two different prices, so the comparison is within-wine. Shiv: give the actual price pair (regular $1.89 versus discounted $0.89) and the mean number of puzzles solved in each condition from the paper. Worchel: state the jar contents (ten cookies versus two) and the rating difference. For Rao and Monroe, report the mean effect size and, more importantly, the moderator that matters — the price–quality association is substantially weaker in multi-cue studies than in single-cue ones, which is the boundary condition a shopper actually faces.  *(effort: medium)*

### [MEDIUM · structure] ## Learning goals

> A **utility function** represents an ordering of alternatives under stated assumptions.

**Problem.** Four paragraphs plus a full collapsible callout (the Tinbergen / four-kinds-of-value material, lines 34–72) sit underneath the "Learning goals" heading with no section heading of their own. In the rendered HTML sidebar and in the epub TOC this substantive content is filed under Learning goals. It is also where the chapter's key definitional scaffolding lives, so it is exactly the material a reader will want to navigate back to.

**Edit.** Insert a `## What "value" refers to` (or `## Four things the word value can mean`) heading immediately before line 34, so that the utility/psychological-valuation definitions, the neuroeconomic pointer, the Tinbergen callout, and the Hume paragraph form a named first section. Learning goals then ends cleanly with its three bullets, matching every other chapter.  *(effort: small)*

### [MEDIUM · structure] ## Practice Lab

> four rows—body and immediate state, self and identity, other people and relationships

**Problem.** The Practice Lab's four rows omit two of the chapter's largest sections. Price — which has its own section, its own audit callout, and three studies — appears nowhere in the audit. Neither does the time/cue dimension from "Context can change the price of waiting." A reader who completes the lab exercises four of the chapter's six substantive topics.

**Edit.** Extend to six rows: body and immediate state; price and the option itself; self and identity; other people and relationships; situation and active motive; time and cue context. Then tie the last row to a concrete deliverable the chapter has already supplied — "for the time row, restate the choice as a smaller-sooner/larger-later pair and note what cue was present when you first felt its appeal." That also gives the chapter's two audits (price, cue) somewhere to be used.  *(effort: small)*

### [MEDIUM · visual] ## Emotion tells the mind what matters (figure)

> Four groups make the influences on value easier to inspect: the option, current state

**Problem.** @fig-valuation is never cross-referenced anywhere in the body (I checked the whole file: the only `@fig-` reference in the chapter is to fig-overlapping-motive-systems). Its caption is a description of the diagram's parts rather than a claim. And it depicts all four families of influence — option, state, goals and experience, social meaning — which correspond to the chapter's next four sections, yet it is dropped into the middle of the Emotion section where it looks like it belongs to emotion alone.

**Edit.** Move the figure up to just after the new "What value refers to" section and use it as the chapter map, with a body sentence that does the work: "@fig-valuation groups the influences the rest of this chapter examines one at a time: the option and its price, the body's current state, goals and identity, and social meaning." Rewrite the caption as a claim: "The same option can receive different value depending on the state, identity, and audience present when it is evaluated — the option itself is only one of four inputs."  *(effort: small)*

### [MEDIUM · visual] ## Motives change the decision landscape

> A hungry person values food differently from a full person.

**Problem.** From the valuation figure to the questions table at the end, the visible main flow (Emotion, The self changes value, Other people, Motives, Context) runs roughly 1,700 words with no figure, table, or styled callout at all — the only relief in that stretch sits inside two collapsed toggles. This is the chapter's longest unbroken block and it coincides with its most abstract material.

**Edit.** Add one new figure in the Emotion section carrying real explanatory load: a two-panel diagram of integral versus incidental emotion. Left panel: a box labeled "the invitation" with arrows from Recognition, Travel cost, Family time feeding a meter labeled "current appeal" — arrows tagged INTEGRAL. Right panel: the identical option and identical arrows, plus a fourth arrow from "a difficult morning" entering the same meter, tagged INCIDENTAL, with the meter reading lower. Caption states the claim: "The option is the same in both panels; only the source of the fourth signal differs. The decision problem is telling the two kinds of arrow apart." This is the chapter's central practical distinction and it is currently text-only.  *(effort: medium)*

### [MEDIUM · visual] line 256, Research Lens: value is distributed

> ::: {.callout-caution .research-lens icon=false}

**Problem.** This is the only one of 36 Research Lens boxes built on .callout-caution instead of .callout-note. Because Quarto paints the base callout first, it renders with caution chrome under the purple research-lens border — a different visual object from the other 35, for content that is an ordinary methods caveat about reverse inference.

**Edit.** Change to `::: {.callout-note .research-lens icon=false}`. Reserve .callout-caution for the evidence-boundary family only, which is where the other five caution callouts already sit.  *(effort: small)*

### [LOW · clarity] '## Motives change the decision landscape' (line 169-176) and '## Research note: are needs a hierarchy?' (line 178)

> A hungry person values food differently from a full person

**Problem.** Chapter 6 is 6,433 words, the longest chapter outside the two closers, and it carries three research notes/lenses plus five thematic sections. Two passages are compressible with no loss. Line 173 is six consecutive sentences in identical grammatical form ('A hungry person values food differently from a full person. A frightened person values safety differently from a relaxed person...') making a point the first two sentences establish. And the Maslow research note (lines 178-214, roughly 36 lines) is a careful debunking of a hierarchy the chapter does not otherwise use, in a chapter that already declares at line 41 that 'How value works is not why a value system exists' — the natural home for that discussion is Appendix B, which exists for exactly this material.

**Edit.** Compress the anaphora list to two sentences plus a short table of state-dependent valuations, which makes it inspectable rather than incantatory. Move the needs-hierarchy research note to Appendix B with a one-line pointer left in ch06. Together these recover roughly 700 words and make the chapter's five genuine contributions (emotion, self, others, motives, price) easier to see.  *(effort: small)*

### [LOW · consistency] ## Using valuation wisely (closing table)

> : Questions for separating value from evidence {#tbl-07-1}

**Problem.** Stale identifier. The label `tbl-07-1` carries the chapter's former number (the aliases show this file was previously chapter 7 and before that chapter 5), and it is the only table in the chapter using the positional style — the other four are semantic (tbl-automatic-evaluation-stages, tbl-value-is-not-one-thing, tbl-maslow-kenrick-valuation, tbl-contextual-cues-and-waiting). The table also arrives immediately after the Research Lens with no lead-in sentence and is never cross-referenced.

**Edit.** Rename to `{#tbl-value-versus-evidence}` and add one lead-in sentence before it that also cross-references it, so it does not appear unannounced after the callout: "Before committing, @tbl-value-versus-evidence runs the chapter's five questions in order." Check the built site for any inbound links to the old anchor.  *(effort: small)*

---

## `chapters/07-the-narrator-after-choice-why-reasons-are-not-always-causes.qmd`  (19 findings)

### [HIGH · accuracy] Opening scenario (before Core Idea)

> Some people notice the switch.

**Problem.** The chapter's foundational phenomenon is quantified nowhere. "Some people notice the switch" leaves the reader free to assume anything from five percent to fifty, and the number is load-bearing: how much weight choice blindness can carry depends entirely on it. Johansson et al. (2005) reported concurrent detection on a minority of manipulated trials, with total detection including retrospective reports still well under a third. The boundary conditions are also missing — the paradigm uses closely matched faces and brief exposure, and detection rises sharply as the options become more distinguishable or viewing time increases. Without them a reader can leave with the over-general conclusion that people never know why they choose, which the chapter's own body text ("People often know their goals, deliberations, and conscious reasons") contradicts.

**Edit.** Give the detection rate in the opening or in the choice-blindness section, and add one sentence of scope: "Detection is not rare because people are oblivious; it depends on the design. The faces were closely matched and shown briefly, and detection rises when the options are easier to tell apart. The result is not that people never know what they chose — it is that the explanation arrives with the same fluency whether or not it has anything to explain."  *(effort: small)*

### [HIGH · clarity] ## Making the narrator accountable

> for detecting hindsight and outcome-based rewriting

**Problem.** Hindsight bias is the mechanism the entire second half of the chapter is built to defeat, and the term appears only in a figure caption, its alt text, and one cell of the detector table. It is never named or defined in the body. A reader arriving at "A review conducted after the outcome has an information advantage and a memory problem" has to reconstruct the concept from that hint. This is also the chapter's learning goal 2 ("how post-choice interpretation can alter memory"), and memory is the least-delivered part of the chapter.

**Edit.** Define it in the first paragraph of that section: "Once an outcome is known, the earlier estimate is hard to recover. In studies of hindsight bias, people asked to recall a forecast they made before the result reliably remember having expected something closer to what happened (Fischhoff, 1975). Asking for greater honesty cannot undo this — the earlier belief is no longer available to be retrieved." Add Fischhoff (1975) to the reference list and cross-link to wherever the book develops it (Chapters 1 and 41 already cite it).  *(effort: small)*

### [HIGH · engagement] ## The interpreter and confabulation

> Research with split-brain patients inspired the idea of an interpreter

**Problem.** This is a three-sentence section — the shortest in the chapter — and it contains the single most vivid demonstration in the entire literature on post-hoc explanation, reduced to the abstraction "an explanatory gap can be filled by a sincere story." The reader is told that a famous thing happened without being shown it. Momentum drops to zero between two substantial sections.

**Edit.** Add the case itself in three sentences: a split-brain patient was shown a chicken claw to the left hemisphere and a snow scene to the right; asked to pick matching cards, the right hand chose a chicken and the left hand chose a shovel; when asked why, the patient — whose speaking hemisphere had no access to the snow scene — explained that you need a shovel to clean out the chicken shed. Then make the point the chapter needs: the explanation was immediate, confident, and constructed from the only evidence available to the explainer. Add one boundary sentence too — these findings come from a handful of patients, and the stronger claims about divided consciousness drawn from them are contested (Pinto et al., 2017, Brain).  *(effort: small)*

### [HIGH · engagement] ## When behavior becomes evidence about the self

> Participants paid only a small amount later evaluated the task more favorably

**Problem.** Festinger and Carlsmith's $1 versus $20 is one of the two or three most famous number pairs in psychology, and the sentence replaces it with "a small amount" and "a stronger external justification." The whole force of the study is the counterintuitive direction — the people paid *less* changed their minds *more* — and that surprise cannot land without the two figures side by side. The paragraph states a genuinely strange result so flatly that the strangeness evaporates.

**Edit.** Restore the numbers and stage the surprise: participants paid $1 to tell a waiting stranger the dull task was enjoyable later rated the task more favorably than those paid $20 — roughly $10 against $200 in today's money. Then state the inversion explicitly: the larger payment produced *less* attitude change, because it supplied an explanation the participant could live with. Also add a scope clause — the study used about twenty participants per cell, and the forced-compliance literature it launched has known design and analysis limitations — which keeps the passage consistent with how the chapter handles Brehm.  *(effort: small)*

### [HIGH · engagement] ## Reasoning as a social instrument

> People can reframe questionable conduct as efficiency, loyalty, standard practice

**Problem.** This section moves through five substantial ideas — motivated reasoning, the argumentative theory, moral rationalization, ethical fading, euphemistic language — across roughly 400 words with not one concrete instance: no case, no date, no organization, no sentence anyone actually said. It is the flattest stretch in the chapter, and it is the one most in need of a specific example, because ethical fading is precisely a claim about *particular words replacing other particular words*.

**Edit.** Anchor ethical fading in one documented case and quote the vocabulary. The Ford Pinto fuel-tank cost-benefit memo is the canonical teaching case for this exact mechanism: a decision about burn deaths conducted entirely in the language of unit cost and expected liability, with no moral term anywhere in the document. Give it two sentences with a date and the framing actually used, then make the point: the memo was not a lie, and nobody in it had to decide to do harm — the frame had already removed the category. One verified case will carry the section; select and cite whichever the author can source cleanly.  *(effort: medium)*

### [MEDIUM · accuracy] Chapter epigraph

> there may be little or no direct introspective access to higher order cognitive processes

**Problem.** The epigraph asserts the strong version of the Nisbett and Wilson thesis, and the body then asserts something incompatible with it — "People often know their goals, deliberations, and conscious reasons" — without ever acknowledging the tension. The strong no-access claim has been contested since Ericsson and Simon (1980, Psychological Review), who argued that verbal reports are valid data about the contents of attention under specified elicitation conditions. A chapter this careful about causal language should not let its epigraph make a stronger claim than its own argument does.

**Edit.** Add one sentence after the Nisbett and Wilson paragraph naming the dispute and stating the chapter's position: "The strong reading — that introspection is never informative — has been contested; Ericsson and Simon (1980) argued that verbal reports are reliable evidence about what was in attention, if not about what caused the response. This chapter takes the narrower claim: people can report what they attended to and endorsed, and cannot reliably report which influences moved them." That is the position the rest of the chapter already occupies; making it explicit strengthens the epigraph rather than undercutting it.  *(effort: small)*

### [MEDIUM · accuracy] ## Making the narrator accountable

> Self-affirmation can sometimes reduce defensiveness by reminding people

**Problem.** The "can sometimes" hedge is correct and I would not flag the wording on its own. The issue is that this sentence is the chapter's one recommendation-to-organizations, and self-affirmation is among the interventions whose effects have shrunk most under preregistered replication — large-scale field replications have reported much smaller or null effects, with benefits concentrated in specific populations and contexts rather than general. The chapter flags an expression of concern on Mazar et al. in its own callout; the same standard applied here would add a boundary clause.

**Edit.** Extend the sentence rather than delete it: "...(Cohen & Sherman, 2014; Steele, 1988), though large preregistered replications have found the effects to be considerably smaller and more context-dependent than early studies suggested, and they should be treated as one possible support rather than a reliable lever." That preserves the practical suggestion while matching the evidentiary care the rest of the chapter shows.  *(effort: small)*

### [MEDIUM · clarity] ## The interpreter and confabulation

> The interpreter and confabulation

**Problem.** "Confabulation" appears in the heading and nowhere else in the chapter. It is a loaded clinical term that a reader may well import the wrong meaning for — most will read it as "lying" — and the section never defines it or earns it. A heading promising a concept the body never delivers is the kind of small breakage that makes a chapter feel thinner than it is.

**Edit.** Define it in one sentence in the body and distinguish it from deception, which is exactly the chapter's core move: "Confabulation is the production of a sincere but unfounded explanation. The speaker is not lying; the explanation system runs on whatever information reaches it, and it does not report when that information is missing." That sentence also does double duty as the bridge to the dissonance section.  *(effort: small)*

### [MEDIUM · clarity] ## Making the narrator accountable

> it preserves the original alternatives, assumptions, forecasts, values, context, and reasons

**Problem.** The decision journal is the chapter's central deliverable and the reader never sees one. It is described as a list of field names in prose, then deferred twice — to Chapter 41 for the definition and Appendix C for the template. "Record before; review after" repeats the same field list in bold. A reader finishing the chapter knows what a decision journal contains but has never seen what a filled entry looks like, which is the difference between a concept and a usable tool.

**Edit.** Insert a five-line filled example in a callout, using a decision the reader can recognize and a real number: a dated entry with the live alternatives, the best forgone option, one probabilistic forecast ("60% that the pilot reaches 200 signups by 31 March"), the assumption it rests on, and the observation that would trigger revision ("fewer than 40 signups in week one"). Then, at the review moment, three lines showing what was appended. The deferrals to Chapter 41 and Appendix C can stay; the example is what makes them worth following.  *(effort: medium)*

### [MEDIUM · engagement] ## Reasons are not the same as causes

> The rightmost item was chosen more frequently, yet participants explained their preferences

**Problem.** The stocking demonstration's power is in its ratio — Nisbett and Wilson report roughly a four-to-one preference for the rightmost of four identical pairs — and in what happened when the influence was named: participants did not merely fail to mention position, they rejected it, some treating the question as odd. "More frequently" and "rejected position as a cause" flatten both. The design is also worth one qualifying clause: this was an informal field demonstration, not a controlled experiment.

**Edit.** State the ratio in the sentence, and give the refusal a concrete shape: participants who were asked directly whether the position of the item had affected them denied it, in some cases appearing to think the question made no sense. Add a half-clause noting it was a store demonstration rather than a controlled study, which costs nothing and prevents an alert reader from discounting the whole passage.  *(effort: small)*

### [MEDIUM · engagement] ## Organizations have narrators too

> decision-makers responsible for an initial allocation sometimes invested more after negative feedback

**Problem.** Staw's escalation study is described only in the abstract terms of its conclusion. The design is what makes it persuasive and memorable — the same negative feedback produced very different second allocations depending only on whether the participant had made the first one. As written, a skeptical reader has no way to see why responsibility is the causal variable rather than a story about it.

**Edit.** Give the design in two sentences: participants acting as executives allocated R&D funds to one of two divisions of a hypothetical company, received deliberately negative results, and then allocated a second round; those who had made the original allocation committed substantially more of the second round to the failing division than those who inherited someone else's decision. State the two allocation means from the paper. The manipulation — personal responsibility, held apart from the information — is the whole point and it is currently invisible.  *(effort: small)*

### [MEDIUM · insight] ## Choice blindness and the confidence of explanation

> some participants failed to notice that an item had been reversed and then argued

**Problem.** Hall et al. (2012) is reported only as a failure of detection, which leaves the reader with "people are gullible." The more consequential result is what happened next: defending the reversed position could move the attitude itself. That turns choice blindness from a curiosity about self-knowledge into a mechanism with a lever — the same loop the chapter later describes as "behavior, explanation, and identity can form a loop" — and the paradigm has since been used deliberately to reduce attitude polarization. The connection is available and unmade.

**Edit.** Add two sentences at the end of that paragraph: participants who argued for a reversed moral or political position sometimes shifted toward it, and later work has used the paradigm to soften entrenched attitudes by getting people to produce arguments they did not originally hold. Then state the implication, which is genuinely uncomfortable: the same process that makes explanations unreliable as evidence also makes them effective as persuasion — including self-persuasion. That sentence would connect the section forward to the self-perception paragraph rather than leaving them as two separate observations.  *(effort: small)*

### [MEDIUM · insight] ## Choice blindness and the confidence of explanation

> Once an outcome is represented as **my choice** or **my view**

**Problem.** This chapter and Chapter 6 are the two halves of one argument — Chapter 6 ends by asking "which benefit first caught your attention," and this chapter is about the account produced afterward — yet neither file links to the other. Chapter 7 contains no cross-reference to Chapter 6 at all, though it links to Chapters 1, 41, and Appendix C. The reader is not given the pairing, which is the cheapest available way to make both chapters feel like parts of a system.

**Edit.** Add a bridge in the opening or at the end of "Reasons are not the same as causes": "[Chapter 6](06-valuation-how-options-become-worth-choosing.qmd) examined what gives an option its weight at the moment of choosing — attention, state, identity, audience, price. Most of those influences leave no trace the chooser can later retrieve. This chapter is about what fills the gap they leave." That single sentence names the mechanism connecting the two chapters and gives the reader a reason the order is what it is.  *(effort: small)*

### [MEDIUM · insight] After the motivated-reasoning paragraph at line 82

> Motivated reasoning occurs when people search and evaluate arguments in ways that favor a preferred conclusion

**Problem.** The book asks the reader to make a moral judgment in almost every chapter — fifteen chapters carry a named '## Ethics:' section, ch40 runs a ten-dimension ethical audit, Appendix C collects the standard — yet it never explains how moral judgment actually works. The phrase 'moral judgment' appears exactly once in 42 chapters, incidentally, inside Entman's definition of framing (ch12, line 97). There is no treatment of moral intuition arriving before justification, of ethical fading, of moral disengagement, or of protected and sacred values. The asymmetry is odd in a book this careful: it teaches a demanding ethical practice while leaving the psychology of that practice undescribed, which also leaves ch07's own thesis about post-hoc reasons stopping just short of its strongest case.

**Edit.** Add ~700 words to ch07 as '## Moral reasoning often arrives after the verdict', placed directly after the Kunda paragraph — ch07 is already the chapter about reasons that are not causes, and the moral case is its best instance. Then two cross-links rather than a new chapter: ~200 words on ethical fading and moral disengagement in ch28 beside Milgram, and ~150 words on protected/sacred values in ch37 beside the trade-discovery method, since proposing a trade on a protected value is the most reliable way to destroy a negotiation and ch37 currently has no warning about it.  *(effort: medium)*

### [MEDIUM · structure] ## Organizations have narrators too

> The problem is an explanation that can survive any outcome.

**Problem.** Duplicate content two lines apart. The preceding paragraph already closes with the sharper formulation — "The danger is a story that can explain every possible result and therefore cannot be wrong" — and the following one-sentence paragraph restates it in weaker words before continuing. The repetition blunts what is the single best line in the chapter by immediately paraphrasing it downward.

**Edit.** Delete the restatement and merge the remainder into the previous paragraph, so it reads: "...and therefore cannot be wrong. 'Customers were not ready' might be correct, but the team should state in advance what observation would distinguish that account from a poor product or an ineffective launch." The same pattern recurs at the end of the accountability section, where "The record lets the team compare what it expected with what it now knows" restates the decision-journal paragraph; that sentence can go too.  *(effort: small)*

### [MEDIUM · visual] ## Choice blindness and the confidence of explanation (figure)

> A choice-blindness switch. A chooser selects one abstract card

**Problem.** Neither figure nor either table is cross-referenced anywhere in this file — I checked the whole file and it contains no `@fig-` or `@tbl-` reference at all, so both figures float beside the text and neither table is introduced. The choice-blindness caption also describes only the procedure and stops before the result, which is the thing worth showing.

**Edit.** Add cross-references in the body for all four ("@fig-choice-blindness-swap shows the manipulation"; "@tbl-rationalization-detector converts..."; "@tbl-process-outcome-review separates..."; "@fig-narrator-learning..."). Rewrite the choice-blindness caption so it ends on the finding rather than the method: "...and the rejected card is presented with a request for reasons — which most participants supply, describing features of a card they did not choose." The narrator-learning caption is already written as a claim and can stand.  *(effort: small)*

### [MEDIUM · visual] ## Reasons are not the same as causes

> It can describe what a person consciously considered before choosing.

**Problem.** Learning goal 1 — distinguish a reason, a justification, and a cause — is delivered entirely as four consecutive prose sentences in one paragraph, with no visual anchor, and the distinction is never returned to in that form. It is also the chapter's organizing distinction, which makes it the one thing a reader should be able to look back at. Separately, the stretch between the two figures (the interpreter, dissonance, social reasoning, and organizational sections) runs roughly 1,200 words of the chapter's most abstract material with only one collapsed evidence note for relief.

**Edit.** Add a four-row table immediately after that paragraph, which both delivers learning goal 1 and breaks the visual-free stretch. Rows: report of conscious deliberation / justification to an audience / endorsed value / post-hoc construction. Columns: "What it is good evidence for" (what was in attention; what the speaker will defend; what the person cares about; what is available now), "What it is not evidence for" (all of them: what caused the choice), and "How you could tell" (a contemporaneous record; whether the reason changes with audience; whether it would justify the rejected option; whether it was produced only after the outcome). The third column is what makes it a tool rather than a taxonomy.  *(effort: medium)*

### [LOW · consistency] ## References cited in this chapter

> Chen, M. K., & Risen, J. L. (2010). How choice affects and reflects preferences

**Problem.** The reference list is alphabetical except for this entry, which sits last, after Weick. Chapter 6's list has the same class of problem in five places (Bechara before Bartra, Griskevicius 2006 before Giner-Sorolla, Klauer before Kenrick, Plassmann after Poldrack, Worchel before Van den Bergh), suggesting entries were appended as they were added rather than inserted in order.

**Edit.** Move Chen & Risen between Brehm and Cohen, and re-sort the five misplaced entries in Chapter 6. Worth a one-off script across all chapter files to sort `.reference` blocks alphabetically and report any that were out of place, since the same pattern is likely elsewhere in the book.  *(effort: small)*

### [LOW · visual] ## Record before; review after

> |  | Good outcome | Bad outcome |

**Problem.** The process/outcome table has an empty top-left header cell. The row labels are "Good process" and "Poor process" and the column labels are outcomes, but nothing in the table tells the reader that the rows are the process dimension until they read the cells — and in a 2x2 whose whole purpose is holding two dimensions apart, an unlabeled axis is the one thing worth fixing.

**Edit.** Label the corner cell "Process quality" (or "Process \\ Outcome"), and add a lead-in sentence that cross-references it. While editing, note that this table is the chapter's clearest statement of the outcome/process distinction, so it deserves a body sentence pointing at the diagonal that surprises people: a good outcome from a poor process is the dangerous cell, because it gets remembered as skill.  *(effort: small)*

---

## `chapters/08-fast-and-frugal-thinking.qmd`  (13 findings)

### [HIGH · clarity] ## Fast thinking is not primitive thinking (fig-fast-slow)

> Type 1 and Type 2 name clusters of processing features.

**Problem.** The figure and its caption use 'Type 1' and 'Type 2'; the body text immediately below uses 'System 1' and 'System 2'; the words 'Type 1' never appear in the body at all. The reader must infer that these are the same distinction under two labels, and there is a live reason for the two labels (Type 1/Type 2 is preferred precisely to avoid implying literal brain systems — which is this chapter's first learning goal). The terminological point being made by the figure is invisible.

**Edit.** Add one clause to the body sentence that introduces the labels: 'The label System 1 is often used for a family of fast, automatic ... processes; many researchers prefer Type 1 and Type 2 precisely because 'system' implies two machines rather than two clusters of features.' That converts an inconsistency into the chapter's own argument and makes @fig-fast-slow's labels self-explaining.  *(effort: small)*

### [HIGH · engagement] ## Fast thinking is not primitive thinking

> A firefighter may sense that a building is unsafe before being able to articulate why.

**Problem.** Three consecutive expertise claims (chess player, physician, firefighter) are generalizations where the source literature supplies vivid, specific scenes. The paragraph is the chapter's best opportunity for concreteness and it spends it on abstractions; the reader is told that expert intuition exists but never shown it working.

**Edit.** Tell Klein's phantom-basement case, which is in the book already cited (Klein, 1998): a lieutenant leads a crew into what is reported as a routine kitchen fire; the living room is hotter than a kitchen fire should make it and unnervingly quiet; without being able to say why, he orders everyone out; moments later the floor collapses into a basement no one knew was there, where the fire actually was. Then, for chess, replace 'sees meaningful patterns' with the finding that makes the cue/ecological-fit point exactly: masters reconstruct real game positions far better than novices, but that advantage vanishes when the same pieces are scattered at random (Chase & Simon, 1973) — the expertise is in the pattern, not in the eyes. Add Chase & Simon to the reference list.  *(effort: medium)*

### [HIGH · engagement] Opening bridge after Learning goals

> The tempting answer uses the numbers fluently while failing to preserve the stated difference.

**Problem.** The bat-and-ball problem is the most reused opener in the behavioral science genre, and here it is resolved with no magnitude attached. The reader who answered 10 cents never learns that they are in excellent company, and the reader who answered 5 cents never learns how unusual that is. The surprise — that the error survives elite quantitative training — is available in Frederick (2005) and is simply not stated.

**Edit.** Append one sentence with the numbers: across Frederick's 3,428 respondents, 33% missed all three CRT items and 83% missed at least one; more than half of the students sampled at Harvard, Princeton, and MIT answered the bat-and-ball item incorrectly. The last clause is what makes the point land: the error is not an intelligence deficit, which is exactly the chapter's thesis. Verify the exact figures against Table 1 of Frederick (2005) before printing.  *(effort: small)*

### [HIGH · insight] ## When intuition deserves trust

> Three questions help decide how much confidence to place in an intuition

**Problem.** Kahneman & Klein (2009) is cited three times in the chapter, but the chapter never tells the story that makes the paper unforgettable and that models the book's own epistemic values. Two researchers who had publicly disagreed for years — Kahneman on heuristics and biases, Klein on naturalistic expertise — set out in an adversarial collaboration to locate their disagreement, and found they agreed on the boundary conditions. The paper's title is 'Conditions for intuitive expertise: A failure to disagree.' Presented as a bare numbered list, the three questions read like a checklist from nowhere.

**Edit.** Add two or three sentences before the list: name the disagreement (Kahneman had spent decades documenting where expert intuition fails; Klein had spent decades documenting where it succeeds), name the method (a deliberate adversarial collaboration), and name the result (they converged on the same three conditions, which is why the paper is subtitled 'A failure to disagree'). This is surprise-then-resolution, it costs no accuracy, and it makes the three questions arrive as a hard-won settlement rather than an assertion.  *(effort: small)*

### [MEDIUM · accuracy] ## When intuition deserves trust

> work sample with the interview impression may be more informative

**Problem.** The chapter's most actionable recommendation is left as a bare 'may be more informative' with no magnitude, when personnel-selection meta-analyses supply one. This is also a place where the obvious source is now the wrong source: Schmidt & Hunter's (1998) widely quoted validity table has been shown to overstate operational validities because of inappropriate range-restriction corrections.

**Edit.** If the author adds numbers here — and it would strengthen the section considerably — use Sackett, Zhang, Berry & Lievens (2022, Journal of Applied Psychology), whose corrected estimates put structured interviews and work samples well below the familiar 1998 figures, not Schmidt & Hunter (1998). Even a single clause ('structured, job-relevant measures predict better than unstructured impressions, though the corrected validities are more modest than the figures still commonly quoted') would make the recommendation evidential rather than exhortative, and the correction itself is exactly the kind of honesty the book's voice is built on.  *(effort: medium)*

### [MEDIUM · accuracy] ## Slow thinking is powerful, expensive, and often late

> In experiments, distraction increased acceptance of statements presented as false

**Problem.** The Spinozan belief account is presented with 'These findings show how cognitive load can interfere with checking,' which is stronger than the current evidential position warrants. Later work on epistemic monitoring (Richter, Schroeder & Wöhrmann, 2009) found that validation against prior knowledge can occur routinely and efficiently during comprehension, which is not what a strict acceptance-first model predicts, and the Gilbert et al. (1993) paradigm has not been extensively replicated.

**Edit.** Soften the second sentence to match the chapter's standard elsewhere: 'These experiments are consistent with load interfering with checking, though whether acceptance genuinely precedes evaluation remains contested (Richter et al., 2009).' The chapter hedges carefully around Bago & De Neys two pages earlier; this claim deserves the same treatment.  *(effort: small)*

### [MEDIUM · clarity] ## Emotion is part of judgment

> Interrogate the feeling rather than suppressing it

**Problem.** This section is two short paragraphs of pure rule with no instance, sandwiched between two substantial sections. It reads as a reminder inserted for completeness rather than a developed argument, and the 'value versus probability' distinction — which the chapter calls 'the diagnostic distinction' — is never shown operating on a case.

**Edit.** Add one three-sentence instance that runs the three questions: an interviewer feels uneasy after a candidate describes leaving a previous role; the unease may be a value signal (this organization cares about how people talk about former colleagues) or carried in from a bad hire two years ago; the forecast that must be checked independently is whether candidates who describe exits this way actually underperform. Same length, one concrete anchor.  *(effort: small)*

### [MEDIUM · consistency] Table: Two processing modes

> Two processing modes {#tbl-04-1}

**Problem.** Two problems in one line. First, the table ID is stale from an earlier chapter numbering — this is Chapter 8 but the anchor is tbl-04-1. The same pattern runs through the assigned files (tbl-10-1 in Chapter 9, tbl-13-1 in Chapter 10) and onward (tbl-14-1 in Ch11, tbl-15-1 in Ch12), while Chapter 7 has already migrated to semantic IDs like tbl-rationalization-detector. Second, the caption 'Two processing modes' is a label, not a claim.

**Edit.** Renumber to semantic IDs matching the Chapter 7 convention (tbl-processing-modes here; tbl-shortcut-correctives in Ch9; tbl-belief-protection-tests in Ch10) and grep the book for any @tbl- cross-references before changing them. Make the caption assert the takeaway the table actually supports: 'Neither mode is the reliable one: each can be brilliantly trained or badly misled.'  *(effort: small)*

### [MEDIUM · engagement] ## Slow thinking is powerful, expensive, and often late

> An interviewer who already likes a candidate can spend considerable effort finding reasons

**Problem.** The claim that deliberation can defend rather than correct an intuition is the chapter's most useful non-obvious idea — it is named in the Core Idea ('Deliberation can correct it, but can also defend it') — yet it is delivered in two flat, agentless sentences and then dropped. The paragraph asserts the mechanism without showing it and without pointing forward to the chapter that develops it.

**Edit.** Give it a scene of two or three sentences (the committee member who, having warmed to a candidate in the first five minutes, spends the next forty assembling a case, and whose extra effort makes the conclusion feel better supported rather than better tested) and add a forward link to Chapter 10, which builds this into an entire chapter. Right now the two chapters' central shared mechanism is never explicitly connected.  *(effort: small)*

### [MEDIUM · insight] ## From a quick answer to a heuristic

> What does the decision actually require?

**Problem.** The four-element diagnosis (target, cue, ecological fit, feedback) is the chapter's central tool and its named deliverable in the Practice Lab, but it is never run end-to-end on a single case. The ingredients are scattered — the recruiter appears in the target/cue discussion, ecological fit appears in the firefighter contrast, feedback appears two sections later under 'How the modes train' — so the reader never watches the tool complete one pass.

**Edit.** Immediately after the numbered list, add a four-sentence worked pass on the recruiter. Target: performance in the role over eighteen months. Cue: conversational fluency in a 45-minute conversation. Ecological fit: whether that cue has ever been validated against that criterion in this organization. Feedback: rejected candidates' outcomes are never observed, so twenty years of interviewing can build confidence without building accuracy. Four sentences make the tool portable and set up the Practice Lab.  *(effort: small)*

### [MEDIUM · insight] After '## When intuition deserves trust' (line ~123)

> In a hiring decision or an emergency, checking takes time that may itself matter

**Problem.** The chapter raises time-pressured decisions in its first pages and then never returns to them. Across 42 chapters, 'time pressure' appears mainly as a row in a table (ch03), a meta-analysis citation (ch36), and a clause in ch41 ('Chess and some skilled emergency work'). Klein is cited six times but naturalistic decision making only once, and recognition-primed decision making — the best-evidenced account of how experts actually decide when the clock binds — is never described. Gawande's checklist work is cited once, in ch03, without explaining why a checklist beats deliberation under load. The book therefore equips the reader well for the deliberate case and leaves the fireground, the trading desk, and the emergency department unaddressed.

**Edit.** Add ~600 words as '## Deciding when there is no time to decide', directly after '## When intuition deserves trust' so it inherits the four diagnostic questions the chapter has just established. Cover recognition-primed decision making (one option generated and evaluated by mental simulation, not compared against alternatives), why checklists protect against load rather than against ignorance, and the boundary: RPD is trustworthy only where ch08's own cue/ecological-fit/feedback conditions are already satisfied, which is exactly why it works for firefighters and not for one-off strategy.  *(effort: medium)*

### [MEDIUM · visual] ## Slow thinking is powerful, expensive, and often late

> People are typically slower and more error-prone when controlled attention must resolve this conflict

**Problem.** @fig-stroop-interference-lab is an activity the reader is asked to perform, but it has no debrief and no magnitude. 'Slower' with no number gives the reader no way to calibrate what they just experienced, and the activity is never connected back to the chapter's own diagnostic frame (target, cue, fit).

**Edit.** Add the magnitude — colour naming of incongruent words is typically on the order of 100 ms slower than neutral baselines, reviewed in MacLeod (1991) — and one debrief sentence in the chapter's own vocabulary: the word meaning is a cue with near-perfect validity for the reading task and zero validity for the ink-naming task, and it arrives anyway. That is the whole chapter in one demonstration the reader has just run on themselves.  *(effort: small)*

### [LOW · consistency] ## References cited in this chapter

> Goldstein, D. G., & Gigerenzer, G. (2002). Models of ecological rationality

**Problem.** Three alphabetization errors in the reference list: Goldstein & Gigerenzer (2002) is placed before Gilbert (1991) and Gilbert et al. (1993); Kahneman & Frederick (2002) is placed after Klein (1998); Stroop (1935) is placed before Shiffrin & Schneider (1977). Also, the Gilbert et al. title is rendered 'You cannot not believe everything you read' — the published title is 'You can't not believe everything you read.'

**Edit.** Reorder to Gigerenzer & Gaissmaier, Gigerenzer & Goldstein, Gilbert (1991), Gilbert et al. (1993), Goldstein & Gigerenzer; Kahneman (2011), Kahneman & Beatty, Kahneman & Frederick, Kahneman & Klein, Klein; Schneider & Shiffrin, Shiffrin & Schneider, Stroop. Restore the Gilbert et al. title as published. Worth a single scripted pass over all chapter reference blocks, since the same drift is likely elsewhere.  *(effort: small)*

---

## `chapters/09-what-feels-likely-availability-affect-and-resemblance.qmd`  (13 findings)

### [HIGH · accuracy] ## When value substitutes for evidence: affect answers first

> Schwarz and Clore (1983) found that current mood influenced reported life satisfaction

**Problem.** This is stated as settled, but the weather-to-life-satisfaction demonstration is one of the more prominent classic effects to have failed large-sample reproduction. Lucas & Lawless (2013, JPSP 104(5), 872-884) analyzed roughly a million US respondents and found weather effects on life-satisfaction reports that were at best tiny, having specifically tested the unseasonably-pleasant and unseasonably-unpleasant days that the original targeted. The original's reported effect was large (on the order of 1.7 points on a 10-point scale). This is the one claim in the chapter that the book's own 'how to read evidence' standards would flag.

**Edit.** Add one clause and one citation: '...though a later analysis of roughly a million respondents found weather effects on life-satisfaction reports that were at best very small (Lucas & Lawless, 2013), and the debate over what that implies for the original demonstration continues (Schwarz & Clore, 2016).' Then make explicit that the mood-as-information account rests on a broader evidence base than this single manipulation, so the reader does not discard the mechanism along with the demonstration. Add Lucas & Lawless to the reference list.  *(effort: small)*

### [HIGH · accuracy] ## When category fit substitutes for probability: resemblance

> Linda is a bank teller and active in the feminist movement

**Problem.** The Linda problem is presented with no error rate and, more importantly, without the best-established boundary condition on it. Asking the same question in a frequency format ('How many of 200 women who fit this description are...') sharply reduces conjunction errors (Fiedler, 1988; Hertwig & Gigerenzer, 1999), and Tversky & Kahneman themselves reported reduced rates under frequency framing in the 1983 paper the chapter cites. Presenting the effect as a clean substitution without the format moderator overstates a single result and leaves the reader unprepared for the natural-frequencies argument the book makes two chapters later.

**Edit.** Add the rate (roughly 85-90% chose the conjunction in the original probability-ranking format) and then a two-sentence boundary: in frequency format the error rate drops to roughly 20-40%, which some read as evidence that part of the effect is a pragmatic misreading of 'probable' and 'bank teller' (Hertwig & Gigerenzer, 1999); an adversarial collaboration concluded the fallacy is reduced but not eliminated by frequency framing (Mellers, Hertwig & Kahneman, 2001). Then point forward: Chapter 14's natural-frequencies section is the same mechanism. This makes the chapter more accurate and better connected in three sentences.  *(effort: medium)*

### [HIGH · consistency] ## References cited in this chapter

> Kahneman, D. (1973). Attention and effort. Prentice-Hall.

**Problem.** Two references are listed but cited nowhere in the body: Kahneman (1973), Attention and effort, and Lerner, Li, Valdesolo & Kassam (2015), Emotion and decision making. Every other reference in the list has a body citation. The section heading is 'References cited in this chapter,' so these are straightforwardly false.

**Edit.** Lerner et al. (2015) should be cited, not removed — it is the obvious review to place beside Lerner & Keltner (2001) in the sentence about emotion-specific appraisals, and it strengthens that claim from one experiment to a review. Kahneman (1973) is about attentional capacity and belongs with Chapter 3; delete it here. Worth running the same both-directions check over every chapter, since two orphans in one list suggests drift during revision.  *(effort: small)*

### [HIGH · engagement] Opening scenario

> A product failure appears in your news feed

**Problem.** The chapter contains no named person, company, product, date, place, or dollar figure from beginning to end. The running example is 'a product failure'; the worked case is 'a vivid aviation accident'; the hiring case is 'a committee.' A chapter whose entire argument is that vivid specifics overwhelm abstract base rates is written without a single vivid specific, which makes it the least concrete of the three chapters despite being about concreteness.

**Edit.** Anchor the running product-failure example in one real, dated case with a published denominator so the reader can watch the denominator do work — the Samsung Galaxy Note 7 is the natural choice: a globally covered story with a recall notice that states both the incident count and the number of units in the field. Pull both figures from the September 2016 CPSC recall notice rather than from memory, and use them at the three places the chapter currently says 'the product failure' (the opening, the affect section, and 'Take it forward'). One case carried across the chapter beats four hypotheticals.  *(effort: medium)*

### [HIGH · engagement] ## One risk, three shortcuts

> Suppose a board must decide whether to suspend employee travel after a vivid aviation accident.

**Problem.** This is the chapter's integrative set-piece and it is entirely hypothetical ('Suppose a board must decide...'), when the canonical, quantified, and genuinely tragic version of exactly this substitution exists and is not mentioned anywhere in the chapter. The section describes what the three shortcuts would do rather than showing what they did do, and the closing requirement — 'comparison with the risks created by alternative travel' — is precisely the comparison that the real case shows people failing to make.

**Edit.** Replace or precede the hypothetical with the post-9/11 substitution of driving for flying: Gigerenzer (2004, Psychological Science) estimated roughly 350 additional US road deaths in the three months after the attacks — more than the number of passengers aboard the four aircraft — and later put the twelve-month figure near 1,600 (Gigerenzer, 2006). Then hedge as the book's voice requires: these are model-based estimates from interrupted time-series comparisons and the magnitude has been contested (Blalock, Kadiyali & Simon, 2009). The hedge is the point — the reader gets a shocking number and immediately learns how to hold it. Add both references.  *(effort: medium)*

### [HIGH · insight] ## When value substitutes for evidence: affect answers first (fig-affect-panda-sea-star)

> The comparison separates immediate appeal from ecological importance.

**Problem.** The figure asks the reader to notice that the sea star may matter more than the panda, but the chapter never supplies a single fact establishing that the sea star matters at all. The exercise that follows is explicitly counterfactual ('suppose independent evidence showed...'), so the reader is asked to imagine the evidence rather than confront it. The illustration's whole rhetorical payload depends on a fact the text withholds.

**Edit.** State the fact, which is better than the hypothetical: Paine (1966) removed the ochre sea star (Pisaster ochraceus) from a rocky intertidal plot at Mukkaw Bay, and within a year mussels crowded out the competition and the community fell from fifteen species to eight — this is the experiment that gave ecology the term 'keystone species.' Then the 'suppose' becomes 'as it happens,' and the reader's initial preference for the panda is corrected by evidence rather than by instruction. Add Paine (1966, American Naturalist) to the reference list.  *(effort: small)*

### [HIGH · visual] ## When correlated cues look like independent evidence

> List each reason for the judgment, then trace its source.

**Problem.** The independence audit is the chapter's most original contribution — it is the idea that distinguishes this chapter from every other treatment of these three heuristics — and it is the only major idea in the chapter with no figure. The three preceding sections each open with a diagram; this one carries the synthesis in prose alone, across roughly 900 words from here to the summary table with no visual relief.

**Edit.** Add a two-panel figure. Left panel: one source event at far left (a single incident) fanning into three labelled channels — affect ('it feels alarming'), availability ('I can picture it'), resemblance ('it looks like the last one') — each arriving at a decision box as a separate arrow, with the decision box labelled 'three reasons.' Right panel: the identical arrows redrawn collapsing back to the single source, with the decision box relabelled 'one reason, counted three times.' Caption should be the claim, not the label: 'Three impressions traced to one event are one piece of evidence, not three.' This is the figure that would make the chapter memorable.  *(effort: large)*

### [MEDIUM · clarity] ## When category fit substitutes for probability: resemblance

> The next statistical chapters provide the formal correction.

**Problem.** A vague forward pointer at exactly the moment the reader most wants to know where the real answer lives. 'The next statistical chapters' does not tell the reader whether that is one chapter or five, or which one supplies base rates versus which supplies sampling variability.

**Edit.** Name them and say what each supplies: 'Chapter 14 supplies the base rate and the conditional probability; Chapter 15 supplies sampling variability, regression, and calibration.' Two named destinations instead of a gesture.  *(effort: small)*

### [MEDIUM · consistency] Table: When affect, availability, and resemblance help or mislead

> Personal example | The case is diagnostically similar.

**Problem.** The summary table has four rows, but only three shortcuts are named and developed in the body. 'Personal example' appears for the first and only time in the table. The chapter title, the Core Idea, the learning goals, and every section heading promise three; the table delivers four, which will read to a careful reader as an oversight.

**Edit.** Either promote it or fold it in. Promotion is better: the 'From an impression to a distribution' section already makes the single-case argument ('One near miss cannot estimate an accident rate, but it can reveal a new failure pathway') — name it there as single-case reasoning and say explicitly that it is a special case of availability in which the sample is one's own experience rather than the media's. Then the table row has a referent.  *(effort: small)*

### [MEDIUM · engagement] ## When recall substitutes for frequency: availability

> Dramatic causes were often overestimated, while less dramatic but more common causes were underestimated.

**Problem.** Lichtenstein et al. (1978) is one of the most quotable studies in the field, and it is reported here only as a direction. The sentence tells the reader the shape of the bias without letting them feel it; the three sentences that follow are equally shapeless ('Events that receive more attention become mentally available'). This is a four-sentence stretch of pure generalization in the section that most needs an instance.

**Edit.** Give one contrasting pair with a multiplier — respondents judged accidents and disease to kill roughly equally often when disease in fact killed many times more, and judged some dramatic causes (tornadoes, botulism, homicide) as more lethal than quieter and far more common ones (asthma, diabetes, stroke). Take the exact pair and ratio from Lichtenstein et al. (1978) or Slovic, Fischhoff & Lichtenstein (1979) rather than from secondary sources, since the figures circulate in distorted form. One verified pair replaces four flat sentences.  *(effort: small)*

### [MEDIUM · engagement] ## When category fit substitutes for probability: resemblance

> predicted election winners above chance

**Problem.** 'Above chance' drains a genuinely startling finding of everything that makes it startling. The footnote that follows does careful, valuable work qualifying the result — but the qualification has nothing to qualify, because the reader has not been given a magnitude to be surprised by in the first place.

**Edit.** Give the number: competence judgments made from one-second exposures to photographs of candidates the participants did not recognize predicted the winner in roughly 69% of 2004 US Senate races, and tracked the margin of victory (Todorov et al., 2005). Then the existing footnote earns its keep — the reader now has something large enough to demand an explanation, and the footnote supplies the alternatives.  *(effort: small)*

### [MEDIUM · visual] ## When recall substitutes for frequency: availability

> People did not simply count examples; they used ease of retrieval as a cue.

**Problem.** The chapter contains no styled callout of any kind — no .activity, no .research-lens, no .evidence-and-boundary-conditions — across its full length, unlike Chapter 8 (research lens) and Chapter 10 (research lens plus watch-and-test). The result is an unbroken run of body prose relieved only by three small diagrams and one end table, which is the flattest visual rhythm of the three chapters. The Schwarz et al. finding is also described when it is one of the few in the book the reader can run on themselves in ninety seconds.

**Edit.** Convert the ease-of-retrieval material into an .activity callout: ask the reader to list six occasions on which they were assertive and rate their own assertiveness, then list six more and rate again. The reversal is the demonstration. Add one sentence of boundary condition — a meta-analysis of ease-of-retrieval studies supports the effect while identifying substantial moderation (Weingarten & Hutchinson, 2018, Psychological Bulletin) — which both breaks up the prose and raises the evidential standard.  *(effort: medium)*

### [LOW · visual] Figure caption (fig-affect-panda-sea-star) and table ID

> Which species receives your immediate concern?

**Problem.** The figure caption is a question rather than a sentence-length claim, so a reader skimming captions learns nothing from it; elsewhere in the chapter the captions do state takeaways (@fig-affect-availability and @fig-prototype-probability both do). Separately, the summary table carries the stale ID {#tbl-10-1} in what is now Chapter 9.

**Edit.** Move the question into the body where it belongs as a prompt, and make the caption a claim the figure supports: 'Charisma and ecological importance are unrelated: the ochre sea star is a keystone predator, the giant panda is not.' Renumber the table to a semantic ID as recommended for Chapter 8. Also move the Todorov entry above the Tversky entries in the reference list.  *(effort: small)*

---

## `chapters/10-beliefs-that-defend-themselves.qmd`  (14 findings)

### [HIGH · accuracy] ## Confirmation and myside bias

> because intelligence can help people generate better arguments for what they already believe

**Problem.** This misstates what Stanovich, West & Toplak (2013) found. Their headline result is a dissociation: myside bias shows little or no correlation with cognitive ability, which is why it is not reduced by intelligence or education. The causal mechanism asserted here — that intelligence supplies better ammunition for prior beliefs — is a different and more contested claim, associated with Perkins's work on informal reasoning and with Kahan's identity-protective cognition, not with the Stanovich paper cited.

**Edit.** Restate as two claims with the right owners: 'Myside bias shows little relation to cognitive ability, which is why it is not corrected by intelligence or education (Stanovich et al., 2013). Greater ability may even supply better arguments for a position already held (Kahan, 2013).' The dissociation finding is also the more interesting one for this chapter's argument, since it undercuts the reader's likely assumption that being smart is the defense.  *(effort: small)*

### [HIGH · accuracy] ## Self-serving explanations

> while attributing failure to bad luck, unfair conditions, other people, or external constraints

**Problem.** Miller & Ross (1975) is cited as evidence for the full self-serving pattern, but that paper argues close to the opposite. Its subtitle is 'Fact or fiction?' and its conclusion was that the evidence supported self-enhancing attributions for success while providing little support for self-protective attributions for failure, and that non-motivational information-processing accounts could explain much of what had been observed. Citing the field's most influential skeptical review as support for the claim it doubted is the kind of slip a careful reader will catch.

**Edit.** Carry the existence claim on Mezulis et al. (2004) alone, and give Miller & Ross their actual role — which makes the passage better, not weaker: 'Miller and Ross (1975) questioned whether the failure half of this pattern was motivated at all, arguing that ordinary information processing could produce it; a later meta-analysis of 266 studies found the overall bias large but highly variable (Mezulis et al., 2004).' That converts a miscitation into the chapter's characteristic move of showing a claim being tested.  *(effort: small)*

### [HIGH · accuracy] ## Confirmation and myside bias

> Participants reported greater polarization after considering the mixed evidence.

**Problem.** The hedge here is exactly right and should be praised — 'reported' is doing precise work. But it is too quiet to protect the reader, who will read the sentence as a plain statement that attitudes polarized. The distinction matters: polarization in Lord et al. was assessed largely through self-reported attitude change, and studies measuring pre- and post-attitudes directly have often failed to find it (Miller, McHoskey, Bane & Dowd, 1993; Kuhn & Lao, 1996). Biased assimilation of the evidence is the better-supported half of the classic finding; attitude polarization is the shakier half.

**Edit.** Follow the hedge through in one sentence: 'That polarization was measured mainly as self-reported attitude change; studies comparing directly measured attitudes before and after often find little or none (Miller et al., 1993; Kuhn & Lao, 1996). The differential evaluation of the two studies — biased assimilation — is the more robust part of the result.' This is a case where making the book more accurate also makes it more interesting, because the reader learns that even the classic has a load-bearing caveat.  *(effort: medium)*

### [HIGH · engagement] ## Attribution: behavior is visible, situations are not

> developed more self-serving assessments and settled less often than those who evaluated the case

**Problem.** 'Settled less often' conceals the sharpest experimental contrast in the chapter. In Babcock et al. (1995), when participants learned their role only after reading the case, 6% of negotiations ended in impasse; when they knew their role before reading, 28% did — a fourfold difference produced by nothing but the timing of one piece of information, with identical case materials. Stated as a direction, it is unremarkable; stated as numbers, it is the chapter's most persuasive single fact and its most directly actionable one.

**Edit.** Give the two figures in the sentence itself: 6% versus 28% impasse, same materials, one change in when the role was revealed. Then draw the one-line implication the chapter has earned but does not state — form your assessment of a case before you learn which side you are on, which is a procedure a reader can actually adopt and which is exactly what the Practice Lab asks for. Verify both percentages against Babcock et al. (1995) or the summary in Babcock & Loewenstein (1997) before printing.  *(effort: small)*

### [HIGH · engagement] ## Confirmation and myside bias

> reasoning about evidence can become entangled with ideology and identity

**Problem.** This is the flattest possible statement of the most striking result in the motivated-reasoning literature, and the chapter loses the surprise entirely. Kahan's data-interpretation study gives the same 2x2 contingency table two labels — a skin-cream trial or a gun-control study — and finds that on the neutral version, higher numeracy produces better answers, while on the political version the most numerate partisans are the most likely to read the table in the direction that favors their side. Greater skill making the error larger is genuinely counterintuitive and is exactly what this chapter is about; right now the reader gets a summary sentence instead.

**Edit.** Add three or four sentences describing the 2x2 manipulation and the reversal (Kahan, Peters, Dawson & Slovic, 2017, Behavioural Public Policy), with the hedge the book's voice requires: replications have been partial and the effect is largest on issues with strong identity loading (e.g. Persson et al., 2021). Note this is a different paper from the Kahan (2013) already cited, so it needs adding to the reference list. This is the chapter's surprise-then-resolution moment and it is currently unused.  *(effort: medium)*

### [HIGH · insight] ## Confirmation and myside bias

> the weakness is choosing a test whose answer does little to distinguish the rival rules

**Problem.** The chapter gets within one sentence of the most important correction to the standard confirmation-bias story and stops. It says positive testing 'is not inherently irrational' but never states the condition under which it is fine and the condition under which it fails — which is known and is precisely the diagnostic the chapter's opening paragraph promises ('A bias label is useful when it identifies a process to examine').

**Edit.** Name Klayman & Ha (1987): positive testing is a generally sensible default that works well when the hypothesized set is smaller than or comparable to the true set, and fails specifically when the hypothesis is a subset of the truth — which is exactly the structure of 2-4-6, where 'increase by two' sits inside 'any ascending triple.' One added sentence converts 'confirmation bias' from a character flaw into a condition you can check, which is the chapter's whole thesis. Add Klayman & Ha (1987, Psychological Review) to the reference list; it appears nowhere in the book.  *(effort: medium)*

### [HIGH · structure] ## Attribution: behavior is visible, situations are not

> Negotiators who both want a fair settlement might expect that shared aim to help

**Problem.** A heading is missing here. After the attribution audit closes ('The audit reveals repairable systems...'), a double blank line is followed by roughly 500 words on self-serving fairness in negotiation (Babcock) and the bias blind spot (Pronin, Scopelliti) — all still nested under the attribution heading. The bias blind spot is a distinct named concept that the chapter treats as important, and it is currently unfindable in the table of contents. The stray double blank line strongly suggests a heading was lost during revision.

**Edit.** Insert '## When fairness is filtered through self-interest' before the negotiators paragraph, covering Babcock and the bias blind spot; or split into two headings if the bias blind spot deserves its own (it arguably does, since the 'reverse the roles' check that closes it is one of the chapter's three concrete tools). Either way the chapter currently has a section that is invisible to a reader navigating by heading.  *(effort: small)*

### [HIGH · visual] ## Attribution: behavior is visible, situations are not

> before converting an action into a judgment of character

**Problem.** This chapter has one figure and one table across roughly 2,600 words — the thinnest visual density of the three assigned chapters. From @fig-belief-protection-loop near the top to the summary table at the end, the only relief is one collapsed research note. The attribution material in particular is a five-step numbered list plus four dense paragraphs of abstraction with nothing to look at, and the self-serving asymmetry is inherently a two-dimensional object being described in one dimension.

**Edit.** Add a 2x2 figure for self-serving attribution: rows = outcome (success / failure), columns = actor (me / the other person), with the characteristic explanation in each cell ('my skill' / 'my bad luck' / 'their good luck' / 'their character'). The diagnostic claim — which the prose states but cannot show — is that the bias lives in the asymmetry across the diagonal, not in any single cell, so no one explanation is evidence of bias on its own. Caption it as that claim. It also gives step 3 of the attribution audit ('apply the same evidentiary standard') a picture, and breaks the chapter's longest unrelieved stretch.  *(effort: large)*

### [MEDIUM · clarity] ## Attribution: behavior is visible, situations are not

> were not necessarily better at avoiding other biases; believing oneself objective can reduce correction

**Problem.** A double negative that both muddles and understates. 'Not necessarily better at avoiding other biases' is a weak, hard-to-parse claim, and the second clause asserts a consequence ('can reduce correction') that reads as the author's inference rather than the study's finding. Scopelliti et al. actually found something sharper and more useful: bias blind spot is a stable individual difference, essentially uncorrelated with cognitive ability and decision-making skill, and people scoring higher on it took less advice from others and benefited less from debiasing training.

**Edit.** Restate directly: 'Scopelliti and colleagues (2015) found that the bias blind spot behaves as a stable individual difference, largely unrelated to cognitive ability or decision-making skill. People higher on it took less advice from others and gained less from debiasing training — believing oneself objective makes correction less likely, not more.' Same length, a real finding, and it lands the practical consequence the paragraph is reaching for.  *(effort: small)*

### [MEDIUM · clarity] Watch and test callout

> the short “kiss test” demonstration

**Problem.** 'Kiss test' names nothing the reader has encountered and nothing the chapter explains; it reads as an in-joke or a stray working title. A reader deciding whether to follow the link has no idea what they will see. The link itself is a bare youtu.be ID with no title or channel, so if it dies the reference is unrecoverable.

**Edit.** Say what it is — a street-interview demonstration of Wason's rule-discovery task in which people are given a number triple, propose further triples, and overwhelmingly propose only confirming ones — and give the video's title and channel alongside the URL so a dead link stays traceable. Drop 'kiss test' unless it is a term the video itself uses and the chapter defines.  *(effort: small)*

### [MEDIUM · consistency] ## Attribution: behavior is visible, situations are not

> also called the **correspondence tendency**, is the tendency to infer a stable personal disposition

**Problem.** Two issues. The standard alternative term in the literature is 'correspondence bias' (Gilbert & Malone, 1995), not 'correspondence tendency'; and the chapter's own learning goal already uses 'correspondence bias' while the body introduces 'correspondence tendency' in bold as the definitional term, so the chapter contradicts itself on its own key vocabulary. Separately, the section never mentions the best-established limit on the effect.

**Edit.** Standardize on 'correspondence bias' in both places and cite Gilbert & Malone (1995). If the author wants to signal that 'fundamental' is a misnomer — and the chapter's careful voice suggests he would — the stronger move is one added clause noting that the effect is substantially weaker in East Asian samples (Miller, 1984; Choi, Nisbett & Norenzayan, 1999), which makes the point empirically rather than terminologically.  *(effort: small)*

### [MEDIUM · engagement] ## Confirmation and myside bias

> Students rated the description as highly accurate.

**Problem.** Forer's paper is a classroom demonstration with a reveal, and the chapter throws away both the number and the theater. 'Highly accurate' is vague where a precise and memorable figure exists, and the detail that gives the study its bite — that the sketch was assembled from a newsstand astrology book and that every student received the identical text — is omitted.

**Edit.** Write it as the demonstration it was: Forer gave 39 students a personality sketch he had assembled from a newsstand astrology book, told each it was derived from their own test results, and asked them to rate its accuracy on a five-point scale; the mean was 4.26, and only then did he reveal that every student had received exactly the same page. Two sentences, one number, and the chapter's most reproducible classroom moment.  *(effort: small)*

### [MEDIUM · engagement] Opening scenario

> each of which would consume time and money and could disappoint some users

**Problem.** The opening scenario is well-constructed but its stakes are stated in exactly the vague, unquantified terms the chapter spends twenty pages arguing against. 'Time and money' and 'some users' cost the reader nothing to imagine, so the disagreement between the two colleagues carries no weight and the demand for a decisive test feels procedural rather than urgent.

**Edit.** Put a number and a deadline on it: the redesign consumes the only release window before the renewal cycle and roughly two quarters of the engineering team, and the wrong choice is not recoverable until the following year. Then the sentence 'they need a test that could separate the explanations' becomes something the reader wants rather than something the chapter asserts.  *(effort: small)*

### [MEDIUM · insight] ## Self-serving explanations

> varies across people, outcomes, development, and cultures

**Problem.** Mezulis et al. (2004) is cited twice in the chapter and never for a number, though it is a meta-analysis of 266 studies whose results are both large and sharply moderated. The list of dimensions along which the bias 'varies' is the vaguest possible rendering of the most decision-relevant finding in the paper, and a reader working in a multinational organization gets nothing usable from it.

**Edit.** Give the figures: across 266 studies the average self-serving attributional bias was large (d ≈ .96), but it was far smaller in Asian samples (d ≈ .30) than in US samples (d ≈ 1.05), and was attenuated among people with psychopathology. Then draw the implication the chapter is positioned to draw and does not: a debiasing procedure calibrated on one population may be solving a problem of a different size elsewhere, which is a caution the review-meeting advice in this section needs.  *(effort: small)*

---

## `chapters/11-when-context-rewrites-comparison.qmd`  (13 findings)

### [HIGH · accuracy] ## The first number enters first

> such as the last two digits of a social security number, could influence willingness to pay

**Problem.** The Ariely, Loewenstein & Prelec (2003) social-security-number anchoring result is presented as an established fact ("Higher arbitrary numbers led to higher valuations"), with no mention that this specific demonstration has failed to hold up under incentivized replication. This is the one claim in the chapter a well-read reviewer would challenge, and it sits next to genuinely robust anchoring evidence, so the reader cannot tell the two apart.

**Edit.** Keep the description but add a boundary sentence: "Later replications with real incentives found much weaker or null effects for this arbitrary-number procedure (Fudenberg, Levine, & Maniadis, 2012; Maniadis, Tufano, & List, 2014), so it is best read as a suggestive demonstration rather than a settled quantity." Then contrast explicitly: the classic comparative-judgment anchoring of Tversky and Kahneman replicated robustly in large multi-site tests (Klein et al., 2014, Many Labs). That contrast is itself the chapter's most useful accuracy lesson: not all anchoring evidence is equally strong.  *(effort: small)*

### [HIGH · accuracy] ## The decoy changes the comparison

> Yet its presence can make the print-plus-online option look like a better deal

**Problem.** The attraction effect is presented without any boundary conditions, even though a well-known 2014 exchange in the Journal of Marketing Research showed the effect is fragile outside numerically described, abstract attribute stimuli. Given that the chapter's central worked case is a classroom demonstration reported in a trade book, the absence of a replication caveat is the chapter's largest evidentiary gap.

**Edit.** Add a short paragraph (ideally as a `.research-lens` callout, which this chapter currently lacks): Frederick, Lee & Baskin (2014) and Yang & Lynn (2014) found the attraction effect largely disappears with realistic, perceptual, or richly described options; Huber, Payne & Puto (2014) replied that the effect is real but narrower than often claimed, strongest when attributes are numeric, few, and easily compared. Conclude with the decision-relevant point: the effect is a reason to check your menu, not a reliable lever to pull.  *(effort: medium)*

### [HIGH · consistency] ## The hiring case: context before evidence

> Return to the product-manager search.

**Problem.** "Return to" promises a callback, but "product manager" appears nowhere else in the book. The running hiring case is introduced in the Preface and Chapter 1 as an unnamed committee choosing between two finalists; it is never given a role title. A reader who takes the instruction literally will page backwards looking for a search that does not exist.

**Edit.** Either drop the role and link the actual case — "Return to the hiring committee from the [Preface](../index.qmd)" — or name the role at its first appearance in the Preface and use it consistently thereafter. The link matters: Chapter 12 links to Choice Architecture with a proper relative link, so this chapter's bare prose callback is also stylistically inconsistent.  *(effort: small)*

### [HIGH · engagement] ## The first number enters first

> Those who saw 65 gave higher estimates than those who saw 10

**Problem.** The book's single most famous anchoring demonstration is reported with no numbers at all. "Gave higher estimates" is exactly the flat, quantity-free phrasing that drains a striking result. The two-step procedure (compare first, then estimate) is also omitted, and that step is what later mechanism work is about.

**Edit.** Write it with the numbers and the procedure: "Participants first said whether the true percentage was higher or lower than the wheel's number, then gave an estimate. Median estimates were 25 after a wheel reading of 10 and 45 after a reading of 65 — a 20-point gap produced by a number everyone had watched a wheel generate." The reader should feel the size of the gap in the sentence, not infer it.  *(effort: small)*

### [HIGH · insight] ## The first number enters first

> In a budget discussion, last year's figure may become the starting point

**Problem.** The chapter's professional-stakes examples are all hypothetical and agentless ("a budget discussion," "a negotiation offer"). The single best piece of evidence for the chapter's actual thesis — that experts anchor on irrelevant numbers with real money and then deny it — is not cited anywhere. Without it, a skeptical manager can dismiss anchoring as a student-lab curiosity.

**Edit.** Add Northcraft & Neale (1987, Organizational Behavior and Human Decision Processes, 39(1), 84-97): experienced real-estate agents toured the same house and received identical ten-page information packets differing only in the listed price (lowest condition $65,900, highest $83,900). Their appraisals moved with the listing price by thousands of dollars, and most agents denied that the listing price had entered their judgment. Verify the exact appraisal means against the paper's tables before quoting them. This single study adds expertise, real dollars, and the denial finding, which links forward to the halo section and back to Chapter 7 on introspective access.  *(effort: medium)*

### [HIGH · structure] line 90, "## Three forms of contextual comparison"

> An anchor influences an estimate, a halo spreads an impression across attributes

**Problem.** Book-wide cross-reference topology is hub-and-spoke rather than a web, and it is measurably lopsided. Across all 42 chapters there are only 79 outbound chapter links, and chapters 1 and 42 carry 26 of them. Twenty chapters have ZERO outbound markdown cross-links in their bodies, and eight of those (03, 09, 11, 14, 23, 29, 33, 36) additionally have zero prose "Chapter N" references — they neither cite nor are reachable from the surrounding argument. Chapter 11 is the clearest casualty: it is the source chapter for anchoring, halo, and the decoy, three mechanisms invoked repeatedly in Parts V-VII, yet it points nowhere and almost nothing points back to it. The effect is that Parts II-VI read as free-standing lecture notes rather than a connected argument, which directly undercuts the "easy to follow" goal.

**Edit.** Set a floor of two outbound links per chapter, placed where a mechanism is first invoked rather than in 'Take it forward'. Highest-value additions, each with an obvious host sentence: ch11 line 46 ("Anchoring is not always irrational") to ch36 #anchor-only-when-you-can-defend-the-frame; ch11 line 98 to ch41 #the-structured-judgment-pipeline; ch33 line 89 (perspective-getting row) forward to ch38 #stage-disclosure-and-verification; ch14 to ch42; ch09 to ch13; ch23 line 83 to ch24. Chapter 1's handling of the decoy (line 123, short version plus a link to ch11 for the full evidence) is the model already working in the manuscript — apply that pattern throughout.  *(effort: large)*

### [MEDIUM · clarity] ## The decoy changes the comparison

> Identify the actual comparison before assigning a mechanism.

**Problem.** The chapter correctly warns that expensive-wine and premium-package effects are not attraction effects, then leaves the reader without any test for telling them apart. The instruction "identify the actual comparison" is the right idea stated too abstractly to execute, which is a shame because the distinction is genuinely crisp.

**Edit.** Give the one-line test immediately after: "Ask whether the added option is worse than one existing option on every attribute that matters and not worse than the other on every attribute. If yes, it is an asymmetrically dominated decoy. If it is simply more extreme on one attribute, you are looking at a compromise or range effect instead." A worked line against the wine example (the expensive bottle is not dominated - it is better on prestige) would take one more sentence and make the distinction stick.  *(effort: small)*

### [MEDIUM · consistency] ## Halo and horn effects

> Nisbett and Wilson (1977a) demonstrated a halo effect in evaluations of a lecturer

**Problem.** The "1977a" letter suffix has no matching "1977b" in this chapter, and Chapters 7 and 18 cite the companion 1977 paper (Telling More Than We Can Know, Psychological Review) as plain "Nisbett & Wilson (1977)" with no letter. Across the book the same author-year pair is therefore lettered in one place and unlettered in two others.

**Edit.** Pick one convention book-wide. Since two distinct 1977 Nisbett and Wilson papers are cited in the manuscript, the correct APA treatment is to letter both: 1977a for the Psychological Review paper and 1977b for the JPSP halo paper (ordered alphabetically by title), and update Chapters 7, 11, and 18 together.  *(effort: small)*

### [MEDIUM · engagement] opening scenario (before Core Idea)

> print alone at exactly the same price as print plus online

**Problem.** The opening hook withholds the prices that make the decoy absurd. "A more expensive print-plus-online subscription" is abstract; $59 versus $125 versus $125 is instantly, viscerally strange. The real numbers appear only 60 lines later, so the opening asks the reader to take the strangeness on faith.

**Edit.** Put the price list in the first sentence: "Web only, $59. Print plus web, $125. Then a third line appears: print only, $125 - the same price as the bundle that includes it." Then let the second paragraph do the analytic work it already does. The surprise-then-resolution structure is already present in the chapter; it is just sequenced so the surprise arrives without its detonator.  *(effort: small)*

### [MEDIUM · insight] ## Halo and horn effects

> They often did not realize that their global impression had influenced specific judgments.

**Problem.** The chapter stops one step short of the finding that makes Nisbett and Wilson memorable. Participants did not merely fail to notice the influence; when asked, many asserted the causal arrow ran the other way - that the instructor's irritating accent had lowered their overall rating of him. That reversal is the point, and stating it flatly loses it.

**Edit.** Add one sentence: "Asked directly, many participants reported the reverse causal story - that the accent and mannerisms had shaped their global impression, rather than the other way round." Then connect forward in half a sentence to Chapter 7's account of introspective reports, which the chapter currently leaves unmade even though the two findings are the same phenomenon.  *(effort: small)*

### [MEDIUM · structure] ## Learning goals

> Explain anchoring and insufficient adjustment.

**Problem.** The learning goal commits the reader to insufficient adjustment as the explanation of anchoring, but twelve lines later the chapter argues the opposite: "Insufficient adjustment is not a complete definition of anchoring." The chapter's most sophisticated move is contradicted by its own stated goal.

**Edit.** Rewrite the goal to match what the chapter actually delivers: "Distinguish the anchoring effect from the mechanisms proposed to explain it (insufficient adjustment, selective accessibility, scale use)." This also makes the goal testable against @fig-anchor-decoy, which is built around exactly that distinction.  *(effort: small)*

### [MEDIUM · structure] ## Three forms of contextual comparison

> An anchor influences an estimate, a halo spreads an impression across attributes

**Problem.** This is a three-sentence section under its own `##` heading, and it says the same thing as tbl-14-1 two sections later. The heading promises a synthesis and delivers a transition, which stalls momentum right where the chapter should be accelerating into its integrated case.

**Edit.** Delete the heading and fold the two sentences into the opening of "The hiring case," then move tbl-14-1 up to this position and give it a fourth column, "Diagnostic question" (anchor: would an unexposed estimator produce this number? halo: is there separate evidence for this criterion? decoy: does the preference survive deleting the dominated option?). One table doing the synthesis is stronger than a paragraph plus a table doing it twice.  *(effort: medium)*

### [LOW · clarity] ## Practice Lab

> Produce a **comparison audit** with three versions

**Problem.** The three deliverables are packed into a single 60-word sentence with a parenthetical workaround embedded in the first one. A reader trying to do this exercise has to parse the sentence twice to find out what three artifacts to produce.

**Edit.** Break into a numbered list with one line each: (1) an estimate collected before the anchor is revealed - use a fresh case or an unexposed colleague if you already know the number; (2) criterion-by-criterion ratings recorded before any overall impression; (3) the same menu with every dominated option deleted. Close with the reporting instruction as it stands. Chapter 13 already uses this numbered format for its familiarity audit, so this also aligns the two labs.  *(effort: small)*

---

## `chapters/12-framing-when-the-same-facts-become-different-decisions.qmd`  (15 findings)

### [HIGH · accuracy] opening scenario (before Core Idea)

> A report says that 90 of every 100 people survived a procedure for one year.

**Problem.** The chapter opens with the survival-versus-mortality frame and never cites the study that demonstrated it - McNeil, Pauker, Sox & Tversky (1982, NEJM). The chapter therefore asks readers to accept its premise hypothetically ("you may find yourself responding differently") when there is a landmark medical finding with real physicians available to establish it. This is simultaneously an accuracy gap and the single largest lost opportunity for stakes in the chapter.

**Edit.** Cite it in the Equivalent facts section: patients, graduate students, and experienced physicians chose between surgery and radiation for lung cancer. When outcomes were described as cumulative survival, about 18% preferred radiation; when the identical data were described as mortality, about 44% did. Add: the effect appeared among physicians, so clinical expertise did not neutralize it. Add McNeil et al. (1982) to the reference list.  *(effort: medium)*

### [HIGH · accuracy] ## Equivalent facts, different meanings

> people evaluated beef more favorably when it was labeled

**Problem.** The chapter cites Levin and Gaeth (1988) but omits the finding named in the paper's own title: the study measured evaluations before and after participants actually tasted the beef, and the framing gap shrank substantially (without disappearing) once they had direct experience of the product. Reporting only the label effect makes the study look like a simple demonstration and drops its most decision-relevant result.

**Edit.** Add two sentences: "Levin and Gaeth also had participants taste the beef. After tasting, the gap between the two labels narrowed but did not close." Then draw the implication the chapter needs: direct experience is a partial corrective to attribute framing, which is precisely why frames matter most for outcomes people cannot sample - a medical prognosis, a pension projection, a strategic forecast. That sentence is the chapter's missing "so what."  *(effort: small)*

### [HIGH · engagement] ## Equivalent facts, different meanings

> The outcomes were logically equivalent, but preferences changed.

**Problem.** The Asian disease problem is set up carefully across five sentences and then resolved with a numberless abstraction. "Preferences changed" and "People tended to be risk averse in the gain frame" describe a near-reversal in majority preference without letting the reader see it. The paragraph builds tension and then refuses to release it.

**Edit.** State the split: "In the gain frame, 72% chose the certain option. In the loss frame, describing exactly the same outcomes, 78% chose the gamble. A majority preference reversed on wording alone." Keep the existing hedge that follows ("shifted aggregate preferences"), which is correct and important - these are between-subject majorities, not individual reversals.  *(effort: small)*

### [HIGH · structure] ## Learning goals

> **Framing** concerns how information or a problem is described and organized.

**Problem.** Four paragraphs plus the personal-illustration callout sit between the Learning goals bullets and the first `##` section, so in rendered output they appear as the body of the Learning goals section. Chapters 11 and 13 both go straight from Learning goals to a `##` heading. This is the only structural deviation among the three chapters and it puts the chapter's definitional core in an unnavigable place - it will not appear in the table of contents or in any section link.

**Edit.** Insert a heading before line 33, for example `## What a frame is - and is not`, covering the definition, the reference-point paragraph, the personal illustration, and the prime/fluency/default distinction. While editing, unpack the closing sentence of that first paragraph: "only the first is a test using complementary numerical descriptions" requires rereading. Try "only the first holds the facts constant while varying the wording; the second changes which objective is on the table."  *(effort: medium)*

### [HIGH · visual] ## Framing memory and causality

> Participants gave higher speed estimates when asked how fast the cars were going when they

**Problem.** Every number from Loftus and Palmer lives in the figure caption and alt text; the body carries none. Worse, the body compares smashed versus hit while the caption's headline numbers compare smashed (40.8) versus contacted (31.8), so a reader who looks from text to figure finds the two do not line up. Readers of the EPUB or anyone skimming gets an entirely qualitative account of the chapter's most quotable study.

**Edit.** Put the values in the sentences: "Mean estimates ran from 31.8 mph for contacted through 34.0 for hit to 40.8 for smashed - a 9 mph spread produced by one verb." And for the second experiment: "a week later, 32% of the smashed group reported broken glass, against 14% of the hit group and 12% of controls. The film contained none." Then note the scale honestly - 45 participants in nine-person groups, 50 per group in Experiment 2 - so the reader knows this is a small classic supported by a large later literature (Loftus, 2005), not a single decisive study.  *(effort: small)*

### [HIGH · visual] ## Equivalent facts, different meanings

> Framing, priming, fluency, and defaults influence choice through different mechanisms.

**Problem.** None of this chapter's three figures is referenced in the body with an @fig- cross-reference, unlike Chapter 11, which discusses both of its figures explicitly. The figures therefore float beside the prose with no textual handshake, and in print the reader has no cue about when to look at them. The caption quoted here is also a label rather than a claim: it names four things and asserts they differ, without saying how.

**Edit.** Add one @fig- sentence per figure, as Chapter 11 does. For this one, rewrite the caption to carry the content: "Four mechanisms, four different questions: framing asks how the information is described, priming what was active beforehand, fluency how easily it processes, and a default what happens if you do nothing." Then in the body: "@fig-context-mechanisms separates the four because each implies a different correction."  *(effort: small)*

### [MEDIUM · accuracy] ## Equivalent facts, different meanings

> but effects are often modest and variable

**Problem.** The hedge is correct but unquantified, so a reader cannot tell whether "modest" means a five-point swing or a fraction of a percentage point. In the goal-framing literature it is closer to the latter, and that magnitude is decision-relevant: it argues against treating message framing as a strong lever for behavior change.

**Edit.** Add the magnitude: O'Keefe and Jensen's meta-analyses put the gain-frame advantage for prevention behaviors at roughly r = .03, a difference of a few percentage points, and found the loss-frame advantage for detection behaviors was concentrated in breast-cancer screening rather than general. Then state the implication plainly: framing reliably shifts what people notice; it shifts what they do only a little, and less than most communication advice implies. Verify the exact coefficients against the two meta-analyses.  *(effort: small)*

### [MEDIUM · accuracy] ## A personal illustration: from a fall to a somersault

> ## A personal illustration: from a fall to a somersault

**Problem.** The two .personal-example boxes (ch12:37, ch40:92) are single first-person anecdotes with no styling to distinguish them from evidence-bearing boxes. The manuscript is otherwise scrupulous about separating illustration from evidence — ch26:95 even carries the anchor #illustration-not-evidence — but the one device that would make that distinction visible does not exist.

**Edit.** Create .author-aside: border var(--book-muted) #607080, no tint, italic standing label 'ILLUSTRATION, NOT EVIDENCE'. Apply to ch12:37 and ch40:92. This extends the book's existing scientific discipline into the visual layer rather than adding decoration.  *(effort: small)*

### [MEDIUM · clarity] line 65, after the Asian disease paragraph

> The risky-choice chapter examines how probabilities, amounts, and reference points affect that comparison.

**Problem.** An unresolvable forward reference. "The risky-choice chapter" matches two chapter titles: Chapter 16 is literally titled *Risky Decision-Making: A Probability Is Not Yet a Feeling*, while the content actually promised — reference points and how they affect the comparison — is in Chapter 17, *Prospect Theory: Gains and Losses Begin at a Reference Point*. The three nouns split the difference: "probabilities" and "amounts" fit ch16's expected-utility material, "reference points" fits ch17. The reader cannot tell which chapter to turn to, and the book's own numbering offers no help because the phrase names neither.

**Edit.** Name the chapter and link it. Since reference points are the operative promise, use ch17: "[*Prospect Theory*](17-prospect-theory-gains-and-losses-begin-at-a-reference-point.qmd#the-prospect-theory-model) examines how probabilities, amounts, and reference points affect that comparison." If the intent was the expected-utility machinery instead, name ch16 — but not an unnamed "the risky-choice chapter", which is the one phrase that fits both.  *(effort: small)*

### [MEDIUM · engagement] ## Questions that contain an answer

> showed that survey responses can be sensitive to question wording, order, and context

**Problem.** Schuman and Presser's book is summarized in the most generic sentence available. The chapter is about how wording changes answers and here cites the definitive source on that without a single instance, so the paragraph teaches nothing the reader did not already grant.

**Edit.** Use the forbid/allow asymmetry, which is the canonical demonstration and perfectly suited to the chapter: asked whether the United States should forbid public speeches against democracy, roughly a fifth of respondents said yes; asked whether it should allow them, roughly half said no. Same policy, same respondents' population, a gap of twenty-odd points on a single verb. Verify the precise percentages against the 1981 volume before publishing, and keep the existing wording-order-context sentence as the generalization that follows the instance.  *(effort: medium)*

### [MEDIUM · engagement] ## Framing in management, negotiation, and policy

> Framing a negotiation as joint problem-solving can invite the information needed to discover a useful trade.

**Problem.** This section is two paragraphs of unbroken abstraction - negotiation frames, dissent framing, political frames - with no scene, no number, no named person, and no worked instance. It arrives right after the chapter's most concrete material (Loftus) and reads as a lull. It is also the section closest to the book's professional audience, so the flatness costs most here.

**Edit.** Anchor it with one short scene carried through both paragraphs: a supplier negotiation where one side opens with "let us find the arrangement that works for both of us" and shares its capacity constraint, and what that disclosure then costs or earns. Then state the asymmetry the current text only gestures at - a joint-problem-solving frame helps a party that has safeguards and hurts one that does not - which is a sharper and more honest claim than "language alone does not create psychological safety."  *(effort: medium)*

### [MEDIUM · insight] ## Ethical framing

> a 50% relative risk reduction or an absolute reduction of 1 in 1,000

**Problem.** The example stops one number short of the sentence that changes behavior. Readers who see "50% versus 1 in 1,000" still lack the translation clinicians actually use, and the chapter has just argued for transparent formats without demonstrating the most transparent one.

**Edit.** Add the number needed to treat: "Put a third way, 1,000 people must take the treatment for one of them to avoid the outcome. All three statements are true; the third is the one that tells a patient what to expect." This turns an abstract principle into a demonstration of the principle, in one sentence, using material already on the page.  *(effort: small)*

### [LOW · clarity] ## Practice Lab

> Produce a paired-frame brief that reports gains and losses

**Problem.** Four framing pairs, a per-pair annotation task, and a final deliverable are compressed into three sentences. The exercise is genuinely good but a reader has to reconstruct its structure before starting, and the four pairs are exactly parallel - the classic case for a table.

**Edit.** Render the four pairs as a two-column table (Pair | What becomes visible / what recedes) with the rows pre-labeled: gains vs losses, absolute vs relative, final state vs change, individual vs system. Leave the closing instruction - choose the version you would show a decision-maker and justify it - as prose, since that is the judgment the lab is really testing.  *(effort: small)*

### [LOW · clarity] line 35

> Prospect theory develops this reference dependence

**Problem.** A forward reference by theory name rather than by chapter, in a book that elsewhere names and links its targets. The reader is told prospect theory develops reference dependence but not that this is Chapter 17, and no link is offered. Combined with the ambiguous 'risky-choice chapter' pointer thirty lines later, Chapter 12 makes two unlinked gestures toward the same chapter without ever naming it — and ch12's single outbound link goes to ch40 instead.

**Edit.** Name and link it: "[*Prospect Theory*](17-prospect-theory-gains-and-losses-begin-at-a-reference-point.qmd#reference-dependence-the-zero-is-psychologically-constructed) develops this reference dependence; here we examine how the representation guides attention and comparison (Tversky & Kahneman, 1981)."  *(effort: small)*

### [LOW · consistency] ## Equivalent facts, different meanings

> The risky-choice chapter examines how probabilities, amounts, and reference points affect that comparison.

**Problem.** A bare prose pointer to an unnamed, unlinked chapter, in a file that twelve lines later uses a proper relative link to Choice Architecture. Given that the manuscript has been renumbered (the front-matter aliases record old filenames), unlinked verbal pointers are also the ones most likely to rot.

**Edit.** Replace with a link in the same form used for Choice Architecture, naming the chapter title. Do the same for the prospect-theory reference in the reference-points paragraph above, which currently says only "Prospect theory develops this reference dependence."  *(effort: small)*

---

## `chapters/13-accessibility-familiarity-and-ease.qmd`  (13 findings)

### [HIGH · accuracy] ## Accessible concepts interpret ambiguity

> Srull and Wyer (1979) similarly found that accessible hostility concepts could influence later impressions

**Problem.** Srull and Wyer's hostile-priming Donald paradigm is cited as supporting evidence with no caveat, yet a large multi-lab Registered Replication Report (McCarthy et al., 2018, Advances in Methods and Practices in Psychological Science) found effects far smaller than the original and near zero on several measures. This is doubly awkward because the chapter's own summary table flags contested social priming two pages later - the text and the table give the reader opposite signals about the same literature.

**Edit.** Add the replication in the same sentence: "A multi-laboratory registered replication of the Srull and Wyer procedure found effects much smaller than the original report (McCarthy et al., 2018), which is one reason to treat trait-construct priming as a real but small and condition-dependent phenomenon rather than a reliable lever." Add the reference. Consider the same treatment for Higgins, Rholes and Jones, noting what has and has not been re-tested, so that the paragraph's evidential status matches the table's.  *(effort: medium)*

### [HIGH · accuracy] ## Clarity without borrowed credibility

> have produced mixed results (Alter et al., 2007; Eitel & Kühl, 2016)

**Problem.** "Mixed results" understates what happened to the disfluency-as-debiasing claim. Alter et al. (2007) reported a hard-to-read font raising Cognitive Reflection Test scores in a sample of forty; a later replication programme with roughly seven thousand participants across seventeen studies found no such effect. Calling that "mixed" implies a roughly even evidential split that does not exist, and the chapter elsewhere is scrupulous about exactly this distinction.

**Edit.** Replace with the actual asymmetry: "A widely cited study found that a hard-to-read font raised performance on a reflection test in a sample of 40 (Alter et al., 2007), but a replication programme of 17 studies with about 7,000 participants found no such benefit (Meyer et al., 2015), and effects in learning contexts are small and condition-dependent (Eitel & Kühl, 2016)." Add Meyer et al. (2015, Journal of Experimental Psychology: General, 144(2), e16-e30) to the reference list. Giving the two sample sizes side by side is also the most vivid number pairing available anywhere in this chapter.  *(effort: medium)*

### [HIGH · consistency] line 140, masked-cues callout

> ::: {.callout-note icon=false #evidence-boundary-concealed-cues-are-not-mind-control}

**Problem.** This box carries three conflicting identities and no styling. Its div id says evidence-boundary, its visible title says 'Research note: processing masked cues', it contains a third stray anchor `[]{#research-lens-masked-primes-and-awareness}`, and it carries neither .evidence-and-boundary-conditions nor .research-lens. Its content is a textbook evidence boundary — it exists to stop readers concluding that masked cues implant goals — and it renders as a plain note beside 35 styled research lenses.

**Edit.** Change the opener to `::: {.callout-caution .evidence-boundary icon=false #evidence-boundary-concealed-cues-are-not-mind-control}`, retitle to 'Evidence Boundary: masked cues are not mind control', and delete the redundant inner anchor. The same pattern applies at ch01:137, whose anchor #two-suggestive-cases-with-weaker-evidence also names the type its class omits.  *(effort: small)*

### [HIGH · engagement] ## Repetition can become liking and truth

> Repeated exposure can increase liking for initially neutral stimuli

**Problem.** This 3,478-word chapter contains no empirical numbers at all apart from one invented figure in a fictional pilot. The mere-exposure and illusory-truth sections in particular describe two of the most demonstrable effects in the field entirely in the abstract - no stimuli, no exposure counts, no effect sizes, no samples. Three consecutive paragraphs pass without a single concrete instance.

**Edit.** Give the section two anchors. First Zajonc's method: nonsense Turkish-like words and Chinese-like characters shown 0, 1, 2, 5, 10, or 25 times, with rated liking climbing monotonically with frequency for shapes that meant nothing. Second, a real-world case - Moreland and Beach (1992), where four women attended a university lecture course 0, 5, 10, or 15 times without ever speaking to anyone, and students later rated the more frequently present women as more likeable and more similar to themselves. Then state Bornstein's boundary: the effect is largest for brief exposures and flattens or reverses with many repetitions, which is exactly the qualification the chapter's next sentence already gestures at.  *(effort: medium)*

### [HIGH · engagement] ## Repetition can become liking and truth

> repetition could increase perceived truth even for statements participants should have known were false

**Problem.** The Fazio et al. (2015) result is the most unsettling finding in the chapter and it is delivered in the most abstract possible form. "Statements participants should have known were false" costs the reader nothing; one of the actual items would land immediately, because the reader will feel the pull themselves.

**Edit.** Name an item: "Participants who could correctly answer that the Pacific is the largest ocean nonetheless rated the repeated statement 'The Atlantic Ocean is the largest ocean on Earth' as more true after seeing it twice." Then keep the existing practical sentence about source checking. The surprise-then-resolution structure is already in the paragraph; it just needs the surprise to be specific enough to feel.  *(effort: small)*

### [HIGH · insight] ## The risk of the familiar

> Run a **familiarity audit** with four questions

**Problem.** The four-question audit is the chapter's best original contribution, and it is never demonstrated. The chapter opens with a vivid running case - "Customers were not ready" repeated across three meetings - and returns to it in Take it forward, but never runs the audit on it. The reader is handed a tool and shown no worked instance, which is the same gap the chapter criticizes in fluent messages that assure rather than demonstrate.

**Edit.** Immediately after the four questions, work them on the chapter's own case in four short answers: (1) the phrase was repeated in three meetings by the same team; (2) no outcome feedback arrived - no test of positioning or onboarding was run; (3) the market has since changed in ways nobody checked; (4) a fair comparison would be a relaunch with corrected positioning against one with corrected onboarding. Four lines, and the audit stops being a checklist and becomes a demonstration. This also closes the loop the opening scene opens.  *(effort: medium)*

### [HIGH · structure] ::: {.callout-note icon=false #evidence-boundary-concealed-cues-are-not-mind-control}

> ::: {.callout-note icon=false #evidence-boundary-concealed-cues-are-not-mind-control}

**Problem.** This callout carries an id naming it an evidence-and-boundary note, contains an inline anchor `#research-lens-masked-primes-and-awareness`, and is titled "Research note" - but it declares neither `.research-lens` nor `.evidence-and-boundary-conditions`, so it renders as an unstyled plain note. Chapter 14, immediately after the same kind of inline anchor, writes `::: {.callout-note .research-lens icon=false}`. Across the manuscript there are 36 `.research-lens` and 11 `.evidence-and-boundary-conditions` callouts; this one looks like a dropped class rather than a choice.

**Edit.** Change the opening to `::: {.callout-note .research-lens icon=false #evidence-boundary-concealed-cues-are-not-mind-control}` (or `.evidence-and-boundary-conditions` if the id reflects the intent), matching Chapter 14's pattern. Worth grepping the whole manuscript for other callouts whose ids mention research-lens or evidence-boundary but whose class list omits the styled class.  *(effort: small)*

### [MEDIUM · clarity] ## Make accurate information fluent

> Teaching benefits from stable terms for recurring distinctions, provided each return does new work.

**Problem.** This sentence addresses the book's own pedagogical method, inside a section that is otherwise instructing the reader on how to write messages to colleagues. The audience switches mid-section from practitioner to author, and the sentence's referent - which terms, whose teaching - is never supplied. It reads as a note-to-self that survived into the draft.

**Edit.** Either cut it, or convert it into advice the reader can act on in their own organization: "Use the same term for the same distinction every time it recurs in your team's documents, and make each reappearance do new work rather than restate the earlier explanation." As written it is the only paragraph in the chapter that speaks past the reader.  *(effort: small)*

### [MEDIUM · consistency] ## Clarity without borrowed credibility

> Easy pronunciation has also affected risk judgments in some tasks

**Problem.** Song and Schwarz (2009) is introduced twice, twenty lines apart, in nearly identical form: first as "Easy pronunciation has also affected risk judgments in some tasks," then as "Easy-to-pronounce names have sometimes been judged less risky." The second occurrence reads as new material to a reader who has forgotten the first, and as repetition to one who has not - awkward in a chapter about the effects of repetition.

**Edit.** Cut the first mention from the @fig-fluency-pathway paragraph, which is already carrying five claims, and keep the fuller treatment in Clarity without borrowed credibility. While there, add one of the study's actual stimuli - a food additive named Hnegripitrom rated more harmful than one named Magnalroxate - so the claim has something concrete attached in the one place it survives.  *(effort: small)*

### [MEDIUM · consistency] ## Accessible concepts interpret ambiguity

> Chapters 6 and 9 distinguish feelings about an option from feelings carried into it.

**Problem.** Bare chapter numbers with no titles and no links, in a manuscript that has demonstrably been renumbered (the front-matter aliases record this chapter's former number 16, and tbl-16-1 still carries the old id). Chapter 12 links cross-references properly. A reader in EPUB or print has no idea which chapters these are, and the numbers will silently go wrong at the next reorganization.

**Edit.** Replace with titled relative links in Chapter 12's format, e.g. [Valuation](06-valuation-how-options-become-worth-choosing.qmd) and [What Feels Likely](09-what-feels-likely-availability-affect-and-resemblance.qmd). While there, update the stale table ids - tbl-16-1 here, tbl-15-1 in Chapter 12, tbl-14-1 in Chapter 11 - to match current chapter numbers, since the heading anchor in this chapter (#ch13-research-findings) has already been renumbered and the table id beneath it has not.  *(effort: small)*

### [MEDIUM · visual] ## Clarity without borrowed credibility

> A challenging comparison, retrieval test, premortem, or requirement to state a rival model

**Problem.** The productive-difficulty versus obstructive-strain distinction is the most practically useful idea in the second half of the chapter, and it is compressed into one dense paragraph of two parallel four-item lists followed by a bolded test question. Parallel lists of this shape are exactly what a small table renders better, and the section from the fluency figure to the summary table runs about 985 words with no visual break other than the familiarity-audit list.

**Edit.** Turn it into a two-column table headed by the diagnostic question - Productive difficulty (exposes structure) | Pointless strain (obstructs access) - with rows: challenging comparison / blurry slide; retrieval test / dense disclosure; premortem / confusing cancellation path; state-a-rival-model requirement / unfamiliar acronym. Keep the bolded test sentence as the table caption so the caption states the claim rather than labelling the contents.  *(effort: medium)*

### [MEDIUM · visual] ## Accessibility: memory prepares an answer

> An earlier cue can make a meaning more accessible

**Problem.** @fig-priming-pathway is never referenced in the body, while @fig-fluency-pathway is discussed at length. Within one chapter, one figure gets a paragraph of interpretation and the other gets nothing, so the first reads as decoration. Its caption is also the weaker of the two: it states a mechanism but not what the reader should take away.

**Edit.** Add a one-sentence in-text reference of the kind already used for the fluency figure, and make it carry the section's argument: "@fig-priming-pathway keeps the two inputs apart on purpose - the accessible meaning and the current evidence are separate sources, and treating the first as if it were the second is how accessibility turns into a diagnosis." That sentence is also the cleanest statement of the section's point, which is currently distributed across three examples.  *(effort: small)*

### [LOW · consistency] ## References cited in this chapter

> Ecker, U. K. H., Lewandowsky, S., & Chadwick, M. (2020).

**Problem.** The Ecker et al. (2020) entry sits after Zajonc at the very end of the list, outside alphabetical order, and is the only entry in the chapter using italics and a DOI - the formatting signature of an entry appended later. Separately, Alter et al. (2007) precedes Alter and Oppenheimer (2009), reversing APA's rule that a two-author entry precedes a same-first-author multi-author one.

**Edit.** Move Ecker et al. to its alphabetical position between Dechene and Eitel, and swap the two Alter entries. Then decide one formatting convention for the chapter: this list mixes plain journal titles with one italicized-and-DOI entry, whereas Chapter 11's list mixes italic and plain styles in the same way. A single pass for italics and DOIs across all three chapters would remove a visible inconsistency in the back matter.  *(effort: small)*

---

## `chapters/14-base-rates-conditional-probability-and-bayesian-updating.qmd`  (13 findings)

### [HIGH · accuracy] Research Lens: conjunction, disjunction, and dilution

> however well the detail matches the description (Tversky & Kahneman, 1983)

**Problem.** The conjunction fallacy is presented as an unqualified demonstration, with no mention of its best-established boundary condition: violation rates drop sharply when the question is posed in frequency terms ("how many out of 100 are...") rather than as a probability ranking. This is a genuine gap in a book this careful, and it is doubly awkward here because the chapter's own thesis two sections earlier is that frequency formats make set relations visible. The chapter is sitting on the explanation and does not connect it.

**Edit.** Add a sentence closing the loop: "The same format shift that helps with Bayes helps here. When the question is asked as a frequency — how many of 100 people fitting this description are bank tellers, and how many are bank tellers active in a social movement — conjunction violations fall substantially (Hertwig & Gigerenzer, 1999), which suggests part of the error is a failure to see the nested sets rather than a failure to hold the rule." Add Hertwig & Gigerenzer (1999), *Journal of Behavioral Decision Making, 12*(4), 275–305 to the reference list.  *(effort: medium)*

### [HIGH · engagement] ## Natural frequencies make Bayes visible

> often making Bayesian reasoning more transparent than isolated percentages

**Problem.** This is the chapter's central practical claim and it is delivered as an abstract assertion with a citation. The Gigerenzer and Hoffrage result has numbers, and the surrounding literature has the stakes: trained physicians reliably give an answer roughly ten times too high on exactly this problem. The chapter builds a hypothetical population of 10,000 and never tells the reader that professionals get this wrong in practice, which is the reason the whole technique matters.

**Edit.** Two additions. (1) Give the effect a size: Gigerenzer and Hoffrage reported roughly 16 percent Bayesian answers under probability formats versus roughly 46 percent under natural-frequency formats — a real improvement, and still fewer than half. (2) Add the stakes before the worked example, e.g. the screening studies in which a large majority of practising gynecologists, given a positive mammogram with a comparable base rate, estimated around 90 percent when the correct answer was under 10 percent (Gigerenzer et al., 2007, *Psychological Science in the Public Interest*). Verify both sets of figures and add the second reference to the list.  *(effort: medium)*

### [HIGH · engagement] Opening scenario (before Core Idea)

> A candidate passes a screening test that is described as

**Problem.** The opening is two paragraphs of rhetorical questions with no person, no organization, no stakes, and one number. Compare with Chapter 15's opening, which gives us a branch, a worst quarter, a manager arriving, and headquarters handing out praise — a scene with tension. Chapter 14 opens with "A candidate," "The committee," and four abstract questions in a row. The second paragraph then compounds it by announcing what the chapter will do ("The distinction is the spine of this chapter") rather than showing it.

**Edit.** Give the scene specifics that cost nothing in accuracy: a named role ("a hiring committee at a 400-person engineering firm"), a pool size ("1,100 applicants, 40 interview slots"), the vendor's claim in quotation marks, and one stake ("a bad hire in this role costs roughly a year of salary and a team's momentum"). Then cut or fold the signposting sentence — replace "The distinction is the spine of this chapter" with the committee actually asking the wrong question out loud and someone catching it.  *(effort: medium)*

### [HIGH · insight] ## Worked update: the same screen in two applicant pools

> Nothing about the assumed test characteristics changed; the starting population did.

**Problem.** The chapter stops one step short of the idea that would make it portable. It shows two posteriors (40% and 72.7%) but never names what stayed constant across the two pools. The likelihood ratio is 0.80/0.30 ≈ 2.7 in both, and that single number is the screen's actual evidential strength — the thing that can legitimately travel between populations when the posterior cannot. Without it the reader gets two arithmetic results and no transferable tool.

**Edit.** Add a short paragraph introducing the odds form: posterior odds = prior odds × likelihood ratio, with LR = P(+|strong)/P(+|not strong) = 0.80/0.30 ≈ 2.7. Then show it does both cases in one line: pool 1, odds 20:80 = 0.25 × 2.7 = 0.67 → 40%; pool 2, odds 50:50 = 1.0 × 2.7 = 2.7 → 73%. Close with the sentence the chapter is reaching for: the screen multiplies your odds by about 2.7 whatever pool you are in — what it does to your probability depends entirely on where you started.  *(effort: medium)*

### [HIGH · visual] ## Worked update: the same screen in two applicant pools

> Now place the same screen in a carefully preselected pool where 50% would meet the standard.

**Problem.** The chapter's headline result — the same screen yielding 40% in one pool and 72.7% in another — exists only as prose arithmetic. The one figure in the chapter illustrates the *secondary* disease example instead. The most surprising thing the chapter has to say is the thing with no picture.

**Edit.** Add a two-panel figure directly after this paragraph. Each panel is a 10×10 grid or stacked block of 10,000 applicants: left panel 20% base rate, right panel 50%, same shading scheme (dark = would meet standard, light = would not; hatched = passed the screen). Label true positives and false positives with the counts already in the text (1,600/2,400 and 4,000/1,500) and print the posterior beneath each panel (40% / 73%). Caption as a claim: "Identical sensitivity and false-positive rate. The only difference is how many strong performers were in the pool to begin with — and the same positive result now means almost twice as much."  *(effort: large)*

### [MEDIUM · accuracy] ## Reference classes are judgment calls

> Base-rate neglect is more likely when individuating detail feels causal

**Problem.** The sentence correctly names a moderator, but the chapter never tells the reader how robust base-rate neglect is overall — and the honest answer is that it is strongly format- and context-dependent. Neglect is largest with textbook word problems and single-case descriptions, and substantially weaker when base rates are learned through experienced sampling, are causally relevant to the outcome, or are described as randomly sampled. A book this careful about replication elsewhere should not present neglect as a uniform property of human judgment.

**Edit.** Add one hedged sentence with a source: "Neglect is not uniform. It is largest for single-case word problems with an incidental-sounding statistic, and substantially smaller when the base rate is learned from repeated experience, is presented as causally relevant, or is described as randomly sampled (Koehler, 1996). Treat it as a failure mode of a particular presentation, not a fixed human deficit." Add Koehler, J. J. (1996), *Behavioral and Brain Sciences, 19*(1), 1–17 to the reference list, and verify.  *(effort: small)*

### [MEDIUM · consistency] Research Lens: conjunction, disjunction, and dilution

> The resemblance chapter showed why a coherent story can feel probable.

**Problem.** Chapter 14 contains no outbound cross-reference links at all, while Chapter 15 links to Chapter 42 in the house format and Chapter 42 links back to both chapters with anchors. Here the chapter refers to "the resemblance chapter" (Chapter 9) in bare prose, giving the reader no way to get there. The concept index already treats Chapter 9 and Chapter 14 as a pair ("Statistical correction: Ch. 14"), so the link is expected and simply absent.

**Edit.** Use the house format: "[Chapter 9](09-what-feels-likely-availability-affect-and-resemblance.qmd) showed why a coherent story can feel probable." Add two more outbound links while you are there — from the reference-class paragraph to Chapter 15's outside-view material, and from "Take it forward" forward to Chapter 15, since the two chapters are a matched pair and neither currently points at the other.  *(effort: small)*

### [MEDIUM · engagement] ## Conditional direction matters

> The same reversal appears in court.

**Problem.** The prosecutor's fallacy is introduced with a hypothetical ("A one-in-a-million probability of a DNA profile") and then buried under a seven-item list of qualifications — selection, comparisons, lab error, relatedness, priors, "and the rest of the case." The most consequential misuse of conditional probability in modern public life is delivered without a case, a name, a date, or a consequence. This is the strongest concrete hook available anywhere in the chapter and it is unused.

**Edit.** Replace or precede the hypothetical with the Sally Clark case: the 1 in 73 million figure given in evidence for two infant deaths in one family, the assumption of independence between the two deaths that produced it, the Royal Statistical Society's public statement in 2001 that the figure had no statistical basis, and the quashing of the conviction in 2003. It is a real case, it carries the stakes, and it demonstrates *two* of this chapter's rules at once — the reversed conditional and the misuse of P(A∩B) = P(A)P(B|A) when the events are not independent. Add a source to the reference list and verify the dates.  *(effort: medium)*

### [MEDIUM · engagement] ## Bayes' rule restores the alternatives

> A useful Bayesian model includes the relevant alternatives and accounts for sample selection

**Problem.** This one-sentence paragraph is a list of four abstract nouns with no agent and no instance — sample selection, environmental change, measurement quality, parameter uncertainty. It tells the reader that things can go wrong without showing any of them going wrong, and it closes a section on an anticlimax right where the chapter's central formula has just been introduced.

**Edit.** Replace with one concrete failure carried by the running example. For instance: "The screen in this example was validated three years ago, on applicants who had already passed a résumé filter, against a performance rating written by the hiring manager. Each of those facts breaks a different part of the model — the prior no longer describes this pool, the false-positive rate was measured on a pre-selected group, and the criterion may be measuring manager agreement rather than job output. The arithmetic will still return a number."  *(effort: small)*

### [MEDIUM · insight] ## Reference classes are judgment calls

> A narrow class may be more relevant but noisier.

**Problem.** This section names the reference-class tradeoff well and then leaves it unresolved. The Practice Lab later asks the reader to "choose and defend two plausible reference classes" and show how the answer changes — but the chapter never demonstrates that once. The reader is asked to perform a move the book has only described, and the genuinely useful insight (that the class choice can swing the posterior further than any refinement of the test) stays implicit.

**Edit.** Work the hiring case through two nested classes with numbers, in four or five lines: e.g. all applicants (base rate 20%, posterior 40%) versus applicants who already cleared a technical screen (base rate 45%, posterior about 69%), with the same LR. Then state the point the chapter is one step away from: for a screen this strong, moving from a broad class to a defensible narrow one changes the answer more than improving the test's sensitivity by ten points would. That is what makes reference-class selection a substantive judgment rather than bookkeeping.  *(effort: medium)*

### [MEDIUM · visual] ## Probability begins with a model

> The subtraction prevents double counting.

**Problem.** The chapter contains no table at all — unusual for this book, and conspicuous here because the four probability rules are precisely the material a table handles better than prose. As written, complement, AND, and OR occupy three H3 subsections, each with a display equation and a paragraph, and the reader has to reassemble them from memory when the conjunction rule returns in the research lens and the union rule returns in Chapter 15's project example.

**Edit.** Keep the three subsections but add a compact summary table at the end of the section with columns: Rule | Formula | What must stay fixed | Typical failure | One-line example. Rows: complement (time horizon and outcome definition; "not finished by Friday" ≠ "the project fails"); AND (the conditioning branch; treating dependent events as independent); OR (the overlap; adding disjoint-looking routes); conditional (the denominator; reversing P(A|B) and P(B|A)). Give it an id so Chapter 15's project section can point back at it.  *(effort: medium)*

### [MEDIUM · visual] Figure: probability-judgment-map

> A positive result can come from either group.

**Problem.** The chapter's only figure is never referenced from the body text, so it sits beside the natural-frequency calculation rather than being used by it. The caption and fig-alt are both strong — the fig-alt in particular is a model of the genre — but the prose finishes the arithmetic and moves on to the next section without ever telling the reader to look at the tree it just described. The file name (probability-judgment-map) also no longer matches what the figure shows.

**Edit.** Add a pointer sentence before the figure: "@fig-probability-judgment-map traces both routes to a positive result and shows why the larger group supplies most of them." Then add one line after it drawing the moral the figure makes obvious and the arithmetic does not: the 9 percent false-positive rate looks small next to 90 percent sensitivity, but it is applied to a group 99 times larger, which is where the 891 comes from. Consider renaming the asset to natural-frequency-tree for maintainability.  *(effort: small)*

### [LOW · clarity] ## Conditional direction matters

> it rules out one linear relationship, not every probabilistic dependence.

**Problem.** A correct and important distinction is made in a single abstract clause with no instance, at the end of a section, where a reader who does not already know it will simply pass over it. Everything else in this section gets a concrete carrier (the test, the court case); this one does not.

**Edit.** Append a five-word example: "—if X is symmetric about zero and Y = X², the two are uncorrelated and yet Y is completely determined by X." One clause, no loss of precision, and the reader now owns the distinction rather than having read it.  *(effort: small)*

---

## `chapters/15-samples-randomness-regression-and-calibration.qmd`  (19 findings)

### [HIGH · accuracy] ## From a project story to a forecast system

> If the inside model gives 18 percent while comparable projects miss the date 55 percent

**Problem.** The worked example is internally impossible. The three delay routes are given marginals of 15%, 10%, and 20%, so any union of them must be at least 20%. An "inside model" of 18% is below the largest single component, which violates P(A∪B∪C) ≥ P(C) — the exact disjunction rule Chapter 14 states as non-negotiable ("P(A\cup B)\ge P(A)"). A careful reader coming straight from Chapter 14 will either think the book contradicts itself or lose confidence in the arithmetic.

**Edit.** Change 18 percent to a value above the largest marginal — e.g. "If the inside model gives 32 percent while comparable projects miss the date 55 percent." (With independence the union would be 1 − 0.85×0.90×0.80 ≈ 39%; positive dependence pulls it down toward 30%, which is the pedagogical point.) Alternatively, if 18% was meant as P(misses the final date) rather than P(any delay occurs), say so explicitly — "the schedule has slack, so only some delays push the final date" — because as written the two quantities read as the same thing.  *(effort: small)*

### [HIGH · engagement] ## Confidence must face a distribution

> people often construct an inside-view story of the steps that should occur

**Problem.** The planning fallacy paragraph is fully agentless and numberless: "people often construct," "it can produce optimistic point estimates." Buehler, Griffin, and Ross is already cited and contains one of the most quotable results in the book, and none of it appears. Three consecutive paragraphs here (Dunning–Kruger, planning fallacy, outside view) pass with no concrete instance until the rail project arrives.

**Edit.** Put the study's numbers in the sentence. Something like: "Buehler, Griffin, and Ross asked psychology students when they would finish their honours theses. The average prediction was about 34 days; the average actual completion was about 56. Fewer than a third finished by their own predicted date — and even their 'if everything went as badly as possible' estimate, roughly 49 days, still beat what actually happened." Verify the exact figures against the 1994 paper before publishing.  *(effort: small)*

### [HIGH · engagement] ## Small samples swing widely

> a tendency Tversky and Kahneman (1971) called belief in the **law of small numbers**

**Problem.** Only the label survives from a paper whose actual finding is the memorable part: the people Tversky and Kahneman caught making this error were professional research psychologists — several of them teachers of statistics — surveyed at conferences. "People often expect a small sample to resemble its population too closely" throws away the surprise-then-resolution structure that is sitting in the cited source.

**Edit.** State who the respondents were and what they got wrong: "The people Tversky and Kahneman surveyed were not undergraduates. They were experienced research psychologists at professional meetings, some of whom taught statistics — and they routinely recommended sample sizes far too small for the effects they hoped to detect, and expected a result that had just reached significance in a small study to replicate in another small study far more often than the numbers allow." Verify the specifics against the 1971 paper.  *(effort: small)*

### [HIGH · insight] ## Confidence must face a distribution

> Moore and Healy (2008) distinguish three patterns

**Problem.** The chapter takes Moore and Healy's taxonomy but leaves behind the paper's actual finding, which is the counterintuitive part. The three confidence errors do not merely differ; on hard tasks people overestimate their own score while simultaneously *under*placing themselves relative to others, and on easy tasks the pattern reverses. That reversal is what proves the assertion "Confidence is not one quantity" — as written, the sentence is a claim the reader has to accept on faith.

**Edit.** After the three bullets, add two sentences: "The three can move in opposite directions at once. Moore and Healy found that on difficult tasks people overestimate their own performance yet rank themselves below others, while on easy tasks they underestimate their score yet believe they are above average — so a single 'overconfidence' score can hide two errors pointing opposite ways." Verify the direction statement against the 2008 paper before publishing.  *(effort: small)*

### [HIGH · visual] ## Calibration makes confidence answerable

> A forecaster is **calibrated** when events assigned 70 percent occur about 70 percent

**Problem.** The chapter's title promises calibration and this section is its payoff, yet calibration is defined only in words and never drawn. Calibration and resolution are inherently two-dimensional ideas — the reliability diagram is the single most explanatory picture available in this chapter and it is missing. The reader is asked to hold "stated probability versus observed frequency across many forecasts" in their head with no visual support.

**Edit.** Add a reliability diagram: x-axis = forecast probability in deciles (0 to 1), y-axis = observed relative frequency (0 to 1), a 45° dashed line labelled "perfect calibration", and two plotted curves — one hugging the diagonal, one bowed away from it and labelled "overconfident: 90 percent forecasts come true about 70 percent of the time." Put a small bar histogram of forecast counts per bin along the bottom axis so resolution is visible as spread away from the base rate. Caption should state the claim, not the setup: "Calibration is the vertical gap from the diagonal; resolution is how far the forecasts spread along it. A forecaster can be well calibrated and still useless if every forecast sits in the middle bin."  *(effort: large)*

### [HIGH · visual] ## Small samples swing widely

> the standard error is about 0.158 for $n=10$ and 0.050 for $n=100$

**Problem.** Roughly 1,450 words run from the chapter opening to the first figure at the regression section — through coin sequences, standard errors, streaks, and clusters — with no figure, table, or callout. This is the longest visual desert in either chapter, and it covers the material most naturally shown rather than told. The 0.158 vs 0.050 contrast in particular is a picture stated as two decimals.

**Edit.** Add a figure here: two overlaid (or side-by-side, shared x-axis) sampling distributions of the sample proportion for p = 0.5, at n = 10 and n = 100, x-axis 0 to 1 labelled "observed success rate", with the central 95% band shaded on each. Mark the point "3 successes out of 3" on the n = 10 curve to tie it back to the interview panel two paragraphs earlier. Caption: "The population is the same in both panels. Only the number of observations differs — which is why a small sample can hand you a result the process would rarely produce again."  *(effort: large)*

### [MEDIUM · clarity] ## Small samples swing widely

> use hierarchical or shrinkage estimates where appropriate

**Problem.** "Hierarchical or shrinkage estimates" is technical vocabulary dropped without a gloss, in a chapter aimed at managers and students, roughly 45 lines before shrinkage is actually explained in the regression section. A reader who does not already know the term gets nothing from the advice, and a reader who reaches the regression section later has no cue that the two passages are about the same idea.

**Edit.** Gloss it in place and forward-link: "pull small-sample estimates toward the average of comparable cases rather than taking each at face value — the shrinkage logic developed in the regression section below." That also sets up the ẑ₂ = r z₁ formula as the formalization of advice the reader has already accepted.  *(effort: small)*

### [MEDIUM · engagement] ## Streaks require a process model

> showed that some earlier tests understated streakiness (Miller & Sanjurjo, 2018)

**Problem.** The hot-hand reversal is one of the genuinely startling results in behavioral science — a canonical finding taught for thirty years turned out to rest on a subtle selection artifact — and it is stated in a single subordinate clause with no mechanism and no magnitude. A reader will skim past it. The chapter's own thesis is that you must know what a process produces on its own before reading a pattern, and Miller and Sanjurjo is the perfect illustration of that thesis applied to the people who invented it.

**Edit.** Give the mechanism one concrete line and the correction a size: "Flip a fair coin 100 times and look at every flip that immediately followed a head. The expected proportion of heads among those flips is not one half — it is below it, because of how the sample of 'flips after a head' is selected. The original hot-hand tests used exactly this comparison, so they were scored against a benchmark that was already too high. Correcting the bias reverses the conclusion in the controlled shooting data the original study relied on." Verify the size of the corrected estimate against the 2018 paper before quoting a figure.  *(effort: medium)*

### [MEDIUM · engagement] ## Calibration makes confidence answerable

> This is the book's treatment of uncertainty helps distinguish a promising demonstration

**Problem.** The paragraph ends with a sentence about what the book is doing rather than doing it — meta-commentary that adds no content after the preceding sentence has already given three concrete instructions (hold out data, match the test to intended use, check whether probabilities support better actions). It is the kind of closing that flattens momentum right before the chapter's last substantive section. Note the quoted text as it stands also reads awkwardly.

**Edit.** Cut the final sentence entirely. The forward link to Chapter 42 and the three concrete instructions carry the paragraph. If a closing beat is wanted, make it a claim rather than a description of the book: "A model that is well calibrated on the data it was fitted to has demonstrated nothing."  *(effort: small)*

### [MEDIUM · insight] ## Regression to the mean

> Return to the branch manager. The recovery is real

**Problem.** The chapter builds the shrinkage machinery (Y = θ + ε, ẑ₂ = r z₁, the worked r = 0.40 case) and then returns to the branch manager without using any of it on him. The opening question — "How much of the recovery should count as evidence of good management?" — is answered qualitatively ("compare with similarly troubled branches") when the chapter has just handed the reader the tool to answer it with a number. This is the chapter's biggest missed payoff.

**Edit.** Put the branch through the formula before the qualitative advice: "Suppose the branch's bad quarter was two standard deviations below its peers and quarter-to-quarter performance correlates about 0.40. The model alone — with no manager, no rescue plan, nothing changed — predicts the next quarter at 0.8 standard deviations below average. That is 1.2 standard deviations of visible 'recovery' that headquarters is about to write a case study about." Then the existing paragraph about comparison groups lands as a method rather than a caution.  *(effort: medium)*

### [MEDIUM · structure] ## Confidence must face a distribution

> Suppose a city team proposes an 18-month rail-project schedule.

**Problem.** This one section runs roughly 700 words across four distinct topics — the Moore and Healy taxonomy, the Dunning–Kruger reanalysis, the planning fallacy, and the inside/outside view with a rail-project case — and ends a long way from what the heading promised. A reader who loses the thread here cannot recover it from the heading, and the Monty Hall research lens is then dropped in before the section resolves, breaking momentum a second time.

**Edit.** Split into two H2 sections. First: "Confidence is not one quantity" — the three-way taxonomy, the table, and the Dunning–Kruger discipline. Second: "The inside view needs an outside check" — planning fallacy, reference classes, rail project. Move the Monty Hall research lens to sit after "Clusters and the search for causes", where its point about how information was generated follows naturally from the search-space discussion rather than interrupting the confidence argument.  *(effort: medium)*

### [MEDIUM · structure] ## Confidence must face a distribution

> as @tbl-confidence-calibration shows

**Problem.** The table is invoked here but does not appear until roughly 450 words later, after the Dunning–Kruger paragraph, the planning-fallacy paragraph, and the rail-project paragraph. Worse, the table contains a "Planning fallacy" row referring to material the reader has not yet met at the point of the reference. The reader either scrolls forward and loses the thread, or reads the reference as a promise and forgets it.

**Edit.** Move the table to sit immediately after the three-bullet taxonomy and before the Dunning–Kruger paragraph, and drop the "Planning fallacy" row from it — the planning fallacy gets its own treatment two paragraphs later and does not need to pre-empt itself. Alternatively, if the four-row table is wanted intact, move the @tbl reference sentence down to introduce the table where it actually sits.  *(effort: small)*

### [MEDIUM · structure] ## Practice Lab

> Choose one event that will resolve within four weeks.

**Problem.** Two labs are deliberately deferred — ch15 ('within four weeks') and ch21 ('For a week, record relevant opportunities') — which is pedagogically right, but neither is split, so a reader working through the chapter today finishes with nothing checkable and no cue to return. ch39 and ch22 have the same shape with a review date but no Part A/Part B structure.

**Edit.** Split each into Part A (today, 20-25 min, with its own success check) and Part B (dated, 10 min). ch15 Part A: the full ledger, checked by 'a stranger could resolve the event without asking you a question, and every percentile adjustment has a stated reason.' ch21 Part A: episode, explanation, next-encounter plan, plus a numeric prediction for the coming week. Full versions in chapter_notes Part 2, items 10-11.  *(effort: medium)*

### [MEDIUM · visual] ## Confidence must face a distribution

> later work suggests that any distinctive metacognitive component may be smaller

**Problem.** The Dunning–Kruger debunk is handled correctly in prose — this is exactly the right hedge and the Gignac and Zajenkowski citation is apt — but the argument is asserted rather than shown. The claim is a visual claim: the familiar quartile chart can be produced by a process containing no metacognitive difference at all. Telling the reader that is far weaker than letting them see the same shape emerge from noise.

**Edit.** Add a two-panel figure with identical axes (x = performance quartile, y = mean percentile, two lines for self-assessment and actual score). Left panel: the familiar crossing pattern from self-assessment data. Right panel: the same chart generated from simulated data in which self-assessment is pure noise plus a constant, with no skill-linked metacognition built in. Caption as the claim: "Both panels show the same shape. Only the left one came from people — which is why the picture alone cannot tell you whether poor performers have a metacognitive problem."  *(effort: large)*

### [MEDIUM · visual] Figure: regression-conditional-shrinkage caption

> A fixed-seed teaching simulation draws 50 observations

**Problem.** The caption is a methods note, not a claim. It leads with the seed number and the data-generating process and only reaches the point — that the prediction line is flatter than the identity line, and that flatness *is* regression — in a compressed final clause. A reader scanning captions learns the simulation parameters and not the idea. The figure is also never referenced from the body text, so it floats beside the section rather than being used by it.

**Edit.** Invert the caption: lead with "The prediction line is flatter than the identity line, and that flatness is regression to the mean: an extreme first measurement predicts a less extreme second one, with no change in underlying ability required. Here a value two standard deviations above average predicts 0.8." Move the simulation parameters (seed, DGP, sample r) to the end of the caption or a note. Then add a sentence in the body pointing at it — "@fig-regression-conditional-shrinkage shows what this looks like for 50 pairs of measurements" — since the figure currently does explanatory work the prose never claims.  *(effort: small)*

### [LOW · accuracy] ## Regression to the mean

> The flight-instructor example illustrates the attribution trap.

**Problem.** The flight-instructor story is an illustrative observation reported by Kahneman and Tversky, not a controlled study, and the chapter — which elsewhere is scrupulous about distinguishing what a study showed from what people infer — presents it in the same register as the empirical material around it. Readers who later learn it was an anecdote may discount the surrounding, better-evidenced content.

**Edit.** Add three words of provenance: "The flight-instructor example — an observation Kahneman and Tversky reported rather than a controlled study — illustrates the attribution trap." The point survives intact, and the honesty is consistent with the book's handling of Dunning–Kruger two sections later.  *(effort: small)*

### [LOW · accuracy] ## Calibration makes confidence answerable

> BS=(p-o)^2

**Problem.** This is the modern binary convention (range 0 to 1), but Brier's 1950 definition summed the squared errors across all forecast categories, which for a binary event gives a range of 0 to 2 — exactly twice this. The citation points to the 1950 paper for a formula the 1950 paper does not contain in this form. Minor, but this book is precise enough that a reader checking the source will notice.

**Edit.** Add a parenthetical: "(Brier's original score summed across categories; the half-Brier form shown here is the modern convention for binary events and ranges from 0 to 1.)" One clause, and the citation becomes defensible as written.  *(effort: small)*

### [LOW · clarity] '## Calibration makes confidence answerable' (line 151)

> define the event precisely, start from reference classes, decompose the problem

**Problem.** The forecasting substance is genuinely complete — Brier scores, resolution, the forecast ledger, reference classes, estimate-first-discuss-second in ch41 — but three terms a reader will arrive with are missing entirely from the manuscript. 'Superforecast' appears zero times and Tetlock & Gardner (2015) is uncited, so a reader who has heard the word finds nothing; the concept index cannot route it. 'Prediction market' and 'Delphi' also appear zero times, leaving ch41's '### Preserve independence, then aggregate' section describing simple and weighted averaging as if they were the only aggregation mechanisms available.

**Edit.** Two small edits, no new sections. In ch15's calibration paragraph, name the forecasting-tournament work explicitly and cite Tetlock & Gardner (2015) alongside Mellers et al. (2014), so the term resolves. In ch41's aggregation section, add ~200 words giving prediction markets and Delphi as two further ways to combine judgments without discussion, each with its failure mode — markets need enough participants and a resolvable question; Delphi needs facilitators who do not quietly steer toward the median, which is the pressure the section already warns about.  *(effort: small)*

### [LOW · consistency] Before ## Practice Lab

> []{#ch15-research-findings}

**Problem.** This anchor is referenced nowhere in the repository — not by the concept index, not by any chapter, not by any appendix — and it sits immediately before the Practice Lab, so anything that did point at it would land on the wrong content. The other explicit anchor pattern in these chapters (#research-lens-conjunction-disjunction-and-dilution in Chapter 14) is genuinely used by concept-index.qmd, which suggests this one is a leftover from a removed section.

**Edit.** Delete the anchor, or if a cross-reference to Chapter 15's research material is intended somewhere, move it to the section it should target (most likely "Streaks require a process model" or the Dunning–Kruger paragraph) and add the corresponding entry in concept-index.qmd.  *(effort: small)*

---

## `chapters/16-risky-decision-making-a-probability-is-not-yet-a-feeling.qmd`  (15 findings)

### [HIGH · engagement] (opening scenario, before ## Core Idea)

> A small organization receives a quote for cyber insurance.

**Problem.** The opening is a single paragraph with no name, no sector, no premium, no loss figure, no date — in a chapter whose entire argument is that numbers alone are not enough. The template calls for a 2-4 paragraph concrete scene; ch17 and ch18 both deliver one. As written the reader has nothing to picture and nothing to carry forward.

**Edit.** Expand to three paragraphs with specifics: name the organization type and size (a 40-person clinic; 11,000 patient records), the quote (€45,000), the line in the spreadsheet that makes it look expensive (€27,000 average annual loss), and the moment the question changes ('could we make payroll in March if the systems were encrypted in February?'). Use the same figures the Worked application will later resolve, so the chapter opens and closes on one case.  *(effort: medium)*

### [HIGH · engagement] ## Optional research and application notes (multiplicative-risk lens)

> The expected terminal value is pulled upward by rare paths with many gains

**Problem.** The most arresting number in the chapter — €1,420,429 expected against roughly €1.95 typical, from the same gamble — sits inside a collapse=true block at the very end, after the references-facing material. Many readers will never open it. Meanwhile the main body's portfolio extension makes a weaker version of the same point with no comparable punch.

**Edit.** Promote a three-sentence version into 'Extension: one project or a portfolio?': state the two numbers (€1.42 million expected terminal wealth, about €1.95 for the median path of 26 gains and 26 losses) and the resolution (expected wealth is an average over paths almost none of which will be yours; the geometric mean return is -15.1% per round). Leave the full derivation in the collapsed lens. This is surprise-then-resolution the chapter already owns and currently hides.  *(effort: small)*

### [HIGH · insight] ### Certainty equivalents and risk premia

> If the outcomes are changes around wealth, then wealth must enter the calculation.

**Problem.** This is the hinge that motivates the whole next chapter, and it is asserted rather than shown. The reader has just been told the risk premium is 25 — half the expected value — and is now told that this depended on a normalization, without seeing how much it depended on it.

**Edit.** Add two sentences with the contrast computed: with the same u(w)=sqrt(w) and the same 50-50 gamble of 0 or 100, a decision-maker with zero starting wealth has a risk premium of €25, while one with €10,000 in the bank has a risk premium of about €0.06 (certainty equivalent €49.94 against an expected €50). Same function, same gamble, a 400-fold difference in implied risk aversion. That number makes the wealth-dependence problem unforgettable and hands the reader a concrete reason why prospect theory codes changes rather than final states.  *(effort: small)*

### [HIGH · structure] ## Learning goals / ## Worked application: should we insure this exposure?

> Compare expected value with expected utility in one consequential insurance decision.

**Problem.** The first learning goal promises a numerical EV-versus-EU comparison in an insurance decision. Neither 'Insurance: expected loss is not the whole premium' nor the 'Worked application' contains a single number. The worked application is four generic questions. The chapter therefore does the EU arithmetic only on an abstract 0/100 lottery and never on the case it opened with.

**Edit.** Put real figures in the cyber-insurance case and run the comparison in the Worked application: e.g. premium €45,000/yr; modelled attack probability 3%/yr; worst credible loss €900,000 (restoration + 6 weeks of interrupted service + notification and liability); liquid reserves €250,000. Then show both readings side by side: expected loss = €27,000, so on expected money alone declining saves €18,000 a year — while the uninsured bad state is €650,000 short of reserves, i.e. not a bad year but the end of the organization. That single contrast delivers the learning goal and needs no utility function to be honest.  *(effort: medium)*

### [MEDIUM · accuracy] ## Risk, uncertainty, and ambiguity

> This is **risk** in the narrow decision-theory sense.

**Problem.** The chapter bolds risk, uncertainty, and ambiguity as technical terms without attributing the risk/uncertainty distinction to Knight (1921), who introduced it. A grep of the whole manuscript finds no Knight citation anywhere. For a book this careful about provenance, introducing a named distinction unattributed is a visible gap, and a reader who meets 'Knightian uncertainty' elsewhere will not know it is the same idea.

**Edit.** Add the attribution inline — 'the distinction between measurable risk and unmeasurable uncertainty is usually traced to Knight (1921), with a parallel argument in Keynes (1921)' — and add Knight, F. H. (1921). *Risk, uncertainty, and profit*. Houghton Mifflin, to the reference list. One clause, and it also earns the term 'Knightian' for later chapters.  *(effort: small)*

### [MEDIUM · consistency] ## Opening puzzle: the same expected value, a different choice

> ## Opening puzzle: the same expected value, a different choice

**Problem.** Ch16 has two openings: an unheaded cyber-insurance paragraph, then Core Idea and Learning goals, then a separate headed 'Opening puzzle' with the €50 gamble. Ch17 and ch18 both put the headed opening puzzle first and then Core Idea and Learning goals. The result in ch16 is that the insurance scene is dropped at line 20 and not picked up again until the Worked application some 2,500 words later, while the €50 puzzle arrives after the reader has already been told the Core Idea.

**Edit.** Align with ch17/ch18: lead with the headed opening puzzle, and fold the cyber-insurance scene into it as the consequential version of the same question (sure €50 versus a coin flip is the toy; €45,000 certain versus a 3% chance of €900,000 is the real one). Then Core Idea, then Learning goals. This also lets the €50 gamble and the insurance case share one set of numbers.  *(effort: medium)*

### [MEDIUM · engagement] ## Ethics: who receives the expected benefit, and who bears the tail?

> shifting catastrophic losses onto employees, customers, taxpayers, or future stakeholders

**Problem.** Three paragraphs of generality with no instance. This is the most morally charged section of the chapter and the only one with no concrete referent at all — the reader is told that tail risk can be transferred but never shown a case where it was.

**Edit.** Anchor it with one named, dated, uncontroversial case and a number, then return to the insurance decision. A clean option: a firm that carried a positive-expected-value exposure whose tail was absorbed by a public balance sheet, stated in one sentence with the figure. Then apply the same test to the clinic: if the policy covers the clinic's restoration costs but not patients' delayed treatment, the organization has bought protection for the party that chose the exposure and not for the party that bears it.  *(effort: medium)*

### [MEDIUM · engagement] ## Take it forward

> The final choice may still be difficult, but the team now knows

**Problem.** Nine of the 42 'Take it forward' sections are summary only — they describe what a fictional character can now do and never address the reader: ch01, ch16, ch18 ('The supplier team's task is…'), ch19 ('For the manager…'), ch22, ch23 ('In both cases, better advice begins by making the dependence visible'), ch26, ch28 ('they no longer need to guess who owns the next step'), ch30. The other 33 end with a second-person commitment ('Before your next consequential choice, write…', 'At your next meeting, ask who…'), which is what the section title promises.

**Edit.** Add one second-person commitment sentence to each of the nine. ch16: 'Before your next insurance or capacity decision, write what your organization could do in each plausible state with and without the contract, and mark the state you could not absorb.' ch23: 'Before your next cross-team conflict, write what each side can do without agreement, then name the one rule — timing, monitoring, or exit — you could actually change.' ch28: 'Before your next escalation, write the sentence a junior colleague could use to question your assessment without first proving you wrong.'  *(effort: medium)*

### [MEDIUM · insight] ### Why do people buy insurance and lottery tickets?

> A globally concave utility function over money cannot explain paying for an unfavorable monetary gamble.

**Problem.** The chapter poses its sharpest puzzle and then stops: it lists four candidate explanations and leaves them unranked and unresolved. Two obvious moves are missing. First, Friedman and Savage (1948) — the canonical utility-theoretic answer, a function concave then convex then concave — is never named. Second, the chapter never tells the reader that the very next chapter resolves this puzzle with the fourfold pattern, where low-probability gains and low-probability losses fall in opposite risk-attitude cells.

**Edit.** Add two sentences: name Friedman and Savage's (1948) wiggly utility function as the classic within-EU repair and say briefly why it is uncomfortable (it requires an odd, ad hoc wealth-dependent shape). Then close with a forward link: 'Prospect theory answers the same puzzle differently, by letting the weight on a small probability rather than the curvature of utility do the work — see the fourfold pattern in the next chapter.' Add Friedman & Savage to the reference list.  *(effort: small)*

### [MEDIUM · insight] ## Risk communication: show the denominator and the consequence

> The absolute reduction is 1 in 1,000, or 0.1 percentage points.

**Problem.** The example stops one step short of the number that patients and managers actually use. Having established 2 in 1,000 versus 1 in 1,000, the chapter gives the relative and absolute forms but not the number needed to treat, which is the format that makes the magnitude physically imaginable.

**Edit.** Add one sentence: 'A third equivalent statement: about 1,000 people must take the treatment for a year for one of them to avoid the outcome — and the other 999 carry whatever costs and side effects it brings.' Then note that all three numbers describe the identical change, which is precisely why the choice of format is a communication decision rather than a reporting detail.  *(effort: small)*

### [MEDIUM · visual] ## The Allais pattern: certainty does not cancel cleanly

> 89% chance of 1, 10% chance of 5, and 1% chance of 0

**Problem.** The four Allais prospects are given as two bulleted pairs, and the cancellation argument then asks the reader to hold all twelve probability-outcome pairs in memory and mentally subtract a common component. This is exactly the kind of argument that a small table makes obvious and prose makes laborious.

**Edit.** Replace the bullets with a 4-row by 3-column table: rows A, B, C, D; columns for the outcomes 0, 1, and 5 (millions); cells holding probabilities (A: 0/1.00/0; B: .01/.89/.10; C: .89/.11/0; D: .90/0/.10). Shade or rule off the common .89 column entry so the reader sees at a glance that A and B share an 89% chance of 1 while C and D share an 89% chance of 0. Caption it as the claim, not the label: 'Replacing the shared 89% consequence turns the first pair into the second; independence says the ranking should survive that replacement.'  *(effort: medium)*

### [MEDIUM · visual] ## The Ellsberg urn: risk is not ambiguity

> First choose a bet that pays if **red** is drawn

**Problem.** The Ellsberg contradiction is presented in four prose paragraphs. The canonical presentation is a payoff matrix, and without it the reader has to reconstruct which bet pays in which colour state before the P(R)>P(B) and P(B)>P(R) derivation can land.

**Edit.** Add the standard 4x3 payoff table: rows are the four bets (Red, Black, Red-or-Yellow, Black-or-Yellow); columns are the three colour states with their counts in the header (Red: 30, Black: ?, Yellow: ? — 60 between them); cells are 100 or 0. The reader then sees directly that the yellow column is identical within each pair, which is the whole argument. Keep the existing prose derivation immediately below it.  *(effort: medium)*

### [MEDIUM · visual] ### Curvature and attitudes toward a mean-preserving risk

> expected utility is 5, the certainty equivalent is 25, and the risk premium is 25

**Problem.** The figure is placed under 'Curvature' but its caption announces the certainty equivalent (25) and risk premium (25) that the text does not derive until the next subsection. The reader meets the answer before the question. The figure is also never pointed at anywhere in the body, so nothing tells the reader what to look at or when.

**Edit.** Move the figure to immediately after the sentence 'Expected final wealth is 50, so the risk premium is 25' and add one pointing sentence: '@fig-risky-decision-map shows the geometry: the risk premium is the horizontal gap between the expected value and the point on the wealth axis where the chord meets the curve.' Also trim the caption's second sentence, which currently describes the companion panel rather than stating its claim.  *(effort: small)*

### [LOW · clarity] After the Allais discussion (line 143)

> Certainty, regret, misunderstanding, probability weighting, and response noise can contribute

**Problem.** Regret is offered here as one of five candidate explanations for the Allais pattern, and it recurs in ch01, ch17, ch23, and ch36 — nine incidental appearances across the book — without ever being defined. Anticipated regret and anticipated disappointment are distinct mechanisms with distinct implications for choice, and the book uses the word as if the distinction had been made. This is the one place where the book's otherwise scrupulous habit of defining a mechanism before invoking it lapses.

**Edit.** Add a 150-word definition beside the Allais list distinguishing anticipated regret (comparison with the outcome of the option not taken, which requires learning what the forgone option would have produced) from disappointment (comparison with a better outcome of the option taken). Then note the practical consequence the book cares about: whether feedback about the forgone option will be received changes which mechanism can operate, which is a design variable in ch40 and a preparation variable in ch36.  *(effort: small)*

### [LOW · structure] ## Take it forward

> the team now knows which losses, assumptions, and obligations drive it

**Problem.** The section describes what the fictional team has achieved rather than committing the reader to an action. Compare ch17's 'Take it forward', which instructs the reader to translate the outbreak programs into survivors and deaths before choosing — a real assignment.

**Edit.** Rewrite as a reader instruction with a stopping condition: 'Take one exposure you currently carry uninsured. Write down the worst credible loss, your liquid reserves, and the ratio between them. If that ratio exceeds one, you are self-insuring something you cannot afford — decide this week whether that is a choice or an oversight.'  *(effort: small)*

---

## `chapters/17-prospect-theory-gains-and-losses-begin-at-a-reference-point.qmd`  (15 findings)

### [HIGH · accuracy] ## Framing changes the comparison; check equivalence

> Ruggeri and colleagues (2020) replicated 94% of tested items

**Problem.** This sentence directly follows 'The original Asian-disease results came from separate groups answering hypothetical problems', so a reader will take Ruggeri et al. (2020) as the replication of the Asian-disease framing effect. It is not. Ruggeri et al. tested items from Kahneman and Tversky (1979); the Asian-disease problem is from Tversky and Kahneman (1981) and was not part of that set. The chapter's best evidence for its own opening puzzle is therefore evidence for a different set of problems.

**Edit.** Say what Ruggeri et al. tested: 'a preregistered multinational replication of the Kahneman and Tversky (1979) problem set — the reflection, certainty, and isolation items rather than the 1981 outbreak framing.' Then add a framing-specific citation: the Many Labs project (Klein et al., 2014, *Social Psychology*, 45(3), 142-152) included the Asian-disease framing item and found it among the most robustly replicating effects across 36 samples; verify and quote their reported effect size. Add Klein et al. to the reference list.  *(effort: small)*

### [HIGH · accuracy] ### The value function: sensitivity diminishes with distance

> estimated $\alpha=\beta=0.88$ and $\lambda=2.25$ in their data

**Problem.** The three numbers that the entire literature treats as canonical are given with no provenance. The later critique — 'The familiar statement "losses loom about twice as large as gains" turns a model estimate into a law' — is correct but abstract, and it lands far weaker than the provenance itself would. The reader is not told these are median estimates from a single small study.

**Edit.** State the sample where the parameters appear: 'These are median estimates fitted to the choices of 25 graduate students in a single 1992 study.' One clause, and it does more debunking work than the paragraph currently devoted to the task — while being strictly more accurate. Then let 'turns a model estimate into a law' land on top of it.  *(effort: small)*

### [HIGH · engagement] ### Worked calculation: a low-probability gain

> If $w(0.01)>0.01$, the small chance receives more decision impact

**Problem.** A section titled 'Worked calculation' contains no worked calculation. It writes the formula, then says the answer depends on both functions and the reference point. The reader who came to this heading for a number leaves without one, and the possibility effect — the chapter's explanation of lottery tickets — remains an assertion.

**Edit.** Plug in the parameters the chapter has already given. With gamma = 0.61, w(0.01) = 0.055: a 1% chance carries roughly five and a half times its objective probability in decision weight. With alpha = 0.88, the prospect value of a 1% chance at €10,000 is 0.055 x 3,311 = 183 value units, against 57.5 for €100 in hand — a certainty equivalent of about €372, more than three times the expected value. That is why a €2 ticket sells. Then state the boundary: change gamma to 0.8 and the advantage shrinks; make the ticket price a coded loss and it shrinks again. The hedge is more convincing once the reader has seen what is being hedged.  *(effort: medium)*

### [HIGH · insight] ## Opening puzzle: 200 saved or 400 lost? / ### The fourfold pattern of risk attitudes

> Why can representing those consequences as gains or losses change which risk people will take?

**Problem.** The chapter asks this question in the opening and never answers it with the machinery it spends the next 2,000 words assembling. The reader is given a value function, a weighting function, and fitted parameters, and is then left to assume the model explains the outbreak reversal. It does — and showing it would be the strongest surprise-then-resolution moment available anywhere in these three chapters.

**Edit.** Add a short subsection after the fourfold pattern that runs the opening problem through the model with Tversky and Kahneman's own 1992 parameters. Gain frame, reference point 'all 600 die': A = v(200) = 200^0.88 = 105.9; B = w(1/3) x v(600) = 0.336 x 277.5 = 93.6, so A is preferred. Loss frame, reference point 'nobody dies': C = -2.25 x 400^0.88 = -438.5; D = -w(2/3) x 2.25 x 600^0.88 = -353.1, so D is preferred. The model reproduces the exact reversal observed in 1981. Then hedge in the author's own voice: the parameters were fitted to money, not lives; the reference point is assumed rather than measured; and the demonstration shows the model is capable of the pattern, not that it caused it.  *(effort: medium)*

### [HIGH · structure] lines 16-30, "## Opening puzzle: 200 saved or 400 lost?"

> Imagine an outbreak expected to kill 600 people. Choose between:

**Problem.** The Asian disease problem is presented twice at full length in two chapters that never cross-reference each other. Chapter 12 line 61 gives it complete with all four programs and the Tversky & Kahneman (1981) citation; Chapter 17 lines 16-30 rebuilds the identical problem as its opening scenario without naming it as the Asian disease problem or citing the source at that point (the name only appears later, at line 150). Neither chapter has a single markdown link to the other — ch12 has exactly one outbound link (to ch40) and ch17 has one (to ch20). Worse, the replication evidence lives only in ch17 line 162 (Ruggeri et al. 2020, preregistered, 4,098 participants, 19 countries, 94% of items replicated with attenuation), so a reader studying framing in the chapter actually titled *Framing* never sees it and is never pointed to it.

**Edit.** Let ch17 keep the full presentation — it is the opening scenario and it drives the value function. Cut ch12 line 61 from six sentences to two that state the result and hand off: "...preferences reversed (Tversky & Kahneman, 1981). [*Prospect Theory*](17-prospect-theory-gains-and-losses-begin-at-a-reference-point.qmd#opening-puzzle-200-saved-or-400-lost) works the problem through the value function and reports the 19-country replication." Add the reciprocal link in ch17 line 150 back to ch12 #equivalent-facts-different-meanings. This also lets ch12 recover space for the concreteness the manuscript needs elsewhere.  *(effort: medium)*

### [MEDIUM · accuracy] ### Reference dependence: the zero is psychologically constructed

> found facial and interview evidence consistent with bronze medalists

**Problem.** The hedging here is correct, but the description is so compressed that the reader cannot judge the evidence: no sport, no Games, no year, no measure, no sample. The Olympic-medalist finding is also one that readers may have heard challenged, and the chapter neither reports the study's design nor mentions the subsequent conceptual replication.

**Edit.** Add the design in one clause — coders rated medalists' facial expressions from the 1992 Barcelona Games on an agony-to-ecstasy scale immediately after competition and at the medal ceremony — and add a sentence noting that a later conceptual replication using automated facial-expression analysis revisited the effect (Hedgcock, Luangrath, & Webster, 2021, *JEP: General*; verify volume, pages, and the direction of their conclusion before citing). Reporting the replication is exactly the move this book makes elsewhere and its absence here is conspicuous.  *(effort: small)*

### [MEDIUM · clarity] ### Probability weighting: decision weight is not belief

> very low positive values can make it nonmonotonic

**Problem.** The Ingersoll caveat is stated without the threshold, so it reads as a vague warning rather than a usable constraint. A reader fitting or reading fitted weighting functions cannot act on 'very low positive values'.

**Edit.** Give the bound: the Tversky-Kahneman form is increasing only for gamma above roughly 0.28, below which it becomes non-monotonic and can imply negative cumulative decision weights (verify Ingersoll's exact stated value before printing it). Note that the fitted 0.61 and 0.69 sit comfortably above it, which is reassuring and worth saying — it tells the reader the caveat is about the functional form's range of validity, not about these estimates.  *(effort: small)*

### [MEDIUM · consistency] ## Opening puzzle: 200 saved or 400 lost?

> Imagine an outbreak expected to kill 600 people.

**Problem.** Ch12 already presents the Asian-disease problem in full, including both frames and both programs. Ch17 re-presents it from scratch as if new. The reader who has read ch12 experiences the opening as repetition rather than escalation — even though ch17 does add something real (the 72/22/78 percentages, which ch12 omits).

**Edit.** Open by acknowledging the earlier encounter and going immediately to what is new: 'You met these programs in [Chapter 12] as an example of risky-choice framing. Here are the numbers that chapter left out.' Then give the percentages with their samples (72% chose A among 152 respondents; 22% chose C and 78% chose D among 155). The chapter then starts from a sharper question than ch12 could ask, and the duplication becomes a deliberate callback.  *(effort: small)*

### [MEDIUM · insight] ## Measuring loss aversion

> Estimated $\lambda$ depends on the assumed reference point, outcome range

**Problem.** The dependence on outcome range is listed as one abstract item in a list of six, when there is a clean experiment that demonstrates it directly. Walasek and Stewart (2015, *JEP: General*, 144(1), 7-11) manipulated the distribution of gains and losses in the choice set and produced loss aversion, loss neutrality, and gain-seeking in comparable participants. That result converts a hedge into a mechanism.

**Edit.** Replace the list item with the demonstration in one or two sentences: by changing only the range of gains and losses that participants sampled across trials, Walasek and Stewart made estimated loss aversion appear, vanish, and reverse. Then draw the conclusion the chapter is already reaching for: lambda may partly describe the choice set the analyst constructed rather than a property of the chooser. Add the reference.  *(effort: small)*

### [MEDIUM · insight] ## Measuring loss aversion / ### Investment: look beyond the purchase price

> An investor bought a share at €100. It now trades at €70.

**Problem.** Every study cited in this chapter is a laboratory or survey study except List (2003). Against Gal and Rucker's challenge, that is a weak evidential position, and the chapter has an obvious remedy it does not use: field evidence for reference dependence. The investor vignette is a hypothetical retelling of the disposition effect, which ch20 documents with Odean's (1998) brokerage data and a 3.41-percentage-point figure — but ch17 neither cites field evidence nor links to that treatment.

**Edit.** Two moves. In the investor vignette, add a cross-reference to the disposition-effect section of ch20 so the hypothetical is visibly backed by field data elsewhere in the book. In 'Measuring loss aversion', add one field result the book does not yet use: Genesove and Mayer (2001, *QJE*) found that house sellers facing nominal losses set asking prices well above otherwise comparable sellers and sold more slowly — reference dependence in a market with high stakes, real money, and experienced participants. Verify the reported magnitude before quoting it.  *(effort: medium)*

### [MEDIUM · structure] ## Framing changes the comparison; check equivalence

> **attribute framing:** “90% survival” versus “10% mortality”

**Problem.** This bulleted taxonomy of attribute, goal, and risky-choice framing, together with the 'verify equivalence' warning and the 90%-survival/10%-mortality example, duplicates ch12 ('Equivalent facts, different meanings'), which already develops all three categories at greater length with Levin and Gaeth (1988) and Rothman and Salovey (1997) and already makes the equivalence-checking argument with the '70% employed / 30% not employed' case. Neither chapter links to the other. The reader meets the same taxonomy twice without being told it is the same taxonomy.

**Edit.** Compress the four bullets to one sentence plus a cross-reference to ch12's taxonomy, keeping only the two categories ch17 genuinely needs (risky-choice and reference-point framing, since those are the ones the value function explains). Reinvest the reclaimed space in the Asian-disease model computation recommended above. Also add a return link from ch12's dangling sentence 'The risky-choice chapter examines how probabilities, amounts, and reference points affect that comparison.'  *(effort: medium)*

### [MEDIUM · structure] ## Learning goals

> Test whether a gain–loss effect reflects prospect theory or a competing mechanism

**Problem.** This learning goal is delivered almost entirely inside the collapse=true Research Lens at the end of the chapter (endowment effects, the five-question ownership test, status quo bias). A reader who never expands that block gets no competing-mechanism training at all. The goal also names 'attention' as a competing mechanism, and attention is never discussed anywhere in the chapter.

**Edit.** Either move the five-question ownership test and the status-quo diagnostic paragraph ('vary one mechanism at a time: make switching costs explicit, provide a neutral recommendation...') into the main body — they are the operational core of the goal and belong beside the Defaults subsection — or drop 'attention' from the goal and rewrite it to promise only what the visible body delivers. The first option is better: the Defaults section already raises inertia and switching cost and would be strengthened by the diagnostic immediately.  *(effort: medium)*

### [MEDIUM · structure] lines 153-158, bulleted framing taxonomy

> **attribute framing:** "90% survival" versus "10% mortality" changes which attribute is salient

**Problem.** Second, separable duplication between the same two chapters: both build a framing taxonomy from scratch, with different and partly incompatible schemes. Chapter 12 organizes framing into attribute framing (Levin & Gaeth's 75% lean / 25% fat, line 54), goal framing (line 57, with Rothman & Salovey and two meta-analyses), and risky-choice framing (line 61). Chapter 17 lines 153-158 re-lists risky-choice, attribute, goal, reference-point, and substantive framing as bullets. The reader meets two competing category systems five chapters apart with no acknowledgement that the second revises the first. The quoted 90%/10% survival example is itself the third appearance of that same illustration (ch01 line 109 as McNeil et al. 1982, ch12 line 17 as the opening hook, ch17 lines 155 and 160).

**Edit.** Give the taxonomy to ch12, which is the chapter named for it, and have ch17 defer. Add ch12's two missing categories (reference-point framing, substantive reframing) to its existing sequence at lines 54-61 so the taxonomy is complete in one place, then replace ch17's five bullets with one sentence: "[*Framing*](12-framing-when-the-same-facts-become-different-decisions.qmd#equivalent-facts-different-meanings) separates attribute, goal, reference-point, and substantive framing; only risky-choice framing is explained by the value function." Keep ch17 lines 160-162 (the equivalence check and the Ruggeri replication) where they are — that material is genuinely prospect-theory-specific.  *(effort: medium)*

### [MEDIUM · visual] ## Measuring loss aversion

> Gal and Rucker (2018) argue that evidence does not justify loss aversion as a context-free general principle.

**Problem.** This is the most contested empirical claim in the chapter and it is delivered in plain running prose, while the book reserves a styled `.evidence-and-boundary-conditions` callout for exactly this purpose and uses it in ten other chapters (including ch16). The stretch from the fourfold table to the Practice Lab — roughly 1,100 words — also contains no figure, table, or callout of any kind.

**Edit.** Convert 'Measuring loss aversion' into an `.evidence-and-boundary-conditions` callout titled something like 'Evidence Boundary: lambda is an estimate, not a constant'. Keep the existing content and add the provenance from the finding above plus one sentence on what would settle it (a preregistered estimate of lambda for the same people across three elicitation methods and two outcome ranges). This simultaneously fixes the visual gap and puts the chapter's most important caution in the format the book has trained readers to notice.  *(effort: small)*

### [LOW · consistency] ## References cited in this chapter

> Ingersoll, J. (2008). Non-monotonicity of the Tversky–Kahneman probability-weighting function

**Problem.** Ingersoll is listed before Gal, breaking alphabetical order in an otherwise correctly ordered list (Gal, Kahneman, Kahneman & Tversky, Kőszegi, List, Medvec...). Ch16 and ch18 reference lists are correctly alphabetized throughout, so this is a one-file slip.

**Edit.** Move the Ingersoll entry to sit between Gal & Rucker and Kahneman, Knetsch, & Thaler.  *(effort: small)*

---

## `chapters/18-decisions-from-experience-when-rare-events-are-not-encountered.qmd`  (14 findings)

### [HIGH · accuracy] ### Small samples can erase rare events

> medians around 11–19 observations per problem have appeared in this literature

**Problem.** This is the chapter's load-bearing quantitative claim — the figure, the 86% and 46% numbers, and the whole sampling argument rest on it — and 'per problem' is ambiguous between draws per option and total draws across both options. The distinction matters enormously: in the sampling paradigm participants split their draws between two decks, so a total of 15 draws means roughly 7 or 8 per option, and (1-p)^n must be evaluated at the per-option n. As written, a careful reader cannot tell whether the figure's n = 15 is the right number to use.

**Edit.** State the unit explicitly and give the primary study's figure: Hertwig et al. (2004) reported a median of about 15 draws per problem in total, split across the two options — roughly 7 or 8 observations of each. Then note that the figure's horizontal axis is observations of a single option, which makes the sampling problem worse than the 11-19 band suggests: at 7 draws, a 10% event is missed 48% of the time and a 5% event 70% of the time. Verify the exact medians against Hertwig et al. (2004) and Hau et al. (2008) before printing.  *(effort: small)*

### [HIGH · engagement] ## Research Lens: transporting the sampling diagnosis

> Mount Vesuvius, the 2021 eruption on La Palma, and floods in Passau provide vivid teaching cases.

**Problem.** Three of the most vivid concrete cases available to this chapter are reduced to a list of place names inside a collapse=true block placed after 'Take it forward'. The sentence promises vividness and then supplies none: no population, no interval since the last event, no human detail. Meanwhile the main body runs roughly 1,400 words (from the sampling figure to the process-outcome table) without a single named real-world instance.

**Edit.** Promote one case into the main body, in '### Personal history becomes a reference class' or immediately after the hot-stove section, and actually narrate it: roughly 700,000 people live in the Vesuvius red zone; the last eruption was in 1944; a resident born in 1950 has accumulated 75 years of confirming evidence that the mountain is scenery. That is the chapter's thesis in one sentence with a human being in it. Keep the remaining cases in the collapsed lens, and give each of them one number rather than a name.  *(effort: medium)*

### [HIGH · structure] ## References cited in this chapter

> Hertwig, R., & Erev, I. (2009). The description–experience gap in risky choice.

**Problem.** Hertwig and Erev (2009) appears in the reference list but is cited nowhere in the chapter body. I checked every in-text citation in the file: the other seventeen references are all cited; this one is an orphan. It is also the single most natural citation for the chapter's central section, 'The description-experience gap', which currently cites only the primary experiments and the later meta-analysis.

**Edit.** Cite it where it belongs — as the review that named and consolidated the phenomenon — in the opening sentence of '## The description–experience gap', alongside Barron & Erev (2003) and Hertwig et al. (2004). One inline citation resolves the orphan and strengthens the section.  *(effort: small)*

### [MEDIUM · consistency] ### Four sources-of-information situations

> ### Four sources-of-information situations

**Problem.** Four different names for one construct appear within twelve lines: the heading says 'sources-of-information situations', the anchor says 'four-epistemic-states', the table column says 'Information state', the figure caption says 'Four information states', and the surrounding prose says 'risk situations'. The heading itself is also the clumsiest phrase in the chapter. Readers navigating back to this framework later will not know what to search for.

**Edit.** Standardize on 'information states' everywhere: rename the heading to '### Four information states', keep the existing anchor id for link stability (it is already a stable-anchor pattern used elsewhere in the book), and make the prose at line 51 read 'The resulting four information states prevent a false choice between numbers and intuition.' Then use the same phrase when the framework is invoked later in the Worked application.  *(effort: small)*

### [MEDIUM · engagement] ## Opening puzzle: the rare outcome that did not happen

> We will return to that decision after examining what experience reveals and conceals.

**Problem.** The chapter signposts its own structure three times rather than simply proceeding: this sentence, then 'The following sections examine how selective exposure, stopping, and memory shape the experienced record' after the sampling figure, then 'The studies below examine what each presentation contributes' in the risk-communication section. Each announces work instead of doing it, and each arrives at a moment where momentum has just been built.

**Edit.** Delete all three. The supplier question is memorable enough to survive until the Worked application without a promise to return to it; the sampling figure sentence should end on the mechanism ('@fig-experience-rare-event-sampling isolates the sampling mechanism — before any psychology has been invoked'); and the risk-communication paragraph should go straight into Kaufmann et al. The chapter loses nothing and reads faster.  *(effort: small)*

### [MEDIUM · engagement] ## Exploration, exploitation, and feedback design

> A trading app can make each gain vivid while keeping portfolio risk and forgone alternatives obscure.

**Problem.** The two most ethically pointed examples in the chapter — the trading app and the workplace dashboard — are unnamed and undated, which makes them read as hypotheticals when they are documented practices. This is a section about how platforms engineer what users can learn, and it declines to name a single one.

**Edit.** Name one, with a date and a source the reader can check: a major retail brokerage removed its celebratory confetti animation in early 2021 after state regulators alleged the interface gamified trading. Describe what the design did in learning terms — it made every completed trade feel like an outcome while portfolio-level variance and forgone alternatives were never displayed, which is partial feedback optimized for engagement. The abstract taxonomy of feedback types becomes immediately usable once the reader has one real interface in mind.  *(effort: medium)*

### [MEDIUM · insight] ### Four sources-of-information situations

> This becomes **deep uncertainty** when no credible model can yet specify

**Problem.** 'Deep uncertainty' is introduced as a bolded technical term with no connection to the taxonomy the reader was given two chapters earlier. Ch16 supplies a four-layer decomposition — variability given a model, parameter uncertainty, model uncertainty and missing outcomes, and trust in the source — that deep uncertainty maps onto precisely (it is layer three exhausting the model). The chapter also lists 'Ambiguity' in its closing lens without linking to ch16's Ellsberg treatment. Two free connections are left unmade.

**Edit.** Add a cross-reference: deep uncertainty is the state in which the third layer of the ch16 decomposition — uncertainty about the model and about which outcomes belong in the list — dominates the first two, so no amount of additional sampling within the current model will help. Link to the ambiguity section of ch16. This also sharpens the chapter's own distinction between a sample that is too small and a model that is missing.  *(effort: small)*

### [MEDIUM · insight] ## Opening puzzle: the rare outcome that did not happen

> The description gives everything required to calculate expected value: A is worth €3; B is worth €3.20.

**Problem.** The opening sets up the €3 versus €3.20 problem beautifully and then never tells the reader what actually happened when it was run. The chapter states the gap as a direction ('rare events often receive relatively low decision weight') but never gives a single choice proportion from any experiment. The most persuasive fact available — that the same problem produces opposite majority choices depending only on how the information arrived — is available in the source and unused.

**Edit.** Report the observed choice proportions for this exact problem from Hertwig et al. (2004) — the description group and the experience group split in opposite directions — and place them either in the opening puzzle or at the head of '## The description–experience gap'. Take the numbers from the paper's own table rather than from memory. Two numbers turn the chapter's central claim from a stated tendency into a demonstrated reversal.  *(effort: small)*

### [MEDIUM · insight] ### The hot-stove effect

> the learner may never encounter the evidence that would correct the initial impression

**Problem.** The hot-stove section stops at the individual learner when its organizational implication is both sharper and directly relevant to the chapter's own case. The Denrell-March mechanism means that an organization's track record is systematically biased toward options that survived early luck, which is exactly the censoring the supplier Worked application later describes — but the chapter never says the two are the same mechanism.

**Edit.** Add a closing sentence that generalizes: because bad early outcomes remove options from the sample, any accumulated organizational record — of suppliers, hires, strategies, or markets — is a record of survivors, and the options that would have done well after a bad start are permanently missing from it. Then forward-link to the supplier case. This turns a laboratory effect into the chapter's organizing insight and links the hot-stove section, the stopping section, and the application into one argument.  *(effort: small)*

### [MEDIUM · structure] ## Learning goals / ## Worked application: a supplier has never failed us

> Diagnose sampling, stopping, recency, avoidance, and feedback mechanisms in one supplier-risk case.

**Problem.** The learning goal names five specific mechanisms that the chapter develops in five separate sections. The Worked application then organizes itself around four different headings (Experience audit, Description audit, Choice audit, Learning design) that do not map onto them. The reader who learned the five mechanisms is not shown them being used, and the chapter's payoff section quietly loses its connection to its teaching sections.

**Edit.** Relabel the audit items so each names the mechanism it tests: Sampling (how many independent exposures, and to which conditions?); Stopping and selection (did earlier screening remove fragile suppliers, so the record is conditional on the policy?); Recency (is the calm recent run evidence of a changed environment or of a lucky one?); Avoidance (which suppliers did we drop before they could reveal their distribution — the hot-stove question); Feedback (would we even learn about a near miss?). The existing content mostly fits; it just needs the labels, and the chapter closes its own loop.  *(effort: medium)*

### [MEDIUM · visual] ## Description and experience are different information conditions

> Four information states created by the presence or absence of statistical description

**Problem.** Two problems in twelve lines. The caption is a label, not a claim — it names what the figure contains instead of telling the reader what to conclude — and it sits directly above tbl-experience-states, which presents the same four cells with more information. The figure and the table are redundant, and the figure loses the comparison. Its fig-alt also carries interpretive content ('Neither is labeled information-poor') that the caption itself does not state.

**Edit.** Rewrite the caption as the claim: 'Neither source is automatically superior: a description without experience can leave a rare risk abstract, while experience without a description can make an unsampled hazard look like zero risk.' Then differentiate the figure from the table by having it do what a table cannot — place two or three concrete decisions from this chapter into the cells (the eight-year supplier record in Experience only; a medicine fact box in Description only; the opioid trial in Both) so the figure becomes a worked classification rather than a restatement. Also add width=100% for consistency with the other two figures in these chapters.  *(effort: medium)*

### [MEDIUM · visual] ### Small samples can erase rare events

> Larger forced samples reduce this source of the gap, but do not always eliminate the gap

**Problem.** This chapter is the longest of the three (about 4,350 words) and contains no styled callout anywhere in its body — no `.research-lens`, no `.evidence-and-boundary-conditions`, no `.activity` — with the only collapsed lens placed after 'Take it forward'. Ch16 uses two body callouts. The consequence is a long unbroken analytic run from the sampling figure to the process-outcome table. The residual-gap passage quoted here is precisely the kind of 'what is and is not settled' content the book gives callout treatment elsewhere.

**Edit.** Convert this paragraph plus the Wulff et al. (2018) summary into an `.evidence-and-boundary-conditions` callout titled roughly 'Evidence Boundary: what survives when sampling error is controlled'. Content: the aggregate gap is robust in meta-analysis; part of it is sampling error and disappears under forced large samples; a residual remains, and the candidate explanations (recency, memory, choice rule) are not yet separated. That is an honest statement of an open question and it gives the chapter's densest stretch visual relief.  *(effort: small)*

### [LOW · clarity] ### Personal history becomes a reference class

> The teaching point is broader than one graph

**Problem.** There is no graph anywhere near this sentence, and none is referenced. The phrase appears to be a leftover from a removed figure, and a reader will stop to look for the graph that is being relativized.

**Edit.** Replace with something that refers to what is actually on the page: 'The teaching point is broader than any single market history.' While editing this paragraph, also consider whether the Lejarraga et al. boom-and-bust environments deserve the figure the sentence seems to remember — a two-panel plot of the same underlying return distribution presented as a description versus as an experienced path, with the resulting allocation difference, would carry real explanatory load here.  *(effort: small)*

### [LOW · structure] ## Take it forward

> The supplier team’s task is to find out what those years cover

**Problem.** 'Take it forward' describes what the fictional team should do rather than committing the reader to an action. The same weakness appears in ch16. Ch17's version, by contrast, gives the reader a direct instruction ('Translate each into the final number of survivors and deaths before choosing').

**Edit.** Address the reader: 'Pick one thing you trust because it has never failed you — a supplier, a backup routine, a commute, a piece of code. Write down how many genuinely independent exposures you have observed, and which conditions were never in the sample. If the answer is fewer than ten exposures, none of them under stress, your confidence is resting on a record too short to have shown you the failure.'  *(effort: small)*

---

## `chapters/19-intertemporal-decision-making-why-later-loses-to-now.qmd`  (16 findings)

### [HIGH · accuracy] ## Why delay changes more than mathematical value → ### Present bias and preference reversal

> Hyperbolic models capture this pattern by making the implied discount rate fall with delay

**Problem.** The chapter presents hyperbolic/quasi-hyperbolic discounting as the description of human choice without the single most important modern boundary condition: when arbitrage and transaction costs are controlled, present bias over MONETARY rewards is weak or absent, while present bias over effort and consumption is robust. This is the brief's 'hyperbolic-discounting universality' trap, and the chapter's own later section on task identification sets it up perfectly but never delivers the punchline.

**Edit.** After the Laibson sentence, add roughly: 'The pattern is not uniform across what is being delayed. Using convex time budgets that let participants split money across two dates, Andreoni and Sprenger (2012) found little present bias for money; Augenblick, Niederle, and Sprenger (2015) gave the same people money choices and real-effort choices and found substantial present bias for effort but not for money. Money is storable and borrowable, so a monetary delay can be undone outside the experiment; a delayed hour of tedious work cannot. Present bias is best read as a claim about delayed consumption and effort, not about every delayed euro.' Add both to the reference list. This also strengthens, rather than weakens, the manager example — the postponed conversation is an effort cost, exactly where present bias is well supported.  *(effort: medium)*

### [HIGH · accuracy] ## Scarcity and trust: when now is rational

> The classic marshmallow task is therefore not a pure assay of willpower.

**Problem.** The chapter corrects the marshmallow test using only Kidd et al. (2013), but never states what the original predictive claim was (Mischel's reported links between seconds of waiting and later SAT scores and life outcomes) and never cites the large preregistered reanalysis that shrank it. A reader who does not already know the folklore cannot tell what is being corrected, and the chapter's correction is weaker than the current evidence warrants.

**Edit.** Name the original claim in one clause, then add the replication: 'Watts, Duncan, and Quan (2018) revisited the prediction in a sample of roughly 900 children drawn to be more representative than the original preschool sample. The bivariate association with age-15 achievement was about half the size reported in the early follow-ups, and it shrank to roughly a third and lost statistical significance once family background and early cognitive ability were controlled. Delay of gratification still correlates with later outcomes; it is largely a marker of the environment a child is in rather than an independent engine of it.' Add Watts, D. W., Duncan, G. J., & Quan, H. (2018), Psychological Science, 29(7), 1159–1177.  *(effort: medium)*

### [HIGH · accuracy] ### Worked application: saving from the next pay increase

> One possible design starts a contribution with the next pay increase

**Problem.** This worked application is the Save More Tomorrow (SMarT) programme described anonymously: no name, no citation, no numbers. The chapter's most quotable real-world result is withheld, and a reader cannot trace the design to its evidence. It also leaves a citation gap in a chapter that is otherwise meticulous about sourcing.

**Edit.** Name and cite it: 'This design has a name and a record. In the Save More Tomorrow programme, employees committed in advance to raise their contribution rate at each future pay increase, so the increment never arrived as a cut in take-home pay. Of those offered the plan, 78% joined, and average saving rates among participants rose from 3.5% to 13.6% over about 40 months (Thaler & Benartzi, 2004).' Then keep the chapter's discipline by adding the boundary condition in the next sentence: the original implementation was a single non-randomised consulting engagement at one mid-sized firm with no randomised control, and later automatic-escalation evaluations report smaller and more variable gains. Add Thaler, R. H., & Benartzi, S. (2004), Journal of Political Economy, 112(S1), S164–S187.  *(effort: medium)*

### [HIGH · engagement] ### Present bias and preference reversal (figure fig-discount-model-crossover)

> the quasi-hyperbolic example prefers €120 in thirteen months when viewed today

**Problem.** The chapter's central mechanism — the crossover — is demonstrated only inside a figure caption. The body prose asserts that reversal happens but never shows the reader a single number doing it. The parameters 0.70 and 0.95 appear in the caption with no names, so a reader who has not met the beta-delta notation cannot connect them to the text. I checked the arithmetic and it is correct, which makes it a waste to hide.

**Edit.** Name the parameters in the body ('a present-bias weight β applied to anything not immediate, and an ordinary period weight δ') and put the four numbers in the prose: 'With β = 0.70 and δ = 0.95, €120 in thirteen months is worth 43.1 today and €100 in twelve months is worth 37.8, so the patient plan wins. Wait eleven months and nothing has changed except the calendar: €100 is now worth 100 and €120 next month is worth 79.8. The same preferences, applied at a different moment, produce the opposite choice.' Then keep the caption but shorten it to the takeaway.  *(effort: small)*

### [HIGH · engagement] ## Opening puzzle: patient tomorrow, impatient today

> Choose between €100 today and €120 in one month.

**Problem.** The opening states the choice pair but never tells the reader how extreme the implied impatience is, so the puzzle reads as a logic exercise rather than something startling. The chapter later builds an entire apparatus on implied discount rates without ever showing one.

**Edit.** Add one sentence after the two choices: 'Turning down €120 in a month for €100 today implies a discount rate above 20% per month — a rate no one would accept if the same decision were labelled an investment. Yet the second pair, which asks for exactly the same month of patience, often gets a different answer.' This makes the stakes numeric in the first fifty words and seeds the implied-rate idea that the identification table later unpacks.  *(effort: small)*

### [HIGH · visual] ## The future must become believable and self-relevant / ## Scarcity and trust / ## Design the bridge

> Delayed outcomes often lose because they are represented poorly.

**Problem.** Lines 154–204 run roughly 1,150 words of continuous prose with no figure, table, or callout — and this is the chapter's practical payoff (future-self work, scarcity, bridge design, the retraction, both worked applications). Every visual in the chapter sits in the first half, so the half that tells the reader what to do has no visual relief at all.

**Edit.** Add one new diagram in 'Design the bridge, not only the destination'. Specify it as: a horizontal timeline from TODAY to the delayed benefit, with the delayed benefit drawn small and faint on the right; four labelled interventions plotted as vertical interventions on the timeline, each annotated with the bottleneck it repairs — first feasible step (repairs ability/friction), date-and-time appointment (repairs renegotiation), commitment device with an escape clause (repairs anticipated reversal), and progress marker or temptation bundle (repairs missing immediate reward). A fifth element at the far right shows the benefit redrawn large and sharp, labelled 'made concrete: episodic future thinking'. Caption it as a claim, e.g. 'Four different bottlenecks on the path to a delayed benefit call for four different repairs; a reminder only fixes the first one.' A reader could then map their own case onto it in the Practice Lab.  *(effort: large)*

### [MEDIUM · accuracy] line 175, marshmallow paragraph

> The classic marshmallow task is therefore not a pure assay of willpower.

**Problem.** The chapter qualifies the marshmallow task using Kidd et al. (2013) on environmental reliability, but omits the replication result and does not point to it. Appendix F line 253 documents that Watts, Duncan & Quan (2018), using a larger and more diverse sample, found the association substantially attenuated — a stronger and more directly relevant caveat than the one given here. Chapter 19 does link to Appendix F, but at line 191, for the Ariely & Wertenbroch retraction, sixteen lines later and about a different study. A reader could finish the marshmallow discussion believing the predictive claim survives intact.

**Edit.** Add one sentence and a link at the end of line 175: "A larger conceptual replication also found the association with later outcomes substantially attenuated once background factors were included ([Appendix F](../appendices/appendix-f-when-evidence-breaks.qmd#when-evidence-breaks-the-replication-crisis-and-research-integrity))." This costs one sentence and closes the book's most visible integrity loop — Appendix F already has the material and the chapter already has the link pattern.  *(effort: small)*

### [MEDIUM · clarity] ### What did the patience task identify?

> A multiple price list seems to turn patience into a number

**Problem.** Two pieces of methodological jargon arrive undefined in a section aimed at non-specialists: 'multiple price list' and, twelve lines later, 'Incentive-compatible payment'. The first is explained only obliquely by the rhetorical question that follows; the second is never explained at all, yet it is the pivot of the paragraph's argument.

**Edit.** Define the first in the same sentence: 'A multiple price list — a table of rows, each offering €100 today against a slightly larger amount in a month, with the row where the person switches taken as their discount rate — seems to turn patience into a number.' For the second, add a clause: 'Paying a randomly selected choice for real, so that answering honestly is in the participant's interest (incentive-compatible payment), can improve a task, but it does not solve every identification problem.'  *(effort: small)*

### [MEDIUM · engagement] ## Scarcity and trust: when now is rational

> If income is unstable, a promised future reward may be risky.

**Problem.** Five consecutive agentless conditional sentences ('If income is unstable... If institutions... If a person faces... If inflation... If a medical condition...'), each hedged with 'may', with no person, place, or number in any of them. This is the flattest paragraph in the chapter, and it sits in the section carrying the chapter's most important ethical argument — that impatience is often correctly diagnosed as constraint.

**Edit.** Keep the list but anchor it with one concrete case before it: 'A borrower rolling over a payday loan at an annual rate in the hundreds of percent is not being offered 20% a month by the world; they are being charged it. For that borrower, €100 today genuinely does dominate €120 next month, and advice about patience is a bill they cannot pay.' Then either compress the five conditionals to three sentences or turn them into a small table with columns 'Constraint | Why waiting costs more | What to check first', which also breaks up the visual-free stretch.  *(effort: medium)*

### [MEDIUM · insight] ### Evidence update: commitment devices require current evidence

> A voluntary deposit contract is one example; its benefits and limits are examined below.

**Problem.** Two related problems. First, the earlier passage signposts ('examined below') instead of doing. Second, and more importantly, the retraction section tells the reader what to stop believing but never says what to believe instead: a reader who currently uses self-imposed deadlines closes the section with a demolished study, one smoking-cessation contract, and no guidance. The most interesting question the retraction raises — whether the mechanism (commitment) survives the loss of its most famous demonstration — is stated as a pointer to Appendix F rather than answered here.

**Edit.** Delete 'its benefits and limits are examined below' (the reader will get there). Then close the retraction subsection with a verdict paragraph: name what survives (the theoretical case from O'Donoghue and Rabin, plus field evidence on binding savings and smoking contracts with their own take-up and harm data), what does not (the specific claim that evenly spaced externally imposed deadlines improve performance), and what a reader should do differently on Monday (keep the deadline, but choose stakes proportionate to a lapse and build in an escape clause for illness). One paragraph converts a negative result into usable advice.  *(effort: medium)*

### [MEDIUM · structure] ### Amount, sign, wording, search, and domain

> ### Amount, sign, wording, search, and domain

**Problem.** The MOST mnemonic is introduced as Magnitude, Opportunity cost, Sign, Time frame, but the body then delivers the bolded lead-ins in the order Magnitude, Sign, Time frame, Opportunity cost (the hidden zero), plus two items outside the mnemonic (search and domain). A reader trying to learn a four-letter mnemonic is walked through it in the order M-S-T-O. The section heading also names five unrelated nouns and does not announce the section's job.

**Edit.** Move the hidden-zero block (and its figure) up so the bolded lead-ins run M, O, S, T in order, then present search and domain under a clearly marked heading such as 'Two further constructors: search order and domain', so the reader knows they have left the mnemonic. Retitle the section 'What makes a discount rate move' or similar. The Practice Lab already asks readers to 'Apply MOST' in order, so the body should model that order.  *(effort: medium)*

### [MEDIUM · structure] ## Learning goals

> Build a credible bridge from a present action to a delayed benefit using the MOST audit.

**Problem.** MOST is defined in the chapter as a diagnostic for four option attributes that shift apparent discounting — not as a bridge-building tool. Bridge design is a separate apparatus in 'Design the bridge, not only the destination'. The learning goal conflates them, and the Practice Lab correctly treats them as two distinct steps, so the goal does not match what the chapter delivers.

**Edit.** Split it into what the chapter actually teaches: 'Use MOST — Magnitude, Opportunity cost, Sign, Time frame — to diagnose why a particular delayed option is losing' and 'Design a bridge from a present action to a delayed benefit: a first feasible step, a date, a commitment matched to the bottleneck, and a recovery path.' Three bullets becomes four, or fold the first two existing goals.  *(effort: small)*

### [MEDIUM · structure] ::: research-lens after Take it forward

> Interest compounds; discounting runs the calculation backward

**Problem.** A collapsed research-lens box on compounding and present value sits AFTER 'Take it forward', between the chapter's closing beat and the references. It breaks the template's closing rhythm, and its content is needed 200 lines earlier: the benchmark section introduces δ and discounting without ever connecting it to the interest rate every reader already understands.

**Edit.** Move the box to immediately after 'The benchmark: value across time', where it earns its place by grounding δ in something familiar before the psychology arrives, and where its final point — that a market rate contains inflation, default risk, and liquidity and so cannot be read as one person's impatience — directly sets up the identification table later. Keep it collapsed. End the chapter on 'survive its encounter with Monday.'  *(effort: small)*

### [MEDIUM · structure] ## Take it forward

> The aim is to help the considered plan survive its encounter with Monday.

**Problem.** 'Take it forward' restates the manager example rather than committing the reader to an action, and — unlike Chapter 20, which closes with an explicit bridge to Chapter 21 — it makes no forward link. The chapter is adjacent to mental accounting (Ch 20) and self-control (Ch 21), both of which it depends on, and links only to Ch 22 and Appendix F.

**Edit.** Replace the second half with a reader commitment plus a bridge: 'Pick the one plan you have renegotiated with yourself more than twice. Give it a date, an opening sentence, and a named first step before you finish this chapter, and write down what you will do if you miss it. Delay is only half the story: the same €100 also behaves differently depending on what it is called and which account it sits in — [Mental Accounting](20-mental-accounting-money-is-fungible-minds-label-it.qmd) takes up the labels, and [Habits, Wanting, and Self-Control](21-habits-wanting-and-self-control.qmd) asks what happens when the reversal stops being a choice at all.'  *(effort: small)*

### [MEDIUM · visual] ### Credibility, attention, and imagination (fig-intertemporal-choice)

> Intertemporal choice can be shaped by immediate salience, uncertainty, weak future imagery

**Problem.** The figure and the six-row table immediately beneath it carry nearly the same content (salience, uncertainty, imagery, friction, states), so the reader processes the same list twice in twenty lines. The figure's caption is a list of nouns rather than a sentence-length claim, and no body sentence discusses the figure, so it reads as decoration ahead of the table that does the work.

**Edit.** Either cut the figure and keep the table, or make the figure do something the table cannot: redraw it as a decision-path diagram where a single choice splits into 'take now' and 'wait', with five labelled leak points on the wait branch, each leak annotated with the design lever that plugs it — so the figure carries the diagnosis→intervention mapping and the table carries the examples. Rewrite the caption as a claim: 'A delayed option can fail at five different points; naming which one is leaking determines which lever will work.' Add one body sentence pointing at it.  *(effort: medium)*

### [LOW · consistency] ### Credibility, attention, and imagination (table caption) and ## References cited in this chapter

> {#tbl-22-delay-mechanisms}

**Problem.** Two small housekeeping defects. The table label carries a stale chapter number (tbl-22- in Chapter 19) — a book-wide legacy pattern, but this file is one instance. Separately, the reference list breaks alphabetical order twice: the Ariely and Wertenbroch entry plus the retraction notice sit ahead of Ainslie, and Giné (2010) appears before Frederick (2002).

**Edit.** Rename to #tbl-19-delay-mechanisms (and sweep the rest of the book for the same pattern in a separate pass — files 03, 05, 06, 08–13, 21, 26, 30–41 all have it). Move Giné after Frederick. For the retracted study, if leading with it is deliberate, keep it but add an inline note such as 'Listed first because it is retracted' so it does not read as an alphabetisation slip; otherwise file both Ariely and the retraction notice in normal order.  *(effort: small)*

---

## `chapters/20-mental-accounting-money-is-fungible-minds-label-it.qmd`  (16 findings)

### [HIGH · accuracy] ## Opening puzzle: is saving €6 worth the trip?

> Yet many people are more willing to travel when the €6 is one third of the price

**Problem.** 'Many people' hides one of the sharpest numbers in behavioural economics, and the canonical source of this exact problem — Tversky and Kahneman's (1981) calculator-and-jacket item — is not cited; only Thaler (1985) appears, and for a different point (the implicit value of time). The chapter's hook therefore has neither a number nor its primary citation.

**Edit.** Put the split in the sentence and add the citation: 'In the original version, 68% of respondents said they would make the trip to save $5 on a $15 calculator; only 29% would make the same trip to save the same $5 on a $125 calculator (Tversky & Kahneman, 1981). The trip is identical. The saving is identical. The answer more than doubles.' Add Tversky, A., & Kahneman, D. (1981), The framing of decisions and the psychology of choice, Science, 211(4481), 453–458 — and note that Li and Feldman (2025), already in the reference list, retested this paradigm, so the chapter can say whether it held.  *(effort: small)*

### [HIGH · accuracy] ### Lost ticket, lost cash

> Yet replacing the lost ticket often feels like spending €40 on theatre

**Problem.** The most famous demonstration of account posting in the literature is presented with no numbers and no citation to its source. Kahneman and Tversky (1984) is not in the reference list at all, and 'often feels like' asks the reader to take on trust a result that has a clean, memorable, and replicated split.

**Edit.** Give the numbers and cite the source: 'Asked directly, 88% said they would buy the ticket after losing a $10 bill, but only 46% said they would buy a replacement after losing the $10 ticket (Kahneman & Tversky, 1984). The wealth position is identical in both versions; only the account the loss was posted to differs.' Add Kahneman, D., & Tversky, A. (1984), Choices, values, and frames, American Psychologist, 39(4), 341–350. Since Li and Feldman (2025) is already cited in this chapter, state in a clause whether this paradigm survived their Registered Report — the chapter has the source in hand and the reader will want to know.  *(effort: small)*

### [HIGH · accuracy] ### Bracket for experience: hedonic editing

> Integrate losses. Combining two losses can hurt less than experiencing each

**Problem.** The four hedonic-editing rules are presented as derivations from the value function's shape, hedged only as 'hypotheses about how separate outcomes will feel'. Missing is the empirical result: when Thaler and Johnson (1990) actually tested the hedonic editing hypothesis, support was mixed, and the 'integrate losses' prediction in particular failed — participants frequently preferred to segregate losses rather than combine them. Thaler (1999), the source cited here, says as much. Presenting all four rules as equally standing understates what is known and is out of step with the chapter's otherwise careful handling of contested results.

**Edit.** Add a short paragraph after the four bullets: 'These are predictions from the shape of the value function, not established regularities. When Thaler and Johnson (1990) tested them directly, support was uneven — the prediction that people prefer losses combined was not reliably borne out, and many participants chose to keep losses separate. Treat the four rules as hypotheses about presentation worth testing in a specific context, not as design rules that will work by default.' This also makes the ethical paragraph that follows sharper: a designer bundling bad news may not even be delivering the hedonic benefit they think they are.  *(effort: small)*

### [HIGH · insight] ### Close and reopen: house money, break-even, and realization

> investors displayed a stronger propensity to realize gains than losses

**Problem.** The disposition-effect section stops one step short of its strongest evidence. Odean (1998) found the preference for realising gains over losses reverses in December, when tax motives are salient — the same investors, the same portfolios, different month. That reversal is close to decisive against an information-based explanation and is exactly the kind of counterintuitive detail the chapter's 'taxes, rebalancing, information, liquidity' paragraph is trying to argue against, yet it is left out.

**Edit.** Add: 'The most telling detail in Odean's data is seasonal. The reluctance to realise losses reverses in December, when the tax benefit of harvesting a loss is most salient. The same investors, holding the same positions, sell losers when the calendar makes the loss worth something — which is difficult to reconcile with the idea that they were holding losers because they expected them to recover.' Then the forward-looking diagnostic question that follows arrives with a demonstration behind it rather than an assertion.  *(effort: small)*

### [HIGH · structure] ## Four operations: label, bracket, couple, and close

> ## Four operations: label, bracket, couple, and close

**Problem.** The heading promises four operations in a stated order, then delivers ten subsections in a different order: Label, Close, Couple, Label-and-bracket, Lost ticket, Close-and-reopen, Bracket, Bracket-for-experience, Menu-as-portfolio, Daily income targets. Two of those (lost ticket; daily income targets) are not operations at all. A reader trying to hold a four-item scheme in mind loses it by the fourth subsection, and the section runs to more than half the chapter without a resurfacing moment.

**Edit.** Keep the four-operation frame but make the delivery match it. Order the subsections Label → Bracket → Couple → Close, folding 'Lost ticket, lost cash' into Label (it is a posting decision), 'Bracket for experience' and 'When the menu becomes the portfolio' under Bracket, and 'Close and reopen' under Close. Move 'Daily income targets' out to its own ## section after the four operations, since it is a boundary case about reference dependence rather than an operation. Add a one-sentence recap at the end of the section naming the four operations again before the audit table, so the audit's rows visibly map back onto them.  *(effort: large)*

### [HIGH · visual] ### Label and bracket: useful budgets that can become walls (tbl-mental-budgets)

> Each entry is the percentage showing the predicted

**Problem.** The Heath and Soll table is 27 cells of a triple-conjunction measure ('no after a prior purchase, yes after receiving that item as a gift, yes after an unrelated expense'), averaged across four unmentioned controls, with six cells bolded and no statement anywhere of what bold means. The contrast that is the entire point — same-category prior expense suppresses the purchase, unrelated expense does not — has been averaged into the measure and is therefore invisible in the display. A careful reader will stall here; a normal reader will skip the table.

**Edit.** Two changes. (1) Say what bold marks in the caption ('Bold marks cells where the prior purchase and the new purchase fall in the same budget category'). (2) Replace or precede the 27-cell grid with a three- or four-row contrast that shows the mechanism directly — rows 'Prior expense: sports ticket / party snacks / unrelated $50 medical expense', a single column 'Share declining a new theatre ticket', so the reader sees the same-category drop against the unrelated-category baseline in one glance. Keep the full grid as a secondary table or move it to an appendix. If the source permits it, a small diverging bar figure (same-category bars right, unrelated-category bars left of a zero line) would carry this better than either table.  *(effort: large)*

### [MEDIUM · accuracy] ### When the menu becomes the portfolio

> Adding a second stock fund can shift the same rule to two-thirds stocks

**Problem.** The 1/n claim is stated as a general consequence of menu composition on the strength of Benartzi and Thaler (2001), which used experimental allocations and cross-plan comparisons. Later work with plan-level administrative data found the relationship is much weaker in practice: participants typically spread contributions across only three or four funds regardless of how many are offered, and equity exposure is not strongly driven by the equity share of the menu. Presented as written, this is a single study carrying a general claim about real retirement portfolios.

**Edit.** Add a qualifying sentence: 'Administrative data temper the claim. Huberman and Jiang (2006) found that participants typically allocate across only three or four funds whatever the menu size, and that the proportion of equity funds offered had little systematic effect on the equity share actually chosen. Naive diversification is real, but menu composition is a weaker lever on the finished portfolio than the experimental version implies.' Add Huberman, G., & Jiang, W. (2006), Offering versus choice in 401(k) plans, Journal of Finance, 61(2), 763–801. The section's closing line — 'Ask about underlying risks, not the number of labels' — survives intact and is strengthened.  *(effort: small)*

### [MEDIUM · accuracy] ### Label and bracket: useful budgets that can become walls

> marginal utility responded about fifteen times as strongly to a gasoline-price increase

**Problem.** Citation check rather than a claim I can refute: the figure most commonly quoted from Hastings and Shapiro (2013) is around twenty, not fifteen, and 'the paper's baseline model' does not tell a reader or a fact-checker which specification produced the number. Given how load-bearing this sentence is for the fungibility argument, the provenance should be exact. Separately, the sentence gives up an easy concrete detail: the 2008 price collapse is described only as 'fell sharply'.

**Edit.** Verify the multiple against the specification you intend and name it in the sentence or footnote ('in their baseline specification, Table N'), or quote the abstract's figure directly. Add the magnitude of the shock, which costs six words and makes the case vivid: 'When US gasoline prices fell from roughly $4 to under $2 a gallon in the second half of 2008, consumers did not bank the saving — they bought better petrol.' Then the milk-and-orange-juice placebo lands as the punchline it is.  *(effort: small)*

### [MEDIUM · accuracy] line 33, Core idea heading

> ## Core idea

**Problem.** Chapters 20, 22 and 27 do NOT lack a Core Idea — all 42 chapters contain exactly one .core-idea callout. These three write the heading as '## Core idea' with a lowercase i while the other 39 write '## Core Idea', so a case-sensitive grep reports them as missing. The existing text in all three is in voice and does not need replacing.

**Edit.** Three one-character edits: ch20:33, ch22:34, ch27:26, '## Core idea' to '## Core Idea'. Do not draft replacement content. If a lint is wanted, add a build check that every chapter contains exactly one `.core-idea` block whose title matches `^## Core Idea$`.  *(effort: small)*

### [MEDIUM · engagement] ### Label: acquisition utility and transaction utility

> Thaler's (1985) hypothetical demonstration found a higher median stated willingness to pay

**Problem.** The beer-on-the-beach study is the chapter's illustration of transaction utility, and its result is given as 'a higher median stated willingness to pay' — a vague comparative where the actual gap is nearly two-to-one. The reader gets the concept without the jolt that makes it stick.

**Edit.** State the medians: 'Median stated willingness to pay was $2.65 when the beer came from a fancy resort hotel and $1.50 when it came from a small run-down grocery store — for the same beer, drunk on the same beach, with no chance of enjoying the hotel.' Then the following paragraph's point about transaction utility silently replacing acquisition utility lands on a number rather than an assertion. (Worth flagging the 1985 dollar figures as such.)  *(effort: small)*

### [MEDIUM · engagement] ### Close: sunk costs and the pain of closing an account

> Vince prepays for a tennis season and later develops a painful elbow.

**Problem.** The chapter has no human spine. Vince appears for two sentences with no amount, no season length, and no sense of what he is losing, then vanishes; the household with €30,000 in savings and €20,000 on a credit card arrives only at line 198 and is the most gripping case in the chapter. Between them are roughly 2,000 words in which the named actors are 'people', 'consumers', 'investors', and 'a project team'.

**Edit.** Give Vince the original's specifics ('a €300 season membership, six weeks in, elbow flaring on every backhand — he plays on, in pain, three times a week') and, more importantly, promote the indebted household to the opening. Open the chapter with them choosing whether to drive twenty minutes to save €6 while €20,000 revolves at high interest on a card, and return to them at Couple, at Close, and in the audit. The chapter's argument — that boundaries can serve you or govern you — is much stronger when one household carries it from first page to last.  *(effort: medium)*

### [MEDIUM · insight] ### Daily income targets

> This debate makes daily income targets a useful test case

**Problem.** The section presents a famous claim, lists three papers that complicate it, and then ends by declaring the unresolved debate 'a useful test case' — a signpost in place of a verdict. The reader is told a controversy exists but is given nothing to believe or do. The chapter is willing to reach verdicts elsewhere (Carvalho on scarcity in Ch 19, Li and Feldman here), so this reads as an abandonment rather than as calibrated hedging.

**Edit.** State where the evidence has landed and why it matters here. Farber's (2015) analysis of GPS trip records for thousands of New York drivers over several years found little support for daily income targeting once driver heterogeneity and the endogeneity of hours are handled; the strongest surviving claim is that some inexperienced drivers behave as if targeting and largely stop doing so with experience. Then say what that implies for this chapter: a mental account that costs money tends to get corrected when feedback is fast, repeated, and financially sharp — which is precisely why the household and portfolio accounts earlier in the chapter, where feedback is slow and blurry, persist. That comparison is the chapter-level insight currently left on the table.  *(effort: medium)*

### [MEDIUM · insight] ### Label and bracket: useful budgets that can become walls

> A later Registered Report found mixed results.

**Problem.** The reader is handed a 27-cell table, then told in one flat sentence that the finding partly failed to replicate, then moved on to gasoline. No verdict is offered, and the most interesting implication of the Li and Feldman result — that the boundary between 'related' and 'unrelated' categories is not stable across people — is left implicit even though it directly changes what the chapter's own audit should ask.

**Edit.** Close the paragraph with the consequence: 'The instructive part of the failure is where it failed. If a flu vaccination can sit in the same mental budget as a sports ticket for some respondents, then category membership is not a property of the expense — it is a property of the person doing the budgeting. That shifts the practical question. Rather than asking which category a cost belongs to, ask what you are actually giving up to pay it.' This also hands the audit table its motivation two sections before it appears.  *(effort: small)*

### [MEDIUM · visual] ### Close: sunk costs and the pain of closing an account

> quitting closes the account with an explicit loss

**Problem.** Two visual gaps overlap here. The sunk-cost and escalation material is the most practically used content in the chapter and has no figure, table, or callout at all — it sits inside a stretch of roughly 370 words of unbroken prose. And the chapter contains no styled callout of any kind apart from Core Idea, whereas Chapter 19 carries two research-lens boxes; the visual texture of the two adjacent chapters is noticeably different.

**Edit.** Add one small diagram at the account-closing mechanism: two side-by-side ledgers for the same decision at the same moment. Left ledger, 'The account the mind is keeping', opens with the €300 already paid as a debit and shows each painful session posted as a credit toward repaying it, closing balance negative if he stops. Right ledger, 'The account that exists', starts at zero today and lists only future items — enjoyment, exercise, time, risk of aggravating the injury. Label the gap between them 'the only amount that changes with the decision: zero'. Caption it as a claim, not a label. Separately, consider promoting the two-representation audit or the 'would I buy this today' diagnostic into a .research-lens or .activity callout so the chapter has one styled box.  *(effort: medium)*

### [LOW · clarity] ## The benchmark: fungibility and total wealth

> one unrestricted unit can substitute for another otherwise-equivalent unit of equal value

**Problem.** The chapter's key definitional sentence is close to circular — 'equivalent unit of equal value' defines fungibility in terms of equivalence — and it arrives before the vivid example that would do the work. Readers meeting the term for the first time get the abstraction first and the salary-versus-raffle illustration second.

**Edit.** Invert and decircularise: 'Money is fungible: a euro buys the same things regardless of where it came from. The €20 note handed over as salary and the €20 won in a raffle buy identical groceries. Taxes, withdrawal penalties, and timing can make nominally equal amounts genuinely different; the label on the source cannot.' Same length, no circularity, example first.  *(effort: small)*

### [LOW · consistency] ## Core idea / ### Couple / ## References cited in this chapter

> ## Core idea

**Problem.** Three small deviations. The Core Idea heading is lowercase here ('## Core idea') where 36 of the book's 42 chapters use '## Core Idea' — only this file, Ch 22, and Ch 27 differ. The Couple subsection contains a bare signpost, 'The studies below examine this link.' And the reference list breaks alphabetical order twice: Li and Feldman (2025) precedes Leclerc (1995), and both Thaler entries precede Staw.

**Edit.** Capitalise to '## Core Idea' (and sweep Ch 22 and Ch 27 in the same pass). Delete 'The studies below examine this link.' — the Gourville sentence that follows already does the work. Move Leclerc above Li, and move both Staw entries above the Thaler entries.  *(effort: small)*

---

## `chapters/21-habits-wanting-and-self-control.qmd`  (16 findings)

### [HIGH · accuracy] ## Changing the routine before the next difficult sentence

> People reporting higher self-control also reported stronger beneficial routines

**Problem.** A chapter titled '...and Self-Control' never mentions that the resource/depletion account of self-control — the reason 'resist harder' was standard advice for two decades — was estimated near zero in coordinated replications. The chapter's whole argument (look past acts of resistance to situations) is motivated by that collapse, but the motivation is invisible, so the pivot to situational strategies reads as a preference rather than a correction. Separately, the Galla & Duckworth sentence is correctly hedged as an association but does not note that both variables are self-reported in the same instrument, which is the main alternative reading.

**Edit.** Add two sentences before the Galla & Duckworth paragraph: name Baumeister et al. (1998), then the 23-lab preregistered replication estimating a near-zero effect (Hagger et al., 2016) and the 36-site paradigmatic test (Vohs et al., 2021), and cross-reference Appendix F (#famous-findings-after-replication) and Ch. 39's 'Willpower is not one depletable fuel.' Then add one clause to the Galla & Duckworth sentence: both self-control and habit strength were self-reported, so shared method and self-perception are live alternatives. The book already carries all this material — this chapter is the one place a reader most needs the pointer and does not get it.  *(effort: medium)*

### [HIGH · accuracy] ### Give the pause a different response

> An if–then plan might be

**Problem.** If–then plans are introduced, recommended, and used as the chapter's central replacement technique with no citation and no effect estimate — in a chapter that otherwise cites scrupulously. These are Gollwitzer's implementation intentions, cited properly in Ch. 39 (Gollwitzer, 1999; Gollwitzer & Sheeran, 2006) but not here, so the chapter's most prescriptive move rests on an unsourced assertion.

**Edit.** Cite Gollwitzer & Sheeran (2006) with its meta-analytic estimate, and add the honest boundary the chapter's own logic demands: that estimate comes from a pre-registration-era literature vulnerable to small-sample and publication bias, and implementation intentions generally do less for well-practised habitual responses than for new goal-directed ones — which is exactly why the chapter's next sentence ('repeated performance in context is still needed') is correct. Cross-reference Ch. 39 so the two treatments cite the same source.  *(effort: small)*

### [HIGH · engagement] Opening scenario (before Core Idea)

> Imagine a student sitting down to write a term paper.

**Problem.** The chapter's only running case opens with zero specificity: no name, no topic, no deadline, no count of checks, no clock. Three paragraphs pass before the first concrete noun that isn't 'phone' or 'sentence.' Because this student carries the entire chapter (he returns at least eight times), every later return inherits the vagueness of the first appearance.

**Edit.** Give the case one paragraph of hard detail and one number the chapter can reuse. E.g. 'Mikkel has 1,400 words due Friday on Danish wind-power subsidies. Between 9:15 and 10:00 he unlocks his phone eleven times. He writes 90 words.' The eleven checks then become the thing the cue analysis explains, the thing the log in the Practice Lab counts, and the thing the Take it forward scene compares against. One number, reused, does more than three paragraphs of 'may' and 'could.'  *(effort: small)*

### [HIGH · engagement] ### The popcorn people kept eating

> Cinema visitors received fresh popcorn or popcorn that was a week old.

**Problem.** This is the most genuinely surprising result in the chapter — people ate week-old popcorn at nearly the rate of fresh popcorn while reporting they disliked it — and it is reported without a single number, without a sensory detail, and in a sentence rhythm identical to every other sentence around it. The surprise is fully dissolved into summary. A reader can pass over the paragraph without registering that anything strange happened.

**Edit.** Restore the surprise-then-resolution shape. First the strange fact with its numbers: report the consumption percentages for strong- vs weak-habit moviegoers under fresh vs stale from Neal et al. (2011, Exp. 1), plus the taste ratings showing strong-habit eaters knew the stale popcorn was worse. Add one line of scene ('the popcorn had been popped seven days earlier and kept in sealed bags; tasters called it stale and chewy'). Then resolve it with the existing explanation. Numbers in the sentence, not in a summary clause.  *(effort: small)*

### [HIGH · insight] ### A learning curve, not a deadline

> The median modeled time to reach 95% of the plateau was 66 days

**Problem.** The chapter reports Lally et al. (2010) correctly and hedges well, but never names the myth it is correcting. '66 days to form a habit' is one of the most repeated factoids in popular behavioral science. A reader who arrives believing it reads this passage as confirmation and leaves with the belief intact — the section heading ('A learning curve, not a deadline') states the correction but the prose never cashes it.

**Edit.** Add two sentences that name and dismantle the factoid: the 66 days is a median of modeled asymptotes among the minority of participants whose curves fitted well (state the n out of the n who supplied usable data), the behaviours were self-chosen and simple (a piece of fruit with lunch, a short walk), some fitted estimates ran past the 12-week observation window, and the spread from 18 to 254 days is the finding — not the median. Close with the line the chapter already believes: the study gives a shape, not a schedule, and certainly not a schedule for a behaviour unlike the ones studied.  *(effort: small)*

### [HIGH · visual] ### What checking accomplishes / ### Wanting can outlast liking

> Observation provides information for redesign.

**Problem.** The chapter tells the reader to record, log, observe, or track on at least six separate occasions (what checking seemed to offer, what happened immediately, where the phone sits, what preceded the lapse, opportunities vs successes, the Practice Lab's week of records) and never once shows a filled-in record. The reader is asked repeatedly to do a thing they have never seen done. This also coincides with the chapter's visual desert: after @fig-wanting-liking at line 100, roughly 1,300 words run to the end of Take it forward with no figure, no table, and only one callout.

**Edit.** Add one small filled-in log table around 'Observation provides information for redesign' — four real-looking rows from the student's afternoon with columns: Time | What preceded | What I did | What changed immediately | Work after. Make the rows show the pattern rather than assert it (two rows preceded by a hard sentence, one by fatigue, one by an actual notification), so the reader sees that 'notifications' explains only one of four checks — the chapter's own claim at line 116. Caption it as a claim: 'Four checks, three different triggers: the log separates the cue the student assumed from the cues that actually preceded the action.' This fills the visual gap and converts the chapter's most-repeated instruction into a demonstration.  *(effort: medium)*

### [MEDIUM · accuracy] ### Wanting can outlast liking

> Research distinguishes these components of reward even though they often occur together

**Problem.** The wanting/liking dissociation is imported without scoping its evidence base. The core dissociation evidence in Berridge & Robinson (1998) comes from rodent work (dopamine manipulations that leave hedonic orofacial reactions intact) and from drug addiction, not from everyday behaviours like phone checking. The chapter carefully guards the addiction inference three paragraphs later but never guards the transfer of the construct itself, so a reader reasonably concludes that 'wanting without liking' is an established finding about social media.

**Edit.** Add one clause at the point of introduction: the separation was established mainly through animal studies manipulating dopamine while measuring hedonic reactions, and through work on drug reward; applying it to phone checking is an interpretive extension, useful for generating an observation, not a demonstrated mechanism in this case. This costs one sentence and makes the later addiction caveat land as part of a consistent stance rather than a disclaimer.  *(effort: small)*

### [MEDIUM · accuracy] ### What checking accomplishes

> rewards that arrive only sometimes can help sustain responding

**Problem.** This is the partial reinforcement extinction effect stated with no citation, in a chapter where every other empirical claim carries one. It is also the chapter's implicit explanation for why feeds are hard to put down, which makes the missing source conspicuous.

**Edit.** Cite it (a reinforcement-schedule source, or Wood & Rünger, 2016, for the habit-relevant framing) and mark the extension explicitly: intermittent-schedule findings come from controlled reinforcement procedures, and describing a social feed as an intermittent schedule is an analogy the reader can test on their own log, not a measured property of the app.  *(effort: small)*

### [MEDIUM · clarity] ### Find the cues that arrive together

> A **cue ecology** is a practical label for inspecting how several cues

**Problem.** 'Cue ecology' is bolded in exactly the same way as habit, automaticity, goal-directed control, wanting, and liking — all of which are established terms of art with citations. A reader will reasonably assume it is standard vocabulary and may go looking for it. It appears to be the author's own working label.

**Edit.** Say so in the sentence: 'I use *cue ecology* as a working label rather than a term from the literature; it is a reminder to inspect the several cues and enabling conditions that converge, instead of assuming one trigger to remove.' The book's voice elsewhere is careful about exactly this distinction, so the fix is a consistency repair, not a concession.  *(effort: small)*

### [MEDIUM · consistency] ::: {.callout-note .loop-location} / ## Take it forward

> ## Where this chapter enters the loop

**Problem.** Two structural devices appear in this chapter and in no other chapter of the book: the 'Where this chapter enters the loop' callout (unique to Ch. 21 across all 42 chapters) and the three-bullet 'Use this when / Do not infer / Try this next' closing (also unique to Ch. 21). A reader meets both once and never again, which reads as an editing leftover rather than a designed feature. Given the recent 'revising the master loop' work, this may be a partial rollout.

**Edit.** Decide and apply book-wide. If the loop callout is the intended new standard, roll it out to all chapters with a consistent class and heading; if not, fold its content into this chapter's prose (it is a good paragraph). Same for the three bullets: they are a genuinely useful closing pattern — either adopt them as the standard 'Take it forward' tail across chapters or remove them here so Ch. 21 matches the one-or-two-paragraph plus bridge form used by Ch. 19, 20, 23, and 24.  *(effort: medium)*

### [MEDIUM · insight] ### Give the pause a different response

> Imagine a manager whose defensive replies have become reliably cued

**Problem.** This is the chapter's only non-student instance and the only one aimed at a working reader, and it gets two sentences before being dropped. A reader who is a manager rather than a student is given nothing they can hold. The chapter has built a four-element scaffold (cue, impulse, action, outcome) and never applies it a second time, so the reader never sees the tool transfer.

**Edit.** Expand to a four-line parallel run through the chapter's own scaffold: cue (the colleague's questioning tone in the Monday review), impulse (heat in the chest, the sentence already forming), action (explaining why the objection is wrong), outcome (immediate relief from feeling judged; three weeks later, a team that has stopped raising objections early). Then the replacement — ask for one concrete example before explaining — lands as a designed substitution rather than an assertion. This also earns the chapter its claim that the analysis generalizes beyond phones.  *(effort: small)*

### [MEDIUM · insight] ## Where this chapter enters the loop

> ## Where this chapter enters the loop

**Problem.** Chapter 21 is the only one of 42 that tells the reader where its mechanism sits on the book's master loop, and the class already has bespoke CSS. The master loop is the book's spine (@fig-normative-decision-loop, invoked from the preface to ch42, and recently revised per the git history), yet 41 chapters leave the reader to locate themselves on it unaided. One styled box for one chapter is the strongest signal in the manuscript that this device was invented and then abandoned.

**Edit.** Promote it to all 42 chapters as a two-sentence band directly under the Core Idea, naming the loop functions the chapter touches in bold — e.g. ch03: 'Attention operates before **Predict**: it decides which signals reach the loop at all.' ch11: 'Context acts on **Value**: the same option is scored against a comparison set the loop did not choose.' ch26: 'Other people enter at **Interpret** as evidence and at **Value** as pressure; the chapter separates the two.' This is the single cheapest fix for 'easy to follow' in the whole book.  *(effort: large)*

### [MEDIUM · insight] ## Take it forward, closing bullets

> - **Use this when** an ordinary repeated action starts with little deliberation

**Problem.** Chapter 21 closes with a three-bullet block — 'Use this when' / 'Do not infer' / 'Try this next' — that is the single most useful closing format in the manuscript: it states the chapter's scope, its over-reach boundary, and one action. It appears exactly once in 42 chapters. Nothing else in the book gives the reader a portable statement of what a mechanism does NOT license.

**Edit.** Generalise it. Append the same three bullets to every 'Take it forward', after the existing callback paragraph. The 'Do not infer' line is the highest-value half and is already implicit in most chapters' hedging — ch09 'Do not infer frequency from how easily a case comes to mind'; ch15 'Do not infer a causal effect from a return toward the average'; ch17 'Do not infer loss aversion from a gain-loss gap without ruling out ownership, attention, inertia, and switching cost'; ch26 'Do not infer private agreement from public compliance'; ch27 'Do not infer a tradable opportunity from a measured anomaly'.  *(effort: large)*

### [MEDIUM · visual] ### A learning curve, not a deadline

> A schematic of increasing automaticity with diminishing gains.

**Problem.** @fig-habit-formation-curve shows one illustrative curve and restates in its caption the numbers already given in the adjacent sentence. It therefore carries no explanatory load beyond decoration — and worse, a single smooth curve visually asserts the very uniformity the section is arguing against.

**Edit.** Redraw as a small-multiples or overlay panel that makes the spread the subject. X axis: days (0-260, log or linear). Y axis: self-reported automaticity (0 to plateau). Plot four or five contrasting individual trajectories from Lally et al.'s well-fitted cases — one reaching 95% near day 18, one near day 66, one near day 254, with the 12-week observation window marked as a vertical dashed line so the reader sees which estimates are extrapolations. Label the median curve. Caption as a claim: 'The 66-day median hides a 14-fold spread; some fitted plateaus lie beyond the period actually observed.'  *(effort: medium)*

### [MEDIUM · visual] Research note: unexpected outcomes and dopamine

> The progress-checkpoint panel extends the learning idea to task design.

**Problem.** @fig-reward-prediction-error-shift has four panels; the fourth ('progress checkpoint') exists only in the caption and alt text. Nothing in the research note, or anywhere in the chapter, explains what a progress checkpoint is or how it relates to prediction error. The reader meets a panel with no referent.

**Edit.** Either add one sentence to the research note that does the work — e.g. an unexpected mid-draft 'done' marker functions like an unpredicted reward, which is why breaking the term paper into markable checkpoints can change what the desk cues — or delete the fourth panel and trim the caption. As it stands the caption promises an idea the chapter does not deliver.  *(effort: small)*

### [LOW · consistency] Optional practice: observing an urge with BRAIN

> : Prompts for observing an urge {#tbl-20-brain}

**Problem.** The table identifier is #tbl-20-brain in chapter 21 — a leftover from the chapter's previous number (the file's alias is 19-habits-...). Every other cross-reference target in the chapter uses a descriptive or ch21 form. A stale numeric prefix in an ID invites a future mis-link.

**Edit.** Rename to #tbl-ch21-brain (or #tbl-brain-prompts) and update any cross-references. While there, check the epigraph page number: the sentence 'Habits are learned dispositions to repeat past responses.' as quoted with a full stop needs verification against Wood & Neal (2007) p. 845 — the closest wording I can place sits in the abstract on the article's first page (843).  *(effort: small)*

---

## `chapters/22-deciding-for-a-better-life-satisfaction-connection-and-meaning.qmd`  (18 findings)

### [HIGH · accuracy] ## Turn the evidence into a personal decision

> people assigned to spend money on others reported greater happiness at the end of the day

**Problem.** This is the chapter's only concrete prescriptive intervention and it is presented as a settled single experiment with no sample size and no replication status. The 2008 Science windfall field experiment was small (n = 46), and a large preregistered multi-site replication (Aknin, Dunn, Proulx, Lok, & Norton, 2020, JPSP) found a substantially smaller effect. In a book with an entire appendix on exactly this failure mode, and in a sentence that immediately follows 'More specific interventions need their own evidence,' presenting it flatly is a self-inconsistency the reader can detect.

**Edit.** Rewrite to: state the original's design and n, then 'A later preregistered multi-site replication found a smaller effect (Aknin et al., 2020),' then the chapter's own lesson — this is precisely why the next paragraph converts advice into a personal hypothesis with a stopping rule rather than a claim. Add the Aknin et al. (2020) reference and cross-reference Appendix F. This turns a liability into the strongest paragraph in the section.  *(effort: small)*

### [HIGH · consistency] ## References cited in this chapter

> Wilson, T. D., & Gilbert, D. T. (2003). Affective forecasting.

**Problem.** Wilson & Gilbert (2003) is in the reference list but is never cited anywhere in the body — I checked both directions and this is the only mismatch in the chapter. Meanwhile, two doors down, **focalism** is defined with no citation at all ('A related mechanism is **focalism**'), and impact bias itself is attributed only via a 'for example' to Gilbert et al. (1998), which is the immune-neglect paper rather than the general review.

**Edit.** Fix both problems with one edit: cite Wilson & Gilbert (2003) as the review source for impact bias and focalism in the '### Impact bias and focalism' section. If the author prefers the primary source for focalism, add Wilson et al. (2000, 'Focalism: A source of durability bias in affective forecasting') and remove Wilson & Gilbert (2003) from the list. Either way, no reference should sit uncited.  *(effort: small)*

### [HIGH · engagement] ## Opening question: which job produces the better life?

> Job A pays substantially more, carries status, and requires a long commute

**Problem.** The Job A / Job B case is the spine of the chapter — it returns six times, at lines 62, 124, 152, 172, 196, and 216 — and the reader never learns a salary, a commute length, a job title, or a number of evenings. 'Substantially more' and 'a long commute' are placeholders. Because the case is never specified, every return is as abstract as the first, and the four-field audit at the end has nothing to be filled in with.

**Edit.** Specify the case once, in the opening: €78,000, 65 minutes each way, two evenings a week, versus €61,000, 20 minutes, evenings free. Then let the later returns do arithmetic the reader can feel. The commute alone is about nine hours a week, roughly 400 hours a year, against €17,000 before tax — about €42 per hour of life sold, at a time of day when the buyer is already tired. That single calculation, built entirely from the chapter's own logic about time use and experienced affect, is the most memorable thing this chapter could contain, and it costs three sentences.  *(effort: small)*

### [HIGH · engagement] ## Income: no magic number

> An adversarial collaboration reanalyzed the apparent conflict.

**Problem.** This is a genuinely dramatic episode in the history of the field — a famous result, a public contradiction, and then the two rivals sitting down with a neutral arbiter to reanalyze the data together — and it is delivered as one agentless clause. 'Adversarial collaboration' is never defined, so a reader who does not already know the term learns nothing. The most striking human fact is omitted entirely: Kahneman co-authored the paper that overturned his own $75,000 plateau.

**Edit.** Spend three sentences here. Define adversarial collaboration in one clause (two researchers who disagree design the reanalysis jointly in advance, with a third party arbitrating, so neither can choose the specification after seeing the result). Then name what happened: Kahneman, who had published the plateau, co-authored the paper that qualified it, with Mellers as arbiter. Then the finding, which the chapter already states accurately. This is not drama for its own sake — it is the book modelling the updating it teaches, and it belongs in a chapter about not manufacturing verdicts.  *(effort: small)*

### [MEDIUM · accuracy] ## Connection is part of the outcome

> stronger social relationships were associated with lower mortality risk

**Problem.** The chapter's claim that 'Relationships belong among the central outcomes of major decisions' rests entirely on a magnitude the reader is never given. Holt-Lunstad et al. (2010) pooled 148 studies and roughly 308,000 participants and reported about a 50% greater likelihood of survival for participants with stronger social relationships (OR ≈ 1.5) — a number that makes the argument. Stating only 'associated with lower mortality risk' gives the reader no basis to weigh relationships against the salary they can see on the contract.

**Edit.** Give the numbers: 148 prospective studies, ~308,000 participants, average follow-up around 7.5 years, OR ≈ 1.5. Then keep the chapter's existing discipline by adding the boundary in the same breath: these are observational studies, health selection and reverse causation are live (ill people withdraw from social life), and the pooled estimate mixes structural and functional measures that the chapter's own tbl-relational-well-being insists on separating. That contrast — a big headline number and a real limitation stated together — is this book's voice at its best.  *(effort: small)*

### [MEDIUM · accuracy] ## Income: no magic number

> flattened around an income category centered near US$75,000 in 2008–2009 dollars

**Problem.** The hedging here is correct and should be kept, but the paragraph reports the outcome of the 2010-2021-2023 sequence without reporting the methodological reason for it, which is the transferable lesson. Kahneman & Deaton's emotional-well-being measure used dichotomous yes/no items about yesterday with a ceiling; Killingsworth used continuous momentary reports. Part of the 'plateau' was a property of the instrument, not of income. The chapter teaches measurement discipline everywhere else and skips it in the one place where a measurement artifact produced a world-famous number.

**Edit.** Add one clause naming the instrument difference (dichotomous yesterday items with a ceiling versus continuous experience-sampling reports) as part of the resolution, so the reader leaves with the method lesson and not just the score. Also anchor the figure in today's money — US$75,000 in 2008-09 is roughly US$110,000 now — because the number is quoted everywhere as if current, and that unstated inflation is itself a small focusing illusion.  *(effort: small)*

### [MEDIUM · accuracy] ## Income: no magic number

> A later reanalysis estimated where the income–well-being curve could bend

**Problem.** Two issues with the Bennedsen (2024) sentence. First, it is the only reference in the chapter I could not match against a literature I can verify, and it is doing load-bearing work as the chapter's final word on the income debate — author, journal, volume, and DOI should be checked before publication. Second, the sentence is vaguer than the reference it cites: the listed title states a plateau around $200,000 per year, while the body says only 'a different plateau pattern,' so the reader is told a number exists and denied it.

**Edit.** Verify the citation against the journal record. If it holds, put the estimate in the sentence and say what changed: allowing the bend point to be estimated rather than fixed moved the apparent plateau far above $75,000. If it does not hold, drop it — the Killingsworth et al. (2023) collaboration already supports the paragraph's conclusion.  *(effort: small)*

### [MEDIUM · clarity] ## Turn the evidence into a personal decision

> More specific interventions need their own evidence.

**Problem.** This short section changes subject twice in five sentences: it returns to the jobs, jumps to prosocial spending, then jumps again to a testable hypothesis about protecting two evenings. The prosocial-spending sentence connects backward to nothing and forward to nothing — the hypothesis that follows is about evenings and sleep, not about giving. The reader arrives at the section's payoff without knowing why the detour happened.

**Edit.** Either cut the Dunn et al. sentence (its content is not required by the section) or make it earn its place by having the personal hypothesis test it: 'If I move one of my two protected evenings to something done for someone else...' — which would let a single worked example carry the intervention evidence, the replication caveat, and the hypothesis format at once. Add one transition sentence either way so the reader knows the section is moving from 'what the evidence supports in general' to 'what I will test in my own case.'  *(effort: small)*

### [MEDIUM · clarity] ## Measuring well-being without manufacturing a verdict

> Reliability asks whether a measure is sufficiently consistent for its purpose.

**Problem.** This section defines reliability and validity abstractly, then lists five things that can change a result — 'Wording, question order, timing, survey mode, and interpretation of response scales' — with not one instance. It is the chapter's densest stretch of abstraction and it concerns the most concrete, most demonstrable phenomenon in the chapter. A reader nods and retains nothing.

**Edit.** Replace the list with one documented demonstration and keep the list as a follow-on clause. The classic item-order case works well: asking students about their dating life before the life-satisfaction question changes the correlation between the two dramatically, while the reverse order does not (Strack, Martin, & Schwarz, 1988) — flag it as a small early study and note it is the same focusing mechanism the chapter has already introduced, which ties this section to the Tuesday test rather than leaving it as a standalone methods aside. If the author prefers a more robust source, an OECD-documented survey-mode effect serves the same purpose.  *(effort: small)*

### [MEDIUM · insight] ## Social comparison and the focusing illusion

> Use a Tuesday test.

**Problem.** The Tuesday test (line 74) and the focusing illusion (line 166) are the same mechanism — attention determines the weight a feature receives in a global judgment — but the chapter introduces them ninety lines apart as if unrelated. Schkade & Kahneman's California students are doing precisely what the Tuesday test is designed to prevent, and the chapter never says so. The reader gets two tools and one unstated idea instead of one idea with a tool attached.

**Edit.** At the focusing illusion paragraph, close the loop explicitly: the students' error is the Tuesday test failing before anyone runs it — asked about California, they simulated the beach and not the commute, the rent, the work, or the same friends they would not have. Then reuse the tool by name for relocation. This gives the chapter a spine: one mechanism, one countermeasure, applied before a choice and again when comparing whole lives. It also lets you add the concrete fact currently missing — that the actual reported life-satisfaction difference between the regions was negligible.  *(effort: small)*

### [MEDIUM · insight] ## Adaptation: selective, incomplete, and morally easy to misuse

> purchases and achievements may produce smaller durable changes than forecast

**Problem.** The section establishes that adaptation is selective and then stops one step short of the decision rule that selectivity implies — which is the whole reason the section belongs in a chapter about choosing between jobs. If adaptation is strong for income, status, and possessions but weak or absent for commuting, chronic pain, insecurity, loneliness, and time pressure, the corollary is a selection rule: buy out the recurring irritants, not the one-off upgrades. That corollary is exactly the Job A / Job B case, and it is never drawn.

**Edit.** Add two sentences making the corollary the section's 'so what,' tied back to the jobs: the salary difference is the kind of change people adapt to; the 65-minute commute is the kind they adapt to poorly, because it recurs, is unpredictable, and cannot be habituated away. Then state the honest limit in the chapter's own register: the domain-by-domain adaptation comparison rests on observational panel data with heterogeneous individual trajectories, so it ranks plausibilities rather than predicting one person's course.  *(effort: small)*

### [MEDIUM · structure] ## A well-being decision audit / ## Learning goals

> names the person, measure, horizon, relationships, distribution, rights, and freedom to revise

**Problem.** Learning goal 3 promises a seven-part instrument. The chapter delivers tbl-well-being-decision-audit with four core fields; person, horizon, and decision authority are demoted to a sentence below the table, and 'measure' appears only as the optional-module paragraph. A reader checking the chapter against its own stated goals finds a shortfall, and the Practice Lab then asks them to build the four-field version.

**Edit.** Align the two. Simplest fix: rewrite the learning goal as 'Build a decision audit across four core fields — ordinary-day experience, evaluation and meaning, material conditions and agency, relationships — plus an explicit statement of who decides, over what horizon, and what must not be sacrificed.' Alternatively add a fifth row ('Authority and horizon: who decides, by when, and what triggers reconsideration') so the table is the whole instrument. Do not leave a seven-item promise answered by a four-cell grid.  *(effort: small)*

### [MEDIUM · structure] ## Opening question: which job produces the better life?

> ## Opening question: which job produces the better life?

**Problem.** The opening deviates from the template in ordering and duplicates itself. Before the Core Idea the reader meets a scenario, a cited study (Benjamin et al., 2012), a full figure showing all six well-being lenses, and a methodological directive — where the template places a 2-4 paragraph scenario. Worse, @fig-well-being-six-lenses front-loads six distinctions before the reader has any reason to want them, and the same six are then re-presented as tbl-well-being-targets twenty lines later.

**Edit.** Keep the two scenario paragraphs as the unheaded (or 'Opening puzzle'-headed) opening; move the Benjamin et al. paragraph and @fig-well-being-six-lenses down into '## One word, several targets,' where they sit beside the six-target table they belong with. The figure and table then reinforce each other in one place rather than duplicating each other across the Core Idea boundary, and the opening keeps the concrete job dilemma as its only content.  *(effort: medium)*

### [MEDIUM · structure] ## A policy dashboard, not a happiness maximum

> []{#what-this-chapter-deliberately-does-not-claim}

**Problem.** An orphan anchor sits between two sections with no heading or content behind it — a reader following an existing link to #what-this-chapter-deliberately-does-not-claim lands on nothing. The anchor name also points to something real that is missing: the chapter makes several strong epistemic commitments (there is no master measure, adaptation is not consent, a self-report correlating with physiology does not validate it) but has no place where it states plainly what it is *not* claiming.

**Edit.** Restore a short section under that anchor, four bullets, before the decision audit: this chapter does not claim that a well-being score should override the person's own judgment; that a higher mean justifies harm to a minority; that adaptation makes a condition acceptable; or that any single measure — life evaluation, affect, meaning, or income — is the master quantity. That is a genuinely distinctive closing move, it fixes the dead anchor, and it gives the audit table its warrant. Separately, note that the heading id #what-appears-to-helpand-what-the-evidence-can-support on 'Turn the evidence into a personal decision' has a mangled 'helpand' from a lost em dash; keep it as an alias but do not create new ids this way.  *(effort: medium)*

### [MEDIUM · visual] ::: {.callout-note icon=false collapse=true} Compare the six questions

> ## Compare the six questions

**Problem.** tbl-well-being-targets is the chapter's single best orientation device and the chapter's governing discipline ('do not move between measures without saying so') depends on the reader holding those six targets in mind. Yet it is hidden inside a collapsed callout, defaults to closed, and is never cross-referenced as @tbl-well-being-targets anywhere in the body — so a reader can complete the chapter without seeing it.

**Edit.** Uncollapse it and promote it to a plain table in the section. Then make the chapter's structure visible by tying the four following section headings to its rows — '## Before the outcome' covers predicted and decision utility, '## During the outcome' covers experienced affect, '## After the outcome' covers remembered utility, '## Across a life' covers life evaluation and eudaimonia. Add a half-sentence at each transition naming which row is now in play ('This is row three of @tbl-well-being-targets'). The reader then always knows which of the six lenses the chapter is currently looking through, which is the chapter's own stated requirement.  *(effort: small)*

### [MEDIUM · visual] ## Adaptation: selective, incomplete, and morally easy to misuse

> A worker's capacity to cope does not erase unsafe work.

**Problem.** Two problems converge here. First, this is the chapter's most important normative claim — adaptation is not consent — and it sits as an undistinguished paragraph in running prose, visually identical to the surrounding descriptive material. Second, the chapter has a long visual desert: after @fig-income-wellbeing-evidence-synthesis at line 148, roughly 1,100-1,200 words run through adaptation, social comparison, personal decision, measurement, and the policy dashboard with no figure, table, or callout until the audit table at line 198.

**Edit.** Put the adaptation-is-not-consent paragraph into a styled callout using the existing .evidence-and-boundary-conditions class (one of the four classes with real CSS), headed something like 'Boundary: what adaptation evidence cannot license.' That both gives the claim the weight it deserves and breaks the longest unillustrated stretch in the chapter at roughly its midpoint. Consider a second callout for the policy-dashboard paragraph, which makes an equally strong normative claim in equally flat typography.  *(effort: small)*

### [MEDIUM · visual] line 48, Compare the six questions

> ## Compare the six questions

**Problem.** Seven callouts are pure lookup grids you consult, not tasks you perform — ch22:48, ch24:48, ch25:50, ch26:46, ch27:150, ch28:93, ch38:60 — plus .negotiation-tactic-diagnostic and .mediation-arbitration in Appendix C. They currently render with the same weight as a Core Idea, so a reference table competes visually with the chapter's central claim.

**Edit.** Create .reference-table as the quietest treatment in the system: border var(--book-line) #d7e0e7, no background tint, title in var(--book-muted), collapse=true. The rule for authors: if there is nothing to fill in and nothing to produce, it is a reference table.  *(effort: small)*

### [LOW · consistency] ## Core idea / ## Bridge: a better life is not made alone

> ## Core idea

**Problem.** Three small deviations from book-wide norms in this file. 'Core idea' is lowercase here and in three other chapters, against 46 that use 'Core Idea'. The opening heading reads 'Opening question:' where chapters 18, 19, 20, 23, 24, and 25 all use 'Opening puzzle:'. And the closing bridge sits under its own '## Bridge:' heading, a pattern used only here and in Ch. 25, while Ch. 20 and Ch. 24 fold the bridge into the last paragraphs of 'Take it forward'.

**Edit.** Change to '## Core Idea' and '## Opening puzzle: which job produces the better life?'. For the bridge, either fold the paragraph into the end of 'Take it forward' to match the majority pattern, or standardize '## Bridge:' as an explicit part-transition device used only at part boundaries and apply it consistently at every part boundary (this chapter closes Part III). Pick one and note the rule so the remaining chapters can be swept in a single pass.  *(effort: small)*

---

## `chapters/23-strategic-interdependence-the-best-move-depends-on-other-minds.qmd`  (13 findings)

### [HIGH · clarity] ### Bargaining is also a coordination problem

> Suppose two players simultaneously claim shares of a total surplus of 4.

**Problem.** The Nash demand game is set up with a number (4) and then the reader is never shown a single claim pair. "Many claim pairs are feasible, and many can be sustained by expectations" is asserted where two lines of arithmetic would demonstrate it. In a chapter that insists on making payoffs inspectable, this is the one worked example that is not worked.

**Edit.** Add three lines immediately after the setup: (2, 2) — both paid, the focal split; (3, 1) — both paid, and it is equally an equilibrium, since neither can raise a claim without risking zero; (3, 2) — claims sum to 5, both receive 0. Then make the point explicit: every pair summing to exactly 4 is a Nash equilibrium, so the theory identifies the whole frontier and says nothing about which point is reached. That is precisely why the distributional question survives the equilibrium analysis — which is the paragraph's actual argument.  *(effort: small)*

### [HIGH · engagement] ## Opening puzzle: meet me in Odense

> You and another person must meet tomorrow in Odense.

**Problem.** The hook is an instruction set, not a scene, and it never delivers the payoff that makes the focal-point idea land: what people actually answer. The reader is told a focal point "might" emerge and is left with a hypothetical. Schelling's own demonstration is the missing punchline.

**Edit.** Add two sentences reporting Schelling's informal result: asked where they would meet a stranger in New York City with no communication, a large majority of his respondents named the Grand Central Station information booth, and an overwhelming majority named 12 noon — the time answer was even more concentrated than the place answer. Hedge it as he did (an informal survey of students, not a controlled experiment), which fits the book's voice and reinforces the later point that 'focal point' can rename rather than explain. Then return to Odense and ask the reader which answer an exchange student versus a lifelong resident would give.  *(effort: small)*

### [HIGH · engagement] ### Commitment changes the game

> A promise to reimburse buyers if the recommended price later fell

**Problem.** Four consecutive conditional, agentless sentences ("could reassure", "It also raised", "If rivals adopted", "could change") with no year, no country, no price, no market, and no outcome. The chapter calls this "a useful stylized case" and then supplies nothing a reader can picture. It is the flattest paragraph in a chapter about one of the most dramatic ideas in the book — deliberately destroying your own options to gain power.

**Edit.** Either give the case a body (year, market, the size of the guaranteed reimbursement, and what rivals did) or replace it with a commitment case the author can state concretely. Also flag as a citation check: verify that the Ford Price Promise is actually the example carried in Rao, Bergen, & Davis (2000) — that HBR article's worked cases are not obviously this one. If the case cannot be sourced precisely, drop to a documented commitment device (a published most-favored-customer clause, or a publicly announced launch date that made retreat visible) rather than keeping a hedged anecdote with a possibly wrong citation.  *(effort: medium)*

### [HIGH · structure] ### Worked application: two departments need one reporting standard

> Worked application: two departments need one reporting standard

**Problem.** The section is labeled 'Worked application' but nothing is worked. Step 5 of the audit the reader just followed says 'Find best responses and equilibria,' and the worked application skips straight to six design bullets without drawing the payoff table the chapter has spent 3,000 words arguing for. The reader is told the method matters and then shown the method being bypassed.

**Edit.** Draw the 2x2 with illustrative numbers before the bullets: rows Department A adopts System A / System B, columns the same for B; compatible cells share a large coordination payoff with the local-quality difference visible (e.g., 8,6 for A's system and 6,8 for B's), incompatible cells much lower for both (e.g., 2,2). Name the structure — this is Battle of the Sexes, which the Research Lens already defined — and note that both compatible cells are equilibria, so the fight is distributional, not technical. Then derive each of the six bullets from a cell or a payoff term, so the reader sees the diagnosis producing the design.  *(effort: medium)*

### [HIGH · visual] ### Strategic uncertainty: the stag hunt

> Stag is strictly better when $p>8/13\approx0.615$

**Problem.** The single most useful number in the chapter arrives as bare algebra with no visual. The insight — that you need better-than-three-in-five confidence in your partner before the jointly better outcome is worth attempting — is exactly the kind of thing a reader remembers from a picture and forgets from a fraction.

**Edit.** Add a small line chart. X-axis: p, the belief that the other player hunts Stag, 0 to 1. Two lines: EU(Stag) = 2 + 13p rising from 2 to 15, and EU(Hare) = 10 flat. Mark the crossing at p = 0.615 with a dropline and shade the region p < 0.615 as 'Hare is the best response even though both prefer Stag–Stag.' Caption should state the claim, not the contents: 'Agreeing that Stag is better is not enough — a player needs more than 62% confidence that the partner will follow through before Stag is worth choosing.' Add fig-alt describing the crossing point and the shaded region.  *(effort: medium)*

### [MEDIUM · clarity] ## First diagnose the strategic problem

> Before choosing a move, identify the structure of dependence.

**Problem.** The section's opening paragraph spends four sentences caveating labels the reader has not yet seen ("anti-coordination is a coordination family in which players benefit from taking different rather than matching roles") before the archetypes are introduced. The reader must hold an abstract disclaimer in memory and then retrofit it to a table two screens later.

**Edit.** Invert. Lead with the table (or the redesigned figure), then place the caveat after it as a one-sentence rider: 'These four overlap. Anti-coordination is a coordination family — players must still match on a rule, but the rule assigns different roles — and most real situations carry mixed-motive features. Let the payoffs, not the label, decide.' Same content, half the cognitive load.  *(effort: small)*

### [MEDIUM · consistency] ## Learning goals

> players, actions, payoffs, information, timing, repetition, and enforcement

**Problem.** Learning goal 1 and the Practice Lab both require seven elements, but the chapter's own numbered specification lists only five (players, actions, payoffs, information, timing). Repetition and enforcement are discussed in the following prose but never enter the checklist the reader will actually use. Students will produce five-element maps and the Practice Lab will grade seven.

**Edit.** Add two numbered items to the list under 'Representing the strategic situation': '6. Repetition: Is this a one-shot encounter, a fixed number of rounds, or a relationship with an uncertain end?' and '7. Enforcement: Who can observe a violation, and what response is available and credible?' The prose that currently follows (one-shot versus uncertain end; public versus private action) then reads as elaboration of items 6 and 7 rather than as loose additions.  *(effort: small)*

### [MEDIUM · engagement] ## Mixed motives, anti-coordination, and escalation

> If both reason this way, bids can exceed the prize.

**Problem.** A genuinely shocking result is stated so flatly the surprise evaporates. 'Bids can exceed the prize' is a logical possibility; what makes the dollar auction famous is how far past the prize bidding routinely goes in practice. The reader gets the mechanism without the jolt that motivates the stop rule two sentences later.

**Edit.** Add one concrete figure with the right hedge. Classroom and executive-education runs of the $20 version regularly close well above the stake, with reported winning bids in the hundreds of dollars. Say so as demonstration evidence, not as an effect estimate: 'In repeated classroom demonstrations the $20 version has sold for many times its value — these are teaching demonstrations, not controlled experiments, which is why the escalation explanation still has to be tested rather than assumed.' That hedge is also exactly the point the paragraph goes on to make about competition neglect versus escalation of commitment.  *(effort: small)*

### [MEDIUM · insight] ## Coordination: shared expectations can do the work

> David (1985) used QWERTY to motivate path dependence

**Problem.** One of the best evidence-evaluation stories in behavioral economics is compressed into a single agentless sentence. The QWERTY/Dvorak dispute is not a footnote about keyboards — it is a case where the celebrated efficiency claim traces to a study its own beneficiary conducted, and where the correction is as interesting as the original. Stating it as 'Liebowitz and Margolis (1990) challenged the familiar claim' hides what they actually found.

**Edit.** Give it three sentences. The widely repeated evidence for Dvorak's superiority traces largely to a wartime U.S. Navy study; Liebowitz and Margolis note that Dvorak himself was involved in that work and that the comparison lacked the controls needed to attribute the difference to the layout. Later controlled comparisons found gains far smaller than the folklore. Then state honestly what remains: QWERTY's persistence is well documented, but its inferiority is not established — so path dependence is the safe lesson and 'locked into a bad standard' is not. This also earns a cross-reference to the book's how-to-read-evidence front matter.  *(effort: medium)*

### [MEDIUM · structure] ## Take it forward

> In both cases, better advice begins by making the dependence visible.

**Problem.** The section restates the chapter instead of committing the reader to an action. Compare chapter 24's 'Take it forward,' which gives a specific pre-registration instruction ('write down the mean you expect and why') and a specific comparison afterward. Chapter 23's closes on a summary sentence the reader can nod at and forget.

**Edit.** Replace the closing sentence with a commitment tied to the audit the chapter just taught: 'Before your next negotiation, standards meeting, or supplier review, write down the other side's three best available actions and the payoff you believe each carries for them — including the non-monetary ones. Afterward, mark which entry you got wrong. The errors, not the map, are what improve the next diagnosis.'  *(effort: small)*

### [MEDIUM · visual] ## First diagnose the strategic problem

> The labels below are strategic archetypes, not mutually exclusive categories.

**Problem.** Two visuals present the same content back to back. @fig-strategic-situation-diagnostic enumerates coordination, conflict, mixed motives, and anti-coordination, and @tbl-strategic-structures immediately enumerates the same four with more detail. The figure adds no explanatory load the table does not carry, and the figure's caption is itself mostly the table's caveat restated.

**Edit.** Repurpose the figure so it does different work: make it a diagnostic decision flow, not a taxonomy. Entry question 'Do our interests align on the outcome?' branches to 'Must our actions match?' (coordination) or 'Must they differ?' (anti-coordination); a 'partly' branch goes to mixed motives with a split into a value-creation limb and an allocation limb; 'no' goes to conflict. Label each terminal with the first design lever (common signal; role assignment or rotation; separate the creation and allocation stages; anticipate the response). The table then stays as the reference card and the figure becomes the thing you use while diagnosing. Alternatively cut the figure.  *(effort: large)*

### [LOW · consistency] ## Mixed motives, anti-coordination, and escalation

> Research Lens: the €50 auction and competitive escalation

**Problem.** The heading names a €50 auction, the hidden anchor says 50, and the body immediately calls it 'Shubik's dollar-auction game.' A reader who searches for either term finds an inconsistent label, and the euro figure never reappears.

**Edit.** Make the heading and body agree: 'Research Lens: the euro auction and competitive escalation,' with a first sentence that names both — 'Shubik's dollar auction, run here for a €50 note, awards the prize to the highest bidder while the second-highest bidder also pays their final bid (Shubik, 1971).' Keep the existing anchor for link stability.  *(effort: small)*

### [LOW · consistency] ## References cited in this chapter

> Smith, V. L. (1962). An experimental study of competitive market behavior

**Problem.** Smith (1962) is listed before Skyrms (2004), breaking the alphabetical ordering used throughout the rest of the list and the rest of the book. Skyrms precedes Smith.

**Edit.** Swap the two reference blocks so the order runs Schelling, Shubik, Skyrms, Smith, Staw.  *(effort: small)*

---

## `chapters/24-behavioral-game-theory-equilibrium-is-a-benchmark-not-a-portrait.qmd`  (14 findings)

### [HIGH · accuracy] ### Cognitive hierarchy: best respond to a mixture

> Descriptive number-game results used to illustrate heterogeneous strategic depth

**Problem.** Eight rows of published experimental data — means, modes, sample sizes, and fitted tau values across CEOs, students, portfolio managers, and newspaper entrants — appear with no source in the caption and no citation in the surrounding sentences. A reader cannot check any of it, and the book's own standards elsewhere are stricter than this.

**Edit.** Add the source to the caption: 'Descriptive number-game results across participant groups, adapted from Camerer, Ho, & Chong (2004); German student data from Nagel (1995); newspaper data from the large-scale newspaper contests reported in Bosch-Domènech, Montalvo, Nagel, & Satorra (2002).' Add the Bosch-Domènech et al. (2002, American Economic Review 92(5), 1687–1701) reference to the list. Also relabel the 'Group size' column as 'N' or 'Participants' — in a beauty contest 'group size' reads as the strategic group, which is not what 7,884 means for the newspaper row.  *(effort: small)*

### [HIGH · engagement] ### Cognitive hierarchy: best respond to a mixture

> Large within-group dispersion remains.

**Problem.** Five words of throwaway after the chapter's richest table, and they bury the best fact in the chapter. The newspaper row reports 7,884 entrants with a mean of 23.0 and a modal choice of 1. That is the chapter's entire thesis sitting in one line: a large cluster of people reasoned all the way to the equilibrium, and they lost, because the winning number in such contests sits in the low teens. Stated as 'dispersion remains,' the surprise is gone.

**Edit.** Replace with three sentences that make it a story. The most common single answer among nearly eight thousand newspaper entrants was 1 — near the game-theoretic solution — while the mean was 23 and the winning number therefore landed far above the equilibrium. Sophistication that ignores the population is a losing strategy, and the players who best understood the theory were systematically wrong about the outcome. Then note the honest caveat the mode reveals: the distribution is not a single bounded-reasoning blob but at least bimodal, which is a constraint on any model fitted only to the mean.  *(effort: small)*

### [HIGH · insight] ### Two beauty contests

> First choose the face you personally find most attractive from a set.

**Problem.** The chapter uses 'beauty contest' in a learning goal, a section heading, and a table caption, and stages a face-choosing exercise that is a direct restaging of Keynes's metaphor — but Keynes is never named, here or anywhere in the book. The reader is handed a term of art with no origin and loses the single most quotable framing of the entire idea, along with its connection to the book's market chapters.

**Edit.** Add a short paragraph before the face exercise. Keynes (1936, General Theory, ch. 12) described newspaper competitions in which readers picked the six prettiest faces from a hundred photographs, the prize going to whoever's picks came closest to the average of all entrants — so the winning strategy is to choose not the faces one finds prettiest, but those one expects others to choose, and at the next degree, the faces others expect others to choose. Then run the face exercise as Keynes's game. Add Keynes (1936) to the reference list, and cross-reference the markets chapter, where the same recursion drives price.  *(effort: small)*

### [HIGH · structure] ## Learning goals

> Compare equilibrium, level-*k*, and cognitive-hierarchy accounts of one beauty-contest dataset.

**Problem.** This learning goal is never delivered. The chapter describes each of the three accounts in separate sections and shows a table of fitted tau values by group, but it never puts three predictions side by side against one dataset and never says which fits better or by how much. The reader finishes with three vocabularies and no comparison.

**Edit.** Add a short table immediately after the tau discussion, using one row of the existing dataset (the newspaper sample is the best choice — largest N and a well-known distribution). Columns: Account | Predicted mean | What the prediction assumes. Rows: Nash equilibrium — 0 — everyone reasons to the limit and believes everyone else does; Level-k with the commonly fitted mixture of levels 1–3 — roughly 20–25 — each player responds to exactly one level below; Cognitive hierarchy at tau = 1.5 — roughly 20 — each player responds to a Poisson mixture of lower levels; Observed — 23.0. Then one sentence stating the honest verdict: both bounded-reasoning accounts land near the data and equilibrium does not, but the two are close enough on this dataset that it cannot separate them — which is why the next section is about identification.  *(effort: medium)*

### [MEDIUM · accuracy] ### Cognitive hierarchy: best respond to a mixture

> | Caltech students | 42 | 23.0 | 35 | 3.0 |

**Problem.** This row does not hang together. A fitted tau of 3.0 puts most population mass near steps 2–3, which in this game corresponds to choices around 15–22, and the reported mean of 23.0 is consistent with that — but the reported modal choice of 35 is a level-1 answer. Either the mode is a transcription error or the row is genuinely bimodal and the anomaly needs a sentence, because as printed it silently undercuts the table's own message that tau tracks depth.

**Edit.** Verify the Caltech row (mode and N) against the source table. If the mode is correct, add one clause to the paragraph following the table explaining it: some groups are bimodal, with a level-1 cluster near 33–35 coexisting with a cluster near the equilibrium, so a single fitted tau summarizes the mean without describing any individual. If it is a transcription error, correct it.  *(effort: small)*

### [MEDIUM · accuracy] ## The action does not identify the thought

> Their results are consistent with different processing as strategic depth increases.

**Problem.** The sentence hedges so hard that no finding survives. The reader is told a study exists and that its results are 'consistent with different processing' — which is compatible with almost any result. This is over-correction rather than care: the book's voice distinguishes what a study showed from what people infer, but here nothing is shown at all.

**Edit.** State the finding, then hedge it. Coricelli and Nagel (2009) had participants play the guessing game against human and computer opponents and found that medial prefrontal activity distinguished higher- from lower-level reasoners and was greater against human opponents. Then the existing caution earns its keep: this identifies a correlate of believing one faces a mind, not a measure of reasoning depth, and reverse inference from a region to a process is not licensed — which is exactly why the design's human-versus-computer contrast, not the imaging, is what does the identifying work.  *(effort: small)*

### [MEDIUM · clarity] ### Cognitive hierarchy: best respond to a mixture

> an average of about 1.5 steps fits behavior across many games

**Problem.** The reader is given a Poisson density, a parameter, and a reported value, and is never shown what the parameter predicts. Nothing in the section converts tau = 1.5 into a number on the 0–100 scale the whole chapter is built on, so the formula stays decorative.

**Edit.** Add one worked sentence after the tau value: 'With tau = 1.5, the model implies roughly 22% of players at step 0, 33% at step 1, 25% at step 2, and the remainder higher — which in the two-thirds game produces a predicted group mean in the low twenties, close to the pooled means in the table below.' One line, and the formula starts earning its place.  *(effort: small)*

### [MEDIUM · consistency] ::: {.callout-note .core-idea icon=false}

> Equilibrium provides one benchmark; limited reasoning and learning provide alternatives.

**Problem.** Chapter 23 builds a table whose caption is literally this chapter's title — 'Equilibrium is a benchmark, not a portrait' — and hands off explicitly ('Behavioral game theory begins where the last column becomes unavoidable'). Chapter 24 never picks the handoff up. The two chapters are joined in one direction only, and the reader who noticed the echo gets no confirmation that it was deliberate.

**Edit.** Add one sentence after the Core Idea or at the head of 'Three lenses, three questions': '@tbl-equilibrium-boundary listed four things equilibrium alone cannot establish. This chapter supplies models for the last two rows — which equilibrium gets selected, and whether the specified beliefs describe the people playing.' A single cross-reference closes the loop and tells the reader the two chapters were designed as a pair.  *(effort: small)*

### [MEDIUM · engagement] ## Limited strategic depth: level-*k*

> The same person can use different depths when the game, incentives, time

**Problem.** Six abstract nouns and no instance. This is the most practically important claim in the level-k section — depth is a state, not a trait, which is what stops the model from becoming a personality label — and it is delivered as a list with nothing attached. It is also the claim the Ethics section later depends on.

**Edit.** Attach one managerial instance. A pricing team that sets price by asking 'how will our rival respond to this announcement?' is reasoning at one step; a team that asks 'what price is our rival setting in anticipation of our response?' is at two. The same team moves between the two depending on how much time it has and whether it has been burned before. Then the Ethics section's warning against labeling someone 'level 1' lands, because the reader has seen the same team occupy both levels.  *(effort: small)*

### [MEDIUM · insight] ## The action does not identify the thought

> An incentivized belief report, information-search record, or experimental change

**Problem.** Three distinct research methods are named in one clause and dropped. 'Information-search record' in particular is doing real work in this literature and is left as an opaque phrase — the reader has no idea what it means or why it is powerful. The section states an identification problem and then gestures at solutions without exercising one.

**Edit.** Spend a sentence on the strongest of the three. Costa-Gomes and Crawford recorded which payoff information participants actually looked up before choosing, and found that many players whose choices matched a given level never opened the information that level's reasoning requires — so the action matched the model while the process did not. That is the cleanest demonstration of the chapter's own thesis, and Crawford et al. (2013) is already in the reference list to support it. Add Costa-Gomes & Crawford (2006, American Economic Review 96(5), 1737–1768) if citing the study directly.  *(effort: medium)*

### [MEDIUM · structure] ## Learning goals

> Two beauty contests

**Problem.** This H3 immediately follows '## Learning goals' with no intervening H2, so in the table of contents and in any collapsed navigation it nests as a subsection of the learning goals. Chapter 25 has the identical defect at the same position. Chapter 23 does not — its parallel exercise sits correctly under an H2.

**Edit.** Promote 'Two beauty contests' to H2, or move it under a new H2 such as '## Two beauty contests' with the face exercise and the Princess Bride exercise as H3s beneath it. Whichever is chosen, apply the same fix to chapter 25's '### Is the scene really a Prisoner's Dilemma?' so the three chapters agree.  *(effort: small)*

### [MEDIUM · structure] line 127, inside the "Advanced research track" callout

> Schelling-style segregation, evolutionary prisoner's-dilemma dynamics, and ethnocentrism models

**Problem.** Chapter 24 lines 125-127 and Appendix B line 225-251 share ten distinct 8-grams and reproduce the same two closing sentences with the same six citations (Schelling 1969; Wilensky 1997, 2002, 2003; Hammond & Axelrod 2006; Axelrod 1984; Imhof et al. 2007). The oddity is that ch24 already links to Appendix B in the very same paragraph — so the chapter both points to the appendix and duplicates what the appendix says, which makes the link look redundant and doubles the citation maintenance burden.

**Edit.** Keep ch24's first two sentences (evolutionary game theory's question, and the caution that frequency change alone does not identify selection — that is the chapter's own argument) and keep the model-provenance requirement. Delete the duplicated implementations list and the tournament/equilibrium/stability sentence, letting the existing Appendix B link carry them: "...seeds and replications. [Appendix B](../appendices/appendix-b-evolutionary-explanations-of-value-choice-and-rationality.qmd#population-model-provenance) lists reproducible teaching implementations and separates tournament success, repeated-game equilibrium, and evolutionary stability as distinct criteria." Drop Wilensky, Hammond & Axelrod, and Imhof from ch24's reference list.  *(effort: small)*

### [MEDIUM · visual] ## Three lenses, three questions

> Three lenses, three questions

**Problem.** An H2 section whose entire substantive content — the three-lens comparison table — is hidden behind collapse=true, leaving one visible paragraph. It sits immediately below a figure that already shows the same three lenses. A reader scrolling past sees a heading, a folded box, and a sentence, and the section's organizing table is optional reading.

**Edit.** Uncollapse this table. It is four rows, it is the section's reason for existing, and unlike the optional research lenses elsewhere in the book it is not supplementary material. Then cut the redundancy with the figure above by having the paragraph point at what the table adds that the figure cannot: the decision rule column. Alternatively, fold the section into the figure discussion and keep only the table.  *(effort: small)*

### [LOW · clarity] ### Two beauty contests

> The scene illustrates recursive reasoning.

**Problem.** The paragraph's last sentence repeats its first sentence ('dramatizes recursive reasoning') with no added content, and it also contradicts the instruction between them, which asks the reader to identify what makes the displayed reasoning unproductive. The paragraph ends by affirming the thing it just asked the reader to doubt.

**Edit.** Cut the sentence and replace it with the actual point: Vizzini's ladder has no stopping rule, so each additional step is as arbitrary as the last — and Westley does not win by climbing one rung higher. He wins by changing the game, having built immunity so that the choice does not matter. That is a level-k failure and a commitment device in one scene, and it links directly back to the previous chapter's commitment section.  *(effort: small)*

---

## `chapters/25-cooperation-and-social-preferences-self-interest-is-not-the-only-payoff.qmd`  (16 findings)

### [HIGH · accuracy] ### Punishment can enforce cooperation—and create another dilemma

> It can also be antisocial, mistaken, retaliatory, or captured by powerful actors.

**Problem.** 'Antisocial punishment' is a technical term with a specific source and a specific, striking result, used here as a loose adjective with no citation. Herrmann, Thöni, and Gächter (2008, Science 319, 1362–1367) ran public goods with punishment in sixteen participant pools worldwide and found that in several — Athens, Muscat, Riyadh, Minsk among them — high contributors were punished so heavily that punishment failed to raise cooperation at all. That is the chapter's own 'cooperation for whom' thesis backed by data, and it is currently a passing word.

**Edit.** Add two sentences and the citation. State the finding: punishing high contributors was common in several societies and large enough to cancel punishment's cooperative benefit, and the cross-society variation tracked measures of rule of law and civic norms. Then add the boundary condition the book's voice requires: these are correlations across participant pools that differ in many ways at once, so the societal-norms interpretation is a hypothesis the design cannot isolate. This finding also belongs in the Ethics section, which currently makes the same point without evidence.  *(effort: medium)*

### [HIGH · accuracy] ### Repetition gives current behavior a future

> With $T=6$, $R=4$, and $P=2$, the threshold is $\delta\geq0.5$.

**Problem.** Two problems in one place. First, Dal Bó and Fréchette (2018) sits in the reference list and is cited nowhere in the body — a dangling reference. Second, the passage that most needs it reads more deterministic than the evidence supports: it says cooperation 'is sustainable' above the threshold and then caveats only monitoring and end dates. Their survey's central result is that a continuation probability above the threshold makes cooperation possible but does not predict it — cooperation reliably emerges only when cooperating is also risk dominant, and even then it takes experience for subjects to get there.

**Edit.** Add one sentence with the citation after the threshold is derived: 'The threshold says when cooperation can be an equilibrium, not when it will occur. Surveying the experimental record, Dal Bó and Fréchette (2018) find that subjects cooperate reliably only when cooperation is also risk dominant — clearing the sustainability threshold is necessary but far from sufficient — and that cooperation rates rise substantially with experience in the setting.' This fixes the uncited reference and supplies the boundary condition the section is missing.  *(effort: small)*

### [HIGH · accuracy] ### Applied case: large stakes do not remove context

> Cooperation persisted at these high stakes in a setting where contestants interacted

**Problem.** The section reports the stakes and three secondary findings but omits the paper's headline number — roughly half of contestants chose Split — and omits the stakes result entirely. 'Cooperation persisted at these high stakes' is the section's conclusion, but van den Assem and colleagues also report that the propensity to cooperate falls as the amount at stake rises over most of the range. A reader gets the reassuring half of the result and not the qualifying half.

**Edit.** State the cooperation rate in the sentence, not just the stakes: roughly 53% of contestants chose Split across the sample of episodes. Then add the stakes finding the section currently omits — cooperation declines as the amount at stake increases, though not linearly — and let the conclusion carry that qualification: cooperation survived large stakes, but stakes mattered. Verify the exact rate and the shape of the stakes relation against the paper before publication.  *(effort: small)*

### [HIGH · engagement] ### Tit-for-tat, forgiveness, and noise

> is a powerful historical illustration of reciprocal restraint

**Problem.** The most vivid material in the chapter — soldiers in the trenches inventing tacit non-aggression under fire — is compressed into one sentence whose only descriptive content is the phrase 'powerful historical illustration.' The chapter asserts that the illustration is powerful instead of making it so. Three paragraphs on either side are abstract, and this was the place to break the rhythm.

**Edit.** Give it three or four sentences of actual mechanics, which are what make it a reciprocity case rather than a war anecdote. Units facing each other for weeks developed routines: artillery fired at the same hours and the same coordinates so both sides could take cover; ration parties moving in the open were left alone; a violation drew a proportionate, unmistakable reply and then restraint resumed. The system broke down when commands rotated units out and ordered raids, destroying the continuation that made restraint self-enforcing. Credit the source Axelrod drew on — Ashworth (1980), Trench Warfare 1914–1918: The Live and Let Live System — alongside Axelrod, and add the reference. Then make the analytic point explicit: the mechanism was not goodwill but a high continuation probability plus observable actions plus a credible proportionate response, which is exactly the three-part condition derived two paragraphs earlier.  *(effort: medium)*

### [HIGH · insight] ### Punishment can enforce cooperation—and create another dilemma

> People sometimes pay to punish defectors or unfair partners.

**Problem.** The chapter's punishment section contains no experimental numbers, no named paradigm, and no citation to the founding work. The public goods game — the workhorse of the entire cooperation literature, and the setting in which costly punishment was demonstrated — appears nowhere in this chapter or anywhere else in the book except as a passing word in the Henrich sentence. A reader finishes the chapter without the single most replicated result in the field.

**Edit.** Add the public goods game as a row in @tbl-cooperation-mechanisms and give it a short subsection in the repeated-interaction part of the chapter. The pattern is reportable with numbers: contributions typically start near 40–60% of the endowment and decay toward the low single digits over about ten rounds, and Fehr and Gächter (2000, American Economic Review 90(4), 980–994) showed that letting players pay to reduce a defector's earnings reverses the decay and holds contributions high. This also makes the chapter's existing 'Before adding sanctions' paragraph concrete rather than advisory. Add the reference.  *(effort: large)*

### [HIGH · insight] ## The mechanism ladder: same outcome, different cause

> Institution | Rules change payoffs, information, or enforcement.

**Problem.** The chapter names institutions as one of five mechanisms, builds an Application section around designing one, and warns that 'the evolutionary label must not erase institutions' — but Ostrom appears nowhere in this chapter or in the entire book. The field's central empirical answer to how real groups sustain cooperation over generations without markets or state enforcement is simply absent, which leaves the institutional rung as the least evidenced of the five.

**Edit.** Add a Research Lens or short subsection on Ostrom (1990, Governing the Commons). The design principles are directly usable and several answer questions the chapter already raises and leaves open: graduated sanctions answer the 'Before adding sanctions' paragraph; monitoring by the appropriators themselves answers 'who judges violations'; accessible conflict-resolution and a recognized right to organize answer 'how errors can be appealed.' State the evidential status carefully — these are regularities induced from comparative case studies of long-enduring irrigation systems, fisheries, and forests, not experimentally identified causes, and Ostrom herself treated them as design hypotheses. Add the reference.  *(effort: large)*

### [MEDIUM · accuracy] ### When a fine changes the meaning of the act

> introducing a fine for late pickup increased lateness in the treated centers

**Problem.** A famous result stated with no numbers and no sample caveat. The reader learns the direction and nothing about the magnitude, the setting, or how much weight the study bears. The chapter is normally careful to distinguish a striking demonstration from a precise estimate, and this passage does not.

**Edit.** Add the specifics: ten daycare centers in Haifa over twenty weeks, with a small fine — about NIS 10 — for collecting a child more than ten minutes late; late pickups in the treated centers roughly doubled, and did not return to baseline in the weeks after the fine was withdrawn. Then add the caveat the section omits: with six treated centers this is a compelling demonstration that price and meaning can move in opposite directions, not a precise estimate of how often they do. That caveat also strengthens the section's closing advice, which currently asserts that design must test both without saying why the single study cannot settle it.  *(effort: small)*

### [MEDIUM · accuracy] ### Ultimatum game: fairness has strategic force

> Classic experiments instead commonly find modal offers around 40–50%

**Problem.** The founding ultimatum study is never cited. Güth, Schmittberger, and Schwarze (1982) introduced the game and is the reference that makes 'classic experiments' a specific claim rather than a gesture. The chapter cites a textbook summary and a meta-analysis but not the original, which is a gap a reader checking the literature will notice immediately.

**Edit.** Add Güth, W., Schmittberger, R., & Schwarze, B. (1982). An experimental analysis of ultimatum bargaining. Journal of Economic Behavior & Organization, 3(4), 367–388, and cite it at the point the game is introduced rather than only in the results sentence — 'In the ultimatum game (Güth, Schmittberger, & Schwarze, 1982), a proposer divides a sum.' Keeping Camerer (2003) and Oosterbeek et al. (2004) for the summary statistics is correct.  *(effort: small)*

### [MEDIUM · clarity] ### Repetition gives current behavior a future

> With $T=6$, $R=4$, and $P=2$, the threshold is $\delta\geq0.5$.

**Problem.** Five display equations in sequence and not one sentence translating the result into something a reader can act on. Delta is introduced as 'the continuation weight' and never given a meaning — the reader never learns that 0.5 corresponds to a coin-flip chance the relationship continues after each round, or roughly one further expected encounter. The most useful managerial number in the chapter is left as algebra.

**Edit.** Add an interpretation sentence: 'Read delta as the chance the relationship continues after each round. A threshold of 0.5 means cooperation can survive only if there is at least a coin-flip chance of meeting again — roughly one more expected encounter. Relationships nearing a known end, short project assignments, and final-quarter supplier contracts all push delta down.' Then add a three-row table showing how the threshold moves with temptation: T=5, R=4, P=2 gives 0.33; T=6 gives 0.50; T=10 gives 0.75. The reader sees that a larger temptation demands a longer shadow of the future, which no single worked number conveys.  *(effort: medium)*

### [MEDIUM · clarity] ### Punishment can enforce cooperation—and create another dilemma

> decisions to punish a defector in a trust-game setting

**Problem.** 'Trust-game' appears exactly once in the entire book — here — with no definition. The trust or investment game (Berg, Dickhaut, & McCabe, 1995) is a core social-preferences paradigm and would sit naturally alongside the ultimatum and dictator games the chapter does develop, but the reader meets the term cold, inside a neuroscience sentence, and must take it on faith.

**Edit.** Either define it in two sentences where it appears — an investor sends any part of an endowment to a trustee, the amount sent is tripled, and the trustee returns whatever they choose, so sending is costly and only pays if trust is reciprocated — or, better, add it as a short subsection between 'Ultimatum game' and 'Dictator game.' It is the one paradigm in this literature that separates trust from trustworthiness, which is a distinction the chapter's mechanism ladder needs and currently lacks. Add the Berg, Dickhaut, & McCabe (1995, Games and Economic Behavior 10(1), 122–142) reference.  *(effort: medium)*

### [MEDIUM · engagement] ## Opening puzzle: why cooperate when defection dominates?

> Two people choose simultaneously between Cooperate and Defect.

**Problem.** The chapter opens on a bare matrix with no human situation attached — no names, no stakes, no reason to care who defects. Chapters 23 and 24 at least give the reader a place (Odense) or a contest to enter. This chapter owns three genuinely gripping cases (the Golden Balls final, the trenches, the Haifa daycare) and opens with none of them.

**Edit.** Keep the 'Opening puzzle' heading and the matrix, but put two or three sentences of concrete situation in front. The Golden Balls setup is ready-made and already in the chapter: two strangers who have talked for twenty minutes, a jackpot on the table, two balls each, one marked Split and one marked Steal, and no way to coordinate at the moment of choice. Then show the matrix as the abstraction of what they face, and the arithmetic that follows acquires a body. This also sets up the applied case later in the chapter as a payoff rather than a digression.  *(effort: small)*

### [MEDIUM · insight] ## Practice Lab

> then four announced rounds with the same partner

**Problem.** The Lab specifies a known, announced four-round horizon — which is precisely the backward-induction unraveling case the chapter warned about earlier ('a known end date can unravel cooperation by backward induction under narrow assumptions') — but never tells the reader that. The Lab's most instructive feature is left invisible, and learners will be surprised by the round-four defection rather than having predicted it.

**Edit.** Make the horizon the point. Add: 'The four-round horizon is announced deliberately. Before playing, write down what backward induction predicts for round 4, then for round 3 given that, and so on back to round 1. Then play. Most pairs cooperate through round 3 and defect in round 4 — neither the equilibrium prediction nor unconditional cooperation. Explaining that specific pattern is the exercise.' This converts a procedural instruction into a surprise-then-resolution and gives the mechanism ladder something real to explain.  *(effort: small)*

### [MEDIUM · structure] ## Application: build cooperation around the diagnosed failure

> Members of a project team withhold information, and the manager proposes a penalty.

**Problem.** At roughly 110 words this is by far the thinnest Application section of the three chapters, and it is the one the reader is most likely to need. It names three explanations and three responses but supplies no diagnostic — nothing tells the reader how to determine which of the three is operating before choosing the response, which is the chapter's entire method. Compare chapter 23, which gives an eight-step audit ending in a recorded prediction.

**Edit.** Add a diagnostic column to match the chapter's own mechanism ladder. For each explanation, state what you would observe if it is the right one: if individual credit is the cause, hoarding should be concentrated among people whose evaluations depend on exclusive knowledge, and should fall when recognition is made joint; if the cause is doubt about reciprocation, people should share readily once one visible contribution is reciprocated, and a small reciprocal trial is the test; if the cause is disagreement about legitimacy, the withheld items should cluster by content rather than by person. Close with the recorded prediction the chapter 23 audit demands: state whose behavior should change, by how much, and what result would count against the diagnosis.  *(effort: medium)*

### [MEDIUM · structure] ## Learning goals

> Is the scene really a Prisoner's Dilemma?

**Problem.** This H3 immediately follows '## Learning goals' with no intervening H2, so the film exercise and the chapter's opening figure both nest under Learning goals in the table of contents. Chapter 24 has the identical defect at the same position; chapter 23 does not.

**Edit.** Promote to H2, or introduce a containing H2 (for example '## Before the mechanisms: is this really a dilemma?') with the film exercise as an H3 beneath it, and apply the same fix to chapter 24's '### Two beauty contests' so the three chapters in this part agree.  *(effort: small)*

### [MEDIUM · visual] ### Revealed preference over allocations

> A familiar summary assigns 47.2% to a selfish type

**Problem.** The section's sharpest point — that the tidy three-type percentages conceal the fact that only 43% of participants fit a pure category exactly, with 57% assigned to a nearest neighbour — is made entirely in prose, in the middle of a roughly 1,400-word stretch with no visual between @tbl-preference-norm and the fairness figure. The number that undercuts the familiar summary is easier to miss than the familiar summary itself.

**Edit.** Add a small stacked bar figure that makes the concealment visible. One bar per type (selfish 47.2%, egalitarian/maximin 30.4%, utilitarian 22.4%), each split into a solid segment for exact fits and a hatched segment for participants assigned to the nearest category, with a footer line reading 'Exact fits: 43% of 176 participants.' Caption as a claim, not a label: 'The three-type summary of Andreoni and Miller (2002) is a classification, not a discovery of three kinds of people — most participants were assigned to the category they came closest to.' This is a figure that carries real explanatory load, which is more than the current prose does.  *(effort: medium)*

### [LOW · visual] ### Dictator game: remove strategic rejection

> An original redraw compares the ultimatum, dictator, and take-or-menu-variant games.

**Problem.** The caption opens with a production note ('An original redraw') rather than a takeaway, and states no numbers, while the fig-alt promises 'historical reported patterns' the caption withholds. The chapter's own fairness figure two sections later is a model of how to do this — it states every percentage in the caption.

**Edit.** Rewrite as a claim with the numbers the body already supplies: 'Removing the responder's power to reject cuts giving sharply — from ultimatum offers modally around 40–50% to dictator transfers averaging about 20% (Forsythe et al., 1994) and closer to 10% under double-blind procedures (Hoffman et al., 1994). Changing whether the allocator may take as well as give alters the property rights and the meaning of the same final allocation.' Move 'original redraw' to the end or drop it, matching the treatment of @fig-fairness-entitlements-redraw.  *(effort: small)*

---

## `chapters/26-social-norms-and-conformity-when-other-people-become-evidence.qmd`  (17 findings)

### [HIGH · engagement] ## Conformity is an outcome, not a mechanism

> yet some participants publicly agreed with a unanimous wrong majority

**Problem.** The single most famous result in the chapter is delivered in a subordinate clause with the vaguest possible quantifier ("some participants"). The surprise — that people deny the evidence of their own eyes about a line length visible from across the room — is completely flattened. The same paragraph also compresses Sherif and Deutsch & Gerard, so three landmark studies pass in four sentences with zero numbers.

**Edit.** Give Asch two short paragraphs with the actual numbers, which also make the chapter MORE accurate by pre-empting the popular overstatement. Suggested: "The lines were not close calls; the correct match was obvious to isolated control participants, who erred on under 1% of trials. Yet participants went along with the unanimous wrong majority on roughly a third of critical trials. The number people remember is that a third conformed. The number worth remembering is the other one: about a quarter of participants never conformed once, and a further group conformed only occasionally." Verify the exact rates against Asch (1956) before setting.  *(effort: medium)*

### [HIGH · engagement] ## Social proof is a cue; a cascade is a mechanism

> showing download counts made success more unequal and outcomes more variable

**Problem.** Salganik's Music Lab is the chapter's best available piece of evidence that popularity partly manufactures itself, and it is described with two abstract comparatives and no number, no song, no magnitude. The concrete design — thousands of participants split into parallel worlds that could not see each other — is the thing that makes the result believable, and it appears only in the fig-alt of the figure that follows, where prose readers will not encounter it.

**Edit.** Move the design into the body and give it stakes: "Salganik and colleagues recruited roughly 14,000 participants, split them into eight independent 'worlds,' and let each world discover the same 48 unknown songs. In some worlds participants saw how many others had downloaded each song; in the control, they did not. The songs were identical. The worlds were not: a song that finished near the top in one social world could finish near the bottom in another, while in the independent condition rankings stayed far more stable." Then keep the existing hedge that quality still mattered — the honest version (quality sets a range, social influence picks the point within it) is more interesting than either extreme.  *(effort: medium)*

### [HIGH · insight] ## Conformity is an outcome, not a mechanism

> even one dissenter can make disagreement socially possible

**Problem.** This is the most actionable sentence in the chapter for anyone running a meeting, and it is stated as a soft possibility with no magnitude. The reader has no way to know whether one ally matters a little or enormously. The Practice Lab and the "Independence before discussion" list both depend on this claim ("one designated ally for dissent"), so the chapter is asking the reader to act on an unquantified assertion.

**Edit.** Replace with the magnitude: in Asch's partner conditions a single confederate who gave the correct answer cut conformity errors to roughly a quarter of their level, and this held even when the ally was wrong in a different direction — what mattered was breaking unanimity, not being right. Then make the organizational implication explicit: unanimity, not majority size, is the pressure variable, which is why appointing one person whose job is to disagree is cheaper and more effective than adding three more committee members.  *(effort: medium)*

### [HIGH · insight] ## Social norms require a reference group

> compared with 1.67% under a sign asking visitors not to remove it

**Problem.** The chapter reports the descriptive-norm sign (7.92%) against the injunctive sign (1.67%) but omits the no-sign control (about 2.92%). That omission loses the genuinely counterintuitive result: the well-intentioned descriptive sign did not merely underperform the better sign — it produced roughly three times more theft than posting nothing at all. As written, a reader could conclude the descriptive sign was just less effective, when the actual lesson is that a norm campaign can be worse than silence.

**Edit.** Add the control and state the kicker directly: "A third area carried no sign at all; there theft ran at about 2.92%. The descriptive sign did not merely help less than the injunctive one. It did roughly three times more damage than saying nothing." Then one sentence of 'so what': the sign's authors intended it as a deterrent, which is why a norm message needs a pretest rather than good intentions.  *(effort: small)*

### [HIGH · structure] ## Independence before discussion

> Asch-type conformity varies across periods, cultures, tasks, and response conditions

**Problem.** Line 144 contains a bare anchor `[]{#ch26-research-findings}` followed by a single orphan sentence with no heading, sitting between the end of "Independence before discussion" and "## Practice Lab". It reads as the residue of a deleted section. The anchor name promises "research findings" and delivers one line. A cross-reference elsewhere in the book may point at this anchor and land on a fragment.

**Edit.** Either delete the anchor and fold the Bond & Smith sentence into the Asch paragraph, or promote it into a real short subsection under "Conformity is an outcome, not a mechanism" that says what the meta-analysis actually found: across 133 studies in 17 countries, conformity was higher in more collectivist samples and US conformity rates declined across the decades after Asch — which supports the chapter's core thesis that conformity is an outcome of conditions, not a fixed human constant. Then grep the repo for `#ch26-research-findings` and repoint any inbound link.  *(effort: small)*

### [MEDIUM · accuracy] ### The social brain is not simply the individually smartest brain

> reported that trained chimpanzees could outperform adult humans

**Problem.** This comparison has a well-known confound that the chapter does not mention: the chimpanzees in Inoue and Matsuzawa (2007) had extensive prior training on the numeral task while the human comparison participants did not. Silberberg and Kearns (2009) and subsequent work reported that practised humans match or exceed the chimpanzee performance. As written, a single contested study is presented as a settled species contrast and then used to carry a thesis about human cognition being distinctively social. That is exactly the pattern the book's voice otherwise avoids.

**Edit.** Add a clause and a citation: "...although the human comparison participants were untrained, and later work reported that humans given comparable practice can match this performance (Silberberg & Kearns, 2009). The point survives the qualification in a weaker and more defensible form: whatever the ceiling on individual working memory, it is not where the human advantage lies." Add the Silberberg and Kearns reference to the list.  *(effort: medium)*

### [MEDIUM · accuracy] ### Mimicry and synchrony

> Some experiments have also found more helping after participants were mimicked

**Problem.** The mimicry literature sits inside the social-priming cluster with the weakest replication record in social psychology, and the chapter's hedge ("depends on the relationship and setting") describes moderation rather than replication uncertainty. Those are different claims. The van Baaren et al. (2004) helping studies used small per-cell samples, and preregistered replication attempts have found substantially smaller or null effects. The chapter is scrupulous about the marginal p = .06 in the figure caption but does not apply the same scrutiny to the downstream behavioral claim.

**Edit.** Change the hedge to name the actual issue: "These are small-sample studies from a research area whose replication record is mixed; preregistered replications of mimicry effects on helping have generally produced smaller estimates than the originals. Treat the direction as plausible and the magnitude as unsettled." Verify and cite one specific replication source. Separately, confirm the N = 35 in the fig-mimicry-study-redraw caption against Chartrand and Bargh's Experiment 1 — published accounts give a recruited N of 39, so the caption may be reporting the analysed subsample without saying so.  *(effort: medium)*

### [MEDIUM · clarity] ## Social norms require a reference group

> Hotel guests were more likely to reuse towels when a sign described reuse

**Problem.** The sentence carries its attribution as a trailing prepositional phrase ("...environmental appeal in Goldstein et al.'s (2008) setting") 26 words after the subject, so the reader must hold the comparison open across the whole sentence before learning whose study it is. It also reports a directional result with no magnitude, immediately before a paragraph that does give magnitudes (Cialdini's 7.92% vs 1.67%), making the pacing uneven.

**Edit.** Recast front-loaded and quantified: "Goldstein and colleagues (2008) tested hotel towel-reuse signs. A sign reporting that most guests who had stayed in this room reused their towels outperformed a standard environmental appeal by roughly nine percentage points." Insert the exact figures from the paper. Then add the honest boundary in the author's own register: the reference group was moved from 'guests' to 'guests in this room,' which is a small design change with a small effect — useful precisely because it is cheap, not because it is large.  *(effort: small)*

### [MEDIUM · clarity] ## Learning goals, goal 1

> Treat conformity as an observed outcome, then distinguish informational learning

**Problem.** Three goals open with verbs that cannot be assessed: ch26 'Treat conformity as an observed outcome…', ch41 'Protect independent evidence, structured disagreement, and accountable use of models or AI', ch38 'Add an advanced term only when its measurement… are defensible'. A reader cannot tell whether they have treated, protected, or added something. Every other goal in the book names an observable act.

**Edit.** ch26: 'Classify one observed instance of agreement into informational learning, normative pressure, coordination, identity, or correlated copying, and name the evidence that separates your choice from the nearest rival.' ch41: 'Design a judgment process that preserves independent estimates before discussion and records how dissent changed the decision.' ch38: 'Justify at most one advanced term by naming the diagnosed problem, its measurement, and its implementation burden.'  *(effort: small)*

### [MEDIUM · engagement] ## Social proof is a cue; a cascade is a mechanism

> people privately doubt or reject a position yet misperceive others as accepting it

**Problem.** Pluralistic ignorance gets a purely definitional paragraph — abstract noun, abstract noun, disclaimer about what it is not — with no instance at all, in a chapter that elsewhere anchors every concept in a scene. Prentice and Miller (1993) is cited but their finding is never stated, so the reader gets the label without the demonstration. This is the chapter's longest stretch of definition-without-instance.

**Edit.** State the finding in one sentence before the definition: Prentice and Miller found that students on average reported being personally more uncomfortable with campus drinking than they believed the typical student was — everyone was privately more moderate than the norm everyone inferred from everyone else's public behavior. Then close the loop back to the hiring committee: the member who withheld her doubt has just made the room's norm look more confident than any individual in it.  *(effort: small)*

### [MEDIUM · engagement] # Social Norms and Conformity: When Other People Become Evidence

> Their agreement looks the same from outside, although one may be revising a belief

**Problem.** The opening scene is structurally correct and does its analytic job, but it has no stakes and no specifics: an unnamed candidate for an unnamed role, a chair with an unnamed judgment, and no consequence attached to getting it wrong. The reader is told two committee members disagree internally but is given nothing to care about. The chapter's thesis is that public agreement destroys information — that only bites if the reader can feel what the lost information was worth.

**Edit.** Add one sentence of stakes and one concrete detail before the pivot question. For example, name what the work sample actually showed (a specific failure the doubting member noticed and nobody else mentioned), and name the cost of the error (the role, the hiring horizon, what a bad hire costs the team). Keep the scene at the same length by trimming the abstract summary sentence — the chapter does not need to tell us the two states "look the same from outside" if the scene shows it.  *(effort: small)*

### [MEDIUM · insight] Core Idea (line 27) and the section on public alignment

> Public alignment can reflect learning, pressure, or copying

**Problem.** AI is quarantined. Counting AI terms per chapter: 73 in ch42, 29 in ch41, 6 in ch04, then two or fewer everywhere else and zero in 24 of 42 chapters. Chapter 26 is where the quarantine costs the most. The chapter's central claim is that others' agreement is informative only when their judgments formed independently — and synthetic accounts, bot amplification, and machine-generated reviews break that independence at industrial scale. The only place the book discusses manufactured social proof is a retired file (chapters/retired-conformity-norms-and-social-proof.qmd), which is not built.

**Edit.** Add ~300 words to the public-alignment section: when the nods around the table can be generated at zero marginal cost, 'how many others agree' stops being evidence and becomes a production statistic. Give the reader the diagnostic the chapter already implies — ask what each agreeing party could have observed independently, and what it would cost to fabricate the agreement. Apply the same principle across the book (AI enters a chapter only where it changes a mechanism that chapter already teaches): ch13 (machine-generated text raises processing fluency without raising evidential support), ch10 (personalized retrieval as a better toolkit for motivated search), ch32 (LLM drafts are fluent by construction, which is the trap '## Fluency: power and danger' already names), ch36 (AI-assisted preparation and the asymmetry when only one side has it), ch03 (recommenders as the attention-allocating institution).  *(effort: small)*

### [MEDIUM · structure] ## Research Lens: social learning and cumulative culture

> Research Lens: social learning and cumulative culture

**Problem.** This collapsed callout runs roughly 1,100 words — about 30% of the chapter — and contains its two most memorable pieces of content: the Horner and Whiten overimitation study, and the reframe that children's apparently irrational copying may be the smarter strategy under causal opacity. Placed inside `collapse=true`, most readers will never open it, and the main chapter's claim that "copying can preserve a useful routine or reproduce an untested error" is left without its best demonstration.

**Edit.** Promote the overimitation material (roughly lines 181-187) into the main body of "Other people as living data," where it directly serves the new-employee scenario about the skipped final check — the parallel is exact and currently unexploited. Keep the comparative-cognition material (chimpanzee memory, Dunbar, matching pennies) in the collapsed Research Lens, which is genuinely optional depth. Do not expand the callout wholesale; the fix is moving one subsection, not flattening the structure.  *(effort: medium)*

### [MEDIUM · visual] ## Conformity is an outcome, not a mechanism

> An Asch-style line-comparison activity. Choose a line before imagining

**Problem.** The caption is an instruction to the reader, not a statement of what the figure shows or why it matters. A reader scanning captions to navigate the chapter learns nothing about the argument from this one. The chapter's other captions (norm-message-diagnostic, social-pathways) correctly state claims, so this is an inconsistency as well as a weakness. The same issue affects the family-photograph caption, "Matching postures in a family photograph illustrate behavioral similarity," which is a label with no takeaway.

**Edit.** Lead the caption with the claim and demote the instruction: "The correct match is not ambiguous — which is precisely what makes public agreement with a wrong majority informative about social pressure rather than about perception. Choose a line yourself, then imagine several people answering B aloud before your turn." For the photograph: "Unplanned postural matching between a child and an adult — the kind of alignment that happens without either party noticing."  *(effort: small)*

### [MEDIUM · visual] ## Four conditions make social evidence more diagnostic

> First, observers need **relevant contact with the problem**.

**Problem.** Four numbered conditions run for about 400 words of tightly reasoned abstraction with no visual anchor, and each is then tested nowhere except in prose. This is the chapter's analytic spine — the thing a reader would want to carry into a real meeting — and it exists only as running text. The reference table earlier in the chapter is inside a collapsed callout, so a reader who does not expand it sees an unbroken run from line 36 to the Asch figure at line 79.

**Edit.** Add a compact four-gate diagram: a stream of individual judgments entering left, passing through four labelled gates in sequence — CONTACT (did they touch the problem?), INDEPENDENCE (how many distinct sources?), DIVERSITY (do different positions reach the decision?), AGGREGATION (what rule combines them?) — with the pipe narrowing at each gate. Annotate the output with two endpoints: "ten independent reports" versus "one report repeated ten times," both arriving as the same-looking consensus. That single image does the work of the whole section and gives the Practice Lab a checklist shape.  *(effort: large)*

### [LOW · clarity] line 77

> Asch's line-judgment studies changed the problem.

**Problem.** Two different Solomon Asch studies appear in two chapters with no signal that they are different studies by the same researcher. Chapter 11 line 62 uses Asch (1946) on impression formation and trait order; Chapter 26 line 77 uses Asch (1956) on line judgment and conformity. This is correct scholarship, not duplication — but a reader who met "Solomon Asch's classic work" in ch11 will reasonably assume ch26 is revisiting it, and the two chapters do not link to each other (both are zero-outbound-link chapters). The 1946/1956 dates are visible only in the reference lists.

**Edit.** One clause removes the collision and adds a small payoff: "Asch's line-judgment studies — a different program from the impression-formation work in [*When Context Rewrites Comparison*](11-when-context-rewrites-comparison.qmd) — changed the problem." Cheap to do, and it gives ch11 one of the inbound links it currently lacks.  *(effort: small)*

### [LOW · consistency] ## References cited in this chapter

> Boyd, R., & Richerson, P. J. (1985). Culture and the evolutionary process.

**Problem.** The reference list is two separately alphabetised blocks concatenated: entries run Boyd through van Baaren, then restart at Asch and run through Sparkman. Within the second block there are further ordering errors (Bikhchandani before Bicchieri; Salganik and Sherif before Schultz). Separately, the first table carries the stale identifier `{#tbl-22-1}`, inherited from this chapter's former number 22 (see the file's own alias), while the second table uses a semantic id `{#tbl-social-alignment-mechanisms}`.

**Edit.** Merge into one alphabetical sequence. Rename `tbl-22-1` to something semantic such as `tbl-social-cue-audit` and grep the repo for `tbl-22-1` to repoint any cross-reference. Worth checking whether the same two-block pattern exists in other chapters that were renumbered, since chapter 27's list has the identical defect.  *(effort: small)*

---

## `chapters/27-markets-mispricing-and-bubbles.qmd`  (17 findings)

### [HIGH · clarity] ## A bubble is a reinforcing-process hypothesis

> Here $D_t$ must incorporate the timing and risk relevant to that claim.

**Problem.** Lines 118-124 are a single seven-sentence paragraph that opens on fundamental-value definition, detours into discount-factor mechanics and certainty equivalents (a term used without definition), issues a methodological instruction, and then — in its last sentence — delivers the chapter's operative definition of a bubble diagnosis. The section's title concept is buried in the tail of a paragraph about discounting. A reader tracking the argument loses the thread precisely where the chapter turns.

**Edit.** Split into three. (1) Fundamental value is not printed beside the price, with the formula. (2) The discounting caveat — define certainty equivalent in a clause, or cut the sentence entirely, since it adds a second valuation route the chapter never uses. (3) A new paragraph beginning at "A bubble diagnosis becomes more plausible when..." so the definition gets its own opening position and the four conditions (gains raise expectations, attention and financing follow, demand or resale is induced, the forecast is temporarily validated) can be set as a short numbered list rather than a comma chain.  *(effort: medium)*

### [HIGH · engagement] ## Opening puzzle: earnings beat expectations

> A listed company reports earnings above the analyst consensus before the market opens.

**Problem.** The chapter opens on a hypothetical with no company, no numbers, no dollar amounts, and no person — "a listed company," "the analyst consensus," "an attractive return." Compare chapter 26, which opens on a specific room with specific people. A reader cannot form a mental image of anything here. The section also carries a `## Opening puzzle` heading, which deviates from the template's unheaded opening scenario used across the book.

**Edit.** Make it a real announcement with real numbers, then let the puzzle emerge from them: a named (or clearly composite-labelled) firm reports EPS of, say, $1.42 against a consensus of $1.31, the stock is quoted 9% higher in pre-market before you can place an order, and by the time you can trade at 9:30 the entire beat is in the price — so your question is not "were earnings good" but "what is left." Give the reader the two prices. Then drop the `## Opening puzzle` heading so the scene sits unheaded before the Core Idea, matching every other chapter.  *(effort: medium)*

### [HIGH · engagement] ## Fast price discovery is possible

> establishes its release at 14:00 on September 18, 2013

**Problem.** The chapter names one of the most dramatic price-discovery events on record and then declines to say what happened, handing the reader a homework assignment instead: "To measure how quickly the market responded, an event study must pair that timestamp with price and volume data." This is a paragraph explaining what could be done rather than doing it. The section is titled "Fast price discovery is possible" and contains no demonstration of fast price discovery — the Challenger case that follows is about dispersed inference, not speed.

**Edit.** Tell the story. The September 2013 no-taper decision moved Chicago futures within about two milliseconds of the 14:00 Washington release — faster than information can travel the roughly 1,000 km between the cities at the speed of light, which is what made the episode evidence of an early release rather than of fast trading. That is a genuinely startling fact, it is documented, and it makes the chapter's real point better than any abstraction: the speed at which prices move is now far below the speed at which a human can read a sentence. Then land the implication the chapter already wants — "recognizing the news correctly may still come too late" — as a consequence the reader has just felt rather than been told.  *(effort: medium)*

### [HIGH · engagement] ## Fast price discovery is possible

> By the end of the trading response, Morton Thiokol experienced the distinctive loss.

**Problem.** This is the chapter's most remarkable claim — that a market identified the guilty supplier months before a presidential commission did — and it is delivered in a nine-word clause with no magnitude, in the passive-adjacent register ("experienced the distinctive loss"). The reader has no way to know whether the discrimination was a rounding error or overwhelming. The following sentence, "Collective trading can reveal information no single public announcement states," then asserts the conclusion the prose never earned.

**Edit.** Give the numbers and the texture: the four contractors all fell together in the first minutes, but by the close Morton Thiokol was down roughly 12% while Lockheed, Martin Marietta, and Rockwell had each lost about 3%; Thiokol's stock was halted for a period that day on order imbalance. Add the corrective the popular retelling omits and that the author's voice requires: the separation was not instantaneous, it emerged over hours of trading, and Maloney and Mulherin found no insider-trading trail and no news story that explained it — which is what leaves dispersed inference as the residual explanation rather than as a demonstrated one.  *(effort: medium)*

### [HIGH · engagement] ### One laboratory market: a known risk-neutral benchmark can still be exceeded

> Prices in many baseline markets nevertheless rose above the benchmark and later fell

**Problem.** The Smith-Suchanek-Williams result is the strongest evidence in the chapter that bubbles do not require ambiguous fundamentals, and it is stated with no numbers at all — the formula FV = kd is given but never instantiated. "Rose above the benchmark" could mean 5% or 300%. The genuinely arresting fact is buried: subjects held a printed dividend table, could compute the exact expected value at every moment, and traded at multiples of it anyway.

**Edit.** Work the arithmetic once, in the text: with a 15-period asset paying an expected 24 cents per period, fundamental value starts at $3.60 and steps down by 24 cents each period to $0.24 in the final round — and every trader has this table in front of them. Then give the observed magnitude from the paper: prices in baseline sessions routinely traded at several times the contemporaneous benchmark through the middle periods before collapsing near expiry. Close with the point the section is built to make: the ambiguity explanation for bubbles is not necessary, because here there was none.  *(effort: medium)*

### [HIGH · visual] ### One field episode: dot-com innovation and extreme expectations

> the NASDAQ Composite rose about 579%

**Problem.** Four dated index levels and two percentage changes are delivered as running prose in a single sentence pair — 743.58, 5,048.62, 1,114.11, 579%, 77.9% — which is exactly the load a small chart carries better than a sentence. The chapter's most viscerally persuasive available evidence (a five-year climb erased in thirty months) is currently something the reader must reconstruct arithmetically. This is also the only major section in the chapter with no visual of its own.

**Edit.** Add a log-scale NASDAQ Composite line from January 1995 to December 2002, with three labelled markers: 1995-01-03 at 743.58, 2000-03-10 peak at 5,048.62, 2002-10-09 at 1,114.11. Log scale matters — it makes the shape read as a compounding process rather than a spike, which is the chapter's actual claim. Annotate the descent with the elapsed time (about 31 months) so the asymmetry between the climb and the fall is visible. The data are already sourced to FRED NASDAQCOM, so the series is reproducible. Caption it as a claim, not a label: something like "Five years of gains, then thirty-one months that returned the index below its 1996 level — the same chart supports both an innovation story and a feedback story, which is why the episode needs a diagnostic rather than a glance."  *(effort: large)*

### [MEDIUM · clarity] ## A bubble is a reinforcing-process hypothesis

> state the growth, margin, risk-adjustment, discount-rate, and terminal assumptions

**Problem.** The chapter instructs the reader to reverse-engineer the assumptions embedded in a price and gives a formula, but never demonstrates the procedure with numbers. The memo's point 3, "What does the current price already require the firm or market to achieve?", asks for exactly this operation, so the reader is assigned a technique the chapter has shown only in symbols. This is the one place where a worked example would convert an abstraction into a skill.

**Edit.** Add a five-line worked reversal: take a firm trading at a stated price, hold the discount rate fixed, and solve for the growth rate the price requires — then show the same price under two other discount rates so the reader sees how much of the "required growth" is really an assumption about rates. A small 3x3 table (growth rate down the side, discount rate across the top, implied value in the cells, observed price highlighted) does this compactly and shows the reader that one cell of a sensitivity grid is what most valuation disagreements actually reduce to. Keep the existing caution that discounting risky flows at a risk-free rate overstates value; the table demonstrates it.  *(effort: medium)*

### [MEDIUM · engagement] ## The Palm–3Com case: visible inconsistency, costly correction

> observed prices implied that the residual 3Com businesses were worth about negative $22 billion

**Problem.** Negative $22 billion is a large abstract number; the per-share arithmetic that makes the absurdity feel absurd is omitted, even though the chapter has just written the relative-value equation. The reader is told "simple addition makes that hard to defend" without being shown the simple addition. This is the book's single best example of a visible, checkable, arithmetic-level mispricing and the arithmetic is missing.

**Edit.** Do the subtraction in the text: Palm closed its first day at about $95 a share, so the 1.5 Palm shares embedded in each 3Com share were worth roughly $143 — while 3Com itself closed near $82. Buying 3Com therefore meant paying $82 for $143 of Palm plus a profitable, cash-rich operating business, and the market was valuing that business at about negative $61 per share. Multiply by 3Com's share count and the residual is the -$22 billion figure. Then keep the existing limits-to-arbitrage turn intact — it is the best paragraph in the section and it lands harder once the reader has done the subtraction themselves.  *(effort: small)*

### [MEDIUM · engagement] ## Evidence Boundary: an anomaly is not a mechanism or a trade

> found that average predictability declined after publication

**Problem.** The McLean and Pontiff result is one of the cleanest facts in empirical finance and it is stated without its magnitude, so the reader cannot tell whether "declined" means a shaving or a collapse. The same paragraph invokes "thousands of securities, variables, transformations, and subperiods" as an abstraction where Harvey, Liu and Zhu supply a concrete count.

**Edit.** Insert the magnitudes: McLean and Pontiff found that predictor returns fell by roughly a quarter out of sample and by roughly half again after publication — the strategies decayed fastest in exactly the stocks where trading costs were lowest, which is what makes correction-through-trading the leading explanation rather than pure data mining. And give Harvey and colleagues' number: they catalogued well over 300 published return predictors and argued that conventional significance thresholds are far too permissive given that search. Verify both figures against the papers before setting.  *(effort: small)*

### [MEDIUM · engagement] ### One laboratory market: a known risk-neutral benchmark can still be exceeded

> The evidence supports interaction among heterogeneous trading strategies.

**Problem.** A full table plus a figure plus a paragraph of methodological detail resolve into a nine-word conclusion that says almost nothing — "interaction among heterogeneous trading strategies" is a restatement of the fact that different traders behaved differently. The section builds to a flat stop, and the reader never learns why the mix matters.

**Edit.** Replace with the consequence: roughly a third of traders tracked fundamentals throughout, and they did not stop the bubble. That is the finding. A market does not need a majority of irrational participants to produce a bubble-like path; it needs enough feedback and speculative demand to move the price, and enough friction that the fundamentalists cannot absorb it. Then connect explicitly back to the limits-to-arbitrage section — the laboratory reproduces, in miniature and with no borrowing costs at all, the same asymmetry that Shleifer and Vishny describe in the field.  *(effort: small)*

### [MEDIUM · insight] ## A two-direction bubble dashboard

> Even a high bubble probability does not reveal timing.

**Problem.** The chapter correctly says timing is not revealed, then stops one step short of the finding that would make the section memorable and would tell the reader what the dashboard is actually good for. Greenwood, Shleifer and You (2019) examined industry price run-ups and found that a sharp run-up did not on its own predict lower average future returns — but it sharply raised the probability of a large crash, and predicted it better in combination with the accelerating-price, high-issuance, and high-turnover features the chapter's own dashboard rows already list. That result validates the dashboard's design and explains the chapter's robustness prescription.

**Edit.** Add a short closing paragraph: a run-up alone is a weak signal about the mean, and a much stronger one about the tail — which is why the honest output of this dashboard is a statement about crash probability and exposure, not a forecast of a date. Then state what remains unknown, in the author's own register: no published bubble indicator has demonstrated reliable out-of-sample timing, which is the reason to manage leverage and position size rather than to attempt an exit at the peak. Cite Greenwood, Shleifer, and You (2019, Journal of Financial Economics) and add it to the reference list.  *(effort: medium)*

### [MEDIUM · insight] ### Strategic resale and synchronization risk

> A buyer can believe that a price exceeds their own estimate of fundamental value

**Problem.** This is the point where chapter 26's information cascade and this chapter's bubble mechanism are structurally the same idea, and the connection is never made. The link to chapter 26 appears much later, in "Investor behavior," and only for the narrow point about independent evidence. The sharper and more memorable observation — that a price is a cascade with a payoff attached — is available and left implicit.

**Edit.** Add two sentences opening the subsection: in a cascade (chapter 26), later actors abandon a private signal because earlier actions look informative; the cost of following is only being wrong. In a market, following pays. A buyer who thinks the price is too high can still profit by joining, provided someone else joins after them — which converts a cascade from an inference error into a rational trade and explains why market bubbles can persist against far stronger contrary information than social cascades survive. Then the existing synchronization-risk material becomes the answer to the obvious next question: why do the skeptics not end it?  *(effort: small)*

### [MEDIUM · structure] ## Practice Lab

> Produce a falsifiable market memo and a two-direction bubble dashboard with a robust action.

**Problem.** Learning goal 3 promises the reader will produce a memo and a bubble dashboard; the Practice Lab asks only for an event-study audit. Learning goal 2 promises evaluation of four evidence types (event study, limits-to-arbitrage case, laboratory market, field episode); the Practice Lab exercises one. So the chapter builds a ten-point memo template and a four-domain dashboard table, then never asks the reader to fill either in. The two most transferable deliverables in the chapter are demonstrated but not assigned.

**Edit.** Restructure the Practice Lab as two short tasks rather than one long one. Task A: the existing event-study audit (serves goal 2's first item). Task B: pick one asset currently attracting attention, complete the ten-point memo for a position you will not take, and fill the four rows of the bubble dashboard in both columns — naming, for each row, the one observation that would move you. Require the robust action the chapter specifies (position cap, review date, funding stress test) rather than a directional call. Add a one-line date-stamp instruction so the record is testable later, which is the chapter's own thesis.  *(effort: medium)*

### [MEDIUM · visual] ## The Palm–3Com case: visible inconsistency, costly correction

> $$
P(3Com) \approx 1.5P(Palm) + \text{value of 3Com's other businesses}.
$$

**Problem.** The section has an equation and no figure, in a chapter where a single diagram would make the case unforgettable. The stub-value picture is inherently visual — two stacked bars that should nest and instead overflow — and it is the one image a reader would carry out of the chapter.

**Edit.** Add a two-bar diagram. Left bar: the observed 3Com share price (~$82), drawn to scale. Right bar: the components it should contain — a tall segment of 1.5 x Palm (~$143) plus a positive segment for 3Com's other businesses. The right bar visibly overshoots the left, and the gap is shaded and labelled "implied value of 3Com's remaining businesses: about -$61 per share (~-$22 billion)." Add a short caption stating the takeaway claim: the mispricing required no valuation model, only subtraction — and it persisted anyway, because Palm shares could not be borrowed cheaply. Sourced to Lamont and Thaler (2003).  *(effort: large)*

### [MEDIUM · visual] ## Classification details

> : Rule-based behavioral classifications in Haruvy and Noussair (2006)

**Problem.** The four classification percentages (36.5, 33.1, 25.4, 4.9) appear three times in immediate succession: in the collapsed table `tbl-bubble-strategies`, again in the caption of `fig-bubble-trader-strategies-redraw`, and again in that figure's fig-alt. The figure and the table carry identical content. Meanwhile the section's genuinely explanatory image — the price path against the declining fundamental-value step function — does not exist anywhere in the chapter. Scarce figure budget is being spent on four numbers that a sentence could carry.

**Edit.** Delete either the table or the redrawn bar chart (the table, inside its collapsed callout, is the more disposable of the two given the methodological detail it preserves — so keep the table and cut the redundant bar chart, or vice versa, but not both). Then commission the figure the section actually needs: mean transaction price by period plotted against the FV = kd step function, with the benchmark descending from $3.60 to $0.24 and the price path arcing above it and crashing near expiry. That single image proves "a known benchmark can still be exceeded" in a way no percentage breakdown can.  *(effort: medium)*

### [LOW · accuracy] ## Advanced research track: auditing an event study

> documented **post-earnings-announcement drift**

**Problem.** Post-earnings-announcement drift is attributed solely to Rendleman, Jones and Latané (1982). The phenomenon was first documented by Ball and Brown (1968), and the standard modern references establishing its robustness and its resistance to risk-based explanation are Bernard and Thomas (1989, 1990). Citing only the 1982 paper understates how long-standing and how heavily scrutinised the pattern is — which matters here, because the chapter's argument is that a pattern surviving decades of attack is different in kind from a fresh backtest.

**Edit.** Change to "first documented by Ball and Brown (1968) and studied extensively since (Rendleman et al., 1982; Bernard & Thomas, 1989)" and add both references. The anomalies table's Earnings drift row should carry the same correction. This strengthens rather than weakens the chapter's joint-test caution: drift is the anomaly that has survived the most scrutiny, and it still has not settled the question.  *(effort: small)*

### [LOW · consistency] ## Core idea

> ## Core idea

**Problem.** Three small template deviations in this file. The Core Idea heading is lowercase here and title-case ("## Core Idea") in chapter 26 and elsewhere, which will surface as inconsistent in any generated contents or callout styling that keys on the heading text. The file also lacks the `::: {.content-visible unless-format="epub"}` anchor block that chapter 26 carries immediately after its title, so epub-safe inbound linking differs between the two. And the reference list has the same two-concatenated-alphabetical-blocks defect as chapter 26 (Barber, Barberis, Banz, then Abreu; a second block restarting at Dufwenberg; Hussam before Holt).

**Edit.** Change to `## Core Idea`; add the matching content-visible anchor block after the chapter title; merge the reference list into one alphabetical sequence. Worth running a repo-wide check for `## Core idea` and for the split-reference-list pattern, since both defects appearing in two adjacent files suggests they are not isolated.  *(effort: small)*

---

## `chapters/28-authority-groupthink-and-shared-responsibility.qmd`  (16 findings)

### [HIGH · clarity] ## Groupthink: a familiar but contested umbrella

> Check whether each safeguard reveals previously hidden evidence or disagreement.

**Problem.** This paragraph opens with 'each safeguard' when no safeguards have been mentioned in the prose. The antecedent lives inside the preceding figure, which is dropped into the text with no lead-in sentence and no cross-reference. Neither chapter uses @fig- or @tbl- anywhere, so the figure and the collapsed table float free of the argument. A reader who skips the image hits a paragraph with a dangling referent, then an Edmondson citation that arrives without any bridge.

**Edit.** Add a lead-in sentence before the figure that does the referring work, cross-referenced properly: 'Silence is not one mechanism. @fig-silence-mechanisms separates five pathways, each with an observable test and a safeguard that fits only that pathway.' Then open the following paragraph with its job rather than a pronoun: 'Each safeguard should be judged by whether it surfaces something the group did not already have.' Move the Edmondson sentence into that paragraph with a connective, or cut it here — as it stands it is a bare finding with no link to the safeguards on either side.  *(effort: small)*

### [HIGH · engagement] ## Authority and responsibility

> remain among the most famous and disturbing studies in psychology

**Problem.** The chapter's centerpiece study is described entirely without numbers. The reader is told the studies are famous and disturbing rather than shown anything that would produce that reaction. In a book that elsewhere quotes effect sizes and sample sizes precisely, an obedience chapter with zero obedience rates reads as evasive rather than careful.

**Edit.** Replace the 'famous and disturbing' assertion with the baseline result stated in the sentence: 'In the condition reported in 1963, 26 of 40 participants — 65 percent — continued to the maximum 450-volt switch, past the point where the learner had stopped responding.' Then add Burger's number where he is already cited: 'Burger (2009) found that 70 percent continued past 150 volts, against 82.5 percent in Milgram's comparable condition, a difference that was not statistically significant.' Verify both against Milgram (1963, p. 376) and Burger (2009, p. 5).  *(effort: small)*

### [HIGH · insight] ## Authority and responsibility

> Burger (2009) reproduced substantial continuation to a lower stopping point

**Problem.** The chapter presents obedience as a single phenomenon with a single rate. The scientifically important and genuinely counterintuitive fact — that Milgram ran roughly two dozen variations and that full obedience swung from near zero to over 90 percent depending on the situation — is never stated. That variation is what converts Milgram from a fable about human nature into a design claim about situations, which is exactly the chapter's thesis.

**Edit.** Add a short paragraph after the Burger sentence: obedience fell as the learner became more proximate (roughly 65 percent remote, 40 percent same-room, 30 percent when the participant had to press the learner's hand onto the plate), collapsed when two confederate peers refused, and collapsed to zero when two authorities gave contradicting orders. Then draw the line the chapter needs: the same person obeys or refuses depending on features a manager can actually change — proximity to the harmed party, whether anyone else has already objected, and whether authority speaks with one voice. Verify the cell values against Milgram (1974) before publishing exact percentages.  *(effort: medium)*

### [HIGH · insight] ## Groupthink: a familiar but contested umbrella

> Match the safeguard to the pathway.

**Problem.** The figure caption instructs the reader to match safeguard to pathway, but the body never states the payoff of getting the match wrong. The memorable point is one step away and unmade: the five pathways call for opposite remedies, and applying the wrong one can make things worse rather than merely fail.

**Edit.** Add two or three sentences after the figure making the mismatch explicit with instances. An open invitation to speak ('Any concerns?') helps with suppressed dissent but actively worsens diffusion of responsibility, because it spreads an unowned request across everyone present. Naming a single owner fixes diffusion but does nothing about a hidden profile, because the owner may still lack the evidence. Anonymous polling reveals pluralistic ignorance but cannot supply expertise nobody in the room has. This is the sentence readers will remember: a safeguard aimed at the wrong pathway does not just miss, it can confirm that the matter was handled.  *(effort: medium)*

### [HIGH · structure] ## Learning goals

> shared-information bias and hidden profiles, pluralistic ignorance, and diffusion of responsibility

**Problem.** Learning goal 2 promises the reader will be able to distinguish five pathways, and appendix-d-index-of-major-course-examples.qmd advertises 'hidden-profile tasks' as one of this chapter's major examples. But shared-information bias and hidden profiles appear nowhere in the body — only inside one cell of a collapsed table placed after 'Take it forward'. False unanimity is likewise named in the goal but never developed. A reader who does not expand the optional block never meets the mechanism.

**Edit.** Promote hidden profiles into the body as its own short section between 'Groupthink' and 'Bystanders and pluralistic ignorance'. Describe the Stasser and Titus (1985) setup concretely: each member is given some facts everyone holds and some facts only they hold, arranged so that the best candidate is visible only if the unique facts are pooled; discussion instead recirculated shared and preference-consistent information, and groups often chose the inferior candidate. Then map it back to the safety email: the manager's reassurance may rest on what everyone already knows, while the one recipient who saw the same fault last quarter never says so.  *(effort: medium)*

### [HIGH · structure] Whole chapter; especially '## Authority and responsibility' (line 36) and '## Groupthink: a familiar but contested umbrella' (line 46)

> Stanley Milgram’s obedience experiments remain among the most famous and disturbing studies in psychology

**Problem.** Chapter 28 carries Milgram, Asch-style conformity pressure, groupthink, hidden profiles, pluralistic ignorance, and diffusion of responsibility — six distinct mechanisms and the field's single most famous experiment — in 2,271 words, the third-shortest chapter in the book. For comparison, ch41 gets 7,460 and ch06 gets 6,433. It is also one of the few chapters with no opening puzzle heading, and it runs an engineering-safety scenario rather than the hiring committee that the preface, how-to-use, and Part I promise as the book's spine — despite the committee's silence being the exact phenomenon the chapter explains. The most-anticipated chapter in the book is its thinnest.

**Edit.** Expand to roughly 4,000 words. Three moves: (1) open with the hiring committee's silence, so the book's spine case finally reaches the chapter about groups; (2) give each of the six mechanisms its own named subsection with a worked diagnostic, since the current text runs several of them together under 'Authority and responsibility'; (3) add the published numbers this chapter is conspicuously missing, which the project has already flagged as the book-wide weakness. Also add a 200-word passage on ethical fading and moral disengagement beside the Milgram material — it explains continuation better than 'obedience' does and connects to the moral-judgment gap below.  *(effort: large)*

### [MEDIUM · accuracy] ## Groupthink: a familiar but contested umbrella

> poorer decisions appeared under additional conditions such as directive leadership

**Problem.** Citation check. Mullen et al. (1994) is correctly cited for the null overall cohesion effect and for the dependence on how cohesiveness was operationalized (interpersonal attraction versus commitment to task versus group pride). The directive-leadership moderator, however, is not the moderator that meta-analysis reports; it comes from the experimental groupthink literature (Flowers, 1977; Leana, 1985; and later Peterson and colleagues). As written, the sentence attributes both moderators to Mullen et al.

**Edit.** Split the attribution: keep 'A meta-analysis found no significant overall effect of cohesion on decision quality, and what effect appeared depended on how cohesion was measured (Mullen et al., 1994)', then attribute the leadership result separately, e.g. 'Experimental work manipulating leadership style has found poorer processes under directive leaders (Flowers, 1977).' Add the corresponding reference entry if the second claim is retained.  *(effort: small)*

### [MEDIUM · clarity] ## Authority and responsibility

> Together, these studies show how a legitimate-looking institutional sequence can produce continuation

**Problem.** 'These studies' has no plural antecedent — only Milgram's experiments have been described, and the preceding sentence cites Haslam and Reicher, which is a review rather than a study. The paragraph also opens with a five-item agentless list of competing explanations before the reader knows what is being explained, so the sentence has to be read twice.

**Edit.** Reorder the paragraph so it opens with its job and fix the referent: 'Why people continued is still disputed. Haslam and Reicher (2017) argue for engaged followership — identification with the scientific project — against blind obedience, while institutional trust, uncertainty about harm, gradual escalation, and pressure to finish the task remain live alternatives. What the variations do establish is narrower: a legitimate-looking institutional sequence can produce continuation despite visible distress, especially when responsibility appears to move upward.'  *(effort: small)*

### [MEDIUM · clarity] ## Practice Lab

> Then produce an escalation map showing who must notice, what observation triggers action

**Problem.** The Practice Lab is one paragraph containing at least eight deliverables stacked into two long sentences (diagnose a pathway, produce a map with six named components, plus write a sentence a junior person can use). It is doable in principle but hard to execute from the page, and the reader cannot check off progress.

**Edit.** Number it: (1) pick the incident; (2) name the most plausible pathway and state the observation that supports it, not the outcome; (3) draw the escalation map as a six-column row — who notices, trigger, owner, receipt confirmation, dissent channel, next escalation and deadline; (4) write the one sentence a junior person can say without first proving wrongdoing. Supplying a model sentence for step 4 ('I may be wrong, but I would like to see the test data before we close this') makes the hardest step imitable.  *(effort: small)*

### [MEDIUM · engagement] opening scenario

> An engineer emails a possible safety fault to seven colleagues.

**Problem.** The opening scene is structurally good but has no people, no object, and no stakes. 'An engineer', 'a possible safety fault', 'a senior manager' are roles rather than characters, and the reader never learns what could go wrong or to whom. Then 'Take it forward' suddenly introduces Lena and Sam, names that appear nowhere else in the book, so the payoff lands on strangers.

**Edit.** Name the people in the opening and give the fault a physical referent and a consequence: 'Lena, a test engineer, emails seven colleagues at 9:40 a.m.: a brake actuator on the pre-production van has failed its hold test twice in a week. If the pattern is real, forty vehicles already in customer hands share the part.' Keep Lena and Sam as the same characters in 'Take it forward' so the closing message reads as the resolution of a scene the reader has been holding for ten pages.  *(effort: small)*

### [MEDIUM · engagement] ## Groupthink: a familiar but contested umbrella

> a familiar account of how pressure for concurrence could narrow

**Problem.** Three consecutive paragraphs discuss groupthink — its claims, its contestation, a meta-analysis — without a single case, date, or decision. A reader who does not already know why the term became famous learns what is wrong with it before learning what it refers to. The debunking therefore has nothing to push against, and the section is the flattest stretch in the chapter.

**Edit.** Give Janis one concrete sentence before the critique: he built the model from retrospective case studies of policy failures, the Bay of Pigs invasion above all, where advisers who privately doubted the plan said nothing in the room. Then the contestation sentence lands with real force, because the reader can see the problem: the evidence was the fiasco, and the syndrome was read backwards out of it. That is also the cleanest illustration in the book of outcome bias in theory-building — a connection worth one clause.  *(effort: small)*

### [MEDIUM · engagement] ## Bystanders and pluralistic ignorance

> less likely to help a person apparently having a seizure

**Problem.** The chapter's second most famous study is again reported without numbers, in a hedged, agentless sentence. 'Less likely' does no work; the actual gradient is what makes the finding surprising, and the meta-analytic effect size is omitted too even though the meta-analysis is cited in the same paragraph for its boundary conditions.

**Edit.** State the gradient: participants who believed they were the only witness reported the seizure about 85 percent of the time, falling to roughly 62 percent with one other believed present and 31 percent with four. Then give Fischer et al. an effect size rather than a direction ('an overall effect of about d = −0.35 across 105 studies'), which also makes the attenuation in dangerous emergencies interpretable as a moderator rather than a hedge. Verify the cell percentages against Darley and Latané (1968, p. 380).  *(effort: small)*

### [MEDIUM · structure] ## Optional diagnostic detail

> Distinct pathways through which groups can suppress evidence, dissent, or action

**Problem.** The diagnostic table sits in a collapsed callout placed after 'Take it forward', i.e. after the chapter has formally closed, and it duplicates the figure almost line for line — the SVG already carries all five pathways, each with a Test and a Safeguard in nearly the same wording. The one thing the table adds that the figure does not is the Stasser and Titus citation. So the chapter hides its most useful content behind a fold and pays for it twice.

**Edit.** Cut the duplicated table. Keep the figure in the body as the diagnostic reference, and relocate the Stasser and Titus sentence into the new hidden-profiles body section. If a text version is wanted for accessibility or for epub, keep the table but move it up into the 'Groupthink' section, uncollapsed, and trim the figure caption to avoid restating it. Do not leave a post-conclusion appendix carrying material the learning goals promise.  *(effort: small)*

### [MEDIUM · structure] ## Keeping the decision accountable

> Expertise can guide judgment, but an instruction does not transfer moral accountability

**Problem.** This is a two-sentence section under a level-2 heading, half of which is a forward pointer to chapter 30. It reads as the residue of a removed section (the orphan anchors #two-links-outward and #authority-evidence-boundary immediately after it point the same way). A heading that promises 'Keeping the decision accountable' and delivers one claim plus a cross-link breaks the reading rhythm right before the Practice Lab.

**Edit.** Either fold the accountability sentence into the end of the bystander section and move the chapter-30 pointer into 'Take it forward', deleting the heading; or develop the section to earn it — the strongest available content is the boundary the chapter keeps implying but never states, namely that an instruction from a legitimate authority reallocates felt responsibility without reallocating actual accountability, which is why escalation routes have to exist outside the chain of command. Remove the two dead anchors if nothing links to them.  *(effort: small)*

### [MEDIUM · visual] ## Bystanders and pluralistic ignorance

> notice the event, interpret it as an emergency, accept responsibility

**Problem.** The Latané and Darley five-step sequence is the chapter's best organizing device and is buried mid-paragraph as a comma list. The chapter's whole argument — that a group can see a concern and still not act — is exactly this sequence, yet it is never mapped onto the safety email that frames the chapter. The body also carries only one visual across roughly 1,500 words.

**Edit.** Pull the sequence into a five-row table with three columns: Step (notice / interpret / accept responsibility / know how to help / act); What failure looks like in an emergency; What failure looks like in the safety email (nobody opens the thread / 'probably fine' / seven recipients, no owner / nobody knows who can authorize an inspection / the thread scrolls off the screen). The parallel is the chapter's thesis rendered in one glance, and it gives the long bystander section its only visual anchor.  *(effort: medium)*

### [LOW · consistency] ## References cited in this chapter

> Darley, J. M., & Latané, B. (1968). Bystander intervention in emergencies

**Problem.** Two entries break alphabetical order: Darley and Latané (1968) is placed after Janis (1982), and Perry et al. (2020) is placed after Prentice and Miller (1993). Every other entry is alphabetized. The same slip occurs in chapter 29, so it is likely a repeated editing artifact rather than an intentional grouping.

**Edit.** Move the Darley and Latané entry to sit after Burger (2009), and move Perry et al. before Prentice and Miller. Also consider adding DOIs to the Burger, Edmondson, Darley and Latané, Milgram, and Prentice and Miller entries, which currently lack them while most others in the list have them.  *(effort: small)*

---

## `chapters/29-culture-and-identity-the-same-action-is-not-the-same-act.qmd`  (17 findings)

### [HIGH · engagement] ## Lens 4: What does the action mean in this relationship or institution?

> introducing a fine for late pickup increased lateness; a plausible interpretation

**Problem.** The day-care study is retold here in a weaker form than chapter 25 already tells it. Chapter 25 includes the detail that makes the study famous — 'the effect did not simply disappear when the fine was removed' — and this chapter drops it, keeps no numbers, and does not cross-reference the earlier treatment. The surprise is spent, and the reader who remembers chapter 25 gets a diminished repeat.

**Edit.** Cross-link to chapter 20 or 25 and add the one fact that carries the chapter's own thesis: late pickups roughly doubled after the fine was introduced and stayed elevated after it was withdrawn. Then state the implication this chapter is uniquely positioned to make and currently does not: a price can be removed, but the meaning it installed cannot. That asymmetry — reversible policy, irreversible reinterpretation — is the sharpest 'so what' available in the section, and it converts the example from a curiosity into a design warning.  *(effort: small)*

### [HIGH · engagement] ## Research Lens: testing an honor mechanism

> Randomly assigned insult and control conditions produced a larger difference in mean cortisol

**Problem.** The Research Lens never says what the insult was. 'Randomly assigned insult and control conditions' is the most abstract possible description of one of the most vivid procedures in social psychology, and the reader cannot evaluate the manipulation without it. The chapter also omits the behavioral results entirely, so the section rests on a hormone measure alone.

**Edit.** Add one procedural sentence: a confederate bumped the participant in a narrow corridor and called him an obscenity, with the control participants passing unbumped. Then add the behavioral corroboration in a clause — insulted southern participants were rated as more visibly angry, shook hands more firmly, and yielded later in a subsequent corridor game of chicken — which converts a single physiological measure into converging evidence and makes the design panel in the figure worth reading. Verify the details against Cohen et al. (1996, Studies 1–3).  *(effort: small)*

### [HIGH · insight] ### A three-object prediction

> Categorization depends on what kind of similarity the current setting has trained us

**Problem.** The chapter asks the reader to commit to an answer, then never tells them what anyone else answered. No source is given for the triad task and no result is reported — not a percentage, not a direction, not a sample. An interactive prompt with no payoff trains readers to skip the next one, and it leaves the chapter open to the charge that the claim is folklore.

**Edit.** Cite the paradigm and give a number. Ji, Zhang, and Nisbett (2004, JPSP) and the earlier Chiu (1972) triad work report that participants from Chinese-speaking backgrounds chose relational pairings (monkey–banana) substantially more often than American participants, who favored taxonomic pairings. State the actual proportions from whichever source is used, then keep the existing and excellent caution — ask for the reason before interpreting the choice — and add the honest limit: these are group tendencies with heavy overlap, and a single person's pairing diagnoses nothing. Add the reference to the list.  *(effort: medium)*

### [HIGH · insight] ## Lens 4: What does the action mean in this relationship or institution?

> Giving someone €50 is physically and arithmetically the same transfer across settings.

**Problem.** The nine meanings of €50 are the best device in the chapter and the section stops at enumeration. The reader is shown that meaning varies but is given nothing that would let them predict which meaning applies. The operative question — what actually fixes the interpretation — is left implicit, and Zelizer's earmarking is presented without the connection to the book's own mental-accounting chapter.

**Edit.** Follow the list with the variables that determine the category: who gives it relative to who receives it, whether the transfer is public or private, whether it was asked for, whether it can be refused without cost, and whether it is repeated or one-off. Run one case through them — the same €50 handed to an inspector is a bribe if unsolicited, private, and unrefusable; the same amount invoiced and receipted is a fee. Then link explicitly to Mental Accounting: Money Is Fungible, Minds Label It (chapter 20), which treats the same labeling from inside a single head while Zelizer treats it as a social fact.  *(effort: medium)*

### [MEDIUM · accuracy] ::: {.callout-tip} Application: make difficulty identity-safe

> Brief belonging interventions illustrate how interpretations of adversity can affect persistence

**Problem.** Walton and Cohen (2011) is cited without any sample or scale information, in a literature where scale-up has materially changed the picture. The original study randomized 92 first-year students at one selective university, with the three-year GPA effect concentrated among Black students. Later multi-site replications found smaller and highly heterogeneous effects that depend on institutional context. The chapter's own standard elsewhere — naming samples, distinguishing what a study showed from what people infer — is not applied here.

**Edit.** Add the sample and the boundary in one sentence: 'In a randomized study of 92 first-year students at one selective university, a brief intervention reframing early adversity as common and temporary was followed by higher grade-point averages over three years among Black students (Walton & Cohen, 2011); multi-site replications have found smaller, context-dependent effects that depend on whether the institution can deliver on the message.' This strengthens rather than weakens the paragraph, because the chapter's actual claim is that credible support requires 'adequate instruction, fair evaluation, resources, and structural access' — the heterogeneity is evidence for that claim.  *(effort: small)*

### [MEDIUM · accuracy] ## Lens 3: How do hierarchy and face filter information?

> Hofstede's (1980) national dimensions made the concept prominent in management research.

**Problem.** Hofstede is introduced with no provenance, so the hedge that follows ('local organizations may differ substantially') reads as generic caution rather than as a specific reason for doubt. The specific reason is concrete and memorable and is missing: the scores come from attitude surveys of employees of a single multinational corporation, collected around 1967–1973.

**Edit.** Add the provenance where it doubles as a concrete detail: 'The scores come from surveys of IBM employees in more than forty countries between roughly 1967 and 1973 — a workforce matched on employer, industry, and often occupation, which is what made the comparison possible and also what limits it.' That single clause supplies a date, an institution, and the boundary condition at once, and it turns an abstract caveat into something a reader can act on when someone waves a power-distance score at them in a meeting.  *(effort: small)*

### [MEDIUM · clarity] ## Lens 1: Which self or identity enters the decision?

> Reviews of cultural cognition have found broad, context-dependent tendencies toward more analytic

**Problem.** One paragraph carries four citation clusters (Nisbett et al.; Kitayama et al.; Miller; Morris and Peng) and not one description of what any of them actually did. Every verb is hedged and agentless — 'reviews have found', 'experiments have reported', 'attribution studies have found variation' — so the reader accumulates four parentheticals and no image. Three consecutive paragraphs in this section pass without a concrete instance.

**Edit.** Keep the hedging, which is appropriate, but spend the space on one study rendered concretely instead of four named abstractly. The Kitayama framed-line task is ideal: participants see a line inside a square frame, then must reproduce either the line's absolute length or its length relative to a new, differently sized frame; performance on the two versions differed by sample in the predicted direction. Describe that in two sentences, then compress the remaining three citations into a single closing sentence ('Attribution studies report related variation in the weight given to dispositions and situations'). The paragraph gets shorter and far more vivid.  *(effort: medium)*

### [MEDIUM · engagement] ## Opening puzzle: what did the silence mean?

> Nobody speaks, so the manager moves to the next item.

**Problem.** This opening reuses chapter 28's situation almost exactly — a senior person, a group, silence mistaken for agreement, a concern surfacing afterward — without acknowledging the repetition. Chapter 28 closes by explicitly handing off ('The final chapter of this part therefore asks what the same observable action means here'), so the reader arrives primed for a continuation and instead gets what feels like the same scene told again with different anonymous actors.

**Edit.** Make it an explicit continuation rather than a parallel: keep Lena and Sam from chapter 28 and move the scene forward in time — the inspection was assigned, ownership was clear, and the meeting still produced silence, which is precisely the residue chapter 28's safeguards cannot explain. Open with one sentence naming that: 'Chapter 28's remedies assign responsibility. They do not tell you what the silence meant.' The reader then knows immediately why a second chapter on silence exists.  *(effort: small)*

### [MEDIUM · engagement] ## Worked application: redesign the silent meeting

> Later chapters apply the same four lenses to persuasion, communication, negotiation

**Problem.** This paragraph announces what the book will do later and restates what the chapter just did, rather than doing anything. It sits at the end of the worked application, where momentum should be highest, and it dilutes an otherwise strong six-step sequence. The preceding line, 'The design makes consequential information accessible through several channels', is similarly a summary of a summary.

**Edit.** Cut both sentences and end the worked application on its last operational step. If a forward pointer is wanted, make it specific and singular rather than a list of four future topics — one clause naming what the next chapter does with one of these lenses is worth more than an inventory. The chapter already closes properly in 'Take it forward', so this paragraph is doing that job twice.  *(effort: small)*

### [MEDIUM · structure] ## Worked application: redesign the silent meeting

> Agreement, uncertainty, deference, fear, processing time, language difficulty, private-disagreement norm.

**Problem.** The chapter is built on four named lenses — learning goal 1 promises the reader will use them, and the Practice Lab asks for a four-row audit with exactly those rows — but the worked application uses a different six-step scheme that never names a lens. The one place the chapter demonstrates its own method therefore does not model the artifact the Practice Lab requires, and the four lenses are never seen working together on a single case.

**Edit.** Restructure Step 2 as the four-lens pass so the worked example produces the same object the Practice Lab asks for: salient self (is the junior member answering as an individual expert or as a member of a team whose senior has already spoken?); sanction strength (what happens here to someone who contradicts a proposal in public?); hierarchy and face (does raising the problem cost the presenter standing?); local relational meaning (what does speaking in this room communicate about loyalty?). Keep the remaining steps. Then the reader has a template rather than a narrative.  *(effort: medium)*

### [MEDIUM · structure] ## Cross cultures by asking, not assuming

> Zelizer (1994) showed that people earmark money and distinguish household money

**Problem.** This chapter contains zero inline cross-references to other chapters, while chapter 28 carries two and uses them to good effect. Several connections are sitting unmade: Zelizer's earmarking to Mental Accounting (chapter 20); hierarchy filtering information to Authority, Groupthink, and Shared Responsibility (chapter 28), whose pluralistic-ignorance material is the same mechanism seen from a different angle; and the closing claim about audiences interpreting messages to Persuasion (chapter 30), which is named in prose but not linked.

**Edit.** Add three inline links in the book's existing style: from the Zelizer paragraph to chapter 20; from the 'Hierarchy can therefore degrade the information available to the hierarchy itself' sentence back to chapter 28's pluralistic-ignorance section; and from the final paragraph's mention of Part V to chapter 30. Each costs one clause and materially improves navigability, especially for a chapter that is otherwise the most self-contained in the part.  *(effort: small)*

### [MEDIUM · visual] ### Organizations are local cultures

> a firm praises integrity and rewards only sales; a university praises teaching

**Problem.** Four sharp contrasts between espoused values and actual rewards are compressed into one semicolon-chained sentence, where each gets about eight words and none can breathe. This is exactly the content a small table renders better than prose, and the surrounding stretch from the incentive table to the audit table runs roughly 1,000 words with no visual relief at all.

**Edit.** Convert to a three-column table: Espoused value | What actually gets rewarded | Lesson the organization teaches. Rows: integrity / closed deals / 'results excuse method'; teaching / publication count / 'teaching is what you do with leftover time'; safety / punished error reports / 'do not report'; diversity / one communication style / 'belong by sounding like us'. The third column is the addition that makes it worth doing — the prose currently names the mismatch but never states the lesson learned, which is the whole point of the section.  *(effort: small)*

### [MEDIUM · visual] ### Organizations are local cultures

> visible layouts, language, ceremonies, dashboards, routines, and meeting formats

**Problem.** Schein's three levels appear as a bare numbered list of definitions with no worked instance running through them, which is the one thing that makes the model useful. A reader finishes the list able to recite three labels and unable to apply them. This is also the chapter's best candidate for a diagram that would carry genuine explanatory load.

**Edit.** Thread one case vertically through all three levels — the hospital that values safety and punishes error reports is already in the preceding paragraph: artifact (an incident-report form that requires a name and a manager signature), espoused value ('a just culture, we learn from every event'), underlying assumption ('reporting marks you as unreliable'). Then consider a figure: three stacked bands, visible-to-invisible top to bottom, with the same case's three entries on the left and, on the right, the diagnostic question that reaches each level ('what can you photograph?', 'what is on the poster?', 'what happened to the last person who reported?'). Caption it with the claim, not the model name: the level you can see is the level least likely to explain the decision.  *(effort: medium)*

### [MEDIUM · visual] ### A three-object prediction (caption)

> Monkey, panda, and banana: a three-object categorization prompt.

**Problem.** The caption is a label, not a claim. It tells the reader what the picture contains, which they can see, rather than what it shows, which they cannot. The chapter's other captions (the meaning map especially) are sentence-length claims, so this one is also inconsistent with the book's own standard.

**Edit.** Rewrite as the takeaway, phrased so it does not spoil the prompt before the reader answers: 'Two defensible pairings — one by category, one by relationship — and the pairing a person reaches for first reflects what their setting has trained them to treat as similar.' Keep the instruction to answer before reading on in the body text above the figure, where it currently sits.  *(effort: small)*

### [MEDIUM · visual] ## Research Lens: testing an honor mechanism (figure caption)

> Mean cortisol change by assigned insult condition and measured regional upbringing

**Problem.** The caption describes the axes instead of stating the result, so the figure's most striking feature goes unremarked in both caption and body: northern-raised students who were insulted showed no cortisol rise relative to their controls (33 percent versus 39 percent), while southern-raised students nearly doubled (79 percent versus 42 percent). The body's phrase 'a larger difference in mean cortisol change' hides an asymmetry that is the whole point.

**Edit.** Caption it as the claim: 'The same insult raised cortisol sharply among students raised in the South and not at all among students raised in the North — the reaction tracked what the insult was taken to mean, not the insult itself.' Then add the northern null to the body sentence, since a difference between a large effect and a zero effect is a far stronger result than 'a larger difference' conveys. The existing footnote on assigned-versus-measured factors is exactly right and should stay as written.  *(effort: small)*

### [LOW · consistency] ## References cited in this chapter

> Cohen, D., Nisbett, R. E., Bowdle, B. F., & Schwarz, N. (1996)

**Problem.** Cohen et al. (1996) is placed after Gneezy and Rustichini (2000), breaking the otherwise alphabetical list — the same slip that occurs twice in chapter 28. The list is also inconsistent in punctuation: most entries use hyphens for page ranges ('715-753') while Gneezy and Rustichini uses an en dash and italics, and it is the only entry with formatting markup.

**Edit.** Move the Cohen et al. entry to sit after Bowles (2008). Normalize page-range dashes across the list and either italicize all journal titles or none — currently only the Gneezy and Rustichini entry is styled.  *(effort: small)*

### [LOW · consistency] ### A three-object prediction (figure)

> ../figures/culture-triad-monkey-panda-banana.png

**Problem.** This is the only figure in either chapter referenced as a .png with no paired .svg in figures/ — the other three (silence-mechanism-diagnostic, culture-meaning-map, culture-honor-study-redraw) all exist as both. The figure will not scale cleanly in print or at high zoom, and it breaks the project's file convention.

**Edit.** Produce an .svg companion and reference it the way the other figures are referenced, keeping the .png for epub fallback. While regenerating, note that the fig-alt is currently descriptive of the artwork ('an original textbook illustration shows a monkey and a giant panda above a banana') but does not convey the task; extend it to say that the reader is asked to choose which two of the three belong together, so the prompt works for a screen-reader user.  *(effort: small)*

---

## `chapters/30-persuasion-changing-minds-means-updating-models.qmd`  (16 findings)

### [HIGH · engagement] Opening scenario (before Core Idea)

> Imagine that a company plans to replace its familiar project system

**Problem.** The platform proposal is the spine of the entire chapter — it recurs in eight separate sections and gets a full redesign at the end — yet across 3,500 words it never acquires a single number, name, sector, headcount, or date. Compare Ch31's Sara (named) and Ch32's restaurant owner (concrete task). The reader has nothing to hold onto, so every later callback ("For the platform proposal...") re-imports an abstraction instead of a scene.

**Edit.** Give the case three anchors in the opening two paragraphs and reuse them verbatim later: a sector and size ("a 180-person engineering consultancy"), the actual slide number the leaders showed ("an audit found 38% of active project files existed in three or more versions; the slide promised four hours saved per person per month"), and one named-role objection ("a senior engineer asked who would see her check-in timestamps during performance review"). Then in 'The platform proposal, redesigned' the six-week pilot can predeclare a target against that same 38%/four-hour figure, which makes the pilot's decision rule inspectable rather than notional.  *(effort: medium)*

### [HIGH · engagement] Influence cues are signals, not buttons

> reason-giving increased compliance compared with asking without a reason

**Problem.** This paragraph describes three of the most famous experiments in social psychology (Langer, Freedman & Fraser, Cialdini) and reports zero numbers. The hedging is correct, but without rates the boundary condition — the whole point of the paragraph — is invisible. 'The pattern weakened when the request imposed a larger cost' is an abstraction where the actual contrast is startling.

**Edit.** Put Langer's rates in the sentence: with the small request (5 pages) compliance ran about 60% with no reason and roughly 93-94% with either a real reason or the contentless 'because I have to make copies'; with the large request (20 pages) the placebic reason bought nothing (about 24%, the same as no reason) while only the real reason moved it (about 42%). Stated that way, the reader sees a placebic reason work perfectly and then die, which is the finding. Author should verify the exact cell percentages against the 1978 paper before printing.  *(effort: small)*

### [HIGH · insight] Two routes through a message

> the same variable can play different roles

**Problem.** The multiple-roles hypothesis is the most sophisticated idea in the chapter and the one that justifies the chapter's refusal to say 'which route.' It is currently a subordinate clause in the middle of the Petty/Cacioppo/Goldman paragraph, followed by a five-item list delivered as apposition. The reader who most needs it will skim past it.

**Edit.** Give it its own short paragraph with a worked instance on the running case: the CTO's technical expertise can act as a bare cue for an employee with ten minutes ('the CTO signed off, fine'); as genuine evidence for one who reads the workflow analysis and knows the CTO has run three such migrations; as a motivator that makes a skeptic read more closely; as a bias that makes a distrustful employee generate counterarguments rather than fewer; and as a confidence-changer that firms up whatever thoughts the employee already had. One case, five roles, in six sentences — this is the passage readers will quote.  *(effort: medium)*

### [HIGH · visual] Resistance and reactance

> Only people afraid of accountability oppose this system

**Problem.** From the influence-cue table to the end of the chapter runs roughly 1,125 words of prose — 'Diagnose the audience', 'Resistance and reactance', 'Ethical persuasion', 'The platform proposal, redesigned' — with no table, figure, or callout. This is the chapter's entire second half and its ethical payoff, delivered as unbroken paragraphs.

**Edit.** Add two things. First, an `.evidence-and-boundary-conditions` callout after the compliance-experiments paragraph, in the house style used in Chapter 27: title it 'Evidence Boundary: compliance is not belief change', and state that the classic techniques were measured on a single immediate behavior, that effect sizes are modest and moderated by request cost, delay, and relationship, and that none of them was designed to test whether the target's model of the situation changed. Second, convert 'The platform proposal, redesigned' from a First/Second/Third/Fourth/Finally paragraph into a two-column table (Original message → Redesigned move) with five rows matching @tbl-25-model-update's stages, so the chapter's climax is skimmable and visibly closes the loop on the sequence the chapter opened with.  *(effort: medium)*

### [MEDIUM · accuracy] Source, evidence, and stakes

> Two-sided refutational messages can be especially useful for informed or skeptical audiences

**Problem.** The two claims in this sentence trace to different sources. O'Keefe's (1999) meta-analysis established the refutational/non-refutational distinction — two-sided messages that answer the objection outperform one-sided ones, while two-sided messages that raise an objection without answering it perform worse than one-sided. The audience moderator (education, initial opposition) comes from Hovland et al. (1949), not from O'Keefe, whose analysis did not find audience characteristics to be a reliable moderator. As written, the citation pair implies both sources support both claims.

**Edit.** Split it: 'Acknowledging a consequential objection helps only when the message answers it; meta-analytic evidence indicates that two-sided messages which raise an objection without refuting it are *less* persuasive than one-sided messages (O'Keefe, 1999). Early wartime studies found the advantage concentrated among better-educated and initially opposed audiences (Hovland et al., 1949).' The corrected version is also more useful, because the failure mode it names — naming an objection you cannot answer — is a mistake practitioners actually make.  *(effort: small)*

### [MEDIUM · accuracy] Source, evidence, and stakes

> low-credibility information may remain familiar even when its origin is forgotten

**Problem.** This invokes the sleeper effect without its boundary conditions. Kumkale and Albarracín's (2004) meta-analysis found the effect small overall and dependent on a restrictive configuration: a message strong enough to produce initial argument-based change, a discounting cue delivered *after* rather than before the message, and enough processing for the arguments to be encoded. Stated unconditionally, it reads as a general law of memory, which is the kind of overclaim the book elsewhere avoids.

**Edit.** Add the conditions in one clause: '...(Kumkale & Albarracín, 2004), though the meta-analysis found this delayed rebound small and confined to cases where the message was well argued and the credibility discount arrived after it rather than before.' This also strengthens the chapter's practical advice: disclosing a source's interest before the argument is heard is more protective than disclosing it afterward.  *(effort: small)*

### [MEDIUM · accuracy] Resistance and reactance

> Meta-analyses suggest that inoculation can build resistance across domains

**Problem.** A magnitude-free endorsement of a whole literature, and it omits the most decision-relevant result in Banas and Rains (2010): inoculation conferred resistance relative to no-treatment controls but did not reliably outperform plain supportive messages. A practitioner reading this will build an inoculation message where a straightforward supportive one would do the same work.

**Edit.** Report both halves: 'A meta-analysis found a modest resistance advantage over no-treatment controls but no reliable advantage over simply supportive messages (Banas & Rains, 2010), so inoculation earns its extra complexity mainly when a specific misleading argument is genuinely likely to arrive.' Author should check the reported effect magnitude in the paper before quoting a number. This correction also makes the following paragraph's advice ('Test whether the exercise improves later judgment') feel necessary rather than dutiful.  *(effort: small)*

### [MEDIUM · clarity] Resistance and reactance

> An audience may understand the present proposal yet later encounter a misleading argument

**Problem.** One ## section carries five distinct topics — reactance, self-determination theory and autonomy support, inoculation, the state of the correction/backfire literature, and motivational interviewing — with no subheadings and with abrupt paragraph starts (there are orphaned blank-line gaps at the seams, suggesting removed transitions). A reader arriving at the inoculation paragraph has no signal that the subject changed from autonomy to pre-emptive defense.

**Edit.** Add three ### subheads within the section: 'Reactance and autonomy-supportive framing' (covering Brehm and Deci & Ryan), 'Inoculation: preparing for the argument that has not arrived yet' (McGuire, Banas & Rains, the graph-distortion exercise), and 'Correcting a claim the audience already holds' (Wood & Porter, Lewandowsky). Fold the motivational-interviewing paragraph into the first, where it belongs conceptually, with a transition sentence naming what it adds: eliciting the audience's own reasons rather than supplying yours.  *(effort: small)*

### [MEDIUM · clarity] Practice Lab

> one claim-evidence-warrant chain

**Problem.** 'Warrant' in the Toulmin sense is required equipment for the Practice Lab but is never defined in this chapter, and a repo-wide check confirms the phrase 'claim-evidence-warrant' appears nowhere else in the book. A student reaching the lab cannot complete the deliverable.

**Edit.** Either define it where the chapter already discusses evidence-claim fit — after 'Evidence must answer the audience's actual question and match the claim being made', add: 'The link between them is the **warrant**: the assumption that makes this evidence count as support for this claim. Stating it aloud is what lets a skeptic dispute it.' — or replace the Practice Lab phrase with vocabulary the chapter has taught, e.g. 'one pivotal claim with the evidence that tests it and the assumption connecting them.'  *(effort: small)*

### [MEDIUM · consistency] Chapter epigraph

> Rhetoric may be defined as the faculty of observing in any given case

**Problem.** The epigraph quotes W. Rhys Roberts's translation (linked to the MIT Classics text) but the reference list supplies only Kennedy's 2007 translation, which renders 1355b quite differently ('an ability, in each [particular] case, to see the available means of persuasion'). A reader following the citation will not find the quoted words.

**Edit.** Either change the epigraph wording to Kennedy's, since that is the edition listed, or add a Roberts entry to the reference list — Aristotle. (1954). *Rhetoric* (W. R. Roberts, Trans.). Modern Library — and attribute the epigraph to it. The second option is cleaner since the hyperlink already points at the Roberts text.  *(effort: small)*

### [MEDIUM · engagement] Two routes through a message

> demonstrated this with a study about comprehensive exams

**Problem.** The single empirical demonstration of the chapter's central theoretical claim is compressed into eleven words with no design, no manipulation, and no result pattern. A reader cannot tell what was varied or what the crossover looked like, so the ELM stays a taxonomy rather than a finding.

**Edit.** Name the lever, which is unusually elegant and takes one sentence: students heard a proposal for senior comprehensive exams that would take effect either the following year (high personal relevance) or in ten years (low). Under high relevance, argument quality drove attitudes and the source's expertise barely mattered; under low relevance the pattern reversed. Add the crossover in one clause — 'the same expert source that was decisive for students facing the policy was close to irrelevant for students who would never face it' — so the surprise lands instead of being asserted.  *(effort: small)*

### [MEDIUM · insight] The platform proposal, redesigned

> First, it begins in shared reality: teams are losing time to duplicate files

**Problem.** This is the chapter's payoff and it stops one step short. Everything listed is something the leaders *say*; nothing listed is something the leaders *gave up*. The chapter's own thesis — 'Listening may reveal a defect in the proposal rather than in its presentation' — is never cashed out, so the redesign reads as better packaging of the same proposal.

**Edit.** Add one sentence naming a concession the diagnosis forced: 'Two of these were not presentation choices. The written rule that individual activity logs are not visible to line managers, and the two hours of training per person, were absent from the original plan; the objections put them there, at a cost the leaders had to accept.' That single sentence converts the section from a communication recipe into the chapter's real claim — that persuasion sometimes changes the persuader — and it makes 'Resistance is not treated as a defect; it helps specify the test' land as demonstrated rather than asserted.  *(effort: medium)*

### [MEDIUM · insight] '## From information transfer to model updating' (line 34) or '## Resistance and reactance' (line 153)

> Persuasion begins by finding the question that stands between the audience

**Problem.** Chapter 30's thesis is that persuasion is model updating rather than argument volume. The strongest published test of that thesis since the chapter's existing sources is absent: Costello, Pennycook & Rand (2024, Science) found that personalized dialogues with an LLM produced durable reductions in conspiracy belief — roughly a 20% drop that persisted at two months — precisely because the machine could address each person's specific evidence rather than repeat a generic case. That is the chapter's own argument, demonstrated. Omitting it leaves the chapter's central claim supported only by mechanism and older studies, and leaves the book's persuasion material reading as pre-2023.

**Edit.** Add ~400 words as a subsection or research note after '## From information transfer to model updating'. Report the design, the effect size, the persistence window, and — in the book's own idiom — the boundary conditions: it worked on factual beliefs with checkable referents, tells us little about identity-fused commitments, and the same capability is symmetric in its uses, which is the ethics point '## Ethical persuasion' (line 175) can then pick up. This is a case where the AI angle strengthens a behavioral claim rather than decorating it.  *(effort: small)*

### [MEDIUM · structure] Take it forward

> More efficiency statistics will help only if uncertainty about efficiency

**Problem.** The 'Take it forward' restates the chapter's thesis rather than committing the reader to an action. Ch31's and Ch32's versions both issue an instruction ('When you retell a case, carry that distinction with it'; 'Read your draft from the audience's position'), so this one is also out of step with its siblings.

**Edit.** Convert to a commitment tied to the reader's own situation: 'Take one proposal you are currently arguing for. Write the single question standing between your audience and agreement, and ask one person in that audience whether you got it right. If the answer names a cost your proposal does not address, you have found a defect in the proposal, not in the pitch — revise the proposal before the slides.' Keep the current thesis sentence as the lead-in, then add the instruction.  *(effort: small)*

### [MEDIUM · visual] From information transfer to model updating

> a visible pattern may fit several accounts: steady growth, acceleration

**Problem.** Both figures in this chapter (@fig-model-underdetermination and @fig-persuasion-update) are inserted but never referenced by @fig- and never discussed in the body. The underdetermination figure's caption carries a real datum — 'A new observation of 44 at period 8 favors the plateau' — that the prose never uses, so the most concrete number in the chapter sits where readers skip. @fig-persuasion-update is worse: it appears immediately under a section heading with no introduction, before the paragraph that would motivate it.

**Edit.** In the sentence at line 38, write: 'Three curves fit the same five observations equally well (@fig-model-underdetermination); only a further observation separates them, and a reading of 44 at period 8 would favor the plateau while ruling little else out.' For @fig-persuasion-update, move it below the paragraph beginning 'A detailed workflow comparison...' and reference it where the text distinguishes belief revision from intention from action, since that three-way split is exactly what the figure shows and the body never states as a list.  *(effort: small)*

### [LOW · clarity] Two routes through a message

> shorthand for the high- and low-elaboration ends of a continuum

**Problem.** 'Elaboration' is used as a technical term three times before it is defined, and its definition arrives only implicitly in the next clause ('devote more thought to issue-relevant information'). Two paragraphs later it is used as a bare noun ('Extensive elaboration can be selective or identity-defensive') before the reader has a stable handle on it.

**Edit.** Define it once, up front, in the sentence that introduces the model: '**Elaboration** is the amount of issue-relevant thinking a person does about a message. The elaboration likelihood model... uses *central* and *peripheral* routes as shorthand for the high- and low-elaboration ends of that continuum.' One added clause fixes it.  *(effort: small)*

---

## `chapters/31-why-stories-move-minds.qmd`  (14 findings)

### [HIGH · accuracy] The power—and danger—of one

> The story creates attention and care; the statistic creates proportion.

**Problem.** The prescription contradicts the study cited four lines above it. Small, Loewenstein and Slovic (2007) found that pairing an identifiable victim with statistical information *reduced* donations relative to the identifiable victim alone, and that prompting deliberative thought lowered giving to the identifiable victim without raising giving to statistical victims. The chapter presents 'story plus statistic' as the clean resolution when the cited evidence says the combination can suppress the very response the story produced.

**Edit.** State the awkward result — it is the most memorable thing in the chapter and the book's voice is well suited to it: 'The combination is harder than it sounds. In the same experiments, adding statistical information to an identifiable victim reduced giving rather than adding proportion to it, and prompting deliberative thought lowered giving to the identified person without raising giving to the statistical many (Small et al., 2007).' Then keep the ethical point but change its status from recipe to open problem: the goal is proportionate response, and simply bolting a denominator onto a face is not a demonstrated way to get it. Author should verify the condition means before quoting figures.  *(effort: medium)*

### [HIGH · consistency] Four mechanisms of narrative persuasion

> Simulation and causal understanding | What mechanism links choice to consequence?

**Problem.** @tbl-26-1 lists the four mechanism families in the order Attention, Simulation, Identity, Emotion — but the four numbered sections that immediately follow run Attention (1), Identity (2), Emotion (3), Simulation (4). The table is the reader's map and it disagrees with the terrain two lines later. A reader who uses the table to navigate will look for simulation in section 2 and find identification.

**Edit.** Reorder the table rows to match the section sequence: Attention and curiosity → Identity and self-reference → Emotion, memory, and reduced resistance → Simulation and causal understanding. Reordering the table is safer than renumbering the sections, because the current section order has a defensible escalation (notice → enter → feel → rehearse) and 'Simulation and causal understanding' rightly sits last, adjacent to 'Causal stories and causal evidence' and the identifiable-victim section.  *(effort: small)*

### [HIGH · engagement] Opening scenario (before Core Idea)

> Sara, a fictional team leader, reads an anonymous comment

**Problem.** A chapter titled 'Why Stories Move Minds' never tells a story. Sara appears in six fragments spread across six sections (opening, 'Information is not yet narrative', 'Story as model updating', 'Why facts alone can fail', 'Identification', 'Self-reference'), never running longer than three sentences. The chapter therefore argues for narrative in expository form — and Chapter 32, which is about evidence rather than narrative, contains the two properly told stories in this part of the book (Maria, the deadline).

**Edit.** Consolidate the Sara material into one continuous 150-200 word scene immediately after the epigraph, carrying her through the full arc the chapter later names: the comment, the dismissal, the meeting notes where every proposed solution is her own, the silence she waits through at the next meeting, and the delivery risk that surfaces. Then let the later sections quote back single lines from that scene as callbacks rather than re-establishing her each time. The chapter would then demonstrate its own claim, and the 'protagonist, goal, obstacle, stakes, choice, change' checklist in 'What is a story?' could point at the scene the reader just read.  *(effort: medium)*

### [HIGH · visual] 4. Simulation and causal understanding

> Students may readily endorse "report unfavorable results" or "look for shared interests"

**Problem.** Roughly 1,200 words run from the mechanism table to the Research Lens callout, covering all four mechanisms, with no table, figure, callout, or list. This is the analytical core of the chapter and it is delivered as uninterrupted prose. The chapter as a whole has only one figure, one table, and one callout.

**Edit.** Add a diagram carrying real explanatory load rather than decoration: a single horizontal spine showing one story moving left to right through four labeled gates — Attend, Enter, Feel, Rehearse — with two outputs drawn from each gate, an upward arrow to what it buys (a reason to keep reading; access to the character's constraints; a sense of what is at stake; a rehearsed decision procedure) and a downward arrow to its characteristic failure (manufactured suspense; erasure of other affected parties; feeling exceeding evidence; coherence mistaken for proof). That is the chapter's argument in one image and it does not currently exist in any of the four figures. Second, add an `.evidence-and-boundary-conditions` callout after the Transportation subsection on what the transportation literature does and does not license — measured transportation and story-consistent belief are usually assessed together, durability beyond short follow-ups is sparsely tested, and 'reduced counterarguing' is more often inferred than directly measured.  *(effort: large)*

### [MEDIUM · accuracy] Transportation

> meta-analytic work by van Laer and colleagues, supports its importance

**Problem.** This is the flattest sentence in the chapter and the only substantive claim in these three chapters made with author names but no year and no magnitude. 'Supports its importance' tells the reader nothing about how large, how consistent, or under what conditions — which is precisely the standard the book applies everywhere else.

**Edit.** Give the magnitude and at least one moderator from van Laer et al. (2014) — e.g. that transportation was reliably associated with story-consistent affective and cognitive responses, with an average correlation of modest size, and that identifiable characters and a clear plot were among the antecedents that raised it. Add the year citation. If the author prefers not to quote an effect size here, then at minimum state what the meta-analysis could and could not settle: it aggregates associations between measured transportation and story-consistent responses, so it establishes the link more firmly than it establishes the causal direction.  *(effort: small)*

### [MEDIUM · clarity] Story as model updating

> The five-part route in @fig-story-update turns this change of explanation into a writing template.

**Problem.** The body names a five-part template and then never lists the five parts, so a reader must decode them from the SVG (or from the caption, which lists them in running prose). This is the only place in the chapter where the reader is sent to a figure to obtain information the text withholds — and print readers of a greyscale figure are worst served.

**Edit.** Name the five in the sentence: 'current story → trouble → candidate model → evidence → possible action.' Then the following paragraph's three questions map visibly onto parts 1, 2, and 4, and the figure becomes a reinforcement rather than a dependency. Also cross-reference @tbl-25-model-update in Chapter 30, since these are the same five stages under different names — saying so explicitly is a one-line insight that ties the two chapters together.  *(effort: small)*

### [MEDIUM · consistency] What is a story?

> Practitioner writers such as Lisa Cron and Will Storr offer useful craft questions

**Problem.** Two authors are named in the body but appear nowhere in 'References cited in this chapter', and a repo-wide grep confirms they appear nowhere else in the book. Everywhere else these three chapters name a source, a citation follows. A reader who wants the craft questions has no way to find them.

**Edit.** Either add reference entries — Cron, L. (2012). *Wired for story*. Ten Speed Press; Storr, W. (2019). *The science of storytelling*. William Collins — with parenthetical citations in the sentence, or cut the names and keep the three questions as the book's own, since the questions stand on their own. Adding the entries is preferable: it signals to students where the craft literature sits relative to the research literature, which is a distinction this chapter is otherwise careful about.  *(effort: small)*

### [MEDIUM · engagement] Transportation

> A political film can make a misleading causal story feel true.

**Problem.** Three consecutive risk sentences ('A political film...', 'A corporate change story...') are hypotheticals with no instance, in a section whose own cited source contains a perfectly concrete and uncontroversial one. The reader is asked to accept that transportation can install beliefs without ever being shown it happening.

**Edit.** Describe Green and Brock's actual stimulus, which is citable, non-partisan, and vivid: readers given a narrative in which a young girl is killed in a shopping mall by a psychiatric patient subsequently held more story-consistent beliefs — rating malls as less safe and endorsing greater restriction of psychiatric patients' freedoms — and more transported readers shifted more. That is the mechanism, demonstrated, in two sentences, and it makes the ethical questions that follow ('What world am I inviting the audience to enter?') land on a real case rather than a category. Keep the hypotheticals afterward as extensions.  *(effort: small)*

### [MEDIUM · engagement] 3. Emotion, memory, and reduced resistance

> a small supplier that invested in new equipment, expected a contract, lost revenue

**Problem.** This is the best concrete passage in the chapter and it is compressed into a single trailing clause of five participles. The chapter is arguing at that exact moment that meaning becomes visible when we see who was affected — and then demonstrates the point in a subordinate clause, at speed, with no numbers.

**Edit.** Let it breathe for two sentences and give it one figure: 'The project was delayed by six months' is information. A supplier with eleven employees had bought a €40,000 press against the expected contract; when the order slipped, two shifts went, and the next time an innovation partnership was offered the firm declined. Same delay, different thing understood.' The rhythm break — long sentence, then four words — is also the kind of varied cadence the surrounding prose lacks.  *(effort: small)*

### [MEDIUM · insight] The power—and danger—of one

> A rare disease with a compelling story may attract disproportionate funding.

**Problem.** This section is the natural junction with three other chapters and connects to none of them. Availability and affect (Ch9), samples and base rates (Ch15), and the identifiable case as a frequency signal all bear directly on why one face outruns a denominator, and the book has already built that machinery.

**Edit.** Add one bridging sentence that names the mechanism rather than restating the phenomenon: 'This is the availability mechanism of Chapter 9 operating through a character: the retrievable case supplies the frequency estimate that the base rate should have supplied (Chapter 15). The story does not argue against the statistic; it arrives first and answers the question the statistic was going to answer.' That reframing — the story is not competing with the number, it is pre-empting it — is the memorable formulation this section is currently one step short of.  *(effort: small)*

### [MEDIUM · insight] What is a story?

> Fisher (1984, 1987) likewise distinguished a story's coherence from its fit

**Problem.** Both Bruner's and Fisher's distinctions are described accurately but their technical terms are withheld, so the reader gets the ideas without a handle to carry them. Fisher's pair in particular — narrative probability (does it hang together) versus narrative fidelity (does it ring true against what I already believe and value) — is exactly the diagnostic the chapter needs later when it warns that coherence is not proof.

**Edit.** Name them: Bruner's narrative versus paradigmatic modes of thought; Fisher's narrative probability versus narrative fidelity. Then reuse 'fidelity' in the Transportation risk paragraph — 'a misleading story can score high on fidelity precisely because it matches what the audience already believes, which is why coherence and familiarity together can feel like corroboration' — which converts a named term into working equipment rather than a label.  *(effort: small)*

### [MEDIUM · structure] Four mechanisms of narrative persuasion

> ## Four mechanisms of narrative persuasion

**Problem.** The four numbered mechanisms are ## headings, i.e. siblings of the ## heading that introduces them, so the document outline shows five peer sections where the structure is one parent and four children. In the rendered sidebar and in the PDF table of contents, 'Four mechanisms of narrative persuasion' appears as a same-level section containing only a paragraph and a table.

**Edit.** Demote the four to ### ('### 1. Attention and curiosity' ... '### 4. Simulation and causal understanding') and their existing subheads to #### (Transportation, Identification, Self-reference, Reduced resistance, Causal stories and causal evidence). This is a mechanical fix that makes the sidebar mirror the table and costs nothing in prose.  *(effort: small)*

### [MEDIUM · visual] Story as model updating

> A narrative-design template begins with the audience's current model

**Problem.** The caption describes what the figure contains rather than stating what it shows. Compare Chapter 30's @fig-model-underdetermination caption, which does state a takeaway ('A new observation of 44 at period 8 favors the plateau'). A caption that is a contents list gives a skimming reader nothing.

**Edit.** Rewrite as a claim: 'A story changes a model only if the trouble it introduces is one the audience's current explanation cannot absorb; the evidence and action stages are what stop the turning point from standing in for a test.' Same for Ch32's braid figure. Rule of thumb worth applying across all four figures in these chapters: if the caption would still be true of a different diagram on the same topic, it is a label.  *(effort: small)*

### [LOW · consistency] References cited in this chapter

> van Laer, T., de Ruyter, K., Visconti, L. M., & Wetzels, M. (2014)

**Problem.** The reference list is alphabetized except at the end: Small et al. (2007) is placed after van Laer et al. (2014). Chapters 30 and 32 are correctly alphabetized throughout, so this is a local slip rather than a house style.

**Edit.** Move the Small et al. (2007) block up to follow Hasson et al. (2004) and precede Stephens et al. (2010). While there, note that the same Small et al. entry appears in Chapter 32's list with an en dash in the page range (143–153) versus a hyphen here (143-153); several other entries in both chapters mix hyphens and en dashes in page ranges and issue numbers. Worth a single pass across the three files.  *(effort: small)*

---

## `chapters/32-building-an-evidence-aligned-message.qmd`  (14 findings)

### [HIGH · clarity] The STORY framework

> **R**—report only verified pilot behavior, comparisons, uncertainty, and limits

**Problem.** The worked STORY example changes register halfway through. S, T, and O are written as message content the owner would hear; R and Y switch to instructions addressed to the writer ('report only verified...'), so the example evaporates at exactly the two letters the chapter spends the most effort teaching. The trailing sentence 'any traction number must be real, sourced, and appropriate to the claim' reads like a warning left behind after an earlier example containing a number was removed.

**Edit.** Write R and Y as actual sentences of the pitch, with a placeholder clearly marked as illustrative: 'R — in a 6-restaurant, 8-week trial, forecast error was lower than the owners' own estimates on 5 of 6 sites; on the sixth, with irregular event bookings, it was worse. We have no data yet on whether lower error translates into lower waste. Y — we are inviting 20 restaurants with at least 12 months of point-of-sale history to an 8-week trial; you keep every override, we publish the comparison including sites where the tool loses, and you can stop at any week.' Mark the trial figures as illustrative in a following sentence, then keep the existing warning — it becomes meaningful once there is a number for it to govern.  *(effort: medium)*

### [HIGH · engagement] Fluency: power and danger

> show waste in units they can reconstruct—portions or ingredient costs over a stated period

**Problem.** A chapter whose thesis is that messages must carry inspectable evidence contains no worked number anywhere in 2,750 words. It repeatedly instructs the reader to supply denominators, comparisons, and magnitudes, and never once models what that looks like. This is the chapter's central credibility gap: it teaches a discipline it does not practice on its own running example.

**Edit.** Add a four-line worked block right here, in the owner's units: '42 portions of the braised pork prepared on a Tuesday, 31 sold, 11 discarded at €4.20 ingredient cost — €46. Across 14 Tuesdays, roughly €640, or about 3% of food spend. The number the owner actually needs, though, is not the waste; it is the difference between waste under her current guess and waste under the tool's recommendation on the same days.' That last sentence is the chapter's whole argument about comparisons, delivered in one concrete line, and it sets up the pilot design in 'The story-evidence braid'.  *(effort: medium)*

### [HIGH · insight] Worked example: structured hiring

> The example makes the reason for structure understandable; Chapter 41 examines

**Problem.** The chapter's title promises an evidence-aligned message and its worked examples deliver only the story half. Maria's story is well told and its structure is analyzed, but the Reasons row — the row @tbl-27-claim-evidence exists to fill — is outsourced to another chapter. The reader finishes 'Worked transformations' having seen narrative craft demonstrated twice and the braid demonstrated zero times.

**Edit.** Append a short Reasons block to the Maria example, using the chapter's own taxonomy: pivotal claim type = causal impact; evidence = meta-analytic and comparative work on structured versus unstructured interview validity; comparison = same roles, same firm, structured versus unstructured; uncertainty = validity estimates have been revised downward as corrections for range restriction and measurement error were reassessed, so the ordering is better established than the magnitude; what it does not establish = that this manager's judgment improves, or that structure survives contact with hiring managers who dislike it. Then add the self-audit sentence: 'Maria's story is evidence of nothing. It is a fictional case asserting a causal mechanism — the failure mode this chapter names as anecdote as denominator. Its job is to make the mechanism imaginable so the comparative evidence has somewhere to land.' That turning of the chapter's own audit on its own example is the most memorable move available here.  *(effort: medium)*

### [HIGH · structure] References cited in this chapter

> Berger, J., & Heath, C. (2007). Where consumers diverge from others

**Problem.** Berger and Heath (2007) is listed under 'References cited in this chapter' but is cited nowhere in the body. I checked every parenthetical in the file: the sharing paragraph cites Berger & Milkman (2012), Falk et al. (2013), and Baek et al. (2017) only. The reverse direction is clean — every in-body citation has an entry — so this is the single orphan.

**Edit.** Either delete the entry, or cite it where it would genuinely earn its place: the sharing paragraph currently lists identity signaling as a motive for transmission ('People may pass content on because it expresses identity') without a source, and Berger & Heath (2007) is the identity-signaling citation. Adding it to that sentence is the better fix, since it supplies the one motive in the list that is otherwise unsupported.  *(effort: small)*

### [HIGH · structure] Ethics and common failure modes

> The ethical audit below is useful after drafting

**Problem.** 'The audit below' points at @tbl-27-2, which does not appear below — it appears two sections later, after 'Worked transformations', parked under the unrelated heading 'Edit for clarity without confusing fluency with truth'. A reader who takes the sentence literally scrolls into the worked examples and finds no audit. The same heading also holds @tbl-27-1, which belongs with the story/example/anecdote definitions, not with editing for fluency.

**Edit.** Move @tbl-27-2 (the ethical story audit) up into '### Ethical storytelling', directly after the sentence that promises it, and add an explicit cross-reference (@tbl-27-2) so the pointer survives future reordering. Leave 'Edit for clarity' to hold only the editing material, which is coherent on its own.  *(effort: small)*

### [HIGH · visual] Adapt the message without changing its discipline

> A message built for the restaurant owner cannot simply be relabeled for a student

**Problem.** Roughly 1,195 words run from @tbl-27-claim-evidence to @tbl-27-1 with only one bullet list for relief, covering fluency, the braid, adaptation across six domains, ethics, and two long worked examples. The six-domain paragraph in particular compresses teaching, leadership, health, policy, entrepreneurship, and negotiation into six clauses of a single sentence-stream — a list masquerading as prose.

**Edit.** Convert that paragraph into a five- or six-row table with columns: Domain | The stakeholder's consequential decision | Pivotal claim type (from @tbl-27-claim-evidence) | Characteristic failure. Teaching: does this concept apply to the case in front of me / mechanism / the case becomes the lesson instead of creating the need for one. Leadership: should I commit to this change / feasibility and adoption / the invented burning platform. Health and policy: should I take this action, for this population / causal impact and distribution / one patient standing in for a prevalence. Entrepreneurship: is this worth my money or time / need and economics / the founder as protagonist. Negotiation: can I accept this term / need and mechanism / one side's account presented as the situation. That table does explanatory work the paragraph cannot, and it explicitly links back to the claim-evidence table, which the body otherwise references only in the Practice Lab.  *(effort: medium)*

### [MEDIUM · accuracy] Edit for clarity without confusing fluency with truth

> its average persuasive advantage is small and context-dependent

**Problem.** Correct but unquantified, in a chapter about matching claims to inspectable evidence. Sopory and Dillard (2002) report an average effect around r = .07, a number that is both memorable and rhetorically useful to this author, since it is the sort of small-but-real magnitude that supports the book's anti-hype stance better than the adjective 'small' does.

**Edit.** Give the number and one moderator: 'across studies the average advantage was about r = .07 — real, but far smaller than the craft literature implies — and larger for a single extended metaphor placed early than for metaphors scattered through a message (Sopory & Dillard, 2002).' The same treatment would help the fluency paragraph two sections earlier, where Hasher et al. (1977) and Fazio et al. (2015) are cited without any indication of how much repetition shifts perceived truth.  *(effort: small)*

### [MEDIUM · clarity] Fluency: power and danger

> so ease of reading must not become the reason to believe it

**Problem.** A 90-word ## section sitting between two substantial ones, whose heading promises a duality ('power and danger') that two short paragraphs cannot deliver, and whose point is then made again in 'Edit for clarity' ('These are editing choices, not reasons to believe the claim'). The same idea occupies two separate sections at opposite ends of the chapter.

**Edit.** Fold this section's first paragraph into 'Edit for clarity without confusing fluency with truth', which already carries the same argument and the Chapter 13 relationship, and move its second paragraph (the restaurant waste units) into the worked-number block recommended above. That removes a heading, removes the duplication, and lets the reader meet the fluency caution once, at the point of drafting, where it is actionable.  *(effort: small)*

### [MEDIUM · clarity] Design the change

> ### Hidden resistance and protected identity

**Problem.** The heading names two things and the paragraph delivers one. Hidden resistance is covered (accuracy doubts, record quality, staff treating recommendations as orders); protected identity is not addressed at all — the owner's professional identity as someone who knows her own trade is handled in the previous subsection, 'Begin with the audience's current story'. A reader looking for the identity material under the heading that promises it finds nothing.

**Edit.** Either retitle to '### Find the hidden objection', or add the missing content in two sentences, which is the more valuable option since the identity threat is the sharpest thing in this scenario: 'The deepest objection may not be about accuracy at all. A forecasting tool tells an owner that a judgment she has made well for fifteen years can be made better by software, and a pitch that treats that judgment as the problem to be solved will lose regardless of its error rates. The override rule matters less as a feature than as a statement about whose call it remains.'  *(effort: small)*

### [MEDIUM · consistency] Edit for clarity without confusing fluency with truth

> Sara resists anonymous feedback, sees that her competence has become a bottleneck

**Problem.** The Sara row of @tbl-27-1 does not match the Sara of Chapter 31. There, Sara does not resist anonymous feedback — she reads an anonymous comment and initially dismisses it as unfair; her change is not 'creates a habit of honesty' but a specific behavioral change, waiting for colleagues to describe a problem before offering an answer. Readers who follow the callback will find a different character.

**Edit.** Rewrite the cell to match Chapter 31 exactly: 'Sara dismisses an anonymous comment as unfair, rereads a month of meeting notes and finds every proposed solution was her own, then waits before answering at the next meeting — and hears a delivery risk that was not on the dashboard.' This also improves the row, because it contains an actual consequence (the unreported risk surfacing) rather than an abstraction ('a habit of honesty').  *(effort: small)*

### [MEDIUM · engagement] Opening scenario (before Core Idea)

> Imagine rebuilding the pitch around that decision.

**Problem.** The opening promises a rebuilt pitch and the chapter never shows one. Chapter 30 makes exactly this promise and keeps it in 'The platform proposal, redesigned'; Chapter 32 leaves its own opening unresolved, so the three slides that failed are never replaced by three slides that work. The restaurant thread appears in six places but always as commentary on a pitch the reader never sees.

**Edit.** Add a short 'The pitch, rebuilt' subsection near the end of 'The story-evidence braid' showing the first three slides in outline — Slide 1: the owner's Tuesday, 11 portions discarded, the guess she is making at 4pm; Slide 2: what her booking count misses and what her own sales history already contains; Slide 3: the trial, its comparison, its stopping rule, and what happens to her data if she stops. Roughly 120 words, and it closes the loop the first paragraph opened.  *(effort: medium)*

### [MEDIUM · structure] Edit for clarity without confusing fluency with truth

> | Information | States facts, events, features, dates, or numbers.

**Problem.** @tbl-27-1 restates distinctions Chapter 31 already makes in prose in 'What is a story?' (example versus anecdote versus story), and it lands under a heading about editing for fluency where nothing in the surrounding paragraphs refers to it. Duplicate content in the wrong place: the table is genuinely good, and it is the better presentation of the distinction, but it is 4,000 words from the discussion it serves.

**Edit.** Move @tbl-27-1 to Chapter 31's 'What is a story?' section, where it replaces two paragraphs of prose definition with a scannable five-row comparison, and have Chapter 32 cross-reference it once from 'Anecdote as denominator' in Common mistakes. That removes the duplication, gives Chapter 31 badly needed visual relief in its first 400 words, and leaves Chapter 32's editing section focused.  *(effort: medium)*

### [MEDIUM · visual] Build the message with one primary workflow

> An ethical communication framework braids human meaning with base rates

**Problem.** @fig-story-evidence-braid is never referenced by @fig- and never discussed; it sits directly under a section heading before any text has motivated it, and its caption is a description of the metaphor rather than a claim. The section that would naturally discuss it — 'The story-evidence braid' — is four sections later and does not point to it.

**Edit.** Move the figure down to 'The story-evidence braid' where its own name appears, reference it in the sentence 'A useful draft can move from the scene to evidence, explain the proposed mechanism, and then return to the decision (@fig-story-evidence-braid)', and rewrite the caption as a takeaway: 'The scene and the evidence answer different questions — one makes a cost imaginable, the other says how common it is — and a message fails when either strand is asked to do the other's job.'  *(effort: small)*

### [LOW · structure] Learning goals

> use AND–BUT–THEREFORE only as an optional compression test

**Problem.** A learning goal phrased as a defensive ranking of two tools rather than as a capability the reader will acquire, and the subordinated tool then gets one sentence in the body with no worked instance ('For a brief version, try AND–BUT–THEREFORE'). A reader cannot perform the compression test because they have never seen one performed.

**Edit.** Either demonstrate it in one line using the running case — 'Independent restaurants already forecast demand informally, BUT daily preparation is still a guess that costs either waste or lost sales, THEREFORE test whether existing sales history forecasts it better than the guess does' — or drop ABT from the learning goal and leave it as a passing note in the body. The one-line demonstration is preferable: it takes 30 words and it shows the reader that a good STORY draft should survive compression, which is a real diagnostic.  *(effort: small)*

---

## `chapters/33-communication-language-is-not-a-file-transfer.qmd`  (13 findings)

### [HIGH · engagement] ## Communication is coordination and repair

> yet actual email accuracy was only 56%

**Problem.** The chapter's single most striking number is reported without the baseline that makes it striking. The task was a binary judgment (was this sentence sarcastic or serious), so blind guessing produces about 50%. As written, 56% reads as merely "lower than people expected" rather than "barely distinguishable from a coin flip while both parties felt 78-90% sure."

**Edit.** Put the baseline in the sentence: "...actual email accuracy was 56% - in a task where the reader only had to decide 'sarcastic or serious,' so guessing alone would have produced about 50%." The following sentence ("The striking result is the gap") can then be cut, because the number does the work instead of the adjective.  *(effort: small)*

### [HIGH · insight] ## Ask rather than merely imagine

> found that people were often more accurate when they asked others for their perspective

**Problem.** This is the chapter's central practical claim and its most surprising evidence, and "often more accurate" flattens it into a mild comparison. The paper's result is stronger and stranger: across a long series of experiments, instructing people to take another's perspective did not improve accuracy at all, and in several studies made predictions worse; only asking improved them. Stated as a mild preference, the reader has no reason to change a habit.

**Edit.** Give scale and direction: "Across more than two dozen experiments - predicting a spouse's preferences, a stranger's opinions, whether a speaker was lying - instructing people to take the other person's perspective failed to improve accuracy, and sometimes reduced it. Asking improved it." Verify the exact experiment count against the paper before printing a number.  *(effort: small)*

### [MEDIUM · accuracy] Figure caption, #fig-communication-calibration-evidence

> In a task involving 29 dyads, senders and receivers forecast high decoding accuracy

**Problem.** Citation check. The body says "In one study" while the caption attributes the chart to Study 2 with 29 dyads. The widely cited 78% / 56% / 73.1% values are usually reported from the paper's first sarcasm experiment, and the ~90% receiver forecast may come from a different experiment in the same paper. If the three bars are drawn from more than one study, the caption misstates the source and the N.

**Edit.** Re-check Kruger et al. (2005) and make body and caption name the same experiment and sample ("Study 1, 30 pairs" or "Study 2, 29 pairs"). If sender forecast, receiver forecast, and actual accuracy come from different experiments in the paper, either restrict the chart to a single experiment or label each bar's source in the caption. Also name the study number in the body sentence, not only in the caption.  *(effort: small)*

### [MEDIUM · accuracy] ## Mind-reading is a hypothesis

> partners predicted each other’s judgments of self-worth, abilities, and preferences better than chance

**Problem.** Citation check. Eyal & Epley (2010), "How to seem telepathic," is primarily a construal-matching paper: its contribution is that accuracy in predicting another person's impression improved when the two parties' construal levels matched. The sentence describes a general accuracy-versus-expectation comparison in couples as though that were this paper's result, which may belong to a different source.

**Edit.** Verify what Eyal & Epley (2010) actually reports. Either restate it as the construal finding (which is more surprising and more actionable: abstract judgments of another person can be more accurate than detailed ones), or keep the accuracy/overconfidence claim and attach it to the study that established it, citing Eyal & Epley separately for the construal result.  *(effort: medium)*

### [MEDIUM · accuracy] ## Communication is coordination and repair

> Kruger and colleagues (2005) found that people overestimate how well they can communicate

**Problem.** The chapter's strongest empirical claim rests on a 2005 laboratory sarcasm task, with no boundary conditions stated. Readers now communicate in channels with emoji, reactions, voice notes, and video, and the task's difficulty (deliberately ambiguous sentences, unfamiliar partners, plain text) is part of why accuracy was so low. Without this, the finding invites exactly the over-generalization the book warns against elsewhere.

**Edit.** Add an .evidence-and-boundary-conditions callout - a class the book styles but this chapter never uses - with three short lines: what the study did (binary sarcasm judgments, laboratory dyads, plain-text email, 2005); what generalizes (the sender-receiver confidence gap, which recurs in related work); what is unknown (whether emoji, reactions, and voice notes narrow the gap, and by how much). This also supplies the visual relief the first half of the chapter lacks.  *(effort: medium)*

### [MEDIUM · clarity] ## Mind-reading is a hypothesis

> The counterpart is the illusion of understanding: overestimating how much of the context

**Problem.** One paragraph introduces a new named construct, pivots to thin slices and emotion reading with three citations stacked together, and ends with an imperative. Three arguments share a paragraph, and the reader cannot tell which claim each of the three citations supports.

**Edit.** Split into two paragraphs. First: the illusion of understanding, tied back to the manager ("the context in the sender's head does not travel with the words"). Second: the evidence on reading faces and behavior, with each citation attached to its own claim - Ambady & Rosenthal for signal present in thin slices, Barrett et al. for the limits of inferring emotion from facial movement, DePaulo et al. for the weakness of deception cues - closing with "state it, ask, and verify."  *(effort: small)*

### [MEDIUM · clarity] ## Practice Lab

> literal words; intended meaning; at least two plausible interpretations; missing context

**Problem.** Nine deliverables are packed into a single semicolon chain, so a student has to parse the sentence before they can begin, and the lab's two distinct products - the grounding map and the rewritten message - are not visually separated.

**Edit.** Convert to a numbered list of the nine map rows, with the rewrite as a clearly marked second deliverable. Add one worked row using the manager's own email (for example, under "power or relationship cues": "sent by the person who writes my performance review, at 19:40, with no greeting") so the reader sees the level of specificity expected.  *(effort: small)*

### [MEDIUM · engagement] ## Communication is coordination and repair

> If someone asks, “Can you pass the salt?” the literal answer may be “yes”

**Problem.** Four consecutive paragraphs of theory (Shannon/Weaver, Clark, Clark & Brennan, Grice) run without touching the opening email, and the Gricean illustrations are textbook stock examples. The manager's own sentence is a better Gricean object and is sitting unused two paragraphs above.

**Edit.** Keep one stock example and replace the other with the case: "Please come prepared tomorrow" says almost nothing literally; what the reader supplies is the implicature - prepared for what, and prepared because someone is at fault. Close with one line: the manager was relying on an inference they never checked. This threads the case through the theory block instead of parking it.  *(effort: small)*

### [MEDIUM · engagement] ## Begin with a failed email

> After a project deadline slips, a manager writes: “We need to discuss accountability.

**Problem.** The opening has a strong sentence but no people and no stakes. "A manager," "one employee," "another," "a third" are placeholders, and nothing says what the slipped deadline cost anyone. Chapter 34 then reuses the same case with the same anonymity, so the reader meets it twice without ever seeing it once.

**Edit.** Name the people and give one concrete stake, and carry the same names into Chapter 34: the client deliverable was two days late, the manager has already promised the client a recovery plan, and one of the three readers went through last year's restructuring. Two added clauses turn placeholders into a scene and let the two chapters read as one continuing case rather than two similar hypotheticals.  *(effort: small)*

### [MEDIUM · insight] ## Close the loop: utterance to shared-enough meaning

> Persuasion seeks a warranted change in another person's model.

**Problem.** The chapter treats leftover ambiguity purely as a defect awaiting repair. The sharper point is left unmade: ambiguity is often chosen. People keep a sentence vague to preserve options, avoid commitment, protect a relationship, or hold a coalition together - and someone who benefits from not being pinned down will resist grounding. A chapter about testing interpretations that never mentions a partner who does not want them tested stops one step short.

**Edit.** Add three or four sentences closing this section: name strategic ambiguity; give one instance ("we'll look at headcount later" instead of "there will be cuts"); state the diagnostic (when repeated, specific questions keep returning unspecific answers, the vagueness is probably doing a job); and point forward to the negotiation chapters, where deliberate imprecision returns as a tactic rather than a failure.  *(effort: medium)*

### [MEDIUM · structure] ## Learning goals (orphan paragraph immediately after)

> Here, **shared reality** means a perceived commonality with another person's inner state

**Problem.** A dense definitional paragraph with a bare anchor sits between the learning goals and the first section heading, belonging to no section. The term is then never used again in this chapter - it resurfaces only in Chapter 34 - so the reader pays for a definition the chapter never spends, at the exact point where momentum from the opening scene should carry them forward.

**Edit.** Move the paragraph into "Meaning is inferred, tested, and repaired" and tie it to the section's work ("grounding aims at shared reality, not agreement - and shared reality is not truth"), or move the definition forward to Chapter 34, where it is actually used at the validation section. Keep the []{#shared-reality-in-communication} anchor wherever it lands so existing cross-links survive.  *(effort: small)*

### [MEDIUM · visual] ## Mind-reading is a hypothesis

> A related error is the false consensus effect: people overestimate how common

**Problem.** From this heading through the end of "Close the loop" runs roughly 1,050 words with no figure, table, or callout, and it introduces five distinct constructs in quick succession (egocentric projection, false consensus, naive cynicism, illusion of transparency, illusion of understanding). It reads as a bias catalogue, and the whole chapter carries exactly one callout, the Core Idea.

**Edit.** Add a compact four-column table here: Error | What it gets wrong | Tell-tale sentence | Check that corrects it. The four projection quotes already in the text ("I would not be offended by this feedback...") supply the tell-tale column, and naive cynicism and illusion of transparency each need only one line. This converts a list of names into a usable diagnostic and breaks the longest unbroken prose run in the chapter.  *(effort: medium)*

### [LOW · consistency] YAML front matter (aliases)

> 28-communication-is-joint-inference.html

**Problem.** The chapter's former title survives as visible link text elsewhere in the book: chapters/38-designing-better-agreements.qmd (line 163) links here as "Communication Is Joint Inference," which matches neither the current title nor the chapter's running argument about recoverability.

**Edit.** Update the link text in chapters/38-designing-better-agreements.qmd to "Communication: Language Is Not a File Transfer" and grep the book for other inbound links carrying the old title. Keep the alias entry itself so existing URLs resolve.  *(effort: small)*

---

## `chapters/34-connection-and-repair-warm-honesty-makes-truth-usable.qmd`  (15 findings)

### [HIGH · clarity] ### Listen for the layer beneath the words

> Use the prompts that clarify the conversation.

**Problem.** This sentence is an orphan: it names no prompts, points to nothing, and closes the section on a shrug. It also sits under a mismatch - the table above it is first-person self-reflection ("How does it land in me?", "Why did I feel that way?") inside a section titled "Listen for the layer beneath the words," so a listening section is being taught with a self-listening instrument.

**Edit.** Delete the orphan sentence. Then resolve the mismatch: either retitle the section "Locate the layer beneath your own reaction," or add a second column giving the other-directed form of each prompt ("How did that land for you?", "What did you take it to mean?", "What mattered to you there?"), and close with a line saying which column is for the speaker and which for the listener.  *(effort: medium)*

### [HIGH · consistency] ### Apology and repair

> identify the harm, accept appropriate responsibility, and make a credible offer of repair

**Problem.** The chapter names the components of a repair four times with three different lists. The Core Idea says "responsibility and a credible change in what happens next"; learning goal 3 says "acknowledges harm, accepts responsibility, and specifies changed behavior"; this sentence says harm, responsibility, repair; and the Practice Lab demands five ("acknowledgment, responsibility, remorse, repair, and changed behavior"). A student doing the lab cannot tell which list is the chapter's.

**Edit.** Fix one canonical sequence here - acknowledgment of the specific harm, responsibility, remorse, offer of repair, changed behavior - and make the Core Idea, learning goal 3, and the Practice Lab use those same five words in that order. The worked apology at the end of the section already contains all five; label each clause inline so the reader can see the structure in a real sentence.  *(effort: small)*

### [HIGH · structure] ## References cited in this chapter

> Kumar, A., & Epley, N. (2023). A little good goes an unexpectedly long way

**Problem.** This reference is listed but cited nowhere in the body. The kindness callout cites Bohns (2016), Kumar & Epley (2018), and Zhao & Epley (2021, 2022) only. The section heading explicitly promises "References cited in this chapter," so an uncited entry is a defect a reader can catch.

**Edit.** Cite it in the "Two small practices that strengthen connection" callout, where the underestimated-impact-of-kindness result is precisely the claim being made, or delete the entry. Citing is preferable: it is the strongest direct support for "people often underestimate the value of a sincere appreciation." Also worth a reverse check on the other direction across the chapter.  *(effort: small)*

### [MEDIUM · accuracy] ### Cross the net carefully

> Conflict often follows a **pinch → story → avoidance → crunch** cycle.

**Problem.** A four-stage model is set in bold - the same typographic authority the chapter gives to defined technical terms - with no source and no evidence status. Nothing tells the reader whether this is a practitioner heuristic from organizational development or a tested empirical sequence, in a chapter that is otherwise scrupulous about that distinction. The "cross the net" metaphor in the same section is likewise unsourced.

**Edit.** Attribute and mark the status in half a sentence: "A practitioner model from organizational development describes conflict as pinch → story → avoidance → crunch; it is a useful frame rather than a tested causal sequence." Verify the attribution (the pinch model is usually credited to Sherwood & Glidewell, 1973) before printing it, and do the same for "stay on your own side of the net," which can be credited to the difficult-conversations tradition already cited via Stone et al. (2010).  *(effort: small)*

### [MEDIUM · accuracy] ### Constructive disagreement

> Civility matters because contempt closes minds and damages the conditions for thought.

**Problem.** A causal claim ("contempt closes minds") stated with no evidence and no hedge, standing alone as a one-sentence paragraph, in a chapter where nearly every comparable claim carries a citation. It reads as an aphorism inserted where an argument should be, and a reader trained by this book to ask "what showed that?" will notice.

**Edit.** Either support it - the relationship literature on contempt is the natural anchor, with the standard caveat that the widely quoted divorce-prediction accuracies come from models fitted after the fact and have been criticized on that ground - or reframe it explicitly as the chapter's normative stance: civility is not being claimed here as a technique that works, but as the condition under which the preceding paragraph's diagnosis can be carried out at all.  *(effort: medium)*

### [MEDIUM · accuracy] ### Replace mind-reading with verified understanding

> Agreement remains optional; visible uptake and a path to correction do not

**Problem.** Laurenceau et al. (1998) is cited four times in this chapter - for disclosure pacing, for partner-centered attention and dignity, for visible uptake, and for building shared reality. It is a diary study of self-disclosure, partner disclosure, and perceived partner responsiveness in ongoing relationships. It does not test dignity, visible uptake, or correction paths, so it appears to be the evidence base for normative recommendations it cannot support.

**Edit.** Keep Laurenceau for the disclosure-responsiveness-intimacy link only, where it is exactly right. For the uptake and correction claims, cite the grounding evidence from Chapter 33 (Clark & Brennan, 1991) or state plainly that this is a recommendation derived from the grounding model rather than a tested result. The same narrowing applies at the partner-centered attention paragraph, where Laurenceau is paired with Epley et al. (2004) for a claim about dignity that neither study addresses.  *(effort: medium)*

### [MEDIUM · accuracy] line 104

> Use the ask–listen–reflect–verify loop from Chapter 33

**Problem.** Backward reference misdescribes what Chapter 33 says. Chapter 33 never names a four-step loop; its only formulation is at line 89, in the perspective-taking table: "Use perspective-getting: ask, listen, and verify." Three steps, no "reflect", and not labelled a loop. A reader who turns back to ch33 looking for "the ask–listen–reflect–verify loop" will not find that phrase, and the extra step (reflect) is the one ch34 actually relies on in the following sentence about paraphrase and acknowledgment.

**Edit.** Fix in ch33 rather than ch34, because ch34's four steps are the better procedure and ch33 should own the naming. Promote ch33 line 89 into a named procedure in the body text — "ask, listen, reflect, and verify" — so the label exists at its source, then make ch34 line 104 a link: "Use the [ask–listen–reflect–verify loop](33-communication-language-is-not-a-file-transfer.qmd#perspective-getting) until the other person can recognize or correct your account." This also gives ch33, currently a zero-link chapter, an inbound anchor.  *(effort: small)*

### [MEDIUM · clarity] ### Diagnose the conversation before answering it

> The same sentence can carry at least three kinds of need.

**Problem.** This paragraph runs eight sentences and does four jobs: restates the case, states the diagnostic task, defines three bolded terms with two citations, and states the failure mode. The three definitions - the section's actual content - are buried mid-paragraph, and the table immediately below formalizes the same three layers, so the reader receives the same material twice in two formats within twenty lines.

**Edit.** Split into three short paragraphs: (1) the case and its double bind; (2) the three layers at one sentence each, letting the table carry the detail instead of duplicating it; (3) the mismatch failure ("advice fails when the speaker is asking to be understood; validation frustrates when an urgent plan is needed"), which is the sharpest line in the section and currently ends a paragraph nobody is still reading closely.  *(effort: small)*

### [MEDIUM · consistency] ### Replace mind-reading with verified understanding

> Use the ask–listen–reflect–verify loop from Chapter 33

**Problem.** Chapter 33 never names an "ask-listen-reflect-verify loop." It presents "Utterance → interpretation → test → correction → shared-enough meaning" as its labeled sequence and, separately, the phrase "ask, listen, and verify." A reader who turns back to find the loop under this name will not find it, and the two chapters' central procedure ends up with two names and neither definition.

**Edit.** Use one label in both chapters. Either rename the Chapter 33 sequence to the four-step loop and print it there as a labeled, numbered sequence (which would also make Chapter 33's "Close the loop" section heading pay off), or change this sentence to "the utterance → interpretation → test → correction sequence from Chapter 33." The same one-label rule applies to "perspective-getting," which Chapter 33 defines and this chapter uses without re-anchoring.  *(effort: small)*

### [MEDIUM · engagement] ### Diagnose the conversation before answering it (closeness paragraph)

> gradually escalating **reciprocal** self-disclosure produced greater immediate feelings of closeness

**Problem.** This is the procedure that became famous as the "36 questions that lead to love," almost certainly the most recognizable study in the chapter, and it appears as an abstract description with no procedure, no duration, and no name. The reader who knows it will not recognize it; the reader who does not will not remember it.

**Edit.** Give the scene in one clause - 45 minutes, strangers paired in a lab, three sets of questions escalating from "Would you like to be famous? In what way?" to "When did you last cry in front of another person?" - and name it as the procedure later circulated as the 36 questions. Keep the existing "immediate" hedge, which is the honest boundary that popular retellings drop and which becomes more valuable once readers recognize what is being qualified.  *(effort: small)*

### [MEDIUM · engagement] ### Test the social forecast

> People expected more enjoyment from solitude, but participants assigned to connect reported

**Problem.** The most counterintuitive experiment in the section is delivered in one agentless sentence with no setting, no sample, and no magnitude. "A more positive experience" does not tell the reader whether the effect was trivial or large, and "commuters" places them nowhere, so the paragraph's conclusion ("anxiety is a forecast, not a verdict") has nothing concrete under it.

**Edit.** Place it and size it: Chicago-area train and bus commuters, randomly assigned on an ordinary morning commute; give the direction and size of the forecasting error in the study's own units; keep the productivity result, which is the part that disarms the obvious objection. One extra sentence on the predictors' confidence would also mirror the Kruger calibration gap from Chapter 33 and tie the two chapters together.  *(effort: small)*

### [MEDIUM · engagement] Opening scenario (before Core Idea)

> We will follow this fictional exchange through listening, a more accurate account

**Problem.** The opening's third paragraph stops the scene to announce the chapter's itinerary. The preceding two paragraphs had built a genuine double bind - a real delivery problem plus an unfair accusation - and this sentence releases that tension into a table of contents instead of using it.

**Edit.** Replace with the stake: what the manager loses by leading with the explanation - the colleague hears a defence, the handoff stays broken, and the next date change fails the same way. If the fictional status needs disclosing, attach it to the case ("the case is composite") rather than to a preview of the chapter's sections.  *(effort: small)*

### [MEDIUM · insight] ### Apology and repair

> responsibility and repair can be particularly influential in how apologies are evaluated

**Problem.** The citation is accurate but the finding's most useful detail is dropped. Lewicki et al. tested six components and produced a ranking, with acknowledgment of responsibility rated most effective and a request for forgiveness least. That ranking tells the reader where to spend their sentences, and it explains evidentially - rather than by assertion - why "I'm sorry if you were offended" fails and why appending "will you forgive me?" does not rescue it.

**Edit.** Replace the hedged sentence with the ranking: name the six components, say which ranked highest and lowest, and state the design (participants rating apology scenarios, not tracked field outcomes) so the reader knows what kind of evidence this is. A three-column table - Component | What it does | Version of it in the project case - would carry this better than prose and supply the visual relief this section lacks.  *(effort: medium)*

### [MEDIUM · insight] ### Constructive disagreement

> experiences of harm were judged as more rational and increased respect more than factual claims

**Problem.** The chapter reports that personal experience earns respect but never says what it does not do. In that work, respect and persuasion came apart: hearing an experience of harm raised judgments of the speaker's rationality and increased respect without reliably moving the listener's position. That gap is the memorable point, and it is also what keeps the technique from reading as a persuasion trick right after the moral-reframing paragraph.

**Edit.** Add one sentence: respect rose while positions largely did not, which is exactly what this section needs - a way to keep disagreeing without contempt, not a way to win. Then tie it back to the boundary Chapter 33 draws between communication and persuasion: making models mutually testable is a different achievement from changing one.  *(effort: small)*

### [MEDIUM · visual] ### Listen for the layer beneath the words (figure)

> A repair procedure moves from the event and private interpretation toward perspective-getting

**Problem.** A figure showing a repair procedure is placed inside the listening subsection and is never discussed in the surrounding body, while section 3, "Repair meaning and relationship," runs about 1,140 words - co-rumination, constructive disagreement, apology - with no figure and no table, relieved only by one collapsed research note.

**Edit.** Move fig-conversation-repair into "Apology and repair," where its content is actually being taught, and give it one sentence of body discussion that earns it (for example: the third box is where most apologies stop, because the speaker treats explaining the intent as the repair). If the listening section then needs relief, the What/How/Why table already there can carry it.  *(effort: small)*

---

## `chapters/35-negotiation-as-joint-decision-design.qmd`  (14 findings)

### [HIGH · engagement] L63, "### What skilled practice looks like"

> prepared more for possible common ground, asked more questions

**Problem.** Rackham & Carlisle (1978) is the single most-cited observational study in negotiation training, and the chapter reports it entirely without numbers, sample size, or design. Every one of its findings is delivered as a comparative adjective ("more," "fewer"), which is exactly the flatness that kills a surprising result. A reader cannot tell whether skilled negotiators asked 10% more questions or twice as many — the answer is that questions were roughly a fifth of their observed behaviour versus a tenth for the average group, which is a startling ratio and lands as nothing.

**Edit.** Rewrite the passage with the published figures (verify against the 1978 article before setting): 48 negotiators observed across 102 real negotiating sessions; skilled negotiators spent about 40% of planning comments on areas of possible common ground versus 11% for the average group; questions were 21.3% of their bargaining behaviour versus 9.6%; they advanced 1.8 reasons per argument versus 3.0; they used 2.3 'irritators' per hour versus 10.8; defend/attack behaviour was 1.9% versus 6.3%; they considered 5.1 possible outcomes per issue versus 2.6. Then add the boundary condition the book's voice requires: the sample was selected by reputation and track record, the design is observational not experimental, and the setting was 1970s UK labour and commercial bargaining, so the behaviours are correlates of rated skill, not demonstrated causes of it.  *(effort: medium)*

### [HIGH · engagement] L18, "## A supplier says no"

> A manufacturer asks a long-standing supplier to accept a large order

**Problem.** The gateway chapter for the whole negotiation part opens with a scenario containing no number at all: not the order size, not the unit price, not the date, not the penalty, not the margin on the displaced work. Chapter 37's opener (same part, same supplier motif) names $18 per pound, one million pounds, and 250 pounds, and is incomparably more gripping. The abstraction also weakens the argument: the reader is asked to accept that price, capacity, timing, risk, and implementation trade against each other without ever seeing one quantity trade against another.

**Edit.** Give the scenario four numbers in the first two sentences: the order quantity and unit price (e.g., 40,000 units at €12.40), the fixed production date, the value of the higher-margin work the supplier would displace, and the late-delivery penalty the supplier would be exposed to. Carry the same numbers into section 3's split-delivery trade so the chapter closes the loop it opened.  *(effort: small)*

### [HIGH · structure] L32, "## Learning goals" / L131 Practice Lab

> Produce a prepare–interact–implement plan for one joint decision.

**Problem.** Learning goal 3 promises a three-phase plan, but the Practice Lab asks only for a preparation artifact — a one-page joint-decision map of parties, positions, interests, issues, alternatives, standards, authority, and risks. Nothing in the lab produces the interact or implement halves. Section 3, "Implement and learn," is only about 230 words and delivers one definition (governance) plus a forward pointer; it contains no learning or review content despite its title.

**Edit.** Either extend the Practice Lab to three columns — Prepare (the existing map), Interact (two diagnostic questions and one conditional trade to test), Implement (who confirms capacity, what triggers payment, what happens if batch one is late, when the parties review) — or narrow the learning goal to preparation and retitle section 3 "Implement" so the promise matches delivery.  *(effort: medium)*

### [MEDIUM · accuracy] L99, "### Emotion, face, and relationship"

> depending on legitimacy, power, interpretation, and context (Van Kleef et al., 2004)

**Problem.** A single 2004 experiment is cited as the source for a four-moderator claim it did not test. Van Kleef, De Dreu and Manstead (2004, JPSP 86(1)) manipulated an opponent's expressed anger versus happiness in a computer-mediated multi-issue negotiation and found participants conceded more to the angry opponent; legitimacy, power and cultural interpretation come from separate later literatures. As written, the sentence presents a literature-level synthesis as one study's finding — a pattern the book is otherwise careful to avoid.

**Edit.** Split the sentence: report the 2004 result with its direction and magnitude (concessions were higher against an angry than a happy counterpart), then cite the moderators to their own sources — e.g., Sinaceur and Tiedens (2006) on when anger extracts concessions and when a strong alternative reverses it, and work on cultural variation in responses to expressed anger — or replace the single citation with a review.  *(effort: medium)*

### [MEDIUM · clarity] L34–38, between Learning goals and "## 1. Prepare the joint decision"

> Individual decision analysis asks which available option best serves one decision-maker.

**Problem.** Three substantive paragraphs — the distinction between individual decision analysis and negotiation, the relation to persuasion and communication, and the chapter roadmap — float unheaded between the Learning goals and the first numbered section. They carry the chapter's conceptual definition of negotiation, yet a reader scanning headings passes straight from goals to "Prepare the joint decision" and never sees where the definition lives. Chapters 36 and 37 both begin their body with a heading.

**Edit.** Give the block a heading such as "### What makes a negotiation different from a decision" placed under section 1, or promote it to its own short section before section 1. Either way the definitional material becomes navigable and the numbered prepare/interact/implement scheme starts cleanly.  *(effort: small)*

### [MEDIUM · clarity] line 55, myths table row

> A deal can be worse than the BATNA.

**Problem.** BATNA is used as a bare acronym here, in a table in the first chapter of Part VI, but it is not expanded anywhere in the book until Chapter 36 line 38 ("That course of action is your **BATNA**, the best alternative to a negotiated agreement (Fisher et al., 2011)"). A reader meeting the term for the first time in this table has no way to decode it, and ch35 never expands it — the chapter uses "best alternative" in the adjacent cell but never connects the two. Chapter 35 is also one of the twenty zero-link chapters, so there is no pointer to follow.

**Edit.** Expand on first use in ch35 line 55: "A deal can be worse than the best alternative to a negotiated agreement (BATNA)." Then, since ch35 line 87 already promises "Chapter 36 develops preparation and claiming", convert that promise to a live link to #batna-aspiration-and-bargaining-power so the reader can reach the definition immediately rather than waiting a chapter.  *(effort: small)*

### [MEDIUM · consistency] L59, table caption

> Negotiation myths and replacement questions {#tbl-30-1}

**Problem.** Both tables in this chapter carry stale labels from the pre-renumbering draft (#tbl-30-1 in chapter 35), and neither is cross-referenced with @tbl- in the body — a pattern that holds across all three chapters: nine labelled tables, zero @tbl- references. A labelled float that nothing points to will still be numbered by Quarto, so readers see "Table 1" with no prose that names it.

**Edit.** Rename to #tbl-35-myths and #tbl-35-gateway-map, and add one referencing sentence each ("@tbl-35-myths pairs each habit with the question that replaces it"). Apply the same rename across chapters 36 and 37, where #tbl-31-1, #tbl-31-preparation-test, #tbl-31-first-offer-matrix, #tbl-33-1, #tbl-33-information-matrix and #tbl-33-supplier-package all carry the old chapter numbers.  *(effort: small)*

### [MEDIUM · consistency] L103, "### Culture and meaning"

> Earlier chapters provided a Meaning Audit.

**Problem.** The Meaning Audit is a named, reusable tool defined in the Practice Lab of chapter 29, and chapter 38 links to it precisely ("Return to the **Meaning Audit** in [Culture and Identity](29-culture-and-identity...)"). Chapter 35 gestures at "earlier chapters" with no link and no chapter number, so a reader instructed to "use it here" has no way to find it.

**Edit.** Match chapter 38's treatment: bold the term and link it — "Chapter 29 introduced the **Meaning Audit** ([Culture and Identity](29-culture-and-identity-the-same-action-is-not-the-same-act.qmd))" — so the same tool is addressable from both of the chapters that tell readers to run it.  *(effort: small)*

### [MEDIUM · engagement] L38, L87, L125

> The rest of this part develops the details.

**Problem.** The chapter tells the reader what the next three chapters will do three separate times — at L38, again at L87 ("Chapter 36 develops preparation and claiming; Chapter 37 develops discovery..."), and again at L125 ("The next three chapters develop this sequence"). In a 2,229-word chapter that is roughly one roadmap per 700 words, and it displaces the concrete supplier material the chapter actually needs.

**Edit.** Keep only the L87 version, which names the chapters and their distinct jobs. Replace L38 with the supplier case's opening tension restated as a question, and replace L125 with the one thing the split-delivery trade still leaves undecided, so the handoff to chapter 36 is a live problem rather than a table of contents.  *(effort: small)*

### [MEDIUM · engagement] L99, "### Emotion, face, and relationship"

> Anger can induce concessions or provoke retaliation, concealment, and distrust

**Problem.** This is one of the most counterintuitive results in the negotiation literature — displayed anger can pay — and it is stated so evenhandedly that the surprise dissolves into a list. The mechanism, which is the genuinely useful part, is never given: expressed anger works by changing the target's inference about where the angry party's limit sits, not by frightening them, which is why it collapses when the target has a strong alternative or can retaliate later.

**Edit.** Name the mechanism and the reversal in two sentences: anger moves the counterpart's estimate of your reservation value, so it extracts concessions from someone with weak alternatives and provokes retaliation or walkaway from someone with strong ones. Attach the concession difference from the original study, then land the practical point the chapter already implies — a tactic that works on the party who has no exit is precisely the tactic the ethics callout two pages later says to test.  *(effort: medium)*

### [MEDIUM · engagement] L52–59, myths table

> Toughness can destroy information and value.

**Problem.** The table asserts five myths and five hidden costs with no evidence attached to any row and no instance of anyone paying the cost. The first row's claim is precisely what the Rackham & Carlisle data ten lines above could substantiate, and the connection is never made; rows 2 and 5 (a deal worse than the BATNA, ignored implementation) are the two failure modes the reader is most likely to have experienced and neither gets a case.

**Edit.** Add an "Evidence or case" column: row 1 takes the Rackham irritator and defend/attack figures; row 2 takes a one-line instance of a signed deal that underperformed the walk-away option; row 5 takes a one-line instance of an agreement that failed in implementation. Five short entries convert the table from a list of opinions into the chapter's evidence summary.  *(effort: medium)*

### [MEDIUM · insight] L95, "### Fairness and objective standards"

> Alternatives create power; standards help create legitimacy.

**Problem.** This is the sharpest sentence in the chapter and the paragraph moves on without cashing it out. The implication the chapter stops one step short of is the one that ties the whole part together: the party with the stronger alternative can dictate terms but still depends on the weaker party's voluntary performance afterwards, so power buys the signature and legitimacy buys the implementation. Section 3 then introduces governance with no connection back to this point.

**Edit.** Add two sentences after the quoted line: power determines what terms you can obtain; legitimacy determines whether the other side executes them without monitoring, dispute, or quiet non-performance. Then make section 3's governance paragraph the payoff — governance is what you need when you won on power and lost on legitimacy — which gives the chapter's three sections a causal spine instead of three parallel lists.  *(effort: small)*

### [MEDIUM · visual] L42–44, figure under "Replace performance myths with design questions"

> Replace performance myths with design questions

**Problem.** @fig-negotiation-architecture is placed directly under a heading about negotiation myths, which is not what the figure shows, and it is never cross-referenced with @fig- anywhere in the chapter or the book (verified across all .qmd files). The caption states a definition rather than a takeaway, so a reader skimming figures learns nothing that the surrounding prose does not already say.

**Edit.** Move the figure to sit beside the gateway-map material (L69–79), where its panels actually correspond to the table rows, and add a sentence that references it: "@fig-negotiation-architecture shows why the buyer's demand and the supplier's refusal can both be rational: each side is comparing the package with a different alternative." Rewrite the caption to that claim rather than a restatement of the chapter definition.  *(effort: small)*

### [MEDIUM · visual] L121–125, "## 3. Implement and learn"

> Suppose the supplier can meet the production date by delivering half the order first

**Problem.** This is the chapter's only worked trade — the moment the whole gateway argument pays off — and it is three sentences of prose with no table, figure, or callout. The 537-word stretch from the gateway map at L79 to the ethics callout at L105 also runs with no visual. The reader is told a package "beats each party's alternative" without ever seeing the two packages side by side.

**Edit.** Add a compact before/after table beside L121: rows for delivery date, batch size, unit price, penalty allocation, and review trigger; columns for "Original demand," "Split-delivery package," "What changes for the buyer," "What changes for the supplier." Using the numbers recommended for the opening scenario, this lets the gateway chapter demonstrate in one table what chapters 36–38 then unpack.  *(effort: medium)*

---

## `chapters/36-preparing-and-claiming-value.qmd`  (16 findings)

### [HIGH · accuracy] L188, "## 3. Respond"

> excessive precision can look theatrical or uninformed (Mason et al., 2013)

**Problem.** Misattribution. Mason, Lee, Wiley and Ames (2013) tested whether precise first offers elicit more conciliatory counteroffers and attributions of knowledge; they did not establish that excessive precision backfires. That is the too-much-precision effect, from Loschelder, Friese, Schaerer and Galinsky (2016) and Loschelder, Friese and Trötschel (2017). The manuscript's own retired anchoring chapter states this correctly and cites both papers, but neither Loschelder entry survives in references.qmd — the correct citations were dropped in the chapter reorganization and the claim was folded into the wrong source.

**Edit.** Split the claim: cite Mason et al. (2013) for the precision-signals-calculation half with its actual result, and cite Loschelder, D. D., Friese, M., Schaerer, M., & Galinsky, A. D. (2016), The too-much-precision effect, Psychological Science, 27(12), 1573–1587 for the backfire half, adding the boundary condition that paper establishes (it backfires with experts and when the number has no credible basis). Restore both Loschelder entries to references.qmd and to this chapter's reference list.  *(effort: small)*

### [HIGH · accuracy] L120, "### BATNA, aspiration, and bargaining power"

> Research on aspirations supports the importance of targets (White & Neale, 1994)

**Problem.** This citation conveys no information — it names no design, no measure, no magnitude, and no boundary. It also omits the best-established caveat about aspirations, which the chapter's own section 5 needs: raising a target improves objective outcomes but lowers satisfaction with the identical deal, because the reference point against which the outcome is judged moves with it. The chapter warns against comparing €9,400 to "the emotionally salient €9,800 target" without ever explaining why the target became emotionally salient.

**Edit.** Replace with a sentence stating what White and Neale measured (aspirations and settlement expectancies as predictors of bargaining outcomes) and what they found, and add the counterfactual-satisfaction finding (negotiators with high aspirations obtain better terms and feel worse about them — Galinsky, Mussweiler & Medvec, 2002, JPSP) as the bridge into section 5. That turns two disconnected paragraphs into one argument.  *(effort: medium)*

### [HIGH · consistency] L120 vs L186

> Keep the reservation value, target, and opening offer separate.

**Problem.** The chapter states the three-number discipline, prints it as a table row (tbl-31-1 lists "Opening offer" as distinct from "Target"), and then collapses it in the worked case: at L186 the seller says "€9,800 is the appropriate starting point," making the target and the opening the same number. The case therefore never produces an opening offer at all, and section 5's warning about the "emotionally salient €9,800 target" is now warning about the seller's own stated asking price — a different and much weaker point.

**Edit.** Give the seller a distinct opening with its own justification (e.g., €10,400, supported by the two highest comparable sales plus the recent service record), keep €9,800 as the target, and keep €8,000 as the reservation value. Then the counter-anchor script at L186 demonstrates the separation instead of contradicting it, and the close at L209 has three reference points to test the €9,400 offer against.  *(effort: medium)*

### [HIGH · consistency] L213, immediately before "## Practice Lab"

> []{#ch36-research-findings}

**Problem.** A bare anchor with no heading and no content sits at the end of section 5. concept-index.qmd L411 routes the Informed consent entry to it — "Negotiation boundary: [Ch. 36](chapters/36-preparing-and-claiming-value.qmd#ch36-research-findings)" — but chapter 36 contains no discussion of informed consent, disclosure duties, or consent under pressure anywhere; that material lives in chapter 35's "Ethics is part of agreement quality" callout and in chapter 38. The link resolves, so no link checker will flag it, and the reader lands on a closing paragraph about nibbles. The anchor name also promises a "research findings" section that does not exist.

**Edit.** Decide which is true. If chapter 36 should carry the consent boundary, add the paragraph — when a claiming tactic crosses into manufacturing a false belief, and what changes when the counterpart cannot exit — and give it a real heading. Otherwise delete the empty anchor and repoint concept-index.qmd L411 to chapter 35's ethics callout, which is where the content actually is.  *(effort: small)*

### [HIGH · engagement] L148, "## 2. Open: anchor only when you can defend the frame"

> Experiments show that first offers can anchor settlements (Galinsky & Mussweiler, 2001)

**Problem.** The chapter's central empirical claim is reported with no numbers and, more damagingly, without the study's most useful result. Galinsky and Mussweiler found not only a first-mover advantage in settlement prices but that the advantage was eliminated when the responding negotiator was directed to focus on their own reservation price or target, or to take the opponent's perspective. That moderator is exactly the countermeasure section 3 prescribes twenty lines later ("Return to the €8,000 alternative, the €9,800 target") — the chapter gives the prescription and withholds the evidence that it works.

**Edit.** Report the settlement difference between the buyer-first and seller-first conditions in their negotiation exercise, then add the moderator in its own sentence: the first-offer advantage disappeared when the receiving side was focused on their own reservation price and target, or on the other side's alternatives. Then open section 3 by naming it as the tested remedy rather than as advice.  *(effort: medium)*

### [HIGH · insight] L200 vs L209–211

> If payment is completed this week, I can move to €9,500.

**Problem.** The worked case contains a textbook nibble that the chapter never points at. The seller offers €9,500 conditional on payment this week; the buyer then returns with €9,400 and payment this week — taking the condition and shaving €100 off the price attached to it. One paragraph later the chapter warns "Do not let a late 'nibble' convert relief into another unilateral concession," without noticing that its own example just staged one. The chapter also frames the wrong comparison at close (€9,400 versus €8,000 and versus €9,800) and omits the decisive one: €9,400 versus the seller's own conditional €9,500.

**Edit.** Make it explicit at L209: the buyer has accepted the condition and unbundled the price from it, so the live comparison is €9,400 against the €9,500 the seller had already made contingent on exactly this payment timing. Add the repair move the chapter's own discipline 3 implies — re-link them ("€9,500 with payment this week, or €9,400 with payment on transfer") — which demonstrates conditional concession-making in the case rather than only in the list.  *(effort: small)*

### [HIGH · structure] L217, "## Practice Lab"

> Run the used-car negotiation in pairs.

**Problem.** The lab is not runnable as written. The body text gives every reader both reservation values — the seller's €8,000 and the buyer's €10,000 — plus the seller's €9,800 target and the €9,200 illustrative settlement. Two students who have read the chapter share complete information, so there is nothing to discover, no anchor can shift an estimate, and the lab's own instruction to "mark where an anchor changed an estimate" cannot be satisfied. No role sheets exist anywhere in the book (verified across all appendices).

**Edit.** Supply two short confidential role sheets with numbers different from the worked example — seller: firm competing offer of €7,400, documented service history, must sell within three weeks; buyer: financing ceiling of €9,600, needs a car before a start date, two comparable listings at €8,900 and €9,700 — and state that each side reads only its own sheet. Keep €8,000/€10,000 as the illustration. Placing the sheets in Appendix C would make them reusable for chapter 37's lab too.  *(effort: medium)*

### [HIGH · visual] L203, "## 4. Move: make concessions carry information"

> Across seven studies, recipients of decreasing concessions made less ambitious counteroffers

**Problem.** Sections 3, 4 and 5 run 629 words with no figure, table, or callout — the longest unrelieved stretch in the chapter — and section 4 is its most research-dense passage. Concession patterns are inherently a shape over time, which is the one thing prose cannot show: a reader must hold three offer sequences in memory to see that they can all end at the same price while teaching the counterpart three different things.

**Edit.** Add a small line chart beside the Tey et al. paragraph. X-axis: offer round 1–4. Y-axis: seller's price in euros, €9,200 to €10,400. Three labelled seller paths all terminating at €9,200 — constant (three moves of €400), decreasing (€800, €400, €150), and one single move of €1,200 — annotated with the counteroffer each pattern elicited in the studies. Caption as the takeaway: "Three routes to the same price teach the counterpart three different things about your limit."  *(effort: medium)*

### [MEDIUM · accuracy] L205, "## 4. Move"

> Silence can create time for deliberation and sometimes improve value creation

**Problem.** Curhan et al. (2022) is cited for advice the reader cannot act on, because the chapter omits the operationalization that makes the finding a finding: the paper studies extended silence, defined by a specific duration threshold, not a general recommendation to pause. "Make the pause recoverable" gives a script but no length. The chapter also does not distinguish which of the paper's studies were observational coding of recorded negotiations and which experimentally manipulated silence, so the causal warrant is invisible in a book that is normally scrupulous about this.

**Edit.** State the threshold the paper used (silences of roughly three seconds or longer) so the advice is executable, and add one clause distinguishing the observational analyses from the experimental manipulation, as the book does for Kruger et al. in chapter 33. The second half of the sentence — that silence can also signal disrespect or disengagement — should be attributed separately if it is not from this paper.  *(effort: small)*

### [MEDIUM · accuracy] L205, "## 4. Move"

> Time pressure can accelerate agreement, but delay costs are rarely symmetric

**Problem.** A meta-analysis is cited with no k and no effect size — the one citation type where the magnitude is the entire contribution. Worse, the sentence bundles two claims under one citation: the meta-analytic result about time pressure and agreement speed, and the asymmetry-of-delay-costs point, which is the authors' own analytic framing and not a meta-analytic estimate. A reader cannot tell which half the citation supports.

**Edit.** Report the number of studies and the direction and size of the pooled effect on concession-making and agreement rates. Then move the asymmetry sentence outside the citation and make it the chapter's own diagnostic — whose deadline is it, what happens to each party the day after, and who can extend it — since that is what the following instruction ("Ask what changes at the deadline and for whom") actually operationalizes.  *(effort: small)*

### [MEDIUM · clarity] L188, "## 3. Respond"

> €9,800 to €10,200 depending on timing and payment

**Problem.** The chapter gives correct range-offer advice but names neither of the two terms that make it findable or memorable. Ames and Mason distinguish a bolstering range (lower endpoint at or near your target) from a bracketing range (target in the middle, lower endpoint below it). The manuscript's retired anchoring chapter defined both explicitly; the current chapter describes the distinction in a subordinate clause — "a range whose lower endpoint concedes the target" — and drops the vocabulary, so a reader who wants to look this up has no search term.

**Edit.** Restore the two labels in bold on first use and give each one clause: a **bolstering range** starts at the target and extends upward; a **bracketing range** puts the target in the middle and invites the counterpart to hear the bottom. One added sentence recovers the terminology and makes the €9,800–€10,200 example self-explaining.  *(effort: small)*

### [MEDIUM · structure] L16, "## 1. Prepare: the case before the vocabulary"

> 1. Prepare: the case before the vocabulary

**Problem.** Template deviation. In chapters 35 and 37 the opening scenario gets its own unnumbered heading ("A supplier says no," "Why would a supplier refuse a million-pound order?") and the Core Idea and Learning goals follow it before the numbered body begins. Here the scenario is swallowed by the first numbered section, so Core Idea and Learning goals appear inside section 1 and the section then resumes at L38 — a reader scrolling the outline sees section 1 interrupted by front matter.

**Edit.** Split the block: give L18–24 its own scenario heading (e.g., "## The car and the offer you already have"), then Core Idea, then Learning goals, then "## 1. Prepare" starting at L38. This costs one heading and brings the chapter into line with its two neighbours.  *(effort: small)*

### [MEDIUM · structure] line 148

> extending anchoring research on numerical judgment (Tversky & Kahneman, 1974)

**Problem.** A chapter pair that should cross-link and does not. This sentence explicitly frames itself as an extension of the anchoring literature, and cites the exact Tversky & Kahneman (1974) wheel-of-fortune study that Chapter 11 line 38 works through in full. Chapter 11 is where the mechanism debate lives (insufficient adjustment versus selective accessibility, Mussweiler & Strack 1999; @fig-anchor-decoy separating effect from mechanism), and ch36's next sentence — "The effect is not solely a failure to adjust" — is a direct reply to that debate. But ch36 has zero outbound links and ch11 has zero outbound links, so the two halves of one argument never meet.

**Edit.** Add the link at ch36 line 148: "...extending [anchoring research on numerical judgment](11-when-context-rewrites-comparison.qmd#the-decoy-changes-the-comparison) (Tversky & Kahneman, 1974)." Then add the reciprocal forward pointer at ch11 line 46, where the chapter already concedes anchors can be informative: "...weakly justified. [*Preparing and Claiming Value*](36-preparing-and-claiming-value.qmd) treats a first offer as a deliberate anchoring decision." The same treatment is warranted for ch35 line 117, which lists "Anchoring, overconfidence, self-serving interpretation, reactive devaluation, and fixed-pie assumptions" with no link to ch11, ch15, or ch10.  *(effort: small)*

### [MEDIUM · visual] L18 and L77

> Before reading on, write down:

**Problem.** Two related gaps. First, the chapter's only reader activity — the five-item preparation exercise that the whole chapter is built to answer — is plain prose, while the book has a styled .activity callout class used elsewhere; the chapter's single styled element is the Core Idea. Second, @fig-zopa is never cross-referenced in the body even though the surrounding 700 words on reservation values, surplus, and the €9,200 split are precisely what it depicts, so the figure and the arithmetic sit adjacent without ever addressing each other.

**Edit.** Wrap L18–24 in `::: {.callout-note .activity icon=false}` with a short title such as "Five numbers, before the vocabulary," and return to it explicitly at L120 so the reader checks their five answers against the finished framework. In the ZOPA section add a referencing sentence — "@fig-zopa shows the same interval the arithmetic below computes" — so the figure carries the worked numbers rather than duplicating them silently.  *(effort: small)*

### [LOW · clarity] line 83

> The bargaining zone, also called the zone of possible agreement or ZOPA

**Problem.** ZOPA is introduced twice from scratch inside one chapter, 39 lines apart. Line 44 already says "When acceptable prices overlap, there is a **zone of possible agreement**, or **ZOPA**. We will calculate it below." Line 83 then re-expands the acronym as if new. The second definition also silently introduces a third synonym ("bargaining zone"), so the reader is handed three labels for one construct without being told they are the same thing.

**Edit.** Line 44 is the right place to define it, since it explicitly promises the calculation. Trim line 83 to deliver on that promise: "The ZOPA lies between €8,000 and €10,000." If "bargaining zone" is worth keeping as a synonym, fold it into the line 44 definition instead, where the other terms are introduced.  *(effort: small)*

### [LOW · consistency] L239–243, "## References cited in this chapter"

> White, S. B., & Neale, M. A. (1994)

**Problem.** The reference list is two concatenated alphabetical runs: Fisher, Galinsky, Tversky, White — then restarting at Ames, Curhan, Mason, Stuhlmacher, Sun Tzu, Tey. Chapter 37's list is correctly ordered throughout, so the deviation is chapter-specific and visible to any reader who scans for a source. Chapter 35 has a smaller instance of the same problem: Thompson, Wang & Gunia (2010) is placed before Thompson & Hastie (1990), whereas APA orders the two-author entry first.

**Edit.** Re-sort chapter 36's list into a single alphabetical sequence, and swap the two Thompson entries in chapter 35 so Thompson & Hastie precedes Thompson, Wang & Gunia. Worth a one-off script across all chapters given that two of three files in this part deviate.  *(effort: small)*

---

## `chapters/37-creating-value-across-differences.qmd`  (14 findings)

### [HIGH · accuracy] L111, "## Interests behind positions"

> Perspective-taking can improve discovery when it generates questions rather than confident projection

**Problem.** The claim and the citation point in different directions. Galinsky, Maddux, Gilin and White (2008) manipulated instructed perspective-taking against empathy and found perspective-taking raised individual and joint gains; it did not test question-asking and offers no evidence about projection. The stated claim is the perspective-getting result of Eyal, Steffel and Epley (2018) — which the manuscript already holds, cites correctly in chapter 33 ("people were often more accurate when they asked others for their perspective than when they merely tried to imagine it") and pairs correctly with Galinsky in chapter 38 L139. Chapter 37 alone attaches the getting result to the taking study.

**Edit.** Follow chapter 38's pattern exactly: cite both (Eyal et al., 2018; Galinsky et al., 2008), state which does what — imagination reduces egocentrism and can improve joint gains, but direct questions supply new correctable evidence — and add the cross-reference to chapter 33 where the distinction is established. Add the Eyal et al. entry to this chapter's reference list; it is already in references.qmd.  *(effort: small)*

### [HIGH · engagement] L92, "## Barriers to value creation"

> Fixed-pie beliefs and inaccurate social perception prevent negotiators from discovering compatible interests

**Problem.** The chapter's core empirical premise gets one flat sentence and one citation with no numbers, in a book whose stated weakness is exactly this. The most arresting statistic in the integrative-negotiation literature is absent: across the accumulated studies, a substantial share of negotiators settle on outcomes both sides liked less than an available alternative, and roughly half fail to notice an issue on which their interests were perfectly compatible. Stated as "fixed-pie beliefs prevent discovery," it reads as a truism; stated as a percentage, it is alarming and immediately motivates the rest of the chapter.

**Edit.** Add Thompson and Hrebec (1996), Lose-lose agreements in interdependent decision making, Psychological Bulletin, 120(3), 396–409 — a review of 32 studies reporting roughly 20% lose-lose settlements and about 50% failure to identify a fully compatible issue (verify the figures before setting). Add Thompson and Hastie's own timing result: fixed-pie judgments form in the opening minutes and resist revision. Place both immediately before the barriers table so the table answers a demonstrated failure rate rather than an assertion.  *(effort: medium)*

### [HIGH · engagement] L18–20, "## Why would a supplier refuse a million-pound order?"

> an existing promise to sell only 250 pounds a year to a cousin

**Problem.** The chapter states one million pounds a year at $18 per pound at L18 and the 250-pound cousin promise at L20, and never does the arithmetic that makes this case unforgettable: the carve-out is 0.025% of the volume, about $4,500 a year against an $18 million contract, and the buyer had been offering minimum orders and more money to move a position worth a rounding error. That ratio is the entire lesson of investigative negotiation and the reader is left to compute it.

**Edit.** State it in one sentence at the reveal: 250 pounds out of a million is one-fortieth of one percent of the volume — roughly $4,500 against an $18 million annual contract — and the buyer had twice raised the price rather than ask what the refusal protected. Then the chapter's closing line about diagnosing before paying carries the number with it.  *(effort: small)*

### [HIGH · engagement] L46, Camp David paragraph

> an official U.S. account describes Egypt pressing for Israeli withdrawal from the Sinai

**Problem.** The most famous integrative negotiation in the field is delivered in three sentences with no date, no participant's name, and no outcome. The reader is told that separating sovereignty from security "made a multi-issue package conceivable" but never learns what the package was, whether it held, or what it cost. The careful sourcing is admirable; the effect is that the chapter's flagship historical case is less concrete than its invented software-provider example.

**Edit.** Add the specifics the official source supports: the thirteen-day summit at Camp David in September 1978 with Sadat, Begin and Carter; the resolution in which Egyptian sovereignty over the Sinai was restored while the peninsula was demilitarized with limited-force zones and monitoring; formalization in the March 1979 treaty; completion of withdrawal in 1982. Then add the caveat the book's voice would want and that no textbook retelling includes: the tidy sovereignty-versus-security summary compresses a negotiation that nearly collapsed several times and an implementation that took three more years — which is exactly this part's thesis that a package must survive implementation.  *(effort: medium)*

### [HIGH · insight] L172, "## Logrolling"

> Logrolling is the heart of integrative negotiation.

**Problem.** The chapter asserts its central mechanism and never quantifies it once. Across 3,349 words there is not a single worked trade showing that both parties end up better off than under a compromise — no points, no prices, no comparison. Chapter 36 computes surpluses to the euro; chapter 37, whose whole claim is that trading across differences beats splitting, asks the reader to take it on faith. The Practice Lab then requires students to perform exactly the calculation the chapter declined to demonstrate.

**Edit.** Add a compact payoff table immediately after the quoted line, using the supplier case and three issues (exclusivity, volume commitment, delivery flexibility). Show each side's 100-point allocation, then three columns: split-the-difference compromise, the logrolled package, and each party's BATNA score — with the compromise scoring roughly 50/50 and the logrolled package roughly 70/65, both above the alternatives. One small table converts "logrolling transforms difference into value" from a slogan into a demonstration and makes the Practice Lab immediately runnable.  *(effort: medium)*

### [HIGH · structure] L22, roadmap vs L60 "## Pareto efficiency"

> diagnose fixed-pie assumptions, map interests and priorities, construct trades

**Problem.** The chapter announces a five-step sequence and then delivers it out of order. Pareto efficiency — step five, the test of whether a package improved both sides — arrives third, about 250 words in, before fixed-pie barriers, interests, priorities, or logrolling have been introduced. Its illustration (a software provider with unused training capacity and a client who needed training, where a longer contract lowers the price) is a logrolling example deployed 110 lines before logrolling is defined, and the reader has no vocabulary for it yet.

**Edit.** Move "## Pareto efficiency" to sit immediately before "## Build the supplier package," where the reader has a package to evaluate and the software example reads as an application rather than a preview. That restores the announced order, gives @fig-pareto a concrete package set to refer to, and lets "Compromise is not integration" follow directly from the opening case as the roadmap promises.  *(effort: medium)*

### [HIGH · structure] L215, "## Practice Lab"

> calculate whether each package beats both BATNAs

**Problem.** The lab requires a calculation the chapter makes impossible. Neither party's BATNA appears anywhere in chapter 37: the buyer's alternative source is never characterized, the supplier's alternative order book is never mentioned, and the supplier-package table gives issues and interests but no reservation values. Students can allocate 100 points and rank packages, but the beats-both-BATNAs test has no inputs.

**Edit.** Supply both alternatives, either in the supplier-package table or in the lab preamble — for example, the buyer's next-best qualified source at $21 per pound with a six-month qualification delay, and the supplier's alternative committed capacity at $16 per pound with no volume guarantee — and state the point totals each side assigns to its own BATNA so "beats both BATNAs" becomes a number a student can compute.  *(effort: medium)*

### [MEDIUM · accuracy] L126, tbl-33-1 priority map

> Use standards; do not expect easy integration.

**Problem.** The priority map states hypotheses as facts and contains a claim the chapter itself refutes. The price row asserts that price is high-priority for both sides and not integrable — yet L70's software example has a longer contract lowering the price, and L207's supplier package resolves price through volume tiers plus a contribution to verifiable capacity investment. Both are integrative moves on price. The "Their likely priority" column also invites exactly the confident projection the chapter warns against two sections earlier.

**Edit.** Retitle the columns "My priority" and "Their priority (hypothesis to test)" to match the chapter's own epistemics, and rewrite the price row to state the real condition: price resists integration while it is one number, and becomes tradable once it is decomposed into rate, volume tier, timing, and who bears which risk — pointing forward to the supplier-package table where the chapter does precisely that.  *(effort: small)*

### [MEDIUM · clarity] L66–68, "## Pareto efficiency"

> The feasible set may be discrete, nonconvex, or only partly known.

**Problem.** The formal definition — "Pareto efficient relative to a specified feasible set if there is no feasible alternative that at least one specified party prefers while no specified party is worse off" — packs three qualifications into one sentence and requires rereading. "Nonconvex" then appears once, is never defined, never recurs, and carries no consequence for the argument; it is jargon that costs the reader attention and returns nothing.

**Edit.** Split the definition in two: give the plain version first ("no other package available to these parties would make one of them better off without making the other worse off"), then the qualification in its own sentence ("efficient relative to which parties, which issues, and which value measures — a package can be efficient on the map and inefficient once an excluded issue is added"). Cut "nonconvex"; keep "discrete" and "only partly known," which the figure and the software example actually illustrate.  *(effort: small)*

### [MEDIUM · clarity] L42 and L172

> Logrolling is the heart of integrative negotiation.

**Problem.** "Integrative" is used as a load-bearing term here and in two table captions ("A priority map for integrative trade-offs") but is never defined in the chapter, while chapter 36 defined "distributive" explicitly. L42 introduces value creation and value claiming as the operative pair without saying that these map onto integrative and distributive — the terms the concept index, the table captions, and most other negotiation sources use. A reader moving between this chapter and the index meets two vocabularies for one distinction.

**Edit.** At L42, where value creation and value claiming are bolded, add one clause tying them to the standard terms: integrative (value-creating) and distributive (value-claiming), noting that chapter 36 developed the distributive half. This costs half a sentence and makes the table captions, the concept index, and the outside literature all legible from inside the chapter.  *(effort: small)*

### [MEDIUM · engagement] L20, opening scenario

> Write one sentence you would say at the table.

**Problem.** The instruction to the reader and the answer occupy the same paragraph, three sentences apart. The reader is told to compose a question, immediately handed the suggested question, and then handed the cousin reveal — the chapter's best surprise — inside a subordinate clause of the same block. There is no white space for the exercise and no pause before the resolution, so the surprise-then-resolution structure collapses into a single undifferentiated paragraph.

**Edit.** Break into two paragraphs. End the first with the reader's task and the suggested diagnostic question, so the page turns on an open question. Open the second with the reveal given its own sentence — "The answer, when the buyer finally asked, was a cousin." — followed by the promised 250 pounds a year and the arithmetic. Consider wrapping the task in the book's .activity callout so the instruction is visually separated from its answer.  *(effort: small)*

### [MEDIUM · insight] L192, "## Differences are opportunities"

> One party may have spare capacity, another may need earlier delivery

**Problem.** The chapter lists four or five sources of gains from trade — capacity, timing, risk-bearing cost, differing forecasts — dissolved into two sentences of prose, and never presents them as the named, countable set that makes them portable. This is the single most reusable checklist in integrative negotiation: a reader who leaves with five named difference types can run them against any deal, whereas a reader who leaves with "differences are opportunities" has a slogan. The section is 150 words and is the chapter's weakest-carrying real estate.

**Edit.** Convert to a five-row table beside this paragraph: difference in priorities (device: logroll across issues), difference in forecasts (contingent term), difference in risk tolerance (warranty, insurance, indemnity), difference in time preference (staging, financing, payment schedule), difference in capability or cost (allocate the task to whoever does it cheaper). Give each row the supplier case's own instance. This also sets up chapter 38's contingent-terms module, which currently arrives with only one of the five prepared.  *(effort: medium)*

### [MEDIUM · visual] L48, Camp David figure

> style="width:100%;min-width:0;max-width:100%;max-height:none;height:auto;"

**Problem.** Three problems on one line. The figure is never cross-referenced with @fig-camp-david-two-issue anywhere in the body, so the reader is never told to look at it. Its caption restates the adjacent sentence rather than delivering a takeaway the prose does not already carry. And it alone among the figures in these three chapters carries an inline style override, which bypasses the stylesheet and will behave differently in the EPUB build than the HTML one.

**Edit.** Add a referencing sentence to the Camp David paragraph. Rewrite the caption to state what the reader should conclude — one line over territory has two possible answers and neither was acceptable; two separate issues have four combinations, and one of them was. Move the sizing rule into quarto-custom.scss as a class (the other figures in these chapters use either no override or a plain width attribute) so the figure renders consistently across formats.  *(effort: small)*

### [LOW · consistency] L60 onward, heading scheme

> ## Pareto efficiency

**Problem.** Chapters 35 and 36 organize the body with numbered top-level sections ("## 1. Prepare the joint decision," "## 2. Interact," "## 3. Implement and learn"; "## 1. Prepare," through "## 5. Close"), which readers of Part 6 will have been trained on for two consecutive chapters. Chapter 37 abandons numbering entirely across ten top-level sections, and chapter 38 uses a third scheme ("Optional module 1..4"). Within one four-chapter arc the reader meets three different organizing conventions.

**Edit.** Pick one scheme for the part. Numbering chapter 37's sections to match its neighbours is the smaller edit and would also expose the sequence problem flagged separately — a numbered outline makes it obvious that the test step is sitting in position three.  *(effort: small)*

---

## `chapters/38-designing-better-agreements.qmd`  (14 findings)

### [HIGH · engagement] Opening scenario (before Core Idea), line 16

> The buyer and supplier agree on a promising package

**Problem.** The chapter's running case — which carries all six required fields, both example tables, three MESO packages, the contingent term, and the closing payoff — has no magnitude, no industry, no date, no named parties, and no consequence. Nothing is at stake when "the buyer" asks "the supplier" for "an urgent extra batch." Chapters 37 (Camp David) and 42 (Flint) show the book's own house style is the named, sized case; this chapter opens on pure abstraction and never recovers a single number in 3,900 words.

**Edit.** Size the case in the first two sentences and keep those numbers for the rest of the chapter: name the sector and the contract value (e.g. a three-year wiring-harness supply agreement worth ~EUR 40M), the urgent batch (12,000 units), the deadline that makes it urgent (a line that stops at 08:00 Monday), and the hourly cost of the stoppage. Then the phrase "flexibility was the point of the agreement" has a price attached. Reuse the same figures in @tbl-agreement-minimum-example (currently "capacity inside the agreed band" with no band) and in the surge-price bullet at line 125, so the six fields are demonstrated on real quantities rather than placeholders. Alternatively, replace the anonymous case with a documented supply dispute over forecast and allocation (the 2021–22 semiconductor allocation disputes offer several) and verify the figures against the source.  *(effort: medium)*

### [HIGH · engagement] Replace lie detection with claim verification, line 159

> nonverbal cues to deception are faint and unreliable

**Problem.** The chapter's most memorable empirical point is stated as an adjective and then abandoned. The redrawn figure directly below it carries the actual payoff — its own on-canvas headline reads "Believed 'tells' are much stronger than observed associations" and "max |r| = .19" across nine behaviors — but no sentence of body prose states a single one of those numbers, and @fig-lie-cues-belief-gap is never cross-referenced anywhere in the file. A reader skimming the prose learns only that cues are "faint," which is exactly the claim they will not believe about themselves.

**Edit.** Add two sentences after "faint and unreliable" that state the figure's numbers and name the cue everyone trusts: across nine behaviors in the meta-analytic synthesis the largest observed association was |r| = .19, and gaze aversion — the most widely believed tell — sits near zero, while students' and professionals' belief estimates for gaze aversion, blinking, and adaptor movements run several times larger than anything observed. Then add the cross-reference ("@fig-lie-cues-belief-gap plots the gap"). This is a surprise-then-resolution beat that currently exists only inside an SVG.  *(effort: small)*

### [HIGH · structure] Optional extension: search safely after agreement, line 206

> Optional extension: search safely after agreement

**Problem.** @tbl-agreement-module-routing promises five routed modules, but the chapter delivers four numbered H2 modules; the fifth ("Protected post-settlement search") is demoted to an H3 buried inside module 4, and a sixth topic (third-party processes) appears as an unnumbered research-lens callout also inside module 4 and titled "Optional module: when direct negotiation needs a third party." A reader who uses the routing table as instructed by the Practice Lab ("Choose no more than one optional module from @tbl-agreement-module-routing") cannot find two of the five rows as modules, and module 4's section silently contains three separate topics.

**Edit.** Renumber to match the table row-for-row: module 1 packages, module 2 contingent terms, module 3 staged disclosure and verification, module 4 process and third-party rules, module 5 protected post-settlement search. Promote "search safely after agreement" to "## Optional module 5: Search safely after agreement" as its own H2 after module 4 ends, and either promote the third-party callout to its own H2 (keeping the research-lens styling inside it) or retitle it so it does not claim the word "module" while sitting inside another module's section. Keep the existing []{#third-party-dispute-resolution} anchor wherever the content lands.  *(effort: medium)*

### [HIGH · visual] Optional module 2: Use contingent terms when forecasts differ, line 107

> Four agreement-design tools and the conditions that make each useful.

**Problem.** The chapter's only conceptual figure covers all four optional tools (its SVG title is "Choose an agreement tool for the problem"; its panels are MESOs, contingent terms, post-settlement search, and governance) but it is parked under the module 2 heading, after module 1 has already been taught and before three of the four panels have been introduced. It also duplicates @tbl-agreement-module-routing, which sits 37 lines earlier and makes the same routing argument, so the reader meets the same map twice in two formats without being told they are the same map. The caption labels the contents instead of stating a claim.

**Edit.** Move the figure to immediately follow @tbl-agreement-module-routing inside (or directly after) the "Add an advanced module only for a diagnosed problem" callout, and make it the visual index for the module sequence that follows — the table gives the decision rule, the figure gives the conditions. Recaption as a claim, e.g. "Each tool answers one diagnosed problem; added without that problem, it buys interpretation, monitoring, and gaming costs instead of protection." Keep the existing "Use @fig-agreement-design to check…" sentence with it, and delete the duplicated routing content from whichever of the two you decide is secondary.  *(effort: medium)*

### [HIGH · visual] Turn the supplier package into operating rules, lines 230–245

> The illustrative priority map below helps the parties question the proposed terms

**Problem.** The sentence says "below," but @tbl-34-1 is fifteen lines away: between the pointer and the table sit a blank gap, a 130-word implementation paragraph, and the chapter's concluding six-fields claim. The table is never cross-referenced with @tbl-34-1, so it renders after the chapter's closing sentence as an unexplained appendix, and its generic rows (Price / Delivery / Payment timing / Service level / Contract length) never connect to the supplier case the surrounding prose is resolving.

**Edit.** Move the table so it sits directly under its introducing sentence, cite it explicitly ("@tbl-34-1 maps the issues…"), and let the six-fields paragraph be the last thing in the section. Rename the id from the stale tbl-34-1 to tbl-agreement-priority-map to match the chapter's other ids. Then repopulate at least two rows with the chapter's own case (call-off band, surge price) so the map illustrates the agreement being designed rather than a generic deal.  *(effort: small)*

### [MEDIUM · accuracy] Optional module 1: Reveal priorities through packages, line 89

> Research comparing MESOs with single-package offers has found economic

**Problem.** A single paper is presented as a body of research ("Research comparing… has found"), with no design, no magnitude, and no boundary condition — in a chapter that elsewhere hedges meticulously. The claim as written cannot be checked or bounded by a reader: "economic and relational benefits" could mean anything, and the paper's own framing (MESOs as a way to make a *first offer* without the usual dilemma) is lost.

**Edit.** Attribute it precisely and give one number: state that Leonardelli and colleagues (2019) report a series of experiments in which negotiators making a MESO first offer obtained better economic outcomes than those making an equivalent single first offer while counterparts reported greater satisfaction, and quote one reported magnitude from the paper. Add the boundary condition the chapter already believes: these are controlled negotiations with prepared packages, and the relational benefit depends on the packages being sincere and genuinely near-equivalent — which is why the following paragraph's decoy warning matters.  *(effort: small)*

### [MEDIUM · clarity] Culture changes the meaning of a move, line 143

> including differences across settings in how common measures predict joint gains

**Problem.** This clause has to be reread and still yields nothing usable. "Common measures" is undefined, "predict joint gains" is unexplained, and the sentence carries two citations while making no statement a reader could act on or disagree with. It is the only evidential content in an otherwise vivid section about "yes" meaning three different things, so the section's hedge is where its substance should be.

**Edit.** Replace with the concrete finding. Brett and Okumura (1998) compared U.S. and Japanese negotiators in intracultural and intercultural dyads and found lower joint gains in the intercultural pairs, tracing this to differences in information exchange and in what each side assumed about priorities. Say that, then use Brett et al. (2021) for the second, more interesting point: the negotiation strategies that predict joint gains are not the same everywhere, which is precisely why the Meaning Audit questions that follow are asked rather than assumed. One concrete sentence plus one generalization beats two abstractions.  *(effort: small)*

### [MEDIUM · consistency] References cited in this chapter, lines 303 and 335

> Köhnken, G. (1988). *Glaubwürdigkeit* [Credibility].

**Problem.** Two reference entries — Köhnken (1988) and Zuckerman, Koestner, and Driver (1981) — have no in-text citation anywhere in the chapter. They are not errors: the figure's own SVG footer credits them as the source of the belief estimates ("belief estimates reported there from Zuckerman et al. (1981) and Köhnken (1988)"). But that attribution lives only inside the image, so a reader of the .qmd caption and reference list sees two entries with no visible provenance, and the EPUB/alt-text path never surfaces them at all.

**Edit.** Extend the @fig-lie-cues-belief-gap caption so the attribution is in the document text, not only in the drawing: "…Redrawn from Sporer and Schwandt (2007), Figure 1; the belief estimates reported there come from Zuckerman et al. (1981) and Köhnken (1988)." That makes both entries cited and matches the chapter's practice of naming sources for every number it shows.  *(effort: small)*

### [MEDIUM · consistency] Replace lie detection with claim verification, line 163

> [Communication Is Joint Inference](33-communication-language-is-not-a-file-transfer.qmd)

**Problem.** The link text names a chapter title that no longer exists. Chapter 33's actual title is "Communication: Language Is Not a File Transfer"; "Communication Is Joint Inference" is the retired name preserved only in that file's alias (28-communication-is-joint-inference.html). The two sibling links in the same sentence use correct current titles, so the error reads as a real book with one stale label. (The adjacent claim at line 139 that "Chapter 33 distinguished perspective-taking from perspective-getting" is correct — chapter 33 does exactly that at its line 118 — so only the title needs fixing.)

**Edit.** Change the link text to "Communication: Language Is Not a File Transfer" (or "Language Is Not a File Transfer" for length), keeping the same target path. This is the only occurrence of the retired title in any chapter file.  *(effort: small)*

### [MEDIUM · engagement] Optional module 2: Use contingent terms when forecasts differ, line 111

> Suppose a builder expects early completion while a buyer fears delay.

**Problem.** The module that teaches contingent contracts — the chapter's most vivid tool, where real money changes hands on a measured outcome — runs entirely on "a builder," "a bonus for finishing early," and "a vague 'successful launch'." No bonus size, no day count, no case. The measurement-gaming warning that follows ("speed cannot be achieved by omitting quality checks") would land far harder attached to a contract where someone actually earned the bonus.

**Edit.** Anchor the module in one documented incentive contract with published numbers. The Caltrans rebuild of the I-10 Santa Monica Freeway after the January 1994 Northridge earthquake is the canonical teaching case: a per-day early-completion bonus paired with per-day liquidated damages, and a contractor who finished far ahead of the scheduled date and collected a multimillion-dollar bonus — verify the exact day count and bonus figure against Caltrans/FHWA sources before printing them. Then reuse that case for the two cautions already in the paragraph: what "complete" was defined to mean, and who verified the date. Two sentences of named case will do more for this module than the whole abstract paragraph.  *(effort: medium)*

### [MEDIUM · insight] Add an advanced module only for a diagnosed problem (callout), line 72

> If no diagnosed problem fits a module, do not add one.

**Problem.** This is the chapter's most counterintuitive and most useful claim — a negotiation chapter telling the reader that the clever tools are usually the wrong answer — and it is the last line inside a collapsible-looking tip callout, delivered in two flat sentences. Everything after it (four-plus modules of technique) pulls the other way, and the closing section never returns to the restraint rule, so the chapter's structure argues against its own thesis.

**Edit.** Promote it. Add the restraint claim to the Core Idea as its own sentence (the Core Idea currently says only that tools "should answer a diagnosed need" — say instead what an undiagnosed tool costs). Then pay it off in the closing section: name the specific price of each module added without a diagnosis — a MESO without priority uncertainty leaks your own valuations; a contingent term without a controllable, verifiable measure imports a future dispute into a signed contract; an arbitration clause without a finality need surrenders outcome control the parties wanted to keep. That turns a rule into an argument the reader will remember.  *(effort: small)*

### [MEDIUM · insight] Chapter epigraph, line 11, and closing paragraph, line 236

> Covenants, without the Sword, are but Words, and of no strength

**Problem.** The Hobbes epigraph sets up the chapter's real thesis and is then never mentioned again. The closing ("A deal is not complete when it looks clever on paper") states the practical version but leaves the sharper point implicit: the six fields *are* the sword, privately constructed — measurement, verification, and exit are what give a promise force without invoking a court. The chapter stops one step short of its own frame.

**Edit.** Close the loop in two sentences at the end of "Complete the minimum agreement": the six fields are what a private covenant has instead of a sword, and the corollary is uncomfortable — a clause no one will ever measure, check, or act on fails Hobbes's test no matter how carefully it was drafted. That also gives the reader a test to apply to their own contracts: for each material promise, name who would notice the breach and what they would do next.  *(effort: small)*

### [MEDIUM · structure] Practice Lab, line 251

> belong in an advanced agreement-design file, not in the minimum exercise

**Problem.** The Practice Lab defers the advanced work to "an advanced agreement-design file" that does not exist anywhere in the manuscript — the phrase appears nowhere else in the repo. The material it describes does exist: Appendix C contains a "Package and Contingency Worksheet" (MESOs plus contingent terms) and "Mediation and Arbitration Are Different Choices," neither of which this chapter ever links. Chapters 07 and 41 link to Appendix C tools by anchor, so the convention exists and this chapter is the outlier. A second problem: "the supplier obligation most likely to fail" does not say whose supplier — the chapter's case or the reader's own.

**Edit.** Replace the phantom file with real links: "…belong in the [Package and Contingency Worksheet](../appendices/appendix-c-portable-course-tools.qmd#tool-…) and [Mediation and Arbitration Are Different Choices](…), not in the minimum exercise." Add the missing anchor ids in Appendix C if needed. In the first line, say explicitly which obligation to use — "the supplier obligation in this chapter's case, or one from an agreement you are responsible for" — so the exercise is doable by a student without a live contract.  *(effort: small)*

### [LOW · structure] Complete the minimum agreement: implementation and review, lines 216–222

> Complete the minimum agreement: implementation and review

**Problem.** The H2 announces implementation and review, but its first H3 is "Ethics of value creation" — two short paragraphs on making costs visible and preserving meaningful refusal, which is neither implementation nor review. The reader arrives expecting the promised close-out of the six fields and gets an ethics aside first; the actual implementation content sits in the next H3.

**Edit.** Either retitle the H2 to cover both ("Close the agreement: ethics, implementation, and review") or move the ethics H3 to sit before this section as its own H2, so the closing section runs straight from the supplier case into the six-field summary without a topic detour. The two ethics paragraphs are good — the "ask each side to explain the failure rules in its own words" test is one of the chapter's best moves — and would read as a stronger beat if they were not filed under implementation.  *(effort: small)*

---

## `chapters/39-behavior-design-make-the-better-action-easier.qmd`  (18 findings)

### [HIGH · accuracy] Optional tools for a diagnosed bottleneck (precommitment paragraph), line 107

> Examples include automatic savings, self-imposed or externally structured deadlines, app blockers

**Problem.** This contradicts the book's own carefully documented position. Chapter 19 states that Ariely and Wertenbroch (2002) — the study behind the self-imposed-deadline recommendation — was retracted on 2 September 2026, that a direct replication found negligible deadline effects, and explicitly that "the original study should not support a recommendation to impose deadlines." Chapter 39 then lists self-imposed and externally structured deadlines as a precommitment example with no caveat, no citation, and no cross-reference, in a manuscript whose integrity standard is to bold retractions in reference lists.

**Edit.** Remove deadlines from the example list, or keep them with the qualification the book has already earned: note that the best-known evidence for self-imposed deadlines has been retracted and a direct replication found negligible effects, so deadlines should be treated as an untested commitment device rather than a demonstrated one, and link to [Chapter 19](19-intertemporal-decision-making-why-later-loses-to-now.qmd) and Appendix F. Handled well, this is a chance to model the book's own update discipline inside the applied chapter; left as is, it is the one place where the manuscript recommends what it elsewhere retracts.  *(effort: small)*

### [HIGH · accuracy] Willpower is not one depletable fuel (callout), line 175

> has faced serious replication and measurement challenges (Hagger et al., 2016)

**Problem.** This boundary-conditions callout is thinner than the book's own Appendix F treatment of the same claim, and the link runs only one way. Appendix F gives the multilab result, adds the 36-site paradigmatic test (Vohs et al., 2021) and the multilab project that did find a small significant effect (Dang et al., 2021), and cross-links *to* Chapter 39 — while Chapter 39 names one study, no numbers, and never points back. A reader of the chapter alone cannot tell whether "challenges" means "contested" or "near-zero in coordinated tests."

**Edit.** Give the callout the numbers and the two-sided evidence Appendix F already contains: 23 laboratories, roughly 2,141 participants, an estimated effect near zero with a confidence interval spanning zero (Hagger et al., 2016); a 36-site paradigmatic test finding a very small nonsignificant effect (Vohs et al., 2021); and one multilab project reporting a small significant effect (Dang et al., 2021). Close with a link to [Appendix F](../appendices/appendix-f-when-evidence-breaks.qmd) so the cross-reference is reciprocal, and keep the existing alternative-explanations sentence, which is good.  *(effort: small)*

### [HIGH · engagement] Optional tools for a diagnosed bottleneck (implementation intentions), line 97

> increased vaccination compared with a reminder without that planning field

**Problem.** The chapter's single applied field-experiment citation is stripped of every number, and the direction-only phrasing hides the result that makes the study worth citing. Chapter 40 describes the same study in the same numberless way ("increased vaccination relative to a reminder without that planning field"), so the book reports its clearest behavior-design evidence twice without a figure either time.

**Edit.** Give the published numbers and the contrast that carries the mechanism: roughly 3,272 employees at a large firm; the mailer asking for the planned date *and time* produced about 37.3 percent vaccination versus about 33.1 percent for the plain reminder (a 4.2-point gain), while the mailer asking only for a date added about 1.5 points and was not statistically significant. Verify against the PNAS paper before printing. The date-only null is the surprise — the planning field only worked when it forced a specific moment — and it is exactly the chapter's thesis about cue-linked plans, currently thrown away.  *(effort: small)*

### [HIGH · engagement] Research note: the ideas behind the workflow, line 60

> Research on implementation intentions, habits, and behavior-change maintenance supports planning

**Problem.** Implementation intentions are the chapter's most-used tool — three worked if-then examples, a row in @tbl-21-1, a required step in the Practice Lab, and a move inside the mini-case — yet the meta-analysis supporting them is cited once, inside a callout marked collapse=true (hidden by default in HTML), in a sentence that says only that research "supports planning." No effect size, no study count, no boundary condition appears anywhere in the chapter.

**Edit.** Move the evidence into open prose beside the if-then examples and state it: Gollwitzer and Sheeran's (2006) meta-analysis of 94 independent tests (roughly 8,000 participants) reported a medium-to-large average effect of about d = 0.65 on goal attainment. Then add the boundary condition the chapter needs in order to stay honest: the effect depends on the underlying goal commitment being real — an if-then plan for a goal the person does not hold does little — and estimates are smaller for behaviors needing sustained effort than for one-shot actions like showing up for a vaccination.  *(effort: small)*

### [HIGH · structure] Mini-case: the defensive meeting loop, lines 50 and 144

> What is the smallest change that directly addresses the diagnosed bottleneck?

**Problem.** The chapter's showcase worked example violates the chapter's own rule. Step 3 of @tbl-behavior-design-workflow requires "One change" and asks for the smallest change addressing the diagnosed bottleneck; the Practice Lab repeats it ("change one decisive point... no more than one primary tool"). The mini-case redesign then changes five things simultaneously — pre-named uncertainty, a new manager question, the project lead's implementation intention, an assigned summarizer, and a closing learning note — with no acknowledgment. A reader who follows the model rather than the rule will run an untestable bundle; a reader who notices will not know which instruction to trust.

**Edit.** Either stage it or name the exception, and the second is more interesting. State that a multi-person routine cannot be changed one lever at a time because each participant's behavior is another's cue — so organizational redesign trades diagnostic precision for feasibility, which is exactly why the measurement plan at line 146 has to carry more weight there than in personal design. Then identify which of the five changes addresses the diagnosed bottleneck (the manager's question, if the diagnosis is that a skeptical question cues defense) and mark the rest as supports. This converts an internal contradiction into the chapter's sharpest insight about the limits of its own workflow.  *(effort: medium)*

### [HIGH · structure] ## Practice Lab: behavior-design studio (inside .callout-tip .activity)

> ::: {.callout-tip .activity icon=false}

**Problem.** Chapters 39, 40 and 41 wrap the Practice Lab inside a .callout-tip .activity div, which turns the `##` heading into a callout title and removes it from the page table of contents. Verified against the built HTML in docs/: 'Practice Lab in TOC: False' for chapters 39, 40, 41 and True for chapter 38. In exactly the three chapters a practitioner is most likely to jump straight to the lab, the lab is unreachable from the sidebar.

**Edit.** Delete the callout wrapper in ch39:203-238, ch40:250-245, ch41:354-262 and leave `## Practice Lab` as a plain section, matching the other 39 chapters. Reserve .activity (renamed .mini-lab) for in-body exercises only — ch30:67, ch41:102, appendix-e:417, appendix-f:200.  *(effort: small)*

### [HIGH · visual] Mini-case: the defensive meeting loop, line 142

> a skeptical question cues a defensive reply, while explaining protects the project lead

**Problem.** Roughly 900 words run from the digital-loop table through organizational habits, the mini-case, habit design as power, fresh starts and identity, and relapse, with no figure, table, or callout — and the mini-case, the most diagrammable content in the chapter, is prose only. The chapter's whole argument is that a loop sustains itself through the immediate function of each move, and that argument is currently invisible: the reader has to hold six actors' moves in working memory to see the cycle.

**Edit.** Add a two-panel figure beside this paragraph. Panel A, the observed loop as a closed cycle of five nodes — skeptical question → heard as criticism → defensive explanation → others go quiet → manager escalates → (back to) skeptical question — with each arrow labeled by its immediate function for the person making the move ("protects standing now," "avoids conflict now," "seeks the missing information"), and a caption stating that nobody chose the routine yet each move is locally reasonable. Panel B, the same cycle with one arrow visibly interrupted and the replacement response on it ("Can you say more about the risk you are seeing?"), plus the measurement note: track whether concerns appear earlier, including concerns aimed at the manager. Caption as a claim, not a label. This also gives the section that currently runs longest without a visual its anchor.  *(effort: large)*

### [MEDIUM · accuracy] Research note: the ideas behind the workflow, line 60

> B=MAP describes motivation, ability, and a prompt converging at a behavioral moment

**Problem.** B=MAP is attributed to Fogg (2009), but the 2009 paper presents the model as B=MAT with "trigger" as the third factor; "prompt" is the later relabeling used in Fogg (2020), which the chapter also lists. The chapter's own epigraph quotes the 2009 paper saying "an effective trigger" while every other mention says prompt, so an attentive reader sees two different third factors with no explanation — and a reader who looks up Fogg (2009) will not find the acronym they were given.

**Edit.** Cite both editions at the naming ("Fogg, 2009, 2020") and add one clause where the epigraph's vocabulary is first reused: the 2009 model called the third factor a trigger, later renamed a prompt, with no change of meaning. One sentence removes the discrepancy and models the citation care the rest of the book shows. The §"Optional lens" paragraph at line 66 already cites both years correctly, so only the research-note sentence and a bridging clause need changing.  *(effort: small)*

### [MEDIUM · accuracy] Design an attention boundary, line 111

> Even the mere presence of one's phone can occupy cognitive capacity in some settings

**Problem.** "In some settings" is an unexplained hedge where the book's own standard is to name what failed. The brain-drain effect has drawn direct replication attempts that did not reproduce it, and the original result was moderated by self-reported smartphone dependence — neither fact appears here, and the effect has no Appendix F row (unlike watched eyes and ego depletion, which get full treatment). A reader cannot tell whether the hedge means "context-dependent" or "may not be real."

**Edit.** Say what the hedge is hiding in one sentence: the original studies found reduced available working memory when the phone was merely present, moderated by self-reported dependence, but direct replications have not consistently reproduced it (e.g. Hartmann et al., 2020; Ruiz Pardo & Minda, 2022 — verify and add to the reference list). Then keep the practical point, which does not depend on the lab effect: the boundary is justified by what the device actually does when it buzzes, not by a contested capacity result. Consider adding a row to Appendix F so the book's replication ledger stays complete.  *(effort: medium)*

### [MEDIUM · clarity] Research Lens: COM-B widens the diagnosis, line 80

> COM-B and B=MAP as complementary diagnostic lenses

**Problem.** The table merges rows from two frameworks without saying which row comes from which, so "Motivation" and "Ability now" read as near-duplicates of each other, and "Prompt" appears in a table introduced as COM-B's contribution. The caption calls them complementary but the table gives the reader no way to see how — the one real distinction (COM-B asks about standing conditions, B=MAP about one moment) is stated in the prose above and then discarded in the layout.

**Edit.** Add a leading column naming the source lens for each row (COM-B / COM-B / COM-B / B=MAP / B=MAP), and add one sentence under the table: COM-B asks whether the conditions for the behavior exist at all; B=MAP asks whether they converged at the moment the behavior was supposed to happen — which is why an unchanged answer on Capability but a failed Prompt sends the redesign somewhere completely different. Consider also adding a 2-axis B=MAP sketch (motivation on the vertical, ability on the horizontal, an action line, prompts landing above and below it), which would carry real explanatory load in a section that is currently all prose.  *(effort: medium)*

### [MEDIUM · clarity] One primary workflow, line 55

> implementation intentions, WOOP, friction changes, temptation bundling, and precommitment can support a selected redesign

**Problem.** Seven named frameworks (B=MAP, COM-B, implementation intentions, WOOP, friction changes, temptation bundling, precommitment) arrive in a single sentence, none defined, 9 to 52 lines before their explanations — WOOP is not unpacked until line 99. The sentence sits immediately after the workflow table, where a reader has just been told to spend effort on the diagnosed bottleneck, and it front-loads exactly the tool-shopping the chapter is arguing against.

**Edit.** Replace with a pointer rather than a list: "Two diagnostic lenses and six redesign tools appear later in the chapter; @tbl-21-1 pairs each tool with the bottleneck it addresses, and none of them should be chosen before Step 2 is complete." That preserves the signpost, removes seven undefined terms from the reader's working memory, and reinforces the diagnosis-first rule at the exact point where the reader is most tempted to skip it.  *(effort: small)*

### [MEDIUM · consistency] Optional tools for a diagnosed bottleneck, line 103

> Chapter 40 examines their mechanisms, boundary conditions, and ethics.

**Problem.** This chapter contains zero hyperlinked cross-references in a manuscript with 68 of them. "Chapter 40" (line 103) and "Chapter 21's classroom mnemonic" (line 199, inside a table cell) are bare numbers with no link, so in HTML and EPUB they are dead ends. Both numbers are correct — chapter 40 is choice architecture and chapter 21 does contain BRAIN — but the chapter also silently reuses chapter 19's temptation bundling and precommitment material and chapter 21's habit-loop material with no acknowledgment at all, and it never links Appendix C's "Behavior Redesign Canvas," which is the exact printable form of this chapter's Practice Lab.

**Edit.** Convert both bare references to linked titles in the style of chapters 07 and 41, e.g. [Choice Architecture](40-choice-architecture-the-environment-gets-a-vote.qmd) and [Chapter 21](21-habits-wanting-and-self-control.qmd#optional-practice-observing-an-urge-with-brain). Add a link to [Chapter 19](19-intertemporal-decision-making-why-later-loses-to-now.qmd) at the temptation-bundling and precommitment paragraphs, where that chapter established the present-bias reason these devices work. And point the Practice Lab at [Appendix C](../appendices/appendix-c-portable-course-tools.qmd#tool-behavior-redesign-canvas), which already carries the canvas the exercise describes.  *(effort: small)*

### [MEDIUM · engagement] Optional tools for a diagnosed bottleneck (temptation bundling), line 105

> initially increased visits compared with a control group given a bookstore gift certificate

**Problem.** "Initially increased" is a correct hedge doing the work a number should do, and the decay — which is the genuinely interesting finding and the evidence for the very next sentence about fragility — is compressed into one adverb. Chapter 19 cites the same study with the same absence of numbers, so the book's one temptation-bundling result is reported twice with no magnitude.

**Edit.** Report the published pattern: gym visits rose roughly 51 percent for the full-treatment group and about 29 percent for the intermediate condition relative to control in the early weeks, the advantage eroded over the intervention and did not survive the Thanksgiving break, and a majority of participants nonetheless chose to pay for gym-only access to the audiobooks at the end (verify all figures against the Management Science paper). That last result is the memorable one — people paid for a constraint they had watched stop working — and it is the chapter's best evidence that a bundle is a device, not a cure.  *(effort: small)*

### [MEDIUM · engagement] Fresh starts, identity, and social context, line 160

> A temporal landmark can also create a psychological “fresh start”

**Problem.** A memorable, data-rich finding is reduced to a definition with a citation. The paper's own evidence is exactly the kind of concrete instance the section needs and the surrounding paragraph is otherwise abstract for six sentences ("Stable contexts help cues retrieve practiced responses"; "A transition may therefore be a useful occasion").

**Edit.** Give one observed pattern from Dai, Milkman, and Riis (2014): searches for "diet," gym visits, and commitment-contract creation rise at the start of a new week, month, semester, and year, and after birthdays — landmarks that change nothing material but separate the person from a past self. Then add the caution the section needs and currently lacks: the evidence is about *initiation*, not maintenance, which is why the paragraph's own advice is to have the new routine ready to practice rather than to rely on the landmark.  *(effort: small)*

### [MEDIUM · structure] Take it forward, line 220

> Choose a recurring moment when an intention loses to the easier response.

**Problem.** "Take it forward" restates the Practice Lab in miniature — choose a moment, change one thing, observe, revise the diagnosis, add a lapse plan — which is Steps 1 through 5 compressed. It commits the reader to nothing they were not just assigned, and it returns to none of the chapter's own material. Chapters 41 and 42 close by returning to a named case (the hiring meeting, Flint); this chapter has two excellent candidates and uses neither.

**Edit.** Return to the opening scene and close the frame: the student whose laptop opens onto the inbox, or the Monday meeting where the skeptical question arrives. Then commit to something checkable — name the one condition you will change before the next occurrence, and the observation that would tell you the diagnosis was wrong rather than the design weak. That distinction (wrong diagnosis vs weak design) is the chapter's most transferable idea and currently appears nowhere in the closing.  *(effort: small)*

### [MEDIUM · visual] Research note: the ideas behind the workflow, line 57

> ::: {.callout-note .research-lens icon=false collapse=true}

**Problem.** @fig-behavior-design is placed before "## Learning goals" — only 2 of the book's 42 chapters do this; the other 40 place the first figure after the learning goals — and its single cross-reference in the entire chapter sits inside this collapse=true callout. In HTML the figure therefore appears with no adjacent explanation, and the sentence that explains it is hidden behind a disclosure the reader must click. The figure also duplicates @tbl-behavior-design-workflow's five steps while sitting 21 lines away from it.

**Edit.** Move the figure below the learning goals and next to @tbl-behavior-design-workflow, so the visual and the required-output table are read together, and add one open-prose sentence cross-referencing it ("@fig-behavior-design shows the loop the table records: review can send you back to diagnosis, and a lapse can send you back to the goal"). Keep the collapsed research note for the framework provenance, which is the right use of a collapse. Also recast the caption from a list of steps to a claim — the figure's real content is that the arrow runs backwards as often as forwards.  *(effort: small)*

### [LOW · accuracy] Optional tools for a diagnosed bottleneck (WOOP), line 99

> supports modest average gains in goal attainment relative to control conditions

**Problem.** "Modest average gains" is the third consecutive evidence claim in this section given without a magnitude, and the citation is to a meta-analysis whose pooled estimate is available. The sentence also says gains are relative to "control conditions without the combined exercise" — correct but unhelpfully circular — and the promised "variation across goals and settings" is asserted rather than specified.

**Edit.** Report the pooled effect size and study count from Wang, Wang, and Gai (2021), and say what moderated it (goal domain, and whether the comparison condition included any planning at all). If the pooled estimate shrinks in the higher-quality or preregistered subset, say so — that is the kind of detail this manuscript reports elsewhere and it protects WOOP from being read as equivalent in strength to implementation intentions, which have a much larger evidence base.  *(effort: small)*

### [LOW · consistency] References cited in this chapter, line 250

> Gollwitzer, P. M. (1999). Implementation intentions: Strong effects of simple plans.

**Problem.** This entry has no in-text citation anywhere in the chapter; only Gollwitzer and Sheeran (2006) is cited. The book's reference lists are otherwise tightly matched to in-text citations, so an uncited entry reads as an oversight.

**Edit.** Cite it where it belongs — at line 97, where the if-then structure is first defined, since the 1999 paper is the canonical statement of the construct — or remove the entry. Citing it is preferable: it gives the definition a source and separates the construct (Gollwitzer, 1999) from the evidence for it (Gollwitzer & Sheeran, 2006), which is the distinction the chapter is implicitly making.  *(effort: small)*

---

## `chapters/40-choice-architecture-the-environment-gets-a-vote.qmd`  (17 findings)

### [HIGH · accuracy] ### Set the starting point: defaults and active choice (line 114)

> Organ-donation consent is highly sensitive to default format

**Problem.** Two problems. (a) Johnson & Goldstein's cross-country comparison of effective consent rates is observational; countries differ in registries, family-veto law, and transplant infrastructure. "Highly sensitive to default format" reads as a causal claim about the country data, and it is notably less careful than Chapter 1's own wording on the same study ("found large differences in stated agreement across online experimental defaults"). (b) Chapter 1 already cites Dallacker et al. (2024), a longitudinal analysis of five countries that switched from opt-in to opt-out and found no average increase in deceased donation — and Chapter 1 explicitly forward-links to this exact section. The reader who follows that pointer arrives at weaker, older evidence than they just left, in a book whose whole character is to foreground disconfirming follow-ups.

**Edit.** Rewrite as: stated consent in Johnson and Goldstein's online experiment roughly doubled under opt-out (about 82% versus 42%), and registered consent across European countries ranges from around 12% in opt-in Germany to 99.98% in opt-out Austria — but that country comparison is observational. Then add the Dallacker et al. (2024) sentence and citation already used in Chapter 1: across five countries that actually switched policy, deceased-donation rates did not rise on average. Add Dallacker et al. (2024) to this chapter's reference list. This turns a vague sensitivity claim into the chapter's best worked case of a default that moves a registry number without moving the outcome that matters.  *(effort: medium)*

### [HIGH · clarity] ### Construct the menu: options, order, and overload (line 90)

> the visible benefit of one option can crowd out the cost of the path displaced by it

**Problem.** The sentence needs rereading: "the cost of the path displaced by it" is an abstraction stacked on an abstraction, and it is the only support given for an idea (opportunity-cost neglect) that the chapter elsewhere treats as foundational. Frederick et al.'s actual experiment is a one-line manipulation with a large, memorable effect, and it is exactly the kind of worked instance the chapter otherwise asks designers to produce.

**Edit.** Replace the sentence with the study itself: when the alternative to buying a $14.99 video was described as "keep the $14.99 for other purchases" rather than simply "do not buy," the share choosing to buy fell from about 75% to about 55% — seven added words changed one purchase decision in five. Then state the design rule in plain terms: a menu that names only what you get, never what you give up, is not a neutral menu.  *(effort: small)*

### [HIGH · engagement] ### Construct the menu: options, order, and overload (line 86)

> a large display attracted attention, while a smaller display produced more purchases

**Problem.** The single most famous demonstration in the choice-overload literature is reported with no numbers at all. "Attracted attention" and "more purchases" conceal a 10-to-1 result that is the whole reason the study is famous, and the sentence as written is unfalsifiable and forgettable. The later hedging sentence about moderators is excellent and should stay — but it currently hedges a finding the reader was never shown.

**Edit.** Insert the published figures: the Draeger's display offered 24 jams versus 6; about 60% of passers-by stopped at the large display versus 40% at the small one, but only 3% of those who stopped at the 24-jam table bought, against 30% at the 6-jam table — ten times the conversion from a quarter of the options. Then keep the existing Scheibehenne/Chernev hedge and add the meta-analytic punchline (mean effect near zero, with overload appearing only under the listed moderators), so the reader gets surprise-then-resolution rather than an unquantified anecdote.  *(effort: small)*

### [HIGH · engagement] ### Set the starting point: defaults and active choice (line 114)

> Automatic enrollment substantially increased participation in one large 401(k) plan

**Problem.** "Substantially increased" is the vaguest possible reporting of the most quantitatively striking result in the entire nudge literature, and it sits in the chapter whose opening puzzle is a retirement form. The chapter also omits the second, more surprising half of Madrian & Shea's finding — that automatic enrollment does not merely raise participation, it freezes people at whatever contribution rate and fund the designer picked, which is the strongest possible argument for the governance questions the chapter raises two paragraphs earlier about smart defaults.

**Edit.** Replace with the published numbers: 401(k) participation among newly hired employees rose from about 37% under opt-in to about 86% under automatic enrollment — and roughly three-quarters of automatically enrolled participants stayed at both the default 3% contribution rate and the default money-market fund, a rate and fund most would not have chosen deliberately. Add one sentence drawing the moral the chapter needs: the default did not just increase action, it also chose the amount and the portfolio. Do the same for Carroll et al. (2009): active-decision designs raised participation roughly 28 percentage points over standard opt-in at three months of tenure.  *(effort: small)*

### [HIGH · engagement] ### Treat every intervention as a hypothesis (line 204)

> Mertens et al. (2022) reported an average behavioral effect across diverse choice-architecture studies

**Problem.** This is the most dramatic evidentiary reversal in the chapter — a headline meta-analysis in PNAS, and a reanalysis in the same journal finding the effect vanishes under publication-bias correction — and it is told entirely without numbers, so the surprise dies on the page. "An average behavioral effect" and "no clear average effect" give the reader nothing to hold or compare. A reader cannot tell whether the dispute is between 0.43 and 0.38 or between 0.43 and 0.

**Edit.** State both magnitudes: Mertens et al. reported an average effect of about d = 0.43 across 447 effect sizes; Maier et al., applying PET-PEESE and Bayesian model-averaged bias correction to the same data, found the estimate collapse to approximately zero with no evidence for an average effect once small-study effects were modeled. Add one sentence on what a reader should conclude (the domain averages are uninformative; the design-and-setting-specific evidence is what counts), which is the point the chapter already wants to make and would now be earned.  *(effort: small)*

### [HIGH · structure] ## Practice Lab: architecture autopsy and redesign

> In groups, document one real choice path from first cue to feedback.

**Problem.** This is the thinnest Practice Lab in the book — one paragraph, group-only, no named artifact, no success check — in the chapter whose subject (defaults, friction, exit) is the one a solo reader can most easily audit on a service they used yesterday. Seven other labs are also partner- or group-gated with no solo path: ch24 ('Run five rounds of the two-thirds number game'), ch25 ('then four announced rounds with the same partner'), ch36 ('Run the used-car negotiation in pairs'), ch37 (each side allocates points), ch34 ('An observer marks any sentence that crosses'), ch32 ('Peer feedback identifies one unsupported inferential jump'), ch42 ('Give two people the same case').

**Edit.** Give each a solo default with the group version as an explicit extension. Full rewrites naming input, steps, output artifact, success check and time are in chapter_notes Part 2 (items 1-8). For ch40 specifically: audit one subscription or enrolment flow you used this month, label every step with one of the seven architecture terms, mark the decisive step, write 'Changing X should affect Y because mechanism Z', name one alternative instrument and one harm measure. 35 minutes.  *(effort: large)*

### [HIGH · visual] ### An arrow that changed the action path (lines 160-166)

> In 2012, Google added a clickable right-pointing arrow

**Problem.** The chapter's weakest evidence receives its strongest treatment. A corporate blog post with no effect size, no control, and no isolation of the arrow from the bundled typography changes gets its own ### section, its own heading asserting the arrow "changed the action path," and a dedicated SVG figure — while Madrian & Shea, Johnson & Goldstein, and the Mertens/Maier dispute get no visual at all. The footnote hedge is admirable but cannot undo a section heading that states the causal claim the footnote retracts. The passage also restates Chapter 1's version almost verbatim while Chapter 1 promised this section would return to the case "as a design problem" — a development that never arrives.

**Edit.** Retitle the section to something the evidence supports (e.g. "A bundled redesign and what it cannot show") and make the heading's own claim the teaching point: this is what an uninterpretable result looks like. Then deliver Chapter 1's promise by adding two or three sentences of actual design analysis — what a clean test would have randomized, which outcome (clicks) is the platform's metric rather than the user's, and how it connects to the "Audit the platform's metric against the user's objective" paragraph 30 lines later. Separately, consider demoting or shrinking fig-digital-arrow-affordance and spending that visual budget on the defaults evidence instead.  *(effort: medium)*

### [MEDIUM · clarity] ## From behavior design to choice architecture, tbl-35-policy-tools (line 58)

> Boost | The person's competence | Teach natural frequencies or negotiation preparation

**Problem.** "Boost" is introduced as one of six headline instruments in a comparison table, is used again at line 208 ("including a boost, an incentive, service redesign"), and appears in Learning goal 2 — but is never defined in prose and carries no citation anywhere in the chapter. Every other instrument in the table is either self-explanatory or developed in the surrounding text. A reader who does not already know the nudge-versus-boost debate will not learn from this chapter what a boost is, why it is a distinct research program, or why its central claim (transfer beyond the environment) differs from a nudge's.

**Edit.** Add two sentences after the table: a boost aims to build a competence the person keeps — reading natural frequencies, using a simple decision rule, preparing a negotiation — so that it works after the designed environment is gone, whereas a nudge works only while the environment holds. Cite Hertwig and Grüne-Yanoff (2017) and add the entry to the reference list. Then tie it to the existing "Will the skill transfer beyond this environment?" column, which currently poses a question the text never helps the reader answer.  *(effort: small)*

### [MEDIUM · consistency] ## References cited in this chapter (lines 296-298, 312-314)

> Milkman, K. L., Minson, J. A., & Volpp, K. G. M. (2014). Holding the Hunger Games hostage

**Problem.** Two entries in a list headed "References cited in this chapter" are never cited in this chapter. Milkman et al. (2014) on temptation bundling appears nowhere in the body — the chapter cites Milkman et al. (2011) on flu-shot planning prompts, and temptation bundling is handled in chapters 19 and 39, where the same entry already appears. Thaler (1985) is likewise uncited here; mental accounting is handled by a chapter link to 20, where the entry also already appears. Additionally, the list is not in a single alphabetical sequence — it runs Chernev-to-Thaler, restarts at Allcott, and then appends Maier at the end — which makes a reader hunting for a source scan three times.

**Edit.** Delete both orphan entries, or cite them in the body if they are wanted (temptation bundling would fit the commitment-device sentence at line 168). Then re-sort the whole list into one alphabetical sequence. Worth a quick scripted check of the same two directions across all 42 chapters, since the three-block ordering pattern suggests entries were appended over time rather than merged.  *(effort: small)*

### [MEDIUM · engagement] ### Support action at the right moment (line 168)

> increased vaccination relative to a reminder without that planning field

**Problem.** Milkman et al. (2011) is reported without its effect size, and — more costly — without the contrast that makes it scientifically interesting. The study ran two planning prompts, and only one worked. Omitting that turns a precise finding about which planning detail matters into a generic endorsement of "add a planning field."

**Edit.** Add: writing both the date and the time of an intended clinic visit raised vaccination from 33.1% to 37.3% (+4.2 percentage points); writing the date alone raised it by only about 1.5 points, not reliably different from the plain reminder. Follow with the sentence the chapter has earned: the specificity of the plan, not the presence of a planning box, carried the effect. Also add Thaler & Benartzi's published numbers a few lines later — 78% of those offered joined Save More Tomorrow, and participants' average saving rate rose from 3.5% to 13.6% across four pay raises.  *(effort: small)*

### [MEDIUM · engagement] Opening puzzle: the form that already chose (line 22)

> Imagine enrolling in a retirement plan.

**Problem.** The chapter opens with an invented hypothetical containing no organization, no date, no person, and no stakes — in a chapter that happens to possess one of behavioral science's most vivid real numbers about exactly this form. Three paragraphs pass (the prefilled field, the reversed subscription/travel/warranty examples) before any reader is given a reason to care, and all of them are generic. The opening also states the abstract lesson ("Every environment does") before any instance has made it felt.

**Edit.** Open on the real case with the real number: a single large US employer switched its 401(k) from opt-in to automatic enrolment, changed nothing about the fund menu, the match, or the paperwork, and participation among new hires went from roughly 37% to roughly 86% — then note that most of those newly enrolled employees were still sitting at the designer's default 3% rate years later. Follow with the reversed examples already written. The abstract framing question at the end of the section then lands on a reader who has seen the stakes.  *(effort: medium)*

### [MEDIUM · engagement] ### Simplification, friction, and sludge (line 150)

> Simpler benefit notices increased take-up of an earned-income tax credit

**Problem.** Two of the strongest field experiments in the administrative-burden literature are reported with no magnitudes, in a paragraph that immediately afterwards tells readers a sludge audit should "count time and steps." The chapter asks for quantification while modeling its absence. The Bettinger et al. sentence does preserve the crucial null (information without assistance did not work), which is good — but the reader has no sense of whether the assistance effect was worth the program cost.

**Edit.** Add magnitudes from both papers, verifying against the published tables: for Bhargava and Manoli, the original IRS notice produced roughly 22% response among eligible non-claimants and the simplified notice raised it by several percentage points; for Bettinger et al., hands-on FAFSA assistance plus personalized aid information raised college enrollment among high-school-senior participants by roughly 8 percentage points, while personalized information alone produced no detectable gain. The contrast between the two arms is the memorable result and is already half-stated.  *(effort: small)*

### [MEDIUM · structure] ::: Practice Lab: architecture autopsy and redesign (line 253)

> In groups, document one real choice path from first cue to feedback.

**Problem.** This Practice Lab is markedly vaguer than its neighbours. Chapter 39 specifies a one-page record keyed to a named table; chapter 41 gives eight numbered stages, a stated deliverable ("the completed pipeline, not an essay"), and an explicit short form for low-stakes cases. This lab names no time box, no artifact, no group size, no worked format, and ends on a discussion question rather than an output. "Document one real choice path" gives a student no way to know when they are finished or what to hand in.

**Edit.** Give it the same skeleton the chapter already teaches: a one-page path map with seven labeled rows (menu, default, mapping, friction, timing, social information, exit), each row recording what the designer currently does and one proposed change; then the one-sentence causal claim already asked for; then one alternative instrument drawn from tbl-35-policy-tools; then one harm measure and who would report it. State the deliverable explicitly ("the submitted artifact is the completed path map") and the time box. The chapter's own two worked examples, missed appointments and cancellation sludge, can serve as the model answer.  *(effort: medium)*

### [MEDIUM · structure] ## Take it forward (line 260)

> Follow the choice path as the person using it would

**Problem.** This "Take it forward" restates the chapter's method in the abstract rather than committing the reader to anything. Compare chapter 39 ("Choose a recurring moment when an intention loses to the easier response. Make one feasible change to that moment, observe what happens"), chapter 38 ("Return to the term in your agreement most likely to become disputed"), and chapter 42 ("Choose one recurring decision this week"). Those name a target, an action, and a horizon; this one names none, so the chapter's strongest practical instrument — the symmetry test — goes unused at the moment the reader is most likely to act.

**Edit.** Commit the reader to a specific object and a specific test: name one service you currently pay for, and this week time how long joining took versus how long leaving takes; then apply the symmetry test already stated at line 144 and write down which of the ten audit questions in tbl-35-ethics that service would fail. That converts the chapter's own apparatus into a two-minute action with an inspectable result.  *(effort: small)*

### [MEDIUM · visual] Figures and tables throughout (lines 68, 126, 148, 166; tables 62, 228)

> Five questions locate possible problems in the objective, menu, understanding, action, and feedback.

**Problem.** Neither chapter 40 nor 41 contains a single @fig- or @tbl- cross-reference, although chapters 38, 39, and 42 use them (e.g. "complete the one-page record in @tbl-behavior-design-workflow"). Every figure and table here floats: nothing in the body text tells the reader to look at it, when, or what to take from it. fig-choice-architecture in particular duplicates the numbered list directly beneath it without either acknowledging the other, so the reader cannot tell whether the figure is the list or something additional.

**Edit.** Add body cross-references at the paragraph each visual serves: "@fig-choice-architecture sets out the five questions in order"; "Compare the instruments in @tbl-35-policy-tools before choosing one"; "@fig-mpg-fuel-use shows why the unit, not the arithmetic, is doing the work"; "Run the ten tests in @tbl-35-ethics against the design." This costs one clause each and brings the chapter into line with its neighbours.  *(effort: small)*

### [MEDIUM · visual] ### Use social information carefully through ### Treat every intervention as a hypothesis (lines 170-214)

> Behavioral effects are heterogeneous. An average effect may conceal strong benefit

**Problem.** About 1,100 words of continuous prose run from fig-digital-arrow-affordance to the ethics table with no figure, no table, and only a single indented block quote to break it. This stretch carries the chapter's most consequential material — norm boomerangs, feedback decay, platform governance, and the Mertens/Maier/DellaVigna evidence dispute — and it is also the densest, least illustrated part of the chapter.

**Edit.** Add one figure beside the "Treat every intervention as a hypothesis" paragraph: a single horizontal dot-and-interval chart, one row per estimate, x-axis "reported effect," showing (1) Mertens et al. pooled d = 0.43, (2) Maier et al. bias-adjusted estimate at approximately 0, (3) DellaVigna & Linos nudge-unit average 1.4 percentage points on a 17.4% baseline, and (4) the academic-journal comparison at 8.7 points, with the second axis clearly labeled so the two metrics are not conflated. Caption it with the takeaway, not the label: "The same literature yields a moderate effect, no effect, or a small one, depending on whose studies are counted and how publication bias is modeled." This is the chapter's thesis rendered in one image.  *(effort: large)*

### [LOW · consistency] line 92, personal-example callout title

> ### Ask, do not merely tell—but define the real choice

**Problem.** Three callouts use a `###` title where the other 157 use `##`: ch40:92 (.personal-example), ch28:93 (bare note), ch27:260 (.research-lens). Quarto renders the first heading in a callout as its title regardless of level, so this is invisible in output but makes the source inconsistent and will break any future script that extracts callout titles by matching `^## `.

**Edit.** Normalise all three to `##`. Then a single grep pattern reliably enumerates every callout title, which is what the taxonomy migration in chapter_notes will need.  *(effort: small)*

---

## `chapters/41-decision-hygiene-build-a-process-that-can-learn.qmd`  (19 findings)

### [HIGH · accuracy] ## During the decision: structure disagreement (line 192)

> In a before-and-after study of eight hospitals, Haynes et al. (2009) observed lower complication

**Problem.** The "before-and-after" framing is exactly the right hedge and should stay — but the chapter stops there. The surgical safety checklist has a large, well-known, directly relevant failed scale-up: Urbach et al. (2014, NEJM) examined mandated implementation across 101 Ontario hospitals and found no significant reduction in 30-day mortality or in complications. In a book whose Appendix F systematically documents failed replications and whose reference lists bold retractions, omitting the single most famous null in the decision-hygiene toolkit is out of character, and it leaves the chapter's own advice ("treat every intervention as a hypothesis," per chapter 40) unapplied to its own recommended tool. The Haynes numbers are also missing.

**Edit.** Give the numbers and the reversal: Haynes et al. observed inpatient death fall from 1.5% to 0.8% and complications from 11.0% to 7.0% across eight hospitals before-and-after; Urbach et al. (2014), studying mandated adoption in 101 Ontario hospitals, found no significant change in mortality or complications. Then draw the conclusion the chapter is already positioned to make and which strengthens rather than weakens its case: a checklist is not a talisman, and the conditions listed in this very sentence — short, at a useful pause, tied to a known failure, and actually used rather than merely mandated — are what distinguish the two results. Add the Urbach entry to the reference list.  *(effort: medium)*

### [HIGH · consistency] ## The structured judgment pipeline, fig-structured-judgment-pipeline (line 75)

> A structured judgment workflow connects definition, decomposition, independent assessment, aggregation, recording, and review.

**Problem.** The figure and the text disagree about the chapter's central workflow. The SVG contains exactly six labeled boxes (Define the decision, Separate the criteria, Judge independently, Compare and combine, Decide and record, Review the result) and the caption and alt text both say six. The numbered list immediately beneath has eight steps, adding "Ground" (base rates and reference classes) and "Challenge" (premortem, red team) — and both omitted stages have their own full body sections later. The Practice Lab then says "complete all eight stages," and its low-stakes short form is "define → challenge → decide → review," which requires a stage that does not exist in the figure at all. A reader who learns the pipeline from the diagram will be missing the outside view and the premortem.

**Edit.** Add two boxes to figures/structured-judgment-pipeline.svg — "Ground the estimate" (subtitle: start from base rates or a transparent baseline) between Separate the criteria and Judge independently, and "Challenge" (subtitle: premortem, red team, what would change our minds) between Compare and combine and Decide and record. Update the caption to name all eight and the alt text from "Six steps" to "Eight steps." Then add the missing @fig- cross-reference in the lead-in sentence at line 73 so the list and figure are explicitly bound to each other.  *(effort: medium)*

### [HIGH · engagement] ## Why judgment systems fail: bias, noise, and misplaced intuition (line 46)

> managers rate the same candidate from 4 to 9 on a ten-point scale

**Problem.** The chapter's foundational concept is introduced entirely through invented illustrations — teachers who "grade the same essay very differently," physicians who "use different thresholds," managers rating 4 to 9. Kahneman, Sibony and Sunstein is cited, but none of its published audit numbers appears, and the most arresting of those numbers is precisely a surprise-then-resolution: professionals did not merely disagree, they had no idea how much they disagreed. Stated as a hypothetical range, the point reads as a reasonable worry rather than a discovered fact.

**Edit.** Replace or precede the hypothetical with the insurance noise audit: executives at the firm predicted that two underwriters pricing the same risk would differ by about 10%; the median difference was 55% — more than five times their estimate — and claims adjusters differed by about 43%. Then keep the existing "Noise is easy to miss because people usually encounter one judgment" paragraph as the explanation of why the executives' guess was so far off. That sequence (expected 10, found 55, here is why nobody noticed) is the strongest teaching move available in this chapter and it is currently unused.  *(effort: small)*

### [HIGH · engagement] ### Ground forecasts in the outside view (line 125)

> Research on project forecasts documents underestimation of costs and delays

**Problem.** This is the flattest sentence in the chapter and it carries one of behavioral science's most quotable datasets. "Documents underestimation" tells a reader nothing about how large, how common, or how persistent the problem is — and the persistence is what makes the outside view feel urgent rather than optional. Three paragraphs on reference classes follow with no concrete instance of a reference class at all.

**Edit.** Add Flyvbjerg et al.'s published figures: across 258 transport infrastructure projects in 20 countries, costs were underestimated in roughly nine of every ten projects, with average overruns of about 28% overall (around 45% for rail, 34% for fixed links, 20% for roads) — and no improvement across the 70 years the data cover. That last clause is the memorable one: seven decades of experience did not fix it, which is exactly why a procedure rather than more expertise is needed. Then add one concrete reference class worked through in two sentences (e.g. the base rate of on-time completion for comparable internal projects) so the abstract advice has an instance.  *(effort: small)*

### [HIGH · engagement] ::: Research Lens: AI and accountable judgment (line 164)

> the **target-variable problem** allows technical accuracy to optimize the wrong objective

**Problem.** Obermeyer et al. (2019) is compressed into a half-clause naming a mechanism, with no description of what the algorithm did, to whom, or at what scale. It is one of the few studies in the literature with a number so stark it settles the argument by itself, and the chapter reduces it to a definitional parenthesis. The same paragraph does this to two more findings, so a reader passes three major results in four lines without encountering a single fact.

**Edit.** Give Obermeyer two or three sentences of its own before the abstract label: a widely deployed algorithm used to select patients for extra care predicted future health-care costs rather than future health; because less money is spent on Black patients at the same level of illness, Black patients assigned the same risk score had about 26% more chronic conditions. Correcting the target variable would have raised the share of Black patients flagged for additional help from 17.7% to 46.5%. Then the sentence "technical accuracy can optimize the wrong objective" lands as a conclusion the reader has already drawn.  *(effort: medium)*

### [MEDIUM · clarity] ## Why judgment systems fail: bias, noise, and misplaced intuition (line 46)

> A hiring process can repeatedly favor the wrong cue, or it can produce different judgments

**Problem.** The chapter's single most important conceptual distinction is delivered in one unbroken paragraph of roughly 200 words that does six jobs: motivating example, why the two errors need different fixes, definition of bias, the calibrated-standard caveat, the value-laden-benchmark caveat, definition of noise, three illustrations, and the citation. The bolded term **Noise** arrives in the paragraph's second-to-last sentence, long after the reader has stopped tracking. This is the first body paragraph of the chapter and it is the densest one in either chapter.

**Edit.** Split into three short paragraphs: (1) the hiring example and the claim that fixing direction does not fix inconsistency; (2) bias — definition, the scale that reads two kilograms high, and the benchmark caveat; (3) noise — definition, the three illustrations, and the citation, with the audit number recommended above. Each bolded term then opens its own paragraph rather than closing someone else's.  *(effort: small)*

### [MEDIUM · consistency] tbl-36-noise (lines 54-61)

> Legitimate discretion | Variation reflects relevant information, values, or circumstances.

**Problem.** The table's first column is headed "Failure," but its last row is explicitly not a failure — it is the category the surrounding text insists must be preserved ("Nor should consistency erase morally relevant differences"). A reader scanning the table alone takes away the opposite of the chapter's ethical point: that legitimate discretion is a failure mode to be engineered out. The caption ("Different sources of disagreement in a judgment system") is already correct; only the column header contradicts it.

**Edit.** Rename the first column "Source of variation" to match the caption, and optionally add a visual separator or a note marking the final row as the one case where the correct response is to document rather than to reduce. One-word fix, and it removes a contradiction between the table and the paragraph directly beneath it.  *(effort: small)*

### [MEDIUM · consistency] line 198, psychological safety paragraph

> It does not mean comfort, agreement, or low standards

**Problem.** Psychological safety is defined from scratch in four chapters (12 line 105, 28 line 57, 29 line 248, 41 line 198), all citing Edmondson (1999), all carrying the citation in their own reference lists, and none linking to any of the others. The quoted nine-word clause is verbatim identical in ch29 line 248 and ch41 line 198 — a literal copy across two different parts of the book. Only ch28 line 57 supplies the concrete grounding ("associated with learning behavior in 51 work teams"), so the chapter with the actual evidence is the one the other three never point to.

**Edit.** Designate ch28 line 57 the full treatment, since it holds the study detail and sits in the chapter on authority and dissent. Reduce ch29 line 248 and ch41 line 198 to one sentence each that states the local application and links back, e.g. in ch41: "Psychological safety is the social infrastructure beneath these tools ([*Authority, Groupthink, and Shared Responsibility*](28-authority-groupthink-and-shared-responsibility.qmd#bystanders-and-pluralistic-ignorance)). Leaders create it behaviorally by..." — preserving ch41's genuinely new material (the four leader behaviors) and dropping the re-definition. Note that ch34 line 242 and ch41 line 200 already do exactly this for the five groupthink pathways; that is the pattern to copy.  *(effort: small)*

### [MEDIUM · engagement] ::: Research Lens: AI and accountable judgment (line 146)

> simple mechanical or statistical rules often match or outperform unaided human judgment

**Problem.** Seventy years of the clinical-versus-statistical prediction literature — Meehl, Dawes, Grove, all cited — are summarized as "often match or outperform." "Often" is doing enormous work and hides the actual shape of the result, which is far more one-sided than the phrasing suggests and is the empirical foundation for everything the callout says afterwards about accountable model use.

**Edit.** Add Grove et al.'s meta-analytic tally: across 136 studies, mechanical prediction was roughly as accurate or better in about 94% of comparisons, and human judgment was clearly superior in about 6%. Pair it immediately with the boundary condition the chapter already believes — this holds for repeated tasks with measurable outcomes and available cues, which is why the surrounding text is right to say the target, data, and deployment context decide whether the model serves the decision.  *(effort: small)*

### [MEDIUM · engagement] ### Ground forecasts in the outside view (line 127)

> events assigned 70 percent should occur about 70 percent of the time

**Problem.** Calibration is defined correctly but never shown to have been achieved or improved by anyone, so the reader has no reason to believe the practice the chapter recommends actually works. Mellers et al. and the Good Judgment Project are cited in exactly the place where their results would supply that evidence, but no result is reported — the citation does the work of a claim without stating one.

**Edit.** Add the finding: in a multi-year forecasting tournament, training in probabilistic reasoning, working in teams, and tracking Brier scores each produced measurable accuracy gains, and the best-performing forecasters remained accurate across years rather than regressing — evidence that calibration is a trainable skill rather than a trait. State the magnitude the paper reports. This turns "forecasts should be probabilities" from a stylistic preference into a claim with support.  *(effort: small)*

### [MEDIUM · insight] ::: Research Lens: AI and accountable judgment (line 164)

> automation bias and algorithm aversion produce over- and under-reliance

**Problem.** The chapter names the pair of failure modes and stops, leaving the reader with a problem and no design response — in a chapter whose entire thesis is that design moves beat advice. The most useful finding in this literature is one step further on: Dietvorst and colleagues' follow-up showed that giving people even a tightly bounded ability to adjust an algorithm's output substantially increased their willingness to use it, and they ended up more accurate than when forced to choose between the model and themselves. That is a concrete, cheap, implementable answer to algorithm aversion and it is missing.

**Edit.** Add one sentence and citation: after seeing a model err, people abandon it for their own judgment even when the model remains more accurate (Dietvorst et al., 2015) — but letting them adjust the model's output within a narrow band restores use and improves accuracy over both alternatives (Dietvorst et al., 2018). Then state the design rule, which is the chapter's own: do not ask people to trust a model, give them a bounded way to argue with it. Connects directly to the "real human authority to correct the system" sentence two lines below, which currently asserts the principle without an evidenced mechanism.  *(effort: small)*

### [MEDIUM · structure] ::: Research Lens: AI and accountable judgment (lines 143-182) and Practice Lab step 7 (line 365)

> attach the [minimum AI-use record](#minimum-ai-use-record)

**Problem.** The Research Lens callout runs roughly 1,000 words, contains two of the chapter's seven tables, and carries its own ### subsection — and it holds material the Practice Lab treats as mandatory. Step 7 of the graded deliverable instructs students to attach the minimum AI-use record, which lives inside a callout class the book uses for supplementary research context. A reader skimming past a "Research Lens" (reasonable behavior, given how the class is used elsewhere) will miss a required artifact. The nested "### Minimum AI-use record" also sits at the same heading level as the chapter's real sections while being inside a callout under another ### section, so it surfaces in the table of contents as a peer of "Preserve independence, then aggregate."

**Edit.** Promote the AI material out of the callout into its own ## section (e.g. "## Accountable use of models and AI"), keeping only the Meehl/Dawes/Grove evidence paragraph inside a genuine Research Lens. The minimum AI-use record then becomes a normal ### subsection of a normal section, the two tables sit at the chapter's top level where the Practice Lab can reference them, and the TOC reflects the chapter's actual structure. This also fixes the heading-level jump without changing a word of the content.  *(effort: medium)*

### [MEDIUM · structure] ## Design choices, not just advice (lines 204-206)

> Advice leaves the surrounding process intact.

**Problem.** An entire ## section consists of three sentences and no instance. It functions as a transition but is formatted as a peer of substantial sections like "The structured judgment pipeline" and "The decision audit," so it appears in the table of contents and in page navigation as though it contained material. It also makes a claim the chapter never demonstrates — that a design move beats advice for a diagnosed weak stage — without showing one paired example.

**Edit.** Either demote it to a transitional paragraph at the end of the preceding section, or earn the heading by adding the missing worked pair: take one stage from the pipeline (say, the chair speaking first), give the advice version ("remember to hold back your view") and the design version ("collect written scores in a shared form before the meeting opens; the chair's row is filled last"), and state which one survives a busy week. Two sentences of concrete contrast would make this the chapter's most portable idea instead of its thinnest section.  *(effort: medium)*

### [MEDIUM · structure] line 38, The final standard

> ::: {.callout-important .the-final-standard icon=false}

**Problem.** Five blocks state a binding rule the reader is asked to hold to rather than an explanation or an exercise — ch41:38 'The final standard', ch41:260 'The same-name rule', ch35:105 'Ethics is part of agreement quality', ch16:169 'Process check: risk does not rewrite decision quality', appendix-f:216 'Read the status, not just the headline'. They use three different base types (.callout-important, .callout-caution, .callout-tip) and one bespoke class, so the book's few genuine commitments read as ordinary asides.

**Edit.** Create .standard on a .callout-important base: border var(--book-ink) #183047, bg var(--book-panel), no icon, small-caps label 'STANDARD'. Apply to all five. These are the sentences a reader should be able to recall a year later; give them one unmistakable shape.  *(effort: small)*

### [MEDIUM · visual] fig-decision-audit (line 242)

> A sound or weak process can be followed by either a favorable or unfavorable outcome.

**Problem.** The figure is never mentioned in the body, has no @fig- cross-reference, and sits orphaned between the decision-audit table and the next ## heading. Worse, its content — the process/outcome two-by-two that underwrites resulting and outcome bias — is stated in prose about 40 lines further down ("A good decision can produce a bad outcome, and a poor process can get lucky"), where the reader can no longer see it. The figure and its explanation are separated by an entire subsection.

**Edit.** Move fig-decision-audit down to sit beside the "Review the process using what was knowable at the time" paragraph (line 281) and cross-reference it there: "@fig-decision-audit separates the two questions the review must keep apart." Then strengthen the caption to state the consequence rather than the layout — something like "Judging the process by the outcome rewards luck in one quadrant and punishes sound judgment in another." Apply the same cross-referencing to fig-bias-and-noise and fig-master-loop-finale, neither of which is referenced either.  *(effort: small)*

### [LOW · consistency] Table identifiers throughout (lines 61, 220, 238, 304, 323, 352)

> : The integrated decision audit {#tbl-35-1}

**Problem.** Table anchors carry stale identifiers from an earlier numbering scheme and are internally inconsistent within a single chapter: chapter 41 contains both #tbl-36-noise, #tbl-36-meeting, #tbl-36-proportionality and #tbl-35-decision-audit, #tbl-35-decision-journal, #tbl-35-1. Chapter 40 uses #tbl-35-policy-tools and #tbl-35-ethics. #tbl-35-1 is additionally uninformative. Because nothing currently cross-references these anchors, the problem is invisible today — but it becomes a live source of wrong links the moment the @tbl- references recommended above are added.

**Edit.** Rename to content-based, chapter-agnostic slugs before adding cross-references: #tbl-noise-sources, #tbl-decision-meeting, #tbl-decision-audit, #tbl-decision-journal, #tbl-decision-moves, #tbl-proportionate-hygiene, #tbl-policy-tools, #tbl-ethics-audit. The chapter's better-named anchors (#tbl-minimum-ai-use-record, #tbl-ai-prediction-judgment-causation) already follow this convention. Worth a repo-wide grep for the tbl-3x- pattern, since the mismatch suggests it recurs across Parts VI and VII.  *(effort: small)*

### [LOW · consistency] line 281

> A good decision can produce a bad outcome, and a poor process can get lucky.

**Problem.** Inconsistent back-referencing of the book's most reused idea. The process/outcome distinction is established in ch01 lines 200-204 under the anchor #outcome-is-not-process, and four chapters link back to it by name (07:130, 16:172, 18:155, 27:204). Chapter 41 restates the thesis in the quoted near-verbatim echo of ch01 line 202 ("a good decision can produce a bad outcome, and a poor decision can produce a favorable one") but is the one chapter that does not link back — even though ch41 is the chapter the reader is most likely to arrive at directly, as the practical process chapter.

**Edit.** Match the established pattern: "Review the process using what was knowable at the time. [A good decision can produce a bad outcome](01-how-decisions-should-be-made-and-how-they-actually-are.qmd#outcome-is-not-process), and a poor process can get lucky." Chapter 41's surrounding material on regression to the mean and calibration is new and should stay.  *(effort: small)*

### [LOW · insight] '## Before the decision: improve the input' (line 88)

> Chess and some skilled emergency work can provide such learning conditions

**Problem.** Decision quality is treated throughout as a property of process, evidence, and environment, but never as a property of the decider's current state. Sleep is named as a resource in ch22; ch06 covers hot/cold motivational states and has a research note on arousal and impatience; but no chapter tells the reader that fatigue, acute stress, hunger, or time of day are inputs a person can actually manage before a consequential choice. In a chapter whose whole subject is protecting judgment before the answer becomes obvious, the absence of the cheapest available protection is noticeable.

**Edit.** Add ~350 words to '## Before the decision: improve the input' as a hygiene rule rather than a psychology lecture — the actionable form is a process commitment ('no irreversible commitment on a day with under five hours of sleep; reconvene rather than push through'). Keep the book's hedging discipline: the ego-depletion literature is contested and the chapter should say so rather than borrow its confidence, which makes this a good place to model how to act sensibly on evidence that has not settled.  *(effort: small)*

### [LOW · structure] ::: The final standard callout (lines 38-42)

> A useful intervention should remain defensible if the people affected understand how it works

**Problem.** A callout is inserted between "## Learning goals" and the first body section, a slot the chapter template reserves for the transition into the body — chapters 39, 40, and 42 all move directly from learning goals into content. Its content also near-duplicates chapter 40's closing line ("Would the design remain defensible if the people affected understood how it worked, whose goal it served, and how to refuse it?"), which chapter 40 explicitly frames as "the standard used throughout this book." Placed here, unattributed to its earlier statement, it reads as a new claim rather than a deliberate callback, and it interrupts the momentum of the hiring-committee scenario that opened three paragraphs earlier.

**Edit.** Either move the callout to the chapter's close, beside "## Ethics, governance, and proportionality," where it summarizes work the reader has done; or keep it here but name the callback explicitly ("Chapter 40 closed on a standard this chapter now applies to the process itself") and link to the choice-architecture section. Keeping the wording identical to chapter 40's phrasing would also make it recognizable as a recurring refrain rather than a restatement.  *(effort: small)*

---

## `chapters/42-data-driven-decision-making.qmd`  (19 findings)

### [HIGH · consistency] ## Practice Lab: build a small AI decision system (line 268)

> ## Practice Lab: build a small AI decision system

**Problem.** Chapters 39, 40 and 41 — the three Part 7 chapters this one closes — each wrap their Practice Lab in `::: {.callout-tip .activity icon=false}`, one of only four classes with real CSS. Chapter 42's Practice Lab is bare prose. The result is that the book's final and longest hands-on exercise renders with no visual container at all, and the chapter as a whole carries exactly one styled callout (the Core Idea) across 7,100 words.

**Edit.** Wrap lines 268-302 in `::: {.callout-tip .activity icon=false}` ... `:::` matching chapter 41's Practice Lab exactly. While doing so, add the missing operating details chapters 39-41 supply: a stated deliverable (the completed canvas plus a one-paragraph Round 4 record, not an essay) and a note for solo readers, since Round 1 as written ('Give two people the same case') is undoable alone — chapter 41 handles this with its 'if only one decision-maker is available, record an initial estimate before seeking advice' clause.  *(effort: small)*

### [HIGH · engagement] ## Opening puzzle: why did better predictions provoke opposition? (line 17, first sentence)

> Flint, Michigan, needed to find and replace hazardous water-service lines.

**Problem.** The book's final chapter opens on the most notorious drinking-water disaster in recent US history and strips it of every stake. No date, no cause, no scale, no human. A reader who does not already know Flint learns only that some pipes needed replacing and that excavation is expensive — so the residents' later fury in paragraph two reads as unreasonable rather than as the predictable behavior of people who were poisoned and then told to trust a model. The chapter's own surprise-then-resolution structure depends on stakes it never supplies.

**Edit.** Add two sentences of grounding before 'The pipes were underground': the April 2014 switch to the Flint River, corrosion control not applied, lead leaching into the water of a city of roughly 100,000; the 2017 Concerned Pastors v. Khouri settlement obligating the city to inspect and replace some 18,000 service lines on a court deadline. Then the model's job has a clock and a body count behind it, and 'wealthier residents angry that their pipes were not being checked' lands as a real conflict between reassurance and protection rather than as a complaint.  *(effort: small)*

### [HIGH · engagement] ### Values enter before the final button {#ai-target-variable-problem} (line 128)

> Black patients were sicker than White patients with the same risk score

**Problem.** Obermeyer et al. (2019) is the single most cited empirical result in algorithmic fairness and the chapter reports it with zero numbers. 'Sicker' does all the work. The reader cannot tell whether this is a rounding error or a scandal, and the sentence that follows ('The model could perform well at predicting its label') generalizes away from the case before the case has registered. This is exactly the omission pattern the manuscript needs fixed.

**Edit.** Add the three published figures: at the same algorithmic risk score, Black patients had 26.3 percent more chronic conditions; correcting the label from cost to health need would raise the share of Black patients auto-referred into the high-risk management programme from 17.7 percent to 46.5 percent; and algorithms of this family were applied to roughly 200 million people annually in the US. The 17.7-to-46.5 jump is the memorable number — a proxy choice, not a modelling error, nearly tripled who got help.  *(effort: small)*

### [HIGH · engagement] ### Customer support: help at the moment of action {#ai-customer-support} (line 198)

> by 15 percent on average, with substantial differences across workers

**Problem.** The heterogeneity is the finding, and 'substantial differences across workers' buries it in an abstraction. Brynjolfsson, Li and Raymond's result is counterintuitive and directly relevant to this chapter's thesis about complements: the assistant raised novice and low-skilled agents' resolutions per hour by about 34 percent while doing close to nothing for the most experienced and highest-skilled agents — the tool propagated the tacit know-how of top performers rather than amplifying existing skill. Stated as written, the surprise dies and the paragraph teaches nothing the next sentence does not already say.

**Edit.** Replace the clause with the split: roughly 34 percent for the least experienced agents, near zero for the most experienced, and note that the gain grew with months of exposure. Then add one sentence drawing the inference the chapter is set up to make: a tool that compresses the skill distribution has different implications for hiring, training and pay than one that raises everyone equally — and a 15 percent average would have concealed that entirely.  *(effort: small)*

### [HIGH · insight] ## Flint: a probability map becomes a public decision {#flint-lead-pipes} (line 146)

> better prediction became a struggle over decision authority

**Problem.** The chapter reaches the door of its own best point and stops. It reports that the hit rate fell from 80 to 15 percent, and it says authority was contested — but it never states who paid for the switch. Under uniform ward-by-ward digging, the households most likely to have lead lines waited longer, and the same crews and dollars removed roughly one-fifth as many hazardous pipes. The policy that was adopted to answer a fairness objection produced, for the people actually drinking from lead pipes, a materially worse outcome. That is the memorable, transferable lesson — equal treatment of inspections purchased at the cost of unequal protection — and it is left for the reader to assemble.

**Edit.** After 'a struggle over decision authority', add two sentences naming the distributional consequence: spreading crews evenly gave more residents the visible reassurance of work on their street, while the households most likely to be drinking through lead lines waited longer and fewer of those lines came out per dollar spent. Then state the general form: a procedural fairness claim about who gets looked at can trade directly against a substantive fairness claim about who gets protected, and no probability map can adjudicate between them — which is precisely why the chapter's Core Idea reserves valuation for accountable human authority.  *(effort: small)*

### [HIGH · visual] ## Test the whole decision, not just the model {#test-the-whole-decision} (lines 192-266)

> ## Test the whole decision, not just the model

**Problem.** 1,863 words run from the workbench table (line 190) to the canvas table (line 286) with no figure, table, or callout of any kind. The stretch contains the chapter's densest technical material — LLM token prediction, three empirical case studies, the trust/authority argument, and four evaluation subsections — and 'Test the whole decision' alone is 797 words of pure prose that is structurally a checklist. This is the hardest part of the chapter to follow and the least supported visually.

**Edit.** Convert the four subsections of 'Test the whole decision' into one table beside the prose, with columns: Stage / Question to answer / Failure it catches / Evidence to record. Rows drawn verbatim from the existing text: unit and moment of decision ('Use only information available at that moment') catches leakage; held-out test set catches tuning on the answer; credible simple baseline catches improvement that is not improvement; discrimination vs calibration catches good ranking with bad probabilities; action-rule evaluation catches gains far from any threshold; logged action alongside prediction catches the policy contaminating its own evidence. The prose then explains the rows rather than carrying them alone.  *(effort: medium)*

### [MEDIUM · accuracy] ### Customer support: help at the moment of action {#ai-customer-support} (line 198)

> a generative-AI assistant among 5,172 customer-support agents

**Problem.** The published sample size appears to be 5,179 agents, not 5,172. A transposed digit in a headline sample size is the kind of error that undermines a manuscript whose scientific care is otherwise its strongest asset, and it is not recoverable by a reader.

**Edit.** Check the QJE 140(2) abstract and correct to the published figure. While in the paragraph, confirm the outcome wording matches the paper's ('issues resolved per hour' is correct) and consider naming the setting — a Fortune 500 enterprise software firm's support organization — since the chapter elsewhere insists that context determines whether a result travels.  *(effort: small)*

### [MEDIUM · accuracy] ## Test the whole decision, not just the model {#test-the-whole-decision} (line 236)

> The course materials for strategic and data-driven decision-making add the managerial questions

**Problem.** An uncited, unnamed source in a chapter where every other empirical or conceptual claim carries a reference. 'The course materials' has no author, no institution, no year, and no entry in the reference list; a reader cannot follow it, and it reads as an unconverted remnant of lecture notes in a manuscript whose citation discipline is otherwise exemplary.

**Edit.** Either cite the source properly (add a reference-list entry and an in-text citation) or delete the attribution and state the questions in the book's own voice: 'The managerial questions follow: which errors matter, what capacity exists, and who will act on the result.' The sentence loses nothing.  *(effort: small)*

### [MEDIUM · accuracy] ::: {.chapter-epigraph} (line 12)

> chapter 2, “Cheap Creates Value”

**Problem.** Two problems in the book's closing epigraph. First, chapter 2 of Prediction Machines is titled 'Cheap Changes Everything'; 'Cheap Creates Value' does not appear to be a chapter title in that book — verify against the edition before print. Second, the epigraph links to what looks like an unauthorized full-text PDF of an HBR Press book hosted on a university course site, while the reference list links the 2022 editions of the same authors to store.hbr.org. The manuscript should not point readers at a pirated copy of a copyrighted book.

**Edit.** Correct the chapter title after checking the 2018 edition's table of contents, and replace the wpmucdn PDF link with the publisher or a DOI/library link, matching the pattern already used for Agrawal et al. (2022a, 2022b). Also reconcile the edition: the epigraph cites 2018 while the body cites 2022b for the same book (line 72), and the reference list carries both — either cite one edition throughout or make the epigraph read '(Agrawal et al., 2018)' so the two entries are clearly distinguished.  *(effort: small)*

### [MEDIUM · accuracy] ## Trust, valuation, and responsibility {#trust-and-responsibility} (line 220)

> sometimes placed more weight on advice attributed to an algorithm

**Problem.** Two opposing literatures are set side by side and left unresolved. The chapter reports Bigman and Gray's moral-decision aversion and Logg's algorithm appreciation in consecutive sentences, hedged only by 'sometimes', with no numbers and no statement of the moderator that reconciles them — Logg's appreciation appears for objective, numeric, quantifiable estimates, whereas aversion appears for morally weighted or subjective judgments. Worse, chapter 41 (line 164) has already given the reader the correct pair for this argument, automation bias and algorithm aversion (Dietvorst et al., 2015; Mosier et al., 1998), and chapter 42 neither builds on it nor cross-references it, so the final chapter restates a weaker version of material the previous chapter handled better.

**Edit.** State the moderator explicitly — reliance rises for tasks people code as objective and numeric, and falls for tasks they code as moral or subjective — and give one anchoring number from each study rather than 'sometimes'. Then link back: 'Chapter 41 named the two failure modes this produces: automation bias and algorithm aversion (Dietvorst et al., 2015). Neither is trust calibrated to comparative evidence.' Add Dietvorst to this chapter's reference list, since it carries the single most useful boundary condition here — people abandon an algorithm after seeing it err, even when it still outperforms them.  *(effort: small)*

### [MEDIUM · clarity] ### Screening: change the workflow, then test it {#ai-masai-screening} (line 206)

> The rate ratio was 0.88, with a 95 percent confidence interval of 0.65–1.18.

**Problem.** One paragraph introduces and defines four technical terms (interval cancers, non-inferiority, sensitivity, specificity) while delivering seven numbers across two arms and two studies. The reader must hold 1.55 vs 1.76, a rate ratio and its interval, 80.5 vs 73.8, and 98.5 vs 98.5 in working memory while also learning what each metric means. Nothing is wrong; it is simply unreadable at speed, and it sits inside the chapter's longest stretch without a visual.

**Edit.** Move the numbers into a small three-column table (Measure / AI-supported / Standard double reading) with rows for interval cancer rate per 1,000, sensitivity, specificity, and screen-reading workload, captioned with the takeaway rather than the label: 'Halving the reading work did not cost detection — the AI-supported workflow met the prespecified non-inferiority margin on interval cancers.' Keep only the definitions of interval cancer and non-inferiority in the prose, where they carry conceptual weight.  *(effort: small)*

### [MEDIUM · clarity] ## Flint: a probability map becomes a public decision {#flint-lead-pipes} (line 142)

> an actual unnecessary-visit rate of 18.8 percent with 2.0 percent

**Problem.** A fourth metric arrives with no definition, one sentence after the reader has been taught hit rates of 80, 15 and 70 percent. 'Unnecessary-visit rate' is never defined, and 18.8 percent is in fact the near-complement of the 80 percent hit rate just given — so the reader who does not notice that spends the sentence trying to reconcile two apparently unrelated statistics. The sentence also compresses what is being compared with what: 'compared an actual... with 2.0 percent under a proposed procedure' leaves it unclear that both figures come from the authors' own retrospective simulation of their own method.

**Edit.** Rewrite to connect the metrics and flag the comparison's status: 'An unnecessary visit is an excavation that uncovers a safe line — the mirror image of the hit rate. Abernethy and colleagues estimated that 18.8 percent of visits in the field were unnecessary, against 2.0 percent when they replayed the historical record through their proposed selection procedure. That 2.0 percent is a simulated upper bound on the same data the method was developed from, not a result achieved in the street.'  *(effort: small)*

### [MEDIUM · clarity] ## Learning goals, goals 2-3

> Explain how AI, machine learning, and algorithms relate, and match tools

**Problem.** Chapter 42 carries four goals, two of them 'Explain', while the chapter's substantive work is evaluating deployed-AI evidence — Flint service lines, the healthcare cost-proxy audit, the MASAI randomized screening trial, the physician-vignette study — and none of the four goals names that skill. Appendix D lists five separate ch42 examples of exactly this kind.

**Edit.** Replace goal 2 with: 'Evaluate one deployed AI system against its baseline, its target variable, and its measured outcome, and say which of the three the evidence actually tests.' Keep goals 1 and 4; fold goal 3 into goal 4 so the chapter returns to three goals like the other 39.  *(effort: small)*

### [MEDIUM · consistency] # Data Driven Decision Making (line 1)

> # Data Driven Decision Making

**Problem.** This is the only one of the book's 42 chapter titles without a colon subtitle — every other title pairs a concept with a memorable claim ('Decision Hygiene: Build a Process That Can Learn', 'Choice Architecture: The Environment Gets a Vote', 'Framing: When the Same Facts Become Different Decisions'). It is also the only title containing an unhyphenated compound modifier; the book writes 'Intertemporal Decision-Making' and 'Risky Decision-Making' with hyphens elsewhere. The result is that the book's closing chapter carries its blandest and least characteristic heading, and the table of contents ends on a generic category label.

**Edit.** Hyphenate and add a subtitle in the house pattern, drawn from the chapter's own closing line and Core Idea — for example 'Data-Driven Decision-Making: Cheap Prediction Does Not Decide What Is Worth Doing'. Keep the filename and the `[]{#data-driven-decision-making}` anchor unchanged so existing links survive.  *(effort: small)*

### [MEDIUM · engagement] ### Screening: change the workflow, then test it {#ai-masai-screening} (line 204)

> screen-reading workload fell by 44.3 percent relative to standard double reading

**Problem.** The MASAI interim analysis is reported with only its cost-saving number, which makes the paragraph read as a story about efficiency. The genuinely surprising interim result is omitted: the AI-supported workflow detected about 20 percent more cancers (6.1 vs 5.1 per 1,000 screened) while cutting reading work nearly in half, with no increase in the false-positive rate (1.5 percent in both arms). Less work and more cancers found, simultaneously, is the result that makes the later non-inferiority analysis worth caring about — and the chapter's own framing sentence ('Reducing the number of human readings would save effort, but missed cancers could make that saving costly') sets up exactly that tension and then declines to resolve it.

**Edit.** Add the interim detection rates and the unchanged false-positive rate alongside the 44.3 percent workload figure, and name the trial size precisely (80,033 women). One added clause — 'and it did so while detecting about 20 percent more cancers, with the false-positive rate unchanged' — converts a cost story into the surprise the paragraph was built for.  *(effort: small)*

### [MEDIUM · engagement] ## Why this is the final chapter {#why-this-final-chapter} (line 58)

> Using that opportunity draws on the whole book:

**Problem.** A five-bullet inventory of what earlier chapters said, in which not one bullet contains a concrete instance. Every bullet follows the same shape — Chapter X asks A; Chapter Y examines B; these questions apply to C — so the section signposts the book's coherence instead of demonstrating it, and it does so on page three, interrupting the Flint argument just as it has taken hold. The Flint case is sitting right there and would make each abstraction land.

**Edit.** Anchor each bullet to Flint in a clause: attention and interpretation — which properties never entered the training data because nobody had ever dug there; prediction and evidence — whether an 80 percent hit rate is impressive without knowing the base rate of lead lines in the stock that remained; valuation — whether success means pipes removed or households reassured; other minds and institutions — the settlement that decided who set the priorities; design and learning — the inspection capacity spent on learning rather than on removal. Also consider moving the section to follow 'What becomes possible when prediction becomes cheap?', so the chapter's argument is underway before it turns to look back at the book.  *(effort: medium)*

### [MEDIUM · insight] ### One rain forecast, two sensible choices (line 120)

> A threshold of 50 percent would be appropriate only for equal error losses

**Problem.** The chapter derives p > C_F/(C_F+C_M) and correctly notes that 50 percent is a special case — and then walks past the fact that it has just rebuilt the signal-detection criterion, which chapter 8 already gave the reader. A named connection would convert a one-off arithmetic exercise into a recognizable structure the reader has met before in a completely different setting, which is the payoff a final chapter is uniquely positioned to deliver.

**Edit.** Add one sentence after the threshold derivation: 'This is the criterion from signal detection in [Chapter 8], reached from the other direction. There, shifting where a person sets the line between signal and noise trades false alarms against misses; here, the error costs set that line explicitly. A model supplies p; it never supplies the criterion.' Verify the anchor in chapters/08-fast-and-frugal-thinking.qmd, which is where signal detection is developed.  *(effort: small)*

### [MEDIUM · visual] ## Predicting risk does not tell us whom an intervention will help (line 177)

> The figure makes the causal input visible alongside those allocation priorities.

**Problem.** The chapter defines two figures and four tables and cross-references none of them. Both figures are gestured at as 'the figure' or 'The figures below', and all four tables are introduced by bare prose ('The following decisions determine...', 'Complete the following canvas'). In HTML and PDF the exhibits float, so 'the figure' and 'below' can point at nothing; the chapter's only @-references (lines 90 and 312) both point to chapter 1's figure. Chapters 38 and 39 do use @tbl-/@fig- references, so the convention exists in the book.

**Edit.** Replace every deictic reference with the numbered cross-reference that already has an id: '@fig-ai-risk-is-not-benefit makes the causal input visible...' (line 177), '@fig-ai-same-forecast-different-values shows...' (add near line 124), '@tbl-ai-rain-losses' (line 98), '@tbl-ai-flint-decision' (line 148), '@tbl-ai-workbench' (line 181), '@tbl-ai-decision-canvas' (line 274). Also rewrite the caption on @tbl-ai-flint-decision, which currently reads 'Decisions in a pipe-replacement program' and merely repeats its own column header; make it state the takeaway, e.g. 'The model answers only the first row; the other four remain human decisions.'  *(effort: small)*

### [LOW · consistency] ### subsection anchors throughout (lines 94, 238, 246, 254, 262)

> ### One rain forecast, two sensible choices

**Problem.** Subsection ids are applied unevenly: four `###` headings carry explicit anchors ({#ai-target-variable-problem}, {#ai-customer-support}, {#ai-masai-screening}, {#ai-physician-vignettes}, {#ai-decision-canvas}) while five do not ('One rain forecast, two sensible choices', 'Make the test resemble the task', 'Evaluate probabilities and decisions separately', 'Compare workflows before scaling', 'Communicate enough uncertainty to support a choice'). The unanchored ones are exactly the material other chapters would want to link to — the threshold derivation and the evaluation discipline — and auto-generated ids will silently change if a heading is ever reworded.

**Edit.** Add stable ids to the five bare `###` headings, following the chapter's existing ai- prefix convention: {#ai-rain-threshold}, {#ai-test-resembles-task}, {#ai-discrimination-calibration}, {#ai-compare-workflows}, {#ai-communicate-uncertainty}. This also gives chapter 15's calibration material a target to link forward to.  *(effort: small)*

---

## `how-to-read-evidence.qmd`  (11 findings)

### [HIGH · consistency] Read the comparison and outcome

> ## Read the comparison and outcome {#read-each-boundary-in-four-moves}

**Problem.** The anchor id promises 'four moves' that the section does not contain; the heading names two things and the body names three (comparison, outcome, explanation being tested). Unlike the stale id in how-to-use-this-book.qmd, this one has a live inbound link: concept-index.qmd line 287 sends 'Evidence boundary' here, so a reader following the index lands on a section that does not match the promise the index made.

**Edit.** Make heading, id, and content agree. Simplest fix: retitle the section 'Read the comparison, the outcome, and the claim being tested', give it the id `{#read-the-comparison-and-outcome}`, add an empty anchor span `[]{#read-each-boundary-in-four-moves}` immediately beneath the heading so the concept-index link keeps working, and update the concept-index entry to the new id. If the 'four moves' framing is still wanted, add the fourth explicitly (comparison, outcome, explanation, time frame) and number them.  *(effort: small)*

### [HIGH · engagement] Whole file (opening through the six-question audit)

> In a hypothetical service team, an increase from 10 to 12 completed cases per hour

**Problem.** A 903-word guide to reading evidence contains no actual evidence: no named study, researcher, year, journal, or published number. Every illustration is hypothetical — a training programme, a service team, an unequal offer. The file teaches evaluation by describing it rather than performing it, which is precisely the 'illustration vs. evidence' distinction it warns against two sections later.

**Edit.** Work one real case end to end through the six questions, using material Appendix F has already vetted so no new verification is needed. The watched-eyes honesty box is the right size: Bateson, Nettle and Roberts (2006) reported higher honesty-box contributions under images of eyes than under flowers; two meta-analyses found no reliable effect of artificial surveillance cues on generosity (Northover et al., 2017). Run the six questions against it in six short lines and the guide becomes a demonstration instead of a checklist.  *(effort: medium)*

### [HIGH · engagement] Treat replication as information, not a verdict

> A failed replication may weaken confidence in an original finding, reveal a boundary

**Problem.** The three-way distinction offered here (weakened confidence / boundary condition / implementation difference) is the right framework, but it is stated with no magnitude, so the reader cannot tell whether replication failure is a rare event worth noting or a systematic feature of the literature they are about to read 42 chapters of. Appendix F line 31 has the numbers; this section withholds them.

**Edit.** Open the section with the scale, then give the framework: 'The Open Science Collaboration attempted replications of 100 psychology studies. Ninety-seven percent of the originals reported statistically significant results; 36 percent of the replications did, and the replication effects averaged about half the original magnitude (Open Science Collaboration, 2015).' The existing three-way distinction then reads as guidance for interpreting a common event rather than an abstract taxonomy — and it establishes the book's credibility with a reader who already knows about the replication crisis.  *(effort: small)*

### [HIGH · insight] Separate size from certainty

> A statistically significant result can be too small to matter in practice

**Problem.** This section stops one step short of the most decision-relevant fact about the behavioral literature: among small studies, the ones that reach significance systematically overestimate the effect, so the published number is biased upward even when nobody did anything wrong. Without it, a reader concludes only that significance and size are different questions — true but not actionable. The book already owns the demonstration in Appendix F.

**Edit.** Add two sentences and a link to the simulation the manuscript already contains: with a true effect of 0.20 standard deviations and 50 observations per arm (17% power), the studies that clear p < .05 average 0.490 — about 2.5 times the truth — and a few even have the wrong sign. Then the practical rule follows naturally: when a literature consists of small studies, expect the true effect to be smaller than the published one, and treat the first significant result as an upper bound. Link @fig-selected-literature-simulation in Appendix F so the interested reader can see the mechanism.  *(effort: small)*

### [HIGH · structure] A six-question evidence audit (closing)

> You do not need to become a methods specialist before reading the book.

**Problem.** The file opens with a live decision — should you spend a limited training budget on a programme advertised at '+20% productivity'? — and never resolves it. The training example returns three times as an illustration but the purchase is never made, refused, or conditioned. The guide therefore ends as a methods note, when the book's entire thesis is that evaluation exists to serve a decision.

**Edit.** Close the loop in a short final paragraph before the 'You do not need to become a methods specialist' line: state what you would actually do with the training budget given a pre/post design and a same-day knowledge test — buy a small pilot for one team rather than the full programme, agree the outcome in advance (supervisor-rated case handling at 90 days, not the test score), keep an untrained comparison team, and name in advance what result would stop the rollout. That is the audit turned into a decision, and it is the single change that makes this guide feel like part of this book rather than a generic methods primer.  *(effort: medium)*

### [HIGH · visual] A six-question evidence audit

> ## A six-question evidence audit

**Problem.** 903 words with zero figures, tables, and callouts — the only file in the front matter with no visual relief at all, and the one whose content is most abstract. The six-question audit, which is the file's deliverable and the thing readers will return to, is rendered as a plain numbered list indistinguishable from body text, even though the book has a styled `.activity` callout class available.

**Edit.** Wrap the audit in `::: {.callout-note .activity icon=false}` so it is visually findable, and render the six items as a three-column table: 'Question | What a good answer contains | What a weak answer sounds like'. Row 3 for example: 'How large and uncertain is the estimate? | a number in real units plus an interval | "statistically significant" or "a 20% improvement" with no base'. The third column is what converts a checklist into a diagnostic skill, and it gives the reader a reason to reread the page.  *(effort: medium)*

### [MEDIUM · clarity] Read the comparison and outcome

> A useful account of evidence identifies the comparison, the outcome, and the explanation being tested.

**Problem.** This is the guide's central move and it is the shortest section in the file: one instruction sentence, one pointer to footnotes, and one two-sentence gloss on the training example. The reader is told what to identify but never sees the identification performed, so the move stays a slogan.

**Edit.** Work the training claim out loud in three labeled lines: 'Comparison: the 150 volunteers' own scores before the course, not a group that did not attend. Outcome: a 20-item knowledge test taken the same afternoon, not work performance. Explanation tested: that the course taught the material — not that it changed what people do at their desks.' Then the follow-up sentence about a workplace-performance measure has something to contrast with, and the reader has a template they can copy onto the next claim they meet.  *(effort: small)*

### [MEDIUM · clarity] Treat replication as information, not a verdict

> Low precision, flexible analysis, and selective publication can make a literature look more convincing

**Problem.** 'Precision' and 'preregistration' both appear here for the first time in the book with no definition, in the file specifically designed for readers who are not methods specialists. 'Precision' is the worse problem: the guide's own earlier section deliberately used plain vocabulary ('how uncertain the estimate is', 'the range of plausible values') and then switches to the technical term without connecting the two — and Chapter 4 later uses 'precision' in a different, predictive-processing sense ('precision weighting') that a reader may mistakenly connect to this one.

**Edit.** Use the guide's own earlier vocabulary: 'Small samples and imprecise estimates, flexible analysis, and selective publication can make a literature look more convincing than it is.' Then gloss preregistration in four words at first use — 'preregistration (committing to the analysis before seeing the data)'. If the word 'precision' is wanted, define it once against the earlier section and add a half-sentence noting that Chapter 4 uses the same word for a different quantity.  *(effort: small)*

### [MEDIUM · insight] Ask whether the finding travels

> “It depends” is the beginning of an explanation only when we can say what it depends on.

**Problem.** The best sentence in the file is also its last word on generalization, and it leaves the reader with an aphorism rather than a procedure. The reader now agrees that 'it depends' needs specifying, but has no move to make when they next face that situation.

**Edit.** Convert it into a three-step test in the following sentence: name the one difference you think matters most (volunteers vs. required attendance), say which direction it should push the effect and why, and say what observation would embarrass your guess. Then add the payoff the book is well-placed to make: a moderator you can state and test is a contribution; a moderator invoked only after a failure is a way of protecting the original claim from evidence. That second clause is the honest, slightly uncomfortable point that makes the section memorable.  *(effort: small)*

### [MEDIUM · visual] Distinguish an illustration from evidence

> Field studies examine behavior in everyday or organizational settings and may be observational or experimental.

**Problem.** Six source types — fictional cases, classroom demonstrations, single studies, replications, field studies, formal models, and meta-analyses (seven, in fact) — are packed into two dense paragraphs of running prose. This is a list wearing paragraph clothing, and nothing in the presentation helps a reader hold the comparison the section is asking them to make.

**Edit.** Replace the two paragraphs with a small table: 'Source | What it can establish | What it cannot'. E.g. 'Classroom demonstration | that something can happen, memorably | any estimate of how often or how large'; 'Single experiment | an effect under one specified comparison | that the effect survives other samples or implementations'; 'Meta-analysis | a cumulative estimate and its heterogeneity | a correction for the selection that produced the literature'. Six rows replace roughly 130 words, give the file its first visual relief, and make the section usable as a lookup.  *(effort: medium)*

### [LOW · accuracy] Separate size from certainty

> A *p*-value is not an effect size or the probability that a theory is true.

**Problem.** The statement is correct, and the two misreadings it names are real. But it omits the misreading that is by far the most common among the students this book targets: that a p-value is the probability the result is due to chance, or that 1 − p is the probability the finding will replicate. A guide whose purpose is inoculation should name the error its readers will actually make.

**Edit.** Extend to three clauses: 'A *p*-value is not an effect size, not the probability that a theory is true, and not the probability that the result is due to chance. It is the probability of data at least this extreme if the null hypothesis were true, which is why it cannot by itself tell you how likely the effect is to appear again.' One added clause, no change to the file's careful tone, and it closes the gap that leads readers to treat p < .05 as a replication guarantee.  *(effort: small)*

---

## `how-to-use-this-book.qmd`  (14 findings)

### [HIGH · clarity] Find your place in the book

> ## Find your place in the book {#follow-the-highlighted-loop}

**Problem.** Heading and content do not match. The heading promises navigation; the section actually delivers the four-term vocabulary table (Interpret, Predict, Expectation, Value) that the whole book depends on, buried under a navigation label and preceded by a paragraph about part maps. The most important 60 words in this file are the hardest to find.

**Edit.** Split into two sections. 'How the decision map is used' keeps the first paragraph and the note about part openers. 'Four terms that keep their meaning' takes the vocabulary table plus the Chapter 4 caveat about the two senses of *prediction*, and gets its own heading so it appears in the sidebar TOC and can be linked from chapters that need it.  *(effort: small)*

### [HIGH · consistency] Reading layers

> An **Applied Module** extends the ideas into a particular domain.

**Problem.** 'Applied Module' is presented as a standing reading layer alongside Research Lens, Practice Lab, and Footnotes. There is exactly one in the entire book: the collapsed '.applied-module' callout in Chapter 23 ('Applied module: market rules change the strategic game'). A reader told to expect a recurring feature will look for it 41 more times and not find it.

**Edit.** Either name it as a one-off — 'Chapter 23 adds a collapsed **Applied Module** that carries the strategic ideas into market institutions' — or cut the sentence. If the intention is that it should recur, that is a manuscript decision, not a front-matter one, and the front matter should describe what is there now.  *(effort: small)*

### [HIGH · consistency] Reading layers

> **Research Lens** boxes and **optional research notes** develop formal models

**Problem.** These are named as two distinct reading layers, but the book does not maintain the distinction. Three of the four optional research notes (Ch. 10 #research-note-positive-illusions, Ch. 32 #research-note-curiosity, Ch. 34 #research-note-forgiveness) are themselves `.research-lens` callouts; only Ch. 6's 'Research note: are needs a hierarchy?' is a plain `.callout-note`. The reader is taught a two-way distinction that the styling contradicts on first contact.

**Edit.** Collapse to one layer in the description: '**Research Lens** boxes develop formal models, measurement, or contested evidence; some are collapsed as optional research notes you can open later.' Separately, give Chapter 6's research note the `.research-lens` class so all four look alike, or drop the 'research note' label there.  *(effort: small)*

### [HIGH · consistency] ## Reading layers, Applied Module sentence

> An **Applied Module** extends the ideas into a particular domain.

**Problem.** Exactly one block in the book carries .applied-module (ch23:243). But the layer is not missing — eleven applied extensions exist across seven chapters under six competing names: 'Application box' (ch16:244), 'Applied Lens' (ch19:206, ch25:246), 'Applied module' (ch23:243), 'Optional module 1-4' as plain headings (ch38:75/105/131/174), 'Optional module' (ch38:187), 'Optional Media Lab' (ch39:222). Three more carry a seventh name, 'Advanced research track' (ch24, ch25, ch27), for content that is methods rather than application.

**Edit.** Neither cut the promise nor write new modules — relabel. Apply .applied-module to ch16:244, ch19:206, ch23:243, ch25:246, ch38:187, ch39:222 and convert ch38's four plain 'Optional module N' headings to the same class, routed from @tbl-agreement-module-routing. Leave ch16:271 and ch21:190 as Research Lens (theory and practice, not domain). Demote the three 'Advanced research track' boxes to plain Research Lens titling so track/lens/module stop competing. Seven chapters then carry a visible Applied Module with zero new prose. Five cheap additions, if wanted, are listed in chapter_notes Part 4.  *(effort: medium)*

### [HIGH · structure] A recurring chapter rhythm

> Chapters introduce a problem, develop an explanation, examine evidence

**Problem.** This is a three-sentence section describing the book's most rigorously maintained asset in terms so generic they would fit any textbook. The real template — italic subtitle, epigraph, opening scenario, Core Idea, Learning goals, body, Practice Lab, Take it forward, References cited in this chapter — is consistent across all 42 chapters and is never shown. 'Reading layers' also omits Core Idea, Learning goals, and Take it forward entirely, so a reader meets the three most load-bearing elements of every chapter with no instruction about them.

**Edit.** Replace the section with an 'Anatomy of a chapter' table: column 1 the element in the order it appears; column 2 what it is for; column 3 what to do with it. E.g. 'Core Idea | the one claim the chapter defends | read it first, then read it again at the end and see whether you now believe it'; 'Practice Lab | produces an inspectable output | do one per part, not one per chapter'; 'Take it forward | a commitment, not a summary | write the date you will check it'. This teaches the reader to use the book in about 120 words and is the highest-leverage single addition to this file.  *(effort: medium)*

### [HIGH · structure] ## Reading layers

> Start with the chapter's opening situation and follow the main argument.

**Problem.** The Reading layers section names four devices — Research Lens, optional research notes, Applied Module, Practice Lab, Footnotes — and never names the three elements that actually appear in all 42 chapters: the Core Idea box, Learning goals, and Take it forward. A reader arrives at chapter 1, meets a styled orange box called 'Core Idea' that the front matter never mentioned, and has no guidance on whether Learning goals are a contract or a preview.

**Edit.** Rewrite Reading layers as a six-row table of what recurs in every chapter and what it is for: epigraph (orientation), opening scenario (the problem in one situation), Core Idea (the claim the chapter defends — read it before and again after), Learning goals (what you should be able to do, not what you will have read), Practice Lab (the artifact you produce), Take it forward (the commitment you make). Then a second short list of the optional layers: Research Lens, Evidence Boundary, Applied Module, Predict First, Tools, Footnotes.  *(effort: medium)*

### [MEDIUM · consistency] Find your place in the book

> {#follow-the-highlighted-loop}

**Problem.** The anchor id is a leftover from a previous heading ('follow the highlighted loop') that no longer corresponds to anything on the page. A grep across the manuscript finds no inbound link to it, so it is a dead id whose only effect is to make the URL misdescribe the section.

**Edit.** Rename to ids that match the split headings recommended above (e.g. `{#how-the-decision-map-is-used}` and `{#four-terms}`). Since nothing links to the old id, no alias span is needed — unlike the analogous stale id in how-to-read-evidence.qmd, which does have an inbound link.  *(effort: small)*

### [MEDIUM · consistency] Find your place in the book

> In the preface’s map, green arrows show where learning can prompt revision.

**Problem.** This sentence and the one following it restate, almost clause for clause, two paragraphs the Preface has just delivered ('Follow the green arrows back...' and 'The first box names the current context and available information... The map leaves those changes to future inputs outside its return path'). A reader arriving here three pages later is told the same thing twice, which teaches them that the front matter can be skimmed.

**Edit.** Cut both sentences and link instead: 'The map and its feedback path are explained in the [Preface](index.qmd#fig-master-loop).' Use the recovered space for the anatomy-of-a-chapter table.  *(effort: small)*

### [MEDIUM · consistency] Use one recurring ethical audit

> ask whose objective it serves, who benefits, and who bears the cost.

**Problem.** The book's recurring ethical test is stated three times in the front matter in three different wordings: here; in the Preface ('whose goal a design serves, who bears its costs, and whether affected people can understand, question, or leave it'); and in about.qmd ('would remain defensible if the people affected understood how it worked, whose objective it served, what evidence supported it, and how they could refuse, correct, or revise it'). Appendix C holds a fourth, fuller version. A test described as 'one recurring ethical audit' should have one canonical wording.

**Edit.** Adopt the about.qmd formulation as canonical, since it is the fullest and is the one echoed in the part openers ('Would the design remain defensible if the people affected understood how it worked?'). Quote it verbatim here and in the Preface, each time linking to [Appendix C](appendices/appendix-c-portable-course-tools.qmd#ethical-audit). Repetition of an identical formula builds a recognizable test; repetition of three paraphrases builds nothing.  *(effort: small)*

### [MEDIUM · consistency] '## Reading layers' (line 11)

> extends the ideas into a particular domain

**Problem.** The reading-layers section promises readers four navigational devices — Research Lens boxes, optional research notes, Practice Labs, and an 'Applied Module'. The first three are delivered heavily (36 Research Lens instances across 25 chapters, 8 research notes, a Practice Lab in every chapter). 'Applied Module' is delivered exactly once in the entire manuscript, as a section heading inside ch23 ('## Applied module: market rules change the strategic game'). A reader who learns the device in the front matter will look for it 41 more times and not find it.

**Edit.** Choose one. Either promote the device — the obvious candidates are ch23's existing module, ch27 (markets), ch29's organizational culture audit, and ch42's decision canvas, which would make four and justify the name — or delete the sentence and describe only the three devices the book actually uses. The second is a one-line fix; the first is worth doing only alongside the applied-interlude decision below.  *(effort: small)*

### [MEDIUM · consistency] '## Use the recurring cases cumulatively' (line 59)

> A hiring decision lets us examine evidence, intuition, and group judgment

**Problem.** The hiring committee is promised as the book's spine in the preface, in how-to-use, and in the Part I opener ('The hiring case develops along the way'). Measured by density of hiring/candidate/applicant/committee terms, it is genuinely load-bearing in ch01 (27), ch14 (23), ch26 (18), ch11 (17), ch08 (12), ch09 (10), and ch41 (36) — and then it vanishes. Chapters 17-23, 25, 27-29, 33-34, and 36-40 carry zero or one mention. Most damagingly it is absent from ch28, the chapter about groups agreeing too easily, and from Part VII, where the preface explicitly returns to the committee ('Return to the committee room'). The supplier case shows the same pattern in reverse: strong in ch35-38, near-absent before ch18.

**Edit.** Do not force the case into chapters where it does not fit — that would produce worse examples, not better continuity. Instead close the three gaps where its absence is a missed opportunity rather than a stylistic choice: ch28 (the committee's silence is the chapter's subject), ch39-40 (the preface promises the committee-room redesign and Part VII opens with it, but the chapters deliver forms and study habits), and one chapter in Part III — ch19 or ch22 — so the spine does not disappear for seven consecutive chapters. Then revise the how-to-use sentence to say where the cases run, rather than implying they run throughout.  *(effort: medium)*

### [MEDIUM · engagement] Reading layers

> Choose a manageable example and make the output specific enough to inspect.

**Problem.** The instruction that governs every Practice Lab in the book is itself not specific enough to inspect. A student who does not already know what a good decision record looks like learns nothing from 'specific enough to inspect', and this is the sentence that determines whether the Practice Labs get done well or performed.

**Edit.** Show one three-line output immediately after: 'Weak: "I expect the new hire to do well." Inspectable: "By 1 March I expect the new hire to have completed at least three of five onboarding milestones; I will check the tracker on 3 March; if fewer than three, my read of the interview evidence was wrong."' One contrast pair teaches the standard faster than any amount of instruction, and it models the book's own discipline of recording a belief before the outcome is known.  *(effort: small)*

### [MEDIUM · structure] Reading routes

> | Your interest | Suggested route |

**Problem.** The file carries two routing devices — tbl-long-form-journey under 'The long-form journey' and this nine-row Reading routes table — separated by four intervening sections (chapter rhythm, ethical audit, find your place, recurring cases). A reader deciding how to read the book must hold the first table in mind while three unrelated topics go past, then re-orient at the second.

**Edit.** Move 'Reading routes' up to sit immediately after 'The long-form journey', so the two tables read as one navigation block: the default route, then the alternatives. The remaining sections (chapter rhythm, ethical audit, vocabulary, recurring cases) then form a coherent 'how to read a chapter' block, and the version/link policy closes the file.  *(effort: small)*

### [LOW · accuracy] Reading routes

> | Evolutionary explanations | Chapters 6 and 8, then Appendix B. |

**Problem.** Citation check on the route, not on a scientific claim. Four chapters draw on Appendix B — 6, 8, 22 (well-being and needs) and 24 (behavioral game theory) — but the route names only 6 and 8. A reader following the evolutionary thread will miss the two places where it does the most work on value and on cooperation.

**Edit.** Verify the intended route and, if 22 and 24 are meant to be included, revise to 'Chapters 6, 8, 22, and 24, then Appendix B.' If they are deliberately excluded as secondary uses, the current row is fine and needs no change — but it should be a decision, not an omission.  *(effort: small)*

---

## `index.qmd`  (13 findings)

### [HIGH · engagement] Opening scene (before the first ## heading)

> This imagined committee gives us the central question of the book

**Problem.** All 1,838 words of the Preface run on a single hypothetical committee. There is not one real study, named researcher, date, place, or published number anywhere in the front door of a book whose subtitle promises "The Behavioral Science of Choice, Influence, and Agreement." A reader deciding whether to buy or assign the book never sees the book do the thing it claims to do.

**Edit.** Keep the committee as the spine, but land two real anchors inside it. (a) In 'The environment gets a vote', use the Flint lead-pipe case the book already owns in Ch. 42: model-guided excavation found hazardous pipes in about 80 percent of digs; after priorities were changed under resident pressure, that fell to 15 percent in 2018. (b) In 'Evidence, ethics, and responsibility', name one finding that was revised (see separate finding). Two real anchors are enough; the hypothetical committee then reads as a lens, not as a substitute for evidence.  *(effort: medium)*

### [HIGH · engagement] Evidence, ethics, and responsibility

> A memorable finding can suggest a change worth making.

**Problem.** This section is the Preface's statement of scientific conscience and it is entirely meta: three short paragraphs about how the book will treat evidence, describing a revision that never happens on the page. The reader is asked to trust the discipline rather than shown it working.

**Edit.** Show one revision in two sentences, using material Appendix F has already vetted: 'Signing an honesty statement at the top of a form rather than the bottom was reported to reduce dishonest reporting (Shu et al., 2012). Five conceptual replications and a preregistered direct replication found no effect (Kristal et al., 2020), and the original article was later retracted.' Then the existing sentence 'To keep a practical lesson useful, we need to know what was tested and what would warrant revising it' has something concrete to be about, and the reader learns the book's stance rather than being told it.  *(effort: small)*

### [HIGH · engagement] The environment gets a vote

> Cheaper prediction creates opportunities whose value depends on the rest of the process

**Problem.** The Preface's most timely and saleable claim — that AI changes what decision-making requires of people — is delivered in the flattest sentence in the file: an abstract noun subject ('Cheaper prediction') acting on an abstract object ('opportunities whose value depends on the rest of the process'). Chapter 42 opens with a genuinely gripping version of exactly this point and the Preface borrows none of its energy.

**Edit.** Replace the abstraction with the case and let the abstraction follow: 'Flint, Michigan, used a model to predict which homes had lead service lines; about 80 percent of model-guided excavations found a hazardous pipe. Residents in low-risk streets objected to waiting, the city spread the digging across wards, and the hit rate fell to about 15 percent in 2018. The prediction had improved; the decision had not. Cheaper prediction creates opportunities whose value depends on the rest of the process...'  *(effort: small)*

### [HIGH · engagement] Preface, after the master-loop figure (line 16 / line 24)

> what has shaped a choice before the moment when someone appears to make it?

**Problem.** The book has a real, defensible differentiator — a six-function decomposition of any decision that turns 'bias' into a diagnosis rather than a label, carried unbroken from perception (ch3-4) to contract design (ch38) to AI (ch42) — but it is never claimed as a differentiator. The preface presents the map, the vocabulary, the ethics, and the arc, and reaches the end of its 3,000 words without a single sentence a reader could repeat to explain why this book rather than Kahneman, Thaler, or Bazerman. The first number or named study appears only in Chapter 1. A reader in the first ten pages grasps the organizing question but not what the organizing question buys them.

**Edit.** Insert one paragraph immediately after the master-loop figure (after line 26). Draft: 'Most books about decisions choose one lens. Some catalogue the errors intuition makes; some show how the presentation of a choice steers it; some teach you to argue, to listen, or to bargain. Each is useful, and none of them alone explains why a committee running a careful process still produced a hire nobody can defend. This book takes a different route. It treats a decision as six things that can each go right or wrong separately — what was noticed, what options existed, what was predicted, what was valued, what was done, and what was learned — and then asks of every finding in the book: which of those six did it change? That question is what makes anchoring a diagnosis instead of a label, and it is what lets one argument run from how the eye resolves an ambiguous image to how two firms design a contract they can both live with. You will not get a list of biases to memorize. You will get a place to put each one, and a test for whether it is the thing actually going wrong in front of you.' Claim the method; do not name rivals.  *(effort: small)*

### [HIGH · insight] Notice. Test. Ask. Design. Learn.

> This book grew from teaching behavioral economics and decision, persuasion, and negotiation.

**Problem.** The Preface never says what this book does that the well-known behavioral books do not. The differentiating commitment is present in the manuscript — the book is organized around a decision *process* rather than a catalogue of biases, and it treats a bias label as a hypothesis needing a comparison rather than an explanation — but it is never stated as a claim about the book. A reader who has read Kahneman or Thaler has no stated reason to continue.

**Edit.** Add one paragraph, most naturally at the end of 'From labels to causes' where the idea is already half-made: most treatments of this material hand the reader a list of named effects; naming an effect is not yet explaining a decision. This book is organized by the functions in the map, and every named effect is treated as a hypothesis that has to earn its place against a competing account and a specified observation. That is a defensible, non-hyped differentiator and it is what the manuscript actually delivers.  *(effort: medium)*

### [MEDIUM · clarity] Follow the decision upstream

> revise a performance forecast, expose an overlooked cost of poor coordination

**Problem.** The five feedback lessons in this sentence map one-to-one onto the five functions in @fig-master-loop, but the mapping is left implicit. The reader has to hold five clauses and five boxes in mind and pair them without help, at the moment the book's organizing framework is being introduced.

**Edit.** Name the function after each clause: '...that interview confidence was a weak signal (*notice and interpret*), suggest a work sample as another option (*construct options*), revise a performance forecast (*predict consequences*), expose an overlooked cost of poor coordination (*value consequences*), or change how the next hire is supported (*choose, commit and act*).' Five short parentheticals make the figure readable in one pass and teach the vocabulary the rest of the book uses.  *(effort: small)*

### [MEDIUM · engagement] Follow the decision upstream

> Possible actions come to mind, their consequences are anticipated, and those consequences are judged worth pursuing or avoiding.

**Problem.** Four consecutive agentless clauses ('attracts attention and is given meaning', 'come to mind', 'are anticipated', 'are judged') describe a process with nobody in it, immediately after an opening scene that had a room, a clock, and raised hands. The reader loses the committee exactly where the book's central framework is introduced, which is the worst possible place to go abstract.

**Edit.** Run the same sentence through the committee members already on stage: 'Someone notices a line in a reference letter and decides what it means. Someone else names an option nobody had raised — reopen the search. Each member privately forecasts how the candidate will handle a difficult client, then decides how much that matters against creativity.' Same five functions, same length, with agents.  *(effort: small)*

### [MEDIUM · engagement] Opening scene (before the first ## heading)

> We would need to hear how the position was defined, see which applications were read first

**Problem.** The third paragraph converts the concrete room into a list of hypotheticals, with three sentences opening 'We would need to...' in four lines. The scene stops being a scene and becomes a syllabus of things the book will later cover. This is the paragraph where a reader decides whether the book will show or tell.

**Edit.** Dramatize at least one item instead of listing it. For example, replace 'see which applications were read first' with a beat: 'The first application in the pile arrived with a recommendation from a former colleague of the chair. By the fourth CV, the committee was no longer asking who was strong; it was asking who compared well with the first one.' Keep one 'we would need to ask' as the closer so the anaphora still lands.  *(effort: small)*

### [MEDIUM · insight] From labels to causes

> Choosing a remedy before distinguishing these explanations could remove a useful source of judgment while leaving the actual problem untouched.

**Problem.** This is the sharpest idea in the Preface and it is stated only in the abstract. The counterintuitive implication — that a well-intentioned debiasing fix can destroy information and leave the real defect running — is left for the reader to construct.

**Edit.** Instantiate it in one sentence with the committee: 'If the chair responds by banning any mention of first impressions, the committee loses a genuine signal from the interview and still has no agreed meaning for *fit* — the defect that produced the problem in the first place.' The surprise (the remedy makes things worse on both counts) is what makes the point memorable.  *(effort: small)*

### [MEDIUM · structure] Notice. Test. Ask. Design. Learn.

> ## Notice. Test. Ask. Design. Learn.

**Problem.** The heading promises five named moves. The three paragraphs beneath it deliver none of them by name, and this five-verb motif appears nowhere else in the manuscript (grep returns this line only). A heading that sets up a framework and then drops it costs the reader more than a plain heading would.

**Edit.** Either earn it or drop it. To earn it, give each verb one clause tied to the exercise types the section already mentions: notice what shaped a judgment, test a forecast you wrote down, ask the question you were about to assume the answer to, design one change to the conditions, learn from a record made before the outcome was known. To drop it, retitle to what the section actually does, e.g. 'What you will be asked to do.'  *(effort: small)*

### [MEDIUM · visual] fig-master-loop caption

> An organizing map of a decision. Green feedback arrows connect observation and learning

**Problem.** The caption's opening sentence is a label ('An organizing map of a decision') rather than a claim, and the rest describes the figure's mechanics. The figure carries the book's whole organizing argument, and its caption never states the takeaway a reader should leave with.

**Edit.** Lead with the claim, keep the mechanics second: 'The visible choice is the fifth function, not the first: what people notice, which options they build, what they predict, and what they value have already happened by the time anyone votes. Green feedback arrows connect observation and learning to those five earlier functions; functions can overlap or recur, and feedback need not improve judgment.'  *(effort: small)*

### [MEDIUM · visual] When other minds enter

> The book follows an expanding journey: **choice, influence, and agreement**.

**Problem.** After @fig-master-loop at roughly word 400, the remaining ~1,300 words and six sections run with no figure, table, or callout of any kind. The stretch from 'From labels to causes' to the end is unrelieved prose, and the three-word structure that gives the book its subtitle is delivered as a single bolded phrase in the middle of a paragraph.

**Edit.** Add one compact three-row table where the subtitle is introduced: rows Choice / Influence / Agreement; columns 'Who is deciding' (one person / a person facing an audience / parties who must both say yes), 'The central question' (what shaped this judgment? / what would reasonably change this mind? / which differences permit a deal both sides can carry out?), and 'What goes wrong' (a shortcut misapplied / a case that answers the wrong concern / an agreement nobody can implement). It gives the Preface visual relief, previews Parts I-III, IV-V and VI, and makes the book's title structure legible at a glance.  *(effort: medium)*

### [LOW · consistency] Evidence, ethics, and responsibility

> footnotes provide additional methodological detail

**Problem.** This sentence restates how-to-use-this-book.qmd's 'Footnotes provide methodological details and qualifications that some readers may want to examine more closely.' The Preface spends two of its scarcest sentences on apparatus that the very next file explains properly.

**Edit.** Cut the apparatus sentence from the Preface (keep it in how-to-use-this-book.qmd) and spend the recovered space on the concrete revised finding recommended above. The Preface should earn trust by demonstration; the mechanics belong in the how-to-use file.  *(effort: small)*

---

## `parts/applied-interlude.qmd`  (1 findings)

### [MEDIUM · structure] Whole file (orphaned; absent from both _quarto-html.yml and _quarto-epub.yml)

> Markets are a demanding application of the preceding chapters

**Problem.** A complete, well-written part opener exists that frames ch27 (markets, 5,076 words) as an optional applied interlude with its own figure (master-loop-interlude.svg), its own rationale callout, and its own guiding questions. It is wired into neither build profile, so it ships in no format. Meanwhile ch27 sits inside Part IV, where it is the one chapter that does not develop the hiring or negotiation spine, and the reading-routes table already treats it as a detour ('Markets and finance | Parts I–III, then the markets chapter in Part IV'). The structural decision was made, drafted, and then left uncommitted — which is why Part IV now carries seven chapters and an argumentative seam.

**Edit.** Decide and finish. Either wire parts/applied-interlude.qmd into both profiles with ch27 beneath it — which shortens Part IV to six chapters, makes the optionality explicit for finance-track readers, and lets the reading-routes table point at a named unit rather than 'the markets chapter in Part IV' — or delete the orphan file so it stops implying an unmade decision. The first is the better book; both are better than the current state.  *(effort: small)*

---

## `parts/part-1.qmd`  (10 findings)

### [HIGH · accuracy] # Part I. How a Choice Takes Shape — roadmap paragraph 2

> The hiring case develops along the way

**Problem.** This is not true of Part I. Chapters 04, 05, 06, and 07 contain zero occurrences of "hiring," "candidate," "applicant," or "interview"; chapter 03 has a single passing clause inside a numbered list ("A hiring question about who impressed the committee highlights charisma"). The committee scene appears in chapter 01 and then vanishes for five chapters. A reader instructed to track it will conclude they missed something.

**Edit.** Either soften the promise — "Chapters 1 and 2 work the hiring case directly; the chapters that follow examine the mechanisms it depends on" — or, better, add one hiring callback sentence to each of chapters 4–7 (perception: reading confidence into an ambiguous answer; expectations: the candidate given no room to perform; valuation: what "fit" is worth today; the narrator: the reason the committee gives itself afterward) and then the sentence becomes accurate as written.  *(effort: medium)*

### [HIGH · engagement] # Part I. How a Choice Takes Shape — opening scene, paragraph 1

> A hiring committee is about to vote.

**Problem.** The preface opens the identical scene with hard specifics — "At 3:17 p.m., the chair of a hiring committee asks for a vote. Five hands rise for one candidate, two for another." Part I re-enters the same room and strips every one of them. The reader who just read the preface gets a fainter version of a scene they already have, so the opener reads as recap rather than resumption, and the stakes of the vote are never stated.

**Edit.** Re-anchor on the preface's own specifics and add a stake. E.g. "The vote is five to two. Everyone has read the same applications, yet the discussion turned on different things: one member remembers an impressive interview, another worries about reliability, a third keeps returning to the candidate they liked first. Five to two looks like agreement. It is not, and the organization is about to commit three years of a team's work to it."  *(effort: small)*

### [HIGH · engagement] # Part I. How a Choice Takes Shape — roadmap paragraph 2

> It then follows the actual process, from the evidence that attracts attention

**Problem.** This 25-word sentence names four abstract functions (attention, interpretation, expectations, values) in a chain and demonstrates none of them. It tells the reader what the part is about to do instead of doing it. Part I's chapters contain the invisible gorilla, the door swap, the hollow-face illusion, and Shirl Jennings's restored sight — four of the most arresting demonstrations in the whole book — and the opener mentions none of them.

**Edit.** Replace the abstract chain with one instance that models the whole move. E.g. "Attention comes first: people counting basketball passes fail to see a person in a gorilla suit walk through the middle of the game. What never becomes evidence cannot be weighed. What does become evidence is then interpreted through expectations, and only then valued." One concrete carries the abstraction that follows it.  *(effort: medium)*

### [HIGH · structure] Figure fig-alt, master-loop-part-1.svg

> What can we learn afterward?

**Problem.** The figure's third question misdescribes the chapter it stands for. Part I's final chapter is 07, "The Narrator After Choice: Why Reasons Are Not Always Causes" — whose point is that the account we give after the fact can be reconstructed rather than reported. "What can we learn afterward?" points at retrospective learning, which is chapter 41's subject, not chapter 07's. The part's own map mislabels its own conclusion.

**Edit.** Change the third box (in both the SVG and the fig-alt) to "Can we trust the reasons we give afterward?" and add a matching roadmap clause: "...and it ends by asking whether the explanation we offer for a choice is a report of its causes or a story assembled once the choice is made."  *(effort: small)*

### [HIGH · visual] Figure caption, master-loop-part-1.svg

> A reading route through Part I. The arrows show the progression of questions

**Problem.** This caption is a label, not a claim, and the identical boilerplate appears verbatim under all seven part figures (only the roman numeral changes). Its second clause — "The arrows show the progression of questions" — describes the graphic's syntax, which the reader can see, and duplicates the fig-alt. Compare the caption chapter 41 gives the same file at line 310: "Part VII follows a practical reading route: find the obstacle, change the conditions, and check the results." That one states something.

**Edit.** Give each part figure a sentence-length claim naming its three questions, on the chapter-41 model. Part I: "Part I moves from what the decision is, to how the judgment takes shape, to whether the reasons given afterward can be trusted." Part II: "...from what guides an intuition, to when it misleads, to what would check it." Part VI: "...from what each side can do without a deal, to where value is claimed or created, to whether the agreement can be carried out." Delete the arrows clause everywhere.  *(effort: small)*

### [HIGH · visual] Figure, master-loop-part-1.svg (applies to all seven part openers)

> ../figures/master-loop-part-1.svg

**Problem.** All seven part figures are the same 640x520 graphic — three rounded boxes, two arrows, identical <title>"The questions ahead" — and each restates three questions the same page already states in prose and again in the bullets. In Parts VI and VII the boxes are near-paraphrases of the bullets directly below them ("What are the alternatives?" / "What can each side do if we do not agree?"). Seven full-page graphics carry zero information the text does not. Worse, the filename master-loop-part-N and the anchor #follow-the-highlighted-loop in how-to-use-this-book.qmd both promise a view of the preface's decision map, and how-to-use-this-book tells readers "Each part opens with a shorter map of its own questions" — a map is what these are not.

**Edit.** Redraw all seven as the preface's master loop with this part's territory highlighted. Same six labelled functions as fig-master-loop (current context and information; notice and interpret; construct options; predict consequences; value consequences; choose, commit and act; observe and learn) plus the enclosing frame, drawn small and grey, with the functions this part covers in the live blue/teal and the rest dimmed — Part I lights notice/interpret through value; Part II lights predict consequences; Part III lights value consequences and choose/act; Part IV lights the enclosing frame; Part V and VI light choose/commit/act plus the frame; Part VII lights the frame and the green return path. Set the part's three questions as a short caption strip along the right edge rather than as the entire graphic. This gives the reader a genuine "you are here," earns the filename, makes good on how-to-use-this-book's promise, and repays seven page-sized figures with real navigational load.  *(effort: large)*

### [MEDIUM · clarity] # Part I. How a Choice Takes Shape — roadmap paragraph 2

> investigate an uncertainty that could change the decision

**Problem.** This is the value-of-information idea stated in its most abstract form, before the book has given the reader any hook for it. Chapter 2 has a perfectly concrete version on its first page: the student stops her comparison table at "work–life balance" because neither employer has told her what an ordinary week looks like.

**Edit.** Name the uncertainty: "...while a choice between two job offers shows how to construct alternatives and then chase down the one thing she cannot find on either website — what an ordinary week actually looks like." The reader now knows what "investigating an uncertainty" means before the term arrives.  *(effort: small)*

### [MEDIUM · engagement] # Part I. How a Choice Takes Shape — whole file

> Before asking who should get the job, we need to understand how these judgments took shape.

**Problem.** Part I has the flattest rhythm of the seven openers. After the four-word opening fragment, its ten remaining sentences run 33, 20, 16, 21, 24, 27, 15, 16, 16, 17 words — not one under 15, and the roadmap paragraph delivers 21, 24, and 27 in succession. The prose never lands. Part V, by contrast, varies between 6 and 25 words and reads noticeably faster.

**Edit.** Break the three long roadmap sentences with two short ones. A four-to-seven-word sentence after a 25-word sentence is the cheapest available fix: "Attention comes first." "That is the whole problem." "Five to two is not agreement." Target at least three sentences under ten words in a 300-word opener.  *(effort: small)*

### [MEDIUM · insight] ## Questions to carry forward — third bullet

> What should we record now so that the outcome can teach us later?

**Problem.** This bullet is the correct conclusion of chapter 07 but the opener never draws the line to it. The reason to record beliefs now is precisely that the explanation we produce later is partly reconstructed — that is the counterintuitive payoff of the part, and it is left entirely implicit. The bullet currently reads as generic good practice rather than as a consequence of something the reader is about to learn.

**Edit.** Add one sentence to the third paragraph: "Because the reasons we give after a decision are partly assembled once the outcome is known, what we write down before the outcome is visible becomes the only reliable record of what we actually believed." That converts the bullet from advice into an implication.  *(effort: small)*

### [LOW · visual] Figure fig-alt, master-loop-part-1.svg

> How does the judgment form?

**Problem.** The fig-alt does not match the rendered figure. The SVG's second box reads "How does the judgment take shape?" (and its <desc> says the same). Part I is the only one of the seven with this mismatch — Parts II–VII alt text matches their SVG text word for word — so a screen-reader user gets a slightly different question from the one sighted readers see, and the phrase also differs from the H1, "How a Choice Takes Shape."

**Edit.** Change the fig-alt to "How does the judgment take shape?" to match the SVG and the part title.  *(effort: small)*

---

## `parts/part-2.qmd`  (5 findings)

### [MEDIUM · clarity] # Part II. Judgment Under Uncertainty — roadmap paragraph 2

> statistical tools that make an impression testable

**Problem.** Compressed to the point of opacity. "Make an impression testable" asks the reader to hold three abstractions at once and gives no picture of what a tool would look like or what testing would involve. It is the last clause of the roadmap paragraph, where the reader most needs a foothold.

**Edit.** Name what the tools do: "...before turning to two tools that let you check an impression against something: a base rate, and a record of what you predicted before you knew the answer." Both are concrete objects the reader can imagine producing.  *(effort: small)*

### [MEDIUM · engagement] # Part II. Judgment Under Uncertainty — opening scene, paragraph 1

> tells a vivid story about rescuing a failing project

**Problem.** The opener asserts that a story is vivid instead of being vivid. It describes the existence of a compelling anecdote and then asks the reader to accept that it was compelling — which is the exact move the chapter warns against. The entire file contains no proper noun, no number, and no quoted speech.

**Edit.** Give one line of the story so the pull is felt rather than reported. E.g. "One describes walking into a project three weeks from launch with the lead developer already gone, and shipping it anyway. The other has four years of releases that arrived on time and no story about any of them. The committee must predict performance; only one of these makes performance easy to picture." The contrast now does the work the adjective "vivid" was doing.  *(effort: small)*

### [MEDIUM · engagement] # Part II. Judgment Under Uncertainty — roadmap paragraph 2

> They begin with intuitive judgment, then show how comparison and presentation affect the answer

**Problem.** Three-stage signposting with no instance, and the three stages do not cleanly cover the eight chapters: chapter 10, "Beliefs That Defend Themselves," is neither intuitive judgment nor comparison-and-presentation, and is left unplaced by this sentence (the earlier phrase "convenient to believe" gestures at it, but the roadmap does not).

**Edit.** Add the missing move and one instance: "...then show how comparison and presentation change the answer — the same treatment described as saving 200 lives or as letting 400 die draws opposite choices from the same people — and how a belief, once held, recruits the evidence that protects it." That places chapter 10 and gives the reader the framing result up front.  *(effort: small)*

### [MEDIUM · engagement] # Part II. Judgment Under Uncertainty — roadmap paragraph 2

> others give weight to what is memorable, easy to process, or convenient to believe

**Problem.** Part II contains several genuinely surprising results — that adding a plausible detail can make an event seem more likely rather than less, that a number pulled from a spinning wheel moves unrelated estimates, that people asked how fast cars were going when they "smashed" report higher speeds and remember broken glass that was never there. The opener promises only that shortcuts sometimes mislead, which no reader will find surprising, so the part opens at a lower energy than it will sustain.

**Edit.** Preview exactly one counterintuitive result and leave it unresolved: "Some of what follows is uncomfortable. Adding a detail to a description makes it less probable and more believable at the same time, and the two effects pull against each other in the same reader." A surprise stated and left open is the strongest thing a part opener can carry.  *(effort: small)*

### [MEDIUM · insight] # Part II. Judgment Under Uncertainty — paragraph 3

> A base rate may improve a forecast, a denominator may expose a misleading percentage

**Problem.** This is the best sentence in the file — three parallel moves, correctly hedged — but all three stay at the level of the move, so none of them bites. Chapter 14's worked case (a positive hiring screen and a positive medical test, rebuilt as natural frequencies) sits exactly on Part II's hiring spine and is the obvious instance for the first two clauses.

**Edit.** Attach the numbers to the second clause: "...a denominator may expose a misleading percentage — a screening test that is right 90 percent of the time still flags far more people who will not perform than people who will, once you ask how many of each there were to begin with — and a record of earlier predictions may reveal confidence that has outrun accuracy." Use chapter 14's own figures so the opener and the chapter agree.  *(effort: medium)*

---

## `parts/part-3.qmd`  (4 findings)

### [HIGH · insight] # Part III. Risk, Time, and Well-Being — paragraph 3

> daily experience, satisfaction, relationships, and meaning

**Problem.** This four-noun list flattens the most memorable thing in chapter 22 and in arguably all of Part III: that what a person predicts they will feel, what they actually feel while living it, and what they later remember feeling are three different quantities that can disagree, and that the third is what drives the next decision. As written, the sentence promises a survey of life domains. The part stops one step short of its own point.

**Edit.** State the distinction instead of the domains: "The final chapter widens the lens, and splits a single question into three that do not always agree: what you expect an option to feel like, what it feels like while you are living it, and what you will remember about it afterward. Only the third gets a vote in your next decision." That last clause is the part's payoff and is currently nowhere in the opener.  *(effort: small)*

### [MEDIUM · clarity] # Part III. Risk, Time, and Well-Being — roadmap paragraph 2

> why a gain or loss depends partly on the point from which it is judged

**Problem.** Reference dependence stated in its most abstract form, before the reader has any concrete instance and before the term exists. "The point from which it is judged" is doing heavy lifting with no support. The hedge "partly" is correct and should stay — the problem is comprehensibility, not accuracy.

**Edit.** Anchor it with chapter 17's own case: "...and shows why the same outcome is a gain or a loss depending on where you start counting. A programme described as saving 200 of 600 people and a programme described as letting 400 of 600 die are the same programme, and people choose differently between them." The abstraction then lands on an example the reader can check.  *(effort: small)*

### [MEDIUM · engagement] # Part III. Risk, Time, and Well-Being — opening scene, paragraph 1

> Imagine choosing between a secure job and a new venture.

**Problem.** Part III is the only one of the seven openers that begins with "Imagine." The other six drop the reader straight into a scene in progress — "A supplier wants a higher price," "A manager explains why a new system will save time," "Two applicants reach the final interview." The instruction to imagine holds the reader one step outside the situation, and the situation itself is generic enough that there is little to imagine.

**Edit.** Drop the framing verb and add the trade-off as a number, drawing on chapter 22's Job A / Job B case: "The offer on the table pays well and is safe. The venture pays nothing for a year and might pay nothing after that. Even with a clear forecast of success, you must give up something you value — and the option that feels exciting tonight has to survive an ordinary Tuesday in March."  *(effort: small)*

### [MEDIUM · engagement] # Part III. Risk, Time, and Well-Being — roadmap paragraph 2

> It then asks how learning from experience differs from reading probabilities

**Problem.** Four consecutive roadmap clauses, each naming a chapter's topic at the level of the topic: the comparison of risky options, reference dependence, description versus experience, present bias, mental accounting. Part III's chapters supply unusually crisp concretes for every one of these — €100 now or €120 later, the lost ticket versus the lost cash, the rare supplier failure nobody has yet encountered — and the opener uses none of them, then hands the entire concrete budget of the file to chapter 21's student.

**Edit.** Convert two of the five clauses into their instances: "...how learning from experience differs from reading a probability, when the rare failure has simply not happened to you yet; why €120 next month loses to €100 today once today arrives; and why the same fifty euros is spendable from a bonus and untouchable from savings." Keep the remaining clauses abstract so the rhythm varies.  *(effort: medium)*

---

## `parts/part-4.qmd`  (5 findings)

### [HIGH · accuracy] # Part IV. Strategic and Social Decisions — roadmap paragraph 2

> individual forecasts become prices and those prices become information for later decisions

**Problem.** This sentence states only the aggregation half of the story and reads as an endorsement of price informativeness, while the chapter it previews is titled "Markets, Mispricing, and Bubbles" and spends its length on when aggregation fails. It is the one place in the seven openers where the framing is out of step with the evidence the book actually presents. The correction is also the part's best available hook: chapter 27 reports that after Palm's first trading day, prices implied 3Com's remaining businesses were worth about negative $22 billion (Lamont & Thaler, 2003) — and that the inconsistency still was not a free lunch, because Palm shares were scarce to borrow and the distribution was delayed and conditional.

**Edit.** Balance the sentence and import the number: "Markets provide a larger setting in which individual forecasts become prices, and those prices become information for later decisions. They also show what that aggregation costs. For a stretch in 2000, prices implied that everything 3Com owned apart from its stake in Palm was worth about negative $22 billion — and the inconsistency was still not a free lunch, because the shares needed to correct it could not be borrowed." Surprise, then the resolution that keeps it honest.  *(effort: medium)*

### [HIGH · insight] # Part IV. Strategic and Social Decisions — opening scene, paragraph 1

> A team would benefit if everyone shared what they knew.

**Problem.** This generic "team" is in fact the book's hiring committee. Chapter 26 opens with exactly this scene: "A hiring committee hears the chair describe a candidate as 'an obvious leader.' Around the table, heads nod. One member had doubts about the work sample but now wonders whether the others saw something she missed; another shares those doubts but does not want to hold up the decision." Part IV generalizes away the continuity it could have had, and with it the reader's recognition that the committee from the preface has walked into a new kind of trouble.

**Edit.** Name the committee and borrow chapter 26's specifics: "The chair calls the candidate an obvious leader, and heads nod around the table. One member had doubts about the work sample and now wonders what the others saw that she missed. Another shares the doubts and does not want to be the person who holds up the decision. From outside, the two nods are identical — but one is a revised belief and one is a swallowed objection, and the committee cannot tell which it is looking at." This also sets up the part's third bullet directly.  *(effort: medium)*

### [MEDIUM · clarity] # Part IV. Strategic and Social Decisions — paragraph 3

> Understanding social behavior requires attention to the incentives and the setting

**Problem.** This is the closing sentence of the roadmap paragraph — the position where a claim should land — and it is agentless, hedged, and abstract, asserting only that context matters. It follows two much better sentences ("A public agreement may conceal private doubt; an instruction may carry different meanings in different relationships") and dissipates them.

**Edit.** Replace with a sentence that says what follows from the two preceding clauses: "The visible action is the same in each case. What the part supplies is a way to ask which of several different things just happened, because the remedy for a swallowed objection is not the remedy for a genuine change of mind."  *(effort: small)*

### [MEDIUM · engagement] # Part IV. Strategic and Social Decisions — roadmap paragraph 2

> We then ask why people cooperate, punish, follow norms, and learn from one another.

**Problem.** Four verbs, no instances, covering three chapters. Part IV holds the book's most demonstrable material — the meet-me-in-Odense coordination game, the €50 auction, ultimatum offers, the honesty box, Asch's lines, hotel towel cards — and the opener converts all of it into a list of verbs.

**Edit.** Keep the list but attach one instance to "punish," which is the counterintuitive one: "We then ask why people cooperate, follow norms, learn from one another, and pay out of their own pocket to punish someone who has cheated a stranger — a move no purely self-interested account predicts, and one that people make reliably."  *(effort: small)*

### [MEDIUM · insight] ## Questions to carry forward — third bullet

> Can this group reveal disagreement and use information that only one member holds?

**Problem.** This is the sharpest bullet in the seven openers and it is the hidden-profile problem stated exactly right — but nothing in the prose above prepares it. The opener's scene is about silence (motive), while this bullet is about distributed information (structure), and the reader has no bridge between them. The bullet arrives as a new idea in the last line of the file.

**Edit.** Add one sentence to paragraph 3: "Some of what a group needs is not withheld but simply unshared: when each member holds a different piece, groups reliably spend their discussion on what everyone already knows." The bullet then lands as the question the part has earned.  *(effort: small)*

---

## `parts/part-5.qmd`  (5 findings)

### [HIGH · accuracy] # Part V. Persuasion, Communication, and Connection — roadmap paragraph 2

> A recurring organizational-change example shows how to develop a clear, well-supported message.

**Problem.** Wrong on both counts. The organizational-change case (the shared-platform proposal) runs in chapter 30 only; chapter 31 uses Sara and the anonymous feedback comment, chapter 33 the accountability email, chapter 34 the missed-deadline exchange. More pointedly, the chapter that actually teaches how to develop a clear, well-supported message — chapter 32, "Building an Evidence-Aligned Message" — runs on a completely different case: a forecasting-assistant pitch to a restaurant owner. Appendix D confirms this ("Restaurant-forecasting pitch and hiring/deadline messages"). A reader following the opener will look for the platform proposal in chapter 32 and not find it.

**Edit.** Correct to what the part does: "A proposal to replace a familiar project system runs through the persuasion chapter, where the argument that people resist becomes a decision they can examine. A separate case — a forecasting tool pitched to a restaurant owner who needs to know how much food to prepare tomorrow — is then built from scratch into a message whose claims match its evidence." This is both accurate and more concrete than the sentence it replaces.  *(effort: small)*

### [MEDIUM · accuracy] # Part V. Persuasion, Communication, and Connection — roadmap paragraph 2

> Stories make consequences easier to imagine, while evidence helps people evaluate them.

**Problem.** This states only the benefit and omits the caution that is chapter 31's Core Idea: "a convincing account of one person can feel like evidence about everyone." Read alone the sentence is an endorsement of narrative, which is out of step with a chapter whose subtitle is "Use narrative to carry evidence, not to replace it" and whose epigraph is Feynman on fooling yourself. The caution does appear in the file — but only in a bullet, three paragraphs later.

**Edit.** Add the clause: "Stories make consequences easier to imagine, while evidence helps people evaluate them — and a convincing account of one person can feel like evidence about everyone, which is the risk that comes with the benefit."  *(effort: small)*

### [MEDIUM · clarity] # Part V. Persuasion, Communication, and Connection — paragraph 3

> The final chapter follows a difficult workplace conversation to examine honest disagreement

**Problem.** A 22-word sentence resolving into a three-noun abstraction ("honest disagreement, responsiveness, and repair when meaning or trust has been damaged"). Chapter 34's actual opening is two lines of dialogue that make the whole problem visible instantly: "This is unacceptable. We need to discuss your reliability" / "You never told me the client changed the date."

**Edit.** Use the exchange: "The final chapter starts from six words that cannot be taken back — 'We need to discuss your reliability' — and the reply that makes them unfair: the colleague was never copied on the email changing the date. There is still a late deliverable to fix, and now an accusation to repair, and explaining what the manager meant will not do both."  *(effort: small)*

### [MEDIUM · engagement] # Part V. Persuasion, Communication, and Connection — opening scene, paragraph 1

> Repeating the time-saving argument leaves the source of their resistance unanswered.

**Problem.** The best opening scene of the seven ends on a generalization about what the manager's argument fails to do, rather than on the thing the team actually says. Chapter 30 has the concrete version one page later: employees "ask who will see their activity data and when they will have time to learn the system." The opener summarizes the objection instead of letting the reader hear it.

**Edit.** End the paragraph on the question itself: "So the manager brings more efficiency figures to the next meeting. The team asks who will be able to see their activity data, and when exactly they are supposed to find time to learn the thing. Neither question is about efficiency, and neither is answered by a better number."  *(effort: small)*

### [MEDIUM · insight] ## Questions to carry forward — second bullet

> Does the message make the evidence clearer, or merely more persuasive?

**Problem.** This is the ethical hinge of the entire part — the line between persuasion and manipulation — and it is demoted to the second of three bullets, while the prose above never raises the question at all. Part V is the part where a reader most needs to be told, early, that the techniques they are about to learn work regardless of whether the claim is true.

**Edit.** Promote it into the roadmap paragraph as the part's stated commitment: "Everything in this part works whether or not the claim is true, which is why each technique arrives with the same test attached: does this make the evidence easier for the audience to judge, or only harder to refuse?" Keep the bullet as the reminder.  *(effort: small)*

---

## `parts/part-6.qmd`  (5 findings)

### [HIGH · accuracy] # Part VI. Negotiating Joint Decisions — roadmap paragraph 2

> This part follows a supplier relationship and an employment package across four chapters.

**Problem.** Neither half survives checking. Chapter 36, "Preparing and Claiming Value," runs entirely on a used-car sale — a competing offer of €8,000, a buyer reservation value of €10,000, a €9,800 target, an opening at €6,500 — and mentions no supplier and no employment package. No employment package is a running case anywhere in Part VI; the only trace in chapter 37 is a table row reading "Price / salary." And the supplier case is not one relationship: chapter 35's is a manufacturer asking a long-standing supplier for a large order before a fixed date, while chapters 37–38 run the Malhotra and Bazerman case of an ingredient supplier at $18 per pound refusing exclusivity. A reader told to track two cases across four chapters will lose the thread in chapter 36.

**Edit.** Describe what is actually there: "This part works three cases. A supplier refuses an order the buyer thought was attractive, and chapters 37 and 38 return to that refusal to build a package and then make it operable. Between them, a used car with a firm competing offer of €8,000 supplies the arithmetic of preparation — walk-away point, target, and the range in which any deal must sit." If the author prefers the current sentence, the fix is at the other end: rebuild chapter 36 on the employment package Appendix D's recurring-case map already claims for chapters 35–38.  *(effort: medium)*

### [HIGH · engagement] # Part VI. Negotiating Joint Decisions — opening scene, paragraph 1

> bargaining over that single number can leave them deadlocked

**Problem.** Part VI is the most number-dense part of the book and its opener contains no numbers at all. Chapter 36 gives a fully worked range (€8,000 / €10,000 / €9,800 / €6,500) and chapter 37 gives the single best surprise-then-resolution story in the manuscript: a supplier turns down a million pounds a year at $18 a pound and refuses exclusivity at any price, and the obstacle turns out to be a standing promise to sell 250 pounds a year to a cousin. That is a 4,000-to-1 ratio between the size of the deal and the size of the obstacle, and the opener leaves it entirely on the table.

**Edit.** Open on the puzzle: "A supplier turns down a million pounds a year. The buyer raises the price, guarantees minimum orders, and is refused again — the one condition that makes the whole investment worthwhile is the one condition the supplier will not accept. The obstacle, when it finally surfaces, is a promise to sell 250 pounds a year to a cousin. No amount of money was ever going to move it; a question would have." Then the existing generalization about price, timing, and volume lands on something.  *(effort: medium)*

### [MEDIUM · accuracy] # Part VI. Negotiating Joint Decisions — roadmap paragraph 2

> We begin with preparation: what each side can do without an agreement

**Problem.** Part VI does not begin with preparation. Chapter 35, "Negotiation as Joint Decision Design," opens the part with the supplier refusal and the reframing of negotiation as a search for a package that beats both alternatives; preparation is chapter 36. The sentence skips the part's own first chapter, which is also the chapter that establishes why the rest of Part VI is organized as it is.

**Edit.** Add the missing step: "We begin by reframing the problem — not who wins on price, but whether any package beats what each side can already do. Preparation follows: what each side can do without an agreement, what an acceptable agreement must provide, and what remains uncertain."  *(effort: small)*

### [MEDIUM · clarity] # Part VI. Negotiating Joint Decisions — opening scene, paragraph 1

> They risk losing an agreement each would prefer to walking away.

**Problem.** The sentence needs rereading. "An agreement each would prefer to walking away" makes the reader parse "prefer X to Y" across an intervening relative clause, and the sentence has to carry the part's central concept (a deal inside both parties' reservation values) at the same time. It is the pivot of the opening paragraph and it stalls.

**Edit.** Split it: "There is almost certainly a deal here that both of them would rather have than no deal at all. Arguing over price is how they lose it."  *(effort: small)*

### [MEDIUM · insight] # Part VI. Negotiating Joint Decisions — opening scene, paragraph 1

> What do they need to learn about one another's priorities to find it?

**Problem.** The question is well posed but the part's actual answer is sharper than "priorities" and is never stated. In chapter 37 what unlocks the deal is not a priority but a constraint the other side is protecting — an existing obligation that no concession on price can touch. "Priorities" suggests trading along a preference ranking; the memorable finding is that the blocking item is often something the other party cannot trade at all, and that paying more to move it is money spent on the wrong thing.

**Edit.** Sharpen the question: "What do they need to learn about one another — and is it a priority they could trade, or an obligation they cannot?" Then close the paragraph: "The difference decides whether the next move should be a better offer or a better question."  *(effort: small)*

---

## `parts/part-7.qmd`  (6 findings)

### [HIGH · engagement] # Part VII. Designing Better Decisions — paragraph 4

> Each intervention is a proposal to test.

**Problem.** This is exactly the right posture and it is asserted rather than earned — the file contains no number anywhere. Chapter 40 already holds the verified evidence that would make the sentence bite: Mertens et al. (2022) reported an average choice-architecture effect whose robustness to publication bias was disputed, Maier et al. (2022) found no clear average after adjustment, and DellaVigna and Linos (2022) found average take-up increases of 1.4 percentage points in nudge-unit trials against 8.7 points in the academic-journal comparison. That 1.4-versus-8.7 gap is the single most useful number in Part VII and it is invisible in the opener.

**Edit.** Import it: "Each intervention is a proposal to test, and the testing matters more than it sounds. Designs of the kind this part describes raised take-up by an average of 8.7 percentage points in the academic literature and 1.4 points when public nudge units ran them at scale. Both numbers are real. Only one of them describes what your redesign is likely to do." Keep the existing follow-up about whose goal it serves.  *(effort: medium)*

### [MEDIUM · clarity] # Part VII. Designing Better Decisions — paragraph 3

> examining how evidence is selected, making values explicit, testing forecasts, managing disagreement

**Problem.** The densest paragraph in the seven openers: four sentences carrying a chapter link with a section anchor, a callback to chapter 1's prediction/valuation distinction, a claim about AI and the cost of prediction, a five-item list summarizing the whole book, and a two-chapter division of labour. The five-item list in particular asks the reader to hold five abstractions with nothing between them, at the point where the book is trying to land its closing argument.

**Edit.** Break it in two and cut the list to three items. Paragraph A: the link to chapter 42 and the callback to prediction versus valuation. Paragraph B: "When prediction gets cheap, the other work does not. Someone still has to decide what the forecast is for, what a good outcome is worth, and who answers for the result. Chapter 41 builds that process; chapter 42 puts AI inside it without letting it absorb the parts that were never prediction to begin with."  *(effort: medium)*

### [MEDIUM · engagement] # Part VII. Designing Better Decisions — roadmap paragraph 2

> Behavior design asks what would make a useful action easier to repeat.

**Problem.** Three sentences, each naming one chapter's topic, none showing it — and the file's own opening paragraph has already supplied the perfect concrete two lines earlier ("the phone remains beside the keyboard"). Chapter 39 resolves exactly that scene: the laptop opens to the problem set, the first task is already written, the phone begins in another room. The opener sets up a picture and then abandons it for abstractions.

**Edit.** Finish the picture the opener started: "Behavior design asks what would make the better action easier to repeat, and the answer is unglamorous — the laptop opens to the problem set rather than the inbox, the first task is already written down, and the phone starts the morning in another room. Choice architecture asks the same question about options someone else has arranged." The student's phone then pays off instead of dangling.  *(effort: small)*

### [MEDIUM · insight] # Part VII. Designing Better Decisions — closing line

> How could its next decision be made easier to examine, challenge, and improve?

**Problem.** A strong closing question that stops one step short of the book's answer. Chapter 41 gives a specific one — preserve independent judgments before discussion, and keep a dated record of what was believed while the uncertainty was still visible — and that answer is precisely what Part I's third bullet asked the reader to carry forward ("What should we record now so that the outcome can teach us later?"). Naming it here would close a loop the book opened 42 chapters earlier; leaving it open makes the final line read as a rhetorical flourish.

**Edit.** Answer it in one clause: "We return to the hiring committee with a more useful question than whether its members are rational. How could its next decision be made easier to examine, challenge, and improve? Part I asked what the committee should write down before the outcome was known. This part is where that record gets built, and where we find out whether it survives contact with the meeting."  *(effort: small)*

### [MEDIUM · visual] Figure, master-loop-part-7.svg

> ../figures/master-loop-part-7.svg

**Problem.** This exact figure file is used twice within Part VII: here, and again at line 310 of chapters/41-decision-hygiene-build-a-process-that-can-learn.qmd, where it carries a different caption and the cross-reference id #fig-master-loop-finale. A reader who opens the part and reads two chapters meets the same three boxes twice inside thirty pages, which drains whatever navigational value the first appearance had. The chapter-41 caption is also the better of the two.

**Edit.** Keep one. If the figure's job is orientation, keep it in the part opener and replace the chapter-41 instance with something that carries chapter 41's own content (for example, the two meetings on a timeline: independent judgments recorded before discussion, the correlated discussion, the outcome, and the reconstructed memory — with the dated record shown as the only line that does not move). If the figure's job is the finale, drop it from the part opener.  *(effort: medium)*

### [LOW · consistency] # Part VII. Designing Better Decisions — paragraph 3

> [Data Driven Decision Making](../chapters/42-data-driven-decision-making.qmd#why-this-final-chapter)

**Problem.** Part VII is the only one of the seven openers that contains an inline chapter cross-link or names chapters by number ("Chapter 41 builds the process; Chapter 42 shows how to put AI to work"). The other six deliberately refer to chapters by role — "the habit chapter," "the final chapter" — which keeps the openers readable independently of the numbering. The inconsistency is visible because part openers are read in sequence.

**Edit.** Either drop the link and the numbers here ("The decision-hygiene chapter builds the process; the final chapter puts AI to work inside it"), or add one equivalent link to each of the other six openers at the point where each names its keystone chapter. Consistency either way; the first option is less maintenance.  *(effort: small)*

---

## `parts/part-8.qmd`  (1 findings)

### [MEDIUM · structure] # Part VIII. Communication and Connection {.unnumbered}

> # Part VIII. Communication and Connection {.unnumbered}

**Problem.** parts/ contains four orphan files from a retired ten-part structure — part-8.qmd, part-9.qmd, part-10.qmd, and applied-interlude.qmd. None appears in _quarto-html.yml or _quarto-epub.yml, and nothing in index.qmd, how-to-use-this-book.qmd, chapters/, or appendices/ references them. They also use a .part-overview callout class and a "Why this part comes before/after X" convention that the current seven openers dropped. Anyone editing parts/ will hit Part VIII before Part VII in a directory listing and has to work out which files are live.

**Edit.** Rename them to the retired-*.qmd convention the chapters/ directory already uses, or delete them. Before deleting, harvest two lines the current openers would be better for: part-9's "The other side is not merely an audience: they can question, refuse, counter, misunderstand, and walk away" is sharper than anything in the Part VI opener, and part-10's "Knowledge is not implementation" is a better four-word statement of Part VII's thesis than the current "The final part turns explanation into design."  *(effort: small)*

---

## `quarto-custom.scss`  (2 findings)

### [HIGH · visual] L64-L79, callout class block

> .callout.core-idea { border-left-color: var(--book-warm); }

**Problem.** 70 of the book's 160 live callouts render as undifferentiated plain notes: 31 carry no custom class at all and 39 carry a one-off class with no CSS. A reader cannot tell a fillable worksheet from a lookup table from a skippable methods aside from a binding ethical rule — they are all the same grey box. The stated premise that only four classes have CSS is also wrong: six do (.part-overview at L66 and .loop-location at L67-70 are styled too, plus a dead .evidence-boundary alias at L76).

**Edit.** Adopt the 9-type taxonomy in chapter_notes (.core-idea, .research-lens, .evidence-boundary, .tool with three level modifiers, .predict-first, .applied-module, .standard, .reference-table, .author-aside) and apply the complete 41-class mapping table. Result: 160/160 callouts carry a type, 0 render as plain notes, and the SCSS block grows from ~16 lines to ~55.  *(effort: large)*

### [LOW · consistency] L66, .callout.part-overview

> .callout.part-overview { border-left-color: var(--book-accent); }

**Problem.** All four uses of .part-overview are in parts/part-8.qmd, parts/part-9.qmd, parts/part-10.qmd and parts/applied-interlude.qmd. _quarto-html.yml lists only parts/part-1.qmd through part-7.qmd, so this CSS styles nothing in the built book. Meanwhile .loop-location has full CSS (border #6b78a8, bg #f4f5fb) for exactly one box, in ch21.

**Edit.** Delete .part-overview from the SCSS and delete the four unbuilt part files (they sit alongside the already-dead retired-*.qmd and parts/*.md). Separately, do not retire .loop-location — promote it: see the next finding.  *(effort: small)*

---
