const fs = require('fs'), path = require('path');
const {pathToFileURL} = require('url');
const {chromium} = require('playwright');

(async () => {
  const out = path.join(process.cwd(), 'audits/habit-response-replacement-20260918');
  const browser = await chromium.launch({headless: true, executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'});
  const targets = [
    {file: '21-habits-wanting-and-self-control', id: 'give-a-familiar-cue-a-new-response', link: 'implementation-intentions'},
    {file: '39-behavior-design-make-the-better-action-easier', id: 'implementation-intentions', link: 'give-a-familiar-cue-a-new-response'}
  ];
  const checks = [];
  try {
    for (const width of [1280, 390]) for (const target of targets) {
      const page = await browser.newPage({viewport: {width, height: 1000}});
      await page.goto(pathToFileURL(path.join(process.cwd(), 'docs/chapters', target.file + '.html')).href);
      const section = page.locator('#' + target.id);
      if (await section.count() !== 1) throw Error('Missing or duplicate section: ' + target.id);
      if (await section.evaluate(n => !!n.closest('.callout,.collapse,details'))) throw Error('Main text unexpectedly collapsed');
      if (target.file.startsWith('21-')) {
        if (await page.locator('#give-the-pause-a-different-response').count() !== 1) throw Error('Legacy anchor missing');
        if (await section.locator(':scope > ol > li').count() !== 5) throw Error('Replacement sequence did not render as five steps');
      }
      if (width === 390) {
        await section.evaluate(n => window.scrollTo({top: scrollY + n.getBoundingClientRect().top - 115, behavior: 'instant'}));
        await page.screenshot({path: path.join(out, target.id + '-' + width + '.png')});
      } else {
        await section.screenshot({path: path.join(out, target.id + '-' + width + '.png')});
      }
      const dimensions = await page.evaluate(() => ({viewport: innerWidth, pageWidth: document.documentElement.scrollWidth}));
      if (dimensions.pageWidth > width + 1) throw Error('Horizontal page overflow');
      const link = section.locator('a[href$="#' + target.link + '"]');
      if (await link.count() !== 1) throw Error('Missing or duplicate cross-reference');
      await page.goto(new URL(await link.getAttribute('href'), page.url()).href);
      if (await page.locator('#' + target.link).count() !== 1) throw Error('Cross-reference target missing');
      checks.push({chapter: target.file, mainTextVisible: true, crossReferenceResolved: true, ...dimensions});
      await page.close();
    }
    fs.writeFileSync(path.join(out, 'browser-checks.json'), JSON.stringify(checks, null, 2) + '\n');
    console.log(JSON.stringify(checks, null, 2));
  } finally { await browser.close(); }
})().catch(error => {console.error(error); process.exitCode = 1;});
