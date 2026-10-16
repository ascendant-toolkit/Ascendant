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

const ITEMS = [["Food", 40, 5], ["Housing", 30, 2], ["Transport", 20, 10], ["Leisure", 10, -5]];
function cpiChart(s) {
  const base = 240; let o = SV.line(60, base, 710, base) + SV.line(60, base - 4, 60, 60);
  ITEMS.forEach(([n, w, c], i) => {
    const x = 100 + i * 150; let g = "";
    g += `<g opacity="${s.a}">` + SV.rect(x, base - w * 3.5, 50, w * 3.5, "", { style: "fill:var(--accent)", opacity: 0.85 }) + SV.text(x + 25, base - w * 3.5 - 6, w + "%", "sm bd", { "text-anchor": "middle" }) + "</g>";
    const h = Math.abs(c) * 10, y = c >= 0 ? base - h : base;
    g += `<g opacity="${s.b}">` + SV.rect(x + 56, y, 40, h, "", { style: `fill:var(${c >= 0 ? "--bad" : "--good"})`, opacity: 0.8 }) + SV.text(x + 76, c >= 0 ? y - 6 : y + h + 14, (c > 0 ? "+" : "") + c + "%", "sm bd", { "text-anchor": "middle" }) + "</g>";
    g += SV.text(x + 48, base + 78, n, "sm", { "text-anchor": "middle" });
    g += `<g opacity="${s.c}">` + SV.text(x + 48, base + 98, (w / 100 * c >= 0 ? "+" : "") + money((w / 100) * c, 1), "lbl bd t2", { "text-anchor": "middle" }) + "</g>";
    o += g;
  });
  o += SV.text(60, 50, s.a > 0 ? "Blue: weight in spending · Red/green: price change" : "", "sm");
  o += `<g opacity="${s.c}">` + SV.text(380, base + 128, "Weighted total = 4.1% inflation", "lbl bd t3", { "text-anchor": "middle", style: "font-size:18px" }) + "</g>";
  return o;
}
Lib.stepper($("#stC"), { w: 760, h: 400, label: "Building the CPI", base: { a: 0, b: 0, c: 0 }, draw: cpiChart, steps: [
  { cap: "<b>Step 1: the basket and weights.</b> Statisticians survey household spending. Food takes 40% of spending, housing 30%, transport 20%, leisure 10%. These are the <b>weights</b>.", s: { a: 1, b: 0, c: 0 } },
  { cap: "<b>Step 2: price changes.</b> Over the year food rose 5%, housing 2%, transport 10%, and leisure fell 5%.", s: { a: 1, b: 1, c: 0 } },
  { cap: "<b>Step 3: weighted average.</b> Each price change is multiplied by its weight: 2.0 + 0.6 + 2.0 − 0.5 = <b>4.1%</b>. This is the inflation rate. Items with larger weights matter more.", s: { a: 1, b: 1, c: 1 } },
] });
function idxChart(s) {
  const base = 320, k = 2.2, vals = [100, 103, 106.1, 109.3], labs = ["Year 0", "Year 1", "Year 2", "Year 3"]; let o = SV.line(60, base, 710, base);
  vals.forEach((v, i) => { const op = clamp(s.n - i, 0, 1); if (op <= 0) return; const x = 100 + i * 150, h = (v - 60) * 5; o += `<g opacity="${op}">` + SV.rect(x, base - h, 100, h, "", { style: "fill:var(--accent)", opacity: 0.8 }) + SV.text(x + 50, base - h - 8, money(v, 1), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 50, base + 20, labs[i], "sm", { "text-anchor": "middle" }); if (i) o += SV.text(x + 50, base - h - 28, "+" + money(((v - vals[i - 1]) / vals[i - 1]) * 100, 1) + "%", "lbl bd t2", { "text-anchor": "middle" }); o += "</g>"; });
  return o;
}
Lib.stepper($("#stN"), { w: 760, h: 400, label: "From CPI numbers to the inflation rate", base: { n: 0 }, draw: idxChart, steps: [
  { cap: "In the <b>base year</b> the CPI is set at <b>100</b>.", s: { n: 1 } },
  { cap: "Next year the CPI is <b>103</b>. Inflation = (103 − 100) ÷ 100 × 100 = <b>3%</b>.", s: { n: 2 } },
  { cap: "Then <b>106.1</b>: (106.1 − 103) ÷ 103 × 100 = <b>3%</b>. The index rises every year, because prices are still rising: the <b>rate</b> is what changes.", s: { n: 3 } },
  { cap: "Year 3: <b>109.3</b>. Compared with the base year, prices are <b>9.3% higher</b>. Always divide by the <b>earlier</b> index number.", s: { n: 4 } },
] });

/* Lab 1: weighted inflation */
function labC() {
  if (!$("#ca") || !$("#cb") || !$("#cc") || !$("#cd")) return;
  const ch = [+$("#ca").value, +$("#cb").value, +$("#cc").value, +$("#cd").value], w = [40, 30, 20, 10], infl = ch.reduce((a, c, i) => a + (c * w[i]) / 100, 0), simple = ch.reduce((a, c) => a + c, 0) / 4;
  $("#ca1").textContent = money(infl, 1) + "%"; $("#ca2").textContent = money(simple, 1) + "%";
  $("#cav").textContent = `Weighted inflation = ${ch.map((c, i) => `${w[i]}% × ${c}%`).join(" + ")} = ${money(infl, 1)}%. A simple average would give ${money(simple, 1)}%, which ignores how much households spend on each item. Weights matter: raise the price of food (40%) and see the effect, then try leisure (10%).`;
  const base = 280; let o = SV.line(60, base, 700, base);
  [["Food", ch[0], 40], ["Housing", ch[1], 30], ["Transport", ch[2], 20], ["Leisure", ch[3], 10]].forEach(([n, c, wt], i) => { const x = 100 + i * 150, h = Math.abs((c * wt) / 100) * 22, y = c >= 0 ? base - h : base; o += SV.rect(x, y, 100, h, "", { style: `fill:var(${c >= 0 ? "--accent" : "--good"})`, opacity: 0.85 }) + SV.text(x + 50, base + 22, n + " (" + wt + "%)", "sm", { "text-anchor": "middle" }) + SV.text(x + 50, c >= 0 ? y - 6 : y + h + 14, (c * wt / 100 >= 0 ? "+" : "") + money((c * wt) / 100, 1), "lbl bd", { "text-anchor": "middle" }); });
  $("#labC").innerHTML = o + SV.text(60, 30, "Contribution to inflation (weight × price change)", "sm");
}
Lib.slider($("#g1"), { id: "ca", label: "Food prices (weight 40%)", min: -10, max: 20, step: 1, value: 5, fmt: (v) => v + "%", onInput: labC });
Lib.slider($("#g2"), { id: "cb", label: "Housing (weight 30%)", min: -10, max: 20, step: 1, value: 2, fmt: (v) => v + "%", onInput: labC });
Lib.slider($("#g3"), { id: "cc", label: "Transport (weight 20%)", min: -10, max: 20, step: 1, value: 10, fmt: (v) => v + "%", onInput: labC });
Lib.slider($("#g4"), { id: "cd", label: "Leisure (weight 10%)", min: -10, max: 20, step: 1, value: -5, fmt: (v) => v + "%", onInput: labC });
/* Lab 2: different households */
const HH = [
  { n: "Typical household (the CPI)", w: [40, 30, 20, 10] },
  { n: "Pensioner", w: [35, 45, 5, 15] },
  { n: "Student", w: [25, 40, 10, 25] },
  { n: "Family with a long commute", w: [35, 25, 30, 10] },
];
const PC = [5, 2, 10, -5];
button_table("hhBtns", "hhOut", HH, 0, (p) => { const infl = p.w.reduce((a, w, i) => a + (w * PC[i]) / 100, 0); return `<div class="tw"><table class="t"><tr><th>Food</th><th>Housing</th><th>Transport</th><th>Leisure</th><th>Their inflation</th></tr><tr><td>${p.w[0]}%</td><td>${p.w[1]}%</td><td>${p.w[2]}%</td><td>${p.w[3]}%</td><td><b>${money(infl, 1)}%</b></td></tr></table></div><p class="note">Same price changes (food +5%, housing +2%, transport +10%, leisure −5%), different spending, different personal inflation. This is why the CPI is not exact for every household.</p>`; });

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each a <b>step in building the CPI</b> or a <b>limitation of the CPI</b>?", buckets: [{ label: "Step in building the CPI" }, { label: "Limitation" }], items: [
  { text: "Survey household spending to choose a basket", b: 0 }, { text: "Give each item a weight by share of spending", b: 0 }, { text: "Collect prices and compare with the base year", b: 0 }, { text: "Calculate a weighted average of price changes", b: 0 },
  { text: "No household buys exactly the average basket", b: 1 }, { text: "Quality improvements are hard to measure", b: 1 }, { text: "Consumers switch to cheaper goods", b: 1 }, { text: "Weights can be out of date", b: 1 },
], done: "A good answer on the CPI has the method and its limits." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Consumer Prices Index", "A weighted measure of the average change in prices of a basket of goods and services"],
  ["Basket of goods", "The goods and services typical households buy"],
  ["Weights", "The importance of each item, based on its share of spending"],
  ["Base year", "The year when the index is set at 100"],
  ["Price index", "A number showing the price level compared with the base year"],
  ["Inflation rate", "The percentage change in the CPI over a year"],
], done: "Good vocabulary scores marks." });
Lib.calc($("#c1"), { qs: [
  { q: "The CPI was 125 last year and is 130 this year. Calculate the inflation rate (%).", a: 4, sol: "(130 − 125) ÷ 125 × 100 = <b>4%</b>." },
  { q: "The CPI rises from 100 in the base year to 112 three years later. By how much have prices risen overall (%)?", a: 12, sol: "(112 − 100) ÷ 100 × 100 = <b>12%</b>." },
  { q: "Food (weight 50%) rises 4% and everything else (weight 50%) is unchanged. What is the inflation rate (%)?", a: 2, sol: "0.5 × 4 = <b>2%</b>." },
  { q: "Housing (weight 30%) rises 10%, transport (20%) rises 5% and the other 50% falls 2%. What is the inflation rate (%)?", a: 3, sol: "0.3 × 10 + 0.2 × 5 + 0.5 × (−2) = 3 + 1 − 1 = <b>3%</b>." },
  { q: "The CPI is 150 in Year 2 and 144 in Year 1. What is the inflation rate (%, 1 d.p.)?", a: 4.2, tol: 0.1, sol: "(150 − 144) ÷ 144 × 100 = <b>4.2%</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What does the CPI measure?", opts: ["Output", "The average change in prices of a basket of goods and services", "Employment", "The exchange rate"], a: 1, why: "A weighted index of consumer prices." },
  { q: "Why are weights used in the CPI?", opts: ["Because some items are more important in household spending", "Because all prices change equally", "To measure output", "To raise inflation"], a: 0, why: "Bigger spending shares matter more." },
  { q: "The CPI rises from 100 to 105. Inflation is:", opts: ["105%", "5%", "0.5%", "10%"], a: 1, why: "(105 − 100) ÷ 100 × 100." },
  { q: "Which is a limitation of the CPI?", opts: ["It is a weighted average", "It uses a basket", "It may not match the spending of every household", "It uses a base year"], a: 2, why: "No household is typical." },
  { q: "The base year of an index has a value of:", opts: ["0", "1", "100", "1,000"], a: 2, why: "The index starts at 100." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Consumer Prices Index (CPI)", "A weighted measure of the average change in the prices of a basket of goods and services."],
  ["Basket of goods and services", "The items typical households buy that are used to calculate the CPI."],
  ["Weights", "The importance given to each item, based on its share of household spending."],
  ["Base year", "The year used as the starting point of an index, set at 100."],
  ["Price index", "A number that shows price levels compared with a base year."],
  ["Weighted average", "An average where each item counts according to its importance."],
  ["Cost of living", "The cost of the goods and services households need to live."],
  ["Inflation rate", "The percentage rise in the price level, usually per year."],
] });
labC(); 
