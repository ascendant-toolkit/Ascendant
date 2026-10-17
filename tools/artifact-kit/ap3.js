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

/* ---------- 75 minutes ---------- */
const TX = (m) => 70 + m * 8.8;
function timeDraw(s) {
  let o = SV.line(70, 150, 730, 150) + SV.text(70, 28, "0 min", "sm") + SV.text(730, 28, "75 min", "sm", { "text-anchor": "end" });
  [0, 15, 30, 45, 60, 75].forEach((m) => (o += SV.line(TX(m), 144, TX(m), 156) + SV.text(TX(m), 176, m, "sm", { "text-anchor": "middle" })));
  const blk = (a, b, c, l, sub, k) => (k > 0 ? SV.rect(TX(a), 60, TX(b) - TX(a), 76, c, op(0.65 * k)) + SV.text((TX(a) + TX(b)) / 2, 92, l, "lbl bd", { "text-anchor": "middle", ...op(k) }) + SV.text((TX(a) + TX(b)) / 2, 112, sub, "sm", { "text-anchor": "middle", ...op(k) }) : "");
  o += blk(0, 50, "f1", "First pass", "30 questions, about 100 seconds each", s.a) + blk(50, 66, "f3", "Second pass", "hard ones", s.b) + blk(66, 75, "f2", "Check", "sheet", s.c);
  if (s.d > 0) o += tag(400, 220, "Total: 75 minutes. Any blank at the end gets a guess: there is no penalty.", "t4", s.d, "middle");
  return o;
}
Lib.stepper($("#pic1"), { w: 760, h: 250, label: "A 75 minute timeline split into a 50 minute first pass, a 16 minute second pass and a 9 minute check", base: { a: 0, b: 0, c: 0, d: 0 }, draw: timeDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>First pass, about 50 minutes.</b> Go through all 30 questions at roughly 100 seconds each. Answer what you can, make a best guess on the rest and flag anything that needs more than a minute or two.", s: { a: 1 } },
  { cap: "<b>Second pass, about 16 minutes.</b> Return to the flagged questions. Use the four-step method and give each a fair try, but stop at 3 minutes.", s: { a: 1, b: 1 } },
  { cap: "<b>Check, about 9 minutes.</b> Make sure every question has an answer, the letters match the question numbers, and re-read the stems of the negative questions.", s: { a: 1, b: 1, c: 1 } },
  { cap: "<b>Total 75 minutes.</b> There is no negative marking, so fill every blank before time runs out.", s: { a: 1, b: 1, c: 1, d: 1 } },
] });
$("#pic2").innerHTML = (() => { const v = [["A", 21], ["B", 27], ["C", 28], ["D", 24]]; let o = SV.line(70, 190, 730, 190) + SV.line(70, 190, 70, 20) + SV.text(76, 16, "Share of correct answers (%)", "sm"); v.forEach(([l, p], i) => { const x = 130 + i * 140, h = p * 5; o += SV.rect(x, 190 - h, 80, h, "f1", op(0.7)) + SV.text(x + 40, 210, "Answer " + l, "sm", { "text-anchor": "middle" }) + SV.text(x + 40, 190 - h - 8, p + "%", "lbl bd", { "text-anchor": "middle" }); }); return `<svg viewBox="0 0 760 225" role="img" aria-label="Correct answers by letter in 1,155 Paper 3 questions: A 21 percent, B 27, C 28, D 24">${o}</svg>`; })();

/* ---------- the four steps on a real question ---------- */
const OPT = ["A  An improvement in labour productivity", "B  An improvement in the quality of capital and technology", "C  An increase in the birth rate and a fall in the death rate", "D  An increase in the availability of natural resources"];
function stepDraw(s) {
  let o = SV.rect(40, 14, 680, 44, "f1", op(0.25)) + SV.text(60, 42, "What is", "lbl bd") + SV.text(120, 42, "least likely", "lbl bd", { style: "fill:var(--bad)" + (s.q > 0 ? ";text-decoration:underline" : "") }) + SV.text(220, 42, "to lead to an increase in a country's optimum population?", "lbl bd");
  if (s.p > 0) o += SV.rect(40, 66, 680, 34, "f3", op(0.3 * s.p)) + SV.text(60, 88, "My prediction: optimum rises with productivity, capital, technology and resources. Look for the one that is not.", "sm", op(s.p));
  OPT.forEach((t, i) => { const y = 112 + i * 44, el = i !== 2 ? Math.max(0, Math.min(1, s.e)) : 0, ok = i === 2 && s.c > 0; o += SV.rect(40, y, 680, 36, ok ? "f3" : "f1", op(ok ? 0.55 : 0.18)) + SV.text(60, y + 24, t, "lbl", { style: el > 0.5 ? "text-decoration:line-through;opacity:.45" : "" }) + (el > 0.5 ? SV.text(700, y + 24, "✗ raises the optimum", "sm", { "text-anchor": "end", style: "fill:var(--bad)" }) : "") + (ok ? SV.text(700, y + 24, "✓ changes actual, not optimum", "sm", { "text-anchor": "end", style: "fill:var(--good)" }) : ""); });
  return o;
}
Lib.stepper($("#stM"), { w: 760, h: 300, label: "The four steps applied to a negative optimum population question", base: { q: 0, p: 0, e: 0, c: 0 }, draw: stepDraw, tween: 700, dwell: 6200, steps: [
  { cap: "<b>Step 1 · Read the stem.</b> Underline <b>least likely</b>. This is a negative question: three options raise the optimum population and one does not.", s: { q: 1 } },
  { cap: "<b>Step 2 · Predict.</b> Before reading the options, list what raises the optimum population: higher productivity, better capital and technology, more resources.", s: { q: 1, p: 1 } },
  { cap: "<b>Step 3 · Eliminate.</b> A, B and D each raise output per head at every population size, so they raise the optimum. Cross them out.", s: { q: 1, p: 1, e: 1 } },
  { cap: "<b>Step 4 · Check.</b> C changes the actual size of the population, not the best size. It is the answer to 'least likely'.", s: { q: 1, p: 1, e: 1, c: 1 } },
] });

/* ---------- Lab 1 ---------- */
function labC() {
  if (!$("#nm") || !$("#in") || !$("#pg")) return;
  const n = +$("#nm").value / 10, p = +$("#in").value / 10, q = +$("#pg").value / 10, right = ((1 + n / 100) / (1 + p / 100) / (1 + q / 100) - 1) * 100, noPop = ((1 + n / 100) / (1 + p / 100) - 1) * 100, noInf = ((1 + n / 100) / (1 + q / 100) - 1) * 100;
  $("#r1").textContent = (right >= 0 ? "+" : "") + Lib.fmtN(right, 1) + "%"; $("#r2").textContent = (noPop >= 0 ? "+" : "") + Lib.fmtN(noPop, 1) + "%"; $("#r3").textContent = (noInf >= 0 ? "+" : "") + Lib.fmtN(noInf, 1) + "%";
  $("#rv").textContent = `Nominal income grew ${Lib.fmtN(n, 1)}%, prices ${Lib.fmtN(p, 1)}% and population ${Lib.fmtN(q, 1)}%. Real income per head changed by about ${Lib.fmtN(right, 1)}%. Forgetting the population gives ${Lib.fmtN(noPop, 1)}% and forgetting inflation gives ${Lib.fmtN(noInf, 1)}%: examiners often include these as the wrong options. Quick check: ${Lib.fmtN(n, 1)} − ${Lib.fmtN(p, 1)} − ${Lib.fmtN(q, 1)} = ${Lib.fmtN(n - p - q, 1)}.`;
  const Y = (v) => 150 - v * 8; let o = SV.line(40, 150, 400, 150) + SV.line(40, 20, 40, 280) + SV.text(46, 16, "% change", "sm");
  [["Correct", right, "f3"], ["No population", noPop, "f2"], ["No inflation", noInf, "f2"]].forEach(([l, v, c], i) => { const x = 60 + i * 115, y = Y(Math.max(-16, Math.min(16, v))); o += SV.rect(x, Math.min(y, 150), 80, Math.abs(y - 150), c, op(i ? 0.5 : 0.85)) + SV.text(x + 40, 296, l, "sm", { "text-anchor": "middle" }) + tag(x + 40, v >= 0 ? y - 6 : y + 16, (v >= 0 ? "+" : "") + Lib.fmtN(v, 1), "t1", 1, "middle"); });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "nm", label: "Nominal income growth, % ", min: -20, max: 100, step: 5, value: 20, fmt: (v) => (v / 10).toFixed(1), onInput: labC });
Lib.slider($("#g2"), { id: "in", label: "Inflation, % ", min: 0, max: 100, step: 5, value: 30, fmt: (v) => (v / 10).toFixed(1), onInput: labC });
Lib.slider($("#g3"), { id: "pg", label: "Population growth, % ", min: -10, max: 30, step: 5, value: 10, fmt: (v) => (v / 10).toFixed(1), onInput: labC });
labC();

/* ---------- Lab 2 ---------- */
function labT() {
  if (!$("#sp") || !$("#fl") || !$("#fs")) return;
  const sp = +$("#sp").value, fl = +$("#fl").value, fs = +$("#fs").value, p1 = 30 * sp / 60, p2 = fl * fs / 60, left = 75 - p1 - p2;
  $("#t1").textContent = Lib.fmtN(p1, 0) + " min"; $("#t2").textContent = Lib.fmtN(p2, 0) + " min"; $("#t3").textContent = (left >= 0 ? "" : "−") + Lib.fmtN(Math.abs(left), 0) + " min";
  $("#tv").textContent = left >= 8 ? `At ${sp} seconds per question you finish the first pass in ${Lib.fmtN(p1, 0)} minutes, spend ${Lib.fmtN(p2, 0)} on the ${fl} flagged questions and still have ${Lib.fmtN(left, 0)} minutes to check. That is a safe plan.` : left >= 0 ? `This leaves only ${Lib.fmtN(left, 0)} minutes to check. Speed up the first pass or flag fewer questions.` : `This plan takes ${Lib.fmtN(-left, 0)} minutes more than you have. Cut the time on the second pass: guess on the hardest questions rather than run out of time.`;
  const X = (m) => 30 + m * 4.6; let o = SV.line(30, 160, 380, 160) + SV.text(30, 40, "0", "sm") + SV.text(X(75), 40, "75 min", "sm", { "text-anchor": "end" });
  const segs = [["First pass", p1, "f1"], ["Second pass", p2, "f3"], ["Left to check", Math.max(0, left), left >= 8 ? "f1" : "f2"]]; let x0 = 0;
  segs.forEach(([l, v, c], i) => { const w = Math.min(v, 75 - x0) * 4.6; o += SV.rect(X(x0), 80, Math.max(0, w), 60, c, op(i === 2 ? 0.35 : 0.7)) + (w > 28 ? SV.text(X(x0) + w / 2, 115, Lib.fmtN(v, 0), "lbl bd", { "text-anchor": "middle" }) : "") + SV.text(X(x0) + w / 2, 180 + i * 14, l, "sm", { "text-anchor": "middle" }); x0 += v; });
  $("#labB").innerHTML = o;
}
Lib.slider($("#g4"), { id: "sp", label: "Seconds per question on the first pass ", min: 60, max: 130, step: 5, value: 95, fmt: (v) => v, onInput: labT });
Lib.slider($("#g5"), { id: "fl", label: "Questions flagged as hard ", min: 0, max: 15, step: 1, value: 6, fmt: (v) => v, onInput: labT });
Lib.slider($("#g6"), { id: "fs", label: "Seconds per flagged question on the second pass ", min: 45, max: 240, step: 15, value: 120, fmt: (v) => v, onInput: labT });
labT();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Which type of question is it?", buckets: [{"label": "Negative"}, {"label": "Calculation"}, {"label": "Diagram or data"}, {"label": "Combination table"}], items: [{"text": "Which of these is not a function of the IMF?", "b": 0}, {"text": "GNP rises 3%, prices 4% and population 1%. What is the approximate change in real income per head?", "b": 1}, {"text": "The diagram shows a Lorenz curve with areas X and Y. How is the Gini coefficient calculated?", "b": 2}, {"text": "What is the effect on the current account and the financial account? (Improves or worsens for each)", "b": 3}, {"text": "What is least likely to raise the optimum population?", "b": 0}, {"text": "Employed 900,000 and unemployed 300,000. What is the unemployment rate?", "b": 1}, {"text": "From the table of birth rates and death rates, which conclusion can be drawn?", "b": 2}, {"text": "Which row shows the effect on employment, investment and the balance of payments (yes or no)?", "b": 3}], done: "Negative: not, least. Calculation: numbers and a rate. Diagram or data: a figure or table to read. Combination: a grid of yes/no columns." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Not, except, least likely", "Three options are true; find the odd one out"], ["Most likely, best", "Choose the strongest of several possibilities"], ["Definitely", "The conclusion must always follow, not just sometimes"], ["Per head", "Divide the total by the population"], ["Real", "Adjusted for inflation"], ["In the short run", "Before everything has adjusted; time can reverse the answer"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the four steps in order.", items: ["Read the stem and underline the qualifier", "Predict your own answer", "Eliminate the wrong options with reasons", "Check the answer against the qualifier and mark the sheet"], done: "Read, predict, eliminate, check." });
Lib.calc($("#c1"), { qs: [
  {"q": "Over a year nominal national income rises 5%, prices rise 3% and population rises 1%. By roughly what percentage does real income per head change (%, nearest whole number)?", "a": 1, "unit": "%", "tol": 0.1, "hint": "5 − 3 − 1.", "sol": "<b>+1%</b>: 1.05 ÷ 1.03 ÷ 1.01 = 1.009."},
  {"q": "Employed 1,500,000 and unemployed 100,000. Calculate the unemployment rate (%, 1 decimal place).", "a": 6.3, "unit": "%", "tol": 0.1, "hint": "Labour force = 1.6m.", "sol": "100,000 ÷ 1,600,000 × 100 = <b>6.3%</b>."},
  {"q": "The area between the line of equality and the Lorenz curve is 0.1 and the area under the Lorenz curve is 0.4. Calculate the Gini coefficient.", "a": 0.2, "unit": "", "tol": 0.005, "hint": "0.1 ÷ (0.1 + 0.4).", "sol": "<b>0.20</b>."},
  {"q": "The MPC is 0.75. Calculate the multiplier.", "a": 4, "unit": "", "tol": 0.01, "hint": "1 ÷ (1 − 0.75).", "sol": "<b>4</b>."},
  {"q": "Export prices rise 10% and import prices rise 25% (starting at 100 each). Calculate the terms of trade index.", "a": 88, "unit": "", "tol": 0.5, "hint": "110 ÷ 125 × 100.", "sol": "<b>88</b>: a deterioration."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "[Negative] Which is least likely to cause an increase in a country's long-run economic growth?", opts: ["Higher spending on education", "A fall in the capital stock", "Better technology", "More skilled migrants"], a: 1, why: "A fall in the capital stock reduces productive capacity. The other three raise it. Notice the qualifier: you need the one that does not help." },
  { q: "[Calculation] Nominal GDP rises 6% and prices rise 4%. Population is unchanged. What is the approximate change in real GDP per head?", opts: ["−2%", "0%", "+2%", "+10%"], a: 2, why: "6 − 4 = 2. The 10% option adds instead of subtracting, and −2% reverses the sign." },
  { q: "[Combination] A country's currency depreciates and the Marshall-Lerner condition holds. What happens to exports and to imports in domestic currency terms? Exports (volume) and import prices.", opts: ["Exports rise; import prices rise", "Exports rise; import prices fall", "Exports fall; import prices rise", "Exports fall; import prices fall"], a: 0, why: "Cheaper for foreigners means more exports, and a lower currency makes imports dearer at home. Half-right options reverse one column." },
  { q: "[Concept] Which curve shows income inequality rising and then falling as income per head rises?", opts: ["Lorenz curve", "Laffer curve", "Kuznets curve", "Phillips curve"], a: 2, why: "Four similar sounding curves are the classic 'neighbouring concept' distractor." },
  { q: "[Data] A table shows that in five countries those with a higher Gini coefficient also have a lower share of people below the poverty line. What can be concluded?", opts: ["Inequality causes lower poverty", "Inequality causes higher poverty", "There is a negative relationship in these countries but cause is not proved", "Poverty has fallen over time"], a: 2, why: "Data about five countries at one time show a pattern, not a cause or a trend." },
  { q: "[Application] A new factory pollutes a river used by a village downstream. This is an example of:", opts: ["A positive consumption externality", "A negative production externality", "A private cost", "A public good"], a: 1, why: "The cost falls on a third party (the village) and arises in production." },
  { q: "[Diagram] Supply of a good shifts right while demand is unchanged. What happens to equilibrium price and quantity?", opts: ["Price rises, quantity rises", "Price rises, quantity falls", "Price falls, quantity rises", "Price falls, quantity falls"], a: 2, why: "Sketch it: a rightward supply shift moves down the demand curve." },
  { q: "[Extreme wording] Which statement about tariffs is most likely to be correct?", opts: ["Tariffs always raise welfare", "Tariffs never affect prices", "Tariffs may protect domestic jobs but raise prices to consumers", "Tariffs only affect exporters"], a: 2, why: "The correct option is hedged ('may'). Statements with always, never and only are easy to disprove." },
] });
Lib.cards($("#fc1"), { cards: [
  ["The four steps", "Read, predict, eliminate, check."],
  ["Negative stem", "Three true, one odd one out."],
  ["Real income per head", "Nominal growth − inflation − population growth."],
  ["Unemployment rate", "Unemployed ÷ (employed + unemployed)."],
  ["Neighbouring concept", "Laffer, Lorenz, Kuznets, Phillips: know each."],
  ["Combination tables", "Decide each column, then match the row."],
  ["No negative marking", "Answer every question."],
  ["Timing", "About 100 seconds a question, then flagged ones, then check."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "[Negative] Which is not a source of market failure? (May/June 2022 · 31 · Q13, reworded)", opts: ["Imperfect information", "Income inequality", "Monopoly power", "Non-excludability"], a: 1, why: "Inequality is an equity issue, not a failure of the market to allocate resources efficiently. The others are classic causes of market failure." },
  { q: "[Negative] Which is not a reason for small firms to survive in a market dominated by large firms? (Oct/Nov 2020 · 31 · Q12, reworded)", opts: ["Small firms can concentrate on specialist services", "Small firms enjoy greater economies of scale", "Small firms enter with new ideas", "Small firms know local markets well"], a: 1, why: "Large firms, not small ones, usually enjoy the economies of scale." },
  { q: "[Negative] A government wants to reduce pollution from producing a good. Which policy does not make use of market forces? (May/June 2024 · 32 · Q11, reworded)", opts: ["A quota to limit production", "A regulation banning production", "A tax on production", "A tradable pollution permit system"], a: 1, why: "A ban is direct regulation. Taxes and tradable permits use prices and trading." },
  { q: "[Concept] If consumers aim to maximise utility, how will they arrange their spending? (Oct/Nov 2024 · 32 · Q1, reworded)", opts: ["Equal total utility from each commodity", "Equal total utility per $ on each commodity", "Equal utility from the last unit of each commodity", "Equal utility from the last $ spent on each commodity"], a: 3, why: "The equi-marginal principle: marginal utility per dollar is equal across goods. Options A to C mix up total, unit and per-dollar measures." },
  { q: "[Application] Helmets become compulsory for motorbike riders. What would be a positive externality of consumption? (Oct/Nov 2024 · 32 · Q4, reworded)", opts: ["Less pressure on the provision of health care", "Costs of checking that riders comply", "Increased life expectancy of riders", "Higher profits for helmet makers"], a: 0, why: "An externality affects third parties. Riders' longer lives are a private benefit and manufacturers' profits are not an externality." },
  { q: "[Calculation] In one year national income in money terms rose 3%, prices rose 4% and population rose 1%. What was the approximate change in real income per head? (May/June 2020 · 31 · Q23, reworded)", opts: ["−1%", "−2%", "+2%", "+3%"], a: 1, why: "3 − 4 − 1 = −2. Forgetting population gives −1%." },
  { q: "[Calculation] Employed 15m, unemployed 0.5m, not available for work 7m, working-age population 23m. What is the size of the labour force? (Oct/Nov 2021 · 32 · Q21, reworded)", opts: ["15m", "15.5m", "22m", "22.5m"], a: 1, why: "The labour force is the employed plus the unemployed. Those not available for work are outside it." },
  { q: "[Calculation] Total population 2,000,000; labour force 1,200,000; employed 900,000; unemployed 300,000. What is the unemployment rate? (Oct/Nov 2024 · 31 · Q20, reworded)", opts: ["25%", "33%", "60%", "75%"], a: 0, why: "300,000 ÷ 1,200,000 = 25%. 15% would come from dividing by total population." },
  { q: "[Combination] A multinational buys a manufacturing firm in a developing country that sells to local consumers, and then exports machinery and raw materials to it. What is the likely effect on the current account and the financial account? (May/June 2024 · 32 · Q28, reworded)", opts: ["Both improve", "Current improves; financial worsens", "Current worsens; financial improves", "Both worsen"], a: 2, why: "Imports of machinery worsen the current account; the purchase is a capital inflow. Decide each column separately." },
  { q: "[Combination] FDI trains workers (raising productivity) but profits are sent home. How do aggregate demand and aggregate supply shift? (Oct/Nov 2020 · 33 · Q21, reworded)", opts: ["AD left; AS left", "AD right; AS left", "AD left; AS right", "AD right; AS right"], a: 2, why: "Skills shift AS right; the profit outflow lowers domestic demand. Treat each curve on its own." },
  { q: "[Data] GDP and population: Bangladesh $206.7bn and 153.5m; India $2,989bn and 1,147.9m; Nigeria $292.7bn and 138.3m; South Africa $467.1bn and 43.8m. Which is likely to have the lowest standard of living? (May/June 2024 · 31 · Q28, reworded)", opts: ["Bangladesh", "India", "Nigeria", "South Africa"], a: 0, why: "GDP per head: about $1,350, $2,600, $2,100 and $10,700. India has the largest GDP but is not lowest per head." },
  { q: "[Data] The table gives birth rate, death rate, infant mortality and the share under 16: Singapore 12, 4, 5, 18%; Hong Kong 15, 6, 8, 20%; China 20, 9, 28, 38%. Which conclusion can be drawn? (May/June 2024 · 32 · Q29, reworded)", opts: ["China had the highest percentage of children who died in infancy", "People in Hong Kong lived the longest", "Singapore had the most people over 16", "Singapore's population was expected to fall"], a: 0, why: "Infant mortality of 28 per 1,000 is the highest. The other statements need data the table does not give." },
] });
