# Reference and anchor preservation audit

Baseline: `227f62ed57dedc46b6c1d3bef2ed67b4e3612d3b`.
Scope: the same 61 sources configured in `_quarto-html.yml` at baseline and at the final source snapshot. Exact timestamp, source hashes, per-entry locations, and all six review-file hashes are in [the JSON record](reference-preservation-check.json).

## Result

**No bibliographic work was deleted from the configured book.** The deduplicated bibliography increased from **838 to 849 works**, with **11 added and 0 removed**. The habit chapter and all other nonempty chapter/appendix reference lists pass the final author-based ordering check. No baseline explicit anchor was lost from its original file, and all six preserved review files match their baseline SHA-256 hashes.

| Measure | Baseline | Revised | Interpretation |
| --- | ---: | ---: | --- |
| Configured sources | 61 | 61 | Same paths; no configured source dropped or added |
| Reference-block occurrences, including the master bibliography | 1,824 | 1,847 | Includes intentional chapter/appendix/master repetitions |
| Reference-block occurrences outside the master | 986 | 998 | Net increase of 12 local entries |
| Deduplicated normalized entries | 838 | 849 | Net increase of 11 |
| Distinct bibliographic works under the identity rule below | 838 | 849 | 11 added, none deleted |
| Baseline explicit anchors missing from the original file | — | 0 | Legacy table and section anchors preserved |
| Preserved review files matching baseline hashes | — | 6 of 6 | Original supplied review records unchanged |

At the literal normalized-entry level there are **12 added entries and 1 removed entry**. The apparent removal is the old, DOI-free version of Tversky and Kahneman (1981). Chapters 12 and 17 now use the same DOI-enriched entry added to Chapter 20. The title, authors, year, journal, volume, and pages identify the same work; this is metadata enrichment and consolidation of formatting variants, not deletion of a study.

## The eleven newly listed works

| Work | Local chapter |
| --- | --- |
| Asch (1955), *Opinions and social pressure* | 26 |
| Bechara, Damasio, Damasio, and Anderson (1994), *Insensitivity to future consequences following damage to human prefrontal cortex* | 6 |
| Frederick, Lee, and Baskin (2014), *The limits of attraction* | 11 |
| Loschelder, Friese, Schaerer, and Galinsky (2016), *The too-much-precision effect* | 36 |
| Maia and McClelland (2004), *A reexamination of the evidence for the somatic marker hypothesis* | 6 |
| Meyer et al. (2015), *Disfluent fonts don't help people solve math problems* | 13 |
| Parry (2024), *Does the mere presence of a smartphone impact cognitive performance?* | 39 |
| Rackham (1980), *The behavior of successful negotiators*, consulted author-report reprint | 35 |
| Stothart, Mitchum, and Yehnert (2015), *The attentional cost of receiving a cell phone notification* | 3 |
| Urbach et al. (2014), *Introduction of surgical safety checklists in Ontario, Canada* | 41 |
| Yang and Lynn (2014), *More evidence challenging the robustness and usefulness of the attraction effect* | 11 |

The JSON contains the full entries and source locations. Source verification and substantive interpretation are documented in the separate chapter revision reports; this audit independently tracks bibliographic presence and change.

## Local removals and propagated references

Three entries disappeared from Chapter 6's local list when the extended needs/Maslow discussion was consolidated into Appendix B. Each already appeared in Appendix B before revision and remains there and in the master bibliography:

- Bridgman, Cummings, and Ballard (2019), *Who built Maslow's pyramid?*
- Kesebir, Graham, and Oishi (2010), *A theory of human needs should be human-centered, not animal-centered*.
- Peterson and Park (2010), *What happened to self-actualization?*

These are **consolidated local coverage**, rather than works deleted from the book or newly moved into a previously empty appendix.

Four works already present elsewhere gained additional chapter-local entries:

- Tversky and Kahneman (1981) in Chapter 20.
- Watts, Duncan, and Quan (2018) in Chapter 19.
- Eyal, Steffel, and Epley (2018) in Chapter 37.
- Dallacker et al. (2024) in Chapter 40.

Thus the 12-entry net increase outside the master is 11 new works plus 4 added locations for existing works, minus 3 consolidated Chapter 6 locations.

## Ordering correction and verification

The first independent audit found that sorting full citation strings treated `&` as earlier than alphabetic coauthors. For example, it placed Wood and Rünger before Wood, Quinn, and Kashy, even though Quinn should precede Rünger. Similar coauthor ordering issues appeared in Chapters 17, 18, 27, 30, 33, 34, Appendix F, and the master bibliography.

After the root explicitly expanded ownership, only the sorting helper in `scripts/sync_references.py`, the ordering of reference blocks, and the regenerated master bibliography were changed. The helper now compares surname/initial pairs for each author, followed by year, suffix, and title. Shorter matching author lists precede longer ones; corporate authors have a separate fallback. Punctuation, diacritics, apostrophes, and ampersands do not override name ordering. Known authors preceding `et al.` remain usable for ordering.

Reference blocks were reordered in Chapters 4, 17, 18, 21, 27, 30, 33, and 34, plus Appendix F. The Chapter 4 change follows the different printed initials, K. versus K. J.; no author metadata was silently rewritten. The master was regenerated with the same 849 entries.

During each reorder, assertions checked both the exact multiset of reference bodies and the complete text outside reference blocks. **No reference body or non-reference chapter/appendix text was changed by this ordering operation.** The master introductory text is generated by the existing synchronization procedure.

Validation completed:

- Nine targeted ordering comparisons exercised coauthor order, sole authors, author-list prefixes, apostrophes, year order, undated works, and truncated `et al.` credits.
- Five persistent doctest examples are in the sorting helper, including the Wood/Quinn/Rünger regression and shorter-list cases. `python -m doctest -v scripts/sync_references.py` passed all five.
- `python scripts/sync_references.py --check` passed with 849 entries.
- The final independent audit uses its own regular-expression extraction of surname/initial groups; it does **not** import the production sorting helper. It found no adjacent ordering inversion in any nonempty list.
- All 42 chapter lists, four appendix lists, and the master list passed. Appendices C and D have no standalone `.reference` blocks, so alphabetization is not applicable there.
- `git diff --check` passed for the helper, master, chapters, and appendices.

## Method and limits

1. Read the 61 configured source paths from both current `_quarto-html.yml` and `git show <baseline>:_quarto-html.yml`; compare their sets and reject duplicates. Read each baseline source through `git show <baseline>:<path>` and each current source from disk.
2. Extract complete `::: {.reference}` blocks. For entry matching, normalize whitespace, case, terminal full stops, typographic quotes/dashes, italic/code markup, and punctuation spacing. Keep substantive reference text and URLs, so DOI additions remain visible as metadata changes.
3. Match work identity using the author list, year, and title prefix before the first sentence break, ignoring markup, punctuation/diacritics, and URLs. Manually inspect the unmatched-entry and changed-variant records. Here the only changed retained work was Tversky–Kahneman (1981), and none of the 838 baseline work identities was missing afterward. This identity rule is sufficient for these observed changes; it is not a general bibliographic authority resolver.
4. Compare source locations excluding the master, distinguishing loss of a local mention from disappearance of the work. This separates the three Chapter 6 consolidations from deletions.
5. Check alphabetization using independently extracted author-name groups, dates, and titles. This is an author-based ordering check, not complete APA copyediting. Existing variations in initials, capitalization, edition description, and truncated author lists were preserved; unknown omitted coauthors cannot be alphabetized as though their identities were known.
6. Extract explicit Quarto identifiers inside attribute braces and literal HTML `id` attributes. Compare each baseline anchor with the same current file, not merely with the book-wide union. Automatic heading slugs, footnote-generated IDs, rendered DOM duplication, and semantic suitability of anchor destinations require the root's build/link checks. The restored `tbl-34-1` and the Chapter 6 legacy table anchor are included in this preservation check.
7. Compute SHA-256 directly from the six original review files and compare with `baseline.json`. All matched. Record current source SHA-256 hashes, then reread the sources at the end to detect concurrent changes; none changed during the final audit run.

Bibliographic preservation does not establish that every sentence or every empirical claim stayed identical. The revision intentionally changes explanations, corrections, and placement. This audit establishes that no listed work vanished, identifies the consolidated locations, and checks navigation identifiers and ordering; scientific adequacy of the revised discussions is addressed in the chapter audits. Final HTML/EPUB rendering and external publication are outside this audit.

## Final link-integration refresh

The embedded independent audit was rerun after the root added stable `chapter-NN-start` anchors to the existing epigraph blocks and redirected chapter links. The refreshed snapshot is **2026-09-12T19:21:53.805674+00:00**. All 42 chapter-start anchors were independently confirmed on their epigraph blocks. Chapter 39's Appendix F pointer now targets `#direct-or-coordinated-tests-that-did-not-reproduce-the-focal-result`, and that exact source link was verified.

The changes alter 47 of the 61 whole-source hashes: all 42 chapters, Appendices A/B/D/F, and the concept index. Compared with the previous audit, exactly 42 explicit anchors were added, all in the expected `chapter-NN-start` family; none of the previously recorded added anchors was lost. The final census contains **818 baseline file/identifier pairs and 873 current pairs**, with no baseline pair missing from its original file. The machine record lists the new identifiers and updated hashes.

The bibliography results are unchanged: 838 → 849 works, 11 additions, no deletions, the same Tversky–Kahneman metadata enrichment, the same local consolidations and propagated references, and no ordering inversions. All six original review-file hashes still match. No source changed while the final refresh was running.

This refresh compares the prior audit's reference identities, locations, variants, counts, ordering results, and whole-source hashes. The previous complete source texts were not retained, so the hash changes alone cannot establish a byte-for-byte exclusion of every possible non-reference prose edit. Current hashes of each file's ordered raw reference bodies are now also recorded for any subsequent check. No manuscript or figure was changed by this refresh.
