"""Check retained material and the new cross-format content/anchors; run from book root."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import hashlib, json, re, sys, zipfile
from collections import Counter
from xml.etree import ElementTree as ET
root=Path.cwd()
sys.path.insert(0,str(root/'scripts'))
from sync_references import REFERENCE_BLOCK
out=root/'audits/predictive-learning-metacognition-20260918'
chapters=['04-the-predictive-mind-perception-is-inference','08-fast-and-frugal-thinking']
checks=[]
class Page(HTMLParser):
    def __init__(self,text):
        super().__init__();self.ids=[];self.links=[];self.feed(text)
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.append(a['id'])
        if tag=='a' and 'href' in a:self.links.append(a['href'])
for ch in chapters:
    source=root/'chapters'/f'{ch}.qmd'
    current=source.read_text()
    before=(out/f'chapter-{ch[:2]}-before.qmd').read_text()
    assert set(REFERENCE_BLOCK.findall(before)) <= set(REFERENCE_BLOCK.findall(current))
    assert set(re.findall(r'!\[[^\n]+',before)) <= set(re.findall(r'!\[[^\n]+',current))
    html=root/'docs/chapters'/f'{ch}.html'
    page=Page(html.read_text())
    assert not [k for k,v in Counter(page.ids).items() if v>1]
    for href in page.links:
        url=urlsplit(href)
        if url.scheme or url.netloc or not url.path.endswith('.html'):continue
        target=(html.parent/unquote(url.path)).resolve()
        assert target.exists(),href
        if url.fragment:assert unquote(url.fragment) in Page(target.read_text()).ids,href
    checks.append({'chapter':ch,'all_prior_references_preserved':True,'all_figures_preserved':True,'html_ids_unique':True,'html_local_links_resolve':True})
expected={
 'generative-ai-and-predictive-processing':['in-context learning','Nassar et al.','Boyke et al.'],
 'research-lens-restored-sight-as-a-bounded-calibration-case':['Shirl Jennings','Held et al.'],
 'monitoring-and-guiding-thought':['Metacognition','Desender et al.'],
 'ai-reasoning-and-reflective-thought':['Tree of Thoughts','Huang et al.','Guo et al.'],
}
epub=root/'docs/Decision-in-the-Making.epub'
with zipfile.ZipFile(epub) as z:
    nodes={}
    for name in z.namelist():
        if not name.endswith('.xhtml'):continue
        doc=ET.fromstring(z.read(name))
        for e in doc.iter():
            if e.get('id') in expected:nodes.setdefault(e.get('id'),[]).append((name,e))
    for anchor,texts in expected.items():
        assert len(nodes.get(anchor,[]))==1,(anchor,'must have one EPUB anchor')
        name,node=nodes[anchor][0]
        text=' '.join(' '.join(node.itertext()).split())
        for t in texts:assert t in text,(anchor,t)
        assert not any(e.tag.endswith('details') or e.get('hidden') is not None for e in node.iter())
        checks.append({'epub_anchor':anchor,'file':name,'unique':True,'content_present_and_expanded':True})
report={'checks':checks,'epub_sha256':hashlib.sha256(epub.read_bytes()).hexdigest()}
(out/'content-checks.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
