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

const TR = ["Buyers want goods and are willing and able to pay", "Sellers offer goods at the price they need to cover costs and make profit", "They agree a price and trade", "Buyers receive goods; sellers receive income", "The price tells both sides how to act next"];
Lib.stepper($("#stT"), { w: 760, h: 380, label: "A market transaction", base: { n: 0 }, draw: mkChain(TR, "--accent"), steps: chainSteps(["<b>Buyers</b> want goods and are willing and able to pay.", "<b>Sellers</b> offer goods at a price that covers costs and makes a profit.", "They <b>agree a price</b> and trade.", "Buyers receive goods; sellers receive <b>income</b>.", "The <b>price</b> tells both sides how to act next."]) });
const PM = ["Consumers want more of a good", "Demand rises and the price rises", "Higher profit attracts firms: they produce more", "Resources move into this good", "The market has answered 'what to produce'"];
Lib.stepper($("#stP"), { w: 760, h: 380, label: "The price mechanism at work", base: { n: 0 }, draw: mkChain(PM, "--good"), steps: chainSteps(["Consumers want <b>more of a good</b>.", "Demand rises and the <b>price rises</b>.", "Higher profit attracts firms: they <b>produce more</b>.", "<b>Resources move</b> into this good.", "The market has answered <b>what to produce</b>."]) });

/* Lab 1: market price and trades */
const BUY = [90, 80, 70, 60, 50, 40, 30, 20], SELL = [20, 30, 40, 50, 60, 70, 80, 90];
function labM() {
  if (!$("#pa")) return;
  const p = +$("#pa").value, nb = BUY.filter((v) => v >= p).length, ns = SELL.filter((v) => v <= p).length, q = Math.min(nb, ns), rev = q * p;
  $("#pa1").textContent = nb; $("#pa2").textContent = ns; $("#pa3").textContent = q;
  $("#pav").textContent = `At a price of $${p}, ${nb} buyers are willing to buy and ${ns} sellers are willing to sell. ${nb > ns ? "More want to buy than sell: a shortage, so the price tends to rise." : nb < ns ? "More want to sell than buy: a surplus, so the price tends to fall." : "Buyers and sellers match: the market clears."} ${q} trades take place (revenue $${rev}).`;
  const base = 290; let o = SV.line(60, base, 700, base);
  BUY.forEach((v, i) => { const x = 80 + i * 76, ok = v >= p, h = v * 2; o += SV.rect(x, base - h, 30, h, "", { style: "fill:var(--accent)", opacity: ok ? 0.85 : 0.25 }) + SV.rect(x + 32, base - SELL[i] * 2, 30, SELL[i] * 2, "", { style: "fill:var(--warn)", opacity: SELL[i] <= p ? 0.85 : 0.25 }); });
  o += SV.line(60, base - p * 2, 700, base - p * 2, "gr") + SV.text(700, base - p * 2 - 6, "Price $" + p, "lbl bd", { "text-anchor": "end" }) + SV.text(60, 24, "Blue: most each buyer will pay. Orange: least each seller will accept.", "sm");
  $("#labM").innerHTML = o;
}
Lib.slider($("#g1"), { id: "pa", label: "Market price", min: 10, max: 100, step: 10, value: 50, fmt: (v) => "$" + v, onInput: labM });
const MK = [
  { n: "A farmers' market", t: "Goods market", b: "Shoppers", s: "Farmers" },
  { n: "An online shop", t: "Goods market", b: "Online shoppers", s: "The retailer" },
  { n: "Hairdressing", t: "Services market", b: "Customers", s: "Hairdressers" },
  { n: "The labour market", t: "Factor market", b: "Firms (buy labour)", s: "Workers (sell labour)" },
  { n: "The stock market", t: "Financial market", b: "Investors", s: "Share owners" },
  { n: "The world oil market", t: "Global commodity market", b: "Importing countries and firms", s: "Oil producers" },
];
button_table("mkBtns", "mkOut", MK, 0, (p) => `<div class="tw"><table class="t"><tr><th>Type</th><th>Buyers</th><th>Sellers</th></tr><tr><td><b>${p.t}</b></td><td>${p.b}</td><td>${p.s}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Which <b>type of market</b> is each?", buckets: [{ label: "Goods market" }, { label: "Services market" }, { label: "Factor market" }, { label: "Financial market" }], items: [
  { text: "Cars", b: 0 }, { text: "Coffee", b: 0 },
  { text: "Hairdressing", b: 1 }, { text: "Tourism", b: 1 },
  { text: "The labour market", b: 2 }, { text: "Rented farmland", b: 2 },
  { text: "Foreign exchange", b: 3 }, { text: "Shares", b: 3 },
], done: "Goods, services, factors, finance." });
Lib.classify($("#cl2"), { prompt: "Is each a <b>buyer</b> or a <b>seller</b> in the market named?", buckets: [{ label: "Buyer" }, { label: "Seller" }], items: [
  { text: "A shopper in a supermarket", b: 0 }, { text: "A firm hiring workers (labour market)", b: 0 }, { text: "A government buying medicines", b: 0 },
  { text: "A farmer selling wheat", b: 1 }, { text: "A worker offering labour (labour market)", b: 1 }, { text: "A shop selling clothes", b: 1 },
], done: "Both sides are needed for a market." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [
  ["Market", "Where buyers and sellers meet to trade"],
  ["Demand", "Willingness and ability to buy at a price"],
  ["Supply", "Willingness and ability to sell at a price"],
  ["Price mechanism", "Prices adjusting to allocate resources"],
  ["Price signal", "Information from prices to buyers and sellers"],
  ["Incentive", "A reason to act, such as profit"],
], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how the price mechanism reallocates resources</b>.", items: [
  "Consumers want more of a good",
  "Demand rises and the price rises",
  "Profit in that market rises",
  "Firms produce more of it",
  "Resources move into its production",
], done: "The price mechanism in action." });
Lib.calc($("#c1"), { qs: [
  { q: "At a price of $50, 5 buyers want to buy and 4 sellers want to sell. How many units are in shortage?", a: 1, sol: "5 − 4 = <b>1</b>." },
  { q: "A market sells 200 units at $12. What is the total revenue ($)?", a: 2400, sol: "200 × 12 = <b>$2,400</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A market is:", opts: ["A place only", "Where buyers and sellers meet to trade", "A shop", "A government"], a: 1, why: "It can be online." },
  { q: "Which is a factor market?", opts: ["The labour market", "The car market", "The coffee market", "A hairdresser"], a: 0, why: "Resources are bought and sold." },
  { q: "Buyers in a market want:", opts: ["High prices", "Low prices", "No goods", "Taxes"], a: 1, why: "Get the most for their money." },
  { q: "What is the role of the price mechanism in a market economy?", opts: ["To allocate resources through prices", "To plan output", "To set wages", "To collect taxes"], a: 0, why: "Prices signal and incentivise." },
  { q: "Demand requires consumers to be:", opts: ["Willing only", "Able only", "Willing and able to pay", "Rich"], a: 2, why: "Both." },
] });

Lib.cards($("#fc1"), { cards: [
  ["Market", "Where buyers and sellers meet to trade goods, services or resources."],
  ["Buyer (consumer)", "Someone who demands goods and services."],
  ["Seller (producer)", "Someone who supplies goods and services."],
  ["Demand", "The quantity buyers are willing and able to buy at each price."],
  ["Supply", "The quantity sellers are willing and able to sell at each price."],
  ["Price mechanism", "The way prices adjust to allocate resources."],
  ["Price signal", "Information from price changes."],
  ["Incentive", "A reason to change behaviour, such as profit."],
  ["Factor market", "A market for the factors of production."],
] });
labM(); 
