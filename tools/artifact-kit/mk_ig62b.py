"""Builds IGCSE Economics 6.2.4 to 6.2.6 (trade restrictions: types, reasons, consequences), written from scratch.
Run: python3 tools/artifact-kit/mk_ig62b.py"""
from igsy import *
F = Old("fisc")
M = Old("mon")
HEAD = M.j_((2, 25)) + F.j_((139, 160))
COMMON = open(D / "mk_ig44.py").read().split("COMMON = '''")[1].split("'''")[0]
CL = lambda t: f"IGCSE Economics · 0455 · {t}"

TM = '''
const trade = (o) => {
  const pw = o.pw ?? 40, t = o.t || 0, sub = o.sub || 0; let P = pw, mode = "free";
  if (o.emb && pw < 60) { P = 60; mode = "embargo"; }
  else if (o.q !== undefined && o.q !== null && (110 - pw) - (pw - 10) > o.q) { P = (120 - o.q) / 2; mode = "quota"; }
  else if (t > 0) { P = Math.min(pw + t, 60); mode = "tariff"; }
  const qs = P - 10 + (mode === "free" ? sub : 0), qd = 110 - P, imp = mode === "embargo" ? 0 : Math.max(0, qd - qs);
  return { P, qs, qd, imp, mode, rev: mode === "tariff" ? (P - pw) * imp : 0, cost: mode === "free" ? sub * qs : 0, rent: mode === "quota" ? (P - pw) * imp : 0 };
};
function tmChart(o) {
  const r = trade(o), pw = o.pw ?? 40; let s = axes("Price", "Quantity") + curve(-1, 110, "c1", "Demand", { t: "t1", dx: -90, dy: -12 }) + curve(1, 10, "c3", "Domestic supply", { t: "t3", dx: -125, dy: 16 });
  if (o.sub) s += curve(1, 10 - o.sub, "c2") + SV.text(QX(30), PY(30 - o.sub) + 30, "Supply + subsidy", "lbl bd t2");
  s += SV.line(QX(0), PY(pw), QX(100), PY(pw), "c4", { "stroke-width": 2.5 }) + SV.text(QX(100), PY(pw) + 18, "World price $" + Math.round(pw), "lbl bd t4", { "text-anchor": "end" });
  if (r.mode === "tariff" || r.mode === "quota" || r.mode === "embargo") {
    if (r.mode === "tariff" && r.imp > 0.5) s += SV.rect(QX(r.qs), PY(r.P), QX(r.qd) - QX(r.qs), PY(pw) - PY(r.P), "", { style: "fill:var(--good);fill-opacity:0.35" }) + SV.text(QX((r.qs + r.qd) / 2), PY((r.P + pw) / 2) + 4, "Revenue", "sm bd", { "text-anchor": "middle" });
    s += SV.line(QX(0), PY(r.P), QX(r.qd), PY(r.P), "gr", { style: "stroke-dasharray:5 4" }) + SV.text(QX(0) - 8, PY(r.P) + 4, "$" + money(r.P, 0), "sm bd", { "text-anchor": "end" });
  }
  s += SV.line(QX(r.qs), PY(Math.max(pw, r.P)), QX(r.qs), PY(0), "gr") + SV.line(QX(r.qd), PY(r.P), QX(r.qd), PY(0), "gr") + SV.circle(QX(r.qs), PY(r.P), 6, "dot2") + SV.circle(QX(r.qd), PY(r.P), 6, "dot2") + SV.text(QX(r.qs), PY(0) + 18, "Qs " + Math.round(r.qs), "sm bd", { "text-anchor": "middle" }) + SV.text(QX(r.qd), PY(0) + 18, "Qd " + Math.round(r.qd), "sm bd", { "text-anchor": "middle" });
  if (r.imp > 0.5) s += SV.text(QX((r.qs + r.qd) / 2), PY(r.P) - 28, "Imports " + Math.round(r.imp), "lbl bd t2", { "text-anchor": "middle", style: halo });
  return s;
}
'''

# =========================================================== 6.2.4 Types
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>The syllabus lists four <b>methods of protection</b> (trade restrictions): <span class="kw">tariffs</span>, <span class="kw">import quotas</span>, <span class="kw">subsidies</span> and <span class="kw">embargoes</span>. All aim to protect domestic producers from foreign competition, but they work differently, and each has different effects on prices, quantities, the government and trading partners. Tariffs are <b>tariff barriers</b>; the others are <b>non-tariff barriers</b>.</p></div>

  <h2>The four methods</h2>
  <div class="tw"><table class="t">
    <tr><th>Method</th><th>What it is</th><th>Main effects</th></tr>
    <tr><td><b>Tariff</b></td><td>A <b>tax on imports</b> (or exports) that raises their price</td><td>Imports fall, domestic output rises, consumers pay more, the government gains <b>revenue</b></td></tr>
    <tr><td><b>Import quota</b></td><td>A <b>limit on the quantity</b> of a good that can be imported</td><td>Imports fixed, supply falls, price rises; no tax revenue (the gain goes to importers)</td></tr>
    <tr><td><b>Subsidy</b></td><td>A <b>payment by the government to domestic producers</b> that lowers their costs</td><td>Domestic producers can charge less and supply more, so imports fall; costs taxpayers</td></tr>
    <tr><td><b>Embargo</b></td><td>A <b>total ban</b> on trade with a country or on a product</td><td>Imports (or exports) of that product stop; supply falls sharply and prices rise</td></tr>
  </table></div>
  <p><b>Other non-tariff barriers</b> include rules and regulations (quality, safety and labelling standards), complicated customs procedures (red tape), voluntary export restraints and exchange controls.</p>

  <h2>How each affects a market</h2>
  <ul>
    <li><b>Tariff:</b> world price $40 plus a $10 tariff makes the domestic price $50. Quantity demanded falls, domestic supply rises, imports fall, and the government collects $10 on each unit imported.</li>
    <li><b>Quota:</b> limiting imports to a fixed number reduces supply, so the domestic price rises. The effect on the price can be the same as a tariff, but there is no tax revenue.</li>
    <li><b>Subsidy:</b> shifts the domestic supply curve to the right (costs fall), so domestic output rises and the market price falls, but the government pays for it.</li>
    <li><b>Embargo:</b> imports are zero, so the country relies on its own production, which usually means a higher price and less choice.</li>
  </ul>

  <h2>Why a government may subsidise</h2>
  <p>Subsidies can protect infant industries, help exporters compete abroad, reduce food prices for consumers, secure food supplies (a strategic aim), encourage production with external benefits (such as renewable energy) or support jobs in a declining industry. Costs: taxpayers pay, they can distort markets, and other countries may object that they are unfair.</p>
'''
js = HEAD + COMMON + TM + '''
Lib.stepper($("#stT"), { w: 760, h: 400, label: "A tariff on imports", base: { pw: 40, t: 0 }, draw: tmChart, steps: [
  { cap: "With <b>free trade</b> the world price is $40. Domestic firms supply <b>30</b>, consumers buy <b>70</b> and <b>40</b> is imported.", s: { pw: 40, t: 0 } },
  { cap: "The government puts a <b>$10 tariff</b> on imports. Imported goods now cost <b>$50</b> in the shops.", s: { pw: 40, t: 10 } },
  { cap: "<b>Domestic output rises</b> to 40, <b>consumers buy less</b> (60) at the higher price, and <b>imports fall</b> to 20. The green box is <b>tariff revenue</b> ($10 × 20 = $200).", s: { pw: 40, t: 10 } },
  { cap: "<b>Evaluate:</b> domestic producers and the government gain. Consumers lose (higher price, less choice). Other countries may retaliate.", s: { pw: 40, t: 10 } },
] });
Lib.stepper($("#stQ"), { w: 760, h: 400, label: "An import quota", base: { pw: 40, q: 100 }, draw: tmChart, steps: [
  { cap: "With free trade, <b>40</b> units are imported at $40.", s: { pw: 40, q: 100 } },
  { cap: "The government sets an <b>import quota of 20 units</b>: no more than 20 can be imported.", s: { pw: 40, q: 20 } },
  { cap: "Supply falls, so the <b>price rises to $50</b>. Domestic firms supply 40 and consumers buy 60. The effect on price is like a tariff, but <b>there is no tax revenue</b>: the extra $10 goes to the importers who hold the licences.", s: { pw: 40, q: 20 } },
] });
Lib.stepper($("#stS"), { w: 760, h: 400, label: "A subsidy to domestic producers", base: { pw: 40, sub: 0 }, draw: tmChart, steps: [
  { cap: "The world price is $40. Domestic firms supply <b>30</b> and <b>40</b> is imported.", s: { pw: 40, sub: 0 } },
  { cap: "The government gives domestic producers a <b>$10 subsidy per unit</b>. Their costs fall: <b>supply shifts right</b>.", s: { pw: 40, sub: 10 } },
  { cap: "At the world price, domestic firms now supply <b>40</b> instead of 30, so <b>imports fall</b> to 30. Consumers still pay $40. The <b>cost to taxpayers is $10 × 40 = $400</b>.", s: { pw: 40, sub: 10 } },
] });
Lib.stepper($("#stE"), { w: 760, h: 400, label: "An embargo", base: { pw: 40, emb: 0 }, draw: (s) => tmChart({ pw: 40, emb: s.emb > 0.5 }), steps: [
  { cap: "With free trade the good is imported at <b>$40</b> and consumers buy <b>70</b>.", s: { emb: 0 } },
  { cap: "An <b>embargo bans imports</b> of the good. Only domestic firms can supply it.", s: { emb: 1 } },
  { cap: "The price rises to <b>$60</b>, consumers buy only <b>50</b> and all of it is domestic. Producers gain; consumers lose choice and pay more.", s: { emb: 1 } },
] });

/* Lab 1: tariff */
function labT() {
  if (!$("#ta")) return; const t = +$("#ta").value, r = trade({ pw: 40, t });
  $("#ta1").textContent = "$" + money(r.P, 0); $("#ta2").textContent = Math.round(r.imp); $("#ta3").textContent = "$" + money(r.rev, 0);
  $("#tav").textContent = t === 0 ? "No tariff: free trade at $40." : `A $${t} tariff raises the price to $${money(r.P, 0)}. Domestic output rises to ${Math.round(r.qs)}, consumers buy ${Math.round(r.qd)}, imports fall to ${Math.round(r.imp)} and the government collects $${money(r.rev, 0)}. ${r.P >= 60 ? "The tariff is so high that imports stop: it acts like an embargo." : ""}`;
  $("#labT").innerHTML = tmChart({ pw: 40, t });
}
Lib.slider($("#g1"), { id: "ta", label: "Tariff per unit", min: 0, max: 30, step: 5, value: 10, fmt: (v) => "$" + v, onInput: labT });
function labQ() {
  if (!$("#qa")) return; const q = +$("#qa").value, r = trade({ pw: 40, q });
  $("#qa1").textContent = "$" + money(r.P, 0); $("#qa2").textContent = Math.round(r.imp); $("#qa3").textContent = "$" + money(r.rent, 0);
  $("#qav").textContent = q >= 40 ? "A quota of 40 or more does not limit imports: free trade imports are already 40." : `Limiting imports to ${q} raises the price to $${money(r.P, 0)}. Domestic firms supply ${Math.round(r.qs)} and consumers buy ${Math.round(r.qd)}. The extra $${money(r.P - 40, 0)} per unit on ${q} units ($${money(r.rent, 0)}) goes to importers, not the government.`;
  $("#labQ").innerHTML = tmChart({ pw: 40, q });
}
Lib.slider($("#g2"), { id: "qa", label: "Import quota (units)", min: 0, max: 40, step: 5, value: 20, fmt: (v) => v, onInput: labQ });
function labS() {
  if (!$("#sa")) return; const sub = +$("#sa").value, r = trade({ pw: 40, sub });
  $("#sa1").textContent = Math.round(r.qs); $("#sa2").textContent = Math.round(r.imp); $("#sa3").textContent = "$" + money(r.cost, 0);
  $("#sav").textContent = sub === 0 ? "No subsidy." : `With a $${sub} subsidy domestic firms supply ${Math.round(r.qs)} at the $40 world price, so imports fall to ${Math.round(r.imp)}. Consumers still pay $40. The cost to taxpayers is $${money(r.cost, 0)}.`;
  $("#labS").innerHTML = tmChart({ pw: 40, sub });
}
Lib.slider($("#g3"), { id: "sa", label: "Subsidy per unit", min: 0, max: 30, step: 5, value: 10, fmt: (v) => "$" + v, onInput: labS });
const MT = [
  { n: "Tariff", w: "A tax on imports: raises their price.", a: "Revenue for the government; protects domestic producers.", d: "Higher prices for consumers; retaliation; cost to firms using imported inputs." },
  { n: "Import quota", w: "A limit on the quantity imported.", a: "Guarantees a ceiling on imports; protects domestic producers.", d: "No tax revenue; higher prices; may encourage smuggling." },
  { n: "Subsidy", w: "Payment to domestic producers lowering their costs.", a: "Lower prices and more output; no price rise for consumers.", d: "Cost to taxpayers; inefficiency; may breach trade rules." },
  { n: "Embargo", w: "A ban on trade with a country or product.", a: "Total protection; can be a political tool.", d: "Higher prices, less choice, retaliation; trading partner's exports lost." },
  { n: "Other non-tariff barriers", w: "Regulations, standards, red tape, exchange controls.", a: "Protect consumers and industries; hard to challenge.", d: "Costly for foreign firms; may be hidden protection." },
];
button_table("mtBtns", "mtOut", MT, 0, (p) => `<div class="tw"><table class="t"><tr><th>What it is</th><th>Advantages</th><th>Disadvantages</th></tr><tr><td>${p.w}</td><td>${p.a}</td><td>${p.d}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Which <b>method of protection</b> is each?", buckets: [{ label: "Tariff" }, { label: "Import quota" }, { label: "Subsidy" }, { label: "Embargo" }], items: [
  { text: "A 15% tax on imported cars", b: 0 }, { text: "A customs duty on imported steel", b: 0 },
  { text: "No more than 10,000 tonnes of sugar may be imported", b: 1 }, { text: "A limit on imported textiles", b: 1 },
  { text: "Government pays domestic farmers $50 per tonne", b: 2 }, { text: "Grants to domestic car makers", b: 2 },
  { text: "A complete ban on imports from one country", b: 3 }, { text: "Trade with a country is prohibited", b: 3 },
], done: "Tax, limit, payment, ban." });
Lib.classify($("#cl2"), { prompt: "Is each a <b>tariff barrier</b> or a <b>non-tariff barrier</b>?", buckets: [{ label: "Tariff barrier" }, { label: "Non-tariff barrier" }], items: [
  { text: "A tax on imports", b: 0 }, { text: "Customs duty", b: 0 },
  { text: "Quota", b: 1 }, { text: "Subsidy", b: 1 }, { text: "Embargo", b: 1 }, { text: "Complicated customs paperwork", b: 1 }, { text: "Safety and labelling rules aimed at imports", b: 1 },
], done: "Only a tariff is a tax on imports." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Tariff", "A tax on imports"],
  ["Import quota", "A limit on the quantity of imports"],
  ["Subsidy", "A payment by the government to producers to lower their costs"],
  ["Embargo", "A ban on trade with a country or product"],
  ["Protection", "Measures to protect domestic producers from foreign competition"],
  ["Customs duty", "Another word for a tariff"],
], done: "Good vocabulary scores marks." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how a tariff protects domestic producers</b>.", items: [
  "The government puts a tax on imports",
  "Imported goods become more expensive",
  "Consumers buy fewer imports and more domestic goods",
  "Domestic firms sell more and may expand",
  "Employment in the industry may rise",
], done: "A tariff chain." });
''' + calc_js([
    ("The world price is $40 and a 25% tariff is applied. What is the price of the imported good ($)?", 50, "40 × 1.25 = <b>$50</b>.", None, None),
    ("A tariff of $10 is paid on 20 imported units. How much revenue does the government collect ($)?", 200, "10 × 20 = <b>$200</b>.", None, None),
    ("A government pays a subsidy of $8 per unit on 500 units. What does it cost ($)?", 4000, "8 × 500 = <b>$4,000</b>.", None, None),
    ("A quota cuts imports from 40 to 20 units. By what percentage did imports fall?", 50, "20 ÷ 40 × 100 = <b>50%</b>.", None, None),
]) + mcq_js("qz1", [
    ("What is a tariff?", ["A limit on imports", "A tax on imports", "A payment to producers", "A ban on trade"], 1, "A tariff is a tax on imports."),
    ("An import quota is:", ["A tax on imports", "A limit on the quantity of imports", "A subsidy", "A free trade area"], 1, "A quantity limit."),
    ("A subsidy to domestic producers is most likely to:", ["Raise their costs", "Lower their costs so they supply more", "Reduce output", "Raise import prices"], 1, "Supply shifts right."),
    ("Which is a non-tariff method of protection?", ["Customs duty", "Import tariff", "Import quota", "VAT"], 2, "Quotas are non-tariff."),
    ("An embargo is:", ["A tax on exports", "A ban on trade with a country or product", "A limit on imports", "A subsidy"], 1, "Total ban."),
]) + "\n" + cards_js([("Protection", "Measures used to protect domestic producers from foreign competition."), ("Tariff", "A tax on imports (or exports) that raises their price."), ("Import quota", "A limit on the quantity of a good that can be imported."), ("Subsidy", "A payment by the government to producers to lower their costs."), ("Embargo", "A ban on trade with a particular country or in a particular product."), ("Tariff barrier", "A barrier to trade in the form of a tax."), ("Non-tariff barrier", "A barrier to trade that is not a tax, such as a quota or regulations."), ("Customs duty", "A tax on goods crossing a border."), ("Red tape", "Bureaucratic rules and paperwork that slow trade.")]) + "labT(); labQ(); labS(); \n"
explore = '''
  <h2>Lab 1 · Tariff simulator</h2>
  <p>The world price is $40 and the domestic equilibrium without trade is $60. Set a tariff and see the effect.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div></div>
    <div><div class="readout"><div><small>Price paid</small><strong id="ta1"></strong></div><div><small>Imports</small><strong id="ta2"></strong></div><div><small>Tariff revenue</small><strong id="ta3"></strong></div></div><div class="verdict" id="tav"></div></div></div>
    <svg id="labT" viewBox="0 0 760 400" role="img" aria-label="Market with a tariff"></svg>
  </div>

  <h2>Lab 2 · Quota simulator</h2>
  <p>Limit imports to a quota and see the price and who gains the difference.</p>
  <div class="card"><div class="grid2"><div><div id="g2"></div></div>
    <div><div class="readout"><div><small>Price paid</small><strong id="qa1"></strong></div><div><small>Imports</small><strong id="qa2"></strong></div><div><small>Gain to importers</small><strong id="qa3"></strong></div></div><div class="verdict" id="qav"></div></div></div>
    <svg id="labQ" viewBox="0 0 760 400" role="img" aria-label="Market with a quota"></svg>
  </div>

  <h2>Lab 3 · Subsidy simulator</h2>
  <p>Give domestic producers a subsidy and see how imports and the cost to taxpayers change.</p>
  <div class="card"><div class="grid2"><div><div id="g3"></div></div>
    <div><div class="readout"><div><small>Domestic output</small><strong id="sa1"></strong></div><div><small>Imports</small><strong id="sa2"></strong></div><div><small>Cost to taxpayers</small><strong id="sa3"></strong></div></div><div class="verdict" id="sav"></div></div></div>
    <svg id="labS" viewBox="0 0 760 400" role="img" aria-label="Market with a subsidy"></svg>
  </div>

  <h2>Lab 4 · The methods compared</h2>
  <p>Pick a method to see what it is and its advantages and disadvantages.</p>
  <div class="card"><div class="row" id="mtBtns"></div><div id="mtOut"></div></div>
'''
ex = exam(
    Q(1, "Define", 2, "Define tariffs. (Oct/Nov 2020, P21)", "A tax on imports (or exports) which raises their price.", "[K|A tariff is a tax on imports (or exports)] [K|which increases the price of the imported (or exported) goods.]"),
    Q(2, "Identify", 2, "Identify two methods of protection. (Feb/Mar 2020, P22; Oct/Nov 2022, P22)", "Any two: tariffs, quotas, subsidies, embargoes.", "[K|Tariffs (a tax on imports).] [K|Quotas (or subsidies or embargoes).]"),
    Q(3, "Explain", 4, "Explain two non-tariff methods of protection. (Oct/Nov 2020, P21)", "Quota, subsidy, embargo, regulations; each with a description.",
      "[K|An import quota is a limit on the quantity of imports that can enter a country,] [N|so supply from abroad is limited and domestic firms sell more.] [K|A subsidy is a grant to domestic firms,] [N|which lowers their costs so they can charge lower prices and compete better with imports.]"),
    Q(4, "Explain", 4, "Explain two reasons why a government may subsidise food production. (Oct/Nov 2023, P22)", "Lower food prices, food security, support farmers' incomes, correct market failure, reduce imports.",
      "[K|To reduce the price of food.] [N|A subsidy lowers farmers' costs so food can be sold more cheaply, helping low-income households afford basic necessities.] [K|To raise food self-sufficiency.] [N|More domestic production reduces dependence on imports, making supplies more secure and improving the current account.]"),
    Q(5, "Analyse", 5, "Analyse, using a demand and supply diagram, how a subsidy given to producers could affect the market for electric cars. (May/June 2020, P22)", "Draw S shifting right to S₁, label P to P₁, Q to Q₁; explain lower price, higher quantity.",
      "[K|A subsidy lowers producers' costs of making electric cars,] [N|so the supply curve shifts to the right from S to S₁.] [N|At the original price firms now supply more, so the equilibrium price falls from P to P₁ and the quantity bought rises from Q to Q₁.] [A|Cheaper electric cars may raise sales and help reduce pollution.] [E|The government pays for the subsidy, which has an opportunity cost.]", key=True),
    Q(6, "Analyse", 6, "Analyse how an import tariff affects a market for a good.", "Draw: price rises, domestic supply up, imports down, revenue. Evaluate: consumers lose.",
      "[K|A tariff is a tax on imports, so the price of imported goods rises.] [N|Consumers buy less at the higher price, and domestic producers face less competition, so they supply more.] [N|Imports fall, and the government earns tariff revenue on the imports that remain.] [A|For example, a $10 tariff on a $40 import raises the price to $50.] [E|However, consumers pay more and have less choice, and other countries may retaliate.]", key=True),
)
tp = tips([
    ("Four methods:", "tariffs, quotas, subsidies, embargoes."),
    ("Tariff = tax. Quota = limit. Subsidy = payment. Embargo = ban.", "Define each."),
    ("Draw the diagram.", "Tariff: price up. Subsidy: supply right. Label P, P₁, Q, Q₁."),
    ("Quota gives no revenue.", "Tariffs do."),
    ("Evaluate with consumers and retaliation.", "Higher prices, less choice, trade war risk."),
], cmds("Define", "Identify", "Explain", "Analyse"))
body = page(CL("6.2.4 Types of trade restrictions / methods of protection"), "Types of Trade Restrictions", "Tariffs, import quotas, subsidies and embargoes: what they are and how each affects a market. Syllabus 6.2.4.",
    learn=learn, watch=watch(("A tariff on imports", "stT"), ("An import quota", "stQ"), ("A subsidy to domestic producers", "stS"), ("An embargo", "stE")), explore=explore,
    practise=practise(("Which method?", "cl1", "card"), ("Tariff or non-tariff barrier?", "cl2", "card"), ("Match the term", "m1", "card"), ("Order the tariff chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("US steel tariffs", "In 2018 the United States put tariffs on imported steel and aluminium, raising prices for US firms that use them and prompting retaliation from other countries.", "A tariff and its effects."),
        rw("Quotas on imports", "Some countries limit imports of sugar or textiles by quota. Quota holders can earn high profits because the quantity is restricted.", "A quota with no tax revenue."),
        rw("Subsidies to farmers", "The EU's Common Agricultural Policy and the US farm programmes pay subsidies to farmers, helping them compete with imports but costing taxpayers.", "Subsidies as protection."),
        rw("Russia embargo", "After 2022 many countries banned imports of Russian oil and gas and exports of certain technology, an embargo with major effects on prices.", "An embargo for political reasons.")),
    exam=ex, tips=tp)
write("tr1", body, js, "Types of Trade Restrictions", "ig-trade-restrictions-types")

# =========================================================== 6.2.5 Reasons
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>Governments restrict free trade for eight main reasons: to <b>protect infant (sunrise) industries</b>, to <b>protect declining (sunset) industries</b>, to <b>protect strategic industries</b>, to <b>avoid dumping</b>, to <b>reduce a deficit on the current account</b>, to <b>raise tax revenue</b>, to <b>restrict imports of demerit goods</b> and to <b>promote environmental sustainability</b>. For each reason, explain what the government is trying to achieve, how the restriction helps, and the possible problems.</p></div>

  <h2>The eight reasons</h2>
  <div class="tw"><table class="t">
    <tr><th>Reason</th><th>Why a government may restrict trade</th><th>Possible problem</th></tr>
    <tr><td><b>Protect infant (sunrise) industries</b></td><td>New industries are small and have high costs; they need time to grow, gain skills and economies of scale before facing foreign rivals</td><td>May never become efficient; consumers pay more meanwhile</td></tr>
    <tr><td><b>Protect declining (sunset) industries</b></td><td>Keeps jobs and gives time for workers to retrain and the area to adjust, reducing structural unemployment</td><td>Delays change; keeps inefficient firms; consumers pay more</td></tr>
    <tr><td><b>Protect strategic industries</b></td><td>Food, energy, defence and steel are needed for national security and self-sufficiency</td><td>Higher costs; may be hard to justify</td></tr>
    <tr><td><b>Avoid dumping</b></td><td>Foreign firms may sell below cost to drive out local firms; duties keep competition fair</td><td>Hard to prove dumping; retaliation</td></tr>
    <tr><td><b>Reduce a current account deficit</b></td><td>Tariffs and quotas cut imports and may raise demand for domestic goods</td><td>Works only if import demand is elastic; retaliation may reduce exports</td></tr>
    <tr><td><b>Raise tax revenue</b></td><td>Tariffs are easy to collect, especially in low-income countries with few other taxes</td><td>Revenue falls if imports fall; higher prices</td></tr>
    <tr><td><b>Restrict demerit goods</b></td><td>Limit imports of tobacco, alcohol, drugs and weapons to protect health and safety</td><td>Smuggling; black markets</td></tr>
    <tr><td><b>Promote environmental sustainability</b></td><td>Restrict imports of goods made unsustainably (illegal timber, ivory, high-pollution products) or that damage the environment</td><td>May be protection in disguise; hard to monitor</td></tr>
  </table></div>

  <h2>Infant industry argument in detail</h2>
  <p>A new industry has a small output and so high <b>average costs</b>. Foreign firms with a large output have lower average costs and can sell more cheaply. If the infant industry is protected, it can grow and its average costs fall through <b>economies of scale</b> until it can compete without help. The protection should be <b>temporary</b>.</p>

  <h2>Dumping</h2>
  <p><span class="kw">Dumping</span> is selling goods abroad at a price below their cost of production. A foreign firm may do this to win market share and drive out rivals, then raise prices. Anti-dumping tariffs aim to keep competition fair.</p>

  <h2>Evaluating the reasons</h2>
  <ul>
    <li>Do the benefits to protected firms and workers outweigh the cost to consumers?</li>
    <li>Is the protection <b>temporary</b> or permanent? Permanent protection may make firms inefficient.</li>
    <li>Will other countries <b>retaliate</b>?</li>
    <li>Is the elasticity of demand for imports high enough for a tariff to cut imports?</li>
    <li>Are there <b>better policies</b>, such as subsidies, training or retraining?</li>
  </ul>
'''
js = HEAD + COMMON + '''
function acChart(s) {
  const X = (q) => 80 + q * 3, Y = (v) => 340 - (v - 20) * 1.3, ac = (q) => 30 + 4000 / (q + 10);
  let o = SV.line(80, 340, 80, 40) + SV.line(80, 340, 700, 340) + SV.text(86, 48, "Average cost ($)", "sm") + SV.text(700, 362, "Output of the domestic industry", "sm", { "text-anchor": "end" });
  const pts = []; for (let q = 15; q <= 200; q += 5) pts.push([X(q), Y(ac(q))]); o += SV.path(ptsPath(pts), "c1", { "stroke-width": 3 }) + SV.text(X(30) + 10, Y(ac(30)) - 12, "Average cost", "lbl bd t1");
  o += SV.line(80, Y(60), 700, Y(60), "dash", { style: "stroke:var(--bad);stroke-width:2.5" }) + SV.text(696, Y(60) - 8, "World price $60", "lbl bd t2", { "text-anchor": "end" });
  if (s.p > 0.02) o += `<g opacity="${s.p}">` + SV.line(80, Y(105), 700, Y(105), "dash", { style: "stroke:var(--good);stroke-width:2.5" }) + SV.text(696, Y(105) - 8, "Protected price $105", "lbl bd t3", { "text-anchor": "end" }) + "</g>";
  const q = s.q; o += SV.circle(X(q), Y(ac(q)), 8, ac(q) > 60 ? "dot2" : "dot3") + SV.line(X(q), Y(ac(q)), X(q), 340, "gr") + SV.text(X(q), 358, "Output " + Math.round(q), "sm bd", { "text-anchor": "middle" });
  o += SV.text(X(q) + 12, Y(ac(q)) - 12, "AC $" + Math.round(ac(q)), "lbl bd " + (ac(q) > 60 ? "t2" : "t3"), { style: halo });
  return o;
}
Lib.stepper($("#stI"), { w: 760, h: 400, label: "The infant industry argument", base: { q: 20, p: 0 }, draw: acChart, steps: [
  { cap: "A <b>new industry</b> produces only a small amount (20 units), so its <b>average cost is high ($143)</b>, far above the <b>world price of $60</b>. Foreign firms are larger and cheaper: it cannot compete and would be driven out.", s: { q: 20, p: 0 } },
  { cap: "The government <b>protects</b> it with a tariff or subsidy. The protected price is <b>$105</b>, so the industry can sell and survive, and it grows.", s: { q: 60, p: 1 } },
  { cap: "As output grows, <b>average cost falls</b> (economies of scale and learning).", s: { q: 110, p: 1 } },
  { cap: "At about 150 units, average cost is <b>below the world price</b>. The industry can now compete, and the protection can be <b>removed</b>. <b>Evaluate:</b> protection must be temporary, and some infant industries never become competitive.", s: { q: 160, p: 0 } },
] });
const DM = ["A foreign firm sells in a country below its cost of production", "Domestic firms cannot match the low price", "Domestic firms lose sales and close", "The foreign firm gains market power", "It then raises prices: consumers lose in the long run", "Anti-dumping tariffs aim to stop this"];
Lib.stepper($("#stD"), { w: 760, h: 400, label: "Dumping", base: { n: 0 }, draw: mkChain(DM, "--bad"), steps: chainSteps(["A foreign firm sells in a country <b>below its cost of production</b>.", "Domestic firms <b>cannot match</b> the low price.", "They <b>lose sales and close</b>.", "The foreign firm gains <b>market power</b>.", "It then <b>raises prices</b>: consumers lose in the long run.", "<b>Anti-dumping tariffs</b> aim to stop this and keep competition fair. Evaluate: dumping is hard to prove and may lead to retaliation."]) });
const CA = ["A country has a current account deficit: imports exceed exports", "The government raises tariffs or quotas on imports", "Imports become dearer and fall; some demand switches to domestic goods", "The deficit narrows", "But other countries may retaliate, so exports fall", "And firms using imports face higher costs: the net effect is uncertain"];
Lib.stepper($("#stA"), { w: 760, h: 400, label: "Using tariffs to reduce a current account deficit", base: { n: 0 }, draw: mkChain(CA, "--accent"), steps: chainSteps(["The country has a <b>current account deficit</b>: imports exceed exports.", "The government raises <b>tariffs or quotas</b> on imports.", "Imports become <b>dearer and fall</b>; some demand switches to domestic goods.", "The <b>deficit narrows</b>.", "But other countries may <b>retaliate</b>, so exports fall.", "And firms using imports face <b>higher costs</b>. <b>Evaluate:</b> the net effect is uncertain and depends on elasticity."]) });

/* Lab 1: tariff and the current account */
function labC() {
  if (!$("#ca") || !$("#cb") || !$("#cc")) return;
  const t = +$("#ca").value / 100, e = +$("#cb").value, r = +$("#cc").value / 100, imp = 100 * Math.pow(1 + t, -e), exp = 90 * Math.pow(1 + r * t, -1.2), def = imp - exp, rev = t * imp;
  $("#ca1").textContent = "$" + money(imp, 0) + "bn"; $("#ca2").textContent = "$" + money(exp, 0) + "bn"; $("#ca3").textContent = (def >= 0 ? "Deficit $" : "Surplus $") + money(Math.abs(def), 0) + "bn";
  $("#cav").textContent = `Imports fall from $100bn to $${money(imp, 0)}bn (import demand elasticity ${e}). ${r > 0 ? `Foreign countries retaliate with tariffs of ${Math.round(r * t * 100)}%, so exports fall from $90bn to $${money(exp, 0)}bn.` : "No retaliation: exports stay at $90bn."} The deficit goes from $10bn to $${money(def, 0)}bn. Tariff revenue is $${money(rev, 1)}bn. ${def > 10 ? "The deficit has got worse: retaliation and low elasticity can make the policy backfire." : def < 10 ? "The deficit has narrowed." : ""}`;
  const base = 290, k = 2.2; let o = SV.line(60, base, 700, base);
  [["Imports", imp, "--bad"], ["Exports", exp, "--good"], ["Deficit", Math.max(0, def), "--warn"]].forEach(([n, v, c], i) => { const x = 130 + i * 190, h = v * k; o += SV.rect(x, base - h, 120, h, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.text(x + 60, base - h - 8, "$" + money(v, 0) + "bn", "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 60, base + 22, n, "sm", { "text-anchor": "middle" }); });
  $("#labC").innerHTML = o + SV.text(60, 24, "Baseline: imports $100bn, exports $90bn, deficit $10bn", "sm");
}
Lib.slider($("#g1"), { id: "ca", label: "Tariff on imports", min: 0, max: 50, step: 5, value: 20, fmt: (v) => v + "%", onInput: labC });
Lib.slider($("#g2"), { id: "cb", label: "Price elasticity of demand for imports", min: 0.2, max: 2, step: 0.2, value: 1, fmt: (v) => v.toFixed(1) + (v < 1 ? " inelastic" : v > 1 ? " elastic" : ""), onInput: labC });
Lib.slider($("#g3"), { id: "cc", label: "Foreign retaliation (share of our tariff matched)", min: 0, max: 100, step: 25, value: 0, fmt: (v) => v + "%", onInput: labC });
const RS = [
  { n: "Infant industry", w: "A new, small industry has high costs and cannot yet compete.", h: "Protection gives time to grow and gain economies of scale.", c: "May never become efficient; consumers pay more." },
  { n: "Declining (sunset) industry", w: "An old industry is losing out to cheaper imports.", h: "Protects jobs and gives time to retrain workers and adjust.", c: "Delays change; consumers pay more; resources tied up." },
  { n: "Strategic industry", w: "Food, energy and defence are vital for security.", h: "Keeps domestic supply and avoids dependence.", c: "Higher costs; hard to define 'strategic'." },
  { n: "Avoiding dumping", w: "Foreign firms sell below cost to win market share.", h: "Anti-dumping duties keep competition fair.", c: "Hard to prove; retaliation." },
  { n: "Current account deficit", w: "Imports exceed exports.", h: "Cutting imports narrows the deficit.", c: "Elasticity and retaliation can make it fail." },
  { n: "Raising tax revenue", w: "The government needs revenue.", h: "Tariffs are easy to collect.", c: "Revenue falls if imports fall; higher prices." },
  { n: "Demerit goods", w: "Tobacco, alcohol, drugs and weapons are harmful.", h: "Restricting imports reduces consumption and protects health.", c: "Smuggling; black markets." },
  { n: "Environmental sustainability", w: "Some imports are produced unsustainably.", h: "Restrictions protect forests, wildlife and the climate.", c: "May be disguised protection; hard to monitor." },
];
button_table("rsBtns", "rsOut", RS, 0, (p) => `<div class="tw"><table class="t"><tr><th>Situation</th><th>How restriction helps</th><th>Problem</th></tr><tr><td>${p.w}</td><td>${p.h}</td><td>${p.c}</td></tr></table></div>`);
const SC = [
  { n: "A new electric car firm cannot match large foreign makers", a: "Infant industry", w: "Small, new, high costs: needs time to grow." },
  { n: "A coal industry is closing as demand falls", a: "Declining (sunset) industry", w: "Protection slows job losses." },
  { n: "A country wants to avoid relying on imported food", a: "Strategic industry", w: "Self-sufficiency and security." },
  { n: "A foreign steel firm sells below its production cost", a: "Avoiding dumping", w: "Selling below cost." },
  { n: "A very low-income country with few taxes imposes import duties", a: "Raising tax revenue", w: "Tariffs are easy to collect." },
  { n: "A government bans imports of ivory and illegally logged timber", a: "Environmental sustainability", w: "Protecting forests and wildlife." },
];
button_table("scBtns", "scOut", SC, 0, (p) => `<div class="tw"><table class="t"><tr><th>Reason for restriction</th><th>Why</th></tr><tr><td><b>${p.a}</b></td><td>${p.w}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Which <b>reason for trade restrictions</b> fits each situation?", buckets: [{ label: "Infant industry" }, { label: "Declining industry" }, { label: "Strategic industry" }, { label: "Dumping" }], items: [
  { text: "A new computer maker with high costs", b: 0 }, { text: "A start-up car battery firm needing time to grow", b: 0 },
  { text: "A shipyard losing jobs to cheaper foreign yards", b: 1 }, { text: "An old textile industry in decline", b: 1 },
  { text: "A country's food and energy supply", b: 2 }, { text: "Defence equipment manufacturing", b: 2 },
  { text: "Foreign firms selling below cost to win market share", b: 3 }, { text: "Cheap steel flooding the market at a price below cost", b: 3 },
], done: "Know all eight reasons." });
Lib.classify($("#cl2"), { prompt: "Is each a <b>benefit</b> or a <b>problem</b> of using tariffs to reduce a current account deficit?", buckets: [{ label: "Benefit" }, { label: "Problem" }], items: [
  { text: "Imports fall", b: 0 }, { text: "Demand for domestic goods rises", b: 0 }, { text: "The deficit narrows", b: 0 },
  { text: "Other countries may retaliate and cut our exports", b: 1 }, { text: "Firms using imported inputs face higher costs", b: 1 }, { text: "Consumers pay higher prices", b: 1 }, { text: "Fails if demand for imports is inelastic", b: 1 },
], done: "The net effect is uncertain." });
Lib.match($("#m1"), { prompt: "Match the reason to what the government wants.", pairs: [
  ["Infant industry protection", "Give a new industry time to grow and gain economies of scale"],
  ["Sunset industry protection", "Slow job losses and give time to adjust"],
  ["Strategic industry protection", "Secure food, energy and defence supplies"],
  ["Anti-dumping duties", "Stop foreign firms selling below cost"],
  ["Tariffs on imports", "Raise tax revenue or cut imports"],
  ["Import bans on demerit goods", "Protect health and safety"],
], done: "Link the reason to the aim." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>why dumping may harm domestic firms</b>.", items: [
  "A foreign firm sells below cost in the domestic market",
  "Domestic firms lose sales",
  "Some domestic firms close and workers lose jobs",
  "The foreign firm has less competition",
  "It raises prices later",
], done: "A dumping chain." });
''' + calc_js([
    ("A foreign firm's cost of producing a good is $20 but it sells it abroad for $14. By what percentage is the price below cost?", 30, "6 ÷ 20 × 100 = <b>30%</b>.", None, None),
    ("A country imports $200bn and exports $180bn. A tariff cuts imports by 10%, with no other change. What is the new deficit ($bn)?", 0, "Imports = $180bn, so the deficit = 180 − 180 = <b>$0bn</b>.", None, None),
    ("Imports fall from 100 units to 70 units after a tariff. At $5 a unit, tariff revenue is $1 per unit. How much revenue ($)?", 70, "70 × 1 = <b>$70</b>.", None, None),
]) + mcq_js("qz1", [
    ("Why might a government protect an infant industry?", ["It is declining", "It needs time to grow and gain economies of scale", "It is very efficient", "It sells at a high price"], 1, "New firms have high costs."),
    ("What is dumping?", ["Selling goods abroad below cost", "Buying too many imports", "Banning imports", "Taxing exports"], 0, "A price below cost."),
    ("Which is a reason for restricting imports of demerit goods?", ["To protect health", "To raise prices", "To reduce exports", "To increase imports"], 0, "Reduce harmful consumption."),
    ("A tariff may fail to reduce a current account deficit if:", ["Demand for imports is inelastic", "Demand for imports is elastic", "No country retaliates", "Imports are cheap"], 0, "Imports will not fall much."),
    ("Why might a government protect a strategic industry?", ["For national security and self-sufficiency", "To raise prices", "To cut exports", "To reduce competition abroad"], 0, "Food, energy and defence."),
]) + "\n" + cards_js([("Infant (sunrise) industry", "A new industry that is not yet able to compete with established foreign firms."), ("Declining (sunset) industry", "An industry in long-term decline that may be protected to slow job losses."), ("Strategic industry", "An industry essential for national security, such as defence, energy and food."), ("Dumping", "Selling goods abroad at a price below the cost of production."), ("Current account deficit", "When the value of imports (and outflows) exceeds exports (and inflows)."), ("Demerit good", "A good that is harmful to consumers, such as tobacco."), ("Environmental sustainability", "Meeting today's needs without damaging future generations' ability to meet theirs."), ("Retaliation", "A response by another country, such as raising its own tariffs."), ("Self-sufficiency", "Producing enough of a good at home not to depend on imports.")]) + "labC(); \n"
explore = '''
  <h2>Lab 1 · Can a tariff cut the current account deficit?</h2>
  <p>Baseline: imports $100bn, exports $90bn. Set a tariff, how sensitive import demand is, and how much other countries retaliate.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div></div>
    <div><div class="readout"><div><small>Imports</small><strong id="ca1"></strong></div><div><small>Exports</small><strong id="ca2"></strong></div><div><small>Current account</small><strong id="ca3"></strong></div></div><div class="verdict" id="cav"></div></div></div>
    <svg id="labC" viewBox="0 0 760 330" role="img" aria-label="Imports, exports and the deficit after a tariff"></svg>
  </div>

  <h2>Lab 2 · The eight reasons</h2>
  <p>Pick a reason to see the situation, how restriction helps and the problem.</p>
  <div class="card"><div class="row" id="rsBtns"></div><div id="rsOut"></div></div>

  <h2>Lab 3 · Which reason is it?</h2>
  <p>Pick a situation to see which reason for trade restrictions fits.</p>
  <div class="card"><div class="row" id="scBtns"></div><div id="scOut"></div></div>
'''
ex = exam(
    Q(1, "Explain", 4, "Explain why an infant industry may need protection. (Feb/Mar 2022, P22)", "New, small, high costs, no economies of scale; foreign firms cheaper; protection gives time; jobs.",
      "[K|An infant industry is new and small, so its average costs are high.] [N|Established foreign firms produce on a large scale and have lower costs, so they can sell more cheaply and could drive the new firms out of business.] [N|Protection gives the industry time to grow, gain skills and economies of scale, so its costs fall and it can compete.] [A|It could then create jobs and contribute to growth.]"),
    Q(2, "Explain", 2, "Explain one way that import tariffs could improve the US economy. (Feb/Mar 2023, P22)", "Current account, output, or tax revenue, with an explanation.", "[K|They could improve the current account,] [N|by raising the price of imports and so reducing them.]"),
    Q(3, "Analyse", 6, "Analyse the reasons for imposing tariffs on imports. (May/June 2023, P22; Oct/Nov 2022, P23)", "Several reasons, each with a link: reduce imports and the deficit, protect infant, declining and strategic industries, revenue, dumping.",
      "[K|A country may impose tariffs to raise the price of imports.] [N|Demand for imports could fall, reducing import spending and improving the current account, while demand for domestic firms rises, which could reduce unemployment and raise output.] [N|Tariffs can protect infant industries, giving them time to gain economies of scale so they are not driven out by larger foreign firms.] [N|They can protect declining industries, preventing unemployment from rising too quickly, and strategic industries, to ensure self-sufficiency.] [N|They also raise revenue for the government, and anti-dumping tariffs stop foreign firms from selling below cost.]", key=True),
    Q(4, "Discuss", 8, "Discuss whether or not imposing tariffs on imports will increase a country's output. (Oct/Nov 2023, P23)", "For: higher demand for domestic goods, protected firms grow, jobs. Against: retaliation, higher costs for firms using imports, inefficiency, consumer demand falls.",
      "[K|A tariff is a tax on imports, and output is the total production of goods and services.] [N|Tariffs raise the price of imports, so consumers may switch to domestic goods, and domestic firms can sell more, expand and employ more workers, so output could rise.] [N|Protected infant industries may grow.] [E|This is more likely if domestic firms can supply the goods and import demand is elastic.] [N|However, firms that use imported raw materials face higher costs and may cut output, and other countries may retaliate, reducing exports.] [N|Protected firms may become inefficient, and higher prices reduce consumers' spending power.] [E|Overall, tariffs could raise output in the protected industries but are unlikely to raise total output if there is retaliation and higher costs.]", key=True),
    Q(5, "Discuss", 6, "Discuss whether or not an increase in Nigeria's import tariff on rice would increase the output of Nigerian rice. (May/June 2021, P21)", "For: dearer imports so demand for domestic rice rises; protects farmers. Against: farmers' capacity and costs, smuggling, higher prices, other constraints.",
      "[K|A tariff on imported rice raises its price.] [N|Consumers could switch to Nigerian rice, so demand for it rises, and farmers may produce and invest more, increasing output.] [E|This is more likely if farmers can expand quickly.] [N|However, output may not rise much if farmers lack land, machinery or finance, or if prices of inputs rise, and smuggling could limit the effect.] [E|Overall, a tariff could raise rice output in the long run if farmers can respond, but it depends on supply constraints.]", key=True),
    Q(6, "Explain", 4, "Explain what is meant by dumping and why a government may take action against it.", "Define dumping (below cost), then the harm and the response (anti-dumping duty).",
      "[K|Dumping is when a foreign firm sells goods in another country at a price below their cost of production.] [N|Domestic firms cannot match the price, so they lose sales and some may close, causing unemployment.] [N|Once rivals have gone, the foreign firm could raise prices.] [A|A government may impose an anti-dumping tariff to raise the price of the goods and keep competition fair.]"),
)
tp = tips([
    ("Eight reasons:", "infant, declining, strategic, dumping, current account, revenue, demerit goods, environment."),
    ("Explain the aim and how the restriction helps.", "For infant: lower costs through scale."),
    ("Dumping = selling below cost.", "Not just selling cheaply."),
    ("Say it should be temporary for infant industries.", "Otherwise firms may stay inefficient."),
    ("Evaluate: retaliation, elasticity, higher costs.", "A tariff may not cut the deficit."),
], cmds("Explain", "Analyse", "Discuss"))
body = page(CL("6.2.5 Reasons for trade restrictions"), "Reasons for Trade Restrictions", "Why governments restrict trade: infant, declining and strategic industries, dumping, the current account, tax revenue, demerit goods and the environment. Syllabus 6.2.5.",
    learn=learn, watch=watch(("The infant industry argument", "stI"), ("Dumping", "stD"), ("Using tariffs to reduce a current account deficit", "stA")), explore=explore,
    practise=practise(("Which reason?", "cl1", "card"), ("Benefit or problem?", "cl2", "card"), ("Match the reason to the aim", "m1", "card"), ("Order the dumping chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("Protecting Korean and Japanese infant industries", "In the 1960s to 1980s South Korea and Japan protected young industries such as cars and electronics, then opened markets as firms became competitive.", "Infant industry protection that worked."),
        rw("EU anti-dumping duties on steel and solar panels", "The EU has imposed duties on cheap steel and solar panels from China, arguing they were sold below cost.", "Avoiding dumping."),
        rw("Food security and rice", "Countries such as Japan and the Philippines protect their rice farmers because rice is a staple food.", "Strategic industry protection."),
        rw("Import bans on ivory and illegally logged timber", "Many countries ban imports of ivory and illegally logged timber to protect wildlife and forests.", "Environmental reasons."),
        rw("Tariffs as revenue", "Customs duties are a major source of government revenue in many low-income countries with few other taxes.", "Raising tax revenue.")),
    exam=ex, tips=tp)
write("tr2", body, js, "Reasons for Trade Restrictions", "ig-trade-restrictions-reasons")

# =========================================================== 6.2.6 Consequences
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>Trade restrictions affect the <b>home country</b> (the country that imposes them) and its <b>trading partners</b>. They help protected producers and workers and may raise government revenue, but they raise prices, reduce choice and efficiency, and invite <b>retaliation</b>, which can start a <b>trade war</b> where everyone loses. Good answers weigh the advantages and disadvantages of restricting free trade and say who gains and who loses.</p></div>

  <h2>Impact on the home country</h2>
  <div class="tw"><table class="t">
    <tr><th>Group</th><th>Likely effect of a tariff or quota</th></tr>
    <tr><td><b>Consumers</b></td><td>Pay <b>higher prices</b> for imports and (as competition falls) domestic goods; less choice</td></tr>
    <tr><td><b>Protected domestic producers</b></td><td>Sell more, may expand; may become <b>complacent and inefficient</b> without competition</td></tr>
    <tr><td><b>Firms that use imported inputs</b></td><td>Costs rise, so they may cut output or jobs or lose competitiveness</td></tr>
    <tr><td><b>Workers</b></td><td>Jobs saved or created in protected industries; jobs lost in industries that import or export</td></tr>
    <tr><td><b>The government</b></td><td>Tariff revenue (not from quotas); but may need to pay subsidies; may raise inflation</td></tr>
    <tr><td><b>The economy</b></td><td>Imports fall, the current account may improve; but lower efficiency, higher prices (inflation) and lower consumer spending power</td></tr>
  </table></div>

  <h2>Impact on trading partners</h2>
  <ul>
    <li><b>Exporters lose sales</b> in the country imposing the restrictions, so output and jobs fall in those industries.</li>
    <li>Their <b>export earnings and growth</b> may fall; a current account deficit may widen.</li>
    <li>They may <b>retaliate</b> with their own tariffs or quotas, hurting the first country's exporters.</li>
    <li>Prices of the goods they buy from the first country may rise too.</li>
  </ul>

  <h2>Trade wars</h2>
  <p>If one country raises tariffs and others retaliate, trade between them falls, prices rise for everyone, supply chains are disrupted, and growth slows. A <span class="kw">trade war</span> can leave all countries worse off than under free trade.</p>

  <h2>Advantages of restricting free trade</h2>
  <ul>
    <li>Protects infant, declining and strategic industries; saves jobs.</li>
    <li>Reduces imports and may improve the current account.</li>
    <li>Raises government revenue (tariffs).</li>
    <li>Prevents dumping and limits demerit goods.</li>
  </ul>
  <h2>Disadvantages of restricting free trade</h2>
  <ul>
    <li>Higher prices and less choice for consumers.</li>
    <li>Lack of competition leads to inefficiency and complacency.</li>
    <li>Higher costs for firms using imported inputs.</li>
    <li>Retaliation and trade wars; lower exports.</li>
    <li>Smuggling; cost of administration; may breach trade agreements.</li>
    <li>Slower growth for both countries.</li>
  </ul>
  <p>The overall effect often depends on the <b>elasticity of demand for imports</b>: if demand is <b>inelastic</b>, a tariff raises prices without cutting imports much, mainly raising revenue; if <b>elastic</b>, imports fall a lot.</p>
'''
js = HEAD + COMMON + TM + '''
Lib.stepper($("#stH"), { w: 760, h: 400, label: "Who gains and who loses from a tariff?", base: { pw: 40, t: 0 }, draw: tmChart, steps: [
  { cap: "Free trade: price <b>$40</b>, consumers buy 70, domestic firms supply 30, imports 40.", s: { pw: 40, t: 0 } },
  { cap: "A <b>$10 tariff</b> raises the price to <b>$50</b>. <b>Consumers lose</b>: they pay more and buy less (60).", s: { pw: 40, t: 10 } },
  { cap: "<b>Domestic producers gain</b>: they sell more (40) at a higher price. <b>The government gains</b> tariff revenue (the green box). <b>Foreign exporters lose</b>: imports fall from 40 to 20.", s: { pw: 40, t: 10 } },
  { cap: "<b>Evaluate:</b> the loss to consumers is larger than the gains to domestic producers and the government taken together, so the economy as a whole is likely to lose, though protected workers gain.", s: { pw: 40, t: 10 } },
] });
const TW = ["Country A raises tariffs on imports from Country B", "B's exporters lose sales and jobs", "B retaliates with tariffs on imports from A", "A's exporters lose sales; both countries' consumers pay more", "Firms' supply chains are disrupted and costs rise", "Trade and growth fall in both countries: a trade war"];
Lib.stepper($("#stW"), { w: 760, h: 400, label: "A trade war", base: { n: 0 }, draw: mkChain(TW, "--bad"), steps: chainSteps(["Country A <b>raises tariffs</b> on imports from Country B.", "B's <b>exporters lose sales</b> and jobs.", "B <b>retaliates</b> with tariffs on imports from A.", "A's exporters lose sales; <b>consumers in both countries pay more</b>.", "Firms' <b>supply chains are disrupted</b> and costs rise.", "<b>Trade and growth fall</b> in both countries: a trade war leaves everyone worse off."]) });
const PT = ["The home country imposes a tariff or quota", "Foreign exporters sell less in that market", "Foreign firms cut output and workers lose jobs", "Their export earnings and growth fall", "The foreign government may retaliate or seek new markets", "Trading partners' current accounts and incomes may worsen"];
Lib.stepper($("#stP"), { w: 760, h: 400, label: "Effects on trading partners", base: { n: 0 }, draw: mkChain(PT, "--warn"), steps: chainSteps(["The home country imposes a <b>tariff or quota</b>.", "<b>Foreign exporters</b> sell less in that market.", "Foreign firms <b>cut output</b> and workers lose jobs.", "Their <b>export earnings and growth</b> fall.", "The foreign government may <b>retaliate</b> or seek new markets.", "Trading partners' <b>current accounts and incomes</b> may worsen."]) });

/* Lab 1: trade war */
function labW() {
  if (!$("#wa") || !$("#wb")) return;
  const tA = +$("#wa").value, r = +$("#wb").value / 100, tB = r * tA, outA = 100 + 0.2 * tA - 0.3 * tB, outB = 100 + 0.2 * tB - 0.3 * tA, price = 0.5 * tA, wt = 100 - 0.5 * (tA + tB);
  $("#wa1").textContent = money(outA, 1); $("#wa2").textContent = money(outB, 1); $("#wa3").textContent = "+" + money(price, 1) + "%"; $("#wa4").textContent = money(wt, 0);
  $("#wav").textContent = tA === 0 ? "No tariff: free trade, output index 100 for both." : `A's tariff of ${tA}% protects some of its industries (+${money(0.2 * tA, 1)}), but ${r > 0 ? `B retaliates with ${money(tB, 0)}%, hitting A's exports (−${money(0.3 * tB, 1)}). Net output index for A: ${money(outA, 1)}.` : "B does not retaliate. A's output index rises slightly."} B's output index: ${money(outB, 1)}. World trade falls to ${money(wt, 0)}. Consumers in A pay about ${money(price, 1)}% more. ${r >= 1 && tA > 0 ? "With full retaliation both countries end up worse off than under free trade: a trade war." : ""}`;
  const base = 290, k = 2.4; let o = SV.line(60, base, 700, base);
  [["Output A", outA, "--accent"], ["Output B", outB, "--good"], ["World trade", wt, "--warn"]].forEach(([n, v, c], i) => { const x = 130 + i * 190, h = (v - 50) * k * 1.5; o += SV.rect(x, base - h, 120, h, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.text(x + 60, base - h - 8, money(v, 1), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 60, base + 22, n, "sm", { "text-anchor": "middle" }); });
  $("#labW").innerHTML = o + SV.text(60, 24, "Index (free trade = 100). Illustrative model.", "sm");
}
Lib.slider($("#g1"), { id: "wa", label: "Country A's tariff", min: 0, max: 40, step: 5, value: 20, fmt: (v) => v + "%", onInput: labW });
Lib.slider($("#g2"), { id: "wb", label: "Country B's retaliation (share of A's tariff matched)", min: 0, max: 100, step: 25, value: 100, fmt: (v) => v + "%", onInput: labW });
const WL = [
  { n: "Consumers in the home country", g: "None, unless a protected industry becomes efficient.", l: "Higher prices, less choice, lower quality if competition falls." },
  { n: "Protected domestic producers", g: "More sales and profit; jobs protected.", l: "May become inefficient and complacent." },
  { n: "Firms using imported inputs", g: "None.", l: "Higher costs; some lose competitiveness." },
  { n: "The home government", g: "Tariff revenue; may improve the current account.", l: "May have to pay subsidies; higher inflation; breaking trade agreements." },
  { n: "Foreign exporters", g: "None.", l: "Lost sales, jobs and earnings; may retaliate." },
  { n: "Foreign consumers", g: "May gain if other exports are cheaper (diverted).", l: "Higher prices if they retaliate." },
];
button_table("wlBtns", "wlOut", WL, 0, (p) => `<div class="tw"><table class="t"><tr><th>Possible gains</th><th>Possible losses</th></tr><tr><td>${p.g}</td><td>${p.l}</td></tr></table></div>`);
const AD = [
  { n: "For the home country", a: "Protects jobs and infant, declining and strategic industries; may reduce the current account deficit; raises revenue.", d: "Higher prices; less choice; inefficiency; higher costs for firms using imports; risk of retaliation." },
  { n: "For trading partners", a: "None directly; may find new markets.", d: "Lost exports, jobs and growth; may widen their current account deficit; may retaliate." },
  { n: "For the world economy", a: "Can protect vulnerable industries while they adjust.", d: "Less trade and specialisation; slower growth; trade wars; less competition." },
];
button_table("adBtns", "adOut", AD, 0, (p) => `<div class="tw"><table class="t"><tr><th>Advantages</th><th>Disadvantages</th></tr><tr><td>${p.a}</td><td>${p.d}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is each effect of a tariff a <b>gain</b> or a <b>loss</b> for the <b>home country</b>?", buckets: [{ label: "Gain" }, { label: "Loss" }], items: [
  { text: "Domestic producers sell more", b: 0 }, { text: "The government collects revenue", b: 0 }, { text: "Jobs saved in protected industries", b: 0 }, { text: "Imports fall, helping the current account", b: 0 },
  { text: "Consumers pay higher prices", b: 1 }, { text: "Less choice for consumers", b: 1 }, { text: "Firms using imported inputs face higher costs", b: 1 }, { text: "Protected firms may become inefficient", b: 1 },
], done: "Always give both sides." });
Lib.classify($("#cl2"), { prompt: "Who is affected? Is each effect on the <b>home country</b> or on <b>trading partners</b>?", buckets: [{ label: "Home country" }, { label: "Trading partners" }], items: [
  { text: "Consumers pay higher prices", b: 0 }, { text: "Domestic firms gain market share", b: 0 }, { text: "Tariff revenue for the government", b: 0 },
  { text: "Exporters lose sales and jobs", b: 1 }, { text: "Governments may retaliate with tariffs", b: 1 }, { text: "Export earnings fall", b: 1 },
], done: "Tariffs hurt trading partners' exporters." });
Lib.match($("#m1"), { prompt: "Match the term to its definition.", pairs: [
  ["Retaliation", "Responding to a trade restriction with one of your own"],
  ["Trade war", "Countries raising barriers against each other, harming trade"],
  ["Complacency", "Domestic firms becoming inefficient because of weak competition"],
  ["Consumer surplus", "The gain consumers get from paying less than they were willing to pay"],
  ["Trading partner", "A country that buys from and sells to your country"],
  ["Import-competing industry", "An industry that competes with imports"],
], done: "Good vocabulary scores marks." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>how a trade war reduces growth</b>.", items: [
  "One country raises tariffs",
  "Trading partners retaliate",
  "Trade between the countries falls",
  "Prices rise and supply chains are disrupted",
  "Firms cut output and investment: growth slows",
], done: "A trade war chain." });
''' + calc_js([
    ("A tariff raises the price of imported shoes from $50 to $60. By what percentage has the price risen?", 20, "10 ÷ 50 × 100 = <b>20%</b>.", None, None),
    ("A country's exports to a market fall from $80bn to $68bn after a tariff. By what percentage did they fall?", 15, "12 ÷ 80 × 100 = <b>15%</b>.", None, None),
    ("Domestic production rises from 30 to 40 units after a tariff. By what percentage?", 33.3, "10 ÷ 30 × 100 = <b>33.3%</b>.", None, 0.1),
]) + mcq_js("qz1", [
    ("Who is most likely to lose from a tariff on imports?", ["Domestic producers", "The government", "Consumers", "Protected workers"], 2, "Consumers pay higher prices."),
    ("A likely effect of a tariff on trading partners is:", ["Exports to that country rise", "Exports to that country fall", "No change", "Higher imports"], 1, "Foreign goods become dearer."),
    ("A trade war is:", ["Countries lowering tariffs", "Countries raising barriers against each other", "A war over trade routes", "Free trade"], 1, "Retaliation spirals."),
    ("A disadvantage of restricting trade is:", ["Protects jobs", "Raises revenue", "Higher prices for consumers", "Reduces imports"], 2, "Consumers lose."),
    ("A tariff is least likely to work if demand for imports is:", ["Elastic", "Inelastic", "Unit elastic", "Falling"], 1, "Imports will not fall much."),
]) + "\n" + cards_js([("Retaliation", "A response to a trade restriction with a similar restriction on the other country's goods."), ("Trade war", "A situation where countries impose trade restrictions on each other, harming trade."), ("Complacency", "A lack of effort to improve because of weak competition."), ("Trading partner", "A country with which another country regularly trades."), ("Consumer loss", "Higher prices and less choice for consumers caused by trade restrictions."), ("Import-competing industry", "An industry that competes directly with imports."), ("Smuggling", "Illegally bringing goods into a country to avoid tariffs or bans."), ("Efficiency", "Producing goods at the lowest cost possible."), ("Current account", "The part of the balance of payments for trade in goods and services and income flows.")]) + "labW(); \n"
explore = '''
  <h2>Lab 1 · A trade war</h2>
  <p>Country A raises a tariff. Country B may retaliate. See the effects on output, prices and world trade. (Illustrative model; free trade = 100.)</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div></div>
    <div><div class="readout"><div><small>Output in A</small><strong id="wa1"></strong></div><div><small>Output in B</small><strong id="wa2"></strong></div><div><small>Prices for A's consumers</small><strong id="wa3"></strong></div><div><small>World trade</small><strong id="wa4"></strong></div></div><div class="verdict" id="wav"></div></div></div>
    <svg id="labW" viewBox="0 0 760 330" role="img" aria-label="Output and trade in a trade war"></svg>
  </div>

  <h2>Lab 2 · Who gains and loses from restrictions?</h2>
  <p>Pick a group to see the possible gains and losses.</p>
  <div class="card"><div class="row" id="wlBtns"></div><div id="wlOut"></div></div>

  <h2>Lab 3 · Advantages and disadvantages</h2>
  <p>Pick a perspective to see the advantages and disadvantages of restricting free trade.</p>
  <div class="card"><div class="row" id="adBtns"></div><div id="adOut"></div></div>
'''
ex = exam(
    Q(1, "Explain", 4, "Explain how a tariff on imports could affect consumers and producers in the country imposing it.", "Consumers: higher price, less choice. Producers: more sales.",
      "[K|A tariff raises the price of imports.] [N|Consumers pay more and buy less, and may have less choice, so their living standards could fall.] [K|Domestic producers face less competition from imports.] [N|They can sell more and raise output, so profits and jobs could rise.]"),
    Q(2, "Explain", 4, "Explain two ways in which a country's trading partners may be affected when it imposes import restrictions.", "Lost exports; retaliation; lower growth.",
      "[K|Its trading partners' exporters lose sales.] [N|Imports become dearer in the country with the restrictions, so demand for foreign goods falls, reducing output and jobs in exporting industries.] [K|Trading partners may retaliate.] [N|If they impose their own tariffs, the first country's exports fall, so both countries lose trade.]"),
    Q(3, "Analyse", 6, "Analyse how a trade war could affect an economy.", "Retaliation; lower trade; higher prices; supply chains; growth.",
      "[K|A trade war is when countries raise tariffs on each other's goods in turn.] [N|Exports to the other country fall, so exporters lose sales and workers may lose jobs.] [N|Imports become dearer, raising prices for consumers and costs for firms that use imported inputs, which could cause cost-push inflation.] [N|Supply chains are disrupted, firms cut investment and growth slows.] [E|Some protected industries might gain, but overall both economies are likely to be worse off.]", key=True),
    Q(4, "Discuss", 8, "Discuss whether or not protection in international trade benefits an economy. (May/June 2022, P23)", "For: current account, infant and sunset industries, strategic, demerit goods. Against: higher prices, retaliation, higher input costs, complacency, unemployment where imports are used.",
      "[K|Protection means measures such as tariffs, quotas and subsidies that restrict imports and help domestic firms.] [N|It could benefit an economy by reducing imports and improving the current account, protecting infant industries so they can grow and compete, and maintaining jobs in declining or strategic industries.] [N|It may also restrict harmful imports of demerit goods.] [E|These gains are larger if protection is temporary and targeted.] [N|However, higher prices reduce consumers' purchasing power, and firms that use imported raw materials face higher costs.] [N|Other countries may retaliate, making it harder to export, and protected firms may become complacent and produce low-quality goods.] [E|Overall, protection is likely to benefit particular industries but harm the economy as a whole if it is widespread and permanent, so it depends on how long, how much and which industries.]", key=True),
    Q(5, "Discuss", 6, "Discuss whether or not an increase in its import tariffs would be likely to benefit the Pakistani economy. (May/June 2020, P22)", "For: reduce imports and deficit, protect industries, revenue. Against: prices, retaliation, input costs.",
      "[K|An import tariff is a tax on imports.] [N|Higher tariffs could reduce imports and the current account deficit, protect domestic industries and raise government revenue.] [N|Domestic firms could expand and create jobs.] [E|The gain is greater if demand for imports is elastic.] [N|However, consumers would pay higher prices, firms using imported inputs would face higher costs, and trading partners may retaliate, reducing Pakistan's exports.] [E|Overall, tariffs could help some industries but their net effect on the economy is uncertain and depends on retaliation and elasticity.]", key=True),
    Q(6, "Discuss", 8, "Discuss whether or not an increase in government subsidies will reduce a deficit on the current account of the balance of payments. (Feb/Mar 2021, P22)", "For: lowers costs, exports and import substitutes. Against: cost to taxpayers, inefficiency, may not raise exports, imports of inputs, retaliation, time.",
      "[K|A subsidy is a payment to producers that lowers their costs.] [N|It could reduce a current account deficit by making domestic goods cheaper, so exports rise and consumers switch from imports to domestic products.] [N|Lower costs may also raise output and competitiveness.] [E|This works best if demand for the goods is elastic.] [N|However, subsidies cost taxpayers and may require higher taxes or borrowing, and other countries may retaliate or complain, reducing exports.] [N|Subsidised firms may become inefficient, and if they use imported raw materials, imports could rise.] [E|Overall, subsidies may narrow the deficit but the effect depends on elasticity and on how the subsidy is paid for.]", key=True),
)
tp = tips([
    ("Give effects on the home country and trading partners.", "The syllabus asks for both."),
    ("Name who gains and who loses.", "Consumers, producers, workers, government, foreign exporters."),
    ("Trade wars harm everyone.", "Retaliation lowers trade and growth."),
    ("Evaluate with elasticity.", "A tariff only cuts imports if demand is elastic."),
    ("End with 'it depends on…'.", "Temporary or permanent, which industries, retaliation."),
], cmds("Explain", "Analyse", "Discuss"))
body = page(CL("6.2.6 Consequences of trade restrictions"), "Consequences of Trade Restrictions", "The effects of trade restrictions on the home country and its trading partners, trade wars, and the advantages and disadvantages of restricting free trade. Syllabus 6.2.6.",
    learn=learn, watch=watch(("Who gains and who loses from a tariff?", "stH"), ("A trade war", "stW"), ("Effects on trading partners", "stP")), explore=explore,
    practise=practise(("Gain or loss for the home country?", "cl1", "card"), ("Home country or trading partners?", "cl2", "card"), ("Match the term", "m1", "card"), ("Order the trade war chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("US-China tariffs, 2018 onwards", "The US and China raised tariffs on hundreds of billions of dollars of each other's goods. US farmers lost sales, prices rose for some goods, and firms moved some production to other countries.", "Retaliation and a trade war."),
        rw("Smoot-Hawley tariffs, 1930", "US tariffs raised in 1930 were followed by retaliation by other countries, and world trade fell sharply during the Great Depression.", "A historic trade war."),
        rw("Cars and EU protection", "The EU's tariff on imported cars raises prices for European consumers but protects European car producers.", "Gains for producers, losses for consumers."),
        rw("Chicken wars", "Several African countries have restricted imports of cheap frozen chicken to protect local poultry farmers, raising prices for consumers.", "Protection of local producers against cheap imports.")),
    exam=ex, tips=tp)
write("tr3", body, js, "Consequences of Trade Restrictions", "ig-trade-restrictions-consequences")
