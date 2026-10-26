"""AS CS 8.2: Database Management Systems. Run: python3 tools/artifact-kit/mk_as82.py"""
from ak8 import *

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>A <b>Database Management System (DBMS)</b> is software used to create, maintain and query a database. Its main tools are the <b>data dictionary</b> (metadata: data about the data, such as table and field names, data types, validation rules, keys and relationships), the <b>logical schema</b> (a model of the database, such as an E-R diagram, not specific to one DBMS), the <b>query processor</b> (takes the user's criteria, searches, and returns and organises the results) and the <b>developer interface</b> (tools to create tables, relationships, forms, reports and queries). A DBMS provides <b>security</b> with authentication, <b>access rights</b>, <b>views</b>, back-up and recovery, encryption and record locking, and supports <b>integrity</b> with validation, referential integrity and normalisation. Exam answers name the tool and say what it does or contains.</p></div>

  <h2>1 · DBMS features and tools</h2>
  <div class="tw"><table class="t">
    <tr><th>Tool</th><th>What it is or does</th></tr>
    <tr><td><b>Data dictionary</b></td><td>Stores <b>metadata</b>, data about the data in the database or the structure of the database: table names, field (attribute) names, data types, validation rules, primary and foreign keys, relationships</td></tr>
    <tr><td><b>Logical schema</b></td><td>An overview of the database structure that models the problem, using methods such as an E-R diagram; independent of any particular DBMS; shows the relationship between data and its structure</td></tr>
    <tr><td><b>Query processor</b></td><td>Allows the user to enter criteria, searches for the data that meets them (processes and executes queries written in SQL) and organises the results to display to the user</td></tr>
    <tr><td><b>Developer interface</b></td><td>Allows the user to create, modify and delete tables, set up relationships, create forms for data input (with drop-down boxes and buttons), design reports and menus, and run SQL queries</td></tr>
  </table></div>

  <h2>2 · Security</h2>
  <div class="tw"><table class="t">
    <tr><th>Method</th><th>How it protects the data</th></tr>
    <tr><td><b>Authentication</b> (passwords, biometrics, two-factor)</td><td>Prevents unauthorised access to the data</td></tr>
    <tr><td><b>Access rights</b> (privileges)</td><td>Different users or accounts get different permissions to different tables (read only, read and write, full access, no access), so only those with permission can read or edit the data</td></tr>
    <tr><td><b>Views</b></td><td>Different users see different parts of the database, only what they need to see (for example a manager sees only their own shops)</td></tr>
    <tr><td><b>Back-up and recovery</b></td><td>The DBMS takes copies of the database automatically on a regular basis (stored off site) so the data can be recovered if lost or damaged</td></tr>
    <tr><td><b>Encryption</b></td><td>Data is turned into cipher text so it cannot be understood without the decryption key</td></tr>
    <tr><td><b>Record and table locking</b></td><td>Prevents simultaneous access to the same data so updates are not lost or overwritten</td></tr>
  </table></div>

  <h2>3 · Integrity</h2>
  <p>A DBMS supports data integrity by enforcing <b>validation</b> rules, <b>referential integrity</b> (with cascading updates and deletes), and a normalised design, and by <b>record locking</b> so concurrent changes are consistent.</p>

  <h2>Common ways to lose marks</h2>
  <ul>
    <li>Describing the data dictionary as "a list of words". It stores metadata: table names, field names, data types, validation rules and keys.</li>
    <li>Confusing the logical schema (the design, independent of any DBMS) with the data dictionary (the stored description).</li>
    <li>Naming a security method without how it protects the data ("access rights" needs "so only those with permission can read or edit").</li>
    <li>Saying the query processor "stores queries". It takes criteria, finds matching data and organises the results.</li>
    <li>Describing the developer interface as "typing SQL". It is the set of tools to build tables, forms and reports.</li>
  </ul>
'''

watch = '''
  <h2>1 · A query goes through the DBMS</h2>
  <div id="stA"></div>
  <h2>2 · Views and access rights</h2>
  <div id="stB"></div>
  <h2>3 · Record locking</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Access rights</h2>
  <p>Choose a user and see what the DBMS allows.</p>
  <div class="card"><div id="aB" class="btnrow"></div><div id="aO"></div></div>
  <h2>Lab 2 · Which DBMS tool?</h2>
  <div class="card"><div id="tB" class="btnrow"></div><div id="tO"></div></div>
  <h2>Lab 3 · Which security method?</h2>
  <div class="card"><div id="sB" class="btnrow"></div><div id="sO"></div></div>
'''

_pr, _prjs = PR(["Which DBMS tool?", "Security or integrity?", "Match the tool to its description", "Put the query steps in order", "Working out", "Multiple choice"],
  ("Which DBMS tool does it describe?", ["Data dictionary", "Logical schema", "Query processor", "Developer interface"], [("Stores field names and data types", 0), ("A model of the database not specific to one DBMS", 1), ("Finds the data that matches the user's criteria", 2), ("Lets the user create forms and reports", 3), ("Stores validation rules and keys", 0), ("Uses an E-R diagram to show structure", 1)], "Match the tool."),
  ("Does it support security or integrity?", ["Security", "Integrity"], [("Access rights", 0), ("Referential integrity", 1), ("Views", 0), ("Validation rules", 1), ("Encryption", 0), ("Cascading updates and deletes", 1)], "Access, views, encryption: security."),
  [["Data dictionary", "Metadata: data about the data"], ["Logical schema", "A model independent of any DBMS"], ["Query processor", "Searches for data meeting criteria"], ["Developer interface", "Tools to build tables, forms and reports"], ["View", "A user sees only part of the database"]],
  ("Put the query steps in order.", ["The user enters criteria", "The query processor reads the criteria", "It searches the tables for matching data", "It organises the results", "The results are displayed to the user"], "Enter, read, search, organise, display."),
  [{"q": "A back-up is taken every day and kept for 14 days. How many back-ups are kept?", "a": 14, "unit": "", "tol": 0.01, "hint": "One a day.", "sol": "<b>14</b>."}, {"q": "A table has 5 users; 2 have full access, 2 read-only and 1 none. How many can read it?", "a": 4, "unit": "", "tol": 0.01, "hint": "2 + 2.", "sol": "<b>4</b>."}, {"q": "Two users update a record of 100 at the same time, each adding 10, with no locking. The final value is 110 instead of 120. How many units are lost?", "a": 10, "unit": "", "tol": 0.01, "hint": "120 − 110.", "sol": "<b>10</b>."}, {"q": "A data dictionary holds 6 tables with 8 fields each. How many field entries?", "a": 48, "unit": "", "tol": 0.01, "hint": "6 × 8.", "sol": "<b>48</b>."}, {"q": "How many security methods are in the Learn tab table?", "a": 6, "unit": "", "tol": 0.01, "hint": "Count rows.", "sol": "<b>6</b>."}],
  [("The data dictionary stores:", ["Metadata", "Only passwords", "Query results", "Back-ups"], 0, "Metadata."), ("A view lets a user:", ["See only part of the database", "Delete tables", "Change keys", "Compile SQL"], 0, "Part only."), ("The query processor:", ["Finds data matching criteria", "Creates forms", "Encrypts data", "Draws E-R diagrams"], 0, "Criteria."), ("Record locking prevents:", ["Lost updates", "Large tables", "Passwords", "Views"], 0, "Lost updates."), ("The logical schema is:", ["Independent of any DBMS", "A table", "An SQL query", "A password"], 0, "Independent."), ("Access rights:", ["Give users different permissions", "Store keys", "Make tables", "Search data"], 0, "Permissions.")],
  [("Data dictionary", "Metadata: names, types, rules, keys."), ("Logical schema", "Model of the database, not DBMS-specific."), ("Query processor", "Criteria in, results out."), ("Developer interface", "Tables, forms, reports, SQL."), ("Access rights", "Different permissions per user."), ("View", "Part of the database for a user."), ("Record locking", "Stops lost updates."), ("Back-up", "Recover lost data.")])

real = RWNOTE + (
rw("A shop manager and a till operator", "The manager can see sales for all shops and change prices; the till operator can only add sales. Different access rights and views for each.", "access rights and views.") +
rw("Two people booking the last seat", "The DBMS locks the seat record while one booking is processed so the second person cannot book it too.", "record locking.") +
rw("Searching a library catalogue", "You type criteria such as an author; the query processor finds the books and lists them in order.", "query processor.") +
rw("A new form for entering orders", "The database designer drags fields onto a form with drop-down boxes using the developer interface.", "developer interface.") +
rw("A nightly copy of the database", "Stored off site, so if the server fails the data can be recovered.", "back-up and recovery.")
)

where = [
  ("O/N 2021", "11, 13", "5(b)", "3", "How access rights protect the data in Javier's database"),
  ("O/N 2021", "12", "6(b)", "3", "The purpose and contents of the data dictionary"),
  ("M/J 2022", "12", "5(e)", "6", "Complete the description of the features and tools of a DBMS"),
  ("O/N 2022", "12", "5(d)", "2 + 2", "A data dictionary with an example; a logical schema"),
  ("O/N 2022", "13", "2(b), (f)", "1 + 2", "The feature that describes the relationship between data and its structure; the purpose of a query processor"),
  ("M/J 2023", "11", "2(a)", "2 + 2", "A data dictionary; data integrity with an example"),
  ("M/J 2023", "12", "2(a), (b)", "4 + 3", "Complete the table of DBMS features; why referential integrity is important"),
  ("O/N 2023", "12", "2(b)", "4", "Methods a DBMS can use to improve security"),
  ("M/J 2025", "12", "5(c)", "4 + 2", "Two methods to protect the data; two ways a DBMS supports integrity"),
  ("O/N 2025", "12", "4(d)", "2", "The purpose of a developer interface"),
  ("O/N 2025", "13", "5(d)", "4", "Two ways the DBMS can ensure the security of customer data"),
  ("M/J 2026", "12", "3(c)", "5", "Complete the description of data dictionary, logical schema, access rights and developer interface")]

past = '''  <p class="note">The four DBMS tools and the security methods are asked in a different layout each series (complete a paragraph, complete a table, describe). Questions are reworded from the papers; check the original paper and mark scheme for the exact wording.</p>
''' + peq(SRC("w21", "11/13", "Q5(b)"), "3 marks", "Describe",
  "Describe the ways in which access rights can be used to protect the data in Javier's database from unauthorised access.", "Different accounts, different permissions, views for each manager.",
  "<p>" + mks(["Access rights give managers and Javier access to different elements", "by having different accounts or logins", "which have different access rights, for example read only, no access, read and write", "Specific views can be assigned, for example managers can only see the data for their own shops"]) + " (max 3)</p>", None) + peq(SRC("w21", "12", "Q6(b)"), "3 marks", "Describe",
  "The shop manager uses a DBMS. Describe the purpose and contents of the data dictionary in the DBMS.", "Metadata; names, types, rules, keys.",
  "<p>" + mks(["Purpose: stores metadata about the database"]) + " Contents, any two: " + mks(["field or attribute names", "table names", "validation rules", "data types", "primary or foreign keys", "relationships"], "a") + "</p>", None) + peq(SRC("s22", "12", "Q5(e)"), "6 marks", "Complete",
  "Complete the descriptions of the features and tools found in a DBMS using the given terms (not all are used): data dictionary, field names, primary keys, logical schema, query, interface, input, output, Boolean, data redundancy, normalisation, structure, operating system. A DBMS provides data management. This includes the development of a ... that stores information about the data stored, such as ... and ... . The ... uses methods, such as an E-R diagram, to show the structure of the database and its relationships. The ... processor allows a user to perform searches to find specific data. The DBMS also provides a developer ... that allows the user to create tables, forms and reports.", "Data dictionary, field names and primary keys, logical schema, query, interface.",
  "<p>" + mks(["data dictionary", "field names (or primary keys)", "primary keys (or field names)", "logical schema", "query", "interface"]) + "</p>", None) + peq(SRC("w22", "12", "Q5(d)"), "2 + 2 marks", "Describe",
  "(i) Describe, using an example, what is meant by a data dictionary. (ii) Describe what is meant by a logical schema.", "Metadata with an example. Overview, models the problem, independent of the DBMS.",
  "<p><b>(i)</b> " + mks(["Stores metadata about the database", "Example: field names, table names, validation rules, data types, primary or foreign keys, or relationships"]) + "</p><p><b>(ii)</b> Any two: " + mks(["The overview of a database structure", "It models the problem or situation", "by using methods such as an E-R diagram", "It is independent of any particular DBMS"], "a") + "</p>", None) + peq(SRC("w22", "13", "Q2(b)(f)"), "1 + 2 marks", "Identify / Describe",
  "(b) Identify the DBMS feature that describes the relationship between data and its structure. (f) Describe the purpose of a query processor in a DBMS.", "Logical schema. Criteria, search, organise results.",
  "<p><b>(b)</b> " + mks(["Logical schema"]) + "</p><p><b>(f)</b> Any two: " + mks(["Allows the user to enter criteria", "Searches for the data that meets the entered criteria", "Organises the results to be displayed to the user"], "a") + "</p>", None) + peq(SRC("s23", "11", "Q2(a)"), "2 + 2 marks", "State",
  "(i) State what is meant by a data dictionary and give one example of an item typically found in it. (ii) State what is meant by data integrity and give one example of how it is implemented in a database.", "Data about the data. Consistent data; referential integrity or validation.",
  "<p><b>(i)</b> " + mks(["Data about the data in the database, or data about its structure (metadata)", "Example: table names, data types or field names"]) + "</p><p><b>(ii)</b> " + mks(["Methods of making sure the data is consistent", "Example: enforcing referential integrity (cascading update or delete), or validation and verification rules"], "a") + "</p>", None) + peq(SRC("s23", "12", "Q2(a)(b)"), "4 + 3 marks", "Complete / Explain",
  "(a) Complete the table of DBMS features: data dictionary; query processor; a model of a database that is not specific to one DBMS; a software tool that allows the user to create items such as tables, forms and reports. (b) Explain the reasons why referential integrity is important in a database.", "Metadata; software that finds results; logical schema; developer interface.",
  "<p><b>(a)</b> " + mks(["Data dictionary: data about the data or the structure of the database", "Query processor: software that allows the user to enter criteria then finds and returns the result, or processes and executes SQL queries", "Logical schema: a model of a database that is not specific to one DBMS", "Developer interface: a software tool that allows the user to create tables, forms and reports"]) + "</p><p><b>(b)</b> Any three: " + mks(["It makes sure data is consistent and up to date", "It ensures every foreign key has a corresponding primary key", "It prevents records being added, deleted or modified incorrectly", "If data is changed in one place the change is reflected in all related records", "It makes sure queries return accurate and complete results"], "a") + "</p>", None) + peq(SRC("w23", "12", "Q2(b)"), "4 marks", "Describe",
  "Authentication is one method a DBMS can use to improve the security of a database. Describe other methods that a DBMS can use to improve the security of a database.", "Back-up, access rights, views, locking, encryption, each with how.",
  "<p>Any four (max 2 if no descriptions): " + mks(["Back-up and recovery: copies of the database taken automatically and stored off site so the data can be recovered if lost", "Access rights: different users get different permissions to different tables, for example read only or full access", "Views: different users see different parts of the database, only what they need to see", "Record and table locking: prevents simultaneous access so updates are not lost or overwritten", "Encryption: the data is turned into cipher text so it cannot be understood without a key"]) + "</p>", None) + peq(SRC("s25", "12", "Q5(c)"), "4 + 2 marks", "Identify / Give",
  "(i) Identify two methods the DBMS can use to protect the data in the table USER from unauthorised access, and explain how each protects the data. (ii) Give two ways a DBMS can support data integrity.", "Access rights, password, encryption, views. Validation, referential integrity.",
  "<p><b>(i)</b> " + mks(["Access rights: appropriate permissions for the table are needed to read or edit the data", "A password for the database or table: prevents users without the password from accessing the data", "Encrypting the database: stops users without the key from understanding the data", "Views: users can be given a view that does not include the table USER"]) + " (a method and its explanation, twice)</p><p><b>(ii)</b> " + mks(["Validation", "Enforce referential integrity", "Cascade update or delete", "Ensuring the database is normalised"], "a") + " (any two)</p>", None) + peq(SRC("w25", "12", "Q4(d)"), "2 marks", "Describe",
  "Describe the purpose of a developer interface in a DBMS.", "Create tables, relationships, forms, reports, queries.",
  "<p>Any two: " + mks(["To allow the user to create, modify and delete tables, or maintain the database", "To allow the user to set up or modify relationships", "To allow the user to create a form for data input, with tools such as drop-down boxes or buttons", "To allow the user to design a report", "To allow the user to inspect the database contents and metadata by creating or running SQL queries"]) + "</p>", None) + peq(SRC("w25", "13", "Q5(d)"), "4 marks", "Describe",
  "A DBMS is used to maintain and manage the database. Describe two ways in which the DBMS can be used to ensure the security of the customer data.", "Method plus description, twice.",
  "<p>One mark for each method and one for its description, twice: " + mks(["Authentication (passwords, biometrics, two-factor): prevents unauthorised access to the customer data", "Access rights or privileges: only those with the right permissions can read or edit the data", "Regular back-ups: a second copy of the data is available in case of loss or damage", "Encryption: the data cannot be understood by anyone who gains unauthorised access", "Views: not everyone can see the customer data"]) + "</p>", None) + peq(SRC("s26", "12", "Q3(c)"), "5 marks", "Complete",
  "Complete the description by writing the missing words. The ... stores data about the data in the database: the table names, field names and relationships, and two other examples of data. When designing a database, the ... schema is the design independent of any DBMS. A DBMS provides security: ... are used to give user accounts permission to read, or read and write. When creating a database, a ... provides tools to create forms and reports.", "Data dictionary with two examples; logical; access rights; developer interface.",
  "<p>" + mks(["data dictionary, with two other examples such as data types, type of validation, primary key or foreign key (the examples are one mark)", "logical", "access rights", "developer interface"]) + "</p>", "Giving 'table names' or 'field names' as the two examples. They are given in the question.")

review = req("2 marks", "Describe", "Describe what a view is and why a school uses one for teachers.", "Part of the database.", "<p>" + mks(["A view shows a user only part of the database", "so each teacher can only see their own classes' data"]) + "</p>", None) + req("3 marks", "Explain", "Explain how record locking prevents lost updates when two clerks edit the same customer record.", "One at a time.", "<p>" + mks(["The DBMS locks the record while the first clerk is editing it", "the second clerk cannot change it at the same time", "so the first update is not overwritten"]) + "</p>", None) + req("2 marks", "State", "State two items stored in a data dictionary.", "Metadata.", "<p>" + mks(["Table and field names", "Data types, validation rules, keys or relationships"]) + "</p>", None) + req("2 marks", "Describe", "Describe the purpose of a query processor.", "Criteria, search, results.", "<p>" + mks(["It takes the criteria entered by the user and finds the data that matches", "and organises the results for display"]) + "</p>", None) + req("2 marks", "Explain", "Explain why a DBMS takes regular back-ups.", "Recovery.", "<p>" + mks(["So the database can be restored if it is lost, damaged or corrupted", "copies stored off site protect against a disaster at the main site"]) + "</p>", None)

tips = tips_html([
  ("Data dictionary: metadata.", "Names, types, rules, keys."),
  ("Logical schema: the design.", "E-R diagram; independent of any DBMS."),
  ("Query processor: criteria to results.", "Search and organise."),
  ("Developer interface: build things.", "Tables, forms, reports, queries."),
  ("Security: method plus how.", "Access rights so only permitted users..."),
  ("Integrity: validation, referential integrity.", "Not the same as security."),
], [("metadata", "Data about the data."), ("a view", "The part of a database a user is allowed to see."), ("record locking", "Stopping two users changing the same record at once."), ("a logical schema", "A model of the database independent of the DBMS.")],
  [("State", "Short answer."), ("Describe", "Several points."), ("Explain", "Reasons as well."), ("Complete", "Fill in the missing terms.")]) + FC

js = AKJS + AK20JS + r'''
(function () {
  const draw = (s) => { const k = Math.round(s.i); const B = (x, t, on) => SV.rect(x, 40, 110, 44, on ? "f3" : "cell", { rx: 8 }) + SV.text(x + 55, 67, t, "lbl bd", { "text-anchor": "middle", style: "font-size:11px" }); let o = B(10, "user criteria", k >= 0) + B(140, "query processor", k >= 1) + B(270, "tables", k >= 2) + B(400, "results shown", k >= 4) + SV.path("M120,62 H140", "ax") + SV.path("M250,62 H270", "ax") + SV.path("M380,62 H400", "ax"); return o; };
  Lib.stepper($("#stA"), { w: 530, h: 110, label: "Query", base: { i: 0 }, draw, tween: 100, dwell: 2400, steps: ["The user enters criteria.", "The <b>query processor</b> reads them.", "It searches the tables for matching data.", "It organises the results.", "The results are displayed."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const rows = [["Ann", "Shop 1", "£500"], ["Bob", "Shop 2", "£700"], ["Cy", "Shop 1", "£300"]]; let o = SV.text(20, 20, k === 0 ? "Owner sees all rows" : "Manager of Shop 1 sees a view", "lbl bd", { style: "font-size:13px" }); rows.forEach((r, i) => { const show = k === 0 || r[1] === "Shop 1"; o += SV.rect(20, 30 + i * 30, 360, 24, show ? "f1" : "cell", { rx: 4, ...(show ? {} : op(0.3)) }) + (show ? SV.text(30, 47 + i * 30, r.join("   "), "lbl", { style: "font-size:12px" }) : ""); }); return o; };
  Lib.stepper($("#stB"), { w: 420, h: 130, label: "Views", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: ["The owner has full access to every row.", "A <b>view</b> and access rights show the Shop 1 manager only the rows they need."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.rect(20, 40, 120, 40, "cell", { rx: 6 }) + SV.text(80, 65, "User A", "lbl bd", { "text-anchor": "middle" }) + SV.rect(20, 100, 120, 40, "cell", { rx: 6 }) + SV.text(80, 125, "User B", "lbl bd", { "text-anchor": "middle" }) + SV.rect(260, 70, 160, 40, k >= 1 ? "f2" : "f1", { rx: 6 }) + SV.text(340, 95, k >= 1 ? "record locked" : "record", "lbl bd", { "text-anchor": "middle" });
    if (k >= 1) o += SV.path("M140,60 L260,85", "ax"); if (k >= 2) o += SV.text(150, 128, "waits for the lock", "sm"); if (k >= 3) o += SV.path("M140,120 L260,100", "ax") + SV.text(340, 135, "A's update saved first", "sm", { "text-anchor": "middle" }); return o; };
  Lib.stepper($("#stC"), { w: 460, h: 150, label: "Locking", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: ["Two users want to edit the same record.", "User A opens it: the DBMS <b>locks</b> the record.", "User B has to wait.", "A saves, the lock is released, then B can edit: no update is lost."].map((c, i) => ({ cap: c, s: { i } })) });
})();
btnTable("aB", "aO", [
  ["Owner", "Full access: read, write, delete all tables", "Administrator"],
  ["Manager of one shop", "Read and write for own shop through a view", "Sees only their shops"],
  ["Till operator", "Add new sales only", "Cannot see other data"],
  ["Student visitor", "No access", "Not authorised"]
], ["User", "Allowed", "Why"]);
btnTable("tB", "tO", [
  ["Where are the field names and data types stored?", "Data dictionary", "Metadata"],
  ["Which tool shows the structure as an E-R diagram?", "Logical schema", "Independent of the DBMS"],
  ["Which tool finds the matching rows for a search?", "Query processor", "Criteria in, results out"],
  ["Which tool lets me build a data entry form?", "Developer interface", "Forms, reports, tables"]
], ["Question", "Tool", "Why"]);
btnTable("sB", "sO", [
  ["Only some staff can edit customer data", "Access rights", "Different permissions"],
  ["Managers see only their own shop's rows", "Views", "Part of the database"],
  ["Data stays unreadable if stolen", "Encryption", "Cipher text"],
  ["Data restored after a server failure", "Back-up and recovery", "Copies"],
  ["Two edits at once do not overwrite each other", "Record locking", "One at a time"]
], ["Need", "Method", "Why"]);
''' + _prjs

finish("as-8-2-database-management-systems", "as82", "Database Management Systems",
  "The DBMS tools (data dictionary, logical schema, query processor and developer interface), and how a DBMS provides security and supports integrity, with animations, labs and the real Paper 1 questions from 2021 to 2026.",
  "8.2", "8 · Databases", "section 8.2 Database management systems (DBMS)", learn, watch, explore, _pr, real, where, past, review,
  "Part 1 is real 9618 questions on database management systems (Paper 1), 2021 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", tips, js)
