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

/* ---------- Income groups ---------- */
const LX = (g) => 90 + (Math.log10(g) - Math.log10(300)) / (Math.log10(60000) - Math.log10(300)) * 620, TH = [1200, 4500, 14000], GN = ["Low income", "Lower-middle", "Upper-middle", "High income"], GC = ["f2", "f1", "f1", "f3"];
function incDraw(s) {
  let o = SV.line(90, 210, 710, 210) + SV.text(710, 254, "GNI per capita ($, log scale)", "sm", { "text-anchor": "end" });
  const edges = [300, ...TH, 60000]; [300, 1200, 4500, 14000, 60000].forEach((g) => (o += SV.line(LX(g), 205, LX(g), 215) + SV.text(LX(g), 232, "$" + g.toLocaleString("en-US"), "sm", { "text-anchor": "middle" })));
  for (let i = 0; i < 4; i++) { const k = Math.max(0, Math.min(1, s.z - i)); if (k > 0) o += SV.rect(LX(edges[i]), 150, LX(edges[i + 1]) - LX(edges[i]), 55, GC[i], op(0.25 + 0.5 * k * (i % 2 ? 0.7 : 1))) + tag((LX(edges[i]) + LX(edges[i + 1])) / 2, 182, GN[i], "t1", k, "middle"); }
  if (s.m > 0) { const g = s.p, x = LX(g); o += SV.circle(x, 140, 8, "dot4", op(s.m)) + SV.line(x, 148, x, 150, "c4", op(s.m)) + tag(x, 120, "$" + Lib.fmtN(g, 0), "t4", s.m, "middle") + tag(x, 104, "a country on the move", "t4", s.m, "middle"); }
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 260" role="img" aria-label="Income groups on a logarithmic scale of GNI per capita">${incDraw({ z: 4, p: 3000, m: 0 })}</svg>`;
Lib.stepper($("#stI"), { w: 760, h: 260, label: "The four World Bank income groups on a log scale and a country moving between groups", base: { z: 0, p: 3000, m: 0 }, draw: incDraw, tween: 1100, dwell: 5600, steps: [
  { cap: "<b>Low income:</b> GNI per capita below about $1,200. Many people rely on subsistence farming and basic services are limited.", s: { z: 1 } },
  { cap: "<b>Lower-middle income:</b> roughly $1,200 to $4,500. Manufacturing and urban jobs start to grow, but much work is informal.", s: { z: 2 } },
  { cap: "<b>Upper-middle income:</b> roughly $4,500 to $14,000. Industry and services are larger, and schooling and health are better.", s: { z: 3 } },
  { cap: "<b>High income:</b> above roughly $14,000. A large services sector, high productivity and wide access to health and education.", s: { z: 4 } },
  { cap: "<b>A lower-middle income country</b> has GNI per capita of $3,000.", s: { z: 4, p: 3000, m: 1 } },
  { cap: "<b>Moving up.</b> At 4% growth a year it passes the $4,500 line in about 10 years and moves from the lower-middle to the upper-middle group.", s: { z: 4, p: 4900, m: 1 } },
] });

/* ---------- What changes ---------- */
const CHG = [["Life expectancy (years)", [62, 68, 74, 80], 90, "f1"], ["Workers in agriculture (%)", [60, 40, 20, 3], 100, "f2"], ["Births per 1,000 people", [35, 25, 15, 11], 50, "f3"]];
function chgDraw(s) {
  let o = SV.line(70, 250, 730, 250) + SV.line(70, 250, 70, 30);
  CHG.forEach((c, k) => { const p = Math.max(0, Math.min(1, s.i - k)); if (p <= 0) return; const [name, vals, mx, cls] = c; o += SV.text(70 + k * 220 + 70, 24 - 0, name, "lbl bd", { "text-anchor": "middle", ...op(p) }); vals.forEach((v, i) => { const h = v / mx * 180 * p, x = 80 + k * 220 + i * 46; o += SV.rect(x, 250 - h, 34, h, cls, op(0.35 + 0.18 * i)) + SV.text(x + 17, 244 - h, v, "sm", { "text-anchor": "middle", ...op(p) }) + SV.text(x + 17, 266, ["L", "LM", "UM", "H"][i], "sm", { "text-anchor": "middle" }); }); });
  return o + SV.text(730, 290, "L low, LM lower-middle, UM upper-middle, H high income (typical values, for illustration)", "sm", { "text-anchor": "end" });
}
Lib.stepper($("#stC"), { w: 760, h: 300, label: "Typical life expectancy, share of workers in agriculture and birth rate across the four income groups", base: { i: 0 }, draw: chgDraw, tween: 1100, dwell: 5600, steps: [
  { cap: "<b>Life expectancy</b> rises with income: better health care, nutrition and sanitation. This is a development gain beyond income itself.", s: { i: 1 } },
  { cap: "<b>The share of workers in agriculture</b> falls sharply: labour moves from low-productivity farming to industry and services (structural change).", s: { i: 2 } },
  { cap: "<b>The birth rate</b> falls as incomes, education and health improve, so the dependency ratio falls and more can be saved and invested.", s: { i: 3 } },
] });

/* ---------- Lab 1 ---------- */
function labI() {
  if (!$("#gn")) return;
  const g = Math.round(Math.pow(10, +$("#gn").value)), k = g < 1200 ? 0 : g < 4500 ? 1 : g < 14000 ? 2 : 3, feat = ["Mostly primary sector; low productivity; high birth rate", "Growing industry and cities; large informal sector", "Larger industry and services; better health and schooling", "Large tertiary sector; high productivity; ageing population"];
  $("#r1").textContent = "$" + g.toLocaleString("en-US"); $("#r2").textContent = GN[k]; $("#r3").textContent = ["Early", "Developing", "Emerging", "Developed"][k];
  $("#rv").textContent = `${GN[k]} (roughly): ${feat[k]}. This is only a typical pattern: income per head is an average, and countries with the same income can differ in health, education and inequality.`;
  $("#labA").innerHTML = (() => { const X = (v) => 30 + (Math.log10(v) - Math.log10(300)) / (Math.log10(60000) - Math.log10(300)) * 360; let o = SV.line(30, 160, 390, 160) + SV.text(390, 196, "GNI per capita ($, log scale)", "sm", { "text-anchor": "end" }); const e = [300, 1200, 4500, 14000, 60000]; for (let i = 0; i < 4; i++) o += SV.rect(X(e[i]), 110, X(e[i + 1]) - X(e[i]), 50, GC[i], op(i === k ? 0.85 : 0.25)) + SV.text((X(e[i]) + X(e[i + 1])) / 2, 140, ["Low", "Lower-mid", "Upper-mid", "High"][i], "sm", { "text-anchor": "middle" }); o += SV.circle(X(g), 98, 8, "dot4") + tag(X(g), 80, "$" + g.toLocaleString("en-US"), "t4", 1, "middle"); return o; })();
}
Lib.slider($("#g1"), { id: "gn", label: "GNI per capita (log scale) ", min: 2.5, max: 4.7, step: 0.02, value: 3.5, fmt: (v) => "$" + Math.round(Math.pow(10, v)).toLocaleString("en-US"), onInput: labI });
labI();

/* ---------- Lab 2 ---------- */
function labG() {
  if (!$("#gr")) return;
  const r = +$("#gr").value / 10 / 100, yrs = (t) => Math.log(t / 3000) / Math.log(1 + r), y45 = yrs(4500), y14 = yrs(14000), g20 = 3000 * Math.pow(1 + r, 20);
  $("#t1").textContent = Lib.fmtN(y45, 1); $("#t2").textContent = Lib.fmtN(y14, 1); $("#t3").textContent = "$" + Math.round(g20).toLocaleString("en-US");
  $("#tv").textContent = `At ${Lib.fmtN(r * 100, 1)}% a year, GNI per capita passes $4,500 after about ${Lib.fmtN(y45, 0)} years and $14,000 after about ${Lib.fmtN(y14, 0)} years. Lasting growth of a few percent a year takes decades to change a country's income group.`;
  const X = (t) => 40 + t * 7, Y = (v) => 270 - (v / 20000) * 240; let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(400, 292, "Years", "sm", { "text-anchor": "end" }) + SV.text(46, 16, "GNI per capita ($)", "sm");
  [4500, 14000].forEach((th) => (o += SV.line(40, Y(th), 400, Y(th), "c4 dash", op(0.6)) + SV.text(44, Y(th) - 4, "$" + th.toLocaleString("en-US"), "sm")));
  const pts = []; for (let t = 0; t <= 50; t += 1) pts.push([X(t), Math.max(20, Y(3000 * Math.pow(1 + r, t)))]);
  $("#labB").innerHTML = o + SV.path(Lib.ptsPath(pts), "c1");
}
Lib.slider($("#g2"), { id: "gr", label: "Growth rate of GNI per capita, % a year × 10 ", min: 10, max: 80, step: 5, value: 40, fmt: (v) => (v / 10).toFixed(1) + "%", onInput: labG });
labG();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Which type of economy does the description fit best?", buckets: [{"label": "Developed"}, {"label": "Emerging"}, {"label": "Developing"}], items: [{"text": "A very large tertiary sector and low birth and death rates", "b": 0}, {"text": "Fast growth, rapid urbanisation and rising manufacturing exports", "b": 1}, {"text": "Most workers in low-productivity farming and a high dependency ratio", "b": 2}, {"text": "An ageing population and high productivity", "b": 0}, {"text": "Moving workers from agriculture into factories at speed", "b": 1}, {"text": "Heavy reliance on exporting a few primary products", "b": 2}, {"text": "Wide access to health care and long life expectancy", "b": 0}, {"text": "Rising incomes but still large informal sector", "b": 1}], done: "Developed: high income and services. Emerging: fast structural change. Developing: low income and primary reliance." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["GNI per capita", "A country's total income from residents divided by its population"], ["Low-income country", "Below about $1,200 GNI per capita in the World Bank classification"], ["Emerging economy", "A fast-growing economy shifting from agriculture to industry"], ["Economic development", "Improvements in living standards, health, education and choice"], ["Dependency ratio", "Dependants (young and old) per person of working age"], ["HDI", "A composite of income, health and education"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the World Bank income groups in order, lowest income first.", items: ["Low income", "Lower-middle income", "Upper-middle income", "High income"], done: "Thresholds are roughly $1,200, $4,500 and $14,000 of GNI per capita." });
Lib.calc($("#c1"), { qs: [
  {"q": "A country has GNI of $60bn and a population of 15 million. Calculate GNI per capita ($).", "a": 4000, "unit": "$", "tol": 0.5, "hint": "60bn ÷ 15m.", "sol": "60,000m ÷ 15m = <b>$4,000</b>: lower-middle income."},
  {"q": "GNI per capita rises from $3,000 to $3,150 in a year. Calculate the percentage growth (%).", "a": 5, "unit": "%", "tol": 0.05, "hint": "150 ÷ 3000.", "sol": "<b>5%</b>."},
  {"q": "A country has 4 dependants for every 10 people of working age. Calculate the dependency ratio as a percentage (%).", "a": 40, "unit": "%", "tol": 0.5, "hint": "4 ÷ 10.", "sol": "<b>40%</b>."},
  {"q": "Using a growth rate of 5% a year, by about how many years would $3,000 double? (Rule of 70, years)", "a": 14, "unit": "years", "tol": 0.5, "hint": "70 ÷ 5.", "sol": "70 ÷ 5 = <b>14 years</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which is used to classify countries into low, lower-middle, upper-middle and high income?", opts: ["GNI per capita", "The HDI only", "Population", "The Gini coefficient"], a: 0, why: "The World Bank uses GNI per capita." },
  { q: "A country has grown fast but most people have not seen better health or schooling. This shows:", opts: ["Growth without development", "Development without growth", "Neither", "Both"], a: 0, why: "Output rose but well-being did not improve widely." },
  { q: "A typical developing economy has:", opts: ["A large primary sector", "A very small dependency ratio", "The highest life expectancy", "A very large tertiary sector"], a: 0, why: "Many workers are in farming and primary activities." },
  { q: "An advantage of classifying by GNI per capita is that:", opts: ["It is easy to measure and compare", "It measures well-being fully", "It shows income distribution", "It includes health and education"], a: 0, why: "It is a simple, widely available statistic." },
  { q: "Which statement is true of income groups?", opts: ["Countries can move between them as incomes change", "The thresholds never change", "They show equality", "They include education"], a: 0, why: "Bangladesh moved up from low to lower-middle income, for example." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Developed", "High income, large services sector, high life expectancy."],
  ["Emerging", "Fast growth and structural change."],
  ["Developing", "Lower income, primary reliance, high dependency."],
  ["LDC", "Least developed country on the UN list."],
  ["GNI per capita", "Income of residents ÷ population."],
  ["Income groups", "Low, lower-middle, upper-middle, high."],
  ["Growth vs development", "Output rises vs lives improve."],
  ["Limit of income groups", "An average that hides inequality and well-being."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "The table shows data for four countries in 2015: GDP, HDI and population. Which country is most likely to be classed as developed? A: GDP $10.9 trillion, HDI 0.727, population 1.37 billion. B: $2.4 trillion, 0.897, 66.8 million. C: $481 billion, 0.527, 182.2 million. D: $19 billion, 0.516, 15.6 million. (Feb/March 2020 · 32 · Q22, reworded)", opts: ["A", "B", "C", "D"], a: 1, why: "B has the highest HDI (0.897) and a high GDP per head (GDP divided by a small population). A has the biggest GDP but a lower HDI and a huge population." },
  { q: "What is likely to happen in a developing country as it becomes more developed? (Feb/March 2024 · 32 · Q30, reworded)", opts: ["A lower percentage of people will go to university", "Average life expectancy will rise", "The rate of population growth will increase", "The tertiary sector will decline in importance"], a: 1, why: "Better health care and nutrition raise life expectancy. Population growth usually slows and the tertiary sector grows." },
  { q: "Which combination of characteristics is usually associated with a low-income country? (May/June 2025 · 34 · Q28, reworded)", opts: ["High death rate and low levels of productivity", "High GDP and low infant mortality", "Low birth rate and a large share of income from primary industries", "Low capital exports and a large tertiary sector"], a: 0, why: "Low incomes go with weaker health (higher death rates) and low productivity. The others describe richer or inconsistent economies." },
  { q: "Which row correctly identifies the characteristics of a low-income economy? Dependence on the primary sector, Gini coefficient and real income per capita. (Oct/Nov 2023 · 33 · Q27, reworded)", opts: ["High, high, high", "High, high, low", "High, low, low", "Low, high, low"], a: 1, why: "Low-income economies rely on primary products, have unequal income distribution (high Gini) and low real income per head." },
  { q: "The table shows the percentage of employment in the primary, secondary and tertiary sectors in four countries. Which is most likely a high-income country? A: 15, 40, 45. B: 30, 40, 30. C: 35, 45, 20. D: 45, 35, 20. (Oct/Nov 2024 · 33 · Q30, reworded)", opts: ["A", "B", "C", "D"], a: 0, why: "High-income countries have the largest tertiary sector and smallest primary sector. A has 45% in services and only 15% in the primary sector." },
  { q: "Which indicator is least likely to be used when comparing the economic development of countries? (Feb/March 2022 · 32 · Q21, reworded)", opts: ["Adult literacy rate", "Life expectancy at birth", "Real GNP per head", "Size of population"], a: 3, why: "Literacy, life expectancy and income per head show well-being. Total population does not." },
] });
