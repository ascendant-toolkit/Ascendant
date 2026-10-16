"""Builds the three ch36 part pages (gs1..gs3) from slices of gs.* plus new content. Run: python3 tools/artifact-kit/mk_ch36.py"""
from splitter import *
mktips = tips
S = Src("gs")
HEAD = S.j_((1, 14))
EY = "A Level Economics · 9708 · Syllabus 7.7 · Part {} of 3"
RW = '<p class="note">Examples are explained in general terms. Check current details before quoting them in an exam answer.</p>\n'

# ------------------------------------------------------------------ 36.1
learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>Firms grow for reasons such as <b>lower costs</b> from economies of scale, <b>market power</b>, <b>spreading risk</b> and the aims of owners and managers. They can grow <b>organically</b>, using their own profits and resources, or <b>externally</b> by joining with another firm in a <b>merger</b> (two firms agree to form one) or a <b>takeover</b> (one firm buys another). A deal is <b>horizontal</b> (same stage, same industry), <b>vertical</b> (backward to a supplier or forward to a customer) or <b>conglomerate</b> (unrelated). Naming the type correctly is the first mark in many answers.</p></div>
''' + S.b((25, 32), (33, 41), (42, 52))
watch = S.b((107, 109)).replace("2 · Four ways", "1 · Four ways")
explore = '''
  <h2>Lab 1 · What type of deal is it?</h2>
  <p>A bakery is in the middle of a supply chain: flour suppliers before it, cafés after it. Choose who the bakery buys and see how the deal is classified.</p>
  <div class="card"><div class="grid2"><div><div id="g8"></div>
    <div class="readout"><div><small>Target</small><strong id="a1"></strong></div><div><small>Type of integration</small><strong id="a2"></strong></div><div><small>Typical motive</small><strong id="a3"></strong></div></div>
    <div class="verdict" id="av"></div></div>
    <div><svg id="labV" viewBox="0 0 420 280" role="img" aria-label="Supply chain with the bakery in the middle and the target of the deal highlighted"></svg></div></div></div>
'''
practise = S.b((145, 146)) + '''
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Calculations</h2><div id="c1"></div>
  <h2>4 · Multiple choice</h2><div id="qz1"></div>
'''
real = RW + S.b((167, 168), (170, 170), (172, 172))
exam = '''
  <h2>Past paper questions on growth and integration</h2>
  <p>We searched the A Level Economics papers in the folder (2020 to 2025). The long written questions on mergers and takeovers are in part 3, because they ask about their effects. Here is a practice question with a model answer on types of growth, and Paper 3 multiple choice questions on the types of integration. Mark scheme points are summarised in our own words, not copied.</p>
  <div class="tw"><table class="t">
    <tr><th>Type</th><th>Examples found</th><th>Where</th></tr>
    <tr><td>Multiple choice (Paper 3)</td><td>7 shown below</td><td>2020 to 2024</td></tr>
    <tr><td>Longer questions on mergers and takeovers</td><td>See part 3</td><td>2020 to 2025</td></tr>
  </table></div>
  <h2>A · Practice question with a model answer</h2>
  <details class="eq"><summary>Practice (not a past paper question) <span class="mark">8 marks</span> Explain the difference between a merger and a takeover and between horizontal and vertical integration.</summary><div class="body">
    <div class="tip"><b class="h">Plan</b>Define merger and takeover. Define horizontal, backward vertical and forward vertical integration with an example of each. Link one to a likely motive.</div>
''' + KEYS + '''
    <div class="ans">
    <p><span class="mk k" data-t="K">A merger is an agreement between two firms to join together to form a single new company, while a takeover is when one firm buys another, usually by buying a majority of its shares. Both are forms of external growth, as opposed to organic growth from a firm's own resources.</span></p>
    <p><span class="mk k" data-t="K">Horizontal integration joins firms at the same stage of production in the same industry, such as two supermarket chains. Vertical integration joins firms at different stages: backward integration is with a supplier, such as a bakery buying a flour mill, and forward integration is with a customer, such as a bakery buying a chain of cafés.</span></p>
    <p><span class="mk a" data-t="A">A horizontal deal is likely to be motivated by economies of scale and greater market share, which could give more market power. A backward deal may secure supplies and cut costs, while a forward deal may secure outlets for the firm's products.</span> <span class="mk e" data-t="E">Which motive is likely to dominate may depend on the industry, because a horizontal deal may draw a competition authority's attention in a way a vertical deal does not.</span></p></div>
  </div></details>
''' + MCQTAIL.format("B · Multiple choice questions (Paper 3)")
tips = mktips(S, (279, 280), '', (292, 293)) + cmd(CW["explain"], CW["consider"]) + FC
js = HEAD + S.j_((47, 81)) + '''
/* ---------- Lab 1: type of deal ---------- */
function labDeal() {
  if (!$("#tg")) return;
  const t = +$("#tg").value, names = ["A flour mill (a supplier)", "A rival bakery", "A chain of cafés (a customer)", "A mobile phone maker"], types = ["Backward vertical", "Horizontal", "Forward vertical", "Conglomerate"], mot = ["Secure supplies and cut input costs", "Economies of scale and market share", "Secure outlets for the bakery's products", "Spread risk by diversifying"];
  const why = ["The target is earlier in the supply chain.", "The target is in the same industry at the same stage.", "The target is later in the supply chain, closer to the customer.", "The target is in an unrelated industry."];
  $("#a1").textContent = ["Flour mill", "Rival bakery", "Café chain", "Phone maker"][t]; $("#a2").textContent = types[t]; $("#a3").textContent = ["Secure supplies", "Economies of scale", "Secure outlets", "Spread risk"][t];
  $("#av").textContent = `The bakery buys ${names[t].toLowerCase()}. ${why[t]} This is ${types[t].toLowerCase()} integration. Typical motive: ${mot[t].toLowerCase()}.`;
  const box = (x, y, w, h, l, on, c) => SV.rect(x, y, w, h, on ? c : "f1", { opacity: on ? 0.95 : 0.35, rx: 8 }) + SV.text(x + w / 2, y + h / 2 + 4, l, "lbl bd", { "text-anchor": "middle", style: "paint-order:stroke;stroke:var(--surface);stroke-width:4px" });
  let o = box(20, 100, 100, 50, "Flour mill", t === 0, "f4") + box(160, 100, 100, 50, "Bakery", true, "f1") + box(300, 100, 100, 50, "Cafés", t === 2, "f3") + box(160, 10, 100, 50, "Rival bakery", t === 1, "f2") + box(160, 200, 100, 50, "Phone maker", t === 3, "f4");
  o += SV.line(120, 125, 160, 125, "gr", { "stroke-width": 2 }) + SV.line(260, 125, 300, 125, "gr", { "stroke-width": 2 }) + SV.text(70, 175, "backward", "sm", { "text-anchor": "middle" }) + SV.text(350, 175, "forward", "sm", { "text-anchor": "middle" }) + SV.text(110, 40, "horizontal", "sm", { "text-anchor": "end" }) + SV.text(110, 232, "conglomerate", "sm", { "text-anchor": "end" });
  $("#labV").innerHTML = o;
}
Lib.slider($("#g8"), { id: "tg", label: "Who does the bakery buy? (0 supplier, 1 rival, 2 café chain, 3 unrelated firm): ", min: 0, max: 3, step: 1, value: 0, fmt: (v) => v, onInput: labDeal });

/* ---------- Practise ---------- */
''' + S.j_((154, 163)) + '''Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Organic growth", "Growth using the firm's own resources"],
  ["Merger", "Two firms agree to join and form one new company"],
  ["Takeover", "One firm buys another, usually by buying its shares"],
  ["Horizontal integration", "Joining with a firm in the same industry at the same stage"],
  ["Backward vertical integration", "Buying a firm earlier in the supply chain, such as a supplier"],
  ["Forward vertical integration", "Buying a firm later in the supply chain, such as a retailer"],
  ["Conglomerate integration", "Joining with a firm in an unrelated industry"],
  ["Demerger", "A firm splits into separate businesses"],
], done: "Eight words for the types of growth." });
''' + calc(S, (196, 197), '''  { q: "A bidder offers $12 a share for a company with 5 million shares. What is the total value of the bid ($ million)?", a: 60, sol: "12 × 5 = <b>$60 million</b>." },
  { q: "A firm's sales rise from $50 million to $55 million through organic growth. What is the growth rate (%)?", a: 10, sol: "(55 − 50) ÷ 50 × 100 = <b>10%</b>." },
''') + qz(S, (202, 203, 207), '''  { q: "A takeover is best described as:", opts: ["two firms agreeing to form a new company", "one firm buying another", "a firm growing by retained profit", "a firm closing down"], a: 1, why: "One firm buys another, usually by acquiring a majority of its shares." },
''') + cards(S, tuple(range(210, 220))) + mcq(S, (229, 236, 237, 238, 240, 241), '''  { q: "[May/June 2024 · 31 · Q9] A major UK chemical firm was bought by its rival, a Dutch chemical firm. What definitely occurred when the Dutch firm bought the UK firm?", opts: ["a partnership", "economies of scale", "horizontal integration", "increased profits"], a: 2, why: "Both firms are in the same industry at the same stage, so it is horizontal integration. Economies of scale and higher profits are possible but not certain." },
''')
write("gs1", page(EY.format(1), "Why and How Firms Grow: Organic Growth, Mergers and Integration",
  "Why firms grow, organic against external growth, mergers and takeovers, and horizontal, vertical and conglomerate integration. Animated supply chains, labs, drills and the past paper questions.",
  learn=learn, watch=watch, explore=explore, practise=practise, real=real, exam=exam, tips=tips), js,
  "Why and How Firms Grow: Organic Growth, Mergers and Integration", "why-and-how-firms-grow")

# ------------------------------------------------------------------ 36.2
learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>The <b>long-run average cost (LRAC)</b> curve is usually U-shaped. While it falls, the firm enjoys <b>economies of scale</b>; at the lowest point it reaches <b>minimum efficient scale (MES)</b>; beyond that it may face <b>diseconomies of scale</b> from problems of management and communication. The size of MES compared with the market decides how many firms can survive at the lowest cost: a small MES means room for many firms, a large MES leaves room for only a few. Growth is therefore not always good: costs can rise, and several things limit how far a firm can grow.</p></div>
''' + S.b((68, 73), (74, 76)).replace("5 · What limits", "1 · What limits").replace("6 · The picture", "2 · The picture") + '''
  <h2>3 · Types of economy of scale</h2>
  <div class="tw"><table class="t">
    <tr><th>Economy</th><th>Meaning</th><th>Example</th></tr>
    <tr><td><b>Technical</b></td><td>Larger machines and more efficient processes at high output</td><td>A bigger oven that bakes more loaves for the same fuel</td></tr>
    <tr><td><b>Purchasing</b></td><td>Discounts on bulk buying</td><td>A supermarket chain negotiating prices with suppliers</td></tr>
    <tr><td><b>Financial</b></td><td>Cheaper borrowing for a large firm</td><td>Lower interest rates for a well-known company</td></tr>
    <tr><td><b>Managerial</b></td><td>Specialist managers become affordable</td><td>A separate finance director</td></tr>
    <tr><td><b>Marketing</b></td><td>Advertising costs spread over more output</td><td>A national campaign costs little per unit</td></tr>
  </table></div>
  <p><b>Diseconomies of scale</b> come from slower decisions, poorer communication, weaker motivation and difficulty coordinating, so LRAC rises beyond MES. Economies of scale are <b>internal</b> when they come from the firm's own size; <b>external</b> economies come from the growth of the industry (for example a skilled labour force nearby).</p>
'''
watch = '''
  <h2>1 · Build the LRAC curve</h2><p>Press Play, or click the steps.</p><div id="stA"></div>
'''
explore = S.b((114, 119), (121, 126))
practise = '''
  <h2>1 · Economy or diseconomy of scale?</h2><div id="cl1" class="card"></div>
  <h2>2 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Calculations</h2><div id="c1"></div>
  <h2>4 · Multiple choice</h2><div id="qz1"></div>
'''
real = RW + '''  <div class="rw"><h3>Supermarket buying power</h3><p>A large supermarket chain buys in huge quantities and can negotiate discounts from suppliers, which is a purchasing economy of scale. A small corner shop cannot match that unit cost on the same goods.</p><div class="use"><b>Exam use:</b> a purchasing economy of scale. Evaluate: savings may not be passed on, and suppliers may be squeezed.</div></div>
  <div class="rw"><h3>A very large organisation</h3><p>A company with many divisions in many countries may find decisions slow, communication poor and staff less motivated. Some large firms have been broken up or have sold divisions to cut costs.</p><div class="use"><b>Exam use:</b> diseconomies of scale, and a reason why growth may not lower unit costs.</div></div>
  <div class="rw"><h3>Car plants and minimum efficient scale</h3><p>Making cars needs very large plants to reach the lowest cost, so MES is a big share of the market. Only a few firms can reach it, which is a barrier to entry.</p><div class="use"><b>Exam use:</b> a large MES relative to the market means few firms; a small MES means many.</div></div>
'''
exam = '''
  <h2>Past paper questions on economies of scale and the limits to growth</h2>
  <p>We searched the A Level Economics papers in the folder (2020 to 2025). Below are the 13 mark question on economies of scale, a practice question with a model answer, and Paper 3 multiple choice questions. Mark scheme points are summarised in our own words, not copied.</p>
  <div class="tw"><table class="t">
    <tr><th>Type</th><th>Examples found</th><th>Where</th></tr>
    <tr><td>Essay part, 13 marks</td><td>1</td><td>May/June 2022 (42)</td></tr>
    <tr><td>Multiple choice (Paper 3)</td><td>4 shown below</td><td>2020 to 2023</td></tr>
  </table></div>
  <h2>A · A 13 mark question</h2>
''' + KEYL + S.b((256, 264)) + '''
  <h2>B · Practice question with a model answer</h2>
  <details class="eq"><summary>Practice (not a past paper question) <span class="mark">8 marks</span> Explain what is meant by economies of scale and why long-run average cost may rise beyond minimum efficient scale.</summary><div class="body">
    <div class="tip"><b class="h">Plan</b>Define economies of scale and MES. Give two types with examples. Explain diseconomies and say what happens to LRAC.</div>
''' + KEYS + '''
    <div class="ans">
    <p><span class="mk k" data-t="K">Economies of scale are falls in long-run average cost as a firm increases its output. The minimum efficient scale is the lowest output at which long-run average cost is at its minimum.</span></p>
    <p><span class="mk a" data-t="A">A supermarket chain may buy in bulk and negotiate lower prices from suppliers (a purchasing economy), and a large manufacturer may use specialised machinery (a technical economy), so each loaf or product costs less to produce.</span> <span class="mk n" data-t="N">Beyond minimum efficient scale, long-run average cost may rise because of diseconomies of scale. As the firm becomes very large, communication may become slower and decisions more complicated, and workers may feel less motivated, so costs per unit could increase.</span> <span class="mk e" data-t="E">Whether a firm reaches diseconomies may depend on how well it is managed, because firms with good systems might delay them.</span></p></div>
  </div></details>
''' + MCQTAIL.format("C · Multiple choice questions (Paper 3)")
tips = mktips(S, (281,), '''    <li><b>Label the LRAC curve:</b> economies of scale on the falling part, MES at the minimum, diseconomies on the rising part.</li>
    <li><b>Say which type of economy it is,</b> technical, purchasing, financial, managerial or marketing, and give an example.</li>
''', (294,)) + cmd(CW["explain"], CW["discuss"], CW["consider"]) + FC
js = HEAD + S.j_((15, 46), (82, 115)) + '''
/* ---------- Practise ---------- */
Lib.classify($("#cl1"), {
  prompt: "Is each cause an economy or a diseconomy of scale?",
  buckets: [{ label: "Economy of scale" }, { label: "Diseconomy of scale" }],
  items: [
    { text: "Bulk-buying discounts from suppliers", b: 0 }, { text: "Cheaper borrowing for a large firm", b: 0 }, { text: "Specialist managers become affordable", b: 0 }, { text: "Larger machines cut cost per unit", b: 0 }, { text: "Advertising costs spread over more units", b: 0 },
    { text: "Decisions slow down as layers of management grow", b: 1 }, { text: "Workers feel less motivated in a very large firm", b: 1 }, { text: "Communication between divisions becomes poor", b: 1 }, { text: "Difficulty coordinating many sites", b: 1 },
  ], done: "Economies lower unit cost as output grows; diseconomies raise it beyond MES.",
});
Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Long-run average cost", "Cost per unit when all inputs can be changed"],
  ["Economies of scale", "A fall in LRAC as output rises"],
  ["Diseconomies of scale", "A rise in LRAC as output rises beyond MES"],
  ["Minimum efficient scale", "The smallest output at which LRAC is lowest"],
  ["Internal economies", "Savings that come from the size of the firm itself"],
  ["External economies", "Savings that come from the growth of the whole industry"],
  ["Barrier to entry", "Something that makes it hard for new firms to join a market"],
], done: "Seven words for costs and size." });
''' + calc(S, (195, 198), '''  { q: "A firm produces 100 units at a total cost of $1,000, then 200 units at a total cost of $1,600. What is the average cost at 200 units ($)?", a: 8, sol: "1,600 ÷ 200 = <b>$8</b>, down from $10: economies of scale." },
  { q: "MES is 20% of the market. About how many firms can reach MES?", a: 5, sol: "100 ÷ 20 = <b>5</b> firms." },
''') + qz(S, (205,), '''  { q: "Falling long-run average cost as output rises shows:", opts: ["diseconomies of scale", "economies of scale", "constant returns", "a barrier to entry"], a: 1, why: "Economies of scale are falls in LRAC as output rises." },
  { q: "Which is a technical economy of scale?", opts: ["A bulk discount on materials", "A larger, more efficient machine", "Cheaper loans", "Advertising spread over more output"], a: 1, why: "Technical economies come from the production process and equipment." },
  { q: "If the minimum efficient scale is a small share of the market:", opts: ["only a few firms can reach it", "many firms can reach it", "no firm can survive", "all firms are monopolies"], a: 1, why: "A small MES leaves room for many firms operating at the lowest cost." },
''') + cards(S, tuple(range(220, 223))) + mcq(S, (239,), '''  { q: "[Feb/March 2020 · 32 · Q10] What is true about economies of scale but not diseconomies of scale?", opts: ["They occur because average revenue is increasing.", "They occur because of management policy changes.", "They occur in the short run.", "They occur with decreasing average cost."], a: 3, why: "Economies of scale are falling average cost as output rises; diseconomies are rising average cost." },
  { q: "[May/June 2023 · 31 · Q4] Which type of efficiency is shown by the shift from long-run average cost curve 1 (LRAC1) to long-run average cost curve 2 (LRAC2), where LRAC2 is below LRAC1?", opts: ["allocative", "dynamic", "Pareto", "productive"], a: 1, why: "A downward shift of the LRAC curve over time shows dynamic efficiency." },
  { q: "[May/June 2022 · 31 · Q8] Firms often remain small even when growth could result in technical economies of scale. What is not a likely reason for this?", opts: ["Demand for the product tends to change often and rapidly.", "Individual entrepreneurs wish to keep a tight personal control over their own firm.", "The entrepreneurs who establish the firms tend to be ambitious risk-takers.", "The market in which they operate is very specialised in nature, often selling unique products."], a: 2, why: "Ambitious risk-takers would be expected to grow their firms, so this is not a reason for staying small." },
''')
write("gs2", page(EY.format(2), "Economies of Scale, LRAC and the Limits to Growth",
  "The long-run average cost curve, economies and diseconomies of scale, minimum efficient scale and how many firms a market can hold. Animated diagrams, labs, drills and the past paper questions.",
  learn=learn, watch=watch, explore=explore, practise=practise, real=real, exam=exam, tips=tips), js,
  "Economies of Scale, LRAC and the Limits to Growth", "economies-of-scale-lrac-limits-to-growth")

# ------------------------------------------------------------------ 36.3
learn = '''
  <div class="card big"><h3>This part in four sentences</h3>
  <p>A merger or takeover can <b>benefit consumers</b> through economies of scale passed on in lower prices, and can benefit the firm through more profit, but it can also create <b>market power</b>, fewer rivals and higher prices. Whether consumers gain depends on how big the cost saving is, how much is passed on and how much competition remains, which is why competition authorities review large deals. Small firms survive in the same economy because <b>cost is not the only thing customers value</b>: niche products, personal service, flexibility and small markets protect them. Both sides of the argument are needed for evaluation.</p></div>
''' + S.b((53, 67)).replace("4 · Effects", "1 · Effects") + S.b((78, 98)).replace("7 · Why do small", "2 · Why do small")
watch = '''
  <h2>1 · A takeover and the consumer</h2>
  <p>Before the takeover the price is $10 and unit cost $8. Press Play, or click the steps.</p><div id="stT"></div>
'''
explore = S.b((128, 133), (135, 140)).replace("Lab 3 ·", "Lab 1 ·").replace("Lab 4 ·", "Lab 2 ·")
practise = S.b((148, 149)).replace("2 · Helps", "1 · Helps") + '''
  <h2>2 · Put the argument in order</h2><div id="o1" class="card"></div>
  <h2>3 · Match the word to its meaning</h2><div id="m1" class="card"></div>
  <h2>4 · Calculations</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''
real = RW + S.b((169, 169), (171, 171)) + '''  <div class="rw"><h3>A merger blocked or approved with conditions</h3><p>Competition authorities sometimes block large mergers or approve them only if the firms sell off parts of the business, because the merged firm could raise prices. The authority weighs possible higher prices against cost savings.</p><div class="use"><b>Exam use:</b> the 2023 merger question. Draw the diagram, show a cost saving against a price rise, and evaluate.</div></div>
'''
exam = '''
  <h2>Past paper questions on the effects of mergers and the survival of small firms</h2>
  <p>We searched the A Level Economics papers in the folder (2020 to 2025). Below are the essays on the effects of takeovers and mergers and the role of small firms, the data response parts and Paper 3 multiple choice questions. Mark scheme points are summarised in our own words, not copied.</p>
  <div class="tw"><table class="t">
    <tr><th>Type</th><th>Examples found</th><th>Where</th></tr>
    <tr><td>Essay, 20 marks</td><td>2</td><td>May/June 2025 (41, 43); Oct/Nov 2023 (41)</td></tr>
    <tr><td>Essay parts, 13 marks</td><td>3</td><td>Oct/Nov 2020 (41, 42); Oct/Nov 2021 (43)</td></tr>
    <tr><td>Data response parts, 8 marks</td><td>2</td><td>Feb/March 2021 (42); Oct/Nov 2024 (43)</td></tr>
    <tr><td>Multiple choice (Paper 3)</td><td>6 shown below</td><td>2020 to 2024</td></tr>
  </table></div>
  <h2>A · Essay questions</h2>
''' + KEYL + S.b((190, 205), (207, 215), (217, 235), (237, 245), (247, 254)) + '''
  <h2>B · Data response questions</h2>
''' + S.b((267, 268)) + '''
''' + MCQTAIL.format("C · Multiple choice questions (Paper 3)")
tips = mktips(S, (282, 283, 284, 285, 286), '', (295, 296, 297)) + cmd(CW["discuss"], CW["evaluate"], CW["consider"]) + FC
js = HEAD + '''
/* ---------- Watch: takeover and the consumer ---------- */
const TB = 270, TH = (v) => v * 20;
function takeDraw(s) {
  let o = SV.line(60, TB, 740, TB) + SV.text(62, 24, "$ per unit", "sm");
  const bar = (x, v, c, l, k, t) => k > 0 ? SV.rect(x, TB - TH(v), 64, TH(v), c, { opacity: k }) + SV.text(x + 32, TB - TH(v) - 6, t, "lbl bd", { "text-anchor": "middle", opacity: k }) + SV.text(x + 32, TB + 18, l, "sm", { "text-anchor": "middle", opacity: k }) : "";
  o += bar(90, 10, "f1", "Price", s.a, "$10.00") + bar(170, 8, "f2", "Cost", s.a, "$8.00") + (s.a > 0 ? SV.text(165, TB + 42, "Before", "lbl bd", { "text-anchor": "middle" }) : "");
  o += bar(310, 7.2, "f3", "Cost", s.b, "$7.20") + bar(390, 9.6, "f1", "Price", s.c, "$9.60") + (s.b > 0 ? SV.text(385, TB + 42, "After: saving passed on", "lbl bd", { "text-anchor": "middle" }) : "");
  o += bar(560, 7.2, "f3", "Cost", s.d, "$7.20") + bar(640, 10.6, "f4", "Price", s.d, "$10.60") + (s.d > 0 ? SV.text(635, TB + 42, "After: market power", "lbl bd", { "text-anchor": "middle" }) : "");
  return o;
}
Lib.stepper($("#stT"), { w: 780, h: 320, label: "Price and unit cost before a takeover, after it with savings passed on and after it with greater market power", base: { a: 0, b: 0, c: 0, d: 0 }, draw: takeDraw, tween: 800, dwell: 5600, steps: [
  { cap: "<b>Before the takeover.</b> The firm sells at <b>$10</b> and unit cost is <b>$8</b>, so profit is $2 a unit.", s: { a: 1 } },
  { cap: "<b>Economies of scale.</b> A larger firm cuts unit cost by 10% to <b>$7.20</b>, a saving of $0.80 a unit.", s: { a: 1, b: 1 } },
  { cap: "<b>Competition passes on half.</b> If rivals keep competition strong, the firm passes half of the saving to consumers: price falls to <b>$9.60</b> and profit rises to $2.40. Consumers <b>and</b> the firm gain.", s: { a: 1, b: 1, c: 1 } },
  { cap: "<b>Market power instead.</b> If the takeover removes a rival and the firm can raise price by 10% while still passing on half the saving, price is <b>$10.60</b>. Costs fall but consumers pay more: the gain goes to the firm, which is why authorities may block some deals.", s: { a: 1, b: 0.4, c: 0.4, d: 1 } },
] });
''' + S.j_((117, 151)) + '''
/* ---------- Practise ---------- */
''' + S.j_((164, 173), (184, 191)) + '''Lib.match($("#m1"), { prompt: "Match each word to its meaning.", pairs: [
  ["Market power", "The ability of a firm to influence price"],
  ["Concentration ratio", "The combined market share of the largest few firms"],
  ["Competition authority", "A body that reviews mergers and can block them"],
  ["Niche market", "A small specialist part of a market"],
  ["Economies of scale", "A fall in LRAC as output rises"],
  ["Contestable market", "A market where rivals can enter easily"],
  ["Public interest", "The overall benefit to consumers and society"],
], done: "Seven words for the effects of mergers." });
''' + calc(S, (193, 194, 199), '''  { q: "A takeover cuts unit cost from $8 to $7.20 and the price was $10. The firm passes on half of the saving. What is the new price ($)?", a: 9.6, tol: 0.01, sol: "Saving 0.80; half is 0.40; 10 − 0.40 = <b>$9.60</b>." },
''') + qz(S, (204, 206), '''  { q: "A takeover removes a rival and the merged firm raises price. Consumers are:", opts: ["better off", "worse off", "unaffected", "certain to gain from economies of scale"], a: 1, why: "A higher price with fewer rivals reduces consumer welfare, even if costs fall." },
''') + cards(S, (223, 224)) + mcq(S, (230, 231, 232, 233, 234, 235))
write("gs3", page(EY.format(3), "Effects of Mergers and Takeovers, and the Survival of Small Firms",
  "Whether mergers and takeovers help or harm consumers, why competition authorities review them, and why small firms survive next to large ones. Animated diagrams, labs, drills and the past paper questions.",
  learn=learn, watch=watch, explore=explore, practise=practise, real=real, exam=exam, tips=tips), js,
  "Effects of Mergers and Takeovers, and the Survival of Small Firms", "effects-of-mergers-and-small-firms")
