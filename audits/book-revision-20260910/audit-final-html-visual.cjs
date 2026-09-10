/** Independent, read-only representative HTML inspection at two reading widths. */
const fs = require('node:fs');
const path = require('node:path');
const {pathToFileURL} = require('node:url');
const {chromium} = require('playwright');

const audit = __dirname;
const root = path.resolve(audit, '../..');
const out = path.join(audit, 'final-html-independent-screenshots');
const targets = [
  ['index', 'index.html', '#fig-master-loop'],
  ['part1', 'parts/part-1.html', 'main img[src$="master-loop-part-1.svg"]'],
  ['chapter4', 'chapters/04-the-predictive-mind-perception-is-inference.html', '#fig-predictive-processing-decision'],
  ['chapter21', 'chapters/21-habits-wanting-and-self-control.html', '#fig-habit-loop'],
  ['chapter40', 'chapters/40-choice-architecture-the-environment-gets-a-vote.html', '#fig-choice-architecture'],
  ['appendixF', 'appendices/appendix-f-when-evidence-breaks.html', '#fig-selected-evidence-pipeline'],
];

(async () => {
  fs.mkdirSync(out, {recursive: true});
  const browser = await chromium.launch({headless: true,
    executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    args: ['--allow-file-access-from-files']});
  const results = [];
  try {
    for (const view of [{name:'desktop', width:1440, height:1080}, {name:'mobile', width:390, height:844}]) {
      const context = await browser.newContext({viewport:{width:view.width,height:view.height},colorScheme:'light'});
      // The audit needs only local rendered files, never remote video/comments.
      await context.route(/^https?:\/\//, route => route.abort());
      const page = await context.newPage();
      for (const [name, file, selector] of targets) {
        await page.goto(pathToFileURL(path.join(root,'docs',file)).href, {waitUntil:'load'});
        await page.waitForFunction(() => [...document.images].every(i=>i.complete));
        await page.evaluate(() => document.fonts.ready);
        await page.evaluate(() => window.scrollTo({top:0,left:0,behavior:'instant'}));
        await page.evaluate(() => new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve))));
        const result = await page.evaluate(({selector, view}) => {
          const main = document.querySelector('main.content') || document.querySelector('main');
          const selected = document.querySelector(selector);
          if (!main || !selected) throw Error('Missing main or selected figure');
          const container = selected.closest('.quarto-figure') || selected.closest('figure') || selected;
          const image = selected.tagName==='IMG' ? selected : selected.querySelector('img');
          const mainRect = main.getBoundingClientRect(), figureRect=container.getBoundingClientRect();
          const pane=image?.closest('div[aria-describedby]');
          return {
            pageWidth:innerWidth,documentWidth:document.documentElement.scrollWidth,scrollY,
            titleY:document.querySelector('h1')?.getBoundingClientRect().y,
            titleHeight:document.querySelector('h1')?.getBoundingClientRect().height,
            main:{x:mainRect.x,width:mainRect.width},
            figure:{x:figureRect.x,y:figureRect.y+scrollY,width:figureRect.width,height:figureRect.height},
            image:image ? {src:image.getAttribute('src'),naturalWidth:image.naturalWidth,naturalHeight:image.naturalHeight,width:image.getBoundingClientRect().width,height:image.getBoundingClientRect().height}:null,
            readingPane:pane ? {clientWidth:pane.clientWidth,scrollWidth:pane.scrollWidth,overflowX:getComputedStyle(pane).overflowX,description:document.getElementById(pane.getAttribute('aria-describedby'))?.textContent}:null,
            unloadedImages:[...document.images].filter(i=>!i.naturalWidth).map(i=>i.getAttribute('src')),
            title:document.querySelector('h1')?.textContent.trim(),
            viewport:view,
          };
        },{selector,view});
        const stem=`${name}-${view.name}`;
        const opening=path.join(out,`${stem}-opening.png`);
        const x=view.name==='desktop' ? Math.max(0,Math.floor(result.main.x)) : 0;
        const width=view.name==='desktop' ? Math.ceil(result.main.width) : view.width;
        await page.screenshot({path:opening,fullPage:true,clip:{x,y:0,width,height:view.height}});
        const figY=Math.max(0,Math.floor(result.figure.y-140));
        const figHeight=Math.ceil(result.figure.height+280);
        const figure=path.join(out,`${stem}-figure-context.png`);
        await page.screenshot({path:figure,fullPage:true,clip:{x,y:figY,width,height:figHeight}});
        let panned=null;
        if (result.readingPane && result.readingPane.scrollWidth > result.readingPane.clientWidth+2) {
          const pan=await page.evaluate(selector=>{
            const e=document.querySelector(selector),image=e.tagName==='IMG'?e:e.querySelector('img');
            const pane=image.closest('div[aria-describedby]');pane.scrollLeft=pane.scrollWidth;
            return {scrollLeft:pane.scrollLeft,maximum:pane.scrollWidth-pane.clientWidth};
          },selector);
          panned=path.join(out,`${stem}-figure-right.png`);
          await page.screenshot({path:panned,fullPage:true,clip:{x,y:figY,width,height:figHeight}});
          result.horizontalPan=pan;
        }
        results.push({name,file,selector,...result,screenshots:{opening,figure,panned}});
      }
      await context.close();
    }
  } finally {await browser.close();}
  fs.writeFileSync(path.join(audit,'final-html-independent-visual-metrics.json'),JSON.stringify({createdUTC:new Date().toISOString(),results},null,2)+'\n');
  console.log(JSON.stringify({pages:targets.length,viewports:2,screenshots:results.reduce((n,r)=>n+2+(r.screenshots.panned?1:0),0),overflow:results.filter(r=>r.documentWidth>r.pageWidth+2).map(r=>r.name+' '+r.viewport.name),unloaded:results.filter(r=>r.unloadedImages.length).map(r=>r.name+' '+r.viewport.name)}));
})().catch(e=>{console.error(e);process.exit(1)});
