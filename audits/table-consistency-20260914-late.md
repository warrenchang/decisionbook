# Table consistency review: Chapters 23–42 and Appendices A–G

Date: 14 September 2026. Canonical sources only. This is the late-book portion of the coordinated review; Chapter 39 edits belong to the coordinating agent.

## Scope and rule

Reviewed all 101 Markdown tables, including tables inside callouts, in Chapters 23–42 and the seven configured appendices. The source sweep found no raw HTML tables in this scope. Appendix A and Parts IV–VII contain no source tables. Excluded historical files were not treated as published chapters.

Tables should identify the level being compared. A mechanism, its subtype, an example, and a measurement procedure should not appear as unexplained peer categories. Practical workflow, routing, and comparison tables can legitimately bring different tools or questions together when their purpose and columns make that relationship explicit. Examples, studies, and normative boundaries were retained.

Result: 24 tables revised and 77 passed. This worker revised 22 tables across 13 canonical source files; the coordinating agent resolved the two Chapter 39 findings, and this worker confirmed both source fixes.

## Preservation and scientific boundary

- Preserved all pre-existing explicit anchors, every reference section, and all figure lines in the files edited by this worker. Retained the old generated cooperation-callout anchor explicitly after clarifying its heading.
- No published study, reference, empirical estimate, mathematical example, or figure was deleted. Removed taxonomy rows were relocated or integrated into the explanation; the change to Chapter 37 replaces an incoherent hypothetical rating scheme with explicit, testable hypotheses about different kinds of priority.
- The substantial pre-existing Appendix F revision remains intact. Local changes there concern the claim-family labels, experiment-setting hierarchy, and related table captions/record labels.
- Noise terminology was checked against Kahneman, Sibony, and Sunstein (2021), chapter 16 (pp. 203–204): pattern noise contains stable pattern and occasion components. The existing book reference supports the clarified terminology. No new source or unpublished-slide citation was introduced.
- Static checks verified equal table counts, retained anchors/reference sections/figures, and consistent Markdown row widths. Full reference synchronization and destination rendering belong to the coordinating agent; this worker did not render, commit, or push.

## Inventory

### appendices/appendix-b-evolutionary-explanations-of-value-choice-and-rationality.qmd

| Status | Table ID | Title or role | Finding |
| --- | --- | --- | --- |
| REVISED | `tbl-fitness-utility-welfare-morality` | Fitness, preference, well-being, and moral worth are not interchangeable | Renamed Quantity to Kind of assessment; normative value is not necessarily a measured quantity. |
| PASS | `tbl-maslow-popular-kenrick` | Three representations that should not be treated as equivalent | Compares three representations across matching dimensions; original proposal, popular simplification, and revised proposal are clearly distinguished. |
| REVISED | `tbl-rationality-standards` | Different rationality standards can produce different assessments of one behavior | Moved evolutionary explanation outside the table: an explanatory lens is not a peer rationality standard. Preserved its question and boundary in adjacent prose. |
| REVISED | `tbl-heuristics-fit-and-failure` | Heuristics and the conditions that support or weaken them | Kept recognition and availability as peer heuristics. Moved skilled intuition and the threat threshold to their own adjacent explanations; preserved learning conditions and asymmetric-error-cost logic. |
| PASS | `tbl-evolutionary-evidence` | Different evidence answers different parts of an evolutionary claim | Compares contributions and limits of evidence or analytical approaches, not exclusive causal mechanisms. |
| PASS | `tbl-evolutionary-valuation-audit` | Applying the evolutionary lens to a decision | Practical questions about one decision; explanatory, fit, and normative lenses are intentionally distinguished. |
| PASS | `tbl-bennett-five-breakthroughs` | Bennett's proposed five breakthroughs | Five attributed theoretical capacities, with matching lineage, function, and book-connection columns. |
| REVISED | `tbl-model-provenance` | A minimum provenance record for population and spatial models | Changed Model component to Aspect to document; simulation configuration and transport claims are documentation topics rather than peer model mechanisms. |

### appendices/appendix-c-portable-course-tools.qmd

| Status | Table ID | Title or role | Finding |
| --- | --- | --- | --- |
| PASS | `tbl-tool-levels` | Scale the tool to the decision rather than the number of available frameworks | Three explicitly declared levels of use and expected output. |
| PASS | `tbl-canonical-tools` | Twelve tools matched to the task and the output. | Routing table from decision tasks to practical tools and inspectable outputs; not a taxonomy of mechanisms. |
| PASS | `unnumbered-table-line-60` | One-page decision journal (unnumbered) | Seven matched journal fields use the same before/after unit; each right-hand entry answers its left-hand counterpart. |
| PASS | `tbl-tactic-diagnostic` | A diagnostic response to common bargaining tactics. | Practical tactic-response comparison; closely related deceptive claims are grouped explicitly rather than mistaken for mechanisms. |

### appendices/appendix-d-index-of-major-course-examples.qmd

| Status | Table ID | Title or role | Finding |
| --- | --- | --- | --- |
| PASS | `tbl-recurring-case-map` | Five recurring cases and the new analytical layer added when each returns. | Five recurring case families, with introduction and later development consistently separated. |
| REVISED | `tbl-extended-example-index` | Extended index of examples, their decision concepts, evidential roles, and primary chapter homes. | Changed Mechanism to Decision concept or question, matching the actual mixed conceptual coverage; standardized Chapter 9 label to representativeness. |
| PASS | `tbl-linked-video-cases` | Third-party video cases and the observation question that keeps each clip subordinate to the concept and evidence. | Index of optional teaching clips and observation questions; clips are explicitly examples, not evidence categories. |

### appendices/appendix-e-how-behavioral-evidence-is-built.qmd

| Status | Table ID | Title or role | Finding |
| --- | --- | --- | --- |
| PASS | `tbl-experimental-workflow` | Running an experimental study from definition to preservation | Five research phases with matching action and preservation outputs. |
| REVISED | `tbl-claim-families` | Claim families require different evidence | Distinguished Causal effect from Causal mechanism, avoiding a general causation category beside its more specific pathway question. |
| REVISED | `tbl-evidence-designs` | Approaches to evidence differ in how the comparison is generated | Removed laboratory and field settings as peers of randomized experiments; retained both in adjacent prose as an independent setting dimension. Marked other observational comparisons separately from quasi-experimental comparisons. |
| PASS | `tbl-research-reactivity` | Participation can alter the comparison through different pathways | Candidate participation-related pathways, each with a behavioral change and corresponding design check; pathways may coexist. |
| REVISED | `tbl-claim-design-matching` | Examples of matching claims to the evidence and assumptions that support them | Caption now explicitly identifies examples of claim-to-evidence matching, rather than implying an exhaustive taxonomy of mutually exclusive designs. |
| REVISED | `tbl-evidence-design-card` | A compact evidence design card | Aligned the claim-family field with Causal effect and Causal mechanism in the earlier classification. |
| PASS | `tbl-worked-reminder-design` | Planned design for the simulated reminder study | Fields of one explicitly simulated study; preserves units, estimand, outcome horizon, and boundaries. |

### appendices/appendix-f-when-evidence-breaks.qmd

| Status | Table ID | Title or role | Finding |
| --- | --- | --- | --- |
| PASS | `tbl-credibility-questions` | Different credibility questions require different tests | Four complementary credibility questions with matching data and diagnostic columns; not a hierarchy of rigor. |
| PASS | `tbl-research-safeguards` | Safeguards solve different credibility problems | Practical safeguards compared by purpose and needed complementary check; open practices are not represented as validity guarantees. |
| PASS | `tbl-famous-direct-replication-cases` | Prominent direct and coordinated replication cases, updated 10 September 2026 | Each row is an empirical claim with an evidence update; replication and integrity status are explicitly distinguished. |
| PASS | `tbl-famous-qualified-replication-cases` | Famous findings revised by later evidence and analysis | Each row is a conclusion qualified by later evidence; effect heterogeneity, reanalysis, and replication remain distinct. |

### appendices/appendix-literature-review.qmd

| Status | Table ID | Title or role | Finding |
| --- | --- | --- | --- |
| PASS | `tbl-literature-search-record` | A compact search and selection record | Fields of a search log, with a consistent preservation task. |
| PASS | `tbl-literature-evidence-matrix` | An evidence matrix for comparing studies | Study-extraction fields, with consistent reading questions rather than competing causal concepts. |
| PASS | `tbl-savings-review-example` | Three studies with different roles in a savings review | Three selected studies are compared on design and contribution; not presented as exhaustive evidence or equivalent assignment designs. |
| PASS | `tbl-literature-review-structure` | A writing structure in which each section advances the answer | Writing sections compared by their role in the argument. |

### chapters/23-strategic-interdependence-the-best-move-depends-on-other-minds.qmd

| Status | Table ID | Title or role | Finding |
| --- | --- | --- | --- |
| PASS | `tbl-price-war` | Illustrative price-war payoff matrix; Firm 1's payoff appears first | Two players’ action sets crossed in one illustrative payoff matrix; payoff ordering is explicit. |
| PASS | `tbl-equilibrium-boundary` | Equilibrium is a benchmark, not a portrait | Parallel contrasts between what a benchmark can and cannot establish; no example is classified as a concept. |
| PASS | `tbl-stag-hunt` | Stag hunt with a payoff-dominant and a safer equilibrium | Two players’ action sets and consistent ordered payoffs; the surrounding calculation uses the same units. |
| REVISED | `tbl-strategic-structures` | Four strategic archetypes that can overlap; the coordination rows distinguish matching from complementary actions | Clarified Coordination through matching actions, distinguishing matching from complementary actions while retaining the standard term and stated overlap among strategic archetypes. |
| PASS | `tbl-market-institutions` | Market institutions alter information, timing, and bargaining power | Three trading institutions compared by rule and strategic consequence. |

### chapters/24-behavioral-game-theory-equilibrium-is-a-benchmark-not-a-portrait.qmd

| Status | Table ID | Title or role | Finding |
| --- | --- | --- | --- |
| PASS | `tbl-beauty-contest-groups` | Descriptive number-game results used to illustrate heterogeneous strategic depth | Participant-group summaries preserve common number-game measures, sample sizes, and explicitly descriptive interpretation. |
| PASS | `tbl-three-strategic-lenses` | Three lenses on strategic behavior | Three questions for analysis are intentionally distinguished: equilibrium, individual reasoning, and population change. |
| REVISED | `tbl-strategy-diffusion-diagnostic` | Four mechanisms that can produce the same diffusion pattern | Changed Institution to Institutional change so every row names a process that could explain diffusion. |

### chapters/25-cooperation-and-social-preferences-self-interest-is-not-the-only-payoff.qmd

| Status | Table ID | Title or role | Finding |
| --- | --- | --- | --- |
| PASS | `tbl-one-shot-pd` | One-shot Prisoner's Dilemma | Two-player payoff matrix with consistent action labels and ordered values. |
| PASS | `tbl-five-rules` | Five-rule taxonomy for the evolution of cooperation | Attributed five-rule taxonomy with each row at the level of a cooperation mechanism. |
| PASS | `tbl-preference-norm` | Social preferences and social norms require different evidence | Comparison separates preferences, expectations, and enforcement by what enters the account and how it can be measured; no claimed exclusive partition. |
| REVISED | `tbl-cooperation-mechanisms` | Interaction features change the conditions for cooperation | Table now compares interaction features; moved population evolution and learning to adjacent prose as a separate level of explanation. Preserved every process, boundary, and cross-link. |

### chapters/26-social-norms-and-conformity-when-other-people-become-evidence.qmd

| Status | Table ID | Title or role | Finding |
| --- | --- | --- | --- |
| REVISED | `tbl-social-alignment-mechanisms` | Similar public alignment can have different causes | Moved information cascade from a peer row to adjacent prose as a specific social-learning pattern; retained its definition and the warning about uninformative popularity. |
| PASS | `tbl-22-1` | Auditing social evidence | Three social cues, each compared by use, failure, and test. |

### chapters/27-markets-mispricing-and-bubbles.qmd

| Status | Table ID | Title or role | Finding |
| --- | --- | --- | --- |
| PASS | `tbl-bubble-strategies` | Rule-based behavioral classifications in Haruvy and Noussair (2006): 162 classifications from 18 sessions, fractional allocation of ties, and a highest consistency score of at least 8 of 15 periods. | Shares use the same descriptive classification rule and participant denominator; unclassified share is a remainder, not a new mechanism. |
| PASS | `tbl-bubble-dashboard` | A two-direction bubble diagnostic | Four diagnostic domains each pair concern-raising and concern-lowering evidence. |
| PASS | `tbl-finance-anomalies` | Historical return patterns require competing explanations, not a single behavioral label | Five return patterns are compared as observations, with candidate explanations and rival accounts in separate columns. |

### chapters/28-authority-groupthink-and-shared-responsibility.qmd

| Status | Table ID | Title or role | Finding |
| --- | --- | --- | --- |
| REVISED | `tbl-group-failure-pathways` | Distinct pathways through which groups can suppress evidence, dissent, or action—and the safeguard matched to each pathway. | Kept Shared-information bias as the pathway; moved hidden-profile tasks to the explanatory cell instead of joining a research task to the mechanism label. |

### chapters/29-culture-and-identity-the-same-action-is-not-the-same-act.qmd

| Status | Table ID | Title or role | Finding |
| --- | --- | --- | --- |
| PASS | `tbl-culture-tight-loose` | Tightness and looseness are context-dependent trade-offs | Two norm environments with comparable potential strengths and failures. |
| PASS | `tbl-culture-face-honor-dignity` | Different cultural logics can assign different stakes to the same exchange | Same exchange events crossed with three cultural logics; modal language preserves conditional interpretation. |
| REVISED | `tbl-culture-incentive-meaning` | Incentives enter both the payoff and the relationship | Changed Intended material effect to Intended purpose so appreciation is not misclassified as a material effect; aligned introductory sentence. |
| PASS | `tbl-culture-meaning-audit` | A culture-and-identity meaning audit | Questions and exposed risks form a practical audit, not a taxonomy of culture. |

### chapters/30-persuasion-changing-minds-means-updating-models.qmd

| Status | Table ID | Title or role | Finding |
| --- | --- | --- | --- |
| PASS | `tbl-25-model-update` | A practical model-updating sequence | Practical sequence with a diagnostic question and design move at each stage; explicitly a design aid. |
| PASS | `tbl-25-barriers` | A barrier matrix for persuasive design | Barrier domains are distinct from illustrative audience thoughts and corresponding responses. |
| PASS | `tbl-25-1` | Audience conditions and elaboration | Four motivation-by-ability combinations form a complete two-by-two comparison. |
| PASS | `tbl-25-influence-signals` | Influence cues should be audited for cue validity, independence, transparency, and agency | Signals are consistently separated from valid information, counterfeit use, and diagnostic questions. |

### chapters/31-why-stories-move-minds.qmd

| Status | Table ID | Title or role | Finding |
| --- | --- | --- | --- |
| PASS | `tbl-26-1` | Narrative mechanisms, design questions, and risks | Four explicitly broad narrative mechanism families, each mapped to a design question and risk. |

### chapters/32-building-an-evidence-aligned-message.qmd

| Status | Table ID | Title or role | Finding |
| --- | --- | --- | --- |
| PASS | `tbl-27-story` | STORY as an operational model-update sequence | Five mnemonic functions, each with an operational test; not claimed as independent psychological mechanisms. |
| PASS | `tbl-27-claim-evidence` | Match the pivotal claim to evidence that can test it | Practical decision claims are compared with evidence required and what remains unestablished. |
| REVISED | `tbl-27-1` | Choose the form that supplies what the audience needs to understand | Organized overlapping communicative forms by purpose rather than presenting information, examples, anecdotes, cases, and stories as exclusive peer categories. Retained all examples and limitations. |
| PASS | `tbl-27-2` | An ethical story audit | Ethical audit criteria with consistently paired questions and warning signs. |

### chapters/33-communication-language-is-not-a-file-transfer.qmd

| Status | Table ID | Title or role | Finding |
| --- | --- | --- | --- |
| PASS | `tbl-28-recoverability` | Designing a message for recoverability | Message components have examples in a separate example column. |
| PASS | `tbl-28-1` | Grounding failures and repair moves | Communication failures, proposed sources, and repair moves are consistently separated. |

### chapters/34-connection-and-repair-warm-honesty-makes-truth-usable.qmd

| Status | Table ID | Title or role | Finding |
| --- | --- | --- | --- |
| PASS | `tbl-29-conversation-layer` | Three conversations can occupy the same words | Three conversational needs, with questions and mismatches separated; overlap is explicit. |
| PASS | `tbl-29-1` | A question ladder | Levels of inquiry are paired with example questions; examples are not additional levels. |
| PASS | `tbl-29-question-patterns` | Questions should make updating possible | Four questioning patterns with their failure and repair; practical comparison is explicit. |
| PASS | `tbl-29-2` | Separate your reaction before checking the other person’s experience | Reflective prompts divide a personal account into aspects; this is a self-check, not a taxonomy of psychological mechanisms. |
| PASS | `tbl-29-net` | Warm honesty separates observable impact from inferred motive | Paired example statements and inquiry questions illustrate two complementary conversational moves. |

### chapters/35-negotiation-as-joint-decision-design.qmd

| Status | Table ID | Title or role | Finding |
| --- | --- | --- | --- |
| PASS | `tbl-30-1` | Negotiation myths and replacement questions | Myth statements paired with hidden costs and replacement questions. |
| PASS | `tbl-negotiation-gateway-map` | The gateway map for a negotiation | Practical preparation fields with one question per field. |

### chapters/36-preparing-and-claiming-value.qmd

| Status | Table ID | Title or role | Finding |
| --- | --- | --- | --- |
| PASS | `tbl-31-preparation-test` | Preparation as a set of decisions rather than a list of wishes | Preparation domains with tasks/questions; not an exclusive taxonomy. |
| REVISED | `tbl-31-first-offer-matrix` | A first-offer decision heuristic when each side’s information can be assessed | Kept the four Good/Weak information combinations. Moved uncertainty about either side’s information quality outside the matrix into a preliminary diagnostic rule. |
| REVISED | `tbl-31-1` | The alternatives, thresholds, and offers to prepare before bargaining | Revised the caption: BATNA is an alternative, so the table is not merely a list of numbers. |

### chapters/37-creating-value-across-differences.qmd

| Status | Table ID | Title or role | Finding |
| --- | --- | --- | --- |
| PASS | `tbl-value-creation-barriers` | Three families of barriers to value creation | Three barrier families; particular biases are subordinate examples within the beliefs cell. |
| REVISED | `tbl-33-1` | Illustrative hypotheses about differences to test, not facts about a counterpart | Replaced incompatible High/Medium priority ratings, costs, tolerance, and horizons in paired columns with explicit hypotheses about the relevant difference. No invented common scale or counterpart priorities. |
| PASS | `tbl-33-information-matrix` | What different kinds of information do in negotiation | Kinds of negotiation information with parallel claiming/creation/default-use columns. |
| PASS | `tbl-37-package-scores` | A trade across differently valued issues | Four hypothetical packages compared in each party’s own units; surrounding prose warns against interpersonal addition. |
| PASS | `tbl-33-supplier-package` | Turning differences into a supplier package | Negotiable issues compared across buyer values, supplier values, and package moves. |

### chapters/38-designing-better-agreements.qmd

| Status | Table ID | Title or role | Finding |
| --- | --- | --- | --- |
| PASS | `tbl-agreement-six-questions` | Six fields that turn a package into a minimum viable agreement | Six agreement fields with consistent operational purposes. |
| PASS | `tbl-agreement-minimum-example` | A minimum viable agreement for one supplier obligation | The same six agreement fields applied to one obligation; hypothetical terms remain clearly labeled. |
| PASS | `tbl-agreement-module-routing` | Route a diagnosed agreement problem to an optional module | Diagnosis-to-tool routing with conditions of use; heterogeneous tools are legitimate responses to different problems. |
| PASS | `tbl-34-third-party-processes` | Mediation assists party choice; arbitration transfers decision authority | Mediation and arbitration compared on the same authority, purpose, fit, and risk dimensions. |

### chapters/39-behavior-design-make-the-better-action-easier.qmd

| Status | Table ID | Title or role | Finding |
| --- | --- | --- | --- |
| PASS | `tbl-behavior-design-workflow` | A minimum behavior-design record | Five practical workflow steps with outputs and governing questions; root retains ownership of Chapter 39. |
| REVISED | `tbl-21-diagnosis` | Components within COM-B and B=MAP; the frameworks overlap but organize the diagnosis differently | Coordinating agent added an explicit Framework column and all three components of each model. Motivation is defined separately within each framework. Source fix confirmed. |
| REVISED | `tbl-21-digital-loop` | Four features of a digital engagement loop and their safeguards | Coordinating agent retained four loop features and moved measurement into adjacent evaluation guidance, preserving goal attainment, well-being, and opportunity-cost checks. Source fix confirmed. |
| PASS | `tbl-21-1` | Behavior-change tools and their best uses | Practical behavior-change tools, uses, and examples; does not claim all tools are one mechanism or mutually exclusive. |

### chapters/40-choice-architecture-the-environment-gets-a-vote.qmd

| Status | Table ID | Title or role | Finding |
| --- | --- | --- | --- |
| PASS | `tbl-35-policy-tools` | Different tools for different barriers | Policy instruments compared by intervention target and example; practical toolkit legitimately crosses scope and theory. |
| PASS | `tbl-35-ethics` | An ethical choice-architecture audit | Parallel ethical audit tests with questions. |

### chapters/41-decision-hygiene-build-a-process-that-can-learn.qmd

| Status | Table ID | Title or role | Finding |
| --- | --- | --- | --- |
| REVISED | `tbl-36-noise` | Three components of noise in a judgment system | Kept three peer components: level, stable pattern, and occasion noise. Explained the pattern-noise hierarchy and moved bias and legitimate discretion to surrounding prose; discretion is not classified as a failure. |
| PASS | `tbl-ai-prediction-judgment-causation` | Prediction is one task inside accountable decision-making | Distinct tasks in an accountable decision, each with a governing question. |
| PASS | `tbl-minimum-ai-use-record` | A minimum record for consequential AI-supported judgment | Five record fields, each specifies auditable information. |
| PASS | `tbl-36-meeting` | A decision meeting organized around judgment rather than presentation | Meeting phases with process rules and intended protection. |
| REVISED | `tbl-35-decision-audit` | A decision-loop diagnostic | Explicitly labeled rows audit focuses rather than separate components of the decision loop; opportunity cost remains a diagnostic question, not a newly invented loop function. |
| PASS | `tbl-simplified-decision-journal` | A hypothetical decision journal in which every ex-post entry answers its ex-ante counterpart | Hypothetical seven-row record aligns every ex-post assessment with its ex-ante counterpart and preserves unresolved counterfactuals. |
| PASS | `tbl-35-decision-journal` | A matched decision-journal template: freeze, compare, and update | Same seven journal fields before and after the outcome. |
| PASS | `tbl-35-1` | The integrated decision audit | Practical moves with questions and tools; examples remain in the tool column. |
| REVISED | `tbl-36-proportionality` | Proportionate decision hygiene | Changed neutral activities Repeated prediction and AI-supported judgment to the diagnosed failures Inconsistent repeated predictions and Uncritical reliance on AI. |

### chapters/42-data-driven-decision-making.qmd

| Status | Table ID | Title or role | Finding |
| --- | --- | --- | --- |
| PASS | `tbl-ai-rain-losses` | The same forecast can imply different actions under different values | Two decision makers use the same forecast and common hypothetical loss units; expected-loss arithmetic is internally consistent. |
| PASS | `tbl-ai-flint-decision` | Decisions in a pipe-replacement program | Decision components applied consistently to one program. |
| PASS | `tbl-ai-workbench` | Select functions for a decision workflow; these tool families overlap | Decision tasks map to possible tools, output, and human check; overlap among tool families is explicitly stated. |
| PASS | `tbl-ai-decision-canvas` | An AI decision canvas that keeps prediction, valuation, causal evidence, and responsibility distinct | Practical pilot fields consistently ask for decisions/records before the test. |

## Files without tables

- `appendices/appendix-a-rational-choice-and-decision-analysis.qmd`
- `parts/part-4.qmd`
- `parts/part-5.qmd`
- `parts/part-6.qmd`
- `parts/part-7.qmd`

## Rendered HTML content verification

Checked the completed HTML build in `docs/` on 14 September 2026 using an independent HTML parser. All **24 revised tables across 14 source/destination pairs** appear exactly once, with **169 body rows** in total. Every rendered header and cell matches the current source after normalizing typographic quotation marks and whitespace; all 24 captions match and carry the expected chapter or appendix numbering. No source rows or cells were lost in rendering.

All **17 context checks** passed: the moved evolutionary explanation, skilled-intuition discussion, threat-threshold explanation, laboratory/field distinction, population-change account, information-cascade explanation, unknown-information rule, bias/discretion discussion, and digital-outcome measurement remain in ordinary paragraphs outside the relevant taxonomies. The noise hierarchy, overlapping strategic/communication categories, and different negotiation dimensions remain explicit.

This review checks rendered content and logical hierarchy. Screen geometry, phone readability, and EPUB checks are handled by the coordinating agent.

| Table ID | Rendered number | Body rows × columns | Content result |
| --- | --- | --- | --- |
| `tbl-fitness-utility-welfare-morality` | Table B.1 | 4 × 3 | PASS: every source cell and caption retained |
| `tbl-rationality-standards` | Table B.3 | 6 × 3 | PASS: every source cell and caption retained |
| `tbl-heuristics-fit-and-failure` | Table B.4 | 2 × 3 | PASS: every source cell and caption retained |
| `tbl-model-provenance` | Table B.8 | 4 × 2 | PASS: every source cell and caption retained |
| `tbl-extended-example-index` | Table D.2 | 54 × 5 | PASS: every source cell and caption retained |
| `tbl-claim-families` | Table F.2 | 5 × 4 | PASS: every source cell and caption retained |
| `tbl-evidence-designs` | Table F.3 | 4 × 4 | PASS: every source cell and caption retained |
| `tbl-claim-design-matching` | Table F.5 | 7 × 3 | PASS: every source cell and caption retained |
| `tbl-evidence-design-card` | Table F.6 | 12 × 2 | PASS: every source cell and caption retained |
| `tbl-strategic-structures` | Table 23.4 | 4 × 4 | PASS: every source cell and caption retained |
| `tbl-strategy-diffusion-diagnostic` | Table 24.3 | 4 × 3 | PASS: every source cell and caption retained |
| `tbl-cooperation-mechanisms` | Table 25.4 | 4 × 4 | PASS: every source cell and caption retained |
| `tbl-social-alignment-mechanisms` | Table 26.1 | 4 × 3 | PASS: every source cell and caption retained |
| `tbl-group-failure-pathways` | Table 28.1 | 5 × 3 | PASS: every source cell and caption retained |
| `tbl-culture-incentive-meaning` | Table 29.3 | 5 × 3 | PASS: every source cell and caption retained |
| `tbl-27-1` | Table 32.3 | 5 × 4 | PASS: every source cell and caption retained |
| `tbl-31-first-offer-matrix` | Table 36.2 | 4 × 4 | PASS: every source cell and caption retained |
| `tbl-31-1` | Table 36.3 | 5 × 2 | PASS: every source cell and caption retained |
| `tbl-33-1` | Table 37.2 | 5 × 3 | PASS: every source cell and caption retained |
| `tbl-21-diagnosis` | Table 39.2 | 6 × 3 | PASS: every source cell and caption retained |
| `tbl-21-digital-loop` | Table 39.3 | 4 × 4 | PASS: every source cell and caption retained |
| `tbl-36-noise` | Table 41.1 | 3 × 3 | PASS: every source cell and caption retained |
| `tbl-35-decision-audit` | Table 41.5 | 6 × 4 | PASS: every source cell and caption retained |
| `tbl-36-proportionality` | Table 41.9 | 7 × 3 | PASS: every source cell and caption retained |

**Ancillary anchor check — corrected and verified:** Quarto initially dropped `compare-the-cooperation-mechanisms` from the callout title. The coordinating agent moved the alias to the callout container and rerendered Chapter 25. An independent recheck confirms that both this alias and `tbl-cooperation-mechanisms` now resolve. Final integration checks are recorded by the coordinating agent.
