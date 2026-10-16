const op = (v) => ({ opacity: Math.max(0, Math.min(1, v)) });
const halo = { style: "paint-order:stroke;stroke:var(--surface);stroke-width:5px" };
const arrow = (x1, y1, x2, y2, dir, cls, v) => `<g style="opacity:${Math.max(0, Math.min(1, v))}">${SV.line(x1, y1, x2, y2, cls, { "stroke-width": 2.5 })}${SV.arrowHead(x2, y2, dir, cls === "c2" ? "dot2" : cls === "c3" ? "dot3" : cls === "c4" ? "dot4" : "dot1")}</g>`;
const axes = (x0, y0, x1, y1, xl, yl) => SV.line(x0, y0, x1, y0) + SV.line(x0, y0, x0, y1) + SV.text(x1, y0 + 26, xl, "sm", { "text-anchor": "end" }) + SV.text(x0 + 6, y1 - 6, yl, "sm");
const tag = (x, y, t, c, v = 1, a = "start") => SV.text(x, y, t, "lbl bd " + c, { "text-anchor": a, ...halo, ...op(v) });
/* click a button, show its row of results */
function btnTable(btnId, outId, rows, heads) {
  const box = $("#" + btnId), out = $("#" + outId); if (!box || !out) return;
  box.innerHTML = rows.map((r, i) => `<button class="b" data-i="${i}">${r[0]}</button>`).join("");
  const show = (i) => { const r = rows[i]; $$("button", box).forEach((b, k) => b.classList.toggle("pri", k === i)); out.innerHTML = `<div class="tw"><table class="t"><tr>${heads.map((h) => `<th>${h}</th>`).join("")}</tr><tr>${r.slice(1).map((c, k) => `<td>${k ? c : "<b>" + c + "</b>"}</td>`).join("")}</tr></table></div>`; };
  $$("button", box).forEach((b) => (b.onclick = () => show(+b.dataset.i))); show(0);
}

/* ---------- Learn picture: unemployment by age ---------- */
$("#pic1").innerHTML = `<svg viewBox="0 0 760 330" role="img" aria-label="Bar chart of unemployment rates by age group: youth 14 percent, prime age 5 percent, older workers 4 percent, with the national average of 6 percent">${(() => { const g = [["15 to 24", 14, "f2", "t2"], ["25 to 49", 5, "f1", "t1"], ["50 to 64", 4, "f3", "t3"]]; let o = SV.line(70, 290, 720, 290) + SV.line(70, 290, 70, 30) + tag(70, 22, "Illustrative unemployment rates by age (%)", "t1"); const Y = (v) => 290 - v * 16; g.forEach(([l, v, c, t], i) => { const x = 130 + i * 170; o += SV.rect(x, Y(v), 100, 290 - Y(v), c) + tag(x + 50, Y(v) - 8, v + "%", t, 1, "middle") + SV.text(x + 50, 312, l, "sm bd", { "text-anchor": "middle" }); }); o += SV.line(70, Y(6), 700, Y(6), "c4 dash") + tag(698, Y(6) - 6, "national average 6%", "t4", 1, "end"); return o; })()}</svg>`;

/* ---------- Watch 1: growth and unemployment ---------- */
const GR = [3, 2.5, -2, -0.5, 2, 3, 3.2, 2.8, 2.5, -5, 3, 3.5], UR = [5, 5, 8, 9, 8.2, 7.1, 6.2, 5.6, 5.3, 8.5, 7.6, 6.4];
const GX = (i) => 100 + i * 52, GYb = (g) => 160 - g * 12, GYu = (u) => 310 - u * 11;
function guDraw(s) {
  let o = SV.line(70, 160, 740, 160) + SV.text(66, 164, "0", "sm", { "text-anchor": "end" }) + tag(70, 28, "GDP growth (%, bars)", "t1") + tag(70, 208, "Unemployment rate (%, line)", "t2") + SV.line(70, 310, 740, 310, "gr");
  const n = Math.round(s.n);
  for (let i = 0; i < n && i < 12; i++) { const g = GR[i], y = g >= 0 ? GYb(g) : 160; o += SV.rect(GX(i) - 14, y, 28, Math.abs(g) * 12, g >= 0 ? "f1" : "f2") + SV.text(GX(i), 330, "Y" + (i + 1), "sm", { "text-anchor": "middle" }); }
  const pts = []; for (let i = 0; i < n && i < 12; i++) pts.push([GX(i), GYu(UR[i])]);
  if (pts.length > 1) o += SV.path(Lib.ptsPath(pts), "c2"); pts.forEach((p) => (o += SV.circle(p[0], p[1], 4, "dot2")));
  if (s.m1 > 0 && n >= 4) o += tag(GX(3) , GYu(9) - 12, "peak after the fall in output", "t2", s.m1, "middle");
  if (s.m2 > 0 && n >= 10) o += tag(GX(9) , GYu(8.5) - 12, "rises again", "t2", s.m2, "middle");
  return o;
}
Lib.stepper($("#stG"), { w: 760, h: 345, label: "Bars for GDP growth and a line for unemployment over twelve years with two recessions", base: { n: 0, m1: 0, m2: 0 }, draw: guDraw, tween: 1200, dwell: 6000, steps: [
  { cap: "<b>A normal expansion.</b> In years 1 and 2 growth is solid at about 3% and unemployment is steady at 5%.", s: { n: 2 } },
  { cap: "<b>Recession.</b> Output falls in years 3 and 4 and unemployment jumps from 5% to 9%. Notice that unemployment keeps rising in year 4 even though the economy is shrinking by less: the <b>lag</b>.", s: { n: 4, m1: 1 } },
  { cap: "<b>Recovery.</b> Growth returns and unemployment falls, but slowly, over about four years. Firms hire late and some of the long-term unemployed have lost skills.", s: { n: 8, m1: 1 } },
  { cap: "<b>A second shock.</b> A deep one-year fall in output (year 10) raises unemployment sharply again, though the recovery that follows is quicker because many jobs were kept.", s: { n: 12, m1: 1, m2: 1 } },
] });

/* ---------- Watch 2: what the average hides ---------- */
const BX = (i) => 110 + i * 70;
function avgDraw(s) {
  const grp = [["All", 6, "f4"], ["15-24", 14, "f2"], ["25-49", 5, "f1"], ["50-64", 4, "f3"], ["City", 4, "f1"], ["Old industry", 11, "f2"]];
  let o = SV.line(70, 280, 740, 280) + SV.line(70, 280, 70, 30), Y = (v) => 280 - v * 14;
  grp.forEach(([l, v, c], i) => { const on = i === 0 || (i <= 3 && s.a > 0) || (i >= 4 && s.b > 0), op_ = i === 0 ? 1 : i <= 3 ? s.a : s.b; if (!on) return; o += SV.rect(BX(i) - 25, Y(v), 50, 280 - Y(v), c, op(op_)) + tag(BX(i), Y(v) - 8, v + "%", i === 0 ? "t4" : "t1", op_, "middle") + SV.text(BX(i), 300, l, "sm bd", { "text-anchor": "middle", ...op(op_) }); });
  o += SV.line(70, Y(6), 740, Y(6), "c4 dash") + tag(738, Y(6) - 6, "average 6%", "t4", 1, "end");
  return o;
}
Lib.stepper($("#stB"), { w: 760, h: 330, label: "National unemployment rate of 6 percent broken down by age and region", base: { a: 0, b: 0 }, draw: avgDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>The headline.</b> The national unemployment rate is <b>6%</b>. It sounds moderate, and it is a useful single number.", s: {} },
  { cap: "<b>By age.</b> Young workers face <b>14%</b>, prime-age workers 5% and older workers 4%. Youth have less experience and fewer contacts, and are the first to be let go.", s: { a: 1 } },
  { cap: "<b>By region.</b> A prosperous city is at 4% while a region that depended on a declining industry is at 11%. The average hides large differences, so policy must be targeted.", s: { a: 1, b: 1 } },
] });

/* ---------- Lab 1: who counts ---------- */
function labCount() {
  if (!$("#gu") || !$("#uh")) return;
  const g = +$("#gu").value, f = Math.min(+$("#uh").value, 6 - g);
  const emp = 62 + f, unemployed = 6 - g - f, inactive = 32 + g, labour = emp + unemployed;
  $("#r1").textContent = Lib.fmtN(unemployed / labour * 100, 1) + "%"; $("#r2").textContent = Lib.fmtN(emp, 0) + "%"; $("#r3").textContent = Lib.fmtN(labour, 0) + "%";
  $("#rv").textContent = g === 0 && f === 0 ? "Baseline: 62 employed, 6 unemployed and 32 inactive out of 100. Unemployment rate = 6 ÷ 68 = 8.8%." : g > 0 && f === 0 ? `${g} unemployed people stopped looking for work. The unemployment rate falls to ${Lib.fmtN(unemployed / labour * 100, 1)}% but employment is still 62 out of 100 and the participation rate has fallen to ${labour}%. No jobs were created, so the headline rate understates the problem.` : `${f} unemployed people found jobs, so employment rises to ${emp}% and the unemployment rate falls to ${Lib.fmtN(unemployed / labour * 100, 1)}%` + (g > 0 ? `, and ${g} others stopped looking, so the participation rate is ${labour}%.` : ".");
  let x = 50, o = SV.line(40, 250, 400, 250);
  [[emp, "f1", "Employed"], [unemployed, "f2", "Unemployed"], [inactive, "f3", "Inactive"]].forEach(([v, c, l]) => { const w = v * 3.2; o += SV.rect(x, 120, w, 70, c) + SV.text(x + w / 2, 160, v, "lbl bd", { "text-anchor": "middle" }); if (v > 4) o += SV.text(x + w / 2, 212, l, "sm bd", { "text-anchor": "middle" }); x += w; });
  o += tag(50, 100, "100 people of working age", "t1") + SV.line(50, 232, 50 + labour * 3.2, 232, "c4", { "stroke-width": 3 }) + tag(50, 250, "labour force: " + labour, "t4");
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "gu", label: "Unemployed who stop looking ", min: 0, max: 6, step: 1, value: 0, fmt: (v) => v, onInput: labCount });
Lib.slider($("#g2"), { id: "uh", label: "Unemployed who find jobs ", min: 0, max: 6, step: 1, value: 0, fmt: (v) => v, onInput: labCount });
labCount();
btnTable("lbBtns", "lbOut", [
  ["The unemployment rate fell from 8% to 6%.", "Fewer unemployed as a share of the labour force.", "Check whether employment rose or people left the labour force (participation rate)."],
  ["Unemployment is 5% nationally but 12% for under-25s.", "A pattern by age: youth are hit harder.", "Ask why (experience, last in first out) and whether students are included."],
  ["Employment rose by 300,000 while unemployment rose too.", "The labour force grew (more people entered).", "Rates and numbers can move differently. Look at participation and population."],
  ["Unemployment has risen for three years while GDP is growing again.", "Unemployment lags behind output.", "Consider hysteresis, productivity growth and skills mismatch."],
  ["Measured unemployment is 4% but half the workforce is in informal work.", "Measured unemployment may understate under-use of labour.", "Look for underemployment and low pay, especially in developing countries."],
  ["The claimant count fell by 10% but survey unemployment fell by 3%.", "The two measures use different definitions.", "Benefit rules and eligibility can change the claimant count without changing real unemployment."]
], ["Statement", "What it tells you", "What to check"]);

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Is the person counted as unemployed in the survey measure?", buckets: [{"label": "Counted as unemployed"}, {"label": "Not counted as unemployed"}], items: [{"text": "Without a job, available and applying for jobs", "b": 0}, {"text": "A full-time student who is not looking for work", "b": 1}, {"text": "A worker who gave up looking after a year", "b": 1}, {"text": "A part-time worker who wants full-time hours", "b": 1}, {"text": "A person who lost their job last week and is searching", "b": 0}, {"text": "A retired person", "b": 1}, {"text": "A graduate waiting to start a job next week, who has been searching for three months", "b": 0}, {"text": "A parent caring for children who is not looking for work", "b": 1}], done: "Unemployed means without work, available to start and actively seeking work." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Participation rate", "Labour force as a share of the working-age population"], ["Claimant count", "Number of people claiming unemployment benefits"], ["Underemployment", "Workers with too few hours or in jobs below their skills"], ["Okun's law", "A fall in output below trend is linked to more unemployment"], ["Long-term unemployment", "Out of work for 12 months or more"], ["Discouraged worker", "Someone who has stopped looking for work because they expect no success"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the way a recession shows up in the data in order.", items: ["Real GDP falls", "Firms cut hours and freeze hiring", "Unemployment rises, with a lag", "The share of long-term unemployed rises", "After recovery begins unemployment falls slowly"], done: "Unemployment lags behind output at both turning points." });
Lib.calc($("#c1"), { qs: [
  {"q": "The working-age population is 40m, of whom 26m are employed, 2m are unemployed and the rest are inactive. Calculate the participation rate (%).", "a": 70, "unit": "%", "tol": 0.05, "hint": "Labour force = employed + unemployed = 28m.", "sol": "28 ÷ 40 × 100 = <b>70%</b>."},
  {"q": "Using the same data, calculate the unemployment rate (to one decimal place).", "a": 7.1, "unit": "%", "tol": 0.1, "hint": "Unemployed ÷ labour force.", "sol": "2 ÷ 28 × 100 = <b>7.1%</b>."},
  {"q": "Unemployment rises from 4% to 6%. By how many percentage points has it risen?", "a": 2, "unit": "points", "tol": 0.01, "hint": "Subtract.", "sol": "6 − 4 = <b>2 percentage points</b>. (It is a 50% rise.)"},
  {"q": "Using Okun's law (2% below trend output goes with 1 percentage point more unemployment), by how many percentage points would unemployment rise if output is 5% below trend?", "a": 2.5, "unit": "points", "tol": 0.05, "hint": "5 ÷ 2.", "sol": "5 ÷ 2 = <b>2.5 percentage points</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "The unemployment rate falls but the employment rate is unchanged. What is the most likely explanation?", opts: ["More jobs have been created", "Some unemployed people have left the labour force", "The population has fallen", "Output has grown"], a: 1, why: "If nobody found a job but some stopped searching, the unemployment rate falls without any rise in employment." },
  { q: "What is the labour force?", opts: ["Everyone of working age", "Employed plus unemployed", "Employed only", "Unemployed only"], a: 1, why: "The labour force is the employed plus those actively seeking work." },
  { q: "Which statement describes the lag between output and unemployment?", opts: ["Unemployment rises before output falls", "Unemployment usually keeps rising after output starts to recover", "Unemployment and output move together without a delay", "Output always follows unemployment"], a: 1, why: "Firms keep workers at first and hire late in a recovery." },
  { q: "Which group usually has the highest unemployment rate?", opts: ["Prime-age workers", "Older workers", "Young workers", "Highly qualified workers"], a: 2, why: "Young workers have less experience and fewer contacts." },
  { q: "Why might measured unemployment be low in a developing country?", opts: ["Most people have well-paid secure jobs", "Many people work in the informal sector or are underemployed", "There are no benefits", "Growth is always rapid"], a: 1, why: "Informal and underemployed workers count as employed even though their work is limited." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Unemployment rate", "Unemployed ÷ labour force × 100."],
  ["Employment rate", "Employed ÷ working-age population × 100."],
  ["Participation rate", "Labour force ÷ working-age population."],
  ["Claimant count", "Number claiming unemployment benefits."],
  ["Discouraged worker", "Stopped looking; not counted as unemployed."],
  ["Underemployment", "Too few hours or a job below skill level."],
  ["Okun's law", "About 2% below-trend output goes with 1 point more unemployment."],
  ["Long-term unemployment", "Out of work 12 months or more."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "The table shows labour market data: employed 15m; unemployed 0.5m; not available for work 7m; working-age population 23m. What is the size of the labour force? (Oct/Nov 2021 · 32 · Q21, reworded)", opts: ["15m", "15.5m", "22m", "22.5m"], a: 1, why: "Labour force = employed + unemployed = 15m + 0.5m = 15.5m." },
  { q: "Which groups are part of a country's labour force? (May/June 2023 · 31 · Q28, reworded)", opts: ["Unemployed only", "Unemployed and self-employed, but not the economically inactive", "Unemployed and inactive", "Inactive and self-employed"], a: 1, why: "The labour force is those in work (including self-employed) plus those actively seeking work. The inactive are outside it." },
  { q: "The Netherlands has the highest share of part-time employees and an average working week of 32 hours. Greece has a smaller share of part-time employees and an average of 41 hours. What can be concluded? (Feb/March 2020 · 32 · Q26, reworded)", opts: ["Greece has a higher percentage of its workforce in full-time employment than the Netherlands", "Part-time employees work longer on average in Greece", "Full-time employees work longer weeks in Greece", "There are more part-time employees in the Netherlands than in Greece"], a: 0, why: "A smaller part-time share means a larger full-time share. The other statements compare hours or numbers of people that the data do not give." },
  { q: "A report suggests that automation could threaten a third of existing jobs in the UK, mainly in manufacturing and retail. Which type of unemployment is this? (Feb/March 2020 · 32 · Q27, reworded)", opts: ["Demand-deficient", "Frictional", "Seasonal", "Structural"], a: 3, why: "Technology changing the pattern of jobs causes structural unemployment." },
  { q: "The table shows monthly US inflation (2.2, 1.9, 1.6, 1.7, 1.9, 2.2 per cent) and unemployment (3.9, 3.8, 3.9, 3.9, 3.8, 3.7 per cent). What can be concluded? (May/June 2022 · 31 · Q30, reworded)", opts: ["Falling inflation leads to lower unemployment", "Rising inflation leads to rising unemployment", "Inflation correlates exactly with unemployment", "Inflation has only a marginal effect on unemployment over this period"], a: 3, why: "Unemployment barely moved while inflation changed, so the data show only a small effect. They do not show cause." },
  { q: "Unemployment in a country rose from 3.5% to 4.8% over five years while inflation fell from 4.0% to 2.0%. Which statement about the Phillips curve is best supported? (Oct/Nov 2024 · 32 · Q23, reworded)", opts: ["The data are entirely consistent with the Phillips curve idea", "The data prove the Phillips curve does not work", "No conclusion about the Phillips curve is possible", "The Phillips curve is correct, with time lags"], a: 0, why: "Higher unemployment with lower inflation fits the inverse relationship, although five observations cannot prove it." },
  { q: "Which combination is most likely to increase a country's budget deficit? (Feb/March 2023 · 32 · Q17, reworded)", opts: ["Government spending falls, GDP rises, unemployment falls", "Government spending falls, GDP rises, unemployment unchanged", "Government spending rises, GDP falls, unemployment rises", "Government spending rises, GDP falls, unemployment unchanged"], a: 2, why: "A downturn cuts tax revenue and raises benefit spending, and higher spending adds to the deficit." },
  { q: "Two people lose their jobs. Mariana's factory closes because of cheaper imports. Alfonso, a shop assistant, is laid off because sales fall in a recession. How would an economist classify the two job losses? (Feb/March 2021 · 32 · Q21, reworded)", opts: ["Frictional and seasonal", "Regional and frictional", "Structural and cyclical", "Technological and structural"], a: 2, why: "Competition from imports changing the pattern of demand is structural. A recession-led fall in sales is cyclical." },
] });
