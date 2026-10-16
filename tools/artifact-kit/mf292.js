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
Lib.stepper($("#st0"), { w: 760, h: 380, label: "Public goods and the free-rider problem", base: { n: 0 }, draw: mkChain(["Street lighting benefits everyone on the street", "Nobody can be excluded from using it", "Many people choose not to pay: free riders", "A private firm cannot earn profit", "The market does not supply it: the government does"], "--accent"), steps: chainSteps(["Street lighting benefits everyone on the street", "Nobody can be excluded from using it", "Many people choose not to pay: free riders", "A private firm cannot earn profit", "The market does not supply it: the government does"]) });
Lib.stepper($("#st1"), { w: 760, h: 380, label: "From private to social benefit", base: { n: 0 }, draw: mkChain(["A student gains from education: private benefit", "Employers and society gain too: external benefit", "Private benefit + external benefit = social benefit", "The market ignores the external part", "Education is under-consumed"], "--good"), steps: chainSteps(["A student gains from education: private benefit", "Employers and society gain too: external benefit", "Private benefit + external benefit = social benefit", "The market ignores the external part", "Education is under-consumed"]) });
function labA() {
  const ids = ["a0","a1"]; if (!ids.every((i) => $('#' + i))) return;
  const v = ids.map((i) => +$('#' + i).value);
  const R = (function(v) {const s = v[0] + v[1], sh = Math.round(v[1] / s * 100); return { r: ['$' + s + 'k', sh + '%', 'Sees only $' + v[0] + 'k'], t: 'A student gains $' + v[0] + 'k privately and society gains a further $' + v[1] + 'k: a social benefit of $' + s + 'k. The market takes account only of the private benefit, so too little education is bought: this is under-consumption of a merit good.', bars: [['Private benefit', v[0], '--accent'], ['External benefit', v[1], '--good'], ['Social benefit', s, '--warn']] };})(v);
  $('#ar0').textContent = R.r[0]; $('#ar1').textContent = R.r[1]; $('#ar2').textContent = R.r[2]; $('#avv').textContent = R.t;
  if (R.svg) { $('#labA').innerHTML = R.svg; return; }
  const base = 270; let o = SV.line(60, base, 700, base); const mx = Math.max(1, ...R.bars.map((b) => Math.abs(b[1]))), k = 190 / mx, w = Math.min(120, 560 / R.bars.length - 20);
  R.bars.forEach((b, i) => { const x = 90 + i * (w + 24), h = Math.abs(b[1]) * k, y = b[1] >= 0 ? base - h : base; o += SV.rect(x, y, w, Math.max(h, 2), '', { style: 'fill:var(' + b[2] + ')', opacity: 0.85 }) + SV.text(x + w / 2, b[1] >= 0 ? y - 8 : y + h + 16, b[3] || b[1], 'lbl bd', { 'text-anchor': 'middle' }) + SV.text(x + w / 2, base + 24, b[0], 'sm', { 'text-anchor': 'middle', style: 'font-size:11px' }); });
  $('#labA').innerHTML = o;
}
Lib.slider($("#ga0"), { id: "a0", label: "Private benefit per student ($000)", min: 5, max: 60, step: 5, value: 30, fmt: (v) => '$' + v + 'k', onInput: labA });
Lib.slider($("#ga1"), { id: "a1", label: "External benefit per student ($000)", min: 0, max: 60, step: 5, value: 20, fmt: (v) => '$' + v + 'k', onInput: labA });
const L2 = [{"n": "Street lighting", "a": "Public good", "b": "Non-excludable and non-rival."}, {"n": "Education", "a": "Merit good", "b": "More benefit than consumers realise."}, {"n": "Cigarettes", "a": "Demerit good", "b": "More harm than consumers realise."}, {"n": "A private cinema ticket", "a": "Private good", "b": "Excludable and rival."}, {"n": "National defence", "a": "Public good", "b": "Protects everyone; cannot exclude."}, {"n": "A single local railway", "a": "Monopoly", "b": "One seller."}];
button_table("lbBtns", "lbOut", L2, 0, (p) => `<div class="tw"><table class="t"><tr><th>Type</th><th>Why</th></tr><tr><td><b>${p.a}</b></td><td>${p.b}</td></tr></table></div>`);
Lib.classify($("#cl1"), { prompt: "Which <b>type of good</b> is each?", buckets: [{"label": "Public good"}, {"label": "Merit good"}, {"label": "Demerit good"}], items: [{"text": "National defence", "b": 0}, {"text": "Street lighting", "b": 0}, {"text": "Education", "b": 1}, {"text": "Vaccinations", "b": 1}, {"text": "Cigarettes", "b": 2}, {"text": "Alcohol", "b": 2}], done: "Public, merit, demerit." });
Lib.classify($("#cl2"), { prompt: "Is each a <b>private</b>, <b>external</b> or <b>social</b> cost or benefit?", buckets: [{"label": "Private"}, {"label": "External"}, {"label": "Social"}], items: [{"text": "A firm's wage bill", "b": 0}, {"text": "Pollution harming residents", "b": 1}, {"text": "Total cost of production plus pollution", "b": 2}, {"text": "A graduate's higher pay", "b": 0}, {"text": "Neighbours protected by vaccination", "b": 1}, {"text": "Private plus external benefit", "b": 2}], done: "Private, external, social." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Public good", "Non-excludable and non-rival"], ["Merit good", "Under-consumed: more benefit than realised"], ["Demerit good", "Over-consumed: more harm than realised"], ["External cost", "Cost borne by third parties"], ["Social benefit", "Private plus external benefit"], ["Monopoly", "A single dominant seller"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>why public goods are not provided by the market</b>.", items: ["The good benefits everyone", "Nobody can be excluded", "Some people free-ride without paying", "A private firm cannot make a profit", "The market does not provide it"], done: "The free-rider problem." });
Lib.calc($("#c1"), { qs: [
  { q: "A student's private benefit is $30k and the external benefit is $20k. What is the social benefit ($k)?", a: 50, sol: "30 + 20 = <b>$50k</b>." },
  { q: "A firm's private cost is $60 and the external cost is $15. What is the social cost ($)?", a: 75, sol: "60 + 15 = <b>$75</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A public good is:", opts: ["Excludable and rival", "Non-excludable and non-rival", "A demerit good", "Free of charge only"], a: 1, why: "Cannot exclude; use does not reduce others'." },
  { q: "A merit good is:", opts: ["Over-consumed", "Under-consumed", "A public good", "Always free"], a: 1, why: "More benefit than realised." },
  { q: "Which is a demerit good?", opts: ["Education", "Cigarettes", "Street lighting", "Vaccination"], a: 1, why: "More harm than realised." },
  { q: "Social cost =", opts: ["Private cost", "External cost", "Private cost + external cost", "Revenue − cost"], a: 2, why: "Sum." },
  { q: "A free rider:", opts: ["Pays more", "Uses a good without paying", "Produces for free", "Owns a monopoly"], a: 1, why: "Enjoys it without paying." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Public good", "A non-excludable, non-rival good that the market does not supply."],
  ["Merit good", "A good with more benefit than consumers realise; under-consumed."],
  ["Demerit good", "A good with more harm than consumers realise; over-consumed."],
  ["Private benefit", "Benefit to the individual buyer or seller."],
  ["External benefit", "Benefit to third parties."],
  ["Social benefit", "Private benefit plus external benefit."],
  ["Private cost", "Cost to the individual buyer or seller."],
  ["External cost", "Cost to third parties."],
  ["Social cost", "Private cost plus external cost."],
] });
labA(); 
