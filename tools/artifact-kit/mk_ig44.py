"""Builds the three IGCSE Economics 4.4 Supply-side policy reviews (4.4.1 to 4.4.3), written from scratch.
Run: python3 tools/artifact-kit/mk_ig44.py"""
from igsy import *
F = Old("fisc")
M = Old("mon")
HEAD = M.j_((2, 25)) + F.j_((139, 160))   # axes helpers, then asP / solveAD / adLine / adChart
CL = lambda t: f"IGCSE Economics · 0455 · {t}"

COMMON = '''
function solve2(sh, a) {
  const c = 90 + 0.8 * sh; let y = (c - 30 + 0.4 * a) / 1.2;
  if (y - a > 60) y = (c + 78 + 2.2 * a) / 3;
  return [y, c - 0.8 * y, c];
}
function adasChart(s) {
  const sh = s.sh, a = s.a, [y1, p1, c] = solve2(sh, a), movedAD = Math.abs(sh) >= 1, movedAS = Math.abs(a) >= 1;
  const pts = (x) => [[QX(Math.max(0, x)), PY(x < 0 ? 30 - 0.4 * x : 30)], [QX(60 + x), PY(54)], [QX(87.7 + x), PY(115)]];
  let o = axes("Price level", "Real GDP");
  if (movedAS) o += SV.path(ptsPath(pts(0)), "c3", { opacity: 0.4 });
  o += SV.path(ptsPath(pts(a)), "c3") + SV.text(QX(87.7 + a) + 6, PY(115) + 4, movedAS ? "AS₁" : "AS", "lbl bd t3");
  o += adLine(90, "c1", "AD", { t: "t1", attrs: { opacity: movedAD ? 0.4 : 1 } });
  if (movedAD) o += adLine(c, "c2", "AD₁", { t: "t2" });
  o += hline(50) + vline(50, 50) + ylab(50, "P") + xlab(50, "Y") + SV.circle(QX(50), PY(50), 6, "dot1", { opacity: movedAD || movedAS ? 0.45 : 1 });
  if (movedAD || movedAS) o += hline(p1, "gr", y1) + vline(y1, p1) + SV.circle(QX(y1), PY(p1), 6, "dot2") + ylab(p1, "P₁", "sm bd") + xlab(y1, "Y₁", "sm bd");
  return o;
}
const mkChain = (list, col) => (s) => {
  const bh = 46, gap = 14, x = 110, w = 540; let o = "";
  list.forEach((t, i) => {
    const v = clamp(s.n - i, 0, 1); if (v <= 0) return;
    const y = 14 + i * (bh + gap);
    let g = SV.rect(x, y, w, bh, "", { rx: 8, style: `fill:var(${col});fill-opacity:0.16;stroke:var(${col});stroke-width:2` });
    g += SV.circle(x - 28, y + bh / 2, 15, "dot1", { style: `fill:var(${col})` }) + SV.text(x - 28, y + bh / 2 + 5, i + 1, "lbl bd", { "text-anchor": "middle", style: "fill:var(--surface);font-size:14px" });
    g += SV.text(x + w / 2, y + bh / 2 + 5, t, "lbl bd", { "text-anchor": "middle", style: "font-size:14px" });
    if (i < list.length - 1) g += SV.line(x + w / 2, y + bh + 1, x + w / 2, y + bh + gap - 3, "ax", { style: "stroke-width:2" }) + SV.arrowHead(x + w / 2, y + bh + gap, "d", "dot1");
    o += `<g opacity="${v}">${g}</g>`;
  });
  return o;
};
const chainSteps = (caps) => caps.map((c, i) => ({ cap: c, s: { n: i + 1 } }));
function button_table(btnId, outId, data, cols, fn) {
  const show = (i) => {
    $("#" + btnId).innerHTML = data.map((q, j) => `<button class="b${j === i ? " pri" : ""}" data-j="${j}">${q.n}</button>`).join("");
    $$("#" + btnId + " .b").forEach((b) => (b.onclick = () => show(+b.dataset.j)));
    $("#" + outId).innerHTML = fn(data[i]);
  };
  show(0);
}
'''

# =========================================================== 4.4.1 Definition
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p><span class="kw">Supply-side policy</span> is the use of government measures to <b>increase the economy's ability to produce</b>: its productive capacity and aggregate supply. Where fiscal and monetary policy work on <b>demand</b> (AD), supply-side policy works on <b>supply</b> (AS). A successful policy shifts AS to the right, so the economy can produce more goods and services at each price level.</p></div>

  <h2>Why aggregate supply matters</h2>
  <p><span class="kw">Aggregate supply (AS)</span> is the total output firms are willing to supply at each price level. It depends on the <b>quantity</b> and <b>quality</b> of the factors of production (land, labour, capital, enterprise) and on how efficiently firms use them. Anything that raises these shifts AS to the right.</p>
  <div class="grid2">
    <div class="card"><h3>If AD shifts right</h3><p>Output rises, but the price level rises too, and if the economy is close to full capacity most of the effect is <b>inflation</b>.</p></div>
    <div class="card"><h3>If AS shifts right</h3><p>Output rises and the price level <b>falls</b> (or rises by less). Growth with less inflation: the best of both.</p></div>
  </div>
  <p>The same idea appears on a <b>production possibility curve</b>: a successful supply-side policy shifts the PPC outwards, because the economy can now produce more of everything.</p>

  <h2>What supply-side policy aims to do</h2>
  <ul>
    <li>Raise <b>productivity</b> and potential output, so long-run growth is higher.</li>
    <li>Reduce <b>unemployment</b>, especially structural unemployment where workers' skills do not match vacancies.</li>
    <li>Reduce firms' <b>costs</b>, which helps hold prices down and make exports more competitive.</li>
    <li>Improve <b>efficiency</b> and encourage firms to compete and invest.</li>
  </ul>

  <h2>Demand-side compared with supply-side</h2>
  <div class="tw"><table class="t">
    <tr><th></th><th>Demand-side (fiscal and monetary)</th><th>Supply-side</th></tr>
    <tr><td><b>Works on</b></td><td>Aggregate demand</td><td>Aggregate supply</td></tr>
    <tr><td><b>Tools</b></td><td>Taxes, government spending, interest rates, money supply, exchange rate</td><td>Education, infrastructure, labour market reforms, tax cuts, deregulation, incentives, privatisation</td></tr>
    <tr><td><b>Time to work</b></td><td>Can be quick (months)</td><td>Usually slow (years)</td></tr>
    <tr><td><b>Main effect</b></td><td>Short-run changes in output and prices</td><td>Long-run growth in productive capacity</td></tr>
    <tr><td><b>Main risk</b></td><td>Inflation, deficit</td><td>Costs, winners and losers, uncertain results</td></tr>
  </table></div>
  <p class="note">Supply-side policies are sometimes called <b>microeconomic</b> policies because many work by changing how individual markets, firms and workers behave.</p>
'''
js = HEAD + COMMON + '''
/* PPC outward */
function ppcChart(s) {
  const ox = 90, oy = 330, X = 250 * s.s, Y = 215 * s.s, X0 = 250, Y0 = 215;
  const curve = (X, Y) => { const p = []; for (let t = 0; t <= 90; t += 5) { const r = (t * Math.PI) / 180; p.push([ox + X * Math.cos(r), oy - Y * Math.sin(r)]); } return p; };
  let o = SV.line(ox, oy, ox, 30) + SV.line(ox, oy, 700, oy) + SV.text(ox + 6, 40, "Capital goods", "sm") + SV.text(700, oy + 24, "Consumer goods", "sm", { "text-anchor": "end" });
  if (s.s > 1.02) o += SV.path(ptsPath(curve(X0, Y0)), "c3", { opacity: 0.4 }) + SV.text(ox + X0 * 0.7071 + 10, oy - Y0 * 0.7071 + 22, "PPC", "lbl bd t3", { opacity: 0.6 });
  o += SV.path(ptsPath(curve(X, Y)), "c1") + SV.text(ox + X * 0.7071 + 12, oy - Y * 0.7071 - 6, s.s > 1.02 ? "PPC₁" : "PPC", "lbl bd t1");
  const px = ox + X * 0.7071, py = oy - Y * 0.7071;
  o += SV.line(px, py, px, oy, "gr") + SV.line(ox, py, px, py, "gr") + SV.circle(px, py, 7, s.s > 1.02 ? "dot2" : "dot1");
  return o;
}
Lib.stepper($("#stP"), { w: 760, h: 400, label: "Supply-side policy shifts the PPC outwards", base: { s: 1 }, draw: ppcChart, steps: [
  { cap: "A production possibility curve shows the <b>most the economy can produce</b> with its resources and technology. Here the economy produces on the curve.", s: { s: 1 } },
  { cap: "The government improves <b>education, infrastructure</b> and the way markets work. Workers are more productive and firms have better capital. The economy's <b>productive capacity</b> grows.", s: { s: 1.2 } },
  { cap: "The PPC shifts <b>outwards</b> to PPC₁. The economy can produce more of everything: this is what a <b>successful supply-side policy</b> achieves, and the same as a shift of AS to the right.", s: { s: 1.2 } },
] });
Lib.stepper($("#stS"), { w: 760, h: 400, label: "Supply-side policy shifts AS to the right", base: { sh: 0, a: 0 }, draw: adasChart, steps: [
  { cap: "The economy starts at <b>Y</b> and <b>P</b>, where AD meets AS.", s: { sh: 0, a: 0 } },
  { cap: "A <b>supply-side policy</b> (for example training for workers) raises productive capacity. <b>AS shifts right</b> to AS₁. Real GDP rises to Y₁ and the price level <b>falls</b> to P₁.", s: { sh: 0, a: 14 } },
  { cap: "Compare an <b>increase in AD</b> instead: AD shifts right and output rises, but the price level <b>rises</b> too.", s: { sh: 14, a: 0 } },
  { cap: "If both shift, output rises a lot and the price level barely changes: <b>fast growth without inflation</b>. <b>Evaluate:</b> supply-side effects take years to appear.", s: { sh: 14, a: 14 } },
] });

/* Lab 1 */
function labS() {
  if (!$("#ga") || !$("#gb")) return;
  const sh = +$("#ga").value, a = +$("#gb").value, [y, p] = solve2(sh, a);
  $("#sa1").textContent = (y - 50 >= 0 ? "+" : "−") + money(Math.abs(y - 50), 1); $("#sa2").textContent = (p - 50 >= 0.05 ? "+" : p - 50 <= -0.05 ? "−" : "") + money(Math.abs(p - 50), 1);
  $("#sa3").textContent = a > 0 && sh === 0 ? "Supply-side" : sh > 0 && a === 0 ? "Demand-side" : sh > 0 && a > 0 ? "Both" : "None";
  $("#sav").textContent = sh === 0 && a === 0 ? "Nothing has changed. Move one of the sliders." : a > 0 && sh === 0 ? `AS shifts right: output rises by ${money(y - 50, 1)} and the price level falls by ${money(50 - p, 1)}. Growth with lower inflationary pressure.` : sh > 0 && a === 0 ? `AD shifts right: output rises by ${money(y - 50, 1)} but the price level rises by ${money(p - 50, 1)}. More inflationary pressure.` : `Both shift: output rises by ${money(y - 50, 1)} and the price level changes by ${p - 50 >= 0 ? "+" : "−"}${money(Math.abs(p - 50), 1)}. A lot of growth with little inflation.`;
  $("#labS").innerHTML = adasChart({ sh, a });
}
Lib.slider($("#g1"), { id: "ga", label: "Demand-side policy: shift in AD", min: 0, max: 30, step: 2, value: 0, fmt: (v) => "+" + v, onInput: labS });
Lib.slider($("#g2"), { id: "gb", label: "Supply-side policy: shift in AS", min: 0, max: 30, step: 2, value: 14, fmt: (v) => "+" + v, onInput: labS });

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each policy <b>demand-side</b> or <b>supply-side</b>?", buckets: [{ label: "Demand-side" }, { label: "Supply-side" }], items: [
  { text: "Cut interest rates to raise spending", b: 0 }, { text: "Raise government spending in a recession", b: 0 }, { text: "Cut VAT to raise consumption", b: 0 }, { text: "Increase the money supply", b: 0 },
  { text: "Fund training for unemployed workers", b: 1 }, { text: "Build new motorways and broadband", b: 1 }, { text: "Remove rules that stop new firms entering a market", b: 1 }, { text: "Privatise a state-owned firm", b: 1 },
], done: "Demand-side shifts AD; supply-side shifts AS." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Supply-side policy", "Measures to raise the economy's productive capacity and shift AS to the right"],
  ["Aggregate supply", "Total output firms will supply at each price level"],
  ["Productivity", "Output per worker (or per unit of input)"],
  ["Productive capacity", "The most an economy can produce with its resources"],
  ["Potential output", "Output when resources are fully and efficiently used"],
  ["Economic growth", "A rise in real GDP over time"],
], done: "Good vocabulary scores marks." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how a successful supply-side policy could reduce inflationary pressure</b>.", items: [
  "The government improves education, infrastructure or competition",
  "Productivity rises and firms' costs per unit fall",
  "Aggregate supply shifts to the right",
  "Real GDP rises",
  "The price level falls, or rises by less than otherwise",
], done: "Growth with lower inflationary pressure." });
''' + calc_js([
    ("A firm produces 6,000 units a month with 40 workers. What is output per worker?", 150, "6,000 ÷ 40 = <b>150 units</b> per worker.", None, None),
    ("After training, the same 40 workers produce 7,200 units. What is the percentage rise in productivity?", 20, "(7,200 − 6,000) ÷ 6,000 × 100 = <b>20%</b>.", None, None),
    ("Real GDP rises from $800bn to $840bn. What is the rate of economic growth (%)?", 5, "40 ÷ 800 × 100 = <b>5%</b>.", None, None),
]) + mcq_js("qz1", [
    ("What is a supply-side policy?", ["A measure to increase aggregate demand", "A measure to increase aggregate supply", "A change in interest rates", "A change in the exchange rate"], 1, "Supply-side policy aims to raise productive capacity."),
    ("What is the likely effect of a successful supply-side policy?", ["Aggregate supply shifts left", "Aggregate supply shifts right", "The price level rises sharply", "The exchange rate falls"], 1, "AS shifts right, raising output."),
    ("Which is a supply-side policy?", ["Cutting income tax to raise spending", "Funding training for workers", "Raising interest rates", "Increasing benefits"], 1, "Training raises the quality of labour."),
    ("A successful supply-side policy is most likely to:", ["Raise output and lower prices", "Lower output and raise prices", "Raise both output and prices a lot", "Have no effect"], 0, "AS shifts right: more output at a lower price level."),
    ("Which statement about supply-side policy is correct?", ["Its effects are usually quick", "It usually takes years to work", "It only affects demand", "It is the same as monetary policy"], 1, "Better skills and capital take time to build."),
]) + "\n" + cards_js([("Supply-side policy", "Government measures to increase the economy's productive capacity by shifting aggregate supply to the right."), ("Aggregate supply", "The total output firms are willing to supply at each price level."), ("Productivity", "Output per worker, or per unit of input."), ("Productive capacity", "The maximum output an economy can produce."), ("Potential output", "The level of output when resources are fully and efficiently used."), ("Economic growth", "A rise in real GDP over time."), ("Structural unemployment", "Unemployment caused by a mismatch between workers' skills and the jobs available."), ("Aggregate demand", "Total spending in an economy: C + I + G + (X − M)."), ("Microeconomic policy", "Policy that works on individual markets, firms and workers.")]) + "labS();\n"
explore = '''
  <h2>Lab 1 · Demand-side or supply-side?</h2>
  <p>Shift AD, AS or both and compare what happens to output and the price level. The faint lines are the originals.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div></div>
    <div><div class="readout"><div><small>Change in real GDP</small><strong id="sa1"></strong></div><div><small>Change in price level</small><strong id="sa2"></strong></div><div><small>Policy</small><strong id="sa3"></strong></div></div><div class="verdict" id="sav"></div></div></div>
    <svg id="labS" viewBox="0 0 760 400" role="img" aria-label="Aggregate demand and supply diagram"></svg>
    <p class="note">Illustrative model with spare capacity at low output and an AS curve that steepens as the economy nears full capacity.</p>
  </div>
'''
ex = exam(
    Q(1, "Define", 2, "What is meant by a supply-side policy?", "Two ideas: government measures, and that they raise aggregate supply or productive capacity.",
      "[K|A supply-side policy is a government measure designed to increase aggregate supply,] [K|by raising the quantity or quality of resources or improving the efficiency with which they are used.]", warn="Describing demand-side measures such as cutting taxes to raise spending. Supply-side is about the ability to produce."),
    Q(2, "Explain", 4, "Explain one difference between supply-side policy and demand-side policy.", "Use 'whereas'. Compare what they shift, or how long they take.",
      "[K|Supply-side policy aims to increase aggregate supply and productive capacity,] [K|whereas demand-side policy, such as fiscal or monetary policy, aims to change aggregate demand.] [N|Supply-side effects, such as better skills or new roads, usually take years to appear,] [N|whereas a change in interest rates or government spending can affect spending much more quickly.]"),
    Q(3, "Explain", 4, "Using an AD/AS diagram, explain how a successful supply-side policy could affect real GDP and the price level.", "Draw AS shifting right, label Y to Y₁ and P to P₁, then explain in words.",
      "[K|A successful supply-side policy increases the economy's productive capacity, so aggregate supply shifts to the right.] [N|At each price level firms can now supply more,] [N|so real GDP rises from Y to Y₁ and the price level falls from P to P₁, or rises by less than it otherwise would.] [A|For example, better training could raise workers' productivity.]"),
    Q(4, "Analyse", 6, "Analyse how supply-side policy could help to reduce inflationary pressure.", "Chain: policy, productivity or costs, AS shifts right, price level. Name one measure.",
      "[K|Supply-side policy aims to raise aggregate supply.] [A|For example, spending on training or infrastructure could raise productivity and lower firms' costs per unit.] [N|Lower costs could allow firms to hold or cut prices, and AS shifts to the right.] [N|Output is higher at each price level, so the price level may fall or rise more slowly, even if demand grows.] [N|This could reduce cost-push and demand-pull pressure.] [E|However, the effect could take years to appear.]", key=True),
)
tp = tips([
    ("Supply-side = raise AS.", "Productive capacity, not spending."),
    ("Draw AS shifting right.", "Label Y to Y₁ and P to P₁; say output rises and prices fall."),
    ("Name a measure.", "Training, infrastructure, tax cuts, privatisation, deregulation."),
    ("Time lags.", "Supply-side effects take years: use this in evaluation."),
    ("Contrast with demand-side.", "Demand-side can be quicker but may be more inflationary."),
], cmds("Define", "Explain", "Analyse"))
body = page(CL("4.4.1 Definition of supply-side policy"), "Definition of Supply-Side Policy", "What supply-side policy is, how it shifts aggregate supply and the PPC, and how it differs from demand-side policy. Syllabus 4.4.1.",
    learn=learn, watch=watch(("Supply-side policy and the PPC", "stP"), ("Supply-side policy and AD / AS", "stS")), explore=explore,
    practise=practise(("Demand-side or supply-side?", "cl1", "card"), ("Match the term", "m1", "card"), ("Order the chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("Germany's labour market reforms", "In the early 2000s Germany reformed its labour market, making unemployment benefits conditional on job search and making it easier to offer flexible jobs. Unemployment fell over the following years, though critics say some of the new jobs were low paid.", "A supply-side measure aimed at structural unemployment, with an evaluation point about inequality."),
        rw("China's market reforms", "From the late 1970s China gradually deregulated markets, allowed private firms and invested heavily in infrastructure and education. Output grew very fast for decades.", "Several measures together raising productive capacity. A past paper uses China as a case."),
        rw("Training schemes", "Several governments, for example Singapore, fund training accounts or apprenticeships so workers can learn new skills as industries change.", "Education and training raising the quality of labour, with a long time lag.")),
    exam=ex, tips=tp)
write("ss1", body, js, "Definition of Supply-Side Policy", "ig-supply-side-definition")

# =========================================================== 4.4.2 Measures
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>The syllabus lists seven supply-side measures: <b>education and training, infrastructure spending, labour market reforms, lower direct taxes, deregulation, improving incentives to work and invest, and privatisation</b>. Each works by raising the <b>quality</b> or <b>quantity</b> of resources, or by raising <b>efficiency</b> and <b>incentives</b>. For each one learn how it shifts AS, who gains, and the catch.</p></div>

  <h2>The seven measures</h2>
  <div class="tw"><table class="t">
    <tr><th>Measure</th><th>What it means</th><th>How it raises AS</th></tr>
    <tr><td><b>Education and training</b></td><td>Schools, colleges, apprenticeships, retraining</td><td>More skilled and productive workers; workers can move to jobs that are available</td></tr>
    <tr><td><b>Infrastructure spending</b></td><td>Roads, rail, ports, power, broadband</td><td>Lower costs and faster trade; better capital for all firms</td></tr>
    <tr><td><b>Labour market reforms</b></td><td>Easier hiring and firing, weaker union power, reduced unemployment benefit, help with job search and mobility</td><td>More people willing to take work; lower and more flexible labour costs</td></tr>
    <tr><td><b>Lower direct taxes</b></td><td>Cuts in income tax and corporation tax</td><td>More incentive to work, save and invest; firms keep more profit to invest</td></tr>
    <tr><td><b>Deregulation</b></td><td>Removing rules and barriers that restrict competition</td><td>More firms enter, competition lowers costs and raises efficiency</td></tr>
    <tr><td><b>Improving incentives to work and invest</b></td><td>Tax breaks for investment, grants and subsidies for new firms, lower benefits for the able to work</td><td>More employment, more investment, more start-ups</td></tr>
    <tr><td><b>Privatisation</b></td><td>Selling state-owned firms to private owners</td><td>Profit motive and competition cut costs; sale raises revenue</td></tr>
  </table></div>

  <h2>Raising the quality or quantity of resources</h2>
  <div class="grid2">
    <div class="card"><h3>Quality of labour and capital</h3><p>Education and training raise labour quality. Infrastructure and investment raise the quality of capital. Both are slow and costly.</p></div>
    <div class="card"><h3>Quantity of labour and capital</h3><p>Lower taxes and reduced benefits may increase the number of people willing to work. Investment incentives raise the capital stock.</p></div>
  </div>
  <div class="grid2">
    <div class="card"><h3>Incentives</h3><p>If people keep more of what they earn, and benefits are not much higher than wages, more people may choose to work, work longer or start a firm.</p></div>
    <div class="card"><h3>Efficiency and competition</h3><p>Deregulation and privatisation expose firms to competition and the profit motive, so they may cut waste. Without competition, privatisation may just replace a public monopoly with a private one.</p></div>
  </div>

  <h2>Evaluating the measures</h2>
  <ul>
    <li><b>Time lags:</b> training and infrastructure take years to pay off.</li>
    <li><b>Cost and opportunity cost:</b> education and infrastructure need spending, which may mean borrowing or giving up other uses.</li>
    <li><b>Uncertainty:</b> training may not match the skills employers want; lower taxes may not change behaviour much.</li>
    <li><b>Winners and losers:</b> labour reforms and cuts to benefits may widen inequality; privatisation may cost jobs.</li>
    <li><b>Demand effects:</b> cutting benefits or wages can reduce spending and AD.</li>
  </ul>
'''
js = HEAD + COMMON + '''
const SKILL = ["The government funds more education and training", "Workers gain skills and qualifications", "Labour becomes more productive and more mobile", "Firms can produce more per worker; skill gaps narrow", "AS shifts right: more output and lower unemployment, after a lag"];
const INCENT = ["The government cuts income tax and trims unemployment benefit", "Take-home pay from working rises relative to benefits", "More people look for work or work longer hours", "Firms have more workers to hire; costs may fall", "AS shifts right: more output and employment"];
const EFFIC = ["The government privatises a firm and deregulates the market", "Private owners seek profit and face competition", "Firms cut waste and costs, and new firms enter", "Prices may fall and quality and choice may rise", "Productivity and AS rise; the sale also raises revenue"];
Lib.stepper($("#stK"), { w: 760, h: 400, label: "Education and training", base: { n: 0 }, draw: mkChain(SKILL, "--good"), steps: chainSteps(["Step 1: the government <b>funds education and training</b>.", "Workers gain <b>skills and qualifications</b>.", "Labour is <b>more productive and more mobile</b>: workers can move into vacancies.", "Firms can produce more per worker, and <b>structural unemployment</b> may fall.", "<b>AS shifts right</b>. <b>Evaluate:</b> it takes years, costs money and only works if the skills match employers' needs."]) });
Lib.stepper($("#stI"), { w: 760, h: 400, label: "Lower taxes and better incentives", base: { n: 0 }, draw: mkChain(INCENT, "--accent"), steps: chainSteps(["The government <b>cuts income tax</b> and reduces unemployment benefit.", "<b>Take-home pay from working rises</b> compared with life on benefits.", "More people <b>look for work or work longer</b>.", "Firms find it easier to hire, and <b>labour costs may fall</b>.", "<b>AS shifts right.</b> <b>Evaluate:</b> some people may not change behaviour, revenue may fall, and cutting benefits can hurt the poor and reduce spending."]) });
Lib.stepper($("#stE"), { w: 760, h: 400, label: "Privatisation and deregulation", base: { n: 0 }, draw: mkChain(EFFIC, "--warn"), steps: chainSteps(["The government <b>privatises</b> a state-owned firm and <b>deregulates</b> the market.", "The firm now has <b>private owners seeking profit</b> and faces competition.", "Firms <b>cut waste and costs</b>; new firms can enter the market.", "Prices may fall and quality and choice may rise.", "<b>Productivity and AS rise</b>. <b>Evaluate:</b> a private monopoly could charge high prices, and jobs or services may be lost."]) });

/* Lab 1: is it worth working */
function labW() {
  if (!$("#wa") || !$("#wb")) return;
  const t = +$("#wa").value, b = +$("#wb").value, take = 400 * (1 - t / 100), gain = take - b;
  $("#wa1").textContent = "$" + Math.round(take); $("#wa2").textContent = "$" + b; $("#wa3").textContent = (gain >= 0 ? "+$" : "−$") + Math.round(Math.abs(gain));
  $("#wav").textContent = gain < 50 ? "Working pays little more than benefits: there is a weak incentive to take a job, which can keep people unemployed (an unemployment trap)." : gain > 200 ? "Working pays much more than benefits: a strong incentive to work." : "Working pays more than benefits, but the gap is modest.";
  const base = 300, k = 0.6;
  let o = SV.line(100, base, 680, base);
  [["Take-home pay", take, "--accent"], ["Unemployment benefit", b, "--warn"]].forEach(([n, v, c], i) => {
    const x = 170 + i * 250, h = v * k;
    o += SV.rect(x, base - h, 150, h, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.text(x + 75, base - h - 8, "$" + Math.round(v), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 75, base + 22, n, "sm", { "text-anchor": "middle" });
  });
  $("#labW").innerHTML = o + SV.text(100, 30, "Per week", "sm");
}
Lib.slider($("#g1"), { id: "wa", label: "Income tax rate on a $400 weekly wage", min: 0, max: 50, step: 5, value: 20, fmt: (v) => v + "%", onInput: labW });
Lib.slider($("#g2"), { id: "wb", label: "Weekly unemployment benefit", min: 0, max: 350, step: 25, value: 150, fmt: (v) => "$" + v, onInput: labW });

/* Lab 2: measure picker */
const MS = [
  { n: "Education and training", how: "Raises skills, productivity and mobility of workers.", as: "Quality of labour: AS shifts right (long run).", gain: "Workers, firms, and the government through tax revenue.", lag: "Slow (years)", catch: "Costly; skills must match jobs." },
  { n: "Infrastructure", how: "Roads, rail, power and broadband cut firms' costs and travel times.", as: "Better capital for all firms: AS shifts right.", gain: "Firms, regions and consumers.", lag: "Slow (years)", catch: "Big cost, borrowing, delays and possible environmental damage." },
  { n: "Labour market reforms", how: "Easier hiring and firing, weaker union power, reduced benefits, help with job search.", as: "More people willing to work and lower labour costs.", gain: "Firms and people who find work.", lag: "Medium", catch: "Job insecurity, lower wages for some, inequality." },
  { n: "Lower direct taxes", how: "Income tax cuts raise take-home pay; corporation tax cuts raise retained profit.", as: "More work effort and more investment.", gain: "Workers, entrepreneurs, firms.", lag: "Medium", catch: "Revenue may fall; high earners gain most; behaviour may not change much." },
  { n: "Deregulation", how: "Removes rules and barriers so new firms can enter.", as: "More competition, lower costs, more output.", gain: "Consumers and new firms.", lag: "Medium", catch: "Less protection for consumers, workers and the environment." },
  { n: "Incentives to work and invest", how: "Tax breaks for investment, grants and subsidies, lower benefits.", as: "More employment, investment and start-ups.", gain: "Firms and workers.", lag: "Medium", catch: "Cost to the government; may not be well targeted." },
  { n: "Privatisation", how: "Sells state firms to private owners who seek profit and face competition.", as: "Lower costs and higher efficiency; sale raises revenue.", gain: "Government (sale), consumers if prices fall, owners.", lag: "Medium", catch: "Private monopolies may raise prices; jobs and services may be lost." },
];
button_table("msBtns", "msOut", MS, 0, (p) => `<div class="tw"><table class="t"><tr><th>How it works</th><th>Effect on AS</th><th>Who gains</th><th>Time lag</th><th>The catch</th></tr><tr><td>${p.how}</td><td>${p.as}</td><td>${p.gain}</td><td>${p.lag}</td><td>${p.catch}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Which <b>kind of supply-side measure</b> is each?", buckets: [{ label: "Raise skills (education, training)" }, { label: "Improve incentives (tax, benefits)" }, { label: "Raise efficiency (privatisation, deregulation)" }, { label: "Better capital (infrastructure)" }], items: [
  { text: "Fund apprenticeships", b: 0 }, { text: "Retraining for workers in declining industries", b: 0 },
  { text: "Cut income tax rates", b: 1 }, { text: "Reduce unemployment benefit for those able to work", b: 1 },
  { text: "Sell a state-owned airline", b: 2 }, { text: "Remove licence rules that block new firms", b: 2 },
  { text: "Build a new railway", b: 3 }, { text: "Roll out national broadband", b: 3 },
], done: "Seven measures, four ideas: skills, incentives, efficiency, capital." });
Lib.classify($("#cl2"), { prompt: "Is each a <b>supply-side measure</b> or <b>not</b>?", buckets: [{ label: "Supply-side" }, { label: "Not supply-side" }], items: [
  { text: "Cut corporation tax to encourage investment", b: 0 }, { text: "Privatise the state telephone company", b: 0 }, { text: "Fund training for the unemployed", b: 0 }, { text: "Deregulate bus services", b: 0 },
  { text: "Cut interest rates to boost spending", b: 1 }, { text: "Raise government spending on a stimulus package", b: 1 }, { text: "Allow the exchange rate to fall", b: 1 }, { text: "Raise VAT to cut the deficit", b: 1 },
], done: "Supply-side raises productive capacity; the others work on demand." });
Lib.match($("#m1"), { prompt: "Match the measure to how it raises AS.", pairs: [
  ["Education and training", "Raises skills and productivity of workers"],
  ["Infrastructure spending", "Cuts firms' costs and improves transport and communications"],
  ["Labour market reforms", "Makes hiring easier and raises willingness to work"],
  ["Lower direct taxes", "Raises take-home pay and retained profit"],
  ["Deregulation", "Removes barriers so more firms can compete"],
  ["Privatisation", "Transfers firms to private owners seeking profit"],
], done: "Link each measure to a mechanism." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how lower income tax could raise AS</b>.", items: [
  "The government cuts income tax rates",
  "Take-home pay from working rises",
  "More people choose to work, or work longer hours",
  "The labour force and output potential grow",
  "AS shifts to the right",
], done: "An incentive-based supply-side chain." });
''' + calc_js([
    ("A worker earns $500 a week and pays income tax of 20%. What is take-home pay ($)?", 400, "500 × 0.8 = <b>$400</b>.", None, None),
    ("The tax rate falls to 15%. What is take-home pay now ($)?", 425, "500 × 0.85 = <b>$425</b>.", None, None),
    ("Unemployment benefit is $300 a week. Take-home pay from a job is $420. How much better off is the worker in work ($)?", 120, "420 − 300 = <b>$120</b>.", None, None),
    ("A government sells a state firm for $2bn. The firm made a loss of $0.1bn a year. If the government no longer pays that subsidy, how much does it save in 5 years ($bn)?", 0.5, "0.1 × 5 = <b>$0.5bn</b> (plus the $2bn sale revenue).", None, None),
]) + mcq_js("qz1", [
    ("Which supply-side measure would help to match the skills of workers to job vacancies?", ["Lower interest rates", "Education and training", "Higher VAT", "Higher government spending on benefits"], 1, "Training raises skills and mobility."),
    ("Privatisation is most likely to:", ["Transfer firms to private owners", "Raise government ownership of firms", "Reduce competition by law", "Raise tax rates"], 0, "State-owned firms are sold to private owners."),
    ("Which is deregulation?", ["Removing rules that restrict firms entering a market", "Building new roads", "Cutting income tax", "Raising the minimum wage"], 0, "Deregulation reduces barriers to competition."),
    ("A cut in income tax may be a supply-side measure because it:", ["Reduces the deficit", "May raise the incentive to work", "Reduces productivity", "Raises AD only"], 1, "More take-home pay can raise labour supply."),
    ("Which is a possible disadvantage of privatisation?", ["A private monopoly could raise prices", "Firms always become less efficient", "It always raises government spending", "It reduces the incentive to cut costs"], 0, "Without competition, private owners may exploit market power."),
    ("Which measure is most likely to raise the quality of capital?", ["Spending on infrastructure", "Cutting unemployment benefit", "Cutting the exchange rate", "Raising interest rates"], 0, "Roads, rail and broadband are capital."),
]) + "\n" + cards_js([("Education and training", "Spending on schools, colleges and training to raise workers' skills and productivity."), ("Infrastructure", "The roads, rail, ports, energy and broadband networks an economy relies on."), ("Labour market reforms", "Changes to make labour markets more flexible, such as easier hiring and weaker union power."), ("Direct tax cuts", "Lower income tax or corporation tax to raise incentives to work and invest."), ("Deregulation", "Removing rules and barriers that restrict competition."), ("Privatisation", "Selling state-owned firms to private owners."), ("Incentive", "A reward that encourages people or firms to act in a particular way."), ("Unemployment trap", "When benefits are so close to wages that working pays little more than being unemployed."), ("Mobility of labour", "How easily workers can move between jobs, industries or places.")]) + "labW();\n"
explore = '''
  <h2>Lab 1 · Is it worth working?</h2>
  <p>A job pays $400 a week before tax. Change the tax rate and the weekly benefit and see how much better off a worker is in work.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div></div>
    <div><div class="readout"><div><small>Take-home pay</small><strong id="wa1"></strong></div><div><small>Benefit</small><strong id="wa2"></strong></div><div><small>Gain from working</small><strong id="wa3"></strong></div></div><div class="verdict" id="wav"></div></div></div>
    <svg id="labW" viewBox="0 0 760 340" role="img" aria-label="Take-home pay compared with unemployment benefit"></svg>
  </div>

  <h2>Lab 2 · Measure picker</h2>
  <p>Pick a supply-side measure to see how it works, who gains and the catch.</p>
  <div class="card"><div class="row" id="msBtns"></div><div id="msOut"></div></div>
'''
ex = exam(
    Q(1, "Identify", 2, "Identify two supply-side policy measures.", "Two named measures from the list. Short phrases.",
      "[K|Education and training (or infrastructure spending).] [K|Privatisation (or deregulation, lower direct taxes, labour market reforms).]"),
    Q(2, "Explain", 4, "Explain two supply-side policy measures that a government could use. (May/June 2020, P23 style)", "Two different measures, each with a mechanism. Say how each raises productivity or output.",
      "[K|One measure is education and training.] [N|This could raise the skills and productivity of workers and help them move into jobs that are available, so aggregate supply could rise.] [K|A second measure is privatisation.] [N|Private owners seek profit and may face competition, so they could cut costs and raise efficiency, which may raise output and lower prices.]"),
    Q(3, "Explain", 4, "Explain how lower income tax rates could increase the supply of labour.", "Link tax to take-home pay and then to the decision to work.",
      "[K|Lower income tax rates raise workers' take-home pay.] [N|Working becomes more rewarding compared with leisure or unemployment benefit, so more people may enter the labour force or work longer hours.] [N|Aggregate supply could rise as a result.] [E|However, some workers may not change their hours, particularly if they have fixed commitments.]"),
    Q(4, "Explain", 4, "Explain how privatisation could improve efficiency.", "Profit motive, competition, cutting costs. Add a limit.",
      "[K|Privatisation is the sale of state-owned firms to private owners.] [N|Private owners are motivated by profit, so they may cut waste and costs, and if the firm faces competition it may also improve quality and prices.] [E|However, if it becomes a private monopoly it may raise prices.]"),
    Q(5, "Discuss", 8, "Discuss whether or not education and training is the best supply-side policy measure.", "Weigh education and training against another measure. For: raises skills, mobility, productivity, lowers structural unemployment. Against: slow, costly, mismatch; other measures may be quicker.",
      "[K|Education and training is a supply-side measure that raises the skills of the labour force.] [N|It could raise productivity and help workers move into jobs that are available, reducing structural unemployment.] [N|Better skills could attract investment and raise earnings, increasing tax revenue in the long run.] [E|However, it takes years to work and has an opportunity cost.] [N|By comparison, privatisation or lower taxes could affect incentives more quickly, and infrastructure may lower costs for all firms.] [N|Training is also wasted if the skills taught do not match what employers want.] [E|Overall, education and training is likely to be a strong long-term measure, but the best policy depends on the problem: if unemployment is structural it may be the best, whereas if firms need cheaper transport, infrastructure may be more effective.]", key=True),
)
tp = tips([
    ("Seven measures:", "education and training, infrastructure, labour market reforms, lower direct taxes, deregulation, incentives, privatisation."),
    ("For each measure give a mechanism.", "'Training raises productivity' is a developed point; 'training is good' is not."),
    ("Say it raises AS.", "Link every measure to a shift of AS, higher output and often lower prices."),
    ("Evaluate with time lag, cost and uncertainty.", "And with who loses: lower benefits, job losses, monopoly."),
    ("Use hedged words.", "Could, may, is likely to."),
], cmds("Identify", "Explain", "Discuss"))
body = page(CL("4.4.2 Supply-side policy measures"), "Supply-Side Policy Measures", "Education and training, infrastructure, labour market reforms, lower direct taxes, deregulation, incentives and privatisation: how each raises AS and the catch. Syllabus 4.4.2.",
    learn=learn, watch=watch(("Education and training", "stK"), ("Lower taxes and better incentives", "stI"), ("Privatisation and deregulation", "stE")), explore=explore,
    practise=practise(("Which kind of measure?", "cl1", "card"), ("Supply-side or not?", "cl2", "card"), ("Match the measure", "m1", "card"), ("Order the chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("Reforming labour markets", "Germany's early-2000s reforms tightened the rules on unemployment benefit and encouraged flexible jobs. Unemployment fell, but some of the new jobs were low paid.", "Labour market reforms and an evaluation point about inequality."),
        rw("Privatising state firms", "In the 1980s the UK sold state-owned firms such as the telephone and gas companies. Many became more efficient, but in some cases prices rose and critics said competition was weak.", "Privatisation: efficiency gain and the risk of private monopoly."),
        rw("Infrastructure for growth", "Many governments fund roads, rail, ports and broadband. Large projects such as high-speed rail often cost more and take longer than planned.", "Infrastructure lowering costs, and a good source of evaluation: cost and time lag."),
        rw("Cutting corporation tax", "Several countries, including Ireland, have used low corporation tax rates to attract foreign firms and investment.", "Lower direct taxes and incentives to invest, with the cost of lost revenue."),
        rw("Deregulation in China", "As China loosened controls on prices and entry from the late 1970s, many private firms were created. A recent paper used China to show how deregulation can move an economy towards a market system.", "Deregulation, competition and the speed of change."),
    ), exam=ex, tips=tp)
write("ss2", body, js, "Supply-Side Policy Measures", "ig-supply-side-measures")

# =========================================================== 4.4.3 Effects on aims
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>Supply-side policy can help a government reach several macroeconomic aims at once: <b>higher growth, lower unemployment, lower inflationary pressure</b> and a <b>better balance of payments</b>. Unlike fiscal and monetary policy it does this by raising productive capacity, so there is less conflict between growth and inflation. But it is slow, costly and its effects are uncertain, and some measures may harm equity or the environment.</p></div>

  <h2>Aim by aim</h2>
  <div class="tw"><table class="t">
    <tr><th>Aim</th><th>How supply-side policy could help</th><th>Possible problem</th></tr>
    <tr><td>Economic growth</td><td>AS shifts right: potential output and long-run growth rise</td><td>Takes years; measures may not raise productivity</td></tr>
    <tr><td>Full employment</td><td>Training and mobility reduce structural unemployment; incentives help the unemployed find work</td><td>Does not cure cyclical (demand-deficient) unemployment; some measures cost jobs at first</td></tr>
    <tr><td>Stable prices</td><td>Lower costs and higher output hold prices down (cost-push pressure falls)</td><td>Little effect on inflation caused by excess demand in the short run</td></tr>
    <tr><td>Balance of payments</td><td>Lower costs make exports more competitive; domestic goods may replace imports</td><td>Higher incomes also raise imports</td></tr>
    <tr><td>Redistribution of income</td><td>Training can raise incomes of the low-skilled; some jobs created</td><td>Lower direct taxes and benefit cuts may widen inequality</td></tr>
    <tr><td>Environmental sustainability</td><td>Green infrastructure and training in new technologies</td><td>Deregulation and faster growth may increase pollution</td></tr>
  </table></div>

  <h2>Supply-side policy and the budget</h2>
  <ul>
    <li><b>Could reduce the deficit:</b> if growth and employment rise, tax revenue rises and benefit spending falls; privatisation raises sale revenue and ends subsidies to loss-making firms.</li>
    <li><b>Could widen the deficit at first:</b> education and infrastructure spending cost money, and tax cuts reduce revenue.</li>
  </ul>

  <h2>Why supply-side policy may not work as planned</h2>
  <ul>
    <li><b>Time lags.</b> It can take years for training or new roads to raise output.</li>
    <li><b>Cost.</b> Many measures need government spending, which has an opportunity cost.</li>
    <li><b>Uncertainty.</b> Workers may not respond to tax cuts; skills may not match jobs.</li>
    <li><b>Wrong problem.</b> If unemployment is caused by low demand (cyclical), supply-side policy alone may not help and cuts to benefits could reduce demand.</li>
    <li><b>Side effects.</b> Inequality, loss of public services, private monopolies, pollution.</li>
  </ul>
'''
GAIN = '''
const SG = ["Government spends on training, infrastructure and incentives", "AS shifts right: productive capacity rises", "Real GDP rises: economic growth", "Structural unemployment falls as skills match vacancies", "Costs fall, so the price level falls or rises by less", "Exports become more competitive: current account may improve"];
Lib.stepper($("#stG"), { w: 760, h: 400, label: "Gains of a successful supply-side policy", base: { n: 0 }, draw: mkChain(SG, "--good"), steps: chainSteps(["The government uses <b>supply-side measures</b>: training, infrastructure, incentives.", "<b>AS shifts right</b>: the economy can produce more at each price level.", "<b>Growth:</b> real GDP rises.", "<b>Jobs:</b> better skills and incentives mean <b>structural unemployment</b> may fall.", "<b>Prices:</b> lower costs and more output mean the price level falls or rises by less.", "<b>Balance of payments:</b> lower costs could make exports more competitive. <b>Evaluate:</b> all of this takes years, and some measures have costs."]) });
const SC = [
  { n: "Education and training", g: "▲ long run", u: "▼ structural falls", i: "▼ eases", c: "▲ may improve", b: "▲ revenue later, ▼ cost first", catch: "Slow and costly; skills must match jobs." },
  { n: "Infrastructure", g: "▲ long run", u: "▼ construction jobs, then others", i: "▼ lower costs", c: "▲ exports easier", b: "▼ large cost", catch: "Delays, cost and environmental damage." },
  { n: "Labour market reforms", g: "▲ may rise", u: "▼ may fall", i: "▼ lower wage costs", c: "▲ more competitive", b: "▲ less benefit spending", catch: "Insecurity and inequality; cuts in benefits reduce demand." },
  { n: "Lower direct taxes", g: "▲ incentives", u: "▼ may fall", i: "◆ little effect", c: "◆ little effect", b: "▼ revenue falls", catch: "High earners gain most; behaviour may not change." },
  { n: "Deregulation", g: "▲ competition", u: "▼ new firms, new jobs", i: "▼ competition cuts prices", c: "▲ may improve", b: "◆ small effect", catch: "Less protection for consumers, workers and the environment." },
  { n: "Privatisation", g: "▲ efficiency", u: "▲ job losses at first", i: "▼ may fall (or rise if monopoly)", c: "◆ little effect", b: "▲ sale revenue", catch: "Private monopoly; loss of public service; job losses." },
];
button_table("scBtns", "scOut", SC, 0, (p) => `<div class="tw"><table class="t"><tr><th>Growth</th><th>Unemployment</th><th>Inflation</th><th>Current account</th><th>Budget</th></tr><tr><td>${p.g}</td><td>${p.u}</td><td>${p.i}</td><td>${p.c}</td><td>${p.b}</td></tr></table></div><div class="warn"><b class="h">The catch</b>${p.catch}</div>`);
const UT = [
  { n: "Structural", d: "Workers' skills do not match vacancies, often after an industry declines.", w: "Supply-side policy works well: training and mobility help match workers and jobs.", t: "Training, retraining, relocation help." },
  { n: "Frictional", d: "People are between jobs and searching.", w: "Supply-side policy helps: better job information, and lower benefits may speed job search.", t: "Job information, benefit conditions." },
  { n: "Cyclical (demand-deficient)", d: "Not enough demand in a recession.", w: "Supply-side policy alone may not help: there are no jobs because spending is low. Demand-side policy fits better.", t: "Fiscal and monetary policy." },
  { n: "Seasonal", d: "Work depends on the time of year, such as tourism or farming.", w: "Limited: the pattern of work is the cause, though training for other industries may help.", t: "Retraining; year-round industries." },
];
button_table("utBtns", "utOut", UT, 0, (p) => `<div class="tw"><table class="t"><tr><th>What it is</th><th>Will supply-side policy help?</th><th>Better tool</th></tr><tr><td>${p.d}</td><td>${p.w}</td><td>${p.t}</td></tr></table></div>`);
function labA() {
  if (!$("#ab") || !$("#aa")) return;
  const a = +$("#aa").value, sh = +$("#ab").value, [y, p] = solve2(sh, a);
  $("#ab1").textContent = (y - 50 >= 0 ? "+" : "−") + money(Math.abs(y - 50), 1); $("#ab2").textContent = (p - 50 >= 0.05 ? "+" : p - 50 <= -0.05 ? "−" : "") + money(Math.abs(p - 50), 1);
  $("#abv").textContent = a === 0 && sh === 0 ? "Move a slider." : a > sh ? "A bigger supply-side effect: output grows with lower or falling prices. But it took years to build." : sh > a ? "A bigger demand-side effect: output rises but with more inflationary pressure." : "Equal shifts: growth with a roughly stable price level.";
  $("#labA").innerHTML = adasChart({ sh, a });
}
Lib.slider($("#g3"), { id: "aa", label: "Supply-side policy (AS shift)", min: 0, max: 30, step: 2, value: 14, fmt: (v) => "+" + v, onInput: labA });
Lib.slider($("#g4"), { id: "ab", label: "Demand-side policy (AD shift)", min: 0, max: 30, step: 2, value: 0, fmt: (v) => "+" + v, onInput: labA });
'''
js = HEAD + COMMON + GAIN + '''
/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each a <b>gain</b> or a <b>cost or risk</b> of supply-side policy?", buckets: [{ label: "Gain" }, { label: "Cost or risk" }], items: [
  { text: "Real GDP could rise in the long run", b: 0 }, { text: "Structural unemployment could fall", b: 0 }, { text: "Firms' costs could fall, holding prices down", b: 0 }, { text: "Exports could become more competitive", b: 0 },
  { text: "It can take years to work", b: 1 }, { text: "Education and infrastructure are costly", b: 1 }, { text: "Cuts in benefits and taxes could widen inequality", b: 1 }, { text: "Privatisation could create a private monopoly", b: 1 },
], done: "Every policy has gains and costs: that is evaluation." });
Lib.classify($("#cl2"), { prompt: "Which <b>macroeconomic aim</b> does each measure mainly support?", buckets: [{ label: "Growth" }, { label: "Lower unemployment" }, { label: "Stable prices" }, { label: "Balance of payments" }], items: [
  { text: "Infrastructure that raises long-run productive capacity", b: 0 }, { text: "Tax breaks for business investment", b: 0 },
  { text: "Retraining for workers in declining industries", b: 1 }, { text: "Help with job search", b: 1 },
  { text: "Deregulation that cuts firms' costs", b: 2 }, { text: "Competition that holds prices down", b: 2 },
  { text: "Lower costs make exports cheaper", b: 3 }, { text: "Home-produced goods replace imports", b: 3 },
], done: "Name the aim, then follow the chain." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how supply-side policy could reduce structural unemployment</b>.", items: [
  "The government funds retraining for workers in a declining industry",
  "Workers gain skills that employers need",
  "Workers can fill vacancies in growing industries",
  "The mismatch between workers and jobs narrows",
  "Structural unemployment falls",
], done: "A chain for a 6-mark analysis." });
''' + calc_js([
    ("Unemployment falls from 2.5 million to 2.0 million. The labour force is 25 million. What is the new unemployment rate (%)?", 8, "2.0 ÷ 25 × 100 = <b>8%</b>.", None, None),
    ("Real GDP rises from $600bn to $624bn after supply-side reforms. What is the percentage growth?", 4, "24 ÷ 600 × 100 = <b>4%</b>.", None, None),
    ("A government runs a deficit of $20bn. Growth raises tax revenue by $4bn and cuts benefit spending by $2bn. What is the new deficit ($bn)?", 14, "20 − 4 − 2 = <b>$14bn</b>.", None, None),
]) + mcq_js("qz1", [
    ("What is the most likely effect of a successful supply-side policy on an economy?", ["Falling real GDP", "A rise in productive capacity and potential output", "Higher inflation and unemployment", "A bigger budget deficit"], 1, "AS shifts right, raising potential output."),
    ("Which type of unemployment is most likely to fall because of education and training?", ["Cyclical", "Structural", "Seasonal only", "None"], 1, "Training matches workers' skills to vacancies."),
    ("Supply-side policy is less likely to help when unemployment is caused by:", ["A lack of skills", "A recession with low demand", "A decline in an industry", "Job search delays"], 1, "Low demand needs demand-side policy."),
    ("Which is a possible disadvantage of cutting unemployment benefit as a supply-side measure?", ["It may reduce spending by the poor", "It always raises employment", "It raises the deficit", "It cuts productivity"], 0, "Lower benefits reduce incomes and may reduce AD."),
    ("A supply-side policy could reduce a budget deficit if it:", ["Raises employment and tax revenue", "Lowers GDP", "Raises benefits", "Raises imports"], 0, "More jobs mean more tax and fewer benefits."),
]) + "\n" + cards_js([("Structural unemployment", "Unemployment caused by a mismatch between workers' skills and the jobs available."), ("Frictional unemployment", "Unemployment of people between jobs and searching for work."), ("Cyclical unemployment", "Unemployment caused by lack of demand in a recession."), ("Cost-push inflation", "A rise in the price level caused by rising costs of production."), ("Potential output", "The level of output when resources are fully and efficiently used."), ("Time lag", "The delay between a policy change and its effects."), ("Unemployment trap", "When benefits are so close to wages that working pays little more."), ("Private monopoly", "A single privately owned firm dominating a market, which may raise prices.")]) + "showSC0(); labA();\n".replace("showSC0();", "")
explore = '''
  <h2>Lab 1 · Supply-side or demand-side effects?</h2>
  <p>Set the size of a supply-side shift and a demand-side shift and compare the effects on output and the price level.</p>
  <div class="card"><div class="grid2"><div><div id="g3"></div><div id="g4"></div></div>
    <div><div class="readout"><div><small>Change in real GDP</small><strong id="ab1"></strong></div><div><small>Change in price level</small><strong id="ab2"></strong></div></div><div class="verdict" id="abv"></div></div></div>
    <svg id="labA" viewBox="0 0 760 400" role="img" aria-label="Aggregate demand and supply diagram"></svg>
  </div>

  <h2>Lab 2 · Supply-side policy scorecard</h2>
  <p>Pick a measure and see the usual effect on each aim, and the catch.</p>
  <div class="card"><div class="row" id="scBtns"></div><div id="scOut"></div></div>

  <h2>Lab 3 · Will supply-side policy cure it?</h2>
  <p>Pick a type of unemployment and see whether supply-side policy is the right tool.</p>
  <div class="card"><div class="row" id="utBtns"></div><div id="utOut"></div></div>
'''
ex = exam(
    Q(1, "Analyse", 6, "Analyse how supply-side policy measures could reduce unemployment. (Oct/Nov 2023, P22)", "Cover several measures, each with a mechanism: education, lower taxes or benefits, lower corporation tax, privatisation or deregulation. Reward the same point once.",
      "[K|Supply-side policy measures aim to increase aggregate supply.] [N|Education and training raise skills and mobility, so workers can fill vacancies and structural unemployment could fall.] [N|Lower income tax or lower unemployment benefit could increase the incentive to find work quickly, reducing frictional and voluntary unemployment.] [N|Lower corporation tax and tax incentives could encourage firms to invest and expand output, increasing demand for workers.] [N|Privatisation and deregulation could lower costs and raise efficiency, so firms may be able to afford more workers.] [E|However, these measures take time to work.]", key=True),
    Q(2, "Discuss", 8, "Discuss whether or not the use of supply-side policy measures will reduce unemployment. (May/June 2022, P21)", "Two sides. For: training, incentives, investment and competition. Against: time lag, does not cure cyclical unemployment, benefit cuts reduce demand. Judge with 'it depends on the type of unemployment'.",
      "[K|Supply-side policy measures are designed to increase aggregate supply.] [N|Education and training can improve workers' skills and mobility, which could reduce structural unemployment, and lower income tax or lower unemployment benefit could raise the incentive to work.] [N|Privatisation, deregulation and lower corporation tax could encourage firms to expand and employ more workers.] [E|However, these measures can take years to work.] [N|They are unlikely to reduce cyclical unemployment caused by low demand in a recession, because firms will not hire if they cannot sell more, and a cut in unemployment benefit could reduce spending and make the problem worse.] [E|Overall, supply-side policy is more likely to reduce unemployment that is structural or frictional. For cyclical unemployment demand-side policy may work better, so the answer depends on the cause.]", key=True),
    Q(3, "Discuss", 8, "Discuss whether supply-side policy measures will reduce a government's budget deficit. (Feb/Mar 2025, P22)", "Both sides. For: growth, tax revenue, privatisation revenue, less benefit spending. Against: spending on education and infrastructure, tax cuts reduce revenue, time lag. Do not confuse a budget deficit with a trade deficit.",
      "[K|A budget deficit is when government spending is higher than revenue.] [N|Supply-side policy could reduce it if education and training raise productivity, growth and employment, since higher incomes raise direct and indirect tax revenue and fewer people claim benefits.] [N|Privatisation could raise revenue from the sale and end subsidies to loss-making state firms, and profitable private firms may pay more tax.] [E|However, these effects can take years to appear.] [N|In the short run, spending on education and infrastructure raises government spending, and tax cuts reduce revenue, so the deficit could widen.] [E|Overall, supply-side policy is more likely to reduce the deficit in the long run if it succeeds in raising growth, but in the short run it may increase it. The outcome depends on the size of the measures and how quickly output responds.]", key=True),
    Q(4, "Discuss", 8, "Discuss whether or not supply-side policy measures always promote economic growth. (May/June 2022, P23)", "The word 'always' invites 'not always'. Show how they could promote growth, then why they might not.",
      "[K|Economic growth is a rise in real GDP, and supply-side measures aim to raise it by increasing productive capacity.] [N|Training could make workers more productive, infrastructure could cut costs and tax incentives could raise investment, all shifting AS to the right.] [E|However, they do not always work.] [N|Training may not match the skills firms need, firms and workers may not respond to tax cuts, and large projects can be late or wasteful.] [N|Cuts in benefits could reduce demand, and if the economy is in recession, low demand rather than supply may be holding growth back.] [E|Overall, supply-side policy is likely to promote growth in the long run when measures are well targeted, but it is not guaranteed. The result depends on the measure chosen and on the state of demand.]", key=True),
    Q(5, "Discuss", 8, "Discuss whether or not supply-side policy measures can reduce inflation. (Oct/Nov 2021, P22)", "For: lower costs, higher output, competition. Against: little effect on excess demand, slow, some measures raise AD.",
      "[K|Supply-side policy raises aggregate supply, which can lower the price level or slow price rises.] [N|Training and infrastructure could raise productivity and lower costs per unit, so firms could hold or cut prices; deregulation and privatisation could increase competition.] [N|With a higher supply of goods, demand-pull pressure may ease.] [E|However, the effects can take years.] [N|Supply-side policy does little to reduce inflation caused by excess demand in the short run, and tax cuts could even raise spending and prices.] [E|Overall, supply-side policy could reduce inflation over the long term, particularly cost-push inflation, but demand-side policy may be needed for faster results.]", key=True),
)
tp = tips([
    ("Match the cause of unemployment to the policy.", "Structural and frictional: supply-side. Cyclical: demand-side."),
    ("Give a long-run gain and a short-run cost.", "Training raises productivity later but costs money now."),
    ("Budget deficit is not a trade deficit.", "A past paper punished this: keep to government spending and revenue."),
    ("Always evaluate.", "Time lag, cost, uncertainty, inequality, side effects."),
    ("'Always' means 'not always'.", "Question the word in the exam and show when it fails."),
], cmds("Analyse", "Discuss"))
body = page(CL("4.4.3 Effects of supply-side policy measures on macroeconomic aims"), "Effects of Supply-Side Policy on the Aims", "How supply-side policy measures could help a government meet its macroeconomic aims, and why they may not work as planned. Syllabus 4.4.3.",
    learn=learn, watch=watch(("Gains of a successful supply-side policy", "stG"), ("Supply-side policy and AD / AS", "stS")), explore=explore,
    practise=practise(("Gain or cost?", "cl1", "card"), ("Which aim does it support?", "cl2", "card"), ("Order the chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("Fewer people out of work after reform", "Countries that combined retraining, job-search help and flexible labour rules, such as Germany in the 2000s, saw unemployment fall while others had high unemployment for longer. Some critics note a rise in low-paid jobs.", "Supply-side measures reducing unemployment, evaluated with inequality."),
        rw("Selling state firms to raise revenue", "Governments have raised large sums by privatising firms. This helped to reduce deficits in the short run but removed future profits and sometimes led to higher prices.", "Privatisation and the budget: short-run revenue against long-run loss."),
        rw("Long delays on big projects", "Major infrastructure projects often take a decade or more and cost more than first planned.", "A clear example of time lags and costs when evaluating supply-side policy."),
        rw("Uganda and unemployment", "A past paper describes a government using supply-side measures to cope with persistently high unemployment.", "Linking measures to the cause of unemployment: structural against cyclical."),
    ), exam=ex, tips=tp)
write("ss3", body, js, "Effects of Supply-Side Policy on the Aims", "ig-supply-side-aims")
