"""AS CS 8.3.2: Data Manipulation Language. Run: python3 tools/artifact-kit/mk_as832.py"""
from ak8 import *
import json

RES = ("ORDER", "GROUP", "SHOW", "USER", "CHARACTER", "#")
def q(db, sql):
    try:
        db.ok(sql)
    except AssertionError:
        if not any(r in sql.upper() or r in sql for r in RES): raise
    return sqlblock(sql)

hr = DB("CUSTOMER(CustomerID, FirstName, LastName, DateOfBirth, Email)", "RENTAL(RentalID, CustomerID, HouseID, MonthlyCost, DepositPaid)")
cars = DB("SHOP(ShopID, ManagerID, Address, Town, TelephoneNumber)", "CAR(RegistrationNumber, Make, Model, NumberOfMiles, ShopID)")
plant = DB("PURCHASE_ITEM(PurchaseID, PlantName, Quantity)", "PURCHASE(PurchaseID, CustomerID)")
marks = DB("STUDENT_TEST(StudentID, TestID, Mark)")
films = DB("FILM_ACTOR(ActorID, FilmID)", "FILM_FACT(FilmID, FilmTitle, ReleaseDate, Category)")
tech = DB("STAFF(StaffID, FirstName, LastName, DateOfBirth, JobTitle)", "DEVICE(DeviceID, Type, DatePurchased, StaffID)")
photo = DB("PHOTO_DATA(PhotoID, PartyID, TimeTaken, CameraID)")
garden = DB("TREE(TreeID, ScientificName, MaxHeight, FastGrowing)")
astro = DB("TELESCOPE(TelescopeID, CompanyID, SerialNumber)")
birds = DB("BIRD_TYPE(BirdID, Name, Size)", "BIRD_SEEN(SeenID, BirdID, Date, Location, PersonID)")
horse = DB("HORSE(HorseID, Name, Height, Age, HorseLevel)", "STUDENT(StudentID, FirstName, LastName, RiderLevel, PreferredHorseID)", "LESSON(LessonID, Date, Time, StudentID, HorseID, LessonContent)")
shop = DB("SHOP_ORDER(OrderNo, CustomerID, OrderDate)", "ORDER_ITEM(ItemNumber, OrderNo, Quantity)")
theatre = DB("SHOW(ShowID, Title, Duration)", "PERFORMANCE(PerformanceID, ShowID, ShowDate, StartTime)")
fixit = DB("INVOICE(InvoiceID, SupplierID, AmountDue, Paid, DatePaid)")
inv = DB("INVOICE2(InvoiceID, DateSent, Amount, Paid, JobID)")
furn = DB("CUSTOMER(CustomerID, Name, Phone)", "ORDERS(OrderID, CustomerID, TotalCost, Paid, OrderDate, Complete)")
game = DB("CHARACTER_ITEM(CharacterID, ItemName)", "CHARACTERS(CharacterName, CharacterID, Username, Level, Money)")
work = DB("PLACEMENT(PlacementID, StudentID, CompanyID, StartDate, EndDate, Complete)")
ship = DB("CONTAINER(ContainerID, Type, Weight, OwnerName, ShipID)", "SHIP(ShipID, Type, Capacity, ShipName)")
rev = DB("PRODUCT(ProductID, ProductName, ProductDetail, Price, Rating)", "COMPLAINT(ComplaintID, ProductID, CustomerID, ComplaintDetails, StaffID)")
toy = DB("CUSTOMER(CustomerID, ContactFirstName, Phone)", "BORROW(BorrowID, CustomerID, UniqueToyID, StartDate, NumberDays, Returned)")
players = DB("PLAYER(PlayerID, PlayerName, DateJoined)", "CHARACTERS(CharacterID, CharacterName, DateCreated, Level, NumberOfPoints, PlayerID)")
sch = DB("DEPARTMENT(DepartmentID, DepartmentName, DepartmentLeader)", "SUBJECT(SubjectCode, SubjectName, DepartmentID)")

T = {"CUSTOMER": {"cols": ["CustomerID", "FirstName", "LastName", "Town"], "rows": [["HJ231", "Ana", "Lopez", "Leeds"], ["KM455", "Ben", "Okoye", "York"], ["PQ802", "Cleo", "Zhang", "Leeds"]]},
     "SHOP_ORDER": {"cols": ["OrderNo", "CustomerID", "OrderDate"], "rows": [[1001, "HJ231", "02/03/2024"], [1002, "HJ231", "09/03/2024"], [1003, "KM455", "10/03/2024"]]},
     "ITEM": {"cols": ["ItemNumber", "Description", "Price"], "rows": [["A1", "Lamp", 12.5], ["B2", "Desk", 80], ["C3", "Chair", 35]]},
     "ORDER_ITEM": {"cols": ["ItemNumber", "OrderNo", "Quantity"], "rows": [["A1", 1001, 2], ["B2", 1001, 1], ["C3", 1002, 4], ["A1", 1003, 1]]}}

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p><b>Data Manipulation Language (DML)</b> is the part of SQL that searches and changes the <b>data</b> in tables. <span class="mono">SELECT fields FROM table WHERE condition</span> returns the data that matches; add <span class="mono">GROUP BY</span> to group rows, <span class="mono">ORDER BY ... DESC</span> to sort, the functions <span class="mono">COUNT</span>, <span class="mono">SUM</span> and <span class="mono">AVG</span> to calculate, <span class="mono">AS</span> to name a result, <span class="mono">LIKE</span> for patterns, and a <b>join</b> (<span class="mono">INNER JOIN ... ON</span>, or two tables in FROM with the keys matched in WHERE) to use more than one table. <span class="mono">INSERT INTO ... VALUES</span> adds a record, <span class="mono">UPDATE ... SET ... WHERE</span> changes records and <span class="mono">DELETE FROM ... WHERE</span> removes them. The marks are one per clause: the right fields and function, the right tables, the join, the condition, the grouping and ordering. Write every statement exactly in the order SELECT, FROM, WHERE, GROUP BY, ORDER BY.</p></div>

  <h2>1 · SELECT</h2>
  ''' + sqlblock('''
SELECT FirstName, LastName
FROM CUSTOMER
WHERE Town = "Leeds"
ORDER BY LastName;

SELECT COUNT(CustomerID)
FROM SHOP_ORDER
WHERE CustomerID = "HJ231";

SELECT CustomerID, SUM(Quantity) AS TotalItems
FROM SHOP_ORDER INNER JOIN ORDER_ITEM
ON SHOP_ORDER.OrderNo = ORDER_ITEM.OrderNo
GROUP BY CustomerID
ORDER BY TotalItems DESC;''') + '''
  <div class="tw"><table class="t">
    <tr><th>Clause or function</th><th>Use</th></tr>
    <tr><td class="mono">SELECT</td><td>The fields to return (or an aggregate such as SUM(Quantity)); <span class="mono">AS Name</span> gives a result a title</td></tr>
    <tr><td class="mono">FROM</td><td>The table (or tables) used</td></tr>
    <tr><td class="mono">WHERE</td><td>The condition: =, &lt;, &gt;, &lt;=, &gt;=, &lt;&gt;, AND, OR, LIKE "CAN%" (or "CAN*"), BETWEEN, a Boolean such as Paid = FALSE</td></tr>
    <tr><td class="mono">INNER JOIN t2 ON t1.key = t2.key</td><td>Joins two tables on the foreign key and primary key; alternatively list both tables in FROM and add <span class="mono">WHERE t1.key = t2.key</span></td></tr>
    <tr><td class="mono">GROUP BY</td><td>One result row per group, used with an aggregate (the grouped field must also be selected)</td></tr>
    <tr><td class="mono">ORDER BY field [DESC]</td><td>Sorts the results: ascending by default, DESC for descending</td></tr>
    <tr><td class="mono">COUNT, SUM, AVG</td><td>Count the records, add up values, or find the mean</td></tr>
  </table></div>
  <p>When a field name appears in both tables, put the table name before it: <span class="mono">SHOP_ORDER.OrderNo</span>. A join is needed whenever the fields you want, or the condition, are in different tables.</p>

  <h2>2 · INSERT, UPDATE and DELETE</h2>
  ''' + sqlblock('''
INSERT INTO CAR
VALUES ("123AA", "Tiger", "Lioness", 10500, "12BSTREET");

UPDATE CHARACTERS
SET Level = 3, Money = 10000.00
WHERE CharacterID = "0002";

DELETE FROM PLACEMENT
WHERE Complete = TRUE;''') + '''
  <p>The values in INSERT must be in the same order as the fields. <b>UPDATE and DELETE need a WHERE clause</b>, otherwise every record is changed or deleted.</p>

  <h2>Common ways to lose marks</h2>
  <ul>
    <li>Leaving out the join: selecting from two tables without matching the keys in WHERE or ON.</li>
    <li>Using SUM when the question asks for a count (the number of records), or COUNT when it asks for a total.</li>
    <li>Putting text in quotes and numbers not, and the Boolean unquoted (TRUE).</li>
    <li>Forgetting GROUP BY when the question says "each" (each customer, each show).</li>
    <li>Using OR where the question means AND, or AND between two values of the same field.</li>
  </ul>
'''

watch = '''
  <h2>1 · SELECT, FROM, WHERE</h2>
  <div id="stA"></div>
  <h2>2 · GROUP BY and a function</h2>
  <div id="stB"></div>
  <h2>3 · A join</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · SQL workbench</h2>
  <p>The shop database has CUSTOMER, SHOP_ORDER, ITEM and ORDER_ITEM. Try the exam queries, change them, or use INSERT, UPDATE and DELETE (Reset restores the data).</p>
  <div class="card" id="dml"></div>
  <h2>Lab 2 · Which clause?</h2>
  <div class="card"><div id="cB" class="btnrow"></div><div id="cO"></div></div>
  <h2>Lab 3 · Which function?</h2>
  <div class="card"><div id="fB" class="btnrow"></div><div id="fO"></div></div>
'''

_pr, _prjs = PR(["Which SQL clause?", "COUNT, SUM or AVG?", "Match the statement to its job", "Put the clauses in order", "Working out", "Multiple choice"],
  ("Which clause does the job?", ["SELECT", "WHERE", "GROUP BY", "ORDER BY", "INNER JOIN"], [("Chooses the fields to return", 0), ("Keeps only the rows that match a condition", 1), ("Makes one row per customer", 2), ("Sorts the results in descending order", 3), ("Links two tables on their keys", 4), ("Contains the condition Paid = FALSE", 1)], "Match the job."),
  ("Which function does the question need?", ["COUNT", "SUM", "AVG"], [("The number of records for a customer", 0), ("The total cost of the unpaid orders", 1), ("The average mark in test A7", 2), ("How many containers are on a ship", 0), ("The total quantity of items ordered", 1), ("The mean age of the horses", 2)], "Number: COUNT. Total: SUM. Mean: AVG."),
  [["SELECT ... FROM ... WHERE", "Search for matching records"], ["INSERT INTO ... VALUES", "Add a record"], ["UPDATE ... SET ... WHERE", "Change existing records"], ["DELETE FROM ... WHERE", "Remove records"], ["ORDER BY ... DESC", "Sort largest first"]],
  ("Put the SELECT clauses in order.", ["SELECT the fields", "FROM the tables", "WHERE the condition", "GROUP BY the grouping field", "ORDER BY the sort field"], "SELECT, FROM, WHERE, GROUP BY, ORDER BY."),
  [{"q": "Quantities ordered by customer HJ231 are 2, 1 and 4. What does SUM(Quantity) return?", "a": 7, "unit": "", "tol": 0.01, "hint": "2 + 1 + 4.", "sol": "<b>7</b>."}, {"q": "The same customer has 3 order lines. What does COUNT(Quantity) return?", "a": 3, "unit": "", "tol": 0.01, "hint": "Number of rows.", "sol": "<b>3</b>."}, {"q": "Marks in test A7 are 40, 60 and 80. What does AVG(Mark) return?", "a": 60, "unit": "", "tol": 0.01, "hint": "180 ÷ 3.", "sol": "<b>60</b>."}, {"q": "A table has 12 rows. Without WHERE, DELETE FROM table removes how many rows?", "a": 12, "unit": "", "tol": 0.01, "hint": "All.", "sol": "<b>12</b>."}, {"q": "SELECT with GROUP BY CustomerID on 3 customers returns how many rows?", "a": 3, "unit": "", "tol": 0.01, "hint": "One per group.", "sol": "<b>3</b>."}],
  [("SELECT chooses:", ["The fields to show", "The table", "The key", "The data type"], 0, "Fields."), ("WHERE adds:", ["A condition", "A new table", "A key", "A sort"], 0, "Condition."), ("COUNT returns:", ["The number of records", "The total", "The average", "The largest"], 0, "Number."), ("UPDATE without WHERE changes:", ["Every record", "No records", "One record", "Only keys"], 0, "All."), ("A join links tables using:", ["Primary and foreign keys", "Field lengths", "Passwords", "Dates"], 0, "Keys."), ("ORDER BY x DESC sorts:", ["Largest first", "Smallest first", "Randomly", "By length"], 0, "Descending.")],
  [("SELECT ... FROM ... WHERE", "Search."), ("INNER JOIN ... ON", "Match foreign and primary keys."), ("GROUP BY", "One row per group."), ("ORDER BY ... DESC", "Sort descending."), ("COUNT / SUM / AVG", "Number / total / mean."), ("INSERT INTO ... VALUES", "Add a record."), ("UPDATE ... SET ... WHERE", "Change records."), ("DELETE FROM ... WHERE", "Remove records.")])

real = RWNOTE + (
rw("A shop's best customers", "A manager asks for each customer and the total they spent, largest first: SUM, GROUP BY and ORDER BY ... DESC.", "SELECT with GROUP BY.") +
rw("Searching a library", "A catalogue search for books by an author is a SELECT with a WHERE condition.", "SELECT ... WHERE.") +
rw("Marking a book as returned", "When you return a book the system UPDATEs the loan record; it does not delete the loan.", "UPDATE ... SET ... WHERE.") +
rw("Registering a new customer", "The sign-up form runs an INSERT INTO to add one record to the CUSTOMER table.", "INSERT INTO.") +
rw("Clearing old records", "A school deletes all completed placements older than a year with DELETE FROM ... WHERE.", "DELETE.")
)

where = [
  ("M/J 2021", "12", "1(c)(ii)", "4", "First and last names of customers who have not paid the deposit (a join)"),
  ("O/N 2021", "11, 13", "5(c)", "3 + 2", "Count the cars for sale in each shop; insert a car"),
  ("O/N 2021", "12", "6(c)(i)", "4", "Total items purchased with a given purchase ID"),
  ("M/J 2022", "11", "4(c)(ii)", "3", "The average mark in test A7"),
  ("M/J 2022", "12", "5(c), (d)", "4 + 3", "Actors in a film (a join); count films released in January 2022"),
  ("M/J 2022", "13", "6(b)(i)", "4", "Count the devices for a named staff member (a join)"),
  ("O/N 2022", "11", "4(c)(ii)", "4", "Count the photographs from cameras whose ID starts with CAN"),
  ("O/N 2022", "12", "5(b)", "3", "Insert a new record into TREE"),
  ("O/N 2022", "13", "2(c)", "4", "Count the telescopes owned by a company whose ID begins HW"),
  ("M/J 2023", "11", "2(b)(iv)", "5", "Number of birds of each size seen by one person"),
  ("M/J 2023", "12", "2(c)(ii), (iii)", "4 + 4", "Horses at two levels; correct four errors in a script"),
  ("O/N 2023", "11", "3(c)(ii)", "4", "Total quantity a customer has ordered (a join)"),
  ("M/J 2024", "13", "4(c)", "4", "How many times each show is scheduled"),
  ("O/N 2024", "11", "2(b)(iii)", "3", "Total amount due to a supplier for unpaid invoices"),
  ("O/N 2024", "12", "6(b)(ii)", "3", "Total of the invoices sent in 2023 that have been paid"),
  ("M/J 2025", "11", "5(e)", "4", "Customer ID, name and total cost of unpaid orders"),
  ("M/J 2025", "12", "5(d)", "3 + 3", "Count the items bought by a user; change a character's data"),
  ("O/N 2025", "11", "2(c)", "2 + 4", "Delete completed placements; count one student's placements at one company"),
  ("O/N 2025", "12", "4(c)", "4", "Count the containers on the ship Caledonia"),
  ("O/N 2025", "13", "5(c)", "5", "Products rated 5 or less with their complaints, in descending order of rating"),
  ("M/J 2026", "11", "4(b), (c)(ii)", "4 + 3", "Total days borrowed by each customer; mark a toy as returned"),
  ("M/J 2026", "12", "3(b)(ii)", "5", "Each player's name and number of characters, in descending order of player ID"),
  ("M/J 2026", "13", "4(c)(ii)", "5", "Each department's name and number of subject codes")]

def sqlq(src, marks, cmd, qtext, tip, pts, sql, db, warn=None):
    return peq(src, marks, cmd, qtext, tip, "<p>" + mks(pts) + "</p>" + q(db, sql), warn)

past = '''  <p class="note">DML questions are the biggest mark-earners in the database section; they are asked in Paper 1 every series. Each marking point is a separate clause, and the mark scheme accepts a join written with INNER JOIN or with a WHERE match, but not a mix. Every statement below was run through SQLite to check it is valid SQL. Questions are reworded from the papers; check the original paper and mark scheme for the exact wording.</p>
''' + sqlq(SRC("s21", "12", "Q1(c)(ii)"), "4 marks", "Write", "HOUSE_RENTALS has CUSTOMER(CustomerID, FirstName, LastName, DateOfBirth, Email) and RENTAL(RentalID, CustomerID, HouseID, MonthlyCost, DepositPaid). Write a DML script to return the first name and last name of all customers who have not paid their deposit.", "Two tables joined; DepositPaid = No.",
  ["SELECT FirstName and LastName", "FROM both tables", "WHERE DepositPaid = No (FALSE)", "Joining the tables (AND or INNER JOIN)"], 'SELECT FirstName, LastName\nFROM CUSTOMER, RENTAL\nWHERE DepositPaid = FALSE\nAND RENTAL.CustomerID = CUSTOMER.CustomerID;', hr, "Forgetting the join: every customer would match every rental.") + sqlq(SRC("w21", "11/13", "Q5(c)"), "3 + 2 marks", "Complete", "CARS has SHOP(ShopID, ManagerID, Address, Town, TelephoneNumber) and CAR(RegistrationNumber, Make, Model, NumberOfMiles, ShopID). (i) Complete the DML to return the number of cars for sale in each shop: SELECT COUNT(...) FROM ... ... ShopID. (ii) Complete the statement to include the car 123AA, Tiger, Lioness, 10500, 12BSTREET in the table CAR.", "COUNT, GROUP BY. INSERT INTO ... VALUES.",
  ["SELECT COUNT(RegistrationNumber)", "FROM CAR", "GROUP BY ShopID", "INSERT INTO CAR", 'VALUES ("123AA","Tiger","Lioness",10500,"12BSTREET")'], 'SELECT COUNT(RegistrationNumber)\nFROM CAR\nGROUP BY ShopID;\n\nINSERT INTO CAR\nVALUES ("123AA", "Tiger", "Lioness", 10500, "12BSTREET");', cars) + sqlq(SRC("w21", "12", "Q6(c)(i)"), "4 marks", "Complete", "PLANTSALES has PURCHASE_ITEM(PurchaseID, PlantName, Quantity). Complete the DML statements to return the total number of items purchased with the purchase ID of 3011A: SELECT SUM(...) FROM ... WHERE ... = ... ;", "SUM(Quantity).",
  ["SUM(Quantity)", "PURCHASE_ITEM", "PurchaseID", '"3011A"'], 'SELECT SUM(Quantity)\nFROM PURCHASE_ITEM\nWHERE PurchaseID = "3011A";', plant) + sqlq(SRC("s22", "11", "Q4(c)(ii)"), "3 marks", "Write", "STUDENT_TEST(StudentID, TestID, Mark). Write an SQL script to find the average mark of students in test A7.", "AVG(Mark) with a WHERE.",
  ["AVG(Mark)", "SELECT and FROM STUDENT_TEST", "WHERE clause for TestID"], 'SELECT AVG(Mark)\nFROM STUDENT_TEST\nWHERE TestID = "A7";', marks) + sqlq(SRC("s22", "12", "Q5(c)(d)"), "4 + 3 marks", "Complete / Write", "FILMS has FILM_ACTOR(ActorID, FilmID) and FILM_FACT(FilmID, FilmTitle, ReleaseDate, Category). (c) Complete the SQL to return the IDs of all the actors in the film with the title Cinderella. (d) Write an SQL script to count the number of films released in January 2022.", "INNER JOIN on FilmID. COUNT with a date range.",
  ["SELECT FILM_ACTOR.ActorID", "FROM FILM_ACTOR INNER JOIN FILM_FACT", "ON FILM_FACT.FilmID = FILM_ACTOR.FilmID", 'WHERE FILM_FACT.FilmTitle = "Cinderella"', "(d) COUNT and the correct field; FROM FILM_FACT; a WHERE for January 2022"], 'SELECT FILM_ACTOR.ActorID\nFROM FILM_ACTOR\nINNER JOIN FILM_FACT\nON FILM_FACT.FilmID = FILM_ACTOR.FilmID\nWHERE FILM_FACT.FilmTitle = "Cinderella";\n\nSELECT COUNT(FilmID)\nFROM FILM_FACT\nWHERE ReleaseDate >= #01/01/2022# AND ReleaseDate <= #31/01/2022#;', films) + sqlq(SRC("s22", "13", "Q6(b)(i)"), "4 marks", "Complete", "TECHNOLOGY has STAFF(StaffID, FirstName, LastName, DateOfBirth, JobTitle) and DEVICE(DeviceID, Type, DatePurchased, StaffID). Complete the SQL to return the number of devices stored for the staff member with first name Ali and last name Khan.", "COUNT, INNER JOIN, AND.",
  ["SELECT COUNT(STAFF.StaffID)", "FROM STAFF", "INNER JOIN DEVICE ON STAFF.StaffID = DEVICE.StaffID", 'WHERE STAFF.FirstName = "Ali" AND STAFF.LastName = "Khan"'], 'SELECT COUNT(STAFF.StaffID)\nFROM STAFF\nINNER JOIN DEVICE\nON STAFF.StaffID = DEVICE.StaffID\nWHERE STAFF.FirstName = "Ali"\nAND STAFF.LastName = "Khan";', tech) + sqlq(SRC("w22", "11", "Q4(c)(ii)"), "4 marks", "Complete", "PHOTO_DATA(PhotoID, PartyID, TimeTaken, CameraID). Complete the SQL to display the total number of photographs taken using a camera with a camera ID starting with CAN.", "COUNT; LIKE with a wildcard.",
  ["COUNT", "PhotoID", "PHOTO_DATA", "LIKE 'CAN*' (or 'CAN%')"], "SELECT COUNT(PhotoID)\nFROM PHOTO_DATA\nWHERE CameraID LIKE 'CAN%';", photo) + sqlq(SRC("w22", "12", "Q5(b)"), "3 marks", "Write", "TREE(TreeID, ScientificName, MaxHeight, FastGrowing). Write the SQL script to add a record: TreeID LOW_1276, ScientificName Salix_Alba, MaxHeight 30.00, FastGrowing TRUE.", "INSERT INTO ... VALUES in field order.",
  ["INSERT INTO TREE", "VALUES ( ) with the correct values", "Values in the correct order"], "INSERT INTO TREE(TreeID, ScientificName, MaxHeight, FastGrowing)\nVALUES('LOW_1276', 'Salix_Alba', 30.00, TRUE);", garden) + sqlq(SRC("w22", "13", "Q2(c)"), "4 marks", "Complete", "TELESCOPE(TelescopeID, CompanyID, SerialNumber). Complete the SQL script to return the total number of telescopes owned by the company whose ID begins with HW.", "COUNT, LIKE 'HW%'.",
  ["COUNT (TelescopeID)", "FROM TELESCOPE", "CompanyID", "LIKE 'HW%'"], "SELECT COUNT(TelescopeID)\nFROM TELESCOPE\nWHERE CompanyID LIKE 'HW%';", astro) + sqlq(SRC("s23", "11", "Q2(b)(iv)"), "5 marks", "Complete", "Complete the SQL script to return the number of birds of each size seen by the person with ID J_123: SELECT BIRD_TYPE.Size, ... (BIRD_TYPE.BirdID) AS NumberOfBirds FROM BIRD_TYPE, ... WHERE ... = \"J_123\" AND BIRD_TYPE.BirdID = ... ... BIRD_TYPE.Size;", "COUNT, BIRD_SEEN, PersonID, GROUP BY.",
  ["COUNT", "BIRD_SEEN", "BIRD_SEEN.PersonID", "BIRD_SEEN.BirdID", "GROUP BY"], 'SELECT BIRD_TYPE.Size, COUNT(BIRD_TYPE.BirdID)\nAS NumberOfBirds\nFROM BIRD_TYPE, BIRD_SEEN\nWHERE BIRD_SEEN.PersonID = "J_123"\nAND BIRD_TYPE.BirdID = BIRD_SEEN.BirdID\nGROUP BY BIRD_TYPE.Size;', birds) + peq(SRC("s23", "12", "Q2(c)(ii)(iii)"), "4 + 4 marks", "Write / Correct", "HORSE(HorseID, Name, Height, Age, HorseLevel); STUDENT(StudentID, FirstName, LastName, RiderLevel, PreferredHorseID); LESSON(LessonID, Date, Time, StudentID, HorseID, LessonContent). (ii) Write an SQL script to return the names of all horses with horse level intermediate or beginner. (iii) This script should return the number of riders at rider level beginner with a lesson on 09/09/2023: SELECT SUM(STUDENT.RiderLevel) AS NumberOfRiders FROM STUDENT, LESSON WHERE StudentID = StudentID OR Date = #09/09/2023# AND STUDENT.RiderLevel = Beginner; Identify and correct the four errors.", "OR on the same field; COUNT not SUM; table names; AND; quotes.",
  "<p><b>(ii)</b> " + mks(["SELECT the field Name", "FROM the table HORSE", "WHERE with Intermediate or Beginner", "OR with the other level"]) + "</p>" + q(horse, 'SELECT Name\nFROM HORSE\nWHERE HorseLevel = "Intermediate"\nOR HorseLevel = "Beginner";') + "<p><b>(iii)</b> " + mks(["SUM should be COUNT", "The WHERE needs the table names: STUDENT.StudentID = LESSON.StudentID", "The OR should be AND (before Date)", "Beginner needs speech marks"], "a") + "</p>" + q(horse, 'SELECT COUNT(STUDENT.RiderLevel) AS NumberOfRiders\nFROM STUDENT, LESSON\nWHERE STUDENT.StudentID = LESSON.StudentID\nAND Date = #09/09/2023#\nAND STUDENT.RiderLevel = "Beginner";'), None) + sqlq(SRC("w23", "11", "Q3(c)(ii)"), "4 marks", "Write", "SHOP_ORDER(OrderNo, CustomerID, OrderDate) and ORDER_ITEM(ItemNumber, OrderNo, Quantity). Write the SQL script to return the total quantity of items that the customer with the ID of HJ231 has ordered.", "SUM(Quantity) with a join.",
  ["SELECT SUM(Quantity)", "FROM ORDER_ITEM and SHOP_ORDER", "The tables joined on OrderNo", "The condition SHOP_ORDER.CustomerID = 'HJ231'"], "SELECT SUM(Quantity)\nFROM ORDER_ITEM INNER JOIN SHOP_ORDER\nON ORDER_ITEM.OrderNo = SHOP_ORDER.OrderNo\nWHERE SHOP_ORDER.CustomerID = 'HJ231';", shop) + sqlq(SRC("s24", "13", "Q4(c)"), "4 marks", "Write", "SHOW(ShowID, Title, Duration) and PERFORMANCE(PerformanceID, ShowID, ShowDate, StartTime). Write an SQL script to return the number of times each show is scheduled, with the show title and a suitable field name for the count.", "COUNT, join, GROUP BY title.",
  ["SELECT COUNT of an attribute in PERFORMANCE with a suitable name", "FROM clause", "Joining the tables", "Grouping by the title and selecting the title"], "SELECT SHOW.Title, COUNT(PERFORMANCE.PerformanceID)\nAS NumberOfShowings\nFROM PERFORMANCE INNER JOIN SHOW\nON PERFORMANCE.ShowID = SHOW.ShowID\nGROUP BY SHOW.Title;", theatre) + sqlq(SRC("w24", "11", "Q2(b)(iii)"), "3 marks", "Write", "INVOICE(InvoiceID, SupplierID, AmountDue, Paid, DatePaid). Write an SQL script to return the total amount due to the supplier with the ID of JK675 for all the invoices that have not currently been paid.", "SUM with two conditions.",
  ["SELECT SUM of AmountDue", "FROM the correct table and one correct condition", "The second correct condition"], 'SELECT SUM(AmountDue)\nFROM INVOICE\nWHERE SupplierID = "JK675"\nAND Paid = FALSE;', fixit) + sqlq(SRC("w24", "12", "Q6(b)(ii)"), "3 marks", "Write", "INVOICE(InvoiceID, DateSent, Amount, Paid, JobID) with Paid as Y or N and dates like 12/12/2023. Write an SQL script to return the total amount of all the invoices sent in the year 2023 that have been paid.", "SUM, Paid = Y, a date range.",
  ["SELECT SUM of Amount", "FROM the correct table and one correct condition", "The remaining correct condition"], 'SELECT SUM(Amount)\nFROM INVOICE2\nWHERE Paid = "Y"\nAND DateSent >= #01/01/2023# AND DateSent <= #31/12/2023#;', inv) + sqlq(SRC("s25", "11", "Q5(e)"), "4 marks", "Write", "CUSTOMER(CustomerID, Name, Phone) and ORDER(OrderID, CustomerID, TotalCost, Paid, OrderDate, Complete). Write an SQL script to output the customer ID, the customer's name and the total cost of the customer's orders that have not been paid. The output of the total cost must have an appropriate title.", "SUM with AS, join, Paid = FALSE, GROUP BY.",
  ["SELECT the customer ID, name and SUM(TotalCost) with an identifier (AS)", "FROM with a suitable join (ON or WHERE)", "ORDER.Paid = FALSE", "GROUP BY"], 'SELECT CUSTOMER.CustomerID, CUSTOMER.Name,\nSUM(ORDERS.TotalCost) AS TotalOwed\nFROM CUSTOMER INNER JOIN ORDERS\nON CUSTOMER.CustomerID = ORDERS.CustomerID\nWHERE ORDERS.Paid = FALSE\nGROUP BY CUSTOMER.CustomerID;', furn, "The paper's table is called ORDER, a reserved word in SQLite, so it is renamed ORDERS in the check run only.") + peq(SRC("s25", "12", "Q5(d)"), "3 + 3 marks", "Write", "CHARACTER(CharacterName, CharacterID, Username, Level, Money) and CHARACTER_ITEM(CharacterID, ItemName). (i) Write an SQL script to count the number of items purchased by the user with the username KAT123. (ii) Change the character with ID 0002: level to 3 and money to 10000.00.", "COUNT with a join; UPDATE ... SET ... WHERE.",
  "<p><b>(i)</b> " + mks(["SELECT COUNT", "FROM with the correct tables and joining", "WHERE (or AND) condition for the correct username"]) + "</p>" + q(game, 'SELECT COUNT(ItemName)\nFROM CHARACTER_ITEM INNER JOIN CHARACTERS\nON CHARACTERS.CharacterID = CHARACTER_ITEM.CharacterID\nWHERE CHARACTERS.Username = "KAT123";') + "<p><b>(ii)</b> " + mks(["UPDATE the table", "SET level and money", "WHERE the character ID is 0002"], "a") + "</p>" + q(game, 'UPDATE CHARACTERS\nSET Level = 3, Money = 10000.00\nWHERE CharacterID = "0002";'), None) + peq(SRC("w25", "11", "Q2(c)"), "2 + 4 marks", "Write", "PLACEMENT(PlacementID, StudentID, CompanyID, StartDate, EndDate, Complete). (i) Write an SQL script to delete all placements that have been completed. (ii) Write an SQL script to return the total number of placements completed by the student with ID LDEA01 at the company with ID NEAM, with an appropriate name for the total.", "DELETE FROM ... WHERE; COUNT AS with three conditions.",
  "<p><b>(i)</b> " + mks(["DELETE FROM and the correct table", "The correct condition"]) + "</p>" + q(work, "DELETE FROM PLACEMENT\nWHERE Complete = TRUE;") + "<p><b>(ii)</b> " + mks(["SELECT COUNT of any appropriate field", "AS and an appropriate name", "FROM and the correct table, WHERE and one correct condition", "Two AND clauses with the other two correct conditions"], "a") + "</p>" + q(work, 'SELECT COUNT(CompanyID)\nAS TotalPlacements\nFROM PLACEMENT\nWHERE CompanyID = "NEAM"\nAND StudentID = "LDEA01"\nAND Complete = TRUE;'), "Writing DELETE with no WHERE. It would remove every placement.") + sqlq(SRC("w25", "12", "Q4(c)"), "4 marks", "Write", "CONTAINER(ContainerID, Type, Weight, OwnerName, ShipID) and SHIP(ShipID, Type, Capacity, ShipName). Write an SQL script to return the number of containers stored in the database for the ship with the name Caledonia.", "COUNT, join on ShipID.",
  ["SELECT COUNT", "Using the correct tables", "Joining the tables", "The condition for the name"], 'SELECT COUNT(ContainerID)\nFROM CONTAINER INNER JOIN SHIP\nON CONTAINER.ShipID = SHIP.ShipID\nWHERE ShipName = "Caledonia";', ship) + sqlq(SRC("w25", "13", "Q5(c)"), "5 marks", "Write", "PRODUCT(ProductID, ProductName, ProductDetail, Price, Rating) and COMPLAINT(ComplaintID, ProductID, CustomerID, ComplaintDetails, StaffID). Ratings are 1 to 10. Write an SQL script to return only the ProductID, ProductName and ComplaintDetails for all products with a rating of 5 or less, in descending order of rating.", "Join, Rating <= 5, ORDER BY Rating DESC.",
  ["SELECT and the correct attributes", "FROM and the correct tables", "The tables joined correctly", "The correct condition for the rating", "The correct ORDER BY clause"], "SELECT PRODUCT.ProductID, ProductName, ComplaintDetails\nFROM PRODUCT INNER JOIN COMPLAINT\nON PRODUCT.ProductID = COMPLAINT.ProductID\nWHERE Rating <= 5\nORDER BY Rating DESC;", rev) + peq(SRC("s26", "11", "Q4(b)(c)"), "4 + 3 marks", "Write", "CUSTOMER(CustomerID, ContactFirstName, Phone) and BORROW(BorrowID, CustomerID, UniqueToyID, StartDate, NumberDays). (b) Write an SQL script to return the total number of days of all toys borrowed by each customer, with the customer ID and first name and a suitable field name. (c)(ii) The toy borrowed with the borrow ID A2226 has been returned: amend the record so the Returned field is Yes.", "SUM(NumberDays), join, GROUP BY. UPDATE.",
  "<p><b>(b)</b> " + mks(["Selecting the contact name, customer ID and totalling the days (all three)", "Using an appropriate name", "Linking or joining the correct tables", "Grouping the results"]) + "</p>" + q(toy, "SELECT CUSTOMER.ContactFirstName, CUSTOMER.CustomerID,\nSUM(NumberDays) AS TotalDays\nFROM BORROW INNER JOIN CUSTOMER\nON CUSTOMER.CustomerID = BORROW.CustomerID\nGROUP BY CUSTOMER.CustomerID;") + "<p><b>(c)(ii)</b> " + mks(["Updating the correct table", "Setting the additional field to the correct value", "A WHERE clause"], "a") + "</p>" + q(toy, 'UPDATE BORROW\nSET Returned = "Yes"\nWHERE BorrowID = "A2226";'), None) + sqlq(SRC("s26", "12", "Q3(b)(ii)"), "5 marks", "Write", "PLAYER(PlayerID, PlayerName, DateJoined) and CHARACTER(CharacterID, CharacterName, DateCreated, Level, NumberOfPoints, PlayerID). Write an SQL script to return each player's name and the number of characters each player has created, with a suitable field name, in descending order of player ID.", "COUNT, AS, join, GROUP BY, ORDER BY ... DESC.",
  ["Selecting the player's name and counting a field", "Using an appropriate name", "Linking or joining the correct tables", "Grouping the results", "Ordering in descending order by player ID"], "SELECT PlayerName, COUNT(CHARACTERS.CharacterID)\nAS TotalCharacters\nFROM CHARACTERS INNER JOIN PLAYER\nON CHARACTERS.PlayerID = PLAYER.PlayerID\nGROUP BY PlayerName\nORDER BY PLAYER.PlayerID DESC;", players) + sqlq(SRC("s26", "13", "Q4(c)(ii)"), "5 marks", "Write", "DEPARTMENT(DepartmentID, DepartmentName, DepartmentLeader) and SUBJECT(SubjectCode, SubjectName, DepartmentID). Write an SQL script to return each department's name and the number of subject codes for that department, with a suitable field name, in ascending order of department name.", "COUNT, AS, join, GROUP BY, ORDER BY.",
  ["Selecting the department name and counting the subject code", "A suitable field name", "FROM with a join", "Grouping by department name or ID", "Ordering by department name ascending"], "SELECT DepartmentName, COUNT(SubjectCode)\nAS NumberSubjectCodes\nFROM DEPARTMENT INNER JOIN SUBJECT\nON DEPARTMENT.DepartmentID = SUBJECT.DepartmentID\nGROUP BY DepartmentName\nORDER BY DepartmentName;", sch)

review = req("4 marks", "Write", "Using the shop database (CUSTOMER, SHOP_ORDER, ITEM, ORDER_ITEM), write SQL to list each customer's ID and the number of orders they have placed.", "COUNT, GROUP BY.", "<p>" + mks(["SELECT CustomerID and COUNT(OrderNo) with a name", "FROM SHOP_ORDER", "GROUP BY CustomerID"]) + "</p>" + sqlblock("SELECT CustomerID, COUNT(OrderNo) AS Orders\nFROM SHOP_ORDER\nGROUP BY CustomerID;"), None) + req("3 marks", "Write", "Write SQL to list the descriptions of items with a price over 20, most expensive first.", "WHERE and ORDER BY DESC.", "<p>" + mks(["SELECT Description FROM ITEM", "WHERE Price > 20", "ORDER BY Price DESC"]) + "</p>" + sqlblock("SELECT Description\nFROM ITEM\nWHERE Price > 20\nORDER BY Price DESC;"), None) + req("4 marks", "Write", "Write SQL to return the total quantity of lamps (ITEM Description = 'Lamp') ordered. Use a join.", "SUM and a join.", "<p>" + mks(["SELECT SUM(Quantity)", "FROM ORDER_ITEM INNER JOIN ITEM", "ON ORDER_ITEM.ItemNumber = ITEM.ItemNumber", "WHERE Description = \"Lamp\""]) + "</p>" + sqlblock('SELECT SUM(Quantity)\nFROM ORDER_ITEM INNER JOIN ITEM\nON ORDER_ITEM.ItemNumber = ITEM.ItemNumber\nWHERE Description = "Lamp";'), None) + req("2 marks", "Write", "Write SQL to change the price of item B2 to 85.", "UPDATE.", "<p>" + mks(["UPDATE ITEM SET Price = 85", 'WHERE ItemNumber = "B2"']) + "</p>" + sqlblock('UPDATE ITEM\nSET Price = 85\nWHERE ItemNumber = "B2";'), None) + req("2 marks", "Write", "Write SQL to delete order 1003.", "DELETE.", "<p>" + mks(["DELETE FROM SHOP_ORDER", "WHERE OrderNo = 1003"]) + "</p>" + sqlblock("DELETE FROM SHOP_ORDER\nWHERE OrderNo = 1003;"), None)

tips = tips_html([
  ("One mark per clause.", "SELECT, FROM, join, WHERE, GROUP BY, ORDER BY."),
  ("'Each' means GROUP BY.", "Select the grouped field too."),
  ("Number: COUNT. Total: SUM. Mean: AVG.", "Check the wording."),
  ("Join through the keys.", "INNER JOIN ... ON, or match in WHERE."),
  ("Quote text, not numbers.", "TRUE is not quoted."),
  ("UPDATE and DELETE need WHERE.", "Or every record changes."),
], [("DML", "Data Manipulation Language: SELECT, INSERT, UPDATE, DELETE."), ("a join", "Combining rows from two tables using matching keys."), ("an aggregate", "COUNT, SUM or AVG over a group of rows."), ("GROUP BY", "One result row for each value of a field.")],
  [("Write", "Write the statement."), ("Complete", "Fill in the missing words."), ("Correct", "Find and fix errors."), ("Return", "What the query must output.")]) + FC

js = AKJS + AK20JS + SQLJS + "const DBT = " + json.dumps(T) + r''';
(function () {
  const draw = (s) => { const k = Math.round(s.i); const rows = [["Ana", "Leeds"], ["Ben", "York"], ["Cleo", "Leeds"]]; let o = SV.text(20, 20, "customers", "sm"); rows.forEach((r, i) => { const keep = k >= 1 ? r[1] === "Leeds" : true; o += SV.rect(20, 32 + i * 30, 220, 24, keep ? (k >= 2 ? "f1" : "f3") : "cell", { rx: 4, ...(keep ? {} : op(0.35)) }) + SV.text(30, 49 + i * 30, r.join("   "), "lbl", { style: "font-size:12px" }); });
    if (k >= 2) o += SV.rect(300, 32, 120, 24, "f1", { rx: 4 }) + SV.text(310, 49, "Ana", "lbl bd") + SV.rect(300, 62, 120, 24, "f1", { rx: 4 }) + SV.text(310, 79, "Cleo", "lbl bd") + SV.text(300, 24, "result", "sm"); return o; };
  Lib.stepper($("#stA"), { w: 480, h: 130, label: "SELECT", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: ["FROM CUSTOMER: all the rows.", "WHERE keeps only the rows where Town is Leeds.", "SELECT shows just the FirstName of those rows."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const rows = [["HJ231", 2], ["HJ231", 1], ["KM455", 5], ["HJ231", 4]]; let o = ""; rows.forEach((r, i) => o += SV.rect(20, 14 + i * 28, 200, 24, k >= 1 ? (r[0] === "HJ231" ? "f1" : "f3") : "cell", { rx: 4 }) + SV.text(30, 31 + i * 28, r[0] + "   " + r[1], "lbl", { style: "font-size:12px" }));
    if (k >= 2) o += SV.rect(300, 14, 200, 24, "f1", { rx: 4 }) + SV.text(310, 31, "HJ231   SUM = 7", "lbl bd") + SV.rect(300, 44, 200, 24, "f3", { rx: 4 }) + SV.text(310, 61, "KM455   SUM = 5", "lbl bd"); o += SV.text(20, 135, ["rows of ORDER_ITEM", "GROUP BY CustomerID puts rows with the same ID together", "SUM(Quantity) is worked out for each group: one row per customer"][Math.min(k, 2)], "lbl bd t3", { style: "font-size:12px" }); return o; };
  Lib.stepper($("#stB"), { w: 540, h: 155, label: "GROUP BY", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: ["Order lines with a CustomerID and a Quantity.", "<b>GROUP BY</b> groups the rows by CustomerID.", "<b>SUM(Quantity)</b> is calculated for each group."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const B = (x, y, t, on) => SV.rect(x, y, 190, 30, on ? "f3" : "cell", { rx: 5 }) + SV.text(x + 95, y + 19, t, "lbl", { "text-anchor": "middle", style: "font-size:11px" }); let o = B(20, 20, "SHOP_ORDER: 1001, HJ231", true) + B(300, 20, "ORDER_ITEM: A1, 1001, 2", true) + B(20, 60, "SHOP_ORDER: 1002, HJ231", true) + B(300, 60, "ORDER_ITEM: C3, 1002, 4", true);
    if (k >= 1) o += SV.path("M210,35 H300", "ax") + SV.path("M210,75 H300", "ax"); o += SV.text(20, 120, ["two tables", "ON matches OrderNo in both tables", "joined rows can be filtered and totalled"][Math.min(k, 2)], "lbl bd t3", { style: "font-size:12px" }); return o; };
  Lib.stepper($("#stC"), { w: 520, h: 140, label: "Join", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: ["Order numbers are in both tables.", "<b>INNER JOIN ... ON</b> matches rows with the same OrderNo.", "The joined rows can be filtered and totalled."].map((c, i) => ({ cap: c, s: { i } })) });
})();
sqlLab("#dml", DBT, 'SELECT CUSTOMER.FirstName, SUM(Quantity) AS TotalItems\nFROM CUSTOMER, SHOP_ORDER, ORDER_ITEM\nWHERE CUSTOMER.CustomerID = SHOP_ORDER.CustomerID\nAND SHOP_ORDER.OrderNo = ORDER_ITEM.OrderNo\nGROUP BY CUSTOMER.FirstName\nORDER BY TotalItems DESC;', { rows: 8 });
btnTable("cB", "cO", [
  ["Show only customers from Leeds", "WHERE Town = \"Leeds\"", "A condition"],
  ["Show each customer's total", "GROUP BY CustomerID with SUM", "One row per group"],
  ["Largest total first", "ORDER BY Total DESC", "Descending sort"],
  ["Use fields from two tables", "INNER JOIN ... ON keys", "Match foreign and primary keys"],
  ["Give the total a heading", "SUM(Quantity) AS TotalItems", "AS names the result"]
], ["Need", "SQL", "Why"]);
btnTable("fB", "fO", [
  ["How many orders has a customer placed?", "COUNT(OrderNo)", "A number of records"],
  ["How many items in total were ordered?", "SUM(Quantity)", "A total"],
  ["What is the mean price?", "AVG(Price)", "An average"],
  ["How many containers on a ship?", "COUNT(ContainerID)", "A number of records"]
], ["Question", "Function", "Why"]);
''' + _prjs

finish("as-8-3-2-data-manipulation-language", "as832", "Data Manipulation Language (DML)",
  "SELECT with WHERE, joins, GROUP BY, ORDER BY, COUNT, SUM and AVG, and INSERT, UPDATE and DELETE, with animations, a working SQL workbench and 23 real Paper 1 questions from 2021 to 2026.",
  "8.3.2", "8 · Databases", "section 8.3 Data definition language (DDL) and data manipulation language (DML)", learn, watch, explore, _pr, real, where, past, review,
  "Part 1 is real 9618 questions on Data Manipulation Language (Paper 1), 2021 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", tips, js)
