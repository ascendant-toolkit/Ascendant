"""Builds the five IGCSE Economics 2.6 Price elasticity of demand reviews (2.6.1 to 2.6.5).
Run: python3 tools/artifact-kit/mk_ig26.py"""
from igsy import *
F = Old("fisc")
M = Old("mon")
HEAD = M.j_((2, 25)) + F.j_((139, 160))
COMMON = open(D / "mk_ig44.py").read().split("COMMON = '''")[1].split("'''")[0]
CL = lambda t: f"IGCSE Economics · 0455 · {t}"
DSJS = open(D / "mk_ig24.py").read().split("DSJS = '''")[1].split("'''")[0]
PEDJS = '''
/* PED curves through (50, 50). kind: 0 inelastic perfectly, 1 inelastic, 2 unitary, 3 elastic, 4 perfectly elastic */
function pedCurve(kind, cls, lab, t) {
  let o = "", lx = 0, ly = 0;
  if (kind === 0) { o = SV.line(X(50), Y(0), X(50), Y(105), cls || "c1"); lx = 50; ly = 100; }
  else if (kind === 4) { o = SV.line(X(0), Y(50), X(110), Y(50), cls || "c1"); lx = 112; ly = 50; }
  else if (kind === 2) { let d = ""; for (let q = 25; q <= 105; q += 2) d += (d ? "L" : "M") + X(q).toFixed(1) + " " + Y(2500 / q).toFixed(1); o = SV.path(d, cls || "c1"); lx = 100; ly = 25; }
  else { const k = kind === 1 ? 3 : 0.35, qa = Math.max(0, 50 - 48 / k), qb = Math.min(108, 50 + 48 / k), pa = 50 - k * (qa - 50), pb = 50 - k * (qb - 50); o = SV.line(X(qa), Y(pa), X(qb), Y(pb), cls || "c1"); lx = qb + 1; ly = pb; }
  return o + SV.text(X(lx) + 6, Y(ly), lab || "D", "lbl bd " + (t || "t1"));
}
function pedLabel(v) { if (v === 0) return "perfectly inelastic"; if (v === Infinity) return "perfectly elastic"; const a = Math.abs(v); return a < 0.99 ? "inelastic" : a > 1.01 ? "elastic" : "unitary"; }
'''

# =========================================================== 2.6.1
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p><span class="kw">Price elasticity of demand (PED)</span> measures <b>how responsive the quantity demanded of a good is to a change in its price</b>. If a small price change causes a large change in quantity demanded, demand is <b>elastic</b>. If a large price change causes only a small change in quantity demanded, demand is <b>inelastic</b>.</p></div>

  <h2>Why it matters</h2>
  <ul>
    <li>Demand curves slope downwards, but the <b>steepness</b> differs from good to good.</li>
    <li>PED tells firms what happens to <b>sales and revenue</b> when they change the price, and tells governments what happens when they <b>tax</b> a good.</li>
  </ul>

  <h2>Elastic and inelastic demand</h2>
  <div class="tw"><table class="t">
    <tr><th></th><th>Elastic demand</th><th>Inelastic demand</th></tr>
    <tr><td><b>Response</b></td><td>Quantity demanded changes by a <b>bigger percentage</b> than the price</td><td>Quantity demanded changes by a <b>smaller percentage</b> than the price</td></tr>
    <tr><td><b>Curve</b></td><td>Flatter</td><td>Steeper</td></tr>
    <tr><td><b>Examples</b></td><td>Branded chocolate bars, holidays, restaurant meals (many substitutes)</td><td>Petrol, salt, medicine, cigarettes (few substitutes or necessities)</td></tr>
  </table></div>
  <p class="note">The word <b>elastic</b> means stretchy: if the price changes, quantity demanded stretches a lot. <b>Inelastic</b> means it hardly moves.</p>

  <h2>The idea in a sentence</h2>
  <div class="formula">PED = % change in quantity demanded ÷ % change in price</div>
  <p>The next review shows how to calculate and interpret the value.</p>
'''
js = HEAD + COMMON + DSJS + PEDJS + '''
Lib.stepper($("#stE"), { w: 760, h: 380, label: "Elastic vs inelastic", base: { n: 0 }, draw: (s) => {
  let o = axes();
  if (s.n >= 0) o += pedCurve(3, "c2", "Elastic D", "t2") + SV.circle(X(50), Y(50), 6, "dot1");
  if (s.n >= 1) o += pedCurve(1, "c1", "Inelastic D", "t1");
  return o;
}, steps: [
  { cap: "A <b>flat</b> (elastic) demand curve: a small price change makes quantity demanded change a lot.", s: { n: 0 } },
  { cap: "A <b>steep</b> (inelastic) demand curve: a big price change changes quantity demanded only a little.", s: { n: 1 } },
] });
const RS = ["The price of a good rises by 10%", "Quantity demanded changes", "If quantity falls by more than 10%: elastic", "If quantity falls by less than 10%: inelastic", "PED measures this response"];
Lib.stepper($("#stR"), { w: 760, h: 380, label: "Responsiveness", base: { n: 0 }, draw: mkChain(RS, "--accent"), steps: chainSteps(["The <b>price</b> of a good rises by 10%.", "<b>Quantity demanded</b> changes.", "If quantity falls by <b>more</b> than 10%: <b>elastic</b>.", "If quantity falls by <b>less</b> than 10%: <b>inelastic</b>.", "<b>PED</b> measures this response."]) });

/* Lab 1 */
function labR() {
  if (!$("#ra") || !$("#rb")) return;
  const dp = +$("#ra").value, dq = +$("#rb").value, ped = dp === 0 ? 0 : dq / dp, lab = pedLabel(Math.abs(ped));
  $("#ra1").textContent = (dq >= 0 ? "+" : "") + dq + "%"; $("#ra2").textContent = money(Math.abs(ped), 2); $("#ra3").textContent = lab.charAt(0).toUpperCase() + lab.slice(1);
  $("#rav").textContent = `A ${dp}% price rise cuts quantity demanded by ${Math.abs(dq)}%. The percentage change in quantity (${Math.abs(dq)}) is ${Math.abs(dq) > dp ? "bigger" : Math.abs(dq) < dp ? "smaller" : "equal"} than the percentage change in price (${dp}), so demand is ${lab}.`;
  const q1 = 50 * (1 - Math.abs(dq) / 100), p1 = 50 * (1 + dp / 100), k = (p1 - 50) / (q1 - 50), qa = Math.max(0, 50 + (95 - 50) / k), qb = Math.min(108, 50 + (5 - 50) / k), pa = 50 + k * (qa - 50), pb = 50 + k * (qb - 50);
  $("#labR").innerHTML = axes() + SV.line(X(qa), Y(pa), X(qb), Y(pb), "c1") + dsDrop(50, 50) + SV.circle(X(50), Y(50), 6, "dot1") + dsDrop(q1, p1) + SV.circle(X(q1), Y(p1), 7, "dot2") + SV.text(X(0) - 8, Y(50), "P", "sm bd", { "text-anchor": "end" }) + SV.text(X(0) - 8, Y(p1), "P₁", "sm bd", { "text-anchor": "end" }) + SV.text(X(50), Y(0) + 18, "Q", "sm bd", { "text-anchor": "middle" }) + SV.text(X(q1), Y(0) + 18, "Q₁", "sm bd", { "text-anchor": "middle" });
}
Lib.slider($("#g1"), { id: "ra", label: "Price rise", min: 5, max: 40, step: 5, value: 10, fmt: (v) => "+" + v + "%", onInput: labR });
Lib.slider($("#g2"), { id: "rb", label: "Change in quantity demanded", min: -80, max: -2, step: 2, value: -20, fmt: (v) => v + "%", onInput: labR });
const EL = [
  { n: "Petrol", t: "Inelastic", w: "Necessity for drivers; few substitutes in the short run." },
  { n: "Salt", t: "Inelastic", w: "Cheap; no close substitute; tiny part of spending." },
  { n: "Branded chocolate", t: "Elastic", w: "Many substitute brands; a luxury." },
  { n: "Package holidays", t: "Elastic", w: "Many alternatives; large part of income." },
  { n: "Life-saving medicine", t: "Inelastic", w: "Essential; no substitute." },
];
button_table("elBtns", "elOut", EL, 0, (p) => `<div class="tw"><table class="t"><tr><th>Demand is</th><th>Why</th></tr><tr><td><b>${p.t}</b></td><td>${p.w}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Is demand for each likely to be <b>elastic</b> or <b>inelastic</b>?", buckets: [{ label: "Elastic" }, { label: "Inelastic" }], items: [
  { text: "A luxury holiday", b: 0 }, { text: "A branded snack with many rivals", b: 0 }, { text: "A restaurant meal", b: 0 },
  { text: "Petrol", b: 1 }, { text: "Salt", b: 1 }, { text: "Insulin for diabetics", b: 1 },
], done: "Substitutes and necessity matter." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [
  ["PED", "Responsiveness of quantity demanded to a price change"],
  ["Elastic demand", "Quantity changes by a bigger % than price"],
  ["Inelastic demand", "Quantity changes by a smaller % than price"],
  ["Flat demand curve", "Elastic"],
  ["Steep demand curve", "Inelastic"],
  ["Responsiveness", "How much one variable reacts to another"],
], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>what happens to quantity when price rises for an elastic good</b>.", items: [
  "The price rises by 10%",
  "Consumers switch to substitutes",
  "Quantity demanded falls by more than 10%",
  "Demand is elastic",
], done: "Elastic means a big response." });
''' + calc_js([
    ("A 10% rise in price causes a 20% fall in quantity demanded. Is the % change in quantity bigger? Enter the % change in quantity (positive number).", 20, "<b>20%</b>: bigger than 10%, so demand is elastic.", None, None),
    ("Price rises 20% and quantity demanded falls 5%. What is the size of the % change in quantity?", 5, "<b>5%</b>: smaller than 20%, so demand is inelastic.", None, None),
]) + mcq_js("qz1", [
    ("PED measures:", ["How price responds to quantity", "How quantity demanded responds to price", "Income and demand", "Supply and price"], 1, "Responsiveness of Qd to price."),
    ("Demand is elastic if:", ["Quantity changes by a smaller % than price", "Quantity changes by a bigger % than price", "Price does not change", "Quantity is zero"], 1, "A big response."),
    ("Which is likely to be inelastic?", ["A branded chocolate", "Petrol", "A holiday", "A restaurant meal"], 1, "A necessity."),
    ("An elastic demand curve is:", ["Steep", "Flat", "Vertical", "Absent"], 1, "Flatter."),
    ("Inelastic demand means consumers:", ["Respond a lot to price", "Respond little to price", "Buy nothing", "Buy more when price rises"], 1, "Hardly respond."),
]) + "\n" + cards_js([("Price elasticity of demand", "A measure of the responsiveness of quantity demanded to a change in price."), ("Elastic demand", "Quantity demanded changes by a bigger percentage than price."), ("Inelastic demand", "Quantity demanded changes by a smaller percentage than price."), ("Responsiveness", "How much one variable reacts to a change in another."), ("Substitute", "A good that can replace another."), ("Necessity", "A good people need and cannot easily do without."), ("Luxury", "A good people want but could do without."), ("Quantity demanded", "The amount bought at one price."), ("Percentage change", "Change divided by the original, times 100.")]) + "labR(); \n"
explore = '''
  <h2>Lab 1 · How responsive is demand?</h2>
  <p>Set the price rise and the fall in quantity demanded and see whether demand is elastic or inelastic.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div></div>
    <div><div class="readout"><div><small>Change in quantity</small><strong id="ra1"></strong></div><div><small>Size of response</small><strong id="ra2"></strong></div><div><small>Demand is</small><strong id="ra3"></strong></div></div><div class="verdict" id="rav"></div></div></div>
    <svg id="labR" viewBox="0 0 760 340" role="img" aria-label="A demand curve showing responsiveness"></svg>
  </div>

  <h2>Lab 2 · Elastic or inelastic goods?</h2>
  <p>Pick a good to see its likely elasticity and why.</p>
  <div class="card"><div class="row" id="elBtns"></div><div id="elOut"></div></div>
'''
ex = exam(
    Q(1, "Define", 2, "Define price elasticity of demand. (Oct/Nov 2022, P22 style)", "Responsiveness of quantity demanded to a price change.", "[K|Price elasticity of demand is a measure of the responsiveness] [K|of quantity demanded to a change in price.]"),
    Q(2, "Explain", 4, "Explain the difference between elastic and inelastic demand.", "Bigger % change in quantity vs smaller.",
      "[K|With elastic demand a change in price causes a bigger percentage change in quantity demanded.] [N|Consumers respond strongly, for example by switching to substitutes.] [K|With inelastic demand quantity demanded changes by a smaller percentage than the price.] [N|Consumers respond little because the good is a necessity or has few substitutes.]"),
    Q(3, "Identify", 2, "Identify two goods with inelastic demand.", "Petrol, salt, medicine.", "[K|Petrol.] [K|Salt (or medicine).]"),
)
tp = tips([
    ("PED = responsiveness of Qd to price.", "Say 'quantity demanded'."),
    ("Elastic = flat; inelastic = steep.", "Drawing tip."),
    ("Substitutes and necessity decide it.", "Name them."),
    ("Compare % changes.", "Bigger or smaller."),
], cmds("Define", "Identify", "Explain"))
body = page(CL("2.6.1 Definition of price elasticity of demand (PED)"), "Definition of Price Elasticity of Demand", "What PED measures and the difference between elastic and inelastic demand. Syllabus 2.6.1.",
    learn=learn, watch=watch(("Elastic vs inelastic", "stE"), ("Responsiveness", "stR")), explore=explore,
    practise=practise(("Elastic or inelastic?", "cl1", "card"), ("Match the term", "m1", "card"), ("Order the chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("Petrol", "Drivers keep buying even when prices jump, because there are few short-run substitutes.", "Inelastic demand."),
        rw("Streaming subscriptions", "Many rivals exist, so a price rise often leads subscribers to cancel.", "Elastic demand."),
        rw("Cigarettes", "Smokers cut back little when prices rise because of addiction.", "Inelastic demand."),
        rw("Foreign holidays", "Households quickly switch to cheaper destinations or stay at home when prices rise.", "Elastic demand.")),
    exam=ex, tips=tp)
write("p261", body, js, "Definition of Price Elasticity of Demand", "ig-ped-definition")

# =========================================================== 2.6.2
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>PED is calculated with the formula <b>PED = % change in quantity demanded ÷ % change in price</b>. Because demand slopes downwards, PED is <b>negative</b> and we usually ignore the sign and look at its <b>size</b>. The size tells us whether demand is perfectly inelastic, inelastic, unitary, elastic or perfectly elastic.</p></div>

  <h2>Calculating PED</h2>
  <div class="formula">% change = (new − old) ÷ old × 100<br>PED = % change in quantity demanded ÷ % change in price</div>
  <p><b>Example:</b> price rises from $10 to $12 (+20%) and quantity demanded falls from 100 to 70 (−30%). PED = −30 ÷ +20 = <b>−1.5</b>. Ignoring the sign, 1.5: <b>elastic</b>.</p>

  <h2>Interpreting the value</h2>
  <div class="tw"><table class="t">
    <tr><th>PED (ignoring sign)</th><th>Name</th><th>Meaning</th><th>Curve</th></tr>
    <tr><td><b>0</b></td><td>Perfectly inelastic</td><td>Quantity demanded does not change at all</td><td>Vertical</td></tr>
    <tr><td><b>Between 0 and 1</b></td><td>Inelastic</td><td>Quantity changes by a smaller % than price</td><td>Steep</td></tr>
    <tr><td><b>1</b></td><td>Unitary</td><td>Quantity changes by the same % as price</td><td>Rectangular hyperbola</td></tr>
    <tr><td><b>Greater than 1</b></td><td>Elastic</td><td>Quantity changes by a bigger % than price</td><td>Flat</td></tr>
    <tr><td><b>Infinity</b></td><td>Perfectly elastic</td><td>Any rise in price reduces quantity demanded to zero</td><td>Horizontal</td></tr>
  </table></div>
  <p class="note">Use the <b>% change</b>, not the absolute change. For a fall in price the signs are reversed but the result is the same. Always show your working and state whether demand is elastic or inelastic.</p>
'''
js = HEAD + COMMON + DSJS + PEDJS + '''
const KN = [["Perfectly inelastic: PED = 0", 0], ["Inelastic: PED between 0 and 1", 1], ["Unitary: PED = 1", 2], ["Elastic: PED greater than 1", 3], ["Perfectly elastic: PED = infinity", 4]];
Lib.stepper($("#stK"), { w: 760, h: 380, label: "Five types of PED", base: { k: 0 }, draw: (s) => axes() + pedCurve(s.k, "c1", "D") + SV.text(X(3), Y(106), KN[s.k][0], "lbl bd t1"), steps: KN.map(([c, k]) => ({ cap: "<b>" + c + "</b>.", s: { k } })) });
const CL2 = ["Find the % change in quantity demanded", "Find the % change in price", "Divide: quantity ÷ price", "Ignore the sign; compare with 1", "Say elastic or inelastic"];
Lib.stepper($("#stC"), { w: 760, h: 380, label: "Calculating PED", base: { n: 0 }, draw: mkChain(CL2, "--accent"), steps: chainSteps(["Find the <b>% change in quantity</b> demanded.", "Find the <b>% change in price</b>.", "<b>Divide</b>: quantity ÷ price.", "Ignore the sign; <b>compare with 1</b>.", "Say <b>elastic or inelastic</b>."]) });

/* Lab 1: calculator */
function labP() {
  if (!$("#pa") || !$("#pb") || !$("#pc") || !$("#pd")) return;
  const p0 = +$("#pa").value, p1 = +$("#pb").value, q0 = +$("#pc").value, q1 = +$("#pd").value, dp = (p1 - p0) / p0 * 100, dq = (q1 - q0) / q0 * 100, ped = dp === 0 ? 0 : dq / dp, a = Math.abs(ped);
  $("#pa1").textContent = money(dp, 1) + "%"; $("#pa2").textContent = money(dq, 1) + "%"; $("#pa3").textContent = money(ped, 2);
  $("#pav").textContent = `Price ${p0} → ${p1} is ${money(dp, 1)}%; quantity ${q0} → ${q1} is ${money(dq, 1)}%. PED = ${money(dq, 1)} ÷ ${money(dp, 1)} = ${money(ped, 2)}. Ignoring the sign, ${money(a, 2)}: demand is ${a === 0 ? "perfectly inelastic" : pedLabel(a)}.`;
  const k = a < 0.01 ? 0 : a < 0.99 ? 1 : a < 1.01 ? 2 : 3;
  $("#labP").innerHTML = axes() + pedCurve(k, "c1", "D") + SV.circle(X(50), Y(50), 6, "dot1");
}
[["g1", "pa", "Old price ($)", 10, 5, 20], ["g2", "pb", "New price ($)", 12, 5, 20], ["g3", "pc", "Old quantity", 100, 20, 200], ["g4", "pd", "New quantity", 70, 0, 200]].forEach(([g, id, l, v, mn, mx]) => Lib.slider($("#" + g), { id, label: l, min: mn, max: mx, step: id === "pa" || id === "pb" ? 1 : 10, value: v, fmt: (x) => x, onInput: labP }));
const TY = [
  { n: "PED = 0", t: "Perfectly inelastic", c: "Vertical curve", e: "Insulin, for a patient who must buy a fixed dose." },
  { n: "0 < PED < 1", t: "Inelastic", c: "Steep curve", e: "Petrol, salt, cigarettes." },
  { n: "PED = 1", t: "Unitary", c: "Curved (hyperbola)", e: "Rare; revenue is unchanged by a price change." },
  { n: "PED > 1", t: "Elastic", c: "Flat curve", e: "Holidays, branded goods." },
  { n: "PED = ∞", t: "Perfectly elastic", c: "Horizontal curve", e: "A firm in perfect competition: any higher price loses all sales." },
];
button_table("tyBtns", "tyOut", TY, 0, (p) => `<div class="tw"><table class="t"><tr><th>Name</th><th>Curve</th><th>Example</th></tr><tr><td><b>${p.t}</b></td><td>${p.c}</td><td>${p.e}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Which <b>type of PED</b> is each value (ignoring the sign)?", buckets: [{ label: "Inelastic (0 to 1)" }, { label: "Unitary (1)" }, { label: "Elastic (above 1)" }], items: [
  { text: "0.3", b: 0 }, { text: "0.8", b: 0 }, { text: "1.0", b: 1 }, { text: "1.5", b: 2 }, { text: "3.2", b: 2 }, { text: "0.5", b: 0 },
], done: "Compare the size with 1." });
Lib.classify($("#cl2"), { prompt: "Which <b>curve shape</b> matches each PED?", buckets: [{ label: "Vertical" }, { label: "Steep" }, { label: "Flat" }, { label: "Horizontal" }], items: [
  { text: "PED = 0", b: 0 }, { text: "PED = 0.4", b: 1 }, { text: "PED = 2.5", b: 2 }, { text: "PED = infinity", b: 3 },
], done: "Steeper means more inelastic." });
Lib.match($("#m1"), { prompt: "Match the term to its PED value.", pairs: [
  ["Perfectly inelastic", "PED = 0"],
  ["Inelastic", "PED between 0 and 1"],
  ["Unitary", "PED = 1"],
  ["Elastic", "PED greater than 1"],
  ["Perfectly elastic", "PED = infinity"],
  ["Formula", "% change in Qd ÷ % change in price"],
], done: "Learn the five." });
Lib.order($("#o1"), { prompt: "Put the steps in order: <b>calculating PED</b>.", items: [
  "Calculate the % change in quantity demanded",
  "Calculate the % change in price",
  "Divide the first by the second",
  "Ignore the sign",
  "State whether demand is elastic or inelastic",
], done: "Show every step." });
''' + calc_js([
    ("Price rises from $10 to $12 and quantity demanded falls from 100 to 70. Calculate PED (ignore the sign, 1 decimal place).", 1.5, "%ΔP = 20%, %ΔQ = −30%. PED = −30 ÷ 20 = <b>−1.5</b>.", None, None),
    ("Price falls from $50 to $45 and quantity demanded rises from 200 to 210. Calculate PED (ignore the sign).", 0.5, "%ΔP = −10%, %ΔQ = +5%. PED = 5 ÷ −10 = <b>−0.5</b>.", None, None),
    ("Price rises 8% and quantity demanded falls 12%. Calculate PED (ignore the sign).", 1.5, "12 ÷ 8 = <b>1.5</b>: elastic.", None, None),
    ("PED is 0.4 and price rises 10%. By what percentage does quantity demanded fall?", 4, "0.4 × 10 = <b>4%</b>.", None, None),
]) + mcq_js("qz1", [
    ("PED is calculated as:", ["%ΔP ÷ %ΔQd", "%ΔQd ÷ %ΔP", "ΔQ ÷ ΔP", "P ÷ Q"], 1, "Quantity demanded over price."),
    ("A PED of −2 means demand is:", ["Inelastic", "Unitary", "Elastic", "Perfectly inelastic"], 2, "Size 2 is above 1."),
    ("A vertical demand curve shows:", ["Perfectly elastic demand", "Perfectly inelastic demand", "Unitary demand", "Elastic demand"], 1, "Qd does not change."),
    ("A PED of 0.6 means demand is:", ["Elastic", "Inelastic", "Unitary", "Perfectly elastic"], 1, "Between 0 and 1."),
    ("A horizontal demand curve shows:", ["Perfectly inelastic demand", "Perfectly elastic demand", "Unitary demand", "No demand"], 1, "Infinite response."),
]) + "\n" + cards_js([("PED formula", "% change in quantity demanded ÷ % change in price."), ("Perfectly inelastic", "PED = 0: quantity does not change."), ("Inelastic", "PED between 0 and 1."), ("Unitary", "PED = 1."), ("Elastic", "PED above 1."), ("Perfectly elastic", "PED = infinity: any rise in price cuts quantity to zero."), ("Percentage change", "(New − old) ÷ old × 100."), ("Ignoring the sign", "PED is negative for a normal good; we use its size."), ("Rectangular hyperbola", "The shape of a unitary elastic demand curve.")]) + "labP(); \n"
explore = '''
  <h2>Lab 1 · PED calculator</h2>
  <p>Enter old and new price and quantity and see the PED and curve.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div><div id="g4"></div></div>
    <div><div class="readout"><div><small>% change in price</small><strong id="pa1"></strong></div><div><small>% change in quantity</small><strong id="pa2"></strong></div><div><small>PED</small><strong id="pa3"></strong></div></div><div class="verdict" id="pav"></div></div></div>
    <svg id="labP" viewBox="0 0 760 340" role="img" aria-label="A demand curve for the calculated PED"></svg>
  </div>

  <h2>Lab 2 · The five types</h2>
  <p>Pick a type to see its curve and an example.</p>
  <div class="card"><div class="row" id="tyBtns"></div><div id="tyOut"></div></div>
'''
ex = exam(
    Q(1, "Calculate", 3, "The price of a good rises from $10 to $12. Quantity demanded falls from 100 to 70. Calculate PED. (May/June 2023, P22 style)", "%ΔQ ÷ %ΔP.", "[A|%ΔP = 2 ÷ 10 × 100 = 20%; %ΔQ = −30 ÷ 100 × 100 = −30%.] [A|PED = −30 ÷ 20] [A|= −1.5.]"),
    Q(2, "Explain", 4, "Explain what a PED value of 0.4 means.", "Inelastic; quantity responds less than price.",
      "[K|A PED of 0.4 means demand is inelastic.] [N|A 10% rise in price would cause quantity demanded to fall by only 4%.] [N|Consumers are not very responsive to price changes.]"),
    Q(3, "Identify", 2, "Identify the PED value for a perfectly inelastic demand curve.", "Zero.", "[K|Zero (0).] [K|Quantity demanded does not change.]"),
    Q(4, "Explain", 4, "Explain how a demand curve would look if demand was perfectly elastic.", "Horizontal; any rise loses all sales.",
      "[K|It would be a horizontal line.] [N|At that price consumers will buy any quantity,] [N|but if the price rises even slightly quantity demanded falls to zero.]"),
)
tp = tips([
    ("PED = %ΔQ ÷ %ΔP.", "Always use percentages."),
    ("Show every step.", "Percentage changes first."),
    ("Ignore the sign when interpreting.", "Compare the size with 1."),
    ("Learn the five values.", "0, <1, 1, >1, ∞."),
    ("State elastic or inelastic.", "Finish the answer."),
], cmds("Calculate", "Identify", "Explain"))
body = page(CL("2.6.2 Calculation of PED"), "Calculation and Interpretation of PED", "Calculating PED, interpreting its value and drawing demand curves for different elasticities. Syllabus 2.6.2.",
    learn=learn, watch=watch(("Five types of PED", "stK"), ("Calculating PED", "stC")), explore=explore,
    practise=practise(("Which type?", "cl1", "card"), ("Which curve?", "cl2", "card"), ("Match the term", "m1", "card"), ("Order the steps", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("Fuel", "Studies often find petrol has a PED well below 1 in the short run.", "Inelastic demand."),
        rw("Restaurant meals", "Diners switch away quickly when menu prices rise.", "Elastic demand."),
        rw("Tobacco", "A 10% price rise cuts smoking by only a few per cent.", "Inelastic demand."),
        rw("Own-brand vs brand-name", "Customers switch easily between close substitutes.", "Elastic demand.")),
    exam=ex, tips=tp)
write("p262", body, js, "Calculation and Interpretation of PED", "ig-ped-calculation")

# =========================================================== 2.6.3
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>How elastic or inelastic demand is depends on a set of <b>influences</b>. Goods with <b>close substitutes</b>, goods that are <b>luxuries</b>, goods that take a <b>large share of income</b> and goods with a <b>long time to adjust</b> tend to have <b>elastic</b> demand. The opposite gives <b>inelastic</b> demand.</p></div>

  <h2>Determinants of PED</h2>
  <div class="tw"><table class="t">
    <tr><th>Determinant</th><th>Elastic demand</th><th>Inelastic demand</th></tr>
    <tr><td><b>Availability of substitutes</b></td><td>Many close substitutes: easy to switch</td><td>Few or no substitutes</td></tr>
    <tr><td><b>Necessity or luxury</b></td><td>Luxury or want</td><td>Necessity</td></tr>
    <tr><td><b>Proportion of income spent</b></td><td>Large share of income (a car, a holiday)</td><td>Tiny share of income (salt, matches)</td></tr>
    <tr><td><b>Time period</b></td><td>Long run: time to find alternatives (e.g. buy an electric car)</td><td>Short run: habits and contracts limit change</td></tr>
    <tr><td><b>Addiction or habit</b></td><td>Not habit-forming</td><td>Addictive or habitual goods (cigarettes, caffeine)</td></tr>
    <tr><td><b>How broadly the good is defined</b></td><td>A specific brand (many rivals)</td><td>A broad category such as "food" or "fuel"</td></tr>
  </table></div>

  <h2>Examples</h2>
  <ul>
    <li><b>Petrol:</b> inelastic in the short run (few substitutes, a necessity, habitual), more elastic in the long run.</li>
    <li><b>A particular brand of trainers:</b> elastic (many rival brands).</li>
    <li><b>Salt:</b> inelastic (cheap, tiny share of income, no substitute).</li>
    <li><b>Foreign holidays:</b> elastic (luxury, large share of income, many alternatives).</li>
  </ul>
  <p class="note">An exam answer should name the determinant, say whether it makes demand more or less elastic and link it to the <b>product in the question</b>.</p>
'''
js = HEAD + COMMON + DSJS + PEDJS + '''
const SU = ["A brand of chocolate has many close rivals", "The price of the brand rises", "Consumers switch to rival brands", "Quantity demanded falls by a large %", "Demand is elastic"];
Lib.stepper($("#stS"), { w: 760, h: 380, label: "Many substitutes", base: { n: 0 }, draw: mkChain(SU, "--good"), steps: chainSteps(["A brand of chocolate has <b>many close rivals</b>.", "The <b>price rises</b>.", "Consumers <b>switch</b> to rival brands.", "Quantity demanded falls by a <b>large %</b>.", "Demand is <b>elastic</b>."]) });
const NE = ["Petrol is a necessity for drivers", "The price of petrol rises", "Drivers still need to travel", "Quantity demanded falls by a small %", "Demand is inelastic"];
Lib.stepper($("#stN"), { w: 760, h: 380, label: "A necessity", base: { n: 0 }, draw: mkChain(NE, "--bad"), steps: chainSteps(["Petrol is a <b>necessity</b> for drivers.", "The <b>price rises</b>.", "Drivers still <b>need to travel</b>.", "Quantity demanded falls by a <b>small %</b>.", "Demand is <b>inelastic</b>."]) });
Lib.stepper($("#stT"), { w: 760, h: 380, label: "Time and elasticity", base: { k: 1 }, draw: (s) => axes() + pedCurve(s.k, "c1", s.k === 1 ? "Short-run D" : "Long-run D", "t1"), steps: [
  { cap: "In the <b>short run</b> consumers have few options: demand is <b>inelastic</b> (steep).", s: { k: 1 } },
  { cap: "In the <b>long run</b> consumers find alternatives: demand is <b>more elastic</b> (flatter).", s: { k: 3 } },
] });

/* Lab 1: score a good */
function labD() {
  if (!$("#da") || !$("#db") || !$("#dc") || !$("#dd")) return;
  const s = +$("#da").value, n = +$("#db").value, i = +$("#dc").value, t = +$("#dd").value, score = s + (5 - n) + i + t, ped = 0.2 + score * 0.12, lab = pedLabel(ped);
  $("#da1").textContent = money(ped, 2); $("#da2").textContent = lab.charAt(0).toUpperCase() + lab.slice(1); $("#da3").textContent = score + " / 20";
  $("#dav").textContent = `With ${s} out of 5 for substitutes, a necessity score of ${n}, ${i} for share of income and ${t} for time to adjust, the elasticity score is ${score}/20 and PED is roughly ${money(ped, 2)}: ${lab}. More substitutes, a luxury, a bigger share of income and more time all push demand towards elastic (illustrative model).`;
  const k = ped < 0.99 ? 1 : ped > 1.01 ? 3 : 2;
  $("#labD").innerHTML = axes() + pedCurve(k, "c1", "D") + SV.circle(X(50), Y(50), 6, "dot1");
}
Lib.slider($("#g1"), { id: "da", label: "Availability of substitutes (1 few, 5 many)", min: 1, max: 5, step: 1, value: 3, fmt: (v) => v, onInput: labD });
Lib.slider($("#g2"), { id: "db", label: "How much of a necessity (1 luxury, 5 necessity)", min: 1, max: 5, step: 1, value: 3, fmt: (v) => v, onInput: labD });
Lib.slider($("#g3"), { id: "dc", label: "Share of income spent (1 tiny, 5 large)", min: 1, max: 5, step: 1, value: 3, fmt: (v) => v, onInput: labD });
Lib.slider($("#g4"), { id: "dd", label: "Time to adjust (1 short, 5 long)", min: 1, max: 5, step: 1, value: 3, fmt: (v) => v, onInput: labD });
const GD = [
  { n: "Petrol (short run)", d: "Inelastic", w: "Necessity, few substitutes, habitual." },
  { n: "Petrol (long run)", d: "More elastic", w: "People move closer to work or buy efficient cars." },
  { n: "A brand of trainers", d: "Elastic", w: "Many rival brands." },
  { n: "Salt", d: "Inelastic", w: "Cheap, no substitute, tiny share of income." },
  { n: "Cigarettes", d: "Inelastic", w: "Addictive." },
  { n: "A new car", d: "Elastic", w: "Large share of income; can delay." },
];
button_table("gdBtns", "gdOut", GD, 0, (p) => `<div class="tw"><table class="t"><tr><th>Demand is</th><th>Why</th></tr><tr><td><b>${p.d}</b></td><td>${p.w}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Does each make demand <b>more elastic</b> or <b>more inelastic</b>?", buckets: [{ label: "More elastic" }, { label: "More inelastic" }], items: [
  { text: "Many close substitutes", b: 0 }, { text: "A luxury good", b: 0 }, { text: "A large share of income", b: 0 }, { text: "A long time to adjust", b: 0 },
  { text: "Few substitutes", b: 1 }, { text: "A necessity", b: 1 }, { text: "A tiny share of income", b: 1 }, { text: "Addiction", b: 1 },
], done: "Substitutes, necessity, income share, time, habit." });
Lib.classify($("#cl2"), { prompt: "Is demand for each likely to be <b>elastic</b> or <b>inelastic</b>?", buckets: [{ label: "Elastic" }, { label: "Inelastic" }], items: [
  { text: "A branded soft drink", b: 0 }, { text: "A foreign holiday", b: 0 }, { text: "A new car", b: 0 },
  { text: "Salt", b: 1 }, { text: "Tap water", b: 1 }, { text: "Cigarettes", b: 1 },
], done: "Apply the determinants." });
Lib.match($("#m1"), { prompt: "Match the determinant to its effect.", pairs: [
  ["Many substitutes", "More elastic"],
  ["A necessity", "More inelastic"],
  ["Large share of income", "More elastic"],
  ["Long time period", "More elastic"],
  ["Addiction", "More inelastic"],
  ["Narrow definition (a brand)", "More elastic"],
], done: "Learn the determinants." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>why demand for petrol is inelastic in the short run</b>.", items: [
  "Petrol is a necessity for travel",
  "There are few substitutes in the short run",
  "The price of petrol rises",
  "Drivers cut consumption only slightly",
  "Demand is inelastic",
], done: "Necessity plus few substitutes." });
''' + calc_js([
    ("A good has a PED of 0.5. Price rises 20%. By what percentage does quantity demanded fall?", 10, "0.5 × 20 = <b>10%</b>.", None, None),
    ("A good has a PED of 2. Price rises 5%. By what percentage does quantity demanded fall?", 10, "2 × 5 = <b>10%</b>.", None, None),
]) + mcq_js("qz1", [
    ("Which makes demand more elastic?", ["Few substitutes", "A necessity", "Many close substitutes", "Addiction"], 2, "Easy to switch."),
    ("Demand for salt is inelastic because:", ["It is a luxury", "It is a tiny share of income with no substitute", "It has many substitutes", "It is expensive"], 1, "Cheap and essential."),
    ("In the long run demand tends to be:", ["More inelastic", "More elastic", "Unchanged", "Zero"], 1, "Time to find alternatives."),
    ("Which good is most likely to have elastic demand?", ["Salt", "Petrol", "A brand of chocolate", "Insulin"], 2, "Many rival brands."),
    ("Addictive goods tend to have:", ["Elastic demand", "Inelastic demand", "Perfectly elastic demand", "No demand"], 1, "Habit."),
]) + "\n" + cards_js([("Determinants of PED", "Factors that decide how elastic or inelastic demand is."), ("Substitutes", "Goods that can replace each other."), ("Necessity", "A good that people need."), ("Luxury", "A good that people want but can do without."), ("Proportion of income", "The share of income spent on a good."), ("Time period", "Demand is more elastic in the long run."), ("Addictive good", "A good people find hard to stop buying."), ("Short run", "A period too short to change habits or find alternatives."), ("Long run", "A period long enough to adjust.")]) + "labD(); \n"
explore = '''
  <h2>Lab 1 · Score a good</h2>
  <p>Set the four determinants for a good and see its likely PED.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div><div id="g3"></div><div id="g4"></div></div>
    <div><div class="readout"><div><small>Likely PED</small><strong id="da1"></strong></div><div><small>Demand is</small><strong id="da2"></strong></div><div><small>Score</small><strong id="da3"></strong></div></div><div class="verdict" id="dav"></div></div></div>
    <svg id="labD" viewBox="0 0 760 340" role="img" aria-label="A demand curve for the scored good"></svg>
  </div>

  <h2>Lab 2 · Goods and their elasticity</h2>
  <p>Pick a good to see why its demand is elastic or inelastic.</p>
  <div class="card"><div class="row" id="gdBtns"></div><div id="gdOut"></div></div>
'''
ex = exam(
    Q(1, "Explain", 4, "Explain two influences on the price elasticity of demand for a good.", "Substitutes, necessity, income share, time.",
      "[K|The availability of substitutes affects PED.] [N|If a good has many close substitutes, consumers can switch easily when its price rises, so demand is elastic.] [K|Whether a good is a necessity matters.] [N|Necessities such as salt have inelastic demand because people must keep buying them.]"),
    Q(2, "Explain", 4, "Explain why demand for petrol is likely to be more elastic in the long run than in the short run.", "Time to adjust: alternatives, cars, moving.",
      "[K|In the short run drivers have few alternatives and are tied to existing cars.] [N|In the long run consumers have time to switch to electric cars, move closer to work or use public transport,] [N|so quantity demanded responds more to the price: demand is more elastic.]"),
    Q(3, "Identify", 2, "Identify two goods with inelastic demand and say why.", "Necessities, addictive goods.", "[K|Cigarettes, because they are addictive.] [K|Salt, because it is a cheap necessity with no substitute.]"),
)
tp = tips([
    ("Learn the determinants.", "Substitutes, necessity, income share, time, habit."),
    ("Say elastic or inelastic.", "And name the good."),
    ("Link to the product.", "Don't just list determinants."),
    ("Short run vs long run.", "Long run is more elastic."),
], cmds("Identify", "Explain"))
body = page(CL("2.6.3 Determinants of PED"), "Determinants of PED", "The main influences on whether demand is elastic or inelastic. Syllabus 2.6.3.",
    learn=learn, watch=watch(("Many substitutes", "stS"), ("A necessity", "stN"), ("Time and elasticity", "stT")), explore=explore,
    practise=practise(("More elastic or inelastic?", "cl1", "card"), ("Elastic or inelastic?", "cl2", "card"), ("Match the determinant", "m1", "card"), ("Order the chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("Petrol: short run and long run", "Demand is inelastic in the short run but over years drivers move to efficient or electric cars.", "Time."),
        rw("Streaming services", "With many rivals, a price rise often leads to cancellations.", "Substitutes."),
        rw("Tobacco", "Addiction keeps demand inelastic.", "Habit."),
        rw("Bread", "A cheap staple with a small share of income.", "Necessity.")),
    exam=ex, tips=tp)
write("p263", body, js, "Determinants of PED", "ig-ped-determinants")

# =========================================================== 2.6.4
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>When the price changes, the <b>amount spent by consumers</b> (consumer expenditure) and the <b>revenue earned by firms</b> change by an amount that depends on <b>PED</b>. Revenue (= consumer expenditure) = <b>price × quantity</b>. On a diagram it is the <b>area of the rectangle</b> under the price and quantity.</p></div>

  <h2>The rule</h2>
  <div class="tw"><table class="t">
    <tr><th>PED</th><th>If price rises</th><th>If price falls</th></tr>
    <tr><td><b>Inelastic (< 1)</b></td><td>Revenue <b>rises</b> (quantity falls by less than the price rises)</td><td>Revenue <b>falls</b></td></tr>
    <tr><td><b>Unitary (= 1)</b></td><td>Revenue <b>unchanged</b></td><td>Revenue <b>unchanged</b></td></tr>
    <tr><td><b>Elastic (> 1)</b></td><td>Revenue <b>falls</b> (quantity falls by more than the price rises)</td><td>Revenue <b>rises</b></td></tr>
  </table></div>

  <h2>Calculation</h2>
  <div class="formula">Revenue = price × quantity sold</div>
  <p><b>Example, elastic:</b> price $10, sells 100 (revenue $1,000). Price rises to $12 and sells 60 (revenue $720): revenue <b>falls</b>.</p>
  <p><b>Example, inelastic:</b> price $10, sells 100 ($1,000). Price rises to $12 and sells 90 ($1,080): revenue <b>rises</b>.</p>

  <h2>On a diagram</h2>
  <ul>
    <li>Revenue before: rectangle P₀ × Q₀. Revenue after: rectangle P₁ × Q₁.</li>
    <li>Compare the areas: the larger rectangle is greater revenue.</li>
  </ul>
  <p class="note">The rule links <b>PED, price change and revenue</b>. In exams, show the before and after revenue and state the relationship with PED. Consumer expenditure is the same as the firm's revenue.</p>
'''
js = HEAD + COMMON + DSJS + PEDJS + '''
function revChart(p0, q0, p1, q1) {
  let o = axes();
  o += SV.rect(X(0), Y(p0), X(q0) - X(0), Y(0) - Y(p0), "", { style: "fill:var(--accent)", opacity: 0.22 });
  o += SV.rect(X(0), Y(p1), X(q1) - X(0), Y(0) - Y(p1), "", { style: "fill:var(--warn)", opacity: 0.25 });
  o += SV.line(X(0), Y(p0), X(q0), Y(p0), "gr") + SV.line(X(q0), Y(p0), X(q0), Y(0), "gr") + SV.line(X(0), Y(p1), X(q1), Y(p1), "gr") + SV.line(X(q1), Y(p1), X(q1), Y(0), "gr");
  o += SV.circle(X(q0), Y(p0), 6, "dot1") + SV.circle(X(q1), Y(p1), 6, "dot2") + SV.text(X(0) - 8, Y(p0), "P₀", "sm bd", { "text-anchor": "end" }) + SV.text(X(0) - 8, Y(p1), "P₁", "sm bd", { "text-anchor": "end" }) + SV.text(X(q0), Y(0) + 18, "Q₀", "sm bd", { "text-anchor": "middle" }) + SV.text(X(q1), Y(0) + 18, "Q₁", "sm bd", { "text-anchor": "middle" });
  return o + SV.text(X(60), Y(104), "Blue: old revenue  ·  Orange: new revenue", "sm");
}
Lib.stepper($("#stI"), { w: 760, h: 380, label: "Price rise, inelastic demand", base: { n: 0 }, draw: (s) => s.n === 0 ? revChart(40, 60, 40, 60) : revChart(40, 60, 60, 52), steps: [
  { cap: "Price $40, quantity 60: revenue = 40 × 60 = <b>2,400</b>.", s: { n: 0 } },
  { cap: "Price rises to $60 and quantity falls only to 52: revenue = 60 × 52 = <b>3,120</b>. Revenue <b>rises</b>: demand is inelastic.", s: { n: 1 } },
] });
Lib.stepper($("#stL"), { w: 760, h: 380, label: "Price rise, elastic demand", base: { n: 0 }, draw: (s) => s.n === 0 ? revChart(40, 60, 40, 60) : revChart(40, 60, 60, 30), steps: [
  { cap: "Price $40, quantity 60: revenue = <b>2,400</b>.", s: { n: 0 } },
  { cap: "Price rises to $60 and quantity falls to 30: revenue = 60 × 30 = <b>1,800</b>. Revenue <b>falls</b>: demand is elastic.", s: { n: 1 } },
] });
const RL = ["A firm raises its price", "Demand is elastic: quantity falls by a bigger %", "Revenue falls", "Demand is inelastic: quantity falls by a smaller %", "Revenue rises"];
Lib.stepper($("#stR"), { w: 760, h: 380, label: "The rule", base: { n: 0 }, draw: mkChain(RL, "--accent"), steps: chainSteps(["A firm <b>raises its price</b>.", "If demand is <b>elastic</b>, quantity falls by a bigger %.", "<b>Revenue falls</b>.", "If demand is <b>inelastic</b>, quantity falls by a smaller %.", "<b>Revenue rises</b>."]) });

/* Lab 1 */
function labV() {
  if (!$("#va") || !$("#vb")) return;
  const dp = +$("#va").value, ped = +$("#vb").value / 10, p0 = 40, q0 = 60, p1 = p0 * (1 + dp / 100), q1 = q0 * (1 - ped * dp / 100), r0 = p0 * q0, r1 = p1 * q1, ch = r1 - r0;
  $("#va1").textContent = "$" + money(r0, 0); $("#va2").textContent = "$" + money(r1, 0); $("#va3").textContent = (ch >= 0 ? "+" : "−") + "$" + money(Math.abs(ch), 0);
  $("#vav").textContent = `PED ${money(ped, 1)} (${pedLabel(ped)}). A ${dp >= 0 ? "rise" : "fall"} of ${Math.abs(dp)}% changes price from $${p0} to $${money(p1, 0)} and quantity from ${q0} to ${money(q1, 0)}. Revenue goes from $${money(r0, 0)} to $${money(r1, 0)}: ${ch > 1 ? "it rises" : ch < -1 ? "it falls" : "it is unchanged"}. ${ped < 1 ? "Inelastic: price and revenue move together." : ped > 1 ? "Elastic: price and revenue move in opposite directions." : "Unitary: no change in revenue."}`;
  $("#labV").innerHTML = revChart(p0, q0, Math.min(100, p1), Math.max(2, q1));
}
Lib.slider($("#g1"), { id: "va", label: "Price change", min: -30, max: 30, step: 5, value: 20, fmt: (v) => (v > 0 ? "+" : "") + v + "%", onInput: labV });
Lib.slider($("#g2"), { id: "vb", label: "PED (size, ×0.1)", min: 2, max: 30, step: 1, value: 5, fmt: (v) => money(v / 10, 1), onInput: labV });
const SC = [
  { n: "Elastic demand, price rises", r: "Revenue falls", w: "Quantity falls by a bigger % than price rises." },
  { n: "Elastic demand, price falls", r: "Revenue rises", w: "Quantity rises by a bigger % than price falls." },
  { n: "Inelastic demand, price rises", r: "Revenue rises", w: "Quantity falls by a smaller % than price rises." },
  { n: "Inelastic demand, price falls", r: "Revenue falls", w: "Quantity rises by a smaller % than price falls." },
  { n: "Unitary demand, any price change", r: "Revenue unchanged", w: "Equal % changes cancel." },
];
button_table("scBtns", "scOut", SC, 0, (p) => `<div class="tw"><table class="t"><tr><th>Revenue</th><th>Why</th></tr><tr><td><b>${p.r}</b></td><td>${p.w}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "What happens to <b>revenue</b>?", buckets: [{ label: "Revenue rises" }, { label: "Revenue falls" }, { label: "Revenue unchanged" }], items: [
  { text: "Price rises, demand inelastic", b: 0 }, { text: "Price falls, demand elastic", b: 0 },
  { text: "Price rises, demand elastic", b: 1 }, { text: "Price falls, demand inelastic", b: 1 },
  { text: "Price changes, demand unitary", b: 2 },
], done: "Elastic: price and revenue move in opposite directions." });
Lib.classify($("#cl2"), { prompt: "Should the firm <b>raise</b> or <b>cut</b> its price to increase revenue?", buckets: [{ label: "Raise price" }, { label: "Cut price" }], items: [
  { text: "Demand is inelastic", b: 0 }, { text: "PED is 0.4", b: 0 }, { text: "Demand is elastic", b: 1 }, { text: "PED is 2.5", b: 1 },
], done: "Use the rule (educational, not advice)." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [
  ["Total revenue", "Price × quantity sold"],
  ["Consumer expenditure", "What consumers spend; equals firms' revenue"],
  ["Inelastic demand", "Price rise increases revenue"],
  ["Elastic demand", "Price rise decreases revenue"],
  ["Unitary demand", "Revenue unchanged by price changes"],
  ["Area of rectangle", "Revenue on a diagram"],
], done: "Learn the link." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>why a price rise reduces revenue when demand is elastic</b>.", items: [
  "The firm raises its price",
  "Consumers switch to substitutes",
  "Quantity demanded falls by a bigger percentage than the price rise",
  "Revenue (price × quantity) falls",
], done: "Elastic demand punishes price rises." });
''' + calc_js([
    ("Price $10 with 100 sold; price rises to $12 with 90 sold. By how much does revenue change ($)?", 80, "1,080 − 1,000 = <b>+$80</b>.", None, None),
    ("Price $10 with 100 sold; price rises to $12 with 60 sold. What is the new revenue ($)?", 720, "12 × 60 = <b>$720</b>.", None, None),
    ("PED is 0.5. A firm raises its price by 10%. By what percentage does revenue change (approximately, enter a whole number)?", 4, "Quantity falls 5%; revenue ≈ 1.10 × 0.95 = 1.045: about <b>+4%</b>.", None, None),
]) + mcq_js("qz1", [
    ("If demand is inelastic and a firm raises price, revenue:", ["Rises", "Falls", "Is unchanged", "Is zero"], 0, "Quantity falls by a smaller %."),
    ("If demand is elastic and a firm raises price, revenue:", ["Rises", "Falls", "Is unchanged", "Doubles"], 1, "Quantity falls by a bigger %."),
    ("Consumer expenditure equals:", ["Firms' costs", "Firms' revenue", "Firms' profit", "Taxes"], 1, "Spending = revenue."),
    ("If PED = 1 and the price rises, revenue:", ["Rises", "Falls", "Is unchanged", "Is zero"], 2, "Equal % changes."),
    ("Revenue is shown on a diagram as:", ["A point", "A line", "The area of the rectangle P × Q", "The slope"], 2, "Price × quantity."),
]) + "\n" + cards_js([("Total revenue", "Price multiplied by quantity sold."), ("Consumer expenditure", "The amount spent by consumers on a good."), ("Elastic demand", "Price rise reduces revenue."), ("Inelastic demand", "Price rise increases revenue."), ("Unitary demand", "Revenue does not change when price changes."), ("Area of rectangle", "How revenue is shown on a diagram."), ("Percentage change", "Used in PED."), ("Price rise", "Increase in price."), ("Price fall", "Decrease in price.")]) + "labV(); \n"
explore = '''
  <h2>Lab 1 · Price, PED and revenue</h2>
  <p>Change the price and the PED and see what happens to revenue (starting at $40 × 60 = $2,400).</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div></div>
    <div><div class="readout"><div><small>Old revenue</small><strong id="va1"></strong></div><div><small>New revenue</small><strong id="va2"></strong></div><div><small>Change</small><strong id="va3"></strong></div></div><div class="verdict" id="vav"></div></div></div>
    <svg id="labV" viewBox="0 0 760 340" role="img" aria-label="Revenue before and after a price change"></svg>
  </div>

  <h2>Lab 2 · The four cases</h2>
  <p>Pick a case to see the effect on revenue.</p>
  <div class="card"><div class="row" id="scBtns"></div><div id="scOut"></div></div>
'''
ex = exam(
    Q(1, "Explain", 4, "Explain how an increase in the price of milk may affect the revenue earned by milk producers. (Oct/Nov 2020, P22 style)", "Depends on PED: inelastic revenue rises; elastic falls.",
      "[K|Revenue is price multiplied by quantity sold.] [N|If demand for milk is inelastic, a rise in price causes a smaller percentage fall in quantity, so revenue rises.] [N|If demand is elastic, quantity falls by a bigger percentage, so revenue falls.]"),
    Q(2, "Calculate", 3, "Price rises from $10 to $12 and quantity falls from 100 to 90. Calculate the change in revenue and say what it shows about PED.", "Before 1,000; after 1,080; revenue rises: inelastic.", "[A|Old revenue 10 × 100 = $1,000; new revenue 12 × 90 = $1,080.] [A|Revenue rises by $80.] [N|Revenue rises when price rises, so demand is inelastic.]"),
    Q(3, "Analyse", 6, "Analyse the relationship between PED and the revenue earned by a firm when it changes its price.", "Rule for inelastic, elastic, unitary.",
      "[K|Revenue is price multiplied by quantity.] [N|If demand is inelastic, a price rise causes a smaller % fall in quantity, so revenue rises, and a price fall reduces revenue.] [N|If demand is elastic, a price rise causes a bigger % fall in quantity, so revenue falls, and a price fall raises revenue.] [N|If demand is unitary revenue does not change.] [E|The actual effect depends on how accurately the firm knows its PED.]", key=True),
    Q(4, "Discuss", 8, "Discuss whether a firm should lower its price to increase revenue.", "Depends on PED, costs, rival reactions.",
      "[K|Lowering price raises revenue only if demand is elastic, as quantity rises by a bigger percentage than the price falls.] [N|If demand is inelastic, revenue falls.] [N|The firm should also consider costs: extra output may raise total costs and lower profit.] [N|Rival firms may cut prices too, cancelling the advantage.] [E|Overall, cutting price is likely to raise revenue only for elastic goods with spare capacity, so the firm needs to know its PED and its costs first.]", key=True),
)
tp = tips([
    ("Revenue = P × Q.", "Compare before and after."),
    ("Inelastic: price and revenue same direction.", "Elastic: opposite."),
    ("Always calculate both revenues.", "Then state the change."),
    ("Link to PED.", "Say whether elastic or inelastic."),
    ("Evaluate with costs and rivals.", "Revenue is not profit."),
], cmds("Calculate", "Explain", "Analyse", "Discuss"))
body = page(CL("2.6.4 PED, consumer expenditure and firms' revenue"), "PED, Consumer Expenditure and Firms' Revenue", "How price changes affect consumer spending and firms' revenue, in diagrams and calculations. Syllabus 2.6.4.",
    learn=learn, watch=watch(("Price rise, inelastic demand", "stI"), ("Price rise, elastic demand", "stL"), ("The rule", "stR")), explore=explore,
    practise=practise(("Revenue effect?", "cl1", "card"), ("Raise or cut price?", "cl2", "card"), ("Match the term", "m1", "card"), ("Order the chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("Fuel prices", "Petrol retailers can raise prices and still keep revenue because demand is inelastic.", "Inelastic demand."),
        rw("Airline sales", "Discounted fares fill planes: demand for holidays is elastic, so revenue rises.", "Elastic demand."),
        rw("Cinema tickets", "Cheap-ticket days raise attendance and total takings.", "Elastic demand."),
        rw("Tobacco taxes", "Governments tax cigarettes knowing consumer spending will rise as quantities fall little.", "Inelastic demand.")),
    exam=ex, tips=tp)
write("p264", body, js, "PED, Consumer Expenditure and Firms' Revenue", "ig-ped-revenue")

# =========================================================== 2.6.5
learn = '''
  <div class="card big"><h3>The big idea</h3>
  <p>Knowing the PED of a good helps <b>consumers, workers, firms and governments</b> make decisions. Firms use it to set prices, governments use it to decide which goods to tax and what the effects will be, workers and unions use it to understand the effect of wage claims on jobs.</p></div>

  <h2>Implications for decision-making</h2>
  <div class="tw"><table class="t">
    <tr><th>Decision-maker</th><th>How PED matters</th></tr>
    <tr><td><b>Consumers</b></td><td>Understand which price rises they can avoid (elastic goods) and which they cannot (inelastic necessities); a rise in the price of an inelastic good takes a larger share of spending</td></tr>
    <tr><td><b>Workers</b></td><td>If demand for the product (and so for labour) is inelastic, unions can push for higher wages without large job losses; if elastic, higher wages raise costs and prices and may cost jobs</td></tr>
    <tr><td><b>Producers (firms)</b></td><td>Inelastic: raising price increases revenue; elastic: cutting price increases revenue. Also affects pricing strategies, discounts and promotions, and responses to higher costs</td></tr>
    <tr><td><b>Governments</b></td><td>Taxes on <b>inelastic</b> goods (cigarettes, alcohol, petrol) raise lots of revenue because quantity falls little, but are less effective at reducing consumption; taxes on elastic goods reduce consumption more but raise less</td></tr>
  </table></div>

  <h2>Examples</h2>
  <ul>
    <li><b>Tax on cigarettes:</b> demand is inelastic so tax revenue is high, but consumption falls only a little.</li>
    <li><b>Price discrimination:</b> airlines charge business travellers (inelastic) more than leisure travellers (elastic).</li>
    <li><b>A sale:</b> shops cut prices on goods with elastic demand to raise revenue.</li>
    <li><b>Subsidies and minimum prices</b> have different effects depending on PED.</li>
  </ul>
  <p class="note">PED is a <b>tool</b>: its value helps predict outcomes. Estimates may be unreliable and PED can change over time, so effects are uncertain.</p>
'''
js = HEAD + COMMON + DSJS + PEDJS + '''
const GV = ["The government taxes cigarettes (inelastic demand)", "The price rises", "Quantity demanded falls only slightly", "Tax revenue is high but consumption barely falls", "The tax raises revenue more than it reduces smoking"];
Lib.stepper($("#stG"), { w: 760, h: 380, label: "Taxing an inelastic good", base: { n: 0 }, draw: mkChain(GV, "--bad"), steps: chainSteps(["The government <b>taxes cigarettes</b> (inelastic demand).", "The <b>price rises</b>.", "Quantity demanded falls only <b>slightly</b>.", "<b>Tax revenue is high</b> but consumption barely falls.", "The tax <b>raises revenue</b> more than it reduces smoking."]) });
const FM = ["A firm sells an elastic good", "It cuts its price", "Quantity sold rises by a bigger %", "Revenue rises", "Cutting price is a sensible strategy (if costs allow)"];
Lib.stepper($("#stF"), { w: 760, h: 380, label: "A firm's pricing", base: { n: 0 }, draw: mkChain(FM, "--good"), steps: chainSteps(["A firm sells an <b>elastic</b> good.", "It <b>cuts its price</b>.", "Quantity sold rises by a <b>bigger %</b>.", "<b>Revenue rises</b>.", "Cutting price can work (if costs allow)."]) });
const WK = ["Workers' union demands a pay rise", "Firm's costs rise; it raises the product price", "Demand for the product is elastic: sales fall a lot", "Firm needs fewer workers", "Jobs may be lost"];
Lib.stepper($("#stW"), { w: 760, h: 380, label: "Workers and PED", base: { n: 0 }, draw: mkChain(WK, "--warn"), steps: chainSteps(["A union demands a <b>pay rise</b>.", "The firm's <b>costs rise</b>; it raises the price.", "If demand is <b>elastic</b>, sales fall a lot.", "The firm needs <b>fewer workers</b>.", "<b>Jobs may be lost</b>."]) });

/* Lab 1: tax revenue */
function labT() {
  if (!$("#ta") || !$("#tb")) return;
  const tax = +$("#ta").value, ped = +$("#tb").value / 10, p0 = 10, q0 = 100, p1 = p0 + tax, q1 = q0 * (1 - ped * (tax / p0)), rev = tax * q1, drop = q0 - q1;
  $("#ta1").textContent = money(Math.max(0, q1), 0); $("#ta2").textContent = "$" + money(Math.max(0, rev), 0); $("#ta3").textContent = money((drop / q0) * 100, 0) + "%";
  $("#tav").textContent = `A $${tax} tax raises the price from $10 to $${p1} (+${money((tax / p0) * 100, 0)}%). With PED ${money(ped, 1)} (${pedLabel(ped)}), quantity falls from 100 to ${money(Math.max(0, q1), 0)} (${money((drop / q0) * 100, 0)}% fall). Tax revenue is $${tax} × ${money(Math.max(0, q1), 0)} = $${money(Math.max(0, rev), 0)}. ${ped < 1 ? "Inelastic: high revenue, small fall in consumption." : "Elastic: large fall in consumption, lower revenue."}`;
  const base = 290; let o = SV.line(60, base, 700, base);
  [["Quantity before", 100, "--accent"], ["Quantity after", Math.max(0, q1), "--warn"], ["Tax revenue", Math.max(0, rev) / 5, "--good"]].forEach(([n, v, c], i) => { const x = 110 + i * 190, h = v * 2; o += SV.rect(x, base - h, 120, h, "", { style: `fill:var(${c})`, opacity: 0.85 }) + SV.text(x + 60, base - h - 8, i === 2 ? "$" + money(Math.max(0, rev), 0) : money(v, 0), "lbl bd", { "text-anchor": "middle" }) + SV.text(x + 60, base + 20, n, "sm", { "text-anchor": "middle" }); });
  $("#labT").innerHTML = o;
}
Lib.slider($("#g1"), { id: "ta", label: "Tax per unit (price starts at $10)", min: 1, max: 5, step: 1, value: 2, fmt: (v) => "$" + v, onInput: labT });
Lib.slider($("#g2"), { id: "tb", label: "PED (size, ×0.1)", min: 2, max: 25, step: 1, value: 4, fmt: (v) => money(v / 10, 1), onInput: labT });
const DM = [
  { n: "Consumers", d: "Know which goods they can avoid buying when prices rise." },
  { n: "Workers", d: "Pay claims are more affordable when product demand is inelastic." },
  { n: "Firms", d: "Choose price rises or cuts to raise revenue." },
  { n: "Government", d: "Taxes on inelastic goods raise revenue; on elastic goods cut consumption." },
];
button_table("dmBtns", "dmOut", DM, 0, (p) => `<div class="tw"><table class="t"><tr><th>How PED helps</th></tr><tr><td>${p.d}</td></tr></table></div>`);

/* ================= PRACTISE ================= */
Lib.classify($("#cl1"), { prompt: "Which <b>decision-maker</b> uses PED this way?", buckets: [{ label: "Firm" }, { label: "Government" }, { label: "Worker/union" }, { label: "Consumer" }], items: [
  { text: "Cutting prices on an elastic good to raise revenue", b: 0 }, { text: "Charging more for an inelastic good", b: 0 },
  { text: "Taxing cigarettes to raise revenue", b: 1 }, { text: "Choosing which goods to tax", b: 1 },
  { text: "Asking for higher pay when demand for the product is inelastic", b: 2 },
  { text: "Switching away from a dearer elastic good", b: 3 },
], done: "PED guides decisions." });
Lib.classify($("#cl2"), { prompt: "Is each tax <b>good at raising revenue</b> or <b>good at cutting consumption</b>?", buckets: [{ label: "Raises revenue" }, { label: "Cuts consumption" }], items: [
  { text: "A tax on an inelastic good", b: 0 }, { text: "A tax on cigarettes", b: 0 }, { text: "A tax on an elastic good", b: 1 }, { text: "A tax on a luxury with many substitutes", b: 1 },
], done: "Inelastic: revenue. Elastic: consumption." });
Lib.match($("#m1"), { prompt: "Match the situation to the implication.", pairs: [
  ["Inelastic demand, firm raises price", "Revenue rises"],
  ["Elastic demand, firm cuts price", "Revenue rises"],
  ["Tax on inelastic good", "High revenue, small fall in consumption"],
  ["Tax on elastic good", "Large fall in consumption"],
  ["Inelastic product demand", "Union pay claims cost fewer jobs"],
  ["Price discrimination", "Charge more where demand is inelastic"],
], done: "Link PED to decisions." });
Lib.order($("#o1"), { prompt: "Put the chain in order: <b>why a tax on cigarettes raises a lot of revenue</b>.", items: [
  "The government taxes cigarettes",
  "The price rises",
  "Demand is inelastic so quantity falls only a little",
  "Many units are still sold",
  "Tax revenue is high",
], done: "Inelastic goods are good revenue-raisers." });
''' + calc_js([
    ("A $2 tax is placed on each unit. 80 units are still sold. What is the tax revenue ($)?", 160, "2 × 80 = <b>$160</b>.", None, None),
    ("PED is 0.4 and a tax raises the price by 25%. By what percentage does quantity demanded fall?", 10, "0.4 × 25 = <b>10%</b>.", None, None),
]) + mcq_js("qz1", [
    ("Governments tax goods with inelastic demand because:", ["Revenue stays high", "Consumption falls a lot", "They are luxuries", "Prices fall"], 0, "Quantity falls little."),
    ("A firm with inelastic demand that wants more revenue should:", ["Cut price", "Raise price", "Do nothing", "Stop selling"], 1, "Revenue rises with price."),
    ("Workers can seek pay rises more safely when product demand is:", ["Elastic", "Inelastic", "Zero", "Falling"], 1, "Higher prices will not cut sales much."),
    ("A tax is most effective at cutting consumption when demand is:", ["Inelastic", "Elastic", "Zero", "Unitary only"], 1, "Quantity responds."),
    ("Which good is the best source of tax revenue?", ["A brand of chocolate", "Cigarettes", "Holidays", "Restaurant meals"], 1, "Inelastic demand."),
]) + "\n" + cards_js([("Indirect tax", "A tax on goods and services."), ("Price discrimination", "Charging different prices to different groups for the same good."), ("Pay claim", "A request by workers for higher wages."), ("Tax revenue", "Money raised by taxes."), ("Consumption", "The quantity of a good consumed."), ("Strategy", "A plan to achieve an aim."), ("Promotion", "A temporary price cut or offer."), ("Short-run", "A period too short to adjust."), ("Reliability", "How far PED estimates can be trusted.")]) + "labT(); \n"
explore = '''
  <h2>Lab 1 · Taxing a good</h2>
  <p>Put a tax on a good that costs $10 and sells 100 units. Choose the PED and see revenue and the fall in consumption.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div><div id="g2"></div></div>
    <div><div class="readout"><div><small>Quantity after tax</small><strong id="ta1"></strong></div><div><small>Tax revenue</small><strong id="ta2"></strong></div><div><small>Fall in consumption</small><strong id="ta3"></strong></div></div><div class="verdict" id="tav"></div></div></div>
    <svg id="labT" viewBox="0 0 760 330" role="img" aria-label="Effect of a tax"></svg>
  </div>

  <h2>Lab 2 · Who uses PED?</h2>
  <p>Pick a decision-maker to see how PED helps them.</p>
  <div class="card"><div class="row" id="dmBtns"></div><div id="dmOut"></div></div>
'''
ex = exam(
    Q(1, "Explain", 4, "Explain why a government might tax goods with inelastic demand.", "High revenue; small fall in quantity.",
      "[K|Demand for goods such as cigarettes is inelastic.] [N|A tax raises the price, but quantity demanded falls by a smaller percentage,] [N|so many units are still sold and the government raises a lot of tax revenue.]"),
    Q(2, "Explain", 4, "Explain how knowledge of PED could help a firm decide whether to raise its prices.", "Inelastic: raise; elastic: don't.",
      "[K|If demand for its product is inelastic, a price rise will cause a smaller percentage fall in quantity,] [N|so revenue will rise and the firm could raise prices.] [K|If demand is elastic, a price rise will cause a bigger fall in quantity,] [N|so revenue will fall and the firm should not raise prices.]"),
    Q(3, "Analyse", 6, "Analyse how PED may influence the demands of workers for higher pay.", "Product demand inelastic: safe to ask; elastic: jobs lost.",
      "[K|If demand for the firm's product is inelastic, a rise in costs from higher pay can be passed on in higher prices.] [N|Sales will fall only a little, so job losses are small and workers can ask for more.] [N|If demand is elastic, higher prices cause a big fall in sales, so the firm may cut jobs.] [E|Workers may therefore ask for smaller rises in elastic markets.]", key=True),
    Q(4, "Discuss", 8, "Discuss whether a government should rely on taxing inelastic goods to raise revenue and reduce consumption.", "Revenue high; consumption falls little; regressive; alternatives.",
      "[K|Taxing inelastic goods such as cigarettes raises a lot of revenue because quantity falls little.] [N|It also raises prices, which discourages some consumption, though the fall is small.] [N|However, the tax may be regressive: poorer households spend a larger share of income on it.] [N|Illegal markets may grow if prices are high.] [E|Overall, it is an effective revenue source but a limited way of cutting consumption, so the government may need other measures such as education.]", key=True),
)
tp = tips([
    ("Learn the four decision-makers.", "Consumers, workers, firms, government."),
    ("Inelastic: tax for revenue.", "Elastic: tax to reduce consumption."),
    ("Link to the context.", "Cigarettes, petrol, holidays."),
    ("Evaluate.", "Regressive taxes; reliability of PED; time."),
], cmds("Explain", "Analyse", "Discuss"))
body = page(CL("2.6.5 Significance of PED"), "Significance of PED", "How knowledge of PED influences decisions by consumers, workers, firms and governments. Syllabus 2.6.5.",
    learn=learn, watch=watch(("Taxing an inelastic good", "stG"), ("A firm's pricing", "stF"), ("Workers and PED", "stW")), explore=explore,
    practise=practise(("Who uses PED?", "cl1", "card"), ("Revenue or consumption?", "cl2", "card"), ("Match the situation", "m1", "card"), ("Order the chain", "o1", "card"), ("Calculations", "c1", ""), ("Multiple choice", "qz1", "")),
    real=real(
        rw("Tobacco and alcohol taxes", "Governments raise large sums because demand is inelastic.", "Government decisions."),
        rw("Airline pricing", "Last-minute business fares are higher than advance leisure fares.", "Firms and price discrimination."),
        rw("Supermarket promotions", "Offers on branded goods with many substitutes boost sales.", "Elastic demand."),
        rw("Sugar taxes", "Governments tax sugary drinks to cut consumption, helped by many substitutes.", "A more elastic good.")),
    exam=ex, tips=tp)
write("p265", body, js, "Significance of PED", "ig-ped-significance")
