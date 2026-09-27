#!/usr/bin/env python3
"""Audit authored MCQs, generated keys, and optionally both published formats."""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict
from html.parser import HTMLParser
import itertools
import json
from pathlib import Path
import re
import zipfile
from xml.etree import ElementTree as ET
from build_practice import ROOT, LETTERS, read_bank, outputs

class Node:
    def __init__(self, tag='', attrs=None):
        self.tag, self.attrs, self.children, self.parts = tag, dict(attrs or []), [], []
    def all(self, tag=None, cls=None):
        out=[]
        for child in self.children:
            if (tag is None or child.tag == tag) and (cls is None or cls in child.attrs.get('class','').split()):
                out.append(child)
            out.extend(child.all(tag,cls))
        return out
    def raw(self):
        return ''.join(p if isinstance(p,str) else p.raw() for p in self.parts)
    def content(self):
        return ' '.join(self.raw().split())

class Tree(HTMLParser):
    VOID={'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}
    def __init__(self,text):
        super().__init__(convert_charrefs=True);self.root=Node();self.stack=[self.root];self.feed(text)
    def handle_starttag(self,tag,attrs):
        n=Node(tag,attrs);self.stack[-1].children.append(n);self.stack[-1].parts.append(n)
        if tag not in self.VOID:self.stack.append(n)
    def handle_startendtag(self,tag,attrs):self.handle_starttag(tag,attrs);self.handle_endtag(tag)
    def handle_endtag(self,tag):
        for i in range(len(self.stack)-1,0,-1):
            if self.stack[i].tag==tag:self.stack=self.stack[:i];break
    def handle_data(self,data):self.stack[-1].parts.append(data)

def norm(s):
    # Pandoc applies typographic punctuation in EPUB; preserve substantive text.
    s=s.translate(str.maketrans({'’':"'",'‘':"'",'“':'"','”':'"'}))
    return ' '.join(s.split())
def words(s): return re.findall(r'\b\w+\b',s.lower())
def run(keys):return max((len(list(g)) for _,g in itertools.groupby(keys)),default=0)

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--rendered',action='store_true');args=ap.parse_args()
    items=read_bank();blueprint=json.loads((ROOT/'assessments/blueprint.json').read_text());sets=defaultdict(list)
    errors=[]
    def check(ok,msg):
        if not ok:errors.append(msg)
    for q in items:sets[q['set']].append(q)
    check(len(items)==280,'Expected 280 questions');check(len(sets)==49,'Expected 49 sets')
    check(len({q['id'] for q in items})==len(items),'Duplicate item IDs')
    check(len({norm(q['stem']).lower() for q in items})==len(items),'Duplicate stems')
    check(len(blueprint)==49,'Blueprint has wrong number of sets')
    for b in blueprint:
        qs=sets[b['set']];check(len(qs)==b['count'],f'{b["set"]}: wrong count')
        check(dict(Counter(q['difficulty'] for q in qs))==b['difficulty'],f'{b["set"]}: difficulty mismatch')
        expected=[f'{b["set"]}.{i:02}' for i in range(1,b['count']+1)]
        check([q['id'] for q in qs]==expected,f'{b["set"]}: ID sequence')
        covered=set(n for q in qs for n in q['chapters'])
        if b['set'].startswith('P'):check(set(b['chapters'])<=covered,f'{b["set"]}: chapter coverage missing')
        else:check(int(b['set'][1:]) in covered,f'{b["set"]}: missing own chapter')
        source=(ROOT/b['source']).read_text()
        check(source.count(f'include ../assessments/generated/{b["set"].lower()}.qmd')==1,f'{b["set"]}: include missing or repeated')
    for q in items:
        check(q['difficulty'] in ('easy','medium','hard'),q['id']+': bad difficulty')
        check(q['cognitive'] in ('understand','apply','analyze'),q['id']+': bad cognitive tag')
        check(bool(q['topic']) and bool(q['stem']) and bool(q['chapters']),q['id']+': metadata missing')
        check(len({c['text'].lower() for c in q['choices']})==5,q['id']+': duplicate alternatives')
        check(all(c['rationale'] for c in q['choices']),q['id']+': missing rationale')
        check(all(1<=n<=42 for n in q['chapters']),q['id']+': invalid source chapter')
    for p,text in outputs(items):check(p.exists() and p.read_text()==text,f'Stale output: {p.relative_to(ROOT)}')
    keys=[q['answer'] for q in items];counts=Counter(keys)
    check(all(0.12<=counts[n]/len(items)<=0.28 for n in range(5)),'Strong global answer-position imbalance')
    check(run(keys)<=5,'Long global run of identical correct letters')
    correct_lengths=[];distractor_lengths=[];part_stats={}
    for p in range(1,8):
        qs=[q for q in items if q['source_file'].endswith(f'part-{p}.md')];cl=[];dl=[];unique_longest=0
        for q in qs:
            lengths=[len(words(c['text'])) for c in q['choices']];cl.append(lengths[q['answer']]);other=[x for j,x in enumerate(lengths) if j!=q['answer']];dl+=other
            unique_longest+=lengths[q['answer']]>max(other)
        correct_lengths+=cl;distractor_lengths+=dl
        part_stats[str(p)]={'questions':len(qs),'correct_option_mean_words':round(sum(cl)/len(cl),2),'distractor_mean_words':round(sum(dl)/len(dl),2),'correct_uniquely_longest':unique_longest,'answers':dict(sorted(Counter(LETTERS[q['answer']] for q in qs).items()))}
    ratio=(sum(correct_lengths)/len(correct_lengths))/(sum(distractor_lengths)/len(distractor_lengths))
    check(.9<=ratio<=1.1,f'Global correct/distractor word-length ratio {ratio:.3f} outside 0.9–1.1')
    stop=set('a an the of and to is in it as with for which what how on from by are that this its each at than or be not'.split())
    token_sets=[set(words(q['stem']))-stop for q in items];near=[]
    for a in range(len(items)):
        for b in range(a+1,len(items)):
            score=len(token_sets[a]&token_sets[b])/max(1,len(token_sets[a]|token_sets[b]))
            if score>=.40:near.append({'a':items[a]['id'],'b':items[b]['id'],'jaccard':round(score,3)})
    rendered_counts={}
    if args.rendered:
        for b in blueprint:
            path=ROOT/'docs'/Path(b['source']).with_suffix('.html');check(path.is_file(),f'Missing HTML {path}')
            if not path.is_file():continue
            tree=Tree(path.read_text()).root;forms=tree.all('form','book-practice');check(len(forms)==1,f'{b["set"]}: HTML form count')
            if len(forms)!=1:continue
            form=forms[0];qs=sets[b['set']];fields=form.all('fieldset','practice-question');answers=[x for x in form.all('li') if 'data-answer' in x.attrs]
            check(len(fields)==len(qs)==len(answers),b['set']+': rendered question/key counts')
            check(any(s.attrs.get('src')=='../assets/practice.js' for s in tree.all('script')),b['set']+': script missing')
            for q,field,answer in zip(qs,fields,answers):
                check(norm(field.all('legend')[0].content()).endswith(norm(q['stem'])),q['id']+': changed stem')
                options=field.all('input');check(len(options)==5,q['id']+': radio count')
                check(all(o.attrs.get('type')=='radio' and 'checked' not in o.attrs for o in options),q['id']+': radio initialization')
                check([o.attrs.get('value') for o in options]==list(map(str,range(5))),q['id']+': radio values')
                check(answer.attrs['data-answer']==str(q['answer']),q['id']+': changed HTML key')
                for c,dt,dd in zip(q['choices'],answer.all('dt'),answer.all('dd')):
                    check(c['text'] in dt.content(),q['id']+': HTML option/key association')
                    check(norm(c['rationale'])==dd.content(),q['id']+': HTML rationale mismatch')
            key=form.all('details','practice-key')[0];check('open' not in key.attrs,b['set']+': answer key starts open')
        check((ROOT/'docs/assets/practice.js').read_bytes()==(ROOT/'assets/practice.js').read_bytes(),'Published JavaScript is stale')
        ns='{http://www.w3.org/1999/xhtml}'
        with zipfile.ZipFile(ROOT/'docs/Decision-in-the-Making.epub') as z:
            question_nodes={};key_nodes={}
            for name in z.namelist():
                if not name.endswith('.xhtml'):continue
                try:
                    tree=ET.fromstring(z.read(name))
                except ET.ParseError as exc:
                    check(False,f'{name}: invalid XHTML: {exc}')
                    continue
                for node in tree.iter():
                    classes=node.get('class','').split()
                    if 'practice-question' in classes:question_nodes[node.get('id')]=node
                    if 'practice-answer-key' in classes:key_nodes[node.get('id')]=node
            check(len(question_nodes)==280,f'EPUB question count {len(question_nodes)}')
            check(len(key_nodes)==49,f'EPUB key count {len(key_nodes)}')
            for q in items:
                qid=q['id'].lower().replace('.','-');node=question_nodes.get(qid)
                check(node is not None,q['id']+': EPUB question missing')
                if node is None:continue
                text=norm(''.join(node.itertext()));check(norm(q['stem']) in text,q['id']+': EPUB stem mismatch')
                lis=node.findall(f'.//{ns}li');check(len(lis)==5,q['id']+': EPUB option count')
                for c,li in zip(q['choices'],lis):check(norm(c['text'])==norm(''.join(li.itertext())),q['id']+': EPUB option order')
                key=key_nodes.get('answers-'+q['set'].lower());key_text=norm(''.join(key.itertext())) if key is not None else ''
                number=int(q['id'].split('.')[1]);check(f'Question {number}: {LETTERS[q["answer"]]}.' in key_text,q['id']+': EPUB key mismatch')
                check(all(norm(c['rationale']) in key_text for c in q['choices']),q['id']+': EPUB rationale missing')
            rendered_counts={'html_sets':len(blueprint),'epub_questions':len(question_nodes),'epub_answer_sections':len(key_nodes)}
    report={'status':'PASS' if not errors else 'FAIL','questions':len(items),'sets':len(sets),'errors':errors,'difficulty':dict(Counter(q['difficulty'] for q in items)),'cognitive_level':dict(Counter(q['cognitive'] for q in items)),'answer_positions':{LETTERS[i]:counts[i] for i in range(5)},'longest_answer_run':run(keys),'correct_to_distractor_mean_word_ratio':round(ratio,3),'parts':part_stats,'near_duplicate_candidates_for_editorial_review':near,'rendered':rendered_counts}
    (ROOT/'assessments/qa-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ('status','questions','sets','errors','answer_positions','longest_answer_run','correct_to_distractor_mean_word_ratio','rendered')},indent=2))
    return bool(errors)
if __name__=='__main__':raise SystemExit(main())
