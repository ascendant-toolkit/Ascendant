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
Lib.stepper($("#st0"), { w: 760, h: 380, label: "Why public goods are not supplied", base: { n: 0 }, draw: mkChain(["A public good cannot exclude non-payers", "People can free-ride on others' payments", "Few choose to pay", "Firms cannot earn profit", "The market does not supply the good"], "--accent"), steps: chainSteps(["A public good cannot exclude non-payers", "People can free-ride on others' payments", "Few choose to pay", "Firms cannot earn profit", "The market does not supply the good"]) });
Lib.stepper($("#st1"), { w: 760, h: 380, label: "Why demerit goods are over-consumed", base: { n: 0 }, draw: mkChain(["Consumers underestimate the harm of the good", "Addiction or imperfect information", "Demand is higher than the real benefit justifies", "More is consumed than is best for society", "Market failure: over-consumption"], "--bad"), steps: chainSteps(["Consumers underestimate the harm of the good", "Addiction or imperfect information", "Demand is higher than the real benefit justifies", "More is consumed than is best for society", "Market failure: over-consumption"]) });
Lib.stepper($("#st2"), { w: 760, h: 380, label: "Why monopolies restrict output", base: { n: 0 }, draw: mkChain(["A firm is the only seller", "It faces no competition", "It cuts output and raises the price", "Consumers pay more and get less", "Market failure: restricted supply"], "--warn"), steps: chainSteps(["A firm is the only seller", "It faces no competition", "It cuts output and raises the price", "Consumers pay more and get less", "Market failure: restricted supply"]) });
function labA() {
  const ids = ["a0","a1","a2"]; if (!ids.every((i) => $('#' + i))) return;
  const v = ids.map((i) => +$('#' + i).value);
  const R = (function(v) {const p = v[0] * (1 + v[1] / 100), q = 100 * (1 - v[2] / 100), loss = (p - v[0]) * q; return { r: ['$' + p.toFixed(0), q.toFixed(0) + ' units', '$' + loss.toFixed(0)], t: 'A competitive market sells 100 units at $' + v[0] + '. A monopoly raises the price to $' + p.toFixed(0) + ' (a ' + v[1] + '% mark-up) and cuts output to ' + q.toFixed(0) + ' units. Consumers pay an extra $' + loss.toFixed(0) + ' on the units they still buy, and ' + (100 - q).toFixed(0) + ' units are no longer bought: a market failure caused by lack of competition.', bars: [['Competitive price', v[0], '--good'], ['Monopoly price', p, '--bad'], ['Output (units ÷ 5)', q / 5, '--accent', q.toFixed(0)]] };})(v);
  $('#ar0').textContent = R.r[0]; $('#ar1').textContent = R.r[1]; $('#ar2').textContent = R.r[2]; $('#avv').textContent = R.t;
  if (R.svg) { $('#labA').innerHTML = R.svg; return; }
  const base = 270; let o = SV.line(60, base, 700, base); const mx = Math.max(1, ...R.bars.map((b) => Math.abs(b[1]))), k = 190 / mx, w = Math.min(120, 560 / R.bars.length - 20);
  R.bars.forEach((b, i) => { const x = 90 + i * (w + 24), h = Math.abs(b[1]) * k, y = b[1] >= 0 ? base - h : base; o += SV.rect(x, y, w, Math.max(h, 2), '', { style: 'fill:var(' + b[2] + ')', opacity: 0.85 }) + SV.text(x + w / 2, b[1] >= 0 ? y - 8 : y + h + 16, b[3] || b[1], 'lbl bd', { 'text-anchor': 'middle' }) + SV.text(x + w / 2, base + 24, b[0], 'sm', { 'text-anchor': 'middle', style: 'font-size:11px' }); });
  $('#labA').innerHTML = o;
}
Lib.slider($("#ga0"), { id: "a0", label: "Competitive price ($)", min: 10, max: 50, step: 5, value: 20, fmt: (v) => '$' + v, onInput: labA });
Lib.slider($("#ga1"), { id: "a1", label: "Monopoly mark-up (%)", min: 0, max: 100, step: 10, value: 40, fmt: (v) => v + '%', onInput: labA });
Lib.slider($("#ga2"), { id: "a2", label: "Cut in output (%)", min: 0, max: 60, step: 5, value: 25, fmt: (v) => v + '%', onInput: labA });
const L2 = [{"n": "Public good", "a": "Not provided", "b": "Free riders; no profit."}, {"n": "Merit good", "a": "Under-consumed", "b": "Benefits undervalued; imperfect information."}, {"n": "Demerit good", "a": "Over-consumed", "b": "Harm underestimated; addiction."}, {"n": "External cost", "a": "Over-produced", "b": "Price ignores the cost on third parties."}, {"n": "External benefit", "a": "Under-produced", "b": "Price ignores the benefit to third parties."}, {"n": "Monopoly", "a": "Output restricted; higher price", "b": "No competition."}];
button_table("lbBtns", "lbOut", L2, 0, (p) => `<div class="tw"><table class="t"><tr><th>Outcome</th><th>Why</th></tr><tr><td><b>${p.a}</b></td><td>${p.b}</td></tr></table></div>`);
Lib.classify($("#cl1"), { prompt: "What is the market <b>outcome</b> for each?", buckets: [{"label": "Not provided"}, {"label": "Over-consumed"}, {"label": "Under-consumed"}], items: [{"text": "Street lighting", "b": 0}, {"text": "National defence", "b": 0}, {"text": "Cigarettes", "b": 1}, {"text": "Alcohol", "b": 1}, {"text": "Education", "b": 2}, {"text": "Vaccinations", "b": 2}], done: "Public, demerit, merit." });
Lib.classify($("#cl2"), { prompt: "Which <b>cause</b> explains each failure?", buckets: [{"label": "Free-rider problem"}, {"label": "Imperfect information"}, {"label": "Ignoring third parties"}, {"label": "Lack of competition"}], items: [{"text": "Firms cannot charge users of street lights", "b": 0}, {"text": "Smokers underestimate the harm", "b": 1}, {"text": "A factory does not pay for pollution", "b": 2}, {"text": "A monopoly raises prices", "b": 3}, {"text": "Parents undervalue schooling", "b": 1}], done: "Link cause to outcome." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Free-rider problem", "Using a good without paying"], ["Imperfect information", "Buyers do not know the true costs or benefits"], ["Spillover", "Cost or benefit to a third party"], ["Monopoly abuse", "Restricting output and raising price"], ["Addiction", "Makes demerit goods over-consumed"], ["Non-excludable", "Cannot stop non-payers using it"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how a monopoly causes market failure</b>.", items: ["A firm is the only supplier", "It faces no competition", "It restricts output", "It raises the price", "Consumers pay more and buy less"], done: "Restricted supply and higher prices." });
Lib.calc($("#c1"), { qs: [
  { q: "A monopoly raises the price from $20 to $28. What is the percentage rise?", a: 40, sol: "8 ÷ 20 × 100 = <b>40%</b>." },
  { q: "A firm's output falls from 100 to 75 units. What is the percentage fall?", a: 25, sol: "25 ÷ 100 × 100 = <b>25%</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Public goods are not supplied by the market because:", opts: ["They are too cheap", "Firms cannot charge users, so no profit", "Demand is zero", "They are demerit goods"], a: 1, why: "Free riders." },
  { q: "Why are demerit goods over-consumed?", opts: ["Consumers underestimate the harm", "Their price is too high", "They are public goods", "They are rival"], a: 0, why: "Imperfect information." },
  { q: "An external cost leads to:", opts: ["Under-production", "Over-production", "A shortage", "Monopoly"], a: 1, why: "Prices too low." },
  { q: "A monopoly abuses power by:", opts: ["Raising output", "Restricting output and raising price", "Cutting prices", "Increasing competition"], a: 1, why: "No rivals." },
  { q: "Merit goods are under-consumed because:", opts: ["Consumers undervalue the benefits", "They are too harmful", "They are public goods", "Producers refuse"], a: 0, why: "Imperfect information." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Free-rider problem", "People use a good without paying, so firms cannot profit."],
  ["Imperfect information", "Buyers do not know the full costs or benefits."],
  ["Externality", "A cost or benefit to a third party."],
  ["Over-provision", "Producing more than is best for society."],
  ["Under-provision", "Producing less than is best for society."],
  ["Restricted supply", "A monopoly limiting output."],
  ["Addiction", "A compulsion that keeps demand high."],
  ["Competition", "Rivalry that keeps prices down."],
  ["Abuse of monopoly power", "Using market power to raise prices and cut output."],
] });
labA(); 
