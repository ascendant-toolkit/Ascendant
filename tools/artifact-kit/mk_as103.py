"""AS CS 10.3: text files. Run: python3 tools/artifact-kit/mk_as103.py"""
from ascs import *

def pc(text, label=None): return code(text.strip("\n").split("\n"), label=label)

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>A <b>text file</b> stores data permanently as lines of text; a program must <b>open</b> it in a <b>mode</b>, <b>read</b> or <b>write</b> it, and <b>close</b> it. <b>READ</b> mode lets you read lines one at a time with <span class="mono">READFILE</span> until <span class="mono">EOF()</span> (end of file) is true; <b>WRITE</b> mode creates the file or <b>overwrites</b> everything in it; <b>APPEND</b> mode <b>adds to the end</b> and keeps the existing data. A file is a better store than an array when the data must survive after the computer is switched off, when it is more than an array can hold, or when another program must use it. A file can only hold text, so numbers and Booleans must be converted to strings before writing (and back after reading). Typical exam tasks: search a file for a value, output the last lines, copy and reformat lines, and create several files.</p></div>

  <h2>1 · The file statements</h2>
  ''' + pc('''
OPENFILE "Stock.txt" FOR READ          // READ, WRITE or APPEND
READFILE "Stock.txt", ThisLine         // read the next line into a variable
WRITEFILE "Result.txt", NewString      // write one line
CLOSEFILE "Stock.txt"

WHILE NOT EOF("Stock.txt")             // repeat until the end of the file
   READFILE "Stock.txt", ThisLine
ENDWHILE''') + '''
  <div class="tw"><table class="t">
    <tr><th>Mode</th><th>Effect</th><th>Use when</th></tr>
    <tr><td><b>READ</b></td><td>Lines are read one at a time from the start</td><td>You only need the data</td></tr>
    <tr><td><b>WRITE</b></td><td>Creates the file, or <b>overwrites</b> existing data</td><td>Making a new file</td></tr>
    <tr><td><b>APPEND</b></td><td>Adds lines at the end; existing data is kept</td><td>Adding records to a file that already has data (AddItem(), adding names to a support list)</td></tr>
  </table></div>
  <p>Why use a file instead of an array: data is <b>saved after the computer is switched off</b> and need not be re-entered; the number of values can be larger than a fixed array; the data can be used by another program.</p>

  <h2>2 · Common file algorithms</h2>
  <ul>
    <li><b>Search:</b> open for READ; loop until EOF <b>or</b> the value is found; read a line; extract the field (MID, LEFT, RIGHT with the field lengths); compare; if found, output; close; if not found, say so after the loop.</li>
    <li><b>Last three lines:</b> keep three variables and <b>shuffle</b> them as each line is read: <span class="mono">LineX ← LineY</span>, <span class="mono">LineY ← LineZ</span>, <span class="mono">LineZ ← ThisLine</span>; after the loop output them in order.</li>
    <li><b>Efficient search of a sorted file:</b> the search can stop as soon as the current value read is greater than the value being searched for.</li>
    <li><b>Copy and reformat:</b> open the old file for READ and the new file for WRITE; read three lines; join them with a separator; write; repeat until EOF; close both.</li>
    <li><b>Several files:</b> a loop creates a name (root, a dot, a three-digit suffix padded with zeros) and opens each file for WRITE, writes a line and closes it.</li>
  </ul>
  ''' + pc('''
PROCEDURE LastLines(ThisFile : STRING)
   DECLARE ThisLine, LineX, LineY, LineZ : STRING
   OPENFILE ThisFile FOR READ
   LineY ← ""
   LineZ ← ""
   WHILE NOT EOF(ThisFile)
      READFILE ThisFile, ThisLine
      LineX ← LineY
      LineY ← LineZ
      LineZ ← ThisLine
   ENDWHILE
   CLOSEFILE ThisFile
   OUTPUT LineX
   OUTPUT LineY
   OUTPUT LineZ
ENDPROCEDURE''') + '''

  <h2>Common ways to lose marks</h2>
  <ul>
    <li>Not opening the file, not closing it, or opening it in the wrong mode (WRITE when the data must be kept).</li>
    <li>Reading with no loop, or a loop with no EOF test.</li>
    <li>Reading the file inside the loop after the end condition (read, then test again).</li>
    <li>Writing a number without converting it to a string.</li>
    <li>Searching the whole file when the question says the file is sorted and asks for efficiency.</li>
  </ul>
'''

watch = '''
  <h2>1 · Reading a file line by line</h2>
  <div id="stA"></div>
  <h2>2 · Write and append</h2>
  <div id="stB"></div>
  <h2>3 · The last three lines</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Write or append?</h2>
  <p>The file starts with three names. Choose a mode and add a new name.</p>
  <div class="card"><div class="btnrow"><button id="wm_w">WRITE "Dee"</button><button id="wm_a">APPEND "Dee"</button><button id="wm_r">Reset</button></div><div id="wmV"></div></div>
  <h2>Lab 2 · Search a file</h2>
  <div class="card"><div id="sS"></div><div class="btnrow"><button id="fs_step">Read next line</button><button id="fs_reset">Reset</button></div><div id="fsV"></div></div>
  <h2>Lab 3 · Which mode?</h2>
  <div class="card"><div id="mB" class="btnrow"></div><div id="mO"></div></div>
'''

_pr, _prjs = PR(["Which file mode?", "File or array?", "Match the statement to its job", "Put the file-search steps in order", "Working out", "Multiple choice"],
  ("Which file mode is needed?", ["READ", "WRITE", "APPEND"], [("Searching a file for a value", 0), ("Creating a brand new file", 1), ("Adding an item to the end of Stock.txt", 2), ("Counting the lines in a file", 0), ("Replacing all the data in a file", 1), ("Adding names to a file that already has other group tests", 2)], "Read: look. Write: replace. Append: add."),
  ("Is a file or an array the better store?", ["File", "Array"], [("The data must be saved after the computer is switched off", 0), ("A small, fixed number of values used while the program runs", 1), ("The data must be used by another program", 0), ("Fast access by index in a loop", 1), ("The number of values is unknown and may be large", 0), ("Temporary values that can be lost at the end", 1)], "Permanent: file. Temporary: array."),
  [["OPENFILE", "Opens a file in a mode"], ["READFILE", "Reads the next line"], ["WRITEFILE", "Writes a line"], ["EOF", "True at the end of the file"], ["CLOSEFILE", "Closes the file"]],
  ("Put the file-search steps in order.", ["Open the file in read mode", "Repeat until the value is found or the end of the file", "Read a line and extract the field", "Compare it with the search value", "Close the file and report whether it was found"], "Open, loop, read, compare, close."),
  [{"q": "A file has 10 000 lines. A linear search finds a word on line 4321. How many lines are read?", "a": 4321, "unit": "", "tol": 0.01, "hint": "Up to and including that line.", "sol": "<b>4321</b>."}, {"q": "A file has 12 lines. After APPEND of 3 lines, how many lines?", "a": 15, "unit": "", "tol": 0.01, "hint": "12 + 3.", "sol": "<b>15</b>."}, {"q": "A file has 12 lines. After WRITE of 3 lines (overwriting), how many lines?", "a": 3, "unit": "", "tol": 0.01, "hint": "The old lines are gone.", "sol": "<b>3</b>."}, {"q": "A suffix is always three characters. The file number 7 gives the suffix 007. How many zeros are added?", "a": 2, "unit": "", "tol": 0.01, "hint": "3 − 1.", "sol": "<b>2</b>."}, {"q": "The record is <Field1><Field2><Field3> with lengths 4, 5 and 12. Field 2 starts at which character?", "a": 5, "unit": "", "tol": 0.01, "hint": "4 + 1.", "sol": "<b>5</b> (MID(Line, 5, 5))."}],
  [("APPEND mode:", ["Adds to the end and keeps old data", "Deletes old data", "Only reads", "Closes the file"], 0, "Adds."), ("WRITE mode:", ["Overwrites existing data", "Keeps old data", "Only reads", "Appends"], 0, "Overwrites."), ("EOF is true at:", ["The end of the file", "The start", "Line 1", "Never"], 0, "End."), ("A file is better than an array when:", ["Data must be kept after switch-off", "The data is tiny", "Speed only", "No data"], 0, "Permanent."), ("Before writing a number to a file you:", ["Convert it to a string", "Round it", "Close it", "Sort it"], 0, "Convert to string."), ("Always:", ["Close the file after use", "Leave it open", "Use WRITE", "Use EOF only"], 0, "Close.")],
  [("OPENFILE", "Mode: READ, WRITE or APPEND."), ("READFILE", "Next line into a variable."), ("WRITEFILE", "A line to the file."), ("EOF", "True at the end."), ("APPEND", "Add; keep old data."), ("WRITE", "Overwrite."), ("Search", "Loop until found or EOF."), ("Why a file", "Permanent; shared; unlimited.")])

real = RWNOTE + (
rw("A game's high-score table", "Scores are saved in a file so they are still there tomorrow; each new score is appended.", "append mode.") +
rw("A teacher's mark list", "A program reads the class list from a file line by line to print each name, until the end of the file.", "read until EOF.") +
rw("A log file", "Programs add a line to a log every time something happens; old lines are never overwritten.", "append.") +
rw("Importing contacts", "An app reads each line of a file, splits it at the separator character and creates a contact.", "extract fields from a line.") +
rw("Saving a document", "Saving writes the whole document to a file, replacing the earlier version.", "write mode.")
)

where = [
  ("M/J 2022", "21", "5", "6", "Describe the algorithm to search a file of fixed-length fields"),
  ("M/J 2022", "22", "4", "6 + 3", "Write LastLines(); the changes needed to output any number of lines"),
  ("O/N 2023", "22", "6", "6 + 3", "Write CreateFiles(); the module type, header and mode for CheckFiles()"),
  ("M/J 2023", "21", "8", "7 + 7 + 3 + 1 + 3", "IsNewSupp(); an efficient CheckNewItem(); testing; the file mode for AddItem(); a sorted file"),
  ("O/N 2024", "21", "3", "4 + 1 + 4", "Complete the steps to output the last three lines; their purpose; output from a given line"),
  ("O/N 2025", "22", "3", "6 + 1 + 3", "Convert a three-line file into one line per member with a separator"),
  ("M/J 2026", "22", "3", "6", "Describe an efficient algorithm to check that a word is in WordList.txt")]

past = '''  <p class="note">File questions appear in every Paper 2 and are marked on the same points: open (right mode), loop to EOF, read a line, test or extract, output or write, close. Paper 2 questions are reworded from the papers; check the original paper and mark scheme for the exact wording.</p>
''' + peq(SRC("s22", "21", "Q5"), "6 marks", "Describe",
  "Each line of a text file contains fixed-length fields <Field 1><Field 2><Field 3>. An algorithm is required to search for the first instance of a given value of Field 2 and, if found, to output the corresponding values of Field 1 and Field 3. Describe the algorithm. Do not include pseudocode statements.", "Open, loop to found or EOF, read, extract Field 2, compare, output, close.",
  "<p>Any six: " + mks(["Open the file in read mode", "A conditional loop, repeating until the value is found or the end of the file is reached", "Read a line from the file in the loop", "Extract Field 2", "Describe how Field 2 is extracted (for example a substring function with the lengths of Fields 1 and 2)", "Compare the extracted field with the search value", "If found, extract Fields 1 and 3 and output them", "Close the file after the loop has finished"]) + "</p>", None) + peq(SRC("s22", "22", "Q4"), "6 + 3 marks", "Write / Outline",
  "(a) A procedure LastLines() takes the name of a text file as a parameter and outputs the last three lines in the order they appear. Use local variables LineX, LineY and LineZ. Assume the file exists and has at least three lines. Write pseudocode. (b) The calling program now also passes the number of lines to output (1 to 30). Outline three changes needed.", "Read in a loop and shuffle LineX, LineY, LineZ. Parameter, array, shuffle.",
  "<p><b>(a)</b> " + mks(["Procedure heading with the parameter, and ending", "Declare the local variables, open the file in READ mode and close it", "A loop until EOF(ThisFile)", "Read a line from the file in the loop", "An attempt at a shuffle in the loop", "Correctly shuffle LineX, LineY and LineZ in the loop", "Output the three lines in the correct sequence"]) + "</p>" + pc('''
PROCEDURE LastLines(ThisFile : STRING)
   DECLARE ThisLine, LineX, LineY, LineZ : STRING
   OPENFILE ThisFile FOR READ
   LineY ← ""
   LineZ ← ""
   WHILE NOT EOF(ThisFile)
      READFILE ThisFile, ThisLine
      LineX ← LineY
      LineY ← LineZ
      LineZ ← ThisLine
   ENDWHILE
   CLOSEFILE ThisFile
   OUTPUT LineX
   OUTPUT LineY
   OUTPUT LineZ
ENDPROCEDURE''') + "<p><b>(b)</b> " + mks(["Change the procedure header to include a numeric parameter as well as the filename", "Replace LineX, LineY and LineZ with an array", "Amend the shuffle mechanism"], "a") + "</p>", "Opening the file in WRITE mode. That would erase the file you are trying to read.") + peq(SRC("w23", "22", "Q6"), "6 + 3 marks", "Write",
  "(a) A procedure CreateFiles() takes a string file name and an integer number of files. It creates that many text files; each name is the file name followed by a dot and a three-character suffix based on the file number (CreateFiles(\"TestData\", 3) creates TestData.001, TestData.002 and TestData.003), and each file holds a single line such as \"This is File TestData.002\". Write pseudocode (the integer is between 1 and 999). (b) A module CheckFiles() takes a file name and returns the number of files found. (i) Identify the type of module. (ii) Write its header. (iii) State the file mode.", "FOR loop; NUM_TO_STR; pad with '0'; OPENFILE FOR WRITE; WRITEFILE; CLOSEFILE. Function; READ.",
  "<p><b>(a)</b> " + mks(["Procedure heading, including parameters, and ending", "A loop for NumFiles iterations", "An attempt to create the suffix using NUM_TO_STR() in the loop", "The completely correct filename", "OPENFILE in WRITE mode and the subsequent CLOSE in the loop", "Write the first line to the file in the loop"]) + "</p>" + pc('''
PROCEDURE CreateFiles(NameRoot : STRING, NumFiles : INTEGER)
   DECLARE FileName, Suffix : STRING
   DECLARE Count : INTEGER
   FOR Count ← 1 TO NumFiles
      Suffix ← NUM_TO_STR(Count)
      WHILE LENGTH(Suffix) <> 3
         Suffix ← '0' & Suffix
      ENDWHILE
      FileName ← NameRoot & '.' & Suffix
      OPENFILE FileName FOR WRITE
      WRITEFILE FileName, "This is File " & FileName
      CLOSEFILE FileName
   NEXT Count
ENDPROCEDURE''') + "<p><b>(b)</b> " + mks(["(i) Function", "(ii) FUNCTION CheckFiles(NameRoot : STRING) RETURNS INTEGER", "(iii) Read"], "a") + "</p>", None) + peq(SRC("s23", "21", "Q8(b)(d)(e)"), "7 + 1 + 3 marks", "Write / State",
  "Stock.txt has one line per item <ItemNum><SupplierCode><Description> (ItemNum is 4 numeric characters, \"0001\" to \"5999\"); the file is in ascending order of ItemNum and does not contain every value. (b) Write efficient pseudocode for CheckNewItem(NewLine : STRING), which returns TRUE if the item number of NewLine is not already in the file, otherwise FALSE. (d) AddItem() will add information to the file: state the file mode. (e) FindItem() searches the sorted file: describe how the organisation improves efficiency.", "LEFT(line, 4); loop until EOF or found or the current value is greater. Append. Stop early.",
  "<p><b>(b)</b> " + mks(["Open Stock.txt in READ mode and close it", "Extract NewItemNum from the parameter", "A conditional loop until EOF", "or until the number is found", "or until ThisItemNum is greater than NewItemNum", "Read a line and extract ThisItemNum in the loop", "If ThisItemNum = NewItemNum terminate the loop or set a flag", "Return a Boolean"]) + " (max 7)</p>" + pc('''
FUNCTION CheckNewItem(NewLine : STRING) RETURNS BOOLEAN
   DECLARE NotFound : BOOLEAN
   DECLARE NewItemNum, ThisItemNum, ThisLine : STRING
   NotFound ← TRUE
   OPENFILE "Stock.txt" FOR READ
   NewItemNum ← LEFT(NewLine, 4)
   ThisItemNum ← "0000"
   WHILE NOT EOF("Stock.txt") AND NotFound = TRUE AND ThisItemNum < NewItemNum
      READFILE "Stock.txt", ThisLine
      ThisItemNum ← LEFT(ThisLine, 4)
      IF ThisItemNum = NewItemNum THEN
         NotFound ← FALSE
      ENDIF
   ENDWHILE
   CLOSEFILE "Stock.txt"
   RETURN NotFound
ENDFUNCTION''') + "<p><b>(d)</b> " + mks(["Append"], "a") + " <b>(e)</b> " + mks(["The search can stop (the iteration only continues)", "if the current value read from the file is greater than the value being searched for"], "b") + "</p>", "Searching to the end of the file even when the current item number is already larger than the one wanted.") + peq(SRC("w24", "21", "Q3"), "4 + 1 + 4 marks", "Complete / Explain / Describe",
  "An algorithm outputs the last three lines of Result.txt in the order they appear (LineX, LineY and LineZ are empty strings). (a) Complete the eight steps: 1. ...; 2. ...; 3. ...; 4. Assign LineY to LineX; 5. Assign LineZ to LineY; 6. Assign ThisLine to LineZ; 7. ...; 8. Output LineX, LineY, LineZ. (b) Explain the purpose of steps 4, 5 and 6. (c) The algorithm becomes a function that is called with a line number, outputs three lines starting at that line and returns TRUE if three lines were output, or FALSE otherwise. Describe the changes to steps 2 to 8.", "Open, loop until EOF, read into ThisLine; close after. Output in order. Skip lines, three lines, EOF returns FALSE.",
  "<p><b>(a)</b> " + mks(["1: open the file Result.txt in read mode", "2: loop until EOF (end of file)", "3: read the next line from the file and store it in ThisLine", "7: after the loop, close the file"]) + "</p><p><b>(b)</b> " + mks(["So that the last three lines of the file are output in the correct order"], "a") + "</p><p><b>(c)</b> Any four: " + mks(["Loop until the given line number − 1 lines have been read", "If the end of the file is reached return FALSE", "Loop for three lines: read a line and output it", "If the end of the file is reached return FALSE", "After outputting the required lines return TRUE", "The ordering of the lines is no longer needed"], "b") + "</p>", None) + peq(SRC("w25", "22", "Q3"), "6 + 1 + 3 marks", "Complete / Explain",
  "OldFile.txt holds club members, three lines per member (ID \"AB1234\", name, email). It is to be reorganised into NewFile.txt with one line per member using '\\' as a separator, for example \"AB1234\\Freddie Jones\\FreddieJ909@Cambridge.org\". LineX, LineY, LineZ and NewString are STRING variables. (a) Complete the numbered steps of the algorithm. (b) Explain why '\\' is a suitable separator. (c) Two new encrypted items (any characters, up to 99 characters each) will also be stored for each member. Describe how this can be done so each item can be recovered from its line.", "Open both; read three lines; join with separators; write; repeat; close.",
  "<p><b>(a)</b> " + mks(["Open OldFile.txt in read mode and NewFile.txt in write mode", "Read three lines from OldFile.txt and store them in LineX, LineY and LineZ", "Set NewString to LineX & '\\' & LineY & '\\' & LineZ", "Write NewString to NewFile.txt", "Repeat from the read step until the end of OldFile.txt", "Close both files"]) + "</p><p><b>(b)</b> " + mks(["It does not appear in any of the data items (the ID, the name or the email address)"], "a") + "</p><p><b>(c)</b> Any three: " + mks(["Add a new single separator at the end of the third (original) item", "Calculate the length of both new data items", "Store the length of each new item", "as a fixed-length digit string, so each item can be extracted using its length"], "b") + "</p>", "Choosing a separator such as a space or comma that can appear in names or addresses.") + peq(SRC("s26", "22", "Q3"), "6 marks", "Complete",
  "A game uses WordList.txt containing 10 000 unique lower-case words, one per line. An efficient algorithm checks that a word input by the user is in the file: if found, output the line number; if not, output \"Not Found\". Complete the steps (no pseudocode). Steps 1 to 3 are: set line counter to 0; input a word; convert the word to lower case.", "Open in read mode; read the next line; increment the counter; compare; output the counter; not found after.",
  "<p>Any six: " + mks(["Step 4: open WordList.txt in read mode (and close it afterwards), outside any loop", "Step 5: read the next line from the file, in a loop", "Step 6: increment the line counter", "Step 7: check whether the line read equals the word input", "Step 8: if it does, output the line counter", "Step 9: if the word is not found after all iterations, output \"Not Found\"", "Step 10: otherwise repeat from step 5 (with an end condition: found or end of file)"]) + "</p>", None)

review = req("5 marks", "Write", "Write pseudocode for a procedure ShowNames() that outputs every line of the file Names.txt.", "Open, loop to EOF, close.", "<p>" + mks(["Procedure heading and ending, a declared variable", "OPENFILE for READ", "A loop until EOF", "Read and output the line in the loop", "CLOSEFILE"]) + "</p>" + pc("PROCEDURE ShowNames()\n   DECLARE ThisLine : STRING\n   OPENFILE \"Names.txt\" FOR READ\n   WHILE NOT EOF(\"Names.txt\")\n      READFILE \"Names.txt\", ThisLine\n      OUTPUT ThisLine\n   ENDWHILE\n   CLOSEFILE \"Names.txt\"\nENDPROCEDURE"), None) + req("3 marks", "Write", "Write pseudocode to add the string NewName to the end of Names.txt without losing the existing names.", "APPEND.", "<p>" + mks(["OPENFILE in APPEND mode", "WRITEFILE the string", "CLOSEFILE"]) + "</p>", None) + req("2 marks", "State", "State two reasons for storing scores in a file rather than an array.", "Permanent, shared.", "<p>" + mks(["The scores are saved after the computer is switched off", "The file can hold more values than a fixed array and another program can use it"]) + "</p>", None) + req("3 marks", "Describe", "Describe how to count the lines in a file (no pseudocode).", "Counter, loop, EOF.", "<p>" + mks(["Set a counter to zero and open the file for reading", "Repeat until the end of the file: read a line and add 1 to the counter", "Close the file and output the counter"]) + "</p>", None) + req("2 marks", "Explain", "Explain why the number 25 must be converted before it is written to a text file.", "Files hold text.", "<p>" + mks(["A text file stores strings", "so the number is converted with NUM_TO_STR before writing"]) + "</p>", None)

tips = tips_html([
  ("Open, loop, close.", "In READ, WRITE or APPEND."),
  ("Append keeps old data.", "Write overwrites."),
  ("Loop until EOF.", "And until found, if searching."),
  ("Extract fields with MID/LEFT/RIGHT.", "Use the field lengths."),
  ("Sorted file: stop early.", "When the line is greater."),
  ("Strings only.", "Convert numbers before writing."),
], [("a file mode", "READ, WRITE or APPEND: how the file is opened."), ("EOF", "A function that is true at the end of a file."), ("append", "Adding to the end of a file, keeping existing data."), ("a separator", "A character that splits items on a line.")],
  [("Write", "Write the pseudocode."), ("Describe", "Steps in words."), ("Complete", "Fill the missing steps."), ("State", "Short answer.")]) + FC

js = AKJS + AK20JS + r'''
(function () {
  const lines = ["Ann", "Ben", "Cy", "Di"]; const draw = (s) => { const k = Math.round(s.i); let o = SV.text(20, 14, "file", "sm"); lines.forEach((l, i) => o += SV.rect(20, 20 + i * 28, 140, 24, i === k - 1 ? "f3" : i < k - 1 ? "f1" : "cell", { rx: 4 }) + SV.text(28, 37 + i * 28, (i + 1) + "  " + l, "lbl", { style: "font-size:12px" })); o += SV.text(200, 50, k === 0 ? "OPENFILE ... FOR READ" : k <= 4 ? "READFILE: ThisLine = \"" + lines[k - 1] + "\"" : "EOF is TRUE: leave the loop, CLOSEFILE", "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stA"), { w: 520, h: 140, label: "Reading", base: { i: 0 }, draw, tween: 100, dwell: 1800, steps: ["Open the file in read mode.", "Read line 1.", "Read line 2.", "Read line 3.", "Read line 4.", "No more lines: EOF is true."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const old = ["Ann", "Ben"]; let o = SV.text(20, 14, k === 0 ? "file before" : k === 1 ? "after WRITE \"Cy\"" : "after APPEND \"Cy\"", "lbl bd", { style: "font-size:13px" }); const L = k === 0 ? old : k === 1 ? ["Cy"] : [...old, "Cy"]; L.forEach((l, i) => o += SV.rect(20, 24 + i * 28, 160, 24, l === "Cy" ? "f3" : "cell", { rx: 4 }) + SV.text(28, 41 + i * 28, l, "lbl", { style: "font-size:12px" })); o += SV.text(220, 60, k === 1 ? "old data overwritten" : k === 2 ? "old data kept" : "", "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stB"), { w: 440, h: 110, label: "Write and append", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: ["The file holds two names.", "<b>WRITE</b> replaces everything.", "<b>APPEND</b> adds to the end."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const L = ["l1", "l2", "l3", "l4", "l5"]; const draw = (s) => { const k = Math.round(s.i); const x = k >= 1 ? L[k - 1] : "", y = k >= 2 ? L[k - 2] : "", z = k >= 3 ? L[k - 3] : ""; const v = k >= 3 ? [L[k - 3], L[k - 2], L[k - 1]] : ["", "", k >= 1 ? L[k - 1] : ""]; let o = ""; ["LineX", "LineY", "LineZ"].forEach((n, i) => o += SV.rect(20 + i * 100, 20, 92, 36, "cell", { rx: 5 }) + SV.text(66 + i * 100, 34, n, "sm", { "text-anchor": "middle" }) + SV.text(66 + i * 100, 50, v[i], "lbl bd", { "text-anchor": "middle" }));
    o += SV.text(20, 88, k === 0 ? "start: all empty" : "read " + L[k - 1] + ": shuffle LineX ← LineY, LineY ← LineZ, LineZ ← new line", "lbl bd t3", { style: "font-size:12px" }); return o; };
  Lib.stepper($("#stC"), { w: 420, h: 105, label: "Shuffle", base: { i: 0 }, draw, tween: 100, dwell: 2000, steps: ["Three variables start empty.", "Line 1 read.", "Line 2 read.", "Line 3 read.", "Line 4 read: the earliest line drops out.", "Line 5 read: LineX, LineY, LineZ hold the last three, in order."].map((c, i) => ({ cap: c, s: { i } })) });
})();

(function () {
  let st; const reset = () => { st = ["Ann", "Ben", "Cy"]; paint("The file holds Ann, Ben, Cy."); }; const paint = (m) => { $("#wmV").innerHTML = '<div class="tw"><table class="t mono"><tr><th>line</th><th>data</th></tr>' + st.map((l, i) => `<tr><td>${i + 1}</td><td>${l}</td></tr>`).join("") + `</table></div><div class="verdict">${m}</div>`; };
  $("#wm_w").onclick = () => { st = ["Dee"]; paint("WRITE overwrote the file: Ann, Ben and Cy are lost."); }; $("#wm_a").onclick = () => { st.push("Dee"); paint("APPEND added Dee at the end: the old names are kept."); }; $("#wm_r").onclick = reset; reset();
})();
(function () {
  const words = ["apple", "bread", "cheese", "dates", "eggs", "flour", "grapes"]; let target = "eggs", k = 0, found = 0; const paint = () => { $("#fsV").innerHTML = '<div class="tw"><table class="t mono"><tr><th>line</th><th>word</th></tr>' + words.slice(0, k).map((w, i) => `<tr><td>${i + 1}</td><td>${w}${w === target ? " ← found" : ""}</td></tr>`).join("") + `</table></div><div class="verdict">${found ? `Found "${target}" on line <b>${found}</b> after reading ${k} line(s). The loop stops at once.` : k >= words.length ? `End of file: output "Not Found".` : "Press Read next line."}</div>`; };
  const bar = $("#sS"); words.forEach((w) => { const b = document.createElement("button"); b.textContent = w; b.onclick = () => { target = w; bar.querySelectorAll("button").forEach((x) => x.className = x === b ? "on" : ""); k = 0; found = 0; paint(); }; if (w === target) b.className = "on"; bar.appendChild(b); });
  $("#fs_step").onclick = () => { if (found || k >= words.length) return; k++; if (words[k - 1] === target) found = k; paint(); }; $("#fs_reset").onclick = () => { k = 0; found = 0; paint(); }; paint();
})();
btnTable("mB", "mO", [
  ["Read a stock file line by line", "READ", "Only looking"],
  ["Create TestData.001", "WRITE", "A new file"],
  ["AddItem() adds a line to Stock.txt", "APPEND", "Keep the old items"],
  ["Add names to a support list that has earlier group tests", "APPEND", "WRITE would overwrite them"]
], ["Task", "Mode", "Why"]);
''' + _prjs

finish("as-10-3-text-files", "as103", "Text Files",
  "Opening files in READ, WRITE and APPEND mode, reading to the end of file, searching, the last three lines, copying and creating files, with animations, file labs and the real Paper 2 questions from 2021 to 2026.",
  "10.3", "10 · Data types and structures", "section 10.3 Files", learn, watch, explore, _pr, real, where, past, review,
  "Part 1 is real 9618 questions on text files (Paper 2), 2021 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", tips, js)
