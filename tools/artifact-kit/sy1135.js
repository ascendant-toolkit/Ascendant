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

/* ---------- HDI ---------- */
const HV = [["Health index", 0.8, "f1", "Life expectancy 72 years"], ["Education index", 0.65, "f2", "Years of schooling"], ["Income index", 0.7, "f1", "GNI per head at PPP"]], HY = (v) => 290 - v * 230;
function hdiDraw(s) {
  let o = axes(70, 290, 730, 30, "", "Index (0 to 1)"); [0, 0.5, 1].forEach((v) => (o += SV.text(64, HY(v) + 4, v, "sm", { "text-anchor": "end" })));
  HV.forEach(([l, v, c, sub], i) => { const k = [s.a, s.b, s.c][i]; if (k > 0) o += SV.rect(120 + i * 140, HY(v * k), 90, 290 - HY(v * k), c, op(0.7)) + tag(165 + i * 140, HY(v * k) - 8, Lib.fmtN(v * k, 2), "t1", k, "middle") + tag(165 + i * 140, 312, l, "t1", k, "middle") + tag(165 + i * 140, 328, sub, "sm", k, "middle"); });
  if (s.d > 0) { const h = Math.cbrt(0.8 * 0.65 * 0.7); o += SV.rect(560, HY(h * s.d), 110, 290 - HY(h * s.d), "f3", op(0.8)) + tag(615, HY(h * s.d) - 8, "HDI " + Lib.fmtN(h * s.d, 2), "t4", s.d, "middle") + tag(615, 312, "Geometric mean", "t4", s.d, "middle") + tag(615, 328, "(cube root of the product)", "sm", s.d, "middle"); }
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 345" role="img" aria-label="Health, education and income indices of 0.80, 0.65 and 0.70 combined into an HDI of about 0.71">${hdiDraw({ a: 1, b: 1, c: 1, d: 1 })}</svg>`;
Lib.stepper($("#stH"), { w: 760, h: 345, label: "Building the HDI from the health, education and income indices", base: { a: 0, b: 0, c: 0, d: 0 }, draw: hdiDraw, tween: 1100, dwell: 5600, steps: [
  { cap: "<b>Health.</b> Life expectancy of 72 years sits between a minimum of 20 and a maximum of 85: index (72 − 20) ÷ 65 = 0.80.", s: { a: 1 } },
  { cap: "<b>Education.</b> Mean and expected years of schooling give an education index of 0.65.", s: { a: 1, b: 1 } },
  { cap: "<b>Income.</b> GNI per head at PPP, on a logarithmic scale between a floor and a ceiling, gives an income index of 0.70.", s: { a: 1, b: 1, c: 1 } },
  { cap: "<b>The HDI</b> is the geometric mean: (0.80 × 0.65 × 0.70)^(1/3) = 0.71. It is lower than the simple average of 0.72, because a weaker dimension counts for more.", s: { a: 1, b: 1, c: 1, d: 1 } },
] });

/* ---------- Kuznets ---------- */
const KX = (x) => 80 + x * 6.4, KY = (g) => 300 - (g - 0.28) * 1150, kg = (x) => 0.30 + 0.17 * Math.exp(-Math.pow((x - 40) / 28, 2));
function kuzDraw(s) {
  let o = axes(70, 290, 730, 30, "Income per head", "Inequality (Gini coefficient)"); [0.3, 0.4, 0.5].forEach((v) => (o += SV.text(64, KY(v) + 4, v.toFixed(1), "sm", { "text-anchor": "end" })));
  const pts = []; for (let x = 0; x <= Math.min(100, s.p); x += 1) pts.push([KX(x), KY(kg(x))]);
  if (pts.length > 1) o += SV.path(Lib.ptsPath(pts), "c1");
  if (s.p > 0) o += SV.circle(KX(Math.min(100, s.p)), KY(kg(Math.min(100, s.p))), 7, "dot4");
  if (s.l > 0) o += tag(KX(9), 314, "Farming: low inequality", "t1", s.l, "middle");
  if (s.l > 1) o += tag(KX(33), 314, "Industrialisation: rises", "t2", Math.min(1, s.l - 1), "middle");
  if (s.l > 2) o += SV.line(KX(40), KY(0.47), KX(40), 290, "c4 dash", op(Math.min(1, s.l - 2))) + tag(KX(40), KY(0.47) - 10, "turning point", "t4", Math.min(1, s.l - 2), "middle");
  if (s.l > 3) o += tag(KX(72), 314, "Mature economy: falls", "t3", Math.min(1, s.l - 3), "middle");
  return o;
}
$("#pic2").innerHTML = `<svg viewBox="0 0 760 340" role="img" aria-label="Kuznets curve: an inverted U relating inequality to income per head">${kuzDraw({ p: 100, l: 4 })}</svg>`;
Lib.stepper($("#stK"), { w: 760, h: 340, label: "The Kuznets curve: inequality rises, peaks and then falls as income per head grows", base: { p: 0, l: 0 }, draw: kuzDraw, tween: 1500, dwell: 5800, steps: [
  { cap: "<b>A farming economy.</b> Incomes are low and fairly similar, so inequality is low.", s: { p: 5, l: 1 } },
  { cap: "<b>Industrialisation.</b> Workers move to higher-paid jobs in cities and owners of capital and skilled workers gain first, so inequality rises.", s: { p: 28, l: 2 } },
  { cap: "<b>The turning point.</b> Once enough people are educated and urbanised, and governments tax and spend more, inequality peaks.", s: { p: 40, l: 3 } },
  { cap: "<b>A mature economy.</b> Wider education, progressive taxes and welfare reduce inequality. The curve is an inverted U, though real countries do not all follow it.", s: { p: 100, l: 4 } },
] });

/* ---------- Lab 1 ---------- */
function labH() {
  if (!$("#le") || !$("#sc") || !$("#gn")) return;
  const le = +$("#le").value, sc = +$("#sc").value, gn = Math.round(Math.pow(10, +$("#gn").value)), hI = Math.max(0, Math.min(1, (le - 20) / 65)), eI = Math.max(0, Math.min(1, sc / 15)), iI = Math.max(0, Math.min(1, (Math.log(gn) - Math.log(100)) / (Math.log(75000) - Math.log(100)))), h = Math.cbrt(hI * eI * iI), avg = (hI + eI + iI) / 3, grp = h >= 0.8 ? "Very high" : h >= 0.7 ? "High" : h >= 0.55 ? "Medium" : "Low";
  $("#r1").textContent = hI.toFixed(2) + " / " + eI.toFixed(2) + " / " + iI.toFixed(2); $("#r2").textContent = h.toFixed(3); $("#r3").textContent = grp;
  $("#rv").textContent = `Life expectancy ${le}, ${sc} years of schooling and GNI of $${gn.toLocaleString("en-US")} give indices of ${hI.toFixed(2)}, ${eI.toFixed(2)} and ${iI.toFixed(2)}. The geometric mean is ${h.toFixed(3)} (${grp.toLowerCase()} human development), compared with a simple average of ${avg.toFixed(3)}: ${avg - h > 0.005 ? "the weakest dimension drags the HDI below the average." : "the three dimensions are balanced, so the two are close."} (Simplified formula for teaching.)`;
  const Y = (v) => 270 - v * 240; let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(46, 16, "Index (0 to 1)", "sm");
  [["Health", hI, "f1"], ["Education", eI, "f2"], ["Income", iI, "f1"], ["HDI", h, "f3"]].forEach(([l, v, c], i) => { const x = 55 + i * 85; o += SV.rect(x, Y(v), 60, 270 - Y(v), c) + SV.text(x + 30, 290, l, "sm", { "text-anchor": "middle" }) + tag(x + 30, Y(v) - 6, v.toFixed(2), "t1", 1, "middle"); });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "le", label: "Life expectancy at birth (years) ", min: 40, max: 85, step: 1, value: 72, fmt: (v) => v, onInput: labH });
Lib.slider($("#g2"), { id: "sc", label: "Years of schooling ", min: 1, max: 15, step: 0.5, value: 9.8, fmt: (v) => v, onInput: labH });
Lib.slider($("#g3"), { id: "gn", label: "GNI per head at PPP (log scale) ", min: 2.5, max: 4.8, step: 0.02, value: 3.85, fmt: (v) => "$" + Math.round(Math.pow(10, v)).toLocaleString("en-US"), onInput: labH });
labH();

/* ---------- Lab 2 ---------- */
function labM() {
  if (!$("#mh") || !$("#ma")) return;
  const H = +$("#mh").value / 100, A = +$("#ma").value / 100, m = H * A;
  $("#t1").textContent = Lib.fmtN(H * 100, 0) + "%"; $("#t2").textContent = Lib.fmtN(A * 100, 0) + "%"; $("#t3").textContent = m.toFixed(3);
  $("#tv").textContent = `${Lib.fmtN(H * 100, 0)}% of people are poor, and on average they are deprived in ${Lib.fmtN(A * 100, 0)}% of the weighted indicators. MPI = ${H.toFixed(2)} × ${A.toFixed(2)} = ${m.toFixed(3)}. The MPI falls if fewer people are poor or if the poor become less deprived, so it can improve even when the headcount does not change.`;
  const Y = (v) => 270 - v * 240; let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(46, 16, "Share (0 to 1)", "sm");
  [["H", H, "f1"], ["A", A, "f2"], ["MPI", m, "f3"]].forEach(([l, v, c], i) => { const x = 60 + i * 110; o += SV.rect(x, Y(v), 70, 270 - Y(v), c) + SV.text(x + 35, 290, l, "sm", { "text-anchor": "middle" }) + tag(x + 35, Y(v) - 6, v.toFixed(2), "t1", 1, "middle"); });
  $("#labB").innerHTML = o;
}
Lib.slider($("#g4"), { id: "mh", label: "Headcount ratio H (% of people who are poor) ", min: 5, max: 90, step: 1, value: 30, fmt: (v) => v + "%", onInput: labM });
Lib.slider($("#g5"), { id: "ma", label: "Intensity A (average share of weighted indicators lacking) ", min: 33, max: 80, step: 1, value: 45, fmt: (v) => v + "%", onInput: labM });
labM();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Which measure does the description fit?", buckets: [{"label": "HDI"}, {"label": "MEW"}, {"label": "MPI"}], items: [{"text": "Combines life expectancy, years of schooling and income at PPP", "b": 0}, {"text": "Adds the value of leisure and unpaid work and deducts environmental damage", "b": 1}, {"text": "The headcount ratio multiplied by the intensity of deprivation", "b": 2}, {"text": "Uses a geometric mean of three indices", "b": 0}, {"text": "Starts with GDP and adjusts it for welfare", "b": 1}, {"text": "Counts deprivation in cooking fuel, sanitation and electricity", "b": 2}, {"text": "Published by the UN Development Programme each year as a ranking", "b": 0}, {"text": "A person is poor if deprived in about one third of weighted indicators", "b": 2}], done: "HDI: health, education, income. MEW: welfare-adjusted GDP. MPI: multidimensional poverty." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Human Development Index", "Composite of life expectancy, schooling and income per head"], ["Measure of Economic Welfare", "GDP adjusted for leisure, unpaid work and environmental costs"], ["Multidimensional Poverty Index", "Headcount ratio of the poor times the intensity of deprivation"], ["Kuznets curve", "Inverted U: inequality rises then falls as income per head grows"], ["Geometric mean", "The nth root of the product of n numbers"], ["Regrettable expenditure", "Spending that does not raise welfare, such as defence or commuting"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the stages of the Kuznets curve in order.", items: ["A farming economy with low inequality", "Industrialisation: some workers gain first, so inequality rises", "The turning point is reached", "Education, taxes and welfare spread gains", "Inequality falls in a mature economy"], done: "An inverted U." });
Lib.calc($("#c1"), { qs: [
  {"q": "Life expectancy is 70 years, the minimum is 20 and the maximum is 85. Calculate the health index (2 decimal places).", "a": 0.77, "unit": "", "tol": 0.01, "hint": "(70 − 20) ÷ 65.", "sol": "50 ÷ 65 = <b>0.77</b>."},
  {"q": "A country has health, education and income indices of 0.8, 0.5 and 0.4. Calculate the HDI as the geometric mean (2 decimal places).", "a": 0.54, "unit": "", "tol": 0.01, "hint": "Cube root of 0.8 × 0.5 × 0.4.", "sol": "0.16^(1/3) = <b>0.54</b>, compared with an average of 0.57."},
  {"q": "30% of a population are multidimensionally poor and they are deprived in 45% of the weighted indicators on average. Calculate the MPI (3 decimal places).", "a": 0.135, "unit": "", "tol": 0.002, "hint": "H × A.", "sol": "0.30 × 0.45 = <b>0.135</b>."},
  {"q": "A country's Gini coefficient was 0.36 and rises to 0.42. By how many percentage points (hundredths of a Gini point) has it risen?", "a": 6, "unit": "points", "tol": 0.1, "hint": "0.42 − 0.36 = 0.06.", "sol": "<b>6 points</b> (0.06). Inequality has risen: consistent with the early stage of the Kuznets curve."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "The HDI includes:", opts: ["Health, education and income", "Health and unemployment", "Education and inflation", "Income and crime"], a: 0, why: "Life expectancy, schooling and GNI per capita." },
  { q: "The MEW differs from GDP because it:", opts: ["Adjusts for leisure, unpaid work and environmental damage", "Ignores consumption", "Is a measure of inflation", "Counts only exports"], a: 0, why: "It is a welfare-adjusted measure." },
  { q: "The MPI is calculated as:", opts: ["H × A", "H + A", "H ÷ A", "H − A"], a: 0, why: "Headcount ratio times average intensity." },
  { q: "The Kuznets curve suggests that inequality:", opts: ["Rises and then falls as income per head grows", "Always falls", "Always rises", "Is unrelated to income"], a: 0, why: "An inverted U." },
  { q: "A weakness of the HDI is that it:", opts: ["Ignores income inequality in its basic form", "Includes pollution", "Has no income measure", "Is published only once"], a: 0, why: "The standard HDI uses averages." },
] });
Lib.cards($("#fc1"), { cards: [
  ["HDI", "Life expectancy, schooling, income; geometric mean."],
  ["HDI groups", "Very high, high, medium, low."],
  ["MEW", "GDP + leisure and unpaid work − environmental damage."],
  ["MPI", "H × A; ten indicators in three dimensions."],
  ["Kuznets curve", "Inverted U: inequality up, then down."],
  ["Turning point", "Where inequality peaks."],
  ["Limits of HDI", "Equal weights, no inequality or environment."],
  ["Limits of MEW", "Subjective values; little data."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "What is not included in the Human Development Index? (Oct/Nov 2020 · 31 · Q18, reworded)", opts: ["Infant mortality rates", "Gross national income per capita", "Life expectancy at birth", "Mean years of schooling"], a: 0, why: "The HDI has life expectancy, schooling and income. Infant mortality is a health indicator but is not one of the three components." },
  { q: "Which measurement is not included in the calculation of the HDI? (May/June 2025 · 31 · Q26, reworded)", opts: ["Average years of schooling", "GNI per capita", "Infant mortality rate", "Life expectancy at birth"], a: 2, why: "The three dimensions use schooling, GNI per capita and life expectancy." },
  { q: "The HDI is often argued to be a better indicator of development than income per capita because it adjusts for: (Oct/Nov 2024 · 31 · Q27, reworded)", opts: ["Average hours worked", "Environmental pollution", "Inequality in income distribution", "Life expectancy at birth"], a: 3, why: "The HDI adds health (life expectancy) and education to income. The standard HDI does not adjust for pollution or inequality." },
  { q: "The MEW is regarded as a better measure of economic welfare than GDP per head. What is additionally included in the calculation of MEW? (May/June 2021 · 31 · Q20, reworded)", opts: ["The cost of paid work", "The cost of producing armaments", "The estimated cost of damage to the environment", "The negative effect of the shadow economy"], a: 2, why: "The MEW deducts environmental damage, and adds leisure and unpaid work." },
  { q: "Which adjustments are made to GDP to calculate the MEW? (Oct/Nov 2023 · 31 · Q27, reworded)", opts: ["Value of leisure only", "Value of unpaid work only", "Leisure and unpaid work only", "Leisure, unpaid work and the cost of environmental damage"], a: 3, why: "All three adjustments are made: add leisure and unpaid work, deduct environmental costs." },
  { q: "What is not included as a weighted indicator of poverty in the Multidimensional Poverty Index? (Feb/March 2025 · 32 · Q28, reworded)", opts: ["Cooking fuel", "Electricity", "Medication", "Water"], a: 2, why: "The MPI uses nutrition, child mortality, schooling, attendance, cooking fuel, sanitation, drinking water, electricity, housing and assets." },
  { q: "What is shown by the Kuznets curve? (May/June 2022 · 31 · Q20, reworded)", opts: ["A rise then fall in a trade deficit after a devaluation", "A rise then fall in the growth rate as GDP rises", "A rise then fall in inequality as income per head rises", "A rise then fall in tax revenue as the tax rate rises"], a: 2, why: "The Kuznets curve is an inverted U relating inequality to income per head." },
  { q: "The turning point on the Kuznets curve has been estimated at about $10,500 of GDP per head. For a country with GDP per head of $8,000, what is most likely? (Oct/Nov 2023 · 31 · Q30, reworded)", opts: ["A fall in GDP per head would have no effect on inequality", "A fall in GDP per head would increase inequality", "A rise in GDP per head would have no effect on inequality", "A rise in GDP per head would increase inequality"], a: 3, why: "The country is on the rising part of the curve, below the turning point, so further growth would be expected to raise inequality." },
  { q: "During a period a country with a constant population expands its output per head but also suffers more river and air pollution. In the absence of other changes, which measure would show a fall in living standards? (May/June 2024 · 32 · Q30, reworded)", opts: ["GDP per head", "GNP per head", "HDI", "MEW"], a: 3, why: "Only the MEW deducts environmental damage." },
  { q: "Why do economists distinguish between economic growth and economic development? (Oct/Nov 2021 · 31 · Q29, reworded)", opts: ["A country's development depends on its output level, not its growth rate", "Allocation of resources, not their level, decides well-being", "Concern about quality of life rather than quantity of output", "Investment, not consumption, drives development"], a: 2, why: "Development is about improvements in quality of life as well as output." },
] });
