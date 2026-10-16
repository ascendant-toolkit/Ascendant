"""Syllabus 9.2.1-9.2.2 Actual and potential growth, output gaps (chapter 42). Run: python3 tools/artifact-kit/mk_sy921.py"""
from syl import *
EY = "A Level Economics · 9708 · Syllabus 9.2.1 to 9.2.2"

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p><b class="kw">Actual growth</b> is the percentage rise in real GDP from one period to the next. <b class="kw">Potential growth</b> is the rise in the economy's productive capacity, shown by the LRAS curve or the PPC shifting outwards. The <b class="kw">output gap</b> is actual output minus potential output: a <b>positive</b> gap means the economy is running above capacity (inflation pressure), a <b>negative</b> gap means spare capacity (unemployment). Governments try to keep the gap near zero while raising potential growth over time.</p></div>

  <h2>1 · Actual growth and potential growth</h2>
  <div class="grid2">
    <div class="card"><h3>Actual growth (9.2.1)</h3><p>The increase in <b>real GDP</b> over a period, usually a year. On a PPC it is a move from <b>inside</b> the curve towards it. On AD and AS it is a rise in real output at the current price-level equilibrium.</p><div class="formula">growth % = (GDP₂ − GDP₁) ÷ GDP₁ × 100</div></div>
    <div class="card"><h3>Potential growth (9.2.1)</h3><p>The increase in the <b>maximum</b> output the economy can sustain. It comes from more or better <b>factors of production</b> and from technology. On a PPC the curve moves out. On AD and AS the <b>LRAS shifts right</b>.</p></div>
  </div>
  <div class="tip"><b class="h">Short run and long run</b>Actual growth can be fast for a while by using up spare capacity, but it cannot be kept up beyond potential. Only potential growth raises the speed limit. Actual growth can also be <b>negative</b> in a recession; potential growth is rarely negative (a war or disaster that destroys capital is an exception).</div>
  <div id="pic1" class="card"></div>

  <h2>2 · Output gaps (9.2.2)</h2>
  <div class="formula">output gap % = (actual output − potential output) ÷ potential output × 100</div>
  <div class="tw"><table class="t">
    <tr><th></th><th>Positive output gap</th><th>Negative output gap</th></tr>
    <tr><td><b>Actual vs potential</b></td><td>Actual &gt; potential</td><td>Actual &lt; potential</td></tr>
    <tr><td><b>Resources</b></td><td>Stretched: overtime, labour and capital shortages</td><td>Spare capacity: idle workers and machines</td></tr>
    <tr><td><b>Unemployment</b></td><td>Below the natural rate</td><td>Above the natural rate (cyclical unemployment)</td></tr>
    <tr><td><b>Inflation</b></td><td>Rising (demand-pull pressure, wages and costs up)</td><td>Falling, possibly deflation</td></tr>
    <tr><td><b>Growth</b></td><td>Above the trend rate, not sustainable</td><td>Below trend, or negative</td></tr>
    <tr><td><b>Keynesian gap name</b></td><td>Inflationary gap</td><td>Deflationary gap</td></tr>
    <tr><td><b>Typical policy</b></td><td>Tighten: higher interest rates, lower spending, higher taxes</td><td>Stimulate: lower rates, more spending, lower taxes</td></tr>
  </table></div>
  <div class="tip"><b class="h">Two ways to say the same thing</b>The <b>output gap</b> is measured in <b>output</b> (real GDP). The <b>inflationary and deflationary gaps</b> from the circular flow (9.1.3) are measured in <b>expenditure</b>: how far aggregate demand is above or below the level that gives full employment. They are linked, but if a question asks for a deflationary gap on a Keynesian cross, measure the vertical gap in spending, not output.</div>

  <h2>3 · What shifts potential output?</h2>
  <ul>
    <li><b>More factors:</b> a larger labour force (migration, higher participation), more capital (investment), more land and resources.</li>
    <li><b>Better factors:</b> education and training, better health, new technology and research.</li>
    <li><b>Better use of factors:</b> competition, flexible labour markets, better infrastructure, lower barriers to enterprise.</li>
  </ul>
  <p>These are the <b>supply-side</b> policies covered in 9.2.4. Anything that damages capacity (war, natural disaster, loss of skills) shifts potential output left.</p>
'''

watch = '''
  <h2>1 · Actual and potential growth on a PPC</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stP"></div>
  <h2>2 · Output gaps on AD and AS</h2>
  <p>The vertical LRAS marks potential output. Watch the gap as demand moves, then see what a rise in potential growth does.</p>
  <div id="stA"></div>
'''

explore = '''
  <h2>Lab 1 · Measure the output gap</h2>
  <p>Set actual and potential GDP (index, $bn). The lab works out the output gap and says what is probably happening to inflation and unemployment.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div>
    <div class="readout"><div><small>Output gap</small><strong id="r1"></strong></div><div><small>Type of gap</small><strong id="r2"></strong></div><div><small>Likely pressure</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 290" role="img" aria-label="Bars of actual and potential GDP with the output gap marked"></svg></div></div></div>

  <h2>Lab 2 · What changed: actual growth, potential growth or both?</h2>
  <p>Pick an event. See which curve it moves and what happens to the gap.</p>
  <div class="card"><div class="row" id="lbBtns"></div><div id="lbOut"></div></div>
'''

practise = '''
  <h2>1 · Actual growth or potential growth?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the effects of a positive output gap in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Japan after 1990: a long negative gap", "After an asset-price bubble burst, Japan's actual output stayed below potential for much of the 1990s and 2000s. Firms and banks held back, demand was weak and prices barely rose, and policy makers kept interest rates near zero for years.", "an example of a persistent negative output gap with low inflation. Say that spare capacity can last a long time if demand does not recover.") +
rw("The post-pandemic rebound and inflation", "In 2021 and 2022 many economies reopened quickly. Spending rose faster than supply chains and workforces could recover, firms struggled to hire, and inflation rose sharply in many countries.", "a positive output gap and demand-pull pressure combined with supply bottlenecks. Evaluate by noting that part of the inflation was cost-push, not only a gap.") +
rw("A new motorway and a skills programme", "A government that builds transport links and trains workers is trying to shift potential output. Over time firms may be able to move goods faster and fill skilled jobs, so the LRAS shifts right.", "potential growth comes from the supply side. Name the policy, link it to a factor of production, and say it takes time.") +
rw("A storm destroys a region's factories", "Capital and housing are lost, so the economy's capacity falls for a time. Actual output drops as well, but the gap may be small because potential has fallen too.", "potential output can fall, not only rise. Separate a loss of capacity from a fall in demand.")
)

exam = exam_page("actual and potential growth and output gaps",
  "We searched the A Level Economics papers in the folder (2020 to 2025). Below are Paper 4 questions on growth, output gaps and inflationary gaps, reworded, and Paper 3 multiple choice questions on the same ideas. Related questions on growth policies are on the 9.2.4 page.",
  [("Essay, 25 marks", "1", "Oct/Nov 2022 (41)"), ("Essay, 20 marks", "1", "Oct/Nov 2023 (43)"), ("Essay part, 12 marks", "1", "May/June 2020 (41, 43)"), ("Data response parts, 3 to 5 marks", "3", "Oct/Nov 2020 (43); May/June 2023 (42); Oct/Nov 2023 (43)"), ("Multiple choice (Paper 3)", "7 shown below", "2020 to 2025")],
  [
  eq("Based on Oct/Nov 2020 · 9708/43 · Q1(a) and (b)", "3 + 4 marks", "(a) What is meant by economic growth? (b) Explain how economic growth is linked to a country's level of economic development.",
     ["<b>(a)</b> A rise in real national output (real GDP) over time, usually a year. Mention that it is measured as a percentage change, and that real means adjusted for inflation.",
      "<b>(b)</b> Growth raises income per head and can fund health, education and infrastructure, which raise living standards. But development is wider: income distribution, life expectancy, schooling and the environment can lag behind growth."],
     "Define, then link to development in two steps. Finish with a brief comment that growth is necessary but not enough."),
  eq("Based on May/June 2023 · 9708/42 · Q1(b)", "4 marks", "A government starts a large programme of ports, roads and railways. Explain, with the help of a diagram, the likely effect on potential growth and on actual growth.",
     ["Actual growth: higher real GDP using existing resources, as construction spending and jobs raise output (1 to 2 marks).",
      "Potential growth: better transport lowers firms' costs and widens the market, so productive capacity rises. The PPC moves outwards, or the LRAS shifts right (1 to 2 marks).",
      "Diagram: a PPC with a move towards the curve and an outward shift of the curve, or AD and AS with LRAS."],
     "Draw the PPC with two labelled curves. State the two types of growth separately."),
  eq("Based on Oct/Nov 2023 · 9708/43 · Q1(b)", "5 marks", "Define actual economic growth. The table shows a country's real GDP growth and its unemployment rate over six years. Analyse the relationship between growth and unemployment.<br><br><b>Year:</b> 1, 2, 3, 4, 5, 6. <b>GDP growth (%):</b> 3.1, 2.4, −1.8, 0.5, 2.9, 3.4. <b>Unemployment (%):</b> 5.2, 5.0, 7.9, 8.1, 7.0, 6.1.",
     ["Definition: the percentage change in real GDP over a period (2 marks).",
      "Inverse relationship: when growth falls or turns negative (year 3), unemployment rises sharply, because firms cut output and jobs.",
      "Use the data: unemployment peaked at 8.1% in year 4 after the fall in year 3, then eased as growth returned. Unemployment lags behind growth.",
      "Credit a note that growth of only 0.5% in year 4 was too weak to cut unemployment."],
     "Definition first. Then one sentence on the general link, two sentences quoting years from the table."),
  eq("Based on May/June 2020 · 9708/41 and 43 · Q6(a)", "12 marks", "Explain what economists mean by an inflationary gap and discuss why it is considered an economic problem. Use a diagram or diagrams to support your answer.",
     ["A clear definition and an accurate, labelled diagram showing the gap (Keynesian cross, or AD and AS with LRAS).",
      "At least three negative effects, with a view on which matters most: rising inflation expectations, higher wage and cost pressure, loss of export competitiveness and a worse current account, redistribution from savers and lenders to borrowers, uncertainty that holds back investment.",
      "Level 4 (9 to 12) needs the effects analysed and their <b>relative importance</b> judged, not just listed."],
     "Define. Draw. Three effects in order of importance with cause and effect. Short judgement."),
  eq("Based on Oct/Nov 2022 · 9708/41 · Q7", "25 marks", "A government's choice to run a larger budget deficit as a share of GDP depends largely on whether the output gap is positive or negative. Explain and evaluate this statement, with the help of a diagram.",
     ["Define the output gap and show a negative gap on AD and AS with LRAS. Expansionary fiscal policy (higher spending or lower taxes) raises AD, so a bigger deficit may close a negative gap, helped by the multiplier.",
      "With a positive gap the opposite applies: a smaller deficit or a surplus reduces AD and eases inflation.",
      "Evaluation: the deficit also depends on <b>other factors</b> (debt level, interest rates and crowding out, bond market confidence, automatic stabilisers, political goals, the size of the multiplier), the output gap is hard to measure, and time lags.",
      "A conclusion that weighs the output gap against these other influences."],
     "Define gap. Diagram with a negative gap and AD shift. Positive gap case. Then at least three evaluation points and a judgement."),
  eq("Based on Oct/Nov 2023 · 9708/43 · Q4", "20 marks", "With the help of a diagram, assess how effective fiscal policy is in closing a negative output gap.",
     ["<b>Knowledge and analysis (14):</b> fiscal policy as changes in government spending and taxes; negative gap as spare capacity caused by weak demand; a budget deficit adds to AD, magnified by the multiplier, raising output and employment. Diagram: AD shifting right towards LRAS.",
      "<b>Evaluation (6):</b> higher borrowing may raise interest rates and crowd out private investment; the size of the gap is hard to forecast; time lags; the multiplier may be small if people save the extra income or spend on imports; the debt burden; if the gap is a supply problem, demand policy will not help."],
     "Define and draw. Spending route, tax route, multiplier. Then evaluate with crowding out, forecasting, leakages and debt. End with a clear judgement.")
  ],
  )

tips = tips_html(
  [("Define growth with 'real'.", "Say the percentage change in real GDP over time, not just 'a rise in output'."),
   ("Keep actual and potential apart.", "Actual growth is a move towards or beyond the PPC. Potential growth is the PPC or LRAS shifting. Say which one the question asks for."),
   ("Name the sign of the gap first.", "Positive means actual above potential; negative means below. Then give the symptoms: inflation and low unemployment, or spare capacity and unemployment."),
   ("Use the formula for gap questions.", "(actual − potential) ÷ potential × 100. Watch the sign."),
   ("Draw LRAS as a vertical line at potential output.", "Label the actual equilibrium to its left or right. A diagram can lift an answer from Level 2."),
   ("Do not mix up gaps.", "An output gap is in output. An inflationary or deflationary gap is in expenditure on a Keynesian cross."),
   ("Evaluate with measurement.", "Potential output cannot be observed, so output gaps are estimates and are often revised.")],
  [("Define the gap", "An output gap is the difference between actual and potential output, shown as a percentage of potential output."),
   ("Negative gap", "A negative output gap means spare capacity, so unemployment is likely to be above its natural rate and inflation may fall."),
   ("Positive gap", "A positive output gap means actual output is above what the economy can sustain, so inflationary pressure is likely to build."),
   ("Potential growth", "Investment in education and capital could shift the LRAS to the right, which raises potential output."),
   ("Evaluate", "However, potential output has to be estimated, so the size of the gap is uncertain.")],
  [CW["define"], CW["explain"], CW["analyse"], CW["assess"], CW["evaluate"]]) + FC

js = '''
/* ---------- Learn picture: PPC and LRAS ---------- */
const PX = (v) => 70 + v * 2.6, PY = (v) => 310 - v * 2.6;
function ppc(k, o = "c1", v = 1) { return SV.path(`M ${PX(0)} ${PY(100 * k)} Q ${PX(100 * k)} ${PY(100 * k)} ${PX(100 * k)} ${PY(0)}`, o, op(v)); }
$("#pic1").innerHTML = `<svg viewBox="0 0 760 360" role="img" aria-label="PPC with a point inside, on the curve and outside showing actual growth, and an outward shifted curve showing potential growth">
  ${axes(70, 310, 340, 40, "Consumer goods", "Capital goods")}
  ${ppc(0.9)}${ppc(1.12, "c3 dash", 1)}
  ${SV.circle(PX(40), PY(40), 6, "dot2")}${tag(PX(40) + 10, PY(40) + 18, "A: inside, negative gap", "t2")}
  ${SV.circle(PX(72), PY(52), 6, "dot1")}${tag(PX(72) + 10, PY(52) - 10, "B: on the PPC", "t1")}
  ${tag(PX(40), PY(40) - 14, "", "t2")}
  ${SV.path(`M ${PX(41)} ${PY(41)} L ${PX(66)} ${PY(50)}`, "c4 dash", {})}${tag(150, 120, "actual growth: A to B", "t4")}
  ${tag(70, 352, "dashed curve: the PPC after potential growth", "t3")}
  ${axes(430, 310, 740, 40, "Real GDP", "Price level")}
  ${SV.line(600, 310, 600, 60, "c3")}${tag(606, 70, "LRAS₁", "t3")}${SV.line(675, 310, 675, 60, "c3 dash")}${tag(681, 70, "LRAS₂", "t3")}
  ${SV.path("M 440 280 Q 560 230 720 90", "c2")}${tag(722, 98, "AS", "t2", 1, "end")}${SV.path("M 440 80 Q 540 190 720 280", "c1")}${tag(722, 288, "AD", "t1", 1, "end")}
  ${SV.line(600, 198, 675, 198, "c4", { "stroke-width": 4 })}${tag(637, 190, "potential growth", "t4", 1, "middle")}
</svg>`;

/* ---------- Watch 1: PPC ---------- */
function ppcDraw(s) {
  const k = s.k;
  let o = axes(70, 310, 420, 40, "Consumer goods", "Capital goods") + SV.path(`M ${PX(0)} ${PY(90)} Q ${PX(90)} ${PY(90)} ${PX(90)} ${PY(0)}`, "c1", op(0.4 + 0.6 * (1 - s.s)));
  if (s.s > 0) o += SV.path(`M ${PX(0)} ${PY(90 * k)} Q ${PX(90 * k)} ${PY(90 * k)} ${PX(90 * k)} ${PY(0)}`, "c3", op(s.s));
  const px = s.x, py = s.y;
  o += SV.circle(PX(px), PY(py), 7, s.m > 0.5 ? "dot1" : "dot2");
  if (s.l > 0) o += tag(PX(px) - 50, PY(py) + 22, "inside the PPC: spare capacity", "t2", s.l);
  if (s.g > 0) o += tag(PX(px) + 12, PY(py) - 12, "on the PPC: full use of resources", "t1", s.g);
  if (s.s > 0) o += tag(300, 62, "PPC shifts out: potential growth", "t3", s.s, "middle");
  if (s.q > 0) o += SV.line(PX(54), PY(54), PX(71), PY(66), "c4", { "stroke-width": 4, ...op(s.q) });
  return o;
}
Lib.stepper($("#stP"), { w: 760, h: 360, label: "A production possibility curve with a point inside it, a move to the curve and then an outward shift of the curve", base: { k: 1, s: 0, x: 40, y: 40, l: 1, g: 0, m: 0, q: 0 }, draw: ppcDraw, tween: 800, dwell: 5400, steps: [
  { cap: "<b>A negative output gap.</b> The economy is at A, <b>inside</b> its PPC. Some workers and machines are idle, so actual output is below potential.", s: {} },
  { cap: "<b>Actual growth.</b> Demand recovers and idle resources are put back to work. The economy moves from A to B on the curve. Output rises, but <b>potential has not changed</b>.", s: { x: 68, y: 60, l: 0, g: 1, m: 1 } },
  { cap: "<b>The limit.</b> At B the economy is using everything it has. More actual growth is impossible without more capacity. Pushing demand further would only raise prices (a positive output gap).", s: { x: 68, y: 60, l: 0, g: 1, m: 1 } },
  { cap: "<b>Potential growth.</b> Investment, education and new technology shift the whole PPC outwards. The economy can now reach combinations that were impossible before.", s: { x: 78, y: 70, l: 0, g: 0, m: 1, s: 1, k: 1.17 } },
] });

/* ---------- Watch 2: AD and AS with output gaps ---------- */
const AX = (q) => 70 + q * 6.6, AY = (p) => 320 - p * 3.0;
function adasDraw(s) {
  const sh = s.sh, lr = s.lr, a = s.a, Q = (a - 15 + 0.7 * sh) / 1.6, P = 15 + 0.7 * (Q - sh);
  let o = axes(70, 320, 740, 30, "Real GDP", "Price level");
  o += SV.line(AX(lr), 320, AX(lr), 40, "c3") + tag(AX(lr) + 6, 52, "LRAS", "t3");
  o += SV.line(AX(0), AY(15 + 0.7 * (0 - sh)), AX(100), AY(15 + 0.7 * (100 - sh)), "c2") + tag(AX(100) - 4, AY(15 + 0.7 * (100 - sh)) - 8, "SRAS", "t2", 1, "end");
  o += SV.line(AX(0), AY(a), AX(100), AY(a - 0.9 * 100), "c1") + tag(AX(100) - 4, AY(a - 90) + 18, "AD", "t1", 1, "end");
  o += SV.line(AX(Q), AY(P), AX(Q), 320, "gr") + SV.line(70, AY(P), AX(Q), AY(P), "gr") + SV.circle(AX(Q), AY(P), 7, "dot4") + tag(AX(Q), 338, "Y", "t4", 1, "middle");
  const g = Q - lr;
  if (s.gp > 0 && Math.abs(g) > 0.8) o += SV.line(AX(Math.min(Q, lr)), 296, AX(Math.max(Q, lr)), 296, g < 0 ? "c2" : "c4", { "stroke-width": 5, ...op(s.gp) }) + tag(AX((Q + lr) / 2), 288, g < 0 ? "negative gap" : "positive gap", g < 0 ? "t2" : "t4", s.gp, "middle");
  if (s.gp > 0 && Math.abs(g) <= 0.8) o += tag(AX(lr) - 8, 288, "no gap", "t3", s.gp, "end");
  return o;
}
Lib.stepper($("#stA"), { w: 760, h: 365, label: "AD and AS with a vertical LRAS showing a negative output gap, no gap and a positive output gap, then LRAS shifting right", base: { a: 100, sh: 0, lr: 60, gp: 0 }, draw: adasDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>Potential output.</b> The vertical <b>LRAS</b> is the most the economy can produce without pushing up costs. Here AD and SRAS cross to its left.", s: { gp: 0 } },
  { cap: "<b>A negative output gap.</b> Equilibrium output is <b>below</b> potential. There is spare capacity, so unemployment is likely to be above the natural rate and inflation low.", s: { gp: 1 } },
  { cap: "<b>Demand rises.</b> AD shifts right until the equilibrium is on the LRAS: the economy is at potential and the <b>gap is closed</b>.", s: { gp: 1, a: 111 } },
  { cap: "<b>A positive output gap.</b> If AD keeps rising, output is pushed <b>above</b> potential. Labour and capital are stretched, costs and prices rise faster: inflationary pressure. This cannot last.", s: { gp: 1, a: 128 } },
  { cap: "<b>Potential growth.</b> Better skills, capital and technology shift the LRAS (and SRAS) to the right. The same AD now gives a smaller gap and less inflation pressure, and the economy can grow faster without overheating.", s: { gp: 1, a: 128, lr: 76, sh: 16 } },
] });

/* ---------- Lab 1: output gap ---------- */
function labGap() {
  if (!$("#ya") || !$("#yp")) return;
  const A = +$("#ya").value, P = +$("#yp").value, g = (A - P) / P * 100, lab = Math.abs(g) < 0.5 ? "None" : g > 0 ? "Positive" : "Negative";
  $("#r1").textContent = Lib.fmtN(g, 1) + "%"; $("#r2").textContent = lab;
  $("#r3").textContent = lab === "None" ? "Balanced" : g > 0 ? "Inflation up" : "Unemployment up";
  $("#rv").textContent = lab === "None" ? "Actual output equals potential output. Resources are fully used and inflation should be stable." : g > 0 ? `Actual output is ${Lib.fmtN(g, 1)}% above potential. Firms are stretched, unemployment is probably below its natural rate and inflation is likely to rise.` : `Actual output is ${Lib.fmtN(-g, 1)}% below potential. There is spare capacity, unemployment is probably above its natural rate and inflation is likely to fall.`;
  const mx = Math.max(A, P, 100) * 1.1, y = (v) => 250 - v / mx * 210;
  let o = SV.line(40, 250, 400, 250) + SV.rect(90, y(A), 90, 250 - y(A), "f1") + SV.rect(240, y(P), 90, 250 - y(P), "f3") + tag(135, y(A) - 6, "Actual " + A, "t1", 1, "middle") + tag(285, y(P) - 6, "Potential " + P, "t3", 1, "middle");
  o += SV.line(180, y(A), 330, y(A), "c4 dash") + SV.line(180, y(P), 330, y(P), "c3 dash") + tag(210, 275, "gap " + Lib.fmtN(g, 1) + "%", g < 0 ? "t2" : "t4", 1, "start");
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "ya", label: "Actual GDP ($bn) ", min: 80, max: 120, step: 1, value: 96, fmt: (v) => v, onInput: labGap });
Lib.slider($("#g2"), { id: "yp", label: "Potential GDP ($bn) ", min: 80, max: 120, step: 1, value: 100, fmt: (v) => v, onInput: labGap });
labGap();
btnTable("lbBtns", "lbOut", [
  ["Government funds a university skills programme", "Potential growth (LRAS shifts right) over time", "Little change now; raises capacity later", "Gap may widen if AD does not keep up", "Supply-side"],
  ["Consumer confidence jumps and spending surges", "Actual growth (AD shifts right)", "Output moves towards or above potential", "Gap becomes less negative or turns positive", "Demand-side"],
  ["An earthquake destroys factories and roads", "Potential falls (LRAS shifts left)", "Actual output falls too", "Gap could be small, with falling living standards", "Supply shock"],
  ["Interest rates rise sharply", "Fall in actual output (AD shifts left)", "Potential unchanged in the short run", "Gap becomes more negative", "Demand-side"],
  ["New oil field and cheaper energy", "Potential growth (LRAS and SRAS shift right)", "Actual output rises and prices fall", "Gap unchanged or smaller; less inflation pressure", "Supply-side"],
  ["Export orders collapse in a global recession", "Actual output falls (AD shifts left)", "Potential unchanged", "Negative gap opens", "Demand-side"]
], ["Event", "What moves", "Immediate effect", "Effect on the gap", "Type"]);

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Does the event mainly raise actual growth or potential growth?", ["Actual growth", "Potential growth"],
  [("Firms use idle machines after demand picks up", 0), ("Government cuts income tax and spending rises", 0), ("A new apprenticeship scheme raises skills", 1), ("Investment in broadband infrastructure", 1), ("Unemployed workers return to jobs in a recovery", 0), ("A breakthrough in battery technology", 1), ("A boom in exports raises output from existing factories", 0), ("Net migration raises the size of the workforce", 1)],
  "Actual growth uses spare capacity. Potential growth adds capacity.") + MATCH([
  ["Actual growth", "The percentage rise in real GDP over a period"],
  ["Potential growth", "A rise in the productive capacity of the economy"],
  ["Positive output gap", "Actual output is above potential output"],
  ["Negative output gap", "Actual output is below potential output: spare capacity"],
  ["LRAS", "The vertical curve showing potential output"],
  ["Inflationary gap", "Expenditure above the level that gives full employment on a Keynesian cross"]]) + ORDER(
  "Put the effects of a rising positive output gap in order.",
  ["Aggregate demand rises above what the economy can supply", "Firms compete for scarce workers and materials", "Wages and input costs rise", "Firms raise prices and inflation increases", "The central bank raises interest rates to cool demand"],
  "A positive gap tends to lead to inflation, then tighter policy.") + CALC([
  {"q": "Actual GDP is $1,040bn and potential GDP is $1,000bn. Calculate the output gap as a percentage of potential GDP.", "a": 4, "unit": "%", "tol": 0.05, "hint": "(actual − potential) ÷ potential × 100.", "sol": "(1040 − 1000) ÷ 1000 × 100 = <b>4%</b>, a positive gap."},
  {"q": "Real GDP rises from $2,500bn to $2,575bn. Calculate the rate of actual economic growth.", "a": 3, "unit": "%", "tol": 0.05, "hint": "Change ÷ original × 100.", "sol": "75 ÷ 2500 × 100 = <b>3%</b>."},
  {"q": "Potential GDP is $800bn and actual GDP is $760bn. Calculate the output gap as a percentage of potential GDP. Use a minus sign for a negative gap.", "a": -5, "unit": "%", "tol": 0.05, "hint": "Actual is below potential, so the answer is negative.", "sol": "(760 − 800) ÷ 800 × 100 = <b>−5%</b>, a negative gap."},
  {"q": "A closed economy has equilibrium income of $900m. Full employment income is $1,000m and the marginal propensity to consume is 0.75. What size of rise in spending (in $m) would close the gap?", "a": 25, "unit": "$m", "tol": 0.05, "hint": "Multiplier = 1 ÷ (1 − MPC). Gap in income ÷ multiplier.", "sol": "Multiplier = 1 ÷ 0.25 = 4. Income gap = 100, so spending must rise by 100 ÷ 4 = <b>$25m</b>."}]) + MCQ([
  ("An economy moves from inside its PPC towards the curve. What has occurred?", ["Potential growth", "Actual growth", "A fall in the output gap to zero from a positive gap", "A fall in productive capacity"], 1, "A move towards the curve uses spare capacity: actual growth. Potential growth would shift the curve."),
  ("Which would most likely raise potential output?", ["A cut in interest rates", "A rise in government spending", "An increase in the number of skilled workers", "A fall in the exchange rate"], 2, "More and better factors of production shift the LRAS. The others mainly move AD."),
  ("An economy has a negative output gap. Which is most likely?", ["Unemployment above its natural rate", "Rising inflation", "Output above capacity", "A shortage of skilled labour"], 0, "Spare capacity means unemployment above the natural rate and weak inflation pressure."),
  ("Actual growth is 4% a year and potential growth is 2.5% a year. What is likely to happen to the output gap?", ["It will move towards negative", "It will become more positive", "It will stay the same", "It will disappear"], 1, "Output is growing faster than capacity, so the gap becomes more positive (or less negative)."),
  ("Which statement about the output gap is correct?", ["It is observed directly in national accounts", "It is an estimate because potential output cannot be measured exactly", "It always equals the inflation rate", "It is the same as the budget deficit"], 1, "Potential output has to be estimated, so the output gap is an estimate that is often revised.")
], "qz1") + CARDS([
  ("Actual growth", "Percentage change in real GDP over a period."),
  ("Potential growth", "Rise in the economy's productive capacity (LRAS or PPC shifts out)."),
  ("Output gap", "Actual output minus potential output, as a % of potential."),
  ("Positive output gap", "Actual above potential: inflation pressure, unemployment below natural rate."),
  ("Negative output gap", "Actual below potential: spare capacity, cyclical unemployment."),
  ("Inflationary gap", "Expenditure above full-employment output on a Keynesian cross."),
  ("Deflationary gap", "Expenditure short of full-employment output on a Keynesian cross."),
  ("Trend growth", "The average rate of growth of potential output over time.")]) + MCQ([
  ("What movement on a production possibility diagram shows actual economic growth? (Feb/March 2025 · 32 · Q16, reworded)", ["A positive output gap", "A move from a point inside the curve towards the curve", "A recession", "An outward shift of the curve"], 1, "Actual growth uses existing capacity; an outward shift of the curve is potential growth."),
  ("What does an output gap show? (Oct/Nov 2021 · 33 · Q18, reworded)", ["The gap between actual output and long-run potential output", "The gap between maximum output in a boom and minimum output in a recession", "The gap between exports and imports", "The gap between actual output and output at full employment of labour only"], 0, "Output gap is actual output minus long-run potential output."),
  ("What is most likely in an economy with a positive output gap? (May/June 2022 · 31 · Q24, reworded)", ["Potential GDP above actual GDP", "High unemployment", "Inflation", "Low labour costs"], 2, "Output above potential stretches resources, so inflation tends to rise."),
  ("An economy has a positive output gap. What is happening to growth and the price level? (May/June 2025 · 31 · Q17, reworded)", ["Growth below trend, prices falling", "Growth above trend, prices rising", "Growth below trend, prices rising", "Growth above trend, prices falling"], 1, "Above-trend growth pushes output over potential and puts upward pressure on prices."),
  ("An economy has a negative output gap. What is most likely to happen to inflation and unemployment? (Oct/Nov 2022 · 32 · Q24, reworded)", ["Inflation falls, unemployment falls", "Inflation falls, unemployment rises", "Inflation rises, unemployment falls", "Inflation rises, unemployment rises"], 1, "Spare capacity means weak price pressure and unemployment above its natural rate."),
  ("A closed economy with no government has equilibrium income of $1,000bn. Households spend 80% of any income. Full employment income is $1,200bn. By how much must aggregate demand rise initially to close the deflationary gap? (Oct/Nov 2021 · 33 · Q26, reworded)", ["−$200bn", "−$40bn", "+$40bn", "+$200bn"], 2, "Multiplier = 1 ÷ 0.2 = 5. Income gap $200bn ÷ 5 = $40bn of extra spending."),
  ("What may prevent a government achieving a faster rate of growth of real GDP? (Feb/March 2020 · 32 · Q30, reworded)", ["Consumption and investment are sensitive to interest rates", "Inflation is below the central bank target", "The economy is already operating on its long-run aggregate supply curve", "There is a large negative output gap"], 2, "If the economy is already at potential output on LRAS, more demand only raises prices; faster growth needs a shift in LRAS.")
])

build("sy921", "actual-potential-growth-output-gaps", "Actual and Potential Growth, and Output Gaps", EY,
  "9.2.1 and 9.2.2: what actual and potential growth are, how output gaps are measured, and what a positive or negative gap means for inflation and unemployment. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
