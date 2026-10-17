"""AS syllabus 1.3.1-1.3.3 Factors of production, human and physical capital, rewards. Run: python3 tools/artifact-kit/mk_as13.py"""
from asx import *
EY = EYAS("1.3.1 to 1.3.3")

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>The <b class="kw">factors of production</b> are the resources used to make goods and services: <b>land</b> (natural resources), <b>labour</b> (human effort), <b>capital</b> (human-made goods used in production) and <b>enterprise</b> (organising the other factors and bearing risk). Capital can be <b class="kw">physical</b> (machines, buildings) or <b class="kw">human</b> (the knowledge and skills of workers). Each factor earns a reward: <b>rent</b> for land, <b>wages</b> for labour, <b>interest</b> for capital and <b>profit</b> for enterprise, and profit is what is left after the other rewards are paid, so it can be negative.</p></div>

  <h2>1 · The four factors of production (1.3.1)</h2>
  <div id="pic1" class="card"></div>
  <div class="tw"><table class="t">
    <tr><th>Factor</th><th>Definition</th><th>Examples</th><th>Not included</th></tr>
    <tr><td><b>Land</b></td><td>All natural resources, "gifts of nature", used in production</td><td>Farmland, forests, fish stocks, oil, minerals (including undiscovered ones), water</td><td>Buildings or machinery on the land</td></tr>
    <tr><td><b>Labour</b></td><td>The physical and mental effort of people in production</td><td>Factory workers, teachers, doctors, software developers</td><td>Unpaid leisure activities</td></tr>
    <tr><td><b>Capital</b></td><td>Human-made resources used to produce other goods and services</td><td>Machines, ovens, factories, tools, aeroplanes, roads and computers</td><td><b>Money, shares and loans</b> (this is financial capital, which pays for factors but is not itself a factor)</td></tr>
    <tr><td><b>Enterprise</b></td><td>The entrepreneur's role in <b>organising</b> the other factors and <b>taking the risk</b> of production</td><td>The founder of a start-up, the owner-manager of a restaurant</td><td>Hired managers who bear no risk of loss</td></tr>
  </table></div>
  <ul>
    <li>All factors are <b>scarce</b>, which is the source of the economic problem. Their <b>quantity and quality</b> determine how much an economy can produce.</li>
    <li><b>Enterprise is needed first</b> to set up a new business: someone must decide to combine the other factors and accept the risk.</li>
    <li>A business expansion usually involves all four: for example a bakery needs a site (land), staff (labour), ovens (capital) and an owner who takes the risk (enterprise). Raising money from shareholders is not a factor of production; it is how the capital is financed.</li>
  </ul>

  <h2>2 · Human capital and physical capital (1.3.2)</h2>
  <div id="pic2" class="card"></div>
  <div class="tw"><table class="t">
    <tr><th></th><th>Physical capital</th><th>Human capital</th></tr>
    <tr><td><b>Meaning</b></td><td>Man-made goods used in production</td><td>The qualities, <b>knowledge and skills</b> that make a worker more productive</td></tr>
    <tr><td><b>Examples</b></td><td>Machinery, factories, vehicles, computers, infrastructure</td><td>Education, training, apprenticeships, work experience, health</td></tr>
    <tr><td><b>How it is built</b></td><td>Investment in equipment and buildings</td><td>Spending on schools, training and health care</td></tr>
    <tr><td><b>Effect</b></td><td>Raises output per worker; wears out (depreciates)</td><td>Raises productivity and adaptability; it is embodied in people and moves with them</td></tr>
  </table></div>
  <ul>
    <li>Both raise <b>productivity</b> (output per worker) and the productive potential of the economy. They often work together: a skilled worker gets more from a machine.</li>
    <li>A country that spends more on education but taxes imports of machinery may increase human capital while physical capital grows more slowly.</li>
  </ul>

  <h2>3 · Rewards to the factors of production (1.3.3)</h2>
  <div class="tw"><table class="t">
    <tr><th>Factor</th><th>Reward</th><th>What it is</th></tr>
    <tr><td><b>Land</b></td><td><b>Rent</b></td><td>Payment for the use of land and natural resources</td></tr>
    <tr><td><b>Labour</b></td><td><b>Wages</b> (and salaries)</td><td>Payment for work done</td></tr>
    <tr><td><b>Capital</b></td><td><b>Interest</b></td><td>Payment for the use of capital (or the funds that buy it)</td></tr>
    <tr><td><b>Enterprise</b></td><td><b>Profit</b></td><td>The surplus after all other costs are paid: the <b>residual</b>, and the reward for taking risk</td></tr>
  </table></div>
  <ul>
    <li>Profit is different from the other rewards: rent, wages and interest are <b>contractual</b> (agreed in advance), whereas profit is <b>uncertain</b> and may be zero or <b>negative (a loss)</b>. This is why the share of income from profit varies more over time than the shares of rent, wages and interest.</li>
    <li>In a modern economy ownership and control are often separate (shareholders own, managers control), but profit still rewards the risk of those who own the business.</li>
    <li>Rewards depend on the <b>supply</b> and <b>demand</b> for each factor: scarce, productive factors earn more.</li>
  </ul>
  <div class="tip"><b class="h">Exam tip</b>Do not list money or shares as capital. Capital in economics means <b>real</b> things used to produce, such as machines, and its reward is <b>interest</b>. Profit belongs to enterprise.</div>
'''

watch = '''
  <h2>1 · From factors to rewards</h2>
  <p>Press Play, or click the numbered steps. A bakery brings the four factors together.</p>
  <div id="stF"></div>
  <h2>2 · Human capital and physical capital</h2>
  <div id="stH"></div>
'''

explore = '''
  <h2>Lab 1 · Who gets paid, and what is left for enterprise?</h2>
  <p>A business earns revenue and pays rent, wages and interest first. What is left is profit, the reward for enterprise. Change the numbers and see profit become a loss.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div><div id="g4"></div>
    <div class="readout"><div><small>Costs paid first</small><strong id="r1"></strong></div><div><small>Profit (residual)</small><strong id="r2"></strong></div><div><small>Profit as % of revenue</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 300" role="img" aria-label="Stacked bar of revenue split into wages, rent, interest and profit or loss"></svg></div></div></div>

  <h2>Lab 2 · Skills and machines work together</h2>
  <p>Output per worker depends on the worker's training (human capital) and the machines available (physical capital). Set both and see the output. Notice that together they give more than the sum of each on its own.</p>
  <div class="card"><div class="grid2"><div><div id="g5"></div><div id="g6"></div>
    <div class="readout"><div><small>Output per worker</small><strong id="t1"></strong></div><div><small>From training</small><strong id="t2"></strong></div><div><small>From machines + teamwork</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 420 300" role="img" aria-label="Bars of the base output and the extra output from training and from machines"></svg></div></div></div>
'''

practise = '''
  <h2>1 · Which factor of production?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the factor to its reward</h2><div id="m1" class="card"></div>
  <h2>3 · Put the steps for setting up a bakery in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Apprenticeships and human capital", "Many countries run apprenticeship schemes that combine work and study. The trainee earns a lower wage while learning, and later earns more because the skills raise productivity. The employer, the worker and the economy gain from the extra human capital.", "human capital as an investment that raises productivity and later wages.") +
rw("Robots in a car factory", "A car plant that replaces assembly workers with robots uses more physical capital and less labour per car. Output per worker rises, but workers need new skills to program and maintain the machines, so human capital matters too.", "physical capital raising productivity and its link with human capital.") +
rw("A start-up and its founder", "A founder who starts an online shop organises the website, suppliers and staff and puts in savings. If sales are poor she bears the loss, and if sales boom she keeps the profit. Wages, rent and software licences must be paid either way.", "enterprise as risk-taking and profit as the residual reward.") +
rw("Oil-rich land", "A country with large oil reserves has valuable land in the economist's sense. Companies pay rent or royalties to the government or owners to extract it. The reserves are natural resources, whereas the rigs and pipelines are capital.", "the difference between land (natural resources) and capital (man-made equipment).")
)

mc_exam = [
  mcq("w21_11", 1, "A European airline opens a new route. It buys aeroplanes, rents landing slots, hires pilots and buys back some shares. What is an example of the factor of production capital?", ["Aeroplanes", "Landing slots", "Pilots", "Shares"], 0, "Aeroplanes are human-made resources used in production. Pilots are labour; shares are financial assets."),
  mcq("w21_12", 4, "Which statement about the factors of production is correct?", ["The factor capital includes shares and deposit accounts at banks", "The factor labour includes human-made resources", "The factor land includes forests and undiscovered copper", "The factor enterprise takes risks and is rewarded with interest"], 2, "Land is all natural resources, whether or not they have been discovered. Enterprise is rewarded with profit, and capital excludes financial assets."),
  mcq("s21_13", 10, "A UK food company diversifying its range borrows $10m from a bank to buy land, build and equip a bakery. What would an economist not classify as a factor of production?", ["The $10m loan", "The land on which the bakery is built", "The ovens", "The soya used to make bread"], 0, "The loan is money, which pays for factors but is not itself a factor. Land, ovens and the raw material are resources."),
  mcq("s22_13", 4, "Which term assumes the existence of 'qualities, knowledge and skills' that allow an individual to be more productive?", ["Enterprise investment", "Human capital", "Mechanisation", "Specialisation"], 1, "Human capital is the knowledge and skills embodied in workers."),
  mcq("w22_13", 1, "Which action would not raise the quality of the particular factor of production?", ["Capital: operating a machine continuously at full capacity", "Enterprise: providing risk management advice", "Land: increasing the use of fertilisers", "Labour: making apprenticeships and training compulsory"], 0, "Using a machine harder uses it more but does not improve its quality. Fertiliser, training and advice raise quality."),
  mcq("w24_13", 3, "The factors of production earn different rewards. What identifies the correct economic term for these rewards?", ["Capital: surpluses", "Enterprise: dividends", "Labour: interest", "Land: rents"], 3, "Land earns rent, labour wages, capital interest and enterprise profit."),
  mcq("s24_12", 5, "The share of total incomes from profit shows more variation over time than incomes from interest, rent and wages. What is the most likely reason?", ["Interest rates are set by government", "Profit is what is left after interest, rent and wages are subtracted from total income", "Rent is only the return to the factor and so is always the smallest", "Wages only change annually"], 1, "Profit is the residual, so it absorbs all the changes in revenue and costs."),
  mcq("s23_12", 1, "Which factor of production is needed first in order to set up a new business?", ["Capital", "Enterprise", "Labour", "Land"], 1, "An entrepreneur must decide to combine the other factors and take the risk, before they can be hired."),
  mcq("s25_12", 4, "A country increases spending on education and training. It pays for this by reducing unemployment benefit payments and increasing taxes on imports of machinery. What is the likely effect on human capital and physical capital?", ["Human capital decreases; physical capital decreases", "Human capital decreases; physical capital increases", "Human capital increases; physical capital decreases", "Human capital increases; physical capital increases"], 2, "More education raises human capital. Taxing imports of machinery makes machines dearer, so the stock of physical capital is likely to grow more slowly."),
  mcq("w24_12", 3, "A wine producer wants to expand production significantly and offers investors meals discounts if they buy 2,000 shares. Which factors of production are most likely to be involved in the expansion?", ["Labour, land, capital and enterprise", "Labour, land and capital only", "Enterprise and land only", "Enterprise only"], 0, "Expanding a wine business needs vineyards (land), workers (labour), equipment (capital) and an organiser who takes the risk (enterprise)."),
  mcq("w24_13", 14, "A large farm uses labour and capital equipment as substitutes. The government subsidises capital equipment. What happens to the quantities of labour and capital used?", ["Labour decreases; capital increases", "Both decrease", "Labour increases; capital decreases", "Both increase"], 0, "Cheaper capital makes it more attractive than labour, so firms substitute capital for labour.")
]

exam = exam_page("factors of production, human and physical capital and their rewards",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). The factors of production and their rewards are tested in Paper 1 in most series, and enterprise appears in the written papers as an 8 mark explanation and in 12 mark essays on supply-side policy. Reworded past questions are below, with two practice questions and ten Paper 1 multiple choice questions.",
  [("Essay part, 8 marks", "1", "Oct/Nov 2020 (22) Q3(a)"), ("Multiple choice (Paper 1)", "11 shown below", "2021 to 2025")],
  [
  eq(P("w20_22", "3(a)"), "8 marks", "Explain how the factor of production enterprise contributes to aggregate supply in a modern economy and how it differs from the other factors of production in terms of the reward for its services.",
     ["Knowledge (2): enterprise organises the other factors of production (1) and bears the risk of production (1).",
      "Application (up to 6): profit is the reward for enterprise (1); to produce, enterprise hires labour (wages, 1), land (rent, 1) and capital (interest, 1); enterprise uses the factors to produce goods and services that raise aggregate supply (1), through an increase in productive potential or a fall in unused resources (1).",
      "Note: profit is the reward for risk and in loss-making firms there is no profit, which contrasts with the contractual rewards to the other factors; in a modern economy ownership (shareholders) is often separate from control (managers)."],
     "What enterprise does (organise, risk). How it raises output. Its reward is profit (residual and uncertain) versus rent, wages and interest.",
     [[("k", "Enterprise is the factor of production that organises the other factors, bringing together land, labour and capital, and that bears the risk of production, since the entrepreneur cannot be sure that revenue will cover costs."), ("n", "In a modern economy enterprise contributes to aggregate supply because the entrepreneur hires workers, land and capital to produce goods and services. If new firms are set up or existing firms expand, productive potential rises, and if enterprise puts unused resources to work, output rises.")], [("e", "The reward differs from the other factors. Labour receives wages, land receives rent and capital receives interest, which are agreed in advance. Enterprise receives profit, which is what is left after those payments, so it is uncertain and can be negative if the firm makes a loss. Profit is therefore the reward for taking risk.")]]),
  eq("Practice question · modelled on the 4 mark style (no past paper)", "4 marks", "Distinguish between human capital and physical capital, giving an example of each.",
     ["Human capital: the knowledge, skills and qualities of workers that make them more productive (1); example such as training or education (1).",
      "Physical capital: human-made resources such as machinery used in production (1); example such as a delivery van or an oven (1)."],
     "Two definitions and two examples.",
     [[("k", "Human capital is the knowledge, skills and health of workers, built up through education and training, for example a nurse's qualification. Physical capital is man-made equipment and buildings used to produce goods and services, for example a bakery's ovens. Both raise productivity, but human capital is part of the worker, whereas physical capital is an asset that wears out.")]]),
  eq("Practice question · modelled on the 8 mark style (no past paper)", "8 marks", "Explain the rewards to the factors of production and consider why profit is different from the other rewards.",
     ["Knowledge (3): land earns rent, labour wages, capital interest and enterprise profit; definitions of each factor.",
      "Analysis (3): rent, wages and interest are agreed in advance as costs; profit is what remains after paying them; profit rewards risk.",
      "Evaluation (2): profit can be negative, and varies more over time; judgement that it is uncertain unlike the other rewards."],
     "Four factors with their rewards. Profit as residual. Judge: uncertain and can be a loss.",
     [[("k", "Land, which is natural resources, earns rent. Labour, the human effort in production, earns wages. Capital, the human-made equipment used to produce, earns interest, and enterprise, which organises production and bears the risk, earns profit."), ("n", "Rent, wages and interest are costs of production that the firm agrees to pay in advance. Profit is different: it is the surplus after those costs have been paid, so it depends on revenue.")], [("e", "Because profit is the residual, it is uncertain and varies more than the other rewards. If revenue is lower than costs the entrepreneur makes a loss, so profit can be negative, which can never happen to a contracted wage or rent. This is why profit is described as the reward for taking risk.")]])
  ],
  )

tips = tips_html(
  [("Capital is not money.", "Say machines, equipment and buildings. Shares and loans are financial."),
   ("Match every factor to its reward.", "Land: rent. Labour: wages. Capital: interest. Enterprise: profit."),
   ("Call profit the residual.", "It is what is left, so it can be negative."),
   ("Define human capital with skills.", "Knowledge, skills and health that raise productivity."),
   ("Give an example each time.", "Ovens, apprenticeships, farmland, a start-up founder."),
   ("Enterprise comes first.", "Someone must organise and take the risk before the other factors are hired."),
   ("Link to productivity.", "Both types of capital raise output per worker.")],
  [("Factors", "The four factors of production are land, labour, capital and enterprise."),
   ("Capital", "Capital refers to man-made resources used to produce other goods, such as machinery."),
   ("Rewards", "Land earns rent, labour earns wages, capital earns interest and enterprise earns profit."),
   ("Risk", "Profit is the reward for risk, and it might be negative if costs are greater than revenue."),
   ("Human capital", "Training may raise human capital, which could raise productivity and wages.")],
  [CW["define"], CW["explain"], CW["consider"], CW["evaluate"]]) + FC

js = '''
/* ---------- four factors ---------- */
const FAC = [["Land", "natural resources", "Rent", "f1"], ["Labour", "human effort", "Wages", "f2"], ["Capital", "man-made equipment", "Interest", "f3"], ["Enterprise", "organises and takes risk", "Profit", "f1"]];
function facDraw(s) {
  let o = ""; FAC.forEach(([n, d, r, c], i) => { const k = Math.max(0, Math.min(1, s.a - i)), kr = Math.max(0, Math.min(1, s.r - i)), y = 16 + i * 62; if (k > 0) o += SV.rect(30, y, 230, 50, c, op(0.45 * k)) + SV.text(46, y + 22, n, "lbl bd", op(k)) + SV.text(46, y + 40, d, "sm", op(k)); if (kr > 0) o += SV.line(262, y + 25, 480, y + 25, "c1", { "stroke-width": 2.2, ...op(kr) }) + SV.arrowHead(480, y + 25, "r", "dot1") + SV.rect(484, y, 220, 50, c, op(0.7 * kr)) + SV.text(594, y + 31, r + (r === "Profit" ? " (residual)" : ""), "lbl bd", { "text-anchor": "middle", ...op(kr) }); });
  return o;
}
$("#pic1").innerHTML = `<svg viewBox="0 0 740 262" role="img" aria-label="The four factors of production and their rewards: land earns rent, labour earns wages, capital earns interest and enterprise earns profit">${facDraw({ a: 4, r: 4 })}</svg>`;
Lib.stepper($("#stF"), { w: 740, h: 262, label: "A bakery's four factors of production and the reward each earns", base: { a: 0, r: 0 }, draw: facDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>Land</b> is the site and natural resources: the bakery's plot of land and the wheat fields that supply flour.", s: { a: 1, r: 0 } },
  { cap: "<b>Labour</b> is the bakers and shop assistants who do the work.", s: { a: 2, r: 0 } },
  { cap: "<b>Capital</b> is the ovens, mixers and delivery van: man-made equipment, not the money used to buy them.", s: { a: 3, r: 0 } },
  { cap: "<b>Enterprise</b> is the owner who organises everything and risks her own money.", s: { a: 4, r: 0 } },
  { cap: "<b>Rewards.</b> Land earns <b>rent</b>, labour <b>wages</b> and capital <b>interest</b>: these are agreed in advance. Enterprise earns <b>profit</b>, what is left after the others are paid. It can be negative.", s: { a: 4, r: 4 } },
] });

/* ---------- human vs physical capital ---------- */
const HV = [["Worker alone", 10, "f1"], ["+ training (human capital)", 14, "f3"], ["+ machine (physical capital)", 20, "f2"], ["Both together", 30, "f3"]];
function hcDraw(s) {
  let o = SV.line(70, 250, 730, 250) + SV.line(70, 250, 70, 30) + SV.text(76, 22, "Output per worker per day", "sm");
  HV.forEach(([l, v, c], i) => { const k = Math.max(0, Math.min(1, s.n - i)); if (k <= 0) return; const x = 110 + i * 150, h = v * 6.4 * k; o += SV.rect(x, 250 - h, 100, h, c, op(0.75)) + SV.text(x + 50, 250 - h - 8, v, "lbl bd", { "text-anchor": "middle", ...op(k) }) + SV.text(x + 50, 270, l, "sm", { "text-anchor": "middle", ...op(k) }); });
  return o;
}
Lib.stepper($("#stH"), { w: 760, h: 290, label: "Output per worker rising with training, a machine and both together", base: { n: 0 }, draw: hcDraw, tween: 900, dwell: 5600, steps: [
  { cap: "<b>A worker alone</b> with basic tools produces 10 units a day.", s: { n: 1 } },
  { cap: "<b>Human capital.</b> Training raises the worker's skills, so output rises to 14 units.", s: { n: 2 } },
  { cap: "<b>Physical capital.</b> A machine, even without more training, lifts output to 20 units.", s: { n: 3 } },
  { cap: "<b>Both together.</b> A trained worker using the machine produces 30 units, more than the sum of the two separate gains: skills make machines more productive.", s: { n: 4 } },
] });
$("#pic2").innerHTML = `<svg viewBox="0 0 760 290" role="img" aria-label="Output per worker rising from 10 to 14 with training, 20 with a machine and 30 with both">${hcDraw({ n: 4 })}</svg>`;

/* ---------- Lab 1 ---------- */
function labR() {
  if (!$("#rv1") || !$("#wg") || !$("#rn") || !$("#it")) return;
  const rev = +$("#rv1").value, w = +$("#wg").value, rn = +$("#rn").value, it = +$("#it").value, cost = w + rn + it, pf = rev - cost;
  $("#r1").textContent = "$" + cost + "k"; $("#r2").textContent = (pf >= 0 ? "+$" : "−$") + Math.abs(pf) + "k"; $("#r3").textContent = Lib.fmtN(pf / rev * 100, 1) + "%";
  $("#rv").textContent = pf >= 0 ? `Revenue of $${rev}k pays wages ($${w}k), rent ($${rn}k) and interest ($${it}k) first. The $${pf}k that is left is profit: the reward for enterprise and for taking the risk.` : `Revenue of $${rev}k is less than the $${cost}k that must be paid in wages, rent and interest. The entrepreneur makes a loss of $${-pf}k, so enterprise earns a negative reward. Wages, rent and interest still have to be paid.`;
  const sc = 250 / Math.max(rev, cost), X = 100; let y = 250, o = SV.line(60, 250, 360, 250) + SV.text(70, 28, "$ thousands", "sm");
  const seg = (v, c, l) => { const h = v * sc; y -= h; return SV.rect(X, y, 100, h, c, op(0.75)) + (h > 16 ? SV.text(X + 50, y + h / 2 + 5, l + " " + v, "lbl bd", { "text-anchor": "middle" }) : ""); };
  o += seg(w, "f1", "Wages") + seg(rn, "f2", "Rent") + seg(it, "f1", "Interest") + (pf > 0 ? seg(pf, "f3", "Profit") : "");
  o += SV.rect(240, 250 - rev * sc, 100, rev * sc, "f3", op(0.25)) + SV.text(290, 250 - rev * sc - 8, "Revenue " + rev, "lbl bd", { "text-anchor": "middle" });
  if (pf < 0) o += SV.text(X + 50, 250 - cost * sc - 8, "Costs " + cost + " (loss " + (-pf) + ")", "lbl bd", { "text-anchor": "middle", style: "fill:var(--bad)" });
  $("#labA").innerHTML = o + SV.text(X + 50, 272, "Costs", "sm", { "text-anchor": "middle" }) + SV.text(290, 272, "Revenue", "sm", { "text-anchor": "middle" });
}
Lib.slider($("#g1"), { id: "rv1", label: "Revenue, $ thousand ", min: 50, max: 300, step: 5, value: 160, fmt: (v) => v, onInput: labR });
Lib.slider($("#g2"), { id: "wg", label: "Wages, $ thousand ", min: 20, max: 150, step: 5, value: 80, fmt: (v) => v, onInput: labR });
Lib.slider($("#g3"), { id: "rn", label: "Rent, $ thousand ", min: 5, max: 60, step: 5, value: 20, fmt: (v) => v, onInput: labR });
Lib.slider($("#g4"), { id: "it", label: "Interest, $ thousand ", min: 0, max: 40, step: 2, value: 10, fmt: (v) => v, onInput: labR });
labR();

/* ---------- Lab 2 ---------- */
function labK() {
  if (!$("#tr") || !$("#mc")) return;
  const tr = +$("#tr").value, mc = +$("#mc").value, base = 10, a = 0.8 * tr, b = 3 * mc, c = 0.45 * tr * mc, out = base + a + b + c;
  $("#t1").textContent = Lib.fmtN(out, 1) + " units"; $("#t2").textContent = "+" + Lib.fmtN(a, 1); $("#t3").textContent = "+" + Lib.fmtN(b + c, 1);
  $("#tv").textContent = `With ${tr} years of training and ${mc} machine${mc === 1 ? "" : "s"} per worker, output per worker is ${Lib.fmtN(out, 1)} units, compared with 10 for a worker with basic tools. Training adds ${Lib.fmtN(a, 1)} and machines add ${Lib.fmtN(b, 1)}, and the combination adds a further ${Lib.fmtN(c, 1)}, because skilled workers get more from the same machines.`;
  const Y = (v) => 270 - v * 3.4; let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 30) + SV.text(46, 22, "Output per worker", "sm"); let y0 = 0;
  [["Base", base, "f1"], ["Training", a, "f3"], ["Machines", b, "f2"], ["Together", c, "f3"]].forEach(([l, v, cl], i) => { const x = 60 + i * 85; o += SV.rect(x, Y(y0 + v), 60, v * 3.4, cl, op(0.75)) + SV.text(x + 30, 290, l, "sm", { "text-anchor": "middle" }) + tag(x + 30, Y(y0 + v) - 6, "+" + Lib.fmtN(v, 1), "t1", 1, "middle"); y0 += v; });
  $("#labB").innerHTML = o;
}
Lib.slider($("#g5"), { id: "tr", label: "Years of training ", min: 0, max: 10, step: 1, value: 4, fmt: (v) => v, onInput: labK });
Lib.slider($("#g6"), { id: "mc", label: "Machines per worker ", min: 0, max: 5, step: 1, value: 2, fmt: (v) => v, onInput: labK });
labK();

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Which factor of production is it?", ["Land", "Labour", "Capital", "Enterprise"],
  [("A copper mine", 0), ("A team of software engineers", 1), ("A delivery van", 2), ("The founder who risks her savings to start a firm", 3), ("A forest", 0), ("A nurse's skills and time", 1), ("An oven in a bakery", 2), ("A manager who organises the factors and bears the loss if sales fall", 3)],
  "Land: nature's gifts. Labour: people's effort. Capital: man-made equipment. Enterprise: organising and risk-taking.") + MATCH([
  ["Land", "Rent"],
  ["Labour", "Wages"],
  ["Capital", "Interest"],
  ["Enterprise", "Profit"],
  ["Human capital", "Knowledge and skills of workers"],
  ["Physical capital", "Man-made equipment used in production"]]) + ORDER(
  "Put the steps for setting up a bakery in order.",
  ["An entrepreneur decides to start the business and takes the risk", "Land is found for the bakery", "Capital equipment such as ovens is bought", "Labour is hired and trained", "Rent, wages and interest are paid and profit is the residual"],
  "Enterprise comes first, then the other factors, then the rewards.") + CALC([
  {"q": "A firm has revenue of $250,000. It pays wages of $120,000, rent of $30,000 and interest of $20,000. Calculate its profit ($).", "a": 80000, "unit": "$", "tol": 1, "hint": "250,000 − 170,000.", "sol": "<b>$80,000</b>."},
  {"q": "Next year revenue falls to $150,000 but the other payments are the same. Calculate its profit or loss ($, use a minus sign for a loss).", "a": -20000, "unit": "$", "tol": 1, "hint": "150,000 − 170,000.", "sol": "<b>−$20,000</b>, a loss."},
  {"q": "Output per worker rises from 10 to 14 units after training. Calculate the percentage increase (%).", "a": 40, "unit": "%", "tol": 0.5, "hint": "4 ÷ 10.", "sol": "<b>40%</b>."},
  {"q": "Wages are $80,000 of a $200,000 total cost. What percentage of costs is wages (%)?", "a": 40, "unit": "%", "tol": 0.5, "hint": "80 ÷ 200.", "sol": "<b>40%</b>."}]) + MCQ([
  ("Which is the reward to enterprise?", ["Profit", "Interest", "Rent", "Wages"], 0, "Enterprise earns profit; the other rewards go to the other factors."),
  ("Which is NOT classified as capital by economists?", ["Money in a bank account", "A factory building", "A tractor", "A delivery van"], 0, "Money is financial capital, which buys factors but is not itself a factor."),
  ("Human capital is increased by:", ["Training workers", "Buying a new machine", "Finding new oil", "Lowering interest rates"], 0, "Training raises skills and knowledge."),
  ("Profit differs from the other rewards because it:", ["Is a residual and can be negative", "Is set by law", "Is paid first", "Is fixed in advance"], 0, "It is what is left after other rewards are paid."),
  ("Land in economics includes:", ["Oil and fish stocks", "Machines", "Skilled workers", "Shares"], 0, "Land means all natural resources.")
], "qz1") + CARDS([
  ("Land", "Natural resources; earns rent."),
  ("Labour", "Human effort; earns wages."),
  ("Capital", "Man-made equipment; earns interest."),
  ("Enterprise", "Organises and bears risk; earns profit."),
  ("Human capital", "Skills and knowledge of workers."),
  ("Physical capital", "Machines, buildings, tools."),
  ("Profit", "Residual; can be negative."),
  ("Not capital", "Money, shares and loans (financial).")]) + MCQ(mc_exam)

build("as13", "as-factors-of-production-rewards", "Factors of Production and Their Rewards", EY,
  "1.3.1 to 1.3.3: land, labour, capital and enterprise, the difference between human and physical capital, and the rewards of rent, wages, interest and profit. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
