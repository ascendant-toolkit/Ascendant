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
  o += SV.circle(SDX(e0.q), SDY(e0.p), 5, "dot1", op(mv ? 0.6 : 1)) + sdGuide(e0, "P1", "Q1", g * (mv ? 0.5 : 1));
  if (mv) o += SV.circle(SDX(e1.q), SDY(e1.p), 6, "dot3", op(n)) + sdGuide(e1, "P2", "Q2", g * n);
  return o;
}

/* ---------- three functions ---------- */
function fnDraw(s) {
  const d = 20, p = s.p, qd = d + (90 - p) / 0.8, qs = (p - 10) / 0.8; let o = sdPlot({ d: s.n * d, s: 0, g: 0, n: s.n });
  o += SV.line(70, SDY(p), SDX(Math.max(qd, qs)), SDY(p), "dash") + SV.circle(SDX(qd), SDY(p), 6, "dot2") + SV.circle(SDX(qs), SDY(p), 6, "dot1") + SV.text(62, SDY(p) + 4, "$" + Lib.fmtN(p, 0), "sm", { "text-anchor": "end" });
  if (qd - qs > 1) o += SV.rect(SDX(qs), SDY(p) - 6, SDX(qd) - SDX(qs), 12, "f3", op(0.7)) + tag(SDX(qd) + 10, SDY(p) + 4, "shortage " + Lib.fmtN(qd - qs, 0), "c3");
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="Demand rises, the price rises and the shortage disappears as price rations, signals and incentivises">${fnDraw({ p: 58, n: 1 })}</svg>`;
Lib.stepper($("#stP"), { w: 760, h: 300, label: "Demand rises and the price mechanism responds", base: { p: 50, n: 0 }, draw: fnDraw, tween: 900, dwell: 5800, steps: [
  { cap: "<b>Start.</b> The market is in equilibrium at $50 and 50 units.", s: { p: 50, n: 0 } },
  { cap: "<b>Demand rises.</b> At the old price of $50 buyers want 70 units but firms supply only 50: a <b>shortage</b> of 20.", s: { p: 50, n: 1 } },
  { cap: "<b>Rationing.</b> The price rises to $54. Buyers with a lower willingness to pay drop out, so quantity demanded falls from 70 to 65 while the shortage narrows.", s: { p: 54, n: 1 } },
  { cap: "<b>Signalling and incentivising.</b> At $58 the higher price signals to firms that consumers want more and the higher profit <b>incentivises</b> them to supply 60 units. The market clears.", s: { p: 58, n: 1 } },
] });

/* ---------- price cap ---------- */
function capDraw(s) {
  const p = s.p, qd = (90 - p) / 0.8, qs = Math.max(0, (p - 10) / 0.8); let o = sdPlot({ d: 0, s: 0, g: 0 });
  o += SV.line(70, SDY(p), 720, SDY(p), "c4", { "stroke-width": 2.5, ...op(s.v) }) + tag(724, SDY(p) - 6, "Max price", "c4", s.v, "end");
  if (s.v > 0.2 && qd - qs > 1) o += SV.rect(SDX(qs), SDY(p) - 8, SDX(qd) - SDX(qs), 16, "f3", op(0.7 * s.v)) + SV.circle(SDX(qd), SDY(p), 6, "dot2", op(s.v)) + SV.circle(SDX(qs), SDY(p), 6, "dot1", op(s.v)) + tag(SDX(qd) + 10, SDY(p) + 22, "shortage " + Lib.fmtN(qd - qs, 0), "c3", s.v);
  return o;
}
$("#pic2").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="A maximum price below equilibrium creates a shortage">${capDraw({ p: 35, v: 1 })}</svg>`;
Lib.stepper($("#stM"), { w: 760, h: 300, label: "A maximum price creates a shortage", base: { p: 35, v: 0 }, draw: capDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>Start.</b> The free market clears at $50 and 50 units.", s: { p: 35, v: 0 } },
  { cap: "<b>A maximum price of $35</b> is set below equilibrium. At $35 buyers want 69 units but firms supply only 31: a <b>shortage</b> of 38 units.", s: { p: 35, v: 1 } },
  { cap: "<b>The price can no longer ration or signal.</b> Queues, waiting lists or black markets must ration the goods, and firms lack the incentive to supply more.", s: { p: 35, v: 1 } },
] });

/* ---------- Lab 1 ---------- */
function labF() {
  if (!$("#dm")) return;
  const d = +$("#dm").value, e = sdEq(d, 0), e0 = sdEq(0, 0), dq = (e.q - e0.q) / e0.q * 100, out = Math.max(0, 50 - (90 - e.p) / 0.8);
  $("#r1").textContent = "$" + Lib.fmtN(e.p, 0); $("#r2").textContent = (dq > 0 ? "+" : "") + Lib.fmtN(dq, 0) + "%"; $("#r3").textContent = Lib.fmtN(out, 0);
  $("#rv").textContent = Math.abs(d) < 0.5 ? "Demand has not changed, so the price stays at $50 and nothing needs to adjust." : d > 0 ? `Demand rises, so the price rises to $${Lib.fmtN(e.p, 0)}. That rations the good (${Lib.fmtN(out, 0)} of the original buyers are priced out), signals firms that consumers want more and incentivises them to raise output by ${Lib.fmtN(dq, 0)}%.` : `Demand falls, so the price falls to $${Lib.fmtN(e.p, 0)}. The lower price signals to firms that consumers want less and incentivises them to cut output by ${Lib.fmtN(-dq, 0)}%. No original buyer is priced out.`;
  $("#labA").innerHTML = sdPlot({ d, s: 0, g: 1, n: 1 });
}
Lib.slider($("#g1"), { id: "dm", label: "Demand shift (negative = fall, positive = rise) ", min: -30, max: 30, step: 5, value: 20, fmt: (v) => v, onInput: labF });
labF();

/* ---------- Lab 2 ---------- */
function labC() {
  if (!$("#cp")) return;
  const p = +$("#cp").value, qd = (90 - p) / 0.8, qs = Math.max(0, (p - 10) / 0.8), eff = p < 50, sh = eff ? qd - qs : 0;
  $("#t1").textContent = Lib.fmtN(eff ? qd : 50, 0); $("#t2").textContent = Lib.fmtN(eff ? qs : 50, 0); $("#t3").textContent = Lib.fmtN(sh, 0);
  $("#tv").textContent = eff ? `A maximum price of $${p} is below the equilibrium of $50, so it is effective. Buyers want ${Lib.fmtN(qd, 0)} units but firms supply only ${Lib.fmtN(qs, 0)}, a shortage of ${Lib.fmtN(sh, 0)}. Price can no longer ration, so queues, coupons or black markets must.` : `A maximum price of $${p} is at or above the equilibrium of $50, so it has no effect: the market still clears at $50 and 50 units.`;
  let o = sdPlot({ d: 0, s: 0, g: 0 }) + SV.line(70, SDY(p), 720, SDY(p), "c4", { "stroke-width": 2.5 }) + tag(724, SDY(p) - 6, "Max price $" + p, "c4", 1, "end");
  if (eff) o += SV.rect(SDX(qs), SDY(p) - 8, SDX(qd) - SDX(qs), 16, "f3", op(0.7)) + SV.circle(SDX(qd), SDY(p), 6, "dot2") + SV.circle(SDX(qs), SDY(p), 6, "dot1");
  $("#labB").innerHTML = o;
}
Lib.slider($("#g2"), { id: "cp", label: "Maximum price, $ ", min: 20, max: 70, step: 5, value: 35, fmt: (v) => "$" + v, onInput: labC });
labC();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Which function of price is it?", buckets: [{"label": "Rationing"}, {"label": "Signalling"}, {"label": "Incentivising"}], items: [{"text": "A higher price for concert tickets means only those willing to pay can buy", "b": 0}, {"text": "A rising price tells farmers that consumers want more wheat", "b": 1}, {"text": "Higher profits attract new firms into the solar panel market", "b": 2}, {"text": "A price fall tells firms that demand has fallen", "b": 1}, {"text": "A crop failure raises the price, so people buy less", "b": 0}, {"text": "A rising wage encourages students to train as engineers", "b": 2}, {"text": "Dearer petrol pushes drivers to switch to public transport", "b": 2}, {"text": "Rising house prices show a city has a shortage of homes", "b": 1}], done: "Rationing reduces demand to match supply. Signalling gives information. Incentivising rewards or discourages action." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Rationing", "Price reduces quantity demanded to match scarce supply"], ["Signalling", "Price tells producers and consumers about changes in the market"], ["Incentivising", "Price changes reward or discourage production and consumption"], ["Transmission of preferences", "Consumers' wishes are communicated to producers through price"], ["Maximum price", "Prevents price from rationing, causing a shortage"], ["Price mechanism", "Allocation of resources through the interaction of demand and supply"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the price mechanism chain in order.", items: ["Consumer demand for a good rises", "A shortage appears at the old price", "The price rises", "Producers see the signal and higher profit and raise output", "A new equilibrium is reached with a higher price and quantity"], done: "Demand leads to a shortage, then price, then supply responds." });
Lib.calc($("#c1"), { qs: [
  {"q": "The price rises from $50 to $58. What is the % rise?", "a": 16, "unit": "%", "tol": 0.5, "hint": "(58 − 50) ÷ 50.", "sol": "<b>16%</b>."},
  {"q": "Qd = 140 − 2P and Qs = 3P − 10. What is the equilibrium price ($)?", "a": 30, "unit": "$", "tol": 0.5, "hint": "140 − 2P = 3P − 10.", "sol": "150 = 5P, so P = <b>$30</b>."},
  {"q": "A maximum price of $20 is set on the market above. What is the shortage (units)?", "a": 50, "unit": "units", "tol": 0.5, "hint": "Qd = 100, Qs = 50.", "sol": "Qd = 140 − 40 = 100 and Qs = 60 − 10 = 50, so the shortage is <b>50</b>."},
  {"q": "In the same market the price rises from $30 to $33. Quantity supplied rises from 80 to 89. What is the % rise in quantity supplied?", "a": 11.25, "unit": "%", "tol": 0.3, "hint": "9 ÷ 80.", "sol": "<b>11.25%</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A higher price reduces demand until it matches supply. This is the function of:", opts: ["Rationing", "Signalling", "Incentivising", "Redistribution"], a: 0, why: "Rationing." },
  { q: "Rising prices telling firms that consumers want more is:", opts: ["Signalling", "Rationing", "Taxation", "Direct provision"], a: 0, why: "Signalling or transmission of preferences." },
  { q: "Higher profits attracting new firms is:", opts: ["Incentivising", "Rationing", "Signalling to consumers", "Price fixing"], a: 0, why: "Incentive to supply." },
  { q: "An effective maximum price will:", opts: ["Create a shortage", "Create a surplus", "Raise quantity supplied", "Have no effect"], a: 0, why: "Below equilibrium." },
  { q: "Which good cannot be allocated through the price mechanism?", opts: ["A public good", "Bread", "A haircut", "A car"], a: 0, why: "Non-excludable." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Rationing", "Price limits demand to scarce supply."],
  ["Signalling", "Price tells firms what consumers want."],
  ["Incentivising", "Profit encourages production."],
  ["Max price", "Shortage and no signal."],
  ["Public good", "Price mechanism fails."],
  ["Factor markets", "Wages signal and incentivise too."],
  ["Mixed economy", "Mainly markets, plus government."],
  ["Limits", "Ability to pay, externalities, information."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "What is a major function of the price mechanism? (May/June 2020 · 12 · Q11, reworded)", opts: ["providing incentive for government intervention to reduce income inequality", "removing shortages by creating incentives for market prices to fall", "removing surpluses by creating incentives for market prices to rise", "signalling changes in market conditions to producers and consumers"], a: 3, why: "Signalling is a main function. Shortages are removed by prices rising and surpluses by prices falling." },
  { q: "When demand for a good falls, its price falls. What is the function of the price fall? (Oct/Nov 2020 · 12 · Q12, reworded)", opts: ["to eliminate shortages", "to reduce consumer surplus", "to send a signal to producers", "to stimulate a further fall in demand"], a: 2, why: "A falling price tells producers that demand has fallen." },
  { q: "What is not a function of the price mechanism? (May/June 2025 · 11 · Q6, reworded)", opts: ["to act as a signal to firms when allocating resources", "to maximise consumer surplus", "to provide an incentive to firms to produce goods", "to ration scarce resources"], a: 1, why: "The three functions are signalling, incentivising and rationing. Maximising consumer surplus is not one." },
  { q: "Price plays a number of functions in the allocation of resources. Which statement best illustrates the function that relies upon consumer choice (sometimes known as the incentivising function)? (May/June 2023 · 12 · Q5, reworded)", opts: ["A price fall can show consumers that a good is becoming less popular", "A price fall tends to persuade some producers not to stay in the market for the good", "A price rise means consumers cannot afford to buy so much of a good", "A price rise tends to reduce competitiveness in the market for a good"], a: 1, why: "The incentivising function means price changes reward or discourage producers, here pushing some to leave the market." },
  { q: "What does not happen when price acts as a means to allocate resources? (May/June 2022 · 12 · Q12, reworded)", opts: ["Price determines the supply of public goods", "Price operates in the markets for both goods and factors of production", "Price recognises consumers' ability to pay rather than consumers' needs", "Price signals to producers which goods are most profitable"], a: 0, why: "Public goods are not supplied through the price mechanism." },
  { q: "When will it not be possible to use price as a rationing mechanism? (May/June 2021 · 11 · Q6, reworded)", opts: ["when a good has a number of close substitutes", "when a good is an inferior good", "when the demand for a good is perfectly inelastic", "when the quantity of a good is in fixed supply"], a: 2, why: "If demand is perfectly inelastic, a price rise does not reduce quantity demanded, so price cannot ration." },
  { q: "When will the price mechanism not function as a system for allocating goods? (May/June 2022 · 11 · Q11, reworded)", opts: ["when the government bans advertising", "when the government maintains an effective maximum price", "when there is a limited supply of the good", "when there is a powerful company able to set the market price"], a: 1, why: "An effective maximum price stops price from adjusting to clear the market." },
  { q: "After a series of poor harvests, a government imposes an effective maximum price on cereals. What would be a consequence of this policy? (Feb/March 2021 · 12 · Q14, reworded)", opts: ["Both rich and poor people would satisfy their demands equally", "Illegal buying and selling through a black market would be prevented", "Rationing would be necessary to ensure a fair distribution of cereals", "The market would fail to clear leaving a surplus of cereals"], a: 2, why: "A price cap below equilibrium causes a shortage, so rationing by other means is needed." },
  { q: "When will the price mechanism be least likely to reallocate resources to meet a change in consumer preferences? (Feb/March 2022 · 12 · Q9, reworded)", opts: ["when the government removes all price controls", "when the new preferences are for more public goods", "when the supply of factors of production is limited", "when there is a redistribution of income"], a: 1, why: "Public goods cannot be supplied through prices." },
  { q: "In which case is the price system not a possible method of allocating resources? (Feb/March 2023 · 12 · Q7, reworded)", opts: ["in the distribution of foodstuff among the population", "in the hiring of workers by employers", "in the ownership of land for agricultural use", "in the provision of public goods by the government"], a: 3, why: "Public goods are non-excludable, so prices cannot allocate them." },
  { q: "What is necessary to achieve the best allocation of resources using the price mechanism? (May/June 2022 · 13 · Q9, reworded)", opts: ["Producers can maximise their collective interest", "Consumers and producers must have perfect knowledge", "The government must be able to apply maximum and minimum prices", "The value of the price elasticity of supply must be greater than one"], a: 1, why: "Correct signals need good information." },
  { q: "What can be concluded about the roles of demand and supply in a free market? (May/June 2022 · 12 · Q7, reworded)", opts: ["They allocate resources to the greatest needs", "They ensure that goods and services are distributed equally", "They are both significant in setting the market price", "They ensure that everyone can benefit from the good or service provided"], a: 2, why: "Price comes from the interaction of both demand and supply. The market allocates by ability to pay, not by need." },
] });
