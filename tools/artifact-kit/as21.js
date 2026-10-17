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

/* ---------- effective demand venn ---------- */
function evDraw(s) {
  let o = SV.circle(290, 160, 110, "dot1", op(0.3 * s.a)) + SV.circle(470, 160, 110, "dot3", op(0.3 * s.b));
  o += SV.text(220, 150, "Willing", "lbl bd", { "text-anchor": "middle", ...op(s.a) }) + SV.text(220, 172, "(wants it)", "sm", { "text-anchor": "middle", ...op(s.a) });
  o += SV.text(540, 150, "Able to pay", "lbl bd", { "text-anchor": "middle", ...op(s.b) }) + SV.text(540, 172, "(income, savings)", "sm", { "text-anchor": "middle", ...op(s.b) });
  if (s.c > 0) o += SV.text(380, 150, "EFFECTIVE", "lbl bd", { "text-anchor": "middle", style: "fill:var(--accent)", ...op(s.c) }) + SV.text(380, 172, "DEMAND", "lbl bd", { "text-anchor": "middle", style: "fill:var(--accent)", ...op(s.c) });
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="Willingness and ability to pay overlap as effective demand">${evDraw({ a: 1, b: 1, c: 1 })}</svg>`;
Lib.stepper($("#stE"), { w: 760, h: 300, label: "Effective demand is where willingness and ability to pay overlap", base: { a: 0, b: 0, c: 0 }, draw: evDraw, tween: 800, dwell: 5200, steps: [
  { cap: "<b>Willingness.</b> Many people would like a good. A want or a need alone is not demand.", s: { a: 1 } },
  { cap: "<b>Ability to pay.</b> Some people have the income or credit to buy at the price, whether or not they want the good.", s: { a: 1, b: 1 } },
  { cap: "<b>The overlap</b> is effective demand: people who both want the good and can pay for it at that price.", s: { a: 1, b: 1, c: 1 } },
] });

/* ---------- horizontal sum ---------- */
const hx = (q) => 70 + q * 12, hy = (p) => 270 - p * 2.4;
function hsDraw(s) {
  let o = axes(70, 270, 700, 25, "Quantity", "Price ($)");
  const ln = (k, c, v, lab) => SV.line(hx(0), hy(100), hx(k), hy(0), c, { "stroke-width": 3, ...op(v) }) + tag(hx(k) + 4, hy(0) - 6, lab, c, v);
  o += ln(20, "c1", s.a, "A") + ln(30, "c3", s.b, "B") + ln(50, "c2", s.m, "Market");
  if (s.m > 0.2) { const pr = 40, qa = 20 - 0.2 * pr, qb = 30 - 0.3 * pr; o += SV.line(70, hy(pr), hx(qa + qb), hy(pr), "dash", op(s.m)) + SV.text(62, hy(pr) + 4, "$40", "sm", { "text-anchor": "end", ...op(s.m) }) + tag(hx(qa / 2), hy(pr) - 6, "A " + qa, "c1", s.m, "middle") + tag(hx(qa + qb / 2), hy(pr) - 6, "B " + qb, "c3", s.m, "middle") + tag(hx(qa + qb) + 4, hy(pr) + 4, "= " + (qa + qb), "c2", s.m); }
  return o;
}
$("#pic2").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="Two individual demand curves added horizontally to give market demand">${hsDraw({ a: 1, b: 1, m: 1 })}</svg>`;
Lib.stepper($("#stH"), { w: 760, h: 300, label: "Two individual demand curves added horizontally", base: { a: 0, b: 0, m: 0 }, draw: hsDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>Consumer A</b> demands 12 units at a price of $40.", s: { a: 1 } },
  { cap: "<b>Consumer B</b> demands 18 units at $40.", s: { a: 1, b: 1 } },
  { cap: "<b>Market demand</b> adds the quantities at each price: 12 + 18 = 30 at $40. The curve is the <b>horizontal sum</b>, not a vertical one.", s: { a: 1, b: 1, m: 1 } },
] });

/* ---------- Lab 1: demand determinants ---------- */
function labD() {
  if (!$("#inc") || !$("#sub") || !$("#cmp") || !$("#tst")) return;
  const raw = 0.9 * +$("#inc").value + 0.6 * +$("#sub").value - 0.6 * +$("#cmp").value + 0.8 * +$("#tst").value, d = Math.max(-30, Math.min(30, raw)), e = sdEq(d, 0), e0 = sdEq(0, 0);
  $("#r1").textContent = Math.abs(d) < 0.5 ? "None" : d > 0 ? "Right" : "Left"; $("#r2").textContent = "$" + Lib.fmtN(e.p, 0); $("#r3").textContent = Lib.fmtN(e.q, 0);
  $("#rv").textContent = Math.abs(d) < 0.5 ? "No determinant has changed, so demand and the equilibrium stay at $50 and 50 units." : `${d > 0 ? "A rise" : "A fall"} in demand shifts the curve to the ${d > 0 ? "right" : "left"}: the equilibrium price ${e.p > e0.p ? "rises" : "falls"} from $50 to $${Lib.fmtN(e.p, 0)} and the quantity ${e.q > e0.q ? "rises" : "falls"} from 50 to ${Lib.fmtN(e.q, 0)}. A change in the price of the good itself would be a movement along a curve, not a shift.`;
  $("#labA").innerHTML = sdPlot({ d, s: 0, g: 1, n: 1 });
}
Lib.slider($("#g1"), { id: "inc", label: "Change in consumers' income, % (normal good) ", min: -20, max: 20, step: 5, value: 0, fmt: (v) => v + "%", onInput: labD });
Lib.slider($("#g2"), { id: "sub", label: "Change in price of a substitute, % ", min: -20, max: 20, step: 5, value: 0, fmt: (v) => v + "%", onInput: labD });
Lib.slider($("#g3"), { id: "cmp", label: "Change in price of a complement, % ", min: -20, max: 20, step: 5, value: 0, fmt: (v) => v + "%", onInput: labD });
Lib.slider($("#g4"), { id: "tst", label: "Change in tastes (advertising, fashion), % ", min: -20, max: 20, step: 5, value: 0, fmt: (v) => v + "%", onInput: labD });
labD();

/* ---------- Lab 2: supply determinants ---------- */
function labS() {
  if (!$("#cst") || !$("#tch") || !$("#tax")) return;
  const raw = -0.9 * +$("#cst").value + 0.9 * +$("#tch").value - 0.9 * +$("#tax").value, s = Math.max(-30, Math.min(30, raw)), e = sdEq(0, s), e0 = sdEq(0, 0);
  $("#t1").textContent = Math.abs(s) < 0.5 ? "None" : s > 0 ? "Right" : "Left"; $("#t2").textContent = "$" + Lib.fmtN(e.p, 0); $("#t3").textContent = Lib.fmtN(e.q, 0);
  $("#tv").textContent = Math.abs(s) < 0.5 ? "Costs, technology and taxes are unchanged, so supply does not shift." : `${s > 0 ? "Lower costs, better technology or a subsidy" : "Higher costs or a tax"} shift supply to the ${s > 0 ? "right" : "left"}. The equilibrium price ${e.p > e0.p ? "rises" : "falls"} to $${Lib.fmtN(e.p, 0)} and the quantity ${e.q > e0.q ? "rises" : "falls"} to ${Lib.fmtN(e.q, 0)}.`;
  $("#labB").innerHTML = sdPlot({ d: 0, s, g: 1, n: 1 });
}
Lib.slider($("#g5"), { id: "cst", label: "Change in costs (wages, materials), % ", min: -20, max: 20, step: 5, value: 0, fmt: (v) => v + "%", onInput: labS });
Lib.slider($("#g6"), { id: "tch", label: "Improvement in technology, % ", min: -20, max: 20, step: 5, value: 0, fmt: (v) => v + "%", onInput: labS });
Lib.slider($("#g7"), { id: "tax", label: "Indirect tax (positive) or subsidy (negative), % ", min: -20, max: 20, step: 5, value: 0, fmt: (v) => v + "%", onInput: labS });
labS();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "What happens to demand for coffee?", buckets: [{"label": "Shifts right"}, {"label": "Shifts left"}, {"label": "Movement along the curve"}], items: [{"text": "Income rises (coffee is a normal good)", "b": 0}, {"text": "Price of tea (a substitute) falls", "b": 1}, {"text": "The price of coffee falls", "b": 2}, {"text": "Consumers expect coffee prices to rise next month", "b": 0}, {"text": "A successful advertising campaign for coffee", "b": 0}, {"text": "Price of milk (a complement) rises", "b": 1}, {"text": "Population grows", "b": 0}, {"text": "The price of coffee rises", "b": 2}], done: "Only the price of coffee itself causes a movement along the curve. Every other determinant shifts it." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Effective demand", "Willingness backed by ability to pay"], ["Market demand", "Horizontal sum of individual demand"], ["Substitute", "A rise in its price raises demand for this good"], ["Complement", "A rise in its price lowers demand for this good"], ["Normal good", "Demand rises as income rises"], ["Inferior good", "Demand falls as income rises"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the steps of finding market demand in order.", items: ["Choose a price", "Read each individual's quantity demanded at that price", "Add the quantities together", "Plot the total against that price", "Repeat for other prices and join the points"], done: "Add quantities horizontally at each price." });
Lib.calc($("#c1"), { qs: [
  {"q": "At a price of $5, three consumers demand 8, 12 and 20 units. What is market demand?", "a": 40, "unit": "units", "tol": 0.5, "hint": "Add the quantities.", "sol": "8 + 12 + 20 = <b>40 units</b>."},
  {"q": "Market demand is Qd = 500 − 20P. What quantity is demanded at P = 10?", "a": 300, "unit": "units", "tol": 1, "hint": "500 − 200.", "sol": "<b>300</b>."},
  {"q": "At P = 15, using the same demand function, what is the quantity demanded?", "a": 200, "unit": "units", "tol": 1, "hint": "500 − 300.", "sol": "<b>200</b>."},
  {"q": "Market supply is Qs = 20P − 100. What quantity is supplied at P = 15?", "a": 200, "unit": "units", "tol": 1, "hint": "300 − 100.", "sol": "<b>200</b>, so at $15 the market clears."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Effective demand requires:", opts: ["Willingness and ability to pay", "Only a need for the good", "A fall in price", "Government support"], a: 0, why: "Both willingness and ability to pay." },
  { q: "Market demand is found by:", opts: ["Adding quantities at each price", "Adding prices at each quantity", "Multiplying individual demands", "Averaging the demand curves"], a: 0, why: "Horizontal summation." },
  { q: "A fall in the price of a complement will:", opts: ["Shift demand for the good to the right", "Shift demand for the good to the left", "Cause a movement along the demand curve", "Shift supply to the right"], a: 0, why: "Cheaper complement raises demand for this good." },
  { q: "Which change will shift the supply curve to the right?", opts: ["A fall in raw material costs", "A rise in the price of the good", "A rise in the wage rate", "An indirect tax on the good"], a: 0, why: "Lower costs raise supply at every price." },
  { q: "A rise in the price of a good causes:", opts: ["A movement along the demand curve", "A shift of the demand curve to the left", "A shift of supply to the right", "A rise in income"], a: 0, why: "Price changes cause movements." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Effective demand", "Willing and able to pay."],
  ["Market demand", "Horizontal sum."],
  ["Normal good", "Income up, demand up."],
  ["Inferior good", "Income up, demand down."],
  ["Substitute", "Its price up, demand up."],
  ["Complement", "Its price up, demand down."],
  ["Cost fall", "Supply shifts right."],
  ["Price of the good", "Movement along, not a shift."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "What is the definition of effective demand? (Feb/March 2024 · 12 · Q6, reworded)", opts: ["demand that is speculative", "demand that is supported by the ability to pay", "the relationship between price and quantity demanded", "the total amount demanded by consumers"], a: 1, why: "Effective demand needs willingness and ability to pay." },
  { q: "How would an economist establish the market demand curve for a private good? (May/June 2021 · 12 · Q12, reworded)", opts: ["by adding consumer surplus to total expenditure", "by combining individual demand curves horizontally", "by combining the price elasticity of individual demands", "by multiplying price by quantity demanded"], a: 1, why: "Market demand is found by summing quantities horizontally at each price." },
  { q: "What describes a market supply curve? (May/June 2020 · 11 · Q5, reworded)", opts: ["It is downward sloping", "It is the same as the aggregate supply curve", "It is the sum of all firms' supply curves for a product", "It is the supply of all products within an economy"], a: 2, why: "Market supply sums the supply of all firms for one product. Aggregate supply covers the whole economy." },
  { q: "What is likely to have a greater effect on an individual demand curve than on a market demand curve? (Feb/March 2025 · 12 · Q9, reworded)", opts: ["changing weather patterns", "government policy to promote consumption", "growth in population", "more expensive substitutes"], a: 3, why: "An individual's demand responds strongly to relative prices of substitutes, while weather, policy and population act on the market as a whole." },
  { q: "What is correct about market supply? (Oct/Nov 2020 · 11 · Q13, reworded)", opts: ["Market supply can increase only when all individual firms increase their output", "Market supply is effective when consumers have sufficient income to buy the good", "Market supply is the result of aggregating the supply of all individual firms", "Market supply of an inferior good falls as price increases"], a: 2, why: "Market supply is the sum of firms' supplies. More firms entering can raise it too." },
  { q: "What most accurately describes a market supply curve? (May/June 2024 · 13 · Q10, reworded)", opts: ["supply at different income levels, assuming product prices remain unchanged", "supply at different levels of factor prices, assuming product prices remain unchanged", "supply at different prices, assuming no changes in technology", "supply at different time periods, assuming no changes in technology"], a: 2, why: "A supply curve relates price to quantity supplied, ceteris paribus, including technology." },
  { q: "What is not held constant when aggregating individual firms' supply curves to give the short-run market supply curve? (Oct/Nov 2024 · 11 · Q9, reworded)", opts: ["the number of firms in the industry", "the price of the product", "the prices of factors of production", "the state of technology"], a: 1, why: "Price is the variable on the vertical axis, so it changes along the curve." },
  { q: "Demand for medical face masks exceeds supply during a disease outbreak. What is the most likely cause of this excess demand? (May/June 2023 · 11 · Q13, reworded)", opts: ["Some consumers do not have effective demand", "The demand for medical face masks is price inelastic in the short run", "The price of medical face masks is fixed below the equilibrium price", "The supply of medical face masks is inelastic in the short run"], a: 2, why: "Excess demand at a fixed price below equilibrium creates a shortage." },
  { q: "Good X is related to good Y. Incomes increase and the price of good Y falls. Which combination would give the greatest increase in demand for good X? (Feb/March 2020 · 12 · Q8, reworded)", opts: ["Good X an inferior good, good Y a complement", "Good X an inferior good, good Y a substitute", "Good X a normal good, good Y a complement", "Good X a normal good, good Y a substitute"], a: 2, why: "Rising income raises demand for a normal good. A fall in the price of a complement also raises demand for X." },
  { q: "In Asia, instant noodles is an inferior good because dried fruit is a better quality substitute. What could have caused demand for instant noodles to shift to the right? (May/June 2024 · 12 · Q9, reworded)", opts: ["a fall in the price of dried fruit", "a rise in real income", "a rise in unemployment", "a successful advertising campaign by dried fruit producers"], a: 2, why: "A rise in unemployment lowers incomes, which raises demand for an inferior good." },
  { q: "What could explain a shift of an upward-sloping supply curve to the right? (May/June 2021 · 11 · Q5, reworded)", opts: ["an increase in firms' unit labour costs", "an increase in the number of firms in the industry", "an increase in the price of the good", "an indirect tax imposed on the good"], a: 1, why: "More firms raise supply at every price. A rise in price is a movement along." },
  { q: "Which reason for the increase in demand for a smartphone is an example of joint demand? (May/June 2024 · 12 · Q11, reworded)", opts: ["a fall in its price", "a fall in the price of connecting to a network", "a fall in the price of parts used to make smartphones", "a rise in the price of a substitute"], a: 1, why: "Network connection is a complement, so a fall in its price raises demand for the phone." },
] });
