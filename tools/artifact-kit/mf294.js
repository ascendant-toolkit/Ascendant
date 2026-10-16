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
Lib.stepper($("#st0"), { w: 760, h: 380, label: "Consequences of over-consumption", base: { n: 0 }, draw: mkChain(["Too many demerit goods are consumed", "Health problems and pollution increase", "The government spends more on healthcare and clean-up", "Productivity and living standards suffer", "Welfare is lower than it could be"], "--bad"), steps: chainSteps(["Too many demerit goods are consumed", "Health problems and pollution increase", "The government spends more on healthcare and clean-up", "Productivity and living standards suffer", "Welfare is lower than it could be"]) });
Lib.stepper($("#st1"), { w: 760, h: 380, label: "Consequences of under-consumption", base: { n: 0 }, draw: mkChain(["Too little education or healthcare is consumed", "Workers are less skilled and less healthy", "Productivity and earnings are lower", "Growth and living standards are reduced", "Welfare is lower than it could be"], "--warn"), steps: chainSteps(["Too little education or healthcare is consumed", "Workers are less skilled and less healthy", "Productivity and earnings are lower", "Growth and living standards are reduced", "Welfare is lower than it could be"]) });
Lib.stepper($("#st2"), { w: 760, h: 380, label: "Consequences of non-provision", base: { n: 0 }, draw: mkChain(["The market does not provide a public good", "Society goes without it", "Everyone is worse off (no defence or lighting)", "The government must provide it", "Funding comes from taxes"], "--accent"), steps: chainSteps(["The market does not provide a public good", "Society goes without it", "Everyone is worse off (no defence or lighting)", "The government must provide it", "Funding comes from taxes"]) });
function labA() {
  const ids = ["a0","a1","a2"]; if (!ids.every((i) => $('#' + i))) return;
  const v = ids.map((i) => +$('#' + i).value);
  const R = (function(v) {const ex = Math.max(0, v[1] - v[0]), cost = ex * v[2]; return { r: [ex + 'm', '$' + cost + 'm', '$' + (cost / 10).toFixed(0)], t: 'The market consumes ' + v[1] + 'm units but the socially best quantity is ' + v[0] + 'm, so ' + ex + 'm units are over-consumed. At an external cost of $' + v[2] + ' a unit that is $' + cost + 'm of harm to society (about $' + (cost / 10).toFixed(0) + ' per household if 10 million households share it). This is the cost of misallocated resources.', bars: [['Best quantity', v[0], '--good'], ['Market quantity', v[1], '--bad'], ['Over-consumed', ex, '--warn']] };})(v);
  $('#ar0').textContent = R.r[0]; $('#ar1').textContent = R.r[1]; $('#ar2').textContent = R.r[2]; $('#avv').textContent = R.t;
  if (R.svg) { $('#labA').innerHTML = R.svg; return; }
  const base = 270; let o = SV.line(60, base, 700, base); const mx = Math.max(1, ...R.bars.map((b) => Math.abs(b[1]))), k = 190 / mx, w = Math.min(120, 560 / R.bars.length - 20);
  R.bars.forEach((b, i) => { const x = 90 + i * (w + 24), h = Math.abs(b[1]) * k, y = b[1] >= 0 ? base - h : base; o += SV.rect(x, y, w, Math.max(h, 2), '', { style: 'fill:var(' + b[2] + ')', opacity: 0.85 }) + SV.text(x + w / 2, b[1] >= 0 ? y - 8 : y + h + 16, b[3] || b[1], 'lbl bd', { 'text-anchor': 'middle' }) + SV.text(x + w / 2, base + 24, b[0], 'sm', { 'text-anchor': 'middle', style: 'font-size:11px' }); });
  $('#labA').innerHTML = o;
}
Lib.slider($("#ga0"), { id: "a0", label: "Socially best quantity (million units)", min: 10, max: 100, step: 10, value: 50, fmt: (v) => v, onInput: labA });
Lib.slider($("#ga1"), { id: "a1", label: "Market quantity (million units)", min: 10, max: 150, step: 10, value: 80, fmt: (v) => v, onInput: labA });
Lib.slider($("#ga2"), { id: "a2", label: "External cost per unit ($)", min: 1, max: 20, step: 1, value: 5, fmt: (v) => '$' + v, onInput: labA });
const L2 = [{"n": "Demerit goods", "a": "Over-consumption", "b": "Health costs; wasted resources."}, {"n": "External costs", "a": "Over-production", "b": "Pollution; congestion."}, {"n": "Merit goods", "a": "Under-consumption", "b": "Lower skills and health."}, {"n": "External benefits", "a": "Under-production", "b": "Society misses out."}, {"n": "Public goods", "a": "Non-provision", "b": "No defence or lighting without the state."}, {"n": "Monopoly", "a": "Restricted supply, higher prices", "b": "Consumers lose."}];
button_table("lbBtns", "lbOut", L2, 0, (p) => `<div class="tw"><table class="t"><tr><th>Consequence</th><th>Effect</th></tr><tr><td><b>${p.a}</b></td><td>${p.b}</td></tr></table></div>`);
Lib.classify($("#cl1"), { prompt: "Is each consequence <b>over-consumption</b>, <b>under-consumption</b>, <b>non-provision</b> or <b>restricted supply</b>?", buckets: [{"label": "Over-consumption"}, {"label": "Under-consumption"}, {"label": "Non-provision"}, {"label": "Restricted supply"}], items: [{"text": "Too many cigarettes smoked", "b": 0}, {"text": "Too much polluting production", "b": 0}, {"text": "Too little education bought", "b": 1}, {"text": "Too few people vaccinated", "b": 1}, {"text": "No street lighting supplied", "b": 2}, {"text": "A monopoly raises prices and cuts output", "b": 3}], done: "Match the consequence." });
Lib.classify($("#cl2"), { prompt: "Who is <b>harmed</b>?", buckets: [{"label": "Society"}, {"label": "Consumers"}, {"label": "Government"}], items: [{"text": "Pollution from factories", "b": 0}, {"text": "A dominant firm raising prices", "b": 1}, {"text": "Higher healthcare costs from smoking", "b": 2}, {"text": "Lower skills from low education", "b": 0}, {"text": "Pays to clean up a spill", "b": 2}], done: "Think about who bears the cost." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Over-consumption", "Too much of a demerit good"], ["Under-consumption", "Too little of a merit good"], ["Non-provision", "A public good is not supplied"], ["Restricted supply", "Monopoly cuts output"], ["Misallocation", "Resources not used in the best way"], ["Welfare loss", "A fall in society's well-being"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how under-consumption of education reduces growth</b>.", items: ["Consumers undervalue education", "Too little education is bought", "Workers are less skilled", "Productivity is lower", "Economic growth is lower"], done: "Under-consumption harms growth." });
Lib.calc($("#c1"), { qs: [
  { q: "The market produces 80 units but the socially best level is 50. How many units are over-produced?", a: 30, sol: "80 − 50 = <b>30</b>." },
  { q: "30 extra units each cause $5 of external cost. What is the total external cost ($)?", a: 150, sol: "30 × 5 = <b>$150</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Over-consumption is a consequence of:", opts: ["Merit goods", "Demerit goods", "Public goods", "Monopoly"], a: 1, why: "Demerit goods." },
  { q: "Non-provision refers to:", opts: ["Public goods", "Merit goods", "Demerit goods", "Free goods"], a: 0, why: "Public goods." },
  { q: "A monopoly leads to:", opts: ["Lower prices", "Restricted supply and higher prices", "More competition", "No profit"], a: 1, why: "No rivals." },
  { q: "Under-consumption leads to:", opts: ["Higher productivity", "Lower skills and health", "More pollution", "Lower prices"], a: 1, why: "Society loses benefits." },
  { q: "Misallocation of resources means:", opts: ["Efficient use", "Resources are not used in the best way for society", "No resources", "Surplus"], a: 1, why: "Wasted potential." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Misallocation of resources", "Resources not used in the best way for society."],
  ["Over-consumption", "Consuming more of a good than is best."],
  ["Under-consumption", "Consuming less than is best."],
  ["Non-provision", "A good is not supplied by the market."],
  ["Restricted supply", "A monopoly limiting output."],
  ["Welfare loss", "A fall in society's well-being."],
  ["Living standards", "The quality of life of a population."],
  ["Productivity", "Output per worker."],
  ["Government intervention", "Action to correct market failure."],
] });
labA(); 
