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

const DE = ["A US importer wants to buy British cars", "It must pay in pounds, so it sells dollars and buys pounds", "Demand for pounds rises", "The same happens with foreign tourists, investors and speculators", "More buyers want pounds than before", "The pound's value tends to rise"];
Lib.stepper($("#stD"), { w: 760, h: 400, label: "Why foreigners demand a currency", base: { n: 0 }, draw: mkChain(DE, "--good"), steps: chainSteps(["A <b>US importer</b> wants to buy British cars.", "It must pay in pounds, so it <b>sells dollars and buys pounds</b>.", "The <b>demand for pounds</b> rises.", "The same applies to <b>foreign tourists, investors</b> and <b>speculators</b>.", "More buyers want pounds than before.", "The pound's <b>value tends to rise</b>."]) });
const SU = ["A British family books a holiday in Spain", "They must pay in euros, so they sell pounds and buy euros", "Supply of pounds rises", "The same happens when UK firms import goods or invest abroad", "More pounds are offered for sale", "The pound's value tends to fall"];
Lib.stepper($("#stS"), { w: 760, h: 400, label: "Why residents supply a currency", base: { n: 0 }, draw: mkChain(SU, "--bad"), steps: chainSteps(["A <b>British family</b> books a holiday in Spain.", "They must pay in euros, so they <b>sell pounds and buy euros</b>.", "The <b>supply of pounds</b> rises.", "The same applies to <b>UK firms importing</b> or <b>investing abroad</b>.", "More pounds are offered for sale.", "The pound's <b>value tends to fall</b>."]) });
const SP = ["Speculators expect the lira to fall in value", "They sell lira now to buy it back cheaper later", "The supply of lira on the market rises", "Others follow and the lira falls", "The expectation becomes self-fulfilling", "The central bank may intervene to buy lira"];
Lib.stepper($("#stP"), { w: 760, h: 400, label: "Speculation", base: { n: 0 }, draw: mkChain(SP, "--warn"), steps: chainSteps(["Speculators <b>expect the lira to fall</b> in value.", "They <b>sell lira now</b> to buy it back cheaper later.", "The <b>supply of lira</b> on the market rises.", "<b>Others follow</b> and the lira falls.", "The expectation becomes <b>self-fulfilling</b>.", "The central bank may <b>intervene</b> to buy lira with its reserves."]) });

/* Lab 1: flows */
const FL = [["Exports bought by foreigners", 60], ["Foreign investment in the country", 20], ["Profits, interest and dividends sent in", 10], ["Remittances sent in", 5], ["Foreign tourists' spending", 15]], FO = [["Imports bought by residents", 70], ["Investment abroad by residents", 15], ["Profits, interest and dividends sent out", 12], ["Remittances sent out", 3], ["Residents' spending abroad on tourism", 18]];
function labF() {
  const ids = ["fa", "fb", "fc", "fd", "fe", "ff", "fg", "fh", "fi", "fj"]; if (!ids.every((i) => $("#" + i))) return;
  const v = ids.map((i) => +$("#" + i).value), inn = v.slice(0, 5).reduce((a, b) => a + b, 0), out = v.slice(5).reduce((a, b) => a + b, 0), net = inn - out;
  $("#fa1").textContent = "$" + inn + "bn"; $("#fa2").textContent = "$" + out + "bn"; $("#fa3").textContent = net > 2 ? "Rises" : net < -2 ? "Falls" : "Stable";
  $("#fav").textContent = `Demand for the currency (inflows) is $${inn}bn and supply (outflows) is $${out}bn. ${net > 2 ? `Demand exceeds supply by $${net}bn: the currency is under pressure to appreciate.` : net < -2 ? `Supply exceeds demand by $${-net}bn: the currency is under pressure to depreciate.` : "Demand and supply are roughly balanced: little pressure on the rate."} In a fixed system the central bank would have to buy or sell currency to stop the rate moving.`;
  const base = 290, k = 1.5; let o = SV.line(60, base, 700, base);
  [["Demand (inflows)", inn, "--good"], ["Supply (outflows)", out, "--bad"]].forEach(([n, x, c], i) => { const px = 190 + i * 260, h = x * k; o += SV.rect(px, base - h, 140, h, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.text(px + 70, base - h - 8, "$" + x + "bn", "lbl bd", { "text-anchor": "middle" }) + SV.text(px + 70, base + 22, n, "sm", { "text-anchor": "middle" }); });
  $("#labF").innerHTML = o;
}
FL.forEach(([l, v], i) => Lib.slider($("#gi" + (i + 1)), { id: ["fa", "fb", "fc", "fd", "fe"][i], label: "Demand: " + l, min: 0, max: 120, step: 5, value: v, fmt: (x) => "$" + x, onInput: labF }));
FO.forEach(([l, v], i) => Lib.slider($("#go" + (i + 1)), { id: ["ff", "fg", "fh", "fi", "fj"][i], label: "Supply: " + l, min: 0, max: 120, step: 5, value: v, fmt: (x) => "$" + x, onInput: labF }));
const TX = [
  { n: "A US firm buys British cars", a: "Demand for pounds", w: "It sells dollars to buy pounds to pay the exporter." },
  { n: "A British firm imports Japanese machinery", a: "Supply of pounds", w: "It sells pounds to buy yen." },
  { n: "A French tourist spends in London", a: "Demand for pounds", w: "Euros are exchanged for pounds." },
  { n: "A foreign investor buys UK shares", a: "Demand for pounds", w: "Foreign currency is sold to buy pounds." },
  { n: "A UK firm builds a factory in Poland", a: "Supply of pounds", w: "Pounds are sold to buy zloty." },
  { n: "A migrant in London sends money to India", a: "Supply of pounds", w: "Pounds are exchanged for rupees." },
  { n: "The Bank of England buys pounds with its reserves", a: "Demand for pounds", w: "Government intervention to raise the rate." },
  { n: "Speculators expect the pound to fall and sell it", a: "Supply of pounds", w: "Speculation increases supply." },
];
button_table("txBtns", "txOut", TX, 0, (p) => `<div class="tw"><table class="t"><tr><th>Effect on the UK pound</th><th>Why</th></tr><tr><td><b>${p.a}</b></td><td>${p.w}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Does each increase the <b>demand for</b> or the <b>supply of</b> a country's currency (the home currency)?", buckets: [{ label: "Demand for the home currency" }, { label: "Supply of the home currency" }], items: [
  { text: "Foreigners buy the country's exports", b: 0 }, { text: "Foreign tourists visit", b: 0 }, { text: "Foreign firms invest in the country", b: 0 }, { text: "Remittances sent home by workers abroad", b: 0 },
  { text: "Residents buy imports", b: 1 }, { text: "Residents go on holiday abroad", b: 1 }, { text: "Home firms invest abroad", b: 1 }, { text: "Foreign firms send profits home", b: 1 },
], done: "Foreigners buying from us demand our currency; we buying from them supply it." });
Lib.classify($("#cl2"), { prompt: "Which <b>reason for buying or selling currency</b> is each?", buckets: [{ label: "Trade" }, { label: "Speculation" }, { label: "Government intervention" }, { label: "Profits, remittances, investment" }], items: [
  { text: "A shop imports clothes", b: 0 }, { text: "A hotel receives foreign tourists", b: 0 },
  { text: "A trader buys a currency expecting it to rise", b: 1 }, { text: "A hedge fund sells a currency it expects to fall", b: 1 },
  { text: "A central bank sells reserves to lower the rate", b: 2 }, { text: "A central bank buys its own currency", b: 2 },
  { text: "Dividends sent to a foreign shareholder", b: 3 }, { text: "A worker abroad sending money home", b: 3 }, { text: "A firm buying a factory in another country", b: 3 },
], done: "Six reasons in the syllabus." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [
  ["Speculation", "Buying or selling a currency to make a profit from expected changes in its value"],
  ["Remittances", "Money sent home by workers abroad"],
  ["Dividends", "Payments of profit to shareholders"],
  ["Foreign direct investment", "Investment in factories and firms in another country"],
  ["Foreign exchange reserves", "A central bank's holdings of foreign currency"],
  ["Hot money", "Funds that move quickly between countries to earn the highest interest rate"],
], done: "Good vocabulary scores marks." });
Lib.order($("#o1"), { prompt: "Put the steps in order: <b>how an export creates demand for a currency</b>.", items: [
  "A foreign buyer orders goods from a UK firm",
  "The UK firm prices the goods in pounds",
  "The foreign buyer sells its own currency and buys pounds",
  "Demand for pounds rises",
  "The pound tends to appreciate",
], done: "Exports increase demand for the exporter's currency." });
Lib.calc($("#c1"), { qs: [
  { q: "Foreigners buy $80bn of a country's exports and $20bn of its services. Residents buy $90bn of imports. What is the net demand for the country's currency from trade ($bn)?", a: 10, sol: "(80 + 20) − 90 = <b>$10bn</b> net demand." },
  { q: "A country receives $12bn of remittances and sends $4bn abroad. What is the net flow in ($bn)?", a: 8, sol: "12 − 4 = <b>$8bn</b> inflow." },
  { q: "Foreign investment into a country is $25bn and its residents invest $30bn abroad. What is the net effect on demand for the currency ($bn)?", a: -5, sol: "25 − 30 = <b>−$5bn</b>: supply exceeds demand." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which increases the demand for a country's currency?", opts: ["Residents buying imports", "Foreigners buying its exports", "Residents investing abroad", "Profits sent abroad"], a: 1, why: "Foreigners need its currency." },
  { q: "A British tourist visiting Spain:", opts: ["Increases demand for pounds", "Increases supply of pounds", "Has no effect", "Raises the pound"], a: 1, why: "Sells pounds to buy euros." },
  { q: "Speculation can cause a currency to fall when speculators:", opts: ["Expect it to rise", "Expect it to fall and sell it", "Buy it", "Ignore it"], a: 1, why: "Selling raises supply." },
  { q: "Workers' remittances sent to a country:", opts: ["Reduce demand for its currency", "Increase demand for its currency", "Reduce supply", "Have no effect"], a: 1, why: "Foreign currency is converted into home currency." },
  { q: "Government intervention in currency markets means:", opts: ["The central bank buys or sells currency", "Firms trade only", "Tourists exchange money", "Banks set interest rates only"], a: 0, why: "Using reserves to move the rate." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Demand for a currency", "The amount of a currency that people want to buy at each exchange rate."],
  ["Supply of a currency", "The amount of a currency that people want to sell at each exchange rate."],
  ["Speculation", "Buying or selling a currency to profit from expected changes in its value."],
  ["Government intervention", "A central bank buying or selling currency to influence its value."],
  ["Remittances", "Money sent home by workers abroad."],
  ["Dividends", "Payments of profit by firms to shareholders."],
  ["Foreign exchange reserves", "A central bank's holdings of foreign currency."],
  ["Foreign direct investment (FDI)", "Investment by firms in factories and offices abroad."],
  ["Hot money", "Funds that move between countries seeking the highest interest rates."],
] });
labF(); 
