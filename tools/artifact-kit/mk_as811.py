"""AS CS 8.1.1: database concepts: file-based against relational, keys, relationships, referential integrity. Run: python3 tools/artifact-kit/mk_as811.py"""
from ak8 import *

T = {"CUSTOMER": {"cols": ["CustomerID", "FirstName", "LastName", "Town"], "rows": [["HJ231", "Ana", "Lopez", "Leeds"], ["KM455", "Ben", "Okoye", "York"], ["PQ802", "Cleo", "Zhang", "Leeds"]]},
     "SHOP_ORDER": {"cols": ["OrderNo", "CustomerID", "OrderDate"], "rows": [[1001, "HJ231", "02/03/2024"], [1002, "HJ231", "09/03/2024"], [1003, "KM455", "10/03/2024"]]}}
import json

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>A <b>file-based approach</b> stores data in separate files for each application, which causes <b>data redundancy</b> (the same data stored many times), <b>data inconsistency</b>, <b>program-data dependence</b> and poor privacy; a <b>relational database</b> stores each item of data once in <b>linked tables</b>, which addresses these limitations. A <b>table</b> holds data about one <b>entity</b>; each <b>record (tuple)</b> is a row and each <b>field (attribute)</b> a column. A <b>primary key</b> uniquely identifies each record; a <b>foreign key</b> is a field in one table that links to the primary key in another, which creates a <b>relationship</b> (one-to-one, one-to-many or many-to-many). <b>Referential integrity</b> keeps the links valid: every foreign key has a matching primary key, so there are no orphaned records. You must be able to define each term and give an example from the database in the question.</p></div>

  <h2>1 · File-based against relational</h2>
  <div class="tw"><table class="t">
    <tr><th>Limitation of a file-based approach</th><th>How a relational database addresses it</th></tr>
    <tr><td><b>Data redundancy</b>: the same data is stored many times</td><td>Separate linked tables; each item of data is stored once</td></tr>
    <tr><td><b>Data inconsistency</b> and poor integrity: duplicated data may be stored differently or not updated everywhere</td><td>Data changed once in one place updates everywhere; linked data cannot be entered differently in two tables; referential integrity can be enforced</td></tr>
    <tr><td><b>Program-data dependence</b>: a change to the structure of the data means the programs must be rewritten</td><td>The DBMS manages the structure; queries are not dependent on how the data is stored, so changes to the data do not require programs to be rewritten</td></tr>
    <tr><td><b>Complex searches</b> are hard: a new program has to be written each time</td><td>Complex queries are easier to run (using SQL)</td></tr>
    <tr><td><b>Lack of privacy</b>: user views cannot easily be set up</td><td>Different views can be provided so users see only specific aspects of the data</td></tr>
    <tr><td>Poor support for several users at once</td><td>Multiple concurrent access is possible through record locking</td></tr>
  </table></div>

  <h2>2 · Terminology</h2>
  <div class="tw"><table class="t">
    <tr><th>Term</th><th>Meaning</th><th>Example</th></tr>
    <tr><td><b>Entity</b></td><td>Something that data is stored about (an object); one table per entity</td><td>A customer, a house</td></tr>
    <tr><td><b>Table</b> (relation)</td><td>The data about one entity, arranged in rows and columns</td><td>CUSTOMER</td></tr>
    <tr><td><b>Field</b> (attribute)</td><td>A column in a table</td><td>CustomerID in CUSTOMER</td></tr>
    <tr><td><b>Record</b> (tuple)</td><td>A row in a table: one instance of the entity</td><td>The row for customer HJ231</td></tr>
    <tr><td><b>Primary key</b></td><td>The attribute (or combination of attributes) that uniquely identifies each record</td><td>CustomerID</td></tr>
    <tr><td><b>Composite primary key</b></td><td>A primary key made of two or more attributes, because neither is unique alone</td><td>(ActorID, FilmID) in FILM_ACTOR</td></tr>
    <tr><td><b>Candidate key</b></td><td>A field (or set of fields) that could be the primary key</td><td>CardNumber in a card table</td></tr>
    <tr><td><b>Secondary key</b></td><td>A candidate key not chosen as the primary key, or an additional key used to find specific data</td><td>SerialNumber in TELESCOPE</td></tr>
    <tr><td><b>Foreign key</b></td><td>A field in one table that is linked to the primary key in another table</td><td>CustomerID in SHOP_ORDER</td></tr>
    <tr><td><b>Referential integrity</b></td><td>Every foreign key has a corresponding primary key; if data is changed in one place the change is reflected in all related records (cascading update or delete); no orphaned records</td><td>An order cannot refer to a customer that does not exist</td></tr>
  </table></div>

  <h2>3 · Relationships</h2>
  <ul>
    <li><b>One-to-one (1:1):</b> a customer has one set of login details. Implemented by making the primary key of one table the foreign key in the other.</li>
    <li><b>One-to-many (1:M):</b> one customer places many orders. The primary key of the "one" table (CustomerID) becomes a foreign key in the "many" table (SHOP_ORDER).</li>
    <li><b>Many-to-many (M:M):</b> an order contains many products and a product is in many orders. This <b>cannot be directly implemented</b> in a normalised relational database: a <b>linking table</b> (ORDER_ITEM) holds the primary keys of both as foreign keys, turning it into two one-to-many relationships.</li>
  </ul>
  <p>To describe a relationship in an exam answer, name the tables, the type (for example 1:M), the primary key and the matching foreign key: "ShipID is the primary key in SHIP and a foreign key in CONTAINER; one ship carries many containers, and each container is on one ship".</p>

  <h2>Common ways to lose marks</h2>
  <ul>
    <li>Defining a foreign key as "a key from another table" without saying it links to that table's primary key.</li>
    <li>Describing a relationship without naming the keys when the question says to refer to them.</li>
    <li>Saying a many-to-many relationship "is not possible". It is implemented with a linking table.</li>
    <li>Stating the advantage of a relational database without the reason (less redundancy <b>because</b> each item is stored once).</li>
    <li>Confusing field and record: the field is a column, the record is a row.</li>
  </ul>
'''

watch = '''
  <h2>1 · Redundancy in a file against a table</h2>
  <div id="stA"></div>
  <h2>2 · A one-to-many relationship through keys</h2>
  <div id="stB"></div>
  <h2>3 · A many-to-many relationship needs a linking table</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Explore the tables</h2>
  <p>Run a query on two linked tables. Try <span class="mono">SELECT * FROM CUSTOMER</span>, then a join on CustomerID.</p>
  <div class="card" id="dbLab"></div>
  <h2>Lab 2 · Which relationship?</h2>
  <div class="card"><div id="rB" class="btnrow"></div><div id="rO"></div></div>
  <h2>Lab 3 · Primary or foreign key?</h2>
  <div class="card"><div id="kB" class="btnrow"></div><div id="kO"></div></div>
'''

_pr, _prjs = PR(["Which database term?", "Primary key or foreign key?", "Match the term to its definition", "Put the linking-table steps in order", "Working out", "Multiple choice"],
  ("Which term does the description give?", ["Field", "Record (tuple)", "Entity", "Foreign key", "Referential integrity"], [("A column in a table", 0), ("A row in a table", 1), ("Anything data can be stored about", 2), ("A field linked to a primary key in another table", 3), ("Every foreign key has a matching primary key", 4), ("One instance of an entity in a table", 1)], "Column: field. Row: record."),
  ("Primary key or foreign key (in the table given)?", ["Primary key", "Foreign key"], [("CustomerID in CUSTOMER", 0), ("CustomerID in SHOP_ORDER", 1), ("OrderNo in SHOP_ORDER", 0), ("ShipID in CONTAINER (ShipID is the primary key of SHIP)", 1), ("ContainerID in CONTAINER", 0), ("StudentID in PLACEMENT (the key of STUDENT)", 1)], "Primary: identifies the record. Foreign: links to another table."),
  [["Primary key", "Uniquely identifies each record"], ["Candidate key", "A field that could be the primary key"], ["Composite key", "A primary key made of two or more fields"], ["Linking table", "Removes a many-to-many relationship"], ["Orphaned record", "A record whose foreign key has no matching primary key"]],
  ("Put the steps for removing a many-to-many relationship in order.", ["Spot a many-to-many relationship (orders and products)", "Create a new linking table (ORDER_ITEM)", "Add the primary key of each table as a foreign key in it", "Make the pair of foreign keys the composite primary key", "The relationship is now two one-to-many relationships"], "Spot, create, add keys, composite key, two 1:M."),
  [{"q": "A customer table has 500 customers. If their address is stored in every order record (average 6 orders each), how many times is each address stored? (Answer: copies per customer.)", "a": 6, "unit": "", "tol": 0.01, "hint": "Once per order.", "sol": "<b>6</b>: this redundancy is why the address belongs in CUSTOMER once."}, {"q": "A table has 8 fields and 40 records. How many data items (cells)?", "a": 320, "unit": "", "tol": 0.01, "hint": "8 × 40.", "sol": "<b>320</b>."}, {"q": "A table SHIP has 12 rows and each ship carries 10 containers. How many rows in CONTAINER?", "a": 120, "unit": "", "tol": 0.01, "hint": "12 × 10.", "sol": "<b>120</b>."}, {"q": "How many foreign keys does a linking table between two tables have?", "a": 2, "unit": "", "tol": 0.01, "hint": "One for each table.", "sol": "<b>2</b>."}, {"q": "Order 1 has 3 items and order 2 has 2 items. How many rows are in the linking table ORDER_ITEM?", "a": 5, "unit": "", "tol": 0.01, "hint": "3 + 2.", "sol": "<b>5</b>."}],
  [("A primary key:", ["Uniquely identifies each record", "Links to another table", "Is a column that repeats", "Stores a password"], 0, "Unique."), ("A foreign key:", ["Links to another table's primary key", "Is the first field", "Must be a number", "Is a candidate key"], 0, "Link."), ("Many-to-many is implemented with:", ["A linking table", "A bigger field", "Two files", "Nothing"], 0, "Linking table."), ("A record is:", ["A row", "A column", "A table", "A key"], 0, "Row."), ("Referential integrity prevents:", ["Orphaned records", "Typing errors", "Big tables", "Passwords"], 0, "Orphans."), ("A flat-file problem is:", ["Data redundancy", "Easy queries", "Linked tables", "Views"], 0, "Redundancy.")],
  [("Entity", "Something data is stored about."), ("Field", "Column (attribute)."), ("Record", "Row (tuple)."), ("Primary key", "Unique identifier."), ("Foreign key", "Links to a primary key."), ("Candidate key", "Could be the primary key."), ("Linking table", "Removes many-to-many."), ("Referential integrity", "No orphaned records.")])

real = RWNOTE + (
rw("A school's student list on paper and in a spreadsheet", "A student's address appears in the sports list, the library list and the register. When they move, it is changed in one place and not the others: redundancy and inconsistency.", "a relational database stores it once.") +
rw("Online shopping", "Your customer details are stored once; each order links to your customer number, so you can have many orders but one customer record.", "one-to-many with a foreign key.") +
rw("Deleting a customer", "If the shop removes a customer but their orders stay, the orders point at nobody: an orphaned record, which referential integrity prevents.", "referential integrity.") +
rw("Students and clubs", "A student joins many clubs and a club has many students: a many-to-many relationship, held in a membership table.", "linking table.") +
rw("A booking system", "Each seat is identified by its own key; each booking uses that key as a foreign key.", "primary and foreign keys.")
)

where = [
  ("M/J 2021", "11, 13", "7", "3 + 3 + 1 + 3", "Why a file-based approach is not better; examples of relationships; the relationship that cannot be directly implemented; data dictionary items"),
  ("M/J 2021", "12", "1(a)", "6", "Define field, entity and foreign key with examples"),
  ("O/N 2021", "11, 13", "5(a)", "2", "Primary or foreign key for four fields"),
  ("M/J 2022", "11", "4(a)", "4", "The advantages of a relational database over a file-based approach"),
  ("O/N 2022", "11", "4(c)(i)", "2", "What a tuple is, with an example"),
  ("O/N 2022", "12", "5(c)", "1", "What a candidate key is"),
  ("O/N 2022", "13", "2(a)", "3", "A primary key, a candidate key and the degree of a relationship"),
  ("M/J 2023", "11", "2(b)(i)", "2", "Identify two foreign keys and the tables where each is found"),
  ("M/J 2023", "13", "4(a), (b)", "4 + 4", "Two ways a relational database addresses the limits of file-based; entity, tuple, secondary key, foreign key"),
  ("O/N 2023", "11", "3(b)", "3", "Three advantages of a relational database"),
  ("O/N 2023", "12", "2(a)", "3", "Entity, primary key and referential integrity"),
  ("O/N 2024", "11", "2(a), (c)", "3 + 3", "A limitation of file-based and how it is addressed; referential integrity, candidate key, tuple"),
  ("O/N 2024", "12", "6(a)", "3", "The benefits of a relational database"),
  ("M/J 2025", "11", "5(b), (c)", "1 + 2", "A candidate key; tables with foreign keys"),
  ("M/J 2025", "12", "5(a), (b)", "2 + 2", "The purpose of a linking table; the primary keys of four tables"),
  ("O/N 2025", "11", "2(d)", "3", "Referential integrity and how it applies to the database"),
  ("M/J 2026", "13", "4(b)", "2", "Why the library database should enforce referential integrity")]

past = '''  <p class="note">The file-based against relational question and the key definitions are asked almost every series, and the marks are always for a point plus its reason. Questions are reworded from the papers; check the original paper and mark scheme for the exact wording. E-R diagrams and normalisation are on the next page.</p>
''' + peq(SRC("s21", "11/13", "Q7"), "3 + 3 + 1 + 3 marks", "Explain / Give / Tick",
  "Bobby tells Kim that a file-based approach is usually better than a relational database. (a) Explain why Bobby is incorrect. (b) Bobby's shop database stores customers, their payment details, orders and the products. (i) Give one example of each relationship: one-to-one, one-to-many, many-to-many. (ii) Tick the relationship that cannot be directly implemented in a normalised relational database. (c) A database has a data dictionary. Give three items that are stored in a data dictionary.", "Redundancy, dependence, inconsistency; examples; many-to-many; table, field, data type.",
  "<p><b>(a)</b> Any three (a point and its reason): " + mks(["The flat file has more data redundancy, because the same data is stored many times", "There is program-data dependence, because a change to the structure of the data means the programs have to be rewritten", "More data inconsistency (worse integrity), because duplicated data might be stored differently or not updated everywhere", "It is not easy to perform complex queries, because a new program has to be written each time", "A lack of privacy, as user views cannot easily be implemented"]) + "</p><p><b>(b)(i)</b> " + mks(["One-to-one: customer to payment details, or customer to login details", "One-to-many: customer to order", "Many-to-many: order to product, or customer to product"], "a") + " <b>(ii)</b> " + mks(["Many-to-many"], "b") + "</p><p><b>(c)</b> Any three: " + mks(["table name", "field name (attribute)", "data type", "type of validation", "primary key", "foreign key", "relationships"], "c") + "</p>", "Saying a relational database 'is more organised'. Give redundancy, consistency or dependence with the reason.") + peq(SRC("s21", "12", "Q1(a)"), "6 marks", "Define",
  "The database HOUSE_RENTALS has CUSTOMER(CustomerID, FirstName, LastName, DateOfBirth, Email), HOUSE(HouseID, HouseNumber, Road, Town, Bedrooms, Bathrooms) and RENTAL(RentalID, CustomerID, HouseID, MonthlyCost, DepositPaid). Give the definition of field, entity and foreign key, using an example from the database for each.", "Definition and example for each term.",
  "<p>One mark for each definition and one for each example: " + mks(["Field: a column or attribute in a table; e.g. CustomerID in the table CUSTOMER", "Entity: anything that data can be stored about; e.g. a customer or a house", "Foreign key: a field in one table that is linked to a primary key in another table; e.g. CustomerID or HouseID in the table RENTAL"]) + "</p>", None) + peq(SRC("w21", "11/13", "Q5(a)"), "2 marks", "Tick",
  "CARS has SHOP(ShopID, ManagerID, Address, Town, TelephoneNumber), MANAGER(ManagerID, FirstName, LastName, DateOfBirth, Wage) and CAR(RegistrationNumber, Make, Model, NumberOfMiles, ShopID). Tick whether each field is a primary key or a foreign key: MANAGER.ManagerID; SHOP.ManagerID; CAR.RegistrationNumber; CAR.ShopID.", "The key of its own table is primary; the key of another table is foreign.",
  "<p>" + mks(["MANAGER.ManagerID: primary key", "SHOP.ManagerID: foreign key", "CAR.RegistrationNumber: primary key", "CAR.ShopID: foreign key"]) + " (2 or 3 correct: 1 mark; all 4: 2 marks)</p>", None) + peq(SRC("s22", "11", "Q4(a)"), "4 marks", "Describe",
  "A teacher uses the relational database MARKS with STUDENT, TEST and STUDENT_TEST tables. Describe the advantages of using a relational database compared to a file-based approach.", "Reduced redundancy, consistency, independence, queries, views, each with a reason.",
  "<p>Any four: " + mks(["Reduced data redundancy, because each item of data is only stored once", "Maintains data consistency or improves data integrity, because changes in one table update the others automatically and linked data cannot be entered differently in two tables", "Program-data independence, because changes to the data do not require programs to be rewritten", "Complex queries are easier to run", "Can provide different views, so users can only see specific aspects of the database"]) + "</p>", None) + peq(SRC("w22", "11", "Q4(c)(i)"), "2 marks", "State",
  "State what is meant by a tuple. Give an example of a tuple from PHOTO_DATA (PhotoID, PartyID, TimeTaken, CameraID).", "A single row; give a whole row.",
  "<p>" + mks(["A single row in a table", "Example: a whole row from the PHOTO_DATA table, such as ST23-56, BD987, 08:34, NIK-02"]) + "</p>", None) + peq(SRC("w22", "12", "Q5(c)"), "1 mark", "State",
  "State what is meant by a candidate key in a relational database.", "Could be the primary key.",
  "<p>" + mks(["An attribute (field), or set of attributes, that could be a primary key"]) + "</p>", None) + peq(SRC("w22", "13", "Q2(a)"), "3 marks", "Complete",
  "ASTRONOMY has COMPANY(TelephoneNumber, CompanyID, CompanyName), PHOTOGRAPH(PhotoID, TelescopeID, DateTaken, TimeTaken, Elevation) and TELESCOPE(TelescopeID, CompanyID, SerialNumber). Write: a suitable primary key in COMPANY; a candidate key in TELESCOPE; the degree of relationship between TELESCOPE and PHOTOGRAPH.", "A telescope takes many photographs.",
  "<p>" + mks(["CompanyID", "SerialNumber (or TelescopeID)", "1:M (one to many)"]) + "</p>", None) + peq(SRC("s23", "11", "Q2(b)(i)"), "2 marks", "Identify",
  "Birds has BIRD_TYPE(BirdID, Name, Size), BIRD_SEEN(SeenID, BirdID, Date, Location, PersonID) and PERSON(PersonID, FirstName, LastName, EmailAddress). Identify two foreign keys and the table where each is found.", "BIRD_SEEN holds links to BIRD_TYPE and PERSON.",
  "<p>" + mks(["BirdID in BIRD_SEEN", "PersonID in BIRD_SEEN"]) + "</p>", None) + peq(SRC("s23", "13", "Q4(a)(b)"), "4 + 4 marks", "Describe / Complete",
  "(a) Describe two ways in which a relational database addresses the limitations of a file-based approach. (b) Complete the table: the term for 'an object that data is stored about'; tuple; secondary key; the term for 'a field in one table that is linked to a primary key in another table'.", "Redundancy and dependence with reasons. Entity, a row, alternative key, foreign key.",
  "<p><b>(a)</b> Mark in pairs, max 2 each: " + mks(["Reduces data redundancy, because linked tables mean each data item is stored only once", "Reduces program-data dependency, because the data is separate from the software so changes to the data do not require programs to be rewritten", "Reduces data inconsistency (improves integrity), because data only needs updating once and linked data cannot be entered differently", "Complex queries are easier to run", "Different views can be provided"]) + "</p><p><b>(b)</b> " + mks(["Entity", "Tuple: a row of data in a table about one instance of an object", "Secondary key: an additional or alternative key used as well as the primary key to locate specific data, or a candidate key not chosen as the primary key", "Foreign key"], "a") + "</p>", None) + peq(SRC("w23", "11", "Q3(b)"), "3 marks", "Identify",
  "Identify three advantages of a relational database compared to a file-based approach.", "Redundancy, integrity, views, independence, queries.",
  "<p>Any three: " + mks(["Reduced data redundancy", "Improved data integrity, consistency or referential integrity", "Allows for views and improved privacy", "Allows for program-data independence", "Complex queries can be executed"]) + "</p>", None) + peq(SRC("w23", "12", "Q2(a)"), "3 marks", "State",
  "State what is meant by the following terms in a relational database model: entity; primary key; referential integrity.", "Object; unique identifier; consistent links.",
  "<p>" + mks(["Entity: an object about which data can be stored", "Primary key: the unique attribute or combination of attributes used to identify the record", "Referential integrity: makes sure that if data is changed in one place the change is reflected in all related records; or that every foreign key has a corresponding primary key"]) + "</p>", None) + peq(SRC("w24", "11", "Q2(a)(c)"), "3 + 3 marks", "Give / Define",
  "(a) Give one limitation of using a file-based approach to store data and explain how a relational database addresses it. (c) Write a definition of referential integrity, candidate key and tuple.", "Redundancy with linked tables. Consistent links; could be primary; a row.",
  "<p><b>(a)</b> One mark for the limitation and two for the explanation: " + mks(["Data redundancy: separate linked tables are used, so each data item is stored once", "Data inconsistency: data changed once in one place updates elsewhere; linked data cannot be entered differently; referential integrity can be enforced", "Dependence on the data structure: changes are managed by the DBMS and queries and programs do not depend on the structure of the data"]) + "</p><p><b>(c)</b> " + mks(["Referential integrity: all duplicate entries of data between tables are consistent, or all foreign keys are matched to an appropriate primary key", "Candidate key: a field that could be a primary key but is not (the smallest set of attributes where no tuple has the same value)", "Tuple: a row or record in a table, one instance of an entity"], "a") + "</p>", None) + peq(SRC("w24", "12", "Q6(a)"), "3 marks", "Explain",
  "Explain the benefits of using a relational database instead of a file-based approach.", "Redundancy, consistency, independence, queries, views, concurrent access.",
  "<p>Any three: " + mks(["Reduced data redundancy, because each item is stored only once", "Data consistency is maintained because changes in one table update the others", "Program-data independence is ensured", "Complex queries are easier to run", "Different views can be provided so users see only what they need", "Multiple concurrent access is possible through record locking"]) + "</p>", None) + peq(SRC("s25", "11", "Q5(b)(c)"), "1 + 2 marks", "Identify",
  "FURNITURE has CUSTOMER(CustomerID, Name, Phone), CUSTOMER_CARD_DATA(CardID, CustomerID, CardType, CardNumber, EndDate), ORDER(OrderID, CustomerID, TotalCost, Paid, OrderDate, Complete) and ORDER_ITEM(OrderItemID, OrderID, Type, Height, Width, Depth, Details). (b) Identify one attribute in CUSTOMER_CARD_DATA that could be a candidate key. (c) Identify two tables that contain a foreign key and give one foreign key in each.", "CardNumber. OrderID in ORDER_ITEM; CustomerID in ORDER or CUSTOMER_CARD_DATA.",
  "<p><b>(b)</b> " + mks(["CardNumber"]) + "</p><p><b>(c)</b> " + mks(["ORDER_ITEM: OrderID", "ORDER: CustomerID, or CUSTOMER_CARD_DATA: CustomerID"], "a") + "</p>", None) + peq(SRC("s25", "12", "Q5(a)(b)"), "2 + 2 marks", "Explain / Underline",
  "The game database has USER(Username, Password, DateOfBirth), CHARACTER(CharacterName, CharacterID, Username, Level, Money), ITEM(ItemName, MinimumLevel, Cost) and CHARACTER_ITEM(CharacterID, ItemName). (a) Explain the purpose of the table CHARACTER_ITEM. (b) Give the primary key in each table.", "Linking table for many-to-many.",
  "<p><b>(a)</b> Any two: " + mks(["To remove the many-to-many relationship between CHARACTER and ITEM", "To allow each character to have many items, and each item to be bought for many characters, by creating a linking table", "recording the items purchased for each character"]) + "</p><p><b>(b)</b> " + mks(["USER: Username; CHARACTER: CharacterID; ITEM: ItemName (the three single keys)", "CHARACTER_ITEM: (CharacterID, ItemName) as a composite key"], "a") + "</p>", None) + peq(SRC("w25", "11", "Q2(d)"), "3 marks", "Explain",
  "WORKEXPERIENCE has STUDENT(StudentID, FirstName, TelephoneNumber, UniversityName), PLACEMENT(PlacementID, StudentID, CompanyID, StartDate, EndDate, Complete) and COMPANY(CompanyID, CompanyName, MaxStudentsPerPlacement). Explain what is meant by referential integrity, and how it applies to this database.", "Foreign key has a primary key; cascade; example from the database.",
  "<p>Generic (max 2): " + mks(["Referential integrity ensures related data is consistent", "It ensures every foreign key has a corresponding primary key", "It provides for cascading update or delete, stopping orphaned records"]) + " Specific (max 2): " + mks(["CompanyID is a foreign key in PLACEMENT and depends on the primary key CompanyID in COMPANY", "If a record is deleted from STUDENT, all records with the same StudentID are deleted from PLACEMENT", "If a CompanyID is changed in COMPANY all records with that CompanyID in PLACEMENT are changed"], "a") + "</p>", "Giving only the general definition when the question asks how it applies to this database.") + peq(SRC("s26", "13", "Q4(b)"), "2 marks", "Explain",
  "Explain the reasons why the library database should enforce referential integrity.", "Consistent, valid links, no orphans, cascade.",
  "<p>Any two: " + mks(["Ensures consistency of data, so it is up to date and not redundant", "Ensures the relationships between data remain valid and prevents orphaned records", "If a change is made in one place it is made everywhere else (cascading updates or deletes)", "Every foreign key has a corresponding primary key"]) + "</p>", None)

review = req("3 marks", "Explain", "Explain two limitations of a school keeping its student data in separate spreadsheets for each department.", "Redundancy and inconsistency.", "<p>" + mks(["The same data, such as an address, is stored many times (redundancy)", "When a student's details change, they may be updated in one spreadsheet and not the others (inconsistency)", "A relational database stores each item once and links tables"]) + "</p>", None) + req("3 marks", "Describe", "Describe the relationship between STUDENT(StudentID, ...) and ABSENCE(AbsenceID, StudentID, Date) referring to the keys.", "StudentID in both.", "<p>" + mks(["StudentID is the primary key in STUDENT and a foreign key in ABSENCE", "One student can have many absences (1:M)", "Each absence is for only one student"]) + "</p>", None) + req("2 marks", "Explain", "Explain how a many-to-many relationship between BOOK and AUTHOR is implemented.", "Linking table.", "<p>" + mks(["A linking table (for example BOOK_AUTHOR) is created", "containing the primary key of BOOK and of AUTHOR as foreign keys, giving two one-to-many relationships"]) + "</p>", None) + req("2 marks", "State", "State two items stored in a data dictionary.", "Metadata.", "<p>" + mks(["Table and field names", "Data types, validation rules, primary or foreign keys, relationships"]) + "</p>", None) + req("2 marks", "Explain", "Explain what an orphaned record is and how it is prevented.", "Referential integrity.", "<p>" + mks(["A record whose foreign key has no matching primary key in the linked table", "Referential integrity prevents it, for example by cascading deletes"]) + "</p>", None)

tips = tips_html([
  ("A point and its reason.", "Redundancy because each item is stored once."),
  ("Field: column. Record: row.", "Entity: the object."),
  ("Name both keys.", "Primary in one table, foreign in the other."),
  ("Many-to-many: linking table.", "Two foreign keys."),
  ("Referential integrity: no orphans.", "Every foreign key has a primary key."),
  ("Use the example asked for.", "From the database in the question."),
], [("a primary key", "Uniquely identifies each record in a table."), ("a foreign key", "A field linked to the primary key of another table."), ("an entity", "Something data is stored about."), ("referential integrity", "Foreign keys always match a primary key.")],
  [("State", "Short answer."), ("Define", "Say what it means, with an example."), ("Explain", "Reasons as well."), ("Describe", "Several points.")]) + FC

js = AKJS + AK20JS + SQLJS + "const DBT = " + json.dumps(T) + ";\n" + r'''
(function () {
  const draw = (s) => { const k = Math.round(s.i); const rows = ["Ana  Lopez  12 High St  order: chair", "Ana  Lopez  12 High St  order: desk", "Ana  Lopez  12 High St  order: lamp"]; let o = SV.text(20, 18, k === 0 ? "File-based: the address is repeated in every order" : "Relational: the address is stored once", "lbl bd", { style: "font-size:13px" });
    if (k === 0) rows.forEach((r, i) => o += SV.rect(20, 30 + i * 30, 480, 24, i === 1 ? "f2" : "cell", { rx: 4 }) + SV.text(30, 47 + i * 30, r, "lbl", { style: "font-size:12px" })); else { o += SV.rect(20, 30, 220, 28, "f1", { rx: 4 }) + SV.text(30, 49, "CUSTOMER: Ana Lopez, 12 High St", "lbl", { style: "font-size:12px" }); ["chair", "desk", "lamp"].forEach((r, i) => o += SV.rect(280, 30 + i * 30, 220, 24, "cell", { rx: 4 }) + SV.text(290, 47 + i * 30, "ORDER: " + r + " (CustomerID)", "lbl", { style: "font-size:12px" })); }
    return o; };
  Lib.stepper($("#stA"), { w: 520, h: 130, label: "Redundancy", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: ["In a file the address is stored again for every order: <b>redundancy</b>. If it changes, one copy may be missed: <b>inconsistency</b>.", "In a relational database the address is stored <b>once</b> in CUSTOMER and each order links to it."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.text(20, 18, "CUSTOMER", "lbl bd") + SV.text(300, 18, "SHOP_ORDER", "lbl bd");
    [["HJ231", "Ana"], ["KM455", "Ben"]].forEach(([id, n], i) => o += SV.rect(20, 28 + i * 34, 210, 28, k >= 1 && i === 0 ? "f3" : "cell", { rx: 4 }) + SV.text(30, 47 + i * 34, id + "  " + n + "   (PK: CustomerID)", "lbl", { style: "font-size:12px" }));
    [[1001, "HJ231"], [1002, "HJ231"], [1003, "KM455"]].forEach(([n, c], i) => o += SV.rect(300, 28 + i * 34, 220, 28, k >= 1 && c === "HJ231" ? "f3" : "cell", { rx: 4 }) + SV.text(310, 47 + i * 34, n + "  " + c + "   (FK)", "lbl", { style: "font-size:12px" }));
    o += SV.text(20, 150, ["", "CustomerID is the primary key in CUSTOMER", "and a foreign key in SHOP_ORDER: one customer, many orders"][k], "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stB"), { w: 540, h: 170, label: "Keys", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: ["Two linked tables.", "<b>CustomerID</b> is the <b>primary key</b> in CUSTOMER.", "It is a <b>foreign key</b> in SHOP_ORDER, giving a <b>one-to-many</b> relationship."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const B = (x, y, t, on) => SV.rect(x, y, 130, 34, on ? "f3" : "cell", { rx: 6 }) + SV.text(x + 65, y + 22, t, "lbl bd", { "text-anchor": "middle", style: "font-size:12px" }); let o = B(20, 40, "ORDER", true) + B(390, 40, "PRODUCT", true);
    if (k === 0) o += SV.path("M150,57 H390", "ax") + SV.text(270, 50, "many : many", "sm", { "text-anchor": "middle" }); else { o += B(205, 40, "ORDER_ITEM", true) + SV.path("M150,57 H205", "ax") + SV.path("M335,57 H390", "ax") + SV.text(177, 50, "1:M", "sm", { "text-anchor": "middle" }) + SV.text(362, 50, "M:1", "sm", { "text-anchor": "middle" }); }
    o += SV.text(20, 110, ["cannot be directly implemented", "a linking table with both keys: two one-to-many relationships", "ORDER_ITEM(OrderNo, ItemNumber, Quantity): composite primary key"][Math.min(k, 2)], "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stC"), { w: 540, h: 130, label: "Linking table", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: ["An order has many products and a product is in many orders: <b>many-to-many</b>.", "A <b>linking table</b> holds the primary keys of both as foreign keys.", "The pair of keys forms a <b>composite primary key</b>; each side is now one-to-many."].map((c, i) => ({ cap: c, s: { i } })) });
})();
sqlLab("#dbLab", DBT, "SELECT CUSTOMER.FirstName, SHOP_ORDER.OrderNo\nFROM CUSTOMER INNER JOIN SHOP_ORDER\nON CUSTOMER.CustomerID = SHOP_ORDER.CustomerID;", { rows: 4 });
btnTable("rB", "rO", [
  ["Customer and the login details they have", "One-to-one", "Each customer has one set of login details"],
  ["Customer and the orders they place", "One-to-many", "Many orders for one customer"],
  ["Order and the products it contains", "Many-to-many", "Needs a linking table"],
  ["Ship and the containers it carries", "One-to-many", "ShipID is a foreign key in CONTAINER"],
  ["Character and the items they buy", "Many-to-many", "Linking table CHARACTER_ITEM"]
], ["Situation", "Relationship", "Why"]);
btnTable("kB", "kO", [
  ["CustomerID in CUSTOMER", "Primary key", "Identifies each customer"],
  ["CustomerID in SHOP_ORDER", "Foreign key", "Links to CUSTOMER"],
  ["(ActorID, FilmID) in FILM_ACTOR", "Composite primary key", "Neither is unique alone"],
  ["SerialNumber in TELESCOPE", "Candidate key", "Could be the primary key"],
  ["OrderNo in ORDER_ITEM", "Part of the key and a foreign key", "Links to the order"]
], ["Field", "Kind of key", "Why"]);
''' + _prjs

finish("as-8-1-1-database-concepts", "as811", "Database Concepts: Keys and Relationships",
  "File-based against relational databases, entities, tables, records, fields, primary, foreign, candidate and secondary keys, the three kinds of relationship and referential integrity, with animations, an SQL lab and the real Paper 1 questions from 2021 to 2026.",
  "8.1.1", "8 · Databases", "section 8.1 Database concepts", learn, watch, explore, _pr, real, where, past, review,
  "Part 1 is real 9618 questions on database concepts (Paper 1), 2021 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", tips, js)
