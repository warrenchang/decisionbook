const fs = require('node:fs');
const path = require('node:path');
const {pathToFileURL} = require('node:url');
const {chromium} = require('playwright');
const root = path.resolve(__dirname, '../..');
const ids = ['lie-detection', 'replace-lie-detection-with-claim-verification'];

(async () => {
  const destinations = [
    {kind:'html', file:path.join(root, 'docs/chapters/33-communication-language-is-not-a-file-transfer.html'), id:ids[0]},
    {kind:'html', file:path.join(root, 'docs/chapters/38-designing-better-agreements.html'), id:ids[1]},
  ];
  if (process.argv[2]) {
    const find = dir => fs.readdirSync(dir, {withFileTypes:true}).flatMap(e => e.isDirectory() ? find(path.join(dir,e.name)) : e.name.endsWith('.xhtml') ? [path.join(dir,e.name)] : []);
    const files = find(path.resolve(process.argv[2]));
    for (const id of ids) {
      const matches = files.filter(file => fs.readFileSync(file,'utf8').includes(`id="${id}"`));
      if (matches.length !== 1) throw Error(`Expected one EPUB destination for ${id}`);
      destinations.push({kind:'epub', file:matches[0], id});
    }
  }
  const browser = await chromium.launch({headless:true, executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'});
  const results = [];
  try {
    for (const target of destinations) for (const width of [1280,390]) {
      const page = await browser.newPage({viewport:{width,height:900}, deviceScaleFactor:1});
      await page.goto(pathToFileURL(target.file).href, {waitUntil:'load'});
      await page.evaluate(() => document.fonts.ready);
      const section = page.locator(`[id="${target.id}"]`);
      const heading = section.locator('h3').first();
      const title = await heading.innerText();
      await heading.evaluate(node => window.scrollTo({top:window.scrollY + node.getBoundingClientRect().top - 110, behavior:'instant'}));
      await page.waitForFunction(id => {
        const top = document.querySelector(`[id="${id}"] h3`).getBoundingClientRect().top;
        return top >= 90 && top <= 130;
      }, target.id);
      await page.screenshot({path:path.join(__dirname,`${target.kind}-${target.id}-${width}.png`)});
      const metrics = await section.evaluate(node => ({width:node.getBoundingClientRect().width,pageWidth:document.documentElement.scrollWidth,viewport:innerWidth,links:[...node.querySelectorAll('a[href]')].map(a=>a.getAttribute('href'))}));
      if (metrics.pageWidth > width + 1) throw Error(JSON.stringify(metrics));
      if (target.id === 'lie-detection') {
        const figure = page.locator('#fig-lie-cues-belief-gap');
        const caption = await figure.locator('figcaption').innerText();
        if (!caption.includes('33.4')) throw Error(caption);
        const img = figure.locator('img');
        if (!(await img.evaluate(node => node.complete && node.naturalWidth > 0))) throw Error('Figure not loaded');
        const figureStyle = '#quarto-header, .quarto-secondary-nav {visibility:hidden!important}';
        await figure.screenshot({path:path.join(__dirname,`${target.kind}-figure-${width}.png`),style:figureStyle});
        metrics.figureCaption = caption;
        metrics.scrollPane = await figure.locator('div[aria-describedby]').evaluate(node => ({clientWidth:node.clientWidth,scrollWidth:node.scrollWidth,overflow:getComputedStyle(node).overflowX}));
        if (width === 390 && metrics.scrollPane.scrollWidth > metrics.scrollPane.clientWidth) {
          await figure.locator('div[aria-describedby]').evaluate(node => {node.scrollLeft = node.scrollWidth;});
          await figure.screenshot({path:path.join(__dirname,`${target.kind}-figure-${width}-right.png`),style:figureStyle});
        }
      } else if (await page.locator('#fig-lie-cues-belief-gap').count()) throw Error('Figure duplicated in Chapter 38');
      results.push({kind:target.kind,id:target.id,title,...metrics});
      await page.close();
    }
    fs.writeFileSync(path.join(__dirname,'layout-check.json'),JSON.stringify(results,null,2)+'\n');
    console.log(`PASS: ${results.length} section layouts; figure numbered 33.4 and absent from Chapter 38.`);
  } finally {await browser.close();}
})().catch(error=>{console.error(error);process.exitCode=1;});
