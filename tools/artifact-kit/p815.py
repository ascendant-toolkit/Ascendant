"""8.1.5 Nested statements."""
from p814k import *

IF_PS = ["INPUT Age", "INPUT Member", "IF Age >= 18", "  THEN", '    IF Member = "Y"', "      THEN", "        Price ← 8", "      ELSE", "        Price ← 10", "    ENDIF", "  ELSE", "    Price ← 5", "ENDIF", "OUTPUT Price"]
IF_PY = ["age = int(input())", "member = input()", "if age >= 18:", '    if member == "Y":', "        price = 8", "    else:", "        price = 10", "else:", "    price = 5", "print(price)"]
HI_PS = ["Highest ← 0", "FOR Count ← 1 TO 4", "    INPUT Mark", "    IF Mark > Highest", "      THEN", "        Highest ← Mark", "    ENDIF", "NEXT Count", "OUTPUT Highest"]
HI_PY = ["highest = 0", "for count in range(1, 5):", "    mark = int(input())", "    if mark > highest:", "        highest = mark", "print(highest)"]
LP_PS = ["FOR Row ← 1 TO 3", "    FOR Column ← 1 TO 3", "        OUTPUT Row * Column", "    NEXT Column", "NEXT Row"]
LP_PY = ["for row in range(1, 4):", "    for column in range(1, 4):", "        print(row * column)"]
TH_PS = ["FOR Student ← 1 TO 2", "    REPEAT", "        INPUT Mark", "    UNTIL Mark >= 0 AND Mark <= 100", "    IF Mark >= 50", "      THEN", '        OUTPUT "Pass"', "      ELSE", '        OUTPUT "Fail"', "    ENDIF", "NEXT Student"]
TH_PY = ["for student in range(1, 3):", "    mark = int(input())", "    while mark < 0 or mark > 100:", "        mark = int(input())", "    if mark >= 50:", '        print("Pass")', "    else:", '        print("Fail")']


def anim_if():
    r = R(["Age", "Member", "Price"])
    r.f("A cinema price depends on age. <b>Only adults</b> are then asked about membership. The user types 20, then \"N\".", [0], [0], inp=[20, "N"])
    r.v["Age"] = 20; r.f("<b>INPUT Age</b>: 20.", [0], [0], hl=["Age"], inp=["N"])
    r.v["Member"] = "N"; r.f('<b>INPUT Member</b>: "N".', [1], [1], hl=["Member"], inp=[])
    r.f("<b>Outer IF</b>: is 20 >= 18? TRUE, so go into the outer THEN.", [2, 3], [2], cond=("20 >= 18", True))
    r.f('<b>Inner IF</b>: is Member = "Y"? It is only tested because the outer test passed.', [4], [3], cond=('"N" = "Y"', False))
    r.v["Price"] = 10; r.f("FALSE, so the <b>inner ELSE</b> runs: Price ← 10.", [7, 8], [5, 6], hl=["Price"])
    r.f("<b>ENDIF</b> closes the inner IF. The outer ELSE is skipped, because the outer test was TRUE.", [9, 12], [], hl=["Price"], note="Outer ELSE skipped")
    r.out.append("10"); r.f("<b>OUTPUT Price</b>: 10.", [13], [9], hl=["Price"])
    return r.js()


def anim_hi():
    q = [41, 73, 58, 90]; r = R(["Count", "Mark", "Highest"])
    r.v["Highest"] = 0; r.f("<b>Highest ← 0</b>. Marks cannot be below 0, so any real mark can beat it.", [0], [0], hl=["Highest"], inp=list(q))
    h = 0
    for i, m in enumerate(q):
        r.v["Count"] = i + 1; r.v["Mark"] = m
        r.f(f"Loop {i + 1}. <b>INPUT Mark</b>: {m}.", [1, 2], [1, 2], hl=["Count", "Mark"], inp=q[i + 1:])
        ok = m > h
        r.f(f"The <b>IF is inside the loop</b>, so this mark is tested now. Is {m} > {h}?", [3], [3], cond=(f"{m} > {h}", ok), inp=q[i + 1:])
        if ok:
            h = m; r.v["Highest"] = h
            r.f(f"TRUE, so <b>Highest ← {m}</b>.", [5], [4], hl=["Highest"], cond=(f"{m} > Highest", True), inp=q[i + 1:])
    r.out.append(str(h)); r.f(f"The loop has ended. <b>OUTPUT Highest</b>: {h}. This is outside the loop, so it appears once.", [8], [5], hl=["Highest"], inp=[])
    return r.js()


def anim_loops():
    r = R(["Row", "Column"])
    r.f("Two FOR loops, one inside the other. Watch how fast each counter changes.", [0], [0])
    for a in range(1, 4):
        r.v["Row"] = a; r.v["Column"] = None
        r.f(f"<b>Outer loop</b>: Row is {a}. The inner loop now starts again from the beginning.", [0], [0], hl=["Row"])
        for b in range(1, 4):
            r.v["Column"] = b; r.out.append(str(a * b))
            r.f(f"<b>Inner loop</b>: Column is {b}. OUTPUT {a} * {b} = <b>{a * b}</b>.", [1, 2], [1, 2], hl=["Column"])
        r.f(f"The inner loop has finished all 3 repeats. " + ("<b>NEXT Row</b> moves the outer loop on." if a < 3 else "The outer loop has finished too. 3 × 3 = <b>9</b> outputs."), [4], [], hl=["Row"])
    return r.js()


def anim_three():
    q = [120, 64, 38]; r = R(["Student", "Mark"]); k = 0
    r.f("Three structures: a <b>FOR</b> loop holding a <b>REPEAT</b> loop (validation) and an <b>IF</b>.", [0], [0], inp=list(q))
    for st in (1, 2):
        r.v["Student"] = st; r.f(f"<b>FOR</b>: Student {st}.", [0], [0], hl=["Student"], inp=q[k:])
        first = True
        while True:
            m = q[k]; k += 1; r.v["Mark"] = m
            r.f(f"<b>INPUT Mark</b>: {m}.", [1, 2], [1] if first else [3], hl=["Mark"], inp=q[k:])
            ok = 0 <= m <= 100
            r.f("Valid, so leave the REPEAT loop." if ok else "Out of range, so the <b>inner loop repeats</b>. The student number does not change.", [3], [2], cond=(f"{m} >= 0 AND {m} <= 100", ok), inp=q[k:])
            if ok:
                break
            first = False
        p = m >= 50
        r.f(f"Now the <b>IF</b>, still inside the FOR loop. Is {m} >= 50?", [4], [4], cond=(f"{m} >= 50", p), inp=q[k:])
        r.out.append("Pass" if p else "Fail")
        r.f(f"OUTPUT \"{'Pass' if p else 'Fail'}\". Then <b>NEXT Student</b>.", [6 if p else 8, 10], [5 if p else 7], inp=q[k:])
    return r.js()


learn = '''
  <h2>8.1.5 Nested statements</h2>
  <p>A statement is <span class="kw">nested</span> when one structure is placed <b>completely inside</b> another: an IF inside an IF, a loop inside a loop, an IF inside a loop, and so on. Nesting lets a program make follow-up decisions and repeat whole blocks of work.</p>

  <h3>Nested selection</h3>
  <p>An IF inside another IF. The <b>inner</b> condition is only tested if the program reaches it through the <b>outer</b> one. Each IF needs its own <span class="ln2">ENDIF</span>.</p>
  <div id="cdIf" class="code"></div>
  <p>A <b>CASE</b> statement can be nested too, and an IF can sit inside one of its branches.</p>
  <div id="cdCase" class="code"></div>

  <h3>Selection inside iteration</h3>
  <p>An IF inside a loop makes a decision about <b>every</b> item. This is how you count passes, check each input or find the highest value.</p>
  <div id="cdHi" class="code"></div>

  <h3>Nested iteration</h3>
  <p>A loop inside a loop. For <b>each single repeat</b> of the outer loop, the inner loop runs <b>all</b> of its repeats. Each loop needs its own counter.</p>
  <div id="cdLp" class="code"></div>
  <div class="tip"><b class="h">How many times?</b>For two FOR loops with fixed limits, multiply: outer repeats × inner repeats. 3 × 3 = 9.</div>

  <h3>Where a line sits changes what it does</h3>
  <div class="tw"><table class="t">
    <tr><th>A line placed...</th><th>runs...</th><th>Typical use</th></tr>
    <tr><td>before the outer loop</td><td>once, at the start</td><td>set an overall total to 0</td></tr>
    <tr><td>inside the outer loop, before the inner loop</td><td>once per outer repeat</td><td>reset a total for each student</td></tr>
    <tr><td>inside the inner loop</td><td>every inner repeat</td><td>input one mark and add it on</td></tr>
    <tr><td>inside the outer loop, after the inner loop</td><td>once per outer repeat</td><td>output that student's total</td></tr>
    <tr><td>after the outer loop</td><td>once, at the end</td><td>output the overall result</td></tr>
  </table></div>

  <h3>Keeping it readable</h3>
  <p><b>Indent</b> each level further than the one outside it, and close structures in reverse order: the last one opened is the <b>first</b> one closed. Structures may sit inside each other but must never cross.</p>
  <div class="warn"><b class="h">Three levels is the limit</b>In the exam you will not be asked to write more than <b>three levels</b> of nested statements.</div>
  <div class="tip"><b class="h">Nested IF or AND?</b><code>IF A THEN IF B</code> with no ELSE does the same job as <code>IF A AND B</code>. Use a nested IF when each level needs its own ELSE or its own message. In Python, <code>elif</code> keeps a chain of tests flat.</div>
'''

watch = '''  <h2>1 · An IF inside an IF</h2><div id="aI"></div>
  <h2>2 · An IF inside a loop</h2><div id="aH"></div>
  <h2>3 · A loop inside a loop</h2><div id="aL"></div>
  <h2>4 · Three levels: loop, validation loop and IF</h2><div id="aT"></div>
'''

explore = '''  <h2>Lab 1 · Follow the path</h2>
  <p>Change the age and membership. The highlighted lines show which parts run.</p>
  <div class="card"><div id="s1"></div><label><input type="checkbox" id="mem"> Member</label><div id="pcode"></div><div class="verdict" id="pv" aria-live="polite"></div></div>

  <h2>Lab 2 · Loops inside loops</h2>
  <p>Each box is one run of the inner loop body, labelled outer,inner. Tick the box to make the inner loop's end value depend on the outer counter.</p>
  <div class="card"><div id="s2"></div><div id="s3"></div><label><input type="checkbox" id="tri"> Inner loop runs from 1 TO Outer</label><div id="gcode"></div><div id="grid" style="margin:10px 0"></div><div class="verdict" id="gv" aria-live="polite"></div></div>

  <h2>Lab 3 · Where does Total ← 0 go?</h2>
  <p>Two students each have three marks: Student 1 has 5, 6, 7 and Student 2 has 8, 9, 10. Move the line that resets Total and compare the output.</p>
  <div class="card"><div id="s4"></div><div id="rcode"></div><div class="out" id="rout" style="min-height:44px"></div><div class="verdict" id="rv" aria-live="polite"></div></div>
'''

practise = '''  <h2>1 · What is nested in what?</h2>
  <div id="cl1" class="card"></div>
  <h2>2 · Build a nested loop</h2>
  <div id="o1" class="card"></div>
  <h2>3 · Trace it</h2>
  <div id="c1"></div>
  <h2>4 · Multiple choice</h2>
  <div id="qz1"></div>
'''

real = (rw("A cash machine", "The machine first checks the PIN. Only if it is correct does it check whether there is enough money for the withdrawal.", "nested selection: the inner test is only reached when the outer test is TRUE.")
        + rw("A school report run", "For every student, the program goes through every subject, then prints that student's average.", "nested iteration: outer loop for students, inner loop for subjects.")
        + rw("Checking a login form", "The system keeps asking while attempts remain, and inside that loop it decides whether the details match.", "selection inside a condition-controlled loop.")
        + rw("Drawing a screen", "An image is drawn one row at a time, and within each row one pixel at a time.", "nested FOR loops: total pixels = rows × pixels per row."))

ex = [
    eq(1, "State", 2, "State what is meant by a <b>nested statement</b> and give one example.", "Say what is inside what.",
       mk(1, "A statement / structure placed inside another one") + " " + mk(2, "Example: an IF inside a loop (or IF inside IF, or loop inside loop)"),
       "Giving two separate IF statements one after the other. That is not nesting."),
    eq(2, "State", 3, "State the output of this code when X is 12 and Y is 3.", "Test the outer condition first.",
       mk(1, "X > 10 is TRUE, so the inner IF is tested") + " " + mk(2, "Y > 5 is FALSE, so the inner ELSE runs") + " " + mk(3, 'Output: B'),
       "Outputting C. The outer ELSE only runs when X > 10 is FALSE.",
       pre=qc(["IF X > 10", "  THEN", "    IF Y > 5", "      THEN", '        OUTPUT "A"', "      ELSE", '        OUTPUT "B"', "    ENDIF", "  ELSE", '    OUTPUT "C"', "ENDIF"])),
    eq(3, "State", 2, "State how many times the word \"Hi\" is output, and show how you worked it out.", "Multiply the repeats.",
       mk(1, "4 × 5") + " " + mk(2, "= 20 times"),
       "Adding 4 + 5. The inner loop runs fully for <b>each</b> outer repeat.",
       pre=qc(["FOR A ← 1 TO 4", "    FOR B ← 1 TO 5", '        OUTPUT "Hi"', "    NEXT B", "NEXT A"])),
    eq(4, "Write", 4, "A mark is stored in Mark. Write pseudocode to output \"Invalid\" if it is below 0 or above 100. Otherwise output \"Pass\" for 50 or more and \"Fail\" for less than 50.", "Validate on the outer IF, grade on the inner IF.",
       mk(1, "IF Mark &lt; 0 OR Mark > 100") + " " + mk(2, 'THEN OUTPUT "Invalid"') + " " + mk(3, 'inner IF Mark >= 50 inside the ELSE, outputting "Pass" / "Fail"') + " " + mk(4, "both IFs closed with ENDIF in the right places")
       + ac(["IF Mark < 0 OR Mark > 100", "  THEN", '    OUTPUT "Invalid"', "  ELSE", "    IF Mark >= 50", "      THEN", '        OUTPUT "Pass"', "      ELSE", '        OUTPUT "Fail"', "    ENDIF", "ENDIF"]),
       "Writing AND in the first test. No number is both below 0 and above 100."),
    eq(5, "Write", 5, "Write pseudocode to input 30 numbers. Count how many are positive and how many are negative (ignore zeros), then output both counts.", "Set both counts to 0 before the loop.",
       mk(1, "Positive ← 0 and Negative ← 0 before the loop") + " " + mk(2, "loop 30 times with INPUT inside") + " " + mk(3, "IF Number > 0, add 1 to Positive") + " " + mk(4, "test for Number &lt; 0 and add 1 to Negative") + " " + mk(5, "OUTPUT both after the loop")
       + ac(["Positive ← 0", "Negative ← 0", "FOR Count ← 1 TO 30", "    INPUT Number", "    IF Number > 0", "      THEN", "        Positive ← Positive + 1", "      ELSE", "        IF Number < 0", "          THEN", "            Negative ← Negative + 1", "        ENDIF", "    ENDIF", "NEXT Count", "OUTPUT Positive, Negative"]),
       "Using a plain ELSE for negatives, which also counts the zeros."),
    eq(6, "Complete", 4, "Give the values output by this code, in order.", "Write down A and B for every inner repeat.",
       mk(1, "A = 1: B runs 1 to 1, output 1") + " " + mk(2, "A = 2: outputs 2, 4") + " " + mk(3, "A = 3: outputs 3, 6, 9") + " " + mk(4, "full order: 1, 2, 4, 3, 6, 9"),
       "Running B from 1 to 3 every time. Its end value is <b>A</b>.",
       pre=qc(["FOR A ← 1 TO 3", "    FOR B ← 1 TO A", "        OUTPUT A * B", "    NEXT B", "NEXT A"])),
    eq(7, "Write", 6, "There are 5 students and each takes 3 tests. Write pseudocode to input the marks and output the total for each student.", "Ask where Total ← 0 must go.",
       mk(1, "outer loop for 5 students") + " " + mk(2, "Total ← 0 inside the outer loop") + " " + mk(3, "inner loop for 3 tests") + " " + mk(4, "INPUT Mark inside the inner loop") + " " + mk(5, "Total ← Total + Mark inside the inner loop") + " " + mk(6, "OUTPUT Total after the inner loop but inside the outer loop")
       + ac(["FOR Student ← 1 TO 5", "    Total ← 0", "    FOR Test ← 1 TO 3", "        INPUT Mark", "        Total ← Total + Mark", "    NEXT Test", "    OUTPUT Total", "NEXT Student"]),
       "Setting Total ← 0 before the outer loop, so totals carry over between students."),
    eq(8, "Explain", 3, "The code below should output 12 values but does not run correctly. Identify the error, explain why it is wrong and correct it.", "Which loop was opened last?",
       mk(1, "NEXT X and NEXT Y are the wrong way round") + " " + mk(2, "the inner loop (Y) must be closed before the outer loop (X), because loops cannot cross") + " " + mk(3, "correct order: NEXT Y then NEXT X"),
       "Changing the loop limits. The limits are fine; the order of the NEXT lines is not.",
       pre=qc(["FOR X ← 1 TO 3", "    FOR Y ← 1 TO 4", "        OUTPUT X + Y", "    NEXT X", "NEXT Y"])),
    eq(9, "Write", 6, "Write pseudocode to input the ages of 100 visitors. Each age must be from 0 to 120; ask again until it is. Count the visitors aged under 12 and output the count.", "This needs three levels: FOR, then REPEAT, and an IF.",
       mk(1, "Children ← 0 before the loop") + " " + mk(2, "FOR loop that repeats 100 times") + " " + mk(3, "REPEAT with INPUT Age inside") + " " + mk(4, "UNTIL Age >= 0 AND Age &lt;= 120") + " " + mk(5, "IF Age &lt; 12 add 1 to Children, inside the FOR loop but after the REPEAT") + " " + mk(6, "OUTPUT Children after the FOR loop")
       + ac(["Children ← 0", "FOR Visitor ← 1 TO 100", "    REPEAT", "        INPUT Age", "    UNTIL Age >= 0 AND Age <= 120", "    IF Age < 12", "      THEN", "        Children ← Children + 1", "    ENDIF", "NEXT Visitor", "OUTPUT Children"]),
       "Counting inside the REPEAT loop, before the age has been checked."),
]

tipshtml = tips([
    "<b>Indent every level.</b> The indentation should show which structure each line belongs to.",
    "<b>Close in reverse order.</b> The structure opened last is closed first.",
    "<b>Every IF needs its own ENDIF</b>, every FOR its own NEXT with the matching counter.",
    "<b>Two nested FOR loops: multiply</b> the repeats (unless the inner limits change).",
    "<b>Place totals carefully.</b> Reset inside the outer loop if each group needs its own total.",
    "<b>Trace the outer counter slowly and the inner counter quickly.</b> Add a trace table column for each.",
])

page("8.1.5 · Nested statements", "Nested Statements", "Selection and iteration placed inside each other, up to three levels deep.",
     "A <span class=\"kw\">nested statement</span> is a structure <b>inside</b> another structure. The inner one only runs when the outer one reaches it, and it runs again each time the outer one does.",
     learn, watch, explore, practise, real, "".join(ex), tipshtml, "p815")

js = []
consts = ", ".join(f"{n} = {json.dumps(v, ensure_ascii=False)}" for n, v in [("IF_PS", IF_PS), ("IF_PY", IF_PY), ("HI_PS", HI_PS), ("HI_PY", HI_PY), ("LP_PS", LP_PS), ("LP_PY", LP_PY), ("TH_PS", TH_PS), ("TH_PY", TH_PY)])
js.append(f'''
const {consts};
tr($("#aI"), {{ label: "Nested IF", title: "Nested selection", pseudo: IF_PS, py: IF_PY, frames: {anim_if()} }});
tr($("#aH"), {{ label: "IF inside a loop", title: "Selection inside iteration", pseudo: HI_PS, py: HI_PY, dwell: 1800, frames: {anim_hi()} }});
tr($("#aL"), {{ label: "Nested loops", title: "Nested iteration", pseudo: LP_PS, py: LP_PY, dwell: 1500, frames: {anim_loops()} }});
tr($("#aT"), {{ label: "Three levels", title: "Three levels of nesting", pseudo: TH_PS, py: TH_PY, frames: {anim_three()} }});
Lib.codePanel($("#cdIf"), {{ pseudo: IF_PS, py: IF_PY }});
Lib.codePanel($("#cdCase"), {{ pseudo: ["CASE OF Choice", "    1 : IF Balance > 0", "          THEN", '            OUTPUT "Withdraw"', "          ELSE", '            OUTPUT "No funds"', "        ENDIF", '    2 : OUTPUT "Deposit"', '    OTHERWISE OUTPUT "Invalid"', "ENDCASE"], py: ["match choice:", "    case 1:", "        if balance > 0:", '            print("Withdraw")', "        else:", '            print("No funds")', "    case 2:", '        print("Deposit")', "    case _:", '        print("Invalid")'] }});
Lib.codePanel($("#cdHi"), {{ pseudo: HI_PS, py: HI_PY }});
Lib.codePanel($("#cdLp"), {{ pseudo: LP_PS, py: LP_PY }});
''')

js.append(r'''
/* ---------- Lab 1 ---------- */
(() => {
  const cp = Lib.codePanel($("#pcode"), { pseudo: IF_PS, py: IF_PY }); let a;
  const upd = () => { if (!a) return; const age = a.get(), m = $("#mem").checked, adult = age >= 18, price = adult ? (m ? 8 : 10) : 5;
    cp.hl(adult ? (m ? [2, 4, 6, 13] : [2, 4, 8, 13]) : [2, 11, 13], adult ? (m ? [2, 3, 4, 9] : [2, 3, 6, 9]) : [2, 8, 9]);
    $("#pv").innerHTML = adult ? `${age} >= 18 is TRUE, so the inner IF is tested. ${m ? "Member" : "Not a member"}: price <b>${price}</b>.` : `${age} >= 18 is FALSE. The inner IF is <b>never tested</b>, so membership makes no difference: price <b>5</b>.`; };
  a = Lib.slider($("#s1"), { id: "pa", label: "Age ", min: 5, max: 40, value: 20, onInput: upd });
  $("#mem").onchange = upd; upd();
})();

/* ---------- Lab 2 ---------- */
(() => {
  let a, b;
  const upd = () => { if (!a || !b) return; const o = a.get(), n = b.get(), t = $("#tri").checked; let total = 0;
    Lib.codePanel($("#gcode"), { pseudo: [`FOR Outer ← 1 TO ${o}`, `    FOR Inner ← 1 TO ${t ? "Outer" : n}`, '        OUTPUT Outer, ",", Inner', "    NEXT Inner", "NEXT Outer"], py: [`for outer in range(1, ${o + 1}):`, `    for inner in range(1, ${t ? "outer + 1" : n + 1}):`, '        print(outer, ",", inner)'] });
    $("#grid").innerHTML = Array.from({ length: o }, (_, i) => `<div style="display:flex;gap:4px;margin-bottom:4px;flex-wrap:wrap">` + Array.from({ length: t ? i + 1 : n }, (_, j) => { total++; return `<span style="border:1px solid var(--line);border-radius:6px;padding:2px 7px;font-family:var(--mono)">${i + 1},${j + 1}</span>`; }).join("") + "</div>").join("");
    $("#gv").innerHTML = t ? `The inner loop runs 1, then 2, ... up to ${o} times: <b>${total}</b> in total. The inner limit slider is not used.` : `${o} × ${n} = <b>${total}</b> runs of the inner body.`; };
  a = Lib.slider($("#s2"), { id: "go", label: "Outer loop end ", min: 1, max: 6, value: 3, onInput: upd });
  b = Lib.slider($("#s3"), { id: "gi", label: "Inner loop end ", min: 1, max: 8, value: 4, onInput: upd });
  $("#tri").onchange = upd; upd();
})();

/* ---------- Lab 3 ---------- */
Lib.slider($("#s4"), { id: "rp", label: "Position of Total ← 0: ", min: 1, max: 3, value: 1, fmt: (v) => ["before the outer loop", "inside the outer loop", "inside the inner loop"][v - 1], onInput: (p) => {
  const L = ["FOR Student ← 1 TO 2", "    FOR Test ← 1 TO 3", "        INPUT Mark", "        Total ← Total + Mark", "    NEXT Test", "    OUTPUT Total", "NEXT Student"], Q = ["for student in range(1, 3):", "    for test in range(1, 4):", "        mark = int(input())", "        total = total + mark", "    print(total)"];
  if (p === 1) { L.splice(0, 0, "Total ← 0"); Q.splice(0, 0, "total = 0"); } else if (p === 2) { L.splice(1, 0, "    Total ← 0"); Q.splice(1, 0, "    total = 0"); } else { L.splice(2, 0, "        Total ← 0"); Q.splice(2, 0, "        total = 0"); }
  Lib.codePanel($("#rcode"), { pseudo: L, py: Q });
  const out = []; let total = 0;
  for (const marks of [[5, 6, 7], [8, 9, 10]]) { if (p === 2) total = 0; for (const m of marks) { if (p === 3) total = 0; total += m; } out.push(total); }
  $("#rout").textContent = out.join("   ");
  $("#rv").innerHTML = ["Wrong for Student 2: the total <b>carries on</b> from Student 1.", "<b>Correct.</b> Total is reset once for each student.", "Wrong: Total is reset before <b>every</b> mark, so only the last mark survives."][p - 1]; } });

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Match each task to the structure it needs.", buckets: [{ label: "IF inside IF" }, { label: "IF inside a loop" }, { label: "Loop inside a loop" }], items: [
  { text: "Check the username, and only if it is right check the password", b: 0 }, { text: "If the customer is a member, check whether they spent over 50", b: 0 },
  { text: "Count how many of 100 marks are passes", b: 1 }, { text: "Find the smallest of 20 temperatures", b: 1 },
  { text: "Input 7 daily readings for each of 4 weeks", b: 2 }, { text: "Output the times tables from 1 to 12", b: 2 }],
  done: "Follow-up decision: nested IF. Decision for every item: IF in a loop. Repeats of repeats: nested loops." });
Lib.order($("#o1"), { prompt: "Output a total for each of 3 days, 24 readings per day.", items: ["FOR Day ← 1 TO 3", "Total ← 0", "FOR Hour ← 1 TO 24", "INPUT Reading", "Total ← Total + Reading", "NEXT Hour", "OUTPUT Total", "NEXT Day"], done: "Reset, inner loop, output, all inside the outer loop." });
Lib.calc($("#c1"), { qs: [
  { q: "FOR A ← 1 TO 6, containing FOR B ← 1 TO 4. How many times does the inner body run?", a: 24, sol: "6 × 4 = 24." },
  { q: "FOR A ← 1 TO 4, containing FOR B ← 1 TO A. How many times does the inner body run?", a: 10, sol: "1 + 2 + 3 + 4 = 10." },
  { q: "Three nested FOR loops each run 1 TO 3. How many times does the innermost body run?", a: 27, sol: "3 × 3 × 3 = 27." },
  { q: "Total ← 0. FOR A ← 1 TO 3, FOR B ← 1 TO 2, Total ← Total + A. What is the final Total?", a: 12, sol: "Each A is added twice: 2 + 4 + 6 = 12." },
  { q: "IF N > 5 THEN (IF N > 10 THEN X ← 1 ELSE X ← 2) ELSE X ← 3. What is X when N is 10?", a: 2, sol: "10 > 5 is TRUE, 10 > 10 is FALSE, so X ← 2." }] });
Lib.quiz($("#qz1"), { qs: [
  { q: "When is an inner IF tested?", opts: ["Only when the program reaches it through the outer structure", "Always, before the outer IF", "Only when the outer test is FALSE and there is no ELSE", "Once at the start of the program"], a: 0, why: "It sits inside one branch of the outer structure." },
  { q: "In nested loops, which loop completes all its repeats first?", opts: ["The inner loop", "The outer loop", "They finish together on every pass", "Whichever has the larger limit"], a: 0, why: "The inner loop runs fully for each outer repeat." },
  { q: "What is the greatest number of nesting levels you will be asked to write?", opts: ["Three", "Two", "Five", "There is no limit"], a: 0, why: "The syllabus limits it to three." },
  { q: "Why indent nested statements?", opts: ["It makes the structure easy to read", "It makes the program run faster", "It removes the need for ENDIF", "It creates local variables"], a: 0, why: "Indentation shows which lines belong together." },
  { q: "IF A THEN IF B (no ELSE anywhere) does the same job as...", opts: ["IF A AND B", "IF A OR B", "IF NOT A", "a WHILE loop on A"], a: 0, why: "Both conditions must be TRUE." }] });
Lib.cards($("#fc1"), { cards: [
  ["Nested statement", "A structure placed inside another structure."],
  ["Nested selection", "A selection statement inside another selection statement."],
  ["Nested iteration", "A loop inside another loop."],
  ["Outer loop", "The loop that contains another loop."],
  ["Inner loop", "The loop inside; it runs fully for each repeat of the outer loop."],
  ["Indentation", "Moving lines to the right to show which structure they belong to."]] });
''')
write_js("p815", js)
