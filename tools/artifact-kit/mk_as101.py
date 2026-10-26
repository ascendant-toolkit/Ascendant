"""AS CS 10.1: data types, records and arrays of records. Run: python3 tools/artifact-kit/mk_as101.py"""
from ascs import *
import json

def pc(text, label=None):
    return code(text.strip("\n").split("\n"), label=label)

EMP = [{"n": 123, "name": "Smith,Eric", "dept": "1B", "att": 97.4}, {"n": 124, "name": "Lopez,Ana", "dept": "2A", "att": 88.5}, {"n": -1, "name": "", "dept": "", "att": 0}, {"n": 126, "name": "Okoye,Ben", "dept": "1B", "att": 71.0}, {"n": 127, "name": "Zhang,Cleo", "dept": "3C", "att": 90.0}]

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>Pseudocode has six basic <b>data types</b>: <span class="mono">INTEGER</span> (whole numbers), <span class="mono">REAL</span> (numbers with a decimal point), <span class="mono">CHAR</span> (one character, in single quotes), <span class="mono">STRING</span> (text in double quotes), <span class="mono">BOOLEAN</span> (TRUE or FALSE) and <span class="mono">DATE</span>. A <b>record</b> is a <b>user-defined composite data type</b> that stores items of <b>different data types under one identifier</b>; you declare it with <span class="mono">TYPE ... ENDTYPE</span>, and access a field with <b>dot notation</b>, <span class="mono">Staff[Index].Attendance</span>. A <b>1D array of records</b> stores many records, each reached by an index, so a loop can process every record. Unused array elements are marked with a standard <b>impossible value</b> (for example EmployeeNumber = −1 or an empty string) so they can be skipped when processing. Exam questions ask you to declare the record and the array, state the benefits of an array of records, and write a procedure or function that loops through the array.</p></div>

  <h2>1 · Data types</h2>
  <div class="tw"><table class="t">
    <tr><th>Type</th><th>Stores</th><th>Example</th></tr>
    <tr><td class="mono">INTEGER</td><td>Whole numbers</td><td class="mono">100, −3</td></tr>
    <tr><td class="mono">REAL</td><td>Numbers with a decimal point</td><td class="mono">97.40, 2.9</td></tr>
    <tr><td class="mono">CHAR</td><td>A single character</td><td class="mono">'B'</td></tr>
    <tr><td class="mono">STRING</td><td>Text (zero or more characters)</td><td class="mono">"Catherine", "AB1234"</td></tr>
    <tr><td class="mono">BOOLEAN</td><td>TRUE or FALSE</td><td class="mono">FALSE</td></tr>
    <tr><td class="mono">DATE</td><td>A date; made with <span class="mono">SETDATE(d, m, y)</span>; read with <span class="mono">DAY()</span>, <span class="mono">MONTH()</span>, <span class="mono">YEAR()</span>, <span class="mono">DAYINDEX()</span></td><td class="mono">25/12/2020</td></tr>
  </table></div>
  <p>Choose the type from the example value and the comment: an ID with letters and digits is STRING; a numeric value used as an array index is INTEGER; a percentage like 97.40 is REAL; a "letter to indicate a stage" is CHAR; "TRUE when ..." is BOOLEAN; "when the rental starts" is DATE.</p>

  <h2>2 · Records</h2>
  ''' + pc('''
TYPE Employee
   DECLARE EmployeeNumber : INTEGER
   DECLARE Name : STRING
   DECLARE Department : STRING
   DECLARE Born : DATE
   DECLARE Attendance : REAL
ENDTYPE

DECLARE Staff : ARRAY [1:500] OF Employee
Staff[3].Attendance ← 92.5
OUTPUT Staff[3].Name''') + '''
  <p><b>Benefits of an array of records:</b> different data types are held for each item under a single identifier; a loop can go through every record (iteration) and an index gives direct access to one record; the code is simpler, with less duplication, so it is easier to write, understand, test and maintain.</p>
  <p><b>Unused elements.</b> If the array is bigger than the number of records, mark unused elements in a standard way: give a field an impossible value (an EmployeeNumber less than 1, an empty string for the name, a weight of zero or less). It is good practice because unused elements can then be recognised when processing or searching; otherwise they may contain old or unexpected data.</p>

  <h2>3 · Processing an array of records</h2>
  <p>The standard pattern: declare a loop counter, loop through every element, <b>skip unused records</b>, test the field with dot notation, and output or count.</p>
  ''' + pc('''
PROCEDURE Absentees()
   DECLARE Index : INTEGER
   FOR Index ← 1 TO 500
      IF Staff[Index].EmployeeNumber <> -1 THEN
         IF Staff[Index].Attendance <= 90 THEN
            OUTPUT Staff[Index].EmployeeNumber
            OUTPUT Staff[Index].Name
         ENDIF
      ENDIF
   NEXT Index
ENDPROCEDURE''') + '''

  <h2>Common ways to lose marks</h2>
  <ul>
    <li>Declaring a numeric ID like "AB1234" as INTEGER, or a percentage as INTEGER instead of REAL.</li>
    <li>Writing <span class="mono">Staff.Attendance</span> or <span class="mono">Staff[Attendance]</span>. The record is the array element: <span class="mono">Staff[Index].Attendance</span>.</li>
    <li>Forgetting <span class="mono">ENDTYPE</span>, or declaring the array without the record type: <span class="mono">ARRAY [1:500] OF Employee</span>.</li>
    <li>Not skipping unused records, or not saying how they are indicated.</li>
    <li>Looping to the wrong limit: loop to the declared size of the array.</li>
  </ul>
'''

watch = '''
  <h2>1 · A record holds mixed types</h2>
  <div id="stA"></div>
  <h2>2 · An array of records</h2>
  <div id="stB"></div>
  <h2>3 · Looping through the array</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Absentees</h2>
  <p>The staff array has five records; one element is unused (EmployeeNumber −1). Change the attendance limit.</p>
  <div class="card"><div id="eS"></div><div id="eG"></div><div id="eV" class="verdict"></div></div>
  <h2>Lab 2 · Which data type?</h2>
  <div class="card"><div id="tB" class="btnrow"></div><div id="tO"></div></div>
  <h2>Lab 3 · Dot notation</h2>
  <div class="card"><div id="dB" class="btnrow"></div><div id="dO"></div></div>
'''

_pr, _prjs = PR(["Which data type?", "Record or array?", "Match the term to its meaning", "Put the declaration in order", "Working out", "Multiple choice"],
  ("Which data type suits the value?", ["INTEGER", "REAL", "CHAR", "STRING", "BOOLEAN", "DATE"], [("123478 (a numeric value used as an array index)", 0), ("13.5 (a value in the range 0 to 100)", 1), ("'B' (a letter for the stage of production)", 2), ("\"AB1234\" (a unique alpha-numeric ID)", 3), ("FALSE (TRUE if the item has been rejected)", 4), ("13/06/2025 (when the rental starts)", 5)], "Match the example and comment."),
  ("Is it a feature of a record or of an array?", ["Record", "Array"], [("Holds fields of different data types", 0), ("Holds many items of the same type", 1), ("Accessed with dot notation", 0), ("Accessed with an index", 1), ("Declared with TYPE ... ENDTYPE", 0), ("Declared with ARRAY [1:500] OF ...", 1)], "Record: mixed types. Array: same type, index."),
  [["Record", "A composite type holding several fields under one identifier"], ["Field", "One item of data inside a record"], ["Dot notation", "Staff[3].Name"], ["Array of records", "Many records reached by an index"], ["Unused element", "Marked with an impossible value"]],
  ("Put the declaration of an array of records in order.", ["TYPE and the record name", "DECLARE each field with its data type", "ENDTYPE", "DECLARE the array with its bounds", "OF the record type"], "Type, fields, ENDTYPE, array, OF type."),
  [{"q": "An array of 500 Employee records has 120 unused elements. How many are in use?", "a": 380, "unit": "", "tol": 0.01, "hint": "500 − 120.", "sol": "<b>380</b>."}, {"q": "A record has 5 fields. How many fields are there in 500 records?", "a": 2500, "unit": "", "tol": 0.01, "hint": "5 × 500.", "sol": "<b>2500</b>."}, {"q": "A loop FOR Index ← 1 TO 500 skips unused records. If 380 are in use, how many are tested?", "a": 380, "unit": "", "tol": 0.01, "hint": "Only used ones.", "sol": "<b>380</b> (the loop passes 500 times; 120 are skipped)."}, {"q": "Attendance values 97.4, 88.5, 71.0 and 90.0 are in use. How many are 90.00 or less?", "a": 3, "unit": "", "tol": 0.01, "hint": "88.5, 71.0, 90.0.", "sol": "<b>3</b>."}, {"q": "An array is declared ARRAY [0:1999]. How many elements?", "a": 2000, "unit": "", "tol": 0.01, "hint": "0 to 1999.", "sol": "<b>2000</b>."}],
  [("A record can store:", ["Different data types", "Only integers", "Only text", "Only one value"], 0, "Different types."), ("A CHAR holds:", ["One character", "Many characters", "A date", "TRUE or FALSE"], 0, "One."), ("Which is valid dot notation?", ["Item[1].Stage", "Item.Stage[1]", "Item[Stage]", "Stage.Item"], 0, "Item[1].Stage."), ("Unused records are marked with:", ["An impossible value", "A random value", "Nothing", "A copy of the last record"], 0, "Impossible value."), ("A percentage such as 97.40 is:", ["REAL", "INTEGER", "CHAR", "BOOLEAN"], 0, "REAL."), ("TYPE must be ended with:", ["ENDTYPE", "END", "NEXT", "ENDIF"], 0, "ENDTYPE.")],
  [("INTEGER / REAL", "Whole / decimal numbers."), ("CHAR / STRING", "One character / text."), ("BOOLEAN / DATE", "TRUE or FALSE / a date."), ("Record", "TYPE ... ENDTYPE; mixed types."), ("Array of records", "Index plus dot notation."), ("Dot notation", "Staff[Index].Name"), ("Unused element", "Standard impossible value."), ("Benefit", "Mixed types, loops, simpler code.")])

real = RWNOTE + (
rw("A school database row", "A student has a name, an ID, a year group and a date of birth: different types in one record, one record per student.", "a record.") +
rw("A contacts list", "Each contact record holds a name, phone number and birthday; the list is an array of those records, so the app can loop through to search.", "array of records.") +
rw("A deleted contact", "Instead of shuffling the list, the app marks the slot as empty so the loop can skip it.", "unused element marked.") +
rw("A game save file", "A player record holds the name (STRING), level (INTEGER), score (REAL) and finished flag (BOOLEAN).", "different data types.") +
rw("Spreadsheet columns", "Each column has a data type: text, number or date. A record is one row.", "fields and records.")
)

where = [
  ("M/J 2021", "22", "1(a), (b)", "4 + 4 + 3", "Data types for four variables; evaluate expressions; tick selection, assignment or iteration"),
  ("O/N 2021", "22", "3", "3 + 2 + 1 + 1 + 7", "Declare a record and an array; unused elements; a procedure that finds the students in a club"),
  ("M/J 2022", "23", "5", "4 + 2 + 2 + 4", "Declare the Employee record and array; unused records; a procedure for absentees"),
  ("M/J 2023", "22", "2", "1 + 2 + 6", "Assign a date; months to the end of the year; the day of the week with an array"),
  ("M/J 2024", "22", "3", "4 + 2 + 3", "Declare the Component record and array; benefits of an array of records"),
  ("M/J 2024", "23", "3(a)", "3 + 1", "Check a weight is in range; indicate an unused array element"),
  ("O/N 2025", "21", "3", "4 + 2 + 3", "Declare RentalRecord and the Rental array; benefits of an array of records"),
  ("O/N 2025", "23", "8(a), (b)", "8 + 7", "Efficient search of a Loan array; count the loans for a tutor"),
  ("M/J 2026", "23", "5(a), (b)", "4 + 7", "Return the summary from a data packet; complete a file search procedure")]

past = '''  <p class="note">These are Paper 2 questions, so answers are written in pseudocode. The mark schemes accept different layouts if the same points are covered. Paper 2 questions are reworded from the papers; check the original paper and mark scheme for the exact wording. The pattern "declare a record and an array, give benefits, then write a procedure" appears in four of the six years.</p>
''' + peq(SRC("s21", "22", "Q1(a)(b)"), "4 + 4 + 3 marks", "Complete / Tick",
  "(a)(i) Give the data type of Name \"Catherine\", Index 100, Modified FALSE, Holiday 25/12/2020. (ii) Evaluate using these values: Modified OR Index > 100; LENGTH(\"Student: \" & Name); INT(Index + 2.9); MID(Name, 1, 3). (b) Tick selection, assignment or iteration for: Index ← Index + 1; IF Modified = TRUE THEN; ENDWHILE.", "STRING, INTEGER, BOOLEAN, DATE. FALSE; 18; 102; \"Cat\".",
  "<p><b>(a)(i)</b> " + mks(["Name: STRING", "Index: INTEGER", "Modified: BOOLEAN", "Holiday: DATE"]) + "</p><p><b>(ii)</b> " + mks(["FALSE", "18", "102", "\"Cat\" (with quotation marks and a capital C)"], "a") + "</p><p><b>(b)</b> " + mks(["Index ← Index + 1: assignment", "IF Modified = TRUE THEN: selection", "ENDWHILE: iteration"], "b") + "</p>", None) + peq(SRC("w21", "22", "Q3"), "3 + 2 + 1 + 1 + 7 marks", "Write",
  "Data about each student is held in a record of type Student with fields StudentID \"CF1234\", Email \"Carmen47@xyzmail.com\", and Club_1, Club_2, Club_3 (1 to 99). (a)(i) Write pseudocode to declare the record. (ii) Declare a 1D array Membership of 3000 elements. (iii) Give a way of indicating an unused array element. (iv) State a way of indicating an unused club field. (b) Write pseudocode for a procedure GetIDs() that prompts and inputs a club number, outputs the StudentID of every student in that club and a count of all students in the club.", "TYPE with STRING and INTEGER fields; ARRAY [1:3000] OF Student; compare all three club fields.",
  "<p><b>(a)(i)</b> " + mks(["TYPE and ENDTYPE", "StudentID and Email as STRING", "All Club fields as INTEGER"]) + "</p>" + pc('''
TYPE Student
   DECLARE StudentID : STRING
   DECLARE Email : STRING
   DECLARE Club_1 : INTEGER
   DECLARE Club_2 : INTEGER
   DECLARE Club_3 : INTEGER
ENDTYPE''') + "<p><b>(ii)</b> " + mks(["DECLARE Membership : ARRAY [1:3000] OF Student"], "a") + "</p><p><b>(iii)</b> " + mks(["Assign an empty string to the StudentID or Email field, or a value out of range to a field"], "b") + " <b>(iv)</b> " + mks(["A number outside the range 1 to 99"], "c") + "</p><p><b>(b)</b> " + mks(["Declare and initialise Count", "Prompt and input the club number before the loop", "Loop through 3000 elements", "Compare one club field with the number input", "Compare all three club fields with the number", "If found output the StudentID and increment Count", "Final output of Count outside the loop"], "d") + "</p>" + pc('''
PROCEDURE GetIDs()
   DECLARE Index : INTEGER
   DECLARE ThisClub, Count : INTEGER
   OUTPUT "Please Input Club Number: "
   INPUT ThisClub
   Count ← 0
   FOR Index ← 1 TO 3000
      IF Membership[Index].Club_1 = ThisClub OR
         Membership[Index].Club_2 = ThisClub OR
         Membership[Index].Club_3 = ThisClub THEN
         Count ← Count + 1
         OUTPUT Membership[Index].StudentID
      ENDIF
   NEXT Index
   OUTPUT "There are ", Count, " students in the club"
ENDPROCEDURE'''), "Comparing only Club_1. A student may be in the club through any of the three fields.") + peq(SRC("s22", "23", "Q5"), "4 + 2 + 2 + 4 marks", "Write",
  "Attendance data for each employee is held in a record of type Employee: EmployeeNumber 123, Name \"Smith,Eric\", Department \"1B\", Born 13/02/2006, Attendance 97.40 (a percentage). (a)(i) Declare the record. (ii) Declare a 1D array Staff of 500 elements. (b)(i) State why it is good practice to have a standard way to indicate unused array elements. (ii) Give one way of indicating an unused record. (c) Write pseudocode for a procedure Absentees() that outputs the EmployeeNumber and Name of all employees with an Attendance of 90.00 or less.", "TYPE Employee; ARRAY [1:500] OF Employee; skip unused; Attendance <= 90.",
  "<p><b>(a)(i)</b> " + mks(["TYPE Employee and ENDTYPE", "EmployeeNumber (INTEGER), Name and Department (STRING)", "Born as DATE", "Attendance as REAL"]) + "</p>" + pc('''
TYPE Employee
   DECLARE EmployeeNumber : INTEGER
   DECLARE Name : STRING
   DECLARE Department : STRING
   DECLARE Born : DATE
   DECLARE Attendance : REAL
ENDTYPE''') + "<p><b>(ii)</b> " + mks(["DECLARE Staff : ARRAY [1:500] OF Employee"], "a") + "</p><p><b>(b)(i)</b> " + mks(["So that unused elements may be recognised when processing or searching; otherwise the element may contain old or unexpected data"], "b") + " <b>(ii)</b> " + mks(["An impossible value, for example EmployeeNumber less than 1, an empty or 'EMPTY' name, or zero or negative attendance"], "c") + "</p><p><b>(c)</b> " + mks(["Procedure heading and ending and a declared loop counter", "Loop through 500 elements", "Attempt to skip unused elements", "Test Staff[Index].Attendance <= 90 in the loop", "Output the EmployeeNumber and Name fields"], "d") + "</p>" + pc('''
PROCEDURE Absentees()
   DECLARE Index : INTEGER
   FOR Index ← 1 TO 500
      IF Staff[Index].EmployeeNumber <> -1 THEN
         IF Staff[Index].Attendance <= 90 THEN
            OUTPUT Staff[Index].EmployeeNumber
            OUTPUT Staff[Index].Name
         ENDIF
      ENDIF
   NEXT Index
ENDPROCEDURE'''), None) + peq(SRC("s23", "22", "Q2"), "1 + 2 + 6 marks", "Write / Describe",
  "A variable MyDOB is of type DATE. (a) Write a statement to assign the value for 17/11/2007 to MyDOB. (b) Write a statement to calculate the number of months from the month of birth until the end of the year and assign it to NumMonths (02/07/2008 gives 5). (c) The program will output the day of the week for MyDOB (22/06/2023 gives \"Thursday\"). An array stores the names of the days. Define the array and describe the algorithm in four steps (no pseudocode).", "SETDATE; 12 − MONTH(MyDOB); a 7-element STRING array and DAYINDEX.",
  "<p><b>(a)</b> " + mks(["MyDOB ← SETDATE(17, 11, 2007)"]) + "</p><p><b>(b)</b> " + mks(["NumMonths ← 12 − MONTH(MyDOB)"], "a") + " (one mark for each underlined part: 12 minus and MONTH(MyDOB))</p><p><b>(c)</b> " + mks(["A 1D array containing 7 elements", "of type STRING", "Step 1: assign \"Sunday\" to the first element, \"Monday\" to the second and so on", "Step 2: use the function DAYINDEX() to return the day number from MyDOB", "Step 3: use the returned value as the array index to access the name", "Step 4: output that element"], "b") + " (max 2 for the array, max 4 for the steps)</p>", None) + peq(SRC("s24", "22", "Q3"), "4 + 2 + 3 marks", "Write / State",
  "Item data is held in a record of type Component: Item_Num 123478 (a numeric array index), Reject FALSE, Stage 'B', Limit_1 13.5, Limit_2 26.4 (0 to 100). (a)(i) Declare the record. (ii) Declare a 1D array Item of 2000 elements. (b) State three benefits of an array of records.", "INTEGER, BOOLEAN, CHAR, REAL, REAL. Iteration; direct access; simpler code.",
  "<p><b>(a)(i)</b> " + mks(["TYPE Component and ENDTYPE", "Item_Num and Reject fields (INTEGER, BOOLEAN)", "The Stage field (CHAR)", "The Limit fields as REAL"]) + "</p>" + pc('''
TYPE Component
   DECLARE Item_Num : INTEGER
   DECLARE Reject : BOOLEAN
   DECLARE Stage : CHAR
   DECLARE Limit_1 : REAL
   DECLARE Limit_2 : REAL
ENDTYPE''') + "<p><b>(ii)</b> " + mks(["DECLARE Item : ARRAY [1:2000] OF Component (or [2000], or [0:1999])"], "a") + "</p><p><b>(b)</b> " + mks(["Allows iteration: a loop can access the records", "An index gives direct access to a record, and dot notation simplifies the code (Item[1].Stage)", "Simplifies the code or algorithm, reduces duplication, and makes the program easier to write, understand, maintain, test and debug"], "b") + "</p>", None) + peq(SRC("s24", "23", "Q3(a)"), "3 + 1 marks", "Write / Suggest",
  "Component(Item_ID : STRING, Reject : BOOLEAN, Weight : REAL) and DECLARE Batch : ARRAY [1:1000] OF Component, with global Min and Max (an inclusive range). (i) A variable ThisIndex is the array index. Write a pseudocode clause to check whether the weight of an individual component is within the acceptable range. (ii) Suggest how an unused array element could be indicated.", "Batch[ThisIndex].Weight >= Min AND <= Max.",
  "<p><b>(i)</b> " + mks(["Reference to Batch[ThisIndex].Weight", "A valid check for one boundary", "A valid check for the other boundary with the correct logic operator"]) + "</p>" + pc('''
IF Batch[ThisIndex].Weight >= Min AND
   Batch[ThisIndex].Weight <= Max THEN''') + "<p><b>(ii)</b> " + mks(["Set Item_ID to an empty string, or NULL or an invalid value; or set Weight to zero or less"], "a") + "</p>", "Using OR with the two boundaries: no weight is both below Min and above Max, so the test would be wrong.") + peq(SRC("w25", "21", "Q3"), "4 + 2 + 3 marks", "Write / State",
  "RentalRecord: RentalID \"AB1234\" (unique alpha-numeric), CarID 241 (a numeric array index), DisCode 'S' (a letter), Start 13/06/2025, Duration 7 (days), Completed FALSE. (a)(i) Declare the record. (ii) Declare a 1D array Rental of 500 elements. (b) State three benefits of an array of records.", "STRING, INTEGER, CHAR, DATE, INTEGER, BOOLEAN.",
  "<p><b>(a)(i)</b> " + mks(["TYPE RentalRecord and ENDTYPE", "RentalID and CarID declared correctly", "DisCode and Start declared correctly", "Duration and Completed declared correctly"]) + "</p>" + pc('''
TYPE RentalRecord
   DECLARE RentalID : STRING
   DECLARE CarID : INTEGER
   DECLARE DisCode : CHAR
   DECLARE Start : DATE
   DECLARE Duration : INTEGER
   DECLARE Completed : BOOLEAN
ENDTYPE''') + "<p><b>(ii)</b> " + mks(["DECLARE Rental : ARRAY[1:500] OF RentalRecord"], "a") + "</p><p><b>(b)</b> " + mks(["Different data types held for each rental under a single identifier", "Allows iteration through the records, or direct access to a record by an index", "Simplifies the code, reduces duplication, and makes testing, debugging and maintenance easier"], "b") + "</p>", None) + peq(SRC("w25", "23", "Q8(a)(b)"), "8 + 7 marks", "Write",
  "Loan records have StudentID (STRING), BookID (STRING) and OnLoan (BOOLEAN, TRUE if not returned) in a global array Loan of 8000 elements; unused elements have StudentID set to an empty string (anywhere in the array). (a) Write efficient pseudocode for LoanStatus(), called with a StudentID and BookID: output whether the loan has been returned, or a warning if no record is found. Each combination occurs only once. (b) Write a function LoansPerTutor() called with a tutor ID (the first three characters of a StudentID) that returns the number of books currently on loan to that tutor's students.", "Stop when found. LEFT(StudentID, 3).",
  "<p><b>(a)</b> " + mks(["Procedure heading, parameters and ending", "Loop through all elements in the Loan array", "or until the loan record is found (efficient)", "Test for the correct StudentID in the loop", "and the correct BookID", "Check the OnLoan data item", "Output both messages as appropriate, once", "If no matching loan is found output 'not found' after the loop"]) + "</p>" + pc('''
PROCEDURE LoanStatus(ThisStudentID, ThisBookID : STRING)
   DECLARE Index : INTEGER
   DECLARE Found : BOOLEAN
   Index ← 1
   Found ← FALSE
   WHILE Index <= 8000 AND NOT Found
      IF Loan[Index].StudentID = ThisStudentID AND
         Loan[Index].BookID = ThisBookID THEN
         IF Loan[Index].OnLoan = FALSE THEN
            OUTPUT "Loan has been returned."
         ELSE
            OUTPUT "Loan has not been returned."
         ENDIF
         Found ← TRUE
      ENDIF
      Index ← Index + 1
   ENDWHILE
   IF NOT Found THEN
      OUTPUT "Warning - Loan not found."
   ENDIF
ENDPROCEDURE''') + "<p><b>(b)</b> " + mks(["Initialise a local integer Count", "Loop through all elements in the Loan array", "Attempt at referencing a data item in the loop", "Extract the tutor ID from StudentID in the loop", "Test for a matching tutor AND that the book is on loan, with correct dot notation", "If true increment Count", "Return Count"], "a") + "</p>" + pc('''
FUNCTION LoansPerTutor(TutorID : STRING) RETURNS INTEGER
   DECLARE Index, Count : INTEGER
   Count ← 0
   FOR Index ← 1 TO 8000
      IF LEFT(Loan[Index].StudentID, 3) = TutorID AND
         Loan[Index].OnLoan = TRUE THEN
         Count ← Count + 1
      ENDIF
   NEXT Index
   RETURN Count
ENDFUNCTION'''), None) + peq(SRC("s26", "23", "Q5"), "4 + 7 marks", "Write / Complete",
  "Each person's interview data is a string packet <initial><shortened surname (5 characters)><office code><summary>, for example \"PWatkiBSecond interview\". (a) Write a function InterviewSummary() that takes the packet as a parameter and returns the interview summary text. (b) The packets are lines of the file JobApps.txt. Complete the pseudocode of Search(Initial : CHAR, ShortSurname : STRING) to output 'Name found' or 'Name not found'.", "The summary starts at character 8: MID or RIGHT with LENGTH.",
  "<p><b>(a)</b> " + mks(["Function identifier, ending and parameter", "The first part of the summary expression using MID or RIGHT", "The second part using LENGTH", "Return the calculated STRING with RETURNS STRING in the header"]) + "</p>" + pc('''
FUNCTION InterviewSummary(ThisApplicant : STRING) RETURNS STRING
   DECLARE Summary : STRING
   Summary ← MID(ThisApplicant, 8, LENGTH(ThisApplicant) - 7)
   RETURN Summary
ENDFUNCTION''') + "<p><b>(b)</b> One mark per gap:</p>" + pc('''
PROCEDURE Search(Initial : CHAR, ShortSurname : STRING)
   DECLARE ThisApplicant, ThisSurname : STRING
   DECLARE ThisInitial : CHAR
   DECLARE Found : BOOLEAN
   OPENFILE "JobApps.txt" FOR READ
   Found ← FALSE
   REPEAT
      READFILE "JobApps.txt", ThisApplicant
      ThisInitial ← LEFT(ThisApplicant, 1)
      ThisSurname ← MID(ThisApplicant, 2, 5)
      IF ThisSurname = ShortSurname AND ThisInitial = Initial THEN
         Found ← TRUE
         OUTPUT "Name found"
      ENDIF
   UNTIL Found = TRUE OR EOF("JobApps.txt")
   IF Found = FALSE THEN
      OUTPUT "Name not found"
   ENDIF
   CLOSEFILE "JobApps.txt"
ENDPROCEDURE'''), None)

review = req("5 marks", "Write", "A record Book holds Title (text), Pages (whole number), Price (decimal) and OnLoan (yes/no). Declare the record and an array Library of 200 books.", "TYPE ... ENDTYPE; ARRAY.", "<p>" + mks(["TYPE Book and ENDTYPE", "Title: STRING and Pages: INTEGER", "Price: REAL and OnLoan: BOOLEAN", "DECLARE Library : ARRAY [1:200] OF Book"]) + "</p>" + pc("TYPE Book\n   DECLARE Title : STRING\n   DECLARE Pages : INTEGER\n   DECLARE Price : REAL\n   DECLARE OnLoan : BOOLEAN\nENDTYPE\nDECLARE Library : ARRAY [1:200] OF Book"), None) + req("5 marks", "Write", "Write a procedure ListLoans() that outputs the Title of every Book on loan in Library. Unused elements have an empty Title.", "Skip empty; test OnLoan.", "<p>" + mks(["Procedure heading, ending and a loop counter", "Loop through 200 elements", "Skip unused (empty Title)", "Test OnLoan = TRUE in the loop", "Output Title"]) + "</p>" + pc("PROCEDURE ListLoans()\n   DECLARE Index : INTEGER\n   FOR Index ← 1 TO 200\n      IF Library[Index].Title <> \"\" THEN\n         IF Library[Index].OnLoan = TRUE THEN\n            OUTPUT Library[Index].Title\n         ENDIF\n      ENDIF\n   NEXT Index\nENDPROCEDURE"), None) + req("3 marks", "State", "State three benefits of storing library books as an array of records.", "Types, loops, code.", "<p>" + mks(["Different data types are stored under one identifier", "A loop can process every record", "The code is simpler and easier to maintain"]) + "</p>", None) + req("2 marks", "Suggest", "Suggest two ways of marking an unused Book record.", "Impossible values.", "<p>" + mks(["Set Title to an empty string", "Set Pages to zero or a negative value"]) + "</p>", None) + req("2 marks", "Write", "Write a statement to output the Price of the 12th book.", "Dot notation.", "<p>" + mks(["OUTPUT Library[12].Price"]) + " (the index in brackets, then dot and field)</p>", None)

tips = tips_html([
  ("Type from the example and comment.", "ID with letters: STRING."),
  ("TYPE ... ENDTYPE.", "Then DECLARE the array OF the type."),
  ("Dot notation.", "Array[Index].Field"),
  ("Skip unused records.", "Say how they are marked."),
  ("Loop to the array size.", "FOR Index ← 1 TO 500."),
  ("Three benefits.", "Mixed types, loops, simpler code."),
], [("a record", "A composite type with fields of different data types."), ("a field", "One item of data in a record."), ("dot notation", "Reaching a field: Staff[3].Name."), ("an unused element", "An array element marked with an impossible value.")],
  [("Write", "Write the pseudocode."), ("Declare", "Write the TYPE or ARRAY declaration."), ("State", "Short answer."), ("Suggest", "Give a sensible idea.")]) + FC

js = AKJS + AK20JS + "const EMP = " + json.dumps(EMP) + r''';
(function () {
  const draw = (s) => { const k = Math.round(s.i); const fl = [["EmployeeNumber", "123", "INTEGER"], ["Name", "\"Smith,Eric\"", "STRING"], ["Born", "13/02/2006", "DATE"], ["Attendance", "97.40", "REAL"]]; let o = SV.rect(20, 10, 440, 24, "f3", { rx: 4 }) + SV.text(28, 27, "TYPE Employee", "lbl bd", { style: "font-size:12px" }); fl.forEach((f, i) => { if (i < k + 1) o += SV.rect(20, 40 + i * 30, 440, 26, "cell", { rx: 4 }) + SV.text(28, 58 + i * 30, "DECLARE " + f[0] + " : " + f[2], "lbl", { style: "font-size:12px" }) + SV.text(300, 58 + i * 30, f[1], "lbl bd t3", { style: "font-size:12px" }); }); if (k >= 4) o += SV.text(20, 175, "ENDTYPE", "lbl bd"); return o; };
  Lib.stepper($("#stA"), { w: 480, h: 190, label: "Record", base: { i: 0 }, draw, tween: 100, dwell: 2400, steps: ["A record starts with TYPE and its name.", "Each field has its own data type: INTEGER.", "STRING.", "DATE.", "REAL, then ENDTYPE. Different types, one identifier."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.text(20, 16, "Staff : ARRAY [1:500] OF Employee", "lbl bd", { style: "font-size:12px" }); EMP.forEach((e, i) => { o += SV.rect(20, 24 + i * 28, 440, 24, e.n === -1 && k >= 2 ? "f2" : (k === 1 && i === 2 ? "f3" : "cell"), { rx: 4 }) + SV.text(28, 41 + i * 28, `[${i + 1}] ` + (e.n === -1 ? "EmployeeNumber -1  (unused)" : e.n + "  " + e.name + "  " + e.att), "lbl", { style: "font-size:11.5px" }); }); o += SV.text(20, 175, ["each element is one Employee record", "Staff[3].Name uses an index, then dot notation", "unused: marked with an impossible value, EmployeeNumber -1"][Math.min(k, 2)], "lbl bd t3", { style: "font-size:12px" }); return o; };
  Lib.stepper($("#stB"), { w: 480, h: 195, label: "Array of records", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: ["An array of five records (the real array has 500).", "<b>Staff[3]</b> picks one record; <b>.Name</b> picks a field.", "An unused element is marked with an impossible value."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = ""; EMP.forEach((e, i) => { const unused = e.n === -1, hit = !unused && e.att <= 90; o += SV.rect(20, 10 + i * 28, 300, 24, i === k ? "f3" : i < k ? (unused ? "cell" : hit ? "f1" : "f2") : "cell", { rx: 4 }) + SV.text(28, 27 + i * 28, `[${i + 1}] ` + (unused ? "unused" : e.name + " " + e.att), "lbl", { style: "font-size:12px" }) + (i <= k ? SV.text(330, 27 + i * 28, unused ? "skip" : hit ? "output" : "no", "lbl bd t3", { style: "font-size:12px" }) : ""); }); return o; };
  Lib.stepper($("#stC"), { w: 420, h: 160, label: "Loop", base: { i: 0 }, draw, tween: 100, dwell: 1800, steps: ["Index 1: attendance 97.4 is above 90: not output.", "Index 2: 88.5 is 90 or less: output.", "Index 3: unused: skip.", "Index 4: 71.0: output.", "Index 5: 90.0 is 90 or less: output."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  let lim = 90; const paint = () => { const hits = EMP.filter((e) => e.n !== -1 && e.att <= lim); let o = '<div class="tw"><table class="t mono"><tr><th>Index</th><th>EmployeeNumber</th><th>Name</th><th>Attendance</th><th>Output?</th></tr>'; EMP.forEach((e, i) => { o += `<tr><td>${i + 1}</td><td>${e.n}</td><td>${e.name || ""}</td><td>${e.n === -1 ? "" : e.att}</td><td>${e.n === -1 ? "skipped (unused)" : e.att <= lim ? "<b>yes</b>" : "no"}</td></tr>`; }); $("#eG").innerHTML = o + "</table></div>"; $("#eV").innerHTML = `Attendance <= <b>${lim}</b>: <b>${hits.length}</b> employee(s) output` + (hits.length ? " (" + hits.map((h) => h.n).join(", ") + ")" : "") + ". The unused record is skipped by the first IF."; };
  Lib.slider($("#eS"), { id: "e1", label: "Attendance limit ", min: 60, max: 100, step: 0.5, value: lim, fmt: (x) => x.toFixed(1), onInput: (v) => { lim = v; paint(); } }); paint();
})();
btnTable("tB", "tO", [
  ["RentalID \"AB1234\"", "STRING", "Letters and digits in quotes"],
  ["CarID 241 (an array index)", "INTEGER", "Whole number"],
  ["DisCode 'S'", "CHAR", "One letter in single quotes"],
  ["Start 13/06/2025", "DATE", "A date"],
  ["Completed FALSE", "BOOLEAN", "TRUE or FALSE"],
  ["Limit_1 13.5", "REAL", "Decimal"]
], ["Field", "Type", "Why"]);
btnTable("dB", "dO", [
  ["Name of the 3rd employee", "Staff[3].Name", "Index then dot"],
  ["Attendance of the record at Index", "Staff[Index].Attendance", "Variable index"],
  ["Weight of the batch item at ThisIndex", "Batch[ThisIndex].Weight", "Same pattern"],
  ["Whether the Index-th loan is on loan", "Loan[Index].OnLoan", "BOOLEAN field"]
], ["Need", "Pseudocode", "Why"]);
''' + _prjs

finish("as-10-1-data-types-records", "as101", "Data Types and Records",
  "The six data types, records declared with TYPE and ENDTYPE, arrays of records and dot notation, unused elements, and procedures that loop through records, with animations, an attendance lab and the real Paper 2 questions from 2021 to 2026.",
  "10.1", "10 · Data types and structures", "section 10.1 Data types and records", learn, watch, explore, _pr, real, where, past, review,
  "Part 1 is real 9618 questions on data types and records (Paper 2), 2021 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", tips, js)
