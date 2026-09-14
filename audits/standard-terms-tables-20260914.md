# Conventional terminology, conceptual tables, and chapter balance

Revision date: 14 September 2026.

## Editorial decisions implemented

- Chapter 8 uses **System 1/System 2** in prose, its comparison table, figure, and alternative text. One sentence explains the legitimate Type terminology and why neither label means two literal brain structures. The table now has named, shared comparison dimensions.
- Chapter 9 uses **representativeness** as the heuristic name. Ordinary similarity language remains explanatory. The older section anchor and file paths are retained for existing links. Personal example is no longer a peer shortcut: anecdotes are evidence inputs whose usefulness is discussed under availability and in the surrounding case-to-distribution discussion. An independent check also corrected the Linda explanation to rely on set inclusion rather than unweighted case counts.
- Chapter 15 remains the principal home of overconfidence: sampling, randomness, regression, reference classes, and calibration provide its assessment tools. Chapter 8 now points forward from confidence without informative feedback. Table 15.1 contains overestimation, overplacement, and overprecision, adjacent to their definitions. Planning fallacy remains a developed application immediately afterward, including optimistic estimates and excessive certainty.
- Chapter 15 adds a connected section on superstition: two verified sporting rituals, the difference between routine and unsupported causal belief, Skinner’s six-of-eight observation and interpretation, and later timing/feeding explanations. Published sources carry the evidence; lecture slides supply topic provenance only.
- Chapter 21 retains the habit, reinforcement, wanting/liking, and urge material, with examples of what each explanation suggests changing. Its Practice Lab now compares episodes and possible explanations. Chapter 39 develops the full intervention workflow, tool selection, measurement, maintenance, and recovery. Existing dopamine and conditioning media links move into Chapter 21’s corresponding optional research notes. No scientific reference is deleted.
- The master decision map’s first box reads **Context & Information**. The generator and raster fallback match. The other Chapter 1 illustrations are unchanged. Chapters 8 and 9’s edited diagrams were also reflowed after an EPUB phone check exposed undersized labels; both now use 760-pixel canvases and at least 28-pixel source text, fitting the screen in HTML and EPUB.

## All-book table review

The review includes all **146 configured source tables**, including the raw HTML table in Chapter 5 and tables inside optional callouts. The criterion is the table’s declared purpose: classifications compare peer concepts; examples belong in subordinate cells or prose. A workflow, evidence comparison, glossary, or practical diagnostic can legitimately compare different roles when explicitly identified.

**34 tables revised; 112 passed without a conceptual change.** The source inventories record each individual table:

- `audits/table-consistency-20260914-early.md`: 45 tables, 10 revised and 35 passed.
- `audits/table-consistency-20260914-late.md`: 101 tables, 24 revised and 77 passed.

Additional corrections include evaluation conditions versus observed effects, physiological observations versus causal explanations, frameworks’ separate component sets, laboratory/field settings versus assignment methods, broad social learning versus information cascades, noise components versus bias, and incompatible scales in a negotiation-priority table. Useful material was relocated or clarified, rather than discarded.

## Preservation and scientific review

The prior uncommitted Appendix F revision is preserved. The task snapshot includes it and was captured shortly after the table workers began; the workers’ own preservation checks additionally cover their edits. The comparison across all 62 configured sources finds no removed reference block, existing explicit anchor, figure path, chapter title, or table. Six verified published sources were added; the normalized master bibliography grows from 878 to 884 works.

An independent teaching/scientific audit checked the five principal chapters and three edited diagrams. Its two additional findings—Linda’s probability explanation and nonbinding examples labelled precommitment—were corrected. The detailed source record distinguishes verified primary text from the Staddon/Simmelhag abstract-only access limit.

Validation files:

- `audits/standard-terms-tables-20260914-preservation.json`
- `audits/standard-terms-and-superstition-20260914-sources.md`

## Rendered validation

- Full HTML rebuild: all 62 configured pages; 2,364 internal HTML links and 685 search entries resolve. Appendix A–G headings and sidebar labels remain consistent.
- The rebuilt EPUB passes the release checks, including compilation date and source freshness. The final rebuild includes the last figure and callout-anchor changes and passes with zero release errors.
- Browser checks cover all 146 tables at 1440/390 pixels in HTML and 768/390 pixels in EPUB, with no page or table-container overflow. Wide HTML tables retain their existing horizontal reading panes; passing this check does not mean every column is simultaneously visible on a phone.
- An independent comparison of all 24 revised late-book tables found every source cell and caption in the rendered output (169 body rows), with 17 checks of relocated explanations. The preserved Chapter 25 callout alias was moved to its container so it resolves in HTML.
- Three changed SVGs were inspected at source size and 330-pixel reading width. Text fits within the intended boxes, connectors attach, and the smallest displayed type is at least 12.15 pixels. Source generation is reproducible; raster fallbacks were regenerated from the final SVGs. New diagram layouts received a separate semantic audit.
- Representative table/figure screenshots were inspected in both destinations. Final captures were refreshed and visually inspected for the two reflowed diagrams in HTML at 1440/390 pixels and EPUB at 768/390 pixels. Both fit the phone reading column without horizontal scrolling. The corrected Chapter 25 alias also resolves in both outputs.

Additional records: `standard-terms-tables-20260914-html-render.json`, `standard-terms-tables-20260914-epub-render.json`, `standard-terms-tables-20260914-navigation.json`, and `standard-terms-tables-20260914-figure-bounds.json` in this directory. No commit or push is part of this request.

Final figure ledger: `master-loop.svg`, `fast-slow.svg`, and `prototype-probability.svg` all PASS source bounds and visual checks at source size and 330-pixel reading width, plus desktop/tablet and 390-pixel HTML/EPUB destinations. The two latter diagrams were revised to resolve the undersized EPUB type found in the first render. Final checks are recorded in `standard-terms-tables-20260914-html-final-figures.json` and `standard-terms-tables-20260914-epub-final-figures.json`.
