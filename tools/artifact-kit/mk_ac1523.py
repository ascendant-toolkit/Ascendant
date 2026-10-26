"""A Level CS syllabus 15.2.3: Boolean algebra, sum-of-products and De Morgan's laws. Run: python3 tools/artifact-kit/mk_ac1523.py"""
from ak15 import *

N = lambda x: 1 - int(bool(x))

# every simplification answered below is checked by brute force when the page is built
assert same(lambda a, b, c: N(a or b or c) or N(b or c), lambda a, b, c: N(b) and N(c), 3)
assert same(lambda a, b, c: N(a or b or c) or N(N(b) or c), lambda a, b, c: N(c) and (N(a) or b), 3)
assert same(lambda x, y, z: (x and y and z) or (x and N(y) and z) or N(x), lambda x, y, z: z or N(x), 3)
assert same(lambda a, b, c, d: N(N(a and b) and N(a and c) and N(b and d)), lambda a, b, c, d: (a and (b or c)) or (b and d), 4)
assert same(lambda a, b, c, d: (N(a) and N(b) and N(c) and N(d)) or (N(a) and N(b) and c and N(d)) or (N(a) and b and N(c) and N(d)) or (N(a) and b and c and N(d)), lambda a, b, c, d: N(a) and N(d), 4)
assert same(lambda a, b, c: N(a or b) and (N(a and b) or N(b and c)), lambda a, b, c: N(a) and N(b), 3)
assert same(lambda a, b, c, d: N(N(a) and b and c and N(d)) or (a and d), lambda a, b, c, d: a or N(b) or N(c) or d, 4)


def wk(rows):
    """Worked solution: (expression, law applied) per line."""
    h = '<div class="tw"><table class="t"><tr><th>Working</th><th>Law used</th></tr>'
    for e, l in rows:
        h += f'<tr><td class="bx">{ob(e)}</td><td>{ob(l)}</td></tr>'
    return h + "</table></div>"


def lawtab():
    rows = [
        ("Identity", "A . 1 = A", "A + 0 = A"),
        ("Annulment (null)", "A . 0 = 0", "A + 1 = 1"),
        ("Idempotent", "A . A = A", "A + A = A"),
        ("Inverse (complement)", "A . ~A = 0", "A + ~A = 1"),
        ("Double negation", "~~A = A", "~~A = A"),
        ("Commutative", "A . B = B . A", "A + B = B + A"),
        ("Associative", "(A . B) . C = A . (B . C)", "(A + B) + C = A + (B + C)"),
        ("Distributive", "A . (B + C) = A . B + A . C", "A + B . C = (A + B) . (A + C)"),
        ("Absorption", "A . (A + B) = A", "A + A . B = A"),
        ("Redundancy", "A . (~A + B) = A . B", "A + ~A . B = A + B"),
        ("De Morgan", "~(A . B) = ~A + ~B", "~(A + B) = ~A . ~B")]
    h = '<div class="tw"><table class="t"><tr><th>Law</th><th>AND form</th><th>OR form</th></tr>'
    for n, a, b in rows:
        h += f'<tr><td><b>{n}</b></td><td class="bx">{ob(a)}</td><td class="bx">{ob(b)}</td></tr>'
    return h + "</table></div>"


T3 = tt_from_mins(["A", "B", "C"], "X", [1, 4, 5, 7])

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p><b>Boolean algebra</b> is a set of laws for rewriting logic expressions, where <b>.</b> means AND, <b>+</b> means OR and a <b>bar</b> over a term means NOT. Any truth table can be written as a <b>sum-of-products</b>: one AND term for each row where the output is 1, all joined by OR. <b>De Morgan's laws</b> break a bar over a group: the bar over AND becomes OR, and the bar over OR becomes AND, with each term inverted. <b>Simplifying</b> means using the laws to give an equivalent expression with fewer terms or gates, and the exam asks you to show each step. Every answer can be checked by comparing truth tables.</p></div>

  <h2>1 · From a truth table to a sum-of-products</h2>
  <p>Find every row where the output is 1. For each one write an AND term using each input once: write the input as it is if its value in that row is 1, with a bar if it is 0. Join the terms with OR.</p>
  ''' + T3 + '''
  <p>X is 1 in rows 001, 100, 101 and 111, so X = ''' + bx(sop([1, 4, 5, 7], ["A", "B", "C"])) + '''. This is a sum (OR) of products (ANDs), and it is exactly the expression for a circuit made of AND gates feeding one OR gate.</p>
  <div class="tip"><b class="h">Remember</b>Use the rows where the output is <b>1</b>. A row with 0 in the output column gives no term. Four inputs give sixteen rows; check that you have one term per 1 and no others.</div>

  <h2>2 · The laws</h2>
  ''' + lawtab() + '''
  <p>The ones used most in the exams are <b>De Morgan</b>, <b>double negation</b>, <b>distributive</b>, <b>absorption</b>, <b>idempotent</b> and <b>annulment</b>. Write the name of the law next to each line.</p>

  <h2>3 · De Morgan's laws</h2>
  <p>Break the bar and change the operator:</p>
  <ul>
    <li>''' + bx("~(A + B) = ~A . ~B") + ''': NOT (A or B) is the same as NOT A and NOT B. This is a NOR gate.</li>
    <li>''' + bx("~(A . B) = ~A + ~B") + ''': NOT (A and B) is the same as NOT A or NOT B. This is a NAND gate.</li>
  </ul>
  <p>The laws extend to three terms: ''' + bx("~(A + B + C) = ~A . ~B . ~C") + '''. A double bar cancels, so ''' + bx("~(~A + B) = A . ~B") + ''' (the bar breaks, A is inverted twice, B once).</p>
  ''' + tt_from_fn(["A", "B"], {"~(A+B)": lambda a, b: N(a or b), "~A.~B": lambda a, b: N(a) and N(b), "~(A.B)": lambda a, b: N(a and b), "~A+~B": lambda a, b: N(a) or N(b)}) + '''
  <p>The columns match in pairs for every row: the two sides of each law have the same truth table.</p>

  <h2>4 · Simplifying with the laws</h2>
  <p>A method that works:</p>
  <ol>
    <li>Remove any bars over groups with De Morgan, and cancel double bars.</li>
    <li>Look for a common factor and take it out with the distributive law.</li>
    <li>Use inverse, idempotent, annulment, identity or absorption to remove terms.</li>
    <li>State the law on each line, and finish with the simplified expression.</li>
  </ol>
  <h3>Worked example 1 (M/J 2026, Paper 33)</h3>
  <p>Simplify ''' + bx("X = ~(A+B+C) + ~(B+C)") + '''</p>
  ''' + wk([("X = ~(A+B+C) + ~(B+C)", "given"), ("X = ~A.~B.~C + ~B.~C", "De Morgan's laws"), ("X = ~B.~C.(~A + 1)", "distributive law (take out ~B.~C)"), ("X = ~B.~C", "annulment: ~A + 1 = 1")]) + '''
  <h3>Worked example 2 (O/N 2025, Paper 33)</h3>
  <p>Simplify ''' + bx("X = ~(A+B+C) + ~(~B+C)") + '''</p>
  ''' + wk([("X = ~(A+B+C) + ~(~B+C)", "given"), ("X = ~A.~B.~C + ~~B.~C", "De Morgan's laws"), ("X = ~A.~B.~C + B.~C", "double negation"), ("X = ~C.(~A.~B + B)", "distributive law"), ("X = ~C.(~A + B)", "redundancy: ~A.~B + B = ~A + B")]) + '''
  <h3>Worked example 3 (O/N 2022, Paper 32)</h3>
  <p>Simplify ''' + bx("~(~(A.B) . ~(A.C) . ~(B.D))") + '''</p>
  ''' + wk([("~(~(A.B) . ~(A.C) . ~(B.D))", "given"), ("~~(A.B) + ~~(A.C) + ~~(B.D)", "De Morgan's laws (bar over a product becomes a sum of barred terms)"), ("A.B + A.C + B.D", "double negation"), ("A.(B + C) + B.D", "distributive law")]) + '''

  <h2>5 · Common ways to lose marks</h2>
  <ul>
    <li>Changing the operator but forgetting to bar each term: ~(A + B) is ~A . ~B, not ~A + ~B.</li>
    <li>Leaving out the name of the law. Several marks are for showing the right law at each step.</li>
    <li>Writing a sum-of-products term for each 0 row.</li>
    <li>Dropping a bar during copying. Rewrite carefully and check with a truth table if there is time.</li>
    <li>Stopping early. Check whether a common factor can still be taken out.</li>
  </ul>
'''

watch = '''
  <h2>1 · Writing a sum-of-products from a truth table</h2>
  <div id="stA"></div>
  <h2>2 · De Morgan's law, row by row</h2>
  <div id="stB"></div>
  <h2>3 · Simplifying step by step</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Build a sum-of-products</h2>
  <p>Click the output column to switch each row between 0 and 1. The sum-of-products and its simplest form update.</p>
  <div class="card"><div id="sopT"></div><div class="verdict" id="sopV"></div></div>
  <h2>Lab 2 · Do two expressions match?</h2>
  <p>Choose a law. The truth tables of both sides are shown side by side.</p>
  <div class="card"><div id="lwB" class="btnrow"></div><div id="lwO"></div></div>
  <h2>Lab 3 · Simplify and check</h2>
  <p>Choose an expression from a past paper. The tool shows the original and the simplified form with their truth tables, so you can see they are equal.</p>
  <div class="card"><div id="spB" class="btnrow"></div><div id="spO"></div></div>
'''

practise = '''
  <h2>1 · Which law?</h2><div id="cl1" class="card"></div>
  <h2>2 · Apply De Morgan's law</h2><div id="cl2" class="card"></div>
  <h2>3 · Match the expression to its simplified form</h2><div id="m1" class="card"></div>
  <h2>4 · Put the steps of simplifying in order</h2><div id="o1" class="card"></div>
  <h2>5 · Counting and checking</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Designing a circuit from a specification", "An engineer writes the sum-of-products from the required truth table, simplifies it, then builds the circuit. Fewer terms means fewer gates, a smaller chip and less power.", "simplifying reduces the number of gates.") +
rw("NAND and NOR gates", "Chips are often built from only NAND (or only NOR) gates because they are cheap and quick to make. De Morgan's laws show how to turn AND/OR designs into NAND/NOR ones.", "~(A . B) = ~A + ~B.") +
rw("Search filters", "'NOT (cats OR dogs)' means 'NOT cats AND NOT dogs': a result must contain neither word. That is De Morgan's law in a search box.", "~(A + B) = ~A . ~B.") +
rw("Safety interlocks", "A machine runs only when the guard is closed AND the stop button is not pressed. Simplified expressions mean simpler wiring and fewer faults.", "the output is a Boolean expression of the inputs.") +
rw("Programming conditions", "NOT (x > 5 AND y > 5) can be rewritten as x <= 5 OR y <= 5, which is often easier to read.", "De Morgan's laws apply to conditions in code as well.")
)

where = [
  ("O/N 2021", "31, 32", "7(a)", "3", "Sum-of-products from a four-input truth table"),
  ("M/J 2023", "32", "9(a)", "3", "Sum-of-products from a four-input truth table"),
  ("O/N 2023", "31, 33", "6(b)", "3", "Simplify a four-term expression with Boolean algebra"),
  ("O/N 2023", "32", "7(a), (b), (c)", "1 + 1 + 3", "Truth table for a three-input NOR; apply De Morgan; simplify with Boolean algebra"),
  ("O/N 2024", "31, 33", "7(a)", "3", "Sum-of-products from a four-input truth table"),
  ("M/J 2025", "31", "5(a)", "2", "Sum-of-products from a four-input truth table"),
  ("M/J 2025", "32", "7(c)", "4", "Simplify with Boolean algebra including De Morgan's laws"),
  ("O/N 2022", "32", "8(c)", "3", "Simplify with Boolean algebra including De Morgan's laws"),
  ("M/J 2026", "32", "7(b)", "3", "Simplify with De Morgan's laws and Boolean algebra"),
  ("M/J 2026", "33", "6(b)", "3", "Simplify with De Morgan's laws and Boolean algebra"),
  ("O/N 2025", "33", "6(b)", "3", "Simplify with De Morgan's laws and Boolean algebra")]


def trow(mins, names, out):
    return tt_from_mins(names, out, mins)


past = '''  <p class="note">Sum-of-products and simplification appear in Paper 3 in almost every series. The Karnaugh-map parts that usually follow them are on the 15.2.4 page. Questions are reworded from the papers; check the original paper and mark scheme for the exact wording.</p>

  <h3>Sum-of-products from a truth table</h3>
''' + peq(SRC("w21", "31/32", "Q7(a)"), "3 marks", "Write",
  "Write the Boolean expression that corresponds to the given truth table as a sum-of-products." + trow([9, 11, 12, 13, 14, 15], ["A", "B", "C", "D"], "Z"),
  "One AND term for each row where Z = 1.",
  "<p>Z = " + bx(sop([9, 11, 12, 13, 14, 15], list("ABCD"))) + "</p><p>" + mks(["Two correct products", "Two more correct products", "The last two correct products (one mark for every two correct, max 3)"]) + "</p>", "Writing terms for the rows where Z = 0. There are ten such rows; only the six rows with Z = 1 give terms.") + peq(SRC("s23", "32", "Q9(a)"), "3 marks", "Write",
  "This truth table represents a logic circuit. Write the Boolean logic expression that corresponds to the given truth table as the sum-of-products." + trow([0, 1, 2, 3, 6, 7], list("ABCD"), "Z"),
  "Count the 1s first: six rows give six terms.",
  "<p>Z = " + bx(sop([0, 1, 2, 3, 6, 7], list("ABCD"))) + "</p><p>" + mks(["Any two correct products", "Four correct products", "All six correct products with none extra"]) + "</p>", None) + peq(SRC("w24", "31/33", "Q7(a)"), "3 marks", "Write",
  "The truth table for a logic circuit is shown. Write the Boolean logic expression that corresponds to the given truth table as the sum-of-products." + trow([1, 3, 9, 11, 13, 15], list("ABCD"), "T"),
  "Six 1s, so six terms. The same table appears in Paper 31 and Paper 33.",
  "<p>T = " + bx(sop([1, 3, 9, 11, 13, 15], list("ABCD"))) + "</p><p>" + mks(["Two correct products", "Four correct products", "All six correct products"]) + " (one mark for every two correct, max 3)</p>", "Putting the bar on the wrong letter. In row 1001, B and C are 0 so they are barred and A and D are not.") + peq(SRC("s25", "31", "Q5(a)"), "2 marks", "Write",
  "This truth table represents a logic circuit. Write the Boolean logic expression that corresponds to the given truth table as the sum-of-products." + trow([0, 5, 7, 8, 13, 15], list("ABCD"), "Z"),
  "Two marks for all six terms, one mark for any three.",
  "<p>Z = " + bx(sop([0, 5, 7, 8, 13, 15], list("ABCD"))) + "</p><p>" + mks(["Two marks for all six correct terms; one mark for any three correct terms"]) + "</p>", None) + '''
  <h3>De Morgan's laws</h3>
'''
past += peq(SRC("w23", "32", "Q7(a)(b)"), "1 + 1 marks", "Complete / Apply",
  "(a) This logic circuit is a three-input NOR gate and represents the Boolean expression " + bx("X = ~(A+B+C)") + ". Complete the truth table. (b) Apply De Morgan's laws to the expression " + bx("X = ~(A+B+C)") + "." + ttable(["A", "B", "C"], ["X"], [bits(m, 3) + [""] for m in range(8)]),
  "NOR is 1 only when every input is 0. Break the bar and invert each input.",
  "<p><b>(a)</b> " + mks(["X = 1 only in the first row (A = B = C = 0), otherwise 0"]) + "</p>" + tt_from_mins(["A", "B", "C"], "X", [0]) + "<p><b>(b)</b> X = " + bx("~A.~B.~C") + " " + mks(["~(A+B+C) becomes ~A . ~B . ~C"], "a") + "</p>", "Writing ~A + ~B + ~C. When a bar over OR is broken, the OR becomes AND.")
past += '''
  <h3>Simplifying with Boolean algebra</h3>
''' + peq(SRC("w23", "32", "Q7(c)"), "3 marks", "Simplify",
  "Simplify the following expression using Boolean algebra. Show all the stages in your simplification. " + bx("T = X.Y.Z + X.~Y.Z + ~X"),
  "Take X.Z out of the first two terms.",
  wk([("T = X.Y.Z + X.~Y.Z + ~X", "given"), ("T = X.Z.(Y + ~Y) + ~X", "distributive law"), ("T = X.Z.1 + ~X = X.Z + ~X", "inverse law, then identity"), ("T = Z + ~X", "redundancy: X.Z + ~X = Z + ~X")]) + "<p>" + mks(["Correct use of the distributive law", "Correct use of the inverse and identity laws (Y + ~Y = 1)", "Correct final answer: Z + ~X"]) + "</p>", "Stopping at X.Z + ~X. The redundancy law removes the X from the first term.") + peq(SRC("w23", "31/33", "Q6(b)"), "3 marks", "Simplify",
  "Simplify the given Boolean expression using Boolean algebra. Show your working. " + bx("Y = ~A.~B.~C.~D + ~A.~B.C.~D + ~A.B.~C.~D + ~A.B.C.~D"),
  "All four terms contain ~A and ~D. Take them out.",
  wk([("Y = ~A.~B.~C.~D + ~A.~B.C.~D + ~A.B.~C.~D + ~A.B.C.~D", "given"), ("Y = ~A.~D.(~B.~C + ~B.C + B.~C + B.C)", "distributive law (common factor ~A.~D)"), ("Y = ~A.~D.(~B.(~C + C) + B.(~C + C))", "distributive law"), ("Y = ~A.~D.(~B.1 + B.1)", "inverse law"), ("Y = ~A.~D.(~B + B) = ~A.~D.1", "inverse law"), ("Y = ~A.~D", "identity")]) + "<p>" + mks(["Correct working, up to two marks", "Correct answer: ~A.~D"]) + "</p>", None) + peq(SRC("w22", "32", "Q8(c)"), "3 marks", "Simplify",
  "Simplify the following expression using Boolean algebra, including De Morgan's laws. Show your working. " + bx("~(~(A.B) . ~(A.C) . ~(B.D))"),
  "A long bar over everything: break it, then cancel the double bars.",
  wk([("~(~(A.B) . ~(A.C) . ~(B.D))", "given"), ("~~(A.B) + ~~(A.C) + ~~(B.D)", "De Morgan's laws"), ("A.B + A.C + B.D", "double negation"), ("A.(B + C) + B.D", "distributive law")]) + "<p>" + mks(["Correct application of De Morgan's law", "Correct application of the double negation or distributive law", "Correct answer: A.(B+C) + B.D"]) + "</p>", "Applying De Morgan to the long bar but leaving the bars on A.B, A.C and B.D unchanged. Each ~(~(A.B)) cancels to A.B.") + peq(SRC("s25", "32", "Q7(c)"), "4 marks", "Simplify",
  "Use Boolean algebra including De Morgan's laws to simplify the following expression. Show all working. " + bx("~(A+B) . (~(A.B) + ~(B.C))"),
  "Break each bar first, then collect the repeated terms.",
  wk([("~(A+B) . (~(A.B) + ~(B.C))", "given"), ("(~A.~B) . (~A + ~B + ~B + ~C)", "De Morgan's laws"), ("(~A.~B) . (~A + ~B + ~C)", "idempotent law (~B + ~B = ~B)"), ("~A.~B.~A + ~A.~B.~B + ~A.~B.~C", "distributive law"), ("~A.~B + ~A.~B + ~A.~B.~C", "idempotent law"), ("~A.~B + ~A.~B.~C = ~A.~B", "absorption law (final answer)")]) + "<p>" + mks(["Correct application of De Morgan's laws", "Correct application of idempotent, distributive or absorption laws", "Another correct application of those laws", "Correct final answer: ~A.~B (or ~(A+B))"]) + "</p>", "Applying De Morgan to the whole second bracket as one bar. There are two separate bars, over A.B and over B.C.") + peq(SRC("s26", "32", "Q7(b)"), "3 marks", "Simplify",
  "Simplify the following expression using De Morgan's laws and Boolean algebra. Show all the stages in your simplification. " + bx("X = ~(~A.B.C.~D) + ~~(A.D)"),
  "Break the first bar. Cancel double bars. Then look for absorption.",
  wk([("X = ~(~A.B.C.~D) + ~~(A.D)", "given"), ("X = ~~A + ~B + ~C + ~~D + A.D", "De Morgan's laws, and double negation on the second term"), ("X = A + ~B + ~C + D + A.D", "double negation"), ("X = A + ~B + ~C + D", "absorption: A + A.D = A")]) + "<p>" + mks(["Correct application of De Morgan's laws", "Correct application of double negation or absorption", "Correct answer: A + ~B + ~C + D"]) + "</p>", "Writing ~A for the first term. The bar over ~A cancels to give A, not ~A.") + peq(SRC("s26", "33", "Q6(b)"), "3 marks", "Simplify",
  "Simplify the following expression using De Morgan's laws and Boolean algebra. Show all the stages in your simplification. " + bx("X = ~(A+B+C) + ~(B+C)"),
  "Break both bars, then take ~B.~C out.",
  wk([("X = ~(A+B+C) + ~(B+C)", "given"), ("X = ~A.~B.~C + ~B.~C", "De Morgan's laws"), ("X = ~B.~C.(~A + 1)", "distributive law"), ("X = ~B.~C", "annulment law")]) + "<p>" + mks(["Correct answer ~B.~C (or ~(B+C))", "Up to two marks for correct use of different laws: De Morgan, distributive, annulment"]) + "</p>", None) + peq(SRC("w25", "33", "Q6(b)"), "3 marks", "Simplify",
  "Simplify the following expression using De Morgan's laws and Boolean algebra. Show all the stages in your simplification. " + bx("X = ~(A+B+C) + ~(~B+C)"),
  "A bar over ~B + C: break it and cancel the double bar on B.",
  wk([("X = ~(A+B+C) + ~(~B+C)", "given"), ("X = ~A.~B.~C + ~~B.~C", "De Morgan's laws"), ("X = ~A.~B.~C + B.~C", "double negation"), ("X = ~C.(~A.~B + B)", "distributive law"), ("X = ~C.(~A + B)", "redundancy law")]) + "<p>" + mks(["Correct use of De Morgan's laws", "Correct use of another Boolean algebra law", "Correct answer: ~C.(~A + B)"]) + "</p>", "Writing ~B.~C for the second term. The bar over ~B cancels with the bar over the whole group, giving B.~C.")

review = req("3 marks", "Write", "The truth table for X has inputs A, B, C and X = 1 for rows 011, 101 and 110. Write X as a sum-of-products, then simplify it if you can.", "Three terms, one for each 1.",
  "<p>" + mks(["Row 011: ~A.B.C", "Row 101: A.~B.C and row 110: A.B.~C", "X = ~A.B.C + A.~B.C + A.B.~C (no further simplification is possible)"]) + "</p>", None) + req("2 marks", "Apply", "Use De Morgan's laws to remove the bar over the whole group in " + bx("~(~A + B . C)") + ".", "Break the bar, change the operator, cancel double bars.",
  "<p>" + wk([("~(~A + B.C)", "given"), ("~~A . ~(B.C)", "De Morgan's laws"), ("A . (~B + ~C)", "double negation and De Morgan's laws")]) + mks(["A . ~(B.C)", "A . (~B + ~C)"]) + "</p>", None) + req("3 marks", "Simplify", "Simplify " + bx("A.B + A.~B + ~A.B") + " using Boolean algebra.", "Take A out of the first two terms.",
  "<p>" + wk([("A.B + A.~B + ~A.B", "given"), ("A.(B + ~B) + ~A.B", "distributive law"), ("A + ~A.B", "inverse and identity laws"), ("A + B", "redundancy law")]) + mks(["A.(B + ~B)", "A + ~A.B", "A + B"]) + "</p>", None) + req("2 marks", "Explain", "Explain why using NAND gates only can be useful when building a circuit.", "Think about the types of gate on a chip.",
  "<p>" + mks(["NAND gates can build any other gate (AND, OR, NOT), so only one type of gate is needed", "Using one type of gate makes manufacture simpler and cheaper"]) + "</p>", None) + req("3 marks", "Show", "Show with a truth table that " + bx("~(A.B)") + " is equal to " + bx("~A + ~B") + ".", "Four rows, four columns.",
  "<p>" + mks(["Truth table with the four rows of A and B", "~(A.B) column: 1, 1, 1, 0", "~A + ~B column: 1, 1, 1, 0, which is identical"]) + "</p>" + tt_from_fn(["A", "B"], {"~(A.B)": lambda a, b: N(a and b), "~A+~B": lambda a, b: N(a) or N(b)}), None)

exam = exam20("Part 1 is real 9618 questions on sum-of-products, De Morgan's laws and Boolean algebra (Paper 3), 2021 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", where, past, review)

tips = tips_html([
  ("Sum-of-products: rows where the output is 1.", "One AND term for each, joined by OR."),
  ("Bar a letter when its value in that row is 0.", "Row 1001 gives A.~B.~C.D."),
  ("De Morgan: break the bar, change the operator.", "~(A+B) = ~A.~B and ~(A.B) = ~A+~B."),
  ("Cancel double bars.", "~~A = A. Check each bar carefully."),
  ("Name the law on every line.", "Marks are for the laws as well as the answer."),
  ("Check with a truth table.", "If both expressions have the same table they are equal."),
], [
  ("a sum-of-products", "AND terms joined by OR, one for each row with output 1."),
  ("De Morgan's laws", "~(A.B) = ~A + ~B and ~(A+B) = ~A . ~B."),
  ("absorption", "A + A.B = A."),
  ("double negation", "~~A = A."),
], [("Write", "Give the expression only, in the form asked."), ("Apply", "Use the law named and show the result."), ("Simplify", "Show each step and name each law."), ("Show", "Provide working or a table that proves it.")]) + FC

SIMP = [
  {"n": "M/J 2026 P33 6(b)", "a": "~(A+B+C) + ~(B+C)", "b": "~B.~C", "f": "(a,b,c)=>!(a|b|c)|!(b|c)", "g": "(a,b,c)=>!b&!c", "nv": 3},
  {"n": "O/N 2025 P33 6(b)", "a": "~(A+B+C) + ~(~B+C)", "b": "~C.(~A+B)", "f": "(a,b,c)=>!(a|b|c)|!(!b|c)", "g": "(a,b,c)=>!c&(!a|b)", "nv": 3},
  {"n": "O/N 2022 P32 8(c)", "a": "~(~(A.B).~(A.C).~(B.D))", "b": "A.(B+C) + B.D", "f": "(a,b,c,d)=>!(!(a&b)&!(a&c)&!(b&d))", "g": "(a,b,c,d)=>(a&(b|c))|(b&d)", "nv": 4},
  {"n": "O/N 2023 P31 6(b)", "a": "~A.~B.~C.~D + ~A.~B.C.~D + ~A.B.~C.~D + ~A.B.C.~D", "b": "~A.~D", "f": "(a,b,c,d)=>(!a&!b&!c&!d)|(!a&!b&c&!d)|(!a&b&!c&!d)|(!a&b&c&!d)", "g": "(a,b,c,d)=>!a&!d", "nv": 4},
  {"n": "M/J 2025 P32 7(c)", "a": "~(A+B) . (~(A.B) + ~(B.C))", "b": "~A.~B", "f": "(a,b,c)=>!(a|b)&(!(a&b)|!(b&c))", "g": "(a,b,c)=>!a&!b", "nv": 3}]

js = AKJS + AK20JS + AK15JS + "const SIMP = " + json.dumps(SIMP) + ";\n" + r'''
/* 1: sum-of-products from the truth table 011, 101, 110 */
(function () {
  const names = ["A", "B", "C"], mins = [3, 5, 6];
  const draw = (s) => { const k = Math.round(s.i); let o = ""; o += SV.text(14, 18, "A  B  C   X", "lbl bd", { style: "font-family:var(--mono)" });
    for (let m = 0; m < 8; m++) { const b = bitsOf(m, 3), one = mins.includes(m), hit = one && mins.indexOf(m) < k; o += SV.rect(8, 28 + m * 30, 190, 26, hit ? "cell-ok" : "cell", { rx: 4 }) + SV.text(14, 46 + m * 30, b.join("  ") + "   " + (one ? 1 : 0), "lbl", { style: "font-family:var(--mono)" }); if (hit) o += SV.text(220, 46 + m * 30, "→ " + [...b].map((x, i) => (x ? names[i] : "~" + names[i])).join("."), "lbl bd t3", { style: "font-family:var(--mono)" }); }
    if (k >= 3) o += SV.text(8, 285, "X = ~A.B.C + A.~B.C + A.B.~C", "lbl bd", { style: "font-family:var(--mono)" }); return o; };
  Lib.stepper($("#stA"), { w: 560, h: 300, label: "Sum-of-products", base: { i: 0 }, draw, tween: 150, dwell: 2400, steps: [{ cap: "Find every row where X = 1: rows 011, 101 and 110.", s: { i: 0 } }, { cap: "Row 011: A = 0, B = 1, C = 1 gives <b>~A.B.C</b>.", s: { i: 1 } }, { cap: "Row 101 gives <b>A.~B.C</b>.", s: { i: 2 } }, { cap: "Row 110 gives <b>A.B.~C</b>. Join the terms with OR.", s: { i: 3 } }] });
})();
/* 2: De Morgan, row by row */
(function () {
  const rows = [[0, 0], [0, 1], [1, 0], [1, 1]];
  const draw = (s) => { const k = Math.round(s.i); let o = SV.text(14, 20, "A B   ~(A.B)   ~A + ~B", "lbl bd", { style: "font-family:var(--mono)" });
    rows.forEach(([a, b], i) => { const nand = 1 - (a & b), or = (1 - a) | (1 - b), on = i <= k; o += SV.rect(8, 30 + i * 40, 420, 34, on ? "cell-ok" : "cell", { rx: 6, ...op(on ? 1 : 0.4) }) + SV.text(18, 53 + i * 40, a + " " + b, "lbl bd", { style: "font-family:var(--mono)" }) + (on ? SV.text(110, 53 + i * 40, String(nand), "lbl bd", { style: "font-family:var(--mono)" }) + SV.text(250, 53 + i * 40, String(or), "lbl bd", { style: "font-family:var(--mono)" }) + SV.text(330, 53 + i * 40, "equal", "sm t3") : ""); });
    return o; };
  Lib.stepper($("#stB"), { w: 440, h: 200, label: "De Morgan", base: { i: 0 }, draw, tween: 150, dwell: 2200, steps: rows.map(([a, b], i) => ({ cap: `A = ${a}, B = ${b}: ~(A.B) = <b>${1 - (a & b)}</b> and ~A + ~B = <b>${(1 - a) | (1 - b)}</b>. The two sides agree in every row, which proves De Morgan's law for AND.`, s: { i } })) });
})();
/* 3: simplifying X = ~(A+B+C) + ~(B+C) */
(function () {
  const lines = [["X = ~(A+B+C) + ~(B+C)", "start"], ["X = ~A.~B.~C + ~B.~C", "De Morgan's laws"], ["X = ~B.~C.(~A + 1)", "distributive law"], ["X = ~B.~C", "annulment: ~A + 1 = 1"]];
  const draw = (s) => { const k = Math.round(s.i); let o = ""; lines.forEach(([e, l], i) => { if (i > k) return; o += SV.rect(10, 14 + i * 56, 420, 46, i === k ? "cell-warn" : "cell-ok", { rx: 8 }) + SV.text(24, 43 + i * 56, e.replace(/~/g, "¬"), "lbl bd", { style: "font-family:var(--mono);font-size:16px" }) + SV.text(446, 43 + i * 56, l, "sm"); }); return o; };
  Lib.stepper($("#stC"), { w: 700, h: 240, label: "Simplifying", base: { i: 0 }, draw, tween: 150, dwell: 2600, steps: [{ cap: "Start from the given expression. In the exam, ¬ is written as a bar above the letters.", s: { i: 0 } }, { cap: "Break each bar with De Morgan's law: a bar over OR becomes AND of the barred terms.", s: { i: 1 } }, { cap: "~B.~C is common to both terms, so take it out with the distributive law.", s: { i: 2 } }, { cap: "~A + 1 is always 1 (annulment). The answer is <b>~B.~C</b>.", s: { i: 3 } }] });
})();

/* lab 1 */
(function () {
  const names = ["A", "B", "C"]; let out = [0, 0, 0, 0, 0, 0, 0, 0]; const el = $("#sopT");
  const paint = () => { let h = '<div class="tw"><table class="t mono"><tr><th>A</th><th>B</th><th>C</th><th>X (click)</th></tr>'; for (let m = 0; m < 8; m++) h += "<tr>" + bitsOf(m, 3).map((x) => "<td>" + x + "</td>").join("") + `<td><button data-m="${m}" class="${out[m] ? "on" : ""}">${out[m]}</button></td></tr>`; el.innerHTML = h + "</table></div>";
    const mins = out.map((v, i) => (v ? i : -1)).filter((x) => x >= 0); $("#sopV").innerHTML = "Sum-of-products: <b>X = " + obJS(sopJS(mins, names)) + "</b><br>Simplified: <b>X = " + obJS(simpJS(mins, names)) + "</b>";
    el.querySelectorAll("button").forEach((b) => b.onclick = () => { out[+b.dataset.m] ^= 1; paint(); }); };
  out[1] = out[4] = out[5] = out[7] = 1; paint();
})();
/* lab 2 */
(function () {
  const L = [["De Morgan (AND)", "~(A.B)", "~A + ~B", (a, b) => 1 - (a & b), (a, b) => (1 - a) | (1 - b)], ["De Morgan (OR)", "~(A+B)", "~A . ~B", (a, b) => 1 - (a | b), (a, b) => (1 - a) & (1 - b)], ["Absorption", "A + A.B", "A", (a, b) => a | (a & b), (a, b) => a], ["Distributive", "A.(A+B)", "A", (a, b) => a & (a | b), (a, b) => a], ["Redundancy", "A + ~A.B", "A + B", (a, b) => a | ((1 - a) & b), (a, b) => a | b], ["Idempotent", "A.A", "A", (a, b) => a & a, (a, b) => a]];
  const show = (i) => { const [n, l, r, f, g] = L[i]; let h = `<h3>${n}</h3><div class="tw"><table class="t mono"><tr><th>A</th><th>B</th><th>${obJS(l)}</th><th>${obJS(r)}</th><th></th></tr>`; for (let m = 0; m < 4; m++) { const a = m >> 1, b = m & 1, x = f(a, b), y = g(a, b); h += `<tr><td>${a}</td><td>${b}</td><td>${x}</td><td>${y}</td><td>${x === y ? "equal" : "different"}</td></tr>`; } $("#lwO").innerHTML = h + "</table></div>"; };
  const b = $("#lwB"); L.forEach((l, i) => { const x = document.createElement("button"); x.textContent = l[0]; x.onclick = () => { b.querySelectorAll("button").forEach((y) => (y.className = "")); x.className = "on"; show(i); }; b.appendChild(x); }); b.firstChild.click();
})();
/* lab 3 */
(function () {
  const b = $("#spB");
  const show = (i) => { const e = SIMP[i], f = eval(e.f), g = eval(e.g), nv = e.nv, names = ["A", "B", "C", "D"].slice(0, nv);
    let h = `<p><b>${e.n}</b></p><p>Original: <span class="bx">${obJS(e.a)}</span><br>Simplified: <span class="bx">${obJS(e.b)}</span></p><div class="tw"><table class="t mono"><tr>` + names.map((n) => `<th>${n}</th>`).join("") + "<th>original</th><th>simplified</th></tr>";
    for (let m = 0; m < 1 << nv; m++) { const bb = bitsOf(m, nv), x = +!!f(...bb), y = +!!g(...bb); h += "<tr>" + bb.map((v) => `<td>${v}</td>`).join("") + `<td>${x}</td><td>${y}</td></tr>`; }
    $("#spO").innerHTML = h + "</table></div>"; };
  SIMP.forEach((e, i) => { const x = document.createElement("button"); x.textContent = e.n; x.onclick = () => { b.querySelectorAll("button").forEach((y) => (y.className = "")); x.className = "on"; show(i); }; b.appendChild(x); }); b.firstChild.click();
})();
''' + CLASSIFY("cl1", "Which law is used?", ["De Morgan", "Double negation", "Absorption", "Distributive"],
  [("~(A + B) = ~A . ~B", 0), ("~~A = A", 1), ("A + A.B = A", 2), ("A.(B + C) = A.B + A.C", 3), ("~(A . B) = ~A + ~B", 0), ("A . (A + B) = A", 2)],
  "De Morgan breaks a bar, double negation cancels two bars, absorption removes a term that contains another, distributive takes out a common factor.") + CLASSIFY("cl2", "Does the statement apply De Morgan's law correctly?", ["Correct", "Incorrect"],
  [("~(A + B) = ~A . ~B", 0), ("~(A + B) = ~A + ~B", 1), ("~(A . B) = ~A + ~B", 0), ("~(A . B) = ~A . ~B", 1), ("~(~A . B) = A + ~B", 0), ("~(~A + B) = A + ~B", 1)],
  "Change the operator and bar each term; ~(~A + B) = A . ~B.") + MATCH([
  ["A + A.B", "A (absorption)"], ["~(A.B)", "~A + ~B"], ["A.~A", "0 (inverse)"], ["A + ~A", "1 (inverse)"], ["A + ~A.B", "A + B (redundancy)"]]) + ORDER(
  "Put the steps for simplifying a bar over a group in order.",
  ["Break the bar with De Morgan's law", "Cancel any double bars", "Take out a common factor", "Use the inverse, absorption or annulment law to remove terms", "State the simplified expression"],
  "Break, cancel, factor, remove, state.") + CALC([
  {"q": "A truth table has 16 rows and the output is 1 in six rows. How many terms does the sum-of-products have?", "a": 6, "unit": "", "tol": 0.01, "hint": "One term per 1.", "sol": "<b>6</b>."},
  {"q": "How many rows does a truth table for three inputs have?", "a": 8, "unit": "", "tol": 0.01, "hint": "2 cubed.", "sol": "<b>8</b>."},
  {"q": "How many literals (letters, counting bars) are in the term ~A.B.~C.D?", "a": 4, "unit": "", "tol": 0.01, "hint": "One per variable.", "sol": "<b>4</b>."},
  {"q": "Using absorption, simplify A + A.B. How many literals remain?", "a": 1, "unit": "", "tol": 0.01, "hint": "The answer is A.", "sol": "<b>1</b>."},
  {"q": "~(A + B) = ~A . ~B. For A = 1 and B = 0, what is the value of the left-hand side?", "a": 0, "unit": "", "tol": 0.01, "hint": "1 + 0 = 1, then NOT.", "sol": "<b>0</b>."}]) + MCQ([
  ("What is ~(A . B) equal to?", ["~A . ~B", "~A + ~B", "A + B", "A . B"], 1, "Bar over AND becomes OR of barred terms."),
  ("A sum-of-products has a term for every row where the output is:", ["0", "1", "either", "neither"], 1, "The rows with output 1."),
  ("What does the absorption law say?", ["A + A.B = A", "A + A = 1", "A.A = 0", "A + 1 = A"], 0, "A + A.B = A."),
  ("Which is the same as ~~A?", ["~A", "A", "0", "1"], 1, "Double negation."),
  ("The annulment law says A + 1 equals:", ["A", "0", "1", "~A"], 2, "OR with 1 is always 1."),
  ("Which gate is the same as ~(A + B)?", ["AND", "NOR", "NAND", "XOR"], 1, "NOR.")], "qz1") + CARDS([
  ("Sum-of-products", "One AND term per 1 in the output, joined by OR."), ("De Morgan", "~(A+B) = ~A.~B and ~(A.B) = ~A+~B."), ("Double negation", "~~A = A."), ("Absorption", "A + A.B = A."),
  ("Distributive", "A.(B+C) = A.B + A.C."), ("Annulment", "A + 1 = 1 and A.0 = 0."), ("Inverse", "A.~A = 0 and A + ~A = 1."), ("Redundancy", "A + ~A.B = A + B.")])

build("ac1523", "ac-15-2-3-boolean-algebra", "Boolean Algebra and De Morgan", EYA("15.2.3"),
  "Sum-of-products from a truth table, the laws of Boolean algebra, De Morgan's laws and step-by-step simplification; animations, labs and the real Paper 3 questions from 2021 to 2026.",
  dict(sub=CBK("Chapter 15 · Hardware and virtual machines, section 15.2 Boolean algebra and logic circuits"), **tabs(learn, watch, explore, practise, real, exam, tips)), js)
