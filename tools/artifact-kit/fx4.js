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

function priceChart(s) {
  const r = s.r, base = 320, k = 0.3; let o = SV.line(60, base, 710, base) + SV.text(380, 40, "£1 = $" + r.toFixed(2), "lbl bd " + (r < 1.45 ? "t2" : r > 1.55 ? "t4" : "t1"), { "text-anchor": "middle", style: "font-size:20px" });
  const xp = 1000 * r, mp = 600 / r;
  [["UK car price in US dollars", xp, "--good", "$"], ["US machine price in pounds", mp, "--warn", "£"]].forEach(([n, v, c, pre], i) => { const x = 140 + i * 280, h = v * k; o += SV.rect(x, base - h, 150, h, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.rect(x, base - (i ? 400 : 1500) * k, 150, (i ? 400 : 1500) * k, "", { style: "fill:none;stroke:var(--muted);stroke-width:2;stroke-dasharray:6 4" }) + SV.text(x + 75, base - Math.max(v, i ? 400 : 1500) * k - 8, pre + money(v, 0), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 75, base + 22, n, "sm", { "text-anchor": "middle" }); });
  return o + SV.text(60, 66, "Dashed outline: prices at £1 = $1.50 (a £1,000 car and a $600 machine)", "sm");
}
Lib.stepper($("#stP"), { w: 760, h: 380, label: "Exchange rate changes and prices", base: { r: 1.5 }, draw: priceChart, steps: [
  { cap: "At <b>£1 = $1.50</b> a UK car priced at £1,000 costs a US buyer <b>$1,500</b>. A US machine priced at $600 costs a UK buyer <b>£400</b>.", s: { r: 1.5 } },
  { cap: "The pound <b>falls</b> to <b>£1 = $1.20</b>. The UK car now costs <b>$1,200</b> in the US: <b>cheaper</b>, so exports may rise. The US machine now costs <b>£500</b> in the UK: <b>dearer</b>, so imports may fall.", s: { r: 1.2 } },
  { cap: "The pound <b>rises</b> to <b>£1 = $1.80</b>. The UK car costs <b>$1,800</b>: <b>dearer</b>, so exports may fall. The US machine costs <b>£333</b>: <b>cheaper</b>, so imports may rise.", s: { r: 1.8 } },
] });
const DP = ["The currency falls (depreciation)", "Exports become cheaper in foreign currency", "Imports become dearer in the home currency", "Export demand rises; import demand falls (if elastic)", "Net exports rise: AD shifts right", "Output and jobs rise; the current account may improve"];
Lib.stepper($("#stD"), { w: 760, h: 400, label: "A fall in the exchange rate and the economy", base: { n: 0 }, draw: mkChain(DP, "--good"), steps: chainSteps(["The currency <b>falls</b> (depreciation).", "Exports become <b>cheaper</b> in foreign currency.", "Imports become <b>dearer</b> in the home currency.", "<b>Export demand rises and import demand falls</b> (if demand is elastic).", "<b>Net exports rise</b>: AD shifts right.", "<b>Output and jobs rise</b>; the current account may improve. <b>Evaluate:</b> imported inflation and elasticity."]) });
const AC = ["The currency rises (appreciation)", "Imported raw materials, fuel and goods become cheaper", "Firms' costs fall and import prices fall", "Inflation is lower", "But exports are dearer abroad and sales fall", "Exporters lose jobs; the current account may worsen"];
Lib.stepper($("#stA"), { w: 760, h: 400, label: "A rise in the exchange rate and the economy", base: { n: 0 }, draw: mkChain(AC, "--warn"), steps: chainSteps(["The currency <b>rises</b> (appreciation).", "Imported raw materials, fuel and goods become <b>cheaper</b>.", "<b>Firms' costs fall</b> and import prices fall.", "<b>Inflation is lower</b>.", "But <b>exports are dearer</b> abroad and sales fall.", "<b>Exporters lose jobs</b>; the current account may worsen."]) });

/* Lab 1: effect simulator */
function labE() {
  if (!$("#ea") || !$("#eb")) return;
  const r = +$("#ea").value, e = +$("#eb").value, r0 = 1.5, xp = 1000 * r, mp = 600 / r, xv = 100 * Math.pow(r / r0, -e), mv = 100 * Math.pow(r / r0, e), exp = (1000 * xv) / 1000, imp = (mp * mv) / 1000, net = exp - imp, bal0 = (1000 * 100 - 400 * 100) / 1000;
  $("#ea1").textContent = "$" + money(xp, 0); $("#ea2").textContent = "£" + money(mp, 0); $("#ea3").textContent = (net - bal0 >= 0 ? "+" : "−") + money(Math.abs(net - bal0), 1);
  $("#eav").textContent = r < 1.45 ? `The pound has fallen to $${r.toFixed(2)}. UK cars cost $${money(xp, 0)} (cheaper abroad, ${money(xv, 0)} sold) and US machines cost £${money(mp, 0)} (dearer, ${money(mv, 0)} bought). ${net > bal0 ? "Net exports improve because demand is elastic enough." : "With inelastic demand, the dearer imports outweigh the extra exports: net exports get worse in the short run."}` : r > 1.55 ? `The pound has risen to $${r.toFixed(2)}. UK cars cost $${money(xp, 0)} (dearer, ${money(xv, 0)} sold) and US machines cost £${money(mp, 0)} (cheaper, ${money(mv, 0)} bought). ${net < bal0 ? "Net exports worsen: exporters lose out, but imports are cheaper and help against inflation." : "Because demand is inelastic, net exports still improve in this model."}` : "No change from £1 = $1.50.";
  const base = 290; let o = SV.line(60, base, 700, base);
  [["Car price in $", xp, "--good", 0.18], ["Machine price in £", mp, "--warn", 0.5], ["Cars sold", xv, "--accent", 1.5], ["Machines bought", mv, "--n", 1.5]].forEach(([n, v, c, k], i) => { const x = 90 + i * 150, h = v * k; o += SV.rect(x, base - h, 100, h, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.text(x + 50, base - h - 8, money(v, 0), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 50, base + 20, n, "sm", { "text-anchor": "middle", style: "font-size:11px" }); });
  $("#labE").innerHTML = o;
}
Lib.slider($("#g1"), { id: "ea", label: "Exchange rate ($ per £1), starting at 1.50", min: 1, max: 2, step: 0.05, value: 1.2, fmt: (v) => "$" + v.toFixed(2), onInput: labE });
Lib.slider($("#g2"), { id: "eb", label: "Price elasticity of demand for exports and imports", min: 0.2, max: 2, step: 0.2, value: 1.4, fmt: (v) => v.toFixed(1) + (v < 1 ? " inelastic" : v > 1 ? " elastic" : ""), onInput: labE });
const WG = [
  { n: "Exporters", f: "Gain: cheaper abroad, more sales.", r: "Lose: dearer abroad, fewer sales and jobs." },
  { n: "Importers and firms using imported inputs", f: "Lose: higher costs.", r: "Gain: lower costs." },
  { n: "Consumers", f: "Lose: imports and foreign holidays cost more.", r: "Gain: cheaper imports and holidays." },
  { n: "Foreign tourists", f: "Gain: the country is cheaper.", r: "Lose: the country is dearer." },
  { n: "Borrowers with debts in foreign currency", f: "Lose: debts cost more.", r: "Gain: debts cost less." },
  { n: "The government", f: "More growth and tax revenue; but inflation.", r: "Lower inflation; but slower growth." },
];
button_table("wgBtns", "wgOut", WG, 0, (p) => `<div class="tw"><table class="t"><tr><th>If the currency falls</th><th>If the currency rises</th></tr><tr><td>${p.f}</td><td>${p.r}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each a likely effect of a <b>fall</b> or a <b>rise</b> in the exchange rate?", buckets: [{ label: "Fall in the exchange rate" }, { label: "Rise in the exchange rate" }], items: [
  { text: "Exports become cheaper for foreigners", b: 0 }, { text: "Imported raw materials cost more", b: 0 }, { text: "Exporters could take on more workers", b: 0 }, { text: "Cost-push inflation risk", b: 0 },
  { text: "Foreign holidays become cheaper", b: 1 }, { text: "Imports are cheaper, helping to reduce inflation", b: 1 }, { text: "Exporters may lose sales and jobs", b: 1 }, { text: "Domestic firms face more competition from imports", b: 1 },
], done: "Fall: exports cheaper, imports dearer. Rise: the reverse." });
Lib.classify($("#cl2"), { prompt: "Who <b>gains</b> and who <b>loses</b> when a country's currency <b>falls</b>?", buckets: [{ label: "Gains" }, { label: "Loses" }], items: [
  { text: "Exporters", b: 0 }, { text: "Foreign tourists visiting", b: 0 }, { text: "Domestic firms competing with imports", b: 0 },
  { text: "Consumers buying imports", b: 1 }, { text: "Firms using imported raw materials", b: 1 }, { text: "People holidaying abroad", b: 1 }, { text: "Borrowers with foreign-currency debts", b: 1 },
], done: "Winners and losers." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Imported inflation", "A rise in prices caused by dearer imports after a fall in the exchange rate"],
  ["Price competitiveness", "How cheap a country's goods are in foreign markets"],
  ["Net exports", "Exports minus imports"],
  ["Elasticity of demand", "The responsiveness of quantity demanded to a price change"],
  ["Current account", "Part of the balance of payments for trade, income and transfers"],
  ["Exchange rate effect", "The change in prices and trade caused by a change in the rate"],
], done: "Good vocabulary scores marks." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how a fall in the exchange rate could reduce a current account deficit</b>.", items: [
  "The exchange rate falls",
  "Exports become cheaper in foreign currency; imports become dearer",
  "Demand for exports rises and demand for imports falls",
  "Export revenue rises and import spending falls",
  "The current account deficit narrows",
], done: "A chain for a 6-mark answer." });
Lib.calc($("#c1"), { qs: [
  { q: "£1 = $1.50 falls to £1 = $1.20. A UK good costs £500. What is the dollar price before and after (answer: fall in dollar price, $)?", a: 150, sol: "Before: 500 × 1.50 = $750. After: 500 × 1.20 = $600. Fall = <b>$150</b>." },
  { q: "£1 = $1.50 falls to £1 = $1.20. A US good costs $300. By how much does its price in pounds rise (£)?", a: 50, sol: "Before: 300 ÷ 1.50 = £200. After: 300 ÷ 1.20 = £250. Rise = <b>£50</b>." },
  { q: "Exports rise from 100 to 120 units after a currency fall. What is the percentage increase?", a: 20, sol: "20 ÷ 100 × 100 = <b>20%</b>." },
  { q: "Import prices rise by 10% and imports make up 30% of consumer spending. By roughly how much do consumer prices rise (%)?", a: 3, sol: "30% × 10% = <b>3%</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A fall in the exchange rate is likely to:", opts: ["Make exports dearer for foreigners", "Make exports cheaper for foreigners", "Make imports cheaper", "Reduce inflation"], a: 1, why: "Foreign currency price of exports falls." },
  { q: "A rise in the exchange rate is most likely to:", opts: ["Raise imported inflation", "Help to reduce inflation", "Make exports cheaper", "Increase export demand"], a: 1, why: "Imports are cheaper." },
  { q: "A fall in the exchange rate may fail to improve the current account if demand for exports and imports is:", opts: ["Elastic", "Inelastic", "Unit elastic", "Rising"], a: 1, why: "Quantities barely change." },
  { q: "Who gains from a fall in the value of the pound?", opts: ["UK importers", "UK exporters", "UK tourists abroad", "People with dollar debts"], a: 1, why: "Exports become more competitive." },
  { q: "Which is a possible cost of a fall in the exchange rate?", opts: ["Cheaper exports", "Imported inflation", "More jobs", "Better current account"], a: 1, why: "Dearer imports raise costs." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Imported inflation", "A rise in prices caused by dearer imports, often after a fall in the exchange rate."],
  ["Price competitiveness", "How cheap a country's goods are compared with rivals' goods."],
  ["Net exports", "The value of exports minus imports."],
  ["Elastic demand", "Quantity demanded changes by a larger percentage than the price change."],
  ["Inelastic demand", "Quantity demanded changes by a smaller percentage than the price change."],
  ["Current account", "The part of the balance of payments for trade in goods and services and income flows."],
  ["Cost-push inflation", "A rise in the price level caused by higher costs of production."],
  ["Exchange rate effect", "The effect of a change in the exchange rate on prices and trade."],
  ["Tourism", "Spending by visitors, affected by the exchange rate."],
] });
labE(); 
