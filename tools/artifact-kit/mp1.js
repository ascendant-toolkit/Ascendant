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

const WHO = ["The central bank sets the base interest rate and controls the money supply", "Commercial banks change their lending and saving rates", "Households and firms borrow, save and spend differently", "Total spending (aggregate demand) changes", "Output, jobs and prices respond"];
function flowChart(s) {
  const bh = 52, gap = 22, x = 110, w = 540; let o = "";
  WHO.forEach((t, i) => {
    const v = clamp(s.n - i, 0, 1); if (v <= 0) return;
    const y = 14 + i * (bh + gap);
    let g = SV.rect(x, y, w, bh, "", { rx: 8, style: "fill:var(--accent);fill-opacity:0.14;stroke:var(--accent);stroke-width:2" });
    g += SV.circle(x - 28, y + bh / 2, 15, "dot1") + SV.text(x - 28, y + bh / 2 + 5, i + 1, "lbl bd", { "text-anchor": "middle", style: "fill:var(--surface);font-size:14px" });
    g += SV.text(x + w / 2, y + bh / 2 + 5, t, "lbl bd", { "text-anchor": "middle", style: "font-size:14px" });
    if (i < WHO.length - 1) g += SV.line(x + w / 2, y + bh + 1, x + w / 2, y + bh + gap - 3, "ax", { style: "stroke-width:2" }) + SV.arrowHead(x + w / 2, y + bh + gap, "d", "dot1");
    o += `<g opacity="${v}">${g}</g>`;
  });
  return o;
}
Lib.stepper($("#stW"), { w: 760, h: 400, label: "Who does what in monetary policy", base: { n: 0 }, draw: flowChart, steps: [
  { cap: "In most countries the <b>central bank</b> runs monetary policy. It sets the <b>base interest rate</b> and can change the <b>money supply</b>.", s: { n: 1 } },
  { cap: "<b>Commercial banks</b> follow the central bank, raising or lowering the rates on loans, mortgages and savings.", s: { n: 2 } },
  { cap: "<b>Households and firms</b> respond to the new rates by borrowing, saving and spending more or less.", s: { n: 3 } },
  { cap: "Their decisions change <b>total spending: aggregate demand</b>.", s: { n: 4 } },
  { cap: "Output, jobs and prices respond. That is why monetary policy is aimed at <b>aggregate demand and inflation</b>.", s: { n: 5 } },
] });
/* ---------- 4. AD / AS ---------- */
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
Lib.stepper($("#stA"), { w: 760, h: 400, label: "Monetary policy shifting aggregate demand", base: { sh: 0 }, draw: adChart, steps: [
  { cap: "The economy starts at <b>Y</b> and <b>P</b> where AD meets AS. <b>AD = C + I + G + (X − M)</b>. Monetary policy works on <b>C and I</b> (interest rates, money supply) and on <b>X − M</b> (exchange rate).", s: { sh: 0 } },
  { cap: "<b>Expansionary monetary policy</b>: lower interest rates, a bigger money supply and/or a lower exchange rate. AD shifts <b>right</b> to AD₁. Real GDP rises (<b>growth</b>), unemployment is likely to fall and the price level edges up.", s: { sh: 15 } },
  { cap: "<b>Evaluate:</b> push too hard when the economy is close to full capacity and AS is steep. Output barely rises and most of the effect is a <b>higher price level</b>: inflation. Imports may also rise and the exchange rate fall further.", s: { sh: 40 } },
  { cap: "<b>Contractionary monetary policy</b>: higher interest rates, a smaller money supply and/or a higher exchange rate. AD shifts <b>left</b> to AD₂. Inflation pressure eases, but output and jobs are likely to fall too.", s: { sh: -15 } },
] });


function labW() {
  if (!$("#wa")) return;
  const r = +$("#wa").value, sv = Math.max(0, r - 1), ln = r + 3;
  $("#wa1").textContent = money(sv, 1) + "%"; $("#wa2").textContent = money(ln, 1) + "%";
  $("#wa3").textContent = "$" + Math.round(200000 * ln / 100).toLocaleString("en-US"); $("#wa4").textContent = "$" + Math.round(10000 * sv / 100).toLocaleString("en-US");
  $("#wav").textContent = r <= 2 ? "A low base rate means cheap borrowing and little reward for saving: households and firms are likely to spend and invest more." : r >= 7 ? "A high base rate makes borrowing expensive and saving rewarding: spending and investment are likely to fall." : "A middle rate: neither strongly encouraging nor discouraging spending.";
  const base = 290, k = 17; let o = SV.line(60, base, 700, base);
  [["Savings rate", sv, "--good"], ["Base rate", r, "--accent"], ["Loan rate", ln, "--bad"]].forEach(([n, v, c], i) => {
    const x = 130 + i * 190, h = v * k;
    o += SV.rect(x, base - h, 120, h, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.text(x + 60, base - h - 8, money(v, 1) + "%", "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 60, base + 22, n, "sm", { "text-anchor": "middle" });
  });
  $("#labW").innerHTML = o;
}
Lib.slider($("#g1"), { id: "wa", label: "Central bank base rate", min: 0, max: 10, step: 0.5, value: 4, fmt: (v) => v + "%", onInput: labW });
const TOOLS = [["Interest rate", ["Raise", "Hold", "Cut"]], ["Money supply", ["Reduce", "Hold", "Increase"]], ["Exchange rate", ["Raise", "Hold", "Lower"]]];
const pick = [1, 1, 1];
function stance() {
  $("#stBtns").innerHTML = TOOLS.map(([n, o], i) => `<div class="row" style="margin:6px 0"><b style="min-width:120px;display:inline-block">${n}</b>${o.map((t, j) => `<button class="b${pick[i] === j ? " pri" : ""}" data-i="${i}" data-j="${j}">${t}</button>`).join("")}</div>`).join("");
  $$("#stBtns .b").forEach((b) => (b.onclick = () => { pick[+b.dataset.i] = +b.dataset.j; stance(); }));
  const sc = pick.reduce((a, j) => a + (j - 1), 0);
  $("#stOut").textContent = sc >= 2 ? "Expansionary: these moves are likely to raise aggregate demand. Watch for inflation." : sc <= -2 ? "Contractionary: these moves are likely to reduce aggregate demand. Watch for unemployment." : sc === 0 && pick.every((j) => j === 1) ? "No change: policy is unchanged." : sc > 0 ? "Mildly expansionary: the net effect is a modest rise in AD." : sc < 0 ? "Mildly contractionary: the net effect is a modest fall in AD." : "Mixed: the moves pull in opposite directions, so the overall effect on AD is small.";
}
stance();

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Would each be <b>expansionary</b> or <b>contractionary</b> monetary policy?", buckets: [{ label: "Expansionary" }, { label: "Contractionary" }], items: [
  { text: "Cut the base interest rate", b: 0 }, { text: "Buy government bonds to increase the money supply", b: 0 }, { text: "Allow the currency to fall", b: 0 }, { text: "Quantitative easing", b: 0 },
  { text: "Raise the base interest rate", b: 1 }, { text: "Sell government bonds to reduce the money supply", b: 1 }, { text: "Revalue the currency upwards", b: 1 }, { text: "Make bank loans harder to get", b: 1 },
], done: "Expansionary raises AD; contractionary reduces it." });
Lib.classify($("#cl2"), { prompt: "Is each <b>fiscal</b> or <b>monetary</b> policy?", buckets: [{ label: "Fiscal policy" }, { label: "Monetary policy" }], items: [
  { text: "Raise income tax", b: 0 }, { text: "Build a new hospital", b: 0 }, { text: "Cut VAT", b: 0 }, { text: "Increase unemployment benefit", b: 0 },
  { text: "Central bank cuts the base rate", b: 1 }, { text: "Central bank buys government bonds", b: 1 }, { text: "Currency allowed to fall", b: 1 }, { text: "Central bank raises its lending rate", b: 1 },
], done: "Fiscal: government spending and taxes. Monetary: interest rates, money supply, exchange rate." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Money supply", "Total amount of money in an economy"],
  ["Monetary policy", "Use of money supply, interest rates and exchange rates to influence AD and inflation"],
  ["Central bank", "Banker to the government and commercial banks, and monetary authority"],
  ["Commercial bank", "A bank that takes deposits and makes loans to households and firms"],
  ["Base rate", "The central bank's main interest rate"],
  ["Expansionary policy", "Aims to raise aggregate demand"],
  ["Contractionary policy", "Aims to reduce aggregate demand"],
], done: "Good vocabulary scores marks." });
Lib.order($("#o1"), { prompt: "Put the <b>chain of control</b> in order.", items: [
  "The central bank changes the base interest rate",
  "Commercial banks change their loan and saving rates",
  "Households and firms borrow, save and spend differently",
  "Aggregate demand changes",
  "Output, jobs and prices respond",
], done: "The route from the central bank to the economy." });
Lib.calc($("#c1"), { qs: [
  { q: "A saver deposits $5,000 at an interest rate of 4% a year. How much interest does she earn in one year ($)?", a: 200, sol: "5,000 × 4% = <b>$200</b>." },
  { q: "The money supply is $800bn. It increases by 5%. What is the new money supply ($bn)?", a: 840, sol: "800 × 1.05 = <b>$840bn</b>." },
  { q: "The money supply is $500bn. It rises by 8%. What is the new money supply ($bn)?", a: 540, sol: "500 × 1.08 = <b>$540bn</b>." },
  { q: "A bank pays 3% interest on savings. How much interest does $2,000 earn in a year ($)?", a: 60, sol: "2,000 × 3% = <b>$60</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What is the money supply?", opts: ["The amount of money the government spends", "The total amount of money in an economy", "The amount of gold a country holds", "The amount of tax collected"], a: 1, why: "It includes notes, coins and bank deposits." },
  { q: "Which organisation usually carries out monetary policy?", opts: ["The central bank", "The tax authority", "A trade union", "A commercial firm"], a: 0, why: "The central bank sets interest rates and influences the money supply." },
  { q: "Which is a monetary policy measure?", opts: ["Cutting income tax", "Cutting the base interest rate", "Building a motorway", "Raising VAT"], a: 1, why: "Interest rates are monetary; tax and spending are fiscal." },
  { q: "Which is expansionary monetary policy?", opts: ["Raising interest rates", "Increasing the money supply", "Raising the exchange rate", "Cutting government spending"], a: 1, why: "A bigger money supply tends to lower rates and raise spending." },
  { q: "The main aim of monetary policy is to influence:", opts: ["Aggregate demand and inflation", "The size of firms", "The level of tax revenue only", "Population growth"], a: 0, why: "Monetary policy works through AD and the price level." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Money supply", "The total amount of money in an economy."],
  ["Monetary policy", "The use of the money supply, interest rates and the foreign exchange rate to influence aggregate demand and inflation."],
  ["Central bank", "The government's banker and monetary authority: sets the base interest rate and manages the money supply."],
  ["Interest rate", "The price of borrowing and the reward for saving."],
  ["Base rate", "The central bank's main interest rate, which commercial banks follow."],
  ["Expansionary monetary policy", "Lower interest rates, a bigger money supply and/or a lower exchange rate to raise AD."],
  ["Contractionary monetary policy", "Higher interest rates, a smaller money supply and/or a higher exchange rate to reduce AD."],
] });
labW();
