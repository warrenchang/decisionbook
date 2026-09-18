const fs = require('fs');
const path = require('path');
const {pathToFileURL} = require('url');
const {chromium} = require('playwright');

const root = path.resolve(__dirname, '../..');
const epub = process.argv[2];
const screenshots = path.join(__dirname, 'screenshots');
fs.mkdirSync(screenshots, {recursive:true});
const targets = {
  35: ['tbl-negotiation-high-low-road', 'tbl-negotiation-principled', 'tbl-negotiation-cultural-goals', 'tbl-negotiation-status-authority'],
  36: ['math-reservation-values', 'tbl-negotiation-range-offers'],
  37: ['vietnamese-prunes', 'tbl-negotiation-sources-of-trade'],
  38: ['tbl-meso-service-menu', 'tbl-mpharm-packages', 'math-mpharm-contract', 'tbl-34-third-party-processes'],
};

(async()=>{
  const browser = await chromium.launch({headless:true, executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'});
  const results = [];
  try {
    const context = await browser.newContext();
    // Only the book's equation renderer may fetch external assets during QA.
    await context.route(/^https?:/, route => /cdn\.jsdelivr\.net\/npm\/(?:mathjax|@mathjax)/.test(route.request().url()) ? route.continue() : route.abort());
    const formats = process.argv[3] ? [process.argv[3]] : epub ? ['html','epub'] : ['html'];
    for (const format of formats) {
      for (const [chapter, ids] of Object.entries(targets)) {
        const file = format === 'html'
          ? path.join(root, 'docs/chapters', fs.readdirSync(path.join(root,'chapters')).find(f=>f.startsWith(chapter+'-')&&f.endsWith('.qmd')).replace(/\.qmd$/, '.html'))
          : path.join(epub, 'EPUB/text', fs.readdirSync(path.join(epub,'EPUB/text')).find(f=>f.endsWith('.xhtml')&&fs.readFileSync(path.join(epub,'EPUB/text',f),'utf8').includes('id="chapter-'+chapter+'-start"')));
        for (const width of [1440,390]) {
          const page = await context.newPage();
          await page.setViewportSize({width,height:1000});
          await page.goto(pathToFileURL(file).href,{waitUntil:'load'});
          await page.evaluate(()=>document.fonts.ready);
          const mathReady = format === 'epub' || await page.evaluate(async()=>{
            if (!document.querySelector('.math')) return true;
            if (!window.MathJax?.startup?.promise) return false;
            await window.MathJax.startup.promise;
            return !!document.querySelector('mjx-container');
          });
          for (const id of ids) {
            const target=page.locator('#'+id);
            if (await target.count() !== 1) throw new Error(`Missing/duplicate ${format} ${id}`);
            if (id.startsWith('math-') && format === 'html') {
              const trigger=target.locator('[data-bs-toggle="collapse"]');
              if (await trigger.count()) {
                if (await trigger.first().getAttribute('aria-expanded') !== 'true') await trigger.first().click();
                await target.locator('.collapse.show').waitFor({state:'visible'});
              }
            }
            await target.scrollIntoViewIfNeeded();
            const metrics=await target.evaluate(e=>{
              const r=e.getBoundingClientRect();
              const imgs=[...document.images].filter(i=>!i.complete||i.naturalWidth===0).map(i=>i.src);
              const cells=[...e.querySelectorAll('th,td')];
              const clipped=cells.filter(c=>c.scrollWidth>c.clientWidth+2 && !['auto','scroll','visible'].includes(getComputedStyle(c).overflowX)).map(c=>c.textContent.trim());
              return {left:r.left,right:r.right,height:r.height,bodyScroll:document.body.scrollWidth,bodyClient:document.body.clientWidth,pageScroll:document.documentElement.scrollWidth,viewport:innerWidth,brokenImages:imgs,clippedCells:clipped,
                tableWidths:[...e.querySelectorAll('table')].map(t=>({width:t.getBoundingClientRect().width,scroll:t.scrollWidth,client:t.clientWidth})),
                mathOverflow:[...e.querySelectorAll('mjx-math, math')].filter(m=>{const b=m.getBoundingClientRect();return b.left<r.left-2||b.right>r.right+2;}).map(m=>m.textContent.trim()),
                mathContainers:e.querySelectorAll('mjx-container, math').length};
            });
            const issues=[];
            if (metrics.bodyScroll>metrics.bodyClient+2) issues.push('Horizontal body overflow');
            if (metrics.left < -2 || metrics.right > width+2) issues.push('Target exceeds viewport');
            if (metrics.brokenImages.length) issues.push('Broken chapter image');
            if (metrics.clippedCells.length) issues.push('Clipped table cells');
            if (id.startsWith('math-') && (!mathReady || !metrics.mathContainers)) issues.push('Math not rendered');
            if (metrics.mathOverflow.length) issues.push('Equation exceeds mathematical box');
            const screenshot=`${format}-${chapter}-${width}-${id}.png`;
            await target.screenshot({path:path.join(screenshots,screenshot)});
            if (width === 390) {
              metrics.horizontalScroll = await target.evaluate(e => {
                const scrollers=[...e.querySelectorAll('*')].filter(t=>t.scrollWidth>t.clientWidth+2&&['auto','scroll'].includes(getComputedStyle(t).overflowX));
                return scrollers.map(t=>{
                  t.scrollLeft=t.scrollWidth;
                  return {element:t.tagName,maximum:t.scrollWidth-t.clientWidth,reached:t.scrollLeft,accessible:t.scrollLeft>=t.scrollWidth-t.clientWidth-2};
                });
              });
              if (metrics.horizontalScroll.some(s=>!s.accessible)) issues.push('Cannot reach horizontally overflowing content');
              if (metrics.horizontalScroll.length) await target.screenshot({path:path.join(screenshots,screenshot.replace('.png','-scroll-end.png'))});
            }
            results.push({format,chapter:Number(chapter),width,id,metrics,issues,screenshot});
            console.log(`${format} ${chapter} ${width} ${id}: ${issues.length?issues.join('; '):'PASS'}`);
          }
          await page.close();
        }
      }
    }
  } finally { await browser.close(); }
  const report={status:results.some(r=>r.issues.length)?'FAIL':'PASS',scope:'New tables, prunes exercise, and expanded mathematical boxes at desktop and phone widths. EPUB inspected as extracted XHTML in Chrome; native-reader pagination not tested.',results};
  fs.writeFileSync(path.join(__dirname,process.argv[3] ? `layout-qa-${process.argv[3]}.json` : 'layout-qa.json'),JSON.stringify(report,null,2)+'\n');
  process.exitCode=report.status==='PASS'?0:1;
})().catch(e=>{console.error(e);process.exitCode=1;});
