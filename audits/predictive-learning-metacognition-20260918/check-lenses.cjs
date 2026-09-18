// Run from the book root with NODE_PATH pointing to a Playwright installation.
const fs=require('fs');
const path=require('path');
const {pathToFileURL}=require('url');
const {chromium}=require('playwright');
const root=process.cwd();
const audit=path.join(root,'audits/predictive-learning-metacognition-20260918');
const targets=[
  {chapter:'04-the-predictive-mind-perception-is-inference',id:'generative-ai-and-predictive-processing',checks:['in-context learning','Lucas et al. (2014)','Nassar et al. (2016)','Boyke et al. (2008)','metacognition']},
  {chapter:'08-fast-and-frugal-thinking',id:'ai-reasoning-and-reflective-thought',checks:['Chain-of-thought prompting','Guo et al., 2025','Tree of Thoughts','Huang et al. (2024)']},
  {chapter:'04-the-predictive-mind-perception-is-inference',id:'research-lens-restored-sight-as-a-bounded-calibration-case',checks:['Shirl Jennings','Held et al., 2011']},
];
(async()=>{
  const browser=await chromium.launch({headless:true,executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'});
  const results=[];
  try {
    for(const width of [1280,390]) {
      const page=await browser.newPage({viewport:{width,height:900}});
      for(const t of targets) {
        await page.goto(pathToFileURL(path.join(root,'docs/chapters',t.chapter+'.html')).href);
        const lens=page.locator('#'+t.id);
        if(await lens.count()!==1)throw Error('Nonunique anchor: '+t.id);
        const header=lens.locator('.callout-header');
        const body=lens.locator('.callout-body').first();
        if(await body.isVisible())throw Error('Should start closed: '+t.id);
        const contents=(await lens.textContent()).replace(/\s+/g,' ');
        for(const text of t.checks)if(!contents.includes(text))throw Error('Missing text: '+text);
        await header.evaluate(n=>window.scrollTo({top:window.scrollY+n.getBoundingClientRect().top-130,behavior:'instant'}));
        await page.screenshot({path:path.join(audit,`${t.id}-closed-${width}.png`)});
        await header.click();
        await body.waitFor({state:'visible'});
        await page.waitForFunction(id=>document.querySelector('#'+id+' .callout-collapse').classList.contains('show'),t.id);
        await page.screenshot({path:path.join(audit,`${t.id}-open-${width}.png`)});
        const dimensions=await page.evaluate(()=>({viewport:innerWidth,document:document.documentElement.scrollWidth}));
        if(dimensions.document>width+1)throw Error('Horizontal overflow: '+JSON.stringify(dimensions));
        await header.click();await body.waitFor({state:'hidden'});
        results.push({id:t.id,width,defaultClosed:true,clickOpens:true,clickCloses:true,textChecks:t.checks.length,...dimensions});
      }
      await page.close();
    }
    fs.writeFileSync(path.join(audit,'browser-checks.json'),JSON.stringify(results,null,2)+'\n');
    console.log(JSON.stringify(results,null,2));
  } finally {await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});
