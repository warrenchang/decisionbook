# Decision, Persuasion, and Negotiation

This is the Quarto source for Huanren Warren Zhang's textbook, *Decision, Persuasion, and Negotiation: How Minds Choose, Influence, Connect, and Bargain*.

The 48 chapters follow a cumulative ten-part journey: the decision-making process; attention, prediction, and expectation; heuristics, biases, and probability judgment; risk, experience, and time; money, finance, and well-being; strategic and social decisions; influence and persuasion; negotiation; communication and connection; and habits and decision design.

## Build

From the project root, build the HTML book with:

```bash
quarto render --profile html
```

Build the EPUB with:

```bash
quarto render --profile epub
```

Both artifacts are written to `docs/`; the EPUB is `docs/Decision-Persuasion-and-Negotiation.epub`. The EPUB build uses `_quarto-epub.yml` and `filters/epub-parts.lua` so Part titles and numbered chapters remain in the table of contents.

## Editorial records

- `audits/lecture-notes-audit-reconciliation.md` and `audits/lecture-notes-coverage.csv` record exact-path coverage of the complete Lecture Notes folder, along with duplicate, rights, and source-authority decisions.
- `audits/lecture-notes-final-integration.md` and `audits/lecture-notes-final-integration.csv` map every audited source path to its final book destination or an explicit non-reuse decision.
- `SOURCE_INTEGRATION_REPORT.md` retains the earlier coverage record for the editable lecture decks and alternative textbook manuscripts.
- `QA_REPORT.md` records the latest release checks.
- `QUARTO_EDITING_GUIDE.md` explains the source layout and editing workflow.
