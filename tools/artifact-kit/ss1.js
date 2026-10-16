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

/* PPC outward */
function ppcChart(s) {
  const ox = 90, oy = 330, X = 250 * s.s, Y = 215 * s.s, X0 = 250, Y0 = 215;
  const curve = (X, Y) => { const p = []; for (let t = 0; t <= 90; t += 5) { const r = (t * Math.PI) / 180; p.push([ox + X * Math.cos(r), oy - Y * Math.sin(r)]); } return p; };
  let o = SV.line(ox, oy, ox, 30) + SV.line(ox, oy, 700, oy) + SV.text(ox + 6, 40, "Capital goods", "sm") + SV.text(700, oy + 24, "Consumer goods", "sm", { "text-anchor": "end" });
  if (s.s > 1.02) o += SV.path(ptsPath(curve(X0, Y0)), "c3", { opacity: 0.4 }) + SV.text(ox + X0 * 0.7071 + 10, oy - Y0 * 0.7071 + 22, "PPC", "lbl bd t3", { opacity: 0.6 });
  o += SV.path(ptsPath(curve(X, Y)), "c1") + SV.text(ox + X * 0.7071 + 12, oy - Y * 0.7071 - 6, s.s > 1.02 ? "PPC₁" : "PPC", "lbl bd t1");
  const px = ox + X * 0.7071, py = oy - Y * 0.7071;
  o += SV.line(px, py, px, oy, "gr") + SV.line(ox, py, px, py, "gr") + SV.circle(px, py, 7, s.s > 1.02 ? "dot2" : "dot1");
  return o;
}
Lib.stepper($("#stP"), { w: 760, h: 400, label: "Supply-side policy shifts the PPC outwards", base: { s: 1 }, draw: ppcChart, steps: [
  { cap: "A production possibility curve shows the <b>most the economy can produce</b> with its resources and technology. Here the economy produces on the curve.", s: { s: 1 } },
  { cap: "The government improves <b>education, infrastructure</b> and the way markets work. Workers are more productive and firms have better capital. The economy's <b>productive capacity</b> grows.", s: { s: 1.2 } },
  { cap: "The PPC shifts <b>outwards</b> to PPC₁. The economy can produce more of everything: this is what a <b>successful supply-side policy</b> achieves, and the same as a shift of AS to the right.", s: { s: 1.2 } },
] });
Lib.stepper($("#stS"), { w: 760, h: 400, label: "Supply-side policy shifts AS to the right", base: { sh: 0, a: 0 }, draw: adasChart, steps: [
  { cap: "The economy starts at <b>Y</b> and <b>P</b>, where AD meets AS.", s: { sh: 0, a: 0 } },
  { cap: "A <b>supply-side policy</b> (for example training for workers) raises productive capacity. <b>AS shifts right</b> to AS₁. Real GDP rises to Y₁ and the price level <b>falls</b> to P₁.", s: { sh: 0, a: 14 } },
  { cap: "Compare an <b>increase in AD</b> instead: AD shifts right and output rises, but the price level <b>rises</b> too.", s: { sh: 14, a: 0 } },
  { cap: "If both shift, output rises a lot and the price level barely changes: <b>fast growth without inflation</b>. <b>Evaluate:</b> supply-side effects take years to appear.", s: { sh: 14, a: 14 } },
] });

/* Lab 1 */
function labS() {
  if (!$("#ga") || !$("#gb")) return;
  const sh = +$("#ga").value, a = +$("#gb").value, [y, p] = solve2(sh, a);
  $("#sa1").textContent = (y - 50 >= 0 ? "+" : "−") + money(Math.abs(y - 50), 1); $("#sa2").textContent = (p - 50 >= 0.05 ? "+" : p - 50 <= -0.05 ? "−" : "") + money(Math.abs(p - 50), 1);
  $("#sa3").textContent = a > 0 && sh === 0 ? "Supply-side" : sh > 0 && a === 0 ? "Demand-side" : sh > 0 && a > 0 ? "Both" : "None";
  $("#sav").textContent = sh === 0 && a === 0 ? "Nothing has changed. Move one of the sliders." : a > 0 && sh === 0 ? `AS shifts right: output rises by ${money(y - 50, 1)} and the price level falls by ${money(50 - p, 1)}. Growth with lower inflationary pressure.` : sh > 0 && a === 0 ? `AD shifts right: output rises by ${money(y - 50, 1)} but the price level rises by ${money(p - 50, 1)}. More inflationary pressure.` : `Both shift: output rises by ${money(y - 50, 1)} and the price level changes by ${p - 50 >= 0 ? "+" : "−"}${money(Math.abs(p - 50), 1)}. A lot of growth with little inflation.`;
  $("#labS").innerHTML = adasChart({ sh, a });
}
Lib.slider($("#g1"), { id: "ga", label: "Demand-side policy: shift in AD", min: 0, max: 30, step: 2, value: 0, fmt: (v) => "+" + v, onInput: labS });
Lib.slider($("#g2"), { id: "gb", label: "Supply-side policy: shift in AS", min: 0, max: 30, step: 2, value: 14, fmt: (v) => "+" + v, onInput: labS });

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each policy <b>demand-side</b> or <b>supply-side</b>?", buckets: [{ label: "Demand-side" }, { label: "Supply-side" }], items: [
  { text: "Cut interest rates to raise spending", b: 0 }, { text: "Raise government spending in a recession", b: 0 }, { text: "Cut VAT to raise consumption", b: 0 }, { text: "Increase the money supply", b: 0 },
  { text: "Fund training for unemployed workers", b: 1 }, { text: "Build new motorways and broadband", b: 1 }, { text: "Remove rules that stop new firms entering a market", b: 1 }, { text: "Privatise a state-owned firm", b: 1 },
], done: "Demand-side shifts AD; supply-side shifts AS." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Supply-side policy", "Measures to raise the economy's productive capacity and shift AS to the right"],
  ["Aggregate supply", "Total output firms will supply at each price level"],
  ["Productivity", "Output per worker (or per unit of input)"],
  ["Productive capacity", "The most an economy can produce with its resources"],
  ["Potential output", "Output when resources are fully and efficiently used"],
  ["Economic growth", "A rise in real GDP over time"],
], done: "Good vocabulary scores marks." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how a successful supply-side policy could reduce inflationary pressure</b>.", items: [
  "The government improves education, infrastructure or competition",
  "Productivity rises and firms' costs per unit fall",
  "Aggregate supply shifts to the right",
  "Real GDP rises",
  "The price level falls, or rises by less than otherwise",
], done: "Growth with lower inflationary pressure." });
Lib.calc($("#c1"), { qs: [
  { q: "A firm produces 6,000 units a month with 40 workers. What is output per worker?", a: 150, sol: "6,000 ÷ 40 = <b>150 units</b> per worker." },
  { q: "After training, the same 40 workers produce 7,200 units. What is the percentage rise in productivity?", a: 20, sol: "(7,200 − 6,000) ÷ 6,000 × 100 = <b>20%</b>." },
  { q: "Real GDP rises from $800bn to $840bn. What is the rate of economic growth (%)?", a: 5, sol: "40 ÷ 800 × 100 = <b>5%</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What is a supply-side policy?", opts: ["A measure to increase aggregate demand", "A measure to increase aggregate supply", "A change in interest rates", "A change in the exchange rate"], a: 1, why: "Supply-side policy aims to raise productive capacity." },
  { q: "What is the likely effect of a successful supply-side policy?", opts: ["Aggregate supply shifts left", "Aggregate supply shifts right", "The price level rises sharply", "The exchange rate falls"], a: 1, why: "AS shifts right, raising output." },
  { q: "Which is a supply-side policy?", opts: ["Cutting income tax to raise spending", "Funding training for workers", "Raising interest rates", "Increasing benefits"], a: 1, why: "Training raises the quality of labour." },
  { q: "A successful supply-side policy is most likely to:", opts: ["Raise output and lower prices", "Lower output and raise prices", "Raise both output and prices a lot", "Have no effect"], a: 0, why: "AS shifts right: more output at a lower price level." },
  { q: "Which statement about supply-side policy is correct?", opts: ["Its effects are usually quick", "It usually takes years to work", "It only affects demand", "It is the same as monetary policy"], a: 1, why: "Better skills and capital take time to build." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Supply-side policy", "Government measures to increase the economy's productive capacity by shifting aggregate supply to the right."],
  ["Aggregate supply", "The total output firms are willing to supply at each price level."],
  ["Productivity", "Output per worker, or per unit of input."],
  ["Productive capacity", "The maximum output an economy can produce."],
  ["Potential output", "The level of output when resources are fully and efficiently used."],
  ["Economic growth", "A rise in real GDP over time."],
  ["Structural unemployment", "Unemployment caused by a mismatch between workers' skills and the jobs available."],
  ["Aggregate demand", "Total spending in an economy: C + I + G + (X − M)."],
  ["Microeconomic policy", "Policy that works on individual markets, firms and workers."],
] });
labS();
