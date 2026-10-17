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

/* ---------- nominal vs real ---------- */
function nrDraw(s) {
  const Y = (v) => 250 - v * 1.7, W = 80; let o = SV.line(60, 250, 700, 250) + SV.line(60, 250, 60, 40) + SV.text(66, 34, "GDP ($bn)", "sm");
  const bar = (x, v, c, l, vis) => vis > 0 ? SV.rect(x, Y(v), W, 250 - Y(v), c, op(0.65 * vis)) + SV.text(x + W / 2, 270, l, "sm", { "text-anchor": "middle", ...op(vis) }) + SV.text(x + W / 2, Y(v) - 6, Lib.fmtN(v, 1), "lbl bd", { "text-anchor": "middle", ...op(vis) }) : "";
  o += bar(120, 100, "f1", "Year 1 (real = nominal)", s.a) + bar(280, 108, "f2", "Year 2 nominal", s.b) + bar(440, 108 / 1.05, "f3", "Year 2 real", s.c);
  if (s.d > 0) o += tag(380, 70, "Nominal growth 8%, inflation 5%, real growth ≈ 2.9%", "c3", s.d, "middle");
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 290" role="img" aria-label="Nominal GDP rises 8 percent, prices 5 percent, so real GDP rises 2.9 percent">${nrDraw({ a: 1, b: 1, c: 1, d: 1 })}</svg>`;
Lib.stepper($("#stR"), { w: 760, h: 290, label: "Nominal GDP, inflation and real GDP", base: { a: 0, b: 0, c: 0, d: 0 }, draw: nrDraw, tween: 800, dwell: 5200, steps: [
  { cap: "<b>Year 1.</b> GDP is $100bn. Taking year 1 as the base year, real and nominal GDP are the same.", s: { a: 1 } },
  { cap: "<b>Year 2 nominal GDP</b> is $108bn at year 2 prices: nominal growth of 8%.", s: { a: 1, b: 1 } },
  { cap: "<b>But prices rose 5%.</b> Deflating: real GDP = 108 ÷ 1.05 = $102.9bn.", s: { a: 1, b: 1, c: 1 } },
  { cap: "<b>Real growth is only about 2.9%.</b> Most of the nominal rise was inflation. Approximately, real growth = nominal growth − inflation.", s: { a: 1, b: 1, c: 1, d: 1 } },
] });
const cyc = (x) => 150 + (x - 20) * 0.55 - 50 * Math.sin((x - 20) / 12);
function cyDraw(s) {
  let o = axes(70, 270, 720, 25, "Time", "Real GDP"), d = "", t = "", n = Math.round(s.k);
  for (let i = 0; i <= 100; i += 2) { const x = 70 + i * 6, y = 145 - i * 0.495 + 45 * Math.sin(i / 12); t += (i ? " L" : "M") + x + "," + (145 - i * 0.495); if (i <= n) d += (d ? " L" : "M") + x + "," + y; }
  o += SV.path(t, "dash", { fill: "none" }) + tag(660, 90, "Trend (potential)", "c4", 1, "end");
  o += d ? SV.path(d, "c2", { fill: "none", "stroke-width": 3.5 }) : "";
  return o;
}
$("#pic2").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="Real GDP rising, peaking, falling and recovering around a trend">${cyDraw({ k: 100 })}</svg>`;
Lib.stepper($("#stC"), { w: 760, h: 300, label: "Real GDP over the business cycle", base: { k: 0 }, draw: cyDraw, tween: 1000, dwell: 5200, steps: [
  { cap: "<b>Trend growth.</b> The dashed line shows the rise in potential output over time.", s: { k: 0 } },
  { cap: "<b>Expansion.</b> Real GDP grows faster than the trend: unemployment falls and spare capacity is used up.", s: { k: 30 } },
  { cap: "<b>Peak and recession.</b> Growth slows and real GDP falls for two or more quarters: <b>negative growth</b>, rising unemployment.", s: { k: 65 } },
  { cap: "<b>Trough and recovery.</b> Output stops falling and begins to rise again towards trend.", s: { k: 100 } },
] });

/* ---------- Lab 1 ---------- */
function labN() {
  if (!["n1", "n2", "pi"].every((i) => $("#" + i))) return;
  const n1 = +$("#n1").value, n2 = +$("#n2").value, pi = +$("#pi").value, r2 = n2 / (pi / 100), ng = (n2 - n1) / n1 * 100, rg = (r2 - n1) / n1 * 100;
  $("#r1").textContent = "$" + Lib.fmtN(r2, 1) + "bn"; $("#r2").textContent = Lib.fmtN(ng, 1) + "%"; $("#r3").textContent = Lib.fmtN(rg, 1) + "%";
  $("#rv").textContent = `Year 2 nominal GDP of $${n2}bn at a price index of ${pi} (year 1 = 100) is $${Lib.fmtN(r2, 1)}bn in year 1 prices. Nominal growth is ${Lib.fmtN(ng, 1)}%, but real growth is ${Lib.fmtN(rg, 1)}%. ${rg < 0 ? "Real GDP has fallen: negative growth, even though nominal GDP rose." : rg < ng ? "Inflation has eaten part of the nominal rise." : ""}`;
  const Y = (v) => 250 - v * 0.8; let o = SV.line(40, 250, 400, 250);
  [["Y1 real", n1, "f1"], ["Y2 nominal", n2, "f2"], ["Y2 real", r2, "f3"]].forEach(([l, v, c], i) => (o += SV.rect(60 + i * 110, Y(v), 80, 250 - Y(v), c, op(0.65)) + SV.text(100 + i * 110, 268, l, "sm", { "text-anchor": "middle" }) + SV.text(100 + i * 110, Y(v) - 6, Lib.fmtN(v, 0), "lbl bd", { "text-anchor": "middle" })));
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "n1", label: "Year 1 nominal GDP (index 100), $bn ", min: 200, max: 400, step: 10, value: 300, fmt: (v) => v, onInput: labN });
Lib.slider($("#g2"), { id: "n2", label: "Year 2 nominal GDP, $bn ", min: 200, max: 450, step: 10, value: 330, fmt: (v) => v, onInput: labN });
Lib.slider($("#g3"), { id: "pi", label: "Year 2 price index (year 1 = 100) ", min: 95, max: 125, step: 1, value: 106, fmt: (v) => v, onInput: labN });
labN();

/* ---------- Lab 2 ---------- */
function labP() {
  if (!["gr", "po"].every((i) => $("#" + i))) return;
  const g = +$("#gr").value, p = +$("#po").value, pc = ((1 + g / 100) / (1 + p / 100) - 1) * 100;
  $("#t1").textContent = g + "%"; $("#t2").textContent = p + "%"; $("#t3").textContent = (pc > 0 ? "+" : "") + Lib.fmtN(pc, 1) + "%";
  $("#tv").textContent = `Real GDP grows ${g}% and the population ${p}%, so GDP per head changes by ${Lib.fmtN(pc, 1)}%. ${pc > 0.05 ? "Average output per person rises, which usually means rising living standards." : pc < -0.05 ? "GDP per head falls although GDP grows: living standards on average fall." : "GDP per head is unchanged."}`;
  const Y = (v) => 150 - v * 12; let o = SV.line(40, 150, 400, 150) + SV.line(40, 20, 40, 190);
  [["GDP", g, "f2"], ["Population", p, "f1"], ["GDP per head", pc, pc >= 0 ? "f2" : "f3"]].forEach(([l, v, c], i) => (o += SV.rect(70 + i * 110, v >= 0 ? Y(v) : 150, 80, Math.abs(Y(v) - 150), c, op(0.65)) + SV.text(110 + i * 110, 185, l, "sm", { "text-anchor": "middle" }) + SV.text(110 + i * 110, (v >= 0 ? Y(v) : 150 + Math.abs(Y(v) - 150)) + (v >= 0 ? -6 : 14), Lib.fmtN(v, 1) + "%", "lbl bd", { "text-anchor": "middle" })));
  $("#labB").innerHTML = o;
}
Lib.slider($("#g4"), { id: "gr", label: "Real GDP growth, % ", min: -2, max: 8, step: 1, value: 3, fmt: (v) => v + "%", onInput: labP });
Lib.slider($("#g5"), { id: "po", label: "Population growth, % ", min: -1, max: 5, step: 1, value: 2, fmt: (v) => v + "%", onInput: labP });
labP();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Nominal or real?", buckets: [{"label": "Nominal (current prices)"}, {"label": "Real (adjusted for inflation)"}], items: [{"text": "GDP measured at today's prices", "b": 0}, {"text": "GDP deflated by a price index", "b": 1}, {"text": "Rises when only prices rise", "b": 0}, {"text": "Rises only if output rises", "b": 1}, {"text": "Used to measure economic growth", "b": 1}, {"text": "Used to show the money value of output", "b": 0}, {"text": "Also called money GDP", "b": 0}, {"text": "GDP in constant base-year prices", "b": 1}], done: "Nominal includes inflation; real removes it." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Economic growth", "A rise in real GDP over time"], ["Nominal GDP", "GDP at current prices"], ["Real GDP", "GDP adjusted for inflation"], ["Recession", "Two or more quarters of falling real GDP"], ["GDP per capita", "Real GDP divided by population"], ["GDP deflator", "Price index used to convert nominal to real GDP"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the steps for finding real growth in order.", items: ["Take nominal GDP for each year", "Divide by the price index and multiply by 100", "This gives real GDP for each year", "Find the change in real GDP", "Divide by the earlier year and multiply by 100"], done: "Deflate first, then find the percentage change." });
Lib.calc($("#c1"), { qs: [
  {"q": "Nominal GDP is $630bn and the price index is 105 (base year 100). What is real GDP ($bn)?", "a": 600, "unit": "$bn", "tol": 0.5, "hint": "630 ÷ 1.05.", "sol": "<b>$600bn</b>."},
  {"q": "Real GDP in the previous year was $580bn. What is real growth (to one decimal place)?", "a": 3.4, "unit": "%", "tol": 0.1, "hint": "20 ÷ 580.", "sol": "<b>3.4%</b>."},
  {"q": "Nominal GDP rises 4% and inflation is 6%. Approximately what is real growth?", "a": -2, "unit": "%", "tol": 0.2, "hint": "4 − 6.", "sol": "<b>−2%</b>: real GDP falls."},
  {"q": "Real GDP grows 3% and population grows 1%. Approximately what is growth in GDP per head?", "a": 2, "unit": "%", "tol": 0.2, "hint": "3 − 1.", "sol": "<b>2%</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Economic growth is measured by:", opts: ["The percentage change in real GDP", "The percentage change in nominal GDP", "The rise in prices", "The fall in unemployment"], a: 0, why: "Real, not nominal." },
  { q: "Real GDP is:", opts: ["GDP adjusted for inflation", "GDP at current prices", "GDP less imports", "GDP per head"], a: 0, why: "Corrected for price changes." },
  { q: "If nominal GDP rises by less than inflation, real GDP:", opts: ["Falls", "Rises", "Stays the same", "Doubles"], a: 0, why: "Negative real growth." },
  { q: "A recession is usually defined as:", opts: ["Two consecutive quarters of falling real GDP", "A rise in prices", "A fall in nominal GDP in one quarter", "Rising unemployment only"], a: 0, why: "Negative growth." },
  { q: "GDP per head rises when:", opts: ["GDP grows faster than population", "Population grows faster than GDP", "Prices rise", "Imports fall"], a: 0, why: "Average output per person." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Growth", "Rise in real GDP."],
  ["Nominal GDP", "Current prices."],
  ["Real GDP", "Adjusted for inflation."],
  ["Real = ", "Nominal ÷ index × 100."],
  ["Recession", "Two quarters of falling real GDP."],
  ["Per capita", "GDP ÷ population."],
  ["Actual growth", "Using spare capacity."],
  ["Potential growth", "LRAS or PPC shifts out."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "The table shows GDP indices over three years: real GDP 100, 105, 106 and money GDP 100, 107, 115 (years 1 to 3). Inflation and economic growth are two macroeconomic policy objectives. Which row gives a correct assessment of the country's achievement of these objectives over the period? (Feb/March 2023 · 12 · Q29, reworded)", opts: ["rate of inflation: cannot tell; economic growth: positive", "rate of inflation: declining; economic growth: cannot tell", "rate of inflation: positive; economic growth: declining", "rate of inflation: rising; economic growth: negative"], a: 2, why: "Money GDP grows faster than real GDP in every year, so there is inflation. Real growth is 5% then about 1%, so growth is positive but declining." },
  { q: "The table gives data for an economy: GDP at current prices ($ billion) 200, 220, 240, 300, 320 for 2010 to 2014, and the GDP deflator 100, 109, 125, 149, 154. In which year did real GDP decline compared with the previous year? (May/June 2023 · 13 · Q18, reworded)", opts: ["2011", "2012", "2013", "2014"], a: 1, why: "Real GDP is nominal ÷ deflator × 100: 200, 201.8, 192.0, 201.3, 207.8. It fell in 2012." },
  { q: "In year 1, a country's real GDP was $500 billion. In year 2, nominal GDP rose to $577.5 billion and the prices increased by 5%. What is the real GDP in year 2? (May/June 2023 · 13 · Q20, reworded)", opts: ["$4.76 billion", "$5 billion", "$476 billion", "$550 billion"], a: 3, why: "577.5 ÷ 1.05 = 550." },
  { q: "A household's income increased by 3%. Over the same period, the rate of inflation was also 3%. Which statement is correct? (May/June 2022 · 13 · Q23, reworded)", opts: ["Both the nominal income and the real income of the household increased by 3%", "The nominal income remained unchanged while the real income increased by 3%", "The nominal income of the household increased by 3% while the real income was unchanged", "Both nominal income and real income remained unchanged"], a: 2, why: "Real income is nominal income adjusted for inflation: +3% less 3% inflation is no change." },
  { q: "The table gives the value of the price index of an economy in two years: year 1 is 60 and year 2 is 120. What can be concluded about the period? (May/June 2024 · 12 · Q16, reworded)", opts: ["Nominal income doubled", "Real income doubled", "The cost of living doubled", "The standard of living doubled"], a: 2, why: "A price index that doubles means the cost of living doubled. Nothing is known about income." },
  { q: "The real national income of a country fell by 3%. What could have caused this? (May/June 2020 · 13 · Q25, reworded)", opts: ["Money national income fell by 3% when the rate of inflation was 6%", "Money national income fell by 6% when the rate of inflation was 3%", "Money national income rose by 3% when the rate of inflation was 6%", "Money national income rose by 6% when the rate of inflation was 3%"], a: 2, why: "Real change ≈ money change minus inflation: +3 − 6 = −3. In option B the real change would be −9%." },
] });
