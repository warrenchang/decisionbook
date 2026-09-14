# Appendix F revision from randomized-evaluation teaching materials

Date: 14 September 2026

Baseline: `41de1608519ce04a28055cdc344afeb9f88a5a18`

## Scope

Revised `appendices/appendix-e-how-behavioral-evidence-is-built.qmd`, displayed as Appendix F. Its filename, existing anchors, figure paths, and publication position remain stable. The supplied PowerPoint files were read as teaching inputs and left unchanged. No unpublished-slide citations were added to the book.

The review covered all 79 slides and notes in **AEE 3&4 Randomized Evaluation.pptx** and all 47 in **AEE 6 Threats in Randomized Evaluation.pptx**, using actual presentation order rather than assuming slide-part numbers or printed footers. Both files are in the author's `Teaching/Advanced Economic Evaluation/Notes` directory.

| Input | SHA-256 |
| --- | --- |
| AEE 3&4 Randomized Evaluation.pptx | `7678b1da52cc5cd272f525bdf47b1d0acbdcaeda4ef1af7ac2dfb185f454fa28` |
| AEE 6 Threats in Randomized Evaluation.pptx | `6d10a89330e559de77004499ca895ccb4135f7fa418f8f82c8364f1ce39ebe76` |

## Changes

- **Figure F.2:** replaced the two independent columns with the source diagram's sequential branching structure: target population, random sampling, evaluation sample versus people outside the evaluation, then random assignment of the evaluation sample to treatment and control. Physical slide 4 contains this diagram; physical slide 5 repeats it with validity annotations. The new figure retains the external/internal validity connections and makes clear that people outside the evaluation are not its randomized controls. It describes a probability-sampled trial as one possible design, not a requirement for every RCT.
- **Counterfactuals:** distinguished a concurrent randomized comparison from a comparison with last year's patients, and a group-average counterfactual from an unobservable individual treatment effect.
- **Design and delivery:** added operational lotteries, randomized phase-in, encouragement, and rotation conditions. Developed the difference between randomization and measurement units, patient versus household/clinic assignment, clustering, and precision. Added a concrete blocking example using clinic and prior attendance.
- **Implementation threats:** developed an attrition example in which treatment changes who attends and is measured. Distinguished missing records from confirmed nonattendance and explained why follow-up, weighting, imputation, bounds, and sensitivity analyses require attention to selection and assumptions.
- **Assignment and receipt:** added a clearly hypothetical calculation with contemporaneous assigned-group employment rates of 43% and 40%, participation rates of 45% and 20%, a 3-percentage-point ITT, and a 12-percentage-point complier effect conditional on the existing IV assumptions. The exclusion-restriction counterexample explains when that interpretation fails.
- **Spillovers:** explained comparisons within treated markets, between exposed and pure-control markets, and across market averages. Added Crépon et al.'s published French job-placement study to distinguish individual gains from net policy benefits.
- **Integration:** removed repeated validity definitions downstream, aligned the figure discussion and practice questions, and linked the new randomization-unit section from the concept index.

The appendix retains its clinic narrative and five-phase workflow. Existing material on factorial designs, research reactivity, measurement, replication, ethics, and reproducibility already covered relevant lecture topics; it was retained rather than duplicated.

## Scientific verification and preservation

Published primary sources support the additions. Two works were added: Duflo, Glennerster, and Kremer (2007), *Using randomization in development economics research: A toolkit*, DOI `10.1016/S1573-4471(07)04061-2`; and Crépon et al. (2013), *Do labor market policies have displacement effects? Evidence from a clustered randomized experiment*, DOI `10.1093/qje/qjt001`. The existing Bruhn and McKenzie (2009) entry is now explicitly cited for blocking. The appendix has 19 alphabetized reference entries and the book-wide bibliography has 878 unique entries.

Independent source and pedagogical reviews corrected three drafting ambiguities: assignment was separated from actual receipt, the hypothetical LATE example explicitly compares groups at the same follow-up, and the cluster-precision claim specifies positive correlation. Crépon's population is identified as eligible young, educated job seekers and the outcome as stable employment. Its transitory gains and limited net benefit are not interpreted as proof of exactly zero effect.

Slide simplifications were not transferred: exact realized covariate balance, unconditional rejection of rerandomization, LATE equated with all treated participants, matching as proof of ignorability, or a universal direction of spillover bias. The existing qualified Hawthorne discussion and ethical limits were preserved. The optional baby-bonus example was omitted rather than importing its inconsistent date.

All 17 original reference blocks, existing explicit anchors, figure-path sequences, displayed equations, and the worked simulation's code remain intact. The simulated attendance counts and numerical results were not changed. Other figure generators and simulated source data were not rerun. The approximate body-word count, including tables and code, changed from 6,241 to 7,366.

## Figure verification

The final SVG is 760 × 1040 and its PNG fallback is 1140 × 1560. All text is at least 30 SVG pixels, approximately 13 pixels when the image is 330 pixels wide. The original slide image and the redraw were visually inspected; the redraw was also inspected at full size and phone width. Text containment, connector endpoints, XML validity, and exact regeneration from the figure function passed. Validity labels are annotations on sampling and assignment, not additional downstream stages.

All three Appendix F figures were then individually inspected in their final destinations: HTML at 1440px and 390px, and EPUB at 768px and 390px. All twelve captures passed for readable labels, attached arrowheads, figure numbering F.1–F.3, caption placement, and absence of horizontal page overflow. The EPUB's three figure assets match the source SVGs byte-for-byte. See `aee-appendix-f-20260914-destination-qa.json` and `aee-appendix-f-20260914-figure-source-qa.json`.

## Publication checks

- Updated HTML for Appendix F, References, and the concept index; rebuilt the complete EPUB successfully.
- Canonical source QA: **0 errors, 0 warnings**. Reference synchronization: **PASS, 878 unique entries**. EPUB release QA: **0 errors**, including internal links, packaged sources, navigation, and image alternative text.
- HTML navigation: **PASS**, all 62 configured pages, 2,360 main-content local HTML links, 685 search destinations, and 126 appendix-labeled links. See `aee-appendix-f-20260914-navigation.json`.
- Source preservation: all checks passed for original references, anchors, figure paths, displayed equations, and worked code. See `aee-appendix-f-20260914-preservation.json`.
- Verified no unpublished-slide citation remained in the revised appendix, bibliography, or HTML/search output. Source SVG/PNG companions match the HTML release copies. Generated-file permission changes were removed.

Changes were saved locally. No commit or push was performed in this revision.
