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
  const base = 320, k = 0.22; let o = SV.line(60, base, 710, base);
  const bars = [["Savings today", 1000, "--muted", clamp(s.n, 0, 1)], ["After a year: money", 1030, "--accent", clamp(s.n - 1, 0, 1)], ["After a year: what it buys", 1030 / 1.05, "--bad", clamp(s.n - 2, 0, 1)]];
  bars.forEach(([n, v, c, op], i) => { if (op <= 0) return; const x = 110 + i * 200, h = v * k; o += `<g opacity="${op}">` + SV.rect(x, base - h, 130, h, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.text(x + 65, base - h - 8, "$" + money(v, 0), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 65, base + 22, n, "sm", { "text-anchor": "middle" }) + "</g>"; });
  if (s.n > 3) o += SV.text(380, 50, "Real value falls by about 1.9%: a real interest rate of about −2%", "lbl bd t2", { "text-anchor": "middle", style: "font-size:16px" });
  return o;
}
Lib.stepper($("#stS"), { w: 760, h: 400, label: "What inflation does to savings", base: { n: 0 }, draw: realChart, steps: [
  { cap: "A saver has <b>$1,000</b>. The bank pays <b>3% interest</b>.", s: { n: 1 } },
  { cap: "After a year she has <b>$1,030</b>: a nominal rise of 3%.", s: { n: 2 } },
  { cap: "But prices rose <b>5%</b>. In terms of what the money buys, $1,030 is worth only about <b>$981</b> in last year's prices.", s: { n: 3 } },
  { cap: "She has <b>lost purchasing power</b>: the <b>real interest rate</b> is 3% − 5% = about <b>−2%</b>. A <b>borrower</b> with a fixed-rate loan gains in the same way, as their debt is worth less.", s: { n: 4 } },
] });
const ICH = ["Inflation in the country is higher than in its trading partners", "Its exports become dearer than rivals' exports", "Foreign buyers switch away: exports fall", "Imports look cheaper, so imports rise", "The current account moves towards deficit", "Output and jobs in export industries are hit"];
Lib.stepper($("#stX"), { w: 760, h: 400, label: "Inflation and international competitiveness", base: { n: 0 }, draw: mkChain(ICH, "--bad"), steps: chainSteps(["The country has <b>higher inflation</b> than its trading partners.", "Its goods become <b>dearer</b> compared with rivals'.", "Foreign buyers <b>switch away</b>: exports fall.", "Domestic buyers switch to cheaper <b>imports</b>.", "The <b>current account</b> moves towards deficit.", "Output and jobs in export industries are hit: a cost of high inflation to the economy."]) });

/* Lab 1: real interest rate */
function labR() {
  if (!$("#ra") || !$("#rb")) return;
  const i = +$("#ra").value, p = +$("#rb").value, real = ((1 + i / 100) / (1 + p / 100) - 1) * 100, sav = 10000 * real / 100;
  $("#ra1").textContent = (real >= 0 ? "+" : "−") + money(Math.abs(real), 1) + "%"; $("#ra2").textContent = (sav >= 0 ? "+$" : "−$") + Math.abs(Math.round(sav)).toLocaleString("en-US");
  $("#ra3").textContent = real < -0.05 ? "Borrowers" : real > 0.05 ? "Savers" : "Neither";
  $("#rav").textContent = real < -0.05 ? `Inflation (${p}%) is higher than the interest rate (${i}%), so the real rate is ${money(real, 1)}%. Savers lose purchasing power; borrowers gain because their debt is worth less in real terms.` : real > 0.05 ? `Interest (${i}%) is above inflation (${p}%): savers earn a positive real return and borrowers pay a real cost.` : "Interest equals inflation: savers just keep their purchasing power.";
  const base = 290, k = 14; let o = SV.line(60, base, 700, base);
  [["Nominal interest", i, "--accent"], ["Inflation", p, "--bad"], ["Real interest", real, real >= 0 ? "--good" : "--warn"]].forEach(([n, v, c], j) => { const x = 120 + j * 190, h = Math.abs(v) * k, y = v >= 0 ? base - h : base; o += SV.rect(x, y, 130, h, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.text(x + 65, v >= 0 ? y - 8 : y + h + 16, (v >= 0 ? "" : "−") + money(Math.abs(v), 1) + "%", "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 65, base + 40, n, "sm", { "text-anchor": "middle" }); });
  $("#labR").innerHTML = o;
}
Lib.slider($("#g1"), { id: "ra", label: "Nominal interest rate", min: 0, max: 12, step: 0.5, value: 3, fmt: (v) => v + "%", onInput: labR });
Lib.slider($("#g2"), { id: "rb", label: "Inflation rate", min: -2, max: 15, step: 0.5, value: 5, fmt: (v) => v + "%", onInput: labR });
const WG = [
  { n: "Savers", g: "Gain if the interest rate is above inflation.", l: "Lose purchasing power if inflation is above the interest rate." },
  { n: "Lenders", g: "Gain if rates rise with inflation or are variable.", l: "Lose with fixed-rate loans when inflation rises: repaid in money worth less." },
  { n: "Borrowers", g: "The real value of the debt falls (fixed-rate loans).", l: "Lose if interest rates are raised to fight inflation (variable rates)." },
  { n: "Pensioners and fixed incomes", g: "Few gains unless pensions rise with prices.", l: "Purchasing power falls each year." },
  { n: "Workers", g: "Gain if wages rise faster than prices.", l: "Real wages fall if pay lags inflation; uncertainty and disputes." },
  { n: "Firms", g: "May gain if prices rise faster than costs; debts eased.", l: "Higher costs, menu costs, uncertainty, and exports less competitive." },
  { n: "Exporters", g: "None, unless inflation is lower than rivals'.", l: "Higher prices abroad reduce sales if inflation is higher than competitors'." },
];
button_table("wgBtns", "wgOut", WG, 0, (p) => `<div class="tw"><table class="t"><tr><th>Possible gains</th><th>Possible losses</th></tr><tr><td>${p.g}</td><td>${p.l}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "When inflation is <b>higher than the interest rate</b>, who is likely to <b>gain</b> and who to <b>lose</b>?", buckets: [{ label: "Gains" }, { label: "Loses" }], items: [
  { text: "A borrower with a fixed-rate loan", b: 0 }, { text: "A household whose mortgage debt is worth less in real terms", b: 0 }, { text: "A firm whose output prices rise faster than costs", b: 0 },
  { text: "A saver with money in a bank account", b: 1 }, { text: "A pensioner on a fixed income", b: 1 }, { text: "A lender with a fixed-rate loan", b: 1 }, { text: "An exporter whose prices rise above competitors'", b: 1 },
], done: "Real interest rate = nominal rate − inflation." });
Lib.classify($("#cl2"), { prompt: "Is each a consequence of <b>inflation</b> or of <b>deflation</b>?", buckets: [{ label: "Inflation" }, { label: "Deflation" }], items: [
  { text: "Purchasing power of money falls", b: 0 }, { text: "Exports become less competitive if inflation is above rivals'", b: 0 }, { text: "Savers lose purchasing power", b: 0 },
  { text: "Consumers delay spending, expecting lower prices", b: 1 }, { text: "The real value of debt rises", b: 1 }, { text: "Firms' profits fall and jobs may be cut", b: 1 },
], done: "Both can cause problems: stable prices are the aim." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Real interest rate", "Nominal interest rate minus inflation"],
  ["Nominal interest rate", "The interest rate not adjusted for inflation"],
  ["Menu costs", "The cost to firms of changing prices"],
  ["Fixed income", "Income that does not rise with prices, such as some pensions"],
  ["Real wage", "Wages adjusted for inflation: what pay can buy"],
  ["Price competitiveness", "How cheap a country's goods are compared with rivals'"],
], done: "Good vocabulary scores marks." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how deflation could cause a recession</b>.", items: [
  "The price level falls",
  "Consumers expect lower prices and delay spending",
  "Total demand falls",
  "Firms' sales and profits fall",
  "Firms cut output and jobs: unemployment rises",
  "Real GDP falls: recession",
], done: "Why deflation can harm an economy." });
Lib.calc($("#c1"), { qs: [
  { q: "Interest on savings is 4% and inflation is 6%. What is the real interest rate (%)?", a: -2, sol: "4 − 6 = <b>−2%</b>." },
  { q: "A worker's pay rises 3% while inflation is 5%. What is the approximate change in real pay (%)?", a: -2, sol: "3 − 5 = <b>−2%</b>." },
  { q: "A saver has $2,000 earning 2% interest while inflation is 5%. After a year she has $2,040. What would the original basket of goods cost now ($)?", a: 2100, sol: "2,000 × 1.05 = <b>$2,100</b>, so she cannot afford it." },
  { q: "A borrower owes $10,000 at a fixed rate. After a year of 8% inflation, what is the debt worth in last year's prices (nearest $)?", a: 9259, tol: 1, sol: "10,000 ÷ 1.08 ≈ <b>$9,259</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Who is most likely to gain from unexpected inflation?", opts: ["A saver", "A pensioner on a fixed income", "A borrower with a fixed-rate loan", "A lender with a fixed-rate loan"], a: 2, why: "The real value of the debt falls." },
  { q: "The real interest rate is:", opts: ["Nominal rate + inflation", "Nominal rate − inflation", "Inflation − nominal rate", "The base rate"], a: 1, why: "Adjust for inflation." },
  { q: "A consequence of high inflation for exporters is:", opts: ["Exports become more competitive", "Exports become less competitive if inflation is higher than rivals'", "No effect", "Exports are always higher"], a: 1, why: "Prices rise relative to competitors'." },
  { q: "A harmful effect of deflation is:", opts: ["People delay spending", "Prices rise", "Debt falls", "Savers lose"], a: 0, why: "Expecting lower prices, they wait." },
  { q: "A benefit of low inflation is:", opts: ["Uncertainty", "Higher interest rates", "Price stability that encourages investment", "Lower exports"], a: 2, why: "Certainty helps firms plan." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Real interest rate", "The nominal interest rate minus the inflation rate."],
  ["Nominal interest rate", "The interest rate before adjusting for inflation."],
  ["Real wage", "Wages adjusted for inflation: what pay can actually buy."],
  ["Menu costs", "The costs to firms of changing prices."],
  ["Fixed income", "Income that does not change with prices, such as some pensions."],
  ["Price competitiveness", "How cheap a country's goods are compared with those of rivals."],
  ["Redistribution by inflation", "Inflation moves wealth from lenders and savers to borrowers."],
  ["Debt deflation", "When falling prices raise the real value of debts."],
  ["Hyperinflation", "Extremely rapid inflation that destroys confidence in money."],
] });
labR();
