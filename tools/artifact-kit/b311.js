const clamp = (v, a, b) => Math.max(a, Math.min(b, v));
const QX = (q) => 80 + 6 * q, PY = (p) => 360 - 2.7 * p;
function seg(m, c) { // clip P = mQ + c to 0<=Q<=100, 0<=P<=120
  let lo = 0, hi = 100;
  if (m !== 0) { const a = (0 - c) / m, z = (120 - c) / m; lo = Math.max(lo, Math.min(a, z)); hi = Math.min(hi, Math.max(a, z)); }
  return [lo, m * lo + c, hi, m * hi + c];
}
function curve(m, c, cls, label, o = {}) {
  const [q1, p1, q2, p2] = seg(m, c);
  if (q2 <= q1) return "";
  let s = SV.line(QX(q1), PY(p1), QX(q2), PY(p2), cls, o.attrs);
  if (label) { const a = { "text-anchor": "start" }; if (o.attrs && o.attrs.opacity !== undefined) a.opacity = o.attrs.opacity; s += SV.text(QX(q2) + (o.dx ?? 6), PY(p2) + (o.dy ?? 4), label, "lbl bd " + (o.t || "t1"), a); }
  return s;
}
function axes(yl = "Price", xl = "Quantity") {
  return SV.line(QX(0), PY(120), QX(0), PY(0)) + SV.line(QX(0), PY(0), QX(104), PY(0)) +
    SV.text(QX(0) + 6, PY(120) + 6, yl, "sm") + SV.text(QX(104), PY(0) + 22, xl, "sm", { "text-anchor": "end" });
}
const hline = (p, c = "gr", x2 = 100) => SV.line(QX(0), PY(p), QX(x2), PY(p), c);
const vline = (q, p, c = "gr") => SV.line(QX(q), PY(p), QX(q), PY(0), c);
const ylab = (p, t, c = "sm") => SV.text(QX(0) - 8, PY(p) + 4, t, c, { "text-anchor": "end" });
const xlab = (q, t, c = "sm") => SV.text(QX(q), PY(0) + 18, t, c, { "text-anchor": "middle" });
const money = (v, d = 1) => Lib.fmtN(v, d);
const halo = "paint-order:stroke;stroke:var(--surface);stroke-width:4px";
const asP = (y) => (y <= 60 ? 30 + 0.4 * y : 54 + 2.2 * (y - 60));
function solveAD(sh) {
  const c = 90 + 0.8 * sh; let y = (c - 30) / 1.2;
  if (y > 60) y = (c + 78) / 3;
  return [y, asP(y), c];
}
function adLine(c, cls, label, o = {}) {
  const lo = Math.max(0, (c - 108) / 0.8), hi = Math.min(100, (c - 8) / 0.8);
  let r = SV.line(QX(lo), PY(c - 0.8 * lo), QX(hi), PY(c - 0.8 * hi), cls, o.attrs);
  if (label) r += SV.text(QX(hi) + 6, PY(c - 0.8 * hi) + (o.dy ?? 4), label, "lbl bd " + (o.t || "t1"), o.attrs && o.attrs.opacity !== undefined ? { opacity: o.attrs.opacity } : {});
  return r;
}
function adChart(s) {
  const sh = s.sh, [y1, p1, c] = solveAD(sh), moved = Math.abs(sh) >= 1;
  let o = axes("Price level", "Real GDP");
  o += SV.path(ptsPath([[QX(0), PY(30)], [QX(60), PY(54)], [QX(87.7), PY(115)]]), "c3") + SV.text(QX(87.7) + 6, PY(115) + 4, "AS", "lbl bd t3");
  o += adLine(90, "c1", "AD", { t: "t1", attrs: { opacity: moved ? 0.4 : 1 } });
  if (moved) o += adLine(c, sh > 0 ? "c2" : "c4", sh > 0 ? "AD₁" : "AD₂", { t: sh > 0 ? "t2" : "t4" });
  o += hline(50) + vline(50, 50) + ylab(50, "P") + xlab(50, "Y") + SV.circle(QX(50), PY(50), 6, "dot1", { opacity: moved ? 0.45 : 1 });
  if (moved) o += hline(p1, "gr", y1) + vline(y1, p1) + SV.circle(QX(y1), PY(p1), 6, sh > 0 ? "dot2" : "dot4") + ylab(p1, "P₁", "sm bd") + xlab(y1, "Y₁", "sm bd");
  return o;
}

function solve2(sh, a) {
  const c = 90 + 0.8 * sh; let y = (c - 30 + 0.4 * a) / 1.2;
  if (y - a > 60) y = (c + 78 + 2.2 * a) / 3;
  return [y, c - 0.8 * y, c];
}
function adasChart(s) {
  const sh = s.sh, a = s.a, [y1, p1, c] = solve2(sh, a), movedAD = Math.abs(sh) >= 1, movedAS = Math.abs(a) >= 1;
  const pts = (x) => [[QX(Math.max(0, x)), PY(x < 0 ? 30 - 0.4 * x : 30)], [QX(60 + x), PY(54)], [QX(87.7 + x), PY(115)]];
  let o = axes("Price level", "Real GDP");
  if (movedAS) o += SV.path(ptsPath(pts(0)), "c3", { opacity: 0.4 });
  o += SV.path(ptsPath(pts(a)), "c3") + SV.text(QX(87.7 + a) + 6, PY(115) + 4, movedAS ? "AS₁" : "AS", "lbl bd t3");
  o += adLine(90, "c1", "AD", { t: "t1", attrs: { opacity: movedAD ? 0.4 : 1 } });
  if (movedAD) o += adLine(c, "c2", "AD₁", { t: "t2" });
  o += hline(50) + vline(50, 50) + ylab(50, "P") + xlab(50, "Y") + SV.circle(QX(50), PY(50), 6, "dot1", { opacity: movedAD || movedAS ? 0.45 : 1 });
  if (movedAD || movedAS) o += hline(p1, "gr", y1) + vline(y1, p1) + SV.circle(QX(y1), PY(p1), 6, "dot2") + ylab(p1, "P₁", "sm bd") + xlab(y1, "Y₁", "sm bd");
  return o;
}
const mkChain = (list, col) => (s) => {
  const bh = 46, gap = 14, x = 110, w = 540; let o = "";
  list.forEach((t, i) => {
    const v = clamp(s.n - i, 0, 1); if (v <= 0) return;
    const y = 14 + i * (bh + gap);
    let g = SV.rect(x, y, w, bh, "", { rx: 8, style: `fill:var(${col});fill-opacity:0.16;stroke:var(${col});stroke-width:2` });
    g += SV.circle(x - 28, y + bh / 2, 15, "dot1", { style: `fill:var(${col})` }) + SV.text(x - 28, y + bh / 2 + 5, i + 1, "lbl bd", { "text-anchor": "middle", style: "fill:var(--surface);font-size:14px" });
    g += SV.text(x + w / 2, y + bh / 2 + 5, t, "lbl bd", { "text-anchor": "middle", style: "font-size:14px" });
    if (i < list.length - 1) g += SV.line(x + w / 2, y + bh + 1, x + w / 2, y + bh + gap - 3, "ax", { style: "stroke-width:2" }) + SV.arrowHead(x + w / 2, y + bh + gap, "d", "dot1");
    o += `<g opacity="${v}">${g}</g>`;
  });
  return o;
};
const chainSteps = (caps) => caps.map((c, i) => ({ cap: c, s: { n: i + 1 } }));
function button_table(btnId, outId, data, cols, fn) {
  const show = (i) => {
    $("#" + btnId).innerHTML = data.map((q, j) => `<button class="b${j === i ? " pri" : ""}" data-j="${j}">${q.n}</button>`).join("");
    $$("#" + btnId + " .b").forEach((b) => (b.onclick = () => show(+b.dataset.j)));
    $("#" + outId).innerHTML = fn(data[i]);
  };
  show(0);
}
Lib.stepper($("#st0"), { w: 760, h: 380, label: "The problem with barter", base: { n: 0 }, draw: mkChain(["A farmer has wheat but wants shoes", "The shoemaker wants fruit, not wheat", "No double coincidence of wants", "Trade is slow or fails", "Money solves the problem"], "--bad"), steps: chainSteps(["A farmer has wheat but wants shoes", "The shoemaker wants fruit, not wheat", "No double coincidence of wants", "Trade is slow or fails", "Money solves the problem"]) });
Lib.stepper($("#st1"), { w: 760, h: 380, label: "How money helps trade", base: { n: 0 }, draw: mkChain(["The farmer sells wheat for money", "The farmer uses the money to buy shoes", "Money acts as a medium of exchange", "Prices let everyone compare values", "Specialisation and trade grow"], "--good"), steps: chainSteps(["The farmer sells wheat for money", "The farmer uses the money to buy shoes", "Money acts as a medium of exchange", "Prices let everyone compare values", "Specialisation and trade grow"]) });
function labA() {
  const ids = ["a0","a1","a2","a3","a4","a5"]; if (!ids.every((i) => $('#' + i))) return;
  const v = ids.map((i) => +$('#' + i).value);
  const R = (function(v) {const nm = ['Acceptable', 'Durable', 'Portable', 'Divisible', 'Scarce', 'Stable'], tot = v.reduce((a, b) => a + b, 0), lo = nm[v.indexOf(Math.min(...v))], vd = tot >= 24 ? 'Works well as money' : tot >= 18 ? 'Works, but with weaknesses' : 'Poor as money'; return { r: [tot + '/30', vd, lo], t: 'The item scores ' + tot + ' out of 30: ' + vd.toLowerCase() + '. Its weakest feature is ' + lo.toLowerCase() + '. For example, gold scores well on durability and scarcity but poorly on portability and divisibility; modern notes and digital money score well on portability and divisibility.', bars: nm.map((n, i) => [n, v[i], ['--accent', '--good', '--warn', '--bad', '--accent', '--good'][i]]) };})(v);
  $('#ar0').textContent = R.r[0]; $('#ar1').textContent = R.r[1]; $('#ar2').textContent = R.r[2]; $('#avv').textContent = R.t;
  if (R.svg) { $('#labA').innerHTML = R.svg; return; }
  const base = 270; let o = SV.line(60, base, 700, base); const mx = Math.max(1, ...R.bars.map((b) => Math.abs(b[1]))), k = 190 / mx, w = Math.min(120, 560 / R.bars.length - 20);
  R.bars.forEach((b, i) => { const x = 90 + i * (w + 24), h = Math.abs(b[1]) * k, y = b[1] >= 0 ? base - h : base; o += SV.rect(x, y, w, Math.max(h, 2), '', { style: 'fill:var(' + b[2] + ')', opacity: 0.85 }) + SV.text(x + w / 2, b[1] >= 0 ? y - 8 : y + h + 16, b[3] || b[1], 'lbl bd', { 'text-anchor': 'middle' }) + SV.text(x + w / 2, base + 24, b[0], 'sm', { 'text-anchor': 'middle', style: 'font-size:11px' }); });
  $('#labA').innerHTML = o;
}
Lib.slider($("#ga0"), { id: "a0", label: "Acceptable", min: 1, max: 5, step: 1, value: 4, fmt: (v) => v, onInput: labA });
Lib.slider($("#ga1"), { id: "a1", label: "Durable", min: 1, max: 5, step: 1, value: 4, fmt: (v) => v, onInput: labA });
Lib.slider($("#ga2"), { id: "a2", label: "Portable", min: 1, max: 5, step: 1, value: 4, fmt: (v) => v, onInput: labA });
Lib.slider($("#ga3"), { id: "a3", label: "Divisible", min: 1, max: 5, step: 1, value: 4, fmt: (v) => v, onInput: labA });
Lib.slider($("#ga4"), { id: "a4", label: "Scarce / limited in supply", min: 1, max: 5, step: 1, value: 4, fmt: (v) => v, onInput: labA });
Lib.slider($("#ga5"), { id: "a5", label: "Stable in value", min: 1, max: 5, step: 1, value: 3, fmt: (v) => v, onInput: labA });
const L2 = [{"n": "Buying a coffee with a card", "a": "Medium of exchange", "b": "Accepted in payment, no barter."}, {"n": "A price tag of $20", "a": "Measure of value", "b": "Prices let goods be compared."}, {"n": "Putting savings in a bank", "a": "Store of value", "b": "Keeps purchasing power for later."}, {"n": "Taking out a mortgage", "a": "Deferred payment", "b": "Pay later in money."}, {"n": "Comparing a $300 and a $900 phone", "a": "Measure of value", "b": "Values stated in money."}, {"n": "Paying wages at the end of the month", "a": "Medium of exchange", "b": "Payment accepted for work."}];
button_table("lbBtns", "lbOut", L2, 0, (p) => `<div class="tw"><table class="t"><tr><th>Function</th><th>Why</th></tr><tr><td><b>${p.a}</b></td><td>${p.b}</td></tr></table></div>`);
Lib.classify($("#cl1"), { prompt: "Which <b>function of money</b> is each?", buckets: [{"label": "Medium of exchange"}, {"label": "Measure of value"}, {"label": "Store of value"}, {"label": "Deferred payment"}], items: [{"text": "Paying for shopping with notes", "b": 0}, {"text": "A shop's price list", "b": 1}, {"text": "Saving money for next year", "b": 2}, {"text": "Repaying a loan over 5 years", "b": 3}, {"text": "Paying with a contactless card", "b": 0}, {"text": "Comparing prices of two goods", "b": 1}], done: "Four functions." });
Lib.classify($("#cl2"), { prompt: "Is each a <b>good</b> or <b>poor</b> characteristic of money?", buckets: [{"label": "Good for money"}, {"label": "Poor for money"}], items: [{"text": "Portable", "b": 0}, {"text": "Durable", "b": 0}, {"text": "Divisible", "b": 0}, {"text": "Easily damaged", "b": 1}, {"text": "Different in each unit", "b": 1}, {"text": "Unlimited supply", "b": 1}], done: "Characteristics of money." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Money", "Anything generally accepted as payment"], ["Barter", "Swapping goods directly"], ["Medium of exchange", "Used to pay for goods and services"], ["Store of value", "Can be saved for later"], ["Legal tender", "Money that must be accepted by law"], ["Divisible", "Can be split into small amounts"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>why money replaced barter</b>.", items: ["Barter needs a double coincidence of wants", "Trade was slow and difficult", "People adopted a common medium of exchange", "Goods were priced in money", "Trade and specialisation expanded"], done: "Money makes trade easier." });
Lib.calc($("#c1"), { qs: [
  { q: "A coat costs $80 and a hat costs $20. How many hats are worth one coat?", a: 4, sol: "80 ÷ 20 = <b>4</b>." },
  { q: "Prices rise 5% in a year. $200 saved last year buys goods worth how many dollars of last year's goods? (200 ÷ 1.05, nearest whole number)", a: 190, sol: "200 ÷ 1.05 ≈ <b>190</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A function of money is:", opts: ["Barter", "Medium of exchange", "Inflation", "Debt only"], a: 1, why: "Used to pay." },
  { q: "Barter needs:", opts: ["A double coincidence of wants", "Banks", "Cards", "Interest"], a: 0, why: "Rare." },
  { q: "Which is a characteristic of good money?", opts: ["Perishable", "Divisible", "Heavy", "Unlimited supply"], a: 1, why: "Small amounts." },
  { q: "Savings in a bank show money as a:", opts: ["Medium of exchange", "Store of value", "Barter", "Tax"], a: 1, why: "Keep for later." },
  { q: "Legal tender is:", opts: ["Any good", "Money that must be accepted by law", "Digital only", "Credit"], a: 1, why: "Required by law." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Money", "Anything generally accepted as a means of payment."],
  ["Barter", "Exchanging goods directly without money."],
  ["Double coincidence of wants", "Two people each want what the other has."],
  ["Medium of exchange", "Function: accepted in payment."],
  ["Measure of value", "Function: prices stated in money."],
  ["Store of value", "Function: can be saved."],
  ["Deferred payment", "Function: debts settled in future."],
  ["Legal tender", "Money that must be accepted by law."],
  ["Divisibility", "Can be broken into small units."],
] });
labA(); 
