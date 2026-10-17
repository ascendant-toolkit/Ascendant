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
  const B = [["Section A", "Q1 data response", "20 marks", 20, "f1"], ["Section B", "One micro essay: (a) 8 + (b) 12", "20 marks", 270, "f2"], ["Section C", "One macro essay: (a) 8 + (b) 12", "20 marks", 520, "f3"]];
  let o = ""; B.forEach(([n, d, m, x, c]) => { o += SV.rect(x, 12, 220, 90, c, { rx: 12, ...op(0.45) }) + SV.text(x + 110, 40, n, "lbl bd", { "text-anchor": "middle", style: "font-size:17px" }) + SV.text(x + 110, 62, d, "sm", { "text-anchor": "middle" }) + SV.text(x + 110, 84, m, "sm", { "text-anchor": "middle" }); });
  return `<svg viewBox="0 0 760 114" role="img" aria-label="Paper 2 has three sections each worth 20 marks">${o}</svg>`;
})();
chainStep("#stA", "Reading a question before writing", ["Find the marks: 12 marks, so developed analysis and evaluation", "Underline the command word: 'Assess whether'", "Circle the scope word: 'always'", "Underline the context: 'expansionary fiscal policy' / 'an economy'", "Plan: one case where it works, one where it does not, two conditions, a conclusion with 'always'"], [
  "<b>Marks</b> decide the length and the paragraphs.", "<b>Command word:</b> both sides, then a judgement.", "<b>Scope word:</b> find a case where it fails.", "<b>Context:</b> stay on the policy and the economy named.", "<b>The plan</b> takes about 2 minutes."]);
chainStep("#stB", "An 8 mark part in three paragraphs", ["Paragraph 1 (AO1): definition and a labelled diagram, in 3 or 4 lines", "Paragraph 2 (AO2): a developed chain that refers to the diagram, in 5 to 7 lines", "Paragraph 3 (AO3): a condition and a short conclusion in the question's words, in 3 lines", "Check: both halves of the question answered ('explain' and 'consider')"], [
  "<b>Up to 3 knowledge marks.</b>", "<b>Up to 3 analysis marks.</b>", "<b>Up to 2 evaluation marks.</b>", "<b>Do not write more than 8 marks deserve.</b>"]);
chainStep("#stC", "A 12 mark answer in four paragraphs", ["Opener (optional, 1 to 2 lines): scope or one definition", "Paragraph 1: the case for, as a developed chain with a diagram (6 to 8 lines)", "Paragraph 2: the case against or an alternative, as a developed chain (6 to 8 lines)", "Paragraph 3: evaluation: two conditions as Condition, If, Then, then weigh them (8 to 10 lines)", "Conclusion: a direct answer in the question's words, with the reason and the condition (2 to 3 lines)"], [
  "<b>Skip it if short of time.</b>", "<b>Analysis (Table A).</b>", "<b>Balance: needed for Level 3.</b>", "<b>Evaluation (Table B).</b>", "<b>Never drop the conclusion.</b>"]);

function pl() {
  const ids = ["rd", "ck", "sa"];
  if (!ids.every((i) => $("#" + i))) return;
  const [rd, ck, sa] = ids.map((i) => +$("#" + i).value), left = 120 - rd - ck - sa, each = left / 2;
  $("#r1").textContent = Lib.fmtN(each, 1) + " min"; $("#r2").textContent = Lib.fmtN(sa / 20, 2) + " min"; $("#r3").textContent = Lib.fmtN(each / 20, 2) + " min";
  $("#rv").textContent = `Reading ${rd} min, checking ${ck} min and Section A ${sa} min leave ${left} minutes: about ${Lib.fmtN(each, 0)} minutes for each 20 mark essay question (about ${Lib.fmtN(each * 0.37, 0)} for part (a) and ${Lib.fmtN(each * 0.63, 0)} for part (b)). ` + (each < 33 ? "This is tight: the essays are worth as much as Section A, so protect their time." : each > 40 ? "Generous: you may be over-investing in the essays; check Section A has enough time." : "A sensible balance.");
  const W = 380, X = (v) => 20 + (v / 120) * W;
  const segs = [["Read", rd, "f3"], ["A", sa, "f1"], ["B", each, "f2"], ["C", each, "f2"], ["Check", ck, "f3"]]; let o = "", acc = 0;
  segs.forEach(([n, v, c]) => { o += SV.rect(X(acc), 70, X(acc + v) - X(acc), 50, c, op(0.5)) + SV.text(X(acc + v / 2), 100, n, "sm", { "text-anchor": "middle" }); acc += v; });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "rd", label: "Reading and planning, minutes ", min: 3, max: 12, step: 1, value: 6, fmt: (v) => v, onInput: pl });
Lib.slider($("#g2"), { id: "ck", label: "Final check, minutes ", min: 3, max: 12, step: 1, value: 7, fmt: (v) => v, onInput: pl });
Lib.slider($("#g3"), { id: "sa", label: "Section A, minutes ", min: 28, max: 50, step: 1, value: 36, fmt: (v) => v, onInput: pl });
pl();

chooser("h", [
  ["1(a): 2 marks, compare data", "Reading data: an explicit comparison", "One or two sentences with figures, linking both series", "About 3 to 4 minutes; 25 to 40 words", 3],
  ["1(b): 2 marks, explain one reason", "AO1 and AO2: 1 + 1", "The point, then a development", "About 4 minutes; 2 sentences", 3],
  ["1(c): 4 marks, consider", "3 analysis + 1 evaluation", "Two developed points using the data, and one evaluative sentence", "About 8 minutes; 70 to 100 words", 4],
  ["1(d), 1(e): 6 marks, assess", "4 analysis + 2 evaluation", "Two developed chains, a diagram if asked, a 2 sentence evaluation with a conclusion", "About 9 to 12 minutes; 120 to 170 words", 5],
  ["Essay (a): 8 marks", "AO1 3, AO2 3, AO3 2", "Definition or diagram, a developed chain, a short judgement", "About 13 to 16 minutes; 150 to 230 words", 5],
  ["Essay (b): 12 marks", "AO1 + AO2 out of 8, AO3 out of 4", "Balanced developed analysis, evaluation with conditions, a conclusion", "About 22 to 24 minutes; 350 to 500 words", 5]
], (it) => `${it[0]}. Marked for: ${it[1].toLowerCase()}. Write: ${it[2].toLowerCase()}. Time and length (a guide): ${it[3].toLowerCase()}.`, "Importance of the part");
chooser("k", [
  ["'Assess whether expansionary fiscal policy always benefits an economy.'", "Assess: both sides then a judgement", "ALWAYS: find a case where it does not (no spare capacity, high debt)", "Show benefits and costs, then say when it fails", 5],
  ["'Explain how the circular flow changes from a closed to an open economy and consider what determines the extent.'", "Explain, then consider", "The 'consider' half asks what determines the extent (size of X and M, openness)", "Explain the new flows (X, M); then name what determines how large the change is", 5],
  ["'Assess whether protectionism is the best way to reduce a current account deficit.'", "Assess: compare policies", "BEST: compare with at least one other policy", "Analyse protection and an alternative, then judge which is best", 5],
  ["'With the help of a diagram, explain how a subsidy affects the market and consider how the cost is affected by elasticity.'", "Explain with a diagram, then consider", "The diagram is an AO1 mark; the 'consider' half is about elasticity and cost", "Draw and label the diagram, explain, then link cost to PED", 4],
  ["'Discuss whether a government should always aim to balance its budget.'", "Discuss: both sides then a judgement", "ALWAYS and SHOULD: find the cases where it should not", "Compare balanced, deficit and surplus; judge over the cycle", 4]
], (it) => `${it[0]} Command word: ${it[1].toLowerCase()}. Scope word or context: ${it[2].toLowerCase()}. A good answer must: ${it[3].toLowerCase()}.`, "How much the scope word matters");
Lib.classify($("#cl1"), { prompt: "Which part is each question?", buckets: [{"label": "Data response (1a/1b)"}, {"label": "Data response (1c to 1e)"}, {"label": "Essay (a)"}, {"label": "Essay (b)"}], items: [{"text": "Compare the changes in two series in a table (2 marks)", "b": 0}, {"text": "Explain one reason why the CPI may be inaccurate (2 marks)", "b": 0}, {"text": "Consider whether disinflation is more harmful than deflation (4 marks)", "b": 1}, {"text": "Assess whether a policy is likely to be helpful using the extract (6 marks)", "b": 1}, {"text": "With the help of a diagram, explain a change and consider the extent (8 marks)", "b": 2}, {"text": "Assess whether a policy always benefits an economy (12 marks)", "b": 3}], done: "Short data parts test reading and short explanations; 4 and 6 mark parts need analysis and a little evaluation; essays are 8 and 12 marks." });
Lib.classify($("#cl2"), { prompt: "Where does the sentence belong in a 12 mark answer?", buckets: [{"label": "Analysis paragraph"}, {"label": "Evaluation paragraph"}, {"label": "Conclusion"}], items: [{"text": "A minimum price raises price above equilibrium, so quantity demanded contracts.", "b": 0}, {"text": "If demand is inelastic, consumption falls only a little, so the policy is less effective.", "b": 1}, {"text": "Therefore a minimum price is unlikely to be the best policy on its own, because demand is likely to be inelastic.", "b": 2}, {"text": "A tax shifts supply left, raising the price and cutting quantity.", "b": 0}, {"text": "This depends on the time period: the effect may be larger in the long run.", "b": 1}, {"text": "Overall, a tariff is only effective if demand for imports is elastic and there is no retaliation.", "b": 2}], done: "Analysis explains how; evaluation introduces conditions; the conclusion answers the question." });
Lib.order($("#o1"), { prompt: "Put the steps in order for planning an essay part (b).", items: ["Read the question and find the marks, command word and scope word", "Choose the two sides or the policy and an alternative", "Plan the two evaluation conditions and the conclusion", "Write the analysis paragraphs with a diagram", "Write the evaluation and the conclusion in the question's words"], done: "Read, plan, analyse, evaluate, conclude." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Question 1(a)", "2 marks: an explicit comparison or calculation from the data"], ["Question 1(c)", "4 marks: 3 analysis and 1 evaluation"], ["Question 1(d)", "6 marks: 4 analysis and 2 evaluation"], ["Essay part (a)", "8 marks: AO1 3, AO2 3, AO3 2"], ["Essay part (b)", "12 marks: AO1 + AO2 out of 8 and AO3 out of 4"], ["Paper 2", "60 marks in 2 hours: three sections of 20 marks"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "Paper 2 is 60 marks in 120 minutes. How many minutes per mark?", "a": 2, "unit": "min", "tol": 0.05, "hint": "120 ÷ 60.", "sol": "<b>2 minutes</b>."},
  {"q": "A 12 mark part gets 22 minutes. How many minutes per mark (1 decimal place)?", "a": 1.8, "unit": "min", "tol": 0.1, "hint": "22 ÷ 12.", "sol": "<b>1.8</b>."},
  {"q": "An essay question is (a) 8 marks and (b) 12 marks. What fraction of its marks is in part (b) (%)?", "a": 60, "unit": "%", "tol": 0.5, "hint": "12 ÷ 20.", "sol": "<b>60%</b>."},
  {"q": "In a 6 mark data response part, 2 marks are for evaluation. What percentage is that (1 decimal place)?", "a": 33.3, "unit": "%", "tol": 0.3, "hint": "2 ÷ 6.", "sol": "<b>33.3%</b>."},
  {"q": "Section A has parts worth 2, 2, 4, 6 and 6 marks. What is the total?", "a": 20, "unit": "marks", "tol": 0.1, "hint": "2 + 2 + 4 + 6 + 6.", "sol": "<b>20</b> marks."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "How many questions must you answer in Paper 2?", opts: ["Two", "Three", "Four", "Five"], a: 1, why: "Question 1, one from Section B and one from Section C." },
  { q: "How is a part (a) of 8 marks marked from 2023?", opts: ["AO1 3, AO2 3, AO3 2", "AO2 8", "AO1 4, AO3 4", "AO3 8"], a: 0, why: "Point marks across the three objectives." },
  { q: "What does a scope word such as 'always' tell you?", opts: ["Look for a case where the claim fails", "Write more", "Ignore it", "Define it"], a: 0, why: "The claim is rarely true in every case." },
  { q: "Which part should usually receive the most time per part?", opts: ["Essay part (b)", "1(a)", "1(b)", "The introduction"], a: 0, why: "12 marks, with analysis and evaluation." },
  { q: "Why quote figures from the extract?", opts: ["The mark scheme expects the analysis to be applied to the data", "It makes the answer longer", "It is compulsory in essays", "Examiners prefer numbers"], a: 0, why: "Application to the data earns analysis credit." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Paper 2", "60 marks, 2 hours, 3 sections of 20."],
  ["Section A", "Data response: 2, 2, 4, 6, 6."],
  ["Essay (a)", "8 marks: AO1 3, AO2 3, AO3 2."],
  ["Essay (b)", "12 marks: Table A out of 8, Table B out of 4."],
  ["2 min a mark", "Less for 1(a) and 1(b)."],
  ["Scope words", "ALL, ALWAYS, ONLY: find the exception."],
  ["Use the data", "Quote figures."],
  ["Conclude", "In the question's words."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "What is not a function of the price mechanism? (May/June 2025 · 11 · Q6, reworded)", opts: ["To act as a signal to firms when allocating resources", "To maximise consumer surplus", "To provide an incentive to firms to produce goods", "To ration scarce resources"], a: 1, why: "Paper 1 and Paper 2 share syllabus content; Paper 2 tests the same ideas through written answers." },
  { q: "Earth observation satellites designed to acquire information are close to the theoretical case of a public good. In 2011, the World Meteorological Organisation estimated that improving satellite observations would cost an extra $1 billion a year. What is a normative statement about Earth observation satellites? (May/June 2024 · 12 · Q3, reworded)", opts: ["The estimated cost of improving satellite observations is $1 billion a year.", "The information received from the satellites is non-rival.", "The satellites are designed to benefit all countries.", "The government should pay for the improvement of satellite observations."], a: 3, why: "'Should' is a value judgement, which is also the language of an evaluation: be ready to justify it." },
] });
