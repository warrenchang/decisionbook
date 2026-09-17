const fs = require('fs');
const path = require('path');
const {pathToFileURL} = require('url');
const {chromium} = require('playwright');

(async () => {
  const root = path.resolve(__dirname, '../..');
  const selections = JSON.parse(fs.readFileSync(path.join(__dirname, 'epigraph-selections.json')));
  const targets = selections.filter(s => [1, 22, 27, 29].includes(s.chapter)).map(s => ({
    chapter: s.chapter, quote: s.quote, format: 'html',
    file: path.join(root, 'docs', s.source.replace(/\.qmd$/, '.html')),
  }));
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
        await page.goto(pathToFileURL(target.file).href, {waitUntil: 'load'});
        await page.evaluate(() => document.fonts.ready);
        const box = page.locator('.chapter-epigraph');
        const issues = [];
        if (await box.count() !== 1) issues.push('Expected one opening quotation');
        const text = await box.innerText();
        const norm = s => s.replace(/[’‘]/g, "'").replace(/[“”]/g, '"').replace(/\s+/g, ' ').trim();
        if (!norm(text).includes(norm(target.quote))) issues.push('Selected quotation missing');
        const metrics = await box.evaluate(e => {
          const r = e.getBoundingClientRect();
          const heading = document.querySelector('main h1, body h1');
          const h = heading?.getBoundingClientRect();
          return {left: r.left, right: r.right, top: r.top, bottom: r.bottom, height: r.height,
            headingBottom: h?.bottom, pageWidth: document.documentElement.scrollWidth, viewportWidth: innerWidth};
        });
        if (metrics.viewportWidth !== width) issues.push('Viewport does not match requested width');
        if (metrics.pageWidth > width + 2) issues.push('Page overflows horizontally');
        if (metrics.left < -2 || metrics.right > width + 2) issues.push('Quotation extends beyond viewport');
        if (metrics.headingBottom && metrics.top < metrics.headingBottom - 1) issues.push('Quotation overlaps chapter title');
        const screenshot = `${target.format}-chapter-${target.chapter}-${width}.png`;
        await page.screenshot({path: path.join(__dirname, screenshot)});
        results.push({format: target.format, chapter: target.chapter, width, metrics, screenshot, issues});
        console.log(`${target.format} chapter ${target.chapter} ${width}: ${issues.length ? issues.join('; ') : 'PASS'}`);
        await page.close();
      }
    }
  } finally { await browser.close(); }
  const report = {status: results.some(r => r.issues.length) ? 'FAIL' : 'PASS', results,
    scope: 'Chapter titles, quotations, and attribution wrapping at desktop and phone widths. External requests blocked. EPUB rendered as extracted XHTML; native-reader pagination not tested.'};
  fs.writeFileSync(path.join(__dirname, 'layout-qa.json'), JSON.stringify(report, null, 2) + '\n');
  process.exitCode = report.status === 'PASS' ? 0 : 1;
})().catch(error => {console.error(error); process.exitCode = 1;});
