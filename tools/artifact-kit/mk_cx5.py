"""IGCSE CS exam technique 5: logic gates, truth tables and databases (Paper 2). Run: python3 tools/artifact-kit/mk_cx5.py"""
import itertools
from csk import *


def tt(n, f):
    return [(b, int(f(*b))) for b in itertools.product([0, 1], repeat=n)]


def outs(n, f):
    return ", ".join(str(o) for _, o in tt(n, f))


def ttable(names, out, f, extra=()):
    """Static truth table HTML. extra: list of (heading, function) intermediate columns."""
    rows = []
    for b, o in tt(len(names), f):
        rows.append(list(b) + [fx(*b) and 1 or 0 for _, fx in extra] + [o])
    return table(names + [h for h, _ in extra] + [out], rows, "t mx")


G2 = lambda f: [f(0, 0), f(0, 1), f(1, 0), f(1, 1)]
GATES = [("NOT", "A single input; the output is the opposite", lambda a, b=0: 1 - a),
         ("AND", "1 only when both inputs are 1", lambda a, b: a & b), ("OR", "1 when at least one input is 1", lambda a, b: a | b),
         ("NAND", "NOT AND: 0 only when both inputs are 1", lambda a, b: 1 - (a & b)), ("NOR", "NOT OR: 1 only when both inputs are 0", lambda a, b: 1 - (a | b)),
         ("XOR", "1 when the inputs are different", lambda a, b: a ^ b)]
gate_rows = []
for n, d, f in GATES:
    if n == "NOT":
        gate_rows.append((f"<b>{n}</b>", d, "A=0: 1 · A=1: 0"))
    else:
        o = G2(f)
        gate_rows.append((f"<b>{n}</b>", d, f"00: {o[0]} · 01: {o[1]} · 10: {o[2]} · 11: {o[3]}"))

# worked table for X = (NOT P OR Q) NAND (Q XOR R)
WK = ttable(["P", "Q", "R"], "X", lambda p, q, r: 1 - (((1 - p) | q) & (q ^ r)), [("NOT P", lambda p, q, r: 1 - p), ("NOT P OR Q", lambda p, q, r: (1 - p) | q), ("Q XOR R", lambda p, q, r: q ^ r)])

learn = '''
  <div class="card big"><h3>This part in five sentences</h3>
  <p>Logic gates, truth tables and a single-table database together made about <b>16 to 17 of the 75 marks</b> in the Oct/Nov 2024 versions of Paper 2 that this review draws on, and almost every one of those marks is <b>exact</b>: a symbol is right or wrong, a truth table output is 0 or 1, an SQL output either matches the table or does not. For logic, you work <b>one gate at a time</b>: write an expression from a circuit by naming each gate's output, complete a truth table with a working column for each gate, and draw a circuit gate by gate without simplifying. A four-mark truth table is marked by the number of correct outputs, so one slip costs a mark rather than all of them, and the examiner reports say tables are usually answered well. For databases, know the words (field, record, primary key, data type), and read an SQL statement in the order the computer does: <b>FROM, WHERE, ORDER BY, then SELECT</b>. The output of a query is the selected columns of the matching rows, written without extra punctuation, in the order of the table or the ORDER BY.</p></div>

  <h2>1 · The six gates</h2>
  <p>Every gate except NOT has two inputs. The syllabus says logic circuits have a maximum of three inputs and one output, and that circuits must be drawn for the statement given, without simplification.</p>
''' + table(["Gate", "Rule", "Output for the input pairs"], gate_rows) + '''
  <h2>2 · Expressions: write one from a circuit</h2>
  <p>Work from the left. Name the output of each gate, then combine. The mark scheme for a three-input circuit gave one mark for each gate or part and one for the whole expression: for a circuit with a NOT gate, an XOR gate and an OR gate, the points were <i>NOT X</i>, <i>Y XOR Z</i> and <i>NOT X OR (Y XOR Z)</i>.</p>
  <div class="tw"><table class="t">
    <tr><th>Do</th><th>Do not</th></tr>
    <tr><td>Write NOT first: <code>NOT X</code></td><td>Write <code>X NOT</code>. The Oct/Nov 2024 report says some candidates reversed the notation.</td></tr>
    <tr><td>Use brackets to show what feeds each gate: <code>NOT X OR (Y XOR Z)</code></td><td>Leave out brackets so the order is unclear</td></tr>
    <tr><td>Write the expression as it appears: no simplifying</td><td>Rewrite it in a shorter form: the question says do not simplify</td></tr>
    <tr><td>Use the gate names AND, OR, NOT, NAND, NOR, XOR</td><td>Use symbols such as + or ·</td></tr>
  </table></div>

  <h2>3 · Truth tables</h2>
  <ul>
    <li><b>Rows in binary order:</b> for three inputs, 000, 001, 010, 011, 100, 101, 110, 111. Eight rows.</li>
    <li><b>Use the working space.</b> Add a column for each gate in the order you worked it out. A slip is then easy to find.</li>
    <li><b>Do the NAND or NOR last.</b> The Feb/March 2025 report notes a common error: the final output column was the exact opposite of the correct answer. A missed final NOT in a NAND or NOR would cause exactly this, so work out the AND or OR first and then reverse it.</li>
  </ul>
  <p>The expression <i>X = (NOT P OR Q) NAND (Q XOR R)</i> from Oct/Nov 2024 paper 22, with a working column for each gate:</p>
''' + WK + '''
  <p>The mark scheme for a four-mark table is by the number of correct outputs.</p>
  <div class="tw"><table class="t">
    <tr><th>Correct outputs (of 8)</th><th>8</th><th>6 or 7</th><th>4 or 5</th><th>2 or 3</th><th>0 or 1</th></tr>
    <tr><td><b>Marks</b></td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr>
  </table></div>

  <h2>4 · Drawing a circuit from an expression</h2>
  <ol>
    <li><b>Find the innermost brackets.</b> In <i>(NOT P OR Q) NAND (Q XOR R)</i> there are three: NOT P, then OR with Q, then Q XOR R.</li>
    <li><b>Draw one gate for each operator.</b> Three gates have two inputs; NOT has one. Each gate may have at most two inputs.</li>
    <li><b>Connect the outputs</b> of the first gates to the final gate (NAND).</li>
    <li><b>Label the inputs and the output.</b></li>
    <li><b>Do not simplify.</b> The Feb/March 2025 report says candidates who built the circuit directly from the expression, without changing any gates, generally achieved the best marks.</li>
  </ol>
  <p>The mark scheme gives one mark for each correct gate with its correct inputs.</p>

  <h2>5 · Database words</h2>
  <div class="tw"><table class="t">
    <tr><th>Word</th><th>Meaning</th><th>Careful</th></tr>
    <tr><td><b>Table</b></td><td>The whole set of data about one kind of thing</td><td></td></tr>
    <tr><td><b>Field</b></td><td>One column: one kind of data, such as Price</td><td>The reports say some candidates reversed the number of fields and records</td></tr>
    <tr><td><b>Record</b></td><td>One row: all the data about one item</td><td>Count the rows of data, not the heading row</td></tr>
    <tr><td><b>Primary key</b></td><td>A field whose values are unique, so each record can be identified</td><td>Reason: it is a unique identifier. A field with repeated values, such as Type, cannot be the key.</td></tr>
    <tr><td><b>Data type</b></td><td>Text or alphanumeric, character, Boolean, integer, real, date and time</td><td>Choose by what is stored, not by how it looks</td></tr>
  </table></div>
  <div class="tw"><table class="t">
    <tr><th>Data stored</th><th>Type</th><th>Why</th></tr>
    <tr><td>A code such as MD1234, a name, a title</td><td>Text or alphanumeric</td><td>Letters and digits</td></tr>
    <tr><td>A single grade letter</td><td>Character</td><td>One character</td></tr>
    <tr><td>Yes or no, in stock or not, painted or not</td><td>Boolean</td><td>Two values</td></tr>
    <tr><td>Number in stock, number of guests</td><td>Integer</td><td>Whole numbers</td></tr>
    <tr><td>A price such as 7.40, a weight such as 20.5</td><td>Real</td><td>Has a fractional part</td></tr>
    <tr><td>The date a song was recorded</td><td>Date/time</td><td>A date</td></tr>
  </table></div>

  <h2>6 · Reading and writing SQL</h2>
  <p>The syllabus limits SQL to SELECT, FROM, WHERE, ORDER BY (ascending or descending), SUM, COUNT, AND and OR, in a single table.</p>
  <div class="tw"><table class="t">
    <tr><th>Keyword</th><th>What it does</th></tr>
    <tr><td><code>SELECT</code></td><td>Lists the fields to display</td></tr>
    <tr><td><code>FROM</code></td><td>Names the table</td></tr>
    <tr><td><code>WHERE</code></td><td>Gives the search condition</td></tr>
    <tr><td><code>ORDER BY</code></td><td>Sorts the rows: ascending by default, or descending</td></tr>
    <tr><td><code>SUM</code>, <code>COUNT</code></td><td>Adds the values of a field, or counts the records</td></tr>
  </table></div>
  <h3>Giving the output of an SQL statement</h3>
  <ol>
    <li><b>FROM:</b> find the table.</li>
    <li><b>WHERE:</b> mark the rows that meet the condition.</li>
    <li><b>ORDER BY:</b> put those rows in order, if asked.</li>
    <li><b>SELECT:</b> write only the fields listed, in the order listed.</li>
    <li><b>Copy the data exactly</b>, with no punctuation added. The Oct/Nov 2024 report says punctuation should not be in the output of an SQL statement.</li>
  </ol>
  <p>A 3-mark output question in Oct/Nov 2024 had one mark for data from the four correct columns (any rows, any order), one for the rows being in the order of the table, with at least two rows and two columns, and one for all the data correct with no extra content. The report says candidates who copied the data from the table in the same order as it appeared got all three marks.</p>
  <h3>Completing an SQL statement</h3>
  <p>A question asked for the names of the cheeses out of stock. The accepted answer was <code>SELECT Name FROM CheeseStock WHERE NOT InStock</code>, or <code>InStock = FALSE</code> or <code>No</code>, or <code>WeightKg = 0.0</code>. The follow-up part asked how one line could change to show the same information, and the mark scheme accepted checking either the Boolean field or the weight field, so <b>name the other field and the value you would test</b>. The report says a minority did so and some gave no reason.</p>
  <h3>Explaining what SQL does</h3>
  <p>For <code>SUM(Minutes) FROM Songs WHERE Genre = "rock"</code> and <code>COUNT(Title) …</code> the mark scheme gave one mark each for: finding the total number of minutes of music, finding the total number of songs, and "available for the genre rock". Say what is added or counted, and which records.</p>

  <h2>7 · Common ways to lose marks</h2>
  <ul>
    <li><b>Writing the NOT after the input</b>, or simplifying the expression.</li>
    <li><b>The last column opposite to the right answer</b>, from missing the final NOT in NAND or NOR.</li>
    <li><b>Adding extra gates</b> to the circuit or giving a gate three inputs.</li>
    <li><b>Counting the heading row as a record</b>, or swapping fields and records.</li>
    <li><b>Choosing a field with repeated values as the primary key.</b></li>
    <li><b>Adding commas, brackets or the headings</b> to the output of an SQL statement.</li>
    <li><b>Writing the columns in the table's order</b> instead of the SELECT order.</li>
    <li><b>Changing the WHERE line without naming a field and a value</b> when asked how it could be changed.</li>
  </ul>
'''

watch = '''
  <h2>1 · Building a circuit gate by gate</h2>
  <p>Press Play, or click the numbered steps. The circuit is X = (NOT P OR Q) NAND (Q XOR R).</p>
  <div id="stA"></div>
  <h2>2 · Filling in the truth table</h2>
  <div id="stB"></div>
  <h2>3 · Reading an SQL statement</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Three circuits, their expressions and truth tables</h2>
  <p>Choose a circuit to see the expression and the completed truth table. Each is one of the real circuits from the Oct/Nov 2023 and 2024 papers.</p>
  <div class="card"><div id="ciB" class="btnrow"></div><div id="ciO"></div></div>

  <h2>Lab 2 · Marks for a truth table</h2>
  <p>Choose how many of the eight outputs are right to see the marks on the four-mark scale.</p>
  <div class="card"><div class="grid2"><div><div id="g1"></div>
    <div class="readout"><div><small>Correct outputs</small><strong id="r1"></strong></div><div><small>Marks (out of 4)</small><strong id="r2"></strong></div></div>
    <div class="verdict" id="rv"></div></div>
    <div><svg id="labA" viewBox="0 0 420 200" role="img" aria-label="Marks for the number of correct outputs"></svg></div></div></div>

  <h2>Lab 3 · Run an SQL query</h2>
  <p>Choose a query to see which rows match, and the output you would write. The table is our own InstrumentStock.</p>
  <div class="card"><div id="sqB" class="btnrow"></div><div id="sqO"></div></div>
'''

practise = '''
  <h2>1 · Which gate is it?</h2><div id="cl1" class="card"></div>
  <h2>2 · Which data type?</h2><div id="cl2" class="card"></div>
  <h2>3 · Put the reading of an SQL statement in order</h2><div id="o1" class="card"></div>
  <h2>4 · Match the SQL keyword to its job</h2><div id="m1" class="card"></div>
  <h2>5 · Calculations</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = '<p class="note">These come from the Principal Examiner Reports for Cambridge IGCSE Computer Science, which describe what candidates actually wrote. The wording is ours.</p>\n' + (
rw("NOT written after the input", "Oct/Nov 2024, paper 21: many candidates produced the correct Boolean expression, but some reversed the notation for NOT X as X NOT. The mark scheme gives marks for the NOT part and for the whole expression.", "write NOT first, then the input.") +
rw("The final column the wrong way round", "Feb/March 2025, paper 22: the majority of candidates scored at least one mark on the truth table and many scored high marks, but a common error was that the final output column was the exact opposite of the correct answer.", "after the last gate, check whether it is NAND or NOR and that its final NOT has been applied.") +
rw("Building the circuit directly", "Feb/March 2025, paper 22: candidates who drew the circuit straight from the given expression, without simplifying or altering any gate, generally scored best. The question says not to simplify.", "one gate for each operator, in the order of the brackets.") +
rw("Fields and records the wrong way round", "Oct/Nov 2024, paper 22: most candidates stated 11 fields and 15 records, but a small number reversed the two values.", "fields are the columns; records are the rows.") +
rw("Punctuation in the SQL output", "Oct/Nov 2024, papers 21 and 22: the most common error in giving the output of an SQL statement was extra data such as punctuation marks. Candidates who copied the data from the table in the same order scored all three marks.", "write the values as they appear in the table, one record per line.") +
rw("Another field with no reason", "Oct/Nov 2024, paper 21: a minority of candidates identified another field that could have been used in the WHERE line, and some gave no explanation. The mark scheme accepted the Boolean InStock field set to FALSE, or the weight field set to 0.0.", "name the field and the value, and say that it picks out the same records.")
)

items = [("w24_21", "7", 7), ("w24_22", "9", 8), ("w23_21", "7", 8), ("w24_21", "10", 10), ("w24_22", "11", 8), ("w23_21", "9", 10), ("s23_22", "10(c)", 3), ("w24_23", "11", 7)]

PLANTS = [("PL01", "Aster", "Yes", "GRO", 3.50, 40), ("PL02", "Begonia", "Yes", "GRO", 4.25, 18), ("PL03", "Camellia", "No", "ORN", 12.00, 0), ("PL04", "Daisy", "Yes", "GRO", 2.75, 60), ("PL05", "Fuchsia", "No", "SUN", 6.50, 0),
          ("PL06", "Geranium", "Yes", "SUN", 5.00, 25), ("PL07", "Hosta", "Yes", "ORN", 8.75, 9), ("PL08", "Iris", "No", "GRO", 4.00, 0)]
_gro = [f"{r[0]} {r[5]}" for r in PLANTS if r[3] == "ORN"]
plant_tbl = table(["PlantNo", "Name", "InStock", "SupplierCode", "PricePerPlant", "Quantity"], [(r[0], r[1], r[2], r[3], f"{r[4]:.2f}", r[5]) for r in PLANTS])
KIT = [("K01", "Microscope", 4, 120.00, "T", "T", "F"), ("K02", "Balance", 6, 85.50, "T", "F", "T"), ("K03", "Microscope", 2, 150.00, "F", "T", "T"), ("K04", "Burner", 8, 12.75, "T", "T", "T"), ("K05", "Balance", 3, 99.00, "F", "F", "T")]
kit_tbl = table(["ItemNo", "Type", "Capacity", "Cost", "Mon", "Tue", "Wed"], [(r[0], r[1], r[2], f"{r[3]:.2f}", r[4], r[5], r[6]) for r in KIT])
kit_out = [f"{r[0]} {r[1]} {r[2]} {r[3]:.2f}" for r in KIT if r[4] == "F"]
fx = lambda a, b, c: (1 - b) | ((a ^ c))
fy = lambda p, q, r: 1 - ((p & (1 - q)) | (q ^ r))
fz = lambda a, b, c: (a | (1 - b)) & c

exam = cs_exam("logic and databases",
  "Eight questions on logic circuits, truth tables and single-table databases. The circuits, tables and data are our own versions of the originals, with the same structure and marking, and the outputs have been recalculated. Do the question on paper first, then check against the points.",
  crows(items), [
  ceq(CP("w24_21", "7"), "[7]", "A logic circuit has inputs A, B and C. Input B passes through a NOT gate. Inputs A and C go into an XOR gate. The outputs of the NOT gate and the XOR gate go into an OR gate whose output is S. (a) Write a logic expression for the circuit. Do not simplify it. (b) Complete the truth table for the circuit.",
    ["(a) Three marks: NOT B; A XOR C; and the whole expression correct: S = NOT B OR (A XOR C)", "(b) Four marks by the number of correct outputs: 8 correct = 4, 6 or 7 = 3, 4 or 5 = 2, 2 or 3 = 1", "Outputs for ABC = 000 to 111 in order: " + outs(3, fx), "The report says some candidates wrote NOT B as B NOT"],
    "<p>Name each gate's output, then combine. For (b) add working columns for NOT B and A XOR C, then OR them.</p>" + ttable(["A", "B", "C"], "S", fx, [("NOT B", lambda a, b, c: 1 - b), ("A XOR C", lambda a, b, c: a ^ c)])),
  ceq(CP("w24_22", "9"), "[8]", "Consider the logic expression X = (P AND NOT Q) NOR (Q XOR R). (a) Draw a logic circuit for the expression. Each gate has a maximum of two inputs. Do not simplify. (b) Complete the truth table.",
    ["(a) Four marks, one for each correct gate with the correct inputs: NOT on Q; AND with inputs P and NOT Q; XOR with inputs Q and R; NOR with the outputs of the AND and the XOR as inputs, giving X", "(b) Four marks by the number of correct outputs", "Outputs for PQR = 000 to 111 in order: " + outs(3, fy), "The report says candidates who built the circuit directly from the expression did best, and that a common error was a final column the exact opposite of the right answer"],
    "<p>Innermost brackets first: NOT Q, then AND, then XOR, then NOR. The NOR is the last gate, so apply its negation last.</p>" + ttable(["P", "Q", "R"], "X", fy, [("NOT Q", lambda p, q, r: 1 - q), ("P AND NOT Q", lambda p, q, r: p & (1 - q)), ("Q XOR R", lambda p, q, r: q ^ r)])),
  ceq(CP("w23_21", "7"), "[8]", "A logic circuit has inputs A, B and C. Input B passes through a NOT gate. The output of the NOT gate and input A go into an OR gate. The output of the OR gate and input C go into an AND gate, whose output is X. (a) Write a logic expression for the circuit. Do not simplify it. (b) Complete the truth table.",
    ["(a) Four marks in the original: one for each part, such as NOT B, A OR NOT B, the AND with C, and the whole expression correct: X = (A OR NOT B) AND C", "(b) Four marks by the number of correct outputs", "Outputs for ABC = 000 to 111 in order: " + outs(3, fz)],
    "<p>Write each gate's output: NOT B, then A OR NOT B, then AND C. Use brackets around the OR part.</p>" + ttable(["A", "B", "C"], "X", fz, [("NOT B", lambda a, b, c: 1 - b), ("A OR NOT B", lambda a, b, c: a | (1 - b))])),
  ceq(CP("w24_21", "10"), "[10]", "A garden centre stores details of plants in the table PlantStock.<br>" + plant_tbl + "(a) State the number of records. (b) Give the field that would be the primary key and state why. (c) Write the output from: SELECT PlantNo, Quantity FROM PlantStock WHERE SupplierCode = \"ORN\"; (d) (i) Complete an SQL statement to display only the names of the plants that are out of stock. (ii) Explain how one line of your statement could be changed to display the same information.",
    ["(a) 8 (1 mark)", "(b) PlantNo (1); a unique identifier, so each record can be identified (1)", "(c) Two marks, one for each record with supplier ORN: " + "; ".join(_gro) + " (no punctuation, in table order)", "(d)(i) Three marks: SELECT Name; FROM PlantStock; WHERE NOT InStock (or InStock = No, or InStock = FALSE, or Quantity = 0)", "(d)(ii) Two marks: the WHERE line could check the InStock field for No or FALSE, or check the Quantity field for 0"],
    "<p>For (c) filter first, then write only the two fields. For (d)(ii) name the other field and the value: Quantity = 0 picks out the same plants as InStock = No.</p>"),
  ceq(CP("w24_22", "11"), "[8]", "The table LabKit stores equipment and the days it is booked.<br>" + kit_tbl + "(a) State the number of fields and the number of records. (b) State why Type cannot be the primary key. (c) Give a field with each data type: alphanumeric, Boolean, real, integer. (d) Give the output of: SELECT ItemNo, Type, Capacity, Cost FROM LabKit WHERE Mon = F;",
    ["(a) Fields 7, records 5 (two marks, one for each)", "(b) The Type field contains repeated data, so it is not unique (1 mark)", "(c) Two marks for four correct fields, one for two or three: for example ItemNo or Type (alphanumeric); Mon, Tue or Wed (Boolean); Cost (real); Capacity (integer)", "(d) Three marks: data from the four correct columns (any rows, any order); rows in the order shown, with at least two rows and two columns; all data correct with no extra content: " + "; ".join(kit_out)],
    "<p>Count rows of data for records and columns for fields. For (d) the four columns come from SELECT; the rows come from WHERE.</p>"),
  ceq(CP("w23_21", "9"), "[10]", "A school library stores: book code, for example LB204; title; number of copies available, for example 3; price, for example 8.50; and whether the book is a hardback, yes or no. (a) Give a suitable field name and data type for each of the five fields. (b) Give the field for the primary key and state why. (c) State what the SQL commands SELECT, FROM and WHERE are used for.",
    ["(a) Five marks, one for each appropriate field name with its data type: BookCode text or alphanumeric; Title text; Copies integer; Price real; Hardback Boolean", "(b) BookCode (1); a unique identifier (1)", "(c) Three marks: SELECT lists the fields to be displayed; FROM identifies the table; WHERE identifies the search criteria"],
    "<p>Choose the type from what is stored: a code and a title are text, a count is an integer, a price is real, yes or no is Boolean.</p>"),
  ceq(CP("s23_22", "10(c)"), "[3]", "Explain the purpose of these SQL statements: SELECT SUM(Pages) FROM Books WHERE Genre = \"history\"; and SELECT COUNT(Title) FROM Books WHERE Genre = \"history\";",
    ["One mark for each point: to find the total number of pages", "To find the total number of books", "Available (only) for the genre history"],
    "<p>Say what is added (the pages), what is counted (the books), and which records (the history ones).</p>"),
  ceq(CP("w24_23", "11"), "[7]", "The table MusicStock has fields ItemNo, Name, InStock (Yes or No), Weight, PricePerItem and Quantity, with these records: M1 Drum Yes 5 40.00 7; M2 Cymbal Yes 5 60.50 3; M3 Snare No 5 35.00 0; M4 Triangle Yes 1 12.00 20. (a) Write the output of SELECT ItemNo, Name FROM MusicStock WHERE Weight = 5 ORDER BY PricePerItem; (b) (i) Complete an SQL statement to display only the names of the items that are out of stock. (ii) Explain how another SQL statement using a different field could display the same information.",
    ["(a) Three marks: one for each correct line, maximum two, and one for the order of the lines. Weight 5 gives M1, M2 and M3; ordered by price, lowest first: M3 Snare; M1 Drum; M2 Cymbal", "(b)(i) Two marks: SELECT Name; FROM MusicStock; WHERE NOT InStock (or InStock = No, or Quantity = 0)", "(b)(ii) Two marks for either point: the WHERE clause can check the InStock field for FALSE or No (1) …", "… or the WHERE clause can check the Quantity field (1) for 0 (1)"],
    "<p>Order by the price, lowest first: 35.00, 40.00, 60.50. ORDER BY changes the order of the rows but SELECT still controls the columns. For (ii) name the other field and the value.</p>"),
])

tips = tips_html(
  [("Work one gate at a time.", "Name each gate's output."),
   ("NOT goes first.", "NOT X, never X NOT."),
   ("Add working columns.", "Do the NAND or NOR last."),
   ("Do not simplify.", "One gate per operator."),
   ("FROM, WHERE, ORDER BY, SELECT.", "That is the order to read a query."),
   ("Copy the data exactly.", "No punctuation, table order."),
   ("Rows are records, columns are fields.", "Do not count the heading.")],
  [("A logic expression", "S = NOT B OR (A XOR C)"),
   ("A reason for the primary key", "It is a unique identifier, so every record can be identified."),
   ("Another field in WHERE", "The WHERE clause could test the Quantity field for 0, which selects the same plants."),
   ("The purpose of SELECT", "SELECT lists the fields to display."),
   ("The purpose of SUM", "It finds the total of the values in the field for the records that match.")],
  [("State", "A clear statement, such as a number of records."), ("Give", "The name of a field or a value."), ("Write", "The expression, statement or output."), ("Complete", "Fill in the table, circuit or statement."), ("Draw", "A circuit with standard symbols."), ("Explain", "The purpose or the reason.")]) + FC

js = CHAINJS + PICKJS + TTJS + '''
/* ---- gate symbols and circuits ---- */
const GW = 56, GH = 44;
function gateSvg(t, x, y, v = 1) {
  const m = y + GH / 2, st = `fill:var(--soft);stroke:var(--ink);stroke-width:2;opacity:${v}`, ns = `fill:none;stroke:var(--ink);stroke-width:2;opacity:${v}`;
  let d, out = x + GW, extra = "";
  if (t === "AND" || t === "NAND") d = `M${x},${y} L${x + GW / 2},${y} A${GW / 2},${GH / 2} 0 0 1 ${x + GW / 2},${y + GH} L${x},${y + GH} Z`;
  else if (t === "NOT") d = `M${x},${y} L${x + GW - 9},${m} L${x},${y + GH} Z`;
  else d = `M${x},${y} Q${x + GW * 0.5},${y} ${x + GW},${m} Q${x + GW * 0.5},${y + GH} ${x},${y + GH} Q${x + GW * 0.3},${m} ${x},${y} Z`;
  if (t === "XOR") extra += `<path d="M${x - 8},${y} Q${x + GW * 0.3 - 8},${m} ${x - 8},${y + GH}" style="${ns}"/>`;
  if (t === "NAND" || t === "NOR" || t === "NOT") { const cx = t === "NOT" ? x + GW - 4 : x + GW + 5; extra += `<circle cx="${cx}" cy="${m}" r="5" style="fill:var(--surface);stroke:var(--ink);stroke-width:2;opacity:${v}"/>`; out = cx + 5; }
  return { t, svg: `<path d="${d}" style="${st}"/>${extra}` + SV.text(x + GW / 2, y + GH + 15, t, "sm", { "text-anchor": "middle", ...op(v) }), out: [out, m], in1: [x, t === "NOT" ? m : y + GH * 0.27], in2: [x, y + GH * 0.73] };
}
const wire = (pts, v = 1) => `<polyline points="${pts.map((p) => p.join(",")).join(" ")}" style="fill:none;stroke:var(--ink);stroke-width:2;opacity:${v}"/>`;
const dot = (x, y, v = 1) => `<circle cx="${x}" cy="${y}" r="3.5" style="fill:var(--ink);opacity:${v}"/>`;
function circuit(id) {
  const g = (t, x, y) => gateSvg(t, x, y);
  if (id === 1) {
    const n = g("NOT", 110, 18), o = g("OR", 235, 50), x = g("XOR", 235, 130), a = g("NAND", 370, 90);
    return { w: 540, h: 215, ins: [["P", 40], ["Q", 100], ["R", 170]], out: "X", parts: [n, o, x, a], dots: [[190, 100]], wires: [
      { p: [[50, 40], n.in1], need: [0] }, { p: [n.out, [205, n.out[1]], [205, o.in1[1]], o.in1], need: [0, 1] },
      { p: [[50, 100], [190, 100]], any: [1, 2] }, { p: [[190, 100], [210, 100], [210, o.in2[1]], o.in2], need: [1] }, { p: [[190, 100], [190, x.in1[1]], x.in1], need: [2] },
      { p: [[50, 170], [215, 170], [215, x.in2[1]], x.in2], need: [2] }, { p: [o.out, [335, o.out[1]], [335, a.in1[1]], a.in1], need: [1, 3] }, { p: [x.out, [350, x.out[1]], [350, a.in2[1]], a.in2], need: [2, 3] }, { p: [a.out, [500, a.out[1]]], need: [3] }],
      f: (p, q, r) => 1 - (((1 - p) | q) & (q ^ r)), names: ["P", "Q", "R"], expr: "X = (NOT P OR Q) NAND (Q XOR R)", src: "Oct/Nov 2024, paper 22, Q9" };
  }
  if (id === 2) {
    const n = g("NOT", 110, 18), x = g("XOR", 110, 125), o = g("OR", 260, 70);
    return { w: 480, h: 215, ins: [["X", 40], ["Y", 110], ["Z", 170]], out: "W", parts: [n, x, o], dots: [], wires: [
      { p: [[50, 40], n.in1], need: [0] }, { p: [n.out, [225, n.out[1]], [225, o.in1[1]], o.in1], need: [0, 2] }, { p: [[50, 110], [90, 110], [90, x.in1[1]], x.in1], need: [1] },
      { p: [[50, 170], [100, 170], [100, x.in2[1]], x.in2], need: [1] }, { p: [x.out, [235, x.out[1]], [235, o.in2[1]], o.in2], need: [1, 2] }, { p: [o.out, [430, o.out[1]]], need: [2] }],
      f: (x, y, z) => (1 - x) | (y ^ z), names: ["X", "Y", "Z"], expr: "W = NOT X OR (Y XOR Z)", src: "Oct/Nov 2024, paper 21, Q7" };
  }
  const n1 = g("NOT", 100, 18), a = g("AND", 230, 50), n2 = g("NOT", 100, 148), o = g("OR", 370, 100);
  return { w: 520, h: 215, ins: [["A", 40], ["B", 100], ["C", 170]], out: "X", parts: [n1, a, n2, o], dots: [], wires: [
    { p: [[50, 40], n1.in1], need: [0] }, { p: [n1.out, [195, n1.out[1]], [195, a.in1[1]], a.in1], need: [0, 1] }, { p: [[50, 100], [210, 100], [210, a.in2[1]], a.in2], need: [1] },
    { p: [[50, 170], n2.in1], need: [2] }, { p: [a.out, [335, a.out[1]], [335, o.in1[1]], o.in1], need: [1, 3] }, { p: [n2.out, [350, n2.out[1]], [350, o.in2[1]], o.in2], need: [2, 3] }, { p: [o.out, [480, o.out[1]]], need: [3] }],
    f: (a_, b, c) => ((1 - a_) & b) | (1 - c), names: ["A", "B", "C"], expr: "X = (NOT A AND B) OR NOT C", src: "Oct/Nov 2023, paper 21, Q7" };
}
function circuitSvg(c, k) {
  const vis = (i) => i < k; let o = "";
  c.ins.forEach(([n, y]) => (o += SV.text(24, y + 5, n, "lbl bd", { "text-anchor": "middle" })));
  c.parts.forEach((p, i) => { if (vis(i)) o += p.svg; });
  c.wires.forEach((w) => { const ok = w.need ? w.need.every(vis) : w.any.some(vis); if (ok) o += wire(w.p); });
  c.dots.forEach(([x, y]) => { if (vis(1) && vis(2)) o += dot(x, y); });
  if (k >= c.parts.length) o += SV.text(c.wires[c.wires.length - 1].p[1][0] + 12, c.wires[c.wires.length - 1].p[1][1] + 5, c.out, "lbl bd");
  return o;
}
const C1 = circuit(1);
Lib.stepper($("#stA"), { w: C1.w, h: C1.h, label: "Building a circuit for X = (NOT P OR Q) NAND (Q XOR R)", base: { k: 0 }, draw: (s) => circuitSvg(C1, Math.round(s.k)), tween: 200, dwell: 4500, steps: [
  { cap: "<b>Innermost bracket first.</b> NOT P is the first gate: one input, with a small circle on the output.", s: { k: 1 } },
  { cap: "<b>OR gate.</b> Its inputs are the output of the NOT gate and Q. This completes (NOT P OR Q).", s: { k: 2 } },
  { cap: "<b>XOR gate.</b> Its inputs are Q and R. Q has two uses, so its line branches, shown with a dot.", s: { k: 3 } },
  { cap: "<b>NAND gate.</b> It joins the OR output and the XOR output, and gives X. The circle on the output is the NOT of AND.", s: { k: 4 } }
] });

/* ---- truth table stepper ---- */
const TT = { heads: ["P", "Q", "R", "NOT P", "NOT P OR Q", "Q XOR R", "X"], f: [null, null, null, (p) => 1 - p, (p, q) => (1 - p) | q, (p, q, r) => q ^ r, (p, q, r) => 1 - (((1 - p) | q) & (q ^ r))] };
function ttDrawSvg(k) {
  const W = [50, 50, 50, 90, 140, 110, 70], rows = [];
  for (let i = 0; i < 8; i++) rows.push([(i >> 2) & 1, (i >> 1) & 1, i & 1]);
  let o = "", x = 40;
  TT.heads.forEach((h, c) => {
    const v = Math.max(0, Math.min(1, k - c)); if (v > 0) {
      o += SV.rect(x, 12, W[c] - 4, 28, c === 6 ? "f1" : c > 2 ? "f2" : "f3", { rx: 5, ...op(0.5 * v) }) + SV.text(x + (W[c] - 4) / 2, 31, h, "lbl bd", { "text-anchor": "middle", style: "font-size:12.5px", ...op(v) });
      rows.forEach((r, i) => { const val = c < 3 ? r[c] : TT.f[c](...r); o += SV.text(x + (W[c] - 4) / 2, 64 + i * 26, val, "lbl bd", { "text-anchor": "middle", style: "font-size:15px;font-family:var(--mono)" + (c === 6 ? ";fill:var(--accent)" : ""), ...op(v) }); });
    }
    x += W[c];
  });
  return o;
}
Lib.stepper($("#stB"), { w: 640, h: 280, label: "Completing a truth table column by column", base: { k: 0 }, draw: (s) => ttDrawSvg(s.k), tween: 500, dwell: 4500, steps: [
  { cap: "<b>Inputs.</b> Three inputs give eight rows, counted in binary from 000 to 111.", s: { k: 3 } },
  { cap: "<b>NOT P.</b> The first working column: the opposite of P in every row.", s: { k: 4 } },
  { cap: "<b>NOT P OR Q.</b> 1 when NOT P is 1 or Q is 1.", s: { k: 5 } },
  { cap: "<b>Q XOR R.</b> 1 when Q and R are different.", s: { k: 6 } },
  { cap: "<b>X.</b> NAND of the two brackets: 0 only when both brackets are 1. Eight outputs: four marks if all are right.", s: { k: 7 } }
] });

chainStep("#stC", "Reading SELECT Name, Quantity FROM InstrumentStock WHERE SupplierCode = \\"BRS\\" AND InStock ORDER BY Quantity", ["FROM: use the table InstrumentStock", "WHERE: both conditions must be true, so Trumpet and Tuba are kept and Trombone is dropped because it is out of stock", "ORDER BY: put them in order of Quantity, lowest first: Tuba, then Trumpet", "SELECT: show only Name and Quantity, in that order: Tuba 2, then Trumpet 5"], [
  "<b>FROM:</b> find the table.", "<b>WHERE:</b> both conditions must be true for AND. Trombone fails InStock.", "<b>ORDER BY:</b> ascending is the default.", "<b>SELECT:</b> write only these fields, with no punctuation."]);

/* ---- circuits lab ---- */
pick("ci", [1, 2, 3].map((n) => ({ label: "Circuit " + n, c: circuit(n) })), (it) => {
  const c = it.c;
  return `<div class="grid2"><div><svg viewBox="0 0 ${c.w} ${c.h}" role="img" aria-label="${c.expr}" style="max-width:100%">${circuitSvg(c, c.parts.length)}</svg></div><div>${ttHtml(c.names, c.out, c.f)}</div></div><p><code>${c.expr}</code> <small>(${c.src})</small></p>`;
});

function tm() {
  const n = +$("#tc").value, m = n === 8 ? 4 : n >= 6 ? 3 : n >= 4 ? 2 : n >= 2 ? 1 : 0;
  $("#r1").textContent = n + " of 8"; $("#r2").textContent = m;
  $("#rv").textContent = n === 8 ? "All eight right: full marks." : n >= 6 ? "Six or seven right: 3 marks. Check the NAND or NOR last step for the row that is wrong." : n >= 4 ? "Four or five right: 2 marks." : n >= 2 ? "Two or three right: 1 mark. Re-do the working columns." : "Fewer than two right: no mark.";
  let o = ""; for (let i = 0; i < 8; i++) o += SV.rect(30 + i * 46, 100, 38, 38, i < n ? "f3" : "f2", { rx: 6, ...op(0.6) }) + SV.text(49 + i * 46, 125, i < n ? "✓" : "✗", "lbl bd", { "text-anchor": "middle" });
  $("#labA").innerHTML = o + SV.text(210, 80, "Marks: " + m + " out of 4", "lbl bd", { "text-anchor": "middle" });
}
Lib.slider($("#g1"), { id: "tc", label: "Correct outputs ", min: 0, max: 8, step: 1, value: 6, fmt: (v) => v, onInput: tm });
tm();

/* ---- SQL lab ---- */
const IS = [["IN01", "Violin", "Yes", "MUS", 120.00, 14], ["IN02", "Viola", "Yes", "MUS", 135.50, 6], ["IN03", "Cello", "No", "ORC", 310.00, 0], ["IN04", "Flute", "Yes", "WND", 95.00, 22], ["IN05", "Oboe", "No", "WND", 480.00, 0],
  ["IN06", "Clarinet", "Yes", "WND", 150.00, 9], ["IN07", "Trumpet", "Yes", "BRS", 210.00, 5], ["IN08", "Trombone", "No", "BRS", 275.00, 0], ["IN09", "Tuba", "Yes", "BRS", 640.00, 2], ["IN10", "Piccolo", "Yes", "WND", 88.50, 11]];
const COLS = ["ItemNo", "Name", "InStock", "SupplierCode", "Price", "Quantity"];
const SQ = [
  { label: "WHERE text", sql: ["SELECT ItemNo, Name", "FROM InstrumentStock", 'WHERE SupplierCode = "WND";'], cols: [0, 1], where: (r) => r[3] === "WND" },
  { label: "WHERE NOT (Boolean)", sql: ["SELECT Name", "FROM InstrumentStock", "WHERE NOT InStock;"], cols: [1], where: (r) => r[2] === "No" },
  { label: "ORDER BY", sql: ["SELECT ItemNo, Name, Price", "FROM InstrumentStock", "WHERE Price > 200", "ORDER BY Price;"], cols: [0, 1, 4], where: (r) => r[4] > 200, order: [4, 1] },
  { label: "AND", sql: ["SELECT Name", "FROM InstrumentStock", 'WHERE SupplierCode = "BRS" AND InStock;'], cols: [1], where: (r) => r[3] === "BRS" && r[2] === "Yes" },
  { label: "OR with DESC", sql: ["SELECT Name, Quantity", "FROM InstrumentStock", 'WHERE SupplierCode = "MUS" OR Quantity > 10', "ORDER BY Quantity DESC;"], cols: [1, 5], where: (r) => r[3] === "MUS" || r[5] > 10, order: [5, -1] },
  { label: "SUM", sql: ["SELECT SUM(Quantity)", "FROM InstrumentStock", 'WHERE SupplierCode = "WND";'], agg: "sum", where: (r) => r[3] === "WND" },
  { label: "COUNT", sql: ["SELECT COUNT(ItemNo)", "FROM InstrumentStock", "WHERE Price < 150;"], agg: "count", where: (r) => r[4] < 150 }
];
pick("sq", SQ, (q) => {
  const hit = IS.filter(q.where); let rows = hit.slice();
  if (q.order) rows.sort((a, b) => (q.order[1] === -1 ? b[q.order[0]] - a[q.order[0]] : q.order[1] === 1 ? (a[q.order[0]] < b[q.order[0]] ? -1 : 1) : a[q.order[0]] - b[q.order[0]]));
  const fmt = (r, c) => (c === 4 ? r[c].toFixed(2) : r[c]);
  const outLines = q.agg ? [q.agg === "sum" ? hit.reduce((s, r) => s + r[5], 0) : hit.length] : rows.map((r) => q.cols.map((c) => fmt(r, c)).join(" "));
  const tb = `<div class="tw"><table class="t mx"><tr>${COLS.map((c) => `<th>${c}</th>`).join("")}</tr>${IS.map((r) => `<tr>${r.map((v, i) => `<td class="${q.where(r) ? "on" : "z"}">${i === 4 ? v.toFixed(2) : v}</td>`).join("")}</tr>`).join("")}</table></div>`;
  return `<div class="formula" style="white-space:pre">${q.sql.join("\\n")}</div>${tb}<p><b>Output</b> (no punctuation, ${q.order ? "in the ORDER BY order" : "in table order"}):</p><div class="formula" style="white-space:pre">${outLines.join("\\n") || "(no records)"}</div><p>${hit.length} record${hit.length === 1 ? "" : "s"} match the WHERE condition. ${q.agg ? "SUM adds the values; COUNT counts the records." : "Only the SELECT fields are written, in the order SELECT lists them."}</p>`;
});
''' + CLASSIFY("cl1", "Which gate is it?", ["NOT", "AND", "OR", "NAND", "NOR", "XOR"],
  [("Reverses a single input", 0), ("Gives 1 only when both inputs are 1", 1), ("Gives 1 when at least one input is 1", 2), ("Gives 0 only when both inputs are 1", 3), ("Gives 1 only when both inputs are 0", 4), ("Gives 1 when the two inputs are different", 5),
   ("Output is 1 for inputs 11, and 0 for inputs 00", 1), ("Output is 0 for inputs 11 and 1 for inputs 01", 3), ("Output is 1 for inputs 01 and 0 for inputs 11", 5)],
  "NAND and NOR are the NOT of AND and OR. XOR needs the inputs to differ.") + CLASSIFY("cl2", "Which data type suits each field?", ["Text or alphanumeric", "Character", "Boolean", "Integer", "Real", "Date/time"],
  [("A book code such as LB204", 0), ("A single grade letter", 1), ("Hardback: yes or no", 2), ("Number of copies in stock", 3), ("A price such as 8.50", 4), ("The date a song was recorded", 5), ("A weight such as 20.5 kg", 4), ("A person's name", 0), ("InStock", 2)],
  "Choose by what is stored: whole numbers are integers, numbers with a fractional part are real, yes or no is Boolean.") + ORDER(
  "Put the reading of an SQL statement in the order the computer does it.",
  ["FROM: find the table", "WHERE: keep the rows that match", "ORDER BY: sort the rows if asked", "SELECT: show only the fields listed, in that order"],
  "FROM, WHERE, ORDER BY, SELECT.") + MATCH([
  ["SELECT", "Lists the fields to display"], ["FROM", "Names the table"], ["WHERE", "Gives the search condition"], ["ORDER BY", "Sorts the rows"], ["COUNT", "Counts the records"], ["SUM", "Adds the values of a field"]]) + CALC([
  {"q": "A truth table has 3 inputs. How many rows does it have?", "a": 8, "unit": "", "tol": 0.01, "hint": "2 × 2 × 2.", "sol": "<b>8</b>."},
  {"q": "A four-mark truth table has 8 outputs and 6 are correct. How many marks?", "a": 3, "unit": "", "tol": 0.01, "hint": "6 or 7 correct gives 3.", "sol": "<b>3</b> marks."},
  {"q": "A table has 7 fields and 12 records. How many data items are stored (not counting the headings)?", "a": 84, "unit": "", "tol": 0.01, "hint": "7 × 12.", "sol": "<b>84</b>."},
  {"q": "Five rock songs last 3, 4, 2, 5 and 6 minutes. What does SELECT SUM(Minutes) … WHERE Genre = 'rock' give?", "a": 20, "unit": "min", "tol": 0.01, "hint": "3 + 4 + 2 + 5 + 6.", "sol": "<b>20</b>."},
  {"q": "What is the output of a NAND gate when both inputs are 1? (Give 0 or 1.)", "a": 0, "unit": "", "tol": 0.01, "hint": "AND gives 1, NAND is NOT AND.", "sol": "<b>0</b>."}]) + MCQ([
  ("How should the NOT of X be written in an expression?", ["X NOT", "NOT X", "X'", "-X"], 1, "NOT comes first."),
  ("Which mistake would turn the final column into the exact opposite of the right answer?", ["Rows in the wrong order", "Missing the final NOT in a NAND or NOR", "Writing the inputs in capitals", "Counting the heading as a row"], 1, "NAND and NOR end with a negation, so missing it reverses every output."),
  ("In SQL, which line decides which records are shown?", ["SELECT", "FROM", "WHERE", "ORDER BY"], 2, "WHERE gives the search condition."),
  ("A table has fields ItemNo, Type and Price. Why is Type not a good primary key?", ["It is text", "Its values repeat, so it is not unique", "It is too short", "It is a Boolean"], 1, "A primary key must be a unique identifier."),
  ("What should the output of an SQL statement not contain?", ["The data", "Extra punctuation", "The right columns", "The right order"], 1, "The report says punctuation should not be in the output.")
], "qz1") + CARDS([
  ("NOT", "Reverses one input."), ("AND, OR", "Both 1; at least one 1."), ("NAND, NOR", "NOT of AND, NOT of OR."), ("XOR", "1 when inputs differ."), ("Truth table", "Binary rows, a column per gate."),
  ("Primary key", "A unique identifier."), ("SQL order", "FROM, WHERE, ORDER BY, SELECT."), ("SQL output", "Selected fields, matching rows, no punctuation.")])

build("cx5", "ig-cs-logic-databases-technique", "Logic Circuits, Truth Tables and Databases: Technique and Practice", EYC,
  "How logic circuits, truth tables and single-table databases are marked in Paper 2: expressions, working columns, drawing circuits, SQL output, data types and primary keys, with eight real questions.",
  tabs(learn, watch, explore, practise, real, exam, tips), js)
