const op = (v) => ({ opacity: Math.max(0, Math.min(1, v)) });
const halo = { style: "paint-order:stroke;stroke:var(--surface);stroke-width:5px" };
const arrow = (x1, y1, x2, y2, dir, cls, v) => `<g style="opacity:${Math.max(0, Math.min(1, v))}">${SV.line(x1, y1, x2, y2, cls, { "stroke-width": 2.5 })}${SV.arrowHead(x2, y2, dir, cls === "c2" ? "dot2" : cls === "c3" ? "dot3" : cls === "c4" ? "dot4" : "dot1")}</g>`;
const axes = (x0, y0, x1, y1, xl, yl) => SV.line(x0, y0, x1, y0) + SV.line(x0, y0, x0, y1) + SV.text(x1, y0 + 26, xl, "sm", { "text-anchor": "end" }) + SV.text(x0 + 6, y1 - 6, yl, "sm");
const tag = (x, y, t, c, v = 1, a = "start") => SV.text(x, y, t, "lbl bd " + c, { "text-anchor": a, ...halo, ...op(v) });
/* click a button, show its row of results */
function btnTable(btnId, outId, rows, heads) {
  const box = $("#" + btnId), out = $("#" + outId); if (!box || !out) return;
  box.innerHTML = rows.map((r, i) => `<button class="b" data-i="${i}">${r[0]}</button>`).join("");
  const show = (i) => { const r = rows[i]; $$("button", box).forEach((b, k) => b.classList.toggle("pri", k === i)); out.innerHTML = `<div class="tw"><table class="t"><tr>${heads.map((h) => `<th>${h}</th>`).join("")}</tr><tr>${r.map((c, k) => `<td>${k ? c : "<b>" + c + "</b>"}</td>`).join("")}</tr></table></div>`; };
  $$("button", box).forEach((b) => (b.onclick = () => show(+b.dataset.i))); show(0);
}

const SDX = (q) => 70 + q * 6.4, SDY = (p) => 270 - p * 2.4;
const sdEq = (d, s) => { const q = 50 + 0.5 * (d + s); return { q, p: 10 + 0.8 * (q - s) }; };
const sdSeg = (k, sh) => {
  const f = (q) => (k === "D" ? 90 - 0.8 * (q - sh) : 10 + 0.8 * (q - sh)), inv = (p) => (k === "D" ? sh + (90 - p) / 0.8 : sh + (p - 10) / 0.8);
  const qa = inv(k === "D" ? 95 : 12), qb = inv(k === "D" ? 12 : 95), lo = Math.max(0, Math.min(qa, qb)), hi = Math.min(100, Math.max(qa, qb));
  return [lo, f(lo), hi, f(hi)];
};
const sdCurve = (k, sh, c, v, name) => { const [a, b, e, f] = sdSeg(k, sh); return SV.line(SDX(a), SDY(b), SDX(e), SDY(f), c, { "stroke-width": 3, ...op(v) }) + tag(SDX(e) + 6, SDY(f) + (k === "D" ? 14 : -4), name, c, v); };
const sdGuide = (e, pn, qn, v) => SV.line(SDX(e.q), SDY(e.p), SDX(e.q), 270, "dash", op(v)) + SV.line(70, SDY(e.p), SDX(e.q), SDY(e.p), "dash", op(v)) + SV.text(62, SDY(e.p) + 4, pn, "sm", { "text-anchor": "end", ...op(v) }) + SV.text(SDX(e.q), 286, qn, "sm", { "text-anchor": "middle", ...op(v) });
function sdPlot(st, lab = {}) {
  const { d = 0, s = 0, g = 1, n = 1 } = st, mv = Math.abs(d) > 0.05 || Math.abs(s) > 0.05, e0 = sdEq(0, 0), e1 = sdEq(d, s);
  let o = axes(70, 270, 720, 25, lab.x || "Quantity", lab.y || "Price");
  o += sdCurve("D", 0, "c2", Math.abs(d) > 0.05 ? 0.4 : 1, lab.D1 || "D1") + sdCurve("S", 0, "c1", Math.abs(s) > 0.05 ? 0.4 : 1, lab.S1 || "S1");
  if (Math.abs(d) > 0.05) o += sdCurve("D", d, "c2", n, lab.D2 || "D2");
  if (Math.abs(s) > 0.05) o += sdCurve("S", s, "c1", n, lab.S2 || "S2");
  o += SV.circle(SDX(e0.q), SDY(e0.p), 5, "dot1", op(mv ? 0.6 : 1)) + sdGuide(e0, lab.P1 || "P1", lab.Q1 || "Q1", g * (mv ? 0.5 : 1));
  if (mv) o += SV.circle(SDX(e1.q), SDY(e1.p), 6, "dot3", op(n)) + sdGuide(e1, lab.P2 || "P2", lab.Q2 || "Q2", g * n);
  return o;
}

function bsDraw(s) {
  const fl = 45, ce = 55; let o = sdPlot({ d: 0, s: s.s, g: 0, n: 1 }, { S1: "S (normal)", S2: "S (this year)" });
  o += SV.line(70, SDY(fl), 720, SDY(fl), "c4", { "stroke-width": 2, "stroke-dasharray": "7 4" }) + tag(724, SDY(fl) + 14, "Floor $45", "c4", 1, "end") + SV.line(70, SDY(ce), 720, SDY(ce), "c4", { "stroke-width": 2, "stroke-dasharray": "7 4" }) + tag(724, SDY(ce) - 6, "Ceiling $55", "c4", 1, "end");
  const ec = sdEq(0, s.s);
  if (ec.p < fl - 0.5) { const qd = (90 - fl) / 0.8, qs = (fl - 10) / 0.8 + s.s; o += SV.rect(SDX(qd), SDY(fl) - 8, SDX(qs) - SDX(qd), 16, "f2", op(0.75)) + tag(SDX(qs) + 8, SDY(fl) + 4, "agency buys " + Lib.fmtN(qs - qd, 1), "c2"); }
  if (ec.p > ce + 0.5) { const qd = (90 - ce) / 0.8, qs = (ce - 10) / 0.8 + s.s; o += SV.rect(SDX(qs), SDY(ce) - 8, SDX(qd) - SDX(qs), 16, "f3", op(0.75)) + tag(SDX(qd) + 8, SDY(ce) + 4, "agency sells " + Lib.fmtN(qd - qs, 1), "c3"); }
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="A good harvest shifts supply right and the agency buys the surplus at the floor price">${bsDraw({ s: 25 })}</svg>`;
Lib.stepper($("#stB"), { w: 760, h: 300, label: "A buffer stock scheme with a price band of $45 to $55", base: { s: 0 }, draw: bsDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>A normal year.</b> The market clears at $50, inside the price band of $45 to $55, so the agency does nothing.", s: { s: 0 } },
  { cap: "<b>A good harvest.</b> Supply shifts right and the price would fall to $40, below the floor. The agency buys about 12.5 units at $45 and stores them.", s: { s: 25 } },
  { cap: "<b>A poor harvest.</b> Supply shifts left and the price would rise to $60, above the ceiling. The agency sells about 12.5 units from its stock at $55.", s: { s: -25 } },
] });

/* ---------- eight years ---------- */
const SH = [0, 25, -25, 10, -25, -25, 25, 0], FLO = 45, CEI = 55;
function yearSim() { let stock = 20, out = []; SH.forEach((s) => { const free = 50 - 0.4 * s; let buy = 0, sell = 0, p = free; if (free < FLO) { buy = Math.max(0, s - 12.5); p = FLO; } else if (free > CEI) { sell = Math.max(0, -s - 12.5); if (sell > stock) { sell = stock; p = free; } else p = CEI; } stock = stock + buy - sell; out.push({ free, p, stock }); }); return out; }
const SIM = yearSim();
function yrDraw(s) {
  const x = (i) => 90 + i * 80, y = (p) => 200 - (p - 35) * 5; let o = SV.line(60, 200, 740, 200) + SV.line(60, 40, 60, 200) + SV.text(66, 34, "Price ($)", "sm") + SV.line(60, y(FLO), 740, y(FLO), "c4", { "stroke-dasharray": "6 4" }) + SV.line(60, y(CEI), 740, y(CEI), "c4", { "stroke-dasharray": "6 4" }) + SV.text(56, y(FLO) + 4, "45", "sm", { "text-anchor": "end" }) + SV.text(56, y(CEI) + 4, "55", "sm", { "text-anchor": "end" });
  const n = Math.round(s.t); let a = "", b = "";
  SIM.forEach((r, i) => { if (i < n) { a += (i ? " L" : "M") + x(i) + "," + y(r.free); b += (i ? " L" : "M") + x(i) + "," + y(r.p); o += SV.rect(x(i) - 14, 270 - r.stock * 2, 28, r.stock * 2, "f2", op(0.6)) + SV.text(x(i), 286, "Y" + (i + 1), "sm", { "text-anchor": "middle" }) + SV.text(x(i), 264 - r.stock * 2, Lib.fmtN(r.stock, 0), "sm", { "text-anchor": "middle" }); } });
  if (a) o += SV.path(a, "c1", { fill: "none", "stroke-width": 2, "stroke-dasharray": "5 4" }) + SV.path(b, "c2", { fill: "none", "stroke-width": 3 }) + tag(742, 60, "Stock (bars)", "c2", 1, "end");
  return o + SV.text(60, 226, "Dashed = free-market price; solid = price with the scheme", "sm");
}
$("#pic2").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="Price with and without the scheme over eight years, with stock levels as bars">${yrDraw({ t: 8 })}</svg>`;
Lib.stepper($("#stY"), { w: 760, h: 300, label: "Harvests, prices and stocks over eight years", base: { t: 0 }, draw: yrDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>The band</b> is $45 to $55. The agency starts with 20 units of stock.", s: { t: 0 } },
  { cap: "<b>Years 1 to 3.</b> A good harvest in year 2 (price would be $40): the agency buys and stock rises. A poor harvest in year 3 (price would be $60): it sells and stock falls. Prices stay in the band.", s: { t: 3 } },
  { cap: "<b>Years 4 to 5.</b> Another poor harvest in year 5 draws the stock down further, to a low level.", s: { t: 5 } },
  { cap: "<b>Years 6 to 8.</b> Another poor harvest in year 6 <b>exhausts the stock</b>: the agency can no longer hold the price, which jumps to the free-market level.", s: { t: 8 } },
] });

/* ---------- Lab 1 ---------- */
function labB() {
  if (!$("#sh") || !$("#fl") || !$("#ce")) return;
  const s = +$("#sh").value, fl = +$("#fl").value, ce = +$("#ce").value, free = 50 - 0.4 * s, qd = (p) => (90 - p) / 0.8, qs = (p) => (p - 10) / 0.8 + s;
  let p = free, act = "None";
  if (free < fl) { p = fl; act = "Buys " + Lib.fmtN(qs(fl) - qd(fl), 1); } else if (free > ce) { p = ce; act = "Sells " + Lib.fmtN(qd(ce) - qs(ce), 1); }
  $("#r1").textContent = "$" + Lib.fmtN(free, 1); $("#r2").textContent = "$" + Lib.fmtN(p, 1); $("#r3").textContent = act;
  $("#rv").textContent = fl >= ce ? "The floor must be below the ceiling." : act === "None" ? `The free-market price of $${Lib.fmtN(free, 1)} is inside the band of $${fl} to $${ce}, so the agency does nothing.` : free < fl ? `The harvest would push the price down to $${Lib.fmtN(free, 1)}, below the floor of $${fl}. The agency buys ${act.slice(5)} units and stores them, holding the price at $${fl}.` : `The shortfall would push the price up to $${Lib.fmtN(free, 1)}, above the ceiling of $${ce}. The agency sells ${act.slice(6)} units from stock, holding the price at $${ce}.`;
  let o = sdPlot({ d: 0, s, g: 0, n: 1 }) + SV.line(70, SDY(fl), 720, SDY(fl), "c4", { "stroke-dasharray": "7 4", "stroke-width": 2 }) + SV.line(70, SDY(ce), 720, SDY(ce), "c4", { "stroke-dasharray": "7 4", "stroke-width": 2 });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "sh", label: "Harvest shock (negative = poor, positive = good) ", min: -30, max: 30, step: 5, value: 25, fmt: (v) => v, onInput: labB });
Lib.slider($("#g2"), { id: "fl", label: "Floor price, $ ", min: 35, max: 50, step: 1, value: 45, fmt: (v) => "$" + v, onInput: labB });
Lib.slider($("#g3"), { id: "ce", label: "Ceiling price, $ ", min: 50, max: 65, step: 1, value: 55, fmt: (v) => "$" + v, onInput: labB });
labB();

/* ---------- Lab 2 ---------- */
function labR() {
  if (!$("#st0") || !$("#bad")) return;
  const S0 = +$("#st0").value, s = +$("#bad").value, sell = Math.max(0, s - 12.5), yrs = sell > 0 ? Math.floor(S0 / sell) : Infinity, free = 50 + 0.4 * s;
  $("#t1").textContent = sell > 0 ? Lib.fmtN(sell, 1) : "None"; $("#t2").textContent = sell > 0 ? yrs + " year" + (yrs === 1 ? "" : "s") : "Indefinitely"; $("#t3").textContent = "$" + Lib.fmtN(free, 0);
  $("#tv").textContent = sell <= 0 ? "The shortfall is small enough that the price stays inside the band without any sales, so the stock is not used." : `Each poor year the agency must sell ${Lib.fmtN(sell, 1)} units to hold the price at $55. A stock of ${S0} lasts about ${yrs} year${yrs === 1 ? "" : "s"}. After that the scheme cannot hold the price and it jumps to about $${Lib.fmtN(free, 0)}.`;
  let o = SV.line(60, 250, 740, 250) + SV.line(60, 250, 60, 40) + SV.text(66, 34, "Stock (units)", "sm"), st = S0;
  for (let i = 0; i < 8; i++) { const h = Math.max(0, st) * (200 / 80); o += SV.rect(90 + i * 80 - 16, 250 - h, 32, h, "f2", op(0.65)) + SV.text(90 + i * 80, 268, "Year " + (i + 1), "sm", { "text-anchor": "middle" }) + SV.text(90 + i * 80, 244 - h, Lib.fmtN(Math.max(0, st), 0), "sm", { "text-anchor": "middle" }); st = Math.max(0, st - sell); }
  $("#labB").innerHTML = o;
}
Lib.slider($("#g4"), { id: "st0", label: "Starting stock, units ", min: 10, max: 80, step: 5, value: 30, fmt: (v) => v, onInput: labR });
Lib.slider($("#g5"), { id: "bad", label: "Size of the poor harvest each year (units of supply lost) ", min: 15, max: 40, step: 1, value: 25, fmt: (v) => v, onInput: labR });
labR();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "What does the agency do?", buckets: [{"label": "Buys into stock"}, {"label": "Sells from stock"}, {"label": "Does nothing"}], items: [{"text": "Good harvest: price falls to the floor", "b": 0}, {"text": "Poor harvest: price rises to the ceiling", "b": 1}, {"text": "Price is inside the band", "b": 2}, {"text": "Bumper crop pushes price below the minimum", "b": 0}, {"text": "Drought pushes price above the maximum", "b": 1}, {"text": "Market price equals the long-run average", "b": 2}, {"text": "A surplus builds up at the floor price", "b": 0}, {"text": "Stocks are released to hold the price down", "b": 1}], done: "Buy at the floor, sell at the ceiling, do nothing in between." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Buffer stock scheme", "A scheme that buys and sells to stabilise a price"], ["Floor price", "The minimum price at which the agency buys"], ["Ceiling price", "The maximum price at which the agency sells"], ["Price band", "The range between the floor and the ceiling"], ["Run out of stock", "A risk after a series of poor harvests"], ["Storage cost", "A cost of buying surplus in good years"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put what happens after a poor harvest in order.", items: ["A drought cuts the harvest", "Supply shifts to the left", "The price rises towards the ceiling", "The agency sells from its stock", "The price is held at the ceiling"], done: "Poor harvest, price up, agency sells." });
Lib.calc($("#c1"), { qs: [
  {"q": "At the floor price of $45 the agency buys 12.5 units. How much does it spend ($)?", "a": 562.5, "unit": "$", "tol": 1, "hint": "45 × 12.5.", "sol": "<b>$562.50</b>."},
  {"q": "The agency holds 20 units and must sell 12.5 each poor year. How many full years does the stock last?", "a": 1, "unit": "years", "tol": 0.1, "hint": "20 ÷ 12.5 rounded down.", "sol": "<b>1 year</b>, with 7.5 left."},
  {"q": "The free-market price would be $60 but the ceiling is $55. By what percentage does the scheme cut the price?", "a": 8.3, "unit": "%", "tol": 0.2, "hint": "5 ÷ 60.", "sol": "<b>8.3%</b>."},
  {"q": "A scheme sells 12.5 units at $55. What revenue does the agency receive ($)?", "a": 687.5, "unit": "$", "tol": 1, "hint": "55 × 12.5.", "sol": "<b>$687.50</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A buffer stock scheme aims to:", opts: ["Stabilise price", "Raise price permanently", "Lower price permanently", "Ban imports"], a: 0, why: "Stability." },
  { q: "In a good harvest the agency:", opts: ["Buys the surplus", "Sells stock", "Cuts the floor", "Taxes farmers"], a: 0, why: "Price is pushed down." },
  { q: "A main risk of a buffer stock scheme is:", opts: ["Running out of stock or money", "Too little storage demand", "Lower taxes", "Fewer buyers"], a: 0, why: "Finite stock." },
  { q: "Agricultural prices fluctuate because:", opts: ["Supply varies and demand and supply are inelastic", "Demand is always elastic", "Supply is fixed", "Prices are set by the government"], a: 0, why: "Weather and inelasticity." },
  { q: "A floor price above the long-run equilibrium will:", opts: ["Build up growing surpluses", "Cut surpluses", "Raise demand", "Have no effect"], a: 0, why: "The agency keeps buying." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Buffer stock", "Buy and sell to stabilise price."],
  ["Floor", "Buy at the minimum price."],
  ["Ceiling", "Sell at the maximum price."],
  ["Good harvest", "Agency buys."],
  ["Poor harvest", "Agency sells."],
  ["Cost", "Buying, storage, spoilage."],
  ["Risk", "Stock or money runs out."],
  ["Alternatives", "Subsidies, futures markets."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "The market for wheat is in equilibrium at price P with supply at 40 million tonnes. Due to a drought in the growing season, supply falls to 20 million tonnes. Which immediate action should be taken to maintain the equilibrium price of P? (Feb/March 2021 · 12 · Q12, reworded)", opts: ["grant a subsidy to farmers equivalent to the rise in price", "impose an indirect tax equivalent to the rise in price", "plant more wheat to increase supplies to 40 million tonnes", "use existing stocks of wheat to increase supplies by 20 million tonnes"], a: 3, why: "Planting takes a season, and subsidies or taxes would not restore supply at once. Releasing existing stocks does." },
  { q: "Which event is most likely to enable firms to respond to an increase in demand by increasing supply rather than by raising price? (Oct/Nov 2023 · 11 · Q12, reworded)", opts: ["Firms reduce their expenditure on the training of workers", "Import duties are increased on machines that increase the speed of production", "The government introduces buffer stock schemes for the goods produced by the firm", "Trade unions become strong, leading to poor labour productivity"], a: 2, why: "A buffer stock can be released to meet demand, so supply rises instead of price." },
  { q: "A country depends heavily on the production of an agricultural product, good X. It decides to introduce a buffer stock scheme for good X. The government allocates a fixed amount of money for setting up and running the scheme. In which situation is the scheme least likely to run out of money? (new farmers can start growing good X easily or with difficulty; the cost of storing good X is high or low; global demand for good X is constant or rising) (May/June 2025 · 13 · Q14, reworded)", opts: ["easy to start, high storage cost, constant demand", "easy to start, low storage cost, rising demand", "difficult to start, high storage cost, constant demand", "difficult to start, low storage cost, rising demand"], a: 3, why: "Difficult entry limits new supply, low storage costs reduce spending, and rising demand keeps prices above the floor so the agency buys less." },
] });
