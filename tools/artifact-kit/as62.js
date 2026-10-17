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

/* ---------- specialisation bars ---------- */
function spDraw(s) {
  const Y = (v) => 250 - v * 8; let o = SV.line(60, 250, 700, 250) + SV.line(60, 250, 60, 30) + SV.text(66, 24, "Units of output", "sm");
  const bar = (x, v, c, l) => SV.rect(x, Y(v), 40, 250 - Y(v), c, op(0.7)) + SV.text(x + 20, Y(v) - 6, Lib.fmtN(v, 0), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 20, 268, l, "sm", { "text-anchor": "middle" });
  const before = s.k < 0.5, carsA = before ? 5 : 0, whA = before ? 10 : 20, carsB = before ? 6 : 12, whB = before ? 6 : 0;
  o += bar(100, carsA, "f3", "A cars") + bar(150, whA, "f2", "A wheat") + bar(230, carsB, "f3", "B cars") + bar(280, whB, "f2", "B wheat");
  o += bar(400, carsA + carsB, "f3", "Total cars") + bar(450, whA + whB, "f2", "Total wheat");
  o += tag(560, 80, before ? "Each splits its resources" : "Each specialises", "c3", 1, "start") + tag(560, 100, before ? "11 cars, 16 wheat" : "12 cars, 20 wheat", "c1", 1, "start") + (before ? "" : tag(560, 122, "More of both", "c2", 1, "start"));
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 285" role="img" aria-label="After specialisation world output rises from 11 cars and 16 wheat to 12 cars and 20 wheat">${spDraw({ k: 1 })}</svg>`;
Lib.stepper($("#stG"), { w: 760, h: 285, label: "Specialising raises world output", base: { k: 0 }, draw: spDraw, tween: 700, dwell: 5400, steps: [
  { cap: "<b>Before trade.</b> Country A (10 cars or 20 wheat) and country B (12 cars or 12 wheat) each use half their resources on each good. Totals: 11 cars and 16 wheat. A's opportunity cost of a car is 2 wheat; B's is 1 wheat.", s: { k: 0 } },
  { cap: "<b>After specialisation.</b> B has the comparative advantage in cars (lower opportunity cost) and A in wheat. B makes 12 cars and A 20 wheat. Total output is 12 cars and 20 wheat: <b>more of both</b>, so there are gains to share through trade.", s: { k: 1 } },
] });

function tpDraw(s) {
  const X = (q) => 80 + q * 36, Y = (p) => 260 - p * 10; let o = axes(80, 260, 560, 30, "Cars", "Wheat");
  o += SV.line(X(0), Y(20), X(10), Y(0), "c1", { "stroke-width": 3 }) + tag(X(10) + 6, Y(0) - 4, "PPC", "c1");
  if (s.t > 0) o += SV.line(X(0), Y(20), X(13.33), Y(0), "c2", { "stroke-width": 3, "stroke-dasharray": "7 4", ...op(s.t) }) + tag(X(13.33) + 6, Y(0) - 4, "TPC", "c2", s.t);
  if (s.p > 0) o += SV.circle(X(4), Y(10), 6, "dot1", op(s.p)) + SV.text(X(4) - 8, Y(10) - 10, "Without trade", "sm", { "text-anchor": "end", ...op(s.p) }) + SV.circle(X(6), Y(11), 8, "dot3", op(s.p)) + SV.text(X(6) + 14, Y(11) - 10, "With trade: more cars and wheat", "lbl bd", { ...halo, ...op(s.p) });
  return o;
}
$("#pic2").innerHTML = `<svg viewBox="0 0 760 290" role="img" aria-label="The trading possibility curve lies outside the production possibility curve">${tpDraw({ t: 1, p: 1 })}</svg>`;
Lib.stepper($("#stT"), { w: 760, h: 290, label: "The PPC and the trading possibility curve for country A", base: { t: 0, p: 0 }, draw: tpDraw, tween: 800, dwell: 5400, steps: [
  { cap: "<b>The PPC.</b> Country A can produce 20 wheat or 10 cars (or combinations). Without trade it can only consume on or inside this line.", s: { t: 0, p: 0 } },
  { cap: "<b>Specialise and trade.</b> A specialises in wheat and trades at a price of 1 car for 1.5 wheat. It can now reach any point on the <b>trading possibility curve</b>, which lies outside the PPC.", s: { t: 1, p: 0 } },
  { cap: "<b>Gains from trade.</b> A can consume 6 cars and 11 wheat, more of both than the 4 cars and 10 wheat it could have had without trade.", s: { t: 1, p: 1 } },
] });

/* ---------- Lab 1 ---------- */
function labS() {
  if (!$("#bw")) return;
  const w = +$("#bw").value, ocA = 2, ocB = w / 12, gain = Math.abs(ocA - ocB), who = ocB < ocA ? "B" : ocB > ocA ? "A" : "Neither";
  $("#r1").textContent = "2 wheat"; $("#r2").textContent = Lib.fmtN(ocB, 2) + " wheat"; $("#r3").textContent = gain < 0.01 ? "None" : "Possible";
  $("#rv").textContent = gain < 0.01 ? "Both countries have the same opportunity cost, so neither has a comparative advantage and there is no gain from specialising." : `A gives up 2 wheat per car and B gives up ${Lib.fmtN(ocB, 2)}. ${who === "B" ? "B has the comparative advantage in cars, and A has it in wheat." : "A has the comparative advantage in cars, and B in wheat."} Each should specialise where its opportunity cost is lower, and trade at a price between ${Lib.fmtN(Math.min(2, ocB), 2)} and ${Lib.fmtN(Math.max(2, ocB), 2)} wheat per car. B ${w >= 20 ? "even has an absolute advantage in both goods" : w < 20 ? "has an absolute advantage in cars but not in wheat" : ""}.`;
  const Y = (v) => 250 - v * 40; let o = SV.line(40, 250, 400, 250);
  [["A: cost of a car", ocA, "f3"], ["B: cost of a car", ocB, "f2"]].forEach(([l, v, c], i) => (o += SV.rect(80 + i * 150, Y(v), 100, 250 - Y(v), c, op(0.65)) + SV.text(130 + i * 150, 268, l, "sm", { "text-anchor": "middle" }) + SV.text(130 + i * 150, Y(v) - 6, Lib.fmtN(v, 2) + " wheat", "lbl bd", { "text-anchor": "middle" })));
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "bw", label: "B's maximum wheat output, units ", min: 6, max: 30, step: 2, value: 12, fmt: (v) => v, onInput: labS });
labS();

/* ---------- Lab 2 ---------- */
const LM = [["No limits (the theory)", 100, "Nobody", "Both countries gain the full amount."], ["Transport costs", 60, "Both countries", "Shipping costs eat into the price advantage, so less trade is worthwhile."], ["Tariffs and trade barriers", 50, "Consumers and exporters", "Taxes on imports raise prices and invite retaliation."], ["Immobile workers", 55, "Displaced workers", "Workers in declining industries cannot easily move to expanding ones, so unemployment results."], ["Rising opportunity costs", 65, "The specialising country", "As output of one good expands, resources become less suited, reducing the advantage."], ["Over-specialisation", 45, "Countries dependent on one export", "A fall in the world price of the main export causes a collapse in incomes."]];
function showL(i) {
  const [n, g, who, why] = LM[i]; $$("#lB button").forEach((b, k) => b.classList.toggle("pri", k === i));
  $("#t1").textContent = n; $("#t2").textContent = g + "%"; $("#t3").textContent = who; $("#tv").textContent = `${n}: ${why} About ${g}% of the potential gain from trade remains in this illustration.`;
  $("#labB").innerHTML = SV.rect(60, 70, 300, 40, "f1", op(0.2)) + SV.rect(60, 70, 3 * g, 40, g > 60 ? "f2" : "f3", op(0.7)) + SV.text(210, 60, "Potential gain from trade = 100%", "lbl bd", { "text-anchor": "middle" }) + SV.text(210, 140, g + "% remains", "lbl bd", { "text-anchor": "middle", style: "font-size:18px" });
}
$("#lB").innerHTML = LM.map((l, i) => `<button class="b" data-i="${i}">${l[0]}</button>`).join("");
$$("#lB button").forEach((b) => (b.onclick = () => showL(+b.dataset.i)));
showL(1);

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Advantage or disadvantage of free trade?", buckets: [{"label": "Advantage"}, {"label": "Disadvantage"}], items: [{"text": "Greater choice for consumers", "b": 0}, {"text": "Job losses in industries that cannot compete", "b": 1}, {"text": "Lower prices from competition", "b": 0}, {"text": "Over-reliance on a few exports", "b": 1}, {"text": "Economies of scale from larger markets", "b": 0}, {"text": "Infant industries may fail", "b": 1}, {"text": "Higher world output", "b": 0}, {"text": "Security risk if vital resources are imported", "b": 1}], done: "Free trade raises output and choice but may harm uncompetitive industries and create dependence." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Comparative advantage", "Lower opportunity cost of producing a good"], ["Absolute advantage", "Can produce more with the same resources"], ["Specialisation", "Concentrating on the good with the lower opportunity cost"], ["Trading possibility curve", "What a country can consume after specialising and trading"], ["Infant industry", "A new industry that cannot yet compete with established rivals"], ["Over-specialisation", "Dependence on one or a few exports"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the gains from specialisation in order.", items: ["Each country finds its lower opportunity cost good", "Each specialises in that good", "Total output rises", "The countries trade at a price between their opportunity costs", "Both can consume more than before"], done: "Specialise, produce more in total, trade, both gain." });
Lib.calc($("#c1"), { qs: [
  {"q": "A can make 10 cars or 20 wheat. What is A's opportunity cost of one car (wheat)?", "a": 2, "unit": "wheat", "tol": 0.05, "hint": "20 ÷ 10.", "sol": "<b>2 wheat</b>."},
  {"q": "B can make 12 cars or 12 wheat. What is B's opportunity cost of one car (wheat)?", "a": 1, "unit": "wheat", "tol": 0.05, "hint": "12 ÷ 12.", "sol": "<b>1 wheat</b>: B has the comparative advantage in cars."},
  {"q": "What is A's opportunity cost of one wheat in cars?", "a": 0.5, "unit": "cars", "tol": 0.02, "hint": "10 ÷ 20.", "sol": "<b>0.5 cars</b>."},
  {"q": "Before trade the two countries together produce 16 wheat. After specialising A makes 20 wheat. How many more wheat is that?", "a": 4, "unit": "wheat", "tol": 0.2, "hint": "20 − 16.", "sol": "<b>4</b>, with 1 more car too."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Comparative advantage means a lower:", opts: ["Opportunity cost", "Price", "Wage", "Tax"], a: 0, why: "Opportunity cost." },
  { q: "The trading possibility curve is:", opts: ["Outside the PPC", "Inside the PPC", "The same as the PPC", "Below the axes"], a: 0, why: "Gains from trade." },
  { q: "A limitation of comparative advantage is:", opts: ["Transport costs", "Perfect mobility", "No trade barriers", "Constant costs"], a: 0, why: "Reduce gains." },
  { q: "An infant industry is at risk from:", opts: ["Free trade", "Protection", "Subsidies", "Tariffs"], a: 0, why: "Established competitors." },
  { q: "A benefit of free trade is:", opts: ["Greater choice for consumers", "Higher unemployment always", "Fewer exports", "Less competition"], a: 0, why: "Variety and lower prices." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Comparative advantage", "Lower opportunity cost."],
  ["Absolute advantage", "More output per input."],
  ["TPC", "Outside the PPC."],
  ["Gains", "Output, choice, prices, scale."],
  ["Costs", "Jobs, dependence, infant industries."],
  ["Limits", "Transport, immobility, rising costs."],
  ["Dynamic", "Advantage can change."],
  ["Judge", "Usually positive, not for everyone."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "Two statements are shown. 1: A country can produce a good at a lower opportunity cost than another country. 2: A country can produce a greater quantity of a good for the same quantity of inputs than another country. What do these two statements describe? (1, 2) (May/June 2021 · 12 · Q24, reworded)", opts: ["absolute advantage, comparative advantage", "absolute advantage, the terms of trade", "comparative advantage, absolute advantage", "the terms of trade, comparative advantage"], a: 2, why: "A lower opportunity cost is comparative advantage; more output from the same inputs is absolute advantage." },
  { q: "Which argument is an importer most likely to use to gain the support of consumers for free trade? (May/June 2020 · 12 · Q22, reworded)", opts: ["More imports allow the government to raise revenue from tariffs", "More imports improve the country's terms of trade", "More imports increase competition in the domestic economy", "More imports raise total employment in the domestic economy"], a: 2, why: "Consumers benefit from competition, which brings lower prices and more choice." },
  { q: "The statements relate to possible gains from an increase in free trade. Which gain is least certain to result in the short run? (May/June 2020 · 12 · Q26, reworded)", opts: ["a reduction in costs of production", "a rise in the number of jobs", "a wider choice of goods available to consumers", "an increase in the level of competition"], a: 1, why: "In the short run, imports may displace domestic jobs, so a rise in jobs is least certain." },
  { q: "An economy with a long history of extensive barriers to trade decides to switch to totally free trade. What is most likely to increase in the short term? (May/June 2020 · 13 · Q26, reworded)", opts: ["consumer surplus", "government revenue", "inflationary pressure", "profits of all domestic companies"], a: 0, why: "Cheaper imports raise consumer surplus. Tariff revenue falls and some domestic firms lose." },
  { q: "What may increase the benefits a country gains from international trade? (May/June 2021 · 13 · Q23, reworded)", opts: ["a reduction in transportation costs because of a fall in world oil prices", "domestic wage rates increase at a faster rate than output per worker", "the domestic labour force becomes more occupationally immobile", "trading partners increase tariffs on imported goods"], a: 0, why: "Lower transport costs raise the gains from trade. Rising unit labour costs, immobility and tariffs reduce them." },
  { q: "Four countries, A, B, C and D, trade internationally. Each circle in the diagram represents a free trade area between the countries within the circle. A country can belong to more than one free trade area. Countries outside of a circle face trade barriers. Which country has the greatest opportunity to benefit from free international trade? (Feb/March 2020 · 12 · Q21, reworded)", opts: ["A", "D", "C", "B"], a: 1, why: "The country that belongs to the most free trade areas has the greatest tariff-free access." },
  { q: "In a closed economy a rise in aggregate demand is needed to increase output in the country. What is necessary to achieve this increase in output in the economy? (Feb/March 2020 · 12 · Q27, reworded)", opts: ["enough capacity to produce the extra goods and services demanded", "free trade to allow imports to make up any shortages in supply", "government spending to be less than tax revenue", "reduced credit to lower inflation"], a: 0, why: "In a closed economy there are no imports, so output can only rise if capacity exists." },
] });
