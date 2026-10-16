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

/* ---------- Lorenz picture and Watch 1 ---------- */
const LX = (v) => 80 + v * 260, LY = (v) => 310 - v * 260;
function lorenzDraw(s) {
  const k = s.k, pts = []; for (let x = 0; x <= 1.0001; x += 0.02) pts.push([LX(x), LY(Math.pow(x, k))]);
  const gini = (k - 1) / (k + 1);
  let o = axes(80, 310, 360, 40, "Cumulative % of households", "Cumulative % of income") + SV.line(LX(0), LY(0), LX(1), LY(1), "c3 dash") + tag(LX(0.55), LY(0.62) - 6, "line of equality", "t3");
  o += SV.path(Lib.ptsPath(pts) + ` L ${LX(1)} ${LY(0)} Z`, "f1", { opacity: 0.12 }) + SV.path(Lib.ptsPath(pts), "c1");
  o += tag(LX(0.78), LY(0.34), "A", "t4", 1, "middle") + tag(LX(0.8), LY(0.08), "B", "t1", 1, "middle");
  o += tag(LX(0.04), LY(0.92), "Gini = A ÷ (A + B) = " + Lib.fmtN(gini, 2), "t1", 1);
  if (s.t) o += tag(LX(0.04), LY(0.82), s.t, "t2");
  return o;
}
function lorenzOnly(k) { return lorenzDraw({ k }); }
$("#pic1").innerHTML = `<svg viewBox="0 0 760 360" role="img" aria-label="Lorenz curve with the line of equality and the Gini coefficient formula, next to a line showing the Kuznets curve"><g>${lorenzDraw({ k: 2 })}</g>
  <g>${axes(430, 310, 740, 40, "Income per head", "Inequality") + SV.path("M 440 280 Q 560 40 725 270", "c2") + SV.circle(500, 156, 6, "dot2") + tag(510, 140, "industrialising: inequality rises", "t2") + SV.circle(660, 188, 6, "dot3") + tag(660, 172, "rich: inequality falls", "t3", 1, "middle") + tag(585, 60, "Kuznets curve", "t1", 1, "middle")}</g></svg>`;
Lib.stepper($("#stL"), { w: 400, h: 340, label: "Lorenz curve showing unequal growth and inclusive growth", base: { k: 2, t: "" }, draw: lorenzDraw, tween: 1100, dwell: 5600, steps: [
  { cap: "<b>Starting point.</b> The Lorenz curve shows the share of income held by each share of households. The further it bows from the line of equality, the greater the inequality. Here Gini is about 0.33.", s: { k: 2 } },
  { cap: "<b>Growth that is not inclusive.</b> GDP per head rises, but most of the gain goes to the top. The curve bows further from equality and the <b>Gini rises</b> to about 0.43, even though average income is higher.", s: { k: 2.5, t: "Gini up: gains concentrated" } },
  { cap: "<b>Inclusive growth.</b> Growth is accompanied by education, training, a progressive tax and better access for poorer households. The curve moves <b>towards</b> the line of equality and the Gini falls to about 0.2.", s: { k: 1.5, t: "Gini down: gains shared" } },
] });

/* ---------- Watch 2: Kuznets ---------- */
function kzDraw(s) {
  const KX = (x) => 70 + x * 650, KY = (x) => 280 - 220 * Math.sin(Math.PI * x) ** 1.0;
  const pts = []; for (let x = 0; x <= s.p + 1e-9; x += 0.01) pts.push([KX(x), KY(x)]);
  let o = axes(70, 300, 740, 30, "Income per head", "Inequality") + SV.path(Lib.ptsPath(pts), "c2") + SV.circle(KX(s.p), KY(s.p), 7, "dot4");
  if (s.l) o += tag(KX(s.p) + 12, KY(s.p) - 12, s.l, "t4");
  return o;
}
Lib.stepper($("#stK"), { w: 760, h: 330, label: "Kuznets curve traced from a poor agricultural economy through industrialisation to a rich economy", base: { p: 0.02, l: "" }, draw: kzDraw, tween: 1300, dwell: 5600, steps: [
  { cap: "<b>Poor, mainly agricultural.</b> Most people are poor, so income is fairly equally (poorly) shared and inequality is low.", s: { p: 0.03, l: "agricultural" } },
  { cap: "<b>Industrialising.</b> Some workers move into higher-paid city jobs and capital owners gain. Average income rises but <b>inequality rises</b> too.", s: { p: 0.3, l: "industrialising" } },
  { cap: "<b>The turning point.</b> Inequality peaks. Schooling spreads, labour becomes scarcer and the government can afford benefits and progressive taxes.", s: { p: 0.5, l: "turning point" } },
  { cap: "<b>Rich economy.</b> On this view inequality <b>falls</b> as income per head keeps rising. In reality the pattern is not automatic, and several rich countries have seen inequality rise again since the 1980s.", s: { p: 0.9, l: "rich economy" } },
] });

/* ---------- Lab 1: who gains ---------- */
function labShare() {
  if (!$("#gr") || !$("#sb") || !$("#st")) return;
  const g = +$("#gr").value / 100, sb = Math.min(+$("#sb").value, 100 - +$("#st").value) / 100, st = +$("#st").value / 100, sm = 1 - sb - st;
  const base = { b: 15, m: 50, t: 35 }, total = 100, extra = total * g;
  const gb = base.b ? extra * sb / base.b * 100 : 0, gm = extra * sm / base.m * 100, gt = extra * st / base.t * 100;
  const shareB = (base.b + extra * sb) / (total + extra) * 100;
  $("#r1").textContent = Lib.fmtN(gb, 1) + "%"; $("#r2").textContent = Lib.fmtN(gt, 1) + "%"; $("#r3").textContent = Lib.fmtN(shareB, 1) + "%";
  const avg = g * 100;
  $("#rv").textContent = gb >= avg ? `The bottom 40% gain ${Lib.fmtN(gb, 1)}%, at least as fast as the ${Lib.fmtN(avg, 1)}% average, so their share rises. This growth is inclusive.` : `The bottom 40% gain ${Lib.fmtN(gb, 1)}%, slower than the ${Lib.fmtN(avg, 1)}% average, so their share falls from 15% to ${Lib.fmtN(shareB, 1)}%. Incomes rise for all but inequality widens: growth is not inclusive.`;
  const mx = Math.max(gb, gm, gt, avg, 1) * 1.15, y = (v) => 250 - v / mx * 210;
  const bars = [["Bottom 40%", gb, "f3", "t3"], ["Middle 50%", gm, "f1", "t1"], ["Top 10%", gt, "f4", "t4"]];
  let o = SV.line(40, 250, 400, 250) + SV.line(40, y(avg), 400, y(avg), "c2 dash") + tag(396, y(avg) - 6, "average " + Lib.fmtN(avg, 1) + "%", "t2", 1, "end");
  bars.forEach((b, i) => { const x = 70 + i * 110; o += SV.rect(x, y(b[1]), 80, 250 - y(b[1]), b[2]) + tag(x + 40, y(b[1]) - 6, Lib.fmtN(b[1], 1) + "%", b[3], 1, "middle") + SV.text(x + 40, 270, b[0], "sm bd", { "text-anchor": "middle" }); });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "gr", label: "Growth in total income (%) ", min: 1, max: 10, step: 1, value: 5, fmt: (v) => v, onInput: labShare });
Lib.slider($("#g2"), { id: "sb", label: "Share of extra income to bottom 40% (%) ", min: 0, max: 60, step: 5, value: 10, fmt: (v) => v, onInput: labShare });
Lib.slider($("#g3"), { id: "st", label: "Share of extra income to top 10% (%) ", min: 0, max: 80, step: 5, value: 50, fmt: (v) => v, onInput: labShare });
labShare();
btnTable("lbBtns", "lbOut", [
  ["Progressive income tax and benefits", "Fiscal", "Takes a larger share from high earners and pays benefits to low earners", "Weaker incentives, cost, targeting"],
  ["Education and training", "Supply-side", "Raises skills and earning power of poorer households", "Slow, costly, may not match jobs"],
  ["Infrastructure in poorer regions", "Supply-side", "Connects remote areas to jobs and markets", "High cost, benefits take years"],
  ["National minimum wage", "Labour market", "Raises pay at the bottom immediately", "May cut jobs if set too high"],
  ["Access to credit and small-firm support", "Supply-side", "Lets poorer people start and grow businesses", "Defaults, hard to target"],
  ["Anti-discrimination laws", "Regulation", "Widens participation by women and minorities", "Hard to enforce"]
], ["Policy", "Type", "How it promotes inclusion", "Weakness"]);

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Does the change make growth more inclusive or less inclusive?", buckets: [{"label": "More inclusive"}, {"label": "Less inclusive"}], items: [{"text": "Free schooling for children in poor regions", "b": 0}, {"text": "Gains from growth go mainly to owners of capital", "b": 1}, {"text": "Introduction of a minimum wage that raises low pay", "b": 0}, {"text": "Growth concentrated in a single capital city", "b": 1}, {"text": "Mobile banking opens finance to poor households", "b": 0}, {"text": "Cuts in benefits while top tax rates are cut", "b": 1}, {"text": "Training schemes for workers whose jobs are automated", "b": 0}, {"text": "Rising Gini coefficient while GDP per head rises", "b": 1}], done: "Inclusive growth shares the gains and widens participation." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Inclusive growth", "Growth whose benefits are widely shared and open to all groups"], ["Gini coefficient", "Measure of inequality from 0 (equal) to 1 (unequal)"], ["Kuznets curve", "Inverted U between income per head and inequality"], ["Equity", "A fair distribution of income, not necessarily equal"], ["Absolute poverty", "Income below a fixed minimum for basic needs"], ["Relative poverty", "Income well below the national average"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the Kuznets curve story in order.", items: ["A poor economy is mainly agricultural, with low inequality", "Workers move to higher-paid industrial jobs and inequality rises", "Inequality reaches a peak at the turning point", "Education spreads and the state expands welfare", "Inequality falls as income per head keeps rising"], done: "The inverted U is a tendency, not a certainty." });
Lib.calc($("#c1"), { qs: [
  {"q": "The poorest 40% of households have a total income of $150bn. Over a year their income rises to $160bn. Calculate the percentage growth in their income.", "a": 6.7, "unit": "%", "tol": 0.1, "hint": "Change ÷ original × 100.", "sol": "10 ÷ 150 × 100 = <b>6.7%</b> (one decimal place)."},
  {"q": "Area A (between the line of equality and the Lorenz curve) is 0.12 and area B (below the Lorenz curve) is 0.38. Calculate the Gini coefficient.", "a": 0.24, "tol": 0.005, "hint": "Gini = A ÷ (A + B).", "sol": "0.12 ÷ (0.12 + 0.38) = 0.12 ÷ 0.50 = <b>0.24</b>."},
  {"q": "National income is $1,000bn and the richest 10% receive $350bn. Over the year income grows by 6% and the richest 10% receive 60% of the extra income. Calculate the richest 10%'s new share of income (percentage, one decimal place).", "a": 36.4, "unit": "%", "tol": 0.1, "hint": "Extra income = 60. Richest get 36 of it.", "sol": "Extra = $60bn. Richest receive 0.6 × 60 = $36bn, so $386bn of $1,060bn = <b>36.4%</b>."},
  {"q": "A country's average income rises 4%. The bottom 40% see their income rise 7%. Is growth inclusive by the 'bottom 40% grow at least as fast as average' test? Type 1 for yes and 0 for no.", "a": 1, "tol": 0.01, "hint": "Compare 7% with 4%.", "sol": "The bottom 40% grew faster than average, so their share rises: <b>yes (1)</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which statement about inclusive growth is correct?", opts: ["It is the same as rapid GDP growth", "It requires the gains from growth to be widely shared", "It means everyone's income is equal", "It is only about reducing absolute poverty"], a: 1, why: "Inclusive growth is about who benefits and who can take part, not just the size of GDP." },
  { q: "A country's GDP per head rises 5% and the Gini coefficient also rises. What does this suggest?", opts: ["Growth has been inclusive", "Growth has probably widened inequality", "Absolute poverty must have risen", "Income is now equally distributed"], a: 1, why: "A rising Gini means income is less equally distributed even though average income has risen." },
  { q: "Which policy is a supply-side way of making growth more inclusive?", opts: ["A cut in the top rate of income tax", "Free vocational training for low-income workers", "A rise in indirect taxes", "A fall in benefits"], a: 1, why: "Training raises skills and earnings of poorer households. The other three do not raise their productivity." },
  { q: "What is the main objection to high marginal tax rates as a way to promote inclusive growth?", opts: ["They always cut tax revenue", "They may weaken the incentive to work and invest", "They have no effect on income distribution", "They reduce the Gini coefficient too slowly"], a: 1, why: "The equity-efficiency trade-off: higher tax rates may reduce effort, saving and investment." },
  { q: "On the Kuznets curve, what happens to inequality at the earliest stage of industrialisation?", opts: ["It falls", "It rises", "It stays constant", "It becomes zero"], a: 1, why: "On the rising part of the inverted U, inequality increases as some workers move to higher-paid jobs." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Inclusive growth", "Growth with widely shared benefits and wide participation."],
  ["Equality", "Equal shares of income or wealth."],
  ["Equity", "A fair distribution, not necessarily equal."],
  ["Gini coefficient", "A ÷ (A + B) on a Lorenz diagram: 0 equal, 1 unequal."],
  ["Lorenz curve", "Cumulative share of income against cumulative share of households."],
  ["Kuznets curve", "Inequality rises then falls as income per head rises."],
  ["Absolute poverty", "Income below a fixed minimum for basic needs."],
  ["Relative poverty", "Income below a fraction of the national average."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "What does the Kuznets curve show? (May/June 2022 · 31 · Q20, reworded)", opts: ["A rise then fall in the balance of trade deficit after a devaluation", "A rise then fall in the economic growth rate as GDP rises", "A rise then fall in inequality as income per head rises", "A rise then fall in tax revenue as the tax rate rises"], a: 2, why: "Kuznets proposed an inverted U between income per head and inequality." },
  { q: "The turning point on the Kuznets curve is estimated at about $10,500 of income per head. For a country with $8,000 per head, what is most likely? (Oct/Nov 2023 · 31 · Q30, reworded)", opts: ["A fall in income per head would have no effect on inequality", "A fall in income per head would increase inequality", "A rise in income per head would have no effect on inequality", "A rise in income per head would increase inequality"], a: 3, why: "To the left of the turning point, growth is on the rising part of the inverted U, so inequality tends to rise." },
  { q: "On a Lorenz diagram area X lies between the line of perfect equality and the Lorenz curve, and Y lies under the curve. How is the Gini coefficient calculated? (May/June 2023 · 31 · Q30, reworded)", opts: ["X ÷ (X + Y)", "(X + Y) ÷ X", "(X + Y) ÷ Y", "Y ÷ (X + Y)"], a: 0, why: "Gini is the area between the curves as a share of the whole triangle under the line of equality." },
  { q: "Which change in the Gini coefficient suggests a country is distributing income more equally? (Oct/Nov 2023 · 32 · Q27, reworded)", opts: ["A move closer to 1", "A move closer to 0", "A move from negative to positive", "A move from positive to negative"], a: 1, why: "A Gini of 0 means perfect equality, so a fall means more equal." },
  { q: "Which fiscal changes would be most effective in reducing income inequality? (Oct/Nov 2023 · 32 · Q13, reworded)", opts: ["Raise top income tax, raise indirect taxes, cut state benefits", "Raise top income tax, cut indirect taxes, raise state benefits", "Cut top income tax, raise indirect taxes, cut state benefits", "Cut top income tax, cut indirect taxes, cut state benefits"], a: 1, why: "Progressive direct taxes and higher benefits redistribute towards the poor, and lower indirect taxes reduce the burden on the poor." },
  { q: "Which policy could reduce income inequality in the short run in a country with high inequality? (Oct/Nov 2024 · 32 · Q15, reworded)", opts: ["A higher sales tax on luxury goods", "A minimum wage", "Heavy investment in schools", "Skills and productivity training to stimulate growth"], a: 1, why: "A minimum wage lifts low pay straight away. Education and training work over many years." },
  { q: "What is likely to cause a more equal distribution of income in the long run? (May/June 2023 · 32 · Q15, reworded)", opts: ["A cut in the top rate of tax", "More government spending on education and training", "A rise in unemployment", "Privatising the education sector"], a: 1, why: "Better skills raise the earning power of poorer households over time." },
] });
