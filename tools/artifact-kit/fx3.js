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

function fxm(s) {
  const d = s.d || 0, sp = s.s || 0, q0 = 50, p0 = 60, q1 = (100 + d + sp) / 2, p1 = 60 + (d - sp) / 2, lab = (p) => "$" + (p / 50).toFixed(2), moved = Math.abs(d) + Math.abs(sp) > 1;
  let o = SV.line(QX(0), PY(120), QX(0), PY(0)) + SV.line(QX(0), PY(0), QX(104), PY(0)) + SV.text(QX(0) + 6, PY(120) + 6, "Exchange rate ($ per £1)", "sm") + SV.text(QX(104), PY(0) + 22, "Quantity of pounds traded", "sm", { "text-anchor": "end" });
  o += curve(-1, 110, "c1", "D", { t: "t1", attrs: { opacity: d ? 0.4 : 1 } }) + curve(1, 10, "c3", "S", { t: "t3", attrs: { opacity: sp ? 0.4 : 1 } });
  if (d) o += curve(-1, 110 + d, "c2", "D₁", { t: "t2" });
  if (sp) o += curve(1, 10 - sp, "c4", "S₁", { t: "t4", dx: 4, dy: 10 });
  o += SV.line(QX(0), PY(p0), QX(q0), PY(p0), "gr") + SV.line(QX(q0), PY(p0), QX(q0), PY(0), "gr") + SV.circle(QX(q0), PY(p0), 6, "dot1", { opacity: moved ? 0.45 : 1 }) + ylab(p0, lab(p0)) + xlab(q0, "Q");
  if (moved) o += SV.line(QX(0), PY(p1), QX(q1), PY(p1), "gr") + SV.line(QX(q1), PY(p1), QX(q1), PY(0), "gr") + SV.circle(QX(q1), PY(p1), 6, "dot2") + ylab(p1, lab(p1), "sm bd") + xlab(q1, "Q₁", "sm bd");
  if (s.t) o += SV.text(380, 30, s.t, "lbl bd t3", { "text-anchor": "middle", style: "font-size:16px" });
  return o;
}

Lib.stepper($("#stM"), { w: 760, h: 400, label: "The market for a currency", base: { d: 0, s: 0, t: "" }, draw: fxm, steps: [
  { cap: "Demand for pounds slopes down and supply slopes up. They meet at an <b>equilibrium exchange rate of $1.20 per £1</b>.", s: { d: 0, s: 0, t: "" } },
  { cap: "<b>Higher demand for UK exports</b> (or a higher UK interest rate, or speculation that the pound will rise) shifts <b>demand right</b> to D₁. The rate rises to about <b>$1.40</b>: an <b>appreciation</b>.", s: { d: 20, s: 0, t: "Appreciation" } },
  { cap: "Instead <b>more imports</b> (or UK investment abroad) shifts <b>supply right</b> to S₁. The pound falls to about <b>$1.00</b>: a <b>depreciation</b>.", s: { d: 0, s: 20, t: "Depreciation" } },
  { cap: "A <b>cut in the interest rate</b> reduces demand and raises supply as hot money leaves: the pound <b>depreciates</b> sharply.", s: { d: -16, s: 16, t: "Depreciation" } },
  { cap: "A <b>rise in the interest rate</b> does the opposite: demand shifts right, supply shifts left and the pound <b>appreciates</b>.", s: { d: 16, s: -16, t: "Appreciation" } },
] });
function fixChart(s) {
  const pf = s.pf, qd = 110 - pf, qs = pf - 10; let o = SV.line(QX(0), PY(120), QX(0), PY(0)) + SV.line(QX(0), PY(0), QX(104), PY(0)) + SV.text(QX(0) + 6, PY(120) + 6, "Exchange rate ($ per £1)", "sm") + SV.text(QX(104), PY(0) + 22, "Quantity of pounds", "sm", { "text-anchor": "end" });
  o += curve(-1, 110, "c1", "D", { t: "t1" }) + curve(1, 10, "c3", "S", { t: "t3" }) + SV.line(QX(0), PY(pf), QX(100), PY(pf), "c2", { "stroke-width": 3 }) + SV.text(QX(100), PY(pf) - 8, "Fixed rate $" + (pf / 50).toFixed(2), "lbl bd t2", { "text-anchor": "end" });
  o += SV.circle(QX(qd), PY(pf), 6, "dot2") + SV.circle(QX(qs), PY(pf), 6, "dot2") + SV.text(QX(qd), PY(0) + 18, "Qd " + Math.round(qd), "sm bd", { "text-anchor": "middle" }) + SV.text(QX(qs), PY(0) + 18, "Qs " + Math.round(qs), "sm bd", { "text-anchor": "middle" });
  if (Math.abs(qd - qs) > 1) o += SV.text(380, 32, qs > qd ? "Excess supply " + Math.round(qs - qd) + ": central bank must buy pounds" : "Excess demand " + Math.round(qd - qs) + ": central bank must sell pounds", "lbl bd t2", { "text-anchor": "middle", style: halo });
  return o;
}
Lib.stepper($("#stF"), { w: 760, h: 400, label: "A fixed exchange rate", base: { pf: 60 }, draw: fixChart, steps: [
  { cap: "The government <b>fixes</b> the rate at the equilibrium level, $1.20 per £1. Demand equals supply.", s: { pf: 60 } },
  { cap: "It fixes the rate <b>higher</b>, at $1.50. At that price people want to <b>sell more pounds than are demanded</b>: excess supply.", s: { pf: 75 } },
  { cap: "To keep the rate, the central bank must <b>buy the surplus pounds</b> using its foreign currency reserves, or raise interest rates. Reserves can run out: then the rate is <b>devalued</b>.", s: { pf: 75 } },
  { cap: "If it fixes the rate <b>lower</b> (below equilibrium), there is excess demand and the central bank must <b>sell pounds</b>, building up reserves.", s: { pf: 45 } },
] });
const AP = ["Higher incomes abroad raise demand for the country's exports", "Foreigners need more of the currency to pay for them", "Demand for the currency shifts right", "The exchange rate rises: an appreciation", "Exports become dearer abroad and imports cheaper at home", "Evaluation: effect on trade depends on elasticity; inflation may fall"];
Lib.stepper($("#stA"), { w: 760, h: 400, label: "Causes and effects of an appreciation", base: { n: 0 }, draw: mkChain(AP, "--good"), steps: chainSteps(["<b>Higher incomes abroad</b> raise demand for the country's exports.", "Foreigners need <b>more of the currency</b> to pay for them.", "<b>Demand for the currency</b> shifts right.", "The exchange rate rises: an <b>appreciation</b>.", "Exports become <b>dearer abroad</b> and imports <b>cheaper</b> at home.", "<b>Evaluate:</b> the effect on trade depends on elasticity; inflation may fall."]) });

/* Lab 1: market simulator */
function labM() {
  if (!$("#ma") || !$("#mb") || !$("#mc") || !$("#md")) return;
  const ex = +$("#ma").value, im = +$("#mb").value, ir = +$("#mc").value, sp = +$("#md").value;
  const d = ex + 3 * ir + sp, s = im - 3 * ir - sp, q1 = (100 + d + s) / 2, p1 = 60 + (d - s) / 2, rate = p1 / 50, ch = ((rate - 1.2) / 1.2) * 100;
  $("#ma1").textContent = "$" + rate.toFixed(2); $("#ma2").textContent = (ch >= 0 ? "+" : "−") + money(Math.abs(ch), 1) + "%"; $("#ma3").textContent = ch > 1 ? "Appreciation" : ch < -1 ? "Depreciation" : "Stable";
  $("#mav").textContent = `Demand for the pound shifts by ${money(d, 0)} and supply by ${money(s, 0)}. The equilibrium rate moves from $1.20 to $${rate.toFixed(2)}: ${ch > 1 ? "an appreciation" : ch < -1 ? "a depreciation" : "almost no change"}. Higher exports, higher interest rates and speculation that the pound will rise push the rate up; more imports and expectations of a fall push it down.`;
  $("#labM").innerHTML = fxm({ d, s });
}
Lib.slider($("#g1"), { id: "ma", label: "Change in demand for UK exports", min: -20, max: 20, step: 2, value: 0, fmt: (v) => (v > 0 ? "+" : "") + v, onInput: labM });
Lib.slider($("#g2"), { id: "mb", label: "Change in UK imports (supply of pounds)", min: -20, max: 20, step: 2, value: 0, fmt: (v) => (v > 0 ? "+" : "") + v, onInput: labM });
Lib.slider($("#g3"), { id: "mc", label: "Change in UK interest rate relative to abroad", min: -5, max: 5, step: 1, value: 0, fmt: (v) => (v > 0 ? "+" : "") + v + " pts", onInput: labM });
Lib.slider($("#g4"), { id: "md", label: "Speculation (+ expect rise, − expect fall)", min: -15, max: 15, step: 3, value: 0, fmt: (v) => (v > 0 ? "+" : "") + v, onInput: labM });
const CF = [
  { n: "Rise in exports", d: "Demand ↑", r: "Appreciation", w: "Foreigners buy more pounds to pay for UK goods." },
  { n: "Rise in imports", d: "Supply ↑", r: "Depreciation", w: "UK residents sell more pounds to buy foreign currency." },
  { n: "Higher interest rate", d: "Demand ↑, supply ↓", r: "Appreciation", w: "Hot money flows in for higher returns." },
  { n: "Lower interest rate", d: "Demand ↓, supply ↑", r: "Depreciation", w: "Hot money flows out to higher rates elsewhere." },
  { n: "Speculation: expect a rise", d: "Demand ↑", r: "Appreciation", w: "Speculators buy now to sell later at a profit." },
  { n: "Speculation: expect a fall", d: "Supply ↑", r: "Depreciation", w: "Speculators sell now to avoid loss." },
  { n: "Lower inflation than other countries", d: "Demand ↑", r: "Appreciation", w: "UK exports are more competitive." },
  { n: "Foreign investment into the UK", d: "Demand ↑", r: "Appreciation", w: "Investors buy pounds to invest." },
];
button_table("cfBtns", "cfOut", CF, 0, (p) => `<div class="tw"><table class="t"><tr><th>Shift</th><th>Effect on the pound</th><th>Why</th></tr><tr><td>${p.d}</td><td><b>${p.r}</b></td><td>${p.w}</td></tr></table></div>`);
const FF = [
  { n: "Floating: advantages", t: "Adjusts automatically to trade imbalances; no need for big reserves; central bank can set interest rates for the domestic economy." },
  { n: "Floating: disadvantages", t: "Uncertainty for traders; volatile; speculation; may rise or fall too far; imported inflation after a fall." },
  { n: "Fixed: advantages", t: "Certainty for exporters and investors; less speculation; discipline on inflation; stable trade planning." },
  { n: "Fixed: disadvantages", t: "Needs large reserves; speculative attacks; interest rates tied to defending the rate; the rate may be wrong (overvalued or undervalued); devaluation may be forced." },
];
button_table("ffBtns", "ffOut", FF, 0, (p) => `<div class="tw"><table class="t"><tr><th>${p.n}</th></tr><tr><td>${p.t}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Would each cause the <b>pound</b> to <b>appreciate</b> or <b>depreciate</b> in a floating system?", buckets: [{ label: "Appreciate" }, { label: "Depreciate" }], items: [
  { text: "Foreigners buy more UK exports", b: 0 }, { text: "UK interest rates rise above other countries'", b: 0 }, { text: "Speculators expect the pound to rise", b: 0 }, { text: "More foreign investment in the UK", b: 0 },
  { text: "UK residents buy more imports", b: 1 }, { text: "UK interest rates fall", b: 1 }, { text: "Speculators expect the pound to fall", b: 1 }, { text: "UK firms invest more abroad", b: 1 },
], done: "Demand up or supply down: appreciation. Demand down or supply up: depreciation." });
Lib.classify($("#cl2"), { prompt: "Does each describe a <b>floating</b> or a <b>fixed</b> exchange rate?", buckets: [{ label: "Floating" }, { label: "Fixed" }], items: [
  { text: "Set by demand and supply", b: 0 }, { text: "Changes every day", b: 0 }, { text: "Rise is an appreciation", b: 0 }, { text: "No need for large reserves", b: 0 },
  { text: "Set by the central bank", b: 1 }, { text: "Rarely changes", b: 1 }, { text: "Fall is a devaluation", b: 1 }, { text: "Central bank must buy or sell currency to keep it", b: 1 },
], done: "Know the differences and the terms." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Floating exchange rate", "A rate determined by demand and supply in the foreign exchange market"],
  ["Fixed exchange rate", "A rate set and maintained by the government or central bank"],
  ["Appreciation", "A rise in the value of a floating currency"],
  ["Depreciation", "A fall in the value of a floating currency"],
  ["Devaluation", "A fall in the value of a fixed currency by decision"],
  ["Revaluation", "A rise in the value of a fixed currency by decision"],
], done: "Good vocabulary scores marks." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how a rise in the interest rate causes an appreciation</b>.", items: [
  "The central bank raises the interest rate",
  "Foreign savers can earn more in the country",
  "Hot money flows in: demand for the currency rises",
  "Fewer residents send money abroad: supply falls",
  "The exchange rate appreciates",
], done: "An interest rate chain." });
Lib.calc($("#c1"), { qs: [
  { q: "The exchange rate rises from £1 = $1.20 to £1 = $1.50. By what percentage has the pound appreciated?", a: 25, sol: "0.30 ÷ 1.20 × 100 = <b>25%</b>." },
  { q: "The rate falls from $1.60 to $1.20 per £1. By what percentage has the pound depreciated?", a: 25, sol: "0.40 ÷ 1.60 × 100 = <b>25%</b>." },
  { q: "Demand for a currency is 80 units at the current rate and supply is 100 units. What is the excess supply the central bank must buy to fix the rate?", a: 20, sol: "100 − 80 = <b>20 units</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "In a floating system, an increase in demand for a currency leads to:", opts: ["A depreciation", "An appreciation", "A devaluation", "No change"], a: 1, why: "The price of the currency rises." },
  { q: "Which could cause a depreciation?", opts: ["A rise in exports", "A rise in interest rates", "A rise in imports", "Speculation that it will rise"], a: 2, why: "More supply of the currency." },
  { q: "A fall in the value of a fixed exchange rate is called:", opts: ["Depreciation", "Devaluation", "Revaluation", "Appreciation"], a: 1, why: "Government decision." },
  { q: "A central bank trying to defend a fixed rate that is too high must:", opts: ["Sell its own currency", "Buy its own currency with reserves", "Ignore the market", "Cut interest rates"], a: 1, why: "Use reserves to raise demand." },
  { q: "One advantage of a fixed exchange rate is:", opts: ["It changes every day", "Certainty for traders", "No need for reserves", "No central bank role"], a: 1, why: "Reduces risk." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Floating exchange rate", "A rate determined by the demand for and supply of a currency."],
  ["Fixed exchange rate", "A rate set and maintained by the government or central bank."],
  ["Appreciation", "A rise in the value of a floating currency."],
  ["Depreciation", "A fall in the value of a floating currency."],
  ["Devaluation", "A government lowering the value of a fixed currency."],
  ["Revaluation", "A government raising the value of a fixed currency."],
  ["Equilibrium exchange rate", "The rate at which demand for a currency equals supply."],
  ["Hot money", "Funds that move between countries to earn the highest interest."],
  ["Foreign exchange reserves", "A central bank's holdings of foreign currency used to manage the rate."],
] });
labM(); 
