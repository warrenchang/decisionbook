// Inspect the final source and its actual HTML / extracted EPUB containers.
const fs = require('node:fs');
const path = require('node:path');
const { pathToFileURL } = require('node:url');
const { chromium } = require('playwright');
const root = path.resolve(__dirname, '../..');

(async () => {
  const browser = await chromium.launch({headless: true, executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'});
  const results = [];
  try {
    const source = fs.readFileSync(path.join(root, 'figures/pareto.svg'), 'utf8');
    for (const width of [760, 340]) {
      const page = await browser.newPage({viewport: {width, height: width}, deviceScaleFactor: 1});
      await page.setContent(`<html><body style="margin:0">${source}</body></html>`);
      await page.addStyleTag({content: 'svg {width:100%;height:auto;display:block}'});
      await page.evaluate(() => document.fonts.ready);
      const texts = await page.locator('svg text').evaluateAll(nodes => nodes.map(node => {
        const box = node.getBoundingClientRect();
        const scale = node.ownerSVGElement.getBoundingClientRect().width / 760;
        return {text: node.textContent, x: box.x, y: box.y, right: box.right, bottom: box.bottom, cssFont: parseFloat(getComputedStyle(node).fontSize) * scale};
      }));
      const clipped = texts.filter(text => text.x < 0 || text.y < 0 || text.right > width || text.bottom > width);
      if (clipped.length) throw Error(JSON.stringify(clipped));
      if (Math.min(...texts.map(text => text.cssFont)) < 12) throw Error('Source text too small');
      await page.screenshot({path: path.join(__dirname, `source-${width}.png`)});
      results.push({kind:'source', width, clipped, smallestText: Math.min(...texts.map(text => text.cssFont))});
      await page.close();
    }
    const destinations = [{kind:'html', file:path.join(root, 'docs/chapters/37-creating-value-across-differences.html')}];
    if (process.argv[2]) {
      const epubRoot = path.resolve(process.argv[2]);
      const findChapter = dir => fs.readdirSync(dir, {withFileTypes:true}).flatMap(entry => {
        const file = path.join(dir, entry.name);
        return entry.isDirectory() ? findChapter(file) : /\.xhtml$/.test(file) && fs.readFileSync(file, 'utf8').includes('id="fig-pareto"') ? [file] : [];
      });
      const chapters = findChapter(epubRoot);
      if (chapters.length !== 1) throw Error('Expected one EPUB chapter with fig-pareto');
      destinations.push({kind:'epub', file:chapters[0]});
    }
    for (const destination of destinations) for (const width of [1280, 390]) {
      const page = await browser.newPage({viewport:{width, height:1000}, deviceScaleFactor:1});
      await page.goto(pathToFileURL(destination.file).href, {waitUntil:'load'});
      await page.evaluate(() => document.fonts.ready);
      const figure = page.locator('#fig-pareto');
      await figure.scrollIntoViewIfNeeded();
      const metrics = await figure.evaluate(node => {
        const img = node.querySelector('img');
        const box = img.getBoundingClientRect();
        return {caption:node.innerText, image:img.src, loaded:img.complete && img.naturalWidth > 0, width:box.width, height:box.height, left:box.left, right:box.right, windowWidth:innerWidth, pageWidth:document.documentElement.scrollWidth, alt:img.alt, class:img.className};
      });
      if (!metrics.loaded || !metrics.caption.includes('37.2') || !metrics.alt.includes('square plot')) throw Error(JSON.stringify(metrics));
      // object-fit:contain can place a square image inside a wider desktop box.
      metrics.smallestText = 28 * Math.min(metrics.width, metrics.height) / 760;
      if (metrics.left < -1 || metrics.right > width + 1 || metrics.smallestText < 12) throw Error(JSON.stringify(metrics));
      await figure.screenshot({path:path.join(__dirname, `${destination.kind}-${width}.png`)});
      results.push({kind:destination.kind, viewport:width, ...metrics});
      await page.close();
    }
    fs.writeFileSync(path.join(__dirname, 'layout-check.json'), JSON.stringify(results, null, 2) + '\n');
    console.log(JSON.stringify(results.map(({kind,width,viewport,smallestText}) => ({kind,width,viewport,smallestText})), null, 2));
  } finally { await browser.close(); }
})().catch(error => {console.error(error);process.exitCode = 1;});
