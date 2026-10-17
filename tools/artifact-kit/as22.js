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

/* ---------- movement along demand ---------- */
function mvDraw(s) {
  const q = (90 - s.p) / 0.8; let o = sdPlot({ d: 0, s: 0, g: 0 });
  o += SV.line(SDX(q), SDY(s.p), SDX(q), 270, "dash") + SV.line(70, SDY(s.p), SDX(q), SDY(s.p), "dash") + SV.circle(SDX(q), SDY(s.p), 7, "dot3") + SV.text(62, SDY(s.p) + 4, "$" + Lib.fmtN(s.p, 0), "sm", { "text-anchor": "end" }) + SV.text(SDX(q), 286, Lib.fmtN(q, 0), "sm", { "text-anchor": "middle" });
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="A fall in price moves the market down the demand curve">${mvDraw({ p: 30 })}</svg>`;
Lib.stepper($("#stM"), { w: 760, h: 300, label: "A movement along the demand curve caused by a change in price", base: { p: 50 }, draw: mvDraw, tween: 900, dwell: 5200, steps: [
  { cap: "<b>Start.</b> At a price of $50 the quantity demanded is 50 units.", s: { p: 50 } },
  { cap: "<b>Price falls to $30.</b> Quantity demanded rises to 75: an <b>extension</b> of demand. The demand curve has not moved.", s: { p: 30 } },
  { cap: "<b>Price rises to $70.</b> Quantity demanded falls to 25: a <b>contraction</b> of demand. Still the same curve.", s: { p: 70 } },
] });

/* ---------- shift of demand ---------- */
function shDraw(s) { return sdPlot({ d: s.d, s: 0, g: s.g, n: s.n }); }
$("#pic2").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="A rise in demand shifts the curve right and raises price and quantity">${shDraw({ d: 20, g: 1, n: 1 })}</svg>`;
Lib.stepper($("#stS"), { w: 760, h: 300, label: "A shift of the demand curve caused by a change in income", base: { d: 0, g: 1, n: 0 }, draw: shDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>Start.</b> Demand D1 and supply S1 give an equilibrium price P1 and quantity Q1.", s: { d: 0, n: 0 } },
  { cap: "<b>Incomes rise</b> (the good is normal). People want more at every price, so demand <b>shifts right</b> to D2. Price and quantity rise to P2 and Q2.", s: { d: 20, n: 1 } },
  { cap: "<b>A health scare</b> would shift demand <b>left</b> instead, lowering price and quantity. The shift changes demand, not just quantity demanded.", s: { d: -20, n: 1 } },
] });

/* ---------- Lab 1 ---------- */
function labP() {
  if (!$("#pp")) return;
  const p = +$("#pp").value, qd = Math.max(0, (90 - p) / 0.8), qs = Math.max(0, (p - 10) / 0.8), res = Math.abs(qd - qs) < 0.5 ? "Balanced" : qd > qs ? "Shortage" : "Surplus";
  $("#r1").textContent = Lib.fmtN(qd, 0); $("#r2").textContent = Lib.fmtN(qs, 0); $("#r3").textContent = res;
  $("#rv").textContent = `At $${p}, buyers want ${Lib.fmtN(qd, 0)} units and sellers offer ${Lib.fmtN(qs, 0)}. ${res === "Balanced" ? "This is the equilibrium price: nothing pushes it to change." : res === "Shortage" ? "Quantity demanded exceeds quantity supplied (excess demand), so price tends to rise: extension of supply, contraction of demand." : "Quantity supplied exceeds quantity demanded (excess supply), so price tends to fall: contraction of supply, extension of demand."} The curves themselves have not moved.`;
  let o = sdPlot({ d: 0, s: 0, g: 0 }); const a = (90 - p) / 0.8, b = (p - 10) / 0.8;
  o += SV.line(70, SDY(p), SDX(Math.max(a, b, 0)), SDY(p), "dash") + SV.circle(SDX(Math.max(0, a)), SDY(p), 6, "dot2") + SV.circle(SDX(Math.max(0, b)), SDY(p), 6, "dot1") + SV.text(62, SDY(p) + 4, "$" + p, "sm", { "text-anchor": "end" });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "pp", label: "Market price, $ ", min: 10, max: 90, step: 5, value: 70, fmt: (v) => "$" + v, onInput: labP });
labP();

/* ---------- Lab 2 ---------- */
const EV = [
  ["Incomes rise (normal good)", 20, 0, "Demand", "A rise in income raises demand for a normal good at every price, so demand shifts right."],
  ["Price of a substitute rises", 15, 0, "Demand", "Consumers switch to this good, so demand shifts right."],
  ["Price of a complement rises", -15, 0, "Demand", "The pair becomes dearer to buy, so demand shifts left."],
  ["Health scare about the good", -20, 0, "Demand", "Tastes turn against the good, so demand shifts left."],
  ["Cost of raw materials falls", 0, 20, "Supply", "Production costs fall, so supply shifts right."],
  ["New technology introduced", 0, 25, "Supply", "Output per unit of input rises and unit costs fall, so supply shifts right."],
  ["Indirect tax imposed", 0, -20, "Supply", "The tax raises each firm's cost, so supply shifts left."],
  ["Drought hits the harvest", 0, -25, "Supply", "Output falls at every price, so supply shifts left."],
];
function showEv(i) {
  const [t, d, s, c, why] = EV[i], e = sdEq(d, s), e0 = sdEq(0, 0);
  $$("#evB button").forEach((b, k) => b.classList.toggle("pri", k === i));
  $("#t1").textContent = c + (d + s > 0 ? " right" : " left"); $("#t2").textContent = "$" + Lib.fmtN(e.p, 0); $("#t3").textContent = Lib.fmtN(e.q, 0);
  $("#tv").textContent = `${t}. ${why} The equilibrium price ${e.p > e0.p ? "rises" : "falls"} from $50 to $${Lib.fmtN(e.p, 0)} and the quantity ${e.q > e0.q ? "rises" : "falls"} from 50 to ${Lib.fmtN(e.q, 0)}.`;
  $("#labB").innerHTML = sdPlot({ d, s, g: 1, n: 1 });
}
$("#evB").innerHTML = EV.map((e, i) => `<button class="b" data-i="${i}">${e[0]}</button>`).join("");
$$("#evB button").forEach((b) => (b.onclick = () => showEv(+b.dataset.i)));
showEv(0);

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Is it a shift or a movement?", buckets: [{"label": "Shift of demand"}, {"label": "Movement along demand"}, {"label": "Shift of supply"}], items: [{"text": "A rise in income (normal good)", "b": 0}, {"text": "The good's price falls", "b": 1}, {"text": "Wages in the industry rise", "b": 2}, {"text": "A successful advertising campaign", "b": 0}, {"text": "A fall in the price of a complement", "b": 0}, {"text": "A new tax on the good", "b": 2}, {"text": "The good's price rises", "b": 1}, {"text": "Better technology for producers", "b": 2}], done: "Own price: movement. Other demand determinants: demand shifts. Cost, tax and technology changes: supply shifts." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Extension of demand", "Quantity demanded rises because price falls"], ["Contraction of demand", "Quantity demanded falls because price rises"], ["Increase in demand", "Right shift of the demand curve"], ["Decrease in supply", "Left shift of the supply curve"], ["Subsidy", "Shifts the supply curve to the right"], ["Indirect tax", "Shifts the supply curve to the left"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the steps of a diagram answer in order.", items: ["Draw and label the axes: price and quantity", "Draw the original demand and supply curves and mark the equilibrium", "Shift the curve that has changed and label it", "Mark the new equilibrium price and quantity", "Explain the change in price and quantity in words"], done: "Always label the new equilibrium and say what happens to price and quantity." });
Lib.calc($("#c1"), { qs: [
  {"q": "Demand shifts right by 20 units at every price. Demand before: Qd = 100 − 2P. At P = 20, what is the new quantity demanded?", "a": 80, "unit": "units", "tol": 1, "hint": "Old Qd at P=20 is 60. Add 20.", "sol": "60 + 20 = <b>80</b>."},
  {"q": "Supply is Qs = 4P. A subsidy shifts supply right by 30 units at every price. At P = 10, what is the new quantity supplied?", "a": 70, "unit": "units", "tol": 1, "hint": "40 + 30.", "sol": "<b>70</b>."},
  {"q": "Price falls from $20 to $15 and quantity demanded rises from 40 to 50. What is the percentage change in quantity demanded?", "a": 25, "unit": "%", "tol": 0.5, "hint": "(50 − 40) ÷ 40.", "sol": "<b>25%</b>, an extension of demand."},
  {"q": "Equilibrium before: P = $50, Q = 50. After demand shifts right, Q = 60. What is the percentage rise in the equilibrium quantity?", "a": 20, "unit": "%", "tol": 0.5, "hint": "(60 − 50) ÷ 50.", "sol": "<b>20%</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A fall in the price of a good causes:", opts: ["A movement along the demand curve", "A shift of the demand curve to the right", "A shift of the supply curve to the left", "A fall in income"], a: 0, why: "Own price: movement." },
  { q: "What is the effect of a rise in demand and no change in supply?", opts: ["Price and quantity both rise", "Price falls and quantity rises", "Price rises and quantity falls", "Price and quantity both fall"], a: 0, why: "Right shift of demand moves along supply." },
  { q: "A new indirect tax on a good will:", opts: ["Shift the supply curve to the left", "Shift the demand curve to the left", "Shift the supply curve to the right", "Cause a movement along demand only"], a: 0, why: "A tax raises costs." },
  { q: "Which would cause demand for an inferior good to rise?", opts: ["A fall in consumers' incomes", "A rise in consumers' incomes", "A fall in its own price", "A subsidy to producers"], a: 0, why: "Negative income elasticity." },
  { q: "A supply shift to the right causes quantity demanded to:", opts: ["Extend along the demand curve", "Shift demand left", "Contract along demand", "Stay the same"], a: 0, why: "Price falls, so quantity demanded rises." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Movement", "Caused only by the good's own price."],
  ["Shift", "Caused by any other determinant."],
  ["Increase in demand", "Right shift."],
  ["Decrease in supply", "Left shift."],
  ["Extension", "Quantity demanded rises as price falls."],
  ["Contraction", "Quantity falls as price rises."],
  ["Cost fall", "Supply shifts right."],
  ["Draw", "Label the new equilibrium."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "What could not cause a shift in an individual's demand curve for good Z? (Feb/March 2021 · 12 · Q5, reworded)", opts: ["a change in advertising expenditure on Z", "a change in the individual's income", "a change in the individual's tastes", "a change in the price of Z"], a: 3, why: "The price of Z moves along the curve. The others shift it." },
  { q: "What causes the demand curve for an inferior good to shift to the right? (Feb/March 2022 · 12 · Q12, reworded)", opts: ["a decrease in consumer incomes", "a decrease in income tax", "a decrease in the price of a substitute good", "a decrease in the price of the good"], a: 0, why: "Falling incomes raise demand for inferior goods. A lower tax raises income, and a price change is a movement." },
  { q: "Which combination of the classification of a good and market change will cause the demand curve for the good to shift right? (May/June 2020 · 13 · Q10, reworded)", opts: ["inferior good, income decrease", "inferior good, price decrease", "normal good, income decrease", "normal good, price decrease"], a: 0, why: "An income fall shifts demand right for an inferior good. A price decrease is a movement." },
  { q: "What leads to a downward shift of a normal supply curve? (May/June 2021 · 12 · Q7, reworded)", opts: ["a rise in the cost of transporting goods", "a rise in the productivity of the labour force", "a rise in the rate of sales tax on the good", "a rise in the wage rate paid to workers"], a: 1, why: "A downward shift of supply (to the right) results from lower costs, so higher productivity." },
  { q: "What will not cause a shift in the market supply curve of a commodity? (May/June 2021 · 13 · Q6, reworded)", opts: ["a change in technology", "a rise in the price of a factor input", "a rise in the price of the commodity", "the introduction of a specific tax on the commodity"], a: 2, why: "The commodity's own price causes a movement along." },
  { q: "Which change would cause the supply curve of sugar-sweetened drinks to shift to the right? (May/June 2022 · 13 · Q7, reworded)", opts: ["a fall in the price of sugar", "a removal of a subsidy on sugar", "an increase in consumer income", "an increase of a specific tax on sugar"], a: 0, why: "Cheaper sugar lowers costs, so supply shifts right." },
  { q: "What is most likely to cause a shift in the supply curve for rice? (May/June 2023 · 13 · Q6, reworded)", opts: ["a change in the price of the rice", "a change in the price of meat", "a change in the size of the rice industry", "a change in tastes and preferences for rice"], a: 2, why: "More firms or farms change supply at every price." },
  { q: "What would not cause a shift in the demand curve for a good? (May/June 2023 · 13 · Q8, reworded)", opts: ["a change in the price of a complement", "a change in the price of a substitute", "a change in the price of the good itself", "a change in consumers' incomes"], a: 2, why: "The good's own price moves along the curve." },
  { q: "The demand curve for new cars in a country shifted to the left. Which change could have caused such a shift? (Oct/Nov 2020 · 11 · Q12, reworded)", opts: ["an increase in real disposable income", "an increase in the cost of borrowing", "an increase in the price of new cars", "an increase in the price of train travel"], a: 1, why: "Dearer credit lowers demand for cars bought on credit. Higher income and a dearer substitute would raise demand." },
  { q: "A bus journey is considered an inferior good in a relatively rich country such as Singapore but a normal good in a relatively poor country such as Tanzania. In which direction would an increase in incomes in both countries cause the demand curve for bus journeys in Singapore and Tanzania to shift? (Oct/Nov 2020 · 13 · Q10, reworded)", opts: ["Singapore left, Tanzania left", "Singapore left, Tanzania right", "Singapore right, Tanzania left", "Singapore right, Tanzania right"], a: 1, why: "Higher income lowers demand for an inferior good and raises it for a normal good." },
  { q: "An increase in which factor is likely to cause a shift to the left of the demand curve for cinema movies? (May/June 2024 · 11 · Q6, reworded)", opts: ["expenses for the heating system in the cinema", "payments charged by movie scriptwriters", "the cost of transport to the cinema", "taxes on the incomes of cinema operators"], a: 2, why: "Transport to the cinema is a complement, so its cost rising lowers demand. The others are costs for the cinema, which affect supply." },
  { q: "Shoe manufacturers often use leather to make their most expensive shoes. Due to a world shortage of leather, the price of leather has risen. What will be the effect of this price change? (May/June 2020 · 11 · Q11, reworded)", opts: ["The demand curve for leather shoes will shift to the left", "The demand curve for a substitute for leather shoes will shift to the right", "The supply curve for leather shoes will shift to the right", "The supply curve for a substitute for leather to make expensive shoes will shift to the left"], a: 1, why: "Dearer leather shoes make substitutes more attractive, so their demand rises. The supply of leather shoes shifts left." },
] });
