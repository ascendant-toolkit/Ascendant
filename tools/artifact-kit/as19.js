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

/* ---------- merit: demand below social benefit ---------- */
function meritDraw(s) {
  let o = SV.line(60, 270, 700, 270) + SV.line(60, 270, 60, 30) + SV.text(66, 24, "Price ($)", "sm") + SV.text(700, 288, "Quantity", "sm", { "text-anchor": "end" });
  o += SV.line(60, 70, 640, 250, "c1") + SV.text(646, 256, "Supply", "lbl bd c1");
  o += SV.line(80, 210, 560, 70, "c2") + SV.text(562, 66, "Demand (private benefit)", "lbl bd c2");
  if (s.a > 0) o += SV.line(80, 150, 560, 30, "c3", op(s.a)) + SV.text(566, 30, "Marginal social benefit", "lbl bd c3", op(s.a));
  o += SV.circle(360, 157, 5, "dot2");
  if (s.b > 0) o += SV.line(360, 157, 360, 270, "dash", op(s.b)) + SV.text(360, 286, "Q market", "sm", { "text-anchor": "middle", ...op(s.b) });
  if (s.c > 0) o += SV.line(440, 127, 440, 270, "dash", op(s.c)) + SV.text(440, 286, "Q best", "sm", { "text-anchor": "middle", ...op(s.c) }) + SV.line(362, 262, 428, 262, "c4", op(s.c)) + SV.arrowHead(440, 262, "r", "dot4") + SV.text(400, 252, "under-consumed", "sm", { "text-anchor": "middle", ...op(s.c) });
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="A merit good: social benefit above private demand, so the market quantity is below the best quantity">${meritDraw({ a: 1, b: 1, c: 1 })}</svg>`;
Lib.stepper($("#stM"), { w: 760, h: 300, label: "Demand, social benefit and supply for a merit good", base: { a: 0, b: 0, c: 0 }, draw: meritDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>The free market.</b> Consumers value the good by what they understand of its benefit, so demand reflects only the <b>private benefit</b>. Supply and demand meet at the market quantity.", s: { b: 1 } },
  { cap: "<b>The true benefit.</b> The benefit to society is higher than consumers realise (information failure, positive externalities), so the <b>marginal social benefit</b> curve lies above demand.", s: { a: 1, b: 1 } },
  { cap: "<b>Under-consumption.</b> The best quantity is to the right of the market quantity. The market fails to provide enough, so the government may subsidise, regulate or provide the good.", s: { a: 1, b: 1, c: 1 } },
] });

/* ---------- demerit tax ---------- */
function demDraw(s) {
  let o = SV.line(60, 270, 700, 270) + SV.line(60, 270, 60, 30) + SV.text(66, 24, "Price ($)", "sm") + SV.text(700, 288, "Quantity", "sm", { "text-anchor": "end" });
  o += SV.line(80, 230, 620, 60, "c2") + SV.text(626, 64, "Demand", "lbl bd c2");
  o += SV.line(80, 90, 620, 220, "c1") + SV.text(626, 224, "S", "lbl bd c1");
  const dy = -s.t * 45;
  if (s.t > 0) o += SV.line(80, 90 + dy, 620, 220 + dy, "c3", op(s.t)) + SV.text(626, 220 + dy, "S + tax", "lbl bd c3", op(s.t));
  o += SV.circle(380, 156, 5, "dot2") + SV.line(380, 156, 380, 270, "dash") + SV.text(380, 286, "Q1", "sm", { "text-anchor": "middle" });
  if (s.t > 0) o += SV.circle(332, 156 + dy + 30, 5, "dot3", op(s.t)) + SV.line(332, 186 + dy, 332, 270, "dash", op(s.t)) + SV.text(332, 286, "Q2", "sm", { "text-anchor": "middle", ...op(s.t) });
  return o;
}
$("#pic2").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="A tax shifts supply left on a demerit good so quantity falls from Q1 to Q2">${demDraw({ t: 1 })}</svg>`;
Lib.stepper($("#stD"), { w: 760, h: 300, label: "A tax on a demerit good shifts supply to the left", base: { t: 0 }, draw: demDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>Over-consumption.</b> Because consumers underestimate the harm, the market quantity Q1 is higher than the best level for society.", s: { t: 0 } },
  { cap: "<b>The tax.</b> An indirect tax raises producers' costs, so supply shifts to the left. The price rises and the quantity falls to Q2, closer to the best level.", s: { t: 1 } },
] });

/* ---------- Lab 1 ---------- */
function labM() {
  if (!$("#aw") || !$("#sb")) return;
  const aw = +$("#aw").value / 100, sb = +$("#sb").value, qm = 100 * aw, qb = Math.min(160, qm + sb), gap = qb - qm;
  $("#r1").textContent = Lib.fmtN(qm, 0); $("#r2").textContent = Lib.fmtN(qb, 0); $("#r3").textContent = Lib.fmtN(gap, 0);
  $("#rv").textContent = gap <= 0.5 ? "Consumers understand the full benefit, so the free market output is the best one and there is no under-consumption." : `Consumers recognise only ${Lib.fmtN(aw * 100, 0)}% of the benefit, so the market supplies ${Lib.fmtN(qm, 0)} units but ${Lib.fmtN(qb, 0)} is best. This under-consumption of ${Lib.fmtN(gap, 0)} units is why governments subsidise, provide or promote merit goods.`;
  const X = (v) => 40 + v * 2.2; let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 30);
  o += SV.line(X(0), 250, X(160), 70, "c1") + SV.line(X(0), 80, X(160), 230, "c2");
  o += SV.line(X(qm), 270, X(qm), 150, "dash") + SV.line(X(qb), 270, X(qb), 150, "dash", { style: "stroke:var(--good)" }) + SV.text(X(qm), 288, "Market " + Lib.fmtN(qm, 0), "sm", { "text-anchor": "middle" }) + SV.text(X(qb), 288, "Best " + Lib.fmtN(qb, 0), "sm", { "text-anchor": "middle", style: "fill:var(--good)" });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "aw", label: "Share of the benefit consumers understand, % ", min: 20, max: 100, step: 5, value: 50, fmt: (v) => v + "%", onInput: labM });
Lib.slider($("#g2"), { id: "sb", label: "Extra output society would want, units ", min: 0, max: 60, step: 5, value: 30, fmt: (v) => v, onInput: labM });
labM();

/* ---------- Lab 2 ---------- */
function labT() {
  if (!$("#tx") || !$("#el")) return;
  const t = +$("#tx").value, el = +$("#el").value / 10, p0 = 10, q0 = 100, p1 = p0 + t, dq = -el * (t / p0) * q0, q1 = Math.max(0, q0 + dq), fall = q0 - q1, rev = q1 * t;
  $("#t1").textContent = Lib.fmtN(q1, 0); $("#t2").textContent = Lib.fmtN(fall, 0) + " units (" + Lib.fmtN(fall / q0 * 100, 0) + "%)"; $("#t3").textContent = "$" + Lib.fmtN(rev, 0);
  $("#tv").textContent = `A $${t} tax raises the price from $${p0} to $${p1} (all passed on, to keep it simple). With price elasticity of demand of ${Lib.fmtN(el, 1)}, quantity falls by ${Lib.fmtN(fall / q0 * 100, 0)}%, and the government collects $${Lib.fmtN(rev, 0)}. ${el < 1 ? "Demand is inelastic, so the tax reduces consumption by less than the price rise, but raises plenty of revenue." : "Demand is elastic, so consumption falls by more, so the tax is more effective at cutting use but raises less revenue."}`;
  const X = (v) => 40 + v * 3, Y = (v) => 270 - v * 10; let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 30);
  o += SV.line(X(0), Y(14), X(110), Y(2), "c2") + SV.line(X(0), Y(3), X(110), Y(15), "c1") + SV.line(X(0), Y(3 + t), X(110), Y(15 + t), "c3");
  o += SV.circle(X(q0), Y(p0), 5, "dot2") + SV.circle(X(q1), Y(p1), 5, "dot3") + SV.line(X(q1), Y(p1), X(q1), 270, "dash");
  $("#labB").innerHTML = o;
}
Lib.slider($("#g3"), { id: "tx", label: "Tax per unit, $ ", min: 0, max: 5, step: 1, value: 2, fmt: (v) => "$" + v, onInput: labT });
Lib.slider($("#g4"), { id: "el", label: "Price elasticity of demand (×10) ", min: 2, max: 20, step: 1, value: 5, fmt: (v) => (v / 10).toFixed(1), onInput: labT });
labT();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Merit good, demerit good or neither?", buckets: [{"label": "Merit good"}, {"label": "Demerit good"}, {"label": "Neither"}], items: [{"text": "Vaccination", "b": 0}, {"text": "Cigarettes", "b": 1}, {"text": "A loaf of bread", "b": 2}, {"text": "Education", "b": 0}, {"text": "Sugary drinks", "b": 1}, {"text": "Health check-ups", "b": 0}, {"text": "A haircut", "b": 2}, {"text": "Gambling", "b": 1}], done: "Merit: under-consumed. Demerit: over-consumed. Both come from information failure." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Merit good", "Under-consumed because consumers undervalue the benefit"], ["Demerit good", "Over-consumed because consumers underestimate the harm"], ["Information failure", "Consumers lack or misjudge relevant information"], ["Subsidy", "Payment to producers that lowers price and raises consumption"], ["Indirect tax", "Raises cost of production and cuts consumption"], ["Minimum price", "Price floor above the equilibrium"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the case for taxing a demerit good in order.", items: ["Consumers underestimate the harm of the good", "Demand is too high, so output and consumption are too high", "The government imposes an indirect tax", "Supply shifts left, the price rises and quantity falls", "Consumption is closer to the best level for society"], done: "Information failure leads to over-consumption, and a tax moves it back." });
Lib.calc($("#c1"), { qs: [
  {"q": "A good is sold at $10 and 100 units are sold. A tax of $2 is passed on to consumers and quantity falls to 90. What is the tax revenue ($)?", "a": 180, "unit": "$", "tol": 1, "hint": "Tax per unit × quantity after tax.", "sol": "2 × 90 = <b>$180</b>."},
  {"q": "In the same example, what is the percentage fall in quantity?", "a": 10, "unit": "%", "tol": 0.2, "hint": "(100 − 90) ÷ 100.", "sol": "<b>10%</b>."},
  {"q": "Price rises from $10 to $12. What is the price elasticity of demand (ignore the minus sign)?", "a": 0.5, "unit": "", "tol": 0.02, "hint": "% change in quantity ÷ % change in price: 10 ÷ 20.", "sol": "10% ÷ 20% = <b>0.5</b>, inelastic."},
  {"q": "A subsidy of $3 per unit lowers a merit good's price from $15 to $12. Quantity rises from 200 to 260. What is the new total subsidy cost ($)?", "a": 780, "unit": "$", "tol": 1, "hint": "3 × 260.", "sol": "3 × 260 = <b>$780</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A merit good is best described as one that is:", opts: ["Under-consumed because its benefits are not fully understood", "Over-consumed because its harm is underestimated", "Non-rival and non-excludable", "Always provided by the government"], a: 0, why: "Information failure leads to under-consumption." },
  { q: "A demerit good is one that is:", opts: ["Over-consumed because the harm is underestimated", "Under-consumed because its benefits are not understood", "Not scarce", "Only found in the black market"], a: 0, why: "Demerit goods are over-consumed." },
  { q: "Merit goods are:", opts: ["Private goods", "Public goods", "Free goods", "Always non-excludable"], a: 0, why: "Rival and excludable." },
  { q: "Which policy is most likely to reduce consumption of a demerit good?", opts: ["An indirect tax", "A subsidy", "A maximum price below equilibrium", "A fall in advertising warnings"], a: 0, why: "A tax raises price and cuts quantity." },
  { q: "If demand for a demerit good is price inelastic, a tax is likely to:", opts: ["Raise a lot of revenue but cut consumption only a little", "Cut consumption a lot and raise little revenue", "Have no effect on price", "Increase consumption"], a: 0, why: "Inelastic demand means quantity falls by less than the price rise." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Merit good", "Under-consumed: benefits not fully seen."],
  ["Demerit good", "Over-consumed: harm underestimated."],
  ["Information failure", "Root cause of both."],
  ["Private good", "Merit and demerit goods are private goods."],
  ["Subsidy", "Merit good policy: lowers price."],
  ["Indirect tax", "Demerit good policy: raises price."],
  ["Minimum price", "Raises price above equilibrium."],
  ["Black market", "Unintended effect of bans and price floors."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "The National Library Board of Singapore is a public sector organisation that finances and manages the state libraries. What is the most likely reason for this? (Feb/March 2022 · 12 · Q16, reworded)", opts: ["Libraries are public goods", "Libraries are merit goods", "The cost of providing library services would be greater in the private sector", "The opportunity cost to the public sector of providing library services is zero"], a: 1, why: "Libraries are private goods that are under-consumed unless the state provides them, so they are merit goods. They are rival and excludable, and the state has an opportunity cost." },
  { q: "What explains the underconsumption of merit goods? (Feb/March 2024 · 12 · Q13, reworded)", opts: ["Their value is not fully understood by consumers", "They are unproductive goods and services", "They can only be provided by the government", "They are only provided by the private sector"], a: 0, why: "Merit goods are under-consumed because consumers do not fully understand their benefits (information failure)." },
  { q: "A government provided additional free hospital care to its citizens. What happened as a result? (May/June 2021 · 11 · Q16, reworded)", opts: ["The supply of merit goods reduced", "The supply of merit goods increased", "The supply of private goods reduced", "The supply of public goods increased"], a: 1, why: "Hospital care is a merit good, so more free provision increases the supply of merit goods. It is a private good, not a public good." },
  { q: "What would be a valid objection to the government provision of goods and services? (May/June 2022 · 14 · Q15, reworded)", opts: ["There will be an increase in consumer sovereignty", "Only the private sector can provide merit goods", "Tax rates and tax income are likely to fall", "Investment in the private sector might be reduced"], a: 3, why: "Government provision can crowd out private investment. The state can provide merit goods, and provision raises, not lowers, the need for taxes." },
  { q: "A government introduces an effective minimum price for a product but makes no other intervention in the market. This policy suggests that the government's objective is (May/June 2024 · 13 · Q12, reworded)", opts: ["to discourage consumption of a demerit good", "to increase the consumption of a merit good", "to reduce the price of a private good", "to support the incomes of producers"], a: 0, why: "A minimum price above the equilibrium raises price and reduces quantity demanded, so it fits a demerit good." },
  { q: "A flood-control dam is an example of a good provided directly by a government. Which statement relating to the direct provision of a flood-control dam is not correct? (May/June 2025 · 13 · Q13, reworded)", opts: ["It allows the government to tackle the failure to provide public goods", "It forces the government to incur an opportunity cost", "It involves the supply of a merit good", "It is an example of government allocation of resources"], a: 2, why: "A flood-control dam is non-rival and non-excludable, so it is a public good, not a merit good." },
  { q: "If an industry is currently state-owned and state-run, what does not represent a reason for it being privatised? (Oct/Nov 2022 · 13 · Q17, reworded)", opts: ["Decisions will no longer be taken with political considerations in mind", "The benefits of merit goods will be taken into account in decision-making", "Its owners would have more incentive to make it operate profitably", "There will be greater incentives for managers to introduce modern technology"], a: 1, why: "A private owner is motivated by profit, so wider merit good benefits are less likely to be taken into account." },
  { q: "Why might a government nationalise a private firm? (Oct/Nov 2021 · 12 · Q16, reworded)", opts: ["to gain greater efficiency due to more competition", "to increase merit good provision", "to increase choice for the consumer", "to raise more tax revenue"], a: 1, why: "Nationalisation can increase provision of merit goods that private firms under-supply. It reduces competition and choice." },
  { q: "A government introduces charges for vehicles using the roads in its capital city. Which characteristic must the roads have for this to be successful in reducing congestion? (Oct/Nov 2023 · 11 · Q14, reworded)", opts: ["The roads must be excludable", "The roads must be merit goods", "The roads must be non-rivalrous", "The roads must be public goods"], a: 0, why: "A charge only works if non-payers can be excluded." },
  { q: "A government regards alcoholic drinks as a demerit good and introduces a minimum price above the equilibrium in an attempt to protect consumers. Demand for alcoholic drinks is price inelastic. What is the most likely outcome? (Oct/Nov 2020 · 13 · Q14, reworded)", opts: ["a fall in the revenue of alcoholic drink producers", "a fall in the quantity of alcoholic drink sales", "a long-run shortage of alcoholic drinks", "an increase in specific tax revenue from the sale of alcoholic drinks"], a: 1, why: "A price above the equilibrium reduces quantity demanded, though only a little when demand is inelastic. Revenue rises, not falls." },
] });
