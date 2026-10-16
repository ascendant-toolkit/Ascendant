"""Syllabus 9.2.4 Policies to promote economic growth and their effectiveness (chapter 42). Run: python3 tools/artifact-kit/mk_sy924.py"""
from syl import *
EY = "A Level Economics · 9708 · Syllabus 9.2.4"

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>Policies to promote growth fall into two groups. <b>Demand-side policies</b> (fiscal, monetary, exchange rate) raise aggregate demand and aim at <b>actual growth</b> by using spare capacity. <b>Supply-side policies</b> raise the quantity, quality or productivity of factors of production and aim at <b>potential growth</b>, shifting the LRAS to the right. Their <b>effectiveness</b> depends on the size of the output gap, time lags, cost and borrowing, crowding out, inflation, the balance of payments and how people and firms respond.</p></div>

  <h2>1 · Demand-side policies: actual growth</h2>
  <div class="tw"><table class="t">
    <tr><th>Policy</th><th>How it raises growth</th><th>Limits</th></tr>
    <tr><td><b>Expansionary fiscal policy</b> (more G, lower T)</td><td>AD shifts right; the multiplier magnifies the rise in income, output and jobs</td><td>Budget deficit and debt, crowding out, time lags, may be inflationary near full capacity, leakages to imports</td></tr>
    <tr><td><b>Expansionary monetary policy</b> (lower interest rates, QE)</td><td>Cheaper borrowing raises consumption and investment, and a weaker currency raises exports</td><td>Weak effect if confidence is low or in a liquidity trap, long lags, inflation risk, asset bubbles</td></tr>
    <tr><td><b>Exchange rate depreciation</b></td><td>Exports cheaper, imports dearer, so net exports (X − M) rise</td><td>Imported inflation, retaliation, depends on elasticities (Marshall-Lerner)</td></tr>
  </table></div>
  <div class="tip"><b class="h">The key condition</b>Demand-side policy works well when there is a <b>negative output gap</b>: spare capacity lets output rise without much inflation. Near full capacity (on the vertical LRAS) the same policy mainly raises <b>prices</b>.</div>
  <div id="pic1" class="card"></div>

  <h2>2 · Supply-side policies: potential growth</h2>
  <div class="grid2">
    <div class="card"><h3>Market-based</h3><ul>
      <li><b>Privatisation and deregulation:</b> profit motive and competition may raise efficiency.</li>
      <li><b>Lower income tax and benefits:</b> more incentive to work and invest.</li>
      <li><b>Labour market reform:</b> weaker union power, more flexible hiring.</li>
      <li><b>Competition policy and free trade:</b> pressure to cut costs and innovate.</li>
    </ul></div>
    <div class="card"><h3>Interventionist</h3><ul>
      <li><b>Education, training and health:</b> better human capital.</li>
      <li><b>Infrastructure:</b> transport, energy and broadband cut firms' costs.</li>
      <li><b>R&amp;D and investment subsidies,</b> tax breaks.</li>
      <li><b>Attracting FDI and managed migration:</b> more capital and labour, technology transfer.</li>
    </ul></div>
  </div>
  <div class="tip"><b class="h">What supply-side policy does on the diagram</b>It shifts <b>LRAS right</b> (and SRAS), giving higher potential output <b>and a lower price level</b>. It is slow, but it can raise growth without adding inflation. Evaluate on <b>lags</b>, <b>cost</b> to the government, <b>equity</b> (tax cuts and weaker unions may widen inequality) and <b>environment</b>.</div>

  <h2>3 · How to judge effectiveness</h2>
  <ul>
    <li><b>Spare capacity:</b> is there a negative gap, or is the economy near full capacity?</li>
    <li><b>Time lags:</b> fiscal and monetary effects take months; education and infrastructure take years.</li>
    <li><b>Size of effect:</b> multiplier, interest rate sensitivity, the productivity gain from an investment (its marginal efficiency).</li>
    <li><b>Costs and side effects:</b> deficits, debt, crowding out, inflation, current account deficit, inequality, environmental damage.</li>
    <li><b>Constraints:</b> political resistance (for example from unions), global conditions, shortages of skilled labour or finance.</li>
  </ul>
  <p>Different schools disagree. <b>Keynesians</b> emphasise demand and active fiscal policy. <b>Monetarists and new classical economists</b> argue that markets reach full employment in the long run, so growth comes mainly from the supply side and stable prices.</p>
'''

watch = '''
  <h2>1 · A demand boost: spare capacity versus no spare capacity</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stD"></div>
  <h2>2 · A supply-side policy shifts LRAS</h2>
  <div id="stU"></div>
'''

explore = '''
  <h2>Lab 1 · Mix demand-side and supply-side policy</h2>
  <p>Start from a negative output gap. Add a demand stimulus and a supply-side improvement and watch actual growth, the price level and the gap.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div>
    <div class="readout"><div><small>Change in output</small><strong id="r1"></strong></div><div><small>Change in price level</small><strong id="r2"></strong></div><div><small>Output gap now</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 300" role="img" aria-label="AD and AS diagram showing the effect of the chosen demand and supply-side policies"></svg></div></div></div>

  <h2>Lab 2 · Policy profile</h2>
  <p>Pick a policy to see how it works, how long it takes and what weakens it.</p>
  <div class="card"><div class="row" id="lbBtns"></div><div id="lbOut"></div></div>
'''

practise = '''
  <h2>1 · Demand-side or supply-side?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the effect of a supply-side policy in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Government infrastructure programmes", "Spending on roads, railways, ports and power networks is an injection that raises demand straight away and, once built, lowers firms' costs and widens markets. Large projects often run over budget and take years before the benefits appear.", "a policy with both actual and potential effects. Say the demand effect is quick and the supply effect slow, and that the benefit depends on how well the money is spent.") +
rw("Education and training", "Better schools and apprenticeship systems raise skills, and skilled workers can earn more and produce more. Countries that invested heavily in education, such as South Korea after the 1960s, grew quickly over decades.", "a classic supply-side example. Evaluate with time lags (10 to 20 years), cost and whether training matches the skills firms need.") +
rw("Tax cuts and deregulation in the 1980s", "Several governments cut top tax rates and privatised state industries, aiming to raise incentives and efficiency. Productivity rose in some sectors, but inequality also widened and some privatised firms became private monopolies.", "market-based supply-side policy. Give both sides: efficiency gains and equity or monopoly concerns.") +
rw("Attracting multinational investment", "Countries such as Vietnam and Ireland have used tax incentives and stable policy to attract foreign firms. This can bring capital, technology and jobs, but profits flow abroad and the country can become dependent on a few firms.", "FDI as a supply-side policy. Link to potential growth and add the outflow of profits and dependence as evaluation.")
)

exam = exam_page("policies to promote economic growth",
  "We searched the A Level Economics papers in the folder (2020 to 2025). Growth policy questions are common in Paper 4, often as 12, 13 or 20 mark questions, and are reworded below. The multiple choice questions are from Paper 3. Questions on fiscal and monetary policy tools in detail are in later chapters.",
  [("Essay, 20 marks", "3", "May/June 2024 (41, 43); Oct/Nov 2024 (42); May/June 2025 (44)"), ("Essay, 12 or 13 marks", "3", "Feb/March 2021 (42); May/June 2021 (42); Oct/Nov 2021 (41)"), ("Multiple choice (Paper 3)", "7 shown below", "2020 to 2024")],
  [
  eq("Based on May/June 2025 · 9708/44 · Q5", "20 marks", "Evaluate how a country could raise its potential economic growth.",
     ["<b>Knowledge and analysis (14):</b> define potential growth and show it on LRAS or a PPC. Identify and analyse at least two supply-side policies (privatisation, education and training, labour market reform, infrastructure, R&amp;D, migration, FDI, competition policy) and explain how each raises long-run output.",
      "<b>Evaluation (6):</b> cost and borrowing limits, political constraints, shortages of labour or resources, time lags, environmental damage, monopoly or exploitation risks after privatisation."],
     "Define and draw LRAS shift. Two policies with chain of reasoning. Then evaluate with cost, lags and side effects. Conclude on which matters most."),
  eq("Based on May/June 2024 · 9708/41 and 43 · Q4", "20 marks", "Many governments see higher public spending as a cause of growth, and argue that it is therefore sensible to spend more to raise growth. To what extent do you agree?",
     ["Distinguish actual from potential growth. Higher spending raises AD, helped by the multiplier, so output and investment may rise.",
      "It works best when there is spare capacity. Near full capacity extra spending raises prices or imports and harms the balance of payments.",
      "Long-run growth also depends on capital, skills, workforce, technology and access to finance, which spending alone does not supply.",
      "Evaluation: quality of spending (investment versus consumption), borrowing and debt, inequality, environmental costs, a judgement on which side is stronger."],
     "Split short run (actual) from long run (potential). Spare capacity condition. Quality of spending. Conclude with 'it depends'."),
  eq("Based on Oct/Nov 2021 · 9708/41 · Q7(a)", "12 marks", "Explain what is meant by infrastructure and consider the view that more investment in infrastructure will raise both actual and potential economic growth.",
     ["A clear explanation of infrastructure with examples: roads, rail, ports, power, broadband, schools and hospitals.",
      "Distinguish actual from potential growth, ideally with a PPC or AD and AS diagram.",
      "Actual growth: spending on construction raises AD, output and jobs in the short run. Potential growth: better transport and energy lower costs and raise productivity, shifting LRAS right.",
      "A conclusion that both are affected but the supply-side effect is slower and depends on project quality."],
     "Define, then short-run demand effect, long-run supply effect, then a conclusion about timing."),
  eq("Based on May/June 2021 · 9708/42 · Q7(b)", "13 marks", "'Policies to achieve economic growth will inevitably cause a government budget deficit.' How far do you agree?",
     ["Explain a budget deficit and the policies: fiscal (G up or T down raises the deficit), monetary (lower interest rates need not), supply-side (education spending adds to expenditure but tax cuts may raise revenue later).",
      "Link policy to the type of growth: demand policies give actual growth in the short run, supply-side policies give potential growth in the long run.",
      "Evaluation: growth itself raises tax receipts and can shrink the deficit; some policies (deregulation, trade liberalisation, monetary easing) need no extra spending."],
     "Two policies, each linked to a deficit or not. Growth feeding tax revenue. Judge: 'not inevitably'."),
  eq("Based on Oct/Nov 2024 · 9708/42 · Q5", "20 marks", "In the decade to 2020 very low interest rates encouraged low-income countries to borrow from foreign lenders to fund long-term growth. Evaluate this approach to promoting long-term growth.",
     ["Long-term growth needs more or better inputs (capital, labour, technology). Low-income countries have low savings, so funds may come from foreign governments, agencies (IMF, World Bank) or multinationals.",
      "Borrowed funds for infrastructure and capital raise AS and AD. The investment must earn a return above the interest rate (marginal efficiency of capital).",
      "Evaluation: when interest rates rise, debt service costs rise, the currency may fall and the balance of payments worsens; projects may fail or be badly chosen; borrowing in foreign currency; alternative sources of funds (FDI, aid, domestic saving)."],
     "Show why funds are needed. How borrowing becomes growth. Then rising rates, exchange rate and debt risk. Judge on the quality of the projects."),
  eq("Based on Feb/March 2021 · 9708/42 · Q7(a)", "12 marks", "'Economic growth should be a government's most important macroeconomic aim.' Discuss.",
     ["Define growth and state the other macro aims: price stability, low unemployment, a sustainable balance of payments (and often equity and the environment).",
      "Benefits of growth: higher incomes, jobs, tax revenue, funds for public services. Costs: inflation, current account deficit, inequality, pollution, resource depletion.",
      "The aims are linked, so pursuing one affects the others. Level 4 needs a conclusion on how far the statement holds."],
     "Define growth. Case for. Case against, with trade-offs. Linked aims. Judgement.")
  ],
  )

tips = tips_html(
  [("Say which type of growth each policy affects.", "Demand-side for actual growth, supply-side for potential growth. Examiners reward the distinction."),
   ("Draw AD and AS.", "AD shifts for demand-side policy. LRAS and SRAS shift for supply-side policy. Label the equilibrium before and after."),
   ("Always check spare capacity.", "A demand boost helps most with a negative output gap. Near full capacity it mainly raises prices."),
   ("Give the chain, not a list.", "For each policy: what changes, how it affects factors of production or AD, what happens to output."),
   ("Use time lags in evaluation.", "Education and infrastructure take years. Interest rate changes take months."),
   ("Name the costs.", "Deficits and debt, crowding out, inflation, current account deficit, inequality, environmental damage."),
   ("Finish with a conclusion.", "Say which policy is most effective for this economy and why: it depends on the size of the gap and on the time horizon.")],
  [("Demand-side", "Expansionary fiscal policy could shift AD to the right and, because of the multiplier, raise national income by more than the initial injection."),
   ("Supply-side", "Investment in education may raise labour productivity, shifting the LRAS to the right and raising potential output."),
   ("Spare capacity", "This is likely to be effective because there is a negative output gap, so extra demand can raise output without much inflation."),
   ("Lags", "However, supply-side policies such as training take years to work, so the effect on growth may be slow."),
   ("Judge", "On balance, the most effective policy depends on whether the problem is a lack of demand or a lack of capacity.")],
  [CW["explain"], CW["assess"], CW["discuss"], CW["evaluate"]]) + FC

js = '''
/* ---------- AD and AS model shared by the diagrams ---------- */
const AX = (q) => 70 + q * 6.6, AY = (p) => 320 - p * 3.0;
function adas(o, a, sh, lr, col = "") {
  const sras = (q) => 15 + 0.7 * (q - sh), Q = (a - 15 + 0.7 * sh) / 1.6, P = sras(Q);
  let s = axes(70, 320, 740, 30, "Real GDP", "Price level");
  s += SV.line(AX(lr), 320, AX(lr), 40, "c3") + tag(AX(lr) + 6, 52, "LRAS", "t3");
  s += SV.line(AX(0), AY(sras(0)), AX(100), AY(sras(100)), "c2") + tag(AX(100) - 4, AY(sras(100)) - 8, "SRAS", "t2", 1, "end");
  s += SV.line(AX(0), AY(a), AX(100), AY(a - 90), "c1") + tag(AX(100) - 4, AY(a - 90) + 18, "AD", "t1", 1, "end");
  s += SV.line(AX(Q), AY(P), AX(Q), 320, "gr") + SV.line(70, AY(P), AX(Q), AY(P), "gr") + SV.circle(AX(Q), AY(P), 7, "dot4");
  return { s, Q, P };
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 360" role="img" aria-label="AD shifting right: with spare capacity output rises a lot, near the LRAS mostly prices rise">${(() => { const A = adas(0, 100, 0, 60), B = adas(0, 111, 0, 60), C = adas(0, 135, 0, 60); return A.s + SV.line(AX(0), AY(111), AX(100), AY(21), "c1 dash") + SV.line(AX(0), AY(135), AX(100), AY(45), "c1 dash") + tag(AX(B.Q) + 10, AY(B.P) - 12, "Output up, prices barely move", "t3") + tag(AX(C.Q) + 10, AY(C.P) - 14, "At capacity: mostly prices rise", "t2"); })()}</svg>`;

/* ---------- Watch 1: demand boost ---------- */
function demDraw(s) {
  const r = adas(0, s.a, 0, 60); let o = r.s;
  if (s.v > 0) o += tag(AX(r.Q) + 12, AY(r.P) + 28, "Q = " + Lib.fmtN(r.Q, 0) + ", P = " + Lib.fmtN(r.P, 0), "t4", s.v);
  if (s.g > 0 && r.Q < 59) o += SV.line(AX(r.Q), 296, AX(60), 296, "c2", { "stroke-width": 5, ...op(s.g) }) + tag(AX((r.Q + 60) / 2), 288, "spare capacity", "t2", s.g, "middle");
  return o;
}
Lib.stepper($("#stD"), { w: 760, h: 360, label: "AD shifting right first with spare capacity then at full capacity", base: { a: 100, v: 1, g: 1 }, draw: demDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>Starting point.</b> There is a negative output gap: equilibrium output is below the vertical LRAS. Q is about 53 and P about 52.", s: {} },
  { cap: "<b>Expansionary policy.</b> Lower interest rates or a rise in government spending shift <b>AD to the right</b>. Output rises towards potential and the price level rises only a little, because spare capacity can absorb the extra demand.", s: { a: 111 } },
  { cap: "<b>Capacity reached.</b> The economy is now on the LRAS. The gap is closed and actual growth has used up all the slack.", s: { a: 111, g: 0 } },
  { cap: "<b>More stimulus.</b> AD shifts again. Output cannot rise much above potential, so the extra demand mostly raises the <b>price level</b>. This is why demand-side policy loses effectiveness near full capacity.", s: { a: 135, g: 0 } },
] });

/* ---------- Watch 2: supply-side policy ---------- */
function supDraw(s) {
  const r = adas(0, 111, s.sh, 60 + s.sh); let o = r.s;
  if (s.sh > 0) o += SV.line(AX(60), 320, AX(60), 40, "c3 dash") + tag(AX(60) - 6, 52, "LRAS₁", "t3", 1, "end");
  if (s.v > 0) o += tag(AX(r.Q) + 12, AY(r.P) + 28, "Q = " + Lib.fmtN(r.Q, 0) + ", P = " + Lib.fmtN(r.P, 0), "t4", s.v);
  return o;
}
Lib.stepper($("#stU"), { w: 760, h: 360, label: "Supply side policy shifting LRAS and SRAS to the right, raising output and lowering prices", base: { sh: 0, v: 1 }, draw: supDraw, tween: 1100, dwell: 5600, steps: [
  { cap: "<b>The economy at full capacity.</b> AD crosses SRAS on the LRAS at Q = 60 and P = 57. The only way to grow faster without inflation is to raise capacity.", s: {} },
  { cap: "<b>Supply-side policy.</b> Education, infrastructure, investment incentives and competition raise the quantity, quality or productivity of factors. <b>LRAS and SRAS shift to the right</b>.", s: { sh: 8 } },
  { cap: "<b>The result.</b> Output is higher and the price level lower than before: potential growth with <b>less</b> inflationary pressure. This is why supply-side policy is a long-run answer, though it works slowly and costs money.", s: { sh: 16 } },
] });

/* ---------- Lab 1: policy mix ---------- */
function labMix() {
  if (!$("#ad") || !$("#sp")) return;
  const dA = +$("#ad").value, dS = +$("#sp").value, a0 = 100, a = a0 + dA, lr = 60 + dS, sh = dS, r0 = adas(0, a0, 0, 60), r1 = adas(0, a, sh, lr);
  const gq = (r1.Q - r0.Q) / r0.Q * 100, gp = (r1.P - r0.P) / r0.P * 100, gap = (r1.Q - lr) / lr * 100;
  $("#r1").textContent = (gq >= 0 ? "+" : "") + Lib.fmtN(gq, 1) + "%"; $("#r2").textContent = (gp >= 0 ? "+" : "") + Lib.fmtN(gp, 1) + "%"; $("#r3").textContent = Lib.fmtN(gap, 1) + "%";
  const note = dA === 0 && dS === 0 ? "No policy: the negative gap stays." : dS === 0 ? (gap > 0.5 ? "Demand-side only: output grows but pushes above potential, so prices rise." : "Demand-side only: spare capacity is used up with little inflation.") : dA === 0 ? "Supply-side only: potential rises and prices fall, but the gap widens because demand has not moved." : "Mix: demand uses spare capacity while the supply side raises potential, so growth is faster with less inflation pressure.";
  $("#rv").textContent = note + ` (Output ${Lib.fmtN(r0.Q, 0)} to ${Lib.fmtN(r1.Q, 0)}; price level ${Lib.fmtN(r0.P, 0)} to ${Lib.fmtN(r1.P, 0)}.)`;
  const X = (q) => 40 + q * 3.6, Y = (p) => 260 - p * 2.2;
  let o = SV.line(40, 260, 400, 260) + SV.line(40, 260, 40, 20) + SV.text(400, 282, "Real GDP", "sm", { "text-anchor": "end" }) + SV.text(46, 16, "Price level", "sm") + SV.line(X(lr), 260, X(lr), 30, "c3") + tag(X(lr) + 4, 42, "LRAS", "t3");
  o += SV.line(X(0), Y(15 + 0.7 * (0 - sh)), X(100), Y(15 + 0.7 * (100 - sh)), "c2") + SV.line(X(0), Y(a), X(100), Y(a - 90), "c1") + SV.circle(X(r1.Q), Y(r1.P), 6, "dot4");
  o += SV.line(X(0), Y(a0), X(100), Y(a0 - 90), "c1 dash", op(0.45)) + SV.circle(X(r0.Q), Y(r0.P), 5, "dot2", op(0.6)) + tag(X(r0.Q) - 8, Y(r0.P) + 20, "start", "t2", 0.8, "end");
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "ad", label: "Demand stimulus (AD shift) ", min: 0, max: 40, step: 1, value: 0, fmt: (v) => v, onInput: labMix });
Lib.slider($("#g2"), { id: "sp", label: "Supply-side improvement (LRAS shift) ", min: 0, max: 20, step: 1, value: 0, fmt: (v) => v, onInput: labMix });
labMix();
btnTable("lbBtns", "lbOut", [
  ["Cut interest rates", "Demand-side (monetary)", "Cheaper borrowing raises consumption and investment; a lower exchange rate lifts exports", "6 to 18 months", "Weak if confidence is low or in a liquidity trap; inflation risk"],
  ["Raise government spending", "Demand-side (fiscal)", "Injection into the circular flow, multiplied", "Months to a year", "Deficit and debt, crowding out, imports leak out"],
  ["Build roads, rail and broadband", "Supply-side (interventionist)", "Lower costs and wider markets, higher productivity", "3 to 10 years", "Expensive, project quality varies, planning delays"],
  ["Fund education and training", "Supply-side (interventionist)", "Higher skills, productivity and employment", "10 to 20 years", "Slow, skills may not match demand, high cost"],
  ["Privatise and deregulate", "Supply-side (market-based)", "Competition and profit motive cut costs", "2 to 8 years", "Private monopolies, job losses, inequality"],
  ["Cut income tax", "Supply-side (market-based) and demand", "More incentive to work and invest; also raises disposable income", "1 to 5 years", "Budget deficit, benefits go mostly to high earners, effect on work effort is small"]
], ["Policy", "Type", "How it raises growth", "Time lag", "Main weakness"]);

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Is the policy mainly demand-side or supply-side?", ["Demand-side (actual growth)", "Supply-side (potential growth)"],
  [("Cut the interest rate", 0), ("Fund apprenticeships and training", 1), ("Increase government spending on benefits", 0), ("Privatise a state-owned airline", 1), ("Quantitative easing", 0), ("Offer tax breaks for research and development", 1), ("Devalue the currency", 0), ("Build a new power grid", 1)],
  "Demand-side moves AD. Supply-side moves LRAS.") + MATCH([
  ["Infrastructure", "Basic facilities that businesses need: roads, power, ports, broadband"],
  ["Deregulation", "Removing rules that restrict competition"],
  ["Privatisation", "Selling state-owned firms to the private sector"],
  ["Crowding out", "Government borrowing reduces private sector investment"],
  ["Time lag", "The delay between a policy change and its full effect"],
  ["FDI", "Investment by a foreign firm in productive assets in another country"]]) + ORDER(
  "Put the effects of better education and training in order.",
  ["The government increases funding for training", "Workers' skills and productivity improve", "Firms can produce more output per worker at lower unit cost", "LRAS shifts right", "Potential output rises and the price level is lower than it would have been"],
  "Supply-side policy works through the quality of factors of production.") + CALC([
  {"q": "A government increases spending by $30bn. The marginal propensity to consume is 0.6 and there are no taxes or imports. Calculate the total increase in national income (in $bn).", "a": 75, "unit": "$bn", "tol": 0.01, "hint": "Multiplier = 1 ÷ (1 − MPC).", "sol": "Multiplier = 1 ÷ 0.4 = 2.5. Rise in income = 2.5 × 30 = <b>$75bn</b>."},
  {"q": "Potential GDP is growing at 2.5% a year. Actual GDP is $950bn and potential is $1,000bn. Spending rises so that actual GDP grows by 6% in the next year. Calculate the new output gap as a percentage of potential GDP (ignore growth in potential; one decimal place, minus sign if negative).", "a": 0.7, "tol": 0.1, "hint": "New actual = 950 × 1.06.", "sol": "950 × 1.06 = 1007. Gap = (1007 − 1000) ÷ 1000 × 100 = <b>+0.7%</b>."},
  {"q": "Real GDP is $2,000bn. Over five years it grows at a steady 3% a year. Calculate real GDP after five years (to the nearest $bn).", "a": 2319, "unit": "$bn", "tol": 1, "hint": "2000 × 1.03⁵.", "sol": "1.03⁵ = 1.1593, so GDP = <b>$2,319bn</b>."}]) + MCQ([
  ("Which policy is most likely to raise potential output?", ["A cut in the interest rate", "Higher government spending on benefits", "Investment in education and training", "A fall in the exchange rate"], 2, "Training raises the quality of labour and shifts LRAS to the right. The other policies move AD."),
  ("Why may expansionary fiscal policy be ineffective at full capacity?", ["Taxes have no effect on demand", "Extra demand mainly raises prices", "The multiplier becomes negative", "Imports always fall"], 1, "With no spare capacity extra demand raises the price level rather than output."),
  ("Which is a market-based supply-side policy?", ["Building a new railway", "Funding an apprenticeship scheme", "Deregulating an industry to increase competition", "Increasing the budget deficit"], 2, "Deregulation relies on markets and competition to raise efficiency. The railway and training are interventionist."),
  ("A government builds roads and broadband. Which describes the likely effects?", ["Only a short-run rise in AD", "A short-run rise in AD and a long-run rise in potential output", "Only a long-run fall in prices", "No effect on either AD or AS"], 1, "Construction spending is an injection now and better infrastructure raises productivity later."),
  ("What is the main limitation of supply-side policies?", ["They always raise inflation", "They take a long time to have an effect", "They reduce potential output", "They cannot be financed"], 1, "Education, infrastructure and reform take years to raise output.")
], "qz1") + CARDS([
  ("Demand-side policy", "Policy that shifts AD (fiscal, monetary, exchange rate) to raise actual growth."),
  ("Supply-side policy", "Policy that raises productive capacity and shifts LRAS right."),
  ("Market-based supply-side", "Deregulation, privatisation, tax cuts, competition policy."),
  ("Interventionist supply-side", "Education, training, infrastructure, R&D subsidies."),
  ("Infrastructure", "Roads, rail, ports, power, broadband and other basic facilities."),
  ("Multiplier", "The rise in income from an injection is a multiple of the injection."),
  ("Time lag", "The delay between a policy and its effect on output."),
  ("Crowding out", "Public borrowing pushes up interest rates and reduces private investment.")]) + MCQ([
  ("What would be the biggest contribution to sustainable economic growth in a developed economy? (Feb/March 2020 · 32 · Q18, reworded)", ["Movement of people from rural to urban areas", "An increase in technical training", "An increase in the size of the population", "Rising consumer credit"], 1, "Technical training raises productivity over the long run without using up resources."),
  ("Which Keynesian policy would most clearly reduce cyclical unemployment? (Feb/March 2020 · 32 · Q23, reworded)", ["Higher government spending on new infrastructure such as roads", "Higher government spending on retraining workers", "A cut in the tax rate on imports", "A cut in the tax rate on goods and services"], 0, "Cyclical unemployment comes from weak demand, so a direct rise in government spending on projects raises AD and jobs."),
  ("What would reduce the effectiveness of a supply-side stimulus to the economy? (May/June 2023 · 31 · Q25, reworded)", ["A limit on the hours people can work in a week", "A rise in public sector spending", "New training schemes", "Relaxed import controls on raw materials"], 0, "A cap on working hours restricts labour supply and works against the stimulus."),
  ("A government raises its deficit to spend on infrastructure and finances it by printing money. How is this likely to affect unemployment, inflation and growth? (Feb/March 2024 · 32 · Q22, reworded)", ["Unemployment less likely, inflation less likely, growth more likely", "Unemployment less likely, inflation more likely, growth less likely", "Unemployment more likely, inflation more likely, growth less likely", "Unemployment more likely, inflation more likely, growth more likely"], 1, "More spending and money should cut unemployment, but printing money and extra demand raise inflation risk, and high inflation can reduce growth."),
  ("What is most likely to encourage foreign direct investment into a developing economy? (Feb/March 2022 · 32 · Q20, reworded)", ["Better health and safety standards", "Higher import quotas", "More spending on infrastructure", "A minimum wage"], 2, "Better infrastructure cuts firms' costs, which attracts FDI."),
  ("Which government measure is most likely to encourage faster and more sustainable growth? (Oct/Nov 2022 · 33 · Q18, reworded)", ["Subsidies to firms that use recycled materials", "Grants to explore new oil deposits", "More spending on environmental education in schools", "Stricter controls on emissions"], 0, "Subsidies for recycling raise output while saving resources. The oil grants use up finite resources."),
  ("Low wages and cheap land will not attract foreign investment into manufacturing in which circumstance? (Oct/Nov 2023 · 33 · Q30, reworded)", ["Genuine central bank independence", "A privatisation programme", "A lack of well-developed infrastructure", "Profits can be sent home freely"], 2, "Without transport, power and communication the cost advantage of cheap labour is lost.")
])

build("sy924", "growth-policies-effectiveness", "Policies to Promote Economic Growth and Their Effectiveness", EY,
  "9.2.4: demand-side and supply-side policies for growth, how each works on AD and AS, and how to judge their effectiveness. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
