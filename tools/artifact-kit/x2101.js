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
Lib.stepper($("#st0"), { w: 760, h: 380, label: "What the government adds to the market", base: { n: 0 }, draw: mkChain(["The market supplies most private goods", "It fails to supply public goods and under-supplies merit goods", "The government provides or funds them", "It also regulates and taxes to correct market failure", "A mixed economy: market plus government"], "--accent"), steps: chainSteps(["The market supplies most private goods", "It fails to supply public goods and under-supplies merit goods", "The government provides or funds them", "It also regulates and taxes to correct market failure", "A mixed economy: market plus government"]) });
Lib.stepper($("#st1"), { w: 760, h: 380, label: "From market to mixed", base: { n: 0 }, draw: mkChain(["A market economy allocates by prices", "Market failure appears: pollution, inequality, monopoly", "Governments intervene with taxes, subsidies and rules", "They also provide some goods directly", "The economy becomes mixed"], "--good"), steps: chainSteps(["A market economy allocates by prices", "Market failure appears: pollution, inequality, monopoly", "Governments intervene with taxes, subsidies and rules", "They also provide some goods directly", "The economy becomes mixed"]) });
function labA() {
  const ids = ["a0","a1","a2"]; if (!ids.every((i) => $('#' + i))) return;
  const v = ids.map((i) => +$('#' + i).value);
  const R = (function(v) {const s = Math.round((v[0] + v[1] + v[2]) / 3), c = s >= 80 ? 'Planned economy' : s >= 15 ? 'Mixed economy' : 'Close to a pure market', pv = 100 - s; return { r: [s + '%', c, pv + '%'], t: 'With state ownership ' + v[0] + '%, government spending ' + v[1] + '% and price control ' + v[2] + '%, the public sector share averages ' + s + '%: ' + c.toLowerCase() + '. Most real economies sit in the middle, with the balance between the private and public sectors varying by country.', bars: [['State ownership', v[0], '--accent'], ['Government spending', v[1], '--warn'], ['Price control', v[2], '--bad']] };})(v);
  $('#ar0').textContent = R.r[0]; $('#ar1').textContent = R.r[1]; $('#ar2').textContent = R.r[2]; $('#avv').textContent = R.t;
  if (R.svg) { $('#labA').innerHTML = R.svg; return; }
  const base = 270; let o = SV.line(60, base, 700, base); const mx = Math.max(1, ...R.bars.map((b) => Math.abs(b[1]))), k = 190 / mx, w = Math.min(120, 560 / R.bars.length - 20);
  R.bars.forEach((b, i) => { const x = 90 + i * (w + 24), h = Math.abs(b[1]) * k, y = b[1] >= 0 ? base - h : base; o += SV.rect(x, y, w, Math.max(h, 2), '', { style: 'fill:var(' + b[2] + ')', opacity: 0.85 }) + SV.text(x + w / 2, b[1] >= 0 ? y - 8 : y + h + 16, b[3] || b[1], 'lbl bd', { 'text-anchor': 'middle' }) + SV.text(x + w / 2, base + 24, b[0], 'sm', { 'text-anchor': 'middle', style: 'font-size:11px' }); });
  $('#labA').innerHTML = o;
}
Lib.slider($("#ga0"), { id: "a0", label: "State ownership of firms", min: 0, max: 100, step: 10, value: 20, fmt: (v) => v + '%', onInput: labA });
Lib.slider($("#ga1"), { id: "a1", label: "Government spending as a share of GDP", min: 0, max: 100, step: 10, value: 40, fmt: (v) => v + '%', onInput: labA });
Lib.slider($("#ga2"), { id: "a2", label: "Prices set by government", min: 0, max: 100, step: 10, value: 10, fmt: (v) => v + '%', onInput: labA });
const L2 = [{"n": "National defence", "a": "Public sector", "b": "A public good; free riders."}, {"n": "Smartphones", "a": "Private sector", "b": "Profitable; competitive."}, {"n": "State schools", "a": "Public sector", "b": "A merit good; funded by taxes."}, {"n": "Restaurants", "a": "Private sector", "b": "Private good."}, {"n": "Street lighting", "a": "Public sector", "b": "Public good."}, {"n": "Healthcare", "a": "Both", "b": "Public hospitals and private clinics."}];
button_table("lbBtns", "lbOut", L2, 0, (p) => `<div class="tw"><table class="t"><tr><th>Usually provided by</th><th>Why</th></tr><tr><td><b>${p.a}</b></td><td>${p.b}</td></tr></table></div>`);
Lib.classify($("#cl1"), { prompt: "Is each usually <b>public sector</b> or <b>private sector</b>?", buckets: [{"label": "Public sector"}, {"label": "Private sector"}], items: [{"text": "National defence", "b": 0}, {"text": "State schools", "b": 0}, {"text": "Street lighting", "b": 0}, {"text": "Supermarkets", "b": 1}, {"text": "Car manufacturers", "b": 1}, {"text": "Fashion shops", "b": 1}], done: "Who provides what." });
Lib.classify($("#cl2"), { prompt: "Is each a feature of a <b>market</b>, <b>planned</b> or <b>mixed</b> economy?", buckets: [{"label": "Market"}, {"label": "Planned"}, {"label": "Mixed"}], items: [{"text": "Prices set by demand and supply only", "b": 0}, {"text": "Government decides all output", "b": 1}, {"text": "Private firms and state-run services", "b": 2}, {"text": "Profit motive and public hospitals", "b": 2}, {"text": "State owns all resources", "b": 1}, {"text": "Little government intervention", "b": 0}], done: "Know the three systems." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Mixed economy", "Market and government both allocate resources"], ["Public sector", "The part of the economy run by the government"], ["Private sector", "Firms and households owned privately"], ["Market economy", "Allocation mainly by prices"], ["Planned economy", "Allocation by the government"], ["Market failure", "A reason for government involvement"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>why governments get involved in the market</b>.", items: ["Markets fail to supply public goods", "Some goods are over- or under-consumed", "Governments intervene with taxes, subsidies or rules", "They provide some goods directly", "The economy becomes mixed"], done: "Market failure justifies intervention." });
Lib.calc($("#c1"), { qs: [
  { q: "Government spending is $40bn and GDP is $100bn. What percentage of GDP is government spending?", a: 40, sol: "40 ÷ 100 × 100 = <b>40%</b>." },
  { q: "The private sector produces 65% of output. What percentage is produced by the public sector?", a: 35, sol: "100 − 65 = <b>35%</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A mixed economy is one where:", opts: ["Only the government decides", "Both the market and the government allocate resources", "Only firms decide", "There are no prices"], a: 1, why: "A mix." },
  { q: "Which is usually provided by the public sector?", opts: ["Smartphones", "National defence", "Fashion", "Restaurants"], a: 1, why: "Public good." },
  { q: "Most economies are:", opts: ["Pure market", "Pure planned", "Mixed", "Barter"], a: 2, why: "Mixed." },
  { q: "The private sector is motivated by:", opts: ["Profit", "Social welfare only", "Taxes", "Quotas"], a: 0, why: "Profit motive." },
  { q: "Governments intervene mainly to:", opts: ["Correct market failure", "Ban prices", "Remove competition", "Create unemployment"], a: 0, why: "Market failure." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Mixed economic system", "An economy where both the market and the government allocate resources."],
  ["Public sector", "The part of the economy owned and run by the government."],
  ["Private sector", "The part owned by individuals and firms."],
  ["Market economy", "Allocation mainly by the price mechanism."],
  ["Planned economy", "Allocation by government decisions."],
  ["Public good", "A non-excludable, non-rival good."],
  ["Merit good", "Under-consumed good with extra benefits."],
  ["Regulation", "Government rules on firms."],
  ["Market failure", "Misallocation of resources by the market."],
] });
labA(); 
