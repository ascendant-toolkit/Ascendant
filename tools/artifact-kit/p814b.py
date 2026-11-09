"""8.1.4 Selection."""
from p814k import *

G_PS = ["INPUT Mark", "IF Mark >= 70", "  THEN", '    OUTPUT "Grade A"', "  ELSE", "    IF Mark >= 50", "      THEN", '        OUTPUT "Grade B"', "      ELSE", '        OUTPUT "Grade C"', "    ENDIF", "ENDIF"]
G_PY = ["mark = int(input())", "if mark >= 70:", '    print("Grade A")', "elif mark >= 50:", '    print("Grade B")', "else:", '    print("Grade C")']


def anim_ifelse():
    r = R(["Mark"]); q = [62]
    r.f("The program starts. Mark has no value yet.", [0], [], inp=[62])
    r.v["Mark"] = 62; r.f("<b>INPUT Mark</b>: the user types 62.", [1], [0], hl=["Mark"], inp=[])
    r.f("The <b>condition</b> is tested. Is 62 >= 50? It is.", [2], [1], cond=("Mark >= 50", True))
    r.f("The condition is TRUE, so the <b>THEN</b> branch runs. The ELSE branch is skipped.", [3], [2], cond=("Mark >= 50", True))
    r.out.append("Pass"); r.f("<b>OUTPUT \"Pass\"</b>. The program then jumps to after ENDIF.", [4], [2], cond=("Mark >= 50", True))
    r.f("<b>ENDIF</b>: the selection is over. Only <b>one</b> of the two branches ever runs.", [7], [], note="THEN branch ran, ELSE did not", nc="t3")
    return r.js()


def anim_nested():
    r = R(["Mark"])
    r.f("Three possible outcomes need <b>more than one test</b>. Mark is going to be 58.", [0], [], inp=[58])
    r.v["Mark"] = 58; r.f("<b>INPUT Mark</b>: 58.", [0], [0], hl=["Mark"], inp=[])
    r.f("First test: is 58 >= 70? No.", [1], [1], cond=("Mark >= 70", False))
    r.f("FALSE, so jump to <b>ELSE</b>. Another test is inside it.", [4, 5], [3], cond=("Mark >= 70", False))
    r.f("Second test: is 58 >= 50? Yes.", [5], [3], cond=("Mark >= 50", True))
    r.f("TRUE, so this THEN runs.", [6, 7], [4], cond=("Mark >= 50", True))
    r.out.append("Grade B"); r.f("<b>OUTPUT \"Grade B\"</b>. The last ELSE is skipped.", [7], [4], cond=("Mark >= 50", True))
    r.f("Both ENDIFs close the selection. Tests run <b>top to bottom</b> and the first TRUE one wins.", [10, 11], [], note="Grade B", nc="t3")
    return r.js()


def anim_case():
    r = R(["Choice"])
    r.f("A menu: 1 Play, 2 Options, 3 Quit. The user will choose 2.", [0], [], inp=[2])
    r.v["Choice"] = 2; r.f("<b>INPUT Choice</b>: 2.", [0], [0], hl=["Choice"], inp=[])
    r.f("<b>CASE OF Choice</b> compares Choice with each value in turn. Is it 1? No.", [1, 2], [1], cond=("Choice = 1", False))
    r.f("Is it 2? Yes.", [3], [3], cond=("Choice = 2", True))
    r.out.append("Options"); r.f("A match, so this line runs: <b>OUTPUT \"Options\"</b>. The remaining cases are skipped.", [3], [4], cond=("Choice = 2", True))
    r.f("<b>ENDCASE</b>. OTHERWISE would only have run if <b>no value</b> had matched.", [6], [], note="Matched case 2", nc="t3")
    return r.js()


learn = '''
  <h2>8.1.4 Selection</h2>
  <p><span class="kw">Selection</span> lets a program <b>choose</b> what to do. It tests a <span class="kw">condition</span>. A condition is something that is either <b>TRUE</b> or <b>FALSE</b>, such as <code>Mark >= 50</code>. The result decides which lines run.</p>

  <h3>IF ... THEN ... ENDIF</h3>
  <p>The simplest form. The lines inside run <b>only if</b> the condition is TRUE. If it is FALSE the program carries on after ENDIF.</p>
  <div id="cdIf" class="code"></div>

  <h3>IF ... THEN ... ELSE ... ENDIF</h3>
  <p>Two routes. One runs if the condition is TRUE, the other (ELSE) if it is FALSE. <b>Exactly one</b> of them runs.</p>
  <div id="cdIfElse" class="code"></div>

  <h3>Nested IF</h3>
  <p>An IF placed inside another IF handles <b>three or more</b> outcomes. The tests run from the top. The <b>first</b> one that is TRUE wins, so the order of the tests matters.</p>
  <div id="cdNest" class="code"></div>
  <div class="warn"><b class="h">Order of the tests</b>If you test <code>Mark >= 50</code> <b>first</b>, then a mark of 85 matches straight away and the test for 70 is never reached. Test the <b>hardest</b> condition first.</div>

  <h3>CASE OF</h3>
  <p>When <b>one variable</b> is compared with several fixed values, CASE OF is tidier than a pile of nested IFs. OTHERWISE catches anything that did not match.</p>
  <div id="cdCase" class="code"></div>

  <h3>Comparing values</h3>
  <p>Conditions use <span class="kw">comparison operators</span>. (You will meet the full set of operators later in this chapter. These six are all you need for now.)</p>
  <div class="tw"><table class="t">
    <tr><th>Meaning</th><th>Pseudocode</th><th>Python</th></tr>
    <tr><td>equal to</td><td>=</td><td>==</td></tr>
    <tr><td>not equal to</td><td>&lt;&gt;</td><td>!=</td></tr>
    <tr><td>less than / greater than</td><td>&lt;  &gt;</td><td>&lt;  &gt;</td></tr>
    <tr><td>less than or equal / greater than or equal</td><td>&lt;=  &gt;=</td><td>&lt;=  &gt;=</td></tr>
  </table></div>
  <div class="tip"><b class="h">Pseudocode and Python</b>In pseudocode, <b>=</b> compares and <b>←</b> assigns. In Python, <b>==</b> compares and <b>=</b> assigns. Python has no ENDIF: the lines <b>inside</b> the IF are <b>indented</b>, and the colon <b>:</b> ends the condition line. ELSE IF is written <b>elif</b>. Python has no CASE OF in the exam, so use if/elif/else (newer versions also have <b>match</b>).</div>
'''

watch = '''  <h2>1 · IF ... THEN ... ELSE</h2><div id="aI"></div>
  <h2>2 · A nested IF with three outcomes</h2><div id="aN"></div>
  <h2>3 · CASE OF</h2><div id="aC"></div>
'''

explore = '''  <h2>Lab 1 · Which line runs?</h2>
  <p>Drag the slider. The highlighted lines are the ones that run for that mark. Find the marks where the grade changes.</p>
  <div class="card"><div id="s1"></div><div id="lcode"></div><div class="verdict" id="lv" aria-live="polite"></div></div>

  <h2>Lab 2 · Does the order of the tests matter?</h2>
  <p>Choose which test comes first, then try a mark of 85. One order gives the wrong grade.</p>
  <div class="card"><div class="row"><label for="ord">Test order&nbsp;</label><select class="sel" id="ord"><option value="ok">Mark >= 70 first, then Mark >= 50</option><option value="bad">Mark >= 50 first, then Mark >= 70</option></select></div><div id="s2"></div><div id="ocode"></div><div class="verdict" id="ov" aria-live="polite"></div></div>

  <h2>Lab 3 · A menu with CASE OF</h2>
  <p>Choose a menu number and see which case matches. Try 9.</p>
  <div class="card"><div class="row"><label for="ch">Choice&nbsp;</label><select class="sel" id="ch"></select></div><div id="ccode"></div><div class="verdict" id="cv" aria-live="polite"></div></div>
'''

practise = '''  <h2>1 · Which selection structure?</h2>
  <div id="cl1" class="card"></div>
  <h2>2 · Put the IF in order</h2>
  <div id="o1" class="card"></div>
  <h2>3 · What is output?</h2>
  <p class="note">Type the word that is output, for example Pass.</p>
  <div id="c1"></div>
  <h2>4 · Multiple choice</h2>
  <div id="qz1"></div>
'''

real = (rw("A login screen", "If the password matches, let the user in. Otherwise show an error message.", "IF ... ELSE with a comparison: one route when TRUE, another when FALSE.")
        + rw("Ticket prices", "A cinema charges one price for children, another for adults and a cheaper one for over 65s.", "a nested IF, because there are three outcomes. Order the tests carefully.")
        + rw("A phone menu", "Press 1 for sales, 2 for support, 3 for billing. Any other number repeats the menu.", "CASE OF with OTHERWISE for an invalid choice.")
        + rw("A thermostat", "If the room is below the set temperature, switch the heating on. Otherwise leave it off.", "selection is how a program responds to data, in this case a sensor reading.")
        )

ex = [
    eq(1, "State", 1, "State the purpose of the <b>ELSE</b> part of an IF statement.", "What happens when the condition is FALSE?",
       mk(1, "It contains the instructions that are run when the condition is FALSE (the alternative route)."),
       "Saying it runs <b>after</b> the THEN part. It runs <b>instead of</b> it."),
    eq(2, "Write", 4, "Write pseudocode to input a person's age and output \"Adult\" if the age is 18 or over, otherwise output \"Child\".", "One test, two routes.",
       mk(1, "INPUT Age") + " " + mk(2, "IF Age >= 18 THEN") + " " + mk(3, "OUTPUT \"Adult\" in the THEN part, and ELSE with OUTPUT \"Child\"") + " " + mk(4, "ENDIF at the end")
       + ac(["INPUT Age", "IF Age >= 18", "  THEN", '    OUTPUT "Adult"', "  ELSE", '    OUTPUT "Child"', "ENDIF"]),
       "Using > 18, which leaves out the age 18 itself. \"18 or over\" needs <b>&gt;=</b>."),
    eq(3, "Complete", 3, "The code is run three times, with inputs 85, 60 and 30. State the output each time.", "Follow the tests from the top. The first TRUE condition wins.",
       mk(1, "85: Grade A") + " " + mk(2, "60: Grade B") + " " + mk(3, "30: Grade C"),
       "Giving both Grade A <b>and</b> Grade B for 85. Only one branch runs.",
       pre=qc(G_PS)),
    eq(4, "Write", 4, "A game menu has options 1 Start, 2 Load and 3 Exit. Write pseudocode using CASE OF to input a choice and output the name of the option. Output \"Invalid\" for any other number.", "CASE OF, one line per value, OTHERWISE for the rest.",
       mk(1, "INPUT Choice") + " " + mk(2, "CASE OF Choice") + " " + mk(3, "1, 2 and 3 each with the correct OUTPUT") + " " + mk(4, "OTHERWISE with OUTPUT \"Invalid\" and ENDCASE")
       + ac(["INPUT Choice", "CASE OF Choice", '  1 : OUTPUT "Start"', '  2 : OUTPUT "Load"', '  3 : OUTPUT "Exit"', '  OTHERWISE OUTPUT "Invalid"', "ENDCASE"]),
       "Forgetting ENDCASE, or putting a condition such as Choice > 3 on the OTHERWISE line."),
    eq(5, "Explain", 3, "The code below should output Distinction for 70 or over. Explain why a mark of 85 gives the wrong output, and how to correct it.", "Which test does 85 match first?",
       mk(1, "85 is >= 50, so the first test is TRUE") + " " + mk(2, "so \"Merit\" is output and the test for 70 is never reached") + " " + mk(3, "Fix: test Mark >= 70 first (swap the order of the two tests)."),
       "Saying the tests are wrong. The tests are fine, it is the <b>order</b> that is wrong.",
       pre=qc(["IF Mark >= 50", "  THEN", '    OUTPUT "Merit"', "  ELSE", "    IF Mark >= 70", "      THEN", '        OUTPUT "Distinction"', "    ENDIF", "ENDIF"])),
    eq(6, "Write", 5, "Write pseudocode to input a temperature. Output \"Too cold\" if it is below 10, \"Just right\" if it is 10 to 25 inclusive, and \"Too hot\" if it is above 25.", "Three outcomes: use a nested IF. Test one end first, then the other.",
       mk(1, "INPUT Temperature") + " " + mk(2, "IF Temperature < 10 THEN OUTPUT \"Too cold\"") + " " + mk(3, "ELSE with a second IF Temperature <= 25 (or > 25)") + " " + mk(4, "correct outputs \"Just right\" and \"Too hot\" in the right branches") + " " + mk(5, "all IFs closed with ENDIF")
       + ac(["INPUT Temperature", "IF Temperature < 10", "  THEN", '    OUTPUT "Too cold"', "  ELSE", "    IF Temperature <= 25", "      THEN", '        OUTPUT "Just right"', "      ELSE", '        OUTPUT "Too hot"', "    ENDIF", "ENDIF"]),
       "Using &lt; 25 or &gt; 10, which gets the boundary values 25 and 10 wrong."),
    eq(7, "Describe", 2, "Describe when a programmer would use CASE OF instead of a nested IF.", "Think about what is being compared.",
       mk(1, "When one variable (the same value) is being compared against several fixed values") + " " + mk(2, "for example a menu choice; it is shorter and easier to read than many nested IFs."),
       "Saying CASE OF can test ranges such as Mark >= 50. It matches <b>fixed values</b>."),
    eq(8, "Write", 6, "A cinema charges $5 per ticket for under 12s and $10 per ticket for everyone else. Write pseudocode to input an age and the number of tickets wanted, then output the total cost.", "Selection chooses the price. Sequence does the rest.",
       mk(1, "INPUT Age and INPUT Tickets") + " " + mk(2, "IF Age < 12") + " " + mk(3, "THEN Price ← 5") + " " + mk(4, "ELSE Price ← 10 and ENDIF") + " " + mk(5, "Total ← Price * Tickets, after the selection") + " " + mk(6, "OUTPUT Total")
       + ac(["INPUT Age", "INPUT Tickets", "IF Age < 12", "  THEN", "    Price ← 5", "  ELSE", "    Price ← 10", "ENDIF", "Total ← Price * Tickets", "OUTPUT Total"]),
       "Working out Total inside the THEN part only, so over-12s never get a total."),
]
exam = "".join(ex)

tipshtml = tips([
    "<b>A condition is TRUE or FALSE.</b> The result decides which lines run.",
    "<b>IF ... ELSE runs exactly one branch.</b> Never both.",
    "<b>With nested IFs the first TRUE test wins.</b> Put the most specific test first.",
    "<b>Check the boundary.</b> \"18 or over\" is &gt;= 18. \"Over 18\" is &gt; 18.",
    "<b>Close every IF with ENDIF</b> and every CASE with ENDCASE.",
    "<b>Pseudocode compares with =, Python with ==.</b> Python also needs a colon and indentation.",
])

page("8.1.4 · Selection", "Selection", "Making decisions in a program: IF, IF ... ELSE, nested IF and CASE OF.",
     "<span class=\"kw\">Selection</span> lets a program choose between routes by testing a condition. The condition is TRUE or FALSE, and that decides which lines run.",
     learn, watch, explore, practise, real, exam, tipshtml, "p814b")

js = []
js.append(f'''
const G_PS = {json.dumps(G_PS, ensure_ascii=False)}, G_PY = {json.dumps(G_PY, ensure_ascii=False)};
const IE_PS = ["DECLARE Mark : INTEGER", "INPUT Mark", "IF Mark >= 50", "  THEN", '    OUTPUT "Pass"', "  ELSE", '    OUTPUT "Fail"', "ENDIF"];
const IE_PY = ["mark = int(input())", "if mark >= 50:", '    print("Pass")', "else:", '    print("Fail")'];
const C_PS = ["INPUT Choice", "CASE OF Choice", '  1 : OUTPUT "Play"', '  2 : OUTPUT "Options"', '  3 : OUTPUT "Quit"', '  OTHERWISE OUTPUT "Invalid choice"', "ENDCASE"];
const C_PY = ["choice = int(input())", "if choice == 1:", '    print("Play")', "elif choice == 2:", '    print("Options")', "elif choice == 3:", '    print("Quit")', "else:", '    print("Invalid choice")'];
tr($("#aI"), {{ label: "IF THEN ELSE", title: "Pass or fail", pseudo: IE_PS, py: IE_PY, dwell: 2200, frames: {anim_ifelse()} }});
tr($("#aN"), {{ label: "Nested IF", title: "Grade", pseudo: G_PS, py: G_PY, dwell: 2200, frames: {anim_nested()} }});
tr($("#aC"), {{ label: "CASE OF", title: "Menu", pseudo: C_PS, py: C_PY, dwell: 2200, frames: {anim_case()} }});
Lib.codePanel($("#cdIf"), {{ pseudo: ["INPUT Battery", "IF Battery < 20", "  THEN", '    OUTPUT "Low battery"', "ENDIF"], py: ["battery = int(input())", "if battery < 20:", '    print("Low battery")'] }});
Lib.codePanel($("#cdIfElse"), {{ pseudo: IE_PS.slice(1), py: IE_PY }});
Lib.codePanel($("#cdNest"), {{ pseudo: G_PS, py: G_PY }});
Lib.codePanel($("#cdCase"), {{ pseudo: C_PS, py: C_PY }});
''')

js.append(r'''
/* ---------- Lab 1 ---------- */
(() => {
  const cp = Lib.codePanel($("#lcode"), { pseudo: G_PS, py: G_PY });
  Lib.slider($("#s1"), { id: "sm", label: "Mark ", min: 0, max: 100, value: 58, onInput: (m) => {
    const a = m >= 70, b = m >= 50;
    if (a) { cp.hl([1, 2, 3], [1, 2]); $("#lv").innerHTML = `${m} >= 70 is TRUE, so <b>Grade A</b>. Nothing else is tested.`; }
    else if (b) { cp.hl([1, 4, 5, 6, 7], [1, 3, 4]); $("#lv").innerHTML = `${m} >= 70 is FALSE. ${m} >= 50 is TRUE, so <b>Grade B</b>.`; }
    else { cp.hl([1, 4, 5, 8, 9], [1, 3, 5, 6]); $("#lv").innerHTML = `${m} >= 70 is FALSE and ${m} >= 50 is FALSE, so the last ELSE runs: <b>Grade C</b>.`; } } });
})();

/* ---------- Lab 2 ---------- */
(() => {
  const OK = [G_PS.slice(0), G_PY], BADPS = ["INPUT Mark", "IF Mark >= 50", "  THEN", '    OUTPUT "Grade B"', "  ELSE", "    IF Mark >= 70", "      THEN", '        OUTPUT "Grade A"', "    ENDIF", "ENDIF"];
  const BADPY = ["mark = int(input())", "if mark >= 50:", '    print("Grade B")', "elif mark >= 70:", '    print("Grade A")'];
  let sl;
  const upd = () => {
    if (!sl) return; const m = sl.get(), bad = $("#ord").value === "bad", cp = Lib.codePanel($("#ocode"), bad ? { pseudo: BADPS, py: BADPY } : { pseudo: G_PS, py: G_PY });
    if (!bad) { const g = m >= 70 ? "A" : m >= 50 ? "B" : "C"; cp.hl(m >= 70 ? [1, 3] : m >= 50 ? [1, 5, 7] : [1, 5, 9], m >= 70 ? [1, 2] : m >= 50 ? [3, 4] : [5, 6]); $("#ov").innerHTML = `Mark ${m}: <b>Grade ${g}</b>. ${m >= 70 ? "Correct." : ""}`; }
    else { cp.hl(m >= 50 ? [1, 3] : [1, 4, 5], m >= 50 ? [1, 2] : [1, 3]); $("#ov").innerHTML = m >= 70 ? `Mark ${m}: <span class="kpri">Grade B</span>. The first test (${m} >= 50) is TRUE, so the test for 70 is never reached.` : m >= 50 ? `Mark ${m}: <b>Grade B</b>. Correct here, but only by luck.` : `Mark ${m}: <b>nothing is output</b>. The 70 test is only reached for marks below 50, and none of those pass it.`; }
  };
  sl = Lib.slider($("#s2"), { id: "so", label: "Mark ", min: 0, max: 100, value: 85, onInput: upd });
  $("#ord").onchange = upd; upd();
})();

/* ---------- Lab 3 ---------- */
(() => {
  const sel = $("#ch"); sel.innerHTML = [1, 2, 3, 4, 9].map((v) => `<option>${v}</option>`).join("");
  const cp = Lib.codePanel($("#ccode"), { pseudo: C_PS, py: C_PY });
  const out = { 1: ["Play", [2], [2]], 2: ["Options", [3], [4]], 3: ["Quit", [4], [6]] };
  const upd = () => { const c = +sel.value, o = out[c];
    if (o) { cp.hl([0, 1].concat(o[1]), [0, 1].concat(o[2])); $("#cv").innerHTML = `Choice ${c} matches a case: <b>${o[0]}</b>.`; }
    else { cp.hl([0, 1, 5], [0, 7, 8]); $("#cv").innerHTML = `${c} matches no case, so OTHERWISE runs: <b>Invalid choice</b>.`; } };
  sel.onchange = upd; upd();
})();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Which structure fits each situation best?", buckets: [{ label: "IF ... THEN" }, { label: "IF ... ELSE" }, { label: "Nested IF" }, { label: "CASE OF" }], items: [
  { text: "Output a warning only if the battery is below 20", b: 0 }, { text: "Add a bonus point only if the key was found", b: 0 },
  { text: "Output Adult or Child", b: 1 }, { text: "Output Open or Closed", b: 1 },
  { text: "Output Grade A, B, C or D from a mark", b: 2 }, { text: "Choose a postage price from four weight bands", b: 2 },
  { text: "Turn a menu number 1 to 4 into an option name", b: 3 }, { text: "Turn day number 1 to 7 into the day name", b: 3 }],
  done: "One test: IF. Two routes: IF ELSE. Ranges with 3+ outcomes: nested IF. One variable against fixed values: CASE." });
Lib.order($("#o1"), { prompt: "Put this program in order.", items: ["INPUT Age", "IF Age >= 18", "THEN OUTPUT \"Adult\"", "ELSE OUTPUT \"Child\"", "ENDIF"], done: "Input, test, THEN branch, ELSE branch, ENDIF." });
Lib.calc($("#c1"), { qs: [
  { q: "IF Mark >= 50 THEN OUTPUT \"Pass\" ELSE OUTPUT \"Fail\" ENDIF. Mark is 50. What is output?", t: ["PASS", '"PASS"'], ph: "word", sol: "50 >= 50 is TRUE, so Pass." },
  { q: "The same code, with Mark 49. What is output?", t: ["FAIL", '"FAIL"'], ph: "word", sol: "49 >= 50 is FALSE, so Fail." },
  { q: "Grade code: &gt;= 70 gives A, otherwise &gt;= 50 gives B, otherwise C. Mark is 70. Which letter is output?", t: ["A", '"A"', "GRADEA"], ph: "letter", sol: "70 >= 70 is TRUE, so A." },
  { q: "The same code with Mark 69. Which letter is output?", t: ["B", '"B"', "GRADEB"], ph: "letter", sol: "69 >= 70 is FALSE. 69 >= 50 is TRUE: B." },
  { q: "A CASE OF has cases 1, 2 and 3 and OTHERWISE. Choice is 7. Which part runs?", t: ["OTHERWISE"], ph: "word", sol: "7 matches no case, so OTHERWISE runs." }] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What is a condition?", opts: ["Something that is TRUE or FALSE", "A loop", "A variable name", "A type of output"], a: 0, why: "Selection runs different lines depending on whether it is TRUE or FALSE." },
  { q: "How many branches of an IF ... ELSE run each time?", opts: ["Exactly one", "Both", "None", "It depends on the program length"], a: 0, why: "Either the THEN part or the ELSE part, never both." },
  { q: "In a nested IF, which test should come first?", opts: ["The most specific (hardest) one", "The easiest one", "It does not matter", "The ELSE"], a: 0, why: "The first TRUE test wins, so a wide test first can hide the others." },
  { q: "Which keyword ends an IF statement in pseudocode?", opts: ["ENDIF", "NEXT", "ENDCASE", "UNTIL"], a: 0, why: "IF ... ENDIF." },
  { q: "In Python, how is the end of an IF block shown?", opts: ["By indentation", "By ENDIF", "By a semicolon", "By NEXT"], a: 0, why: "Python uses indentation and a colon." }] });
Lib.cards($("#fc1"), { cards: [
  ["Selection", "Choosing which lines of a program to run, based on a condition."],
  ["Condition", "A test that is either TRUE or FALSE, such as Mark >= 50."],
  ["IF ... THEN ... ENDIF", "Runs lines only when the condition is TRUE."],
  ["ELSE", "The lines run when the IF condition is FALSE."],
  ["Nested IF", "An IF inside another IF, used for three or more outcomes."],
  ["CASE OF", "Compares one variable with several fixed values and runs the matching line."],
  ["OTHERWISE", "The part of a CASE OF that runs when no value matches."],
  ["Comparison operator", "A symbol such as =, <>, <, >, <= or >= that compares two values."]] });
''')
write_js("p814b", js)
