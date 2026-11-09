"""8.1.4 Iteration."""
from p814k import *

FOR_PS = ["FOR Count ← 1 TO 4", "    OUTPUT Count * 3", "NEXT Count"]
FOR_PY = ["for count in range(1, 5):", "    print(count * 3)"]
WH_PS = ["Number ← 3", "WHILE Number > 0 DO", "    OUTPUT Number", "    Number ← Number - 1", "ENDWHILE", 'OUTPUT "Go!"']
WH_PY = ["number = 3", "while number > 0:", "    print(number)", "    number = number - 1", 'print("Go!")']
RP_PS = ["REPEAT", '    INPUT Password', '    IF Password <> "open"', "      THEN", '        OUTPUT "Wrong"', "    ENDIF", 'UNTIL Password = "open"', 'OUTPUT "Welcome"']
RP_PY = ["while True:", "    password = input()", '    if password != "open":', '        print("Wrong")', "    else:", "        break", 'print("Welcome")']


def anim_for():
    r = R(["Count"])
    r.f("<b>FOR Count ← 1 TO 4</b> will run the loop body 4 times. It sets Count to 1 first.", [0], [0])
    for c in range(1, 5):
        r.v["Count"] = c; r.f(f"Count is <b>{c}</b>. Body: OUTPUT {c} * 3.", [1], [1], hl=["Count"])
        r.out.append(str(c * 3)); r.f(f"Output <b>{c * 3}</b>. <b>NEXT Count</b> adds 1 to Count and goes back to the top.", [2], [1], hl=["Count"]) if c < 4 else r.f(f"Output <b>{c * 3}</b>. Count has reached 4, the last value, so the loop ends.", [2], [1], hl=["Count"], note="4 repeats, then stop", nc="t3")
    return r.js()


def anim_while():
    r = R(["Number"])
    r.v["Number"] = 3; r.f("<b>Number ← 3</b>.", [0], [0], hl=["Number"])
    n = 3
    while True:
        r.f(f"The condition is tested <b>before</b> each repeat. Is Number > 0?", [1], [1], cond=(f"{n} > 0", n > 0))
        if n <= 0: break
        r.out.append(str(n)); r.f(f"TRUE, so the body runs. <b>OUTPUT {n}</b>.", [2], [2], cond=(f"{n} > 0", True))
        n -= 1; r.v["Number"] = n; r.f(f"<b>Number ← Number - 1</b>. It is now {n}. Back to the test.", [3], [3], hl=["Number"])
    r.f("FALSE, so the loop is skipped and the program carries on after ENDWHILE.", [4], [], cond=("0 > 0", False))
    r.out.append("Go!"); r.f('<b>OUTPUT "Go!"</b>.', [5], [4])
    return r.js()


def anim_repeat():
    r = R(["Password"]); q = ["abc", "123", "open"]
    r.f("REPEAT runs the body <b>first</b>, then tests the condition at the end.", [0], [0], inp=list(q))
    for k, p in enumerate(q):
        r.v["Password"] = p; r.f(f"<b>INPUT Password</b>: the user types \"{p}\".", [1], [1], hl=["Password"], inp=q[k + 1:])
        ok = p == "open"
        if not ok:
            r.out.append("Wrong"); r.f(f"\"{p}\" is not \"open\", so OUTPUT \"Wrong\".", [2, 3, 4], [2, 3], hl=["Password"], inp=q[k + 1:])
        r.f(f"<b>UNTIL Password = \"open\"</b>? {'It is, so stop repeating.' if ok else 'Not yet, so go back to REPEAT.'}", [6], [4, 5] if ok else [0], cond=(f'"{p}" = "open"', ok), inp=q[k + 1:])
    r.out.append("Welcome"); r.f("The loop has ended. <b>OUTPUT \"Welcome\"</b>. The body ran 3 times; it always runs <b>at least once</b>.", [7], [6], note="3 repeats", nc="t3")
    return r.js()


learn = '''
  <h2>8.1.4 Iteration</h2>
  <p><span class="kw">Iteration</span> means <b>repeating</b> a set of instructions. The repeated lines are called a <span class="kw">loop</span>. Loops save you from writing the same lines again and again, and let a program repeat something an unknown number of times.</p>

  <h3>FOR: count-controlled</h3>
  <p>Use a <span class="kw">FOR</span> loop when you <b>know how many times</b> to repeat. A <b>loop counter</b> changes by itself each time, from the start value up to the end value. <b>STEP</b> changes the size of the jump.</p>
  <div id="cdFor" class="code"></div>
  <div class="tip"><b class="h">Python's range()</b>In Python, <code>range(1, 5)</code> goes 1, 2, 3, 4. It <b>stops before</b> the end value. Pseudocode's <code>1 TO 4</code> includes 4, so the Python end value is <b>one more</b>. For a step use <code>range(0, 11, 2)</code>.</div>
  <div id="cdStep" class="code"></div>

  <h3>WHILE: condition tested first</h3>
  <p>A <span class="kw">WHILE</span> loop repeats <b>while a condition is TRUE</b>, and tests it <b>before</b> each repeat. If the condition is FALSE at the start, the body <b>never runs</b>. Something inside the loop must change the condition, or it will never stop.</p>
  <div id="cdWhile" class="code"></div>

  <h3>REPEAT ... UNTIL: condition tested last</h3>
  <p>A <span class="kw">REPEAT</span> loop runs the body, then tests the condition at the <b>end</b>. It repeats <b>until</b> the condition becomes TRUE, so the body <b>always runs at least once</b>. That suits asking for input again until it is valid.</p>
  <div id="cdRep" class="code"></div>
  <div class="tip"><b class="h">Python has no REPEAT</b>Python has no post-condition loop. The usual way is <code>while True:</code> with a <code>break</code> when the condition is met.</div>

  <h3>Choosing a loop</h3>
  <div class="tw"><table class="t">
    <tr><th></th><th>FOR</th><th>WHILE</th><th>REPEAT ... UNTIL</th></tr>
    <tr><td>Type</td><td>count-controlled</td><td colspan="2">condition-controlled</td></tr>
    <tr><td>Use when</td><td>the number of repeats is known</td><td>it might need to run zero times</td><td>it must run at least once</td></tr>
    <tr><td>Condition tested</td><td>automatic (counter)</td><td>at the start</td><td>at the end</td></tr>
    <tr><td>Repeats while</td><td>counter not past the end</td><td>condition is TRUE</td><td>condition is FALSE (stops when TRUE)</td></tr>
  </table></div>
  <div class="warn"><b class="h">Infinite loops</b>A loop whose condition never changes runs forever. In a WHILE loop, always check that something inside it moves the condition towards FALSE (for example <code>Number ← Number - 1</code>).</div>
  <p>A loop can also sit <b>inside another loop</b>. This is called a <span class="kw">nested loop</span>: the inner loop runs completely for each repeat of the outer loop.</p>
'''

watch = '''  <h2>1 · A FOR loop</h2><div id="aF"></div>
  <h2>2 · A WHILE loop</h2><div id="aW"></div>
  <h2>3 · A REPEAT ... UNTIL loop</h2><div id="aR"></div>
'''

explore = '''  <h2>Lab 1 · FOR loop explorer</h2>
  <p>Set the start, end and step. See the loop counter values, and how many times the body runs. Try a start that is bigger than the end.</p>
  <div class="card"><div id="s1"></div><div id="s2"></div><div id="s3"></div><div id="fcode"></div><div class="readout"><div><small>Repeats</small><strong id="fn"></strong></div><div><small>Counter values</small><strong id="fv" style="font-size:1rem"></strong></div></div><div class="verdict" id="fvd" aria-live="polite"></div></div>

  <h2>Lab 2 · WHILE or REPEAT?</h2>
  <p>Both loops output Number and add 1, and stop at 3. Change the starting value and compare how many times each body runs. Set the start to 5.</p>
  <div class="card"><div id="s4"></div><div class="tw"><table class="t"><tr><th></th><th>WHILE Number &lt; 3</th><th>REPEAT ... UNTIL Number &gt;= 3</th></tr><tr><td>Body runs</td><td id="wn"></td><td id="rn"></td></tr><tr><td>Output</td><td id="wo" class="ln2"></td><td id="ro" class="ln2"></td></tr></table></div><div class="verdict" id="wv" aria-live="polite"></div></div>

  <h2>Lab 3 · Nested loops</h2>
  <p>The outer loop makes the rows and the inner loop makes the stars in each row.</p>
  <div class="card"><div id="s5"></div><div id="s6"></div><div class="out" id="nout" style="min-height:60px;letter-spacing:.2em"></div><div class="verdict" id="nv" aria-live="polite"></div></div>
'''

practise = '''  <h2>1 · Which loop?</h2>
  <div id="cl1" class="card"></div>
  <h2>2 · A REPEAT loop in order</h2>
  <div id="o1" class="card"></div>
  <h2>3 · How many times?</h2>
  <div id="c1"></div>
  <h2>4 · Multiple choice</h2>
  <div id="qz1"></div>
'''

real = (rw("A playlist on repeat", "The player runs through each song in turn until it gets to the end of the playlist.", "a FOR loop, because the number of songs is known.")
        + rw("A PIN prompt", "The ATM asks for your PIN again until it is right, or the card is blocked.", "REPEAT ... UNTIL: you must be asked at least once, and then until the PIN is valid.")
        + rw("A game loop", "While the player still has lives, the game keeps running frames. When lives reach 0 the game stops.", "a WHILE loop, tested before each repeat.")
        + rw("A timetable grid", "For each day (outer loop) the program lists each lesson (inner loop).", "nested loops: the inner loop runs fully for every pass of the outer loop.")
        )

ex = [
    eq(1, "State", 2, "State the difference between a <b>count-controlled</b> loop and a <b>condition-controlled</b> loop.", "One repeats a set number of times. The other repeats until something is true.",
       mk(1, "Count-controlled: repeats a set number of times (known in advance), for example FOR") + " " + mk(2, "Condition-controlled: repeats while / until a condition is met (the number of repeats may not be known), for example WHILE or REPEAT."),
       "Saying a FOR loop \"has a condition\". It has a <b>counter</b>, not a test of a condition."),
    eq(2, "Write", 3, "Write pseudocode to output the numbers 1 to 20.", "FOR, a counter, an output.",
       mk(1, "FOR Count ← 1 TO 20") + " " + mk(2, "OUTPUT Count inside the loop") + " " + mk(3, "NEXT Count")
       + ac(["FOR Count ← 1 TO 20", "    OUTPUT Count", "NEXT Count"]),
       "Using 1 TO 19 or 0 TO 20. Check the first and last values."),
    eq(3, "Complete", 4, "Complete the trace table for the code, and state the output.", "Test the condition each time, <b>before</b> the body.",
       mk(1, "Number: 3, 2, 1, 0") + " " + mk(2, "Output: 3 2 1") + " " + mk(3, "Condition is FALSE when Number is 0, so the loop stops") + " " + mk(4, "then \"Go!\" is output after the loop"),
       "Outputting 0. When Number is 0 the condition 0 > 0 is FALSE, so the body does not run.",
       pre=qc(WH_PS)),
    eq(4, "Write", 4, "Write pseudocode to keep asking for a password until the user types \"open\". Output \"Welcome\" when it is right.", "It must ask at least once, so REPEAT ... UNTIL fits.",
       mk(1, "REPEAT") + " " + mk(2, "INPUT Password inside the loop") + " " + mk(3, "UNTIL Password = \"open\"") + " " + mk(4, "OUTPUT \"Welcome\" after the loop")
       + ac(["REPEAT", "    INPUT Password", 'UNTIL Password = "open"', 'OUTPUT "Welcome"']),
       "Writing UNTIL Password <> \"open\". UNTIL stops the loop when the condition is TRUE."),
    eq(5, "State", 2, "State which type of loop always runs its body at least once, and explain why.", "Think about where the condition is tested.",
       mk(1, "REPEAT ... UNTIL (post-condition loop)") + " " + mk(2, "because the condition is tested at the end, after the body has run once."),
       "Choosing WHILE. A WHILE loop tests first, so it may never run."),
    eq(6, "Rewrite", 3, "Rewrite the WHILE loop as a REPEAT ... UNTIL loop that gives the same output.", "Reverse the condition: WHILE continues while TRUE, UNTIL stops when TRUE.",
       mk(1, "REPEAT in place of WHILE ... DO and UNTIL in place of ENDWHILE") + " " + mk(2, "Condition reversed: UNTIL Number > 5 (or >= 6)") + " " + mk(3, "Body unchanged: OUTPUT Number and Number ← Number + 1")
       + ac(["Number ← 1", "REPEAT", "    OUTPUT Number", "    Number ← Number + 1", "UNTIL Number > 5"]),
       "Copying the WHILE condition into UNTIL. Reverse it (&lt;= becomes &gt;).",
       pre=qc(["Number ← 1", "WHILE Number <= 5 DO", "    OUTPUT Number", "    Number ← Number + 1", "ENDWHILE"])),
    eq(7, "Write", 3, "Write pseudocode to input 10 numbers and output each one doubled.", "A FOR loop with the INPUT inside it.",
       mk(1, "FOR Count ← 1 TO 10 ... NEXT Count") + " " + mk(2, "INPUT Number inside the loop") + " " + mk(3, "OUTPUT Number * 2 inside the loop")
       + ac(["FOR Count ← 1 TO 10", "    INPUT Number", "    OUTPUT Number * 2", "NEXT Count"]),
       "Putting INPUT before the loop, so only one number is read."),
    eq(8, "Write", 5, "Write pseudocode to input 20 marks. For each mark, output \"Pass\" if it is 50 or more, otherwise \"Fail\".", "A loop around a selection.",
       mk(1, "FOR Count ← 1 TO 20") + " " + mk(2, "INPUT Mark inside the loop") + " " + mk(3, "IF Mark >= 50") + " " + mk(4, "THEN OUTPUT \"Pass\" ELSE OUTPUT \"Fail\"") + " " + mk(5, "ENDIF and NEXT Count in the right places (ENDIF inside the loop)")
       + ac(["FOR Count ← 1 TO 20", "    INPUT Mark", "    IF Mark >= 50", "      THEN", '        OUTPUT "Pass"', "      ELSE", '        OUTPUT "Fail"', "    ENDIF", "NEXT Count"]),
       "Putting NEXT Count inside the IF, which breaks the structure."),
    eq(9, "Explain", 2, "The code below never stops. Explain why, and how to fix it.", "Does anything inside the loop change Number?",
       mk(1, "Number is never changed, so Number > 0 is always TRUE (infinite loop)") + " " + mk(2, "Fix: add Number ← Number - 1 inside the loop."),
       "Saying the condition is wrong. The condition is fine. Nothing makes it <b>become FALSE</b>.",
       pre=qc(["Number ← 5", "WHILE Number > 0 DO", "    OUTPUT Number", "ENDWHILE"])),
]
exam = "".join(ex)

tipshtml = tips([
    "<b>FOR when you know how many times.</b> WHILE and REPEAT when you do not.",
    "<b>WHILE tests first and may never run. REPEAT tests last and always runs at least once.</b>",
    "<b>WHILE repeats while TRUE. REPEAT stops when TRUE.</b> Reverse the condition when you convert.",
    "<b>Check the first and last value of a FOR loop.</b> 1 TO 10 runs 10 times.",
    "<b>Something inside a WHILE loop must change the condition</b>, or it runs forever.",
    "<b>Python's range(1, 11) gives 1 to 10.</b> The end value is not included.",
])

page("8.1.4 · Iteration", "Iteration", "Repeating instructions with FOR, WHILE and REPEAT ... UNTIL loops.",
     "<span class=\"kw\">Iteration</span> repeats a block of code. A <b>FOR</b> loop repeats a set number of times. <b>WHILE</b> and <b>REPEAT</b> loops repeat until a condition says stop.",
     learn, watch, explore, practise, real, exam, tipshtml, "p814c")

js = []
js.append(f'''
const FOR_PS = {json.dumps(FOR_PS, ensure_ascii=False)}, FOR_PY = {json.dumps(FOR_PY, ensure_ascii=False)};
const WH_PS = {json.dumps(WH_PS, ensure_ascii=False)}, WH_PY = {json.dumps(WH_PY, ensure_ascii=False)};
const RP_PS = {json.dumps(RP_PS, ensure_ascii=False)}, RP_PY = {json.dumps(RP_PY, ensure_ascii=False)};
tr($("#aF"), {{ label: "FOR loop", title: "FOR loop", pseudo: FOR_PS, py: FOR_PY, dwell: 1800, frames: {anim_for()} }});
tr($("#aW"), {{ label: "WHILE loop", title: "WHILE loop", pseudo: WH_PS, py: WH_PY, dwell: 1800, frames: {anim_while()} }});
tr($("#aR"), {{ label: "REPEAT loop", title: "REPEAT ... UNTIL loop", pseudo: RP_PS, py: RP_PY, dwell: 2000, frames: {anim_repeat()} }});
Lib.codePanel($("#cdFor"), {{ pseudo: FOR_PS, py: FOR_PY }});
Lib.codePanel($("#cdStep"), {{ pseudo: ["FOR Count ← 0 TO 10 STEP 2", "    OUTPUT Count", "NEXT Count"], py: ["for count in range(0, 11, 2):", "    print(count)"] }});
Lib.codePanel($("#cdWhile"), {{ pseudo: WH_PS, py: WH_PY }});
Lib.codePanel($("#cdRep"), {{ pseudo: RP_PS, py: RP_PY }});
''')

js.append(r'''
/* ---------- Lab 1 ---------- */
(() => {
  let a, b, c;
  const upd = () => {
    if (!a || !b || !c) return; const s = a.get(), e = b.get(), st = c.get(), v = [];
    for (let i = s; i <= e && v.length < 60; i += st) v.push(i);
    Lib.codePanel($("#fcode"), { pseudo: [`FOR Count ← ${s} TO ${e}${st > 1 ? " STEP " + st : ""}`, "    OUTPUT Count", "NEXT Count"], py: [`for count in range(${s}, ${e + 1}${st > 1 ? ", " + st : ""}):`, "    print(count)"] });
    $("#fn").textContent = v.length; $("#fv").textContent = v.length ? v.join(", ") : "none";
    $("#fvd").innerHTML = v.length ? `The loop runs <b>${v.length}</b> time${v.length > 1 ? "s" : ""}. Count starts at ${s}${v.length > 1 ? ` and the last value is ${v[v.length - 1]}` : ""}.` : `The start (${s}) is already past the end (${e}), so the body <b>never runs</b>.`;
  };
  a = Lib.slider($("#s1"), { id: "fs", label: "Start ", min: 0, max: 10, value: 1, onInput: upd });
  b = Lib.slider($("#s2"), { id: "fe", label: "End ", min: 0, max: 20, value: 8, onInput: upd });
  c = Lib.slider($("#s3"), { id: "ft", label: "Step ", min: 1, max: 5, value: 1, onInput: upd });
  upd();
})();

/* ---------- Lab 2 ---------- */
(() => {
  Lib.slider($("#s4"), { id: "ws", label: "Starting value of Number ", min: 0, max: 6, value: 5, onInput: (n0) => {
    let w = [], r = [], n = n0; while (n < 3) { w.push(n); n++; }
    n = n0; do { r.push(n); n++; } while (!(n >= 3) && r.length < 20);
    $("#wn").textContent = w.length; $("#rn").textContent = r.length;
    $("#wo").textContent = w.join(" ") || "(nothing)"; $("#ro").textContent = r.join(" ");
    $("#wv").innerHTML = n0 >= 3 ? `Start ${n0} already meets the stopping condition. <b>WHILE never runs its body</b> (0 times). <b>REPEAT runs it once</b> before it tests.` : `Start ${n0}: both loops run ${w.length} time${w.length === 1 ? "" : "s"}. Try a start of 3 or more.`; } });
})();

/* ---------- Lab 3 ---------- */
(() => {
  let a, b;
  const upd = () => { if (!a || !b) return; const r = a.get(), c = b.get();
    $("#nout").innerHTML = Array.from({ length: r }, () => "★".repeat(c)).join("<br>");
    $("#nv").innerHTML = `The outer loop runs <b>${r}</b> times. Each time the inner loop runs <b>${c}</b> times, so the inner body runs <b>${r} × ${c} = ${r * c}</b> times in total.`; };
  a = Lib.slider($("#s5"), { id: "nr", label: "Rows (outer loop) ", min: 1, max: 6, value: 3, onInput: upd });
  b = Lib.slider($("#s6"), { id: "nc", label: "Stars per row (inner loop) ", min: 1, max: 10, value: 5, onInput: upd });
  upd();
})();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Which loop fits best?", buckets: [{ label: "FOR" }, { label: "WHILE" }, { label: "REPEAT ... UNTIL" }], items: [
  { text: "Output the 12 times table", b: 0 }, { text: "Read 30 test marks", b: 0 },
  { text: "Keep going while the player has lives left (they may have none)", b: 1 }, { text: "Count down while a number is above zero", b: 1 },
  { text: "Ask for a PIN again until it is valid", b: 2 }, { text: "Show a menu at least once, until the user chooses Quit", b: 2 }],
  done: "Known count: FOR. Might run zero times: WHILE. Must run at least once: REPEAT." });
Lib.order($("#o1"), { prompt: "Put this loop in order.", items: ["REPEAT", "INPUT Password", "UNTIL Password = \"open\"", "OUTPUT \"Welcome\""], done: "REPEAT, body, UNTIL test, then output after the loop." });
Lib.calc($("#c1"), { qs: [
  { q: "How many times does FOR Count ← 1 TO 10 run its body?", a: 10, sol: "10 − 1 + 1 = 10." },
  { q: "How many times does FOR Count ← 3 TO 9 run its body?", a: 7, sol: "3, 4, 5, 6, 7, 8, 9 is 7 values." },
  { q: "How many times does FOR Count ← 0 TO 10 STEP 2 run its body?", a: 6, sol: "0, 2, 4, 6, 8, 10 is 6 values." },
  { q: "Number ← 5. WHILE Number > 5 DO ... ENDWHILE. How many times does the body run?", a: 0, sol: "5 > 5 is FALSE at the start, so 0 times." },
  { q: "Number ← 5. REPEAT ... UNTIL Number >= 5. How many times does the body run?", a: 1, sol: "The body runs once before the test, and then 5 >= 5 is TRUE." },
  { q: "An outer loop runs 4 times and an inner loop runs 3 times each. How many times does the inner body run?", a: 12, sol: "4 × 3 = 12." }] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which loop is count-controlled?", opts: ["FOR", "WHILE", "REPEAT", "IF"], a: 0, why: "A FOR loop runs a set number of times." },
  { q: "Where does a WHILE loop test its condition?", opts: ["At the start", "At the end", "In the middle", "It never tests"], a: 0, why: "WHILE tests before each repeat." },
  { q: "A REPEAT ... UNTIL loop stops when the condition is...", opts: ["TRUE", "FALSE", "zero", "negative"], a: 0, why: "UNTIL means stop once it is TRUE." },
  { q: "What causes an infinite loop?", opts: ["The condition never becomes the stopping value", "Using a FOR loop", "A short program", "Using INPUT"], a: 0, why: "Nothing inside changes the condition." },
  { q: "In Python, range(1, 6) gives...", opts: ["1 2 3 4 5", "1 2 3 4 5 6", "0 1 2 3 4 5", "2 3 4 5 6"], a: 0, why: "range stops before the end value." }] });
Lib.cards($("#fc1"), { cards: [
  ["Iteration", "Repeating a set of instructions."],
  ["Loop", "The block of code that is repeated."],
  ["FOR loop", "A count-controlled loop that repeats a set number of times."],
  ["WHILE loop", "A condition-controlled loop that tests first and repeats while the condition is TRUE."],
  ["REPEAT ... UNTIL", "A condition-controlled loop that tests last and stops when the condition is TRUE."],
  ["Loop counter", "A variable, such as Count, that changes each time round a FOR loop."],
  ["Infinite loop", "A loop that never ends because its condition never changes."],
  ["Nested loop", "A loop inside another loop."]] });
''')
write_js("p814c", js)
