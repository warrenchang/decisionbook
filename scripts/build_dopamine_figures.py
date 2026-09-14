#!/usr/bin/env python3
"""Render the A–E teaching schematics shared with BE06. No empirical data.

Owns only reward-prediction-error-abcd.svg and reward-uncertainty-comparison.svg.
Coordinates and source provenance live in figures-src/dopamine-schematics.json.
Render PNG fallbacks from the final SVG files with render_svg_png_fallbacks.cjs.
"""
from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.lines import Line2D
import xml.etree.ElementTree as E
E.register_namespace("", "http://www.w3.org/2000/svg")

ROOT=Path(__file__).resolve().parents[1]
DATA=json.loads((ROOT/'figures-src/dopamine-schematics.json').read_text())['panels']
for name in ['Arial.ttf','Arial Bold.ttf']:
    path=Path('/System/Library/Fonts/Supplemental')/name
    if path.exists():font_manager.fontManager.addfont(path)
plt.rcParams.update({'font.family':'Arial','font.size':19,'svg.fonttype':'none','svg.hashsalt':'be06-ch21-dopamine','axes.labelcolor':'#183047','text.color':'#183047','xtick.color':'#53677a','ytick.color':'#53677a','savefig.facecolor':'white'})
INK='#183047';TEAL='#087F8C';ORANGE='#B64F23';BLUE='#315C95';GRAY='#69777d';LIGHT='#d8e0e4'

def save(fig,name,title,description):
    dest=ROOT/'figures'/f'{name}.svg'
    fig.savefig(dest,format='svg',metadata={'Date':None,'Creator':'Decision Book schematic generator'})
    plt.close(fig)
    root=E.fromstring(dest.read_bytes());ns='http://www.w3.org/2000/svg'
    root.set('role','img');root.set('aria-labelledby','title desc')
    for tag,text in reversed([('title',title),('desc',description)]):
        el=E.Element('{'+ns+'}'+tag,id=tag);el.text=text;root.insert(0,el)
    # Explicit pixels make browser and PNG fallback dimensions consistent.
    vb=[float(v) for v in root.get('viewBox').split()]
    root.set('width','800');root.set('height',str(round(800*vb[3]/vb[2])))
    dest.write_bytes(E.tostring(root,encoding='UTF-8',xml_declaration=True))

def axes_style(ax,events,ylim):
    ax.set_xlim(0,6.3);ax.set_ylim(*ylim)
    for spine in ax.spines.values():spine.set_visible(False)
    ax.axhline(0,color=GRAY,lw=1.1,zorder=0)
    for x,label in events:ax.axvline(x,color=LIGHT,lw=1,zorder=0)
    ax.set_xticks([x for x,_ in events],[label for _,label in events],fontsize=24)
    ax.set_yticks([-.85,0,.85],['−','0','+'],fontsize=24)
    ax.tick_params(axis='both',length=0,pad=6)

fig=plt.figure(figsize=(8,10.2))
specs=[('A','Unexpected reward',[(1,'Cue'),(4,'Reward')]),('B','Learned prediction',[(1,'Cue'),(4,'Reward')]),('C','Reward omitted',[(1,'Cue'),(4,'No reward')]),('D','Unexpected delay',[(1,'Cue'),(3.6,'Due'),(5,'Reward')])]
for i,(key,title,events) in enumerate(specs):
    ax=fig.add_axes([.12,.815-i*.24,.83,.13]);axes_style(ax,events,(-1.15,1.15))
    ax.set_title(f'{key}  {title}',loc='left',fontsize=25,weight='bold',pad=11)
    ax.plot(DATA[key]['xVal'],DATA[key]['yVal'],color=TEAL,lw=3,solid_capstyle='round')
fig.text(.53,.012,'Time within each trial',ha='center',fontsize=24)
save(fig,'reward-prediction-error-abcd','Reward prediction error: panels A–D','A cue that does not yet predict reward elicits no learned reward response in panel A; an unexpected reward elicits a burst. Later panels show a learned cue, reward omission and unexpected delay. Curves show schematic neuronal firing changes around baseline, not absolute dopamine levels.')

fig=plt.figure(figsize=(8,4.8))
fig.legend(handles=[Line2D([0],[0],color=TEAL,lw=3,label='100%: certain reward'),Line2D([0],[0],color=ORANGE,lw=3,ls=(0,(6,4)),label='50%: uncertain reward')],loc='upper left',bbox_to_anchor=(.11,1.02),frameon=False,fontsize=24,handlelength=1.6,labelspacing=.3)
ax=fig.add_axes([.12,.16,.83,.53]);axes_style(ax,[(.8,'Cue'),(4.7,'Outcome')],(-.80,1.60))
ax.set_yticks([0],['0'])
shared=None
for s in DATA['E']:
    certain=s['name'].startswith('100%')
    if certain:
        ax.plot(s['xVal'],s['yVal'],color=TEAL,lw=3,solid_capstyle='round')
        continue
    before=[(x,y) for x,y in zip(s['xVal'],s['yVal']) if x<=4.7]
    after=[(x,y) for x,y in zip(s['xVal'],s['yVal']) if x>=4.7]
    if shared is None:
        shared=before
        ax.plot(*zip(*before),color=ORANGE,lw=3,ls=(0,(6,4)))
    else:assert before==shared,'Uncertain paths must be identical before the outcome.'
    omitted='omitt' in s['name'].lower()
    ax.plot(*zip(*after),color=ORANGE if omitted else BLUE,lw=3,ls=(0,(6,4)))
ax.text(5.52,1.38,'Reward',ha='center',color=BLUE,fontsize=24)
ax.text(5.43,-.74,'No reward',ha='center',color=ORANGE,fontsize=24)
save(fig,'reward-uncertainty-comparison','Certain and uncertain rewards','The solid teal curve represents certain reward. The dashed orange curve shows shared anticipation under fifty-percent reward probability. At the outcome, the blue dashed branch rises for reward received and the orange dashed branch falls for reward omitted. Curves are schematic neuronal firing changes around baseline.')
print('Rendered A–D and E from the shared BE06 schematic coordinates.')
