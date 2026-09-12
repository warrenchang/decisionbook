# GitHub synchronization — 12 September 2026

Updated the main local checkout from `3761a97` to `8db3e75` with a fast-forward merge of `origin/main` (13 incoming commits). The incoming work shortens chapter titles and retunes the Chapter 27 opening around prices as social signals.

## Chapter 27 recovery

Incoming commit `b25fc95`, included in the merged `origin/main`, replaced the entire chapter with the literal text `PLACEHOLDER_WILL_REPLACE`. The local chapter was restored exactly from `24dcdf4`, which already contains the intended new title, subtitle, opening, and core idea. Its 404 lines include the full chapter and reference list. Everything from “Learning goals” onward matches the pre-sync version in `3761a97` byte for byte.

At the end of synchronization, this recovery was a local uncommitted repair. The fetched `origin/main` at `8db3e75` still contained the placeholder. The user subsequently requested committing and pushing the verified repair and rebuilt book.

## Incorporated titles

| Chapter | Current title |
| --- | --- |
| 2 | Building a Better Decision |
| 7 | The Narrator After Choice |
| 9 | What Feels Likely |
| 12 | Framing |
| 13 | Fluency and Familiarity |
| 14 | Base Rates and Updating |
| 19 | Intertemporal Decision Making |
| 24 | Behavioral Game Theory |
| 27 | Prices as Social Signals |
| 33 | Communication |

## Local integration

- Preserved the existing Chapter 7 and Chapter 13 fragment anchors in both HTML and EPUB after their title changes.
- Updated the references to the Chapter 12 and Chapter 13 titles in Chapters 6 and 1.
- Updated EPUB content checks to recognize the shortened titles and retained subtitles, and to require the Chapter 27 title.
- Rebuilt the website, search index, and EPUB. Preserved existing generated-file permissions and removed only incidental generation whitespace.
- Preserved all six pre-existing untracked manuscript-review files, verified by SHA-256 against the pre-sync manifest.

## Verification

- `python3 scripts/sync_references.py --check`: PASS, 838 unique bibliography entries.
- `quarto render --profile html`: completed successfully.
- `quarto render --profile epub`: completed successfully.
- `python3 scripts/qa_quarto_book.py`: PASS, 42 chapters, zero errors and zero warnings.
- `python3 scripts/qa_epub_release.py`: PASS, zero errors.
- HTML link audit using the reusable `configured_sources` and `audit` functions in `audits/book-revision-20260910/audit-final-html-links.py`: PASS across all 61 configured pages and 7,922 local references, with no missing links, invalid fragments, or duplicate IDs. The companion JSON records the audited snapshot.
- All ten changed chapter titles verified in the rendered HTML H1 and EPUB H1 headings; all ten chapter reference sections match the pre-sync version exactly.
- No placeholder remains in canonical chapter/part/appendix sources or in the rebuilt EPUB.
- `git diff --check`: PASS.

This report and its companion JSON record the verification snapshot before the subsequent commit-and-push request. The initial synchronization added no new commit and performed no push; the verified changes comprise the chapter recovery, link adjustments, refreshed checks, reports, and generated book copies.
