# Context, mood, and associative memory

Revision requested: integrate the scuba-diving memory experiment and explain how associative retrieval can contribute to context-dependent judgment, availability, and affect, using an argument with a spouse as an illustration.

## Editorial placement

- Chapter 13 expands the existing `context-dependent-memory` passage within “Accessibility: memory prepares an answer.” No additional section heading was added.
- The new `mood-memory-and-judgment` anchor supports a short connection from Chapter 9's availability discussion. The full relationship example appears only in Chapter 13.
- The relationship scenario is explicitly hypothetical. It is not attributed to the author or presented as an experimental finding.
- Mood-dependent retrieval (matching the state during learning) is distinguished from mood-congruent retrieval (the emotional content of what comes to mind).
- Associative retrieval is presented as one contributor to judgment. The text also retains the direct feelings-as-information route; it does not claim memory mediates every affect effect.

## Sources checked on 2026-09-19

| Source | Design and finding used | Use in the revision |
| --- | --- | --- |
| Godden & Baddeley (1975), [publisher record](https://bpspsychub.onlinelibrary.wiley.com/doi/pdf/10.1111/j.2044-8295.1975.tb01468.x); [original article](https://app.nova.edu/toolbox/instructionalproducts/edd8124/fall11/1975GoddenBaddeley.pdf) | Divers learned and freely recalled word lists in all four land/water combinations. The original study found better recall with matching learning and retrieval environments. | Describes the original finding, without a numerical effect-size claim or extrapolation to recognition, general intelligence, or decisions. |
| Murre (2021), [full article](https://pmc.ncbi.nlm.nih.gov/articles/PMC8568063/) | Sixteen divers in an indoor-pool replication; no matching-context advantage. Setting, timing, and other procedures differed. | Brief footnote records the unsuccessful replication. Procedural differences are not offered as a proven explanation for the discrepancy. |
| Smith & Vela (2001), [author-hosted meta-analysis](https://people.tamu.edu/~stevesmith/Smith%26Vela2001.pdf) | Environmental-context effects across studies; reduced effects with strong noncontextual cues or mental reinstatement of the learning context. | Grounds the broader account of environmental cues beyond the single diving experiment. |
| Bower (1981), [original article](https://www.researchgate.net/profile/Gordon-Bower/publication/229068090_Mood_and_memory/links/00b7d51c1d6e15c434000000/Mood-and-memory.pdf); [bibliographic record](https://pubmed.ncbi.nlm.nih.gov/7224324/) | Reports mood and memory experiments and develops an associative-network account, including reciprocal activation of emotion and associated experiences. | Presents an associative account, not a demonstrated unique neural mechanism or a universal rule about all moods. |
| Eich, Macaulay, & Ryan (1994), [abstract and bibliographic record](https://pubmed.ncbi.nlm.nih.gov/8014613/); [original article](https://www.researchgate.net/profile/Eric-Eich-2/publication/15183858_Mood_Dependent_Memory_for_Events_of_the_Personal_Past/links/53e159460cf2d79877a85b4f/Mood-Dependent-Memory-for-Events-of-the-Personal-Past.pdf) | Three experiments: autobiographical events were generated under induced mood, then recalled two or three days later. Matching generation and recall moods improved recall. | Supports the mood-dependent definition and the carefully specified example of generating and later recalling personal memories. No claim that researchers controlled the mood during the original life event. |
| Teasdale & Fogarty (1979), [original abstract and article text](https://www.researchgate.net/publication/22641233_Differential_effects_of_induced_mood_on_retrieval_of_pleasant_and_unpleasant_events_from_episodic_memory) | Induced happy and depressed moods in students; relative retrieval latency for pleasant versus unpleasant autobiographical experiences changed with mood. | Supports the mood-congruent retrieval illustration. The text describes an induced sad mood, not clinical depression, and does not claim a measured effect on marriage. |
| Isen, Shalker, Clark, & Karp (1978), [author-hosted original article](https://clarkrelationshiplab.yale.edu/sites/default/files/files/Affect,%20accessibility%20of%20material%20in%20memory%20and%20behavior_%20A%20cognitive%20loop.pdf) | Separate studies of positive mood: more favorable product evaluations and enhanced recall of positive material. Authors propose an accessibility-based cognitive loop. | Supports the possible memory contribution to mood and judgment; the prose does not claim that the two studies establish mediation. |

The existing Schwarz & Clore (1983) reference is also included in Chapter 13 to support the direct feelings-as-information contrast already discussed in Chapter 9. That reference is shared with the master bibliography, not duplicated there.

## Interpretation and practical application

The spouse scenario is an application of the associative account: accessible disappointments can bias the sample of experiences used to judge a relationship. The text says remembered incidents may be accurate while their apparent representativeness is exaggerated. It recommends attending to the specific hurt and later reviewing experiences that both support and challenge the broader impression. It does not infer that every disagreement reflects memory bias, or that a positive counterexample negates a serious problem.

No study data, figures, or effect sizes were created or altered.

## Verification

- Full HTML and EPUB builds completed successfully.
- Reference synchronization: 1,036 unique references; six new works added to the master bibliography.
- `qa_quarto_book.py`: zero errors and zero warnings.
- `qa_epub_release.py`: zero errors; staged and released EPUBs match.
- Figure and table reference check: 62 configured sources, 96 figures, 166 tables, zero issues.
- The new paragraphs, retained context anchor, new mood anchor, replication footnote, and Chapter 9 link were checked in both HTML and EPUB; results are in `render-checks.json`.
- Desktop (1,400 px) and phone (390 px) screenshots were inspected. The passage is readable with no page-level horizontal overflow.
- `git diff --check` passed. Unrelated generated file-mode changes and one verified attribute-order-only HTML change were restored to the baseline.
