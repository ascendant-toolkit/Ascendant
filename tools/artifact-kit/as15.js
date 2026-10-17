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

/* ---------- spectrum ---------- */
function spDraw(s) {
  let o = SV.rect(70, 100, 620, 36, "f1", op(0.25)) + SV.rect(70, 100, 620 * s.w, 36, "f3", op(0.55)); o += SV.text(70, 90, "Pure market", "lbl bd") + SV.text(690, 90, "Pure planned", "lbl bd", { "text-anchor": "end" });
  const m = (x, t, sub, k) => (k > 0 ? SV.line(x, 96, x, 150, "c1", { "stroke-width": 2.4, ...op(k) }) + SV.circle(x, 118, 9, "dot4", op(k)) + SV.text(x, 176, t, "lbl bd", { "text-anchor": x < 100 ? "start" : x > 650 ? "end" : "middle", ...op(k) }) + SV.text(x, 194, sub, "sm", { "text-anchor": x < 100 ? "start" : x > 650 ? "end" : "middle", ...op(k) }) : "");
  o += m(70, "Market economy", "prices and private firms decide", s.a) + m(380, "Mixed economies", "both decide; the mix varies", s.b) + m(690, "Planned economy", "the state decides", s.c);
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 230" role="img" aria-label="Spectrum from a pure market economy through mixed economies to a pure planned economy">${spDraw({ w: 0.5, a: 1, b: 1, c: 1 })}</svg>`;
Lib.stepper($("#stS"), { w: 760, h: 230, label: "The spectrum of economic systems", base: { w: 0, a: 0, b: 0, c: 0 }, draw: spDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>Market economy.</b> Prices set by demand and supply allocate resources. Firms are private and the government does little.", s: { w: 0, a: 1 } },
  { cap: "<b>Planned economy.</b> The government decides what, how and for whom to produce and usually owns the factors of production.", s: { w: 1, a: 1, c: 1 } },
  { cap: "<b>Mixed economies.</b> In between, markets allocate most goods, while the government provides public goods and corrects market failure. Where an economy sits on the line shows <b>how mixed</b> it is.", s: { w: 0.5, a: 1, b: 1, c: 1 } },
] });

/* ---------- price signals ---------- */
const PX = (q) => 70 + q * 6, PY = (p) => 290 - p * 3.4;
function prDraw(s) {
  const dsh = 18 * s.d; let o = SV.line(70, 290, 700, 290) + SV.line(70, 290, 70, 30) + SV.text(700, 316, "Quantity", "sm", { "text-anchor": "end" }) + SV.text(76, 24, "Price", "sm");
  const D = (sh) => [[PX(0 + sh), PY(80)], [PX(80 + sh), PY(0)]], Sl = [[PX(0), PY(0)], [PX(80), PY(80)]];
  if (s.d > 0) o += SV.line(...D(0)[0], ...D(0)[1], "c1 dash", op(0.45));
  o += SV.line(...D(dsh)[0], ...D(dsh)[1], "c1") + SV.line(...Sl[0], ...Sl[1], "c3") + tag(PX(78) + 6, PY(2), "D", "t1", 1, "start") + tag(PX(80), PY(80) - 6, "S", "t3", 1, "end");
  const q = 40 + dsh / 2, p = 40 + dsh / 2; o += SV.circle(PX(q), PY(p), 7, "dot4") + tag(PX(q) + 10, PY(p) + 20, "price " + Lib.fmtN(p, 0), "t4");
  if (s.l > 0) o += tag(PX(10), PY(75), "Rationing: price limits demand", "t2", s.l);
  if (s.l > 1) o += tag(PX(10), PY(68), "Signal: consumers want more", "t1", Math.min(1, s.l - 1));
  if (s.l > 2) o += tag(PX(10), PY(61), "Incentive: producers expand output", "t3", Math.min(1, s.l - 2));
  return o;
}
Lib.stepper($("#stP"), { w: 760, h: 330, label: "A rise in demand raises the price, which rations, signals and gives producers an incentive", base: { d: 0, l: 0 }, draw: prDraw, tween: 1100, dwell: 5800, steps: [
  { cap: "<b>Equilibrium.</b> Demand and supply meet at a price of 40.", s: { d: 0, l: 0 } },
  { cap: "<b>Demand rises</b> (a new fashion). Without any government order, the price rises to about 49.", s: { d: 1, l: 0 } },
  { cap: "<b>Rationing.</b> The higher price limits demand to the amount available: those who value the good least drop out.", s: { d: 1, l: 1 } },
  { cap: "<b>Signalling.</b> The price rise tells producers that consumers want more of this good.", s: { d: 1, l: 2 } },
  { cap: "<b>Incentive.</b> Higher profits encourage firms to expand supply and attract new firms, so resources move into the industry.", s: { d: 1, l: 3 } },
] });

/* ---------- Lab 1 ---------- */
function labM() {
  if (!$("#dd") || !$("#ss")) return;
  const d = +$("#dd").value, s = +$("#ss").value, q = 40 + (d - s) / 2 * 1, p = 40 + (d + s) * 0 + (d - s) / 2;
  const P2 = 40 + (d + (-s)) / 2 * 1, Q2 = 40 + (d + s) / 2;
  const peq = 40 + (d - s) * 0.5 * 1, qeq = 40 + (d + s) * 0.5 * 1;
  $("#r1").textContent = Lib.fmtN(peq, 0); $("#r2").textContent = Lib.fmtN(qeq, 0); $("#r3").textContent = d - s > 2 ? "Produce more" : d - s < -2 ? "Produce less" : "No change";
  $("#rv").textContent = `Demand has shifted by ${d} and supply by ${s}. The new price is ${Lib.fmtN(peq, 0)} and the quantity ${Lib.fmtN(qeq, 0)}. ${d - s > 2 ? "The price has risen, which rations demand and signals firms to produce more." : d - s < -2 ? "The price has fallen, which signals firms to produce less." : "Price is about the same, so there is little signal to change output."}`;
  const X = (v) => 40 + v * 3.2, Y = (v) => 270 - v * 3.0; let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 30) + SV.text(400, 292, "Quantity", "sm", { "text-anchor": "end" }) + SV.text(46, 22, "Price", "sm");
  o += SV.line(X(0 + d), Y(80), X(80 + d), Y(0), "c1") + SV.line(X(0 + s), Y(0), X(80 + s), Y(80), "c3") + SV.circle(X(qeq), Y(peq), 7, "dot4") + tag(X(qeq) + 10, Y(peq) + 18, "P " + Lib.fmtN(peq, 0) + ", Q " + Lib.fmtN(qeq, 0), "t4");
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "dd", label: "Change in demand (shift right +) ", min: -20, max: 20, step: 2, value: 10, fmt: (v) => v, onInput: labM });
Lib.slider($("#g2"), { id: "ss", label: "Change in supply (shift right +) ", min: -20, max: 20, step: 2, value: 0, fmt: (v) => v, onInput: labM });
labM();

/* ---------- Lab 2 ---------- */
function labY() {
  if (!$("#so") || !$("#pcn") || !$("#gs")) return;
  const so = +$("#so").value, pcn = +$("#pcn").value, gs = +$("#gs").value, sc = (so * 0.4 + pcn * 0.3 + gs * 0.3);
  $("#t1").textContent = Lib.fmtN(sc, 0); const sys = sc < 15 ? "Market economy" : sc < 40 ? "Mostly market, mixed" : sc < 65 ? "Mixed economy" : sc < 85 ? "Mostly planned, mixed" : "Planned economy";
  $("#t2").textContent = sys; $("#t3").textContent = sc < 15 ? "Prices and firms" : sc < 65 ? "Prices and government" : "The state";
  $("#tv").textContent = `With ${so}% of production state-owned, ${pcn}% of prices controlled and government spending at ${gs}% of the economy's output, the score is ${Lib.fmtN(sc, 0)}: a ${sys.toLowerCase()}. This weights state ownership at 40% and the other two at 30% each, which is a simple teaching rule, not an official index. Real economies differ in how mixed they are, and the answer to 'what, how and for whom' lies between the two extremes.`;
  let o = SV.rect(40, 120, 340, 40, "f1", op(0.25)) + SV.rect(40, 120, 340 * sc / 100, 40, "f3", op(0.6)) + SV.text(40, 108, "Market", "lbl bd") + SV.text(380, 108, "Planned", "lbl bd", { "text-anchor": "end" }) + SV.circle(40 + 340 * sc / 100, 140, 9, "dot4") + tag(40 + 340 * sc / 100, 190, Lib.fmtN(sc, 0), "t4", 1, "middle");
  $("#labB").innerHTML = o;
}
Lib.slider($("#g3"), { id: "so", label: "State-owned share of production, % ", min: 0, max: 100, step: 5, value: 25, fmt: (v) => v + "%", onInput: labY });
Lib.slider($("#g4"), { id: "pcn", label: "Prices set or controlled by the government, % ", min: 0, max: 100, step: 5, value: 15, fmt: (v) => v + "%", onInput: labY });
Lib.slider($("#g5"), { id: "gs", label: "Government spending, % of output ", min: 10, max: 100, step: 5, value: 40, fmt: (v) => v + "%", onInput: labY });
labY();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Which system does it describe?", buckets: [{"label": "Market"}, {"label": "Planned"}, {"label": "Mixed"}], items: [{"text": "Prices set by demand and supply allocate most resources", "b": 0}, {"text": "A central authority sets output targets for each industry", "b": 1}, {"text": "Private firms sell most goods, but the government provides defence and public education", "b": 2}, {"text": "Resources go to those with the ability to pay", "b": 0}, {"text": "Factors of production are mostly state-owned", "b": 1}, {"text": "Governments tax demerit goods and subsidise merit goods", "b": 2}, {"text": "Firms decide what to produce to make a profit", "b": 0}, {"text": "Planners may fail to match output to what consumers want", "b": 1}], done: "Market: prices decide. Planned: the state decides. Mixed: both." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Rationing", "Price limits demand to the amount available"], ["Signalling", "Price passes information on consumers' preferences to firms"], ["Incentivising", "Profit and price changes encourage firms to produce more or less"], ["Command economy", "The government makes the main economic decisions"], ["Mixed economy", "Prices and government both allocate resources"], ["Consumer sovereignty", "Consumers' spending decides what is produced"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the price signal in order.", items: ["Consumers want more of a good", "Demand rises and the price rises", "Producers see higher profit", "Firms expand output and new firms enter", "Resources move into the industry"], done: "Price rises signal, ration and incentivise." });
Lib.calc($("#c1"), { qs: [
  {"q": "A government spends $450bn and the economy's output is $1,500bn. What share of output is government spending (%)?", "a": 30, "unit": "%", "tol": 0.5, "hint": "450 ÷ 1,500.", "sol": "<b>30%</b>."},
  {"q": "The price of a product rises from $40 to $48. Calculate the percentage change (%).", "a": 20, "unit": "%", "tol": 0.5, "hint": "8 ÷ 40.", "sol": "<b>20%</b>."},
  {"q": "State-owned firms produce $300bn of an economy's $1,200bn output. What share is state-owned (%)?", "a": 25, "unit": "%", "tol": 0.5, "hint": "300 ÷ 1,200.", "sol": "<b>25%</b>."},
  {"q": "A planner sets a maximum price of $5 when demand is 120 and supply is 80 at that price. What is the shortage (units)?", "a": 40, "unit": "units", "tol": 0.5, "hint": "120 − 80.", "sol": "<b>40 units</b>: planners without price signals can produce shortages."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "In a market economy, what mainly decides what is produced?", opts: ["Consumers' spending and firms' profit", "A central planning body", "The government budget", "Trade unions"], a: 0, why: "Demand and supply, through prices." },
  { q: "Which is a weakness of a planned economy?", opts: ["Lack of price signals and incentives", "Too much consumer choice", "Excessive competition", "No provision of public goods"], a: 0, why: "Without prices planners lack information and workers lack incentives." },
  { q: "A mixed economy usually has:", opts: ["Both markets and government provision", "No private firms", "No government", "Only public goods"], a: 0, why: "It combines the price mechanism with a role for government." },
  { q: "The signalling function of price means that:", opts: ["Prices tell producers what consumers want", "Prices are fixed by the state", "Prices ration goods by queue", "Prices show costs only"], a: 0, why: "A price rise signals that more is wanted." },
  { q: "Which is least likely after a move from planning to a market economy?", opts: ["Provision of merit goods rises", "Prices of goods rise", "Private ownership grows", "Some workers become unemployed"], a: 0, why: "Markets tend to under-provide merit goods." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Market economy", "Price mechanism and private firms decide."],
  ["Planned economy", "Government decides what, how, for whom."],
  ["Mixed economy", "Both; most real economies."],
  ["Functions of price", "Rationing, signalling, incentivising."],
  ["Market failure", "Public goods, merit/demerit goods, externalities."],
  ["Planned weakness", "No price signals; poor incentives."],
  ["Transition", "Planned to market: prices up, unemployment, inequality."],
  ["How mixed?", "Depends on state ownership, spending, regulation."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "In a planned economy, what will determine the allocation of scarce resources? (Oct/Nov 2022 · 12 · Q2, reworded)", opts: ["A mixture of private and central decision making", "The decisions of central government", "The forces of demand and supply", "The revenue generated from direct and indirect taxes"], a: 1, why: "In a planned economy the state decides, not the market." },
  { q: "What is the main characteristic of a planned economy? (May/June 2022 · 12 · Q2, reworded)", opts: ["All goods and services are produced by privately-owned firms", "All goods and services are produced by state-owned firms", "Private firms produce private goods and state firms produce public goods", "The price mechanism allocates scarce resources through buyers and sellers"], a: 1, why: "State ownership and state decision making are the main characteristics. Option C describes a mixed economy and D a market economy." },
  { q: "What is not a function of the price mechanism? (May/June 2025 · 11 · Q6, reworded)", opts: ["To act as a signal to firms when allocating resources", "To maximise consumer surplus", "To provide an incentive to firms to produce goods", "To ration scarce resources"], a: 1, why: "Price signals, incentivises and rations. It does not aim to maximise consumer surplus." },
  { q: "Which statement best illustrates the function of price that relies on consumer choice (the incentivising function)? (May/June 2023 · 12 · Q5, reworded)", opts: ["A price fall can show consumers that a good is becoming less popular", "A price fall tends to persuade some producers not to stay in the market for the good", "A price rise means consumers cannot afford to buy so much of a good", "A price rise tends to reduce competitiveness in the market for a good"], a: 1, why: "A lower price and profit give producers an incentive to leave the market, while a higher one attracts them." },
  { q: "Which statement about a market economy is not correct? (Feb/March 2025 · 12 · Q1, reworded)", opts: ["Competition is promoted among firms which can increase productive efficiency", "Immobility of the factors of production can lead to allocative inefficiency", "Price always reflects all the costs and all the benefits associated with production", "The entrepreneur is encouraged to innovate and take risks, motivated by profit"], a: 2, why: "Prices often ignore external costs and benefits, so they do not always reflect all costs and benefits." },
  { q: "What is least likely to increase as a result of a transition from a planned economy to a free market economy? (Oct/Nov 2023 · 11 · Q4, reworded)", opts: ["Prices of goods and services", "Privately owned resources", "Provision of merit goods", "Structural unemployment"], a: 2, why: "A free market tends to under-provide merit goods; prices, private ownership and structural unemployment are likely to rise." },
  { q: "When will the price mechanism be least likely to reallocate resources to meet a change in consumer preferences? (Feb/March 2022 · 12 · Q9, reworded)", opts: ["When the government removes all price controls", "When the new preferences are for more public goods", "When the supply of factors of production is limited", "When there is a redistribution of income"], a: 1, why: "Public goods are not provided through the price mechanism, because of free-riding." },
  { q: "What does not happen when price acts as a means to allocate resources? (May/June 2022 · 12 · Q12, reworded)", opts: ["Price determines the supply of public goods", "Price operates in the markets for both goods and factors of production", "Price recognises consumers' ability to pay rather than their needs", "Price signals to producers which goods are most profitable"], a: 0, why: "Public goods are not supplied by the price mechanism. The other three do happen." },
  { q: "What is the main reason an economy is unlikely to rely completely on market forces to allocate resources? (Feb/March 2024 · 12 · Q4, reworded)", opts: ["Demerit goods will be over supplied", "Merit goods will be under supplied", "Private goods will not be supplied", "Public goods will not be supplied"], a: 3, why: "Public goods would not be provided at all in a pure market, which is the most serious failure." },
  { q: "What is produced in a mixed economy but not in a free market economy? (May/June 2024 · 12 · Q2, reworded)", opts: ["Demerit goods", "Free goods", "Private goods", "Public goods"], a: 3, why: "Governments provide public goods in a mixed economy; a free market would not supply them." },
] });
