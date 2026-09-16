const fs = require('fs');
const path = require('path');
const {pathToFileURL} = require('url');
const {chromium} = require('playwright');

(async () => {
  const root = path.resolve(__dirname, '../..');
  const targets = [
    {label: 'asch', file: 'chapters/26-social-norms-and-conformity-when-other-people-become-evidence.html', text: 'Asch’s line-judgment studies', values: ['36.8%', '0.7%']},
    {label: 'cooperation', file: 'chapters/25-cooperation-and-social-preferences-self-interest-is-not-the-only-payoff.html', text: 'A social cue can also suggest an audience', values: ['5.39', '4.17']},
    {label: 'choice', file: 'chapters/40-choice-architecture-the-environment-gets-a-vote.html', text: 'Choice overload occurs', values: ['30%', '3%']},
  ].map(t => ({...t, format: 'html', file: path.join(root, 'docs', t.file)}));
  const epubTargets = path.join(__dirname, 'epub-layout-targets.json');
  if (fs.existsSync(epubTargets)) targets.push(...JSON.parse(fs.readFileSync(epubTargets)));
  const browser = await chromium.launch({headless: true, executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'});
  const context = await browser.newContext();
  await context.route(/^https?:/, route => route.abort());
  const results = [];
  try {
    for (const target of targets) {
      for (const width of [1440, 390]) {
        const page = await context.newPage();
        await page.setViewportSize({width, height: 1000});
        await page.goto(pathToFileURL(target.file).href, {waitUntil: 'load'});
        await page.addStyleTag({content: 'html,body{scroll-behavior:auto!important;}'});
        await page.evaluate(() => document.fonts.ready);
        const paragraph = page.locator('p').filter({hasText: target.text}).first();
        const text = await paragraph.innerText();
        const issues = [];
        for (const value of target.values) if (!text.includes(value)) issues.push(`Missing result ${value}`);
        const removed = [
          'The first percentage describes responses across trials',
          'This measured contributions, not the percentage of people cooperating',
          'These are purchase rates among visitors to the booth, not all shoppers',
        ];
        const body = await page.locator('body').innerText();
        for (const sentence of removed) if (body.includes(sentence)) issues.push('Removed caveat remains');
        await paragraph.evaluate(e => window.scrollTo({top: Math.max(0, e.getBoundingClientRect().top + window.scrollY - (innerWidth < 768 ? 140 : 110)), behavior: 'instant'}));
        const metrics = await paragraph.evaluate(e => {
          const rect = e.getBoundingClientRect();
          return {left: rect.left, right: rect.right, width: rect.width, pageWidth: document.documentElement.scrollWidth, viewportWidth: innerWidth};
        });
        if (metrics.viewportWidth !== width) issues.push('Viewport does not match the requested width');
        if (metrics.pageWidth > width + 2) issues.push('Page overflows horizontally');
        if (metrics.left < -2 || metrics.right > width + 2) issues.push('Paragraph extends beyond viewport');
        const screenshot = `${target.format}-${target.label}-${width}.png`;
        await page.screenshot({path: path.join(__dirname, screenshot)});
        results.push({format: target.format, label: target.label, width, metrics, screenshot, issues});
        console.log(`${target.format} ${target.label} ${width}: ${issues.length ? issues.join('; ') : 'PASS'}`);
        await page.close();
      }
    }
  } finally { await browser.close(); }
  const report = {status: results.some(r => r.issues.length) ? 'FAIL' : 'PASS', results,
    scope: 'Representative edited prose at desktop and phone widths. External embeds blocked. EPUB inspected as extracted XHTML; native-reader pagination not tested.'};
  fs.writeFileSync(path.join(__dirname, 'layout-qa.json'), JSON.stringify(report, null, 2) + '\n');
  process.exitCode = report.status === 'PASS' ? 0 : 1;
})().catch(error => {console.error(error); process.exitCode = 1;});
