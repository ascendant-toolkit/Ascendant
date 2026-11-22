"""Resource: two worked Paper 4 essays for 9.1 (inflationary gap and monetary policy, 13 marks; multiplier and fiscal policy, 20 marks).
Run: python3 tools/artifact-kit/mk_pe91.py"""
import pathlib, subprocess
from syl import HEAD, jq
from splitter import KEYL
D = pathlib.Path(__file__).parent

CSS = '''
.lv3{border-left:5px solid var(--good)} .lv2{border-left:5px solid var(--warn)} .lv1{border-left:5px solid var(--bad)}
.gl{border:1px solid var(--line);border-radius:12px;padding:12px 16px;background:var(--surface);margin-bottom:12px}
.gl h4{margin:0 0 6px;font:700 .8rem var(--sans);letter-spacing:.06em;text-transform:uppercase}
.gl.lv1 h4{color:var(--bad)} .gl.lv2 h4{color:var(--warn)} .gl.lv3 h4{color:var(--good)}
.dgm{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:6px;max-width:680px;margin:12px auto}
.dgm svg{display:block;width:100%;height:auto}
.dgm .cap{font-size:.84rem;color:var(--muted);padding:2px 10px 8px}
.model p{margin:0 0 .85em}
.ck label{display:flex;gap:8px;align-items:flex-start;margin:6px 0;font-size:.95rem}
.ck .res{margin-top:10px;padding:10px 14px;border-radius:10px;background:var(--soft);font-weight:600}
.qbox{padding:14px 16px;border:2px solid var(--accent);border-radius:12px;background:var(--surface);font-size:1.05rem;margin:10px 0}
'''

body = '''
<div class="wrap">
<header class="top">
  <div class="eyebrow">A Level Economics · 9708 · Syllabus 9.1 · Paper 4 worked essays</div>
  <h1>Two Paper 4 Essays on 9.1, Marked in Depth</h1>
  <p class="lead">A 13-mark question on monetary policy and the inflationary gap (May/June 2020) and a 20-mark question on the multiplier and fiscal policy (May/June 2026). Each comes with a plan, diagrams, a colour-coded model answer and a line-by-line account of where the marks come from.</p>
</header>

<nav class="tablist" role="tablist" aria-label="Sections">
  <button role="tab" data-p="start">The two questions</button>
  <button role="tab" data-p="q1">Question 1 · 13 marks</button>
  <button role="tab" data-p="q2">Question 2 · 20 marks</button>
  <button role="tab" data-p="prac">Practise</button>
  <button role="tab" data-p="tips">Tips &amp; keywords</button>
</nav>

<section id="start" role="tabpanel">
  <div class="card big"><h3>This resource in four sentences</h3>
  <p>Both questions test the same 9.1 core: <b>aggregate expenditure, the full employment level of income, the multiplier and the gaps</b>, but they ask you to do different things with it. Question 1 asks <b>how far you agree</b> that one policy (monetary) is the <b>most effective</b> way to close an <b>inflationary gap</b>, so you must compare it with fiscal and supply-side policy. Question 2 asks you to <b>evaluate a statement</b> about the <b>multiplier</b> and <b>expansionary fiscal policy</b> with a <b>negative output gap</b>, so you must show why it is true in theory and then test it. In both, marks come from <b>developed chains of reasoning applied to the question</b>, a <b>correct diagram</b> and <b>explained evaluation</b>.</p></div>

  <h2>How the two questions are marked</h2>
  <div class="tw"><table class="t">
    <tr><th></th><th>Question 1 · 13 marks</th><th>Question 2 · 20 marks</th></tr>
    <tr><td><b>Paper</b></td><td>9708/41, May/June 2020, Q6(b)</td><td>9708/41, May/June 2026, Q4</td></tr>
    <tr><td><b>Command</b></td><td>"How far would you agree that…"</td><td>"Evaluate this statement."</td></tr>
    <tr><td><b>Mark scheme format</b></td><td>Four levels: L1 1–4, L2 5–6, L3 7–8, L4 9–13. The 2020 papers were never sat because of the pandemic; the scheme was published to support teaching.</td><td>Two scales: <b>14 marks</b> for knowledge, application and analysis (Table A: L1 1–5, L2 6–10, L3 11–14) and <b>6 marks</b> for evaluation (Table B: E1 1–3, E2 4–6).</td></tr>
    <tr><td><b>What the top level needs</b></td><td>A detailed explanation of why monetary policy might solve the problems of an inflationary gap, at least two monetary tools, alternatives (fiscal and supply side) explained and discussed, and a conclusion on relative effectiveness.</td><td>The key concepts (negative output gap, full employment, injection, multiplier and its formula), the process of multiple rounds, induced spending, a diagram with more than one shift of AD, then evaluation points that are developed and a justified conclusion.</td></tr>
    <tr><td><b>Time</b></td><td>About 22 to 25 minutes</td><td>About 35 to 40 minutes</td></tr>
    <tr><td><b>Depth of each skill</b></td><td>Knowledge, application, analysis and evaluation each need to appear, but at modest depth: two tools and two alternatives.</td><td>Each skill is marked separately and deeper: three developed analysis chains, applied, with a diagram, and evaluation worth 6 marks of its own.</td></tr>
  </table></div>
  <div class="tip"><b class="h">Same skills, different weight</b>On the 13-mark question one well-developed evaluation paragraph and a conclusion can reach the top level. On the 20-mark question evaluation is <b>30% of the marks</b>, so it has to appear in several places and be explained, not just listed.</div>

  <h2>The colour key used in the model answers</h2>
  <div class="key"><span class="k"><i></i>Knowledge (K)</span><span class="a"><i></i>Application (A)</span><span class="n"><i></i>Analysis (N)</span><span class="e"><i></i>Evaluation (E)</span></div>
  <ul>
    <li><b>Knowledge (K):</b> accurate definitions and concepts, in the language of the syllabus.</li>
    <li><b>Application (A):</b> the figures, examples and context that make the answer about <b>this</b> question and not the topic in general. Application is not a separate mark scale. It is rewarded inside the 14 marks.</li>
    <li><b>Analysis (N):</b> a chain of cause and effect with each link explained, using a diagram where it helps.</li>
    <li><b>Evaluation (E):</b> a judgement on how far, when and for whom the argument holds. A named factor earns little. An explained one (lever, because, so what) earns more.</li>
  </ul>
  <p class="note">Marks in the "how this scores" boxes are illustrative estimates of how a marker could place each answer. Markers give a best-fit level, not a mark per sentence.</p>
</section>

<section id="q1" role="tabpanel" hidden>
  <div class="qbox"><b>Question 1 · 13 marks · 9708/41 May/June 2020 Q6(b).</b> How far would you agree that the use of monetary policy is the most effective way to solve the problem of an inflationary gap?</div>

  <h2>1 · Decode the question</h2>
  <div class="tw"><table class="t">
    <tr><th>Phrase</th><th>What it asks you to do</th></tr>
    <tr><td><b>How far would you agree</b></td><td>Take a position on a scale. A judgement such as "largely, in the short run, for a small gap" is stronger than yes or no.</td></tr>
    <tr><td><b>monetary policy</b></td><td>The central bank's use of interest rates, the money supply and credit. A fiscal-only answer loses most of the marks. The scheme wants <b>at least two types</b> of monetary policy.</td></tr>
    <tr><td><b>the most effective</b></td><td>Comparative: you need <b>alternatives</b> (fiscal, supply side) and a view on which works best.</td></tr>
    <tr><td><b>the problem of an inflationary gap</b></td><td>Define it: AE at full employment is above potential output, so excess demand pulls up the price level. Use a diagram to show it.</td></tr>
  </table></div>

  <h2>2 · A five-minute plan</h2>
  <div class="tw"><table class="t">
    <tr><th>Paragraph</th><th>Content</th><th>Marks it targets</th></tr>
    <tr><td>1 · Open</td><td>Define inflationary gap and monetary policy; take a line</td><td>Knowledge, start of judgement</td></tr>
    <tr><td>2 · Tool one</td><td>Interest rates through the Keynesian diagram, with figures. Evaluate: interest elasticity and lags</td><td>Analysis, application, diagram, evaluation</td></tr>
    <tr><td>3 · Tool two</td><td>Money supply or credit control. Evaluate</td><td>Two types of monetary policy (a level requirement)</td></tr>
    <tr><td>4 · Alternative one</td><td>Fiscal policy: why it might be more direct or less effective</td><td>Alternatives explained and discussed</td></tr>
    <tr><td>5 · Alternative two</td><td>Supply-side policy: raise potential output, but slowly</td><td>Alternatives, compare</td></tr>
    <tr><td>6 · Judgement</td><td>How far you agree and what it depends on: size and cause of the gap, time scale</td><td>Conclusion on relative effectiveness</td></tr>
  </table></div>

  <h2>3 · The diagram</h2>
  <figure class="dgm"><div id="dg1"></div><div class="cap">Keynesian 45° diagram. AE1 = 260 + 0.6Y cuts the 45° line at Y = 650, above full employment income YF = 500. At YF, AE1 is 560, which is 60 above output: the inflationary gap. A rise in interest rates lowers C, I and net exports, shifting AE down by 60 to AE2 = 200 + 0.6Y. With a multiplier of 2.5, income falls by 150 and equilibrium returns to YF.</div></figure>
  <p>Draw it in 90 seconds: axes labelled, the 45° line, AE1 above the 45° line at YF, the gap marked vertically at YF, then AE2 and the new equilibrium. The same numbers appear in the answer, so the diagram is used and not decorative.</p>

  <h2>4 · Model answer</h2>
  <div class="key"><span class="k"><i></i>Knowledge (K)</span><span class="a"><i></i>Application (A)</span><span class="n"><i></i>Analysis (N)</span><span class="e"><i></i>Evaluation (E)</span></div>
  <div class="ans model">
  <p><span class="mk k" data-t="K">An inflationary gap exists when aggregate expenditure at the full employment level of income is greater than potential output, so real output cannot rise to meet demand and the excess demand pulls up the price level. Monetary policy is the use of interest rates, the money supply and credit by the central bank to influence aggregate demand.</span> <span class="mk e" data-t="E">I agree to a considerable extent that monetary policy is the most effective of the main options in the short run, because it can be changed quickly and acts on several parts of aggregate demand, but it is not the most effective in every case: it works with a lag and may not be enough for a large gap or for inflation caused by costs.</span></p>
  <p><span class="mk n" data-t="N">In the diagram the economy is in equilibrium at 650, above full employment income of 500, because AE1 is 60 above the 45° line at YF. A rise in the central bank's interest rate raises the cost of borrowing, so firms may cancel investment projects financed by loans and households with mortgages or credit cards have less to spend. The higher reward for saving may reduce consumption, and higher rates may attract foreign funds, raising the exchange rate and making exports dearer and imports cheaper, so net exports fall.</span> <span class="mk a" data-t="A">The Bank of England raised Bank Rate from 0.1% in late 2021 to 5.25% by August 2023 as UK inflation rose above 11% in 2022.</span> <span class="mk n" data-t="N">As C, I and (X − M) fall, AE shifts down to AE2, and because the multiplier is 2.5, a fall in autonomous spending of 60 lowers income by 150, back to full employment, which removes the excess demand.</span> <span class="mk e" data-t="E">However, this only works if spending is sensitive to interest rates. If firms are confident about profits, or many households hold fixed-rate mortgages, investment and consumption may fall by less than 60, so some of the gap remains. Interest rate changes also take around a year or more to work fully, so the gap could close for other reasons first and the policy could push the economy into a deflationary gap.</span></p>
  <p><span class="mk n" data-t="N">A second type of monetary policy is a reduction in the money supply, for example the central bank selling government bonds or requiring banks to hold more reserves. This reduces banks' ability to lend, so credit becomes scarcer and dearer, and spending on items bought on credit, such as cars and houses, is likely to fall.</span> <span class="mk e" data-t="E">However, banks may find other sources of funds, and the effect on spending is less predictable than a change in the policy rate, so central banks mainly use the interest rate.</span></p>
  <p><span class="mk n" data-t="N">Fiscal policy is the main alternative. A cut in government spending of 60, or a tax rise that cuts consumption by 60, shifts AE down straight away, because government spending is itself a component of AE.</span> <span class="mk e" data-t="E">This makes fiscal policy more direct than monetary policy, whose effect depends on how households and firms respond. However, spending cuts and tax rises are politically unpopular and take time to pass, they could reduce public services for the poor, and the multiplier may make the fall in income larger than the government intended. An independent central bank can change rates monthly, which makes monetary policy more flexible.</span></p>
  <p><span class="mk n" data-t="N">Supply-side policy, such as investment in training and infrastructure, raises potential output so YF moves to the right and the gap is closed by raising the supply of output rather than cutting demand.</span> <span class="mk e" data-t="E">This avoids lower growth and jobs, but it takes years to work, and so it is unlikely to deal with a gap that already exists.</span></p>
  <p><span class="mk e" data-t="E">Overall I agree to a limited but considerable extent. Monetary policy is likely to be the most effective single tool for a small inflationary gap in the short run, because it can be adjusted quickly by an independent central bank and acts on consumption, investment and net exports at once. It is less likely to be the most effective when the gap is large, when inflation is caused by cost-push factors such as energy prices, which higher rates do not reduce directly, or when spending is not sensitive to interest rates. The most effective response is therefore likely to combine monetary policy with fiscal and supply-side measures, and which is most effective depends on the size and cause of the gap and how quickly it must be closed.</span></p>
  </div>

  <h2>5 · Where the marks come from</h2>
  <div class="tw"><table class="t">
    <tr><th>What the mark scheme asks for (Level 4, 9 to 13)</th><th>Where the answer does it</th></tr>
    <tr><td>A detailed explanation of why monetary policy might solve the problems of an inflationary gap</td><td>Paragraph 2: a five-step chain from a higher interest rate to lower C, I and net exports, to AE2 and a lower income, with figures from the diagram</td></tr>
    <tr><td>At least two types of monetary policy considered</td><td>Interest rates (paragraph 2) and money supply and credit (paragraph 3)</td></tr>
    <tr><td>Alternative measures explained and discussed</td><td>Fiscal policy (paragraph 4) and supply-side policy (paragraph 5), each with a mechanism and a limit</td></tr>
    <tr><td>A clear diagram and the problems of an inflationary gap identified</td><td>The labelled 45° diagram, and the definition in paragraph 1</td></tr>
    <tr><td>A conclusion considering relative effectiveness</td><td>The final paragraph: a degree ("considerable but limited") and conditions (size and cause of the gap, time scale)</td></tr>
  </table></div>
  <div class="tip"><b class="h">How this scores</b>Likely 11 to 13 of 13, the upper part of Level 4. All four requirements appear, each with a mechanism. A mark above 11 needs the evaluation to be explained and the conclusion to compare the options, as here. Cost-push inflation is the strongest single evaluation point, because it questions whether the demand-side model applies at all.</div>

  <h2>6 · The same paragraph at different levels</h2>
  <p>The interest rate paragraph, written four ways. The sums are rough marks for this part of the answer.</p>
  <div class="gl lv1"><h4>Level 1 · about 3 of 13</h4><p>Monetary policy is when the government changes interest rates. If interest rates go up people borrow less and spend less so inflation goes down.</p><p class="note">Descriptive. It confuses the central bank with the government, has no mechanism, no diagram, and does not mention the gap.</p></div>
  <div class="gl lv2"><h4>Level 2 · about 6 of 13</h4><p>An inflationary gap happens when AE is above full employment. The central bank can raise interest rates, which raises the cost of borrowing, so investment and consumption fall, aggregate demand falls and the inflationary gap gets smaller. Fiscal policy could also be used.</p><p class="note">Correct, with a brief chain. But there is only one tool, no figures or example, the alternative is mentioned with no explanation, and there is no judgement.</p></div>
  <div class="gl lv3"><h4>Level 3 · about 8 of 13</h4><p>The central bank can raise interest rates, which raises the cost of borrowing, so investment falls and AE shifts down, reducing the gap. A second tool is to cut the money supply. Fiscal policy could reduce the gap by cutting government spending, but it takes time. Monetary policy is probably the most effective because it works quickly.</p><p class="note">Two tools and an alternative, with a conclusion. But the chain stays at two steps, nothing is applied, the claim that it "works quickly" is not explained, and the alternative is not discussed.</p></div>
  <div class="gl lv4"><h4>Level 4 · about 12 of 13</h4><p>The model answer above: a labelled diagram used with figures, a chain that includes the exchange rate and the multiplier, a real example, explained limits on each policy and a conclusion that depends on the size and cause of the gap.</p></div>
  <style>.gl.lv4{border-left:5px solid var(--accent)} .gl.lv4 h4{color:var(--accent)}</style>

  <h2>7 · Check your own answer</h2>
  <p>Tick what your answer includes. The result is a rough guide to the level.</p>
  <div class="card ck" id="ck1"></div>
</section>

<section id="q2" role="tabpanel" hidden>
  <div class="qbox"><b>Question 2 · 20 marks · 9708/41 May/June 2026 Q4.</b> Due to the multiplier process, governments conducting an expansionary fiscal policy do not need to increase spending by the full amount of the negative output gap to bring the output of the economy to its full employment level. <b>Evaluate this statement.</b></div>

  <h2>1 · Decode the question</h2>
  <div class="tw"><table class="t">
    <tr><th>Phrase</th><th>What it asks you to do</th></tr>
    <tr><td><b>Evaluate this statement</b></td><td>The question gives you a claim to test. Decide how far it is true and under what conditions. 6 of the 20 marks are for evaluation, and the conclusion must answer the statement.</td></tr>
    <tr><td><b>Due to the multiplier process</b></td><td>The claim rests on the multiplier. You must explain the process: rounds of spending, leakages, induced consumption and investment.</td></tr>
    <tr><td><b>expansionary fiscal policy</b></td><td>Define it: higher government spending and/or lower taxes, financed by a budget deficit. Not monetary policy.</td></tr>
    <tr><td><b>do not need to increase spending by the full amount of the negative output gap</b></td><td>The core claim: required spending = output gap ÷ multiplier, which is less than the gap if the multiplier is above 1. Test it with numbers.</td></tr>
    <tr><td><b>negative output gap, full employment</b></td><td>Define both. Actual output below potential. All resources fully used at the target.</td></tr>
  </table></div>

  <h2>2 · What the mark scheme says (indicative content)</h2>
  <div class="grid2">
    <div class="card"><h3>Knowledge and analysis (14 marks)</h3><ul>
      <li>Negative output gap: actual output below potential output.</li>
      <li>Full employment: all resources fully and efficiently used, no cyclical unemployment.</li>
      <li>AD as a determinant of output; expansionary fiscal policy as lower taxes and higher G, creating a deficit.</li>
      <li>G as an injection and a component of AD.</li>
      <li>Multiplier = 1 ÷ (1 − MPC) = 1 ÷ MPW = 1 ÷ (MPS + MTR + MPM) = change in income ÷ change in injection.</li>
      <li>Multiple rounds of spending; induced consumption and investment.</li>
      <li>Examples of what the government can spend on and the rounds it creates.</li>
      <li><b>A diagram with more than one shift of AD</b> (or one shift with a written explanation that the rise is more than the government spent).</li>
    </ul></div>
    <div class="card"><h3>Evaluation (6 marks)</h3><ul>
      <li>The multiplier may be uncertain, so spending could be <b>insufficient</b>.</li>
      <li>Uncertainty could also cause <b>overshooting</b> and higher inflation.</li>
      <li>G is a small part of AD, so the impact could be small even with the multiplier.</li>
      <li><b>Crowding out</b>.</li>
      <li><b>National debt</b>: debt servicing, lower investor confidence, debt crises.</li>
      <li>A <b>large MPM</b> or a <b>small MPC</b> gives a small multiplier.</li>
    </ul></div>
  </div>

  <h2>3 · A plan for 20 marks</h2>
  <div class="tw"><table class="t">
    <tr><th>Paragraph</th><th>Content</th><th>Marks it targets</th></tr>
    <tr><td>1 · Define and take a line</td><td>Negative output gap, full employment, expansionary fiscal policy, multiplier. A thesis: true in theory, uncertain in practice</td><td>Knowledge, plus the start of the judgement</td></tr>
    <tr><td>2 · The multiplier process, with numbers</td><td>Gap 100, k 2.5, G needed 40. Rounds of spending, induced consumption and investment. A real type of spending</td><td>Analysis and application</td></tr>
    <tr><td>3 · The diagram explained</td><td>AD1 to AD2 to AD3 on an AD/AS diagram; the horizontal distance is more than the spending</td><td>Diagram, analysis</td></tr>
    <tr><td>4 · Evaluate: the size of the multiplier</td><td>High MPM, high MPS, high taxes: smaller k, so G must be higher. Undershoot and overshoot</td><td>E (explained, with figures)</td></tr>
    <tr><td>5 · Evaluate: crowding out and debt</td><td>Borrowing raises interest rates; debt servicing; investor confidence</td><td>E</td></tr>
    <tr><td>6 · Evaluate: scale and timing</td><td>G as a share of AD, lags, measuring the output gap</td><td>E</td></tr>
    <tr><td>7 · Judgement</td><td>True in principle. In practice depends on the multiplier. Which factor matters most and why</td><td>E2 conclusion</td></tr>
  </table></div>

  <h2>4 · The diagrams</h2>
  <p>The mark scheme asks for <b>more than one shift of AD</b> on an AD/AS diagram. A second diagram, the 45° cross, shows the same numbers and is not required in the exam. One diagram is enough, drawn well and referred to in the text.</p>
  <figure class="dgm"><div id="dg2"></div><div class="cap">Diagram 1 (AD/AS, Keynesian AS). AD1 meets AS at Y1 = 400, a negative output gap of 100 below YF = 500. A rise in G of 40 shifts AD to AD2 (output 440). The multiplier then shifts it again, to AD3, where output reaches 500. The shift from AD1 to AD3 (100) is much bigger than the spending (40).</div></figure>
    <figure class="dgm"><div id="dg3"></div><div class="cap">Diagram 2 (45° cross). AE1 = 160 + 0.6Y cuts the 45° line at 400. At YF = 500, AE1 is 460, so the vertical gap is 40. A rise in G of 40 shifts AE up to AE2 = 200 + 0.6Y, and equilibrium rises by 100 to 500.</div></figure>

  <h2>5 · Model answer</h2>
  <div class="key"><span class="k"><i></i>Knowledge (K)</span><span class="a"><i></i>Application (A)</span><span class="n"><i></i>Analysis (N)</span><span class="e"><i></i>Evaluation (E)</span></div>
  <div class="ans model">
  <p><span class="mk k" data-t="K">A negative output gap exists when actual output is below potential output, so some resources, including labour, are unemployed and there is cyclical unemployment. Full employment is the level of output at which all available resources are fully and efficiently used. Expansionary fiscal policy is an increase in government spending (G) and/or a cut in taxes, financed by a budget deficit, to raise aggregate demand. The multiplier is the ratio of the final change in national income to the initial change in an injection.</span> <span class="mk e" data-t="E">The statement is correct in theory, because every dollar of government spending is re-spent in later rounds, but in practice a government cannot be sure how large the multiplier is or how big the gap is, so it may spend too little or too much.</span></p>
  <p><span class="mk n" data-t="N">Suppose potential output is $500bn and actual output is $400bn, a negative output gap of $100bn. Government spending is an injection into the circular flow and a component of aggregate demand. If the government spends $40bn on building roads and railways, that spending becomes income for construction firms and their workers.</span> <span class="mk a" data-t="A">The workers spend part of their wages in shops and restaurants, which pay their own staff and suppliers, so the spending passes through several rounds.</span> <span class="mk n" data-t="N">With an MPS of 0.1, a marginal rate of tax of 0.2 and an MPM of 0.1, the marginal propensity to withdraw is 0.4, so the multiplier is 1 ÷ 0.4 = 2.5. Of the first $40bn, $24bn is spent in the second round, $14.4bn in the third, and so on, so national income rises by 40 × 2.5 = $100bn. As incomes rise, households also increase induced consumption, and firms with spare capacity may invest in new equipment to meet growing demand, which adds to later rounds. The government therefore needs to spend only the output gap ÷ the multiplier, which is $40bn or 40% of the gap.</span></p>
  <p><span class="mk n" data-t="N">In the diagram, AD1 meets the Keynesian AS curve at $400bn. The initial rise in G of $40bn shifts AD to AD2. The extra income is re-spent, so AD shifts again to AD3, where output reaches the full employment level of $500bn. The total shift of $100bn is much larger than the $40bn the government spent, which supports the statement.</span></p>
  <p><span class="mk n" data-t="N">However, the multiplier is not known with certainty.</span> <span class="mk e" data-t="E">If MPM is large, as in a small, open economy that imports much of what it consumes, or if MPC is small because households in a recession save more out of fear of unemployment, the multiplier may be much lower. With an MPS of 0.2, a tax rate of 0.2 and an MPM of 0.4, the multiplier falls to 1 ÷ 0.8 = 1.25 and the government would need to spend $80bn, four-fifths of the gap, so the statement would be true but hardly useful. If the government spends only the $40bn it estimated, output would remain well below full employment, unemployment would persist and the policy would be judged to have failed. If the multiplier were larger than expected, the extra spending could overshoot full employment, so that demand outruns potential output and inflation rises.</span></p>
  <p><span class="mk n" data-t="N">A second problem is crowding out. Expansionary fiscal policy creates a larger deficit, and the government borrows by selling bonds.</span> <span class="mk e" data-t="E">This raises the demand for loanable funds and may push up interest rates, which reduces private investment, so the net multiplier is smaller and the government would need to spend more than the formula suggests. However, in a deep recession, with spare capacity and a central bank that keeps interest rates low, crowding out is likely to be small. A higher deficit adds to national debt and the cost of servicing it, which may reduce investor confidence and, if debt is already high, raise the risk of a debt crisis in which the government has to cut spending later.</span></p>
  <p><span class="mk e" data-t="E">The size of the effect also depends on scale and timing. Government spending is only part of aggregate demand, and if consumer and business confidence are falling, an increase of $40bn could be offset by falling private spending, so the economy still does not reach full employment. Spending on infrastructure takes time to plan, so it may arrive after the economy has already started to recover, and potential output is estimated and may be wrong, so the gap itself is uncertain.</span></p>
  <p><span class="mk e" data-t="E">Overall, the statement is correct as a matter of economic theory: the spending required is the output gap divided by the multiplier, which is less than the gap whenever the multiplier is greater than one. But the statement is likely to hold in practice only when the multiplier is large, there is real spare capacity and crowding out is weak, as in a closed, low-import economy in a deep recession. For a small, open economy with a high MPM and high debt, the required increase may be close to the full gap. Because governments cannot measure the multiplier or the gap precisely, the most important factor is the size of the multiplier, as every other limitation works by making it smaller. The statement is therefore best seen as a rule of thumb that gives a minimum required spending, and not as a reason to spend less.</span></p>
  </div>

  <h2>6 · Where the marks come from</h2>
  <div class="tw"><table class="t">
    <tr><th>Paragraph</th><th>Scale</th><th>What earns the marks</th><th>Indicative content matched</th></tr>
    <tr><td>1</td><td>K, E (thesis)</td><td>Four definitions, then a line that says true in theory and uncertain in practice</td><td>Negative output gap, full employment, fiscal policy, multiplier</td></tr>
    <tr><td>2</td><td>N, A, K</td><td>A numbered chain: injection, income, spending in later rounds, formula and calculation, induced consumption and investment, then required G = gap ÷ multiplier</td><td>G as injection and AD component, formula, multiple rounds, induced spending, examples</td></tr>
    <tr><td>3</td><td>N (diagram)</td><td>AD1, AD2, AD3 explained, with the key comparison: 100 versus 40</td><td>Diagram with more than one shift</td></tr>
    <tr><td>4</td><td>E</td><td>Both directions: too small a multiplier (undershoot) and too large (overshoot). Figures show the effect (1.25 means $80bn)</td><td>MPM large or MPC small; uncertainty causing insufficient spending or overshooting</td></tr>
    <tr><td>5</td><td>E</td><td>Crowding out with its mechanism, a counter-argument, then debt</td><td>Crowding out; national debt</td></tr>
    <tr><td>6</td><td>E</td><td>G is a small part of AD and the effect may be offset; timing; output gap measurement</td><td>G is a small part of AD</td></tr>
    <tr><td>7</td><td>E (judgement)</td><td>Answers "evaluate this statement": true in theory, conditions for practice, ranks the factors</td><td>Needed for E2 (4 to 6)</td></tr>
  </table></div>
  <div class="tip"><b class="h">How this scores</b>Knowledge, application and analysis, 12 to 14 of 14 (Level 3): all the indicative concepts, a correct diagram with more than one shift, three developed chains, and figures and examples throughout. Evaluation, 5 to 6 of 6 (E2): four explained points and a conclusion that answers the statement and ranks the factors. Total about 17 to 20 of 20. The same ideas with no numbers, no diagram and evaluation as a list ("crowding out and debt") are more likely to score about 8 to 10 for the 14 and 2 for the 6.</div>

  <h2>7 · How each level is earned on this question</h2>
  <h3>Knowledge, application and analysis (Table A, 14 marks)</h3>
  <div class="gl lv1"><h4>Level 1 · about 3 of 14</h4><p>The multiplier means that when the government spends money it has a bigger effect on the economy. More people have jobs and they spend their money. So the statement is true.</p><p class="note">The idea is right but it is descriptive. There are no definitions, no formula, no gap, no numbers, no diagram and the conclusion is asserted.</p></div>
  <div class="gl lv2"><h4>Level 2 · about 8 of 14</h4><p>A negative output gap is when actual output is less than potential output. The multiplier is 1 ÷ (1 − MPC). If MPC is 0.6 the multiplier is 2.5, so if the gap is $100bn the government only needs to spend $40bn. Government spending is an injection into the circular flow. This shows that the statement is true.</p><p class="note">Correct, with a calculation. But the process of spending in rounds is not explained, there is no induced spending, no diagram and no application. It could be about any country. It also uses the closed-economy formula without noting leakages.</p></div>
  <div class="gl lv3"><h4>Level 3 · about 13 of 14</h4><p>Paragraphs 1 to 3 of the model answer: definitions, a chain in which spending becomes income and passes through rounds, the open-economy multiplier from the marginal propensity to withdraw, induced consumption and investment, the required G calculated, and an AD/AS diagram with AD1, AD2 and AD3 explained.</p></div>
  <h3>Evaluation (Table B, 6 marks)</h3>
  <div class="gl lv1"><h4>E1 · about 2 of 6</h4><p>However, there could be crowding out and national debt, so the statement might not always be true. It also depends on the size of the multiplier.</p><p class="note">Two factors named, with no mechanism and no effect on the statement. This is a list, so it stays in E1.</p></div>
  <div class="gl lv3"><h4>E2 · about 6 of 6</h4><p>Paragraphs 4 to 7 of the model answer. Each point has a <b>lever</b> (a high MPM), a <b>because</b> (more of each dollar is spent abroad) and a <b>so what</b> (the multiplier falls to 1.25, so G must be $80bn, and spending only $40bn leaves unemployment). There is a counter-argument (crowding out is small in a deep recession) and a final judgement that ranks the factors.</p></div>

  <h2>8 · What would limit the marks</h2>
  <div class="tw"><table class="t">
    <tr><th>Fault</th><th>Why it costs marks</th><th>Fix</th></tr>
    <tr><td>No diagram, or one with a single AD shift and no explanation</td><td>The scheme asks for more than one shift of AD or an explanation that the increase is more than the spending</td><td>Draw AD1, AD2, AD3 and state that 100 is more than 40</td></tr>
    <tr><td>Calculating the multiplier but not the spending needed</td><td>The statement is about how much the government <b>needs to spend</b></td><td>Required G = output gap ÷ multiplier</td></tr>
    <tr><td>Treating the statement as simply true and then listing problems</td><td>Evaluation must question the statement, not just add disadvantages</td><td>Say how each problem makes the statement less true (small multiplier means required G is nearer the full gap)</td></tr>
    <tr><td>Confusing the output gap with the spending needed</td><td>The $100bn gap is in output. The injection is $40bn.</td><td>Keep the two numbers apart, as in paragraph 2</td></tr>
    <tr><td>Using a closed economy formula only</td><td>Leakages of tax and imports reduce the multiplier</td><td>Use 1 ÷ (MPS + MRT + MPM) and say why</td></tr>
    <tr><td>Writing about monetary policy</td><td>The question says fiscal policy</td><td>One line saying that monetary policy is not the focus is enough</td></tr>
  </table></div>

  <h2>9 · Check your own answer</h2>
  <p>Tick what your answer includes. The result is a rough guide to the level.</p>
  <div class="card ck" id="ck2"></div>
</section>

<section id="prac" role="tabpanel" hidden>
  <h2>1 · Which skill is it?</h2>
  <p>Sentences from the two model answers. Decide whether each one is knowledge, application, analysis or evaluation.</p>
  <div id="cl1" class="card"></div>
  <h2>2 · Put the Question 2 analysis chain in order</h2>
  <div id="o1" class="card"></div>
  <h2>3 · Calculations behind the model answers</h2>
  <div id="c1"></div>
  <h2>4 · Multiple choice</h2>
  <div id="qz1"></div>
  <h2>5 · Write your own</h2>
  <div class="grid2">
    <div class="card"><h3>Try question 1 again</h3><p>Plan it in five minutes using the table in the Question 1 tab. Then write only the paragraph on <b>fiscal policy</b>: mechanism, a limit, and a comparison with monetary policy. Mark it against the Level 2 to Level 4 paragraphs.</p></div>
    <div class="card"><h3>Try a variation on question 2</h3><p>"Evaluate the view that a government should increase spending by more than the output gap in a recession." What changes in the argument? (Hint: leakages and confidence make the multiplier small, so the case rests on whether it is less than one.)</p></div>
  </div>
</section>

<section id="tips" role="tabpanel" hidden>
  <h2>Top tips</h2>
  <div class="tip"><b class="h">Answer the exact wording.</b>"How far", "the most effective" and "evaluate this statement" each need a judgement that uses those words.</div>
  <div class="tip"><b class="h">Use numbers.</b>A gap of 100, a multiplier of 2.5 and spending of 40 show the idea better than three sentences.</div>
  <div class="tip"><b class="h">Know the formula and say what it means.</b>Multiplier = 1 ÷ (MPS + MRT + MPM) = 1 ÷ MPW. The injection needed is the gap ÷ the multiplier.</div>
  <div class="tip"><b class="h">Draw the diagram the question needs.</b>For gaps, the 45° diagram or AD/AS. For the multiplier on AD/AS, more than one shift.</div>
  <div class="tip"><b class="h">Explain evaluation.</b>Lever, because, so what. Then say whether it makes the statement more or less true.</div>
  <div class="tip"><b class="h">Compare when the question says "most".</b>Monetary against fiscal against supply side, and say why one is better in the circumstances.</div>
  <div class="tip"><b class="h">Hedge the conclusion.</b>Use could, may and likely, and say what it depends on.</div>
  <h2>Sentences you can use</h2>
  <div class="tw"><table class="t">
    <tr><th>You want to say</th><th>Use this sentence</th></tr>
    <tr><td>Definition</td><td>"An inflationary gap exists when aggregate expenditure at the full employment level of income exceeds potential output."</td></tr>
    <tr><td>Required spending</td><td>"The government needs to inject only the output gap divided by the multiplier."</td></tr>
    <tr><td>Evaluation</td><td>"However, if the marginal propensity to import is high, the multiplier could be small, so the government would have to spend nearer the full gap."</td></tr>
    <tr><td>Crowding out</td><td>"Borrowing to finance the deficit could raise interest rates and reduce private investment, which lowers the net multiplier."</td></tr>
    <tr><td>Judgement</td><td>"Overall the statement is likely to hold only when the multiplier is large and there is spare capacity, so it depends on the size of the multiplier."</td></tr>
  </table></div>
  <h2>Flashcards</h2>
  <div id="fc1"></div>
</section>
</div>
'''.replace("</section>\n<section", "</section>\n\n<section")

js = HEAD + '''
const tickSet = (gx, gy, x0, y0, xm, ym, sx, sy) => { let o = ""; for (let v = 0; v <= xm + 0.001; v += sx) { if (v > 0) o += SV.line(gx(v), y0, gx(v), gy(ym), "", { style: "stroke:var(--line);stroke-width:1;opacity:.55" }); o += SV.line(gx(v), y0, gx(v), y0 + 5, "", {}) + SV.text(gx(v), y0 + 18, v, "sm", { "text-anchor": "middle" }); }
  for (let v = sy; v <= ym + 0.001; v += sy) { o += SV.line(x0, gy(v), gx(xm), gy(v), "", { style: "stroke:var(--line);stroke-width:1;opacity:.55" }) + SV.line(x0 - 5, gy(v), x0, gy(v), "", {}) + SV.text(x0 - 9, gy(v) + 4, v, "sm", { "text-anchor": "end" }); } return o; };

/* ---------- Keynesian cross, used for both questions ---------- */
function cross(el, cfg) {
  const E0 = 70, MXV = cfg.mx, SC = cfg.sc, TOP = 36, F0 = TOP + MXV * SC, px = (v) => E0 + SC * v, py = (v) => F0 - SC * v, SL = 0.6, a1 = cfg.a1, a2 = cfg.a2, YF = 500;
  const y1 = a1 / (1 - SL), y2 = a2 / (1 - SL), top = a1 + SL * YF, lo = Math.min(YF, top), hi = Math.max(YF, top);
  let o = tickSet(px, py, E0, F0, MXV, MXV, 100, 100) + axes(E0, F0, px(MXV) + 8, TOP - 14, "", "Aggregate expenditure, AE") + SV.text(px(MXV / 2), F0 + 52, "National income, Y", "sm", { "text-anchor": "middle" });
  o += SV.line(px(0), py(0), px(MXV), py(MXV), "c3") + tag(px(MXV) + 6, py(MXV) - 8, "45° line", "t3");
  o += SV.line(px(0), py(a1), px(MXV), py(a1 + SL * MXV), "c1") + tag(px(MXV) + 6, py(a1 + SL * MXV) + 6, "AE1", "t1");
  o += SV.line(px(0), py(a2), px(MXV), py(a2 + SL * MXV), "c2") + tag(px(MXV) + 6, py(a2 + SL * MXV) + 6, "AE2", "t2");
  o += SV.line(px(YF), F0, px(YF), py(hi), "c3 dash") + tag(px(YF), F0 + 34, "YF = 500", "t3", 1, "middle");
  o += SV.line(px(YF), py(lo), px(YF), py(hi), "c2", { "stroke-width": 8 }) + tag(px(YF) - 14, py(hi) - 16, cfg.gapTxt, "t2", 1, "end");
  o += SV.circle(px(y1), py(y1), 6, "dot1") + tag(px(y1) - 10, py(y1) - 14, "Y1 = " + y1, "t1", 1, "end") + SV.circle(px(y2), py(y2), 6, "dot2") + tag(px(y2) + 14, py(y2) + 36, "Y2 = " + y2, "t2");
  $(el).innerHTML = `<svg viewBox="0 0 600 ${F0 + 66}" role="img" aria-label="${cfg.label}">${o}</svg>`;
}
cross("#dg1", { a1: 260, a2: 200, mx: 700, sc: 0.5, gapTxt: "inflationary gap = 60", label: "45 degree diagram showing an inflationary gap of 60 closed by a downward shift of AE" });
cross("#dg3", { a1: 160, a2: 200, mx: 600, sc: 0.58, gapTxt: "deflationary gap = 40", label: "45 degree diagram showing a deflationary gap of 40 closed by an upward shift of AE" });

/* ---------- AD/AS with Keynesian AS: more than one shift of AD ---------- */
(function () {
  const E0 = 70, TOP = 36, SX = 0.6, SY = 1.3, F0 = TOP + 250 * SY, px = (v) => E0 + SX * v, py = (v) => F0 - SY * v, YF = 500, P0 = 100, YMAX = 600;
  const ad = (sh) => (Y) => 200 - 0.25 * (Y - sh);
  let o = tickSet(px, py, E0, F0, YMAX, 250, 100, 50) + axes(E0, F0, px(YMAX) + 10, TOP - 14, "", "Price level") + SV.text(px(300), F0 + 52, "Real GDP ($bn)", "sm", { "text-anchor": "middle" });
  o += SV.path(`M${px(0)} ${py(P0)} L${px(YF)} ${py(P0)} L${px(YF)} ${py(250)}`, "c4") + tag(px(YF) + 6, py(238), "AS", "t4");
  const line = (sh, cls, lab, tc) => { const pts = []; for (let Y = 0; Y <= YMAX; Y += 10) { const p = ad(sh)(Y); if (p >= 40 && p <= 250) pts.push([px(Y), py(p)]); } const lp = sh === 0 ? 175 : sh === 40 ? 200 : 225, lx = px((200 - lp) / 0.25 + sh); return SV.path(Lib.ptsPath(pts), cls) + tag(lx + 6, py(lp) - 8, lab, tc); };
  o += line(0, "c1", "AD1", "t1") + line(40, "c3", "AD2", "t3") + line(100, "c2", "AD3", "t2");
  o += SV.line(px(400), py(P0), px(400), F0, "c1 dash") + SV.circle(px(400), py(P0), 6, "dot1") + tag(px(400) - 4, F0 + 34, "Y1 = 400", "t1", 1, "end");
  o += SV.circle(px(440), py(P0), 5, "dot3") + SV.line(px(440), py(P0), px(440), F0, "c3 dash");
  o += SV.line(px(500), py(P0), px(500), F0, "c2 dash") + SV.circle(px(500), py(P0), 6, "dot2") + tag(px(500) + 4, F0 + 34, "YF = 500", "t2", 1, "start");
  o += tag(px(10), py(P0) - 10, "negative output gap = 100", "t2");
  o += SV.line(px(400), py(P0) + 14, px(440), py(P0) + 14, "c3", { "stroke-width": 3 }) + SV.line(px(440), py(P0) + 14, px(500), py(P0) + 14, "c2", { "stroke-width": 3 });
  o += tag(px(YF) + 26, py(215), "AD1 to AD2: G, 40", "t3") + tag(px(YF) + 26, py(190), "AD2 to AD3: multiplier, 60", "t2");
  $("#dg2").innerHTML = `<svg viewBox="0 0 640 ${F0 + 66}" role="img" aria-label="AD and AS diagram with Keynesian AS showing AD shifting three times from output 400 to output 500">${o}</svg>`;
})();

/* ---------- self check ---------- */
function checker(el, items, res) {
  const box = $(el); if (!box) return;
  box.innerHTML = items.map((t, i) => `<label><input type="checkbox" data-i="${i}"> <span>${t}</span></label>`).join("") + '<div class="res"></div>';
  const upd = () => { const n = $$("input:checked", box).length; box.querySelector(".res").textContent = res(n, items.length); };
  $$("input", box).forEach((c) => (c.onchange = upd)); upd();
}
checker("#ck1", [
  "I defined an inflationary gap (AE at full employment above potential output) and monetary policy",
  "I drew and labelled a diagram showing the gap and used it in the text",
  "I explained a full chain for a rise in interest rates (at least four links) to a lower AE and income",
  "I explained a second type of monetary policy (money supply, credit)",
  "I included a real example or figure",
  "I explained fiscal policy as an alternative, with a limit",
  "I explained supply-side policy as an alternative, with a limit",
  "I evaluated each policy (elasticity of spending, lags, causes of inflation)",
  "I answered 'how far' with a degree and said what it depends on"
], (n, t) => n <= 3 ? "Level 1 to 2 (up to about 6 marks): you need more than one tool, a diagram and a comparison." : n <= 5 ? "Level 3 (about 7 to 8): add the missing tools, alternatives and a conclusion on relative effectiveness." : n <= 7 ? "Level 4, lower to middle (about 9 to 11): explain the evaluation and make the conclusion compare the options." : "Level 4, upper (about 11 to 13): check that the chains are developed and the conclusion depends on size and cause of the gap.");
checker("#ck2", [
  "I defined negative output gap and full employment",
  "I defined expansionary fiscal policy and said G is an injection and a component of AD",
  "I gave the multiplier formula and the open-economy version (MPS + MRT + MPM)",
  "I calculated the spending needed (gap ÷ multiplier) with numbers",
  "I explained multiple rounds of spending and induced consumption and investment",
  "I drew an AD/AS diagram with more than one shift (or explained why the rise is more than the spending)",
  "I applied it to a type of government spending (roads, schools) or a real figure",
  "I evaluated at least three points, each explained (lever, because, so what)",
  "I included both undershoot and overshoot as the multiplier is uncertain",
  "I wrote a conclusion that answers the statement, says when it holds and ranks the factors"
], (n, t) => n <= 3 ? "Level 1 (about 1 to 5 of 14, E1 at best): learn the concepts and the formula and add numbers." : n <= 5 ? "Level 2 (about 6 to 10 of 14, E1): add the rounds, the diagram and application, and explain each evaluation point." : n <= 8 ? "Level 3 for the 14 and E1 to E2 (about 11 to 14, 3 to 5): make sure every evaluation point is explained and ends with 'so what'." : "Level 3 and E2 (about 13 to 14 of 14 and 5 to 6 of 6): check the conclusion answers the statement directly.");

/* ---------- practise ---------- */
Lib.classify($("#cl1"), { prompt: "Which skill does each sentence show?", buckets: [{ label: "Knowledge" }, { label: "Application" }, { label: "Analysis" }, { label: "Evaluation" }], items: [
  { text: "A negative output gap exists when actual output is below potential output.", b: 0 },
  { text: "The Bank of England raised Bank Rate from 0.1% to 5.25% between late 2021 and August 2023.", b: 1 },
  { text: "A higher interest rate raises the cost of borrowing, so firms cancel investment and AE shifts down.", b: 2 },
  { text: "However, if firms are confident, investment may fall by less than expected and some of the gap remains.", b: 3 },
  { text: "The multiplier is the ratio of the final change in income to the initial change in an injection.", b: 0 },
  { text: "Workers on a new railway spend their wages in shops, which pay their own staff.", b: 1 },
  { text: "The multiplier is 1 ÷ 0.4 = 2.5, so $40bn of spending raises income by $100bn.", b: 2 },
  { text: "With a high MPM the multiplier falls to 1.25 and the government would need to spend $80bn.", b: 3 }],
  done: "Evaluation questions the claim and says what changes. Analysis explains the steps. Application uses the specific context or figures." });
Lib.order($("#o1"), { prompt: "Put the chain for question 2 in order, starting with the first event.", items: ["The government spends $40bn on infrastructure", "Construction firms and workers receive $40bn of extra income", "They spend part of it, which becomes income for others (rounds of spending)", "Induced consumption and investment add to later rounds", "National income rises by 40 × 2.5 = $100bn and output reaches full employment"], done: "The required injection is the gap ÷ the multiplier." });
Lib.calc($("#c1"), { qs: [
  { q: "MPS = 0.1, MRT = 0.2 and MPM = 0.1. What is the multiplier?", a: 2.5, tol: 0.01, sol: "MPW = 0.4, so k = 1 ÷ 0.4 = <b>2.5</b>." },
  { q: "The negative output gap is $100bn and the multiplier is 2.5. How much must the government spend ($bn)?", a: 40, tol: 0.01, sol: "100 ÷ 2.5 = <b>$40bn</b>." },
  { q: "MPS = 0.2, MRT = 0.2 and MPM = 0.4. What is the multiplier?", a: 1.25, tol: 0.01, sol: "MPW = 0.8, so k = 1 ÷ 0.8 = <b>1.25</b>." },
  { q: "Using that multiplier and a gap of $100bn, how much must the government spend ($bn)?", a: 80, tol: 0.01, sol: "100 ÷ 1.25 = <b>$80bn</b>." },
  { q: "AE1 = 260 + 0.6Y and full employment is 500. What is the inflationary gap (the vertical distance at 500)?", a: 60, tol: 0.01, sol: "AE at 500 is 260 + 300 = 560. The gap is 560 − 500 = <b>60</b>." },
  { q: "With a multiplier of 2.5, a fall in autonomous spending of 60 lowers income by how much ($bn)?", a: 150, tol: 0.01, sol: "60 × 2.5 = <b>$150bn</b>." }] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which statement about the Question 2 conclusion is best?", opts: ["The statement is always true because the multiplier is greater than one", "The statement is true in theory, but in practice it depends on the size of the multiplier, so spending may be too little or too much", "The statement is false because crowding out always cancels the multiplier", "The statement cannot be evaluated"], a: 1, why: "A top conclusion answers the statement, says when it holds, and ranks the factors." },
  { q: "Which is the strongest evaluation of an interest rate rise as a way to close an inflationary gap?", opts: ["It is expensive", "It depends on how sensitive spending is to interest rates and it works with a lag, so the gap could close first or remain", "It is used by many governments", "It always works"], a: 1, why: "It explains the lever, the reason and the effect on the outcome." },
  { q: "On an AD/AS diagram for Question 2, what should the examiner see?", opts: ["One shift of AD only", "More than one shift of AD, or one shift with an explanation that the rise is more than the spending", "AS shifting to the right", "A fall in the price level"], a: 1, why: "The mark scheme asks for this." },
  { q: "Why is the 20-mark question harder than the 13-mark one?", opts: ["It has more content", "Knowledge and analysis (14) and evaluation (6) are marked separately, so each skill needs more depth", "It needs no diagram", "It is only about evaluation"], a: 1, why: "The 20-mark scales reward depth in each skill separately." },
  { q: "An answer to Question 1 uses only fiscal policy. What is the likely result?", opts: ["Full marks", "A low level because the question asks about monetary policy", "Level 4", "No effect"], a: 1, why: "The scheme asks for at least two types of monetary policy." }] });
Lib.cards($("#fc1"), { cards: [
  ["Inflationary gap", "AE at the full employment level of income exceeds potential output; excess demand pulls up the price level."],
  ["Negative output gap", "Actual output below potential output; spare capacity and cyclical unemployment."],
  ["Multiplier (open economy)", "1 ÷ (MPS + MRT + MPM) = 1 ÷ MPW."],
  ["Injection needed", "Output gap ÷ multiplier."],
  ["Crowding out", "Government borrowing raises interest rates and reduces private investment, lowering the net multiplier."],
  ["Lever, because, so what", "The structure of an explained evaluation point."],
  ["Table A", "14 marks: knowledge, application and analysis (L1 1–5, L2 6–10, L3 11–14)."],
  ["Table B", "6 marks: evaluation (E1 1–3, E2 4–6)."]] });
'''

(D / "pe91.body.html").write_text(body)
(D / "pe91.js").write_text(js)
(D / "pe91.css").write_text(CSS)
print(subprocess.run(["python3", str(D / "assemble.py"), "pe91", "Two Paper 4 Essays on 9.1, Marked in Depth", "paper4-worked-essays-9-1"], capture_output=True, text=True).stdout.strip())
