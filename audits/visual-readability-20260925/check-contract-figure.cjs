const fs = require('node:fs');
const path = require('node:path');
const { chromium } = require('playwright');
const root = path.resolve(__dirname, '../..');
(async () => {
  const svg = fs.readFileSync(path.join(root, 'figures/contract-state-payoffs.svg'), 'utf8');
  const browser = await chromium.launch({headless: true, executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'});
  const records = [];
  try {
    for (const width of [760, 350]) {
      const page = await browser.newPage({viewport: {width, height: Math.ceil(width * 680/760)}, deviceScaleFactor: 1});
      await page.route('**/*', route => route.abort());
      await page.setContent(`<html><head><style>html,body{margin:0;background:white}svg{display:block;width:100%;height:auto}</style></head><body>${svg}</body></html>`);
      await page.evaluate(() => document.fonts.ready);
      const checks = await page.evaluate(() => {
        const svg = document.querySelector('svg');
        const scale = svg.getBoundingClientRect().width / 760;
        const texts = [...svg.querySelectorAll('text')];
        return {
          minimumLabelPixels: Math.min(...texts.map(t => parseFloat(getComputedStyle(t).fontSize) * scale)),
          clipped: texts.filter(t => {const b=t.getBBox();return b.x<0 || b.y<0 || b.x+b.width>760 || b.y+b.height>680;}).map(t=>t.textContent)
        };
      });
      if (checks.clipped.length || checks.minimumLabelPixels < 12) throw new Error(JSON.stringify(checks));
      await page.screenshot({path: path.join(__dirname, `contract-state-payoffs-${width}.png`)});
      records.push({width, ...checks});
      await page.close();
    }
    fs.writeFileSync(path.join(__dirname,'contract-figure-checks.json'), JSON.stringify(records,null,2)+'\n');
  } finally {await browser.close();}
})().catch(error => {console.error(error);process.exitCode=1;});
