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

function realChart(s) {
  const base = 320, k = 2.4, bars = [["Year 1", 100, "--muted", s.a], ["Year 2 nominal", 106, "--warn", s.b], ["Year 2 real", 106 / 1.04, "--good", s.c]];
  let o = SV.line(60, base, 700, base);
  bars.forEach(([n, v, c, op], i) => {
    const x = 110 + i * 210, h = v * k; if (op <= 0.02) return;
    o += `<g opacity="${op}">` + SV.rect(x, base - h, 130, h, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.text(x + 65, base - h - 8, money(v, 1), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 65, base + 22, n, "sm", { "text-anchor": "middle" }) + "</g>";
  });
  if (s.t) o += SV.text(380, 40, s.t, "lbl bd t3", { "text-anchor": "middle", style: "font-size:17px" });
  return o;
}
Lib.stepper($("#stR"), { w: 760, h: 400, label: "Nominal and real GDP", base: { a: 0, b: 0, c: 0, t: "" }, draw: realChart, steps: [
  { cap: "In Year 1 GDP is <b>100</b>. This is the base year, so nominal and real GDP are the same.", s: { a: 1, b: 0, c: 0, t: "" } },
  { cap: "In Year 2 <b>nominal GDP</b> rises to <b>106</b>: up 6%. But did the economy really produce 6% more?", s: { a: 1, b: 1, c: 0, t: "Nominal GDP +6%" } },
  { cap: "Over the year <b>prices rose 4%</b>. Part of the rise in nominal GDP is just dearer goods, not extra goods.", s: { a: 1, b: 1, c: 0, t: "Prices +4%" } },
  { cap: "<b>Real GDP</b> adjusts for inflation: 106 ÷ 1.04 ≈ <b>101.9</b>. Real growth is only about <b>1.9%</b>. This is the figure used to measure economic growth.", s: { a: 1, b: 0.5, c: 1, t: "Real growth ≈ 1.9%" } },
] });
function growthChart(s) {
  const base = 320, k = 0.032, v0 = 8750, v1 = s.v; let o = SV.line(60, base, 700, base);
  [["2016", v0, "--muted"], ["2017", v1, "--accent"]].forEach(([n, v, c], i) => {
    const x = 160 + i * 250, h = v * k; o += SV.rect(x, base - h, 150, h, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.text(x + 75, base - h - 8, "$" + money(v, 1) + "bn", "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 75, base + 22, n, "sm", { "text-anchor": "middle" });
  });
  if (s.show > 0) o += SV.text(380, 40, "Growth = (" + money(v1, 1) + " − 8,750.0) ÷ 8,750.0 × 100 = " + money(((v1 - v0) / v0) * 100, 1) + "%", "lbl bd t3", { "text-anchor": "middle", style: "font-size:16px" });
  return o;
}
Lib.stepper($("#stK"), { w: 760, h: 400, label: "Calculating the growth rate", base: { v: 8750, show: 0 }, draw: growthChart, steps: [
  { cap: "India's real GDP in 2016 was <b>$8,750.0bn</b>.", s: { v: 8750, show: 0 } },
  { cap: "In 2017 it was <b>$9,362.5bn</b>: a rise of $612.5bn.", s: { v: 9362.5, show: 0 } },
  { cap: "<b>Growth rate = change ÷ original × 100</b> = 612.5 ÷ 8,750 × 100 = <b>7%</b>.", s: { v: 9362.5, show: 1 } },
] });

/* Lab 1: real growth and GDP per head */
function labR() {
  if (!$("#ra") || !$("#rb") || !$("#rc")) return;
  const nom = +$("#ra").value, inf = +$("#rb").value, pop = +$("#rc").value, real = ((1 + nom / 100) / (1 + inf / 100) - 1) * 100, pc = ((1 + real / 100) / (1 + pop / 100) - 1) * 100;
  $("#ra1").textContent = (real >= 0 ? "+" : "−") + money(Math.abs(real), 1) + "%"; $("#ra2").textContent = (pc >= 0 ? "+" : "−") + money(Math.abs(pc), 1) + "%"; $("#ra3").textContent = nom + "%";
  $("#rav").textContent = real < 0 ? "Prices rose by more than nominal GDP, so real GDP fell: the economy produced less, even though the money figure rose." : pc < 0 ? "Real GDP rose, but population grew faster, so real GDP per head fell: the average person is worse off." : `Real GDP rose by about ${money(real, 1)}%. After population growth, real GDP per head rose by about ${money(pc, 1)}%.`;
  const base = 300, k = 14; let o = SV.line(60, base, 700, base);
  [["Nominal GDP growth", nom, "--warn"], ["Real GDP growth", real, "--good"], ["Real GDP per head", pc, "--accent"]].forEach(([n, v, c], i) => {
    const x = 120 + i * 190, h = v * k, y = v >= 0 ? base - h : base;
    o += SV.rect(x, y, 130, Math.abs(h), "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.text(x + 65, v >= 0 ? y - 8 : y + Math.abs(h) + 18, (v >= 0 ? "+" : "−") + money(Math.abs(v), 1) + "%", "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 65, base + 40, n, "sm", { "text-anchor": "middle" });
  });
  $("#labR").innerHTML = o;
}
Lib.slider($("#g1"), { id: "ra", label: "Growth of nominal GDP", min: -2, max: 12, step: 0.5, value: 6, fmt: (v) => v + "%", onInput: labR });
Lib.slider($("#g2"), { id: "rb", label: "Inflation (rise in prices)", min: 0, max: 10, step: 0.5, value: 4, fmt: (v) => v + "%", onInput: labR });
Lib.slider($("#g3"), { id: "rc", label: "Population growth", min: 0, max: 4, step: 0.5, value: 1, fmt: (v) => v + "%", onInput: labR });

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each <b>included in GDP</b>, or <b>left out</b>?", buckets: [{ label: "Included in GDP" }, { label: "Left out of GDP" }], items: [
  { text: "A new car produced and sold in the country", b: 0 }, { text: "A haircut paid for", b: 0 }, { text: "Government spending on schools", b: 0 }, { text: "Machinery produced for a factory", b: 0 },
  { text: "Unpaid housework", b: 1 }, { text: "Goods made and sold in the informal economy", b: 1 }, { text: "Second-hand goods resold", b: 1 }, { text: "The value of pollution caused", b: 1 },
], done: "GDP counts final goods and services produced and recorded." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["GDP", "Total value of final goods and services produced in a country in a year"],
  ["Nominal GDP", "GDP at current prices, not adjusted for inflation"],
  ["Real GDP", "GDP adjusted for inflation: measures change in output"],
  ["GDP per head", "GDP divided by population"],
  ["Informal economy", "Activity that is not regulated, recorded or taxed"],
  ["Economic growth rate", "Percentage change in real GDP"],
], done: "Good vocabulary scores marks." });
Lib.calc($("#c1"), { qs: [
  { q: "Real GDP was $500bn last year and is $520bn this year. What is the growth rate (%)?", a: 4, sol: "20 ÷ 500 × 100 = <b>4%</b>." },
  { q: "Nominal GDP rises by 7% and prices rise by 3%. About what is the rise in real GDP (%)?", a: 4, hint: "Subtract inflation.", sol: "7 − 3 = <b>about 4%</b>." },
  { q: "An economy has real GDP of $600bn and a population of 20 million. What is real GDP per head ($)?", a: 30000, hint: "$600bn = 600,000m.", sol: "$600bn ÷ 20m = <b>$30,000</b>." },
  { q: "Real GDP grows by 3% but population grows by 4%. What is the approximate change in real GDP per head (%)?", a: -1, sol: "3 − 4 = <b>about −1%</b>: population grew faster than output, so real GDP per head falls." },
  { q: "Real GDP was 200 in Year 1, 210 in Year 2 and 207 in Year 3. What is the growth rate in Year 3 (%, 1 d.p.)?", a: -1.4, tol: 0.1, sol: "(207 − 210) ÷ 210 × 100 = <b>−1.4%</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What does real GDP measure?", opts: ["Output adjusted for inflation", "Prices only", "The size of the population", "Government spending"], a: 0, why: "Real GDP shows output at constant prices." },
  { q: "Nominal GDP rises by 5% and prices rise by 5%. Real GDP is likely to:", opts: ["Rise by 5%", "Stay about the same", "Fall by 5%", "Double"], a: 1, why: "All the rise is due to price increases." },
  { q: "Which is a limitation of GDP as a measure of living standards?", opts: ["It includes all output", "It does not show how income is shared", "It uses prices", "It is measured in money"], a: 1, why: "Averages hide inequality." },
  { q: "Real GDP per head is calculated as:", opts: ["Real GDP × population", "Real GDP ÷ population", "Nominal GDP ÷ prices", "Real GDP − population"], a: 1, why: "Divide by the number of people." },
  { q: "Which is not counted in GDP?", opts: ["Government spending on roads", "Unpaid housework", "Exports of cars", "A restaurant meal"], a: 1, why: "Unpaid work is not recorded." },
] });

Lib.cards($("#fc1"), { cards: [
  ["GDP", "The total value of final goods and services produced in a country in a year."],
  ["Nominal GDP", "GDP measured at current prices, not adjusted for inflation."],
  ["Real GDP", "GDP adjusted for inflation: measures the actual change in output."],
  ["GDP per head", "GDP divided by population."],
  ["Growth rate", "The percentage change in real GDP."],
  ["Informal economy", "The part of the economy not regulated, protected or taxed by the government."],
  ["Base year", "The year whose prices are used as the starting point for real GDP."],
  ["Living standards", "The quality and quantity of goods and services people can obtain."],
] });
labR();
