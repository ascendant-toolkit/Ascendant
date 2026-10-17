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

/* ---------- adjustment ---------- */
function adjDraw(s) {
  const a = (90 - s.p) / 0.8, b = (s.p - 10) / 0.8; let o = sdPlot({ d: 0, s: 0, g: 0 });
  const lo = Math.min(a, b), hi = Math.max(a, b);
  o += SV.rect(SDX(lo), SDY(s.p) - 6, Math.abs(SDX(hi) - SDX(lo)), 12, s.p > 50 ? "f2" : "f3", op(0.7)) + SV.line(70, SDY(s.p), SDX(hi), SDY(s.p), "dash") + SV.circle(SDX(a), SDY(s.p), 6, "dot2") + SV.circle(SDX(b), SDY(s.p), 6, "dot1") + SV.text(62, SDY(s.p) + 4, "$" + Lib.fmtN(s.p, 0), "sm", { "text-anchor": "end" });
  const gap = Math.abs(a - b); if (gap > 1) o += tag(SDX(hi) + 10, SDY(s.p) + 4, (s.p > 50 ? "excess supply " : "excess demand ") + Lib.fmtN(gap, 0), s.p > 50 ? "c2" : "c3");
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="A price above equilibrium creates excess supply">${adjDraw({ p: 70 })}</svg>`;
Lib.stepper($("#stA"), { w: 760, h: 300, label: "The market adjusts from a price above equilibrium", base: { p: 70 }, draw: adjDraw, tween: 900, dwell: 5400, steps: [
  { cap: "<b>Price too high ($70).</b> Quantity supplied (75) exceeds quantity demanded (25): <b>excess supply</b> of 50 units. Stock piles up.", s: { p: 70 } },
  { cap: "<b>Price falls to $60.</b> Firms cut prices to sell stock. Quantity demanded rises and quantity supplied falls, so the surplus narrows.", s: { p: 60 } },
  { cap: "<b>Price reaches $50.</b> Quantity demanded equals quantity supplied (50). This is the <b>equilibrium</b>: the market clears and there is no tendency to change.", s: { p: 50 } },
  { cap: "<b>Price too low ($30).</b> Quantity demanded (75) exceeds quantity supplied (25): <b>excess demand</b>. Buyers bid the price back up.", s: { p: 30 } },
] });

/* ---------- both shift ---------- */
function bothDraw(s) { return sdPlot({ d: s.d, s: s.s, g: 1, n: s.n }); }
$("#pic2").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="Demand and supply both shift right, quantity rises and price is uncertain">${bothDraw({ d: 25, s: 10, n: 1 })}</svg>`;
Lib.stepper($("#stB"), { w: 760, h: 300, label: "Demand and supply shift at the same time", base: { d: 0, s: 0, n: 0 }, draw: bothDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>Start.</b> The market is in equilibrium at $50 and 50 units.", s: { d: 0, s: 0, n: 0 } },
  { cap: "<b>Demand shifts right a lot, supply a little.</b> Quantity rises for certain. Price rises as well because the demand shift is bigger.", s: { d: 25, s: 10, n: 1 } },
  { cap: "<b>Supply shifts right more than demand.</b> Quantity still rises. Now price <b>falls</b>. The direction of price depends on the relative size of the shifts.", s: { d: 10, s: 25, n: 1 } },
  { cap: "<b>Equal shifts.</b> Quantity rises by the size of the shift and the price stays the same.", s: { d: 20, s: 20, n: 1 } },
] });

/* ---------- Lab 1 ---------- */
function labA() {
  if (!$("#pp")) return;
  const p = +$("#pp").value, a = Math.max(0, (90 - p) / 0.8), b = Math.max(0, (p - 10) / 0.8), st = Math.abs(a - b) < 0.5 ? "Equilibrium" : a > b ? "Shortage" : "Surplus";
  $("#r1").textContent = Lib.fmtN(a, 0); $("#r2").textContent = Lib.fmtN(b, 0); $("#r3").textContent = st;
  $("#rv").textContent = st === "Equilibrium" ? "Quantity demanded equals quantity supplied at $50. The market clears and nothing pushes the price to change." : st === "Shortage" ? `At $${p} there is a shortage (excess demand) of ${Lib.fmtN(a - b, 0)} units. Buyers compete, so the price tends to rise.` : `At $${p} there is a surplus (excess supply) of ${Lib.fmtN(b - a, 0)} units. Sellers compete, so the price tends to fall.`;
  $("#labA").innerHTML = adjDraw({ p });
}
Lib.slider($("#g1"), { id: "pp", label: "Price, $ ", min: 10, max: 90, step: 5, value: 80, fmt: (v) => "$" + v, onInput: labA });
$("#adj").onclick = () => { const el = $("#pp"), p = +el.value, t = Math.abs(p - 50) < 3 ? 50 : p + (50 - p) * 0.4; el.value = Math.round(t / 5) * 5 === p ? (p > 50 ? p - 5 : p + 5) : Math.round(t / 5) * 5; el.dispatchEvent(new Event("input", { bubbles: true })); };
labA();

/* ---------- Lab 2 ---------- */
function labB() {
  if (!$("#dd") || !$("#ss")) return;
  const d = +$("#dd").value, s = +$("#ss").value, e = sdEq(d, s), e0 = sdEq(0, 0), dp = e.p - e0.p, dq = e.q - e0.q;
  $("#t1").textContent = "$" + Lib.fmtN(e.p, 0); $("#t2").textContent = Lib.fmtN(e.q, 0); $("#t3").textContent = Math.abs(dp) < 0.5 ? "None" : dp > 0 ? "Up" : "Down";
  let msg = "";
  if (d === 0 && s === 0) msg = "Neither curve has moved, so the equilibrium is still $50 and 50 units.";
  else if (d * s > 0) msg = `Both curves shift the same way, so quantity ${dq > 0 ? "rises" : "falls"} for certain. The price ${Math.abs(dp) < 0.5 ? "stays the same because the shifts are equal" : dp > 0 ? "rises because demand moved more" : "falls because supply moved more"}.`;
  else if (d * s < 0) msg = `The curves shift in opposite directions, so price ${dp > 0 ? "rises" : "falls"} for certain. The quantity ${Math.abs(dq) < 0.5 ? "stays the same because the shifts are equal" : dq > 0 ? "rises because the demand shift is larger" : "falls because the supply shift is larger"}.`;
  else msg = `Only ${d !== 0 ? "demand" : "supply"} shifts: price ${dp > 0 ? "rises" : "falls"} and quantity ${dq > 0 ? "rises" : "falls"}.`;
  $("#tv").textContent = msg;
  $("#labB").innerHTML = sdPlot({ d, s, g: 1, n: 1 });
}
Lib.slider($("#g2"), { id: "dd", label: "Demand shift (negative = left, positive = right) ", min: -30, max: 30, step: 5, value: 0, fmt: (v) => v, onInput: labB });
Lib.slider($("#g3"), { id: "ss", label: "Supply shift (negative = left, positive = right) ", min: -30, max: 30, step: 5, value: 0, fmt: (v) => v, onInput: labB });
labB();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "What happens to price and quantity?", buckets: [{"label": "Both rise"}, {"label": "Both fall"}, {"label": "Price falls, quantity rises"}, {"label": "Price rises, quantity falls"}], items: [{"text": "Demand shifts right", "b": 0}, {"text": "Demand shifts left", "b": 1}, {"text": "Supply shifts right", "b": 2}, {"text": "Supply shifts left", "b": 3}, {"text": "A successful advertising campaign", "b": 0}, {"text": "A fall in the cost of raw materials", "b": 2}, {"text": "A drought hits a crop", "b": 3}, {"text": "Incomes fall (normal good)", "b": 1}], done: "Demand moves price and quantity in the same direction; supply moves them in opposite directions." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Equilibrium", "Quantity demanded equals quantity supplied"], ["Excess supply", "Price is above equilibrium; Qs exceeds Qd"], ["Excess demand", "Price is below equilibrium; Qd exceeds Qs"], ["Market clearing", "No buyer or seller is left unsatisfied at that price"], ["Disequilibrium", "Quantity demanded differs from quantity supplied"], ["Equilibrium price", "The price at which the market has no tendency to change"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the adjustment to a surplus in order.", items: ["The price is above equilibrium", "Quantity supplied exceeds quantity demanded", "Firms cut price to clear stock", "Quantity demanded rises and quantity supplied falls", "The market reaches equilibrium where Qd = Qs"], done: "Surplus pushes the price down until the market clears." });
Lib.calc($("#c1"), { qs: [
  {"q": "Qd = 120 − 2P and Qs = 3P − 30. What is the equilibrium price ($)?", "a": 30, "unit": "$", "tol": 0.5, "hint": "Set 120 − 2P = 3P − 30.", "sol": "150 = 5P, so P = <b>$30</b>."},
  {"q": "Using the same equations, what is the equilibrium quantity?", "a": 60, "unit": "units", "tol": 0.5, "hint": "Put P = 30 into Qd.", "sol": "120 − 60 = <b>60</b>."},
  {"q": "At a price of $40, what is the excess supply (units)?", "a": 40, "unit": "units", "tol": 0.5, "hint": "Qs = 90, Qd = 40.", "sol": "Qs = 3 × 40 − 30 = 90 and Qd = 120 − 80 = 40, so excess supply is <b>50</b>."},
  {"q": "Qd = 100 − P and Qs = 2P − 20. Find the equilibrium price ($).", "a": 40, "unit": "$", "tol": 0.5, "hint": "100 − P = 2P − 20.", "sol": "120 = 3P, so P = <b>$40</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Equilibrium is where:", opts: ["Quantity demanded equals quantity supplied", "Price is zero", "The government sets the price", "Producers earn maximum revenue"], a: 0, why: "The market clears." },
  { q: "Price above equilibrium causes:", opts: ["Excess supply", "Excess demand", "A shift of demand", "No change"], a: 0, why: "Qs exceeds Qd." },
  { q: "A rise in supply with demand unchanged will:", opts: ["Lower price and raise quantity", "Raise price and lower quantity", "Raise both", "Lower both"], a: 0, why: "Right shift of supply." },
  { q: "Demand and supply both shift right. What is certain?", opts: ["Quantity rises", "Price rises", "Price falls", "Quantity falls"], a: 0, why: "Only quantity is certain." },
  { q: "A market's equilibrium quantity falls and price rises. This is consistent with:", opts: ["A left shift of supply", "A right shift of supply", "A right shift of demand", "A left shift of demand"], a: 0, why: "Higher costs reduce supply." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Equilibrium", "Qd = Qs, no tendency to change."],
  ["Excess supply", "Price above equilibrium."],
  ["Excess demand", "Price below equilibrium."],
  ["Demand shift", "Price and quantity move together."],
  ["Supply shift", "Price and quantity move oppositely."],
  ["Two shifts", "One of price or quantity is uncertain."],
  ["Solve", "Qd = Qs for P, then Q."],
  ["Market clears", "No one left unsatisfied."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "What must be correct when the free market for a good is in disequilibrium? (Feb/March 2020 · 12 · Q9, reworded)", opts: ["Consumers can buy all of the good that they demand at the market price", "Producers can sell all of the good that they supply at the market price", "The market price of the good will not change", "The quantity of the good demanded differs from the quantity supplied"], a: 3, why: "In disequilibrium quantity demanded and quantity supplied differ." },
  { q: "In a free market there is a surplus of a good. Which change would cause the market to come to an equilibrium? (May/June 2020 · 13 · Q5, reworded)", opts: ["a decrease in demand", "a fall in price", "a government minimum price", "an increase in supply"], a: 1, why: "A fall in price reduces the surplus. A minimum price would keep it." },
  { q: "Which statement about market disequilibrium is correct? (May/June 2022 · 12 · Q13, reworded)", opts: ["Price is likely to change", "Supply is equal to demand", "The government must intervene", "There must be shortages"], a: 0, why: "Disequilibrium puts pressure on price. It could be a surplus or a shortage." },
  { q: "The price of a product is above the market equilibrium price. Which combination of changes is certain to result as the market adjusts towards equilibrium? (May/June 2022 · 11 · Q12, reworded)", opts: ["quantity demanded falls, quantity supplied falls", "quantity demanded falls, quantity supplied rises", "quantity demanded rises, quantity supplied falls", "quantity demanded rises, quantity supplied rises"], a: 2, why: "A falling price extends demand and contracts supply." },
  { q: "The quantity demanded of a product is given by QD = 400 − 10P, when P is the price in dollars. Supply of the product is fixed at 100 units. If the price is $20, what will be the position in the market? (Feb/March 2025 · 12 · Q10, reworded)", opts: ["It will be in disequilibrium with excess demand of 100 units", "It will be in disequilibrium with excess supply of 100 units", "It will be in equilibrium with 100 units traded", "It will be in equilibrium with 200 units traded"], a: 0, why: "QD = 400 − 200 = 200, which is 100 more than the supply of 100." },
  { q: "In the market for a good the quantity supplied and the quantity demanded are given by QS = P − 30 and QD = 240 − 2P where P is the price in dollars. A change in the tax on the good makes QS = P − 36. How will the change affect equilibrium price? (May/June 2020 · 12 · Q13, reworded)", opts: ["It will fall by $2", "It will fall by $6", "It will rise by $2", "It will rise by $6"], a: 2, why: "Before: P − 30 = 240 − 2P gives P = 90. After: P − 36 = 240 − 2P gives P = 92, a rise of $2." },
  { q: "The table shows the supply and demand for avocados in Mexico City: at $45, demand 170 and supply 230; at $40, 190 and 190; at $35, 210 and 150; at $30, 230 and 110. As a result of lower transport costs, supply rises by 60 kg at all prices. What is the new equilibrium price? (Feb/March 2020 · 12 · Q11, reworded)", opts: ["$45", "$40", "$35", "$30"], a: 2, why: "At $35 new supply is 150 + 60 = 210, equal to demand." },
  { q: "A market is in equilibrium with 100 units of the product sold at a price of US$10 each. The price elasticity of supply is +2.0 and the price elasticity of demand is −1.0. What will be the state of the market if a minimum price of US$11 is imposed? (May/June 2021 · 12 · Q8, reworded)", opts: ["an excess demand of 10 units", "an excess demand of 30 units", "an excess supply of 20 units", "an excess supply of 30 units"], a: 3, why: "A 10% price rise raises quantity supplied by 20% (120) and cuts quantity demanded by 10% (90), so excess supply is 30." },
  { q: "Goods X and Y are complements. What will be the effect on the equilibrium price and quantity of good X of an increase in the supply of good Y? (May/June 2021 · 12 · Q10, reworded)", opts: ["price decreases, quantity decreases", "price decreases, quantity increases", "price increases, quantity decreases", "price increases, quantity increases"], a: 3, why: "Cheaper Y raises demand for its complement X, so X's price and quantity both rise." },
  { q: "The table shows a competitive market in equilibrium in two periods: in period 1 the price is 50 cents and quantity 10 000, and in period 2 the price is 60 cents and quantity 12 000. What could explain the change from period 1 to period 2? (Feb/March 2021 · 12 · Q7, reworded)", opts: ["an increase in the price of a complement", "an increase in the price of a substitute", "the imposition of a minimum price of 60 cents by a government", "the imposition of an indirect tax on suppliers"], a: 1, why: "Both price and quantity rose, which means demand shifted right. A dearer substitute does that." },
  { q: "The table shows the market demand and supply for kiwifruit. At $3 per kg demand is 160 thousand tonnes and supply 140 thousand tonnes; at $4, 130 and 150; at $2, 190 and 130. At a market price of $3 per kg there is disequilibrium. Which action would the government have to take to achieve market equilibrium at $3 per kg? (Oct/Nov 2021 · 13 · Q12, reworded)", opts: ["impose an indirect tax of $2 per kg on kiwifruit", "purchase the entire supply at $3 per kg and sell at $2 per kg", "set a maximum price of $3 per kg", "subsidise kiwifruit production by $2 per kg"], a: 3, why: "Producers need an effective price of $5 to supply 160, so a $2 subsidy makes the market clear at $3." },
  { q: "The market for a product is initially in equilibrium. Which combination of changes will cause the price of the product to rise and the quantity sold to fall? (Oct/Nov 2022 · 13 · Q13, reworded)", opts: ["a decrease in demand that is larger than a decrease in supply", "a decrease in demand that is smaller than a decrease in supply", "an increase in demand that is larger than an increase in supply", "an increase in demand that is smaller than an increase in supply"], a: 1, why: "Supply falls by more than demand falls, so price rises and quantity falls." },
] });
