const fs = require('node:fs');
const path = require('node:path');
const {pathToFileURL} = require('node:url');
const {chromium} = require('playwright');
const mode = process.argv[2];
const file = path.resolve(process.argv[3]);
const output = path.resolve('audits/ch13-familiarity-studies-20260919');
const ids = ['language-beauty-and-familiarity','flavor-learning-before-birth','repetition-and-perceived-truth'];
(async () => {
  const browser = await chromium.launch({executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless:true});
  const records=[];
  try {
    for (const width of [mode==='html'?1280:768,390]) {
      const height=width===390?844:1400;
      const context=await browser.newContext({viewport:{width,height},colorScheme:'light'});
      const page=await context.newPage();
      await page.goto(pathToFileURL(file).href,{waitUntil:'networkidle'});
      await page.evaluate(()=>document.fonts.ready);
      let previousTop=-1;
      for (const id of ids) {
        const target=page.locator('#'+id);
        if(await target.count()!==1) throw new Error('Missing or duplicate anchor: '+id);
        const record=await target.evaluate(n=>{
          const r=n.getBoundingClientRect();
          return {id:n.id,top:scrollY+r.top,width:r.width,height:r.height,text:n.textContent.trim(),insideCallout:!!n.closest('.callout'),scrollWidth:n.scrollWidth,clientWidth:n.clientWidth};
        });
        if(record.insideCallout) throw new Error('New discussion is collapsed: '+id);
        if(record.top<=previousTop) throw new Error('Unexpected section order: '+id);
        if(record.scrollWidth>record.clientWidth+3) throw new Error('Section overflow: '+id);
        previousTop=record.top;
        records.push({mode,viewport:width,...record});
        if(width===390) {
          const inset=mode==='html'?110:15;
          for(let offset=0,part=1;offset<record.height;offset+=height-inset-55,part++) {
            await page.evaluate(({top,offset,inset})=>scrollTo({top:top+offset-inset,behavior:'instant'}),{top:record.top,offset,inset});
            await page.screenshot({path:path.join(output,`${mode}-${width}-${id}-${part}.png`)});
          }
        } else {
          await target.screenshot({path:path.join(output,`${mode}-${width}-${id}.png`)});
        }
      }
      await context.close();
    }
    fs.writeFileSync(path.join(output,`${mode}-sections-qa.json`),JSON.stringify({status:'PASS',records},null,2)+'\n');
    console.log(`PASS: ${mode}; new discussions in main text, followed by illusory truth; no section overflow at either width.`);
  } finally {await browser.close();}
})().catch(e=>{console.error(e);process.exit(1);});
