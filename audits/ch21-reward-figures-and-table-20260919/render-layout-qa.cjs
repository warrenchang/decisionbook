const fs = require('node:fs');
const path = require('node:path');
const {pathToFileURL} = require('node:url');
const {chromium} = require('playwright');
const mode = process.argv[2];
const file = path.resolve(process.argv[3]);
const output = path.resolve('audits/ch21-reward-figures-and-table-20260919');
const ids = ['tbl-wanting-liking','fig-reward-prediction-error-shift','fig-reward-uncertainty-comparison'];
(async () => {
  const browser = await chromium.launch({executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless:true});
  const records=[];
  try {
    for (const width of [mode==='html'?1280:768,390]) {
      const height=width===390?844:1600;
      const context=await browser.newContext({viewport:{width,height},colorScheme:'light'});
      const page=await context.newPage();
      await page.goto(pathToFileURL(file).href,{waitUntil:'networkidle'});
      await page.evaluate(async()=>{await document.fonts.ready; await Promise.all([...document.images].map(i=>i.decode().catch(()=>{})));});
      const oldImage=await page.locator('img[src*="wanting-liking"]').count();
      if(oldImage) throw new Error('Obsolete wanting-liking illustration remains');
      for (const id of ids) {
        const target=page.locator('#'+id);
        if(await target.count()!==1) throw new Error('Identifier not unique: '+id);
        const record=await target.evaluate(n=>{
          const r=n.getBoundingClientRect(), image=n.querySelector('img'), table=n.querySelector('table');
          return {id:n.id,insideCallout:!!n.closest('.callout'),width:r.width,height:r.height,
            image:image?{src:image.getAttribute('src'),width:image.getBoundingClientRect().width,naturalWidth:image.naturalWidth}:null,
            table:table?{columns:table.querySelector('thead tr').children.length,rows:table.querySelectorAll('tbody tr').length,width:table.clientWidth,scrollWidth:table.scrollWidth,fontSize:getComputedStyle(table).fontSize}:null,
            caption:n.querySelector('figcaption')?.textContent.trim(),
            overflow:[...n.querySelectorAll('*')].filter(e=>e.scrollWidth>e.clientWidth+3 && getComputedStyle(e).overflowX!=='auto' && e.clientWidth>0).slice(0,6).map(e=>({tag:e.tagName,width:e.clientWidth,scrollWidth:e.scrollWidth}))};
        });
        if(record.insideCallout) throw new Error('Main-text item remains in callout: '+id);
        if(record.image && !record.image.naturalWidth) throw new Error('Broken image: '+id);
        if(record.table && record.table.scrollWidth>record.table.width+3) throw new Error('Table needs horizontal scrolling: '+JSON.stringify(record.table));
        if(record.image?.src.endsWith('.svg')) {
          const svg=fs.readFileSync(path.resolve(path.dirname(file),record.image.src),'utf8');
          const vb=svg.match(/viewBox="([^"]+)"/)[1].split(/\s+/).map(Number);
          const sizes=[...svg.matchAll(/font-size:\s*([\d.]+)px/g)].map(m=>Number(m[1]));
          record.image.minLabelPx=Math.min(...sizes)*record.image.width/vb[2];
          if(record.image.minLabelPx<12) throw new Error('Labels too small: '+id);
        }
        records.push({mode,viewport:width,...record});
        if(width===390) {
          const top=await target.evaluate(n=>scrollY+n.getBoundingClientRect().top);
          const inset=mode==='html'?110:15;
          const step=height-inset-55;
          for(let offset=0,part=1;offset<record.height;offset+=step,part++) {
            await page.evaluate(({top,offset,inset})=>scrollTo({top:top+offset-inset,behavior:'instant'}),{top,offset,inset});
            await page.screenshot({path:path.join(output,`${mode}-${width}-${id}-${part}.png`)});
          }
        } else {
          await target.screenshot({path:path.join(output,`${mode}-${width}-${id}.png`)});
        }
      }
      await context.close();
    }
    fs.writeFileSync(path.join(output,`${mode}-layout-qa.json`),JSON.stringify({status:'PASS',records},null,2)+'\n');
    console.log(`PASS: ${mode}, all three items in main text; readable labels and no horizontal table scrolling at both widths.`);
  } finally {await browser.close();}
})().catch(e=>{console.error(e);process.exit(1);});
