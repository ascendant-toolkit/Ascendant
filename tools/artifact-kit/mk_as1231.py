"""AS CS 12.3.1: errors and testing. Run: python3 tools/artifact-kit/mk_as1231.py"""
from ascs import *

def pc(text, label=None): return code(text.strip("\n").split("\n"), label=label)
def tbl(head, rows, cls="t"):
    return '<div class="tw"><table class="%s"><tr>%s</tr>%s</table></div>' % (cls, "".join("<th>%s</th>" % h for h in head), "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % c for c in r) for r in rows))

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>There are three kinds of error. A <b>syntax error</b> breaks the rules of the language, so the program will not run or compile. A <b>logic error</b> means the program runs but gives wrong results, because the algorithm is wrong. A <b>run-time error</b> happens while the program runs, when it is asked to do something impossible (divide by zero, an index outside an array, or an endless loop that makes it stop responding). <b>Testing</b> is planned with a <b>test plan</b>: test data of the right types (normal, abnormal, boundary) with the expected result for each. Testing is done at different levels and by different people: <b>walkthroughs</b>, <b>white-box</b> and <b>black-box</b> testing, <b>stub</b> and <b>integration</b> testing, and finally <b>alpha</b>, <b>beta</b> and <b>acceptance</b> testing.</p></div>

  <h2>1 · Types of error</h2>
  ''' + tbl(["Error", "When found", "Description", "Example"], [
    ["<b>Syntax</b>", "When the program is translated", "The program breaks the rules or grammar of the language: it will not compile or run", "A misspelt keyword, a missing bracket, NEXT where ENDWHILE is needed, using &amp; to join an integer"],
    ["<b>Logic</b>", "When running, from wrong output", "The program runs but does not do what was intended: an error in the algorithm or the design", "The wrong arithmetic operator, the wrong loop count, a condition that is the wrong way round"],
    ["<b>Run-time</b>", "While running", "The program performs an illegal operation and may crash or freeze", "Divide by zero, a value outside the range of an array index, an endless loop"]]) + '''
  <p>A program that is "free of syntax errors" obeys the rules of the language and will run (compile or be interpreted), but may still contain logic or run-time errors.</p>

  <h2>2 · Test data and the test plan</h2>
  <ul>
    <li><b>Normal</b> data is valid and typical: 153 for a range 150 to 155.</li>
    <li><b>Abnormal</b> (erroneous) data should be rejected: a value outside the range, or the wrong type.</li>
    <li><b>Boundary</b> (extreme) data lies at the edge of the range: the smallest and largest accepted values (150, 155) and the values just outside them (149, 156).</li>
    <li>A <b>test plan</b> lists each test with its data, an explanation and the <b>expected result</b>, written before testing.</li>
  </ul>
  ''' + tbl(["Test", "Test data", "Type", "Expected result"], [["1", "153", "Normal", "\"PASS\""], ["2", "150", "Boundary (lowest accepted)", "\"PASS\""], ["3", "155", "Boundary (highest accepted)", "\"PASS\""], ["4", "149", "Abnormal and boundary (largest rejected below)", "\"FAIL\""], ["5", "156", "Abnormal and boundary (smallest rejected above)", "\"FAIL\""], ["6", "&lt; 149 or &gt; 156", "Abnormal", "\"FAIL\""]]) + '''
  <p>For a range <b>24 to 37 inclusive</b> a thorough plan has normal data (30), the boundaries (24, 25, 36, 37) and the values just outside (23, 38) and clearly invalid values (12, 99).</p>

  <h2>3 · Methods of testing</h2>
  <ul>
    <li><b>Dry run / walkthrough:</b> going through the program a line at a time with test data, recording the variables in a <b>trace table</b>; an error shows when a variable or output has an unexpected value. The design (the algorithm or code) and a test plan (inputs and expected outputs) are needed first, so that all paths through the program can be tested.</li>
    <li><b>White-box testing:</b> the tester knows the code and chooses data to make every path through it run (for the bonus pay: one test for each row of the table).</li>
    <li><b>Black-box testing:</b> the tester checks inputs against expected outputs without looking at the code.</li>
    <li><b>Stub testing:</b> the unfinished modules are replaced by simple modules (stubs) that return a known value or output a message to show they were called, so the rest can be tested.</li>
    <li><b>Integration testing:</b> modules that work alone are combined and tested together.</li>
    <li><b>Using an IDE:</b> breakpoints, single-stepping and watching variables find errors (see section 5.2.2).</li>
  </ul>

  <h2>4 · Final stages of testing</h2>
  <ul>
    <li><b>Alpha testing:</b> done in-house by the developers or the company's own testers before the software is released.</li>
    <li><b>Beta testing:</b> carried out by a small group of potential users, who check it works in the real world, find errors and feed back problems and suggestions; these are addressed before the program is sold or released to everyone.</li>
    <li><b>Acceptance testing:</b> the customer tests the whole system on their own hardware, and if the tests are passed the customer accepts the system.</li>
  </ul>

  <h2>Common ways to lose marks</h2>
  <ul>
    <li>Testing only normal data. A plan needs abnormal and boundary data too.</li>
    <li>Omitting the expected result, or giving an expected result that does not match the rule.</li>
    <li>Describing beta testing as done by the developers (that is alpha).</li>
    <li>Calling a freeze a logic error: a program that stops responding has a run-time error.</li>
  </ul>
'''

watch = '''
  <h2>1 · Three errors in one program</h2>
  <div id="stA"></div>
  <h2>2 · Boundaries of a range</h2>
  <div id="stB"></div>
  <h2>3 · Alpha, beta and acceptance</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Build a test plan</h2>
  <p>A function accepts a weight from 150 to 155 inclusive. Choose the values to test. The checker shows which kinds of data you have covered.</p>
  <div class="card"><div id="tpB" class="btnrow"></div><div id="tpV"></div></div>
  <h2>Lab 2 · Which error?</h2>
  <div class="card"><div id="erB" class="btnrow"></div><div id="erO"></div></div>
  <h2>Lab 3 · Which type of testing?</h2>
  <div class="card"><div id="tsB" class="btnrow"></div><div id="tsO"></div></div>
'''

_pr, _prjs = PR(["Which error?", "Type of test data", "Match the testing", "Put the testing stages in order", "Working out", "Multiple choice"],
  ("Which type of error?", ["Syntax", "Logic", "Run-time"], [("NEXT Index used instead of ENDWHILE", 0), ("The program divides by zero and crashes", 2), ("The program adds instead of multiplying, so the total is wrong", 1), ("An endless loop makes the program stop responding", 2), ("A misspelt keyword stops the program compiling", 0), ("A loop runs one time too few and the output is wrong", 1)], "Rules of the language: syntax. Wrong result: logic. Crashes or freezes: run-time."),
  ("Type of test data for a range of 150 to 155 inclusive?", ["Normal", "Boundary", "Abnormal"], [("153", 0), ("150", 1), ("155", 1), ("200", 2), ("12", 2), ("152", 0)], "Typical: normal. Edge: boundary. Outside: abnormal."),
  [["Walkthrough", "Going through code line by line with a trace table"], ["White-box", "Tests chosen to run every path through the code"], ["Black-box", "Inputs and outputs only, no view of the code"], ["Stub testing", "Simple modules replace unfinished ones"], ["Integration testing", "Modules tested together"]],
  ("Put these in order, from first to last.", ["Unit testing of a module", "Integration testing of the modules together", "Alpha testing in-house", "Beta testing by a small group of users", "Acceptance testing by the customer"], "Small to large, developers to customer."),
  [{"q": "A range is 24 to 37 inclusive. How many integers are valid?", "a": 14, "unit": "", "tol": 0.01, "hint": "37 − 24 + 1.", "sol": "<b>14</b>."}, {"q": "A range is 0 to 40 inclusive. The largest abnormal value just above the range is?", "a": 41, "unit": "", "tol": 0.01, "hint": "One more than 40.", "sol": "<b>41</b>."}, {"q": "A plan tests 23, 24, 25, 36, 37, 38 for 24 to 37. How many of these should be rejected?", "a": 2, "unit": "", "tol": 0.01, "hint": "23 and 38.", "sol": "<b>2</b>."}, {"q": "A bonus table has four rows (hours and sales combinations). The fewest white-box tests to cover every row?", "a": 4, "unit": "", "tol": 0.01, "hint": "One per path.", "sol": "<b>4</b>."}, {"q": "A program has 6 modules and 2 are unfinished. How many stubs are needed?", "a": 2, "unit": "", "tol": 0.01, "hint": "One per unfinished module.", "sol": "<b>2</b>."}],
  [("A program that runs but gives wrong totals has a:", ["Logic error", "Syntax error", "Compile error", "No error"], 0, "Logic."), ("Divide by zero is a:", ["Run-time error", "Syntax error", "Logic error", "Design error"], 0, "Run-time."), ("Boundary data is:", ["At the edges of the valid range", "Typical data", "Random data", "Invalid data only"], 0, "Edges."), ("Beta testing is done by:", ["A small group of potential users", "The developer only", "A compiler", "The customer's lawyers"], 0, "Real users."), ("A stub is:", ["A simple module standing in for an unfinished one", "A syntax error", "A test plan", "An IDE tool"], 0, "Simple module."), ("A trace table is used in:", ["A walkthrough or dry run", "Compiling", "Beta testing only", "Maintenance only"], 0, "Dry run.")],
  [("Syntax error", "Breaks the language rules."), ("Logic error", "Wrong result: the algorithm is wrong."), ("Run-time error", "Crash or freeze while running."), ("Normal data", "Valid and typical."), ("Boundary", "At the edge of the range."), ("Abnormal", "Should be rejected."), ("Stub", "A simple stand-in module."), ("Beta testing", "A small group of users.")])

real = RWNOTE + (
rw("An app before launch", "Developers test in-house (alpha), then a small group of users try it (beta), and the fixes are made before everyone gets it.", "alpha and beta.") +
rw("An age check on a website", "Testers try 17, 18 and 19 and a negative number, not only 25, because the errors are at the boundary.", "boundary and abnormal data.") +
rw("A game that freezes", "A loop that never ends is a run-time error: the program has not been told to stop.", "run-time errors.") +
rw("A payment system", "The new module is tested with stubs for the banks that are not yet connected, returning a fixed answer.", "stub testing.")
)

where = [
  ("O/N 2021", "21", "1(a)", "1 + 2", "The meaning of no syntax errors; another type of error"),
  ("O/N 2021", "21", "4(a)", "4", "Test plan for a sensor validation function (0 to 40)"),
  ("M/J 2022", "22", "1(b)", "4 (beta testing part)", "A final test stage before a program is sold"),
  ("M/J 2022", "23", "4", "4", "Black-box test plan for a weight validator (150 to 155)"),
  ("M/J 2023", "21", "5(b)", "3", "Identify and describe the final stage of testing"),
  ("M/J 2023", "23", "5(a)", "3", "Information needed for walkthrough testing"),
  ("M/J 2024", "22", "5", "3 + 2 + 1", "Syntax and other errors in a procedure; a statement not needed; the type of error when it freezes"),
  ("O/N 2024", "21", "5(b)", "4 + 1", "A test plan for a range 24 to 37; the type of testing when combined with other modules"),
  ("M/J 2025", "22", "2(b)", "2 + 2 + 2", "White-box tests; stub testing; types of error"),
  ("M/J 2025", "23", "4(b)", "3", "Describe the walkthrough method")]

past = '''  <p class="note">The test plan table and the testing terms are asked in nearly every series. Learn the three kinds of test data and the two or three points that earn the marks for each testing term.</p>
''' + peq(SRC("w21", "21", "Q1(a)"), "1 + 2 marks", "State / Identify",
  "Sylvia tests a program written by a colleague, who says it does not contain any syntax errors. (i) State what the colleague means. (ii) Identify and describe one other type of error that the program may contain.", "Obeys the rules of the language. Logic or run-time.",
  "<p><b>(i)</b> One from: " + mks(["The program obeys the rules (grammar) of the programming language used", "The program will run (it can be compiled or interpreted)", "By example: no misspelt keywords, all brackets match"], "a") + "</p><p><b>(ii)</b> One mark for the type and one for its description: " + mks(["Logic error: an error in the algorithm or design, so the program does not behave as expected or give the expected output (for example the wrong arithmetic operator or the wrong loop count)", "Run-time error: the program performs an illegal instruction or invalid operation (for example divide by zero, an endless loop, or it crashes or freezes)"], "b") + "</p>", None) + peq(SRC("w21", "21", "Q4(a)"), "4 marks", "Complete",
  "A heating program reads a sensor value, an integer that should be in the range 0 to 40 inclusive. A function validates it. Complete the test plan (the first test, 23, normal data, data is accepted, is given): rows 2 to 5, each with a test data value, an explanation (normal, boundary or abnormal) and the expected outcome.", "Two boundaries accepted; one beyond each end rejected.",
  "<p>One mark per row for rows 2 to 5:" + tbl(["Test", "Test data value", "Explanation", "Expected outcome"], [["1", "23", "Normal data", "Data is accepted"], ["2", "0", "Boundary data", "Data is accepted"], ["3", "40", "Boundary data", "Data is accepted"], ["4", "&gt;= 41", "Abnormal data", "Data is rejected"], ["5", "&lt;= -1", "Abnormal data", "Data is rejected"]]) + "</p>", "Choosing 41 and -1 and calling them boundary data that is accepted: they are just outside the range and must be rejected.") + peq(SRC("s22", "23", "Q4"), "4 marks", "Complete",
  "Items in a factory are weighed automatically. A validation function returns \"PASS\" if the weight in grams is within the range 150 to 155 inclusive, otherwise \"FAIL\". The function is tested with the black-box method. Complete the test plan with additional tests (the normal test 153, \"PASS\" is given).", "Both boundaries, the values just outside them, and values beyond.",
  "<p>One mark per row from rows 2 to 7, maximum 4:" + tbl(["Type of test data", "Example test value", "Expected return value", "Explanation"], [["Normal", "153", "\"PASS\"", "Within the acceptable range"], ["Abnormal", "&lt; 149", "\"FAIL\"", "Outside the acceptable range, too small"], ["Abnormal / boundary", "149", "\"FAIL\"", "Maximum unacceptable"], ["Boundary / extreme / normal", "150", "\"PASS\"", "Minimum acceptable"], ["Boundary / extreme / normal", "155", "\"PASS\"", "Maximum acceptable"], ["Abnormal / boundary", "156", "\"FAIL\"", "Minimum unacceptable"], ["Abnormal", "&gt; 156", "\"FAIL\"", "Outside the acceptable range, too large"]]) + "</p>", "Writing the expected result as \"valid\" instead of the value the function returns.") + peq(SRC("w24", "21", "Q5(b)"), "4 + 1 marks", "Complete / Identify",
  "A validation function takes an integer, returns TRUE if it is within the range 24 to 37 inclusive, otherwise FALSE. (i) Complete the table to define a test plan to thoroughly test it (the normal test 30, TRUE is given). (ii) The function is tested on its own; when it works it is combined with other modules and testing continues. Identify this type of testing.", "Both ends and just outside; integration.",
  "<p><b>(i)</b> One mark per row, maximum 4:" + tbl(["Type of test data", "Test data value", "Expected result"], [["Normal", "30", "TRUE"], ["Abnormal", "12 (&lt; 23)", "FALSE"], ["Abnormal / boundary / extreme", "23", "FALSE"], ["Boundary / extreme", "24", "TRUE"], ["Boundary", "25", "TRUE"], ["Boundary", "36", "TRUE"], ["Boundary / extreme", "37", "TRUE"], ["Abnormal / boundary / extreme", "38", "FALSE"], ["Abnormal", "99 (&gt; 38)", "FALSE"]]) + "</p><p><b>(ii)</b> " + mks(["Integration (testing)"], "a") + "</p>", None) + peq(SRC("w22", "22", "Q1(b)"), "4 marks", "Identify / Describe",
  "A program will be sold to the public. All the software errors identified during in-house testing have been corrected. Identify and describe the additional test stage that may be carried out before the program is sold to the public.", "A small group of users.",
  "<p>" + mks(["Test stage: beta testing", "Carried out by a small group of (potential) users", "The users check that the software works as required, in the real world, and does not contain errors", "Users give feedback on problems or suggestions for improvement", "The problems or suggestions are addressed before the program is sold"]) + " (one mark for the stage and up to three for the description)</p>", "Calling it alpha testing, which is the in-house stage.") + peq(SRC("s23", "23", "Q5(a)"), "3 marks", "Identify / Explain",
  "A program is designed, coded and compiled without errors. The compiled code is sent for testing with the walkthrough method. Additional information is needed before this method can be used. Identify this information and explain why it is needed.", "The code and the test plan.",
  "<p>Max 3: " + mks(["The program (source) code or specification", "A test plan: inputs (test data) and expected outputs", "The structure, design or algorithm of the program needs to be known", "so that all paths through the program can be tested"]) + "</p>", None) + peq(SRC("s25", "23", "Q4(b)"), "3 marks", "Describe / Explain",
  "Once the program has been completed, it is tested using the walkthrough method. Describe the walkthrough method and explain how it can be used to identify errors.", "Line by line with a trace table; unexpected values.",
  "<p>Max 3: " + mks(["Going through the program a line (statement) at a time (a dry run, single-stepping, or peer review)", "Creating a trace table", "Drawing up test data, a list of inputs with expected outputs (boundary, normal and abnormal data)", "Errors are indicated when a variable or output gives an unexpected value", "Faults in the logic can be detected, or an unexpected path through the program"]) + "</p>", None) + peq(SRC("s24", "22", "Q5"), "3 + 2 + 1 marks", "Identify / Explain",
  "PROCEDURE Process(Label : STRING) declares Index and sets Index ← 0, INPUT Data[Index], then WHILE Index < 200: Index ← Index + 1; CASE OF (Index MOD 2) with 0 : Data[Index] ← TO_UPPER(Label), 1 : Data[Index] ← TO_LOWER(Label), OTHERWISE : OUTPUT \"Alarm 1201\", ENDCASE; then NEXT Index, and finally OUTPUT \"Completed \" & Index & \" times\" (the array Data has 200 elements and the first index is 1). (a)(i) The pseudocode contains two syntax errors and one other error. Identify the errors. (ii) The procedure contains a statement that is not needed: identify it and explain why. (b) After correcting the syntax errors the program compiles but stops responding when run. Identify the type of error.", "NEXT for ENDWHILE; & on an integer; index 0. MOD 2 is 0 or 1. Run-time.",
  "<p><b>(a)(i)</b> " + mks(["Syntax: NEXT Index should be ENDWHILE", "Syntax: &amp; used to concatenate an integer in the OUTPUT statement", "Other: accesses an element outside the range (element 0)"]) + "</p><p><b>(ii)</b> " + mks(["Statement: the OTHERWISE statement", "Explanation: the result of MOD 2 can only be 0 or 1"], "a") + "</p><p><b>(b)</b> " + mks(["Run-time (error)"], "b") + "</p>", None) + peq(SRC("s25", "22", "Q2(b)"), "2 + 2 + 2 marks", "State / Describe",
  "A module calculates weekly bonus pay: hours between 1 and 40 inclusive with sales of 2000 or less give 0; hours between 1 and 40 with sales above 2000 give 50; hours above 40 with sales of 2000 or less give 10; hours above 40 with sales above 2000 give 100. (i) White-box testing is used: state two tests, with valid data, that test different paths through the program. (ii) The program uses modules called from different places and is tested with stub testing before all the modules are completed. Describe stub testing. (iii) The tests find that the program does not give the expected results: give the name of a type of error and its description.", "A test per row of the table. Simple stand-in modules. Logic or run-time.",
  "<p><b>(i)</b> One mark for each of two tests (any two of the four paths):" + tbl(["Hours worked", "Value of sales", "Bonus pay expected"], [["between 1 and 40 inclusive", "2000", "0"], ["above 40", "2000", "10"], ["between 1 and 40 inclusive", "above 2000 (for example 3000)", "50"], ["above 40", "above 2000 (for example 3000)", "100"]]) + "</p><p><b>(ii)</b> " + mks(["Simple modules are written to replace each of the unfinished modules", "Each simple module returns an expected value, or outputs a message to show it has been called"], "a") + "</p><p><b>(iii)</b> " + mks(["Logic error: the program does not behave as expected or give the expected result (an error in the logic of the algorithm)", "Or run-time error: the program performs an illegal operation"], "b") + " (max 2)</p>", None)

review = req("3 marks", "State", "State the type of error: (a) a missing closing bracket; (b) a loop that adds when it should multiply; (c) a division by a variable that is zero.", "Rules, wrong result, impossible operation.", "<p>" + mks(["Syntax error", "Logic error", "Run-time error"]) + "</p>", None) + req("4 marks", "Complete", "A function accepts the integers 1 to 100 inclusive. Complete a test plan with four tests of different types, with the expected results.", "Normal, boundary, abnormal.", "<p>" + tbl(["Test data", "Type", "Expected result"], [["50", "Normal", "accepted"], ["1 or 100", "Boundary", "accepted"], ["0 or 101", "Abnormal / boundary", "rejected"], ["-5 or 500", "Abnormal", "rejected"]]) + mks(["A normal value with its result", "A boundary value accepted", "A value just outside rejected", "A value far outside rejected"]) + "</p>", None) + req("3 marks", "Describe", "Describe the difference between alpha and beta testing.", "Developers or users.", "<p>" + mks(["Alpha testing is carried out in-house by the developers or the company's testers", "Beta testing is carried out by a small group of potential users", "Beta testing happens after alpha and checks the program in the real world"]) + "</p>", None) + req("2 marks", "Explain", "Explain what is meant by white-box testing.", "Knows the code.", "<p>" + mks(["The tester uses knowledge of the code", "and chooses test data to make every path through the program run"]) + "</p>", None) + req("2 marks", "Describe", "Describe what a trace table is used for.", "Dry run.", "<p>" + mks(["It records the values of variables line by line during a dry run", "so that errors (unexpected values) can be found"]) + "</p>", None)

tips = tips_html([
  ("Three error names.", "Syntax: rules. Logic: wrong result. Run-time: crashes or freezes."),
  ("Three data types.", "Normal, abnormal and boundary, each with the expected result."),
  ("Both ends of the range.", "The edge values and the values just outside."),
  ("Alpha in-house.", "Beta by users, acceptance by the customer."),
  ("Walkthrough needs a plan.", "Trace table, test data, expected output."),
  ("Stubs return something.", "A known value, or a message that it was called."),
], [("a syntax error", "A breach of the language's rules."), ("a logic error", "An error in the algorithm that gives wrong results."), ("a test plan", "A list of tests with data and expected results."), ("boundary data", "Test data at the edge of a valid range.")],
  [("State", "A short answer."), ("Identify", "Name it."), ("Describe", "Give the main features."), ("Complete", "Fill in the test plan.")]) + FC

js = AKJS + AK20JS + r'''
(function () {
  const L = ["WHILE Count <= 10  ... NEXT Count", "Total ← Total + Value (needs *)", "Result ← 100 / Zero", "IF Mark > 74 THEN ... without ENDIF"]; const K = ["Syntax error: NEXT instead of ENDWHILE", "Logic error: the program runs but the answer is wrong", "Run-time error: divide by zero stops the program", "Syntax error: the program will not compile"]; const draw = (s) => { const k = Math.round(s.i); let o = SV.rect(10, 8, 340, 34, "cell", { rx: 6 }) + SV.text(20, 30, L[k], "lbl bd", { style: "font-size:12px;font-family:monospace" }); o += SV.text(14, 66, K[k], "lbl bd t3", { style: "font-size:12px" }); return o; };
  Lib.stepper($("#stA"), { w: 360, h: 80, label: "Errors", base: { i: 0 }, draw, tween: 100, dwell: 2200, steps: ["A line that breaks the rules.", "A line that runs but computes the wrong thing.", "A line that is impossible at run time.", "Another syntax error."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = ""; const vals = [148, 149, 150, 153, 155, 156, 157]; vals.forEach((v, i) => { const ok = v >= 150 && v <= 155; const on = k === 0 ? false : k === 1 ? (v === 150 || v === 155) : k === 2 ? (v === 149 || v === 156) : v === 153; o += SV.rect(8 + i * 48, 14, 44, 28, on ? "f3" : ok ? "f1" : "cell", { rx: 4 }) + SV.text(30 + i * 48, 33, v, "lbl bd", { "text-anchor": "middle", style: "font-size:12px" }); }); o += SV.text(8, 66, ["Accepted range: 150 to 155 (shaded)", "Boundary: the lowest and highest accepted values", "Abnormal boundary: just outside the range", "Normal: a typical value inside"][k], "lbl bd t3", { style: "font-size:12px" }); return o; };
  Lib.stepper($("#stB"), { w: 350, h: 80, label: "Boundaries", base: { i: 0 }, draw, tween: 100, dwell: 2400, steps: ["The valid range.", "The boundary values.", "The values just outside.", "A normal value."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const N = [["Alpha", "developers, in-house"], ["Beta", "a small group of users"], ["Acceptance", "the customer on their own hardware"]]; let o = ""; N.forEach((n, i) => o += SV.rect(10 + i * 110, 14, 100, 30, i === k ? "f3" : i < k ? "f1" : "cell", { rx: 5 }) + SV.text(60 + i * 110, 34, n[0], "lbl bd", { "text-anchor": "middle", style: "font-size:12px" })); o += SV.text(10, 70, N[k][0] + ": " + N[k][1], "lbl bd t3", { style: "font-size:12px" }); return o; };
  Lib.stepper($("#stC"), { w: 350, h: 84, label: "Final testing", base: { i: 0 }, draw, tween: 100, dwell: 2200, steps: ["Alpha: the developers test it in-house.", "Beta: real users find the remaining problems.", "Acceptance: the customer tests the whole system."].map((c, i) => ({ cap: c, s: { i } })) });
})();

(function () {
  const lo = 150, hi = 155, vals = [-5, 12, 148, 149, 150, 151, 153, 154, 155, 156, 157, 200]; const sel = new Set(); const bar = $("#tpB");
  const kind = (v) => v < lo - 1 || v > hi + 1 ? "Abnormal" : v === lo - 1 || v === hi + 1 ? "Abnormal and boundary" : v === lo || v === hi ? "Boundary (accepted)" : "Normal";
  const paint = () => { const have = [...sel].map(kind); const need = [["Normal", "Normal"], ["Lowest accepted (150)", sel.has(150)], ["Highest accepted (155)", sel.has(155)], ["Just below (149)", sel.has(149)], ["Just above (156)", sel.has(156)], ["Clearly abnormal", [...sel].some((v) => v < 149 || v > 156)]]; need[0][1] = have.includes("Normal");
    $("#tpV").innerHTML = '<div class="tw"><table class="t"><tr><th>Test data</th><th>Type</th><th>Expected result</th></tr>' + [...sel].sort((a, b) => a - b).map((v) => `<tr><td>${v}</td><td>${kind(v)}</td><td>${v >= lo && v <= hi ? "PASS" : "FAIL"}</td></tr>`).join("") + '</table></div><div class="verdict">' + need.map((n) => (n[1] ? "✓ " : "✗ ") + n[0]).join(" &nbsp; ") + "</div>" + (need.every((n) => n[1]) ? "<p>A thorough plan: every kind of test is covered.</p>" : "<p>Add the missing kinds of test data.</p>"); };
  vals.forEach((v) => { const b = document.createElement("button"); b.textContent = v; b.onclick = () => { if (sel.has(v)) sel.delete(v); else sel.add(v); b.className = sel.has(v) ? "on" : ""; paint(); }; bar.appendChild(b); }); paint();
})();
btnTable("erB", "erO", [
  ["NEXT Index used instead of ENDWHILE", "Syntax error", "breaks the rules of the language"],
  ["Total adds when it should multiply", "Logic error", "runs, wrong result"],
  ["Division by zero", "Run-time error", "an illegal operation while running"],
  ["Endless loop: the program stops responding", "Run-time error", "the end condition is never met"],
  ["An element outside the array is accessed", "Run-time error (or a logic error in the design)", "the index is outside the range"]
], ["Fault", "Error type", "Why"]);
btnTable("tsB", "tsO", [
  ["Unfinished modules replaced with simple ones that return fixed values", "Stub testing", "the rest can be tested"],
  ["Tests chosen to run every path through known code", "White-box testing", "the code is known"],
  ["Inputs checked against expected outputs, code not inspected", "Black-box testing", "only inputs and outputs"],
  ["A small group of real users try the software before release", "Beta testing", "in the real world"],
  ["The developers test in-house before release", "Alpha testing", "in-house"],
  ["Working modules are combined and tested together", "Integration testing", "modules combined"]
], ["Description", "Testing", "Why"]);
''' + _prjs

finish("as-12-3-1-errors-and-testing", "as1231", "Errors and Testing",
  "Syntax, logic and run-time errors, test data and test plans, walkthroughs, white-box, black-box, stub and integration testing and alpha, beta and acceptance testing, with animations, labs and the real Paper 2 questions from 2021 to 2026.",
  "12.3.1", "12 · Software development", "section 12.3 Program testing and maintenance", learn, watch, explore, _pr, real, where, past, review,
  "Part 1 is real 9618 questions on errors and testing (Paper 2), 2021 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", tips, js)
