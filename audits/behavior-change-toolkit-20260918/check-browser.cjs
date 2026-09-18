const fs = require('fs'), path = require('path');
const {pathToFileURL} = require('url');
const {chromium} = require('playwright');

(async () => {
  const out = path.join(process.cwd(), 'audits/behavior-change-toolkit-20260918');
  const chapter = name => pathToFileURL(path.join(process.cwd(), 'docs/chapters', name + '.html')).href;
  const ch39 = '39-behavior-design-make-the-better-action-easier';
  const ch40 = '40-choice-architecture-the-environment-gets-a-vote';
  const ids = ['friction-rewards-and-commitment', 'anchor-action-to-a-prompt', 'temptation-bundling', 'rewards-incentives-and-progress', 'commit-before-temptation', 'social-support-and-accountability', 'tbl-21-1'];
  const capture = new Set(['friction-rewards-and-commitment', 'anchor-action-to-a-prompt', 'temptation-bundling', 'tbl-21-1']);
  const browser = await chromium.launch({headless: true, executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'});
  const checks = [];
  try {
    for (const width of [1280, 390]) {
      const page = await browser.newPage({viewport: {width, height: 1000}});
      await page.goto(chapter(ch39));
      for (const id of ids) {
        const element = page.locator('#' + id);
        if (await element.count() !== 1) throw Error('Missing or duplicate section ' + id);
        if (await element.evaluate(n => !!n.closest('.callout,.collapse,details'))) throw Error('Main text unexpectedly collapsed: ' + id);
        if (capture.has(id)) {
          if (width === 390) {
            await element.evaluate(n => window.scrollTo({top: scrollY + n.getBoundingClientRect().top - 115, behavior: 'instant'}));
            await page.screenshot({path: path.join(out, id + '-' + width + '.png')});
          } else {
            await element.screenshot({path: path.join(out, id + '-' + width + '.png')});
          }
        }
      }
      const table = page.locator('#tbl-21-1 table');
      const rows = await table.locator('tbody > tr').count();
      if (rows !== 17) throw Error('Toolkit rows did not render correctly');
      const dimensions = await page.evaluate(() => ({viewport: innerWidth, pageWidth: document.documentElement.scrollWidth}));
      const tableDimensions = await table.evaluate(n => ({width: n.getBoundingClientRect().width, scrollWidth: n.scrollWidth, clientWidth: n.clientWidth}));
      if (dimensions.pageWidth > width + 1 || tableDimensions.width > width || tableDimensions.scrollWidth > tableDimensions.clientWidth + 1) throw Error('Horizontal overflow');
      await page.goto(chapter(ch40));
      const link = page.locator('main a[href$="#temptation-bundling"]');
      if (await link.count() !== 1) throw Error('Chapter 40 link missing');
      await page.goto(new URL(await link.getAttribute('href'), page.url()).href);
      if (await page.locator('#temptation-bundling').count() !== 1) throw Error('Chapter 40 link unresolved');
      checks.push({...dimensions, tableDimensions, toolkitRows: rows, visibleSections: ids, chapter40LinkResolved: true});
      await page.close();
    }
    fs.writeFileSync(path.join(out, 'browser-checks.json'), JSON.stringify(checks, null, 2) + '\n');
    console.log(JSON.stringify(checks, null, 2));
  } finally { await browser.close(); }
})().catch(error => {console.error(error); process.exitCode = 1;});
