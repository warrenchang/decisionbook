#!/usr/bin/env python3
"""Illustrate Music Lab treatment menus. Names and counts are invented examples.
Design source: Salganik, Dodds & Watts (2006), SOM pp. 2–3, Figs. S2–S3.
PNG companion is rendered from this SVG by the book's browser QA workflow.
"""
from pathlib import Path
from html import escape
ROOT=Path(__file__).resolve().parents[1]
W,H=640,1090
parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title desc">',
'<title id="title">What Music Lab participants saw</title>',
'<desc id="desc">Illustrative song menus, not observed data. Experiment 1 shows the same six example songs in a three-column grid: independent choice hides download counts, social influence displays counts from the participant’s world. Both use random order. Experiment 2 shows a single-column list: independent choice uses random order with no counts, social influence orders songs by its world’s download counts. The actual experiments offered 48 songs and eight separate social worlds.</desc>',
'<rect width="640" height="1090" fill="white"/>',
'<g font-family="Arial, sans-serif" fill="#183047">']
def text(x,y,s,size=24,bold=False,fill='#183047',anchor='start'):
 parts.append(f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{700 if bold else 400}" fill="{fill}" text-anchor="{anchor}">{escape(s)}</text>')
def rect(x,y,w,h,fill='#fff',stroke='#bdcdd8',rx=10):
 parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}"/>')
def play(x,y):
 parts.append(f'<path d="M{x},{y-7} l11,7 l-11,7 z" fill="#34789b"/>')
songs=['Dawn','Echo','Rain','Home','Blue','Stay'];counts={'Dawn':16,'Echo':3,'Rain':24,'Home':7,'Blue':11,'Stay':5}
text(164,31,'Independent choice',25,True,anchor='middle')
text(476,31,'Social influence',25,True,anchor='middle')
text(164,65,'Counts hidden',24,anchor='middle')
text(476,65,'Counts visible',24,anchor='middle')
text(16,121,'1  Randomly ordered grids',28,True)
for col in range(2):
 x=12+col*312
 rect(x,146,304,304,fill='#f4f8fb' if col==0 else '#f0f7f5')
 text(x+16,181,'MUSIC LAB',23,True)
 if col:text(x+288,181,'↓',24,True,anchor='end')
 for i,s in enumerate(songs):
  cx=x+12+(i%3)*94;cy=202+(i//3)*99
  rect(cx,cy,90,86)
  text(cx+45,cy+31,s,23,True,anchor='middle')
  play(cx+11,cy+61)
  if col:text(cx+57,cy+68,str(counts[s]),24,fill='#126d64',anchor='middle')
 text(x+152,430,'Random order',24,anchor='middle')
text(16,501,'2  Lists with different ordering',28,True)
for col in range(2):
 x=12+col*312
 rect(x,526,304,426,fill='#f4f8fb' if col==0 else '#f0f7f5')
 text(x+16,565,'MUSIC LAB',23,True)
 if col:text(x+280,565,'↓',24,True,anchor='end')
 order=songs if not col else sorted(songs,key=lambda s:-counts[s])
 for i,s in enumerate(order):
  cy=584+i*48
  rect(x+12,cy,280,46,fill='#fff',stroke='#d9e3e9',rx=4)
  play(x+25,cy+23);text(x+51,cy+31,s,25,True)
  if col:text(x+270,cy+31,str(counts[s]),25,fill='#126d64',anchor='end')
 text(x+152,924,'Random order' if not col else 'Most downloaded first',23,anchor='middle')
text(320,997,'↓ = downloads in your world',24,anchor='middle')
text(320,1035,'48 songs in every condition',24,True,anchor='middle')
text(320,1073,'Listen → rate → choose whether to download',24,anchor='middle')
parts.extend(['</g>','</svg>'])
(ROOT/'figures/cultural-market-study-redraw.svg').write_text('\n'.join(parts)+'\n')
