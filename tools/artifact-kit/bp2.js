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

const DC = ["Incomes and spending at home rise", "Consumers and firms buy more imports", "Meanwhile exports are held back by dear prices or weak demand abroad", "Imports grow faster than exports", "The current account moves towards deficit", "Primary income outflows (profits, interest) can add to it"];
Lib.stepper($("#stD"), { w: 760, h: 400, label: "Causes of a deficit", base: { n: 0 }, draw: mkChain(DC, "--bad"), steps: chainSteps(["<b>Incomes and spending</b> at home rise.", "Consumers and firms <b>buy more imports</b>.", "Meanwhile <b>exports</b> are held back by dear prices or weak demand abroad.", "<b>Imports grow faster</b> than exports.", "The current account moves towards <b>deficit</b>.", "<b>Primary income outflows</b> (profits, interest) can add to it."]) });
const SC = ["Productivity rises and costs fall; quality improves", "Exports become cheaper and more attractive abroad", "Demand for imports falls as home firms compete", "Export revenue rises and import spending falls", "The current account moves towards surplus", "Remittances and overseas investments add further income"];
Lib.stepper($("#stS"), { w: 760, h: 400, label: "Causes of a surplus", base: { n: 0 }, draw: mkChain(SC, "--good"), steps: chainSteps(["<b>Productivity rises</b> and costs fall; quality improves.", "Exports become <b>cheaper and more attractive</b> abroad.", "<b>Demand for imports falls</b> as home firms compete.", "<b>Export revenue rises</b> and import spending falls.", "The current account moves towards <b>surplus</b>.", "<b>Remittances and overseas investments</b> add further income."]) });
function oilChart(s) {
  const pr = [50, 80, 110, 60, 40], ca = [4, 9, 15, 6, 1], X = (i) => 110 + i * 130; let o = SV.line(60, 320, 710, 320) + SV.text(60, 28, "An oil exporter: oil price and the current account", "sm");
  const lab = ["Year 1", "Year 2", "Year 3", "Year 4", "Year 5"];
  pr.forEach((p, i) => { const op = clamp(s.n - i, 0, 1); if (op <= 0) return; const x = X(i) - 50, h = p * 1.6; o += `<g opacity="${op}">` + SV.rect(x, 320 - h, 44, h, "", { style: "fill:var(--warn)", opacity: 0.85 }) + SV.text(x + 22, 320 - h - 6, "$" + p, "sm bd", { "text-anchor": "middle", style: "font-size:11px" }) + SV.rect(x + 50, 320 - ca[i] * 8, 44, ca[i] * 8, "", { style: "fill:var(--accent)", opacity: 0.85 }) + SV.text(x + 72, 320 - ca[i] * 8 - 6, "+" + ca[i] + "%", "sm bd", { "text-anchor": "middle", style: "font-size:11px" }) + SV.text(x + 47, 340, lab[i], "sm", { "text-anchor": "middle" }) + "</g>"; });
  o += SV.rect(480, 40, 14, 14, "", { style: "fill:var(--warn)" }) + SV.text(500, 52, "Oil price ($ a barrel)", "sm") + SV.rect(480, 62, 14, 14, "", { style: "fill:var(--accent)" }) + SV.text(500, 74, "Current account surplus (% of GDP)", "sm");
  return o;
}
Lib.stepper($("#stO"), { w: 760, h: 360, label: "Oil price and an oil exporter's current account", base: { n: 0 }, draw: oilChart, steps: [
  { cap: "An oil exporter earns most of its export revenue from oil. At <b>$50 a barrel</b> the current account has a small surplus (4% of GDP).", s: { n: 1 } },
  { cap: "The oil price rises to <b>$80</b>: export revenue rises, so the <b>surplus widens</b> to 9%.", s: { n: 2 } },
  { cap: "At <b>$110</b> the surplus is 15% of GDP.", s: { n: 3 } },
  { cap: "The price falls back to <b>$60</b> and then <b>$40</b>: export revenue falls and the surplus <b>shrinks</b> to 1%. There is a <b>positive relationship</b> between the oil price and the current account balance of an oil exporter (illustrative figures).", s: { n: 5 } },
] });

/* Lab 1: causes */
function labK() {
  if (!$("#ka") || !$("#kb") || !$("#kc")) return;
  const gy = +$("#ka").value / 100, gw = +$("#kb").value / 100, rp = +$("#kc").value / 100, X = 100 * (1 + 1.5 * gw) * (1 - 0.8 * rp), Mi = 100 * (1 + 1.4 * gy) * (1 + 0.6 * rp), bal = X - Mi;
  $("#ka1").textContent = money(X, 0); $("#ka2").textContent = money(Mi, 0); $("#ka3").textContent = (bal >= 0 ? "+" : "−") + money(Math.abs(bal), 0);
  $("#kav").textContent = `Exports ${money(X, 0)} and imports ${money(Mi, 0)}: balance ${bal >= 0 ? "+" : "−"}${money(Math.abs(bal), 0)} (a ${bal > 0.5 ? "surplus" : bal < -0.5 ? "deficit" : "balance"}). Faster home growth raises imports; stronger world demand raises exports; being less price-competitive than rivals (higher relative prices) cuts exports and raises imports.`;
  const base = 290, k = 1.8; let o = SV.line(60, base, 700, base);
  [["Exports", X, "--good"], ["Imports", Mi, "--bad"]].forEach(([n, v, c], i) => { const x = 160 + i * 250, h = v * k; o += SV.rect(x, base - h, 150, h, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.text(x + 75, base - h - 8, money(v, 0), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 75, base + 22, n, "sm", { "text-anchor": "middle" }); });
  $("#labK").innerHTML = o + SV.text(60, 24, "Baseline: exports 100, imports 100", "sm");
}
Lib.slider($("#g1"), { id: "ka", label: "Growth in home incomes (raises imports)", min: 0, max: 15, step: 1, value: 5, fmt: (v) => v + "%", onInput: labK });
Lib.slider($("#g2"), { id: "kb", label: "Growth in demand abroad (raises exports)", min: -10, max: 15, step: 1, value: 2, fmt: (v) => v + "%", onInput: labK });
Lib.slider($("#g3"), { id: "kc", label: "Domestic prices relative to rivals (higher = less competitive)", min: -10, max: 20, step: 1, value: 0, fmt: (v) => (v > 0 ? "+" : "") + v + "%", onInput: labK });
const CS = [
  { n: "Rising incomes at home", t: "Deficit", e: "Imports rise faster than exports." },
  { n: "Low productivity and high costs", t: "Deficit", e: "Exports uncompetitive; imports more attractive." },
  { n: "High exchange rate", t: "Deficit", e: "Exports dearer abroad, imports cheaper at home." },
  { n: "Recession in trading partners", t: "Deficit", e: "Foreign demand for exports falls." },
  { n: "High export prices (such as oil)", t: "Surplus", e: "Export revenue rises." },
  { n: "Low exchange rate", t: "Surplus", e: "Exports cheap, imports dear." },
  { n: "High saving and low home spending", t: "Surplus", e: "Fewer imports." },
  { n: "Remittances and overseas investment income", t: "Surplus", e: "Large inflows of secondary and primary income." },
];
button_table("csBtns", "csOut", CS, 0, (p) => `<div class="tw"><table class="t"><tr><th>Tends to cause</th><th>How</th></tr><tr><td><b>${p.t}</b></td><td>${p.e}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Does each tend to cause a current account <b>deficit</b> or a <b>surplus</b>?", buckets: [{ label: "Deficit" }, { label: "Surplus" }], items: [
  { text: "Fast rise in consumer spending on imports", b: 0 }, { text: "Costs and prices rising faster than rivals'", b: 0 }, { text: "A very high exchange rate", b: 0 }, { text: "A recession in the main trading partner", b: 0 },
  { text: "Highly competitive, high-quality exports", b: 1 }, { text: "A low exchange rate", b: 1 }, { text: "A rise in the price of the main export", b: 1 }, { text: "Large remittances from workers abroad", b: 1 },
], done: "Think: exports up or imports down gives a surplus." });
Lib.classify($("#cl2"), { prompt: "Which <b>type of cause</b> is each?", buckets: [{ label: "Competitiveness" }, { label: "Demand at home or abroad" }, { label: "Prices of exports or imports" }, { label: "Income flows" }], items: [
  { text: "Higher productivity and lower costs", b: 0 }, { text: "Better quality products", b: 0 },
  { text: "A boom at home raising imports", b: 1 }, { text: "A recession abroad cutting demand for exports", b: 1 },
  { text: "A fall in the world price of the main export", b: 2 }, { text: "A rise in the price of imported oil", b: 2 },
  { text: "Profits sent abroad by foreign firms", b: 3 }, { text: "Remittances from workers overseas", b: 3 },
], done: "Link each cause to exports, imports or income flows." });
Lib.match($("#m1"), { prompt: "Match the cause to its effect.", pairs: [
  ["Higher home incomes", "More imports, so the deficit widens"],
  ["Higher productivity", "More competitive exports"],
  ["Higher oil price (oil exporter)", "More export revenue"],
  ["Recession abroad", "Lower demand for exports"],
  ["High exchange rate", "Exports dearer, imports cheaper"],
  ["Remittances", "Secondary income inflow"],
], done: "Good vocabulary scores marks." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how a high exchange rate could cause a current account deficit</b>.", items: [
  "The exchange rate rises",
  "Exports become dearer for foreign buyers",
  "Imports become cheaper for domestic buyers",
  "Export sales fall and imports rise",
  "The current account moves towards deficit",
], done: "A causal chain." });
Lib.calc($("#c1"), { qs: [
  { q: "Exports are $200bn and imports $220bn. Higher incomes raise imports by 10%, with exports unchanged. What is the new balance ($bn)?", a: -42, sol: "Imports = 242; 200 − 242 = <b>−$42bn</b>." },
  { q: "An oil exporter's oil revenue is $60bn at $60 a barrel. The price rises to $90 with the same quantity. What is the new revenue ($bn)?", a: 90, sol: "60 × 90/60 = <b>$90bn</b>." },
  { q: "Export prices rise 5% while import prices rise 10%. What happens to the terms of trade: by roughly how many percentage points do export prices lag import prices?", a: 5, sol: "10 − 5 = <b>5 percentage points</b>: the deficit may widen." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which is most likely to cause a current account deficit?", opts: ["Higher productivity", "Rising incomes leading to more imports", "A low exchange rate", "Higher export prices"], a: 1, why: "Imports rise." },
  { q: "A rise in the oil price will most likely:", opts: ["Reduce an oil exporter's surplus", "Increase an oil exporter's surplus", "Have no effect", "Reduce its exports"], a: 1, why: "More export revenue." },
  { q: "Higher inflation than competitors tends to:", opts: ["Improve the current account", "Worsen the current account", "Have no effect", "Raise exports"], a: 1, why: "Exports become dearer." },
  { q: "Technology that raises productivity can improve the current account because:", opts: ["Exports become more competitive", "Imports become cheaper", "Exports fall", "Spending rises"], a: 0, why: "Lower costs and better quality." },
  { q: "Which could cause a surplus?", opts: ["A high exchange rate", "A recession abroad", "Remittances from workers abroad", "Higher imports"], a: 2, why: "Income inflows." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Competitiveness", "How attractive a country's goods and services are in terms of price and quality compared with rivals'."],
  ["Terms of trade", "The ratio of export prices to import prices."],
  ["Productivity", "Output per worker."],
  ["Price elasticity of demand", "How responsive quantity demanded is to a price change."],
  ["Overvalued exchange rate", "A rate that is higher than its competitive level, making exports dear."],
  ["Oil exporter", "A country that earns much of its export revenue from oil."],
  ["Import dependence", "Reliance on imports for key goods such as oil and food."],
  ["Hot money", "Funds that move quickly between countries to earn higher returns."],
  ["Net primary income", "Primary income received minus primary income paid."],
] });
labK(); 
