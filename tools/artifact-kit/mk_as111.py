"""AS CS 11.1: programming basics. Run: python3 tools/artifact-kit/mk_as111.py"""
from ascs import *

def pc(text, label=None): return code(text.strip("\n").split("\n"), label=label)
def tbl(head, rows, cls="t mono"):
    return '<div class="tw"><table class="%s"><tr>%s</tr>%s</table></div>' % (cls, "".join("<th>%s</th>" % h for h in head), "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % c for c in r) for r in rows))

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>A program stores data in <b>variables</b> and <b>constants</b>, each with an <b>identifier</b> (a meaningful name) and a <b>data type</b>: INTEGER, REAL, CHAR, STRING, BOOLEAN or DATE. An <b>identifier table</b> lists each identifier with its type, purpose and an example value. <b>Operators</b> (arithmetic, comparison, logical, string &amp;) and <b>built-in functions</b> (LENGTH, LEFT, RIGHT, MID, INT, NUM_TO_STR, STR_TO_NUM, IS_NUM, MONTH ...) are used to build <b>expressions</b>, and each operator and function needs operands of the right type. Evaluating an expression means working out its value step by step, in the correct order. Many exam marks come from either evaluating an expression or <b>spotting the type error</b> in one.</p></div>

  <h2>1 · Data types</h2>
  ''' + tbl(["Type", "Stores", "Example"], [["INTEGER", "A whole number", "29, -4"], ["REAL", "A number that may have a decimal part", "5.42, 15.75"], ["CHAR", "One character (single quotes)", "'X'"], ["STRING", "Zero or more characters (double quotes)", "\"Wong\", \"18/04/2021\""], ["BOOLEAN", "TRUE or FALSE", "TRUE"], ["DATE", "A date", "19/02/1983"]]) + '''
  <p>The data type is decided by <b>how the value is used</b>, not how it looks: a phone number or a date written in quotes is a STRING, and an exam question such as "number of items" is an INTEGER. A value that can have only two states (a flag, whether a customer is new) is BOOLEAN.</p>

  <h2>2 · Identifiers, variables and constants</h2>
  <ul>
    <li>Choose a <b>meaningful name</b> (MemberName, NumItems, NewCustomer, Deposit) and declare it with its type: <span class="mono">DECLARE Points : INTEGER</span>.</li>
    <li>A <b>variable</b> can change while the program runs; a <b>constant</b> is set once (<span class="mono">CONSTANT VATRate ← 0.2</span>) and makes the program easier to read and to change.</li>
    <li>An <b>identifier table</b> gives the name, data type, a description of its purpose and often an example value. Other things it may include: the number of elements of an array or the length of a string, the value of a constant, and the <b>scope</b> (local or global).</li>
    <li>Assignment: <span class="mono">Total ← 0</span>. A value must match the variable's type.</li>
  </ul>

  <h2>3 · Operators</h2>
  ''' + tbl(["Group", "Operators", "Result type"], [["Arithmetic", "+  -  *  /  ^  DIV  MOD", "number (/ gives REAL)"], ["Comparison", "=  &lt;&gt;  &lt;  &gt;  &lt;=  &gt;=", "BOOLEAN"], ["Logical", "AND  OR  NOT", "BOOLEAN (operands must be BOOLEAN)"], ["String join", "&amp;", "STRING (operands must be strings or chars)"]]) + '''
  <ul>
    <li><b>DIV</b> is integer division: 17 DIV 5 = 3. <b>MOD</b> is the remainder: 17 MOD 5 = 2. <b>/</b> gives a real: 17 / 5 = 3.4.</li>
    <li>Order: brackets, then ^, then * / DIV MOD, then + −, then comparisons, then NOT, AND, OR. Use brackets to be sure.</li>
    <li>Common errors: <span class="mono">&amp;</span> on numbers, <span class="mono">+</span> on a string and a number, <span class="mono">x = 3 OR 4</span> (each side of OR must be a complete comparison: <span class="mono">x = 3 OR x = 4</span>), and AND with a value that is not BOOLEAN.</li>
  </ul>

  <h2>4 · Built-in functions</h2>
  ''' + tbl(["Function", "Returns", "Example"], [["LENGTH(s)", "number of characters", "LENGTH(\"Password\") = 8"], ["LEFT(s, n)", "first n characters", "LEFT(\"Cambridge\", 4) = \"Camb\""], ["RIGHT(s, n)", "last n characters", "RIGHT(\"AB12345\", 3) = \"345\""], ["MID(s, start, n)", "n characters from position start (first is 1)", "MID(\"pseudocode\", 4, 1) = \"u\""], ["UCASE(s) / LCASE(s)", "upper / lower case", "(CHAR or STRING as defined; TO_UPPER, TO_LOWER)"], ["NUM_TO_STR(x)", "a number as a string", "NUM_TO_STR(20) = \"20\""], ["STR_TO_NUM(s)", "a string as a number", "STR_TO_NUM(\"37\") + 5 = 42"], ["IS_NUM(s)", "TRUE if the string can be a number", "IS_NUM(\"-23.4\") = TRUE"], ["INT(x)", "the whole-number part", "INT(5.42) = 5"], ["MONTH(d) DAY(d) YEAR(d)", "parts of a DATE", "MONTH(23/04/2004) = 4"], ["ASC(c) / CHR(n)", "character code / character", "ASC('A') = 65"], ["RAND(n)", "a random real from 0 up to n", "RAND(10)"]]) + '''
  <p>Each function wants a particular <b>type</b>: <span class="mono">IS_NUM</span> needs a string (not a number), <span class="mono">LCASE</span> works on a character (or string), <span class="mono">INT</span> needs a number, and <span class="mono">NUM_TO_STR</span> needs a number, so <span class="mono">NUM_TO_STR(Index + "33")</span> is an error (a number plus a string).</p>

  <h2>5 · Evaluating an expression</h2>
  <p>Work out the innermost brackets or functions first, write each intermediate value, and give a final answer of the right type: strings in quotes, REAL results with their decimals (249.50), BOOLEAN as TRUE or FALSE. If a part is invalid, the answer is <b>ERROR</b>.</p>
  ''' + pc('''
// Total = 124.00, DepRate = 2.00, Description = "AB12345:Cleaning Brush (small)"
(Total * DepRate) + 1.5                    // 249.50
RIGHT(Description, 7)                      // "(small)"
(LENGTH(Description) - 8) > 16             // 30 - 8 = 22 > 16, TRUE
NUM_TO_STR(INT(DepRate * 10)) & '%'        // INT(20.0) = 20, so "20%"''') + '''

  <h2>Common ways to lose marks</h2>
  <ul>
    <li>Variable names such as X or Data1, or a type that does not match the example value.</li>
    <li>Quoting a number, or dropping the quotes from a string or character answer.</li>
    <li>Writing "error" for a statement that is valid, or the other way round: read each operator and each function's parameter type.</li>
    <li>Starting MID at position 0 (the first character is position 1).</li>
  </ul>
'''

watch = '''
  <h2>1 · Evaluating step by step</h2>
  <div id="stA"></div>
  <h2>2 · MID, LEFT and RIGHT on a string</h2>
  <div id="stB"></div>
  <h2>3 · DIV, MOD and /</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · String functions</h2>
  <p>Change the string and the numbers. Positions start at 1.</p>
  <div class="card"><div class="btnrow"><label>String <input id="sf_s" value="AB12345:Cleaning Brush" size="26"></label></div><div class="btnrow"><label>n <input id="sf_n" type="number" min="0" max="30" value="4" style="width:60px"></label><label>start <input id="sf_st" type="number" min="1" max="30" value="3" style="width:60px"></label></div><div id="sfV"></div></div>
  <h2>Lab 2 · Evaluate it</h2>
  <p>Values: Total = 124.00, DepRate = 2.00, Index = 100, Result = 5.42, MonthLetter = "JFMAMJJASOND", Birthday = 15/11/2009. Pick an expression, then reveal.</p>
  <div class="card"><div id="evB" class="btnrow"></div><div id="evV"></div></div>
  <h2>Lab 3 · Spot the error</h2>
  <div class="card"><div id="erB" class="btnrow"></div><div id="erO"></div></div>
'''

_pr, _prjs = PR(["Choose the data type", "Valid or error?", "Match the function to its job", "Put the evaluation steps in order", "Working out", "Multiple choice"],
  ("Which data type?", ["INTEGER", "REAL", "STRING", "BOOLEAN", "DATE"], [("The number of items in an order (3)", 0), ("The deposit paid, 15.75", 1), ("A customer name, \"Mr Khan\"", 2), ("Whether a customer is new (TRUE)", 3), ("A membership start date, 19/02/1983", 4), ("A postcode, \"CB2 1TN\"", 2)], "Whole number, decimal, text, two-state, date."),
  ("Does each statement contain a type error?", ["No error", "Error"], [("Result ← 2 + 4", 0), ("Result ← 2 & 4", 1), ("Status ← TRUE AND FALSE", 0), ("IF LENGTH(\"Password\") < \"10\" THEN", 1), ("X ← STR_TO_NUM(\"37\") + 5", 0), ("Message ← \"Done\" + LENGTH(MyString)", 1)], "Operators and functions need the right types."),
  [["LENGTH", "Number of characters"], ["MID", "Characters from a given position"], ["INT", "Whole-number part"], ["NUM_TO_STR", "Number into a string"], ["IS_NUM", "Tests if a string is a number"]],
  ("Put the steps for evaluating INT(DepRate * 10) & '%' in order.", ["Replace DepRate with its value 2.00", "Evaluate DepRate * 10 = 20.0", "Apply INT to give 20", "Convert to a string with NUM_TO_STR as needed: \"20\"", "Join with & '%' to give \"20%\""], "Innermost first."),
  [{"q": "What is 29 DIV 6?", "a": 4, "unit": "", "tol": 0.01, "hint": "Whole number of times 6 goes into 29.", "sol": "<b>4</b>."}, {"q": "What is 100 MOD 30?", "a": 10, "unit": "", "tol": 0.01, "hint": "Remainder after dividing by 30.", "sol": "<b>10</b>."}, {"q": "What is LENGTH(\"AB12345:Cleaning Brush (small)\") − 8?", "a": 22, "unit": "", "tol": 0.01, "hint": "Count the characters: 30.", "sol": "<b>22</b> (the length is 30)."}, {"q": "MONTH(15/11/2009) − 2 is which position in \"JFMAMJJASOND\"?", "a": 9, "unit": "", "tol": 0.01, "hint": "11 − 2.", "sol": "<b>9</b>, which is 'S'."}, {"q": "INT(5.42) + 1 gives what?", "a": 6, "unit": "", "tol": 0.01, "hint": "INT drops the decimal part.", "sol": "<b>6</b>."}],
  [("The data type of a flag that is TRUE or FALSE:", ["BOOLEAN", "STRING", "CHAR", "INTEGER"], 0, "Two states."), ("RIGHT(\"AB12345\", 3) gives:", ["\"345\"", "\"AB1\"", "\"123\"", "345"], 0, "Last three characters, still a string."), ("Which is an error?", ["NUM_TO_STR(5 + \"3\")", "STR_TO_NUM(\"37\") + 5", "INT(4.9)", "LENGTH(\"cat\")"], 0, "Number plus string."), ("An identifier table may include:", ["The scope and an example value", "The program output only", "The mark scheme", "Nothing but the names"], 0, "Name, type, purpose, example."), ("17 MOD 5 =", ["2", "3", "3.4", "12"], 0, "Remainder."), ("A constant:", ["Is set once and not changed", "Changes every loop", "Is a type of loop", "Stores only strings"], 0, "Fixed value.")],
  [("INTEGER", "Whole number."), ("REAL", "Number with a decimal part."), ("STRING", "Text in double quotes."), ("BOOLEAN", "TRUE or FALSE."), ("DIV / MOD", "Quotient / remainder."), ("MID(s, a, n)", "n characters from position a."), ("NUM_TO_STR", "Number to string."), ("IS_NUM", "Needs a string.")])

real = RWNOTE + (
rw("A sign-up form", "The form stores a name as a string, an age as an integer, a price as a real and 'agreed to the terms' as a Boolean.", "choosing types for data.") +
rw("A spreadsheet formula", "A formula such as =LEFT(A2, 3) and =LEN(A2) uses the same functions on text, and an error appears if a number is used as text.", "functions and type errors.") +
rw("Checking a phone number", "A program uses IS_NUM and LENGTH to check that a typed value is only digits and has the right number of characters.", "built-in functions.") +
rw("Totalling a till", "Prices are reals and the number of items is an integer; DIV and MOD split pence into pounds and pence.", "DIV, MOD and types.")
)

where = [
  ("M/J 2021", "21", "1", "4 + 5 + 3", "Complete an identifier table; describe the error in five statements; choose a data structure"),
  ("M/J 2022", "22", "1", "1 + 4 + 2 + 4", "Breakpoint; life cycle stages; identifier table contents; the error in four statements"),
  ("M/J 2022", "23", "1", "5 + 3", "Evaluate Boolean expressions; an example of a Boolean variable"),
  ("O/N 2022", "21", "1", "3 + 5 + 4", "Library routines; arrays and the index variable; the error in four statements"),
  ("O/N 2022", "22", "1", "3", "Evaluate three expressions using MID, INT, MONTH and DAY"),
  ("O/N 2023", "22", "1", "4 + 4 + 3", "Identifier table; evaluate four expressions; store data of different types"),
  ("O/N 2024", "23", "1", "3 + 3", "Data types; evaluate three expressions (one is an ERROR)"),
  ("O/N 2025", "22", "1", "3 + 4", "Data types; evaluate four expressions (one is an ERROR)")]

past = '''  <p class="note">Question 1 of Paper 2 is nearly always an identifier table, a table of expressions to evaluate and a table of statements to check for errors. These are the quickest marks on the paper; practise them until you can do them without hesitation.</p>
''' + peq(SRC("s21", "21", "Q1"), "4 + 5 + 3 marks", "Complete / Describe / State",
  "(a) A football club's program stores: the preferred name of the member (\"Wong\"); whether an existing member lives at the same address (FALSE); when the member joined (19/02/1983); the points a member has earned (1345). Complete an identifier table with a variable name and data type for each. (b) Describe the error in each statement, or write NO ERROR: Result ← 2 & 4; SubString ← MID(\"pseudocode\", 4, 1); IF x = 3 OR 4 THEN; Result ← Status AND INT(x/2); Message ← \"Done\" + LENGTH(MyString). (c) The name (a string) and test score (an integer) are stored for each student in a group: state a suitable data structure and justify it.", "Meaningful names and types. Check each operator's operands. A record holds mixed types.",
  "<p><b>(a)</b> One mark for each sensible variable name with its data type." + tbl(["Example value", "Variable name", "Data type"], [["\"Wong\"", "MemberName", "STRING"], ["FALSE", "FamilyMember", "BOOLEAN"], ["19/02/1983", "StartDate", "DATE"], ["1345", "Points", "INTEGER"]]) + "</p><p><b>(b)</b> One mark per row:" + tbl(["Statement", "Error"], [["Result ← 2 &amp; 4", "&amp; is a string operator: should be an arithmetic operator (or 2 and 4 should be a CHAR or STRING)"], ["SubString ← MID(\"pseudocode\", 4, 1)", "NO ERROR"], ["IF x = 3 OR 4 THEN", "4 is not a Boolean value: the condition is incorrect (x = 3 OR x = 4)"], ["Result ← Status AND INT(x/2)", "INT(x/2) does not evaluate to a Boolean: wrong operator"], ["Message ← \"Done\" + LENGTH(MyString)", "Cannot add a string and a number: \"Done\" is not a number"]], "t") + "</p><p><b>(c)</b> " + mks(["Structure: record", "Allows different data types", "to be stored under one identifier"]) + " Alternative: two 1D arrays (one string, one integer), with the same index linking the name with the score.</p>", "Writing data types that are a reasonable guess from the explanation rather than the example value: \"1345\" is an INTEGER, not a STRING.") + peq(SRC("s22", "22", "Q1(c)(d)"), "2 + 4 marks", "State",
  "(c) An identifier table includes the names of identifiers used. State two other pieces of information it should contain. (d) The pseudocode statements may contain errors. State the error in each case or write NO ERROR: Status ← TRUE AND FALSE; IF LENGTH(\"Password\") < \"10\" THEN; Code ← LCASE(\"Electrical\"); Result ← IS_NUM(-27.3).", "Purpose, type, scope, example. Check each parameter type.",
  "<p><b>(c)</b> Any two: " + mks(["A description of what the identifier is used for", "The data type of the identifier", "The number of elements of an array, or the length of a string", "An example data value", "The value of any constants", "The scope of the variable (local or global)"], "b") + "</p><p><b>(d)</b> One mark per row:" + tbl(["Statement", "Error"], [["Status ← TRUE AND FALSE", "NO ERROR"], ["IF LENGTH(\"Password\") &lt; \"10\" THEN", "\"10\" should not be a string: it must be an integer"], ["Code ← LCASE(\"Electrical\")", "The parameter must be a char, not a string (or LCASE should be TO_LOWER)"], ["Result ← IS_NUM(-27.3)", "The parameter must be a string or char, not a number"]], "t") + "</p>", "Describing what the statement does instead of what is wrong with it.") + peq(SRC("w22", "21", "Q1(b)(c)"), "5 + 4 marks", "Explain / State",
  "A program stores names and test marks in separate variables Name1, Name2, Name3 and Mark1, Mark2, Mark3. (b)(i) The program must now hold data for up to 30 students: explain why arrays are good practice. (ii) OUTPUT \"Student \", Name[Count], \" scored \", Mark[Count]: state the purpose of Count and give its data type. (c) State the error in each case, or NO ERROR: IF EMPTY = \"\" THEN; Status ← IS_NUM(-23.4); X ← STR_TO_NUM(\"37\") + 5; Y ← STR_TO_NUM(\"37\" + \"5\").", "Loop with an index; one identifier. Count is the index (INTEGER). Check IS_NUM's parameter.",
  "<p><b>(b)(i)</b> " + mks(["The algorithm to process, search or organise the data is easier to implement (a loop with an index goes through the values)", "The program is easier to design, code, test and understand", "Many values are referenced by one identifier, so fewer identifiers are needed and the program is easier to amend when the number of students changes"]) + "</p><p><b>(ii)</b> " + mks(["Purpose: it identifies a single array element (provides the index)", "Data type: INTEGER"], "a") + "</p><p><b>(c)</b> One mark per row:" + tbl(["Statement", "Error"], [["IF EMPTY ← \"\" THEN", "Should be = (a comparison), not ←"], ["Status ← IS_NUM(-23.4)", "The parameter should be a string (or char), not a real"], ["X ← STR_TO_NUM(\"37\") + 5", "NO ERROR"], ["Y ← STR_TO_NUM(\"37\" + \"5\")", "Wrong operator: should be &amp; (or the parameter is not a string)"]], "t") + "</p>", None) + peq(SRC("w22", "22", "Q1(c)"), "3 marks", "Complete",
  "FlagDay is a DATE (23/04/2004), CharList is a STRING (\"ABCDEF\"), Count is an INTEGER (29). Evaluate: MID(CharList, MONTH(FlagDay), 1); INT(Count / LENGTH(CharList)); (Count >= 29) AND (DAY(FlagDay) > 23).", "MONTH = 4; 29 / 6 = 4.83; 23 > 23 is FALSE.",
  "<p>One mark per row:" + tbl(["Expression", "Evaluation"], [["MID(CharList, MONTH(FlagDay), 1)", "'D'"], ["INT(Count / LENGTH(CharList))", "4"], ["(Count &gt;= 29) AND (DAY(FlagDay) &gt; 23)", "FALSE"]]) + "</p>", "Starting MID at 0, or giving 5 as the answer to the second row (rounding instead of INT).") + peq(SRC("w23", "22", "Q1"), "4 + 4 + 3 marks", "Complete / Describe",
  "A shop program stores for each order: the customer name (\"Mr Khan\"), the number of items (3), whether the customer is new (TRUE), and the deposit paid (15.75). (a) Complete the identifier table with meaningful variable names and data types. (b) Total = 124.00, DepRate = 2.00, Description = \"AB12345:Cleaning Brush (small)\". Evaluate (Total * DepRate) + 1.5; RIGHT(Description, 7); (LENGTH(Description) - 8) > 16; NUM_TO_STR(INT(DepRate * 10)) & '%'. (c) The data for each order is not all of the same type. Describe an effective way of storing it for many orders while the program is running.", "Types from the examples. Work inside out. Record type, then array of records.",
  "<p><b>(a)</b> " + tbl(["Example value", "Variable name", "Data type"], [["\"Mr Khan\"", "CustomerName", "STRING"], ["3", "NumItems", "INTEGER"], ["TRUE", "NewCustomer", "BOOLEAN"], ["15.75", "Deposit", "REAL"]]) + "</p><p><b>(b)</b> One mark per row:" + tbl(["Expression", "Evaluates to"], [["(Total * DepRate) + 1.5", "249.50"], ["RIGHT(Description, 7)", "\"(small)\""], ["(LENGTH(Description) - 8) &gt; 16", "TRUE"], ["NUM_TO_STR(INT(DepRate * 10)) &amp; '%'", "\"20%\""]]) + "</p><p><b>(c)</b> Any three: " + mks(["Declare a composite (record) type", "Declare an array of that record type", "The record contains all the data items required (items of different data types)", "Each array element represents the data for one order (customer)"], "b") + "</p>", None) + peq(SRC("w24", "23", "Q1(b)(c)"), "3 + 3 marks", "Complete",
  "(b) Give the data type of Available (TRUE), Received (\"18/04/2021\") and Index (100). (c) Using these values, evaluate each expression, writing ERROR if it contains an error: Available AND NOT(Index > 100); Index MOD 30; NUM_TO_STR(Index + \"33\").", "BOOLEAN, STRING (it is in quotes), INTEGER. Then check each operator.",
  "<p><b>(b)</b> " + tbl(["Variable", "Example data value", "Data type"], [["Available", "TRUE", "BOOLEAN"], ["Received", "\"18/04/2021\"", "STRING"], ["Index", "100", "INTEGER"]]) + "</p><p><b>(c)</b> " + tbl(["Expression", "Evaluates to"], [["Available AND NOT(Index &gt; 100)", "TRUE"], ["Index MOD 30", "10"], ["NUM_TO_STR(Index + \"33\")", "ERROR"]]) + "</p>", "Writing a type for Received as DATE: the value is in quotes, so it is a STRING.") + peq(SRC("w25", "22", "Q1(b)(c)"), "3 + 4 marks", "Complete",
  "(b) Give the data type of Result (5.42), MonthLetter (\"JFMAMJJASOND\") and Birthday (15/11/2009). (c) Evaluate, or write ERROR: INT(Result) + 1 > 6; NUM_TO_STR(LENGTH(MonthLetter)); NUM_TO_STR(Result + \"3.2\"); MID(MonthLetter, MONTH(Birthday) − 2, 1).", "REAL, STRING, DATE. INT(5.42) = 5. MONTH = 11; 11 − 2 = 9.",
  "<p><b>(b)</b> " + tbl(["Variable", "Example data value", "Data type"], [["Result", "5.42", "REAL"], ["MonthLetter", "\"JFMAMJJASOND\"", "STRING"], ["Birthday", "15/11/2009", "DATE"]]) + "</p><p><b>(c)</b> " + tbl(["Expression", "Evaluates to"], [["INT(Result) + 1 &gt; 6", "FALSE"], ["NUM_TO_STR(LENGTH(MonthLetter))", "\"12\""], ["NUM_TO_STR(Result + \"3.2\")", "ERROR"], ["MID(MonthLetter, MONTH(Birthday) − 2, 1)", "\"S\""]]) + "</p>", None) + peq(SRC("s22", "23", "Q1(b)"), "2 + 1 marks", "Complete / Give",
  "AAA = TRUE, BBB = FALSE, Count = 99. (i) Evaluate AAA AND (Count > 99); AAA AND (NOT BBB); (Count <= 99) AND (AAA OR BBB); (BBB AND Count > 50) OR NOT AAA. (ii) Give an example of when a Boolean variable would be used.", "Evaluate each comparison to TRUE or FALSE first.",
  "<p><b>(i)</b> One mark for any two rows correct, one for all correct:" + tbl(["Expression", "Evaluation"], [["AAA AND (Count &gt; 99)", "FALSE"], ["AAA AND (NOT BBB)", "TRUE"], ["(Count &lt;= 99) AND (AAA OR BBB)", "TRUE"], ["(BBB AND Count &gt; 50) OR NOT AAA", "FALSE"]]) + "</p><p><b>(ii)</b> One from: " + mks(["To terminate a conditional loop when a value has been found", "When a variable can take only one of two possible values", "To record whether an action has been done (for example yes or no)"], "a") + "</p>", None)

review = req("4 marks", "Complete", "A program stores a pupil's name, year group, average mark (with a decimal) and whether they have paid for the trip. Give a variable name and data type for each.", "Meaningful; the right type.", "<p>" + mks(["PupilName: STRING", "YearGroup: INTEGER", "AverageMark: REAL", "TripPaid: BOOLEAN"]) + "</p>", None) + req("4 marks", "Complete", "Word = \"Cambridge\", N = 17. Evaluate LEFT(Word, 4); MID(Word, 5, 3); N MOD 5; N DIV 5.", "Positions start at 1.", "<p>" + mks(["\"Camb\"", "\"rid\"", "2", "3"]) + "</p>", None) + req("3 marks", "State", "State the error in each statement, or NO ERROR: A ← LENGTH(25); B ← \"Total: \" &amp; NUM_TO_STR(25); C ← \"5\" * 3.", "Check the types.", "<p>" + mks(["A: LENGTH needs a string, not a number", "B: NO ERROR", "C: a string cannot be multiplied (use STR_TO_NUM first)"]) + "</p>", None) + req("2 marks", "State", "State two items of information, other than the name, that an identifier table should contain.", "Type and purpose.", "<p>" + mks(["The data type", "The purpose (or an example value, or the scope)"]) + "</p>", None) + req("2 marks", "Explain", "Explain why a constant is better than typing 0.2 each time a VAT rate is used.", "One place to change.", "<p>" + mks(["It has a meaningful name, so the program is easier to read", "If the rate changes it is changed in one place"]) + "</p>", None)

tips = tips_html([
  ("Type from the value.", "Quoted means STRING. A decimal means REAL."),
  ("Meaningful names.", "MemberName, not X."),
  ("Inside out.", "Evaluate the innermost function first and write down each step."),
  ("Check the operand types.", "&amp; strings only; AND/OR BOOLEAN only."),
  ("Format the answer.", "Strings in quotes, 249.50 with its decimals, TRUE not true."),
  ("Position 1.", "MID and LEFT start counting at 1."),
], [("an identifier", "The name of a variable, constant, subroutine or array."), ("a data type", "What kind of value a variable stores."), ("a constant", "A named value that does not change."), ("a function", "A routine that returns a value.")],
  [("Complete", "Fill in the table."), ("Evaluate", "Work out the value."), ("State", "A short answer."), ("Describe", "Say what is wrong or what happens.")]) + FC

js = AKJS + AK20JS + r'''
(function () {
  const draw = (s) => { const k = Math.round(s.i); const L = [["(Total * DepRate) + 1.5", ""], ["(124.00 * 2.00) + 1.5", "replace the variables"], ["248.00 + 1.5", "brackets first"], ["249.50", "add: the answer is a REAL"]]; let o = SV.rect(10, 8, 330, 34, "cell", { rx: 6 }) + SV.text(24, 31, L[k][0], "lbl bd", { style: "font-size:14px;font-family:monospace" }); o += SV.text(24, 64, L[k][1], "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stA"), { w: 350, h: 80, label: "Evaluate", base: { i: 0 }, draw, tween: 100, dwell: 1800, steps: ["The expression.", "Put the values in.", "Evaluate the brackets.", "Finish the calculation."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const str = "JFMAMJJASOND"; const draw = (s) => { const k = Math.round(s.i); let o = ""; for (let i = 0; i < str.length; i++) { const pos = i + 1; const hl = k === 1 ? pos >= 1 && pos <= 3 : k === 2 ? pos >= 10 : k === 3 ? pos === 9 : false; o += SV.rect(14 + i * 28, 30, 26, 26, hl ? "f3" : "cell", { rx: 3 }) + SV.text(27 + i * 28, 48, str[i], "lbl bd", { "text-anchor": "middle" }) + SV.text(27 + i * 28, 22, pos, "sm", { "text-anchor": "middle" }); } o += SV.text(14, 84, ["\"JFMAMJJASOND\" with positions 1 to 12", "LEFT(s, 3) = \"JFM\"", "RIGHT(s, 3) = \"OND\"", "MID(s, 9, 1) = \"S\"  (position 9, one character)"][k], "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stB"), { w: 360, h: 98, label: "Substrings", base: { i: 0 }, draw, tween: 100, dwell: 2000, steps: ["A string with its positions.", "LEFT takes from the start.", "RIGHT takes from the end.", "MID takes from a position."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const L = ["17 divided by 5", "17 / 5 = 3.4 (REAL)", "17 DIV 5 = 3 (whole number of 5s)", "17 MOD 5 = 2 (what is left: 3 × 5 = 15, 17 − 15)"]; let o = ""; for (let i = 0; i < 17; i++) o += SV.rect(10 + i * 18, 20, 15, 15, Math.floor(i / 5) < 3 && k >= 2 ? "f3" : (i >= 15 && k === 3 ? "f2" : "cell"), { rx: 3 }); o += SV.text(10, 62, L[k], "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stC"), { w: 330, h: 80, label: "DIV and MOD", base: { i: 0 }, draw, tween: 100, dwell: 2200, steps: ["Seventeen items, shared in fives.", "/ gives the real result.", "DIV counts the complete groups.", "MOD is the remainder."].map((c, i) => ({ cap: c, s: { i } })) });
})();

(function () {
  const sS = $("#sf_s"), sN = $("#sf_n"), sT = $("#sf_st"); const q = (x) => '"' + x + '"';
  const paint = () => { const s = sS.value, n = Math.max(0, +sN.value || 0), st = Math.max(1, +sT.value || 1); $("#sfV").innerHTML = '<div class="tw"><table class="t mono"><tr><th>Expression</th><th>Result</th></tr>' + [["LENGTH(s)", s.length], [`LEFT(s, ${n})`, q(s.slice(0, n))], [`RIGHT(s, ${n})`, q(n ? s.slice(-n) : "")], [`MID(s, ${st}, ${n})`, q(s.substr(st - 1, n))], ["UCASE(s)", q(s.toUpperCase())], ["LCASE(s)", q(s.toLowerCase())], ["IS_NUM(s)", s.trim() !== "" && !isNaN(+s) ? "TRUE" : "FALSE"]].map((r) => `<tr><td>${r[0]}</td><td>${r[1]}</td></tr>`).join("") + "</table></div>"; };
  [sS, sN, sT].forEach((e) => e.oninput = paint); paint();
})();
(function () {
  const E = [["(Total * DepRate) + 1.5", "249.50", "124.00 × 2.00 = 248.00, + 1.5"], ["Index MOD 30", "10", "100 = 3 × 30 + 10"], ["INT(Result) + 1 > 6", "FALSE", "INT(5.42) = 5, 5 + 1 = 6, 6 > 6 is FALSE"], ["NUM_TO_STR(LENGTH(MonthLetter))", "\"12\"", "LENGTH = 12, converted to a string"], ["NUM_TO_STR(Result + \"3.2\")", "ERROR", "a real plus a string is invalid"], ["MID(MonthLetter, MONTH(Birthday) - 2, 1)", "\"S\"", "MONTH = 11, 11 − 2 = 9, the 9th letter is S"], ["Available AND NOT(Index > 100)", "TRUE", "NOT(FALSE) = TRUE; TRUE AND TRUE"]];
  const bar = $("#evB"); E.forEach((e, i) => { const b = document.createElement("button"); b.className = "mono"; b.textContent = e[0]; b.onclick = () => { bar.querySelectorAll("button").forEach((x) => x.className = "mono" + (x === b ? " on" : "")); $("#evV").innerHTML = `<div class="verdict mono">${e[0]} = <b>${e[1]}</b></div><p>${e[2]}.</p>`; }; bar.appendChild(b); });
})();
btnTable("erB", "erO", [
  ["Result ← 2 & 4", "Error", "& joins strings; 2 and 4 are numbers"],
  ["SubString ← MID(\"pseudocode\", 4, 1)", "NO ERROR", "valid: gives \"u\""],
  ["IF x = 3 OR 4 THEN", "Error", "4 is not a Boolean: write x = 3 OR x = 4"],
  ["Result ← IS_NUM(-27.3)", "Error", "IS_NUM needs a string"],
  ["Message ← \"Done\" + LENGTH(MyString)", "Error", "cannot add a string and a number"],
  ["Y ← STR_TO_NUM(\"37\") + 5", "NO ERROR", "gives 42"]
], ["Statement", "Verdict", "Why"]);
''' + _prjs

finish("as-11-1-programming-basics", "as111", "Programming Basics",
  "Data types, identifiers and identifier tables, operators, built-in functions, evaluating expressions and spotting errors, with animations, labs and the real Paper 2 questions from 2021 to 2026.",
  "11.1", "11 · Programming", "section 11.1 Programming basics", learn, watch, explore, _pr, real, where, past, review,
  "Part 1 is real 9618 questions on programming basics (Paper 2), 2021 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", tips, js)
