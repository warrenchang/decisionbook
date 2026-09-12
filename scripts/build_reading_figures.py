#!/usr/bin/env python3
"""Build selected compact conceptual figures. No empirical data are generated.

Keep the probability and observational figures in their own source generators.
This file owns only the SVGs listed in BUILDERS below; render their PNG
companions with render_svg_png_fallbacks.cjs after changes.
"""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INK, BLUE, GREEN, WARM = '#183047', '#25678f', '#2b7a78', '#b95f2d'


class Figure:
    def __init__(self, title, description, height):
        self.items = [f'''<svg xmlns="http://www.w3.org/2000/svg" width="760" height="{height}" viewBox="0 0 760 {height}" role="img" aria-labelledby="title desc" data-layout="compact">
<title id="title">{escape(title)}</title><desc id="desc">{escape(description)}</desc>
<defs><style>
text {{font-family:Arial,Helvetica,sans-serif;fill:{INK}}}
.title {{font-family:Georgia,serif;font-size:38px;font-weight:bold}}
</style>''']
        for name, color in [('blue', BLUE), ('green', GREEN), ('warm', WARM)]:
            self.items.append(f'<marker id="{name}" markerWidth="8" markerHeight="8" refX="8" refY="4" orient="auto-start-reverse" markerUnits="userSpaceOnUse"><path d="M0 0 L8 4 L0 8 Z" fill="{color}"/></marker>')
        self.items.append(f'</defs><rect width="760" height="{height}" fill="white"/>')

    def text(self, x, y, lines, size=28, weight='normal', color=INK, anchor='middle', css=''):
        if css == 'title': size = 38
        if isinstance(lines, str): lines = [lines]
        ts = ''.join(f'<tspan x="{x}" dy="{0 if i == 0 else size * 1.24:g}">{escape(line)}</tspan>' for i, line in enumerate(lines))
        self.items.append(f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" font-weight="{weight}" style="fill:{color}" class="{css}">{ts}</text>')

    def box(self, x, y, w, h, title, lines=(), color=BLUE, fill='#f4f7fa', title_size=32):
        self.items.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="{fill}" stroke="{color}" stroke-width="2.5"/>')
        self.text(x+w/2, y+43, title, title_size, 'bold', color)
        if lines: self.text(x+w/2, y+84, lines)

    def arrow(self, d, color='blue', both=False, dash=False):
        paint={'blue':BLUE,'green':GREEN,'warm':WARM}[color]
        self.items.append(f'<path d="{d}" fill="none" stroke="{paint}" stroke-width="3" stroke-linejoin="round" marker-end="url(#{color})"'+(f' marker-start="url(#{color})"' if both else '')+(' stroke-dasharray="7 6"' if dash else '')+'/>')

    def save(self, name):
        (ROOT/'figures'/f'{name}.svg').write_text('\n'.join(self.items+['</svg>'])+'\n')


def option_information():
    f=Figure('Better decisions begin before comparison', 'Four questions for building a better decision: expand the feasible set, name the best forgone option, seek information that could improve the choice, and stress-test the ranking. Earlier steps can be revisited.', 1190)
    f.text(380,54,['Better decisions begin','before comparison'],css='title')
    cards=[
        ('Expand the feasible set', ['Generate, combine, negotiate, stage,', 'keep searching, or walk away.']),
        ('Name the best forgone option', ['What is the best feasible alternative', 'you would give up by committing?']),
        (['Ask what information', 'could change your choice'], ['Seek it when it could improve action', 'enough to justify its cost.']),
        ('Stress-test the ranking', ['Vary assumptions; check thresholds,', 'reversibility, and safeguards.']),
    ]
    for i,(title,lines) in enumerate(cards):
        y=146+i*221
        color=BLUE if i<2 else WARM
        fill='#edf5fa' if i<2 else '#fff8f3'
        f.items.append(f'<rect x="30" y="{y}" width="700" height="177" rx="20" fill="{fill}" stroke="{color}" stroke-width="2.5"/>')
        f.items.append(f'<circle cx="77" cy="{y+46}" r="24" fill="{color}"/>')
        f.text(77,y+56,str(i+1),30,'bold','white')
        multiline=isinstance(title, list)
        f.text(411,y+(36 if multiline else 44),title,32,'bold',color)
        f.text(380,y+(122 if multiline else 115),lines,30)
        if i<3: f.arrow(f'M380 {y+177} V{y+221}')
    f.text(380,1060,['A precise calculation cannot rescue', 'an incomplete menu.'],30,'bold')
    f.text(380,1154,'Revisit earlier steps as you learn more.',30)
    f.save('option-information-portrait')


def urge_observation():
    f=Figure('An urge can change without being acted on', 'A schematic curve shows one possible rise and fall of urge intensity. Below it, breathe, recognize, allow, investigate, and non-identify and nurture are optional observation prompts, not phases of the curve or guaranteed steps to relief.', 1000)
    f.text(380,56,['An urge can change','without being acted on'],css='title')
    f.items.append(f'<path d="M104 182 V439 H702" fill="none" stroke="{INK}" stroke-width="2.5"/><path d="M120 422 C230 422 262 222 367 229 S473 416 680 422" fill="none" stroke="{WARM}" stroke-width="7" stroke-linecap="round"/>')
    f.text(390,480,'Time',30);f.items.append(f'<text x="51" y="315" text-anchor="middle" font-size="30" transform="rotate(-90 51 315)">Urge intensity</text>')
    f.text(380,535,['One possible pattern, not a timetable.','Urges can persist or return.'],30)
    f.box(63,631,634,307,'An optional observation practice',[],GREEN,'#edf7f3',32)
    for i,line in enumerate(['Breathe and pause.','Recognize what you feel.','Allow it without requiring relief.','Investigate what the urge is like.',['Non-identify and nurture','a caring response.']]):
        f.text(100,715+i*40,line,30,anchor='start')
    f.save('urge-wave-observation')


def habit_formation():
    f=Figure('Habit formation has no fixed deadline', 'A schematic automaticity curve approaches a plateau. The study summary separately reports modeled time to reach 95 percent of the plateau: 18 to 254 days, median 66. These are study estimates, not a guarantee for an individual habit.', 930)
    f.text(380,56,['Habit formation has','no fixed deadline'],css='title')
    f.text(380,156,'Illustrative shape of automaticity')
    f.items.append(f'<path d="M115 204 V475 H692" fill="none" stroke="{INK}" stroke-width="2.5"/><path d="M127 454 C165 250 271 239 675 229" fill="none" stroke="{BLUE}" stroke-width="7" stroke-linecap="round"/><path d="M127 217 H681" stroke="#607080" stroke-width="2" stroke-dasharray="7 6"/>')
    f.text(380,519,'Time');f.items.append('<text x="52" y="353" font-size="28" text-anchor="middle" transform="rotate(-90 52 353)">Automaticity</text>')
    f.text(675,201,'Plateau',28,anchor='end')
    f.box(55,587,650,280,'What Lally et al. (2010) estimated',[],title_size=31)
    f.text(380,681,['Modeled days to reach','95% of the plateau'])
    f.text(202,782,'18–254',44,'bold',BLUE);f.text(202,827,'Range')
    f.text(558,782,'66',44,'bold',WARM);f.text(558,827,'Median')
    f.save('habit-formation-curve')


def digital_arrow():
    f=Figure('An interface can make the next step more salient', 'Two versions of an illustrative hotel advertisement carry the same offer. A bundled redesign changes the action arrow, type, spacing, and layout. Reported higher clicks concern the bundle and do not isolate the arrow or establish better decisions.', 1130)
    f.text(380,57,['Make the next step','easier to notice'],css='title')
    f.box(75,168,610,284,'Original presentation',[],title_size=32)
    f.box(124,253,512,162,'Hotel offers',['Compare rooms, dates, and prices.','Choose only when the offer fits.'],title_size=31)
    f.items.append('<rect x="90" y="478" width="580" height="84" rx="14" fill="white" stroke="#607080" stroke-width="2"/>')
    f.arrow('M380 452 V478');f.arrow('M380 562 V592')
    f.text(380,509,['Bundled redesign:','arrow, type, spacing, and layout'])
    f.box(75,592,610,284,'More prominent action cue',[],title_size=32)
    f.box(124,677,512,162,'Hotel offers',['Compare rooms, dates, and prices.','Choose only when the offer fits.'],title_size=31)
    f.items.append(f'<rect x="557" y="693" width="52" height="48" rx="10" fill="{BLUE}"/><path d="M568 717 H596 M585 706 L596 717 L585 728" fill="none" stroke="white" stroke-width="3" stroke-linejoin="round"/>')
    f.text(380,946,['Reported clicks rose after the bundle.','That does not isolate the arrow’s effect','or show that choices improved.'])
    f.save('digital-arrow-affordance')


def heuristic_substitution():
    f=Figure('Notice when the question changes', 'A question about project success is replaced by an easier judgment about the founder. The resulting answer may feel like a probability judgment. The audit checks whether the cue is diagnostic of the original target.', 940)
    f.text(380,58,['Notice when the','question changes'],css='title')
    f.box(65,170,630,146,'The target question',['How likely is this project to succeed?'],WARM,'#fff8f3')
    f.box(65,393,630,146,'An easier question',['How impressive does the founder seem?'])
    f.box(65,616,630,110,'An answer that feels like a forecast',['“It will probably succeed.”'])
    f.arrow('M380 316 V393'); f.arrow('M380 539 V616')
    f.text(380,793,['Does the founder’s impression provide','good evidence about project success?'])
    f.text(380,887,'An informative cue can still receive too much weight.',28)
    f.save('heuristic-substitution')


def context_mechanisms():
    f=Figure('Four questions about context', 'Four separate cards distinguish framing, priming, fluency, and defaults. They are alternative diagnostic questions, not a sequence of stages.', 1040)
    f.text(380,60,['Four questions','about context'],css='title')
    cards=[('Framing',['What is this decision about?','Meaning and reference point'],BLUE),('Priming',['What has just been brought to mind?','Associations and accessibility'],WARM),('Fluency',['How easy does this feel to process?','Ease can become a cue'],GREEN),('Default',['What happens if I do nothing?','The outcome of inaction'],BLUE)]
    for i,(title,lines,color) in enumerate(cards): f.box(65,174+i*199,630,164,title,lines,color)
    f.text(380,1003,'Ask which mechanism the evidence supports.')
    f.save('context-mechanisms')


def fluency_pathway():
    f=Figure('When ease becomes evidence', 'Repetition, clarity, familiarity, and pronounceability can produce processing ease. That ease may inform truth, liking, safety, or confidence judgments. A separate evidence check asks whether the inference is warranted.', 1040)
    f.text(380,59,['When ease','becomes evidence'],css='title')
    f.box(65,171,630,152,'Possible sources',['Repetition, clarity, familiarity,','and pronounceability'])
    f.box(65,390,630,146,'Processing ease',['The information feels smooth,','familiar, or coherent.'],WARM,'#fff8f3')
    f.box(65,603,630,145,'Possible judgments',['“True.” “Likable.” “Safe.”','“I am confident.”'])
    f.arrow('M380 323 V390');f.arrow('M380 536 V603')
    f.box(65,823,630,169,'Check the inference',['Why was this easy to process?','What independent evidence supports it?'],GREEN,'#edf7f3')
    f.arrow('M380 748 V823','green',dash=True)
    f.save('fluency-pathway')


def communication_grounding():
    f=Figure('Understanding develops through checking', 'Person A expresses words and signals that person B interprets in context. Questions, paraphrasing, and corrections provide a return path to the speaker. Understanding remains sufficient for the current purpose and open to repair.', 1000)
    f.text(380,58,['Understanding develops','through checking'],css='title')
    nodes=[('Person A',['Intention and context']),('Words and signals',['Content, tone, and timing']),('Person B',['Interpretation and context']),('Check and repair',['Ask, paraphrase, and correct'])]
    for i,(title,lines) in enumerate(nodes):
        f.box(115,177+i*183,530,116,title,lines,GREEN if i==3 else BLUE)
        if i<3:f.arrow(f'M380 {293+i*183} V{360+i*183}')
    f.arrow('M115 784 H47 V235 H115','green')
    f.text(380,919,['Understanding is sufficient for this purpose','and can be revised in the next exchange.'])
    f.save('communication-grounding')


def conversation_needs():
    f=Figure('The same words can ask for different kinds of help', 'The statement I cannot keep doing this may concern a practical problem, emotional support, or social and identity stakes. Ask which help is wanted instead of diagnosing from the words alone.', 1200)
    f.text(380,61,['“I can’t keep doing this.”','What kind of help is wanted?'],css='title')
    cards=[('Practical',['Options, information, or a next step.','Clarify before trying to solve.','“Would it help to think through what to do?”'],BLUE),('Emotional',['Recognition, regulation, or company.','Acknowledge before redirecting.','“Do you want me to listen or help you think?”'],WARM),('Social or identity',['Respect, belonging, role, or fairness.','Explore the relational stake carefully.','“What did this seem to say about you or us?”'],GREEN)]
    for i,(title,lines,color) in enumerate(cards):f.box(55,186+i*290,650,237,title,lines,color)
    f.text(380,1101,['Ask what would help, then listen and update.','The same conversation can involve several needs.'])
    f.save('conversation-needs-map')


def silence_diagnostic():
    f=Figure('Silence can have different causes', 'Five alternative diagnoses pair a question with a possible safeguard: directive authority, suppressed dissent, shared-information bias, pluralistic ignorance, and diffusion of responsibility. A safeguard should be tested against the diagnosed mechanism.', 1300)
    f.text(380,56,['Silence can have','different causes'],css='title')
    f.text(380,156,'Diagnose before choosing a safeguard.')
    cards=[('Directive authority',['Did the leader signal the answer first?','Collect judgments before the leader speaks.']),('Suppressed dissent',['Are objections privately held but costly to voice?','Protect a way to record the minority view.']),('Shared-information bias',['Is unique evidence missing from the discussion?','Give unshared evidence a dedicated round.']),('Pluralistic ignorance',['Do private views differ from assumed group views?','Elicit both privately, then compare distributions.']),('Diffusion of responsibility',['Does each person expect someone else to act?','Name an owner, trigger, deadline, and backup.'])]
    for i,(title,lines) in enumerate(cards):f.box(40,210+i*197,680,164,title,lines,GREEN if i%2 else BLUE,title_size=31)
    f.text(380,1256,'Test whether the safeguard addresses the problem.')
    f.save('silence-mechanism-diagnostic')


BUILDERS = [option_information, urge_observation, habit_formation,
            digital_arrow, heuristic_substitution, context_mechanisms,
            fluency_pathway, communication_grounding, conversation_needs,
            silence_diagnostic]
if __name__ == '__main__':
    for build in BUILDERS:
        build()
        print(build.__name__)
