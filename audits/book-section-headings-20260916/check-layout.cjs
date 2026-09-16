const fs = require('fs');
const path = require('path');
const {pathToFileURL} = require('url');
const {chromium} = require('playwright');

(async () => {
  const root = path.resolve(__dirname, '../..');
  const targets = [
    {label: 'conformity', file: 'chapters/26-social-norms-and-conformity-when-other-people-become-evidence.html', title: 'Why we conform: informational and normative influence', anchor: 'conformity-is-an-outcome-not-a-mechanism'},
    {label: 'valuation-callout', file: 'chapters/06-valuation-how-options-become-worth-choosing.html', title: 'Research Lens: how interacting brain systems represent value', callout: true},
    {label: 'decision-quality', file: 'chapters/01-how-decisions-should-be-made-and-how-they-actually-are.html', title: 'Evaluate decision quality separately from outcomes', anchor: 'outcome-is-not-process'},
  ].map(t => ({...t, format: 'html', file: path.join(root, 'docs', t.file)}));
  targets.push(...JSON.parse(fs.readFileSync(path.join(__dirname, 'epub-layout-targets.json'))));
  const browser = await chromium.launch({headless: true, executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'});
  const context = await browser.newContext();
  await context.route(/^https?:/, route => route.abort());
  const results = [];
  try {
    for (const target of targets) {
      for (const width of [1440, 390]) {
        const page = await context.newPage();
        await page.setViewportSize({width, height: 1000});
        await page.goto(pathToFileURL(target.file).href + (target.anchor ? '#' + target.anchor : ''), {waitUntil: 'load'});
        await page.addStyleTag({content: 'html,body{scroll-behavior:auto!important;}'});
        await page.evaluate(() => document.fonts.ready);
        const heading = page.locator(target.callout ? '.callout-title-container' : 'h2').filter({hasText: target.title}).first();
        const issues = [];
        if (target.anchor) {
          const anchored = page.locator(`[id="${target.anchor}"]`).first();
          if (!(await anchored.innerText()).includes(target.title)) issues.push('Old anchor does not lead to the new heading');
        }
        if (target.callout) {
          const toggle = heading.locator('..');
          if (await toggle.getAttribute('data-bs-toggle')) await toggle.click();
        }
        if (target.label === 'conformity') {
          const body = await page.locator('body').innerText();
          if (!body.includes('Conformity is the process of adjusting beliefs or behavior')) issues.push('Revised definition missing');
          if (body.includes('Treat conformity as an observed outcome') || body.includes('Conformity is an outcome, not a mechanism')) issues.push('Old conceptual wording remains');
        }
        await heading.evaluate(e => window.scrollTo({top: Math.max(0, e.getBoundingClientRect().top + window.scrollY - (innerWidth < 768 ? 140 : 110)), behavior: 'instant'}));
        const metrics = await heading.evaluate(e => {
          const r = e.getBoundingClientRect();
          return {left: r.left, right: r.right, width: r.width, height: r.height, pageWidth: document.documentElement.scrollWidth, viewportWidth: innerWidth};
        });
        if (metrics.viewportWidth !== width) issues.push('Viewport does not match requested width');
        if (metrics.pageWidth > width + 2) issues.push('Page overflows horizontally');
        if (metrics.left < -2 || metrics.right > width + 2) issues.push('Heading extends beyond viewport');
        const screenshot = `${target.format}-${target.label}-${width}.png`;
        await page.screenshot({path: path.join(__dirname, screenshot)});
        results.push({format: target.format, label: target.label, title: target.title, width, metrics, screenshot, issues});
        console.log(`${target.format} ${target.label} ${width}: ${issues.length ? issues.join('; ') : 'PASS'}`);
        await page.close();
      }
    }
  } finally { await browser.close(); }
  const report = {status: results.some(r => r.issues.length) ? 'FAIL' : 'PASS', results,
    scope: 'Revised normal headings and a callout title at desktop and phone widths. Previous anchors checked. External embeds blocked. EPUB inspected as extracted XHTML; native-reader pagination not tested.'};
  fs.writeFileSync(path.join(__dirname, 'layout-qa.json'), JSON.stringify(report, null, 2) + '\n');
  process.exitCode = report.status === 'PASS' ? 0 : 1;
})().catch(error => {console.error(error); process.exitCode = 1;});
