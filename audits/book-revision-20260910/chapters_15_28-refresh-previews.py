from PIL import Image, ImageDraw
from pathlib import Path
import json,xml.etree.ElementTree as E
ROOT=Path(__file__).resolve().parents[2]; A=Path(__file__).resolve().parent
fs=json.loads((A/'chapters_15_28-figure-paths.json').read_text()); out=A/'chapters_15_28-visuals';out.mkdir(exist_ok=True)
for i,f in enumerate(fs):
 p=ROOT/f['path'];native=p
 if p.suffix=='.svg':
  r=E.parse(p).getroot();native=p.with_suffix('.png'); w=int(float(r.attrib['width']))
 else:w=Image.open(p).width
 im=Image.open(native).convert('RGB')
 im.resize((760,round(im.height*760/im.width)),Image.Resampling.LANCZOS).save(out/f'{i:02d}-{p.stem}.png')
 # 100% source-size inspection preview; matches SVG CSS pixel dimensions.
 im.resize((w,round(im.height*w/im.width)),Image.Resampling.LANCZOS).save(out/f'native-{i:02d}-{p.stem}.png')
for first in [0,20]:
 subset=fs[first:first+20];sheet=Image.new('RGB',(1600,1500),'#e3e8ed');d=ImageDraw.Draw(sheet)
 for j,f in enumerate(subset):
  p=ROOT/f['path'];p=p.with_suffix('.png') if p.suffix=='.svg' else p
  im=Image.open(p).convert('RGB');im.thumbnail((388,264),Image.Resampling.LANCZOS);x=(j%4)*400+(400-im.width)//2;y=(j//4)*300+25;sheet.paste(im,(x,y));d.text(((j%4)*400+8,(j//4)*300+4),f'{first+j:02d} {p.stem}',fill='black')
 sheet.save(out/f'contact-{first:02d}.png')
