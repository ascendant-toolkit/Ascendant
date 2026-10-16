"""Builds the three ch41 part pages (cf1..cf3), written from scratch. Run: python3 tools/artifact-kit/mk_ch41.py"""
from splitter import *
EY = "A Level Economics · 9708 · Syllabus 9.1 · Part {} of 3"
HEAD = '''const op = (v) => ({ opacity: Math.max(0, Math.min(1, v)) });
const halo = { style: "paint-order:stroke;stroke:var(--surface);stroke-width:5px" };
const arrow = (x1, y1, x2, y2, dir, cls, v) => `<g style="opacity:${Math.max(0, Math.min(1, v))}">${SV.line(x1, y1, x2, y2, cls, { "stroke-width": 2.5 })}${SV.arrowHead(x2, y2, dir, cls === "c2" ? "dot2" : cls === "c3" ? "dot3" : cls === "c4" ? "dot4" : "dot1")}</g>`;
'''
RW = '<p class="note">Examples are explained in general terms. Check current details before quoting them in an exam answer.</p>\n'
def mc(q, opts, a, why): return "  { q: " + repr(q).replace("\\'", "'") + ", opts: " + repr(opts) + ", a: " + str(a) + ", why: " + repr(why) + " },\n"
def js_s(x):  # python repr gives single-quoted strings, valid JS
    return x
MCQTEXT = lambda items: 'Lib.quiz($("#qz2"), { qs: [\n' + "".join(mc(*i) for i in items) + '] });\n'

# ------------------------------------------------------------------ 41.1
learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>The <b>circular flow of income</b> shows money moving between households and firms: households receive income from firms for the factors they supply and spend it on goods and services. Not all income is re-spent: <b>withdrawals (leakages)</b> are <b>saving (S)</b>, <b>taxes (T)</b> and <b>imports (M)</b>, while <b>injections</b> are <b>investment (I)</b>, <b>government spending (G)</b> and <b>exports (X)</b>. National income is in <b>equilibrium</b> when injections equal withdrawals (J = W). If J is greater than W, spending is above income and national income, output and employment rise; if W is greater than J, they fall.</p></div>

  <h2>1 · From two sectors to four</h2>
  <ul>
    <li><b>Two sectors (households and firms):</b> households supply factors and receive income (Y); they spend it on output (C); firms pay out all they receive.</li>
    <li><b>Financial sector:</b> households may save (S, a withdrawal); firms borrow to invest (I, an injection).</li>
    <li><b>Government:</b> collects taxes (T, a withdrawal) and spends on goods, services and transfers (G, an injection).</li>
    <li><b>Foreign sector:</b> residents buy imports (M, a withdrawal) and foreigners buy exports (X, an injection).</li>
  </ul>
  <div class="formula">Injections J = I + G + X &nbsp;·&nbsp; Withdrawals W = S + T + M &nbsp;·&nbsp; Equilibrium when J = W</div>

  <h2>2 · Injections and withdrawals</h2>
  <div class="tw"><table class="t">
    <tr><th>Sector</th><th>Withdrawal (leaves the flow)</th><th>Injection (enters the flow)</th><th>Net injection when</th></tr>
    <tr><td><b>Private (financial)</b></td><td>Saving, S</td><td>Investment, I</td><td>I &gt; S</td></tr>
    <tr><td><b>Government</b></td><td>Taxes, T</td><td>Government spending, G</td><td>G &gt; T (a budget deficit)</td></tr>
    <tr><td><b>Foreign</b></td><td>Imports, M</td><td>Exports, X</td><td>X &gt; M (a trade surplus)</td></tr>
  </table></div>
  <p>Transfer payments (benefits) are not an injection of their own: they are negative taxes, so they reduce T. Spending by foreign tourists is an export; spending by residents abroad is an import.</p>

  <h2>3 · What happens when J and W are not equal</h2>
  <div class="grid2">
    <div class="card"><h3>Injections greater than withdrawals</h3><p>More is being spent than earned. Firms sell more, so they produce more and hire more workers. National income, output and employment rise, and withdrawals rise with income (for example, people save and pay more tax) until they match the injections again.</p></div>
    <div class="card"><h3>Withdrawals greater than injections</h3><p>Spending falls short of income. Firms find stocks building up, cut output and jobs, and national income falls until withdrawals have fallen to equal injections.</p></div>
  </div>
  <div class="tip"><b class="h">Using the model in an exam</b>Draw the diagram (or the injections and withdrawals graph), label every injection and withdrawal, identify the starting equilibrium and, if asked about employment, the full employment level of income. Then say which flow the event changes, the direction of the gap between J and W, and how far income moves (the multiplier, part 2). Finish with evaluation: spare capacity, time lags and how the other flows respond.</div>
'''
watch = '''
  <h2>1 · The circular flow diagram</h2>
  <p>Press Play, or click the steps. Withdrawals leave the flow downwards; injections enter it from below.</p><div id="stF"></div>
  <h2>2 · The injections and withdrawals graph</h2>
  <p>Withdrawals rise with income (W = 0.5Y here). Injections are fixed at $200m.</p><div id="stG"></div>
'''
explore = '''
  <h2>Lab 1 · Where is equilibrium?</h2>
  <p>Withdrawals are a fixed share of income (W = wY) and injections are fixed at J. Equilibrium income is where they meet: Y = J ÷ w.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div>
    <div class="readout"><div><small>Equilibrium income</small><strong id="e1"></strong></div><div><small>Withdrawals there</small><strong id="e2"></strong></div><div><small>Value of 1 ÷ w</small><strong id="e3"></strong></div></div>
    <div class="verdict" id="ev"></div></div>
    <div><svg id="labJ" viewBox="0 0 420 300" role="img" aria-label="Injections and withdrawals graph with equilibrium national income"></svg></div></div></div>

  <h2>Lab 2 · Net injection or net withdrawal?</h2>
  <p>Set each flow. The three sector pairs show whether the private, government and foreign sectors are adding to or taking from the circular flow.</p>
  <div class="card"><div class="grid2"><div><div id="g3"></div><div id="g4"></div><div id="g5"></div><div id="g6"></div><div id="g7"></div><div id="g8"></div>
    <div class="readout"><div><small>Injections J</small><strong id="n1"></strong></div><div><small>Withdrawals W</small><strong id="n2"></strong></div><div><small>Net (J − W)</small><strong id="n3"></strong></div><div><small>National income</small><strong id="n4"></strong></div></div>
    <div class="verdict" id="nv"></div></div>
    <div><svg id="labK" viewBox="0 0 420 300" role="img" aria-label="Stacked bars of injections and withdrawals by sector"></svg></div></div></div>
'''
practise = '''
  <h2>1 · Injection, withdrawal or neither?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the adjustment to a rise in injections in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''
real = RW + '''  <div class="rw"><h3>A government infrastructure programme</h3><p>When a government spends on roads and railways without raising taxes by the same amount, G is greater than T: a net injection. Construction firms hire workers, who spend their wages, and national income may rise.</p><div class="use"><b>Exam use:</b> a rise in G as an injection. Say whether there is spare capacity and how far income might rise.</div></div>
  <div class="rw"><h3>A tourism boom</h3><p>Foreign visitors spending in hotels, restaurants and shops are buying a country's exports. A rise in tourist numbers increases X, an injection, and incomes in the local economy rise.</p><div class="use"><b>Exam use:</b> services exports as an injection (a Paper 3 question noted that tourists visiting another country are not an injection for their own country).</div></div>
  <div class="rw"><h3>A rise in household saving</h3><p>If households become worried about the future and save more, saving (a withdrawal) rises. Unless investment rises as well, withdrawals exceed injections and national income falls.</p><div class="use"><b>Exam use:</b> why a rise in saving can reduce national income in the short run.</div></div>
  <div class="rw"><h3>A fall in interest rates</h3><p>Lower interest rates reduce the reward for saving, so saving may fall, and make borrowing cheaper, so consumption and investment may rise. Withdrawals fall and injections rise.</p><div class="use"><b>Exam use:</b> a Paper 4 question asked for the impact of a fall in interest rates on output and employment using a circular flow diagram.</div></div>
'''
exam = '''
  <h2>Past paper questions on the circular flow of income</h2>
  <p>We searched the A Level Economics papers in the folder (2020 to 2025). Below are the Paper 4 questions that asked for a circular flow or injections and withdrawals diagram, a model answer for one of them, and seven Paper 3 multiple choice questions. Mark scheme points are summarised in our own words, not copied.</p>
  <div class="tw"><table class="t">
    <tr><th>Type</th><th>Examples found</th><th>Where</th></tr>
    <tr><td>Essay, 25 marks</td><td>1</td><td>May/June 2022 (41, 43)</td></tr>
    <tr><td>Essay, 20 marks</td><td>1</td><td>May/June 2025 (42)</td></tr>
    <tr><td>Essay parts, 12 marks</td><td>2</td><td>Feb/March 2022 (42); Oct/Nov 2022 (43)</td></tr>
    <tr><td>Multiple choice (Paper 3)</td><td>7 shown below</td><td>2020 to 2022</td></tr>
  </table></div>
  <h2>A · Essay questions</h2>
  <div class="key"><span class="k"><i></i>Knowledge (K)</span><span class="a"><i></i>Application (A)</span><span class="n"><i></i>Analysis (N)</span><span class="e"><i></i>Evaluation (E)</span></div>

  <details class="eq"><summary>Feb/March 2022 · 9708/42 · Q7(a) <span class="mark">12 marks</span> Consider, with the help of a circular flow diagram, the potential impact of a fall in the rate of interest on the level of output and the level of employment.</summary><div class="body">
    <div class="tip"><b class="h">What the mark scheme wants</b>
      <ul><li>An accurate, labelled <b>three sector circular flow diagram</b> with injections and withdrawals identified, the existing equilibrium and the <b>full employment level</b> of income, with the links between expenditure, output and employment explained.</li><li>Analysis of the effect of a fall in interest rates on at least one <b>withdrawal</b> (saving may fall, imports may rise) and one <b>injection</b> (investment, perhaps exports), each with an evaluative comment.</li><li>Evaluation: the effect also depends on the <b>multiplier</b> (a fall in the marginal propensity to save raises it), on how interest-elastic investment is, on business confidence, and on how much spare capacity exists. A conclusion is needed for the top level.</li></ul></div>
    <div class="key"><span class="k"><i></i>K</span><span class="a"><i></i>A</span><span class="n"><i></i>N</span><span class="e"><i></i>E</span></div>
    <div class="ans">
    <p><span class="mk k" data-t="K">In a three sector circular flow, households and firms exchange factor payments and spending, with saving (S), taxes (T) as withdrawals and investment (I) and government spending (G) as injections. National income is in equilibrium where J = W, and output and employment are linked to the level of spending.</span></p>
    <p><span class="mk n" data-t="N">A fall in the rate of interest could reduce the reward for saving, so saving might fall and consumer spending rise, which reduces a withdrawal. It also makes borrowing cheaper, so firms may invest more, which raises an injection. With J greater than W, spending is above income, firms produce more and employ more workers, and national income rises towards the full employment level.</span> <span class="mk e" data-t="E">The size of the effect may depend on how responsive investment is to the interest rate, and on business confidence: if firms are pessimistic, investment may rise only slightly.</span></p>
    <p><span class="mk n" data-t="N">The rise in income is likely to be magnified by the multiplier, because the extra spending becomes income for others, and a fall in the marginal propensity to save raises the multiplier.</span> <span class="mk e" data-t="E">However, if the economy is already close to full employment, extra spending may raise prices more than output, and there may be time lags before lower rates affect spending. Overall, a fall in interest rates is likely to raise output and employment when there is spare capacity, but the size of the effect is uncertain.</span></p></div>
  </div></details>

  <details class="eq"><summary>May/June 2022 · 9708/41 and 43 · Q5 <span class="mark">25 marks</span> With the help of a circular flow diagram discuss how a policy of export-led growth might affect the standard of living in a developing economy.</summary><div class="body">
    <div class="tip"><b class="h">What the mark scheme wants</b>
      <ul><li>Export-led growth as an outward-looking strategy that relies on <b>openness and international trade</b>. A labelled circular flow diagram showing all withdrawals and injections and the rise in exports (an injection) producing a bigger rise in income, output and employment through the <b>multiplier</b>, and a higher GDP per capita.</li><li>Evaluation: developing economies often export <b>primary goods</b> with income-inelastic demand and volatile supply (weather), so growth may be limited; higher income does not guarantee a better standard of living (distribution, leisure, long-term growth).</li></ul></div>
  </div></details>

  <details class="eq"><summary>Oct/Nov 2022 · 9708/43 · Q5(a) <span class="mark">12 marks</span> Consider, with the help of a circular flow diagram, why an export-led growth policy is likely to be successful when a developed economy is in a recession.</summary><div class="body">
    <div class="tip"><b class="h">What the mark scheme wants</b>
      <ul><li>A circular flow diagram with the recession shown as an equilibrium below full employment, and a rise in <b>exports</b> as an injection raising income through the multiplier.</li><li>Evaluation: success depends on spare capacity, <b>demand abroad</b> (are trading partners also in recession?), the exchange rate and price competitiveness, and the size of the multiplier (high marginal propensity to import reduces it).</li></ul></div>
  </div></details>

  <details class="eq"><summary>May/June 2025 · 9708/42 · Q4 <span class="mark">20 marks</span> With the help of an injections and withdrawals graph, assess the impact of a decrease in interest rates on the level of employment in an economy.</summary><div class="body">
    <div class="tip"><b class="h">What the mark scheme wants</b>
      <ul><li>An injections and withdrawals graph: W rising with income, J, equilibrium income and the full employment level. A fall in interest rates may shift <b>J up</b> (investment, exports through a lower exchange rate) and <b>W down</b> (saving falls), raising income and employment.</li><li>Assessment: how interest-elastic investment is, confidence, time lags, spare capacity, the multiplier, and whether the fall in rates leads to inflation instead of jobs.</li></ul></div>
    <div class="tip"><b class="h">Diagram to draw</b>W curve rising, J curve horizontal. Mark Y1 where they cross. Shift J up to J1 (and perhaps W down), mark Y2, and label Yf (full employment) to the right.</div>
  </div></details>

  <h2>B · Multiple choice questions (Paper 3)</h2>
  <p>Choose an answer, then read the reason. Source: paper code and question number.</p>
  <div id="qz2"></div>
'''
tips = '''
  <h2>Top tips</h2>
  <ul class="tips">
    <li><b>Know the lists:</b> injections are I, G and X; withdrawals are S, T and M. Equilibrium is J = W.</li>
    <li><b>Say "net".</b> A net injection means I &gt; S, G &gt; T or X &gt; M overall, not that every injection is bigger than every withdrawal.</li>
    <li><b>Label the diagram fully:</b> every withdrawal and injection, the equilibrium, the full employment level and the direction of change.</li>
    <li><b>Link spending to jobs:</b> higher spending raises demand for output, firms produce more and employ more workers.</li>
    <li><b>Mention the multiplier</b> when income changes. The total change in income is bigger than the initial change in injections.</li>
    <li><b>Evaluate with spare capacity.</b> If the economy is near full employment, extra spending may raise prices rather than output.</li>
    <li><b>Do not count transfer payments or spending by residents abroad as injections.</b></li>
  </ul>
  <h2>Sentences you can use</h2>
  <div class="tw"><table class="t">
    <tr><th>You want to say</th><th>Use this sentence</th></tr>
    <tr><td>Equilibrium</td><td>"National income is in equilibrium where injections equal withdrawals."</td></tr>
    <tr><td>Net injection</td><td>"Injections exceed withdrawals, so spending is above income and national income, output and employment are likely to rise."</td></tr>
    <tr><td>Interest rates</td><td>"A fall in interest rates may reduce saving, a withdrawal, and increase investment, an injection."</td></tr>
    <tr><td>Evaluate</td><td>"However, the effect depends on spare capacity, because near full employment extra spending may mainly raise prices."</td></tr>
  </table></div>
  <h2>Command words</h2>
  <div class="tw"><table class="t">
    <tr><th>Command word</th><th>What it asks for</th></tr>
    <tr><td>Consider</td><td>Look at the issue from several sides and judge how strong each is.</td></tr>
    <tr><td>Discuss</td><td>Arguments on both sides, then a judgement.</td></tr>
    <tr><td>Assess</td><td>Judge how important or effective something is, with reasons.</td></tr>
  </table></div>
  <h2>Flashcards</h2><div id="fc1"></div>
'''
js = HEAD + '''
/* ---------- Watch 1: circular flow diagram ---------- */
function flowDraw(s) {
  const box = (x, y, w, h, t, c, v) => SV.rect(x, y, w, h, c, { opacity: 0.9 * v, rx: 10 }) + SV.text(x + w / 2, y + h / 2 + 5, t, "lbl bd", { "text-anchor": "middle", ...halo, ...op(v) });
  let o = box(60, 130, 150, 70, "Households", "f1", 1) + box(600, 130, 150, 70, "Firms", "f4", 1);
  o += arrow(600, 150, 210, 150, "l", "c1", 1) + SV.text(405, 140, "income Y (wages, rent, interest, profit)", "sm bd", { "text-anchor": "middle", ...halo });
  o += arrow(210, 185, 600, 185, "r", "c1", 1) + SV.text(405, 173, "consumption spending C", "sm bd", { "text-anchor": "middle", ...halo });
  const sec = [["Financial sector", "S", "I", 270, s.f], ["Government", "T", "G", 420, s.g], ["Foreign sector", "M", "X", 570, s.x]];
  sec.forEach(([n, w, j, cx, v]) => {
    if (v <= 0) return;
    o += box(cx - 55, 290, 110, 50, n, "f3", v) + arrow(cx - 20, 190, cx - 20, 290, "d", "c2", v) + SV.text(cx - 32, 245, w, "lbl bd t2", { "text-anchor": "end", ...halo, ...op(v) }) + arrow(cx + 20, 290, cx + 20, 190, "u", "c3", v) + SV.text(cx + 32, 245, j, "lbl bd t3", { ...halo, ...op(v) });
  });
  if (s.t > 0) o += SV.text(405, 372, "Withdrawals S + T + M (red)   ·   Injections I + G + X (green)", "lbl bd", { "text-anchor": "middle", ...halo, ...op(s.t) });
  if (s.u > 0) o += SV.text(405, 110, "J > W: spending exceeds income, so income, output and jobs rise", "lbl bd t3", { "text-anchor": "middle", ...halo, ...op(s.u) });
  if (s.e > 0) o += SV.text(405, 110, "J = W: national income is in equilibrium", "lbl bd t1", { "text-anchor": "middle", ...halo, ...op(s.e) });
  return o;
}
Lib.stepper($("#stF"), { w: 780, h: 385, label: "Circular flow of income with saving, taxes and imports leaving and investment, government spending and exports entering", base: { f: 0, g: 0, x: 0, t: 0, u: 0, e: 0 }, draw: flowDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>Two sectors.</b> Firms pay <b>income (Y)</b> to households for the factors they supply. Households spend it on firms' output as <b>consumption (C)</b>. If everything is spent, the flow is the same size every round.", s: {} },
  { cap: "<b>The financial sector.</b> Households may <b>save (S)</b>: a <b>withdrawal</b> that leaves the flow. Firms may borrow savings to <b>invest (I)</b>: an <b>injection</b> that adds to spending.", s: { f: 1 } },
  { cap: "<b>The government.</b> Households and firms pay <b>taxes (T)</b>, a withdrawal. The government spends on goods, services and benefits (<b>G</b>), an injection.", s: { f: 1, g: 1 } },
  { cap: "<b>The foreign sector.</b> Residents buy <b>imports (M)</b>, a withdrawal. Foreigners buy the country's <b>exports (X)</b>, an injection.", s: { f: 1, g: 1, x: 1, t: 1 } },
  { cap: "<b>Equilibrium.</b> When total injections equal total withdrawals (I + G + X = S + T + M), the flow neither grows nor shrinks and national income is stable.", s: { f: 1, g: 1, x: 1, t: 1, e: 1 } },
  { cap: "<b>A rise in injections.</b> If exports (or investment, or government spending) rise so that J exceeds W, spending is above income. Firms produce more and hire more, and national income rises until withdrawals have grown to match.", s: { f: 1, g: 1, x: 1, t: 1, u: 1 } },
] });

/* ---------- Watch 2: injections and withdrawals graph ---------- */
const GX = (y) => 70 + y * 0.85, GY = (v) => 330 - v * 0.75;
function jwDraw(s) {
  let o = SV.line(70, 330, 760, 330) + SV.line(70, 330, 70, 30) + SV.text(760, 370, "National income Y ($m)", "sm", { "text-anchor": "end" }) + SV.text(76, 24, "Injections and withdrawals ($m)", "sm");
  [0, 200, 400, 600, 800].forEach((y) => { o += SV.text(GX(y), 346, y, "sm", { "text-anchor": "middle" }); });
  if (s.w > 0) o += SV.line(GX(0), GY(0), GX(800), GY(400), "c2", op(s.w)) + SV.text(GX(800) - 4, GY(400) - 8, "W = 0.5Y", "lbl bd t2", { "text-anchor": "end", ...op(s.w) });
  if (s.j > 0) o += SV.line(GX(0), GY(200), GX(800), GY(200), "c3", op(s.j)) + SV.text(GX(800) - 4, GY(200) - 8, "J = $200m", "lbl bd t3", { "text-anchor": "end", ...op(s.j) });
  if (s.e > 0) o += SV.line(GX(400), GY(200), GX(400), 330, "gr", op(s.e)) + SV.circle(GX(400), GY(200), 7, "dot1", op(s.e)) + SV.text(GX(400), 372, "Y = 400", "lbl bd", { "text-anchor": "middle", ...op(s.e) });
  if (s.lo > 0) o += SV.line(GX(200), GY(200), GX(300), GY(200), "c4", { "stroke-width": 4, ...op(s.lo) }) + SV.text(GX(250), GY(200) - 40, "J > W: income rises", "lbl bd t3", { "text-anchor": "middle", ...halo, ...op(s.lo) }) + SV.circle(GX(200), GY(100), 5, "dot2", op(s.lo)) + SV.text(GX(200) - 8, GY(100) + 20, "W = 100", "sm bd t2", { "text-anchor": "end", ...halo, ...op(s.lo) });
  if (s.hi > 0) o += SV.circle(GX(600), GY(300), 5, "dot2", op(s.hi)) + SV.text(GX(600) + 8, GY(300) - 10, "W = 300 > J: income falls", "lbl bd t2", { ...halo, ...op(s.hi) });
  if (s.n > 0) o += SV.line(GX(0), GY(280), GX(800), GY(280), "c4", { "stroke-dasharray": "6 5", ...op(s.n) }) + SV.text(GX(790), GY(280) - 8, "J1 = $280m", "lbl bd t4", { "text-anchor": "end", ...halo, ...op(s.n) }) + SV.circle(GX(560), GY(280), 7, "dot4", op(s.n)) + SV.line(GX(560), GY(280), GX(560), 330, "gr", op(s.n)) + SV.text(GX(560), 372, "Y1 = 560", "lbl bd t4", { "text-anchor": "middle", ...op(s.n) });
  return o;
}
Lib.stepper($("#stG"), { w: 780, h: 385, label: "Withdrawals rising with income, fixed injections, equilibrium national income and a rise in injections", base: { w: 0, j: 0, e: 0, lo: 0, hi: 0, n: 0 }, draw: jwDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>Withdrawals.</b> Saving, taxes and imports all rise with income, so the withdrawals curve slopes up. Here <b>W = 0.5Y</b>: half of any extra income leaks out.", s: { w: 1 } },
  { cap: "<b>Injections.</b> Investment, government spending and exports do not depend on current income in this simple model, so <b>J is a horizontal line</b> at $200m.", s: { w: 1, j: 1 } },
  { cap: "<b>Equilibrium.</b> J = W where 200 = 0.5Y, so equilibrium national income is <b>Y = $400m</b>.", s: { w: 1, j: 1, e: 1 } },
  { cap: "<b>Below equilibrium</b> (Y = 200) withdrawals are only $100m, so J is greater than W: spending exceeds income, firms expand output and income rises towards 400.", s: { w: 1, j: 1, e: 1, lo: 1 } },
  { cap: "<b>Above equilibrium</b> (Y = 600) withdrawals are $300m, more than J: spending falls short, firms cut output and income falls back towards 400.", s: { w: 1, j: 1, e: 1, hi: 1 } },
  { cap: "<b>A rise in injections</b> to $280m shifts J up. The new equilibrium is where 280 = 0.5Y: <b>Y1 = $560m</b>. Injections rose by $80m but income rose by $160m, the multiplier effect (part 2).", s: { w: 1, j: 1, e: 0.4, n: 1 } },
] });

/* ---------- Lab 1: equilibrium ---------- */
function labEq() {
  if (!$("#jj") || !$("#ww")) return;
  const J = +$("#jj").value, w = +$("#ww").value, Y = J / w, F = { x: (v) => 40 + v * 0.34, y: (v) => 270 - v * 0.26 };
  $("#e1").textContent = "$" + Lib.fmtN(Y, 0) + "m"; $("#e2").textContent = "$" + Lib.fmtN(J, 0) + "m"; $("#e3").textContent = Lib.fmtN(1 / w, 2);
  $("#ev").textContent = `Withdrawals are ${Math.round(w * 100)}% of income, so they equal injections of $${J}m when Y = ${J} ÷ ${w} = $${Lib.fmtN(Y, 0)}m. A smaller share of income leaking out (a lower w) means a higher equilibrium income for the same injections.`;
  let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(396, 292, "National income Y ($m)", "sm", { "text-anchor": "end" }) + SV.text(46, 24, "J, W ($m)", "sm");
  o += SV.line(F.x(0), F.y(0), F.x(1000), F.y(w * 1000), "c2") + SV.line(F.x(0), F.y(J), F.x(1000), F.y(J), "c3") + SV.line(F.x(Y), F.y(J), F.x(Y), 270, "gr") + SV.circle(F.x(Y), F.y(J), 6, "dot1") + SV.text(F.x(Y), 288, Lib.fmtN(Y, 0), "sm bd", { "text-anchor": "middle" }) + SV.text(396, F.y(w * 1000) + 16, "W", "sm bd t2", { "text-anchor": "end" }) + SV.text(396, F.y(J) - 6, "J", "sm bd t3", { "text-anchor": "end" });
  $("#labJ").innerHTML = o;
}
Lib.slider($("#g1"), { id: "jj", label: "Injections J ($m): ", min: 100, max: 300, step: 20, value: 200, fmt: (v) => v, onInput: labEq });
Lib.slider($("#g2"), { id: "ww", label: "Withdrawal rate w (share of income): ", min: 0.3, max: 0.8, step: 0.05, value: 0.5, fmt: (v) => Lib.fmtN(v, 2), onInput: labEq });

/* ---------- Lab 2: net injection ---------- */
function labNet() {
  if (!$("#fi") || !$("#fs") || !$("#fg") || !$("#ft") || !$("#fx") || !$("#fm")) return;
  const I = +$("#fi").value, S = +$("#fs").value, G = +$("#fg").value, T = +$("#ft").value, X = +$("#fx").value, M = +$("#fm").value, J = I + G + X, W = S + T + M, net = J - W;
  $("#n1").textContent = "$" + J + "m"; $("#n2").textContent = "$" + W + "m"; $("#n3").textContent = (net > 0 ? "+" : net < 0 ? "−" : "") + "$" + Math.abs(net) + "m"; $("#n4").textContent = net > 0 ? "Rises" : net < 0 ? "Falls" : "Stable";
  const pr = I - S, gv = G - T, fo = X - M;
  $("#nv").textContent = net === 0 ? "Injections equal withdrawals: national income is in equilibrium."
    : `${net > 0 ? "Injections exceed withdrawals" : "Withdrawals exceed injections"} by $${Math.abs(net)}m, so national income ${net > 0 ? "rises" : "falls"}. Private sector (I − S): ${pr >= 0 ? "+" : "−"}${Math.abs(pr)}; government (G − T): ${gv >= 0 ? "+" : "−"}${Math.abs(gv)}; foreign (X − M): ${fo >= 0 ? "+" : "−"}${Math.abs(fo)}.`;
  const H = (v) => v * 0.9, base = 250;
  let o = SV.line(30, base, 400, base);
  [[70, [I, G, X], "Injections", ["I", "G", "X"]], [240, [S, T, M], "Withdrawals", ["S", "T", "M"]]].forEach(([x, vals, l, nm]) => {
    let y = base; const cl = ["f1", "f3", "f4"];
    vals.forEach((v, i) => { const h = H(v); o += SV.rect(x, y - h, 100, h, cl[i]) + (h > 14 ? SV.text(x + 50, y - h / 2 + 4, nm[i] + " " + v, "sm bd", { "text-anchor": "middle", ...halo }) : ""); y -= h; });
    o += SV.text(x + 50, y - 8, "$" + vals.reduce((a, b) => a + b, 0) + "m", "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 50, 272, l, "sm", { "text-anchor": "middle" });
  });
  $("#labK").innerHTML = o;
}
[["#g3", "fi", "Investment I"], ["#g4", "fs", "Saving S"], ["#g5", "fg", "Government spending G"], ["#g6", "ft", "Taxes T"], ["#g7", "fx", "Exports X"], ["#g8", "fm", "Imports M"]].forEach(([sel, id, lab], k) => Lib.slider($(sel), { id, label: lab + " ($m): ", min: 0, max: 100, step: 10, value: [60, 50, 80, 70, 40, 50][k], fmt: (v) => v, onInput: labNet }));

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), {
  prompt: "Is each flow an injection into, a withdrawal from, or neither in the circular flow of income?",
  buckets: [{ label: "Injection" }, { label: "Withdrawal" }, { label: "Neither (stays inside the flow)" }],
  items: [
    { text: "Firms buying new machinery", b: 0 }, { text: "Government spending on hospitals", b: 0 }, { text: "Foreign tourists spending in hotels", b: 0 }, { text: "Exports of manufactured goods", b: 0 },
    { text: "Households saving in a bank", b: 1 }, { text: "Income tax paid", b: 1 }, { text: "Spending on imported cars", b: 1 }, { text: "Residents holidaying abroad", b: 1 },
    { text: "A household buying domestic groceries", b: 2 }, { text: "Wages paid to workers by firms", b: 2 }, { text: "Moving money between two bank accounts", b: 2 },
  ], done: "Injections are I, G and X; withdrawals are S, T and M. Spending on domestic goods and wages stay inside the flow.",
});
Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Circular flow of income", "A model of money moving between households, firms and other sectors"],
  ["Injection", "Spending that enters the circular flow: I, G or X"],
  ["Withdrawal (leakage)", "Income that leaves the circular flow: S, T or M"],
  ["Equilibrium national income", "The level of income at which injections equal withdrawals"],
  ["Net injection", "Total injections greater than total withdrawals"],
  ["Full employment level of income", "The level of national income when all resources are fully employed"],
  ["Transfer payment", "A payment such as a benefit with no good or service in return (a negative tax)"],
], done: "Seven words for the circular flow." });
Lib.order($("#o1"), { prompt: "Put the effects of a rise in exports in order.", items: [
  "Foreign demand for the country's exports rises",
  "Injections (X) are greater than withdrawals",
  "Spending on domestic output rises above income",
  "Firms increase output and take on more workers",
  "National income rises, and withdrawals (saving, taxes, imports) rise with it",
  "A new equilibrium is reached where injections again equal withdrawals",
], done: "A reliable chain for any change in injections." });
Lib.calc($("#c1"), { qs: [
  { q: "Investment is $60m, government spending $80m and exports $40m. What are total injections ($m)?", a: 180, sol: "60 + 80 + 40 = <b>$180m</b>." },
  { q: "Saving is $50m, taxes $70m and imports $50m. What are total withdrawals ($m)?", a: 170, sol: "50 + 70 + 50 = <b>$170m</b>." },
  { q: "Using those figures, what is the net injection ($m)?", a: 10, sol: "180 − 170 = <b>+$10m</b>: national income is likely to rise." },
  { q: "Withdrawals are W = 0.25Y and injections are $150m. What is equilibrium national income ($m)?", a: 600, hint: "Set 0.25Y = 150.", sol: "Y = 150 ÷ 0.25 = <b>$600m</b>." },
  { q: "Injections rise to $180m with W = 0.25Y. What is the new equilibrium income ($m)?", a: 720, sol: "Y = 180 ÷ 0.25 = <b>$720m</b>." },
  { q: "By how much did income rise when injections rose from $150m to $180m ($m)?", a: 120, sol: "720 − 600 = <b>$120m</b>, four times the $30m rise in injections." },
  { q: "A government spends $100m and collects $80m in taxes. Is the government a net injection or withdrawal, and by how much ($m, positive for injection)?", a: 20, sol: "G − T = 100 − 80 = <b>+$20m</b>: a net injection." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which is an injection into the circular flow?", opts: ["saving", "taxation", "imports", "investment"], a: 3, why: "Injections are investment, government spending and exports." },
  { q: "Which is a withdrawal from the circular flow?", opts: ["government spending", "exports", "saving", "investment"], a: 2, why: "Withdrawals are saving, taxes and imports." },
  { q: "National income is in equilibrium when:", opts: ["saving equals investment only", "injections equal withdrawals", "exports equal imports only", "government spending equals zero"], a: 1, why: "J = W: the flow is neither growing nor shrinking." },
  { q: "If injections exceed withdrawals, national income will:", opts: ["rise", "fall", "stay the same", "become zero"], a: 0, why: "Spending is above income, so firms produce and employ more." },
  { q: "A rise in the rate of interest is likely to:", opts: ["raise saving and cut investment", "cut saving and raise investment", "raise exports directly", "have no effect on J or W"], a: 0, why: "Saving rewards rise and borrowing costs rise." },
  { q: "Spending by foreign tourists in a country is:", opts: ["an import", "an export, so an injection", "a withdrawal", "a transfer payment"], a: 1, why: "Foreigners buying the country's services are buying exports." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Circular flow of income", "Money flows from firms to households as income and back as spending, with withdrawals and injections."],
  ["Injection", "Spending added to the flow: investment, government spending and exports."],
  ["Withdrawal (leakage)", "Income taken out of the flow: saving, taxes and imports."],
  ["J = I + G + X", "Total injections."],
  ["W = S + T + M", "Total withdrawals."],
  ["Equilibrium", "National income is stable where injections equal withdrawals."],
  ["Net injection", "J greater than W: income rises."],
  ["Net withdrawal", "W greater than J: income falls."],
  ["Full employment level of income", "The level of income when all resources are fully employed."],
  ["Transfer payment", "A benefit with no good or service in return; treated as a negative tax."],
] });
''' + 'Lib.quiz($("#qz2"), { qs: [\n' + "".join(mc(*i) for i in [
  ("[Feb/March 2021 · 32 · Q27] Which row correctly identifies injections into a country's circular flow of income? (private sector S > I, public sector T > G, trade sector X > M)", ["no, no, no", "no, no, yes", "yes, no, no", "yes, yes, yes"], 1, "Net injections come from the trade sector when X > M. S > I and T > G are net withdrawals."),
  ("[May/June 2021 · 31 · Q27] What would be an increase in leakages or withdrawals from the circular flow of income?", ["increase in government spending on anti-smoking campaigns", "increase in spending on imports of luxury cars", "increase in spending on transfer payments", "increase in wages paid to government employees"], 1, "Imports are a withdrawal. Government spending, transfers and public wages are injections or neutral."),
  ("[May/June 2022 · 32 · Q25] What does not change the level of withdrawals from the circular flow of income?", ["households having more of their income taken in tax following a rise in the rate of income tax", "households spending more on imported cars following a currency appreciation", "households taking money from their savings to spend on a celebration", "households transferring money from an account in one bank to a different bank"], 3, "Moving money between banks does not change saving, taxes or imports. A, B and C change T, M and S."),
  ("[May/June 2022 · 32 · Q27] What could be used to offset a leakage from the circular flow of income?", ["a reduction in domestic consumption", "a reduction in government expenditure", "an increase in the rate of interest", "an increase in investment"], 3, "Investment is an injection, so it offsets a leakage such as saving."),
  ("[Oct/Nov 2020 · 31 · Q25] Which correctly identifies net leakages from a country's circular flow of income? (private sector S > I, government sector T > G, trade sector X > M)", ["no, no, no", "no, no, yes", "yes, yes, no", "yes, yes, yes"], 2, "Net leakages need S > I and T > G, but X > M would be a net injection, so the trade sector is 'no'."),
  ("[Oct/Nov 2021 · 33 · Q23] What is not considered to be an injection into the circular flow of income of an economy?", ["a rise in exports of financial services", "firms investing in new production techniques", "increased government spending on health services", "spending on hotels and entertainment by tourists visiting another country"], 3, "Spending by residents visiting another country is an import for their home economy, not an injection."),
  ("[Oct/Nov 2021 · 33 · Q25] What identifies net injections into a country's circular flow of income? (I > S, X < M, G < T)", ["yes, no, no", "yes, no, yes", "no, yes, no", "no, yes, yes"], 0, "Net injections need I > S, X > M and G > T. So I > S is 'yes', while X < M and G < T are 'no'."),
]) + '] });\n'
write("cf1", page(EY.format(1), "The Circular Flow of Income, Injections and Withdrawals",
  "How money moves between households, firms, banks, the government and the rest of the world, what counts as an injection or a withdrawal, and why national income settles where J = W. Animated diagrams, labs, drills and the past paper questions.",
  learn=learn, watch=watch, explore=explore, practise=practise, real=real, exam=exam, tips=tips), js,
  "The Circular Flow of Income, Injections and Withdrawals", "circular-flow-of-income")

# ------------------------------------------------------------------ 41.2
learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>The <b>multiplier</b> is the number of times an initial change in injections is multiplied into a larger change in national income: <b>ΔY = k × ΔJ</b>. Each round of spending becomes someone else's income, but part of it leaks out as saving, taxes and imports, so the rounds get smaller. The size of the multiplier is <b>k = 1 ÷ (1 − MPC)</b> in a simple closed economy, and more generally <b>k = 1 ÷ MPW</b>, where the <b>marginal propensity to withdraw</b> is <b>MPS + MRT + MPM</b>. The smaller the leakages, the larger the multiplier, but it only gives real output gains when there is spare capacity.</p></div>

  <h2>1 · The multiplier process</h2>
  <p>Suppose investment rises by $100m and households spend 60% of any extra income (MPC = 0.6). Firms and workers who earn the $100m spend $60m. That $60m becomes income for others, who spend $36m, and so on.</p>
  <div class="tw"><table class="t">
    <tr><th>Round</th><th>New spending ($m)</th><th>Running total ($m)</th></tr>
    <tr><td>1</td><td>100</td><td>100</td></tr>
    <tr><td>2</td><td>60</td><td>160</td></tr>
    <tr><td>3</td><td>36</td><td>196</td></tr>
    <tr><td>4</td><td>21.6</td><td>217.6</td></tr>
    <tr><td>and so on</td><td>…</td><td>approaches <b>250</b></td></tr>
  </table></div>
  <p>The total is 100 × 1 ÷ (1 − 0.6) = 100 × 2.5 = <b>$250m</b>.</p>

  <h2>2 · Formulae</h2>
  <div class="formula">Closed economy, no government: k = 1 ÷ (1 − MPC) = 1 ÷ MPS</div>
  <div class="formula">With taxes and imports: k = 1 ÷ MPW = 1 ÷ (MPS + MRT + MPM)</div>
  <div class="tw"><table class="t">
    <tr><th>MPC</th><th>MPS</th><th>Multiplier k = 1 ÷ MPS</th><th>Rise in income from an injection of $100m</th></tr>
    <tr><td>0.5</td><td>0.5</td><td>2</td><td>$200m</td></tr>
    <tr><td>0.6</td><td>0.4</td><td>2.5</td><td>$250m</td></tr>
    <tr><td>0.8</td><td>0.2</td><td>5</td><td>$500m</td></tr>
    <tr><td>0.9</td><td>0.1</td><td>10</td><td>$1,000m</td></tr>
  </table></div>
  <p>With a marginal rate of taxation of 0.1 and a marginal propensity to import of 0.1 as well as an MPS of 0.2, MPW = 0.4 and the multiplier falls from 5 to 2.5.</p>

  <h2>3 · What makes the multiplier bigger or smaller</h2>
  <div class="grid2">
    <div class="card"><h3>Larger multiplier</h3><ul><li>High marginal propensity to consume</li><li>Low marginal propensity to save</li><li>Low marginal rate of taxation</li><li>Low marginal propensity to import</li></ul></div>
    <div class="card"><h3>Smaller multiplier</h3><ul><li>High marginal propensity to save</li><li>Higher tax rates (and benefits that are withdrawn)</li><li>High marginal propensity to import: spending leaks abroad</li><li>Households and firms that save windfalls</li></ul></div>
  </div>

  <h2>4 · Evaluating the multiplier</h2>
  <ul>
    <li><b>Spare capacity.</b> The multiplier assumes unemployed resources and fixed prices. Near full employment extra spending mostly raises prices.</li>
    <li><b>Time lags.</b> Each round takes time, so the full effect may take a year or more.</li>
    <li><b>Crowding out.</b> Extra government spending financed by borrowing may raise interest rates and reduce private investment.</li>
    <li><b>Changes in the leakages.</b> The MPC, MRT and MPM may not be constant as income changes.</li>
    <li><b>Direction.</b> The multiplier works in reverse: a fall in injections reduces income by a multiple.</li>
  </ul>
  <p class="note">The Resources section for this chapter has a step-by-step walkthrough of the multiplier diagram, "Multipliers, Markets and Monopsony".</p>
'''
watch = '''
  <h2>1 · Rounds of spending</h2>
  <p>An injection of $100m and MPC = 0.6. Press Play, or click the steps.</p><div id="stR"></div>
  <h2>2 · Leakages shrink the multiplier</h2>
  <p>The same $100m injection with MPS = 0.2, then with taxes and imports added.</p><div id="stK"></div>
'''
explore = '''
  <h2>Lab 1 · Multiplier calculator</h2>
  <p>Set the three marginal propensities to withdraw and the size of the injection. The multiplier is 1 ÷ (MPS + MRT + MPM).</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div><div id="g4"></div>
    <div class="readout"><div><small>MPW</small><strong id="k1"></strong></div><div><small>Multiplier</small><strong id="k2"></strong></div><div><small>Rise in income</small><strong id="k3"></strong></div></div>
    <div class="verdict" id="kv"></div></div>
    <div><svg id="labL" viewBox="0 0 420 260" role="img" aria-label="Bars comparing the initial injection with the total rise in income"></svg></div></div></div>

  <h2>Lab 2 · Round by round</h2>
  <p>Closed economy, no government. See how much of the total has been reached after each round.</p>
  <div class="card"><div class="grid2"><div><div id="g5"></div><div id="g6"></div>
    <div class="readout"><div><small>Multiplier 1 ÷ (1 − MPC)</small><strong id="r1"></strong></div><div><small>Final rise in income</small><strong id="r2"></strong></div><div><small>Share reached after 5 rounds</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labM" viewBox="0 0 420 280" role="img" aria-label="Bars of new spending in each round of the multiplier process"></svg></div></div></div>
'''
practise = '''
  <h2>1 · Raises or lowers the multiplier?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the multiplier process in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''
real = RW + '''  <div class="rw"><h3>A new factory in a small town</h3><p>Building and running a factory pays wages and buys local supplies. Workers spend on food, rent and services, and those businesses pay their own staff. A town where most spending stays local has a larger multiplier than one where people buy mainly from outside.</p><div class="use"><b>Exam use:</b> the multiplier effect of extra employment, as in the Ghana oil question.</div></div>
  <div class="rw"><h3>Stimulus payments</h3><p>When a government sends cash to households in a recession, the effect depends on how much is spent. If most is saved, MPS is high, the multiplier is low and the rise in income is small.</p><div class="use"><b>Exam use:</b> why the size of the MPC matters for fiscal policy.</div></div>
  <div class="rw"><h3>A small, open economy</h3><p>In an economy that imports much of what it consumes, a large share of extra income leaks abroad. The marginal propensity to import is high and the multiplier is small.</p><div class="use"><b>Exam use:</b> how openness reduces the multiplier.</div></div>
'''
exam = '''
  <h2>Past paper questions on the multiplier</h2>
  <p>We searched the A Level Economics papers in the folder (2020 to 2025). Below are the Paper 4 data response part that used the multiplier effect, a practice question with a model answer, and twelve Paper 3 multiple choice questions including several calculations. Mark scheme points are summarised in our own words, not copied.</p>
  <div class="tw"><table class="t">
    <tr><th>Type</th><th>Examples found</th><th>Where</th></tr>
    <tr><td>Data response part, 4 marks</td><td>1</td><td>Oct/Nov 2024 (41)</td></tr>
    <tr><td>Multiple choice (Paper 3)</td><td>12 shown below</td><td>2020 to 2025</td></tr>
  </table></div>
  <h2>A · Data response part</h2>
  <details class="eq"><summary>Oct/Nov 2024 · 9708/41 · Q1(b) <span class="mark">4 marks</span> Explain how the extraction of natural resources in Ghana will 'create further employment in other sectors through the multiplier effect'.</summary><div class="body">
    <div class="tip"><b class="h">What the mark scheme wants</b>
      <ul><li><b>Two marks for understanding:</b> the multiplier is the total rise in national income or output that follows an initial rise in injections into the circular flow.</li><li><b>Two marks for application:</b> the article identifies new jobs and incomes in the extraction industry, and these create a further round of spending, jobs and income in other sectors.</li><li>To stay in the same band, use the case: workers in the oil sector spend on local goods and services, so other firms produce more and hire more.</li></ul></div>
  </div></details>
  <h2>B · Practice question with a model answer</h2>
  <details class="eq"><summary>Practice (not a past paper question) <span class="mark">8 marks</span> Explain why a rise in government spending of $100m might raise national income by more than $100m.</summary><div class="body">
    <div class="tip"><b class="h">Plan</b>Define the multiplier. Walk through two rounds. Give the formula. Then one evaluative point on leakages or spare capacity.</div>
    <div class="key"><span class="k"><i></i>K</span><span class="a"><i></i>A</span><span class="n"><i></i>N</span><span class="e"><i></i>E</span></div>
    <div class="ans">
    <p><span class="mk k" data-t="K">The multiplier is the ratio of the change in national income to the initial change in injections. The multiplier is given by 1 ÷ (1 − MPC) in a closed economy with no government, or more generally 1 ÷ MPW, where MPW is the marginal propensity to withdraw (MPS + MRT + MPM).</span></p>
    <p><span class="mk n" data-t="N">Government spending of $100m becomes income for the firms and workers who provide the goods. If they spend 60% of any extra income (MPC = 0.6), $60m is spent on other firms' output, which becomes their income, and they spend $36m, and so on. The rounds get smaller because some income leaks out as saving, taxes and imports, but the total is $100m × 1 ÷ 0.4 = $250m, which is more than the original $100m.</span></p>
    <p><span class="mk e" data-t="E">The multiplier could be smaller in practice if households save much of the extra income, if the economy imports a lot, or if higher taxes follow. It also assumes spare capacity: near full employment the extra spending may raise prices more than output.</span></p></div>
  </div></details>
  <h2>C · Multiple choice questions (Paper 3)</h2>
  <p>Choose an answer, then read the reason. Source: paper code and question number.</p>
  <div id="qz2"></div>
'''
tips = '''
  <h2>Top tips</h2>
  <ul class="tips">
    <li><b>Write the formula and show working:</b> k = 1 ÷ MPS (closed, no government) or 1 ÷ (MPS + MRT + MPM). Then ΔY = k × ΔJ.</li>
    <li><b>Check which propensities the question gives.</b> MPC alone is only enough in the closed, no-government model. Add MRT and MPM for the full leakage.</li>
    <li><b>Say why the rounds shrink:</b> part of each round leaks out as saving, taxes and imports.</li>
    <li><b>Remember it works in reverse.</b> A fall in injections reduces income by a multiple.</li>
    <li><b>Evaluate with spare capacity,</b> time lags, crowding out and changing propensities.</li>
    <li><b>Link the multiplier to policy:</b> a larger multiplier means a smaller injection is needed to close a gap in output.</li>
  </ul>
  <h2>Sentences you can use</h2>
  <div class="tw"><table class="t">
    <tr><th>You want to say</th><th>Use this sentence</th></tr>
    <tr><td>Definition</td><td>"The multiplier shows by how much national income changes when injections change."</td></tr>
    <tr><td>Process</td><td>"The initial spending becomes income for others, who spend part of it, so national income rises by a multiple."</td></tr>
    <tr><td>Size</td><td>"The multiplier is larger when the marginal propensity to withdraw is lower."</td></tr>
    <tr><td>Evaluate</td><td>"However, the multiplier may be small if there is little spare capacity or if much of the extra income is saved or spent on imports."</td></tr>
  </table></div>
  <h2>Command words</h2>
  <div class="tw"><table class="t">
    <tr><th>Command word</th><th>What it asks for</th></tr>
    <tr><td>Explain</td><td>Give reasons, with a clear chain of cause and effect.</td></tr>
    <tr><td>Calculate</td><td>Formula, substitution, answer with units.</td></tr>
    <tr><td>Evaluate</td><td>Weigh the arguments and reach a supported conclusion.</td></tr>
  </table></div>
  <h2>Flashcards</h2><div id="fc1"></div>
'''
js = HEAD + '''
/* ---------- Watch 1: rounds ---------- */
const RC = 0.6, RB = 270, RH = (v) => v * 2.0;
function roundsDraw(s) {
  let o = SV.line(60, RB, 740, RB) + SV.text(62, 24, "New spending in each round ($m)", "sm");
  let v = 100, cum = 0;
  for (let i = 0; i < 8; i++) {
    const k = Math.max(0, Math.min(1, s.n - i)); cum += v;
    if (k > 0) o += SV.rect(90 + i * 80, RB - RH(v) * k, 56, RH(v) * k, "f1", op(k)) + SV.text(118 + i * 80, RB - RH(v) * k - 6, Lib.fmtN(v, 1), "sm bd", { "text-anchor": "middle", ...op(k) }) + SV.text(118 + i * 80, RB + 18, "round " + (i + 1), "sm", { "text-anchor": "middle", ...op(k) });
    v *= RC;
  }
  if (s.t > 0) o += SV.text(400, 70, "total approaches $250m = 100 × 1 ÷ (1 − 0.6)", "lbl bd t3", { "text-anchor": "middle", ...halo, ...op(s.t) });
  return o;
}
Lib.stepper($("#stR"), { w: 780, h: 310, label: "Rounds of spending after an injection of 100 million with a marginal propensity to consume of 0.6", base: { n: 0, t: 0 }, draw: roundsDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>Round 1.</b> The injection of <b>$100m</b> is paid out as income to firms and workers.", s: { n: 1 } },
  { cap: "<b>Round 2.</b> They spend 60% of it (MPC = 0.6): <b>$60m</b> becomes income for other firms and workers. The rest leaks out as saving, taxes or imports.", s: { n: 2 } },
  { cap: "<b>Round 3.</b> $60m × 0.6 = <b>$36m</b> is spent again. Each round is 0.6 times the one before.", s: { n: 3 } },
  { cap: "<b>Later rounds</b> keep shrinking: $21.6m, $13m, $7.8m, $4.7m, $2.8m…", s: { n: 8 } },
  { cap: "<b>The total.</b> The rounds add up to <b>$250m</b>: the multiplier is 1 ÷ (1 − 0.6) = <b>2.5</b>, so national income rises by 2.5 times the injection.", s: { n: 8, t: 1 } },
] });

/* ---------- Watch 2: leakages ---------- */
function kDraw(s) {
  const B = 270, H = (v) => v * 0.38;
  let o = SV.line(60, B, 740, B) + SV.text(62, 24, "Rise in income from a $100m injection ($m)", "sm");
  [[110, 500, "f3", "MPS 0.2", "k = 5", s.a], [330, 333.3, "f1", "+ taxes (MRT 0.1)", "k = 3.3", s.b], [550, 250, "f2", "+ imports (MPM 0.1)", "k = 2.5", s.c]].forEach(([x, v, c, l, k, f]) => {
    if (f <= 0) return;
    o += SV.rect(x, B - H(v) * f, 100, H(v) * f, c, op(f)) + SV.text(x + 50, B - H(v) * f - 20, "$" + Lib.fmtN(v, 0) + "m", "lbl bd", { "text-anchor": "middle", ...op(f) }) + SV.text(x + 50, B - H(v) * f - 4, k, "sm bd", { "text-anchor": "middle", ...op(f) }) + SV.text(x + 50, B + 18, l, "sm", { "text-anchor": "middle", ...op(f) });
  });
  return o;
}
Lib.stepper($("#stK"), { w: 780, h: 310, label: "Rise in income from an injection of 100 million as taxes and imports are added to the leakages", base: { a: 0, b: 0, c: 0 }, draw: kDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>Saving only.</b> With MPS = 0.2 and no taxes or imports, MPW = 0.2, so k = 1 ÷ 0.2 = <b>5</b>. A $100m injection raises income by <b>$500m</b>.", s: { a: 1 } },
  { cap: "<b>Add taxes.</b> A marginal rate of taxation of 0.1 raises MPW to 0.3, so k = 1 ÷ 0.3 = <b>3.3</b>. Income rises by <b>$333m</b>.", s: { a: 1, b: 1 } },
  { cap: "<b>Add imports.</b> A marginal propensity to import of 0.1 raises MPW to 0.4, so k = 1 ÷ 0.4 = <b>2.5</b>. Income rises by only <b>$250m</b>: every leakage shrinks the multiplier.", s: { a: 1, b: 1, c: 1 } },
] });

/* ---------- Lab 1 ---------- */
function labMul() {
  if (!$("#ms") || !$("#mt") || !$("#mi") || !$("#mj")) return;
  const s = +$("#ms").value, t = +$("#mt").value, m = +$("#mi").value, J = +$("#mj").value, w = s + t + m, k = 1 / w, dy = k * J;
  $("#k1").textContent = Lib.fmtN(w, 2); $("#k2").textContent = Lib.fmtN(k, 2); $("#k3").textContent = "$" + Lib.fmtN(dy, 0) + "m";
  $("#kv").textContent = `MPW = ${Lib.fmtN(s, 2)} + ${Lib.fmtN(t, 2)} + ${Lib.fmtN(m, 2)} = ${Lib.fmtN(w, 2)}, so the multiplier is 1 ÷ ${Lib.fmtN(w, 2)} = ${Lib.fmtN(k, 2)}. An injection of $${J}m raises national income by $${Lib.fmtN(dy, 0)}m. Lower any of the three leakages and the multiplier rises.`;
  const H = (v) => v / 8, base = 200;
  let o = SV.line(30, base, 400, base);
  [[80, J, "f3", "Injection"], [240, dy, "f1", "Rise in income"]].forEach(([x, v, c, l]) => { o += SV.rect(x, base - H(v), 100, H(v), c) + SV.text(x + 50, base - H(v) - 8, "$" + Lib.fmtN(v, 0) + "m", "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 50, 220, l, "sm", { "text-anchor": "middle" }); });
  $("#labL").innerHTML = o;
}
Lib.slider($("#g1"), { id: "ms", label: "Marginal propensity to save: ", min: 0.05, max: 0.5, step: 0.05, value: 0.2, fmt: (v) => Lib.fmtN(v, 2), onInput: labMul });
Lib.slider($("#g2"), { id: "mt", label: "Marginal rate of taxation: ", min: 0, max: 0.4, step: 0.05, value: 0.1, fmt: (v) => Lib.fmtN(v, 2), onInput: labMul });
Lib.slider($("#g3"), { id: "mi", label: "Marginal propensity to import: ", min: 0, max: 0.4, step: 0.05, value: 0.1, fmt: (v) => Lib.fmtN(v, 2), onInput: labMul });
Lib.slider($("#g4"), { id: "mj", label: "Injection ($m): ", min: 50, max: 200, step: 10, value: 100, fmt: (v) => v, onInput: labMul });

/* ---------- Lab 2 ---------- */
function labRnd() {
  if (!$("#rc") || !$("#rj")) return;
  const c = +$("#rc").value, J = +$("#rj").value, k = 1 / (1 - c), fin = k * J; let v = J, cum = 0; const vals = [];
  for (let i = 0; i < 10; i++) { vals.push(v); cum += v; if (i === 4) var c5 = cum; v *= c; }
  $("#r1").textContent = Lib.fmtN(k, 2); $("#r2").textContent = "$" + Lib.fmtN(fin, 0) + "m"; $("#r3").textContent = Math.round((c5 / fin) * 100) + "%";
  $("#rv").textContent = `With MPC = ${Lib.fmtN(c, 2)} the multiplier is ${Lib.fmtN(k, 2)}. After five rounds ${Math.round((c5 / fin) * 100)}% of the final $${Lib.fmtN(fin, 0)}m has been reached. A higher MPC means the rounds shrink more slowly, so the total is bigger and takes longer to arrive.`;
  const H = (x) => 190 * x / J, base = 230;
  let o = SV.line(30, base, 400, base);
  vals.forEach((x, i) => { o += SV.rect(40 + i * 36, base - H(x), 26, H(x), "f1") + SV.text(53 + i * 36, base + 14, i + 1, "sm", { "text-anchor": "middle" }); });
  o += SV.text(210, 270, "round", "sm", { "text-anchor": "middle" });
  $("#labM").innerHTML = o;
}
Lib.slider($("#g5"), { id: "rc", label: "Marginal propensity to consume: ", min: 0.3, max: 0.9, step: 0.05, value: 0.6, fmt: (v) => Lib.fmtN(v, 2), onInput: labRnd });
Lib.slider($("#g6"), { id: "rj", label: "Injection ($m): ", min: 50, max: 200, step: 10, value: 100, fmt: (v) => v, onInput: labRnd });

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), {
  prompt: "Does each change raise or lower the value of the multiplier?",
  buckets: [{ label: "Raises the multiplier" }, { label: "Lowers the multiplier" }],
  items: [
    { text: "A higher marginal propensity to consume", b: 0 }, { text: "A lower marginal propensity to save", b: 0 }, { text: "A cut in the marginal rate of taxation", b: 0 }, { text: "A fall in the marginal propensity to import", b: 0 },
    { text: "A higher marginal propensity to save", b: 1 }, { text: "A rise in the marginal rate of taxation", b: 1 }, { text: "A rise in the marginal propensity to import", b: 1 }, { text: "More households saving windfall income", b: 1 },
  ], done: "Anything that increases leakages lowers the multiplier; anything that reduces them raises it.",
});
Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Multiplier", "The change in national income divided by the initial change in injections"],
  ["Marginal propensity to consume (MPC)", "The share of an extra dollar of income that is spent"],
  ["Marginal propensity to save (MPS)", "The share of an extra dollar of income that is saved"],
  ["Marginal rate of taxation (MRT)", "The share of an extra dollar of income paid in tax"],
  ["Marginal propensity to import (MPM)", "The share of an extra dollar of income spent on imports"],
  ["Marginal propensity to withdraw (MPW)", "MPS + MRT + MPM: the share of extra income that leaks out"],
  ["Crowding out", "Government borrowing that raises interest rates and cuts private investment"],
], done: "Seven words for the multiplier." });
Lib.order($("#o1"), { prompt: "Put the multiplier process in order.", items: [
  "Injections rise, for example government spending increases by $100m",
  "The $100m becomes income for firms and workers",
  "They spend a share of it (the MPC) on other firms' output",
  "That spending becomes income for others, who spend part of it again",
  "Each round is smaller because of leakages into saving, taxes and imports",
  "National income rises by a multiple of the original injection",
], done: "Always mention the leakages that make each round smaller." });
Lib.calc($("#c1"), { qs: [
  { q: "In a closed economy with no government the MPC is 0.8. What is the multiplier?", a: 5, sol: "1 ÷ (1 − 0.8) = <b>5</b>." },
  { q: "An injection of $40m is made with a multiplier of 5. By how much does national income rise ($m)?", a: 200, sol: "5 × 40 = <b>$200m</b>." },
  { q: "The MPC is 0.6 in a closed economy with no government and investment rises by $100m. What is the rise in national income ($m)?", a: 250, sol: "1 ÷ 0.4 = 2.5; 2.5 × 100 = <b>$250m</b>." },
  { q: "MPS = 0.2, MRT = 0.2 and MPM = 0.1. What is the multiplier?", a: 2, sol: "MPW = 0.5, so k = 1 ÷ 0.5 = <b>2</b>." },
  { q: "In a closed economy MPS = 0.1 and MRT = 0.1. What is the rise in national income from an injection of $100m ($m)?", a: 500, sol: "MPW = 0.2, k = 5, rise = <b>$500m</b>." },
  { q: "Investment rises by $20bn and national income rises by $100bn. What is the multiplier?", a: 5, sol: "100 ÷ 20 = <b>5</b>." },
  { q: "Using that multiplier in a closed economy with no government, what is the MPC?", a: 0.8, tol: 0.01, sol: "k = 1 ÷ (1 − MPC) = 5 gives 1 − MPC = 0.2, so MPC = <b>0.8</b>." },
  { q: "A consumer's income rises from $1,000 to $1,200 and consumption rises from $800 to $900. What is the MPC?", a: 0.5, tol: 0.01, sol: "100 ÷ 200 = <b>0.5</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "The multiplier is greater when:", opts: ["the marginal propensity to save is high", "the marginal propensity to import is low", "the marginal rate of taxation is high", "withdrawals are large"], a: 1, why: "Lower leakages mean more of each round is re-spent." },
  { q: "If MPC = 0.75 in a closed economy with no government the multiplier is:", opts: ["0.75", "1.33", "4", "7.5"], a: 2, why: "1 ÷ (1 − 0.75) = 4." },
  { q: "The multiplier effect works best when:", opts: ["the economy is at full employment", "there is spare capacity", "prices are rising fast", "imports are very high"], a: 1, why: "Unemployed resources allow output to rise rather than prices." },
  { q: "A rise in the rate of income tax will most likely:", opts: ["raise the multiplier", "lower the multiplier", "have no effect on the multiplier", "make MPC rise"], a: 1, why: "A higher marginal rate of taxation increases the leakage." },
  { q: "A fall in injections will:", opts: ["raise income by a multiple", "reduce income by a multiple", "not affect income", "raise the multiplier"], a: 1, why: "The multiplier works in both directions." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Multiplier", "The ratio of the change in national income to the change in injections that caused it."],
  ["k = 1 ÷ (1 − MPC)", "The multiplier in a closed economy with no government."],
  ["k = 1 ÷ MPW", "The multiplier with all leakages: MPW = MPS + MRT + MPM."],
  ["MPC", "The share of extra income that is spent."],
  ["MPS", "The share of extra income that is saved."],
  ["MRT", "Marginal rate of taxation: the share of extra income paid in tax."],
  ["MPM", "Marginal propensity to import: the share of extra income spent on imports."],
  ["ΔY = k × ΔJ", "The change in national income equals the multiplier times the change in injections."],
  ["Crowding out", "Government borrowing that pushes up interest rates and reduces private investment."],
  ["Multiplier in reverse", "A fall in injections reduces income by a multiple."],
] });
''' + 'Lib.quiz($("#qz2"), { qs: [\n' + "".join(mc(*i) for i in [
  ("[Feb/March 2022 · 32 · Q27] In a closed economy with no government sector, the multiplier shows the impact of a change in", ["consumption on investment.", "investment on national income.", "national income on consumption.", "national income on investment."], 1, "The multiplier shows how a change in investment (an injection) changes national income."),
  ("[Feb/March 2021 · 32 · Q24] In a closed economy, the marginal propensity to save is 0.1 and the marginal propensity to pay taxes is also 0.1. These values are constant. What will be the increase in national income if there is an injection of $100 million into the circular flow?", ["$1000 million", "$500 million", "$100 million", "$80 million"], 1, "MPW = 0.1 + 0.1 = 0.2, so the multiplier is 5 and income rises by 5 × $100m = $500m."),
  ("[Oct/Nov 2020 · 33 · Q23] What reduces the value of the multiplier?", ["an increase in government investment expenditure", "an increase in consumption", "an increase in the rate of taxation", "an increase in the volume of exports"], 2, "A higher tax rate increases a leakage. A, B and D increase injections or spending, not the size of the multiplier."),
  ("[Oct/Nov 2020 · 32 · Q26] According to Keynesian theory, how will an increase in autonomous spending affect the value of equilibrium income?", ["Income will increase by an amount equal to the value of autonomous spending.", "Income will increase by an amount greater than the value of autonomous spending.", "Income will increase by an amount smaller than the value of autonomous spending.", "Income will not increase as a result of autonomous spending."], 1, "The multiplier effect means income rises by more than the initial spending."),
  ("[May/June 2021 · 31 · Q24] What describes the multiplier process, as it operates within a closed economy with no government sector?", ["Changes in National Income determine the level of investment.", "The level of consumption depends on the level of National Income.", "The levels of consumption and investment together determine the level of National Income.", "When investment changes, there will be a greater change in equilibrium National Income."], 3, "The multiplier is the greater change in income that follows a change in investment."),
  ("[Oct/Nov 2021 · 32 · Q25] In a closed economy with no government sector the marginal propensity to consume is 0.6 at all levels of income. There is an increase in private sector investment of $100 million. What will be the increase in national income?", ["$60 million", "$100 million", "$166 million", "$250 million"], 3, "k = 1 ÷ (1 − 0.6) = 2.5, so the rise in income is 2.5 × $100m = $250m."),
  ("[May/June 2023 · 32 · Q21] Which condition will produce the highest value of the national income multiplier in an open economy with a government sector?", ["high average and marginal tax rates", "high marginal propensity to save", "low level of autonomous consumption", "low marginal propensity to import"], 3, "A low marginal propensity to import means less of each round leaks abroad. High tax and saving rates reduce the multiplier."),
  ("[May/June 2024 · 32 · Q19] Country X has a marginal propensity to consume (MPC) of 0.7. Its marginal propensity to save (MPS), marginal rate of taxation (MRT) and marginal propensity to import (MPM) are each 0.1. What is likely to lead to the biggest increase in the national income multiplier?", ["a 5% increase in the MPC together with a 5% fall in the MRT", "a 5% increase in the MPM together with a 5% fall in the MRT", "a 5% increase in the MPS together with a 5% fall in the MPM", "a 5% increase in the MRT together with a 5% fall in the MPS"], 0, "Raising the MPC and cutting a leakage both raise the multiplier. B, C and D each add a leakage as well as cutting one."),
  ("[Oct/Nov 2023 · 32 · Q17] The table shows MPC 0.5, MPS 0.2, MRT 0.2 and MPM 0.1 for a four-sector economy. What is the size of the multiplier?", ["1", "2", "5", "10"], 1, "MPW = 0.2 + 0.2 + 0.1 = 0.5, so the multiplier is 1 ÷ 0.5 = 2."),
  ("[Feb/March 2025 · 32 · Q24] In an economy with unemployed resources the marginal propensity to consume is 0.2. The government increases its budget deficit and finances it by selling bonds to the non-bank private sector. What is the likely consequence of this?", ["The currency will depreciate, increasing exports and reducing the trade deficit.", "The increase in real output will be limited as the value of the multiplier is low.", "The money supply will fall, leading to a reduction in aggregate demand.", "There will be a decrease in the rate of interest, causing demand-pull inflation."], 1, "With an MPC of 0.2 the multiplier is only 1.25, so the rise in real output is small."),
  ("[Feb/March 2020 · 32 · Q21] In a closed economy with no government sector, when will an increase in investment spending generate the largest increase in equilibrium national income?", ["when households have a high level of autonomous consumption", "when households have a high level of compulsory saving", "when households have a high marginal propensity to consume", "when households have a high marginal propensity to save"], 2, "A high MPC means a high multiplier."),
  ("[Oct/Nov 2021 · 31 · Q24] In a closed economy with no government there is an initial equilibrium national income of $500 billion. Households spend a constant fraction of every $1 of income. When investment increases by $20 billion national income moves to $600 billion. What is the marginal propensity to consume?", ["0.20", "0.80", "0.83", "1.00"], 1, "The multiplier is 100 ÷ 20 = 5, so MPS = 0.2 and MPC = 0.8."),
]) + '] });\n'
write("cf2", page(EY.format(2), "The Multiplier",
  "How an initial change in injections becomes a larger change in national income, the formulae with and without taxes and imports, what changes its size and its limits. Animated diagrams, labs, drills and the past paper questions.",
  learn=learn, watch=watch, explore=explore, practise=practise, real=real, exam=exam, tips=tips), js,
  "The Multiplier", "the-multiplier")

# ------------------------------------------------------------------ 41.3
learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>Consumption is the largest part of aggregate demand and depends mainly on <b>disposable income</b>: the <b>consumption function</b> is <b>C = a + cY</b>, where <b>a</b> is autonomous consumption and <b>c</b> is the <b>marginal propensity to consume (MPC)</b>. What is not consumed is <b>saved</b>, so S = Y − C and MPC + MPS = 1. Consumption and saving also depend on wealth, interest rates, confidence, credit and taxes, while <b>investment</b> depends on interest rates, expected profit and confidence, and on the <b>accelerator principle</b>: investment depends on the <b>rate of change of national income</b>. Because investment is an injection that is also volatile, it is a main cause of swings in the economy.</p></div>

  <h2>1 · The consumption function</h2>
  <div class="formula">C = a + cY &nbsp;·&nbsp; S = Y − C &nbsp;·&nbsp; MPC = ΔC ÷ ΔY &nbsp;·&nbsp; APC = C ÷ Y</div>
  <p>With a = 100 and c = 0.75, a household with income $400 consumes 100 + 0.75 × 400 = $400, so it saves nothing (break-even income). At income $200 it consumes $250 (it dissaves, using savings or borrowing); at income $800 it consumes $700 and saves $100.</p>
  <div class="tw"><table class="t">
    <tr><th>Income Y</th><th>Consumption C</th><th>Saving S</th><th>APC = C ÷ Y</th><th>MPC (extra C ÷ extra Y)</th></tr>
    <tr><td>200</td><td>250</td><td>−50</td><td>1.25</td><td></td></tr>
    <tr><td>400</td><td>400</td><td>0</td><td>1.00</td><td>0.75</td></tr>
    <tr><td>600</td><td>550</td><td>50</td><td>0.92</td><td>0.75</td></tr>
    <tr><td>800</td><td>700</td><td>100</td><td>0.88</td><td>0.75</td></tr>
  </table></div>
  <p>The <b>average propensity to consume</b> falls as income rises, while the MPC stays constant on a straight-line function. A change in income moves you <b>along</b> the function; a change in anything else (wealth, confidence, interest rates) <b>shifts</b> it.</p>

  <h2>2 · Determinants of consumption and saving</h2>
  <div class="tw"><table class="t">
    <tr><th>Factor</th><th>Effect on consumption</th></tr>
    <tr><td>Disposable income</td><td>The main determinant: more income, more consumption (a movement along the function)</td></tr>
    <tr><td>Wealth</td><td>Higher house or share prices raise consumption (the wealth effect)</td></tr>
    <tr><td>Interest rates</td><td>A lower rate cuts the reward for saving and the cost of borrowing: consumption rises</td></tr>
    <tr><td>Consumer confidence</td><td>Optimism about jobs and incomes raises spending; fear raises saving</td></tr>
    <tr><td>Availability of credit</td><td>Easier borrowing raises consumption now</td></tr>
    <tr><td>Taxes and benefits</td><td>Lower income tax raises disposable income</td></tr>
    <tr><td>Age structure and expectations of inflation</td><td>Younger households spend more of income; expected price rises may bring spending forward</td></tr>
  </table></div>

  <h2>3 · Investment and the accelerator</h2>
  <p>Investment (spending on capital goods) depends on the <b>rate of interest</b> (the cost of borrowing), <b>expected profit and business confidence</b>, the amount of <b>spare capacity</b>, technology and government policy. The <b>accelerator principle</b> says that investment depends on the <b>rate of change of national income</b>, not its level: I = v × ΔY, where v is the accelerator (the capital-output ratio).</p>
  <div class="tw"><table class="t">
    <tr><th>Year</th><th>National income</th><th>Change in income</th><th>Investment (v = 2)</th></tr>
    <tr><td>1</td><td>100</td><td></td><td></td></tr>
    <tr><td>2</td><td>110</td><td>10</td><td>20</td></tr>
    <tr><td>3</td><td>125</td><td>15</td><td>30</td></tr>
    <tr><td>4</td><td>135</td><td>10</td><td>20</td></tr>
    <tr><td>5</td><td>140</td><td>5</td><td>10</td></tr>
    <tr><td>6</td><td>140</td><td>0</td><td>0</td></tr>
  </table></div>
  <div class="tip"><b class="h">The key insight</b>Investment falls in year 4 even though income is still rising, because income is growing more slowly. That makes investment, and so aggregate demand, unstable. A slowdown in the growth of income can cut investment sharply, and a stronger recovery can lift it by more than the rise in income.</div>
  <h3>Evaluating the accelerator</h3>
  <ul>
    <li>It assumes firms are already at full capacity. With spare capacity, a rise in demand can be met without new investment.</li>
    <li>It assumes a constant capital-output ratio, and that firms can get the capital goods and finance.</li>
    <li>Expectations and interest rates also matter: firms may invest because they expect growth, or hold back despite growth if confidence is low.</li>
    <li>Time lags: orders for machinery follow changes in income after a delay.</li>
  </ul>
'''.replace("  </ul>\n'''", "'''")
watch = '''
  <h2>1 · The consumption function</h2>
  <p>C = 100 + 0.75Y. Press Play, or click the steps.</p><div id="stC"></div>
  <h2>2 · The accelerator</h2>
  <p>Income grows by smaller amounts each year; investment is twice the change in income.</p><div id="stA"></div>
'''
explore = '''
  <h2>Lab 1 · Consumption, saving and propensities</h2>
  <p>Set autonomous consumption and the MPC, then move income. The dotted line is C = Y, where saving is zero.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div>
    <div class="readout"><div><small>Consumption C</small><strong id="c1r"></strong></div><div><small>Saving S</small><strong id="c2r"></strong></div><div><small>APC</small><strong id="c3r"></strong></div><div><small>MPC</small><strong id="c4r"></strong></div></div>
    <div class="verdict" id="cv"></div></div>
    <div><svg id="labN" viewBox="0 0 420 300" role="img" aria-label="Consumption function with the 45 degree line and the chosen income level"></svg></div></div></div>

  <h2>Lab 2 · The accelerator</h2>
  <p>Income is 100 in year 1. Choose the growth rate in each of the next three years and the accelerator v. Investment is v times the change in income.</p>
  <div class="card"><div class="grid2"><div><div id="g4"></div><div id="g5"></div><div id="g6"></div><div id="g7"></div>
    <div class="readout"><div><small>Investment, year 2</small><strong id="a1"></strong></div><div><small>Investment, year 3</small><strong id="a2"></strong></div><div><small>Investment, year 4</small><strong id="a3"></strong></div></div>
    <div class="verdict" id="av"></div></div>
    <div><svg id="labO" viewBox="0 0 420 280" role="img" aria-label="Bars of national income and investment over four years"></svg></div></div></div>
'''
practise = '''
  <h2>1 · Movement along or shift of the consumption function?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the accelerator chain in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''
real = RW + '''  <div class="rw"><h3>A housing boom</h3><p>When house prices rise, owners feel wealthier and may spend more, and may borrow against the value of their homes. Consumption rises even with no change in current income: the consumption function shifts up.</p><div class="use"><b>Exam use:</b> the wealth effect as a shift of the consumption function.</div></div>
  <div class="rw"><h3>Car makers during a slowdown</h3><p>If sales of cars are still rising but more slowly, car makers may stop expanding their factories. Orders for machines and robots fall even though the market has not shrunk, which hits the firms that make capital equipment hardest.</p><div class="use"><b>Exam use:</b> the accelerator: investment depends on the rate of change of income.</div></div>
  <div class="rw"><h3>Interest rate cuts and business confidence</h3><p>A central bank cuts rates to encourage investment. If firms expect weak demand, they may leave projects on hold, so investment responds little.</p><div class="use"><b>Exam use:</b> interest-inelastic investment and the role of confidence.</div></div>
'''
exam = '''
  <h2>Past paper questions on consumption, saving and investment</h2>
  <p>We searched the A Level Economics papers in the folder (2020 to 2025). Below are the Paper 4 essay parts on the marginal propensity to consume and on saving, and seven Paper 3 multiple choice questions on the accelerator and the consumption function. Mark scheme points are summarised in our own words, not copied.</p>
  <div class="tw"><table class="t">
    <tr><th>Type</th><th>Examples found</th><th>Where</th></tr>
    <tr><td>Essay parts, 12 and 13 marks</td><td>2</td><td>Oct/Nov 2021 (41)</td></tr>
    <tr><td>Multiple choice (Paper 3)</td><td>7 shown below</td><td>2020 to 2025</td></tr>
  </table></div>
  <h2>A · Essay parts</h2>
  <div class="key"><span class="k"><i></i>Knowledge (K)</span><span class="a"><i></i>Application (A)</span><span class="n"><i></i>Analysis (N)</span><span class="e"><i></i>Evaluation (E)</span></div>
  <details class="eq"><summary>Oct/Nov 2021 · 9708/41 · Q4(a) <span class="mark">12 marks</span> Explain what economists mean by the marginal propensity to consume and consider the importance of this concept in relation to government macroeconomic policy.</summary><div class="body">
    <div class="tip"><b class="h">What the mark scheme wants</b>
      <ul><li>The <b>MPC</b>: the proportion of an extra unit of income that is spent (the change in consumption divided by the change in income), with the link to the MPS.</li><li>Its importance for the government's macroeconomic aims: the MPC determines the size of the <b>multiplier</b>, so it affects how far fiscal changes (or tax cuts) change income, output, employment and inflation, and how much is needed to close a gap.</li><li>Developed analysis relates the MPC to each of several policy goals, with comment on its limits (it may change, and varies between groups).</li></ul></div>
  </div></details>

  <details class="eq"><summary>Oct/Nov 2021 · 9708/41 · Q4(b) <span class="mark">13 marks</span> Discuss what determines the level of savings in an economy and assess the impact of an increase in the level of savings upon economic growth and employment.</summary><div class="body">
    <div class="tip"><b class="h">Plan</b>
      <ul><li><b>Determinants:</b> income and its distribution, interest rates, confidence and expectations, wealth, age structure, access to credit, tax treatment of saving.</li><li><b>Impact:</b> a rise in saving is a withdrawal, so if investment does not rise to match it, injections are below withdrawals and income, growth and employment may fall (the paradox of thrift). If savings fund investment, <b>capacity</b> and long-run growth can rise.</li><li>Evaluate: depends on whether savings are lent to firms and on confidence, on the interest rate, on the state of the economy (recession or boom), and on time.</li></ul></div>
  </div></details>

  <h2>B · Practice question with a model answer</h2>
  <details class="eq"><summary>Practice (not a past paper question) <span class="mark">8 marks</span> Explain the accelerator principle and why it makes investment unstable.</summary><div class="body">
    <div class="tip"><b class="h">Plan</b>State the principle. Give a numerical example showing investment falling while income rises. Link to instability. One evaluative point.</div>
    <div class="key"><span class="k"><i></i>K</span><span class="a"><i></i>A</span><span class="n"><i></i>N</span><span class="e"><i></i>E</span></div>
    <div class="ans">
    <p><span class="mk k" data-t="K">The accelerator principle states that the level of investment depends on the rate of change of national income, not its level. If the capital-output ratio is 2, investment in new capital equals twice the change in income.</span></p>
    <p><span class="mk a" data-t="A">For example, if national income rises by $10m in one year and by $15m the next, investment would be $20m and then $30m. If income then rises by only $10m, investment falls to $20m even though national income is still rising.</span> <span class="mk n" data-t="N">Because a small change in the growth of income causes a larger change in investment, and investment is an injection, aggregate demand can swing sharply, which may amplify booms and recessions.</span> <span class="mk e" data-t="E">The effect could be weaker if firms have spare capacity, if the capital-output ratio is not constant, or if confidence and interest rates matter more than current growth.</span></p></div>
  </div></details>

  <h2>C · Multiple choice questions (Paper 3)</h2>
  <p>Choose an answer, then read the reason. Source: paper code and question number.</p>
  <div id="qz2"></div>
'''
tips = '''
  <h2>Top tips</h2>
  <ul class="tips">
    <li><b>Define MPC as a change:</b> extra consumption divided by extra income. Do not confuse it with the average propensity to consume (C ÷ Y).</li>
    <li><b>Separate movements from shifts:</b> a change in income moves you along the consumption function; wealth, confidence, interest rates and taxes shift it.</li>
    <li><b>Remember MPC + MPS = 1</b> in a simple model, and use it to find the multiplier.</li>
    <li><b>For the accelerator, talk about the rate of change of income.</b> Investment can fall while income is still rising.</li>
    <li><b>Use the numbers.</b> A short example with income, change in income and investment gains application marks.</li>
    <li><b>Evaluate the accelerator</b> with spare capacity, constant capital-output ratio, confidence and interest rates.</li>
  </ul>
  <h2>Sentences you can use</h2>
  <div class="tw"><table class="t">
    <tr><th>You want to say</th><th>Use this sentence</th></tr>
    <tr><td>MPC</td><td>"The marginal propensity to consume is the proportion of an additional dollar of income that is spent."</td></tr>
    <tr><td>Shift</td><td>"A rise in wealth could shift the consumption function upwards, so consumption is higher at every level of income."</td></tr>
    <tr><td>Accelerator</td><td>"According to the accelerator principle, investment depends on the rate of change of national income, so a fall in the growth of income could cut investment."</td></tr>
    <tr><td>Saving</td><td>"A rise in saving is a withdrawal, so unless investment rises, national income may fall."</td></tr>
  </table></div>
  <h2>Command words</h2>
  <div class="tw"><table class="t">
    <tr><th>Command word</th><th>What it asks for</th></tr>
    <tr><td>Explain</td><td>Give reasons, with a clear chain of cause and effect.</td></tr>
    <tr><td>Consider</td><td>Look at the issue from several sides and judge how strong each is.</td></tr>
    <tr><td>Discuss / Assess</td><td>Arguments on both sides, then a judgement.</td></tr>
  </table></div>
  <h2>Flashcards</h2><div id="fc1"></div>
'''
js = HEAD + '''
/* ---------- Watch 1: consumption function ---------- */
const CXs = (y) => 70 + y * 0.85, CYs = (v) => 330 - v * 0.42;
function consDraw(s) {
  let o = SV.line(70, 330, 760, 330) + SV.line(70, 330, 70, 30) + SV.text(760, 370, "Disposable income Y", "sm", { "text-anchor": "end" }) + SV.text(76, 24, "Consumption C", "sm");
  [0, 200, 400, 600, 800].forEach((y) => { o += SV.text(CXs(y), 346, y, "sm", { "text-anchor": "middle" }); });
  if (s.l > 0) o += SV.line(CXs(0), CYs(0), CXs(700), CYs(700), "gr", { "stroke-dasharray": "5 5", ...op(s.l) }) + SV.text(CXs(700) - 4, CYs(700) + 18, "C = Y", "sm bd", { "text-anchor": "end", ...halo, ...op(s.l) });
  if (s.c > 0) o += SV.line(CXs(0), CYs(100), CXs(800), CYs(700), "c1", op(s.c)) + SV.text(CXs(800) - 4, CYs(700) - 10, "C = 100 + 0.75Y", "lbl bd t1", { "text-anchor": "end", ...halo, ...op(s.c) });
  if (s.a > 0) o += SV.circle(CXs(0), CYs(100), 6, "dot3", op(s.a)) + SV.text(CXs(0) + 12, CYs(100) - 8, "autonomous consumption = 100", "lbl bd t3", { ...halo, ...op(s.a) });
  if (s.b > 0) o += SV.line(CXs(400), CYs(400), CXs(400), 330, "gr", op(s.b)) + SV.circle(CXs(400), CYs(400), 7, "dot2", op(s.b)) + SV.text(CXs(400), 372, "Y = 400: C = Y, saving = 0", "lbl bd t2", { "text-anchor": "middle", ...op(s.b) });
  if (s.m > 0) o += SV.line(CXs(600), CYs(550), CXs(800), CYs(550), "c4", { "stroke-width": 3, ...op(s.m) }) + SV.line(CXs(800), CYs(550), CXs(800), CYs(700), "c4", { "stroke-width": 3, ...op(s.m) }) + SV.text(CXs(700), CYs(550) + 18, "ΔY = 200", "sm bd t4", { "text-anchor": "middle", ...halo, ...op(s.m) }) + SV.text(CXs(800) + 6, CYs(625), "ΔC = 150", "sm bd t4", { ...halo, ...op(s.m) });
  return o;
}
Lib.stepper($("#stC"), { w: 780, h: 385, label: "Consumption function C equals 100 plus 0.75 Y with the 45 degree line", base: { l: 0, c: 0, a: 0, b: 0, m: 0 }, draw: consDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>The 45° line.</b> Points on C = Y show consumption equal to income, so saving is zero.", s: { l: 1 } },
  { cap: "<b>The consumption function.</b> C = 100 + 0.75Y slopes up: more income, more consumption, but less than one-for-one.", s: { l: 1, c: 1 } },
  { cap: "<b>Autonomous consumption.</b> The intercept (100) is spending that does not depend on income: it is funded by savings or borrowing at low incomes.", s: { l: 1, c: 1, a: 1 } },
  { cap: "<b>Break-even income.</b> Where the function crosses the 45° line (Y = 400) households spend all their income. Below it they dissave; above it they save.", s: { l: 1, c: 1, a: 1, b: 1 } },
  { cap: "<b>The MPC.</b> The slope is the marginal propensity to consume: when income rises by 200 consumption rises by 150, so <b>MPC = 150 ÷ 200 = 0.75</b>, and MPS = 0.25.", s: { l: 1, c: 1, a: 0.4, b: 0.4, m: 1 } },
] });

/* ---------- Watch 2: accelerator ---------- */
const AY = [100, 110, 125, 135, 140, 140];
function accDraw(s) {
  let o = SV.line(60, 150, 740, 150) + SV.text(62, 24, "National income", "sm") + SV.line(60, 340, 740, 340) + SV.text(62, 196, "Investment = 2 × change in income", "sm");
  AY.forEach((y, i) => {
    const k = Math.max(0, Math.min(1, s.n - i)), x = 90 + i * 108; if (k <= 0) return;
    o += SV.rect(x, 150 - y * 0.8 * k, 56, y * 0.8 * k, "f1", op(k)) + SV.text(x + 28, 150 - y * 0.8 * k - 6, y, "sm bd", { "text-anchor": "middle", ...op(k) }) + SV.text(x + 28, 168, "year " + (i + 1), "sm", { "text-anchor": "middle", ...op(k) });
    if (i > 0) { const inv = 2 * (y - AY[i - 1]); o += SV.rect(x, 340 - inv * 3 * k, 56, inv * 3 * k, inv >= (i > 1 ? 2 * (AY[i - 1] - AY[i - 2]) : 0) ? "f3" : "f2", op(k)) + SV.text(x + 28, 340 - inv * 3 * k - 6, inv, "sm bd", { "text-anchor": "middle", ...op(k) }); }
  });
  if (s.f > 0) o += SV.text(560, 232, "income still rising, investment falls", "lbl bd t2", { "text-anchor": "middle", ...halo, ...op(s.f) });
  return o;
}
Lib.stepper($("#stA"), { w: 780, h: 365, label: "National income growing by smaller amounts and the investment that follows from the accelerator", base: { n: 0, f: 0 }, draw: accDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>Year 1.</b> National income is 100 and there is no change yet, so no net investment is needed.", s: { n: 1 } },
  { cap: "<b>Year 2.</b> Income rises by 10 to 110. With an accelerator of 2, firms need 20 of extra capital: <b>investment = 20</b>.", s: { n: 2 } },
  { cap: "<b>Year 3.</b> Income rises by 15 to 125, a faster rise, so <b>investment rises to 30</b>.", s: { n: 3 } },
  { cap: "<b>Year 4.</b> Income rises by only 10 to 135. Investment falls to <b>20</b> even though income is still rising.", s: { n: 4, f: 1 } },
  { cap: "<b>Years 5 and 6.</b> Growth slows to 5 and then 0, so investment falls to 10 and then 0. A slowdown in growth can cut investment (an injection) sharply.", s: { n: 6, f: 1 } },
] });

/* ---------- Lab 1 ---------- */
function labCons() {
  if (!$("#ca") || !$("#cc") || !$("#cy")) return;
  const a = +$("#ca").value, c = +$("#cc").value, y = +$("#cy").value, C = a + c * y, S = y - C, F = { x: (v) => 40 + v * 0.42, y: (v) => 270 - v * 0.34 };
  $("#c1r").textContent = "$" + Lib.fmtN(C, 0); $("#c2r").textContent = (S < 0 ? "−$" : "$") + Lib.fmtN(Math.abs(S), 0); $("#c3r").textContent = y ? Lib.fmtN(C / y, 2) : "–"; $("#c4r").textContent = Lib.fmtN(c, 2);
  $("#cv").textContent = S < -0.5 ? `At income $${y} consumption ($${Lib.fmtN(C, 0)}) is above income, so households dissave $${Lib.fmtN(-S, 0)} (APC is above 1).` : S > 0.5 ? `At income $${y} households consume $${Lib.fmtN(C, 0)} and save $${Lib.fmtN(S, 0)}. The APC (${Lib.fmtN(C / y, 2)}) is below 1, while the MPC stays at ${Lib.fmtN(c, 2)}.` : `At income $${y} consumption equals income: break-even, saving is zero.`;
  let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(396, 292, "Income Y", "sm", { "text-anchor": "end" }) + SV.text(46, 24, "C", "sm");
  o += SV.line(F.x(0), F.y(0), F.x(800), F.y(800), "gr", { "stroke-dasharray": "5 5" }) + SV.line(F.x(0), F.y(a), F.x(800), F.y(a + c * 800), "c1") + SV.line(F.x(y), F.y(C), F.x(y), 270, "gr") + SV.circle(F.x(y), F.y(C), 6, "dot1") + SV.text(F.x(800) - 4, F.y(800) + 16, "C = Y", "sm bd", { "text-anchor": "end" }) + SV.text(F.x(y), 288, y, "sm bd", { "text-anchor": "middle" });
  $("#labN").innerHTML = o;
}
Lib.slider($("#g1"), { id: "ca", label: "Autonomous consumption a ($): ", min: 0, max: 200, step: 20, value: 100, fmt: (v) => v, onInput: labCons });
Lib.slider($("#g2"), { id: "cc", label: "Marginal propensity to consume c: ", min: 0.5, max: 0.95, step: 0.05, value: 0.75, fmt: (v) => Lib.fmtN(v, 2), onInput: labCons });
Lib.slider($("#g3"), { id: "cy", label: "Disposable income Y ($): ", min: 0, max: 800, step: 50, value: 400, fmt: (v) => v, onInput: labCons });

/* ---------- Lab 2 ---------- */
function labAcc() {
  if (!$("#v2") || !$("#v3") || !$("#v4") || !$("#vv")) return;
  const g = [+$("#v2").value / 100, +$("#v3").value / 100, +$("#v4").value / 100], v = +$("#vv").value, y = [100]; g.forEach((r) => y.push(y[y.length - 1] * (1 + r)));
  const inv = [1, 2, 3].map((i) => v * (y[i] - y[i - 1]));
  $("#a1").textContent = "$" + Lib.fmtN(inv[0], 1); $("#a2").textContent = "$" + Lib.fmtN(inv[1], 1); $("#a3").textContent = "$" + Lib.fmtN(inv[2], 1);
  const fall = inv[2] < inv[1] - 0.05 && y[3] > y[2], fall2 = inv[1] < inv[0] - 0.05 && y[2] > y[1];
  $("#av").textContent = fall || fall2 ? `Income is still rising, but investment falls (${Lib.fmtN(inv[fall2 && !fall ? 0 : 1], 1)} to ${Lib.fmtN(inv[fall2 && !fall ? 1 : 2], 1)}) because the increase in income is smaller than the year before: the accelerator.` : "Investment follows the change in income. Lower the growth rate in a later year to see investment fall while income is still rising.";
  const base = 240;
  let o = SV.line(30, base, 400, base);
  y.forEach((val, i) => { const x = 50 + i * 85; o += SV.rect(x, base - val * 0.8, 28, val * 0.8, "f1") + SV.text(x + 14, base - val * 0.8 - 6, Lib.fmtN(val, 0), "sm bd", { "text-anchor": "middle" }) + SV.text(x + 14, base + 14, "Y" + (i + 1), "sm", { "text-anchor": "middle" }); if (i > 0) { const h = Math.max(0, inv[i - 1]) * 2; o += SV.rect(x + 32, base - h, 28, h, "f3") + SV.text(x + 46, base - h - 6, Lib.fmtN(inv[i - 1], 0), "sm bd t3", { "text-anchor": "middle" }); } });
  o += SV.text(210, 268, "blue: national income · green: investment", "sm", { "text-anchor": "middle" });
  $("#labO").innerHTML = o;
}
Lib.slider($("#g4"), { id: "v2", label: "Growth in year 2: ", min: -2, max: 20, step: 1, value: 10, fmt: (v) => v + "%", onInput: labAcc });
Lib.slider($("#g5"), { id: "v3", label: "Growth in year 3: ", min: -2, max: 20, step: 1, value: 14, fmt: (v) => v + "%", onInput: labAcc });
Lib.slider($("#g6"), { id: "v4", label: "Growth in year 4: ", min: -2, max: 20, step: 1, value: 8, fmt: (v) => v + "%", onInput: labAcc });
Lib.slider($("#g7"), { id: "vv", label: "Accelerator v (capital-output ratio): ", min: 1, max: 4, step: 0.5, value: 2, fmt: (v) => Lib.fmtN(v, 1), onInput: labAcc });

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), {
  prompt: "Does each change move households along the consumption function or shift it?",
  buckets: [{ label: "Movement along the function" }, { label: "Shift of the function" }],
  items: [
    { text: "A rise in disposable income from a pay rise", b: 0 }, { text: "A fall in disposable income after a tax rise", b: 0 },
    { text: "A rise in house prices (wealth)", b: 1 }, { text: "Households become more confident about jobs", b: 1 }, { text: "Credit becomes easier to get", b: 1 }, { text: "A fall in interest rates that discourages saving", b: 1 }, { text: "Fear of a recession raises saving at every income", b: 1 },
  ], done: "Income changes move you along the function; everything else shifts it.",
});
Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Consumption function", "The relationship between consumption and disposable income: C = a + cY"],
  ["Autonomous consumption", "Spending that does not depend on current income"],
  ["Marginal propensity to consume", "The share of an extra dollar of income that is spent"],
  ["Average propensity to consume", "Consumption divided by income"],
  ["Wealth effect", "A change in consumption caused by a change in the value of assets"],
  ["Accelerator principle", "Investment depends on the rate of change of national income"],
  ["Capital-output ratio", "The amount of capital needed to produce a unit of output (the accelerator)"],
], done: "Seven words for consumption and investment." });
Lib.order($("#o1"), { prompt: "Put the accelerator chain in order.", items: [
  "Demand and national income grow",
  "Firms need more capital to meet the extra output",
  "Investment rises by the accelerator times the change in income",
  "National income continues to rise, but by less",
  "The change in income falls, so the extra capital needed falls",
  "Investment falls, reducing aggregate demand even though income is still rising",
], done: "The key point is the rate of change of income." });
Lib.calc($("#c1"), { qs: [
  { q: "Consumption is C = 100 + 0.75Y. What is consumption when income is $600?", a: 550, sol: "100 + 0.75 × 600 = <b>$550</b>." },
  { q: "What is saving at income $600 ($)?", a: 50, sol: "600 − 550 = <b>$50</b>." },
  { q: "What is the average propensity to consume at income $600 (2 decimal places)?", a: 0.92, tol: 0.01, sol: "550 ÷ 600 = <b>0.92</b>." },
  { q: "Income rises from $1,000 to $1,200 and consumption rises from $800 to $900. What is the MPC?", a: 0.5, tol: 0.01, sol: "100 ÷ 200 = <b>0.5</b>." },
  { q: "The MPC is 0.8. What is the MPS?", a: 0.2, tol: 0.01, sol: "1 − 0.8 = <b>0.2</b>." },
  { q: "The accelerator is 3. National income rises by $20m. What is the investment ($m)?", a: 60, sol: "3 × 20 = <b>$60m</b>." },
  { q: "Income rises by $20m in one year and by $15m the next. With an accelerator of 3, by how much does investment fall ($m)?", a: 15, sol: "Investment falls from 60 to 45: a fall of <b>$15m</b>, although income is still rising." },
  { q: "A consumer's income is $1,000 and she spends 80% of it. What is her average propensity to consume?", a: 0.8, tol: 0.01, sol: "800 ÷ 1,000 = <b>0.8</b>." },
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "The marginal propensity to consume is:", opts: ["total consumption ÷ total income", "the change in consumption ÷ the change in income", "income − saving", "saving ÷ income"], a: 1, why: "It is about extra income, not total income." },
  { q: "An increase in house prices is most likely to:", opts: ["move households along the consumption function", "shift the consumption function upwards", "reduce the MPC to zero", "have no effect"], a: 1, why: "A wealth effect raises consumption at every income." },
  { q: "According to the accelerator principle, investment will fall when:", opts: ["income falls only", "the rate of growth of income falls", "income rises at a constant rate", "interest rates fall"], a: 1, why: "Investment depends on the rate of change of income." },
  { q: "If MPC = 0.9, then MPS =", opts: ["0.1", "0.9", "1.9", "0.09"], a: 0, why: "MPC + MPS = 1." },
  { q: "A rise in saving that is not matched by a rise in investment will probably:", opts: ["raise national income", "lower national income", "not affect national income", "raise the multiplier"], a: 1, why: "Withdrawals exceed injections, so income falls." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Consumption function", "C = a + cY: consumption depends on disposable income."],
  ["Autonomous consumption", "Spending that does not depend on current income (the intercept a)."],
  ["MPC", "Change in consumption ÷ change in income."],
  ["APC", "Consumption ÷ income."],
  ["MPS", "Change in saving ÷ change in income; MPC + MPS = 1."],
  ["Wealth effect", "A rise in asset values raises consumption."],
  ["Accelerator principle", "Investment depends on the rate of change of national income."],
  ["Investment determinants", "Interest rates, expected profit, confidence, spare capacity and technology."],
  ["Paradox of thrift", "If everyone saves more, income may fall and total saving may not rise."],
] });
''' + 'Lib.quiz($("#qz2"), { qs: [\n' + "".join(mc(*i) for i in [
  ("[Feb/March 2023 · 32 · Q21] What does the accelerator principle state?", ["Consumption is a function of the rate of change of income.", "Income is a function of the rate of change of investment.", "Investment is a function of the rate of change of income.", "Investment is a function of the rate of interest."], 2, "The accelerator links investment to the rate of change of income."),
  ("[May/June 2020 (not sat) · 31 · Q24] What does the accelerator principle explain?", ["how changes in consumption lead to changes in income", "how changes in income lead to changes in consumption", "how changes in income lead to changes in investment", "how changes in investment lead to changes in income"], 2, "The accelerator explains how changes in income lead to changes in investment. Option D is the multiplier."),
  ("[Feb/March 2025 · 32 · Q15] What does the accelerator principle explain?", ["how changes in consumption lead to changes in income", "how changes in income lead to changes in consumption", "how changes in income lead to changes in investment", "how changes in investment lead to changes in income"], 2, "Income changes lead to changes in investment through the accelerator."),
  ("[Oct/Nov 2020 · 31 · Q24] According to the accelerator theory, what would cause investment in an economy to be lower than in the previous year?", ["a lower marginal propensity to consume than in the previous year", "a lower marginal propensity to save than in the previous year", "a smaller fall in national income than occurred in the previous year", "a smaller rise in national income than occurred in the previous year"], 3, "A smaller rise in income means a smaller change in income, so investment falls."),
  ("[Oct/Nov 2023 · 33 · Q21] What, according to the accelerator principle, will cause the level of investment to fall?", ["a decrease in confidence", "a decrease in the rate of growth of national income", "an increase in the price of capital equipment", "an increase in the rate of interest"], 1, "The accelerator principle is about the rate of growth of national income. The other options are real influences, but not part of the accelerator."),
  ("[Oct/Nov 2023 · 31 · Q22] What is the basic assumption underlying the accelerator theory?", ["Investment depends on the level of business confidence.", "Investment depends on the level of savings.", "Investment depends on the rate of change in national income.", "Investment depends on the rate of change of interest rates."], 2, "Investment depends on the rate of change of national income."),
  ("[Oct/Nov 2024 · 31 · Q19] A consumer has an income of $1000 per week and spends 80% of this. After income rises to $1200 per week, consumption increases to $900 per week. Which statement is correct?", ["The average propensity to consume does not change.", "The initial average propensity to consume is 5.", "The marginal propensity to consume is 0.5.", "The marginal propensity to consume is 2."], 2, "The MPC is the change in consumption (900 − 800 = 100) divided by the change in income (200) = 0.5. The APC falls from 0.8 to 0.75."),
]) + '] });\n'
write("cf3", page(EY.format(3), "Consumption, Saving, Investment and the Accelerator",
  "The consumption function, the MPC and APC, what shifts consumption and saving, what determines investment, and the accelerator principle. Animated diagrams, labs, drills and the past paper questions.",
  learn=learn, watch=watch, explore=explore, practise=practise, real=real, exam=exam, tips=tips), js,
  "Consumption, Saving, Investment and the Accelerator", "consumption-saving-investment-accelerator")
