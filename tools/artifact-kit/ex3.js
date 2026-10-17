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

$("#pic1").innerHTML = (() => {
  const L = [["1 mark", "One simple comment", 15, "f3"], ["2 marks", "Comments + vague conclusion", 205, "f3"], ["3 marks", "One developed point + conclusion", 395, "f1"], ["4 marks", "Two developed points + justified conclusion", 585, "f2"]];
  let o = ""; L.forEach(([n, d, x, c]) => { o += SV.rect(x, 12, 165, 80, c, { rx: 12, ...op(0.45) }) + SV.text(x + 82, 40, n, "lbl bd", { "text-anchor": "middle", style: "font-size:16px" }); const w = d.split(" + "); w.forEach((p, i) => { o += SV.text(x + 82, 62 + i * 18, (i ? "+ " : "") + p, "sm", { "text-anchor": "middle" }); }); });
  return `<svg viewBox="0 0 760 104" role="img" aria-label="Evaluation marks from one to four">${o}</svg>`;
})();
chainStep("#stA", "Building evaluation from 1 mark to 4 marks", ["1 mark: 'A minimum price may not work if demand is inelastic.'", "2 marks: add a second simple comment and a general conclusion ('overall quite good')", "3 marks: develop one point: if demand is inelastic, a 20% price rise cuts quantity by only 5%, so consumption barely falls", "4 marks: add a second condition (information failure remains) and a justified conclusion in the question's words"], [
  "<b>One bare comment.</b>", "<b>Still Level 1:</b> nothing is supported and the conclusion is vague.", "<b>Level 2:</b> a condition, a reason and a consequence.", "<b>Top of Level 2:</b> two developed points and a conclusion that says which policy is best and why."]);
chainStep("#stB", "The CIT method on one point", ["Condition: it depends on the price elasticity of demand among heavy drinkers", "If demand is inelastic: a 20% price rise cuts quantity by only 5%, so consumption barely falls", "If demand is elastic: consumption falls by more than the price rise", "Then: a minimum price is only effective where demand is elastic", "Weigh it: heavy drinkers are the target group and tend to be inelastic, so the policy is limited"], [
  "<b>Condition</b> names the lever (elasticity) and the group.", "<b>If</b> shows the mechanism for one case.", "<b>The opposite case</b> shows you have considered both.", "<b>Then</b> connects the result to the claim in the question.", "<b>Weigh</b> which condition is more likely, with the reason."]);
chainStep("#stC", "From a vague conclusion to a justified one", ["Vague: 'Overall a minimum price is quite good but has problems.'", "Say which: 'A minimum price is not the best policy on its own.'", "Use the question's words: '...to reduce consumption of a demerit good.'", "Add the reason: 'because demand is likely to be inelastic and information failure remains.'", "Add the condition: 'It would work better for cheap drinks where substitutes exist, or with information.'"], [
  "<b>Level 1:</b> no judgement.", "<b>A judgement</b> that answers 'best'.", "<b>Addresses the specific requirements</b> of the question.", "<b>Justified:</b> a reason that links to the analysis.", "<b>Developed:</b> the condition under which the answer would change."]);

function ev() {
  const ids = ["pt", "sp", "cn", "sd"];
  if (!ids.every((i) => $("#" + i))) return;
  const [pts, sup, con, both] = ids.map((i) => +$("#" + i).value);
  let m, why = "";
  if (!both) { m = 0; why = " The analysis is one-sided, so no evaluation marks are available."; }
  else {
    const dev = Math.min(pts, 2) * (sup >= 1 ? 1 : 0.5) * (sup >= 2 ? 1.2 : 1), cc = con === 2 ? 1.5 : con === 1 ? 0.7 : 0;
    m = Math.round(Math.min(4, dev * 1.1 + cc));
    if (con < 2) m = Math.min(m, 3);
    if (pts === 0 && con === 0) m = 0;
    if (sup === 0) m = Math.min(m, 2);
  }
  const L = m >= 3 ? 2 : m >= 1 ? 1 : 0;
  $("#r1").textContent = m + " / 4"; $("#r2").textContent = L ? "Level " + L : "No credit";
  $("#r3").textContent = !both ? "Analyse the other side first" : m >= 4 ? "At the top" : con < 2 ? "Make the conclusion answer the question and give the reason" : sup < 2 ? "Support each point with a reason or figure" : pts < 2 ? "Add a second developed condition" : "Check the conclusion uses the question's words";
  $("#rv").textContent = `${pts} evaluative point(s), support ${["none", "some", "strong"][sup]}, conclusion ${["absent", "vague", "justified and answers the question"][con]}, ${both ? "analysis two-sided" : "analysis one-sided"}: about ${m} out of 4 (${L ? "Level " + L : "no credit"}).` + why;
  const W = 340, X = (v) => 40 + (v / 4) * W;
  let o = SV.rect(X(0), 70, X(2) - X(0), 40, "f3", op(0.4)) + SV.rect(X(2), 70, X(4) - X(2), 40, "f2", op(0.4)) + SV.text(X(1), 95, "Level 1", "lbl bd", { "text-anchor": "middle" }) + SV.text(X(3), 95, "Level 2", "lbl bd", { "text-anchor": "middle" });
  o += SV.line(X(m), 50, X(m), 130, "c4", { "stroke-width": 3 }) + SV.text(X(m), 44, m + "", "lbl bd", { "text-anchor": "middle" });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "pt", label: "Evaluative points made (0 to 3) ", min: 0, max: 3, step: 1, value: 1, fmt: (v) => v, onInput: ev });
Lib.slider($("#g2"), { id: "sp", label: "Support: 0 none, 1 some, 2 reasoned with evidence ", min: 0, max: 2, step: 1, value: 1, fmt: (v) => ["none", "some", "strong"][v], onInput: ev });
Lib.slider($("#g3"), { id: "cn", label: "Conclusion: 0 none, 1 vague, 2 justified ", min: 0, max: 2, step: 1, value: 1, fmt: (v) => ["none", "vague", "justified"][v], onInput: ev });
Lib.slider($("#g4"), { id: "sd", label: "Both sides analysed? (0 no, 1 yes) ", min: 0, max: 1, step: 1, value: 1, fmt: (v) => (v ? "yes" : "no"), onInput: ev });
ev();

chooser("h", [
  ["Elasticity", "It depends on how people respond to price.", "It depends on the price elasticity of demand for cigarettes among long-term smokers: if it is inelastic, a 20% tax raises revenue but barely cuts consumption.", "Is an indirect tax the best way to reduce consumption of a demerit good?", 5],
  ["Time", "In the long run it might be different.", "In the short run, spending on roads raises AD and may raise prices; in the long run, better roads raise capacity and lower prices.", "Will supply-side policy raise inflation?", 5],
  ["Spare capacity", "It depends on the state of the economy.", "If the economy has spare capacity, extra AD raises output; near full capacity it mainly raises the price level, so the policy is less beneficial.", "Does expansionary fiscal policy always benefit an economy?", 5],
  ["Context or type", "It is different in different countries.", "For a developing economy with infant industries, free trade may cause unemployment; for one with strong factor endowments, it is more likely to bring gains.", "Is free trade always better than protectionism?", 4],
  ["Trade-off", "There are good and bad points.", "Higher interest rates reduce demand-pull inflation, but they also raise firms' costs and unemployment, so the benefit depends on how much slack there is.", "Is contractionary monetary policy the best way to reduce inflation?", 4],
  ["Alternatives", "Other policies exist.", "Information tackles the cause of over-consumption, but is slow; a tax is quicker and raises revenue, so a combination is likely to work best.", "Is information the best way to reduce demerit goods?", 4]
], (it) => `${it[0]}. Vague: "${it[1]}" Developed: "${it[2]}" Fits: ${it[3]}`, "How often this lever is useful");
chooser("k", [
  ["'Overall it has advantages and disadvantages.'", "It restates both sides but makes no judgement", "'Overall the policy is likely to work for goods with elastic demand, but not for addictive goods, so it is not the best policy on its own.'", "A judgement, a condition and a reason", 1],
  ["'It depends.'", "No factor, mechanism or answer", "'It depends on whether demand is inelastic: if it is, the tax barely reduces consumption, so it is not the best policy.'", "A named condition and a result", 1],
  ["'So the government should use this policy.'", "A claim with no reason and no weighing", "'The government should combine it with information, because price alone leaves the lack of knowledge in place.'", "A reason that links to the analysis", 2],
  ["'In conclusion, as I said above, a minimum price raises the price.'", "Repeats the analysis", "'In conclusion, a minimum price is unlikely to be the best policy, because demand is likely to be inelastic and an alternative gives more revenue.'", "A judgement using the question's words", 2],
  ["'Overall it is a good policy.'", "A vague judgement with no support", "'Overall it is a good policy for cheap, strong drinks with substitutes, because quantity demanded falls most there.'", "The condition and the group", 2]
], (it) => `Weak: ${it[0]} Why it scores low: ${it[1].toLowerCase()}. Better: ${it[2]} It adds: ${it[3].toLowerCase()}.`, "Marks lost by the weak version (out of 4)");
Lib.classify($("#cl1"), { prompt: "Not evaluation, vague evaluation or developed evaluation?", buckets: [{"label": "Not evaluation"}, {"label": "Vague (Level 1)"}, {"label": "Developed (Level 2)"}], items: [{"text": "A minimum price is set above the equilibrium price.", "b": 0}, {"text": "It depends on many things.", "b": 1}, {"text": "If demand is price inelastic, a 20% rise in price cuts quantity by only 5%, so consumption barely falls and the policy is not effective.", "b": 2}, {"text": "A tax shifts the supply curve left.", "b": 0}, {"text": "Overall there are good and bad points.", "b": 1}, {"text": "A tariff only helps if demand for imports is elastic; if trading partners retaliate, exporters lose, so the benefit depends on retaliation.", "b": 2}], done: "Analysis and facts are not evaluation. Vague comments name no factor. Developed evaluation gives the condition, the reason and the consequence." });
Lib.classify($("#cl2"), { prompt: "Which evaluation lever is it?", buckets: [{"label": "Time"}, {"label": "Elasticity"}, {"label": "Spare capacity"}, {"label": "Trade-off"}], items: [{"text": "Training raises productivity only after several years.", "b": 0}, {"text": "A tax only cuts consumption if demand is elastic.", "b": 1}, {"text": "Extra AD mainly raises prices if the economy is near full capacity.", "b": 2}, {"text": "Higher interest rates cut inflation but may raise unemployment.", "b": 3}, {"text": "The short-run effect is bigger than the long-run effect.", "b": 0}, {"text": "Imports fall only if the sum of the price elasticities is above one.", "b": 1}], done: "Time, elasticity, spare capacity and trade-off are four common levers." });
Lib.order($("#o1"), { prompt: "Put the sentence parts in order: Condition, If, Then.", items: ["It depends on the price elasticity of demand for cigarettes among long-term smokers", "If it is inelastic, a 20% tax raises revenue but barely reduces consumption", "Then the tax is not effective at reducing consumption of this demerit good", "So overall the tax is better at raising revenue than at cutting smoking"], done: "Condition, If, Then, and a weighing sentence." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["1 mark", "A simple evaluative comment"], ["2 marks", "Simple comments with a vague conclusion"], ["3 marks", "One developed point with a conclusion that addresses the question"], ["4 marks", "Two developed points with a justified conclusion"], ["No evaluation marks", "The analysis was one-sided"], ["Justified conclusion", "A judgement with the reason and the condition"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "A 12 mark question gives 4 marks for evaluation. What percentage of the marks is that?", "a": 33.3, "unit": "%", "tol": 0.3, "hint": "4 ÷ 12.", "sol": "<b>33.3%</b>."},
  {"q": "An 8 mark part gives 2 marks for evaluation. What percentage is that?", "a": 25, "unit": "%", "tol": 0.1, "hint": "2 ÷ 8.", "sol": "<b>25%</b>."},
  {"q": "A 6 mark data response part has 2 marks for evaluation. What percentage is that (1 decimal place)?", "a": 33.3, "unit": "%", "tol": 0.3, "hint": "2 ÷ 6.", "sol": "<b>33.3%</b>."},
  {"q": "At 2 minutes a mark, how long should the evaluation of a 12 mark answer take (4 marks)?", "a": 8, "unit": "min", "tol": 0.1, "hint": "4 × 2.", "sol": "<b>8 minutes</b>, including planning."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A response says 'it depends on many factors' and nothing else. Which Table B level is the best fit?", opts: ["Level 1", "Level 2", "Level 0 only", "Level 3"], a: 0, why: "A vague comment with no development is Level 1." },
  { q: "Which feature is required for Level 2 evaluation?", opts: ["A justified conclusion addressing the question and developed, supported comments", "A long introduction", "A repeat of the analysis", "A list of definitions"], a: 0, why: "These are the two Table B descriptors." },
  { q: "A mark scheme says a one-sided response cannot gain evaluation marks. What should the student do?", opts: ["Analyse both sides before evaluating", "Write a longer conclusion", "Only evaluate", "Skip the analysis"], a: 0, why: "Evaluation requires a balanced analysis." },
  { q: "Which conclusion is best for 'assess whether X is the best policy'?", opts: ["It says which policy is best, uses the question's words and gives a reason", "It lists pros and cons", "It repeats the analysis", "It introduces a new point"], a: 0, why: "That is a justified conclusion that addresses the question." },
  { q: "Which is a developed evaluative comment?", opts: ["Demand may be inelastic.", "If demand is inelastic, the tax cuts consumption little, so the policy fails its aim.", "There are other policies.", "Elasticity is important."], a: 1, why: "Condition, if and then." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Table B", "Level 1: vague. Level 2: justified and developed."],
  ["4 marks", "Two developed points + justified conclusion."],
  ["Levers", "Magnitude, time, elasticity, capacity, context, trade-off."],
  ["CIT", "Condition, If, Then."],
  ["One-sided", "No evaluation marks."],
  ["Conclusion", "Use the question's words and give the reason."],
  ["8 mark part", "2 evaluation marks."],
  ["Avoid", "'It depends' alone."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "What would make a policy of raising interest rates less likely to be effective in reducing inflation? (Oct/Nov 2021 · 12 · Q29, reworded)", opts: ["Aggregate supply is increasing faster than aggregate demand", "Consumers expect prices to rise even faster in the future", "Consumers' spending is largely paid for on credit", "Interest rates are still higher abroad"], a: 1, why: "A condition that limits the policy: if consumers expect faster price rises, they bring forward spending." },
  { q: "A government decides to use supply-side policy to increase long-run aggregate supply (LRAS). What is the most likely reason why this policy tool will not lead to a fall in the price level? (Feb/March 2025 · 12 · Q24, reworded)", opts: ["Aggregate demand will also increase.", "Labour productivity levels will increase.", "Workers will save any extra wages they earn.", "Workers will spend any extra wages on imports."], a: 0, why: "An evaluation point: supply-side spending also raises AD, offsetting the fall in prices." },
  { q: "A government has a target to reduce the rate of inflation. Why might it not want to raise interest rates to achieve this target? (May/June 2025 · 13 · Q25, reworded)", opts: ["aggregate demand may fall", "aggregate supply may fall", "saving may fall", "the exchange rate may fall"], a: 1, why: "A cost of the policy: higher borrowing costs for firms can reduce capacity." },
  { q: "A government decides to allow the country's currency to depreciate to remove the deficit on its current account. What is the most likely reason why this would not work? (Feb/March 2024 · 12 · Q25, reworded)", opts: ["The country gains a competitive advantage from the depreciation.", "The country has a surplus on its capital and financial accounts.", "The price elasticities of demand for the country's exports and imports are greater than one.", "There are high trade barriers with the country's main trading partners."], a: 3, why: "A limiting condition: trade barriers reduce the rise in exports." },
  { q: "A country has a balance of trade deficit. When will this be least likely to be improved as a result of a depreciation of its currency? (May/June 2021 · 13 · Q25, reworded)", opts: ["if it is currently operating with a significant amount of unused resources", "if the sum of the price elasticities of demand for exports and imports is less than 1", "if in the long term, the price elasticity of demand for exports should increase", "if the country uses a relatively small proportion of imports in their production process"], a: 1, why: "The elasticity condition: if the sum is below one the trade balance may worsen." },
] });
