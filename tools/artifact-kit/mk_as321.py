"""AS CS 3.2.1: logic gates and logic circuits. Run: python3 tools/artifact-kit/mk_as321.py"""
from ak321 import *

ABC = ["A", "B", "C"]
def cx(t, ins, exp, tag, out="X"):
    check(t, ins, exp, tag)
    return net(t, ins, out)

# ---- exam expressions (each truth table is checked against the published mark scheme)
S21 = XOR(AND("A", "B", "C"), "A"); S21 = OR(AND("A", "B", "C"), XOR("B", "C"))
G_S21 = cx(S21, ABC, [0, 1, 1, 0, 0, 1, 1, 1], "s21 12 Q3", "S")
W21 = NAND(NAND("A", "B"), "C")
G_W21 = cx(W21, ABC, [1, 1, 1, 1, 1, 1, 0, 1][:0] or table(W21, ABC), "w21 12 Q2b", "X")
W22A = NOT(OR(AND(NOT("A"), NOT("B")), AND(NOT("B"), NOT("C"))))
G_W22A = cx(W22A, ABC, [0, 0, 1, 1, 0, 1, 1, 1], "w22 11 Q3", "X")
GREEN = AND("T", NOT("W"), OR(NOT("R"), NOT("M")))
G_GREEN = net(GREEN, ["T", "W", "R", "M"], "X")
W22B = AND(NOT(OR("A", "B", "C")), NOR("B", "C"))
check(W22B, ABC, [1, 0, 0, 0, 0, 0, 0, 0], "w22 12 Q3b")
W22C = NOT(OR(NOT(AND("A", "B")), NOT(AND("B", "C"))))
G_W22C = net(W22C, ABC, "X")
W22D = OR(AND(NOT("P"), "Q"), AND("Q", NOT("R"))); PQR = ["P", "Q", "R"]
check(W22D, PQR, [0, 0, 1, 1, 0, 0, 1, 0], "w22 13 Q5b")
S22 = AND(XOR("A", "B"), NOT("C"))
check(S22, ABC, [0, 0, 1, 0, 1, 0, 0, 0], "s22 12 Q7")
S23A = XOR(OR(NOT("A"), "B"), NAND("C", "D"))
G_S23A = net(S23A, ["A", "B", "C", "D"], "T")
S23B = AND(XOR("R", "S"), NOR(NOT("T"), "P"))
G_S23B = net(S23B, ["R", "S", "T", "P"], "Z")
S23C = XOR(OR(NOT("P"), "Q"), NOR("R", "Q"))
check(S23C, PQR, [0, 1, 1, 1, 1, 0, 1, 1], "s23 12 Q6b")
W23A = XOR(NOT(NAND("A", "B")), AND(NOT("B"), NOR("B", "C")))
check(W23A, ABC, [1, 0, 0, 0, 1, 0, 1, 1], "w23 11 Q4a")
W23B = AND(AND("A", NOT(OR("B", "C"))), NOR("B", "C"))
G_W23B = net(W23B, ABC, "X")
W23C = AND(XOR(AND("P", "Q"), OR(NOT("Q"), "R")), NOT("P"))
check(W23C, PQR, [1, 1, 0, 1, 0, 0, 0, 0], "w23 13 Q4a")
G_W23C = net(W23C, PQR, "Y")
W24A = NAND(XOR("A", "B"), AND("A", XOR("B", "C")))
check(W24A, ABC, [1, 1, 1, 1, 1, 0, 1, 1], "w24 12 Q1a")
W24B = NAND("P", XOR(OR("Q", NOT("R")), XOR("P", "Q")))
G_W24B = net(W24B, PQR, "W")
W24C = AND(OR(AND(NOT("A"), AND("B", "C")), NAND("B", "C")), NOT("A"))
G_W24C = net(W24C, ABC, "X")
W25A = NOT(XOR(NAND("A", "B"), OR(NOT("A"), NOT("C"))))
G_W25A = net(W25A, ABC, "X")
W25B = NAND(NOR("A", "B"), XOR("C", "B"))
W25C = NOT(AND(OR(AND("A", "B"), "C"), NOR("C", "D")))
G_W25C = net(W25C, ["A", "B", "C", "D"], "X")
S24D = NOT(OR(AND("A", "B"), AND("C", "D")))
G_S24D = net(S24D, ["A", "B", "C", "D"], "X")
# s24 13 Q6 matching check
M1 = AND(OR("A", "C"), NOT("B")); M2 = AND(NOT(XOR("A", "B")), "C"); M3 = OR(NAND("A", "B"), "C")
check(M1, ABC, [0, 1, 0, 0, 1, 1, 0, 0], "s24 13 Q6 t1")
check(M2, ABC, [0, 1, 0, 0, 0, 0, 0, 1], "s24 13 Q6 t2")
check(M3, ABC, [1, 1, 1, 1, 1, 1, 0, 1], "s24 13 Q6 t3")
# demo circuits
DEM = AND(XOR("A", "B"), NOT("C")); G_DEM = net(DEM, ABC, "X")

def tt(t, ins, out="X", work=None):
    return ttab(t, ins, out)

def expl(label, exp, ins, out="X"):
    g = net(exp, ins, out)
    return circ_html(g, cap=label)

def blanks(names, out="X"):
    return ttable(names, ["Working space", out], [bits(m, len(names)) + ["", ""] for m in range(1 << len(names))])

def gate_card(kind, expr):
    two = kind != "NOT"
    g = circuit([("A", 22), ("B", 42)] if two else [("A", 32)], [("X", kind, ["A", "B"] if two else ["A"], 0, 32)], outs=["X"], x0=84, colw=100)
    return f'<div class="card" style="text-align:center"><b>{kind}</b>' + circ_html(g, cap=kind + " gate") + f'<div class="bx">{expr}</div></div>'

gt = ttable(["A", "B"], ["AND", "OR", "NAND", "NOR", "XOR"], [[a, b, a & b, a | b, 1 - (a & b), 1 - (a | b), a ^ b] for a in (0, 1) for b in (0, 1)])

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>A <b>logic gate</b> turns binary inputs into one output; the syllabus uses <b>NOT, AND, OR, NAND, NOR and XOR</b>. A <b>logic circuit</b> joins gates together; you can work out its output with a <b>truth table</b> whose <b>working space</b> column holds an intermediate result. You must be able to <b>draw a circuit from a logic expression</b>, <b>write the expression for a circuit</b> and <b>complete a truth table</b> in either direction. Work in a fixed order: inner brackets first, NOT before AND, and every gate of the expression becomes exactly one gate in the diagram. Logic circuits are used in monitoring and control systems, in memory and in the ALU.</p></div>

  <h2>1 · The six gates</h2>
  <div class="grid3">''' + gate_card("NOT", "X = NOT A") + gate_card("AND", "X = A AND B") + gate_card("OR", "X = A OR B") + gate_card("NAND", "X = A NAND B") + gate_card("NOR", "X = A NOR B") + gate_card("XOR", "X = A XOR B") + '''</div>
  ''' + gt + '''
  <p>Say it in words, as the mark schemes do: <b>NOT</b> inverts. <b>AND</b>: output is 1 only when both inputs are 1. <b>OR</b>: output is 0 only when both inputs are 0, otherwise 1. <b>NAND</b>: output is 0 when both inputs are 1, otherwise 1. <b>NOR</b>: output is 1 when both inputs are 0, otherwise 0. <b>XOR</b>: output is 1 when one input is 1 and the other is 0, that is when the inputs are different, otherwise 0. AND and OR can have more than two inputs, for example A AND B AND C is 1 only when all three are 1.</p>

  <h2>2 · Completing a truth table</h2>
  <ol>
    <li>List every input combination in binary order: 2 inputs give 4 rows, 3 give 8, 4 give 16.</li>
    <li>Split the expression into its parts and put each part in the <b>working space</b>.</li>
    <li>Work out the innermost brackets first, then combine them, applying NOT to a term as soon as it appears.</li>
    <li>Write the final column. The paper gives one mark for each half of the rows, so errors in the middle of the table can cost a mark.</li>
  </ol>
  <p>Example: X = (A XOR B) AND NOT C. A XOR B is 1 when A and B differ. NOT C is 1 when C is 0. X is 1 only for the rows 010 and 100.</p>
  ''' + tt(DEM, ABC) + '''

  <h2>3 · Drawing a circuit from an expression</h2>
  <p>Each operator in the expression becomes a gate, and the brackets show which gate feeds which. Start from the <b>outermost</b> operator: it is the last gate. Work inwards, drawing the gates that feed it. Every gate gets inputs from the inputs or from the gates inside its brackets. Example: X = (A XOR B) AND NOT C has three gates: an XOR on A and B, a NOT on C, and an AND of the two results.</p>
  ''' + circ_html(G_DEM, cap="X = (A XOR B) AND NOT C") + '''
  <p>Mark schemes award marks for <b>each correct gate with correct inputs</b> and for <b>no superfluous gates</b>. Draw every NOT as its own gate (or a bubble if you are sure), keep the labels A, B and C on the left and X on the right.</p>

  <h2>4 · Writing an expression from a circuit or a truth table</h2>
  <p>From a circuit: work from the left, writing each gate's expression with brackets, and substitute it into the next gate. From a truth table, take each row where the output is 1, write an AND term (use NOT for any input that is 0), and join the terms with OR. For R S T with output 1 only at 001 and 110, Q = (NOT R AND NOT S AND T) OR (R AND S AND NOT T).</p>

  <h2>5 · Logic in context</h2>
  <p>Conditions in the scenario map directly onto gates. Take a greenhouse window X that opens if the temperature is too high (T) and the wind speed is acceptable (W = 0) and either rain is not detected (R = 0) or the manual override is off (M = 0). Then X = T AND NOT W AND (NOT R OR NOT M).</p>
  ''' + circ_html(G_GREEN, cap="greenhouse window") + '''

  <h2>Common ways to lose marks</h2>
  <ul>
    <li>Treating XOR as OR: XOR is 0 when both inputs are 1.</li>
    <li>Forgetting a NOT in the middle of the expression. Put every NOT in the working space.</li>
    <li>Drawing a gate for a bracket that does not exist, or skipping a gate: count the operators and the gates.</li>
    <li>Describing a gate as "it outputs 1 if A and B". Use the exact conditions for both 0 and 1 outputs.</li>
    <li>Leaving out the brackets when writing an expression from a circuit.</li>
  </ul>
'''

watch = '''
  <h2>1 · Evaluating X = (A XOR B) AND NOT C</h2>
  <p>Press Play. Green wires carry a 1.</p>
  <div id="stA"></div>
  <h2>2 · The greenhouse window</h2>
  <div id="stB"></div>
  <h2>3 · From expression to circuit</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Toggle the inputs</h2>
  <p>Click the inputs of the circuit X = (A XOR B) AND NOT C. The row you are on is highlighted.</p>
  <div class="card" id="labD"></div>
  <h2>Lab 2 · The greenhouse window</h2>
  <div class="card" id="labG"></div>
  <h2>Lab 3 · Gate explorer</h2>
  <div class="card"><div id="gB" class="btnrow"></div><div id="gO"></div></div>
'''

_pr, _prjs = PR(["Which gate?", "Is the output 1?", "Match the gate to its description", "Put the circuit-drawing steps in order", "Working out", "Multiple choice"],
  ("Which gate does the description give?", ["AND", "OR", "XOR", "NAND", "NOR"], [("Output is 1 only when both inputs are 1", 0), ("Output is 0 only when both inputs are 0", 1), ("Output is 1 when the inputs are different", 2), ("Output is 0 only when both inputs are 1", 3), ("Output is 1 only when both inputs are 0", 4), ("A car starts only if the key is turned AND the brake is pressed", 0)], "AND all, OR any, XOR different, NAND not AND, NOR not OR."),
  ("Is the output of X = (A XOR B) AND NOT C equal to 1 or 0?", ["X = 1", "X = 0"], [("A=0, B=1, C=0", 0), ("A=1, B=1, C=0", 1), ("A=1, B=0, C=0", 0), ("A=0, B=1, C=1", 1), ("A=0, B=0, C=0", 1), ("A=1, B=0, C=1", 1)], "The inputs must differ and C must be 0."),
  [["NAND", "Output is 0 when both inputs are 1, otherwise 1"], ["NOR", "Output is 1 when both inputs are 0, otherwise 0"], ["XOR", "Output is 1 when the inputs are different"], ["OR", "Output is 0 when both inputs are 0, otherwise 1"], ["NOT", "Output is the opposite of the input"]],
  ("Put the steps for drawing a circuit from an expression in order.", ["Identify the outermost operator: it is the final gate", "Draw the gates for the brackets that feed it", "Connect each gate to its inputs or to the gates inside its brackets", "Add every NOT as a gate on the correct wire", "Check that the number of gates equals the number of operators"], "Outermost, inner, connect, NOT, count."),
  [{"q": "How many rows does the truth table for a 4-input circuit have?", "a": 16, "unit": "", "tol": 0.01, "hint": "2^4.", "sol": "<b>16</b>."}, {"q": "In X = (A XOR B) AND NOT C, for how many of the 8 rows is X = 1?", "a": 2, "unit": "", "tol": 0.01, "hint": "010 and 100.", "sol": "<b>2</b>."}, {"q": "How many gates are in the circuit for X = NOT ((A AND B) OR (C AND D))?", "a": 4, "unit": "", "tol": 0.01, "hint": "Two ANDs, one OR, one NOT.", "sol": "<b>4</b>."}, {"q": "For A=1, B=1 what is A NAND B (1 or 0)?", "a": 0, "unit": "", "tol": 0.01, "hint": "AND is 1, then NOT.", "sol": "<b>0</b>."}, {"q": "A 3-input AND gate is given 1, 1, 0. What is the output?", "a": 0, "unit": "", "tol": 0.01, "hint": "All must be 1.", "sol": "<b>0</b>."}],
  [("Which gate gives 1 for different inputs?", ["XOR", "AND", "NOR", "NAND"], 0, "XOR."), ("NOR outputs 1 when:", ["Both inputs are 0", "Both are 1", "Either input is 1", "Inputs differ"], 0, "Both inputs 0."), ("How many gates are needed for X = (A AND B) OR NOT C?", ["3", "2", "4", "1"], 0, "AND, NOT, OR."), ("NAND is the same as:", ["AND followed by NOT", "OR followed by NOT", "XOR", "NOT followed by AND"], 0, "AND then NOT."), ("The working space column is used for:", ["Intermediate results", "The final answer only", "Input names", "Row numbers"], 0, "Intermediate values."), ("Which expression is 1 only for 001 and 111?", ["NOT (A XOR B) AND C", "A OR C", "A NAND B", "NOT C"], 0, "A equals B and C is 1.")],
  [("NOT", "Inverts."), ("AND", "1 only if all inputs are 1."), ("OR", "0 only if all inputs are 0."), ("XOR", "1 if the inputs differ."), ("NAND", "0 only if both inputs are 1."), ("NOR", "1 only if both inputs are 0."), ("Truth table", "Every input combination and the output."), ("Working space", "Holds intermediate results.")])

real = RWNOTE + (
rw("A two-way light switch", "A light on a landing is on if exactly one of two switches is up. That is an XOR gate: the output is 1 when the inputs are different.", "XOR.") +
rw("A car that will not start", "The engine starts only if the car is in park AND the brake is pressed. An AND gate makes a safe condition out of two inputs.", "AND.") +
rw("A smoke alarm", "The alarm sounds if smoke is detected OR the battery is low. OR combines conditions where either is enough.", "OR.") +
rw("A machine guard", "A press works only when neither of two guard sensors is triggered: NOR is 1 only when both inputs are 0.", "NOR.") +
rw("Computer memory and the processor", "Every flip-flop in SRAM and every adder in the ALU is built from gates.", "logic circuits are the basis of hardware.")
)

where = [
  ("M/J 2021", "11, 13", "8", "3", "Tick the gate that each statement describes"),
  ("M/J 2021", "12", "3", "4 + 2", "Draw the circuit for S = (A AND B AND C) OR (B XOR C) and complete its truth table"),
  ("O/N 2021", "12", "2(a), (b)", "2 + 2", "Truth tables for NOR and NAND; draw a circuit"),
  ("M/J 2022", "12", "7", "2", "Truth table for X = (A XOR B) AND NOT C"),
  ("O/N 2022", "11", "3", "2 + 2", "Draw the circuit and complete the truth table"),
  ("O/N 2022", "12", "3(a), (b)", "3 + 2", "The greenhouse window circuit; a truth table"),
  ("O/N 2022", "13", "5", "3 + 2", "Draw a circuit; complete a truth table"),
  ("M/J 2023", "11", "5", "2 + 2", "Draw a circuit; describe NAND and NOR"),
  ("M/J 2023", "12", "6", "2 + 2", "Draw a circuit; complete a truth table"),
  ("O/N 2023", "11", "4", "2 + 2", "Truth table; draw a circuit"),
  ("O/N 2023", "13", "4", "2 + 2", "Truth table; draw a circuit"),
  ("M/J 2024", "12", "1", "4 + 2", "Describe four gates; draw a circuit"),
  ("M/J 2024", "13", "6", "3", "Match truth tables to logic expressions"),
  ("O/N 2024", "12", "1", "2 + 2", "Truth table; draw a circuit"),
  ("O/N 2024", "13", "1", "1 + 2 + 2", "Describe XOR; write an expression; draw a circuit"),
  ("M/J 2025", "11, 12, 13", "1, 4, 4", "varies", "Write logic expressions for a circuit (the circuit figure is in the paper)"),
  ("O/N 2025", "11", "3", "2 + 2", "Draw a circuit; write an expression from a truth table"),
  ("O/N 2025", "13", "3", "2 + 2", "Truth table; draw a circuit"),
  ("M/J 2026", "11, 12, 13", "6, 8, 2", "varies", "Write expressions or complete a truth table for a circuit (the figure is in the paper)")]

def draw_q(src, marks, cmd, q, tip, g, ans, warn=None, table_ans=""):
    return peq(src, marks, cmd, q, tip, "<p>" + ans + "</p>" + circ_html(g) + table_ans, warn)

past = '''  <p class="note">Logic questions are in Paper 1 every series, usually a "draw the logic circuit" or "complete the truth table" for an expression. The circuits below are redrawn for the printed expression; your own diagram can have a different layout provided each gate has the right inputs. Questions that need the circuit figure from the paper (write the expression for the circuit, complete a truth table for a given circuit) are listed in the table but need the original paper. Questions are reworded; check the paper for the exact wording.</p>
''' + peq(SRC("s21", "11/13", "Q8"), "3 marks", "Tick",
  "Tick one box in each row to identify the logic gate that each statement describes. The output is 1 only when both inputs are 1. The output is 1 only when both inputs are different. The output is 1 only when both inputs are 0. Boxes: AND, NAND, NOR, XOR, OR.", "AND, XOR, NOR.",
  "<p>" + mks(["Row 1: AND", "Row 2: XOR", "Row 3: NOR"]) + " (one mark per correct row)</p>", None) + draw_q(SRC("s21", "12", "Q3"), "4 + 2 marks", "Draw / Complete",
  "A logic expression is given: S = (A AND B AND C) OR (B XOR C). (a) Draw the logic circuit for the given expression. (b) Complete the truth table for the logic expression.", "A 3-input AND, an XOR, then an OR.", G_S21,
  "<b>(a)</b> " + mks(["One mark for each correct gate with correct inputs (max 4)"]) + " <b>(b)</b> " + mks(["First four rows correct", "Second four rows correct"]), None, tt(S21, ABC, "S")) + draw_q(SRC("w21", "12", "Q2(b)"), "2 marks", "Draw",
  "Draw a logic circuit for the following logic expression: X = NOT(NOT(A AND B) AND C).", "Inner AND, NOT, then AND with C, then NOT.", G_W21,
  "Mark points: " + mks(["NOT (A AND B), that is A NAND B", "NOT the result AND C, that is the result NAND C"]) + " (the circuit drawn uses two NAND gates, which is equivalent to AND, NOT, AND, NOT)", None) + peq(SRC("w21", "12", "Q2(a)"), "2 marks", "Complete",
  "Complete the truth table for each of the following two logic gates (NOR and NAND, drawn on the paper).", "NOR is 1 only for 00. NAND is 0 only for 11.",
  "<p>" + mks(["NOR: 1, 0, 0, 0", "NAND: 1, 1, 1, 0"]) + "</p>", None) + peq(SRC("s22", "12", "Q7"), "2 marks", "Complete",
  "Complete the truth table for the following logic expression: X = (A XOR B) AND NOT C. A, B, C in the standard eight rows, with a working space column.", "XOR first, then NOT C, then AND.",
  "<p>" + mks(["First four rows: 0, 0, 1, 0", "Second four rows: 1, 0, 0, 0"]) + "</p>" + tt(S22, ABC), "Skipping the working column. Write A XOR B first, then NOT C.") + draw_q(SRC("w22", "11", "Q3"), "2 + 2 marks", "Draw / Complete",
  "(a) Draw a logic circuit for X = NOT ((NOT A AND NOT B) OR (NOT B AND NOT C)). (b) Complete the truth table for the expression.", "Two ANDs of NOTs, an OR, a NOT.", G_W22A,
  "<b>(a)</b> " + mks(["NOT A AND NOT B and NOT B AND NOT C (or A NOR B and B NOR C)", "The final OR and NOT gates (or a NOR) with correct inputs"]) + " <b>(b)</b> " + mks(["First four rows: 0, 0, 1, 1", "Second four rows: 0, 1, 1, 1"]), None, tt(W22A, ABC)) + draw_q(SRC("w22", "12", "Q3(a)(b)"), "3 + 2 marks", "Draw / Complete",
  "A greenhouse window X opens if the temperature is too high (T = 1) and the wind speed is acceptable (W = 0) and rain is not detected (R = 0) or the manual override is off (M = 0). (a) Draw a logic circuit to represent the operation of the window. (b) Complete the truth table for X = NOT (A OR B OR C) AND (B NOR C).", "T AND NOT W AND (NOT R OR NOT M).", G_GREEN,
  "<b>(a)</b> " + mks(["T AND NOT W", "NOT R OR NOT M", "The final AND"]) + " <b>(b)</b> " + mks(["First four rows: 1, 0, 0, 0", "Second four rows: 0, 0, 0, 0"]) + " (X is 1 only for 000)", None, tt(W22B, ABC)) + draw_q(SRC("w22", "13", "Q5"), "3 + 2 marks", "Draw / Complete",
  "(a) Draw a logic circuit for X = NOT ((NOT (A AND B)) OR (NOT (B AND C))). (b) Complete the truth table for Y = (NOT P AND Q) OR (Q AND NOT R).", "Two NANDs (AND then NOT), an OR and a NOT.", G_W22C,
  "<b>(a)</b> " + mks(["NOT (A AND B)", "NOT (B AND C)", "NOT(NOT(A AND B) OR NOT(B AND C))"]) + " <b>(b)</b> " + mks(["First four rows: 0, 0, 1, 1", "Second four rows: 0, 0, 1, 0"]), None, tt(W22D, PQR, "Y")) + draw_q(SRC("s23", "11", "Q5"), "2 + 2 marks", "Draw / Describe",
  "(a) Draw the logic circuit for T = (NOT A OR B) XOR (C NAND D). (b) Describe the function of the NAND and NOR logic gates.", "NOT and OR, NAND, then XOR.", G_S23A,
  "<b>(a)</b> " + mks(["Two correct gates", "All four gates correct"], "a") + " (1 mark for two gates, 2 marks for all four) <b>(b)</b> " + mks(["NAND: 0 is output only when both inputs are 1, otherwise 1", "NOR: 1 is output only when both inputs are 0, otherwise 0"]), None) + draw_q(SRC("s23", "12", "Q6"), "2 + 2 marks", "Draw / Complete",
  "(a) Draw the logic circuit for Z = (R XOR S) AND (NOT T NOR P). (b) Complete the truth table for Z = (NOT P OR Q) XOR (R NOR Q).", "XOR and AND; NOT and NOR.", G_S23B,
  "<b>(a)</b> " + mks(["Correct XOR and AND gates, with correct inputs", "Correct NOT and NOR gates, with correct inputs"]) + " <b>(b)</b> " + mks(["First four rows: 0, 1, 1, 1", "Second four rows: 1, 0, 1, 1"]), None, tt(S23C, PQR, "Z")) + draw_q(SRC("w23", "11", "Q4"), "2 + 2 marks", "Complete / Draw",
  "(a) Complete the truth table for X = NOT (A NAND B) XOR (NOT B AND (B NOR C)). (b) Draw a logic circuit for X = (A AND NOT (B OR C)) AND (B NOR C).", "Work out each bracket in a working column.", G_W23B,
  "<b>(a)</b> " + mks(["First four rows: 1, 0, 0, 0", "Second four rows: 1, 0, 1, 1"]) + "<br><b>(b)</b> " + mks(["Both AND gates", "The NOT gate, the OR gate and the NOR gate"]), None, tt(W23A, ABC)) + draw_q(SRC("w23", "13", "Q4"), "2 + 2 marks", "Complete / Draw",
  "Y = ((P AND Q) XOR ((NOT Q) OR R)) AND NOT P. (a) Complete the truth table. (b) Draw a logic circuit for the expression.", "P AND Q; NOT Q OR R; XOR; NOT P; final AND.", G_W23C,
  "<b>(a)</b> " + mks(["First four rows: 1, 1, 0, 1", "Second four rows: 0, 0, 0, 0"]) + "<br><b>(b)</b> " + mks(["P AND Q, and NOT Q OR R", "NOT gate, AND gate and XOR gate"]), None, tt(W23C, PQR, "Y")) + peq(SRC("s24", "12", "Q1(a)"), "4 marks", "Describe",
  "Describe the operation of each of the following logic gates: NAND, NOR, XOR, OR.", "State the 0 and 1 outputs for each.",
  "<p>" + mks(["NAND: the output is 0 when both inputs are 1, otherwise 1", "NOR: the output is 1 when both inputs are 0, otherwise 0", "XOR: the output is 1 when one of the inputs is 1 and the other is 0, otherwise 0", "OR: the output is 0 when both inputs are 0, otherwise 1"]) + "</p>", "Writing 'NAND is AND but opposite'. State the conditions for each output value.") + draw_q(SRC("s24", "12", "Q1(b)"), "2 marks", "Draw",
  "Draw a logic circuit for X = NOT ((A AND B) OR (C AND D)).", "Two ANDs, an OR, a NOT.", G_S24D,
  mks(["Both AND gates with correct inputs", "The OR and NOT gates with correct inputs and no superfluous gates"]), None) + peq(SRC("s24", "13", "Q6"), "3 marks", "Match",
  "Each of the following truth tables has three inputs (A, B, C) and one output X. Match each truth table with its logic expression from: NOT (A XOR B) AND C; (A OR C) AND NOT B; A NAND B NAND C; (A NAND B) OR C; NOT (A AND B AND C). Table 1 has X = 0,1,0,0,1,1,0,0. Table 2 has X = 0,1,0,0,0,0,0,1. Table 3 has X = 1,1,1,1,1,1,0,1 (rows 000 to 111).", "Test each expression on one or two rows.",
  "<p>" + mks(["Table 1 matches (A OR C) AND NOT B", "Table 2 matches NOT (A XOR B) AND C", "Table 3 matches (A NAND B) OR C"]) + "</p>", "Checking only one row. Several expressions agree on some rows; test two or three.") + draw_q(SRC("w24", "12", "Q1"), "2 + 2 marks", "Complete / Draw",
  "(a) Complete the truth table for X = (A XOR B) NAND (A AND (B XOR C)). (b) Draw the logic circuit for W = P NAND ((Q OR NOT R) XOR (P XOR Q)).", "Working columns for A XOR B, B XOR C and A AND (B XOR C).", G_W24B,
  "<b>(a)</b> " + mks(["First four rows: 1, 1, 1, 1", "Second four rows: 1, 0, 1, 1"]) + "<br><b>(b)</b> " + mks(["(P XOR Q) and (Q OR NOT R)", "The second XOR gate and the final NAND gate with appropriate inputs"]), None, tt(W24A, ABC)) + draw_q(SRC("w24", "13", "Q1(a)(c)"), "1 + 2 marks", "Describe / Draw",
  "(a) Describe the operation of a 2-input XOR gate. (c) Draw the logic circuit for X = ((NOT A AND (B AND C)) OR (B NAND C)) AND NOT A.", "Different inputs give 1. Count the operators.", G_W24C,
  "<b>(a)</b> " + mks(["The output is 1 only if one input is 1 and the other is 0 (the inputs are different); 0 if both inputs are the same"]) + "<br><b>(c)</b> " + mks(["NOT gate, two correct AND gates and the NAND gate", "The OR gate and the final AND gate"]), None) + draw_q(SRC("w25", "11", "Q3"), "2 + 2 marks", "Draw / Write",
  "(a) Draw a logic circuit for X = NOT ((A NAND B) XOR (NOT A OR NOT C)). (b) Write the logic expression for the truth table with inputs R, S, T and output Q = 1 only for RST = 001 and 110.", "NAND, two NOTs and OR, XOR, NOT. Sum of products for the table.", G_W25A,
  "<b>(a)</b> " + mks(["(A NAND B) and (NOT A OR NOT C)", "XOR and NOT"]) + "<br><b>(b)</b> " + mks(["One correct term: (R AND S AND NOT T) or (NOT R AND NOT S AND T)", "The second term and the OR in the correct place"]) + " Q = (R AND S AND NOT T) OR (NOT R AND NOT S AND T)", None) + draw_q(SRC("w25", "13", "Q3"), "2 + 2 marks", "Complete / Draw",
  "(a) Complete the truth table for X = (A NOR B) NAND (C XOR B). (b) Draw a logic circuit for X = NOT (((A AND B) OR C) AND (C NOR D)).", "A NOR B, C XOR B, then NAND.", G_W25C,
  "<b>(a)</b> " + mks(["First four rows", "Second four rows"]) + " (both halves correct)<br><b>(b)</b> " + mks(["The AND, OR and NOR gates with correct inputs", "The final AND and NOT gates (or NAND) with correct inputs"]), None, tt(W25B, ABC))

review = req("3 marks", "Complete", "Complete the truth table for X = NOT (A AND B) OR C.", "NAND first.", "<p>" + mks(["Working column NOT (A AND B): 1,1,1,1,1,1,0,0", "First four rows of X: 1, 1, 1, 1", "Second four rows of X: 1, 1, 0, 1"]) + "</p>" + tt(OR(NAND("A", "B"), "C"), ABC), None) + req("2 marks", "Draw", "Draw a logic circuit for X = (A OR B) AND NOT C.", "Three gates.", "<p>" + mks(["The OR and NOT gates with correct inputs", "The final AND gate with correct inputs"]) + "</p>" + circ_html(net(AND(OR("A", "B"), NOT("C")), ABC, "X")), None) + req("2 marks", "Write", "Write the logic expression for the circuit: A and B into an XOR; the output and C into an AND.", "Substitute the gate.", "<p>" + mks(["(A XOR B)", "(A XOR B) AND C"]) + "</p>", None) + req("4 marks", "Describe", "Describe the operation of the AND, OR, NOT and NOR gates.", "State the conditions.", "<p>" + mks(["AND: 1 only when both inputs are 1", "OR: 0 only when both inputs are 0", "NOT: inverts the input", "NOR: 1 only when both inputs are 0"]) + "</p>", None) + req("3 marks", "Draw", "A heater H turns on if the temperature is low (T = 1) and either the window is closed (W = 0) or the override (O) is on (O = 1). Write an expression for H.", "AND with an OR in brackets.", "<p>" + mks(["T AND", "(NOT W OR O)", "H = T AND (NOT W OR O)"]) + "</p>", None)

tips = tips_html([
  ("Use the words of the mark scheme.", "'The output is 0 when both inputs are 1, otherwise 1.'"),
  ("Work inside the brackets first.", "Put each part in the working space."),
  ("One operator, one gate.", "Count them before you draw."),
  ("XOR means different.", "Not 'or'."),
  ("Write every NOT.", "Missing NOTs lose the most marks."),
  ("Test two rows.", "When matching tables to expressions."),
], [("a logic gate", "A circuit element that turns binary inputs into one output."), ("a truth table", "Every input combination and the resulting output."), ("working space", "A column for an intermediate result."), ("superfluous gate", "An unnecessary extra gate (loses a mark).")],
  [("Draw", "Draw the circuit."), ("Complete", "Fill in the truth table."), ("Describe", "State the output conditions."), ("Write", "Give the expression.")]) + FC

js = AKJS + AK20JS + AK15JS + "const GD = " + gjson(G_DEM) + ", GG = " + gjson(G_GREEN) + ", GW = " + gjson(G_W22A) + ";\n" + r'''
(function () {
  const cases = [[0, 1, 0], [1, 1, 0], [1, 0, 1], [0, 0, 0]];
  const draw = (s) => { const [a, b, c] = cases[Math.round(s.i)]; return circFit(GD, circEval(GD, { A: a, B: b, C: c }), 560, { vals: true }); };
  Lib.stepper($("#stA"), { w: 560, h: Math.round(GD.h * 2.2) + 12, label: "X = (A XOR B) AND NOT C", base: { i: 0 }, draw, tween: 150, dwell: 2400, steps: cases.map(([a, b, c], i) => { const x = (a ^ b) & (c ? 0 : 1); return { cap: `A = ${a}, B = ${b}, C = ${c}: A XOR B = <b>${a ^ b}</b>, NOT C = <b>${c ? 0 : 1}</b>, so X = <b>${x}</b>.`, s: { i } }; }) });
})();
(function () {
  const cases = [{ T: 1, W: 0, R: 0, M: 0 }, { T: 1, W: 1, R: 0, M: 0 }, { T: 1, W: 0, R: 1, M: 1 }, { T: 1, W: 0, R: 1, M: 0 }];
  const note = ["Hot, wind acceptable, no rain: the window opens.", "Hot but the wind is too high: the window stays closed.", "Rain detected and override on: closed.", "Rain detected but override off: the window opens."];
  const draw = (s) => circFit(GG, circEval(GG, cases[Math.round(s.i)]), 560, { vals: true });
  Lib.stepper($("#stB"), { w: 560, h: Math.round(GG.h * 2.2) + 12, label: "Greenhouse window", base: { i: 0 }, draw, tween: 150, dwell: 2600, steps: cases.map((c, i) => ({ cap: note[i], s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const v = circEval(GW, { A: 0, B: 1, C: 0 }); Object.keys(v).forEach((n) => { if (!["A", "B", "C"].includes(n) && k < 3) v[n] = 0; }); return circFit(GW, v, 600, { vals: true }); };
  Lib.stepper($("#stC"), { w: 600, h: Math.round(GW.h * 2) + 12, label: "NOT ((NOT A AND NOT B) OR (NOT B AND NOT C))", base: { i: 0 }, draw, tween: 150, dwell: 2800, steps: [
    { cap: "X = NOT ((NOT A AND NOT B) OR (NOT B AND NOT C)). Inputs A = 0, B = 1, C = 0.", s: { i: 0 } },
    { cap: "The outermost operator is NOT, so that is the final gate. Inside it is an OR.", s: { i: 1 } },
    { cap: "The OR takes two ANDs. Each AND takes two NOT gates.", s: { i: 2 } },
    { cap: "The whole circuit gives X = <b>1</b> for A = 0, B = 1, C = 0.", s: { i: 3 } }] });
})();
circLab("#labD", GD, [], ["X"]);
circLab("#labG", GG, [], ["X"]);
btnTable("gB", "gO", [
  ["NOT", "Inverts the input", "0 → 1, 1 → 0", "One input only"],
  ["AND", "1 only when both inputs are 1", "0 0 0 1", "All inputs 1"],
  ["OR", "0 only when both inputs are 0", "0 1 1 1", "Any input 1"],
  ["NAND", "0 only when both inputs are 1", "1 1 1 0", "AND then NOT"],
  ["NOR", "1 only when both inputs are 0", "1 0 0 0", "OR then NOT"],
  ["XOR", "1 when the inputs are different", "0 1 1 0", "Different"]
], ["Gate", "Output is", "Output for AB = 00, 01, 10, 11", "Remember"]);
''' + _prjs

finish("as-3-2-1-logic-gates-circuits", "as321", "Logic Gates and Logic Circuits",
  "The six logic gates, truth tables with working space, drawing a circuit from an expression and writing an expression from a circuit or table, with circuit animations, toggle labs and the real Paper 1 questions from 2021 to 2026.",
  "3.2.1", "3 · Hardware", "section 3.2 Logic gates and logic circuits", learn, watch, explore, _pr, real, where, past, review,
  "Part 1 is real 9618 questions on logic gates and circuits (Paper 1), 2021 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", tips, js)
