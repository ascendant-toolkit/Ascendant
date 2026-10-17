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

/* ---------- Demographic transition ---------- */
const sm = (x) => { const k = Math.max(0, Math.min(1, x)); return k * k * (3 - 2 * k); }, bR = (t) => 40 - 28 * sm((t - 42) / 43), dR = (t) => 36 - 26 * sm((t - 12) / 33) + 1.5 * sm((t - 80) / 20);
const DX = (t) => 80 + t * 6.4, DY = (r) => 300 - r * 6.4;
function dtDraw(s) {
  let o = axes(70, 300, 730, 30, "Time as the economy develops", "Rate per 1,000 people"); [0, 10, 20, 30, 40].forEach((v) => (o += SV.text(64, DY(v) + 4, v, "sm", { "text-anchor": "end" })));
  const n = Math.min(100, s.p), bp = [], dp = []; for (let t = 0; t <= n; t += 2) { bp.push([DX(t), DY(bR(t))]); dp.push([DX(t), DY(dR(t))]); }
  if (bp.length > 1) { o += SV.poly([...bp, ...dp.slice().reverse()], "f1", op(0.28)) + SV.path(Lib.ptsPath(bp), "c2") + SV.path(Lib.ptsPath(dp), "c1"); }
  o += tag(DX(30), DY(40) - 8, "Birth rate", "t2", s.p > 0 ? 1 : 0, "middle") + tag(DX(60), DY(10) + 22, "Death rate", "t1", s.p > 0 ? 1 : 0, "middle");
  const stg = [["Stage 1: both rates high, stable population"], ["Stage 2: deaths fall, population surges"], ["Stage 3: births fall, growth slows"], ["Stage 4: both low, ageing population"]][n < 22 ? 0 : n < 52 ? 1 : n < 82 ? 2 : 3];
  if (s.p > 0) o += tag(400, 334, stg[0], "t4", 1, "middle");
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 345" role="img" aria-label="Demographic transition: death rate falls first, then birth rate, leaving a gap of natural increase that widens then narrows">${dtDraw({ p: 100 })}</svg>`;
Lib.stepper($("#stD"), { w: 760, h: 345, label: "Demographic transition: birth and death rate over time, with the gap showing natural increase", base: { p: 0 }, draw: dtDraw, tween: 1600, dwell: 5800, steps: [
  { cap: "<b>Stage 1.</b> Birth and death rates are both high (about 40 and 36 per 1,000). The population is almost stable, with a young age structure.", s: { p: 10 } },
  { cap: "<b>Stage 2.</b> Better food, clean water and medicine cut the death rate, but the birth rate stays high. The gap (natural increase) widens and the population rises rapidly.", s: { p: 35 } },
  { cap: "<b>Stage 3.</b> Rising incomes, education, urbanisation and contraception pull the birth rate down. The gap narrows, so growth slows and the dependency ratio falls (the demographic dividend).", s: { p: 70 } },
  { cap: "<b>Stage 4.</b> Both rates are low. The population is stable or falling and ageing, so the old-age dependency ratio rises.", s: { p: 100 } },
] });

/* ---------- Optimum population ---------- */
const OX = (p) => 80 + p * 6.4, OY = (y) => 300 - y * 2.4;
const opt = (tt) => 50 + 15 * tt, hgt = (tt) => 70 + 30 * tt, oy = (p, tt) => Math.max(0, hgt(tt) * (1 - Math.pow((p - opt(tt)) / 72, 2)));
function optDraw(s) {
  let o = axes(70, 300, 730, 30, "Population", "Output per head");
  const pts0 = [], pts1 = []; for (let p = 0; p <= 100; p += 2) { pts0.push([OX(p), OY(oy(p, 0))]); pts1.push([OX(p), OY(oy(p, s.t))]); }
  if (s.t > 0) o += SV.path(Lib.ptsPath(pts0), "c3 dash", op(0.4));
  o += SV.path(Lib.ptsPath(pts1), "c1");
  const po = opt(s.t); o += SV.line(OX(po), OY(oy(po, s.t)), OX(po), 300, "c4 dash") + SV.circle(OX(po), OY(oy(po, s.t)), 7, "dot4") + tag(OX(po), 322, "optimum", "t4", 1, "middle");
  if (s.m > 0) { const p = s.m, y = oy(p, s.t); o += SV.circle(OX(p), OY(y), 7, "dot2") + tag(OX(p) + (p < po ? 12 : -12), OY(y) - 12, p < po ? "under-populated" : "over-populated", "t2", 1, p < po ? "start" : "end"); }
  return o;
}
$("#pic2").innerHTML = `<svg viewBox="0 0 760 345" role="img" aria-label="Output per head against population: an inverted U with the optimum at the peak">${optDraw({ t: 0, m: 0 })}</svg>`;
Lib.stepper($("#stO"), { w: 760, h: 345, label: "Output per head against population: the optimum, under- and over-population and the effect of technology", base: { t: 0, m: 0 }, draw: optDraw, tween: 1300, dwell: 5800, steps: [
  { cap: "<b>The curve.</b> With given resources, capital and technology, output per head first rises as more workers allow specialisation and then falls as diminishing returns set in.", s: { t: 0, m: 0 } },
  { cap: "<b>Optimum population.</b> The peak of the curve is the population that maximises output (income) per head.", s: { t: 0, m: 0 } },
  { cap: "<b>Under-population.</b> At a smaller population, resources are not fully used and a larger population would raise output per head.", s: { t: 0, m: 22 } },
  { cap: "<b>Over-population.</b> Beyond the peak, extra people share the same resources, so output per head falls.", s: { t: 0, m: 88 } },
  { cap: "<b>New technology or capital</b> shifts the curve up and to the right: the optimum is higher and a larger population can now be supported.", s: { t: 1, m: 88 } },
] });

/* ---------- Lab 1 ---------- */
function labP() {
  if (!$("#br") || !$("#dr") || !$("#nm")) return;
  const b = +$("#br").value, d = +$("#dr").value, m = +$("#nm").value, ni = b - d, gr = (ni + m) / 10;
  $("#r1").textContent = ni + " per 1,000"; $("#r2").textContent = (gr >= 0 ? "+" : "") + Lib.fmtN(gr, 1) + "% a year"; $("#r3").textContent = gr > 0.05 ? Lib.fmtN(70 / gr, 0) + " yrs" : "none";
  $("#rv").textContent = `Natural increase is ${b} − ${d} = ${ni} per 1,000. Adding net migration of ${m} gives ${ni + m} per 1,000, a growth rate of ${Lib.fmtN(gr, 1)}% a year. ${gr > 0.05 ? "The population doubles in roughly " + Lib.fmtN(70 / gr, 0) + " years (rule of 70)." : gr < -0.05 ? "The population is shrinking." : "The population is roughly stable."}`;
  const Y = (v) => 150 - v * 3.2; let o = SV.line(40, 150, 400, 150) + SV.line(40, 20, 40, 280) + SV.text(46, 16, "per 1,000 people", "sm");
  [["Births", b, "f2"], ["Deaths", -d, "f1"], ["Net migration", m, "f1"], ["Growth", ni + m, "f3"]].forEach(([l, v, c], i) => { const x = 55 + i * 85, y = Y(Math.max(-40, Math.min(40, v))); o += SV.rect(x, Math.min(y, 150), 60, Math.abs(y - 150), c) + SV.text(x + 30, 296, l, "sm", { "text-anchor": "middle" }) + tag(x + 30, v >= 0 ? y - 6 : y + 16, Math.abs(v) + (v < 0 && l === "Deaths" ? "" : ""), "t1", 1, "middle"); });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "br", label: "Birth rate per 1,000 ", min: 8, max: 45, step: 1, value: 30, fmt: (v) => v, onInput: labP });
Lib.slider($("#g2"), { id: "dr", label: "Death rate per 1,000 ", min: 4, max: 30, step: 1, value: 10, fmt: (v) => v, onInput: labP });
Lib.slider($("#g3"), { id: "nm", label: "Net migration per 1,000 ", min: -10, max: 15, step: 1, value: -2, fmt: (v) => v, onInput: labP });
labP();

/* ---------- Lab 2 ---------- */
function labD() {
  if (!$("#yg") || !$("#og")) return;
  let y = +$("#yg").value, o2 = +$("#og").value; if (y + o2 > 95) o2 = 95 - y; const w = 100 - y - o2, dep = (y + o2) / w * 100;
  $("#t1").textContent = w + "%"; $("#t2").textContent = Lib.fmtN(dep, 0); $("#t3").textContent = y >= 30 ? "Youthful" : o2 >= 15 ? "Ageing" : "Mature";
  $("#tv").textContent = `${y}% are under 15 and ${o2}% are over 64, so ${w}% are of working age. The dependency ratio is (${y} + ${o2}) ÷ ${w} × 100 = ${Lib.fmtN(dep, 0)}: each 100 workers support about ${Lib.fmtN(dep, 0)} dependants. ${y >= 30 ? "A young structure like this is typical of a developing economy: spending on children and education competes with investment." : o2 >= 15 ? "An ageing structure like this is typical of a developed economy: pensions and health care raise costs while the workforce shrinks." : "A mature structure with moderate numbers of both groups."}`;
  const X = (v) => 40 + v * 3.4; let o = SV.line(40, 200, 400, 200) + SV.text(40, 20, "Share of population (%)", "sm");
  [["Under 15", y, "f2"], ["15 to 64", w, "f1"], ["Over 64", o2, "f3"]].forEach(([l, v, c], i, arr) => { const x0 = arr.slice(0, i).reduce((a, q) => a + q[1], 0); o += SV.rect(X(x0), 120, v * 3.4, 80, c, op(0.7)) + SV.text(X(x0 + v / 2), 164, v + "%", "lbl bd", { "text-anchor": "middle" }) + SV.text(X(x0 + v / 2), 220 + (i % 2) * 18, l, "sm", { "text-anchor": "middle" }); });
  $("#labB").innerHTML = o;
}
Lib.slider($("#g4"), { id: "yg", label: "Under 15 (% of population) ", min: 10, max: 50, step: 1, value: 35, fmt: (v) => v + "%", onInput: labD });
Lib.slider($("#g5"), { id: "og", label: "Over 64 (% of population) ", min: 2, max: 30, step: 1, value: 5, fmt: (v) => v + "%", onInput: labD });
labD();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Does it tend to raise or lower the birth rate?", buckets: [{"label": "Raise"}, {"label": "Lower"}], items: [{"text": "Children are needed to work on the family farm", "b": 0}, {"text": "More girls complete secondary education", "b": 1}, {"text": "Wider access to contraception", "b": 1}, {"text": "High infant mortality", "b": 0}, {"text": "Introduction of pensions for old age", "b": 1}, {"text": "Rapid urbanisation, where housing costs are high", "b": 1}, {"text": "A cultural preference for large families", "b": 0}, {"text": "Higher incomes and better jobs for women", "b": 1}], done: "Education, contraception, pensions and urban living lower the birth rate. Farm labour needs and high infant mortality raise it." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Natural increase", "Birth rate minus death rate"], ["Dependency ratio", "Under 15s plus over 64s as a percentage of those aged 15 to 64"], ["Optimum population", "The size that gives the highest income per head"], ["Infant mortality rate", "Deaths of babies under one year per 1,000 live births"], ["Net migration", "Immigration minus emigration"], ["Urbanisation", "The rising share of people living in cities"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the stages of the demographic transition in order.", items: ["Both birth and death rates are high; population is stable", "The death rate falls; population grows quickly", "The birth rate falls; growth slows", "Both rates are low; population ageing"], done: "Death rates fall before birth rates." });
Lib.calc($("#c1"), { qs: [
  {"q": "The birth rate is 30 per 1,000 and the death rate is 10 per 1,000. Net migration is −2 per 1,000. Calculate the population growth rate (% a year).", "a": 1.8, "unit": "%", "tol": 0.05, "hint": "(30 − 10 − 2) ÷ 10.", "sol": "18 per 1,000 = <b>1.8%</b>."},
  {"q": "35% of a population are under 15 and 5% are over 64. Calculate the dependency ratio (1 decimal place).", "a": 66.7, "unit": "", "tol": 0.1, "hint": "(35 + 5) ÷ 60 × 100.", "sol": "40 ÷ 60 × 100 = <b>66.7</b>."},
  {"q": "There were 280 infant deaths among 10,000 live births. Calculate the infant mortality rate per 1,000 live births.", "a": 28, "unit": "per 1,000", "tol": 0.5, "hint": "280 ÷ 10,000 × 1,000.", "sol": "<b>28 per 1,000</b>."},
  {"q": "A country has 150 million people and 45 million of them live in cities. Calculate the urbanisation rate (%).", "a": 30, "unit": "%", "tol": 0.5, "hint": "45 ÷ 150.", "sol": "<b>30%</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "The dependency ratio is the number of:", opts: ["Under 15s and over 64s per 100 people aged 15 to 64", "Workers per 100 people", "Unemployed per 100 workers", "Births per 1,000 people"], a: 0, why: "It shows how many dependants each 100 workers support." },
  { q: "Which would raise the optimum population?", opts: ["Better technology", "A higher birth rate", "A fall in capital", "More emigration"], a: 0, why: "Technology raises output per head at every population size." },
  { q: "A typical developing economy has:", opts: ["A high birth rate and a high dependency ratio", "An ageing population", "A very high life expectancy", "Falling urbanisation"], a: 0, why: "Large numbers of children raise the dependency ratio." },
  { q: "Net migration is equal to:", opts: ["Immigration minus emigration", "Births minus deaths", "Emigration plus deaths", "Immigration plus births"], a: 0, why: "It is the net inflow of people." },
  { q: "Which is a cost of rapid urbanisation?", opts: ["Pressure on housing, water and transport", "Smaller markets", "Lower productivity everywhere", "Higher birth rates"], a: 0, why: "Cities can be overwhelmed by rapid inflows." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Natural increase", "Birth rate − death rate."],
  ["Net migration", "Immigrants − emigrants."],
  ["Dependency ratio", "(Under 15 + over 64) ÷ (15 to 64) × 100."],
  ["Demographic dividend", "A large working-age group with fewer dependants."],
  ["Optimum population", "Maximises income per head."],
  ["Under-population", "Too few people to use resources fully."],
  ["Over-population", "Diminishing returns reduce output per head."],
  ["Urbanisation", "Rising share of people in cities."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "What is least likely to lead to an increase in the optimum population? (Feb/March 2025 · 32 · Q27, reworded)", opts: ["An improvement in labour productivity", "An improvement in the quality of capital and technology", "An increase in the birth rate and a fall in the death rate", "An increase in the availability of natural resources"], a: 2, why: "The optimum depends on productivity, capital, technology and resources. A higher birth rate or lower death rate changes the actual population, not the optimum." },
  { q: "What will increase the size of a country's optimum population? (May/June 2024 · 31 · Q29, reworded)", opts: ["A rise in the birth rate", "A lower retirement age", "A rise in the stock of capital", "A fall in productivity in industry"], a: 2, why: "More capital raises output per head at each population size, so the optimum moves to the right." },
  { q: "The optimum population is the level at which real output per head is highest. The diagram shows output per head against population for two years, with the curve shifting up and to the right in year 2. Which change could not satisfactorily explain the shift? (Oct/Nov 2024 · 33 · Q25, reworded)", opts: ["Population has increased", "The state of technology has improved", "The stock of capital has increased", "The volume of productive resources in use has increased"], a: 0, why: "A larger actual population is a movement along a curve, not a shift of the curve. Technology, capital and resources shift it." },
  { q: "In some countries life expectancy has fallen but the birth rate remains high. Which effect will this have? (May/June 2022 · 32 · Q28, reworded)", opts: ["Fewer schools will be needed", "More facilities will be needed for older people", "The population will age", "The working population will tend to become a smaller share of the total"], a: 3, why: "With a high birth rate and early deaths, the young make up a larger share and the working-age group a smaller one." },
  { q: "The table gives birth rate, death rate and infant mortality per 1,000, and the share under 16, for Singapore (12, 4, 5, 18%), Hong Kong (15, 6, 8, 20%) and China (20, 9, 28, 38%). Which conclusion can be drawn? (May/June 2024 · 32 · Q29, reworded)", opts: ["China had the highest percentage of children who died in infancy", "People in Hong Kong lived the longest", "Singapore had the largest number of people over 16", "Singapore's population was expected to fall in the next five years"], a: 0, why: "Infant mortality of 28 per 1,000 is the highest. The table gives no life expectancy or population totals." },
  { q: "A table shows urbanisation in more developed, less developed and least developed regions between 2010 and 2050: 75% to 86%, 45% to 66% and 29% to 55%. Which relationship can be confirmed? (May/June 2023 · 31 · Q29, reworded)", opts: ["The least developed regions have the largest urban populations in both years", "The more developed regions have the lowest growth in urbanisation between 2010 and 2050", "The region with the biggest total population in 2010 has the fastest population growth", "The region with the largest urban population in 2010 has the highest urbanisation level by 2050"], a: 1, why: "The urbanised share rises by 11 points in more developed regions against 21 and 26 points in the others." },
  { q: "China's census shows a falling birth rate, more people reaching retirement age and a shrinking share of working-age people. Which policy would most quickly sustain economic growth? (Oct/Nov 2023 · 33 · Q19, reworded)", opts: ["Allow more immigration of labour", "Encourage women to leave work to have more children", "Increase research to raise labour productivity", "Tax workers more to pay for pensions"], a: 0, why: "Immigration adds workers straight away. Having children takes about 20 years, and research takes time to raise productivity." },
  { q: "Which influence is least likely to promote sustainable economic growth in a developing economy? (Feb/March 2021 · 32 · Q18, reworded)", opts: ["High saving rates", "Involvement in free trade", "Protected property rights", "Rapid population growth"], a: 3, why: "Very fast population growth can reduce capital per worker and spread resources thinly." },
  { q: "Over a year, nominal national income increased by 2%, inflation was 3% and population rose by 1%. Which statement is correct? (Feb/March 2024 · 32 · Q19, reworded)", opts: ["Real income per head fell by about 2%", "Real income per head rose by 1%", "Real income per head rose by 4%", "There was no change in real income per head"], a: 0, why: "Real income fell about 1% (2 − 3). Spread over a population that grew 1%, real income per head fell about 2%." },
] });
