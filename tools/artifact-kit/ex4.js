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

$("#pic1").innerHTML = (() => {
  const B = [["First pass", "35 to 40 min", "Do the sure ones, tick the doubtful", 20, "f2", 330], ["Second pass", "15 to 20 min", "Calculations, diagrams, elimination", 360, "f1", 230], ["Check", "5 min", "No blanks; right row", 600, "f3", 140]];
  let o = ""; B.forEach(([n, t, d, x, c, w]) => { o += SV.rect(x, 12, w, 90, c, { rx: 12, ...op(0.45) }) + SV.text(x + w / 2, 40, n, "lbl bd", { "text-anchor": "middle", style: "font-size:16px" }) + SV.text(x + w / 2, 62, t, "sm", { "text-anchor": "middle" }) + SV.text(x + w / 2, 84, d, "sm", { "text-anchor": "middle" }); });
  return `<svg viewBox="0 0 760 114" role="img" aria-label="Plan for the 60 minutes of Paper 1">${o}</svg>`;
})();
chainStep("#stA", "The four steps on a real question", ["Read: 'What is not an example of protectionism?' Underline 'not'", "Predict: three options restrict imports or help exporters; one does the opposite", "Test: export subsidies help exporters; quotas and tariffs restrict imports; import subsidies encourage imports", "Check: the odd one out is import subsidies"], [
  "<b>Step 1:</b> the word 'not' reverses the usual question.", "<b>Step 2:</b> decide what the answer should look like.", "<b>Step 3:</b> test every option against the definition.", "<b>Step 4:</b> answer B (import subsidies)."]);
chainStep("#stB", "A calculation question", ["Question: nominal GDP rose to $577.5bn and prices rose 5%. What is real GDP?", "Write the formula: real GDP = nominal GDP ÷ price index × 100", "Substitute: 577.5 ÷ 1.05", "Answer: $550bn; check the options for it", "Trap: multiplying by 0.95 or by 1.05 gives wrong options"], [
  "<b>Read:</b> the data is nominal; the question asks for real.", "<b>Formula first.</b>", "<b>Substitute</b> carefully.", "<b>Check</b> that the answer is in the options.", "<b>Wrong options</b> come from the wrong operation."]);
chainStep("#stC", "A two-part combination question", ["Question: a worse current account: effect on the exchange rate and on cost-push inflation?", "Part 1: more imports and fewer exports, so the currency falls (depreciate)", "Part 2: a weaker currency makes imports dearer, so costs rise (inflation increases)", "Find the option with both: depreciate and increase", "The other options each have one part wrong"], [
  "<b>Split the question.</b>", "<b>Work out part 1.</b>", "<b>Work out part 2.</b>", "<b>Match both parts</b> to one option.", "<b>Half-right options</b> are the distractors."]);

function tp() {
  const ids = ["fp", "ex"];
  if (!ids.every((i) => $("#" + i))) return;
  const fp = +$("#fp").value, ex = +$("#ex").value, ck = 5, sp = 60 - fp - ck;
  const per = fp / 30; $("#r1").textContent = Lib.fmtN(per, 1) + " min";
  $("#r2").textContent = sp + " min"; $("#r3").textContent = ex + " (about " + Lib.fmtN(sp / Math.max(ex, 1), 1) + " min each)";
  $("#rv").textContent = `With ${fp} minutes on the first pass (${Lib.fmtN(per, 1)} minutes per question) and ${ck} minutes to check, you have ${sp} minutes for the ${ex} questions you postponed: about ${Lib.fmtN(sp / Math.max(ex, 1), 1)} minutes each. ` + (per > 1.4 ? "The first pass is slow; leave long questions earlier." : per < 1 ? "The first pass is quick: check each answer as you go." : "A balanced plan.");
  const W = 380, X = (v) => 20 + (v / 60) * W;
  $("#labA").innerHTML = SV.rect(X(0), 70, X(fp) - X(0), 50, "f2", op(0.5)) + SV.rect(X(fp), 70, X(fp + sp) - X(fp), 50, "f1", op(0.5)) + SV.rect(X(fp + sp), 70, X(60) - X(fp + sp), 50, "f3", op(0.5)) + SV.text(X(fp / 2), 100, "Pass 1: " + fp, "sm", { "text-anchor": "middle" }) + SV.text(X(fp + sp / 2), 100, "Pass 2: " + sp, "sm", { "text-anchor": "middle" }) + SV.text(X(60) - 6, 160, "Check " + ck, "sm", { "text-anchor": "end" });
}
Lib.slider($("#g1"), { id: "fp", label: "Minutes on the first pass ", min: 25, max: 45, step: 1, value: 38, fmt: (v) => v, onInput: tp });
Lib.slider($("#g2"), { id: "ex", label: "Questions postponed to the second pass ", min: 0, max: 15, step: 1, value: 6, fmt: (v) => v, onInput: tp });
tp();

chooser("h", [
  ["'Which type of good is healthcare?'", "Recall and definition", "Answer before looking at the options", "Mixing merit and public goods", 5],
  ["'What is the real GDP in year 2?'", "Calculation", "Write the formula and substitute", "Using nominal instead of real figures", 5],
  ["'What is not an example of protectionism?'", "'Not' question", "Test each option; find the odd one", "Choosing the first option that is true", 5],
  ["'How will this affect the exchange rate and inflation?'", "Two-part combination", "Work out each part separately", "Getting one part right and guessing the other", 4],
  ["'What is the current account balance?' (table)", "Table or data", "Sum the balances with signs", "Forgetting a deficit is negative", 4],
  ["'Which statement is normative?'", "Positive or normative", "Look for 'should' or a value judgement", "Choosing a prediction with 'definitely'", 3],
  ["'Which area represents total revenue?' (diagram)", "Diagram", "Mark price × quantity on the diagram", "Using the wrong price or quantity", 4]
], (it) => `${it[0]} Type: ${it[1].toLowerCase()}. First move: ${it[2].toLowerCase()}. Trap: ${it[3].toLowerCase()}.`, "How often this type appears");
chooser("k", [
  ["Real GDP from nominal GDP", "Nominal ÷ price index × 100", "Nominal × price index ÷ 100", "It inflates the figure instead of removing the price rise", 5],
  ["Price elasticity of demand", "% change in quantity ÷ % change in price", "Change in quantity ÷ change in price (absolute)", "Elasticity uses percentages", 5],
  ["Income per head when income +10% and population −10%", "1.10 ÷ 0.90 = 1.22 (up 22%)", "10% + 10% = 20%", "A fall in the denominator raises the ratio by more than 20%", 4],
  ["Percentage change from 4% to 6%", "50% rise (2 ÷ 4)", "2% rise", "Two percentage points is not the same as 2%", 4],
  ["Terms of trade index", "(Export price index ÷ import price index) × 100", "Import ÷ export", "It reverses the meaning of improvement", 4],
  ["Current account balance from a table", "Sum the balances: goods, services, primary and secondary income, with signs", "Add exports only", "Ignores imports and payments", 4]
], (it) => `${it[0]}: ${it[1]}. Trap: ${it[2]}. ${it[3]}.`, "How common the trap is");
Lib.classify($("#cl1"), { prompt: "Which type of question is it?", buckets: [{"label": "Recall"}, {"label": "Calculation"}, {"label": "'Not' question"}, {"label": "Combination"}], items: [{"text": "Which type of good is healthcare?", "b": 0}, {"text": "What is the real GDP in year 2?", "b": 1}, {"text": "What is not an aim of protectionism?", "b": 2}, {"text": "How is this likely to affect the exchange rate and inflation?", "b": 3}, {"text": "What is the definition of long run?", "b": 0}, {"text": "What is the unemployment rate for these figures?", "b": 1}, {"text": "Which statement is least likely to be true?", "b": 2}, {"text": "Which combination correctly describes good X?", "b": 3}], done: "Recall questions ask for a fact; calculations need numbers; 'not' questions need the false option; combinations have two parts." });
Lib.classify($("#cl2"), { prompt: "Which distractor is it?", buckets: [{"label": "Reversed relationship"}, {"label": "True but irrelevant"}, {"label": "Calculation slip"}], items: [{"text": "A depreciation makes imports cheaper", "b": 0}, {"text": "Nominal GDP is higher than real GDP when prices rise (a true statement in a question about growth)", "b": 1}, {"text": "Choosing 20% when the answer needs 1.10 ÷ 0.90", "b": 2}, {"text": "A rise in interest rates lowers the cost of borrowing", "b": 0}, {"text": "A correct fact about GNI in a question on GDP", "b": 1}, {"text": "Forgetting to deflate before comparing", "b": 2}], done: "Wrong options are built to catch particular mistakes." });
Lib.order($("#o1"), { prompt: "Put the four steps in order.", items: ["Read the stem twice and underline the key words", "Predict the answer before looking at the options", "Test every option and cross out the wrong ones", "Check units, signs and direction, then answer"], done: "Read, predict, test, check." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Not, least likely", "Find the false option"], ["Always, only", "Usually makes a statement false"], ["Most likely", "Several options may be true; choose the best"], ["Percentage point", "A difference between two percentages"], ["Normative", "Contains a value judgement such as 'should'"], ["Real", "Adjusted for inflation"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "Paper 1 has 30 questions in 60 minutes. How many minutes per question?", "a": 2, "unit": "min", "tol": 0.05, "hint": "60 ÷ 30.", "sol": "<b>2 minutes</b>."},
  {"q": "Nominal GDP is $660bn and the price index is 120. What is real GDP ($bn)?", "a": 550, "unit": "$bn", "tol": 0.5, "hint": "660 ÷ 1.20.", "sol": "<b>$550bn</b>."},
  {"q": "Price rises 20% and quantity demanded falls 30%. What is the price elasticity of demand (size)?", "a": 1.5, "unit": "", "tol": 0.05, "hint": "30 ÷ 20.", "sol": "<b>1.5</b>."},
  {"q": "A rate rises from 4% to 6%. By what percentage has it risen?", "a": 50, "unit": "%", "tol": 0.5, "hint": "2 ÷ 4.", "sol": "<b>50%</b>, a rise of 2 percentage points."},
  {"q": "Goods −30, services +10, primary income +15, secondary income −5 ($bn). What is the current account balance ($bn)?", "a": -10, "unit": "$bn", "tol": 0.5, "hint": "−30 + 10 + 15 − 5.", "sol": "<b>−$10bn</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "How many marks does Paper 1 carry at AS Level?", opts: ["20", "30", "40", "60"], a: 1, why: "30 questions, 1 mark each." },
  { q: "According to the paper instructions, how is a correct answer rewarded?", opts: ["One mark, with no deduction mentioned for a wrong answer", "Two marks", "Half a mark", "One mark minus a penalty for errors"], a: 0, why: "Each correct answer will score one mark; no penalty is stated." },
  { q: "A question says 'which is not...'. What should you do?", opts: ["Find the false option", "Find the true option", "Skip it", "Choose the longest option"], a: 0, why: "Three options will be true." },
  { q: "Why predict the answer before reading the options?", opts: ["It stops you being pulled to a plausible distractor", "It saves paper", "It is compulsory", "Options are random"], a: 0, why: "A prediction guards against distractors." },
  { q: "About how long is available for each question on average?", opts: ["1 minute", "2 minutes", "4 minutes", "5 minutes"], a: 1, why: "60 minutes for 30 questions." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Paper 1", "30 questions, 60 minutes, 30 marks."],
  ["Four steps", "Read, predict, test, check."],
  ["No penalty", "Answer every question."],
  ["Distractors", "Reversed, wrong curve, true but irrelevant, slip."],
  ["Not question", "Find the false option."],
  ["Calculations", "Formula, percentages, signs."],
  ["Time", "2 minutes each; leave and return."],
  ["Normative", "'Should' = value judgement."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "Which type of good is healthcare? (May/June 2020 · 13 · Q3, reworded)", opts: ["demerit", "free", "merit", "public"], a: 2, why: "Recall: healthcare is more beneficial than consumers realise." },
  { q: "In year 1, a country's real GDP was $500 billion. In year 2, nominal GDP rose to $577.5 billion and the prices increased by 5%. What is the real GDP in year 2? (May/June 2023 · 13 · Q20, reworded)", opts: ["$4.76 billion", "$5 billion", "$476 billion", "$550 billion"], a: 3, why: "Calculation: 577.5 ÷ 1.05 = 550. The $476 billion option multiplies by 0.825 instead of dividing." },
  { q: "Following the introduction of a 10% increase in charges for car parking in a city centre, the demand for bus journeys per day into the city rose from 800 to 1000. What was the cross elasticity of demand for bus journeys with respect to car parking charges? (May/June 2020 · 12 · Q8, reworded)", opts: ["-0.4", "+0.4", "+2.0", "+2.5"], a: 3, why: "Calculation: demand rose 25%; the price rose 10%; XED = 25 ÷ 10 = +2.5. Options -0.4 and +0.4 come from inverting the ratio." },
  { q: "A government introduces a subsidy for product X and the market price of X falls by 5%. The cross elasticity of demand for product Y, with respect to the price of X, is +0.4. What will happen to the demand for product Y? (May/June 2021 · 11 · Q10, reworded)", opts: ["It will decrease by 2%.", "It will decrease by 12.5%.", "It will increase by 2%.", "It will increase by 12.5%."], a: 0, why: "Calculation with a sign: 0.4 × (−5%) = −2%." },
  { q: "An extract from a country's balance of payments ($ billion): trade in goods, exports 150 and imports 200; trade in services, exports 70 and imports 50; primary income, receipts 120 and payments 100; secondary income, receipts 15 and payments 20. What is the current account balance? (Feb/March 2024 · 12 · Q27, reworded)", opts: ["-$10bn", "-$15bn", "-$30bn", "-$50bn"], a: 1, why: "Table: (150 − 200) + (70 − 50) + (120 − 100) + (15 − 20) = −50 + 20 + 20 − 5 = −15." },
  { q: "A good has a price elasticity of supply of 2.0. The current quantity supplied is 300 units per week at a market price of $20 per unit. The firm raises the price to $25 per unit. What will the new quantity supplied be per week? (May/June 2020 · 12 · Q10, reworded)", opts: ["150 units", "375 units", "400 units", "450 units"], a: 3, why: "Calculation: price +25%, so quantity +50%: 300 × 1.5 = 450." },
  { q: "A manufacturer progressively reduces the price of his product. The table shows total revenue of $750 (000s) at prices of $10, $9 and $8. What is the price elasticity of demand for the product? (May/June 2020 · 12 · Q6, reworded)", opts: ["perfectly inelastic", "relatively inelastic", "perfectly elastic", "unitary"], a: 3, why: "Table: revenue is constant as price falls, so demand is unitary." },
  { q: "Which statement about a market economy is not correct? (Feb/March 2025 · 12 · Q1, reworded)", opts: ["Competition is promoted among firms which can increase productive efficiency", "Immobility of the factors of production can lead to allocative inefficiency", "Price always reflects all the costs and all the benefits associated with production", "The entrepreneur is encouraged to innovate and take risks, motivated by profit"], a: 2, why: "'Not correct': 'always' makes C false, since prices ignore external costs." },
  { q: "What is not an aim of protectionism? (May/June 2021 · 13 · Q20, reworded)", opts: ["to improve balance of trade", "to increase price of exports", "to protect infant industries", "to reduce the volume of imports"], a: 1, why: "'Not an aim': protectionism aims to cut imports and protect industries, not to raise export prices." },
  { q: "What does not happen when price acts as a means to allocate resources? (May/June 2022 · 12 · Q12, reworded)", opts: ["Price determines the supply of public goods", "Price operates in the markets for both goods and factors of production", "Price recognises consumers' ability to pay rather than their needs", "Price signals to producers which goods are most profitable"], a: 0, why: "Test each statement: public goods are not supplied through the price mechanism." },
  { q: "Increased international competition leads to a worsening in a country's current account balance. In the absence of any offsetting factors, how is this likely to affect the exchange rate and domestic cost-push inflation? (exchange rate, cost-push inflation) (May/June 2021 · 12 · Q27, reworded)", opts: ["appreciate, decrease", "appreciate, increase", "depreciate, decrease", "depreciate, increase"], a: 3, why: "Two parts: worse current account lowers the rate; a lower rate raises import costs and cost-push inflation." },
  { q: "The price elasticity of demand for good X is -2.4, its income elasticity of demand is -0.4 and the cross elasticity of demand for good X with respect to good Y is +0.8. What is the correct description of good X? (Feb/March 2024 · 12 · Q7, reworded)", opts: ["inferior good, price-elastic demand and substitute for good Y", "inferior good, price-inelastic demand and complement to good Y", "normal good, price-elastic demand and complement to good Y", "normal good, price-inelastic demand and substitute for good Y"], a: 0, why: "Three parts: YED negative: inferior; PED size 2.4: elastic; XED positive: substitute." },
  { q: "Good X is related to good Y. Incomes increase and the price of good Y falls. Which combination would give the greatest increase in demand for good X? (nature of good X, relationship between X and Y) (Feb/March 2020 · 12 · Q8, reworded)", opts: ["inferior good, complements", "inferior good, substitutes", "normal good, complements", "normal good, substitutes"], a: 2, why: "Two parts: higher income raises demand for a normal good; a fall in the price of a complement raises demand for X." },
  { q: "Which is a normative statement? (May/June 2020 · 13 · Q4, reworded)", opts: ["If interest rates fall consumption is likely to increase.", "If interest rates fall consumption will definitely increase.", "Interest rates and consumption are usually inversely related.", "The rate of interest should be reduced."], a: 3, why: "Normative: 'should' is a value judgement." },
  { q: "A government decides to allow the country's currency to depreciate to remove the deficit on its current account. What is the most likely reason why this would not work? (Feb/March 2024 · 12 · Q25, reworded)", opts: ["The country gains a competitive advantage from the depreciation.", "The country has a surplus on its capital and financial accounts.", "The price elasticities of demand for the country's exports and imports are greater than one.", "There are high trade barriers with the country's main trading partners."], a: 3, why: "Cause and effect: options A and C would help; trade barriers limit export gains." },
  { q: "The money income of a country rises by 10% whereas its population falls by 10% during a year. What is likely to happen to the national income per head? (Feb/March 2025 · 12 · Q19, reworded)", opts: ["It will remain unchanged", "It will rise by exactly 20%", "It will rise by less than 20%", "It will rise by more than 20%"], a: 3, why: "Calculation trap: 1.10 ÷ 0.90 = 1.22, which is more than 20%, not exactly 20%." },
] });
