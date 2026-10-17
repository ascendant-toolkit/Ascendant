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

const adLab = { x: "Real output (Y)", y: "Price level", D1: "AD1", D2: "AD2", S1: "SRAS1", S2: "SRAS2", P1: "P1", Q1: "Y1", P2: "P2", Q2: "Y2" };
function adasPlot(st, o = {}) {
  const l = st.l || 0, ln = o.lras !== false;
  let s = sdPlot({ d: st.a || 0, s: st.s || 0, g: st.g === undefined ? 1 : st.g, n: st.n === undefined ? 1 : st.n }, adLab);
  if (ln) s += SV.line(SDX(75 + l), SDY(0), SDX(75 + l), SDY(100), "c4", { "stroke-width": 3, "stroke-dasharray": "7 4" }) + tag(SDX(75 + l) + 6, SDY(98), "LRAS", "c4");
  return s;
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
  const L = [["Level 1", "1 to 2 marks", "Assertion, no mechanism", 30, "f3"], ["Level 2", "3 to 5 marks", "Mechanism, limited detail", 270, "f1"], ["Level 3", "6 to 8 marks", "Developed chains, applied, balanced", 510, "f2"]];
  let o = ""; L.forEach(([n, m, d, x, c]) => { o += SV.rect(x, 12, 220, 90, c, { rx: 12, ...op(0.45) }) + SV.text(x + 110, 40, n, "lbl bd", { "text-anchor": "middle", style: "font-size:17px" }) + SV.text(x + 110, 62, m, "sm", { "text-anchor": "middle" }) + SV.text(x + 110, 84, d, "sm", { "text-anchor": "middle" }); });
  return `<svg viewBox="0 0 760 114" role="img" aria-label="The three levels of Table A">${o}</svg>`;
})();
chainStep("#stA", "The same paragraph, level by level", ["Level 1: 'A minimum price makes alcohol cost more so people drink less.' (assertion)", "Add the mechanism: the floor is above equilibrium, so quantity demanded contracts (Level 2)", "Add a limit with a reason: inelastic demand means consumption falls only a little", "Add the effect on others: excess supply and extra revenue to retailers; informal markets", "Add an alternative and compare: a tax gives the government revenue (Level 3)"], [
  "<b>1 to 2 marks:</b> correct, but there is no reason why.", "<b>3 to 4 marks:</b> the economics is stated and linked.", "<b>5 marks:</b> a second developed point, using elasticity.", "<b>6 marks:</b> both sides of the policy are analysed.", "<b>7 to 8 marks:</b> an alternative is analysed, with a diagram explained in the text."]);
chainStep("#stB", "How the 3 analysis marks build", ["Mark 1: a correct statement of cause and effect: a depreciation makes imports dearer", "Mark 2: a complete chain for demand-pull: exports cheaper, net exports rise, AD shifts right, prices rise", "Mark 3: a second chain for cost-push, using the context: few natural resources, so costs rise and SRAS shifts left", "Cap: only one type of inflation considered means a maximum of 2 analysis marks"], [
  "<b>1 mark:</b> the idea, with no development.", "<b>2 marks:</b> one chain to the end.", "<b>3 marks:</b> both types, applied to the country with few natural resources.", "<b>Read the mark scheme caps:</b> they say what stops marks at the next boundary."]);
const mpLab = { x: "Quantity of alcohol", y: "Price", D1: "D", S1: "S", P1: "P*", Q1: "Q*" };
function mpDraw(f, k) {
  const qd = (90 - f) / 0.8, qs = (f - 10) / 0.8; // D: p=90-0.8q ; S: p=10+0.8q
  let o = sdPlot({ d: 0, s: 0, g: 1, n: 0 }, mpLab);
  if (k >= 1) o += SV.line(70, SDY(f), 720, SDY(f), "c3", { "stroke-width": 2.5, ...op(k) }) + tag(724, SDY(f) - 6, "Minimum price", "c3", k, "end");
  if (k >= 2) o += SV.line(SDX(qd), SDY(f), SDX(qd), 270, "dash", op(1)) + SV.text(SDX(qd), 286, "Qd", "sm", { "text-anchor": "middle" }) + SV.line(SDX(qs), SDY(f), SDX(qs), 270, "dash", op(1)) + SV.text(SDX(qs), 286, "Qs", "sm", { "text-anchor": "middle" });
  if (k >= 3) o += SV.line(SDX(qd), SDY(f) + 14, SDX(qs), SDY(f) + 14, "c4", { "stroke-width": 3 }) + SV.text(SDX((qd + qs) / 2), SDY(f) + 32, "Excess supply", "sm", { "text-anchor": "middle" });
  return o;
}
Lib.stepper($("#stC"), { w: 760, h: 300, label: "A minimum price diagram", base: { f: 65, k: 0 }, draw: (s) => mpDraw(s.f, s.k), tween: 800, dwell: 5600, steps: [
  { cap: "<b>1 knowledge mark:</b> axes, D and S labelled, equilibrium P* and Q* marked.", s: { f: 65, k: 0 } },
  { cap: "<b>Draw the floor above P*</b>: a minimum price is only effective above equilibrium.", s: { f: 65, k: 1 } },
  { cap: "<b>Show the two quantities:</b> quantity demanded contracts to Qd, quantity supplied extends to Qs.", s: { f: 65, k: 2 } },
  { cap: "<b>Mark the excess supply</b> (Qs − Qd) and say in words what it means: consumption falls, but the extra supply is unsold. Refer to the diagram in the text for analysis marks.", s: { f: 65, k: 3 } },
] });

/* ---------- Lab 1: level checker ---------- */
function lvl() {
  const ids = ["st", "cx", "dg", "er", "sd"];
  if (!ids.every((i) => $("#" + i))) return;
  const [steps, ctx, dia, err, both] = ids.map((i) => +$("#" + i).value);
  let sc = steps * 1.0 + ctx * 1.0 + dia * 0.75 + (both ? 1.5 : 0) - err * 0.8, cap = 8, why = [];
  if (!both) { cap = Math.min(cap, 5); why.push("one-sided analysis is capped at Level 2 (5)"); }
  if (ctx === 0) { cap = Math.min(cap, 5); why.push("no application to the context caps the answer at Level 2"); }
  if (err >= 2) { cap = Math.min(cap, 5); why.push("several inaccuracies keep it at Level 2"); }
  if (steps <= 1) { cap = Math.min(cap, 2); why.push("a single step is assertion (Level 1)"); }
  let m = Math.max(0, Math.min(Math.round(sc), cap, 8)), L = m >= 6 ? 3 : m >= 3 ? 2 : m >= 1 ? 1 : 0;
  $("#r1").textContent = m + " / 8"; $("#r2").textContent = L ? "Level " + L : "No credit";
  let nx = L === 3 ? "Already at the top band: make every step precise" : L === 2 ? (!both ? "Analyse the other side or an alternative" : ctx < 2 ? "Use the named good, country or figures" : steps < 4 ? "Add another linked step" : "Explain the diagram and remove inaccuracies") : "Add a mechanism: say why, in at least three linked steps";
  $("#r3").textContent = nx;
  $("#rv").textContent = `${steps} linked step(s), ${["no", "general", "specific"][ctx]} application, diagram ${["absent", "drawn but not explained", "correct and explained"][dia]}, ${err} error(s), ${both ? "both sides or an alternative" : "one side only"}: about ${m} out of 8 (Level ${L || 0}).` + (why.length ? " Capped because " + why.join("; ") + "." : "");
  const W = 380, X = (v) => 20 + (v / 8) * W;
  let o = SV.rect(X(0), 60, X(2) - X(0), 40, "f3", op(0.4)) + SV.rect(X(2), 60, X(5) - X(2), 40, "f1", op(0.4)) + SV.rect(X(5), 60, X(8) - X(5), 40, "f2", op(0.4));
  o += SV.text(X(1), 85, "L1", "lbl bd", { "text-anchor": "middle" }) + SV.text(X(3.5), 85, "L2", "lbl bd", { "text-anchor": "middle" }) + SV.text(X(6.5), 85, "L3", "lbl bd", { "text-anchor": "middle" });
  o += SV.line(X(m), 40, X(m), 125, "c4", { "stroke-width": 3 }) + SV.text(X(m), 34, m + "", "lbl bd", { "text-anchor": "middle" }) + SV.text(20, 160, "0", "sm") + SV.text(X(8), 160, "8", "sm", { "text-anchor": "end" });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "st", label: "Linked steps in the best chain (0 to 5) ", min: 0, max: 5, step: 1, value: 3, fmt: (v) => v, onInput: lvl });
Lib.slider($("#g2"), { id: "cx", label: "Application: 0 none, 1 general, 2 specific ", min: 0, max: 2, step: 1, value: 1, fmt: (v) => ["none", "general", "specific"][v], onInput: lvl });
Lib.slider($("#g3"), { id: "dg", label: "Diagram: 0 none, 1 not explained, 2 explained ", min: 0, max: 2, step: 1, value: 1, fmt: (v) => ["none", "not explained", "explained"][v], onInput: lvl });
Lib.slider($("#g4"), { id: "er", label: "Inaccuracies or irrelevant points ", min: 0, max: 3, step: 1, value: 0, fmt: (v) => v, onInput: lvl });
Lib.slider($("#g5"), { id: "sd", label: "Other side or alternative analysed? (0 no, 1 yes) ", min: 0, max: 1, step: 1, value: 0, fmt: (v) => (v ? "yes" : "no"), onInput: lvl });
lvl();

chooser("h", [
  ["Indirect tax", "Costs rise, supply shifts left by the tax, price rises, quantity demanded contracts; elasticity decides who pays", "Name the good and its elasticity (for example cigarettes: addictive, inelastic)", "Shifting the demand curve instead of supply", 5],
  ["Interest rate rise", "Borrowing dearer, saving more attractive, C and I fall, AD shifts left, price level falls", "Use the data or country: who has variable-rate mortgages", "Stopping at 'spending falls' without reaching AD and prices", 5],
  ["Depreciation", "Exports cheaper, imports dearer, net exports rise if elastic, AD rises; dearer inputs shift SRAS left", "State what the country exports and imports", "Assuming net exports always rise", 4],
  ["Supply-side policy", "Training raises productivity, unit costs fall, SRAS and LRAS shift right", "Name the policy, such as apprenticeships, and the time lag", "Forgetting the short-run AD effect of government spending", 4],
  ["Tariff", "Import price rises, imports fall, domestic output rises, consumers lose, revenue gained", "Use the elasticity of demand for imports and possible retaliation", "Ignoring the welfare loss", 4],
  ["Maximum price", "Set below equilibrium: quantity demanded rises, quantity supplied falls, shortage, rationing", "Name the good (rent, bread) and who is protected", "Drawing the line above equilibrium", 4]
], (it) => `${it[0]}: ${it[1].toLowerCase()}. To apply it: ${it[2].toLowerCase()}. A usual slip: ${it[3].toLowerCase()}.`, "How often this chain is asked");
chooser("k", [
  ["'A minimum price makes the price go up.'", "Correct but descriptive: no AO2 credit beyond a knowledge point", "It states the result without why or what follows", "Add: the floor is above equilibrium, so quantity demanded falls", 1],
  ["'Quantity demanded falls, so consumption of the demerit good falls.'", "One analysis step", "A correct link, but short", "Add why the quantity falls and what limits it (elasticity)", 2],
  ["'If demand is inelastic, a 20% rise in price cuts quantity by only 5%, so consumption falls little and spending rises.'", "Developed analysis with a figure", "A mechanism, a number and a consequence", "Link back to the policy question and add the effect on health costs", 4],
  ["'The extra revenue goes to retailers, not the government, unlike a tax.'", "Analysis that also begins a comparison", "It brings in an alternative and a reason", "Develop the tax alternative fully for Level 3", 4],
  ["'So this shows a minimum price is not the best policy.'", "A judgement (evaluation), not analysis", "It answers the question but is not an explanation", "Keep for the conclusion; support it with a condition", 3]
], (it) => `${it[0]} Annotation: ${it[1].toLowerCase()}. Why: ${it[2].toLowerCase()}. To improve: ${it[3].toLowerCase()}.`, "Strength of the sentence");
Lib.classify($("#cl1"), { prompt: "Is the sentence description or analysis?", buckets: [{"label": "Description"}, {"label": "Analysis"}], items: [{"text": "A minimum price is a legal floor on a price.", "b": 0}, {"text": "Because the floor is above equilibrium, quantity demanded contracts, so consumption of alcohol falls.", "b": 1}, {"text": "Unemployment is people without a job.", "b": 0}, {"text": "As unemployment rises, income tax receipts fall and benefit spending rises, so the budget deficit widens.", "b": 1}, {"text": "A tariff is a tax on imports.", "b": 0}, {"text": "A tariff raises the import price, so imports fall and domestic output rises.", "b": 1}], done: "Description says what something is; analysis says why and what follows." });
Lib.classify($("#cl2"), { prompt: "Is the sentence generic or applied?", buckets: [{"label": "Generic"}, {"label": "Applied"}], items: [{"text": "The tax makes the good more expensive.", "b": 0}, {"text": "A 20% tax on cigarettes raises their price, but addicted smokers keep buying, so demand is inelastic.", "b": 1}, {"text": "The depreciation helps exports.", "b": 0}, {"text": "After the depreciation the country's coffee is cheaper abroad, but demand for coffee is inelastic, so revenue may fall.", "b": 1}, {"text": "Unemployment harms the economy.", "b": 0}, {"text": "Unemployment rose from 5% to 8%, so tax revenue falls.", "b": 1}], done: "Applied sentences use the named good, country or figures; generic ones could appear in any answer." });
Lib.order($("#o1"), { prompt: "Put the chain in order: a rise in interest rates reduces inflation.", items: ["The central bank raises the base rate", "Borrowing is dearer and saving more attractive", "Consumption and investment fall", "AD shifts to the left", "The price level falls, so inflation is reduced"], done: "A chain is a sequence of linked steps from cause to the effect asked for." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Level 1 analysis", "Largely descriptive; significant errors or omissions"], ["Level 2 analysis", "Generally accurate, some development but little detail"], ["Level 3 analysis", "Developed and detailed, accurate use of concepts and tools, fully explained"], ["One-sided response", "Capped at Level 2 in the mark scheme"], ["Application", "Using the good, policy, country or data in the question"], ["Chain of reasoning", "Linked steps from cause to effect"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "A 12 mark question is marked out of 8 for AO1 and AO2 and 4 for AO3. What fraction of the marks is for AO3 (%)?", "a": 33.3, "unit": "%", "tol": 0.3, "hint": "4 ÷ 12.", "sol": "<b>33.3%</b>."},
  {"q": "Level 2 in Table A is 3 to 5 marks. How many marks lie in the Level 2 band (count inclusive)?", "a": 3, "unit": "marks", "tol": 0.1, "hint": "3, 4, 5.", "sol": "<b>3</b> marks."},
  {"q": "Paper 2 is 60 marks in 120 minutes. How many minutes per mark?", "a": 2, "unit": "min", "tol": 0.05, "hint": "120 ÷ 60.", "sol": "<b>2 minutes</b>."},
  {"q": "A 12 mark answer is to take 20 minutes. What fraction of a 6 mark question's time (at 2 minutes a mark) is that?", "a": 1.67, "unit": "", "tol": 0.05, "hint": "20 ÷ 12 minutes.", "sol": "A 6 mark question takes 12 minutes, so 20 ÷ 12 = <b>1.67</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A response is correct but states only that 'a tax raises the price'. At which level is its analysis?", opts: ["Level 1", "Level 2", "Level 3", "No credit"], a: 0, why: "A statement without a mechanism is largely descriptive." },
  { q: "Which feature most clearly separates Level 3 from Level 2 analysis?", opts: ["Developed, detailed analysis with tools fully explained", "A longer definition", "More facts in the introduction", "A summary at the end"], a: 0, why: "Level 3 develops and explains; Level 2 is accurate but limited." },
  { q: "A mark scheme says a one-sided response cannot exceed Level 2. What does this mean?", opts: ["Even excellent one-sided analysis stops at the top of Level 2", "Level 3 is for long answers only", "Only evaluation is capped", "It does not affect analysis"], a: 0, why: "Balance is part of the Level 3 descriptor." },
  { q: "Which is an applied sentence?", opts: ["The tax raises the price.", "The 20% tax on cigarettes hits addicted smokers whose demand is inelastic.", "Taxes exist in most countries.", "Elasticity measures responsiveness."], a: 1, why: "It uses the good and the specific market feature." },
  { q: "A diagram is drawn with labelled axes but never mentioned in the text. Likely credit?", opts: ["Partly credited for knowledge but the analysis is limited", "Full analysis marks", "No marks for anything", "Evaluation marks"], a: 0, why: "Diagrams must be used and explained to earn analysis credit." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Level 1", "Assertion, no mechanism."],
  ["Level 2", "Mechanism, limited detail."],
  ["Level 3", "Developed, accurate, applied, balanced."],
  ["Chain", "Cause, mechanism, effect: 3+ steps."],
  ["Applied", "Uses the named good, country or data."],
  ["One-sided", "Capped at Level 2."],
  ["8 mark part", "3 analysis marks."],
  ["12 mark part", "AO1 and AO2 out of 8."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "Increased international competition leads to a worsening in a country's current account balance. In the absence of any offsetting factors, how is this likely to affect the exchange rate and domestic cost-push inflation? (exchange rate, cost-push inflation) (May/June 2021 · 12 · Q27, reworded)", opts: ["appreciate, decrease", "appreciate, increase", "depreciate, decrease", "depreciate, increase"], a: 3, why: "A worse current account tends to lower the exchange rate, which raises import costs and cost-push inflation: a three-step chain." },
  { q: "Why will a contractionary monetary policy reduce inflation? (May/June 2022 · 11 · Q29, reworded)", opts: ["Banks will lend more", "Consumers will have higher disposable income", "Consumers will pay more tax", "Consumers will save more"], a: 3, why: "Higher interest rates encourage saving and reduce spending, lowering AD." },
  { q: "An economy has an unemployment rate of 8%, an increase of 2% from the previous year. At the same time, the current account deficit rose from 3% of GDP to 4% of GDP. What would be most likely to reduce both unemployment and the current account deficit? (Feb/March 2024 · 12 · Q21, reworded)", opts: ["decrease government spending", "depreciation of the currency", "increase indirect taxation", "increase interest rates"], a: 1, why: "A depreciation could raise exports and reduce imports, boosting AD, output and employment while narrowing the deficit." },
  { q: "An indirect tax is imposed on good X. Which situation is most likely to result in producers bearing a higher burden of the tax? (May/June 2025 · 12 · Q11, reworded)", opts: ["price elasticity of demand is elastic", "price elasticity of demand is inelastic", "price elasticity of supply is elastic", "price elasticity of supply is inelastic"], a: 0, why: "With elastic demand, a price rise cuts quantity a lot, so producers absorb more of the tax." },
  { q: "In which circumstance will the total expenditure by consumers on a good increase when its price increases? (Feb/March 2020 · 12 · Q5, reworded)", opts: ["Demand for the good is income elastic.", "Demand for the good is price inelastic.", "The price of a complementary good also increases.", "The price of substitute goods also increases."], a: 1, why: "With inelastic demand quantity falls by a smaller percentage than price rises, so expenditure rises." },
  { q: "A country has a balance of trade deficit. When will this be least likely to be improved as a result of a depreciation of its currency? (May/June 2021 · 13 · Q25, reworded)", opts: ["if it is currently operating with a significant amount of unused resources", "if the sum of the price elasticities of demand for exports and imports is less than 1", "if in the long term, the price elasticity of demand for exports should increase", "if the country uses a relatively small proportion of imports in their production process"], a: 1, why: "If the sum of the elasticities is below one, the Marshall-Lerner condition fails." },
] });
