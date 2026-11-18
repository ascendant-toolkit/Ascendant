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

strip("#pic1", "From a statement to a developed chain", [["Statement", "a claim | no reason"], ["One step", "a claim | and a reason"], ["Chain", "linked steps | to the objective"], ["Applied chain", "linked steps | in this context"]]);
chainStep("#stA", "A chain from trigger to objective", ["Trigger: the central bank raises the interest rate", "Mechanism: borrowing costs rise and saving pays more", "Effect: consumption and investment fall, so AD shifts left", "Consequence: real GDP and the price level fall", "Objective: inflation falls, but unemployment may rise"],
  ["<b>Trigger</b> named in the question.", "<b>Mechanism</b>: why behaviour changes.", "<b>Effect</b> on the diagram.", "<b>Consequence</b> for the economy.", "<b>Objective</b> named, with the trade-off."]);
chainStep("#stB", "A chain with an externality diagram", ["Free market: output where MPB = MPC, above the social optimum", "Marginal social cost is above MPC because of the pollution", "A tax equal to the external cost shifts supply left", "Price rises and output falls towards MSB = MSC", "The welfare loss triangle disappears: allocative efficiency"],
  ["<b>Free market</b> over-produces.", "<b>The gap</b> between MSC and MPC is the external cost.", "<b>The tax</b> internalises it.", "<b>The result</b> is on the diagram.", "<b>The objective</b> in the question's words."]);
chainStep("#stC", "From a number to a cause", ["Select: unemployment fell from 9.1% to 7.4% between 2015 and 2019", "Calculate: a fall of 1.7 percentage points", "Pattern: growth in the same period averaged 3.2% a year", "Cause: with growth above trend, firms may have hired more workers", "Limit: other factors such as emigration could also have lowered the rate"],
  ["<b>Select</b> the relevant figures.", "<b>Calculate</b> with the correct unit.", "<b>Pattern</b> across the data.", "<b>Cause</b> suggested, not asserted.", "<b>Limit</b> stated."]);

function ev() {
  const ids = ["ch", "dv", "dg", "ap"];
  if (!ids.every((i) => $("#" + i))) return;
  const [ch, dv, dg, ap] = ids.map((i) => +$("#" + i).value);
  let m = Math.min(3, ch) * 2.2 * (0.55 + 0.25 * dv) + dg * 1.2 + ap * 1.2 + Math.min(ch, 1) * 0.6;
  m = Math.round(Math.max(0, Math.min(14, m)));
  if (dg === 0) m = Math.min(m, 10);
  if (ch === 0) m = Math.min(m, 3);
  if (dv === 0) m = Math.min(m, 7);
  const L = m >= 11 ? 3 : m >= 6 ? 2 : m >= 1 ? 1 : 0;
  $("#r1").textContent = m + " / 14"; $("#r2").textContent = L ? "Level " + L : "No credit";
  $("#r3").textContent = dg === 0 ? "Add the diagram the question names (capped at Level 2 without it)" : ch < 3 ? "Add a third chain" : dv < 2 ? "Take each chain all the way to the objective" : ap < 2 ? "Apply each chain to the context" : m >= 14 ? "At the top" : "Check the logic and organisation";
  $("#rv").textContent = `${ch} chain(s), development ${["thin", "some", "full"][dv]}, diagram ${["missing", "partly used", "correct and used"][dg]}, application ${["none", "some", "throughout"][ap]}: about ${m} out of 14 (${L ? "Level " + L : "no credit"}).`;
  const W = 340, X = (v) => 40 + (v / 14) * W;
  let o = SV.rect(X(0), 70, X(5) - X(0), 40, "f2", op(0.4)) + SV.rect(X(5), 70, X(10) - X(5), 40, "f1", op(0.4)) + SV.rect(X(10), 70, X(14) - X(10), 40, "f3", op(0.4)) + SV.text(X(2.5), 95, "L1", "lbl bd", { "text-anchor": "middle" }) + SV.text(X(7.5), 95, "L2", "lbl bd", { "text-anchor": "middle" }) + SV.text(X(12), 95, "L3", "lbl bd", { "text-anchor": "middle" });
  o += SV.line(X(m), 50, X(m), 130, "c4", { "stroke-width": 3 }) + SV.text(X(m), 44, m + "", "lbl bd", { "text-anchor": "middle" });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "ch", label: "Developed chains (0 to 4) ", min: 0, max: 4, step: 1, value: 2, fmt: (v) => v, onInput: ev });
Lib.slider($("#g2"), { id: "dv", label: "Development: 0 thin, 1 some, 2 full to the objective ", min: 0, max: 2, step: 1, value: 1, fmt: (v) => ["thin", "some", "full"][v], onInput: ev });
Lib.slider($("#g3"), { id: "dg", label: "Diagram: 0 missing, 1 partly used, 2 correct and used ", min: 0, max: 2, step: 1, value: 1, fmt: (v) => ["missing", "partly used", "correct and used"][v], onInput: ev });
Lib.slider($("#g4"), { id: "ap", label: "Application: 0 none, 1 some, 2 throughout ", min: 0, max: 2, step: 1, value: 1, fmt: (v) => ["none", "some", "throughout"][v], onInput: ev });
ev();

chooser("h", [
  ["because", "Firms cut investment.", "Firms cut investment because the cost of borrowing exceeds the expected return on more projects.", "A reason for the first step", 5],
  ["so", "AD falls.", "Investment is a component of AD, so AD shifts left.", "A consequence on the model", 5],
  ["which means", "Output rises.", "Output rises, which means more workers are needed.", "The next effect", 4],
  ["leading to", "Prices fall.", "Lower AD reduces demand-pull pressure, leading to a lower price level.", "The route to the objective", 4],
  ["as a result", "Inflation is lower.", "As a result, inflation falls towards the target, although unemployment could rise.", "The objective in the question", 5]
], (it) => `Link: ${it[0]}. Without: "${it[1]}" With: "${it[2]}" Adds: ${it[3].toLowerCase()}.`, "How often this link is needed");
chooser("k", [
  ["Tax cut to inflation", "Tax cut → inflation rises", "The step through disposable income, spending and AD", "A tax cut raises disposable income, so spending rises, shifting AD right and pushing the price level up.", 5],
  ["Subsidy to output", "Subsidy → output rises", "Why costs fall and which curve shifts", "A subsidy lowers marginal cost, shifting supply right, so price falls and output rises.", 4],
  ["Depreciation to current account", "Depreciation → exports rise", "Price in foreign currency and elasticity", "A depreciation lowers export prices abroad, so the quantity sold may rise if demand is elastic.", 5],
  ["Training to growth", "Training → growth", "Productivity and LRAS", "Training raises productivity, shifting LRAS right, so potential output and growth rise.", 4],
  ["Minimum wage to jobs", "Minimum wage → unemployment", "Wage above equilibrium, labour demand and supply", "A minimum wage above equilibrium raises supply and lowers demand, creating a surplus of labour.", 5]
], (it) => `Broken: ${it[0]} (${it[1]}). Missing: ${it[2]}. Repaired: ${it[3]}`, "Marks gained by repairing it");
Lib.classify($("#cl1"), { prompt: "Statement, one step or developed chain?", buckets: [{"label": "Statement"}, {"label": "One step"}, {"label": "Developed chain"}], items: [{"text": "Higher taxes reduce spending.", "b": 0}, {"text": "Higher income tax reduces disposable income, so spending falls.", "b": 1}, {"text": "Higher income tax reduces disposable income, so consumption falls, shifting AD left and lowering output and employment.", "b": 2}, {"text": "Subsidies increase output.", "b": 0}, {"text": "A subsidy lowers costs, so supply shifts right.", "b": 1}, {"text": "A subsidy lowers costs and shifts supply right, so price falls and output rises, which could help the poorest households if the good is a necessity.", "b": 2}], done: "A statement claims, a step gives a reason, a chain reaches the objective." });
Lib.classify($("#cl2"), { prompt: "Which part of the chain is it?", buckets: [{"label": "Trigger"}, {"label": "Mechanism"}, {"label": "Effect"}, {"label": "Consequence"}], items: [{"text": "The central bank raises the interest rate.", "b": 0}, {"text": "Borrowing becomes more expensive.", "b": 1}, {"text": "AD shifts left.", "b": 2}, {"text": "Inflation falls towards the target.", "b": 3}, {"text": "The government introduces a tax on sugary drinks.", "b": 0}, {"text": "The price of the drinks rises relative to substitutes.", "b": 1}], done: "Trigger, mechanism, effect, consequence." });
Lib.order($("#o1"), { prompt: "Put the chain in order.", items: ["Government cuts income tax", "Disposable income rises", "Consumption rises", "AD shifts right", "Real GDP and the price level rise"], done: "Each step leads to the next." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Select", "Pick the figures that bear on the question"], ["Calculate", "Show a percentage change or ratio with its unit"], ["Interpret", "Say what the figure means"], ["Suggest a cause", "Offer a reason the pattern may exist"], ["State a limit", "Say what the data cannot show"], ["Link", "Because, so, which means"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "MPC is 0.75 and investment rises by $6bn. Calculate the largest rise in national income (ignore other leakages).", "a": 24, "unit": "$bn", "tol": 0.1, "hint": "k = 1 ÷ 0.25 = 4.", "sol": "<b>$24bn</b>."},
  {"q": "Unemployment falls from 8.0% to 6.4%. By how many percentage points?", "a": 1.6, "unit": "points", "tol": 0.01, "hint": "8.0 − 6.4.", "sol": "<b>1.6 percentage points</b>."},
  {"q": "Real GDP rises from $500bn to $515bn. Calculate the percentage growth.", "a": 3, "unit": "%", "tol": 0.05, "hint": "15 ÷ 500.", "sol": "<b>3%</b>."},
  {"q": "Exports are $60bn and GDP is $240bn. What share of GDP is exports?", "a": 25, "unit": "%", "tol": 0.1, "hint": "60 ÷ 240.", "sol": "<b>25%</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which is a developed chain?", opts: ["A subsidy lowers costs, shifting supply right, so price falls and output rises.", "A subsidy is good.", "Subsidies cost the government.", "Output may change."], a: 0, why: "It has steps with because/so logic." },
  { q: "The best way to end an analysis paragraph is to:", opts: ["name the objective in the question", "start a new topic", "define a term", "write 'in conclusion'"], a: 0, why: "The chain is complete when it reaches the objective." },
  { q: "A required diagram is missing from a 20-mark essay. What is the effect?", opts: ["The 14-mark scale is capped at Level 2", "No effect", "Evaluation is lost", "The essay is marked out of 10"], a: 0, why: "The cap applies to the 14-mark scale." },
  { q: "A correlation across five countries shows:", opts: ["A pattern that suggests a link but does not prove cause", "Proof of cause", "That the data are wrong", "No relationship"], a: 0, why: "Say what it suggests and what it cannot show." },
  { q: "How many developed chains are usually needed to move from Level 2 into Level 3?", opts: ["Three, applied to the context", "One", "Six", "None"], a: 0, why: "A third developed, applied chain is the usual step." },
] });
Lib.cards($("#fc1"), { cards: [
  ["AO2", "Analysis: causes, effects, consequences."],
  ["Weighting", "40% overall, 37% of Paper 4, 40% of Paper 3."],
  ["Chain", "Trigger, mechanism, effect, consequence."],
  ["Link words", "Because, so, which means, leading to."],
  ["Level 3", "Developed, detailed, accurate, diagram explained."],
  ["Three chains", "Target for a 20-mark essay."],
  ["Diagram", "Required diagram missing: capped at Level 2."],
  ["Data", "Select, calculate, interpret, limit."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "An increase in government spending on infrastructure raises AD. In the short run the economy has a large negative output gap. What is the most likely result?", opts: ["real GDP rises with little change in the price level", "the price level rises with no change in real GDP", "real GDP falls", "the price level falls"], a: 0, why: "With spare capacity, extra AD mainly raises output." },
  { q: "The marginal propensity to consume is 0.8 and government spending rises by $4bn. By how much could national income rise, ignoring other leakages?", opts: ["$20bn", "$5bn", "$3.2bn", "$4bn"], a: 0, why: "Multiplier 5 × $4bn = $20bn." },
  { q: "A subsidy is given to producers of a good with a positive externality in consumption. Which result is most likely?", opts: ["output rises towards the social optimum", "output falls", "price rises", "the externality disappears entirely"], a: 0, why: "The subsidy lowers cost, raising output towards where MSB = MSC." },
  { q: "A country's currency depreciates. Why might the current account fail to improve in the short run?", opts: ["demand for exports and imports may be inelastic", "exports become more expensive", "imports become cheaper", "the multiplier falls"], a: 0, why: "If the sum of elasticities is below one, the Marshall–Lerner condition is not met." },
  { q: "Which would most strengthen the link between higher interest rates and lower inflation?", opts: ["a large share of household borrowing at variable rates", "firms with large cash reserves", "most spending financed by savings", "an open economy with a fixed exchange rate"], a: 0, why: "Variable-rate debt passes the change quickly to spending." },
] });
