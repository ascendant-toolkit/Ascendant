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

function strip(el, aria, L) {
  const n = L.length, w = Math.floor((740 - (n - 1) * 10) / n), C = ["f3", "f3", "f1", "f1", "f2", "f2"];
  let o = "";
  L.forEach(([a, b], i) => {
    const x = 10 + i * (w + 10);
    o += SV.rect(x, 12, w, 84, C[i % 6], { rx: 12, ...op(0.45) }) + SV.text(x + w / 2, 40, a, "lbl bd", { "text-anchor": "middle", style: "font-size:16px" });
    b.split(" | ").forEach((p, j) => { o += SV.text(x + w / 2, 62 + j * 18, p, "sm", { "text-anchor": "middle" }); });
  });
  $(el).innerHTML = `<svg viewBox="0 0 760 108" role="img" aria-label="${aria}">${o}</svg>`;
}

strip("#pic1", "A precise definition has three parts", [["The term", "name it exactly"], ["The feature", "the idea that matters"], ["The contrast", "how it differs from its neighbour"]]);
chainStep("#stA", "From a bare definition to Level 3 knowledge", ["Bare: 'A negative externality is pollution.'", "Precise: 'A cost to a third party not in the market price.'", "Add the effect: 'So social cost exceeds private cost.'", "Add the context: 'In coal-fired power, the cost is local air pollution.'", "Add the diagram: MPC, MSC, D labelled for the market"],
  ["<b>Level 1 knowledge:</b> an example is not a definition.", "<b>Accurate:</b> third party and 'not in the price' are the key features.", "<b>Understanding:</b> the consequence shows you know why it matters.", "<b>Application:</b> the market named in the question.", "<b>Level 3:</b> accurate, applied and drawn."]);
chainStep("#stB", "A diagram, mark by mark", ["Label both axes: price level and real GDP", "Draw and name AD1 and SRAS", "Mark the equilibrium and project to both axes", "Shift AD to AD2 with an arrow and say why", "Mark the new equilibrium and the change in price level and output"],
  ["<b>Axes:</b> price level and real GDP, not P and Q.", "<b>Curves:</b> named, with the correct slope.", "<b>Equilibrium:</b> original point P1, Y1.", "<b>Shift:</b> one curve moves, with a reason.", "<b>Result:</b> new equilibrium, and the text refers to it."]);
chainStep("#stC", "Quoting the data: from copying to using", ["Copy: 'Exports were $12bn.'", "Add unit and year: 'Exports were $12bn in 2022.'", "Add the change: 'up from $9bn in 2019, a rise of 33%.'", "Say what it shows: 'so export growth outpaced GDP growth.'", "Say what it cannot show: 'but it says nothing about export prices.'"],
  ["<b>Copying</b> earns little.", "<b>Precise</b> but still only a fact.", "<b>Calculation</b> turns it into evidence.", "<b>Interpretation</b> makes it analysis.", "<b>Limit</b> is the start of evaluation."]);

chooser("h", [
  ["Allocative efficiency", "Using resources well.", "Resources go to the goods society values most, where price equals marginal cost.", "Define allocative efficiency (2 marks).", 5],
  ["Positive externality", "Something good for society.", "A benefit to a third party that is not reflected in the price, so social benefit exceeds private benefit.", "What is meant by a positive externality (2 marks)?", 4],
  ["Structural unemployment", "People with no jobs.", "Unemployment from a mismatch between skills or location and the jobs available after a lasting change in demand.", "Distinguish between structural and cyclical unemployment (3 marks).", 4],
  ["Comparative advantage", "Being better at making something.", "A country can produce a good at a lower opportunity cost than another country.", "Explain comparative advantage (4 marks).", 5],
  ["Government failure", "When the government makes mistakes.", "Government intervention that leads to a net welfare loss, or a less efficient allocation of resources than before.", "What is meant by government failure (2 marks)?", 4]
], (it) => `${it[0]}. Imprecise: "${it[1]}" Precise: "${it[2]}" Fits: ${it[3]}`, "How often this is tested");
chooser("k", [
  ["PED", "% change in quantity demanded ÷ % change in price", "Reversing the fraction, or using absolute changes", "Price up 10%, quantity down 15%: PED = -15 ÷ 10 = -1.5, which is elastic.", 5],
  ["YED", "% change in quantity demanded ÷ % change in income", "Not stating what a negative value means", "Income up 5%, quantity down 2%: YED = -0.4, so an inferior good.", 4],
  ["XED", "% change in quantity of A ÷ % change in price of B", "Using the price of A in the denominator", "Price of B up 10%, quantity of A up 6%: XED = +0.6, so the goods are substitutes.", 4],
  ["Multiplier", "1 ÷ (1 − MPC)", "Using MPC in the denominator, or ignoring withdrawals", "MPC 0.8: k = 1 ÷ 0.2 = 5, so a $2bn injection could raise income by up to $10bn.", 5],
  ["Terms of trade", "Export price index ÷ import price index × 100", "Inverting the fraction", "Exports 110, imports 125: 88, a deterioration.", 4]
], (it) => `${it[0]}: ${it[1]}. Slip: ${it[2]}. Check: ${it[3]}`, "How often this is tested");
chooser("j", [
  ["Interest rates", "A higher interest rate reduces consumption.", "With most borrowing at variable rates, a higher rate could raise repayments quickly, so consumption in this economy may fall sharply.", "The country's borrowing at variable rates", 5],
  ["Exchange rate", "A depreciation makes exports cheaper.", "A depreciation lowers the price of the country's coffee exports in dollars, which could raise sales if foreign demand is elastic.", "The named export and its buyers", 5],
  ["Tax", "A tax reduces demand for a product.", "A 20% tax on cigarettes could cut the quantity bought by long-term smokers only slightly if their demand is inelastic.", "The good, the group and the figure", 4],
  ["Subsidy", "A subsidy lowers costs.", "A subsidy on electric vehicles lowers the price to buyers in this market, shifting supply right and raising sales.", "The market named in the question", 4],
  ["Inflation", "Inflation reduces purchasing power.", "With prices rising 8% a year and wages up 3%, real incomes in this country are falling, particularly for pensioners.", "The figures in the source", 5]
], (it) => `${it[0]}. Generic: "${it[1]}" Applied: "${it[2]}" Added: ${it[3].toLowerCase()}.`, "Application marks earned");
Lib.classify($("#cl1"), { prompt: "Recall, understanding or application?", buckets: [{"label": "Recall"}, {"label": "Understanding"}, {"label": "Application"}], items: [{"text": "Real GDP is GDP adjusted for inflation.", "b": 0}, {"text": "A tax raises the cost of production, so supply shifts left and price rises.", "b": 1}, {"text": "Between 2019 and 2022 this country's exports rose from $9bn to $12bn.", "b": 2}, {"text": "The multiplier is 1 ÷ (1 − MPC).", "b": 0}, {"text": "Because this economy's MPC is 0.6, the $5bn project is likely to raise income by about $12.5bn.", "b": 2}, {"text": "A merger reduces competition because it removes a rival.", "b": 1}], done: "Recall states the fact, understanding explains it, application uses the information given." });
Lib.classify($("#cl2"), { prompt: "Precise or imprecise?", buckets: [{"label": "Imprecise"}, {"label": "Precise"}], items: [{"text": "Inflation is when things get expensive.", "b": 0}, {"text": "Inflation is a sustained rise in the general price level over time.", "b": 1}, {"text": "An externality is pollution.", "b": 0}, {"text": "An externality is a cost or benefit to a third party that is not reflected in the market price.", "b": 1}, {"text": "Productive efficiency is producing a lot.", "b": 0}, {"text": "Productive efficiency is producing at the lowest average cost.", "b": 1}], done: "A precise definition names the feature that matters." });
Lib.order($("#o1"), { prompt: "Put the steps for drawing a diagram in order.", items: ["Label the axes", "Draw and name the curves", "Mark the original equilibrium", "Shift the curve with an arrow and a label", "Mark the new equilibrium", "Write a sentence that refers to the shift"], done: "Axes, curves, equilibrium, shift, new equilibrium, then use it in the text." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Allocative efficiency", "Price equals marginal cost"], ["Productive efficiency", "Output at the minimum of average cost"], ["Negative externality", "A cost to a third party not in the price"], ["Structural unemployment", "A mismatch of skills or location with the jobs available"], ["Terms of trade", "Export price index ÷ import price index × 100"], ["Multiplier", "1 ÷ (1 − MPC)"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "A price rise of 8% reduces quantity demanded by 12%. Calculate PED (1 decimal place, with sign).", "a": -1.5, "unit": "", "tol": 0.05, "hint": "-12 ÷ 8.", "sol": "<b>-1.5</b>, elastic."},
  {"q": "MPC is 0.9 and there are no other leakages. Calculate the multiplier.", "a": 10, "unit": "", "tol": 0.05, "hint": "1 ÷ (1 − 0.9).", "sol": "<b>10</b>."},
  {"q": "Export prices index 130, import prices index 104. Calculate the terms of trade.", "a": 125, "unit": "", "tol": 0.2, "hint": "130 ÷ 104 × 100.", "sol": "<b>125</b>, an improvement."},
  {"q": "Real GDP rises from $200bn to $208bn. Calculate the percentage change.", "a": 4, "unit": "%", "tol": 0.05, "hint": "8 ÷ 200.", "sol": "<b>4%</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A diagram is asked for and none is drawn. What is the likely effect on a 20-mark essay?", opts: ["The 14-mark scale is capped at Level 2", "No effect", "The essay is marked out of 10", "The evaluation marks are lost"], a: 0, why: "Missing required diagrams cap the 14-mark scale at Level 2." },
  { q: "Which sentence shows application?", opts: ["Exports rose from $9bn in 2019 to $12bn in 2022, so they grew faster than GDP.", "Exports are goods sold abroad.", "Exports are a component of AD.", "Exports can rise or fall."], a: 0, why: "It uses the information in the source." },
  { q: "Which is the most precise definition?", opts: ["Allocative efficiency occurs where price equals marginal cost.", "Allocative efficiency means being efficient.", "Allocative efficiency is good for society.", "Allocative efficiency is about prices."], a: 0, why: "It names the condition." },
  { q: "Unemployment falls from 6.0% to 5.5%. Which is correct?", opts: ["A fall of 0.5 percentage points", "A fall of 0.5%", "A fall of 5.5%", "A rise of 0.5 points"], a: 0, why: "Rates change in percentage points." },
  { q: "For a 2-mark 'identify two' part, the best answer is:", opts: ["Two short named points", "A paragraph of analysis", "One long sentence", "A diagram"], a: 0, why: "Identify needs names, not explanation." },
] });
Lib.cards($("#fc1"), { cards: [
  ["AO1", "Recall, understanding, application."],
  ["Weighting", "35% overall, 33% of Paper 4, 47% of Paper 3."],
  ["Diagram cap", "No required diagram: 14-mark scale capped at Level 2."],
  ["Percentage points", "For changes in a rate."],
  ["Swap test", "Change the country. If it still reads, it is not applied."],
  ["Define once", "Early, precisely, then move on."],
  ["Quote data", "Number, unit, year, what it shows."],
  ["Multiplier", "1 ÷ (1 − MPC)."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "Which statement is a precise definition of productive efficiency?", opts: ["Output is produced at the lowest possible average cost", "Firms make a large profit", "Resources are used in a way that is fair", "Output rises over time"], a: 0, why: "Productive efficiency is lowest average cost, at the minimum of the AC curve." },
  { q: "A firm's price elasticity of demand for its product is -2.5. A 4% price rise leads to what change in quantity demanded?", opts: ["a fall of 10%", "a fall of 1.6%", "a rise of 10%", "a fall of 4%"], a: 0, why: "-2.5 × 4% = -10%." },
  { q: "The marginal propensity to consume is 0.75 and there are no other leakages. What is the multiplier?", opts: ["4", "1.33", "0.75", "0.25"], a: 0, why: "1 ÷ (1 − 0.75) = 4." },
  { q: "The export price index is 120 and the import price index is 100. What is the terms of trade?", opts: ["120", "83.3", "100", "20"], a: 0, why: "(120 ÷ 100) × 100 = 120, an improvement from a base of 100." },
  { q: "Unemployment rises from 5% to 6%. Which description is correct?", opts: ["a rise of 1 percentage point", "a rise of 1%", "a rise of 6%", "a fall of 1 point"], a: 0, why: "A change in a rate is described in percentage points; in relative terms it is 20%." },
] });
