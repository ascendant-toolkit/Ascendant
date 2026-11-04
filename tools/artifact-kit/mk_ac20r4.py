"""20.1.2 extra resource: inheritance. Run: python3 tools/artifact-kit/mk_ac20r4.py"""
from ac20r import *

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p><b>Inheritance</b> lets a new class, the <b>child</b> (derived, subclass), take the attributes and methods of an existing <b>parent</b> (base, superclass) instead of rewriting them. The child can <b>add</b> its own attributes and methods, and can <b>override</b> a method by defining one with the same name. It is an <b>"is a"</b> relationship: a Parrot <i>is an</i> Animal. In Python the parent goes in brackets after the child's name, and the child's constructor calls the parent's. The shared code is written once, in the parent.</p></div>

  <h2>1 · Parent and child in code</h2>
  ''' + both('''class Animal:
    # Name : STRING
    # Sound : STRING
    def __init__(self, pName, pSound):
        self.__Name = pName
        self.__Sound = pSound
    def GetName(self):
        return self.__Name
    def Description(self):
        return self.__Name + " says " + self.__Sound

class Parrot(Animal):
    # WingSpan : INTEGER
    def __init__(self, pName, pSound, pWingSpan):
        super().__init__(pName, pSound)
        self.__WingSpan = pWingSpan
    def Description(self):
        return super().Description() + ", wingspan " + str(self.__WingSpan)''', '''CLASS Animal
  PRIVATE Name : STRING
  PRIVATE Sound : STRING
  PUBLIC PROCEDURE NEW(pName, pSound : STRING)
    Name <- pName
    Sound <- pSound
  ENDPROCEDURE
  PUBLIC FUNCTION GetName() RETURNS STRING
    RETURN Name
  ENDFUNCTION
  PUBLIC FUNCTION Description() RETURNS STRING
    RETURN Name & " says " & Sound
  ENDFUNCTION
ENDCLASS

CLASS Parrot INHERITS Animal
  PRIVATE WingSpan : INTEGER
  PUBLIC PROCEDURE NEW(pName, pSound : STRING, pWingSpan : INTEGER)
    SUPER.NEW(pName, pSound)
    WingSpan <- pWingSpan
  ENDPROCEDURE
  PUBLIC FUNCTION Description() RETURNS STRING
    RETURN SUPER.Description() & ", wingspan " & WingSpan
  ENDFUNCTION
ENDCLASS''') + '''

  <h2>2 · What the child gets</h2>
  <div class="tw"><table class="t">
    <tr><th>Item</th><th>Where it comes from</th><th>In the example</th></tr>
    <tr><td>Inherited attributes</td><td>Parent</td><td>Name, Sound (set by the parent constructor)</td></tr>
    <tr><td>Inherited methods</td><td>Parent, unless overridden</td><td><code>GetName()</code></td></tr>
    <tr><td>New attribute</td><td>Child only</td><td>WingSpan</td></tr>
    <tr><td>Overridden method</td><td>Child's own version, same name</td><td><code>Description()</code></td></tr>
  </table></div>
  <p class="note">The parent's attributes are private, so the child cannot use <code>self.__Name</code> directly. It reaches them through the parent's getters, or sets them by calling the parent's constructor.</p>

  <h2>3 · Writing a child class: the steps</h2>
  <ol>
    <li>Header with the parent in brackets: <code>class Parrot(Animal):</code></li>
    <li>Attribute comments for the <b>new</b> attributes only.</li>
    <li>Constructor taking the parent's values and the new ones.</li>
    <li>First line: call the parent's constructor with the inherited values.</li>
    <li>Assign the new attributes.</li>
    <li>Write the new or overriding methods.</li>
  </ol>

  <h2>4 · Why inherit?</h2>
  <p>Write once, reuse many times: Parrot, Dog and Cat all share Name and Sound without repeating them. A fix to Animal fixes every child. New kinds of animal are quick to add.</p>
'''

watch = '''
  <h2>1 · Building a child object</h2><p>Press Play, or click the steps.</p><div id="stA"></div>
  <h2>2 · Where does Python look for a method?</h2><div id="stB"></div>
'''

CH = ["super().__init__(pName, pSound)", "self.__WingSpan = pWingSpan"]
PA = ["self.__Name = pName", "self.__Sound = pSound"]
row = lambda a, b, c: ["Name: " + a, "Sound: " + b, "WingSpan: " + c]
child = lambda c="f1": cls(20, 20, 330, "Parrot.__init__ (child)", CH, c, 24)
parent = lambda c="f2": cls(20, 140, 330, "Animal.__init__ (parent)", PA, c, 24)
obj = lambda a, b, c, cl="f1", t="self (Parrot object)": cls(440, 20, 290, t, row(a, b, c), cl, 24)
stA = stepper("stA", "Building a Parrot object", 760, 250, [
    ('<code>Parrot("Polly", "Squawk", 30)</code> makes an empty Parrot object and runs the Parrot constructor.', [child(), obj("?", "?", "?")]),
    ("The first line calls the <b>parent's constructor</b> with the two inherited values.", [child("f3"), obj("?", "?", "?"), arr(180, 100, 180, 138, "d"), parent()]),
    ("<code>Animal.__init__</code> runs on the same object and sets Name and Sound.", [child(), obj('"Polly"', '"Squawk"', "?", "f2"), parent("f3")]),
    ("Control returns to the child, which sets <b>its own</b> attribute.", [child("f3"), obj('"Polly"', '"Squawk"', "30", "f3")]),
    ("One object has all three attributes. Without the parent call, Name and Sound would never exist.", [obj('"Polly"', '"Squawk"', "30", "f3", "complete Parrot object"), txt(30, 70, "inherited: Name, Sound", "lbl bd"), txt(30, 100, "new in Parrot: WingSpan", "lbl bd")])])

A1 = lambda c: cls(30, 20, 300, "class Animal", ["GetName()", "Description()  # version A"], c, 22)
P1 = lambda c: cls(400, 20, 320, "class Parrot(Animal)", ["Description()  # version B"], c, 22)
stB = stepper("stB", "Method lookup with inheritance", 760, 235, [
    ("Animal has <code>GetName()</code> and <code>Description()</code>. Parrot inherits from Animal and overrides <code>Description()</code> only.", [A1("f1"), P1("f2"), arr(398, 55, 334, 55, "l")]),
    ("<code>polly.Description()</code>: Python looks in Parrot first and finds version B, so it runs.", [A1("f1"), P1("f3"), arr(398, 55, 334, 55, "l"), txt(30, 170, "polly.Description()  runs B", "lbl bd t3")]),
    ("<code>polly.GetName()</code>: not in Parrot, so Python looks in the parent and finds it. The method is <b>inherited</b>.", [A1("f3"), P1("f1"), arr(398, 55, 334, 55, "l"), txt(30, 170, "polly.GetName()  runs Animal's", "lbl bd t3")]),
    ("Inside Parrot's version, <code>super().Description()</code> can still run the parent's version and add to it.", [A1("f3"), P1("f2"), arr(398, 55, 334, 55, "l"), txt(30, 170, "super().Description()  runs A", "lbl bd t3")])])

explore = '''
  <h2>Lab 1 · Which version runs?</h2>
  <p>Pick the kind of object and the method. See where the call is found.</p>
  <div class="card"><div class="btnrow" id="iO"></div><div class="btnrow" id="iM"></div><div id="iC"></div><div class="verdict" id="iL"></div></div>

  <h2>Lab 2 · Build a child class</h2>
  <p>Choose what the child adds or overrides. The code is written the way a mark scheme expects it.</p>
  <div class="card"><div class="btnrow"><label><input type="checkbox" id="bW" checked> new attribute WingSpan</label><label><input type="checkbox" id="bN"> new attribute NumberWords</label><label><input type="checkbox" id="bD" checked> override Description()</label><label><input type="checkbox" id="bC"> add method ChangeNumberWords()</label></div><div id="bO"></div></div>

  <h2>Lab 3 · Spot the mistake</h2>
  <div class="card"><div id="eB" class="btnrow"></div><div id="eO"></div></div>
'''

lab = r'''
(function () {
  const objs = ["Animal", "Parrot", "Dog"], meths = ["GetName()", "Description()", "Fetch()"];
  const has = { Animal: ["GetName()", "Description()"], Parrot: ["Description()"], Dog: ["Fetch()"] }, parent = { Parrot: "Animal", Dog: "Animal" };
  let o = "Parrot", m = "Description()";
  const find = () => { const path = []; let c = o; while (c) { path.push(c); if (has[c].includes(m)) return { path, found: c }; c = parent[c]; } return { path, found: null }; };
  const paint = () => {
    $$("#iO button").forEach((b) => b.classList.toggle("pri", b.textContent === o)); $$("#iM button").forEach((b) => b.classList.toggle("pri", b.textContent === m));
    const r = find();
    $("#iC").innerHTML = codeHTML(["x = " + o + "(...)", "x." + m]);
    $("#iL").textContent = r.found ? "Looked in " + r.path.join(" then ") + ": found in " + r.found + (r.found === o ? " (the object's own class)." : " (inherited from the parent).") : "Looked in " + r.path.join(" then ") + ": not found. AttributeError.";
  };
  $("#iO").innerHTML = objs.map((x) => `<button class="b">${x}</button>`).join(""); $("#iM").innerHTML = meths.map((x) => `<button class="b">${x}</button>`).join("");
  $$("#iO button").forEach((b) => (b.onclick = () => { o = b.textContent; paint(); })); $$("#iM button").forEach((b) => (b.onclick = () => { m = b.textContent; paint(); }));
  paint();
})();

(function () {
  const paint = () => {
    const w = $("#bW").checked, n = $("#bN").checked, d = $("#bD").checked, c = $("#bC").checked;
    const at = [w && ["WingSpan", "INTEGER"], n && ["NumberWords", "INTEGER"]].filter(Boolean);
    const L = ["class Parrot(Animal):"]; at.forEach((a) => L.push(`    # ${a[0]} : ${a[1]}`));
    L.push(`    def __init__(self, pName, pSound${at.map((a) => ", p" + a[0]).join("")}):`, "        super().__init__(pName, pSound)"); at.forEach((a) => L.push(`        self.__${a[0]} = p${a[0]}`));
    if (d) L.push("", "    def Description(self):", '        return super().Description() + " (a parrot)"');
    if (c) L.push("", "    def ChangeNumberWords(self, Amount):", "        self.__NumberWords = self.__NumberWords + Amount");
    $("#bO").innerHTML = codeHTML(L) + (c && !n ? '<div class="verdict">ChangeNumberWords uses NumberWords, so the Parrot needs that attribute: tick it.</div>' : "");
  };
  $$("#bW, #bN, #bD, #bC").forEach((x) => (x.onchange = paint)); paint();
})();

btnTable("eB", "eO", [
  ["No parent constructor", "class Parrot(Animal): def __init__(self, n, w): self.__WingSpan = w", "The inherited attributes are never set, so GetName() fails or returns nothing useful", "super().__init__(n, s) as the first line"],
  ["Parent not named", "class Parrot: ...", "Parrot does not inherit anything", "class Parrot(Animal):"],
  ["Using the parent's private attribute", "return self.__Name  # inside Parrot", "Private to Animal, so Parrot cannot reach it directly", "return self.GetName()"],
  ["Repeating inherited attributes in the comments", "# Name : STRING  # inside Parrot's list", "They belong to Animal. Only list the new ones", "List only WingSpan"],
  ["Misspelling the override", "def Descripton(self): ...", "A new method, not an override; the parent's version still runs", "Same name as the parent's method"],
  ["Saying 'a copy'", "'The child makes a copy of the parent'", "The child is linked to the parent's code, not a copy", "'The child inherits the parent's attributes and methods'"]
], ["Mistake", "Code or answer", "What goes wrong", "Fix"]);
''' + CLASSIFY("cl1", "For a Parrot that inherits from Animal, where does each come from?", ["Inherited from Animal", "New in Parrot", "Overridden in Parrot"],
    [("Name", 0), ("Sound", 0), ("WingSpan", 1), ("GetName()", 0), ("A Description() written again in Parrot", 2), ("ChangeNumberWords()", 1), ("NumberWords", 1), ("A method in Parrot with the same name as one in Animal", 2)],
    "Inherited items come from the parent; new items exist only in the child; an override is a child method with the parent's name.") + ORDER(
    "Put the steps for writing a child class in order.",
    ["Write the class header with the parent in brackets", "Add attribute comments for the new attributes only", "Write the constructor taking the parent's values and the new ones", "Call the parent constructor with the inherited values", "Assign the new attributes", "Write or override the methods that are different"],
    "Header, comments, constructor, parent call, new attributes, methods.") + MATCH([
    ["Parent class", "The class that is inherited from; also base or super class"], ["Child class", "The class that inherits; also derived class or subclass"], ["Inheritance", "A child takes the parent's attributes and methods"], ["Override", "A child method with the same name as the parent's"], ["super().__init__(...)", "Calls the parent's constructor"], ["is a", "The relationship between a child and its parent"]]) + MCQ([
    ("Which statement describes inheritance?", ["A class contains objects of another class", "A class takes the attributes and methods of another class", "Data is hidden in a class", "A method has many forms"], 1, "Child takes from parent."),
    ("How is a Python child class declared?", ["class Parrot inherits Animal", "class Parrot(Animal):", "class Animal(Parrot):", "Parrot = Animal"], 1, "Parent in brackets after the child's name."),
    ("What should the first line of the child's constructor usually do?", ["Print a message", "Call the parent's constructor", "Delete the parent", "Create a new parent"], 1, "It sets the inherited attributes."),
    ("Which describes 'is a'?", ["A Hand is a Card", "A Parrot is an Animal", "An Animal is a Parrot", "A Card is a Hand"], 1, "Inheritance is 'is a'; containment is 'has a'."),
    ("Why use inheritance?", ["To hide data", "To avoid rewriting shared code", "To make methods private", "To print objects"], 1, "Write once, reuse.")], "qz1") + CARDS([
    ("Inheritance", "A child class takes the parent's attributes and methods."), ("Parent / base / super class", "The class that is inherited from."), ("Child / derived / subclass", "The class that inherits."), ("class Child(Parent):", "Python's inheritance header."),
    ("super().__init__(...)", "Calls the parent constructor."), ("Override", "Same method name in the child, so the child's version runs."), ("is a", "A Parrot is an Animal."), ("INHERITS / SUPER", "Pseudocode keywords.")])

real = RWNOTE + (
    rw("Types of vehicle", "Car, Lorry and Motorbike all have a registration, a speed and a Move() method. They inherit those from Vehicle and add their own, such as a trailer count for a lorry.", "common features in the parent, differences in the child.") +
    rw("Types of employee", "Manager and Engineer inherit name, ID and a method that prints a payslip. A Manager adds a team size and overrides the payslip to include a bonus.", "child adds an attribute and overrides a method.") +
    rw("Game characters", "A Wizard and a Knight inherit position and health from Character. Each adds its own abilities.", "inheritance saves repeating the shared code.") +
    rw("Shapes in a drawing program", "Circle and Rectangle inherit colour and position from Shape and override Draw().", "same method name, different version in each child."))

review = (
    req("2 marks", "State", "What is meant by inheritance?", "A child gets the parent's items.", mks(["A child (derived) class takes the properties/attributes and methods of a parent (base) class", "and can add its own or override methods"])) +
    req("5 marks", "Write", "Class <code>Animal</code> has a constructor taking <code>pName</code> and <code>pSound</code>. Write the class <code>Dog</code> that inherits from it and adds a private attribute <code>Tricks</code> (INTEGER).", "Header with parent, comment, constructor with three parameters, parent call, new attribute.", pc('''class Dog(Animal):
    # Tricks : INTEGER
    def __init__(self, pName, pSound, pTricks):
        super().__init__(pName, pSound)
        self.__Tricks = pTricks'''), "Writing <code>self.__Name = pName</code> in the child instead of calling the parent.") +
    req("2 marks", "Explain", "Dog's constructor calls the parent's constructor first. Why?", "Link to the inherited attributes.", mks(["The parent's constructor sets the inherited attributes (Name and Sound)", "otherwise the Dog object would not have them"])) +
    req("3 marks", "Explain", "Parrot overrides <code>Description()</code>. A Parrot object calls <code>Description()</code>. Which version runs, and why?", "Child first.", mks(["Parrot's version runs", "because Python looks in the object's own class first", "and finds a method with that name, so it does not use the parent's"]), "Saying the parent's version runs because it was written first."))

tipsl = [("Parent first.", "super().__init__(...) is the first line of the child constructor."), ("List only the new attributes.", "The inherited ones belong to the parent."), ("Say 'is a'.", "A Parrot is an Animal. Containment is 'has a'."), ("Override means same name.", "A different name is a new method, not an override."), ("Don't repeat the parent.", "The point is to write shared code once.")]
sents = [("Define it", "Inheritance means a child class takes the attributes and methods of its parent class and can add its own."), ("Give a benefit", "The shared code is written once in the parent and reused by every child."), ("Describe the constructor", "The child's constructor calls the parent's constructor to set the inherited attributes, then sets its own.")]

finish("ac20r4", "ac-20-1-2-inheritance", "Inheritance: Parent and Child Classes",
       "What inheritance is, how a child class is written in Python and pseudocode, what it inherits, adds and overrides, and how the parent constructor is called; animations, labs and review questions.",
       learn, watch, explore, practise("cl", "o", "m", "q"), real, review, tipsl, sents, stA + stB + lab)
