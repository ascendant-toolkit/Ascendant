"""AS CS 8.1.2: entity-relationship diagrams and normalisation. Run: python3 tools/artifact-kit/mk_as812.py"""
from ak8 import *

def tbl_html(name, cols, rows, key=()):
    h = f'<div class="tw" style="display:inline-block;margin:4px 10px 4px 0;vertical-align:top"><table class="t mono"><caption style="text-align:left;font-weight:700">{name}</caption><tr>' + "".join(f'<th>{"<u>" + c + "</u>" if c in key else c}</th>' for c in cols) + "</tr>"
    for r in rows: h += "<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>"
    return h + "</table></div>"

# ---- worked normalisation example
N0 = tbl_html("STUDENT (not normalised)", ["StudentName", "DateOfBirth", "TutorGroup", "Subject", "SubjectCode"], [["Yuwei Chen", "01/09/2004", "SMH", "English, Maths, Computer Science", "EN, MA, CS"], ["Claudia Raj", "23/02/2005", "JMB", "Maths, Physics, Art", "MA, PY, AR"]])
N1 = tbl_html("STUDENT", ["StudentID", "FirstName", "LastName", "DateOfBirth", "TutorGroup", "TutorName"], [["S1", "Yuwei", "Chen", "01/09/2004", "SMH", "Mr Hall"], ["S2", "Claudia", "Raj", "23/02/2005", "JMB", "Ms Brown"]], key=("StudentID",)) + tbl_html("STUDENT_SUBJECT", ["StudentID", "SubjectCode", "Subject"], [["S1", "EN", "English"], ["S1", "MA", "Maths"], ["S1", "CS", "Computer Science"], ["S2", "MA", "Maths"], ["S2", "PY", "Physics"]], key=("StudentID", "SubjectCode"))
N2 = tbl_html("STUDENT_SUBJECT", ["StudentID", "SubjectCode"], [["S1", "EN"], ["S1", "MA"], ["S2", "MA"]], key=("StudentID", "SubjectCode")) + tbl_html("SUBJECT", ["SubjectCode", "Subject"], [["EN", "English"], ["MA", "Maths"], ["CS", "Computer Science"], ["PY", "Physics"]], key=("SubjectCode",)) + tbl_html("STUDENT", ["StudentID", "FirstName", "LastName", "DateOfBirth", "TutorGroup", "TutorName"], [["S1", "Yuwei", "Chen", "01/09/2004", "SMH", "Mr Hall"], ["S2", "Claudia", "Raj", "23/02/2005", "JMB", "Ms Brown"]], key=("StudentID",))
N3 = tbl_html("STUDENT", ["StudentID", "FirstName", "LastName", "DateOfBirth", "TutorGroup"], [["S1", "Yuwei", "Chen", "01/09/2004", "SMH"], ["S2", "Claudia", "Raj", "23/02/2005", "JMB"]], key=("StudentID",)) + tbl_html("TUTOR_GROUP", ["TutorGroup", "TutorName"], [["SMH", "Mr Hall"], ["JMB", "Ms Brown"]], key=("TutorGroup",))

# ---- E-R diagrams for the past questions (relationship found from the foreign keys; each answer matches the mark scheme)
E_PLANT = er({"PLANT": (20, 10), "CUSTOMER": (290, 10), "PURCHASE_ITEM": (20, 100), "PURCHASE": (290, 100)}, [("PLANT", "PURCHASE_ITEM", "1:M"), ("PURCHASE", "PURCHASE_ITEM", "1:M"), ("CUSTOMER", "PURCHASE", "1:M")], w=470, h=150, cap="PLANTSALES")
E_FILM = er({"ACTOR": (20, 10), "FILM_FACT": (290, 10), "FILM_ACTOR": (155, 100)}, [("ACTOR", "FILM_ACTOR", "1:M"), ("FILM_FACT", "FILM_ACTOR", "1:M")], w=470, h=150, cap="FILMS")
E_PHOTO = er({"PARTY": (20, 10), "CUSTOMER": (290, 10), "PHOTO_DATA": (20, 100), "CAMERA_DATA": (290, 100)}, [("CUSTOMER", "PARTY", "1:M"), ("PARTY", "PHOTO_DATA", "1:M"), ("CAMERA_DATA", "PHOTO_DATA", "1:M")], w=470, h=150, cap="PHOTOGRAPHS")
E_SHOP = er({"SHOP_ORDER": (20, 10), "CUSTOMER": (290, 10), "ORDER_ITEM": (20, 100), "SUPPLIER": (290, 100), "ITEM": (155, 170)}, [("CUSTOMER", "SHOP_ORDER", "1:M"), ("SHOP_ORDER", "ORDER_ITEM", "1:M"), ("ITEM", "ORDER_ITEM", "1:M"), ("SUPPLIER", "ITEM", "1:M")], w=470, h=220, cap="shop")
E_FIXIT = er({"REPAIR_PART": (20, 10), "PART": (290, 10), "REPAIR": (20, 100), "CUSTOMER": (290, 100)}, [("PART", "REPAIR_PART", "1:M"), ("REPAIR", "REPAIR_PART", "1:M"), ("CUSTOMER", "REPAIR", "1:M")], w=470, h=150, cap="FIXIT")
E_FURN = er({"CUSTOMER": (20, 10), "CUSTOMER_CARD_DATA": (290, 10), "ORDER": (20, 100), "ORDER_ITEM": (290, 100)}, [("CUSTOMER", "CUSTOMER_CARD_DATA", "1:M"), ("CUSTOMER", "ORDER", "1:M"), ("ORDER", "ORDER_ITEM", "1:M")], w=470, h=150, cap="FURNITURE")
E_WORK = er({"STUDENT": (20, 10), "COMPANY": (290, 10), "PLACEMENT": (155, 100)}, [("STUDENT", "PLACEMENT", "1:M"), ("COMPANY", "PLACEMENT", "1:M")], w=470, h=150, cap="WORKEXPERIENCE")
E_REV = er({"CUSTOMER": (20, 10), "PRODUCT": (290, 10), "COMPLAINT": (155, 100), "STAFF": (290, 170)}, [("CUSTOMER", "COMPLAINT", "1:M"), ("PRODUCT", "COMPLAINT", "1:M"), ("STAFF", "COMPLAINT", "1:M")], w=470, h=220, cap="REVIEWS")
E_GAME = er({"PLAYER": (20, 10), "CHARACTER": (290, 10), "GROUP": (290, 100)}, [("PLAYER", "CHARACTER", "1:M"), ("CHARACTER", "GROUP", "M:M")], w=470, h=150, cap="game")
E_DEMO = er({"CUSTOMER": (20, 10), "SHOP_ORDER": (20, 90), "ORDER_ITEM": (155, 170), "ITEM": (290, 90)}, [("CUSTOMER", "SHOP_ORDER", "1:M"), ("SHOP_ORDER", "ORDER_ITEM", "1:M"), ("ITEM", "ORDER_ITEM", "1:M")], w=470, h=215, cap="demo")

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>An <b>entity-relationship (E-R) diagram</b> shows each table (entity) as a box and each relationship as a line, with a bar at the <b>one</b> end and a crow's foot at the <b>many</b> end. To draw one from a list of tables, find each <b>foreign key</b>: the table that holds it is on the <b>many</b> side and the table where it is the primary key is on the <b>one</b> side; a table that holds two foreign keys is usually a <b>linking table</b>. <b>Normalisation</b> organises data to reduce redundancy: <b>1NF</b> has no repeating groups and every field is atomic; <b>2NF</b> is in 1NF and has no partial dependencies (every non-key field depends on the whole of the composite key); <b>3NF</b> is in 2NF and has no non-key (transitive) dependencies (every non-key field depends on the primary key and nothing else). Exam questions ask you to complete an E-R diagram, describe the normal forms, say what normal form a database is in, and normalise a given table.</p></div>

  <h2>1 · E-R diagrams</h2>
  <p>The tables PLANT, CUSTOMER, PURCHASE and PURCHASE_ITEM give this diagram. PURCHASE_ITEM(PurchaseID, PlantName, Quantity) holds the foreign key PurchaseID (to PURCHASE) and PlantName (to PLANT): a linking table, so each of those relationships is one-to-many from the other table to PURCHASE_ITEM.</p>
  ''' + er_html({"PLANT": (20, 10), "CUSTOMER": (290, 10), "PURCHASE_ITEM": (20, 100), "PURCHASE": (290, 100)}, [("PLANT", "PURCHASE_ITEM", "1:M"), ("PURCHASE", "PURCHASE_ITEM", "1:M"), ("CUSTOMER", "PURCHASE", "1:M")], w=470, h=150, cap="E-R diagram") + '''
  <ol>
    <li>List every table and its foreign keys.</li>
    <li>For each foreign key, draw a line to the table where it is the primary key: that table is the "one" side, the table holding the foreign key is the "many" side.</li>
    <li>A many-to-many relationship (a linking table holding the keys of two tables) appears as two one-to-many lines meeting at the linking table.</li>
    <li>Draw no extra lines: the mark scheme takes marks off for extra relationships.</li>
  </ol>

  <h2>2 · Normal forms</h2>
  <div class="tw"><table class="t">
    <tr><th>Normal form</th><th>Rule</th><th>Fixing a table</th></tr>
    <tr><td><b>1NF</b></td><td>No repeating groups or repeating attributes; every field holds one value (atomic); a primary key is identified</td><td>Split repeated fields into their own table, with the key of the first table as a foreign key; split a field such as a full name into FirstName and LastName</td></tr>
    <tr><td><b>2NF</b></td><td>In 1NF and no <b>partial dependencies</b>: every non-key attribute depends on the whole of the (composite) primary key</td><td>Move attributes that depend on only part of the key into a new table</td></tr>
    <tr><td><b>3NF</b></td><td>In 2NF and no <b>non-key (transitive) dependencies</b>: every attribute depends on the primary key and no other attribute</td><td>Move attributes that depend on another non-key attribute into a new table</td></tr>
  </table></div>
  <p>A database in 3NF has <b>no repeating groups</b> (data is atomic), <b>no partial key dependencies</b> and <b>no non-key dependencies</b>; it also has no many-to-many relationships (they are broken up with linking tables).</p>

  <h2>3 · A worked example</h2>
  <p><b>Not normalised:</b> repeating groups of Subject and SubjectCode, and a name that holds two items.</p>
  ''' + N0 + '''
  <p><b>1NF:</b> identify a primary key, make each field atomic (split the name) and remove the repeating group into its own table linked by StudentID. (Suppose each tutor group also has a tutor name.)</p>
  ''' + N1 + '''
  <p><b>2NF:</b> Subject depends only on SubjectCode, which is part of the composite key of STUDENT_SUBJECT: a partial dependency. Move it into SUBJECT.</p>
  ''' + N2 + '''
  <p><b>3NF:</b> TutorName depends on TutorGroup, not on StudentID: a non-key dependency. Move it into TUTOR_GROUP.</p>
  ''' + N3 + '''

  <h2>Common ways to lose marks</h2>
  <ul>
    <li>Drawing an E-R relationship the wrong way round: the crow's foot (many) end is at the table holding the foreign key.</li>
    <li>Adding extra lines to an E-R diagram, or leaving a linking table disconnected from one of its tables.</li>
    <li>Describing 2NF without saying "partial dependency" and what it depends on (part of a composite key).</li>
    <li>Giving only the name of the normal form when the question asks for the justification.</li>
    <li>Normalising without a primary key in each new table, or without the foreign keys that link them.</li>
  </ul>
'''

watch = '''
  <h2>1 · Drawing an E-R diagram from foreign keys</h2>
  <div id="stA"></div>
  <h2>2 · From 0NF to 1NF</h2>
  <div id="stB"></div>
  <h2>3 · 2NF and 3NF</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Normal form of this table</h2>
  <p>Pick a problem the table has and see which normal form it breaks.</p>
  <div class="card"><div id="nB" class="btnrow"></div><div id="nO"></div></div>
  <h2>Lab 2 · Foreign key to relationship</h2>
  <div class="card"><div id="fB" class="btnrow"></div><div id="fO"></div></div>
  <h2>Lab 3 · The shop database</h2>
  <div class="card"><div id="eG"></div></div>
'''

_pr, _prjs = PR(["Which normal form is broken?", "Many side or one side?", "Match the term to its meaning", "Put the normalisation steps in order", "Working out", "Multiple choice"],
  ("Which normal form does this problem break?", ["1NF", "2NF", "3NF"], [("A field holds a list of subjects", 0), ("An attribute depends on only part of a composite key", 1), ("An attribute depends on another non-key attribute", 2), ("The same group of fields repeats on every row", 0), ("Partial dependency", 1), ("Transitive (non-key) dependency", 2)], "1NF: repeats. 2NF: part of the key. 3NF: non-key."),
  ("In an E-R diagram, is the table on the one side or the many side?", ["One side", "Many side"], [("CUSTOMER, where CustomerID is the primary key", 0), ("SHOP_ORDER, which holds the foreign key CustomerID", 1), ("SHIP, where ShipID is the primary key", 0), ("CONTAINER, which holds the foreign key ShipID", 1), ("PLANT in PLANT to PURCHASE_ITEM", 0), ("PURCHASE_ITEM in PURCHASE to PURCHASE_ITEM", 1)], "The foreign key table is the many side."),
  [["1NF", "No repeating groups; fields are atomic"], ["2NF", "No partial dependencies on a composite key"], ["3NF", "No non-key (transitive) dependencies"], ["Linking table", "Breaks up a many-to-many relationship"], ["Atomic", "A field holds one value only"]],
  ("Put the normalisation steps in order.", ["Identify the primary key and make every field atomic", "Move repeating groups into their own table", "Remove partial dependencies (2NF)", "Remove non-key dependencies (3NF)", "Check every table has a primary key and foreign keys link them"], "1NF, repeats, 2NF, 3NF, keys."),
  [{"q": "How many tables are there in the 3NF example in the Learn tab (STUDENT, STUDENT_SUBJECT, SUBJECT, TUTOR_GROUP)?", "a": 4, "unit": "", "tol": 0.01, "hint": "Count them.", "sol": "<b>4</b>."}, {"q": "A linking table joins two tables. How many one-to-many relationships does it make?", "a": 2, "unit": "", "tol": 0.01, "hint": "One to each.", "sol": "<b>2</b>."}, {"q": "In PLANTSALES there are 4 tables and 3 relationships. How many foreign keys are needed (one per relationship)?", "a": 3, "unit": "", "tol": 0.01, "hint": "One per line.", "sol": "<b>3</b>."}, {"q": "A table has a composite key (A, B) and attribute C depends only on A. Which normal form does it break? Answer 2 for 2NF.", "a": 2, "unit": "", "tol": 0.01, "hint": "Partial dependency.", "sol": "<b>2</b> (2NF)."}, {"q": "A student with 3 subjects is stored in 1 row with 3 subject columns (repeating group). In 1NF the subjects are moved to a table with one row per subject: how many rows for 3 subjects?", "a": 3, "unit": "", "tol": 0.01, "hint": "One per subject.", "sol": "<b>3</b>."}],
  [("The crow's foot is drawn at:", ["The many end", "The one end", "Neither", "Both"], 0, "Many end."), ("3NF removes:", ["Non-key dependencies", "Primary keys", "Foreign keys", "All tables"], 0, "Non-key dependencies."), ("A repeating group breaks:", ["1NF", "2NF", "3NF", "None"], 0, "1NF."), ("2NF needs no:", ["Partial dependencies", "Primary keys", "Records", "Tables"], 0, "Partial."), ("A many-to-many relationship is broken up with:", ["A linking table", "A larger field", "An index", "A view"], 0, "Linking table."), ("An atomic field:", ["Holds one value", "Is a key", "Is empty", "Is a table"], 0, "One value.")],
  [("E-R diagram", "Boxes for tables; lines for relationships."), ("Crow's foot", "The many end of a relationship."), ("1NF", "No repeating groups; atomic."), ("2NF", "No partial dependencies."), ("3NF", "No non-key dependencies."), ("Linking table", "Two foreign keys; two 1:M."), ("Partial dependency", "Depends on part of a composite key."), ("Transitive dependency", "Depends on a non-key attribute.")])

real = RWNOTE + (
rw("A school's form list", "A student's subjects are in one cell. Splitting them into their own table, one row per subject, is first normal form.", "1NF.") +
rw("A subject name repeated in every enrolment", "If every row of an enrolment table repeats 'Computer Science' with its code, the name depends only on the code: move it to a SUBJECT table.", "2NF.") +
rw("A tutor's name stored with every student", "The name depends on the tutor group, not on the student; move it to a TUTOR_GROUP table so a name change is made once.", "3NF.") +
rw("A diagram before building", "Database designers sketch an E-R diagram so everyone agrees how tables relate before a line of SQL is written.", "E-R diagram.") +
rw("A cinema booking database", "Many shows, many customers and many seats: linking tables turn those many-to-many relationships into one-to-many ones.", "linking tables.")
)

where = [
  ("M/J 2021", "12", "1(b)", "2", "Is HOUSE_RENTALS in 3NF? Justify with examples"),
  ("O/N 2021", "12", "6(a)", "2 + 3", "Normalisation stage for three tasks; draw the E-R diagram for PLANTSALES"),
  ("M/J 2022", "11", "4(b)", "3", "The highest normal form of the database MARKS, with justification"),
  ("M/J 2022", "12", "5(a)", "2", "Complete the E-R diagram for FILMS"),
  ("O/N 2022", "11", "4(a), (b)", "3 + 3", "Complete the E-R diagram; the characteristics of 3NF"),
  ("O/N 2022", "12", "5(a)", "3", "How the GARDEN database can be normalised to 3NF"),
  ("M/J 2022", "13", "6(c)", "3", "Describe 1NF, 2NF and 3NF"),
  ("M/J 2023", "11", "2(b)(ii)", "1", "Match the normal forms to their definitions"),
  ("M/J 2023", "13", "4(c)", "4", "Write a normalised 3NF design for the car rental database"),
  ("O/N 2023", "11", "3(a)", "3", "Complete the E-R diagram for the shop database"),
  ("O/N 2023", "12", "2(c)", "4", "Explain how to put a table into 1NF"),
  ("M/J 2024", "12", "4(a), (d)", "1 + 5", "The relationship between two tables; additional tables and how they link"),
  ("M/J 2024", "13", "4(a), (d)", "1 + 5", "The relationship between PERFORMANCE and SHOW; additional tables for customers and seats"),
  ("O/N 2024", "11", "2(b)(i)", "3", "Complete the E-R diagram for FIXIT"),
  ("O/N 2024", "12", "6(b)(i)", "6", "Identify each relationship and how it is implemented"),
  ("M/J 2025", "11", "5(a), (d)", "3 + 3", "Complete the E-R diagram; why ORDER_ITEM cannot be stored in ORDER"),
  ("O/N 2025", "11", "2(a), (b)", "2 + 2", "Complete the E-R diagram for WORKEXPERIENCE; why it is in 3NF"),
  ("O/N 2025", "13", "5(a)", "3", "Complete the E-R diagram for REVIEWS"),
  ("M/J 2026", "11", "4(a)", "4", "Describe the relationship between CUSTOMER and BORROW, and TOY_INSTANCE and TOY"),
  ("M/J 2026", "12", "3(a)", "2", "Describe the relationships between player, character and group"),
  ("M/J 2026", "13", "4(a)", "6", "A 3-table 3NF design for the school library")]

def erq(src, marks, q, tip, ans, diag, warn=None):
    return peq(src, marks, "Complete", q, tip, "<p>" + ans + "</p>" + diag, warn)

past = '''  <p class="note">E-R diagrams are asked in Paper 1 almost every series and the marks are one per correct relationship; extra lines lose marks. The diagrams below follow the mark schemes. Questions are reworded from the papers; check the original paper and mark scheme for the exact wording.</p>
''' + peq(SRC("s21", "12", "Q1(b)"), "2 marks", "Tick / Justify",
  "HOUSE_RENTALS has CUSTOMER(CustomerID, FirstName, LastName, DateOfBirth, Email), HOUSE(HouseID, HouseNumber, Road, Town, Bedrooms, Bathrooms) and RENTAL(RentalID, CustomerID, HouseID, MonthlyCost, DepositPaid). Tick whether it is in 3NF or not, and justify using examples from the database.", "Each field depends on the key only.",
  "<p>In 3NF. " + mks(["All fields in all tables are fully dependent on the primary key and on no other fields", "For example all fields in CUSTOMER are fully dependent on CustomerID"]) + "</p>", None) + peq(SRC("w21", "12", "Q6(a)"), "2 + 3 marks", "Tick / Draw",
  "PLANTSALES has PLANT(PlantName, QuantityInStock, Cost), CUSTOMER(CustomerID, FirstName, LastName, Address, Email), PURCHASE(PurchaseID, CustomerID) and PURCHASE_ITEM(PurchaseID, PlantName, Quantity). (i) Tick the stage for each task: remove partial key dependencies; remove repeating groups; remove non-key dependencies. (ii) Draw an E-R diagram for the database.", "Repeating groups: 0NF to 1NF. Partial: 1NF to 2NF. Non-key: 2NF to 3NF.",
  "<p><b>(i)</b> " + mks(["Remove partial key dependencies: 1NF to 2NF", "Remove repeating groups: 0NF to 1NF", "Remove non-key dependencies: 2NF to 3NF"]) + " (1 tick correct: 1 mark; all 3: 2 marks)</p><p><b>(ii)</b> " + mks(["PLANT to PURCHASE_ITEM: one-to-many", "PURCHASE to PURCHASE_ITEM: one-to-many", "CUSTOMER to PURCHASE: one-to-many"]) + "</p>" + E_PLANT, "Drawing PLANT to CUSTOMER directly. They are only linked through the purchase tables.") + peq(SRC("s22", "11", "Q4(b)"), "3 marks", "Give / Justify",
  "MARKS has STUDENT(StudentID, FirstName, LastName), TEST(TestID, Description, TotalMarks) and STUDENT_TEST(StudentID, TestID, Mark). Give the highest level of Normal Form the database is in and justify your choice.", "3NF: no repeated attributes, no partial or transitive dependencies.",
  "<p>" + mks(["3NF"]) + " Justification, any two: " + mks(["There are no repeated attributes (it is already in 2NF)", "Each field is fully dependent on its primary key; no partial dependencies", "There are no transitive dependencies"], "a") + "</p>", None) + erq(SRC("s22", "12", "Q5(a)"), "2 marks",
  "FILMS has ACTOR(ActorID, FirstName, LastName, DateOfBirth), FILM_FACT(FilmID, FilmTitle, ReleaseDate, Category) and FILM_ACTOR(ActorID, FilmID). Complete the E-R diagram.", "FILM_ACTOR is a linking table.",
  mks(["ACTOR to FILM_ACTOR: one-to-many", "FILM_FACT to FILM_ACTOR: one-to-many"]), E_FILM) + erq(SRC("w22", "11", "Q4(a)(b)"), "3 + 3 marks",
  "PHOTOGRAPHS has CUSTOMER(CustomerID, FirstName, LastName, Telephone), PARTY(PartyID, CustomerID, PartyDate, StartTime), PHOTO_DATA(PhotoID, PartyID, TimeTaken, CameraID) and CAMERA_DATA(CameraID, LensType, LightingType). (a) Complete the E-R diagram. (b) Describe the characteristics of a database in 3NF.", "Follow the foreign keys. No repeating groups, no partial, no non-key dependencies.",
  mks(["CUSTOMER to PARTY: 1:M", "PARTY to PHOTO_DATA: 1:M", "CAMERA_DATA to PHOTO_DATA: 1:M"]) + " (b) Any three: " + mks(["No repeating groups of attributes (the data is atomic)", "No partial key dependencies", "No non-key (transitive) dependencies"], "a"), E_PHOTO) + peq(SRC("w22", "12", "Q5(a)"), "3 marks", "Explain",
  "GARDEN has OWNER(OwnerID, FirstName, TelephoneNo, TreeID, TreePosition) and TREE(TreeID, ScientificName, MaxHeight, FastGrowing). The database is not in 3NF. Explain how it can be normalised to 3NF.", "Owner and tree is many-to-many: a linking table.",
  "<p>Any three: " + mks(["Remove the many-to-many relationship between OWNER and TREE", "by removing TreeID and TreePosition from the OWNER table", "and creating a linking table between OWNER and TREE", "containing OwnerID, TreeID and TreePosition", "with a (composite) primary key of OwnerID and TreeID, or a new named primary key"]) + "</p>", None) + peq(SRC("s22", "13", "Q6(c)"), "3 marks", "Describe",
  "The database TECHNOLOGY is in 3NF. Complete the table by describing the three normal forms.", "1NF repeats; 2NF partial; 3NF non-key.",
  "<p>" + mks(["1NF: no repeating groups or repeating attributes", "2NF: all attributes are fully dependent on the (composite) primary key; no partial dependencies", "3NF: all attributes are fully dependent on the primary key and no other attributes; no non-key or transitive dependencies"]) + "</p>", None) + peq(SRC("s23", "11", "Q2(b)(ii)"), "1 mark", "Match",
  "Draw one line from each Normal Form to the most appropriate definition. Normal forms: 1NF, 2NF, 3NF. Definitions: all fields are fully dependent on the primary key; there are no repeating groups of attributes; there are no partial dependencies. (The paper's wording is shuffled, so match by meaning.)", "Repeating groups: 1NF. Partial: 2NF. Dependent on the key: 3NF.",
  "<p>" + mks(["1NF: there are no repeating groups of attributes", "2NF: there are no partial dependencies", "3NF: all fields are fully dependent on the primary key (and on no other field)"]) + " (all three correct for the mark)</p>", None) + peq(SRC("s23", "13", "Q4(c)"), "4 marks", "Write",
  "The car rental database is not normalised: BOOKING(CarRegistration, StartDate, EndDate, CarModel, CarColour, CustomerFirstName) and CUSTOMER(CustomerFirstName, CustomerLastName, EmailAddress, TelephoneNumber). Write a normalised 3NF database design using the field names given and underline the primary key fields.", "Three tables: booking, car, customer.",
  "<p>One answer: BOOKING(<u>BookingID</u>, CarRegistration, CustomerID, StartDate, EndDate); CAR(<u>CarRegistration</u>, CarModel, CarColour); CUSTOMER(<u>CustomerID</u>, CustomerFirstName, CustomerLastName, EmailAddress, TelephoneNumber).</p><p>" + mks(["Only three tables with appropriate identifiers (customer, booking, car)", "An appropriate primary key underlined in each table", "BOOKING includes the primary keys of CAR and CUSTOMER as foreign keys", "All original fields are in the correct tables"]) + "</p>", "Using CustomerFirstName as the customer key. Names are not unique; use a CustomerID.") + erq(SRC("w23", "11", "Q3(a)"), "3 marks",
  "The shop database has CUSTOMER(CustomerID, FirstName, LastName, Town), SHOP_ORDER(OrderNo, CustomerID, OrderDate), SUPPLIER(SupplierID, EmailAddress, TelephoneNumber), ITEM(ItemNumber, SupplierID, Description, Price) and ORDER_ITEM(ItemNumber, OrderNo, Quantity). Complete the E-R diagram.", "ORDER_ITEM links SHOP_ORDER and ITEM.",
  mks(["CUSTOMER to SHOP_ORDER: 1:M", "SUPPLIER to ITEM: 1:M", "SHOP_ORDER to ORDER_ITEM: 1:M and ITEM to ORDER_ITEM: 1:M"]), E_SHOP) + peq(SRC("w23", "12", "Q2(c)"), "4 marks", "Explain",
  "Explain how to modify the table STUDENT(StudentName, DateOfBirth, TutorGroup, Subject, SubjectCode), where Subject and SubjectCode hold several values in one cell, to put it into First Normal Form.", "Repeating groups; atomic; a key.",
  "<p>Any four: " + mks(["Identify the repeating groups of attributes", "Subject and SubjectCode", "Ensure each field is atomic", "StudentName should be split into, for example, FirstName and LastName", "Identify the primary key for the table"]) + "</p>" + N0 + N1, None) + peq(SRC("s24", "12", "Q4(a)(d)"), "1 + 5 marks", "Identify / Describe",
  "EXAM(ExamID, Subject, Level, TotalMarks) and EXAM_QUESTION(ExamQuestionID, ExamID, QuestionNumber, Question, MaxMark). (a) Identify the relationship between EXAM and EXAM_QUESTION. (d) The database also needs to store the students, the exams they take and the marks for each question. Describe the additional tables and explain how all the tables are linked.", "One to many. STUDENT, a linking table to EXAM, a linking table to EXAM_QUESTION.",
  "<p><b>(a)</b> " + mks(["One-to-many"]) + "</p><p><b>(d)</b> Any five: " + mks(["A STUDENT table with a suitable primary key", "A linking table between STUDENT and EXAM with a suitable primary key and name", "that includes the primary key of STUDENT as a foreign key", "and the primary key of EXAM as a foreign key", "A linking table between STUDENT and EXAM_QUESTION", "that includes the key of the previous linking table as a foreign key", "that stores the ExamQuestionID and the mark for that question"], "a") + "</p>", None) + peq(SRC("s24", "13", "Q4(a)(d)"), "1 + 5 marks", "Identify / Describe",
  "The theatre database has SHOW(ShowID, Title, Duration), SEAT(SeatID, RowLetter, SeatNumber) and PERFORMANCE(PerformanceID, ShowID, ShowDate, StartTime). (a) Identify the relationship between PERFORMANCE and SHOW. (d) Customers give a first name, last name and email address when booking, and one booking can include multiple seats. Describe the additional tables and how they are linked.", "Many to one. CUSTOMER, BOOKING, and a linking table to SEAT.",
  "<p><b>(a)</b> " + mks(["Many to one (many performances of each show)"]) + "</p><p><b>(d)</b> Any five: " + mks(["A CUSTOMER table with a suitable primary key and fields including name and email", "A BOOKING table with a suitable primary key", "that stores the primary key of CUSTOMER as a foreign key", "and the primary key of PERFORMANCE as a foreign key", "A linking table between BOOKING and SEAT with a suitable primary key", "that includes the primary key of BOOKING as a foreign key", "that stores the SeatID"], "a") + "</p>", None) + erq(SRC("w24", "11", "Q2(b)(i)"), "3 marks",
  "FIXIT has PART(PartID, Description, Price, SupplierID), CUSTOMER(CustomerID, FirstName, LastName, ContactNumber), REPAIR(RepairNumber, StartDate, EndDate, CustomerID, Device) and REPAIR_PART(PartID, RepairNumber, Quantity). Complete the E-R diagram.", "REPAIR_PART is the linking table.",
  mks(["PART to REPAIR_PART: 1:M", "REPAIR to REPAIR_PART: 1:M", "CUSTOMER to REPAIR: 1:M"]), E_FIXIT) + peq(SRC("w24", "12", "Q6(b)(i)"), "6 marks", "Identify / Explain",
  "The database includes CUSTOMER, EMPLOYEE, LOGIN_DATA (username and password for each employee), JOB and JOB_EMPLOYEE (the employees working on each job). Identify each relationship between the tables and explain how each is implemented in the normalised database.", "Customer to job 1:M; employee to login 1:1; job and employee to JOB_EMPLOYEE 1:M.",
  "<p>" + mks(["CUSTOMER to JOB is one-to-many, implemented by the primary key in CUSTOMER being a foreign key in JOB", "EMPLOYEE to LOGIN_DATA is one-to-one, implemented by the primary key in EMPLOYEE being a foreign key in LOGIN_DATA", "JOB to JOB_EMPLOYEE is one-to-many, implemented by the primary key in JOB being a foreign key in JOB_EMPLOYEE", "EMPLOYEE to JOB_EMPLOYEE is one-to-many, implemented by the primary key in EMPLOYEE being a foreign key in JOB_EMPLOYEE"]) + " (relationship and implementation for each; max 6)</p>", None) + erq(SRC("s25", "11", "Q5(a)"), "3 marks",
  "FURNITURE has CUSTOMER, CUSTOMER_CARD_DATA(CardID, CustomerID, ...), ORDER(OrderID, CustomerID, ...) and ORDER_ITEM(OrderItemID, OrderID, ...). Complete the E-R diagram.", "Three one-to-many relationships; no extra lines.",
  mks(["CUSTOMER to CUSTOMER_CARD_DATA: 1:M", "CUSTOMER to ORDER: 1:M", "ORDER to ORDER_ITEM: 1:M"]) + " (max 2 if there are extra relationships)", E_FURN) + peq(SRC("s25", "11", "Q5(d)"), "3 marks", "Explain",
  "Explain the reasons why the data in the table ORDER_ITEM cannot be stored in the table ORDER.", "Each order has several items.",
  "<p>Any three: " + mks(["Each order would only be able to have one item", "or the database would not be normalised", "it would not be in 1NF", "due to repeated groups of attributes in the ORDER table"]) + "</p>", None) + erq(SRC("w25", "11", "Q2(a)(b)"), "2 + 2 marks",
  "WORKEXPERIENCE has STUDENT, PLACEMENT(PlacementID, StudentID, CompanyID, ...) and COMPANY. (a) Complete the E-R diagram. (b) Explain why the database is in 3NF.", "PLACEMENT holds both foreign keys.",
  mks(["STUDENT to PLACEMENT: 1:M", "COMPANY to PLACEMENT: 1:M"]) + " (b) Any two: " + mks(["There are no repeating groups of attributes", "There are no many-to-many relationships", "There are no partial key dependencies, no non-key dependencies and no transitive dependencies"], "a"), E_WORK) + erq(SRC("w25", "13", "Q5(a)"), "3 marks",
  "REVIEWS has CUSTOMER, PRODUCT, COMPLAINT(ComplaintID, ProductID, CustomerID, ComplaintDetails, StaffID) and STAFF. Complete the E-R diagram.", "COMPLAINT holds three foreign keys.",
  mks(["CUSTOMER to COMPLAINT: 1:M", "PRODUCT to COMPLAINT: 1:M", "STAFF to COMPLAINT: 1:M"]), E_REV) + peq(SRC("s26", "11", "Q4(a)"), "4 marks", "Describe",
  "The toy shop database has CUSTOMER(CustomerID, ContactFirstName, Phone), TOY(ToyID, ToyName, CostPerDay), TOY_INSTANCE(UniqueToyID, ToyID, Quality) and BORROW(BorrowID, CustomerID, UniqueToyID, StartDate, NumberDays). Describe the relationship between CUSTOMER and BORROW, and between TOY_INSTANCE and TOY, including the primary and foreign keys.", "1:M and M:1; name the keys and how they link.",
  "<p>" + mks(["CUSTOMER to BORROW is one-to-many", "TOY_INSTANCE to TOY is many-to-one", "The correct primary key and matching foreign key in both relationships (CustomerID in CUSTOMER and BORROW; ToyID in TOY and TOY_INSTANCE)", "The primary key in the one table is the foreign key in the many table, which creates the relationship"]) + "</p>", None) + peq(SRC("s26", "12", "Q3(a)"), "2 marks", "Describe",
  "A game database has three entities: players, the characters that players create, and the groups that players create and allow characters to join. Describe the relationships between the three entities.", "A player has many characters; groups and characters are many-to-many.",
  "<p>" + mks(["PLAYER to CHARACTER is one-to-many: one player can have many characters but each character is created by one player", "GROUP and CHARACTER is many-to-many: one group can have many characters and one character can be in many groups"]) + "</p>" + E_GAME, None) + peq(SRC("s26", "13", "Q4(a)"), "6 marks", "Create",
  "A school library stores data about books (author, title, category, number of pages), students (name and class) and the books they borrow for 14 days. The database must store whether a book is late. Create a 3-table design normalised to 3NF in the format TableName(Field1, Field2, ...), with primary keys underlined and foreign keys marked.", "Book, Student, Borrow with two foreign keys.",
  "<p>One answer: BOOK(<u>BookID</u>, Author, Title, Category, Pages); STUDENT(<u>StudentID</u>, FirstName, LastName, Class); BORROW(<u>BorrowID</u>, StudentID, BookID, DateBorrowed, Late).</p><p>" + mks(["Three tables with suitable names", "Each has a suitable primary key", "Book has the author, title, category and number of pages", "Student has the first name, last name and class", "Borrow has the book and student keys, the date borrowed and a field to show late", "The foreign keys in BORROW are clearly identified"]) + "</p>", None)

review = req("3 marks", "Draw", "A library has MEMBER(MemberID, Name), BOOK(BookID, Title) and LOAN(LoanID, MemberID, BookID, DueDate). Describe the relationships (by name and type) for an E-R diagram.", "LOAN holds two foreign keys.", "<p>" + mks(["MEMBER to LOAN: one-to-many", "BOOK to LOAN: one-to-many", "Therefore LOAN is a linking table between MEMBER and BOOK (many-to-many)"]) + "</p>" + er_html({"MEMBER": (20, 10), "BOOK": (290, 10), "LOAN": (155, 90)}, [("MEMBER", "LOAN", "1:M"), ("BOOK", "LOAN", "1:M")], w=470, h=140), None) + req("2 marks", "Explain", "A table ORDER(OrderID, Item1, Item2, Item3) holds up to three items per order. Explain how to put it into 1NF.", "Repeating group.", "<p>" + mks(["The repeating group Item1, Item2, Item3 is removed", "A new ORDER_ITEM table has one row per item with OrderID as a foreign key"]) + "</p>", None) + req("2 marks", "Explain", "In ENROL(StudentID, CourseID, CourseName), explain why the table is not in 2NF.", "Partial dependency.", "<p>" + mks(["The key is (StudentID, CourseID)", "CourseName depends only on CourseID, which is part of the key (a partial dependency)"]) + "</p>", None) + req("2 marks", "Explain", "In STAFF(StaffID, DepartmentID, DepartmentName), explain why the table is not in 3NF.", "Transitive dependency.", "<p>" + mks(["DepartmentName depends on DepartmentID, which is not the primary key (a non-key dependency)", "so DepartmentName should be moved to a DEPARTMENT table"]) + "</p>", None) + req("2 marks", "State", "State two characteristics of a database in 3NF.", "No repeating groups, no dependencies.", "<p>" + mks(["No repeating groups; the data is atomic", "No partial key dependencies and no non-key dependencies"]) + "</p>", None)

tips = tips_html([
  ("Crow's foot at the foreign key end.", "The 'many' side holds the foreign key."),
  ("No extra lines.", "Only draw the relationships in the table list."),
  ("1NF: repeats and atomic.", "2NF: partial. 3NF: non-key."),
  ("Name the dependency.", "Partial: part of the composite key."),
  ("A linking table has two foreign keys.", "Two one-to-many lines."),
  ("Give each new table a primary key.", "And mark the foreign keys."),
], [("an E-R diagram", "A diagram of the tables and their relationships."), ("normalisation", "Organising data into tables to remove redundancy."), ("a partial dependency", "An attribute that depends on only part of a composite key."), ("a transitive dependency", "An attribute that depends on a non-key attribute.")],
  [("Complete", "Draw the relationships."), ("Describe", "State the rules."), ("Explain", "Reasons as well."), ("Write", "Give the design.")]) + FC

js = AKJS + AK20JS + r'''
(function () {
  const draw = (s) => { const k = Math.round(s.i); const B = (x, y, t, on) => SV.rect(x, y, 130, 30, on ? "f3" : "cell", { rx: 5 }) + SV.text(x + 65, y + 19, t, "lbl bd", { "text-anchor": "middle", style: "font-size:11px" }); let o = B(20, 20, "CUSTOMER", true) + B(280, 20, "PURCHASE", true) + B(280, 110, "PURCHASE_ITEM", true) + B(20, 110, "PLANT", true);
    if (k >= 1) o += SV.path("M150,35 H280", "ax") + SV.text(215, 28, "1 ——< M", "sm", { "text-anchor": "middle" }); if (k >= 2) o += SV.path("M345,50 V110", "ax") + SV.text(380, 85, "1 —< M", "sm"); if (k >= 3) o += SV.path("M150,125 H280", "ax") + SV.text(215, 118, "1 ——< M", "sm", { "text-anchor": "middle" });
    o += SV.text(20, 175, ["", "CustomerID: PK in CUSTOMER, FK in PURCHASE", "PurchaseID: PK in PURCHASE, FK in PURCHASE_ITEM", "PlantName: PK in PLANT, FK in PURCHASE_ITEM"][k], "lbl bd t3", { style: "font-size:12px" }); return o; };
  Lib.stepper($("#stA"), { w: 440, h: 190, label: "E-R", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: ["Four tables, no relationships drawn yet.", "CustomerID is a foreign key in PURCHASE: <b>CUSTOMER 1:M PURCHASE</b>.", "PurchaseID is a foreign key in PURCHASE_ITEM: <b>PURCHASE 1:M PURCHASE_ITEM</b>.", "PlantName is a foreign key in PURCHASE_ITEM: <b>PLANT 1:M PURCHASE_ITEM</b>."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.text(20, 20, k === 0 ? "StudentName   Subject (list)   SubjectCode (list)" : "StudentID  FirstName  LastName  |  StudentID  SubjectCode", "lbl bd", { style: "font-size:13px" });
    const rows = k === 0 ? ["Yuwei Chen   English, Maths, CS   EN, MA, CS", "Claudia Raj   Maths, Physics, Art   MA, PY, AR"] : ["S1  Yuwei  Chen   |   S1  EN", "S1  Yuwei  Chen   |   S1  MA", "S2  Claudia  Raj   |   S2  MA"]; rows.forEach((r, i) => o += SV.rect(20, 32 + i * 28, 480, 24, k === 0 ? "f2" : "f1", { rx: 4 }) + SV.text(30, 49 + i * 28, r, "lbl", { style: "font-size:12px" })); o += SV.text(20, 135, k === 0 ? "repeating groups and a name that holds two items" : "atomic fields; repeating group moved to its own table: 1NF", "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stB"), { w: 540, h: 150, label: "1NF", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: ["The table has <b>repeating groups</b> (lists of subjects) and a name that is not atomic.", "<b>1NF</b>: split the name, give a key and move the subjects into a table with one row each."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = ""; const T = (x, y, n, rows, on) => { let r = SV.rect(x, y, 230, 22 + rows.length * 20, on ? "f1" : "cell", { rx: 5 }) + SV.text(x + 8, y + 15, n, "lbl bd", { style: "font-size:12px" }); rows.forEach((t, i) => r += SV.text(x + 8, y + 35 + i * 20, t, "lbl", { style: "font-size:11px" })); return r; };
    if (k === 0) o += T(20, 20, "STUDENT_SUBJECT", ["StudentID, SubjectCode, Subject", "(Subject depends on SubjectCode only)"], true); if (k === 1) o += T(20, 20, "STUDENT_SUBJECT", ["StudentID, SubjectCode"], true) + T(280, 20, "SUBJECT", ["SubjectCode, Subject"], true); if (k >= 2) o += T(20, 20, "STUDENT", ["StudentID, ..., TutorGroup"], true) + T(280, 20, "TUTOR_GROUP", ["TutorGroup, TutorName"], true);
    o += SV.text(20, 120, ["partial dependency: Subject depends on part of the key", "2NF: Subject moved into its own table", "3NF: TutorName depends on TutorGroup, so it moves to its own table"][k], "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stC"), { w: 540, h: 140, label: "2NF and 3NF", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: ["Subject depends only on SubjectCode, part of the composite key: a <b>partial dependency</b>.", "<b>2NF</b>: move it to a SUBJECT table.", "<b>3NF</b>: TutorName depends on TutorGroup, a <b>non-key dependency</b>: move it to its own table."].map((c, i) => ({ cap: c, s: { i } })) });
})();

btnTable("nB", "nO", [
  ["A cell holds 'English, Maths, Physics'", "1NF broken", "A repeating group; data is not atomic"],
  ["Subject name depends only on SubjectCode in a table keyed (StudentID, SubjectCode)", "2NF broken", "A partial dependency"],
  ["TutorName depends on TutorGroup, which is not the key", "3NF broken", "A non-key (transitive) dependency"],
  ["Every field depends on the primary key and nothing else", "In 3NF", "All three rules satisfied"]
], ["Problem", "Result", "Why"]);
btnTable("fB", "fO", [
  ["CustomerID in SHOP_ORDER (PK in CUSTOMER)", "CUSTOMER 1:M SHOP_ORDER", "FK table is the many side"],
  ["ShipID in CONTAINER (PK in SHIP)", "SHIP 1:M CONTAINER", "One ship, many containers"],
  ["OrderNo and ItemNumber in ORDER_ITEM", "Linking table: SHOP_ORDER 1:M ORDER_ITEM, ITEM 1:M ORDER_ITEM", "Two FKs"],
  ["StaffID in COMPLAINT (PK in STAFF)", "STAFF 1:M COMPLAINT", "One staff member, many complaints"]
], ["Foreign key", "Relationship", "Why"]);
$("#eG").innerHTML = ''' + json.dumps(E_DEMO) + r''' + '<p class="note">The shop database: CUSTOMER 1:M SHOP_ORDER, SHOP_ORDER 1:M ORDER_ITEM, ITEM 1:M ORDER_ITEM (ORDER_ITEM is the linking table that makes orders and items many-to-many).</p>';
''' + _prjs

finish("as-8-1-2-er-diagrams-normalisation", "as812", "E-R Diagrams and Normalisation",
  "Drawing entity-relationship diagrams from foreign keys, and normalising to first, second and third normal form with a worked example, with animations, labs and the real Paper 1 questions from 2021 to 2026.",
  "8.1.2", "8 · Databases", "section 8.1 Database concepts", learn, watch, explore, _pr, real, where, past, review,
  "Part 1 is real 9618 questions on E-R diagrams and normalisation (Paper 1), 2021 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", tips, js)
