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
const D = (b) => [-b, 50 + 50 * b], S = (d, shift = 0) => [d, 50 - 50 * d + shift];
const fmtSteep = (v) => (v < 0.8 ? "flat (elastic)" : v > 1.4 ? "steep (inelastic)" : "medium");
const money = (v, d = 1) => Lib.fmtN(v, d);

/* AD components bar */
function compChart(s) {
  const parts = [["C", s.c, "--accent"], ["I", s.i, "--good"], ["G", s.g, "--n"], ["X", s.x, "--warn"]], m = s.m, base = 330, k = 2.1;
  let o = SV.line(60, base, 700, base), y = base;
  parts.forEach(([n, v, col]) => {
    const h = v * k; y -= h;
    o += SV.rect(150, y, 130, h, "", { style: `fill:var(${col})`, opacity: 0.85 }) + SV.text(215, y + h / 2 + 5, n + " = " + money(v, 0), "lbl bd", { "text-anchor": "middle", style: "fill:var(--surface)" });
  });
  const total = parts.reduce((a, p) => a + p[1], 0), ad = total - m;
  o += SV.rect(420, base - m * k, 130, m * k, "", { style: "fill:var(--bad)", opacity: 0.75 }) + SV.text(485, base - m * k / 2 + 5, "M = " + money(m, 0), "lbl bd", { "text-anchor": "middle", style: "fill:var(--surface)" });
  o += SV.text(215, base + 22, "Spending on output", "sm", { "text-anchor": "middle" }) + SV.text(485, base + 22, "Leaks to imports", "sm", { "text-anchor": "middle" });
  o += SV.text(380, 40, "AD = C + I + G + (X − M) = " + money(ad, 0), "lbl bd " + (ad > 100.5 ? "t3" : ad < 99.5 ? "t2" : ""), { "text-anchor": "middle", style: "font-size:19px" });
  return o;
}

Lib.stepper($("#stK"), { w: 760, h: 400, label: "Fiscal policy changes the parts of AD", base: { c: 60, i: 20, g: 25, x: 20, m: 25 }, draw: compChart, steps: [
  { cap: "AD = <b>C + I + G + (X − M)</b>. Here C = 60, I = 20, G = 25, X = 20 and M = 25, so <b>AD = 100</b>.", s: { c: 60, i: 20, g: 25, x: 20, m: 25 } },
  { cap: "<b>Expansionary:</b> the government raises its own spending <b>G</b> by 10. AD rises by 10 straight away.", s: { c: 60, g: 35 } },
  { cap: "It also <b>cuts income tax</b>. Households keep more pay, so C rises by about 7 (some of the cut is saved). AD rises again.", s: { c: 67, g: 35 } },
  { cap: "<b>Contractionary:</b> now the government cuts G by 10 and raises taxes. G falls straight away and C falls too. <b>AD falls below 100.</b>", s: { c: 53, g: 15 } },
] });

function labC() {
  if (!$("#ca") || !$("#cb")) return;
  const dG = +$("#ca").value, dT = +$("#cb").value, c = 60 - 0.7 * dT, g = 25 + dG, ad = c + 20 + g + 20 - 25, d = ad - 100;
  $("#ca1").textContent = money(ad, 1); $("#ca2").textContent = (d > 0 ? "+" : d < 0 ? "−" : "") + money(Math.abs(d), 1); $("#ca3").textContent = d > 1 ? "Expansionary" : d < -1 ? "Contractionary" : "Neutral";
  $("#cav").textContent = Math.abs(d) <= 1 ? "The changes roughly cancel out: neutral." : d > 0 ? "AD rises. A rise in G adds straight to AD, and a tax cut raises consumption (but only 70% of it is spent): expansionary." : "AD falls, as lower G and higher taxes reduce spending: contractionary.";
  $("#labC").innerHTML = compChart({ c, i: 20, g, x: 20, m: 25 });
}
Lib.slider($("#g1"), { id: "ca", label: "Change in government spending (G)", min: -15, max: 15, step: 1, value: 0, fmt: (v) => (v > 0 ? "+" : v < 0 ? "−" : "") + Math.abs(v), onInput: labC });
Lib.slider($("#g2"), { id: "cb", label: "Change in taxes (+ = tax rise)", min: -15, max: 15, step: 1, value: 0, fmt: (v) => (v > 0 ? "+" : v < 0 ? "−" : "") + Math.abs(v), onInput: labC });

/* ================= PRACTISE ================= */
Lib.classify($("#cl3"), { prompt: "Which would be <b>expansionary</b> and which <b>contractionary</b> fiscal policy?", buckets: [{ label: "Expansionary" }, { label: "Contractionary" }], items: [
  { text: "Cut income tax rates", b: 0 }, { text: "Raise spending on roads and rail", b: 0 }, { text: "Raise the tax-free allowance", b: 0 }, { text: "Increase benefits for the unemployed", b: 0 },
  { text: "Cut government spending on education", b: 1 }, { text: "Raise VAT", b: 1 }, { text: "Raise corporation tax", b: 1 }, { text: "Freeze public sector pay and cut projects", b: 1 },
], done: "Expansionary raises AD; contractionary reduces it." });
Lib.classify($("#cl4"), { prompt: "Which kind of policy is each? <b>Fiscal</b>, <b>monetary</b> or <b>supply-side</b>?", buckets: [{ label: "Fiscal" }, { label: "Monetary" }, { label: "Supply-side" }], items: [
  { text: "Cut income tax rates", b: 0 }, { text: "Raise spending on hospitals", b: 0 },
  { text: "Central bank cuts the interest rate", b: 1 }, { text: "Central bank increases the money supply", b: 1 },
  { text: "Government funds more training for workers", b: 2 }, { text: "Government privatises a state firm", b: 2 },
  { text: "Government raises VAT", b: 0 }, { text: "Government lets the currency fall", b: 1 },
], done: "Fiscal: taxes and government spending. Monetary: rates, money, exchange rate. Supply-side: raise AS." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Budget deficit", "Government spending is higher than revenue"],
  ["Budget surplus", "Government revenue is higher than spending"],
  ["National debt", "Total amount the government has borrowed over time"],
  ["Multiplier effect", "Final change in AD is larger than the initial change"],
  ["Automatic stabilisers", "Spending and taxes that cushion booms and slumps with no policy change"],
  ["Tax incidence", "How the burden of an indirect tax is shared between consumers and producers"],
  ["Fiscal policy", "Government spending and taxation decisions to influence AD"],
], done: "Good vocabulary scores marks." });
Lib.order($("#o1"), { prompt: "Put the chain for <b>expansionary fiscal policy</b> in order.", items: [
  "The government cuts income tax rates",
  "Households' disposable income rises",
  "Consumption rises (and investment may follow)",
  "Aggregate demand shifts to the right",
  "Real GDP rises and firms take on more workers",
  "The price level may rise and the budget deficit may widen",
], done: "A full analysis chain." });
Lib.calc($("#c1"), { qs: [
  { q: "Consumption is $300bn, investment $80bn, government spending $100bn, exports $90bn and imports $110bn. Calculate AD ($bn).", a: 460, sol: "AD = 300 + 80 + 100 + (90 − 110) = <b>$460bn</b>." },
  { q: "In the same economy government spending rises by $20bn and nothing else changes. What is the new AD ($bn)?", a: 480, sol: "460 + 20 = <b>$480bn</b> (before any multiplier effect)." },
  { q: "AD is $500bn. The government's policy lowers it by 4%. What is the new AD ($bn)?", a: 480, sol: "500 × 0.96 = <b>$480bn</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What is fiscal policy?", opts: ["Changes in interest rates", "Changes in government spending and taxation", "Changes in the money supply", "Changes in the exchange rate"], a: 1, why: "Fiscal policy is the use of government spending and taxes to influence AD." },
  { q: "Which is a likely effect of expansionary fiscal policy?", opts: ["AD shifts left", "Real GDP and employment are likely to rise", "The budget moves towards surplus", "The price level is certain to fall"], a: 1, why: "Higher spending or lower taxes raise AD." },
  { q: "Which part of AD does a government change directly?", opts: ["C", "I", "G", "X − M"], a: 2, why: "G is government spending." },
  { q: "Who usually makes decisions on interest rates, rather than on taxes and spending?", opts: ["The central bank", "The tax authority", "Trade unions", "Households"], a: 0, why: "Interest rates are monetary policy." },
  { q: "Which is contractionary fiscal policy?", opts: ["Cutting income tax", "Raising government spending", "Raising taxes and cutting spending", "Cutting interest rates"], a: 2, why: "It reduces AD." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Fiscal policy", "Government spending and taxation decisions to influence AD"],
  ["Fiscal policy", "Decisions on government spending and taxation designed to influence aggregate demand."],
  ["Expansionary fiscal policy", "Rises in government spending and/or cuts in taxation designed to increase AD."],
  ["Contractionary fiscal policy", "Cuts in government spending and/or rises in taxation designed to reduce AD."],
  ["Automatic stabilisers", "Spending and taxes that cushion booms and slumps with no policy change"],
  ["Automatic stabilisers", "Government spending and taxation that reduce fluctuations in economic activity with no change in policy."],
  ["Aggregate demand", "Total spending on a country's goods and services: C + I + G + (X − M)."],
  ["Discretionary fiscal policy", "A deliberate decision to change government spending or taxes."],
  ["Monetary policy", "Use of interest rates, money supply and the exchange rate to influence AD."],
  ["Supply-side policy", "Measures to raise the economy's ability to produce, shifting AS right."],
] });
labC();
