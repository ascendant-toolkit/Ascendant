"""A Level CS syllabus 15.2.1: logic gates and circuits, half adders and full adders. Run: python3 tools/artifact-kit/mk_ac1521.py"""
from ak15 import *

# ---- circuits (geometry shared by the static diagrams and the labs)
HA = circuit([("A", 24), ("B", 70)], [("S", "XOR", ["A", "B"], 0, 34), ("C", "AND", ["A", "B"], 0, 96)], outs=["S", "C"])
FA = circuit([("A", 22), ("B", 62), ("Cin", 118)],
             [("P", "XOR", ["A", "B"], 0, 40), ("Q", "AND", ["A", "B"], 0, 196), ("Sum", "XOR", ["P", "Cin"], 1, 74), ("R", "AND", ["P", "Cin"], 1, 140), ("Cout", "OR", ["R", "Q"], 2, 168)],
             outs=["Sum", "Cout"])
Q21 = circuit([("A", 22), ("B", 62), ("C", 118)], [("P", "XOR", ["A", "B"], 0, 40), ("Q", "AND", ["A", "B"], 0, 196), ("Y", "XOR", ["P", "C"], 1, 74), ("R", "AND", ["P", "C"], 1, 140), ("Z", "OR", ["R", "Q"], 2, 168)], outs=["Y", "Z"])
Q22 = circuit([("A", 24), ("B", 70)], [("E", "XOR", ["A", "B"], 0, 34), ("F", "AND", ["A", "B"], 0, 96)], outs=["E", "F"])
Q24 = circuit([("A", 20), ("B", 100), ("C", 190)],
              [("P", "NOT", ["B"], 0, 100), ("Q", "AND", ["A", "B", "C"], 1, 30), ("R", "AND", ["A", "P", "C"], 1, 110), ("S", "XOR", ["A", "P"], 1, 185), ("Z", "OR", ["Q", "R", "S"], 2, 110)], outs=["Z"])
Q23 = circuit([("A", 20), ("B", 56), ("C", 92), ("D", 160)], [("P", "NAND", ["A", "B", "C"], 0, 56), ("Q", "AND", ["P", "D"], 1, 128), ("Z", "XOR", ["P", "Q"], 2, 92)], outs=["Z"])
Q25 = circuit([("A", 20), ("B", 70), ("C", 150), ("D", 232)],
              [("P", "NOT", ["C"], 0, 150), ("Q", "NOR", ["A", "B", "P"], 1, 42), ("R", "AND", ["B", "C", "D"], 1, 222), ("S", "OR", ["Q", "P"], 2, 112), ("Z", "NOR", ["S", "R"], 3, 168)], outs=["Z"])


def gate_card(kind, expr):
    two = kind != "NOT"
    g = circuit([("A", 22), ("B", 42)] if two else [("A", 32)], [("X", kind, ["A", "B"] if two else ["A"], 0, 32)], outs=["X"], x0=84, colw=100)
    return f'<div class="card" style="text-align:center"><b>{kind}</b>' + circ_html(g, cap=kind + " gate") + f'<div class="bx">{ob(expr)}</div></div>'


def gate_table():
    rows = []
    for a in (0, 1):
        for b in (0, 1):
            rows.append([a, b, a & b, a | b, 1 - (a & b), 1 - (a | b), a ^ b])
    t = ttable(["A", "B"], ["AND", "OR", "NAND", "NOR", "XOR"], [r for r in rows])
    return t


def blank(names, cols, nrows=None, outs=0):
    """Truth table with inputs filled and everything else empty, as printed on the paper."""
    n = len(names)
    rows = [bits(m, n) + [""] * len(cols) for m in range(1 << n)]
    return ttable(names, cols, rows)


learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>A <b>logic gate</b> turns one or more binary inputs into one output; the Cambridge syllabus uses <b>NOT, AND, OR, NAND, NOR and XOR</b>. A <b>logic circuit</b> joins gates together and you work out its <b>truth table</b> one gate at a time, left to right. A <b>half adder</b> adds two bits using an <b>XOR</b> gate for the sum and an <b>AND</b> gate for the carry. A <b>full adder</b> adds two bits <b>and a carry in</b>, and is built from two half adders and an OR gate. Full adders chained together add whole binary numbers, carrying from one column to the next.</p></div>

  <h2>1 · The six gates</h2>
  <div class="grid3">''' + gate_card("NOT", "X = ~A") + gate_card("AND", "X = A.B") + gate_card("OR", "X = A+B") + gate_card("NAND", "X = ~(A.B)") + gate_card("NOR", "X = ~(A+B)") + gate_card("XOR", "X = A.~B + ~A.B") + '''</div>
  ''' + gate_table() + '''
  <p>NOT turns 0 into 1 and 1 into 0. AND is 1 only when <b>both</b> inputs are 1. OR is 1 when <b>at least one</b> input is 1. NAND and NOR are AND and OR followed by NOT. XOR is 1 when the inputs are <b>different</b>. A gate may have more than two inputs: a three-input AND is 1 only when all three are 1, and a three-input NOR is 1 only when all three are 0.</p>

  <h2>2 · Writing a truth table for a circuit</h2>
  <ol>
    <li>List every combination of the inputs in binary order: 2 inputs give 4 rows, 3 give 8, 4 give 16.</li>
    <li>Give every gate output a name (P, Q, R ...) and add a <b>working</b> column for each.</li>
    <li>Fill the columns in order from left to right, so a gate is only worked out after the gates that feed it.</li>
    <li>The last columns are the outputs. In the exam, one mark is usually for the working columns and the rest for the output column(s).</li>
  </ol>
  <p>A circuit with a NOT gate on an input behaves as if that input had been inverted first. A dot where wires meet means the signal is shared by both.</p>

  <h2>3 · The half adder</h2>
  <p>A half adder adds two single bits A and B and gives a <b>sum</b> S and a <b>carry</b> C:</p>
  ''' + circ_html(HA, cap="half adder") + circ_table(HA)[0] + '''
  <p>Sum: S = A XOR B. Carry: C = A AND B. In sum-of-products form, S = <span class="bx">~A.B + A.~B</span> and C = <span class="bx">A.B</span>. A half adder cannot accept a carry from a previous column, so it can only be used for the right-hand (least significant) column.</p>

  <h2>4 · The full adder</h2>
  <p>A full adder has three inputs: A, B and <b>Cin</b> (the carry from the previous column). It gives a <b>sum</b> and a <b>carry out</b> (Cout). It is two half adders and an OR gate: the first half adder adds A and B (P and Q), the second adds P to Cin (the sum and R), and the OR gate combines the two carries.</p>
  ''' + circ_html(FA, cap="full adder") + circ_table(FA, work=["P", "Q", "R"])[0] + '''
  <p>Sum = A XOR B XOR Cin, so Sum is 1 when an <b>odd number</b> of the three inputs are 1. Cout is 1 when <b>two or more</b> inputs are 1. As sum-of-products:</p>
  <ul>
    <li>Sum = ''' + bx(sop([1, 2, 4, 7], ["A", "B", "C"])) + '''</li>
    <li>Cout = ''' + bx(sop([3, 5, 6, 7], ["A", "B", "C"])) + '''</li>
  </ul>
  <p>Here C stands for the carry in (Cin).</p>

  <h2>5 · Adding binary numbers</h2>
  <p>To add two binary numbers, use a half adder for the rightmost column and a full adder for every other column, passing each carry out to the next column's carry in. This is a <b>ripple-carry adder</b>. Adding 0110 (6) and 0111 (7):</p>
  <div class="tw"><table class="t mono"><tr><th></th><th>bit 3</th><th>bit 2</th><th>bit 1</th><th>bit 0</th></tr>
    <tr><td>carry</td><td>0</td><td>1</td><td>1</td><td>·</td></tr>
    <tr><td>A</td><td>0</td><td>1</td><td>1</td><td>0</td></tr>
    <tr><td>B</td><td>0</td><td>1</td><td>1</td><td>1</td></tr>
    <tr><td><b>sum</b></td><td><b>1</b></td><td><b>1</b></td><td><b>0</b></td><td><b>1</b></td></tr></table></div>
  <p>1101 is 13. The carry out of the top bit signals overflow when the answer does not fit in the number of bits available.</p>

  <h2>6 · Common ways to lose marks</h2>
  <ul>
    <li>Working out an output before the gates that feed it. Fill the working columns from left to right.</li>
    <li>Confusing XOR with OR: XOR is 0 when both inputs are 1.</li>
    <li>Forgetting that a NOT gate on a wire inverts it for every gate that wire feeds after the NOT.</li>
    <li>Calling the full adder a "half adder" or the other way round. A half adder has two inputs and no carry in.</li>
    <li>Not saying what each output <b>means</b> when asked for its purpose: the XOR output is the <b>sum</b>, the AND output is the <b>carry</b>.</li>
    <li>Writing sum-of-products terms for the 0 rows instead of the 1 rows.</li>
  </ul>
'''

watch = '''
  <h2>1 · The half adder, four cases</h2>
  <p>Press Play or click the steps. Green wires carry a 1.</p>
  <div id="stA"></div>
  <h2>2 · The full adder, adding 1 + 1 + 1</h2>
  <div id="stB"></div>
  <h2>3 · A ripple-carry adder, 0110 + 0111</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Half adder</h2>
  <p>Click A and B to flip the inputs. The table highlights the row you are on.</p>
  <div class="card" id="labH"></div>
  <h2>Lab 2 · Full adder</h2>
  <div class="card" id="labF"></div>
  <h2>Lab 3 · Gate explorer</h2>
  <p>Choose a gate to see its truth table and when its output is 1.</p>
  <div class="card"><div id="gB" class="btnrow"></div><div id="gO"></div></div>
  <h2>Lab 4 · Four-bit ripple-carry adder</h2>
  <div class="card"><div id="rA"></div><div id="rB"></div><div id="rT"></div></div>
'''

practise = '''
  <h2>1 · Which gate?</h2><div id="cl1" class="card"></div>
  <h2>2 · Half adder or full adder?</h2><div id="cl2" class="card"></div>
  <h2>3 · Match the gate to its description</h2><div id="m1" class="card"></div>
  <h2>4 · Put the steps for a circuit's truth table in order</h2><div id="o1" class="card"></div>
  <h2>5 · Working out outputs</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("The calculator in your phone", "Inside the processor, an arithmetic logic unit adds numbers using adder circuits built from gates. Every addition you do on a screen is a chain of full adders.", "full adders chained make a ripple-carry adder.") +
rw("A light with two switches", "A landing light switched from the top and bottom of the stairs is on when exactly one switch is up. That is an XOR gate.", "XOR is 1 when the inputs are different.") +
rw("A car that will not start", "The engine starts only if the car is in park AND the brake is pressed. An AND gate makes a safe condition out of two inputs.", "AND is 1 only when every input is 1.") +
rw("A smoke alarm with a battery check", "The alarm sounds if smoke is detected OR the battery is low. OR gates combine conditions where either one is enough.", "OR is 1 when at least one input is 1.") +
rw("Checking data for errors", "Parity bits use XOR to count whether the number of 1s in a byte is odd or even, the same idea as the sum output of an adder.", "XOR of several inputs is 1 for an odd number of 1s.")
)

where = [
  ("M/J 2021", "31, 32, 33", "7", "3 + 1 + 4", "Full adder circuit: truth table with working, its name, and sum-of-products for each output with its purpose"),
  ("M/J 2022", "32", "6", "2 + 1 + 2", "Half adder circuit: truth table, name and purpose of each output"),
  ("O/N 2023", "31, 33", "6(a)", "3", "Truth table with working for a NAND / AND / XOR circuit with four inputs"),
  ("M/J 2024", "31", "6(a), (b)", "3 + 2", "Truth table with working for a circuit with NOT, AND, XOR and OR; sum-of-products"),
  ("M/J 2024", "32, 33", "6", "3 + 2", "A different circuit each in 32 and 33, same format (truth table, sum-of-products), then a K-map (see 15.2.4)"),
  ("M/J 2025", "32", "7(a), (b)", "3 + 1", "Truth table with working for a four-input circuit with NOT, NOR, AND and OR; sum-of-products"),
  ("O/N 2025", "31, 32", "6(a)", "3", "Truth table with working for a given circuit")]

past = '''  <p class="note">Circuit-reading questions appear in Paper 3 almost every series from May/June 2021 to Nov 2025. The circuits below are redrawn from the papers; the paper's own figure may look different but the gates and wiring are the same. Where the paper asks for a K-map next, that part is on the 15.2.4 page. Questions are reworded from the papers; check the original paper and mark scheme for the exact wording.</p>
''' + peq(SRC("s21", "31/32/33", "Q7"), "3 + 1 + 4 marks", "Complete / State / Write",
  "The diagram shows a logic circuit." + circ_html(Q21, cap="M/J 2021 Q7") + "(a) Complete the truth table for the given logic circuit. Show your working. (b) State the name of the logic circuit. (c) Write the Boolean expressions for the two outputs Y and Z in the truth table as sum-of-products and state the purpose of each output." + blank(["A", "B", "C"], ["P", "Q", "R", "Y", "Z"]),
  "Work out P, Q, R in turn, then Y and Z. Y is the sum and Z the carry out.",
  "<p><b>(a)</b> " + mks(["Working columns P, Q and R correct", "Column Y correct", "Column Z correct"]) + "</p>" + circ_table(Q21, work=["P", "Q", "R"], outs=["Y", "Z"])[0] + "<p><b>(b)</b> " + mks(["Full adder"], "a") + "</p><p><b>(c)</b> Y = " + bx("~A.~B.C + ~A.B.~C + A.~B.~C + A.B.C") + " " + mks(["Y: sum-of-products from the four rows where Y = 1", "Purpose of Y: the sum (of A, B and the carry in C)"]) + "<br>Z = " + bx("~A.B.C + A.~B.C + A.B.~C + A.B.C") + " " + mks(["Z: sum-of-products from the four rows where Z = 1", "Purpose of Z: the carry out"]) + "</p>",
  "Naming it a half adder. A half adder has two inputs; this circuit has three (A, B and the carry in C).") + peq(SRC("s22", "32", "Q6"), "2 + 1 + 2 marks", "Complete / State",
  "A logic circuit has two inputs A and B, and two outputs E and F." + circ_html(Q22, cap="M/J 2022 Q6") + "(a) Complete the truth table for this logic circuit. (b)(i) State the name of this logic circuit. (ii) State the purpose of each output E and F." + blank(["A", "B"], ["E", "F"]),
  "XOR on top, AND underneath: that is the half adder.",
  "<p><b>(a)</b> One mark per correct column: " + mks(["E: 0, 1, 1, 0"]) + " " + mks(["F: 0, 0, 0, 1"]) + "</p>" + circ_table(Q22)[0] + "<p><b>(b)(i)</b> " + mks(["Half adder"], "a") + "<br><b>(ii)</b> " + mks(["E is the sum"], "a") + " " + mks(["F is the carry"], "a") + "</p>", "Describing E as 'the answer' and F as 'the extra'. Use the words sum and carry.") + peq(SRC("w23", "31/33", "Q6(a)"), "3 marks", "Complete",
  "This diagram represents a logic circuit." + circ_html(Q23, cap="O/N 2023 Q6") + "Complete the truth table for the given logic circuit. (The paper prints sixteen rows with a working-space column; the rows are shown in full here.)" + blank(["A", "B", "C", "D"], ["P", "Q", "Z"]),
  "A four-input NAND, then an AND, then an XOR. Name the working columns P and Q.",
  "<p>One mark for every shaded block of rows of column Z that is correct (max 3). Z is 1 for every row where D = 0 except the last (A = B = C = 1).</p>" + circ_table(Q23, work=["P", "Q"], outs=["Z"])[0], "Treating the first gate as AND. It has a bubble: it is NAND, so its output is 0 only when A, B and C are all 1.") + peq(SRC("s24", "31", "Q6(a)(b)"), "3 + 2 marks", "Complete / Write",
  "The diagram shows a logic circuit." + circ_html(Q24, cap="M/J 2024 Q6") + "(a) Complete the truth table for the given logic circuit. Show your working. (b) Write the Boolean expression that corresponds to the logic circuit as a sum-of-products." + blank(["A", "B", "C"], ["P", "Q", "R", "S", "Z"]),
  "P is the NOT of B. Q, R and S each use A, then Z is an OR of all three.",
  "<p><b>(a)</b> " + mks(["All four working columns P, Q, R and S correct", "First four rows of Z correct", "Second four rows of Z correct"]) + "</p>" + circ_table(Q24, work=["P", "Q", "R", "S"], outs=["Z"])[0] + "<p><b>(b)</b> Z = " + bx(sop([0, 1, 5, 6, 7], ["A", "B", "C"])) + " " + mks(["Two marks for all five terms and no extras; one mark for any three terms"]) + "</p>", "Writing a term for the 0 rows. Sum-of-products uses the rows where Z is 1.") + peq(SRC("s25", "32", "Q7(a)(b)"), "3 + 1 marks", "Complete / Write",
  "The diagram shows a logic circuit." + circ_html(Q25, cap="M/J 2025 Q7") + "(a) Complete the truth table for the given logic circuit. Show your working. (b) Write the Boolean logic expression that corresponds to the given logic circuit as the sum-of-products." + blank(["A", "B", "C", "D"], ["P", "Q", "R", "S", "Z"]),
  "P = NOT C. Q is a three-input NOR of A, B and P. R is an AND. S is an OR. Z is a NOR of S and R.",
  "<p><b>(a)</b> " + mks(["Working columns P, Q, R and S correct", "First eight rows of Z correct", "Second eight rows of Z correct"]) + "</p>" + circ_table(Q25, work=["P", "Q", "R", "S"], outs=["Z"])[0] + "<p><b>(b)</b> Z = " + bx(sop([6, 10, 11, 14], ["A", "B", "C", "D"])) + " " + mks(["All four terms correct (any order)"]) + "</p>", "Missing the three-input NOR: it is 1 only when all of A, B and P are 0.")

review = req("2 marks", "State", "State the name of the logic gate whose output is 1 only when its inputs are different, and give its output when both inputs are 1.", "XOR.", "<p>" + mks(["XOR (exclusive OR)", "Output 0 when both inputs are 1"]) + "</p>", None) + req("3 marks", "Complete", "A half adder adds the bits A = 1 and B = 1. State the sum and carry outputs, and the decimal value they represent.", "Sum is XOR, carry is AND.", "<p>" + mks(["Sum = 1 XOR 1 = 0", "Carry = 1 AND 1 = 1", "The outputs 10 represent decimal 2"]) + "</p>", None) + req("4 marks", "Explain", "Explain why a full adder is needed for every column of a binary addition except the first.", "Think about the carry.", "<p>" + mks(["Each column after the first may receive a carry from the column to its right", "A half adder only has two inputs, so it cannot accept that carry in", "A full adder has a third input, the carry in, as well as A and B", "Its carry out is passed to the next column (ripple carry)"]) + "</p>", None) + req("3 marks", "Show", "A full adder has A = 1, B = 0 and Cin = 1. Show the values of P, Q and R in the circuit above, then the sum and carry out.", "P = A XOR B, Q = A AND B, R = P AND Cin.", "<p>" + mks(["P = 1 XOR 0 = 1, Q = 1 AND 0 = 0", "R = 1 AND 1 = 1; Sum = P XOR Cin = 0", "Cout = R OR Q = 1"]) + "</p>", None) + req("3 marks", "Complete", "A circuit has inputs A and B. X = (A NAND B) AND (A OR B). Complete its truth table and name the gate it behaves as.", "Work out each bracket first.", "<p>" + mks(["A NAND B: 1, 1, 1, 0 for AB = 00, 01, 10, 11; A OR B: 0, 1, 1, 1", "X: 0, 1, 1, 0", "It behaves as an XOR gate"]) + "</p>", None)

exam = exam20("Part 1 is real 9618 questions on reading logic circuits and the half and full adders (Paper 3), 2021 to 2025. Part 2 is a set of review questions for practice; they are not in exam format.", where, past, review)

tips = tips_html([
  ("Name the wires.", "Give every gate output a letter and add a working column for it."),
  ("Work left to right.", "Never fill an output column before the gates that feed it."),
  ("Look for bubbles.", "A circle on a gate means NOT after it: NAND, NOR and XNOR."),
  ("Sum and carry.", "XOR gives the sum, AND gives the carry. A full adder adds a carry in."),
  ("Sum-of-products uses the 1 rows.", "One AND term per row where the output is 1, joined by OR."),
  ("Count the rows.", "2 inputs 4 rows, 3 inputs 8 rows, 4 inputs 16 rows."),
], [
  ("a half adder", "Two inputs: the sum is A XOR B and the carry is A AND B."),
  ("a full adder", "Three inputs A, B and carry in: the sum is the XOR of all three and the carry out is 1 when two or more inputs are 1."),
  ("a ripple-carry adder", "Full adders in a chain, each carry out feeding the next carry in."),
], [("State / Identify", "Give the name or value only."), ("Complete", "Fill in the table; show working columns."), ("Write", "Give the expression in the form asked."), ("Explain", "Give the reason as well.")]) + FC

js = AKJS + AK20JS + AK15JS + "const GH = " + gjson(HA) + ", GF = " + gjson(FA) + ";\n" + r'''
(function () {
  const cases = [[0, 0], [0, 1], [1, 0], [1, 1]];
  const draw = (s) => { const [a, b] = cases[Math.round(s.i)]; const v = circEval(GH, { A: a, B: b }); return circFit(GH, v, 560, { vals: true }); };
  Lib.stepper($("#stA"), { w: 560, h: Math.round(GH.h * 2.2) + 12, label: "Half adder", base: { i: 0 }, draw, tween: 150, dwell: 2200, steps: cases.map(([a, b], i) => ({ cap: `A = ${a}, B = ${b}: sum = ${a} XOR ${b} = <b>${a ^ b}</b>, carry = ${a} AND ${b} = <b>${a & b}</b>. ` + (i === 3 ? "Binary 1 + 1 = 10: the sum bit is 0 and a 1 is carried." : i === 0 ? "Nothing to add, nothing to carry." : "Only one input is 1: sum 1, no carry."), s: { i } })) });
})();
(function () {
  const draw = (s) => { const v = circEval(GF, { A: 1, B: 1, Cin: 1 }); const k = Math.round(s.i), show = {}; ["A", "B", "Cin"].forEach((n) => show[n] = 1);
    const on = { 0: [], 1: ["P", "Q"], 2: ["P", "Q", "R", "Sum"], 3: ["P", "Q", "R", "Sum", "Cout"] }[k]; Object.keys(v).forEach((n) => { if (!["A", "B", "Cin"].includes(n) && !on.includes(n)) v[n] = 0; }); return circFit(GF, v, 620, { vals: true }); };
  Lib.stepper($("#stB"), { w: 620, h: Math.round(GF.h * Math.min(2.2, 600 / GF.w)) + 12, label: "Full adder", base: { i: 0 }, draw, tween: 150, dwell: 2600, steps: [
    { cap: "Inputs A = 1, B = 1 and carry in = 1.", s: { i: 0 } },
    { cap: "The first half adder: P = 1 XOR 1 = <b>0</b>, Q = 1 AND 1 = <b>1</b>.", s: { i: 1 } },
    { cap: "The second half adder adds P and the carry in: Sum = 0 XOR 1 = <b>1</b>, R = 0 AND 1 = <b>0</b>.", s: { i: 2 } },
    { cap: "The OR gate combines the carries: carry out = R OR Q = 0 OR 1 = <b>1</b>. Result 11 (binary), which is 3: 1 + 1 + 1 = 3.", s: { i: 3 } }] });
})();
(function () {
  const A = [0, 1, 1, 0], B = [0, 1, 1, 1];
  const draw = (s) => {
    const k = Math.round(s.i); let o = "", c = 0; const sums = [], cs = [];
    for (let i = 3; i >= 0; i--) { const t = A[i] + B[i] + c; sums[i] = t % 2; c = t >> 1; cs[i] = c; }
    const lab = ["bit 3", "bit 2", "bit 1", "bit 0"];
    [0, 1, 2, 3].forEach((i) => { const x = 50 + i * 150; o += SV.text(x + 40, 18, lab[i], "sm", { "text-anchor": "middle" }); const col = 3 - i; const doneCol = k > col;
      o += SV.rect(x, 30, 80, 38, "cell", { rx: 6 }) + SV.text(x + 40, 56, "A " + A[i], "lbl bd", { "text-anchor": "middle" });
      o += SV.rect(x, 76, 80, 38, "cell", { rx: 6 }) + SV.text(x + 40, 102, "B " + B[i], "lbl bd", { "text-anchor": "middle" });
      o += SV.rect(x, 130, 80, 40, doneCol ? "cell-ok" : (k === col ? "cell-warn" : "cell"), { rx: 6 }) + (doneCol || k === col ? SV.text(x + 40, 156, "sum " + sums[i], "lbl bd", { "text-anchor": "middle" }) : "");
      if (doneCol || k === col) o += SV.text(x - 14, 150, cs[i] ? "carry " + cs[i] + " ←" : "", "sm t3", { "text-anchor": "end" });
    });
    o += SV.text(14, 56, "", "sm"); if (k > 3) o += SV.text(50, 205, "0110 + 0111 = 1101 (6 + 7 = 13)", "lbl bd t3");
    return o;
  };
  Lib.stepper($("#stC"), { w: 700, h: 225, label: "Ripple-carry addition", base: { i: 0 }, draw, tween: 150, dwell: 2600, steps: [
    { cap: "Add 0110 and 0111 one column at a time, starting on the right. Bit 0 uses a half adder.", s: { i: 0 } },
    { cap: "Bit 0: 0 + 1 = 1, no carry.", s: { i: 1 } }, { cap: "Bit 1: 1 + 1 + carry 0 = 0, <b>carry 1</b> into bit 2.", s: { i: 2 } },
    { cap: "Bit 2: 1 + 1 + carry 1 = 1, <b>carry 1</b> into bit 3.", s: { i: 3 } }, { cap: "Bit 3: 0 + 0 + carry 1 = 1, no further carry. The answer is 1101.", s: { i: 4 } }] });
})();

circLab("#labH", GH, [], ["S", "C"]);
circLab("#labF", GF, ["P", "Q", "R"], ["Sum", "Cout"]);

btnTable("gB", "gO", [
  ["NOT", "1 when the input is 0", "0 0→1, 1→0", "One input only"],
  ["AND", "1 only when both inputs are 1", "0 0 0 1", "Both"],
  ["OR", "1 when at least one input is 1", "0 1 1 1", "Either"],
  ["NAND", "0 only when both inputs are 1", "1 1 1 0", "AND then NOT"],
  ["NOR", "1 only when both inputs are 0", "1 0 0 0", "OR then NOT"],
  ["XOR", "1 when the inputs are different", "0 1 1 0", "Different"]
], ["Gate", "Output is 1 when", "Output for AB = 00, 01, 10, 11", "Remember"]);

(function () {
  let a = 6, b = 7;
  const paint = () => {
    const ab = bin(a, 4), bb = bin(b, 4); let c = 0, h = '<div class="tw"><table class="t mono"><tr><th></th><th>bit 3</th><th>bit 2</th><th>bit 1</th><th>bit 0</th></tr>';
    const sums = [], cs = [0, 0, 0, 0, 0];
    for (let i = 3; i >= 0; i--) { const t = +ab[i] + +bb[i] + c; sums[i] = t % 2; c = t >> 1; cs[i] = c; }
    h += "<tr><td>carry out</td>" + [0, 1, 2, 3].map((i) => `<td>${cs[i]}</td>`).join("") + "</tr>";
    h += "<tr><td>A</td>" + ab.split("").map((x) => `<td>${x}</td>`).join("") + "</tr><tr><td>B</td>" + bb.split("").map((x) => `<td>${x}</td>`).join("") + "</tr>";
    h += "<tr><td><b>sum</b></td>" + sums.map((x) => `<td><b>${x}</b></td>`).join("") + "</tr></table></div>";
    $("#rT").innerHTML = h + `<div class="verdict">${a} + ${b} = ${a + b}. Four bits show ${sums.join("")} (${parseInt(sums.join(""), 2)})` + (a + b > 15 ? `. <b>Overflow</b>: the carry out of bit 3 is 1, so the true answer needs a fifth bit.` : ".") + "</div>";
  };
  Lib.slider($("#rA"), { id: "ra", label: "A ", min: 0, max: 15, value: a, fmt: (x) => x + " = " + bin(x, 4), onInput: (v) => { a = v; paint(); } });
  Lib.slider($("#rB"), { id: "rb", label: "B ", min: 0, max: 15, value: b, fmt: (x) => x + " = " + bin(x, 4), onInput: (v) => { b = v; paint(); } }); paint();
})();
''' + CLASSIFY("cl1", "Which gate does the description give?", ["AND", "OR", "XOR", "NAND"],
  [("Output is 1 only when both inputs are 1", 0), ("Output is 1 when at least one input is 1", 1), ("Output is 1 when the inputs are different", 2), ("Output is 0 only when both inputs are 1", 3), ("A light that is on when the car is in park and the brake is pressed", 0), ("An alarm that sounds if either door is open", 1)],
  "AND all, OR any, XOR different, NAND the opposite of AND.") + CLASSIFY("cl2", "Which circuit has this property?", ["Half adder", "Full adder"],
  [("Has three inputs", 1), ("Has two inputs", 0), ("Is built from two half adders and an OR gate", 1), ("Is built from an XOR gate and an AND gate", 0), ("Has a carry in", 1), ("Used for the least significant column only", 0)],
  "A half adder has no carry in. A full adder does.") + MATCH([
  ["XOR", "1 when the inputs are different"], ["NAND", "AND followed by NOT"], ["Half adder", "Sum is A XOR B, carry is A AND B"], ["Full adder", "Adds A, B and a carry in"], ["Ripple carry", "Each carry out feeds the next carry in"]]) + ORDER(
  "Put the steps for finding a truth table in order.",
  ["List every combination of the inputs", "Name the output of each gate and add a working column", "Fill the working columns from left to right", "Read the output column(s) from the final gates"],
  "Rows, names, working, outputs.") + CALC([
  {"q": "A full adder has A = 1, B = 1 and Cin = 0. What is the sum bit?", "a": 0, "unit": "", "tol": 0.01, "hint": "1 XOR 1 XOR 0.", "sol": "<b>0</b>."},
  {"q": "The same inputs: what is the carry out?", "a": 1, "unit": "", "tol": 0.01, "hint": "Two inputs are 1.", "sol": "<b>1</b>."},
  {"q": "A full adder has A = 1, B = 1 and Cin = 1. What is the sum bit?", "a": 1, "unit": "", "tol": 0.01, "hint": "Three 1s is an odd number.", "sol": "<b>1</b>."},
  {"q": "How many rows does the truth table of a circuit with four inputs have?", "a": 16, "unit": "", "tol": 0.01, "hint": "2 to the power 4.", "sol": "<b>16</b>."},
  {"q": "Adding 0111 and 0001 with a ripple-carry adder: how many columns produce a carry out?", "a": 3, "unit": "", "tol": 0.01, "hint": "Bits 0, 1 and 2 each carry.", "sol": "<b>3</b>: the answer is 1000."}]) + MCQ([
  ("Which gate gives 1 for the inputs 0 and 1 but 0 for 1 and 1?", ["OR", "XOR", "NAND", "AND"], 1, "XOR."),
  ("What does the AND gate in a half adder produce?", ["The sum", "The carry", "The inverse of the sum", "The overflow"], 1, "The carry."),
  ("How many inputs does a full adder have?", ["2", "3", "4", "1"], 1, "A, B and the carry in."),
  ("A NOR gate outputs 1 when:", ["Both inputs are 1", "At least one input is 1", "Both inputs are 0", "The inputs differ"], 2, "NOR is NOT (A OR B)."),
  ("In a ripple-carry adder the carry out of one column goes to:", ["The sum output", "The next column's carry in", "Memory", "The same column"], 1, "It ripples to the next column."),
  ("In a truth table, a working column is used for:", ["The final output only", "The output of a gate inside the circuit", "The input labels", "The number of rows"], 1, "Intermediate gate outputs.")], "qz1") + CARDS([
  ("NOT", "Inverts the input."), ("AND", "1 only when all inputs are 1."), ("OR", "1 when at least one input is 1."), ("XOR", "1 when the inputs are different."),
  ("NAND / NOR", "AND / OR followed by NOT."), ("Half adder", "Sum = A XOR B, carry = A AND B."), ("Full adder", "Sum = A XOR B XOR Cin; carry out when two or more inputs are 1."), ("Ripple carry", "Chain of full adders, carry out to carry in.")])

build("ac1521", "ac-15-2-1-logic-circuits-adders", "Logic Circuits and Adders", EYA("15.2.1"),
  "The six logic gates, how to write a truth table for a circuit, and the half adder and full adder; animations, adder labs and the real Paper 3 circuit questions from 2021 to 2025.",
  dict(sub=CBK("Chapter 15 · Hardware and virtual machines, section 15.2 Boolean algebra and logic circuits"), **tabs(learn, watch, explore, practise, real, exam, tips)), js)
