"""A Level CS syllabus 16.2.3: Reverse Polish Notation. Run: python3 tools/artifact-kit/mk_ac1623.py"""
import json
from ak16 import *

rpn_check()


def T_(r):
    return r.split()


def chk(infix, rpn):
    assert rpn_str(to_rpn(infix)) == rpn.replace("-", "–"), (infix, rpn_str(to_rpn(infix)))


def chk2(rpn, infix, env=None, val=None):
    if infix:
        assert to_infix(T_(rpn)) == infix, (rpn, to_infix(T_(rpn)))
    if val is not None:
        assert abs(run(T_(rpn), env)[0] - val) < 1e-9, (rpn, run(T_(rpn), env)[0])


chk("(a – b) * (a + c) / 7", "a b - a c + * 7 /")
chk("a * b + b - d + 15", "a b * b + d - 15 +")
chk("((7 + 3) - (2 * 8)) / 6", "7 3 + 2 8 * - 6 /")
chk("(7 – 2 + 8) / (9 – 5)", "7 2 – 8 + 9 5 - /")
chk("(2 – 6) * (13 + 7) / 5", "2 6 – 13 7 + * 5 /")
chk("((6 + 12) / (16 – 10)) * 18", "6 12 + 16 10 – / 18 *")
chk("21 * (15 – 3 + 8) / 7", "21 15 3 – 8 + * 7 /")
chk("16 + ((9 – 7) / (18 + 6))", "16 9 7 – 18 6 + / +")
chk("((18 – 15 + 3) * 5) / 12", "18 15 – 3 + 5 * 12 /")
chk2("a b / 4 * a b + -", "a / b * 4 – (a + b)")
chk2("a b - c d + * a /", "(a – b) * (c + d) / a", dict(a=5, b=10, c=27, d=12), -39)
chk2("5 2 - 5 4 + * 9 /", "(5 – 2) * (5 + 4) / 9", None, 3)
chk2("a b * 2 / c d / *", None, dict(a=20, b=3, c=10, d=5), 60)
chk2("a b - c d + * e /", "(a – b) * (c + d) / e", dict(a=17, b=5, c=7, d=3, e=10), 12)
chk2("a d + a b + c - *", "(a + d) * (a + b – c)", dict(a=6, b=3, c=7, d=9), 30)
chk2("b a c - + d b + * c /", "(b + a – c) * (d + b) / c")
chk2("d a b + * c a - /", "d * (a + b) / (c – a)", dict(a=6, b=12, c=15, d=5), 10)
chk2("a b - c + c a - * d /", "(a – b + c) * (c – a) / d")
chk2("c a / b d - * b +", None, dict(a=3, b=16, c=9, d=6), 46)
chk2("c a - b d + * b c + /", "(c – a) * (b + d) / (b + c)", dict(a=4, b=12, c=24, d=6), 10)
chk2("c d + a b - a c - * /", "(c + d) / ((a – b) * (a – c))")
chk2("15 9 - 24 3 / * 18 6 + /", None, None, 2)
chk2("6 15 + 20 3 - - 27 9 * /", "(6 + 15 – (20 – 3)) / (27 * 9)")
chk2("c a b - * b c + / d *", "c * (a – b) / (b + c) * d", dict(a=8, b=2, c=10, d=18), 90)
chk2("16 3 * 36 6 / 18 6 - * +", "16 * 3 + 36 / 6 * (18 – 6)", None, 120)
chk2("a d + a b + c - *", "(a + d) * (a + b – c)", dict(a=6, b=3, c=7, d=9), 30)


def stk(rpn, env=None):
    return rpn_table(T_(rpn), env)[0]


learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p><b>Reverse Polish Notation (RPN)</b>, also called <b>postfix</b>, writes the operator <b>after</b> its operands, so 3 + 4 becomes 3 4 +. It is an <b>unambiguous</b> way of writing an expression that can be read from left to right with <b>no brackets</b> and <b>no rules of precedence</b>, which makes it easy for a computer to evaluate. To <b>evaluate</b> RPN you read it left to right with a <b>stack</b>: push each operand; for each operator, pop the last two values, apply the operator (the older value is on the left) and push the result. The final value left on the stack is the answer. You also need to convert between <b>infix</b> (the usual form, with brackets) and RPN in both directions.</p></div>

  <h2>1 · Why use RPN?</h2>
  <ul>
    <li>It is an <b>unambiguous</b> way to represent an expression.</li>
    <li>It is evaluated <b>left to right</b>.</li>
    <li>It needs <b>no brackets</b>, and no rules of precedence (BODMAS) are needed, because the order of the operators is the order in which they are applied.</li>
    <li>A <b>stack</b> evaluates it easily: operands are popped in the reverse order to that in which they were pushed. A <b>binary tree</b> can also be used, since both infix and postfix come from tree traversal.</li>
  </ul>

  <h2>2 · Evaluating RPN with a stack</h2>
  <ol>
    <li>Read the next item of the expression from the left.</li>
    <li>If it is a <b>number or variable</b>, push its value on the stack.</li>
    <li>If it is an <b>operator</b>, pop the last two values from the stack: the first popped is the right-hand operand and the second popped is the left-hand operand. Apply the operator and push the result.</li>
    <li>Repeat until the whole expression has been read. The one value left on the stack is the result.</li>
  </ol>
  <p>Evaluate <b>c a – b d + * b c + /</b> where a = 4, b = 12, c = 24 and d = 6 (O/N 2025). Each column is the stack after that item has been read; the newest value is at the top.</p>
  ''' + stk("c a - b d + * b c + /", dict(a=4, b=12, c=24, d=6)) + '''
  <p>c a – gives 24 − 4 = 20; b d + gives 12 + 6 = 18; * gives 360; b c + gives 36; / gives 360 ÷ 36 = <b>10</b>. In the exam you show the stack after each step, and the interim totals (here 360) score marks.</p>
  <div class="tip"><b class="h">Remember</b>For – and /, the value pushed <b>earlier</b> is on the left: if the stack holds 24 then 4 and the operator is –, the result is 24 − 4, not 4 − 24.</div>

  <h2>3 · Converting infix to RPN</h2>
  <p>Work out which operation is done first in the infix expression (brackets, then * and / before + and −, and left to right for equal precedence), and write each operation as <b>operand operand operator</b>.</p>
  <p>(2 – 6) * (13 + 7) / 5</p>
  <ol>
    <li>First bracket: <b>2 6 –</b></li>
    <li>Second bracket: <b>13 7 +</b></li>
    <li>Multiply the two results: <b>2 6 – 13 7 + *</b></li>
    <li>Divide by 5: <b>2 6 – 13 7 + * 5 /</b></li>
  </ol>
  <p>A reliable method is to draw the <b>expression tree</b> (the operator at the top, its operands below) and read it with a <b>post-order traversal</b>: left branch, right branch, then the operator. Check your answer by evaluating it with a stack.</p>

  <h2>4 · Converting RPN to infix</h2>
  <p>Read the RPN left to right and use a stack of <b>sub-expressions</b>: push each operand; for an operator pop two, join them as <i>left operator right</i> and push the result. Add <b>brackets</b> where an operator with lower precedence is inside one with higher precedence. Working through <b>a b – c d + * a /</b>:</p>
  <ol>
    <li>a b – gives (a – b)</li>
    <li>c d + gives (c + d)</li>
    <li>* joins them: (a – b) * (c + d)</li>
    <li>a / : the answer is (a – b) * (c + d) / a</li>
  </ol>

  <h2>5 · Common ways to lose marks</h2>
  <ul>
    <li>Reversing the operands of – or /. The second value popped is the <b>left</b> operand.</li>
    <li>Leaving out the brackets needed in the infix answer, for example (a – b) * (c + d).</li>
    <li>Putting all the operators at the end. Each operator goes straight after its operands.</li>
    <li>In a stack table, showing only the final total. Show the stack after <b>every</b> item, and include the interim values.</li>
    <li>Explaining RPN with "it is faster". Give the properties: unambiguous, left to right, no brackets or precedence rules.</li>
  </ul>
'''

watch = '''
  <h2>1 · Evaluating with a stack</h2>
  <p>Press Play. Numbers are pushed; an operator pops two values and pushes the result.</p>
  <div id="stA"></div>
  <h2>2 · Infix to RPN with an expression tree</h2>
  <div id="stB"></div>
  <h2>3 · RPN to infix</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Evaluate RPN</h2>
  <p>Type an RPN expression using numbers, a, b, c, d and + − * /, with spaces between the items. Give values to the letters.</p>
  <div class="card"><input id="eI" type="text" value="c a - b d + * b c + /" style="width:100%;font:inherit;padding:8px"><div id="eV"></div><div id="eO"></div></div>

  <h2>Lab 2 · Infix to RPN</h2>
  <div class="card"><input id="iI" type="text" value="((6 + 12) / (16 - 10)) * 18" style="width:100%;font:inherit;padding:8px"><div class="verdict" id="iO"></div></div>

  <h2>Lab 3 · RPN to infix</h2>
  <div class="card"><input id="rI" type="text" value="a b - c d + * a /" style="width:100%;font:inherit;padding:8px"><div class="verdict" id="rO"></div></div>
'''

practise = '''
  <h2>1 · Infix or RPN?</h2><div id="cl1" class="card"></div>
  <h2>2 · A property of RPN or of infix?</h2><div id="cl2" class="card"></div>
  <h2>3 · Match the infix expression to its RPN</h2><div id="m1" class="card"></div>
  <h2>4 · Put the steps of evaluating RPN in order</h2><div id="o1" class="card"></div>
  <h2>5 · Working out</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Calculators that use RPN", "Some scientific calculators let you type 3 ENTER 4 + instead of 3 + 4 =. They push numbers on a stack and apply operators to the top values, with no brackets keys needed.", "RPN is evaluated with a stack.") +
rw("How a compiler evaluates your sum", "When you write (a + b) * c, the compiler converts it into an order of operations that works like RPN: a b + c *. The processor can then do each step with registers or a stack.", "RPN removes the need for brackets and precedence.") +
rw("Stack-based virtual machines", "Java bytecode and similar systems push operands on a stack and have operators that pop them, which is just the RPN method.", "operators act on the top of the stack.") +
rw("A sandwich counter", "Order of operations in a queue: put the bread, put the filling, then press 'make sandwich'. The action (operator) comes after what it acts on (operands).", "operator after operands.") +
rw("The PostScript language", "Printers read PostScript, a language written in RPN: 100 200 moveto draws from the operands that come first.", "postfix notation is used in real languages.")
)

where = [
  ("M/J 2021", "31, 32, 33", "4", "2 + 2 + 1 + 1 + 2", "Why RPN is used and a data structure; infix to RPN; RPN to infix; evaluate"),
  ("O/N 2022", "31, 33", "5", "1 + 1 + 1", "Infix to RPN; RPN to infix; evaluate the infix"),
  ("O/N 2023", "31, 33", "9", "2 + 4 + 3", "RPN to infix; stack contents when evaluating; explain how a stack evaluates RPN"),
  ("O/N 2023", "32", "6", "4 + 3", "Stack contents when evaluating; explain how RPN is evaluated"),
  ("M/J 2024", "31, 33", "5", "3 + 2 + 4", "RPN to infix; infix to RPN; evaluate with the stack"),
  ("M/J 2024", "32", "5", "2 + 4 + 3", "Infix to RPN; evaluate with the stack; RPN to infix"),
  ("O/N 2025", "31, 32, 33", "8(b), 8(c), 7(b), 7(c)", "2 + 4, 3 + 4, 3 + 4", "Infix to RPN or RPN to infix; evaluate with the stack"),
  ("M/J 2026", "31, 32, 33", "7, 6, 7", "2 + 3 + 4, 2 + 3 + 4, 3 + 2 + 4", "Infix to RPN; RPN to infix; evaluate; outline the use of a stack (Paper 33)")]

past = '''  <p class="note">RPN has been asked in Paper 3 in every series from May/June 2021 to May/June 2026. A question normally has three parts: write an infix expression in RPN, write an RPN expression in infix, and show the changing stack contents while an RPN expression is evaluated. Stack tables are shown here as columns, one per item, with the newest value at the top. Questions are reworded from the papers; check the original paper and mark scheme for the exact wording.</p>
''' + peq(SRC("s21", "31/32/33", "Q4"), "2 + 2 + 1 + 1 + 2 marks", "Explain / Identify / Write / Evaluate",
  "(a)(i) Explain why Reverse Polish Notation (RPN) is used to carry out the evaluation of expressions. (ii) Identify, with reasons, a data structure that could be used to evaluate an expression in RPN. (b) Write the infix expression in RPN: (a – b) * (a + c) / 7. (c) Write the RPN expression as an infix expression: a b / 4 * a b + –. (d) Evaluate the RPN expression a b + c d / / where a = 17, b = 3, c = 48 and d = 12. Show your working.",
  "RPN: unambiguous, no brackets, no precedence rules. Data structure: a stack.",
  "<p><b>(a)(i)</b> Any two: " + mks(["RPN provides an unambiguous method of representing an expression", "reading from left to right", "without the need for brackets", "with no need for rules of precedence (BODMAS)"]) + "</p><p><b>(ii)</b> " + mks(["Stack", "the operands are popped from the stack in the reverse order to how they were pushed"]) + " (or a binary tree, since a tree allows both infix and postfix to be evaluated by traversal)</p><p><b>(b)</b> " + mks(["a b – a c + * 7 /"]) + "</p><p><b>(c)</b> " + mks(["a / b * 4 – (a + b)"]) + "</p><p><b>(d)</b> " + mks(["Correct structure: (a + b) / (c / d)", "Correct substitution: (17 + 3) / (48 / 12) = 20 / 4 = 5"]) + "</p>", "In (c), losing the brackets round (a + b). Without them the expression is a different calculation.") + peq(SRC("w22", "31/33", "Q5"), "1 + 1 + 1 marks", "Write / Evaluate",
  "(a) Write the infix expression in Reverse Polish Notation (RPN): a * b + b – d + 15. (b)(i) Write the RPN expression in infix form: a b – c d + * a /. (ii) Evaluate your infix expression from part (b)(i) when a = 5, b = 10, c = 27 and d = 12.",
  "(a) * first, then the + and – from left to right.",
  "<p><b>(a)</b> " + mks(["a b * b + d – 15 +"]) + "</p><p><b>(b)(i)</b> " + mks(["(a – b) * (c + d) / a"]) + "</p><p><b>(ii)</b> " + mks(["−39"]) + " (−5 × 39 ÷ 5)</p>" + stk("a b - c d + * a /", dict(a=5, b=10, c=27, d=12)), "In (a), writing a b * b d - + 15 +. The expression is read left to right at equal precedence: ((a*b + b) – d) + 15.") + peq(SRC("w23", "31/33", "Q9"), "2 + 4 + 3 marks", "Write / Show / Explain",
  "(a)(i) Write the infix expression for this RPN expression: 5 2 – 5 4 + * 9 /. (ii) Show how the contents of the stack change as the RPN expression in part (a)(i) is evaluated. (b) Explain how a stack can be used to evaluate RPN expressions.",
  "Push numbers; operator pops two.",
  "<p><b>(a)(i)</b> " + mks(["(5 – 2)", "* (5 + 4) / 9"]) + " Complete: (5 – 2) * (5 + 4) / 9</p><p><b>(ii)</b> " + mks(["One mark per correct ring (max 4); the stack after each item, as shown"]) + "</p>" + stk("5 2 - 5 4 + * 9 /") + "<p><b>(b)</b> Any three: " + mks(["The RPN expression is read from left to right, one item at a time", "Each element is checked: if it is a value it is pushed onto the stack", "If it is an operator, the last two values on the stack are popped, the operator is applied and the result is pushed back onto the stack", "This repeats until a single value remains, which is the answer"]) + "</p>", "Applying the operator to the wrong order: 2 – 5 instead of 5 – 2.") + peq(SRC("w23", "32", "Q6"), "4 + 3 marks", "Show / Explain",
  "(a) The RPN expression a b * 2 / c d / * is to be evaluated where a = 20, b = 3, c = 10 and d = 5. Show the changing contents of the stack as the expression is evaluated. (b) Explain how an expression stored in RPN can be evaluated.",
  "Show the stack after every item.",
  "<p><b>(a)</b> " + mks(["One mark per correct ring (max 4)"]) + "</p>" + stk("a b * 2 / c d / *", dict(a=20, b=3, c=10, d=5)) + "<p>The final value is 60.</p><p><b>(b)</b> Any three: " + mks(["The RPN is read from left to right, one element at a time", "Each element is checked to see whether it is an operator or a value", "Values are pushed onto a stack until an operator is found", "The operator is applied to the last two values on the stack and the result is pushed back", "This repeats until a single value remains, which is the solution"]) + "</p>", None) + peq(SRC("s24", "31/33", "Q5"), "3 + 2 + 4 marks", "Write / Evaluate",
  "(a) Write this RPN in infix form: 5 2 + 9 3 – / 3 *. (b) Write this infix expression in RPN: ((7 + 3) – (2 * 8)) / 6. (c) Evaluate this RPN expression: a b – c d + * e / when a = 17, b = 5, c = 7, d = 3 and e = 10. Show the changing contents of the stack.",
  "Work in pairs: operand operand operator.",
  "<p><b>(a)</b> " + mks(["(5 + 2)", "/ (9 – 3)", "* 3"]) + " ((5 + 2) / (9 – 3)) * 3</p><p><b>(b)</b> " + mks(["7 3 +", "2 8 * – 6 /"]) + " Complete: 7 3 + 2 8 * – 6 /</p><p><b>(c)</b> " + mks(["One mark per correct ring (max 4)"]) + "</p>" + stk("a b - c d + * e /", dict(a=17, b=5, c=7, d=3, e=10)) + "<p>Result 12.</p>", "In (b), leaving the subtraction too early: 7 3 + 2 8 * – needs the multiplication first, because 2 * 8 is inside its own bracket.") + peq(SRC("s24", "32", "Q5"), "2 + 4 + 3 marks", "Write / Evaluate",
  "(a) Write this infix expression in RPN: (7 – 2 + 8) / (9 – 5). (b) Evaluate this RPN expression: a d + a b + c – * when a = 6, b = 3, c = 7 and d = 9. Show the changing contents of the stack. (c) Write this RPN expression in infix form: b a c – + d b + * c /.",
  "(a) 7 – 2 + 8 left to right first.",
  "<p><b>(a)</b> " + mks(["7 2 – 8 +", "9 5 – /"]) + " Complete: 7 2 – 8 + 9 5 – /</p><p><b>(b)</b> " + mks(["One mark per correct ring (max 4)"]) + "</p>" + stk("a d + a b + c - *", dict(a=6, b=3, c=7, d=9)) + "<p>Result 30.</p><p><b>(c)</b> " + mks(["(b + (a – c))", "* (d + b)", "/ c"]) + " (b + a – c) * (d + b) / c</p>", None) + peq(SRC("w25", "31", "Q8(b)(c)"), "2 + 4 marks", "Write / Show",
  "(b) Write the RPN for the infix expression (2 – 6) * (13 + 7) / 5. (c) The RPN expression d a b + * c a – / is to be evaluated, where a = 6, b = 12, c = 15 and d = 5. Show the changing contents of the stack.",
  "Left bracket, right bracket, then * and /.",
  "<p><b>(b)</b> " + mks(["2 6 –", "13 7 + * 5 /"]) + " Complete: 2 6 – 13 7 + * 5 /</p><p><b>(c)</b> " + mks(["One mark per correct ring (max 4)"]) + "</p>" + stk("d a b + * c a - /", dict(a=6, b=12, c=15, d=5)) + "<p>Result 10.</p>", None) + peq(SRC("w25", "32", "Q8(b)(c)"), "3 + 4 marks", "Write / Show",
  "(b) Convert this RPN back to its original infix form: a b – c + c a – * d /. (c) The RPN expression c a / b d – * b + is to be evaluated, where a = 3, b = 16, c = 9 and d = 6. Show the changing contents of the stack.",
  "Bracket each pair, and bracket a lower-precedence part inside *.",
  "<p><b>(b)</b> " + mks(["(a – b + c)", "* (c – a)", "/ d"]) + " Complete: (a – b + c) * (c – a) / d</p><p><b>(c)</b> " + mks(["One mark per correct ring (max 4)"]) + "</p>" + stk("c a / b d - * b +", dict(a=3, b=16, c=9, d=6)) + "<p>Result 46.</p>", None) + peq(SRC("w25", "33", "Q7(b)(c)"), "3 + 4 marks", "Write / Show",
  "(b) Write the RPN for the infix expression ((6 + 12) / (16 – 10)) * 18. (c) The RPN expression c a – b d + * b c + / is to be evaluated, where a = 4, b = 12, c = 24 and d = 6. Show the changing contents of the stack.",
  "The brackets show the order: 6 12 + first.",
  "<p><b>(b)</b> " + mks(["6 12 +", "16 10 – /", "18 *"]) + " Complete: 6 12 + 16 10 – / 18 *</p><p><b>(c)</b> " + mks(["One mark per correct ring (max 4), including the interim total 360 and the final total 10"]) + "</p>" + stk("c a - b d + * b c + /", dict(a=4, b=12, c=24, d=6)), "Showing only the answer 10. The stack after each item, with the interim total 360, is where the marks are.") + peq(SRC("s26", "31", "Q7"), "2 + 3 + 4 marks", "Write / Show",
  "(a) Write this infix expression in RPN: 21 * (15 – 3 + 8) / 7. (b) Write this RPN expression in infix form: c d + a b – a c – * /. (c) The RPN expression 15 9 – 24 3 / * 18 6 + / is to be evaluated. Show the changing contents of the stack.",
  "(b) the bracket round the denominator: (a – b) * (a – c).",
  "<p><b>(a)</b> " + mks(["21 15 3 –", "8 + * 7 /"]) + " Complete: 21 15 3 – 8 + * 7 /</p><p><b>(b)</b> " + mks(["(c + d)", "(a – b) * (a – c)", "/ ( … )"]) + " Complete: (c + d) / ((a – b) * (a – c))</p><p><b>(c)</b> " + mks(["One mark per correct ring (max 3), the interim total 48 and the final total 2"]) + "</p>" + stk("15 9 - 24 3 / * 18 6 + /"), "In (b), writing (c + d) / (a – b) * (a – c). The division applies to the whole product, so the denominator needs its own brackets.") + peq(SRC("s26", "32", "Q6"), "2 + 3 + 4 marks", "Write / Show",
  "(a) Write this infix expression in RPN: 16 + ((9 – 7) / (18 + 6)). (b) Write this RPN expression in infix form: 6 15 + 20 3 – – 27 9 * /. (c) The RPN expression c a b – * b c + / d * is to be evaluated, where a = 8, b = 2, c = 10 and d = 18. Show the changing contents of the stack.",
  "(b) the second subtraction takes the bracket (20 – 3).",
  "<p><b>(a)</b> 16 9 7 – 18 6 + / +</p><p><b>(b)</b> (6 + 15 – (20 – 3)) / (27 * 9)</p><p><b>(c)</b> " + mks(["One mark per correct ring"]) + "</p>" + stk("c a b - * b c + / d *", dict(a=8, b=2, c=10, d=18)) + "<p>Result 90.</p>", None) + peq(SRC("s26", "33", "Q7"), "3 + 2 + 4 marks", "Outline / Write / Show",
  "(a) Outline the process of using a stack to evaluate an expression written using RPN. (b) Write the infix expression ((18 – 15 + 3) * 5) / 12 in RPN. (c) The RPN expression 16 3 * 36 6 / 18 6 – * + is to be evaluated. Show the changing contents of the stack.",
  "(a) read left to right, push numbers, pop two for an operator, push the result.",
  "<p><b>(a)</b> Any three: " + mks(["The RPN expression is read from left to right", "If the next element is a number it is pushed onto the stack", "If the next element is an operator, the last two elements are popped from the stack", "the operator is applied to them and the result is pushed onto the stack", "The process repeats until the whole expression has been evaluated"]) + "</p><p><b>(b)</b> " + mks(["18 15 – 3 +", "5 * 12 /"]) + " Complete: 18 15 – 3 + 5 * 12 /</p><p><b>(c)</b> " + mks(["One mark per correct ring (max 4)"]) + "</p>" + stk("16 3 * 36 6 / 18 6 - * +") + "<p>Result 120.</p>", None)

review = req("2 marks", "Write", "Write the infix expression 3 * (4 + 5) in RPN, then evaluate it.", "Bracket first.", "<p>" + mks(["3 4 5 + *", "3 × 9 = 27"]) + "</p>" + stk("3 4 5 + *"), None) + req("2 marks", "Write", "Write the RPN expression 10 2 8 * + 3 – in infix form.", "Work out sub-expressions.", "<p>" + mks(["2 8 * gives 2 * 8", "10 + 2 * 8 – 3 (no brackets are needed, because * binds more tightly than + and –)"]) + "</p>", None) + req("3 marks", "Evaluate", "Evaluate the RPN expression 8 2 / 3 + 4 * showing the stack.", "Operator pops two.", "<p>" + mks(["8 2 / gives 4", "4 3 + gives 7", "7 4 * gives 28"]) + "</p>" + stk("8 2 / 3 + 4 *"), None) + req("2 marks", "Explain", "Explain why the operands of – must be popped in the correct order when evaluating RPN.", "Is 5 − 2 the same as 2 − 5?", "<p>" + mks(["Subtraction (and division) is not commutative, so the order of the operands matters", "The first value popped is the right operand and the second popped is the left operand"]) + "</p>", None) + req("3 marks", "Write", "Write (a + b) * (c – d) / e in RPN.", "Pairs first.", "<p>" + mks(["a b +", "c d –", "* e /"]) + " a b + c d – * e /</p>", None)

exam = exam20("Part 1 is real 9618 questions on Reverse Polish Notation (Paper 3), 2021 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", where, past, review)

tips = tips_html([
  ("Operator after operands.", "3 + 4 is 3 4 +."),
  ("Left to right, stack.", "Push values; an operator pops two, applies, pushes."),
  ("Second popped is on the left.", "Matters for – and /."),
  ("Show every step.", "The stack after each item, including interim totals."),
  ("Brackets in infix answers.", "A lower-precedence sub-expression inside * or / needs brackets."),
  ("RPN is unambiguous.", "No brackets, no precedence rules, left to right."),
], [
  ("RPN", "Reverse Polish Notation: operators written after their operands."),
  ("infix", "Operators written between operands, with brackets and precedence."),
  ("a stack", "A last-in first-out structure used to evaluate RPN."),
  ("post-order traversal", "Left branch, right branch, then the operator."),
], [("Write", "Give the converted expression only."), ("Show", "Draw the stack after each item."), ("Explain", "Give the reasons."), ("Evaluate", "Work out the value, showing steps.")]) + FC

js = AKJS + AK20JS + RPNJS + r'''
function stackSvg(stack, x, yb, w, label) { let o = ""; stack.forEach((v, i) => (o += SV.rect(x, yb - (i + 1) * 36, w, 32, i === stack.length - 1 ? "cell-warn" : "cell", { rx: 4 }) + SV.text(x + w / 2, yb - (i + 1) * 36 + 22, String(v), "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:" + (String(v).length > 12 ? 12 : 15) + "px" }))); return o + (label ? SV.text(x + w / 2, yb + 18, label, "sm", { "text-anchor": "middle" }) : ""); }
(function () {
  const r = "c a - b d + * b c + /".split(" "), env = { a: 4, b: 12, c: 24, d: 6 }, tr = runRpn(r, env).trace;
  const draw = (s) => { const k = Math.round(s.i); let o = SV.text(20, 20, "RPN (a = 4, b = 12, c = 24, d = 6)", "sm");
    r.forEach((t, i) => (o += SV.rect(20 + i * 52, 30, 46, 36, i === k - 1 ? "cell-warn" : i < k - 1 ? "cell-ok" : "cell", { rx: 6 }) + SV.text(43 + i * 52, 54, t.replace("-", "–"), "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:16px" })));
    o += SV.text(20, 108, "stack", "lbl bd"); const st = k ? tr[k - 1] : []; o += stackSvg(st, 20, 220, 120, "") + SV.rect(20, 224, 120, 4, "ax", { fill: "var(--ink)" });
    if (k) { const t = r[k - 1]; let msg = "push " + (env[t] !== undefined ? t + " = " + env[t] : t); if (PREC[t.replace("–", "-")]) { const p = tr[k - 2], b = p[p.length - 1], a = p[p.length - 2]; msg = "pop " + b + " and " + a + ": " + a + " " + t.replace("-", "–") + " " + b + " = " + st[st.length - 1]; } o += SV.text(180, 190, msg, "lbl bd t3", { style: "font-size:14px" }); } return o; };
  Lib.stepper($("#stA"), { w: 620, h: 240, label: "Evaluating RPN", base: { i: 0 }, draw, tween: 100, dwell: 1900, steps: [{ cap: "The stack is empty. Read the expression from the left, one item at a time.", s: { i: 0 } }].concat(r.map((t, i) => ({ cap: PREC[t] ? `Operator <b>${t.replace("-", "–")}</b>: pop the last two values, apply it, push the result.` : `<b>${t}</b> is a value: push ${env[t]} on the stack.`, s: { i: i + 1 } }))) });
})();
(function () {
  const N = [{ t: "*", x: 300, y: 36 }, { t: "/", x: 200, y: 100 }, { t: "18", x: 400, y: 100 }, { t: "+", x: 120, y: 168 }, { t: "–", x: 280, y: 168 }, { t: "6", x: 80, y: 236 }, { t: "12", x: 160, y: 236 }, { t: "16", x: 240, y: 236 }, { t: "10", x: 320, y: 236 }];
  const E = [[0, 1], [0, 2], [1, 3], [1, 4], [3, 5], [3, 6], [4, 7], [4, 8]]; const order = [5, 6, 3, 7, 8, 4, 1, 2, 0];
  const draw = (s) => { const k = Math.round(s.i); let o = ""; E.forEach(([a, b]) => (o += SV.line(N[a].x, N[a].y, N[b].x, N[b].y, "edge")));
    N.forEach((n, i) => { const at = order.indexOf(i); o += SV.circle(n.x, n.y, 22, at < k ? (at === k - 1 ? "nd-cur" : "nd-ok") : "nd") + SV.text(n.x, n.y + 5, n.t, "lbl bd", { "text-anchor": "middle" }); });
    o += SV.text(20, 286, "RPN: " + order.slice(0, k).map((i) => N[i].t).join(" "), "lbl bd t3", { style: "font-family:var(--mono);font-size:15px" }); return o; };
  Lib.stepper($("#stB"), { w: 520, h: 300, label: "Expression tree", base: { i: 0 }, draw, tween: 100, dwell: 1900, steps: [{ cap: "The expression tree of ((6 + 12) / (16 – 10)) * 18: the operator that is done <b>last</b> is at the top. Read it with a post-order traversal: left, right, operator.", s: { i: 0 } }].concat([5, 6, 3, 7, 8, 4, 1, 2, 0].map((x, i) => ({ cap: ["6 is a leaf: output 6.", "12 is the next leaf: output 12.", "Both children of + are done, so output the operator <b>+</b>.", "16 on the right branch of /.", "10.", "Now the operator <b>–</b>.", "Both sides of / are done: output <b>/</b>.", "18, the right child of the top node.", "Finally the root: <b>*</b>. The RPN is <b>6 12 + 16 10 – / 18 *</b>."][i], s: { i: i + 1 } }))) });
})();
(function () {
  const r = "b a c - + d b + * c /".split(" "); const st = []; const frames = [[]]; r.forEach((t) => { const tt = t.replace("–", "-"); if (PREC[tt]) { const b = st.pop(), a = st.pop(); let ea = a[0], eb = b[0]; if (a[1] < PREC[tt]) ea = "(" + ea + ")"; if (b[1] < PREC[tt] || (b[1] === PREC[tt] && "-/".includes(tt))) eb = "(" + eb + ")"; st.push([ea + " " + t.replace("-", "–") + " " + eb, PREC[tt]]); } else st.push([t, 9]); frames.push(st.map((x) => x[0])); });
  const draw = (s) => { const k = Math.round(s.i); let o = SV.text(20, 20, "RPN: " + r.map((t) => t.replace("-", "–")).join(" "), "sm", { style: "font-family:var(--mono)" }); r.forEach((t, i) => (o += SV.rect(20 + i * 44, 30, 40, 32, i === k - 1 ? "cell-warn" : i < k - 1 ? "cell-ok" : "cell", { rx: 5 }) + SV.text(40 + i * 44, 51, t.replace("-", "–"), "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono)" })));
    o += stackSvg(frames[k], 20, 240, 360, "stack of expressions"); return o; };
  Lib.stepper($("#stC"), { w: 530, h: 262, label: "RPN to infix", base: { i: 0 }, draw, tween: 100, dwell: 1900, steps: r.map((t, i) => ({ cap: PREC[t.replace("–", "-")] ? `Operator <b>${t.replace("-", "–")}</b>: pop two expressions, join them as <i>left ${t.replace("-", "–")} right</i> (adding brackets if needed) and push the result.` : `<b>${t}</b>: push it as an expression.`, s: { i: i + 1 } })).concat([{ cap: "One expression is left: <b>" + frames[r.length][0] + "</b>. That is the infix form.", s: { i: r.length } }]).slice(0, r.length + 1) });
})();

(function () {
  const inp = $("#eI"); const vars = { a: 4, b: 12, c: 24, d: 6 };
  const paint = () => { const r = inp.value.trim().split(/\s+/).filter(Boolean); const res = runRpn(r, vars); let h = "";
    if (res.trace && res.trace.length) { const depth = Math.max(...res.trace.map((s) => s.length)); h = '<div class="tw"><table class="t mono stk"><tr>' + r.slice(0, res.trace.length).map((t) => "<th>" + t.replace("-", "–") + "</th>").join("") + "</tr>"; for (let row = depth; row >= 1; row--) h += "<tr>" + res.trace.map((s) => "<td>" + (s.length >= row ? Math.round(s[row - 1] * 1000) / 1000 : "") + "</td>").join("") + "</tr>"; h += "</table></div>"; }
    $("#eV").innerHTML = '<p class="sm">Values: a = 4, b = 12, c = 24, d = 6.</p>'; $("#eO").innerHTML = h + `<div class="verdict">${res.error ? '<b style="color:var(--bad)">' + res.error + "</b>" : res.left !== 1 ? "The expression leaves " + res.left + " values on the stack, so it is not a complete RPN expression." : "Result: <b>" + Math.round(res.result * 1000) / 1000 + "</b>."}</div>`; };
  inp.oninput = paint; paint();
})();
(function () {
  const inp = $("#iI"); const paint = () => { try { const r = toRpn(inp.value); const v = runRpn(r, { a: 4, b: 12, c: 24, d: 6 }); $("#iO").innerHTML = "RPN: <b class='bx'>" + r.join(" ").replace(/-/g, "–") + "</b>" + (v.result !== undefined && !Number.isNaN(v.result) ? ". Value: <b>" + Math.round(v.result * 1000) / 1000 + "</b> (letters use a = 4, b = 12, c = 24, d = 6)." : ""); } catch (e) { $("#iO").textContent = "Check the brackets in the expression."; } };
  inp.oninput = paint; paint();
})();
(function () {
  const inp = $("#rI"); const paint = () => { const r = inp.value.trim().split(/\s+/).filter(Boolean); try { const res = runRpn(r, { a: 1, b: 1, c: 1, d: 1 }); if (res.error || res.left !== 1) throw 0; $("#rO").innerHTML = "Infix: <b class='bx'>" + toInfix(r) + "</b>"; } catch (e) { $("#rO").textContent = "That is not a complete RPN expression."; } };
  inp.oninput = paint; paint();
})();
''' + CLASSIFY("cl1", "Is the expression infix or RPN?", ["Infix", "RPN"],
  [("3 + 4 * 2", 0), ("3 4 2 * +", 1), ("(a – b) * c", 0), ("a b – c *", 1), ("5 2 – 5 4 + * 9 /", 1), ("(5 – 2) * (5 + 4) / 9", 0)],
  "Operators between operands: infix. After operands: RPN.") + CLASSIFY("cl2", "Is it a property of RPN?", ["Yes", "No"],
  [("Evaluated left to right with a stack", 0), ("Needs brackets", 1), ("Needs rules of precedence", 1), ("Unambiguous", 0), ("The operator comes after its operands", 0), ("The operator is between the operands", 1)],
  "RPN: unambiguous, no brackets, no precedence.") + MATCH([
  ["3 + 4 * 2", "3 4 2 * +"], ["(3 + 4) * 2", "3 4 + 2 *"], ["a * b + c", "a b * c +"], ["a * (b + c)", "a b c + *"], ["a – b – c", "a b – c –"]]) + ORDER(
  "Put the steps of evaluating RPN in order.",
  ["Read the next item from the left", "Push it on the stack if it is a value", "If it is an operator, pop the last two values", "Apply the operator and push the result", "When the expression ends, the value on the stack is the answer"],
  "Read, push, pop two, apply and push, finish.") + CALC([
  {"q": "Evaluate 6 2 / 4 * .", "a": 12, "unit": "", "tol": 0.01, "hint": "6 ÷ 2 = 3, then × 4.", "sol": "<b>12</b>."},
  {"q": "Evaluate 9 3 - 4 + 2 *.", "a": 20, "unit": "", "tol": 0.01, "hint": "6, 10, 20.", "sol": "<b>20</b>."},
  {"q": "Evaluate 15 3 5 + / .", "a": 1.875, "unit": "", "tol": 0.001, "hint": "3 + 5 = 8, then 15 ÷ 8.", "sol": "<b>1.875</b>."},
  {"q": "How many values are on the stack after reading a b c in a b c + *?", "a": 3, "unit": "", "tol": 0.01, "hint": "Three pushes.", "sol": "<b>3</b>."},
  {"q": "What is the deepest the stack gets when evaluating 6 12 + 16 10 - / 18 * ?", "a": 3, "unit": "", "tol": 0.01, "hint": "After 6 12 + 16 10 there are 3 values.", "sol": "<b>3</b>."}]) + MCQ([
  ("What is 4 5 + 2 * ?", ["14", "18", "13", "40"], 1, "(4 + 5) × 2 = 18."),
  ("Which data structure evaluates RPN?", ["Queue", "Stack", "Array only", "Linked list"], 1, "A stack."),
  ("In RPN the operator comes:", ["Before the operands", "Between the operands", "After the operands", "At random"], 2, "After."),
  ("5 2 - with the stack: the left operand is:", ["The first popped", "The second popped", "Always 0", "The operator"], 1, "The second popped, 5."),
  ("RPN needs:", ["Brackets", "Precedence rules", "Neither", "Both"], 2, "Neither."),
  ("The infix of a b + c * is:", ["a + b * c", "(a + b) * c", "a + (b * c)", "a * b + c"], 1, "(a + b) * c.")], "qz1") + CARDS([
  ("RPN", "Operators after operands: 3 4 +."), ("Why RPN", "Unambiguous, left to right, no brackets, no precedence."), ("Evaluate", "Push values; operator pops two, applies, pushes."), ("Operand order", "Second popped is the left operand."),
  ("Infix to RPN", "Operand operand operator for each operation, in order."), ("RPN to infix", "Stack of expressions; add brackets where needed."), ("Tree", "Post-order traversal gives RPN."), ("Stack table", "Show the stack after every item.")])

build("ac1623", "ac-16-2-3-reverse-polish-notation", "Reverse Polish Notation", EYA("16.2.3"),
  "Reverse Polish Notation: why it is used, evaluating with a stack, and converting between infix and RPN; animations, an RPN evaluator and converters, and the real Paper 3 questions from 2021 to 2026.",
  dict(sub=CBK("Chapter 16 · System software, section 16.2 Translation software"), **tabs(learn, watch, explore, practise, real, exam, tips)), js)
