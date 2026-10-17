"""AS syllabus 4.2 Circular flow of income. Run: python3 tools/artifact-kit/mk_as42.py"""
from asx import *
EY = EYAS("4.2")

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>The <b class="kw">circular flow of income</b> shows how <b>income</b> flows from firms to households as payments to factors of production (wages, rent, interest, profit) and how <b>expenditure</b> flows back from households to firms as spending on goods and services. In a <b>closed economy</b> with government, <b>withdrawals (leakages)</b> are <b>saving (S)</b> and <b>taxes (T)</b>, and <b>injections</b> are <b>investment (I)</b> and <b>government spending (G)</b>; an <b>open economy</b> adds <b>exports (X)</b> as an injection and <b>imports (M)</b> as a withdrawal. National income is in <b>equilibrium</b> when <b>injections equal withdrawals</b> (I + G + X = S + T + M): if injections exceed withdrawals national income rises, and if withdrawals exceed injections it falls until balance is restored. The multiplier and the marginal propensities are not required at AS.</p></div>

  <h2>1 · The flows (4.2.1)</h2>
  <div id="pic1" class="card"></div>
  <ul>
    <li><b>Households</b> supply factors of production (labour, land, capital, enterprise) and receive <b>income</b>; they spend it on goods and services from <b>firms</b>.</li>
    <li><b>Three-sector economy:</b> households, firms and the <b>government</b>, which collects <b>taxes (T)</b> and spends on public services and investment (<b>G</b>).</li>
    <li><b>Open economy:</b> adds the <b>international sector</b>: foreign buyers purchase <b>exports (X)</b> and domestic buyers purchase <b>imports (M)</b>.</li>
    <li>Money flows <b>round</b> the system, so what one person spends is another's income. Real resources flow the other way.</li>
  </ul>

  <h2>2 · Injections, withdrawals and equilibrium (4.2.2 to 4.2.3)</h2>
  <div id="pic2" class="card"></div>
  <div class="tw"><table class="t">
    <tr><th></th><th>Closed economy</th><th>Open economy</th></tr>
    <tr><td><b>Withdrawals (leakages)</b></td><td>Saving (S), taxes (T)</td><td>S, T and <b>imports (M)</b></td></tr>
    <tr><td><b>Injections</b></td><td>Investment (I), government spending (G)</td><td>I, G and <b>exports (X)</b></td></tr>
    <tr><td><b>Equilibrium</b></td><td>I + G = S + T</td><td>I + G + X = S + T + M</td></tr>
  </table></div>
  <ul>
    <li><b>Injections &gt; withdrawals:</b> more is flowing in than out, so national income <b>rises</b> (economic growth).</li>
    <li><b>Withdrawals &gt; injections:</b> national income <b>falls</b>.</li>
    <li>The equilibrium condition can be rearranged: (S − I) + (T − G) + (M − X) = 0. So a <b>budget deficit</b> (G &gt; T) or a <b>trade deficit</b> (M &gt; X) must be matched by saving exceeding investment, or by another sector's surplus.</li>
    <li><b>Examples:</b> a rise in exports or in investment is an injection and raises national income; a rise in saving or in taxes is a withdrawal and lowers it unless offset by an injection.</li>
  </ul>
  <div class="tip"><b class="h">Exam tip</b>Draw the diagram with <b>both</b> sides: income and expenditure between households and firms, then <b>label injections and withdrawals</b>. State the equilibrium condition and say what happens to national income when they differ.</div>
'''

watch = '''
  <h2>1 · From the simple flow to the open economy</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stC"></div>
  <h2>2 · Injections and withdrawals adjust</h2>
  <div id="stE"></div>
'''

explore = '''
  <h2>Lab 1 · Is the circular flow in equilibrium?</h2>
  <p>Set the injections and withdrawals ($bn) and see whether national income will tend to rise, fall or stay the same.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div><div id="g4"></div><div id="g5"></div><div id="g6"></div>
    <div class="readout"><div><small>Injections</small><strong id="r1"></strong></div><div><small>Withdrawals</small><strong id="r2"></strong></div><div><small>National income will</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 300" role="img" aria-label="Stacked bars of injections and withdrawals"></svg></div></div></div>

  <h2>Lab 2 · Closed or open economy?</h2>
  <p>Choose the type of economy to see which flows are included and the equilibrium condition.</p>
  <div class="card"><div class="grid2"><div><div id="eB" class="btnrow"></div>
    <div class="readout"><div><small>Injections</small><strong id="t1"></strong></div><div><small>Withdrawals</small><strong id="t2"></strong></div><div><small>Equilibrium when</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 420 220" role="img" aria-label="The sectors included in the chosen economy"></svg></div></div></div>
'''

practise = '''
  <h2>1 · Injection or withdrawal?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the effect of a rise in exports in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("A rise in exports", "A car maker wins a big overseas order. Export spending is an injection, so firms hire more workers and pay more income; households spend more, and national income rises until withdrawals (saving, taxes and imports) have also risen to match.", "an injection raising national income.") +
rw("Households save more", "In a downturn households save more and spend less. Saving is a withdrawal, so unless investment or government spending rises to offset it, national income falls.", "a withdrawal lowering national income.") +
rw("A government infrastructure programme", "Spending on roads and rail is an injection (G). Firms and workers receive income and spend part of it, so national income rises, at least until higher taxes or imports leak out of the flow.", "government spending as an injection.") +
rw("A trade deficit", "Imports are higher than exports, so more is leaking out than flowing in from abroad. Unless savings are low or investment and government spending are high, the economy's income will tend to fall.", "the equilibrium condition and the open economy.")
)

mc_exam = [
  mcq("m23_12", 18, "Which statement about the circular flow of income is correct?", ["Exports and imports do not affect the equilibrium level of national income because they always cancel each other out", "The greater the level of saving, the greater the level of injections in the form of investment must be", "When consumers use past savings to increase their spending, there will be a rise in national income", "When a government increases withdrawals by increasing taxes, national income will rise"], 2, "More spending from past savings is an increase in consumption, so national income rises. Saving does not force investment to be larger, and higher taxes are a withdrawal."),
  mcq("m24_12", 17, "According to the circular flow of income, what would be the immediate result of an increase in the value of a country's exports?", ["imports would increase", "national income would increase", "savings would increase", "taxes would increase"], 1, "Exports are an injection, so national income rises immediately. Imports, saving and taxes rise only later as income grows."),
  mcq("s23_12", 21, "The diagram shows a basic two-sector circular flow of income, with the factor market and the product market between firms and households. What can be concluded about the direction of the flows?", ["Consumer expenditure flows anticlockwise", "Goods and services flow clockwise", "Incomes flow anticlockwise", "Resources flow anticlockwise"], 3, "In the standard diagram money flows clockwise (income to households, expenditure to firms) while real flows, such as resources, go the other way, anticlockwise."),
  mcq("s24_13", 17, "The table lists the values of the components of an economy's circular flow of income ($m): government spending 6, exports 8, investment 9, imports 7, saving 10, tax 5. What can be concluded about the economy from the information shown?", ["It has a budget surplus", "It has a trade deficit", "It is a mixed, open economy", "Its circular flow is in equilibrium"], 2, "It has a government sector and trade with abroad, so it is a mixed, open economy. G > T (deficit), X > M (surplus) and injections of 23 exceed withdrawals of 22, so not in equilibrium."),
  mcq("s25_12", 17, "Based on the circular flow of income, which condition is necessary for an open economy to be in equilibrium?", ["Government investment is equal to private investment", "Planned injections are equal to planned withdrawals", "Spending by households is equal to taxes collected by government", "Value of export earnings is equal to expenditure on imports"], 1, "Equilibrium requires I + G + X = S + T + M. Individual components need not match."),
  mcq("s25_11", 17, "An open economy with a government sector is in equilibrium. Households in this economy save $100 million and firms spend $150 million on investment. Which combination of the budget balance and the current account balance would lead to an equilibrium position?", ["$100m deficit and $50m deficit", "$100m deficit and $50m surplus", "$100m surplus and $50m deficit", "$100m surplus and $50m surplus"], 3, "S − I = −50, so (T − G) + (M − X) must equal +50. A budget surplus of 100 and a current account surplus of 50 (M − X = −50) satisfy 100 − 50 = 50.")
]

exam = exam_page("the circular flow of income",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). The circular flow is an 8 mark Paper 2 part most years, usually asking for a diagram, the move from a closed to an open economy and what the model says about growth. Reworded past questions are below, with six Paper 1 multiple choice questions.",
  [("Essay parts, 8 marks", "4", "Feb/March 2023 (22) Q4(a); May/June 2023 (23) Q4(a); May/June 2024 (22) Q4(a); May/June 2025 (21) Q4(a)"), ("Essay parts, 12 marks", "1", "May/June 2023 (23) Q4(b)"), ("Multiple choice (Paper 1)", "6 shown below", "2023 to 2025")],
  [
  eq(P("m23_22", "4(a)"), "8 marks", "Explain the circular flow of income in a closed economy and consider the extent to which the circular flow of income changes as an economy becomes an open economy.",
     ["Knowledge (up to 3): the circular flow in a closed economy involves households, firms and the government (1); injections of I and G and withdrawals of S and T (1); equilibrium income is where I + G = S + T (1).",
      "Analysis (up to 3): as the economy opens it takes part in the international economy (1) through the injection of X and the withdrawal of M (1), so equilibrium income becomes where I + G + X = S + T + M (1).",
      "Evaluation (up to 2): a judgement on the extent of the change, depending on the importance of net international trade (1), and a conclusion (1)."],
     "Closed: households, firms, government; I + G = S + T. Open: add X and M; I + G + X = S + T + M. Judge: depends on how important trade is.",
     [[("k", "In a closed economy income flows from firms to households as wages, rent, interest and profit, and returns as spending. The government collects taxes and spends. Injections are investment (I) and government spending (G), and withdrawals are saving (S) and taxes (T), so income is in equilibrium when I + G = S + T.")], [("n", "As an economy becomes open it trades with the rest of the world. Exports (X) are a new injection, and imports (M) a new withdrawal, so equilibrium is now where I + G + X = S + T + M.")], [("e", "The extent of the change depends on how important international trade is. For a small economy with exports and imports equal to a large share of GDP, the flow changes a lot, while for a large, mainly domestic economy the change is small. Net trade is what matters, since exports and imports may offset each other.")]]),
  eq(P("s25_21", "4(a)"), "8 marks", "Explain how the circular flow of income in an economy changes when that economy moves from a closed to an open economy and consider what determines the extent of this change.",
     ["Knowledge (up to 3): the way income flows around an economy from firms to households and back to firms (1); payments to factors of production in the form of income, profit and rent (1); payments from all these sources are spent on goods and services (1).",
      "Analysis (up to 3): closed economy injections of I and G and withdrawals of S and T; open economy adds spending on exports as an injection and spending on imports as a withdrawal. Maximum 2 if only a closed or only an open economy is considered, with no evaluation marks.",
      "Evaluation (up to 2): consideration of what determines the extent of the change, such as the size of trade relative to GDP, with a conclusion."],
     "Flow of income and spending. Closed: I, G, S, T. Open: add X and M. Extent depends on the size of the trade sector.",
     [[("k", "The circular flow shows income paid by firms to households for factors of production, spent again on goods and services, in a continuous process.")], [("n", "In a closed economy, injections are investment and government spending, and withdrawals are saving and taxes. In an open economy, exports are added to injections and imports to withdrawals, so international trade now affects national income.")], [("e", "The size of the change depends on how open the economy is, measured by trade as a share of GDP, and on the balance between exports and imports. Economies with large trade sectors change more than economies that mainly trade internally.")]]),
  eq(P("s24_22", "4(a)"), "8 marks", "With the help of a diagram, explain what is meant by the circular flow of income in an open economy and consider the extent to which it can explain economic growth in such an economy.",
     ["Knowledge (up to 3): a simple circular flow diagram (1) that shows separately that expenditure flows from households to firms (1) and income flows from firms to households (1).",
      "Analysis (up to 3): injections greater than withdrawals lead to economic growth and a rise in national income (1) and withdrawals greater than injections lead to a fall (1); reference to exports as an injection and imports as a leakage, along with at least one other injection and leakage (1).",
      "Evaluation (up to 2): how the relative sizes of injections and withdrawals lead either to growth or to a fall, with a justified conclusion (1)."],
     "Diagram. J > W: growth. W > J: fall. Include X and M. Judge: the model explains short-run changes in demand, not long-run growth in capacity.",
     [[("k", "The circular flow shows expenditure flowing from households to firms and income flowing from firms to households, with government and the international sector added in an open economy.")], [("n", "If injections (investment, government spending and exports) are greater than withdrawals (saving, taxes and imports), national income rises, which is economic growth. If withdrawals exceed injections, national income falls.")], [("e", "The model explains short-run changes in national income well, because they follow changes in spending, but it says little about what increases an economy's productive capacity, so it only partly explains long-run growth. A conclusion is that it explains demand-led growth but not supply-side growth.")]]),
  eq(P("s23_23", "4(a)"), "8 marks", "With the help of a circular flow of income diagram, explain how equilibrium is determined in an open economy and consider whether a budget deficit or a trade deficit is more likely to cause lasting disequilibrium.",
     ["Knowledge (up to 3): an accurate diagram showing income flows between firms and households (1); correct inclusion of exports and imports (1); correct inclusion of government spending and taxation (1).",
      "Analysis (up to 3): an explanation of injections (1), of leakages (1) and of how equilibrium is determined (1).",
      "Evaluation (up to 2): consideration of how a budget deficit or a trade deficit leads to disequilibrium (1) and of which is likely to cause lasting disequilibrium (1), with a justified conclusion."],
     "Diagram with X, M, G, T. Equilibrium: J = W. Budget or trade deficit: which lasts? Judge.",
     [[("k", "A diagram shows households and firms exchanging income and expenditure, with the government taking taxes and spending, and the international sector adding exports and removing imports.")], [("n", "Injections are investment, government spending and exports, and withdrawals are saving, taxes and imports. Equilibrium national income is where I + G + X = S + T + M, since if injections are larger income rises and if smaller it falls.")], [("e", "A budget deficit (G above T) adds more injections than withdrawals, which can be offset by private saving, while a trade deficit (M above X) is a net withdrawal that must be financed from abroad. A persistent trade deficit is probably more likely to cause lasting disequilibrium, because a country cannot borrow from abroad indefinitely, but a large budget deficit can also persist if the government can finance it.")]])
  ],
  )

tips = tips_html(
  [("Draw both flows.", "Income from firms to households; expenditure back."),
   ("Name injections and withdrawals.", "I, G, X in; S, T, M out."),
   ("Equilibrium: J = W.", "I + G + X = S + T + M."),
   ("Say what happens when they differ.", "J greater: income rises. W greater: it falls."),
   ("Closed to open adds X and M.", "Show the new injection and the new leakage."),
   ("Use examples.", "A rise in exports raises national income."),
   ("Evaluate with the size of trade.", "More open economies are affected more.")],
  [("Circular flow", "The circular flow of income shows income and expenditure moving between households and firms."),
   ("Injections", "Injections are investment, government spending and exports."),
   ("Withdrawals", "Withdrawals are saving, taxes and imports."),
   ("Equilibrium", "National income is in equilibrium when injections equal withdrawals."),
   ("Consider", "The change depends on the importance of trade in the economy.")],
  [CW["define"], CW["explain"], CW["consider"], CW["assess"]]) + FC

js = '''
/* ---------- circular flow ---------- */
function cfDraw(s) {
  const H = [270, 200, 150, 90], F = [270, 40, 150, 90]; // household box (x,y,w,h) and firm box
  let o = SV.rect(60, 120, 160, 60, "f1", op(0.5)) + SV.text(140, 156, "Households", "lbl bd", { "text-anchor": "middle" }) + SV.rect(540, 120, 160, 60, "f2", op(0.5)) + SV.text(620, 156, "Firms", "lbl bd", { "text-anchor": "middle" });
  o += SV.line(220, 135, 535, 135, "c2", { "stroke-width": 3 }) + SV.arrowHead(538, 135, "r", "dot2") + SV.text(380, 126, "Consumer expenditure", "sm", { "text-anchor": "middle" });
  o += SV.line(540, 168, 225, 168, "c1", { "stroke-width": 3 }) + SV.arrowHead(222, 168, "l", "dot1") + SV.text(380, 188, "Income (wages, rent, interest, profit)", "sm", { "text-anchor": "middle" });
  if (s.w > 0) o += SV.line(110, 182, 110, 250, "c3", { "stroke-width": 3, ...op(s.w) }) + SV.arrowHead(110, 254, "d", "dot3") + SV.text(110, 272, "Saving (S) to banks", "sm", { "text-anchor": "middle", ...op(s.w) }) + SV.line(160, 182, 160, 250, "c3", { "stroke-width": 3, ...op(s.w) }) + SV.arrowHead(160, 254, "d", "dot3") + SV.text(200, 290, "Taxes (T) to government", "sm", { "text-anchor": "middle", ...op(s.w) });
  if (s.i > 0) o += SV.line(560, 250, 560, 186, "c4", { "stroke-width": 3, ...op(s.i) }) + SV.arrowHead(560, 182, "u", "dot4") + SV.text(560, 272, "Investment (I)", "sm", { "text-anchor": "middle", ...op(s.i) }) + SV.line(620, 250, 620, 186, "c4", { "stroke-width": 3, ...op(s.i) }) + SV.arrowHead(620, 182, "u", "dot4") + SV.text(640, 290, "Government spending (G)", "sm", { "text-anchor": "middle", ...op(s.i) });
  if (s.x > 0) o += SV.line(660, 40, 660, 114, "c4", { "stroke-width": 3, ...op(s.x) }) + SV.arrowHead(660, 118, "d", "dot4") + SV.text(660, 30, "Exports (X) in", "sm", { "text-anchor": "middle", ...op(s.x) }) + SV.line(580, 118, 580, 44, "c3", { "stroke-width": 3, ...op(s.x) }) + SV.arrowHead(580, 40, "u", "dot3") + SV.text(560, 30, "Imports (M) out", "sm", { "text-anchor": "middle", ...op(s.x) });
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 300" role="img" aria-label="Households and firms exchange income and expenditure, with withdrawals and injections added">${cfDraw({ w: 1, i: 1, x: 1 })}</svg>`;
Lib.stepper($("#stC"), { w: 760, h: 300, label: "The circular flow from two sectors to an open economy", base: { w: 0, i: 0, x: 0 }, draw: cfDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>The basic flow.</b> Firms pay income to households for factors of production. Households spend it on goods and services, which becomes firms' revenue.", s: { w: 0 } },
  { cap: "<b>Withdrawals (leakages).</b> Households save some income (S) and pay taxes (T). These leave the flow and reduce spending.", s: { w: 1 } },
  { cap: "<b>Injections.</b> Firms invest (I) and the government spends (G). These add spending back into the flow.", s: { w: 1, i: 1 } },
  { cap: "<b>The open economy.</b> Exports (X) are a new injection and imports (M) a new withdrawal. Equilibrium: I + G + X = S + T + M.", s: { w: 1, i: 1, x: 1 } },
] });

/* ---------- injections and withdrawals bars ---------- */
function jwDraw(s) {
  const Y = (v) => 250 - v * 1.6; let o = SV.line(60, 250, 700, 250) + SV.line(60, 250, 60, 40) + SV.text(66, 34, "$bn", "sm");
  const stack = (x, parts, cols, lab) => { let y = 250; parts.forEach((p, i) => { const h = p * 1.6; o += SV.rect(x, y - h, 120, h, cols[i], op(0.7)) + SV.text(x + 60, y - h / 2 + 5, ["I", "G", "X"][i] === undefined ? "" : "", "sm"); y -= h; }); o += SV.text(x + 60, 270, lab, "lbl bd", { "text-anchor": "middle" }); };
  const J = [s.i, s.g, s.x], W = [s.s, s.t, s.m];
  let y = 250; J.forEach((p, k) => { const h = p * 1.6; o += SV.rect(180, y - h, 120, h, ["f2", "f3", "f1"][k], op(0.7)) + SV.text(240, y - h / 2 + 5, ["I " + Lib.fmtN(p, 0), "G " + Lib.fmtN(p, 0), "X " + Lib.fmtN(p, 0)][k], "lbl bd", { "text-anchor": "middle" }); y -= h; });
  y = 250; W.forEach((p, k) => { const h = p * 1.6; o += SV.rect(440, y - h, 120, h, ["f2", "f3", "f1"][k], op(0.7)) + SV.text(500, y - h / 2 + 5, ["S " + Lib.fmtN(p, 0), "T " + Lib.fmtN(p, 0), "M " + Lib.fmtN(p, 0)][k], "lbl bd", { "text-anchor": "middle" }); y -= h; });
  const jt = s.i + s.g + s.x, wt = s.s + s.t + s.m;
  o += SV.text(240, 270, "Injections " + Lib.fmtN(jt, 0), "lbl bd", { "text-anchor": "middle" }) + SV.text(500, 270, "Withdrawals " + Lib.fmtN(wt, 0), "lbl bd", { "text-anchor": "middle" });
  const d = jt - wt; o += SV.text(380, 60, Math.abs(d) < 1 ? "Equilibrium: injections = withdrawals" : d > 0 ? "Injections > withdrawals: national income rises" : "Withdrawals > injections: national income falls", "lbl bd", { "text-anchor": "middle", style: Math.abs(d) < 1 ? "fill:var(--good)" : "fill:var(--accent)" });
  return o;
}
$("#pic2").innerHTML = `<svg viewBox="0 0 760 290" role="img" aria-label="Bars of injections and withdrawals in equilibrium">${jwDraw({ i: 30, g: 30, x: 40, s: 30, t: 30, m: 40 })}</svg>`;
Lib.stepper($("#stE"), { w: 760, h: 290, label: "A rise in investment and the adjustment of withdrawals", base: { i: 30, g: 30, x: 40, s: 30, t: 30, m: 40 }, draw: jwDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>Equilibrium.</b> Injections (I 30 + G 30 + X 40 = 100) equal withdrawals (S 30 + T 30 + M 40 = 100). National income is stable.", s: { i: 30, g: 30, x: 40, s: 30, t: 30, m: 40 } },
  { cap: "<b>Investment rises by 20.</b> Injections are now 120, more than withdrawals of 100. Spending exceeds leakages, so national income rises.", s: { i: 50, g: 30, x: 40, s: 30, t: 30, m: 40 } },
  { cap: "<b>As national income rises</b> households save more, pay more tax and buy more imports. Withdrawals grow until they reach 120 and equal injections at a higher level of income.", s: { i: 50, g: 30, x: 40, s: 36, t: 36, m: 48 } },
] });

/* ---------- Lab 1 ---------- */
function labJ() {
  const ids = ["ii", "gg", "xx", "ss", "tt", "mm"]; if (!ids.every((i) => $("#" + i))) return;
  const v = ids.map((i) => +$("#" + i).value), [I, G, X, S, T, M] = v, J = I + G + X, W = S + T + M;
  $("#r1").textContent = J; $("#r2").textContent = W; $("#r3").textContent = Math.abs(J - W) < 1 ? "stay stable" : J > W ? "rise" : "fall";
  $("#rv").textContent = Math.abs(J - W) < 1 ? `Injections (${I} + ${G} + ${X} = ${J}) equal withdrawals (${S} + ${T} + ${M} = ${W}), so the circular flow is in equilibrium.` : `Injections are ${J} and withdrawals ${W}. ${J > W ? "More is injected than leaks out, so national income will rise" : "More leaks out than is injected, so national income will fall"} until withdrawals and injections are equal again. Budget balance (T − G) = ${T - G}; trade balance (X − M) = ${X - M}.`;
  $("#labA").innerHTML = jwDraw({ i: I, g: G, x: X, s: S, t: T, m: M });
}
[["g1", "ii", "Investment (I), $bn "], ["g2", "gg", "Government spending (G), $bn "], ["g3", "xx", "Exports (X), $bn "], ["g4", "ss", "Saving (S), $bn "], ["g5", "tt", "Taxes (T), $bn "], ["g6", "mm", "Imports (M), $bn "]].forEach(([el, id, lab]) => Lib.slider($("#" + el), { id, label: lab, min: 10, max: 60, step: 5, value: [30, 30, 40, 30, 30, 40][["ii", "gg", "xx", "ss", "tt", "mm"].indexOf(id)], fmt: (v) => v, onInput: labJ }));
labJ();

/* ---------- Lab 2 ---------- */
const ECO = [["Closed economy, no government", "I", "S", "I = S", "Only households and firms. Firms' investment is the only injection and household saving the only withdrawal."], ["Closed economy with government", "I + G", "S + T", "I + G = S + T", "The government adds spending (G) as an injection and taxes (T) as a withdrawal."], ["Open economy", "I + G + X", "S + T + M", "I + G + X = S + T + M", "Exports (X) are an injection from foreign buyers and imports (M) a withdrawal to foreign sellers."]];
function showE(i) {
  const [n, j, w, c, why] = ECO[i]; $$("#eB button").forEach((b, k) => b.classList.toggle("pri", k === i));
  $("#t1").textContent = j; $("#t2").textContent = w; $("#t3").textContent = c; $("#tv").textContent = n + ". " + why;
  const box = (x, y, t, k) => SV.rect(x, y, 120, 44, k, op(0.55)) + SV.text(x + 60, y + 27, t, "lbl bd", { "text-anchor": "middle" });
  $("#labB").innerHTML = box(40, 80, "Households", "f1") + box(260, 80, "Firms", "f2") + SV.line(160, 95, 258, 95, "c2", { "stroke-width": 3 }) + SV.line(260, 112, 162, 112, "c1", { "stroke-width": 3 }) + box(150, 10, "Banks (S, I)", "f3") + (i >= 1 ? box(150, 160, "Government (T, G)", "f2") : "") + (i >= 2 ? box(300, 160, "Rest of world (X, M)", "f1") : "");
}
$("#eB").innerHTML = ECO.map((e, i) => `<button class="b" data-i="${i}">${e[0]}</button>`).join("");
$$("#eB button").forEach((b) => (b.onclick = () => showE(+b.dataset.i)));
showE(2);

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Injection or withdrawal?", ["Injection", "Withdrawal"],
  [("Investment by firms", 0), ("Household saving", 1), ("Government spending", 0), ("Taxes", 1), ("Exports", 0), ("Imports", 1), ("A new road building programme", 0), ("A rise in the rate of income tax", 1)],
  "Injections: I, G, X. Withdrawals: S, T, M.") + MATCH([
  ["Circular flow", "Income and expenditure moving between households and firms"],
  ["Injection", "Spending added to the flow: I, G, X"],
  ["Withdrawal", "Income removed from the flow: S, T, M"],
  ["Equilibrium", "Injections equal withdrawals"],
  ["Open economy", "Trades with the rest of the world"],
  ["Closed economy", "No trade with the rest of the world"]]) + ORDER(
  "Put the effect of a rise in exports in order.",
  ["Overseas buyers increase spending on exports", "Injections exceed withdrawals", "Firms produce more and pay more income", "National income rises", "Saving, taxes and imports rise until withdrawals equal injections again"],
  "Higher injections raise national income until withdrawals catch up.") + CALC([
  {"q": "I = 60, G = 50, X = 40. What are total injections ($bn)?", "a": 150, "unit": "$bn", "tol": 0.5, "hint": "Add them.", "sol": "<b>$150bn</b>."},
  {"q": "S = 50, T = 45, M = 45. What are total withdrawals ($bn)?", "a": 140, "unit": "$bn", "tol": 0.5, "hint": "Add them.", "sol": "<b>$140bn</b>."},
  {"q": "With injections of 150 and withdrawals of 140, by how much do injections exceed withdrawals ($bn)?", "a": 10, "unit": "$bn", "tol": 0.5, "hint": "150 − 140.", "sol": "<b>$10bn</b>, so national income will rise."},
  {"q": "Government spending is $50bn and taxes $45bn. What is the budget balance? (deficit as a negative number)", "a": -5, "unit": "$bn", "tol": 0.5, "hint": "T − G.", "sol": "<b>−$5bn</b>, a budget deficit."}]) + MCQ([
  ("An injection into the circular flow is:", ["Exports", "Imports", "Saving", "Taxes"], 0, "Foreign spending on domestic output."),
  ("A withdrawal from the circular flow is:", ["Imports", "Investment", "Government spending", "Exports"], 0, "Spending leaving to other countries."),
  ("National income rises when:", ["Injections exceed withdrawals", "Withdrawals exceed injections", "Both equal zero", "Taxes fall"], 0, "More is added than leaks out."),
  ("The equilibrium condition for an open economy is:", ["I + G + X = S + T + M", "I = S", "G = T", "X = M only"], 0, "Total injections equal total withdrawals."),
  ("When an economy becomes open, the flow gains:", ["Exports and imports", "Saving and taxes", "Investment only", "Profits only"], 0, "A new injection and a new withdrawal.")
], "qz1") + CARDS([
  ("Circular flow", "Income and expenditure round."),
  ("Injections", "I, G, X."),
  ("Withdrawals", "S, T, M."),
  ("Equilibrium", "J = W."),
  ("J > W", "National income rises."),
  ("W > J", "National income falls."),
  ("Open economy", "Adds X and M."),
  ("Not required", "Multiplier, marginal propensities.")]) + MCQ(mc_exam)

build("as42", "as-circular-flow-of-income", "The Circular Flow of Income", EY,
  "4.2: the circular flow in closed and open economies, injections and withdrawals, and equilibrium and disequilibrium of national income. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
