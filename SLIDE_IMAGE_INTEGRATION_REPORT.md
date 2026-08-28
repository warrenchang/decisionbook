# Slide-Image Integration and Rights Report

This report documents the image-level revision of the textbook against the eight editable 2026 lecture decks. It complements `SOURCE_INTEGRATION_REPORT.md`, which records content-level coverage.

## Complete source inventory

The PowerPoint packages contain **396 visual occurrences** across 654 slides, including **46 occurrences on hidden slides**. These comprise 395 embedded-image occurrences and one native chart. Hashing identifies **357 unique embedded files** and 35 image groups reused more than once.

| Deck | Visual occurrences | On hidden slides |
| --- | ---: | ---: |
| DPN01. Decision Process | 56 | 11 |
| DPN02. Attention, Prediction, Expectation | 102 | 18 |
| DPN03. Heuristics & Biases | 56 | 0 |
| DPN04. Influence & Persuasion | 72 | 11 |
| DPN05. Distributive Negotiation | 34 | 0 |
| DPN06. Integrative Negotiation | 46 | 4 |
| DPN07. Communication & Connection | 22 | 2 |
| DPN08. Habits and Behavior Design | 8 | 0 |
| **Total** | **396** | **46** |

The machine-generated occurrence ledger is in `audits/slide-images-raw/slide-image-occurrences.csv`. It records the deck and slide, hidden status, object ID and name, alternative-text metadata, media dimensions, crop, SHA-256 hash, and duplicate group for every occurrence. The reviewed ledger adds pedagogical role, provenance, rights status, treatment, destination, and completion status.

## Rights rule

Changing a protected image's crop, color, style, or surface details does not by itself make reuse lawful. The U.S. Copyright Office states that the copyright owner controls preparation of new versions and that changing someone else's work does not transfer that right ([Copyright Office fair-use FAQ](https://www.copyright.gov/help/faq/faq-fairuse.html); [Circular 14](https://copyright.gov/circs/circ14.pdf)). EUIPO likewise treats permitted use, licensing, and national educational exceptions as questions that must be checked rather than assumed ([Copyright for Educators](https://www.euipo.europa.eu/en/copyright-knowledge-centre/knowledge-and-cultural-institutions/educators)).

The book therefore uses five defensible routes:

1. Reuse an exact asset only when public-domain status or a suitable license is verified and attributed.
2. Rebuild a factual chart from verified primary-study values in an original visual design, with a citation to the study rather than to the slide graphic.
3. Re-express an idea, mechanism, or study design as a genuinely original diagram. Copyright protects particular expression rather than underlying facts, ideas, systems, or methods ([Copyright Office Circular 33](https://www.copyright.gov/circs/circ33.pdf)).
4. Link to protected audiovisual, news, advertising, product, book, journal, or website material when seeing the original is pedagogically important.
5. Omit duplicated, decorative, administrative, provenance-unknown, or pedagogically empty imagery while preserving and mapping any substantive teaching point.

No image is treated as cleared merely because it appeared in a lecture deck. No film frame, television frame, book cover, advertisement, product packaging, journal figure, commercial screenshot, child image, stock photograph, or unexplained AI-like asset is copied or superficially restyled without documented rights.

## Reviewed disposition and book additions

The reviewed ledger accounts for **396 of 396 occurrences exactly once**. Of these, **298 are substantive** and have a completed pedagogical treatment. The remaining 98 are explicitly accounted for as 47 decorative items, 38 exact duplicates, and 13 administrative images such as QR codes or live-poll interfaces.

| Treatment | Occurrences | What the book does |
| --- | ---: | --- |
| Represented in prose, a table, or an activity | 213 | Preserves the example, mechanism, result, qualification, or teaching prompt without copying protected expression. |
| Represented by an existing original book visual | 39 | Routes the slide idea to an already available accessible SVG. |
| Linked to the original source | 26 | Uses an authorised/source link and a predict–observe–debrief prompt; no frame or screenshot is copied. |
| Re-expressed through a new original visual | 20 | Rebuilds the underlying study facts or teaching idea across fourteen new visuals. |
| Decorative omitted | 47 | Omits title art, divider art, and atmosphere-only imagery. |
| Exact duplicate accounted | 38 | Records the repeated occurrence without duplicating the book treatment. |
| Administrative omitted | 13 | Replaces ephemeral QR, Padlet, and poll interfaces with durable instructions where the activity is substantive. |
| **Total** | **396** | **Every occurrence has a destination or an explicit non-use rationale.** |

The rights review identified 218 protected occurrences, 123 with unclear provenance, 43 containing only facts or data suitable for independent re-expression, 11 for which rights were not applicable, and one author-owned occurrence. No embedded slide asset had verified public-domain or open-license provenance. Consequently, **no raw slide raster was copied into the book**.

### Fourteen new original visuals

The image pass adds twelve accessible SVG figures with 2× PNG companions and two original raster illustrations. Several source occurrences can map to one integrated figure, which is why twenty occurrence-level redraw treatments produce fourteen unique visuals.

| New figure | Destination | Editorial function |
| --- | --- | --- |
| `norm-message-diagnostic` | *Conformity: When Popularity Becomes Evidence* | Separates descriptive from injunctive norms and makes the backfire test visible. |
| `first-offer-information-matrix` | *Preparing to Claim Value* | Turns the first-offer advice into a bounded information-and-disclosure heuristic. |
| `communication-calibration-evidence` | *Communication: Language Is Not a File Transfer* | Redraws verified task-specific values and pairs them with an original perspective-getting schematic. |
| `conversation-needs-map` | *Connection and Repair: Warm Honesty Makes Truth Usable* | Distinguishes practical, emotional, and social-or-identity needs without diagnosing from one sentence. |
| `intent-behavior-impact-cycle` | *Connection and Repair: Warm Honesty Makes Truth Usable* | Shows why impact is real evidence but not a motive detector. |
| `habit-formation-curve` | *Habits: The Plan Is Often Not the Decision-Maker* | Replaces a deadline myth with an explicitly illustrative family of gradual trajectories. |
| `reward-prediction-error-shift` | *Wanting and Self-Control: Urge Is Not Action* | Re-expresses reward-prediction-error logic while stating that the panels are not neural traces. |
| `urge-wave-observation` | *Wanting and Self-Control: Urge Is Not Action* | Gives the urge-surfing activity a variable, non-clinical schematic rather than a promised time course. |
| `affect-panda-sea-star` | *Feeling and Availability: When Ease of Recall Becomes Evidence* | Restores the lecture’s conservation-allocation prompt with a wholly new illustration rather than the source photographs. |
| `wording-memory-study-redraw` | *Frames Change the Decision* | Redraws the published speed-estimate and false-glass values in an original two-panel chart. |
| `mimicry-study-redraw` | *Social Learning, Mimicry, and Attribution* | Displays the reported mannerism means together with task-specific and ethical boundaries. |
| `cultural-market-study-redraw` | *Conformity, Norms, and Social Proof* | Redraws the Music Lab unpredictability pattern and explains its parallel-worlds logic. |
| `culture-triad-monkey-panda-banana` | *Culture and Identity: The Same Action Is Not the Same Act* | Restores the analytic-versus-relational categorization prompt with a wholly new three-object illustration. |
| `culture-honor-study-redraw` | *Culture and Identity: The Same Action Is Not the Same Act* | Redraws the published cortisol-change values while keeping the restricted sample and anti-stereotyping boundary visible. |

Each figure has a unique Quarto identifier, a meaningful caption and `fig-alt`, and SVG `<title>` and `<desc>` metadata. The figures are placed at 86–98% of the chapter text width according to their density, with no fixed-width layout dependency.

### Reproducible audit files

- Raw occurrence inventory: `audits/slide-images-raw/slide-image-occurrences.csv`
- Reviewed disposition ledger: `audits/slide-images-reviewed.csv`
- Machine summary: `audits/slide-images-reviewed-summary.json`
- Inventory generator: `scripts/audit_pptx_images.py`
- Ledger merger: `scripts/merge_slide_image_ledgers.py`
- Exact-coverage validator: `scripts/qa_slide_image_coverage.py`

The final validator reports: **PASS — all 396 slide-image occurrences have valid reviewed dispositions**.

### Layout and release validation

The fourteen new visuals were inspected at original size and in their chapter renders, alongside a contact review of all 60 canonical chapter figures. One overly long subtitle in the communication-calibration figure and one crowded legend in the culture evidence redraw were reflowed during those passes. Final checks found no clipped text, overlapping labels, detached connectors, unintended arrow directions, or missing PNG companions for the SVG figures.

The complete 52-source Quarto project was rebuilt to `docs/`. Every new figure renders with Quarto's responsive `img-fluid` class and a chapter-specific width between 86% and 98%. The canonical book audit finishes with **0 errors and 0 warnings**, including 0 missing rendered chapters, 0 rendered images without alternative text, and 0 unresolved author–year citations.
