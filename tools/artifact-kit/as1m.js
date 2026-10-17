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

function chainDraw(nodes, k) {
  const H = 40, G = 16; let o = "";
  nodes.forEach((t, i) => {
    const v = Math.max(0, Math.min(1, k - i)); if (v <= 0) return;
    const y = 8 + i * (H + G);
    o += SV.rect(30, y, 700, H, ["f1", "f2", "f3"][i % 3], { rx: 8, ...op(0.55 * v) }) + SV.text(380, y + 25, t, "lbl bd", { "text-anchor": "middle", ...op(v) });
    if (i > 0) o += SV.poly([[373, y - 10], [387, y - 10], [380, y - 2]], "dot4", op(v));
  });
  return o;
}
function chainStep(el, label, nodes, caps) {
  Lib.stepper($(el), { w: 760, h: 16 + nodes.length * 56, label, base: { k: 0 }, draw: (s) => chainDraw(nodes, s.k), tween: 700, dwell: 5200, steps: nodes.map((n, i) => ({ cap: caps[i], s: { k: i + 1 } })) });
}
function chooser(p, items, tmpl, lab = "Strength of the case") {
  const show = (i) => {
    const it = items[i]; $$("#" + p + "B button").forEach((b, k) => b.classList.toggle("pri", k === i));
    $("#" + p + "1").textContent = it[1]; $("#" + p + "2").textContent = it[2]; $("#" + p + "3").textContent = it[3]; $("#" + p + "v").textContent = tmpl(it);
    const w = (it[4] / 5) * 340;
    $("#" + p + "S").innerHTML = SV.text(210, 60, it[0], "lbl bd", { "text-anchor": "middle", style: "font-size:20px" }) + SV.rect(40, 100, 340, 18, "f3", { rx: 9, ...op(0.2) }) + SV.rect(40, 100, w, 18, "f1", { rx: 9, ...op(0.7) }) + SV.text(210, 146, lab + ": " + it[4] + " out of 5", "sm", { "text-anchor": "middle" });
  };
  $("#" + p + "B").innerHTML = items.map((t, i) => `<button class="b" data-i="${i}">${t[0]}</button>`).join("");
  $$("#" + p + "B button").forEach((b) => (b.onclick = () => show(+b.dataset.i)));
  show(0);
}

$("#pic1").innerHTML = (() => {
  const B = [["Private ownership", "Firms and factors owned privately", 20, "f1"], ["Profit motive", "Firms supply what pays", 270, "f2"], ["Competition", "Rivals cut costs and improve quality", 520, "f3"]];
  let o = ""; B.forEach(([n, d, x, c]) => { o += SV.rect(x, 12, 220, 80, c, { rx: 12, ...op(0.45) }) + SV.text(x + 110, 46, n, "lbl bd", { "text-anchor": "middle", style: "font-size:16px" }) + SV.text(x + 110, 72, d, "sm", { "text-anchor": "middle" }); });
  return `<svg viewBox="0 0 760 104" role="img" aria-label="Private ownership, profit motive and competition are features of a market economy">${o}</svg>`;
})();
$("#pic2").innerHTML = (() => {
  const B = [["What?", "What consumers will pay for", 20, "f1"], ["How?", "The cheapest method wins", 270, "f2"], ["For whom?", "Those able to pay", 520, "f3"]];
  let o = ""; B.forEach(([n, d, x, c]) => { o += SV.rect(x, 12, 220, 80, c, { rx: 12, ...op(0.45) }) + SV.text(x + 110, 46, n, "lbl bd", { "text-anchor": "middle", style: "font-size:18px" }) + SV.text(x + 110, 72, d, "sm", { "text-anchor": "middle" }); });
  return `<svg viewBox="0 0 760 104" role="img" aria-label="The market answers what, how and for whom through prices">${o}</svg>`;
})();
const mkLab = { x: "Quantity", y: "Price", D1: "D1", D2: "D2", S1: "S1", S2: "S2", P1: "P1", Q1: "Q1", P2: "P2", Q2: "Q2" };
function mkDraw(s) { return sdPlot({ d: s.d, s: s.s, g: 1, n: s.n }, mkLab); }
Lib.stepper($("#stA"), { w: 760, h: 300, label: "A rise in demand and the price signal", base: { d: 0, s: 0, n: 0 }, draw: mkDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>Start.</b> Demand and supply give an equilibrium price of 50 and quantity of 50.", s: { d: 0, s: 0, n: 0 } },
  { cap: "<b>Consumers want more.</b> Demand shifts right. At the old price there is a shortage.", s: { d: 20, s: 0, n: 1 } },
  { cap: "<b>The price rises</b> to 58. It <b>rations</b> the scarce good, <b>signals</b> that more is wanted and <b>incentivises</b> firms to supply more: quantity rises to 60.", s: { d: 20, s: 0, n: 1 } },
  { cap: "<b>If supply also expands</b> in response to profits, the price stops rising and quantity rises further.", s: { d: 20, s: 20, n: 1 } },
] });
chainStep("#stB", "How resources move without planning", ["Consumers' tastes shift towards a product", "Demand rises and the price goes up", "Profits in that industry rise", "Firms expand and new firms enter; resources move in", "Other industries lose resources: the market has reallocated them"], [
  "<b>Consumer sovereignty</b> drives the change.", "<b>Price signals</b> the new preference.", "<b>Profit</b> is the incentive.", "<b>Supply</b> expands.", "<b>No central planner</b> was needed."]);
chainStep("#stC", "Why a market fails to supply a public good", ["A good is non-excludable and non-rival", "People can use it without paying (free riders)", "Few people pay voluntarily, so revenue is low", "A private firm makes a loss and does not supply it", "The market fails; the government provides it"], [
  "<b>Street lighting</b> or defence.", "<b>Free riders:</b> why pay if others do?", "<b>No revenue</b> for the firm.", "<b>No supply</b> from the market.", "<b>Government provision</b> financed by taxes (see 3.1)."]);

function labM() {
  if (!["gd", "gs"].every((i) => $("#" + i))) return;
  const d = +$("#gd").value, s = +$("#gs").value, e = sdEq(d, s);
  $("#r1").textContent = Lib.fmtN(e.p, 1); $("#r2").textContent = Lib.fmtN(e.q, 1); $("#r3").textContent = e.p > 50.5 ? "Price up: produce more" : e.p < 49.5 ? "Price down: produce less" : "No change";
  $("#rv").textContent = (Math.abs(d) < 0.5 && Math.abs(s) < 0.5) ? "No change in demand or supply, so the price signal is unchanged." : `Price moves from 50 to ${Lib.fmtN(e.p, 1)} and quantity from 50 to ${Lib.fmtN(e.q, 1)}. ${e.p > 50.5 ? "The higher price rations the good, signals higher demand or scarcity and gives firms an incentive to supply more." : e.p < 49.5 ? "The lower price signals falling demand or a surplus and gives firms an incentive to cut output or leave." : "The two changes offset each other in price."}`;
  $("#labA").innerHTML = sdPlot({ d, s, g: 1, n: 1 }, mkLab);
}
Lib.slider($("#g1"), { id: "gd", label: "Shift in demand ", min: -30, max: 30, step: 5, value: 20, fmt: (v) => (v > 0 ? "+" : "") + v, onInput: labM });
Lib.slider($("#g2"), { id: "gs", label: "Shift in supply ", min: -30, max: 30, step: 5, value: 0, fmt: (v) => (v > 0 ? "+" : "") + v, onInput: labM });
labM();

chooser("h", [
  ["Concert tickets sell out and the price rises", "Rationing", "The higher price limits demand to the available seats", "Those most willing and able to pay get tickets", 5],
  ["The price of electric cars keeps rising", "Signalling", "The price passes information about growing demand", "Firms learn what consumers want", 5],
  ["Rising profits attract new bakeries", "Incentivising", "Higher prices and profit encourage more supply", "More firms enter the market", 5],
  ["A bumper harvest cuts wheat prices", "Signalling and incentive", "Lower prices signal a surplus and discourage production", "Farmers may switch crops", 4],
  ["A hotel doubles its room rate in a busy week", "Rationing", "The price rise limits demand", "Rooms go to those willing and able to pay", 4]
], (it) => `${it[0]}: this is the ${it[1].toLowerCase()} function. ${it[2]}. Result: ${it[3].toLowerCase()}.`, "How clearly it fits the function");
chooser("k", [
  ["Competition between firms", "Strength", "Keeps costs and prices down and raises quality", "Competition policy if monopoly appears", 5],
  ["Consumer choice", "Strength", "Firms produce a wide range of goods", "None needed", 4],
  ["Profit as an incentive to innovate", "Strength", "Rewards new ideas and risk-taking", "Patents, R&D support", 4],
  ["No provision of public goods", "Weakness", "Free riders mean no revenue for firms", "Government provision from taxes", 5],
  ["Under-consumption of merit goods", "Weakness", "Consumers lack information or income", "Subsidies, direct provision", 4],
  ["Inequality of income", "Weakness", "Output goes to those who can pay", "Taxes, benefits, free services", 4],
  ["Monopoly power", "Weakness", "A firm with no rivals can raise prices", "Regulation, competition law", 3]
], (it) => `${it[0]}: a ${it[1].toLowerCase()} of a market economy. ${it[2]}. Government response: ${it[3].toLowerCase()}.`, "Importance");
Lib.classify($("#cl1"), { prompt: "Which function of price is it?", buckets: [{"label": "Rationing"}, {"label": "Signalling"}, {"label": "Incentivising"}], items: [{"text": "A higher price limits demand to the available supply", "b": 0}, {"text": "A rising price tells firms consumers want more", "b": 1}, {"text": "Higher profits encourage firms to produce more", "b": 2}, {"text": "Scarce tickets go to those willing and able to pay", "b": 0}, {"text": "Falling prices show demand has dropped", "b": 1}, {"text": "Low prices push firms to leave a market", "b": 2}], done: "Rationing allocates limited supply; signalling transmits information; incentivising changes producers' behaviour." });
Lib.classify($("#cl2"), { prompt: "Strength or weakness of a market economy?", buckets: [{"label": "Strength"}, {"label": "Weakness"}], items: [{"text": "Competition encourages efficiency", "b": 0}, {"text": "Public goods are not provided", "b": 1}, {"text": "Wide consumer choice", "b": 0}, {"text": "Output goes to those who can pay, so inequality", "b": 1}, {"text": "Prices adjust quickly to new preferences", "b": 0}, {"text": "Prices may not reflect external costs", "b": 1}, {"text": "Profit rewards innovation", "b": 0}, {"text": "Merit goods are under-consumed", "b": 1}], done: "Strengths: efficiency, choice, innovation, flexibility. Weaknesses: market failure and inequality." });
Lib.order($("#o1"), { prompt: "Put the price signal in order.", items: ["Consumer demand for a good rises", "The price rises", "Firms' profits rise", "More firms produce the good", "Supply increases and the price stabilises"], done: "Demand up, price up, profit up, supply up." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Market economy", "An economy where the price mechanism allocates resources"], ["Rationing", "Price limits demand to the available supply"], ["Signalling", "Prices transmit information about preferences"], ["Incentivising", "Prices and profit encourage production"], ["Consumer sovereignty", "Consumers' spending decides what is produced"], ["Market failure", "An inefficient allocation of resources by the market"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "Demand is P = 90 − Q and supply P = 10 + Q. What is the equilibrium price?", "a": 50, "unit": "", "tol": 0.5, "hint": "90 − Q = 10 + Q gives Q = 40.", "sol": "<b>50</b>, with quantity 40."},
  {"q": "Demand rises so that P = 110 − Q (supply unchanged). What is the new equilibrium price?", "a": 60, "unit": "", "tol": 0.5, "hint": "110 − Q = 10 + Q gives Q = 50.", "sol": "<b>60</b>, with quantity 50."},
  {"q": "By what % does the price rise from 50 to 60?", "a": 20, "unit": "%", "tol": 0.1, "hint": "10 ÷ 50.", "sol": "<b>20%</b>."},
  {"q": "A firm sells 500 units at a price of $12 with costs of $9 per unit. What is its profit ($)?", "a": 1500, "unit": "$", "tol": 0.5, "hint": "(12 − 9) × 500.", "sol": "<b>$1,500</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "The price mechanism allocates resources through:", opts: ["Demand and supply", "Central planning", "Government orders", "Tax revenue"], a: 0, why: "Prices signal scarcity and preferences." },
  { q: "Rationing means:", opts: ["Price limits demand to the available supply", "Government gives out goods", "Price falls to zero", "Output is planned"], a: 0, why: "A function of price." },
  { q: "In a market economy 'for whom' is decided by:", opts: ["Ability to pay", "Need", "Planners", "Age"], a: 0, why: "Those with income get the goods." },
  { q: "A weakness of a market economy is:", opts: ["Public goods are not provided", "Competition", "Consumer choice", "Innovation"], a: 0, why: "Market failure." },
  { q: "Profit acts as:", opts: ["An incentive to produce", "A ration", "A tax", "A subsidy"], a: 0, why: "Incentivising function." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Market economy", "Price mechanism, private ownership."],
  ["Rationing", "Limits demand to supply."],
  ["Signalling", "Prices pass information."],
  ["Incentivising", "Profit drives supply."],
  ["What / how / for whom", "Spending, lowest cost, ability to pay."],
  ["Strengths", "Efficiency, choice, innovation."],
  ["Weaknesses", "Public goods, merit goods, inequality, monopoly."],
  ["Reality", "No pure market economy."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "What is not a function of the price mechanism? (May/June 2025 · 11 · Q6, reworded)", opts: ["To act as a signal to firms when allocating resources", "To maximise consumer surplus", "To provide an incentive to firms to produce goods", "To ration scarce resources"], a: 1, why: "Price signals, incentivises and rations. It does not aim to maximise consumer surplus." },
  { q: "Which statement best illustrates the function of price that relies on consumer choice (the incentivising function)? (May/June 2023 · 12 · Q5, reworded)", opts: ["A price fall can show consumers that a good is becoming less popular", "A price fall tends to persuade some producers not to stay in the market for the good", "A price rise means consumers cannot afford to buy so much of a good", "A price rise tends to reduce competitiveness in the market for a good"], a: 1, why: "A lower price and profit give producers an incentive to leave the market, while a higher one attracts them." },
  { q: "Which statement about a market economy is not correct? (Feb/March 2025 · 12 · Q1, reworded)", opts: ["Competition is promoted among firms which can increase productive efficiency", "Immobility of the factors of production can lead to allocative inefficiency", "Price always reflects all the costs and all the benefits associated with production", "The entrepreneur is encouraged to innovate and take risks, motivated by profit"], a: 2, why: "Prices often ignore external costs and benefits, so they do not always reflect all costs and benefits." },
  { q: "When will the price mechanism be least likely to reallocate resources to meet a change in consumer preferences? (Feb/March 2022 · 12 · Q9, reworded)", opts: ["When the government removes all price controls", "When the new preferences are for more public goods", "When the supply of factors of production is limited", "When there is a redistribution of income"], a: 1, why: "Public goods are not provided through the price mechanism, because of free-riding." },
  { q: "What does not happen when price acts as a means to allocate resources? (May/June 2022 · 12 · Q12, reworded)", opts: ["Price determines the supply of public goods", "Price operates in the markets for both goods and factors of production", "Price recognises consumers' ability to pay rather than their needs", "Price signals to producers which goods are most profitable"], a: 0, why: "Public goods are not supplied by the price mechanism. The other three do happen." },
  { q: "What is a major function of the price mechanism? (May/June 2020 · 12 · Q11, reworded)", opts: ["providing incentive for government intervention to reduce income inequality", "removing shortages by creating incentives for market prices to fall", "removing surpluses by creating incentives for market prices to rise", "signalling changes in market conditions to producers and consumers"], a: 3, why: "Signalling is a major function of price. Shortages push prices up and surpluses push them down, so the first three are wrong." },
  { q: "What can be concluded about the roles of demand and supply in a free market? (May/June 2022 · 12 · Q7, reworded)", opts: ["They allocate resources to the greatest needs.", "They ensure that goods and services are distributed equally.", "They are both significant in setting the market price.", "They ensure that everyone can benefit from the good or service provided."], a: 2, why: "Market price is set by the interaction of both demand and supply. Markets respond to ability to pay, not need, and do not distribute equally." },
  { q: "In which case is the price system not a possible method of allocating resources? (Feb/March 2023 · 12 · Q7, reworded)", opts: ["in the distribution of foodstuff among the population", "in the hiring of workers by employers", "in the ownership of land for agricultural use", "in the provision of public goods by the government"], a: 3, why: "Public goods cannot be sold, so the price system cannot allocate them." },
] });
