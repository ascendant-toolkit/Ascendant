"""20.1.2 extra resource: getters and setters. Run: python3 tools/artifact-kit/mk_ac20r3.py"""
from ac20r import *

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>A <b>getter</b> is a method that <b>returns</b> the value of a private attribute. A <b>setter</b> is a method that <b>changes</b> it, using a new value passed in as a parameter. Because attributes are private, getters and setters are the only way other code can read or change them. Most getters have no parameter and most setters have one. If the attribute holds <b>several values</b>, such as a list of cards, the getter and setter need an extra <b>position</b> parameter to say which one.</p></div>

  <h2>1 · The standard pattern</h2>
  ''' + both('''class Pet:
    # PetName : STRING
    # YearBorn : INTEGER
    def __init__(self, NewName, NewYear):
        self.__PetName = NewName
        self.__YearBorn = NewYear

    def GetPetName(self):
        return self.__PetName

    def SetPetName(self, NewName):
        self.__PetName = NewName''', '''CLASS Pet
  PRIVATE PetName : STRING
  PRIVATE YearBorn : INTEGER
  PUBLIC PROCEDURE NEW(NewName : STRING, NewYear : INTEGER)
    PetName <- NewName
    YearBorn <- NewYear
  ENDPROCEDURE
  PUBLIC FUNCTION GetPetName() RETURNS STRING
    RETURN PetName
  ENDFUNCTION
  PUBLIC PROCEDURE SetPetName(NewName : STRING)
    PetName <- NewName
  ENDPROCEDURE
ENDCLASS''') + '''
  <div class="tw"><table class="t">
    <tr><th></th><th>Getter</th><th>Setter</th></tr>
    <tr><td>Job</td><td>Report the value</td><td>Change the value</td></tr>
    <tr><td>Body</td><td><code>return self.__X</code></td><td><code>self.__X = NewX</code></td></tr>
    <tr><td>Parameter (single value)</td><td>None, apart from self</td><td>One: the new value</td></tr>
    <tr><td>Returns</td><td>The value (a function)</td><td>Nothing (a procedure)</td></tr>
    <tr><td>Name</td><td><code>GetX</code></td><td><code>SetX</code></td></tr>
  </table></div>
  <p>Write a getter or setter for an attribute <b>only if the question asks</b>. The question names the ones it wants.</p>

  <h2>2 · Why a getter can have a parameter</h2>
  <p>A getter returns a value. If the attribute is a <b>single value</b>, there is only one thing it could return, so no parameter is needed. If the attribute holds <b>many values</b>, such as a list, the getter must be told which one.</p>
  ''' + both('''class Hand:
    # Cards : ARRAY[0:4] OF Card
    def __init__(self, Card1, Card2, Card3, Card4, Card5):
        self.__Cards = [Card1, Card2, Card3, Card4, Card5]

    def GetCard(self, Position):
        return self.__Cards[Position]

    def SetCard(self, Position, NewCard):
        self.__Cards[Position] = NewCard''', '''CLASS Hand
  PRIVATE Cards : ARRAY[0:4] OF Card
  PUBLIC FUNCTION GetCard(Position : INTEGER) RETURNS Card
    RETURN Cards[Position]
  ENDFUNCTION
  PUBLIC PROCEDURE SetCard(Position : INTEGER, NewCard : Card)
    Cards[Position] <- NewCard
  ENDPROCEDURE
ENDCLASS''') + '''
  <p>Here <code>GetCard(2)</code> returns the third card. The parameter is not a new value to store; it is an <b>index</b> that selects part of the attribute. The setter has two parameters, the position and the new value.</p>

  <h2>3 · Setters can check the value</h2>
  <div class="code">''' + pc('''def SetAge(self, NewAge):
    if NewAge >= 0 and NewAge <= 40:
        self.__Age = NewAge''') + '''</div>

  <h2>4 · Quick rules</h2>
  <div class="grid2">
    <div class="card"><h3>Getter</h3><p>Return. Never print. Never change anything.</p></div>
    <div class="card"><h3>Setter</h3><p>Assign. Never return. Replace the old value, or add to it, as the question says.</p></div>
  </div>
'''

watch = '''
  <h2>1 · A getter reads</h2><p>Press Play, or click the steps.</p><div id="stA"></div>
  <h2>2 · A setter writes</h2><div id="stB"></div>
  <h2>3 · A getter with a position</h2><div id="stC"></div>
'''

P = lambda n, y: ['__PetName: "' + n + '"', "__YearBorn: " + y]
GA = ["print(MyPet.GetPetName())", "def GetPetName(self):", "    return self.__PetName"]
stA = stepper("stA", "GetPetName()", 760, 215, [
    ("<code>print(MyPet.GetPetName())</code>: outside code asks the object for its name.", [code(20, 20, GA, 0, 340, 34), cls(420, 20, 300, "MyPet", P("Rex", "2021"), "f1", 24)]),
    ("The method runs inside the class.", [code(20, 20, GA, 1, 340, 34), cls(420, 20, 300, "MyPet", P("Rex", "2021"), "f1", 24)]),
    ("It reads <code>self.__PetName</code> and returns the value. The attribute is not changed.", [code(20, 20, GA, 2, 340, 34), cls(420, 20, 300, "MyPet", P("Rex", "2021"), "f3", 24), txt(20, 150, 'returns "Rex"', "lbl bd t3")]),
    ("<code>print</code> shows the returned value. The getter itself printed nothing.", [code(20, 20, GA, 0, 340, 34), cls(420, 20, 300, "MyPet", P("Rex", "2021"), "f1", 24), txt(20, 150, "Rex", "lbl bd t3")])])

SS = ['MyPet.SetPetName("Max")', "def SetPetName(self, NewName):", "    self.__PetName = NewName"]
stB = stepper("stB", 'SetPetName("Max")', 760, 215, [
    ('<code>MyPet.SetPetName("Max")</code>: outside code passes in a new name.', [code(20, 20, SS, 0, 340, 34), cls(420, 20, 300, "MyPet", P("Rex", "2021"), "f1", 24)]),
    ("The argument is copied into the parameter <code>NewName</code>.", [code(20, 20, SS, 1, 340, 34), cls(420, 20, 300, "MyPet", P("Rex", "2021"), "f1", 24), txt(20, 150, 'NewName = "Max"', "sm", 1)]),
    ("The assignment replaces the old value. Nothing is returned.", [code(20, 20, SS, 2, 340, 34), cls(420, 20, 300, "MyPet", P("Max", "2021"), "f3", 24)])])

cards = ["Card A", "Card B", "Card C", "Card D", "Card E"]
hand = lambda sel: [txt(20, 40, "self.__Cards", "lbl bd")] + [cls(20 + i * 144, 70, 132, cards[i], ["index " + str(i)], "f3" if i == sel else "f1", 20) for i in range(5)]
stC = stepper("stC", "GetCard(Position)", 760, 215, [
    ("A Hand holds five cards in a list. A getter with no parameter could only return the whole list.", hand(-1)),
    ("<code>MyHand.GetCard(2)</code>: the argument 2 is copied into the parameter <code>Position</code>.", hand(-1) + [txt(20, 190, "GetCard(2):  Position = 2", "sm", 1)]),
    ("<code>return self.__Cards[Position]</code> picks index 2, the third card, and returns it.", hand(2) + [txt(20, 190, "returns Card C", "lbl bd t3")]),
    ("A different argument, a different card: <code>GetCard(4)</code> returns the last one.", hand(4) + [txt(20, 190, "GetCard(4) returns Card E", "lbl bd t3")])])

explore = '''
  <h2>Lab 1 · Call the getters and setters</h2>
  <p>A Pet object has a name and a year born. Call the methods and watch the object and the return value.</p>
  <div class="card"><div id="gO"></div>
    <div class="btnrow"><button class="b" id="g1">GetPetName()</button><button class="b" id="g2">GetYearBorn()</button></div>
    <div class="btnrow"><label>New name <input id="gN" value="Max" size="8"></label><button class="b pri" id="g3">SetPetName(...)</button><label>New year <input id="gY" value="2019" size="5"></label><button class="b pri" id="g4">SetYearBorn(...)</button></div>
    <div id="gC"></div><div class="verdict" id="gL"></div></div>

  <h2>Lab 2 · GetCard with a position</h2>
  <p>Choose the position. The getter returns that item from the list; a getter with no parameter could not do this.</p>
  <div class="card"><div id="pO"></div><div class="btnrow"><label>Position <input type="range" id="pR" min="0" max="4" value="2"> <b id="pV">2</b></label></div><div id="pC"></div><div class="verdict" id="pL"></div></div>

  <h2>Lab 3 · Spot the mistake</h2>
  <div class="card"><div id="eB" class="btnrow"></div><div id="eO"></div></div>
'''

lab = r'''
(function () {
  const o = { n: "Rex", y: 2021 }; let last = ["", "Press a button."];
  const paint = () => {
    $("#gO").innerHTML = codeHTML(['MyPet.__PetName = "' + o.n + '"', "MyPet.__YearBorn = " + o.y]);
    $("#gC").innerHTML = codeHTML([last[0] || " "]);
    $("#gL").textContent = last[1];
  };
  $("#g1").onclick = () => { last = ["print(MyPet.GetPetName())", 'Returned "' + o.n + '". The object is unchanged.']; paint(); };
  $("#g2").onclick = () => { last = ["print(MyPet.GetYearBorn())", "Returned " + o.y + ". The object is unchanged."]; paint(); };
  $("#g3").onclick = () => { o.n = $("#gN").value; last = ['MyPet.SetPetName("' + o.n + '")', "Nothing returned. The name has changed."]; paint(); };
  $("#g4").onclick = () => { const v = parseInt($("#gY").value, 10); if (isNaN(v)) last = ["MyPet.SetYearBorn(" + $("#gY").value + ")", "That is not a whole number, so it was not stored."]; else { o.y = v; last = ["MyPet.SetYearBorn(" + v + ")", "Nothing returned. The year has changed."]; } paint(); };
  paint();
})();

(function () {
  const cards = ["Card A", "Card B", "Card C", "Card D", "Card E"];
  const paint = () => {
    const p = +$("#pR").value; $("#pV").textContent = p;
    $("#pO").innerHTML = '<div class="btnrow">' + cards.map((c, i) => `<span class="b ${i === p ? "pri" : ""}" style="pointer-events:none">${i}: ${c}</span>`).join("") + "</div>";
    $("#pC").innerHTML = codeHTML(["MyHand.GetCard(" + p + ")", "", "def GetCard(self, Position):", "    return self.__Cards[Position]   # index " + p]);
    $("#pL").textContent = "Returns " + cards[p] + ". The first card is index 0, so the last is index 4.";
  };
  $("#pR").oninput = paint; paint();
})();

btnTable("eB", "eO", [
  ["Printing in a getter", "def GetName(self): print(self.__Name)", "Shows the value but returns None, so the caller gets nothing to use", "return self.__Name"],
  ["Returning in a setter", "def SetAge(self, a): return a", "The attribute is never changed", "self.__Age = a"],
  ["Setter with no parameter", "def SetAge(self): self.__Age = 5", "Always stores 5; the caller cannot choose the value", "def SetAge(self, NewAge):"],
  ["Parameter ignored", "def GetCard(self, Position): return self.__Cards", "Returns the whole list, not the card asked for", "return self.__Cards[Position]"],
  ["Parameter in a simple getter", "def GetName(self, x): return self.__Name", "The caller has to pass something that is never used", "def GetName(self):"],
  ["Overwriting instead of adding", "self.__X = XChange", "The object jumps to the new value instead of moving by it", "self.__X = self.__X + XChange"]
], ["Mistake", "Code", "What goes wrong", "Fix"]);
''' + CLASSIFY("cl1", "Getter, setter or neither?", ["Getter", "Setter", "Neither"],
    [("def GetAge(self): return self.__Age", 0), ("def SetAge(self, a): self.__Age = a", 1), ("def GetCard(self, Position): return self.__Cards[Position]", 0), ("def SetCard(self, Position, c): self.__Cards[Position] = c", 1), ("def __init__(self, n): self.__Name = n", 2), ("def IncreaseSpeed(self): ...", 2), ("def GetName(self): print(self.__Name)", 2), ("def Description(self): return 'Pet'", 2)],
    "A getter returns an attribute; a setter assigns one. The constructor, and methods that do a calculation or just report text, are neither. A method that prints instead of returning is not a getter.") + ORDER(
    "Put the lines of a setter for Pet's name in order.",
    ["def SetPetName(self, NewName):", "    self.__PetName = NewName"], "Header with the new value as a parameter, then the assignment.") + MATCH([
    ["Getter", "Returns the value of a private attribute"], ["Setter", "Changes the value of a private attribute"], ["Position parameter", "Selects which item of a list attribute to return or change"], ["return", "Used in a getter, not in a setter"], ["self.__X = NewX", "The body of a simple setter"], ["Validation", "Checking the new value in a setter before storing it"]]) + CALC([
    {"q": "A Hand holds cards [4, 9, 2, 7, 1] in positions 0 to 4. What is the number returned by GetCard(3)?", "a": 7, "unit": "", "tol": 0.01, "hint": "Positions start at 0.", "sol": "<b>7</b>."},
    {"q": "Same Hand: which position holds the card with number 2?", "a": 2, "unit": "", "tol": 0.01, "hint": "Count from 0.", "sol": "<b>2</b>."},
    {"q": "A Character is at x = 10. SetXPosition(25) is called. What does GetXPosition() return?", "a": 25, "unit": "", "tol": 0.01, "hint": "A setter replaces the value.", "sol": "<b>25</b>."},
    {"q": "A Character is at x = 10. ChangePosition(4) adds to the x coordinate. What is x afterwards?", "a": 14, "unit": "", "tol": 0.01, "hint": "Add, not replace.", "sol": "<b>14</b>."}]) + MCQ([
    ("A getter should...", ["Change the attribute", "Return the attribute's value", "Print the attribute", "Delete the attribute"], 1, "It returns without changing."),
    ("A setter for a single attribute normally has...", ["No parameters", "One parameter, the new value", "Two parameters", "A return statement"], 1, "The new value arrives as a parameter."),
    ("Why does GetCard(self, Position) have a parameter?", ["Getters must have parameters", "The attribute holds several values and it must say which", "It is a setter", "To make it private"], 1, "Position selects one item of the list."),
    ("Which statement is false?", ["Setters do not return a value", "Getters change the attribute", "Getters return a value", "Setters assign a value"], 1, "Getters do not change the attribute."),
    ("How many getters should you write?", ["One per attribute always", "Those the question asks for", "None", "Two per attribute"], 1, "Follow the question.")], "qz1") + CARDS([
    ("Getter", "Returns the value of a private attribute."), ("Setter", "Changes the value of a private attribute."), ("def GetX(self)", "return self.__X"), ("def SetX(self, NewX)", "self.__X = NewX"),
    ("GetCard(self, Position)", "A getter that needs an index because the attribute is a list."), ("Setter validation", "If the value is valid, assign it."), ("Getter: never print", "It returns; the caller prints."), ("Setter: never return", "It assigns.")])

real = RWNOTE + (
    rw("A thermostat", "Reading the temperature is a getter. Setting the target temperature is a setter, and it refuses values outside a safe range.", "a setter with validation.") +
    rw("A playlist", "GetSong(position) returns the song at a position. SetSong(position, song) replaces it. Both need the position because the attribute holds many songs.", "getter and setter with a position.") +
    rw("A player profile", "The profile page calls GetUsername() to show the name and SetUsername() when it is edited. The rest of the game never touches the stored value.", "getter reports, setter updates.") +
    rw("A medical appointment", "A report calls GetDoctor() and GetDate(). A receptionist uses SetDate() to move the appointment. Reports never change the data.", "the report only reads; the setter changes."))

review = (
    req("2 marks", "State", "What is the purpose of a getter and of a setter?", "One mark each.", mks(["A getter returns the value of a private attribute", "A setter changes (sets) the value of a private attribute"])) +
    req("3 marks", "Write", "Write the getter and setter for the private attribute <code>Doctor</code> in the class <code>Appointment</code>.", "Self in both; return in the getter; the new value as a parameter in the setter.", pc('''def GetDoctor(self):
    return self.__Doctor

def SetDoctor(self, NewDoctor):
    self.__Doctor = NewDoctor'''), "Using print in the getter.") +
    req("4 marks", "Write", "A class <code>Hand</code> has a private list <code>Cards</code> of five Card objects. Write a getter that returns the card at a given position.", "The parameter is the position; the body indexes the list.", pc('''def GetCard(self, Position):
    return self.__Cards[Position]'''), "Returning <code>self.__Cards</code> with no index.") +
    req("2 marks", "Explain", "Explain why <code>GetCard</code> has a parameter when <code>GetPetName</code> does not.", "Compare a single value and a collection.", mks(["GetCard's attribute holds several values (a list/array)", "so the parameter says which one to return; GetPetName's attribute is a single value"])))

tipsl = [("Getter: return.", "Never print, never assign."), ("Setter: assign.", "Never return. The new value is the parameter."), ("A parameter on a getter means a list.", "The parameter is the position, not a value to store."), ("Write only what is asked.", "The question names which getters and setters it wants."), ("Count marks.", "Each part of the method is a mark: header, self, return or assignment.")]
sents = [("Describe a getter", "A getter returns the value of a private attribute so that other code can read it without changing it."), ("Describe a setter", "A setter assigns a new value to a private attribute, and can check the value first."), ("Explain a position parameter", "The attribute is an array, so the position says which element to return.")]

finish("ac20r3", "ac-20-1-2-getters-and-setters", "Getters and Setters",
       "What getters and setters do, why they exist, why a getter sometimes takes a position, and how to write them in Python and pseudocode; animations, labs and review questions.",
       learn, watch, explore, practise("cl", "o", "m", "c", "q"), real, review, tipsl, sents, stA + stB + stC + lab)
