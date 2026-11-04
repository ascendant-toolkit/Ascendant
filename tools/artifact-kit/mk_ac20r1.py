"""20.1.2 extra resource: constructors. Run: python3 tools/artifact-kit/mk_ac20r1.py"""
from ac20r import *

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>A <b>constructor</b> is the method that runs <b>once, automatically, when an object is created</b>. Its job is to give the new object its starting values. In Python it is called <code>__init__</code>; in the exam pseudocode it is <code>NEW</code>. The values passed in when the object is created arrive as <b>parameters</b>, and the constructor stores them in the object's <b>attributes</b>. A constructor never returns a value and is never called by name afterwards.</p></div>

  <h2>1 · The constructor in code</h2>
  <p>The same class in both forms. Each line inside the constructor assigns one attribute.</p>
  ''' + both('''class Pet:
    # PetName : STRING
    # YearBorn : INTEGER
    def __init__(self, NewName, NewYear):
        self.__PetName = NewName
        self.__YearBorn = NewYear''', '''CLASS Pet
  PRIVATE PetName : STRING
  PRIVATE YearBorn : INTEGER
  PUBLIC PROCEDURE NEW(NewName : STRING, NewYear : INTEGER)
    PetName <- NewName
    YearBorn <- NewYear
  ENDPROCEDURE
ENDCLASS''') + '''

  <h2>2 · Creating an object calls the constructor</h2>
  <div class="code">''' + pc('''MyPet = Pet("Rex", 2021)       # Python
MyPet <- NEW Pet("Rex", 2021)  # pseudocode''') + '''</div>
  <p>You never write <code>MyPet.__init__(...)</code>. Writing the class name with brackets is the call. The arguments in the brackets line up, in order, with the constructor's parameters after <code>self</code>.</p>

  <h2>3 · Parameters and attributes are different things</h2>
  <div class="tw"><table class="t">
    <tr><th></th><th>Parameter</th><th>Attribute</th></tr>
    <tr><td>Where it lives</td><td>In the constructor's brackets</td><td>Inside the object, as <code>self.__Name</code></td></tr>
    <tr><td>How long it lasts</td><td>Only while the constructor runs</td><td>For as long as the object exists</td></tr>
    <tr><td>Named</td><td>Often <code>NewName</code> or <code>pName</code></td><td>The name given in the class description</td></tr>
  </table></div>

  <h2>4 · Not every attribute is a parameter</h2>
  <p>Read the question carefully. Some values are <b>passed in</b>; others are <b>set to a fixed starting value</b> inside the constructor. A vehicle that is created standing still does not need its speed passed in.</p>
  ''' + both('''class Vehicle:
    # VehicleID : STRING
    # MaxSpeed : INTEGER
    # CurrentSpeed : INTEGER
    # HorizontalPosition : INTEGER
    def __init__(self, NewID, NewMax):
        self.__VehicleID = NewID
        self.__MaxSpeed = NewMax
        self.__CurrentSpeed = 0
        self.__HorizontalPosition = 0''', '''CLASS Vehicle
  PRIVATE VehicleID : STRING
  PRIVATE MaxSpeed : INTEGER
  PRIVATE CurrentSpeed : INTEGER
  PRIVATE HorizontalPosition : INTEGER
  PUBLIC PROCEDURE NEW(NewID : STRING, NewMax : INTEGER)
    VehicleID <- NewID
    MaxSpeed <- NewMax
    CurrentSpeed <- 0
    HorizontalPosition <- 0
  ENDPROCEDURE
ENDCLASS''') + '''
  <p>Two parameters, four attributes. Counting the parameters is a common one-mark question.</p>

  <h2>5 · Constructors in child classes</h2>
  <p>A child class has its own constructor. Its first job is to call the <b>parent's constructor</b> so the inherited attributes are set; then it sets its own. This is covered on the Inheritance page.</p>
'''

watch = '''
  <h2>1 · Creating an object</h2><p>Press Play, or click the steps.</p><div id="stA"></div>
  <h2>2 · Parameters and fixed starting values</h2><div id="stB"></div>
'''

L = ['MyPet = Pet("Rex", 2021)', 'def __init__(self, NewName, NewYear):', 'self.__PetName = NewName', 'self.__YearBorn = NewYear']
box = lambda t, a, b, c="f1": cls(420, 20, 300, t, ["__PetName: " + a, "__YearBorn: " + b], c, 24)
stA = stepper("stA", "Creating a Pet object", 760, 215, [
    ("The statement <code>Pet(\"Rex\", 2021)</code> calls the class. Python makes a new, empty object.", [code(20, 20, L, 0, 340, 34)]),
    ("It runs <code>__init__</code> on the new object. Inside the constructor the object is called <b>self</b>.", [code(20, 20, L, 1, 340, 34), box("self (new, empty object)", "?", "?")]),
    ("The arguments become the parameters: <code>NewName = \"Rex\"</code>, <code>NewYear = 2021</code>.", [code(20, 20, L, 1, 340, 34), box("self (new, empty object)", "?", "?"), txt(20, 175, 'NewName = "Rex"   NewYear = 2021', "sm", 1)]),
    ("<code>self.__PetName = NewName</code> creates the first attribute on the object.", [code(20, 20, L, 2, 340, 34), box("self (new, empty object)", '"Rex"', "?")]),
    ("<code>self.__YearBorn = NewYear</code> creates the second. The constructor has finished and the parameters are forgotten.", [code(20, 20, L, 3, 340, 34), box("self (new, empty object)", '"Rex"', "2021")]),
    ("The finished object is stored in <code>MyPet</code>. Calling the class again would make a separate object with its own values.", [code(20, 20, L, 0, 340, 34), box("object stored in MyPet", '"Rex"', "2021", "f3"), txt(420, 165, "MyPet refers to this object", "lbl bd t3")])])

V = ['Vehicle("V1", 120)', 'self.__VehicleID = NewID', 'self.__MaxSpeed = NewMax', 'self.__CurrentSpeed = 0', 'self.__HorizontalPosition = 0']
ob = lambda a, b, c, d, cl="f1": cls(420, 20, 310, "self", ["__VehicleID: " + a, "__MaxSpeed: " + b, "__CurrentSpeed: " + c, "__HorizontalPosition: " + d], cl, 24)
stB = stepper("stB", "Vehicle: two parameters, four attributes", 760, 235, [
    ("Two values are passed in: <code>\"V1\"</code> and <code>120</code>. The constructor has two parameters.", [code(20, 20, V, 0, 330, 34), ob("?", "?", "?", "?")]),
    ("The first parameter is copied into <code>__VehicleID</code>.", [code(20, 20, V, 1, 330, 34), ob('"V1"', "?", "?", "?")]),
    ("The second is copied into <code>__MaxSpeed</code>.", [code(20, 20, V, 2, 330, 34), ob('"V1"', "120", "?", "?")]),
    ("<code>CurrentSpeed</code> is not passed in. The constructor <b>sets it to 0</b>, so a new vehicle is standing still.", [code(20, 20, V, 3, 330, 34), ob('"V1"', "120", "0", "?", "f2")]),
    ("The same for <code>HorizontalPosition</code>. Four attributes now exist, even though only two values were passed in.", [code(20, 20, V, 4, 330, 34), ob('"V1"', "120", "0", "0", "f3")])])

explore = '''
  <h2>Lab 1 · Build a constructor call</h2>
  <p>Pick a class and type the arguments. The call and the parameter-to-attribute mapping update as you type.</p>
  <div class="card"><div id="kB" class="btnrow"></div><div id="kI"></div><div id="kO"></div></div>

  <h2>Lab 2 · Spot the mistake</h2>
  <div class="card"><div id="eB" class="btnrow"></div><div id="eO"></div></div>
'''

lab = r'''
(function () {
  const C = [
    { n: "Pet", p: [["NewName", "PetName", "Rex"], ["NewYear", "YearBorn", "2021"]], d: [] },
    { n: "Card", p: [["NewNumber", "Number", "7"], ["NewColour", "Colour", "Red"]], d: [] },
    { n: "Vehicle", p: [["NewID", "VehicleID", "V1"], ["NewMax", "MaxSpeed", "120"]], d: [["CurrentSpeed", "0"], ["HorizontalPosition", "0"]] }
  ];
  let cur = 0; const val = C.map((c) => c.p.map((p) => p[2]));
  const lit = (v) => (/^-?\d+$/.test(v) ? v : '"' + v + '"');
  const out = () => {
    const c = C[cur], v = val[cur];
    const L = [`Obj = ${c.n}(${v.map(lit).join(", ")})`, "", `def __init__(self, ${c.p.map((p) => p[0]).join(", ")}):`];
    c.p.forEach((p, i) => L.push(`    self.__${p[1]} = ${p[0]}    # ${p[0]} is ${lit(v[i])}`));
    c.d.forEach((d) => L.push(`    self.__${d[0]} = ${d[1]}    # fixed starting value`));
    $("#kO").innerHTML = codeHTML(L) + `<div class="verdict">${c.p.length} arguments passed in, ${c.p.length + c.d.length} attributes in the finished object.</div>`;
  };
  const paint = () => {
    const c = C[cur]; $$("#kB button").forEach((b, i) => b.classList.toggle("pri", i === cur));
    $("#kI").innerHTML = '<div class="btnrow">' + c.p.map((p, i) => `<label>${p[0]} <input data-i="${i}" value="${esc(val[cur][i])}" size="8"></label>`).join(" ") + "</div>";
    $$("#kI input").forEach((x) => (x.oninput = () => { val[cur][+x.dataset.i] = x.value; out(); }));
    out();
  };
  $("#kB").innerHTML = C.map((c, i) => `<button class="b" data-i="${i}">${c.n}</button>`).join("");
  $$("#kB button").forEach((b) => (b.onclick = () => { cur = +b.dataset.i; paint(); }));
  paint();
})();

btnTable("eB", "eO", [
  ["Missing self", "def __init__(NewName): self.__Name = NewName", "TypeError: Python passes the object in as the first argument and there is no parameter to receive it", "def __init__(self, NewName):"],
  ["Attribute without self", "def __init__(self, NewName): __Name = NewName", "A local variable is created and forgotten when the constructor ends. The object has no attribute", "self.__Name = NewName"],
  ["Wrong number of arguments", "Pet(\"Rex\")  # constructor needs two", "TypeError: the constructor is missing NewYear", "Pet(\"Rex\", 2021)"],
  ["Returning a value", "def __init__(self, n): self.__Name = n; return self", "__init__ must not return a value; the object is returned by the class call itself", "Remove the return"],
  ["Parameter used instead of attribute", "def GetName(self): return NewName", "NewName only exists while the constructor runs", "return self.__Name"]
], ["Mistake", "Code", "What goes wrong", "Fix"]);
''' + CLASSIFY("cl1", "Is the value passed in as a parameter, or set to a fixed starting value?", ["Parameter (passed in)", "Fixed starting value"],
    [("A vehicle's VehicleID", 0), ("A vehicle's MaxSpeed", 0), ("A vehicle's CurrentSpeed when it is created", 1), ("A card's Number", 0), ("A counter that always starts at 0", 1), ("A pet's name", 0), ("An empty list of Treatments for a new appointment", 1), ("A patient's ID", 0)],
    "If the question says the value is passed in, it is a parameter. If it says the attribute is initialised, or does not mention it as a parameter, set it inside the constructor.") + ORDER(
    "Put the steps of creating an object in order.",
    ["Write Pet(\"Rex\", 2021)", "A new, empty object is made", "The constructor runs on the new object", "The arguments are copied into the parameters", "The parameters are assigned to attributes", "The finished object is stored in the variable"],
    "Call, make, run, copy to parameters, assign to attributes, store.") + MATCH([
    ["Constructor", "Runs once when an object is created and sets its starting values"], ["__init__", "The name of the constructor in Python"], ["NEW", "The name of the constructor in exam pseudocode"], ["self", "The object being built"], ["Parameter", "A value passed to the constructor, only available while it runs"], ["Attribute", "A value stored in the object for as long as it exists"]]) + CALC([
    {"q": "class Hand has a constructor __init__(self, Card1, Card2, Card3, Card4, Card5). How many arguments are in the call that creates a Hand?", "a": 5, "unit": "", "tol": 0.01, "hint": "One for each parameter after self.", "sol": "<b>5</b>."},
    {"q": "A Vehicle constructor takes NewID and NewMax and sets CurrentSpeed and HorizontalPosition to 0. How many attributes does the object have?", "a": 4, "unit": "", "tol": 0.01, "hint": "Count every attribute, not just the parameters.", "sol": "<b>4</b>: two from parameters, two fixed."},
    {"q": "Same constructor: how many parameters does it have, not counting self?", "a": 2, "unit": "", "tol": 0.01, "hint": "Only the values passed in.", "sol": "<b>2</b>."},
    {"q": "A Parrot's parent constructor sets 4 attributes and the Parrot constructor sets 2 more. How many attributes does a Parrot object have?", "a": 6, "unit": "", "tol": 0.01, "hint": "Inherited plus its own.", "sol": "<b>6</b>."}]) + MCQ([
    ("What triggers the constructor?", ["Calling GetName()", "Creating an object from the class", "Importing the class", "Printing the object"], 1, "Writing the class name with brackets runs it."),
    ("What is the first parameter of every Python method, including __init__?", ["name", "self", "this", "object"], 1, "self refers to the object being worked on."),
    ("A constructor should...", ["Return the object", "Return nothing and set the attributes", "Print the attributes", "Delete the old object"], 1, "It sets starting values; it does not return."),
    ("Which line creates a Pet attribute properly?", ["PetName = NewName", "self.__PetName = NewName", "NewName = self.__PetName", "return NewName"], 1, "The attribute belongs to the object, so it needs self."),
    ("The question says 'the constructor takes the ID as a parameter and sets speed to 0'. How many parameters?", ["0", "1", "2", "3"], 1, "Only the ID is passed in."),
    ("How many constructors does a class normally have?", ["One", "One per attribute", "Two", "None"], 0, "One, called when an object is created.")], "qz1") + CARDS([
    ("Constructor", "Runs once when an object is created. Sets the starting values."), ("__init__(self, ...)", "Python's constructor."), ("NEW", "Pseudocode's constructor name."), ("Argument", "A value you pass in when you create the object."),
    ("Parameter", "The variable in the constructor that receives an argument."), ("Attribute", "A value stored in the object: self.__Name."), ("Fixed starting value", "An attribute set inside the constructor, not passed in."), ("Object", "One instance of a class, made by calling it.")])

real = RWNOTE + (
    rw("A new game character", "When a character appears it needs a name, a position and a health value. The constructor takes the name and start position and sets the health to 100.", "constructor with a mix of parameters and fixed values.") +
    rw("Opening a bank account", "An account is created with the owner's name and starts with a balance of zero. Nothing else in the program can create an account in an invalid state.", "constructor sets a safe starting state.") +
    rw("A blank patient record", "A new record starts with the ID and name supplied and an empty list of treatments. Later setters add the treatments.", "constructor then setters: create, then update.") +
    rw("A shop basket", "A basket is made for a customer and starts empty. Each call to the class gives a separate basket, so two customers never share items.", "each object made by the constructor has its own values."))

review = (
    req("2 marks", "State", "What is the purpose of a constructor?", "Two marks: when it runs, and what it does.", mks(["It is run when an object is created", "to set the starting values of its attributes (initialise the object)"])) +
    req("4 marks", "Write", "Write the class <code>Book</code> with private attributes <code>Title</code> (STRING) and <code>Pages</code> (INTEGER), both passed in to the constructor.", "Class header, attribute comments, constructor header with self, two assignments with self.", pc('''class Book:
    # Title : STRING
    # Pages : INTEGER
    def __init__(self, NewTitle, NewPages):
        self.__Title = NewTitle
        self.__Pages = NewPages'''), "Leaving out <code>self.</code> before the attribute name.") +
    req("3 marks", "Write", "A <code>Counter</code> class has one private attribute <code>Count</code> that starts at 0. Write its constructor.", "No parameters except self, because the value is fixed.", pc('''class Counter:
    # Count : INTEGER
    def __init__(self):
        self.__Count = 0'''), "Adding a parameter when the question says the value starts at 0.") +
    req("2 marks", "Explain", "Why is the first line of a child class's constructor a call to the parent's constructor?", "Link to the inherited attributes.", mks(["The parent's constructor sets the inherited attributes", "so the child object would be missing them if it were not called"]), "Saying the child 'copies' the parent. It runs the parent constructor on the same object."))

tipsl = [("Count the parameters.", "Only the values the question says are passed in. Everything else is set inside the constructor."), ("Always self first.", "def __init__(self, ...) in Python. A missing self is the commonest slip."), ("Every attribute needs self.", "self.__Name = NewName, not Name = NewName."), ("No return.", "A constructor sets values; it does not return anything."), ("Use the names from the question.", "Attribute names and data types are copied exactly into the comments.")]
sents = [("Say what it does", "The constructor is run when an object is created and sets the attributes to their starting values."), ("Say where values come from", "The values passed in are received as parameters and assigned to the attributes."), ("Say why a child calls the parent", "So the inherited attributes are initialised.")]

finish("ac20r1", "ac-20-1-2-constructor", "Constructors: Creating Objects",
       "What a constructor is, how it turns arguments into attributes, parameters against fixed starting values, and how it looks in Python and exam pseudocode; animations, labs and review questions.",
       learn, watch, explore, practise("cl", "o", "m", "c", "q"), real, review, tipsl, sents, stA + stB + lab)
