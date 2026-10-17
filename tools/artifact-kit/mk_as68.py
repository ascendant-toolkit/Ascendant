"""AS syllabus 6.5.1-6.5.2 Policies to correct current account imbalances. Run: python3 tools/artifact-kit/mk_as68.py"""
from as6k import *
EY = EYAS("6.5.1 to 6.5.2")

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>To correct a <b class="kw">current account deficit</b> a government can use <b class="kw">expenditure-switching policies</b>, which move spending <b>from imports to domestic goods</b> (a <b>depreciation</b> or devaluation, <b>protectionism</b> such as tariffs and quotas, and <b>export subsidies</b>), and <b class="kw">expenditure-reducing policies</b>, which cut total spending and so imports (<b>higher taxes</b>, <b>lower government spending</b> and <b>higher interest rates</b>), as well as <b class="kw">supply-side policies</b> that improve long-run competitiveness. Each has costs: switching policies can provoke <b>retaliation</b> and depend on <b>elasticities</b>, reducing policies may cut <b>output and employment</b> and cause <b>deflationary pressure</b>, and supply-side policies are <b>slow and uncertain</b>. For a <b>surplus</b> the policies are broadly the opposite, such as an appreciation, lower tariffs or expansionary policy. The best choice depends on the <b>cause</b> of the imbalance, the <b>size</b>, the <b>time</b> available and the <b>exchange rate system</b>.</p></div>

  <h2>1 · Expenditure-switching and expenditure-reducing</h2>
  <div class="tw"><table class="t">
    <tr><th>Policy</th><th>How it works</th><th>Limits</th></tr>
    <tr><td><b>Depreciation or devaluation</b></td><td>Exports cheaper, imports dearer, so spending switches</td><td>Elasticities (Marshall-Lerner), J-curve, cost-push inflation</td></tr>
    <tr><td><b>Protectionism</b> (tariffs, quotas)</td><td>Raises the price of imports or limits them</td><td>Retaliation, inelastic demand, higher input costs, WTO rules</td></tr>
    <tr><td><b>Export subsidies</b></td><td>Lower export prices</td><td>Cost to taxpayers, retaliation</td></tr>
    <tr><td><b>Contractionary fiscal policy</b></td><td>Higher taxes and lower spending reduce income and imports</td><td>Lower output and jobs, time lags, political cost</td></tr>
    <tr><td><b>Higher interest rates</b></td><td>Reduce spending and may attract inflows, raising the currency</td><td>An appreciation hurts exports; slows growth</td></tr>
    <tr><td><b>Supply-side policies</b></td><td>Raise productivity and quality, improving competitiveness</td><td>Slow, costly and uncertain</td></tr>
  </table></div>

  <h2>2 · Judging the options</h2>
  <ul>
    <li><b>Floating or fixed:</b> under a floating rate the exchange rate may adjust and offset some policies (higher interest rates may raise the currency and hurt exports); under a fixed rate, devaluation or deflation may be needed.</li>
    <li><b>Cause:</b> a deficit from high consumer spending suits reducing policies; one from low competitiveness suits supply-side policy.</li>
    <li><b>Time:</b> tariffs and depreciation work faster than supply-side policy.</li>
    <li><b>Wider aims:</b> reducing policies may conflict with growth and unemployment targets.</li>
  </ul>
  <div class="tip"><b class="h">Exam tip</b>For "discuss" or "assess" questions, give <b>advantages and limitations</b> of each policy, then <b>judge</b> which is most effective given the <b>cause, speed and side effects</b>. Using the term <b>expenditure-switching</b> or <b>expenditure-reducing</b> correctly earns credit.</div>
'''

watch = watch_html("Expenditure-switching: a depreciation", "Expenditure-reducing: contractionary policy")

explore = '''
  <h2>Lab 1 · Close the deficit (a simple illustration)</h2>
  <p>A country has exports of 200 and imports of 240, a deficit of 40. Use a depreciation (switching) and a cut in AD (reducing) and watch the deficit and the cost. Assumed elasticities: PEDx 0.7, PEDm 0.7, income elasticity of imports 1.2.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div>
    <div class="readout"><div><small>New deficit</small><strong id="r1"></strong></div><div><small>Change in output (approx.)</small><strong id="r2"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 220" role="img" aria-label="Bars for exports and imports after the chosen policies"></svg></div></div></div>
''' + chooser_html("h", "Lab 2 · Choose a policy", "Choose a policy to see how it works, its main limit and how effective it tends to be.", ["How it works", "Main limit", "Speed"])

practise = practise_html("Switching or reducing?", "Match the policy to its description", "Put the effects of contractionary policy in order")

real = RWNOTE + (
rw("A tariff on imported goods", "A government taxes imported electronics. They become dearer, so people buy fewer imports, but trading partners may retaliate and firms that use imported parts face higher costs.", "expenditure switching through protection.") +
rw("Tax rises and spending cuts", "A government facing a large deficit raises taxes and cuts spending. Households have less income, buy fewer imports, and the deficit narrows, but growth slows and unemployment may rise.", "expenditure-reducing policy.") +
rw("Investing in skills and technology", "A government spends on training and research so firms become more productive and export more. The results may take many years.", "supply-side policy and competitiveness.") +
rw("A central bank raises rates", "Higher interest rates reduce borrowing and spending, cutting imports. They may also attract foreign savings and raise the currency, which makes exports dearer.", "interest rates and the current account.")
)

mc_exam = [
  mcq("s20_11", 25, "What is an expenditure-switching policy to reduce a country's balance of payments deficit?", ["an increase in budget surplus", "an increase in direct taxes", "an increase in import tariffs", "an increase in interest rates"], 2, "Tariffs switch spending from imports to domestic goods."),
  mcq("s21_12", 29, "Which policy aimed at correcting a balance of trade deficit is an expenditure-reducing policy?", ["depreciation of the currency", "increased direct taxation", "tax incentives for exporters", "the imposition of protectionist tariffs"], 1, "Higher direct taxes reduce disposable income, spending and imports."),
  mcq("s20_13", 30, "Which policy measure is an expenditure-switching measure designed to reduce a current account surplus?", ["a cut in income tax rates", "a depreciation of the exchange rate", "the removal of limits on bank lending", "the removal of subsidies to exporters"], 3, "Removing export subsidies raises export prices, switching spending away from exports."),
  mcq("m21_12", 23, "A country has a deficit on the current account of its balance of payments. What might help the country to reduce its deficit?", ["a decrease in its rate of income tax", "a decrease in its tariffs", "an increase in its level of employment", "an increase in its subsidies to exporters"], 3, "Export subsidies lower export prices and may raise exports."),
  mcq("s22_11", 30, "The government of a country is worried about a large deficit on the current account of its balance of payments and an increasing rate of inflation. The country has a fixed exchange rate for its currency. Which policy measure is most likely to help the government to reduce the current account deficit and lower the rate of inflation?", ["devaluation of the currency", "increasing government spending", "decreasing the direct taxes", "increasing the interest rate"], 3, "A higher interest rate reduces spending and inflation, and cuts imports."),
  mcq("s22_12", 30, "A country with low unemployment and a managed floating exchange rate has a persistent current account deficit on its balance of payments. Which policy to reduce this deficit is most likely to keep unemployment low, but cause inflation?", ["depreciating its currency", "higher direct taxation", "higher import tariffs", "higher interest rates"], 0, "A depreciation raises net exports and AD, keeping employment high, but raises import prices and so inflation."),
  mcq("m23_12", 30, "A government raises interest rates to improve the current account of the balance of payments. What might reduce the effectiveness of this policy?", ["a fall in domestic growth", "consumer pessimism", "increased domestic saving", "price-elastic demand for exports"], 3, "Higher rates may raise the exchange rate, and if demand for exports is elastic, export revenue falls sharply.")
]

exam = exam_page("policies to correct current account imbalances",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). Correcting a current account deficit is a very common 12 mark Paper 2 question, often with protectionism, supply-side or expenditure-reducing policies. Reworded past questions are below, with seven Paper 1 multiple choice questions.",
  [("Essay parts, 8 marks", "1", "Oct/Nov 2023 (23) Q5(a)"), ("Essay parts, 12 marks", "4", "May/June 2022 (23) Q4(b); Oct/Nov 2020 (21) Q4(b); Oct/Nov 2021 (21) Q4(b); Oct/Nov 2022 (21) Q4(b)"), ("Multiple choice (Paper 1)", "7 shown below", "2020 to 2025")],
  [
  eq(P("w23_23", "5(a)"), "8 marks", "Explain how import tariffs might correct an imbalance in the current account of the balance of payments and consider whether these tariffs are the best way of correcting such an imbalance.",
     ["Knowledge (up to 3): what is meant by an import tariff (1); what is measured by the current account (1); what is meant by an imbalance in terms of a surplus or deficit (1).",
      "Analysis (up to 3): how import tariffs affect the prices of imports (1), how this may affect domestic consumption of imports (1), and how this may correct the imbalance (1).",
      "Evaluation (up to 2): the final effect is uncertain, for example because of the PED for imports, other policies that could be used, and retaliation by trading competitors; one mark is reserved for a justified conclusion."],
     "Define tariff, current account, imbalance. Tariff: import prices up, imports down, deficit narrows. Evaluate: PED, retaliation, other policies.",
     [[("k", "An import tariff is a tax on imported goods. The current account measures trade in goods and services and primary and secondary income, and an imbalance means a deficit, where outflows exceed inflows, or a surplus.")], [("n", "A tariff raises the price of imports, so households and firms may buy fewer of them and switch to domestic goods. Spending on imports falls, which reduces a current account deficit.")], [("e", "Tariffs are not necessarily the best way. If demand for imports is inelastic, imports fall by little, trading partners may retaliate and cut the country's exports, and other policies such as supply-side measures could tackle the cause of the deficit. A tariff may therefore help in the short run but is unlikely to be the best long-run solution.")]]),
  eq(P("s22_23", "4(b)"), "12 marks", "Discuss the extent to which expenditure-switching policies and expenditure-reducing policies might be able to reduce a persistent deficit on the current account of the balance of payments.",
     ["Analysis (up to 8): the advantages and disadvantages of expenditure-switching policies (up to 4; maximum 3 if only advantages or only disadvantages) and of expenditure-reducing policies (up to 4; maximum 3 if one-sided). Expenditure-reducing policies lower domestic AD to cut imports, for example raising taxes or reducing government spending; expenditure-switching policies encourage people to buy domestic goods, for example protectionism, supply-side policies and exchange rate policies.",
      "Evaluation (up to 4): compares the advantages and disadvantages of the two approaches to reach a reasoned conclusion on which gives the greater overall benefit in reducing a persistent deficit."],
     "Reducing: taxes up, spending down; cuts imports but costs output and jobs. Switching: tariffs, depreciation, supply-side; shifts spending but retaliation, elasticity. Compare and conclude.",
     [[("n", "Expenditure-reducing policies, such as higher taxes or cuts in government spending, lower AD and so spending on imports, but they may also reduce output and increase unemployment, and the effect may be slow. Expenditure-switching policies, such as a depreciation, tariffs or supply-side measures, move spending from imports to domestic goods without cutting total spending, but a depreciation depends on elasticities, tariffs may provoke retaliation, and supply-side policies are slow.")], [("e", "For a persistent deficit caused by weak competitiveness, switching policies, especially supply-side measures, may have the greater long-run benefit, because reducing policies only cut spending without fixing the cause. In the short run, reducing policies may be more certain. A mix is likely to be most effective.")]]),
  eq(P("w20_21", "4(b)"), "12 marks", "Discuss whether supply-side policies are an effective way of correcting a deficit on an economy's current account of the balance of payments.",
     ["Analysis (up to 8): the potential advantages of supply-side policies (up to 4); the potential disadvantages (up to 4). Policies may include lowering income tax, spending on education and training, reducing trade union power, privatisation and deregulation, each of which does not necessarily deliver the intended result.",
      "Evaluation (up to 4): a judgement on whether supply-side policies are an effective way of correcting a deficit, with a conclusion (1 mark reserved)."],
     "Supply-side: productivity, costs, quality, so exports up and imports down. Limits: slow, costly, uncertain. Judge: effective long run, not short run.",
     [[("n", "Supply-side policies, such as spending on education and training or reducing red tape, may raise productivity and cut costs, making exports cheaper and better and reducing the need for imports. This tackles the cause of a competitiveness-based deficit. But the policies may not increase labour productivity or work incentives as intended, they can be costly, and the effects may take many years to appear.")], [("e", "Supply-side policies may be effective in the long run, as they improve competitiveness, but they are unlikely to correct a deficit quickly. Their success depends on the cause of the deficit and on whether the policies actually raise productivity. They may be best combined with short-run measures.")]]),
  eq(P("w21_21", "4(b)"), "12 marks", "Discuss whether expenditure-reducing policies are likely to reduce the current account deficit on the balance of payments for an economy with a floating exchange rate.",
     ["Analysis (up to 8): the potential success of expenditure-reducing policies in reducing the deficit (up to 4) and their limitations (up to 4). Expenditure-reducing policies reduce total spending and aim to cut imports and/or raise exports; examples include raising interest rates, reducing the money supply and increasing taxes.",
      "Evaluation (up to 4): a judgement on whether the policies are likely to reduce the deficit for an economy with a floating exchange rate, with a conclusion."],
     "Reducing policies: less income, fewer imports. Floating rate: higher rates raise the currency, which hurts exports. Costs: output, jobs. Judge.",
     [[("n", "Higher taxes, lower government spending or higher interest rates reduce disposable income and AD, so households buy fewer imports and the deficit may narrow. Lower demand may also reduce inflation, making exports more competitive over time. But with a floating exchange rate, higher interest rates may attract foreign funds and raise the currency, making exports dearer and imports cheaper, which could offset the policy. The policies may also reduce output and increase unemployment.")], [("e", "The policies are likely to reduce the deficit in the short run if the deficit is caused by excess domestic demand, but the effect may be limited by the exchange rate and by lower growth. They are less likely to succeed if the deficit is caused by poor competitiveness.")]]),
  eq(P("w22_21", "4(b)"), "12 marks", "Discuss whether protectionist policies would be the most effective way to correct a current account deficit on the balance of payments in an economy.",
     ["Analysis (up to 8): the potential advantages of protectionist policies (up to 4), such as tariffs making imports dearer and discouraging consumption of them, quotas restricting the volume of imports, embargoes banning imports, red tape making imports harder, and export subsidies making domestic products more price competitive; and their limitations (up to 4), such as tariffs being less effective if demand for imports is price inelastic.",
      "Evaluation (up to 4): a judgement on whether protectionist policies would be the most effective way to correct a current account deficit, with a conclusion (1 mark reserved)."],
     "Protection: tariffs, quotas, embargoes, red tape, export subsidies cut imports or raise exports. Limits: inelastic demand, retaliation, higher costs. Compare with other policies and judge.",
     [[("n", "Tariffs and quotas raise the price or limit the volume of imports, and export subsidies make exports cheaper, so protectionism could reduce a deficit quickly. But if demand for imports is price inelastic, a tariff reduces imports by little, other countries may retaliate and reduce the country's exports, and firms that rely on imported inputs face higher costs. Protectionism also does not address the underlying lack of competitiveness.")], [("e", "Protectionism may be effective in the short run but is unlikely to be the most effective overall, since supply-side policies could tackle the cause of the deficit, and depreciation or reducing policies may avoid the risk of retaliation. Its effectiveness depends on elasticities and the response of trading partners.")]])
  ],
  )

tips = tips_html(
  [("Know the two types.", "Switching: imports to domestic. Reducing: cut total spending."),
   ("Give limits for each.", "Retaliation, elasticity, lost output, time lags."),
   ("Match policy to cause.", "Demand-led deficit or competitiveness-led deficit."),
   ("Floating or fixed.", "The exchange rate may offset policy."),
   ("Short versus long run.", "Tariffs fast; supply-side slow."),
   ("Compare.", "Weigh the policies against each other."),
   ("Conclude.", "A mix may work best.")],
  [("Expenditure-switching", "Expenditure-switching policies move spending from imports to domestic goods."),
   ("Expenditure-reducing", "Expenditure-reducing policies reduce total spending, including on imports."),
   ("Devaluation", "A devaluation is an official fall in a fixed exchange rate."),
   ("Retaliation", "Retaliation is when trading partners respond with their own barriers."),
   ("Competitiveness", "Competitiveness is the ability to sell goods at attractive price and quality.")],
  [CW["explain"], CW["discuss"], CW["assess"], CW["consider"]]) + FC

js = CHAINJS + '''
chainStep("#stA", "Expenditure-switching through a depreciation", ["The currency depreciates or is devalued", "Exports are cheaper abroad; imports are dearer at home", "Spending switches from imports to domestic goods", "Exports rise and imports fall", "The deficit narrows, if PEDx + PEDm is above one"], [
  "<b>A fall in the exchange rate</b> is the starting point.", "<b>Relative prices change.</b>", "<b>Spending switches</b> without cutting total demand.", "<b>Volumes adjust</b>, though slowly (the J-curve).", "<b>The Marshall-Lerner condition</b> must hold for the balance to improve."]);
chainStep("#stB", "Expenditure-reducing policy", ["The government raises taxes or cuts spending", "Disposable income and AD fall", "Households and firms buy fewer imports", "The current account deficit narrows", "Output and employment may fall, with lower inflation"], [
  "<b>Contractionary policy</b> is chosen to cut spending.", "<b>AD falls</b> through lower consumption and government spending.", "<b>Imports fall</b>, because they depend on income.", "<b>The deficit narrows.</b>", "<b>The cost:</b> slower growth and higher unemployment, though inflation may ease."]);

function labA() {
  if (!["g1v", "g2v"].every((i) => $("#" + i))) return;
  const dep = +$("#g1v").value, cut = +$("#g2v").value;
  const X = 200 * (1 + 0.007 * dep), M = 240 * (1 + dep / 100) * (1 - 0.007 * dep) * (1 - 0.012 * cut), def = M - X, out = -cut + 0.5 * dep;
  $("#r1").textContent = Lib.fmtN(def, 1); $("#r2").textContent = (out >= 0 ? "+" : "") + Lib.fmtN(out, 1) + "%";
  const mx = 300, W = (v) => (v / mx) * 300;
  $("#labA").innerHTML = SV.text(30, 24, "Exports", "sm") + SV.rect(100, 10, W(X), 22, "f1", op(0.7)) + SV.text(104 + W(X), 26, Lib.fmtN(X, 0), "lbl bd") + SV.text(30, 64, "Imports", "sm") + SV.rect(100, 50, W(M), 22, "f3", op(0.7)) + SV.text(104 + W(M), 66, Lib.fmtN(M, 0), "lbl bd") + SV.text(30, 120, "Deficit " + Lib.fmtN(def, 1), "lbl bd") + SV.rect(100, 130, Math.max(2, W(Math.max(def, 0))), 22, "f2", op(0.7)) + SV.text(30, 190, "Original deficit: 40", "sm");
  $("#rv").textContent = `With a depreciation of ${dep}% and a fall in AD of ${cut}%, exports are ${Lib.fmtN(X, 0)} and imports ${Lib.fmtN(M, 0)}, so the deficit is ${Lib.fmtN(def, 1)}. ` + (cut > 0 ? "The cut in AD reduces output (and may raise unemployment). " : "") + (dep > 0 ? "The depreciation raises import prices and may add to inflation. " : "") + "This is a simple illustration with assumed elasticities.";
}
Lib.slider($("#g1"), { id: "g1v", label: "Depreciation, % ", min: 0, max: 20, step: 2, value: 10, fmt: (v) => v + "%", onInput: labA });
Lib.slider($("#g2"), { id: "g2v", label: "Fall in AD from tax rises or spending cuts, % ", min: 0, max: 10, step: 1, value: 0, fmt: (v) => v + "%", onInput: labA });
labA();

chooser("h", [
  ["Depreciation or devaluation", "Cheaper exports, dearer imports", "Elasticities, J-curve, imported inflation", "Medium", 3],
  ["Tariffs and quotas", "Dearer or restricted imports", "Retaliation; inelastic demand", "Fast", 3],
  ["Export subsidies", "Lower export prices", "Cost to taxpayers; retaliation", "Fast", 2],
  ["Contractionary fiscal policy", "Lower income, so fewer imports", "Lower output and jobs", "Medium", 3],
  ["Higher interest rates", "Less spending; may attract funds", "May raise the currency and hurt exports", "Medium", 2],
  ["Supply-side policies", "Better quality and lower costs", "Slow, costly, uncertain", "Slow", 4]
], (it) => `${it[0]}: it works through ${it[1].toLowerCase()}. The main limit is ${it[2].toLowerCase()}. Speed: ${it[3].toLowerCase()}.`, "Long-run effectiveness");
''' + CLASSIFY("cl1", "Is it expenditure-switching or expenditure-reducing?", ["Expenditure-switching", "Expenditure-reducing"],
  [("A tariff on imports", 0), ("Higher income tax", 1), ("A depreciation of the currency", 0), ("A cut in government spending", 1), ("Export subsidies", 0), ("A rise in interest rates to cut spending", 1), ("A quota on imports", 0), ("A reduction in the money supply", 1)],
  "Switching policies change relative prices; reducing policies cut total spending.") + MATCH([
  ["Expenditure-switching", "Moves spending from imports to domestic goods"],
  ["Expenditure-reducing", "Reduces total spending, including on imports"],
  ["Devaluation", "An official fall in a fixed exchange rate"],
  ["Supply-side policy", "Raises long-run competitiveness"],
  ["Retaliation", "A trading partner's response with its own barriers"],
  ["Marshall-Lerner condition", "PEDx + PEDm above one"]]) + ORDER(
  "Put the effects of expenditure-reducing policy in order.",
  ["The government raises taxes or cuts spending", "AD falls", "Imports fall", "The deficit narrows", "Output and employment may fall"],
  "Cut spending, lower imports, narrower deficit, but lower output.") + CALC([
  {"q": "A deficit of $40bn falls by 25% after a policy. What is the new deficit ($bn)?", "a": 30, "unit": "$bn", "tol": 0.5, "hint": "40 × 0.75.", "sol": "<b>$30bn</b>."},
  {"q": "Imports are $240bn and the income elasticity of demand for imports is 1.2. AD falls 5%. What is the % fall in imports?", "a": 6, "unit": "%", "tol": 0.1, "hint": "1.2 × 5.", "sol": "<b>6%</b>."},
  {"q": "What is the fall in imports in $bn?", "a": 14.4, "unit": "$bn", "tol": 0.1, "hint": "0.06 × 240.", "sol": "<b>$14.4bn</b>."},
  {"q": "A 10% tariff is charged on $200bn of imports. What is the tariff revenue ($bn), if imports do not change?", "a": 20, "unit": "$bn", "tol": 0.5, "hint": "0.10 × 200.", "sol": "<b>$20bn</b>."}]) + MCQ([
  ("An expenditure-switching policy is:", ["A tariff", "Higher income tax", "A cut in government spending", "Higher interest rates"], 0, "Changes relative prices."),
  ("An expenditure-reducing policy is:", ["Higher income tax", "A tariff", "An export subsidy", "A depreciation"], 0, "Cuts spending."),
  ("A limit of tariffs is:", ["Retaliation", "Lower prices", "More imports", "No effect on prices"], 0, "Trading partners may respond."),
  ("Supply-side policy mainly affects the deficit:", ["Slowly, in the long run", "Immediately", "Not at all", "Only in the short run"], 0, "Productivity takes time."),
  ("A cost of expenditure-reducing policy is:", ["Lower output and employment", "Higher imports", "Higher AD", "Retaliation"], 0, "Spending falls across the economy.")
], "qz1") + CARDS([
  ("Switching", "Imports to domestic goods."),
  ("Reducing", "Cut total spending."),
  ("Depreciation", "Switching via the exchange rate."),
  ("Tariff", "Switching via import prices."),
  ("Contractionary policy", "Reducing; costs output."),
  ("Supply-side", "Slow, but tackles the cause."),
  ("Limits", "Retaliation, elasticity, output."),
  ("Judge", "Cause, speed, side effects.")]) + MCQ(mc_exam)

build("as68", "as-correcting-current-account-imbalances", "Correcting Current Account Imbalances", EY,
  "6.5.1 to 6.5.2: expenditure-switching, expenditure-reducing and supply-side policies, with their limits. Animated chains, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
