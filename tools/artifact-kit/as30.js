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

/* ---------- static pictures ---------- */
$("#pic1").innerHTML = (() => {
  const B = [["Private good", "Excludable and rival", 30, "f1"], ["Public good", "Non-excludable and non-rival", 270, "f3"], ["Free good", "No opportunity cost", 510, "f2"]];
  let o = ""; B.forEach(([n, d, x, c]) => { o += SV.rect(x, 20, 220, 120, c, { rx: 12, ...op(0.45) }) + SV.text(x + 110, 60, n, "lbl bd", { "text-anchor": "middle", style: "font-size:18px" }) + SV.text(x + 110, 90, d, "sm", { "text-anchor": "middle" }); });
  o += SV.text(380, 175, "Free riders: non-payers cannot be excluded, so a firm earns no revenue and does not supply a public good", "sm", { "text-anchor": "middle" });
  return `<svg viewBox="0 0 760 200" role="img" aria-label="Private good, public good and free good compared">${o}</svg>`;
})();
const meLab = { x: "Quantity", y: "Price", D1: "Perceived demand", D2: "True value", S1: "Supply", S2: "Supply", P1: "P1", Q1: "Qm", P2: "P2", Q2: "Qd" };
function meDraw(d, n) { return sdPlot({ d, s: 0, g: 1, n }, meLab); }
$("#pic2").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="True value above perceived demand for a merit good: the market quantity is below the desirable quantity">${meDraw(20, 1)}</svg>`;
$("#pic3").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="True value below perceived demand for a demerit good: the market quantity is above the desirable quantity">${meDraw(-20, 1)}</svg>`;
const ctlP = (p) => ({ qd: (90 - p) / 0.8, qs: (p - 10) / 0.8 });
function ctlDraw(p, k = 1) {
  const c = ctlP(p); let o = sdPlot({ d: 0, s: 0, g: 1, n: 0 }, { x: "Quantity", y: "Price", D1: "D", S1: "S", P1: "P*", Q1: "Q*" });
  o += SV.line(70, SDY(p), 720, SDY(p), "c3", { "stroke-width": 2.5, ...op(k) }) + tag(724, SDY(p) - 6, (p < 50 ? "Maximum price " : "Minimum price ") + p, "c3", k, "end");
  if (Math.abs(p - 50) > 0.5) o += SV.line(SDX(Math.min(c.qd, c.qs)), SDY(p) + (p < 50 ? 16 : -16), SDX(Math.max(c.qd, c.qs)), SDY(p) + (p < 50 ? 16 : -16), "c4", { "stroke-width": 3, ...op(k) }) + SV.text(SDX((c.qd + c.qs) / 2), SDY(p) + (p < 50 ? 34 : -22), (p < 50 ? "Shortage " : "Surplus ") + Lib.fmtN(Math.abs(c.qd - c.qs), 1), "sm", { "text-anchor": "middle", ...op(k) });
  return o;
}
$("#pic4").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="A maximum price below equilibrium creates a shortage">${ctlDraw(35)}</svg>`;

/* ---------- steppers ---------- */
chainStep("#stA", "The free rider problem", ["A good is provided that nobody can be excluded from using", "Everyone can benefit without paying (free riders)", "Few people pay voluntarily, so a firm earns little revenue", "A private firm makes a loss and does not supply it", "The government provides it and funds it from taxation"], [
  "<b>Non-excludable and non-rival:</b> a street light or flood barrier.", "<b>Free riders:</b> if others pay, you benefit anyway, so why pay?", "<b>Revenue collapses</b> because the firm cannot charge.", "<b>Market failure:</b> the good is not supplied, though its benefit to society exceeds its cost.", "<b>Government provision</b>, with an opportunity cost: the money could be spent elsewhere."]);
Lib.stepper($("#stB"), { w: 760, h: 300, label: "A merit good is under-consumed because consumers undervalue it", base: { d: 0, n: 0 }, draw: (s) => meDraw(s.d, s.n), tween: 900, dwell: 5800, steps: [
  { cap: "<b>Perceived demand and supply</b> give the market quantity Qm: what consumers choose to buy.", s: { d: 0, n: 0 } },
  { cap: "<b>The true value is higher</b> than consumers realise (imperfect information), so the true-value curve lies to the right.", s: { d: 20, n: 1 } },
  { cap: "<b>The desirable quantity Qd is greater than Qm.</b> The gap is the <b>under-consumption</b> that gives the government a reason to intervene.", s: { d: 20, n: 1 } },
] });
Lib.stepper($("#stC"), { w: 760, h: 300, label: "A demerit good is over-consumed because consumers undervalue the harm", base: { d: 0, n: 0 }, draw: (s) => meDraw(s.d, s.n), tween: 900, dwell: 5800, steps: [
  { cap: "<b>Perceived demand and supply</b> give the market quantity Qm.", s: { d: 0, n: 0 } },
  { cap: "<b>The true value is lower</b> than consumers think (they underestimate the harm), so the true-value curve lies to the left.", s: { d: -20, n: 1 } },
  { cap: "<b>The desirable quantity Qd is less than Qm.</b> The gap is the <b>over-consumption</b> that gives the government a reason to intervene.", s: { d: -20, n: 1 } },
] });
chainStep("#stD", "Information failure leads to over-consumption", ["Consumers lack full information about the harm", "They underestimate the risks and the costs to themselves", "They buy more than they would if fully informed", "The market over-provides the demerit good", "The government may provide information, tax or regulate"], [
  "<b>Imperfect information</b> is the root cause.", "<b>Addiction, habit and low prices</b> can make it worse.", "<b>Over-consumption:</b> quantity above the best level.", "<b>Firms</b> supply it because it is profitable.", "<b>Methods</b> are covered in Syllabus 3.2."]);
Lib.stepper($("#stE"), { w: 760, h: 300, label: "A maximum price and a minimum price", base: { p: 50, k: 0 }, draw: (s) => ctlDraw(s.p, s.k), tween: 900, dwell: 5800, steps: [
  { cap: "<b>Free market:</b> equilibrium price 50 and quantity 40.", s: { p: 50, k: 0 } },
  { cap: "<b>A maximum price of 35</b> makes the good affordable (to protect low-income households). It is below equilibrium, so it is effective.", s: { p: 35, k: 1 } },
  { cap: "<b>Result:</b> quantity demanded exceeds quantity supplied, a <b>shortage</b> of 37.5 units: rationing, queues and possible black markets.", s: { p: 35, k: 1 } },
  { cap: "<b>A minimum price of 65</b> supports producers' incomes. It is above equilibrium, so it is effective.", s: { p: 65, k: 1 } },
  { cap: "<b>Result:</b> quantity supplied exceeds quantity demanded, a <b>surplus</b> of 37.5 units, which must be bought, stored or wasted.", s: { p: 65, k: 1 } },
] });

/* ---------- Lab 1 ---------- */
let meMode = 0;
function labA() {
  if (!$("#g1v")) return;
  const m = +$("#g1v").value, d = meMode === 0 ? m : -m, q1 = 50, q2 = 50 + 0.5 * d, gap = Math.abs(q2 - q1);
  $("#r1").textContent = Lib.fmtN(q1, 1); $("#r2").textContent = Lib.fmtN(q2, 1); $("#r3").textContent = Lib.fmtN(gap, 1) + (gap < 0.5 ? "" : meMode === 0 ? " under-consumed" : " over-consumed");
  $("#rv").textContent = gap < 0.5 ? "Consumers judge the good correctly, so the market quantity is about right." : meMode === 0 ? `Consumers underestimate the benefit of a merit good, so the market quantity is ${Lib.fmtN(q1, 1)} but ${Lib.fmtN(q2, 1)} is desirable: under-consumption of ${Lib.fmtN(gap, 1)}.` : `Consumers underestimate the harm of a demerit good, so the market quantity is ${Lib.fmtN(q1, 1)} but ${Lib.fmtN(q2, 1)} is desirable: over-consumption of ${Lib.fmtN(gap, 1)}.`;
  $("#labA").innerHTML = meDraw(d, 1);
}
$("#b1").innerHTML = `<button class="b pri" data-i="0">Merit good (healthcare)</button><button class="b" data-i="1">Demerit good (cigarettes)</button>`;
Lib.slider($("#g1"), { id: "g1v", label: "How far consumers misjudge the value ", min: 0, max: 40, step: 5, value: 20, fmt: (v) => v, onInput: labA });
$$("#b1 button").forEach((b) => (b.onclick = () => { meMode = +b.dataset.i; $$("#b1 button").forEach((x, k) => x.classList.toggle("pri", k === meMode)); labA(); }));
labA();

/* ---------- Lab 2 ---------- */
function labB() {
  if (!["g2v", "g3v", "g4v"].every((i) => $("#" + i))) return;
  const n = +$("#g2v").value, w = +$("#g3v").value, ex = +$("#g4v").value / 100, cost = 200000, ben = n * w, rev = n * ex * w, tax = cost / n;
  $("#t1").textContent = "$" + Lib.fmtN(ben, 0); $("#t2").textContent = "$" + Lib.fmtN(rev, 0); $("#t3").textContent = "$" + Lib.fmtN(tax, 2);
  const mx = Math.max(ben, cost, rev, 1), W = (v) => (v / mx) * 280, bar = (y, lab, v, c) => SV.text(10, y + 15, lab, "sm") + SV.rect(130, y, Math.max(2, W(v)), 22, c, op(0.7));
  $("#labB").innerHTML = bar(20, "Cost", cost, "f3") + bar(70, "Benefit", ben, "f1") + bar(120, "Firm revenue", rev, "f2");
  $("#tv").textContent = ben < cost ? "The benefit to society is below the cost, so providing the good is not worthwhile." : rev >= cost ? `A private firm can charge ${Lib.fmtN(ex * 100, 0)}% of users and collect $${Lib.fmtN(rev, 0)}, enough to cover the cost, so a market could supply it.` : `The benefit ($${Lib.fmtN(ben, 0)}) exceeds the cost ($200 000), but a firm could collect only $${Lib.fmtN(rev, 0)} because most users cannot be made to pay: the free rider problem. A tax of about $${Lib.fmtN(tax, 2)} per person would fund it.`;
}
Lib.slider($("#g2"), { id: "g2v", label: "Number of users ", min: 1000, max: 20000, step: 1000, value: 10000, fmt: (v) => Lib.fmtN(v, 0), onInput: labB });
Lib.slider($("#g3"), { id: "g3v", label: "Value to each user, $ ", min: 5, max: 60, step: 5, value: 40, fmt: (v) => "$" + v, onInput: labB });
Lib.slider($("#g4"), { id: "g4v", label: "Share of users who can be made to pay, % ", min: 0, max: 100, step: 10, value: 0, fmt: (v) => v + "%", onInput: labB });
labB();

/* ---------- Lab 3 ---------- */
function labC() {
  if (!$("#g5v")) return;
  const p = +$("#g5v").value, c = ctlP(p), gap = c.qd - c.qs;
  $("#c1").textContent = Lib.fmtN(c.qd, 1); $("#c2").textContent = Lib.fmtN(c.qs, 1); $("#c3").textContent = Math.abs(gap) < 0.5 ? "None" : (gap > 0 ? "Shortage " : "Surplus ") + Lib.fmtN(Math.abs(gap), 1);
  $("#cv").textContent = p === 50 ? "At the equilibrium price the market clears: no shortage or surplus." : p < 50 ? `A maximum price of ${p} is below equilibrium, so it is effective. It makes the good cheaper, but quantity demanded (${Lib.fmtN(c.qd, 1)}) exceeds quantity supplied (${Lib.fmtN(c.qs, 1)}): a shortage of ${Lib.fmtN(gap, 1)}, with rationing, queues and possible black markets.` : `A minimum price of ${p} is above equilibrium, so it is effective. It raises producers' price, but quantity supplied (${Lib.fmtN(c.qs, 1)}) exceeds quantity demanded (${Lib.fmtN(c.qd, 1)}): a surplus of ${Lib.fmtN(-gap, 1)} that must be bought, stored or wasted.`;
  $("#labC").innerHTML = ctlDraw(p, 1);
}
Lib.slider($("#g5"), { id: "g5v", label: "Control price ", min: 20, max: 80, step: 5, value: 35, fmt: (v) => v, onInput: labC });
labC();

/* ---------- Lab 4 ---------- */
chooser("h", [
  ["A private firm will not light the street", "Public good", "Non-excludable and non-rival: free riders, so no revenue and no supply", "Government provision paid for by taxes", 5],
  ["Many people skip vaccinations", "Merit good", "Imperfect information and cost lead to under-consumption", "Free provision, subsidy, information campaigns", 5],
  ["Teenagers take up smoking", "Demerit good", "Underestimated harm and addiction lead to over-consumption", "Warnings, taxes, bans, minimum prices", 5],
  ["A seller knows a used car's faults, the buyer does not", "Information failure", "Asymmetric information leads to poor choices", "Regulation, labelling, compulsory information", 4],
  ["Bread becomes unaffordable for poor households", "Maximum price case", "Price too high for low-income households", "A maximum price (with a risk of shortages)", 3],
  ["Wheat prices swing and farm incomes are unstable", "Minimum price case", "Supply is uncertain and incomes unpredictable", "A minimum price (with a risk of surpluses)", 3]
], (it) => `${it[0]}: this is ${it[1].toLowerCase()}. The market problem is that ${it[2].toLowerCase()}. A typical response is ${it[3].toLowerCase()}.`, "How clear-cut the case is");
Lib.classify($("#cl1"), { prompt: "What kind of good is it?", buckets: [{"label": "Public good"}, {"label": "Private good"}], items: [{"text": "Street lighting", "b": 0}, {"text": "A pizza", "b": 1}, {"text": "A flood defence barrier", "b": 0}, {"text": "A school textbook bought by a student", "b": 1}, {"text": "National defence", "b": 0}, {"text": "A ticketed concert", "b": 1}, {"text": "A lighthouse", "b": 0}, {"text": "A mobile phone", "b": 1}], done: "Public goods are non-excludable and non-rival; private goods can be charged for and used up." });
Lib.classify($("#cl2"), { prompt: "Which reason for intervention does each statement give?", buckets: [{"label": "Merit good"}, {"label": "Demerit good"}, {"label": "Price control"}], items: [{"text": "Consumers do not realise the full value, so too little is consumed", "b": 0}, {"text": "Consumers underestimate the harm, so too much is consumed", "b": 1}, {"text": "The price must be kept low so poor households can afford it", "b": 2}, {"text": "Farmers' incomes are unstable and need support", "b": 2}, {"text": "Many families cannot afford it and under-use it", "b": 0}, {"text": "It is addictive and cheap, so consumption is high", "b": 1}], done: "Merit goods are under-consumed, demerit goods over-consumed, and price controls respond to affordability or unstable incomes." });
Lib.order($("#o1"), { prompt: "Put the argument for government provision of a public good in order.", items: ["The good is non-excludable and non-rival", "Non-payers cannot be stopped from using it (free riders)", "A private firm cannot earn enough revenue", "The free market does not supply it", "The government provides it, financed by taxation"], done: "Characteristics, free riders, no revenue, no supply, government provision." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Market failure", "An inefficient allocation of resources by the market"], ["Public good", "A good that is non-excludable and non-rival"], ["Free rider", "Someone who uses a good without paying for it"], ["Merit good", "A good better for people than they realise, so under-consumed"], ["Demerit good", "A good worse for people than they realise, so over-consumed"], ["Imperfect information", "Consumers lack full knowledge of costs or benefits"], ["Maximum price", "A legal limit on how high a price can go"], ["Minimum price", "A legal limit on how low a price can go"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "A street light system costs $2 000 000 a year to provide and has 40 000 users. What tax per user would fund it ($)?", "a": 50, "unit": "$", "tol": 0.5, "hint": "2 000 000 ÷ 40 000.", "sol": "<b>$50</b> per user."},
  {"q": "Demand is P = 90 - Q and supply P = 10 + Q (a simpler model than the lab). A maximum price of 30 is set. What is the quantity demanded?", "a": 60, "unit": "", "tol": 0.5, "hint": "Q = 90 - 30.", "sol": "<b>60</b>."},
  {"q": "Using the same maximum price of 30, what is the quantity supplied?", "a": 20, "unit": "", "tol": 0.5, "hint": "Q = 30 - 10.", "sol": "<b>20</b>."},
  {"q": "What is the shortage?", "a": 40, "unit": "", "tol": 0.5, "hint": "60 - 20.", "sol": "<b>40 units</b>."},
  {"q": "A minimum price of 70 is set instead. What is the surplus?", "a": 40, "unit": "", "tol": 0.5, "hint": "Qs = 60, Qd = 20.", "sol": "<b>40 units</b>."},
  {"q": "The government buys the surplus of 40 units at the minimum price of 70. What does it cost ($)?", "a": 2800, "unit": "$", "tol": 0.5, "hint": "40 × 70.", "sol": "<b>$2800</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A public good is:", opts: ["Non-excludable and non-rival", "Excludable and rival", "Excludable and non-rival", "Non-excludable and rival"], a: 0, why: "Neither characteristic of a private good." },
  { q: "The free rider problem arises because:", opts: ["Non-payers cannot be excluded", "Prices are too low", "Goods are rival", "Demand is inelastic"], a: 0, why: "Non-payers benefit anyway." },
  { q: "Merit goods are under-consumed mainly because of:", opts: ["Imperfect information", "Perfect information", "Free provision", "Low production costs"], a: 0, why: "Consumers do not see the full benefit." },
  { q: "A demerit good is likely to be:", opts: ["Over-consumed", "Under-consumed", "A public good", "A free good"], a: 0, why: "Harm is underestimated." },
  { q: "To be effective a maximum price must be:", opts: ["Below equilibrium", "Above equilibrium", "At equilibrium", "Zero"], a: 0, why: "Otherwise it has no effect." },
  { q: "A minimum price above equilibrium creates:", opts: ["A surplus", "A shortage", "Equilibrium", "No change"], a: 0, why: "Supply exceeds demand." },
  { q: "A free good differs from a public good because it has:", opts: ["No opportunity cost", "A high price", "Excludability", "Rivalry"], a: 0, why: "Its supply is unlimited." },
  { q: "Government provision of public goods is financed by:", opts: ["Taxation", "User fees only", "Free riders", "Advertising only"], a: 0, why: "Everyone contributes through taxes." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Market failure", "Inefficient allocation of resources."],
  ["Public good", "Non-excludable and non-rival."],
  ["Free rider", "Uses without paying."],
  ["Merit good", "Better than people realise; under-consumed."],
  ["Demerit good", "Worse than people realise; over-consumed."],
  ["Imperfect information", "Consumers lack full knowledge."],
  ["Maximum price", "Below equilibrium; causes shortage."],
  ["Minimum price", "Above equilibrium; causes surplus."],
  ["Government failure", "Costs, poor information, unintended effects."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "Which type of good is healthcare? (May/June 2020 · 13 · Q3, reworded)", opts: ["demerit", "free", "merit", "public"], a: 2, why: "Healthcare is more beneficial than consumers realise, so it is a merit good." },
  { q: "Consumers do not use enough of a product to maximise their private benefit because they have imperfect information about the product. How would an economist classify this product? (May/June 2020 · 11 · Q3, reworded)", opts: ["demerit good", "free good", "merit good", "public good"], a: 2, why: "Under-consumption caused by imperfect information is the mark of a merit good." },
  { q: "Which type of good would be over-consumed because of information failure? (May/June 2021 · 11 · Q3, reworded)", opts: ["demerit", "inferior", "merit", "public"], a: 0, why: "Consumers underestimate the harm of demerit goods and so buy too much." },
  { q: "What explains the underconsumption of merit goods? (Feb/March 2024 · 12 · Q13, reworded)", opts: ["Their value is not fully understood by consumers.", "They are unproductive goods and services.", "They can only be provided by the government.", "They are only provided by private sector businesses."], a: 0, why: "Imperfect information means consumers do not see their full value." },
  { q: "What is the main reason an economy is unlikely to rely completely on market forces to allocate resources? (Feb/March 2024 · 12 · Q4, reworded)", opts: ["Demerit goods will be over supplied.", "Merit goods will be under supplied.", "Private goods will not be supplied.", "Public goods will not be supplied."], a: 3, why: "Public goods cannot be sold, so the market does not provide them at all." },
  { q: "Why is national defence provided by the government? (Feb/March 2021 · 12 · Q18, reworded)", opts: ["In a free market it is excludable and rival in consumption.", "In a free market it is non-excludable and non-rival in consumption.", "The government has perfect information, so it can set the correct quantity required.", "The private sector firm would charge a high price for its use as it is a necessity."], a: 1, why: "Non-excludability and non-rivalry mean a private firm could not charge for it." },
  { q: "What is a statement of the non-rivalrous nature of public goods? (May/June 2025 · 12 · Q3, reworded)", opts: ["It is not possible to stop a non-payer from using the product.", "One person consuming the product does not reduce the amount of it available to others.", "People consume too little of the product because they are unaware of its true benefits.", "There is an unlimited supply of the product."], a: 1, why: "Non-rival means one person's use does not reduce what is available to others." },
  { q: "In many countries there are goods that must be provided directly by the government. What would be the most convincing argument for such provision? (May/June 2021 · 13 · Q14, reworded)", opts: ["The consumption of these products may be beneficial.", "The production of these products may be harmful.", "The production of these products have high opportunity costs.", "These products are non-rival in consumption and non-excludable."], a: 3, why: "A good that is non-rival and non-excludable will not be supplied by the market." },
  { q: "Why might governments provide free education for children aged 4 to 16 years old? (May/June 2025 · 12 · Q13, reworded)", opts: ["Consumers are not fully aware of the benefits of education.", "Education in a free market system would be over consumed.", "Education is a public good and there would be many free riders.", "The private costs of education exceed the private benefits in a free market."], a: 0, why: "Education is a merit good, under-consumed because people do not see its full benefits." },
  { q: "Education from 4 to 16 years of age in most developed economies is provided at zero price, financed from taxation. Why should the government do this? (May/June 2021 · 12 · Q18, reworded)", opts: ["In a free market, consumers have imperfect information so do not realise the full personal benefit of education.", "In a free market, education is not considered to be a private good.", "In a free market, consumers will be unwilling to pay for education.", "In a free market, education is non-rival and non-excludable in consumption so zero output would be produced."], a: 0, why: "Imperfect information leads to under-consumption of a merit good." },
  { q: "A flood-control dam is an example of a good provided directly by a government. Which statement relating to the direct provision of a flood-control dam is not correct? (May/June 2025 · 13 · Q13, reworded)", opts: ["It allows the government to tackle the failure to provide public goods.", "It forces the government to incur an opportunity cost.", "It involves the supply of a merit good.", "It is an example of government allocation of resources."], a: 2, why: "A flood-control dam is a public good, not a merit good." },
  { q: "A government introduces an effective minimum price for a product but makes no other intervention in the market. This policy suggests that the government's objective is (May/June 2024 · 13 · Q12, reworded)", opts: ["to discourage consumption of a demerit good.", "to increase the consumption of a merit good.", "to reduce the price of a private good.", "to support the incomes of producers."], a: 0, why: "A minimum price raises price and reduces consumption, which fits a demerit good. Supporting producers' incomes is also possible, but the answer key gives the demerit good aim." },
  { q: "The National Library Board of Singapore is a public sector organisation that finances and manages the state libraries. What is the most likely reason for this? (Feb/March 2022 · 12 · Q16, reworded)", opts: ["Libraries are public goods.", "Libraries are merit goods.", "The cost of providing library services would be greater in the private sector.", "The opportunity cost to the public sector of providing library services is zero."], a: 1, why: "Libraries are excludable and rival, so they are merit goods, not public goods." },
  { q: "A good is most suitable to be provided by the market if it is (Feb/March 2023 · 12 · Q1, reworded)", opts: ["excludable and non-rival.", "excludable and rival.", "non-excludable and non-rival.", "non-excludable and rival."], a: 1, why: "A private good can be charged for and used up, so the market can supply it." },
  { q: "How can a public good become a private good? (May/June 2025 · 11 · Q5, reworded)", opts: ["Consumers are dissatisfied with the performance of state-run services.", "New technological developments make the good excludable.", "The government privatises the industry producing the good.", "The price of the good increases so it becomes more profitable."], a: 1, why: "If a way is found to exclude non-payers, the good can be sold." },
  { q: "Which statement is correct? (Oct/Nov 2020 · 12 · Q2, reworded)", opts: ["Private goods are both non-rival and non-excludable.", "Private goods are only provided by the private sector.", "Public goods are both non-rival and non-excludable.", "Public goods do not incur opportunity costs."], a: 2, why: "That is the definition of a public good." },
] });
