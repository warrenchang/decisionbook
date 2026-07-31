
const root=document.documentElement;
const saved=localStorage.getItem('dpn-theme');if(saved)root.dataset.theme=saved;
document.getElementById('theme-button')?.addEventListener('click',()=>{root.dataset.theme=root.dataset.theme==='dark'?'light':'dark';localStorage.setItem('dpn-theme',root.dataset.theme)});
const sidebar=document.querySelector('.sidebar'), menu=document.querySelector('.menu-button'), backdrop=document.querySelector('.sidebar-backdrop');
function setNav(open){sidebar?.classList.toggle('open',open);backdrop?.classList.toggle('show',open);document.body.classList.toggle('nav-open',open);menu?.setAttribute('aria-expanded',String(open));}
menu?.addEventListener('click',()=>setNav(!sidebar.classList.contains('open')));backdrop?.addEventListener('click',()=>setNav(false));
sidebar?.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>setNav(false)));document.addEventListener('keydown',e=>{if(e.key==='Escape')setNav(false)});
const progress=document.querySelector('.reading-progress span');function updateProgress(){const max=document.documentElement.scrollHeight-innerHeight;progress.style.width=(max>0?Math.min(100,scrollY/max*100):0)+'%'}addEventListener('scroll',updateProgress,{passive:true});updateProgress();
const dlg=document.getElementById('search-dialog'),btn=document.getElementById('search-button'),inp=document.getElementById('search-input'),out=document.getElementById('search-results');
btn?.addEventListener('click',()=>{dlg.showModal();setTimeout(()=>inp.focus(),60)});
let idx=[];fetch((document.body.dataset.root||'')+'search-index.json').then(r=>r.json()).then(x=>idx=x).catch(()=>{out.innerHTML='<p>Search index unavailable.</p>'});
function esc(s){return s.replace(/[&<>"']/g,m=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[m]))}
inp?.addEventListener('input',()=>{let q=inp.value.trim().toLowerCase();if(q.length<2){out.innerHTML='';return}let terms=q.split(/\s+/);let hits=idx.map(x=>{let title=x.title.toLowerCase(),heads=x.headings.toLowerCase(),hay=(x.title+' '+x.headings+' '+x.text).toLowerCase();let score=terms.reduce((s,t)=>s+(title.includes(t)?7:0)+(heads.includes(t)?4:0)+(hay.split(t).length-1),0);return {...x,score}}).filter(x=>x.score>0).sort((a,b)=>b.score-a.score).slice(0,30);out.innerHTML=hits.map(x=>`<div class="search-hit"><a href="${document.body.dataset.root||''}${x.href}">${esc(x.title)}</a><div>${esc(x.excerpt)}</div></div>`).join('')||'<p>No results.</p>'});
