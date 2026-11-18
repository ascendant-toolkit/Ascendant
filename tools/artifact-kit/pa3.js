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

strip("#pic1", "Evaluation marks from one to six", [["1 to 2", "simple comments | vague conclusion"], ["3", "list with some | reasons"], ["4", "one developed | point + conclusion"], ["5", "two developed | + justified verdict"], ["6", "woven through | + conditional verdict"]]);
chainStep("#stA", "Building evaluation from 1 mark to 6 marks", ["2 marks: 'A carbon tax could work but has problems. Overall it is mixed.'", "3 marks: add some reasons: 'demand may be inelastic and bills may rise'", "4 marks: develop one point: if demand is inelastic, emissions barely fall", "5 marks: add a second developed point with the context: poorer households", "6 marks: weave in time and alternatives, and end with a conditional verdict"],
  ["<b>E1:</b> simple comments and a vague conclusion.", "<b>Top of E1:</b> reasons given, nothing developed.", "<b>Bottom of E2:</b> condition, reason, consequence.", "<b>E2:</b> two developed points and a justified conclusion.", "<b>Top of E2:</b> a verdict that says what it depends on."]);
chainStep("#stB", "Condition, If, Then on one point", ["Condition: it depends on elasticity of demand for electricity", "If demand is inelastic: a higher price cuts quantity only slightly", "So emissions fall little and bills rise", "If substitutes exist in the long run: demand is more elastic", "Then the tax is more effective over time, so it depends on timing"],
  ["<b>Condition</b> names the lever.", "<b>If</b> describes one case.", "<b>Then</b> gives the consequence.", "<b>The opposite case</b> shows both sides were considered.", "<b>So what</b> feeds the verdict."]);
chainStep("#stC", "From a vague conclusion to a justified one", ["Vague: 'Overall a carbon tax has pros and cons.'", "Say which: 'It is not the most effective policy on its own.'", "Use the question's words: '...to reduce pollution from coal-fired power stations.'", "Give the reason: 'because demand for electricity is inelastic.'", "Say what it depends on: 'unless substitutes are built.'"],
  ["<b>E1:</b> no judgement.", "<b>A judgement</b> that answers 'most effective'.", "<b>Addresses the specific requirements</b> of the question.", "<b>Justified</b> by the analysis.", "<b>Conditional:</b> says what would change it."]);

function ev() {
  const ids = ["pt", "sp", "cn", "cx"];
  if (!ids.every((i) => $("#" + i))) return;
  const [pts, sup, con, cx] = ids.map((i) => +$("#" + i).value);
  let m = Math.min(pts, 3) * (sup === 0 ? 0.6 : sup === 1 ? 1.1 : 1.5) + con * 1.0 + cx * 0.5;
  m = Math.round(Math.min(6, m));
  if (con < 2) m = Math.min(m, 4);
  if (sup === 0) m = Math.min(m, 3);
  if (pts === 0 && con === 0) m = 0;
  const L = m >= 4 ? 2 : m >= 1 ? 1 : 0;
  $("#r1").textContent = m + " / 6"; $("#r2").textContent = L ? "E" + L : "No credit";
  $("#r3").textContent = m >= 6 ? "At the top" : con < 2 ? "Make the conclusion answer the question and say why" : sup < 2 ? "Develop each point with a reason and a consequence" : pts < 3 ? "Add another developed point" : cx < 1 ? "Tie a point to the context" : "Say what the verdict depends on";
  $("#rv").textContent = `${pts} evaluative point(s), support ${["none", "some", "strong"][sup]}, conclusion ${["absent", "vague", "justified and answers the question"][con]}, ${cx ? "context used" : "generic"}: about ${m} out of 6 (${L ? "E" + L : "no credit"}).`;
  const W = 340, X = (v) => 40 + (v / 6) * W;
  let o = SV.rect(X(0), 70, X(3) - X(0), 40, "f3", op(0.4)) + SV.rect(X(3), 70, X(6) - X(3), 40, "f2", op(0.4)) + SV.text(X(1.5), 95, "E1", "lbl bd", { "text-anchor": "middle" }) + SV.text(X(4.5), 95, "E2", "lbl bd", { "text-anchor": "middle" });
  o += SV.line(X(m), 50, X(m), 130, "c4", { "stroke-width": 3 }) + SV.text(X(m), 44, m + "", "lbl bd", { "text-anchor": "middle" });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "pt", label: "Evaluative points made (0 to 3) ", min: 0, max: 3, step: 1, value: 1, fmt: (v) => v, onInput: ev });
Lib.slider($("#g2"), { id: "sp", label: "Support: 0 none, 1 some, 2 reasoned with evidence ", min: 0, max: 2, step: 1, value: 1, fmt: (v) => ["none", "some", "strong"][v], onInput: ev });
Lib.slider($("#g3"), { id: "cn", label: "Conclusion: 0 none, 1 vague, 2 justified ", min: 0, max: 2, step: 1, value: 1, fmt: (v) => ["none", "vague", "justified"][v], onInput: ev });
Lib.slider($("#g4"), { id: "cx", label: "Tied to the context? (0 no, 1 yes) ", min: 0, max: 1, step: 1, value: 0, fmt: (v) => (v ? "yes" : "no"), onInput: ev });
ev();

chooser("h", [
  ["Time", "There could be time lags.", "If interest rate cuts take 18 months to work, the economy may already be recovering, so the cut could add to inflation.", "Is monetary policy the best way to end a recession?", 5],
  ["Elasticity", "It depends on elasticity.", "If demand for cigarettes is inelastic, a 20% tax raises revenue but barely cuts consumption.", "Is a tax the best way to reduce smoking?", 5],
  ["Spare capacity", "It depends on the economy.", "With a large negative output gap, extra AD mainly raises output; near full capacity it raises prices.", "Will expansionary fiscal policy reduce unemployment?", 4],
  ["Context", "It differs by country.", "In a country with a large informal sector, higher income tax may be hard to collect, so revenue could fall short.", "Should a developing economy raise income tax?", 4],
  ["Trade-off", "There are good and bad points.", "Higher interest rates reduce inflation but may raise unemployment, falling mainly on lower-income households.", "Should a central bank raise rates to meet an inflation target?", 5],
  ["Alternatives", "Other policies exist.", "Regulation guarantees the cut but without revenue, whereas a tax raises revenue but leaves the quantity uncertain.", "Is a tax the best way to cut pollution?", 4]
], (it) => `${it[0]}. Named: "${it[1]}" Developed: "${it[2]}" Fits: ${it[3]}`, "How often this lever is useful");
chooser("k", [
  ["'Overall there are advantages and disadvantages.'", "It repeats both sides and makes no judgement", "'Overall the policy is likely to work for goods with close substitutes but not for addictive goods, so it is not the best option on its own.'", "A judgement, a condition and the question's wording", 2],
  ["'It depends.'", "No factor, mechanism or answer", "'It depends on whether demand is inelastic: if it is, the tax barely cuts consumption, so it is not the most effective policy.'", "A named condition and a result", 1],
  ["'So the government should do this.'", "A claim with no reason or weighing", "'The government should combine it with investment in alternatives, because price alone does not create substitutes.'", "A reason linked to the analysis", 2],
  ["'In conclusion, as I said, a tax raises the price.'", "It repeats the analysis", "'In conclusion, a tax is unlikely to be the best policy, because demand is inelastic and regulation guarantees a result.'", "A judgement that weighs", 2],
  ["'Overall it is a good policy.'", "A vague judgement with no support", "'Overall it is a good policy for cheap, strong drinks with substitutes, because the quantity demanded falls most there.'", "The condition and the group", 2]
], (it) => `Weak: ${it[0]} Why it scores low: ${it[1].toLowerCase()}. Better: ${it[2]}`, "Marks lost by the weak version (out of 6)");
Lib.classify($("#cl1"), { prompt: "Not evaluation, named, or developed?", buckets: [{"label": "Not evaluation"}, {"label": "Named (E1)"}, {"label": "Developed (E2)"}], items: [{"text": "A tax raises the price of a good.", "b": 0}, {"text": "There could be time lags.", "b": 1}, {"text": "If demand is inelastic, a 20% rise in price cuts quantity by only 5%, so consumption barely falls and the policy fails its aim.", "b": 2}, {"text": "It depends on a number of factors.", "b": 1}, {"text": "A subsidy shifts supply to the right.", "b": 0}, {"text": "If PES is low, a subsidy may mainly raise the price, so output rises little and the policy is less effective.", "b": 2}], done: "Analysis and facts are not evaluation. Named factors without a reason stay in E1. Developed evaluation gives a condition, a reason and a consequence." });
Lib.classify($("#cl2"), { prompt: "Which lever is it?", buckets: [{"label": "Time"}, {"label": "Elasticity"}, {"label": "Spare capacity"}, {"label": "Trade-off"}], items: [{"text": "Training raises productivity only after several years.", "b": 0}, {"text": "A tax cuts consumption only if demand is elastic.", "b": 1}, {"text": "Extra AD mainly raises prices near full capacity.", "b": 2}, {"text": "Higher interest rates reduce inflation but may raise unemployment.", "b": 3}, {"text": "Interest rate changes may take 18 months to work.", "b": 0}, {"text": "If PES is low, a subsidy raises price more than output.", "b": 1}], done: "Time, elasticity, spare capacity and trade-off are four common levers." });
Lib.order($("#o1"), { prompt: "Put the evaluation in order.", items: ["It depends on the price elasticity of demand for electricity", "If demand is inelastic, a higher price cuts quantity only slightly", "So emissions barely fall and bills rise", "Over a decade, substitutes could make demand more elastic", "Therefore the tax is unlikely to be the most effective policy on its own in the short run"], done: "Condition, if, then, the opposite case, and the verdict." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["E1 (1 to 3)", "Vague conclusion and simple comments"], ["E2 (4 to 6)", "Justified conclusion and developed comments"], ["Lever", "A factor on which the outcome depends"], ["Scope word", "Always, only, alone, best, to what extent"], ["Justified conclusion", "A judgement with the reason and the condition"], ["Assumption", "Something a model takes as given"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "A 20-mark essay gives 6 marks for evaluation. What percentage is that?", "a": 30, "unit": "%", "tol": 0.1, "hint": "6 ÷ 20.", "sol": "<b>30%</b>, matching the Paper 4 weighting."},
  {"q": "Paper 4 has 60 marks. At 30% AO3, how many marks in total are for evaluation?", "a": 18, "unit": "marks", "tol": 0.1, "hint": "0.3 × 60.", "sol": "<b>18 marks</b>."},
  {"q": "A 40-minute essay should give a third of its time to evaluation. How many minutes is that (1 decimal place)?", "a": 13.3, "unit": "min", "tol": 0.1, "hint": "40 ÷ 3.", "sol": "<b>13.3 minutes</b>, including the conclusion."},
  {"q": "Paper 3 is 13% AO3. Of 30 marks, about how many are AO3 (1 decimal place)?", "a": 3.9, "unit": "marks", "tol": 0.1, "hint": "0.13 × 30.", "sol": "<b>3.9 marks</b>, about 4."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A response says 'it depends on many factors' and nothing else. Which level fits best?", opts: ["E1", "E2", "No credit only", "Level 3"], a: 0, why: "Vague with no development is E1." },
  { q: "What does E2 need?", opts: ["A justified conclusion and developed, supported comments", "A long introduction", "A repeat of the analysis", "A list of definitions"], a: 0, why: "Those are the two Table B descriptors." },
  { q: "A question asks whether a policy is 'always' effective. The best conclusion:", opts: ["identifies a case where it is not", "says it is always effective", "lists pros and cons", "repeats the analysis"], a: 0, why: "The scope word demands a counter-case." },
  { q: "Which is a developed evaluative comment?", opts: ["Demand may be inelastic.", "If demand is inelastic, the tax cuts consumption little, so the policy fails its aim.", "There are other policies.", "Elasticity is important."], a: 1, why: "Condition, if and then." },
  { q: "How much of Paper 4 is AO3?", opts: ["30%", "13%", "47%", "25% of each paper"], a: 0, why: "Paper 4 is 30% AO3; Paper 3 is 13%." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Table B", "E1: vague. E2: justified and developed."],
  ["6 marks", "Two or three developed points and a conditional verdict."],
  ["Levers", "Time, elasticity, magnitude, capacity, context, trade-off, alternatives."],
  ["Condition, If, Then", "Name it, explain it, say so what."],
  ["Scope word", "Always, only, alone, best, to what extent."],
  ["Conclusion", "Verdict, strongest reason, what it depends on."],
  ["Weighting", "30% of Paper 4, 13% of Paper 3."],
  ["Avoid", "A list of named factors."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "What would make a rise in the interest rate less likely to reduce inflation?", opts: ["Consumers expect prices to rise faster in future", "Consumers hold large savings in cash", "Aggregate supply is falling", "Wages are growing slowly"], a: 0, why: "Expectations of higher prices may keep spending high despite the higher rate." },
  { q: "A government uses supply-side policy to raise LRAS. What is the most likely reason the price level might not fall?", opts: ["AD may also rise", "LRAS cannot shift", "Costs always rise", "Output is fixed"], a: 0, why: "If AD rises too, the price level may not fall." },
  { q: "A currency depreciates but the current account deficit stays the same. Which is the most likely reason?", opts: ["Demand for exports and imports is inelastic in the short run", "Exports become more expensive", "Imports become cheaper", "The multiplier falls"], a: 0, why: "The Marshall–Lerner condition may not hold." },
  { q: "Which statement is an evaluative comment?", opts: ["The tax may be ineffective if demand is inelastic, because quantity barely falls.", "A tax raises the price.", "The tax is paid by firms.", "Demand curves slope downwards."], a: 0, why: "It gives a condition, a reason and a consequence." },
  { q: "A response to 'Assess whether X is always true' gives two paragraphs of support and concludes 'X is true'. What is its main weakness?", opts: ["It never tests 'always' with a counter-case", "It is too short", "It has no definition", "It has a diagram"], a: 0, why: "The scope word demands a case where the claim fails." },
] });
