"""8.1.4 Use of operators."""
from p814k import *

PR_PS = ["Result ← (4 + 2) * 3 ^ 2", "OUTPUT Result"]
PR_PY = ["result = (4 + 2) * 3 ** 2", "print(result)"]
DM_PS = ["INPUT Minutes", "Hours ← Minutes DIV 60", "Remainder ← Minutes MOD 60", 'OUTPUT Hours, " h ", Remainder, " min"']
DM_PY = ["minutes = int(input())", "hours = minutes // 60", "remainder = minutes % 60", 'print(hours, "h", remainder, "min")']
LG_PS = ["INPUT Age", "INPUT Height", "IF Age >= 8 AND Height >= 120", "  THEN", '    OUTPUT "Allowed"', "  ELSE", '    OUTPUT "Not allowed"', "ENDIF"]
LG_PY = ["age = int(input())", "height = int(input())", "if age >= 8 and height >= 120:", '    print("Allowed")', "else:", '    print("Not allowed")']


def anim_pr():
    r = R(["Result"])
    r.f("Brackets, then powers, then * and /, then + and -. The expression is <b>(4 + 2) * 3 ^ 2</b>.", [0], [0], note="(4 + 2) * 3 ^ 2", nc="t4")
    r.f("<b>1. Brackets first:</b> 4 + 2 = 6.", [0], [0], note="6 * 3 ^ 2", nc="t4")
    r.f("<b>2. Power next:</b> 3 ^ 2 = 9. The power binds tighter than *.", [0], [0], note="6 * 9", nc="t4")
    r.v["Result"] = 54; r.f("<b>3. Multiply:</b> 6 * 9 = 54. It is stored in Result.", [0], [0], hl=["Result"], note="54", nc="t3")
    r.out.append("54"); r.f("<b>OUTPUT Result</b>: 54. Without the brackets the answer would have been 4 + 2 * 9 = 22.", [1], [1], hl=["Result"])
    return r.js()


def anim_dm():
    r = R(["Minutes", "Hours", "Remainder"])
    r.f("Convert minutes into hours and minutes. The user will type 135.", [0], [], inp=[135])
    r.v["Minutes"] = 135; r.f("<b>INPUT Minutes</b>: 135.", [0], [0], hl=["Minutes"], inp=[])
    r.v["Hours"] = 2; r.f("<b>135 DIV 60</b> = 2. DIV gives the <b>whole number</b> of times 60 goes into 135 (2 × 60 = 120).", [1], [1], hl=["Hours"], note="135 DIV 60 = 2", nc="t4")
    r.v["Remainder"] = 15; r.f("<b>135 MOD 60</b> = 15. MOD gives the <b>remainder</b>: 135 − 120 = 15.", [2], [2], hl=["Remainder"], note="135 MOD 60 = 15", nc="t4")
    r.out.append("2 h 15 min"); r.f("<b>OUTPUT</b> joins the pieces: 2 h 15 min. DIV and MOD together split a quantity into units.", [3], [3])
    return r.js()


def anim_lg():
    r = R(["Age", "Height"])
    r.f("A ride needs age 8 or over <b>and</b> height 120 or over. The user types 10, then 115.", [0], [], inp=[10, 115])
    r.v["Age"] = 10; r.f("<b>INPUT Age</b>: 10.", [0], [0], hl=["Age"], inp=[115])
    r.v["Height"] = 115; r.f("<b>INPUT Height</b>: 115.", [1], [1], hl=["Height"], inp=[])
    r.f("Left side of AND: is 10 >= 8?", [2], [2], cond=("10 >= 8", True))
    r.f("Right side of AND: is 115 >= 120?", [2], [2], cond=("115 >= 120", False))
    r.f("<b>AND</b> needs <b>both</b> sides TRUE. TRUE AND FALSE is FALSE.", [2], [2], cond=("TRUE AND FALSE", False))
    r.out.append("Not allowed"); r.f("FALSE, so the ELSE branch runs. If it had been <b>OR</b>, TRUE OR FALSE would be TRUE and the rider would be allowed.", [5, 6], [4, 5], cond=("TRUE AND FALSE", False))
    return r.js()


learn = '''
  <h2>8.1.4 Use of operators</h2>
  <p>An <span class="kw">operator</span> is a symbol or word that <b>does something to values</b>. There are three groups: <b>arithmetic</b> (calculate), <b>comparison</b> (compare, giving TRUE or FALSE) and <b>logical</b> (combine TRUE/FALSE results). You have already used many of them. This page puts them together.</p>

  <h3>Arithmetic operators</h3>
  <div class="tw"><table class="t">
    <tr><th>Operation</th><th>Pseudocode</th><th>Python</th><th>Example</th><th>Result</th></tr>
    <tr><td>add / subtract</td><td>+  -</td><td>+  -</td><td>7 + 3</td><td>10</td></tr>
    <tr><td>multiply</td><td>*</td><td>*</td><td>7 * 3</td><td>21</td></tr>
    <tr><td>divide</td><td>/</td><td>/</td><td>7 / 2</td><td>3.5</td></tr>
    <tr><td>power</td><td>^</td><td>**</td><td>2 ^ 3</td><td>8</td></tr>
    <tr><td>whole-number division</td><td>DIV</td><td>//</td><td>17 DIV 5</td><td>3</td></tr>
    <tr><td>remainder</td><td>MOD</td><td>%</td><td>17 MOD 5</td><td>2</td></tr>
  </table></div>
  <div class="tip"><b class="h">DIV and MOD together</b>17 divided by 5 is <b>3 remainder 2</b>. DIV gives the 3 and MOD gives the 2. (Some books write them as functions, <code>DIV(17, 5)</code> and <code>MOD(17, 5)</code>.) Useful jobs: <b>X MOD 2 = 0</b> tests for an even number. <b>X MOD 10</b> gives the last digit. <b>Minutes DIV 60</b> and <b>Minutes MOD 60</b> turn minutes into hours and minutes.</div>

  <h3>Order of operations</h3>
  <p>The computer works out brackets first, then <b>^</b>, then <b>* and /</b> (left to right), then <b>+ and -</b>. Use <b>brackets</b> to force the order you want.</p>
  <div id="cdPr" class="code"></div>

  <h3>Comparison operators</h3>
  <p>These compare two values and give <b>TRUE or FALSE</b>. They are the tests inside IF, WHILE and UNTIL.</p>
  <div class="tw"><table class="t">
    <tr><th>Meaning</th><th>Pseudocode</th><th>Python</th><th>Example (A = 5)</th></tr>
    <tr><td>equal to</td><td>=</td><td>==</td><td>A = 5 is TRUE</td></tr>
    <tr><td>not equal to</td><td>&lt;&gt;</td><td>!=</td><td>A &lt;&gt; 5 is FALSE</td></tr>
    <tr><td>less than / greater than</td><td>&lt;   &gt;</td><td>&lt;   &gt;</td><td>A &gt; 7 is FALSE</td></tr>
    <tr><td>less than or equal / greater than or equal</td><td>&lt;=   &gt;=</td><td>&lt;=   &gt;=</td><td>A &gt;= 5 is TRUE</td></tr>
  </table></div>
  <div class="warn"><b class="h">← is not =</b>In pseudocode, <b>←</b> stores a value (<code>Total ← 5</code>) and <b>=</b> compares (<code>IF Total = 5</code>). In Python, <b>=</b> stores and <b>==</b> compares.</div>

  <h3>Logical operators</h3>
  <p><b>AND</b>, <b>OR</b> and <b>NOT</b> combine tests. <b>Each side must be a full condition.</b> Write <code>Age &gt;= 13 AND Age &lt;= 19</code>, <b>not</b> <code>Age &gt;= 13 AND &lt;= 19</code>.</p>
  <div class="tw"><table class="t">
    <tr><th>P</th><th>Q</th><th>P AND Q</th><th>P OR Q</th><th>NOT P</th></tr>
    <tr><td>TRUE</td><td>TRUE</td><td>TRUE</td><td>TRUE</td><td>FALSE</td></tr>
    <tr><td>TRUE</td><td>FALSE</td><td>FALSE</td><td>TRUE</td><td>FALSE</td></tr>
    <tr><td>FALSE</td><td>TRUE</td><td>FALSE</td><td>TRUE</td><td>TRUE</td></tr>
    <tr><td>FALSE</td><td>FALSE</td><td>FALSE</td><td>FALSE</td><td>TRUE</td></tr>
  </table></div>
  <ul>
    <li><b>AND</b>: TRUE only when <b>both</b> sides are TRUE.</li>
    <li><b>OR</b>: TRUE when <b>at least one</b> side is TRUE.</li>
    <li><b>NOT</b>: <b>reverses</b> TRUE and FALSE.</li>
  </ul>
  <div id="cdLg" class="code"></div>
  <p>One more operator you have met: <b>&amp;</b> joins strings (concatenation).</p>
'''

watch = '''  <h2>1 · Order of operations</h2><div id="aP"></div>
  <h2>2 · DIV and MOD</h2><div id="aD"></div>
  <h2>3 · AND in a condition</h2><div id="aL"></div>
'''

explore = '''  <h2>Lab 1 · Arithmetic operators</h2>
  <p>Move the sliders and compare the results. Set A to 17 and B to 5, then try a B that does not divide A exactly.</p>
  <div class="card"><div id="s1"></div><div id="s2"></div><div class="tw"><table class="t mono" id="at"></table></div><div class="verdict" id="av" aria-live="polite"></div></div>

  <h2>Lab 2 · AND, OR and NOT</h2>
  <p>A ride needs <b>Age &gt;= 8</b> and <b>Height &gt;= 120</b>. Choose how they are combined.</p>
  <div class="card"><div id="s3"></div><div id="s4"></div><div class="row"><label for="lo">Combine with&nbsp;</label><select class="sel" id="lo"><option value="AND">Age >= 8 AND Height >= 120</option><option value="OR">Age >= 8 OR Height >= 120</option><option value="NOT">NOT (Age >= 8)</option></select></div><div class="tw"><table class="t mono" id="lt"></table></div><div class="verdict" id="lv" aria-live="polite"></div></div>

  <h2>Lab 3 · Does the order matter?</h2>
  <p>Pick an expression and see how it is worked out, step by step.</p>
  <div class="card"><div class="row"><label for="pe">Expression&nbsp;</label><select class="sel" id="pe"></select></div><div class="out" id="pout" style="font-size:1rem;letter-spacing:.02em"></div><div class="verdict" id="pv" aria-live="polite"></div></div>
'''

practise = '''  <h2>1 · Which type of operator?</h2>
  <div id="cl1" class="card"></div>
  <h2>2 · Match the operator to its meaning</h2>
  <div id="m1" class="card"></div>
  <h2>3 · Calculations</h2>
  <p class="note">For TRUE or FALSE answers, type the word.</p>
  <div id="c1"></div>
  <h2>4 · Multiple choice</h2>
  <div id="qz1"></div>
'''

real = (rw("A clock", "Converting 135 minutes into hours and minutes uses DIV and MOD. A 24-hour clock wraps around using MOD 24.", "DIV gives whole units, MOD gives what is left over.")
        + rw("A funfair ride", "A rider must be tall enough <b>and</b> old enough. A child may ride if they are with an adult <b>or</b> are tall enough.", "AND needs both conditions TRUE. OR needs only one.")
        + rw("Odd and even", "A game gives bonus points on even-numbered levels. The program tests <code>Level MOD 2 = 0</code>.", "MOD 2 = 0 means even; MOD 2 = 1 means odd.")
        + rw("Bank interest", "Interest is worked out with a power: the balance multiplied by 1.05 for each year, which is 1.05 ^ Years.", "^ is used for powers; use brackets to control the order.")
        )

ex = [
    eq(1, "State", 2, "State what the operators <b>DIV</b> and <b>MOD</b> do.", "Give an example for each, using 17 and 5.",
       mk(1, "DIV: gives the whole number part of a division (for example 17 DIV 5 = 3)") + " " + mk(2, "MOD: gives the remainder of a division (for example 17 MOD 5 = 2)."),
       "Mixing them up, or saying DIV is the same as /. 17 / 5 is 3.4."),
    eq(2, "Give", 5, "Give the result of each expression. (a) 17 DIV 5 (b) 17 MOD 5 (c) 2 ^ 3 (d) 12 - 2 * 3 (e) (12 - 2) * 3", "Brackets, powers, * and /, then + and -.",
       mk(1, "(a) 3") + " " + mk(2, "(b) 2") + " " + mk(3, "(c) 8") + " " + mk(4, "(d) 6") + " " + mk(5, "(e) 30"),
       "Answering (d) with 20. Multiplication happens before subtraction."),
    eq(3, "State", 3, "State the type of each operator. (a) * (b) &lt;&gt; (c) OR", "Calculate, compare or combine?",
       mk(1, "(a) arithmetic") + " " + mk(2, "(b) comparison (relational)") + " " + mk(3, "(c) logical (Boolean)"),
       "Calling &lt;&gt; arithmetic. It compares and gives TRUE or FALSE."),
    eq(4, "Write", 4, "A teenager is aged 13 to 19 inclusive. Write pseudocode to input an age and output \"Teenager\" if the person is a teenager, otherwise \"Not a teenager\".", "Two tests joined by AND, and each side is a full condition.",
       mk(1, "INPUT Age") + " " + mk(2, "IF Age >= 13 AND Age <= 19") + " " + mk(3, "THEN OUTPUT \"Teenager\"") + " " + mk(4, "ELSE OUTPUT \"Not a teenager\" and ENDIF")
       + ac(["INPUT Age", "IF Age >= 13 AND Age <= 19", "  THEN", '    OUTPUT "Teenager"', "  ELSE", '    OUTPUT "Not a teenager"', "ENDIF"]),
       "Using OR. With OR, every age would be TRUE."),
    eq(5, "Identify", 2, "Identify the error in this condition and write it correctly: <code>IF Age &gt;= 13 AND &lt;= 19</code>", "What must be on each side of AND?",
       mk(1, "Each side of AND must be a complete condition (the second part is missing Age)") + " " + mk(2, "IF Age >= 13 AND Age <= 19"),
       "Saying AND should be OR. AND is correct here."),
    eq(6, "Write", 4, "Write pseudocode to input a number of seconds and output the equivalent number of whole minutes and the seconds left over.", "DIV for the minutes, MOD for the remainder.",
       mk(1, "INPUT Seconds") + " " + mk(2, "Minutes ← Seconds DIV 60") + " " + mk(3, "Left ← Seconds MOD 60") + " " + mk(4, "OUTPUT Minutes and Left")
       + ac(["INPUT Seconds", "Minutes ← Seconds DIV 60", "Left ← Seconds MOD 60", "OUTPUT Minutes, Left"]),
       "Using / for the minutes, which gives a decimal such as 2.25 rather than 2."),
    eq(7, "Complete", 4, "Complete the truth table for <code>(P OR Q) AND NOT P</code>.", "Work out P OR Q and NOT P first, then combine them with AND.",
       mk(1, "P = TRUE, Q = TRUE: FALSE") + " " + mk(2, "P = TRUE, Q = FALSE: FALSE") + " " + mk(3, "P = FALSE, Q = TRUE: TRUE") + " " + mk(4, "P = FALSE, Q = FALSE: FALSE"),
       "Getting the last row TRUE. P OR Q is FALSE there, so the AND is FALSE."),
    eq(8, "Write", 6, "Write pseudocode to input 20 whole numbers and output how many of them are even.", "A loop, a counter and MOD 2.",
       mk(1, "Count ← 0 before the loop") + " " + mk(2, "FOR Index ← 1 TO 20 with INPUT Number inside") + " " + mk(3, "IF Number MOD 2 = 0") + " " + mk(4, "THEN Count ← Count + 1 ... ENDIF") + " " + mk(5, "NEXT Index") + " " + mk(6, "OUTPUT Count after the loop")
       + ac(["Count ← 0", "FOR Index ← 1 TO 20", "    INPUT Number", "    IF Number MOD 2 = 0", "      THEN", "        Count ← Count + 1", "    ENDIF", "NEXT Index", "OUTPUT Count"]),
       "Writing Number DIV 2 = 0, which is only TRUE for 0 and 1."),
    eq(9, "Write", 7, "Write pseudocode to input 10 marks. Output the average of all the marks and how many of the marks are between 40 and 70 inclusive.", "Totalling and counting in one loop, with AND for the range.",
       mk(1, "Total ← 0 and Count ← 0 before the loop") + " " + mk(2, "FOR Index ← 1 TO 10 with INPUT Mark inside") + " " + mk(3, "Total ← Total + Mark") + " " + mk(4, "IF Mark >= 40 AND Mark <= 70") + " " + mk(5, "THEN Count ← Count + 1 ... ENDIF") + " " + mk(6, "Average ← Total / 10 after the loop") + " " + mk(7, "OUTPUT Average and OUTPUT Count")
       + ac(["Total ← 0", "Count ← 0", "FOR Index ← 1 TO 10", "    INPUT Mark", "    Total ← Total + Mark", "    IF Mark >= 40 AND Mark <= 70", "      THEN", "        Count ← Count + 1", "    ENDIF", "NEXT Index", "Average ← Total / 10", "OUTPUT Average", "OUTPUT Count"]),
       "Working out the average inside the loop, before all the marks have been added."),
]
exam = "".join(ex)

tipshtml = tips([
    "<b>DIV is the whole number, MOD is the remainder.</b> 17 DIV 5 = 3 and 17 MOD 5 = 2.",
    "<b>X MOD 2 = 0 means X is even.</b>",
    "<b>Order: brackets, ^, * and /, then + and -.</b> Add brackets when unsure.",
    "<b>Each side of AND or OR is a full condition.</b> Age >= 13 AND Age <= 19.",
    "<b>AND needs both TRUE. OR needs at least one TRUE.</b> NOT reverses.",
    "<b>In pseudocode ← stores and = compares.</b> In Python = stores and == compares.",
])

page("8.1.4 · Use of operators", "Use of Operators", "Arithmetic, comparison and logical operators, including DIV, MOD and AND/OR/NOT.",
     "<span class=\"kw\">Operators</span> work on values. <b>Arithmetic</b> operators calculate, <b>comparison</b> operators give TRUE or FALSE, and <b>logical</b> operators (AND, OR, NOT) combine those results.",
     learn, watch, explore, practise, real, exam, tipshtml, "p814f")

js = []
js.append(f'''
const PR_PS = {json.dumps(PR_PS, ensure_ascii=False)}, PR_PY = {json.dumps(PR_PY, ensure_ascii=False)};
const DM_PS = {json.dumps(DM_PS, ensure_ascii=False)}, DM_PY = {json.dumps(DM_PY, ensure_ascii=False)};
const LG_PS = {json.dumps(LG_PS, ensure_ascii=False)}, LG_PY = {json.dumps(LG_PY, ensure_ascii=False)};
tr($("#aP"), {{ label: "Order of operations", title: "Order of operations", pseudo: PR_PS, py: PR_PY, dwell: 2300, frames: {anim_pr()} }});
tr($("#aD"), {{ label: "DIV and MOD", title: "Minutes to hours and minutes", pseudo: DM_PS, py: DM_PY, dwell: 2300, frames: {anim_dm()} }});
tr($("#aL"), {{ label: "AND in a condition", title: "Ride check", pseudo: LG_PS, py: LG_PY, dwell: 2300, frames: {anim_lg()} }});
Lib.codePanel($("#cdPr"), {{ pseudo: PR_PS, py: PR_PY }});
Lib.codePanel($("#cdLg"), {{ pseudo: LG_PS, py: LG_PY }});
''')

js.append(r'''
/* ---------- Lab 1 ---------- */
(() => {
  let a, b;
  const upd = () => {
    if (!a || !b) return; const x = a.get(), y = b.get(), d = Math.floor(x / y), m = x % y;
    $("#at").innerHTML = `<tr><th>Pseudocode</th><th>Python</th><th>Result</th></tr><tr><td>A + B</td><td>a + b</td><td>${x + y}</td></tr><tr><td>A - B</td><td>a - b</td><td>${x - y}</td></tr><tr><td>A * B</td><td>a * b</td><td>${x * y}</td></tr><tr><td>A / B</td><td>a / b</td><td>${fmtN(x / y, 3)}</td></tr><tr><td>A ^ 2</td><td>a ** 2</td><td>${x * x}</td></tr><tr><td>A DIV B</td><td>a // b</td><td>${d}</td></tr><tr><td>A MOD B</td><td>a % b</td><td>${m}</td></tr>`;
    $("#av").innerHTML = `${x} ÷ ${y} is <b>${d} remainder ${m}</b>: ${x} DIV ${y} = ${d} and ${x} MOD ${y} = ${m}. Check: ${d} × ${y} + ${m} = ${d * y + m}.${m === 0 ? ` MOD is 0, so ${y} divides ${x} exactly.` : ""}`;
  };
  a = Lib.slider($("#s1"), { id: "oa", label: "A ", min: 0, max: 30, value: 17, onInput: upd });
  b = Lib.slider($("#s2"), { id: "ob", label: "B ", min: 1, max: 10, value: 5, onInput: upd });
  upd();
})();

/* ---------- Lab 2 ---------- */
(() => {
  let a, h; const sel = $("#lo");
  const upd = () => {
    if (!a || !h) return; const ag = a.get(), ht = h.get(), p = ag >= 8, q = ht >= 120, o = sel.value;
    const T = (v) => (v ? "TRUE" : "FALSE"), r = o === "AND" ? p && q : o === "OR" ? p || q : !p;
    $("#lt").innerHTML = `<tr><th>Part</th><th>Value</th></tr><tr><td>Age >= 8  (${ag} >= 8)</td><td>${T(p)}</td></tr>` + (o === "NOT" ? "" : `<tr><td>Height >= 120  (${ht} >= 120)</td><td>${T(q)}</td></tr>`) + `<tr><td><b>${o === "NOT" ? "NOT (Age >= 8)" : "Age >= 8 " + o + " Height >= 120"}</b></td><td><b>${T(r)}</b></td></tr>`;
    $("#lv").innerHTML = o === "AND" ? (r ? "Both tests are TRUE, so AND is TRUE." : `AND needs <b>both</b> TRUE. ${!p && !q ? "Neither is" : !p ? "Age is not" : "Height is not"} TRUE.`) : o === "OR" ? (r ? "At least one test is TRUE, so OR is TRUE." : "Neither test is TRUE, so OR is FALSE.") : `NOT reverses ${T(p)} to ${T(!p)}.`;
  };
  a = Lib.slider($("#s3"), { id: "la", label: "Age ", min: 0, max: 30, value: 10, onInput: upd });
  h = Lib.slider($("#s4"), { id: "lh", label: "Height (cm) ", min: 80, max: 200, value: 115, onInput: upd });
  sel.onchange = upd; upd();
})();

/* ---------- Lab 3 ---------- */
(() => {
  const E = [["12 - 2 * 3", "12 - 6", 6, "* happens before -."], ["(12 - 2) * 3", "10 * 3", 30, "The brackets make the subtraction happen first."], ["2 + 3 ^ 2", "2 + 9", 11, "^ happens before +."], ["(2 + 3) ^ 2", "5 ^ 2", 25, "Brackets first, then the power."], ["20 / 4 + 1", "5 + 1", 6, "/ happens before +."], ["20 / (4 + 1)", "20 / 5", 4, "Brackets first."]];
  const sel = $("#pe"); sel.innerHTML = E.map((e, i) => `<option value="${i}">${e[0]}</option>`).join("");
  const upd = () => { const e = E[+sel.value]; $("#pout").innerHTML = `${esc(e[0])} &nbsp;→&nbsp; ${esc(e[1])} &nbsp;→&nbsp; <b>${e[2]}</b>`; $("#pv").textContent = e[3]; };
  sel.onchange = upd; upd();
})();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Sort each operator into its type.", buckets: [{ label: "Arithmetic" }, { label: "Comparison" }, { label: "Logical" }], items: [
  { text: "+", b: 0 }, { text: "*", b: 0 }, { text: "^", b: 0 }, { text: "DIV", b: 0 }, { text: "MOD", b: 0 },
  { text: "=", b: 1 }, { text: "<>", b: 1 }, { text: ">=", b: 1 }, { text: "<", b: 1 },
  { text: "AND", b: 2 }, { text: "OR", b: 2 }, { text: "NOT", b: 2 }],
  done: "Arithmetic calculates, comparison gives TRUE/FALSE, logical combines TRUE/FALSE." });
Lib.match($("#m1"), { prompt: "Match each operator to what it does.", pairs: [
  ["MOD", "Remainder after division"], ["DIV", "Whole number of times it divides"], ["^", "To the power of"], ["<>", "Not equal to"], ["AND", "TRUE only if both sides are TRUE"], ["OR", "TRUE if at least one side is TRUE"]],
  done: "MOD is the remainder, DIV is the whole number." });
Lib.calc($("#c1"), { qs: [
  { q: "What is 17 DIV 5?", a: 3, sol: "5 goes into 17 three times (15)." },
  { q: "What is 17 MOD 5?", a: 2, sol: "17 − 15 = 2." },
  { q: "What is 2 ^ 5?", a: 32, sol: "2 × 2 × 2 × 2 × 2 = 32." },
  { q: "What is 3 + 4 * 2?", a: 11, sol: "4 * 2 = 8 first, then 3 + 8 = 11." },
  { q: "What is (3 + 4) * 2?", a: 14, sol: "Brackets first: 7 * 2 = 14." },
  { q: "What is 100 DIV 60? (Whole hours in 100 minutes.)", a: 1, sol: "60 goes into 100 once." },
  { q: "What is NOT (5 > 3)? Type TRUE or FALSE.", t: ["FALSE"], ph: "TRUE or FALSE", sol: "5 > 3 is TRUE. NOT reverses it to FALSE." },
  { q: "Age is 15. Is Age >= 13 AND Age <= 19 TRUE or FALSE?", t: ["TRUE"], ph: "TRUE or FALSE", sol: "Both parts are TRUE, so AND is TRUE." }] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which expression is TRUE when X is even?", opts: ["X MOD 2 = 0", "X DIV 2 = 0", "X ^ 2 = 0", "X / 2 = 1"], a: 0, why: "An even number has no remainder when divided by 2." },
  { q: "What is 7 + 3 * 2?", opts: ["13", "20", "16", "12"], a: 0, why: "Multiply first: 6, then add 7." },
  { q: "TRUE AND FALSE is...", opts: ["FALSE", "TRUE", "0", "an error"], a: 0, why: "AND needs both sides TRUE." },
  { q: "TRUE OR FALSE is...", opts: ["TRUE", "FALSE", "0", "an error"], a: 0, why: "OR needs at least one TRUE." },
  { q: "Which operator gives the remainder of a division?", opts: ["MOD", "DIV", "^", "/"], a: 0, why: "MOD gives the remainder." }] });
Lib.cards($("#fc1"), { cards: [
  ["Operator", "A symbol or word that does something to values."],
  ["Arithmetic operator", "Calculates: + - * / ^ DIV MOD."],
  ["Comparison operator", "Compares two values and gives TRUE or FALSE: = <> < > <= >=."],
  ["Logical operator", "Combines TRUE/FALSE values: AND, OR, NOT."],
  ["DIV", "Division that gives only the whole number part (17 DIV 5 = 3)."],
  ["MOD", "Gives the remainder of a division (17 MOD 5 = 2)."],
  ["^", "The power operator: 2 ^ 3 = 8."],
  ["Boolean", "A data type with only two values: TRUE and FALSE."]] });
''')
write_js("p814f", js)
