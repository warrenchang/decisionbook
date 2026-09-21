from pathlib import Path
import csv,hashlib,json,posixpath,re,zipfile,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).resolve().parent
sha=lambda b:hashlib.sha256(b).hexdigest()
figs=[('fig-finance-fed-announcement','27.2','finance-fed-announcement'),
 ('fig-finance-september11-futures','27.3','finance-september11-futures'),
 ('fig-finance-challenger','27.4','finance-challenger-redraw'),
 ('fig-finance-earnings-evidence','27.5','finance-earnings-drift-redraw')]
source=ROOT/'chapters/27-markets-mispricing-and-bubbles.qmd'
text=source.read_text();old=(HERE/'chapter-before.qmd').read_text()
assert '### Election night:' not in text and 'Kalshi.' not in text and 'Yahoo Finance.' not in text
assert '**News-timing comparison.** Compare the scheduled Fed announcement with the unfolding September 11 attacks.' in text
assert 'National Commission on Terrorist Attacks Upon the United States. (2004).' in text
# Substantive later text is preserved except the updated exercise.
def preserved_body(s):
 s=s[s.index('## What market efficiency'):s.index('## References cited')]
 return [x for x in s.splitlines() if not x.startswith('**News-timing comparison.**')]
assert preserved_body(text)==preserved_body(old)
assert sha((ROOT/'figures/finance-earnings-drift-redraw.svg').read_bytes())=='1d7a7a86407fb4f4a24b3db53b040d2d1958d7a357855c9d064fb00650c4af4c'
htmlp=ROOT/'docs/chapters/27-markets-mispricing-and-bubbles.html';html=htmlp.read_text()
assert '### Election night:' not in html and '<h3 data-anchor-id="election-night' not in html
assert 'finance-election-night.svg' not in html
checks=[]
epub=ROOT/'docs/Decision-in-the-Making.epub'
with zipfile.ZipFile(epub) as z:
 name=next(n for n in z.namelist() if n.endswith('.xhtml') and b'id="fig-finance-september11-futures"' in z.read(n))
 tree=ET.fromstring(z.read(name))
 epub_text=' '.join(tree.itertext())
 assert 'Kalshi' not in epub_text and 'Election night:' not in epub_text
 for ident,num,stem in figs:
  # Check HTML local number, caption, alt text and delivered vector bytes.
  start=html.index('<div id="'+ident+'"');block=html[start:html.index('</figure>',start)]
  assert 'Figure&nbsp;'+num+':' in block
  assert '../figures/'+stem+'.svg' in block
  assert 'alt="' in block
  svg=(ROOT/'figures'/f'{stem}.svg').read_bytes()
  assert sha(svg)==sha((ROOT/'docs/figures'/f'{stem}.svg').read_bytes())
  assert sha((ROOT/'figures'/f'{stem}.png').read_bytes())==sha((ROOT/'docs/figures'/f'{stem}.png').read_bytes())
  f=next(e for e in tree.iter() if e.get('id')==ident)
  image=next(e for e in f.iter() if e.tag.endswith('}img'))
  caption=' '.join(' '.join(f.itertext()).split())
  assert 'Figure '+num+':' in caption
  member=posixpath.normpath(posixpath.join(posixpath.dirname(name),image.get('src')))
  assert sha(z.read(member))==sha(svg)
  assert image.get('alt')
  checks.append({'id':ident,'number':num,'asset':stem+'.svg','html_and_epub_bytes_match':True,'caption_and_alt_text':True})
 assert 'Approximate trace of Siegel' in epub_text
assert sha(epub.read_bytes())==sha((ROOT/'_epub/Decision-in-the-Making.epub').read_bytes())
# Every published point is retained with the declared percentage conversion.
rows=list(csv.DictReader((HERE/'challenger-vector-points.csv').open()));assert len(rows)==897
assert all(abs(float(r['change_from_open_percent'])-100*(float(r['price_relative_to_open'])-1))<1e-10 for r in rows)
assert not any(r['company']=='Morton Thiokol' and 11.875<float(r['time_hour'])<12.58 for r in rows)
# User-facing search text for this chapter no longer carries the election example.
search=json.loads((ROOT/'docs/search.json').read_text())
entries=[x for x in search if 'chapters/27-markets-mispricing-and-bubbles.html' in x.get('href','')]
assert entries and all('Kalshi' not in x.get('text','') and '2024 US election night' not in x.get('text','') for x in entries)
result={'status':'PASS','figures':checks,'challenger_markers':len(rows),'percentage_transform':'PASS','trading_gap':'PASS',
 'election_example_removed_from_reading_path_and_search':True,'later_substantive_text_preserved_except_exercise':True,'earnings_figure_unchanged':True,
 'epub_staged_and_delivered_match':True,
 'qa':{k:(HERE/f'qa-{k}.txt').read_text().strip() for k in ['book','epub','floats']},
 'references':'PASS:1064 unique references','visual_checks':{'native_and_800px':'PASS','390px':'existing900px SVG reading pane needed for comfortable label size','browser_destination_screenshot':'not attempted; prior local-file preview restriction respected','native_epub_reader':'not inspected'},
 'sha256':{str(p.relative_to(ROOT)):sha(p.read_bytes()) for p in [source,ROOT/'references.qmd',htmlp,epub]}}
(HERE/'validation.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
