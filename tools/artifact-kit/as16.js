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

/* ---------- helpers ---------- */
const yk = (x, k) => 100 * Math.pow(Math.max(0, 1 - Math.pow(x / 100, k)), 1 / k);
const PXX = (x) => 90 + x * 5.2, PYY = (y) => 300 - y * 2.6;
function axesP(xl, yl) { return SV.line(90, 300, 640, 300) + SV.line(90, 300, 90, 30) + SV.text(640, 326, xl, "sm", { "text-anchor": "end" }) + SV.text(96, 24, yl, "sm"); }
const curve = (k, c, d) => { const p = []; for (let x = 0; x <= 100; x += 2) p.push([PXX(x), PYY(yk(x, k))]); return SV.path(Lib.ptsPath(p), c, d); };

/* ---------- opportunity cost on a PPC ---------- */
function ocDraw(s) {
  let o = axesP("Capital goods", "Consumer goods") + curve(2, "c1");
  const pts = [[20, "A"], [60, "B"], [90, "C"]];
  pts.forEach(([x, l], i) => { if (s.p > i) o += SV.circle(PXX(x), PYY(yk(x, 2)), 7, "dot4") + tag(PXX(x) + 10, PYY(yk(x, 2)) - 10, l, "t4"); });
  if (s.m > 0) { const x1 = 20, x2 = 60, y1 = yk(x1, 2), y2 = yk(x2, 2); o += SV.line(PXX(x1), PYY(y1), PXX(x2), PYY(y1), "c3", op(s.m)) + SV.line(PXX(x2), PYY(y1), PXX(x2), PYY(y2), "c2", { "stroke-width": 4, ...op(s.m) }) + tag(PXX(40), PYY(y1) - 8, "+40 capital goods", "t3", s.m, "middle") + tag(PXX(x2) - 8, PYY((y1 + y2) / 2) + 4, "−" + Lib.fmtN(y1 - y2, 0) + " consumer goods", "t2", s.m, "end"); }
  if (s.n > 0) { const x1 = 60, x2 = 90, y1 = yk(x1, 2), y2 = yk(x2, 2); o += SV.line(PXX(x1), PYY(y1), PXX(x2), PYY(y1), "c3", op(s.n)) + SV.line(PXX(x2), PYY(y1), PXX(x2), PYY(y2), "c2", { "stroke-width": 4, ...op(s.n) }) + tag(PXX(75), PYY(y1) - 8, "+30 capital goods", "t3", s.n, "middle") + tag(PXX(x2) + 8, PYY((y1 + y2) / 2) + 4, "−" + Lib.fmtN(y1 - y2, 0) + " consumer goods", "t2", s.n); }
  return o;
}
Lib.stepper($("#stO"), { w: 760, h: 345, label: "A PPC with three points and the consumer goods given up as capital goods rise", base: { p: 0, m: 0, n: 0 }, draw: ocDraw, tween: 900, dwell: 5800, steps: [
  { cap: "<b>The curve.</b> It shows the most consumer goods and capital goods that the economy can produce together with its resources.", s: { p: 0, m: 0, n: 0 } },
  { cap: "<b>Point A</b> has few capital goods and many consumer goods: about 98 consumer goods and 20 capital goods.", s: { p: 1, m: 0, n: 0 } },
  { cap: "<b>Moving from A to B</b> adds 40 capital goods but costs about 18 consumer goods: the opportunity cost is about 0.45 consumer goods per capital good.", s: { p: 2, m: 1, n: 0 } },
  { cap: "<b>Moving from B to C</b> adds only 30 capital goods but costs about 36 consumer goods: about 1.2 per capital good. The opportunity cost has risen.", s: { p: 3, m: 1, n: 1 } },
] });
$("#pic1").innerHTML = `<svg viewBox="0 0 760 345" role="img" aria-label="A concave production possibility curve with three points">${ocDraw({ p: 3, m: 1, n: 1 })}</svg>`;

/* ---------- straight vs concave ---------- */
function scDraw(s) {
  let o = axesP("Good X", "Good Y");
  if (s.l > 0) o += curve(1, "c3", op(s.l)) + tag(PXX(58), PYY(40) - 8, "Straight line: constant opportunity cost", "t3", s.l, "start");
  if (s.c > 0) o += curve(2, "c1", op(s.c)) + tag(PXX(60), PYY(yk(60, 2)) - 12, "Concave: increasing opportunity cost", "t1", s.c, "start");
  if (s.b > 0) { [[0, 25], [25, 50], [50, 75], [75, 100]].forEach(([a, b], i) => { const dy = yk(a, 2) - yk(b, 2), dl = 25, x = PXX(b); o += SV.rect(x - 8, PYY(yk(a, 2)), 16, dy * 2.6, "f2", op(0.6 * s.b)) + tag(x, PYY(yk(a, 2)) + dy * 2.6 + 16, Lib.fmtN(dy, 0), "t2", s.b, "middle"); }); o += tag(PXX(60), PYY(95), "Y lost for each extra 25 units of X", "t2", s.b, "start"); }
  return o;
}
Lib.stepper($("#stC"), { w: 760, h: 345, label: "A straight-line PPC with constant opportunity cost and a concave PPC with increasing opportunity cost", base: { l: 0, c: 0, b: 0 }, draw: scDraw, tween: 900, dwell: 5800, steps: [
  { cap: "<b>Straight line.</b> If resources are equally suited to both goods, each extra 25 units of X costs 25 units of Y: constant opportunity cost.", s: { l: 1, c: 0, b: 0 } },
  { cap: "<b>Concave curve.</b> If resources are specialised, the curve bows out. The opportunity cost is not the same along it.", s: { l: 1, c: 1, b: 0 } },
  { cap: "<b>Increasing cost.</b> The first 25 units of X cost only 3 units of Y, but the last 25 cost 66. Each unit of X costs more Y as resources less suited to X are moved.", s: { l: 0, c: 1, b: 1 } },
] });
$("#pic2").innerHTML = `<svg viewBox="0 0 760 345" role="img" aria-label="Straight-line and concave PPCs">${scDraw({ l: 1, c: 1, b: 0 })}</svg>`;

/* ---------- Lab 1 ---------- */
function labP() {
  if (!$("#kk") || !$("#xx")) return;
  const k = +$("#kk").value / 10, x = +$("#xx").value, y = yk(x, k), y2 = yk(Math.min(100, x + 10), k), oc = y - y2;
  $("#r1").textContent = Lib.fmtN(y, 1); $("#r2").textContent = Lib.fmtN(oc, 1); $("#r3").textContent = x >= 100 ? "–" : Lib.fmtN(oc / 10, 2) + " Y";
  $("#rv").textContent = k <= 1.05 ? `With a straight-line PPC the next 10 units of X always cost ${Lib.fmtN(oc, 1)} units of Y: the opportunity cost is constant at ${Lib.fmtN(oc / 10, 2)} units of Y per unit of X.` : `At X = ${x}, Y is ${Lib.fmtN(y, 1)}. Producing 10 more units of X means giving up ${Lib.fmtN(oc, 1)} units of Y, or ${Lib.fmtN(oc / 10, 2)} per unit of X. Move the point to the right and the cost rises: increasing opportunity cost. The more curved the PPC, the faster it rises.`;
  const X = (v) => 40 + v * 3.4, Y = (v) => 270 - v * 2.4; let o = SV.line(40, 270, 390, 270) + SV.line(40, 270, 40, 30) + SV.text(390, 292, "Good X", "sm", { "text-anchor": "end" }) + SV.text(46, 22, "Good Y", "sm");
  const p = []; for (let v = 0; v <= 100; v += 2) p.push([X(v), Y(yk(v, k))]); o += SV.path(Lib.ptsPath(p), "c1") + SV.circle(X(x), Y(y), 7, "dot4");
  if (x < 100) o += SV.line(X(x), Y(y), X(x + 10), Y(y), "c3", { "stroke-width": 3 }) + SV.line(X(x + 10), Y(y), X(x + 10), Y(y2), "c2", { "stroke-width": 4 });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "kk", label: "Curvature (1.0 = straight line) ", min: 10, max: 40, step: 1, value: 20, fmt: (v) => (v / 10).toFixed(1), onInput: labP });
Lib.slider($("#g2"), { id: "xx", label: "Units of good X ", min: 0, max: 100, step: 5, value: 50, fmt: (v) => v, onInput: labP });
labP();

/* ---------- Lab 2 ---------- */
const PL = [[2, 12], [3, 11], [4, 10], [6, 8], [8, 6], [10, 4], [11, 3], [12, 2]];
function labL() {
  if (!$("#pn")) return;
  const n = +$("#pn").value; let w = 56, c = 0; for (let i = 0; i < n; i++) { w -= PL[i][0]; c += PL[i][1]; }
  const last = n > 0 ? PL[n - 1][0] / PL[n - 1][1] : 0;
  $("#t1").textContent = w; $("#t2").textContent = c; $("#t3").textContent = n === 0 ? "–" : Lib.fmtN(last, 2);
  $("#tv").textContent = n === 0 ? "All 8 plots grow wheat (56 units). Cotton output is zero." : `${n} plot${n > 1 ? "s are" : " is"} now growing cotton. Wheat is ${w} and cotton is ${c}. The last plot switched gave up ${PL[n - 1][0]} wheat to gain ${PL[n - 1][1]} cotton, an opportunity cost of ${Lib.fmtN(last, 2)} wheat per unit of cotton. Plots are switched in order of how well suited they are to cotton, so the cost of each extra unit of cotton keeps rising: that is increasing opportunity cost.`;
  const X = (v) => 40 + v * 5.6, Y = (v) => 270 - v * 4.4; let o = SV.line(40, 270, 390, 270) + SV.line(40, 270, 40, 30) + SV.text(390, 292, "Cotton", "sm", { "text-anchor": "end" }) + SV.text(46, 22, "Wheat", "sm");
  const pts = [[X(0), Y(56)]]; let ww = 56, cc = 0; PL.forEach(([a, b]) => { ww -= a; cc += b; pts.push([X(cc), Y(ww)]); });
  o += SV.path(Lib.ptsPath(pts), "c1");
  let w2 = 56, c2 = 0; for (let i = 0; i < n; i++) { w2 -= PL[i][0]; c2 += PL[i][1]; } o += SV.circle(X(c2), Y(w2), 7, "dot4");
  $("#labB").innerHTML = o;
}
Lib.slider($("#g3"), { id: "pn", label: "Plots switched to cotton ", min: 0, max: 8, step: 1, value: 3, fmt: (v) => v, onInput: labL });
labL();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Does the situation give constant or increasing opportunity cost?", buckets: [{"label": "Constant"}, {"label": "Increasing"}], items: [{"text": "Identical workers who can make either of two similar products equally well", "b": 0}, {"text": "Land that is much better for wheat than for cotton", "b": 1}, {"text": "A straight-line PPC", "b": 0}, {"text": "A PPC that gets steeper as more of one good is produced", "b": 1}, {"text": "Resources that are specialised and cannot easily be switched", "b": 1}, {"text": "Machines that make either product with no change in efficiency", "b": 0}, {"text": "Moving the last skilled farmers from wheat to cotton", "b": 1}, {"text": "Each extra unit of X always costs 2 units of Y", "b": 0}], done: "Constant: resources equally suited to both goods. Increasing: resources specialised." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Production possibility curve", "Maximum combinations of two goods with given resources and technology"], ["Opportunity cost on a PPC", "Units of one good given up to gain units of the other"], ["Straight-line PPC", "Constant opportunity cost"], ["Concave PPC", "Increasing opportunity cost"], ["Specialised resources", "Better suited to some uses than others"], ["Point on the PPC", "Maximum output using resources fully and efficiently"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the explanation of increasing opportunity cost in order.", items: ["Resources are specialised, not equally suited to both goods", "The best-suited resources are moved to the new good first", "Later resources moved are less suited to the new good", "Each extra unit of the new good costs more of the other good", "The PPC becomes steeper and bowed out"], done: "Specialised resources make the cost of switching rise." });
Lib.calc($("#c1"), { qs: [
  {"q": "A country moves along its PPC. Consumer goods fall from 100 to 85 as capital goods rise from 20 to 50. Calculate the opportunity cost of one capital good in consumer goods (1 decimal place).", "a": 0.5, "unit": "units", "tol": 0.05, "hint": "15 ÷ 30.", "sol": "15 ÷ 30 = <b>0.5 consumer goods</b> per capital good."},
  {"q": "Later, consumer goods fall from 85 to 55 as capital goods rise from 50 to 80 (30 more). Calculate the opportunity cost per capital good.", "a": 1, "unit": "units", "tol": 0.05, "hint": "30 ÷ 30.", "sol": "<b>1.0</b>: the cost has doubled, so opportunity cost is increasing."},
  {"q": "A straight-line PPC runs from 100 units of Y to 50 units of X. What is the opportunity cost of one unit of X in units of Y?", "a": 2, "unit": "units", "tol": 0.05, "hint": "100 ÷ 50.", "sol": "<b>2 units of Y</b>, constant everywhere."},
  {"q": "A farmer switches a plot from wheat to cotton: wheat falls from 56 to 54 and cotton rises from 0 to 12. What is the wheat given up per unit of cotton (2 decimal places)?", "a": 0.17, "unit": "units", "tol": 0.01, "hint": "2 ÷ 12.", "sol": "2 ÷ 12 = <b>0.17</b>. The first plot costs little."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A straight-line PPC shows:", opts: ["Constant opportunity cost", "Increasing opportunity cost", "Decreasing opportunity cost", "No opportunity cost"], a: 0, why: "The trade-off is the same along the line." },
  { q: "Why is a PPC usually concave?", opts: ["Resources cannot be switched easily between uses", "Resources are equally suited to both goods", "There is no scarcity", "Technology always changes"], a: 0, why: "Specialised resources make the cost of switching rise." },
  { q: "A point outside a PPC is:", opts: ["Unattainable with current resources", "Efficient", "Inefficient", "On the curve"], a: 0, why: "The curve is the limit of what resources allow." },
  { q: "The axes of a PPC should show:", opts: ["Two named goods", "Price and quantity", "Cost and revenue", "Time and output"], a: 0, why: "Name the goods, such as consumer goods and capital goods." },
  { q: "Moving along a PPC from consumer goods to capital goods:", opts: ["Reduces consumer goods", "Increases both goods", "Shifts the curve", "Removes scarcity"], a: 0, why: "More of one good means less of the other." },
] });
Lib.cards($("#fc1"), { cards: [
  ["PPC", "Maximum combinations of two goods."],
  ["Slope", "Shows the opportunity cost."],
  ["Straight line", "Constant opportunity cost."],
  ["Concave curve", "Increasing opportunity cost."],
  ["Why concave", "Resources are specialised."],
  ["On the curve", "Resources fully and efficiently used."],
  ["Outside", "Unattainable."],
  ["Label the axes", "Name the two goods; touch both axes."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "The PPC of a desert island economy, where the inhabitants produce coconuts and fish, is a straight line. What explains the shape of the PPC? (Feb/March 2020 · 12 · Q1, reworded)", opts: ["Coconuts and fish are perfect complements", "Coconuts and fish are perfect substitutes", "The inhabitants consume more fish than coconuts", "The opportunity cost of increasing fish production is constant"], a: 3, why: "A straight line means each extra unit of fish costs the same number of coconuts: constant opportunity cost." },
  { q: "The PPC for wheat and corn has a straight section from point M to point N. What can be deduced? (Feb/March 2023 · 12 · Q4, reworded)", opts: ["As the price of corn falls, more of it is demanded", "Resources used in producing corn are more efficient than in producing wheat", "The opportunity cost of producing corn falls when moving from M to N", "The opportunity cost of producing corn is constant when moving from M to N"], a: 3, why: "A straight line segment shows a constant trade-off between the two goods." },
  { q: "A PPC for goods X and Y is bowed outwards (concave to the origin). What can be deduced from the shape of this curve? (Oct/Nov 2020 · 12 · Q1, reworded)", opts: ["Decreasing marginal returns to consumption", "Decreasing opportunity costs of consumption", "Increasing opportunity costs of production", "Increasing returns to scale"], a: 2, why: "A bowed-out PPC shows rising opportunity costs of production. It says nothing about consumption." },
  { q: "A PPC for goods X and Y is bowed outwards. What happens to the opportunity cost of producing more of good Y and of producing more of good X? (Oct/Nov 2022 · 13 · Q4, reworded)", opts: ["Decreases; decreases", "Decreases; increases", "Increases; decreases", "Increases; increases"], a: 3, why: "On a concave PPC the opportunity cost of expanding either good rises." },
  { q: "Country T's PPC is bowed outwards. What happens to country T's opportunity costs of producing X as it increases production of X? (Oct/Nov 2023 · 12 · Q1, reworded)", opts: ["Constant between points 1 and 2 and between points 3 and 4", "Decrease between points 1 and 2 and increase between points 3 and 4", "Decrease between both pairs of points", "Increase between points 1 and 2 and between points 3 and 4"], a: 3, why: "On a concave curve the opportunity cost of X keeps rising throughout." },
  { q: "A country's PPC is a straight line from 100 units of food to 50 units of drink. What can be concluded? (Oct/Nov 2024 · 13 · Q1, reworded)", opts: ["Food and drink are normal goods", "The country is self-sufficient in food and drink", "The opportunity cost of food falls as more drink is produced", "There is a constant opportunity cost between food and drink"], a: 3, why: "A straight-line PPC has the same slope throughout: constant opportunity cost." },
  { q: "A PPC for a country shows manufactured goods against agricultural goods. What can be determined from the diagram? (Oct/Nov 2024 · 12 · Q1, reworded)", opts: ["The consumers' preferred combination of output", "The level of economic growth", "The opportunity cost of manufactured goods in terms of agricultural products", "The preference for present consumption rather than future consumption"], a: 2, why: "The slope of the PPC gives the opportunity cost. The curve alone does not show preferences or growth." },
  { q: "Luke can produce 18 rings and 0 bracelets, 12 and 6, 6 and 12, or 0 and 18. Zoe can produce 20 rings and 0 bracelets, 16 and 8, 12 and 16, or 8 and 24. Which statement is not correct? (Oct/Nov 2023 · 13 · Q3, reworded)", opts: ["Luke has a larger opportunity cost than Zoe for making bracelets", "The opportunity cost of producing rings is constant for both Luke and Zoe", "Zoe should specialise in making bracelets", "Zoe's opportunity cost for each bracelet is 2 rings"], a: 3, why: "Zoe gives up 4 rings for 8 bracelets, so each bracelet costs 0.5 ring, not 2. Luke gives up 1 ring per bracelet, so Zoe has the lower cost for bracelets." },
] });
