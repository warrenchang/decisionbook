from __future__ import annotations

import importlib.util
import json
import math
import os
import re
import shutil
import subprocess
import zipfile
from pathlib import Path
from typing import List, Dict, Tuple

from bs4 import BeautifulSoup
from jinja2 import Environment, BaseLoader, select_autoescape
from markdown_it import MarkdownIt

ROOT = Path('/mnt/data')
BASE_SCRIPT = ROOT / 'build_github_ebook.py'
QA_SCRIPT = ROOT / 'qa_repository.py'
spec = importlib.util.spec_from_file_location('dpn_base_builder', BASE_SCRIPT)
b = importlib.util.module_from_spec(spec)
assert spec and spec.loader
import sys
sys.modules[spec.name] = b
spec.loader.exec_module(b)

# Revised deliverables. The source DOCX remains untouched.
b.OUT = ROOT / 'Decision_Persuasion_Negotiation_GitHub_Ebook_Revised'
b.ZIP = ROOT / 'Decision_Persuasion_Negotiation_GitHub_Ebook_Revised.zip'
b.EPUB = ROOT / 'Decision_Persuasion_Negotiation_Student_Ebook_Revised.epub'

b.PARTS.clear()
b.PARTS.update({
    1: ('The Architecture of Choice', 'From the visible choice to the hidden processes of attention, prediction, valuation, and expectation.'),
    2: ('Judgment Under Uncertainty and Context', 'How shortcuts, statistics, comparison sets, frames, and fluency shape what seems true and worth doing.'),
    3: ('How Choices Become Stories and Habits', 'How post-choice explanation, repetition, craving, and environment design shape behavior over time.'),
    4: ('The Social Mind', 'How other people become models, mirrors, evidence, audiences, norms, and authorities.'),
    5: ('Persuasion, Story, and Connection', 'How messages update models, stories create simulated meaning, and conversation builds shared understanding.'),
    6: ('Negotiation: Claiming and Creating Value', 'How interdependent decision-makers prepare, bargain, trade across differences, and design workable agreements.'),
    7: ('Better Decision Systems', 'How to make good judgment repeatable through decision hygiene, structured disagreement, and learning.'),
})

PART_GUIDES = {
    1: {
        'why': 'The book begins upstream of choice. Students first need a functional map of a decision, a benchmark for coherence, and a psychologically realistic account of what becomes evidence and value.',
        'questions': ['What happens before a visible choice?', 'What would coherent choice require?', 'How do attention, prediction, value, and expectation shape the decision?'],
        'bridge': 'Once the architecture is visible, Part II examines the shortcuts and contextual forces that bend judgment inside it.'
    },
    2: {
        'why': 'The rational benchmark is useful only when students can diagnose where real judgment departs from it. This part moves from adaptive shortcuts to statistical correction and then to context effects.',
        'questions': ['When do heuristics fit the environment?', 'Why do stories overpower base rates?', 'How do anchors, frames, primes, and fluency change judgment?'],
        'bridge': 'Part III follows the decision beyond choice: how the mind explains what happened and how repeated loops become habits.'
    },
    3: {
        'why': 'A course on decision-making should not stop at one-off choices. Explanations affect learning, and repeated cue–response loops determine whether knowledge survives pressure.',
        'questions': ['Why can sincere explanations miss the cause?', 'How do choices become automatic?', 'How can behavior be redesigned without relying on heroic willpower?'],
        'bridge': 'Part IV adds other people. Social learning and social pressure now enter the same decision loop.'
    },
    4: {
        'why': 'Human judgment is culturally accumulated and socially regulated. This part separates learning from others, conformity and norms, and specific influence triggers.',
        'questions': ['When are other people good evidence?', 'How do norms and unanimity change what is speakable?', 'When does a useful social signal become a counterfeit trigger?'],
        'bridge': 'Part V turns from ambient social influence to intentional messages and then to mutual understanding.'
    },
    5: {
        'why': 'Persuasion, storytelling, and communication are related but not identical. The sequence moves from intentional model change, to narrative simulation, to the joint construction and repair of meaning.',
        'questions': ['What prevents an audience from updating?', 'How should story and evidence be braided?', 'How do people ground meaning, listen, disagree, and repair?'],
        'bridge': 'Negotiation is the capstone because it requires decision analysis, persuasion, communication, emotion regulation, and strategic interdependence at once.'
    },
    6: {
        'why': 'Negotiation turns private judgment into joint choice. The sequence moves from basic architecture to distributive preparation and tactics, then to integrative trade-offs and advanced agreement design.',
        'questions': ['What is my alternative and walk-away point?', 'How should anchors and concessions be managed?', 'How can differences in priorities, beliefs, and risk create value?'],
        'bridge': 'The final part asks how these skills can be embedded in recurring organizational and personal decision systems.'
    },
    7: {
        'why': 'The concluding chapter integrates the course into a repeatable practice. The aim is not perfect rationality, but better inputs, better process, and better learning.',
        'questions': ['What should be noticed, tested, asked, designed, and learned?', 'How can dissent become a process rather than an act of heroism?', 'How can outcomes inform learning without rewriting the past?'],
        'bridge': 'The cycle returns to Chapter 1: a visible choice is still the tip of an iceberg, but the hidden structure is now inspectable and redesignable.'
    },
}

# ---------------- Editorial structure fixes ----------------

_orig_make_social = b.make_social_chapters

def make_social_chapters(ch22, ch23):
    c22, c23, c24 = _orig_make_social(ch22, ch23)

    # Chapter 22 should end in attribution/perspective-getting, not preview Ch. 23 as a learning goal.
    for block in c22['blocks']:
        if isinstance(block, b.PBlock) and block.style == 'Learning Objective' and 'informational and normative conformity' in block.text.lower():
            block.text = 'Use an attribution flip and perspective-getting question before treating a social interpretation as fact.'

    # Remove the accidentally duplicated core idea and duplicated learning-goal block in Chapter 23,
    # while preserving the substantive norm introduction that followed them.
    cleaned = []
    core_seen = 0
    learning_seen = 0
    skip_learning_items = False
    for block in c23['blocks']:
        if isinstance(block, b.TBlock) and block.rows and block.rows[0] and b.ntext(block.rows[0][0]).upper() == 'CORE IDEA':
            core_seen += 1
            if core_seen > 1:
                continue
        if isinstance(block, b.PBlock) and block.style == 'Heading 2' and b.ntext(block.text).lower() == 'learning goals':
            learning_seen += 1
            if learning_seen > 1:
                skip_learning_items = True
                continue
        if skip_learning_items and isinstance(block, b.PBlock) and block.style == 'Learning Objective':
            continue
        if skip_learning_items:
            skip_learning_items = False
        cleaned.append(block)
    c23['blocks'] = cleaned
    return c22, c23, c24

b.make_social_chapters = make_social_chapters

_orig_restructure = b.restructure

def restructure(front, raw_chapters):
    chapters = _orig_restructure(front, raw_chapters)
    for ch in chapters:
        ch.title = b.patch_text(ch.title)
        ch.subtitle = b.patch_text(ch.subtitle)
        if ch.num == 13:
            ch.subtitle = 'Confirmation, self-serving judgment, and the feeling of knowing'
    return chapters

b.restructure = restructure


def _replace_in_block(block, replacements: Dict[str, str]):
    if isinstance(block, b.PBlock):
        for old, new in replacements.items():
            block.text = block.text.replace(old, new)
    else:
        block.rows = [[_replace_text(cell, replacements) for cell in row] for row in block.rows]


def _replace_text(text: str, replacements: Dict[str, str]) -> str:
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def _insert_heading_before(ch, paragraph_start: str, heading: str):
    for i, block in enumerate(ch.blocks):
        if isinstance(block, b.PBlock) and b.ntext(block.text).startswith(paragraph_start):
            # Avoid duplicate insertion.
            if i and isinstance(ch.blocks[i-1], b.PBlock) and ch.blocks[i-1].style == 'Heading 2' and ch.blocks[i-1].text == heading:
                return
            ch.blocks.insert(i, b.PBlock(heading, 'Heading 2'))
            return


def _max_table_number(ch) -> int:
    pat = re.compile(rf'\bTable\s+{ch.num}\.(\d+)\b', re.I)
    vals = []
    for block in ch.blocks:
        texts = [block.text] if isinstance(block, b.PBlock) else sum(block.rows, [])
        for text in texts:
            vals += [int(x) for x in pat.findall(text)]
    return max(vals, default=0)


def _insert_table_at_section_end(ch, heading: str, caption: str, rows: List[List[str]]):
    idx = next((i for i, block in enumerate(ch.blocks)
                if isinstance(block, b.PBlock) and block.style in {'Heading 2', 'Heading 3'} and b.ntext(block.text).lower() == heading.lower()), -1)
    if idx < 0:
        return
    end = len(ch.blocks)
    current_level = 2 if ch.blocks[idx].style == 'Heading 2' else 3
    for j in range(idx + 1, len(ch.blocks)):
        block = ch.blocks[j]
        if isinstance(block, b.PBlock) and block.style in {'Heading 2', 'Heading 3'}:
            lvl = 2 if block.style == 'Heading 2' else 3
            if lvl <= current_level:
                end = j
                break
    num = _max_table_number(ch) + 1
    insert = [b.PBlock(f'Table {ch.num}.{num}. {caption}', 'Caption'), b.TBlock(rows)]
    ch.blocks[end:end] = insert


def _group_headings(ch, group_heading: str, first_heading: str, last_heading: str):
    """Insert a new H2 before first_heading and demote H2s through last_heading to H3."""
    first = next((i for i, block in enumerate(ch.blocks) if isinstance(block, b.PBlock) and block.style == 'Heading 2' and b.ntext(block.text) == first_heading), -1)
    last = next((i for i, block in enumerate(ch.blocks) if isinstance(block, b.PBlock) and block.style == 'Heading 2' and b.ntext(block.text) == last_heading), -1)
    if first < 0 or last < first:
        return
    ch.blocks.insert(first, b.PBlock(group_heading, 'Heading 2'))
    last += 1
    for i in range(first + 1, last + 1):
        block = ch.blocks[i]
        if isinstance(block, b.PBlock) and block.style == 'Heading 2':
            block.style = 'Heading 3'


def _reorganize_ch24(ch):
    # Split into H2 sections.
    prefix = []
    sections = []
    current = None
    for block in ch.blocks:
        if isinstance(block, b.PBlock) and block.style == 'Heading 2':
            current = [block]
            sections.append(current)
        elif current is None:
            prefix.append(block)
        else:
            current.append(block)
    sec = {b.ntext(s[0].text): s for s in sections}
    required = ['Learning goals', 'Authority and responsibility', 'Bystanders and pluralistic ignorance',
                'A reason can be a trigger', 'Social proof', 'Commitment and consistency', 'Reciprocity',
                'Authority', 'Scarcity', 'Liking', 'Unity', 'Signals and counterfeit signals',
                'When influence helps - and harms', 'Designing and resisting influence', 'Key ideas', 'Study and practice']
    if not all(k in sec for k in required):
        return

    diagnostic = [
        b.PBlock('Influence triggers: a diagnostic map', 'Heading 2'),
        b.PBlock('Influence triggers are compressed social rules. They are useful when a visible cue reliably tracks expertise, demand, obligation, commitment, or shared identity. They become manipulative when the cue is manufactured, material facts are hidden, or the cost of refusal is quietly increased.', 'Normal'),
        b.PBlock('Table 24.1. Legitimate signals and counterfeit triggers', 'Caption'),
        b.TBlock([
            ['Trigger', 'Legitimate information it can carry', 'Counterfeit form', 'Pause question'],
            ['A reason', 'The request has a relevant justification.', 'A reason-shaped phrase with no diagnostic content.', 'Would the reason change my judgment if the word “because” disappeared?'],
            ['Social proof', 'Independent people with relevant experience converged.', 'Bots, copied reviews, paid popularity, or a cascade.', 'Are these judgments independent?'],
            ['Commitment', 'A freely chosen promise expresses an endorsed value.', 'Early commitment was obtained before costs were disclosed.', 'Was the commitment informed and reversible?'],
            ['Reciprocity', 'A genuine gift or concession supports cooperation.', 'A strategic favor functions as a hidden invoice.', 'Would I owe this if the tactic were explicit?'],
            ['Authority', 'Relevant expertise is accountable and evidence-based.', 'Titles, uniforms, confidence, or logos substitute for reasons.', 'What is the source expert in, and who checks them?'],
            ['Scarcity', 'Limited supply or time is real and decision-relevant.', 'A fake countdown or manufactured shortage creates panic.', 'Is the scarcity genuine, and does it change underlying value?'],
            ['Liking', 'Trust grows from repeated, responsive interaction.', 'Charm, similarity, or compliments bypass scrutiny.', 'Would the claim survive if I disliked the source?'],
            ['Unity', 'Shared identity supports mutual obligation.', 'Belonging is built through exclusion or contempt.', 'What is this “we” asking me not to see?'],
        ])
    ]

    trigger_names = ['A reason can be a trigger', 'Social proof', 'Commitment and consistency', 'Reciprocity', 'Authority', 'Scarcity', 'Liking', 'Unity']
    trigger_blocks = [b.PBlock('Eight recurring triggers', 'Heading 2')]
    for name in trigger_names:
        part = sec[name]
        part[0].style = 'Heading 3'
        trigger_blocks.extend(part)

    # Drop the redundant long overview section; every substantive trigger is retained in the detailed sections.
    new_blocks = prefix + sec['Learning goals'] + sec['Authority and responsibility'] + sec['Bystanders and pluralistic ignorance']
    new_blocks += diagnostic + trigger_blocks + sec['Signals and counterfeit signals']
    new_blocks += sec['When influence helps - and harms'] + sec['Designing and resisting influence'] + sec['Key ideas'] + sec['Study and practice']
    ch.blocks = new_blocks


def _add_summary_tables(ch):
    tables = {
        5: ('Designing better attention', 'Attention failures and design responses', [
            ['Failure', 'Mechanism', 'Design response'],
            ['Unexpected event is missed', 'Search is tuned to another target.', 'Assign an anomaly role or run a deliberate second scan.'],
            ['Important information never enters discussion', 'Agenda, metric, or hierarchy filters attention.', 'Change the question, representation, or speaking order.'],
            ['Divided attention weakens encoding', 'Working memory is consumed by task switching.', 'Protect focused intervals and remove avoidable digital capture.'],
            ['Team closes too early', 'A coherent interpretation suppresses alternatives.', 'Use a diagnostic timeout, premortem, or independent review.'],
        ]),
        7: ('Using valuation wisely', 'Questions for separating value from evidence', [
            ['Question', 'What it diagnoses', 'Typical risk'],
            ['What am I feeling?', 'The current value signal.', 'Treating emotion as probability.'],
            ['What feature has my attention?', 'Attribute weighting in the moment.', 'Ignoring a quiet but important objective.'],
            ['Do I want this, or expect to like it?', 'Motivational pull versus experienced value.', 'Choosing the cue rather than the outcome.'],
            ['Whose approval or identity is involved?', 'Social and self-relevance.', 'Borrowing another audience’s values.'],
            ['What changes if my state changes?', 'Hunger, fatigue, threat, or mood dependence.', 'Mistaking a temporary state for a stable preference.'],
        ]),
        8: ('Building truthful, supported expectations', 'Expectation pathways and ethical conditions', [
            ['Domain', 'Pathway', 'Ethical condition'],
            ['Medicine', 'Expectation changes attention, anxiety, and symptom experience.', 'Give balanced risk information and a credible coping plan.'],
            ['Education', 'Ability beliefs change effort, persistence, and interpretation of difficulty.', 'Pair high expectations with strategy, support, and opportunity.'],
            ['Management', 'Leader expectations change autonomy, feedback, and challenge.', 'Make resources and standards match the expectation.'],
            ['Relationships', 'Predicted rejection changes behavior and the response it elicits.', 'Test the prediction through perspective-getting, not mind-reading.'],
        ]),
        10: ('Vivid memory and hidden denominators', 'When affect and availability help or mislead', [
            ['Shortcut', 'Useful when', 'Misleads when', 'Corrective'],
            ['Affect', 'Feeling summarizes relevant, repeated experience.', 'Mood or identity spills into an unrelated forecast.', 'Name the feeling, then estimate probability separately.'],
            ['Availability', 'Memory samples the environment fairly.', 'News, vividness, recency, or repetition distort retrieval.', 'Find the denominator and a representative reference class.'],
            ['Personal example', 'The case is diagnostically similar.', 'One case substitutes for a distribution.', 'Ask how often the pattern occurs across comparable cases.'],
        ]),
        11: ('Small samples, streaks, and clusters', 'From resemblance to probability', [
            ['Evidence', 'Question it can answer', 'Common error', 'Better use'],
            ['Prototype match', 'What category does this resemble?', 'Treating resemblance as probability.', 'Combine with base rates and diagnosticity.'],
            ['Detailed story', 'How could events connect?', 'Conjunction fallacy: detail feels more likely.', 'Check whether added conditions can only reduce probability.'],
            ['Short streak', 'What happened in this small sample?', 'Inferring a stable process from noise.', 'Estimate expected variation and seek more observations.'],
            ['Appearance or confidence', 'What first impression was triggered?', 'Substituting “looks like” for predictive evidence.', 'Use structured, job-relevant measures.'],
        ]),
        13: ('Three forms of overconfidence', 'Bias diagnosis and process correction', [
            ['Bias', 'Story from the inside', 'Process correction'],
            ['Confirmation / myside', '“The evidence keeps supporting us.”', 'Specify disconfirming evidence and assign an opposing test.'],
            ['Self-serving judgment', '“Our success was skill; failure was circumstance.”', 'Apply the same attribution rule to self and others.'],
            ['Overestimation', '“We can do more than the record suggests.”', 'Compare prediction with past calibrated performance.'],
            ['Overplacement', '“We are better than the competitors.”', 'Use a real comparison distribution, not an imagined average.'],
            ['Overprecision', '“The range is narrow because the story is clear.”', 'Use intervals, scenarios, and sensitivity analysis.'],
        ]),
        15: ('Ethical framing', 'Framing mechanisms and safeguards', [
            ['Frame type', 'What changes', 'Safeguard'],
            ['Attribute frame', 'Which side of an equivalent description is focal.', 'Present both logically equivalent forms.'],
            ['Risky-choice frame', 'Whether outcomes are coded as gains or losses.', 'Make the reference point explicit.'],
            ['Goal frame', 'Whether action pursues benefit or avoids cost.', 'Match the frame to accurate stakes and efficacy.'],
            ['Question frame', 'Which alternatives and causes enter search.', 'Ask a second question from another stakeholder’s perspective.'],
            ['Causal frame', 'Who or what appears responsible.', 'Test competing mechanisms before assigning blame.'],
        ]),
        16: ('What the evidence does - and does not - justify', 'Evidence tiers in priming', [
            ['Claim', 'Evidence status', 'Responsible interpretation'],
            ['Semantic and perceptual accessibility', 'Robust across many laboratory paradigms.', 'Recent activation can change speed and interpretation.'],
            ['Affective evaluation', 'Well-supported under specified tasks.', 'A prior cue can tilt immediate evaluation.'],
            ['Identity and goal activation', 'Context-sensitive with important boundary conditions.', 'Effects depend on relevance, motivation, awareness, and setting.'],
            ['Large automatic behavioral effects from subtle social primes', 'Many famous findings are contested or difficult to replicate.', 'Do not present priming as mind control or a universal behavior switch.'],
        ]),
        17: ('Defending against misleading ease', 'What processing ease can and cannot tell you', [
            ['Source of ease', 'Potentially valid inference', 'Invalid leap', 'Check'],
            ['Clear organization', 'The message is easier to understand.', 'The claim must be true.', 'Inspect evidence and omitted complexity.'],
            ['Repetition', 'The statement is familiar.', 'The statement is accurate.', 'Trace independent sources.'],
            ['Easy pronunciation', 'The name is fluent.', 'The product is safer or better.', 'Separate the label from outcome data.'],
            ['Familiar option', 'Past exposure reduces uncertainty.', 'The option has the best value now.', 'Compare current alternatives and costs.'],
        ]),
        20: ('Self-control without heroics', 'Intervene before the peak of temptation', [
            ['Stage', 'Tool', 'Why it helps'],
            ['Before the cue', 'Situation selection, availability, precommitment.', 'Prevents the strongest loop from being activated.'],
            ['At the cue', 'Prompt, if–then plan, replacement action.', 'Makes the desired response retrievable.'],
            ['During the urge', 'Name sensations, urge surf, delay, BRAIN/RAIN.', 'Turns a command into a changing experience.'],
            ['After action', 'Immediate feedback and nonmoralizing review.', 'Updates the promised reward against the actual experience.'],
            ['After lapse', 'Recovery plan and next-cue restart.', 'Prevents one lapse from becoming an identity and a streak.'],
        ]),
        22: ('Other people as living data', 'Auditing social evidence', [
            ['Social cue', 'Why it can be useful', 'Failure mode', 'Test'],
            ['Prestige', 'May summarize recognized expertise.', 'Status spills across domains.', 'What relevant performance earned the prestige?'],
            ['Majority behavior', 'Can aggregate independent experience.', 'People may be copying the same source.', 'How independent are the judgments?'],
            ['Similarity', 'Similar people may face similar constraints.', 'Shared identity can share the same blind spot.', 'Which similarities are decision-relevant?'],
            ['Mimicry / synchrony', 'Can signal responsiveness and rapport.', 'Performed similarity becomes manipulation.', 'Does attunement improve mutual understanding?'],
            ['Attribution', 'Creates a causal model for the next action.', 'Character stories hide situational constraints.', 'What question would discriminate among explanations?'],
        ]),
        25: ('Two routes through a message', 'Audience conditions and persuasion design', [
            ['Audience condition', 'Likely processing', 'Design implication'],
            ['High motivation and ability', 'Careful scrutiny of arguments.', 'Use strong evidence, causal logic, uncertainty, and counterarguments.'],
            ['High motivation, low ability', 'Interest without sufficient comprehension.', 'Reduce jargon, scaffold concepts, and show concrete mechanisms.'],
            ['Low motivation, high ability', 'Limited willingness to elaborate.', 'Create relevance before adding detail.'],
            ['Low motivation and ability', 'Greater reliance on cues and simple heuristics.', 'Use transparent cues, one clear action, and avoid exploiting inattention.'],
        ]),
        26: ('The psychology of narrative persuasion', 'Narrative mechanisms, design questions, and risks', [
            ['Mechanism', 'Design question', 'Risk'],
            ['Attention', 'What unresolved question makes the audience want the next event?', 'Manufactured suspense can hide weak relevance.'],
            ['Transportation', 'What world is the audience invited to simulate?', 'Absorption can smuggle assumptions past scrutiny.'],
            ['Identification', 'Whose goals and constraints can the audience understand?', 'A single perspective can erase affected others.'],
            ['Emotion and valuation', 'What should matter if the evidence is understood?', 'Intensity can exceed the truth of the stakes.'],
            ['Causal simulation', 'What mechanism links choice to consequence?', 'A coherent story can be mistaken for causal proof.'],
            ['Memory', 'What principle will the story make retrievable?', 'The vivid case may crowd out the base rate.'],
        ]),
        28: ('Communication is coordination and repair', 'Grounding failures and repair moves', [
            ['Failure', 'Hidden source', 'Repair move'],
            ['Same word, different meaning', 'Different assumptions or professional models.', 'Ask for an example and define the term in use.'],
            ['Tone is misread', 'Text removes vocal and contextual cues.', 'State intent explicitly and check interpretation.'],
            ['Mind-reading hardens', 'An inference is treated as fact.', 'Name it as a hypothesis and ask the person.'],
            ['Agreement is assumed', 'Silence is interpreted as consent.', 'Invite a summary, private response, or explicit concern.'],
            ['Perspective-taking projects the self', 'We imagine what we would feel.', 'Use perspective-getting: ask, listen, and verify.'],
        ]),
        30: ('What negotiation is not', 'Negotiation myths and replacement questions', [
            ['Myth', 'Hidden cost', 'Replacement question'],
            ['“Good negotiators are tough.”', 'Toughness can destroy information and value.', 'What process protects interests and learning?'],
            ['“Success means reaching agreement.”', 'A deal can be worse than the BATNA.', 'Is this agreement better than our best alternative?'],
            ['“Compromise is the ideal.”', 'Splitting positions can miss compatible interests.', 'What do the parties value differently?'],
            ['“Negotiation begins at the table.”', 'Alternatives, stakeholders, and standards are left undeveloped.', 'What can be improved before the conversation?'],
            ['“Signing ends the negotiation.”', 'Implementation and adaptation are ignored.', 'How will the agreement be governed, reviewed, and repaired?'],
        ]),
        33: ('Preparing across issues', 'A priority map for integrative trade-offs', [
            ['Issue', 'My priority', 'Their likely priority', 'Potential trade'],
            ['Price / salary', 'High', 'High', 'Use standards; do not expect easy integration.'],
            ['Timing', 'High', 'Low or different', 'Trade speed, start date, or staging for value elsewhere.'],
            ['Risk allocation', 'Medium', 'Different tolerance or forecast', 'Use warranties, insurance, or contingent terms.'],
            ['Recognition / title', 'Low cost to one side', 'High symbolic value to the other', 'Trade status or visibility for a material term.'],
            ['Future relationship', 'Different time horizons', 'Different', 'Use volume, renewal, review, or option clauses.'],
        ]),
    }
    if ch.num in tables:
        _insert_table_at_section_end(ch, *tables[ch.num])


_orig_clean = b.clean_chapter_flow

def clean_chapter_flow(ch):
    _orig_clean(ch)

    replacements = {
        'Chapter 18 described rationalization as the story after the choice.': 'Chapter 18 examines rationalization as the story after the choice.',
        'This bias will connect to later chapters on framing, choice architecture, and nudging,': 'This bias connects directly to Chapter 15 on framing and Chapter 21 on behavior design,',
        'This error will be discussed more fully in the chapter on probability judgment.': 'Chapter 12 develops the statistical correction in detail.',
        'As Earlier chapters explained': 'As earlier chapters explained',
        'the preparation discussed in Chapter 13': 'the preparation discussed in Chapter 31',
        'The chapter ends with two bridges. Chapter 8 first examines expectations: beliefs that can change attention, action, and feedback. Part III then follows repeated cue–value–action loops as they become habits.':
            'The chapter ends with two bridges. Chapter 8 examines expectations: beliefs that can change attention, action, and feedback. Part II then shows how shortcuts and context shape judgment; Chapters 18–21 follow the choice into explanation, habit, self-control, and behavior design.',
        'Part III turns from explanation to habits and behavior design. Expectations shape what we notice, feel, and do.':
            'Parts II and III carry this loop forward. Chapters 9–18 examine judgment and post-choice explanation; Chapters 19–21 then show how repeated expectation-guided actions can become habits and how those habits can be redesigned. Expectations shape what we notice, feel, and do.',
    }
    for block in ch.blocks:
        _replace_in_block(block, replacements)

    if ch.num == 5:
        _insert_heading_before(ch, 'Imagine watching a video of people passing a basketball.', 'Inattentional blindness: what attention leaves out')
        _insert_heading_before(ch, 'Attention is often described as a spotlight, but that metaphor can mislead.', 'Top-down goals and bottom-up capture')
        _insert_heading_before(ch, 'Attention is also limited.', 'Attention under divided demand')
        _insert_heading_before(ch, 'Change blindness shows a related problem.', 'Change blindness')

    if ch.num == 24:
        _reorganize_ch24(ch)

    # Reduce overly fragmented web TOCs while preserving all substantive subsections.
    if ch.num == 27:
        _group_headings(ch, 'Design the change', "Begin with the audience's current story", 'Turning point, evidence, and change')
        _group_headings(ch, 'Applications across DPN', 'Teaching and academic writing', 'Stories in negotiation')
        _group_headings(ch, 'Ethics and common failure modes', 'Ethical storytelling', 'Common mistakes')
        _group_headings(ch, 'Worked transformations', 'From argument to story', 'Worked example: negotiation deadline')
        _group_headings(ch, 'Advanced craft and judgment', 'Story under information overload', 'Story as a technology of meaning')
    if ch.num == 32:
        _group_headings(ch, 'Concessions and pressure', 'When an offer is surprisingly good', 'Common tactics and responses')
        _group_headings(ch, 'Ethics and process', 'Ethics in claiming value', 'A distributive process')
        _group_headings(ch, 'Worked examples', 'Worked example: salary', 'Worked example: used car')
    if ch.num == 34:
        _group_headings(ch, 'Designing across disagreement', 'Contingent contracts', 'Post-settlement settlements')
        _group_headings(ch, 'Applications', 'Employment', 'Public policy')
        _group_headings(ch, 'Ethics, process, and implementation', 'Ethics of value creation', 'From agreement to architecture')

    _add_summary_tables(ch)

b.clean_chapter_flow = clean_chapter_flow

# ---------------- Visual system ----------------

_orig_generate_figures = b.generate_figures

def _finish_figure(d, p, key, figs, caption, alt):
    b.save_svg(d, p)
    figs[key] = {'file': p.name, 'caption': caption, 'alt': alt}


def generate_figures(figdir: Path):
    figs = _orig_generate_figures(figdir)

    # A portrait cover for EPUB readers and repository previews.
    cover_path = figdir / 'cover.svg'
    cover = b.new_svg(
        cover_path,
        w=1600,
        h=2560,
        title='Decision, Persuasion, and Negotiation cover',
        desc='Dark blue course-textbook cover with the title, subtitle, author, and a five-stage line from notice to bargain.'
    )
    C = b.COL
    cover.elements.clear()
    cover.add(cover.rect(insert=(0, 0), size=(1600, 2560), fill='#17324d'))
    cover.add(cover.circle(center=(1240, 300), r=235, fill='#2b7a78', opacity=.48))
    cover.add(cover.circle(center=(1345, 485), r=160, fill='#d98a4a', opacity=.55))
    cover.add(cover.line(start=(110, 600), end=(1490, 600), stroke='#9bd4ef', stroke_width=4))
    def ctext(x, y, text, size, weight='normal', fill='white', anchor='start'):
        cover.add(cover.text(text, insert=(x, y), font_family='Arial, sans-serif', font_size=size,
                             font_weight=weight, text_anchor=anchor, fill=fill))
    for y, line in [(890, 'DECISION,'), (1010, 'PERSUASION,'), (1130, 'AND NEGOTIATION')]:
        ctext(110, y, line, 88, 'bold')
    ctext(110, 1285, 'How Minds Choose, Influence,', 38, fill='#d7e5ef')
    ctext(110, 1340, 'Connect, and Bargain', 38, fill='#d7e5ef')
    stages = ['NOTICE', 'PREDICT', 'VALUE', 'CONNECT', 'BARGAIN']
    xs = [160, 470, 780, 1090, 1400]
    for i, (x, label) in enumerate(zip(xs, stages)):
        cover.add(cover.circle(center=(x, 1770), r=78, fill='none', stroke='#d7e5ef', stroke_width=5))
        ctext(x, 1781, label, 24, 'bold', anchor='middle')
        if i < len(xs)-1:
            cover.add(cover.line(start=(x+78, 1770), end=(xs[i+1]-88, 1770), stroke='#d98a4a', stroke_width=5))
            cover.add(cover.polygon(points=[(xs[i+1]-88,1770),(xs[i+1]-108,1759),(xs[i+1]-108,1781)], fill='#d98a4a'))
    ctext(110, 2265, 'HUANREN WARREN ZHANG', 34, 'bold')
    ctext(110, 2335, '2026 REVISED COURSE EDITION', 24, fill='#b9cbd8')
    b.save_svg(cover, cover_path)
    C = b.COL

    # Front-matter reading map.
    p = figdir / 'book-flow.svg'; d = b.new_svg(p, h=720, title='Reading map for the textbook', desc='Seven parts move from the architecture of individual choice through uncertainty, habit, social influence, persuasion and communication, negotiation, and better decision systems.')
    b.txt(d, 600, 48, 'A reading map: from private judgment to joint decision systems', 32, 'bold')
    labels = [
        ('1', 'Architecture of choice', 70, 125, C['light'], C['blue']),
        ('2', 'Uncertainty + context', 355, 125, C['sand'], C['orange']),
        ('3', 'Stories + habits', 640, 125, '#edf4ed', C['green']),
        ('4', 'The social mind', 925, 125, '#f5ebf5', '#795a8a'),
        ('5', 'Persuasion + connection', 210, 390, C['light'], C['blue']),
        ('6', 'Negotiation', 495, 390, C['sand'], C['orange']),
        ('7', 'Better decision systems', 780, 390, '#edf4ed', C['green']),
    ]
    for n, lab, x, y, fill, stroke in labels:
        b.box(d, x, y, 210, 105, f'Part {n}', lab, fill=fill, stroke=stroke)
    for a in [(280,178,355,178),(565,178,640,178),(850,178,925,178),(1030,230,315,390),(420,442,495,442),(705,442,780,442)]:
        b.arrow(d, *a, stroke=C['teal'], width=3)
    b.txt(d, 600, 610, 'Each part changes the question: What happened? → What is likely? → What matters? → Whose mind enters? → How do we update together?', 21)
    _finish_figure(d, p, 'book-flow', figs, 'Reading map. The book moves from individual judgment to social influence, communication, negotiation, and decision-system design.', 'Seven-part reading map from the architecture of choice to better decision systems.')

    # Ch. 3
    p = figdir / 'option-information.svg'; d = b.new_svg(p, title='Option generation, opportunity cost, and value of information', desc='Better decisions expand the feasible set, identify the best forgone alternative, seek information only when it could change action, and test whether the choice survives plausible assumptions.')
    b.txt(d, 600, 48, 'Better choices begin before comparison', 34, 'bold')
    items = [('Expand the feasible set', 'generate • combine • negotiate', 50), ('Name the best forgone option', 'opportunity cost', 330), ('Ask what could change the choice', 'value of information', 610), ('Stress-test the ranking', 'sensitivity + reversibility', 890)]
    for title, sub, x in items: b.box(d, x, 230, 230, 125, title, sub, fill=C['light'] if x < 600 else C['sand'], stroke=C['blue'] if x < 600 else C['orange'])
    for x1, x2 in [(280,330),(560,610),(840,890)]: b.arrow(d, x1,292,x2,292)
    b.txt(d,600,470,'The “best” calculation cannot rescue a menu that omitted the best feasible option.',23)
    b.txt(d,600,530,'Information is valuable only when it can change action enough to justify its cost.',21,fill=C['gray'])
    _finish_figure(d,p,'option-information',figs,'A disciplined decision expands options, represents sacrifice, values information, and tests sensitivity before committing.','Four-step flow from option generation through opportunity cost and value of information to sensitivity analysis.')

    # Ch. 10
    p = figdir / 'affect-availability.svg'; d = b.new_svg(p, title='Affect and availability as substitutions', desc='Feelings and ease of recall can substitute for evidence about risk, benefit, frequency, or probability; a corrective separates value from likelihood and retrieves a denominator.')
    b.txt(d,600,48,'When feeling and memory answer the wrong question',34,'bold')
    b.box(d,70,150,275,115,'Affect cue','How good or bad does it feel?',fill=C['sand'],stroke=C['orange'])
    b.box(d,70,390,275,115,'Available examples','How easily can I recall it?',fill=C['light'],stroke=C['blue'])
    b.arrow(d,345,205,520,285,stroke=C['orange']); b.arrow(d,345,445,520,325,stroke=C['blue'])
    b.box(d,520,235,265,145,'Substituted judgment','“High risk / common / valuable”',fill=C['navy'],stroke=C['navy']); b.txt(d,652,296,'Substituted judgment',26,'bold',fill='white'); b.txt(d,652,333,'high risk • common • valuable',18,fill='white')
    b.arrow(d,785,307,920,307)
    b.box(d,920,205,230,205,'Decision audit','Separate feeling from probability.\nFind the denominator.\nUse a reference class.',fill='#edf4ed',stroke=C['green'])
    b.txt(d,600,585,'The shortcut is adaptive when the cue samples reality fairly—and biased when salience has been engineered.',21,fill=C['gray'])
    _finish_figure(d,p,'affect-availability',figs,'Affect and availability become biases when a feeling or memorable case silently substitutes for probability and evidence.','Affect and available examples converge on a substituted judgment, followed by a denominator and reference-class audit.')

    # Ch. 11
    p = figdir / 'prototype-probability.svg'; d = b.new_svg(p, title='Prototype resemblance versus probability', desc='Resemblance generates a quick category match, but probability also requires a base rate and evidence diagnosticity.')
    b.txt(d,600,48,'A representative story is not yet a probability',34,'bold')
    b.box(d,65,160,300,155,'Prototype match','How much does this case resemble the category?',fill=C['sand'],stroke=C['orange'])
    b.arrow(d,365,238,535,238,stroke=C['orange']); b.box(d,535,180,230,115,'Quick likelihood','“It fits, so it is likely.”',fill='#f9e7e7',stroke=C['red'])
    b.box(d,65,405,300,125,'Base rate','How common is the category?',fill=C['light'],stroke=C['blue'])
    b.box(d,455,405,300,125,'Diagnosticity','How different is this evidence under alternatives?',fill=C['light'],stroke=C['blue'])
    b.arrow(d,365,468,455,468); b.arrow(d,755,468,895,365,stroke=C['teal']); b.arrow(d,765,238,895,300,stroke=C['teal'])
    b.box(d,895,245,255,170,'Calibrated probability','prior + diagnostic evidence\n+ sample size',fill='#edf4ed',stroke=C['green'])
    b.txt(d,600,595,'More detail can improve narrative fit while reducing statistical probability.',22,fill=C['gray'])
    _finish_figure(d,p,'prototype-probability',figs,'Probability requires base rates and diagnostic evidence in addition to resemblance.','Prototype match produces a quick likelihood judgment, while base rate and diagnosticity produce calibrated probability.')

    # Ch. 13
    p = figdir / 'belief-protection-loop.svg'; d = b.new_svg(p, title='Belief protection loop', desc='A belief guides search, interpretation, memory, and confidence, which reinforce the belief. Disconfirming tests and independent standards can interrupt the loop.')
    b.txt(d,600,48,'How a belief becomes its own evidence',34,'bold')
    labs=[('Belief','a conclusion feels plausible'),('Selective search','supporting evidence is easier to seek'),('Biased interpretation','ambiguity is read in its favor'),('Confidence','coherence feels like knowledge'),('Memory + explanation','support is retrieved and failure externalized')]
    pts=[]; cx,cy,R=600,320,220
    for i,(a,sub) in enumerate(labs):
        ang=-math.pi/2+2*math.pi*i/5; x=cx+R*math.cos(ang); y=cy+R*math.sin(ang); pts.append((x,y)); b.box(d,x-105,y-48,210,96,a,sub,fill=C['light'] if i<3 else C['sand'],stroke=C['blue'] if i<3 else C['orange'])
    for i in range(5): b.arrow(d,pts[i][0],pts[i][1],pts[(i+1)%5][0],pts[(i+1)%5][1],stroke=C['teal'],width=3)
    b.box(d,460,270,280,100,'Interrupt the loop','predefine criteria • consider opposite\nindependent estimate • calibration',fill='#edf4ed',stroke=C['green'])
    _finish_figure(d,p,'belief-protection-loop',figs,'Bias persists when search, interpretation, memory, and confidence form a self-reinforcing loop.','Circular belief-protection loop with a central intervention box for disconfirming tests and independent standards.')

    # Ch. 14
    p = figdir / 'anchor-decoy.svg'; d = b.new_svg(p, title='Anchoring and decoy effects', desc='The first number pulls later estimates through insufficient adjustment; a decoy changes the comparison set and can make one option look dominant.')
    b.txt(d,600,48,'Context bends numerical and comparative judgment',34,'bold')
    b.txt(d,275,105,'Anchoring',27,'bold'); b.txt(d,895,105,'Decoy comparison',27,'bold')
    b.box(d,70,175,180,100,'First number','offer • list price • forecast',fill=C['sand'],stroke=C['orange']); b.arrow(d,250,225,385,225,stroke=C['orange']); b.box(d,385,175,180,100,'Adjustment','usually insufficient',fill=C['light'],stroke=C['blue']); b.arrow(d,475,275,475,390); b.box(d,350,390,250,105,'Final estimate','still pulled toward the anchor',fill='#f9e7e7',stroke=C['red'])
    # option set
    b.box(d,700,175,170,100,'Option A','strong on quality',fill=C['light'],stroke=C['blue']); b.box(d,955,175,170,100,'Option B','strong on price',fill=C['light'],stroke=C['blue']); b.box(d,955,390,170,100,'Decoy B−','worse than B on both',fill=C['sand'],stroke=C['orange']); b.arrow(d,1040,390,1040,275,stroke=C['orange']); b.txt(d,910,335,'B now looks\nclearly dominant',22,'bold',fill=C['orange'])
    b.txt(d,600,585,'Independent estimates protect against anchors; stable criteria protect against comparison-set manipulation.',21,fill=C['gray'])
    _finish_figure(d,p,'anchor-decoy',figs,'Anchors pull numerical judgments, while decoys change the comparison that constructs preference.','Two-panel diagram showing insufficient adjustment from an anchor and a decoy making one option appear dominant.')

    # Ch. 16
    p = figdir / 'priming-pathway.svg'; d = b.new_svg(p, title='Priming pathway', desc='A prior cue increases accessibility of a concept, which can shape interpretation and evaluation of ambiguous input. Effects depend on timing, relevance, awareness, goals, and context.')
    b.txt(d,600,48,'Priming changes what is ready to interpret the next event',34,'bold')
    items=[('Prior cue','word • image • identity • goal',50,C['sand'],C['orange']),('Accessibility','related concepts become easier',330,C['light'],C['blue']),('Ambiguous input','email • face • offer • event',610,C['light'],C['blue']),('Interpretation + evaluation','which meaning wins?',890,'#edf4ed',C['green'])]
    for title,sub,x,fill,stroke in items: b.box(d,x,225,230,125,title,sub,fill=fill,stroke=stroke)
    for x1,x2 in [(280,330),(560,610),(840,890)]: b.arrow(d,x1,287,x2,287)
    b.box(d,350,445,500,95,'Boundary conditions','timing • relevance • awareness • motivation • measurement • replication',fill='white',stroke=C['teal'])
    b.txt(d,600,585,'Priming is altered accessibility, not a remote control for complex behavior.',22,fill=C['gray'])
    _finish_figure(d,p,'priming-pathway',figs,'Priming affects accessibility and can tilt interpretation, but effects depend on clear boundary conditions.','Four-step path from prior cue to accessibility, ambiguous input, and interpretation, with a boundary-conditions box.')

    # Ch. 17
    p = figdir / 'fluency-pathway.svg'; d = b.new_svg(p, title='Processing fluency pathway', desc='Repetition, clarity, familiarity, and pronunciation increase processing ease, which can be misattributed to truth, liking, safety, and confidence. An evidence check separates ease from validity.')
    b.txt(d,600,48,'The mind often treats ease as evidence',34,'bold')
    sources=[('repetition',95),('clarity',285),('familiarity',475),('pronounceability',665)]
    for lab,x in sources: b.box(d,x,145,165,80,lab,'',fill=C['light'],stroke=C['blue']); b.arrow(d,x+82,225,600,305,width=2)
    b.box(d,485,270,230,120,'Processing ease','smooth • familiar • coherent',fill=C['sand'],stroke=C['orange'])
    outs=[('truth',825,145),('liking',1000,145),('safety',825,390),('confidence',1000,390)]
    for lab,x,y in outs: b.box(d,x,y,145,80,lab,'',fill='#f9e7e7',stroke=C['red']); b.arrow(d,715,330,x,y+40,stroke=C['orange'],width=2)
    b.box(d,120,430,420,105,'Evidence check','Why is this easy? What independent evidence supports it?',fill='#edf4ed',stroke=C['green']); b.arrow(d,540,480,600,390,stroke=C['green'])
    _finish_figure(d,p,'fluency-pathway',figs,'Processing ease can be misattributed to truth, liking, safety, and confidence.','Repetition, clarity, familiarity, and pronounceability feed processing ease, which branches to truth, liking, safety, and confidence, with an evidence check.')

    # Ch. 20
    p = figdir / 'wanting-liking.svg'; d = b.new_svg(p, title='Wanting, liking, and craving', desc='A cue can create strong wanting and action readiness even when experienced liking is weak. Observing the urge and comparing promised with actual reward supports relearning.')
    b.txt(d,600,48,'Wanting can remain strong after liking has faded',34,'bold')
    b.box(d,65,235,200,110,'Cue','notification • smell • stress • place',fill=C['sand'],stroke=C['orange']); b.arrow(d,265,290,430,290,stroke=C['orange'])
    b.box(d,430,190,260,200,'Wanting','incentive salience\nattention + action readiness',fill='#f9e7e7',stroke=C['red']); b.txt(d,560,270,'Wanting',29,'bold',fill=C['red']); b.txt(d,560,310,'attention + action readiness',18)
    b.arrow(d,690,290,840,290,stroke=C['red']); b.box(d,840,205,260,170,'Outcome','actual liking may be brief, weak,\nor followed by regret',fill=C['light'],stroke=C['blue'])
    b.box(d,355,465,490,95,'Relearning','observe the wave • delay • compare promise with experience • change the cue',fill='#edf4ed',stroke=C['green']); b.arrow(d,970,375,760,465,stroke=C['green']); b.arrow(d,355,512,165,345,stroke=C['green'])
    _finish_figure(d,p,'wanting-liking',figs,'Craving is a prediction and action tendency; comparing promised reward with actual experience creates room for relearning.','Cue leads to strong wanting and then an outcome with lower liking, followed by a relearning feedback loop.')

    # Ch. 22
    p = figdir / 'social-learning-culture.svg'; d = b.new_svg(p, title='Social learning and cumulative culture', desc='People observe, imitate, coordinate, teach, and preserve practices, producing cumulative culture; the same pathway can copy errors and obsolete rituals.')
    b.txt(d,600,48,'Social learning turns individual experience into cumulative culture',34,'bold')
    items=[('Observe','others become evidence',50),('Imitate','actions and conventions',280),('Coordinate','shared expectations',510),('Teach + preserve','high-fidelity transmission',740),('Cumulative culture','tools • norms • institutions',970)]
    for title,sub,x in items: b.box(d,x,220,180,115,title,sub,fill=C['light'] if x<700 else C['sand'],stroke=C['blue'] if x<700 else C['orange'])
    for x1,x2 in [(230,280),(460,510),(690,740),(920,970)]: b.arrow(d,x1,277,x2,277)
    b.box(d,380,445,440,100,'Risk of copied error','prestige without expertise • cascades • ritual without function',fill='#f9e7e7',stroke=C['red']); b.arrow(d,600,335,600,445,stroke=C['red'])
    b.txt(d,600,590,'The right question is not “Did others do it?” but “What information made their behavior worth copying?”',21,fill=C['gray'])
    _finish_figure(d,p,'social-learning-culture',figs,'Social learning supports cumulative culture while also transmitting errors, cascades, and obsolete routines.','Five-step social-learning flow from observing to cumulative culture, with a branch to copied-error risks.')

    # Overwrite the previous broad social pathways graphic with a Ch. 23-specific norm cascade.
    p = figdir / 'social-pathways.svg'; d = b.new_svg(p, title='From private information to a social cascade', desc='Private judgments become public actions; observed actions become social evidence; apparent consensus raises the cost of dissent and can produce a cascade. Independent elicitation interrupts the loop.')
    b.txt(d,600,48,'How apparent consensus can manufacture more consensus',34,'bold')
    items=[('Private signal','what I saw or believe',60),('Public action','what others can observe',320),('Social evidence','“they may know more”',580),('Dissent cost','isolation • embarrassment • conflict',840)]
    for title,sub,x in items: b.box(d,x,220,220,115,title,sub,fill=C['light'] if x<560 else C['sand'],stroke=C['blue'] if x<560 else C['orange'])
    for x1,x2 in [(280,320),(540,580),(800,840)]: b.arrow(d,x1,277,x2,277)
    b.arrow(d,1060,335,170,430,stroke=C['red']); b.arrow(d,170,430,170,335,stroke=C['red'])
    b.box(d,380,455,440,100,'Interrupt the cascade','independent estimates • anonymous input • first ally • visible dissent norm',fill='#edf4ed',stroke=C['green'])
    _finish_figure(d,p,'social-pathways',figs,'A social cascade forms when public actions become evidence and raise the cost of dissent; independent elicitation can interrupt it.','Cycle from private signal to public action, social evidence, and dissent cost, with an intervention box for independent judgments and allies.')

    # Ch. 24
    p = figdir / 'influence-signal-audit.svg'; d = b.new_svg(p, title='Influence signal audit', desc='A trigger is evaluated by whether it tracks reality, whether material facts are visible, and whether refusal remains meaningful. The outcome distinguishes informative influence from manipulation.')
    b.txt(d,600,48,'A four-question audit for influence triggers',34,'bold')
    b.box(d,60,235,200,110,'Trigger detected','authority • scarcity • liking • reciprocity',fill=C['sand'],stroke=C['orange']); b.arrow(d,260,290,385,290)
    b.box(d,385,155,225,105,'1. Does the cue track reality?','relevant expertise, demand, obligation?',fill=C['light'],stroke=C['blue']); b.box(d,385,365,225,105,'2. Are material facts visible?','costs, alternatives, uncertainty?',fill=C['light'],stroke=C['blue'])
    b.arrow(d,610,207,760,240); b.arrow(d,610,417,760,360)
    b.box(d,760,220,220,160,'3. Can the person refuse?','time to think • no hidden penalty • reversible exit',fill=C['light'],stroke=C['blue']); b.arrow(d,980,300,1070,220,stroke=C['green']); b.arrow(d,980,300,1070,430,stroke=C['red'])
    b.box(d,1030,145,150,95,'Legitimate','informative + agency-preserving',fill='#edf4ed',stroke=C['green']); b.box(d,1030,405,150,95,'Manipulative','counterfeit cue + obscured exit',fill='#f9e7e7',stroke=C['red'])
    b.txt(d,600,590,'Ethical influence remains defensible when its mechanism is made explicit.',22,fill=C['gray'])
    _finish_figure(d,p,'influence-signal-audit',figs,'Influence is more legitimate when cues track reality, material facts remain visible, and refusal remains meaningful.','Flowchart auditing an influence trigger for reality, visible facts, and ability to refuse, ending in legitimate or manipulative influence.')

    # Ch. 27
    p = figdir / 'story-evidence-braid.svg'; d = b.new_svg(p, title='Story-evidence braid', desc='Story supplies character, stakes, causal simulation, and action readiness; evidence supplies prevalence, comparison, mechanism, uncertainty, and limits. The strands converge on informed judgment.')
    b.txt(d,600,48,'Story creates meaning; evidence creates proportion',34,'bold')
    b.txt(d,115,150,'STORY STRAND',22,'bold',anchor='start',fill=C['orange']); b.txt(d,115,420,'EVIDENCE STRAND',22,'bold',anchor='start',fill=C['blue'])
    story=[('character',200),('stakes',400),('conflict + change',600),('action',800)]
    evidence=[('base rate',200),('comparison',400),('mechanism',600),('uncertainty',800)]
    for lab,x in story: b.box(d,x,115,160,80,lab,'',fill=C['sand'],stroke=C['orange'])
    for lab,x in evidence: b.box(d,x,385,160,80,lab,'',fill=C['light'],stroke=C['blue'])
    for i in range(3):
        b.arrow(d,story[i][1]+160,155,story[i+1][1],155,stroke=C['orange'],width=3)
        b.arrow(d,evidence[i][1]+160,425,evidence[i+1][1],425,stroke=C['blue'],width=3)
    # crossing strands
    b.arrow(d,480,195,600,385,stroke=C['teal'],width=3); b.arrow(d,480,385,600,195,stroke=C['teal'],width=3)
    b.arrow(d,960,155,1030,265,stroke=C['orange']); b.arrow(d,960,425,1030,315,stroke=C['blue'])
    b.box(d,1000,235,170,115,'Informed judgment','attention + scale + agency',fill='#edf4ed',stroke=C['green'])
    b.txt(d,600,575,'Anecdote without evidence distorts scale; evidence without lived meaning may never guide action.',21,fill=C['gray'])
    _finish_figure(d,p,'story-evidence-braid',figs,'An ethical persuasive story braids human meaning with base rates, mechanisms, comparisons, and uncertainty.','Two horizontal strands, story and evidence, cross and converge on informed judgment.')

    # Ch. 29
    p = figdir / 'conversation-repair.svg'; d = b.new_svg(p, title='Conversation and repair sequence', desc='An event is interpreted through a private story, producing feeling and need. Perspective-getting and grounding create shared meaning and a repair action.')
    b.txt(d,600,48,'Repair begins when interpretation becomes a hypothesis',34,'bold')
    items=[('Event','what happened',45),('Private story','what I think it meant',270),('Feeling + need','why it matters',495),('Perspective-getting','ask • listen • verify',720),('Shared meaning + repair','apology • boundary • next action',945)]
    for title,sub,x in items: b.box(d,x,230,190,125,title,sub,fill=C['light'] if x<700 else C['sand'],stroke=C['blue'] if x<700 else C['orange'])
    for x1,x2 in [(235,270),(460,495),(685,720),(910,945)]: b.arrow(d,x1,292,x2,292)
    b.box(d,420,455,360,95,'Layered listening','WHAT • HOW • WHY • WHO • WHEN • ACTION',fill='#edf4ed',stroke=C['green']); b.arrow(d,600,455,815,355,stroke=C['green'])
    b.txt(d,600,590,'Connection improves when people stop treating inferred minds as observed facts.',21,fill=C['gray'])
    _finish_figure(d,p,'conversation-repair',figs,'Perspective-getting turns a private interpretation into shared meaning and a repairable next action.','Five-step sequence from event and private story through feeling, perspective-getting, and shared repair.')

    # Ch. 32
    p = figdir / 'concession-pattern.svg'; d = b.new_svg(p, title='Concession pattern', desc='A disciplined concession pattern moves in diminishing, conditional steps. Equal or unilateral concessions signal room to continue and give away information about limits.')
    b.txt(d,600,48,'Concessions communicate as much as offers',34,'bold')
    vals=[('Opening',100,120),('Move 1',92,360),('Move 2',88,600),('Move 3',86,840)]
    y=280
    for name,val,x in vals:
        b.box(d,x,y-55,170,110,name,f'offer index {val}',fill=C['light'] if x<600 else C['sand'],stroke=C['blue'] if x<600 else C['orange'])
    for (n1,v1,x1),(n2,v2,x2) in zip(vals,vals[1:]):
        b.arrow(d,x1+170,y,x2,y,stroke=C['teal']); b.txt(d,(x1+x2+170)/2,y-25,f'−{v1-v2}',20,'bold',fill=C['teal'])
    b.box(d,385,440,430,105,'Each move should be conditional','“If you can move on X, I can move on Y.”',fill='#edf4ed',stroke=C['green'])
    b.txt(d,600,590,'Shrinking steps signal a limit. Repeated equal concessions invite the other side to wait for more.',21,fill=C['gray'])
    _finish_figure(d,p,'concession-pattern',figs,'A disciplined concession pattern uses diminishing, reciprocal, and conditional moves.','Sequence of four offers with shrinking concessions of eight, four, and two units, plus a conditional-move rule.')

    # Ch. 34
    p = figdir / 'agreement-design.svg'; d = b.new_svg(p, title='Advanced agreement design', desc='MESOs reveal priorities, contingent contracts manage belief differences, post-settlement settlements improve packages, and governance supports implementation.')
    b.txt(d,600,48,'Better agreements solve more than the bargaining moment',34,'bold')
    d.add(d.circle(center=(600,320),r=105,fill=C['navy'])); b.txt(d,600,310,'Better',29,'bold',fill='white'); b.txt(d,600,348,'agreement',29,'bold',fill='white')
    nodes=[('MESOs','reveal priorities without asking for one answer',95,140,C['light'],C['blue']),('Contingent contracts','bet on different forecasts',825,140,C['sand'],C['orange']),('Post-settlement search','improve without risking the signed deal',95,430,'#edf4ed',C['green']),('Governance','monitor • adapt • repair • learn',825,430,'#f5ebf5','#795a8a')]
    for title,sub,x,y,fill,stroke in nodes:
        b.box(d,x,y,280,110,title,sub,fill=fill,stroke=stroke); b.arrow(d,x+140,y+55,600,320,stroke=stroke,width=3)
    b.txt(d,600,605,'Agreement quality includes allocation, information, implementation, and the capacity to adapt.',21,fill=C['gray'])
    _finish_figure(d,p,'agreement-design',figs,'Advanced agreement design uses MESOs, contingent terms, post-settlement improvement, and implementation governance.','Four agreement-design tools point toward a central better-agreement node.')

    # Update placements: one original conceptual illustration per chapter.
    b.FIGURE_PLACEMENT.update({
        3: ('Information has value only when it can change action', 'option-information'),
        10: ('Availability: what comes to mind feels common', 'affect-availability'),
        11: ('The representative story', 'prototype-probability'),
        13: ('Confirmation and myside bias', 'belief-protection-loop'),
        14: ('Halo and horn effects', 'anchor-decoy'),
        16: ('Priming, framing, fluency, and architecture', 'priming-pathway'),
        17: ('Repetition becomes liking', 'fluency-pathway'),
        20: ('Craving as sensation and prediction', 'wanting-liking'),
        22: ('Copying and cumulative culture', 'social-learning-culture'),
        23: ('Social proof and cascades', 'social-pathways'),
        24: ('Influence triggers: a diagnostic map', 'influence-signal-audit'),
        27: ('Practical story tools', 'story-evidence-braid'),
        29: ('Listen for the layer beneath the words', 'conversation-repair'),
        32: ('Concessions and pressure', 'concession-pattern'),
        34: ('Designing across disagreement', 'agreement-design'),
    })

    # Stable chapter-based figure numbering.
    for chapter_num, (_, key) in sorted(b.FIGURE_PLACEMENT.items()):
        if key in figs:
            cap = re.sub(r'^Figure\s+\d+(?:\.\d+)?\.\s*', '', figs[key]['caption'])
            figs[key]['caption'] = f'Figure {chapter_num}.1. {cap}'
    return figs

b.generate_figures = generate_figures

# ---------------- Appendix B correction ----------------

_orig_appendix_to_md = b.appendix_to_md

def appendix_to_md(title: str, blocks):
    if 'Index of Major Course Examples' not in title:
        return _orig_appendix_to_md(title, blocks)
    rows = [
        ['Example', 'Main concept', 'Chapter(s)'],
        ['Two job offers: consulting or sustainability start-up', 'Prediction, valuation, opportunity cost, and multi-objective choice', '1–3, 7'],
        ['Bat-and-ball problem', 'Cognitive reflection and intuitive substitution', '4'],
        ['Invisible gorilla and radiologist gorilla', 'Inattentional blindness and expert search templates', '5'],
        ['Door-study change blindness', 'The illusion of complete visual representation', '5'],
        ['Bees’ ultraviolet flower patterns and animal Umwelt', 'Species-specific perception and epistemic humility', '5'],
        ['Checker shadow, Kanizsa triangle, Thatcher illusion, and rubber hand', 'Perception as inference', '6'],
        ['Subliminal reward cue and handgrip effort', 'Motivation with limited awareness', '7'],
        ['Wine price, energy-drink discount, placebo, and nocebo', 'Expectation changes experience and performance', '8'],
        ['Ecological shortcuts and trigger features', 'Heuristics as adaptive tools', '9'],
        ['Plane crashes, vivid risks, and recent performance', 'Availability and affect', '10'],
        ['Linda problem, prototypes, faces, and elections', 'Representativeness and conjunction error', '11'],
        ['Medical-test frequencies, gambler’s fallacy, hot hand, and regression', 'Base rates, conditional probability, randomness, and calibration', '12'],
        ['Wason task, death-penalty evidence, Barnum effect, and overconfidence', 'Confirmation, self-serving judgment, and calibration', '13'],
        ['Wheel-of-fortune anchor, halo, decoy, sunk cost, and escalation', 'Contextual comparison and commitment', '14'],
        ['Survival versus mortality, lean versus fat, and Asian disease', 'Framing and reference dependence', '15'],
        ['Semantic, affective, identity, and goal priming', 'Associative accessibility and its boundary conditions', '16'],
        ['Mere exposure, illusory truth, rhymes, and easy names', 'Fluency, familiarity, liking, and belief', '17'],
        ['Stockings position effect and choice blindness', 'Reasons versus causes and rationalization', '18'],
        ['Phone checking, procrastination, defensiveness, and habit loops', 'Context-cued automaticity', '19'],
        ['Wanting versus liking, craving waves, and addiction', 'Incentive salience and self-control', '20'],
        ['Implementation intentions, WOOP, B=MAP, defaults, and friction', 'Behavior design', '21'],
        ['Overimitation, chameleon effect, and attribution flip', 'Social learning, mimicry, and causal explanation', '22'],
        ['Sherif, Asch, towel reuse, energy feedback, and cultural markets', 'Conformity, norms, social proof, and cascades', '23'],
        ['Milgram, bystanders, copier “because,” reciprocity, and scarcity', 'Authority, responsibility, and influence triggers', '24'],
        ['Ethos–pathos–logos, elaboration likelihood, fear, and reactance', 'Persuasion and resistance', '25'],
        ['Transportation, identification, identifiable victim, and ABT', 'Why narrative persuades', '26'],
        ['STORY, evidence ladder, story–evidence braid, and worked transformations', 'Evidence-aligned storytelling', '27'],
        ['Email tone, illusion of transparency, perspective-getting, and shared reality', 'Communication as joint inference', '28'],
        ['Deep questions, liking gap, appreciation, help, support, and apology', 'Conversation and repair', '29'],
        ['Positions, interests, BATNA, and the negotiator’s dilemma', 'Negotiation architecture', '30'],
        ['Used-car ZOPA and salary preparation', 'Reservation values, targets, and bargaining power', '31'],
        ['First offers, re-anchoring, concessions, even split, and deadlines', 'Distributive tactics', '32'],
        ['Orange story, Camp David, priority mapping, and logrolling', 'Integrative trade-offs', '33'],
        ['MESOs, contingent contracts, post-settlement search, and supplier terms', 'Advanced agreement design', '34'],
        ['Decision journal, independent estimates, premortem, and after-action review', 'Decision hygiene', '35'],
    ]
    lines = ['---', f'title: "{title}"', 'appendix: true', '---\n', f'# {title}\n',
             'Use this index to revisit the cases, demonstrations, and worked examples most likely to appear in class discussion and application questions.\n',
             b.table_to_md(b.TBlock(rows)) + '\n']
    return '\n'.join(lines)

b.appendix_to_md = appendix_to_md

# ---------------- Student-facing static site ----------------

SITE_TEMPLATE = '''<!doctype html>
<html lang="en" data-theme="light">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#17324d">
<title>{{ page_title }} · Decision, Persuasion, and Negotiation</title>
<meta name="description" content="{{ description|e }}">
<link rel="stylesheet" href="{{ root }}assets/style.css">
<script defer src="{{ root }}assets/site.js"></script>
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
<header class="topbar"><button class="menu-button" aria-label="Open book navigation" aria-expanded="false">☰</button><a class="brand" href="{{ root }}index.html">Decision, Persuasion, and Negotiation</a><div class="top-actions"><button id="search-button" aria-label="Search book">Search</button><button id="theme-button" aria-label="Toggle dark mode">◐</button></div></header>
<div class="reading-progress" aria-hidden="true"><span></span></div>
<button class="sidebar-backdrop" aria-label="Close navigation"></button>
<div class="layout">
<aside class="sidebar" aria-label="Book navigation"><div class="sidebar-inner">{{ nav|safe }}</div></aside>
<main id="main" class="content">{{ content|safe }}<nav class="page-nav" aria-label="Previous and next pages">{% if prev %}<a class="prev" href="{{ root }}{{ prev.href }}">← {{ prev.label }}</a>{% endif %}{% if next %}<a class="next" href="{{ root }}{{ next.href }}">{{ next.label }} →</a>{% endif %}</nav></main>
<aside class="on-page" aria-label="On this page">{{ toc|safe }}</aside>
</div>
<dialog id="search-dialog"><form method="dialog"><button class="close-search">Close</button></form><h2>Search the textbook</h2><input id="search-input" type="search" placeholder="Search concepts, cases, and tools" autocomplete="off"><div id="search-results" aria-live="polite"></div></dialog>
<footer><p>© 2026 Huanren Warren Zhang · Course textbook for Decision, Persuasion, and Negotiation · <a href="{{ root }}start-here.html">Start here</a> · <a href="{{ root }}references.html">References</a></p></footer>
</body></html>'''

EXTRA_CSS = r'''
.table-wrapper{width:100%;overflow-x:auto;margin:1.4rem 0;-webkit-overflow-scrolling:touch}.table-wrapper table{display:table;min-width:100%;margin:0}
:focus-visible{outline:3px solid var(--accent2);outline-offset:3px}.reading-progress{position:fixed;z-index:25;top:57px;left:0;right:0;height:3px;background:transparent}.reading-progress span{display:block;height:100%;width:0;background:var(--accent2)}.sidebar-backdrop{display:none;position:fixed;inset:58px 0 0 0;z-index:25;border:0;border-radius:0;background:rgba(0,0,0,.35);padding:0}.nav-start,.part-overview-link{display:block;text-decoration:none}.nav-start{font-weight:850;color:var(--accent);margin:.25rem 0 1.2rem}.part-overview-link{font-size:.82rem;font-weight:750;color:var(--accent);padding:.25rem 0 .35rem .65rem}.part-nav .part-overview-link{border-left:2px solid transparent}.chapter-kicker,.eyebrow{font-size:.82rem;letter-spacing:.08em;text-transform:uppercase;color:var(--accent);font-weight:850}.subtitle{font-family:Georgia,serif;font-size:1.15rem;color:var(--muted);margin-top:.25rem}.reading-time{color:var(--muted);font-size:.88rem}.flow-figure{margin:2rem 0}.flow-figure img{width:100%;border:1px solid var(--line);border-radius:14px;background:white}.part-overview{border:1px solid var(--line);border-radius:15px;background:var(--panel);padding:1.2rem 1.4rem;margin:1.5rem 0}.question-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:.8rem}.question-card{border:1px solid var(--line);border-radius:10px;background:var(--paper);padding:.9rem}.stats{display:flex;flex-wrap:wrap;gap:.75rem;margin:1.1rem 0}.stat{border:1px solid var(--line);border-radius:10px;background:var(--panel);padding:.65rem .85rem}.stat strong{display:block;font-size:1.25rem}.home-actions a.primary{background:var(--accent);color:white;border-color:var(--accent)}.chapter-card .minutes{display:block;margin-top:.45rem;color:var(--muted);font-size:.82rem}.complete-book-note{border:1px dashed var(--line);padding:1rem;border-radius:10px;color:var(--muted)}.content>h1+em,.content>p>em:first-child{color:var(--muted)}.content ul{padding-left:1.25rem}.content li{margin:.35rem 0}.toc-h3{padding-left:.7rem!important;font-size:.84rem}.on-page nav:before{content:'On this page';display:block;font-weight:800;margin-bottom:.5rem;color:var(--ink)}summary{list-style-position:outside}.reference{overflow-wrap:anywhere}.book-figure img{max-height:620px;object-fit:contain}.callout.scientific-caution,.callout.evidence-and-boundary-conditions{border-left-color:var(--accent2)}.callout.activity{border-left-color:var(--teal,#2b7a78)}
@media(max-width:780px){body.nav-open{overflow:hidden}.sidebar-backdrop.show{display:block}.sidebar{height:calc(100vh - 58px);overflow:auto}.topbar{padding:.35rem .6rem}.brand{max-width:58vw;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.page-nav{flex-direction:column}.next{text-align:left;margin-left:0}.hero .download-row{display:grid}.hero .download-row a{text-align:center}.stats{display:grid;grid-template-columns:1fr 1fr}.on-page{display:none}}
@media print{.reading-progress,.sidebar-backdrop{display:none!important}.content{font-size:11pt}.hero{border:0;padding:0}.book-figure img{max-height:none}}
'''

SITE_JS = r'''
const root=document.documentElement;
const saved=localStorage.getItem('dpn-theme');if(saved)root.dataset.theme=saved;
document.getElementById('theme-button')?.addEventListener('click',()=>{root.dataset.theme=root.dataset.theme==='dark'?'light':'dark';localStorage.setItem('dpn-theme',root.dataset.theme)});
const sidebar=document.querySelector('.sidebar'), menu=document.querySelector('.menu-button'), backdrop=document.querySelector('.sidebar-backdrop');
function setNav(open){sidebar?.classList.toggle('open',open);backdrop?.classList.toggle('show',open);document.body.classList.toggle('nav-open',open);menu?.setAttribute('aria-expanded',String(open));}
menu?.addEventListener('click',()=>setNav(!sidebar.classList.contains('open')));backdrop?.addEventListener('click',()=>setNav(false));
sidebar?.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>setNav(false)));document.addEventListener('keydown',e=>{if(e.key==='Escape')setNav(false)});
const progress=document.querySelector('.reading-progress span');function updateProgress(){const max=document.documentElement.scrollHeight-innerHeight;progress.style.width=(max>0?Math.min(100,scrollY/max*100):0)+'%'}addEventListener('scroll',updateProgress,{passive:true});updateProgress();
const dlg=document.getElementById('search-dialog'),btn=document.getElementById('search-button'),inp=document.getElementById('search-input'),out=document.getElementById('search-results');
btn?.addEventListener('click',()=>{dlg.showModal();setTimeout(()=>inp.focus(),60)});
let idx=[];fetch((document.body.dataset.root||'')+'search-index.json').then(r=>r.json()).then(x=>idx=x).catch(()=>{out.innerHTML='<p>Search index unavailable.</p>'});
function esc(s){return s.replace(/[&<>"']/g,m=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[m]))}
inp?.addEventListener('input',()=>{let q=inp.value.trim().toLowerCase();if(q.length<2){out.innerHTML='';return}let terms=q.split(/\s+/);let hits=idx.map(x=>{let title=x.title.toLowerCase(),heads=x.headings.toLowerCase(),hay=(x.title+' '+x.headings+' '+x.text).toLowerCase();let score=terms.reduce((s,t)=>s+(title.includes(t)?7:0)+(heads.includes(t)?4:0)+(hay.split(t).length-1),0);return {...x,score}}).filter(x=>x.score>0).sort((a,b)=>b.score-a.score).slice(0,30);out.innerHTML=hits.map(x=>`<div class="search-hit"><a href="${document.body.dataset.root||''}${x.href}">${esc(x.title)}</a><div>${esc(x.excerpt)}</div></div>`).join('')||'<p>No results.</p>'});
'''


def _reading_minutes_from_md(text: str) -> int:
    body = re.sub(r'^---\n.*?\n---\n', '', text, flags=re.S)
    body = body.split('## References cited in this chapter')[0]
    body = re.sub(r'<[^>]+>', ' ', body)
    words = len(re.findall(r"\b[\w’'-]+\b", body))
    return max(1, round(words / 220))


def _nav_html(chapters, appendices, active='', prefix=''):
    out = [f'<a class="nav-start{" active" if active=="start-here" else ""}" href="{prefix}start-here.html"' + (' aria-current="page"' if active=='start-here' else '') + '>Start here</a>']
    for part,(title,_) in b.PARTS.items():
        open_attr = ' open' if active == f'part-{part}' or any(ch.slug == active and ch.part == part for ch in chapters) else ''
        out.append(f'<details class="part-nav"{open_attr}><summary>Part {part}. {b.html.escape(title)}</summary>')
        cls = ' active' if active == f'part-{part}' else ''
        aria = ' aria-current="page"' if cls else ''
        out.append(f'<a class="part-overview-link{cls}"{aria} href="{prefix}part-{part}.html">Part overview</a>')
        for ch in [x for x in chapters if x.part == part]:
            cls = ' class="active"' if ch.slug == active else ''
            aria = ' aria-current="page"' if ch.slug == active else ''
            out.append(f'<a{cls}{aria} href="{prefix}chapters/{ch.slug}.html">{ch.num}. {b.html.escape(ch.title)}</a>')
        out.append('</details>')
    out.append('<details class="part-nav" open><summary>Appendices and resources</summary>')
    for slug,title in appendices:
        cls=' class="active"' if active==slug else ''; aria=' aria-current="page"' if active==slug else ''
        out.append(f'<a{cls}{aria} href="{prefix}appendices/{slug}.html">{b.html.escape(title)}</a>')
    for slug,label,href in [('references','References','references.html'),('complete-book','Complete book (single page)','complete-book.html'),('about','About and editorial notes','about.html')]:
        cls=' class="active"' if active==slug else ''; aria=' aria-current="page"' if active==slug else ''
        out.append(f'<a{cls}{aria} href="{prefix}{href}">{label}</a>')
    out.append('</details>')
    return ''.join(out)


def _start_here_md(chapters, figure_count, table_count, reference_count):
    rows = [['Part', 'Central movement', 'What students should be able to do']]
    for p,(title,desc) in b.PARTS.items():
        ability = PART_GUIDES[p]['questions'][0]
        rows.append([f'{p}. {title}', desc, ability])
    table = b.table_to_md(b.TBlock(rows))
    return f'''---
title: "Start Here"
---

# Start Here

*How to use this textbook as a cumulative course rather than a catalogue of effects*

A visible decision is usually the end of a hidden process. Attention has selected evidence, a predictive model has interpreted it, valuation has made some outcomes matter, social cues have changed what feels normal, and previous choices may already have become habits. The book therefore begins upstream and moves outward—from one mind, to other minds, to joint decisions and decision systems.

<div class="stats"><div class="stat"><strong>{len(chapters)}</strong>short chapters</div><div class="stat"><strong>{figure_count}</strong>accessible illustrations</div><div class="stat"><strong>{table_count}</strong>substantive tables</div><div class="stat"><strong>{reference_count}</strong>cited works</div></div>

<figure class="flow-figure"><img src="figures/book-flow.svg" alt="Seven-part reading map from the architecture of choice to better decision systems." /><figcaption>Reading map. Each part supplies concepts needed by the next.</figcaption></figure>

## The organizing logic

{table}

## How to read a chapter

1. **Begin with the opening case.** Make a prediction before reading the explanation.
2. **Use the figure as a model, not decoration.** Explain every arrow or distinction in your own words.
3. **Interrogate the evidence.** Distinguish an established pattern from a context-sensitive or contested claim.
4. **Work the table or tool.** Apply it to a decision from work, study, public life, or negotiation.
5. **Finish with Experience–Explain–Apply.** Use no more than 120 words: one concrete experience, one or two concepts, and one improvement or testable prediction.

## Scientific and citation policy

The text uses APA-style author–date citations. Every chapter ends with only the works cited in that chapter; the master bibliography is the deduplicated union of those lists. Effects with important boundary conditions—such as social priming, stereotype-related performance effects, watched-eyes cues, and some mindset interventions—are explicitly qualified rather than presented as universal laws.

## Suggested routes

- **Full course:** read in order. The sequence is cumulative.
- **Decision unit:** Chapters 1–21.
- **Influence and communication unit:** Chapters 22–29.
- **Negotiation unit:** Chapters 30–35, with Chapters 1–3, 7, 13–15, 23–25, and 28–29 as foundations.
- **Exam review:** use Appendix B to locate major examples and Appendix A to rehearse the portable tools.
'''


def _part_md(part, chapters):
    title, desc = b.PARTS[part]; guide = PART_GUIDES[part]
    q = ''.join(f'<div class="question-card">{b.html.escape(x)}</div>' for x in guide['questions'])
    cards = []
    for ch in [x for x in chapters if x.part == part]:
        md = (b.OUT/'chapters'/f'{ch.slug}.md').read_text(encoding='utf-8')
        mins = _reading_minutes_from_md(md)
        cards.append(f'<a class="chapter-card" href="chapters/{ch.slug}.html"><small>Chapter {ch.num}</small><strong>{b.html.escape(ch.title)}</strong><span>{b.html.escape(ch.subtitle)}</span><span class="minutes">About {mins} min</span></a>')
    return f'''---
title: "Part {part}. {title}"
---

# Part {part}. {title}

*{desc}*

<div class="part-overview"><strong>Why this part comes here</strong><p>{guide['why']}</p></div>

## Guiding questions

<div class="question-grid">{q}</div>

## Chapters

<div class="chapter-card-grid">{''.join(cards)}</div>

## Bridge to the next part

{guide['bridge']}
'''


def build_site(chapters, appendices, all_refs, figs):
    docs=b.OUT/'docs'; assets=docs/'assets'; chdir=docs/'chapters'; apdir=docs/'appendices'; fdir=docs/'figures'; down=docs/'downloads'; parts_dir=b.OUT/'parts'
    for p in [assets,chdir,apdir,fdir,down,parts_dir]: p.mkdir(parents=True,exist_ok=True)
    shutil.copytree(b.OUT/'figures',fdir,dirs_exist_ok=True)
    (assets/'style.css').write_text(b.CSS + EXTRA_CSS,encoding='utf-8')
    (assets/'site.js').write_text(SITE_JS,encoding='utf-8')
    (docs/'.nojekyll').write_text('',encoding='utf-8')
    md=MarkdownIt('commonmark',{'html':True,'linkify':True}).enable('table')
    env=Environment(loader=BaseLoader(),autoescape=select_autoescape(['html'])); tpl=env.from_string(SITE_TEMPLATE)
    appmeta=[(b.slugify(t),t) for t in appendices]

    used_figures = len(b.FIGURE_PLACEMENT) + 1
    table_count = sum(1 for ch in chapters for block in ch.blocks if isinstance(block,b.TBlock) and max((len(r) for r in block.rows),default=0)>1)
    start_md=_start_here_md(chapters,used_figures,table_count,len(all_refs)); (b.OUT/'start-here.md').write_text(start_md,encoding='utf-8')
    for part in b.PARTS:
        pm=_part_md(part,chapters); (parts_dir/f'part-{part}.md').write_text(pm,encoding='utf-8')

    # Reading order includes part overviews, which makes transitions explicit online.
    pages=[{'href':'start-here.html','label':'Start here','kind':'start'}]
    for part in b.PARTS:
        pages.append({'href':f'part-{part}.html','label':f'Part {part}. {b.PARTS[part][0]}','kind':'part','part':part})
        for ch in [x for x in chapters if x.part==part]: pages.append({'href':f'chapters/{ch.slug}.html','label':f'Chapter {ch.num}. {ch.title}','kind':'chapter','ch':ch})
    for title in appendices: pages.append({'href':f'appendices/{b.slugify(title)}.html','label':title,'kind':'appendix','title':title})
    pages += [{'href':'references.html','label':'References','kind':'references'},{'href':'about.html','label':'About and editorial notes','kind':'about'}]
    index_by_href={p['href']:i for i,p in enumerate(pages)}
    search=[]

    def render_page(href,title,description,source_md,root,active,search_it=True,add_meta=''):
        content=b.render_markdown(md,source_md); soup=BeautifulSoup(content,'html.parser')
        if add_meta:
            h1=soup.find('h1')
            if h1:
                tag=soup.new_tag('p'); tag['class']='chapter-kicker'; tag.string=add_meta; h1.insert_before(tag)
                sub=h1.find_next_sibling('p')
                if sub and sub.find('em'): sub['class']='subtitle'
        toc=b.headings_toc(soup); idx=index_by_href.get(href); prev=pages[idx-1] if idx is not None and idx>0 else None; nxt=pages[idx+1] if idx is not None and idx+1<len(pages) else None
        hp=tpl.render(page_title=title,description=description,root=root,content=str(soup),toc=toc,nav=_nav_html(chapters,appmeta,active,prefix=root),prev=prev,next=nxt).replace('<body>','<body data-root="'+root+'">')
        target=docs/href; target.parent.mkdir(parents=True,exist_ok=True); target.write_text(hp,encoding='utf-8')
        if search_it:
            text=soup.get_text(' ',strip=True); heads=' '.join(h.get_text(' ',strip=True) for h in soup.find_all(['h2','h3']))
            search.append({'title':title,'headings':heads,'text':text,'excerpt':text[:260]+'…','href':href})

    render_page('start-here.html','Start Here','How to use the textbook and understand its cumulative structure.',start_md,'','start-here')
    for part in b.PARTS:
        src=(parts_dir/f'part-{part}.md').read_text(encoding='utf-8'); render_page(f'part-{part}.html',f'Part {part}. {b.PARTS[part][0]}',b.PARTS[part][1],src,'',f'part-{part}')

    for ch in chapters:
        src=(b.OUT/'chapters'/f'{ch.slug}.md').read_text(encoding='utf-8'); mins=_reading_minutes_from_md(src)
        render_page(f'chapters/{ch.slug}.html',f'Chapter {ch.num}. {ch.title}',ch.subtitle,src,'../',ch.slug,add_meta=f'Part {ch.part} · About {mins} min read')

    for title,blocks in appendices.items():
        slug=b.slugify(title); src=(b.OUT/'appendices'/f'{slug}.md').read_text(encoding='utf-8')
        render_page(f'appendices/{slug}.html',title,'Portable tools and an index of major course examples.',src,'../',slug)

    # References.
    refcontent='<h1>References</h1><p>This master bibliography contains only works cited in the textbook. Each chapter also provides its own cited-reference list.</p>'+''.join(f'<div class="reference">{b.html.escape(r)}</div>' for r in all_refs)
    soup=BeautifulSoup(refcontent,'html.parser'); toc=b.headings_toc(soup); href='references.html'; idx=index_by_href[href]
    hp=tpl.render(page_title='References',description='Works cited in the textbook.',root='',content=str(soup),toc=toc,nav=_nav_html(chapters,appmeta,'references'),prev=pages[idx-1],next=pages[idx+1]).replace('<body>','<body data-root="">')
    (docs/href).write_text(hp,encoding='utf-8'); search.append({'title':'References','headings':'','text':soup.get_text(' ',strip=True),'excerpt':'Complete bibliography containing only works cited in the textbook.','href':href})

    # About/editorial report.
    report=(b.OUT/'STRUCTURE_AND_EDITORIAL_REPORT.md').read_text(encoding='utf-8'); href='about.html'; idx=index_by_href[href]
    content=b.render_markdown(md,report); soup=BeautifulSoup(content,'html.parser'); toc=b.headings_toc(soup)
    hp=tpl.render(page_title='About and editorial notes',description='Organization, visual system, reference policy, and audit limitations.',root='',content=str(soup),toc=toc,nav=_nav_html(chapters,appmeta,'about'),prev=pages[idx-1],next=None).replace('<body>','<body data-root="">')
    (docs/href).write_text(hp,encoding='utf-8')

    # Homepage.
    cards=[]
    for part,(pt,desc) in b.PARTS.items():
        cards.append(f'<section class="part-intro"><p class="eyebrow">Part {part}</p><h2><a href="part-{part}.html">{b.html.escape(pt)}</a></h2><p>{b.html.escape(desc)}</p><div class="chapter-card-grid">')
        for ch in [x for x in chapters if x.part==part]:
            src=(b.OUT/'chapters'/f'{ch.slug}.md').read_text(encoding='utf-8'); mins=_reading_minutes_from_md(src)
            cards.append(f'<a class="chapter-card" href="chapters/{ch.slug}.html"><small>Chapter {ch.num}</small><strong>{b.html.escape(ch.title)}</strong><span>{b.html.escape(ch.subtitle)}</span><span class="minutes">About {mins} min</span></a>')
        cards.append('</div></section>')
    home=f'''<section class="hero"><p class="eyebrow">Student textbook · revised GitHub edition · 2026</p><h1>Decision, Persuasion, and Negotiation</h1><p>How minds choose, influence, connect, and bargain. The book moves from the hidden architecture of a choice to judgment under uncertainty, habits, social influence, persuasion, communication, negotiation, and better decision systems.</p><div class="download-row home-actions"><a class="primary" href="start-here.html">Start reading</a><a href="downloads/{b.EPUB.name}">Download EPUB</a><a href="complete-book.html">Open complete book</a><a href="references.html">Browse references</a></div></section><figure class="flow-figure"><img src="figures/book-flow.svg" alt="Seven-part reading map from the architecture of choice to better decision systems." /><figcaption>The cumulative flow of the textbook.</figcaption></figure>{''.join(cards)}'''
    hp=tpl.render(page_title='Home',description='Online textbook for Decision, Persuasion, and Negotiation.',root='',content=home,toc='',nav=_nav_html(chapters,appmeta),prev=None,next=pages[0]).replace('<body>','<body data-root="">')
    (docs/'index.html').write_text(hp,encoding='utf-8')

    # Single-page print/offline edition. Chapter-specific bibliographies are omitted here; the master list appears once at the end.
    whole=['<section class="hero"><p class="eyebrow">Complete single-page edition</p><h1>Decision, Persuasion, and Negotiation</h1><p>Use your browser’s print command to create a personal PDF. For normal study, the chapter-by-chapter edition is faster and easier to navigate.</p></section>']
    for part,(pt,pd) in b.PARTS.items():
        whole.append(f'<section class="part-intro"><p class="eyebrow">Part {part}</p><h1>{b.html.escape(pt)}</h1><p>{b.html.escape(pd)}</p></section>')
        for ch in [x for x in chapters if x.part==part]:
            src=b.blocks_to_md(ch,figs,include_refs=False,image_prefix='figures/')
            whole.append(b.render_markdown(md,src))
    whole.append('<h1>References</h1>'+''.join(f'<div class="reference">{b.html.escape(r)}</div>' for r in all_refs))
    hp=tpl.render(page_title='Complete book',description='Complete print-friendly single-page edition.',root='',content=''.join(whole),toc='',nav=_nav_html(chapters,appmeta,'complete-book'),prev=None,next=None).replace('<body>','<body class="complete-book" data-root="">')
    (docs/'complete-book.html').write_text(hp,encoding='utf-8')

    # Accessible fallback page.
    fallback = tpl.render(
        page_title='Page not found',
        description='The requested textbook page could not be found.',
        root='',
        content='<h1>Page not found</h1><p>The page may have moved. Return to the <a href="index.html">textbook home page</a> or use search.</p>',
        toc='',
        nav=_nav_html(chapters,appmeta),
        prev=None,
        next=None,
    ).replace('<body>','<body data-root="">')
    (docs/'404.html').write_text(fallback,encoding='utf-8')

    # Wrap every table in a responsive region, including the complete-book page.
    for html_path in docs.rglob('*.html'):
        text = html_path.read_text(encoding='utf-8')
        if '<table' not in text:
            continue
        page_soup = BeautifulSoup(text, 'html.parser')
        changed = False
        for table in page_soup.find_all('table'):
            parent = table.parent
            if parent and 'table-wrapper' in (parent.get('class') or []):
                continue
            wrapper = page_soup.new_tag('div')
            wrapper['class'] = ['table-wrapper']
            wrapper['role'] = 'region'
            wrapper['aria-label'] = 'Scrollable table'
            wrapper['tabindex'] = '0'
            table.wrap(wrapper)
            changed = True
        if changed:
            html_path.write_text(str(page_soup), encoding='utf-8')

    (docs/'search-index.json').write_text(json.dumps(search,ensure_ascii=False),encoding='utf-8')

b.build_site = build_site

# ---------------- Reports and repository guidance ----------------

def write_support_files(chapters, old_refs, all_refs, removed_refs, unresolved):
    b.OUT.mkdir(parents=True,exist_ok=True)
    word_count=0; table_count=0
    for ch in chapters:
        text=' '.join(block.text if isinstance(block,b.PBlock) else ' '.join(sum(block.rows,[])) for block in ch.blocks)
        word_count += len(re.findall(r"\b[\w’'-]+\b",text))
        table_count += sum(1 for block in ch.blocks if isinstance(block,b.TBlock) and max((len(r) for r in block.rows),default=0)>1)
    figure_count=len(b.FIGURE_PLACEMENT)+1

    lines=['# Structure and editorial report','',
    '## Editorial judgment','',
    'The material is strongest when it is read as one expanding decision system rather than as separate units on biases, persuasion, and bargaining. The revised structure therefore follows a causal and pedagogical sequence: hidden choice architecture → judgment under uncertainty → post-choice learning and habit → the social mind → intentional influence and connection → negotiation → repeatable decision systems.','',
    '## Main structural improvements','',
    '1. **A clearer opening architecture.** Rational choice, opportunity cost, fast/slow processing, attention, prediction, valuation, and expectation now form one uninterrupted foundation.','2. **Probability sits next to representativeness.** The seductive story is immediately followed by base rates, conditional probability, randomness, regression, and calibration.','3. **The narrator opens the behavior-over-time part.** Students see how outcomes are explained before studying how repeated loops become habits.','4. **The social material is decompressed.** Social learning and attribution, conformity and norms, and authority and influence triggers are separate chapters.','5. **Persuasion, story, and communication are distinguished.** Persuasion is intentional model updating; story is simulated meaning; communication is joint inference and repair.','6. **Negotiation remains the integrative capstone.** It moves from architecture and preparation to distributive tactics, integrative trades, and agreement governance.','7. **The website adds explicit bridges.** A Start Here page and seven part-overview pages explain why each unit follows the previous one.','',
    '## Revised part structure','']
    for p,(title,desc) in b.PARTS.items():
        lines += [f'### Part {p}. {title}','',desc,'']
        for ch in [x for x in chapters if x.part==p]: lines.append(f'- Chapter {ch.num}. **{ch.title}** — {ch.subtitle}')
    lines += ['', '## Chapter-level flow corrections','',
    '- Added missing subheadings to the long opening of Chapter 5 so inattentional blindness, top-down/bottom-up attention, divided attention, and change blindness can be studied separately.','- Removed the duplicated learning-goal and core-idea blocks in Chapter 23.','- Reorganized Chapter 24 around authority, bystander responsibility, a diagnostic influence map, eight recurring triggers, counterfeit signals, and ethical resistance; the repetitive trigger overview was removed without deleting the detailed evidence.','- Grouped the many short subsections in Chapters 27, 32, and 34 under higher-level headings, preserving all content while producing a readable on-page table of contents.','- Corrected stale cross-references, including the integrative-negotiation reference to Chapter 31 and forward references from Chapters 7, 8, 11, 13, 14, and 16.','- Rebuilt Appendix B so every example points to the revised chapter number.','',
    '## Visual and table system','',
    f'- **{figure_count} accessible illustrations:** one original conceptual diagram for each of the {len(chapters)} chapters, plus a seven-part reading map. SVG is used online and PNG in EPUB.','- Every figure has alternative text, an SVG title and description, and a chapter-based figure number.','- New visuals cover option generation and value of information, affect and availability, resemblance versus probability, belief-protection loops, anchors and decoys, priming, fluency, wanting versus liking, cumulative culture, influence ethics, the story–evidence braid, conversation repair, concession patterns, and advanced agreement design.','- Substantive summary tables were added where they improve comparison or transfer, while existing editable tables were preserved as responsive HTML.','',
    '## Reference policy and audit','',
    f'- Source master bibliography: {len(old_refs)} entries.',f'- Published master bibliography: {len(all_refs)} unique works that are cited in the text.',f'- Removed from the published bibliography because no in-text citation remained: {len(removed_refs)} entries.',f'- Unresolved author–year citation strings: {len(unresolved)}.',f'- Published bibliography entries without a corresponding in-text match: **0** (the master list is generated from chapter citation matches).','- Each chapter ends with only the works cited in that chapter. The global reference page is the deduplicated union of those chapter lists.','',
    '## GitHub and accessibility design','',
    '- The `docs/` directory is prebuilt and can be published directly with GitHub Pages; no build step is required for students to access the book.','- The site includes Start Here and part-overview pages, responsive navigation, full-text search, dark mode, reading progress, previous/next links, mobile controls, print styles, and a complete single-page edition.','- Tables scroll horizontally on small screens. Figures scale without losing text clarity. Keyboard focus, a skip link, semantic headings, alt text, and visible focus styles support accessibility.','- A downloadable EPUB is included in `docs/downloads/`.','',
    '## Scope and audit limitation','',
    'The citation audit guarantees text–bibliography correspondence at the author–year level and removes uncited bibliography entries. It does not claim that an automated matcher can decide whether every source supports every clause at the level of a systematic review. The prose itself retains scientific cautions for context-sensitive, debated, or replication-sensitive findings.','',
    f'Approximate chapter-body word count: **{word_count:,}**. Substantive tables detected: **{table_count}**.']
    (b.OUT/'STRUCTURE_AND_EDITORIAL_REPORT.md').write_text('\n'.join(lines),encoding='utf-8')

    audit={'summary':{'source_reference_entries':len(old_refs),'published_unique_cited_references':len(all_refs),'removed_uncited_entries':len(removed_refs),'unresolved_citations':len(unresolved),'published_orphan_references':0,'chapters':len(chapters),'chapter_figures':len(b.FIGURE_PLACEMENT),'front_matter_figures':1,'substantive_tables':table_count},'chapters':[{'chapter':c.num,'title':c.title,'reference_count':len(c.references),'references':c.references} for c in chapters],'removed_uncited_references':removed_refs,'unresolved_citations':unresolved}
    (b.OUT/'citation-audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2),encoding='utf-8')
    md=['# Citation audit','',f'Published references: **{len(all_refs)}**  ',f'Removed uncited entries: **{len(removed_refs)}**  ',f'Unresolved citations: **{len(unresolved)}**  ','Published orphan references: **0**','', '## Method','', 'Chapter bibliographies are generated by matching author–year citations in chapter bodies to the reference database assembled from the uploaded manuscript and source chapters. The master bibliography is the deduplicated union of those chapter lists. Therefore, an entry cannot appear in the published reference list unless it has a corresponding citation match in the text.','', '## Chapter counts','', '| Chapter | References cited |','|---|---:|']
    for c in chapters: md.append(f'| {c.num}. {c.title} | {len(c.references)} |')
    md += ['','## Removed uncited entries','']+[f'- {x}' for x in removed_refs]
    if unresolved: md += ['','## Unresolved citation strings','']+[f'- {x}' for x in unresolved]
    (b.OUT/'CITATION_AUDIT.md').write_text('\n'.join(md),encoding='utf-8')

    readme=f'''# Decision, Persuasion, and Negotiation — GitHub-ready online textbook

The student-facing website is already built in `docs/`. Upload the complete repository to GitHub and publish it with GitHub Pages; students can then open the book immediately in a browser.

## Publish with GitHub Pages

1. Create a GitHub repository and upload **all contents of this folder**.
2. Open **Settings → Pages**.
3. Under **Build and deployment**, choose either:
   - **GitHub Actions** (the included `.github/workflows/pages.yml` deploys `docs/`), or
   - **Deploy from a branch**, select the default branch and `/docs`.
4. Save. GitHub will display the public course address after deployment.

No site generator, package manager, or external web service is required. All links are relative, and `docs/.nojekyll` lets GitHub serve the prebuilt files as-is.

## Preview locally

```bash
python -m http.server 8000 --directory docs
```

Then open the local address shown by Python.

## What students receive

- {len(chapters)} chapters in seven cumulative parts.
- A **Start Here** guide and seven part-overview pages.
- One accessible conceptual figure per chapter plus a whole-book reading map.
- Responsive HTML tables, full-text search, dark mode, reading progress, mobile navigation, and print styles.
- Chapter-specific reference lists and a master bibliography containing only cited works.
- A complete single-page edition and a downloadable EPUB.

## Repository map

- `docs/` — publishable website; this is what GitHub Pages serves.
- `chapters/` — editable Markdown chapter sources.
- `parts/` and `start-here.md` — editable orientation and transition pages.
- `appendices/` — portable tools and the corrected example index.
- `figures/` — SVG web illustrations and PNG EPUB illustrations.
- `book.md` — combined book source used for the EPUB.
- `CITATION_AUDIT.md` and `citation-audit.json` — reference correspondence audit.
- `STRUCTURE_AND_EDITORIAL_REPORT.md` — rationale for the revised flow.
- `QA_REPORT.md` — post-build checks.

## Editing

Small text edits can be made directly in the Markdown files and corresponding prebuilt HTML. For a full regeneration from the original DOCX sources, see `scripts/`; those scripts are included for provenance and require the original source files.

No license has been added. Add the license you want students and other users to follow before making the repository public.
'''
    (b.OUT/'README.md').write_text(readme,encoding='utf-8')
    (b.OUT/'.nojekyll').write_text('',encoding='utf-8')
    (b.OUT/'.gitignore').write_text('__pycache__/\n.DS_Store\n',encoding='utf-8')
    (b.OUT/'requirements.txt').write_text('markdown-it-py>=3.0\nJinja2>=3.1\nbeautifulsoup4>=4.12\nPyYAML>=6.0\n',encoding='utf-8')
    (b.OUT/'CITATION.cff').write_text('''cff-version: 1.2.0
title: "Decision, Persuasion, and Negotiation: How Minds Choose, Influence, Connect, and Bargain"
message: "Please cite this textbook using the metadata below."
type: book
authors:
  - family-names: Zhang
    given-names: Huanren Warren
year: 2026
version: "2026 revised GitHub edition"
''',encoding='utf-8')
    wf=b.OUT/'.github/workflows'; wf.mkdir(parents=True,exist_ok=True)
    (wf/'pages.yml').write_text('''name: Deploy static textbook to GitHub Pages
on:
  push:
    branches: ["main", "master"]
  workflow_dispatch:
permissions:
  contents: read
  pages: write
  id-token: write
concurrency:
  group: pages
  cancel-in-progress: true
jobs:
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      - name: Configure Pages
        uses: actions/configure-pages@v5
      - name: Upload prebuilt site
        uses: actions/upload-pages-artifact@v3
        with:
          path: docs
      - name: Deploy
        id: deployment
        uses: actions/deploy-pages@v4
''',encoding='utf-8')

b.write_support_files = write_support_files

# Run the base pipeline with all overridden editorial, visual, and site functions.
def build():
    b.main()

    # Rebuild EPUB with a proper cover resource and update the student download.
    epub_cmd = [
        'pandoc', 'book.md', '-o', str(b.EPUB), '--toc', '--toc-depth=2',
        '--metadata', 'title=Decision, Persuasion, and Negotiation',
        '--metadata', 'author=Huanren Warren Zhang',
        '--metadata', 'lang=en',
        '--epub-cover-image=figures/cover.png',
    ]
    subprocess.run(epub_cmd, cwd=b.OUT, check=True)
    shutil.copy2(b.EPUB, b.OUT/'docs/downloads'/b.EPUB.name)

    # Root convenience redirect and a publication checklist for the repository owner.
    (b.OUT/'index.html').write_text('''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Decision, Persuasion, and Negotiation</title><meta http-equiv="refresh" content="0; url=docs/index.html"></head><body><main><p><a href="docs/index.html">Open the textbook</a></p></main></body></html>''', encoding='utf-8')
    (b.OUT/'GITHUB_UPLOAD_CHECKLIST.md').write_text('''# GitHub upload checklist

1. Create a new GitHub repository.
2. Upload **every file and folder** in this package, including hidden folders such as `.github` and files such as `.nojekyll`.
3. Open **Settings → Pages**.
4. Choose one publishing method:
   - **GitHub Actions:** select GitHub Actions as the source; the included workflow deploys the prebuilt `docs/` folder after each push to `main` or `master`.
   - **Deploy from a branch:** select the default branch and the `/docs` folder.
5. Wait for deployment to finish and open the public Pages address shown by GitHub.
6. Test the home page, **Start Here**, one chapter, search, dark mode, mobile navigation, the complete-book page, references, and the EPUB download.
7. Before later releases, run `python scripts/qa_repository.py` from the repository root and publish only when `QA_REPORT.md` reports **PASS**.

For a local preview:

```bash
python -m http.server 8000 --directory docs
```
''', encoding='utf-8')

    # Keep source and QA scripts for provenance and repeatable release checks.
    shutil.copy2(BASE_SCRIPT,b.OUT/'scripts/base_docx_conversion.py')
    shutil.copy2(Path(__file__),b.OUT/'scripts/revised_build_pipeline.py')
    if QA_SCRIPT.exists():
        shutil.copy2(QA_SCRIPT,b.OUT/'scripts/qa_repository.py')
        subprocess.run(['python', str(b.OUT/'scripts/qa_repository.py'), str(b.OUT)], check=True)

    # Recreate the archive after the cover, scripts, and QA reports have been added.
    if b.ZIP.exists():
        b.ZIP.unlink()
    with zipfile.ZipFile(b.ZIP,'w',zipfile.ZIP_DEFLATED) as z:
        for f in b.OUT.rglob('*'):
            if f.is_file():
                z.write(f,f.relative_to(b.OUT.parent))

if __name__ == '__main__':
    build()
