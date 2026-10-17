"""AS syllabus 1.3.4-1.3.5 Division of labour, specialisation and the entrepreneur. Run: python3 tools/artifact-kit/mk_as14.py"""
from asx import *
EY = EYAS("1.3.4 to 1.3.5")

learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p><b class="kw">Division of labour</b> splits production into separate tasks, each done by a different worker, and <b class="kw">specialisation</b> means individuals, firms, regions or countries concentrate on the activities they do best. Specialising raises <b>productivity and output and lowers average cost</b>, because workers gain skill, save time switching and can use machines, but it can also cause <b>boredom, loss of wider skills and dependence on other producers</b>. The <b class="kw">entrepreneur</b> <b>organises the other factors of production and takes the risk</b> of production; in a contemporary economy entrepreneurs start new firms, create jobs, innovate and are rewarded with profit if they succeed.</p></div>

  <h2>1 · Division of labour and specialisation (1.3.4)</h2>
  <div id="pic1" class="card"></div>
  <ul>
    <li><b>Division of labour:</b> a production process is divided into many tasks, each done by a different worker. For example, in a factory making chairs, one worker cuts, another assembles and another paints.</li>
    <li><b>Specialisation:</b> a worker, firm, region or country concentrates on a limited range of tasks or products. Specialisation by countries follows comparative advantage (syllabus 6.1).</li>
    <li>Specialisation needs <b>exchange</b>: people no longer make everything they need, so they sell their output for money and buy what they want.</li>
    <li>Division of labour is more effective in a <b>large market with stable demand</b>, where the extra output can be sold. In a small market that wants custom-made goods it is less useful.</li>
  </ul>
  <div class="tw"><table class="t">
    <tr><th>Advantages</th><th>Disadvantages</th></tr>
    <tr><td><b>Higher productivity:</b> workers become skilled and fast at one task through practice</td><td><b>Boredom and low motivation:</b> repetitive work can reduce effort, quality and productivity after the first gains</td></tr>
    <tr><td><b>Less time lost</b> moving between tasks and tools</td><td><b>Loss of skills:</b> workers may lose the wider skills needed to change jobs</td></tr>
    <tr><td><b>Use of machines:</b> simple tasks can be mechanised</td><td><b>Interdependence:</b> if one stage stops, the whole line stops</td></tr>
    <tr><td><b>Higher output and lower average cost</b>, so lower prices or higher profit</td><td><b>Structural unemployment</b> when an industry or task disappears; <b>over-dependence</b> on a single product or market</td></tr>
    <tr><td><b>Better quality</b> from skilled specialists; gains from trade</td><td>Less flexibility if demand or technology changes</td></tr>
  </table></div>

  <h2>2 · The entrepreneur (1.3.5)</h2>
  <div id="pic2" class="card"></div>
  <ul>
    <li>The <b>entrepreneur</b> has two core functions: <b>organising</b> (taking decisions, combining and coordinating the factors of production) and <b>taking risk</b> (investing money and time without knowing whether the product will earn a profit).</li>
    <li><b>Risk and uncertainty:</b> the entrepreneur pays wages, rent and interest in advance and gets paid only if sales cover costs. The reward for success is <b>profit</b>; the penalty for failure is a loss.</li>
    <li><b>In contemporary economies</b> entrepreneurs <b>innovate</b> (new products and methods), <b>create jobs</b>, introduce competition, meet changing needs quickly and so can increase the productive potential and long-run growth of an economy.</li>
    <li><b>Encouraging entrepreneurship</b> (supply-side policy): subsidies and start-up grants for small firms, lower taxes on business profits, training in management skills, easier access to finance, and less regulation. These have costs and may be slow to work.</li>
    <li>Not every manager is an entrepreneur: a hired manager organises resources but does not bear the risk of loss.</li>
  </ul>
  <div class="tip"><b class="h">Exam tip</b>For the entrepreneur, always give <b>both</b> functions: <b>organising the other factors</b> and <b>taking risk</b>. Each is worth a mark.</div>
'''

watch = '''
  <h2>1 · The pin factory</h2>
  <p>Press Play, or click the numbered steps. The famous example of division of labour comes from Adam Smith (1776).</p>
  <div id="stD"></div>
  <h2>2 · How an entrepreneur's decision plays out</h2>
  <div id="stE"></div>
'''

explore = '''
  <h2>Lab 1 · How far should tasks be divided?</h2>
  <p>A factory makes chairs with 12 workers. Set the number of separate tasks. At first output per worker rises steeply, but too many tiny tasks cause boredom and the gains fade. A market that is too small cannot absorb the extra output.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div>
    <div class="readout"><div><small>Output per worker</small><strong id="r1"></strong></div><div><small>Chairs per day</small><strong id="r2"></strong></div><div><small>Sold (market limit)</small><strong id="r3"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 300" role="img" aria-label="Chairs made per day against the number of tasks with the market limit marked"></svg></div></div></div>

  <h2>Lab 2 · The entrepreneur's risk</h2>
  <p>An entrepreneur must pay a fixed $20,000 to set up a stall before selling anything. Each item costs $6 to make and sells for the price you set. Demand might be weak, average or strong. See the profit or loss in each case.</p>
  <div class="card"><div class="grid2"><div><div id="g3"></div><div id="g4"></div>
    <div class="readout"><div><small>Weak demand</small><strong id="t1"></strong></div><div><small>Average demand</small><strong id="t2"></strong></div><div><small>Strong demand</small><strong id="t3"></strong></div></div>
    <div class="verdict" id="tv"></div></div>
    <div><svg id="labB" viewBox="0 0 420 300" role="img" aria-label="Bars of profit or loss in weak, average and strong demand"></svg></div></div></div>
'''

practise = '''
  <h2>1 · Advantage or disadvantage of division of labour?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the effects of division of labour in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("A modern car assembly line", "Each worker or robot on the line does a small task such as fitting doors or installing seats. Cars are built far faster than if one worker built a whole car. The disadvantages include repetitive work, and when one station breaks down the whole line may stop.", "division of labour in a factory with both its advantages and its drawbacks.") +
rw("A country that specialises in financial services", "A small country may build a reputation as a banking centre. It benefits from expertise and low transport costs for online services, but depends heavily on one industry. If the financial sector suffers a crisis, the whole economy is hit.", "specialisation at the level of a country and the case for diversification.") +
rw("Start-ups and risk", "Most new businesses fail within a few years. Founders put in their own money and time and have no guaranteed income. Those who succeed, such as the founders of successful technology firms, earn very large profits, which is the reward for taking the risk.", "the entrepreneur's risk-taking and the link between risk and profit.") +
rw("Policy support for entrepreneurs", "Governments offer start-up grants, tax breaks for new firms, business training and loans guaranteed by the state. The aim is to raise the supply of enterprise, create jobs and raise the long-run growth rate, though the money has an opportunity cost.", "supply-side policy to increase entrepreneurship.")
)

mc_exam = [
  mcq("s20_11", 4, "What is meant by the division of labour?", ["Each worker specialises in a different task in production", "Some workers work part-time and others full-time", "The same amount of output per hour is produced by each worker", "Workers divide their time between different jobs"], 0, "Division of labour means splitting production into tasks, each done by a specialist worker."),
  mcq("s20_12", 3, "A factory introduces an automated production line to take advantage of division of labour. What is most likely to increase?", ["Average cost of production", "Job satisfaction of workers", "The range of skills of each worker", "Worker productivity"], 3, "Specialised tasks and machinery raise output per worker. Skill range and satisfaction are likely to fall."),
  mcq("s23_11", 4, "A factory manufactures chairs and divides the process into a number of tasks. What is a likely disadvantage of this division of labour?", ["Decrease in motivation", "Decrease in output", "Decrease in productivity", "Decrease in quality of the final product"], 0, "Repetitive work tends to reduce motivation. Output, productivity and quality are expected to rise."),
  mcq("s23_12", 4, "What is not likely to result from the use of division of labour?", ["A decrease in average costs", "An increase in motivation", "An increase in productivity", "An improvement in the quality of the final product"], 1, "Division of labour typically reduces motivation, so increased motivation is the unlikely result."),
  mcq("s24_13", 5, "What will encourage a higher degree of division of labour?", ["Firms wishing for greater self-sufficiency", "Firms wishing to increase flexibility in production", "Firms wishing to raise their productivity", "Firms wishing to reduce their risk"], 2, "The main reason for dividing labour is to raise productivity."),
  mcq("m25_12", 5, "When is division of labour likely to be most effective?", ["In a large market with stable demand", "In a market where consumers prefer a handmade product", "In a market where consumers require a variety of goods", "In a small market where consumers require a custom-made product"], 0, "Division of labour pays off when large, steady sales justify high-volume production of standard products."),
  mcq("w24_12", 2, "In a clothing business, after specialisation, output per worker rose in the first six months but then began to fall. What is the most likely reason?", ["More output per worker in the long run depends on higher pay", "More output per worker requires more capital", "Specialisation means workers lose skills", "Workers get bored repeating the same work"], 3, "Repetitive tasks reduce motivation over time, so the early gains in productivity fade."),
  mcq("w24_13", 4, "What is most likely to be an advantage of the division of labour?", ["An increase in creativity of the labour force", "An increase in labour productivity", "An increase in workforce flexibility", "An increase in worker satisfaction"], 1, "More output per worker is the main advantage. Creativity, flexibility and satisfaction tend to fall."),
  mcq("s25_13", 4, "What is the most likely benefit of specialisation to a firm?", ["An increase in the motivation of employees", "An increase in imports from other countries", "An increase in the number of employees", "An increase in the level of output"], 3, "Specialisation raises output (and productivity)."),
  mcq("w23_12", 2, "What is considered the essential requirement for all entrepreneurs?", ["Attracting customers", "Buying stock", "Managing staff", "Taking risks"], 3, "Entrepreneurs bear the risk of production; managing staff or buying stock can be done by hired employees."),
  mcq("s25_12", 24, "Which supply-side policy will encourage new entrepreneurs?", ["An increase in government subsidy to small firms", "An increase in the national minimum wage", "An increase in the power of trade unions", "An increase in the tax on business profits"], 0, "Subsidies lower costs and risk for small firms. The other measures raise costs or lower the reward from profit.")
]

exam = exam_page("division of labour, specialisation and the entrepreneur",
  "We searched the AS Level Economics papers in the folder (2020 to 2025). The role of the entrepreneur and the effects of specialisation appear as 2 and 6 mark data response parts and as a 12 mark essay on enterprise, and division of labour is tested in Paper 1 every year. Reworded past questions are below, with eleven Paper 1 multiple choice questions.",
  [("Essay parts, 12 marks", "2", "May/June 2023 (22) Q3(b); Feb/March 2021 (22) Q2(b)"), ("Data response, 2 marks", "1", "Oct/Nov 2020 (21) Q1(a)"), ("Data response, 6 marks", "2", "Feb/March 2024 (22) Q1(e); Oct/Nov 2020 (21) Q1(e)"), ("Multiple choice (Paper 1)", "11 shown below", "2020 to 2025")],
  [
  eq(P("w20_21", "1(a)"), "2 marks", "Describe the functions of an entrepreneur in the production process.",
     ["A reference to taking decisions or organising, combining and coordinating the factors of production (1).", "A reference to taking a risk (1)."],
     "Organises the factors. Takes the risk. One mark each.",
     [[("k", "The entrepreneur organises production by making decisions and combining land, labour and capital, and takes the risk that the product may not sell well enough to cover the costs.")]]),
  eq(P("m24_22", "1(e)"), "6 marks", "A country is investing heavily in artificial intelligence (AI). Assess the likely impact of the growth of AI on the specialisation and trade of a country such as Japan.",
     ["Up to 3 marks: benefits of AI for specialisation and trade, such as higher productivity, lower costs and prices, development of comparative advantage and better international competitiveness.",
      "Up to 3 marks: drawbacks, such as over-specialisation, over-reliance on one industry or on non-renewable resources, and structural unemployment.",
      "Maximum of 5 marks for the points; 1 mark reserved for an evaluated conclusion."],
     "Benefits: productivity, costs, comparative advantage. Costs: over-dependence, jobs lost. Conclude.",
     [[("k", "AI could raise productivity and lower the cost of producing goods and services in industries where Japan specialises, such as electronics and cars, which could strengthen its comparative advantage and increase exports.")], [("e", "However, relying heavily on AI-based industries could lead to over-specialisation, so the economy might be badly affected if demand or technology changes. Workers whose tasks are automated might face structural unemployment. Overall AI could improve trade performance, but the gains might depend on how well displaced workers are retrained and how diversified the economy remains.")]]),
  eq(P("w20_21", "1(e)"), "6 marks", "A small country has built a reputation as a banking centre. Discuss whether it is better for it to specialise in banking services rather than have a more diversified economy.",
     ["Up to 3 marks for the advantages of specialising in banking: builds expertise, comparative advantage, low transport costs for services.",
      "Up to 3 marks for the advantages of a diversified economy: avoids over-specialisation and the risk of a downturn in one sector.",
      "5 marks maximum; reserve 1 mark for a conclusion."],
     "For specialising. For diversifying. Conclude.",
     [[("k", "Specialising in banking could build the country's expertise and reputation, and since financial services are easy to deliver abroad, transport costs are low. It would let the country use its comparative advantage.")], [("e", "However, an economy that depends on one sector is vulnerable. A financial crisis could cause large losses and unemployment across the economy, whereas a diversified economy can spread risk. A mixed approach may be best: develop strengths in banking while encouraging other industries.")]]),
  eq(P("s23_22", "3(b)"), "12 marks", "Entrepreneurs are vital in a modern economy to achieve long-run economic growth. Assess whether encouraging entrepreneurship or increasing another factor of production will be a more effective way to achieve long-run economic growth.",
     ["Analysis (up to 8): entrepreneurs organise the other factors and take risks, and profit motivates them; their creativity and innovation can raise the productive potential of the economy (a shift of the PPC); modern economies are dynamic and need people who can respond quickly.",
      "Costs and limits: it costs money to train entrepreneurs; success may be low; other factors such as subsidies and the quality of other factors matter; risk-takers may seek short-run gain.",
      "Compare with increasing one other factor (land, labour or capital), including the advantages and disadvantages and availability of the other factors; a one-sided answer cannot score above Level 2.",
      "Evaluation (up to 4): compare the importance of entrepreneurship with one other factor and conclude which is most important."],
     "Case for entrepreneurship. Case for one other factor (for example capital). Compare. Conclude.",
     [[("k", "Entrepreneurs organise land, labour and capital and bear the risk of production, and the profit motive encourages them to succeed. By innovating they can create new products and methods, which raises the productive potential of the economy and shifts the PPC outwards, increasing long-run growth."), ("n", "Policies to encourage entrepreneurship, such as start-up grants or tax breaks, may increase the number of new firms and jobs. But they cost money, many start-ups fail and risk-takers might seek short-term gains rather than long-term growth.")], [("k", "Increasing capital, for example investment in machinery and infrastructure, raises productivity and can also shift the PPC outwards, but it needs savings and may take time, and without entrepreneurs to organise it the capital may be poorly used."), ("e", "Overall entrepreneurship is probably the factor that makes the others effective, but it works best with good-quality capital and labour. So the most effective approach may be to encourage enterprise alongside investment in human and physical capital.")]]),
  eq(P("m21_22", "2(b)"), "12 marks", "Discuss the view that supply-side policies to increase the supply of labour to an economy are likely to be more successful than those designed to increase the supply of entrepreneurship.",
     ["Analysis of at least two measures to increase the supply of labour: training, relaxing immigration controls, cutting income tax, raising the retirement age (up to 4; maximum 3 if only one measure).",
      "Analysis of at least two measures to increase entrepreneurship: management training, lower business taxes, subsidies and start-up grants (up to 4; maximum 3 if only one).",
      "Evaluation: which are likely to be more successful (3) and a reasoned conclusion (1)."],
     "Labour measures (2). Enterprise measures (2). Compare success and time lags. Judge.",
     [[("k", "Policies to increase the supply of labour include training to help people enter the labour force, relaxing immigration controls and cutting income tax to raise the reward from working."), ("n", "These could raise the size and skills of the workforce, and productive capacity. Policies to increase entrepreneurship include management training, lower taxes on business profits and start-up grants, which could create new firms and jobs.")], [("e", "Which is more successful depends on the economy. If there are many unemployed workers but few new businesses, boosting enterprise may be more effective, since firms create the jobs. The effects of training take years, and entrepreneurship policy has a high failure rate. Overall policies for labour may give more reliable gains, while enterprise policies may bring bigger but riskier rewards.")]])
  ],
  )

tips = tips_html(
  [("Define division of labour precisely.", "Splitting production into separate tasks, each done by a different worker."),
   ("Give the mechanism for productivity.", "Skill from practice, no time lost switching, and use of machines."),
   ("Always give a disadvantage.", "Boredom, loss of skills, interdependence, structural unemployment."),
   ("Two functions of the entrepreneur.", "Organises the other factors and takes the risk."),
   ("Link profit to risk.", "Profit is the reward for bearing risk; a loss is the penalty."),
   ("For a country, link to comparative advantage.", "Specialise where the opportunity cost is lower, but keep diversification in mind."),
   ("Compare in 12 mark answers.", "Weigh entrepreneurs against one other factor and conclude.")],
  [("Productivity", "Division of labour could increase productivity because workers become skilled at one task and waste less time switching."),
   ("Cost", "As output per worker rises, average cost may fall, so firms could cut prices or raise profit."),
   ("Drawback", "However, repeating the same task might reduce motivation and productivity over time."),
   ("Entrepreneur", "The entrepreneur organises the factors of production and bears the risk of production."),
   ("Judge", "The gains from specialisation may depend on the size of the market and how diversified the economy is.")],
  [CW["define"], CW["explain"], CW["assess"], CW["evaluate"]]) + FC

js = '''
/* ---------- pin factory ---------- */
const PF = [["One worker doing every task", 20, "f2"], ["10 workers, each on one or two of 18 tasks", 4800, "f3"]];
function pinDraw(s) {
  let o = SV.line(60, 230, 700, 230) + SV.text(60, 24, "Pins per worker per day (log scale)", "sm");
  const lg = (v) => Math.log10(v) * 55; [10, 100, 1000, 10000].forEach((v) => (o += SV.line(60, 230 - lg(v) + 0, 700, 230 - lg(v), "gr", op(0.35)) + SV.text(54, 234 - lg(v), v.toLocaleString("en-US"), "sm", { "text-anchor": "end" })));
  PF.forEach(([l, v, c], i) => { const k = Math.max(0, Math.min(1, s.n - i)); if (k <= 0) return; const x = 140 + i * 300, h = lg(v) * k; o += SV.rect(x, 230 - h, 130, h, c, op(0.75)) + SV.text(x + 65, 230 - h - 10, v.toLocaleString("en-US") + " pins", "lbl bd", { "text-anchor": "middle", ...op(k) }) + SV.text(x + 65, 252, l.split("|")[0], "sm", { "text-anchor": "middle", ...op(k) }); });
  if (s.n >= 2) o += tag(420, 80, "240 times as many pins per worker", "t4", Math.min(1, s.n - 1), "middle");
  return o;
}
Lib.stepper($("#stD"), { w: 760, h: 275, label: "Adam Smith's pin factory: output per worker for one worker and for ten specialised workers", base: { n: 0 }, draw: pinDraw, tween: 1000, dwell: 5800, steps: [
  { cap: "<b>One worker</b> who must draw the wire, straighten it, cut it, point it, grind the top, make the head, and so on, might make at best about twenty pins a day.", s: { n: 1 } },
  { cap: "<b>Divide the tasks.</b> Smith described ten workers, each doing one or two of the eighteen operations. Together they made about 48,000 pins a day, or 4,800 each.", s: { n: 2 } },
  { cap: "<b>Why?</b> Practice makes each worker faster, no time is lost changing tools, and simple tasks can be helped by machines. Division of labour raised output per worker about 240 times in this example.", s: { n: 2 } },
] });
$("#pic1").innerHTML = `<svg viewBox="0 0 760 275" role="img" aria-label="Pins per worker: 20 for a single worker and 4,800 for ten specialised workers, on a log scale">${pinDraw({ n: 2 })}</svg>`;

/* ---------- entrepreneur decision ---------- */
function entDraw(s) {
  const box = (x, y, w, h, t, c, k) => (k > 0 ? SV.rect(x, y, w, h, c, op(0.5 * k)) + t.split("|").map((l, i, a) => SV.text(x + w / 2, y + h / 2 - (a.length - 1) * 8 + i * 16 + 5, l, "lbl bd", { "text-anchor": "middle", ...op(k) })).join("") : "");
  const ar = (x1, y1, x2, y2, k) => (k > 0 ? SV.line(x1, y1, x2, y2, "c1", { "stroke-width": 2.4, ...op(k) }) + SV.arrowHead(x2, y2, "r", "dot1") : "");
  let o = box(20, 110, 140, 60, "Entrepreneur has|an idea", "f1", s.a) + ar(160, 140, 200, 140, s.b) + box(200, 100, 170, 80, "Organises land, labour|and capital; pays costs|in advance", "f1", s.b) + ar(370, 140, 410, 110, s.c) + ar(370, 140, 410, 175, s.c) + box(410, 70, 150, 60, "Sales high: PROFIT", "f3", s.c) + box(410, 150, 150, 60, "Sales low: LOSS", "f2", s.c);
  if (s.d > 0) o += tag(640, 105, "Reward for risk", "t3", s.d, "middle") + tag(640, 185, "Entrepreneur bears it", "t2", s.d, "middle") + SV.line(570, 100, 570, 100, "c1");
  return o;
}
$("#pic2").innerHTML = `<svg viewBox="0 0 760 230" role="img" aria-label="An entrepreneur organises the factors, pays costs in advance and then earns a profit or makes a loss">${entDraw({ a: 1, b: 1, c: 1, d: 1 })}</svg>`;
Lib.stepper($("#stE"), { w: 760, h: 230, label: "An entrepreneur has an idea, organises the factors, pays costs in advance and then earns a profit or a loss", base: { a: 0, b: 0, c: 0, d: 0 }, draw: entDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>An idea.</b> The entrepreneur spots an opportunity and decides to produce a new product.", s: { a: 1 } },
  { cap: "<b>Organise.</b> She combines land, labour and capital, and pays wages, rent and interest before a single sale is made.", s: { a: 1, b: 1 } },
  { cap: "<b>The outcome is uncertain.</b> If sales are high she keeps a profit after paying all costs. If sales are low she makes a loss and still has to pay the others.", s: { a: 1, b: 1, c: 1 } },
  { cap: "<b>Risk and reward.</b> The entrepreneur bears the risk. Profit is the reward, which is why entrepreneurs are willing to start new firms.", s: { a: 1, b: 1, c: 1, d: 1 } },
] });

/* ---------- Lab 1 ---------- */
function labD() {
  if (!$("#tk") || !$("#mk")) return;
  const t = +$("#tk").value, mk = +$("#mk").value, pw = Math.max(5, 6 * (1 + 1.9 * Math.log(t)) - (t > 6 ? 0.9 * (t - 6) * (t - 6) : 0)), made = pw * 12, sold = Math.min(made, mk);
  $("#r1").textContent = Lib.fmtN(pw, 1); $("#r2").textContent = Lib.fmtN(made, 0); $("#r3").textContent = Lib.fmtN(sold, 0);
  $("#rv").textContent = `With ${t} task${t === 1 ? "" : "s"} each worker makes about ${Lib.fmtN(pw, 1)} chairs a day, so the 12 workers make ${Lib.fmtN(made, 0)}. ${made > mk ? `The market only takes ${mk} chairs a day, so the extra ${Lib.fmtN(made - mk, 0)} cannot be sold: more specialisation does not pay in a small market.` : "The market can absorb all the output."} ${t > 6 ? "Beyond about six tasks, boredom and the loss of skills start to reduce output per worker." : ""}`;
  const X = (k) => 50 + k * 28, Y = (v) => 270 - v * 0.62; let o = SV.line(40, 270, 400, 270) + SV.line(40, 270, 40, 30) + SV.text(400, 292, "Number of tasks", "sm", { "text-anchor": "end" }) + SV.text(46, 22, "Chairs per day", "sm");
  const pts = []; for (let k = 1; k <= 12; k++) pts.push([X(k), Y(Math.max(5, 6 * (1 + 1.9 * Math.log(k)) - (k > 6 ? 0.9 * (k - 6) * (k - 6) : 0)) * 12)]);
  o += SV.path(Lib.ptsPath(pts), "c1") + SV.line(40, Y(mk), 400, Y(mk), "c2 dash") + tag(396, Y(mk) - 6, "market takes " + mk, "t2", 1, "end") + SV.circle(X(t), Y(made), 7, "dot4") + tag(X(t), Y(made) - 12, Lib.fmtN(made, 0), "t4", 1, "middle");
  $("#labA").innerHTML = o;
}
Lib.slider($("#g1"), { id: "tk", label: "Number of separate tasks ", min: 1, max: 12, step: 1, value: 4, fmt: (v) => v, onInput: labD });
Lib.slider($("#g2"), { id: "mk", label: "Chairs the market will buy each day ", min: 60, max: 400, step: 10, value: 220, fmt: (v) => v, onInput: labD });
labD();

/* ---------- Lab 2 ---------- */
function labE() {
  if (!$("#pc") || !$("#fx")) return;
  const p = +$("#pc").value, fx = +$("#fx").value * 1000, cases = [["Weak", 2000], ["Average", 4000], ["Strong", 7000]], pr = cases.map(([l, q]) => q * (p - 6) - fx);
  $("#t1").textContent = (pr[0] >= 0 ? "+$" : "−$") + Math.abs(pr[0]).toLocaleString("en-US"); $("#t2").textContent = (pr[1] >= 0 ? "+$" : "−$") + Math.abs(pr[1]).toLocaleString("en-US"); $("#t3").textContent = (pr[2] >= 0 ? "+$" : "−$") + Math.abs(pr[2]).toLocaleString("en-US");
  $("#tv").textContent = `At a price of $${p} each item adds $${p - 6} to revenue after its $6 cost. With a fixed set-up cost of $${fx.toLocaleString("en-US")} the entrepreneur ${pr[0] < 0 ? "makes a loss if demand is weak" : "still makes a profit even if demand is weak"}, ${pr[1] < 0 ? "a loss at average demand" : "a profit at average demand"} and ${pr[2] < 0 ? "even a loss in strong demand" : "a profit of $" + pr[2].toLocaleString("en-US") + " in strong demand"}. The entrepreneur pays the costs before knowing which case will happen: that is the risk.`;
  const mx = Math.max(10000, ...pr.map(Math.abs)), Y = (v) => 150 - v / mx * 110; let o = SV.line(40, 150, 400, 150) + SV.line(40, 30, 40, 270) + SV.text(46, 22, "Profit or loss, $", "sm");
  cases.forEach(([l], i) => { const x = 60 + i * 115, y = Y(pr[i]); o += SV.rect(x, Math.min(y, 150), 80, Math.abs(y - 150), pr[i] >= 0 ? "f3" : "f2", op(0.75)) + SV.text(x + 40, 292, l + " demand", "sm", { "text-anchor": "middle" }) + tag(x + 40, pr[i] >= 0 ? y - 6 : y + 16, (pr[i] >= 0 ? "+" : "−") + Math.abs(pr[i]).toLocaleString("en-US"), "t1", 1, "middle"); });
  $("#labB").innerHTML = o;
}
Lib.slider($("#g3"), { id: "pc", label: "Price per item, $ ", min: 7, max: 20, step: 1, value: 12, fmt: (v) => v, onInput: labE });
Lib.slider($("#g4"), { id: "fx", label: "Fixed set-up cost, $ thousand ", min: 5, max: 40, step: 1, value: 20, fmt: (v) => v, onInput: labE });
labE();

/* ---------- Practise ---------- */
''' + CLASSIFY("cl1", "Advantage or disadvantage of division of labour?", ["Advantage", "Disadvantage"],
  [("Workers become faster at their single task", 0), ("Workers may become bored by repetitive work", 1), ("Less time is lost moving between tasks", 0), ("Workers may lose wider skills", 1), ("Simple tasks can be done by machines", 0), ("If one stage stops, the whole line stops", 1), ("Output per worker rises and average cost falls", 0), ("Workers are made redundant if the task is automated", 1)],
  "More output per worker is the advantage. Boredom, lost skills and interdependence are the drawbacks.") + MATCH([
  ["Division of labour", "Splitting production into tasks done by different workers"],
  ["Specialisation", "Concentrating on a limited range of tasks or products"],
  ["Entrepreneur", "Organises the factors of production and bears risk"],
  ["Risk", "The chance that costs will not be covered by revenue"],
  ["Profit", "The reward to enterprise for taking risk"],
  ["Interdependence", "Dependence of each stage or country on others"]]) + ORDER(
  "Put the effects of dividing labour in order.",
  ["Production is divided into separate tasks", "Each worker practises one task and becomes faster", "Less time is lost changing tools and tasks; machines are used", "Output per worker rises and average cost falls", "Boredom and loss of skills may reduce the gains if specialisation goes too far"],
  "Productivity first, then the limits.") + CALC([
  {"q": "A single worker makes 20 pins a day. Ten specialised workers make 48,000 pins a day. How many pins does each specialised worker make?", "a": 4800, "unit": "pins", "tol": 1, "hint": "48,000 ÷ 10.", "sol": "<b>4,800 pins</b>."},
  {"q": "By what factor does output per worker rise (4,800 compared with 20)?", "a": 240, "unit": "×", "tol": 1, "hint": "4,800 ÷ 20.", "sol": "<b>240 times</b>."},
  {"q": "A firm's output rises from 400 to 500 chairs a day after dividing tasks. Calculate the percentage increase (%).", "a": 25, "unit": "%", "tol": 0.5, "hint": "100 ÷ 400.", "sol": "<b>25%</b>."},
  {"q": "An entrepreneur sells 3,000 items at $10. Each costs $6 and the fixed cost is $9,000. Calculate her profit ($).", "a": 3000, "unit": "$", "tol": 1, "hint": "3,000 × 4 − 9,000.", "sol": "12,000 − 9,000 = <b>$3,000</b>."}]) + MCQ([
  ("The entrepreneur is the factor that:", ["Organises the other factors and takes risk", "Provides money to the firm", "Is paid wages", "Supplies the land"], 0, "Organising and risk-taking are the two functions."),
  ("Division of labour is likely to raise productivity because:", ["Workers become skilled at one task", "Workers do many different tasks", "Machines are not needed", "Output falls"], 0, "Specialisation builds skill and saves time."),
  ("A disadvantage of specialisation for a country is:", ["Dependence on a few industries", "Higher output", "Lower costs", "More trade"], 0, "A downturn in the one industry hits the whole economy."),
  ("Which would encourage entrepreneurship?", ["Start-up grants for new firms", "Higher taxes on business profits", "More red tape", "A ban on new firms"], 0, "Subsidies reduce the cost and risk."),
  ("In which market is division of labour least useful?", ["A small market wanting custom-made goods", "A large market with stable demand", "A market for standard goods", "A mass-market"], 0, "Specialised mass production needs a big market for standard products.")
], "qz1") + CARDS([
  ("Division of labour", "Splitting production into tasks."),
  ("Specialisation", "Concentrating on what you do best."),
  ("Benefits", "Productivity up, average cost down."),
  ("Drawbacks", "Boredom, lost skills, interdependence."),
  ("Entrepreneur", "Organises factors; takes risk."),
  ("Reward", "Profit (or loss)."),
  ("Enterprise policy", "Grants, tax cuts, training, finance."),
  ("Large market", "Needed for division of labour to pay.")]) + MCQ(mc_exam)

build("as14", "as-division-of-labour-entrepreneur", "Division of Labour, Specialisation and the Entrepreneur", EY,
  "1.3.4 to 1.3.5: division of labour and specialisation with their advantages and disadvantages, and the role of the entrepreneur in a contemporary economy. Animated diagrams, labs, drills and the past paper questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
