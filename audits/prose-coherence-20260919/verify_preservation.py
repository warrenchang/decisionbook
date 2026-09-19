"""Verify retained book structure and evidence artifacts after the prose-only edit."""
from pathlib import Path
from collections import Counter
import hashlib,json,re
ROOT=Path(__file__).resolve().parents[2]
AUDIT=Path(__file__).resolve().parent

def digest(items):
    return hashlib.sha256(json.dumps(items,ensure_ascii=False,sort_keys=True).encode()).hexdigest()

def signatures(text):
    body=re.split(r'^## References',text,flags=re.M)[0]
    return {
        'headings':digest(re.findall(r'^#{1,6} .+$',text,re.M)),
        'anchors':digest(dict(Counter(re.findall(r'\{[^}\n]*#([A-Za-z][\w.-]*)',text)))),
        'figures':digest(re.findall(r'^!\[.*$',text,re.M)),
        'tables':digest(re.findall(r'^\|.*$|^: [^\n]*#tbl-[^\n]*$',text,re.M)),
        'references':digest(re.split(r'^## References',text,flags=re.M)[1:]),
        'body_years':digest(sorted(set(re.findall(r'\b(?:18|19|20)\d{2}[a-z]?\b',body)))),
    }

if __name__=='__main__':
    expected=json.loads((AUDIT/'preservation-baseline.json').read_text());records=[]
    for f,data in expected.items():
        current=(ROOT/f).read_text();actual=signatures(current)
        assert actual==data['signatures'],(f,[key for key in actual if actual[key]!=data['signatures'][key]])
        records.append({'file':f,'structure_and_evidence_artifacts':'PASS','word_reduction':data['words']-len(current.split())})
    result={'status':'PASS','sources_reviewed':len(records),'net_words_removed':sum(r['word_reduction'] for r in records),'records':records}
    (AUDIT/'preservation-qa.json').write_text(json.dumps(result,indent=2)+'\n')
    print(f"PASS: all {len(records)} source files retain headings, anchors, figures, tables, reference lists and distinct citation years. Net reduction: {result['net_words_removed']} words.")
