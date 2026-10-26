"""A Level CS syllabus 13.1.1: why user-defined types are needed; non-composite types (enumerated, pointer). Run: python3 tools/artifact-kit/mk_ac1311.py"""
from ak20 import *

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>A <b>user-defined data type</b> is a type the programmer builds because the language does not already have one that fits the data. A <b>non-composite</b> type is defined without referring to another data type's structure: an <b>enumerated</b> type is an ordered list of every value the variable may take, and a <b>pointer</b> type stores the memory address of a variable of a stated type. A <b>composite</b> type (record, set, class) is built from other types and is covered on the next page. Declaring a type lets the compiler reject impossible values, makes code easier to read, and stores the data in the right amount of space. In the exam you write the <code>TYPE</code> statement, say what the type is, and give its characteristics.</p></div>

  <h2>1 · Why user-defined types are needed</h2>
  <ul>
    <li>The language only has a few built-in types (INTEGER, STRING, REAL, BOOLEAN, CHAR, DATE). A programmer may need a type that <b>does not exist</b>, such as "day of the school week".</li>
    <li>A user-defined type <b>matches the data exactly</b>: a variable of type <code>SchoolDay</code> can only hold one of five values, so a typing mistake or an impossible value is rejected.</li>
    <li>It makes the program <b>easier to read</b>: <code>Today ← Wednesday</code> is clearer than <code>Today ← 3</code>.</li>
    <li>It lets several related items be grouped under a <b>single identifier</b> (composite types).</li>
  </ul>
  <p>The mark scheme's answers: to create a new data type from existing ones; to allow types not available in the language to be constructed; to extend the flexibility of the language; to represent a particular group of data under a single identifier; to make the code easier to read.</p>

  <h2>2 · Non-composite and composite</h2>
  <div class="tw"><table class="t">
    <tr><th></th><th>Non-composite</th><th>Composite</th></tr>
    <tr><td>Definition</td><td>Defined <b>without referencing another data type</b>; holds a single value (or an address)</td><td>Defined by <b>referring to other types</b>: it holds more than one value under a single identifier</td></tr>
    <tr><td>Kinds</td><td>Primitive types (INTEGER, BOOLEAN...), and the user-defined <b>enumerated</b> and <b>pointer</b> types</td><td>User-defined <b>record</b>, <b>set</b> and <b>class / object</b></td></tr>
    <tr><td>Example</td><td><code>TYPE Day = (Monday, Tuesday, ...)</code></td><td><code>TYPE Pet ... DECLARE PetName : STRING ... ENDTYPE</code></td></tr>
  </table></div>

  <h2>3 · Enumerated types</h2>
  <p>An <b>enumerated type</b> is a user-defined non-composite type whose possible values are given as a <b>list</b>. Each value is a name, not a string: no quotation marks.</p>
  <div class="code">''' + pc('''TYPE SchoolDay = (Monday, Tuesday, Wednesday, Thursday, Friday)
TYPE WeekEnd = (Saturday, Sunday)

DECLARE Today : SchoolDay
Today ← Wednesday                    // a value from the list, no quotation marks
IF Today < Friday THEN               // ordered, so < and > can be used
   OUTPUT "Not the end of the week yet"
ENDIF''') + '''</div>
  <p><b>Characteristics of the list</b> (all are mark-scheme answers):</p>
  <ul>
    <li>It contains <b>all the possible values</b>, and the list is <b>fixed</b>: values cannot be added after it is defined.</li>
    <li>It is <b>ordered</b> (ordinal): the values have a position, so they can be compared and counted through. Wednesday comes after Tuesday.</li>
    <li>The values are <b>unique</b> (no repeats) and all of the same kind.</li>
    <li>A variable of the type can hold <b>one</b> value from the list.</li>
  </ul>
  <p>Internally each value is stored as a small whole number (its ordinal position, starting at 0), which is why enumerated types take little space and are fast to compare.</p>
  <div class="code">''' + pc('''from enum import Enum

class SchoolDay(Enum):                # Python's equivalent of an enumerated type
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4

Today = SchoolDay.WEDNESDAY
print(Today.value)                    # 2
print(Today.value < SchoolDay.FRIDAY.value)   # True''') + '''</div>

  <h2>4 · Pointer types</h2>
  <p>A <b>pointer type</b> is a user-defined non-composite type that <b>references a memory location</b>. It stores an <b>address</b>, not a value, and the declaration says what <b>type of data</b> is stored at that address. The symbol <code>^</code> in the type declaration means "pointer to".</p>
  <div class="code">''' + pc('''TYPE TIntPointer = ^INTEGER           // a pointer to an INTEGER
TYPE Word = ^STRING                   // a pointer to a STRING

DECLARE Score : INTEGER
DECLARE P : TIntPointer

Score ← 40
P ← ^Score                            // P now holds the address of Score
OUTPUT P^                             // P^ is the value stored at that address: 40
P^ ← P^ + 2                           // changes the value at that address
OUTPUT Score                          // 42: Score has changed too''') + '''</div>
  <div class="tw"><table class="t">
    <tr><th>Notation</th><th>Meaning</th></tr>
    <tr><td><code>^INTEGER</code> in a TYPE</td><td>The type is a pointer to an integer</td></tr>
    <tr><td><code>P ← ^Score</code></td><td>Store the <b>address</b> of Score in the pointer P</td></tr>
    <tr><td><code>P^</code></td><td>The <b>value</b> at the address held in P (following the pointer)</td></tr>
  </table></div>
  <p>Pointers are used to build structures that link items by address, such as linked lists, and to pass big items around without copying them. Python hides addresses: a variable holding a list or object is already a reference to it.</p>

  <h2>5 · Writing the declarations</h2>
  <ol>
    <li>Start with <code>TYPE</code>, then the new name, then <code>=</code>. Use only the equals sign: <code>TYPE Animals = (Alpaca, Chicken, Donkey)</code>.</li>
    <li>For an enumerated type, put the values in brackets, in the order given, separated by commas, with no quotation marks and no extra punctuation.</li>
    <li>For a pointer type, write <code>^</code> and the type of the data: <code>TYPE Word = ^STRING</code>.</li>
    <li>Declare a variable of the type with <code>DECLARE Name : TypeName</code>.</li>
  </ol>

  <h2>6 · Common ways to lose marks</h2>
  <ul>
    <li>Putting quotation marks round enumerated values, or changing the order the question gives them.</li>
    <li>Writing a pointer type without <code>^</code>, or without the type it points to.</li>
    <li>Saying a pointer "points to a value". It stores the <b>address</b> (memory location) of the value.</li>
    <li>Saying an enumerated type "holds a list of values". A variable holds <b>one</b> value; the type defines the list of allowed ones.</li>
    <li>Defining non-composite as "simple". Say it is defined <b>without reference to another data type</b>.</li>
    <li>Leaving out the "ordered" characteristic of an enumerated list.</li>
  </ul>
'''

watch = '''
  <h2>1 · Why a new type? A string lets mistakes through</h2>
  <p>Press Play, or click the steps.</p>
  <div id="stA"></div>
  <h2>2 · An enumerated type is an ordered list</h2>
  <div id="stB"></div>
  <h2>3 · A pointer holds an address</h2>
  <div id="stC"></div>
  <h2>4 · Changing a value through a pointer</h2>
  <div id="stD"></div>
'''

explore = '''
  <h2>Lab 1 · Work with an enumerated type</h2>
  <p>Choose a type, then pick two values. See their positions, which is larger, and what a value outside the list does.</p>
  <div class="card"><div id="eB" class="btnrow"></div><div id="eV1" class="btnrow"></div><div id="eV2" class="btnrow"></div>
    <div class="readout"><div><small>Position of first</small><strong id="e1"></strong></div><div><small>Position of second</small><strong id="e2"></strong></div><div><small>First &lt; second?</small><strong id="e3"></strong></div></div>
    <p><input id="eT" type="text" placeholder="Try assigning a value, e.g. Sunday" style="width:100%;padding:8px;border:1px solid var(--line);border-radius:8px;font:500 .95rem var(--mono)" aria-label="Value to assign"></p>
    <div class="btnrow"><button class="b pri" id="eA">Assign this value</button></div><div class="verdict" id="eV"></div></div>

  <h2>Lab 2 · Follow the pointer</h2>
  <p>Two integer variables sit at addresses. Run the statements and watch the pointer P and the values.</p>
  <div class="card"><div class="btnrow"><button class="b" data-s="0">P ← ^Score</button><button class="b" data-s="1">P ← ^Lives</button><button class="b" data-s="2">P^ ← P^ + 1</button><button class="b" data-s="3">OUTPUT P^</button><button class="b" id="pR">Reset</button></div><div id="pO"></div><div class="verdict" id="pV"></div></div>

  <h2>Lab 3 · Declaration or mistake?</h2>
  <div class="card"><div id="mB" class="btnrow"></div><div id="mO"></div></div>
'''

practise = '''
  <h2>1 · Which kind of type is it?</h2><div id="cl1" class="card"></div>
  <h2>2 · Characteristics: enumerated or pointer?</h2><div id="cl2" class="card"></div>
  <h2>3 · Put the steps for declaring and using an enumerated type in order</h2><div id="o1" class="card"></div>
  <h2>4 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>5 · Positions and counts</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Days, months and menu choices", "A calendar program has a Month type with twelve named values. A menu has a Choice type (Start, Options, Quit). A variable of these types cannot hold an impossible value, so mistakes are caught early.", "enumerated types make code clear and safe.") +
rw("Traffic lights and game states", "A traffic light has exactly three states, Red, Amber and Green, in a fixed order. A game has states such as Menu, Playing and GameOver. The program moves from one value to the next.", "an ordered list of all possible values.") +
rw("Linked lists and trees", "Each item in a linked list stores a pointer to the next item. The pointer holds the memory location of the next node, not the data itself.", "pointers store addresses and make it easy to link structures together.") +
rw("Passing a large item to a subroutine", "Rather than copying a huge record, a program can pass the address of it. The subroutine follows the pointer to read or change the original.", "a pointer references a memory location.") +
rw("Days of the week in a database", "A database stores 0 to 6 for the weekday instead of the words, because it takes less space. The program shows the names to the user.", "enumerated values are stored as ordinal numbers.")
)

where = [
  ("M/J 2021", "31, 32, 33", "2(a), 2(b)", "2 + 1 + 1", "Purpose of a user-defined type; define two enumerated types"),
  ("O/N 2021", "31, 32", "3", "2 + 2", "Write pseudocode for an enumerated type and a pointer type"),
  ("O/N 2022", "31, 33", "3(a), (b), (c)", "1 + 1 + 2", "Define enumerated and pointer types; define Quarter1"),
  ("M/J 2023", "31, 33", "4", "2 + 2", "Declarations for a set of primes and a pointer to a day"),
  ("O/N 2023", "31, 33", "3", "4", "Describe enumerated and pointer data types"),
  ("O/N 2023", "32", "2", "4", "Describe composite and non-composite data types"),
  ("M/J 2024", "31, 33", "3(a)", "3", "Explain non-composite and composite data types"),
  ("M/J 2024", "32", "3(a)", "3", "Explain a non-composite type and give an example"),
  ("O/N 2025", "33", "1(a)", "2 + 2", "Declare an enumerated type; give two characteristics of its list"),
  ("M/J 2026", "31", "1(a), 1(b)", "2 + 1 + 2", "Name two composite types; purpose of a pointer; declare a pointer type"),
  ("M/J 2026", "32", "1", "2 + 1 + 2", "Declare an enumerated type; name it; two features of its list"),
  ("M/J 2026", "33", "1", "3 + 2", "Why user-defined types are needed; declare Fibonacci")]

past = '''  <p class="note">Enumerated and pointer types, and the idea of a user-defined type, appear in Paper 3 in every series from May/June 2021 to May/June 2026. Declarations of composite types (record, set) are on the next page. Questions are reworded from the papers; check the original paper and mark scheme for the exact wording.</p>

  <h3>Why user-defined types, and what non-composite means</h3>
''' + peq(SRC("s21", "31, 32, 33", "Q2(a), (b)"), "2 + 1 + 1 marks", "Describe / Define",
  "(a) Describe the purpose of a user-defined data type. (b) Define, using pseudocode, the following enumerated data types: (i) SchoolDay, to hold data about the days students are usually in school; (ii) WeekEnd, to hold data about the days that are not school days.",
  "(a) Create a new type that the language does not have. (b) Use TYPE, equals, and the values in brackets without quotation marks.",
  "<p><b>(a)</b> " + mks(["To create a new data type (from existing data types)", "to allow data types not available in the language to be constructed / to extend the flexibility of the language"]) + "</p><p><b>(b)</b> " + mks(["TYPE SchoolDay = (Monday, Tuesday, Wednesday, Thursday, Friday)"], "a") + " " + mks(["TYPE WeekEnd = (Saturday, Sunday)"], "a") + "</p>",
  "Defining the type with a STRING variable and a comment. The question asks for an enumerated <code>TYPE</code> statement.") + peq(SRC("w23", "32", "Q2"), "4 marks", "Describe",
  "Describe what is meant by composite and non-composite data types.",
  "Two marks for each: what is held, and whether other types are referred to.",
  "<p>Composite: " + mks(["a (user-defined) data type that is a collection of data that can consist of multiple elements", "of different or the same data types, grouped under a single identifier"]) + " Non-composite: " + mks(["can be defined without referencing another data type", "can be a primitive type available in a language, or a user-defined type"], "a") + "</p>",
  "Writing that composite types are 'complicated'. Say they hold several values, grouped under one name.") + peq(SRC("s24", "31, 33", "Q3(a)"), "3 marks", "Explain",
  "Explain what is meant by non-composite and composite data types.",
  "Two points each, three marks in total: single-reference against several-reference, and the kinds of each.",
  "<p>Non-composite: " + mks(["can be user-defined or primitive", "does not refer to other data types in its definition", "(kinds: primitive, enumerated, pointer)"]) + " Composite: " + mks(["refers to other data types in its definition / contains more than one data type", "(kinds: record, set, class)"], "a") + " (maximum 3)</p>", None) + peq(SRC("s24", "32", "Q3(a)"), "3 marks", "Explain / Give",
  "Explain what is meant by the term non-composite data type and give an example of a non-composite data type.",
  "A definition that does not need another type, and the type of one example.",
  "<p>" + mks(["A data type defined without referencing another data type", "it can be a primitive data type in a programming language or a user-defined data type", "example: an enumerated type or a pointer type (or a correct declaration of one)"]) + "</p>", None) + peq(SRC("s26", "33", "Q1"), "3 + 2 marks", "Explain / Write",
  "User-defined data types may be created by programmers when writing software. (a) Explain the reasons why user-defined data types are needed. (b) Write the pseudocode statement to declare a non-composite data type, Fibonacci, that holds the following numbers: 0, 1, 2, 3, 5, 8, 13, 21.",
  "(a) Three reasons. (b) An enumerated type: the numbers in the order given, in brackets, with no quotation marks.",
  "<p><b>(a)</b> Up to three: " + mks(["The programmer may need a data type that does not exist within the programming language", "to represent a particular set / group of data under a single identifier", "or to extend existing data types so that the code is easier to understand, or so it exactly matches the program's requirements"]) + "</p><p><b>(b)</b> " + mks(["TYPE Fibonacci =", "(0, 1, 2, 3, 5, 8, 13, 21)"], "a") + "</p>" + pc('''TYPE Fibonacci = (0, 1, 2, 3, 5, 8, 13, 21)'''),
  "Putting the numbers in quotation marks, or listing them in a different order.") + '''
  <h3>Enumerated types</h3>
''' + peq(SRC("w21", "31, 32", "Q3(a)"), "2 marks", "Write",
  "Enumerated and pointer are two non-composite data types. (a) Write pseudocode to create an enumerated type called Parts to include these parts sold in a computer shop: Monitor, CPU, SSD, HDD, LaserPrinter, Keyboard, Mouse.",
  "Two marks: TYPE Parts = and the bracketed list.",
  "<p>" + mks(["TYPE Parts =", "(Monitor, CPU, SSD, HDD, LaserPrinter, Keyboard, Mouse)"]) + "</p>" + pc('''TYPE Parts = (Monitor, CPU, SSD, HDD, LaserPrinter, Keyboard, Mouse)'''), None) + peq(SRC("w22", "31, 33", "Q3(a), (c)"), "1 + 2 marks", "State / Write",
  "(a) State what is meant by the term enumerated data type. (c) The months are January, February, March, April, May, June, July, August, September, October, November and December. Write the pseudocode statement to define the data type Quarter1, to hold the names of the first three months of a year.",
  "(a) a user-defined non-composite type with an ordered list of values. (c) only the three months.",
  "<p><b>(a)</b> " + mks(["A (user-defined non-composite) data type with an ordered list of possible values"]) + "</p><p><b>(c)</b> " + mks(["TYPE Quarter1 =", "(January, February, March)"], "a") + "</p>" + pc('''TYPE Quarter1 = (January, February, March)'''),
  "Defining Quarter1 with all twelve months. The type holds only the first three.") + peq(SRC("w25", "33", "Q1(a)"), "2 + 2 marks", "Write / Identify",
  "An enumerated data type, Spectrum, is required to hold the names of colours. (i) Write the pseudocode statement for the type declaration of Spectrum to hold: Red, Orange, Yellow, Green, Blue, Indigo, Violet. (ii) Identify two characteristics of the list of values given in an enumerated data type declaration.",
  "(ii) think ordered, complete, unique, same type.",
  "<p><b>(i)</b> " + mks(["TYPE Spectrum =", "(Red, Orange, Yellow, Green, Blue, Indigo, Violet)"]) + "</p>" + pc('''TYPE Spectrum = (Red, Orange, Yellow, Green, Blue, Indigo, Violet)''') + "<p><b>(ii)</b> Any two: " + mks(["the list is ordered / ordinal", "the list contains all possible values", "there are no duplicate values", "all values are the same data type"], "a") + "</p>", None) + peq(SRC("s26", "32", "Q1"), "2 + 1 + 2 marks", "Write / State / Give",
  "A user-defined data type is required to store the types of animals in a children's zoo. (a) Write the pseudocode statement to declare a non-composite data type, Animals, that holds: Alpaca, Chicken, Donkey, Duck, Goat, Pony, Sheep. (b)(i) State the type of user-defined non-composite data type created in (a). (ii) Give two features that would apply to any list used in the data type in (a).",
  "Keep the order given. The type is a named list of values.",
  "<p><b>(a)</b> " + mks(["TYPE Animals =", "(Alpaca, Chicken, Donkey, Duck, Goat, Pony, Sheep)"]) + "</p>" + pc('''TYPE Animals = (Alpaca, Chicken, Donkey, Duck, Goat, Pony, Sheep)''') + "<p><b>(b)(i)</b> " + mks(["Enumerated"], "a") + " <b>(ii)</b> Any two: " + mks(["the list is complete / fixed length: values cannot be changed after it is declared", "the list is ordered", "the elements are unique"], "a") + "</p>",
  "Adding extra punctuation or writing the names on more than one line without keeping the order.") + '''
  <h3>Pointer types</h3>
''' + peq(SRC("w21", "31, 32", "Q3(b)"), "2 marks", "Write",
  "Write pseudocode to create a pointer type called SelectParts that will reference the memory location in which the current part name is stored. (The type Parts is the enumerated type from part (a).)",
  "TYPE name = ^ and the type of data at that address.",
  "<p>" + mks(["TYPE SelectParts = ^", "the correct data type, Parts"]) + "</p>" + pc('''TYPE SelectParts = ^Parts'''),
  "Writing <code>SelectParts = Parts</code>. Without <code>^</code> it is not a pointer type.") + peq(SRC("w22", "31, 33", "Q3(b)"), "1 mark", "State",
  "State what is meant by the term pointer data type.",
  "A user-defined non-composite type, and what it holds.",
  "<p>" + mks(["A user-defined non-composite data type used to reference a memory location"]) + "</p>", None) + peq(SRC("w23", "31, 33", "Q3"), "4 marks", "Describe",
  "Describe what is meant by enumerated and pointer data types.",
  "Two marks each: for enumerated, the list and its order; for pointer, addresses and the type of data stored.",
  "<p>Enumerated: " + mks(["a user-defined non-composite data type", "with a list of all possible values", "that is ordered"]) + " Pointer: " + mks(["a user-defined non-composite data type", "that stores addresses / memory locations only", "and indicates the type of data stored in the memory location"], "a") + " (maximum 2 each)</p>", None) + peq(SRC("s23", "31, 33", "Q4"), "2 + 2 marks", "Write",
  "Two descriptions of user-defined data types are given. Give appropriate type declaration statements for each, including appropriate names. (a) A data type to hold a set of prime numbers below 20: 2, 3, 5, 7, 11, 13, 17, 19. (b) A data type to point to a day in the week, for example Monday.",
  "(a) the mark scheme accepts a bracketed list. (b) a pointer to STRING, or to a day type.",
  "<p><b>(a)</b> " + mks(["TYPE Prime =", "(2, 3, 5, 7, 11, 13, 17, 19)"]) + " <b>(b)</b> " + mks(["TYPE TDayPointer =", "^STRING (or ^DayOfWeek)"], "a") + "</p>" + pc('''TYPE Prime = (2, 3, 5, 7, 11, 13, 17, 19)
TYPE TDayPointer = ^STRING'''),
  "Leaving out the <code>^</code> in (b), so it declares a plain type.") + peq(SRC("s26", "31", "Q1"), "2 + 1 + 2 marks", "Identify / State / Write",
  "(a) A record data type is a type of composite user-defined data type. Identify two other types of composite user-defined data types. (b)(i) A pointer data type is a non-composite user-defined data type. State the purpose of a pointer user-defined data type. (ii) Write the pseudocode statement to declare a pointer data type called Word to be used with STRING data.",
  "(a) not record. (b)(i) refer to a memory location.",
  "<p><b>(a)</b> " + mks(["set", "class / object"]) + " <b>(b)(i)</b> " + mks(["To reference a memory location"], "a") + " <b>(ii)</b> " + mks(["TYPE Word", "= ^STRING"], "a") + "</p>" + pc('''TYPE Word = ^STRING'''),
  "Writing 'to point to a pointer' for the purpose. The purpose is to reference (hold the address of) a memory location.")

review = req("2 marks", "State", "State two reasons why a programmer might define an enumerated type for the days of the week rather than use the strings \"Monday\", \"Tuesday\" and so on.", "Think about what the compiler can check and how easy the code is to read.",
  "<p>" + mks(["Only the seven listed values are allowed, so a mistyped or impossible value is rejected.", "The values are ordered, so they can be compared, and the code is easier to read than numbers."]) + "</p>", None) + req("2 marks", "Write", "Write the pseudocode to declare an enumerated type Level to hold Beginner, Intermediate and Advanced, and a variable Skill of that type.", "A TYPE statement and a DECLARE statement.",
  "<p>" + mks(["TYPE Level = (Beginner, Intermediate, Advanced)", "DECLARE Skill : Level"]) + "</p>" + pc('''TYPE Level = (Beginner, Intermediate, Advanced)
DECLARE Skill : Level'''), "Quoting the values: <code>(\"Beginner\", ...)</code>.") + req("3 marks", "Write", "Write pseudocode to declare a pointer type TRealPointer for REAL values, a variable Ptr of that type, and statements to make Ptr point to the variable Price (a REAL) and then output the value of Price using Ptr.", "TYPE, DECLARE, address-of, then follow the pointer.",
  "<p>" + mks(["TYPE TRealPointer = ^REAL and DECLARE Ptr : TRealPointer", "Ptr ← ^Price", "OUTPUT Ptr^"]) + "</p>" + pc('''TYPE TRealPointer = ^REAL
DECLARE Ptr : TRealPointer
Ptr ← ^Price
OUTPUT Ptr^'''), "Writing <code>OUTPUT Ptr</code>, which outputs the address, not the value.") + req("2 marks", "Describe", "Score holds 8, and P points to Score. State the value of Score after <code>P^ ← P^ * 2</code> and explain why.", "Follow the pointer to the variable.",
  "<p>" + mks(["Score is 16", "P^ is the value stored at the address in P, which is the address of Score, so changing P^ changes Score"]) + "</p>", None) + req("2 marks", "Distinguish", "Distinguish between an enumerated type and a pointer type.", "What does each store?",
  "<p>" + mks(["An enumerated type has an ordered list of all the possible values, and a variable holds one of them.", "A pointer type stores the address (memory location) of a variable of a stated data type."]) + "</p>", None)

exam = exam20("Part 1 is real 9618 questions on user-defined types and the non-composite types, enumerated and pointer (Paper 3), 2021 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", where, past, review)

tips = tips_html([
  ("Copy the values exactly.", "Keep the order the question gives, with no quotation marks and no extra punctuation."),
  ("Use the type words.", "Enumerated: an ordered list of all possible values. Pointer: stores an address and says what type of data is there."),
  ("Say 'without referencing another type'.", "That is the mark for non-composite."),
  ("Give the reason for a type.", "A type the language does not have, tailored to the data, clearer code, fewer errors."),
  ("^ means pointer.", "TYPE Word = ^STRING. P^ is the value at the address."),
  ("Check what the type should hold.", "Quarter1 holds three months, not twelve."),
], [
  ("what an enumerated type is", "A user-defined non-composite data type with an ordered list of possible values."),
  ("what a pointer type is", "A user-defined non-composite data type that stores a memory address and the type of data held there."),
  ("what non-composite means", "The type is defined without referencing another data type."),
  ("why use a user-defined type", "To create a type that does not exist in the language and so match the data exactly."),
], [("State", "A short definition or the declaration, no explanation."), ("Describe", "Say what it is and what it holds, in two or three points."), ("Explain", "Give reasons."), ("Write the pseudocode", "A TYPE statement in the exact form, with the values in the order given.")]) + FC

js = AKJS + AK20JS + r'''
(function () {
  const draw = (s) => {
    const k = Math.round(s.i); let o = "";
    o += SV.rect(20, 20, 330, 190, "f1", { rx: 10, ...op(0.18) }) + SV.text(185, 44, "DECLARE Day : STRING", "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:15px" });
    o += SV.rect(410, 20, 330, 190, "f2", { rx: 10, ...op(0.18) }) + SV.text(575, 44, "DECLARE Day : SchoolDay", "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:15px" });
    if (k >= 1) o += SV.text(40, 80, "Day ← \"Wensday\"", "lbl", { style: "font-family:var(--mono);font-size:15px" }) + SV.text(430, 80, "Day ← Wensday", "lbl", { style: "font-family:var(--mono);font-size:15px" });
    if (k >= 2) o += SV.rect(40, 100, 290, 36, "cell-ok", { rx: 6 }) + SV.text(52, 124, "accepted: any text is allowed", "lbl bd t3") + SV.rect(430, 100, 290, 36, "cell-no", { rx: 6 }) + SV.text(442, 124, "rejected: not in the list", "lbl bd t2");
    if (k >= 3) o += SV.text(40, 170, "A misspelling spreads through the program", "sm") + SV.text(430, 170, "Only Monday ... Friday can be stored", "sm");
    return o;
  };
  Lib.stepper($("#stA"), { w: 760, h: 225, label: "STRING against an enumerated type", base: { i: 0 }, draw, tween: 300, dwell: 3200, steps: [
    { cap: "A program stores the day a lesson is on. With a <b>STRING</b>, any text is allowed. With a user-defined type <code>SchoolDay</code> only five values are.", s: { i: 0 } },
    { cap: "The programmer mistypes the day as <b>Wensday</b>.", s: { i: 1 } },
    { cap: "The STRING variable accepts it. The enumerated type <b>rejects</b> it, because Wensday is not one of the listed values.", s: { i: 2 } },
    { cap: "A user-defined type matches the data exactly, so mistakes are caught when the program is compiled or run, not later.", s: { i: 3 } }] });
})();

(function () {
  const names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"];
  const draw = (s) => {
    const k = Math.round(s.i); let o = SV.text(30, 28, "TYPE SchoolDay = (Monday, Tuesday, Wednesday, Thursday, Friday)", "lbl bd", { style: "font-family:var(--mono);font-size:14px" });
    names.forEach((n, i) => { const x = 30 + i * 144; o += SV.rect(x, 50, 130, 50, k >= 1 ? "f3" : "cell", { rx: 8, ...op(k >= 1 || i < 5 ? 1 : 0) }) + SV.text(x + 65, 80, n, "lbl bd", { "text-anchor": "middle", style: "font-size:15px" }); if (k >= 1) o += SV.text(x + 65, 122, "position " + i, "sm", { "text-anchor": "middle" }); });
    if (k >= 2) o += SV.text(30, 160, "Wednesday < Friday   is TRUE   (2 < 4)", "lbl bd t3", { style: "font-family:var(--mono);font-size:15px" });
    if (k >= 3) o += SV.text(30, 190, "Saturday is not in the list: it cannot be stored in a SchoolDay", "lbl bd t2");
    return o;
  };
  Lib.stepper($("#stB"), { w: 760, h: 210, label: "An enumerated type as an ordered list", base: { i: 0 }, draw, tween: 300, dwell: 3200, steps: [
    { cap: "The declaration lists every possible value. The names are not strings, so there are no quotation marks.", s: { i: 0 } },
    { cap: "The list is <b>ordered</b>: each value has a position, starting at 0. This is how the values are stored.", s: { i: 1 } },
    { cap: "Because the list is ordered the values can be <b>compared</b>: Wednesday comes before Friday.", s: { i: 2 } },
    { cap: "The list is <b>complete and fixed</b>. A value that is not in it cannot be stored.", s: { i: 3 } }] });
})();

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); let o = SV.text(40, 24, "memory", "sm");
    o += memCell(40, 36, "addr 5000", 40, "f3", 1, 240, 44) + SV.text(330, 64, "Score  (INTEGER)", "lbl", { style: "font-size:14px" });
    o += memCell(40, 96, "addr 5004", 7, "f3", 1, 240, 44) + SV.text(330, 124, "Lives  (INTEGER)", "lbl", { style: "font-size:14px" });
    o += memCell(40, 170, "P", k === 0 ? "?" : k === 1 ? "5000" : "5004", k === 0 ? "cell" : "f2", 1, 240, 44) + SV.text(330, 198, "P : TIntPointer", "lbl", { style: "font-size:14px" });
    if (k === 1) o += SV.path("M 285 190 C 345 190 345 70 285 60", "c1", { fill: "none", "stroke-width": 2.5 }) + SV.arrowHead(285, 60, "l", "dot1");
    if (k === 2) o += SV.path("M 285 190 C 345 190 345 130 285 120", "c1", { fill: "none", "stroke-width": 2.5 }) + SV.arrowHead(285, 120, "l", "dot1");
    if (k >= 1) o += SV.text(430, 70, k === 1 ? "P ← ^Score  stores the ADDRESS 5000" : "P ← ^Lives  stores the ADDRESS 5004", "lbl bd", { style: "font-family:var(--mono);font-size:14px" }) + SV.text(430, 100, "P^ is the value at that address: " + (k === 1 ? 40 : 7), "lbl", { style: "font-family:var(--mono);font-size:14px" });
    return o;
  };
  Lib.stepper($("#stC"), { w: 760, h: 240, label: "A pointer holds an address", base: { i: 0 }, draw, tween: 300, dwell: 3400, steps: [
    { cap: "Two variables are stored at addresses in memory. The pointer variable <b>P</b> has not been given an address yet.", s: { i: 0 } },
    { cap: "<code>P ← ^Score</code> stores the <b>address</b> of Score (5000) in P. P does not hold 40; it refers to where 40 is stored.", s: { i: 1 } },
    { cap: "Pointing P at Lives instead: <code>P ← ^Lives</code> changes the address in P to 5004. <code>P^</code> is now 7.", s: { i: 2 } }] });
})();

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); const score = k >= 3 ? 42 : 40; let o = "";
    o += memCell(40, 36, "Score", score, k >= 3 ? "cell-warn" : "f3", 1, 240, 44) + memCell(40, 120, "P", "→ Score", "f2", 1, 240, 44);
    o += SV.path("M 280 142 C 340 142 340 58 285 58", "c1", { fill: "none", "stroke-width": 2.5 }) + SV.arrowHead(285, 58, "l", "dot1");
    o += SV.text(380, 70, "Score ← 40;  P ← ^Score", "lbl", { style: "font-family:var(--mono);font-size:14px" });
    if (k >= 1) o += SV.text(380, 104, "OUTPUT P^   →  40", "lbl bd", { style: "font-family:var(--mono);font-size:14px" });
    if (k >= 2) o += SV.text(380, 138, "P^ ← P^ + 2", "lbl bd", { style: "font-family:var(--mono);font-size:14px" });
    if (k >= 3) o += SV.text(380, 172, "OUTPUT Score   →  42", "lbl bd t3", { style: "font-family:var(--mono);font-size:14px" });
    return o;
  };
  Lib.stepper($("#stD"), { w: 760, h: 200, label: "Changing a value through a pointer", base: { i: 0 }, draw, tween: 300, dwell: 3000, steps: [
    { cap: "P holds the address of Score, which holds 40.", s: { i: 0 } },
    { cap: "<code>OUTPUT P^</code> follows the pointer and outputs the value at that address: 40.", s: { i: 1 } },
    { cap: "<code>P^ ← P^ + 2</code> follows the pointer and changes the value stored at that address.", s: { i: 2 } },
    { cap: "Score itself has changed, because P^ <i>is</i> Score's memory location. Output: 42.", s: { i: 3 } }] });
})();

/* Lab 1 */
(function () {
  const types = { SchoolDay: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], Spectrum: ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"], Level: ["Beginner", "Intermediate", "Advanced"], Animals: ["Alpaca", "Chicken", "Donkey", "Duck", "Goat", "Pony", "Sheep"] };
  let t = "SchoolDay", a = 0, b = 2;
  const paint = () => {
    const L = types[t]; if (a >= L.length) a = 0; if (b >= L.length) b = L.length - 1;
    $$("#eB button").forEach((x) => x.classList.toggle("pri", x.textContent === t));
    $("#eV1").innerHTML = '<span style="align-self:center;margin-right:6px">First:</span>' + L.map((v, i) => `<button class="b${i === a ? " pri" : ""}" data-i="${i}">${v}</button>`).join("");
    $("#eV2").innerHTML = '<span style="align-self:center;margin-right:6px">Second:</span>' + L.map((v, i) => `<button class="b${i === b ? " pri" : ""}" data-i="${i}">${v}</button>`).join("");
    $$("#eV1 button").forEach((x) => (x.onclick = () => { a = +x.dataset.i; paint(); })); $$("#eV2 button").forEach((x) => (x.onclick = () => { b = +x.dataset.i; paint(); }));
    $("#e1").textContent = a; $("#e2").textContent = b; $("#e3").textContent = a < b ? "TRUE" : "FALSE";
    $("#eV").innerHTML = `<code>TYPE ${t} = (${L.join(", ")})</code>`;
  };
  $("#eB").innerHTML = Object.keys(types).map((k) => `<button class="b">${k}</button>`).join("");
  $$("#eB button").forEach((x) => (x.onclick = () => { t = x.textContent; paint(); }));
  $("#eA").onclick = () => { const v = $("#eT").value.trim(), L = types[t]; $("#eV").innerHTML = L.includes(v) ? `<b>${v}</b> is in the list, so it is stored (position ${L.indexOf(v)}).` : `<b>${v || "(nothing)"}</b> is not in the list for ${t}, so it is rejected. A variable of this type can only hold: ${L.join(", ")}.`; };
  paint();
})();

/* Lab 2 */
(function () {
  let st;
  const reset = () => { st = { score: 40, lives: 7, p: null, out: "" }; paint("Choose a statement to run."); };
  const paint = (msg) => {
    $("#pO").innerHTML = '<div class="tw"><table class="t mono"><tr><th>Score (5000)</th><th>Lives (5004)</th><th>P holds</th><th>P^ is</th><th>Output</th></tr><tr><td>' + st.score + "</td><td>" + st.lives + "</td><td>" + (st.p === null ? "?" : st.p) + "</td><td>" + (st.p === 5000 ? st.score : st.p === 5004 ? st.lives : "?") + "</td><td>" + st.out + "</td></tr></table></div>";
    $("#pV").textContent = msg;
  };
  $$("[data-s]").forEach((b) => (b.onclick = () => {
    const s = +b.dataset.s;
    if (s === 0) { st.p = 5000; paint("P ← ^Score stores the address 5000."); }
    else if (s === 1) { st.p = 5004; paint("P ← ^Lives stores the address 5004."); }
    else if (st.p === null) paint("P does not point anywhere yet: assign an address first.");
    else if (s === 2) { if (st.p === 5000) st.score++; else st.lives++; paint("P^ ← P^ + 1 changed the variable at address " + st.p + "."); }
    else { st.out = st.p === 5000 ? st.score : st.lives; paint("OUTPUT P^ follows the pointer and outputs " + st.out + "."); }
  }));
  $("#pR").onclick = reset; reset();
})();

(function () {
  const rows = [
    ["TYPE Day = (\"Mon\", \"Tue\", \"Wed\")", "Quotation marks make the values strings, not enumerated names", "TYPE Day = (Mon, Tue, Wed)"],
    ["TYPE Word = STRING", "This only renames STRING; it is not a pointer. A pointer needs ^", "TYPE Word = ^STRING"],
    ["TYPE Quarter1 = (January, February, March, April)", "Holds a fourth month the question did not include", "TYPE Quarter1 = (January, February, March)"],
    ["TYPE Fibonacci = (0, 1, 2, 3, 5, 8, 13, 21), 34", "Extra punctuation and a value that was not given", "TYPE Fibonacci = (0, 1, 2, 3, 5, 8, 13, 21)"],
    ["P ← Score  (P is a pointer)", "Stores the value of Score, not its address", "P ← ^Score"],
    ["OUTPUT P  (to show Score)", "Outputs the address held in P, not the value", "OUTPUT P^"]
  ];
  const paint = (i) => { $$("#mB button").forEach((b, k) => b.classList.toggle("pri", k === i)); const r = rows[i]; $("#mO").innerHTML = '<div class="tw"><table class="t"><tr><th>Mistake</th><th>What is wrong</th><th>Correct</th></tr><tr><td><code>' + r[0].replace(/&/g, "&amp;").replace(/</g, "&lt;") + "</code></td><td>" + r[1] + "</td><td><code>" + r[2] + "</code></td></tr></table></div>"; };
  $("#mB").innerHTML = rows.map((r, i) => `<button class="b" data-i="${i}">Mistake ${i + 1}</button>`).join("");
  $$("#mB button").forEach((b) => (b.onclick = () => paint(+b.dataset.i))); paint(0);
})();
''' + CLASSIFY("cl1", "What kind of type is each declaration?", ["Enumerated", "Pointer", "Composite (record)"],
  [("TYPE Colour = (Red, Green, Blue)", 0), ("TYPE TNamePtr = ^STRING", 1), ("TYPE Pet ... DECLARE PetName : STRING ... ENDTYPE", 2), ("TYPE Level = (Low, Medium, High)", 0), ("TYPE TAgePtr = ^INTEGER", 1), ("TYPE Book ... DECLARE Title : STRING ... DECLARE Pages : INTEGER ... ENDTYPE", 2)],
  "Brackets with a list of names: enumerated. ^ in the type: pointer. TYPE ... ENDTYPE with DECLARE lines: record.") + CLASSIFY("cl2", "Which statement describes an enumerated type, and which a pointer type?", ["Enumerated", "Pointer"],
  [("An ordered list of all possible values", 0), ("Stores a memory address", 1), ("The values are unique and cannot be added to", 0), ("Says what type of data is stored at the address", 1), ("A variable holds one value from the list", 0), ("P^ is the value at the address", 1)],
  "Enumerated: a fixed ordered list. Pointer: an address plus the type it points to.") + ORDER(
  "Put the steps for using an enumerated type in order.",
  ["Write TYPE and a name for the new type", "Give the list of values in brackets, in order, with no quotation marks", "DECLARE a variable of the new type", "Assign one of the listed values to the variable", "Compare it with other values using the order of the list"],
  "Type, list, variable, assign, compare.") + MATCH([
  ["Non-composite type", "Defined without referencing another data type"], ["Enumerated type", "An ordered list of all the possible values"], ["Pointer type", "Stores the memory address of data of a stated type"], ["^", "Marks a pointer type in a declaration"], ["User-defined type", "A type created by the programmer"]]) + CALC([
  {"q": "TYPE Day = (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday). Counting from 0, what is the position of Thursday?", "a": 3, "unit": "", "tol": 0.01, "hint": "Monday is 0.", "sol": "<b>3</b>."},
  {"q": "TYPE Spectrum has 7 values. How many different values can a variable of this type hold at one time?", "a": 1, "unit": "", "tol": 0.01, "hint": "A variable holds one value.", "sol": "<b>1</b>."},
  {"q": "How many values are in TYPE Fibonacci = (0, 1, 2, 3, 5, 8, 13, 21)?", "a": 8, "unit": "", "tol": 0.01, "hint": "Count them.", "sol": "<b>8</b>."},
  {"q": "TYPE Level = (Beginner, Intermediate, Advanced). How many bits are enough to store a position (0, 1 or 2)?", "a": 2, "unit": "bits", "tol": 0.01, "hint": "2 bits give 4 values.", "sol": "<b>2</b> bits."},
  {"q": "Score holds 10 and P points to Score. What is Score after P^ ← P^ + 5?", "a": 15, "unit": "", "tol": 0.01, "hint": "P^ is Score.", "sol": "<b>15</b>."},
  {"q": "A set of 12 months is stored as an enumerated type. What is the position of December if January is 0?", "a": 11, "unit": "", "tol": 0.01, "hint": "12th value is position 11.", "sol": "<b>11</b>."}]) + MCQ([
  ("What is an enumerated type?", ["A pointer to a list", "An ordered list of all the possible values", "A record", "A kind of loop"], 1, "It lists every allowed value, in order."),
  ("What does a pointer type store?", ["A value", "A memory address", "A list", "A record"], 1, "An address, plus the type of data there."),
  ("Which is a correct enumerated declaration?", ["TYPE Size = (\"S\", \"M\", \"L\")", "TYPE Size = (S, M, L)", "TYPE Size = ^(S, M, L)", "Size = [S, M, L]"], 1, "Names in brackets, no quotation marks."),
  ("Which is a correct pointer type to STRING?", ["TYPE Word = STRING", "TYPE Word = ^STRING", "TYPE Word = (STRING)", "TYPE Word = STRING^"], 1, "^ comes before the type."),
  ("Which makes a type non-composite?", ["It holds many fields", "It is defined without referencing another type", "It is a record", "It is an array"], 1, "That is the mark scheme's definition."),
  ("Why is a user-defined type used?", ["To make the program slower", "To create a type the language does not have and match the data", "To avoid declaring variables", "To remove loops"], 1, "It tailors the type to the data.")], "qz1") + CARDS([
  ("User-defined type", "A data type created by the programmer."), ("Non-composite", "Defined without referencing another data type."), ("Enumerated", "An ordered list of all possible values. TYPE T = (a, b, c)."), ("Pointer", "Stores a memory address and the type of data there. TYPE P = ^INTEGER."),
  ("P ← ^Score", "P holds the address of Score."), ("P^", "The value at the address in P."), ("Composite", "Record, set, class: built from other types."), ("Why", "A type the language lacks, matching the data, clearer, safer.")])

build("ac1311", "ac-13-1-1-non-composite-types", "User-defined Types: Enumerated and Pointer", EYA("13.1.1"),
  "Why user-defined types are needed, composite against non-composite, enumerated and pointer types and how to declare them; animations, labs and the real 9618 questions from 2021 to 2026.",
  dict(sub=CBK("Chapter 13 · Data representation, section 13.1 User-defined data types"), **tabs(learn, watch, explore, practise, real, exam, tips)), js)
