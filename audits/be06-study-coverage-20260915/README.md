# BE06 study coverage in Decision in the Making

Date: 15 September 2026

## Scope and outcome

Reviewed the current `BE06. Habits and Behavior Design.pptx`: all 56 slides, including 24 hidden appendix slides, and all speaker notes. The book now contains substantive discussion for every study in that material. The 39 sources listed by the deck plus the implicit Stroop source are mapped individually in `source-coverage.csv`; `slide-coverage.csv` accounts for every slide. Reviews, design frameworks, practice guidance, and the book's own applications are identified separately from empirical studies.

Added or expanded the discussions in Chapters 21 and 39. Existing discussions in Chapters 8, 20, and 40 are linked from the revised narrative. Chapters 20 and 40 received reference-identifier harmonization only. The preceding animal variable-reward Research Lens and unrelated source edits were preserved. No slide was edited and no commit or push was performed.

Four new Research Lenses cover delay/progress/effort, urge surfing, WOOP evidence, and fresh starts versus changed settings. The main narrative now explains the popcorn manipulations, taste reactivity, cigarette/water availability procedure, vaccination planning prompts, temptation bundling, and uncertainty's effects on repeated participation more precisely.

## Verification

- `inputs.json`: exact source deck and SHA-256.
- `source-coverage.csv`: source type, substantive slide locations, book location, change disposition, and inferential boundary.
- `slide-coverage.csv`: all 56 slides, including hidden status.
- `browser-qa.json`: four new lenses checked at 1440px and 390px, plus final HTML coverage-anchor checks.
- `validation.json`: source coverage, fragment links, EPUB content and numerical details, references, deck preservation, unrelated-source preservation, and file-mode preservation.
- Full HTML render, refresh of harmonized references, and full EPUB render completed.
- Book QA: zero errors and zero warnings. EPUB QA: zero errors. Master reference synchronization: 921 entries.

## Primary-source checks for new or expanded empirical claims

Sources were checked through original papers, publisher records, PubMed, or author-hosted copies. Existing unchanged study discussions were audited for substantive coverage, not presented as a new replication of their evidence.

| Source | Primary record checked |
| --- | --- |
| Neal et al. (2011) | https://doi.org/10.1177/0146167211419863; author-hosted full paper, Methods and Results |
| Berridge & Robinson (1998) | https://doi.org/10.1016/S0165-0173(98)00019-8; author-hosted full paper |
| Bailey et al. (2010) | https://pmc.ncbi.nlm.nih.gov/articles/PMC2807894/; indexed full text, Methods and Results |
| Fiorillo et al. (2003) | https://www.hms.harvard.edu/bss/neuro/bornlab/nb204/exam/FiorilloSchultz_Science.pdf; original paper, Figure 1 |
| Kobayashi & Schultz (2008) | https://pubmed.ncbi.nlm.nih.gov/18667616/; abstract and figure descriptions |
| Howe et al. (2013) | https://pubmed.ncbi.nlm.nih.gov/23913271/; abstract and figure descriptions |
| Hamid et al. (2016) | https://www.nature.com/articles/nn.4173; publisher abstract |
| Schultz (2016) | https://pubmed.ncbi.nlm.nih.gov/27069377/; review and bibliographic record |
| Bowen & Marlatt (2009) | https://pubmed.ncbi.nlm.nih.gov/20025372/; abstract |
| Milkman et al. (2011) | https://doi.org/10.1073/pnas.1103170108; author-hosted full paper, Table 2 |
| Milkman et al. (2014) | https://pubsonline.informs.org/doi/10.1287/mnsc.2013.1784; publisher abstract |
| Shen et al. (2019) | https://doi.org/10.1093/jcr/ucy062; authors' institutional publication record and abstract |
| Wang et al. (2021) | https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2021.565202/full; Results and publication-bias analysis |
| Dai et al. (2014) | https://pubsonline.informs.org/doi/10.1287/mnsc.2014.1901; original article abstract |
| Verplanken & Roy (2016) | https://doi.org/10.1016/j.jenvp.2015.11.008; authors' institutional publication record and abstract |

## Slide wording discrepancies retained for follow-up

The deck was read-only for this request. The book follows the study evidence rather than copying these two overstatements:

1. PPTX slide 10 (displayed page 9) says a missed occasion disrupts automaticity. Its own notes and the book instead explain that one missed opportunity did not materially disrupt habit formation in Lally et al. (2010).
2. PPTX slide 21 (displayed page 20) promises that an observed urge will pass. The book explains that urges may persist or return and that behavior can change without a significant reduction in reported urges.

The slide numbers in the coverage tables use the full PPTX sequence, including the cover; displayed footers are generally one lower.
