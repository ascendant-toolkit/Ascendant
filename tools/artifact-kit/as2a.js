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

const xLab = { x: "Quantity of X", y: "Price of X", D1: "D1", D2: "D2", S1: "S", S2: "S", P1: "P1", Q1: "Q1", P2: "P2", Q2: "Q2" };
function xDraw(s) { return sdPlot({ d: s.d, s: 0, g: 1, n: s.n }, xLab); }
$("#pic1").innerHTML = (() => {
  const X = (v) => 70 + (v + 3) * 100, Y = (q) => 250 - (q + 60) * 1.6;
  let o = axes(70, 250, 700, 25, "XED", "% change in demand for X (price of Y +10%)");
  o += SV.line(X(-3), Y(-30), X(3), Y(30), "c2", { "stroke-width": 3 }) + SV.line(X(0), 250, X(0), 40, "dash");
  o += SV.text(X(1.5), Y(5), "Substitutes (XED > 0)", "lbl bd", { "text-anchor": "middle" }) + SV.text(X(-1.5), Y(-5), "Complements (XED < 0)", "lbl bd", { "text-anchor": "middle" }) + SV.text(X(0) + 6, 52, "Unrelated", "sm");
  return `<svg viewBox="0 0 760 270" role="img" aria-label="The change in demand for X against XED: positive for substitutes, negative for complements">${o}</svg>`;
})();
Lib.stepper($("#stA"), { w: 760, h: 300, label: "The price of a substitute rises, so demand for X rises", base: { d: 0, n: 0 }, draw: xDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>Start.</b> The market for good X is in equilibrium at a price of 50 and a quantity of 50.", s: { d: 0, n: 0 } },
  { cap: "<b>The price of a substitute (Y) rises.</b> XED is positive, so consumers switch to X and the demand curve for X shifts right.", s: { d: 20, n: 1 } },
  { cap: "<b>The price of X rises</b> to 58 and the quantity to 60.", s: { d: 20, n: 1 } },
] });
Lib.stepper($("#stB"), { w: 760, h: 300, label: "The price of a complement rises, so demand for X falls", base: { d: 0, n: 0 }, draw: xDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>Start.</b> The same market for good X.", s: { d: 0, n: 0 } },
  { cap: "<b>The price of a complement (Y) rises.</b> XED is negative, so the combined cost of using X and Y rises and the demand curve for X shifts left.", s: { d: -20, n: 1 } },
  { cap: "<b>The price of X falls</b> to 42 and the quantity to 40.", s: { d: -20, n: 1 } },
] });

function labA() {
  if (!["g1v", "g2v"].every((i) => $("#" + i))) return;
  const x = +$("#g1v").value / 10, pc = +$("#g2v").value, qc = x * pc;
  $("#r1").textContent = (qc >= 0 ? "+" : "") + Lib.fmtN(qc, 1) + "%"; $("#r2").textContent = Math.abs(x) < 0.05 ? "Unrelated" : (x > 0 ? "Substitutes" : "Complements") + (Math.abs(x) >= 1 ? " (close)" : " (weak)");
  const bar = (yy, lab, v, c) => SV.text(20, yy + 15, lab, "sm") + SV.rect(150, yy, Math.abs(v) * 8, 22, c, op(0.7)) + SV.text(156 + Math.abs(v) * 8, yy + 16, (v >= 0 ? "+" : "") + Lib.fmtN(v, 1) + "%", "lbl bd");
  $("#labA").innerHTML = bar(30, "Price of Y", pc, "f3") + bar(90, "Demand for X", qc, "f1");
  $("#rv").textContent = Math.abs(x) < 0.05 ? "XED is about zero: the price of Y does not affect demand for X." : `With XED of ${Lib.fmtN(x, 1)}, a ${pc >= 0 ? "rise" : "fall"} of ${Math.abs(pc)}% in the price of Y changes demand for X by ${Lib.fmtN(qc, 1)}%. ` + (x > 0 ? "The goods are substitutes: consumers switch between them." : "The goods are complements: they are used together.");
}
Lib.slider($("#g1"), { id: "g1v", label: "XED × 10 ", min: -20, max: 20, step: 2, value: 12, fmt: (v) => Lib.fmtN(v / 10, 1), onInput: labA });
Lib.slider($("#g2"), { id: "g2v", label: "Change in the price of Y, % ", min: -10, max: 10, step: 2, value: 10, fmt: (v) => (v > 0 ? "+" : "") + v + "%", onInput: labA });
labA();

chooser("h", [
  ["Two rival smartphone brands", "Large and positive", "Demand for the other rises sharply", "Predict the effect of a rival's price cut", 5],
  ["Bread and rice", "Moderate and positive", "Demand for bread rises somewhat", "Weak competition; monitor rice prices", 3],
  ["Printers and ink", "Large and negative", "Demand for ink falls sharply", "Price the printer low and ink high", 5],
  ["Bread and butter", "Small and negative", "Demand for bread falls slightly", "Little effect on pricing", 2],
  ["Cars and pencils", "About zero", "No change", "No link to use in pricing", 1],
  ["Tea and coffee", "Positive", "Demand for the other rises", "Watch each other's price changes", 3]
], (it) => `${it[0]}: XED is likely to be ${it[1].toLowerCase()}. If the price of one rises, ${it[2].toLowerCase()}. For a firm: ${it[3].toLowerCase()}.`, "Strength of the link");
Lib.classify($("#cl1"), { prompt: "Are the goods more likely to be substitutes or complements?", buckets: [{"label": "Substitutes (positive XED)"}, {"label": "Complements (negative XED)"}], items: [{"text": "Tea and coffee", "b": 0}, {"text": "Printers and ink cartridges", "b": 1}, {"text": "Two rival car brands", "b": 0}, {"text": "Cars and petrol", "b": 1}, {"text": "Butter and margarine", "b": 0}, {"text": "Bread and butter", "b": 1}, {"text": "Bus and train travel", "b": 0}, {"text": "Games consoles and games", "b": 1}], done: "Substitutes replace each other; complements are used together." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["XED", "% change in Q of X ÷ % change in price of Y"], ["Substitutes", "Positive cross elasticity"], ["Complements", "Negative cross elasticity"], ["Close substitutes", "A large positive XED"], ["Unrelated goods", "XED close to zero"], ["Joint demand", "Goods used together, such as printers and ink"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the effects of a rise in the price of a substitute in order.", items: ["The price of good Y rises", "Consumers switch to good X", "The demand curve for X shifts right", "The price and quantity of X rise"], done: "Price of the substitute up, demand for X up, shift right." });
Lib.calc($("#c1"), { qs: [
  {"q": "The price of Y rises by 10% and demand for X rises by 6%. What is XED?", "a": 0.6, "unit": "", "tol": 0.01, "hint": "6 ÷ 10.", "sol": "<b>+0.6</b>, substitutes."},
  {"q": "XED is -1.5 and the price of Y rises by 4%. By what % does demand for X change?", "a": -6, "unit": "%", "tol": 0.1, "hint": "-1.5 × 4.", "sol": "<b>-6%</b>."},
  {"q": "XED is +2.0 and the price of Y falls by 5%. By what % does demand for X change?", "a": -10, "unit": "%", "tol": 0.1, "hint": "2.0 × -5.", "sol": "<b>-10%</b>."},
  {"q": "The price of Y rises from $4 to $5 and demand for X falls from 200 to 170. What is XED?", "a": -0.6, "unit": "", "tol": 0.01, "hint": "% change in Q = -15%; in price = +25%.", "sol": "<b>-0.6</b>, complements."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A positive XED means the goods are:", opts: ["Substitutes", "Complements", "Unrelated", "Inferior"], a: 0, why: "Demand rises when the other's price rises." },
  { q: "A negative XED means the goods are:", opts: ["Complements", "Substitutes", "Normal", "Luxuries"], a: 0, why: "Used together." },
  { q: "A larger size of XED suggests:", opts: ["A closer relationship", "A weaker relationship", "No relationship", "An inferior good"], a: 0, why: "Closer links, bigger responses." },
  { q: "XED measures the response of demand to:", opts: ["The price of another good", "Income", "The good's own price", "Supply"], a: 0, why: "The 'cross' price." },
  { q: "If the price of a complement rises, demand for X:", opts: ["Falls", "Rises", "Is unchanged", "Becomes perfectly elastic"], a: 0, why: "The pair costs more." },
] });
Lib.cards($("#fc1"), { cards: [
  ["XED formula", "%ΔQ of X ÷ %ΔP of Y."],
  ["Positive XED", "Substitutes."],
  ["Negative XED", "Complements."],
  ["Zero XED", "Unrelated."],
  ["Large size", "Close relationship."],
  ["Substitute price up", "Demand for X shifts right."],
  ["Complement price up", "Demand for X shifts left."],
  ["Business use", "Predict rivals' effects, price complements."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "What is the measure of cross-elasticity of demand for good X in terms of good Y? (Feb/March 2022 · 12 · Q8, reworded)", opts: ["the change in the demand for X divided by the change in the price of Y", "the change in the price of X divided by the change in the demand for Y", "the percentage change in the demand for X divided by the percentage change in the price of Y", "the percentage change in the demand for Y divided by the percentage change in the price of X"], a: 2, why: "XED of X with respect to Y is the % change in demand for X over the % change in the price of Y." },
  { q: "Following the introduction of a 10% increase in charges for car parking in a city centre, the demand for bus journeys per day into the city rose from 800 to 1000. What was the cross elasticity of demand for bus journeys with respect to car parking charges? (May/June 2020 · 12 · Q8, reworded)", opts: ["-0.4", "+0.4", "+2.0", "+2.5"], a: 3, why: "Demand rose by 25% and the price rose by 10%, so XED = 25 ÷ 10 = +2.5." },
  { q: "A government introduces a subsidy for product X and the market price of X falls by 5%. The cross elasticity of demand for product Y with respect to the price of X is +0.4. What will happen to the demand for product Y? (May/June 2021 · 11 · Q10, reworded)", opts: ["It will decrease by 2%.", "It will decrease by 12.5%.", "It will increase by 2%.", "It will increase by 12.5%."], a: 0, why: "0.4 × (-5%) = -2%, so demand for Y falls by 2%." },
  { q: "What can be concluded about a good with a positive cross-price elasticity of demand? (May/June 2022 · 11 · Q13, reworded)", opts: ["Its price will be sensitive to changes in prices of close substitutes.", "Its price will be sensitive to changes in quantity demanded of close substitutes.", "The quantity demanded for this good will be sensitive to changes in prices of close substitutes.", "The quantity demanded for this good will be sensitive to changes in quantity demanded of close substitutes."], a: 2, why: "Positive XED means substitutes; the quantity demanded responds to the price of the substitute." },
  { q: "The price elasticity of demand for good X is -2.4, its income elasticity of demand is -0.4 and the cross elasticity of demand for good X with respect to good Y is +0.8. What is the correct description of good X? (Feb/March 2024 · 12 · Q7, reworded)", opts: ["inferior good, price-elastic demand and substitute for good Y", "inferior good, price-inelastic demand and complement to good Y", "normal good, price-elastic demand and complement to good Y", "normal good, price-inelastic demand and substitute for good Y"], a: 0, why: "XED positive: substitute for Y; YED negative: inferior; PED size 2.4: elastic." },
  { q: "Good X is related to good Y. Incomes increase and the price of good Y falls. Which combination would give the greatest increase in demand for good X? (nature of good X, relationship between X and Y) (Feb/March 2020 · 12 · Q8, reworded)", opts: ["inferior good, complements", "inferior good, substitutes", "normal good, complements", "normal good, substitutes"], a: 2, why: "X is normal, so higher income raises demand, and a fall in the price of a complement also raises it." },
] });
