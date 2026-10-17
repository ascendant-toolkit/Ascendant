"""AS syllabus 5.2.5-5.2.7 Government spending and fiscal policy. Run: python3 tools/artifact-kit/mk_as53.py"""
from asx import *
EY = EYAS("5.2.5 to 5.2.7")

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p><b class="kw">Fiscal policy</b> is the use of <b>government spending and taxation</b> to influence the economy. Government spending is either <b class="kw">current</b> (day-to-day: wages of public workers, benefits, running costs) or <b class="kw">capital</b> (investment in roads, hospitals, schools), and governments spend to provide <b>public and merit goods</b>, redistribute income, support the economy and raise <b>productive capacity</b>. <b class="kw">Expansionary fiscal policy</b> (higher spending or lower taxes, often a bigger deficit) shifts <b>AD right</b> to raise output and employment; <b class="kw">contractionary fiscal policy</b> (lower spending or higher taxes, a smaller deficit or a surplus) shifts <b>AD left</b> to reduce inflation. The results depend on spare capacity and on limits such as <b>time lags</b>, the <b>cost</b> in higher debt, <b>crowding out</b> of private spending and <b>imports</b> leaking abroad.</p></div>

  <h2>1 · Government spending (5.2.5)</h2>
  <div id="pic1" class="card"></div>
  <div class="tw"><table class="t">
    <tr><th>Type</th><th>Meaning</th><th>Examples</th></tr>
    <tr><td><b>Current expenditure</b></td><td>Day-to-day spending that does not create a lasting asset</td><td>Salaries of teachers and nurses, running costs, <b>transfer payments</b> (benefits and pensions)</td></tr>
    <tr><td><b>Capital (investment) expenditure</b></td><td>Spending on lasting assets that add to productive capacity</td><td>Roads, railways, schools, hospitals, power networks</td></tr>
  </table></div>
  <ul>
    <li><b>Reasons for spending:</b> provide <b>public goods</b> (defence, street lighting) and <b>merit goods</b> (education, health care); <b>redistribute</b> income; support demand in a recession; invest to raise <b>productive capacity</b>; provide a safety net.</li>
    <li><b>Transfer payments</b> are not part of G in AD; they change AD indirectly through household incomes.</li>
  </ul>

  <h2>2 · Expansionary and contractionary fiscal policy (5.2.6 to 5.2.7)</h2>
  <div id="pic2" class="card"></div>
  <div class="tw"><table class="t">
    <tr><th></th><th>Expansionary</th><th>Contractionary</th></tr>
    <tr><td><b>Tools</b></td><td>Raise spending, cut taxes</td><td>Cut spending, raise taxes</td></tr>
    <tr><td><b>Budget</b></td><td>Deficit rises (or surplus falls)</td><td>Deficit falls (or surplus rises)</td></tr>
    <tr><td><b>AD</b></td><td>Shifts right</td><td>Shifts left</td></tr>
    <tr><td><b>Real output and employment</b></td><td>Rise (if spare capacity)</td><td>Fall</td></tr>
    <tr><td><b>Price level</b></td><td>Rises (more near full capacity)</td><td>Falls (inflation reduced)</td></tr>
    <tr><td><b>Used when</b></td><td>Recession, high unemployment, deflation</td><td>Boom, high inflation</td></tr>
  </table></div>
  <ul>
    <li><b>Strengths:</b> can be targeted at particular sectors or groups; can act directly on AD; spending on infrastructure and education can also raise AS.</li>
    <li><b>Limits:</b> <b>time lags</b> (recognition, decision, implementation); <b>higher debt</b> and interest costs; <b>crowding out</b> if borrowing raises interest rates; <b>imports</b> leak some of the rise in demand abroad; political pressures to avoid unpopular tax rises; uncertain effect on confidence.</li>
    <li><b>Evaluation:</b> an expansionary policy increases AD only if consumers and firms spend the extra income, and is most effective with spare capacity.</li>
  </ul>
  <div class="tip"><b class="h">Exam tip</b>Explain the <b>chain</b>: tax cut, higher disposable income, higher consumption, AD shifts right, higher output and prices. Evaluate with spare capacity, time lags and the effect on the budget and debt.</div>
'''

watch = '''
  <h2>1 · Expansionary policy in a recession</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stE"></div>
  <h2>2 · Contractionary policy when inflation is high</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Change spending and taxes</h2>
  <p>Raise or cut government spending and taxes ($bn). The AD curve shifts and the budget balance changes.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div>
    <div class="readout"><div><small>Effect on AD</small><strong id="r1"></strong></div><div><small>Real output and price level</small><strong id="r2"></strong></div><div><small>Change in budget balance</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 760 300" role="img" aria-label="AD and SRAS with AD shifted by the fiscal change"></svg></div></div></div>

  <h2>Lab 2 · Which stance fits the situation?</h2>
  <p>Choose an economic situation to see which kind of fiscal policy is usually used, and the main risk.</p>
  <div class="card"><div class="grid2"><div><div id="sB" class="btnrow"></div>
    <div class="readout"><div><small>Policy stance</small><strong id="t1"></strong></div><div><small>Typical tools</small><strong id="t2"></strong></div><div><small>Main risk</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 420 200" role="img" aria-label="The policy stance for the chosen situation"></svg></div></div></div>
'''

practise = '''
  <h2>1 · Expansionary or contractionary?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the effect of a tax cut in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("A stimulus package", "In a recession a government announces extra spending on infrastructure and cuts income tax. AD shifts right, output and jobs recover, but the budget deficit and the national debt rise.", "expansionary fiscal policy and its cost.") +
rw("Austerity", "To reduce a large deficit, a government cuts spending and raises taxes. AD falls, which reduces borrowing but can slow growth and raise unemployment in the short run.", "contractionary fiscal policy and its short-run cost.") +
rw("Building a rail network", "Capital spending on railways gives jobs in the short run (AD) and improves transport for firms in the long run (AS). Investment spending can therefore serve both demand and supply.", "capital expenditure raising capacity.") +
rw("A tax cut that is saved", "If households save most of a tax cut, or spend it on imports, consumption of domestic goods rises by less, so the policy does not raise AD as much as expected.", "why fiscal policy may not always raise AD.")
)

mc_exam = [
  mcq("m20_12", 29, "What is an example of fiscal policy aimed at increasing aggregate demand in an economy?", ["increasing expenditure by firms on skills training programmes for unskilled workers", "increasing the commercial banks' lending ability", "reducing the rate of income tax for all income earners", "reducing the rate of interest on loans to manufacturing companies"], 2, "A lower rate of income tax is a fiscal policy measure that raises disposable income and spending. The others are firm spending or monetary policy."),
  mcq("m23_12", 28, "What is least likely to rise as a result of the use of expansionary fiscal policy?", ["aggregate demand", "budget surplus", "nominal income", "inflation"], 1, "Higher spending or lower taxes reduce a surplus (or raise the deficit)."),
  mcq("s24_11", 22, "What is most likely to decrease if a government uses expansionary fiscal policy?", ["a balance of payments deficit", "cyclical unemployment", "the level of wages", "the rate of inflation"], 1, "Higher AD creates jobs and reduces cyclical unemployment."),
  mcq("m25_12", 22, "Which combination of fiscal policy measures will reduce both the inflation rate and income inequality? (subsidies on food and public transport, direct taxes, indirect taxes)", ["decrease, decrease, increase", "decrease, increase, increase", "increase, decrease, increase", "increase, increase, decrease"], 3, "Higher direct taxes and lower indirect taxes cut AD (lower inflation) and are progressive, while higher subsidies help the poor."),
  mcq("s20_13", 29, "Which combination of fiscal and monetary policies is most likely to be effective in the short run for tackling deflation in a closed economy? (fiscal policy, monetary policy)", ["decreasing the budget deficit, decreasing the interest rate", "decreasing the budget deficit, decreasing the money supply", "increasing the budget deficit, decreasing the interest rate", "increasing the budget deficit, decreasing the money supply"], 2, "A bigger deficit and a lower interest rate both raise AD and so counter deflation."),
  mcq("s21_12", 30, "Which policy will not cause a reduction in the rate of inflation?", ["increasing income tax", "reducing government spending", "reducing interest rates", "removing subsidies"], 2, "Lower interest rates raise AD. The other policies are contractionary or raise costs."),
  mcq("s20_12", 28, "Which combination correctly classifies an expansionary fiscal measure and its impact on a budget deficit? (fiscal policy, budget deficit)", ["increased quantitative easing, unchanged", "increased welfare spending, increased", "lower income tax, reduced", "lower interest rates, unchanged"], 1, "Higher welfare spending is fiscal and raises the deficit. Quantitative easing and interest rates are monetary policy, and a lower income tax would raise the deficit."),
  mcq("s21_13", 17, "A government decides to build additional public sector housing to be rented to people receiving low incomes. What is most likely to fall as a result of this increase in public sector housing?", ["employment in the construction industry", "land prices in towns and cities", "rents of houses in the private sector", "total government spending"], 2, "More public rental housing increases supply of rented homes and lowers private sector rents.")
]

exam = exam_page("government spending and fiscal policy",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). Fiscal policy is an 8 or 12 mark part nearly every series: expansionary policy and AD, whether it always benefits an economy, and whether it is the best way to deal with inflation or deflation. Reworded past questions are below, with eight Paper 1 multiple choice questions.",
  [("Essay parts, 8 marks", "1", "Feb/March 2025 (22) Q5(a)"), ("Essay parts, 12 marks", "5", "May/June 2025 (21) Q5(b); Oct/Nov 2024 (21) Q5(b); Feb/March 2022 (22) Q3(b); May/June 2025 (22) Q4(b); May/June 2021 (22) Q4(b)"), ("Multiple choice (Paper 1)", "8 shown below", "2020 to 2025")],
  [
  eq(P("m25_22", "5(a)"), "8 marks", "With the help of an AD/AS diagram, explain what is meant by an expansionary fiscal policy and consider the extent to which an expansionary fiscal policy will always increase the level of aggregate demand.",
     ["Knowledge (up to 3): expansionary fiscal policy is an increase in government spending and/or a reduction in tax rates (1); aggregate demand is the total demand for an economy's goods and services at a given price level, or C + I + G + (X − M) (1); an accurate diagram showing AD and AS curves (1).",
      "Analysis (up to 3): an explanation of how a decrease in income tax, for example, increases disposable income (1), which increases consumption and so aggregate demand (1); a diagram showing a rightward shift of the AD curve (1).",
      "Evaluation (up to 2): an explanation of whether expansionary fiscal policy will increase AD (1) and a justified conclusion (1)."],
     "Define expansionary policy and AD. Tax cut: more disposable income, more consumption, AD right, with diagram. Evaluate: savings, imports, confidence.",
     [[("k", "Expansionary fiscal policy is a rise in government spending or a cut in taxes. Aggregate demand is total spending on an economy's output, C + I + G + (X − M). The diagram shows AD and SRAS meeting at the initial price level and output.")], [("n", "A cut in income tax raises households' disposable income, so consumption rises, and as consumption is a component of AD the AD curve shifts to the right, raising real output and the price level.")], [("e", "AD will not always rise by as much as expected. Households may save the tax cut or spend it on imports, and higher government borrowing could raise interest rates and crowd out private spending. The effect is largest when there is spare capacity and consumers are confident.")]]),
  eq(P("s25_21", "5(b)"), "12 marks", "Assess whether expansionary fiscal policy always benefits an economy.",
     ["Analysis (up to 8): the benefits, such as a rise in AD, real output and employment, and a fall in cyclical unemployment, with a diagram (up to 4); the costs and limits, such as a higher budget deficit and national debt, inflation near full capacity, crowding out, imports and time lags (up to 4).",
      "Evaluation (up to 4): a judgement on whether expansionary policy always benefits the economy, depending on spare capacity, the size and type of spending and the level of debt, with a conclusion."],
     "Benefits: AD, output, jobs. Costs: deficit, debt, inflation, crowding out, time lags. Judge: depends on spare capacity and debt.",
     [[("n", "Expansionary fiscal policy, through higher spending or lower taxes, raises AD, which increases real output and reduces cyclical unemployment, especially in a recession with spare capacity. But it increases the budget deficit and the national debt, and if the economy is near full capacity the rise in AD mainly raises prices. Higher borrowing may crowd out private investment by raising interest rates, some of the extra demand leaks abroad as imports, and time lags may mean the policy takes effect too late.")], [("e", "The policy does not always benefit an economy. It is most beneficial in a deep recession with spare capacity and a manageable debt, and least beneficial when the economy is close to full employment or debt is already high.")]]),
  eq(P("w24_21", "5(b)"), "12 marks", "Assess whether a government should always aim for an expansionary fiscal policy rather than a contractionary fiscal policy.",
     ["Analysis (up to 8): the case for expansionary policy: raises AD, output and employment, useful in a recession (up to 4); the case for contractionary policy: reduces inflation and the budget deficit and debt (up to 4).",
      "Evaluation (up to 4): a judgement, depending on the economic situation (recession or boom), inflation, unemployment and debt, with a conclusion that neither should be used always."],
     "Expansionary: recession, jobs. Contractionary: inflation, debt. Judge: depends on the stage of the cycle and the objectives.",
     [[("n", "Expansionary fiscal policy is suitable when output is below potential and unemployment is high, since extra spending or tax cuts raise AD and create jobs. But it adds to the deficit and may cause inflation if used when the economy is at capacity. Contractionary policy reduces inflationary pressure and the deficit, but it reduces AD, so growth slows and unemployment may rise.")], [("e", "A government should not always choose expansion. The right policy depends on where the economy is in the cycle, on the level of debt and on its objectives, so expansionary policy is best in recession and contractionary policy in a boom.")]]),
  eq(P("m22_22", "3(b)"), "12 marks", "Discuss the ways in which fiscal policy can be used to increase the aggregate supply of products in an economy and consider whether this approach is likely to be effective.",
     ["Analysis (up to 8): ways fiscal policy can raise AS, such as capital spending on infrastructure, spending on education, training and health, tax incentives for investment and research, lower income tax to encourage work, and subsidies for technology (up to 4 for explaining ways, up to 4 for how each raises AS).",
      "Evaluation (up to 4): whether the approach is likely to be effective: time lags, cost and opportunity cost, uncertainty about returns, the possibility of crowding out, the need for matching AD, with a conclusion."],
     "Ways: infrastructure, education, tax incentives. Effect: shifts LRAS right. Limits: time lags, cost, uncertain return.",
     [[("n", "Fiscal policy can raise aggregate supply through capital spending on roads and railways, which lowers firms' costs, and through spending on education and training, which raises the productivity of labour. Tax incentives for investment and research encourage firms to expand capacity, and lower income taxes may encourage more people to work. Each shifts LRAS to the right, raising potential output.")], [("e", "These policies are likely to be effective in the long run, but they take years to work, they cost money and raise the deficit, and the return is uncertain if the money is spent badly. In the short run the spending also raises AD, so inflation could rise before supply benefits arrive.")]])
  ],
  )

tips = tips_html(
  [("Define expansionary and contractionary.", "Spending up or taxes down; spending down or taxes up."),
   ("Show the chain.", "Tax cut, income, consumption, AD, output."),
   ("Use an AD/AS diagram.", "Right shift for expansionary, left for contractionary."),
   ("Say when each is used.", "Recession versus inflation."),
   ("Evaluate with spare capacity.", "Output rises most if there is spare capacity."),
   ("Mention limits.", "Time lags, debt, crowding out, imports."),
   ("Capital spending can raise AS.", "Infrastructure, education.")],
  [("Fiscal policy", "Fiscal policy uses government spending and taxation to influence the economy."),
   ("Capital spending", "Capital expenditure adds to productive capacity."),
   ("Expansionary", "Expansionary fiscal policy shifts AD to the right."),
   ("Contractionary", "Contractionary fiscal policy can reduce inflationary pressure."),
   ("Evaluation", "The impact depends on spare capacity, time lags and the level of debt.")],
  [CW["define"], CW["explain"], CW["consider"], CW["assess"]]) + FC

js = SDJS + ADASJS + '''
/* ---------- spending composition ---------- */
function spDraw(s) {
  const Y = (v) => 250 - v * 3; let o = SV.line(60, 250, 700, 250) + SV.line(60, 250, 60, 40) + SV.text(66, 34, "% of government spending", "sm");
  const parts = [["Transfer payments", 35, "f1"], ["Current spending (wages, running costs)", 45, "f2"], ["Capital spending", 20, "f3"]]; let y = 250;
  parts.forEach(([n, v, c], i) => { const k = Math.max(0, Math.min(1, s.k - i)); if (k > 0) { const h = v * 3 * k; o += SV.rect(240, y - h, 170, h, c, op(0.65)) + SV.text(325, y - h / 2 + 5, v + "%", "lbl bd", { "text-anchor": "middle" }) + SV.text(430, y - h / 2 + 5, n, "sm"); y -= h; } });
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 290" role="img" aria-label="Government spending split into transfer payments, current spending and capital spending">${spDraw({ k: 3 })}</svg>`;
function fpDraw(s) { return adasPlot({ a: s.a, s: 0, l: s.l, g: 1, n: s.n }); }
$("#pic2").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="Expansionary fiscal policy shifts AD to the right">${fpDraw({ a: 20, l: 0, n: 1 })}</svg>`;
Lib.stepper($("#stE"), { w: 760, h: 300, label: "Expansionary fiscal policy in a recession", base: { a: 0, l: 0, n: 0 }, draw: fpDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>A recession.</b> Equilibrium output (50) is well below potential output (75): spare capacity and cyclical unemployment.", s: { a: 0, l: 0, n: 0 } },
  { cap: "<b>The government cuts income tax and raises spending.</b> Disposable income and demand rise: AD shifts <b>right</b>. Real output rises towards potential and employment rises, with only a modest rise in the price level.", s: { a: 20, l: 0, n: 1 } },
  { cap: "<b>The cost.</b> The budget deficit and the national debt rise, and some of the extra spending leaks abroad as imports.", s: { a: 20, l: 0, n: 1 } },
] });
function cpDraw(s) { return adasPlot({ a: s.a, s: 0, l: -15, g: 1, n: s.n }); }
Lib.stepper($("#stC"), { w: 760, h: 300, label: "Contractionary fiscal policy when the economy is overheating", base: { a: 25, n: 0 }, draw: cpDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>A boom.</b> AD has risen so that output (about 62) is above the sustainable level (the LRAS at 60) and prices are rising: an inflationary gap.", s: { a: 25, n: 0 } },
  { cap: "<b>The government raises taxes and cuts spending.</b> AD shifts <b>left</b>: output falls back to the sustainable level and the price level falls, reducing inflation.", s: { a: 8, n: 1 } },
  { cap: "<b>The cost.</b> Slower growth and some unemployment in the short run, but a smaller deficit.", s: { a: 8, n: 1 } },
] });

/* ---------- Lab 1 ---------- */
function labF() {
  if (!["dg", "dt"].every((i) => $("#" + i))) return;
  const g = +$("#dg").value, t = +$("#dt").value, a = Math.max(-30, Math.min(40, 1.0 * g - 0.6 * t)), e = sdEq(a, 0), e0 = sdEq(0, 0), bal = -(g) + t;
  $("#r1").textContent = Math.abs(a) < 0.5 ? "No change" : a > 0 ? "Shifts right" : "Shifts left"; $("#r2").textContent = "Y " + Lib.fmtN(e.q, 1) + ", P " + Lib.fmtN(e.p, 1); $("#r3").textContent = (bal >= 0 ? "+" : "−") + "$" + Math.abs(bal) + "bn";
  $("#rv").textContent = Math.abs(a) < 0.5 ? "The changes offset each other (or are zero), so AD does not shift." : `${g > 0 ? "Spending rises by $" + g + "bn. " : g < 0 ? "Spending falls by $" + -g + "bn. " : ""}${t > 0 ? "Taxes rise by $" + t + "bn. " : t < 0 ? "Taxes fall by $" + -t + "bn. " : ""}AD shifts ${a > 0 ? "right (expansionary)" : "left (contractionary)"}: real output ${e.q > e0.q ? "rises" : "falls"} to ${Lib.fmtN(e.q, 1)} and the price level ${e.p > e0.p ? "rises" : "falls"} to ${Lib.fmtN(e.p, 1)}. The budget balance moves by ${bal >= 0 ? "+" : "−"}$${Math.abs(bal)}bn (before any change in tax revenue caused by the new output). (Government spending changes AD fully; a tax change affects it by less, because some of the extra income is saved.)`;
  $("#labA").innerHTML = adasPlot({ a, s: 0, g: 1, n: 1 });
}
Lib.slider($("#g1"), { id: "dg", label: "Change in government spending, $bn ", min: -20, max: 30, step: 5, value: 20, fmt: (v) => v, onInput: labF });
Lib.slider($("#g2"), { id: "dt", label: "Change in taxes, $bn ", min: -30, max: 30, step: 5, value: 0, fmt: (v) => v, onInput: labF });
labF();

/* ---------- Lab 2 ---------- */
const SIT = [["A deep recession with high unemployment", "Expansionary", "Raise spending, cut taxes", "Higher deficit and debt", "AD is far below capacity, so a boost to demand raises output and jobs with little inflation."], ["A boom with rising inflation", "Contractionary", "Cut spending, raise taxes", "Slower growth, rising unemployment", "AD is above capacity, so reducing it lowers inflation."], ["Deflation and falling spending", "Expansionary", "Tax cuts, infrastructure spending", "May not raise confidence", "More spending counters falling prices and demand."], ["A large budget deficit and high debt, steady growth", "Contractionary", "Gradual spending cuts, tax rises", "May slow growth", "The aim is to reduce borrowing and debt over time."], ["Weak growth but low spare capacity", "Supply-side focused", "Spending on education and infrastructure", "Takes years to work", "Capital spending raises productive capacity (LRAS), not only AD."]];
function showS(i) {
  const [n, st, tl, rk, why] = SIT[i]; $$("#sB button").forEach((b, k) => b.classList.toggle("pri", k === i));
  $("#t1").textContent = st; $("#t2").textContent = tl; $("#t3").textContent = rk; $("#tv").textContent = `${n}: ${why}`;
  $("#labB").innerHTML = SV.rect(60, 50, 300, 90, st === "Expansionary" ? "f2" : st === "Contractionary" ? "f3" : "f1", { rx: 12, ...op(0.45) }) + SV.text(210, 105, st, "lbl bd", { "text-anchor": "middle", style: "font-size:20px" }) + SV.text(210, 170, tl, "sm", { "text-anchor": "middle" });
}
$("#sB").innerHTML = SIT.map((s, i) => `<button class="b" data-i="${i}">${s[0]}</button>`).join("");
$$("#sB button").forEach((b) => (b.onclick = () => showS(+b.dataset.i)));
showS(0);

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Expansionary or contractionary fiscal policy?", ["Expansionary", "Contractionary"],
  [("A cut in income tax", 0), ("Higher government spending on roads", 0), ("A rise in VAT", 1), ("Cutting public sector spending", 1), ("A tax rise to reduce the deficit", 1), ("Increasing welfare payments", 0), ("A government stimulus package", 0), ("Reducing a budget deficit to curb inflation", 1)],
  "Expansionary: more spending or lower taxes. Contractionary: less spending or higher taxes.") + MATCH([
  ["Fiscal policy", "Use of government spending and taxation"],
  ["Capital expenditure", "Spending on lasting assets such as roads"],
  ["Current expenditure", "Day-to-day spending such as wages"],
  ["Expansionary fiscal policy", "Raises AD through higher spending or lower taxes"],
  ["Crowding out", "Government borrowing reduces private spending"],
  ["Time lag", "Delay between a problem and the effect of a policy"]]) + ORDER(
  "Put the effect of a cut in income tax in order.",
  ["The government cuts income tax", "Disposable income rises", "Consumption rises", "AD shifts to the right", "Real output and employment rise"],
  "Tax cut raises spending and AD.") + CALC([
  {"q": "Government spending is $500bn, of which $90bn is capital spending. What share is capital spending (%)?", "a": 18, "unit": "%", "tol": 0.1, "hint": "90 ÷ 500.", "sol": "<b>18%</b>."},
  {"q": "Spending rises by $20bn and taxes are unchanged. What is the change in the budget balance ($bn)?", "a": -20, "unit": "$bn", "tol": 0.5, "hint": "More spending, same revenue.", "sol": "<b>−$20bn</b>: the deficit rises."},
  {"q": "A tax cut of $10bn raises consumption by $6bn (the rest is saved). By how much does AD rise at first ($bn)?", "a": 6, "unit": "$bn", "tol": 0.1, "hint": "Only the spent part.", "sol": "<b>$6bn</b>."},
  {"q": "Real GDP is $800bn and rises 2.5% after a stimulus. What is the new real GDP ($bn)?", "a": 820, "unit": "$bn", "tol": 0.5, "hint": "800 × 1.025.", "sol": "<b>$820bn</b>."}]) + MCQ([
  ("Which is an expansionary fiscal measure?", ["A cut in income tax", "A rise in interest rates", "A cut in government spending", "A rise in VAT"], 0, "Lower taxes raise AD."),
  ("Contractionary fiscal policy would be used to:", ["Reduce inflation", "Reduce unemployment", "Raise AD", "Raise the deficit"], 0, "It lowers AD."),
  ("Capital expenditure is:", ["Spending on lasting assets", "Spending on wages", "Benefits", "Interest on debt"], 0, "Roads, schools, hospitals."),
  ("A limit of fiscal policy is:", ["Time lags", "Always works immediately", "No effect on the deficit", "Lowers debt always"], 0, "Delays."),
  ("Expansionary fiscal policy most likely:", ["Raises the budget deficit", "Cuts the national debt", "Reduces AD", "Raises unemployment"], 0, "More spending, less tax.")
], "qz1") + CARDS([
  ("Fiscal policy", "Spending and taxes."),
  ("Expansionary", "AD right."),
  ("Contractionary", "AD left."),
  ("Capital spending", "Raises capacity."),
  ("Current spending", "Day-to-day."),
  ("Use in recession", "Expansionary."),
  ("Use in boom", "Contractionary."),
  ("Limits", "Lags, debt, crowding out.")]) + MCQ(mc_exam)

build("as53", "as-fiscal-policy", "Government Spending and Fiscal Policy", EY,
  "5.2.5 to 5.2.7: current and capital government spending, expansionary and contractionary fiscal policy, and AD/AS analysis of their effects. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
