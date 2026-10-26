"""AS CS 8.3.1: Data Definition Language. Run: python3 tools/artifact-kit/mk_as831.py"""
from ak8 import *
import json

def run_ok(*stmts):
    c = sqlite3.connect(":memory:")
    for s in stmts: c.execute(s)
    return "\n".join(stmts)

RENTAL = run_ok("""CREATE TABLE RENTAL(
RentalID INTEGER NOT NULL,
CustomerID INTEGER NOT NULL,
HouseID VARCHAR(5) NOT NULL,
MonthlyCost REAL NOT NULL,
DepositPaid BOOLEAN NOT NULL,
PRIMARY KEY (RentalID)
);""")
ST = run_ok("""CREATE TABLE STUDENT_TEST(
StudentID INTEGER,
TestID VARCHAR(5),
Mark INTEGER,
PRIMARY KEY (StudentID, TestID),
FOREIGN KEY (TestID) REFERENCES TEST(TestID),
FOREIGN KEY (StudentID) REFERENCES STUDENT(StudentID)
);""")
BIRD = run_ok("""CREATE TABLE BIRD_TYPE(
BirdID CHAR(4) NOT NULL,
Name VARCHAR(9),
Size VARCHAR(6),
PRIMARY KEY (BirdID)
);""")
EXAM = run_ok("""CREATE TABLE EXAM(
ExamID VARCHAR(8) NOT NULL,
Subject VARCHAR(20),
Level INTEGER,
TotalMarks INTEGER,
PRIMARY KEY (ExamID)
);""")
PERF = run_ok("""CREATE TABLE PERFORMANCE(
PerformanceID VARCHAR(4) NOT NULL,
ShowID VARCHAR(4),
ShowDate DATE,
StartTime TIME,
PRIMARY KEY (PerformanceID),
FOREIGN KEY (ShowID) REFERENCES SHOW(ShowID)
);""")
RP = run_ok("""CREATE TABLE REPAIR_PART(
PartID VARCHAR(20) NOT NULL,
RepairNumber VARCHAR(4) NOT NULL,
Quantity INTEGER NOT NULL,
PRIMARY KEY (PartID, RepairNumber)
);""")
STAFF = run_ok("""CREATE TABLE STAFF(
StaffID INTEGER NOT NULL,
StaffFirstName VARCHAR(20),
StaffLastName VARCHAR(20),
Department CHAR(1),
RemoteWorker BOOLEAN,
PRIMARY KEY (StaffID)
);""")
ALT = run_ok("CREATE TABLE T(A INTEGER)", "ALTER TABLE T ADD Returned BOOLEAN")

T = {"STUDENT": {"cols": ["StudentID", "FirstName", "LastName"], "rows": [[12, "Ayo", "Bell"], [13, "Cam", "Diaz"]]}}

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p><b>Data Definition Language (DDL)</b> is the part of SQL that <b>defines</b> a database and its tables, rather than the data in them: <span class="mono">CREATE DATABASE</span>, <span class="mono">CREATE TABLE</span> and <span class="mono">ALTER TABLE</span> (to add a field or a key). In <span class="mono">CREATE TABLE</span> you give each field a name and a <b>data type</b> (<span class="mono">CHAR</span>, <span class="mono">VARCHAR</span>, <span class="mono">BOOLEAN</span>, <span class="mono">INTEGER</span>, <span class="mono">REAL</span>, <span class="mono">DATE</span>, <span class="mono">TIME</span>), optional constraints such as <span class="mono">NOT NULL</span>, then the <span class="mono">PRIMARY KEY</span> and any <span class="mono">FOREIGN KEY ... REFERENCES</span>. Choose the data type from the sample data: text IDs with letters are <span class="mono">VARCHAR</span> or <span class="mono">CHAR(n)</span>, whole numbers <span class="mono">INTEGER</span>, money <span class="mono">REAL</span>, yes/no <span class="mono">BOOLEAN</span>. Exam questions ask you to write a statement, complete one, or find and correct errors, each mark for a specific feature.</p></div>

  <h2>1 · The statements</h2>
  ''' + sqlblock('''
CREATE DATABASE SHOP;

CREATE TABLE CUSTOMER(
CustomerID VARCHAR(5) NOT NULL,
FirstName VARCHAR(20),
LastName VARCHAR(20),
DateOfBirth DATE,
PRIMARY KEY (CustomerID)
);

CREATE TABLE SHOP_ORDER(
OrderNo INTEGER NOT NULL,
CustomerID VARCHAR(5),
OrderDate DATE,
PRIMARY KEY (OrderNo),
FOREIGN KEY (CustomerID) REFERENCES CUSTOMER(CustomerID)
);

ALTER TABLE SHOP_ORDER
ADD Paid BOOLEAN;

ALTER TABLE SHOP_ORDER
ADD FOREIGN KEY (CustomerID) REFERENCES CUSTOMER(CustomerID);''') + '''
  <div class="tw"><table class="t">
    <tr><th>Part</th><th>What it does</th></tr>
    <tr><td class="mono">CREATE DATABASE name;</td><td>Defines a new database with that name</td></tr>
    <tr><td class="mono">CREATE TABLE name( ... );</td><td>Creates a table: opening and closing brackets, fields separated by commas</td></tr>
    <tr><td class="mono">field type</td><td>Gives each field its data type (the length goes in brackets for CHAR and VARCHAR)</td></tr>
    <tr><td class="mono">NOT NULL</td><td>A constraint: a value must be entered</td></tr>
    <tr><td class="mono">PRIMARY KEY (field)</td><td>Sets the primary key; a composite key lists both fields, PRIMARY KEY (A, B)</td></tr>
    <tr><td class="mono">FOREIGN KEY (field) REFERENCES table(field)</td><td>Links the field to the primary key of another table</td></tr>
    <tr><td class="mono">ALTER TABLE name ADD field type;</td><td>Adds a new field to an existing table (add several with commas); also used to add a foreign key</td></tr>
  </table></div>

  <h2>2 · Choosing data types</h2>
  <div class="tw"><table class="t">
    <tr><th>Sample data</th><th>Type</th></tr>
    <tr><td>000001, ST23-56, A123AA (codes, text, leading zeros)</td><td>VARCHAR(n) or CHAR(n); not INTEGER</td></tr>
    <tr><td>Names, addresses</td><td>VARCHAR(n)</td></tr>
    <tr><td>Whole numbers (age, quantity, marks)</td><td>INTEGER</td></tr>
    <tr><td>Money (30.00, 22.50), measurements</td><td>REAL (or CURRENCY)</td></tr>
    <tr><td>TRUE / FALSE, Yes / No</td><td>BOOLEAN</td></tr>
    <tr><td>01/01/2024, 13:00</td><td>DATE, TIME</td></tr>
  </table></div>

  <h2>Common ways to lose marks</h2>
  <ul>
    <li>Forgetting the commas between fields, or the closing bracket and semicolon.</li>
    <li>Using INTEGER for an ID that contains letters or leading zeros.</li>
    <li>Writing PRIMARY KEY CharacterID without brackets, or FOREIGN KEY with no REFERENCES table and field.</li>
    <li>Using CREATE DATA BASE or NONULL (spelling errors the paper plants as 'find the error' questions).</li>
    <li>Using INSERT for a new field. A new field is added with ALTER TABLE ... ADD.</li>
  </ul>
'''

watch = '''
  <h2>1 · CREATE TABLE line by line</h2>
  <div id="stA"></div>
  <h2>2 · ALTER TABLE adds a field</h2>
  <div id="stB"></div>
  <h2>3 · A foreign key links two tables</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Create a table</h2>
  <p>Edit and run the statement, then query the new table.</p>
  <div class="card" id="ddl"></div>
  <h2>Lab 2 · Choose the data type</h2>
  <div class="card"><div id="tB" class="btnrow"></div><div id="tO"></div></div>
  <h2>Lab 3 · Find the error</h2>
  <div class="card"><div id="eB" class="btnrow"></div><div id="eO"></div></div>
'''

_pr, _prjs = PR(["Which data type?", "Correct or error?", "Match the clause to its job", "Put the CREATE TABLE parts in order", "Working out", "Multiple choice"],
  ("Which data type suits the field?", ["VARCHAR / CHAR", "INTEGER", "REAL", "BOOLEAN", "DATE"], [("A registration number such as A123AA", 0), ("The number of items ordered", 1), ("A price such as 22.50", 2), ("Whether a deposit has been paid", 3), ("The date of birth", 4), ("A postcode", 0)], "Match the sample data."),
  ("Is the DDL fragment correct or does it contain an error?", ["Correct", "Error"], [("CREATE DATABASE SHOP;", 0), ("CREATE DATA BASE SHOP;", 1), ("PRIMARY KEY (OrderNo)", 0), ("PRIMARY KEY OrderNo", 1), ("FOREIGN KEY (ShipID) REFERENCES SHIP(ShipID)", 0), ("FOREIGN KEY (ShipID)", 1)], "The key needs brackets; REFERENCES needs table and field."),
  [["CREATE TABLE", "Defines a new table"], ["ALTER TABLE ... ADD", "Adds a field to an existing table"], ["NOT NULL", "A value must be entered"], ["PRIMARY KEY", "Identifies each record uniquely"], ["REFERENCES", "Names the table and field a foreign key links to"]],
  ("Put the parts of CREATE TABLE in order.", ["CREATE TABLE and the table name, then an opening bracket", "Each field with its data type, separated by commas", "NOT NULL constraints where needed", "PRIMARY KEY and FOREIGN KEY lines", "A closing bracket and a semicolon"], "Name, fields, constraints, keys, close."),
  [{"q": "A table has fields ID, Name and Age. How many commas are needed in the field list of CREATE TABLE if the PRIMARY KEY line is also listed after the last field?", "a": 3, "unit": "", "tol": 0.01, "hint": "Between each of the 4 items.", "sol": "<b>3</b>."}, {"q": "A table has a composite key (PartID, RepairNumber). How many fields are named in PRIMARY KEY (...)?", "a": 2, "unit": "", "tol": 0.01, "hint": "Two.", "sol": "<b>2</b>."}, {"q": "VARCHAR(5) can hold at most how many characters?", "a": 5, "unit": "", "tol": 0.01, "hint": "The number in brackets.", "sol": "<b>5</b>."}, {"q": "How many ALTER TABLE statements are needed to add one field to one table?", "a": 1, "unit": "", "tol": 0.01, "hint": "One.", "sol": "<b>1</b>."}, {"q": "A database has 4 tables, each created with one CREATE TABLE. How many CREATE statements in total including CREATE DATABASE?", "a": 5, "unit": "", "tol": 0.01, "hint": "4 + 1.", "sol": "<b>5</b>."}],
  [("DDL stands for:", ["Data Definition Language", "Data Delete Language", "Database Design List", "Data Display Layer"], 0, "Definition."), ("A new field is added with:", ["ALTER TABLE ... ADD", "INSERT", "UPDATE", "SELECT"], 0, "ALTER."), ("A price such as 12.50 is:", ["REAL", "BOOLEAN", "DATE", "CHAR(1)"], 0, "REAL."), ("A foreign key uses:", ["REFERENCES", "WHERE", "ORDER BY", "GROUP BY"], 0, "REFERENCES."), ("NOT NULL means:", ["A value is required", "The field is a key", "The field is empty", "The field is a date"], 0, "Required."), ("A code like A123AA is stored as:", ["VARCHAR or CHAR", "INTEGER", "BOOLEAN", "REAL"], 0, "Text.")],
  [("CREATE DATABASE", "Defines a new database."), ("CREATE TABLE", "Brackets, fields, types, keys."), ("ALTER TABLE", "ADD a field or a foreign key."), ("PRIMARY KEY (a)", "Unique identifier; brackets."), ("FOREIGN KEY ... REFERENCES t(f)", "Links to another table."), ("NOT NULL", "Value required."), ("VARCHAR(n)", "Text up to n characters."), ("Data types", "CHAR VARCHAR BOOLEAN INTEGER REAL DATE TIME.")])

real = RWNOTE + (
rw("Building a new app's database", "Before any data goes in, the developer writes CREATE TABLE statements for each entity, choosing field types and keys.", "DDL defines the structure.") +
rw("Adding a feature later", "A shop wants to record whether a toy has been returned: ALTER TABLE adds a Returned field without losing existing records.", "ALTER TABLE ... ADD.") +
rw("Why IDs are text", "A customer number like 000123 must keep its leading zeros, so it is stored as text, not a number.", "VARCHAR for codes.") +
rw("Linking orders to customers", "FOREIGN KEY (CustomerID) REFERENCES CUSTOMER(CustomerID) stops an order being created for a customer that does not exist.", "foreign key constraint.") +
rw("Creating the database itself", "Before tables exist the database is created once with CREATE DATABASE.", "CREATE DATABASE.")
)

where = [
  ("M/J 2021", "11, 13", "7(b)(iii)", "1", "Define a database called SHOPORDERS"),
  ("M/J 2021", "12", "1(c)(i)", "4", "Complete the CREATE TABLE statement for RENTAL"),
  ("O/N 2021", "12", "6(c)(ii)", "3", "Add a date of order field to PURCHASE"),
  ("M/J 2022", "11", "4(c)(i)", "5", "Create the table STUDENT_TEST with its keys"),
  ("O/N 2022", "11", "4(d)", "3", "Add two fields to CAMERA_DATA"),
  ("O/N 2022", "13", "2(d)", "2", "Add a resolution field to PHOTOGRAPH"),
  ("M/J 2022", "13", "6(b)(ii)", "2", "Add a Returned field to DEVICE"),
  ("M/J 2023", "11", "2(b)(iii)", "4", "Define the table BIRD_TYPE"),
  ("O/N 2023", "11", "3(c)(i)", "1", "Define a database called SHOP"),
  ("M/J 2024", "12", "4(b), (c)", "3 + 2", "Define the table EXAM; link a foreign key with ALTER TABLE"),
  ("M/J 2024", "13", "4(b)", "4", "Define the table PERFORMANCE"),
  ("O/N 2024", "11", "2(b)(ii)", "5", "Define REPAIR_PART with constraints"),
  ("O/N 2025", "12", "4(b)", "2", "Add a date of last inspection field to CONTAINER"),
  ("O/N 2025", "13", "5(b)", "4", "Define the table STAFF"),
  ("M/J 2026", "11", "4(c)(i)", "2", "Add a Yes/No field to BORROW"),
  ("M/J 2026", "12", "3(b)(i)", "4", "Four errors in a CREATE TABLE script"),
  ("M/J 2026", "13", "4(c)(i)", "4", "Four errors in two CREATE scripts")]

past = '''  <p class="note">DDL appears in Paper 1 every series. The mark scheme gives one mark per feature (CREATE TABLE and brackets, each field with a sensible type, the primary key, the foreign key), so a missing comma or key costs a mark. Every statement below was run to check it is valid SQL. Questions are reworded from the papers; check the original paper and mark scheme for the exact wording.</p>
''' + peq(SRC("s21", "11/13", "Q7(b)(iii)"), "1 mark", "Write",
  "Write a Data Definition Language statement to define a new database with the name SHOPORDERS.", "CREATE DATABASE.",
  "<p>" + mks(["CREATE DATABASE SHOPORDERS;"]) + "</p>", None) + peq(SRC("s21", "12", "Q1(c)(i)"), "4 marks", "Complete",
  "Example data from RENTAL (RentalID 1, 2, 3, 4; CustomerID 22, 13, 1, 3; HouseID 15B5L, 3F, 12AB, 37; MonthlyCost 1000.00, 687.00, 550.00, 444.50; DepositPaid Yes/No). Complete the DDL statement: CREATE ... ... ( RentalID INTEGER NOT NULL, CustomerID INTEGER NOT NULL, HouseID ... (5) NOT NULL, MonthlyCost ... NOT NULL, DepositPaid BOOLEAN NOT NULL, ... (RentalID) );", "TABLE RENTAL; VARCHAR; REAL; PRIMARY KEY.",
  "<p>" + mks(["CREATE TABLE RENTAL", "HouseID VARCHAR (5) NOT NULL", "MonthlyCost REAL (or CURRENCY) NOT NULL", "PRIMARY KEY (RentalID)"]) + "</p>" + sqlblock(RENTAL), "Giving HouseID an INTEGER type. The data has letters.") + peq(SRC("w21", "12", "Q6(c)(ii)"), "3 marks", "Write",
  "Write DDL statements to include a field in the table PURCHASE to store the date of the order.", "ALTER TABLE, ADD, DATE.",
  "<p>" + mks(["ALTER TABLE PURCHASE", "ADD OrderDate", "with a suitable data type, such as DATE"]) + "</p>" + sqlblock("ALTER TABLE PURCHASE\nADD OrderDate DATE;"), None) + peq(SRC("s22", "11", "Q4(c)(i)"), "5 marks", "Write",
  "STUDENT_TEST(StudentID, TestID, Mark) has sample data 12, A1, 50; 12, P10, 100; 13, A1, 75; 14, P10, 60. Write an SQL script to create the table. StudentID is a key of STUDENT and TestID a key of TEST.", "Composite key and two foreign keys.",
  "<p>" + mks(["CREATE TABLE, the table name, opening and closing brackets", "StudentID and Mark as INTEGER", "TestID as VARCHAR", "The primary key correctly set up (a composite of StudentID and TestID)", "Foreign keys correctly set up"]) + "</p>" + sqlblock(ST), None) + peq(SRC("w22", "11", "Q4(d)"), "3 marks", "Write",
  "Write an SQL script to include two new fields in CAMERA_DATA to store the number of photographs currently on the camera and the date the camera was last used.", "ALTER TABLE; two fields with types.",
  "<p>" + mks(["ALTER TABLE CAMERA_DATA", "ADD NumberStored INTEGER", ", LastUsed DATE"]) + "</p>" + sqlblock("ALTER TABLE CAMERA_DATA\nADD NumberStored INTEGER, LastUsed DATE;"), None) + peq(SRC("w22", "13", "Q2(d)"), "2 marks", "Write",
  "Write the SQL script to add one field to the table PHOTOGRAPH to store the resolution of the photograph, for example 1920 × 1068.", "Text type, since 1920 × 1068 is not a number.",
  "<p>" + mks(["ALTER TABLE PHOTOGRAPH", "ADD Resolution TEXT (or VARCHAR(11))"]) + "</p>" + sqlblock("ALTER TABLE PHOTOGRAPH\nADD Resolution VARCHAR(11);"), "Using INTEGER. The value has an 'x' in it, so it is text.") + peq(SRC("s22", "13", "Q6(b)(ii)"), "2 marks", "Write",
  "The table DEVICE needs a new attribute to store whether the device has been returned or not. Write an SQL script to insert the new attribute into the table.", "ALTER TABLE ... ADD Returned BOOLEAN.",
  "<p>" + mks(["ALTER TABLE DEVICE", "ADD an appropriate field name with an appropriate data type"]) + "</p>" + sqlblock("ALTER TABLE DEVICE\nADD Returned BOOLEAN;"), None) + peq(SRC("s23", "11", "Q2(b)(iii)"), "4 marks", "Write",
  "BIRD_TYPE sample data: BirdID 0123, 0035, 0004, 0085; Name Blackbird, Jay, Raven, Robin; Size Medium, Large, Large, Small. The database supports character, varchar, Boolean, integer, real, date and time. Write an SQL script to define the table BIRD_TYPE.", "BirdID as text, key.",
  "<p>" + mks(["CREATE TABLE with the start and end brackets", "BirdID as CHAR or VARCHAR", "Name and Size as VARCHAR or CHAR", "BirdID as the primary key"]) + "</p>" + sqlblock(BIRD), "BirdID as INTEGER: 0004 would become 4.") + peq(SRC("w23", "11", "Q3(c)(i)"), "1 mark", "Write",
  "Write a Structured Query Language script to define the database called SHOP.", "CREATE DATABASE SHOP.",
  "<p>" + mks(["CREATE DATABASE SHOP;"]) + "</p>", None) + peq(SRC("s24", "12", "Q4(b)(c)"), "3 + 2 marks", "Write",
  "EXAM sample data: ExamID 00956124, 00956125 ...; Subject Computer Science, Mathematics, Physics; Level 2 or 3; TotalMarks 75, 120, 100, 150, 70, 80. (b) Write an SQL script to define the table EXAM. (c) EXAM_QUESTION has been created but the foreign key has not been linked. Write an SQL script to link the foreign key to EXAM.", "Table with a primary key; ALTER TABLE ... ADD FOREIGN KEY.",
  "<p><b>(b)</b> " + mks(["CREATE TABLE EXAM with opening and closing brackets", "All fields with appropriate data types and commas at the end of lines", "ExamID as the primary key"]) + "</p>" + sqlblock(EXAM) + "<p><b>(c)</b> " + mks(["Altering the table EXAM_QUESTION", "Linking ExamID to ExamID in EXAM"], "a") + "</p>" + sqlblock("ALTER TABLE EXAM_QUESTION\nADD FOREIGN KEY (ExamID) REFERENCES EXAM(ExamID);"), None) + peq(SRC("s24", "13", "Q4(b)"), "4 marks", "Write",
  "PERFORMANCE(PerformanceID, ShowID, ShowDate, StartTime) has sample data 0001, MK12, 5/5/2025, 13:00 ... Write an SQL script to define the table PERFORMANCE. ShowID is the key of SHOW.", "Four fields, key, foreign key.",
  "<p>" + mks(["CREATE TABLE PERFORMANCE with opening and closing brackets", "All four attributes with appropriate data types", "PerformanceID as the primary key", "ShowID as a foreign key referencing the SHOW table"]) + "</p>" + sqlblock(PERF), None) + peq(SRC("w24", "11", "Q2(b)(ii)"), "5 marks", "Write",
  "REPAIR_PART sample data: PartID ACD128SA, PPOR543DWW, TR453, PPOR543DWW, WED5; RepairNumber 0022, 0022, 0023, 0023, 0024; Quantity 3, 1, 1, 2, 5. Write an SQL script to define the table. Include constraints on the data that can be entered into each field where appropriate.", "NOT NULL on each; composite key.",
  "<p>" + mks(["CREATE TABLE REPAIR_PART with brackets, all statements inside", "PartID and RepairNumber as VARCHAR (or equivalent)", "Quantity as INTEGER", "At least one appropriate constraint (such as NOT NULL)", "A composite primary key (PartID, RepairNumber)"]) + "</p>" + sqlblock(RP), "Using a single-field primary key. Each part can appear in many repairs.") + peq(SRC("w25", "12", "Q4(b)"), "2 marks", "Write",
  "The table CONTAINER needs an additional field to store the date of last inspection, for example 08/07/2019. Write an SQL script to add one field.", "ALTER TABLE; DATE.",
  "<p>" + mks(["ALTER TABLE CONTAINER", "ADD a field with a suitable name and type, for example InspectionDate DATE"]) + "</p>" + sqlblock("ALTER TABLE CONTAINER\nADD InspectionDate DATE;"), None) + peq(SRC("w25", "13", "Q5(b)"), "4 marks", "Write",
  "STAFF sample data: StaffID 1, 2, 3; StaffFirstName Ralph, Luca, Darwin; StaffLastName Jura, Emcee, Acula; Department E, A, F; RemoteWorker Yes, Yes, No. Write an SQL script to define the table STAFF.", "Integer id, text names, a single-letter department, Boolean.",
  "<p>" + mks(["CREATE TABLE with brackets and commas separating the attributes", "Appropriate types for StaffFirstName, StaffLastName and Department", "Appropriate types for StaffID and RemoteWorker", "The primary key correctly defined"]) + "</p>" + sqlblock(STAFF), None) + peq(SRC("s26", "11", "Q4(c)(i)"), "2 marks", "Write",
  "The table BORROW needs an additional field that stores whether the toy has been returned, either Yes or No. Write an SQL script to include the additional field.", "ALTER TABLE BORROW ADD with a suitable type.",
  "<p>" + mks(["Altering the correct table", "Adding an appropriately named field with an appropriate data type"]) + "</p>" + sqlblock("ALTER TABLE BORROW\nADD Returned BOOLEAN;") + "<p>VARCHAR or CHAR(3) is also accepted.</p>", None) + peq(SRC("s26", "12", "Q3(b)(i)"), "4 marks", "Correct",
  "The following script defines the table CHARACTER and contains four errors. 01 CREATE TABLE CHARACTER( 02 CharacterID INT, 03 CharacterName VARCHAR, 04 DateCreated DATE, 05 TheLevel INT, 06 NumberOfPoints INT, 07 PlayerID VARCHAR, 08 PRIMARY KEY CharacterID, 09 FOREIGN KEY(PlayerID) 10 ); Give the line number of each error and the corrected line. (The sample data has CharacterID values like 00123, and the field is called Level.)", "ID with leading zeros; field name; key brackets; REFERENCES.",
  "<p>" + mks(["Line 02: CharacterID VARCHAR, (or VARCHAR(5)): the ID has leading zeros", "Line 05: Level INT, (the field is Level)", "Line 08: PRIMARY KEY(CharacterID),", "Line 09: FOREIGN KEY(PlayerID) REFERENCES PLAYER(PlayerID)"]) + "</p>", None) + peq(SRC("s26", "13", "Q4(c)(i)"), "4 marks", "Correct",
  "These scripts create the database and the table SUBJECT and contain four errors. 01 CREATE DATA BASE SCHOOLDATA; 02 CREATE TABLE SUBJECT( 03 SubjectCode VARCHAR NONULL, 04 SubjectName VARCHAR 05 DepartmentID VARCHAR, 06 PRIMARY KEY (SubjectCode), 07 FOREIGN KEY (DepartmentID) REFERENCES (DepartmentID) 08 ); Give the line number of each error and the corrected line.", "Spelling, a missing comma, a missing table name.",
  "<p>" + mks(["Line 01: CREATE DATABASE SCHOOLDATA;", "Line 03: SubjectCode VARCHAR NOT NULL,", "Line 04: SubjectName VARCHAR, (a comma is missing)", "Line 07: FOREIGN KEY (DepartmentID) REFERENCES DEPARTMENT(DepartmentID)"]) + "</p>", None)

review = req("3 marks", "Write", "Write DDL to create the table CAR with fields CarReg (text of 6), Make (text up to 20), Year (whole number) and Electric (yes or no), with CarReg as the primary key.", "Types and key.", "<p>" + mks(["CREATE TABLE CAR with brackets and commas", "Suitable types: VARCHAR(6), VARCHAR(20), INTEGER, BOOLEAN", "PRIMARY KEY (CarReg)"]) + "</p>" + sqlblock(run_ok("CREATE TABLE CAR(\nCarReg VARCHAR(6) NOT NULL,\nMake VARCHAR(20),\nYear INTEGER,\nElectric BOOLEAN,\nPRIMARY KEY (CarReg)\n);")), None) + req("2 marks", "Write", "Write DDL to add a field Notes (text up to 100 characters) to the table CAR.", "ALTER TABLE.", "<p>" + mks(["ALTER TABLE CAR", "ADD Notes VARCHAR(100)"]) + "</p>", None) + req("2 marks", "Explain", "Explain why a phone number field is stored as VARCHAR, not INTEGER.", "Leading zeros.", "<p>" + mks(["A phone number can start with 0 or contain + or spaces", "an INTEGER would lose the leading zero and you do not do arithmetic on it"]) + "</p>", None) + req("2 marks", "Write", "Write DDL to link BOOKING(CustomerID) to CUSTOMER(CustomerID) as a foreign key using ALTER TABLE.", "ADD FOREIGN KEY.", "<p>" + mks(["ALTER TABLE BOOKING ADD FOREIGN KEY (CustomerID)", "REFERENCES CUSTOMER(CustomerID)"]) + "</p>", None) + req("2 marks", "State", "State the purpose of NOT NULL in a CREATE TABLE statement.", "Value required.", "<p>" + mks(["It is a constraint on a field", "so a value must be entered for every record"]) + "</p>", None)

tips = tips_html([
  ("CREATE TABLE: brackets, commas, semicolon.", "Check the end of every line."),
  ("Pick types from the sample data.", "Letters or leading zeros: VARCHAR."),
  ("PRIMARY KEY (field).", "Composite: both fields."),
  ("FOREIGN KEY ... REFERENCES table(field).", "Name the table and the field."),
  ("New field: ALTER TABLE ... ADD.", "Not INSERT."),
  ("Spell the keywords.", "CREATE DATABASE, NOT NULL."),
], [("DDL", "Data Definition Language: statements that define tables and databases."), ("NOT NULL", "A constraint: a value must be entered."), ("VARCHAR", "A text field of variable length."), ("REFERENCES", "Names the table and field a foreign key links to.")],
  [("Write", "Write the statement."), ("Complete", "Fill the missing words."), ("Correct", "Find and fix errors."), ("Define", "Create the table.")]) + FC

js = AKJS + AK20JS + SQLJS + "const DBT = " + json.dumps(T) + r''';
(function () {
  const draw = (s) => { const k = Math.round(s.i); const L = ["CREATE TABLE CAR(", "  CarReg VARCHAR(6) NOT NULL,", "  Make VARCHAR(20),", "  Electric BOOLEAN,", "  PRIMARY KEY (CarReg)", ");"]; let o = ""; L.forEach((l, i) => { o += SV.rect(20, 10 + i * 26, 300, 22, i === k ? "f3" : i < k ? "f1" : "cell", { rx: 4 }) + SV.text(28, 26 + i * 26, l, "lbl", { style: "font-size:12px" }); });
    o += SV.text(340, 60, ["table name and bracket", "text field, a value is required", "text field", "yes/no field", "the key", "closing bracket and semicolon"][k], "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stA"), { w: 560, h: 175, label: "CREATE TABLE", base: { i: 0 }, draw, tween: 100, dwell: 2000, steps: ["CREATE TABLE names the table and opens a bracket.", "Each field has a name and a type; NOT NULL means a value is required.", "Fields are separated by commas.", "BOOLEAN stores yes or no.", "PRIMARY KEY names the unique identifier, in brackets.", "Close the bracket and end with a semicolon."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.text(20, 20, "BORROW", "lbl bd") + SV.rect(20, 28, 140, 26, "cell", { rx: 4 }) + SV.text(28, 46, "BorrowID", "lbl", { style: "font-size:12px" }) + SV.rect(165, 28, 140, 26, "cell", { rx: 4 }) + SV.text(173, 46, "CustomerID", "lbl", { style: "font-size:12px" }); if (k >= 1) o += SV.rect(310, 28, 140, 26, "f1", { rx: 4 }) + SV.text(318, 46, "Returned (new)", "lbl", { style: "font-size:12px" });
    o += SV.text(20, 90, k >= 1 ? "ALTER TABLE BORROW ADD Returned BOOLEAN;" : "ALTER TABLE adds a field to an existing table", "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stB"), { w: 480, h: 110, label: "ALTER TABLE", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: ["The table has two fields.", "<b>ALTER TABLE ... ADD</b> creates a new field; existing records keep their data."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const B = (x, t, on) => SV.rect(x, 30, 170, 44, on ? "f3" : "cell", { rx: 8 }) + SV.text(x + 85, 57, t, "lbl bd", { "text-anchor": "middle", style: "font-size:12px" }); let o = B(20, "CUSTOMER(CustomerID)", true) + B(300, "SHOP_ORDER(CustomerID)", k >= 1); if (k >= 1) o += SV.path("M190,52 H300", "ax"); o += SV.text(20, 110, ["", "FOREIGN KEY (CustomerID)", "REFERENCES CUSTOMER(CustomerID)"][Math.min(k, 2)], "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stC"), { w: 520, h: 130, label: "Foreign key", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: ["CustomerID is the primary key of CUSTOMER.", "In SHOP_ORDER, <b>FOREIGN KEY (CustomerID)</b> marks the field as a foreign key...", "...<b>REFERENCES CUSTOMER(CustomerID)</b> names the table and field it links to."].map((c, i) => ({ cap: c, s: { i } })) });
})();
sqlLab("#ddl", DBT, "CREATE TABLE TEST(\nTestID VARCHAR(5) NOT NULL,\nDescription VARCHAR(30),\nTotalMarks INTEGER,\nPRIMARY KEY (TestID)\n);", { rows: 7 });
btnTable("tB", "tO", [
  ["A100, B245 (codes)", "VARCHAR(4)", "Text, may have letters"],
  ["Quantity 3, 1, 5", "INTEGER", "Whole numbers"],
  ["Price 22.50", "REAL", "Decimals"],
  ["Paid TRUE/FALSE", "BOOLEAN", "Two values"],
  ["13:00", "TIME", "A time of day"]
], ["Sample data", "Type", "Why"]);
btnTable("eB", "eO", [
  ["PRIMARY KEY CharacterID", "PRIMARY KEY (CharacterID)", "Brackets needed"],
  ["FOREIGN KEY (PlayerID)", "...REFERENCES PLAYER(PlayerID)", "Name the table and field"],
  ["SubjectCode VARCHAR NONULL", "SubjectCode VARCHAR NOT NULL", "Spelling"],
  ["SubjectName VARCHAR", "SubjectName VARCHAR,", "A comma is missing"]
], ["Faulty line", "Correct line", "Why"]);
''' + _prjs

finish("as-8-3-1-data-definition-language", "as831", "Data Definition Language (DDL)",
  "CREATE DATABASE, CREATE TABLE with data types, constraints and keys, and ALTER TABLE, with animations, a working SQL lab and the real Paper 1 questions from 2021 to 2026.",
  "8.3.1", "8 · Databases", "section 8.3 Data definition language (DDL) and data manipulation language (DML)", learn, watch, explore, _pr, real, where, past, review,
  "Part 1 is real 9618 questions on Data Definition Language (Paper 1), 2021 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", tips, js)
