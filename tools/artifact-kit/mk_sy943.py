"""Syllabus 9.4.3 The quantity theory of money. Run: python3 tools/artifact-kit/mk_sy943.py"""
from syl import *
EY = "A Level Economics · 9708 · Syllabus 9.4.3"

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>The <b class="kw">quantity theory of money</b> is built on the identity <b>MV = PT</b>: the money supply (M) times the velocity of circulation (V) equals the price level (P) times the volume of transactions (T). If <b>V is stable</b> and <b>T is fixed</b> at full employment, a rise in M leads to a proportional rise in P, so <b>inflation is caused by growth of the money supply</b>. This is the monetarist view and it supports controlling the money supply to control inflation. Critics say V is unstable, T can change when there is spare capacity, causation may run from prices to money, and the money supply is hard to define and control.</p></div>

  <h2>1 · The equation</h2>
  <div class="formula">MV = PT</div>
  <div class="tw"><table class="t">
    <tr><th>Symbol</th><th>Meaning</th></tr>
    <tr><td><b>M</b></td><td>The money supply: the stock of money in the economy</td></tr>
    <tr><td><b>V</b></td><td>The <b>velocity of circulation</b>: the average number of times a unit of money is used in transactions in a period</td></tr>
    <tr><td><b>P</b></td><td>The average price level</td></tr>
    <tr><td><b>T</b></td><td>The number (volume) of transactions of goods and services in the period, often taken as real output (the Fisher form)</td></tr>
  </table></div>
  <p><b>MV = PT is an identity</b>: both sides measure total spending, so it is true by definition. It becomes a <b>theory</b> when assumptions are added about V and T.</p>
  <div id="pic1" class="card"></div>

  <h2>2 · The monetarist argument</h2>
  <ul>
    <li><b>V is stable or changes predictably</b> in the short run, because it depends on institutions and habits (how often people are paid, the use of credit cards and cash machines).</li>
    <li><b>T is fixed in the long run</b> at the level determined by real factors: the economy tends to full employment and output is determined by supply.</li>
    <li>Therefore a change in <b>M</b> changes only <b>P</b>. To raise prices 5% a year more than output grows, the money supply must grow more than output.</li>
    <li><b>Policy conclusion:</b> to control inflation, control the growth of the money supply (set a rule or target).</li>
  </ul>
  <div class="formula">% change in P ≈ % change in M + % change in V − % change in T</div>

  <h2>3 · What affects velocity?</h2>
  <ul>
    <li><b>Frequency of income payments:</b> weekly pay means people hold smaller balances, so V is higher than with monthly pay.</li>
    <li><b>Interest rates:</b> higher rates give a reward for holding less money, so V rises.</li>
    <li><b>Payment technology:</b> credit and debit cards, online banking and cash machines let people hold smaller balances, raising V.</li>
    <li><b>Expectations:</b> if people expect prices to rise, they spend money quickly, raising V.</li>
    <li><b>Confidence and uncertainty:</b> in a crisis people hold on to money and V falls.</li>
  </ul>

  <h2>4 · Evaluation</h2>
  <div class="tw"><table class="t">
    <tr><th>Criticism</th><th>Explanation</th></tr>
    <tr><td><b>V is not stable</b></td><td>Financial innovation, changes in interest rates and in confidence move V. After 2008 V fell sharply, so large increases in M (quantitative easing) did not raise prices much.</td></tr>
    <tr><td><b>T is not fixed</b></td><td>With spare capacity (a negative output gap) extra money can raise output and employment rather than prices (the Keynesian view).</td></tr>
    <tr><td><b>Causation</b></td><td>The money supply may be <b>endogenous</b>: it responds to demand for loans and rising prices, rather than causing them.</td></tr>
    <tr><td><b>Defining and controlling M</b></td><td>Which measure of the money supply? Banks create deposits by lending, and the central bank cannot control them precisely.</td></tr>
    <tr><td><b>Time lags</b></td><td>The effect of money on prices is long and variable.</td></tr>
    <tr><td><b>Other causes of inflation</b></td><td>Cost-push inflation (oil prices, wages) is not due to the money supply, though it may need monetary accommodation to continue.</td></tr>
  </table></div>
  <div class="tip"><b class="h">Strong conclusion</b>The theory may hold in the long run, in high-inflation episodes (hyperinflation is almost always accompanied by very rapid money growth), but it is a poor guide in the short run, when V and T are changing, especially in a recession.</div>
'''

watch = '''
  <h2>1 · The equation as a balance</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stE"></div>
  <h2>2 · Money growth and inflation: two cases</h2>
  <div id="stG"></div>
'''

explore = '''
  <h2>Lab 1 · MV = PT calculator</h2>
  <p>Change the money supply, velocity and transactions. The lab shows the price level the equation implies, and how it changes from the base case (M = 1,000, V = 4, T = 2,000, P = 2).</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div>
    <div class="readout"><div><small>Price level P = MV ÷ T</small><strong id="r1"></strong></div><div><small>Change in P</small><strong id="r2"></strong></div><div><small>Total spending MV</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 300" role="img" aria-label="Bars showing MV on the left and PT on the right"></svg></div></div></div>

  <h2>Lab 2 · Does extra money mean inflation?</h2>
  <p>The money supply rises by 10%. Choose how much spare capacity there is. The more spare capacity, the more of the extra spending is met by extra output.</p>
  <div class="card"><div class="grid2"><div><div id="g5"></div>
    <div class="readout"><div><small>Rise in output (T)</small><strong id="t1"></strong></div><div><small>Rise in prices (P)</small><strong id="t2"></strong></div><div><small>View supported</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 420 300" role="img" aria-label="Bars showing the rise in output and prices after a 10 percent rise in the money supply"></svg></div></div></div>
'''

practise = '''
  <h2>1 · What happens to prices?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the monetarist argument in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Weimar Germany, 1923", "The government financed its spending by printing money. The money supply rose by many times a month and prices rose even faster, as V also rose because people spent money as soon as they got it.", "the strongest evidence for the quantity theory: very fast money growth and hyperinflation. Add that V rose too.") +
rw("Quantitative easing after 2008", "Central banks created trillions of dollars of reserves, but inflation stayed low for a decade. Banks held reserves instead of lending them, V fell, and the economy had spare capacity.", "a counter-example for the theory: V is not stable and T can rise when there is spare capacity.") +
rw("Monetary targeting in the 1980s", "The US and UK tried to control inflation by targeting the growth of the money supply. They found it hard to control and unstable relationships between money and prices, and moved to targeting interest rates and then inflation directly.", "the practical difficulty of defining and controlling M and unstable velocity.") +
rw("Digital payments and velocity", "As contactless cards and mobile payments spread, people hold less cash and can move money faster. This tends to raise V and means that a given money supply supports more spending.", "a factor that changes velocity and a reason V is not constant.")
)

mc_exam = [
  ("In MV = PT, V is the income velocity of circulation. Which change would tend to reduce V? (Feb/March 2025 · 32 · Q17, reworded)", ["A move to monthly rather than weekly salary payments", "A rise in interest rates", "More use of cash machines to reduce money balances held", "A fall in the use of credit cards by individuals"], 0, "Less frequent payments mean people hold larger balances for longer, so money circulates more slowly."),
  ("The quantity theory is sometimes written MV = PT. Which statement is not correct? (May/June 2025 · 34 · Q19, reworded)", ["M is the total value of notes and coins in circulation only", "P measures the average price level", "T stands for the quantity of real transactions in the period", "V is the average number of times money changes hands in a period"], 0, "M is the whole money supply, including bank deposits, not only notes and coins."),
  ("Which components of the quantity theory are considered constant and which variable by monetarists? (Oct/Nov 2022 · 33 · Q23, reworded)", ["Money supply constant, velocity variable, price level constant, transactions variable", "Velocity and transactions constant; money supply and price level variable", "Money supply variable, velocity constant, price level variable, transactions constant", "All variable"], 1, "Monetarists assume V and T are constant, so M changes lead to changes in P."),
  ("What is an important assumption of monetarism? (Oct/Nov 2020 · 32 · Q25, reworded)", ["Fiscal policy is more effective than monetary policy in reducing inflation", "Long-term unemployment results from deficient demand", "The interest elasticity of investment is low", "The velocity of circulation is stable"], 3, "A stable velocity is what makes money growth predict inflation."),
  ("Which statement does not correctly characterise the monetarist view? (Oct/Nov 2022 · 31 · Q25, reworded)", ["Inflation is always caused by increases in the money supply in the long run", "The LRAS curve is vertical", "The velocity of circulation of money is highly unstable", "Policy should follow set rules"], 2, "Monetarists believe velocity is stable or predictable."),
  ("What belief do Keynesians and monetarists share? (May/June 2020 · 31 · Q27, reworded)", ["Expectations adapt quickly", "Fiscal policy is the most effective policy", "There is a need for individual choice expressed through the market", "Velocity of circulation is stable"], 2, "Both accept a role for markets and individual choice, though they disagree about the rest."),
  ("What do monetarists believe? (Oct/Nov 2022 · 32 · Q25, reworded)", ["Economies are naturally unstable", "Policy makers should follow set rules targeting the money supply", "The AS curve has a slight slope", "Wages are sticky downwards"], 1, "Monetarists favour rules for the money supply rather than discretion.")
]

exam = exam_page("the quantity theory of money",
  "We searched the A Level Economics papers in the folder (2020 to 2025). The quantity theory is a favourite Paper 4 12 mark question and appears as the basis of longer essays on money and inflation. Reworded questions are below, with eight Paper 3 multiple choice questions.",
  [("Essay part, 12 marks", "3", "May/June 2021 (41, 43) Q7(a); Oct/Nov 2021 (41) Q5(a); Oct/Nov 2021 (42) Q7(a)"), ("Essay, 20 marks", "1", "Oct/Nov 2024 (43) Q4"), ("Essay, 25 marks", "1", "Feb/March 2020 (42) Q6"), ("Multiple choice (Paper 3)", "7 shown below", "2020 to 2025")],
  [
  eq("Based on May/June 2021 · 9708/41 and 43 · Q7(a)", "12 marks", "Explain and critically evaluate the quantity theory of money.",
     ["The theory is based on MV = PT and assumes V is constant and T is constant (at full employment), so a change in M directly changes P.",
      "Critics question both assumptions, and point out that the money supply is hard to measure and control.",
      "Level 4 (9 to 12) needs a clear explanation of the theory and its assumptions with at least two critical points (unstable velocity, T flexible with spare capacity, causation, definition and control of M)."],
     "Equation and meaning. Assumptions. Monetarist conclusion. Two or three criticisms. Judgement on short run versus long run."),
  eq("Based on Oct/Nov 2021 · 9708/41 · Q5(a)", "12 marks", "Explain the quantity theory of money and discuss why the theory might not work in practice.",
     ["Explain MV = PT and the assumptions about V and T and the conclusion that inflation is a monetary phenomenon.",
      "Why it might not work: velocity changes with payment technology, interest rates and expectations; with spare capacity extra money raises output not prices; the money supply is endogenous and hard to control; cost-push inflation.",
      "Credit evidence: QE after 2008 raised M without much inflation; hyperinflation episodes support the link."],
     "Theory first. Then three reasons it might fail with examples. Short conclusion."),
  eq("Based on Oct/Nov 2021 · 9708/42 · Q7(a)", "12 marks", "Explain the quantity theory of money and consider its relevance for a country's macroeconomic policy.",
     ["Explain the equation and the monetarist assumptions.",
      "Policy relevance: control inflation by targeting money supply growth; central banks control M with interest rates and open market operations; supports rules rather than discretion.",
      "Limits: unstable V, difficulty of controlling M, effect on output when there is spare capacity; most central banks now target inflation or interest rates directly.",
      "A reasoned conclusion on how relevant it is today."],
     "Equation. Policy implication. Practical limits. Judgement."),
  eq("Based on Oct/Nov 2024 · 9708/43 · Q4", "20 marks", "'Central banks can control the money supply. An increase in the money supply will cause inflation. Therefore central banks can control inflation.' Evaluate this statement.",
     ["<b>Analysis (14):</b> how a central bank can influence the money supply (open market operations, interest rates, reserve requirements, QE); the quantity theory MV = PT and the link from M to P; link to inflation targets; other causes of inflation.",
      "<b>Evaluation (6):</b> commercial banks create most money, so control of M is incomplete; velocity is unstable; with spare capacity more money raises output; cost-push and imported inflation are not controlled by M; time lags and expectations; central banks usually target interest rates and use M as an indicator."],
     "Two links in the argument: can the bank control M, and does M cause P? Test each. Then other causes. Conclude: partly."),
  eq("Based on Feb/March 2020 · 9708/42 · Q6", "25 marks", "'Monetarists insist that control of the money supply is the key to solving inflation, Keynesians argue that inflation can only be controlled by controlling expenditure.' To what extent do you agree that both approaches are only partially correct?",
     ["Explain the monetarist argument (quantity theory, V and T stable, rules for money) and the Keynesian argument (inflation from excess aggregate demand, controlled by fiscal and monetary policy aimed at expenditure; cost-push causes).",
      "Show that the approaches overlap: controlling expenditure and controlling the money supply are linked through MV, and both only address demand-side inflation.",
      "Both are partial: cost-push inflation and expectations need other policies (supply-side, exchange rate, incomes policy); the best answer depends on the cause and the state of the economy."],
     "Two views. Overlap. What each misses (cost-push, expectations). Conclude: partial.")
  ],
  )

tips = tips_html(
  [("Write the equation and define every letter.", "MV = PT with M, V, P and T."),
   ("State the assumptions.", "V stable and T fixed at full employment. Without them it is only an identity."),
   ("Give the conclusion.", "Inflation is caused by excess growth of the money supply, so control M."),
   ("Criticise with three points.", "Unstable velocity, T changes with spare capacity, causation or control of M."),
   ("Use evidence.", "Hyperinflation supports it, QE after 2008 weakens it."),
   ("Distinguish short run and long run.", "The theory is more convincing in the long run."),
   ("Use 'could' and 'may'.", "These are theories about tendencies, not certainties.")],
  [("Equation", "The quantity theory is based on the equation MV = PT, where M is the money supply, V the velocity, P the price level and T the volume of transactions."),
   ("Assumption", "If V and T are constant, a rise in M must lead to a proportional rise in P."),
   ("Policy", "To control inflation the central bank should control the growth of the money supply."),
   ("Evaluate", "However, velocity is not stable, because it depends on payment technology, interest rates and expectations."),
   ("Spare capacity", "If there is spare capacity, a rise in M may raise output (T) instead of prices.")],
  [CW["define"], CW["explain"], CW["evaluate"], CW["discuss"]]) + FC

js = '''
/* ---------- Scale picture ---------- */
function scaleSvg(M, V, P, T, note) {
  const L = M * V, R = P * T, mx = Math.max(L, R, 1) * 1.15, Y = (v) => 270 - v / mx * 220; let o = SV.line(40, 270, 720, 270);
  o += SV.rect(110, Y(L), 220, 270 - Y(L), "f1") + tag(220, Y(L) - 8, "MV = " + Lib.fmtN(L, 0), "t1", 1, "middle") + SV.text(220, 290, "M × V (spending)", "sm bd", { "text-anchor": "middle" });
  o += SV.rect(430, Y(R), 220, 270 - Y(R), "f4") + tag(540, Y(R) - 8, "PT = " + Lib.fmtN(R, 0), "t4", 1, "middle") + SV.text(540, 290, "P × T (value of transactions)", "sm bd", { "text-anchor": "middle" });
  o += tag(220, 190, "M = " + M + ", V = " + Lib.fmtN(V, 1), "t1", 1, "middle") + tag(540, 190, "P = " + Lib.fmtN(P, 2) + ", T = " + Lib.fmtN(T, 0), "t4", 1, "middle");
  if (note) o += tag(380, 30, note, "t3", 1, "middle");
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 310" role="img" aria-label="Bars showing that money supply times velocity equals price level times transactions">${scaleSvg(1000, 4, 2, 2000, "Both sides measure total spending: 4,000")}</svg>`;
function eqDraw(s) { const M = 1000 * (1 + 0.1 * s.m), V = 4 * (1 + s.v), T = 2000 * (1 + s.t), P = M * V / T; return scaleSvg(M, V, P, T, s.l); }
Lib.stepper($("#stE"), { w: 760, h: 310, label: "The equation MV = PT as two bars of equal height changing as M rises, V changes or T changes", base: { m: 0, v: 0, t: 0, l: "" }, draw: eqDraw, tween: 1000, dwell: 5800, steps: [
  { cap: "<b>The identity.</b> M = 1,000, V = 4 so total spending MV is 4,000. With T = 2,000 transactions, P = 2. Both sides measure the same thing.", s: { l: "Base case: P = 2" } },
  { cap: "<b>M rises 10%</b> with V and T unchanged. Spending is 4,400 and P rises to 2.2: a 10% rise. This is the quantity theory's prediction.", s: { m: 1, l: "M up 10%: P up 10%" } },
  { cap: "<b>Velocity falls.</b> If people hold on to money (V falls 10%), the extra money is offset and P stays near 2. The prediction fails if V is not stable.", s: { m: 1, v: -0.1, l: "V down 10%: P back to about 2" } },
  { cap: "<b>Transactions rise.</b> With spare capacity T could rise 10%, so the extra spending buys more output. P is back at 2 with higher output. The prediction fails if T is not fixed.", s: { m: 1, t: 0.1, l: "T up 10%: P back to 2" } },
] });

/* ---------- Watch 2: two cases ---------- */
const GXX = (t) => 90 + t * 62, GYY = (v) => 300 - v * 2.2;
function twoDraw(s) {
  let o = SV.line(70, 300, 700, 300) + SV.line(70, 300, 70, 40) + SV.text(700, 320, "Years", "sm", { "text-anchor": "end" }) + SV.text(76, 34, "Index (year 0 = 100)", "sm");
  const N = Math.round(s.n), mk = (f) => Lib.ptsPath(Array.from({ length: N + 1 }, (_, t) => [GXX(t), GYY(f(t) - 80)]));
  const money = (t) => 100 * Math.pow(1.12, t), pr1 = (t) => 100 * Math.pow(s.k > 0 ? 1.12 : 1.02, t), out1 = (t) => 100 * Math.pow(s.k > 0 ? 1.0 : 1.05, t);
  if (N >= 1) { o += SV.path(mk(money), "c1") + SV.path(mk(pr1), "c2") + SV.path(mk(out1), "c3"); o += tag(GXX(N) + 6, GYY(money(N) - 80) - 6, "money supply", "t1") + tag(GXX(N) + 6, GYY(pr1(N) - 80) + 14, "prices", "t2") + tag(GXX(N) + 6, GYY(out1(N) - 80) + 28, "real output", "t3"); }
  o += tag(380, 56, s.l, "t4", 1, "middle");
  return o;
}
Lib.stepper($("#stG"), { w: 760, h: 340, label: "Money supply growing 12 percent a year with prices rising in one case and output rising in the other", base: { n: 0, k: 0, l: "" }, draw: twoDraw, tween: 1000, dwell: 6000, steps: [
  { cap: "<b>The same money growth.</b> In both economies the money supply grows 12% a year.", s: { n: 1, k: 0, l: "Case A: spare capacity" } },
  { cap: "<b>Case A: spare capacity.</b> The economy has idle resources. Extra spending raises <b>real output</b> by about 5% a year and prices by only 2%: velocity or output absorbs the money. This supports the Keynesian view.", s: { n: 8, k: 0, l: "Case A: spare capacity" } },
  { cap: "<b>Case B: full employment.</b> Output cannot rise. Money growth of 12% shows up almost wholly as <b>inflation of 12%</b>, as the quantity theory predicts.", s: { n: 8, k: 1, l: "Case B: at full employment" } },
] });

/* ---------- Lab 1 ---------- */
function labQT() {
  if (!$("#qm") || !$("#qv") || !$("#qt")) return;
  const M = +$("#qm").value, V = +$("#qv").value / 10, T = +$("#qt").value, P = M * V / T, chg = (P / 2 - 1) * 100;
  $("#r1").textContent = Lib.fmtN(P, 2); $("#r2").textContent = (chg >= 0 ? "+" : "") + Lib.fmtN(chg, 1) + "%"; $("#r3").textContent = Lib.fmtN(M * V, 0);
  $("#rv").textContent = Math.abs(chg) < 0.5 ? "The three variables roughly offset: the price level is about unchanged." : chg > 0 ? `MV = ${Lib.fmtN(M * V, 0)} against T = ${T}, so P = ${Lib.fmtN(P, 2)}, a rise of ${Lib.fmtN(chg, 1)}%. Spending has grown faster than transactions.` : `MV = ${Lib.fmtN(M * V, 0)} against T = ${T}, so P = ${Lib.fmtN(P, 2)}, a fall of ${Lib.fmtN(-chg, 1)}%. Transactions have grown faster than spending (deflation).`;
  $("#labA").innerHTML = scaleSvg(M, V, P, T, "");
}
Lib.slider($("#g1"), { id: "qm", label: "Money supply M ", min: 600, max: 1600, step: 50, value: 1000, fmt: (v) => v, onInput: labQT });
Lib.slider($("#g2"), { id: "qv", label: "Velocity V ", min: 20, max: 80, step: 2, value: 40, fmt: (v) => Lib.fmtN(v / 10, 1), onInput: labQT });
Lib.slider($("#g3"), { id: "qt", label: "Transactions T ", min: 1400, max: 2800, step: 100, value: 2000, fmt: (v) => v, onInput: labQT });
labQT();

/* ---------- Lab 2 ---------- */
function labSC() {
  if (!$("#sp")) return;
  const g = 10, share = +$("#sp").value / 100, dT = g * share, dP = (1 + g / 100) / (1 + dT / 100) * 100 - 100;
  $("#t1").textContent = "+" + Lib.fmtN(dT, 1) + "%"; $("#t2").textContent = "+" + Lib.fmtN(dP, 1) + "%"; $("#t3").textContent = share < 0.2 ? "Monetarist" : share > 0.6 ? "Keynesian" : "Mixed";
  $("#tv").textContent = `A 10% rise in the money supply with ${Math.round(share * 100)}% of it met by extra output raises output by ${Lib.fmtN(dT, 1)}% and prices by ${Lib.fmtN(dP, 1)}% (velocity held constant). With full employment (0% met by output) all of the rise goes to prices; with large spare capacity most goes to output.`;
  let o = SV.line(40, 250, 400, 250); [["Output", dT, "f3", "t3"], ["Prices", dP, "f2", "t2"]].forEach(([l, v, c, t], i) => { const x = 90 + i * 150, h = v / 11 * 200; o += SV.rect(x, 250 - h, 90, Math.max(h, 2), c) + tag(x + 45, 250 - h - 8, "+" + Lib.fmtN(v, 1) + "%", t, 1, "middle") + SV.text(x + 45, 270, l, "sm bd", { "text-anchor": "middle" }); });
  $("#labB").innerHTML = o;
}
Lib.slider($("#g5"), { id: "sp", label: "Share of extra spending met by extra output (%) ", min: 0, max: 100, step: 10, value: 0, fmt: (v) => v, onInput: labSC });
labSC();

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "According to the quantity theory (V and T constant), what happens to the price level?", ["Rises", "Falls", "Stays the same"],
  [("The money supply rises 8% and output is unchanged", 0), ("The money supply is unchanged and transactions rise 5%", 1), ("The money supply and transactions both rise 4%", 2), ("The money supply falls 6% and output is unchanged", 1), ("The money supply rises 5% and transactions rise 5%", 2), ("The money supply rises 15% and transactions rise 3%", 0)],
  "With V constant: %ΔP ≈ %ΔM − %ΔT.") + MATCH([
  ["MV = PT", "Total spending equals the value of transactions: an identity"],
  ["Velocity of circulation", "How many times a unit of money is spent in a period"],
  ["Monetarism", "The view that money supply growth drives inflation"],
  ["Endogenous money", "Money supply that responds to demand for credit"],
  ["Fisher equation", "The form of the theory with T as transactions or real output"],
  ["Money supply rule", "A rule to keep the growth of money in line with output"]]) + ORDER(
  "Put the monetarist argument in order.",
  ["The central bank allows the money supply to grow faster than output", "There is more money chasing the same quantity of goods", "With V and T constant total spending rises while output cannot", "Prices rise", "Inflation can be controlled only by slowing money growth"],
  "Inflation is a monetary phenomenon in the monetarist view.") + CALC([
  {"q": "M = 500, V = 4 and T = 1,000. Calculate the price level P.", "a": 2, "tol": 0.01, "hint": "P = MV ÷ T.", "sol": "500 × 4 ÷ 1000 = <b>2</b>."},
  {"q": "M rises to 600 with V = 4 and T = 1,000. Calculate the percentage change in the price level from the previous question.", "a": 20, "unit": "%", "tol": 0.05, "hint": "New P = 600 × 4 ÷ 1000 = 2.4.", "sol": "P rises from 2 to 2.4: <b>20%</b>."},
  {"q": "The money supply grows 7% a year, velocity is constant and real output grows 2% a year. Using the approximation, what is the inflation rate (%)?", "a": 5, "unit": "%", "tol": 0.05, "hint": "%ΔP ≈ %ΔM − %ΔT.", "sol": "7 − 2 = <b>5%</b>."},
  {"q": "Nominal GDP is $2,400bn and the money supply is $600bn. Calculate the income velocity of circulation.", "a": 4, "tol": 0.01, "hint": "V = nominal GDP ÷ M.", "sol": "2400 ÷ 600 = <b>4</b>."}]) + MCQ([
  ("The quantity theory of money states that:", ["A rise in the money supply raises output", "A rise in the money supply raises the price level when V and T are constant", "Velocity always rises", "Prices are unrelated to money"], 1, "With V and T fixed, MV = PT implies that a rise in M raises P."),
  ("Which would raise the velocity of circulation?", ["Wages paid monthly instead of weekly", "More use of credit cards", "A fall in interest rates", "Greater uncertainty and hoarding of cash"], 1, "Card use lets people hold smaller balances so money circulates faster."),
  ("What would a Keynesian say about the effect of extra money in a recession?", ["Prices will rise one-for-one", "Output may rise because there is spare capacity", "Velocity is stable", "Nothing will happen to demand"], 1, "With spare capacity T can rise, so the quantity theory prediction fails."),
  ("Which is a criticism of the quantity theory?", ["V is not stable", "It uses equations", "It mentions prices", "It is too simple to state"], 0, "V changes with technology, interest rates and confidence."),
  ("Which period is most associated with money growth causing hyperinflation?", ["Weimar Germany in 1923", "The UK in 1990", "Japan in 2000", "The US in 2019"], 0, "Rapid printing of money led to extreme price rises.")
], "qz1") + CARDS([
  ("MV = PT", "Money supply × velocity = price level × transactions."),
  ("Velocity of circulation", "Times a unit of money is spent in a period."),
  ("Quantity theory", "With V and T stable, M changes P."),
  ("Monetarism", "Inflation is caused by excessive money supply growth."),
  ("Endogenous money", "The supply of money responds to demand."),
  ("Hyperinflation", "Extremely rapid, accelerating inflation."),
  ("Money supply rule", "Fixed target for money growth."),
  ("Fisher", "Developed the equation of exchange.")]) + MCQ(mc_exam)

build("sy943", "quantity-theory-of-money", "The Quantity Theory of Money (MV = PT)", EY,
  "9.4.3: the equation MV = PT, the monetarist assumptions about velocity and transactions, and an evaluation of the theory. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
