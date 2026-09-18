# Chapter 20: future self and patience

Date: 2026-09-18. Canonical source: `chapters/19-intertemporal-decision-making-why-later-loses-to-now.qmd`. The filename retains an older number; both current Quarto profiles and rendered HTML place Intertemporal Decision Making at Chapter 20. No chapter reordering was performed.

## Scope and synthesis

Expanded the existing future-imagination section into a connected account of the future beneficiary, neural self–other representation, age-progressed images, and saving. Retained episodic future thinking and subjective time as distinct mechanisms. Connected the new discussion to learning goals, the saving application, and the practice exercise. Four new references are added; existing relevant references are retained.

The central inference is that making a future beneficiary personally meaningful may increase patience. Similarity, social closeness, temporal continuity, and vividness are related but distinct constructs. An imaging association and a behavioral intervention do not by themselves identify a neural mediator.

## Evidence matrix and verified identifiers

Full bibliographic entries appear in the chapter. Links below point to the primary sources used; Mitchell and Krienen were checked against indexed abstracts and, for Krienen, figure captions, without claiming uninspected methodological detail.

| Source | Design and context | Finding used and boundary |
| --- | --- | --- |
| [Denny et al. (2012)](https://scan.psych.columbia.edu/papers/Denny_et_al_2012.pdf), doi:10.1162/jocn_a_00233 | Meta-analysis of 107 imaging studies | Overlapping self/other processing with a relative ventral–dorsal gradient; not a literal moving activation point. |
| [Mitchell et al. (2006)](https://pubmed.ncbi.nlm.nih.gov/16701214/), doi:10.1016/j.neuron.2006.03.040 | fMRI judgments about similar/dissimilar others | Similarity-related ventral/dorsal contrast; similarity does not establish friendship. |
| [Krienen et al. (2010)](https://pubmed.ncbi.nlm.nih.gov/20943931/), doi:10.1523/JNEUROSCI.2180-10.2010 | Four fMRI experiments; 98 participants overall | Actual friendship and similarity separated; no fixed three-location self/friend/stranger ladder. |
| [Ersner-Hershfield et al. (2009)](https://academic.oup.com/scan/article/4/1/85/1613040), doi:10.1093/scan/nsn042 | 18 young adults; trait judgments and later monetary choice | Right-rACC association; small, correlational, outlier-sensitive evidence, explained in a footnote. |
| [Hershfield et al. (2011)](https://www.microsoft.com/en-us/research/wp-content/uploads/2019/06/Hershfield_Goldstein_et_al_Increasing_Saving_Behavior_Age_Progressed_Renderings_Future_Self.pdf), doi:10.1509/jmkr.48.SPL.S23 | Avatar experiments, Studies 1–2 | Hypothetical allocation distinguished from incentivized choice; identification task acknowledged; Study 2 combined p=.056 retained. |
| [Robalino et al. (2023)](https://journals.sagepub.com/doi/10.1177/23794607231190607), doi:10.1177/23794607231190607 | Randomized app intervention; 48,853 Mexican account holders | Small one-time contribution effect was exploratory; preregistered participation outcomes null. Bundled intervention, unidentified mechanism. |

## Editorial boundaries

- The brain evidence concerns regional involvement in specified tasks, not a general anatomical scale of social distance.
- The early studies do not establish that a brief photograph reliably changes a stable discount parameter or long-run pension wealth.
- Field evidence is compared with laboratory evidence rather than presented as a direct replication of the avatar experiment.
- The policy implication is to connect an affordable action with a concrete future beneficiary; financial constraints and trust remain part of the chapter's explanation.
- Remaining research gap: a design measuring or manipulating continuity separately from attention and imagery, with a preregistered long-run saving outcome, would better identify mechanism and persistence.

## Verification

- Source checks: `python3 scripts/qa_quarto_book.py` passed with 0 errors and 0 warnings; `git diff --check` passed.
- References: `python3 scripts/sync_references.py --check` passed with 984 unique chapter-and-appendix references.
- Rendered the changed chapter and master references with the HTML profile, then rebuilt the EPUB with the EPUB profile.
- HTML content checks confirmed the Chapter 20 title, new anchors, study figures and qualifications, and the neural-evidence footnote. Inspected both new content areas in the in-app browser at its normal 1280×720 viewport; text, headings, and table-of-contents navigation were readable.
- Final EPUB content checks confirmed Chapter 20 in `EPUB/text/ch026.xhtml`, both new explicit anchors, all four new DOI references, key sample sizes and outcomes, and the footnote. `python3 scripts/qa_epub_release.py` passed with 0 errors. This is package/content validation; no native EPUB-reader pagination check was performed for this prose-only revision.
- No commits, pushes, or external publication were performed.
