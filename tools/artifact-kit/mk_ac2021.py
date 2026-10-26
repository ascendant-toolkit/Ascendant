"""A Level CS syllabus 20.2.1: file processing (text, serial, sequential and random files). Run: python3 tools/artifact-kit/mk_ac2021.py"""
from ak20 import *

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>A program's variables disappear when it ends, so data that must last is stored in a <b>file</b> on secondary storage. To use a file you <b>open</b> it in a mode (read, write, append, or random), <b>read</b> or <b>write</b> one record or line at a time, and then <b>close</b> it. A <b>text file</b> is processed from the start in order: <b>serial</b> files hold records in the order they were added and <b>sequential</b> files hold them in key order, so both are read one record after another until the end of the file. A <b>random</b> file lets the program jump straight to a record: <b>SEEK</b> moves to a position, then <b>GETRECORD</b> reads it or <b>PUTRECORD</b> writes it. Paper 3 asks you to complete this pseudocode; Paper 4 asks you to read and write files in Python.</p></div>

  <h2>1 · Opening, reading, writing and closing</h2>
  <div class="tw"><table class="t">
    <tr><th>Pseudocode</th><th>What it does</th><th>Python</th></tr>
    <tr><td><code>OPENFILE "Data.txt" FOR READ</code></td><td>Opens an existing file to read from the start</td><td><code>f = open("Data.txt", "r")</code></td></tr>
    <tr><td><code>OPENFILE "Out.txt" FOR WRITE</code></td><td>Opens a file to write. A new file is created; an existing file is <b>overwritten</b></td><td><code>f = open("Out.txt", "w")</code></td></tr>
    <tr><td><code>OPENFILE "Log.txt" FOR APPEND</code></td><td>Opens a file and adds new data to the <b>end</b></td><td><code>f = open("Log.txt", "a")</code></td></tr>
    <tr><td><code>READFILE "Data.txt", Line</code></td><td>Reads the next line into the variable</td><td><code>Line = f.readline()</code> or <code>for Line in f:</code></td></tr>
    <tr><td><code>WRITEFILE "Out.txt", Line</code></td><td>Writes the value as the next line</td><td><code>f.write(Line + "\\n")</code></td></tr>
    <tr><td><code>EOF("Data.txt")</code></td><td>True when there is nothing left to read</td><td>the <code>for</code> loop ends; <code>readline()</code> returns <code>""</code></td></tr>
    <tr><td><code>CLOSEFILE "Data.txt"</code></td><td>Closes the file so all data is saved and it can be reused</td><td><code>f.close()</code></td></tr>
  </table></div>
  <div class="tip"><b class="h">Always close</b>Every file that is opened must be closed, in an appropriate place (after the loop, not inside it). Closing a written file makes sure the data is actually saved. Python's <code>with open(...) as f:</code> closes it for you; the mark scheme accepts it.</div>

  <h2>2 · Reading a text file into an array</h2>
  <p>Each line of a text file is one string. Convert it to the type you need (<code>int(Line)</code>), and remove the newline with <code>strip()</code> if you will compare or split it.</p>
  <div class="code">''' + pc('''DataArray = []                                   # 25 elements of type integer
DataFile = open("Data.txt", "r")
for Line in DataFile:                            # one pass for each line, until the end of file
    DataArray.append(int(Line))
DataFile.close()''') + '''</div>
  <p>When a record is spread over several lines, read the lines in the order they were written, or keep the fields on one line and split them:</p>
  <div class="code">''' + pc('''File = open("HighScore.txt", "r")
for x in range(0, 10):
    FileData[x][0] = File.readline()[:3]        # line 1: three-character player name
    FileData[x][1] = File.readline().strip()    # line 2: the score
File.close()

# a record on one line, fields separated by spaces:   "Aria True 12 3"
Parts = Line.strip().split(" ")                 # ["Aria", "True", "12", "3"]''') + '''</div>

  <h2>3 · Writing and appending</h2>
  <div class="code">''' + pc('''File = open("NewHighScore.txt", "w")             # write: creates or overwrites
for x in range(0, 10):
    File.write(str(FileData[x][0]) + "\\n")
    File.write(str(FileData[x][1]) + "\\n")
File.close()

Log = open("Log.txt", "a")                       # append: adds to the end
Log.write("Game finished\\n")
Log.close()''') + '''</div>
  <p><code>write</code> needs a string, so convert numbers with <code>str()</code>, and add <code>"\\n"</code> to start a new line. A comma-separated line such as the tree example is built by joining the fields: <code>str(A) + "," + str(B) + "," + str(C) + "\\n"</code>.</p>

  <h2>4 · Serial, sequential and random files</h2>
  <div class="tw"><table class="t">
    <tr><th>File</th><th>How records are stored</th><th>How you find a record</th><th>Adding a record</th></tr>
    <tr><td><b>Serial</b></td><td>In the order they were added, with no ordering on a key</td><td>Read from the start until found (or to the end to process all)</td><td>Append to the end</td></tr>
    <tr><td><b>Sequential</b></td><td>In order of a key field</td><td>Read in order; can stop once the key has been passed</td><td>Write a new file, inserting the record in the right place</td></tr>
    <tr><td><b>Random</b></td><td>At an address calculated from the key (position, or a hash)</td><td>Go straight to the address with SEEK, then GETRECORD</td><td>SEEK to the address, then PUTRECORD</td></tr>
  </table></div>
  <p>For a serial or sequential file the program loops: open, repeat <code>READFILE</code> until <code>EOF</code>, close. Processing a file means doing something to each record in that loop (copying, totalling, searching). To <b>delete</b> or <b>change</b> a record in a text file, write every record to a new file, changing or leaving out the one required.</p>
  <div class="code">''' + pc('''OPENFILE "ActiveFile.txt" FOR READ
OPENFILE "ArchiveFile.txt" FOR WRITE
WHILE NOT EOF("ActiveFile.txt")
   READFILE "ActiveFile.txt", Account
   IF Account = "" THEN
      WRITEFILE "ArchiveFile.txt", "Account not present"
   ELSE
      WRITEFILE "ArchiveFile.txt", Account
   ENDIF
ENDWHILE
CLOSEFILE "ActiveFile.txt"
CLOSEFILE "ArchiveFile.txt"''') + '''</div>

  <h2>5 · Random files: SEEK, GETRECORD and PUTRECORD</h2>
  <p>A random file is opened with <code>FOR RANDOM</code>. Each record has the same size, so the program can work out where record number <i>n</i> starts and jump there.</p>
  <div class="tw"><table class="t">
    <tr><th>Command</th><th>What it does</th></tr>
    <tr><td><code>OPENFILE "Stock.dat" FOR RANDOM</code></td><td>Opens the file for reading and writing at any position</td></tr>
    <tr><td><code>SEEK "Stock.dat", Location</code></td><td>Moves the file pointer to the record at that location</td></tr>
    <tr><td><code>GETRECORD "Stock.dat", Item</code></td><td>Reads the record at the pointer into the variable</td></tr>
    <tr><td><code>PUTRECORD "Stock.dat", Item</code></td><td>Writes the variable as the record at the pointer</td></tr>
  </table></div>
  <div class="code">''' + pc('''OPENFILE "StockList.dat" FOR RANDOM
OUTPUT "Enter a location between 1 and 500: "
INPUT Location
SEEK "StockList.dat", Location        // always SEEK before GETRECORD or PUTRECORD
GETRECORD "StockList.dat", Item
IF Item = "" THEN
   OUTPUT "This record is missing."
ELSE
   OUTPUT "The item in stock is ", Item
ENDIF
CLOSEFILE "StockList.dat"''') + '''</div>
  <p>The location is often calculated from the key with a <b>hash function</b> (for example the account number MOD the number of slots), so a record can be found without searching: <code>Location ← Hash(Customer.AccountNumber)</code>, <code>SEEK AccountFile, Location</code>, <code>GETRECORD AccountFile, Customer</code>. A random file has empty locations, which is why a record that reads back as <code>""</code> means "nothing stored here".</p>
  <div class="tw"><table class="t">
    <tr><th>Task</th><th>Pattern</th></tr>
    <tr><td>Read a record at a known place</td><td>OPEN RANDOM, SEEK, GETRECORD, CLOSE</td></tr>
    <tr><td>Store a record at a known place</td><td>OPEN RANDOM, SEEK, PUTRECORD, CLOSE</td></tr>
    <tr><td>Find the first empty slot</td><td>loop: SEEK, GETRECORD, if empty then PUTRECORD and stop, else add 1 to the location</td></tr>
    <tr><td>Copy records from one file to another</td><td>FOR each position: SEEK, GETRECORD from the first file, SEEK, PUTRECORD in the second</td></tr>
  </table></div>

  <h2>6 · Common ways to lose marks</h2>
  <ul>
    <li>Forgetting <code>CLOSEFILE</code>, or closing inside the loop, or before the last read.</li>
    <li>Using <code>FOR WRITE</code> when the data must be added to what is already there (that is <code>APPEND</code>), or <code>FOR READ</code> on a file you also write to.</li>
    <li>Leaving out <code>SEEK</code> before <code>GETRECORD</code> or <code>PUTRECORD</code> in a random file.</li>
    <li>Not converting what was read: a line is a string. Use <code>int()</code> before adding or comparing as numbers.</li>
    <li>Not removing the newline, so the data never equals what it should.</li>
    <li>Writing a number without <code>str()</code>, or forgetting the new line, so everything ends up on one line.</li>
    <li>Looping a fixed number of times when the question says "until the end of the file".</li>
    <li>In Paper 4, forgetting the exception handling mark for opening or reading the file (see the next page).</li>
  </ul>
'''

watch = '''
  <h2>1 · Reading a text file into an array</h2>
  <p>Press Play, or click the steps.</p>
  <div id="stA"></div>
  <h2>2 · Write overwrites, append adds</h2>
  <div id="stB"></div>
  <h2>3 · Copying a file one line at a time</h2>
  <div id="stC"></div>
  <h2>4 · Reaching record 600: serial or random?</h2>
  <div id="stD"></div>
  <h2>5 · A random file lookup with a hash</h2>
  <div id="stE"></div>
'''

explore = '''
  <h2>Lab 1 · What does the open mode do?</h2>
  <p>Choose a mode and whether the file already exists. The file holds the lines Ana, Ben, Cho. The program then writes the line Dev.</p>
  <div class="card"><div id="mB" class="btnrow"></div><div id="mE" class="btnrow"></div><div id="mO"></div><div class="verdict" id="mV"></div></div>

  <h2>Lab 2 · Step through a read loop</h2>
  <p>The file Scores.txt holds five numbers, one per line. Press Step to run each statement of the loop and watch the pointer, the variable and the total.</p>
  <div class="card"><div id="rS"></div><div class="btnrow"><button class="b pri" id="rN">Step</button><button class="b" id="rR">Reset</button></div><div class="verdict" id="rV"></div></div>

  <h2>Lab 3 · Find a record with a hash</h2>
  <p>Account records are stored in a random file with 11 locations, using Location = AccountNumber MOD 11. Enter an account number to see where it is stored, then try two numbers that map to the same place.</p>
  <div class="card"><div id="hS"></div><div id="hT"></div><div class="verdict" id="hV"></div></div>
'''

practise = '''
  <h2>1 · Read, write, append or random?</h2><div id="cl1" class="card"></div>
  <h2>2 · Serial, sequential or random file?</h2><div id="cl2" class="card"></div>
  <h2>3 · Put the steps for processing a text file in order</h2><div id="o1" class="card"></div>
  <h2>4 · Match the command to its job</h2><div id="m1" class="card"></div>
  <h2>5 · Count the operations</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("A high score table", "A game saves the top ten names and scores in a text file when it closes and reads them back when it starts. Writing replaces the old file with the new table.", "WRITE overwrites the file; read it back in the same order it was written.") +
rw("A log of events", "A server adds one line to a log every time something happens. The program opens the file in append mode so earlier lines are never lost.", "APPEND adds to the end of an existing file.") +
rw("A bank's account file", "Millions of account records are stored in a random file. The account number is turned into a location by a hash function, so one record can be fetched without reading the rest.", "random access: SEEK to the location and GETRECORD.") +
rw("A payroll run", "A program reads each employee's hours from a file, line by line, calculates pay and writes a payslip line to a new file. It stops at the end of the file.", "serial processing: read until EOF, process, write, close.") +
rw("Backing up a file", "A copy of every record is written one at a time from the live file to a stored file. Anything that is blank is replaced with a standard message.", "copying with SEEK, GETRECORD and PUTRECORD for random files, or READFILE and WRITEFILE for text.")
)

where = [
  ("M/J 2023", "31, 33", "10", "5", "Complete the copy of ActiveFile.txt to ArchiveFile.txt, replacing blank lines"),
  ("M/J 2023", "32", "6(b)", "5", "Complete the read of every record in the random file DentalFile.dat"),
  ("O/N 2023", "31, 33", "8(a)", "5", "Complete a random file lookup using a hash function"),
  ("O/N 2023", "32", "12(b)", "7", "Complete a search of a random file for a customer by name"),
  ("M/J 2025", "31", "12", "5", "Complete a check of a location in StockList.dat"),
  ("M/J 2025", "32", "13", "5", "Complete the copy of 50 records between two random files"),
  ("M/J 2025", "33", "11", "5", "Complete the insertion of a new stock item into the next empty location"),
  ("M/J 2026", "32", "10(b)", "6", "Complete TempCheck() using SEEK and GETRECORD"),
  ("M/J 2022", "41, 43", "1(b), 1(f)", "6 + 4", "Read pairs of lines from HighScore.txt; write the table to NewHighScore.txt"),
  ("O/N 2025", "42", "3(d)", "5", "Write the contents of TreeArray to a new text file, one comma-separated line each")]

past = '''  <p class="note">Paper 3 asks you to complete file-handling <b>pseudocode</b> (text and random files). Paper 4 asks you to read and write text files as <b>Python</b>, in almost every paper; the Paper 4 questions that award marks for exception handling are on the next page, and two that are mainly about reading and writing are here. Python is shown for Paper 4; Paper 3 answers are in the pseudocode the exam uses. Questions are reworded from the papers; check the original paper and mark scheme for the exact wording.</p>

  <h3>Paper 3: text files</h3>
''' + peq(SRC("s23", "31, 33", "Q10"), "5 marks", "Complete",
  "The pseudocode algorithm copies an active accounts text file ActiveFile.txt to an archive accounts text file ArchiveFile.txt, one line at a time. Any blank lines found in the active accounts file are replaced with the words \"Account not present\" in the archive file. Complete this file-handling pseudocode." + qcode('''DECLARE Account : STRING
...
OPENFILE "ArchiveFile.txt" FOR WRITE
WHILE NOT ...
   READFILE "ActiveFile.txt", Account
   IF Account = "" THEN
      WRITEFILE "ArchiveFile.txt", " ..."
   ELSE
      WRITEFILE "ArchiveFile.txt", ...
   ENDIF
ENDWHILE
...
CLOSEFILE "ArchiveFile.txt"'''),
  "Open the active file for reading, loop until its end, close both files at the end.",
  "<p>One mark for each correctly completed line (maximum 5): " + mks(['OPENFILE "ActiveFile.txt" FOR READ', 'WHILE NOT EOF("ActiveFile.txt")', 'WRITEFILE "ArchiveFile.txt", "Account not present"', 'WRITEFILE "ArchiveFile.txt", Account', 'CLOSEFILE "ActiveFile.txt"']) + "</p>" + pc('''DECLARE Account : STRING
OPENFILE "ActiveFile.txt" FOR READ
OPENFILE "ArchiveFile.txt" FOR WRITE
WHILE NOT EOF("ActiveFile.txt")
   READFILE "ActiveFile.txt", Account
   IF Account = "" THEN
      WRITEFILE "ArchiveFile.txt", "Account not present"
   ELSE
      WRITEFILE "ArchiveFile.txt", Account
   ENDIF
ENDWHILE
CLOSEFILE "ActiveFile.txt"
CLOSEFILE "ArchiveFile.txt"'''),
  "Closing only the archive file. Both files that were opened must be closed.") + '''
  <h3>Paper 3: random files</h3>
''' + peq(SRC("s23", "32", "Q6(b)"), "5 marks", "Complete",
  "The pseudocode reads dental records stored in a random file using the user-defined data type TAppointments and prints the contents of the file, one record at a time. Complete this file-handling pseudocode." + qcode('''DECLARE DentalRecord : ARRAY[1:250] OF TAppointments
DECLARE DentalFile : STRING
DECLARE Count : INTEGER
DentalFile ← "DentalFile.dat"
OUTPUT "The file ", DentalFile, " contains these records:"
OPENFILE ...
...  ← 1
REPEAT
   SEEK DentalFile, Count
   ...
   OUTPUT DentalRecord[Count]
   Count ← Count + 1
UNTIL ...
...'''),
  "A random file needs OPENFILE FOR RANDOM, a SEEK before each read, GETRECORD into the array element, and a stop at the end of the file.",
  "<p>One mark for each correctly completed line (maximum 5): " + mks(["OPENFILE DentalFile FOR RANDOM", "Count ← 1", "GETRECORD DentalFile, DentalRecord[Count]", "UNTIL EOF(DentalFile)", "CLOSEFILE DentalFile"]) + "</p>" + pc('''OPENFILE DentalFile FOR RANDOM
Count ← 1
REPEAT
   SEEK DentalFile, Count
   GETRECORD DentalFile, DentalRecord[Count]
   OUTPUT DentalRecord[Count]
   Count ← Count + 1
UNTIL EOF(DentalFile)
CLOSEFILE DentalFile'''),
  "Using READFILE on a random file. Random files are read with SEEK and GETRECORD.") + peq(SRC("w23", "31, 33", "Q8(a)"), "5 marks", "Complete",
  "A pseudocode algorithm finds a customer account record in a random file and outputs it. The records are stored using the user-defined data type TAccount (AccountNumber : INTEGER, LastName, FirstName, Address, ContactNumber : STRING). The function Hash() takes the customer account number as a parameter, calculates and returns the hash value. Complete the file-handling pseudocode." + qcode('''DECLARE Customer : TAccount
DECLARE Location : INTEGER
DECLARE AccountFile : STRING
...      "AccountRecords.dat"
... AccountFile ...
OUTPUT "Please enter an account number"
INPUT Customer.AccountNumber
Location ← Hash( ...)
SEEK ... , Location
... AccountFile, ...
OUTPUT Customer                // output customer record
CLOSEFILE AccountFile'''),
  "Assign the filename, open for random access, hash the account number, SEEK, then read the record into Customer.",
  "<p>One mark for each correctly completed line (maximum 5): " + mks(['AccountFile ← "AccountRecords.dat"', "OPENFILE AccountFile FOR RANDOM", "Hash(Customer.AccountNumber)", "SEEK AccountFile, Location", "GETRECORD AccountFile, Customer"]) + "</p>" + pc('''AccountFile ← "AccountRecords.dat"
OPENFILE AccountFile FOR RANDOM
OUTPUT "Please enter an account number"
INPUT Customer.AccountNumber
Location ← Hash(Customer.AccountNumber)
SEEK AccountFile, Location
GETRECORD AccountFile, Customer
OUTPUT Customer
CLOSEFILE AccountFile'''),
  "Missing the SEEK. Without it GETRECORD reads from wherever the pointer already is.") + peq(SRC("w23", "32", "Q12(b)"), "7 marks", "Complete",
  "A pseudocode algorithm searches for a customer record in the random file AccountRecord.dat. A user inputs the name of the customer. The records use the type TAccount (AccountNumber : INTEGER, Name, Address, Telephone : STRING). If the record is found it is output, otherwise an error message is displayed. Complete the file-handling pseudocode." + qcode('''MaxSize ← 1000
OPENFILE ...
Location ← 1
...  ← FALSE
OUTPUT "Enter the customer's name"
...
... AND Location <= MaxSize
   ... "AccountRecord.dat", ...
   GETRECORD "AccountRecord.dat", Customer
   IF SearchCustomer = Customer.Name THEN
      OUTPUT "Customer found: "
      OUTPUT Customer
      FoundFlag ← TRUE
   ENDIF
   Location ← Location + 1
ENDWHILE
IF NOT FoundFlag THEN
   OUTPUT "..."
ENDIF'''),
  "A search loop with a flag: stop when found or when the end of the file is reached.",
  "<p>One mark for each correctly completed blank (maximum 7): " + mks(['OPENFILE "AccountRecord.dat" FOR RANDOM', "FoundFlag", "INPUT SearchCustomer", "WHILE NOT FoundFlag", "SEEK", "Location", "OUTPUT \"Customer does not exist.\""]) + "</p>" + pc('''OPENFILE "AccountRecord.dat" FOR RANDOM
Location ← 1
FoundFlag ← FALSE
OUTPUT "Enter the customer's name"
INPUT SearchCustomer
WHILE NOT FoundFlag AND Location <= MaxSize
   SEEK "AccountRecord.dat", Location
   GETRECORD "AccountRecord.dat", Customer
   IF SearchCustomer = Customer.Name THEN
      OUTPUT "Customer found: "
      OUTPUT Customer
      FoundFlag ← TRUE
   ENDIF
   Location ← Location + 1
ENDWHILE
IF NOT FoundFlag THEN
   OUTPUT "Customer does not exist."
ENDIF'''),
  "Not closing the file, or leaving the flag unset so the loop never uses it.") + peq(SRC("s25", "31", "Q12"), "5 marks", "Complete",
  "The pseudocode algorithm checks whether a location in a stock file StockList.dat is empty or not. The location is given by the user. If the location is empty, a suitable message is displayed, otherwise the item stored at that location is displayed. Complete this file-handling pseudocode algorithm." + qcode('''DECLARE Location : INTEGER
DECLARE Item : STRING
DECLARE Continue : BOOLEAN
DECLARE Answer : CHAR
Continue ← TRUE
OPENFILE ...
WHILE Continue
   OUTPUT "Enter a location between 1 and 500: "
   INPUT Location
   ...
   GETRECORD ...
   IF Item = "" THEN
      OUTPUT "This record is missing."
   ELSE
      OUTPUT "The item in stock is ", ...
   ENDIF
   OUTPUT "Another location (Y or N)?"
   INPUT Answer
   IF Answer <> 'Y' THEN
      Continue ← FALSE
   ENDIF
ENDWHILE
...
OUTPUT "End of program"'''),
  "Open once before the loop, SEEK and GETRECORD inside it, close after it.",
  "<p>One mark for each correctly completed line (maximum 5): " + mks(['OPENFILE "StockList.dat" FOR RANDOM', 'SEEK "StockList.dat", Location', 'GETRECORD "StockList.dat", Item', "OUTPUT \"The item in stock is \", Item", 'CLOSEFILE "StockList.dat"']) + "</p>" + pc('''OPENFILE "StockList.dat" FOR RANDOM
WHILE Continue
   OUTPUT "Enter a location between 1 and 500: "
   INPUT Location
   SEEK "StockList.dat", Location
   GETRECORD "StockList.dat", Item
   ...
ENDWHILE
CLOSEFILE "StockList.dat"
OUTPUT "End of program"'''),
  "Placing CLOSEFILE inside the loop, so the file is closed after the first location checked.") + peq(SRC("s25", "32", "Q13"), "5 marks", "Complete",
  "The pseudocode uses random file access to copy 50 records from a live file CurrentResults.dat to a stored file StoredResults.dat one record at a time, using the type StudentResult (LastName, FirstName, ExamGrade : STRING). If any grades are missing in CurrentResults.dat, the text \"Missing grade\" is put in the ExamGrade field in StoredResults.dat. Complete this file-handling pseudocode." + qcode('''DECLARE Grade : StudentResult
DECLARE Position : INTEGER
...
OPENFILE "StoredResults.dat" FOR RANDOM
...
   SEEK "CurrentResults.dat", Position
   GETRECORD "CurrentResults.dat", Grade
   IF Grade.ExamGrade = "" THEN
      ...
   ENDIF
   ...
   ...
NEXT Position
CLOSEFILE "CurrentResults.dat"
CLOSEFILE "StoredResults.dat"'''),
  "Two files open, so two OPENFILE statements. A FOR loop over 50 positions. Replace a blank grade, then SEEK and PUTRECORD in the stored file.",
  "<p>One mark for each correctly completed line: " + mks(['OPENFILE "CurrentResults.dat" FOR RANDOM', "FOR Position ← 1 TO 50", 'Grade.ExamGrade ← "Missing grade"', 'SEEK "StoredResults.dat", Position', 'PUTRECORD "StoredResults.dat", Grade']) + "</p>" + pc('''OPENFILE "CurrentResults.dat" FOR RANDOM
OPENFILE "StoredResults.dat" FOR RANDOM
FOR Position ← 1 TO 50
   SEEK "CurrentResults.dat", Position
   GETRECORD "CurrentResults.dat", Grade
   IF Grade.ExamGrade = "" THEN
      Grade.ExamGrade ← "Missing grade"
   ENDIF
   SEEK "StoredResults.dat", Position
   PUTRECORD "StoredResults.dat", Grade
NEXT Position
CLOSEFILE "CurrentResults.dat"
CLOSEFILE "StoredResults.dat"'''),
  "Writing to the stored file without a SEEK first. PUTRECORD writes at the pointer, which is not Position.") + peq(SRC("s25", "33", "Q11"), "5 marks", "Complete",
  "The pseudocode allows a user to input a new stock item. The random file is searched for the next empty location and the new item is inserted there. A suitable message is displayed if the file is full. Complete this pseudocode." + qcode('''Max ← 100000
Stored ← FALSE
Location ← 1
...
OUTPUT "Enter the new item you wish to store: "
INPUT NewStock
WHILE NOT Stored AND Location <= Max
   ...
   GETRECORD "StockList.dat", ...
   IF CurrentStock = "" THEN
      ... "StockList.dat", NewStock
      Stored ← TRUE
   ELSE
      Location ← Location + 1
   ENDIF
ENDWHILE
IF ... THEN
   OUTPUT "The new item has not been stored as the file was full."
ENDIF
...'''),
  "Find the first empty location by reading each one in turn; the empty one is where PUTRECORD stores the item.",
  "<p>One mark for each correctly completed line: " + mks(['OPENFILE "StockList.dat" FOR RANDOM', 'SEEK "StockList.dat", Location', "GETRECORD ..., CurrentStock", 'PUTRECORD "StockList.dat", NewStock', "IF Stored = FALSE THEN ... CLOSEFILE \"StockList.dat\""]) + "</p>" + pc('''OPENFILE "StockList.dat" FOR RANDOM
...
WHILE NOT Stored AND Location <= Max
   SEEK "StockList.dat", Location
   GETRECORD "StockList.dat", CurrentStock
   IF CurrentStock = "" THEN
      PUTRECORD "StockList.dat", NewStock
      Stored ← TRUE
   ELSE
      Location ← Location + 1
   ENDIF
ENDWHILE
IF Stored = FALSE THEN
   OUTPUT "The new item has not been stored as the file was full."
ENDIF
CLOSEFILE "StockList.dat"'''),
  "Putting the record with PUTRECORD without having done SEEK to the empty location in this pass of the loop.") + peq(SRC("s26", "32", "Q10(b)"), "6 marks", "Complete",
  "A temperature in degrees Celsius is recorded every minute for one day in a random file, Temperatures.dat. The position of each temperature corresponds to the number of minutes after midnight (10:00 am is at position 600). Complete the algorithm to check a temperature, by passing its position in the file as a parameter and using file-handling commands to find the data item. If it is above freezing return \"Not freezing\", otherwise \"Freezing\". Some blank lines may not be used." + qcode('''FUNCTION TempCheck( ...
   DECLARE Temperature : REAL
   DECLARE Response : STRING
   OPENFILE ...
   ...
   ...
   ...
ENDFUNCTION'''),
  "Header with the parameter and return type, open, SEEK, GETRECORD, IF, CLOSE, RETURN. The close must come before the RETURN.",
  "<p>Up to six marks: " + mks(["correct FUNCTION header", "OPENFILE statement", "SEEK with the position", "GETRECORD into Temperature", "a complete IF ... ELSE ... ENDIF that gives the right messages", "CLOSEFILE before the RETURN (and a correct RETURN)"]) + "</p>" + pc('''FUNCTION TempCheck(Position : INTEGER) RETURNS STRING
   DECLARE Temperature : REAL
   DECLARE Response : STRING
   OPENFILE "Temperatures.dat" FOR RANDOM
   SEEK "Temperatures.dat", Position
   GETRECORD "Temperatures.dat", Temperature
   IF Temperature > 0 THEN
      Response ← "Not freezing"
   ELSE
      Response ← "Freezing"
   ENDIF
   CLOSEFILE "Temperatures.dat"
   RETURN Response
ENDFUNCTION'''),
  "Writing RETURN before CLOSEFILE. The function ends at the RETURN, so the file is never closed.") + '''
  <h3>Paper 4: reading and writing text files in Python</h3>
''' + peq(SRC("s22", "41, 43", "Q1(b), (f)"), "6 + 4 marks", "Write",
  "The text file HighScore.txt stores the top ten players in a game in descending order of score. For each player it stores the 3-character name and the integer score, in the order: player, score (two lines per player). The program stores the players and scores in the global array FileData, 11 rows and 2 columns, declared as <code>FileData = [[\"\"] * 2 for i in range(11)]</code>. (b) The procedure ReadHighScores() opens HighScore.txt and reads the data into the data structure. Use exception handling. Write program code for ReadHighScores(). (f) The procedure WriteTopTen() stores the new top ten player names and scores in a text file called NewHighScore.txt. Write program code for WriteTopTen().",
  "(b) read two lines for each of 10 players. (f) write two lines for each, with a new line after each value. Use try/except round the file handling.",
  "<p><b>(b)</b> Up to six marks: " + mks(["procedure header", "opening the text file to read", "looping 10 times, or to the end of the file", "reading each pair of lines", "storing player name and score in the data structure", "closing the file"]) + " plus try and catch on the file handling with suitable output (maximum 6 in total).</p>" + pc('''def ReadHighScores():
    Filename = "HighScore.txt"
    try:
        File = open(Filename, "r")
        for x in range(0, 10):
            FileData[x][0] = File.readline()[:3]       # player name
            FileData[x][1] = File.readline().strip()   # score
        File.close()
    except IOError:
        print("File not found")''') + "<p><b>(f)</b> Four marks: " + mks(["procedure header, opening NewHighScore.txt to write", "closing the file", "looping through all 10 array values", "writing the player name, then the score"], "a") + " and exception handling with an appropriate output.</p>" + pc('''def WriteTopTen():
    try:
        File = open("NewHighScore.txt", "w")
        for x in range(0, 10):
            File.write(str(FileData[x][0]) + "\\n")
            File.write(str(FileData[x][1]) + "\\n")
        File.close()
    except IOError:
        print("Cannot write to file")''', 12),
  "Using <code>readline()</code> without <code>strip()</code> and comparing the score as a number, or leaving off the <code>\\n</code> so the two values are joined on one line.") + peq(SRC("w25", "42", "Q3(d)"), "5 marks", "Write",
  "The procedure WriteAllToFile() stores the content of TreeArray in a new text file with the filename Tree.txt. The file is not provided. Each node in TreeArray is stored on one line with a comma separating each value. For example, if the rows of the 50-row array are (−1, 20, 1), (−1, 30, −1) and so on, the file will contain the lines <code>−1,20,1</code> and <code>−1,30,−1</code> and so on. Write program code for WriteAllToFile(). Include exception handling when writing to the file.",
  "A loop over the 50 rows, build one string with commas and a new line, and write it. Try and except round it.",
  "<p>One mark each: " + mks(["procedure header with exception handling for writing (try / except with a message)", "opening Tree.txt to write and closing it in an appropriate place", "looping through each element of the array", "creating the correct string", "writing each string to the file"]) + "</p>" + pc('''def WriteAllToFile():
    try:
        File = open("Tree.txt", "w")
        for x in range(0, 50):
            Line = str(TreeArray[x][0]) + "," + str(TreeArray[x][1]) + "," + str(TreeArray[x][2]) + "\\n"
            File.write(Line)
        File.close()
    except:
        print("Cannot write to file")'''),
  "Forgetting <code>str()</code> on the numbers, or leaving out the commas, which are part of the file format.")

review = req("2 marks", "Distinguish", "Distinguish between opening a file for WRITE and opening it for APPEND.", "What happens to the data already in the file?",
  "<p>" + mks(["WRITE creates the file, or replaces the existing contents, so earlier data is lost.", "APPEND keeps the existing contents and adds the new data at the end."]) + "</p>", "Saying write 'adds' data. It overwrites.") + req("3 marks", "Complete", "Scores.txt holds one integer on each line. Write pseudocode to output the total of all the scores in the file.", "Read until the end of the file, converting nothing in pseudocode but adding to a total.",
  "<p>" + mks(["OPENFILE \"Scores.txt\" FOR READ and CLOSEFILE", "WHILE NOT EOF(\"Scores.txt\") with READFILE inside", "Total ← Total + Score, with Total set to 0 first, and output"]) + "</p>" + pc('''Total ← 0
OPENFILE "Scores.txt" FOR READ
WHILE NOT EOF("Scores.txt")
   READFILE "Scores.txt", Score
   Total ← Total + Score
ENDWHILE
CLOSEFILE "Scores.txt"
OUTPUT Total'''), None) + req("3 marks", "Write", "Write Python to read the numbers in Scores.txt into the list Scores and then print the largest.", "Convert each line to an integer.",
  "<p>" + mks(["opening the file to read and closing it", "reading each line and appending int(Line) to the list", "outputting the largest value, e.g. print(max(Scores))"]) + "</p>" + pc('''Scores = []
File = open("Scores.txt", "r")
for Line in File:
    Scores.append(int(Line))
File.close()
print(max(Scores))'''), "Appending the line without <code>int()</code>: <code>max</code> would then compare strings, so \"9\" beats \"10\".") + req("2 marks", "Explain", "Explain why a random file is better than a serial file for finding one customer's record in a very large file.", "Searching against going straight there.",
  "<p>" + mks(["In a serial file records must be read one after another from the start until the one wanted is found.", "In a random file the record's location is calculated (for example by a hash), so SEEK moves straight to it without reading the others."]) + "</p>", None) + req("4 marks", "Write", "Write pseudocode to store the string \"Sold\" in location 25 of the random file Stock.dat.", "Open, SEEK, PUTRECORD, close.",
  "<p>" + mks(['OPENFILE "Stock.dat" FOR RANDOM', 'SEEK "Stock.dat", 25', 'PUTRECORD "Stock.dat", "Sold"', 'CLOSEFILE "Stock.dat"']) + "</p>" + pc('''OPENFILE "Stock.dat" FOR RANDOM
SEEK "Stock.dat", 25
PUTRECORD "Stock.dat", "Sold"
CLOSEFILE "Stock.dat"'''), "Using WRITEFILE. WRITEFILE is for text files; PUTRECORD is for random files.") + req("2 marks", "State", "A text file holds names in alphabetical order. State the file organisation, and one drawback of inserting a new name in the right place.", "Ordered by a key.",
  "<p>" + mks(["Sequential", "The new record cannot just be added to the end: the file must be rewritten (copied) with the record inserted in the correct position."]) + "</p>", None)

exam = exam20("Part 1 is real 9618 questions on file processing: Paper 3 pseudocode for text and random files, and Paper 4 Python for text files. Part 2 is a set of review questions for practice; they are not in exam format.", where, past, review)

tips = tips_html([
  ("Match the file to the command.", "Text files: READFILE and WRITEFILE. Random files: SEEK with GETRECORD and PUTRECORD."),
  ("Open once, close once.", "OPENFILE before the loop, CLOSEFILE after it. Close every file you opened."),
  ("SEEK first.", "In a random file, SEEK to the position before every GETRECORD and PUTRECORD."),
  ("Pick the right mode.", "READ to read. WRITE replaces. APPEND adds. RANDOM to jump about."),
  ("Check what the loop depends on.", "'Until the end of the file' is EOF. A set number of records is a FOR loop."),
  ("Convert what you read.", "Lines are strings: int(Line), and strip() the newline."),
  ("Convert what you write.", "write() takes a string: str(value) + \"\\n\"."),
], [
  ("read until the end of the file", "WHILE NOT EOF(\"File.txt\") with READFILE inside the loop."),
  ("go straight to a record", "SEEK File, Location, then GETRECORD File, Item."),
  ("add to a file without losing data", "Open it FOR APPEND, then WRITEFILE."),
  ("save the changes", "CLOSEFILE, so the data is written to the file."),
], [("Complete", "Fill in the missing lines of the given pseudocode."), ("Write program code", "Produce Python that opens, reads or writes and closes the file."), ("Explain", "Say why one organisation suits a task, with a reason."), ("State", "Give the file mode or organisation asked for.")]) + FC

js = AKJS + AK20JS + r'''
(function () {
  const lines = ["Ana", "Ben", "Cho", "Dev", "Eli"];
  const draw = (s) => {
    const k = Math.round(s.i); let o = SV.text(30, 22, "Names.txt", "sm");
    lines.forEach((l, i) => { o += SV.rect(30, 30 + i * 40, 160, 34, i === k - 1 ? "cell-warn" : i < k - 1 ? "cell-ok" : "cell", { rx: 6 }) + SV.text(46, 53 + i * 40, l, "lbl", { style: "font-family:var(--mono);font-size:15px" }); });
    if (k >= 1 && k <= 5) o += SV.text(200, 53 + (k - 1) * 40, "◀ file pointer", "sm");
    o += SV.text(300, 22, "Names array", "sm");
    for (let i = 0; i < 5; i++) o += memCell(300, 30 + i * 40, i, i < k ? lines[i] : "", i === k - 1 ? "cell-warn" : "f3", 1, 160, 34);
    o += SV.text(520, 60, "Line", "sm") + SV.rect(520, 66, 140, 40, "f2", { rx: 6, ...op(0.55) }) + SV.text(590, 93, k >= 1 && k <= 5 ? lines[k - 1] : "", "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:17px" });
    if (k >= 6) o += SV.text(520, 150, "end of file", "lbl bd t3") + SV.text(520, 172, "the loop stops", "sm");
    return o;
  };
  Lib.stepper($("#stA"), { w: 760, h: 250, label: "Reading a text file into an array", base: { i: 0 }, draw, tween: 400, dwell: 2600, steps: [
    { cap: "<code>OPENFILE \"Names.txt\" FOR READ</code>: the pointer is at the start. The array is empty.", s: { i: 0 } },
    { cap: "<code>READFILE</code> reads line 1 into <code>Line</code> and moves the pointer on. <code>Line</code> is added to the array.", s: { i: 1 } },
    { cap: "The loop reads line 2, then adds it. One line each time round.", s: { i: 2 } },
    { cap: "Line 3.", s: { i: 3 } },
    { cap: "Line 4.", s: { i: 4 } },
    { cap: "Line 5. The pointer is now at the end.", s: { i: 5 } },
    { cap: "<code>EOF(\"Names.txt\")</code> is now true, so <code>WHILE NOT EOF</code> stops. <code>CLOSEFILE</code> then closes the file.", s: { i: 6 } }] });
})();

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); let o = "";
    const box = (x, title, rows, cls) => SV.text(x, 22, title, "sm") + rows.map((r, i) => SV.rect(x, 30 + i * 36, 150, 30, cls, { rx: 6 }) + SV.text(x + 14, 51 + i * 36, r, "lbl", { style: "font-family:var(--mono);font-size:14px" })).join("");
    o += box(20, "Before", ["Ana", "Ben", "Cho"], "cell");
    const w = k >= 2 ? ["Dev"] : ["Ana", "Ben", "Cho"], a = k >= 1 ? ["Ana", "Ben", "Cho", "Dev"] : ["Ana", "Ben", "Cho"];
    o += box(230, "After FOR WRITE \"Dev\"", k >= 2 ? ["Dev"] : ["(open)"], k >= 2 ? "cell-no" : "cell");
    o += box(480, "After FOR APPEND \"Dev\"", k >= 1 ? ["Ana", "Ben", "Cho", "Dev"] : ["(open)"], k >= 1 ? "cell-ok" : "cell");
    if (k >= 2) o += SV.text(230, 190, "old lines lost", "lbl bd t2") + SV.text(480, 190, "old lines kept, Dev added at the end", "lbl bd t3");
    return o;
  };
  Lib.stepper($("#stB"), { w: 760, h: 215, label: "Write against append", base: { i: 0 }, draw, tween: 350, dwell: 3000, steps: [
    { cap: "The file Names.txt already holds Ana, Ben and Cho. The program wants to add the line Dev.", s: { i: 0 } },
    { cap: "Opened <b>FOR APPEND</b>, the existing lines are kept and <code>WRITEFILE</code> adds Dev at the <b>end</b>.", s: { i: 1 } },
    { cap: "Opened <b>FOR WRITE</b>, the file is emptied first, so after writing Dev only <b>Dev</b> is left. Choose WRITE only when the whole file is being replaced.", s: { i: 2 } }] });
})();

(function () {
  const src = ["Eli", "", "Fay", "", "Gus"];
  const draw = (s) => {
    const k = Math.round(s.i); let o = SV.text(30, 22, "ActiveFile.txt", "sm") + SV.text(330, 22, "ArchiveFile.txt", "sm");
    src.forEach((l, i) => { o += SV.rect(30, 30 + i * 38, 220, 32, i === k - 1 ? "cell-warn" : "cell", { rx: 6 }) + SV.text(44, 52 + i * 38, l === "" ? "(blank)" : l, "lbl", { style: "font-family:var(--mono);font-size:14px" }); });
    for (let i = 0; i < Math.min(5, k); i++) { const t = src[i] === "" ? "Account not present" : src[i]; o += SV.rect(330, 30 + i * 38, 260, 32, src[i] === "" ? "cell-ok" : "f3", { rx: 6 }) + SV.text(344, 52 + i * 38, t, "lbl", { style: "font-family:var(--mono);font-size:14px" }); }
    if (k >= 1 && k <= 5) o += SV.text(620, 52 + (k - 1) * 38, "READFILE: " + (src[k - 1] === "" ? "\"\"" : src[k - 1]), "sm");
    if (k >= 6) o += SV.text(330, 240, "EOF reached: both files closed", "lbl bd t3");
    return o;
  };
  Lib.stepper($("#stC"), { w: 760, h: 255, label: "Copying a file and replacing blank lines", base: { i: 0 }, draw, tween: 300, dwell: 2400, steps: [
    { cap: "Both files are opened: Active for READ, Archive for WRITE. The loop runs until <code>EOF(\"ActiveFile.txt\")</code>.", s: { i: 0 } },
    { cap: "Line 1 is not blank: <code>WRITEFILE</code> copies it.", s: { i: 1 } },
    { cap: "Line 2 is blank, so the IF is true: <code>WRITEFILE ... \"Account not present\"</code>.", s: { i: 2 } },
    { cap: "Line 3 is copied.", s: { i: 3 } },
    { cap: "Line 4 is blank: replaced.", s: { i: 4 } },
    { cap: "Line 5 is copied.", s: { i: 5 } },
    { cap: "The end of the file is reached. Both files must be closed: <code>CLOSEFILE</code> twice.", s: { i: 6 } }] });
})();

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); let o = "";
    o += SV.text(30, 30, "Serial / sequential: read from the start", "lbl bd") + SV.rect(30, 40, 700, 26, "cell", { rx: 6 });
    const w = k >= 1 ? Math.min(1, s.p) * 600 : 0;
    o += SV.rect(30, 40, w + 2, 26, "f3", { rx: 6, ...op(0.7) }) + SV.text(30, 90, k >= 1 ? "records read: " + Math.round(s.p * 600) + " before record 600 is reached" : "", "sm");
    o += SV.text(30, 140, "Random: SEEK straight to the position", "lbl bd") + SV.rect(30, 150, 700, 26, "cell", { rx: 6 });
    if (k >= 2) o += SV.rect(30 + 600 - 2, 150, 6, 26, "cell-ok", { rx: 3 }) + arrow(632, 200, 632, 180, "u", "c2", 1) + SV.text(730, 222, "SEEK 600, then GETRECORD: 1 record read", "lbl bd t3", { "text-anchor": "end" });
    return o;
  };
  Lib.stepper($("#stD"), { w: 760, h: 240, label: "Serial against random access", base: { i: 0, p: 0 }, draw, tween: 1200, dwell: 3500, steps: [
    { cap: "The temperature at position <b>600</b> is wanted from a file of 1440 records.", s: { i: 0, p: 0 } },
    { cap: "In a <b>serial</b> or <b>sequential</b> file the program reads from the start: 599 records are read and thrown away before the 600th.", s: { i: 1, p: 1 } },
    { cap: "In a <b>random</b> file, <code>SEEK</code> moves the pointer straight to position 600 and <code>GETRECORD</code> reads it. One read.", s: { i: 2, p: 1 } }] });
})();

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); let o = "";
    o += SV.text(30, 28, "AccountNumber = 4719", "lbl bd", { style: "font-family:var(--mono);font-size:16px" });
    if (k >= 1) o += SV.text(30, 62, "Location ← Hash(4719) = 4719 MOD 11 = 6", "lbl", { style: "font-family:var(--mono);font-size:15px" });
    if (k >= 2) o += SV.text(30, 92, "SEEK AccountFile, 6", "lbl", { style: "font-family:var(--mono);font-size:15px" });
    for (let i = 0; i < 11; i++) o += memCell(430, 20 + i * 21, i, i === 6 && k >= 3 ? "4719 Hall" : i === 2 ? "1202 Ito" : i === 9 ? "7745 Ray" : "", i === 6 && k >= 2 ? "cell-warn" : "f3", 1, 280, 19);
    if (k >= 3) o += SV.text(30, 122, "GETRECORD AccountFile, Customer", "lbl", { style: "font-family:var(--mono);font-size:15px" }) + SV.text(30, 152, "Customer = 4719 Hall", "lbl bd t3", { style: "font-family:var(--mono);font-size:16px" });
    return o;
  };
  Lib.stepper($("#stE"), { w: 760, h: 260, label: "Finding a record in a random file with a hash", base: { i: 0 }, draw, tween: 400, dwell: 3200, steps: [
    { cap: "A customer enters an account number. The file has 11 locations, numbered 0 to 10.", s: { i: 0 } },
    { cap: "The hash function turns the key into a location: 4719 MOD 11 = <b>6</b>.", s: { i: 1 } },
    { cap: "<code>SEEK</code> moves the file pointer to location 6.", s: { i: 2 } },
    { cap: "<code>GETRECORD</code> reads the record there into <code>Customer</code>. No other record was read.", s: { i: 3 } }] });
})();

/* Lab 1 */
(function () {
  let mode = 0, exists = true;
  const modes = ["READ", "WRITE", "APPEND"];
  const paint = () => {
    $$("#mB button").forEach((b, i) => b.classList.toggle("pri", i === mode)); $$("#mE button").forEach((b, i) => b.classList.toggle("pri", (i === 0) === exists));
    let rows, msg;
    if (mode === 0) { rows = exists ? ["Ana", "Ben", "Cho"] : null; msg = exists ? "FOR READ: the contents are unchanged. WRITEFILE is not allowed on a file opened for reading, so Dev is not added." : "FOR READ: the file does not exist, so the OPENFILE fails. This is the case exception handling is for."; }
    if (mode === 1) { rows = ["Dev"]; msg = exists ? "FOR WRITE: the old lines are lost. Only Dev is in the file." : "FOR WRITE: a new file is created containing only Dev."; }
    if (mode === 2) { rows = exists ? ["Ana", "Ben", "Cho", "Dev"] : ["Dev"]; msg = exists ? "FOR APPEND: the old lines are kept and Dev is added at the end." : "FOR APPEND: the file is created, and Dev is its first line."; }
    $("#mO").innerHTML = rows ? '<div class="tw"><table class="t mono"><tr><th>Names.txt afterwards</th></tr>' + rows.map((r) => `<tr><td>${r}</td></tr>`).join("") + "</table></div>" : '<div class="tw"><table class="t mono"><tr><th>Names.txt afterwards</th></tr><tr><td>error: file not found</td></tr></table></div>';
    $("#mV").textContent = msg;
  };
  $("#mB").innerHTML = modes.map((m, i) => `<button class="b" data-i="${i}">FOR ${m}</button>`).join(""); $("#mE").innerHTML = '<button class="b">File exists (Ana, Ben, Cho)</button><button class="b">File does not exist</button>';
  $$("#mB button").forEach((b) => (b.onclick = () => { mode = +b.dataset.i; paint(); })); $$("#mE button").forEach((b, i) => (b.onclick = () => { exists = i === 0; paint(); }));
  paint();
})();

/* Lab 2 */
(function () {
  const data = [12, 7, 30, 5, 18]; let st;
  const reset = () => { st = { pc: 0, ptr: 0, line: "", total: 0, open: false, msg: "Press Step to run the first statement." }; paint(); };
  const prog = ["OPENFILE \"Scores.txt\" FOR READ", "WHILE NOT EOF(\"Scores.txt\")", "   READFILE \"Scores.txt\", Line", "   Total ← Total + Line", "ENDWHILE", "CLOSEFILE \"Scores.txt\"", "OUTPUT Total"];
  const paint = () => {
    $("#rS").innerHTML = '<div class="code"><pre class="cp">' + prog.map((l, i) => `<span class="ln${i === st.pc ? " on" : ""}">${l.replace(/&/g, "&amp;").replace(/</g, "&lt;")}</span>`).join("") + '</pre></div><div class="tw"><table class="t mono"><tr><th>pointer</th><th>Line</th><th>Total</th><th>EOF?</th></tr><tr><td>' + st.ptr + " of 5</td><td>" + st.line + "</td><td>" + st.total + "</td><td>" + (st.open ? (st.ptr >= 5) : "-") + "</td></tr></table></div>";
    $("#rV").textContent = st.msg;
  };
  $("#rN").onclick = () => {
    const p = st.pc;
    if (p === 0) { st.open = true; st.msg = "File opened for reading, pointer at the start."; st.pc = 1; }
    else if (p === 1) { if (st.ptr >= 5) { st.msg = "EOF is true: leave the loop."; st.pc = 5; } else { st.msg = "Not at the end of the file: enter the loop."; st.pc = 2; } }
    else if (p === 2) { st.line = data[st.ptr]; st.ptr++; st.msg = "READFILE reads " + st.line + " and moves the pointer on."; st.pc = 3; }
    else if (p === 3) { st.total += st.line; st.msg = "Total is now " + st.total + "."; st.pc = 1; }
    else if (p === 5) { st.open = false; st.msg = "File closed."; st.pc = 6; }
    else if (p === 6) { st.msg = "OUTPUT " + st.total + ": the sum of 12 + 7 + 30 + 5 + 18."; st.pc = 7; }
    paint();
  };
  $("#rR").onclick = reset; reset();
})();

/* Lab 3 */
(function () {
  let key = 4719;
  const slots = { 2: "1202 Ito", 9: "7745 Ray", 6: "4719 Hall" };
  const paint = () => {
    const loc = key % 11;
    $("#hT").innerHTML = '<div class="tw"><table class="t mono"><tr><th>Location</th>' + Array.from({ length: 11 }, (_, i) => `<td${i === loc ? ' style="background:var(--warn-soft);font-weight:700"' : ""}>${i}</td>`).join("") + "</tr><tr><th>Stored</th>" + Array.from({ length: 11 }, (_, i) => `<td>${slots[i] ? slots[i].split(" ")[0] : ""}</td>`).join("") + "</tr></table></div>";
    const occ = slots[loc];
    $("#hV").innerHTML = `Hash(${key}) = ${key} MOD 11 = <b>${loc}</b>. ` + (occ ? (occ.startsWith(key + " ") ? "SEEK " + loc + " finds the record for this account." : `Location ${loc} is already used by account ${occ.split(" ")[0]}: a <b>collision</b>, so another method is needed to place this record.`) : `Location ${loc} is empty, so a new record would be stored here.`);
  };
  Lib.slider($("#hS"), { id: "hsl", label: "Account number ", min: 1000, max: 9999, value: key, fmt: (x) => x, onInput: (v) => { key = v; paint(); } });
  paint();
})();
''' + CLASSIFY("cl1", "Which open mode or file command fits?", ["Read a text file", "Replace a text file", "Add to a text file", "Random file"],
  [("OPENFILE \"Data.txt\" FOR READ", 0), ("OPENFILE \"Out.txt\" FOR WRITE", 1), ("OPENFILE \"Log.txt\" FOR APPEND", 2), ("SEEK \"Stock.dat\", 25", 3), ("GETRECORD \"Stock.dat\", Item", 3), ("READFILE \"Data.txt\", Line", 0), ("open(\"Log.txt\", \"a\")", 2), ("open(\"Data.txt\", \"r\")", 0), ("open(\"Out.txt\", \"w\")", 1)],
  "r reads, w replaces, a adds. SEEK, GETRECORD and PUTRECORD are for random files.") + CLASSIFY("cl2", "Is it serial, sequential or random?", ["Serial", "Sequential", "Random"],
  [("Records are stored in the order they were added", 0), ("Records are stored in order of a key field", 1), ("The record's location is calculated from its key", 2), ("A new record is simply appended to the end", 0), ("Adding a record means writing a new file with it in the right place", 1), ("SEEK takes you straight to the record", 2)],
  "Serial: order added. Sequential: key order. Random: direct access by address.") + ORDER(
  "Put the steps for processing a text file in order.",
  ["Open the file in the correct mode", "Read the first line", "Process it (add, copy, compare)", "Repeat until the end of the file", "Close the file"],
  "Open, read, process, repeat to EOF, close.") + MATCH([
  ["EOF", "True when there is nothing more to read"], ["SEEK", "Moves the file pointer to a record"], ["GETRECORD", "Reads the record at the pointer"], ["PUTRECORD", "Writes a record at the pointer"], ["CLOSEFILE", "Ends file use and saves written data"]]) + CALC([
  {"q": "A text file has 25 lines. How many times does READFILE run in a loop that reads until the end of the file?", "a": 25, "unit": "", "tol": 0.01, "hint": "One read for each line.", "sol": "<b>25</b>."},
  {"q": "A random file has 500 records and you want record 350. How many records does GETRECORD read after SEEK 350?", "a": 1, "unit": "", "tol": 0.01, "hint": "SEEK moves straight there.", "sol": "<b>1</b>."},
  {"q": "A serial file has 500 records. How many records are read to reach record 350 from the start (including it)?", "a": 350, "unit": "", "tol": 0.01, "hint": "Read 1, 2, ... 350.", "sol": "<b>350</b>."},
  {"q": "Hash(Key) = Key MOD 11. At which location is account number 5000 stored?", "a": 6, "unit": "", "tol": 0.01, "hint": "11 × 454 = 4994, so the remainder is 5000 - 4994.", "sol": "<b>6</b> (5000 MOD 11 = 6)."},
  {"q": "A file is opened FOR APPEND. It has 8 lines. Two WRITEFILE statements run. How many lines does it have after?", "a": 10, "unit": "", "tol": 0.01, "hint": "8 + 2.", "sol": "<b>10</b>."},
  {"q": "A file with 8 lines is opened FOR WRITE and two lines are written. How many lines does it have after?", "a": 2, "unit": "", "tol": 0.01, "hint": "WRITE replaces the old contents.", "sol": "<b>2</b>."}]) + MCQ([
  ("Which statement must come before GETRECORD in a random file?", ["READFILE", "SEEK", "EOF", "OPENFILE FOR APPEND"], 1, "SEEK moves the pointer to the record."),
  ("A program must add new lines to the end of an existing log. Which mode?", ["READ", "WRITE", "APPEND", "RANDOM"], 2, "APPEND keeps the old lines."),
  ("What does EOF tell you?", ["The file is empty", "There is nothing more to read", "The file is closed", "The file is full"], 1, "End of file."),
  ("What type is a line read from a text file in Python?", ["integer", "string", "boolean", "real"], 1, "Convert with int() if you need a number."),
  ("Why must a file be closed?", ["To delete it", "So written data is saved and the file can be reused", "To make it random", "To sort it"], 1, "Closing finishes the writes."),
  ("Which file organisation stores records in order of a key?", ["Serial", "Sequential", "Random", "Text"], 1, "Sequential files are ordered by key.")], "qz1") + CARDS([
  ("OPENFILE ... FOR READ", "Open an existing file to read from the start."), ("... FOR WRITE", "Create or overwrite the file."), ("... FOR APPEND", "Add to the end of the file."), ("... FOR RANDOM", "Open for direct access to records."),
  ("READFILE / WRITEFILE", "Read or write one line of a text file."), ("EOF(File)", "True when no more data to read."), ("SEEK / GETRECORD / PUTRECORD", "Random access: move, read, write."), ("CLOSEFILE", "Always close what you open.")])

build("ac2021", "ac-20-2-1-file-processing", "File Processing: Text, Serial, Sequential and Random Files", EYA("20.2.1"),
  "Opening, reading, writing and closing text files; serial, sequential and random files; SEEK, GETRECORD and PUTRECORD; Python for Paper 4; animations, labs and the real Paper 3 and Paper 4 file questions.",
  dict(sub=CBK("Chapter 20 · Further programming, section 20.2 File processing and exception handling"), **tabs(learn, watch, explore, practise, real, exam, tips)), js)
