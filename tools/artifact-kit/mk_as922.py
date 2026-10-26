"""AS CS 9.2.2: stepwise refinement, structured English and from flowchart to pseudocode. Run: python3 tools/artifact-kit/mk_as922.py"""
from ak9 import *

J = ("proc", "", 0, 0, (4, 4))
def jn(x, y): return ("proc", "", x, y, (4, 4))

F_BOOT = flow({
  "S": ("term", "START", 170, 16), "A": ("proc", "Set Count to 1", 170, 58, (150, 30)), "B": ("proc", "Set Flag to FALSE", 170, 100, (150, 30)), "J": jn(170, 128),
  "D": ("dec", "Is Flag = FALSE\nAND Count <= 5 ?", 170, 185, (210, 66)), "R1": ("call", "ReBoot()", 440, 185, (110, 32)), "R2": ("proc", "Set Count to Count + 1", 440, 232, (160, 30)), "R3": ("proc", "Set Flag to Check()", 440, 276, (150, 30)),
  "D2": ("dec", "Is Flag = FALSE ?", 170, 270, (170, 56)), "C": ("call", "Alert(27)", 170, 345, (120, 32)), "E": ("term", "END", 170, 400)},
  [("S", "b", "A", "t", [], None, None), ("A", "b", "B", "t", [], None, None), ("B", "b", "J", "t", [], None, None), ("J", "b", "D", "t", [], None, None),
   ("D", "r", "R1", "l", [], "YES", (305, 178)), ("R1", "b", "R2", "t", [], None, None), ("R2", "b", "R3", "t", [], None, None), ("R3", "l", "J", "r", [(340, 276), (340, 128)], None, None),
   ("D", "b", "D2", "t", [], "NO", (176, 230)), ("D2", "b", "C", "t", [], "YES", (176, 318)), ("C", "b", "E", "t", [], None, None), ("D2", "l", "E", "l", [(30, 270), (30, 400)], "NO", (36, 262))], w=560, h=425, cap="the ReBoot flowchart")
F_PAIRS = flow({
  "S": ("term", "START", 170, 16), "I1": ("proc", "Tries ← 0\nCount ← 0", 170, 56, (130, 36)), "J": jn(170, 92), "N": ("io", "INPUT A, B", 170, 122, (150, 30)), "T": ("proc", "Tries ← Tries + 1", 170, 168, (150, 30)),
  "D1": ("dec", "A > B ?", 170, 232, (130, 56)), "C": ("proc", "Count ← Count + 1", 400, 232, (150, 30)), "D2": ("dec", "Count = 10 ?", 400, 305, (150, 56)), "O": ("io", "OUTPUT Tries", 400, 370, (130, 30)), "E": ("term", "END", 400, 418)},
  [("S", "b", "I1", "t", [], None, None), ("I1", "b", "J", "t", [], None, None), ("J", "b", "N", "t", [], None, None), ("N", "b", "T", "t", [], None, None), ("T", "b", "D1", "t", [], None, None),
   ("D1", "r", "C", "l", [], "YES", (255, 224)), ("D1", "l", "J", "l", [(40, 232), (40, 92)], "NO", (46, 224)), ("C", "b", "D2", "t", [], None, None),
   ("D2", "b", "O", "t", [], "YES", (406, 340)), ("O", "b", "E", "t", [], None, None), ("D2", "l", "J", "r", [(300, 305), (300, 92)], "NO", (322, 297))], w=540, h=445, cap="count pairs until A has been greater than B 10 times")
F_CHAR = flow({
  "S": ("term", "START", 170, 16), "P1": ("io", "OUTPUT \"Enter a character\"", 170, 56, (190, 30)), "I1": ("io", "INPUT MyChar", 170, 96, (150, 30)), "P2": ("io", "OUTPUT \"Enter a count\"", 170, 136, (190, 30)), "I2": ("io", "INPUT MyCount", 170, 176, (150, 30)),
  "A": ("proc", "MyString ← \"\"", 170, 216, (150, 30)), "J": jn(170, 246), "D": ("dec", "MyCount > 0 ?", 170, 292, (140, 56)), "C1": ("proc", "MyString ← MyString & MyChar", 420, 292, (190, 30)), "C2": ("proc", "MyCount ← MyCount − 1", 420, 338, (170, 30)),
  "O": ("io", "OUTPUT MyString", 170, 350, (150, 30)), "E": ("term", "END", 170, 396)},
  [("S", "b", "P1", "t", [], None, None), ("P1", "b", "I1", "t", [], None, None), ("I1", "b", "P2", "t", [], None, None), ("P2", "b", "I2", "t", [], None, None), ("I2", "b", "A", "t", [], None, None), ("A", "b", "J", "t", [], None, None), ("J", "b", "D", "t", [], None, None),
   ("D", "r", "C1", "l", [], "YES", (250, 285)), ("C1", "b", "C2", "t", [], None, None), ("C2", "l", "J", "r", [(310, 338), (310, 246)], None, None), ("D", "b", "O", "t", [], "NO", (176, 328)), ("O", "b", "E", "t", [], None, None)], w=540, h=420, cap="repeat a character")

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p><b>Stepwise refinement</b> is increasing the level of detail of an algorithm by breaking each step into smaller steps, repeatedly, <b>until the steps can be directly translated into lines of code</b>. An algorithm can be refined and written in <b>structured English</b>: numbered steps in plain words that name the variables, the loops and the decisions, but contain <b>no pseudocode statements</b>. A good description mentions the same things the mark scheme looks for: <b>open the file</b> (in the right mode) and close it, <b>initialise</b> a variable or index before the loop, a <b>loop</b> with its end condition, the <b>input or read</b> inside the loop, the <b>test</b> and its action, and the <b>increment</b>. The constructs you must identify are <b>sequence</b> (steps in order), <b>selection</b> and <b>iteration</b>. You must also be able to turn a program flowchart into pseudocode, step by step, or complete a flowchart from words.</p></div>

  <h2>1 · Stepwise refinement</h2>
  <p>Start with the problem in one line, then rewrite each step in more detail. Example: <i>copy the lines of a file into an array</i> refines to:</p>
  <ol>
    <li>Open the file for reading (and close it afterwards).</li>
    <li>Set an index variable to 1 before the loop.</li>
    <li>Repeat until the end of the file is reached:
      <ol type="a"><li>read one line from the file into a string variable;</li><li>store that line in the array at the index;</li><li>add 1 to the index.</li></ol></li>
    <li>Close the file.</li>
  </ol>
  <p>Each line is now simple enough to become one pseudocode statement. The construct needed apart from sequence is <b>iteration</b> (a conditional loop, repeating until the end of the file), and a <b>selection</b> statement tests the value returned by the EOF function or whether an element is blank.</p>

  <h2>2 · Writing an algorithm in structured English</h2>
  <ul>
    <li>Use numbered steps and indent the steps inside a loop.</li>
    <li>Name the variables the question gives (MyChar, MyCount).</li>
    <li>For files: say <b>open</b>, the <b>mode</b> (read, write or <b>append</b> if the file already has data you must keep), and <b>close</b>.</li>
    <li>Do not write pseudocode statements such as <span class="mono">WHILE</span> or <span class="mono">←</span>; use words.</li>
  </ul>
  <p><b>Example answer</b> for "input numbers until zero, then output the sum of the positive and the sum of the negative numbers": (1) set the two sums to zero; (2) prompt for and input a number; (3) if it is greater than zero add it to the positive sum, if it is less than zero add it to the negative sum; (4) repeat from step 2 if the number was not zero; (5) output the two sums.</p>

  <h2>3 · From a flowchart to pseudocode</h2>
  <p>Take the flowchart in order. The two boxes before a loop become initialisations. A decision whose YES branch returns to the decision itself is a <b>WHILE</b> loop with the decision as its condition. After the loop, a decision with two exits is an <b>IF</b>. A call box is <b>CALL</b>.</p>
  ''' + F_BOOT + '''
  ''' + code('''Count ← 1
Flag ← FALSE
WHILE Flag = FALSE AND Count <= 5
   CALL ReBoot()
   Count ← Count + 1
   Flag ← Check()
ENDWHILE
IF Flag = FALSE THEN
   CALL Alert(27)
ENDIF'''.split("\n"), label="Pseudocode for the flowchart (O/N 2021)") + '''

  <h2>4 · From words to a flowchart</h2>
  <p>Count pairs of values input until A has been greater than B ten times, then output the number of pairs:</p>
  ''' + F_PAIRS + '''
  <p>Marks: initialise both counts; increment Tries for every pair input; compare A &gt; B and increment Count if true; test for Count = 10 (the decision must have YES and NO labels); output Tries when it is, otherwise loop.</p>

  <h2>Common ways to lose marks</h2>
  <ul>
    <li>Writing pseudocode when the question says "do not include pseudocode statements".</li>
    <li>Forgetting to open or close the file, or using write mode when data must be kept (append).</li>
    <li>Not initialising the index or counter before the loop.</li>
    <li>Leaving out the end condition of the loop (until end of file, until the value is zero).</li>
    <li>Not incrementing the index inside the loop.</li>
  </ul>
'''

watch = '''
  <h2>1 · Refining a step</h2>
  <div id="stA"></div>
  <h2>2 · A loop copying a file into an array</h2>
  <div id="stB"></div>
  <h2>3 · From flowchart to pseudocode</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Run the algorithm: file into array</h2>
  <p>Step through the algorithm. The file has four lines.</p>
  <div class="card"><div class="btnrow"><button id="fa_step">Step</button><button id="fa_reset">Reset</button></div><div id="faV"></div></div>
  <h2>Lab 2 · Order the steps</h2>
  <div class="card"><div id="oB" class="btnrow"></div><div id="oO"></div></div>
  <h2>Lab 3 · Which file mode?</h2>
  <div class="card"><div id="mB" class="btnrow"></div><div id="mO"></div></div>
'''

_pr, _prjs = PR(["Which construct is needed?", "Right step or wrong step?", "Match the term to its meaning", "Put the file-to-array steps in order", "Working out", "Multiple choice"],
  ("Which construct is being used?", ["Sequence", "Selection", "Iteration"], [("Steps carried out one after another in order", 0), ("Test whether an element is blank", 1), ("Repeat until the end of the file", 2), ("Open the file, then read a line", 0), ("Check the value returned by EOF", 1), ("Repeat for 35 students", 2)], "Order, choice, repeat."),
  ("Is the step correct for an algorithm that appends the names of students with a mark under 20 to an existing file?", ["Correct", "Wrong"], [("Open the file in append mode", 0), ("Open the file in write mode", 1), ("Write the name if the mark is less than 20", 0), ("Write the mark as well as the name", 1), ("Repeat for each student", 0), ("Close the file before the first student", 1)], "Append keeps the old data."),
  [["Stepwise refinement", "Adding detail until each step can be coded"], ["Structured English", "Numbered steps in words, no pseudocode"], ["Sequence", "Steps in order"], ["Iteration", "Repeating steps"], ["Append mode", "Adds to a file without overwriting it"]],
  ("Put the algorithm for copying a file into an array in order.", ["Open the file for reading", "Set the index to 1", "Repeat until the end of the file is reached", "Read a line, store it in the array at the index, add 1 to the index", "Close the file"], "Open, index, loop, body, close."),
  [{"q": "A file has 4 lines copied into an array starting at index 1. What is the index after the last line is stored and incremented?", "a": 5, "unit": "", "tol": 0.01, "hint": "4 lines, then +1.", "sol": "<b>5</b>."}, {"q": "An array has 65 elements and the algorithm checks each once. How many loop passes?", "a": 65, "unit": "", "tol": 0.01, "hint": "One per element.", "sol": "<b>65</b>."}, {"q": "Of 65 elements, 40 are blank. How many lines are written to the file?", "a": 25, "unit": "", "tol": 0.01, "hint": "65 − 40.", "sol": "<b>25</b>."}, {"q": "A student list has 35 students and the mark under 20 for 6 of them. How many names are appended?", "a": 6, "unit": "", "tol": 0.01, "hint": "Only those under 20.", "sol": "<b>6</b>."}, {"q": "A string is to be built by repeating a character 5 times. How many times is the loop body run if the counter counts down from 5 to 0 (loop while counter > 0)?", "a": 5, "unit": "", "tol": 0.01, "hint": "5, 4, 3, 2, 1.", "sol": "<b>5</b>."}],
  [("Stepwise refinement:", ["Adds detail until steps can be coded", "Compiles the code", "Removes steps", "Draws the screen"], 0, "Adds detail."), ("To keep existing data in a file, open it in:", ["Append mode", "Write mode", "Read mode only", "Delete mode"], 0, "Append."), ("A loop that repeats until the end of a file is:", ["Iteration", "Selection", "Sequence", "Declaration"], 0, "Iteration."), ("Structured English contains:", ["No pseudocode statements", "Only code", "Only flowcharts", "Compiler errors"], 0, "No pseudocode."), ("Before a counting loop you should:", ["Initialise the variable", "Close the file", "Output the result", "Nothing"], 0, "Initialise."), ("A decision with a loop back is usually a:", ["WHILE loop", "FUNCTION", "DECLARE", "CASE"], 0, "WHILE.")],
  [("Stepwise refinement", "More detail until directly codeable."), ("Structured English", "Numbered words; no pseudocode."), ("Sequence", "Steps in order."), ("Selection", "A test and a choice."), ("Iteration", "A loop with an end condition."), ("Append", "Add to the end of a file."), ("Initialise", "Set before the loop."), ("Increment", "Add 1 each pass.")])

real = RWNOTE + (
rw("Writing a recipe for a robot", "'Make a sandwich' is refined into: get two slices, spread butter, add filling... until each step is simple enough for the robot to do.", "stepwise refinement.") +
rw("A to-do list that keeps growing", "Opening a file to add a new line at the end, instead of replacing the file, is append mode.", "append.") +
rw("Tidy code from a plan", "A programmer writes the numbered steps first, then turns each step into one line of code: the plan is the structured English.", "stepwise refinement.") +
rw("Turning a flowchart into code", "Each box becomes a statement and each loop-back becomes a WHILE: a mechanical process once you know the shapes.", "flowchart to pseudocode.") +
rw("Checking an algorithm by hand", "Before coding, you work through a small example to see that the steps and the loop end work.", "dry run.")
)

where = [
  ("O/N 2021", "21, 23", "2(a), (b)", "6 + 6", "Refine and describe a sort in structured English; pseudocode for a flowchart"),
  ("M/J 2022", "22", "2(a)", "5 + 1 + 1", "Describe the steps for appending names to a file; why a file not an array; why not write mode"),
  ("O/N 2022", "23", "3", "5", "Describe the algorithm for summing positive and negative numbers"),
  ("M/J 2023", "21", "2(a), (b)", "4 + 3", "Draw a flowchart for repeating a character; declare and assign a date"),
  ("M/J 2024", "21", "2(a), (b)", "5 + 2", "Complete the flowchart counting pairs; the variable ThisSequence"),
  ("M/J 2024", "23", "2", "5 + 2", "Five steps for copying a file into an array; another construct"),
  ("M/J 2025", "22", "2(a)", "2", "Describe stepwise refinement"),
  ("O/N 2025", "23", "2", "6 + 2", "Six steps for writing non-blank elements to a file; another construct")]

past = '''  <p class="note">Stepwise refinement answers are marked on a fixed list of points: open and close the file, initialise, loop, read or test, write or store, increment. Count the points you have before you stop. Paper 2 questions are reworded from the papers; check the original paper and mark scheme for the exact wording.</p>
''' + peq(SRC("w21", "21/23", "Q2(a)"), "6 marks", "Apply",
  "An algorithm to sort a 1D array into ascending order is described: move the largest value to the end; keep repeating until the array is sorted. Apply stepwise refinement to produce a more detailed description in structured English, with no pseudocode statements.", "Index variable, a loop, an inner loop, compare, swap.",
  "<p>Any six: " + mks(["Use a variable as an index to the array", "A loop to iterate through the array", "An inner loop with a reducing range", "Test if the current element is greater than the next element", "If so then swap the elements", "A description of the swap (store one value in a temporary variable)", "An attempt at an efficient algorithm"]) + "</p><p>For example: (1) set a variable Last to the last position of the array; (2) set an index to 1; (3) while the index is less than Last: if the element at the index is greater than the next element, swap them using a temporary variable; add 1 to the index; (4) reduce Last by 1; (5) repeat from step 2 until Last is 1 (no swaps are needed).</p>", "Writing pseudocode (WHILE, ←). The question says to use structured English.") + peq(SRC("w21", "21/23", "Q2(b)"), "6 marks", "Write",
  "The program flowchart shown: START; Set Count to 1; Set Flag to FALSE; Is Flag = FALSE AND Count <= 5? YES: ReBoot(); Set Count to Count + 1; Set Flag to Check(); back to the test; NO: Is Flag = FALSE? YES: Alert(27); NO or after: END. Write pseudocode for the algorithm.", "A WHILE with both conditions, then an IF after.",
  "<p>" + F_BOOT + "</p>" + code('''Count ← 1
Flag ← FALSE
WHILE Flag = FALSE AND Count <= 5
   CALL ReBoot()
   Count ← Count + 1
   Flag ← Check()
ENDWHILE
IF Flag = FALSE THEN
   CALL Alert(27)
ENDIF'''.split("\n")) + "<p>" + mks(["Initialisation of Count and Flag", "WHILE ... ENDWHILE (or REPEAT ... UNTIL)", "including both conditions", "Call ReBoot() and increment Count inside the loop", "Assign the return value from Check() to Flag inside the loop", "A final test of Flag and a call to Alert(27), not in a loop"]) + "</p>", "Putting the test of Flag and Alert(27) inside the loop.") + peq(SRC("s22", "22", "Q2(a)"), "5 + 1 + 1 marks", "Describe / Explain",
  "An algorithm prompts and inputs the name and test mark for each of 35 students and adds the names of students with a mark below 20 to an existing text file Support_List.txt, which contains data from other group tests. (i) Describe the steps. Do not include pseudocode. (ii) Explain why it may be better to store the names in a file than in an array. (iii) Explain why WRITE mode cannot be used.", "Open in append mode; prompt and input; if mark is 20 or more skip; write the name; repeat 35 times.",
  "<p><b>(i)</b> " + mks(["Open the file in append mode (and subsequently close it)", "Prompt for and input a student name and mark", "If the mark is greater than or equal to 20 jump to step 5", "Write only the name to the file", "Repeat from step 2 for 35 times (the number of students)"]) + "</p><p><b>(ii)</b> " + mks(["Data in a file is saved after the computer is switched off, so it does not have to be entered again when the program is re-run"], "a") + "</p><p><b>(iii)</b> " + mks(["So that the existing file data is not overwritten"], "b") + "</p>", None) + peq(SRC("w22", "23", "Q3"), "5 marks", "Describe",
  "An algorithm processes a sequence of numbers (positive or negative, integer or decimal): prompt and input one number at a time until zero is input; sum the negative numbers; sum the positive numbers; when zero is input, output the two sums and end. Describe the algorithm needed. Do not include pseudocode.", "Two REAL sums set to zero; input; add to the right sum; repeat unless zero; output.",
  "<p>" + mks(["Declare two (real) variables for the two sums and initialise both to zero", "Prompt for and input a number", "If the number is greater than zero add it to the positive sum; if less than zero add it to the negative sum", "Repeat from the input step if the number is not zero", "After the loop output the positive and negative sums"]) + "</p>", "Using integers for the sums. The numbers may be decimal.") + peq(SRC("s23", "21", "Q2(a)(b)"), "4 + 3 marks", "Draw / Write",
  "(a) An algorithm: 1. prompt and input a character and store it in MyChar; 2. prompt and input an integer and store it in MyCount; 3. generate a string of MyChar repeated MyCount times; 4. output the string. Draw a program flowchart. (b) A different part of the program uses the variable StartDate. Write pseudocode to declare StartDate and assign it the date 15/11/2005.", "Two prompts and inputs; empty string; loop with decrement and concatenate; output.",
  "<p><b>(a)</b> " + mks(["Both prompts", "Both inputs using the identifiers MyChar and MyCount", "Initialise MyString to an empty string and output it after the loop", "A loop of MyCount iterations including decrementing MyCount", "Concatenation inside the loop"]) + " (max 4)</p>" + F_CHAR + "<p><b>(b)</b> " + mks(["DECLARE StartDate : DATE", "StartDate ← SETDATE(15, 11, 2005) (the function and its three parameters)"], "a") + "</p>", None) + peq(SRC("s24", "21", "Q2"), "5 + 2 marks", "Complete / Describe",
  "An algorithm: 1. repeatedly input a pair of numeric values A and B; 2. count the number of pairs input until A has been greater than B 10 times; 3. output the number of pairs. (a) Complete the program flowchart. (b) Step 1 changes: a variable ThisSequence is used to enter a sequence of 10 pairs of values with a single input statement. Describe the variable ThisSequence and how the numbers are extracted.", "Two counters, increment, compare, test 10, output.",
  "<p><b>(a)</b> One mark per region: " + mks(["Initialise both counts", "Increment Tries every time a pair is input", "Compare A > B and increment Count if TRUE", "Test for Count = 10, with Yes and No labels", "If so output Tries, otherwise loop"]) + "</p>" + F_PAIRS + "<p><b>(b)</b> " + mks(["A variable of type string is input, for example \"67,72\"", "A special character is used to separate each numeric value, or all the numbers are a fixed length, so the string can be split into the numbers"], "a") + "</p>", "Leaving the Yes and No labels off the decision. The mark needs them.") + peq(SRC("s24", "23", "Q2"), "5 + 2 marks", "Outline / Identify",
  "A program uses a global 1D array of type string and a text file. An algorithm: copy the first line of the file into the first element of the array; the second into the second element; continue until all lines have been copied. Stepwise refinement is applied. (a) Outline five steps that could be used to produce pseudocode (no pseudocode statements; the array has more elements than the file has lines). (b) Identify one other construct (besides sequence) needed in the pseudocode and explain its use.", "Open; index; loop to end of file; read; store; increment.",
  "<p><b>(a)</b> Any five: " + mks(["Open the file (in read mode and subsequently close it)", "Initialise an index variable to 1 (or 0)", "Repeat until the end of the file is reached", "Read a line from the file into a string variable", "Store the line in the array at the index", "Increment the index in the loop"]) + "</p><p><b>(b)</b> " + mks(["Construct: a conditional loop (iteration); use: to keep repeating until the end of the file is reached", "Alternative: a selection statement; use: to test the value returned by the EOF() function"], "a") + "</p>", None) + peq(SRC("s25", "22", "Q2(a)"), "2 marks", "Describe",
  "Stepwise refinement has been used in the design of the program that calculates employees' pay. Describe stepwise refinement.", "Add detail; until steps can be coded.",
  "<p>" + mks(["To increase the level of detail of the algorithm, or to break the problem or task into smaller steps", "until the steps can be directly translated into lines of code"]) + "</p>", None) + peq(SRC("w25", "23", "Q2"), "6 + 2 marks", "Describe / Identify",
  "A global 1D array of type STRING has 65 elements and an existing text file stores its data; only non-blank elements are written. An algorithm: write the first element as a new line, continue until all elements have been written, each to a new line. Stepwise refinement is applied. (a) Describe up to six steps that could be used to produce pseudocode (no pseudocode statements). (b) Iteration is one construct. Identify one other construct required and explain how it is used.", "Open in append; index; loop; test blank; write; increment.",
  "<p><b>(a)</b> Any six: " + mks(["Open the file in append mode (and close it after the loop)", "Initialise a variable to 1 (or 0) before the loop", "Use the variable as an index to access an element of the array in the loop", "Test if the element is blank or empty", "If it is not blank write the value to the file", "Increment the variable", "Repeat until all 65 elements have been checked"]) + "</p><p><b>(b)</b> " + mks(["Selection: to test whether the array element is blank", "Alternative: sequence, to specify the order the steps must be followed"], "a") + "</p>", "Opening the file in write mode when the file already holds data that must be kept.")

review = req("4 marks", "Describe", "Describe an algorithm (no pseudocode) that inputs the marks of 30 students and outputs how many marks are 50 or more.", "Counter; loop 30 times; test; output.", "<p>" + mks(["Set a counter to zero", "Repeat 30 times: input a mark", "If the mark is 50 or more add 1 to the counter", "After the loop output the counter"]) + "</p>", None) + req("3 marks", "Describe", "Describe the file steps to add a new name to the end of an existing list without losing the old names.", "Append.", "<p>" + mks(["Open the file in append mode", "Write the new name", "Close the file"]) + "</p>", None) + req("2 marks", "State", "State what stepwise refinement means.", "Detail; code.", "<p>" + mks(["Breaking each step into smaller, more detailed steps", "until each step can be translated directly into code"]) + "</p>", None) + req("3 marks", "Write", "Write pseudocode for: set Total to 0; input a number until it is zero, adding each to Total; output Total.", "WHILE or REPEAT.", "<p>" + mks(["Total ← 0 and an INPUT of the first number", "A loop that stops when the number is 0, adding to Total and inputting the next", "OUTPUT Total after the loop"]) + "</p>" + code("Total ← 0\nINPUT Number\nWHILE Number <> 0\n   Total ← Total + Number\n   INPUT Number\nENDWHILE\nOUTPUT Total".split("\n")), None) + req("2 marks", "Identify", "Identify the construct used when an algorithm tests whether a mark is below 20.", "Selection.", "<p>" + mks(["Selection", "an IF statement to test the condition"]) + "</p>", None)

tips = tips_html([
  ("Open, initialise, loop, close.", "The skeleton of a file algorithm."),
  ("End condition of the loop.", "End of file, zero, count reached."),
  ("Append keeps old data.", "Write overwrites."),
  ("No pseudocode when told not to.", "Use words."),
  ("Increment the index.", "Inside the loop."),
  ("Count your points.", "One mark each; check you have enough."),
], [("stepwise refinement", "Adding detail until each step can be coded."), ("structured English", "An algorithm in numbered steps in words."), ("append mode", "Opening a file to add data at the end."), ("a conditional loop", "A loop that repeats until a condition is met.")],
  [("Describe", "Several steps in order."), ("Outline", "A short list of steps."), ("Draw", "Draw the flowchart."), ("Write", "Write the pseudocode.")]) + FC

js = AKJS + AK20JS + r'''
(function () {
  const draw = (s) => { const k = Math.round(s.i); const lv = [["copy the file into an array"], ["open the file", "set the index", "loop until end of file", "close the file"], ["open the file", "set the index to 1", "loop until end of file:", "   read a line", "   store it at the index", "   add 1 to the index", "close the file"]][Math.min(k, 2)]; let o = ""; lv.forEach((l, i) => o += SV.rect(20, 10 + i * 24, 300, 20, k === 0 ? "f3" : k === 1 ? "f1" : "cell", { rx: 4 }) + SV.text(28, 24 + i * 24, l, "lbl", { style: "font-size:11px" })); o += SV.text(340, 40, ["one step", "refined once", "each step can now be coded"][Math.min(k, 2)], "lbl bd t3", { style: "font-size:12px" }); return o; };
  Lib.stepper($("#stA"), { w: 560, h: 190, label: "Refinement", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: ["The problem as one step.", "<b>Refine</b> it into main steps.", "Refine again until each step can be <b>directly coded</b>."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const file = ["red", "green", "blue", "pink"]; const draw = (s) => { const k = Math.round(s.i); let o = SV.text(20, 16, "file", "sm") + SV.text(250, 16, "array", "sm"); file.forEach((l, i) => o += SV.rect(20, 22 + i * 28, 150, 24, i < k ? "f1" : "cell", { rx: 4 }) + SV.text(28, 39 + i * 28, l, "lbl", { style: "font-size:12px" })); for (let i = 0; i < 6; i++) o += SV.rect(250, 22 + i * 28, 150, 24, "cell", { rx: 4 }) + SV.text(258, 39 + i * 28, (i + 1) + (i < k ? "  " + file[i] : ""), "lbl", { style: "font-size:12px" }); o += SV.text(420, 60, "index = " + (k + 1), "lbl bd t3"); return o; };
  Lib.stepper($("#stB"), { w: 540, h: 195, label: "File into array", base: { i: 0 }, draw, tween: 100, dwell: 1800, steps: ["Open the file; index is 1.", "Read line 1, store it at index 1, index becomes 2.", "Read line 2, store it, index becomes 3.", "Read line 3, store it, index becomes 4.", "Read line 4, store it, index becomes 5. End of file: stop and close."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const L = ["Count ← 1", "Flag ← FALSE", "WHILE Flag = FALSE AND Count <= 5", "   CALL ReBoot()", "   Count ← Count + 1", "   Flag ← Check()", "ENDWHILE", "IF Flag = FALSE THEN CALL Alert(27)"]; const at = [[0, 1], [2, 5], [7, 7]][Math.min(k, 2)]; let o = ""; L.forEach((l, i) => o += SV.rect(20, 8 + i * 22, 340, 20, i >= at[0] && i <= at[1] ? "f3" : "cell", { rx: 3 }) + SV.text(28, 22 + i * 22, l, "lbl", { style: "font-size:11px" })); o += SV.text(380, 40, ["before the loop: initialise", "loop-back decision: WHILE", "final decision: IF"][Math.min(k, 2)], "lbl bd t3", { style: "font-size:11px" }); return o; };
  Lib.stepper($("#stC"), { w: 620, h: 190, label: "Flowchart to code", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: ["Initialisation boxes become assignments.", "The loop-back decision becomes a <b>WHILE</b> loop.", "The final decision becomes an <b>IF</b>."].map((c, i) => ({ cap: c, s: { i } })) });
})();

(function () {
  const file = ["red", "green", "blue", "pink"]; let st;
  const reset = () => { st = { phase: 0, idx: 1, arr: [], pos: 0, log: ["Ready."] }; paint(); };
  const step = () => { const s = st; if (s.phase === 0) { s.log.push("Open the file for reading; index = 1"); s.phase = 1; } else if (s.phase === 1) { if (s.pos >= file.length) { s.log.push("End of file reached: leave the loop"); s.phase = 2; } else { const l = file[s.pos++]; s.arr[s.idx - 1] = l; s.log.push(`Read "${l}", store it in array[${s.idx}], index becomes ${s.idx + 1}`); s.idx++; } } else if (s.phase === 2) { s.log.push("Close the file. Done."); s.phase = 3; } paint(); };
  const paint = () => { const s = st; let h = '<div class="tw"><table class="t mono"><tr><th>index</th>' + [1, 2, 3, 4, 5, 6].map((i) => `<th>${i}</th>`).join("") + "</tr><tr><td>array</td>" + [0, 1, 2, 3, 4, 5].map((i) => `<td>${s.arr[i] || ""}</td>`).join("") + "</tr></table></div>"; $("#faV").innerHTML = h + '<div class="verdict">' + s.log.slice(-3).join("<br>") + "</div>"; };
  $("#fa_step").onclick = step; $("#fa_reset").onclick = reset; reset();
})();
btnTable("oB", "oO", [
  ["Copy a file into an array", "Open, index = 1, loop until end of file (read, store, add 1), close", "Iteration with an end-of-file test"],
  ["Write non-blank array items to a file", "Open in append mode, index = 1, loop 65 times (if not blank write; add 1), close", "Selection inside iteration"],
  ["Sum positives and negatives until 0", "Set sums to 0, input, add to the right sum, repeat until 0, output both", "Selection inside iteration"]
], ["Task", "Steps", "Constructs"]);
btnTable("mB", "mO", [
  ["Read the names in a file", "Read mode", "Nothing is changed"],
  ["Start a new file or replace all its contents", "Write mode", "Overwrites existing data"],
  ["Add names to a file that already has data", "Append mode", "Existing data is kept"]
], ["Task", "Mode", "Why"]);
''' + _prjs

finish("as-9-2-2-stepwise-refinement", "as922", "Stepwise Refinement and Structured English",
  "Stepwise refinement, describing algorithms in structured English, turning a flowchart into pseudocode and words into a flowchart, with animations, a file-to-array simulator and the real Paper 2 questions from 2021 to 2026.",
  "9.2.2", "9 · Algorithm design and problem-solving", "section 9.2 Algorithms", learn, watch, explore, _pr, real, where, past, review,
  "Part 1 is real 9618 questions on stepwise refinement and describing algorithms (Paper 2), 2021 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", tips, js)
