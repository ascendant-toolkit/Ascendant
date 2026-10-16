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
Lib.stepper($("#st0"), { w: 760, h: 380, label: "A rise in interest rates", base: { n: 0 }, draw: mkChain(["The central bank raises interest rates", "Saving pays more: households save more", "Borrowing is dearer: households borrow less", "Households spend less", "Aggregate demand falls"], "--accent"), steps: chainSteps(["The central bank raises interest rates", "Saving pays more: households save more", "Borrowing is dearer: households borrow less", "Households spend less", "Aggregate demand falls"]) });
Lib.stepper($("#st1"), { w: 760, h: 380, label: "Falling confidence", base: { n: 0 }, draw: mkChain(["Households worry about jobs and the economy", "They cut back on big purchases", "They save more as a precaution", "Spending falls and firms lose sales", "Economic growth slows"], "--bad"), steps: chainSteps(["Households worry about jobs and the economy", "They cut back on big purchases", "They save more as a precaution", "Spending falls and firms lose sales", "Economic growth slows"]) });
function labA() {
  const ids = ["a0","a1","a2"]; if (!ids.every((i) => $('#' + i))) return;
  const v = ids.map((i) => +$('#' + i).value);
  const R = (function(v) {const sr = Math.max(0.02, Math.min(0.6, 0.12 + 0.015 * v[1] + 0.00002 * (v[0] - 3000) - 0.02 * (v[2] - 5))), sav = v[0] * sr, spend = v[0] - sav; return { r: ['$' + spend.toFixed(0), '$' + sav.toFixed(0), (sr * 100).toFixed(0) + '%'], t: 'With income $' + v[0] + ', a ' + v[1] + '% savings rate and confidence ' + v[2] + ', the household spends $' + spend.toFixed(0) + ' and saves $' + sav.toFixed(0) + ' (' + (sr * 100).toFixed(0) + '% of income). Higher interest rates and lower confidence push saving up; higher confidence and cheaper borrowing push spending up (illustrative model).', bars: [['Spending', spend, '--accent'], ['Saving', sav, '--good']] };})(v);
  $('#ar0').textContent = R.r[0]; $('#ar1').textContent = R.r[1]; $('#ar2').textContent = R.r[2]; $('#avv').textContent = R.t;
  if (R.svg) { $('#labA').innerHTML = R.svg; return; }
  const base = 270; let o = SV.line(60, base, 700, base); const mx = Math.max(1, ...R.bars.map((b) => Math.abs(b[1]))), k = 190 / mx, w = Math.min(120, 560 / R.bars.length - 20);
  R.bars.forEach((b, i) => { const x = 90 + i * (w + 24), h = Math.abs(b[1]) * k, y = b[1] >= 0 ? base - h : base; o += SV.rect(x, y, w, Math.max(h, 2), '', { style: 'fill:var(' + b[2] + ')', opacity: 0.85 }) + SV.text(x + w / 2, b[1] >= 0 ? y - 8 : y + h + 16, b[3] || b[1], 'lbl bd', { 'text-anchor': 'middle' }) + SV.text(x + w / 2, base + 24, b[0], 'sm', { 'text-anchor': 'middle', style: 'font-size:11px' }); });
  $('#labA').innerHTML = o;
}
Lib.slider($("#ga0"), { id: "a0", label: "Monthly income ($)", min: 1000, max: 6000, step: 500, value: 3000, fmt: (v) => '$' + v, onInput: labA });
Lib.slider($("#ga1"), { id: "a1", label: "Interest rate on savings (%)", min: 0, max: 10, step: 1, value: 3, fmt: (v) => v + '%', onInput: labA });
Lib.slider($("#ga2"), { id: "a2", label: "Confidence (1 low, 10 high)", min: 1, max: 10, step: 1, value: 6, fmt: (v) => v, onInput: labA });
const L2 = [{"n": "Income rises", "a": "More spending and saving", "b": "More to divide."}, {"n": "Interest rates rise", "a": "More saving, less borrowing", "b": "Higher reward; dearer loans."}, {"n": "Confidence falls", "a": "Less spending, more saving", "b": "Precaution against job loss."}, {"n": "Young age", "a": "More borrowing", "b": "Homes and education."}, {"n": "Middle age", "a": "More saving", "b": "Retirement."}, {"n": "Culture of thrift", "a": "More saving", "b": "Social attitudes."}];
button_table("lbBtns", "lbOut", L2, 0, (p) => `<div class="tw"><table class="t"><tr><th>Effect on spending/saving</th><th>Why</th></tr><tr><td><b>${p.a}</b></td><td>${p.b}</td></tr></table></div>`);
Lib.classify($("#cl1"), { prompt: "Does each <b>raise</b> or <b>lower</b> household spending?", buckets: [{"label": "Raises spending"}, {"label": "Lowers spending"}], items: [{"text": "Higher income", "b": 0}, {"text": "Higher confidence", "b": 0}, {"text": "Lower interest rates", "b": 0}, {"text": "Higher interest rates", "b": 1}, {"text": "Fear of unemployment", "b": 1}, {"text": "A culture of thrift", "b": 1}], done: "Know the effects." });
Lib.classify($("#cl2"), { prompt: "Which <b>influence</b> is each?", buckets: [{"label": "Income"}, {"label": "Interest rate"}, {"label": "Confidence"}, {"label": "Age"}, {"label": "Culture"}], items: [{"text": "A pay rise", "b": 0}, {"text": "Mortgage payments rise", "b": 1}, {"text": "Worry about job losses", "b": 2}, {"text": "Students borrowing for study", "b": 3}, {"text": "A tradition of saving for family", "b": 4}], done: "Five influences." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Saving", "Income not spent"], ["Consumption", "Household spending"], ["Borrowing", "Spending using money from lenders"], ["Confidence", "How optimistic households feel"], ["Interest rate", "Reward for saving and cost of borrowing"], ["Saving ratio", "Saving as a percentage of income"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how falling confidence slows the economy</b>.", items: ["Households fear job losses", "They cut spending and save more", "Firms' sales fall", "Firms cut output and jobs", "Growth slows"], done: "Confidence drives demand." });
Lib.calc($("#c1"), { qs: [
  { q: "A household earns $3,000 and saves $450. What is the saving ratio (%)?", a: 15, sol: "450 ÷ 3,000 × 100 = <b>15%</b>." },
  { q: "Income is $4,000, spending is $3,400 and tax is $200. How much is saved ($)?", a: 400, sol: "4,000 − 3,400 − 200 = <b>$400</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A rise in interest rates is likely to:", opts: ["Reduce saving", "Increase borrowing", "Reduce borrowing", "Increase spending"], a: 2, why: "Borrowing is dearer." },
  { q: "Higher confidence leads to:", opts: ["More spending", "Less spending", "No change", "More saving only"], a: 0, why: "Optimism." },
  { q: "Young adults tend to:", opts: ["Save the most", "Borrow", "Retire", "Avoid debt"], a: 1, why: "Homes and education." },
  { q: "Saving ratio is:", opts: ["Spending ÷ income", "Saving ÷ income × 100", "Income ÷ saving", "Interest ÷ saving"], a: 1, why: "Percentage." },
  { q: "Which affects borrowing attitudes?", opts: ["Culture", "Weather", "Gravity", "Tides"], a: 0, why: "Social norms." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Consumption", "Household spending on goods and services."],
  ["Saving", "Income not spent."],
  ["Borrowing", "Obtaining funds to be repaid with interest."],
  ["Rate of interest", "The reward for saving and cost of borrowing."],
  ["Confidence", "How optimistic households are about the future."],
  ["Saving ratio", "Saving as a percentage of income."],
  ["Disposable income", "Income after tax."],
  ["Aggregate demand", "Total spending in the economy."],
  ["Precautionary saving", "Saving to be ready for bad times."],
] });
labA(); 
