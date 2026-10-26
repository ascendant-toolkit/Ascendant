"""A Level CS syllabus 20.2.2: exception handling. Run: python3 tools/artifact-kit/mk_ac2022.py"""
from ak20 import *

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>An <b>exception</b> is an unexpected event that happens while a program is running and disrupts its normal flow, and unless something responds to it the program <b>halts</b>. <b>Exception handling</b> is the process of responding to the unwanted event so the program does not stop unexpectedly: the risky statements go in a <code>try</code> block and the response goes in an <code>except</code> block. Exceptions have three common causes: <b>programming errors</b> (dividing by zero, an index outside an array), <b>user errors</b> (typing text where a number is expected, a wrong file name) and <b>hardware failure</b> (a disk crash, a lost connection to a printer). Use exception handling when something outside the program's control could go wrong, especially opening and reading files and converting user input. Paper 3 asks you to define and describe it; Paper 4 awards marks for writing it round a file.</p></div>

  <h2>1 · What an exception is</h2>
  <div class="tw"><table class="t">
    <tr><th>Cause</th><th>Example</th><th>Python exception</th></tr>
    <tr><td><b>Programming error</b></td><td>Divide by zero; read an array element that does not exist; a variable of the wrong type</td><td><code>ZeroDivisionError</code>, <code>IndexError</code>, <code>TypeError</code></td></tr>
    <tr><td><b>User error</b></td><td>Typing <code>abc</code> when a number is asked for; giving a file name that does not exist</td><td><code>ValueError</code>, <code>FileNotFoundError</code></td></tr>
    <tr><td><b>Hardware or system failure</b></td><td>A disk crash; the file is on a device that has been unplugged; the disk is full; a printer is disconnected</td><td><code>OSError</code> (which <code>IOError</code> is an alias of)</td></tr>
  </table></div>
  <p>Without handling, Python stops at the line where it happened and prints an error message. Statements after it never run, and files may be left open.</p>

  <h2>2 · Why use exception handling?</h2>
  <ul>
    <li>To <b>trap runtime errors</b> and stop the program halting unexpectedly.</li>
    <li>To <b>show a meaningful message</b> to the user instead of a system error.</li>
    <li>To let the program <b>recover or carry on</b>: ask again, use a default, or close down safely.</li>
  </ul>
  <p>The mark scheme's wording: <i>exception handling is a process that responds to unwanted or unexpected events when a program runs, to prevent the program or computer from stopping unexpectedly.</i></p>

  <h2>3 · try and except in Python</h2>
  <div class="code">''' + pc('''try:
    File = open("Data.txt", "r")          # might fail: file missing
    for Line in File:
        Numbers.append(int(Line))         # might fail: a line is not a number
    File.close()
except IOError:                           # the response when the file cannot be opened
    print("Could not find the file")
except ValueError:                        # the response when int() fails
    print("The file contains something that is not a number")''') + '''</div>
  <ol>
    <li>Python runs the statements in the <b><code>try</code></b> block.</li>
    <li>If one of them causes an exception, the rest of the block is <b>skipped</b> and the matching <b><code>except</code></b> block runs.</li>
    <li>If nothing goes wrong, the <code>except</code> blocks are skipped.</li>
    <li>The program then carries on after the whole <code>try</code> statement.</li>
  </ol>
  <div class="tw"><table class="t">
    <tr><th>Part</th><th>Use</th></tr>
    <tr><td><code>try:</code></td><td>The statements that might cause the exception</td></tr>
    <tr><td><code>except IOError:</code> / <code>except:</code></td><td>What to do if it happens. Naming the exception is best; a bare <code>except:</code> catches everything and is accepted in the exam</td></tr>
    <tr><td><code>else:</code></td><td>Runs only if no exception happened</td></tr>
    <tr><td><code>finally:</code></td><td>Runs whether or not an exception happened, for example to close a file</td></tr>
  </table></div>
  <p>The syllabus pseudocode form is the same idea:</p>
  <pre class="plain">TRY
   OPENFILE "Data.txt" FOR READ
   READFILE "Data.txt", Line
EXCEPT
   OUTPUT "File not found"
FINALLY
   CLOSEFILE "Data.txt"
ENDTRY</pre>

  <h2>4 · When to use it</h2>
  <div class="tw"><table class="t">
    <tr><th>Use exception handling for</th><th>Use ordinary checks (IF, validation) for</th></tr>
    <tr><td>Opening, reading and writing files</td><td>A value that must be in a range: <code>IF Age &lt; 0 THEN</code></td></tr>
    <tr><td>Converting user input: <code>int(input())</code></td><td>A list index you can test with <code>IF Index &lt; len(List)</code></td></tr>
    <tr><td>Network, printer or disk problems</td><td>Menu choices from a known set</td></tr>
    <tr><td>Division where the divisor comes from the user</td><td>Logic errors in your own algorithm (fix the code)</td></tr>
  </table></div>
  <p>Use it where the problem comes from <b>outside the program</b> and cannot be ruled out in advance. It does not replace validation, and it does not fix a logic error.</p>

  <h2>5 · Patterns the exams use</h2>
  <div class="code">''' + pc('''# 1. Reading a file: the paper says "use exception handling when opening and reading"
def LoadAvatars():
    global AvailableAvatars
    try:
        TheFile = open("AvatarFile.txt")
        for Line in TheFile:
            Data = Line.strip().split(" ")
            AvailableAvatars.append(Avatar(Data[0], Data[1] == "True", Data[2], int(Data[3])))
        TheFile.close()
    except:
        print("File not found")

# 2. Writing a file
try:
    File = open("Tree.txt", "w")
    File.write("-1,20,1\\n")
    File.close()
except:
    print("Cannot write to file")

# 3. Input: ask again until it is valid
Valid = False
while not Valid:
    try:
        Age = int(input("Enter your age: "))
        Valid = True
    except ValueError:
        print("Please enter a whole number")''') + '''</div>
  <p>The mark scheme awards separate marks for: the <b>try</b> structure, the <b>except</b> (catch) block, an <b>appropriate output message</b>, and for the file work inside it (open, loop, read, close).</p>

  <h2>6 · Common ways to lose marks</h2>
  <ul>
    <li>Defining an exception as "an error". Say it is an unexpected event during execution that can make the program halt.</li>
    <li>Listing a cause that is not an exception cause (for example "the program is slow"). Use programming errors, user errors or hardware failure.</li>
    <li>Writing <code>try</code> without <code>except</code>, or an <code>except</code> with no message or action.</li>
    <li>Putting <code>try</code> round the wrong lines: the file opening and reading must be <i>inside</i> it.</li>
    <li>Describing validation (an <code>IF</code> check) as exception handling.</li>
    <li>In Paper 4, leaving out the exception handling when the question says "use exception handling". It is usually worth a mark or two.</li>
  </ul>
'''

watch = '''
  <h2>1 · Without handling, the program halts</h2>
  <p>Press Play, or click the steps. The same program runs with a bad input, first with no handling and then with try and except.</p>
  <div id="stA"></div>
  <h2>2 · With try and except, the program carries on</h2>
  <div id="stB"></div>
  <h2>3 · Which except block runs?</h2>
  <div id="stC"></div>
  <h2>4 · finally always runs</h2>
  <div id="stD"></div>
'''

explore = '''
  <h2>Lab 1 · Run the program</h2>
  <p>The program asks for a file name, reads a number from the first line and divides 100 by it. Choose the situation, then turn exception handling on or off.</p>
  <div class="card"><div id="sB" class="btnrow"></div><div class="btnrow"><button class="b" id="sT">Exception handling: off</button></div><div id="sC"></div><div class="verdict" id="sV"></div></div>

  <h2>Lab 2 · Which exception, which cause?</h2>
  <p>Choose a situation to see the exception, the type of cause and the handler.</p>
  <div class="card"><div id="eB" class="btnrow"></div><div id="eO"></div></div>

  <h2>Lab 3 · Mistakes in exception handling</h2>
  <div class="card"><div id="mB" class="btnrow"></div><div id="mO"></div></div>
'''

practise = '''
  <h2>1 · What kind of cause is it?</h2><div id="cl1" class="card"></div>
  <h2>2 · Exception handling or an ordinary check?</h2><div id="cl2" class="card"></div>
  <h2>3 · Put the steps of try and except in order</h2><div id="o1" class="card"></div>
  <h2>4 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>5 · What is output?</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("A web form that asks for a quantity", "If a customer types ten instead of 10, converting it to a number would normally crash the page. The code catches the error and shows 'Please enter a whole number'.", "user error handled by an exception handler with a helpful message.") +
rw("A spreadsheet opening a missing file", "When a linked file has been moved or deleted, the program says it cannot find the file and offers to browse for it instead of closing.", "file not found: caught so the program can carry on.") +
rw("A game saving to a full disk", "If there is no space left, the save fails. The game reports it and keeps running so the player does not lose their progress in memory.", "hardware or system failure: the response protects the data.") +
rw("A banking program dividing by a count", "An average is total divided by the number of transactions. With no transactions that would divide by zero, so the program handles it and reports 'no transactions'.", "a programming error that can be caught (or checked first with IF).") +
rw("An app losing its network connection", "A download stops when the Wi-Fi drops. The app catches the connection error, tells the user, and lets them retry.", "failure outside the program's control, reported rather than crashing.")
)

where = [
  ("M/J 2022", "32", "9", "4", "State the reasons for including exception handling, with an example"),
  ("O/N 2023", "31, 33", "8(b), 8(c)", "1 + 2", "Define exception handling; state two causes of an exception"),
  ("O/N 2023", "32", "12(a)", "2", "Describe, with an example, what is meant by an exception"),
  ("O/N 2025", "31", "10", "3", "Explain exception handling with an example of a cause"),
  ("O/N 2025", "32", "10(a), 10(b)", "2 + 2", "Describe how termination due to an exception is avoided; identify two causes"),
  ("O/N 2025", "33", "12(a), 12(b)", "3 + 2", "Explain an exception; give an example and why it causes a problem"),
  ("O/N 2022", "41, 43", "1(b)", "6", "ReadFile(): read 100 integers from IntegerData.txt with exception handling"),
  ("M/J 2023", "41, 43", "1(a)(ii)", "4", "Read 25 integers from Data.txt into an array with exception handling"),
  ("O/N 2025", "42", "3(c)", "4", "Read 50 integers from TreeData.txt into a binary tree, with exception handling"),
  ("M/J 2026", "42", "2(b)", "7 + 1", "LoadAvatars(): read objects from AvatarFile.txt with exception handling")]

past = '''  <p class="note">Exception handling is tested in Paper 3 as a short theory question (definition, causes, why) in May/June 2022, Oct/Nov 2023 and Oct/Nov 2025. In Paper 4 it is a mark inside the file questions, and appears in most papers; four are shown here and the rest are on the previous page. Python is shown for Paper 4. Questions are reworded from the papers; check the original paper and mark scheme for the exact wording.</p>

  <h3>Paper 3: define, describe and explain</h3>
''' + peq(SRC("s22", "32", "Q9"), "4 marks", "State",
  "State the reasons for including exception handling routines when writing a program. Include an example of an exception in your answer.",
  "Reasons: trap errors, stop the halt, give a helpful message. One mark for an example.",
  "<p>" + mks(["To trap (some) runtime errors", "To prevent a program halting unexpectedly", "To produce meaningful error messages for these errors", "Example: divide by zero / end of file / file not found"]) + "</p>",
  "Giving only the example. The question asks for the reasons as well.") + peq(SRC("w23", "31, 33", "Q8(b), (c)"), "1 + 2 marks", "Define / State",
  "(b) Define the term exception handling. (c) State two possible causes of an exception.",
  "(b) A response to an unexpected event so the program does not halt. (c) Two of programming, user and hardware.",
  "<p><b>(b)</b> " + mks(["(Exception handling is the process of) responding to an unexpected event when the program is running so it does not halt unexpectedly"]) + " <b>(c)</b> " + mks(["Programming errors", "User errors / hardware failure / runtime errors"], "a") + "</p>",
  "Defining it as 'catching errors' without saying the program must not halt unexpectedly.") + peq(SRC("w23", "32", "Q12(a)"), "2 marks", "Describe",
  "Describe, with an example, what is meant by an exception.",
  "One mark for the description and one for the example.",
  "<p>" + mks(["An exception is an event that occurs during the execution of a program that disrupts the normal flow of instructions / causes the program to halt", "Example: hardware failure, a programming error such as an out-of-bounds array element or divide by zero, or a user error such as a wrong file name"]) + "</p>", None) + peq(SRC("w25", "31", "Q10"), "3 marks", "Explain",
  "Explain what is meant by exception handling. Include an example of a possible cause of an exception in your answer.",
  "Two marks for the explanation, one for the cause.",
  "<p>" + mks(["Exception handling is a process that responds to unwanted / unexpected events when a program runs", "to prevent the program / computer from stopping unexpectedly", "Cause: programming errors, user errors or hardware failure (such as losing the connection to a printer)"]) + "</p>", None) + peq(SRC("w25", "32", "Q10"), "2 + 2 marks", "Describe / Identify",
  "An exception is an error that may cause a program to halt unexpectedly. (a) Describe how program termination due to an exception can be avoided. (b) Identify two possible causes of exceptions.",
  "(a) use an exception handling routine, and name try ... except or an error message.",
  "<p><b>(a)</b> " + mks(["Use an exception handling routine (to respond to unwanted / unexpected events while the program runs)", "using try ... except / catch, or by generating an error message"]) + " <b>(b)</b> " + mks(["Coding errors", "User errors / hardware failure"], "a") + "</p>", None) + peq(SRC("w25", "33", "Q12"), "3 + 2 marks", "Explain / Identify",
  "An exception can occur when running a program. (a) Explain what is meant by an exception. (b) Identify one example of an exception and give one reason why the exception may cause a problem.",
  "(a) unexpected event at run time, caused by something not detected earlier, and the effect. (b) one example and its consequence.",
  "<p><b>(a)</b> " + mks(["An unplanned / unexpected event that occurs when a program is running", "due to an error in the programming or logic that was not detected during construction or compilation", "The effect can be that the program halts unexpectedly"]) + "</p><p><b>(b)</b> " + mks(["Example: division by zero", "Reason: the processor cannot evaluate the answer, so the program cannot continue"], "a") + "</p>", None) + '''
  <h3>Paper 4: exception handling inside file questions (Python)</h3>
''' + peq(SRC("w22", "41, 43", "Q1(b)"), "6 marks", "Write",
  "The text file IntegerData.txt stores 100 integer numbers between 1 and 100 inclusive, one on each line. The procedure ReadFile() must read in the numbers from the text file and store each one in the global array DataArray, which has space for 100 integers. Use appropriate exception handling. Write program code for the procedure ReadFile().",
  "Header, open to read, loop 100 times or to the end of the file, convert and store each value, close, and try and except with a message.",
  "<p>Marks: " + mks(["procedure ReadFile() header", "opening IntegerData.txt for read", "looping through the 100 elements / to the end of the file", "reading each value from the file and storing it in the array", "closing the file in an appropriate place", "exception handling round the file opening or reading, with an appropriate message"]) + "</p>" + pc('''def ReadFile():
    global DataArray
    try:
        File = open("IntegerData.txt", "r")
        for X in range(0, 100):
            DataArray[X] = int(File.readline())
        File.close()
    except IOError:
        print("Could not find the file")'''),
  "Putting the <code>try</code> only round the <code>open</code>, so an error while reading is not caught, or leaving out the message in the <code>except</code> block.") + peq(SRC("s23", "41, 43", "Q1(a)"), "1 + 4 marks", "Write",
  "A program reads data from a file and searches for specific data. (a)(i) Write program code to declare the local 1D array DataArray, which holds 25 integers. (ii) Amend the main program to read the 25 integer data items from the text file Data.txt into DataArray.",
  "Open for reading, loop through the lines, append each as an integer, close, and handle the missing file.",
  "<p><b>(i)</b> " + mks(["1D array named DataArray (with 25 elements of type integer)"]) + "</p>" + pc('''DataArray = []    # 25 elements of type integer''') + "<p><b>(ii)</b> Four marks: " + mks(["opening Data.txt to read", "looping through all 25 / to the end of the file, reading each line and appending it to the array", "exception handling with an appropriate output", "closing the file (in an appropriate place)"], "a") + "</p>" + pc('''try:
    DataFile = open("Data.txt", "r")
    for Line in DataFile:
        DataArray.append(int(Line))
    DataFile.close()
except IOError:
    print("Could not find file")''', 2),
  "Appending the line as a string. The array holds integers, so convert with <code>int()</code>.") + peq(SRC("w25", "42", "Q3(c)"), "4 marks", "Write",
  "The text file TreeData.txt stores 50 integers, one on each line. The main program reads each integer from the file and stores it in the binary tree in the order read, using the procedure AddNode() (which takes the integer as its parameter). Write program code for the main program. Use exception handling.",
  "Open, loop through the lines, call AddNode() with each integer, close, and try and except.",
  "<p>" + mks(["opening the file to read, and closing it in an appropriate place", "looping 50 times / through the file / until the end of the file, reading each line", "calling AddNode() with each value read", "exception handling (try ... except) with an appropriate message"]) + "</p>" + pc('''try:
    File = open("TreeData.txt")
    for Line in File:
        AddNode(int(Line.strip()))
    File.close()
except:
    print("Error: cannot open file")'''),
  "Reading the lines but never calling AddNode(), or reading a string instead of converting to an integer.") + peq(SRC("s26", "42", "Q2(b)"), "7 + 1 marks", "Write",
  "The text file AvatarFile.txt stores data for 30 avatars. Each avatar is on a new line, in the order: name, glasses, hair colour, age, with each value separated by a space. For example, the first line is <code>Kit True blonde 21</code>. The class Avatar has a constructor that takes the name, a Boolean for glasses, the hair colour and the age. (i) The procedure LoadAvatars() reads the data from the text file, creates a new object for each avatar and stores the objects in a global array AvailableAvatars. The procedure uses exception handling when opening and reading from the file. Write program code for LoadAvatars(). (ii) Write the main program to call LoadAvatars().",
  "Split each line on spaces, convert the glasses text and the age, create an Avatar and store it. Everything that touches the file is inside the try.",
  "<p><b>(i)</b> Seven marks: " + mks(["procedure header and appropriate exception handling with output", "opening the text file (to read) and closing it", "looping until the end of the file / 30 times", "reading in each line", "splitting each line by space", "creating an object with the correct values", "storing each object in the global array"]) + "</p>" + pc('''def LoadAvatars():
    global AvailableAvatars
    try:
        TheFile = open("AvatarFile.txt")
        for Line in TheFile:
            DataSplit = Line.strip().split(" ")
            Glasses = DataSplit[1] == "True"
            AvailableAvatars.append(Avatar(DataSplit[0], Glasses, DataSplit[2], int(DataSplit[3])))
        TheFile.close()
    except:
        print("File not found")''') + "<p><b>(ii)</b> " + mks(["LoadAvatars()"], "a") + "</p>" + pc('''LoadAvatars()''', 14),
  "Treating the glasses value <code>\"True\"</code> as a Boolean directly. A string from a file is always a string: compare it to <code>\"True\"</code>.")

review = req("2 marks", "Distinguish", "Distinguish between an exception and a logic error.", "One happens when something unexpected occurs at run time; the other is a mistake in the algorithm.",
  "<p>" + mks(["An exception is an unexpected event during execution (such as a missing file) that disrupts the program and can be handled.", "A logic error is a mistake in the program's design that gives wrong results without stopping it; it has to be fixed in the code."]) + "</p>", None) + req("3 marks", "Write", "Write Python that asks the user for a whole number and keeps asking until a whole number is entered.", "Loop, try int(input()), catch ValueError.",
  "<p>" + mks(["a loop that repeats until the input is valid", "try ... int(input(...)) so conversion is inside the try", "except ValueError with a message, and the loop continuing"]) + "</p>" + pc('''Valid = False
while not Valid:
    try:
        Number = int(input("Enter a whole number: "))
        Valid = True
    except ValueError:
        print("That was not a whole number")'''), "Setting <code>Valid = True</code> before the conversion, so a bad input ends the loop.") + req("2 marks", "State", "Name two possible causes of an exception when a program reads a file.", "Think user and hardware.",
  "<p>" + mks(["The file does not exist or the wrong file name was given (user error).", "The disk or device fails or the file is corrupted (hardware failure)."]) + "</p>", None) + req("3 marks", "Complete", "The code below crashes when the user enters 0. Rewrite it so that it outputs 'Cannot divide by zero' instead." + qcode('''Number = int(input("Enter a number: "))
print(100 / Number)'''), "The risky statement goes in the try; the response goes in the except.",
  "<p>" + mks(["try block round the division (and the input)", "except ZeroDivisionError (or a general except)", "OUTPUT of the message 'Cannot divide by zero'"]) + "</p>" + pc('''try:
    Number = int(input("Enter a number: "))
    print(100 / Number)
except ZeroDivisionError:
    print("Cannot divide by zero")'''), None) + req("2 marks", "Explain", "Explain why checking a file exists with an IF statement is not always enough, and why exception handling is used as well.", "Think of what can go wrong after the check.",
  "<p>" + mks(["The file may be removed, locked or damaged between the check and the open, or fail part-way through reading.", "Exception handling responds to the problem whenever it occurs, so the program does not halt."]) + "</p>", None)

exam = exam20("Part 1 is real 9618 questions on exceptions and exception handling: the Paper 3 theory questions and four Paper 4 questions where exception handling is part of the marks. Part 2 is a set of review questions for practice; they are not in exam format.", where, past, review)

tips = tips_html([
  ("Define it fully.", "An exception is an unexpected event during execution that disrupts normal flow and can make the program halt. Exception handling responds to it so the program does not stop unexpectedly."),
  ("Give causes in three groups.", "Programming errors, user errors, hardware failure. Name one example of each."),
  ("Put the risky code inside try.", "File opening, reading and converting input all go in the try block."),
  ("Always add a message.", "An except block that does nothing gets no mark. Output an appropriate message."),
  ("Handle what is outside your control.", "Files, input, devices. Use IF for ranges and logic."),
  ("Read the question for 'use exception handling'.", "It is a separate mark in Paper 4 file questions."),
], [
  ("what exception handling does", "It responds to an unexpected event while the program is running so the program does not halt unexpectedly."),
  ("a cause of an exception", "A user error, such as entering a file name that does not exist."),
  ("how to avoid termination", "Use a try ... except block with an appropriate message."),
  ("why use it", "To trap runtime errors, prevent the program halting and give a meaningful message."),
], [("Define", "Give the exact meaning in one sentence."), ("State / Identify", "Give a fact, cause or example in a few words."), ("Describe / Explain", "Say what happens and why, with an example."), ("Write program code", "Python with try, except and a message.")]) + FC

js = AKJS + AK20JS + r'''
(function () {
  const L = ["Number = int(input(\"Enter a number: \"))", "Result = 100 / Number", "print(Result)", "print(\"Finished\")"];
  const draw = (s) => {
    const k = Math.round(s.i); let o = codeList(20, 20, L, k === 0 ? -1 : k === 1 ? 0 : k >= 2 ? 1 : -1, 1, 36, 410);
    o += SV.text(450, 40, "Input: 0", "lbl bd", { style: "font-family:var(--mono);font-size:16px" });
    if (k >= 2) o += SV.rect(450, 70, 290, 80, "cell-no", { rx: 8 }) + SV.text(464, 98, "ZeroDivisionError", "lbl bd t2", { style: "font-family:var(--mono);font-size:15px" }) + SV.text(464, 124, "program halts here", "lbl");
    if (k >= 3) o += SV.text(20, 190, "print(Result) and print(\"Finished\") never run", "lbl bd t2");
    return o;
  };
  Lib.stepper($("#stA"), { w: 760, h: 215, label: "A program with no exception handling", base: { i: 0 }, draw, tween: 300, dwell: 2800, steps: [
    { cap: "A short program that divides 100 by a number the user types. The user types <b>0</b>.", s: { i: 0 } },
    { cap: "Line 1 works: Number = 0.", s: { i: 1 } },
    { cap: "Line 2 divides 100 by 0. That is impossible, so Python raises a <b>ZeroDivisionError</b> exception. With nothing to respond to it, the program <b>halts</b>.", s: { i: 2 } },
    { cap: "The remaining lines never run, and the user sees a system error. That is the unexpected halt that exception handling prevents.", s: { i: 3 } }] });
})();

(function () {
  const L = ["try:", "    Number = int(input(\"Enter a number: \"))", "    print(100 / Number)", "except ZeroDivisionError:", "    print(\"Cannot divide by zero\")", "print(\"Finished\")"];
  const draw = (s) => {
    const k = Math.round(s.i); const hl = [-1, 1, 2, 3, 4, 5][k]; let o = codeList(20, 10, L, hl, 1, 34, 420);
    o += SV.text(470, 36, "Input: 0", "lbl bd", { style: "font-family:var(--mono);font-size:16px" });
    if (k >= 2) o += SV.rect(470, 56, 270, 64, "cell-no", { rx: 8 }) + SV.text(484, 84, "ZeroDivisionError", "lbl bd t2", { style: "font-family:var(--mono);font-size:14px" }) + SV.text(484, 106, "jump to the matching except", "sm");
    if (k >= 4) o += SV.rect(470, 130, 270, 40, "cell-ok", { rx: 8 }) + SV.text(484, 156, "Cannot divide by zero", "lbl bd t3", { style: "font-family:var(--mono);font-size:14px" });
    if (k >= 5) o += SV.rect(470, 178, 270, 36, "cell-ok", { rx: 8 }) + SV.text(484, 202, "Finished", "lbl bd t3", { style: "font-family:var(--mono);font-size:14px" });
    return o;
  };
  Lib.stepper($("#stB"), { w: 760, h: 235, label: "The same program with try and except", base: { i: 0 }, draw, tween: 300, dwell: 2800, steps: [
    { cap: "The risky lines are placed in a <code>try</code> block, followed by an <code>except</code> block that says what to do.", s: { i: 0 } },
    { cap: "The try block starts: the user types 0 and <code>Number</code> is 0.", s: { i: 1 } },
    { cap: "<code>100 / Number</code> raises <b>ZeroDivisionError</b>. The rest of the try block is skipped.", s: { i: 2 } },
    { cap: "Python looks for an <code>except</code> that matches and finds <code>except ZeroDivisionError</code>.", s: { i: 3 } },
    { cap: "The handler runs and the user sees a meaningful message, not a system error.", s: { i: 4 } },
    { cap: "The program <b>carries on</b> after the try statement and prints Finished. It did not halt unexpectedly.", s: { i: 5 } }] });
})();

(function () {
  const cases = [["abc", "ValueError", "int(\"abc\") fails: the text is not a number", "Please enter a whole number"], ["0", "ZeroDivisionError", "100 / 0 is impossible", "Cannot divide by zero"], ["4", "(none)", "everything works: 100 / 4", "25.0"]];
  const draw = (s) => {
    const k = Math.round(s.i); const c = cases[Math.max(0, k - 1)]; let o = SV.text(20, 26, "try:  Number = int(input(...));  print(100 / Number)", "lbl bd", { style: "font-family:var(--mono);font-size:14px" });
    o += SV.rect(20, 50, 400, 44, k === 1 ? "cell-warn" : "cell", { rx: 6 }) + SV.text(34, 78, "except ValueError:  \"Please enter a whole number\"", "lbl", { style: "font-family:var(--mono);font-size:12px" });
    o += SV.rect(20, 104, 400, 44, k === 2 ? "cell-warn" : "cell", { rx: 6 }) + SV.text(34, 132, "except ZeroDivisionError:  \"Cannot divide by zero\"", "lbl", { style: "font-family:var(--mono);font-size:12px" });
    if (k >= 1) o += SV.text(440, 70, "User types: " + c[0], "lbl bd", { style: "font-family:var(--mono);font-size:15px" }) + SV.text(440, 100, "Exception: " + c[1], "lbl bd " + (k === 3 ? "t3" : "t2"), { style: "font-family:var(--mono);font-size:14px" }) + SV.text(440, 128, c[2], "sm", { style: "font-size:11px" }) + SV.text(440, 160, "Output: " + c[3], "lbl bd t3", { style: "font-family:var(--mono);font-size:13px" });
    return o;
  };
  Lib.stepper($("#stC"), { w: 760, h: 190, label: "Several except blocks", base: { i: 0 }, draw, tween: 250, dwell: 3000, steps: [
    { cap: "Different problems can have different responses: one <code>except</code> for each exception type.", s: { i: 0 } },
    { cap: "The user types <b>abc</b>. <code>int()</code> raises a <b>ValueError</b>, so that handler runs.", s: { i: 1 } },
    { cap: "The user types <b>0</b>. The division raises <b>ZeroDivisionError</b>, so the other handler runs.", s: { i: 2 } },
    { cap: "The user types <b>4</b>. No exception happens, so no except block runs and the answer is printed.", s: { i: 3 } }] });
})();

(function () {
  const L = ["try:", "    File = open(\"Data.txt\")", "    Line = File.readline()", "except IOError:", "    print(\"Problem with the file\")", "finally:", "    print(\"Done\")"];
  const draw = (s) => {
    const k = Math.round(s.i); const hl = [-1, 1, 3, 4, 5, 6][k]; let o = codeList(20, 10, L, hl, 1, 34, 360);
    if (k >= 2) o += SV.rect(420, 40, 310, 40, "cell-no", { rx: 8 }) + SV.text(434, 66, "IOError: file not found", "lbl bd t2", { style: "font-family:var(--mono);font-size:14px" });
    if (k >= 3) o += SV.rect(420, 92, 310, 40, "cell-ok", { rx: 8 }) + SV.text(434, 118, "Problem with the file", "lbl bd t3", { style: "font-family:var(--mono);font-size:14px" });
    if (k >= 5) o += SV.rect(420, 144, 310, 40, "cell-ok", { rx: 8 }) + SV.text(434, 170, "Done  (always runs)", "lbl bd t3", { style: "font-family:var(--mono);font-size:14px" });
    return o;
  };
  Lib.stepper($("#stD"), { w: 760, h: 255, label: "The finally block", base: { i: 0 }, draw, tween: 250, dwell: 2800, steps: [
    { cap: "A <code>finally</code> block runs <b>whether or not</b> an exception happened. It is used for clean-up, such as closing a file.", s: { i: 0 } },
    { cap: "The file cannot be opened.", s: { i: 1 } },
    { cap: "An IOError is raised, so the try block stops and the matching except runs.", s: { i: 2 } },
    { cap: "The except block outputs its message.", s: { i: 3 } },
    { cap: "Then the <code>finally</code> block.", s: { i: 4 } },
    { cap: "It would also have run if the file had opened without error. The mark scheme does not require <code>finally</code>, but it is a correct use.", s: { i: 5 } }] });
})();

/* Lab 1 */
(function () {
  let sit = 0, on = false;
  const sits = [["File exists, first line 5", "5"], ["File exists, first line is the word five", "five"], ["File exists, first line 0", "0"], ["File does not exist", ""]];
  const run = () => {
    const s = sits[sit], out = []; let halted = null;
    try {
      if (sit === 3) throw ["FileNotFoundError", "Could not find the file"];
      const v = s[1]; if (isNaN(parseInt(v, 10)) || !/^-?\d+$/.test(v)) throw ["ValueError", "The file does not hold a number"];
      if (+v === 0) throw ["ZeroDivisionError", "Cannot divide by zero"];
      out.push("100 / " + v + " = " + 100 / +v);
    } catch (e) { if (on) out.push(e[1]); else { halted = e[0]; } }
    return { out, halted };
  };
  const paint = () => {
    $$("#sB button").forEach((b, i) => b.classList.toggle("pri", i === sit)); $("#sT").textContent = "Exception handling: " + (on ? "on" : "off"); $("#sT").classList.toggle("pri", on);
    const r = run(), code = ['File = open("Data.txt")', "Number = int(File.readline())", "print(100 / Number)"];
    const lines = on ? ["try:", ...code.map((c) => "    " + c), "except:", '    print("An error occurred")'] : code;
    $("#sC").innerHTML = '<div class="code"><pre class="cp">' + lines.map((l) => `<span class="ln">${l.replace(/&/g, "&amp;").replace(/</g, "&lt;")}</span>`).join("") + "</pre></div>";
    $("#sV").innerHTML = r.halted ? "<b>Output:</b> the program <b>halts</b> with " + r.halted + ". Nothing after the error runs." : "<b>Output:</b> " + r.out.join("<br>") + (on && !/^100/.test(r.out[0] || "") ? "<br>The program carries on after the try statement." : "");
  };
  $("#sB").innerHTML = sits.map((s, i) => `<button class="b" data-i="${i}">${s[0]}</button>`).join("");
  $$("#sB button").forEach((b) => (b.onclick = () => { sit = +b.dataset.i; paint(); })); $("#sT").onclick = () => { on = !on; paint(); };
  paint();
})();

btnTable("eB", "eO", [
  ["User types text for a number", "ValueError", "User error", "except ValueError: print(\"Please enter a whole number\")"],
  ["Divide by a zero entered by the user", "ZeroDivisionError", "User error shown as a programming error", "except ZeroDivisionError: print(\"Cannot divide by zero\")"],
  ["Open a file that does not exist", "FileNotFoundError (an IOError)", "User error (wrong name) or system error", "except IOError: print(\"File not found\")"],
  ["Read element 10 of a list of 5", "IndexError", "Programming error", "Check the index with IF, or except IndexError"],
  ["Disk full while saving", "OSError", "Hardware / system failure", "except OSError: print(\"Cannot save\")"],
  ["Add a string to an integer", "TypeError", "Programming error", "Fix the code: convert with str() or int()"]
], ["Situation", "Exception", "Type of cause", "Handler"]);

(function () {
  const rows = [
    ["try with no except", "try:\n    File = open(\"Data.txt\")", "A SyntaxError: a try needs at least one except (or finally)", "Add except IOError: with a message"],
    ["Empty except", "except:\n    pass", "The error is hidden, nothing is shown to the user, and no mark for a message", "print(\"File not found\")"],
    ["Open outside the try", "File = open(\"Data.txt\")\ntry:\n    ...", "The most likely failure is not protected, so the program can still halt", "Put the open inside the try"],
    ["Using try for a range check", "try:\n    Age = int(Age)\nexcept:\n    print(\"Too old\")", "A value that is too large is not an exception: it needs IF", "IF Age > 120 THEN"],
    ["Closing the file only in the try", "try:\n    File = open(...)\n    ...\n    File.close()", "If an error happens, the file is not closed; use finally or close it as well", "finally: File.close()"]
  ];
  const paint = (i) => { $$("#mB button").forEach((b, k) => b.classList.toggle("pri", k === i)); const r = rows[i]; $("#mO").innerHTML = '<div class="tw"><table class="t"><tr><th>Mistake</th><th>What goes wrong</th><th>Fix</th></tr><tr><td><b>' + r[0] + "</b><pre class=\"plain\">" + r[1].replace(/&/g, "&amp;").replace(/</g, "&lt;") + "</pre></td><td>" + r[2] + "</td><td>" + r[3] + "</td></tr></table></div>"; };
  $("#mB").innerHTML = rows.map((r, i) => `<button class="b" data-i="${i}">${r[0]}</button>`).join("");
  $$("#mB button").forEach((b) => (b.onclick = () => paint(+b.dataset.i))); paint(0);
})();
''' + CLASSIFY("cl1", "What type of cause is each situation?", ["Programming error", "User error", "Hardware failure"],
  [("Dividing by a variable that holds zero", 0), ("Typing a file name that does not exist", 1), ("A hard disk crashes", 2), ("Reading element 12 of a 10-element array", 0), ("Entering letters where a number is expected", 1), ("A printer is disconnected during printing", 2), ("Adding a string to an integer in code", 0), ("The network cable is pulled out", 2)],
  "Programming errors are mistakes the program makes; user errors are bad input; hardware failure is a device problem.") + CLASSIFY("cl2", "Exception handling or an ordinary IF check?", ["Exception handling", "IF check"],
  [("Opening a file that might not exist", 0), ("Making sure a mark is between 0 and 100", 1), ("Converting text typed by the user to an integer", 0), ("Checking a menu choice is 1, 2 or 3", 1), ("Reading from a network that might disconnect", 0), ("Checking an index is less than the length of the list", 1), ("Writing to a disk that might be full", 0), ("Making sure a name is not empty", 1)],
  "Use exception handling for events outside the program's control. Use IF to check values you can test.") + ORDER(
  "Put the steps of a try and except in order.",
  ["The statements in the try block start to run", "One of them causes an exception", "The rest of the try block is skipped", "The matching except block runs", "The program carries on after the try statement"],
  "Try, exception, skip, handle, carry on.") + MATCH([
  ["Exception", "An unexpected event that disrupts a running program"], ["Exception handling", "Responding to the event so the program does not halt unexpectedly"], ["try", "The block of statements that might cause the exception"], ["except", "The block that responds to the exception"], ["finally", "Runs whether or not an exception happened"]]) + CALC([
  {"q": "A try block has 4 statements. The 2nd causes an exception. How many statements of the try block run completely?", "a": 1, "unit": "", "tol": 0.01, "hint": "Only the 1st finishes; the 2nd fails.", "sol": "<b>1</b>."},
  {"q": "A loop reads 10 lines in a try block. The 6th line is not a number, which raises ValueError. How many lines were converted successfully?", "a": 5, "unit": "", "tol": 0.01, "hint": "Lines 1 to 5.", "sol": "<b>5</b>."},
  {"q": "A program prints Done after a try/except. How many times is Done printed if an exception occurs and is handled?", "a": 1, "unit": "", "tol": 0.01, "hint": "The program carries on after the try statement.", "sol": "<b>1</b>."},
  {"q": "The user enters 5, then 0, then abc into a program with a handler for ValueError and a handler for ZeroDivisionError. How many handler blocks run in total?", "a": 2, "unit": "", "tol": 0.01, "hint": "5 causes no exception; 0 and abc each cause one.", "sol": "<b>2</b>."},
  {"q": "A file has 30 lines. A loop reads each line inside a try, with the file closed afterwards. If the file does not exist, how many lines are read?", "a": 0, "unit": "", "tol": 0.01, "hint": "The open fails.", "sol": "<b>0</b>."}]) + MCQ([
  ("What is an exception?", ["A programming language", "An unexpected event during execution that disrupts the program", "A type of loop", "An error in the design"], 1, "It happens at run time."),
  ("Which is the best definition of exception handling?", ["Preventing all errors", "Responding to unexpected events so the program does not halt unexpectedly", "Printing a program's errors", "Ignoring errors"], 1, "The program responds and carries on."),
  ("Which is a hardware cause of an exception?", ["Dividing by zero", "Typing a wrong file name", "A disk crash", "A missing bracket"], 2, "Disk crash or a lost device connection."),
  ("Where should the file opening go?", ["Outside the try", "Inside the try", "In the except", "After the program"], 1, "It is the statement that might fail."),
  ("What does the except block do?", ["Runs the risky code", "Responds to the exception, e.g. with a message", "Closes the program", "Creates a file"], 1, "It is the response."),
  ("Which should use an IF check rather than exception handling?", ["Opening a file", "Converting user input", "Checking that a score is between 0 and 100", "Reading a network connection"], 2, "A range can be tested directly.")], "qz1") + CARDS([
  ("Exception", "An unexpected event during execution that disrupts the program."), ("Exception handling", "Responding to it so the program does not halt unexpectedly."), ("try", "Statements that might cause an exception."), ("except", "Statements that respond to the exception."),
  ("Causes", "Programming errors, user errors, hardware failure."), ("finally", "Runs whether or not an exception happened."), ("Always add", "An output message in the except block."), ("Use for", "Files, input, devices: things outside the program's control.")])

build("ac2022", "ac-20-2-2-exception-handling", "Exception Handling: try and except", EYA("20.2.2"),
  "What an exception is, its causes, why and when to use exception handling, try, except and finally in Python, the patterns the exam uses with files and input; animations, labs and the real Paper 3 and Paper 4 questions.",
  dict(sub=CBK("Chapter 20 · Further programming, section 20.2 File processing and exception handling"), **tabs(learn, watch, explore, practise, real, exam, tips)), js)
