"""Builds the three ch35 part pages (mk1..mk3) from slices of mkt.* plus new content. Run: python3 tools/artifact-kit/mk_ch35.py
The Learn and Explore tabs keep their legacy styling, so mkt.css is copied next to each part."""
import shutil
from splitter import *
mktips = tips
S = Src("mkt")
HEAD = "// uses: econ\n"
EY = "A Level Economics · 9708 · Syllabus 7.6 · Part {} of 3"
for n in ("mk1", "mk2", "mk3"): shutil.copy(D / "mkt.css", D / f"{n}.css")
def renum(t, start):
    import re
    c = [start - 1]
    def f(m): c[0] += 1; return f'<span class="topic-num">{c[0]}</span>'
    return re.sub(r'<span class="topic-num">\d+</span>', f, t)
EXNOTE = '<p>The exam-style questions below were written for this page (open each one for reminders, a model answer and the common mistake). The Paper 3 multiple choice questions are real past paper questions: choose an answer, then read the reason. Mark scheme points are summarised in our own words, not copied.</p>\n'
KEYEX = '<div class="key" aria-label="Colour key"><span class="k"><i></i>Knowledge (K)</span><span class="a"><i></i>Application (A)</span><span class="n"><i></i>Analysis (N)</span><span class="e"><i></i>Evaluation (E)</span></div>\n'
LEGNOTE = '<p class="note">Tap or hover a key term for its definition. The interactive labs are on the Explore tab.</p>\n'
RWNOTE = '<p class="note">Examples are explained in general terms so they stay true. Look up current figures before quoting them in an exam answer.</p>\n'
def labs_js(labs, prompts):
    return S.j_((143, 205), *labs) + "/* ---------- practice ---------- */\nvar PROMPTS=[\n" + S.j_(*[(i, i) for i in prompts]) + "];\n" + S.j_((385, 393)) + "\n})();\n" + S.j_((396, 445))
PRACT = '''
  <h2>{}</h2>
  <p>Sketch each diagram in your notebook, then explain it in your own words and apply it to a real firm.</p>
  <div id="promptList"></div>
'''
TIPSTAIL = '  <h2>Keyword flashcards</h2>\n  <p>Click the card to flip it. Mark the ones you know.</p>\n  <div id="fc1"></div>\n'

# ------------------------------------------------------------------ 35.1
learn = LEGNOTE + renum(S.b((21, 37), (40, 62)), 1)
watch = '''
  <h2>1 · Perfect competition: price, profit and the shutdown point</h2>
  <p>Press Play, or click the steps.</p><div id="stA"></div>
'''
explore = '<p>Drag the sliders and read the verdict under the chart.</p>\n' + S.b((191, 200))
practise = S.b((250, 252)) + '''
  <h2>2 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>3 · Long-run adjustment in perfect competition</h2><div id="o1" class="card"></div>
  <h2>4 · Calculations</h2>
  <p>Enter numbers only.</p>
  <div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
''' + PRACT.format("6 · Draw it. Explain it. Apply it.")
real = RWNOTE + S.b((275, 275)) + '''  <div class="rw"><h3>A street market of identical stalls</h3><p>Many traders sell almost identical vegetables, buyers can compare prices at a glance and new traders can set up easily. No trader can charge much more than the going price, and a trader who charges less gives away profit.</p><div class="use"><b>Exam use:</b> price taking, free entry and exit, and supernormal profit being competed away.</div></div>
'''
exam = '''
  <h2>Exam questions on perfect competition and concentration</h2>
  ''' + EXNOTE + KEYEX + S.b((296, 300)) + MCQTAIL.format("Paper 3 multiple choice questions")
tips = '<h2>Top tips</h2>\n  <ul class="tips">\n' + S.b((334, 334), (336, 338)) + '  </ul>\n' + cmd(("Define / State", "A precise meaning in one or two ideas."), ("Calculate", "Formula, substitution, answer with units."), CW["explain"]) + TIPSTAIL
js = HEAD + S.j_((2, 25), (80, 90)) + '''Lib.match($("#m1"), { prompt: "Match each term to its meaning.", pairs: [
  ["Price taker", "A firm that must accept the market price"],
  ["Shutdown price", "The lowest point of AVC: below it the firm closes in the short run"],
  ["Productive efficiency", "Producing at the lowest point of average total cost"],
  ["Allocative efficiency", "Producing where price equals marginal cost"],
  ["Concentration ratio", "The share of market sales held by the largest few firms"],
  ["Free entry and exit", "No barriers to firms joining or leaving the market"],
], done: "Six terms for the spectrum and perfect competition." });
''' + S.j_((99, 105)) + calc(S, (107, 108, 110), '''  { q: "A perfectly competitive firm has AVC of $6 at its lowest point. The market price falls to $5. In the short run should it stay open? (type yes or no)", t: ["no"], ph: "yes or no", sol: "Price is below the lowest AVC, so it cannot cover variable costs: <b>no</b>, it should shut down." },
''') + qz(S, (114,), '''  { q: "Which feature is found in perfect competition but not in monopolistic competition?", opts: ["many firms", "identical products", "profit-seeking firms", "free entry"], a: 1, why: "Perfect competition has homogeneous products; monopolistic competition has differentiated products." },
''') + cards(S, (121, 123, 124, 125, 133)) + labs_js([(206, 244)], (378,)) + mcq(S, (), '''  { q: "[Feb/March 2020 · 32 · Q2] What is correct if a firm in a perfectly competitive market is maximising its long-run profits? (it is allocatively efficient, it is productively efficient)", opts: ["no, no", "no, yes", "yes, no", "yes, yes"], a: 3, why: "In the long run the firm produces where price = MC (allocative efficiency) at the lowest point of ATC (productive efficiency)." },
''')
write("mk1", page(EY.format(1), "The Spectrum of Market Structures and Perfect Competition",
  "How market structures are defined, and perfect competition in the short run, at the shutdown point and in the long run. Animated diagrams, an interactive lab, drills and the past paper questions.",
  learn_class="legacy", explore_class="legacy", learn=learn, watch=watch, explore=explore, practise=practise, real=real, exam=exam, tips=tips), js,
  "The Spectrum of Market Structures and Perfect Competition", "market-spectrum-perfect-competition")

# ------------------------------------------------------------------ 35.2
learn = LEGNOTE + renum(S.b((65, 85), (88, 98)), 1)
watch = '''
  <h2>1 · Monopoly: restricted output, higher price</h2>
  <p>Press Play, or click the steps.</p><div id="stB"></div>
'''
explore = '<p>Drag the sliders and read the verdict under each chart.</p>\n' + S.b((202, 211), (213, 222)).replace("Lab 2 ·", "Lab 1 ·").replace("Lab 3 ·", "Lab 2 ·")
practise = '''
  <h2>1 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>2 · Calculations</h2>
  <p>Enter numbers only.</p>
  <div id="c1"></div>
  <h2>3 · Multiple choice</h2><div id="qz1"></div>
''' + PRACT.format("4 · Draw it. Explain it. Apply it.")
real = RWNOTE + S.b((276, 277)) + '''  <div class="rw"><h3>A pharmaceutical patent</h3><p>A patent gives a drug company the sole right to sell a new medicine for a period. It can charge a price well above cost and earn supernormal profit, which it may use to fund new research, until rivals can copy the drug.</p><div class="use"><b>Exam use:</b> a monopoly protected by a legal barrier to entry, with a price above marginal cost and possible dynamic efficiency.</div></div>
'''
exam = '''
  <h2>Exam questions on monopoly and monopolistic competition</h2>
  ''' + EXNOTE + KEYEX + S.b((290, 294), (302, 307), (317, 327)) + MCQTAIL.format("Paper 3 multiple choice questions")
tips = '<h2>Top tips</h2>\n  <ul class="tips">\n' + S.b((335, 335)) + '''    <li><b>For a monopoly, find MR = MC, then go up to the demand curve for the price.</b> Mark the deadweight loss between the monopoly output and the output where P = MC.</li>
    <li><b>In long-run monopolistic competition</b> demand touches ATC at a tangent, so only normal profit is earned, and output is below the lowest-cost output (excess capacity).</li>
''' + '  </ul>\n' + cmd(("Define / State", "A precise meaning in one or two ideas."), CW["explain"], CW["analyse"], CW["discuss"]) + TIPSTAIL
js = HEAD + S.j_((26, 49)) + '''Lib.match($("#m1"), { prompt: "Match each term to its meaning.", pairs: [
  ["Price maker", "A firm that faces a downward-sloping demand curve and chooses price by choosing output"],
  ["Barriers to entry", "Anything that stops or deters new firms joining a market"],
  ["Deadweight loss", "Welfare lost because output is below the socially best level"],
  ["Natural monopoly", "An industry where LRAC keeps falling over the range of market demand"],
  ["Product differentiation", "Making a product different through branding, quality or service"],
  ["Tangency solution", "Long-run position in monopolistic competition where demand just touches ATC"],
  ["Excess capacity", "Producing less than the output at the lowest point of ATC"],
], done: "Seven terms for monopoly and monopolistic competition." });
''' + calc(S, (109, 111), '''  { q: "A monopolist maximises profit where MR = MC. Demand is P = 20 − Q, so MR = 20 − 2Q, and MC = Q. What output does it produce (1 decimal place)?", a: 6.7, tol: 0.1, sol: "20 − 2Q = Q gives 3Q = 20, so Q = <b>6.7</b>. The price is read from demand: 20 − 6.7 = $13.3." },
  { q: "In long-run monopolistic competition, price equals ATC. If price is $8 and the firm sells 50 units, what is its total revenue ($)?", a: 400, sol: "8 × 50 = <b>$400</b>, equal to total cost: only normal profit." },
''') + qz(S, (115, 118), '''  { q: "A monopolist earns supernormal profit that lasts in the long run because of:", opts: ["free entry", "barriers to entry", "price taking", "perfect information"], a: 1, why: "Barriers stop new firms entering and competing the profit away." },
''') + cards(S, (122, 126, 127, 128, 129, 130, 131)) + labs_js([(246, 273), (275, 304)], (379, 380)) + mcq(S, (), '''  { q: "[Feb/March 2020 · 32 · Q11] What is most likely to be found when comparing the long-run equilibrium outcome in monopolistic competition with that in perfect competition?", opts: ["a greater degree of excess capacity in monopolistic competition", "a higher level of profit in monopolistic competition", "a larger number of firms in monopolistic competition", "a more price-elastic demand curve in monopolistic competition"], a: 0, why: "In monopolistic competition demand is tangent to ATC to the left of its lowest point, so firms produce below the efficient scale. Entry removes supernormal profit in both structures." },
  { q: "[Feb/March 2023 · 32 · Q6] What is achieved in monopolistic competition in the long run? (allocative efficiency, supernormal profit)", opts: ["no, no", "no, yes", "yes, no", "yes, yes"], a: 0, why: "Entry removes supernormal profit, but price stays above marginal cost, so there is no allocative efficiency." },
''')
write("mk2", page(EY.format(2), "Monopoly and Monopolistic Competition",
  "Price makers: monopoly with restricted output and a higher price, and monopolistic competition moving from supernormal to normal profit. Animated diagrams, interactive labs, drills and the past paper questions.",
  learn_class="legacy", explore_class="legacy", learn=learn, watch=watch, explore=explore, practise=practise, real=real, exam=exam, tips=tips), js,
  "Monopoly and Monopolistic Competition", "monopoly-monopolistic-competition")

# ------------------------------------------------------------------ 35.3
learn = LEGNOTE + renum(S.b((101, 124), (127, 137), (140, 154), (157, 170)), 1)
watch = '''
  <h2>1 · The prisoner's dilemma in oligopoly</h2>
  <p>Press Play, or click the steps.</p><div id="stC"></div>
'''
explore = '<p>Drag the sliders and read the verdict under each chart.</p>\n' + S.b((224, 233), (235, 245)).replace("Lab 4 ·", "Lab 1 ·").replace("Lab 5 ·", "Lab 2 ·")
practise = '''
  <h2>1 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>2 · Calculations</h2>
  <p>Enter numbers only.</p>
  <div id="c1"></div>
  <h2>3 · Multiple choice</h2><div id="qz1"></div>
''' + PRACT.format("4 · Draw it. Explain it. Apply it.")
real = RWNOTE + S.b((278, 281))
exam = '''
  <h2>Exam questions on oligopoly, collusion and contestability</h2>
  ''' + EXNOTE + KEYEX + S.b((309, 315)) + MCQTAIL.format("Paper 3 multiple choice questions")
tips = '<h2>Top tips</h2>\n  <ul class="tips">\n' + S.b((339, 341)) + '''    <li><b>Interdependence is the key idea.</b> Each firm's best choice depends on how rivals respond, which is why prices are sticky, collusion is tempting and cartels are unstable.</li>
''' + '  </ul>\n' + cmd(("Define / State", "A precise meaning in one or two ideas."), CW["explain"], CW["discuss"]) + TIPSTAIL
js = HEAD + S.j_((50, 78)) + '''Lib.match($("#m1"), { prompt: "Match each term to its meaning.", pairs: [
  ["Interdependence", "Each firm's best decision depends on how rivals respond"],
  ["Kinked demand curve", "Rivals ignore a price rise but match a cut, giving a kink and a gap in MR"],
  ["Collusion", "Firms co-operating to limit competition"],
  ["Cartel", "A formal agreement between firms to fix price or output"],
  ["Nash equilibrium", "No player can do better by changing strategy alone"],
  ["Contestable market", "A market with low sunk costs where entry and exit are easy"],
  ["X-inefficiency", "Costs above the lowest achievable level because of weak competition"],
  ["Concentration ratio", "The share of market sales held by the largest few firms"],
], done: "Eight terms for oligopoly." });
''' + calc(S, (), '''  { q: "Two airlines can each hold or cut fares. If both hold, each earns $10m. If both cut, each earns $6m. If one cuts and the other holds, the cutter earns $12m and the holder $4m. What does each earn if both cut ($m)?", a: 6, sol: "Both cutting gives <b>$6m</b> each, less than $10m each if both held fares: the prisoner's dilemma." },
  { q: "In the game above, if you expect your rival to hold, what is the best response? Compare $12m (cut) with $10m (hold). Type cut or hold.", t: ["cut"], ph: "cut or hold", sol: "$12m is more than $10m, so the best response is to <b>cut</b>." },
  { q: "The four largest firms have market shares of 25%, 20%, 15% and 10%. What is the four-firm concentration ratio (%)?", a: 70, sol: "25 + 20 + 15 + 10 = <b>70%</b>." },
''') + qz(S, (116, 117), '''  { q: "A market is contestable when:", opts: ["there is only one firm", "entry and exit are easy and cheap", "firms collude", "the product is differentiated"], a: 1, why: "The threat of entry disciplines incumbents even if there are few firms." },
''') + cards(S, tuple(range(132, 140)) if False else (132, 134, 135, 136, 137, 138, 139)) + labs_js([(306, 336), (338, 374)], (381, 382, 383)) + mcq(S, (), '''  { q: "[Feb/March 2021 · 32 · Q7] What is correct about cartels?", opts: ["They are a form of trade union restrictive practice.", "They are a type of industrial merger.", "They are often subject to government investigation.", "They establish a vertical link between firms."], a: 2, why: "Agreeing to fix price or output limits competition, so cartels are often investigated and are illegal in many countries." },
  { q: "[Feb/March 2025 · 32 · Q3] What is likely to prevent the development of an effective cartel in an industry?", opts: ["a high concentration ratio", "a limit-pricing policy", "high fixed costs", "low barriers to entry"], a: 3, why: "If new firms can enter easily, outsiders undercut the cartel and its high price cannot be held." },
  { q: "[May/June 2022 · 32 · Q10] What is a condition for operating a successful cartel?", opts: ["a large number of firms in the industry", "having a differentiated product", "low barriers of entry to the industry", "strictly enforced production quotas"], a: 3, why: "Members must keep to their output quotas, otherwise each gains by cheating." },
  { q: "[May/June 2020 (not sat) · 31 · Q11] When will a cartel find it most difficult to fix the market price of its product? (proportion of firms in the industry that are members, barriers to entry)", opts: ["high, high", "high, low", "low, high", "low, low"], a: 3, why: "A cartel with few of the industry's firms and easy entry cannot control the market price." },
  { q: "[May/June 2021 · 31 · Q6] A kinked demand curve is often used when economists analyse oligopolists. What does the kinked demand curve indicate?", opts: ["Oligopolists are unable to achieve profit maximisation.", "Satisficing is the best objective for firms that operate under conditions of oligopoly.", "There are always benefits available for oligopolists if they reduce price, but not if they increase it.", "There is a tendency towards price stability when firms operate under conditions of oligopoly."], a: 3, why: "Rivals match a price cut but ignore a rise, so firms have little incentive to change price." },
  { q: "[May/June 2022 · 31 · Q7] Firms in a market decide to collude over the price that they charge for their products. What is not likely to be a feature of the market?", opts: ["Firms have similar cost structures.", "Products of the firms are close substitutes.", "There are high barriers to entry into the market.", "There is a large number of competing firms."], a: 3, why: "Collusion is easier with a few firms; a large number makes agreement and policing difficult." },
''')
write("mk3", page(EY.format(3), "Oligopoly, Collusion and Contestable Markets",
  "Interdependence and the kinked demand curve, collusion and the prisoner's dilemma, contestable markets and X-inefficiency, and how firm performance compares across structures. Animated diagrams, interactive labs, drills and the past paper questions.",
  learn_class="legacy", explore_class="legacy", learn=learn, watch=watch, explore=explore, practise=practise, real=real, exam=exam, tips=tips), js,
  "Oligopoly, Collusion and Contestable Markets", "oligopoly-collusion-contestable")
