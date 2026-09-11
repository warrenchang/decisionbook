#!/usr/bin/env python3
"""Build the book's decision map and the seven compact part reading maps.

The main map names analytical functions, not mandatory psychological stages.
Part-map arrows indicate reading order; they make no causal claim.
"""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parents[1] / 'figures'
PARTS = {
    1: [('What is the decision?',), ('How does the judgment', 'take shape?'), ('What can we learn', 'afterward?')],
    2: [('What guides intuition?',), ('When does it mislead?',), ('How can we check it?',)],
    3: [('What are the consequences?',), ('What changes over time?',), ('What makes life better?',)],
    4: [('How do choices depend', 'on others?'), ('Why cooperate or conform?',), ('What happens in', 'groups and markets?')],
    5: [('What does the audience', 'believe?'), ('How can we make', 'meaning clear?'), ('How do we check', 'and repair it?')],
    6: [('What are the alternatives?',), ('Where is value', 'claimed or created?'), ('How will the', 'agreement work?')],
    7: [('Where is the obstacle?',), ('What conditions', 'can change?'), ('What do the results show?',)],
}
NAVIGATION = ['Current context & information', 'Notice & interpret', 'Construct options', 'Predict consequences', 'Value consequences', 'Choose, commit & act', 'Observe & learn']

def begin(width, height, title, desc):
    return [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">', f'<title id="title">{escape(title)}</title>', f'<desc id="desc">{escape(desc)}</desc>', '<defs><marker id="arrow" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto" markerUnits="userSpaceOnUse"><path d="M0.5 0.5 L8 4.5 L0.5 8.5 Z" fill="#47647e"/></marker></defs>', f'<rect width="{width}" height="{height}" fill="#fff"/>']

def label(x,y,lines,size=32,weight=600,color='#17324d'):
    first=y-(len(lines)-1)*19
    spans=''.join(f'<tspan x="{x}" y="{first+i*38}">{escape(line)}</tspan>' for i,line in enumerate(lines))
    return f'<text text-anchor="middle" font-family="Arial, sans-serif" font-size="{size}" font-weight="{weight}" fill="{color}">{spans}</text>'

def arrow(d):
    return f'<path d="{d}" fill="none" stroke="#47647e" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" marker-end="url(#arrow)"/>'

def reading_map(number):
    labels=PARTS[number]
    desc='A reading route through this part: '+ '; '.join(' '.join(q) for q in labels)+'. Arrows indicate the order of questions in the book.'
    s=begin(640,520,'The questions ahead',desc)
    s.append(label(320,43,['The questions ahead'],32,700))
    for i,lines in enumerate(labels):
        y=82+i*148
        fill,stroke=('#eaf3f8','#2f6f9f') if i<2 else ('#eaf4f1','#2b7a78')
        s.append(f'<g id="question-{i+1}"><rect x="60" y="{y}" width="520" height="100" rx="18" fill="{fill}" stroke="{stroke}" stroke-width="2.5"/>{label(320,y+61,lines)}</g>')
        if i<2:s.append(arrow(f'M320 {y+100} V{y+148}'))
    return '\n'.join(s+['</svg>'])+'\n'

def decision_map():
    desc = ('An organizing map of a decision, with current context and information as inputs. '
            'Observe and learn sends feedback through one shared path to notice and interpret, '
            'construct options, predict consequences, value consequences, and choose, commit and act. '
            'These arrows indicate possible revisions, not guaranteed improvement or a fixed sequence. '
            'The enclosing frame shows that people, institutions, and design can shape the whole process. '
            'Actions and learning can change the context and information available for a later decision.')
    s=begin(700,978,'A decision in the making',desc)
    s.append('<defs><marker id="feedback-arrow" markerWidth="10" markerHeight="10" refX="9" refY="5" orient="auto" markerUnits="userSpaceOnUse"><path d="M1 1 L9 5 L1 9 Z" fill="#267766"/></marker></defs>')
    s.append(label(350,44,['A decision in the making'],34,700))
    s.append('<rect x="44" y="70" width="612" height="888" rx="24" fill="#f7f9fc" stroke="#9fb2c3" stroke-width="2"/>')
    s.append(label(350,108,['People, institutions, and design'],26,600))
    s.append(label(350,142,['can shape the whole process'],26,400,'#53677a'))
    for i,name in enumerate(NAVIGATION):
        y=167+i*104
        fill='#eaf4f1' if i==6 else '#eaf3f8'
        size=28 if i==0 else 30
        s.append(f'<g id="function-{i+1}"><rect x="110" y="{y}" width="480" height="72" rx="16" fill="{fill}" stroke="#2f6f9f" stroke-width="2.5"/>{label(350,y+47,[name],size)}</g>')
        if i<6:s.append(arrow(f'M350 {y+72} V{y+104}'))
    s.append('<g id="learning-feedback" fill="none" stroke="#267766" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">')
    s.append('<path id="feedback-to-notice" d="M590 827 H620 Q638 827 638 809 V325 Q638 307 620 307 H590" stroke-width="3" marker-end="url(#feedback-arrow)"/>')
    for name,y in [('options',411),('prediction',515),('value',619),('action',723)]:
        s.append(f'<path id="feedback-to-{name}" d="M638 {y} H590" stroke-width="3" marker-end="url(#feedback-arrow)"/>')
        s.append(f'<circle cx="638" cy="{y}" r="3.5" fill="#267766" stroke="none"/>')
    s.append('</g>')
    s.append(label(350,899,['Feedback can revise earlier decision steps'],26,400,'#267766'))
    s.append(label(350,937,['Functions can overlap or recur'],26,400,'#53677a'))
    return '\n'.join(s+['</svg>'])+'\n'

def main():
    OUT.mkdir(exist_ok=True)
    (OUT/'master-loop.svg').write_text(decision_map())
    for n in PARTS:(OUT/f'master-loop-part-{n}.svg').write_text(reading_map(n))

if __name__=='__main__':main()
