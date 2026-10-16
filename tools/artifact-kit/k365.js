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
Lib.stepper($("#st0"), { w: 760, h: 380, label: "Survival first", base: { n: 0 }, draw: mkChain(["A new restaurant opens", "Customers are few and costs are high", "The owner cuts costs and offers discounts to stay open", "Profit is low but the business survives", "Later it can aim for growth and profit"], "--bad"), steps: chainSteps(["A new restaurant opens", "Customers are few and costs are high", "The owner cuts costs and offers discounts to stay open", "Profit is low but the business survives", "Later it can aim for growth and profit"]) });
Lib.stepper($("#st1"), { w: 760, h: 380, label: "Growth and long-run profit", base: { n: 0 }, draw: mkChain(["A firm reinvests profit instead of paying it out", "It expands and wins more customers", "Economies of scale cut unit costs", "Market power rises", "Higher profit in the long run"], "--good"), steps: chainSteps(["A firm reinvests profit instead of paying it out", "It expands and wins more customers", "Economies of scale cut unit costs", "Market power rises", "Higher profit in the long run"]) });
Lib.stepper($("#st2"), { w: 760, h: 380, label: "Social welfare as an objective", base: { n: 0 }, draw: mkChain(["A state-owned bus company serves rural routes", "These routes make a loss", "It keeps them running for the community", "Profit is sacrificed", "Social welfare is achieved"], "--accent"), steps: chainSteps(["A state-owned bus company serves rural routes", "These routes make a loss", "It keeps them running for the community", "Profit is sacrificed", "Social welfare is achieved"]) });
function labA() {
  const ids = ["a0","a1","a2","a3"]; if (!ids.every((i) => $('#' + i))) return;
  const v = ids.map((i) => +$('#' + i).value);
  const R = (function(v) {const sc = [['Survival', v[0]], ['Profit maximisation', v[1]], ['Growth', v[2]], ['Social welfare', v[3]]], top = sc.reduce((a, b) => b[1] > a[1] ? b : a); return { r: [top[0], v[1] + '/10', v[3] + '/10'], t: 'The strongest pull is towards ' + top[0].toLowerCase() + '. New or struggling firms prioritise survival, shareholder-owned firms profit, expanding firms growth, and public or charitable firms social welfare. Real firms usually pursue a mix (illustrative model).', bars: sc.map((s, i) => [s[0], s[1], ['--bad', '--good', '--accent', '--warn'][i]]) };})(v);
  $('#ar0').textContent = R.r[0]; $('#ar1').textContent = R.r[1]; $('#ar2').textContent = R.r[2]; $('#avv').textContent = R.t;
  if (R.svg) { $('#labA').innerHTML = R.svg; return; }
  const base = 270; let o = SV.line(60, base, 700, base); const mx = Math.max(1, ...R.bars.map((b) => Math.abs(b[1]))), k = 190 / mx, w = Math.min(120, 560 / R.bars.length - 20);
  R.bars.forEach((b, i) => { const x = 90 + i * (w + 24), h = Math.abs(b[1]) * k, y = b[1] >= 0 ? base - h : base; o += SV.rect(x, y, w, Math.max(h, 2), '', { style: 'fill:var(' + b[2] + ')', opacity: 0.85 }) + SV.text(x + w / 2, b[1] >= 0 ? y - 8 : y + h + 16, b[3] || b[1], 'lbl bd', { 'text-anchor': 'middle' }) + SV.text(x + w / 2, base + 24, b[0], 'sm', { 'text-anchor': 'middle', style: 'font-size:11px' }); });
  $('#labA').innerHTML = o;
}
Lib.slider($("#ga0"), { id: "a0", label: "Is the firm new or struggling? (1 no, 10 yes)", min: 1, max: 10, step: 1, value: 3, fmt: (v) => v, onInput: labA });
Lib.slider($("#ga1"), { id: "a1", label: "Owned by shareholders seeking returns (1 no, 10 yes)", min: 1, max: 10, step: 1, value: 7, fmt: (v) => v, onInput: labA });
Lib.slider($("#ga2"), { id: "a2", label: "Wants to expand and win market share (1 no, 10 yes)", min: 1, max: 10, step: 1, value: 5, fmt: (v) => v, onInput: labA });
Lib.slider($("#ga3"), { id: "a3", label: "Owned by government or a charity (1 no, 10 yes)", min: 1, max: 10, step: 1, value: 2, fmt: (v) => v, onInput: labA });
const L2 = [{"n": "A new start-up", "a": "Survival", "b": "Must stay open."}, {"n": "A listed company", "a": "Profit maximisation", "b": "Shareholders want returns."}, {"n": "A supermarket opening new stores", "a": "Growth", "b": "Larger market share."}, {"n": "A state hospital", "a": "Social welfare", "b": "Provides a public service."}, {"n": "A charity shop", "a": "Social welfare", "b": "Raises money for a cause."}, {"n": "A firm in a deep recession", "a": "Survival", "b": "Avoid bankruptcy."}];
button_table("lbBtns", "lbOut", L2, 0, (p) => `<div class="tw"><table class="t"><tr><th>Likely objective</th><th>Why</th></tr><tr><td><b>${p.a}</b></td><td>${p.b}</td></tr></table></div>`);
Lib.classify($("#cl1"), { prompt: "Which <b>objective</b> does each describe?", buckets: [{"label": "Survival"}, {"label": "Profit maximisation"}, {"label": "Growth"}, {"label": "Social welfare"}], items: [{"text": "Staying in business through a recession", "b": 0}, {"text": "Making the largest possible profit", "b": 1}, {"text": "Increasing market share", "b": 2}, {"text": "Providing free services to the community", "b": 3}, {"text": "Avoiding bankruptcy", "b": 0}, {"text": "Opening new branches to expand", "b": 2}], done: "Four objectives." });
Lib.classify($("#cl2"), { prompt: "Is each firm more likely to be <b>private</b> or <b>public/charity</b>?", buckets: [{"label": "Private (profit, growth)"}, {"label": "Public/charity (social welfare)"}], items: [{"text": "A listed technology company", "b": 0}, {"text": "A shareholder-owned bank", "b": 0}, {"text": "A fast-food chain", "b": 0}, {"text": "A state hospital", "b": 1}, {"text": "A charity", "b": 1}, {"text": "A state school", "b": 1}], done: "Ownership and aims." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Survival", "Staying in business"], ["Profit maximisation", "Making the largest profit possible"], ["Growth", "Increasing the size of the firm"], ["Social welfare", "Benefiting society, not just profit"], ["Satisficing", "Making enough profit while pursuing other aims"], ["Market share", "A firm's share of total sales"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>why firms may pursue growth</b>.", items: ["The firm expands output", "It gains economies of scale", "Unit costs fall", "Its market share and power rise", "Long-run profit rises"], done: "Growth pays off." });
Lib.calc($("#c1"), { qs: [
  { q: "A firm's market share rises from 10% to 14%. By how many percentage points?", a: 4, sol: "14 − 10 = <b>4</b> percentage points." },
  { q: "A start-up has revenue of $60,000 and costs of $65,000. What is the profit or loss ($)? Enter the figure.", a: -5000, sol: "60,000 − 65,000 = <b>−$5,000</b>: a loss." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A new firm's most likely first objective is:", opts: ["Growth", "Survival", "Social welfare", "Monopoly"], a: 1, why: "Stay open." },
  { q: "Public sector firms often aim for:", opts: ["Profit maximisation", "Social welfare", "Bankruptcy", "Tax avoidance"], a: 1, why: "Public service." },
  { q: "Profit maximisation means:", opts: ["Largest possible profit", "Largest firm", "Lowest price", "Highest wages"], a: 0, why: "TR − TC largest." },
  { q: "Growth may:", opts: ["Lower short-run profit but raise long-run profit", "Always raise short-run profit", "Reduce sales", "Remove costs"], a: 0, why: "Investment." },
  { q: "Satisficing is:", opts: ["Maximum profit only", "Making enough profit while pursuing other aims", "Closing down", "Raising prices"], a: 1, why: "Good enough." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Survival", "The objective of staying in business."],
  ["Profit maximisation", "The objective of making the largest profit."],
  ["Growth", "The objective of increasing the firm's size."],
  ["Social welfare", "The objective of benefiting society."],
  ["Satisficing", "Making an acceptable profit while pursuing other aims."],
  ["Market share", "A firm's share of total market sales."],
  ["Shareholder", "An owner of part of a company."],
  ["Social enterprise", "A business with social aims."],
  ["Bankruptcy", "When a firm cannot pay its debts."],
] });
labA(); 
