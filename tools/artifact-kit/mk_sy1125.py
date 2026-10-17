"""Syllabus 11.2.5 Effects of changing exchange rates: Marshall-Lerner and the J curve. Run: python3 tools/artifact-kit/mk_sy1125.py"""
from syl import *
EY = "A Level Economics · 9708 · Syllabus 11.2.5"

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>A <b>fall</b> in the exchange rate makes <b>exports cheaper abroad and imports dearer at home</b>, but whether the <b>current account improves</b> depends on how much the quantities change. The <b class="kw">Marshall-Lerner condition</b> says a depreciation or devaluation will improve the current account only if the <b>sum of the price elasticities of demand for exports and imports is greater than 1</b>. Because buyers and sellers are slow to react (contracts, habits, lack of substitutes), elasticities are low in the short run, so the current account often <b>gets worse before it gets better</b>: the <b class="kw">J curve</b>. A rise in the exchange rate has the opposite effects.</p></div>

  <h2>1 · What a depreciation does</h2>
  <ul>
    <li><b>Price effect:</b> each export is cheaper in foreign currency, so foreigners buy more. Each import costs more in home currency, so residents buy fewer.</li>
    <li><b>Volume effect:</b> the extra export sales and the cut in imports add to the demand for domestic goods, raising aggregate demand and employment. A <b>net exports (X − M)</b> increase raises AD.</li>
    <li>The trade balance rises only if the <b>gain in volume outweighs the higher price paid for imports</b>. This is what the elasticities decide.</li>
    <li>Other effects: higher <b>imported inflation</b> (dearer raw materials and goods), a higher burden on <b>debts in foreign currency</b>, and possible <b>retaliation</b> (competitive devaluation).</li>
  </ul>

  <h2>2 · The Marshall-Lerner condition</h2>
  <div id="pic1" class="card"></div>
  <ul>
    <li><b>PEDx + PEDm &gt; 1</b> (taking the elasticities as positive numbers). Then a depreciation or devaluation <b>improves</b> the current account.</li>
    <li><b>If PEDx + PEDm = 1</b> the balance is unchanged. <b>If it is less than 1</b> the current account <b>worsens</b>: the extra amount paid for imports is greater than the gain in export sales.</li>
    <li><b>Worked example</b> (trade initially balanced at $100m each way, depreciation of 10%): if PEDx = 0.8 and PEDm = 0.6 (sum 1.4), exports rise by 8% to $108m and import spending is 100 × 1.10 × 0.94 = $103.4m, so the balance improves by about $4.6m. If PEDx = 0.3 and PEDm = 0.2 (sum 0.5), exports rise to $103m and imports cost $107.8m, so the balance <b>worsens</b> by about $4.8m.</li>
    <li>Elasticity is high when there are <b>good substitutes</b>, when the product is a <b>luxury</b>, when <b>spare capacity</b> lets exporters respond, and when <b>more time</b> has passed. It is low for essential imports such as oil or food and for primary commodity exports with inelastic supply.</li>
  </ul>

  <h2>3 · The J curve</h2>
  <div id="pic2" class="card"></div>
  <ul>
    <li><b>Short run:</b> contracts are already agreed, buyers are slow to notice price changes, and firms need time to find new suppliers or expand capacity. Short-run PEDs are <b>low (sum below 1)</b>, so the dearer import bill outweighs any gain: the current account <b>worsens</b>.</li>
    <li><b>Medium to long run:</b> contracts end, consumers switch and exporters expand output. PEDs rise (sum above 1), so the current account <b>improves</b> and eventually moves above its starting point.</li>
    <li>The graph of the current account balance against time then looks like the letter <b>J</b>. A <b>revaluation</b> may produce an <b>inverse J</b> (the account first improves, then worsens).</li>
  </ul>

  <h2>4 · The effects of changing exchange rates on the external economy</h2>
  <div class="tw"><table class="t">
    <tr><th></th><th>Depreciation or devaluation</th><th>Appreciation or revaluation</th></tr>
    <tr><td><b>Export prices abroad</b></td><td>Fall</td><td>Rise</td></tr>
    <tr><td><b>Import prices at home</b></td><td>Rise</td><td>Fall</td></tr>
    <tr><td><b>Current account</b></td><td>Improves if Marshall-Lerner holds, after a J curve</td><td>Worsens if Marshall-Lerner holds</td></tr>
    <tr><td><b>Inflation</b></td><td>Rises (imported inflation, higher AD)</td><td>Falls</td></tr>
    <tr><td><b>Employment and growth</b></td><td>May rise through net exports</td><td>May fall in export industries</td></tr>
    <tr><td><b>Foreign-currency debt</b></td><td>Burden rises</td><td>Burden falls</td></tr>
  </table></div>
  <div class="tip"><b class="h">Evaluation points</b>The effect depends on (1) the elasticities and the time frame, (2) spare capacity at home to meet the extra demand, (3) how much of exports use imported inputs, (4) whether domestic inflation wipes out the gain (the real exchange rate), (5) the reaction of trading partners, and (6) the structure of the economy, for example a low-income country exporting commodities with inelastic supply may gain little.</div>
'''

watch = '''
  <h2>1 · The Marshall-Lerner condition at work</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stM"></div>
  <h2>2 · The J curve</h2>
  <div id="stJ"></div>
'''

explore = '''
  <h2>Lab 1 · Does the depreciation work?</h2>
  <p>Trade starts balanced at 100 each way. Set the depreciation and the elasticities. The Marshall-Lerner sum decides whether the balance improves.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div>
    <div class="readout"><div><small>PEDx + PEDm</small><strong id="r1"></strong></div><div><small>Export / import bill</small><strong id="r2"></strong></div><div><small>New balance</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 300" role="img" aria-label="Bars of export revenue and import spending before and after a depreciation"></svg></div></div></div>

  <h2>Lab 2 · Draw your own J curve</h2>
  <p>Combined elasticity starts at the short-run value and rises towards the long-run value. Move both and see when the J appears.</p>
  <div class="card"><div class="grid2"><div><div id="g4"></div><div id="g5"></div>
    <div class="readout"><div><small>Lowest point</small><strong id="t1"></strong></div><div><small>After 12 periods</small><strong id="t2"></strong></div><div><small>Shape</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 420 300" role="img" aria-label="Current account balance over time after a depreciation for chosen short-run and long-run elasticities"></svg></div></div></div>
'''

practise = '''
  <h2>1 · Does the current account improve, worsen or stay the same?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the J curve in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Sterling after 2016", "After the pound fell in 2016, the UK trade deficit did not narrow quickly. Many importers and exporters were tied to contracts and supply chains, and imported components became dearer. This is often used as an example of a slow, drawn-out J curve.", "short-run elasticities being low, and why the current account may take time to improve.") +
rw("Japan's weak yen after 2013", "Japan's yen fell sharply in 2013. Exporters' profits rose when converted into yen, but the volume of exports rose less than hoped because many firms already produced abroad. Import costs for energy and food rose, and the trade balance first worsened.", "an example of the volume effect being limited, and imported inflation as a cost of depreciation.") +
rw("Commodity exporters", "Many low-income countries export primary products such as coffee, copper or cocoa. Supply in the short run is inelastic because it takes time to plant or open mines, so a depreciation may not raise export volumes much, even if the price in foreign currency falls.", "the supply side limit on a depreciation in a low-income economy, which is the link in the Paper 4 question on growth.") +
rw("Oil importers", "Countries that rely on imported oil have a very inelastic demand for imports, at least in the short run. When their currency falls, the oil bill rises sharply in local currency, which can worsen the trade balance and add to inflation.", "very low PEDm, so the Marshall-Lerner condition may fail.")
)

mc_exam = [
  ("The diagram shows a J curve: a fall in the exchange rate worsens the current account before it improves it. What is said to explain this? (May/June 2023 · 32 · Q28, reworded)", ["A time lag before price changes are recognised and acted on", "An improvement in the quality of goods produced", "Demand for imports and exports is elastic in the short run", "The supply of goods is price elastic"], 0, "In the short run buyers and sellers react slowly, so elasticities are low and the dearer import bill dominates."),
  ("What does the J-curve effect show? (May/June 2024 · 31 · Q26, reworded)", ["A depreciation works only if the sum of the elasticities of demand for exports and imports exceeds 1", "After a devaluation the current account is likely to get worse before it gets better", "In the short run the demand for imports and exports is usually price elastic", "The terms of trade decide how well a devaluation works"], 1, "The J-curve describes the time path: a worse current account first, then an improvement."),
  ("A government devalues its currency to move the current account from deficit to surplus. Under which condition would this succeed? (May/June 2024 · 32 · Q27, reworded)", ["If the combined price elasticity of demand for exports and imports is greater than 1", "If the combined price elasticity is less than 1", "If income elasticity of demand is less than 1", "If other countries impose tariffs on all imports"], 0, "This is the Marshall-Lerner condition."),
  ("The values below are short-run (SR) and long-run (LR) elasticities for exports (PEDx) and imports (PEDm). In which case does a depreciation produce a J curve? A: SR 0.5 and 0.2; LR 0.6 and 0.6. B: SR 0.5 and 0.6; LR 1.2 and 1.0. C: SR 0.6 and 0.6; LR 0.5 and 0.2. D: SR 1.2 and 1.0; LR 0.5 and 0.6. (May/June 2025 · 34 · Q27, reworded)", ["A", "B", "C", "D"], 0, "In A the short-run sum is 0.7 (below 1, so the account worsens) and the long-run sum is 1.2 (above 1, so it improves). In B the short-run sum is already 1.1."),
  ("A revaluation raises the exchange rate. The short-run PEDx and PEDm are 0.4 and 0.4 and the long-run values are 0.8 and 0.8. What shape would the current account take over time? (May/June 2025 · 31 · Q27, reworded)", ["It rises, and keeps rising", "It rises, then falls", "It falls, then rises", "It falls, and keeps falling"], 1, "In the short run the sum is 0.8 (below 1) so a revaluation improves the balance. In the long run the sum is 1.6 (above 1), so it then worsens: an inverse J."),
  ("How would a depreciation of the currency of a low-income economy most likely affect these objectives: raising the growth rate, reducing the current account deficit, reducing unemployment? (May/June 2025 · 34 · Q29, reworded)", ["Raises growth and reduces unemployment but not the deficit", "It helps all three", "Reduces the deficit and unemployment but not growth", "Reduces the deficit only"], 1, "Cheaper exports and dearer imports can increase net exports, raising AD, output and jobs and narrowing the deficit, provided the elasticity conditions are met."),
  ("Both the elasticity of demand for imported raw materials and the elasticity of demand for exports are 0.3. What is the effect of a depreciation on cost-push and demand-pull inflation? (Oct/Nov 2020 · 32 · Q29, reworded)", ["Cost-push falls; demand-pull falls", "Cost-push falls; demand-pull rises", "Cost-push rises; demand-pull falls", "Cost-push rises; demand-pull rises"], 2, "With inelastic imports the import bill and costs rise (cost-push up). With inelastic exports net exports fall, which lowers AD (demand-pull down).")
]

exam = exam_page("exchange rate changes, the Marshall-Lerner condition and the J curve",
  "We searched the A Level Economics papers in the folder (2020 to 2025). The effect of a depreciation on the economy is a regular 20 mark essay, and the Marshall-Lerner and J curve ideas appear in Paper 3 every year. One past essay is reworded below, with two practice questions and seven Paper 3 multiple choice questions.",
  [("Essay, 20 marks", "1", "May/June 2023 (42) Q4"), ("Multiple choice (Paper 3)", "7 shown below", "2020 to 2025")],
  [
  eq("Based on May/June 2023 · 9708/42 · Q4", "20 marks", "Consider the extent to which the depreciation of its foreign exchange rate contributes to the economic growth of a low-income country.",
     ["Knowledge and analysis of the effect of a depreciation on export and import prices, and so on the demand for and supply of exports and imports.",
      "Link to AD through net exports (X − M), shown with an AD and AS diagram or the multiplier; state whether the growth is actual or potential.",
      "Evaluation: the ability of supply capacity in the low-income country to respond; primary product exports often have inelastic supply compared with, say, oil; short-run employment gains but also inflation from dearer imports; the effect on debt, which rises in cost if borrowing is in foreign currency but falls in cost if in domestic currency."],
     "Price effects. Net exports raise AD (diagram). Actual growth. Supply constraints. Inflation. Debt in foreign currency.",
     [[("k", "A depreciation lowers the price of a low-income country's exports in foreign currency and raises the price of its imports."), ("n", "If the Marshall-Lerner condition holds, export revenue could rise by more than the import bill, so net exports increase. Because X − M is part of aggregate demand, AD may shift to the right, raising output through the multiplier. This is actual growth, as it uses spare capacity.")],
      [("e", "However, many low-income countries export primary products with inelastic supply in the short run, so export volumes may rise little. Dearer imported inputs and capital goods could also raise costs and inflation, and reduce potential growth. If much of the country's debt is in dollars, the cost of repayments in local currency rises. So the contribution to growth may be modest and temporary.")]]),
  eq("Practice question · modelled on the 12 mark style (no past paper)", "12 marks", "Explain, with the help of a diagram, the J curve effect and why a depreciation may make the current account worse in the short run.",
     ["Diagram: current account balance against time, falling after the depreciation and then rising above its starting point.",
      "Short run: price elasticities of demand for exports and imports are low (sum below 1) because of existing contracts, slow reactions and lack of substitutes, so the dearer import bill outweighs the extra export sales.",
      "Long run: elasticities rise (sum above 1), consumers switch and exporters expand, so the account improves (Marshall-Lerner).",
      "Mention the condition and that the speed depends on the economy."],
     "Diagram. Short-run elasticity and why. Long-run improvement. Marshall-Lerner condition.",
     [[("k", "The J curve shows the current account getting worse for a time after a depreciation before it improves, so the graph of the balance over time looks like the letter J."), ("n", "In the short run, contracts have already been agreed, consumers are slow to change their habits and there may be no easy substitutes, so demand for imports and exports is price inelastic. The dearer import bill is then greater than the extra revenue from exports, so the balance worsens.")],
      [("n", "Over time, contracts end, consumers switch to cheaper domestic goods and exporters expand output, so elasticities rise. When the sum of the elasticities is above 1, the Marshall-Lerner condition is met and the current account may improve, eventually above its starting level."), ("e", "How long this takes may depend on the economy's spare capacity and import dependence.")]]),
  eq("Practice question · modelled on the 8 mark style (no past paper)", "8 marks", "Explain the Marshall-Lerner condition and why it might not hold in a low-income country.",
     ["Condition: a depreciation improves the current account if PEDx + PEDm > 1.",
      "Reason it may fail: inelastic demand for essential imports (oil, food, capital goods); inelastic supply of commodity exports; limited spare capacity; low-quality exports; short time period.",
      "A developed chain of analysis."],
     "Condition. Reasons. A conclusion about the likelihood.",
     [[("k", "The Marshall-Lerner condition states that a depreciation or devaluation will improve the current account only if the sum of the price elasticities of demand for exports and imports is greater than 1.")],
      [("n", "In a low-income country the condition may not hold. Imports such as oil, food and machinery are essential, so demand could be inelastic, and the import bill will rise sharply when the currency falls. Exports are often primary products with inelastic supply in the short run, so export volumes may rise little."), ("e", "The condition is more likely to be met in the long run, when more substitutes and capacity are available.")]])
  ],
  )

tips = tips_html(
  [("State the condition fully.", "PEDx + PEDm greater than 1 for a depreciation to improve the current account."),
   ("Say which direction.", "Depreciation: exports cheaper, imports dearer. Appreciation is the opposite."),
   ("Label the J.", "Current account balance on the vertical axis, time on the horizontal axis, a dip then a rise above the start."),
   ("Short run versus long run.", "Elasticities are low in the short run and higher in the long run. That is the whole reason for the J."),
   ("Link net exports to AD.", "X minus M is part of aggregate demand, so a rise shifts AD right."),
   ("Mention costs.", "Imported inflation, dearer foreign debt and possible retaliation."),
   ("Evaluate for the economy.", "Low-income countries often have inelastic commodity exports and import needs.")],
  [("Condition", "A depreciation could improve the current account if the sum of the price elasticities of demand for exports and imports is greater than 1."),
   ("J curve", "The current account may first worsen after a depreciation because short-run elasticities are low, and then improve."),
   ("Imports", "A fall in the exchange rate raises the home price of imports, so the import bill may rise before quantities adjust."),
   ("Growth", "Higher net exports raise aggregate demand and may increase actual growth if there is spare capacity."),
   ("Limits", "The gain may be reduced by inflation, slow supply responses and retaliation by trading partners.")],
  [CW["define"], CW["explain"], CW["consider"], CW["evaluate"]]) + FC

js = '''
/* ---------- Marshall-Lerner bars ---------- */
const MB = (v) => 300 - v * 2.3;
function mlDraw(s) {
  let o = axes(70, 300, 730, 30, "", "Value ($m)"); [0, 50, 100].forEach((v) => (o += SV.text(64, MB(v) + 4, v, "sm", { "text-anchor": "end" })));
  o += SV.line(70, MB(100), 730, MB(100), "gr dash", op(0.6));
  const bx = (i, v, c, l, k) => SV.rect(130 + i * 200, MB(v), 90, 300 - MB(v), c, op(k)) + tag(175 + i * 200, MB(v) - 8, Lib.fmtN(v, 1), "t1", k, "middle") + tag(175 + i * 200, 322, l, "t1", k, "middle");
  o += bx(0, s.x, "f1", "Export revenue", 1) + bx(1, s.m, "f2", "Import spending", 1);
  const b = s.x - s.m; o += tag(620, 120, "Balance", "t1", 1, "middle") + tag(620, 156, (b >= 0 ? "+" : "") + Lib.fmtN(b, 1), b >= 0 ? "t3" : "t2", 1, "middle");
  if (s.n > 0) o += tag(620, 190, s.n === 1 ? "sum = 1.4: improves" : "sum = 0.5: worsens", "t4", 1, "middle");
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 340" role="img" aria-label="Export revenue and import spending bars after a depreciation when the Marshall-Lerner condition holds">${mlDraw({ x: 108, m: 103.4, n: 1 })}</svg>`;
Lib.stepper($("#stM"), { w: 760, h: 340, label: "A 10 percent depreciation: export revenue and import spending when the elasticity sum is high and low", base: { x: 100, m: 100, n: 0 }, draw: mlDraw, tween: 1100, dwell: 6200, steps: [
  { cap: "<b>Start.</b> Trade is balanced: exports $100m, imports $100m.", s: { x: 100, m: 100, n: 0 } },
  { cap: "<b>The price effect.</b> A 10% depreciation raises the home price of imports by 10% at once. Before quantities change, the import bill rises to $110m and the balance falls to −$10m.", s: { x: 100, m: 110, n: 0 } },
  { cap: "<b>Elastic demand (PEDx 0.8, PEDm 0.6, sum 1.4).</b> Exports rise 8% to $108m and import volumes fall 6%, so imports cost $103.4m. The balance improves to +$4.6m: Marshall-Lerner holds.", s: { x: 108, m: 103.4, n: 1 } },
  { cap: "<b>Inelastic demand (PEDx 0.3, PEDm 0.2, sum 0.5).</b> Exports rise only 3% to $103m and import volumes fall just 2%, so imports cost $107.8m. The balance is −$4.8m: the condition fails.", s: { x: 103, m: 107.8, n: 2 } },
] });

/* ---------- J curve ---------- */
const jb = (t) => -10 - 10 * (t / 2) * Math.exp(1 - t / 2) + 15 * (1 - Math.exp(-t / 4));
const JX = (t) => 90 + t * 52, JY = (b) => 190 - b * 7;
function jDraw(s) {
  let o = axes(70, 300, 730, 30, "Time after the depreciation", "Current account balance"); o += SV.line(70, JY(0), 730, JY(0), "gr", op(0.7)) + SV.text(66, JY(0) + 4, "0", "sm", { "text-anchor": "end" }) + SV.line(JX(0), 40, JX(0), 300, "c4 dash", op(0.8)) + tag(JX(0) + 6, 52, "depreciation", "t4");
  const pts = []; for (let t = -0.35; t <= s.p * 12 + 0.001 && t <= 12; t += 0.25) pts.push([JX(t), JY(t <= 0 ? -10 : jb(t))]);
  if (pts.length > 1) o += SV.path(Lib.ptsPath(pts), "c1");
  const t0 = Math.min(12, s.p * 12), last = pts.length ? pts[pts.length - 1] : [JX(0), JY(-10)];
  o += SV.circle(last[0], last[1], 6, "dot4");
  if (s.l > 0) o += tag(JX(3), 320, "Short run: contracts and habits, low elasticities", "t2", s.l, "middle");
  if (s.l > 1) o += tag(JX(7), 232, "Adjustment: elasticities rise", "t1", Math.min(1, s.l - 1), "middle");
  if (s.l > 2) o += tag(JX(11), JY(3.5) - 12, "Long run: ML holds", "t3", Math.min(1, s.l - 2), "end");
  return o;
}
$("#pic2").innerHTML = `<svg viewBox="0 0 760 340" role="img" aria-label="J curve: the current account falls after a depreciation then rises above its starting level">${jDraw({ p: 1, l: 3 })}</svg>`;
Lib.stepper($("#stJ"), { w: 760, h: 340, label: "J curve: current account balance over time after a depreciation", base: { p: 0, l: 0 }, draw: jDraw, tween: 1500, dwell: 6200, steps: [
  { cap: "<b>Before.</b> The country has a current account deficit of about 10 units. The currency then depreciates.", s: { p: 0, l: 0 } },
  { cap: "<b>Short run.</b> Contracts are already agreed and buyers are slow to switch, so quantities barely change but the import bill rises. The <b>deficit widens</b> to about 14.", s: { p: 0.17, l: 1 } },
  { cap: "<b>Adjustment.</b> As contracts end, consumers switch and exporters expand, elasticities rise. The balance starts to recover and passes its starting level.", s: { p: 0.6, l: 2 } },
  { cap: "<b>Long run.</b> The sum of elasticities is above 1, so the current account is better than before the depreciation. The path looks like the letter J.", s: { p: 1, l: 3 } },
] });

/* ---------- Lab 1 ---------- */
function labM() {
  if (!$("#dp") || !$("#ex") || !$("#im")) return;
  const d = +$("#dp").value / 100, ex = +$("#ex").value / 10, im = +$("#im").value / 10, x = 100 * (1 + ex * d), m = 100 * (1 + d) * (1 - im * d), b = x - m, sum = ex + im;
  $("#r1").textContent = Lib.fmtN(sum, 1); $("#r2").textContent = Lib.fmtN(x, 1) + " / " + Lib.fmtN(m, 1); $("#r3").textContent = (b >= 0 ? "+" : "") + Lib.fmtN(b, 1);
  $("#rv").textContent = sum > 1.001 ? `The sum of the elasticities (${Lib.fmtN(sum, 1)}) is above 1: the Marshall-Lerner condition holds, so the balance improves to ${b >= 0 ? "+" : ""}${Lib.fmtN(b, 1)}.` : sum < 0.999 ? `The sum (${Lib.fmtN(sum, 1)}) is below 1: the condition fails and the balance worsens to ${Lib.fmtN(b, 1)}. The dearer import bill outweighs the export gain.` : "The sum is exactly 1: roughly no change in the balance (the exact result depends on the starting position).";
  const Y = (v) => 270 - v * 1.7; let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(46, 16, "$m", "sm");
  [["Exports before", 100, "f1"], ["Exports after", x, "f1"], ["Imports before", 100, "f2"], ["Imports after", m, "f2"]].forEach(([l, v, c], i) => { const px = 55 + i * 88; o += SV.rect(px, Y(v), 60, 270 - Y(v), c, i % 2 ? {} : op(0.55)) + SV.text(px + 30, 288, l.split(" ")[1], "sm", { "text-anchor": "middle" }) + tag(px + 30, Y(v) - 6, Lib.fmtN(v, 1), "t1", 1, "middle"); });
  o += SV.text(115, 304, "Exports", "sm", { "text-anchor": "middle" }) + SV.text(291, 304, "Imports", "sm", { "text-anchor": "middle" });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "dp", label: "Depreciation, % ", min: 5, max: 30, step: 5, value: 10, fmt: (v) => v, onInput: labM });
Lib.slider($("#g2"), { id: "ex", label: "PED of exports × 10 ", min: 0, max: 20, step: 1, value: 8, fmt: (v) => (v / 10).toFixed(1), onInput: labM });
Lib.slider($("#g3"), { id: "im", label: "PED of imports × 10 ", min: 0, max: 20, step: 1, value: 6, fmt: (v) => (v / 10).toFixed(1), onInput: labM });
labM();

/* ---------- Lab 2 ---------- */
function labJ() {
  if (!$("#sr") || !$("#lr")) return;
  const sr = +$("#sr").value / 10, lr = +$("#lr").value / 10, f = (t) => -10 + 20 * ((sr + (lr - sr) * (1 - Math.exp(-t / 3))) - 1);
  let lo = 0, lt = 0; for (let t = 0; t <= 12; t += 0.1) { if (f(t) < lo) { lo = f(t); } } lo = Math.min(lo, -10);
  const end = f(12), shape = sr < 1 && lr > 1 ? "J curve" : sr >= 1 ? "Improves at once" : "Never improves";
  $("#t1").textContent = Lib.fmtN(lo, 1); $("#t2").textContent = (end >= 0 ? "+" : "") + Lib.fmtN(end, 1); $("#t3").textContent = shape;
  $("#tv").textContent = shape === "J curve" ? `Short-run elasticities sum to ${sr.toFixed(1)} (below 1), so the account worsens first, to about ${Lib.fmtN(lo, 1)}. They rise to ${lr.toFixed(1)} (above 1), so by period 12 the balance is ${Lib.fmtN(end, 1)}.` : shape === "Improves at once" ? "With the short-run sum already above 1, the current account improves straight away, so there is no J." : "The long-run sum stays below 1, so the Marshall-Lerner condition never holds and the current account stays worse than before.";
  const X = (t) => 40 + t * 28, Y = (b) => 150 - b * 6; let o = SV.line(40, 280, 400, 280) + SV.line(40, 280, 40, 20) + SV.text(400, 296, "Time", "sm", { "text-anchor": "end" }) + SV.text(46, 16, "Current account balance", "sm") + SV.line(40, Y(-10), 400, Y(-10), "gr dash", op(0.7)) + SV.text(44, Y(-10) - 6, "start", "sm");
  const pts = []; for (let t = 0; t <= 12; t += 0.25) pts.push([X(t), Math.max(25, Math.min(275, Y(f(t))))]);
  $("#labB").innerHTML = o + SV.path(Lib.ptsPath(pts), "c1");
}
Lib.slider($("#g4"), { id: "sr", label: "Short-run PEDx + PEDm × 10 ", min: 2, max: 14, step: 1, value: 6, fmt: (v) => (v / 10).toFixed(1), onInput: labJ });
Lib.slider($("#g5"), { id: "lr", label: "Long-run PEDx + PEDm × 10 ", min: 6, max: 24, step: 1, value: 16, fmt: (v) => (v / 10).toFixed(1), onInput: labJ });
labJ();

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "What happens to the current account?", ["Improves", "Worsens", "No change"],
  [("Depreciation when PEDx + PEDm = 1.6", 0), ("Depreciation when PEDx + PEDm = 0.6", 1), ("Depreciation in the short run, when contracts are fixed and elasticities are low", 1), ("Depreciation in the long run when the sum exceeds 1", 0), ("Depreciation when PEDx + PEDm = 1.0", 2), ("Devaluation when the country imports only essential goods with very inelastic demand", 1), ("Revaluation when PEDx + PEDm = 1.8", 1), ("Revaluation when PEDx + PEDm = 0.5", 0)],
  "Depreciation improves the balance if the sum is above 1. A revaluation does the opposite.") + MATCH([
  ["Marshall-Lerner condition", "PEDx + PEDm > 1 for a depreciation to improve the current account"],
  ["J curve", "A current account that worsens before it improves"],
  ["Price effect", "Imports cost more in home currency after a depreciation"],
  ["Volume effect", "Export sales rise and import purchases fall"],
  ["Inverse J", "A revaluation that first improves, then worsens, the account"],
  ["Net exports", "Exports minus imports, a component of AD"]]) + ORDER(
  "Put the J curve in order.",
  ["The exchange rate depreciates", "Import prices rise but quantities hardly change (contracts, habits)", "The current account deficit widens", "Elasticities rise as consumers and firms adjust", "The current account improves above its starting level"],
  "Low elasticities first, higher elasticities later.") + CALC([
  {"q": "PEDx is 0.9 and PEDm is 0.4. Calculate PEDx + PEDm.", "a": 1.3, "unit": "", "tol": 0.01, "hint": "Add them.", "sol": "<b>1.3</b>, which is above 1: depreciation should improve the current account."},
  {"q": "A 10% depreciation is followed by a rise in export volumes with PEDx = 1.2. By what percentage do export volumes rise (%)?", "a": 12, "unit": "%", "tol": 0.05, "hint": "PED × % change in price.", "sol": "1.2 × 10% = <b>12%</b>."},
  {"q": "Imports cost $200m. After a depreciation their home-currency price rises 8% and volume falls 5%. Calculate the new import spending ($m, 1 decimal place).", "a": 205.2, "unit": "$m", "tol": 0.1, "hint": "200 × 1.08 × 0.95.", "sol": "200 × 1.08 × 0.95 = <b>$205.2m</b>."},
  {"q": "Exports were $200m and rise 6%. Imports are $205.2m. Calculate the new trade balance ($m, 1 decimal place).", "a": 6.8, "unit": "$m", "tol": 0.1, "hint": "212 − 205.2.", "sol": "<b>+$6.8m</b>, so the balance has improved from 0."}]) + MCQ([
  ("The Marshall-Lerner condition says a depreciation improves the current account if:", ["PEDx + PEDm > 1", "PEDx + PEDm < 1", "PEDx = PEDm", "Both elasticities are zero"], 0, "The sum of the elasticities must be greater than 1."),
  ("The J curve occurs because, in the short run:", ["Elasticities are low", "Elasticities are very high", "Inflation falls", "Exports fall"], 0, "Contracts and habits delay the response."),
  ("A depreciation will raise the price of:", ["Imports in home currency", "Exports in home currency", "Domestic services only", "Nothing"], 0, "Imports cost more in home currency."),
  ("Which makes the Marshall-Lerner condition less likely to hold?", ["Many substitutes for imports", "Imports are essential and have no substitutes", "Exporters have spare capacity", "Plenty of time has passed"], 1, "Inelastic demand for imports keeps the sum low."),
  ("A depreciation could cause inflation because:", ["Imports and imported inputs cost more", "Exports fall", "Interest rates fall", "Wages fall"], 0, "Imported inflation and higher AD.")
], "qz1") + CARDS([
  ("Marshall-Lerner", "Depreciation improves the current account if PEDx + PEDm > 1."),
  ("J curve", "Current account worsens first, then improves."),
  ("Why a J?", "Short-run elasticities are low."),
  ("Inverse J", "A revaluation may improve, then worsen, the account."),
  ("Price effect", "Imports dearer in home currency."),
  ("Volume effect", "More exports sold, fewer imports bought."),
  ("Net exports", "X − M, part of AD."),
  ("Costs of depreciation", "Imported inflation, dearer foreign debt, retaliation.")]) + MCQ(mc_exam)

build("sy1125", "marshall-lerner-j-curve", "Marshall-Lerner and the J Curve", EY,
  "11.2.5: the effect of a change in the exchange rate on the current account, the Marshall-Lerner condition and the J curve. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
