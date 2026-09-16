const fs = require('fs');
const path = require('path');
const {pathToFileURL} = require('url');
const {chromium} = require('playwright');

(async () => {
  const targets = JSON.parse(fs.readFileSync(path.join(__dirname, 'layout-targets.json')));
  const browser = await chromium.launch({headless: true, executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'});
  const context = await browser.newContext();
  const cache = new Map();
  const results = [];
  const assets = [];
  // Render the actual MathJax formulas, while avoiding unrelated external embeds.
  await context.route(/^https?:/, async route => {
    const url = route.request().url();
    if (!url.startsWith('https://cdn.jsdelivr.net/npm/mathjax@') && !url.startsWith('https://cdn.jsdelivr.net/npm/@mathjax/')) {
      return route.abort();
    }
    if (!cache.has(url)) {
      cache.set(url, (async () => {
        const response = await route.fetch();
        const body = await response.body();
        assets.push({url, status: response.status(), bytes: body.length});
        return {status: response.status(), headers: response.headers(), body};
      })());
    }
    await route.fulfill(await cache.get(url));
  });
  try {
    for (const target of targets) {
      for (const width of [1440, 390]) {
        const page = await context.newPage({viewport: {width, height: 1000}});
        await page.setViewportSize({width, height: 1000});
        await page.goto(pathToFileURL(target.file).href, {waitUntil: 'load', timeout: 45000});
        await page.addStyleTag({content: 'html,body{scroll-behavior:auto!important;}'});
        if (target.format === 'html' && await page.locator('span.math').count()) {
          await page.waitForFunction(() => window.MathJax && window.MathJax.startup && window.MathJax.startup.promise, {timeout: 20000});
          await page.evaluate(() => window.MathJax.startup.promise);
        }
        await page.evaluate(() => document.fonts.ready);
        const boxes = page.locator('.mathematical-analysis');
        const count = await boxes.count();
        const issues = [];
        if (count !== target.boxes) issues.push(`Expected ${target.boxes} boxes, found ${count}`);
        const collapsedWidth = await page.evaluate(() => document.documentElement.scrollWidth);
        if (collapsedWidth > width + 2) issues.push('Main page overflows horizontally');
        for (let i = 0; i < count; i++) {
          const box = boxes.nth(i);
          const toggle = box.locator('[data-bs-toggle="collapse"]').first();
          if (target.format === 'html') {
            if (!(await toggle.count())) issues.push(`Box ${i} has no expansion control`);
            else {
              if (await toggle.getAttribute('aria-expanded') !== 'false') issues.push(`Box ${i} is not initially collapsed`);
              await toggle.click();
              await page.waitForFunction(() => !document.querySelector('.collapsing'));
            }
          }
          const metrics = await box.evaluate(e => ({
            id: e.closest('[id]')?.id || '',
            visible: e.getBoundingClientRect().height > 30,
            math: e.querySelectorAll('span.math, math').length,
            typeset: e.querySelectorAll('mjx-container, math').length,
            mathErrors: e.querySelectorAll('mjx-merror, merror').length,
            pageWidth: document.documentElement.scrollWidth,
          }));
          if (!metrics.visible) issues.push(`Box ${i} not visible after expansion`);
          if (metrics.math && !metrics.typeset) issues.push(`Box ${i} formulas not typeset`);
          if (metrics.mathErrors) issues.push(`Box ${i} has mathematical rendering errors`);
          if (metrics.pageWidth > width + 2) issues.push(`Expanded box ${i} causes page overflow`);
          if (target.screenshot === metrics.id) {
            await box.evaluate(e => window.scrollTo({top: Math.max(0, e.getBoundingClientRect().top + window.scrollY - (innerWidth < 768 ? 110 : 20)), behavior: 'instant'}));
            await page.screenshot({path: path.join(__dirname, `${target.format}-${target.label}-${width}.png`)});
          }
        }
        results.push({format: target.format, label: target.label, width, boxes: count, issues});
        console.log(`${target.format} ${target.label} ${width}: ${issues.length ? issues.join('; ') : 'PASS'}`);
        await page.close();
      }
    }
  } finally {
    await browser.close();
  }
  const report = {status: results.some(r => r.issues.length) ? 'FAIL' : 'PASS', results, mathjaxAssets: assets,
    limit: 'EPUB inspected as extracted XHTML in Chromium; native-reader pagination not tested.'};
  fs.writeFileSync(path.join(__dirname, 'layout-qa.json'), JSON.stringify(report, null, 2) + '\n');
  process.exitCode = report.status === 'FAIL' ? 1 : 0;
})().catch(e => {console.error(e); process.exitCode = 1;});
