"""Verify source preservation and the figure shipped inside HTML and EPUB."""
from pathlib import Path
import hashlib,json,re,posixpath,zipfile
import xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[2]
HERE=Path(__file__).resolve().parent
sha=lambda b:hashlib.sha256(b).hexdigest()
source=ROOT/'chapters/27-markets-mispricing-and-bubbles.qmd'
before=(HERE/'chapter-before.qmd').read_text().splitlines()
after=source.read_text().splitlines()
assert len(before)==len(after)
assert sum(x!=y for x,y in zip(before,after))==1
figure=ROOT/'figures/finance-earnings-drift-redraw.svg'
assert sha((ROOT/'figures/finance-earnings-drift-evidence.png').read_bytes()) == '1a3ac4a128b076e2ccb2ba452165aab135b3489ffe801b8a7600a5db126bb4a4'
r=ET.fromstring(figure.read_bytes()); ns={'s':'http://www.w3.org/2000/svg'}
assert r.find('s:title',ns) is not None and r.find('s:desc',ns) is not None
assert r.get('viewBox')=='0 0 604.8 432'
labels=[t.text for t in r.findall('.//s:text',ns)]
assert all(str(i) in labels for i in range(1,11))
htmlpath=ROOT/'docs/chapters/27-markets-mispricing-and-bubbles.html'
html=htmlpath.read_text()
start=html.index('<div id="fig-finance-earnings-evidence"')
block=html[start:html.index('</figure>',start)]
assert 'Figure&nbsp;27.5:' in block
assert '../figures/finance-earnings-drift-redraw.svg' in block
assert 'Approximately digitized' in block
assert 'alt="Ten earnings-surprise groups' in block
assert sha((ROOT/'docs/figures/finance-earnings-drift-redraw.svg').read_bytes())==sha(figure.read_bytes())
assert sha((ROOT/'docs/figures/finance-earnings-drift-redraw.png').read_bytes())==sha((ROOT/'figures/finance-earnings-drift-redraw.png').read_bytes())
epub=ROOT/'docs/Decision-in-the-Making.epub'
with zipfile.ZipFile(epub) as z:
    matched=[(n,z.read(n)) for n in z.namelist() if n.endswith('.xhtml') and b'id="fig-finance-earnings-evidence"' in z.read(n)]
    assert len(matched)==1
    n,content=matched[0]
    tree=ET.fromstring(content)
    f=next(e for e in tree.iter() if e.get('id')=='fig-finance-earnings-evidence')
    img=next(e for e in f.iter() if e.tag.endswith('}img'))
    text=' '.join(' '.join(f.itertext()).split())
    assert 'Figure 27.5:' in text
    assert 'Approximately digitized' in text
    assert 'Curves are traced approximately' in img.get('alt','')
    member=posixpath.normpath(posixpath.join(posixpath.dirname(n),img.get('src')))
    assert sha(z.read(member)) == sha(figure.read_bytes())
assert sha(epub.read_bytes())==sha((ROOT/'_epub/Decision-in-the-Making.epub').read_bytes())
result={
    'status':'PASS',
    'source_preservation':{'chapter_lines_changed':1,'original_scan_unchanged':True},
    'svg':{'accessible_title_description':True,'endpoint_labels':10,'viewBox':r.get('viewBox')},
    'html':{'figure_number':'27.5','svg_matches_source':True,'png_fallback_matches_source':True,'approximation_caption':True,'alt_text':True},
    'epub':{'chapter':n,'image':member,'figure_number':'27.5','svg_matches_source':True,'approximation_caption':True,'alt_text':True,'staged_and_delivered_match':True},
    'visual_checks':{'native_figure':'PASS','800px':'PASS','390px':'labels too small when fitted; existing 900px HTML SVG reading pane retained','independent_source_fidelity_review':'PASS','browser_destination_screenshot':'not performed; existing local-file preview policy block respected','native_epub_reader':'not inspected'},
    'sha256':{str(p.relative_to(ROOT)):sha(p.read_bytes()) for p in [source,figure,htmlpath,epub]}
}
(HERE/'validation.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
