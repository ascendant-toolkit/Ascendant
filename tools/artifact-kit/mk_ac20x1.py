"""20.2.2 extra resource: what an exception is and what causes it. Run: python3 tools/artifact-kit/mk_ac20x1.py"""
from ac20f import *

OLDQ = old_questions("mk_ac2022.py")
SUB2 = CBK("Chapter 20 · Further programming, section 20.2 File processing and exception handling")

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>An <b>exception</b> is an unexpected event that happens while a program is running and disrupts its normal flow of instructions. If nothing responds to it, the program <b>halts</b> at that line and the remaining statements never run. Exceptions have three common causes: <b>programming errors</b> (dividing by zero, using an index that does not exist), <b>user errors</b> (typing text where a number is needed, giving a file name that does not exist) and <b>hardware failure</b> (a disk crash, a printer or network connection lost). An exception is different from a <b>syntax error</b>, which is found before the program runs, and from a <b>logic error</b>, where the program runs but gives wrong results. Python gives each exception a name, such as <code>ZeroDivisionError</code>, and prints it with the line where it happened.</p></div>

  <h2>1 · What happens with no handling</h2>
  <p>This program divides 100 by a number the user types. The user types <b>0</b>.</p>
  ''' + both('''Number = int(input("Enter a number: "))
Result = 100 / Number
print(Result)
print("Finished")''', '''INPUT Number
Result <- 100 / Number
OUTPUT Result
OUTPUT "Finished"''') + '''
  <p>The first line works. The second line cannot be carried out, so an exception is raised and the program halts there. <code>Result</code> is never output and <code>Finished</code> is never printed. The user sees a system message instead.</p>

  <h2>2 · The three causes</h2>
  <div class="tw"><table class="t">
    <tr><th>Cause</th><th>Examples</th><th>Python exception</th></tr>
    <tr><td><b>Programming error</b></td><td>Divide by zero; an index outside the array; adding a string to a number</td><td><code>ZeroDivisionError</code>, <code>IndexError</code>, <code>TypeError</code></td></tr>
    <tr><td><b>User error</b></td><td>Typing <code>abc</code> where a number is expected; a file name that does not exist</td><td><code>ValueError</code>, <code>FileNotFoundError</code></td></tr>
    <tr><td><b>Hardware or system failure</b></td><td>A disk crash; the disk is full; the connection to a printer or network is lost</td><td><code>OSError</code></td></tr>
  </table></div>

  <h2>3 · Code that raises each one</h2>
  <div class="code">''' + pc('''print(100 / 0)                    # ZeroDivisionError: division by zero
Numbers = [4, 8, 15]
print(Numbers[5])                 # IndexError: list index out of range
Age = int("abc")                  # ValueError: invalid literal for int()
File = open("missing.txt", "r")   # FileNotFoundError: no such file
print("5" + 3)                    # TypeError: can only concatenate str to str''') + '''</div>

  <h2>4 · Reading the error message</h2>
  <div class="code">''' + pc('''Traceback (most recent call last):
  File "prog.py", line 2, in <module>
    Result = 100 / Number
ZeroDivisionError: division by zero''') + '''</div>
  <p>The last line is the exception and its reason. The line above shows the statement that caused it, and the line before that gives the line number.</p>

  <h2>5 · Exception, syntax error or logic error?</h2>
  <div class="tw"><table class="t">
    <tr><th></th><th>When it shows up</th><th>What happens</th><th>Example</th></tr>
    <tr><td><b>Syntax error</b></td><td>Before the program runs</td><td>The program will not start</td><td><code>print("Hi"</code> (missing bracket)</td></tr>
    <tr><td><b>Exception</b></td><td>While the program is running</td><td>The program halts unless it is handled</td><td><code>int("abc")</code></td></tr>
    <tr><td><b>Logic error</b></td><td>The program runs to the end</td><td>The output is wrong; nothing stops it</td><td>Average calculated as total × count</td></tr>
  </table></div>

  <h2>6 · Common ways to lose marks</h2>
  <ul>
    <li>Defining an exception as just "an error". Say it is an unexpected event during execution that disrupts the normal flow and can make the program halt.</li>
    <li>Giving a cause that is not one of the three, such as "the program is slow".</li>
    <li>Giving two examples of the same cause when two different causes are asked for.</li>
    <li>Describing a syntax error or a logic error as an exception.</li>
  </ul>
'''

watch = '''
  <h2>1 · A program with no handling halts</h2><p>Press Play, or click the steps. Both versions of the code are highlighted together.</p><div id="stA"></div>
  <h2>2 · Where exceptions come from</h2><div id="stB"></div>
  <h2>3 · Reading the error message</h2><div id="stC"></div>
'''

PS = ['INPUT Number', 'Result <- 100 / Number', 'OUTPUT Result', 'OUTPUT "Finished"']
PY = ['Number = int(input("Enter a number: "))', 'Result = 100 / Number', 'print(Result)', 'print("Finished")']
red = lambda s, y=0: (330, y, s, "lbl bd t2")
stA = stp("stA", "A program with no exception handling", [
    dict(c="A short program divides 100 by a number the user types. The user is going to type <b>0</b>.", p=-1, y=-1, v=[("Number", ""), ("Result", "")], f=[]),
    dict(c="The first line reads the input. <code>Number</code> is 0.", p=0, y=0, v=[("Number", "0"), ("Result", "")], f=[]),
    dict(c="<code>100 / Number</code> cannot be worked out. An exception is <b>raised</b>: ZeroDivisionError.", p=1, y=1, v=[("Number", "0"), ("Result", "")], f=[], t=[red("ZeroDivisionError: division by zero")]),
    dict(c="Nothing responds to it, so the program <b>halts</b>. The last two lines never run and the user sees a system error message.", p=-1, y=-1, v=[("Number", "0"), ("Result", "")], f=[], t=[red("Program halted at line 2"), (330, 30, "OUTPUT Result and OUTPUT \"Finished\" never run", "sm")])],
    PS, PY, lh=24, vw=150, fh=60)

cols = lambda n: [F(20, 20, "Programming error", ["divide by zero", "index out of range", "wrong data type"], w=220), F(260, 20, "User error", ["text for a number", "wrong file name", "empty input"], w=220), F(500, 20, "Hardware failure", ["disk crash", "disk full", "printer or network lost"], w=220)][:n]
stB = stp("stB", "The three causes of an exception", [
    dict(c="A program can run perfectly for years and still meet an exception. The cause is one of three kinds. First, <b>programming errors</b>: something the code asks for that cannot be done.", f=cols(1)),
    dict(c="Second, <b>user errors</b>: the user gives the program something it cannot use.", f=cols(2)),
    dict(c="Third, <b>hardware or system failure</b>: something outside the program stops working.", f=cols(3)),
    dict(c="In every case the program is stopped by an <b>unexpected event while it is running</b>. That is what makes it an exception, rather than a syntax error found before the program starts.", f=cols(3))],
    fh=125, dwell=3600)

TB = ['Traceback (most recent call last):', '  File "prog.py", line 2, in <module>', '    Result = 100 / Number', 'ZeroDivisionError: division by zero']
tf = lambda i: [F(20, 20, "What Python prints", TB, w=520, hl=i)]
stC = stp("stC", "Reading a Python error message", [
    dict(c="When an exception is not handled, Python prints a message like this and stops.", f=tf(None)),
    dict(c="The second line gives the <b>line number</b> in the program where it happened: line 2.", f=tf(1)),
    dict(c="The third line is the <b>statement</b> that raised the exception.", f=tf(2)),
    dict(c="The last line is the <b>name of the exception</b> and the reason: ZeroDivisionError, because the program divided by zero.", f=tf(3))],
    fh=135, dwell=3400)

explore = '''
  <h2>Lab 1 · Trigger an exception</h2>
  <p>Choose a statement to see what goes wrong, the name of the exception and the type of cause.</p>
  <div class="card"><div id="eB" class="btnrow"></div><div id="eO"></div></div>

  <h2>Lab 2 · Exception, syntax error or logic error?</h2>
  <div class="card"><div id="kB" class="btnrow"></div><div id="kO"></div></div>
'''

lab = r'''
btnTable("eB", "eO", [
  ["100 / 0", "print(100 / 0)", "A number cannot be divided by zero", "ZeroDivisionError", "Programming error"],
  ["List index", "Numbers = [4, 8, 15]; print(Numbers[5])", "The list has 3 items, so index 5 does not exist", "IndexError", "Programming error"],
  ["Text to number", "Age = int(\"abc\")", "\"abc\" cannot be turned into a whole number", "ValueError", "User error (typed input)"],
  ["Missing file", "open(\"missing.txt\", \"r\")", "No file with that name exists to open", "FileNotFoundError", "User error (wrong file name)"],
  ["Adding types", "print(\"5\" + 3)", "A string and a number cannot be added", "TypeError", "Programming error"],
  ["Disk full", "File.write(Line)  # no space left", "The device cannot store any more data", "OSError", "Hardware or system failure"]
], ["Statement", "Code", "What goes wrong", "Exception", "Cause"]);
btnTable("kB", "kO", [
  ["print(\"Hi\"", "print(\"Hi\"", "The bracket is never closed, so Python cannot read the line", "Syntax error", "Found before the program runs"],
  ["Average", "Average = Total * Count", "It runs, but should be Total / Count, so the answer is wrong", "Logic error", "The program does not stop"],
  ["int(\"abc\")", "Age = int(\"abc\")", "The program stops at this line while it is running", "Exception", "ValueError"],
  ["Wrong test", "IF Score > 50 THEN  (should be < 50)", "Runs to the end with the wrong result", "Logic error", "The program does not stop"],
  ["No file", "open(\"missing.txt\")", "The file is missing when the program tries to open it", "Exception", "FileNotFoundError"]
], ["Example", "Code", "What happens", "Kind", "Detail"]);
''' + CLASSIFY("cl1", "Which cause is this?", ["Programming error", "User error", "Hardware failure"],
    [("Dividing by a variable that is 0", 0), ("Using index 10 in a list of 5 items", 0), ("Typing a name where a number is asked for", 1), ("Giving the name of a file that does not exist", 1), ("A disk crash while saving", 2), ("The connection to a printer is lost", 2), ("Adding a string to an integer", 0), ("Leaving a required input empty", 1)],
    "Programming: the code asks for something impossible. User: bad input from the user. Hardware: something outside the program fails.") + ORDER(
    "Put these events in order when an exception is not handled.",
    ["The program is running normally", "A statement cannot be carried out", "An exception is raised", "The rest of the program is skipped", "The program halts and an error message is shown"],
    "Running, impossible statement, exception raised, rest skipped, halt and message.") + MATCH([
    ["Exception", "An unexpected event during execution that disrupts the normal flow"], ["Syntax error", "A mistake in the code found before the program runs"], ["Logic error", "The program runs but gives wrong results"], ["ZeroDivisionError", "Raised when a number is divided by zero"], ["IndexError", "Raised when an index does not exist in a list"], ["ValueError", "Raised when a value has the right type but cannot be used, such as int(\"abc\")"]]) + CALC([
    {"q": "A program runs print(\"A\"), then print(5 / 0), then print(\"B\") with no handling. How many lines of output does it produce before it halts?", "a": 1, "unit": "", "tol": 0.01, "hint": "Only the first print completes.", "sol": "<b>1</b> (A)."},
    {"q": "A list has 5 items numbered from 0. What is the highest index that does NOT raise an IndexError?", "a": 4, "unit": "", "tol": 0.01, "hint": "0, 1, 2, 3, 4.", "sol": "<b>4</b>."},
    {"q": "A loop converts 10 lines of a file with int() and has no handling. The fourth line is abc. How many numbers have been stored when the program halts?", "a": 3, "unit": "", "tol": 0.01, "hint": "Lines 1, 2 and 3 were fine.", "sol": "<b>3</b>."},
    {"q": "Of these four, how many are hardware or system failures: disk crash, wrong file name, divide by zero, printer disconnected?", "a": 2, "unit": "", "tol": 0.01, "hint": "Disk crash and printer disconnected.", "sol": "<b>2</b>."},
    {"q": "How many different causes of exceptions does the syllabus list (programming errors, user errors, ...)?", "a": 3, "unit": "", "tol": 0.01, "hint": "Programming, user, hardware.", "sol": "<b>3</b>."}]) + MCQ([
    ("What happens to the rest of a program when an unhandled exception is raised?", ["It carries on", "It is skipped and the program halts", "It runs twice", "It is deleted"], 1, "The program halts at that line."),
    ("Which is an exception rather than a syntax error?", ["A missing bracket", "Dividing by a variable that is 0 at run time", "A misspelt keyword", "A missing colon"], 1, "Exceptions happen while the program runs."),
    ("What does int(\"abc\") raise?", ["IndexError", "ZeroDivisionError", "ValueError", "OSError"], 2, "The text cannot be converted to a number."),
    ("A user types a file name that does not exist. This is mainly a...", ["Hardware failure", "User error", "Syntax error", "Logic error"], 1, "The user gave bad input."),
    ("A program runs to the end but the average is wrong. This is a...", ["Syntax error", "Logic error", "Exception", "Hardware failure"], 1, "The program does not stop; the result is wrong."),
    ("Which line of a Python error message names the exception?", ["The first", "The last", "The one with the line number", "There is no such line"], 1, "The last line gives the name and reason.")], "qz1") + CARDS([
    ("Exception", "An unexpected event during execution that disrupts normal flow."), ("Halt", "What an unhandled exception does to the program."), ("Programming error", "Divide by zero, index out of range."), ("User error", "Wrong input or wrong file name."),
    ("Hardware failure", "Disk crash, printer or network lost."), ("Syntax error", "Found before the program runs."), ("Logic error", "Runs, but gives wrong output."), ("Traceback", "Python's message: line number, statement, exception name.")])

real = RWNOTE + (
    rw("A web form quantity box", "A customer types ten instead of 10. Converting it to a number fails, which is a user error causing a ValueError.", "user error: text where a number is expected.") +
    rw("A spreadsheet with a moved file", "A linked file has been renamed. Opening it fails because it no longer exists under that name.", "user error: wrong or missing file name.") +
    rw("A game saving to a full disk", "There is no space left, so the write fails. The program did nothing wrong; the device could not cope.", "hardware or system failure.") +
    rw("An average of no values", "A program divides a total by the number of transactions. On a quiet day there are none, so it divides by zero.", "programming error: a case the code did not allow for.") +
    rw("A lost network connection", "A download stops when the Wi-Fi drops. The program cannot prevent this.", "failure outside the program's control."))

review = (
    req("2 marks", "Define", "Define the term <b>exception</b>.", "Unexpected, during execution, and the effect on the program.", mks(["An unexpected event that occurs while a program is running", "that disrupts the normal flow of instructions (and may cause the program to halt)"])) +
    req("2 marks", "State", "State two possible causes of an exception.", "Two different causes from the three.", mks(["A programming error (such as dividing by zero)", "A user error (such as a wrong file name) or hardware failure (such as a disk crash)"], "a")) +
    req("3 marks", "Classify", "For each event, say whether it is a programming error, a user error or a hardware failure: (a) dividing by zero in the code, (b) typing a file name that does not exist, (c) the disk failing while a file is saved.", "One mark each.", mks(["(a) programming error", "(b) user error", "(c) hardware failure"]) ) +
    req("2 marks", "Distinguish", "Distinguish between an exception and a syntax error.", "When each happens, and what happens next.", mks(["A syntax error is found before the program runs, so the program will not start", "An exception happens while the program is running and, if not handled, makes it halt"])) +
    req("3 marks", "Explain", "Explain what happens when an exception is raised in a program that has no exception handling.", "What stops, what is skipped, what the user sees.", mks(["The program halts at the statement that caused it", "the remaining statements are not executed", "a system error message is shown to the user"]), "Saying the program 'crashes' without saying that the later statements are skipped."))

where = [("O/N 2023", "31, 33", "8(b), 8(c)", "1 + 2", "Define exception handling; state two causes of an exception"),
         ("O/N 2023", "32", "12(a)", "2", "Describe, with an example, what is meant by an exception"),
         ("O/N 2025", "33", "12(a), 12(b)", "3 + 2", "Explain an exception; give an example and why it causes a problem")]
past = "".join(OLDQ[k] for k in ["O/N 2023 · 9618/31, 33 · Q8(b), (c)", "O/N 2023 · 9618/32 · Q12(a)", "O/N 2025 · 9618/33 · Q12"])
note = "These questions are reworded from the papers; check the original paper and mark scheme for the exact wording. What an exception is and what causes it is asked as a short Paper 3 theory question."

tipsl = [("Say 'unexpected'.", "An exception is an unexpected event during execution, not just an error."), ("Say what it does.", "It disrupts the normal flow and may make the program halt."), ("Give causes in three groups.", "Programming error, user error, hardware failure."), ("Different causes.", "If two causes are asked for, pick from two different groups."), ("Name an example with each.", "Divide by zero; wrong file name; disk crash."), ("Don't mix them up.", "Syntax errors are found before running; logic errors do not stop the program.")]
sents = [("Define an exception", "An exception is an unexpected event that occurs while a program is running and disrupts its normal flow."), ("Give an effect", "If it is not handled, the program halts and the remaining statements are not executed."), ("Give a cause", "A user error, such as entering the name of a file that does not exist, can cause an exception.")]
words = [("Define", "Give the meaning in one precise sentence."), ("State / Identify", "A fact, cause or example in a few words."), ("Describe / Explain", "Say what happens, with an example, and why it matters."), ("Distinguish", "Give a difference between the two, not a description of each.")]

finishf("ac20x1", "ac-20-2-2-what-is-an-exception", "What an Exception Is and What Causes It",
        "Defining an exception, what happens when one is not handled, the three causes with Python examples, and how an exception differs from a syntax or logic error; pseudocode and Python side by side, with step-by-step animations.",
        learn, watch, explore, practise("cl", "o", "m", "c", "q"), real, review, tipsl, sents, stA + stB + stC + lab, where, past, note, words, sub_num="20.2.2")
