// Local SVG containment and type-size checks, plus narrow screenshots.
const fs=require('fs'),path=require('path'),{chromium}=require('playwright');
const root=path.resolve(__dirname,'../..');
const names=['elaboration-quadrant'];
(async()=>{
 const browser=await chromium.launch({headless:true,executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'});
 const records=[];
 try {
  for(const stem of names){
   const svg=fs.readFileSync(path.join(root,'figures',stem+'.svg'),'utf8');
   const [,,w,h]=svg.match(/viewBox="([^"]+)"/)[1].split(' ').map(Number);
   for(const width of [780,350]){
    const page=await browser.newPage({viewport:{width,height:Math.ceil(width*h/w)},deviceScaleFactor:1});
    await page.route('**/*',r=>r.abort());
    await page.setContent('<style>html,body{margin:0;background:white}svg{display:block;width:100%;height:auto}</style>'+svg);
    await page.evaluate(()=>document.fonts.ready);
    const metrics=await page.evaluate(()=>{
     const svg=document.querySelector('svg'),box=svg.getBoundingClientRect(),scale=box.width/svg.viewBox.baseVal.width;
     const labels=[...svg.querySelectorAll('text')];
     return {minimumLabelPixels:Math.min(...labels.map(t=>parseFloat(getComputedStyle(t).fontSize)*scale)),clipped:labels.filter(t=>{const b=t.getBoundingClientRect();return b.left<box.left-.5||b.top<box.top-.5||b.right>box.right+.5||b.bottom>box.bottom+.5}).map(t=>t.textContent)};
    });
    if(metrics.clipped.length||metrics.minimumLabelPixels<12)throw Error(stem+': '+JSON.stringify(metrics));
    await page.screenshot({path:path.join(__dirname,stem+'-'+width+'.png')});
    records.push({stem,width,...metrics});await page.close();
   }
  }
  fs.writeFileSync(path.join(__dirname,'new-figure-checks.json'),JSON.stringify(records,null,2)+'\n');
  console.log(JSON.stringify(records,null,2));
 }finally{await browser.close()}
})().catch(e=>{console.error(e);process.exitCode=1});
