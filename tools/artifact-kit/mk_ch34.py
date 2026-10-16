"""Builds the three ch34 part pages (fi1..fi3) from slices of fif.* plus new content. Run: python3 tools/artifact-kit/mk_ch34.py
The Learn content keeps its legacy topic styling, so fif.css is copied next to each part."""
import shutil
from splitter import *
mktips = tips
S = Src("fif")
HEAD = "// uses: econ\n"
EY = "A Level Economics · 9708 · Syllabus 7.5 · Part {} of 3"
for n in ("fi1", "fi2", "fi3"): shutil.copy(D / "fif.css", D / f"{n}.css")
def renum(t, start): 
    import re
    c = [start - 1]
    def f(m): c[0] += 1; return f'<span class="topic-num">{c[0]}</span>'
    return re.sub(r'<span class="topic-num">\d+</span>', f, t)
EXNOTE = '<p>The exam-style questions below were written for this page (open each one for reminders, a model answer and the common mistake). The Paper 3 multiple choice questions are real past paper questions: choose an answer, then read the reason. Mark scheme points are summarised in our own words, not copied.</p>\n'
LEG = "legacy"

# ------------------------------------------------------------------ 34.1
learn = renum(S.b((20, 75), (77, 161)), 1)
watch = '''
  <h2>1 · Diminishing returns: TP, MP and AP</h2>
  <p>Press Play, or use the numbered steps to jump around. Each step adds one worker to a fixed factory.</p><div id="stA"></div>
  <h2>2 · Short-run cost curves and how MC cuts the averages</h2><div id="stB"></div>
'''
explore = S.b((409, 416))
practise = S.b((448, 450)) + '''
  <h2>2 · Put the diminishing-returns chain in order</h2><div id="o1" class="card"></div>
  <h2>3 · Calculations</h2>
  <p>Enter numbers only. Give answers to one decimal place where needed.</p>
  <div id="c1"></div>
  <h2>4 · Multiple choice</h2><div id="qz1"></div>
  <h2>5 · Draw it. Explain it. Apply it.</h2>
  <p>For each prompt, sketch the diagram on paper, then explain it and apply it to a real firm of your choice.</p>
  <div id="promptList"></div>
'''
real = '<p class="note">Examples are explained in general terms so they stay true. Look up current figures before quoting them in an exam answer.</p>\n' + S.b((476, 476)) + '''  <div class="rw"><h3>A bakery adding bakers</h3><p>With one oven, the first few bakers add a lot of extra bread. Once the oven is crowded, each extra baker adds less and less, so the cost of each extra loaf rises.</p><div class="use"><b>Exam use:</b> diminishing returns, MP falling and MC rising.</div></div>
'''
exam = '''
  <h2>Exam questions on short-run production and costs</h2>
  ''' + EXNOTE + '''
  <div class="key" aria-label="Colour key"><span class="k"><i></i>Knowledge (K)</span><span class="a"><i></i>Application (A)</span><span class="n"><i></i>Analysis (N)</span><span class="e"><i></i>Evaluation (E)</span></div>
''' + S.b((491, 495), (503, 508)) + MCQTAIL.format("Paper 3 multiple choice questions")
tips = '<h2>Top tips</h2>\n  <ul class="tips">\n' + S.b((535, 536), (541, 541)) + '  </ul>\n' + cmd(("Define / State", "A precise meaning in one or two ideas."), ("Calculate", "Formula, substitution, answer with units."), CW["explain"]) + '  <h2>Keyword flashcards</h2>\n  <p>Click the card to flip it. Mark the ones you know.</p>\n  <div id="fc1"></div>\n'
js = HEAD + S.j_((2, 59), (83, 96)) + '''
/* ---------- Practise ---------- */
''' + S.j_((145, 153), (171, 177)) + calc(S, (179, 180, 181, 182), '''  { q: "AVC at 4 units of output is $11 and AFC is $12.50. What is ATC ($)?", a: 23.5, tol: 0.01, sol: "ATC = AFC + AVC = 12.50 + 11 = <b>$23.50</b>." },
''') + qz(S, (187, 188), '''  { q: "Which cost falls continuously as output rises in the short run?", opts: ["Marginal cost", "Average variable cost", "Average fixed cost", "Average total cost"], a: 2, why: "Fixed cost is spread over more and more units." },
''') + cards(S, tuple(range(195, 201))) + '''
/* ---------- Draw it. Explain it. Apply it. ---------- */
const PROMPTS = [
''' + S.j_((216, 217)) + '''];
''' + S.j_((224, 232)) + mcq(S, (), '''  { q: "[Feb/March 2021 · 32 · Q8] When output increases in the short run, which statement is correct?", opts: ["Average fixed cost first falls and then, beyond some point, rises.", "Average variable cost increases as soon as the law of diminishing marginal returns begins to operate.", "The minimum point of the average total cost curve occurs at a greater level of output than the minimum point of the average variable cost curve.", "When marginal cost reaches its minimum point, average variable cost must be greater than average fixed cost."], a: 2, why: "MC cuts AVC at its minimum and ATC at its minimum, and ATC includes falling AFC, so ATC reaches its lowest point at a higher output than AVC." },
  { q: "[Feb/March 2025 · 32 · Q1] Which cost will continually decrease as a firm's output increases in the short run?", opts: ["average cost", "average fixed cost", "average variable cost", "marginal cost"], a: 1, why: "Average fixed cost is fixed cost divided by output, so it falls as output rises." },
  { q: "[Feb/March 2020 · 32 · Q8] Why might a firm continue in production in the short run even though the price of its product has fallen below its average total costs of production?", opts: ["It anticipates a rise in variable costs.", "It expects the fall in price to be temporary.", "It has large fixed costs of production.", "It has no control over the price of its product."], a: 1, why: "In the short run a firm may carry on if price covers variable cost and it expects price to recover. Large fixed costs are paid anyway, but they do not explain staying open." },
  { q: "[May/June 2020 (not sat) · 31 · Q6] In the short run, a firm produces an extra unit of output. Which of the firm's production costs will change?", opts: ["fixed cost only", "fixed cost and variable cost", "variable cost only", "variable cost and total cost"], a: 3, why: "Fixed cost does not change with output, so variable cost and total cost both rise." },
  { q: "[May/June 2020 (not sat) · 32 · Q7] The table shows total costs for a firm producing chairs: output 0 gives $50, 1 gives $60, 2 gives $64, 3 gives $77, 4 gives $94, 5 gives $114. What is the average variable cost when output is 4 chairs?", opts: ["$11", "$17", "$44", "$23.50"], a: 0, why: "Fixed cost is $50 (the cost at zero output), so variable cost at 4 chairs is 94 − 50 = 44, and 44 ÷ 4 = $11." },
''')
write("fi1", page(EY.format(1), "Short-Run Production and Costs",
  "The short-run production function, diminishing returns and the shape of the short-run cost curves, with labs on cost per unit and the optimum output. Animated diagrams, drills and the past paper questions.",
  learn_class=LEG, learn=learn, watch=watch, explore=explore, practise=practise, real=real, exam=exam, tips=tips), js,
  "Short-Run Production and Costs", "short-run-production-and-costs")

# ------------------------------------------------------------------ 34.2
learn = renum(S.b((163, 243), (245, 283), (285, 311)), 3)
watch = '''
  <h2>1 · SRAC curves and the LRAC envelope</h2><div id="stC"></div>
'''
explore = S.b((418, 425))
practise = S.b((452, 453)) + '''
  <h2>2 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Put the economies of scale argument in order</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2>
  <p>Enter numbers only. Give answers to one decimal place where needed.</p>
  <div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
  <h2>6 · Draw it. Explain it. Apply it.</h2>
  <p>For each prompt, sketch the diagram on paper, then explain it and apply it to a real firm of your choice.</p>
  <div id="promptList"></div>
'''
real = '<p class="note">Examples are explained in general terms so they stay true. Look up current figures before quoting them in an exam answer.</p>\n' + S.b((477, 480))
exam = '''
  <h2>Exam questions on long-run production, costs and economies of scale</h2>
  ''' + EXNOTE + '''
  <div class="key" aria-label="Colour key"><span class="k"><i></i>Knowledge (K)</span><span class="a"><i></i>Application (A)</span><span class="n"><i></i>Analysis (N)</span><span class="e"><i></i>Evaluation (E)</span></div>
''' + S.b((510, 516)) + MCQTAIL.format("Paper 3 multiple choice questions")
tips = '<h2>Top tips</h2>\n  <ul class="tips">\n' + S.b((538, 539)) + '''    <li><b>In the long run all factors are variable,</b> so there are no fixed costs and no diminishing returns. Talk about returns to scale and economies of scale instead.</li>
''' + '  </ul>\n' + cmd(("Define / State", "A precise meaning in one or two ideas."), CW["explain"], CW["analyse"]) + '  <h2>Keyword flashcards</h2>\n  <p>Click the card to flip it. Mark the ones you know.</p>\n  <div id="fc1"></div>\n'
js = HEAD + S.j_((60, 82), (98, 111)) + '''
/* ---------- Practise ---------- */
''' + S.j_((154, 162)) + '''Lib.match($("#m1"), { prompt: "Match each term to its meaning.", pairs: [
  ["Isoquant", "All labour and capital combinations that give the same output"],
  ["Isocost line", "All combinations of factors that cost the same total amount"],
  ["Least-cost combination", "Where the isocost line just touches the isoquant"],
  ["Long-run average cost", "The lowest average cost at each output when all factors can change"],
  ["Minimum efficient scale", "The lowest output at which LRAC reaches its minimum"],
  ["Internal economies", "Falling LRAC from the growth of the firm itself"],
  ["External economies", "Lower costs for every firm from the growth of the whole industry"],
], done: "Seven terms for the long run." });
Lib.order($("#o1"), { prompt: "Put the explanation of how internal economies of scale lower average cost in order.", items: [
  "The firm increases its output in the long run",
  "It can buy materials in bulk and use specialised machinery and managers",
  "Total cost rises by less than the rise in output",
  "Average cost (total cost ÷ output) falls",
  "The firm moves down its long-run average cost curve towards MES",
  "Beyond MES diseconomies of scale may raise average cost again",
], done: "Internal economies are a movement along the LRAC curve." });
Lib.calc($("#c1"), { qs: [
  { q: "To produce 100 units, labour costs $10 a unit and capital $10 a unit, and the least-cost mix is 10 labour and 10 capital. What is the total cost ($)?", a: 200, sol: "10 × 10 + 10 × 10 = <b>$200</b>." },
  { q: "The wage rises to $40. The least-cost mix becomes 5 labour and 20 capital (capital still $10). What is the total cost ($)?", a: 400, sol: "40 × 5 + 10 × 20 = <b>$400</b>. The firm uses less of the dearer factor." },
  { q: "A firm's total cost is $2,000 at 100 units and $3,600 at 300 units. What is the long-run average cost at 300 units ($)?", a: 12, sol: "3,600 ÷ 300 = <b>$12</b>, down from $20 at 100 units: economies of scale." },
  { q: "Output doubles from 200 to 400 and total cost rises from $4,000 to $6,000. By what percentage does average cost fall (%)?", a: 25, sol: "Average cost falls from $20 to $15: (20 − 15) ÷ 20 × 100 = <b>25%</b>." },
] });
''' + qz(S, (190,), '''  { q: "A firm growing along its long-run average cost curve towards MES is likely to benefit from:", opts: ["diminishing returns", "internal economies of scale", "fixed costs", "external diseconomies"], a: 1, why: "Falling LRAC as the firm grows is the effect of internal economies of scale." },
  { q: "Which is a diseconomy of scale?", opts: ["Bulk-buying discounts", "Slower decisions in a very large firm", "Cheaper loans", "A local pool of skilled workers"], a: 1, why: "Management and communication problems raise average cost beyond MES." },
''') + cards(S, tuple(range(201, 207))) + '''
/* ---------- Draw it. Explain it. Apply it. ---------- */
const PROMPTS = [
''' + S.j_((218, 220)) + '''];
''' + S.j_((224, 232)) + mcq(S, (), '''  { q: "[Feb/March 2024 · 32 · Q4] The statement and the table provide information about a production function. The production function represents the amount of ...1... obtainable from each combination of ...2... and can be used to give information about ...3.... Which words correctly complete gaps 1, 2 and 3?", opts: ["demand, labour, returns to scale", "demand, labour, normal profit", "output, inputs, returns to scale", "output, inputs, supernormal profit"], a: 2, why: "A production function links inputs to the maximum output, and shows returns to scale when all inputs change." },
  { q: "[Feb/March 2020 · 32 · Q10] What is true about economies of scale but not diseconomies of scale?", opts: ["They occur because average revenue is increasing.", "They occur because of management policy changes.", "They occur in the short run.", "They occur with decreasing average cost."], a: 3, why: "Economies of scale are falling average cost as output rises; diseconomies are rising average cost." },
  { q: "[Feb/March 2024 · 32 · Q5] Two firms selling the same type of product find it more efficient to merge. Which combination describes how the merged firm's average costs of production and demand curve are expected to change?", opts: ["average costs fall, demand curve more elastic", "average costs fall, demand curve more inelastic", "average costs rise, demand curve more elastic", "average costs rise, demand curve more inelastic"], a: 1, why: "A larger firm may gain economies of scale so costs fall, and with fewer rivals the demand it faces becomes less elastic." },
''')
write("fi2", page(EY.format(2), "Long-Run Production, Costs and Economies of Scale",
  "Isoquants and isocosts, the least-cost combination of factors, the long-run average cost curve, and internal and external economies and diseconomies of scale. Animated diagrams, labs, drills and the past paper questions.",
  learn_class=LEG, learn=learn, watch=watch, explore=explore, practise=practise, real=real, exam=exam, tips=tips), js,
  "Long-Run Production, Costs and Economies of Scale", "long-run-production-costs-economies")

# ------------------------------------------------------------------ 34.3
learn = renum(S.b((313, 358), (360, 389)), 6)
watch = '''
  <h2>1 · Average, marginal and total revenue</h2>
  <p>A price maker faces the demand curve P = 20 − Q. Press Play, or click the steps.</p><div id="stR2"></div>
  <h2>2 · Normal, subnormal and supernormal profit</h2>
  <p>A firm sells 500 units and its total cost, which includes normal profit, is $5,200. What happens as the price changes?</p><div id="stP2"></div>
'''
explore = S.b((427, 434), (436, 443)).replace("Lab 3 ·", "Lab 1 ·").replace("Lab 4 ·", "Lab 2 ·")
practise = '''
  <h2>1 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>2 · Calculations</h2>
  <p>Enter numbers only. Give answers to one decimal place where needed.</p>
  <div id="c1"></div>
  <h2>3 · Multiple choice</h2><div id="qz1"></div>
  <h2>4 · Draw it. Explain it. Apply it.</h2>
  <p>For each prompt, sketch the diagram on paper, then explain it and apply it to a real firm of your choice.</p>
  <div id="promptList"></div>
'''
real = '<p class="note">Examples are explained in general terms so they stay true. Look up current figures before quoting them in an exam answer.</p>\n' + S.b((481, 482))
exam = '''
  <h2>Exam questions on revenue and profit</h2>
  ''' + EXNOTE + '''
  <div class="key" aria-label="Colour key"><span class="k"><i></i>Knowledge (K)</span><span class="a"><i></i>Application (A)</span><span class="n"><i></i>Analysis (N)</span><span class="e"><i></i>Evaluation (E)</span></div>
''' + S.b((497, 501), (518, 528)) + MCQTAIL.format("Paper 3 multiple choice questions")
tips = '<h2>Top tips</h2>\n  <ul class="tips">\n' + S.b((537, 537), (540, 540), (542, 542)) + '  </ul>\n' + cmd(("Calculate", "Formula, substitution, answer with units."), CW["explain"], CW["discuss"]) + '  <h2>Keyword flashcards</h2>\n  <p>Click the card to flip it. Mark the ones you know.</p>\n  <div id="fc1"></div>\n'
js = HEAD + '''
const op = (v) => ({ opacity: Math.max(0, Math.min(1, v)) });
/* ---------- Watch 1: AR, MR and TR ---------- */
const RLX = (q) => 70 + q * 15, RLY = (p) => 150 - p * 5, RRX = (q) => 450 + q * 14, RRY = (v) => 270 - v * 2;
function revDraw(s) {
  let o = SV.line(70, 150, 380, 150) + SV.line(70, 40, 70, 260) + SV.text(380, 186, "Quantity", "sm", { "text-anchor": "end" }) + SV.text(76, 34, "Price, AR, MR ($)", "sm");
  [0, 10, 20].forEach((q) => { o += SV.text(RLX(q), 164, q, "sm", { "text-anchor": "middle" }); });
  o += SV.line(450, 270, 740, 270) + SV.line(450, 40, 450, 276) + SV.text(740, 294, "Quantity", "sm", { "text-anchor": "end" }) + SV.text(456, 34, "Total revenue ($)", "sm");
  if (s.ar > 0) o += SV.line(RLX(0), RLY(20), RLX(20), RLY(0), "c1", op(s.ar)) + SV.text(RLX(19), RLY(0) - 8, "AR = D", "lbl bd t1", { "text-anchor": "end", ...op(s.ar) });
  if (s.mr > 0) o += SV.line(RLX(0), RLY(20), RLX(20), RLY(-20), "c2", op(s.mr)) + SV.text(RLX(18.5), RLY(-17) + 14, "MR", "lbl bd t2", { "text-anchor": "end", ...op(s.mr) });
  if (s.tr > 0) { const pts = []; for (let q = 0; q <= 20 * s.tr + 0.01; q += 0.5) pts.push([RRX(q), RRY(q * (20 - q))]); if (pts.length > 1) o += SV.path(Lib.ptsPath(pts), "c3"); }
  if (s.mk > 0) o += SV.line(RLX(10), RLY(0), RLX(10), 260, "gr", op(s.mk)) + SV.circle(RLX(10), RLY(0), 6, "dot2", op(s.mk)) + SV.line(RRX(10), RRY(100), RRX(10), 270, "gr", op(s.mk)) + SV.circle(RRX(10), RRY(100), 6, "dot3", op(s.mk)) + SV.text(RRX(10) + 10, RRY(100) - 8, "TR = $100 (maximum)", "lbl bd t3", { style: "paint-order:stroke;stroke:var(--surface);stroke-width:4px", ...op(s.mk) }) + SV.text(RLX(10) - 8, RLY(0) + 36, "MR = 0 at Q = 10", "lbl bd t2", { "text-anchor": "end", style: "paint-order:stroke;stroke:var(--surface);stroke-width:4px", ...op(s.mk) });
  return o;
}
Lib.stepper($("#stR2"), { w: 780, h: 310, label: "Average revenue, marginal revenue and total revenue for a price maker", base: { ar: 0, mr: 0, tr: 0, mk: 0 }, draw: revDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>Average revenue.</b> The firm can only sell more by cutting its price, so average revenue (price) falls as quantity rises: <b>AR = D = 20 − Q</b>.", s: { ar: 1 } },
  { cap: "<b>Marginal revenue.</b> To sell one more unit the firm cuts the price on <b>all</b> units, so the extra revenue is less than the price. MR = 20 − 2Q lies below AR and is twice as steep. It reaches zero at Q = 10 and then goes negative.", s: { ar: 1, mr: 1 } },
  { cap: "<b>Total revenue.</b> TR = price × quantity. It rises while MR is positive, then falls once MR is negative.", s: { ar: 1, mr: 1, tr: 1 } },
  { cap: "<b>MR = 0 where TR is at its maximum</b> ($100 at Q = 10). At that point price elasticity of demand is 1. A firm that wants maximum revenue stops here; a profit-maximiser stops earlier, where MR = MC.", s: { ar: 1, mr: 1, tr: 1, mk: 1 } },
] });

/* ---------- Watch 2: profit types ---------- */
const PB = 270, PH = (v) => v / 30;
function profDraw(s) {
  const r = s.r, tc = 5200, ok = r > tc + 1, eq = Math.abs(r - tc) <= 1;
  let o = SV.line(60, PB, 740, PB) + SV.text(62, 24, "$", "sm");
  o += SV.rect(160, PB - PH(tc), 110, PH(tc), "f2") + SV.text(215, PB - PH(tc) - 8, "$5,200", "lbl bd t2", { "text-anchor": "middle" }) + SV.text(215, PB + 20, "Total cost", "sm bd", { "text-anchor": "middle" }) + SV.text(215, PB + 38, "(includes normal profit)", "sm", { "text-anchor": "middle" });
  o += SV.rect(420, PB - PH(r), 110, PH(r), ok ? "f3" : eq ? "f4" : "f1") + SV.text(475, PB - PH(r) - 8, "$" + Math.round(r / 10) * 10, "lbl bd", { "text-anchor": "middle" }) + SV.text(475, PB + 20, "Total revenue", "sm bd", { "text-anchor": "middle" }) + SV.text(475, PB + 38, "(price × 500)", "sm", { "text-anchor": "middle" });
  o += SV.text(640, PB - 100, ok ? "supernormal profit" : eq ? "normal profit only" : "subnormal profit", "lbl bd " + (ok ? "t3" : eq ? "t4" : "t2"), { "text-anchor": "middle" });
  return o;
}
Lib.stepper($("#stP2"), { w: 780, h: 320, label: "Total revenue against total cost, showing supernormal, normal and subnormal profit", base: { r: 5200 }, draw: profDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>Total cost is $5,200</b>, including <b>normal profit</b>: the minimum return that keeps the entrepreneur in the industry. If total revenue equals total cost, the firm earns normal profit and is content to stay.", s: { r: 5200 } },
  { cap: "<b>Price $12.</b> Total revenue = 12 × 500 = $6,000, which is $800 more than total cost. That extra $800 is <b>supernormal profit</b>: it may attract new firms unless there are barriers to entry.", s: { r: 6000 } },
  { cap: "<b>Price $10.40.</b> Total revenue = $5,200 equals total cost: only <b>normal profit</b>. There is no incentive to enter or leave.", s: { r: 5200 } },
  { cap: "<b>Price $9.</b> Total revenue = $4,500, which is $700 below total cost. The firm earns <b>subnormal profit</b>, less than the minimum needed. In the long run it may leave the industry.", s: { r: 4500 } },
] });
''' + S.j_((113, 142)) + '''
/* ---------- Practise ---------- */
Lib.match($("#m1"), { prompt: "Match each term to its meaning.", pairs: [
  ["Total revenue", "Price × quantity sold"],
  ["Average revenue", "Total revenue ÷ quantity, equal to the price"],
  ["Marginal revenue", "The extra revenue from selling one more unit"],
  ["Price taker", "A firm facing a horizontal demand curve that must accept the market price"],
  ["Normal profit", "The minimum return needed to keep the firm in the industry, included in total cost"],
  ["Supernormal profit", "Profit above normal profit: TR greater than TC"],
  ["Subnormal profit", "Profit below normal profit: TR less than TC"],
], done: "Seven terms for revenue and profit." });
''' + calc(S, (183, 184), '''  { q: "Demand is P = 20 − Q. What is marginal revenue at Q = 6 (MR = 20 − 2Q)?", a: 8, sol: "20 − 2 × 6 = <b>$8</b>." },
  { q: "At what output is total revenue greatest for P = 20 − Q?", a: 10, sol: "MR = 20 − 2Q = 0 gives Q = <b>10</b>." },
  { q: "A firm sells 400 units at $9.50 each and total cost (including normal profit) is $3,600. What is its supernormal profit ($)?", a: 200, sol: "TR = 3,800; 3,800 − 3,600 = <b>$200</b>." },
''') + qz(S, (189, 191), '''  { q: "Total revenue is $4,500 and total cost, including normal profit, is $5,200. The firm earns:", opts: ["supernormal profit", "normal profit", "subnormal profit", "zero total revenue"], a: 2, why: "Revenue is less than total cost, which already includes normal profit." },
''') + cards(S, tuple(range(207, 212))) + '''
/* ---------- Draw it. Explain it. Apply it. ---------- */
const PROMPTS = [
''' + S.j_((221, 222)) + '''];
''' + S.j_((224, 232)) + mcq(S, (), '''  { q: "[May/June 2020 (not sat) · 32 · Q8] At which level of output will a firm achieve the aim of sales maximisation?", opts: ["where AC = AR", "where AC = MC", "where MC = AR", "where MR = zero"], a: 0, why: "Sales maximisation subject to a minimum profit is at AR = AC, where only normal profit is earned. MR = 0 is revenue maximisation." },
  { q: "[Feb/March 2025 · 32 · Q7] A profit-maximising monopoly makes an abnormal profit and decides to reinvest some of this profit to improve its capital stock. What are the most likely outcomes from this change? (allocative, dynamic, productive efficiency)", opts: ["improves, improves, improves", "unchanged, improves, improves", "improves, unchanged, unchanged", "unchanged, unchanged, improves"], a: 1, why: "Investing improves capital and lowers costs over time (dynamic and productive efficiency), but price is still above marginal cost, so allocative efficiency is unchanged." },
  { q: "[Feb/March 2023 · 32 · Q6] What is achieved in monopolistic competition in the long run? (allocative efficiency, supernormal profit)", opts: ["no, no", "no, yes", "yes, no", "yes, yes"], a: 0, why: "Entry removes supernormal profit in the long run, but price stays above marginal cost, so there is no allocative efficiency." },
''')
write("fi3", page(EY.format(3), "Revenue and Profit",
  "Total, average and marginal revenue for price takers and price makers, and normal, subnormal and supernormal profit. Animated diagrams, labs, drills and the past paper questions.",
  learn_class=LEG, learn=learn, watch=watch, explore=explore, practise=practise, real=real, exam=exam, tips=tips), js,
  "Revenue and Profit", "revenue-and-profit")
