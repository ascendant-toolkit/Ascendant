// uses: econ
/* ---------- 2. stepper: monopoly ---------- */
const mD = (q) => 20 - q, mMR = (q) => 20 - 2 * q, mMC = (q) => q, mATC = (q) => 0.5 * q + 32 / q, QM = 20 / 3, PM = 20 - QM;
Lib.stepper($("#stB"), {
  w: 760, h: 400, label: "Monopoly: demand, marginal revenue, marginal cost, profit-maximising output and deadweight loss", base: { d: 0, m: 0, e: 0, pr: 0, c: 0 },
  draw: (s) => {
    const F = frame(760, 400, 70, 730, 20, 350, 20, 0, 20);
    let o = axes(F, "Output (Q)", "Price / cost / revenue ($)");
    if (s.d) o += SV.path(curve(mD, 0, 20, F), "c1", { opacity: s.d }) + SV.text(F.X(19.4), F.Y(1.2) - 6, "D = AR", "lbl bd t1", { "text-anchor": "end", opacity: s.d }) + SV.path(curve(mMR, 0, 10, F), "c2", { opacity: s.d }) + SV.text(F.X(9.6), F.Y(0) - 8, "MR", "lbl bd t2", { "text-anchor": "end", opacity: s.d });
    if (s.m) o += SV.path(curve(mMC, 0, 20, F), "c3", { opacity: s.m }) + SV.text(F.X(14.2), F.Y(14.4) + 18, "MC", "lbl bd t3", { opacity: s.m }) + SV.path(curve(mATC, 1.6, 20, F), "c4", { opacity: s.m }) + SV.text(F.X(17.5), F.Y(mATC(17.5)) - 8, "ATC", "lbl bd t4", { opacity: s.m });
    if (s.pr) o += SV.rect(F.X(0), F.Y(PM), F.X(QM) - F.X(0), F.Y(mATC(QM)) - F.Y(PM), "f3", { opacity: s.pr }) + SV.text(F.X(QM / 2), (F.Y(PM) + F.Y(mATC(QM))) / 2 + 5, "Supernormal profit", "lbl bd t3", { "text-anchor": "middle", opacity: s.pr });
    if (s.c) o += SV.poly([[F.X(QM), F.Y(PM)], [F.X(QM), F.Y(QM)], [F.X(10), F.Y(10)]], "f2", { opacity: s.c }) + SV.circle(F.X(10), F.Y(10), 6, "dot3", { opacity: s.c }) + SV.text(F.X(10.4), F.Y(5.2), "Competitive: Q = 10, P = $10", "lbl bd t3", { opacity: s.c }) + SV.text(F.X(7), F.Y(16), "Deadweight loss", "lbl bd t2", { opacity: s.c });
    if (s.e) o += SV.circle(F.X(QM), F.Y(mMC(QM)), 7, "dot4", { opacity: s.e }) + SV.line(F.X(QM), F.Y(0), F.X(QM), F.Y(PM), "gr", { opacity: s.e }) + SV.line(F.X(0), F.Y(PM), F.X(QM), F.Y(PM), "gr", { opacity: s.e }) + SV.circle(F.X(QM), F.Y(PM), 7, "dot1", { opacity: s.e })
      + SV.text(F.X(QM), F.Y(0) + 18, "Qm", "lbl bd", { "text-anchor": "middle", opacity: s.e }) + SV.text(F.X(0) - 8, F.Y(PM) + 4, "Pm", "lbl bd", { "text-anchor": "end", opacity: s.e });
    return o;
  },
  steps: [
    { cap: "A monopolist faces the <b>whole market demand curve</b> (D = AR). To sell more it must cut the price on <b>every</b> unit, so <b>MR lies below AR</b> and falls twice as fast.", s: { d: 1 } },
    { cap: "Add its costs: <b>MC</b> and <b>ATC</b>. MC cuts ATC at its lowest point.", s: { d: 1, m: 1 } },
    { cap: "It maximises profit where <b>MR = MC</b>, at output Qm. It then reads the <b>price off the demand curve</b>, not off MR: Pm is well above MC.", s: { d: 1, m: 1, e: 1 } },
    { cap: "Price is above ATC, so the box (Pm − ATC) × Qm is <b>supernormal profit</b>. Barriers to entry may allow it to last in the long run.", s: { d: 1, m: 1, e: 1, pr: 1 } },
    { cap: "A competitive industry with the same costs would produce where <b>D = MC</b>: more output, lower price. The triangle between D and MC over the lost output is the <b>deadweight loss</b> from monopoly.", s: { d: 1, m: 1, e: 1, pr: 1, c: 1 } },
  ],
});

Lib.match($("#m1"), { prompt: "Match each term to its meaning.", pairs: [
  ["Price maker", "A firm that faces a downward-sloping demand curve and chooses price by choosing output"],
  ["Barriers to entry", "Anything that stops or deters new firms joining a market"],
  ["Deadweight loss", "Welfare lost because output is below the socially best level"],
  ["Natural monopoly", "An industry where LRAC keeps falling over the range of market demand"],
  ["Product differentiation", "Making a product different through branding, quality or service"],
  ["Tangency solution", "Long-run position in monopolistic competition where demand just touches ATC"],
  ["Excess capacity", "Producing less than the output at the lowest point of ATC"],
], done: "Seven terms for monopoly and monopolistic competition." });
Lib.calc($("#c1"), { qs: [
  { q: "A monopolist produces 100 units, sells at $30 and has ATC of $22. What is its profit?", a: 800, unit: "$", hint: "(P − ATC) × Q.", sol: "(30 − 22) × 100 = $800 supernormal profit." },
  { q: "A firm faces demand P = 20 − Q. What is its total revenue when it sells 6 units?", a: 84, unit: "$", hint: "Price at Q = 6 is 20 − 6 = 14, then TR = P × Q.", sol: "P = 14. TR = 14 × 6 = $84." },
  { q: "A monopolist maximises profit where MR = MC. Demand is P = 20 − Q, so MR = 20 − 2Q, and MC = Q. What output does it produce (1 decimal place)?", a: 6.7, tol: 0.1, sol: "20 − 2Q = Q gives 3Q = 20, so Q = <b>6.7</b>. The price is read from demand: 20 − 6.7 = $13.3." },
  { q: "In long-run monopolistic competition, price equals ATC. If price is $8 and the firm sells 50 units, what is its total revenue ($)?", a: 400, sol: "8 × 50 = <b>$400</b>, equal to total cost: only normal profit." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A profit-maximising monopolist sets price", opts: ["on the MR curve at MR = MC", "on the demand curve above the MR = MC output", "equal to MC", "equal to the lowest point of ATC"], a: 1, why: "Output is where MR = MC, but the price is read off the demand curve at that output." },
  { q: "In the long run, a firm in monopolistic competition produces", opts: ["at the lowest point of ATC", "where demand is tangent to ATC, to the left of the lowest point", "where P = MC", "where it earns supernormal profit"], a: 1, why: "The tangency solution gives P = ATC (normal profit) at output below the minimum of ATC, which is excess capacity." },
  { q: "A monopolist earns supernormal profit that lasts in the long run because of:", opts: ["free entry", "barriers to entry", "price taking", "perfect information"], a: 1, why: "Barriers stop new firms entering and competing the profit away." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Price maker", "A firm that faces a downward-sloping demand curve and so chooses price by choosing output."],
  ["Deadweight loss", "Welfare lost when output is below the socially best level."],
  ["Barriers to entry", "Anything that stops or deters new firms joining a market."],
  ["Natural monopoly", "An industry where LRAC keeps falling over the whole range of market demand, so one firm is cheapest."],
  ["Product differentiation", "Making a product different from rivals' through branding, quality, design or service."],
  ["Tangency solution", "The long-run position in monopolistic competition where demand just touches ATC."],
  ["Excess capacity", "Producing less than the output at the lowest point of ATC."],
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

/* =====================  LAB 2: MONOPOLY  ===================== */
var MB=1.8, MN=0.6;
var mo=sliders('moCtl',[
  {k:'A',label:'Demand strength (price intercept)',min:14,max:26,step:0.5,v:20,fmt:function(v){return '$'+f1(v)},hint:'Shifts demand and MR right or left.'},
  {k:'m',label:'Marginal cost at zero output',min:1,max:10,step:0.25,v:4,fmt:function(v){return '$'+f2(v)}},
  {k:'FC',label:'Fixed costs',min:0,max:40,step:1,v:10,fmt:function(v){return '$'+v}}
],[{k:'cmp',label:'Show competitive outcome and deadweight loss',v:true}],drawMO);
function drawMO(){
  var A=mo.A,m=mo.m,FC=mo.FC;
  var Dm=function(q){return A-MB*q}, MR=function(q){return A-2*MB*q}, MC=function(q){return m+MN*q}, ATC=function(q){return m+MN*q/2+FC/q};
  var qm=(A-m)/(2*MB+MN), pm=Dm(qm), qc=(A-m)/(MB+MN), pc_=Dm(qc);
  var prof=(pm-ATC(qm))*qm, dwl=0.5*(qc-qm)*(pm-MC(qm));
  var cs=0.5*qm*(A-pm);
  var ch=Chart(14,26,2,4,'Output (units per week)','Price / cost ($)');
  ch.rect(0,ATC(qm),qm,pm,prof>=0?'profit':'bad',.35);
  if(mo.cmp) ch.poly([[qm,pm],[qm,MC(qm)],[qc,pc_]],'bad',.4);
  ch.ln(ATC,0.25,14,'cost',2.4).ln(MC,0,14,'rev',2.4).ln(Dm,0,14,'prod',2.6).ln(MR,0,A/(2*MB),'ink',2.2,true);
  ch.seg(qm,0,qm,pm,'ink-dim',1.2,true).seg(0,pm,qm,pm,'ink-dim',1.2,true).dot(qm,MC(qm),'ink').dot(qm,pm,'ink');
  ch.tick(qm,'Qm','ink').ytick(pm,'Pm','ink');
  if(mo.cmp){ ch.dot(qc,pc_,'ink-dim',true).tick(qc,'Qc','ink-dim').txt(qc+0.2,pc_-1.4,'competitive: D = MC','ink-dim','start',true).txt((qm+qc)/2+0.2,(pm+MC(qm))/2+0.2,'DWL','bad','start'); }
  ch.txt(0.2,Math.min(A+1,25.2),'D = AR','prod','start').txt(A/(2*MB)-0.15,1.2,'MR','ink','end').txt(13.85,Math.min(MC(13.85)+1.2,25),'MC','rev','end').txt(13.85,ATC(13.85)+1.5,'ATC','cost','end');
  ch.render('moSvg');
  stats('moStats',[['Output Qm',f2(qm)],['Price Pm','$'+f2(pm)],['Profit','$'+f2(prof),prof>0?'good':'bad'],['Price above MC','$'+f2(pm-MC(qm))],['Deadweight loss','$'+f2(dwl),'bad']]);
  var v='<b>MR = MC at '+f2(qm)+' units, price read off demand at $'+f2(pm)+'.</b> A competitive market would sell '+f2(qc)+' units at $'+f2(pc_)+'. ';
  v+=prof>=0?'Supernormal profit of $'+f2(prof)+' is protected by barriers to entry.':'At these costs even the monopolist makes a loss of $'+f2(-prof)+'; it would need to cut fixed costs or shut down in the long run.';
  $('moVerdict').innerHTML=v;
}
drawMO();
/* =====================  LAB 3: MONOPOLISTIC COMPETITION  ===================== */
var CN=0.5, CM=3;
var mc=sliders('mcCtl',[
  {k:'e',label:'Entry of rival firms',min:0,max:130,step:1,v:0,fmt:function(v){return v+'%'},hint:'100% = long-run equilibrium.'},
  {k:'B',label:'Brand loyalty (steepness of demand)',min:0.8,max:2.2,step:0.05,v:1.2,fmt:function(v){return f2(v)},hint:'Higher = fewer close substitutes.'},
  {k:'FC',label:'Fixed costs',min:4,max:24,step:1,v:12,fmt:function(v){return '$'+v}}
],[],drawMC);
function drawMC(){
  var B=mc.B,FC=mc.FC,e=mc.e/100;
  var ATC=function(q){return CM+CN*q/2+FC/q}, MCf=function(q){return CM+CN*q};
  var qt=Math.sqrt(FC/(B+CN/2)), At=ATC(qt)+B*qt, A0=At+5;
  var A=A0-(A0-At)*e;
  var Dm=function(q){return A-B*q}, MR=function(q){return A-2*B*q};
  var q=Math.max(0,(A-CM)/(2*B+CN)), p=Dm(q), prof=(p-ATC(q))*q, qmin=Math.sqrt(2*FC/CN);
  var ch=Chart(8,20,1,4,'Output (units per week)','Price / cost ($)');
  if(q>0) ch.rect(0,ATC(q),q,p,prof>=0?'profit':'bad',.35);
  ch.ln(ATC,0.5,8,'cost',2.4).ln(MCf,0,8,'rev',2.4).ln(Dm,0,8,'prod',2.6).ln(MR,0,A/(2*B),'ink',2.2,true);
  if(q>0){ ch.seg(q,0,q,p,'ink-dim',1.2,true).seg(0,p,q,p,'ink-dim',1.2,true).dot(q,MCf(q),'ink').dot(q,p,'ink').tick(q,'Q','ink'); }
  ch.dot(qmin,ATC(qmin),'cost',true).txt(qmin,ATC(qmin)-1.5,'lowest ATC','cost','middle',true);
  ch.txt(0.15,Math.min(A+.9,19.3),'D = AR','prod','start').txt(A/(2*B)-.1,.9,'MR','ink','end').txt(7.9,MCf(7.9)+1,'MC','rev','end').txt(7.9,ATC(7.9)+1.5,'ATC','cost','end');
  ch.render('mcSvg');
  var st=Math.abs(prof)<0.15?'Normal':(prof>0?'Supernormal':'Subnormal');
  stats('mcStats',[['Output',f2(q)],['Price','$'+f2(p)],['ATC','$'+f2(ATC(q))],['Profit','$'+f2(prof),Math.abs(prof)<0.15?'warn':(prof>0?'good':'bad')],['Excess capacity',f2(Math.max(0,qmin-q))+' units']]);
  var v;
  if(Math.abs(prof)<0.15) v='<b>Long-run equilibrium.</b> Demand is tangent to ATC at the MR = MC output, so P = ATC and profit is normal. Output is '+f2(qmin-q)+' units below the lowest-ATC output: excess capacity, and P is above MC by $'+f2(p-MCf(q))+'.';
  else if(prof>0) v='<b>Supernormal profit of $'+f2(prof)+'.</b> Easy entry means rivals with similar (not identical) products arrive. Each takes some of this firm\'s customers, shifting D left. Move the entry slider to 100%.';
  else v='<b>Subnormal profit.</b> D lies below ATC at every output, so some firms exit. The remaining firms\' demand shifts back right until profit returns to normal.';
  $('mcVerdict').innerHTML=v;
}
drawMC();
/* ---------- practice ---------- */
var PROMPTS=[
 {id:'p2',title:'2 — Monopoly and deadweight loss',ctx:'Sketch D, MR, MC and ATC with supernormal profit shaded and the deadweight loss triangle marked.',ask:'Explain why the monopolist prices off the demand curve, not the MR curve. Apply it: name a firm with market power and say what protects its profits.'},
 {id:'p3',title:'3 — Monopolistic competition, short and long run',ctx:'Draw two diagrams: supernormal profit in the short run, then the long-run tangency solution.',ask:'Explain what causes the shift between the two. Apply it: choose a local market (cafés, salons) and describe non-price competition in it.'},
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
  { q: "[Feb/March 2020 · 32 · Q11] What is most likely to be found when comparing the long-run equilibrium outcome in monopolistic competition with that in perfect competition?", opts: ["a greater degree of excess capacity in monopolistic competition", "a higher level of profit in monopolistic competition", "a larger number of firms in monopolistic competition", "a more price-elastic demand curve in monopolistic competition"], a: 0, why: "In monopolistic competition demand is tangent to ATC to the left of its lowest point, so firms produce below the efficient scale. Entry removes supernormal profit in both structures." },
  { q: "[Feb/March 2023 · 32 · Q6] What is achieved in monopolistic competition in the long run? (allocative efficiency, supernormal profit)", opts: ["no, no", "no, yes", "yes, no", "yes, yes"], a: 0, why: "Entry removes supernormal profit, but price stays above marginal cost, so there is no allocative efficiency." },
] });
