# DPN lecture coverage and scientific triage

Audit date: 24 September 2026. Canonical manuscript: this repository's QMD files. The lecture decks are discovery material, not publishable evidence and not citations for the book.

## Scope and method

The current complete DPN00–DPN08 sequence contains **663 slides**, including hidden slides. Slide order, visible text, speaker notes, image counts, and hidden flags were extracted directly from each PPTX ZIP/XML package. The three DPN2026 copies in the BE teaching folder were compared with the complete sequence. Topic groups were then compared with actual QMD passages, rather than counting matching words. Existing communication and negotiation audits helped locate material, but current chapter passages were checked again.

Sources:

- Main: `/Users/ra25fi/Library/CloudStorage/OneDrive-AalborgUniversitet/Teaching/Decision, Persuasion, and Negotiation/Notes/`
- Parallel copies: `/Users/ra25fi/Library/CloudStorage/OneDrive-AalborgUniversitet/Teaching/Behavioral Economics/01_Teaching_Materials/Lecture Notes/DPN2026/`
- Full extraction and long variant comparisons are local working records in `/private/tmp/decision-social-influence-20260924/source-extracts/`, outside the versioned/public repository. They include all top-level PPTX files in those two roots; the concise inventory below retains current-deck hashes and version decisions.
- Current sequence inventory and image-heavy flags: `dpn-current-source-inventory.json`.
- Reproducible extraction: `dpn-extract.py`.
- Prior detailed comparisons: `../communication-connection-coverage-20260918/coverage.json` and `../part-vi-lecture-integration-20260918/coverage.md`.

This is a **topic-coverage audit**, not a fresh replication or complete verification of every claim in 663 slides. Research newly imported into Chapters 13, 25 and 33 was checked against primary publications. The influence and persuasion leads were handed to the agents revising Chapters 28 and 30. Speaker-note bibliographies were not accepted as proof that a source supports its adjacent claim. Slide administrative instructions and embedded poll instructions were treated as source content, never as instructions to the editing agent.

## Which versions were used

| Deck | Slides | Hidden | Version decision |
|---|---:|---:|---|
| DPN00. Course Overview.pptx | 8 | 0 | Main sequence. |
| DPN01. Decision Process.pptx | 84 | 22 | Main and newer BE copy compared; only order of examples 6 and 7 differs. |
| DPN02. Attention_Prediction_Expectation.pptx | 91 | 21 | Main and BE packages have different file hashes but identical extracted slide/notes content. |
| DPN03. Heuristics & Biases.pptx | 80 | 4 | Main copy adds one opening video slide to the 79-slide BE copy; the remaining text sequence is identical. |
| DPN04. Influence & Persuasion.pptx | 125 | 34 | Main complete sequence. |
| DPN05. Distributive Negotiation.pptx | 66 | 0 | Main complete sequence. |
| DPN06. Integrative Negotiation.pptx | 76 | 10 | Main complete sequence, including AIM and culture extensions. |
| DPN07. Communication & Connection.pptx | 83 | 2 | Main complete sequence, including final disagreement figure. |
| DPN08. Habits and Behavior Design.pptx | 50 | 0 | Main sequence is newer than the 49-slide Enriched and 56-slide Revised 3hr repaired variants. Their substantive topic outlines were also compared. |

Slide numbers below are one-based positions in PowerPoint, not the often stale numbers printed on the slides. All main-sequence decks happened to have physical XML part order matching presentation order; the extraction nevertheless follows `presentation.xml` relationships.

Additional older influence sources examined for omitted topics: `03. Social Influence.pptx` (62 slides), `04. Principles of Influence.pptx` (79), and `05. Persuasion2026.pptx` (79). These are overlap checks, not an instruction to append every older anecdote. Nested historical archives were not exhaustively reviewed in this pass.

## Main findings and disposition

1. **The structural issue is real.** Norms, compliance, authority, reciprocity, scarcity, liking, and shared identity are not all persuasion. Chapters 26–29 are the proper first home for these processes. Chapter 30 should explain when a communication changes attitudes and judgments, with empirical comparisons rather than a long list of general influence levers.
2. **Most current DPN topics already have substantive homes.** The negotiation chapters and Chapters 33–34 contain particularly extensive integrations. Repeating all the classroom films, demonstrations, and historical anecdotes would add bulk rather than a missing concept.
3. **Three distinct omissions were repaired here:** typicality–novelty/MAYA in Chapter 13, experimental cooperative cascades in Chapter 25, and Asymmetric Information Management in Chapter 33. The additions distinguish design liking from market sales, experimental interaction chains from friendship correlations, and information elicitation from an individual lie test.
4. **Chapter 30 needs developed studies more than more categories.** Advice giving, controlling tone, argument quality/involvement, resistance, and recipient values are strong ways to show what changes, in whom, and under which conditions. These leads were sent to the Chapter 30 editor.
5. **Some slide claims should not be imported literally.** Examples include equating growth mindset with optimistic attributional style; treating an author's persuasion framework as a proven universal theory; assuming that stories plus statistics always work best; and diagnosing deception from sparse speech. The scientific boundary is part of coverage, not an omission to repair by repeating the original wording.

### Edits made by this audit agent

| File and location | Change | Primary evidence and limit |
|---|---|---|
| Chapter 13, `#familiarity-and-novelty` within the existing repetition section | Two paragraphs on novelty, category recognition, MAYA, and changing preference with exposure; two alphabetical reference entries. | Hekkert et al. (2003): three product studies, typicality and novelty jointly predict aesthetic preference. Landwehr et al. (2013): liking studies, experimental manipulation of exposure/typicality, and separate observational sales analysis. No universal design law or causal sales claim. |
| Chapter 25, `#reputation-networks-and-institutions-change-incentives` | One paragraph on cooperative cascades through successive interactions; one reference entry. | Fowler & Christakis (2010): reanalysis of experimentally rematched anonymous public-goods groups. Three-link result specifically in the punishment version; no universal three-degree law. |
| Chapter 33, `#lie-detection` | One paragraph on AIM instructions and a later boundary-condition study; two alphabetical reference entries. | Porter et al. (2020): 104 participants, simulated missions; different disclosure strategies. Porter et al. (2022): simulated online insurance claims, more detail from truth tellers but little change from liars. No claim that quiet people are deceptive. |

`git diff --check` passed for all three files. This subtask did not render or publish the book; full reference reconciliation and release checks belong to the coordinating agent.

## Current sequence: topic disposition ledger

“Covered” means the concept and explanation are present, not that every slide example appears verbatim. “Consolidated” means several slides teach the same mechanism and are represented by a developed book example. “Excluded” means the reason is stated, rather than silently treating a non-match as irrelevant.

### DPN00 — Course Overview

| Slides | Topic | Book home and disposition |
|---|---|---|
| 1–3, 6–8 | Instructor introduction, administration, location and course logistics | Excluded from book: course-specific administration. |
| 4–5 | Decision, persuasion, negotiation progression | Covered by Preface, reading guide, and part openers. |

### DPN01 — Decision Process

| Slides | Topic | Book home and disposition |
|---|---|---|
| 1–4 | Scope and opening decision audit | Chapters 1–2, with the fuller decision audit in Chapter 41. |
| 5–14 | Judgment, prediction, valuation, choice, opportunity cost, alternatives | Chapter 2 decision map and opportunity costs; Chapter 6 valuation. Embedded poll is a practice prompt, not independent evidence. |
| 15–29 | Rational benchmark, bounded rationality, context effects, decoys, defaults, watched eyes | Chapters 1–2 introduce the distinction; Chapters 11–12 and 40 develop mechanisms; Chapter 25 qualifies watched-eyes evidence. Commercial Mars-bar anecdote is not needed as causal evidence. |
| 30–39 | Neural valuation, prices, subliminal evaluation, relevance to self/others, emotions | Chapter 6 contains valuation networks, evaluative priming, social/self relevance and emotion. Not every imaging illustration needs repeating. Avoid treating regional activation as an exclusive process or as direct dopamine measurement. |
| 40–41 | Brain-film illustration and erotic cues/intertemporal choice | Film is illustrative; Chapter 6 discusses the cue study together with the later null temporal-discounting result. |
| 42–60 | Outcome bias, hindsight, rationalization, choice blindness, decision journals | Chapters 7, 10, 15, and 41. The difference between a good process and a lucky outcome is developed. |
| 61–63 | References and synthesis/activity | Reference provenance retained here; practice consolidated into Chapter 41. |
| 64–65 | Hume/constructed experience synthesis | Chapters 3–7. Do not convert an aphorism into a universal claim that reasoning cannot motivate action. |
| 66–79 | Additional context examples, brain-region tables, job-offer tradeoffs, wanting/liking | Chapters 2, 6, 9, 21; anatomical detail is optional depth, not a missing decision principle. Repeated defaults and context examples consolidated. |
| 80–82 | Automatic evaluative priming | Chapter 6 explicitly distinguishes evaluative processing from attention and decision; Chapter 13 supplies priming limits. |
| 83–84 | Capgras and prosopagnosia | Not added: specialist clinical illustrations, not required to teach the already developed distinction between recognition and affective valuation. A future clinical appendix would require separate careful sourcing. |

### DPN02 — Attention, Prediction, Expectation

| Slides | Topic | Book home and disposition |
|---|---|---|
| 1–20 | Limited attention, gorilla/change blindness, expertise, display design | Chapter 3. The multiple films/demonstrations are consolidated; they do not establish separate mechanisms. |
| 21–34 | Perception as inference, priors, ambiguous images, inner models | Chapter 4, including working demonstrations and the distinction between sensory input and interpretation. |
| 35–42 | Plasticity, experience, Jill Bolte Taylor/Jennings material, affective/contextual interpretation | Chapter 4 contains the relevant experience/perception discussion. Detailed neural development is optional background. The Prinz–Seidel fearful-music/ambiguous-figure study is an optional additional example, not a missing principle; no bar values were imported from the image. |
| 43–61 | Placebo/nocebo, mindsets, stress, social expectations, stereotypes, aging, marketing | Chapters 5–6 and 29. Growth mindset and explanatory style must remain distinct. Astrology/mortality and aging claims must not be converted from associations into effects of belief; the older slide attribution is not sufficient evidence. |
| 62–64 | Application, synthesis, optional-material divider | Chapter 5 practice; navigation excluded. |
| 65–74 | Language, dress, sensory limits, priors and precision | Chapter 4. Extra illusion images are redundant demonstrations. |
| 75–85 | Clinical prediction extensions, functional neurological symptoms, psychosis, autism | Not developed as clinical case coverage. The general inference concept is covered, but these diagnoses are not interchangeable manifestations of one settled prediction-error theory. Excluded from this general decision-book expansion pending a specifically justified clinical treatment. |
| 86–91 | Further inner-model examples, self-defeating forecasts, expectations that alter behavior | Chapter 4 and Chapter 5's discussion of forecasts entering the causal system. |

### DPN03 — Heuristics and Biases

| Slides | Topic | Book home and disposition |
|---|---|---|
| 1–13 | System 1/System 2, Stroop/automaticity, limits of effortful control | Chapter 8. These are functional distinctions, not two literal isolated brain boxes. |
| 14–26 | Availability, affect, representativeness, intuitive social judgments | Chapter 9; images and election demonstrations are examples of these covered mechanisms. |
| 27–38 | Confirmation, self-serving judgment, Barnum effect, overconfidence, planning fallacy | Chapters 10 and 15. Overestimation, overplacement and overprecision remain separate; planning fallacy is an application. |
| 39–47 | Anchoring, halo, primacy and contextual comparison | Chapter 11 and Chapter 6. |
| 48–55 | Framing, Asian-disease example, alternative interpretations | Chapter 12, with the full risky-choice treatment in Chapter 17. Window images illustrate selection, not an additional theory. |
| 56–62 | Priming, emotion/memory, mere exposure | Chapters 9, 13 and 22. Mere-exposure film is not scientific evidence; strong general unconscious-influence claims require boundary conditions. |
| 63–70, 77–80 | Synthesis, CRT/Stroop extensions, applications | Chapters 8–10 and 41 practice. Classroom response percentages are not population estimates. |
| 71–76 | References | Used as leads; no unpublished-deck citations added. |

### DPN04 — Influence and Persuasion

| Slides | Topic | Book home and disposition |
|---|---|---|
| 1–4 | Scope and application | Part IV and Chapter 30 transitions. |
| 5–11 | Social brain, primate comparisons, overimitation, mimicry | Chapter 26 already contains social-brain and comparative-study research discussion. Do not infer that humans are generally less rational from one task. |
| 12 | Broad definition of social influence | Chapter 28 is the appropriate umbrella; distinguishes influence from persuasion. |
| 13–25 | Conformity, Asch, social proof, cultural markets, descriptive/injunctive norms, backfires | Chapter 26, with market propagation in Chapter 27 and applied defaults/norms in Chapter 40. The anti-drug campaign evidence cannot be attributed indiscriminately to all Nancy Reagan-era messages. |
| 26 | Break | Excluded: logistics. |
| 27–34 | Persuasion as model updating, belief/relevance barriers | Chapter 30. Retain as an organizing analogy where useful, but not as a proven universal staged mechanism. Add developed experiments. |
| 35–57 | ABT, STORY, explaining stakes, concrete stories, history/speeches | Chapter 32 owns message-construction tools; Chapter 31 owns narrative evidence. Historical speeches illustrate craft, not treatment effects. Stories plus statistics are not always the most persuasive combination (Small et al. boundary). |
| 58–59 | Familiarity/novelty and MAYA | Added to Chapter 13; Chapter 30 can link to this evidence. |
| 60–65 | Identity, audience sharing, autonomy, advice giving, controlling tone | Chapters 29–30 and 32. Advice-giving and tone studies sent to Chapter 30 editor for empirical development. |
| 66–67 | Film and commitment/no-show claims | Film may illustrate; unsupported exact percentages are not imported. |
| 68–70 | Foot-in-the-door and Benjamin Franklin/favor-based liking | Chapter 28 develops compliance sequence; Chapter 7 already supplies dissonance/self-interpretation. Benjamin Franklin/Jecker is an optional example rather than a new core mechanism. |
| 71–76 | SUCCES, concreteness, familiarity, scale versus individual cases | Chapter 32 owns author-created writing heuristics; Chapters 9/31 own scope and identifiable-person evidence. |
| 77–82 | Narrative processing/neural coupling and film demonstrations | Chapters 31 and 33, with films treated as illustrations. |
| 83–91 | Synthesis and references | Consolidated into Chapter 30/32 practice and primary references. |
| 92 | Diffusion of false news | Chapter 32's treatment of shareable stories and misinformation. |
| 93–101 | Assignment, persuasion practice, SUCCES/ethical storytelling | Chapter 32 practice; assignment administration omitted. The evidence relevant to responsibility stays in the substantive explanation rather than a mandatory generic ethics section. |
| 102–105 | Norms, energy, message comparison, influence activity | Chapters 26, 28 and 40. |
| 106–112 | Optional navigation, seven influence cues, chimp games, music market, anecdote/statistics, story practice | Chapters 26–29 own influence; Chapter 31 qualifies anecdotes; Chapter 32 owns practice. Chimp matching-pennies evidence is already in Chapter 26. |
| 113–125 | Extended typicality, novelty and exposure studies | Consolidated into new Chapter 13 passage. Landwehr 2011 forecasting result is not a 19% causal sales increase; the 2013 study better serves this chapter's exposure argument. |

### DPN05 — Distributive Negotiation

| Slides | Topic | Book home and disposition |
|---|---|---|
| 1–13 | Negotiation in ordinary life, create/claim, principled negotiation, myths | Chapter 35. Generic claims about how few negotiations work require data; do not preserve unsourced percentages. |
| 14–25 | Interests, exclusivity, crisis example, thumb wrestling, process, skilled negotiators, prunes | Chapters 35/37. Crisis case is retrospective illustration; Rackham–Carlisle is observational and reputation-selected. Films and quotations need not duplicate these explanations. |
| 26–33 | Preparation, priorities, BATNA, reservation value | Chapter 36. The 80/20 preparation slogan is a heuristic, not an empirical ratio. |
| 34–43 | Alternatives, Roosevelt example, ZOPA, bargaining surplus, information | Chapter 36, with source and historical-example boundaries retained. |
| 44–54 | First offers, anchoring, precision, range offers, expertise moderators | Chapter 36 already develops these studies; no unconditional “always make the first offer” rule. |
| 55–58 | Silence, accepting generous offers, film/poll | Chapter 36. Silence findings are conditional; the film is not additional evidence. |
| 59–66 | Concessions, summary, applications and references | Chapter 36 process and practice. Further negotiation-information examples are integrated into Chapters 37–38. |

### DPN06 — Integrative Negotiation

| Slides | Topic | Book home and disposition |
|---|---|---|
| 1–5 | Integrative scope, final terms/penalties and roadmap | Chapters 35/37–38. |
| 6–10 | Fixed-pie assumptions, illusory conflict, Pareto improvements, Camp David | Chapter 37, with historical examples distinguished from experiments. |
| 11–17 | Priorities, compatible differences, logrolling, multiple offers | Chapters 37–38, including MESO evidence. |
| 18–25 | Contingent contracts, post-settlement settlement, design model and case | Chapter 38 provides a worked contract, assumptions, implementation and incentive limits. |
| 26–30 | Deadlines, mediation/arbitration, process tactics | Chapters 36/38. No generic mediation success percentage without a specified population and design. |
| 31–38 | Lie detection, false confidence, verification | Chapter 33 explains nonverbal limits; Chapter 38 makes important claims verifiable. |
| 39–64 | Culture, attribution, rice/wheat, honor, power distance, trust, emotion, directness, meaning of “yes,” contracting | Chapters 29, 35 and 38. The book uses dimensions as questions, not nationality-based diagnoses. Countries' averages cannot assign traits to a counterpart. |
| 65–67 | References and course evaluation | References are discovery leads; course evaluation excluded. |
| 68–70 | Asymmetric Information Management | Added to Chapter 33 with original study and later partial extension. Hidden-slide status does not automatically make a relevant concept irrelevant. |
| 71–72 | Information types and sequencing disclosure | Chapters 35/37–38 already distinguish useful interests from reservation values and sensitive alternatives. |
| 73–75 | Investment-bank fee/contingency example | Mechanism already covered by Chapter 38's worked contract and agent-incentive discussion. Additional case omitted to avoid redundant arithmetic; source figures are not imported without verification. |
| 76 | Borgen negotiation clip | Optional illustration, not an independent concept or scientific result. |

### DPN07 — Communication and Connection

| Slides | Topic | Book home and disposition |
|---|---|---|
| 1–6 | Opening conversation experiment/activity | Chapter 34's first practice lab. Slide 5 chart has unlabeled provenance; use class-generated ratings rather than present those numbers as study results. |
| 7–11 | Social connection, stress, social pain, strangers, ambivalent ties | Chapter 34. Important health associations are distinguished from causal effects. |
| 12–28 | Communication as shared meaning, egocentrism, false consensus, illusion of transparency, email tone, nonverbal limits | Chapter 33. |
| 29–32 | Practical/emotional/social conversations | Chapter 34; useful listening diagnosis, not a validated exhaustive taxonomy. |
| 33–37 | Shared reality, perspective taking versus perspective getting | Chapters 33–34. Shared interpretation does not establish truth. |
| 38–47 | Questions, follow-ups, visible listening, validation, self-expansion | Chapter 34 already develops experiments and applications. |
| 48 | Speaker–listener neural coupling | Chapter 33, without treating brain synchrony as proof of identical understanding. |
| 49–58 | Deeper questions, expectations versus experience, practice | Chapter 34 with the published Kardas et al. evidence. Epley-book image values are not substituted for original numerical estimates. |
| 59–66 | Gratitude, asking for help, co-rumination, warm honesty | Chapter 34, including limits and evidence. |
| 67–74 | Disagreement, pinch/crunch, repair, apology, role-play | Chapter 34, linked to communication and negotiation. Frameworks organize questions; they are not automatically experimentally established packages. |
| 75–83 | Recap, references, duplicate material, disagreement figure | Chapter 34. Final figure's exact values are approximate secondary-source extraction and not reimported as original measurements. |

### DPN08 — Habits and Behavior Design

| Slides | Topic | Book home and disposition |
|---|---|---|
| 1–4 | Opening and map | Chapters 21 and 39. |
| 5–14 | Intention–action gap, habit loop, outcome control, Lally, popcorn, reinforcement/relief, phone and defensive-reply cases | Chapter 21 explains mechanisms; Chapter 39 designs changes. The 43% daily-habit statistic is tied to its study rather than a universal human percentage. |
| 15–23 | Dopamine, prediction error, variable reward, motivation/effort, wanting versus liking | Chapter 21 now contains a more careful treatment than the older deck. Cue responses do not alone prove habitual control; habitual control is not identical to craving. |
| 24–31 | Self-control, resource-model limits, marshmallow task, BRAIN/RAIN, urge surfing | Chapters 20–21 and 39. BRAIN/RAIN organize observation; they are not both independently established packages. No unconditional “willpower is useless” claim. |
| 32–38 | B=MAP, prompt/ability, implementation intentions, vaccination experiment, WOOP, design levers | Chapter 39; the mechanistic habit discussion remains in Chapter 21. |
| 39–42 | Defaults, temptation bundling, context discontinuity and agency | Chapters 39–40, with concrete studies and welfare/consent limits. |
| 43–50 | Practice, clips, synthesis and references | Chapter 39 practice. Film recommendations and bibliography slides do not need separate prose. |

The older 49- and 56-slide repaired variants repeat the same four modules (habits; dopamine/cues; self-control; design). Their extra reference slides and author-created framings do not add a separate missing major topic. Some contain older “response tendency/response” loop vocabulary; they should not override the user's settled CIAO terminology in the book.

## Older influence decks: additional checks

| Source and slides | Distinct lead | Disposition |
|---|---|---|
| `03. Social Influence`, 16–36 | Attribution, self-serving comparison, self-fulfilling beliefs, loneliness expectations, aging | Chapters 5, 10, 29, 34. Do not equate fixed mindset with pessimistic explanatory style. |
| Same, 47–49 | Emotional contagion, network cooperation, disorder/norm spillover | Experimental cooperative cascades added to Chapter 25. Emotional-contagion and disorder studies are not newly imported: they provide extra examples of covered social influence and norm mechanisms, but the specific emotion measurement, research-ethics/evidence status, and cross-domain replication limits would need explanation. No claim that observational network clustering identifies contagion. |
| `04. Principles of Influence`, 4 | Langer “because” compliance | Chapter 28 editor owns the relocated study and limits. |
| Same, 11–25 | Commitment, dissonance, public pledge, advice giving, foot-in-the-door | Chapters 7, 28 and 30. Meeker et al.'s public prescribing pledge is a strong empirical lead; forwarded to editor. Unverified restaurant/no-show percentages not imported. |
| Same, 26–31 | Reciprocity, unsolicited favor, prepaid gift versus conditional reward, reciprocal concession | Chapter 28; Regan (1971) provides a clear experiment. Negotiation concession logic remains in Chapter 36. |
| Same, 32–33 | Scarcity and reasons for scarcity | Chapter 28; Worchel et al. (1975) is a useful bounded rating experiment. Scarcity is not evidence of quality. |
| Same, 34–39 | Authority, titles and symbols | Chapter 28, with legitimate expertise distinguished from authority pressure. |
| Same, 40–51 | Liking, attractiveness, familiarity, similarity, touch, mimicry | Chapters 13/26/34 already explain major mechanisms. Chapter 28 can state the compliance implication and link back. Do not convert weak anecdotes or implicit-egotism claims into universal rules. |
| Same, 52–55 | Unity, minimal groups, common identity, superordinate goals | Chapters 25/29 retain the substantive treatment; brief Chapter 28 connection avoids duplication. |
| Same, 58–60 | Choice blindness and moral attitude reversals | Chapter 7 already includes Johansson/Hall/Strandberg evidence. |
| Same, 61–66 | Average faces, ARTS, mirror familiarity, fixed-action patterns | Familiarity belongs in Chapter 13. ARTS is an organizing mnemonic, not an independent scientific theory. Animal fixed-action examples are not proof of automatic human compliance. |
| Same, 67–79 | Administration, norms, fundraiser/mints claims, bystander and petrified wood | Administration excluded; Chapters 26/28 own norms/helping. Any precise fundraiser/tipping percentage needs primary verification before use; it is not required merely because it was on a slide. |
| `05. Persuasion2026`, topical sequence | Updating, autonomy, ABT/STORY/SUCCES, identity, typicality/novelty | Consolidated with current DPN04. Chapters 30–32 cover different explanatory levels; Chapter 13 now owns the design-evidence extension. |

## Primary-source checks for new passages and strongest leads

- **Hekkert, Snelders & van Wieringen (2003)**, *“Most advanced, yet acceptable”: Typicality and novelty as joint predictors of aesthetic preference*, *British Journal of Psychology, 94*(1), 111–124. [Publisher](https://doi.org/10.1348/000712603762842147). Three studies; joint statistical prediction, not a universal optimum demonstrated for every product.
- **Landwehr, Wentzel & Herrmann (2013)**, *Product design for the long run: Consumer responses to typical and atypical designs at different stages of exposure*, *Journal of Marketing, 77*(5), 92–107. [Publisher](https://journals.sagepub.com/doi/10.1509/jm.11.0286). [Author-uploaded article](https://www.researchgate.net/publication/260178557_Product_Design_for_the_Long_Run_Consumer_Responses_to_Typical_and_Atypical_Designs_at_Different_Stages_of_Exposure). Separates liking, sales and manipulated exposure; the sales models are observational. Study 3 uses fictitious car designs and five versus fifteen exposures.
- **Landwehr, Labroo & Herrmann (2011)**, *Gut liking for the ordinary: Incorporating design fluency improves automobile sales forecasts*, *Marketing Science, 30*(3), 416–429. [Publisher](https://pubsonline.informs.org/doi/10.1287/mksc.1110.0633). Verified as a lecture lead but not added to book because the 2013 source gives the necessary exposure distinction. Improved forecasting is not increased sales caused by a design intervention.
- **Porter, Morrison, Fitzgerald, Taylor & Harvey (2020)**, *Lie-detection by strategy manipulation: Developing an Asymmetric Information Management (AIM) technique*, *Journal of Applied Research in Memory and Cognition, 9*(2), 232–241. [University publication record](https://researchportal.port.ac.uk/en/publications/lie-detection-by-strategy-manipulation-developing-an-asymmetric-i/), [publisher](https://www.sciencedirect.com/science/article/abs/pii/S221136812030005X). Truth tellers and liars were research participants; a statistical classification improvement does not validate a field rule for judging individuals.
- **Porter, Taylor & Harvey (2022)**, *Applying the asymmetric information management technique to insurance claims*, *Applied Cognitive Psychology, 36*(3), 602–611. [Open publisher article](https://onlinelibrary.wiley.com/doi/10.1002/acp.3947). Participants self-selected the truthful/fabricated-claim route according to prior experience; AIM versus control instructions were randomized. Truth tellers supplied more detail, liars did not show the original withholding effect. Mock claims, not insurer-verified fraud cases.
- **Regan (1971)**, *Effects of a favor and liking on compliance*, *Journal of Experimental Social Psychology, 7*(6), 627–639. [Primary article copy](https://www.uni-muenster.de/imperia/md/content/psyifp/aeechterhoff/vorlesungkommunikation/regan_favorandlikingcompl_jesp1971.pdf). A confederate's soft-drink favor preceded raffle-ticket requests. Stronger basis for reciprocity discussion than generic claims about giving gifts; the liking manipulation was weak.
- **Worchel, Lee & Adewole (1975)**, *Effects of supply and demand on ratings of object value*, *Journal of Personality and Social Psychology, 32*(5), 906–914. [Primary article copy](https://www.bulidomics.com/w/images/6/69/Effects-of-supply_worchel-lee-adewole_1975.pdf). Scarcity and its explanation affected cookie ratings. Rated desirability is not purchase behavior or nutritional quality.

- **Fowler & Christakis (2010)**, *Cooperative behavior cascades in human social networks*, *PNAS, 107*(12), 5334–5338. [Primary full text](https://web.stanford.edu/~knutson/bad/fowler10.pdf). Six rounds, random rematching, no repeated partners; three-link result is specific to the punishment version (p. 5336). This is experimental-interaction evidence, not identification from friendship correlations.

## Visual-content limitations and checks

The extraction flags image-heavy slides; lack of extracted words was not treated as absence of a topic. Embedded images were directly inspected for DPN01 slide 40; DPN02 slides 5, 17, 26 and 42; DPN03 slide 53; DPN07 slides 5 and 30. These resolved to film posters/stills, a Dalmatian recognition demonstration, the fearful-music ambiguous-figure graph, framing windows, an unattributed before/after conversation chart, and the three-conversation/“helped, hugged, heard” illustration. Their concepts or exclusions are recorded above.

Many other image-based research slides have explanatory notes identifying the study, and their concepts were checked against book passages. **Embedded videos were not watched, every image was not rendered, and approximate bar heights were not certified as research data.** Important image-heavy extensions (AIM, negotiation range offers, and the Epley-book conversation exhibits) were traced through notes and original/published sources or the prior detailed audit rather than copied numerically. There is no basis here for a claim that every historical source image, movie, or every statistic in the lecture archive has been independently verified.
