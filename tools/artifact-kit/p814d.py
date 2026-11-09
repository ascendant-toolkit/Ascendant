"""8.1.4 Counting and totalling."""
from p814k import *

TOT_PS = ["Total ← 0", "FOR Count ← 1 TO 5", "    INPUT Number", "    Total ← Total + Number", "NEXT Count", "OUTPUT Total"]
TOT_PY = ["total = 0", "for count in range(1, 6):", "    number = int(input())", "    total = total + number", "print(total)"]
CNT_PS = ["Count ← 0", "FOR Index ← 1 TO 5", "    INPUT Mark", "    IF Mark >= 50", "      THEN", "        Count ← Count + 1", "    ENDIF", "NEXT Index", "OUTPUT Count"]
CNT_PY = ["count = 0", "for index in range(1, 6):", "    mark = int(input())", "    if mark >= 50:", "        count = count + 1", "print(count)"]
SEN_PS = ["Total ← 0", "Count ← 0", "INPUT Number", "WHILE Number <> -1 DO", "    Total ← Total + Number", "    Count ← Count + 1", "    INPUT Number", "ENDWHILE", "Average ← Total / Count", "OUTPUT Average"]
SEN_PY = ["total = 0", "count = 0", "number = int(input())", "while number != -1:", "    total = total + number", "    count = count + 1", "    number = int(input())", "average = total / count", "print(average)"]


def anim_tot():
    q = [12, 7, 20, 5, 16]; r = R(["Count", "Number", "Total"])
    r.v["Total"] = 0; r.f("<b>Total ← 0</b> before the loop. A running total must <b>start at 0</b>.", [0], [0], hl=["Total"], inp=list(q))
    t = 0
    for i, n in enumerate(q):
        r.v["Count"] = i + 1; r.v["Number"] = n
        r.f(f"Loop {i + 1}. <b>INPUT Number</b>: {n}.", [1, 2], [1, 2], hl=["Count", "Number"], inp=q[i + 1:])
        t += n; r.v["Total"] = t
        r.f(f"<b>Total ← Total + {n}</b> = <b>{t}</b>. The new total replaces the old one.", [3], [3], hl=["Total"], inp=q[i + 1:])
    r.out.append(str(t)); r.f(f"The loop has finished. <b>OUTPUT Total</b> shows <b>{t}</b>, once, after the loop.", [5], [4], hl=["Total"], inp=[])
    return r.js()


def anim_cnt():
    q = [62, 45, 78, 50, 31]; r = R(["Index", "Mark", "Count"])
    r.v["Count"] = 0; r.f("<b>Count ← 0</b> before the loop. A count <b>starts at 0</b>.", [0], [0], hl=["Count"], inp=list(q))
    c = 0
    for i, m in enumerate(q):
        r.v["Index"] = i + 1; r.v["Mark"] = m
        r.f(f"Loop {i + 1}. <b>INPUT Mark</b>: {m}.", [1, 2], [1, 2], hl=["Index", "Mark"], inp=q[i + 1:])
        ok = m >= 50
        r.f(f"Is {m} >= 50?", [3], [3], cond=(f"{m} >= 50", ok), inp=q[i + 1:])
        if ok:
            c += 1; r.v["Count"] = c
            r.f(f"TRUE, so <b>Count ← Count + 1</b> = <b>{c}</b>. Counting adds <b>1</b>, not the mark.", [5], [4], hl=["Count"], cond=(f"{m} >= 50", True), inp=q[i + 1:])
    r.out.append(str(c)); r.f(f"After the loop, <b>OUTPUT Count</b>: <b>{c}</b> marks were 50 or more.", [8], [5], hl=["Count"], inp=[])
    return r.js()


def anim_sen():
    q = [8, 5, 11, -1]; r = R(["Number", "Total", "Count", "Average"])
    r.v["Total"] = 0; r.v["Count"] = 0; r.f("Set <b>Total</b> and <b>Count</b> to 0. The user will stop the program by typing <b>-1</b> (a <span class=\"kw\">sentinel</span>).", [0, 1], [0, 1], hl=["Total", "Count"], inp=list(q))
    r.v["Number"] = 8; r.f("<b>INPUT Number</b> before the loop: 8.", [2], [2], hl=["Number"], inp=q[1:])
    t = c = 0
    for i, n in enumerate(q[:3]):
        r.f(f"Is {n} <> -1? Yes, so the loop runs.", [3], [3], cond=(f"{n} <> -1", True), inp=q[i + 1:])
        t += n; c += 1; r.v["Total"] = t; r.v["Count"] = c
        r.f(f"<b>Total ← Total + {n}</b> = {t}. <b>Count ← Count + 1</b> = {c}.", [4, 5], [4, 5], hl=["Total", "Count"], inp=q[i + 1:])
        r.v["Number"] = q[i + 1]
        r.f(f"<b>INPUT Number</b> again, at the <b>end</b> of the loop body: {q[i + 1]}.", [6], [6], hl=["Number"], inp=q[i + 2:])
    r.f("Is -1 <> -1? No, so the loop ends. The -1 is <b>not</b> added to the total.", [3, 7], [3], cond=("-1 <> -1", False), inp=[])
    r.v["Average"] = t // c if t % c == 0 else round(t / c, 2)
    r.f(f"<b>Average ← Total / Count</b> = {t} / {c} = <b>{r.v['Average']}</b>.", [8], [7], hl=["Average"])
    r.out.append(str(r.v["Average"])); r.f(f"<b>OUTPUT Average</b>: {r.v['Average']}.", [9], [8], hl=["Average"])
    return r.js()


learn = '''
  <h2>8.1.4 Counting and totalling</h2>
  <p>Programs often need to keep track of something as they run. <span class="kw">Totalling</span> adds up values. <span class="kw">Counting</span> works out how many times something happens. Both use a variable that <b>changes inside a loop</b>, so they build on iteration, and counting often uses selection too.</p>

  <h3>Totalling</h3>
  <p>A <span class="kw">running total</span> starts at <b>0</b>. Inside the loop, each new value is <b>added</b> to it. The new total is stored back in the same variable.</p>
  <div id="cdTot" class="code"></div>

  <h3>Counting</h3>
  <p>A <span class="kw">count</span> starts at <b>0</b>. Each time something happens, <b>1 is added</b>. Counting always adds <b>1</b>. Totalling adds the <b>value</b>.</p>
  <div id="cdCnt" class="code"></div>
  <div class="tw"><table class="t">
    <tr><th></th><th>Totalling</th><th>Counting</th></tr>
    <tr><td>Start value</td><td>Total ← 0</td><td>Count ← 0</td></tr>
    <tr><td>Inside the loop</td><td>Total ← Total + Number</td><td>Count ← Count + 1</td></tr>
    <tr><td>Adds</td><td>the value of the data</td><td>always 1</td></tr>
    <tr><td>Answers</td><td>"What is the sum?"</td><td>"How many?"</td></tr>
  </table></div>

  <h3>Initialise before the loop, output after it</h3>
  <p>Setting a variable to its starting value is called <span class="kw">initialising</span>. Do it <b>before</b> the loop. If it is inside the loop, it is reset to 0 on every repeat. Output the answer <b>after</b> the loop, when the total is complete.</p>
  <div class="warn"><b class="h">Two classic mistakes</b><b>Not setting Total or Count to 0</b> (it holds a leftover or missing value). <b>Putting OUTPUT inside the loop</b>, which shows a half-finished total on every repeat.</div>

  <h3>Counting and totalling with a sentinel</h3>
  <p>If you do not know how many values there will be, use a loop that stops on a special value, called a <span class="kw">sentinel</span> (for example -1). Total and count as you go, then work out the <b>average</b> = Total / Count after the loop. The sentinel is not part of the data, so it is never added.</p>
  <div id="cdSen" class="code"></div>
  <div class="tip"><b class="h">The input before the loop</b>The first INPUT comes <b>before</b> the WHILE so there is a value to test. The next INPUT goes at the <b>end</b> of the loop body.</div>

  <h3>Pseudocode and Python</h3>
  <p>The logic is identical. Python's <code>total += number</code> is a short way to write <code>total = total + number</code>, and you may see it in other code. In pseudocode, use the full form.</p>
'''

watch = '''  <h2>1 · Totalling five numbers</h2><div id="aT"></div>
  <h2>2 · Counting marks of 50 or more</h2><div id="aC"></div>
  <h2>3 · Totalling and counting until -1, then the average</h2><div id="aS"></div>
'''

explore = '''  <h2>Lab 1 · The till</h2>
  <p>Type some prices (separated by spaces). The program totals them, counts them and counts the expensive ones. Move the slider to change what counts as expensive.</p>
  <div class="card"><input class="ipin" id="pi" type="text" value="3.5 12 8 2.25 15 6" maxlength="60" aria-label="Prices" spellcheck="false"><div id="s1"></div><div class="readout"><div><small>Total</small><strong id="pt"></strong></div><div><small>Count (all items)</small><strong id="pc"></strong></div><div><small>Count over limit</small><strong id="po"></strong></div><div><small>Average</small><strong id="pa"></strong></div></div><div class="verdict" id="pv" aria-live="polite"></div></div>

  <h2>Lab 2 · Break the program</h2>
  <p>The numbers 4, 6 and 5 are input. Choose the faulty versions and see the wrong results. The correct version is the first choice in each box.</p>
  <div class="card"><div class="row"><label for="b1">Start values&nbsp;</label><select class="sel" id="b1"><option value="ok">Total ← 0, Count ← 0</option><option value="none">Total never set</option><option value="ten">Total ← 10</option><option value="inloop">Total ← 0 inside the loop</option></select></div>
  <div class="row" style="margin-top:6px"><label for="b2">Counting line&nbsp;</label><select class="sel" id="b2"><option value="ok">Count ← Count + 1</option><option value="val">Count ← Count + Number</option></select></div>
  <div class="row" style="margin-top:6px"><label for="b3">OUTPUT&nbsp;</label><select class="sel" id="b3"><option value="after">after the loop</option><option value="in">inside the loop</option></select></div>
  <div id="bcode"></div><div class="out" id="bout" style="min-height:46px;margin-top:8px"></div><div class="verdict" id="bv" aria-live="polite"></div></div>

  <h2>Lab 3 · Pass and fail counters</h2>
  <p>Two counters, one pass mark. Pass + Fail always equals the number of marks.</p>
  <div class="card"><input class="ipin" id="mi" type="text" value="62 45 78 50 31 91 40" maxlength="60" aria-label="Marks" spellcheck="false"><div id="s2"></div><div class="readout"><div><small>Pass</small><strong id="mp"></strong></div><div><small>Fail</small><strong id="mf"></strong></div><div><small>Marks</small><strong id="mt"></strong></div></div><div class="verdict" id="mv" aria-live="polite"></div></div>
'''

practise = '''  <h2>1 · Totalling, counting or initialising?</h2>
  <div id="cl1" class="card"></div>
  <h2>2 · Average of a list until -1, in order</h2>
  <div id="o1" class="card"></div>
  <h2>3 · Calculations</h2>
  <div id="c1"></div>
  <h2>4 · Multiple choice</h2>
  <div id="qz1"></div>
'''

real = (rw("A supermarket till", "As each item is scanned, its price is added to the bill and the number of items goes up by one.", "totalling adds the value, counting adds 1. A till does both in the same loop.")
        + rw("A school's attendance system", "A program counts how many students were present, then divides by the class size to find the percentage.", "counting with a condition: Count goes up only when the student was present.")
        + rw("A step counter", "A fitness band adds 1 to a counter every time it detects a step.", "counting starts at 0 and adds 1 each time an event happens.")
        + rw("Exam results", "A teacher totals everyone's marks, divides by the number of students for the average, and counts how many passed.", "totalling, counting and average in a single loop.")
        )

ex = [
    eq(1, "State", 2, "State what is meant by <b>totalling</b> and by <b>counting</b> in a program.", "One adds the values, the other adds 1.",
       mk(1, "Totalling: keeping a running total by adding each value to it") + " " + mk(2, "Counting: adding 1 to a variable each time something happens."),
       "Saying counting \"adds up the numbers\". Counting adds <b>1</b> each time."),
    eq(2, "Write", 4, "Write pseudocode to input 10 numbers and output their total.", "Initialise, loop, input and add, then output.",
       mk(1, "Total ← 0 before the loop") + " " + mk(2, "FOR Count ← 1 TO 10 ... NEXT Count") + " " + mk(3, "INPUT Number and Total ← Total + Number inside the loop") + " " + mk(4, "OUTPUT Total after the loop")
       + ac(["Total ← 0", "FOR Count ← 1 TO 10", "    INPUT Number", "    Total ← Total + Number", "NEXT Count", "OUTPUT Total"]),
       "Forgetting to set Total to 0, or putting OUTPUT inside the loop."),
    eq(3, "Write", 4, "25 temperatures are input. Write pseudocode to count how many are below 0 and output the count.", "Counting with a condition: the count goes up only when the test is TRUE.",
       mk(1, "Count ← 0 before the loop") + " " + mk(2, "FOR loop of 25 repeats with INPUT Temperature inside") + " " + mk(3, "IF Temperature < 0 THEN Count ← Count + 1 ENDIF") + " " + mk(4, "OUTPUT Count after the loop")
       + ac(["Count ← 0", "FOR Index ← 1 TO 25", "    INPUT Temperature", "    IF Temperature < 0", "      THEN", "        Count ← Count + 1", "    ENDIF", "NEXT Index", "OUTPUT Count"]),
       "Writing Count ← Count + Temperature, which totals instead of counting."),
    eq(4, "Write", 6, "Write pseudocode to input numbers until -1 is entered. Output the total and the average of the numbers. Do not include -1.", "Sentinel loop: first input before WHILE, next input at the end of the loop.",
       mk(1, "Total ← 0 and Count ← 0 before the loop") + " " + mk(2, "INPUT Number before the loop") + " " + mk(3, "WHILE Number <> -1") + " " + mk(4, "Total ← Total + Number and Count ← Count + 1 inside the loop") + " " + mk(5, "INPUT Number again at the end of the loop") + " " + mk(6, "Average ← Total / Count and OUTPUT Total, Average after the loop")
       + ac(SEN_PS[:9] + ["OUTPUT Total, Average"]),
       "Adding -1 to the total, which happens if you add before testing the input."),
    eq(5, "Identify", 4, "The code should output the total of 10 numbers. Identify two errors and correct them.", "Where should Total be set, and where should it be output?",
       mk(1, "Error: Total is never initialised (set to 0)") + " " + mk(2, "Fix: Total ← 0 before the loop") + " " + mk(3, "Error: OUTPUT Total is inside the loop (it shows a running total every time)") + " " + mk(4, "Fix: move OUTPUT Total to after NEXT Index."),
       "Saying INPUT is the problem. The INPUT is in the right place.",
       pre=qc(["FOR Index ← 1 TO 10", "    INPUT Number", "    Total ← Total + Number", "    OUTPUT Total", "NEXT Index"])),
    eq(6, "Complete", 4, "The code is run with the inputs 12, 7, 20 and 5. Complete the final values of Total and Count and state the output.", "Only numbers over 10 are counted. Everything is totalled.",
       mk(1, "Total: 12, 19, 39, 44 (final 44)") + " " + mk(2, "Count: 1, 1, 2, 2 (final 2)") + " " + mk(3, "OUTPUT 44") + " " + mk(4, "OUTPUT 2 (after the total)"),
       "Counting every number. Count only goes up when Number > 10.",
       pre=qc(["Total ← 0", "Count ← 0", "FOR Index ← 1 TO 4", "    INPUT Number", "    Total ← Total + Number", "    IF Number > 10", "      THEN", "        Count ← Count + 1", "    ENDIF", "NEXT Index", "OUTPUT Total", "OUTPUT Count"])),
    eq(7, "Write", 5, "20 marks are input. A mark of 40 or more is a pass. Write pseudocode to count the passes and the fails, and output both counts.", "Two counters, both set to 0 before the loop.",
       mk(1, "Pass ← 0 and Fail ← 0 before the loop") + " " + mk(2, "FOR loop of 20 with INPUT Mark inside") + " " + mk(3, "IF Mark >= 40 THEN Pass ← Pass + 1") + " " + mk(4, "ELSE Fail ← Fail + 1 ... ENDIF") + " " + mk(5, "OUTPUT Pass and OUTPUT Fail after the loop")
       + ac(["Pass ← 0", "Fail ← 0", "FOR Index ← 1 TO 20", "    INPUT Mark", "    IF Mark >= 40", "      THEN", "        Pass ← Pass + 1", "      ELSE", "        Fail ← Fail + 1", "    ENDIF", "NEXT Index", "OUTPUT Pass", "OUTPUT Fail"]),
       "Using 40 as the test but writing &gt; 40, which misses a mark of exactly 40."),
    eq(8, "Explain", 2, "Explain why Count must be set to 0 before the loop starts.", "What would Count hold otherwise?",
       mk(1, "Otherwise it would have no value (or an old value), so the count would be wrong / an error") + " " + mk(2, "Count ← Count + 1 needs a starting value to add to."),
       "Saying \"because it is a rule\". Explain what goes <b>wrong</b>."),
    eq(9, "Write", 7, "A shop till reads item prices until 0 is entered. Write pseudocode to output the total cost, the number of items and how many items cost more than $10. Do not count the 0.", "Three results from one loop: total, count, conditional count.",
       mk(1, "Total ← 0, Items ← 0 and Expensive ← 0 before the loop") + " " + mk(2, "INPUT Price before the loop") + " " + mk(3, "WHILE Price <> 0") + " " + mk(4, "Total ← Total + Price and Items ← Items + 1") + " " + mk(5, "IF Price > 10 THEN Expensive ← Expensive + 1 ENDIF") + " " + mk(6, "INPUT Price at the end of the loop") + " " + mk(7, "OUTPUT Total, Items and Expensive after the loop")
       + ac(["Total ← 0", "Items ← 0", "Expensive ← 0", "INPUT Price", "WHILE Price <> 0 DO", "    Total ← Total + Price", "    Items ← Items + 1", "    IF Price > 10", "      THEN", "        Expensive ← Expensive + 1", "    ENDIF", "    INPUT Price", "ENDWHILE", "OUTPUT Total", "OUTPUT Items", "OUTPUT Expensive"]),
       "Putting the second INPUT Price at the top of the loop, so the sentinel 0 is added to the total."),
]
exam = "".join(ex)

tipshtml = tips([
    "<b>Total and Count start at 0.</b> Set them <b>before</b> the loop.",
    "<b>Counting adds 1. Totalling adds the value.</b>",
    "<b>Output after the loop.</b> Inside it you only see a running total.",
    "<b>Count with a condition: put the Count ← Count + 1 inside an IF.</b>",
    "<b>Average = Total / Count</b>, worked out after the loop.",
    "<b>With a sentinel, never add the sentinel.</b> Input once before the loop and again at the end of the body.",
])

page("8.1.4 · Counting and totalling", "Counting and Totalling", "Running totals, counters and averages: how a variable keeps track of data inside a loop.",
     "<span class=\"kw\">Totalling</span> adds up values. <span class=\"kw\">Counting</span> adds 1 each time something happens. Both start at 0 before a loop, change inside it, and are output after it.",
     learn, watch, explore, practise, real, exam, tipshtml, "p814d")

js = []
js.append(f'''
const TOT_PS = {json.dumps(TOT_PS, ensure_ascii=False)}, TOT_PY = {json.dumps(TOT_PY, ensure_ascii=False)};
const CNT_PS = {json.dumps(CNT_PS, ensure_ascii=False)}, CNT_PY = {json.dumps(CNT_PY, ensure_ascii=False)};
const SEN_PS = {json.dumps(SEN_PS, ensure_ascii=False)}, SEN_PY = {json.dumps(SEN_PY, ensure_ascii=False)};
tr($("#aT"), {{ label: "Totalling", title: "Running total", pseudo: TOT_PS, py: TOT_PY, dwell: 1900, frames: {anim_tot()} }});
tr($("#aC"), {{ label: "Counting", title: "Counting marks >= 50", pseudo: CNT_PS, py: CNT_PY, dwell: 1900, frames: {anim_cnt()} }});
tr($("#aS"), {{ label: "Sentinel loop and average", title: "Sentinel -1", pseudo: SEN_PS, py: SEN_PY, dwell: 2100, frames: {anim_sen()} }});
Lib.codePanel($("#cdTot"), {{ pseudo: TOT_PS, py: TOT_PY }});
Lib.codePanel($("#cdCnt"), {{ pseudo: CNT_PS, py: CNT_PY }});
Lib.codePanel($("#cdSen"), {{ pseudo: SEN_PS, py: SEN_PY }});
''')

js.append(r'''
/* ---------- Lab 1 ---------- */
(() => {
  let sl; const inp = $("#pi");
  const upd = () => {
    if (!sl) return; const D = nums(inp.value, 20), lim = sl.get();
    if (!D.length) { ["pt", "pc", "po", "pa"].forEach((i) => ($("#" + i).textContent = "–")); $("#pv").textContent = "Enter some prices."; return; }
    const t = D.reduce((a, b) => a + b, 0), c = D.filter((x) => x > lim).length;
    $("#pt").textContent = fmtN(t, 2); $("#pc").textContent = D.length; $("#po").textContent = c; $("#pa").textContent = fmtN(t / D.length, 2);
    $("#pv").innerHTML = `<b>Total</b> adds each price: ${fmtN(t, 2)}. <b>Count</b> adds 1 per item: ${D.length}. <b>Count over $${lim}</b> adds 1 only when Price > ${lim}: ${c}. Average = ${fmtN(t, 2)} / ${D.length} = ${fmtN(t / D.length, 2)}.`;
  };
  sl = Lib.slider($("#s1"), { id: "pl", label: "Expensive means over $", min: 0, max: 20, value: 10, onInput: upd });
  inp.addEventListener("input", upd); upd();
})();

/* ---------- Lab 2 ---------- */
(() => {
  const D = [4, 6, 5];
  function upd() {
    const a = $("#b1").value, b = $("#b2").value, c = $("#b3").value;
    const ps = [a === "ten" ? "Total ← 10" : a === "none" ? "(Total is never set)" : "Total ← 0", "Count ← 0", "FOR Index ← 1 TO 3"];
    if (a === "inloop") ps.push("    Total ← 0");
    ps.push("    INPUT Number", "    Total ← Total + Number", b === "ok" ? "    Count ← Count + 1" : "    Count ← Count + Number");
    if (c === "in") ps.push("    OUTPUT Total, Count");
    ps.push("NEXT Index"); if (c === "after") ps.push("OUTPUT Total, Count");
    const py = [a === "ten" ? "total = 10" : a === "none" ? "# total is never set" : "total = 0", "count = 0", "for index in range(3):"];
    if (a === "inloop") py.push("    total = 0");
    py.push("    number = int(input())", "    total = total + number", b === "ok" ? "    count = count + 1" : "    count = count + number");
    if (c === "in") py.push("    print(total, count)");
    if (c === "after") py.push("print(total, count)");
    Lib.codePanel($("#bcode"), { pseudo: ps, py });
    let t = a === "ten" ? 10 : a === "none" ? undefined : 0, n = 0, outs = [], err = false;
    for (const x of D) { if (a === "inloop") t = 0; if (t === undefined) { err = true; break; } t += x; n += b === "ok" ? 1 : x; if (c === "in") outs.push(`${t} ${n}`); }
    if (!err && c === "after") outs.push(`${t} ${n}`);
    $("#bout").innerHTML = err ? `<span class="kpri">Error: Total has no value when Total + Number is worked out.</span>` : outs.join("<br>");
    const good = a === "ok" && b === "ok" && c === "after";
    $("#bv").innerHTML = good ? `<span class="kpub">Correct.</span> Total 15 (4 + 6 + 5) and Count 3 (three numbers).` :
      [a === "ten" ? "Total started at 10, so every total is 10 too high." : "", a === "inloop" ? "Total is reset to 0 on every repeat, so only the last number survives." : "", a === "none" ? "A variable must be given a start value." : "", b === "val" ? "Count adds the <b>value</b> instead of 1, so it is totalling, not counting." : "", c === "in" ? "OUTPUT inside the loop shows a running total on every repeat." : ""].filter(Boolean).join(" ");
  }
  ["b1", "b2", "b3"].forEach((i) => ($("#" + i).onchange = upd)); upd();
})();

/* ---------- Lab 3 ---------- */
(() => {
  let sl; const inp = $("#mi");
  const upd = () => {
    if (!sl) return; const D = nums(inp.value, 20), pm = sl.get();
    if (!D.length) { ["mp", "mf", "mt"].forEach((i) => ($("#" + i).textContent = "–")); $("#mv").textContent = "Enter some marks."; return; }
    const p = D.filter((x) => x >= pm).length;
    $("#mp").textContent = p; $("#mf").textContent = D.length - p; $("#mt").textContent = D.length;
    $("#mv").innerHTML = `Marks of ${pm} or more add 1 to <b>Pass</b>. All the others add 1 to <b>Fail</b>. ${p} + ${D.length - p} = ${D.length}.`;
  };
  sl = Lib.slider($("#s2"), { id: "pm", label: "Pass mark ", min: 0, max: 100, value: 50, onInput: upd });
  inp.addEventListener("input", upd); upd();
})();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Sort each statement.", buckets: [{ label: "Totalling" }, { label: "Counting" }, { label: "Initialising" }], items: [
  { text: "Total ← Total + Price", b: 0 }, { text: "Sum ← Sum + Number", b: 0 },
  { text: "Count ← Count + 1", b: 1 }, { text: "Pass ← Pass + 1", b: 1 },
  { text: "Total ← 0", b: 2 }, { text: "Count ← 0", b: 2 }, { text: "Fail ← 0", b: 2 }],
  done: "Initialise to 0, add the value to total, add 1 to count." });
Lib.order($("#o1"), { prompt: "Put the steps of the average algorithm in order.", items: [
  "Total ← 0 and Count ← 0", "INPUT Number", "WHILE Number <> -1", "Add Number to Total and 1 to Count, then INPUT the next Number", "ENDWHILE, then Average ← Total / Count"], done: "Initialise, first input, test, body, after the loop." });
Lib.calc($("#c1"), { qs: [
  { q: "The numbers 4, 9, 2 and 7 are totalled. What is the final Total?", a: 22, sol: "4 + 9 + 2 + 7 = 22." },
  { q: "How many of 12, 7, 20, 5 and 16 are greater than 10?", a: 3, sol: "12, 20 and 16: 3." },
  { q: "What is the average of 8, 5 and 11?", a: 8, sol: "24 / 3 = 8." },
  { q: "A loop runs 8 times and contains Count ← Count + 1 with no IF. What is Count at the end (starting from 0)?", a: 8, sol: "1 is added on each of the 8 repeats." },
  { q: "Total was wrongly started at 10. The inputs 3 and 4 are added. What is Total at the end?", a: 17, sol: "10 + 3 + 4 = 17. It should be 7." },
  { q: "Numbers are input until -1. The user types 5, 9, 4, -1. What is Count at the end?", a: 3, sol: "Only 5, 9 and 4 are counted. The sentinel -1 is not." }] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What should a running total start at?", opts: ["0", "1", "The first number", "-1"], a: 0, why: "Start at 0 so the first value is added to nothing." },
  { q: "What does Count ← Count + 1 do?", opts: ["Adds 1 to the count", "Adds the input to the count", "Resets Count", "Outputs Count"], a: 0, why: "Counting adds 1 each time." },
  { q: "Where should OUTPUT Total normally go?", opts: ["After the loop", "Inside the loop", "Before the loop", "It does not matter"], a: 0, why: "After the loop the total is complete." },
  { q: "A sentinel value is...", opts: ["A special value that ends the input", "The largest number", "The first number", "A loop counter"], a: 0, why: "For example -1 signals that there is no more data." },
  { q: "Average is worked out as...", opts: ["Total / Count", "Total * Count", "Total + Count", "Count / Total"], a: 0, why: "The total divided by how many values there were." }] });
Lib.cards($("#fc1"), { cards: [
  ["Totalling", "Keeping a running total by adding each value to it, starting at 0."],
  ["Counting", "Adding 1 to a variable each time something happens, starting at 0."],
  ["Running total", "A total that is updated each time round a loop."],
  ["Initialise", "Give a variable its starting value before the loop."],
  ["Sentinel", "A special value, such as -1, typed to show there is no more data."],
  ["Average", "The total divided by the number of values (Total / Count)."],
  ["Counter", "A variable used to count, for example Count or Pass."]] });
''')
write_js("p814d", js)
