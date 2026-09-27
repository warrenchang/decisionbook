#!/usr/bin/env python3
"""Build the book's original MCQ sets from reviewed, human-readable source banks."""
from __future__ import annotations
import argparse
import hashlib
import html
import json
import random
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROMAN = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']
LETTERS = 'ABCDE'
EXTRA_SOURCES = {'C02.05': 'appendices/appendix-a-rational-choice-and-decision-analysis.qmd',
                 'P01.09': 'appendices/appendix-a-rational-choice-and-decision-analysis.qmd'}

def read_bank():
    items = []
    for path in sorted((ROOT / 'assessments/bank').glob('part-*.md')):
        for block in re.split(r'^## ', path.read_text(), flags=re.M)[1:]:
            heading, body = block.split('\n', 1)
            ident, topic, difficulty, cognitive, sources = heading.split(' | ')
            lines = [line.strip() for line in body.splitlines() if line.strip()]
            choices = []
            stem = []
            for line in lines:
                if line.startswith(('+ ', '- ')):
                    text, rationale = line[2:].split(' | ', 1)
                    choices.append({'text': text, 'rationale': rationale, 'correct': line[0] == '+'})
                else:
                    assert not choices, f'{ident}: prose after choices'
                    stem.append(line)
            assert len(choices) == 5 and sum(c['correct'] for c in choices) == 1, ident
            # Stable per-item randomization: edits to other items never change this key.
            random.Random('decision-book-practice-2026:' + ident).shuffle(choices)
            chapters = [int(s) for s in sources.split(',')]
            item = dict(id=ident, set=ident.split('.')[0], topic=topic, difficulty=difficulty,
                        cognitive=cognitive, chapters=chapters, stem=' '.join(stem), choices=choices)
            item['answer'] = next(i for i, c in enumerate(choices) if c['correct'])
            item['source_file'] = str(path.relative_to(ROOT))
            items.append(item)
    return items

def source_paths(item):
    result = [(f'Chapter {n}', next(ROOT.glob(f'chapters/{n:02}-*.qmd')).relative_to(ROOT)) for n in item['chapters']]
    if item['id'] in EXTRA_SOURCES:
        result.append(('Appendix A: decision analysis', Path(EXTRA_SOURCES[item['id']])))
    return result

def render_set(set_id, items):
    sid = set_id.lower()
    count = len(items)
    esc = html.escape
    form = [f'<form class="book-practice" id="quiz-{sid}" data-practice-set="{set_id}" novalidate>',
            f'<p id="quiz-{sid}-instructions">Choose one answer for each of the {count} questions. Complete the set, then select <strong>Check answers</strong> to see your score and explanations. Each question is worth one point.</p>',
            '<noscript><p>For a self-check without JavaScript, record your choices, then open the answer key below.</p></noscript>']
    for n, q in enumerate(items, 1):
        qid = q['id'].lower().replace('.', '-')
        form += [f'<fieldset class="practice-question" id="{qid}" aria-describedby="quiz-{sid}-instructions">',
                 f'<legend><span class="practice-number">{n}.</span> {esc(q["stem"])}</legend>']
        for j, c in enumerate(q['choices']):
            oid = f'{qid}-{LETTERS[j].lower()}'
            form.append(f'<label class="practice-option" for="{oid}"><input type="radio" id="{oid}" name="{qid}" value="{j}"><span><strong>{LETTERS[j]}.</strong> {esc(c["text"])}</span></label>')
        form.append(f'<p class="practice-item-result" id="{qid}-result" hidden></p></fieldset>')
    form += [f'<div class="practice-controls"><p class="practice-progress" aria-live="polite">0 of {count} answered</p>',
             '<button class="practice-submit" type="submit" disabled>Check answers</button>',
             '<button class="practice-retry" type="button" hidden>Try again</button></div>',
             '<p class="practice-score" role="status" tabindex="-1" hidden></p>',
             f'<details class="practice-key" id="answers-{sid}"><summary>Answers and explanations</summary><ol class="practice-answer-list">']
    for n, q in enumerate(items, 1):
        qid = q['id'].lower().replace('.', '-')
        form.append(f'<li data-answer="{q["answer"]}" data-question="{qid}"><h3>Question {n}: {LETTERS[q["answer"]]}</h3><p class="practice-your-answer" hidden></p><dl>')
        for j, c in enumerate(q['choices']):
            label = 'Correct' if c['correct'] else 'Incorrect'
            form.append(f'<dt>{LETTERS[j]}. {esc(c["text"])} <span class="practice-verdict">({label})</span></dt><dd>{esc(c["rationale"])}</dd>')
        links = ' · '.join(f'<a href="../{p.with_suffix(".html")}">{esc(label)}</a>' for label, p in source_paths(q))
        form.append(f'</dl><p class="practice-source">Review: {links}. <a href="#{qid}">Back to question {n}</a></p></li>')
    form += ['</ol></details></form>', '<script src="../assets/practice.js" defer></script>']
    out = ['<!-- Generated by scripts/build_practice.py. Edit assessments/bank/ instead. -->',
           '::: {.content-visible unless-format="epub"}', '```{=html}', *form, '```', ':::', '',
           '::: {.content-visible when-format="epub"}',
           f'Choose one answer (A–E) for each of the {count} questions. Record all your choices before following the link to the answer key. Each question is worth one point.', '']
    for n, q in enumerate(items, 1):
        qid = q['id'].lower().replace('.', '-')
        out += [f'::: {{#{qid} .practice-question}}', f'**Question {n}.** {q["stem"]}', '']
        out += [f'{LETTERS[j]}) {c["text"]}' for j, c in enumerate(q['choices'])]
        out += ['', ':::', '']
    out += [f'[Finished the set? Check the answers and explanations.](#answers-{sid})', '',
            f'::: {{#answers-{sid} .practice-answer-key}}', '**Answers and explanations**', '',
            'Count one point for each correct answer, then review the explanations for any alternatives you considered.', '']
    for n, q in enumerate(items, 1):
        qid = q['id'].lower().replace('.', '-')
        out += [f'**Question {n}: {LETTERS[q["answer"]]}.**', '']
        for j, c in enumerate(q['choices']):
            verdict = 'Correct' if c['correct'] else 'Incorrect'
            out += [f'- **{LETTERS[j]}. {c["text"]} ({verdict})** {c["rationale"]}']
        links = ' · '.join(f'[{label}](../{p}' + ('#rational-choice-and-decision-analysis' if p.parts[0] == 'appendices' else '') + ')' for label, p in source_paths(q))
        out += ['', f'Review: {links}. [Back to question {n}](#{qid}).', '']
    out += [':::', ':::', '']
    return '\n'.join(out)

def outputs(items):
    sets = defaultdict(list)
    for item in items:
        sets[item['set']].append(item)
    for sid, questions in sets.items():
        yield ROOT / f'assessments/generated/{sid.lower()}.qmd', render_set(sid, questions)
    # Metadata is a reproducible review artifact, not a second authored bank.
    yield ROOT / 'assessments/published-bank.json', json.dumps(items, ensure_ascii=False, indent=2) + '\n'

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    items = read_bank()
    stale = []
    for path, content in outputs(items):
        if not path.exists() or path.read_text() != content:
            stale.append(str(path.relative_to(ROOT)))
            if not args.check:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content)
    if args.check and stale:
        raise SystemExit('Stale practice outputs: ' + ', '.join(stale))
    print(f'Practice bank: {len(items)} questions, {len(set(q["set"] for q in items))} sets; {len(stale)} ' + ('stale' if args.check else 'updated'))

if __name__ == '__main__':
    main()
