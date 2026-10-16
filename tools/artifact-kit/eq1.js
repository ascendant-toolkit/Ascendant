/* ---------- data: income shares of five equal groups (poorest to richest) ---------- */
const op = (v) => ({ opacity: Math.max(0, Math.min(1, v)) });
const BASE = [5, 9, 14, 22, 50], AFTER = [8, 12, 16, 23, 41], halo = { style: "paint-order:stroke;stroke:var(--surface);stroke-width:5px" };
const cumOf = (s) => { const t = s.reduce((a, b) => a + b, 0); let c = 0; return [0, ...s.map((v) => (c += (v / t) * 100))]; };
const ginOf = (s) => { const y = cumOf([...s].sort((a, b) => a - b)); let sum = 0; for (let i = 1; i < y.length; i++) sum += y[i - 1] / 100 + y[i] / 100; return 1 - 0.2 * sum; };
const FL = { x0: 60, y0: 300, w: 300, h: 250 }, LX = (p) => FL.x0 + (p / 100) * FL.w, LY = (v) => FL.y0 - (v / 100) * FL.h;
const lorAxes = () => SV.line(FL.x0, FL.y0, FL.x0 + FL.w + 8, FL.y0) + SV.line(FL.x0, FL.y0, FL.x0, FL.y0 - FL.h - 8) + SV.text(FL.x0 + FL.w + 8, FL.y0 + 36, "Cumulative % of population", "sm", { "text-anchor": "end" }) + SV.text(FL.x0 + 6, FL.y0 - FL.h - 14, "Cumulative % of income", "sm");
function lorenzPath(cum, n) {
  const pts = [], f = Math.floor(n), fr = n - f;
  for (let i = 0; i <= Math.min(f, 5); i++) pts.push([LX(i * 20), LY(cum[i])]);
  if (f < 5 && fr > 0) pts.push([LX(f * 20 + fr * 20), LY(cum[f] + (cum[f + 1] - cum[f]) * fr)]);
  return pts;
}

/* ---------- Learn picture and Watch 1 ---------- */
const cB = cumOf(BASE), cA = cumOf(AFTER);
function lorDraw(s) {
  let o = lorAxes();
  for (let v = 0; v <= 100; v += 20) o += SV.text(FL.x0 - 6, LY(v) + 4, v, "sm", { "text-anchor": "end" }) + SV.text(LX(v), FL.y0 + 14, v, "sm", { "text-anchor": "middle" });
  if (s.sh > 0) { const poly = [[LX(0), LY(0)], ...cB.map((v, i) => [LX(i * 20), LY(v)])]; o += SV.poly([[LX(0), LY(0)], ...cB.map((v, i) => [LX(i * 20), LY(v)]).slice(1), [LX(100), LY(100)]], "f2", op(s.sh)) + SV.poly([[LX(0), LY(0)], ...cB.map((v, i) => [LX(i * 20), LY(v)]).slice(1), [LX(100), LY(0)]], "f1", op(s.sh)) + SV.text(LX(70), LY(75), "A", "lbl bd t2", { "text-anchor": "middle", ...op(s.sh) }) + SV.text(LX(78), LY(25), "B", "lbl bd t1", { "text-anchor": "middle", ...op(s.sh) }); }
  if (s.eq > 0) o += SV.line(LX(0), LY(0), LX(100), LY(100), "gr", { "stroke-width": 2.5, ...op(s.eq) }) + SV.text(LX(46), LY(60), "line of equality", "sm bd", { ...halo, ...op(s.eq) });
  const pts = lorenzPath(cB, s.n); if (pts.length > 1) o += SV.path(Lib.ptsPath(pts), "c1");
  for (let i = 1; i <= 5; i++) if (s.n >= i) o += SV.circle(LX(i * 20), LY(cB[i]), 5, "dot1") + (i < 5 ? SV.text(LX(i * 20) + 8, LY(cB[i]) + 14, Lib.fmtN(cB[i], 0) + "%", "sm bd t1", { ...halo }) : "");
  if (s.aft > 0) { const p2 = lorenzPath(cA, 5); o += SV.path(Lib.ptsPath(p2), "c3", { "stroke-dasharray": "6 4", ...op(s.aft) }) + SV.text(LX(1), LY(86), "- - -  after tax and benefits", "lbl bd t3", { ...halo, ...op(s.aft) }); }
  if (s.sh > 0.5) o += SV.text(LX(2), LY(100) + 20, "Gini = A ÷ (A + B) ≈ " + Lib.fmtN(ginOf(BASE), 2) + (s.aft > 0.5 ? "  →  " + Lib.fmtN(ginOf(AFTER), 2) + " after" : ""), "lbl bd", { ...halo });
  // bars of quintile shares
  const bx = (i) => 450 + i * 58, bh = (v) => (v / 50) * 200;
  o += SV.text(450, 40, "Income share of each group (%)", "lbl bd") + SV.line(440, 300, 750, 300);
  ["poorest", "2nd", "3rd", "4th", "richest"].forEach((l, i) => { o += SV.text(bx(i) + 20, 316, l, "sm", { "text-anchor": "middle" }); if (s.n > i) o += SV.rect(bx(i), 300 - bh(BASE[i]), 18, bh(BASE[i]), "f1", op(Math.min(1, s.n - i))) + SV.text(bx(i) + 9, 300 - bh(BASE[i]) - 6, BASE[i], "sm bd t1", { "text-anchor": "middle", ...op(Math.min(1, s.n - i)) }); if (s.aft > 0) o += SV.rect(bx(i) + 20, 300 - bh(AFTER[i]), 18, bh(AFTER[i]), "f3", op(s.aft)) + SV.text(bx(i) + 29, 300 - bh(AFTER[i]) - 6, AFTER[i], "sm bd t3", { "text-anchor": "middle", ...op(s.aft) }); });
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 780 345" role="img" aria-label="Lorenz curve below the line of equality with areas A and B, and income shares of five groups">${lorDraw({ n: 5, eq: 1, sh: 1, aft: 0 })}</svg>`;
Lib.stepper($("#stA"), { w: 780, h: 345, label: "Building a Lorenz curve from five income groups and calculating the Gini coefficient", base: { n: 0, eq: 0, sh: 0, aft: 0 }, draw: lorDraw, tween: 900, dwell: 5800, steps: [
  { cap: "<b>The line of equality.</b> If every group had the same income, the poorest 20% would get 20%, the poorest 40% would get 40%, and so on: a straight diagonal.", s: { eq: 1 } },
  { cap: "<b>Plot the data.</b> The poorest 20% of households receive <b>5%</b> of income. Adding the next group, the poorest 40% receive 5 + 9 = <b>14%</b>. The poorest 60% receive <b>28%</b>, the poorest 80% receive <b>50%</b>. The richest 20% receive the other 50%.", s: { eq: 1, n: 4 } },
  { cap: "<b>The Lorenz curve</b> joins the points up to (100, 100). It bows below the line of equality because the poor get a smaller share than their share of the population.", s: { eq: 1, n: 5 } },
  { cap: `<b>The Gini coefficient.</b> Area <b>A</b> is between the line of equality and the curve. Area <b>B</b> is under the curve. Gini = A ÷ (A + B) = <b>${Lib.fmtN(ginOf(BASE), 2)}</b>. A bigger bow means a larger A, so a higher Gini.`, s: { eq: 1, n: 5, sh: 1 } },
  { cap: `<b>After tax and benefits.</b> Progressive taxes and transfers raise the poorest 20% from 5% to 8% and cut the richest 20% from 50% to 41%. The Lorenz curve (dashed) moves towards the line of equality and the Gini falls to <b>${Lib.fmtN(ginOf(AFTER), 2)}</b>.`, s: { eq: 1, n: 5, sh: 1, aft: 1 } },
] });

/* ---------- Lab 1: Lorenz and Gini ---------- */
function lab1() {
  if (!$("#ts") || !$("#rd")) return;
  const T = +$("#ts").value, r = +$("#rd").value / 100, f = (100 - T) / 50;
  const pre = [BASE[0] * f, BASE[1] * f, BASE[2] * f, BASE[3] * f, T], sh = pre.map((v) => (1 - r) * v + r * 20), c = cumOf(sh), g = ginOf(sh);
  $("#r1").textContent = Lib.fmtN(c[2], 0) + "%"; $("#r2").textContent = Lib.fmtN(sh[4], 0) + "%"; $("#r3").textContent = Lib.fmtN(g, 2);
  $("#rv").textContent = g > 0.5 ? "Very unequal: the richest 20% hold a large share, the curve bows far from the line of equality and the Gini is high."
    : g < 0.25 ? "Fairly equal: the curve is close to the line of equality and the Gini is low."
    : "A moderate level of inequality. Raise the top share to widen the gap, or add redistribution to bring the curve closer to the line.";
  const F = { x0: 50, y0: 290, w: 330, h: 250 }, X = (p) => F.x0 + (p / 100) * F.w, Y = (v) => F.y0 - (v / 100) * F.h;
  const pts = c.map((v, i) => [X(i * 20), Y(v)]);
  let o = SV.line(F.x0, F.y0, F.x0 + F.w + 8, F.y0) + SV.line(F.x0, F.y0, F.x0, F.y0 - F.h - 8) + SV.text(F.x0 + F.w + 8, F.y0 + 24, "Cumulative % of population", "sm", { "text-anchor": "end" }) + SV.text(F.x0 + 6, F.y0 - F.h - 14, "Cumulative % of income", "sm");
  o += SV.poly([[X(0), Y(0)], ...pts.slice(1), [X(100), Y(100)]], "f2") + SV.line(X(0), Y(0), X(100), Y(100), "gr", { "stroke-width": 2 }) + SV.path(Lib.ptsPath(pts), "c1") + pts.slice(1, 5).map((p) => SV.circle(p[0], p[1], 5, "dot1")).join("");
  o += SV.text(X(70), Y(78), "A", "lbl bd t2", { "text-anchor": "middle" }) + SV.text(X(80), Y(24), "B", "lbl bd t1", { "text-anchor": "middle" });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "ts", label: "Share of income going to the richest 20%: ", min: 30, max: 70, step: 1, value: 50, fmt: (v) => v + "%", onInput: lab1 });
Lib.slider($("#g2"), { id: "rd", label: "Redistribution through tax and benefits: ", min: 0, max: 60, step: 5, value: 0, fmt: (v) => v + "%", onInput: lab1 });

/* ---------- Lab 2: poverty lines ---------- */
function labPov() {
  if (!$("#gr")) return;
  const g = +$("#gr").value / 100, inc = [8, 12, 18, 30, 60].map((v) => v * (1 + g)), med = inc[2], rel = 0.5 * med, a = inc.filter((v) => v < 10).length, r = inc.filter((v) => v < rel).length;
  $("#v1").textContent = "$" + Lib.fmtN(med, 1) + "k"; $("#v2").textContent = a + " of 5"; $("#v3").textContent = "$" + Lib.fmtN(rel, 1) + "k"; $("#v4").textContent = r + " of 5";
  $("#vv").textContent = g === 0 ? "With incomes as they are, one household is below the absolute line and one below the relative line."
    : `Every income has risen ${Math.round(g * 100)}%. The absolute line is fixed at $10k, so ${a === 0 ? "nobody" : a + (a === 1 ? " household is" : " households are")} below it. The relative line moves up with the median to $${Lib.fmtN(rel, 1)}k, and ${r} household${r === 1 ? " is" : "s are"} still below it. Absolute poverty can fall while relative poverty stays the same.`;
  const base = 240, H = (v) => v * 2.6, bw = 40;
  let o = SV.line(30, base, 400, base) + SV.text(30, 20, "Income ($k)", "sm");
  inc.forEach((v, i) => { const x = 50 + i * 68; o += SV.rect(x, base - H(v), bw, H(v), v < 10 || v < rel ? "f2" : "f1") + SV.text(x + bw / 2, base - H(v) - 6, Lib.fmtN(v, 1), "sm bd", { "text-anchor": "middle" }) + SV.text(x + bw / 2, base + 16, "H" + (i + 1), "sm", { "text-anchor": "middle" }); });
  o += SV.line(30, base - H(10), 400, base - H(10), "c3", { "stroke-dasharray": "6 5" }) + SV.text(398, base - H(10) - 6, "absolute $10k", "sm bd t3", { "text-anchor": "end", style: "paint-order:stroke;stroke:var(--surface);stroke-width:4px" }) + SV.line(30, base - H(rel), 400, base - H(rel), "c4", { "stroke-dasharray": "3 4" }) + SV.text(398, base - H(rel) + 16, "relative $" + Lib.fmtN(rel, 1) + "k", "sm bd t4", { "text-anchor": "end", style: "paint-order:stroke;stroke:var(--surface);stroke-width:4px" });
  $("#labW").innerHTML = o;
}
Lib.slider($("#g7"), { id: "gr", label: "Rise in every household's income: ", min: 0, max: 100, step: 10, value: 0, fmt: (v) => v + "%", onInput: labPov });

/* ---------- Practise ---------- */
Lib.classify($("#cl3"), {
  prompt: "Is each item income (a flow) or wealth (a stock)?",
  buckets: [{ label: "Income" }, { label: "Wealth" }],
  items: [
    { text: "Monthly salary", b: 0 }, { text: "Interest received this year", b: 0 }, { text: "Dividends paid to a shareholder", b: 0 }, { text: "Unemployment benefit", b: 0 },
    { text: "A house", b: 1 }, { text: "Savings in a bank account", b: 1 }, { text: "Shares owned", b: 1 }, { text: "A pension fund", b: 1 },
  ], done: "Income is received over a period; wealth is a stock of assets at a point in time.",
});
Lib.order($("#o1"), { prompt: "Put the steps for drawing a Lorenz curve in order.", items: [
  "Rank households from poorest to richest and split them into equal groups",
  "Work out each group's share of total income",
  "Calculate cumulative population and cumulative income shares",
  "Draw the line of equality from (0, 0) to (100, 100)",
  "Plot the cumulative points and join them to form the Lorenz curve",
  "Compare the area between the curve and the line (A) with the area below the curve (B) to find the Gini",
], done: "A bigger bow means a higher Gini coefficient." });
Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Economic equality", "An equal distribution of income, wealth or opportunities"],
  ["Equity", "Fairness in the distribution of resources, a value judgement"],
  ["Income", "A flow received over a period"],
  ["Wealth", "A stock of assets at a point in time"],
  ["Lorenz curve", "Cumulative % of income against cumulative % of the population"],
  ["Gini coefficient", "Area A ÷ (A + B), from 0 (equality) to 1 (inequality)"],
  ["Absolute poverty", "Income below the level needed for basic survival"],
  ["Relative poverty", "Income low compared with the average in the same society"],
], done: "Eight words for measuring inequality." });
Lib.calc($("#c1"), { qs: [
  { q: "Income shares of five equal groups are 5%, 9%, 14%, 22% and 50%. What share does the poorest 60% receive (%)?", a: 28, sol: "5 + 9 + 14 = <b>28%</b>." },
  { q: "On a Lorenz diagram area A is 0.1 and area B is 0.4. What is the Gini coefficient?", a: 0.2, sol: "A ÷ (A + B) = 0.1 ÷ 0.5 = <b>0.2</b>." },
  { q: "A country's Gini coefficient falls from 0.40 to 0.30. By what percentage did it fall (%)?", a: 25, sol: "(0.40 − 0.30) ÷ 0.40 × 100 = <b>25%</b>." },
  { q: "The richest 20% receive 50% of income and the poorest 20% receive 5%. By how many percentage points does the richest share exceed the poorest share?", a: 45, sol: "50 − 5 = <b>45</b> percentage points." },
  { q: "Five household incomes are $8k, $12k, $18k, $30k and $60k. What is the median ($k)?", a: 18, sol: "The middle value of the five, in order, is <b>$18k</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A Gini coefficient of 0 means:", opts: ["perfect inequality", "perfect equality", "high poverty", "no wealth"], a: 1, why: "At 0 everyone receives the same: the Lorenz curve is the line of equality." },
  { q: "A bigger bow of the Lorenz curve away from the line of equality shows:", opts: ["more equality", "more inequality", "lower poverty", "a lower Gini"], a: 1, why: "Area A is bigger, so the Gini is higher." },
  { q: "Equity differs from equality because equity:", opts: ["is an equal distribution", "is about fairness, a value judgement", "can be measured by the Gini coefficient", "ignores incomes"], a: 1, why: "Equity is normative, equality is an outcome that can be measured." },
  { q: "Relative poverty is measured against:", opts: ["a fixed survival income", "the average income in the same society", "the poverty line of another country", "zero income"], a: 1, why: "Relative poverty compares a household with the typical household in its own society." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Economic equality", "An equal distribution of income, wealth and opportunities."],
  ["Equity", "Fairness or justice in the distribution of resources. A normative idea."],
  ["Income", "A flow received over a period: wages, profit, rent, interest, benefits."],
  ["Wealth", "A stock of assets at a point in time: property, savings, shares."],
  ["Lorenz curve", "Cumulative % of income against cumulative % of the population."],
  ["Line of equality", "The 45 degree line showing a perfectly equal distribution."],
  ["Gini coefficient", "Area A ÷ (A + B). From 0 (perfect equality) to 1 (perfect inequality)."],
  ["Absolute poverty", "Income below the level needed for basic survival (a poverty line)."],
  ["Relative poverty", "Income low compared with the average in the same society."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "[May/June 2021 · 31 · Q15] The Gini coefficient of a country is 0.40. The poorest income earners pay no income tax. The government increases the tax rate on the highest income earners, which results in a more even distribution of income. What could be concluded from this?", opts: ["The Gini coefficient falls and the income tax system becomes more progressive.", "The Gini coefficient falls and the income tax system becomes more regressive.", "The Gini coefficient rises and the income tax system becomes more progressive.", "The Gini coefficient rises and the income tax system becomes more regressive."], a: 0, why: "A more even distribution means a lower Gini, and raising rates on the rich makes the tax more progressive." },
  { q: "[Feb/March 2025 · 32 · Q9] When does a more equal distribution of income occur?", opts: ["when a country's income tax system is made more progressive", "when someone is made better off without making someone else worse off", "when the best use is made of scarce resources", "when there is an increase in the Gini coefficient"], a: 0, why: "B is a Pareto improvement, C is efficiency, D is greater inequality." },
  { q: "[May/June 2020 (not sat) · 31 · Q16] The diagram shows two Lorenz curves. If the Lorenz curve shifts from L1 to L2 (further from the line of equality), what is least likely to have caused this?", opts: ["Capital gains tax has been reduced.", "Income tax has been made more progressive.", "Inheritance tax has been reduced.", "The tax-free allowance has been decreased for everyone."], a: 1, why: "A shift away from the line of equality means more inequality. A more progressive income tax reduces it, so it is the least likely cause." },
  { q: "[Feb/March 2023 · 32 · Q27] A diagram shows income inequality rising and then falling as income per capita increases. Which curve is shown?", opts: ["Kuznets curve", "Laffer curve", "Lorenz curve", "Phillips curve"], a: 0, why: "The Kuznets curve suggests inequality first rises then falls as a country develops." },
] });
