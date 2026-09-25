// Standalone figure QA; destination HTML/EPUB checks are run by the book build.
const fs = require('node:fs');
const path = require('node:path');
const {chromium} = require('playwright');
const root = path.resolve(__dirname, '../..');
const figures = ['cold-water-better-ending', 'stag-hunt-belief-payoffs'];
(async () => {
  const browser = await chromium.launch({headless:true,
    executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'});
  const records=[];
  try {
    for (const stem of figures) for (const width of [760,350]) {
      const page = await browser.newPage({viewport:{width:width+40,height:1000},deviceScaleFactor:1});
      await page.route('**/*', route=>route.abort());
      const svg = fs.readFileSync(path.join(root,'figures',stem+'.svg'),'utf8');
      await page.setContent(`<style>body{margin:20px;background:white}svg{display:block;width:${width}px;height:auto}</style>${svg}`);
      await page.evaluate(()=>document.fonts.ready);
      const metrics=await page.evaluate(()=>{
        const svg=document.querySelector('svg'), bounds=svg.getBoundingClientRect();
        const labels=[...svg.querySelectorAll('text')].map(el=>{
          const r=el.getBoundingClientRect(),m=el.getScreenCTM();
          return {text:el.textContent, renderedFont:parseFloat(getComputedStyle(el).fontSize)*Math.hypot(m.a,m.b),
            contained:r.left>=bounds.left-.1 && r.top>=bounds.top-.1 && r.right<=bounds.right+.1 && r.bottom<=bounds.bottom+.1};
        });
        return {width:bounds.width,height:bounds.height,minimumFont:Math.min(...labels.map(x=>x.renderedFont)),labels};
      });
      await page.locator('svg').screenshot({path:path.join(__dirname,`${stem}-${width}.png`)});
      records.push({stem,...metrics});
      if(metrics.minimumFont<12 || metrics.labels.some(x=>!x.contained)) throw Error(JSON.stringify(records.at(-1)));
      await page.close();
    }
    fs.writeFileSync(path.join(__dirname,'coordination-experience-standalone-qa.json'),JSON.stringify(records,null,2)+'\n');
    console.log('Both figures: text contained, minimum font >=12px at widths 760 and350.');
  } finally {await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});
