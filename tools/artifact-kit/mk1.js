// uses: econ
/* ---------- 1. stepper: perfect competition ---------- */
const qStar = (p) => (p < 6 ? 0 : 2 + Math.sqrt((p - 3) / 3));
Lib.stepper($("#stA"), {
  w: 760, h: 400, label: "A perfectly competitive firm at four different market prices", base: { p: 16 },
  draw: (s) => {
    const F = frame(760, 400, 70, 730, 20, 350, 5.5, 0, 40), p = s.p, q = qStar(p);
    let o = axes(F, "Output (Q)", "Cost / revenue per unit ($)") + costSet(F, 20, { a: 0 });
    o += SV.line(F.l, F.Y(p), F.r, F.Y(p), "c4") + SV.text(F.r - 4, F.Y(p) - 8, "P = AR = MR = D", "lbl bd t4", { "text-anchor": "end" });
    if (q > 0) {
      const atc = ATC(q), u = p - atc;
      o += SV.rect(F.X(0), Math.min(F.Y(p), F.Y(atc)), F.X(q) - F.X(0), Math.abs(F.Y(p) - F.Y(atc)), u >= 0 ? "f3" : "f2") + SV.line(F.X(q), F.Y(p), F.X(q), F.Y(0), "gr") + SV.circle(F.X(q), F.Y(p), 7, "dot4");
      o += SV.text(F.X(q) + 10, F.Y(0) - 8, "Q = " + Lib.fmtN(q, 1), "lbl bd", { "text-anchor": "start" });
    } else o += SV.text(F.X(2.75), F.Y(p) - 30, "Output = 0: the firm shuts down", "lbl bd t2", { "text-anchor": "middle" });
    return o;
  },
  steps: [
    { cap: "A price taker accepts the <b>market price</b>. Its demand curve is horizontal at that price, so <b>P = AR = MR</b>. It only chooses output, and it produces where <b>MC = MR</b>.", s: { p: 16 } },
    { cap: "<b>P = $16</b> is above ATC at the chosen output, so the shaded box (P − ATC) × Q is <b>supernormal profit</b>. In the long run this is likely to attract new firms.", s: { p: 16 } },
    { cap: "<b>P ≈ $11.8</b> touches the lowest point of ATC. TR just equals TC, which includes normal profit, so the firm earns <b>normal profit</b>. This is the long-run position.", s: { p: 11.8 } },
    { cap: "<b>P = $9</b> is below ATC but above the lowest AVC. The box is <b>subnormal profit</b>. The firm still covers its variable costs, so it may stay open in the short run, but it is likely to leave in the long run.", s: { p: 9 } },
    { cap: "<b>P = $5</b> is below the lowest AVC ($6). Revenue cannot cover even variable costs, so the firm <b>shuts down</b>. It loses only its fixed costs instead of fixed costs plus a bigger shortfall.", s: { p: 5 } },
  ],
});

Lib.classify($("#cl1"), {
  prompt: "Which market structure does each description fit best?",
  buckets: [{ label: "Perfect competition" }, { label: "Monopolistic competition" }, { label: "Oligopoly" }, { label: "Monopoly" }],
  items: [
    { text: "Firms are price takers: D = AR = MR", b: 0 }, { text: "Free entry and exit with perfect information", b: 0 },
    { text: "Many firms, differentiated products, tangency solution", b: 1 }, { text: "Excess capacity in the long run", b: 1 },
    { text: "Kinked demand curve and sticky prices", b: 2 }, { text: "A few firms with a high concentration ratio", b: 2 }, { text: "Cartels and game theory", b: 2 },
    { text: "A single seller protected by barriers to entry", b: 3 }, { text: "Price maker causing a deadweight loss", b: 3 }, { text: "Natural monopoly with falling LRAC", b: 3 },
  ],
  done: "Good: structure is defined by the number of firms, product type and barriers to entry.",
});
Lib.match($("#m1"), { prompt: "Match each term to its meaning.", pairs: [
  ["Price taker", "A firm that must accept the market price"],
  ["Shutdown price", "The lowest point of AVC: below it the firm closes in the short run"],
  ["Productive efficiency", "Producing at the lowest point of average total cost"],
  ["Allocative efficiency", "Producing where price equals marginal cost"],
  ["Concentration ratio", "The share of market sales held by the largest few firms"],
  ["Free entry and exit", "No barriers to firms joining or leaving the market"],
], done: "Six terms for the spectrum and perfect competition." });
Lib.order($("#o1"), { prompt: "Put the long-run adjustment after supernormal profit in perfect competition in order.", items: [
  "Firms in the industry earn supernormal profit.",
  "New firms enter, attracted by the profit.",
  "Market supply shifts to the right.",
  "Market price falls.",
  "Profit is competed away until only normal profit is earned.",
] });
Lib.calc($("#c1"), { qs: [
  { q: "The five largest firms in a market have sales of $60m in total. Total market sales are $80m. What is the five-firm concentration ratio (%)?", a: 75, unit: "%", hint: "Concentration ratio = top firms' sales ÷ total sales × 100.", sol: "60 ÷ 80 × 100 = 75%." },
  { q: "A price-taking firm sells 50 units at $12. Its ATC at that output is $9. How much supernormal profit does it earn?", a: 150, unit: "$", hint: "(P − ATC) × Q.", sol: "(12 − 9) × 50 = $150." },
  { q: "A perfectly competitive firm sells 40 units at $8. ATC is $10. How large is the loss?", a: 80, unit: "$", hint: "(ATC − P) × Q.", sol: "(10 − 8) × 40 = $80 subnormal profit (a loss against normal profit)." },
  { q: "A perfectly competitive firm has AVC of $6 at its lowest point. The market price falls to $5. In the short run should it stay open? (type yes or no)", t: ["no"], ph: "yes or no", sol: "Price is below the lowest AVC, so it cannot cover variable costs: <b>no</b>, it should shut down." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "In perfect competition in the long run, a firm", opts: ["earns supernormal profit", "produces where P = MC at the lowest point of ATC", "restricts output to raise price", "faces a downward-sloping demand curve"], a: 1, why: "Entry and exit remove supernormal and subnormal profit, leaving P = MC = min ATC." },
  { q: "Which feature is found in perfect competition but not in monopolistic competition?", opts: ["many firms", "identical products", "profit-seeking firms", "free entry"], a: 1, why: "Perfect competition has homogeneous products; monopolistic competition has differentiated products." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Price taker", "A firm that must accept the market price and only chooses output. Faces a horizontal demand curve."],
  ["Shutdown price", "The lowest point of AVC. Below it a firm closes in the short run."],
  ["Productive efficiency", "Producing at the lowest point of average total cost."],
  ["Allocative efficiency", "Producing where price equals marginal cost (P = MC)."],
  ["Concentration ratio", "The share of total market sales held by the largest few firms."],
] });
(function(){
var $=function(id){return document.getElementById(id)};
var f1=function(x){return x.toFixed(1)}, f2=function(x){return x.toFixed(2)};

/* ---------- slider builder ---------- */
function sliders(boxId, cfg, extras, onChange){
  var box=$(boxId), st={};
  cfg.forEach(function(c){
    st[c.k]=c.v;
    var d=document.createElement('div'); d.className='ctl';
    d.innerHTML='<label for="'+boxId+'_'+c.k+'"><span>'+c.label+'</span><output id="'+boxId+'_'+c.k+'_o"></output></label>'+
      '<input type="range" id="'+boxId+'_'+c.k+'" min="'+c.min+'" max="'+c.max+'" step="'+c.step+'" value="'+c.v+'">'+
      (c.hint?'<p class="hint">'+c.hint+'</p>':'');
    box.appendChild(d);
    var inp=d.querySelector('input'), out=d.querySelector('output');
    var show=function(){ out.textContent=(c.fmt?c.fmt(st[c.k]):st[c.k]); };
    show();
    inp.addEventListener('input',function(){ st[c.k]=parseFloat(inp.value); show(); onChange(); });
  });
  (extras||[]).forEach(function(x){
    st[x.k]=x.v;
    var l=document.createElement('label'); l.className='chk';
    l.innerHTML='<input type="checkbox" id="'+boxId+'_'+x.k+'"'+(x.v?' checked':'')+'> '+x.label;
    box.appendChild(l);
    l.querySelector('input').addEventListener('change',function(e){ st[x.k]=e.target.checked; onChange(); });
  });
  return st;
}

/* ---------- SVG chart helper ---------- */
function Chart(xmax,ymax,xstep,ystep,xlab,ylab){
  var W=620,H=340,L=52,R=26,T=16,B=44, s=[];
  var sx=function(q){return L+q/xmax*(W-L-R)}, sy=function(p){return H-B-p/ymax*(H-T-B)};
  for(var x=0;x<=xmax+1e-9;x+=xstep){ if(x>0) s.push('<line class="grid" x1="'+sx(x)+'" y1="'+T+'" x2="'+sx(x)+'" y2="'+(H-B)+'"/>'); s.push('<text class="lbl-dim" x="'+sx(x)+'" y="'+(H-B+15)+'" text-anchor="middle">'+x+'</text>'); }
  for(var y=0;y<=ymax+1e-9;y+=ystep){ if(y>0) s.push('<line class="grid" x1="'+L+'" y1="'+sy(y)+'" x2="'+(W-R)+'" y2="'+sy(y)+'"/>'); s.push('<text class="lbl-dim" x="'+(L-7)+'" y="'+(sy(y)+3.5)+'" text-anchor="end">'+y+'</text>'); }
  s.push('<line class="axis" x1="'+L+'" y1="'+T+'" x2="'+L+'" y2="'+(H-B)+'"/><line class="axis" x1="'+L+'" y1="'+(H-B)+'" x2="'+(W-R)+'" y2="'+(H-B)+'"/>');
  s.push('<text class="lbl-dim" x="'+((L+W-R)/2)+'" y="'+(H-8)+'" text-anchor="middle">'+xlab+'</text>');
  s.push('<text class="lbl-dim" transform="translate(13 '+((T+H-B)/2)+') rotate(-90)" text-anchor="middle">'+ylab+'</text>');
  var c={
    sx:sx, sy:sy,
    ln:function(fn,x0,x1,col,w,dash){
      var pts=[],seg=[],n=140;
      for(var i=0;i<=n;i++){ var q=x0+(x1-x0)*i/n, y=fn(q);
        if(y>=0&&y<=ymax){ seg.push(sx(q).toFixed(1)+','+sy(y).toFixed(1)); } else if(seg.length){ pts.push(seg); seg=[]; } }
      if(seg.length) pts.push(seg);
      pts.forEach(function(p){ if(p.length>1) s.push('<polyline points="'+p.join(' ')+'" fill="none" style="stroke:var(--'+col+')" stroke-width="'+(w||2.4)+'"'+(dash?' stroke-dasharray="6 4"':'')+' stroke-linecap="round" stroke-linejoin="round"/>'); });
      return c;
    },
    seg:function(x1,y1,x2,y2,col,w,dash){ s.push('<line x1="'+sx(x1)+'" y1="'+sy(y1)+'" x2="'+sx(x2)+'" y2="'+sy(y2)+'" style="stroke:var(--'+col+')" stroke-width="'+(w||1.4)+'"'+(dash?' stroke-dasharray="4 4"':'')+'/>'); return c; },
    dot:function(x,y,col,hollow){ s.push('<circle cx="'+sx(x)+'" cy="'+sy(y)+'" r="5" style="fill:'+(hollow?'var(--surface)':'var(--'+col+')')+';stroke:var(--'+col+')" stroke-width="2"/>'); return c; },
    rect:function(x1,y1,x2,y2,col,op){ var top=Math.min(y1,y2), bot=Math.max(y1,y2); s.push('<rect x="'+sx(x1)+'" y="'+sy(bot)+'" width="'+Math.max(0,sx(x2)-sx(x1))+'" height="'+Math.max(0,sy(top)-sy(bot))+'" style="fill:var(--'+col+')" fill-opacity="'+(op||.25)+'"/>'); return c; },
    poly:function(p,col,op){ s.push('<polygon points="'+p.map(function(a){return sx(a[0]).toFixed(1)+','+sy(a[1]).toFixed(1)}).join(' ')+'" style="fill:var(--'+col+')" fill-opacity="'+(op||.25)+'"/>'); return c; },
    txt:function(x,y,t,col,anchor,dim){ s.push('<text class="'+(dim?'lbl-dim':'lbl')+'" x="'+sx(x)+'" y="'+sy(y)+'" text-anchor="'+(anchor||'start')+'"'+(col?' style="fill:var(--'+col+')"':'')+'>'+t+'</text>'); return c; },
    tick:function(x,t,col){ s.push('<text class="lbl" x="'+sx(x)+'" y="'+(H-B+29)+'" text-anchor="middle" style="fill:var(--'+col+')">'+t+'</text>'); return c; },
    ytick:function(y,t,col){ s.push('<text class="lbl" x="'+(L-7)+'" y="'+(sy(y)-6)+'" text-anchor="end" style="fill:var(--'+col+')">'+t+'</text>'); return c; },
    render:function(id){ $(id).innerHTML=s.join(''); }
  };
  return c;
}
function stats(id,arr){
  $(id).innerHTML=arr.map(function(a){ return '<div class="stat '+(a[2]||'')+'"><small>'+a[0]+'</small><b>'+a[1]+'</b></div>'; }).join('');
}

/* =====================  LAB 1: PERFECT COMPETITION  ===================== */
var PB=1.5, PC=0.15;
var pc=sliders('pcCtl',[
  {k:'P',label:'Market price',min:2,max:20,step:0.25,v:11,fmt:function(v){return '$'+f2(v)}},
  {k:'FC',label:'Fixed costs',min:0,max:40,step:1,v:15,fmt:function(v){return '$'+v}},
  {k:'a',label:'Input costs (wages, materials)',min:8,max:12,step:0.25,v:10,fmt:function(v){return '$'+f2(v)},hint:'Shifts MC, AVC and ATC up or down.'}
],[{k:'sup',label:'Highlight the supply curve',v:false}],drawPC);
function drawPC(){
  var a=pc.a,FC=pc.FC,P=pc.P;
  var MC=function(q){return a-2*PB*q+3*PC*q*q}, AVC=function(q){return a-PB*q+PC*q*q}, ATC=function(q){return AVC(q)+FC/q};
  var qv=PB/(2*PC), minAVC=AVC(qv);
  var D=4*PB*PB-12*PC*(a-P), q=0;
  if(D>=0){ q=(2*PB+Math.sqrt(D))/(6*PC); if(P<AVC(q)) q=0; }
  var open=q>0, tc=open?ATC(q)*q:FC, tr=P*q, profit=tr-tc;
  var minATC=1e9,qa=0; for(var i=0.1;i<=10;i+=0.02){ var v=ATC(i); if(v<minATC){minATC=v;qa=i;} }
  var ch=Chart(10,28,1,4,'Output (units per week)','Price / cost ($)');
  if(open){ ch.rect(0,ATC(q),q,P,profit>=0?'good':'bad',.28); }
  ch.ln(ATC,0.2,10,'cost',2.4).ln(AVC,0,10,'ink-dim',2.2).ln(MC,0,10,'rev',2.4);
  if(pc.sup) ch.ln(MC,qv,10,'rev',5.5);
  ch.seg(0,P,10,P,'prod',2.6);
  if(open){ ch.seg(q,0,q,P,'ink-dim',1.2,true).dot(q,P,'ink').tick(q,'Q*','ink'); }
  ch.txt(9.85,Math.min(MC(9.85)+1.2,27),'MC','rev','end').txt(9.85,ATC(9.85)+1.4,'ATC','cost','end').txt(9.85,AVC(9.85)-1.7,'AVC','ink-dim','end',true);
  ch.txt(0.15,P+0.9,'P = AR = MR = D','prod','start');
  ch.dot(qv,minAVC,'ink-dim',true);
  if(!open) ch.txt(5,24.5,'Shut down: P is below the lowest AVC','bad','middle');
  ch.render('pcSvg');
  var status,cls;
  if(!open){ status='Shutdown'; cls='bad'; }
  else if(Math.abs(profit)<0.05*Math.max(1,tc)/10 || Math.abs(P-ATC(q))<0.06){ status='Normal profit'; cls='warn'; }
  else if(profit>0){ status='Supernormal'; cls='good'; } else { status='Subnormal'; cls='bad'; }
  stats('pcStats',[['Output Q*',open?f2(q):'0'],['Total revenue','$'+f2(tr)],['Total cost','$'+f2(tc)],['Profit','$'+f2(profit),profit>0.02?'good':(profit<-0.02?'bad':'warn')],['Status',status,cls]]);
  var v;
  if(!open) v='<b>Short-run shutdown.</b> P ($'+f2(P)+') is below the lowest AVC ($'+f2(minAVC)+'). Staying open loses more than the fixed costs of $'+FC+', so the firm produces nothing until price recovers.';
  else if(P<ATC(q)-0.06) v='<b>Subnormal profit, but stay open.</b> P covers AVC ($'+f2(AVC(q))+') though not ATC ($'+f2(ATC(q))+'). The loss is smaller than shutting down, so the firm continues in the short run. In the long run firms exit, supply shifts left, and price rises.';
  else if(P>ATC(q)+0.06) v='<b>Supernormal profit.</b> P is above ATC by $'+f2(P-ATC(q))+' per unit. New firms are attracted in, supply shifts right, and price falls towards the lowest ATC of $'+f2(minATC)+'.';
  else v='<b>Normal profit: long-run equilibrium.</b> P = ATC at Q* (lowest ATC is $'+f2(minATC)+' at about '+f1(qa)+' units). No entry, no exit.';
  $('pcVerdict').innerHTML=v;
}
drawPC();
/* ---------- practice ---------- */
var PROMPTS=[
 {id:'p1',title:'1 — Perfect competition and shutdown',ctx:'Sketch MC, ATC, AVC and a horizontal price line in three versions: supernormal profit, normal profit, and P between AVC and ATC.',ask:'Explain why the firm keeps producing at a loss in the short run, and where its supply curve is. Apply it: which real market comes closest to perfect competition, and where does the match break down?'},
];
var list=$('promptList');
PROMPTS.forEach(function(p){
  var card=document.createElement('div'); card.className='prompt-card';
  card.innerHTML='<h3>'+p.title+'</h3><p class="ctx">'+p.ctx+'</p><div class="applywrap"><label for="'+p.id+'">Explain &amp; apply</label><br><textarea id="'+p.id+'" placeholder="'+p.ask.replace(/"/g,'&quot;')+'"></textarea></div>';
  list.appendChild(card);
  var ta=card.querySelector('textarea');
  try{ var sv=localStorage.getItem('mktstruct-'+p.id); if(sv) ta.value=sv; }catch(e){}
  ta.addEventListener('input',function(){ try{ localStorage.setItem('mktstruct-'+p.id,ta.value); }catch(e){} });
});

})();
(function(){

var G={"perfect competition": ["Very many small buyers and sellers, identical products, free entry and exit, and perfect information. Every firm is a price taker.", ""], "imperfect competition": ["Any market that breaks one or more conditions of perfect competition: monopoly, oligopoly and monopolistic competition. Firms have some control over price.", ""], "monopoly": ["A single seller, or one dominant firm, protected by barriers to entry. It faces the whole market demand curve, so it is a price maker.", ""], "monopolistic competition": ["Many firms selling differentiated products, with fairly free entry. Each has some price-setting power, but entry removes supernormal profit in the long run.", "Examples: restaurants, hairdressers, clothing brands."], "oligopoly": ["A market dominated by a few large firms whose decisions are interdependent. Usually has significant barriers to entry.", "Measured with a concentration ratio."], "natural monopoly": ["An industry where long-run average cost keeps falling across the whole range of market demand, so one firm can supply at lowest cost. Usually regulated.", "Examples: water pipes, rail track."], "barriers to entry": ["Anything that stops or deters new firms joining a market: economies of scale, high sunk costs, patents and licences, control of key resources, brand loyalty, predatory pricing.", ""], "price maker":["A firm that faces a downward-sloping demand curve and so can choose its price by choosing its output. Monopolists are price makers; to sell more they must cut price on every unit.",""],"price taker / price maker": ["A price taker must accept the market price and only chooses output (perfect competition). A price maker faces a downward-sloping demand curve and so chooses price by choosing output.", ""], "mc = mr": ["The profit-maximising rule: produce where marginal cost equals marginal revenue, with MC cutting MR from below. Past that output, each extra unit costs more than it earns.", "In perfect competition MR = price, so P = MC."], "supernormal profit": ["Profit above the normal level: total revenue exceeds total costs, including the owner's normal profit. On the diagram, P is above ATC.", "Also called abnormal profit. It attracts entry where barriers are low."], "subnormal profit": ["Profit below the normal level: total revenue does not cover total costs, so P is below ATC.", "Firms can stay open in the short run if P is at least AVC, but leave in the long run."], "shutdown price": ["The price below which a firm closes in the short run: the lowest point of AVC. Below it, revenue does not cover variable costs, so producing nothing loses less (only the fixed costs).", ""], "firm's supply curve": ["In perfect competition, the part of the MC curve above the lowest point of AVC. It shows how much the firm will supply at each market price.", ""], "entry and exit": ["Firms joining or leaving the industry in response to profit. Supernormal profit brings entry, market supply shifts right and price falls. Subnormal profit brings exit, supply shifts left and price rises.", ""], "productive efficiency": ["Producing at the lowest possible average cost, at the lowest point of ATC, so no resources are wasted.", ""], "allocative efficiency": ["Producing where price equals marginal cost (P = MC), so output matches what consumers value: the last unit is worth exactly what it costs to make.", ""], "deadweight loss": ["Welfare lost when output is below the socially best level: units that consumers value more than they cost to make are never produced. On the lab diagram it is the triangle between demand and MC.", ""], "x-inefficiency": ["The gap between a firm's actual costs and the lowest costs it could achieve. It appears when there is little competitive pressure, for example overstaffing or overpaying managers.", ""], "allocative inefficiency": ["Output where P is above MC: consumers would pay more for an extra unit than it costs to produce, but it is not made, so too little of the good is supplied.", ""], "product differentiation": ["Making a product different from rivals' through branding, quality, design, location or service, so buyers do not see it as a perfect substitute.", ""], "brand loyalty": ["Customers' preference for one brand even when similar products are cheaper. It makes demand less elastic, shown as a steeper demand curve in the lab.", ""], "non-price competition": ["Competing on anything other than price: branding, advertising, quality, after-sales service, loyalty schemes and innovation.", ""], "tangency solution": ["The long-run position in monopolistic competition where the demand (AR) curve just touches ATC at the profit-maximising output. P = ATC, so profit is normal.", ""], "excess capacity": ["Producing less than the output at the lowest point of ATC, so plant is under-used and unit costs are higher than they need to be. A feature of monopolistic competition in the long run.", ""], "interdependence": ["Each firm's best decision depends on how rivals respond, so firms must anticipate their reactions on price, output and advertising before acting.", ""], "concentration ratio": ["The share of total market sales held by the largest few firms, for example a five-firm concentration ratio of 80%. A high ratio signals an oligopoly.", ""], "kinked demand curve": ["A model of oligopoly: rivals ignore a price rise, so demand above the current price is elastic, but match a price cut, so demand below it is inelastic. The kink makes a vertical gap in the MR curve.", ""], "price rigidity": ["Prices staying the same for long periods even when costs change. The kinked demand curve is one explanation.", ""], "price war": ["A run of price cuts as rivals undercut each other. It lowers profit for every firm, so oligopolists often prefer non-price competition.", ""], "collusion": ["Firms co-operating to limit competition, for example by fixing price or output, to raise their joint profit. Formal agreements are illegal in many countries.", ""], "cartel": ["A formal (overt) agreement between firms to fix price or output so that they act like a monopolist. It is unstable because each member gains by cheating.", ""], "game theory": ["The study of strategic decisions where each player's payoff depends on what the others choose. Used to model oligopoly behaviour.", ""], "payoff matrix": ["A table showing each firm's profit for every combination of the strategies the two firms could choose.", ""], "dominant strategy": ["A strategy that gives a player the higher payoff whatever the rival does.", ""], "nash equilibrium": ["An outcome where neither player can do better by changing their own strategy, given what the other is doing. It can leave both worse off than if they co-operated.", ""], "tacit collusion": ["Firms moving in step without any formal agreement, for example following a price leader. Harder for regulators to detect and prove than a cartel.", ""], "repeated games": ["The same game played again and again. The threat of punishment in later rounds, such as a price war, can make co-operation rational if the future matters enough.", ""]};
var tip=document.createElement('div'); tip.id='kwTip'; tip.setAttribute('role','tooltip'); tip.hidden=true; document.body.appendChild(tip);
var cur=null, pinned=false, canHover=window.matchMedia&&window.matchMedia('(hover:hover)').matches;
function key(t){ return t.replace(/[\u2018\u2019]/g,"'").trim().toLowerCase(); }
function place(el){
  var r=el.getBoundingClientRect(), w=tip.offsetWidth, h=tip.offsetHeight, vw=window.innerWidth, vh=window.innerHeight;
  var x=Math.max(12,Math.min(r.left,vw-w-12)), y=r.bottom+8;
  if(y+h>vh-8 && r.top-h-8>8) y=r.top-h-8;
  tip.style.left=x+'px'; tip.style.top=y+'px';
}
function show(el){
  var g=G[el.dataset.term]; if(!g) return;
  cur=el;
  tip.innerHTML='<div class="tt"></div><div class="df"></div>'+(g[1]?'<div class="ex"></div>':'');
  tip.querySelector('.tt').textContent=el.textContent;
  tip.querySelector('.df').textContent=g[0];
  if(g[1]) tip.querySelector('.ex').textContent=g[1];
  tip.style.setProperty('--accent',getComputedStyle(el).getPropertyValue('--accent')||'');
  tip.hidden=false; place(el);
  el.setAttribute('aria-describedby','kwTip');
}
function hide(){
  if(cur){ cur.classList.remove('open'); cur.removeAttribute('aria-describedby'); }
  cur=null; pinned=false; tip.hidden=true;
}
document.querySelectorAll('.kw').forEach(function(el){
  var k=key(el.textContent); if(!G[k]) return;
  el.dataset.term=k; el.setAttribute('role','button'); el.tabIndex=0;
  if(canHover){
    el.addEventListener('mouseenter',function(){ if(!pinned) show(el); });
    el.addEventListener('mouseleave',function(){ if(!pinned) hide(); });
  }
  el.addEventListener('focus',function(){ if(!pinned) show(el); });
  el.addEventListener('blur',function(){ if(!pinned) hide(); });
  el.addEventListener('click',function(e){
    e.stopPropagation();
    if(pinned && cur===el){ hide(); return; }
    if(cur) cur.classList.remove('open');
    show(el); pinned=true; el.classList.add('open');
  });
  el.addEventListener('keydown',function(e){ if(e.key==='Enter'||e.key===' '){ e.preventDefault(); el.click(); } });
});
document.addEventListener('click',function(){ if(pinned) hide(); });
document.addEventListener('keydown',function(e){ if(e.key==='Escape') hide(); });
window.addEventListener('scroll',function(){ if(cur&&!tip.hidden) place(cur); },{passive:true});
window.addEventListener('resize',function(){ if(cur&&!tip.hidden) place(cur); });

})();
Lib.quiz($("#qz2"), { qs: [
  { q: "[Feb/March 2020 · 32 · Q2] What is correct if a firm in a perfectly competitive market is maximising its long-run profits? (it is allocatively efficient, it is productively efficient)", opts: ["no, no", "no, yes", "yes, no", "yes, yes"], a: 3, why: "In the long run the firm produces where price = MC (allocative efficiency) at the lowest point of ATC (productive efficiency)." },
] });
