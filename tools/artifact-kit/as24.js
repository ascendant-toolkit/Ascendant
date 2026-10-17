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

/* ---------- complement and substitute ---------- */
function csDraw(s) { return sdPlot({ d: s.d, s: 0, g: 1, n: s.n }, { y: "Price of cars", D1: "D1", D2: "D2" }); }
$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="Demand for cars falls when the price of fuel, a complement, rises">${csDraw({ d: -20, n: 1 })}</svg>`;
Lib.stepper($("#stC"), { w: 760, h: 300, label: "The market for cars when the price of a related good rises", base: { d: 0, n: 0 }, draw: csDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>Start.</b> The market for cars is in equilibrium.", s: { d: 0, n: 0 } },
  { cap: "<b>The price of petrol (a complement) rises.</b> Driving costs more, so demand for cars shifts <b>left</b>. XED for cars with respect to petrol is <b>negative</b>.", s: { d: -20, n: 1 } },
  { cap: "<b>The price of public transport (a substitute) rises.</b> Cars look cheaper by comparison, so demand shifts <b>right</b>. XED is <b>positive</b>.", s: { d: 20, n: 1 } },
] });

/* ---------- derived demand chain ---------- */
const bx = (x, y, w, t, v, c = "f1") => SV.rect(x, y, w, 46, c, { rx: 8, ...op(0.55 * v) }) + SV.text(x + w / 2, y + 28, t, "lbl bd", { "text-anchor": "middle", ...op(v) });
function chDraw(s) {
  const ar = (x1, x2, v) => SV.line(x1, 70, x2 - 8, 70, "c4", { "stroke-width": 2.5, ...op(v) }) + SV.arrowHead(x2, 70, "r", "dot4");
  let o = bx(20, 47, 150, "Demand for cars rises", s.a, "f3") + ar(172, 210, s.b) + bx(212, 47, 160, "Car firms order more steel", s.b) + ar(374, 412, s.c) + bx(414, 47, 150, "Demand for steel rises", s.c, "f2") + ar(566, 604, s.d) + bx(606, 47, 130, "Steel price up", s.d, "f1");
  return o;
}
$("#pic2").innerHTML = `<svg viewBox="0 0 760 120" role="img" aria-label="Demand for cars rises so car firms order more steel, so demand and price for steel rise">${chDraw({ a: 1, b: 1, c: 1, d: 1 })}</svg>`;

/* ---------- joint supply chain ---------- */
function jsDraw(s) {
  const ar = (x1, x2, y, v) => SV.line(x1, y, x2 - 8, y, "c4", { "stroke-width": 2.5, ...op(v) }) + SV.arrowHead(x2, y, "r", "dot4");
  let o = bx(20, 20, 190, "Demand for beef rises", s.a, "f3") + ar(212, 260, 43, s.a) + bx(262, 20, 190, "Beef price and output rise", s.b) + ar(454, 502, 43, s.b);
  o += bx(504, 20, 230, "Movement along beef supply", s.b, "f1");
  o += SV.line(357, 68, 357, 112, "c4", { "stroke-width": 2.5, ...op(s.c) }) + SV.arrowHead(357, 120, "d", "dot4") + bx(20, 124, 200, "More hides are produced", s.c);
  o += ar(222, 262, 147, s.d) + bx(264, 124, 190, "Leather supply shifts right", s.d, "f2") + ar(456, 502, 147, s.e) + bx(504, 124, 230, "Leather price falls", s.e, "f1");
  return o;
}
Lib.stepper($("#stJ"), { w: 760, h: 190, label: "Joint supply of beef and leather", base: { a: 0, b: 0, c: 0, d: 0, e: 0 }, draw: jsDraw, tween: 700, dwell: 4800, steps: [
  { cap: "<b>Demand for beef rises.</b> This is the main product, and the first change in the chain.", s: { a: 1 } },
  { cap: "<b>Beef price and output rise.</b> Farmers move along their beef supply curve.", s: { a: 1, b: 1 } },
  { cap: "<b>More cattle are slaughtered,</b> so more hides are produced as a by-product.", s: { a: 1, b: 1, c: 1 } },
  { cap: "<b>The supply of leather shifts right</b> at every price, because the hides come with the beef.", s: { a: 1, b: 1, c: 1, d: 1 } },
  { cap: "<b>The price of leather falls</b> and the quantity rises, with no change in demand for leather.", s: { a: 1, b: 1, c: 1, d: 1, e: 1 } },
] });

/* ---------- Lab 1 ---------- */
const REL = [
  ["Complements (joint demand)", "price of the first good", "Demand", -0.6, "A rise in the price of a complement lowers demand for this good."],
  ["Substitutes (alternative demand)", "price of the first good", "Demand", 0.6, "A rise in the price of a substitute raises demand for this good."],
  ["Derived demand", "demand for the final product", "Demand", 0.6, "More demand for the final product raises demand for the input."],
  ["Joint supply", "demand for the main product", "Supply", 0.6, "More of the main product means more of the by-product at every price."],
];
let relI = 0;
function labR() {
  if (!$("#rr")) return;
  const [nm, trig, curve, k, why] = REL[relI], t = +$("#rr").value, sh = Math.max(-30, Math.min(30, k * t)), d = curve === "Demand" ? sh : 0, s = curve === "Supply" ? sh : 0, e = sdEq(d, s), e0 = sdEq(0, 0);
  $$("#relB button").forEach((b, k2) => b.classList.toggle("pri", k2 === relI));
  $("#r1").textContent = Math.abs(sh) < 0.5 ? "Nothing" : curve + (sh > 0 ? " right" : " left"); $("#r2").textContent = "$" + Lib.fmtN(e.p, 0); $("#r3").textContent = Lib.fmtN(e.q, 0);
  $("#rv").textContent = Math.abs(sh) < 0.5 ? `The ${trig} is unchanged, so the second market does not move.` : `${nm}: a ${t > 0 ? "rise" : "fall"} of ${Math.abs(t)}% in the ${trig}. ${why} The curve moves ${sh > 0 ? "right" : "left"}, so the price ${e.p > e0.p ? "rises" : "falls"} and the quantity ${e.q > e0.q ? "rises" : "falls"} in the second market.`.replace(why, t > 0 ? why : "The opposite happens: " + why.charAt(0).toLowerCase() + why.slice(1));
  $("#labA").innerHTML = sdPlot({ d, s, g: 1, n: 1 });
}
$("#relB").innerHTML = REL.map((r, i) => `<button class="b" data-i="${i}">${r[0]}</button>`).join("");
$$("#relB button").forEach((b) => (b.onclick = () => { relI = +b.dataset.i; labR(); }));
Lib.slider($("#g1"), { id: "rr", label: "Change in the trigger, % ", min: -30, max: 30, step: 5, value: 20, fmt: (v) => v + "%", onInput: labR });
labR();

/* ---------- Lab 2 ---------- */
function labX() {
  if (!$("#xp") || !$("#xq")) return;
  const p = +$("#xp").value, q = +$("#xq").value, x = p === 0 ? 0 : q / p, a = Math.abs(x);
  $("#t1").textContent = (x > 0 ? "+" : "") + Lib.fmtN(x, 2); $("#t2").textContent = a < 0.05 ? "Unrelated" : x > 0 ? "Substitutes" : "Complements"; $("#t3").textContent = a < 0.05 ? "None" : a < 1 ? "Weak" : "Strong";
  $("#tv").textContent = a < 0.05 ? `A ${p}% price rise leaves demand unchanged, so XED is about zero and the goods are unrelated.` : `XED = ${q}% ÷ ${p}% = ${x > 0 ? "+" : ""}${Lib.fmtN(x, 2)}. ${x > 0 ? "Positive, so the goods are substitutes" : "Negative, so the goods are complements"}; ${a < 1 ? "the value is below 1 in size, so the link is fairly weak." : "the value is above 1 in size, so the link is strong."}`;
  const X = (v) => 30 + (v + 3) * 60, mx = Math.max(-3, Math.min(3, x));
  let o = SV.line(30, 100, 390, 100) + [-3, -2, -1, 0, 1, 2, 3].map((v) => SV.line(X(v), 94, X(v), 106) + SV.text(X(v), 124, (v > 0 ? "+" : "") + v, "sm", { "text-anchor": "middle" })).join("");
  o += SV.text(X(-1.5), 70, "Complements", "lbl bd", { "text-anchor": "middle" }) + SV.text(X(1.5), 70, "Substitutes", "lbl bd", { "text-anchor": "middle" }) + SV.circle(X(mx), 100, 9, "dot3") + SV.text(X(mx), 82, (x > 0 ? "+" : "") + Lib.fmtN(x, 2), "lbl bd", { "text-anchor": "middle", ...halo });
  $("#labB").innerHTML = o;
}
Lib.slider($("#g2"), { id: "xp", label: "% change in the price of good X ", min: 5, max: 30, step: 5, value: 10, fmt: (v) => v + "%", onInput: labX });
Lib.slider($("#g3"), { id: "xq", label: "% change in quantity demanded of good Y ", min: -30, max: 30, step: 1, value: 14, fmt: (v) => v + "%", onInput: labX });
labX();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "How are the two goods related?", buckets: [{"label": "Complements"}, {"label": "Substitutes"}, {"label": "Unrelated"}], items: [{"text": "Cars and petrol", "b": 0}, {"text": "Tea and coffee", "b": 1}, {"text": "Printers and ink cartridges", "b": 0}, {"text": "Bus travel and train travel", "b": 1}, {"text": "Butter and margarine", "b": 1}, {"text": "Bread and butter", "b": 0}, {"text": "A guitar and a bag of rice", "b": 2}, {"text": "Smartphones and mobile data", "b": 0}], done: "Used together: complements. Replace each other: substitutes. No link: unrelated." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Joint demand", "Goods used together, so demand moves together"], ["Alternative demand", "Goods that can replace each other"], ["Derived demand", "Demand for an input that comes from demand for the final good"], ["Joint supply", "Producing one good also produces another"], ["Positive XED", "Substitutes"], ["Negative XED", "Complements"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the joint supply chain in order.", items: ["Demand for beef rises", "Beef price and output rise", "More hides are produced", "The supply of leather shifts to the right", "The price of leather falls"], done: "A by-product's supply shifts when the main product's output changes." });
Lib.calc($("#c1"), { qs: [
  {"q": "The price of rice rises 10% and demand for bread rises 14%. What is the cross elasticity of demand?", "a": 1.4, "unit": "", "tol": 0.05, "hint": "14 ÷ 10.", "sol": "<b>+1.4</b>: strong substitutes."},
  {"q": "The price of butter rises 10% and demand for bread falls 7%. What is the cross elasticity (include the sign)?", "a": -0.7, "unit": "", "tol": 0.05, "hint": "−7 ÷ 10.", "sol": "<b>−0.7</b>: weaker complements."},
  {"q": "XED between two goods is +0.4. The price of one rises 15%. By what % does demand for the other change?", "a": 6, "unit": "%", "tol": 0.2, "hint": "0.4 × 15.", "sol": "<b>+6%</b>."},
  {"q": "XED of cars with respect to petrol is −0.5. Petrol prices rise 40%. What is the % change in demand for cars (include the sign)?", "a": -20, "unit": "%", "tol": 0.5, "hint": "−0.5 × 40.", "sol": "<b>−20%</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A positive cross elasticity of demand means the goods are:", opts: ["Substitutes", "Complements", "Unrelated", "Inferior"], a: 0, why: "Positive XED: substitutes." },
  { q: "A rise in the price of a complement:", opts: ["Lowers demand for this good", "Raises demand for this good", "Raises supply of this good", "Has no effect"], a: 0, why: "Used together." },
  { q: "Demand for steel is an example of:", opts: ["Derived demand", "Joint supply", "Alternative demand", "Effective demand"], a: 0, why: "Steel is demanded because of what it makes." },
  { q: "Beef and leather are an example of:", opts: ["Joint supply", "Joint demand", "Derived demand", "Alternative demand"], a: 0, why: "Leather is a by-product." },
  { q: "XED = +3 compared with +0.5 shows:", opts: ["A closer substitute", "A weaker substitute", "A complement", "An inferior good"], a: 0, why: "A larger positive value means a stronger link." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Joint demand", "Complements: used together."],
  ["Alternative demand", "Substitutes: replace each other."],
  ["Derived demand", "Input demand comes from final demand."],
  ["Joint supply", "By-products: one output brings another."],
  ["XED formula", "% change Qd of A ÷ % change price of B."],
  ["Positive XED", "Substitutes."],
  ["Negative XED", "Complements."],
  ["Zero XED", "Unrelated."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "What is the measure of cross-elasticity of demand for good X in terms of good Y? (Feb/March 2022 · 12 · Q8, reworded)", opts: ["the change in the demand for X divided by the change in the price of Y", "the change in the price of X divided by the change in the demand for Y", "the percentage change in the demand for X divided by the percentage change in the price of Y", "the percentage change in the demand for Y divided by the percentage change in the price of X"], a: 2, why: "XED of X with respect to Y is the percentage change in demand for X divided by the percentage change in the price of Y." },
  { q: "Which row correctly describes the relationship between two goods implied by the value of the cross elasticity of demand? (May/June 2023 · 11 · Q5, reworded)", opts: ["−2.0: weak complements", "−0.5: weak substitutes", "+0.5: weak substitutes", "+2.0: strong complements"], a: 2, why: "A positive value means substitutes and a value near zero means a weak link. A negative value means complements." },
  { q: "Following the introduction of a 10% increase in charges for car parking in a city centre, the demand for bus journeys per day into the city rose from 800 to 1000. What was the cross elasticity of demand for bus journeys with respect to car parking charges? (May/June 2020 · 12 · Q8, reworded)", opts: ["−0.4", "+0.4", "+2.0", "+2.5"], a: 3, why: "Quantity demanded rose 25% (200 ÷ 800) and the price rose 10%, so XED = +25 ÷ 10 = +2.5." },
  { q: "The cross elasticity of demand between bus travel and rail travel is +2. A rise in the price of bus fares caused the demand for rail travel to rise by 10%. Which change in bus fares would have caused this? (May/June 2023 · 12 · Q8, reworded)", opts: ["from 20 cents to 21 cents", "from 30 cents to 33 cents", "from 40 cents to 45 cents", "from 50 cents to 60 cents"], a: 0, why: "A 10% rise in rail demand with XED +2 needs a 5% rise in bus fares, which is 20 to 21." },
  { q: "The cross-elasticity of demand of good S with respect to the price of good P is +1.5. The cross-elasticity of demand of good S with respect to the price of good R is −1.5. The cross-elasticity of demand of good P with respect to the price of good R is −1.5. What can be concluded about goods P, R and S? (May/June 2022 · 12 · Q10, reworded)", opts: ["S and P are complements; P and R are substitutes", "S and P are complements; R is an inferior good", "S and P are substitutes; P and R are complements", "S and P are substitutes; R is an inferior good"], a: 2, why: "Positive values mean substitutes (S and P) and negative values mean complements (S and R, P and R)." },
  { q: "Which reason for the increase in demand for a smartphone is an example of joint demand? (May/June 2024 · 12 · Q11, reworded)", opts: ["a fall in its price", "a fall in the price of connecting to a network", "a fall in the price of parts used to make smartphones", "a rise in the price of a substitute"], a: 1, why: "Network connection is a complement, so its price falling raises demand for the phone." },
  { q: "Goods X and Y are complements and have upward-sloping supply curves. What will be the effect on the equilibrium price and quantity of good X of an increase in the supply of good Y? (May/June 2022 · 14 · Q5, reworded)", opts: ["price decreases, quantity decreases", "price increases, quantity decreases", "price decreases, quantity increases", "price increases, quantity increases"], a: 3, why: "Cheaper Y raises demand for X, so price and quantity of X both rise." },
  { q: "What does joint supply mean? (May/June 2023 · 13 · Q9, reworded)", opts: ["A firm can choose between producing a range of different goods", "A good has multiple uses", "A good is a by-product of the production process of another good", "Consumers consider two goods as complements"], a: 2, why: "Joint supply is where a by-product is produced with the main product." },
  { q: "Butter and buttermilk are goods in joint supply. Supply curves in both markets slope upwards to the right. Health concerns cause people to reduce their consumption of butter. What are the initial consequences of this for supply in the markets for butter and buttermilk? (Feb/March 2023 · 12 · Q11, reworded)", opts: ["butter: move left along supply curve; buttermilk: move left along supply curve", "butter: move left along supply curve; buttermilk: shift left of the supply curve", "butter: shift left of the supply curve; buttermilk: move left along supply curve", "butter: shift left of the supply curve; buttermilk: shift left of the supply curve"], a: 1, why: "Lower butter demand cuts the price, a movement along butter's supply. Less butter means less buttermilk at every price, a left shift of its supply." },
  { q: "Butter is a normal good. It is in joint demand with bread and in joint supply with buttermilk. The demand for butter increases because of a rise in consumer incomes. What are the effects of this increase on the prices of bread and buttermilk? (Feb/March 2024 · 12 · Q10, reworded)", opts: ["bread price decreases, buttermilk price decreases", "bread price decreases, buttermilk price increases", "bread price increases, buttermilk price decreases", "bread price increases, buttermilk price increases"], a: 2, why: "More butter demand raises bread demand (complement), so bread price rises. Butter output rises, so buttermilk supply rises and its price falls." },
  { q: "Goods X, Y and Z all have downward-sloping demand curves and upward-sloping supply curves. Good X is in joint supply with good Y and in joint demand with good Z. There is an increase in the demand for good X. What will happen to the prices and sales of goods Y and Z? (May/June 2022 · 13 · Q10, reworded)", opts: ["Y: price falls, sales fall; Z: price rises, sales rise", "Y: price falls, sales rise; Z: price rises, sales rise", "Y: price rises, sales fall; Z: price falls, sales rise", "Y: price rises, sales rise; Z: price falls, sales fall"], a: 1, why: "More X means more of its by-product Y, so Y's supply rises (price falls, sales rise). Z is a complement of X, so demand for Z rises (price and sales rise)." },
  { q: "Which pair of products are substitutes both in consumption and production? (May/June 2023 · 12 · Q6, reworded)", opts: ["barley and cotton", "gold and silver", "soap and toothpaste", "spinach and cabbage"], a: 3, why: "Consumers can replace one leafy vegetable with another and farmers can switch land between them." },
] });
