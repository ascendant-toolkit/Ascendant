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

/* ---------- PPC drawing ---------- */
const fy = (x, xm, ym) => ym * Math.sqrt(Math.max(0, 1 - (x / xm) * (x / xm)));
const QX = (x) => 90 + x * 4.0, QY = (y) => 300 - y * 2.0;
function pAxes(xl, yl) { return SV.line(90, 300, 650, 300) + SV.line(90, 300, 90, 30) + SV.text(650, 326, xl, "sm", { "text-anchor": "end" }) + SV.text(96, 24, yl, "sm"); }
const pcurve = (xm, ym, c, d) => { const p = []; for (let x = 0; x <= xm; x += 2) p.push([QX(x), QY(fy(x, xm, ym))]); p.push([QX(xm), QY(0)]); return SV.path(Lib.ptsPath(p), c, d); };

function shDraw(s) {
  let o = pAxes("Good X", "Good Y") + pcurve(100, 100, "c1", op(s.o > 0 || s.b > 0 || s.i > 0 ? 0.35 : 1)) + tag(QX(60), QY(fy(60, 100, 100)) - 10, "PPC₁", "t1", 1, "start");
  if (s.o > 0) o += pcurve(100 + 30 * s.o, 100 + 30 * s.o, "c3", op(1)) + tag(QX(95), QY(fy(95, 130, 130)) - 18, "PPC₂ (outward)", "t3", s.o, "start");
  if (s.b > 0) o += pcurve(100, 100 + 30 * s.b, "c2", op(1)) + tag(QX(30), QY(fy(30, 100, 130)) - 10, "PPC₃ (Y only)", "t2", s.b, "start");
  if (s.i > 0) o += pcurve(100 - 30 * s.i, 100 - 30 * s.i, "c4", op(1)) + tag(QX(40), QY(fy(40, 70, 70)) + 4, "PPC₄ (inward)", "t4", s.i, "middle");
  return o;
}
Lib.stepper($("#stS"), { w: 760, h: 345, label: "An outward shift of the PPC, a one-sided shift and an inward shift", base: { o: 0, b: 0, i: 0 }, draw: shDraw, tween: 1000, dwell: 5800, steps: [
  { cap: "<b>The original PPC</b> for goods X and Y with maximum outputs of 100 of each.", s: { o: 0, b: 0, i: 0 } },
  { cap: "<b>An outward shift</b> (growth in potential output): more resources or better technology. The curve moves out on both axes, so more of both goods can be made, with no opportunity cost.", s: { o: 1, b: 0, i: 0 } },
  { cap: "<b>A one-sided shift.</b> A technology that helps only good Y raises the maximum Y but not X: the curve pivots on the Y axis.", s: { o: 0, b: 1, i: 0 } },
  { cap: "<b>An inward shift.</b> War, a natural disaster or a fall in the labour force reduces resources, so the whole curve moves in and potential output falls.", s: { o: 0, b: 0, i: 1 } },
] });
$("#pic1").innerHTML = `<svg viewBox="0 0 760 345" role="img" aria-label="An original PPC with an outward shift, a pivot on one axis and an inward shift">${shDraw({ o: 1, b: 1, i: 1 })}</svg>`;

function posDraw(s) {
  let o = pAxes("Good X", "Good Y") + pcurve(100, 100, "c1");
  const P = (x, y, c, l, k, dx, dy, an) => (k > 0 ? SV.circle(QX(x), QY(y), 8, c, op(k)) + tag(QX(x) + dx, QY(y) + dy, l, "t1", k, an) : "");
  o += P(50, 50, "dot2", "A: inside (unused resources)", s.a, -12, -10, "end") + P(70.7, 70.7, "dot4", "B: on the curve (efficient)", s.b, 12, 26, "start") + P(90, 90, "dot1", "C: outside (unattainable)", s.c, 12, -8, "start");
  if (s.m > 0) o += SV.line(QX(50), QY(50), QX(70.7), QY(70.7), "c3", { "stroke-width": 3, ...op(s.m) }) + SV.arrowHead(QX(70.7), QY(70.7), "r", "dot3") + tag(QX(50) + 4, QY(50) + 30, "actual growth: idle resources put to work", "t3", s.m, "start");
  if (s.g > 0) o += pcurve(135, 135, "c3 dash", op(s.g)) + tag(QX(4), QY(122), "potential growth: the curve shifts out, so C becomes attainable", "t3", s.g, "start");
  return o;
}
Lib.stepper($("#stP"), { w: 760, h: 345, label: "Points inside, on and outside a PPC, with actual growth and potential growth", base: { a: 0, b: 0, c: 0, m: 0, g: 0 }, draw: posDraw, tween: 900, dwell: 5800, steps: [
  { cap: "<b>Inside the curve (A).</b> Some resources are unemployed or inefficiently used. More of one or both goods could be made at no opportunity cost.", s: { a: 1 } },
  { cap: "<b>On the curve (B).</b> Resources are fully and efficiently used. More of one good now means less of the other.", s: { a: 1, b: 1 } },
  { cap: "<b>Outside the curve (C).</b> Unattainable with existing resources and technology.", s: { a: 1, b: 1, c: 1 } },
  { cap: "<b>Actual growth.</b> Moving from A towards B uses idle resources, so output rises without any new resources.", s: { a: 1, b: 1, c: 1, m: 1 } },
  { cap: "<b>Potential growth.</b> Only a shift of the whole curve outwards (more or better resources) makes point C attainable.", s: { a: 1, b: 1, c: 1, m: 1, g: 1 } },
] });
$("#pic2").innerHTML = `<svg viewBox="0 0 760 345" role="img" aria-label="Points inside, on and outside a PPC">${posDraw({ a: 1, b: 1, c: 1, m: 1, g: 0 })}</svg>`;

/* ---------- Lab 1 ---------- */
function labS() {
  if (!$("#lb") || !$("#tc") || !$("#ds")) return;
  const lb = +$("#lb").value / 100, tc = +$("#tc").value / 100, ds = +$("#ds").value / 100, xm = 100 * (1 + lb) * (1 - ds), ym = 100 * (1 + lb) * (1 + tc) * (1 - ds);
  $("#r1").textContent = Lib.fmtN(xm, 0) + " (" + (xm >= 100 ? "+" : "") + Lib.fmtN(xm - 100, 0) + ")"; $("#r2").textContent = Lib.fmtN(ym, 0) + " (" + (ym >= 100 ? "+" : "") + Lib.fmtN(ym - 100, 0) + ")"; $("#r3").textContent = xm > 100.5 && ym > 100.5 ? "Outward" : xm < 99.5 && ym < 99.5 ? "Inward" : Math.abs(xm - 100) < 0.5 && Math.abs(ym - 100) < 0.5 ? "None" : "One-sided / mixed";
  $("#rv").textContent = `Maximum X is now ${Lib.fmtN(xm, 0)} and maximum Y is ${Lib.fmtN(ym, 0)}. ${xm > 100.5 && ym > 100.5 ? "More of both goods can be made, an outward shift (potential growth) that does not involve an opportunity cost." : xm < 99.5 && ym < 99.5 ? "Less of both goods can be made: an inward shift, lower potential output." : "The curve has moved out on one axis and in (or not at all) on the other: a biased shift."}`;
  const X = (x) => 40 + x * 2.6, Y = (y) => 270 - y * 1.7; let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 30) + SV.text(400, 292, "Good X", "sm", { "text-anchor": "end" }) + SV.text(46, 22, "Good Y", "sm");
  const c = (xm_, ym_, cl, d) => { const p = []; for (let x = 0; x <= xm_; x += 2) p.push([X(x), Y(fy(x, xm_, ym_))]); p.push([X(xm_), Y(0)]); return SV.path(Lib.ptsPath(p), cl, d); };
  $("#labA").innerHTML = o + c(100, 100, "c1", op(0.45)) + c(xm, ym, "c3");
}
Lib.slider($("#g1"), { id: "lb", label: "More labour and capital (both goods), % ", min: 0, max: 30, step: 5, value: 10, fmt: (v) => v + "%", onInput: labS });
Lib.slider($("#g2"), { id: "tc", label: "Technology raising Y only, % ", min: 0, max: 40, step: 5, value: 0, fmt: (v) => v + "%", onInput: labS });
Lib.slider($("#g3"), { id: "ds", label: "Resources lost in a disaster, % ", min: 0, max: 30, step: 5, value: 0, fmt: (v) => v + "%", onInput: labS });
labS();

/* ---------- Lab 2 ---------- */
function labG() {
  if (!$("#ks")) return;
  const k = +$("#ks").value / 100, c0 = 100 * (1 - k), g = 0.06 * k, cb0 = 90, gb = 0.006;
  let cross = null; for (let t = 0; t <= 80; t++) if (c0 * Math.pow(1 + g, t) >= cb0 * Math.pow(1 + gb, t)) { cross = t; break; }
  $("#t1").textContent = Lib.fmtN(c0, 0); $("#t2").textContent = Lib.fmtN(g * 100, 1) + "%"; $("#t3").textContent = k <= 0.1 ? "–" : cross === null ? "over 80 yrs" : (cross === 0 ? "0" : cross) + " yrs";
  $("#tv").textContent = k <= 0.1 ? "This is the same as the baseline economy: 10% of resources in capital goods." : `Putting ${Lib.fmtN(k * 100, 0)}% of resources into capital goods cuts consumption today to ${Lib.fmtN(c0, 0)} (against 90), but raises growth of capacity to ${Lib.fmtN(g * 100, 1)}% a year. ${cross === null ? "It never catches up within 80 years in this model." : "Consumption overtakes the 10% economy after about " + cross + " years."} This is the opportunity cost of growth: less consumption now for more later. (Illustrative model.)`;
  const X = (t) => 40 + t * 8.4, mx = 220, Y = (v) => 270 - v / mx * 230; let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 30) + SV.text(400, 292, "Years", "sm", { "text-anchor": "end" }) + SV.text(46, 22, "Consumption", "sm");
  const pa = [], pb = []; for (let t = 0; t <= 40; t++) { pa.push([X(t), Y(Math.min(mx, cb0 * Math.pow(1 + gb, t)))]); pb.push([X(t), Y(Math.min(mx, c0 * Math.pow(1 + g, t)))]); }
  o += SV.path(Lib.ptsPath(pa), "c2 dash") + SV.path(Lib.ptsPath(pb), "c1") + tag(396, Y(cb0 * Math.pow(1 + gb, 40)) - 8, "10% invested", "t2", 1, "end") + tag(396, Math.max(40, Y(Math.min(mx, c0 * Math.pow(1 + g, 40)))) + 18, "your choice", "t1", 1, "end");
  $("#labB").innerHTML = o;
}
Lib.slider($("#g4"), { id: "ks", label: "Share of resources in capital goods, % ", min: 10, max: 60, step: 5, value: 40, fmt: (v) => v + "%", onInput: labG });
labG();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "What does it show on a PPC?", buckets: [{"label": "Movement along"}, {"label": "Shift"}, {"label": "Movement towards the curve"}], items: [{"text": "A government moves resources from consumer goods to capital goods", "b": 0}, {"text": "New technology raises the output of all goods", "b": 1}, {"text": "Unemployed workers find jobs as demand recovers", "b": 2}, {"text": "More immigration increases the labour force", "b": 1}, {"text": "A farmer switches land from wheat to barley", "b": 0}, {"text": "Idle factories are put back into use", "b": 2}, {"text": "A flood destroys part of a country's farmland", "b": 1}, {"text": "Producing more cars and fewer trucks with the same resources", "b": 0}], done: "Reallocation is a movement along; more or better resources shift the curve; idle resources move the economy from inside towards the curve." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Outward shift", "More of both goods can be made: potential growth"], ["Inward shift", "Potential output falls because resources are lost"], ["Inside the PPC", "Resources are unused or used inefficiently"], ["On the PPC", "Resources are fully and efficiently used"], ["Outside the PPC", "Unattainable with current resources"], ["Actual growth", "Using idle resources, moving towards the curve"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the effects of a recession and recovery in order.", items: ["Demand falls and firms cut output", "Unemployment rises and some factories sit idle", "The economy moves to a point inside the PPC", "Demand recovers and firms hire workers again", "The economy moves back towards the PPC: actual growth"], done: "A recession is a move inside the curve; recovery is a move back towards it." });
Lib.calc($("#c1"), { qs: [
  {"q": "An economy's maximum output of Y rises from 100 to 130 after a technology boost. Calculate the percentage increase in the maximum output of Y (%).", "a": 30, "unit": "%", "tol": 0.5, "hint": "30 ÷ 100.", "sol": "<b>30%</b>."},
  {"q": "An economy operating inside its PPC produces 60 units of Y when it could produce 80. By what percentage is actual output below potential (%)?", "a": 25, "unit": "%", "tol": 0.5, "hint": "(80 − 60) ÷ 80.", "sol": "<b>25%</b> below potential."},
  {"q": "Moving to the curve, actual output of Y rises from 60 to 80. Calculate the percentage increase in actual output (%, 1 decimal place).", "a": 33.3, "unit": "%", "tol": 0.1, "hint": "20 ÷ 60.", "sol": "<b>33.3%</b>."},
  {"q": "An economy that puts 40% of its resources into capital goods has consumption of 60 each year. The baseline economy has 90. By how many units is consumption lower today?", "a": 30, "unit": "units", "tol": 0.5, "hint": "90 − 60.", "sol": "<b>30 units</b>: the opportunity cost of faster future growth."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "An outward shift of the PPC could be caused by:", opts: ["Investment in new technology", "A fall in the labour force", "A recession", "A move along the curve"], a: 0, why: "Better technology raises potential output." },
  { q: "A point inside the PPC means that:", opts: ["Resources are unused or inefficiently used", "Resources are fully used", "The point cannot be reached", "Opportunity cost is zero everywhere"], a: 0, why: "Output could be raised without giving anything up." },
  { q: "Which is a movement along the PPC?", opts: ["Moving resources from food to cars", "New technology in all industries", "A rise in the labour force", "A fall in unemployment"], a: 0, why: "Reallocating existing resources is a movement along the curve." },
  { q: "Producing more capital goods now is likely to:", opts: ["Shift the PPC outwards in the future", "Shift the PPC inwards", "Move the economy outside the PPC immediately", "Have no effect on consumption"], a: 0, why: "More capital raises future capacity, at the cost of current consumption." },
  { q: "A point outside the PPC is:", opts: ["Unattainable now", "Inefficient", "On the curve", "A movement along"], a: 0, why: "Not enough resources." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Outward shift", "More resources or better technology; potential growth."],
  ["Inward shift", "Fall in resources; lower potential output."],
  ["Movement along", "Reallocation; opportunity cost."],
  ["Inside", "Unused or inefficient resources."],
  ["On", "Full and efficient use."],
  ["Outside", "Unattainable."],
  ["Actual growth", "From inside towards the curve."],
  ["Cost of growth", "Fewer consumer goods now."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "An economist knows the current point at which an economy operates within its production possibility curve. What can the economist conclude about this economy? (May/June 2024 · 11 · Q5, reworded)", opts: ["Its degree of self-sufficiency", "Its international competitiveness", "Its level of output of the two goods", "Its rate of economic growth"], a: 2, why: "A point on the diagram gives the output of the two goods. It says nothing about trade or growth." },
  { q: "An economy is operating at a point inside its production possibility curve. Why is this described as inefficient? (Oct/Nov 2020 · 13 · Q1, reworded)", opts: ["Individuals are enjoying too much leisure", "More of one good can be produced without decreasing production of another", "The combination of labour and capital is wrong", "There are shortages of some goods and an excess supply of others"], a: 1, why: "Inside the curve resources are unused or wasted, so output of one good could rise at no cost to the other." },
  { q: "Assuming nothing else changes, which change in an economy's labour market will cause the PPC to shift to the left? (May/June 2023 · 12 · Q2, reworded)", opts: ["An increase in worker immigration", "An increase in the retirement age", "An increase in labour productivity", "An increase in the school leaving age"], a: 3, why: "A higher school leaving age keeps young people out of the workforce, so the quantity of labour falls. The other three raise it." },
  { q: "A PPC for consumer goods and capital goods shifts outwards. What could have caused this shift? (May/June 2025 · 12 · Q5, reworded)", opts: ["A decrease in mineral resources", "A decrease in prices of consumer goods", "An increase in employment", "An increase in technology"], a: 3, why: "Technology raises the economy's capacity. A rise in employment moves the economy towards the curve but does not shift it." },
  { q: "A PPC shows the combinations of consumer goods and capital goods produced using all available resources. Position X lies outside the curve. What does position X indicate? (May/June 2024 · 12 · Q1, reworded)", opts: ["A lower ratio of capital to consumer goods is needed for growth", "Increasing levels of unemployment", "Insufficient factors of production are available", "Too many consumer goods are produced"], a: 2, why: "A point outside the PPC cannot be reached because the economy does not have enough factors of production." },
  { q: "An economy's PPC for computers and cars is JK. It pivots inwards on the cars axis only. What could cause this? (Oct/Nov 2021 · 13 · Q1, reworded)", opts: ["A fall in output per worker in the car industry", "A fall in the level of competition in the car industry", "A rise in the potential workforce of the economy", "A rise in the price of cars"], a: 0, why: "Only the maximum output of cars falls, so a fall in productivity in the car industry is the cause. A rise in the workforce would shift the curve out on both axes." },
  { q: "Farmers using traditional methods lack finance and often employ family members part-time. If working practices in agriculture are improved, how is this likely to be shown on the PPC? (Oct/Nov 2024 · 11 · Q5, reworded)", opts: ["By a movement along the PPC", "By an outward shift of the PPC on both axes", "By a movement from a point inside the PPC to a point on the PPC", "By an inward shift of the PPC"], a: 2, why: "Better use of existing resources moves the economy from inside the curve towards it: actual growth." },
  { q: "A farmer with fixed land grows wheat and barley. Some barley land is flooded and cannot be used. The farmer then plants genetically modified wheat that gives higher yields on the remaining land. What is the likely effect on the farmer's PPC? (May/June 2022 · 14 · Q2, reworded)", opts: ["Both the maximum wheat and the maximum barley rise", "Both fall", "The maximum wheat rises and the maximum barley falls", "The maximum wheat falls and the maximum barley rises"], a: 2, why: "The flood reduces barley capacity and GM wheat raises wheat capacity, so the PPC pivots." },
] });
