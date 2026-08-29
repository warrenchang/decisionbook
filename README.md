# Decision, Persuasion, and Negotiation

This is the Quarto source for Huanren Warren Zhang's textbook, *Decision, Persuasion, and Negotiation: How Choices Take Shape—and How Minds Shape One Another*.

The 41 chapters follow a cumulative seven-part journey plus an applied market interlude: how a choice takes shape; judgment under uncertainty; risk, time, self-regulation, and a good life; markets, mispricing, and bubbles; interdependent choices; influence, communication, and connection; negotiating joint decisions; and designing better loops. Four appendices provide portable tools, an evidence-aware example index, a Research Companion on running experimental studies, and a guide to replication and research integrity. A curated concept index identifies each key concept's main discussion and selected later applications.

## Build

From the project root, build the HTML book with:

```bash
quarto render --profile html
```

Build the EPUB with:

```bash
quarto render --profile epub
```

Both release artifacts end in `docs/`; the EPUB is `docs/Decision-Persuasion-and-Negotiation.epub`. The EPUB profile builds in the ignored `_epub/` staging directory and a post-render hook normalizes its navigation and copies the finished book beside the HTML release. This prevents either profile from cleaning the other format. The EPUB build uses `_quarto-epub.yml` and `filters/epub-parts.lua` so numbered chapters are nested beneath Part and Applied Interlude titles while section headings remain outside the table of contents.

## Editorial records

- `audits/lecture-notes-audit-reconciliation.md` and `audits/lecture-notes-coverage.csv` record exact-path coverage of the complete Lecture Notes folder, along with duplicate, rights, and source-authority decisions.
- `audits/lecture-notes-final-integration.md` and `audits/lecture-notes-final-integration.csv` map every audited source path to its final book destination or an explicit non-reuse decision.
- `SOURCE_INTEGRATION_REPORT.md` retains the earlier coverage record for the editable lecture decks and alternative textbook manuscripts.
- `QA_REPORT.md` records the latest release checks.
- `EPUB_QA_REPORT.md` records package, navigation, date, numbering, and required-content checks for the canonical EPUB.
- `QUARTO_EDITING_GUIDE.md` explains the source layout and editing workflow.
