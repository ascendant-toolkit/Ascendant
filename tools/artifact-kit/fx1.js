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

function convChart(s) {
  const r = s.r, base = 320, k = 1.7; let o = SV.line(60, base, 710, base) + SV.text(60, 26, "A €100 good sold to a US buyer", "sm");
  [["Price in euros (€)", 100, "--muted"], ["Price in US dollars ($)", 100 * r, "--accent"]].forEach(([n, v, c], i) => { const x = 150 + i * 250, h = v * k; o += SV.rect(x, base - h, 150, h, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.text(x + 75, base - h - 8, (i ? "$" : "€") + money(v, 0), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 75, base + 22, n, "sm", { "text-anchor": "middle" }); });
  return o + SV.text(380, 56, "€1 = $" + r.toFixed(2), "lbl bd t3", { "text-anchor": "middle", style: "font-size:20px" });
}
Lib.stepper($("#stC"), { w: 760, h: 380, label: "Converting a price", base: { r: 1 }, draw: convChart, steps: [
  { cap: "A good costs <b>€100</b> in Germany. At <b>€1 = $1.00</b> an American pays <b>$100</b>.", s: { r: 1 } },
  { cap: "The euro <b>rises</b> to <b>€1 = $1.25</b>. One euro now buys more dollars, so the same good costs <b>$125</b> for the American buyer.", s: { r: 1.25 } },
  { cap: "The euro <b>falls</b> to <b>€1 = $0.80</b>. The good now costs only <b>$80</b> for Americans, so a falling currency makes <b>exports cheaper</b> for foreign buyers.", s: { r: 0.8 } },
] });
function quoteChart(s) {
  const r = s.r, inv = 1 / r; let o = "";
  const box = (y, t, c) => SV.rect(130, y, 500, 90, "", { rx: 12, style: `fill:var(${c});fill-opacity:0.15;stroke:var(${c});stroke-width:2.5` }) + SV.text(380, y + 56, t, "lbl bd", { "text-anchor": "middle", style: "font-size:28px" });
  o += SV.text(380, 40, "The same rate, two ways", "sm", { "text-anchor": "middle" }) + box(60, "£1 = $" + r.toFixed(2), "--accent") + SV.line(380, 154, 380, 186, "ax", { style: "stroke-width:2.5" }) + SV.arrowHead(380, 190, "d", "dot1") + SV.text(400, 176, "invert (1 ÷ rate)", "sm") + box(200, "$1 = £" + inv.toFixed(2), "--warn");
  if (s.t) o += SV.text(380, 340, s.t, "lbl bd t3", { "text-anchor": "middle", style: "font-size:15px" });
  return o;
}
Lib.stepper($("#stQ"), { w: 760, h: 370, label: "Two ways of quoting a rate", base: { r: 1.5, t: "" }, draw: quoteChart, steps: [
  { cap: "The rate <b>£1 = $1.50</b> says what one pound buys.", s: { r: 1.5, t: "" } },
  { cap: "Turn it round: <b>$1 = £0.67</b> (1 ÷ 1.50). It is the same rate, from the dollar's side.", s: { r: 1.5, t: "Same rate, different view" } },
  { cap: "Now £1 = <b>$1.20</b>. The pound buys fewer dollars: the <b>pound has fallen</b>.", s: { r: 1.2, t: "The pound has fallen" } },
  { cap: "Turn it round: $1 = <b>£0.83</b>. More pounds are needed for a dollar: the <b>dollar has risen</b> against the pound.", s: { r: 1.2, t: "The dollar has risen against the pound" } },
] });

/* Lab 1: converter */
function labV() {
  if (!$("#va") || !$("#vb")) return;
  const r = +$("#va").value, p = +$("#vb").value;
  $("#va1").textContent = "$" + money(p * r, 2); $("#va2").textContent = "£" + money(p / r, 2); $("#va3").textContent = "$1 = £" + money(1 / r, 2);
  $("#vav").textContent = `At £1 = $${r.toFixed(2)}: a £${p} British good costs $${money(p * r, 2)} for a US buyer (£ × ${r.toFixed(2)}). A $${p} US good costs £${money(p / r, 2)} for a British buyer ($ ÷ ${r.toFixed(2)}). A higher £ rate makes UK exports dearer in dollars and US goods cheaper in pounds.`;
  const base = 290, k = 1.5; let o = SV.line(60, base, 700, base);
  [["£" + p + " UK good, in $", p * r, "--accent"], ["$" + p + " US good, in £", p / r, "--warn"]].forEach(([n, v, c], i) => { const x = 150 + i * 260, h = v * k; o += SV.rect(x, base - h, 150, h, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.text(x + 75, base - h - 8, (i ? "£" : "$") + money(v, 1), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 75, base + 22, n, "sm", { "text-anchor": "middle" }); });
  $("#labV").innerHTML = o;
}
Lib.slider($("#g1"), { id: "va", label: "Exchange rate ($ per £1)", min: 1, max: 2, step: 0.05, value: 1.5, fmt: (v) => "$" + v.toFixed(2), onInput: labV });
Lib.slider($("#g2"), { id: "vb", label: "Price of the good (in its home currency)", min: 50, max: 200, step: 10, value: 100, fmt: (v) => v, onInput: labV });
const DR = [
  { n: "£1 = $1.50 → £1 = $1.80", a: "The pound rose", w: "One pound buys more dollars. The dollar fell." },
  { n: "£1 = $1.50 → £1 = $1.20", a: "The pound fell", w: "One pound buys fewer dollars. The dollar rose." },
  { n: "$1 = 15,000 dong → $1 = 23,000 dong", a: "The dong fell", w: "More dong are needed to buy a dollar." },
  { n: "€1 = $1.10 → €1 = $1.05", a: "The euro fell", w: "One euro buys fewer dollars." },
  { n: "$1 = ¥110 → $1 = ¥100", a: "The dollar fell (yen rose)", w: "A dollar buys fewer yen." },
];
button_table("drBtns", "drOut", DR, 0, (p) => `<div class="tw"><table class="t"><tr><th>What happened</th><th>Why</th></tr><tr><td><b>${p.a}</b></td><td>${p.w}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Did the <b>first-named currency</b> rise or fall?", buckets: [{ label: "Rose" }, { label: "Fell" }], items: [
  { text: "£1 = $1.50 changes to £1 = $1.70", b: 0 }, { text: "€1 = $1.10 changes to €1 = $1.25", b: 0 }, { text: "$1 = 100 rupees changes to $1 = 80 rupees (the rupee)", b: 0 },
  { text: "£1 = $1.50 changes to £1 = $1.30", b: 1 }, { text: "€1 = $1.10 changes to €1 = $0.95", b: 1 }, { text: "$1 = 100 rupees changes to $1 = 120 rupees (the rupee)", b: 1 },
], done: "A currency rises when one unit buys more of another." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Foreign exchange rate", "The price of one currency in terms of another"],
  ["Currency", "The money used in a country"],
  ["Exchange rate quote", "A statement such as £1 = $1.50"],
  ["Rise in a currency", "One unit buys more of another currency"],
  ["Fall in a currency", "One unit buys less of another currency"],
  ["Foreign currency", "Money of another country"],
], done: "Good vocabulary scores marks." });
Lib.calc($("#c1"), { qs: [
  { q: "£1 = $1.50. A UK good costs £200. What does a US buyer pay in dollars?", a: 300, sol: "200 × 1.50 = <b>$300</b>." },
  { q: "£1 = $1.50. A US good costs $240. What does a UK buyer pay in pounds?", a: 160, sol: "240 ÷ 1.50 = <b>£160</b>." },
  { q: "€1 = $1.25. A car costs €20,000. What is the price in dollars?", a: 25000, sol: "20,000 × 1.25 = <b>$25,000</b>." },
  { q: "£1 = $1.50 falls to £1 = $1.20. By what percentage does the pound fall against the dollar?", a: 20, sol: "0.30 ÷ 1.50 × 100 = <b>20%</b>." },
  { q: "£1 = $1.25. What is $1 in pounds (2 d.p.)?", a: 0.8, tol: 0.01, sol: "1 ÷ 1.25 = <b>£0.80</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What is a foreign exchange rate?", opts: ["The price of one good in terms of another", "The price of one currency in terms of another", "The rate of interest abroad", "The cost of importing"], a: 1, why: "Currency for currency." },
  { q: "£1 = $1.50 changes to £1 = $1.30. The pound has:", opts: ["Risen", "Fallen", "Not changed", "Doubled"], a: 1, why: "One pound buys fewer dollars." },
  { q: "If £1 = $2, how many pounds do you get for $10?", opts: ["£20", "£5", "£2", "£0.5"], a: 1, why: "10 ÷ 2." },
  { q: "If the euro rises against the dollar, European exports to the US:", opts: ["Become cheaper", "Become dearer in dollars", "Do not change", "Double"], a: 1, why: "Dollar price rises." },
  { q: "$1 = 10 pesos changes to $1 = 12 pesos. The peso has:", opts: ["Risen", "Fallen", "Not changed", "Doubled"], a: 1, why: "More pesos for a dollar." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Foreign exchange rate", "The price (value) of one currency in terms of another currency."],
  ["Currency", "The money used in a country."],
  ["Exchange rate quote", "A statement of how much of one currency one unit of another buys, such as £1 = $1.50."],
  ["Appreciation", "A rise in the value of a currency in a floating system."],
  ["Depreciation", "A fall in the value of a currency in a floating system."],
  ["Foreign currency", "The money of another country."],
  ["Strong currency", "A currency with a high value against others."],
  ["Weak currency", "A currency with a low value against others."],
] });
labV(); 
