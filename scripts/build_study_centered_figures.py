#!/usr/bin/env python3
"""Replot published summaries, never simulated participant-level observations.

Requires Python with matplotlib and numpy. Source locations,
reported values, transformations and limitations are written beside the audit.
"""
from pathlib import Path
from html import escape
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'figures'
AUDIT = ROOT / 'audits/study-centered-20260924'
NAVY, BLUE, TEAL, MUTED = '#183047', '#254f77', '#087e8b', '#536879'
GRID, AXIS = '#dce3e8', '#9aabb5'
plt.rcParams.update({'font.family': 'sans-serif', 'font.sans-serif': ['Arial', 'DejaVu Sans'], 'font.size': 19,
    'svg.fonttype': 'none', 'svg.hashsalt': 'study-centered-20260924',
    'text.color': NAVY, 'axes.labelcolor': NAVY, 'xtick.color': MUTED,
    'ytick.color': MUTED, 'axes.edgecolor': AXIS})

def style(ax, ylabel, maximum, step):
    ax.spines[['top', 'right']].set_visible(False)
    ax.set_axisbelow(True)
    ax.grid(axis='y', color=GRID, linewidth=.8)
    ax.set_ylim(0, maximum)
    ax.set_yticks(np.arange(0, maximum + .01, step))
    ax.set_ylabel(ylabel, fontsize=19, labelpad=12)
    ax.tick_params(length=4, pad=8, labelsize=18)
    ax.set_xlim(-.6, 1.6)

def save(fig, stem, title, desc):
    fig.savefig(OUT / (stem + '.png'), dpi=180, facecolor='white')
    p = OUT / (stem + '.svg')
    fig.savefig(p, facecolor='white', metadata={'Date': None})
    plt.close(fig)
    svg = p.read_text()
    idx = svg.index('>', svg.index('<svg')) + 1
    svg = svg[:idx] + '\n<title id="title">' + escape(title) + '</title><desc id="desc">' + escape(desc) + '</desc>\n' + svg[idx:]
    p.write_text(svg.replace('<svg ', '<svg role="img" aria-labelledby="title desc" ', 1))

records = {}

# Two separately randomized experiments. Do not pool or compare their effects.
fig, axs = plt.subplots(2, 1, figsize=(6.8, 9.2))
fig.subplots_adjust(left=.19, right=.96, top=.94, bottom=.10, hspace=.62)
panels = [
    ('A · Using a laptop', ['Taking notes\nonly', 'Notes + unrelated\nonline tasks'], [66,55], [12,11], 20),
    ('B · Seeing nearby laptops', ['No view of\nmultitasking', 'View of\nmultitasking'], [73,56], [12,12], 19),
]
for ax, (title, labels, means, sds, n) in zip(axs, panels):
    sems = np.array(sds) / np.sqrt(n)
    style(ax, 'Test score (%)', 100, 25)
    ax.bar([0,1], means, width=.55, color=[TEAL,BLUE], zorder=3,
           yerr=sems, capsize=5, error_kw={'ecolor':NAVY,'elinewidth':1.3})
    ax.set_xticks([0,1], labels)
    ax.set_title(title, fontsize=20, loc='left', pad=15)
    for x, y, se in zip([0,1], means, sems):
        ax.text(x, y+se+4, f'{y}%', ha='center', fontsize=20, fontweight='bold')
records['study-laptop-distraction'] = {
    'source':'Sana, Weston, & Cepeda (2013), Experiments 1 and 2, pp. 27–29',
    'url':'https://www.yorku.ca/ncepeda/publications/SWC2013.pdf',
    'panels':[{'means_percent':p[2], 'sd_percentage_points':p[3], 'n_per_group':p[4]} for p in panels],
    'uncertainty':'SEM calculated as reported rounded SD / sqrt(n); no individual observations inferred',
    'scope':'Separate experiments; learner note-taking medium differs. No cross-experiment causal comparison.'}
save(fig, 'study-laptop-distraction', 'Laptop multitasking and lecture comprehension',
     'Two experiments by Sana and colleagues (2013). In Experiment 1, mean test scores were 66% for note-taking only and 55% with unrelated online tasks, n=20 per group. In Experiment 2, scores were 73% with no view of multitasking and 56% with a view, n=19 per group. Error bars are standard errors derived from rounded reported standard deviations. The experiments should not be compared as if they were one randomized design.')

fig, ax = plt.subplots(figsize=(6.8, 5.8))
fig.subplots_adjust(left=.18, right=.95, top=.94, bottom=.21)
style(ax, 'Mean percentage', 60, 15)
ax.set_xlim(.85,4.65)
confidence = [33.2,39.2,46.0,52.8]
accuracy = [26.0,23.0,28.4,27.8]
ax.plot([1,2,3,4], confidence, '-o', color=BLUE, lw=2.4, markersize=7)
ax.plot([1,2,3,4], accuracy, '--s', color=TEAL, lw=2.4, markersize=7)
ax.text(4.08,52.8,'52.8',fontsize=18,va='center',color=BLUE)
ax.text(4.08,27.8,'27.8',fontsize=18,va='center',color=TEAL)
ax.text(1.08,43,'Confidence',fontsize=20,color=BLUE)
ax.text(1.18,15,'Accuracy',fontsize=20,color=TEAL)
ax.set_xticks([1,2,3,4],['1','2','3','4'])
ax.set_xlabel('Successive information stages',fontsize=19,labelpad=12)
records['study-confidence-accuracy'] = {
    'source':'Oskamp (1965), Table 2, p. 264',
    'url':'https://faculty.fortlewis.edu/burke_b/Senior/BLINK%20replication/Overconfidence.pdf',
    'n_judges':32,'items_per_stage':25,'accuracy_percent':accuracy,'confidence_percent':confidence,
    'scope':'Repeated judgments about one case. Lines join observed stage means; no smoothing or uncertainty estimates invented.'}
save(fig, 'study-confidence-accuracy', 'Confidence rises as case information accumulates',
     'Oskamp (1965) asked 32 judges to answer the same 25 five-option questions at four stages of information about one case. Accuracy means were 26.0, 23.0, 28.4 and 27.8 percent. Confidence means were 33.2, 39.2, 46.0 and 52.8 percent. The result concerns this case and task, not all additional information.')

fig, ax = plt.subplots(figsize=(6.8, 5.7))
fig.subplots_adjust(left=.17, right=.97, top=.91, bottom=.24)
style(ax, 'Mean donation ($)', 3, 1)
ax.set_xlim(-.6,2.6)
means = [2.38,1.14,1.43]
ax.bar([0,1,2],means,width=.58,color=[TEAL,BLUE,BLUE],zorder=3)
ax.set_xticks([0,1,2],['Identifiable\nchild','Statistics','Child +\nstatistics'])
for x, val in enumerate(means):
    ax.text(x,val+.10,f'${val:.2f}',ha='center',fontsize=20,fontweight='bold')
records['study-donation-information'] = {
    'source':'Small, Loewenstein, & Slovic (2007), Study 3, pp. 148–149 / Figure 3',
    'url':'https://www.cmu.edu/dietrich/sds/docs/loewenstein/SympathyCallous.pdf',
    'n_total':159,'donation_budget_usd':5,'mean_donations_usd':means,
    'scope':'Reported means only; no error bars reconstructed. Child-only exceeds each other condition; statistics versus combined was not statistically distinguished.'}
save(fig, 'study-donation-information', 'Adding statistics can reduce giving to an identifiable child',
     'In Study 3 of Small and colleagues (2007), 159 participants could donate from a five-dollar payment. Mean donations were $2.38 with an identifiable child, $1.14 with statistical information, and $1.43 with both. The child-only condition exceeded both others; the two lower means were not statistically distinguished. These are donation amounts, not measures of informed allocation quality.')

fig, ax = plt.subplots(figsize=(6.8, 5.7))
fig.subplots_adjust(left=.18, right=.96, top=.91, bottom=.24)
style(ax, 'Employees vaccinated (%)', 50, 10)
means = [33.1,37.1]
ax.bar([0,1],means,width=.55,color=[BLUE,TEAL],zorder=3)
ax.set_xticks([0,1],['Clinic\nreminder','Reminder +\ndate-and-time plan'])
for x, val in enumerate(means):
    ax.text(x,val+1.5,f'{val:.1f}%',ha='center',fontsize=20,fontweight='bold')
records['study-vaccination-plans'] = {
    'source':'Milkman et al. (2011), Tables 1–2 (group sizes and clinic vaccination rates)',
    'url':'https://www.hbs.edu/ris/download.aspx?name=implementation_intentions.pdf',
    'raw_vaccination_rates_percent':means,'n_groups':[1268,1270],
    'raw_difference_percentage_points':4.0,
    'adjusted_effect_percentage_points':4.2,'adjusted_95ci_percentage_points':[0.5,7.8],
    'scope':'Control and date-plus-time groups were available at all study sites. Date-only condition omitted because offered at multiday sites only. Raw percentages are distinct from adjusted estimates.'}
save(fig, 'study-vaccination-plans', 'A date-and-time plan increases workplace vaccination uptake',
     'Milkman and colleagues (2011) reported vaccination rates of 33.1% among 1,268 employees receiving a clinic reminder, and 37.1% among 1,270 receiving the reminder plus a prompt to write a date and time. These are raw rates. The covariate-adjusted effect was 4.2 percentage points, with a 95% confidence interval of 0.5 to 7.8 points.')

AUDIT.mkdir(parents=True, exist_ok=True)
(AUDIT / 'figure-data.json').write_text(json.dumps(records, indent=2, ensure_ascii=False)+'\n')
print('Built four study figures and their PNG fallbacks; wrote figure-data.json.')
