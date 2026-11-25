"""8.1.8 Maintainable programs."""
from p814k import *

BAD_PS = ["INPUT A", "INPUT B", "C ← A * B", "IF C > 100", "  THEN", "    C ← C * 0.9", "ENDIF", "OUTPUT C"]
BAD_PY = ["a = float(input())", "b = int(input())", "c = a * b", "if c > 100:", "    c = c * 0.9", "print(c)"]
GOOD_PS = ["CONSTANT DiscountLimit ← 100", "CONSTANT DiscountRate ← 0.1", "// Input one order", "INPUT TicketPrice", "INPUT Quantity", "TotalCost ← TicketPrice * Quantity", "// Large orders get a discount", "IF TotalCost > DiscountLimit", "  THEN", "    TotalCost ← TotalCost * (1 - DiscountRate)", "ENDIF", "OUTPUT TotalCost"]
GOOD_PY = ["DISCOUNT_LIMIT = 100", "DISCOUNT_RATE = 0.1", "# Input one order", "ticket_price = float(input())", "quantity = int(input())", "total_cost = ticket_price * quantity", "# Large orders get a discount", "if total_cost > DISCOUNT_LIMIT:", "    total_cost = total_cost * (1 - DISCOUNT_RATE)", "print(total_cost)"]
SUB_PS = ["// Returns the price after any discount", "FUNCTION ApplyDiscount(Cost : REAL) RETURNS REAL", "    IF Cost > 100", "      THEN", "        RETURN Cost * 0.9", "      ELSE", "        RETURN Cost", "    ENDIF", "ENDFUNCTION", "", "// Main program: two orders", "OUTPUT ApplyDiscount(80)", "OUTPUT ApplyDiscount(200)"]
SUB_PY = ["# Returns the price after any discount", "def apply_discount(cost):", "    if cost > 100:", "        return cost * 0.9", "    else:", "        return cost", "", "# Main program: two orders", "print(apply_discount(80))", "print(apply_discount(200))"]


def anim_bad():
    r = R(["A", "B", "C"])
    r.f("This program works. But what is it <b>for</b>? Watch it and try to guess. The user types 15, then 8.", [0], [0], inp=[15, 8])
    r.v["A"] = 15; r.f("<b>INPUT A</b>. A price? An age? A length?", [0], [0], hl=["A"], inp=[8])
    r.v["B"] = 8; r.f("<b>INPUT B</b>. The name tells us nothing.", [1], [1], hl=["B"], inp=[])
    r.v["C"] = 120; r.f("<b>C ← A * B</b> = 120.", [2], [2], hl=["C"])
    r.f("<b>Why 100?</b> There is no clue.", [3], [3], cond=("120 > 100", True))
    r.v["C"] = 108; r.f("<b>C ← C * 0.9</b> = 108. What does 0.9 mean?", [5], [4], hl=["C"])
    r.out.append("108"); r.f("<b>OUTPUT C</b>: 108. Correct, but hard to understand and risky to change.", [7], [5])
    return r.js()


def anim_good():
    r = R(["TicketPrice", "Quantity", "TotalCost"])
    r.f("The <b>same program</b>, written to be maintained. Constants at the top name the fixed values.", [0, 1], [0, 1], note="Limit = 100, rate = 0.1", nc="t4", inp=[15, 8])
    r.v["TicketPrice"] = 15; r.f("A <b>comment</b> says what this section does. <b>TicketPrice</b> is 15.", [2, 3], [2, 3], hl=["TicketPrice"], inp=[8])
    r.v["Quantity"] = 8; r.f("<b>INPUT Quantity</b>: 8.", [4], [4], hl=["Quantity"], inp=[])
    r.v["TotalCost"] = 120; r.f("The calculation now reads like a sentence.", [5], [5], hl=["TotalCost"])
    r.f("The comment and the name explain the test.", [6, 7], [6, 7], cond=("120 > DiscountLimit", True))
    r.v["TotalCost"] = 108; r.f("Take off the discount: <b>108</b>.", [9], [8], hl=["TotalCost"])
    r.out.append("108"); r.f("Same output, <b>108</b>. Changing the rate now means editing <b>one line</b>.", [11], [9])
    return r.js()


def anim_sub():
    r = R([])
    r.f("The discount rule is written <b>once</b>, in a function with a meaningful name and a comment.", [0, 1, 8], [0, 1], title="Main program")
    for cost, ps, py, res, line_ps, line_py in [(80, 11, 8, 80, [6], [5]), (200, 12, 9, 180, [4], [3])]:
        r.v = {}; r.f(f"<b>ApplyDiscount({cost})</b> is called.", [ps], [py], title="Main program")
        r.v = {"Cost": cost}; r.f(f"Inside the function, is {cost} > 100?", [2], [2], hl=["Cost"], title="Inside ApplyDiscount", cond=(f"{cost} > 100", cost > 100))
        r.f(f"<b>RETURN</b> {res}.", line_ps, line_py, title="Inside ApplyDiscount", note=f"returns {res}", nc="t3")
        r.v = {}; r.out.append(str(res)); r.f(f"The main program outputs <b>{res}</b>.", [ps], [py], title="Main program")
    return r.js()


learn = '''
  <h2>8.1.8 Maintainable programs</h2>
  <p>Programs are read far more often than they are written. They get fixed, improved and changed, often by someone who did not write them. A <span class="kw">maintainable program</span> is <b>easy to read, understand and change</b> without breaking it.</p>

  <h3>1 · Meaningful identifiers</h3>
  <p>An <span class="kw">identifier</span> is the name given to a variable, constant, array, procedure or function. A <b>meaningful</b> identifier says what the thing holds or does.</p>
  <div class="tw"><table class="t">
    <tr><th>Used for</th><th>Poor</th><th>Meaningful</th></tr>
    <tr><td>Variable</td><td>x</td><td>TotalMarks</td></tr>
    <tr><td>Constant</td><td>n</td><td>MaxStudents</td></tr>
    <tr><td>Array</td><td>list1</td><td>StudentName</td></tr>
    <tr><td>Procedure</td><td>p1</td><td>DisplayMenu</td></tr>
    <tr><td>Function</td><td>f</td><td>CalculateAverage</td></tr>
  </table></div>
  <div class="tip"><b class="h">Naming rules</b>Start with a letter. No spaces (join words as TotalMarks or total_marks). Do not use a keyword such as OUTPUT or FOR. Be consistent.</div>

  <h3>2 · Comments</h3>
  <p>A <span class="kw">comment</span> is a note for the human reader that the computer <b>ignores</b>. Pseudocode comments start with <span class="ln2">//</span>, Python comments with <span class="ln2">#</span>. A useful comment explains the <b>purpose</b> of a section or <b>why</b> something is done.</p>
  <div id="cdCm" class="code"></div>

  <h3>3 · Procedures and functions</h3>
  <p>Splitting a program into <b>procedures and functions</b> gives small parts that each do one job. Each can be read and tested on its own, and a repeated job is changed in <b>one place</b>.</p>
  <div id="cdSub" class="code"></div>

  <h3>Constants and layout also help</h3>
  <p>A <span class="kw">constant</span> names a value that does not change while the program runs. To change it you edit one line, and it cannot be altered by accident. <b>Indentation</b> and blank lines show the structure.</p>
  <div id="cdGood" class="code"></div>

  <div class="tw"><table class="t">
    <tr><th>Feature</th><th>How it helps the next programmer</th></tr>
    <tr><td>Meaningful identifiers</td><td>shows what each item stores or does</td></tr>
    <tr><td>Comments</td><td>explains purpose and difficult lines</td></tr>
    <tr><td>Procedures and functions</td><td>splits the program into parts that can be tested, reused and changed separately</td></tr>
    <tr><td>Constants</td><td>a fixed value is changed in one place</td></tr>
    <tr><td>Indentation and white space</td><td>shows where structures start and end</td></tr>
  </table></div>
  <div class="warn"><b class="h">Maintainable is not the same as correct or fast</b>Both programs in the Watch tab give the same output. The difference is how easily a person can work with them.</div>
'''

watch = '''  <h2>1 · A hard-to-maintain program</h2><div id="aB"></div>
  <h2>2 · The same program, maintainable</h2><div id="aG"></div>
  <h2>3 · One rule, written once in a function</h2><div id="aS"></div>
'''

explore = '''  <h2>Lab 1 · Clean up the program</h2>
  <p>Tick each improvement and watch the code change. The output never changes.</p>
  <div class="card">
    <label style="display:block"><input type="checkbox" class="imp" id="iN"> Meaningful identifiers</label>
    <label style="display:block"><input type="checkbox" class="imp" id="iK"> Constants</label>
    <label style="display:block"><input type="checkbox" class="imp" id="iC"> Comments</label>
    <label style="display:block"><input type="checkbox" class="imp" id="iF"> A function</label>
    <label style="display:block"><input type="checkbox" class="imp" id="iI"> Indentation</label>
    <div id="lcode"></div><div class="verdict" id="lv" aria-live="polite"></div>
  </div>

  <h2>Lab 2 · The price has changed</h2>
  <p>A tax rate appears in many places in a program. How many lines must be edited, with and without a constant?</p>
  <div class="card"><div id="s1"></div><div id="s2"></div><div class="readout"><div><small>Typed-in value: lines to edit</small><strong id="m1n"></strong></div><div><small>Constant: lines to edit</small><strong>1</strong></div></div><div class="verdict" id="mv" aria-live="polite"></div></div>
'''

practise = '''  <h2>1 · Good or poor identifier?</h2>
  <div id="cl1" class="card"></div>
  <h2>2 · Match the feature to its benefit</h2>
  <div id="m1" class="card"></div>
  <h2>3 · Put a program in a sensible layout</h2>
  <div id="o1" class="card"></div>
  <h2>4 · Useful comment or not?</h2>
  <div id="cl2" class="card"></div>
  <h2>5 · Multiple choice</h2>
  <div id="qz1"></div>
'''

real = (rw("A tax rate changes", "A government changes a sales tax. A shop system that stores the rate in one constant needs one edit.", "constants: change a value in one place, with less chance of missing one.")
        + rw("A new team member", "A programmer joins a project and has to fix a fault in code written years earlier.", "meaningful identifiers and comments let someone else understand the code.")
        + rw("A school system upgrade", "Only the way report grades are calculated changes. It lives in its own function.", "subroutines: one part can be changed and tested without rewriting the rest.")
        + rw("Shared libraries", "Teams publish routines with clear names and notes so that others can call them correctly.", "meaningful routine names and commenting support reuse."))

ex = [
    eq(1, "State", 3, "State three features of a <b>maintainable</b> program.", "Think names, notes and structure.",
       mk(1, "Meaningful identifiers") + " " + mk(2, "Comments") + " " + mk(3, "Procedures and functions"),
       "Writing \"it works\" or \"it is fast\". Neither makes code easier to maintain."),
    eq(2, "Explain", 2, "Explain why <b>meaningful identifiers</b> make a program easier to maintain.", "Say what the reader gains.",
       mk(1, "The name shows the purpose of the variable / routine / what it stores") + " " + mk(2, "so a programmer can understand and change the code more easily, with fewer mistakes"),
       "Saying the computer understands the names. The computer does not care."),
    eq(3, "Suggest", 3, "A program stores a student's name, the number of tests taken and whether the student has passed. Suggest a meaningful identifier for each.", "No spaces.",
       mk(1, "e.g. StudentName") + " " + mk(2, "e.g. TestCount / NumberOfTests") + " " + mk(3, "e.g. HasPassed"),
       "Using names with spaces, such as Student Name, or single letters."),
    eq(4, "Explain", 4, "Explain two ways in which using <b>procedures and functions</b> helps to maintain a program.", "Each way needs a reason.",
       mk(1, "The program is split into smaller parts") + " " + mk(2, "so each part is easier to understand and test separately") + " " + mk(3, "Repeated code is written once") + " " + mk(4, "so a change or fix only has to be made in one place"),
       "Listing two features with no explanation. \"Explain\" needs the why."),
    eq(5, "State", 2, "State the purpose of a <b>comment</b> and how it is written in pseudocode.", "Who is it for?",
       mk(1, "To explain the code to a person reading it (it is ignored when the program runs)") + " " + mk(2, "It starts with //"),
       "Saying comments are output on the screen."),
    eq(6, "Explain", 2, "Explain why <b>VatRate</b> would be declared as a constant.", "Change and safety.",
       mk(1, "The value can be changed in one place") + " " + mk(2, "and it cannot be changed by accident while the program runs"),
       "Saying a constant can never be edited by the programmer.", pre=qc(["CONSTANT VatRate ← 0.1"])),
    eq(7, "Rewrite", 5, "Rewrite this pseudocode so that it is easier to maintain. It calculates the area of a rectangle.", "Names, a comment, a declaration of what each value is.",
       mk(1, "meaningful identifier for the length") + " " + mk(2, "meaningful identifier for the width") + " " + mk(3, "meaningful identifier for the area") + " " + mk(4, "a relevant comment") + " " + mk(5, "logic unchanged: two inputs, multiply, output")
       + ac(["// Calculate the area of a rectangle", "INPUT RectangleLength", "INPUT RectangleWidth", "RectangleArea ← RectangleLength * RectangleWidth", "OUTPUT RectangleArea"]),
       "Changing what the program does while tidying it.", pre=qc(["INPUT X", "INPUT Y", "Z ← X * Y", "OUTPUT Z"])),
    eq(8, "Write", 6, "A cinema charges 12 for a ticket. Write maintainable pseudocode with a function that takes the number of tickets and returns the cost, taking 5 off when more than 4 are bought. Input the number and output the cost.", "Use constants, clear names and a comment.",
       mk(1, "constant for the ticket price (and/or discount)") + " " + mk(2, "function with a meaningful name, one parameter and RETURNS") + " " + mk(3, "cost calculated as number × price") + " " + mk(4, "IF more than 4, subtract 5, then RETURN the cost") + " " + mk(5, "INPUT, function call and OUTPUT") + " " + mk(6, "a relevant comment and meaningful identifiers throughout")
       + ac(["CONSTANT TicketPrice ← 12", "CONSTANT GroupDiscount ← 5", "", "// Returns the cost, with a discount for more than 4 tickets", "FUNCTION TicketCost(Tickets : INTEGER) RETURNS INTEGER", "    DECLARE Cost : INTEGER", "    Cost ← Tickets * TicketPrice", "    IF Tickets > 4", "      THEN", "        Cost ← Cost - GroupDiscount", "    ENDIF", "    RETURN Cost", "ENDFUNCTION", "", "INPUT NumberOfTickets", "OUTPUT TicketCost(NumberOfTickets)"]),
       "Using >= 4. \"More than 4\" means &gt; 4."),
]

tipshtml = tips([
    "<b>The three to remember:</b> meaningful identifiers, comments, procedures and functions.",
    "<b>Explain, do not just list:</b> add \"so that...\" to each feature.",
    "<b>In \"write an algorithm\" questions, use meaningful names</b> and the names given in the question exactly.",
    "<b>Comments say why or what a section is for</b>, not a copy of the line.",
    "<b>Constants are for values that stay the same</b> while the program runs.",
    "<b>Maintainability is about people</b> reading and changing code, not about speed.",
])

page("8.1.8 · Maintainable programs", "Maintainable Programs", "Meaningful identifiers, comments, procedures and functions: code that people can read and change.",
     "A program is <span class=\"kw\">maintainable</span> when another person can <b>understand it and change it safely</b>. Good names, useful comments and well-chosen <b>procedures and functions</b> make that possible.",
     learn, watch, explore, practise, real, "".join(ex), tipshtml, "p818")

js = []
consts = ", ".join(f"{n} = {json.dumps(v, ensure_ascii=False)}" for n, v in [("BAD_PS", BAD_PS), ("BAD_PY", BAD_PY), ("GOOD_PS", GOOD_PS), ("GOOD_PY", GOOD_PY), ("SUB_PS", SUB_PS), ("SUB_PY", SUB_PY)])
js.append(f'''
const {consts};
tr($("#aB"), {{ label: "Hard to maintain", pseudo: BAD_PS, py: BAD_PY, frames: {anim_bad()} }});
tr($("#aG"), {{ label: "Maintainable", pseudo: GOOD_PS, py: GOOD_PY, frames: {anim_good()} }});
tr($("#aS"), {{ label: "Using a function", pseudo: SUB_PS, py: SUB_PY, frames: {anim_sub()} }});
Lib.codePanel($("#cdCm"), {{ pseudo: ["// Add up the five test marks", "Total ← 0", "FOR Test ← 1 TO 5", "    INPUT Mark", "    Total ← Total + Mark    // keep a running total", "NEXT Test"], py: ["# Add up the five test marks", "total = 0", "for test in range(1, 6):", "    mark = int(input())", "    total = total + mark    # keep a running total"] }});
Lib.codePanel($("#cdSub"), {{ pseudo: SUB_PS, py: SUB_PY }});
Lib.codePanel($("#cdGood"), {{ pseudo: GOOD_PS, py: GOOD_PY }});
''')

js.append(r'''
/* ---------- Lab 1 ---------- */
(() => {
  const upd = () => {
    const N = $("#iN").checked, K = $("#iK").checked, C = $("#iC").checked, F = $("#iF").checked, I = $("#iI").checked;
    const build = (py) => {
      const nm = (a, b, c) => (N ? (py ? c : b) : a);
      const price = nm("a", "TicketPrice", "ticket_price"), qty = nm("b", "Quantity", "quantity"), tot = nm("c", "TotalCost", "total_cost");
      const lim = K ? (py ? "DISCOUNT_LIMIT" : "DiscountLimit") : "100", fac = K ? `(1 - ${py ? "DISCOUNT_RATE" : "DiscountRate"})` : "0.9";
      const fn = nm("f", "ApplyDiscount", "apply_discount"), p = nm("x", "Cost", "cost");
      const sp = (n) => (I || py ? " ".repeat(n) : ""), cm = (t) => { if (C) L.push((py ? "# " : "// ") + t); };
      const L = [], ar = py ? "=" : "←";
      if (K) L.push(py ? "DISCOUNT_LIMIT = 100" : "CONSTANT DiscountLimit ← 100", py ? "DISCOUNT_RATE = 0.1" : "CONSTANT DiscountRate ← 0.1");
      if (F) {
        cm("Returns the cost after any discount");
        if (py) L.push(`def ${fn}(${p}):`, `    if ${p} > ${lim}:`, `        ${p} = ${p} * ${fac}`, `    return ${p}`);
        else L.push(`FUNCTION ${fn}(${p} : REAL) RETURNS REAL`, `${sp(4)}IF ${p} > ${lim}`, `${sp(6)}THEN`, `${sp(8)}${p} ← ${p} * ${fac}`, `${sp(4)}ENDIF`, `${sp(4)}RETURN ${p}`, "ENDFUNCTION");
      }
      cm("Input one order");
      L.push(py ? `${price} = float(input())` : `INPUT ${price}`, py ? `${qty} = int(input())` : `INPUT ${qty}`, `${tot} ${ar} ${price} * ${qty}`);
      cm("Large orders get a discount");
      if (F) L.push(`${tot} ${ar} ${fn}(${tot})`);
      else if (py) L.push(`if ${tot} > ${lim}:`, `    ${tot} = ${tot} * ${fac}`);
      else L.push(`IF ${tot} > ${lim}`, `${sp(2)}THEN`, `${sp(4)}${tot} ← ${tot} * ${fac}`, "ENDIF");
      L.push(py ? `print(${tot})` : `OUTPUT ${tot}`);
      return L;
    };
    Lib.codePanel($("#lcode"), { pseudo: build(false), py: build(true) });
    const n = $$(".imp").filter((x) => x.checked).length;
    $("#lv").innerHTML = `<b>${n} of 5</b> improvements. ` + (n === 5 ? "A new programmer could understand and change this." : "Which one would help a new reader most?") + (I ? "" : " Python always needs indentation, so its tab stays indented.");
  };
  $$(".imp").forEach((x) => (x.onchange = upd)); upd();
})();

/* ---------- Lab 2 ---------- */
(() => {
  let a, b;
  const upd = () => { if (!a || !b) return; const n = a.get(), m = Math.min(b.get(), n); $("#m1n").textContent = n;
    $("#mv").innerHTML = m ? `If <b>${m}</b> line${m > 1 ? "s are" : " is"} missed, the program uses <b>two different rates</b> and gives wrong results in places. A constant avoids this.` : `All ${n} lines must be found and edited correctly. With a constant there is only one.`; };
  a = Lib.slider($("#s1"), { id: "mu", label: "Places the value is used ", min: 1, max: 40, value: 12, onInput: upd });
  b = Lib.slider($("#s2"), { id: "mm", label: "Lines the programmer misses ", min: 0, max: 5, value: 1, onInput: upd });
  upd();
})();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Sort the identifiers.", buckets: [{ label: "Meaningful" }, { label: "Poor or not allowed" }], items: [
  { text: "HighestScore", b: 0 }, { text: "CalculateTotal", b: 0 }, { text: "MaxPlayers", b: 0 }, { text: "StudentName", b: 0 },
  { text: "x1", b: 1 }, { text: "thing", b: 1 }, { text: "Total Cost", b: 1 }, { text: "OUTPUT", b: 1 }],
  done: "Good names describe the contents or the job, have no spaces and are not keywords." });
Lib.match($("#m1"), { prompt: "Drag each benefit to its feature.", pairs: [["Meaningful identifiers", "Shows what each item stores or does"], ["Comments", "Explains the purpose of a section to the reader"], ["Procedures and functions", "Lets parts be tested and reused separately"], ["Constants", "A fixed value is changed in one place"], ["Indentation", "Shows where structures start and end"]] });
Lib.order($("#o1"), { prompt: "Arrange the parts of a well-laid-out program.", items: ["// Program purpose", "CONSTANT TaxRate ← 0.1", "DECLARE Price : REAL", "FUNCTION AddTax(Cost : REAL) RETURNS REAL ... ENDFUNCTION", "INPUT Price", "OUTPUT AddTax(Price)"], done: "Purpose, constants, variables, routines, then the main program." });
Lib.classify($("#cl2"), { prompt: "Which comments would help a reader?", buckets: [{ label: "Useful" }, { label: "Not useful" }], items: [
  { text: "// Repeat until the PIN is valid", b: 0 }, { text: "// Discount applies to orders over 100", b: 0 }, { text: "// Returns the average of three marks", b: 0 },
  { text: "// This is a line of code", b: 1 }, { text: "// X", b: 1 }, { text: "// Add 1 to Count (above: Count ← Count + 1)", b: 1 }],
  done: "Useful comments explain purpose or reason, not what is already obvious." });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which is the most meaningful identifier for the number of items sold?", opts: ["ItemsSold", "n", "Data1", "Items Sold"], a: 0, why: "Descriptive and without a space." },
  { q: "What does the computer do with a comment?", opts: ["Ignores it", "Outputs it", "Stores it in a variable", "Runs it twice"], a: 0, why: "Comments are for people." },
  { q: "Which makes a repeated job easiest to change?", opts: ["Putting it in a procedure or function", "Copying it wherever it is needed", "Removing the indentation", "Using shorter names"], a: 0, why: "One place to edit." },
  { q: "Why use a constant for a fixed rate?", opts: ["It is changed in one place", "It can change while the program runs", "It makes the rate a parameter", "It stops the program needing inputs"], a: 0, why: "Easier and safer to update." }] });
Lib.cards($("#fc1"), { cards: [
  ["Maintainable program", "A program that is easy to read, understand and change."],
  ["Identifier", "The name of a variable, constant, array, procedure or function."],
  ["Meaningful identifier", "A name that describes what the item stores or does."],
  ["Comment", "A note for the reader that the computer ignores."],
  ["Constant", "A named value that does not change while the program runs."],
  ["Indentation", "Moving lines to the right to show the structure."]] });
''')
write_js("p818", js)
