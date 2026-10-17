"""IGCSE CS exam technique 3: Paper 2 algorithms (trace tables, errors, flowcharts, pseudocode, test data). Run: python3 tools/artifact-kit/mk_cx3.py"""
from csk import *

learn = '''
  <div class="card big"><h3>This part in five sentences</h3>
  <p>Paper 2 is a <b>75-mark written paper in 1 hour 45 minutes</b> on Topics 7 to 10, with about 60% of its marks for applying knowledge (AO2), and <b>no calculator</b>. Most of the marks outside the last question come from a few tasks that repeat every series: <b>complete a trace table</b>, <b>find and fix errors</b>, <b>draw a flowchart</b>, <b>write short pseudocode</b>, <b>suggest test data</b> and <b>name checks</b>. The syllabus publishes the pseudocode that the paper uses, and the examiner reports say that candidates who follow it exactly score the most, while answers written in program code earn <b>no marks</b> unless it is the 15-mark scenario question. Logic matters more than syntax, but <b>precision</b> matters: <i>x &gt; y</i> is accepted and "x is greater than y" is not. Learn the standard patterns for counting, totalling, finding the largest and smallest, searching and sorting, because most algorithm marks are for <b>initialising, looping, comparing and updating</b> in the right places.</p></div>

  <h2>1 · The facts</h2>
  <div class="tw"><table class="t">
    <tr><th>Feature</th><th>Detail</th></tr>
    <tr><td><b>Paper</b></td><td>Paper 2 Algorithms, Programming and Logic (variants 21 to 23 in the main series)</td></tr>
    <tr><td><b>Time and marks</b></td><td>1 hour 45 minutes, 75 marks. The final question is worth 15 marks and the syllabus says to spend about 30 minutes on it, which leaves about 75 minutes for the other 60 marks: 1.25 minutes a mark.</td></tr>
    <tr><td><b>Content</b></td><td>Topics 7 to 10: algorithm design and problem solving, programming, databases, Boolean logic</td></tr>
    <tr><td><b>Pseudocode</b></td><td>Solutions written in program code are not awarded marks, except in the 15-mark scenario question, where pseudocode, Python, Visual Basic or Java may be used</td></tr>
    <tr><td><b>Syntax</b></td><td>Knowledge of programming language syntax is not examined; the logic is more important than the syntax. The pseudocode in the syllabus is the basis of the questions.</td></tr>
    <tr><td><b>Assessment objectives</b></td><td>Approximately AO1 20%, AO2 60%, AO3 20%</td></tr>
    <tr><td><b>Equipment</b></td><td>Black or dark blue pen; HB pencil for diagrams; no calculator</td></tr>
  </table></div>

  <h2>2 · Where the 75 marks sit</h2>
  <p>This is Oct/Nov 2024 paper 21, with marks added up from the published mark scheme. This review covers every question in the table except the logic and database ones and the last question, which have their own reviews.</p>
  <div class="tw"><table class="t">
    <tr><th>Q</th><th>Task</th><th>Marks</th></tr>
    <tr><td>1, 2</td><td>Tick the check used for verification; tick what shows the inputs and output of a Boolean expression</td><td>2</td></tr>
    <tr><td>3</td><td>Match four operators to operator types</td><td>4</td></tr>
    <tr><td>4</td><td>Identify three stages of the program development life cycle</td><td>3</td></tr>
    <tr><td>5</td><td>Describe three methods to design and construct a solution</td><td>6</td></tr>
    <tr><td>6</td><td>Complete an algorithm; write output pseudocode; suggest meaningful identifiers</td><td>9</td></tr>
    <tr><td>7</td><td>Logic circuit: write the expression, complete the truth table</td><td>7</td></tr>
    <tr><td>8</td><td>Complete a flowchart; write file-handling pseudocode; explain why data is stored in a file</td><td>11</td></tr>
    <tr><td>9</td><td>Find four errors in pseudocode; give the range; complete a trace table</td><td>8</td></tr>
    <tr><td>10</td><td>Database: records, primary key, SQL output, complete SQL</td><td>10</td></tr>
    <tr><td>11</td><td>15-mark scenario: write a program</td><td>15</td></tr>
  </table></div>

  <h2>3 · The syllabus pseudocode on one page</h2>
  <p>These are the constructs the questions use. Keywords are in capitals, assignment is ←, THEN and ELSE are indented two spaces, and identifiers use mixed case such as <i>TotalMarks</i>.</p>
  <div class="tw"><table class="t">
    <tr><th>Task</th><th>Pseudocode</th></tr>
    <tr><td>Declare, assign, constant</td><td><code>DECLARE Count : INTEGER</code> · <code>Count ← 0</code> · <code>CONSTANT Limit ← 50</code></td></tr>
    <tr><td>Input and output</td><td><code>INPUT Mark</code> · <code>OUTPUT "Total is ", Total</code></td></tr>
    <tr><td>Selection</td><td><code>IF … THEN … ELSE … ENDIF</code> · <code>CASE OF … OTHERWISE … ENDCASE</code></td></tr>
    <tr><td>Count-controlled loop</td><td><code>FOR Index ← 1 TO 10 STEP 1 … NEXT Index</code></td></tr>
    <tr><td>Pre-condition loop</td><td><code>WHILE Count &lt; 10 DO … ENDWHILE</code> (tests first, may run zero times)</td></tr>
    <tr><td>Post-condition loop</td><td><code>REPEAT … UNTIL Mark = -1</code> (tests last, runs at least once)</td></tr>
    <tr><td>Arrays</td><td><code>DECLARE Names : ARRAY[1:30] OF STRING</code> · <code>Names[Index] ← "Ali"</code> · 2D: <code>Grid[Row, Column]</code></td></tr>
    <tr><td>Operators</td><td><code>+ − * / ^ MOD DIV</code> · <code>= &lt; &lt;= &gt; &gt;= &lt;&gt;</code> · <code>AND OR NOT</code></td></tr>
    <tr><td>Library routines</td><td><code>LENGTH SUBSTRING LCASE UCASE ROUND RANDOM</code></td></tr>
    <tr><td>Files</td><td><code>OPENFILE "Notes.txt" FOR WRITE</code> · <code>WRITEFILE "Notes.txt", Line</code> · <code>READFILE</code> · <code>CLOSEFILE</code></td></tr>
    <tr><td>Procedures and functions</td><td><code>PROCEDURE … ENDPROCEDURE</code> · <code>CALL Name(Value)</code> · <code>FUNCTION Name(…) RETURNS INTEGER … RETURN … ENDFUNCTION</code></td></tr>
  </table></div>
  <div class="tw"><table class="t">
    <tr><th>Common slip</th><th>Correct form</th></tr>
    <tr><td><code>IF x is greater than y</code></td><td><code>IF X &gt; Y</code> (precision is required)</td></tr>
    <tr><td><code>Total = Total + 1</code></td><td><code>Total ← Total + 1</code> (= is for comparing)</td></tr>
    <tr><td><code>PRINT Total</code> or <code>print(Total)</code></td><td><code>OUTPUT Total</code> in a pseudocode question</td></tr>
    <tr><td><code>ELSEIF</code>, <code>ENDCASE</code> to close an IF</td><td><code>ENDIF</code> closes IF; <code>ENDCASE</code> closes CASE</td></tr>
    <tr><td><code>REPEAT … WHILE …</code></td><td><code>REPEAT … UNTIL …</code></td></tr>
    <tr><td>An array called <code>Array</code></td><td>A name that says what it holds: <code>Marks</code>, <code>MemberTime</code></td></tr>
    <tr><td>Python in a "write pseudocode" question</td><td>The examiner report says program code was used when the question asked for pseudocode; it earns no marks</td></tr>
  </table></div>

  <h2>4 · The standard methods</h2>
  <p>The syllabus limits standard methods to linear search, bubble sort, totalling, counting and finding the maximum, minimum and average. In each, the marks are for the same four things: <b>initialise</b>, <b>loop</b>, <b>compare or update</b>, and <b>output</b>. The examiner report for Oct/Nov 2024 says the maximum and minimum variables must be initialised, and totals set to zero before they are used.</p>
  <h3>Counting and totalling</h3>
''' + code(["Total ← 0", "Count ← 0", "FOR Index ← 1 TO 50", "    IF Marks[Index] > 0", "      THEN", "        Total ← Total + Marks[Index]", "        Count ← Count + 1", "    ENDIF", "NEXT Index", "Average ← Total / Count"]) + '''
  <h3>Largest and smallest</h3>
''' + code(["Largest ← Marks[1]", "Smallest ← Marks[1]", "FOR Index ← 2 TO 50", "    IF Marks[Index] > Largest", "      THEN", "        Largest ← Marks[Index]", "    ENDIF", "    IF Marks[Index] < Smallest", "      THEN", "        Smallest ← Marks[Index]", "    ENDIF", "NEXT Index"]) + '''
  <h3>Linear search</h3>
''' + code(["Found ← FALSE", "Index ← 1", "WHILE Found = FALSE AND Index <= 50 DO", "    IF Names[Index] = SearchName", "      THEN", "        Found ← TRUE", "      ELSE", "        Index ← Index + 1", "    ENDIF", "ENDWHILE"]) + '''
  <h3>Bubble sort with the two efficiency features</h3>
  <p>The Oct/Nov 2024 mark scheme gives the two features that make a bubble sort efficient: a flag that shows whether a swap was made, so the loop stops once the data is in order, and an inner loop whose limit reduces after each pass, so fewer comparisons are needed.</p>
''' + code(["Limit ← 100", "Pass ← 1", "Swapped ← TRUE", "WHILE Swapped = TRUE AND Pass <= Limit - 1 DO", "    Swapped ← FALSE", "    FOR Counter ← 1 TO Limit - Pass", "        IF ItemList[Counter] > ItemList[Counter + 1]", "          THEN", "            Temp ← ItemList[Counter]", "            ItemList[Counter] ← ItemList[Counter + 1]", "            ItemList[Counter + 1] ← Temp", "            Swapped ← TRUE", "        ENDIF", "    NEXT Counter", "    Pass ← Pass + 1", "ENDWHILE"]) + '''

  <h2>5 · Trace tables</h2>
  <p>The syllabus says a trace table records, at each step, the variables, the outputs and the user prompts. The examiner reports give three rules that cost marks every series:</p>
  <ul>
    <li><b>Record every assignment.</b> Each time a variable is given a value, the new value goes in its column.</li>
    <li><b>No quotation marks on outputs.</b> The output column shows what the user sees.</li>
    <li><b>Stop when the stopping condition is met.</b> Once the terminating value is processed, make no further entries, even if there is more input data.</li>
  </ul>
  <p>Here is the trace table for the Oct/Nov 2024 paper 22 question: the algorithm multiplies the input by every whole number below it, stops at −1, and the input data is 5, 6, −1, 20, 9, 4. The mark scheme gives one mark for each correct column, with the Answer column split into the rows to the first output and the rest.</p>
  <div class="tw"><table class="t mx">
    <tr><th>Value</th><th>Count</th><th>Answer</th><th>OUTPUT</th></tr>
    <tr><td>5</td><td></td><td>5</td><td></td></tr><tr><td></td><td>4</td><td>20</td><td></td></tr><tr><td></td><td>3</td><td>60</td><td></td></tr><tr><td></td><td>2</td><td>120</td><td></td></tr><tr><td></td><td>1</td><td>120</td><td>120</td></tr>
    <tr><td>6</td><td></td><td>6</td><td></td></tr><tr><td></td><td>5</td><td>30</td><td></td></tr><tr><td></td><td>4</td><td>120</td><td></td></tr><tr><td></td><td>3</td><td>360</td><td></td></tr><tr><td></td><td>2</td><td>720</td><td></td></tr><tr><td></td><td>1</td><td>720</td><td>720</td></tr>
    <tr><td>−1</td><td></td><td></td><td></td></tr>
  </table></div>
  <p>The values 20, 9 and 4 never appear, because the algorithm stopped at −1. The same paper asked for the purpose (it multiplies a number by each number below it, which gives its factorial) and for the problem when the value is 1, 0 or below −1: the loop counter starts below 1 and never reaches it, so the loop is endless.</p>
  <div class="tip"><b class="h">Exam tip</b>Write the column headings first, in the order the variables are first used, and keep a ruler under the row you are on. When you reach the stopping value, draw a line and stop.</div>

  <h2>6 · Finding and fixing errors</h2>
  <p>Two real questions show the pattern. In both, the answer is a <b>line number</b> and a <b>correction</b>. The Oct/Nov 2024 report on a flowchart question in paper 23 notes that many candidates identified the same error twice, so list each error once.</p>
  <div class="tw"><table class="t">
    <tr><th>Question</th><th>Errors the mark scheme accepted</th><th>The type of error</th></tr>
    <tr><td><b>Check a temperature in a range</b> (Oct/Nov 2024, paper 21, 4 errors)</td><td>Line 03: <i>Temp</i> should be <i>Temperature</i><br>Line 04: <code>=</code> should be <code>&lt;&gt;</code><br>Line 14: <code>OR</code> should be <code>AND</code><br>Line 19: <code>WHILE</code> should be <code>UNTIL</code></td><td>Wrong variable name; wrong comparison; wrong logical operator; wrong loop keyword</td></tr>
    <tr><td><b>Bubble sort</b> (Oct/Nov 2024, paper 22, 5 errors)</td><td>Line 02: loop counter declared <code>STRING</code>, should be <code>INTEGER</code><br>Line 09: <code>Temp ← TRUE</code> should be <code>Swapped ← TRUE</code><br>Line 10: <code>OR</code> should be <code>AND</code><br>Line 17: <code>ItemList[Counter]</code> should be <code>ItemList[Counter + 1]</code><br>Line 19: <code>ENDCASE</code> should be <code>ENDIF</code></td><td>Wrong data type; wrong variable; wrong operator; wrong index; wrong closing keyword</td></tr>
  </table></div>
  <ol>
    <li><b>Check the structure first.</b> Every IF needs an ENDIF, every REPEAT an UNTIL, every FOR a NEXT.</li>
    <li><b>Check every variable name</b> against the declarations.</li>
    <li><b>Check every condition and operator</b>: comparisons, AND against OR, the stopping value.</li>
    <li><b>Run one small example</b> through the algorithm to catch an index or initialisation error.</li>
    <li><b>Write each error once</b>, with its line number and the corrected line.</li>
  </ol>

  <h2>7 · Flowcharts</h2>
  <p>Flowchart questions are marked with one mark for each of a short list of points. For a count-controlled totalling flowchart in Oct/Nov 2024 the list was: two labelled terminators, loop initialisation, incrementation and termination, input with a prompt, total initialised and added to, output with a message, and a fully correct chart with arrows, Yes/No labels and symbols. The examiner reports add that candidates lost marks for wrong symbols and for flow lines without arrows.</p>
  <div class="tw"><table class="t">
    <tr><th>Symbol</th><th>Use it for</th><th>Rule</th></tr>
    <tr><td><b>Terminator</b> (rounded box)</td><td>START and STOP</td><td>Label both</td></tr>
    <tr><td><b>Process</b> (rectangle)</td><td>Assignments and calculations</td><td>e.g. <code>Total ← Total + Number</code></td></tr>
    <tr><td><b>Input / output</b> (parallelogram)</td><td>INPUT and OUTPUT, including the prompt</td><td>Prompts and messages go here too</td></tr>
    <tr><td><b>Decision</b> (diamond)</td><td>A condition with a Yes and a No exit</td><td>Label both exits; one question only</td></tr>
    <tr><td><b>Subroutine</b></td><td>A call to a separate flowchart</td><td>Not for ordinary steps</td></tr>
    <tr><td><b>Flow line</b></td><td>Direction of control</td><td>Every line has an arrowhead; lines go to a symbol or terminator</td></tr>
  </table></div>

  <h2>8 · Validation, verification and test data</h2>
  <div class="tw"><table class="t">
    <tr><th>Idea</th><th>Meaning in the syllabus</th><th>Careful with</th></tr>
    <tr><td><b>Validation</b></td><td>Checks that data is reasonable: range, length, type, presence, format, check digit</td><td>The report says many candidates named a validation check when verification was asked for</td></tr>
    <tr><td><b>Verification</b></td><td>Checks the data was entered correctly: visual check, double entry check</td><td>Outline = name plus how it works: double entry means entered twice, compared, re-entry requested if they differ</td></tr>
    <tr><td><b>Normal data</b></td><td>Data that should be accepted</td><td>Give an actual value</td></tr>
    <tr><td><b>Abnormal data</b></td><td>Data that should be rejected</td><td>Give an actual value</td></tr>
    <tr><td><b>Extreme data</b></td><td>The largest or smallest acceptable value</td><td>It is accepted</td></tr>
    <tr><td><b>Boundary data</b></td><td>The largest or smallest acceptable value and the matching smallest or largest rejected value</td><td>Two values: one accepted and one rejected</td></tr>
  </table></div>
  <p>A real Oct/Nov 2024 question asked for two items of test data to test a limit of 80 for whole numbers, with a reason for each. The mark scheme: 80, the largest accepted number at the limit; and 81, the smallest rejected number. The report says many candidates named types of test data or gave any values. In another Oct/Nov 2024 question (paper 23) each type needed <b>the name, the actual data and whether it is accepted or rejected</b>, and boundary data needed two values, one accepted and one rejected.</p>

  <h2>9 · Short written answers in Paper 2</h2>
  <ul>
    <li><b>Purpose of an algorithm:</b> say what it achieves with the input, not how it loops. "It multiplies the input by every whole number below it" earns the mark; "it loops" does not.</li>
    <li><b>Program development life cycle:</b> analysis, design, coding, testing. Analysis: abstraction (removing unnecessary detail), decomposition (inputs, processes, outputs, storage), identifying the problem and the requirements.</li>
    <li><b>Design methods:</b> structure diagram (a hierarchy showing a program broken into parts), flowchart (the ordered steps), pseudocode (what the program does in plain language). Each method named earns one mark and its description another.</li>
    <li><b>Why store data in a file:</b> it can be retrieved when needed, and storage is non-volatile. The report says candidates wrote about checking a password instead of why it is stored.</li>
    <li><b>Meaningful identifiers:</b> <i>Marks</i>, <i>Counter</i>, <i>Total</i>. <i>Array</i> is not meaningful. Maintainable code uses comments, procedures and functions, and white space.</li>
  </ul>

  <h2>10 · Common ways to lose marks</h2>
  <ul>
    <li><b>Program code in a pseudocode question.</b></li>
    <li><b>Not initialising</b> a total, a counter, or the largest and smallest.</li>
    <li><b>Quotation marks in the output column</b> of a trace table, or entries after the stopping value.</li>
    <li><b>Wrong flowchart symbols</b>, or lines with no arrows, or decisions with one exit labelled.</li>
    <li><b>Naming a type of test data</b> instead of giving values, or giving one value for boundary data.</li>
    <li><b>Naming a validation check</b> when verification is asked for.</li>
    <li><b>Listing the same error twice</b> in an error-finding question.</li>
    <li><b>Vague descriptions of purpose</b> such as "it counts" without saying what.</li>
  </ul>
'''

watch = '''
  <h2>1 · Building a flowchart for six marks</h2>
  <p>Press Play, or click the numbered steps. Each step adds the part that earns a mark.</p>
  <div id="stA"></div>
  <h2>2 · Finding the four errors</h2>
  <div id="stB"></div>
  <h2>3 · Choosing test data for a limit</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Trace it row by row</h2>
  <p>Choose an algorithm, then press <b>Next row</b> to run it one step at a time. The highlighted line is the line just run.</p>
  <div id="trB" class="btnrow"></div>
  <div id="trO" class="card"></div>

  <h2>Lab 2 · Test data for a rule</h2>
  <p>Choose a rule to see the test data that covers it, whether each value is accepted or rejected, and the reason that earns the second mark.</p>
  <div class="card"><div id="tdB" class="btnrow"></div><div id="tdO"></div></div>

  <h2>Lab 3 · Fix the line</h2>
  <p>Choose a faulty line to see the correction and the reason it costs a mark.</p>
  <div class="card"><div id="fxB" class="btnrow"></div><div id="fxO"></div></div>

  <h2>Lab 4 · Validation or verification?</h2>
  <p>Choose a check to see which it is, what it does and the sentence that earns the mark for "outline".</p>
  <div class="card"><div id="vvB" class="btnrow"></div><div id="vvO"></div></div>
'''

practise = '''
  <h2>1 · Validation or verification?</h2><div id="cl1" class="card"></div>
  <h2>2 · Which flowchart symbol?</h2><div id="cl2" class="card"></div>
  <h2>3 · Put the steps for a trace table in order</h2><div id="o1" class="card"></div>
  <h2>4 · Match the type of test data to its meaning</h2><div id="m1" class="card"></div>
  <h2>5 · Calculations</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = '<p class="note">These come from the Principal Examiner Reports for Cambridge IGCSE Computer Science, which describe what candidates actually wrote. The wording is ours.</p>\n' + (
rw("Program code in a pseudocode question", "Oct/Nov 2024, papers 21 and 23: asked to write pseudocode, many candidates used program code or pseudocode that did not match the syllabus. The syllabus says solutions in program code are not awarded marks except in the 15-mark scenario question.", "any 'write pseudocode' question: use the syllabus keywords (OUTPUT, ←, ENDIF) and nothing else.") +
rw("An array called Array", "Oct/Nov 2024, papers 21 and 23: when asked for meaningful identifiers, many candidates used Array for the array, which is not meaningful. The mark scheme accepts names such as MyArray or Names.", "name things for what they hold: Marks, MemberTime, Total, Counter.") +
rw("Quotation marks and extra rows in a trace table", "Oct/Nov 2024, paper 21: quotation marks on outputs are incorrect, and once the stopping condition has been met no further entries should be made. In paper 23: each time a variable is assigned a value it must be recorded in the table.", "trace tables: record every assignment, write outputs as the user sees them, stop at the stopping value.") +
rw("Naming validation when verification is asked", "Oct/Nov 2024, paper 22: a significant number of candidates named validation checks such as range check or presence check when asked for a verification check. Visual check and double entry check were the accepted answers.", "check the word: validation, verification.") +
rw("Test data without the detail", "Oct/Nov 2024, paper 22: a significant number of candidates named types of test data or gave any values. The question asked for test data that tested the limit of 80, so boundary data was needed: 80 as the highest accepted and 81 as the first rejected.", "give the actual value, say if it is accepted or rejected, and give the reason.") +
rw("The same error twice", "Oct/Nov 2024, paper 23: many candidates identified the same error twice by swapping Yes and No on one decision box in a flowchart. The question had different errors to find.", "list each error once; if you have found the same error twice, look for another.") +
rw("Wrong symbols and flow lines with no arrows", "Oct/Nov 2024, paper 21: many candidates used incorrect flowchart symbols or did not complete flow lines with arrows. Flow lines should go to a terminator or a subroutine.", "flowcharts: use a terminator, a process, a decision and an input/output box, and put an arrowhead on every line.")
)

items = [("w24_21", "6(a)", 3), ("w24_21", "6(c)", 3), ("w24_21", "9", 8), ("w24_22", "4", 8), ("w24_22", "7", 8), ("w24_22", "3(b)", 6), ("w24_21", "8", 11),
         ("w23_21", "8(c)", 4), ("w24_22", "8", 4), ("w24_22", "6", 2), ("w24_21", "5", 6), ("w24_22", "5(b)", 3), ("w24_22", "10", 6), ("w23_21", "6(d)", 2)]

exam = cs_exam("algorithms and programming",
  "Fourteen Paper 2 questions on completing and correcting algorithms, tracing, flowcharts, test data, file handling and design. Code and figures are our own versions of the originals with the same logic, so the mark scheme points still apply. Try the question first, then open the mark scheme points.",
  crows(items), [
  ceq(CP("w24_21", "6(a)"), "[3]", "An incomplete algorithm counts the zero readings in an array and totals the other readings. Complete it." + qc(['DECLARE A[1:40] : INTEGER', 'DECLARE C : INTEGER', 'DECLARE Z : INTEGER', 'DECLARE S : INTEGER', 'S ← 0', '...............................', 'FOR C ← 1 TO 40', '    IF A[C] ...............', '      THEN', '        Z ← Z + 1', '      ELSE', '        S ← S + A[C]', '    ENDIF', '...............................']) + "",
    ["One mark for each of three points: initialise the zero counter, Z ← 0, before the loop", "The comparison that tests for a zero element: = 0", "The loop closing statement: NEXT C"],
    "<p>Check what is used before it is set. S is set to 0 on line 5, so Z must be set on the blank line. Check the IF line against the THEN and ELSE, and close the FOR with NEXT and the same variable.</p>"),
  ceq(CP("w24_21", "6(c)"), "[3]", "Meaningful identifiers have not been used in the algorithm above. Suggest meaningful identifiers for the array A, and for the variables C, Z and S.",
    ["One mark for a meaningful identifier for the array, such as Readings or MyArray", "One mark for two meaningful identifiers for variables, two marks for all three, such as Index, ZeroCount, Total", "'Array' on its own was not accepted as meaningful"],
    "<p>The name should say what the thing holds or does: <i>Readings</i>, <i>Index</i>, <i>ZeroCount</i>, <i>Total</i>. Use mixed case and no spaces, as in the syllabus.</p>"),
  ceq(CP("w24_21", "9"), "[8]", "A program checks a quiz mark between 0 and 20 inclusive. Input stops when 99 is entered. (a) Identify four errors and correct each. (b) Give the range of marks accepted. (c) Complete the trace table for the corrected program using 7, 21, 0, 99, 5." + qc(['REPEAT', '    OUTPUT "Enter the mark "', '    INPUT Mrk', '    IF Mark = 99', '      THEN', '        IF Mark > 20', '          THEN OUTPUT "Too high"', '        ENDIF', '        IF Mark < 0', '          THEN OUTPUT "Too low"', '        ENDIF', '        IF Mark >= 0 OR Mark <= 20', '          THEN OUTPUT "Valid"', '        ENDIF', '    ENDIF', 'WHILE Mark = 99']) + "",
    ["(a) Four errors, each with its correction: the variable is Mrk but everywhere else Mark; the IF should test Mark <> 99; the OR should be AND; the REPEAT must end with UNTIL Mark = 99, not WHILE", "(b) Two marks: greater than or equal to 0, and less than or equal to 20", "(c) One mark for each correct column, maximum two: Mark column 7, 21, 0, 99; output column Valid, Too high, Valid, with the prompt before each input; nothing after 99"],
    "<p>Read for structure (REPEAT…UNTIL), then names, then operators. For the trace table, the final 5 is never read. Remember: no quotation marks on the outputs.</p>"),
  ceq(CP("w24_22", "4"), "[8]", "A bubble sort puts the 30 names in NameList into alphabetical order. (a) Identify five errors and correct each. (b) Explain why the corrected algorithm is efficient." + qc(['DECLARE NameList : ARRAY[1:30] OF STRING', 'DECLARE Index : STRING', 'DECLARE Last : INTEGER', 'DECLARE Round : INTEGER', 'DECLARE Changed : BOOLEAN', 'DECLARE Hold : STRING', 'Last ← 30', 'Round ← 1', 'Hold ← TRUE', 'WHILE Changed = TRUE OR Round <= Last - 1 DO', '    Changed ← FALSE', '    FOR Index ← 1 TO Last - Round', '        IF NameList[Index] > NameList[Index + 1]', '          THEN', '            Hold ← NameList[Index]', '            NameList[Index] ← NameList[Index + 1]', '            NameList[Index] ← Hold', '            Changed ← TRUE', '        ENDCASE', '        Round ← Round + 1', '    NEXT Index', 'ENDWHILE']) + "",
    ["(a) One mark each: line 2, Index declared STRING should be INTEGER; line 9, Hold ← TRUE should be Changed ← TRUE", "Line 10, OR should be AND; line 17, NameList[Index] ← Hold should be NameList[Index + 1] ← Hold; line 19, ENDCASE should be ENDIF", "(b) Up to three: a flag, set to FALSE at the start of each pass, shows whether a swap was made", "…so the loop stops once the list is sorted; the limit of the inner loop reduces after each pass, so fewer comparisons are needed"],
    "<p>Five errors of five different kinds: data type, variable name, operator, index and closing keyword. For part (b) name both features and what each saves.</p>"),
  ceq(CP("w24_22", "7"), "[8]", "An algorithm stops when −1 is entered. (a) Complete the trace table for the input data 4, 5, −1, 12, 3. (b) State the purpose of the algorithm. (c) Describe the problem if the value 0, 1 or less than −1 is input." + qc(['REPEAT', '    INPUT Number', '    IF Number <> -1', '      THEN', '        Product ← Number', '        FOR Step ← Number - 1 TO 1 STEP -1', '            Product ← Product * Step', '        NEXT Step', '        OUTPUT Product', '    ENDIF', 'UNTIL Number = -1']) + "Columns: Number, Step, Product, OUTPUT.",
    ["(a) Five marks: correct Number column; correct Step column; the Product column down to the first output; the rest of the Product column; the OUTPUT column", "For 4: Product 4, then Step 3 → 12, Step 2 → 24, Step 1 → 24, OUTPUT 24. For 5: 5, then 20, 60, 120, 120, OUTPUT 120. Then −1; 12 and 3 are never read", "(b) It multiplies the input by every whole number below it, down to 1 (the factorial)", "(c) Two marks: the program would accept the value and enter the FOR loop; the counter would keep reducing and never reach 1, as it would already be less than 1, so the loop would be endless"],
    "<p>Record the Product after every pass of the loop. Stop at −1. For (c), the mark scheme says the program accepts the value and enters the FOR loop, and that the counter never reaches 1.</p>"),
  ceq(CP("w24_22", "3(b)"), "[6]", "Draw a flowchart that: uses a count-controlled loop from 1 to 30; asks with a suitable prompt for a mark between 0 and 100; totals the marks as they are entered; outputs the total after the loop with a suitable message.",
    ["One mark each: two labelled terminators START and STOP", "Loop initialisation, incrementation and termination", "Input with a prompt", "Total initialised and totalling of the inputs", "Output with a message", "A fully correct flowchart: arrows, Yes/No labels and correct symbols"],
    "<p>Use the stepper in the Watch tab as a model: set Total and Count first, then the input, the totalling, the increment and the decision with its loop back. Label the Yes and No exits.</p>"),
  ceq(CP("w24_21", "8"), "[11]", "A program checks a password. Requirements: input Password; check that it has at least 10 characters; check that it is not the same as the stored password OldPass; output 'accepted' if both tests pass, otherwise 'rejected'. (a) Complete the flowchart. (b) Write pseudocode to open the file MyPassword.txt, write the accepted password to it and close it. (c) Explain why the accepted password needs to be stored in a file.",
    ["(a) Six marks: correct symbols; working flow lines; input correct; working length check (Length ≥ 10); working comparison (Password <> OldPass); correct output messages", "(b) Three marks: OPENFILE MyPassword.txt FOR WRITE; WRITEFILE MyPassword.txt, Password; CLOSEFILE MyPassword.txt", "(c) Two marks: it needs to be retrieved when required or kept for later; storage must be non-volatile", "The report says most candidates wrote about the use of the password instead of why it is stored"],
    "<p>For (a): INPUT, then a decision for the length, then a decision for the comparison, then two OUTPUT boxes that both go to STOP. For (c) think about the program being switched off.</p>"),
  ceq(CP("w23_21", "8(c)"), "[4]", "A program accepts the length of a ribbon, a number from 1.0 to 5.0 metres inclusive. Give two different sets of test data and state the purpose of each set.",
    ["One mark for each set of test data and one for its purpose, maximum four", "For example, 3.0 is normal data: it should be accepted, to check the program accepts a valid value", "−1 is abnormal data: it should be rejected, to check that an invalid length is refused", "(Other correct sets include extreme or boundary values: 1.0 and 5.0 accepted; 0.9 and 5.1 rejected)"],
    "<p>Each set: the value, the type, whether it is accepted or rejected, and what it proves. Two clear sets earn all four marks.</p>"),
  ceq(CP("w24_22", "8"), "[4]", "A program accepts whole numbers that are not greater than 60. Identify two items of test data that test the limit of 60. Explain the reason for each.",
    ["60: the largest whole number accepted, at the limit (boundary or extreme data that is accepted)", "61: the smallest whole number rejected, just above the limit (boundary or abnormal data that is rejected)", "One mark for each value and one for each reason"],
    "<p>A limit needs a pair: the last accepted value and the first rejected value, and a reason for each. The report says many candidates named types or gave any values.</p>"),
  ceq(CP("w24_22", "6"), "[2]", "Outline one type of verification check that could be used when inputting data.",
    ["One mark for naming the check and one for an expansion, maximum two", "Visual check: looking at the data that has been entered and confirming it is correct or correcting errors", "Or double entry check: the data is entered twice and the two sets are compared by the computer; if they do not match, re-entry is requested"],
    "<p>Choose a verification check, not a validation check, name it and say how it works.</p>"),
  ceq(CP("w24_21", "5"), "[6]", "Describe three methods that are used to design and construct a solution to a problem.",
    ["One mark for each method identified and one for a further description, maximum six", "Structure diagram: a hierarchical diagram showing the breakdown of a program into sub-programs", "Flowchart: a diagram showing the ordered steps to complete a program", "Pseudocode: shows what a program does in plain language"],
    "<p>Name the method, then say what it shows. The report says many candidates named one or two methods but did not describe the use or purpose of each.</p>"),
  ceq(CP("w24_22", "5(b)"), "[3]", "Describe the analysis stage of the program development life cycle.",
    ["Any three from: abstraction, removing irrelevant detail or keeping the key elements of the problem", "Decomposition of the problem, breaking it into inputs, processes and outputs", "Identification of the problem and of the requirements of the solution", "Research into the problem by data collection"],
    "<p>Use the syllabus words: abstraction, decomposition, identification of the problem and requirements. Do not describe design or coding.</p>"),
  ceq(CP("w24_22", "10"), "[6]", "The function LENGTH(X) gives the length of a string X. Write pseudocode to: input a line of text; store it in the text file Notes.txt; calculate the length of the line and output the text in upper case with its length; store the upper-case text in the file Upper.txt. Declare any variables and close both files.",
    ["Maximum six from: declaration of suitable string variables; input of a line of text", "Correct use of UCASE (LCASE in the original) and of LENGTH; opening a required file with the given name", "Storing the line in the first file and the converted line in the second", "Closing both files; correct output"],
    "<p>Declare, input, open, write, close, convert, output, open, write, close. Use OPENFILE … FOR WRITE, WRITEFILE and CLOSEFILE exactly as in the syllabus.</p>"),
  ceq(CP("w23_21", "6(d)"), "[2]", "State two ways in which a programmer can make a program easy to maintain.",
    ["One mark each, maximum two: use of comments", "Use of procedures or functions", "Use of white space"],
    "<p>The syllabus lists meaningful identifiers, comments, procedures and functions as the features of a maintainable program.</p>"),
])

tips = tips_html(
  [("Use the syllabus pseudocode.", "OUTPUT, ←, ENDIF. No program code."),
   ("Initialise before the loop.", "Totals to 0, counters to 0, largest and smallest to the first value."),
   ("Trace every assignment.", "No quotation marks. Stop at the stopping value."),
   ("Check structure, names, operators.", "Then run one small example."),
   ("Label both exits.", "Yes and No, and an arrow on every line."),
   ("Test data needs a pair.", "Last accepted and first rejected."),
   ("Meaningful names.", "Marks, Counter, Total. Not Array.")],
  [("Purpose of an algorithm", "It multiplies the input by every whole number below it."),
   ("Boundary data", "80 is the largest value accepted and 81 is the smallest value rejected."),
   ("Verification", "In a double entry check the data is entered twice and compared, and re-entry is requested if they differ."),
   ("Why store in a file", "A file is non-volatile, so the data can be retrieved later."),
   ("An efficient bubble sort", "A flag stops the loop once no swaps are made, and the inner limit reduces after each pass.")],
  [("State", "A clear statement."), ("Identify", "Name or select the line, error or stage."), ("Describe", "Features or steps, in order."), ("Explain", "Reasons: why and how."), ("Outline", "Name plus how it works."), ("Complete", "Fill the gaps; only what is missing."), ("Write", "Write the pseudocode or program as asked.")]) + FC

js = CHAINJS + PICKJS + '''
/* ---- flowchart builder ---- */
const FCN = [
  { t: "t", l: "START" }, { t: "p", l: "Total ← 0" }, { t: "p", l: "Count ← 1" }, { t: "i", l: "OUTPUT 'Enter a mark (0 to 100)'" }, { t: "i", l: "INPUT Mark" },
  { t: "p", l: "Total ← Total + Mark" }, { t: "p", l: "Count ← Count + 1" }, { t: "d", l: "Count > 30 ?" }, { t: "i", l: "OUTPUT 'The total is ', Total" }, { t: "t", l: "STOP" }
];
(() => { let y = 12; FCN.forEach((n) => { n.h = n.t === "d" ? 56 : 34; n.y = y; n.m = y + n.h / 2; y += n.h + 22; }); })();
const FCH = FCN[FCN.length - 1].y + 50;
function fcDraw(k) {
  let o = ""; const cx = 300;
  FCN.forEach((n, i) => {
    const v = Math.max(0, Math.min(1, k - i)); if (v <= 0) return;
    const w = n.t === "t" ? 140 : n.t === "d" ? 230 : 280, x = cx - w / 2, a = op(0.55 * v);
    if (n.t === "t") o += SV.rect(x, n.y, w, n.h, "f1", { rx: 17, ...a });
    else if (n.t === "p") o += SV.rect(x, n.y, w, n.h, "f2", { rx: 3, ...a });
    else if (n.t === "i") o += SV.poly([[x + 14, n.y], [x + w + 14, n.y], [x + w - 14, n.y + n.h], [x - 14, n.y + n.h]], "f3", a);
    else o += SV.poly([[cx, n.y], [cx + w / 2, n.m], [cx, n.y + n.h], [cx - w / 2, n.m]], "f1", a);
    o += SV.text(cx, n.m + 4, n.l, "lbl", { "text-anchor": "middle", style: "font-size:12.5px;font-family:var(--mono)", ...op(v) });
    if (i > 0) o += SV.line(cx, FCN[i - 1].y + FCN[i - 1].h, cx, n.y - 6, "ax", { "stroke-width": 2, ...op(v) }) + `<g style="opacity:${v}">${SV.arrowHead(cx, n.y, "d", "dot4")}</g>`;
    if (n.t === "d") {
      o += SV.text(cx + 8, n.y + n.h + 14, "Yes", "sm bd", op(v)) + SV.text(cx + w / 2 + 6, n.m - 6, "No", "sm bd", op(v));
      const t = FCN[3], bx = cx + 190, ty = t.m;
      o += SV.line(cx + w / 2, n.m, bx, n.m, "ax", { "stroke-width": 2, ...op(v) }) + SV.line(bx, n.m, bx, ty, "ax", { "stroke-width": 2, ...op(v) }) + SV.line(bx, ty, cx + 148, ty, "ax", { "stroke-width": 2, ...op(v) }) + `<g style="opacity:${v}">${SV.arrowHead(cx + 141, ty, "l", "dot4")}</g>`;
    }
  });
  return o;
}
Lib.stepper($("#stA"), { w: 600, h: FCH, label: "Building a flowchart for a count-controlled totalling loop", base: { k: 0 }, draw: (s) => fcDraw(s.k), tween: 500, dwell: 5000, steps: [
  { cap: "<b>Terminators.</b> The flowchart starts with a rounded box labelled START, and ends with one labelled STOP.", s: { k: 1 } },
  { cap: "<b>Initialise.</b> Set <b>Total</b> to 0 (total initialised) and <b>Count</b> to 1 (loop initialisation) before the loop. An unset total is a common slip.", s: { k: 3 } },
  { cap: "<b>Input with a prompt.</b> The prompt and the INPUT are both input/output boxes (parallelograms).", s: { k: 5 } },
  { cap: "<b>Totalling.</b> A process box adds the new mark to the total.", s: { k: 6 } },
  { cap: "<b>Loop incrementation.</b> A second process box adds 1 to the counter.", s: { k: 7 } },
  { cap: "<b>Loop termination.</b> A decision diamond asks whether the count has passed 30. <b>No</b> loops back to the prompt; <b>Yes</b> leaves the loop. Both exits are labelled.", s: { k: 8 } },
  { cap: "<b>Output with a message, and a fully correct chart.</b> After the loop, output the total with a message, then STOP. Every line has an arrow, every exit a label.", s: { k: 10 } }
] });

chainStep("#stB", "Finding four errors in a range-checking algorithm", ["Structure: REPEAT must end with UNTIL, not WHILE: line 19", "Names: INPUT Temp, but the rest uses Temperature: line 03", "Conditions: IF Temperature = 999 only runs for the stop value: should be <> : line 04", "Operators: >= 35.0 OR <= 38.0 is true for every number: should be AND: line 14"], [
  "<b>Structure first:</b> match every opening keyword with its closing keyword.", "<b>Names:</b> compare each variable with the declarations and the other lines.", "<b>Conditions:</b> test the stopping value with a quick example.", "<b>Operators:</b> a range needs AND. Four errors, each written once, with line number and correction."]);
chainStep("#stC", "Test data for a limit of 80", ["The rule: whole numbers not greater than 80 are accepted", "80: the largest accepted value, at the limit (boundary or extreme data)", "81: the smallest rejected value, just above the limit (boundary or abnormal data)", "Write the value, accepted or rejected, and the reason for each"], [
  "<b>Read the rule</b> and find the limit.", "<b>Accepted end:</b> the limit itself.", "<b>Rejected end:</b> the next value outside it.", "<b>Marks:</b> one for each value and one for each reason."]);

/* ---- trace lab ---- */
function traceLab() {
  const A = (() => { const rows = []; [5, 6, -1].forEach((v) => { rows.push({ ln: 1, v: { Value: v } }); if (v !== -1) { let ans = v; rows[rows.length - 1].v.Answer = ans; rows[rows.length - 1].ln = 4; for (let c = v - 1; c >= 1; c--) { ans *= c; rows.push({ ln: 6, v: { Count: c, Answer: ans } }); } rows[rows.length - 1].v.OUTPUT = ans; rows[rows.length - 1].ln = 8; } }); return rows; })();
  const B = (() => { const rows = []; [34.22, 36.1, 37.4, 38.0, 999].forEach((t) => { rows.push({ ln: 1, v: { OUTPUT: "(Please enter temperature)" } }); const r = { ln: 2, v: { Temperature: t } }; if (t !== 999) r.v.OUTPUT = t > 38.0 ? "Temperature too high" : t < 35.0 ? "Temperature too low" : "Temperature normal"; rows.push(r); }); return rows; })();
  const C = (() => { const rows = [{ ln: 0, v: { Largest: 0 } }]; let big = 0; [7, 3, 9, 4, 8].forEach((n, i) => { const r = { ln: 2, v: { Index: i + 1, Number: n } }; if (n > big) { big = n; r.v.Largest = n; r.ln = 5; } rows.push(r); }); rows.push({ ln: 8, v: { OUTPUT: big } }); return rows; })();
  const T = [
    { label: "Product of descending numbers", cols: ["Value", "Count", "Answer", "OUTPUT"], rows: A, note: "Input 5, 6, −1, 20, 9, 4. After −1 the algorithm stops, so 20, 9 and 4 are never read.",
      code: ["REPEAT", "    INPUT Value", "    IF Value <> -1", "      THEN", "        Answer ← Value", "        FOR Count ← Value - 1 TO 1 STEP -1", "            Answer ← Answer * Count", "        NEXT Count", "        OUTPUT Answer", "    ENDIF", "UNTIL Value = -1"] },
    { label: "Temperature check", cols: ["Temperature", "OUTPUT"], rows: B, note: "Input 34.22, 36.1, 37.4, 38.0, 999, −1. The prompt is recorded as an output; the −1 after 999 is never read.",
      code: ["REPEAT", "    OUTPUT \\"Please enter temperature \\"", "    INPUT Temperature", "    IF Temperature <> 999", "      THEN", "        IF Temperature > 38.0", "          THEN OUTPUT \\"Temperature too high\\"", "        ENDIF", "        IF Temperature < 35.0", "          THEN OUTPUT \\"Temperature too low\\"", "        ENDIF", "        IF Temperature >= 35.0 AND Temperature <= 38.0", "          THEN OUTPUT \\"Temperature normal\\"", "        ENDIF", "    ENDIF", "UNTIL Temperature = 999"] },
    { label: "Largest of five numbers", cols: ["Largest", "Index", "Number", "OUTPUT"], rows: C, note: "Input 7, 3, 9, 4, 8. Largest is initialised to 0 before the loop, which is why the first row is there.",
      code: ["Largest ← 0", "FOR Index ← 1 TO 5", "    INPUT Number", "    IF Number > Largest", "      THEN", "        Largest ← Number", "    ENDIF", "NEXT Index", "OUTPUT Largest"] }
  ];
  const B_ = $("#trB"), O = $("#trO");
  let cur = 0, k = 0;
  const draw = () => {
    const t = T[cur], shown = t.rows.slice(0, k);
    $$(".ln", O).forEach((l) => l.classList.remove("on"));
    if (k > 0) { const l = $(`.ln[data-k="${t.rows[k - 1].ln}"]`, O); l && l.classList.add("on"); }
    $("#trT", O).innerHTML = `<tr>${t.cols.map((c) => `<th>${c}</th>`).join("")}</tr>` + shown.map((r) => `<tr>${t.cols.map((c) => `<td>${r.v[c] === undefined ? "" : r.v[c]}</td>`).join("")}</tr>`).join("");
    $("#trV", O).textContent = k === 0 ? "Press Next row. " + t.note : k >= t.rows.length ? "Finished: " + t.rows.length + " rows. " + t.note : "Row " + k + " of " + t.rows.length + ".";
  };
  const build = () => {
    const t = T[cur];
    O.innerHTML = `<div class="grid2"><div class="code"><pre class="cp">${t.code.map((l, i) => `<span class="ln" data-k="${i}">${esc(l)}</span>`).join("")}</pre></div><div><div class="tw"><table class="t mx" id="trT"></table></div><div class="row"><button class="b" data-a="back">◀ Back</button> <button class="b pri" data-a="next">Next row ▶</button> <button class="b" data-a="reset">↻ Reset</button></div><div class="verdict" id="trV"></div></div></div>`;
    $("[data-a=next]", O).onclick = () => { k = Math.min(T[cur].rows.length, k + 1); draw(); };
    $("[data-a=back]", O).onclick = () => { k = Math.max(0, k - 1); draw(); };
    $("[data-a=reset]", O).onclick = () => { k = 0; draw(); };
    draw();
  };
  B_.innerHTML = T.map((t, i) => `<button class="b${i ? "" : " pri"}" data-i="${i}">${t.label}</button>`).join("");
  $$("button", B_).forEach((b) => (b.onclick = () => { cur = +b.dataset.i; k = 0; $$("button", B_).forEach((x) => x.classList.toggle("pri", x === b)); build(); }));
  build();
}
traceLab();

pick("td", [
  { label: "Whole number 1 to 80", rows: [["40", "Normal", "Accepted", "A typical valid value"], ["1", "Extreme / boundary", "Accepted", "The smallest accepted value"], ["80", "Extreme / boundary", "Accepted", "The largest accepted value, at the limit"], ["0", "Boundary / abnormal", "Rejected", "The first value below the range"], ["81", "Boundary / abnormal", "Rejected", "The first value above the range"], ["\\"ten\\"", "Abnormal", "Rejected", "The wrong data type"]] },
  { label: "Password 8 to 20 characters", rows: [["12 characters", "Normal", "Accepted", "A typical valid length"], ["8 characters", "Extreme / boundary", "Accepted", "The shortest accepted"], ["20 characters", "Extreme / boundary", "Accepted", "The longest accepted"], ["7 characters", "Boundary / abnormal", "Rejected", "The first length that is too short"], ["21 characters", "Boundary / abnormal", "Rejected", "The first length that is too long"], ["no characters", "Abnormal", "Rejected", "Presence check: nothing entered"]] },
  { label: "Temperature 35.0 to 38.0", rows: [["36.5", "Normal", "Accepted", "A typical valid value"], ["35.0", "Extreme / boundary", "Accepted", "The lowest accepted"], ["38.0", "Extreme / boundary", "Accepted", "The highest accepted"], ["34.9", "Boundary / abnormal", "Rejected", "The first value below"], ["38.1", "Boundary / abnormal", "Rejected", "The first value above"], ["\\"hot\\"", "Abnormal", "Rejected", "The wrong data type"]] },
  { label: "Ribbon 1.0 to 5.0 m", rows: [["3.0", "Normal", "Accepted", "Valid length"], ["1.0", "Extreme / boundary", "Accepted", "The shortest accepted"], ["5.0", "Extreme / boundary", "Accepted", "The longest accepted"], ["0.9", "Boundary / abnormal", "Rejected", "Just below"], ["5.1", "Boundary / abnormal", "Rejected", "Just above"], ["−1", "Abnormal", "Rejected", "A negative length cannot exist"]] }
], (it) => `<div class="tw"><table class="t"><tr><th>Value</th><th>Type</th><th>Result</th><th>Reason</th></tr>${it.rows.map((r) => `<tr><td><b>${r[0]}</b></td><td>${r[1]}</td><td>${r[2]}</td><td>${r[3]}</td></tr>`).join("")}</table></div><p>For a limit, a pair of values (the last accepted and the first rejected) is boundary data. Each answer needs the value, whether it is accepted or rejected, and the reason.</p>`);

pick("fx", [
  { label: "x is greater than y", bad: "IF x is greater than y", good: "IF X > Y", why: "The syllabus says precision is required: the symbol must be used." },
  { label: "= to assign", bad: "Total = Total + 1", good: "Total ← Total + 1", why: "= tests equality; ← assigns a value." },
  { label: "PRINT", bad: "PRINT Total", good: "OUTPUT Total", why: "A pseudocode question uses the syllabus keyword OUTPUT." },
  { label: "WHILE after REPEAT", bad: "REPEAT … WHILE Mark = 99", good: "REPEAT … UNTIL Mark = 99", why: "REPEAT ends with UNTIL. WHILE starts a pre-condition loop." },
  { label: "ENDCASE for IF", bad: "IF A > B … ENDCASE", good: "IF A > B … ENDIF", why: "IF closes with ENDIF; ENDCASE closes CASE." },
  { label: "Range with OR", bad: "IF Mark >= 0 OR Mark <= 20", good: "IF Mark >= 0 AND Mark <= 20", why: "Every number is either at least 0 or at most 20, so OR accepts everything." },
  { label: "Array called Array", bad: "Array[Index] ← 5", good: "Marks[Index] ← 5", why: "The report says Array is not a meaningful identifier." },
  { label: "Loop counter as STRING", bad: "DECLARE Counter : STRING", good: "DECLARE Counter : INTEGER", why: "A FOR loop counter must be an INTEGER." },
  { label: "Swap uses wrong index", bad: "ItemList[Counter] ← Temp", good: "ItemList[Counter + 1] ← Temp", why: "The second half of a swap writes to the next element, or the first value is overwritten." }
], (it) => `<div class="grid2"><div><small>Faulty</small><p><code>${it.bad}</code></p></div><div><small>Corrected</small><p><code>${it.good}</code></p></div></div><div class="verdict">${it.why}</div>`);

pick("vv", [
  { label: "Visual check", k: "Verification", d: "The user looks at what was entered and confirms it is correct, or corrects it.", s: "A visual check means looking at the data entered to confirm it is correct or to find errors." },
  { label: "Double entry check", k: "Verification", d: "The data is entered twice and the computer compares the two copies.", s: "In a double entry check the data is entered twice and compared; if they do not match, an error has been made and re-entry is requested." },
  { label: "Range check", k: "Validation", d: "Checks that a value lies between a lowest and highest value.", s: "A range check tests that the number is between the lowest and highest acceptable values." },
  { label: "Length check", k: "Validation", d: "Checks the number of characters is allowed.", s: "A length check tests that the data has an acceptable number of characters." },
  { label: "Type check", k: "Validation", d: "Checks the data is of the right data type, such as a whole number.", s: "A type check tests that the data is the right type, for example that it is a whole number." },
  { label: "Presence check", k: "Validation", d: "Checks that something has been entered.", s: "A presence check tests that data has been entered and the field has not been left empty." },
  { label: "Format check", k: "Validation", d: "Checks the data follows a set pattern.", s: "A format check tests that the data matches a pattern, such as two letters followed by four digits." },
  { label: "Check digit", k: "Validation", d: "A digit calculated from the other digits and checked after input.", s: "A check digit is calculated from the other digits and recalculated after input; if the two differ, an error has occurred." }
], (it) => `<p><b>${it.k}</b></p><p>${it.d}</p><div class="verdict">${it.s}</div>`);
''' + CLASSIFY("cl1", "Is each check validation or verification?", ["Validation", "Verification"],
  [("Range check", 0), ("Double entry check", 1), ("Length check", 0), ("Visual check", 1), ("Presence check", 0), ("Type check", 0), ("Format check", 0), ("Check digit", 0)],
  "Verification is the visual check and the double entry check. The other checks in the syllabus are validation.") + CLASSIFY("cl2", "Which flowchart symbol does each step use?", ["Terminator", "Process", "Input or output", "Decision"],
  [("START", 0), ("STOP", 0), ("Total ← Total + Number", 1), ("Count ← Count + 1", 1), ("INPUT Password", 2), ("OUTPUT 'Accepted'", 2), ("Is Length >= 8 ?", 3), ("Is Count > 50 ?", 3)],
  "A terminator marks the start and end; a process assigns or calculates; input/output covers prompts and messages; a decision has two exits.") + ORDER(
  "Put the steps for completing a trace table in order.",
  ["Write a column for each variable and one for the output", "Take the first input and write it in its column", "Follow the lines in order and write each new value in a row", "Write any output without quotation marks", "Stop when the stopping condition is met"],
  "Headings, first input, follow the lines, outputs, stop.") + MATCH([
  ["Normal data", "Data that should be accepted"], ["Abnormal data", "Data that should be rejected"], ["Extreme data", "The largest or smallest acceptable value"], ["Boundary data", "The largest or smallest accepted value and the matching rejected value"]]) + CALC([
  {"q": "Paper 2 has 75 marks in 105 minutes. The final question is 15 marks and should take 30 minutes. How many minutes a mark for the other 60 marks?", "a": 1.25, "unit": "min", "tol": 0.01, "hint": "(105 − 30) ÷ 60.", "sol": "<b>1.25 minutes</b>."},
  {"q": "Trace: Total ← 0, then FOR Index ← 1 TO 4 with Total ← Total + Index. What is Total at the end?", "a": 10, "unit": "", "tol": 0.01, "hint": "1 + 2 + 3 + 4.", "sol": "<b>10</b>."},
  {"q": "A FOR loop runs FOR Count ← 3 TO 1 STEP -1 with Answer starting at 3 and Answer ← Answer * Count. What is Answer at the end?", "a": 18, "unit": "", "tol": 0.01, "hint": "3 × 3 × 2 × 1.", "sol": "<b>18</b>."},
  {"q": "A limit is 'whole numbers not greater than 60'. What is the smallest rejected value?", "a": 61, "unit": "", "tol": 0.01, "hint": "One above the limit.", "sol": "<b>61</b>."},
  {"q": "A flowchart scores one mark each for: terminators, loop set-up, input with prompt, total, output with message and a fully correct chart. How many marks if everything is correct except the arrows and labels?", "a": 5, "unit": "", "tol": 0.01, "hint": "The last point is the correct chart overall.", "sol": "<b>5</b> of 6 (the final mark needs correct arrows and labels)."}]) + MCQ([
  ("A question asks for pseudocode. Which answer can earn marks?", ["Python code using print", "OUTPUT with ← for assignment", "A paragraph of English", "A flowchart"], 1, "Use the syllabus pseudocode."),
  ("In a trace table, what should you do when the stopping value is processed?", ["Carry on with the next input", "Make no further entries", "Cross out the table", "Write the stopping value twice"], 1, "Once the stopping condition has been met, no further entries should be made."),
  ("Which pair is boundary data for a limit of 80?", ["80 and 40", "80 and 81", "0 and 1", "79 and 78"], 1, "The last accepted value and the first rejected value."),
  ("Which check is verification?", ["Range check", "Presence check", "Double entry check", "Format check"], 2, "Visual and double entry checks are verification."),
  ("Why do flowchart flow lines need arrowheads?", ["To look neat", "They show the direction of control", "They are decisions", "They are terminators"], 1, "Lines without arrows lose a mark.")
], "qz1") + CARDS([
  ("Pseudocode", "OUTPUT, ←, ENDIF. No program code."), ("Initialise", "Total ← 0 before the loop."), ("Trace table", "Every assignment; no quotes; stop at stop."), ("Errors", "Structure, names, operators; line and correction."),
  ("Flowchart", "Terminator, process, input/output, decision; arrows."), ("Boundary data", "Last accepted and first rejected."), ("Verification", "Visual and double entry."), ("Bubble sort", "Flag, and a shrinking inner limit.")])

build("cx3", "ig-cs-paper2-algorithms-technique", "Paper 2 Algorithms and Programming: Technique and Practice", EYC,
  "How Paper 2 is built, the syllabus pseudocode, the standard methods, trace tables, finding errors, flowcharts, test data and short written answers, with fourteen real questions and what each mark was for.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
