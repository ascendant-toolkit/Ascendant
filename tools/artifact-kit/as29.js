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

const incLab = { x: "Quantity", y: "Price", D1: "D1", D2: "D2", S1: "S", S2: "S", P1: "P1", Q1: "Q1", P2: "P2", Q2: "Q2" };
function inDraw(s) { return sdPlot({ d: s.d, s: 0, g: 1, n: s.n }, incLab); }
$("#pic1").innerHTML = (() => {
  const X = (v) => 70 + v * 6, Y = (q) => 250 - q * 2;
  let o = axes(70, 250, 700, 25, "Income", "Quantity demanded");
  o += SV.line(X(0), Y(20), X(100), Y(95), "c2", { "stroke-width": 3 }) + tag(X(100) + 4, Y(95), "Luxury (YED > 1)", "c2");
  o += SV.line(X(0), Y(30), X(100), Y(55), "c1", { "stroke-width": 3 }) + tag(X(100) + 4, Y(55), "Necessity (0 to 1)", "c1");
  o += SV.line(X(0), Y(80), X(100), Y(30), "c3", { "stroke-width": 3 }) + tag(X(100) + 4, Y(30), "Inferior (YED < 0)", "c3");
  return `<svg viewBox="0 0 760 270" role="img" aria-label="Quantity demanded against income for a luxury, a necessity and an inferior good">${o}</svg>`;
})();
Lib.stepper($("#stA"), { w: 760, h: 300, label: "A rise in income increases demand for a normal good", base: { d: 0, n: 0 }, draw: inDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>Start.</b> Demand and supply for a normal good meet at a price of 50 and a quantity of 50.", s: { d: 0, n: 0 } },
  { cap: "<b>Incomes rise.</b> YED is positive, so demand increases and the demand curve shifts right.", s: { d: 20, n: 1 } },
  { cap: "<b>The equilibrium moves</b> to a higher price (58) and quantity (60).", s: { d: 20, n: 1 } },
] });
Lib.stepper($("#stB"), { w: 760, h: 300, label: "A rise in income decreases demand for an inferior good", base: { d: 0, n: 0 }, draw: inDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>Start.</b> The same market, now for an inferior good.", s: { d: 0, n: 0 } },
  { cap: "<b>Incomes rise.</b> YED is negative: consumers switch to better goods, so demand falls and the curve shifts left.", s: { d: -20, n: 1 } },
  { cap: "<b>The equilibrium moves</b> to a lower price (42) and quantity (40).", s: { d: -20, n: 1 } },
] });

function labA() {
  if (!["g1v", "g2v"].every((i) => $("#" + i))) return;
  const y = +$("#g1v").value / 10, ic = +$("#g2v").value, qc = y * ic;
  $("#r1").textContent = (qc >= 0 ? "+" : "") + Lib.fmtN(qc, 1) + "%"; $("#r2").textContent = y < 0 ? "Inferior" : y < 1 ? "Normal (necessity)" : "Normal (luxury)";
  const bar = (yy, lab, v, c) => SV.text(20, yy + 15, lab, "sm") + SV.rect(150, yy, Math.abs(v) * 8, 22, c, op(0.7)) + SV.text(156 + Math.abs(v) * 8, yy + 16, (v >= 0 ? "+" : "") + Lib.fmtN(v, 1) + "%", "lbl bd");
  $("#labA").innerHTML = bar(30, "Income", ic, "f3") + bar(90, "Quantity", qc, "f1");
  $("#rv").textContent = `With YED of ${Lib.fmtN(y, 1)} a ${ic >= 0 ? "rise" : "fall"} of ${Math.abs(ic)}% in income changes quantity demanded by ${Lib.fmtN(qc, 1)}%. ` + (y < 0 ? "The good is inferior: demand moves in the opposite direction to income." : y < 1 ? "The good is a necessity: demand changes by a smaller percentage than income." : "The good is a luxury: demand changes by a larger percentage than income.");
}
Lib.slider($("#g1"), { id: "g1v", label: "YED × 10 ", min: -15, max: 30, step: 5, value: 20, fmt: (v) => Lib.fmtN(v / 10, 1), onInput: labA });
Lib.slider($("#g2"), { id: "g2v", label: "Change in income, % ", min: -10, max: 10, step: 2, value: 6, fmt: (v) => (v > 0 ? "+" : "") + v + "%", onInput: labA });
labA();

chooser("h", [
  ["Foreign holidays", "Above +1 (luxury)", "Demand rises strongly", "Demand falls sharply", 5],
  ["Basic food (bread, rice)", "0 to +1 (necessity)", "Demand rises slightly", "Demand barely falls", 2],
  ["Own-brand budget goods", "Below 0 (inferior)", "Demand falls", "Demand rises", 3],
  ["New cars", "Above +1 (luxury)", "Demand rises strongly", "Demand falls sharply", 5],
  ["Restaurant meals", "Above +1", "Demand rises", "Demand falls", 4],
  ["Public bus travel (for some)", "Below 0 (may be inferior)", "May fall as people buy cars", "May rise", 2]
], (it) => `${it[0]}: likely YED is ${it[1].toLowerCase()}. In a boom, ${it[2].toLowerCase()}; in a recession, ${it[3].toLowerCase()}.`, "Strength of the response to income");
Lib.classify($("#cl1"), { prompt: "Is the good more likely to be normal or inferior?", buckets: [{"label": "Normal good"}, {"label": "Inferior good"}], items: [{"text": "Foreign holidays", "b": 0}, {"text": "Own-brand budget cereal", "b": 1}, {"text": "Designer clothes", "b": 0}, {"text": "Cheap instant noodles", "b": 1}, {"text": "New cars", "b": 0}, {"text": "Low-quality own-label ready meals", "b": 1}, {"text": "Restaurant meals", "b": 0}, {"text": "Basic bread", "b": 0}], done: "Normal goods are bought more as income rises; inferior goods are bought less because better alternatives become affordable. Basic bread is usually a normal necessity." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["YED", "% change in quantity demanded ÷ % change in income"], ["Normal good", "YED is positive"], ["Inferior good", "YED is negative"], ["Luxury", "YED is above 1"], ["Necessity", "YED is between 0 and 1"], ["Income elastic", "Quantity changes by a greater percentage than income"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the effects of a rise in income on a normal good in order.", items: ["Incomes rise", "Demand for the normal good increases", "The demand curve shifts right", "Equilibrium price and quantity rise"], done: "Income up, demand up, shift right, price and quantity up." });
Lib.calc($("#c1"), { qs: [
  {"q": "Income rises by 5% and quantity demanded rises by 15%. What is YED?", "a": 3, "unit": "", "tol": 0.05, "hint": "15 ÷ 5.", "sol": "<b>3</b>, a luxury."},
  {"q": "YED is -0.5 and income rises by 8%. By what % does quantity demanded change?", "a": -4, "unit": "%", "tol": 0.1, "hint": "-0.5 × 8.", "sol": "<b>-4%</b>."},
  {"q": "YED is +0.4 and income falls by 10%. By what % does quantity demanded change?", "a": -4, "unit": "%", "tol": 0.1, "hint": "0.4 × -10.", "sol": "<b>-4%</b>."},
  {"q": "Income rises from $2000 to $2200 and quantity demanded rises from 50 to 60. What is YED?", "a": 2, "unit": "", "tol": 0.05, "hint": "% change in Q = 20%; in income = 10%.", "sol": "<b>2</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A negative YED means the good is:", opts: ["Inferior", "Normal", "A luxury", "A necessity"], a: 0, why: "Demand falls as income rises." },
  { q: "A YED of +1.8 suggests:", opts: ["A luxury", "A necessity", "An inferior good", "Unit elastic demand"], a: 0, why: "Above one." },
  { q: "In a recession, demand for an inferior good is likely to:", opts: ["Rise", "Fall", "Stay the same", "Disappear"], a: 0, why: "People trade down." },
  { q: "YED = ", opts: ["% change in Q demanded ÷ % change in income", "% change in Q ÷ % change in price", "Change in income ÷ change in Q", "Price × quantity"], a: 0, why: "The YED formula." },
  { q: "A rise in income shifts the demand curve for a normal good:", opts: ["Right", "Left", "Not at all", "Up only"], a: 0, why: "Demand increases." },
] });
Lib.cards($("#fc1"), { cards: [
  ["YED formula", "%ΔQd ÷ %Δincome."],
  ["Normal good", "Positive YED."],
  ["Inferior good", "Negative YED."],
  ["Necessity", "0 to +1."],
  ["Luxury", "Above +1."],
  ["Income rises, normal", "Demand shifts right."],
  ["Income rises, inferior", "Demand shifts left."],
  ["Business use", "Forecast sales through the cycle."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "A firm calculates that the income elasticity of demand for its product is -3.0. What can be deduced from this information? (May/June 2024 · 11 · Q10, reworded)", opts: ["In a period of economic growth, its total revenue should increase.", "In a period of economic recession, its total revenue should increase.", "It has few substitutes so it should increase its price to increase total revenue.", "It has many substitutes so it should decrease price to increase total revenue."], a: 1, why: "A negative YED means an inferior good: demand rises when incomes fall." },
  { q: "The price elasticity of demand for good X is -2.4, its income elasticity of demand is -0.4 and the cross elasticity of demand for good X with respect to good Y is +0.8. What is the correct description of good X? (Feb/March 2024 · 12 · Q7, reworded)", opts: ["inferior good, price-elastic demand and substitute for good Y", "inferior good, price-inelastic demand and complement to good Y", "normal good, price-elastic demand and complement to good Y", "normal good, price-inelastic demand and substitute for good Y"], a: 0, why: "YED negative: inferior; PED size 2.4: elastic; XED positive: substitute." },
  { q: "What causes the demand curve for an inferior good to shift to the right? (Feb/March 2022 · 12 · Q12, reworded)", opts: ["a decrease in consumer incomes", "a decrease in income tax", "a decrease in the price of a substitute good", "a decrease in the price of the good"], a: 0, why: "Demand for an inferior good rises when incomes fall." },
  { q: "Which combination of the classification of a good and market change will cause the demand curve for the good to shift right? (classification, market change) (May/June 2020 · 13 · Q10, reworded)", opts: ["inferior good, income decrease", "inferior good, price decrease", "normal good, income decrease", "normal good, price decrease"], a: 0, why: "A fall in income raises demand for an inferior good. A price change is a movement along the curve." },
  { q: "Good X is related to good Y. Incomes increase and the price of good Y falls. Which combination would give the greatest increase in demand for good X? (nature of good X, relationship between X and Y) (Feb/March 2020 · 12 · Q8, reworded)", opts: ["inferior good, complements", "inferior good, substitutes", "normal good, complements", "normal good, substitutes"], a: 2, why: "A normal good gains from higher income, and a fall in the price of a complement raises demand for X." },
  { q: "The government redistributes income by raising the top rate of income tax and using the money raised to finance additional benefits to students and the unemployed. Under which conditions will total spending in the economy increase the most? (YED of top-rate taxpayers, YED of students and the unemployed) (Feb/March 2021 · 12 · Q16, reworded)", opts: [">1 and >1", ">1 and <1", "<1 and >1", "<1 and <1"], a: 2, why: "Spending falls little where taxpayers' YED is low and rises most where recipients' YED is high." },
] });
