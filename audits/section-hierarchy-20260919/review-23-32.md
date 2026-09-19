# Section hierarchy review: canonical chapter prefixes 23–32

Reviewed the complete chapter prose, including research and application callouts, against the hierarchy concern raised about the valuation chapter. Revised nine chapters; retained Chapter 28 unchanged. The changes organize headings around concepts or substantial tasks, keep individual studies/examples within the arguments they illustrate, and consolidate fragmented applications. Existing studies, results, scientific distinctions, tables, figures, footnotes, and bibliography entries are preserved.

## Chapter-by-chapter decisions

### 23 — Strategic Interdependence

The three developed examples perform different conceptual jobs and should remain navigable sections. Renamed their headings to expose those jobs: **Coordinating through shared expectations**, **Separating preference from prediction**, and **Anticipating how far others reason**. Their concert, face-choice, and guessing-game discussions remain intact. The concluding application now reads **Anticipate the response before committing**, with its existing anchor retained. The reasoning-and-learning subsection remains substantial and conceptually distinct within the guessing-game discussion.

### 24 — Coordination and Focal Points

Integrated **Unreliable communication and the electronic-mail game** and **Why public events can have disproportionate effects** into the common-knowledge section. They now extend a continuous argument: higher-order beliefs, unreliable private confirmations, and publicly visible reception. Added brief transitions making those connections explicit. Preserved both former heading anchors. The integrated diagnostic section remains, with its title shortened to **Diagnose the obstacle before choosing the tool** and its anchor retained. Game structures, commitment, and conventions still warrant separate conceptual sections.

### 25 — Cooperation and Social Preferences

- Renamed **How a future relationship supports cooperation** to **How relationships and rules support cooperation**, accurately covering repetition, reciprocity, reputation, and institutions.
- Integrated the short **Golden Balls** case into the reputation/institutions discussion. Its new opening explains why the case belongs there: audience, prior interaction, and immediate incentives coexist.
- Combined mutual-cooperation and punishment reward discussions under **Reciprocity changes what feels rewarding**. Their scientific distinctions, including BOLD versus dopamine and anticipation versus experienced mood, remain intact; the punishment anchor remains at the relevant passage.
- Integrated **Rebuild cooperation without erasing differences** into the common-ingroup-identity discussion, connecting dual identity and the practical sequence directly to the preceding account.
- Within the evolutionary research callout, integrated the fourth-level ethnocentrism example into **Spatial models: who encounters whom?**. It remains a developed model illustration with its old anchor.
- Within the social-preference research callout, integrated **Worked identification contrast: same allocation, different control** into **Outcomes and intentions are different**. The contrast now illustrates its organizing distinction instead of competing with it.
- Within the applied callout, integrated the one-paragraph daycare-fine example into the enforcement discussion, with a transition about how enforcement changes social meaning.

Six headings were consolidated; all their anchors were retained. The advanced and mathematical callouts themselves remain unchanged in status.

### 26 — Social Norms and Conformity

Integrated **Four conditions make social evidence more diagnostic** into **Learning from other people's choices**. The conditions directly answer the opening section's question about when prestige, success, similarity, and majorities provide useful evidence. Added a transition from the employee example back to the hiring committee. The former heading anchor remains. The sections on conformity, norms, cascades, and preserving independence describe distinct concepts or an integrated response and remain separate. Research-lens subsections remain developed and distinct.

### 27 — Markets, Mispricing, and Bubbles

Renamed the opening conceptual section **How markets incorporate information** and integrated the brief **Fast price discovery is possible** discussion into it. The Federal Reserve timing and Challenger studies now supply evidence for information incorporation, rather than appearing as a separate organizing topic. Preserved the former price-discovery anchor.

Combined **Lottery payoffs and cognitive reflection** and **Gender, context, and a distinct hormonal intervention** under **Payoffs and participants shape market behavior**. Added transitions distinguishing payoff distributions, individual differences, market composition, and the separate intervention. No findings or qualifications were changed. Both original anchors remain.

Renamed **A two-direction bubble dashboard** to **Evaluating competing explanations for a boom**. Its table remains a tool serving that conceptual task. Retained the developed historical comparison and laboratory-design subsections; they distinguish meaningful institutional and experimental contrasts rather than elevating single studies.

### 28 — Authority, Groupthink, and Shared Responsibility

**Unchanged.** The main sections distinguish authority, pressure for concurrence, unshared information, and failures of helping/ownership. The shorter hidden-profile discussion introduces a distinct informational mechanism; merging it with groupthink would blur a distinction the chapter needs. The final safeguard section integrates these mechanisms, and its diagnostic table is already in a note box.

### 29 — Culture and Identity

Integrated **Using cultural patterns to guide questions about individuals** into **Culture is a meaning environment**, where it establishes how to use the concept before the four lenses begin. The former heading anchor remains.

Combined **Cross cultures by asking, not assuming**, **Worked application: redesign the silent meeting**, and **The culture-and-identity meaning audit** into **Interpreting differences and designing a shared process**. Inquiry now leads directly into the opening meeting's redesign and then the general audit. All three anchors remain. The four lenses and their substantial identity, face, and organizational-culture subsections remain navigable because they distinguish genuinely different questions.

### 30 — Persuasion

Promoted and renamed the developed cue discussion as **How influence cues affect judgment and action**, a conceptual peer to processing routes. This avoids presenting reciprocity, commitment, and compliance as merely a subordinate elaboration route. Integrated **Small commitments, concessions, and self-persuasion** into that cue section, with a transition from cue validity to the sequence of requests. Its anchor remains.

Renamed the developed final synthesis **Build a proposal the audience can evaluate**; the platform example illustrates that task throughout the section. The previous platform-proposal anchor remains.

### 31 — Why Stories Move Minds

Corrected the explicit hierarchy: the four mechanism families are now third-level subsections under **Four mechanisms of narrative persuasion**, rather than five competing second-level headings. Retained each existing anchor and removed redundant heading numerals. Each mechanism has a developed discussion and warrants a subsection.

Renamed **The power—and danger—of one** to **Keep individual stories in proportion**. The identifiable-victim study remains evidence within that general task, with its old anchor retained.

### 32 — Building an Evidence-Aligned Message

Integrated **Worked transformations** and its two example headings into the developed subsection **Adapt the message to the audience’s decision**. The hiring and negotiation cases now follow the explanation of audience-specific adaptation. Short bold labels distinguish the cases without adding independent subsections. All three old anchors remain.

Renamed the final editing section **Audit the finished message**, reflecting its actual scope: clarity, representations, common failures, communication form, and ethical audit. Moved the existing common-mistakes list into that final audit, with a brief introduction. The previous editing anchor remains. The five conceptual stages now form a clearer progression: design, STORY, evidence, clarity/adaptation, and final audit.

## Verification and scope

- Compared revisions with `source-baseline.json`.
- Verified that reference sections, figure lines, table rows/captions, and footnote definitions are unchanged for all ten chapters.
- Verified that every explicit baseline anchor is retained; checked exact generated IDs in the corresponding canonical `docs/chapters/<source-stem>.html` for headings converted into explicit anchors or renamed.
- Reread the revised passages and transitions. `git diff --check` passes for the owned chapter files.
- Heading count across these ten files decreases by 17 (including callout headings in the count); four Chapter 31 headings were demoted and one Chapter 30 heading promoted to correct conceptual nesting.
- No new scientific claims or citations were required. No render, shared-index edit, reference sync, commit, or push was performed by this worker.
- No external link requires repair. The concept index's link labeled “The culture-and-identity meaning audit” still accurately names the retained audit table and reaches its preserved anchor.
