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

function wfChart(s) {
  const items = s.items, base0 = 190, k = s.k || 3.2; let o = SV.line(40, base0, 720, base0) + SV.text(40, 26, "$bn", "sm");
  let cum = 0; const w = 100, gap = 30;
  items.forEach(([n, v, c], i) => {
    const op = clamp(s.n - i, 0, 1); const x = 60 + i * (w + gap);
    if (op > 0) { const y0 = base0 - cum * k, y1 = base0 - (cum + v) * k, top = Math.min(y0, y1), h = Math.abs(y1 - y0); o += `<g opacity="${op}">` + SV.rect(x, top, w, Math.max(h, 2), "", { style: `fill:var(${v >= 0 ? "--good" : "--bad"})`, opacity: 0.85 }) + SV.text(x + w / 2, v >= 0 ? top - 8 : top + h + 16, (v >= 0 ? "+" : "−") + Math.abs(v), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + w / 2, 330, n, "sm bd", { "text-anchor": "middle", style: "font-size:11px" }) + "</g>"; }
    cum += v;
  });
  const tot = items.reduce((a, b) => a + b[1], 0), x = 60 + items.length * (w + gap), op = clamp(s.n - items.length, 0, 1);
  if (op > 0) { const y1 = base0 - tot * k, top = Math.min(base0, y1), h = Math.abs(y1 - base0); o += `<g opacity="${op}">` + SV.rect(x, top, w, Math.max(h, 2), "", { style: `fill:var(${tot >= 0 ? "--accent" : "--warn"})`, opacity: 0.9 }) + SV.text(x + w / 2, tot >= 0 ? top - 8 : top + h + 16, (tot >= 0 ? "+" : "−") + Math.abs(tot), "lbl bd t3", { "text-anchor": "middle", style: "font-size:16px" }) + SV.text(x + w / 2, 330, "Current account", "sm bd", { "text-anchor": "middle", style: "font-size:11px" }) + SV.text(x + w / 2, 346, tot >= 0 ? "SURPLUS" : "DEFICIT", "lbl bd " + (tot >= 0 ? "t3" : "t2"), { "text-anchor": "middle", style: "font-size:13px" }) + "</g>"; }
  return o;
}

const ITEMS = [["Goods", -30, ""], ["Services", 25, ""], ["Primary income", -8, ""], ["Secondary income", 3, ""]];
Lib.stepper($("#stW"), { w: 760, h: 360, label: "Building the current account", base: { items: ITEMS, n: 0, k: 3.2 }, draw: wfChart, steps: [
  { cap: "<b>Trade in goods:</b> the country exports $200bn and imports $230bn of goods: a <b>deficit of $30bn</b>.", s: { items: ITEMS, n: 1, k: 3.2 } },
  { cap: "<b>Trade in services:</b> exports of $90bn and imports of $65bn: a <b>surplus of $25bn</b>, which offsets most of the goods deficit.", s: { items: ITEMS, n: 2, k: 3.2 } },
  { cap: "<b>Primary income:</b> $20bn comes in from investments and work abroad but $28bn goes out as profits and interest to foreigners: a <b>deficit of $8bn</b>.", s: { items: ITEMS, n: 3, k: 3.2 } },
  { cap: "<b>Secondary income:</b> transfers such as remittances and aid net +$3bn.", s: { items: ITEMS, n: 4, k: 3.2 } },
  { cap: "<b>Current account balance</b> = −30 + 25 − 8 + 3 = <b>−$10bn</b>: a <b>deficit</b>. It has to be financed by borrowing or selling assets.", s: { items: ITEMS, n: 5, k: 3.2 } },
] });
function trChart(s) {
  const base = 300, k = 1.1; let o = SV.line(60, base, 710, base) + SV.text(60, 26, "Value of goods and services traded ($bn)", "sm");
  [["Goods exports", 200, "--good"], ["Goods imports", 230, "--bad"], ["Services exports", 90, "--good"], ["Services imports", 65, "--bad"]].forEach(([n, v, c], i) => { const op = clamp(s.n - i * 0.5, 0, 1); if (op <= 0) return; const x = 90 + i * 150, h = v * k; o += `<g opacity="${op}">` + SV.rect(x, base - h, 110, h, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.text(x + 55, base - h - 8, v, "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 55, base + 20, n, "sm", { "text-anchor": "middle", style: "font-size:12px" }) + "</g>"; });
  if (s.n >= 2) o += SV.text(370, 70, "Goods: " + (200 - 230) + "  ·  Services: +" + (90 - 65), "lbl bd t3", { "text-anchor": "middle", style: "font-size:17px" });
  return o;
}
Lib.stepper($("#stT"), { w: 760, h: 350, label: "Goods and services", base: { n: 0 }, draw: trChart, steps: [
  { cap: "<b>Goods</b> are physical items. Exports of $200bn are less than imports of $230bn.", s: { n: 1 } },
  { cap: "<b>Services</b> are things like tourism and banking. Exports of $90bn exceed imports of $65bn.", s: { n: 4 } },
  { cap: "A country can run a <b>deficit in goods</b> and a <b>surplus in services</b> at the same time. Always calculate each balance separately.", s: { n: 4 } },
] });

/* Lab 1 */
function labC() {
  const ids = ["xa", "xb", "xc", "xd", "xe", "xf", "xg", "xh"]; if (!ids.every((i) => $("#" + i))) return;
  const v = ids.map((i) => +$("#" + i).value), gb = v[0] - v[1], sb = v[2] - v[3], pb = v[4] - v[5], sc = v[6] - v[7], ca = gb + sb + pb + sc;
  $("#xa1").textContent = (gb >= 0 ? "+" : "−") + Math.abs(gb); $("#xa2").textContent = (sb >= 0 ? "+" : "−") + Math.abs(sb); $("#xa3").textContent = (pb + sc >= 0 ? "+" : "−") + Math.abs(pb + sc); $("#xa4").textContent = (ca >= 0 ? "+" : "−") + Math.abs(ca);
  $("#xav").textContent = `Goods ${gb >= 0 ? "+" : "−"}${Math.abs(gb)}, services ${sb >= 0 ? "+" : "−"}${Math.abs(sb)}, primary income ${pb >= 0 ? "+" : "−"}${Math.abs(pb)}, secondary income ${sc >= 0 ? "+" : "−"}${Math.abs(sc)}. Current account = ${ca >= 0 ? "+" : "−"}${Math.abs(ca)}: a ${ca > 0 ? "surplus" : ca < 0 ? "deficit" : "balance"}. ${gb < 0 && sb > 0 ? "A goods deficit may be partly offset by a services surplus." : ""}`;
  $("#labC").innerHTML = wfChart({ items: [["Goods", gb, ""], ["Services", sb, ""], ["Primary income", pb, ""], ["Secondary income", sc, ""]], n: 5, k: 2 });
}
[["xa", "g1", "Exports of goods", 200], ["xb", "g2", "Imports of goods", 230], ["xc", "g3", "Exports of services", 90], ["xd", "g4", "Imports of services", 65], ["xe", "g5", "Primary income received", 20], ["xf", "g6", "Primary income paid", 28], ["xg", "g7", "Secondary income received", 12], ["xh", "g8", "Secondary income paid", 9]].forEach(([id, g, l, v]) => Lib.slider($("#" + g), { id, label: l, min: 0, max: 300, step: 5, value: v, fmt: (x) => "$" + x, onInput: labC }));
const TX = [
  { n: "A country exports cars", a: "Trade in goods", w: "Physical product sold abroad." },
  { n: "Foreign tourists stay in its hotels", a: "Trade in services (export)", w: "Tourism is a service sold to foreigners." },
  { n: "A firm pays interest on a loan from a foreign bank", a: "Primary income (payment)", w: "Interest paid to foreign owners of capital." },
  { n: "A foreign company sends profits home", a: "Primary income (payment)", w: "Profits flow out to foreign owners." },
  { n: "Migrant workers send money to families at home", a: "Secondary income (receipt)", w: "A transfer with nothing exchanged." },
  { n: "The government gives aid to another country", a: "Secondary income (payment)", w: "Transfers with no good or service in return." },
  { n: "A UK bank sells insurance to a foreign firm", a: "Trade in services (export)", w: "Financial services sold abroad." },
  { n: "A shop imports clothing", a: "Trade in goods (import)", w: "Physical goods bought from abroad." },
];
button_table("txBtns", "txOut", TX, 0, (p) => `<div class="tw"><table class="t"><tr><th>Component</th><th>Why</th></tr><tr><td><b>${p.a}</b></td><td>${p.w}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Which <b>component of the current account</b> is each?", buckets: [{ label: "Trade in goods" }, { label: "Trade in services" }, { label: "Primary income" }, { label: "Secondary income" }], items: [
  { text: "Exports of steel", b: 0 }, { text: "Imports of smartphones", b: 0 },
  { text: "Tourism spending by visitors", b: 1 }, { text: "Insurance sold to foreign firms", b: 1 },
  { text: "Dividends paid to foreign shareholders", b: 2 }, { text: "Interest received from loans abroad", b: 2 },
  { text: "Workers' remittances", b: 3 }, { text: "Foreign aid", b: 3 },
], done: "Four components: goods, services, primary income, secondary income." });
Lib.classify($("#cl2"), { prompt: "Is each a <b>receipt (money in)</b> or a <b>payment (money out)</b> for the UK current account?", buckets: [{ label: "Receipt (in)" }, { label: "Payment (out)" }], items: [
  { text: "A US firm buys British cars", b: 0 }, { text: "French tourists spend in London", b: 0 }, { text: "A UK firm's profits from its Indian factory", b: 0 }, { text: "A UK worker in Dubai sends money home", b: 0 },
  { text: "A UK shop buys Chinese clothing", b: 1 }, { text: "British tourists spend in Spain", b: 1 }, { text: "Profits sent by a foreign-owned UK firm to its parent abroad", b: 1 }, { text: "UK foreign aid", b: 1 },
], done: "Receipts add to the balance; payments subtract." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Current account", "Record of trade in goods and services, primary income and secondary income"],
  ["Trade in goods balance", "Exports of goods minus imports of goods"],
  ["Primary income", "Wages, profits, interest and dividends earned from and paid abroad"],
  ["Secondary income", "Transfers such as remittances and aid"],
  ["Current account deficit", "Payments to the rest of the world exceed receipts"],
  ["Current account surplus", "Receipts from the rest of the world exceed payments"],
], done: "Good vocabulary scores marks." });
Lib.calc($("#c1"), { qs: [
  { q: "Exports of goods are $120bn and imports of goods are $150bn. What is the trade in goods balance ($bn)?", a: -30, sol: "120 − 150 = <b>−$30bn</b>: a deficit." },
  { q: "Goods balance −$30bn, services balance +$22bn, primary income −$6bn, secondary income +$4bn. What is the current account balance ($bn)?", a: -10, sol: "−30 + 22 − 6 + 4 = <b>−$10bn</b>." },
  { q: "A country earns $15bn of primary income from abroad and pays $20bn abroad. What is the primary income balance ($bn)?", a: -5, sol: "15 − 20 = <b>−$5bn</b>." },
  { q: "Exports of goods and services are $300bn and imports are $280bn. Primary and secondary income net to −$12bn. What is the current account balance ($bn)?", a: 8, sol: "(300 − 280) − 12 = <b>+$8bn</b>: a surplus." },
  { q: "A current account deficit is $12bn and GDP is $400bn. What is the deficit as a percentage of GDP?", a: 3, sol: "12 ÷ 400 × 100 = <b>3%</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which is a component of the current account?", opts: ["Government spending", "Trade in goods", "Inflation", "Unemployment"], a: 1, why: "Goods, services, primary income, secondary income." },
  { q: "Workers' remittances are part of:", opts: ["Trade in goods", "Trade in services", "Primary income", "Secondary income"], a: 3, why: "Transfers with no good in return." },
  { q: "A trade in goods deficit means:", opts: ["Exports exceed imports of goods", "Imports of goods exceed exports of goods", "Services imports exceed exports", "No trade"], a: 1, why: "Expenditure on goods imports is greater than revenue from exports." },
  { q: "Profits sent abroad by foreign-owned firms are part of:", opts: ["Trade in goods", "Secondary income", "Primary income", "Trade in services"], a: 2, why: "Income paid to foreign owners." },
  { q: "The current account balance is:", opts: ["Goods + services only", "Goods + services + primary income + secondary income", "Exports + imports", "Government revenue − spending"], a: 1, why: "All four components." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Current account", "The part of the balance of payments that records trade in goods and services, primary income and secondary income."],
  ["Trade in goods", "Exports and imports of physical goods (visible trade)."],
  ["Trade in services", "Exports and imports of services such as tourism and banking (invisible trade)."],
  ["Primary income", "Wages, profits, interest and dividends earned from and paid abroad."],
  ["Secondary income", "Transfers with nothing received in return, such as remittances and aid."],
  ["Current account deficit", "When payments to the rest of the world exceed receipts."],
  ["Current account surplus", "When receipts from the rest of the world exceed payments."],
  ["Balance of payments", "A record of all payments between a country and the rest of the world."],
  ["Visible trade", "Trade in goods."],
] });
labC(); 
