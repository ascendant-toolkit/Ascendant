#!/bin/bash
# usage: smoke.sh <slug>  -- loads the page headless, clicks every button, reports JS errors and empty SVG/NaN
S=$1; SRC=~/Documents/GitHub/econ-cs-artifacts/artifacts_src/$S/index.html; T=/tmp/smoke_$S.html
python3 - "$SRC" "$T" <<'PY'
import sys
h=open(sys.argv[1]).read()
inj="""<script>
window.__e=[];window.addEventListener('error',e=>window.__e.push(e.message+' @'+e.lineno));
window.addEventListener('load',()=>setTimeout(()=>{try{
 document.querySelectorAll('[role=tabpanel]').forEach(p=>p.hidden=false);
 document.querySelectorAll('button').forEach(b=>{try{b.click()}catch(e){window.__e.push('click '+e.message)}});
 document.querySelectorAll('input[type=checkbox]').forEach(b=>{try{b.click()}catch(e){}});
 document.querySelectorAll('input[type=range]').forEach(r=>{try{r.value=r.max;r.dispatchEvent(new Event('input'))}catch(e){window.__e.push('range '+e.message)}});
 document.querySelectorAll('button').forEach(b=>{try{b.click()}catch(e){window.__e.push('click2 '+e.message)}});
}catch(e){window.__e.push('harness '+e.message)}
 setTimeout(()=>{const c=document.body.cloneNode(true);c.querySelectorAll('script,style').forEach(x=>x.remove());const nan=(c.innerHTML.match(/NaN|undefined/g)||[]).length;document.title='ERRS='+window.__e.length+' NAN='+nan;const p=document.createElement('pre');p.id='errs';p.textContent=window.__e.join('\\n');document.body.prepend(p)},1500)},300));
</script>"""
open(sys.argv[2],'w').write(h.replace('</body>',inj+'</body>'))
PY
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu --virtual-time-budget=8000 --dump-dom "file://$T" 2>/dev/null | grep -E "<title>|<pre id=\"errs\">" -A3 | head -12
