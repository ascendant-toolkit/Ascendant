"""Syllabus 11.5.1 International aid. Run: python3 tools/artifact-kit/mk_sy1151.py"""
from syl import *
EY = "A Level Economics · 9708 · Syllabus 11.5.1"

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p><b class="kw">International aid</b> is the transfer of resources (money, goods, expertise) from governments, international organisations and charities to developing countries, on <b>concessional (easier than market) terms</b>. It comes in many <b>forms</b> (grants, soft loans, technical assistance, food and emergency aid; bilateral or multilateral; tied or untied), is given for <b>humanitarian, political and economic reasons</b>, and can raise growth by <b>filling the savings and foreign exchange gaps</b> and funding infrastructure, health and education. Its effects depend on how it is used, and critics argue that it can create <b>dependency, corruption, distortion and debt</b>.</p></div>

  <h2>1 · Forms of aid</h2>
  <div class="tw"><table class="t">
    <tr><th>Distinction</th><th>Types</th><th>Notes</th></tr>
    <tr><td><b>Source</b></td><td><b>Bilateral</b> (one government to another); <b>multilateral</b> (through the World Bank, UN agencies or regional banks); <b>NGOs and charities</b> (private)</td><td>Official aid (official development assistance, ODA) is from governments and agencies and must aim at development. Private charity or disaster relief from NGOs is not counted as official aid</td></tr>
    <tr><td><b>Form</b></td><td><b>Grants</b> (gifts, no repayment); <b>soft loans</b> (low interest, long repayment, grace periods); <b>technical assistance</b> (experts, training); <b>food aid and emergency relief</b>; <b>project</b> aid (a specific scheme) versus <b>programme or budget support</b></td><td>Grants do not add to debt; loans must be repaid</td></tr>
    <tr><td><b>Conditions</b></td><td><b>Tied aid</b> must be spent on the donor's goods and services; <b>untied aid</b> can be spent anywhere</td><td>Tying can raise costs by 15% to 30% or more and may serve the donor's exporters</td></tr>
  </table></div>

  <h2>2 · Why countries give aid</h2>
  <ul>
    <li><b>Humanitarian:</b> to relieve hunger, disease and disaster, and to reduce absolute poverty.</li>
    <li><b>Economic self-interest:</b> to create future markets and trading partners, secure supplies of raw materials, and reduce migration pressures. Tied aid directly supports the donor's exports.</li>
    <li><b>Political and strategic:</b> to gain allies, influence or access, and reflect historical ties.</li>
    <li><b>Global concerns:</b> to deal with shared problems such as pandemics, climate change and instability.</li>
    <li>The UN target is for high-income countries to give <b>0.7% of their gross national income</b> as aid. Few meet it, though several do.</li>
  </ul>

  <h2>3 · How aid can promote growth: the two gaps</h2>
  <div id="pic1" class="card"></div>
  <ul>
    <li><b>The savings gap:</b> a poor country has low saving, so it cannot fund the investment needed for growth. In the <b>Harrod-Domar</b> idea, growth = investment rate ÷ capital-output ratio. Aid can add to the investment funds.</li>
    <li><b>The foreign exchange gap:</b> a developing country needs to import capital goods and technology but earns little foreign currency. Aid provides foreign exchange to pay for them.</li>
    <li><b>Human capital and infrastructure:</b> aid spent on schools, health, roads, water and power raises productivity and potential output (an outward shift of the PPC and long-run aggregate supply).</li>
    <li><b>Emergency and food aid</b> saves lives in the short run and prevents the loss of human capital.</li>
  </ul>

  <h2>4 · Problems with aid</h2>
  <ul>
    <li><b>Dependency:</b> long-term reliance can weaken incentives for reform and local initiative, and over-reliance on technical assistance may crowd out local skills.</li>
    <li><b>Corruption and waste:</b> money may be diverted or spent on prestige projects, and weak governance reduces the benefit.</li>
    <li><b>Tied aid</b> raises the cost of projects and favours donor firms; <b>conditions</b> (privatisation, trade opening) may harm some groups.</li>
    <li><b>Distortion:</b> free food aid can lower local food prices and hurt local farmers; large inflows can raise the exchange rate (an aid version of Dutch disease).</li>
    <li><b>Debt:</b> loan aid must be repaid, so if it is poorly invested it adds to the debt burden.</li>
    <li><b>Unpredictability:</b> aid can be cut when donors' politics change, making planning hard.</li>
  </ul>
  <h3>The importance of aid</h3>
  <p>Aid matters most for the <b>poorest, least developed countries</b>, where it may be a large share of government spending and of foreign exchange. For emerging economies it is small relative to trade, investment and remittances. Evidence on its impact on growth is mixed: it works best in countries with sound institutions and when it funds health, education and infrastructure.</p>
  <div id="pic2" class="card"></div>
  <div class="tip"><b class="h">Evaluation point</b>Whether aid works depends on the type (grants for health versus tied loans), the recipient's governance, how it is spent and whether it is predictable. Alternatives such as trade access, debt relief, remittances and FDI may matter as much as aid.</div>
'''

watch = '''
  <h2>1 · How aid fills the savings gap</h2>
  <p>Press Play, or click the numbered steps.</p>
  <div id="stG"></div>
  <h2>2 · Routes aid takes</h2>
  <div id="stR"></div>
'''

explore = '''
  <h2>Lab 1 · The Harrod-Domar growth effect of aid</h2>
  <p>Growth = (domestic saving + aid) ÷ capital-output ratio, as a share of GDP. Set the saving rate, the aid inflow and the capital-output ratio.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div>
    <div class="readout"><div><small>Investment</small><strong id="r1"></strong></div><div><small>Growth without aid</small><strong id="r2"></strong></div><div><small>Growth with aid</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 300" role="img" aria-label="Bars of saving, aid and investment as a share of GDP and the growth rates with and without aid"></svg></div></div></div>

  <h2>Lab 2 · What is $100m of aid really worth?</h2>
  <p>Tying aid to the donor's goods raises costs, and corruption or waste leaks some of the money. See how much reaches the intended use.</p>
  <div class="card"><div class="grid2"><div><div id="g4"></div><div id="g5"></div>
    <div class="readout"><div><small>Cost premium</small><strong id="t1"></strong></div><div><small>Leakage</small><strong id="t2"></strong></div><div><small>Effective value</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 420 300" role="img" aria-label="Bars of the amount given and the effective value after tying and leakage"></svg></div></div></div>
'''

practise = '''
  <h2>1 · Which type of aid is it?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the chain from aid to growth in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("The 0.7% target", "In the 1970s the United Nations suggested that rich countries give 0.7% of their gross national income as aid. A handful of countries, mostly in northern Europe, meet or exceed it, while many of the largest economies give a much smaller share of income, though not necessarily a small amount in absolute dollars.", "the importance and scale of aid, and the difference between the amount and the share of income.") +
rw("Tied aid and health supplies", "When aid for health care must be spent on the donor's own medicines, recipients may pay more than they would for cheaper generic drugs from other countries. Tying can therefore reduce the number of people treated per dollar of aid.", "tied aid as a cost to the recipient and a benefit to donor exporters.") +
rw("Emergency aid after disasters", "After an earthquake or flood, food, shelter and medical teams from governments, UN agencies and charities arrive quickly. This saves lives, but long-term rebuilding depends on grants and loans for infrastructure and on local capacity.", "emergency aid versus long-term development aid.") +
rw("Aid and local farmers", "When large amounts of free food are shipped in, local grain prices can fall and farmers lose income, which may reduce local production. Aid agencies now often buy food locally or give cash to avoid this distortion.", "unintended effects of aid on local markets.")
)

mc_exam = [
  ("Money given by the US government to certain African countries to fight HIV/AIDS requires their governments to buy expensive US drugs rather than cheaper ones from South Africa, India or Brazil. What is this an example of? (Oct/Nov 2021 · 31 · Q28, reworded)", ["Bilateral aid", "Debt relief", "Multilateral aid", "Tied aid"], 3, "Tied aid must be spent on the donor's own goods, which can raise costs for the recipient."),
  ("Some conditions for providing foreign aid to low-income countries are restrictive. Which kind of aid fits this description? (Oct/Nov 2024 · 31 · Q28, reworded)", ["Food aid after natural disasters such as drought", "Grants tied to buying donor country goods", "Loans repaid over a long period at a low rate of interest", "Technical assistance using highly skilled workers"], 1, "Tying the grant to purchases from the donor limits how the recipient can spend it."),
  ("A developing country receiving foreign financial aid is most likely to grow in the long run if it uses the money to: (Oct/Nov 2020 · 33 · Q18, reworded)", ["Boost welfare benefits for the poorest households", "Pay for imports of capital goods", "Reduce environmental pollution", "Reduce income tax for all households"], 1, "Capital goods raise productive capacity, which raises long-run growth. The others are worthwhile but raise consumption or reduce external costs rather than capacity."),
  ("Why is disaster relief money sent by non-governmental organisations to a South American country not classified as official foreign aid? (Oct/Nov 2022 · 32 · Q20, reworded)", ["It does not finance a long-term investment programme", "It does not incur interest", "It is not supplied by a government", "Only countries in Asia and Africa count as developing"], 2, "Official aid is government or agency aid. Private charity is outside it."),
  ("The table shows GNI and foreign aid spending in 2016: Belgium $468.9bn and $2.10bn; Germany $3,612.1bn and $23.84bn; Sweden $532.7bn and $5.38bn; South Korea $1,403.6bn and $2.10bn. What can be concluded? (Oct/Nov 2020 · 32 · Q19, reworded)", ["Countries with higher GNI always spend more on aid", "Germany spends the most on aid in the world", "South Korea and Belgium give an equal share of GNI", "Sweden gave the highest share of GNI"], 3, "Aid as a share of GNI: Sweden about 1.0%, Germany 0.66%, Belgium 0.45%, South Korea 0.15%."),
  ("Some economists argue there is little evidence of the value of aid in improving development. Which situation supports this claim? (Feb/March 2025 · 32 · Q30, reworded)", ["Greater capacity to benefit from communications technology", "Investment in infrastructure creating transport links and ports", "Over-reliance on technical assistance impairing local initiative and innovation", "Education and training projects improving the supply side"], 2, "Dependence on outside experts is a way that aid can undermine local capacity. The others are benefits."),
  ("Middle Eastern countries want to help low-income countries to grow. Which policy would be least likely to achieve this? (Feb/March 2023 · 32 · Q19, reworded)", ["Writing off debts to ease foreign exchange shortages", "Financing clean water capital projects through aid", "Hiring mainly labour from low-income countries to build infrastructure in the Middle East", "Cutting fuel exports to low-income countries to reduce pollution"], 3, "Cutting the fuel supply would raise energy costs and slow growth. The other three raise capacity or income."),
  ("Which items are classified as foreign aid? Foreign direct investment, official development assistance, portfolio investment flows. (May/June 2022 · 31 · Q27, reworded)", ["Foreign direct investment only", "Official development assistance only", "Official development assistance and portfolio investment", "Foreign direct investment and portfolio investment"], 1, "Only official development assistance is aid. Investment flows are commercial.")
]

exam = exam_page("international aid: forms, reasons, effects and importance",
  "We searched the A Level Economics papers in the folder (2020 to 2025). No full Paper 4 question was set on aid in these papers, although aid appears in 25 mark discussions of development and trade, and in Paper 3 multiple choice every year. Below are two practice questions in the Paper 4 style with model answers, and eight Paper 3 multiple choice questions.",
  [("Paper 4 (no stand-alone question found)", "0", "Practice questions below"), ("Multiple choice (Paper 3)", "8 shown below", "2020 to 2025")],
  [
  eq("Practice question · modelled on the 12 mark style (no past paper)", "12 marks", "Explain the main forms of aid and consider whether aid is likely to promote development in a low-income country.",
     ["Forms: grants, soft loans, technical assistance, food and emergency aid; bilateral or multilateral; tied or untied; project or programme aid.",
      "Benefits: fills the savings and foreign exchange gaps, funds infrastructure, health and education, raising productive capacity.",
      "Drawbacks: dependency, corruption, tied aid costs, distortion of local markets, debt (if loans).",
      "Judgement: depends on type, governance and use of the aid."],
     "Forms. How aid helps (two gaps). Problems. Judgement.",
     [[("k", "Aid takes several forms. Grants are gifts, soft loans have low interest and long repayment, technical assistance provides experts and training, and food and emergency aid meet urgent needs. Aid can be bilateral from one government or multilateral through bodies such as the World Bank, and it can be tied to purchases from the donor."), ("n", "Aid could promote development by filling the savings gap, since investment in schools, health, roads and power raises productivity and potential output. It also supplies foreign exchange for imports of capital goods, which may raise growth by increasing investment.")],
      [("n", "However, aid may create dependency and weaken local initiative. Tied aid may raise costs, and corruption may divert funds. Free food could lower prices and harm local farmers, and loans may add to the debt burden."), ("e", "Overall, aid is likely to promote development when it is given as grants, spent on infrastructure, health and education, and where governance is sound. If it is tied or poorly used, the benefit may be small.")]]),
  eq("Practice question · modelled on the 8 mark style (no past paper)", "8 marks", "Explain two reasons why high-income countries give aid to low-income countries.",
     ["Humanitarian reason with development: to reduce poverty and relieve suffering, which also supports longer-term stability.",
      "Economic or political self-interest with development: future markets and trade partners, access to raw materials, reducing migration pressure, strategic alliances.",
      "Each reason explained with a short chain of analysis."],
     "Reason 1: humanitarian. Reason 2: economic or political. Explain each.",
     [[("k", "One reason is humanitarian. Governments and their voters may want to reduce absolute poverty and respond to hunger, disease and disasters."), ("n", "Helping poor countries grow could also reduce conflict and the spread of disease, which benefits donors in the longer term.")],
      [("k", "A second reason is economic self-interest."), ("n", "Aid, especially tied aid, can create markets for the donor's exports and help recipient countries become richer trading partners. A richer neighbour may also reduce pressures to migrate, which may benefit the donor.")]])
  ],
  )

tips = tips_html(
  [("Split the forms.", "Grants or loans, tied or untied, bilateral or multilateral, emergency or long-term."),
   ("Give two types of reason.", "Humanitarian and self-interest (economic or political)."),
   ("Use the two gaps.", "Savings gap and foreign exchange gap link aid to investment and growth."),
   ("Say what the aid is spent on.", "Capital goods, health and education may raise long-run growth. Consumption may not."),
   ("Always include costs.", "Dependency, corruption, tied aid, distortion of local markets and debt."),
   ("Judge with conditions.", "Aid works better with good governance, grants and untied funding."),
   ("Mention alternatives.", "Trade access, FDI, debt relief and remittances can matter as much.")],
  [("Forms", "Aid may take the form of grants, soft loans, technical assistance or emergency relief."),
   ("Tied", "Tied aid could raise the cost of projects because the recipient must buy goods from the donor."),
   ("Gaps", "Aid may fill the savings gap and foreign exchange gap, which could allow higher investment."),
   ("Costs", "Aid might create dependency and could be diverted by corruption."),
   ("Judge", "The impact of aid may depend on how it is used and on the quality of governance.")],
  [CW["define"], CW["explain"], CW["consider"], CW["evaluate"]]) + FC

js = '''
/* ---------- Savings gap ---------- */
const GY = (v) => 300 - v * 8.5;
function gapDraw(s) {
  let o = axes(70, 300, 730, 30, "", "% of GDP"); [0, 10, 20, 30].forEach((v) => (o += SV.text(64, GY(v) + 4, v, "sm", { "text-anchor": "end" })));
  const bx = (x, v, y0, c, l, k) => (k > 0 ? SV.rect(x, GY(y0 + v * k), 100, v * k * 8.5, c, op(0.75)) + tag(x + 50, GY(y0 + v * k) - 6, l + " " + Lib.fmtN(v, 0) + "%", "t1", 1, "middle") : "");
  o += SV.rect(120, GY(25), 100, 25 * 8.5, "f2", op(0.2)) + SV.line(120, GY(25), 220, GY(25), "c2 dash") + tag(170, GY(25) - 6, "needed: 25%", "t2", s.a, "middle");
  o += bx(300, 12, 0, "f1", "Saving", s.a);
  if (s.b > 0) o += bx(300, 13, 12, "f3", "Aid", s.b);
  if (s.c > 0) o += tag(560, 80, "Growth = investment ÷ capital-output ratio (4)", "t4", s.c, "middle") + tag(560, 106, "Without aid: 12 ÷ 4 = 3% a year", "t1", s.c, "middle") + tag(560, 132, "With aid: 25 ÷ 4 = 6.25% a year", "t3", s.c, "middle");
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 760 345" role="img" aria-label="Investment needed of 25 percent of GDP, domestic saving of 12 percent and an aid-funded gap of 13 percent">${gapDraw({ a: 1, b: 1, c: 1 })}</svg>`;
Lib.stepper($("#stG"), { w: 760, h: 345, label: "A savings gap filled by aid and the effect on growth", base: { a: 0, b: 0, c: 0 }, draw: gapDraw, tween: 1200, dwell: 5800, steps: [
  { cap: "<b>The target.</b> To grow at about 6% a year with a capital-output ratio of 4, the economy needs to invest about 25% of GDP.", s: { a: 1 } },
  { cap: "<b>Domestic saving</b> is only 12% of GDP, because incomes are low and little is left over after meeting basic needs.", s: { a: 1 } },
  { cap: "<b>Aid fills the gap.</b> An aid inflow worth 13% of GDP, used for investment, brings total funds up to 25%.", s: { a: 1, b: 1 } },
  { cap: "<b>Growth.</b> Investment of 25% ÷ capital-output ratio 4 gives growth of about 6.25% a year, compared with 3% without aid, provided the aid is invested well.", s: { a: 1, b: 1, c: 1 } },
] });

/* ---------- Routes of aid ---------- */
function routeDraw(s) {
  const box = (x, y, w, t, c, k) => (k > 0 ? SV.rect(x, y, w, 48, c, op(0.5 * k)) + SV.text(x + w / 2, y + 30, t, "lbl bd", { "text-anchor": "middle", ...op(k) }) : "");
  let o = box(40, 130, 150, "Donor government", "f1", 1) + box(570, 130, 150, "Recipient country", "f3", 1);
  const ar = (x1, y1, x2, y2, k, t, ty) => (k > 0 ? SV.line(x1, y1, x2, y2, "c1", { "stroke-width": 2.5, ...op(k) }) + SV.arrowHead(x2, y2, "r", "dot1") + tag((x1 + x2) / 2, ty, t, "t1", k, "middle") : "");
  o += ar(190, 154, 570, 154, s.a, "Bilateral aid (grants, loans, technical help)", 144);
  if (s.b > 0) o += box(290, 40, 180, "World Bank / UN agencies", "f2", s.b) + ar(190, 140, 290, 70, s.b, "", 90) + ar(470, 70, 570, 140, s.b, "Multilateral aid", 80);
  if (s.c > 0) o += box(290, 240, 180, "NGOs and charities", "f2", s.c) + ar(190, 170, 290, 262, s.c, "Donations and grants", 230) + ar(470, 262, 570, 172, s.c, "Emergency and local projects", 244);
  if (s.d > 0) o += tag(380, 118, "TIED: must buy from the donor", "t2", s.d, "middle") + SV.rect(575, 190, 140, 34, "f2", op(0.4 * s.d)) + tag(645, 212, "Higher project costs", "t2", s.d, "middle");
  return o;
}
$("#pic2").innerHTML = `<svg viewBox="0 0 760 310" role="img" aria-label="Aid flowing from a donor government to a recipient directly, via multilateral agencies and via NGOs">${routeDraw({ a: 1, b: 1, c: 1, d: 0 })}</svg>`;
Lib.stepper($("#stR"), { w: 760, h: 310, label: "Aid routes: bilateral, multilateral and through NGOs, and the effect of tying", base: { a: 0, b: 0, c: 0, d: 0 }, draw: routeDraw, tween: 1000, dwell: 5600, steps: [
  { cap: "<b>Bilateral aid</b> goes directly from one government to another as grants, soft loans or technical assistance.", s: { a: 1 } },
  { cap: "<b>Multilateral aid</b> is pooled through organisations such as the World Bank and UN agencies, which decide how to spend it.", s: { a: 1, b: 1 } },
  { cap: "<b>NGOs and charities</b> channel private donations and some government funds into emergency relief and local projects. Private charity is not counted as official aid.", s: { a: 1, b: 1, c: 1 } },
  { cap: "<b>Tying.</b> If bilateral aid must be spent on the donor's goods, the recipient loses the chance to buy more cheaply elsewhere, so the same money does less.", s: { a: 1, b: 1, c: 1, d: 1 } },
] });

/* ---------- Lab 1 ---------- */
function labA() {
  if (!$("#sv") || !$("#ai") || !$("#ko")) return;
  const sv = +$("#sv").value, ai = +$("#ai").value, k = +$("#ko").value / 10, inv = sv + ai, g0 = sv / k, g1 = inv / k;
  $("#r1").textContent = Lib.fmtN(inv, 0) + "% of GDP"; $("#r2").textContent = Lib.fmtN(g0, 1) + "%"; $("#r3").textContent = Lib.fmtN(g1, 1) + "%";
  $("#rv").textContent = ai === 0 ? `With no aid, investment equals saving (${sv}% of GDP) and growth is ${sv} ÷ ${Lib.fmtN(k, 1)} = ${Lib.fmtN(g0, 1)}% a year.` : `Aid of ${ai}% of GDP lifts investment from ${sv}% to ${inv}% of GDP. With a capital-output ratio of ${Lib.fmtN(k, 1)}, growth rises from ${Lib.fmtN(g0, 1)}% to ${Lib.fmtN(g1, 1)}% a year. This assumes all the aid is invested productively, which is the key limit of the model.`;
  const Y = (v) => 270 - v * 6; let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(46, 16, "% of GDP, % a year", "sm");
  [["Saving", sv, "f1"], ["Aid", ai, "f3"], ["Growth, no aid", g0, "f1"], ["Growth, aid", g1, "f3"]].forEach(([l, v, c], i) => { const x = 55 + i * 85; o += SV.rect(x, Y(Math.min(v, 40)), 60, 270 - Y(Math.min(v, 40)), c) + SV.text(x + 30, 290, l, "sm", { "text-anchor": "middle" }) + tag(x + 30, Y(Math.min(v, 40)) - 6, Lib.fmtN(v, 1), "t1", 1, "middle"); });
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "sv", label: "Domestic saving, % of GDP ", min: 5, max: 25, step: 1, value: 12, fmt: (v) => v + "%", onInput: labA });
Lib.slider($("#g2"), { id: "ai", label: "Aid invested, % of GDP ", min: 0, max: 15, step: 1, value: 6, fmt: (v) => v + "%", onInput: labA });
Lib.slider($("#g3"), { id: "ko", label: "Capital-output ratio ", min: 20, max: 60, step: 5, value: 40, fmt: (v) => (v / 10).toFixed(1), onInput: labA });
labA();

/* ---------- Lab 2 ---------- */
function labE() {
  if (!$("#tp") || !$("#lk")) return;
  const p = +$("#tp").value / 100, l = +$("#lk").value / 100, eff = 100 * (1 - l) / (1 + p);
  $("#t1").textContent = "+" + Lib.fmtN(p * 100, 0) + "%"; $("#t2").textContent = Lib.fmtN(l * 100, 0) + "%"; $("#t3").textContent = "$" + Lib.fmtN(eff, 1) + "m";
  $("#tv").textContent = `Of $100m of aid, ${Lib.fmtN(l * 100, 0)}% leaks away, leaving $${Lib.fmtN(100 * (1 - l), 0)}m. If the tied goods cost ${Lib.fmtN(p * 100, 0)}% more than on the open market, that $${Lib.fmtN(100 * (1 - l), 0)}m buys only what $${Lib.fmtN(eff, 1)}m would buy: an effective value of ${Lib.fmtN(eff, 1)}% of the nominal figure.`;
  const Y = (v) => 270 - v * 2.3; let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 20) + SV.text(46, 16, "$m", "sm");
  [["Given", 100, "f1"], ["After leakage", 100 * (1 - l), "f2"], ["Effective value", eff, "f3"]].forEach(([lab, v, c], i) => { const x = 60 + i * 115; o += SV.rect(x, Y(v), 80, 270 - Y(v), c) + SV.text(x + 40, 290, lab, "sm", { "text-anchor": "middle" }) + tag(x + 40, Y(v) - 6, Lib.fmtN(v, 1), "t1", 1, "middle"); });
  $("#labB").innerHTML = o;
}
Lib.slider($("#g4"), { id: "tp", label: "Extra cost of tied goods, % ", min: 0, max: 40, step: 1, value: 25, fmt: (v) => v + "%", onInput: labE });
Lib.slider($("#g5"), { id: "lk", label: "Leakage through waste or corruption, % ", min: 0, max: 40, step: 1, value: 10, fmt: (v) => v + "%", onInput: labE });
labE();

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Which type of aid is it?", ["Grant or soft loan", "Technical assistance", "Emergency or food aid", "Tied aid"],
  [("A gift of $50m for rural schools with no repayment", 0), ("Experts sent to help a ministry reform tax collection", 1), ("Food and tents sent after a flood", 2), ("A loan that must be spent on the donor's engineering firms", 3), ("A 40-year loan at 0.5% interest", 0), ("Teaching teams train local nurses", 1), ("Medical supplies flown in after an earthquake", 2), ("A grant that can be used only to buy the donor's drugs", 3)],
  "Grants and soft loans are financial; technical help is expertise; emergency aid meets urgent needs; tied aid is limited to donor goods.") + MATCH([
  ["Bilateral aid", "Aid from one government directly to another"],
  ["Multilateral aid", "Aid pooled and channelled through international bodies"],
  ["Tied aid", "Aid that must be spent on the donor's goods and services"],
  ["Official development assistance", "Government aid to promote development on concessional terms"],
  ["Savings gap", "Shortage of domestic saving to fund the investment needed for growth"],
  ["Foreign exchange gap", "Shortage of foreign currency to pay for imports of capital goods"]]) + ORDER(
  "Put the chain from aid to growth in order.",
  ["Aid is received and invested in infrastructure and schools", "The savings and foreign exchange gaps narrow", "Investment and human capital rise", "Productive capacity (potential output) rises", "Growth and living standards may improve"],
  "Aid helps growth only if it is invested productively.") + CALC([
  {"q": "A donor gives $24bn of aid and its GNI is $3,600bn. Calculate aid as a percentage of GNI (2 decimal places).", "a": 0.67, "unit": "%", "tol": 0.01, "hint": "24 ÷ 3,600 × 100.", "sol": "<b>0.67%</b>, close to but below the UN target of 0.7%."},
  {"q": "Saving is 15% of GDP and the capital-output ratio is 3. Calculate the growth rate with no aid (%).", "a": 5, "unit": "%", "tol": 0.05, "hint": "15 ÷ 3.", "sol": "<b>5%</b>."},
  {"q": "Aid worth 6% of GDP is invested as well. Using the same figures, calculate the new growth rate (%).", "a": 7, "unit": "%", "tol": 0.05, "hint": "(15 + 6) ÷ 3.", "sol": "21 ÷ 3 = <b>7%</b>."},
  {"q": "A $100m tied aid package costs 25% more than the same goods on the open market and 10% is lost to waste. Calculate the effective value ($m).", "a": 72, "unit": "$m", "tol": 0.5, "hint": "100 × 0.9 ÷ 1.25.", "sol": "90 ÷ 1.25 = <b>$72m</b>."}]) + MCQ([
  ("Tied aid is aid that:", ["Must be spent on goods from the donor", "Has to be repaid in a year", "Is given to a company", "Is only for emergencies"], 0, "The recipient has less freedom to choose cheaper suppliers."),
  ("Which is a possible benefit of aid?", ["Funding for infrastructure, health and education", "Guaranteed zero debt", "Lower birth rates in every case", "A fall in the exchange rate"], 0, "Productive spending can raise potential output."),
  ("A disadvantage of food aid is that it may:", ["Lower local food prices and hurt local farmers", "Raise the price of capital goods", "Increase interest rates", "Reduce imports of oil"], 0, "Local producers face competition from free supplies."),
  ("The UN target for aid from high-income countries is:", ["0.7% of GNI", "7% of GNI", "0.07% of GNI", "20% of exports"], 0, "The 0.7% of GNI target has been met by few countries."),
  ("Which is least likely to be official foreign aid?", ["A donation by a charity after a flood", "A government grant for schools", "A soft loan from the World Bank", "Technical assistance from a government agency"], 0, "Official aid comes from governments and agencies.")
], "qz1") + CARDS([
  ("Bilateral aid", "Government to government."),
  ("Multilateral aid", "Through the World Bank or UN."),
  ("Tied aid", "Spent on donor's goods."),
  ("Grant", "A gift; no repayment."),
  ("Soft loan", "Low interest, long term."),
  ("Savings gap", "Too little saving to fund investment."),
  ("Foreign exchange gap", "Too little foreign currency for imports."),
  ("0.7% target", "UN aid target as share of GNI.")]) + MCQ(mc_exam)

build("sy1151", "international-aid", "International Aid: Forms, Reasons and Effects", EY,
  "11.5.1: the forms of aid, why countries give it, how it can raise growth through the savings and foreign exchange gaps, and why it sometimes fails. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
