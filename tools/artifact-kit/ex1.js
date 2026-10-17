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

chainStep("#stA", "Building a full-mark definition: price elasticity of demand", ["Start with the idea: the responsiveness of quantity demanded to a change in price", "Add the measure: percentage change in quantity demanded divided by percentage change in price", "Add the size meaning: elastic if the percentage change in quantity is greater than the change in price", "Check: no repeating the term, no vague words like 'how much'"], [
  "<b>Key idea (1 mark).</b>", "<b>Formula (1 mark).</b>", "<b>Meaning of elastic and inelastic in percentage terms (1 mark).</b>", "<b>Three AO1 marks</b> for a full answer."]);
chainStep("#stB", "The three AO1 marks for an elasticity answer", ["Mark 1: what it measures: responsiveness of demand to price", "Mark 2: the correct formula", "Mark 3: elastic and inelastic in percentage terms", "Then move to analysis: effect on revenue; evaluation: elasticity changes along the curve"], [
  "<b>Meaning.</b>", "<b>Formula.</b>", "<b>Interpretation.</b>", "<b>AO1 is the base; analysis builds on it.</b>"]);
const dgLab = { x: "Quantity", y: "Price", D1: "D", S1: "S", S2: "S1", P1: "P", Q1: "Q", P2: "P1", Q2: "Q1" };
Lib.stepper($("#stC"), { w: 760, h: 300, label: "Drawing a subsidy diagram for the AO1 marks", base: { s: 0, n: 0, g: 0 }, draw: (s) => sdPlot({ d: 0, s: s.s, g: s.g, n: s.n }, dgLab), tween: 800, dwell: 5200, steps: [
  { cap: "<b>1 mark:</b> axes labelled (price, quantity); D and S labelled; original equilibrium shown with P and Q marked.", s: { s: 0, n: 0, g: 1 } },
  { cap: "<b>An increase in subsidy shifts supply to the right</b> (to S1): costs fall.", s: { s: 20, n: 1, g: 1 } },
  { cap: "<b>Mark the new equilibrium</b> (P1, Q1): price falls and quantity rises. This earns the diagram mark; the analysis marks need the explanation in words.", s: { s: 20, n: 1, g: 1 } },
] });

function ao1() {
  const items = [["m", "What it measures: the responsiveness of quantity demanded to a change in price"], ["f", "The correct formula: % change in quantity demanded ÷ % change in price"], ["i", "Elastic and inelastic explained in percentage terms"], ["x", "A vague phrase like 'how much demand changes' only"], ["e", "An example with no definition"]];
  const on = items.map((it, i) => !!$("#ck" + i) && $("#ck" + i).checked);
  const m = on[0] ? 1 : 0, f = on[1] ? 1 : 0, i = on[2] ? 1 : 0, total = m + f + i;
  $("#r1").textContent = total + " / 3";
  const miss = [m ? "" : "meaning", f ? "" : "formula", i ? "" : "elastic and inelastic in % terms"].filter(Boolean);
  $("#r2").textContent = miss.length ? miss.join(", ") : "Nothing: full AO1 marks";
  $("#rv").textContent = `Ticked: ${on.filter(Boolean).length} item(s). ` + (on[3] && !on[0] ? "A vague phrase is not credited as the meaning. " : "") + (on[4] && !on[0] ? "An example without a definition does not earn the meaning mark. " : "") + (total === 3 ? "All three AO1 marks are earned; the next step is analysis (the effect on revenue) and evaluation." : `${total} AO1 mark(s). Add: ${miss.join("; ")}.`);
}
$("#chk").innerHTML = ["What it measures: the responsiveness of quantity demanded to a change in price", "The correct formula: % change in quantity demanded ÷ % change in price", "Elastic and inelastic explained in percentage terms", "A vague phrase like 'how much demand changes' only", "An example with no definition"].map((t, i) => `<label style="display:block;margin:6px 0"><input type="checkbox" id="ck${i}"> ${t}</label>`).join("");
[0, 1, 2, 3, 4].forEach((i) => ($("#ck" + i).onchange = ao1));
ao1();

chooser("h", [
  ["Price elasticity of demand", "How elastic demand is.", "How much demand changes when price changes.", "The responsiveness of quantity demanded to a change in price: % change in quantity demanded ÷ % change in price.", 5],
  ["Opportunity cost", "The cost of something.", "What you give up.", "The value of the next best alternative given up when a choice is made.", 4],
  ["Merit good", "A good that is good for you.", "A good that is under-consumed.", "A good more beneficial than consumers realise, so under-consumed and under-provided in a free market.", 4],
  ["Inflation", "Prices going up.", "A rise in prices.", "A sustained rise in the general price level.", 3],
  ["Real GDP", "GDP in real terms.", "GDP adjusted for prices.", "GDP adjusted for inflation, so it shows the change in the quantity of output.", 4],
  ["Terms of trade", "How good trade is.", "Export prices and import prices.", "The ratio of export prices to import prices, (export price index ÷ import price index) × 100.", 4]
], (it) => `${it[0]}. Weak: "${it[1]}" Partial: "${it[2]}" Full: "${it[3]}"`, "Marks at stake for the definition");
chooser("k", [
  ["Supply and demand shift", "Axes, D and S labelled, equilibrium, the shift labelled, new equilibrium", "Forgetting to label the shifted curve or the new price and quantity", "1 to 2", 3],
  ["Indirect tax", "Supply shifts left by the tax, vertical gap equal to the tax, prices paid and received", "Showing the demand curve shifting", "2", 4],
  ["Maximum price", "Control line below equilibrium, shortage shown", "Drawing the line above equilibrium", "2", 4],
  ["AD/AS", "Price level and real output on axes, AD and SRAS, the shift and new equilibrium", "Using price and quantity as the axes", "2", 4],
  ["Currency market", "Exchange rate on the vertical axis, demand and supply of the currency, the shift", "Shifting the wrong curve for the cause", "1 to 2", 3],
  ["Tariff", "World price, price with tariff, the quantities of imports before and after", "Drawing a tariff without labelling quantities", "2", 3]
], (it) => `${it[0]}: include ${it[1].toLowerCase()}. Common slip: ${it[2].toLowerCase()}. Marks at stake: about ${it[3]}.`, "Importance of labelling");
Lib.classify($("#cl1"), { prompt: "Which assessment objective does the skill show?", buckets: [{"label": "AO1 Knowledge"}, {"label": "AO2 Analysis"}, {"label": "AO3 Evaluation"}], items: [{"text": "Define price elasticity of demand", "b": 0}, {"text": "Write the formula for real GDP", "b": 0}, {"text": "Explain why a tax raises price and cuts quantity", "b": 1}, {"text": "Show that a rise in AD raises output and prices using a diagram", "b": 1}, {"text": "Judge whether a policy is the best option and say why", "b": 2}, {"text": "Conclude that it depends on the elasticity of demand", "b": 2}], done: "AO1 is recall and understanding; AO2 explains causes and effects; AO3 weighs and judges." });
Lib.classify($("#cl2"), { prompt: "Is it a full-mark definition?", buckets: [{"label": "Full credit"}, {"label": "Not enough"}], items: [{"text": "Inflation is a sustained rise in the general price level.", "b": 0}, {"text": "Inflation is prices going up.", "b": 1}, {"text": "Real GDP is GDP adjusted for inflation.", "b": 0}, {"text": "Real GDP is real.", "b": 1}, {"text": "A merit good is more beneficial than consumers realise, so it is under-consumed.", "b": 0}, {"text": "A merit good is a good that is good.", "b": 1}], done: "A full definition gives the key idea and the qualifier." });
Lib.order($("#o1"), { prompt: "Put the calculation steps in order.", items: ["Write the formula", "Substitute the figures", "Work out the answer", "Add the unit and check the sign", "Check it is sensible"], done: "Formula, substitute, answer, units." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Price elasticity of demand", "% change in quantity demanded ÷ % change in price"], ["Terms of trade", "(export price index ÷ import price index) × 100"], ["Real GDP", "Nominal GDP ÷ price index × 100"], ["Unemployment rate", "Unemployed ÷ labour force × 100"], ["GDP by expenditure", "C + I + G + (X − M)"], ["Marginal rate of tax", "Change in tax ÷ change in income"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "Price rises 10% and quantity demanded falls 25%. What is the price elasticity of demand (size)?", "a": 2.5, "unit": "", "tol": 0.05, "hint": "25 ÷ 10.", "sol": "<b>2.5</b>, elastic."},
  {"q": "Nominal GDP is $660bn and the price index is 120. What is real GDP ($bn)?", "a": 550, "unit": "$bn", "tol": 0.5, "hint": "660 ÷ 1.20.", "sol": "<b>$550bn</b>."},
  {"q": "The export price index is 105 and the import price index is 95. What are the terms of trade (1 decimal place)?", "a": 110.5, "unit": "", "tol": 0.1, "hint": "(105 ÷ 95) × 100.", "sol": "<b>110.5</b>."},
  {"q": "Goods balance −40, services +25, primary income +10, secondary income −5 ($bn). What is the current account balance ($bn)?", "a": -10, "unit": "$bn", "tol": 0.5, "hint": "−40 + 25 + 10 − 5.", "sol": "<b>−$10bn</b>."},
  {"q": "2 million are unemployed and 30 million are employed. What is the unemployment rate (%, 2 decimal places)?", "a": 6.25, "unit": "%", "tol": 0.05, "hint": "2 ÷ 32.", "sol": "<b>6.25%</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "How many AO1 marks are typically available in an 8 mark essay part from 2023?", opts: ["1", "2", "3", "5"], a: 2, why: "AO1 3, AO2 3, AO3 2." },
  { q: "Which earns full credit as a definition of inflation?", opts: ["Prices going up", "A sustained rise in the general price level", "Inflation is inflation", "The cost of living"], a: 1, why: "Key idea with the qualifier 'sustained'." },
  { q: "A question says 'with the help of a formula'. What is it signalling?", opts: ["A mark is available for a correct formula", "Only a calculation is needed", "No definition is needed", "Evaluation marks"], a: 0, why: "It is an AO1 mark." },
  { q: "Why is a key term used without understanding not credited?", opts: ["The generic principles say examiners need evidence it is understood", "Examiners dislike key terms", "Terms are not marked", "It is repeated"], a: 0, why: "Credit needs evidence of understanding." },
  { q: "A diagram has no labels. Likely AO1 credit?", opts: ["Little or none", "Full marks", "Evaluation marks", "Double marks"], a: 0, why: "Labelling is part of accuracy." },
] });
Lib.cards($("#fc1"), { cards: [
  ["AO1", "Knowledge and understanding."],
  ["8 mark part", "3 AO1 marks (2 before 2023)."],
  ["12 mark part", "AO1 + AO2 in Table A out of 8."],
  ["Definition", "Key idea + qualifier."],
  ["Formula", "Learn exactly."],
  ["Diagram", "Axes, curves, shift, equilibrium."],
  ["Calculation", "Formula, working, unit."],
  ["Key terms", "Credit needs understanding."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "Which type of good is healthcare? (May/June 2020 · 13 · Q3, reworded)", opts: ["demerit", "free", "merit", "public"], a: 2, why: "Healthcare is more beneficial than consumers realise, so it is a merit good." },
  { q: "What is a necessary characteristic of a public good? (May/June 2020 · 11 · Q18, reworded)", opts: ["It has a fixed maximum price.", "It has an opportunity cost of production of zero.", "It is non-excludable.", "It is an essential good."], a: 2, why: "Non-excludability is a defining characteristic." },
  { q: "What is the measure of cross-elasticity of demand for good X in terms of good Y? (Feb/March 2022 · 12 · Q8, reworded)", opts: ["the change in the demand for X divided by the change in the price of Y", "the change in the price of X divided by the change in the demand for Y", "the percentage change in the demand for X divided by the percentage change in the price of Y", "the percentage change in the demand for Y divided by the percentage change in the price of X"], a: 2, why: "A percentage formula, with X's demand on top and Y's price below." },
  { q: "What is a statement of the non-rivalrous nature of public goods? (May/June 2025 · 12 · Q3, reworded)", opts: ["It is not possible to stop a non-payer from using the product.", "One person consuming the product does not reduce the amount of it available to others.", "People consume too little of the product because they are unaware of its true benefits.", "There is an unlimited supply of the product."], a: 1, why: "Non-rival means one person's use does not reduce what is available to others." },
  { q: "Which statement is correct? (Oct/Nov 2020 · 12 · Q2, reworded)", opts: ["Private goods are both non-rival and non-excludable.", "Private goods are only provided by the private sector.", "Public goods are both non-rival and non-excludable.", "Public goods do not incur opportunity costs."], a: 2, why: "A definition recall question." },
  { q: "What is the definition of long run? (Feb/March 2023 · 12 · Q2, reworded)", opts: ["the time period when all factors of production are specialised", "the time period when all factors of production are variable", "the time period when all key inputs into production are variable", "the time period when at least one factor of production is fixed"], a: 1, why: "In the long run all factors can be varied." },
  { q: "What is not an example of a public good? (May/June 2024 · 13 · Q1, reworded)", opts: ["education", "flood control systems", "national defence", "street lighting"], a: 0, why: "Education is a merit good." },
] });
