# Chapter 27: review of the former Figure 27.6

Reviewed figure: `fig-behavioral-finance-audit` (`figures/behavioral-finance-audit.svg`, with PNG fallback).

Decision: remove the checklist diagram from the chapter. It repeats the joint-hypothesis discussion, return-anomalies table, and evidence-boundary box. Its arrows do not explain how to distinguish the competing accounts, and its large collection of labels adds little to the explanation.

The existing hypothetical return example now compares the same 12% average annual return with expected returns of 8% and 12%. The unexplained differences are four and zero percentage points, respectively. These are illustrative numbers, not empirical results. The discussion retains the distinction between a return benchmark, a mispricing interpretation, and a usable trading opportunity.

The obsolete numbered reference was removed and the event-study paragraph now follows directly from the joint-hypothesis discussion. The old identifier remains as an unnumbered anchor so existing links still reach that discussion. The original SVG and PNG remain available as unused source assets.

Verification:

- Chapter HTML and full EPUB rebuilt successfully.
- The diagram is absent in both editions; the legacy anchor and revised example are present.
- Chapter figure captions run consecutively from 27.1 to 27.8 in both editions.
- Source, HTML, and EPUB figure/table reference coverage passed with zero issues.
- Book QA passed with zero errors and zero warnings; EPUB release QA passed with zero errors.
- Reference synchronization passed with 1,069 unique references; the edited source passed `git diff --check`.

This review concerns one figure and its surrounding passage; it is not a new visual audit of every remaining illustration.
