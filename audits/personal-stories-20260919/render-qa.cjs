const fs = require('node:fs');
const path = require('node:path');
const {pathToFileURL} = require('node:url');
const {chromium} = require('playwright');
(async () => {
  const out = path.resolve('audits/personal-stories-20260919');
  const files = fs.readdirSync('chapters').filter(f => /^(04|08|12|17|21|40)-.*\.qmd$/.test(f)).map(f => f.replace(/\.qmd$/,'.html'));
  if (files.length !== 6) throw Error('Expected six revised chapters');
  const browser = await chromium.launch({executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless:true});
  const records = [];
  try {
    for (const width of [1280,390]) {
      const page = await browser.newPage({viewport:{width,height:1000},colorScheme:'light'});
      let boxes = 0;
      for (const file of files) {
        await page.goto(pathToFileURL(path.resolve('docs/chapters',file)).href,{waitUntil:'networkidle'});
        await page.evaluate(() => document.fonts.ready);
        const stats = await page.locator('.personal-example').evaluateAll(nodes => nodes.map(n => ({
          title:n.querySelector('.callout-title-container')?.textContent.trim(),
          text:n.textContent.replace(/\s+/g,' ').trim(),
          overflow:n.scrollWidth > n.clientWidth + 2,
          collapsed:!!n.querySelector('.collapse'),
          images:[...n.querySelectorAll('img')].map(i=>({loaded:i.complete && i.naturalWidth>0}))
        })));
        for (const s of stats) {
          if (!s.title?.includes('From my experience:') || s.overflow || s.collapsed || s.images.some(i=>!i.loaded)) throw Error(JSON.stringify({file,width,...s}));
        }
        if (await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth+2)) throw Error('Page overflows: '+file+' '+width);
        boxes += stats.length;
        records.push({file,width,boxes:stats});
        await page.addStyleTag({content:'#quarto-header, .quarto-secondary-nav { visibility:hidden !important; }'});
        for (const id of ['personal-story-leaving-the-park','personal-story-cola']) {
          const node = page.locator('#'+id);
          if (await node.count()) await node.screenshot({path:path.join(out,`${id}-${width}.png`)});
        }
        if(file.startsWith('08-') && width===390) await page.locator('.personal-example').screenshot({path:path.join(out,'counting-mobile.png')});
      }
      if (boxes!==7) throw Error('Expected seven boxes, got '+boxes);
      await page.close();
    }
    fs.writeFileSync(path.join(out,'browser-qa.json'),JSON.stringify({status:'PASS',records},null,2)+'\n');
    console.log('PASS: seven labeled, expanded personal story boxes; six chapters at desktop and mobile widths; no overflow or missing images.');
  } finally {await browser.close();}
})().catch(e=>{console.error(e);process.exit(1)});
