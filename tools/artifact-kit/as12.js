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

/* ---------- positive / normative ---------- */
const STM = [["The government should cut income tax", "normative", "should"], ["Cutting income tax raises disposable income", "positive", "raises"], ["Unemployment fell from 6% to 5% last year", "positive", "fell"], ["The minimum wage is unfair to small firms", "normative", "unfair"]];
function pnDraw(s) {
  let o = ""; STM.forEach(([t, kind, cue], i) => { const k = Math.max(0, Math.min(1, s.i - i)); if (k <= 0) return; const y = 20 + i * 70, c = kind === "positive" ? "f3" : "f2", cueOn = s.c > i; o += SV.rect(30, y, 540, 50, "f1", op(0.25 * k)) + SV.text(46, y + 31, t, "lbl", op(k));
    if (cueOn) { const w = t.split(" "), idx = w.findIndex((x) => x.toLowerCase().startsWith(cue)); o += SV.rect(40 + w.slice(0, idx).join(" ").length * 8.4 + (idx ? 6 : 0), y + 10, cue.length * 8.8 + 6, 30, "f2", { opacity: 0.25 * k, rx: 4 }); }
    if (s.l > i) o += SV.rect(590, y + 6, 140, 38, c, op(0.7)) + SV.text(660, y + 31, kind === "positive" ? "POSITIVE: testable" : "NORMATIVE: opinion", "lbl bd", { "text-anchor": "middle" }); });
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="Four statements labelled positive or normative">${pnDraw({ i: 4, c: 4, l: 4 })}</svg>`;
Lib.stepper($("#stP"), { w: 760, h: 300, label: "Four statements classified as positive or normative", base: { i: 0, c: 0, l: 0 }, draw: pnDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>A value word.</b> 'The government <u>should</u> cut income tax' contains 'should'. Nobody can prove with data that it ought to happen, so it is a value judgement.", s: { i: 1, c: 1, l: 1 } },
  { cap: "<b>A testable claim.</b> 'Cutting income tax raises disposable income' is a cause-and-effect claim that can be checked against data. It is positive.", s: { i: 2, c: 2, l: 2 } },
  { cap: "<b>A fact.</b> 'Unemployment fell from 6% to 5%' can be checked. It is positive, even if the figures turn out to be wrong.", s: { i: 3, c: 3, l: 3 } },
  { cap: "<b>Another value judgement.</b> 'Unfair' depends on what someone believes is fair, so it is normative.", s: { i: 4, c: 4, l: 4 } },
] });

/* ---------- ceteris paribus ---------- */
const CX = (q) => 70 + (q - 60) * 6.6, CY = (p) => 300 - (p - 56) * 3.1;
function cpDraw(s) {
  let o = SV.line(70, 300, 730, 300) + SV.line(70, 300, 70, 30) + SV.text(730, 326, "Quantity demanded", "sm", { "text-anchor": "end" }) + SV.text(76, 24, "Price", "sm");
  const d = (sh) => [[CX(60), CY(140 + sh)], [CX(140), CY(60 + sh)]];
  o += SV.line(...d(0)[0], ...d(0)[1], "c1") + tag(CX(138), CY(62) + 22, "D₀", "t1", 1, "end");
  if (s.sh > 0.01) o += SV.line(...d(8 * s.sh)[0], ...d(8 * s.sh)[1], "c3") + tag(CX(140) + 6, CY(60 + 8 * s.sh) + 4, "D₁", "t3", 1, "start");
  o += SV.circle(CX(100), CY(100), 7, "dot1") + tag(CX(100) + 10, CY(100) + 20, "A  (P 100, Q 100)", "t1");
  if (s.m > 0) o += SV.circle(CX(100 - 5 * s.m), CY(100 + 5 * s.m), 7, "dot2") + tag(CX(100 - 5 * s.m) - 10, CY(100 + 5 * s.m) - 12, s.m > 0.9 ? "B  (P 105, Q 95)" : "", "t2", 1, "end");
  if (s.sh > 0.5) o += SV.circle(CX(95 + 8 * s.sh), CY(105), 7, "dot4") + tag(CX(95 + 8 * s.sh) + 10, CY(105) - 12, s.sh > 0.9 ? "C  observed (P 105, Q 103)" : "", "t4");
  return o;
}
Lib.stepper($("#stC"), { w: 760, h: 345, label: "Price up 5 percent along a demand curve, then an income rise shifting demand so that quantity demanded rises 3 percent", base: { sh: 0, m: 0 }, draw: cpDraw, tween: 1100, dwell: 5800, steps: [
  { cap: "<b>Start.</b> At a price of 100 the quantity demanded is 100 (point A on the demand curve D₀).", s: { sh: 0, m: 0 } },
  { cap: "<b>Ceteris paribus.</b> The price rises 5% and everything else is held constant. We move up D₀ to B: the quantity demanded falls to 95.", s: { sh: 0, m: 1 } },
  { cap: "<b>But other things change.</b> Incomes rise 4%, which shifts the demand curve right to D₁. At the new price the quantity demanded is now 103.", s: { sh: 1, m: 1 } },
  { cap: "<b>The observed result</b> (price +5%, quantity +3%) looks as if the law of demand has failed, but it has not. Other things did not remain equal.", s: { sh: 1, m: 1 } },
] });
$("#pic2").innerHTML = `<svg viewBox="0 0 760 345" role="img" aria-label="A demand curve and a shifted demand curve showing why other things must be held equal">${cpDraw({ sh: 1, m: 1 })}</svg>`;

/* ---------- Lab 1 ---------- */
function labS() {
  if (!$("#u0") || !$("#u1") || !$("#ac")) return;
  const a = +$("#u0").value / 10, b = +$("#u1").value / 10, ac = +$("#ac").value / 10;
  $("#r1").textContent = b < a ? "TRUE" : b > a ? "FALSE" : "FALSE (no change)"; $("#r2").textContent = b > ac ? "Agrees (for this view)" : "Disagrees (for this view)"; $("#r3").textContent = "Positive: yes. Normative: no";
  $("#rv").textContent = `Unemployment moved from ${a.toFixed(1)}% to ${b.toFixed(1)}%. The positive statement 'unemployment fell' is ${b < a ? "true" : "false"}: the data decide it. The normative statement 'unemployment is too high' is true only for someone who thinks ${ac.toFixed(1)}% is acceptable; another person may choose a different level, and no data can tell you which view is right.`;
  const Y = (v) => 270 - v * 20; let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 30) + SV.text(46, 22, "Unemployment rate, %", "sm");
  [["Year 1", a, "f1"], ["Year 2", b, "f3"]].forEach(([l, v, c], i) => { const x = 80 + i * 130; o += SV.rect(x, Y(v), 80, 270 - Y(v), c, op(0.75)) + SV.text(x + 40, 290, l, "sm", { "text-anchor": "middle" }) + tag(x + 40, Y(v) - 6, v.toFixed(1) + "%", "t1", 1, "middle"); });
  o += SV.line(40, Y(ac), 400, Y(ac), "c2 dash") + tag(396, Y(ac) - 6, "your 'acceptable' rate " + ac.toFixed(1) + "%", "t2", 1, "end");
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "u0", label: "Unemployment, year 1, % ", min: 20, max: 120, step: 1, value: 60, fmt: (v) => (v / 10).toFixed(1), onInput: labS });
Lib.slider($("#g2"), { id: "u1", label: "Unemployment, year 2, % ", min: 20, max: 120, step: 1, value: 50, fmt: (v) => (v / 10).toFixed(1), onInput: labS });
Lib.slider($("#g3"), { id: "ac", label: "The rate YOU think is acceptable, % ", min: 20, max: 120, step: 1, value: 40, fmt: (v) => (v / 10).toFixed(1), onInput: labS });
labS();

/* ---------- Lab 2 ---------- */
function labT() {
  if (!$("#pr") || !$("#e1") || !$("#e2")) return;
  const pr = +$("#pr").value, e1 = +$("#e1").value / 10, e2 = +$("#e2").value / 10, base = 100000, sr = base * (1 + e1 * pr / 100), lr = base * (1 + e2 * pr / 100);
  $("#t1").textContent = Math.round(sr).toLocaleString("en-US"); $("#t2").textContent = Math.round(lr).toLocaleString("en-US"); $("#t3").textContent = "+" + Math.round(lr - sr).toLocaleString("en-US");
  $("#tv").textContent = `A ${pr}% price rise with a short-run price elasticity of supply of ${e1.toFixed(1)} raises the quantity supplied by ${Lib.fmtN(e1 * pr, 1)}% to ${Math.round(sr).toLocaleString("en-US")}. In the long run, with an elasticity of ${e2.toFixed(1)}, supply rises ${Lib.fmtN(e2 * pr, 1)}% to ${Math.round(lr).toLocaleString("en-US")}. Firms can adjust more as time passes, so the response is bigger.`;
  const Y = (v) => 270 - (v - 90000) / 40000 * 220; let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 30) + SV.text(46, 22, "Quantity supplied", "sm");
  [["Before", base, "f1"], ["Short run", sr, "f2"], ["Long run", lr, "f3"]].forEach(([l, v, c], i) => { const x = 60 + i * 115; o += SV.rect(x, Y(v), 80, 270 - Y(v), c, op(0.75)) + SV.text(x + 40, 290, l, "sm", { "text-anchor": "middle" }) + tag(x + 40, Y(v) - 6, Math.round(v / 1000) + "k", "t1", 1, "middle"); });
  $("#labB").innerHTML = o;
}
Lib.slider($("#g4"), { id: "pr", label: "Price rise, % ", min: 2, max: 30, step: 1, value: 10, fmt: (v) => v + "%", onInput: labT });
Lib.slider($("#g5"), { id: "e1", label: "Short-run PES × 10 ", min: 1, max: 20, step: 1, value: 8, fmt: (v) => (v / 10).toFixed(1), onInput: labT });
Lib.slider($("#g6"), { id: "e2", label: "Long-run PES × 10 ", min: 5, max: 40, step: 1, value: 14, fmt: (v) => (v / 10).toFixed(1), onInput: labT });
labT();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Positive or normative?", buckets: [{"label": "Positive"}, {"label": "Normative"}], items: [{"text": "A rise in interest rates will reduce consumer spending", "b": 0}, {"text": "The government should reduce income inequality", "b": 1}, {"text": "Inflation was 3% last year", "b": 0}, {"text": "A minimum wage is unfair to small businesses", "b": 1}, {"text": "Higher taxes on cigarettes reduce smoking", "b": 0}, {"text": "Healthcare ought to be free for everyone", "b": 1}, {"text": "Unemployment is lower in country A than in country B", "b": 0}, {"text": "Economic growth is more important than low inflation", "b": 1}], done: "Positive: can be tested with data. Normative: a value judgement." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Positive statement", "A statement of fact that can be tested"], ["Normative statement", "A value judgement about what ought to be"], ["Ceteris paribus", "All other things being equal"], ["Short run", "At least one factor of production is fixed"], ["Long run", "All factors can be varied; technology fixed"], ["Very long run", "Technology and other conditions can change"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the steps for classifying a statement in order.", items: ["Read the statement carefully", "Look for value words such as should, ought, fair", "Ask whether data could prove it true or false", "Label it positive if it can be tested, normative if not", "Give one reason for your label"], done: "Value words and testability decide the label." });
Lib.calc($("#c1"), { qs: [
  {"q": "Price elasticity of supply is 0.8 in the short run. A price rise of 10% starts from a supply of 100,000. By how many units does supply rise in the short run?", "a": 8000, "unit": "units", "tol": 1, "hint": "0.8 × 10% × 100,000.", "sol": "8% of 100,000 = <b>8,000 units</b>."},
  {"q": "In the long run the elasticity is 1.4. By how many units does supply rise for the same price rise?", "a": 14000, "unit": "units", "tol": 1, "hint": "1.4 × 10% × 100,000.", "sol": "<b>14,000 units</b>."},
  {"q": "What is the difference between the long-run and short-run increases (units)?", "a": 6000, "unit": "units", "tol": 1, "hint": "14,000 − 8,000.", "sol": "<b>6,000 units</b>."},
  {"q": "Ceteris paribus, with a price elasticity of demand of 1, a 5% price rise changes the quantity demanded by what percentage (%)?", "a": -5, "unit": "%", "tol": 0.1, "hint": "PED × % change in price, with the opposite sign.", "sol": "<b>−5%</b>: demand falls when price rises, other things equal."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which is a normative statement?", opts: ["Unemployment fell last year", "The government should help the unemployed", "Inflation is measured by a price index", "Higher prices reduce demand"], a: 1, why: "'Should' signals a value judgement." },
  { q: "Why do economists use ceteris paribus?", opts: ["To isolate the effect of one variable", "Because everything else always changes", "To avoid using data", "To make assumptions realistic"], a: 0, why: "Holding other things constant separates cause and effect." },
  { q: "In the short run:", opts: ["At least one factor of production is fixed", "All factors are variable", "Technology can change", "Supply is perfectly elastic"], a: 0, why: "That is the definition of the short run." },
  { q: "A positive statement:", opts: ["Can be tested and may be false", "Is always true", "Is an opinion", "Uses the word should"], a: 0, why: "Positive statements are testable, not necessarily correct." },
  { q: "The price elasticity of supply is usually higher in the long run because:", opts: ["Firms can change all factors of production", "Prices are lower", "Consumers buy more", "The government lowers taxes"], a: 0, why: "More inputs can be varied given time." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Social science", "Studies human behaviour; results are tendencies."],
  ["Positive", "Testable fact; may be true or false."],
  ["Normative", "Value judgement; should, ought, fair."],
  ["Ceteris paribus", "All other things equal."],
  ["Short run", "At least one fixed factor."],
  ["Long run", "All factors variable."],
  ["Very long run", "Technology can change."],
  ["Why time matters", "Elasticities and responses differ."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "A newspaper article says: 1. The burden of tax should be shifted more to the highest earners. 2. It is in the public interest that key services are nationalised. Which type of statement is each? (Feb/March 2020 · 12 · Q3, reworded)", opts: ["Both normative", "1 normative, 2 positive", "1 positive, 2 normative", "Both positive"], a: 0, why: "Both contain value judgements ('should', 'in the public interest'), so both are normative." },
  { q: "Which statement is a positive statement? (Feb/March 2021 · 12 · Q4, reworded)", opts: ["The distribution of income and wealth in most western European countries is unequal", "The government ought to increase income tax on high earners", "There should be more legal rights for workers", "Wages of those on low incomes should be increased"], a: 0, why: "It describes a fact that can be tested. The others use 'ought' and 'should'." },
  { q: "Which statement is a normative statement? (Feb/March 2024 · 12 · Q2, reworded)", opts: ["Aggregate demand will increase following a fall in interest rates", "A rise in unemployment will decrease inflationary pressures", "The incentive to work will rise if benefit payments are reduced", "Unsustainable economic growth is more harmful to the economy than hyperinflation"], a: 3, why: "Judging what is 'more harmful' is a value judgement. The others are predictions that can be tested." },
  { q: "In 2015 the Chinese economy grew by 6.9%, India's by 7.6% and the US by 2.4%. Which comment contains two positive statements? (May/June 2021 · 11 · Q1, reworded)", opts: ["Chinese growth exceeded US growth by 4.5% in 2015 but was 0.7% less than India's", "Chinese growth was more than double the US's but disappointing compared with India's", "India's growth was better than that of the US", "US growth was too low in 2015 and India's was too high"], a: 0, why: "Both parts of the first comment are facts that can be checked against the figures. 'Disappointing', 'better' and 'too low' are value judgements." },
  { q: "Which list has the most words that are likely to relate to a positive statement rather than a normative one? (May/June 2022 · 12 · Q1, reworded)", opts: ["Describe, better, should, value, emotion", "Bias, objective, ought, opinion, tastes", "Contestable, is, motive, subjective, moral", "Actual, ethics, fact, was, testable"], a: 3, why: "Words such as actual, fact, was and testable point to positive statements; should, ought, better and moral point to normative ones." },
  { q: "What does the phrase 'ceteris paribus' mean? (May/June 2021 · 11 · Q4, reworded)", opts: ["All the resources used are of equal quality", "Everything else remains unchanged", "The price mechanism rations scarce goods", "The variable under consideration is held constant"], a: 1, why: "It means all other things are held equal. Option D is the opposite: it is the variable studied that changes." },
  { q: "Demand curves are drawn ceteris paribus. Which 'other things' are not required to remain the same when an individual's demand curve for ice cream is constructed? (Feb/March 2022 · 12 · Q7, reworded)", opts: ["The consumer's income", "The consumer's tastes and preferences", "The price of fresh fruit", "The price of ice cream"], a: 3, why: "The price of ice cream is the variable on the vertical axis and is allowed to change. Everything else is held constant." },
  { q: "The price of a good rises by 5% and the quantity demanded rises by 3%. At the same time, consumers' incomes rise by 4%. The law of demand appears not to be working. What is the most likely explanation? (Feb/March 2025 · 12 · Q4, reworded)", opts: ["Other things did not remain equal", "The demand for the good was price inelastic", "The real price of the good fell", "The time period was the very short run"], a: 0, why: "The rise in income shifted the demand curve, so ceteris paribus did not hold." },
  { q: "What is the definition of the long run? (Feb/March 2023 · 12 · Q2, reworded)", opts: ["The time period when all factors of production are specialised", "The time period when all factors of production are variable", "The time period when all key inputs are variable and technology can change", "The time period when at least one factor of production is fixed"], a: 1, why: "In the long run all factors of production can be varied. In the short run at least one is fixed." },
  { q: "What distinguishes the very long run from the long run? (Feb/March 2021 · 12 · Q3, reworded)", opts: ["The ability to change resource allocation", "The ability to change the state of technology", "The absence of government market intervention", "The existence of variable factors of production"], a: 1, why: "In the very long run technology can change, whereas it is fixed in the long run." },
  { q: "To increase production, a firm in industry X needs to install capital equipment, while a firm in industry Y needs to research and introduce new technology. What time periods are illustrated? (Feb/March 2025 · 12 · Q2, reworded)", opts: ["Short run for X, long run for Y", "Long run for both", "Long run for X, very long run for Y", "Very long run for both"], a: 2, why: "Installing equipment means varying a factor of production (long run). Introducing new technology is a change in technology (very long run)." },
  { q: "When the price of good X is $2.00, the quantity supplied is 100,000. The price elasticity of supply is 0.8 in the short run and 1.4 in the long run. The price rises to $2.20. What is the increase in the quantity supplied between the short run and the long run? (May/June 2023 · 11 · Q7, reworded)", opts: ["6,000", "60,000", "114,000", "140,000"], a: 0, why: "A 10% price rise gives +8% (108,000) in the short run and +14% (114,000) in the long run: a difference of 6,000." },
] });
