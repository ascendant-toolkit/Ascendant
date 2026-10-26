#!/bin/bash
# usage: chkh.sh <slug> -- headless chk2.js run: prints CHK n=<issues> and the first few distinct issues
S=$1; SRC=~/Documents/GitHub/Ascendant/artifacts_src/$S/index.html; T=/tmp/chkh_$S.html
python3 - "$SRC" "$T" <<'PY'
import sys,html
h=open(sys.argv[1]).read(); c=open("/Users/garybyatt/Documents/GitHub/Ascendant/tools/artifact-kit/chk2.js").read()
inj="<script>window.requestAnimationFrame=cb=>setTimeout(()=>cb(performance.now()),5);window.addEventListener('load',()=>setTimeout(()=>{"+c+";let n=0;const w=()=>{if(window.__chk){const r=JSON.parse(window.__chk);const u=[...new Set(r.issues.map(x=>x.replace(/^[^:]*: /,'')))].slice(0,6);document.title='CHK n='+r.issues.length+' '+u.join(' | ').replace(/</g,'')}else if(n++<400)setTimeout(w,200)};w()},500));</script>"
open(sys.argv[2],'w').write(h.replace('</body>',inj+'</body>'))
PY
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu --virtual-time-budget=120000 --dump-dom "file://$T" 2>/dev/null | grep -o "<title>CHK[^<]*" | head -1
