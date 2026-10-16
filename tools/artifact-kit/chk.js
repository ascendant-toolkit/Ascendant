(async()=>{document.querySelectorAll('[role=tabpanel]').forEach(p=>p.hidden=false);
const res=[];
const run=async(sv,dots,name)=>{for(let i=0;i<Math.max(1,dots.length);i++){ if(dots[i]) dots[i].click(); await new Promise(r=>setTimeout(r,1250));
 const ts=[...sv.querySelectorAll('text')].filter(t=>+(t.style.opacity||t.getAttribute('opacity')||1)>0.5&&t.textContent.trim());
 const bb=ts.map(t=>({t:t.textContent,b:t.getBBox()}));
 for(let a=0;a<bb.length;a++)for(let c=a+1;c<bb.length;c++){const A=bb[a].b,B=bb[c].b;if(A.x<B.x+B.width-1&&B.x<A.x+A.width-1&&A.y<B.y+B.height-1&&B.y<A.y+A.height-1)res.push(name+' s'+(i+1)+': "'+bb[a].t+'" x "'+bb[c].t+'"');}
 const vb=sv.viewBox.baseVal;bb.forEach(o=>{if(o.b.x<-2||o.b.x+o.b.width>vb.width+2||o.b.y<0||o.b.y+o.b.height>vb.height+2)res.push(name+' s'+(i+1)+' off: '+o.t);});}};
for(const st of document.querySelectorAll('.stp')){await run(st.querySelector('svg'),[...st.querySelectorAll('.stp-dots button')],st.parentElement.id||'stp');}
for(const sv of document.querySelectorAll('svg[id^=lab]')){await run(sv,[],sv.id);}
const dup=[...document.querySelectorAll('[id]')].map(e=>e.id).filter((x,i,a)=>a.indexOf(x)!==i);
const empty=[...document.querySelectorAll('[id]')].filter(e=>/^(st|cl|m\d|o\d|c\d|qz|fc|g\d)/.test(e.id)&&!e.children.length&&!e.textContent.trim()).map(e=>e.id);
const tabs=[...document.querySelectorAll('[role=tab]')].length;
return JSON.stringify({overlaps:res,dup,empty,tabs});})()
