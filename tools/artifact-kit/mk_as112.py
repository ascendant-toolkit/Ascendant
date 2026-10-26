"""AS CS 11.2: programming constructs. Run: python3 tools/artifact-kit/mk_as112.py"""
from ascs import *

def pc(text, label=None): return code(text.strip("\n").split("\n"), label=label)
def tbl(head, rows, cls="t mono"):
    return '<div class="tw"><table class="%s"><tr>%s</tr>%s</table></div>' % (cls, "".join("<th>%s</th>" % h for h in head), "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % c for c in r) for r in rows))
def tick(grid, head, rows):
    return tbl(head, [[r[0]] + ["✓" if x else "" for x in r[1:]] for r in rows])

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>Every program is built from three <b>constructs</b>: <b>sequence</b> (statements in order), <b>selection</b> (choosing: IF or CASE) and <b>iteration</b> (repeating: FOR, WHILE or REPEAT). <b>Assignment</b> (<span class="mono">←</span>) stores a value, and a <b>subroutine call</b> is a construct too. A <b>count-controlled</b> loop (FOR) repeats a set number of times, a <b>pre-condition</b> loop (WHILE) tests first and may never run, and a <b>post-condition</b> loop (REPEAT ... UNTIL) tests last and always runs at least once. Choose the loop that fits what you know: a known count, or a condition that ends it. A loop whose end condition can never become true runs for ever and the program stops responding.</p></div>

  <h2>1 · Selection</h2>
  ''' + pc('''
IF Mark > 74 THEN
   Grade ← 'A'
ELSE
   IF Mark > 59 THEN
      Grade ← 'B'
   ELSE
      Grade ← 'C'
   ENDIF
ENDIF

CASE OF MySwitch
   1 : ThisChar ← 'a'
   2 : ThisChar ← 'y'
   3 : ThisChar ← '7'
   OTHERWISE : ThisChar ← '*'
ENDCASE''') + '''
  <ul>
    <li>Use <b>IF</b> for one or two conditions or ranges of values; use <b>CASE</b> to choose between several exact values of one variable. A CASE clause can also be a range (<span class="mono">1 TO 5 : ...</span>), and <span class="mono">OTHERWISE</span> covers everything else.</li>
    <li>A CASE can always be rewritten as nested IF ... ELSE ... ENDIF, and an IF on one variable with two outcomes needs a single IF ... THEN ... ELSE ... ENDIF.</li>
    <li>Two clauses that differ only by a number can be merged: <span class="mono">1 TO 2 : Index ← Index + CaseVar</span>.</li>
  </ul>

  <h2>2 · Iteration</h2>
  ''' + pc('''
FOR Index ← 1 TO 10 STEP 2            // count-controlled: known number of repeats
   OUTPUT Index
NEXT Index

WHILE Value <> 0                      // pre-condition: test first, may run zero times
   INPUT Value
   Total ← Total + Value
ENDWHILE

REPEAT                                // post-condition: always runs at least once
   INPUT Password
UNTIL Password = "secret"''') + '''
  <div class="tw"><table class="t">
    <tr><th>Loop</th><th>Test</th><th>Minimum runs</th><th>Use when</th></tr>
    <tr><td><b>FOR ... NEXT</b></td><td>Counter reaches the end value</td><td>0 (if start is past the end)</td><td>The number of repeats is known, or you step through an array</td></tr>
    <tr><td><b>WHILE ... ENDWHILE</b></td><td>Before each pass</td><td>0</td><td>The data may be empty, or the end is a value or end of file</td></tr>
    <tr><td><b>REPEAT ... UNTIL</b></td><td>After each pass</td><td>1</td><td>The loop must run once before it can be tested (validating an input)</td></tr>
  </table></div>
  <ul>
    <li>The loop to use when the number of iterations is not known is a <b>conditional</b> (pre- or post-condition) loop; the exam answer "the number of iterations is not known, or the loop ends after a particular input" is a standard justification.</li>
    <li>A <b>count</b> starts at 0 and adds 1; a <b>total</b> starts at 0 and adds a value. Always <b>initialise before the loop</b>.</li>
    <li>A conditional loop that never ends is a <b>run-time error</b> (the program freezes): the terminating condition is never satisfied.</li>
  </ul>

  <h2>3 · Constructs in one table</h2>
  ''' + tbl(["Code", "Construct"], [["FOR Index ← 1 TO 3 ... NEXT Index", "iteration"], ["IF Mark > 74 THEN ... ENDIF", "selection"], ["CASE OF ... OTHERWISE : ... ENDCASE", "selection"], ["REPEAT UNTIL AllDone() = TRUE", "iteration + subroutine (function call)"], ["Grade ← 'A'", "assignment"], ["INPUT MyName", "assignment (the value is stored)"], ["CALL Reset(Count)", "subroutine"]]) + '''

  <h2>Common ways to lose marks</h2>
  <ul>
    <li>Ticking only one construct in a row where a statement does more than one job (an IF containing a FOR is both selection and iteration; a call inside a loop is iteration and subroutine).</li>
    <li>Not initialising a count or total before the loop.</li>
    <li>Using WHILE when the loop must run once, or REPEAT when it might not.</li>
    <li>Testing the wrong bound: <span class="mono">FOR ThisInt ← 100 TO 200</span> includes both 100 and 200.</li>
  </ul>
'''

watch = '''
  <h2>1 · The three loops</h2>
  <div id="stA"></div>
  <h2>2 · CASE chooses one path</h2>
  <div id="stB"></div>
  <h2>3 · Counting and totalling</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · How many times does it run?</h2>
  <p>Set the starting value, then compare the three loops. Each adds 1 to the value and stops at 5.</p>
  <div class="card"><div class="btnrow"><label>Start value <input id="lp_x" type="number" value="1" min="-5" max="12" style="width:70px"></label></div><div id="lpV"></div></div>
  <h2>Lab 2 · CASE or IF?</h2>
  <div class="card"><div class="btnrow" id="csB"></div><div id="csV"></div></div>
  <h2>Lab 3 · Which loop?</h2>
  <div class="card"><div id="lcB" class="btnrow"></div><div id="lcO"></div></div>
'''

_pr, _prjs = PR(["Which construct?", "Which loop?", "Match the term", "Put the algorithm in order", "Working out", "Multiple choice"],
  ("Which construct is the statement?", ["Selection", "Iteration", "Assignment"], [("IF Mark > 74 THEN", 0), ("WHILE AllDone() = TRUE", 1), ("Count ← Count + 1", 2), ("CASE OF CaseVar", 0), ("FOR Index ← 1 TO 3", 1), ("Total ← 0", 2)], "Choose, repeat, store."),
  ("Which loop is best?", ["FOR", "WHILE", "REPEAT ... UNTIL"], [("Process exactly 30 students", 0), ("Read lines until the end of a file, which might be empty", 1), ("Ask for a password at least once, until it is right", 2), ("Step through an array of 12 months", 0), ("Add values until the rogue value 0 is input; the first input may already be 0", 1), ("Show a menu and repeat until Quit is chosen", 2)], "Known count: FOR. May run zero times: WHILE. Run at least once: REPEAT."),
  [["Sequence", "Statements run in order"], ["Selection", "A choice (IF, CASE)"], ["Iteration", "Repetition (FOR, WHILE, REPEAT)"], ["Count-controlled", "A set number of repeats"], ["Condition-controlled", "Repeats until a test is satisfied"]],
  ("Put the algorithm for counting the values 100 to 200 that end in 7 in order.", ["Declare ThisInt and Count and set Count to 0", "FOR ThisInt from 100 to 200", "IF ThisInt MOD 10 = 7", "OUTPUT ThisInt and add 1 to Count", "After the loop OUTPUT Count"], "Initialise, loop, test, act, report."),
  [{"q": "How many values from 100 to 200 inclusive end in the digit 7?", "a": 10, "unit": "", "tol": 0.01, "hint": "107, 117 ... 197.", "sol": "<b>10</b>."}, {"q": "How many times does FOR Index ← 1 TO 20 STEP 3 run?", "a": 7, "unit": "", "tol": 0.01, "hint": "1, 4, 7, 10, 13, 16, 19.", "sol": "<b>7</b>."}, {"q": "A REPEAT loop starts with X = 10 and stops UNTIL X >= 5, adding 1 each time. How many times does it run?", "a": 1, "unit": "", "tol": 0.01, "hint": "Tested after the first pass.", "sol": "<b>1</b>."}, {"q": "A WHILE loop starts with X = 10, runs WHILE X < 5. How many times does it run?", "a": 0, "unit": "", "tol": 0.01, "hint": "Tested first.", "sol": "<b>0</b>."}, {"q": "A CASE has clauses 1, 2, 3, 4 and OTHERWISE. CaseVar is 9. Which clause runs?", "a": 5, "unit": "th clause", "tol": 0.01, "hint": "Counting OTHERWISE as the fifth.", "sol": "<b>OTHERWISE</b> (the fifth clause)."}],
  [("The loop that tests its condition last:", ["REPEAT ... UNTIL", "WHILE", "FOR", "CASE"], 0, "Post-condition."), ("A loop that may run zero times:", ["WHILE", "REPEAT ... UNTIL", "Both", "Neither"], 0, "WHILE tests first."), ("CASE OTHERWISE covers:", ["Any value not listed", "Only the first value", "The end of the program", "Errors only"], 0, "Default."), ("A program freezes. A likely cause:", ["A conditional loop whose end condition is never true", "A FOR loop with 10 passes", "An IF statement", "A constant"], 0, "Infinite loop."), ("Initialise a total:", ["Before the loop", "Inside the loop at the start", "After the loop", "Never"], 0, "Else it restarts."), ("Which is not a construct?", ["Variable", "Selection", "Iteration", "Sequence"], 0, "A variable is data.")],
  [("Selection", "Choose a path: IF, CASE."), ("Iteration", "Repeat: FOR, WHILE, REPEAT."), ("FOR", "Count-controlled."), ("WHILE", "Test first; may not run."), ("REPEAT", "Test last; runs once at least."), ("OTHERWISE", "The default CASE clause."), ("Infinite loop", "End condition never true."), ("Initialise", "Set counts and totals before a loop.")])

real = RWNOTE + (
rw("A login screen", "It repeats the password prompt until it is right or the attempts run out: a loop that must run at least once.", "REPEAT ... UNTIL.") +
rw("A cash machine menu", "A menu item is chosen with a CASE: balance, withdraw, deposit or quit, and an invalid key falls through to OTHERWISE.", "CASE.") +
rw("A grade calculator", "A mark above a boundary gives a grade: nested IF statements test the boundaries in order.", "IF.") +
rw("A stopwatch", "A loop adds one every tenth of a second, repeating until the stop button is pressed.", "conditional loop.") +
rw("A game that freezes", "A bug in the loop's end condition means it never finishes and the game stops responding.", "infinite loop.")
)

where = [
  ("M/J 2022", "21", "6", "5 + 4", "Output the values 100 to 200 ending in 7 with a count; rewrite a CASE using IF"),
  ("M/J 2022", "23", "1", "5", "Tick selection, iteration and assignment for five code examples"),
  ("O/N 2023", "22", "2", "5 + 2", "Flowchart for summing after 27 until 0; name and justify a loop structure"),
  ("O/N 2024", "22", "5", "3 + 2 + 2", "Three statements that cause run-time errors; the construct that freezes; rewrite a CASE"),
  ("O/N 2024", "23", "1", "4", "Tick selection, iteration and subroutine for four code examples"),
  ("O/N 2025", "22", "1", "4", "Tick selection, iteration and subroutine for four code examples"),
  ("O/N 2025", "23", "5", "1 + 2", "Combine two CASE clauses into one")]

past = '''  <p class="note">The tick grids and the CASE rewrite appear regularly in Paper 2 question 1 to question 5. In a tick grid, read each row for every construct it contains, not just the first line.</p>
''' + peq(SRC("s22", "21", "Q6"), "5 + 4 marks", "Write / Write",
  "(a) An algorithm will output each integer between 100 and 200 that ends with the digit 7 (for example 107), and then output a final count of the values output. Write pseudocode (declare any variables). (b) CASE OF MySwitch: 1 : ThisChar ← 'a'; 2 : ThisChar ← 'y'; 3 : ThisChar ← '7'; OTHERWISE : ThisChar ← '*'; ENDCASE. Write pseudocode with the same functionality without using a CASE structure.", "FOR 100 TO 200; IF MOD 10 = 7; count. Nested IF with ELSE for OTHERWISE.",
  "<p><b>(a)</b> " + mks(["Declare the loop variable and counter as integers, counter initialised", "Loop 100 to 200 (no step defined)", "Test the value in the loop", "Output the selected value and increment the counter in the loop", "Output the counter after the loop"]) + "</p>" + pc('''
DECLARE ThisInt, Count : INTEGER
Count ← 0
FOR ThisInt ← 100 TO 200
   IF ThisInt MOD 10 = 7 THEN
      OUTPUT ThisInt
      Count ← Count + 1
   ENDIF
NEXT ThisInt
OUTPUT Count''') + "<p>Alternative: <span class=\"mono\">FOR ThisInt ← 107 TO 197 STEP 10</span> with OUTPUT and the counter in the loop.</p><p><b>(b)</b> " + mks(["Any test of MySwitch = 1, 2 or 3", "All three comparisons with the corresponding assignments", "OTHERWISE, or an initial assignment of the default value", "Completely correct IF ... THEN ... ELSE ... ENDIF syntax"]) + "</p>" + pc('''
IF MySwitch = 1 THEN
   ThisChar ← 'a'
ELSE
   IF MySwitch = 2 THEN
      ThisChar ← 'y'
   ELSE
      IF MySwitch = 3 THEN
         ThisChar ← '7'
      ELSE
         ThisChar ← '*'
      ENDIF
   ENDIF
ENDIF'''), "Stopping the loop at 199 or starting at 101, or testing the last digit with a string function instead of MOD 10.") + peq(SRC("s22", "23", "Q1(a)"), "5 marks", "Complete",
  "Each example may include all or part of selection, iteration and assignment. Place one or more ticks in each row: (1) FOR Index ← 1 TO 3, Safe[Index] ← GetResult(), NEXT Index; (2) OTHERWISE : OUTPUT \"ERROR 1202\"; (3) REPEAT UNTIL Index = 27; (4) INPUT MyName; (5) IF Mark > 74 THEN Grade ← 'A' ENDIF.", "A row can have more than one tick.",
  "<p>One mark per row:" + tick(None, ["Pseudocode example", "Selection", "Iteration", "Assignment"], [["FOR Index ← 1 TO 3 / Safe[Index] ← GetResult() / NEXT Index", 0, 1, 1], ["OTHERWISE : OUTPUT \"ERROR 1202\"", 1, 0, 0], ["REPEAT UNTIL Index = 27", 0, 1, 0], ["INPUT MyName", 0, 0, 1], ["IF Mark &gt; 74 THEN Grade ← 'A' ENDIF", 1, 0, 1]]) + "</p>", "Missing the assignment inside the FOR or the IF. The tick grid counts every construct in the lines shown.") + peq(SRC("w23", "22", "Q2"), "5 + 2 marks", "Draw / Give",
  "An algorithm will input a sequence of integers one at a time; ignore all values until 27 is input, then sum the remaining values; stop summing when 0 is input and output the sum. (a) Draw a program flowchart. (b) The solution includes iteration. Give the name of a suitable loop structure and justify your answer.", "Two loops: wait for 27, then sum until 0. Not a known count.",
  "<p><b>(b)</b> " + mks(["Name: a (pre- or post-) conditional loop (WHILE or REPEAT ... UNTIL)", "Justification: the number of iterations is not known, or the loop ends following a specific input"], "a") + "</p><p>The flowchart for part (a) is drawn in the earlier page on flowcharts (section 9.2).</p>", "Choosing FOR: it needs a known number of repeats, and the number of inputs is not known.") + peq(SRC("w24", "22", "Q5"), "3 + 2 + 2 marks", "Identify / Write",
  "A program has a global INTEGER array Data (100 elements). FUNCTION Process(Number : INTEGER, Label : STRING) RETURNS STRING declares Index, Count and ReturnValue and contains: Count ← INT(100 / Number); Index ← Data[Number]; CASE OF (Index MOD 2) with 0 : ReturnValue ← TO_UPPER(RIGHT(Label, Count)) and 1 : ReturnValue ← \"****\"; then RETURN RetVal. (a) Identify three statements that could generate a run-time error and explain how each could. (b) One type of run-time error can make a program stop responding. Identify a programming construct that can generate it and explain why. (c) Write pseudocode with a single selection construct with the same functionality as the CASE.", "Divide by zero; index out of range; RIGHT too long; RetVal does not exist. Conditional loop that never ends. IF ... ELSE.",
  "<p><b>(a)</b> Any three statements (one mark each for the statement and its description):" + tbl(["Statement", "Possible error"], [["Count ← INT(100 / Number)", "Number could be zero: divide by zero"], ["Index ← Data[Number]", "Number could be outside the range of the array indices"], ["ReturnValue ← TO_UPPER(RIGHT(Label, Count))", "Count could be too big, negative or out of range for RIGHT: Label may have too few characters"], ["RETURN RetVal", "There is no variable RetVal: no value to return"]], "t") + "</p><p><b>(b)</b> " + mks(["Construct: a (pre- or post-) conditional loop", "Explanation: the terminating condition is never satisfied"], "a") + "</p><p><b>(c)</b> " + mks(["IF ... THEN ... ELSE ... ENDIF", "Both correct assignments and the correct test"]) + "</p>" + pc('''
IF Index MOD 2 = 0 THEN
   ReturnValue ← TO_UPPER(RIGHT(Label, Count))
ELSE
   ReturnValue ← "****"
ENDIF'''), None) + peq(SRC("w24", "23", "Q1(a)"), "4 marks", "Complete",
  "Place one or more ticks in each row for selection, iteration and subroutine: (1) FOR Index ← 1 TO 3, IF Safe[Index] = TRUE THEN Flap[Index] ← 0 ENDIF, NEXT Index; (2) CASE OF Compound(3); (3) REPEAT UNTIL AllDone() = TRUE; (4) WHILE Result[3] <> FALSE.", "A function call is a subroutine.",
  "<p>One mark per row:" + tick(None, ["Pseudocode example", "Selection", "Iteration", "Subroutine"], [["FOR Index ← 1 TO 3 / IF Safe[Index] = TRUE THEN / Flap[Index] ← 0 / ENDIF / NEXT Index", 1, 1, 0], ["CASE OF Compound(3)", 1, 0, 1], ["REPEAT UNTIL AllDone() = TRUE", 0, 1, 1], ["WHILE Result[3] &lt;&gt; FALSE", 0, 1, 0]]) + "</p>", "Not ticking subroutine for a function call used as the condition: Compound(3) and AllDone() are both calls.") + peq(SRC("w25", "22", "Q1(a)"), "4 marks", "Complete",
  "Place one or more ticks in each row for selection, iteration and subroutine: (1) IF Status = FALSE THEN, FOR Count ← 1 TO 20, CALL Reset(Count), NEXT Count, ENDIF; (2) OTHERWISE : Status ← TRUE; (3) WHILE AllDone() = TRUE; (4) 30 : NextChar ← 'X'.", "OTHERWISE and numbered clauses belong to a CASE: selection.",
  "<p>One mark per row:" + tick(None, ["Pseudocode example", "Selection", "Iteration", "Subroutine"], [["IF Status = FALSE THEN / FOR Count ← 1 TO 20 / CALL Reset(Count) / NEXT Count / ENDIF", 1, 1, 1], ["OTHERWISE : Status ← TRUE", 1, 0, 0], ["WHILE AllDone() = TRUE", 0, 1, 1], ["30 : NextChar ← 'X'", 1, 0, 0]]) + "</p>", None) + peq(SRC("w25", "23", "Q5(b)"), "1 + 2 marks", "Identify / Write",
  "CASE OF CaseVar: clause 1 is Num[Index] ← Num[Index] + Index, Index ← Index + 1, Count ← Count + 1; clause 2 is Num[Index] ← Num[Index] + Index, Index ← Index + 2, Count ← Count + 2; clause 3 is Num[Index] ← Num[Index] * 2, Index ← Index + 3, Count ← Count - 1; clause 4 is Count ← Count + 4; OTHERWISE : Count ← 20. The CASE could be optimised by combining two existing clauses. (i) Identify the two CaseVar values. (ii) Write a single clause to replace them.", "Clauses 1 and 2 differ only by the number added; use CaseVar.",
  "<p><b>(i)</b> " + mks(["1 and 2"], "a") + "</p><p><b>(ii)</b> " + mks(["Use of the variable CaseVar rather than literal values", "A completely correct clause"], "b") + "</p>" + pc('''
1 TO 2 : Num[Index] ← Num[Index] + Index
         Index ← Index + CaseVar
         Count ← Count + CaseVar'''), "Combining clauses 1 and 3: their assignments differ (+ Index against * 2).")

review = req("5 marks", "Write", "Write pseudocode that inputs 10 integers and outputs the number of them that are negative.", "FOR 1 TO 10; IF < 0; count.", "<p>" + mks(["Declare the variables and set the counter to 0", "A FOR loop of 10 iterations", "INPUT in the loop", "IF the value is less than 0 add 1 to the counter", "OUTPUT the counter after the loop"]) + "</p>" + pc("DECLARE Value, Count, N : INTEGER\nCount ← 0\nFOR N ← 1 TO 10\n   INPUT Value\n   IF Value < 0 THEN\n      Count ← Count + 1\n   ENDIF\nNEXT N\nOUTPUT Count"), None) + req("3 marks", "Describe", "Describe the difference between a WHILE loop and a REPEAT ... UNTIL loop.", "Where the test is.", "<p>" + mks(["WHILE tests the condition before each pass; REPEAT tests it after", "so WHILE may run zero times", "and REPEAT always runs at least once"]) + "</p>", None) + req("2 marks", "Explain", "Explain why a loop with the condition WHILE Total < 100 never ends if Total is not changed in the loop.", "The test never changes.", "<p>" + mks(["The condition Total &lt; 100 stays true", "so the loop never stops and the program stops responding"]) + "</p>", None) + req("3 marks", "Write", "Rewrite using IF statements: CASE OF Day, 1 : Name ← \"Mon\", 2 : Name ← \"Tue\", OTHERWISE : Name ← \"?\".", "Nested IF.", "<p>" + mks(["Test Day = 1 and Day = 2 with the assignments", "ELSE for the OTHERWISE value", "Correct IF ... THEN ... ELSE ... ENDIF syntax"]) + "</p>", None) + req("2 marks", "State", "State the construct in each: (a) FOR Count ← 1 TO 5 ... NEXT Count; (b) IF Age >= 18 THEN ... ENDIF.", "Repeat or choose.", "<p>" + mks(["(a) Iteration (count-controlled)", "(b) Selection"]) + "</p>", None)

tips = tips_html([
  ("Match the loop to the question.", "Known count: FOR. Might be zero: WHILE. At least once: REPEAT."),
  ("Initialise first.", "Set count and total to 0 before the loop."),
  ("Tick every construct.", "Read the whole row; an IF inside a FOR is both."),
  ("Calls are subroutines.", "A function used in a condition counts."),
  ("CASE needs OTHERWISE.", "Or the equivalent final ELSE."),
  ("Check both ends.", "100 TO 200 includes 100 and 200."),
], [("selection", "A statement that chooses what to do."), ("iteration", "Repeating statements."), ("a count-controlled loop", "A loop with a set number of repeats (FOR)."), ("a conditional loop", "A loop that repeats until a condition is met (WHILE, REPEAT).")],
  [("Write", "Write pseudocode."), ("Complete", "Fill the grid or table."), ("Identify", "Name it."), ("Justify", "Give a reason for the choice.")]) + FC

js = AKJS + AK20JS + r'''
(function () {
  const draw = (s) => { const k = Math.round(s.i); const L = [["FOR Count ← 1 TO 3", "runs 3 times: count-controlled"], ["WHILE X < 3", "tests first, then runs"], ["REPEAT ... UNTIL X >= 3", "runs, then tests"], ["Loop ends: test satisfied", "(or counter past the end)"]]; let o = SV.rect(10, 10, 320, 34, k === 3 ? "f2" : "cell", { rx: 6 }) + SV.text(24, 33, L[k][0], "lbl bd", { style: "font-size:14px;font-family:monospace" }); o += SV.text(24, 66, L[k][1], "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stA"), { w: 340, h: 82, label: "Loops", base: { i: 0 }, draw, tween: 100, dwell: 2000, steps: ["FOR repeats a set number of times.", "WHILE tests before each pass.", "REPEAT tests after each pass.", "All three end when the condition says so."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const cl = [1, 2, 3, "OTHERWISE"]; const draw = (s) => { const k = Math.round(s.i); let o = SV.text(14, 18, "CaseVar = " + [2, 2, 7][k > 2 ? 2 : k > 0 ? 1 : 0], "lbl bd", { style: "font-size:13px" }); const val = [2, 2, 7][k > 2 ? 2 : k > 0 ? 1 : 0]; const hit = val === 1 ? 0 : val === 2 ? 1 : val === 3 ? 2 : 3; cl.forEach((c, i) => o += SV.rect(14, 28 + i * 28, 200, 24, k >= 1 && i === hit ? "f3" : "cell", { rx: 4 }) + SV.text(22, 45 + i * 28, c + " : ThisChar ← " + ["'a'", "'y'", "'7'", "'*'"][i], "lbl bd", { style: "font-size:12px;font-family:monospace" })); o += SV.text(14, 152, k === 0 ? "Test CaseVar against each clause value" : k === 1 ? "Only the matching clause runs" : "Nothing matches: OTHERWISE runs", "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stB"), { w: 330, h: 165, label: "CASE", base: { i: 0 }, draw, tween: 100, dwell: 2200, steps: ["CaseVar is compared with each value.", "CaseVar = 2: clause 2 runs, the others are skipped.", "CaseVar = 7 matches nothing, so OTHERWISE runs."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const vals = [4, 9, -3, 6]; const draw = (s) => { const k = Math.round(s.i); let o = ""; vals.forEach((v, i) => o += SV.rect(14 + i * 60, 14, 52, 26, i < k ? "f3" : "cell", { rx: 4 }) + SV.text(40 + i * 60, 32, v, "lbl bd", { "text-anchor": "middle" })); const t = vals.slice(0, k).reduce((a, b) => a + b, 0); o += SV.text(14, 66, "Total = " + t + "     Count = " + k, "lbl bd t3", { style: "font-size:14px" }); o += SV.text(14, 88, k === 0 ? "Set Total ← 0 and Count ← 0 before the loop" : k < 4 ? "Total ← Total + value; Count ← Count + 1" : "Loop finished: OUTPUT Total, Count", "lbl", { style: "font-size:12px" }); return o; };
  Lib.stepper($("#stC"), { w: 270, h: 104, label: "Total and count", base: { i: 0 }, draw, tween: 100, dwell: 1800, steps: ["Initialise.", "Add the first value.", "Add the second.", "Add the third.", "Add the fourth: the loop ends."].map((c, i) => ({ cap: c, s: { i } })) });
})();

(function () {
  const inp = $("#lp_x"); const paint = () => { let x0 = Math.round(+inp.value || 0); const run = (kind) => { let x = x0, n = 0; if (kind === "FOR") { for (let c = x0; c <= 5; c++) n++; return n; } if (kind === "WHILE") { while (x < 5 && n < 100) { x++; n++; } return n; } do { x++; n++; } while (!(x >= 5) && n < 100); return n; };
    $("#lpV").innerHTML = '<div class="tw"><table class="t mono"><tr><th>Loop</th><th>Test</th><th>Times it runs</th></tr>' + [["FOR X ← " + x0 + " TO 5", "counter ≤ 5", run("FOR")], ["WHILE X < 5", "before each pass", run("WHILE")], ["REPEAT ... UNTIL X >= 5", "after each pass", run("REPEAT")]].map((r) => `<tr><td>${r[0]}</td><td>${r[1]}</td><td><b>${r[2]}</b></td></tr>`).join("") + "</table></div>" + (x0 >= 5 ? '<div class="verdict">X already meets the end condition: WHILE and FOR run zero times, but REPEAT still runs once.</div>' : ""); };
  inp.oninput = paint; paint();
})();
(function () {
  const bar = $("#csB"); const out = $("#csV"); const map = { 1: "'a'", 2: "'y'", 3: "'7'" };
  [1, 2, 3, 4, 7].forEach((v) => { const b = document.createElement("button"); b.textContent = "MySwitch = " + v; b.onclick = () => { bar.querySelectorAll("button").forEach((x) => x.className = x === b ? "on" : ""); const r = map[v] || "'*'"; out.innerHTML = `<div class="verdict">ThisChar = <b>${r}</b> ${map[v] ? "" : "(OTHERWISE / the final ELSE)"}</div><p class="mono">CASE: matches ${map[v] ? "clause " + v : "no clause, so OTHERWISE"}.<br>IF: ${v === 1 ? "the first test is true" : v === 2 ? "the first test is false, the second is true" : v === 3 ? "the first two tests are false, the third is true" : "all three tests are false, so ELSE"}.</p>`; }; bar.appendChild(b); });
})();
btnTable("lcB", "lcO", [
  ["Process exactly 30 students", "FOR", "the count is known"],
  ["Read lines until the end of a file that may be empty", "WHILE", "may run zero times"],
  ["Ask for a PIN at least once, until it is right", "REPEAT ... UNTIL", "must run once before the test"],
  ["Add numbers until a rogue value 0, even if the first is 0", "WHILE", "test before the first pass"],
  ["Step through the 12 months in an array", "FOR", "the count is known"]
], ["Task", "Loop", "Why"]);
''' + _prjs

finish("as-11-2-programming-constructs", "as112", "Programming Constructs",
  "Selection with IF and CASE, count-controlled and condition-controlled loops, counting and totalling and run-time errors, with animations, labs and the real Paper 2 questions from 2021 to 2026.",
  "11.2", "11 · Programming", "section 11.2 Programming constructs", learn, watch, explore, _pr, real, where, past, review,
  "Part 1 is real 9618 questions on programming constructs (Paper 2), 2021 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", tips, js)
