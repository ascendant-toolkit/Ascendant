"""A Level CS syllabus 16.2.2: syntax diagrams and Backus-Naur Form. Run: python3 tools/artifact-kit/mk_ac1622.py"""
import json
import re
from ak16 import *

# the example strings in the mark schemes, checked against the grammars drawn below
CH = {
    "w21": r"[$%&*#][0-9AEIOU]+", "s23_31": r"[ADPRY]+[0-9]+[$%&@#]+", "s23_32": r"[ACEGIKMOQSUWY]+[0-9]?", "s23_32reg": r"[ACEGIKMOQSUWY]{2}[0-9]{1,3}",
    "s25_31": r"[ACEGJ](?:[bdfhk]|[$@#&%]|[0-9])+", "s25_32": r"[A-HJK](?:[A-HJK]|[0-9])*", "s25_33": r"[JKLVXZ](?:[aeipuy]|[0-9]){2}[0-9]", "w24_32": r"[13579](?:[13579]|[02468])?"}
for k, good, bad in [("w21", ["$A9E3"], ["A$9", "$"]), ("s23_31", ["DPAD99$"], ["DAD#95", "ADY123?"]), ("s23_32", ["UWY"], ["9SW"]), ("s23_32reg", ["AC768"], ["A768"]), ("s25_31", ["J%d7"], ["#Jd7", "C%6A"]),
                     ("s25_32", ["AC768", "A"], ["9K"]), ("s25_33", ["Ja99", "J999"], ["JJ90"]), ("w24_32", ["1", "13", "19"], ["21", "123"])]:
    assert all(re.fullmatch(CH[k], g) for g in good) and not any(re.fullmatch(CH[k], b) for b in bad), k

D_PASS21 = sx("password", S(R("character"), L(A(R("digit"), R("capital letter")))))
D_PASS23 = sx("password", S(L(R("letter")), L(R("digit")), L(R("symbol"))))
D_VAR23 = sx("variable", S(L(R("letter")), A(R("digit"), bypass=True)))
D_PC25 = sx("passcode", S(R("uppercase"), L(A(R("lowercase"), R("symbol"), R("digit")))))
D_VAR25 = sx("variable", S(R("letter"), A(L(A(R("letter"), R("digit"))), bypass=True)))
D_EXP25 = sx("expression", S(R("variable"), T("="), R("variable"), L(S(R("operator"), R("variable")))))
D_PCIN33 = sx("passcode", S(R("upper"), A(R("lower"), R("digit")), A(R("lower"), R("digit")), R("digit")))
D_PCOUT33 = sx("passcode", S(R("upper"), A(R("lower"), R("digit")), A(R("lower"), R("digit"), R("upper")), L(R("digit"))))
D_NUM24 = sx("number", S(R("odd"), A(R("odd"), R("even"), bypass=True)))
D_CODE24 = sx("code", S(R("letter"), R("number"), A(R("number"), bypass=True), R("symbol")))
D_LAB24 = sx("label", S(R("letter"), R("digit"), A(R("digit"), bypass=True)))
D_EQ24 = sx("equation", S(R("label"), T("="), R("label"), R("operator"), R("label")))
D_ID23 = sx("identifier", S(L(R("letter")), A(L(R("digit")), bypass=True)))
D_REG23 = sx("vehicle registration", S(R("letter"), R("letter"), R("digit"), A(R("digit"), bypass=True), A(R("digit"), bypass=True)))
D_BIT = sx("bit", A(T("0"), T("1")))
D_SIGN = sx("integer", S(A(T("+"), T("-"), bypass=True), L(R("digit"))))

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>The <b>grammar</b> of a programming language, the rules for how its statements can be written, can be shown as <b>syntax diagrams</b> or in <b>Backus-Naur Form (BNF)</b>. A syntax diagram follows arrows from left to right: <b>rectangles</b> are names of other rules, <b>rounded boxes</b> are characters that appear exactly as written, a <b>choice</b> is a set of parallel routes, and a <b>loop</b> back lets something repeat. In BNF each rule has the form <b>&lt;name&gt; ::= definition</b>, where <b>|</b> means "or", names are in angle brackets, and repetition is written with <b>recursion</b>, a rule that uses its own name. The two notations describe the same thing, so you must be able to turn a diagram into BNF and back, and to decide whether a string is valid. Syntax analysis uses these rules to check a program.</p></div>

  <h2>1 · Syntax diagrams</h2>
  <p>Start at the arrow on the left, follow the lines to the arrow on the right, and write down each box you pass through. A string is <b>valid</b> if it can be made by some route.</p>
  <ul>
    <li><b>Rounded box</b>: a <b>terminal</b>, a symbol that appears as it is, such as a digit or an operator.</li>
    <li><b>Rectangle</b>: a <b>non-terminal</b>, the name of another rule that is defined by its own diagram.</li>
    <li><b>Choice</b>: parallel routes; take exactly one.</li>
    <li><b>Loop back</b>: the route can return to an earlier point, so the part inside the loop can be used <b>one or more times</b>.</li>
    <li><b>Bypass</b>: a line that goes straight past a box, so the box is <b>optional</b>.</li>
  </ul>
  <p>A bit is 0 or 1; an integer is an optional sign followed by one or more digits:</p>
  ''' + D_BIT + D_SIGN + '''
  <p>This diagram describes a variable: one or more letters, then at most one digit. <b>UWY</b> and <b>AB7</b> are valid; <b>9SW</b> is not, because it starts with a digit, and <b>AB78</b> is not, because only one digit is allowed.</p>
  ''' + D_VAR23 + '''

  <h2>2 · Backus-Naur Form</h2>
  <div class="tw"><table class="t">
    <tr><th>Symbol</th><th>Meaning</th><th>Example</th></tr>
    <tr><td class="bx">&lt;name&gt;</td><td>a rule (non-terminal), written in angle brackets</td><td class="bx">&lt;digit&gt;</td></tr>
    <tr><td class="bx">::=</td><td>"is defined as"</td><td class="bx">&lt;bit&gt; ::= 0 | 1</td></tr>
    <tr><td class="bx">|</td><td>"or": a choice between alternatives</td><td class="bx">&lt;symbol&gt; ::= $ | % | &amp;</td></tr>
    <tr><td>terminals</td><td>characters written as they are</td><td class="bx">0 1 $ +</td></tr>
    <tr><td>side by side</td><td>one after the other (a sequence)</td><td class="bx">&lt;character&gt;&lt;code&gt;</td></tr>
  </table></div>
  <h3>Turning a diagram into BNF</h3>
  <ul>
    <li><b>A choice</b> becomes alternatives joined by |: for a symbol diagram that offers $, %, &amp;, @ or #, <span class="bx">&lt;symbol&gt; ::= $ | % | &amp; | @ | #</span>.</li>
    <li><b>A sequence</b> is written side by side: a number that is an odd digit followed by an optional odd or even digit is built from <span class="bx">&lt;odd&gt;</span> then the rest.</li>
    <li><b>An optional part</b> becomes two alternatives, one with it and one without: <span class="bx">&lt;number&gt; ::= &lt;odd&gt; | &lt;odd&gt;&lt;even&gt; | &lt;odd&gt;&lt;odd&gt;</span>.</li>
    <li><b>A repeat</b> (a loop) is written with <b>recursion</b>, so that the rule is defined using itself: one or more letters is <span class="bx">&lt;word&gt; ::= &lt;letter&gt; | &lt;word&gt;&lt;letter&gt;</span> (or <span class="bx">&lt;letter&gt;&lt;word&gt;</span>). The first alternative ends the repetition; the second adds one more.</li>
  </ul>
  <h3>Worked example (O/N 2021, Paper 31)</h3>
  <p>A password is a character followed by one or more digits or capital letters.</p>
  ''' + D_PASS21 + '''
  <p>The loop needs a helper rule <span class="bx">&lt;code&gt;</span>, one or more digits or capital letters:</p>
  <pre class="plain">&lt;password&gt; ::= &lt;character&gt;&lt;code&gt;
&lt;code&gt; ::= &lt;digit&gt; | &lt;capital_letter&gt; | &lt;digit&gt;&lt;code&gt; | &lt;capital_letter&gt;&lt;code&gt;</pre>
  <p>A valid password is $A9E3. Names with a space, such as capital letter, are written with an underscore in BNF.</p>

  <h2>3 · Drawing a syntax diagram from a description</h2>
  <ol>
    <li>Put the elements in order, as rectangles (or rounded boxes for fixed characters).</li>
    <li>Add a <b>choice</b> where the description says "or".</li>
    <li>Add a <b>loop back</b> where it says "one or more" or "can be repeated".</li>
    <li>Add a <b>bypass</b> where it says "optional" or "zero or one".</li>
    <li>Label the diagram with its name, and put arrows on every line, including one at the start and one at the end.</li>
  </ol>
  <p>Example: an identifier begins with one or more letters, followed by zero digits, one digit, or more digits:</p>
  ''' + D_ID23 + '''

  <h2>4 · Common ways to lose marks</h2>
  <ul>
    <li>Forgetting the angle brackets round names, or writing = or := instead of ::=.</li>
    <li>Writing a repeat as the name followed by "..." or "*". BNF has no repeat symbol; use recursion.</li>
    <li>Making a rule that can never end: the recursive rule needs a non-recursive alternative.</li>
    <li>Giving the reason a string is invalid without referring to the diagram: the first character must be a letter, the symbol must come after the digits, ? is not an allowed symbol.</li>
    <li>In a drawn diagram, missing the arrows, the label, or the loop, or adding extra boxes.</li>
  </ul>
'''

watch = '''
  <h2>1 · Following a diagram: a valid string</h2>
  <p>The password diagram needs letters, then digits, then symbols. Press Play.</p>
  <div id="stA"></div>
  <h2>2 · Following a diagram: an invalid string</h2>
  <div id="stB"></div>
  <h2>3 · Building a string with BNF</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Is it valid?</h2>
  <p>Choose a grammar and type a string. The checker says whether it is valid and shows where it goes wrong.</p>
  <div class="card"><div id="vB" class="btnrow"></div><div id="vD"></div><input id="vI" type="text" style="width:100%;font:inherit;padding:8px" value="DPAD99$"><div class="verdict" id="vV"></div></div>

  <h2>Lab 2 · Diagram or BNF?</h2>
  <p>Pick a rule to see its diagram and its BNF side by side.</p>
  <div class="card"><div id="bB" class="btnrow"></div><div id="bO"></div></div>
'''

practise = '''
  <h2>1 · Terminal or non-terminal?</h2><div id="cl1" class="card"></div>
  <h2>2 · Which BNF feature?</h2><div id="cl2" class="card"></div>
  <h2>3 · Match the diagram feature to its meaning</h2><div id="m1" class="card"></div>
  <h2>4 · Put the steps of drawing a syntax diagram in order</h2><div id="o1" class="card"></div>
  <h2>5 · Counting</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Checking a program's grammar", "The syntax-analysis stage of a compiler uses the grammar of the language, often written in BNF, to decide whether a line of code is allowed.", "BNF defines the rules a parser applies.") +
rw("Forms that reject your input", "A website that says a postcode or password is invalid is applying a grammar like these diagrams: letters first, then digits, with only certain symbols allowed.", "validity is a pattern of allowed characters.") +
rw("Rules for a username", "'One or more letters followed by at most two digits' is exactly a loop on letter and an optional digit in a syntax diagram.", "loops and bypasses express repetition and options.") +
rw("Language reference manuals", "Languages such as Python and SQL publish their grammar in BNF-like notation so that anyone can build a tool that understands them.", "BNF is a standard way to define a language.") +
rw("Number plates", "Two letters, two digits and three letters is a pattern, in the same way as the vehicle-registration question in the exam.", "a sequence of named parts.")
)

where = [
  ("O/N 2021", "31, 32", "4", "2 + 1 + 4", "BNF for a diagram of characters; a valid password; BNF for the password diagram"),
  ("M/J 2023", "31, 33", "6", "3 + 1 + 4", "Valid or invalid passwords with reasons; BNF for symbol and letter; draw a diagram for an identifier"),
  ("M/J 2023", "32", "3", "2 + 3 + 1 + 3", "Valid or invalid variables; BNF for word and variable; an example registration; draw its diagram"),
  ("O/N 2024", "31, 33", "10", "4 + 3 + 2", "BNF for operator, label and equation; draw and write BNF for a password rule"),
  ("O/N 2024", "32", "7", "2 + 2 + 3 + 2", "Why each number is invalid; BNF for symbol and number; draw and write BNF for code"),
  ("M/J 2025", "31", "7", "2 + 4", "Why each passcode is invalid; BNF for uppercase and passcode"),
  ("M/J 2025", "32", "9", "1 + 1 + 3 + 1", "Why 9K is not valid; BNF for operator; complete the diagram for an expression; a valid variable"),
  ("M/J 2025", "33", "9", "1 + 3 + 2", "Why JJ90 is not valid; BNF for upper and passcode; change the passcode diagram")]

past = '''  <p class="note">Syntax diagrams and BNF are asked in Paper 3 in nearly every series from 2021 to 2025 and always as a three or four part question: judge validity, write BNF, draw a diagram. The digit, letter and symbol diagrams are simple lists of characters and are described in words below; the longer diagrams are redrawn. Questions are reworded from the papers; check the original paper and mark scheme for the exact wording.</p>
''' + peq(SRC("w21", "31/32", "Q4"), "2 + 1 + 4 marks", "Write / State",
  "The syntax diagrams for a particular language define a digit (0 to 9), a capital letter (A, E, I, O or U) and a character ($, %, &, * or #). (a) Write the Backus-Naur Form (BNF) notation of the syntax diagram for character. (b) A password must begin with a character and be followed by one or more digits or capital letters. (i) State an example of a valid password. (ii) A valid password is represented by this syntax diagram. Write the BNF notation of the syntax diagram for password." + D_PASS21,
  "A repeat needs recursion: a helper rule that uses its own name.",
  "<p><b>(a)</b> " + mks(["&lt;character&gt; ::=", "$ | % | &amp; | * | #"]) + "<br><span class=\"bx\">&lt;character&gt; ::= $ | % | &amp; | * | #</span></p><p><b>(b)(i)</b> " + mks(["$A9E3 (a character, then digits or capital letters)"], "a") + "</p><p><b>(ii)</b> " + mks(["&lt;password&gt; ::= &lt;character&gt;…", "…&lt;code&gt;", "&lt;code&gt; ::= …", "… &lt;digit&gt; | &lt;capital_letter&gt;", "… | &lt;digit&gt;&lt;code&gt; | &lt;capital_letter&gt;&lt;code&gt;"]) + "</p><pre class=\"plain\">&lt;password&gt; ::= &lt;character&gt;&lt;code&gt;\n&lt;code&gt; ::= &lt;digit&gt; | &lt;capital_letter&gt; | &lt;digit&gt;&lt;code&gt; | &lt;capital_letter&gt;&lt;code&gt;</pre>", "Writing the repeat as <code>&lt;digit&gt;...</code> or leaving out the alternative without recursion, so that only one extra character is allowed.") + peq(SRC("s23", "31/33", "Q6"), "3 + 1 + 4 marks", "State / Complete / Draw",
  "Several syntax diagrams are shown: operator (+ - * /), digit (0 to 9), symbol ($ % &amp; @ #), letter (A D P R Y) and password." + D_PASS23 + "(a) State whether each password is valid or invalid and give a reason: DPAD99$; DAD#95; ADY123?. (b) Complete the BNF for the diagrams: &lt;symbol&gt; ::= ; &lt;letter&gt; ::= . (c) An identifier begins with one or more letters, followed by zero digits, or one digit, or more digits. Draw a syntax diagram for an identifier.",
  "Follow the password diagram: letters, then digits, then symbols.",
  "<p><b>(a)</b> " + mks(["DPAD99$: valid, because it is several letters followed by several digits followed by a symbol", "DAD#95: invalid, because the symbol comes before the digits; it should come after", "ADY123?: invalid, because ? is not a valid symbol"]) + "</p><p><b>(b)</b> " + mks(["&lt;symbol&gt; ::= $ | % | &amp; | @ | #, and &lt;letter&gt; ::= A | D | P | R | Y"]) + "</p><p><b>(c)</b> " + mks(["Begins with a letter", "A letter can repeat and a digit is present", "A digit can repeat or can be bypassed", "Correct structure: name, boxes and arrows (in and out)"]) + "</p>" + D_ID23, "Drawing the digit loop without a bypass, so at least one digit is forced. The question allows zero digits.") + peq(SRC("s23", "32", "Q3"), "2 + 3 + 1 + 3 marks", "State / Complete / Draw",
  "The diagrams define a digit (0 to 9), a letter (A C E G I K M O Q S U W Y) and a variable." + D_VAR23 + "(a) State whether each variable is valid or invalid and give a reason: 9SW; UWY. (b) &lt;word&gt; contains one or more letters. Complete the BNF for &lt;word&gt; and use this to complete the BNF for &lt;variable&gt;. (c) Vehicle registrations must begin with two letters and be followed by one, two or three digits. (i) State an example of a valid vehicle registration. (ii) Draw a syntax diagram for a vehicle registration.",
  "A repeating letter: recursion in &lt;word&gt;. An optional digit: two alternatives.",
  "<p><b>(a)</b> " + mks(["9SW: invalid, because a variable must begin with a letter", "UWY: valid, because it begins with a letter and is followed by two other letters"]) + "</p><p><b>(b)</b> " + mks(["&lt;word&gt; ::= &lt;letter&gt; |", "… &lt;word&gt;&lt;letter&gt;", "&lt;variable&gt; ::= &lt;word&gt; | &lt;word&gt;&lt;digit&gt;"]) + "</p><pre class=\"plain\">&lt;word&gt; ::= &lt;letter&gt; | &lt;word&gt;&lt;letter&gt;\n&lt;variable&gt; ::= &lt;word&gt; | &lt;word&gt;&lt;digit&gt;</pre><p><b>(c)(i)</b> " + mks(["AC768 (two letters, then one to three digits)"], "a") + "</p><p><b>(ii)</b> " + mks(["Always exactly two letters", "One, two or three digits possible", "Correct arrows, boxes and name of the diagram"]) + "</p>" + D_REG23, "Giving 'invalid' for UWY because it has no digit. The digit is optional in the diagram.") + peq(SRC("w24", "31/33", "Q10"), "4 + 3 + 2 marks", "Complete / Draw / Write",
  "Several syntax diagrams are shown: letter (A E I O U Y), operator (+ - * /), symbol (# $ ? &amp; @), digit (0 to 9), label and equation." + D_LAB24 + D_EQ24 + "(a) Complete the BNF for the given syntax diagrams: &lt;operator&gt; ::= ; &lt;label&gt; ::= ; &lt;equation&gt; ::= . (b) A new syntax rule, password, is required. It must begin with a letter or a symbol, followed by a digit and end with one or two symbols. (i) Draw a syntax diagram for password. (ii) Write the BNF for password.",
  "Label: letter, digit, optional second digit. Password: a choice at the start, then digit, then one or two symbols.",
  "<p><b>(a)</b> " + mks(["&lt;operator&gt; ::= + | - | * | /", "&lt;label&gt; ::= &lt;letter&gt;&lt;digit&gt; | &lt;letter&gt;&lt;digit&gt;&lt;digit&gt;", "&lt;equation&gt; ::= &lt;label&gt; =", "&lt;label&gt;&lt;operator&gt;&lt;label&gt;"]) + "</p><p><b>(b)(i)</b> " + mks(["Begins with either a letter or a symbol", "Ends with either one or two symbols", "Digit and all other connections and the label correct"]) + "</p>" + sx("password", S(A(R("letter"), R("symbol")), R("digit"), R("symbol"), A(R("symbol"), bypass=True))) + "<p><b>(ii)</b> " + mks(["&lt;password&gt; ::= &lt;letter&gt;&lt;digit&gt;&lt;symbol&gt; | &lt;letter&gt;&lt;digit&gt;&lt;symbol&gt;&lt;symbol&gt; |", "&lt;symbol&gt;&lt;digit&gt;&lt;symbol&gt; | &lt;symbol&gt;&lt;digit&gt;&lt;symbol&gt;&lt;symbol&gt;"]) + "</p>", "In (b)(i), putting the letter and symbol in sequence instead of as a choice at the start. The password begins with one or the other.") + peq(SRC("w24", "32", "Q7"), "2 + 2 + 3 + 2 marks", "State / Complete / Draw / Write",
  "Several syntax diagrams are shown: odd (1 3 5 7 9), even (0 2 4 6 8), symbol (% £ # @ $), letter (A B C D E) and number." + D_NUM24 + "(a) State why each number is invalid: 21; 123. (b) Complete the BNF for symbol and number. (c) A new syntax rule, code, must begin with a letter, followed by one or two numbers, and end with a symbol. (i) Draw a syntax diagram for code. (ii) Write the BNF for code.",
  "The number diagram has an optional second digit.",
  "<p><b>(a)</b> " + mks(["21: a number must begin with an odd digit, and 2 is even", "123: a number can only be one or two digits long, not three"]) + "</p><p><b>(b)</b> " + mks(["&lt;symbol&gt; ::= % | £ | # | @ | $", "&lt;number&gt; ::= &lt;odd&gt; | &lt;odd&gt;&lt;even&gt; | &lt;odd&gt;&lt;odd&gt;"]) + "</p><p><b>(c)(i)</b> " + mks(["Letter, number and symbol in the correct order", "Provision for one or two numbers with the connectors", "All other connections and the label correct, with no additional data"]) + "</p>" + D_CODE24 + "<p><b>(ii)</b> " + mks(["&lt;code&gt; ::= &lt;letter&gt;&lt;number&gt;&lt;symbol&gt; |", "&lt;letter&gt;&lt;number&gt;&lt;number&gt;&lt;symbol&gt;"]) + "</p><pre class=\"plain\">&lt;code&gt; ::= &lt;letter&gt;&lt;number&gt;&lt;symbol&gt; | &lt;letter&gt;&lt;number&gt;&lt;number&gt;&lt;symbol&gt;</pre>", "Answering (a) for 21 with 'it has no letter'. Check the diagram: a number is built only from odd and even digits.") + peq(SRC("s25", "31", "Q7"), "2 + 4 marks", "State / Complete",
  "Several syntax diagrams are shown: uppercase (A C E G J), lowercase (b d f h k), symbol ($ @ # &amp; %), digit (0 to 9) and passcode." + D_PC25 + "(a) State why each passcode is invalid: #Jd7; C%6A. (b) Complete the BNF for &lt;uppercase&gt; and &lt;passcode&gt;.",
  "A passcode is one uppercase, then one or more of lowercase, symbol or digit.",
  "<p><b>(a)</b> " + mks(["#Jd7: it must begin with a member of the group uppercase; it cannot begin with a symbol", "C%6A: the fourth character cannot be a member of uppercase; it must be a symbol, digit or lowercase"]) + "</p><p><b>(b)</b> " + mks(["&lt;uppercase&gt; ::= A | C | E | G | J", "&lt;passcode&gt; ::= &lt;uppercase&gt;&lt;code&gt;", "&lt;code&gt; ::= &lt;lowercase&gt; | &lt;symbol&gt; | &lt;digit&gt; | &lt;lowercase&gt;&lt;code&gt; | &lt;symbol&gt;&lt;code&gt; | &lt;digit&gt;&lt;code&gt;"]) + "</p>", "Writing &lt;passcode&gt; with only the three alternatives and no recursion. The loop lets any number of characters follow the uppercase letter.") + peq(SRC("s25", "32", "Q9"), "1 + 1 + 3 + 1 marks", "State / Complete",
  "The diagrams define a letter (A B C D E F G H J K), a digit (0 to 9), an operator (+ - * / ^) and a variable." + D_VAR25 + "(a) State why 9K is not a valid variable. (b) Complete the BNF for &lt;operator&gt;. (c) An expression is a variable assigned to a variable followed by an operator followed by another variable. The operator and final variable can be repeated as many times as necessary. Complete the syntax diagram for an expression (the first two boxes, variable and =, are given). (d) A variable must also have at least four characters to pass validation. State one example of a valid variable.",
  "(c) after the first variable and =, the variable, operator, variable chain with a loop.",
  "<p><b>(a)</b> " + mks(["Variables must begin with a letter, not a digit"]) + "</p><p><b>(b)</b> " + mks(["&lt;operator&gt; ::= + | - | * | / | ^"]) + "</p><p><b>(c)</b> " + mks(["Two variable boxes added to the diagram", "One operator box added and all boxes in the correct order", "Connections, arrows and the return loop correct, with no additional boxes or connections"]) + "</p>" + D_EXP25 + "<p><b>(d)</b> " + mks(["For example AC768: begins with a letter, followed by any letters or digits, at least four characters"], "a") + "</p>", "Drawing the loop round operator only, or round the whole expression. The loop goes round operator and the final variable together.") + peq(SRC("s25", "33", "Q9"), "1 + 3 + 2 marks", "State / Complete / Draw",
  "The diagrams define upper (J K L V X Z), lower (a e i p u y), digit (0 to 9) and passcode." + D_PCIN33 + "(a) State why JJ90 is not a valid passcode. (b) Complete the BNF for &lt;upper&gt; and &lt;passcode&gt;. (c) A character can be an upper, a lower or a digit. The rules have changed so the third character may also be selected from upper and the final character may be repeated one or more times. Complete the syntax diagram for passcode to show these changes.",
  "The two middle characters are each a lower or a digit.",
  "<p><b>(a)</b> " + mks(["The second character must come from lower or digit; it cannot be upper"]) + "</p><p><b>(b)</b> " + mks(["&lt;upper&gt; ::= J | K | L | V | X | Z", "Any two correct options for &lt;passcode&gt;", "The remaining two options correct"]) + "</p><pre class=\"plain\">&lt;passcode&gt; ::= &lt;upper&gt;&lt;lower&gt;&lt;lower&gt;&lt;digit&gt; | &lt;upper&gt;&lt;lower&gt;&lt;digit&gt;&lt;digit&gt; |\n               &lt;upper&gt;&lt;digit&gt;&lt;digit&gt;&lt;digit&gt; | &lt;upper&gt;&lt;digit&gt;&lt;lower&gt;&lt;digit&gt;</pre><p>Or with an interim rule: &lt;passcode&gt; ::= &lt;upper&gt;&lt;middle&gt;&lt;middle&gt;&lt;digit&gt; and &lt;middle&gt; ::= &lt;lower&gt; | &lt;digit&gt;.</p><p><b>(c)</b> " + mks(["A box for upper in the correct place with the correct connections", "The correct repetition arrow for the final digit"]) + "</p>" + D_PCOUT33, "Putting the loop round both the third character and the final digit. The loop is only on the last digit.")

review = req("3 marks", "Write", "Write the BNF for a rule &lt;word&gt; that is one or more letters, given that &lt;letter&gt; ::= A | B | C. Then say which part ends the repetition.", "Recursion with a non-recursive alternative.", "<p>" + mks(["&lt;word&gt; ::= &lt;letter&gt; | &lt;word&gt;&lt;letter&gt;", "The first alternative &lt;letter&gt; ends the repetition", "The second alternative adds one more letter to an existing word"]) + "</p>", None) + req("2 marks", "Write", "A code is an odd digit followed by an optional letter. Write the BNF given &lt;odd&gt; and &lt;letter&gt; are defined.", "Optional means two alternatives.", "<p>" + mks(["&lt;code&gt; ::= &lt;odd&gt;", "| &lt;odd&gt;&lt;letter&gt;"]) + "</p>", None) + req("3 marks", "Draw", "Draw a syntax diagram for a PIN: exactly four digits.", "Four boxes in a row.", "<p>" + mks(["The name PIN with an arrow in and an arrow out", "Four rectangles labelled digit in sequence", "No loops or bypasses"]) + "</p>" + sx("PIN", S(R("digit"), R("digit"), R("digit"), R("digit"))), None) + req("2 marks", "State", "Using the password diagram of one or more letters, then one or more digits, then one or more symbols, state why A1 is not valid and give a valid string.", "What is missing?", "<p>" + mks(["A1 has no symbol at the end, and a symbol is required", "A valid string is for example A1$"]) + "</p>", None) + req("2 marks", "Explain", "Explain how a loop in a syntax diagram is written in BNF.", "Recursion.", "<p>" + mks(["The rule is defined using its own name (recursion)", "There must also be a non-recursive alternative so that the repetition can stop"]) + "</p>", None)

exam = exam20("Part 1 is real 9618 questions on syntax diagrams and BNF (Paper 3), 2021 to 2025. Part 2 is a set of review questions for practice; they are not in exam format.", where, past, review)

tips = tips_html([
  ("Follow the arrows.", "A string is valid only if some route through the diagram makes it."),
  ("Give the reason.", "Begins with a digit, symbol before digits, a character that is not allowed, too many digits."),
  ("::= and |.", "BNF: ::= means is defined as, | means or."),
  ("Repeat = recursion.", "&lt;word&gt; ::= &lt;letter&gt; | &lt;word&gt;&lt;letter&gt;."),
  ("Optional = two alternatives.", "One with the part, one without."),
  ("Diagram: name, arrows, boxes.", "Label it, put arrows on every line, add loops and bypasses carefully."),
], [
  ("BNF", "Backus-Naur Form: a notation for the grammar of a language."),
  ("a terminal", "A symbol that appears exactly as written."),
  ("a non-terminal", "The name of a rule, written in angle brackets."),
  ("recursion in BNF", "A rule that uses its own name, to allow repetition."),
], [("State", "Give the reason, referring to the diagram."), ("Complete", "Finish the rule or diagram given."), ("Draw", "Boxes, arrows, loops and the name."), ("Write", "BNF with ::= and |.")]) + FC

js = AKJS + AK20JS + r'''
(function () {
  const run = (str, cap0) => { const E = [["letter", /[ADPRY]/], ["digit", /[0-9]/], ["symbol", /[$%&@#]/]];
    const steps = [{ i: 0, cap: cap0 }]; let e = 0, ok = true, doneChars = [];
    for (let i = 0; i < str.length && ok; i++) { const c = str[i]; let m = -1; for (let j = e; j < 3; j++) if (E[j][1].test(c) && (j === e || doneChars.length)) { m = j; break; }
      if (m < 0) { steps.push({ i: i + 1, bad: i, cap: `<b>${c}</b>: no route allows this here. ` + (E[0][1].test(c) || E[1][1].test(c) ? "The diagram only moves forward through letters, then digits, then symbols; after a symbol no letters or digits are allowed." : "It is not one of the allowed characters.") + " The string is <b>invalid</b>." }); ok = false; break; }
      e = m; doneChars.push([c, m]); steps.push({ i: i + 1, cap: `<b>${c}</b> matches <b>${E[m][0]}</b>.` }); }
    return { steps, E }; };
  const make = (el, str, cap0) => { const { steps } = run(str, cap0), E = ["letter", "digit", "symbol"], R = [/[ADPRY]/, /[0-9]/, /[$%&@#]/];
    const assign = []; let e = 0; for (const c of str) { let m = -1; for (let j = e; j < 3; j++) if (R[j].test(c)) { m = j; break; } if (m < 0) { assign.push(-1); break; } e = m; assign.push(m); }
    const draw = (s) => { const k = Math.round(s.i); let o = SV.text(20, 22, "password", "lbl bd");
      E.forEach((n, j) => { const used = assign.slice(0, k).some((a) => a === j), cur = k > 0 && assign[k - 1] === j; o += SV.rect(30 + j * 190, 34, 130, 40, cur ? "cell-warn" : used ? "cell-ok" : "cell", { rx: 4 }) + SV.text(95 + j * 190, 59, n + " (one or more)", "lbl", { "text-anchor": "middle", style: "font-size:12px" }); if (j < 2) o += SV.path("M" + (160 + j * 190) + ",54 H" + (220 + j * 190), "ax"); });
      o += SV.text(20, 118, "string", "sm"); [...str].forEach((c, i) => { const bad = assign[i] === -1; const on = i < k; o += SV.rect(20 + i * 52, 126, 46, 40, on ? (bad ? "cell-no" : "cell-ok") : "cell", { rx: 6, ...op(on ? 1 : 0.4) }) + SV.text(43 + i * 52, 153, c, "lbl bd", { "text-anchor": "middle", style: "font-size:18px;font-family:var(--mono)" }); });
      return o; };
    Lib.stepper(el, { w: 640, h: 190, label: "Syntax diagram path", base: { i: 0 }, draw, tween: 120, dwell: 1900, steps: steps.map((x) => ({ cap: x.cap, s: { i: x.i } })) }); };
  make($("#stA"), "DPAD99$", "String <b>DPAD99$</b>: does the password diagram accept it? It needs letters, then digits, then symbols.");
  make($("#stB"), "DAD#95", "String <b>DAD#95</b>: follow it through the same diagram.");
})();
(function () {
  const steps = [["&lt;word&gt;", "Start with the rule &lt;word&gt;."], ["&lt;word&gt;&lt;letter&gt;", "Use the second alternative: &lt;word&gt; ::= &lt;word&gt;&lt;letter&gt;. One more letter will be added."], ["&lt;word&gt;&lt;letter&gt;&lt;letter&gt;", "Use the second alternative again for the &lt;word&gt;."], ["&lt;letter&gt;&lt;letter&gt;&lt;letter&gt;", "Use the first alternative: &lt;word&gt; ::= &lt;letter&gt;. This <b>ends</b> the recursion."], ["A B C", "Replace each &lt;letter&gt; with a terminal from &lt;letter&gt; ::= A | B | C. The string <b>ABC</b> is valid."]];
  const draw = (s) => { const k = Math.round(s.i); let o = SV.text(20, 22, "<word> ::= <letter> | <word><letter>", "lbl bd", { style: "font-family:var(--mono);font-size:14px" }); steps.slice(0, k + 1).forEach(([t], i) => { const txt = t.replace(/&lt;/g, "<").replace(/&gt;/g, ">"); o += SV.rect(20, 44 + i * 46, 440, 38, i === k ? "cell-warn" : "cell-ok", { rx: 6 }) + SV.text(34, 69 + i * 46, (i ? "→  " : "") + txt, "lbl", { style: "font-family:var(--mono);font-size:15px" }); }); return o; };
  Lib.stepper($("#stC"), { w: 520, h: 290, label: "Derivation", base: { i: 0 }, draw, tween: 120, dwell: 2600, steps: steps.map((x, i) => ({ cap: x[1], s: { i } })) });
})();

const GR = {
  "Password (M/J 2023)": { re: /^([ADPRY]+)([0-9]+)([$%&@#]+)$/, d: "letters A D P R Y, then digits, then symbols $ % & @ #", parts: ["letter", "digit", "symbol"], ex: "DPAD99$" },
  "Variable (M/J 2023, P32)": { re: /^([ACEGIKMOQSUWY]+)([0-9]?)$/, d: "one or more letters (A C E G I K M O Q S U W Y), then at most one digit", parts: ["letters", "optional digit"], ex: "UWY" },
  "Number (O/N 2024)": { re: /^([13579])([0-9]?)$/, d: "an odd digit, then optionally one more digit (odd or even)", parts: ["odd", "optional digit"], ex: "135" },
  "Passcode (M/J 2025)": { re: /^([ACEGJ])((?:[bdfhk]|[$@#&%]|[0-9])+)$/, d: "uppercase (A C E G J), then one or more lowercase (b d f h k), symbols or digits", parts: ["uppercase", "rest"], ex: "J%d7" }
};
(function () {
  const b = $("#vB"), inp = $("#vI"); let cur = Object.keys(GR)[0];
  const paint = () => { const g = GR[cur]; const s = inp.value; $("#vD").innerHTML = `<p><b>${cur}:</b> ${g.d}.</p>`; let r = g.re.test(s); let why = "";
    if (!r) { if (!s) why = "The string is empty."; else { const first = s[0]; if (cur.startsWith("Password") && !/[ADPRY]/.test(first)) why = "It must begin with a letter A, D, P, R or Y."; else if (cur.startsWith("Variable") && !/[ACEGIKMOQSUWY]/.test(first)) why = "It must begin with a letter from the diagram."; else if (cur.startsWith("Number") && !/[13579]/.test(first)) why = "It must begin with an odd digit."; else if (cur.startsWith("Number") && s.length > 2) why = "At most two digits are allowed."; else if (cur.startsWith("Passcode") && !/[ACEGJ]/.test(first)) why = "It must begin with an uppercase letter from the diagram."; else why = "A character is not allowed where it appears, or a required part is missing or out of order."; } }
    $("#vV").innerHTML = r ? `<b style="color:var(--good)">${s}</b> is <b>valid</b>.` : `<b style="color:var(--bad)">${s || "(empty)"}</b> is <b>invalid</b>. ${why}`;
    b.querySelectorAll("button").forEach((x) => (x.className = x.dataset.k === cur ? "on" : "")); };
  Object.keys(GR).forEach((k) => { const x = document.createElement("button"); x.textContent = k; x.dataset.k = k; x.onclick = () => { cur = k; inp.value = GR[k].ex; paint(); }; b.appendChild(x); });
  inp.oninput = paint; paint();
})();
const BN = [["Choice of symbols", "&lt;symbol&gt; ::= $ | % | &amp; | @ | #", "SYMBOL"], ["Optional digit", "&lt;number&gt; ::= &lt;odd&gt; | &lt;odd&gt;&lt;even&gt; | &lt;odd&gt;&lt;odd&gt;", "NUMBER"], ["One or more letters", "&lt;word&gt; ::= &lt;letter&gt; | &lt;word&gt;&lt;letter&gt;", "WORD"], ["Sequence", "&lt;code&gt; ::= &lt;letter&gt;&lt;number&gt;&lt;symbol&gt; | &lt;letter&gt;&lt;number&gt;&lt;number&gt;&lt;symbol&gt;", "CODE"]];
(function () {
  const DG = { SYMBOL: DSYM, NUMBER: DNUM, WORD: DWORD, CODE: DCODE }; const b = $("#bB");
  const show = (i) => { $("#bO").innerHTML = `<h3>${BN[i][0]}</h3><pre class="plain">${BN[i][1]}</pre>` + DG[BN[i][2]]; b.querySelectorAll("button").forEach((x, j) => (x.className = j === i ? "on" : "")); };
  BN.forEach((o, i) => { const x = document.createElement("button"); x.textContent = o[0]; x.onclick = () => show(i); b.appendChild(x); }); show(0);
})();
''' + CLASSIFY("cl1", "Is it a terminal or a non-terminal?", ["Terminal", "Non-terminal"],
  [("$", 0), ("&lt;digit&gt;", 1), ("A", 0), ("&lt;password&gt;", 1), ("7", 0), ("&lt;code&gt;", 1)],
  "Terminals are the characters themselves; non-terminals are names of rules in angle brackets.") + CLASSIFY("cl2", "Which BNF feature does it use?", ["Alternatives (|)", "Sequence", "Recursion"],
  [("&lt;bit&gt; ::= 0 | 1", 0), ("&lt;pair&gt; ::= &lt;letter&gt;&lt;digit&gt;", 1), ("&lt;word&gt; ::= &lt;letter&gt; | &lt;word&gt;&lt;letter&gt;", 2), ("&lt;sign&gt; ::= + | -", 0), ("&lt;code&gt; ::= &lt;digit&gt;&lt;code&gt; | &lt;digit&gt;", 2), ("&lt;id&gt; ::= &lt;letter&gt;&lt;digit&gt;&lt;digit&gt;", 1)],
  "| for choices, side by side for sequence, own name for repetition.") + MATCH([
  ["Rounded box", "A terminal that appears as written"], ["Rectangle", "A non-terminal: the name of another rule"], ["Loop back", "One or more repeats"], ["Bypass line", "An optional element"], ["::=", "Is defined as"]]) + ORDER(
  "Put the steps for drawing a syntax diagram in order.",
  ["Write the name of the rule at the top left", "Draw the elements in order", "Add a choice where the description says or", "Add loops for repetition and bypasses for options", "Check that every line has an arrow"],
  "Name, order, choices, loops and bypasses, arrows.") + CALC([
  {"q": "In the password diagram (one or more letters, one or more digits, one or more symbols) what is the smallest number of characters in a valid password?", "a": 3, "unit": "", "tol": 0.01, "hint": "One of each.", "sol": "<b>3</b>."},
  {"q": "A number is an odd digit followed by an optional digit (odd or even). How many different lengths of valid number are there?", "a": 2, "unit": "", "tol": 0.01, "hint": "One or two digits.", "sol": "<b>2</b>."},
  {"q": "&lt;number&gt; ::= &lt;odd&gt; | &lt;odd&gt;&lt;even&gt; | &lt;odd&gt;&lt;odd&gt; with 5 odd digits and 5 even digits: how many one-digit numbers are valid?", "a": 5, "unit": "", "tol": 0.01, "hint": "Any odd digit.", "sol": "<b>5</b>."},
  {"q": "The same rule: how many two-digit numbers are valid (5 × (5 + 5))?", "a": 50, "unit": "", "tol": 0.01, "hint": "Odd then any digit.", "sol": "5 × 10 = <b>50</b>."},
  {"q": "How many alternatives does &lt;word&gt; ::= &lt;letter&gt; | &lt;word&gt;&lt;letter&gt; have?", "a": 2, "unit": "", "tol": 0.01, "hint": "Count the |.", "sol": "<b>2</b>."}]) + MCQ([
  ("What does ::= mean in BNF?", ["Equals zero", "Is defined as", "Is not", "Repeat"], 1, "Is defined as."),
  ("How is repetition written in BNF?", ["With a star", "With recursion", "With a loop symbol", "It cannot be written"], 1, "A rule that uses its own name."),
  ("A rectangle in a syntax diagram is:", ["A terminal", "A non-terminal", "An error", "An arrow"], 1, "The name of another rule."),
  ("A bypass line in a syntax diagram makes an element:", ["Repeat", "Optional", "Compulsory", "Invalid"], 1, "Optional."),
  ("Why is DAD#95 invalid for letters, digits, then symbols?", ["It is too long", "The symbol comes before the digits", "It has no letters", "It has no digits"], 1, "Wrong order."),
  ("Which stage of compilation uses the grammar?", ["Syntax analysis", "Lexical analysis", "Code generation", "Linking"], 0, "Syntax analysis.")], "qz1") + CARDS([
  ("Syntax diagram", "Boxes and arrows showing allowed structure."), ("BNF", "Text notation: <name> ::= definition."), ("|", "Or: a choice between alternatives."), ("Recursion", "A rule that uses its own name to repeat."),
  ("Terminal", "A character that appears as written."), ("Non-terminal", "A named rule in angle brackets."), ("Loop", "One or more repeats."), ("Bypass", "Optional element.")])

DSYM = sx("symbol", A(*[T(c) for c in "$%&@#"]))
build("ac1622", "ac-16-2-2-syntax-diagrams-bnf", "Syntax Diagrams and BNF", EYA("16.2.2"),
  "How to read and draw syntax diagrams and write Backus-Naur Form, including recursion for repetition; animations, a string checker and the real Paper 3 questions from 2021 to 2025.",
  dict(sub=CBK("Chapter 16 · System software, section 16.2 Translation software"), **tabs(learn, watch, explore, practise, real, exam, tips)), "const DSYM = " + json.dumps(DSYM) + ", DNUM = " + json.dumps(D_NUM24) + ", DWORD = " + json.dumps(sx("word", A(R("letter"), S(R("word"), R("letter"))))) + ", DCODE = " + json.dumps(D_CODE24) + ";\n" + js)
