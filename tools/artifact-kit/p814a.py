"""8.1.4 Sequence. python3 tools/artifact-kit/p814a.py, then assemble.py p814a "Sequence" ig-cs-sequence"""
from p814k import *

# ---------- animations ----------
def anim_ticket():
    r = R(["Price", "Quantity", "Total"]); q = [4.5, 3]
    r.f("The program runs <b>one line at a time, from the top</b>. DECLARE creates the three variables. They have no value yet.", [0, 1, 2], [], inp=list(q))
    r.v["Price"] = 4.5
    r.f("<b>INPUT Price</b>: the user types 4.5 and it is stored in Price.", [3], [0], hl=["Price"], inp=q[1:])
    r.v["Quantity"] = 3
    r.f("<b>INPUT Quantity</b>: the user types 3.", [4], [1], hl=["Quantity"], inp=[])
    r.v["Total"] = 13.5
    r.f("<b>Process.</b> Total ← 4.5 * 3 = <b>13.5</b>. Both inputs already have values, so this line works.", [5], [2], hl=["Total"], inp=[])
    r.out.append("Total cost: 13.5")
    r.f("<b>OUTPUT</b> shows the result. The last line has run, so the program ends.", [6], [3], hl=["Total"], inp=[])
    return r.js()

def anim_swap():
    r = R(["A", "B", "Temp"])
    r.v["A"] = 5; r.f("<b>A ← 5.</b>", [0], [0], hl=["A"])
    r.v["B"] = 9; r.f("<b>B ← 9.</b>", [1], [1], hl=["B"])
    r.v["Temp"] = 5; r.f("<b>Temp ← A.</b> Save A's value (5) before it is overwritten.", [2], [2], hl=["Temp"])
    r.v["A"] = 9; r.f("<b>A ← B.</b> A is now 9. The old 5 is safe in Temp.", [3], [3], hl=["A"])
    r.v["B"] = 5; r.f("<b>B ← Temp.</b> B takes the saved 5. The values have been swapped.", [4], [4], hl=["B"])
    r.out.append("9 5"); r.f("<b>OUTPUT A, B</b> shows 9 5.", [5], [5])
    return r.js()

def anim_wrong():
    r = R(["A", "B"])
    r.v["A"] = 5; r.f("<b>A ← 5.</b>", [0], [0], hl=["A"])
    r.v["B"] = 9; r.f("<b>B ← 9.</b>", [1], [1], hl=["B"])
    r.v["A"] = 9; r.f("<b>A ← B.</b> A becomes 9. The old 5 is overwritten and lost.", [2], [2], hl=["A"], note="5 has gone", nc="t2")
    r.v["B"] = 9; r.f("<b>B ← A.</b> A is already 9, so B stays 9.", [3], [3], hl=["B"], note="Both are 9", nc="t2")
    r.out.append("9 9"); r.f("<b>OUTPUT A, B</b> shows 9 9. The swap failed because there was no Temp.", [4], [4], note="Wrong", nc="t2")
    return r.js()

# ---------- sections ----------
learn = '''
  <h2>8.1.4 Sequence</h2>
  <p><span class="kw">Sequence</span> means the instructions in a program run <b>one after another, in the order they are written</b>, from the top to the bottom. Nothing is skipped and nothing is repeated. Every program uses sequence, and selection and iteration are built on top of it.</p>

  <h3>Input, process, output</h3>
  <p>Most simple programs follow the same pattern. They take in data (<span class="kw">input</span>), work something out (<span class="kw">process</span>), then show the result (<span class="kw">output</span>). A value is stored with an <b>assignment</b>: the arrow <b>←</b> means "store the value on the right in the variable on the left".</p>
  <div id="cdIPO" class="code"></div>
  <div class="tw"><table class="t">
    <tr><th>Part</th><th>Pseudocode</th><th>What it does</th></tr>
    <tr><td>Declare</td><td>DECLARE Price : REAL</td><td>Names a variable and says what type of data it holds</td></tr>
    <tr><td>Input</td><td>INPUT Price</td><td>Reads a value from the user into the variable</td></tr>
    <tr><td>Process</td><td>Total ← Price * Quantity</td><td>Works out a value and stores it</td></tr>
    <tr><td>Output</td><td>OUTPUT "Total: ", Total</td><td>Shows text and values to the user</td></tr>
  </table></div>

  <h3>The order matters</h3>
  <p>The computer cannot look ahead. A line can only use a variable that has <b>already been given a value</b> by an earlier line. Put the lines in the wrong order and the program gives an error or a wrong answer.</p>
  <div id="cdOrd" class="code"></div>
  <div class="warn"><b class="h">Order of the lines</b>If the process line came <b>before</b> the INPUT lines, Price and Quantity would have no values yet. The result would be an error, or a meaningless answer.</div>

  <h3>Swapping two values</h3>
  <p>A classic sequence problem. To swap A and B you cannot just write A ← B, because the old value of A is lost. Use a <b>temporary variable</b> to hold it, and get the three lines in the right order.</p>
  <div id="cdSwap" class="code"></div>

  <h3>Pseudocode and Python</h3>
  <div class="tw"><table class="t">
    <tr><th></th><th>Pseudocode</th><th>Python</th></tr>
    <tr><td>Assignment</td><td>Total ← 5</td><td>total = 5</td></tr>
    <tr><td>Input a whole number</td><td>INPUT Quantity</td><td>quantity = int(input())</td></tr>
    <tr><td>Input a decimal</td><td>INPUT Price</td><td>price = float(input())</td></tr>
    <tr><td>Output</td><td>OUTPUT "Total: ", Total</td><td>print("Total:", total)</td></tr>
    <tr><td>Declaring</td><td>DECLARE Total : REAL</td><td>Not needed. Python creates a variable when you first assign to it.</td></tr>
  </table></div>
  <div class="tip"><b class="h">Why int() and float()?</b>Python's input() always gives you <b>text</b>. To do arithmetic you convert it with int() for whole numbers or float() for decimals. Pseudocode does this for you because the variable was declared with a type.</div>
'''

watch = '''  <h2>1 · Input, process, output</h2><div id="aT"></div>
  <h2>2 · Swapping two values with a temporary variable</h2><div id="aS"></div>
  <h2>3 · What goes wrong without Temp</h2><div id="aW"></div>
'''

explore = '''  <h2>Lab 1 · Fix the order</h2>
  <p>This program works out a price after a discount. Use the arrows to put the lines in a working order, then see what happens. Try the order it starts in first.</p>
  <div class="card"><div id="ro"></div><div class="row" style="margin-top:8px"><button class="b" id="roShuf">Shuffle</button><button class="b pri" id="roFix">Show a working order</button></div><div class="verdict" id="roV" aria-live="polite"></div></div>

  <h2>Lab 2 · Input, process, output</h2>
  <p>Move the sliders (the inputs) and watch the process line and the output change.</p>
  <div class="card"><div id="s1"></div><div id="s2"></div><div class="scn" style="margin-top:10px"><div class="r"><b>Input</b><span class="q" id="ipI"></span></div><div class="r"><b>Process</b><span class="q" id="ipP"></span></div><div class="r"><b>Output</b><span class="q" id="ipO"></span></div></div></div>
'''

practise = '''  <h2>1 · Input, process or output?</h2>
  <div id="cl1" class="card"></div>
  <h2>2 · Put the program in order</h2>
  <div id="o1" class="card"></div>
  <h2>3 · The swap, in order</h2>
  <div id="o2" class="card"></div>
  <h2>4 · Work out the value</h2>
  <p class="note">Follow the lines in order, top to bottom.</p>
  <div id="c1"></div>
  <h2>5 · Multiple choice</h2>
  <div id="qz1"></div>
'''

real = (rw("A recipe", "Beat the eggs, add the flour, then bake. Do the steps in a different order and you get a different result, or a mess.", "sequence is a set of steps carried out in order. Say what goes wrong if the order changes.")
        + rw("An ATM withdrawal", "Insert the card, enter the PIN, choose an amount, take the cash. The machine will not let you take cash before the PIN is checked.", "the order of statements matters because later steps rely on earlier ones.")
        + rw("A calculator", "You type the first number, the operator, then the second number. The calculator then works the answer out and displays it.", "input, then process, then output.")
        + rw("Swapping seats", "Two students want to swap desks, but both desks are full. One has to put their bag down in a spare spot first.", "a temporary variable holds one value while the other is moved.")
        )

ex = [
    eq(1, "State", 1, "State what is meant by <b>sequence</b> in a program.", "One idea: in order.",
       mk(1, "Instructions are carried out one after another, in the order they are written (top to bottom)."),
       "Mixing it up with iteration. Sequence does <b>not</b> repeat anything."),
    eq(2, "Explain", 2, "Explain why the order of the statements in a program is important.", "A line can only use values that already exist.",
       mk(1, "Each statement is run in turn, so a statement may use a variable that has not been given a value yet if the order is wrong") + " " + mk(2, "which causes an error or an incorrect result (changing the order changes the output)."),
       "Saying "
       "\"the program will not work\" with no reason. Say <b>why</b>: a value is used before it is set."),
    eq(3, "Identify", 3, "Identify the line number of one <b>input</b> statement, one <b>process</b> statement and one <b>output</b> statement in the program.", "Input reads data in, process calculates, output shows.",
       mk(1, "Input: line 1 or line 2") + " " + mk(2, "Process: line 3") + " " + mk(3, "Output: line 4"),
       "Choosing line 4 as a process. Anything that only shows a value is <b>output</b>.",
       pre=qc(["INPUT Length", "INPUT Width", "Area ← Length * Width", 'OUTPUT "Area is ", Area']).replace('<span class="ln">', '<span class="ln">', 1)),
    eq(4, "Complete", 3, "The program below is run. State the final value of <b>A</b>, <b>B</b> and <b>C</b>.", "Go line by line, updating one variable at a time. Write each new value down.",
       mk(1, "C = 11 (4 + 7)") + " " + mk(2, "A = 22 (11 * 2)") + " " + mk(3, "B = 11 (22 - 11)"),
       "Using the <b>old</b> value of A on the last line. By then A has already changed to 22.",
       pre=qc(["A ← 4", "B ← 7", "C ← A + B", "A ← C * 2", "B ← A - C"])),
    eq(5, "Write", 4, "Write pseudocode to input two numbers and output their sum.", "Declare, input, process, output.",
       mk(1, "DECLARE the variables, for example DECLARE Num1, Num2, Sum : INTEGER (or REAL)") + " " + mk(2, "INPUT Num1 and INPUT Num2") + " " + mk(3, "Sum ← Num1 + Num2") + " " + mk(4, "OUTPUT Sum")
       + ac(["DECLARE Num1 : INTEGER", "DECLARE Num2 : INTEGER", "DECLARE Sum : INTEGER", "INPUT Num1", "INPUT Num2", "Sum ← Num1 + Num2", "OUTPUT Sum"]),
       "Adding before the numbers have been input, or writing <b>Num1 + Num2</b> on its own without storing or outputting it."),
    eq(6, "Complete", 2, "A program swaps the values in A and B. Write the missing line and state why Temp is needed.", "What would be lost if A ← B came first?",
       mk(1, "A ← B") + " " + mk(2, "Temp holds A's original value, otherwise it would be overwritten (lost) by A ← B."),
       "Writing <b>B ← A</b> in the gap. That would copy the value back before A has changed.",
       pre=qc(["Temp ← A", "............", "B ← Temp"])),
    eq(7, "Explain", 3, "The program below should output the cost of some tickets, but it does not work. Explain the problem and how to fix it.", "Which line uses a variable before it has a value?",
       mk(1, "Total ← Price * Quantity is run before Price and Quantity have been input") + " " + mk(2, "so they have no values (error / wrong answer)") + " " + mk(3, "Fix: move the two INPUT lines above the process line."),
       "Saying the calculation is wrong. The <b>calculation</b> is fine, the <b>order</b> is not.",
       pre=qc(["Total ← Price * Quantity", "INPUT Price", "INPUT Quantity", 'OUTPUT "Total: ", Total'])),
    eq(8, "Write", 5, "A carpet costs $12 per square metre. Write pseudocode to input the length and width of a room in metres, work out the area and the cost, and output the cost.", "Two inputs, two calculations, one output, in the right order.",
       mk(1, "INPUT Length and INPUT Width (both)") + " " + mk(2, "Area ← Length * Width") + " " + mk(3, "Cost ← Area * 12") + " " + mk(4, "OUTPUT Cost (with or without a message)") + " " + mk(5, "Statements in a correct order, with suitable variable names")
       + ac(["INPUT Length", "INPUT Width", "Area ← Length * Width", "Cost ← Area * 12", 'OUTPUT "Cost: $", Cost']),
       "Working out Cost before Area, so Area has no value yet."),
]
exam = "".join(ex)

tipshtml = tips([
    "<b>Sequence = in order.</b> One statement after another, top to bottom.",
    "<b>A variable needs a value before you use it.</b> Inputs and assignments come first.",
    "<b>Input, process, output.</b> Most simple programs follow this pattern.",
    "<b>← stores a value.</b> Read X ← Y + 1 as \"X becomes Y + 1\".",
    "<b>To swap two values you need a temporary variable.</b>",
    "<b>When tracing, write down each variable's new value after every line.</b>",
])

page("8.1.4 · Sequence", "Sequence", "Instructions that run one after another, in order: input, process, output, and why the order matters.",
     "A program is a list of instructions. <span class=\"kw\">Sequence</span> means they run <b>one after another in the order written</b>. Get the order wrong, and the program may give the wrong answer or fail.",
     learn, watch, explore, practise, real, exam, tipshtml, "p814a")

js = []
js.append(f'''
const IPO_PS = ["DECLARE Price : REAL", "DECLARE Quantity : INTEGER", "DECLARE Total : REAL", "INPUT Price", "INPUT Quantity", "Total ← Price * Quantity", 'OUTPUT "Total cost: ", Total'];
const IPO_PY = ["price = float(input())", "quantity = int(input())", "total = price * quantity", 'print("Total cost:", total)'];
const SW_PS = ["A ← 5", "B ← 9", "Temp ← A", "A ← B", "B ← Temp", "OUTPUT A, B"];
const SW_PY = ["a = 5", "b = 9", "temp = a", "a = b", "b = temp", "print(a, b)"];
const WR_PS = ["A ← 5", "B ← 9", "A ← B", "B ← A", "OUTPUT A, B"];
const WR_PY = ["a = 5", "b = 9", "a = b", "b = a", "print(a, b)"];
tr($("#aT"), {{ label: "Input, process, output", title: "Ticket cost", pseudo: IPO_PS, py: IPO_PY, dwell: 2300, frames: {anim_ticket()} }});
tr($("#aS"), {{ label: "Swapping with a temporary variable", title: "Swap A and B", pseudo: SW_PS, py: SW_PY, dwell: 2200, frames: {anim_swap()} }});
tr($("#aW"), {{ label: "A swap without Temp", title: "Wrong: no Temp", pseudo: WR_PS, py: WR_PY, dwell: 2200, frames: {anim_wrong()} }});
Lib.codePanel($("#cdIPO"), {{ pseudo: IPO_PS, py: IPO_PY }});
Lib.codePanel($("#cdOrd"), {{ pseudo: ["INPUT Price", "INPUT Quantity", "Total ← Price * Quantity", 'OUTPUT "Total: ", Total'], py: ["price = float(input())", "quantity = int(input())", "total = price * quantity", 'print("Total:", total)'] }});
Lib.codePanel($("#cdSwap"), {{ pseudo: ["Temp ← A", "A ← B", "B ← Temp"], py: ["temp = a", "a = b", "b = temp"] }});
''')

js.append(r'''
/* ---------- Lab 1: fix the order ---------- */
(() => {
  const S = [
    { ps: "Price ← 20", sets: "Price", uses: [], f: (e) => 20 },
    { ps: "Discount ← Price / 10", sets: "Discount", uses: ["Price"], f: (e) => e.Price / 10 },
    { ps: "Final ← Price - Discount", sets: "Final", uses: ["Price", "Discount"], f: (e) => e.Price - e.Discount },
    { ps: "OUTPUT Final", out: "Final", uses: ["Final"] }];
  let ord = [1, 3, 0, 2];
  const box = $("#ro"), v = $("#roV");
  function draw() {
    const env = {}; let err = -1, msg = "", outp = null;
    ord.forEach((si, pos) => {
      if (err >= 0) return; const s = S[si], miss = s.uses.find((u) => env[u] === undefined);
      if (miss) { err = pos; msg = `Line ${pos + 1} uses <b>${miss}</b>, but it has no value yet.`; return; }
      if (s.out) outp = env[s.out]; else env[s.sets] = s.f(env);
    });
    box.innerHTML = '<ol class="scn" style="list-style:none;padding:0">' + ord.map((si, pos) => `<li class="r ${err === pos ? "no" : err >= 0 && pos > err ? "" : err < 0 ? "ok" : "ok"}"><b>${pos + 1}</b><span class="q" style="font-family:var(--mono)">${esc(S[si].ps)}</span><button class="b" data-m="${pos}" data-d="-1" aria-label="Move up" ${pos === 0 ? "disabled" : ""}>↑</button><button class="b" data-m="${pos}" data-d="1" aria-label="Move down" ${pos === 3 ? "disabled" : ""}>↓</button></li>`).join("") + "</ol>";
    v.innerHTML = err >= 0 ? `<span class="kpri">Error.</span> ${msg} Move a line that gives it a value above this one.` : `<span class="kpub">It runs.</span> Output: <b>${outp}</b>. (The discount is 10% of 20, so the final price is 18.)`;
  }
  box.addEventListener("click", (e) => { const b = e.target.closest("button[data-m]"); if (!b) return; const p = +b.dataset.m, d = +b.dataset.d; [ord[p], ord[p + d]] = [ord[p + d], ord[p]]; draw(); });
  $("#roShuf").onclick = () => { do { ord = shuffle([0, 1, 2, 3]); } while (ord.join() === "0,1,2,3"); draw(); };
  $("#roFix").onclick = () => { ord = [0, 1, 2, 3]; draw(); };
  draw();
})();

/* ---------- Lab 2: input, process, output ---------- */
(() => {
  let a, b;
  const upd = () => { if (!a || !b) return; const h = a.get(), r = b.get();
    $("#ipI").innerHTML = `INPUT Hours → <b>${h}</b> &nbsp; INPUT Rate → <b>${r}</b>`;
    $("#ipP").innerHTML = `Pay ← Hours * Rate → ${h} * ${r} = <b>${h * r}</b>`;
    $("#ipO").innerHTML = `OUTPUT "Pay: $", Pay → <b>Pay: $${h * r}</b>`; };
  a = Lib.slider($("#s1"), { id: "sh", label: "Hours worked ", min: 0, max: 40, value: 25, onInput: upd });
  b = Lib.slider($("#s2"), { id: "sr", label: "Rate per hour ($) ", min: 5, max: 30, value: 12, onInput: upd });
  upd();
})();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Is each statement an input, a process or an output?", buckets: [{ label: "Input" }, { label: "Process" }, { label: "Output" }], items: [
  { text: "INPUT Age", b: 0 }, { text: "INPUT Name", b: 0 }, { text: "Read a number typed by the user", b: 0 },
  { text: "Area ← Length * Width", b: 1 }, { text: "Total ← Price * Quantity", b: 1 }, { text: "Temp ← A", b: 1 },
  { text: "OUTPUT Total", b: 2 }, { text: 'OUTPUT "Hello ", Name', b: 2 }, { text: "Show the answer on the screen", b: 2 }],
  done: "Input brings data in, process works it out, output shows it." });
Lib.order($("#o1"), { prompt: "Put these steps of an area program in order. Length is input first.", items: [
  "Declare the variables", "INPUT Length", "INPUT Width", "Area ← Length * Width", "OUTPUT Area"], done: "Declare, inputs, process, output." });
Lib.order($("#o2"), { prompt: "Put the lines of a swap of A and B in order.", items: ["Temp ← A", "A ← B", "B ← Temp"], done: "Save A, copy B into A, copy the saved value into B." });
Lib.calc($("#c1"), { qs: [
  { q: "Price ← 8, Quantity ← 5, Total ← Price * Quantity. What is Total?", a: 40, sol: "8 * 5 = 40." },
  { q: "A ← 6, B ← 4, A ← A + B, B ← A - B. What is B at the end?", a: 6, sol: "A becomes 10. Then B ← 10 - 4 = 6.", hint: "A changes on the third line, before B is worked out." },
  { q: "X ← 3, Y ← X * 2, X ← Y + 1. What is X at the end?", a: 7, sol: "Y = 6. X ← 6 + 1 = 7." },
  { q: "Hours ← 7, Rate ← 12, Pay ← Hours * Rate, Pay ← Pay + 10. What is Pay?", a: 94, sol: "7 * 12 = 84. Then 84 + 10 = 94." },
  { q: "A program has 7 lines, with no selection and no iteration. How many lines are run?", a: 7, sol: "Sequence runs every line once, in order: 7." }] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What does sequence mean?", opts: ["Instructions run in the order written", "Some instructions are skipped", "Instructions repeat", "Instructions run at random"], a: 0, why: "Sequence is one instruction after another, in order." },
  { q: "What does Total ← 5 do?", opts: ["Stores 5 in Total", "Compares Total with 5", "Outputs 5", "Inputs 5"], a: 0, why: "The arrow is assignment." },
  { q: "Which line should come first?", opts: ["INPUT Price", "Total ← Price * 2", "OUTPUT Total", "They can be in any order"], a: 0, why: "Price needs a value before it is used." },
  { q: "Why is Temp used in a swap?", opts: ["To hold a value so it is not overwritten", "To make the program faster", "To store the output", "It is not needed"], a: 0, why: "A ← B would otherwise destroy A's old value." },
  { q: "In Python, what does input() always give you?", opts: ["Text", "An integer", "A decimal", "A Boolean"], a: 0, why: "Convert with int() or float() to use it as a number." }] });
Lib.cards($("#fc1"), { cards: [
  ["Sequence", "Instructions carried out one after another, in the order they are written."],
  ["Input", "Data entered into a program, for example INPUT Age."],
  ["Process", "A calculation or other action done on the data."],
  ["Output", "Data shown to the user, for example OUTPUT Total."],
  ["Assignment", "Storing a value in a variable using ←, for example Total ← 0."],
  ["Variable", "A named memory location whose value can change while the program runs."],
  ["DECLARE", "A pseudocode statement that names a variable and gives its data type."],
  ["Temporary variable", "A variable used to hold a value while two values are swapped."]] });
''')
write_js("p814a", js)
