# Independent review of reference and discussion revisions

Date: 14 September 2026. Reviewer: figure_text_late. Read-only review of production sources.

## Scope and method

Compared current source with `/tmp/figure-reference-review-20260914/before` for the preface (`index.qmd`), `how-to-use-this-book.qmd`, Parts I–VII, Appendix B, Appendix C, Appendix F (physical `appendix-e-how-behavioral-evidence-is-built.qmd`), and Appendix G (physical `appendix-f-when-evidence-breaks.qmd`). Read every changed paragraph and its neighboring prose, captions, and relevant table content. The review checks whether each introduced figure/table reference has a clear teaching purpose, preserves the existing evidence boundary, and flows grammatically into the surrounding explanation. It is independent of the whole-book count and link checks run by the root agent.

Also inspected the current Chapter 9 Figure 9.1 PNG individually, together with its paragraph, caption, alt text, and following exercise. This is a semantic and visual source review, not a claim that final HTML/EPUB rendering has been checked here.

## One concrete correction

**Part II — missing antecedent, reported to root.** In `parts/part-2.qmd`, replacing “The chapters in this part examine both possibilities” with a sentence about “The route in @fig-part-2-route” leaves “They begin with intuitive judgment” without a grammatical antecedent. Change this to “The chapters begin with intuitive judgment.” Status: **resolved**. Independently re-read the current source and confirmed “The chapters begin with intuitive judgment” is present.

## Passed checks

- **Preface and reading guide:** The decision-map reference points to the explanation of how a choice takes shape. The reading-route and vocabulary references describe how to use the corresponding tables, rather than adding empty “see” instructions. The new caption and ID for the previously uncaptioned reading-routes table are appropriate.
- **Part openers:** Each route reference connects the map to the substantive questions developed in that part. Apart from the Part II antecedent, the paragraphs remain coherent. The repeated “route” framing across separated part openers serves consistent navigation and does not introduce local redundancy.
- **Appendix B:** The comparison references tell readers which distinction to examine; descriptive, evolutionary, formal, and normative claims retain their existing boundaries. No new causal claim or unsupported equivalence is introduced.
- **Appendix C:** The table references make the tool levels, canonical tool selection, and minimum journal usable. Giving the minimum-journal table a caption and stable ID is justified. The prose explains the record to keep without duplicating every cell.
- **Appendix F:** The revised discussion connects design choices to the claims they can support. It preserves the distinction between assignment effects and effects of receiving treatment, between prediction and intervention, and between simulated patterns and evidence about human mechanisms. The worked reminder study remains explicitly simulated.
- **Appendix G:** The discussion distinguishes reproducibility, replication, robustness, and generalizability, and explains what to examine in the safeguard and evidence-update tables. Failed replication and retraction remain distinct reasons to update confidence. No added claim goes beyond the existing table evidence.

## Chapter 9 Figure 9.1

**PASS.** The individually viewed image, `figures/affect-panda-sea-star.png`, depicts a giant panda cub in a tree and purple/orange sea stars on wet intertidal rocks among mussels. The scenes do not mix species anatomy or habitats. Stout arms, color range, and pale patterned spines are consistent with ochre sea stars; this narrow visual check used the primary species descriptions from the [Georgia Aquarium](https://www.georgiaaquarium.org/animal/ochre-sea-star/) and [Aquarium of the Pacific](https://www.aquariumofpacific.org/onlinelearningcenter/species/ochre-sea-star).

The body asks which species first draws the reader’s concern without assuming a universal answer. The following conservation-allocation exercise explicitly begins “For a hypothetical exercise, suppose independent evidence showed…”. The image and alt text do not claim that the sea stars actually have greater conservation value, and AI-generated editorial provenance is stated in the caption. This preserves the distinction between emotional appeal and evidence about intervention benefits.

## Outcome

No outstanding concrete defect found in the reviewed changes. The one Part II antecedent issue is corrected in source; final destination rendering remains the root agent’s responsibility.
