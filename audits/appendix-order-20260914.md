# Appendix order revision — 14 September 2026

Moved the former Appendices C and D to the end of the appendix sequence, as requested. The final order is:

| Letter | Appendix | Previous letter |
| --- | --- | --- |
| A | Rational Choice and Decision Analysis | A |
| B | Evolutionary Explanations of Value, Choice, and Rationality | B |
| C | Conducting and Writing a Literature Review | E |
| D | Running an Experimental Study | F |
| E | When Evidence Breaks | G |
| F | Portable Tools | C |
| G | Index of Major Examples | D |

Both publishing profiles, the reader-facing appendix labels and ranges, the concept index, and the source/EPUB order checks use this sequence. The lecture-integration report generator also uses the new labels for future runs. Historical audit records retain the numbering in effect when they were written. Source filenames and anchors remain unchanged to preserve saved links. Apart from appendix labels and ranges, source prose is unchanged by this revision; earlier local edits remain intact.

Verification:

- Full HTML and EPUB builds succeeded. Source QA reports zero errors and zero warnings; EPUB release QA reports zero errors.
- All 887 reference entries remain synchronized.
- HTML navigation checks cover all 62 pages, 2,576 main-content local links, 685 search entries, and 127 labeled appendix links. All seven appendix headings and all page sidebars match the new order. See `appendix-order-20260914-navigation.json`.
- EPUB checks confirm all seven appendix letters, 134 labeled links including navigation entries, and 37 appendix figure/table labels. See `appendix-order-20260914-epub-labels.json`.
- All 116 figures and 147 tables retain their required prose references in the source and appropriate publication editions. No hard-coded appendix figure/table numbers were found in the configured sources.
- The final diff passes whitespace checks. No commit or push was performed.
