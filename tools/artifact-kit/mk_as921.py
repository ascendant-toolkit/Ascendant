"""AS CS 9.2.1: algorithms, identifier tables, flowcharts and pseudocode constructs. Run: python3 tools/artifact-kit/mk_as921.py"""
from ak9 import *

# ---- flowcharts (drawn to match the mark schemes)
F_SUM = flow({
  "S": ("term", "START", 240, 18), "I": ("proc", "Set PosSum, PosCount,\nNegSum, NegCount to 0", 240, 68, (190, 40)),
  "N": ("io", "INPUT Number", 240, 125), "D1": ("dec", "Number = 0 ?", 240, 190), "O": ("io", "OUTPUT PosSum, PosCount\nNegSum, NegCount", 78, 190, (156, 44)), "E": ("term", "END", 78, 255),
  "D2": ("dec", "Number > 0 ?", 240, 265), "P": ("proc", "PosSum ← PosSum + Number\nPosCount ← PosCount + 1", 430, 265, (170, 40)), "M": ("proc", "NegSum ← NegSum + Number\nNegCount ← NegCount + 1", 240, 335, (170, 40))},
  [("S", "b", "I", "t", [], None, None), ("I", "b", "N", "t", [], None, None), ("N", "b", "D1", "t", [], None, None),
   ("D1", "l", "O", "r", [], "YES", (174, 172)), ("O", "b", "E", "t", [], None, None), ("D1", "b", "D2", "t", [], "NO", (250, 231)),
   ("D2", "r", "P", "l", [], "YES", (322, 253)), ("D2", "b", "M", "t", [], "NO", (250, 306)),
   ("P", "t", "N", "r", [(430, 125)], None, None), ("M", "r", "N", "r", [(350, 335), (350, 125)], None, None)], w=540, h=365, cap="sum and count positive and negative values")
F_PRIME = flow({
  "S": ("term", "START", 240, 18), "I": ("proc", "Count ← 0", 240, 68), "N": ("io", "INPUT Num", 240, 120), "D1": ("dec", "Num < 0 ?", 240, 185),
  "O": ("io", "OUTPUT \"Primes: \", Count", 78, 185, (150, 40)), "E": ("term", "END", 78, 250), "D2": ("dec", "IsPrime(Num)\nreturns TRUE ?", 240, 260, (160, 66)), "P": ("proc", "Count ← Count + 1", 430, 260, (140, 36))},
  [("S", "b", "I", "t", [], None, None), ("I", "b", "N", "t", [], None, None), ("N", "b", "D1", "t", [], None, None),
   ("D1", "l", "O", "r", [], "YES", (174, 172)), ("O", "b", "E", "t", [], None, None), ("D1", "b", "D2", "t", [], "NO", (250, 227)),
   ("D2", "r", "P", "l", [], "YES", (326, 248)), ("P", "t", "N", "r", [(430, 120)], None, None), ("D2", "b", "N", "r", [(240, 320), (350, 320), (350, 120)], "NO", (250, 309))], w=540, h=340, cap="count the prime numbers")
F_GIVEN = flow({
  "S": ("term", "START", 160, 16), "A": ("io", "INPUT UserID", 160, 62), "B": ("proc", "Set Average to\nGetAverage(UserID)", 160, 112, (150, 40)), "C": ("proc", "Set Total to 0", 160, 160, (150, 32)), "D": ("proc", "Set Index to 4", 160, 205, (150, 32)),
  "L": ("dec", "Is Index < 7 ?", 160, 272, (150, 62)), "G": ("proc", "Set Last to\nSameMonth[Index]", 400, 272, (140, 40)), "H": ("dec", "Is Average\n> Last ?", 400, 345, (140, 64)),
  "P1": ("proc", "Add Average\nto Total", 545, 345, (88, 40)), "P2": ("proc", "Add Last to Total", 400, 415, (130, 32)), "I": ("proc", "Add 1 to Index", 400, 465, (130, 32)),
  "U": ("call", "Update(UserID, Total)", 160, 350, (160, 36)), "E": ("term", "END", 160, 410)},
  [("S", "b", "A", "t", [], None, None), ("A", "b", "B", "t", [], None, None), ("B", "b", "C", "t", [], None, None), ("C", "b", "D", "t", [], None, None), ("D", "b", "L", "t", [], None, None),
   ("L", "r", "G", "l", [], "YES", (240, 264)), ("L", "b", "U", "t", [], "NO", (166, 316)), ("U", "b", "E", "t", [], None, None), ("G", "b", "H", "t", [], None, None),
   ("H", "r", "P1", "l", [], "YES", (482, 338)), ("H", "b", "P2", "t", [], "NO", (406, 388)), ("P1", "b", "I", "r", [(545, 465)], None, None), ("P2", "b", "I", "t", [], None, None), ("I", "l", "L", "l", [(60, 465), (60, 272)], None, None)], w=600, h=495, cap="flowchart from O/N 2022")

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>An <b>algorithm</b> is a sequence of steps that describes how to solve a problem. During <b>design</b> it can be written as <b>numbered steps in words</b>, drawn as a <b>program flowchart</b>, or written in <b>pseudocode</b>; a table called an <b>identifier table</b> lists every variable with a meaningful name, its data type, an explanation (purpose) and an example value. Every algorithm is built from three constructs: <b>assignment</b> (store a value in a variable), <b>selection</b> (choose with IF or CASE) and <b>iteration</b> (repeat with FOR, WHILE or REPEAT). A flowchart uses a <b>terminator</b> (START and END), a <b>parallelogram</b> for input and output, a <b>rectangle</b> for a process (assignment), a <b>diamond</b> for a decision with YES and NO exits, and a <b>rectangle with double sides</b> for a call to a subroutine; arrows show the flow. Exam questions ask you to complete an identifier table, tick the constructs in some pseudocode, draw a flowchart from a description, or turn a flowchart into pseudocode.</p></div>

  <h2>1 · Identifier tables</h2>
  <p>An identifier table is produced in the <b>design</b> stage and documents the variables to simplify program maintenance.</p>
  <div class="tw"><table class="t">
    <tr><th>Example value</th><th>Explanation</th><th>Variable name</th><th>Data type</th></tr>
    <tr><td class="mono">"Wong"</td><td>The preferred name of the member joining the football club</td><td class="mono">MemberName</td><td class="mono">STRING</td></tr>
    <tr><td class="mono">FALSE</td><td>Whether an existing member lives at the same address</td><td class="mono">FamilyMember</td><td class="mono">BOOLEAN</td></tr>
    <tr><td class="mono">19/02/1983</td><td>When the member joined the club</td><td class="mono">StartDate</td><td class="mono">DATE</td></tr>
    <tr><td class="mono">1345</td><td>The points a member has earned</td><td class="mono">Points</td><td class="mono">INTEGER</td></tr>
  </table></div>
  <p>Choose a <b>meaningful name</b> (a name such as <span class="mono">Temp</span> or <span class="mono">X</span> does not say what the variable is used for, which is not good practice) and a data type from the example value: text in quotes STRING, a single character in single quotes CHAR, whole numbers INTEGER, numbers with a decimal point REAL, TRUE or FALSE BOOLEAN, a date DATE. An identifier table also holds the <b>purpose</b>, an <b>example value</b>, the <b>number of elements</b> of an array or length of a string, the <b>value of constants</b> and the <b>scope</b> (local or global).</p>

  <h2>2 · The three constructs</h2>
  <div class="tw"><table class="t">
    <tr><th>Construct</th><th>Pseudocode</th></tr>
    <tr><td><b>Assignment</b></td><td class="mono">Total ← Total + Number</td></tr>
    <tr><td><b>Selection</b></td><td class="mono">IF Mark &gt; 74 THEN ... ELSE ... ENDIF; CASE OF Option ... OTHERWISE ... ENDCASE</td></tr>
    <tr><td><b>Iteration</b> (repetition)</td><td class="mono">FOR Index ← 1 TO 10 ... NEXT Index; WHILE condition DO ... ENDWHILE (test first); REPEAT ... UNTIL condition (test last)</td></tr>
    <tr><td>Subroutine</td><td class="mono">CALL Reset(Count); Result ← CalculateTotal(); FUNCTION and PROCEDURE definitions</td></tr>
    <tr><td>Input/output</td><td class="mono">INPUT Name; OUTPUT Total; READFILE; WRITEFILE</td></tr>
  </table></div>
  <p>One line can contain more than one construct: <span class="mono">REPEAT INPUT Value UNTIL Sales[4] &gt; Value</span> is both iteration and input; an <span class="mono">IF</span> with an assignment inside is selection and assignment; a <span class="mono">FOR</span> whose body calls a procedure is iteration and a subroutine call.</p>

  <h2>3 · Program flowcharts</h2>
  <p>Draw START, then the steps in order. A decision has two exits labelled YES and NO. A loop is drawn by an arrow that returns to an earlier box. A call to a function is shown as a call box or inside a decision. Variable declarations are not required. Example: <i>input integers until zero is entered; sum and count the positive values and the negative values; output the two sums and two counts.</i></p>
  ''' + flow_html({}, [], w=1, h=1) + F_SUM + '''
  <p>The same idea for "input integers until a negative value; count how many times IsPrime() returns TRUE":</p>
  ''' + F_PRIME + '''
  <p>Marks go for: initialising the counters before the loop; the input inside the loop; the loop test and exit; the correct calculations; and the output after the loop.</p>

  <h2>4 · Reading a flowchart as pseudocode</h2>
  <p>Work from START. Each decision with a loop-back becomes a <b>WHILE</b> (test first) or REPEAT loop; a decision with two forward paths becomes IF ... ELSE ... ENDIF; the call box becomes <b>CALL</b>.</p>

  <h2>Common ways to lose marks</h2>
  <ul>
    <li>Writing a variable called <span class="mono">X</span> or <span class="mono">Temp</span> in an identifier table: the name must say what it holds.</li>
    <li>Using INTEGER for a decimal value or STRING for a date.</li>
    <li>Initialising a counter inside the loop (it resets every time).</li>
    <li>Using a diamond for an assignment or a rectangle for a decision.</li>
    <li>Forgetting the YES and NO labels on a decision, or leaving a decision with only one exit.</li>
  </ul>
'''.replace(flow_html({}, [], w=1, h=1), "")

watch = '''
  <h2>1 · Building a flowchart</h2>
  <div id="stA"></div>
  <h2>2 · Tracing a flowchart loop</h2>
  <div id="stB"></div>
  <h2>3 · Which construct?</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Run the sum and count algorithm</h2>
  <p>Enter integers one at a time; 0 ends the input.</p>
  <div class="card"><div class="btnrow"><button id="fl_p5">+5</button><button id="fl_p2">+2</button><button id="fl_m3">−3</button><button id="fl_m7">−7</button><button id="fl_0">0 (end)</button><button id="fl_r">Reset</button></div><div id="flV" class="verdict"></div></div>
  <h2>Lab 2 · Assignment, selection or iteration?</h2>
  <div class="card"><div id="cB" class="btnrow"></div><div id="cO"></div></div>
  <h2>Lab 3 · Flowchart symbols</h2>
  <div class="card"><div id="sB" class="btnrow"></div><div id="sO"></div></div>
'''

_pr, _prjs = PR(["Which construct?", "Which flowchart symbol?", "Match the term to its meaning", "Put the algorithm steps in order", "Working out", "Multiple choice"],
  ("Which construct does the pseudocode use?", ["Assignment", "Selection", "Iteration"], [("Total ← Total + 1", 0), ("IF Mark > 74 THEN", 1), ("FOR Index ← 1 TO 10", 2), ("CASE OF Option", 1), ("WHILE IsClosed", 2), ("Discount ← TRUE", 0)], "Store, choose, repeat."),
  ("Which flowchart symbol is used?", ["Terminator", "Parallelogram", "Rectangle", "Diamond"], [("START", 0), ("INPUT Number", 1), ("Count ← Count + 1", 2), ("Number = 0 ?", 3), ("END", 0), ("OUTPUT Total", 1)], "Input/output: parallelogram. Decision: diamond."),
  [["Algorithm", "A sequence of steps that solves a problem"], ["Identifier table", "Variables with name, type, purpose and example"], ["Assignment", "Storing a value in a variable"], ["Selection", "Choosing which statements to run"], ["Iteration", "Repeating statements"]],
  ("Put the algorithm for 'sum the numbers until 0' in order.", ["Set Total to 0", "Input a number", "If it is 0, stop and output Total", "Add the number to Total", "Go back and input the next number"], "Initialise, input, test, add, repeat."),
  [{"q": "The algorithm sums inputs 5, 2, −3, −7, 0. What is the sum of the positive values?", "a": 7, "unit": "", "tol": 0.01, "hint": "5 + 2.", "sol": "<b>7</b>."}, {"q": "For the same inputs what is the count of negative values?", "a": 2, "unit": "", "tol": 0.01, "hint": "−3 and −7.", "sol": "<b>2</b>."}, {"q": "The loop in the algorithm runs once for each non-zero input. How many times for 5, 2, −3, −7, 0?", "a": 4, "unit": "", "tol": 0.01, "hint": "The 0 ends it.", "sol": "<b>4</b> (the 0 is input but not processed)."}, {"q": "A FOR loop is FOR Index ← 4 TO 6. How many times does the body run?", "a": 3, "unit": "", "tol": 0.01, "hint": "4, 5, 6.", "sol": "<b>3</b>."}, {"q": "A flowchart has 2 diamonds and each has YES and NO exits. How many labelled exits?", "a": 4, "unit": "", "tol": 0.01, "hint": "2 × 2.", "sol": "<b>4</b>."}],
  [("A decision is drawn as a:", ["Diamond", "Rectangle", "Oval", "Parallelogram"], 0, "Diamond."), ("A WHILE loop tests:", ["Before the body", "After the body", "Never", "Once"], 0, "First."), ("A REPEAT loop tests:", ["After the body", "Before the body", "Never", "Twice"], 0, "Last."), ("An identifier table has:", ["Variable names and data types", "Only passwords", "Only loops", "Files"], 0, "Names and types."), ("INPUT is drawn as a:", ["Parallelogram", "Diamond", "Oval", "Triangle"], 0, "Parallelogram."), ("A good variable name:", ["Says what it holds", "Is a single letter", "Is Temp", "Is X"], 0, "Meaningful.")],
  [("Algorithm", "Steps that solve a problem."), ("Identifier table", "Name, type, purpose, example."), ("Terminator", "START and END."), ("Parallelogram", "Input and output."), ("Rectangle", "Process (assignment)."), ("Diamond", "Decision: YES and NO."), ("WHILE", "Test first."), ("REPEAT ... UNTIL", "Test last.")])

real = RWNOTE + (
rw("A recipe", "Numbered steps in order, with choices ('if the sauce is thin...') and repeats ('stir until thick'): an algorithm with selection and iteration.", "algorithm.") +
rw("A phone's unlock logic", "Input the code, if it matches unlock, otherwise add one to the wrong-attempt count and ask again: assignment, selection and iteration.", "constructs.") +
rw("Planning before coding", "Programmers draw a flowchart for the tricky part of a program first, so the team agrees on the logic before writing it.", "flowcharts in design.") +
rw("Naming variables", "A team reading `Total` knows what it means; `T1` forces them to look it up. That is why identifier tables ask for meaningful names.", "identifier table.") +
rw("A self-service checkout", "Scan item, add price to total, repeat until Finished is pressed, then take payment: a loop with an exit test.", "iteration.")
)

where = [
  ("M/J 2021", "21, 23", "1(a)", "4", "Complete an identifier table for a football club program"),
  ("O/N 2021", "22", "2(a)", "5", "Draw a program flowchart for an algorithm that sums and counts positive and negative values"),
  ("M/J 2022", "21", "1(a), (b)", "1 + 4 + 2", "The term for a sequence of steps; data types for variables; a poor variable name"),
  ("M/J 2022", "22", "2", "4", "Draw a flowchart for an algorithm that counts the primes"),
  ("M/J 2022", "22", "1(b), (c)", "4 + 2", "Life cycle stage of four activities; what an identifier table contains"),
  ("M/J 2022", "23", "1(a)", "5", "Tick selection, iteration and assignment for pseudocode lines"),
  ("O/N 2022", "22", "4", "6 + 1", "Write the pseudocode for a flowchart; name the iterative construct"),
  ("O/N 2023", "22", "1(a)", "4", "Complete an identifier table for a car accessories shop"),
  ("M/J 2024", "22", "1(a), (c)", "4 + 2", "Tick selection, iteration and input/output; document the variables"),
  ("O/N 2024", "23", "1(a), (b)", "4 + 3", "Tick selection, iteration and subroutine; data types"),
  ("M/J 2025", "21", "1(a), (b)", "4 + 5", "Complete an identifier table; tick assignment, selection and iteration"),
  ("O/N 2025", "22", "1(a), (b)", "4 + 3", "Tick selection, iteration and subroutines; data types")]

past = '''  <p class="note">Question 1 of Paper 2 is nearly always an identifier table or a "tick the construct" table, followed by questions on data types and expressions (the expressions are on the page for programming basics). The flowchart questions have appeared in 2021 and 2022 with the same mark points (initialise before the loop, input in the loop, test and exit, output after). Paper 2 questions are reworded from the papers; check the original paper and mark scheme for the exact wording.</p>
''' + peq(SRC("s21", "21/23", "Q1(a)"), "4 marks", "Complete",
  "A program is being developed to help manage the membership of a football club. Complete the identifier table: example value \"Wong\" (the preferred name of the member joining); FALSE (whether an existing member lives at the same address); 19/02/1983 (when the member joined the club); 1345 (the points a member has earned). Give a variable name and data type for each.", "Meaningful names; STRING, BOOLEAN, DATE, INTEGER.",
  "<p>One mark for each appropriate variable name with its data type: " + mks(["\"Wong\": MemberName, STRING", "FALSE: FamilyMember, BOOLEAN", "19/02/1983: StartDate, DATE", "1345: Points, INTEGER"]) + "</p>", "A name such as X or Value. It must say what the variable is for.") + peq(SRC("w21", "22", "Q2(a)"), "5 marks", "Draw",
  "An algorithm will: 1. input an integer value; 2. jump to step 6 if the value is zero; 3. sum and count the positive values; 4. sum and count the negative values; 5. repeat from step 1; 6. output the two sum values and the two count values. Draw a program flowchart to represent the algorithm. (Variable declarations are not required.)", "Initialise four totals; input; zero test; positive test; update; loop back; output.",
  "<p>One mark for each outlined group: " + mks(["START, and the initialisation of the four variables to zero before the loop", "INPUT of the value", "The decision on zero, exiting to the output", "The decision on positive, with the sum and count for positive values", "The sum and count for negative values, with both paths looping back to the input"]) + " (max 4 for a non-working solution)</p>" + F_SUM, "Initialising the totals inside the loop, so they restart on every input.") + peq(SRC("s22", "21", "Q1(a)(b)"), "1 + 4 + 2 marks", "Give / Complete",
  "(a) Give the technical term for a sequence of steps that describe how to solve a problem. (b)(i) Write the most appropriate data type for: Temp (the average temperature), PetName (my pet's name), MyDOB (to calculate the days until my next birthday), LightOn (the light is only on or off). (ii) Identify the variable name that is not good practice and give a reason.", "Algorithm; REAL, STRING, DATE, BOOLEAN; Temp does not say what it holds.",
  "<p><b>(a)</b> " + mks(["An algorithm"]) + "</p><p><b>(b)(i)</b> " + mks(["Temp: REAL", "PetName: STRING", "MyDOB: DATE", "LightOn: BOOLEAN"], "a") + "</p><p><b>(ii)</b> " + mks(["Variable: Temp", "Reason: the name does not indicate what the variable is used for"], "b") + "</p>", None) + peq(SRC("s22", "22", "Q2"), "4 marks", "Draw",
  "An algorithm is described as follows: 1. Input an integer value. 2. Jump to step 6 if the value is less than zero. 3. Call the function IsPrime() using the integer value as a parameter. 4. Keep a count of the number of times IsPrime() returns TRUE. 5. Repeat from step 1. 6. Output the value of the count with a suitable message. Draw a program flowchart.", "Count before the loop; input in the loop; test; call the function; update.",
  "<p>One mark per point: " + mks(["Initialise Count before the loop and input the number in a loop", "Loop until the number is less than zero, with an output including Count and a message", "Use of IsPrime(Num) as a function (it returns a value)", "Check the return value and increment Count if appropriate"]) + "</p>" + F_PRIME, None) + peq(SRC("s22", "22", "Q1(b)(c)"), "4 + 2 marks", "Complete / State",
  "(b) Complete the table by writing the life cycle stage for each activity: an identifier table is produced; syntax errors can occur; the developer discusses the program requirements with the customer; a trace table is produced. (c) An identifier table includes the names of identifiers used. State two other pieces of information the table should contain.", "Design, coding, analysis, testing. Purpose, type, example, scope.",
  "<p><b>(b)</b> " + mks(["Identifier table: Design", "Syntax errors can occur: Coding", "Discussing the requirements: Analysis", "Trace table: Testing"]) + "</p><p><b>(c)</b> Any two: " + mks(["A description of what the identifier is used for", "The data type of the identifier", "The number of elements of an array, or the length of a string", "An example data value", "The value of any constants used", "The scope of the variable (local or global)"], "a") + "</p>", None) + peq(SRC("s22", "23", "Q1(a)"), "5 marks", "Tick",
  "Tick selection, iteration and assignment (one or more) for each: FOR Index ← 1 TO 3 with Safe[Index] ← GetResult() inside and NEXT Index; OTHERWISE : OUTPUT \"ERROR 1202\"; REPEAT UNTIL Index = 27; INPUT MyName; IF Mark > 74 THEN Grade ← 'A' ENDIF.", "A FOR with an assignment inside is iteration and assignment.",
  "<p>One mark per row: " + mks(["The FOR loop with the assignment: iteration and assignment", "OTHERWISE : OUTPUT: selection (part of a CASE)", "REPEAT UNTIL Index = 27: iteration", "INPUT MyName: none of the three (input only)", "IF Mark > 74 with Grade ← 'A': selection and assignment"]) + "</p>", None) + peq(SRC("w22", "22", "Q4"), "6 + 1 marks", "Write / Give",
  "The flowchart shown: START; INPUT UserID; Set Average to GetAverage(UserID); Set Total to 0; Set Index to 4; Is Index < 7? (YES: Set Last to SameMonth[Index]; Is Average > Last? YES: Add Average to Total; NO: Add Last to Total; Add 1 to Index; back to the test; NO: Update(UserID, Total); END). (a) Write the equivalent pseudocode. (b) Give the name of the iterative construct in the flowchart.", "A WHILE loop with an IF ... ELSE inside; CALL Update after.",
  "<p>" + F_GIVEN + "<p><b>(a)</b> " + mks(["Input UserID and use GetAverage() with assignment", "Total initialised to zero and Index to 4", "A conditional loop with Index from 4 to 6", "Last assigned from SameMonth[Index] in the loop", "IF ... THEN ... ELSE ... ENDIF in the loop", "Correct assignments and the final call to Update() after the loop"]) + "</p>" + code('''INPUT UserID
Average ← GetAverage(UserID)
Total ← 0
Index ← 4

WHILE Index < 7
   Last ← SameMonth[Index]
   IF Average > Last THEN
      Total ← Total + Average
   ELSE
      Total ← Total + Last
   ENDIF
   Index ← Index + 1
ENDWHILE

CALL Update(UserID, Total)'''.split("\n")) + "<p><b>(b)</b> " + mks(["A WHILE loop (a conditional, pre-condition loop)"], "a") + "</p>", "Using a FOR loop without the correct limits, or putting the call to Update() inside the loop.") + peq(SRC("w23", "22", "Q1(a)"), "4 marks", "Complete",
  "An order for car accessories stores: \"Mr Khan\" (the name of the customer); 3 (the number of items in the order); TRUE (whether this is a new customer); 15.75 (the deposit paid). Complete the identifier table with meaningful variable names and appropriate data types.", "STRING, INTEGER, BOOLEAN, REAL.",
  "<p>" + mks(["CustomerName: STRING", "NumItems: INTEGER", "NewCustomer: BOOLEAN", "Deposit: REAL"]) + "</p>", None) + peq(SRC("s24", "22", "Q1(a)(c)"), "4 + 2 marks", "Tick / State",
  "(a) Tick selection, iteration and input/output for: FOR Index ← 1 TO 10, Data[Index] ← 0, NEXT Index; WRITEFILE ThisFile, \"****\"; UNTIL Level > 25; IF Mark > 74 THEN READFILE OldFile, Data ENDIF. (c) The variables are documented during design to simplify maintenance. State a suitable way of documenting them and one piece of information to record, other than the data type.", "FOR: iteration. WRITEFILE: input/output. UNTIL: iteration. IF with READFILE: selection and input/output. Identifier table.",
  "<p><b>(a)</b> " + mks(["FOR with the assignment: iteration", "WRITEFILE: input/output", "UNTIL: iteration", "IF with READFILE: selection and input/output"]) + "</p><p><b>(c)</b> " + mks(["An identifier table", "One of: an explanation or purpose of each variable; an example of the data values stored; the initialisation value"], "a") + "</p>", None) + peq(SRC("w24", "23", "Q1(a)(b)"), "4 + 3 marks", "Tick / Complete",
  "(a) Tick selection, iteration and subroutine for: FOR Index ← 1 TO 3 with IF Safe[Index] = TRUE THEN Flap[Index] ← 0 ENDIF NEXT Index; CASE OF Compound(3); REPEAT UNTIL AllDone() = TRUE; WHILE Result[3] <> FALSE. (b) Give the data type of Available (TRUE), Received (\"18/04/2021\") and Index (100).", "A subroutine is a call such as Compound(3) or AllDone().",
  "<p><b>(a)</b> " + mks(["FOR with IF inside: selection and iteration", "CASE OF Compound(3): selection and subroutine", "REPEAT UNTIL AllDone() = TRUE: iteration and subroutine", "WHILE Result[3] <> FALSE: iteration"]) + "</p><p><b>(b)</b> " + mks(["Available: BOOLEAN", "Received: STRING (it is in quotes)", "Index: INTEGER"], "a") + "</p>", "Calling Received a DATE. The quotes make it a STRING.") + peq(SRC("s25", "21", "Q1(a)(b)"), "4 + 5 marks", "Complete / Tick",
  "(a) Complete the identifier table: \"Fruit\" (a category of stock sold in the shop); 20/02/2025 (when an item was sold); 12.67 (the cost of an item); TRUE (to indicate if an item is in stock). (b) Tick assignment, selection and iteration for: Result ← CalculateTotal(); WHILE IsClosed; REPEAT INPUT Value UNTIL Sales[4] > Value; IF Sales[Current] <= 150 THEN Discount ← TRUE ENDIF; CASE OF Option.", "Category STRING, DateSold DATE, Cost REAL, InStock BOOLEAN.",
  "<p><b>(a)</b> " + mks(["Category: STRING", "DateSold: DATE", "ItemCost: REAL", "InStock: BOOLEAN"]) + "</p><p><b>(b)</b> " + mks(["Result ← CalculateTotal(): assignment", "WHILE IsClosed: iteration", "REPEAT INPUT ... UNTIL: iteration (and assignment, as the table gives)", "IF ... Discount ← TRUE: selection and assignment", "CASE OF Option: selection"], "a") + "</p>", None) + peq(SRC("w25", "22", "Q1(a)(b)"), "4 + 3 marks", "Tick / Complete",
  "(a) Tick selection, iteration and subroutines for: IF Status = FALSE THEN FOR Count ← 1 TO 20 CALL Reset(Count) NEXT Count ENDIF; OTHERWISE : Status ← TRUE; WHILE AllDone() = TRUE; 30 : NextChar ← 'X'. (b) Give the data type of Result (5.42), MonthLetter (\"JFMAMJJASOND\") and Birthday (15/11/2009).", "A CASE branch is selection; a function call in the test is a subroutine.",
  "<p><b>(a)</b> " + mks(["IF with FOR and CALL: selection, iteration and subroutine", "OTHERWISE : Status ← TRUE: selection", "WHILE AllDone() = TRUE: iteration and subroutine", "30 : NextChar ← 'X': selection"]) + "</p><p><b>(b)</b> " + mks(["Result: REAL", "MonthLetter: STRING", "Birthday: DATE"], "a") + "</p>", None)

review = req("4 marks", "Complete", "Complete an identifier table for a school library: \"Dune\" (the title of a book); 12 (the number of days a book is borrowed); 1.50 (the fine per day); TRUE (whether the book has been returned).", "Name and type each.", "<p>" + mks(["Title: STRING", "DaysBorrowed: INTEGER", "FinePerDay: REAL", "Returned: BOOLEAN"]) + "</p>", None) + req("3 marks", "Draw", "Draw a flowchart for: input a number; if it is greater than 100 output \"Large\" otherwise output \"Small\".", "One decision.", "<p>" + mks(["START, INPUT Number", "A decision Number > 100 with YES and NO exits", "OUTPUT \"Large\" and OUTPUT \"Small\" on the correct exits, then END"]) + "</p>" + flow_html({"S": ("term", "START", 200, 18), "N": ("io", "INPUT Number", 200, 64), "D": ("dec", "Number > 100 ?", 200, 125), "L": ("io", "OUTPUT \"Large\"", 80, 190, (130, 36)), "M": ("io", "OUTPUT \"Small\"", 320, 190, (130, 36)), "E": ("term", "END", 200, 250)}, [("S", "b", "N", "t", [], None, None), ("N", "b", "D", "t", [], None, None), ("D", "l", "L", "t", [(80, 125)], "YES", (112, 118)), ("D", "r", "M", "t", [(320, 125)], "NO", (282, 118)), ("L", "b", "E", "l", [(80, 250)], None, None), ("M", "b", "E", "r", [(320, 250)], None, None)], w=420, h=275), None) + req("2 marks", "Explain", "Explain why the counter in a loop is set to zero before the loop, not inside it.", "It would reset.", "<p>" + mks(["Inside the loop it would be set to zero on every pass", "so the count would never grow beyond 1"]) + "</p>", None) + req("2 marks", "State", "State the difference between WHILE and REPEAT ... UNTIL.", "Test first or last.", "<p>" + mks(["WHILE tests the condition before the body (the body may never run)", "REPEAT ... UNTIL tests after the body (the body runs at least once)"]) + "</p>", None) + req("2 marks", "State", "State two items an identifier table records, other than the name.", "Type, purpose, example.", "<p>" + mks(["The data type", "The purpose or explanation, or an example value"]) + "</p>", None)

tips = tips_html([
  ("Meaningful names.", "Not X or Temp."),
  ("Type from the example value.", "Quotes: STRING. Decimal: REAL."),
  ("Initialise before the loop.", "Input inside it."),
  ("Decision: diamond, YES and NO.", "Input/output: parallelogram."),
  ("A line can hold several constructs.", "Tick every one."),
  ("WHILE: test first. REPEAT: test last.", "Name the loop type."),
], [("an algorithm", "A sequence of steps that solves a problem."), ("an identifier table", "A table of variables with names, types, purposes and example values."), ("iteration", "Repeating statements in a loop."), ("selection", "Choosing which statements to run.")],
  [("Complete", "Fill in the table."), ("Draw", "Draw the flowchart."), ("Write", "Write the pseudocode."), ("State", "Short answer.")]) + FC

js = AKJS + AK20JS + r'''
(function () {
  const draw = (s) => { const k = Math.round(s.i); const B = (x, y, w, t, kind, on) => (kind === "dec" ? SV.path(`M${x},${y - 22} L${x + w / 2},${y} L${x},${y + 22} L${x - w / 2},${y} Z`, on ? "f3" : "cell") : SV.rect(x - w / 2, y - 14, w, 28, on ? "f3" : "cell", { rx: kind === "term" ? 14 : 3 })) + SV.text(x, y + 4, t, "lbl", { "text-anchor": "middle", style: "font-size:10px" });
    let o = B(100, 20, 90, "START", "term", k >= 0) + (k >= 1 ? B(100, 65, 150, "Total ← 0", "proc", true) : "") + (k >= 2 ? B(100, 110, 150, "INPUT Number", "proc", true) : "") + (k >= 3 ? B(100, 160, 150, "Number = 0 ?", "dec", true) : "") + (k >= 4 ? B(300, 160, 150, "Total ← Total + Number", "proc", true) : "") + (k >= 5 ? B(100, 215, 130, "OUTPUT Total", "proc", true) : "");
    if (k >= 4) o += SV.path("M175,160 H225", "ax") + SV.path("M300,146 V110 H175", "ax"); return o; };
  Lib.stepper($("#stA"), { w: 440, h: 240, label: "Flowchart", base: { i: 0 }, draw, tween: 100, dwell: 2200, steps: ["START.", "Initialise Total before the loop.", "Input a number (in the loop).", "A decision: is it 0?", "NO: add to Total and loop back to the input.", "YES: output Total."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const ins = [5, 2, -3, 0]; const draw = (s) => { const k = Math.round(s.i); let pos = 0, cp = 0, neg = 0, cn = 0; for (let i = 0; i < Math.min(k, 3); i++) { if (ins[i] > 0) { pos += ins[i]; cp++; } else { neg += ins[i]; cn++; } }
    let o = SV.text(20, 22, "inputs: " + ins.slice(0, Math.min(k + 1, 4)).join(", "), "lbl bd", { style: "font-size:13px" }); [["PosSum", pos], ["PosCount", cp], ["NegSum", neg], ["NegCount", cn]].forEach(([n, v], i) => o += SV.rect(20 + i * 110, 40, 100, 44, "cell", { rx: 6 }) + SV.text(70 + i * 110, 58, n, "sm", { "text-anchor": "middle" }) + SV.text(70 + i * 110, 76, v, "lbl bd", { "text-anchor": "middle" }));
    o += SV.text(20, 112, k < 3 ? "input " + ins[k] + (ins[k] > 0 ? ": positive, add to PosSum" : ": negative, add to NegSum") : "input 0: leave the loop and output the four values", "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stB"), { w: 460, h: 130, label: "Trace", base: { i: 0 }, draw, tween: 100, dwell: 2400, steps: ["First input 5.", "Next input 2.", "Next input −3.", "Input 0 ends the loop."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const L = ["Total ← 0", "FOR i ← 1 TO 3", "IF Total > 5 THEN", "OUTPUT Total"]; const kinds = ["assignment", "iteration", "selection", "input/output"]; const draw = (s) => { const k = Math.round(s.i); let o = ""; L.forEach((l, i) => { o += SV.rect(20, 14 + i * 34, 220, 28, i === k ? "f3" : "cell", { rx: 5 }) + SV.text(30, 33 + i * 34, l, "lbl", { style: "font-size:12px" }) + (i === k ? SV.text(260, 33 + i * 34, "← " + kinds[i], "lbl bd t3", { style: "font-size:12px" }) : ""); }); return o; };
  Lib.stepper($("#stC"), { w: 440, h: 160, label: "Constructs", base: { i: 0 }, draw, tween: 100, dwell: 2400, steps: kinds.map((c, i) => ({ cap: "This line is <b>" + c + "</b>.", s: { i } })) });
})();

(function () {
  let pos = 0, cp = 0, neg = 0, cn = 0, done = false, log = [];
  const paint = () => { $("#flV").innerHTML = `PosSum = <b>${pos}</b>, PosCount = <b>${cp}</b>, NegSum = <b>${neg}</b>, NegCount = <b>${cn}</b>.` + (log.length ? "<br>Inputs: " + log.join(", ") : "") + (done ? "<br><b>0 entered: the loop ends and the four values are output.</b>" : ""); };
  const add = (v) => { if (done) return; log.push(v); if (v === 0) done = true; else if (v > 0) { pos += v; cp++; } else { neg += v; cn++; } paint(); };
  $("#fl_p5").onclick = () => add(5); $("#fl_p2").onclick = () => add(2); $("#fl_m3").onclick = () => add(-3); $("#fl_m7").onclick = () => add(-7); $("#fl_0").onclick = () => add(0); $("#fl_r").onclick = () => { pos = cp = neg = cn = 0; done = false; log = []; paint(); }; paint();
})();
btnTable("cB", "cO", [
  ["Total ← Total + 1", "Assignment", "Stores a value"],
  ["IF Mark > 74 THEN", "Selection", "Chooses"],
  ["WHILE Index < 7", "Iteration", "Repeats while true"],
  ["CASE OF Option", "Selection", "Chooses between cases"],
  ["REPEAT INPUT Value UNTIL ...", "Iteration (and input)", "Repeats; one line, two constructs"]
], ["Line", "Construct", "Why"]);
btnTable("sB", "sO", [
  ["START / END", "Terminator (rounded)", "Begins and ends"],
  ["INPUT / OUTPUT", "Parallelogram", "Data in or out"],
  ["Total ← 0", "Rectangle", "A process (assignment)"],
  ["Number = 0 ?", "Diamond", "A decision with YES and NO"],
  ["CALL Update(...)", "Rectangle with double sides", "A subroutine call"]
], ["Step", "Symbol", "Meaning"]);
''' + _prjs

finish("as-9-2-1-algorithms-flowcharts-identifiers", "as921", "Algorithms, Flowcharts and Identifier Tables",
  "Algorithms, identifier tables with data types, the assignment, selection and iteration constructs, and drawing and reading program flowcharts, with animations, labs and the real Paper 2 questions from 2021 to 2026.",
  "9.2.1", "9 · Algorithm design and problem-solving", "section 9.2 Algorithms", learn, watch, explore, _pr, real, where, past, review,
  "Part 1 is real 9618 questions on algorithms, identifier tables and flowcharts (Paper 2), 2021 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", tips, js)
