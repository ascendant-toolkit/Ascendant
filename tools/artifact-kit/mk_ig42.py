"""Builds the six IGCSE Economics 4.2 Fiscal policy reviews (4.2.1 to 4.2.6) from slices of fisc.* plus new content.
Run: python3 tools/artifact-kit/mk_ig42.py   (then assemble.py for each, done here via write())"""
from igsy import *
F = Old("fisc")
HEAD = F.j_((2, 26))
CL = lambda t: f"IGCSE Economics · 0455 · {t}"

# shared AD/AS helpers for pages that need the diagram without the stepper (fisc.js 139-160)
ADFN = F.j_((139, 160))

# =========================================================== 4.2.1 Government budget
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>A government plans each year how much it will <b>spend</b> and how much it expects to <b>raise</b>, mainly through taxes. That plan is the <span class="kw">government budget</span>. The gap between the two is the <b>budget deficit</b> or <b>budget surplus</b>, and it tells you whether the government has to borrow. Everything else in fiscal policy shows up here first.</p></div>
''' + F.b((25, 33)) + '''
  <h2>Calculating a budget position</h2>
  <p>Work in three steps: add up all revenue, add up all spending, then subtract. Show each total and say whether the answer is a deficit or a surplus.</p>
  <div class="tw"><table class="t">
    <tr><th>Item</th><th>$bn</th></tr>
    <tr><td>Income tax</td><td>40</td></tr><tr><td>Sales tax</td><td>25</td></tr><tr><td>Other revenue</td><td>10</td></tr>
    <tr><td><b>Total revenue</b></td><td><b>75</b></td></tr>
    <tr><td>Healthcare and education</td><td>45</td></tr><tr><td>Pensions and benefits</td><td>25</td></tr><tr><td>Other spending</td><td>10</td></tr>
    <tr><td><b>Total spending</b></td><td><b>80</b></td></tr>
  </table></div>
  <p>Budget balance = 75 − 80 = <b>−$5bn</b>, a <b>deficit of $5bn</b>. If GDP is $100bn the deficit is 5% of GDP.</p>
  <h2>Why a budget changes without a new policy</h2>
  <p><span class="kw">Automatic stabilisers</span> are spending and taxes that move with the economy. In a slump, incomes fall so tax revenue falls, and more people claim unemployment benefit, so spending rises: the deficit widens with no new decision. In a boom the opposite happens. They cushion the swings in demand.</p>
  <h2>Why deficits matter</h2>
  <ul>
    <li>A deficit has to be <b>borrowed</b>, so it adds to the national debt.</li>
    <li>Debt means <b>interest payments</b> in future years, which is spending that does not buy new services (an opportunity cost).</li>
    <li>A deficit during a slump can support spending and jobs; a deficit that persists in a boom may be harder to justify.</li>
    <li>A surplus can repay debt, but raising taxes or cutting spending to get one may slow the economy.</li>
  </ul>
'''
explore = F.b((116, 123)) + '''
  <h2>Lab 2 · Deficits build the national debt</h2>
  <p>The national debt starts at $60bn and GDP is $200bn. Set a yearly budget position and a number of years. Negative means a deficit.</p>
  <div class="card"><div class="grid2"><div><div id="g9"></div><div id="g10"></div></div>
    <div><div class="readout"><div><small>National debt at the end</small><strong id="da1"></strong></div><div><small>Change since the start</small><strong id="da2"></strong></div><div><small>Debt as % of GDP</small><strong id="da3"></strong></div></div><div class="verdict" id="dav"></div></div></div>
    <svg id="labD" viewBox="0 0 760 360" role="img" aria-label="National debt each year"></svg>
    <p class="note">Simplified: GDP stays at $200bn and debt interest is ignored, to show that deficits add to the debt and surpluses reduce it.</p>
  </div>'''
labd = '''
function labD() {
  if (!$("#da") || !$("#db")) return;
  const bal = +$("#da").value, n = +$("#db").value, d0 = 60, GDP = 200;
  const debt = [d0]; for (let i = 1; i <= n; i++) debt.push(Math.max(0, debt[i - 1] - bal));
  const end = debt[n];
  $("#da1").textContent = "$" + money(end, 0) + "bn"; $("#da2").textContent = (end - d0 >= 0 ? "+" : "−") + "$" + money(Math.abs(end - d0), 0) + "bn"; $("#da3").textContent = money((end / GDP) * 100, 1) + "%";
  $("#dav").textContent = bal < 0 ? `A deficit of $${-bal}bn a year is borrowed every year, so the debt rises by $${-bal * n}bn over ${n} years. The debt is the running total of past deficits.` : bal > 0 ? `A surplus of $${bal}bn a year can repay debt, so the debt falls (it cannot go below zero).` : "A balanced budget leaves the debt unchanged: no new borrowing is needed.";
  const base = 320, mx = Math.max(100, ...debt), k = 250 / mx, w = Math.min(54, 600 / (n + 1)), gap = w * 0.25;
  let o = SV.line(40, base, 730, base);
  debt.forEach((v, i) => {
    const x = 50 + i * (w + gap);
    o += SV.rect(x, base - v * k, w, v * k, "", { style: "fill:var(--bad)", opacity: 0.6 }) + SV.text(x + w / 2, base - v * k - 6, money(v, 0), "sm bd", { "text-anchor": "middle" }) + SV.text(x + w / 2, base + 18, i ? "Yr " + i : "Now", "sm", { "text-anchor": "middle" });
  });
  $("#labD").innerHTML = o + SV.text(40, 24, "National debt ($bn)", "sm");
}
Lib.slider($("#g9"), { id: "da", label: "Budget position each year", min: -30, max: 30, step: 5, value: -10, fmt: (v) => (v < 0 ? "deficit $" + -v : v > 0 ? "surplus $" + v : "balanced") + (v ? "bn" : ""), onInput: labD });
Lib.slider($("#g10"), { id: "db", label: "Number of years", min: 1, max: 10, step: 1, value: 5, fmt: (v) => v + " years", onInput: labD });
'''
js = HEAD + F.j_((28, 52)) + F.j_((168, 200)) + labd + '''
/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Deficit, surplus or balanced? Revenue first, spending second.", buckets: [{ label: "Budget deficit" }, { label: "Budget surplus" }, { label: "Balanced budget" }], items: [
  { text: "Revenue $90bn, spending $100bn", b: 0 }, { text: "Revenue $52bn, spending $60bn", b: 0 }, { text: "Revenue $120bn, spending $110bn", b: 1 }, { text: "Revenue $75bn, spending $70bn", b: 1 },
  { text: "Revenue $80bn, spending $80bn", b: 2 }, { text: "Spending is higher than revenue, so the government borrows", b: 0 }, { text: "Revenue exceeds spending, so debt can be repaid", b: 1 }, { text: "Spending and revenue are equal", b: 2 },
], done: "Compare revenue with spending: whichever is higher decides it." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Government budget", "A plan of what the government expects to raise and spend"],
  ["Budget deficit", "Government spending is higher than revenue"],
  ["Budget surplus", "Government revenue is higher than spending"],
  ["Balanced budget", "Government spending and revenue are equal"],
  ["National debt", "Total amount the government has borrowed over time"],
  ["Automatic stabilisers", "Spending and taxes that change with the economy without a new policy"],
], done: "Good vocabulary scores marks." });
Lib.order($("#o1"), { prompt: "Put the steps in order: how a <b>recession</b> widens the deficit with no change in policy.", items: [
  "The economy slows and firms lay off workers",
  "Household incomes and spending fall",
  "Income tax and sales tax revenue fall",
  "More people claim unemployment benefit, so spending rises",
  "Spending rises while revenue falls: the budget deficit widens",
  "The government borrows more, adding to the national debt",
], done: "That is how automatic stabilisers work." });
''' + calc_js([], F.jl(301, 302, 303, 304, 305)) + mcq_js("qz1", [
    ("What is a budget deficit?", ["Revenue is higher than spending", "Spending is higher than revenue", "The total amount borrowed over time", "Revenue and spending are equal"], 1, "A deficit means the government spends more than it raises in that period."),
    ("A government has revenue of $60bn and spending of $68bn. What is its budget position?", ["Surplus of $8bn", "Surplus of $128bn", "Deficit of $8bn", "Balanced"], 2, "60 − 68 = −8: a deficit of $8bn."),
    ("What is the national debt?", ["The yearly budget deficit", "The total the government has borrowed over time", "Spending on imports", "The gap between exports and imports"], 1, "Deficits add to the debt each year; the debt is the running total."),
    ("A recession is likely to cause the deficit to:", ["Narrow, as tax revenue rises", "Widen, as tax revenue falls and benefit spending rises", "Disappear", "Stay unchanged whatever the government does"], 1, "Automatic stabilisers move the budget towards deficit in a slump."),
    ("Which is most likely to happen if a government runs a budget surplus?", ["It has to borrow more", "It can repay some debt", "The national debt must rise", "Taxes must fall"], 1, "A surplus gives spare money which can repay debt."),
    ("Which is an opportunity cost of a large national debt?", ["Higher interest payments each year", "Larger tax revenues", "Fewer imports", "More workers employed"], 0, "Interest on the debt uses money that could have paid for services."),
]) + "\n" + cards_js(pick_cards(F, ["Budget", "Budget deficit", "Budget surplus", "Balanced budget", "National debt", "Automatic stabilisers", "Tax burden"]) + [("Government budget", "A plan of what the government expects to raise in revenue and spend over a year."), ("Borrowing", "Money a government raises, usually by selling bonds, to cover a deficit.")]) + "labA(); labD();\n"
ex = exam(
    Q(1, "Define", 2, "What is meant by a budget deficit?", "Two ideas: spending is higher than revenue, and it has to be borrowed (or funded from savings).",
      "[K|A budget deficit is when a government's spending is higher than its revenue in a period,] [K|so it has to borrow the difference.]"),
    F.b((204, 210)) .replace('<details class="eq"><summary>Q2', '<details class="eq"><summary>Q2'),
    Q(3, "Explain", 4, "Explain two reasons why a government may have a budget deficit.", "Two reasons, each with a link. Good pairs: recession (revenue falls, benefits rise), extra spending on services or stimulus, tax cuts, debt interest.",
      "[K|One reason is a recession.] [N|Incomes and spending fall, so tax revenue falls, and more people claim unemployment benefit, so government spending rises. The gap between spending and revenue could widen.] [K|A second reason is a decision to raise spending, for example on healthcare or infrastructure,] [N|without raising taxes by as much, which means spending exceeds revenue and the government may borrow the difference.]"),
    Q(4, "Discuss", 8, "Discuss whether or not a government should always aim for a balanced budget.", "Two sides and a judgement. For: debt and interest costs, fairness to future taxpayers. Against: deficits can support jobs in a slump, borrowing to invest can raise future growth. End with 'it depends on…'.",
      "[K|A balanced budget is where government spending equals revenue, so no new borrowing is needed.] [N|Aiming for one could help to keep the national debt under control, which limits interest payments and leaves more of future tax revenue for services.] [N|Lenders may also trust a government that does not keep borrowing, which could keep its borrowing costs low.] [E|However, these benefits may be smaller if the debt is already small compared with GDP.] [N|On the other hand, an insistence on balance could force spending cuts or tax rises in a recession, which are likely to reduce aggregate demand, raise unemployment and cut tax revenue further.] [N|Borrowing to build roads, schools or hospitals may raise productivity and output, so that future revenue could rise.] [E|Overall, a government is more likely to benefit from balancing the budget over the economic cycle, running deficits in slumps and surpluses in booms, rather than every year. The best approach depends on the size of the existing debt, the state of the economy and what the borrowing is used for.]", key=True),
)
tp = tips([
    ("Budget balance = revenue − spending.", "A negative answer is a deficit; a positive answer is a surplus."),
    ("Deficit is a yearly flow; national debt is the running total.", "Deficits add to the debt."),
    ("Show your totals.", "Add the revenue column and the spending column before you subtract."),
    ("A recession widens the deficit by itself.", "Tax revenue falls and benefit spending rises: automatic stabilisers."),
    ("Give a cost of borrowing.", "Interest payments are an opportunity cost: money not spent on services."),
    ("Use hedged words.", "A deficit 'could' raise the debt; spending 'may' support jobs."),
], cmds("Define", "Calculate", "Explain", "Discuss"))
body = page(CL("4.2.1 Government budget"), "Government Budget", "What a government budget is, how to calculate a deficit or surplus, and how borrowing builds the national debt. Syllabus 4.2.1.",
    learn=learn, watch=watch(("Budget deficit, surplus and national debt", "stB")), explore=explore,
    practise=practise(("Deficit, surplus or balanced?", "cl1", "card"), ("Match the term", "m1", "card"), ("Order the recession chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(F.b((181, 181)), F.b((186, 186)), F.b((188, 188)), F.b((187, 187))), exam=ex, tips=tp)
write("fb1", body, js, "Government Budget", "ig-fiscal-budget")

# =========================================================== 4.2.2 Reasons for government spending
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>Governments spend for four main reasons: to <b>influence economic activity</b>, to <b>reduce market failure</b>, to <b>promote equity</b> and to <b>pay interest on the national debt</b>. Spending is a powerful tool because of the <b>multiplier effect</b>: each dollar spent is passed on as income to others, so total demand rises by more than the first injection.</p></div>

  <h2>The four reasons</h2>
  <div class="grid2">
    <div class="card"><h3>Influence economic activity</h3><p>More spending raises G, a part of AD, which could increase output, growth and employment. Less spending can cool an overheating economy.</p></div>
    <div class="card"><h3>Reduce market failure</h3><p>Public goods (defence, street lighting) will not be provided by private firms. Merit goods (education, healthcare) would be under-provided. Spending can also pay for regulators and environmental protection.</p></div>
    <div class="card"><h3>Promote equity</h3><p>Pensions, unemployment benefit, housing support and free schooling help people on low incomes and could reduce inequality.</p></div>
    <div class="card"><h3>Pay interest on debt</h3><p>Earlier borrowing has to be paid for each year. This spending buys no new services, which is why a large debt has an opportunity cost.</p></div>
  </div>

  <h2>Main areas of spending: reasons and effects</h2>
  <div class="tw"><table class="t">
    <tr><th>Area</th><th>Why governments spend on it</th><th>Possible effects</th></tr>
    <tr><td><b>Healthcare</b></td><td>Merit good; healthier workers; equity of access</td><td>Higher productivity and life expectancy; large cost as populations age</td></tr>
    <tr><td><b>Education</b></td><td>Merit good; skills for the workforce</td><td>Could raise productivity and long-run growth; benefits take years to appear</td></tr>
    <tr><td><b>Pensions and benefits</b></td><td>Equity; support for the old, sick and unemployed</td><td>Supports spending in a slump; may reduce the incentive to work if too generous</td></tr>
    <tr><td><b>Defence and law and order</b></td><td>Public goods; protect people and property</td><td>Secure conditions for business; high opportunity cost</td></tr>
    <tr><td><b>Infrastructure</b></td><td>Roads, rail, broadband that private firms may not build</td><td>Creates jobs now and lowers firms' costs later, which may raise AS</td></tr>
    <tr><td><b>Debt interest</b></td><td>Pays for past borrowing</td><td>Uses revenue that could fund services</td></tr>
  </table></div>

  <h2>The multiplier effect</h2>
''' + F.b((42, 42)) + '''
  <div class="formula">Multiplier = 1 ÷ (1 − share of extra income spent) &nbsp;·&nbsp; Total change in income = initial injection × multiplier</div>
  <p>The more people <b>save</b>, <b>pay in tax</b> or <b>spend on imports</b> out of extra income, the smaller each round and the smaller the multiplier. These are the leakages.</p>
  <h2>Evaluating spending</h2>
  <ul>
    <li><b>Opportunity cost:</b> money spent on one area cannot be spent on another.</li>
    <li><b>Time lags:</b> building a hospital or training teachers takes years.</li>
    <li><b>Borrowing:</b> if spending is not funded by tax, the deficit and debt interest rise.</li>
    <li><b>Spare capacity:</b> if the economy is already close to full capacity, extra spending could mostly raise prices.</li>
  </ul>
'''
# new stepper: spending on education, short run AD then long run AS
newjs = '''
/* education spending: AD rises now, AS later */
function solve2(sh, a) {
  const c = 90 + 0.8 * sh; let y = (c - 30 + 0.4 * a) / 1.2;
  if (y - a > 60) y = (c + 78 + 2.2 * a) / 3;
  return [y, c - 0.8 * y, c];
}
function adasChart(s) {
  const sh = s.sh, a = s.a, [y1, p1, c] = solve2(sh, a), movedAD = Math.abs(sh) >= 1, movedAS = a >= 1;
  const pts = (x) => [[QX(x), PY(30)], [QX(60 + x), PY(54)], [QX(87.7 + x), PY(115)]];
  let o = axes("Price level", "Real GDP");
  if (movedAS) o += SV.path(ptsPath(pts(0)), "c3", { opacity: 0.4 });
  o += SV.path(ptsPath(pts(a)), "c3") + SV.text(QX(87.7 + a) + 6, PY(115) + 4, movedAS ? "AS₁" : "AS", "lbl bd t3");
  o += adLine(90, "c1", "AD", { t: "t1", attrs: { opacity: movedAD ? 0.4 : 1 } });
  if (movedAD) o += adLine(c, "c2", "AD₁", { t: "t2" });
  o += hline(50) + vline(50, 50) + ylab(50, "P") + xlab(50, "Y") + SV.circle(QX(50), PY(50), 6, "dot1", { opacity: movedAD || movedAS ? 0.45 : 1 });
  if (movedAD || movedAS) o += hline(p1, "gr", y1) + vline(y1, p1) + SV.circle(QX(y1), PY(p1), 6, "dot2") + ylab(p1, "P₁", "sm bd") + xlab(y1, "Y₁", "sm bd");
  return o;
}
Lib.stepper($("#stE"), { w: 760, h: 400, label: "Spending on education: short-run and long-run effects", base: { sh: 0, a: 0 }, draw: adasChart, steps: [
  { cap: "The economy starts at <b>Y</b> and <b>P</b>. The government decides to spend more on <b>education</b>.", s: { sh: 0, a: 0 } },
  { cap: "In the <b>short run</b> the spending is part of <b>G</b>. Builders and teachers are paid and spend their pay, so <b>AD shifts right</b> to AD₁. Real GDP and jobs rise, and the price level edges up.", s: { sh: 22, a: 0 } },
  { cap: "In the <b>long run</b> the workforce is better skilled and more productive. The economy can produce more at each price level, so <b>AS shifts right</b> to AS₁. Output is higher and the price level lower than AD alone would give.", s: { sh: 22, a: 14 } },
  { cap: "<b>Evaluate:</b> the supply effect takes years, the money has an <b>opportunity cost</b> (it could have been spent elsewhere) and it only works if the education is of good quality and leads to jobs.", s: { sh: 22, a: 14 } },
] });

/* spending scorecard */
const SP = [
  { n: "Healthcare", why: "Merit good: a healthier workforce, fairer access to treatment.", ad: "Pays staff and suppliers, so AD could rise quickly.", lr: "Fewer days lost to illness: productivity may rise.", cost: "Large and rising cost, especially as populations age." },
  { n: "Education", why: "Merit good: skills for jobs, equal opportunity.", ad: "Pays teachers and builders: AD could rise.", lr: "A more skilled workforce raises AS and long-run growth.", cost: "Benefits take years to appear; quality matters." },
  { n: "Pensions and benefits", why: "Equity: income for the old, the sick and the unemployed.", ad: "Recipients spend most of it, so AD could rise, and benefits rise automatically in a slump.", lr: "Little direct effect on AS.", cost: "Can be costly; may reduce the incentive to work if too generous." },
  { n: "Infrastructure", why: "Roads, rail and broadband that private firms may not build.", ad: "Construction jobs and orders raise AD.", lr: "Lower costs and faster transport can raise AS.", cost: "Large projects, long delays, and money borrowed to build them has to be repaid." },
  { n: "Defence and law and order", why: "Public goods that markets will not supply.", ad: "Pays soldiers, police and suppliers.", lr: "Security helps firms and investors.", cost: "High opportunity cost: the money could go to other areas." },
];
function showSP(i) {
  const p = SP[i];
  $("#spBtns").innerHTML = SP.map((q, j) => `<button class="b${j === i ? " pri" : ""}" data-j="${j}">${q.n}</button>`).join("");
  $$("#spBtns .b").forEach((b) => (b.onclick = () => showSP(+b.dataset.j)));
  $("#spOut").innerHTML = `<div class="tw"><table class="t"><tr><th>Why spend</th><th>Short run: effect on AD</th><th>Long run</th><th>Cost or limit</th></tr><tr><td>${p.why}</td><td>${p.ad}</td><td>${p.lr}</td><td>${p.cost}</td></tr></table></div>`;
}
showSP(0);
'''
explore = F.b((124, 130)).replace('Lab 2 · The multiplier', 'Lab 1 · The multiplier') + '''
  <h2>Lab 2 · Where does the money go?</h2>
  <p>Pick an area of spending to see why governments spend there and what it might do.</p>
  <div class="card"><div class="row" id="spBtns"></div><div id="spOut"></div></div>
'''
js = HEAD + ADFN + F.j_((53, 78)) + newjs + F.j_((201, 211)) + '''
/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Which <b>reason for government spending</b> fits each example?", buckets: [{ label: "Influence economic activity" }, { label: "Reduce market failure" }, { label: "Promote equity" }, { label: "Pay debt interest" }], items: [
  { text: "A stimulus package of road building during a recession", b: 0 }, { text: "Cutting spending when the economy is overheating", b: 0 },
  { text: "Providing street lighting and national defence", b: 1 }, { text: "Free vaccination (a merit good)", b: 1 },
  { text: "Pensions for older people", b: 2 }, { text: "Housing support for low-income families", b: 2 },
  { text: "Interest on money borrowed in earlier years", b: 3 }, { text: "Repaying part of the national debt", b: 3 },
], done: "Match the reason to the aim behind the spending." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Multiplier effect", "Final change in AD is larger than the initial change"],
  ["Injection", "Money added to the flow of income, such as government spending"],
  ["Leakage", "Money taken out of the flow, such as saving, taxes and imports"],
  ["Merit good", "A good that is under-provided by the market and may be provided by the government"],
  ["Public good", "A good that private firms will not supply because people cannot be excluded"],
  ["Transfer payment", "Benefits paid by the government with no good or service in return"],
], done: "Good vocabulary scores marks." });
''' + F.j_((284, 291)).replace('$("#o1")', '$("#o1")') + '''Lib.order($("#o2"), { prompt: "Put the long-run effect of <b>spending on education</b> in order.", items: [
  "The government raises spending on schools and training",
  "More young people gain skills and qualifications",
  "Workers become more productive",
  "Firms can produce more at each price level: AS shifts right",
  "Output rises and the price level may be lower than otherwise",
  "Future tax revenue could rise as incomes grow",
], done: "A supply-side chain from spending." });
''' + calc_js([
    ("Government spending rises by $50m. People spend 80% of any extra income. Calculate the total rise in income ($m).", 250, "Multiplier = 1 ÷ (1 − 0.8) = 5. Total rise = 5 × 50 = <b>$250m</b>.", "Multiplier = 1 ÷ 0.2.", None),
    ("The multiplier is 4. The government injects $30m. What is the final rise in income ($m)?", 120, "4 × 30 = <b>$120m</b>.", None, None),
    ("People spend 50% of any extra income. What is the multiplier?", 2, "1 ÷ (1 − 0.5) = <b>2</b>.", None, None),
    ("A government spends $15bn on healthcare out of total spending of $75bn. What percentage is spent on healthcare?", 20, "15 ÷ 75 × 100 = <b>20%</b>.", None, None),
], F.jl(307)) + mcq_js("qz1", [
    ("Which is a reason for government spending?", ["To pay interest on the national debt", "To discourage demerit goods", "To protect domestic firms by taxing imports", "To raise the costs of polluters"], 0, "The other three are aims of taxation, not spending."),
    ("Which is an example of a public good the government may provide?", ["Cinema tickets", "National defence", "A restaurant meal", "Mobile phone"], 1, "Defence is non-excludable, so private firms will not supply it."),
    ("What is the multiplier effect?", ["A fall in AD after a tax rise", "The final change in AD being larger than the initial injection", "Spending financed only by tax", "A rise in the deficit"], 1, "Each round of spending creates income for someone else."),
    ("Which would make the multiplier smaller?", ["People spend a larger share of extra income", "People save a larger share of extra income", "Government spending rises", "Firms hire more workers"], 1, "More leakages mean a smaller multiplier."),
    ("Government spending on education is most likely to raise AS in the long run because:", ["Teachers spend their wages", "Workers become more skilled and productive", "It raises the budget deficit", "It reduces imports"], 1, "Productivity rises, so the economy can produce more."),
    ("Which spending is mainly to promote equity?", ["Unemployment benefit", "Road building", "Defence", "Debt interest"], 0, "Benefits redistribute income to people on low incomes."),
]) + "\n" + cards_js([("Government spending", "Money spent by the government on goods, services, benefits and debt interest. Also called G in AD."), ("Multiplier effect", "The final impact on aggregate demand is greater than the initial change."), ("Public good", "A good provided for everyone, which private firms will not supply as non-payers cannot be excluded."), ("Merit good", "A good that people may not value enough, so it is under-provided by the market, such as education and healthcare."), ("Transfer payment", "A payment, such as a pension or benefit, made by the government with nothing received in return."), ("Injection", "Money added to the circular flow, such as government spending."), ("Leakage", "Money taken out of the circular flow: savings, taxes and imports."), ("Opportunity cost", "The next best alternative given up when a choice is made."), ("Infrastructure", "The roads, rail, energy and broadband networks the economy relies on.")]) + "labM(); showSP(0);\n"
ex = exam(
    Q(1, "Define", 2, "What is meant by the multiplier effect?", "Two ideas: an initial change in spending, and a final change in income bigger than that.",
      "[K|The multiplier effect is when an initial injection of spending, such as government spending,] [K|leads to a larger final increase in aggregate demand and national income, as the money is spent and re-spent.]"),
    Q(2, "Explain", 4, "Explain two reasons why a government spends on healthcare.", "Two separate reasons, each developed. Merit good, equity, productivity, market failure.",
      "[K|Healthcare is a merit good that people may under-consume if they have to pay,] [N|so governments provide it to make sure people with low incomes can still receive treatment, which could improve equity.] [K|A second reason is to improve productivity.] [N|Healthier people take fewer sick days and may work more effectively, which could raise output and long-run growth.]"),
    Q(3, "Calculate", 4, "The government increases spending on a new railway by $40m. People spend 75% of any extra income. Calculate the total rise in income.", "Multiplier first, then multiply by the injection. Units.",
      "[A|Multiplier = 1 ÷ (1 − 0.75) = 1 ÷ 0.25 = 4.] [A|Total rise in income = 4 × $40m = $160m.]"),
    Q(4, "Analyse", 6, "Analyse how an increase in government spending on infrastructure could affect an economy.", "Short run (AD, multiplier) then long run (AS). Hedged words. Add the cost for evaluation if you have time.",
      "[K|Infrastructure spending is part of G.] [N|Firms and workers building a road or railway receive income and spend part of it, so aggregate demand could shift right through a multiplier effect.] [N|Real GDP could rise and unemployment fall.] [N|In the longer run, better transport and broadband may lower firms' costs and raise productivity, which could shift aggregate supply right and give growth with less inflationary pressure.] [E|However, it may take years to build and the money has an opportunity cost.]", key=True),
    Q(5, "Discuss", 8, "Discuss whether or not increasing government spending is the best way to reduce unemployment.", "Both sides. For: raises AD, jobs in the projects, multiplier. Against: time lags, deficit, inflation near full capacity, other policies (supply-side) may work better for structural unemployment.",
      "[K|Government spending is a part of AD and can be used to create demand for workers.] [N|If spending on construction or public services rises, firms and public bodies are likely to hire more workers, and the multiplier effect could create further jobs as those workers spend.] [N|It could be particularly effective in a recession with spare capacity.] [E|However, projects can take time to plan, so the effect may arrive late.] [N|The spending may raise the budget deficit and national debt, and if the economy is close to full capacity it could cause inflation.] [N|It may also not help workers whose skills do not match the jobs available, so supply-side measures such as training could do more for those people.] [E|Overall, spending is more likely to help when unemployment is caused by low demand. The best solution depends on the cause of the unemployment and on the state of the economy and public finances.]", key=True),
)
tp = tips([
    ("Four reasons to spend:", "influence activity, reduce market failure, promote equity, pay debt interest."),
    ("Multiplier = 1 ÷ (1 − share spent).", "Then multiply by the injection."),
    ("Name the area of spending.", "Healthcare, education, pensions, infrastructure give you something specific to write about."),
    ("Split short run and long run.", "Spending changes AD at once; education and infrastructure may change AS later."),
    ("Evaluate with opportunity cost, time lags and borrowing.", "And spare capacity: near full capacity, extra spending mostly raises prices."),
], cmds("Define", "Explain", "Calculate", "Analyse", "Discuss"))
body = page(CL("4.2.2 Reasons for government spending"), "Reasons for Government Spending", "Why governments spend, the main areas of spending and their effects, and how the multiplier magnifies an injection. Syllabus 4.2.2.",
    learn=learn, watch=watch(("The multiplier effect", "stM"), ("Spending on education: short run and long run", "stE")), explore=explore,
    practise=practise(("Which reason for spending?", "cl1", "card"), ("Match the term", "m1", "card"), ("Order the multiplier", "o1", "card"), ("Order the education chain", "o2", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(F.b((187, 187)), rw("Spending on health in a pandemic", "During the COVID-19 pandemic many governments sharply raised healthcare spending on hospitals, testing and vaccines, and paid wage support to keep people in work.", "Reason for spending: reduce market failure (a merit good) and influence economic activity. Evaluate with the size of the resulting deficit."), rw("Infrastructure for growth", "Many governments fund roads, rail, ports and broadband. Large projects such as new high-speed rail lines have often cost more and taken longer than first planned.", "Short-run AD effect, long-run AS effect, then evaluate with opportunity cost and time lags."), rw("Large pension bills", "In countries with ageing populations, pensions and healthcare take a growing share of government spending, leaving less for other areas.", "Opportunity cost of spending and why governments may need to raise taxes or borrow more.")), exam=ex, tips=tp)
write("fb2", body, js, "Reasons for Government Spending", "ig-fiscal-spending")

# =========================================================== 4.2.3 Taxation
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>A <span class="kw">tax</span> is a compulsory payment to the government. Governments tax to <b>raise revenue</b> and to achieve other aims such as reducing the consumption of demerit goods or redistributing income. Taxes are classified as <b>direct or indirect</b> and as <b>progressive, proportional or regressive</b>, and each tax affects consumers, workers, firms, the government and the economy differently.</p></div>
''' + F.b((44, 92)) + '''
  <h2>Putting the effects together</h2>
  <div class="tw"><table class="t">
    <tr><th>Who</th><th>Possible impact of higher taxes</th></tr>
    <tr><td><b>Consumers</b></td><td>Lower disposable income (direct taxes) or higher prices (indirect taxes), so spending may fall</td></tr>
    <tr><td><b>Workers</b></td><td>Lower take-home pay, which may reduce the incentive to work longer hours or seek promotion (but not always)</td></tr>
    <tr><td><b>Producers and firms</b></td><td>Higher costs and lower profits; may cut output, investment or jobs, or move abroad</td></tr>
    <tr><td><b>Government</b></td><td>More revenue to spend or repay debt, if the tax base does not shrink</td></tr>
    <tr><td><b>The economy</b></td><td>Lower AD, which can ease inflation but may slow growth; can redistribute income and correct market failures</td></tr>
  </table></div>
'''
explore = F.b((131, 138)).replace('Lab 3 · Three tax systems', 'Lab 1 · Three tax systems') + '''
  <h2>Lab 2 · Who pays an indirect tax?</h2>
  <p>A tax of 20 is put on a good. Change how responsive demand and supply are and see who bears the burden.</p>
  <div class="card"><div class="grid2"><div><div id="g11"></div><div id="g12"></div></div>
    <div><div class="readout"><div><small>Price rises by</small><strong id="ta1"></strong></div><div><small>Consumers bear</small><strong id="ta2"></strong></div><div><small>Producers bear</small><strong id="ta3"></strong></div><div><small>Tax revenue</small><strong id="ta4"></strong></div></div><div class="verdict" id="tav"></div></div></div>
    <svg id="labT" viewBox="0 0 760 400" role="img" aria-label="Incidence of an indirect tax"></svg>
  </div>'''
labt = '''
function labT() {
  if (!$("#ta") || !$("#tb")) return;
  const b = +$("#ta").value, d = +$("#tb").value, t = 20, q1 = 50 - t / (b + d), pc = 50 + (b * t) / (b + d), cs = pc - 50, ps = 50 - (pc - t);
  $("#ta1").textContent = money(cs); $("#ta2").textContent = money((cs / t) * 100, 0) + "% (" + money(cs) + ")"; $("#ta3").textContent = money((ps / t) * 100, 0) + "% (" + money(ps) + ")"; $("#ta4").textContent = money(t * q1, 0);
  $("#tav").textContent = cs > ps + 1 ? "Demand is steep relative to supply (inelastic): buyers keep buying, so firms pass on most of the tax. Consumers bear the greater share." : ps > cs + 1 ? "Demand is flat relative to supply (elastic): buyers would switch away, so firms absorb most of the tax. Producers bear the greater share." : "Demand and supply are similarly responsive, so the burden is shared about equally.";
  $("#labT").innerHTML = taxChart({ b, d, t, inc: 1 });
}
Lib.slider($("#g11"), { id: "ta", label: "Demand steepness (higher = more inelastic)", min: 0.3, max: 3, step: 0.1, value: 1, fmt: (v) => v.toFixed(1) + " " + fmtSteep(v), onInput: labT });
Lib.slider($("#g12"), { id: "tb", label: "Supply steepness (higher = more inelastic)", min: 0.3, max: 3, step: 0.1, value: 1, fmt: (v) => v.toFixed(1) + " " + fmtSteep(v), onInput: labT });
'''
js = HEAD + F.j_((79, 137)) + F.j_((212, 235)) + labt + '''
/* ================= PRACTISE ================= */
''' + F.j_((253, 262)) + F.j_((267, 274)) + '''Lib.classify($("#cl3"), { prompt: "Which <b>reason for taxation</b> fits each tax?", buckets: [{ label: "Raise revenue" }, { label: "Discourage demerit goods" }, { label: "Redistribute income" }, { label: "Protect environment or reduce imports" }], items: [
  { text: "Income tax paid by almost every worker", b: 0 }, { text: "VAT on most goods", b: 0 },
  { text: "Excise duty on cigarettes", b: 1 }, { text: "A high tax on alcohol", b: 1 },
  { text: "Higher rates of income tax on high earners", b: 2 }, { text: "Inheritance tax on large estates", b: 2 },
  { text: "A tax on plastic bags", b: 3 }, { text: "A tariff on imported steel", b: 3 },
], done: "Taxes often have more than one aim: say which one the question asks about." });
''' + calc_js([], F.jl(304, 306, 308)) + mcq_js("qz1", [
    ("What is meant by a regressive tax?", ["A tax that falls in line with inflation", "A tax that takes a larger percentage of income from the poor than the rich", "A tax that reduces government revenue over time", "A tax that is replaced by a bigger one"], 1, "Regressive: the percentage taken falls as income rises."),
    ("A government wants to redistribute income from the rich to the poor. Which tax changes would help?", ["Cut corporation tax, raise sales tax", "Cut VAT, raise income tax", "Cut capital gains tax and inheritance tax", "Raise customs duties and excise duties"], 1, "Cutting an indirect (regressive) tax and raising a progressive direct tax moves the burden to the rich."),
    ("In which situation will consumers bear the greatest share of an indirect tax?", ["Elastic demand, inelastic supply", "Inelastic demand, inelastic supply", "Inelastic demand, elastic supply", "Elastic demand, elastic supply"], 2, "When demand is inelastic buyers keep buying, and when supply is elastic firms cut output rather than absorb the tax."),
    ("Which is an example of a direct tax?", ["VAT", "Excise duty on alcohol", "Customs duty", "Capital gains tax"], 3, "Capital gains tax is a tax on profit from selling an asset."),
    ("Tax revenue from income tax rises in a boom with no change in tax rates. This is an example of:", ["An automatic stabiliser", "A flat tax", "A windfall tax", "A regressive tax"], 0, "Revenue rising automatically in a boom cushions swings in demand."),
    ("Which is an advantage of indirect taxes?", ["They are always progressive", "They are relatively cheap and easy to collect", "They cannot raise prices", "They redistribute income to the poor"], 1, "Firms do much of the collecting, and they are harder to evade, but they tend to be regressive."),
]) + "\n" + cards_js(pick_cards(F, ["Direct tax", "Indirect tax", "Progressive tax", "Proportional tax", "Regressive tax", "Income tax", "Corporation tax", "Capital gains tax", "Inheritance tax", "Excise duty", "Customs duty", "Tax allowance", "Tax base", "Tax burden", "Incidence of tax", "Flat tax", "Windfall tax", "Informal economy"])) + "labR(); labT();\n"
ex = exam(F.b((198, 202)), F.b((211, 215)), F.b((216, 224)), F.b((233, 237)), F.b((238, 247)).replace("</section>", ""))
tp = tips([
    ("Progressive is about the percentage.", "The rich pay more dollars under every tax. Compare the % of income."),
    ("Direct = income and wealth. Indirect = spending.", "Give an example of each whenever asked."),
    ("Tax shifts supply left by the tax amount.", "Draw S₁ to S₂, label the new price and quantity, and mark who bears what."),
    ("Incidence follows elasticity.", "Inelastic demand: consumers bear most. Elastic demand: producers bear most."),
    ("Say who is affected.", "Consumers, workers, firms, the government and the economy: the syllabus asks for all five."),
    ("Use specific context.", "Cigarettes, petrol, income tax bands, VAT, recession and boom."),
], cmds("Define", "Explain", "Analyse", "Discuss"))
body = page(CL("4.2.3 Taxation"), "Taxation", "Why governments tax, direct and indirect, progressive, proportional and regressive taxes, what makes a good tax, and who bears the impact. Syllabus 4.2.3.",
    learn=learn, watch=watch(("Progressive, proportional and regressive taxes", "stR"), ("Who pays an indirect tax?", "stT")), explore=explore,
    practise=practise(("Direct or indirect?", "cl1", "card"), ("Progressive, proportional or regressive?", "cl2", "card"), ("Reasons for taxation", "cl3", "card"), ("Principles of a good tax", "m1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(F.b((182, 185)), F.b((189, 189))), exam=ex, tips=tp)
write("fb3", body, js, "Taxation", "ig-fiscal-taxation")

# =========================================================== 4.2.4 Definition of fiscal policy
COMP = '''
/* AD components bar */
function compChart(s) {
  const parts = [["C", s.c, "--accent"], ["I", s.i, "--good"], ["G", s.g, "--n"], ["X", s.x, "--warn"]], m = s.m, base = 330, k = 2.1;
  let o = SV.line(60, base, 700, base), y = base;
  parts.forEach(([n, v, col]) => {
    const h = v * k; y -= h;
    o += SV.rect(150, y, 130, h, "", { style: `fill:var(${col})`, opacity: 0.85 }) + SV.text(215, y + h / 2 + 5, n + " = " + money(v, 0), "lbl bd", { "text-anchor": "middle", style: "fill:var(--surface)" });
  });
  const total = parts.reduce((a, p) => a + p[1], 0), ad = total - m;
  o += SV.rect(420, base - m * k, 130, m * k, "", { style: "fill:var(--bad)", opacity: 0.75 }) + SV.text(485, base - m * k / 2 + 5, "M = " + money(m, 0), "lbl bd", { "text-anchor": "middle", style: "fill:var(--surface)" });
  o += SV.text(215, base + 22, "Spending on output", "sm", { "text-anchor": "middle" }) + SV.text(485, base + 22, "Leaks to imports", "sm", { "text-anchor": "middle" });
  o += SV.text(380, 40, "AD = C + I + G + (X − M) = " + money(ad, 0), "lbl bd " + (ad > 100.5 ? "t3" : ad < 99.5 ? "t2" : ""), { "text-anchor": "middle", style: "font-size:19px" });
  return o;
}
'''
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p><span class="kw">Fiscal policy</span> is the government's use of <b>spending and taxation</b> to influence <b>aggregate demand</b> and so the economy's performance against its macroeconomic aims. It is decided by the government, usually in a yearly budget, and it works by changing the parts of AD: government spending (G) directly, and consumption (C) and investment (I) through taxes.</p></div>

  <h2>What it is made of</h2>
  <div class="formula">AD = C + I + G + (X − M)</div>
  <div class="grid2">
    <div class="card"><h3>Government spending (G)</h3><p>A direct part of AD. A change in G changes AD at once.</p></div>
    <div class="card"><h3>Taxation</h3><p>Changes how much households and firms have left to spend. Lower income tax raises disposable income and could raise C; lower corporation tax could raise I.</p></div>
  </div>

  <h2>Expansionary, contractionary or neutral</h2>
  <div class="grid2">
    <div class="card"><h3>Expansionary</h3><p><b>Higher government spending and/or lower taxes</b>, designed to <b>increase AD</b>. Used when there is spare capacity, unemployment or a recession.</p></div>
    <div class="card"><h3>Contractionary</h3><p><b>Lower government spending and/or higher taxes</b>, designed to <b>reduce AD</b>. Used when the economy is overheating or inflation is too high.</p></div>
  </div>
  <p>A policy is <b>neutral</b> if the changes in spending and taxes leave AD roughly unchanged.</p>

  <h2>Fiscal policy compared with other policies</h2>
  <div class="tw"><table class="t">
    <tr><th>Policy</th><th>Who decides</th><th>Tools</th></tr>
    <tr><td><b>Fiscal</b></td><td>Government</td><td>Government spending and taxes</td></tr>
    <tr><td><b>Monetary</b></td><td>Central bank (often independent)</td><td>Interest rates, money supply, exchange rate</td></tr>
    <tr><td><b>Supply-side</b></td><td>Government</td><td>Education, infrastructure, deregulation, labour market reforms: raise AS</td></tr>
  </table></div>
  <h2>Discretionary and automatic</h2>
  <p><b>Discretionary</b> fiscal policy is a deliberate decision to change spending or taxes. <span class="kw">Automatic stabilisers</span> change the budget without any new decision when the economy moves into a boom or slump.</p>
'''
explore = '''
  <h2>Lab 1 · Build AD from its parts</h2>
  <p>Aggregate demand starts at 100. Change government spending and taxes and watch the components. In this model 70% of a tax change is passed on in consumption (the rest is saved).</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div></div>
    <div><div class="readout"><div><small>Total AD</small><strong id="ca1"></strong></div><div><small>Change in AD</small><strong id="ca2"></strong></div><div><small>Stance</small><strong id="ca3"></strong></div></div><div class="verdict" id="cav"></div></div></div>
    <svg id="labC" viewBox="0 0 760 380" role="img" aria-label="Components of aggregate demand"></svg>
  </div>'''
labc = '''
function labC() {
  if (!$("#ca") || !$("#cb")) return;
  const dG = +$("#ca").value, dT = +$("#cb").value, c = 60 - 0.7 * dT, g = 25 + dG, ad = c + 20 + g + 20 - 25, d = ad - 100;
  $("#ca1").textContent = money(ad, 1); $("#ca2").textContent = (d > 0 ? "+" : d < 0 ? "−" : "") + money(Math.abs(d), 1); $("#ca3").textContent = d > 1 ? "Expansionary" : d < -1 ? "Contractionary" : "Neutral";
  $("#cav").textContent = Math.abs(d) <= 1 ? "The changes roughly cancel out: neutral." : d > 0 ? "AD rises. A rise in G adds straight to AD, and a tax cut raises consumption (but only 70% of it is spent): expansionary." : "AD falls, as lower G and higher taxes reduce spending: contractionary.";
  $("#labC").innerHTML = compChart({ c, i: 20, g, x: 20, m: 25 });
}
Lib.slider($("#g1"), { id: "ca", label: "Change in government spending (G)", min: -15, max: 15, step: 1, value: 0, fmt: (v) => (v > 0 ? "+" : v < 0 ? "−" : "") + Math.abs(v), onInput: labC });
Lib.slider($("#g2"), { id: "cb", label: "Change in taxes (+ = tax rise)", min: -15, max: 15, step: 1, value: 0, fmt: (v) => (v > 0 ? "+" : v < 0 ? "−" : "") + Math.abs(v), onInput: labC });
'''
stc = '''
Lib.stepper($("#stK"), { w: 760, h: 400, label: "Fiscal policy changes the parts of AD", base: { c: 60, i: 20, g: 25, x: 20, m: 25 }, draw: compChart, steps: [
  { cap: "AD = <b>C + I + G + (X − M)</b>. Here C = 60, I = 20, G = 25, X = 20 and M = 25, so <b>AD = 100</b>.", s: { c: 60, i: 20, g: 25, x: 20, m: 25 } },
  { cap: "<b>Expansionary:</b> the government raises its own spending <b>G</b> by 10. AD rises by 10 straight away.", s: { c: 60, g: 35 } },
  { cap: "It also <b>cuts income tax</b>. Households keep more pay, so C rises by about 7 (some of the cut is saved). AD rises again.", s: { c: 67, g: 35 } },
  { cap: "<b>Contractionary:</b> now the government cuts G by 10 and raises taxes. G falls straight away and C falls too. <b>AD falls below 100.</b>", s: { c: 53, g: 15 } },
] });
'''
js = HEAD + COMP + stc + labc + '''
/* ================= PRACTISE ================= */
''' + F.j_((263, 266)).replace('$("#cl3")', '$("#cl3")') + '''Lib.classify($("#cl4"), { prompt: "Which kind of policy is each? <b>Fiscal</b>, <b>monetary</b> or <b>supply-side</b>?", buckets: [{ label: "Fiscal" }, { label: "Monetary" }, { label: "Supply-side" }], items: [
  { text: "Cut income tax rates", b: 0 }, { text: "Raise spending on hospitals", b: 0 },
  { text: "Central bank cuts the interest rate", b: 1 }, { text: "Central bank increases the money supply", b: 1 },
  { text: "Government funds more training for workers", b: 2 }, { text: "Government privatises a state firm", b: 2 },
  { text: "Government raises VAT", b: 0 }, { text: "Government lets the currency fall", b: 1 },
], done: "Fiscal: taxes and government spending. Monetary: rates, money, exchange rate. Supply-side: raise AS." });
''' + F.j_((275, 283)).replace('$("#m2")', '$("#m1")') + F.j_((292, 299)).replace('$("#o2")', '$("#o1")') + calc_js([
    ("Consumption is $300bn, investment $80bn, government spending $100bn, exports $90bn and imports $110bn. Calculate AD ($bn).", 460, "AD = 300 + 80 + 100 + (90 − 110) = <b>$460bn</b>.", None, None),
    ("In the same economy government spending rises by $20bn and nothing else changes. What is the new AD ($bn)?", 480, "460 + 20 = <b>$480bn</b> (before any multiplier effect).", None, None),
    ("AD is $500bn. The government's policy lowers it by 4%. What is the new AD ($bn)?", 480, "500 × 0.96 = <b>$480bn</b>.", None, None),
]) + mcq_js("qz1", [
    ("What is fiscal policy?", ["Changes in interest rates", "Changes in government spending and taxation", "Changes in the money supply", "Changes in the exchange rate"], 1, "Fiscal policy is the use of government spending and taxes to influence AD."),
    ("Which is a likely effect of expansionary fiscal policy?", ["AD shifts left", "Real GDP and employment are likely to rise", "The budget moves towards surplus", "The price level is certain to fall"], 1, "Higher spending or lower taxes raise AD."),
    ("Which part of AD does a government change directly?", ["C", "I", "G", "X − M"], 2, "G is government spending."),
    ("Who usually makes decisions on interest rates, rather than on taxes and spending?", ["The central bank", "The tax authority", "Trade unions", "Households"], 0, "Interest rates are monetary policy."),
    ("Which is contractionary fiscal policy?", ["Cutting income tax", "Raising government spending", "Raising taxes and cutting spending", "Cutting interest rates"], 2, "It reduces AD."),
]) + "\n" + cards_js(pick_cards(F, ["Fiscal policy", "Expansionary fiscal policy", "Contractionary fiscal policy", "Automatic stabilisers"]) + [("Aggregate demand", "Total spending on a country's goods and services: C + I + G + (X − M)."), ("Discretionary fiscal policy", "A deliberate decision to change government spending or taxes."), ("Monetary policy", "Use of interest rates, money supply and the exchange rate to influence AD."), ("Supply-side policy", "Measures to raise the economy's ability to produce, shifting AS right.")]) + "labC();\n"
ex = exam(
    Q(1, "Define", 2, "What is meant by fiscal policy?", "Two ideas: changes in government spending and taxation, to influence AD (or the economy).",
      "[K|Fiscal policy is the use of changes in government spending and taxation] [K|to influence aggregate demand and achieve macroeconomic aims.]", warn="Mixing it up with monetary policy. Interest rates are not fiscal."),
    Q(2, "Identify", 2, "Identify two fiscal policy measures.", "Short phrases. One about tax, one about spending is safest.",
      "[K|A change in taxation, for example raising income tax.] [K|A change in government spending, for example on roads.]"),
    Q(3, "Explain", 4, "Explain the difference between expansionary and contractionary fiscal policy.", "Use 'whereas'. Say what changes, and what happens to AD, in each.",
      "[K|Expansionary fiscal policy is higher government spending and/or lower taxes] [N|designed to raise aggregate demand and increase output and employment,] [K|whereas contractionary fiscal policy is lower government spending and/or higher taxes] [N|designed to reduce aggregate demand, which could reduce inflationary pressure.]"),
    Q(4, "Explain", 4, "Explain one way in which fiscal policy differs from monetary policy.", "Who decides, or what the tools are. Develop it with a second point.",
      "[K|Fiscal policy uses government spending and taxation,] [K|whereas monetary policy uses interest rates, the money supply and the exchange rate.] [A|Fiscal decisions are made by the government, for example in a budget, but interest rate decisions are often made by an independent central bank.] [N|This could mean fiscal policy targets particular groups or projects, while a change in interest rates affects the whole economy.]"),
)
tp = tips([
    ("Fiscal = government spending and taxes.", "Never interest rates."),
    ("Expansionary raises AD; contractionary reduces it.", "Say which and why."),
    ("Link to AD = C + I + G + (X − M).", "G changes directly; taxes change C and I."),
    ("Know who decides.", "Government for fiscal; central bank for monetary."),
], cmds("Define", "Identify", "Explain"))
body = page(CL("4.2.4 Definition of fiscal policy"), "Definition of Fiscal Policy", "What fiscal policy is, how it works through the components of aggregate demand, and how it differs from monetary and supply-side policy. Syllabus 4.2.4.",
    learn=learn, watch=watch(("Fiscal policy and the components of AD", "stK")), explore=explore,
    practise=practise(("Expansionary or contractionary?", "cl3", "card"), ("Fiscal, monetary or supply-side?", "cl4", "card"), ("Match the term", "m1", "card"), ("Order the chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(F.b((187, 188)), F.b((186, 186))), exam=ex, tips=tp)
write("fb4", body, js, "Definition of Fiscal Policy", "ig-fiscal-definition")

# =========================================================== 4.2.5 Fiscal policy measures
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>The syllabus lists two kinds of fiscal policy measure: changes in <b>taxes</b> and changes in <b>government spending</b>. Each can be expansionary or contractionary. A government picks the measure that suits its aim: speed, who it helps, and what it costs the budget.</p></div>

  <h2>Changes in taxes</h2>
  <div class="tw"><table class="t">
    <tr><th>Measure</th><th>Expansionary (tax cut)</th><th>Contractionary (tax rise)</th></tr>
    <tr><td><b>Income tax</b></td><td>Workers keep more pay: consumption could rise; may encourage work</td><td>Less disposable income: consumption could fall</td></tr>
    <tr><td><b>Corporation tax</b></td><td>Firms keep more profit: investment could rise; may attract firms</td><td>Less profit to invest; firms might move abroad</td></tr>
    <tr><td><b>Sales tax (VAT)</b></td><td>Lower prices: spending could rise; helps low-income households</td><td>Higher prices: spending could fall; may raise inflation first</td></tr>
    <tr><td><b>Excise and other duties</b></td><td>Cheaper alcohol, fuel or tobacco: consumption could rise</td><td>Discourages demerit goods; raises revenue</td></tr>
    <tr><td><b>Tax allowance</b></td><td>More income is tax free</td><td>Fewer people are exempt</td></tr>
  </table></div>

  <h2>Changes in government spending</h2>
  <div class="tw"><table class="t">
    <tr><th>Measure</th><th>Expansionary (increase)</th><th>Contractionary (cut)</th></tr>
    <tr><td><b>Capital spending</b> (roads, schools, hospitals)</td><td>Builds assets, creates jobs, and may raise AS later</td><td>Fewer projects; jobs lost in construction</td></tr>
    <tr><td><b>Current spending</b> (wages, services)</td><td>Staff and suppliers paid; services improve</td><td>Public sector jobs or pay cut</td></tr>
    <tr><td><b>Transfer payments</b> (benefits, pensions)</td><td>Recipients spend most of it: strong AD effect</td><td>Lower incomes for poorer households</td></tr>
    <tr><td><b>Subsidies</b></td><td>Lower costs for firms, which may raise output</td><td>Firms' costs rise</td></tr>
  </table></div>

  <h2>Tax cut or spending rise?</h2>
  <div class="grid2">
    <div class="card"><h3>Spending</h3><p>Goes into AD in full and at once. Can be targeted at an area or group. Harder to reverse once it starts.</p></div>
    <div class="card"><h3>Tax cuts</h3><p>Part of the cut is saved or spent on imports, so the first effect on AD is smaller. People choose how to use the money. Easier to reverse.</p></div>
  </div>
  <div class="tip"><b class="h">Evaluation reminders</b>Which group gains, how fast the effect is, what it does to the budget deficit, whether the economy has spare capacity, and whether it conflicts with other aims.</div>
'''
tipsadd = '''
/* tax cut vs spending rise */
function tsChart(s) {
  const base = 320, k = 8.5, rows = [["Spending rise $10bn", s.g, "--n"], ["Tax cut $10bn", s.t, "--accent"]];
  let o = SV.line(60, base, 700, base) + SV.text(60, 30, "First-round rise in AD ($bn)", "sm");
  rows.forEach(([n, v, col], i) => {
    const x = 160 + i * 260, h = v * k;
    o += SV.rect(x, base - h, 140, h, "", { style: `fill:var(${col})`, opacity: 0.85 }) + SV.text(x + 70, base - h - 8, v ? "$" + money(v, 0) + "bn" : "", "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 70, base + 22, n, "sm", { "text-anchor": "middle" });
  });
  if (s.note) o += SV.text(380, 60, s.note, "lbl bd t3", { "text-anchor": "middle" });
  return o;
}
Lib.stepper($("#stL"), { w: 760, h: 400, label: "A spending rise compared with a tax cut", base: { g: 0, t: 0, note: "" }, draw: tsChart, steps: [
  { cap: "The government has $10bn to use. First option: <b>raise its own spending</b> by $10bn.", s: { g: 0, t: 0, note: "" } },
  { cap: "All $10bn is <b>spent</b> on goods, services and workers, so AD rises by the full <b>$10bn</b> in the first round.", s: { g: 10, t: 0, note: "" } },
  { cap: "Second option: <b>cut taxes</b> by $10bn. Households keep the money, but they <b>save part</b> and spend part on imports.", s: { g: 10, t: 7, note: "" } },
  { cap: "In this example about <b>$7bn</b> is spent in the first round. A tax cut is slower and weaker at first, but gives people the choice and is easier to reverse.", s: { g: 10, t: 7, note: "Spending: bigger first effect" } },
] });
'''
explore = F.b((139, 145)).replace("Lab 4 ·", "Lab 1 ·") + '''
  <h2>Lab 2 · Which lever?</h2>
  <p>Pick a fiscal measure to see how it works and the catch.</p>
  <div class="card"><div class="row" id="lvBtns"></div><div id="lvOut"></div></div>
'''
lvjs = '''
const LV = [
  { n: "Cut income tax", s: "Expansionary", w: "Workers' disposable income rises, so consumption could rise.", g: "Workers and households; may encourage work.", c: "Part is saved. The deficit could widen and higher earners gain most in cash terms." },
  { n: "Raise income tax", s: "Contractionary", w: "Disposable income falls, so consumption could fall.", g: "Government: more revenue. Could help redistribute income if progressive.", c: "May discourage effort; AD and growth could slow." },
  { n: "Cut corporation tax", s: "Expansionary", w: "Firms keep more profit, which could raise investment and attract foreign firms.", g: "Firms and shareholders.", c: "Effect depends on firms' confidence; revenue may fall." },
  { n: "Cut VAT", s: "Expansionary", w: "Prices fall, so spending could rise; helps low-income households most.", g: "Consumers, especially the poor.", c: "Revenue falls; firms may not pass on the whole cut." },
  { n: "Raise spending on infrastructure", s: "Expansionary", w: "Direct rise in G with a multiplier effect; may also raise AS.", g: "Construction firms, workers, later all firms.", c: "Slow to start, large cost, borrowing needed." },
  { n: "Raise benefits", s: "Expansionary", w: "Low-income households spend most of it, so AD could rise fast.", g: "People on low incomes.", c: "Costly; may reduce the incentive to work if too generous." },
  { n: "Cut government spending", s: "Contractionary", w: "G falls, so AD falls; the deficit may narrow.", g: "Taxpayers (lower deficit, lower future taxes).", c: "Jobs and services may be lost; growth could slow." },
];
function showLV(i) {
  const p = LV[i];
  $("#lvBtns").innerHTML = LV.map((q, j) => `<button class="b${j === i ? " pri" : ""}" data-j="${j}">${q.n}</button>`).join("");
  $$("#lvBtns .b").forEach((b) => (b.onclick = () => showLV(+b.dataset.j)));
  $("#lvOut").innerHTML = `<div class="tw"><table class="t"><tr><th>Stance</th><th>How it works</th><th>Who gains</th><th>The catch</th></tr><tr><td><b>${p.s}</b></td><td>${p.w}</td><td>${p.g}</td><td>${p.c}</td></tr></table></div>`;
}
showLV(0);
'''
js = HEAD + F.j_((138, 167)) + tipsadd + F.j_((236, 251)) + lvjs + '''
/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each a change in <b>taxes</b> or a change in <b>government spending</b>?", buckets: [{ label: "Change in taxes" }, { label: "Change in government spending" }], items: [
  { text: "Raise the rate of income tax", b: 0 }, { text: "Cut corporation tax", b: 0 }, { text: "Raise VAT", b: 0 }, { text: "Increase the tax-free allowance", b: 0 },
  { text: "Build a new motorway", b: 1 }, { text: "Increase old age pensions", b: 1 }, { text: "Cut public sector pay", b: 1 }, { text: "Increase spending on schools", b: 1 },
], done: "Syllabus 4.2.5: changes in taxes and changes in government spending." });
''' + F.j_((263, 266)).replace('$("#cl3")', '$("#cl2")') + F.j_((292, 299)).replace('$("#o2")', '$("#o1")') + calc_js([
    ("A government cuts taxes by $20bn. Households save 30% of the tax cut. How much of the cut is spent ($bn)?", 14, "70% of 20 = <b>$14bn</b>.", None, None),
    ("A government raises spending by $10bn and the multiplier is 3. What is the total rise in income ($bn)?", 30, "3 × 10 = <b>$30bn</b>.", None, None),
    ("A worker earns $40,000, the tax-free allowance is $10,000 and the tax rate above it is 20%. The government raises the allowance to $12,000. How much less tax does she pay ($)?", 400, "Extra tax-free income = $2,000. 20% × 2,000 = <b>$400</b> less.", "Only the extra allowance escapes tax.", None),
]) + mcq_js("qz1", [
    ("Which is a likely effect of expansionary fiscal policy?", ["AD shifts left", "Real GDP and employment are likely to rise", "The budget moves towards surplus", "The price level is certain to fall"], 1, "Higher spending or lower taxes raise AD, which tends to raise output and employment."),
    ("Why might a $10bn tax cut raise AD by less than $10bn of extra spending?", ["Taxes are always saved", "Part of the tax cut may be saved or spent on imports", "Spending cannot raise AD", "Tax cuts reduce G"], 1, "Only the amount spent on domestic goods in the first round adds to AD."),
    ("Which measure is contractionary fiscal policy?", ["Cut in corporation tax", "Increase in benefits", "Increase in VAT with lower spending", "Cut in income tax"], 2, "Both reduce AD."),
    ("A government wants to help low-income households quickly. Which measure is most likely to raise their spending most?", ["Cut corporation tax", "Raise benefits", "Cut capital gains tax", "Cut inheritance tax"], 1, "Low-income households spend most of any extra income."),
    ("A cut in corporation tax is most likely to:", ["Raise firms' costs", "Increase firms' after-tax profit and may encourage investment", "Reduce AD directly", "Raise imports"], 1, "Higher after-tax profit may be used to invest."),
]) + "\n" + cards_js(pick_cards(F, ["Fiscal policy", "Expansionary fiscal policy", "Contractionary fiscal policy", "Income tax", "Corporation tax", "Excise duty", "Tax allowance", "Multiplier effect"]) + [("Capital spending", "Government spending on assets such as roads, schools and hospitals."), ("Current spending", "Government spending on day-to-day items such as wages and services."), ("Subsidy", "Payment by the government to producers to lower their costs.")]) + "labF(); showLV(0);\n"
ex = exam(F.b((225, 232)),
    Q(2, "Explain", 4, "Explain how a cut in corporation tax could affect firms.", "Link tax to profit, then to a decision firms might make. Add a second effect, such as attracting foreign firms.",
      "[K|Corporation tax is a tax on firms' profits, so a cut raises the profit firms keep.] [N|Firms could use the extra profit to invest in machinery or expand, which could raise their output.] [N|A lower rate could also encourage firms from abroad to locate in the country, creating jobs.]"),
    Q(3, "Analyse", 6, "Analyse how an increase in VAT could reduce inflation.", "Say which kind of inflation. Chain: VAT up, price up, real income down, spending down, AD left. Mention that VAT may first raise prices.",
      "[K|VAT is an indirect tax on spending, so a rise increases the prices of goods in the shops.] [N|Households have less real disposable income to spend, so consumption could fall.] [N|Lower consumption shifts aggregate demand to the left,] [N|which reduces demand-pull pressure on the price level.] [E|However, the rise in VAT raises prices directly at first, so measured inflation could rise before it falls.]", key=True),
    Q(4, "Discuss", 8, "Discuss whether cutting income tax is a better way to reduce unemployment than raising government spending.", "Compare speed, size, targeting, cost. End with 'it depends on…'.",
      "[K|Both are expansionary fiscal policy, designed to raise aggregate demand and so create jobs.] [N|A cut in income tax raises disposable income, so consumption could rise and firms could take on workers. It also gives people the choice of how to spend, and may encourage people to work.] [E|However, some of the extra income may be saved or spent on imports, so the first effect on AD is smaller.] [N|Raising government spending adds to AD in full and can be targeted at areas with high unemployment, for example building projects, and the multiplier could create further jobs.] [E|However, projects may take time to start and it may need borrowing.] [E|Overall, spending is likely to be better when unemployment is high in particular regions or skill groups, whereas a tax cut may be better if the aim is to give broad support quickly and the government wants to reduce its own role. The choice depends on the cause of unemployment, the budget position and spare capacity.]", key=True),
)
tp = tips([
    ("Name the measure exactly.", "Income tax, corporation tax, VAT, infrastructure spending, benefits: not just 'taxes'."),
    ("A spending rise adds to AD in full; a tax cut only in part.", "Some is saved or spent on imports."),
    ("Say who gains and who loses.", "Households, firms, the unemployed, taxpayers."),
    ("Evaluate with the budget.", "Expansionary measures usually widen the deficit."),
    ("Time lags.", "Capital projects take years; tax changes can be quick."),
], cmds("Explain", "Analyse", "Discuss"))
body = page(CL("4.2.5 Fiscal policy measures"), "Fiscal Policy Measures", "Changes in taxes and in government spending: what each measure does, who gains, and the catch. Syllabus 4.2.5.",
    learn=learn, watch=watch(("A spending rise compared with a tax cut", "stL"), ("Fiscal policy and aggregate demand", "stA")), explore=explore,
    practise=practise(("Taxes or spending?", "cl1", "card"), ("Expansionary or contractionary?", "cl2", "card"), ("Order the chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(F.b((187, 188)), F.b((183, 184))), exam=ex, tips=tp)
write("fb5", body, js, "Fiscal Policy Measures", "ig-fiscal-measures")

# =========================================================== 4.2.6 Effects on macroeconomic aims
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>Fiscal policy can help a government meet its macroeconomic aims, but each measure helps some aims and may harm others. <b>Expansionary</b> policy tends to help growth and jobs but risks inflation, a bigger deficit and a worse trade balance. <b>Contractionary</b> policy tends to help prices and the budget but risks growth and jobs. Good answers say which aim, how, and what depends on the economy's state.</p></div>

  <h2>Aim by aim</h2>
  <div class="tw"><table class="t">
    <tr><th>Aim</th><th>Expansionary (spend more, tax less)</th><th>Contractionary (spend less, tax more)</th></tr>
    <tr><td>Economic growth</td><td>AD shifts right: growth could rise</td><td>AD shifts left: growth could slow</td></tr>
    <tr><td>Full employment</td><td>Firms hire to meet demand: unemployment could fall</td><td>Unemployment could rise</td></tr>
    <tr><td>Stable prices</td><td>Risk of demand-pull inflation, especially near full capacity</td><td>Eases demand-pull pressure</td></tr>
    <tr><td>Balance of payments</td><td>Higher incomes raise imports: current account may worsen</td><td>Spending on imports falls: current account may improve</td></tr>
    <tr><td>Redistribution of income</td><td>Benefits and progressive taxes can narrow the gap</td><td>Cuts to benefits can widen the gap</td></tr>
    <tr><td>Environmental sustainability</td><td>Spending on green projects and taxes on pollution can help</td><td>Cuts to green spending, or lower taxes on polluters, can harm</td></tr>
  </table></div>

  <h2>Fiscal policy and the budget</h2>
''' + F.b((94, 94)) + '''
  <h2>Why fiscal policy may not work as planned</h2>
  <ul>
    <li><b>Time lags.</b> It takes time to recognise a problem, pass a budget and for spending to reach the economy.</li>
    <li><b>Size of the multiplier.</b> If people save or spend a lot on imports, the effect is smaller.</li>
    <li><b>Spare capacity.</b> With little spare capacity, extra AD mostly raises prices.</li>
    <li><b>The deficit.</b> Borrowing adds to the national debt and interest payments.</li>
    <li><b>Confidence and expectations.</b> If households expect higher taxes later, they may save a tax cut.</li>
    <li><b>Conflicts.</b> Growth and jobs against inflation and the current account; spending against the deficit.</li>
  </ul>
'''
chain_js = '''
const FCH = ["Government raises spending and/or cuts taxes", "AD shifts to the right", "Output ↑ (growth) and jobs ↑ (unemployment ↓)", "Price level ↑: risk of demand-pull inflation", "Imports ↑ with higher incomes: current account may worsen", "Budget deficit widens: more borrowing and debt"];
function fchain(s) {
  const bh = 46, gap = 14, x = 110, w = 540; let o = "";
  FCH.forEach((t, i) => {
    const v = clamp(s.n - i, 0, 1); if (v <= 0) return;
    const y = 14 + i * (bh + gap), col = i < 3 ? "--good" : "--bad";
    let g = SV.rect(x, y, w, bh, "", { rx: 8, style: `fill:var(${col});fill-opacity:0.16;stroke:var(${col});stroke-width:2` });
    g += SV.circle(x - 28, y + bh / 2, 15, "dot1", { style: `fill:var(${col})` }) + SV.text(x - 28, y + bh / 2 + 5, i + 1, "lbl bd", { "text-anchor": "middle", style: "fill:var(--surface);font-size:14px" });
    g += SV.text(x + w / 2, y + bh / 2 + 5, t, "lbl bd", { "text-anchor": "middle", style: "font-size:15px" });
    if (i < FCH.length - 1) g += SV.line(x + w / 2, y + bh + 1, x + w / 2, y + bh + gap - 3, "ax", { style: "stroke-width:2" }) + SV.arrowHead(x + w / 2, y + bh + gap, "d", "dot1");
    o += `<g opacity="${v}">${g}</g>`;
  });
  return o;
}
Lib.stepper($("#stF"), { w: 760, h: 400, label: "Gains and costs of expansionary fiscal policy", base: { n: 0 }, draw: fchain, steps: [
  { cap: "The government uses <b>expansionary fiscal policy</b>: more spending and/or lower taxes.", s: { n: 1 } },
  { cap: "<b>AD shifts right.</b>", s: { n: 2 } },
  { cap: "<b>Gains:</b> real GDP rises and firms need more workers. Growth and employment aims move closer.", s: { n: 3 } },
  { cap: "<b>Costs:</b> as demand rises the price level may rise, especially close to full capacity: demand-pull inflation.", s: { n: 4 } },
  { cap: "Higher incomes also draw in more <b>imports</b>, so the current account may worsen.", s: { n: 5 } },
  { cap: "And the government has to <b>borrow</b> more, so the budget deficit and national debt grow. This is why aims <b>conflict</b>.", s: { n: 6 } },
] });
'''
explore = '''
  <h2>Lab 1 · Boom or slump? The same policy, different results</h2>
  <p>Set where the economy starts, then change government spending. In a slump there is spare capacity and output responds. Near full capacity much of the effect is prices.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div></div>
    <div><div class="readout"><div><small>Change in real GDP</small><strong id="sa1"></strong></div><div><small>Change in price level</small><strong id="sa2"></strong></div><div><small>Starting position</small><strong id="sa3"></strong></div></div><div class="verdict" id="sav"></div></div></div>
    <svg id="labS" viewBox="0 0 760 400" role="img" aria-label="Aggregate demand and supply diagram"></svg>
    <p class="note">Illustrative model. The faint line is the original AD; the solid line is AD after the policy.</p>
  </div>

  <h2>Lab 2 · Fiscal policy scorecard</h2>
  <p>Pick a policy and see the usual effect on each aim, and the catch.</p>
  <div class="card"><div class="row" id="scBtns"></div><div id="scOut"></div></div>
'''
labs = '''
function labS() {
  if (!$("#sa") || !$("#sb")) return;
  const b = +$("#sa").value, dG = +$("#sb").value, [y0, p0] = solveAD(b), [y1, p1, c1] = solveAD(b + dG), c0 = 90 + 0.8 * b;
  $("#sa1").textContent = (y1 - y0 >= 0 ? "+" : "−") + money(Math.abs(y1 - y0), 1); $("#sa2").textContent = (p1 - p0 >= 0 ? "+" : "−") + money(Math.abs(p1 - p0), 1);
  $("#sa3").textContent = y0 < 40 ? "Deep slump" : y0 < 52 ? "Spare capacity" : y0 < 62 ? "Near full capacity" : "Overheating";
  $("#sav").textContent = Math.abs(dG) < 1 ? "No policy change: nothing moves." : y1 - y0 > 2 * Math.abs(p1 - p0) ? "There is spare capacity, so most of the effect shows up in output and jobs, with only a small change in prices." : "Close to full capacity, a large part of the effect shows up in the price level: more inflation for each unit of extra output.";
  const xs = (y) => QX(y), ypos = (p) => PY(p);
  let o = axes("Price level", "Real GDP") + SV.path(ptsPath([[QX(0), PY(30)], [QX(60), PY(54)], [QX(87.7), PY(115)]]), "c3") + SV.text(QX(87.7) + 6, PY(115) + 4, "AS", "lbl bd t3");
  o += adLine(c0, "c1", "AD", { t: "t1", attrs: { opacity: Math.abs(dG) >= 1 ? 0.4 : 1 } });
  if (Math.abs(dG) >= 1) o += adLine(c1, dG > 0 ? "c2" : "c4", dG > 0 ? "AD₁" : "AD₂", { t: dG > 0 ? "t2" : "t4" });
  o += hline(p0, "gr", y0) + vline(y0, p0) + SV.circle(xs(y0), ypos(p0), 6, "dot1", { opacity: 0.5 }) + ylab(p0, "P", "sm bd") + xlab(y0, "Y", "sm bd");
  if (Math.abs(dG) >= 1) o += hline(p1, "gr", y1) + vline(y1, p1) + SV.circle(xs(y1), ypos(p1), 6, dG > 0 ? "dot2" : "dot4") + ylab(p1, "P₁", "sm bd") + xlab(y1, "Y₁", "sm bd");
  $("#labS").innerHTML = o;
}
Lib.slider($("#g1"), { id: "sa", label: "Where the economy starts", min: -30, max: 35, step: 5, value: -10, fmt: (v) => (v < -15 ? "slump" : v < 15 ? "spare capacity" : "near full capacity"), onInput: labS });
Lib.slider($("#g2"), { id: "sb", label: "Change in government spending (AD shift)", min: -20, max: 20, step: 1, value: 10, fmt: (v) => (v > 0 ? "+" : v < 0 ? "−" : "") + Math.abs(v), onInput: labS });
const SC = [
  { n: "Cut taxes", g: "▲ rises", u: "▼ falls", i: "▲ may rise", c: "▼ may worsen (more imports)", b: "▼ deficit widens", catch: "Some of the cut is saved; benefits higher earners most in cash." },
  { n: "Raise government spending", g: "▲ rises", u: "▼ falls", i: "▲ risk near full capacity", c: "▼ may worsen", b: "▼ deficit widens", catch: "Time lags; opportunity cost; borrowing." },
  { n: "Raise taxes", g: "▼ slows", u: "▲ may rise", i: "▼ eases", c: "▲ may improve", b: "▲ deficit narrows", catch: "May discourage effort and investment; slower growth reduces revenue." },
  { n: "Cut government spending", g: "▼ slows", u: "▲ may rise", i: "▼ eases", c: "▲ may improve", b: "▲ deficit narrows", catch: "Public services and jobs suffer; may take longer than hoped to cut the deficit." },
  { n: "Progressive taxes and higher benefits", g: "◆ little effect", u: "◆ little effect", i: "◆ little effect", c: "◆ little effect", b: "▼ may widen", catch: "Redistributes income, but a high tax may reduce effort." },
  { n: "Green spending and pollution taxes", g: "▲ long run", u: "◆ may create jobs", i: "▲ costs may rise", c: "◆ little effect", b: "◆ depends", catch: "Helps environmental sustainability; may conflict with short-run growth." },
];
function showSC(i) {
  const p = SC[i];
  $("#scBtns").innerHTML = SC.map((q, j) => `<button class="b${j === i ? " pri" : ""}" data-j="${j}">${q.n}</button>`).join("");
  $$("#scBtns .b").forEach((b) => (b.onclick = () => showSC(+b.dataset.j)));
  $("#scOut").innerHTML = `<div class="tw"><table class="t"><tr><th>Growth</th><th>Unemployment</th><th>Inflation</th><th>Current account</th><th>Budget</th></tr><tr><td>${p.g}</td><td>${p.u}</td><td>${p.i}</td><td>${p.c}</td><td>${p.b}</td></tr></table></div><div class="warn"><b class="h">The catch</b>${p.catch}</div>`;
}
showSC(0);
'''
js = HEAD + F.j_((139, 167)) + "" + chain_js + labs + '''
/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each a <b>gain</b> or a <b>cost</b> of expansionary fiscal policy?", buckets: [{ label: "Gain" }, { label: "Cost or risk" }], items: [
  { text: "Real GDP rises", b: 0 }, { text: "Unemployment may fall", b: 0 }, { text: "More tax revenue as incomes rise", b: 0 }, { text: "Benefits help people on low incomes", b: 0 },
  { text: "Demand-pull inflation near full capacity", b: 1 }, { text: "Bigger budget deficit", b: 1 }, { text: "Higher imports and a worse current account", b: 1 }, { text: "More borrowing and debt interest", b: 1 },
], done: "Every policy has gains and costs: that is evaluation." });
Lib.classify($("#cl2"), { prompt: "Which <b>macroeconomic aim</b> does each measure mainly support?", buckets: [{ label: "Growth and jobs" }, { label: "Stable prices" }, { label: "Redistribution" }, { label: "Environment" }], items: [
  { text: "Cut income tax to raise spending in a slump", b: 0 }, { text: "Build roads and rail to create jobs", b: 0 },
  { text: "Raise taxes in an overheating economy", b: 1 }, { text: "Cut government spending to reduce demand-pull inflation", b: 1 },
  { text: "Higher tax on high earners and benefits for the poor", b: 2 }, { text: "Free healthcare for low-income households", b: 2 },
  { text: "A tax on carbon emissions", b: 3 }, { text: "Subsidies for renewable energy", b: 3 },
], done: "Name the aim, then follow the chain." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>why expansionary fiscal policy could conflict with the balance of payments</b>.", items: [
  "The government cuts taxes or raises spending",
  "AD rises and real incomes grow",
  "Households and firms spend more, including on imports",
  "Imports rise by more than exports",
  "The current account moves towards deficit",
], done: "A conflict between growth and the balance of payments." });
''' + calc_js([
    ("Real GDP is $500bn and it rises to $520bn. What is the percentage growth?", 4, "20 ÷ 500 × 100 = <b>4%</b>.", None, None),
    ("A government has a deficit of $12bn. After a contractionary policy it falls to $9bn. By what percentage did the deficit fall?", 25, "3 ÷ 12 × 100 = <b>25%</b>.", None, None),
    ("The price level rises from 100 to 103 after a boost to AD. What is the inflation rate (%)?", 3, "3 ÷ 100 × 100 = <b>3%</b>.", None, None),
]) + mcq_js("qz1", [
    ("A government cuts taxes when the economy is close to full capacity. The most likely result is:", ["Large fall in prices", "Mostly higher prices rather than higher output", "A budget surplus", "Lower imports"], 1, "With little spare capacity, extra AD mostly raises prices."),
    ("Expansionary fiscal policy could create a conflict between:", ["Full employment and stable prices", "Equal pay and education", "Free trade and tariffs", "Poverty and population"], 0, "More spending can reduce unemployment but raise demand-pull inflation."),
    ("Which is a limit on the effectiveness of fiscal policy?", ["Time lags", "Higher AD", "More jobs", "Lower taxes"], 0, "It can take a long time before spending reaches the economy."),
    ("Which fiscal policy is most likely to improve the current account in the short run?", ["Higher government spending", "Higher taxes and lower spending, which reduce spending on imports", "Lower VAT", "Higher benefits"], 1, "Falling incomes reduce import spending."),
    ("A progressive tax system and generous benefits mainly support which aim?", ["Redistribution of income", "Balance of payments stability", "Low inflation", "Full employment"], 0, "They move income from richer to poorer households."),
]) + "\n" + cards_js([("Demand-pull inflation", "A rise in the price level caused by AD growing faster than AS."), ("Spare capacity", "Unused resources: when output is below what the economy could produce."), ("Time lag", "The delay between a policy change and its effects."), ("Conflict of aims", "When achieving one macroeconomic aim makes another harder."), ("Budget deficit", "Government spending is higher than revenue."), ("Economic growth", "A rise in real GDP over time."), ("Current account", "The part of the balance of payments for trade in goods and services and income flows."), ("Redistribution of income", "Moving income from richer to poorer people, for example through taxes and benefits.")]) + "labS(); showSC(0);\n"
ex = exam(F.b((238, 247)).replace("</section>", ""),
    Q(1, "Explain", 4, "Explain two conflicts between macroeconomic aims that could result from expansionary fiscal policy.", "Two pairs of aims, each with a chain. Employment and prices; growth and the current account.",
      "[K|One conflict is between full employment and stable prices.] [N|Higher spending raises AD so firms hire more workers, but demand could rise faster than supply, causing demand-pull inflation.] [K|A second is between economic growth and the balance of payments.] [N|Higher incomes could lead to more spending on imports, so the current account deficit could widen.]"),
    Q(2, "Analyse", 6, "Analyse how a government could use fiscal policy to reduce unemployment.", "Pick expansionary measures; chain to AD, output and jobs. Mention one limit.",
      "[K|A government could use expansionary fiscal policy: increase spending and/or cut taxes.] [A|For example, building roads or cutting income tax.] [N|Higher G adds directly to AD and a tax cut raises disposable income and consumption, so AD could shift right.] [N|Firms need to produce more, so they are likely to hire more workers, and the multiplier could lead to further jobs.] [E|However, the effect may be slow and the deficit may rise.]", key=True),
    Q(3, "Discuss", 8, "Discuss whether or not a government should reduce its budget deficit by cutting spending.", "Both sides. For: debt interest, confidence, inflation. Against: lost jobs, growth, services, lower revenue. End with a judgement.",
      "[K|A budget deficit exists when spending is higher than revenue, and cutting spending is contractionary fiscal policy.] [N|Cutting spending could reduce borrowing, so the national debt and interest payments grow more slowly, leaving more of future revenue for services.] [N|It could also reduce demand-pull inflationary pressure.] [E|These gains are larger when the economy is near full capacity.] [N|However, spending cuts reduce AD, so output and employment could fall, which lowers tax revenue and raises benefit spending, so the deficit may fall by less than hoped.] [N|Cuts to health, education or benefits can hurt vulnerable groups and long-run growth.] [E|Overall, cutting spending is more likely to be suitable in a boom than in a recession. The best approach depends on the state of the economy, the size of the debt and which spending is cut.]", key=True),
)
tp = tips([
    ("Name the aim, then follow the chain.", "Growth, employment, prices, balance of payments, redistribution, environment."),
    ("Always give a cost as well as a gain.", "Expansionary: inflation, deficit, imports. Contractionary: jobs, growth."),
    ("Use conflicts.", "Pairs the syllabus names: employment and prices; growth and the environment; employment and the balance of payments."),
    ("Evaluate with lags, multiplier, spare capacity and the deficit.", "Spare capacity decides whether output or prices respond."),
    ("Judge: 'it depends on…'", "The state of the economy, the size of the policy and how it is funded."),
], cmds("Explain", "Analyse", "Discuss"))
body = page(CL("4.2.6 Effects of fiscal policy on macroeconomic aims"), "Effects of Fiscal Policy on the Aims", "How fiscal policy measures could help a government meet its macroeconomic aims, the conflicts between them and the limits of fiscal policy. Syllabus 4.2.6.",
    learn=learn, watch=watch(("Gains and costs of expansionary fiscal policy", "stF"), ("Fiscal policy and aggregate demand", "stA")), explore=explore,
    practise=practise(("Gain or cost?", "cl1", "card"), ("Which aim does it support?", "cl2", "card"), ("Order the conflict chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(F.b((186, 188)), F.b((181, 181))), exam=ex, tips=tp)
write("fb6", body, js, "Effects of Fiscal Policy on the Aims", "ig-fiscal-aims")
