const op = (v) => ({ opacity: Math.max(0, Math.min(1, v)) });
const halo = { style: "paint-order:stroke;stroke:var(--surface);stroke-width:5px" };
const arrow = (x1, y1, x2, y2, dir, cls, v) => `<g style="opacity:${Math.max(0, Math.min(1, v))}">${SV.line(x1, y1, x2, y2, cls, { "stroke-width": 2.5 })}${SV.arrowHead(x2, y2, dir, cls === "c2" ? "dot2" : cls === "c3" ? "dot3" : cls === "c4" ? "dot4" : "dot1")}</g>`;
const axes = (x0, y0, x1, y1, xl, yl) => SV.line(x0, y0, x1, y0) + SV.line(x0, y0, x0, y1) + SV.text(x1, y0 + 26, xl, "sm", { "text-anchor": "end" }) + SV.text(x0 + 6, y1 - 6, yl, "sm");
const tag = (x, y, t, c, v = 1, a = "start") => SV.text(x, y, t, "lbl bd " + c, { "text-anchor": a, ...halo, ...op(v) });
/* click a button, show its row of results */
function btnTable(btnId, outId, rows, heads) {
  const box = $("#" + btnId), out = $("#" + outId); if (!box || !out) return;
  box.innerHTML = rows.map((r, i) => `<button class="b" data-i="${i}">${r[0]}</button>`).join("");
  const show = (i) => { const r = rows[i]; $$("button", box).forEach((b, k) => b.classList.toggle("pri", k === i)); out.innerHTML = `<div class="tw"><table class="t"><tr>${heads.map((h) => `<th>${h}</th>`).join("")}</tr><tr>${r.map((c, k) => `<td>${k ? c : "<b>" + c + "</b>"}</td>`).join("")}</tr></table></div>`; };
  $$("button", box).forEach((b) => (b.onclick = () => show(+b.dataset.i))); show(0);
}

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
Lib.classify($("#cl1"), { prompt: "Advantage or disadvantage of division of labour?", buckets: [{"label": "Advantage"}, {"label": "Disadvantage"}], items: [{"text": "Workers become faster at their single task", "b": 0}, {"text": "Workers may become bored by repetitive work", "b": 1}, {"text": "Less time is lost moving between tasks", "b": 0}, {"text": "Workers may lose wider skills", "b": 1}, {"text": "Simple tasks can be done by machines", "b": 0}, {"text": "If one stage stops, the whole line stops", "b": 1}, {"text": "Output per worker rises and average cost falls", "b": 0}, {"text": "Workers are made redundant if the task is automated", "b": 1}], done: "More output per worker is the advantage. Boredom, lost skills and interdependence are the drawbacks." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Division of labour", "Splitting production into tasks done by different workers"], ["Specialisation", "Concentrating on a limited range of tasks or products"], ["Entrepreneur", "Organises the factors of production and bears risk"], ["Risk", "The chance that costs will not be covered by revenue"], ["Profit", "The reward to enterprise for taking risk"], ["Interdependence", "Dependence of each stage or country on others"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the effects of dividing labour in order.", items: ["Production is divided into separate tasks", "Each worker practises one task and becomes faster", "Less time is lost changing tools and tasks; machines are used", "Output per worker rises and average cost falls", "Boredom and loss of skills may reduce the gains if specialisation goes too far"], done: "Productivity first, then the limits." });
Lib.calc($("#c1"), { qs: [
  {"q": "A single worker makes 20 pins a day. Ten specialised workers make 48,000 pins a day. How many pins does each specialised worker make?", "a": 4800, "unit": "pins", "tol": 1, "hint": "48,000 ÷ 10.", "sol": "<b>4,800 pins</b>."},
  {"q": "By what factor does output per worker rise (4,800 compared with 20)?", "a": 240, "unit": "×", "tol": 1, "hint": "4,800 ÷ 20.", "sol": "<b>240 times</b>."},
  {"q": "A firm's output rises from 400 to 500 chairs a day after dividing tasks. Calculate the percentage increase (%).", "a": 25, "unit": "%", "tol": 0.5, "hint": "100 ÷ 400.", "sol": "<b>25%</b>."},
  {"q": "An entrepreneur sells 3,000 items at $10. Each costs $6 and the fixed cost is $9,000. Calculate her profit ($).", "a": 3000, "unit": "$", "tol": 1, "hint": "3,000 × 4 − 9,000.", "sol": "12,000 − 9,000 = <b>$3,000</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "The entrepreneur is the factor that:", opts: ["Organises the other factors and takes risk", "Provides money to the firm", "Is paid wages", "Supplies the land"], a: 0, why: "Organising and risk-taking are the two functions." },
  { q: "Division of labour is likely to raise productivity because:", opts: ["Workers become skilled at one task", "Workers do many different tasks", "Machines are not needed", "Output falls"], a: 0, why: "Specialisation builds skill and saves time." },
  { q: "A disadvantage of specialisation for a country is:", opts: ["Dependence on a few industries", "Higher output", "Lower costs", "More trade"], a: 0, why: "A downturn in the one industry hits the whole economy." },
  { q: "Which would encourage entrepreneurship?", opts: ["Start-up grants for new firms", "Higher taxes on business profits", "More red tape", "A ban on new firms"], a: 0, why: "Subsidies reduce the cost and risk." },
  { q: "In which market is division of labour least useful?", opts: ["A small market wanting custom-made goods", "A large market with stable demand", "A market for standard goods", "A mass-market"], a: 0, why: "Specialised mass production needs a big market for standard products." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Division of labour", "Splitting production into tasks."],
  ["Specialisation", "Concentrating on what you do best."],
  ["Benefits", "Productivity up, average cost down."],
  ["Drawbacks", "Boredom, lost skills, interdependence."],
  ["Entrepreneur", "Organises factors; takes risk."],
  ["Reward", "Profit (or loss)."],
  ["Enterprise policy", "Grants, tax cuts, training, finance."],
  ["Large market", "Needed for division of labour to pay."],
] });
Lib.quiz($("#qz2"), { qs: [
  { q: "What is meant by the division of labour? (May/June 2020 · 11 · Q4, reworded)", opts: ["Each worker specialises in a different task in production", "Some workers work part-time and others full-time", "The same amount of output per hour is produced by each worker", "Workers divide their time between different jobs"], a: 0, why: "Division of labour means splitting production into tasks, each done by a specialist worker." },
  { q: "A factory introduces an automated production line to take advantage of division of labour. What is most likely to increase? (May/June 2020 · 12 · Q3, reworded)", opts: ["Average cost of production", "Job satisfaction of workers", "The range of skills of each worker", "Worker productivity"], a: 3, why: "Specialised tasks and machinery raise output per worker. Skill range and satisfaction are likely to fall." },
  { q: "A factory manufactures chairs and divides the process into a number of tasks. What is a likely disadvantage of this division of labour? (May/June 2023 · 11 · Q4, reworded)", opts: ["Decrease in motivation", "Decrease in output", "Decrease in productivity", "Decrease in quality of the final product"], a: 0, why: "Repetitive work tends to reduce motivation. Output, productivity and quality are expected to rise." },
  { q: "What is not likely to result from the use of division of labour? (May/June 2023 · 12 · Q4, reworded)", opts: ["A decrease in average costs", "An increase in motivation", "An increase in productivity", "An improvement in the quality of the final product"], a: 1, why: "Division of labour typically reduces motivation, so increased motivation is the unlikely result." },
  { q: "What will encourage a higher degree of division of labour? (May/June 2024 · 13 · Q5, reworded)", opts: ["Firms wishing for greater self-sufficiency", "Firms wishing to increase flexibility in production", "Firms wishing to raise their productivity", "Firms wishing to reduce their risk"], a: 2, why: "The main reason for dividing labour is to raise productivity." },
  { q: "When is division of labour likely to be most effective? (Feb/March 2025 · 12 · Q5, reworded)", opts: ["In a large market with stable demand", "In a market where consumers prefer a handmade product", "In a market where consumers require a variety of goods", "In a small market where consumers require a custom-made product"], a: 0, why: "Division of labour pays off when large, steady sales justify high-volume production of standard products." },
  { q: "In a clothing business, after specialisation, output per worker rose in the first six months but then began to fall. What is the most likely reason? (Oct/Nov 2024 · 12 · Q2, reworded)", opts: ["More output per worker in the long run depends on higher pay", "More output per worker requires more capital", "Specialisation means workers lose skills", "Workers get bored repeating the same work"], a: 3, why: "Repetitive tasks reduce motivation over time, so the early gains in productivity fade." },
  { q: "What is most likely to be an advantage of the division of labour? (Oct/Nov 2024 · 13 · Q4, reworded)", opts: ["An increase in creativity of the labour force", "An increase in labour productivity", "An increase in workforce flexibility", "An increase in worker satisfaction"], a: 1, why: "More output per worker is the main advantage. Creativity, flexibility and satisfaction tend to fall." },
  { q: "What is the most likely benefit of specialisation to a firm? (May/June 2025 · 13 · Q4, reworded)", opts: ["An increase in the motivation of employees", "An increase in imports from other countries", "An increase in the number of employees", "An increase in the level of output"], a: 3, why: "Specialisation raises output (and productivity)." },
  { q: "What is considered the essential requirement for all entrepreneurs? (Oct/Nov 2023 · 12 · Q2, reworded)", opts: ["Attracting customers", "Buying stock", "Managing staff", "Taking risks"], a: 3, why: "Entrepreneurs bear the risk of production; managing staff or buying stock can be done by hired employees." },
  { q: "Which supply-side policy will encourage new entrepreneurs? (May/June 2025 · 12 · Q24, reworded)", opts: ["An increase in government subsidy to small firms", "An increase in the national minimum wage", "An increase in the power of trade unions", "An increase in the tax on business profits"], a: 0, why: "Subsidies lower costs and risk for small firms. The other measures raise costs or lower the reward from profit." },
] });
