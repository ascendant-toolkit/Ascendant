"""20.1.2 extra resource: containment. Run: python3 tools/artifact-kit/mk_ac20r6.py"""
from ac20r import *

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p><b>Containment</b> (also called <b>aggregation</b>) is when one class has an attribute that is an <b>object of another class</b>, or an array of them. It is a <b>"has a"</b> relationship: a Hand <i>has</i> Cards. The contained objects are created <b>first</b> and passed to the container's constructor. The container reaches them through its own methods, and a call can be chained: <code>MyHand.GetCard(2).GetNumber()</code>. Containment is different from inheritance, which is "is a".</p></div>

  <h2>1 · A Hand that contains Cards</h2>
  ''' + both('''class Card:
    # Number : INTEGER
    # Colour : STRING
    def __init__(self, NewNumber, NewColour):
        self.__Number = NewNumber
        self.__Colour = NewColour
    def GetNumber(self):
        return self.__Number
    def GetColour(self):
        return self.__Colour

class Hand:
    # Cards : ARRAY[0:4] OF Card
    def __init__(self, Card1, Card2, Card3, Card4, Card5):
        self.__Cards = [Card1, Card2, Card3, Card4, Card5]
    def GetCard(self, Position):
        return self.__Cards[Position]''', '''CLASS Card
  PRIVATE Number : INTEGER
  PRIVATE Colour : STRING
  PUBLIC PROCEDURE NEW(NewNumber : INTEGER, NewColour : STRING)
    Number <- NewNumber
    Colour <- NewColour
  ENDPROCEDURE
  PUBLIC FUNCTION GetNumber() RETURNS INTEGER
    RETURN Number
  ENDFUNCTION
  PUBLIC FUNCTION GetColour() RETURNS STRING
    RETURN Colour
  ENDFUNCTION
ENDCLASS

CLASS Hand
  PRIVATE Cards : ARRAY[0:4] OF Card
  PUBLIC PROCEDURE NEW(Card1, Card2, Card3, Card4, Card5 : Card)
    Cards[0] <- Card1
    Cards[1] <- Card2
    Cards[2] <- Card3
    Cards[3] <- Card4
    Cards[4] <- Card5
  ENDPROCEDURE
  PUBLIC FUNCTION GetCard(Position : INTEGER) RETURNS Card
    RETURN Cards[Position]
  ENDFUNCTION
ENDCLASS''') + '''

  <h2>2 · Creating them in the right order</h2>
  <div class="code">''' + pc('''C1 = Card(4, "Red")
C2 = Card(9, "Blue")
C3 = Card(2, "Red")
C4 = Card(7, "Green")
C5 = Card(1, "Blue")
MyHand = Hand(C1, C2, C3, C4, C5)''') + '''</div>
  <p>The Hand needs the Cards to exist before its constructor runs, because they are passed in as arguments. Creating the Hand first would leave nothing to pass.</p>

  <h2>3 · Reaching a contained object</h2>
  <div class="code">''' + pc('''ThirdCard = MyHand.GetCard(2)         # a Card object
print(ThirdCard.GetNumber())          # 2
print(MyHand.GetCard(2).GetNumber())  # the same, chained''') + '''</div>
  <p>Read the chain left to right: the Hand returns a Card, then that Card is asked for its number. The Hand never needs to know how a Card stores its number.</p>

  <h2>4 · Has-a or is-a?</h2>
  <div class="tw"><table class="t">
    <tr><th></th><th>Containment</th><th>Inheritance</th></tr>
    <tr><td>Relationship</td><td>"has a"</td><td>"is a"</td></tr>
    <tr><td>Example</td><td>A Hand has Cards</td><td>A Parrot is an Animal</td></tr>
    <tr><td>In code</td><td>An attribute that is an object</td><td>The parent in brackets after the class name</td></tr>
    <tr><td>Test</td><td>A Hand is not a Card</td><td>A Parrot is an Animal</td></tr>
  </table></div>
  <p class="note">Say the sentence out loud. If "A is a B" sounds right, use inheritance. If "A has a B" sounds right, use containment.</p>
'''

watch = '''
  <h2>1 · Creating the contained objects, then the container</h2><p>Press Play, or click the steps.</p><div id="stA"></div>
  <h2>2 · A chained call</h2><div id="stB"></div>
'''

cardv = ["4 Red", "9 Blue", "2 Red", "7 Green", "1 Blue"]
cb = lambda n, hl=-1: [cls(20 + i * 144, 20, 130, "Card " + str(i + 1), [cardv[i]], "f3" if i == hl else "f1", 22) for i in range(n)]
LST = "__Cards: [Card 1, Card 2, Card 3, Card 4, Card 5]"
stA = stepper("stA", "Five Cards, then a Hand", 760, 250, [
    ("Five Card objects are created first, one statement each.", cb(5)),
    ("<code>Hand(C1, C2, C3, C4, C5)</code> passes the five Card objects to the Hand constructor.", cb(5) + [txt(20, 130, "MyHand = Hand(C1, C2, C3, C4, C5)", "sm", 1)]),
    ("The constructor stores them in a list: <code>self.__Cards = [Card1, ..., Card5]</code>.", cb(5) + [cls(20, 140, 700, "MyHand", [LST], "f3", 22)]),
    ("The Hand now <b>has</b> five Cards. The cards are objects in their own right, with their own methods.", cb(5) + [cls(20, 140, 700, "MyHand has Cards", [LST], "f3", 22), txt(20, 235, "has-a relationship", "lbl bd t3")])])

stB = stepper("stB", "MyHand.GetCard(2).GetNumber()", 760, 250, [
    ("The whole call is <code>MyHand.GetCard(2).GetNumber()</code>. It is evaluated from left to right.", cb(5) + [txt(20, 130, "MyHand.GetCard(2).GetNumber()", "lbl bd", 1)]),
    ("<code>MyHand.GetCard(2)</code> asks the Hand for the card at position 2. It returns a Card object.", cb(5, 2) + [txt(20, 130, "MyHand.GetCard(2)  ->  Card 3", "sm", 1)]),
    ("<code>.GetNumber()</code> is now called on that Card, not on the Hand. The Card returns its number.", cb(5, 2) + [txt(20, 130, "Card 3 .GetNumber()  ->  2", "lbl bd t3", 1), txt(20, 165, "the Hand never needs to know how a Card stores its number", "sm")])])

explore = '''
  <h2>Lab 1 · Chain a call through the Hand</h2>
  <p>Choose a position and which method to call on the card that comes back.</p>
  <div class="card"><div id="hO"></div><div class="btnrow"><label>Position <input type="range" id="hR" min="0" max="4" value="2"> <b id="hV">2</b></label><button class="b pri" id="hN">GetNumber()</button><button class="b" id="hC">GetColour()</button></div><div id="hC2"></div><div class="verdict" id="hL"></div></div>

  <h2>Lab 2 · Has-a or is-a?</h2>
  <p>Pick a pair. Say the sentence and decide.</p>
  <div class="card"><div id="aB" class="btnrow"></div><div id="aO"></div></div>

  <h2>Lab 3 · Spot the mistake</h2>
  <div class="card"><div id="eB" class="btnrow"></div><div id="eO"></div></div>
'''

lab = r'''
(function () {
  const cards = [[4, "Red"], [9, "Blue"], [2, "Red"], [7, "Green"], [1, "Blue"]]; let m = "N";
  const paint = () => {
    const p = +$("#hR").value; $("#hV").textContent = p;
    $("#hO").innerHTML = '<div class="btnrow">' + cards.map((c, i) => `<span class="b ${i === p ? "pri" : ""}" style="pointer-events:none">${i}: ${c[0]} ${c[1]}</span>`).join("") + "</div>";
    $("#hN").classList.toggle("pri", m === "N"); $("#hC").classList.toggle("pri", m === "C");
    const call = "MyHand.GetCard(" + p + ")." + (m === "N" ? "GetNumber()" : "GetColour()");
    $("#hC2").innerHTML = codeHTML(["print(" + call + ")"]);
    $("#hL").textContent = "GetCard(" + p + ") returns the card " + cards[p][0] + " " + cards[p][1] + ", then " + (m === "N" ? "GetNumber() returns " + cards[p][0] : "GetColour() returns " + cards[p][1]) + ".";
  };
  $("#hR").oninput = paint; $("#hN").onclick = () => { m = "N"; paint(); }; $("#hC").onclick = () => { m = "C"; paint(); }; paint();
})();

btnTable("aB", "aO", [
  ["Hand and Card", "A Hand has Cards", "A Hand is not a Card", "Containment: the Hand's attribute is an array of Card objects"],
  ["Parrot and Animal", "A Parrot is an Animal", "An Animal does not have a Parrot", "Inheritance: class Parrot(Animal)"],
  ["Car and Engine", "A Car has an Engine", "A Car is not an Engine", "Containment: Car holds an Engine object"],
  ["Dog and Animal", "A Dog is an Animal", "An Animal does not have a Dog", "Inheritance: class Dog(Animal)"],
  ["Library and Book", "A Library has Books", "A Library is not a Book", "Containment: a list of Book objects"],
  ["Manager and Employee", "A Manager is an Employee", "An Employee does not have a Manager", "Inheritance: class Manager(Employee)"]
], ["Pair", "Say it", "Check the other way", "Answer"]);

btnTable("eB", "eO", [
  ["Hand created first", "MyHand = Hand(C1, C2, C3, C4, C5)  # before the Cards exist", "NameError: C1 does not exist yet", "Create the five Cards, then the Hand"],
  ["Forgetting the position", "def GetCard(self): return self.__Cards", "Returns the whole list, not one card", "def GetCard(self, Position): return self.__Cards[Position]"],
  ["Chain in the wrong order", "MyHand.GetNumber().GetCard(2)", "The Hand has no GetNumber(); that method belongs to Card", "MyHand.GetCard(2).GetNumber()"],
  ["Using inheritance instead", "class Hand(Card): ...", "A Hand is not a Card; it has Cards", "Store Card objects in an attribute"],
  ["Reaching into the Card", "MyHand.GetCard(2).__Number", "Number is private to Card", "MyHand.GetCard(2).GetNumber()"],
  ["Counting from 1", "MyHand.GetCard(5)", "IndexError: positions 0 to 4 only", "MyHand.GetCard(4) for the last card"]
], ["Mistake", "Code", "What goes wrong", "Fix"]);
''' + CLASSIFY("cl1", "Containment or inheritance?", ["Containment (has a)", "Inheritance (is a)"],
    [("A Hand and its five Cards", 0), ("A Parrot and an Animal", 1), ("A Library and its Books", 0), ("A Manager and an Employee", 1), ("A Car and its Engine", 0), ("A Dog and an Animal", 1), ("A Playlist and its Songs", 0), ("A Circle and a Shape", 1)],
    "Say the sentence. A Hand has Cards (containment). A Parrot is an Animal (inheritance).") + ORDER(
    "Put the steps in order: building a Hand.",
    ["Create the first Card", "Create the other four Cards", "Pass the five Cards to the Hand constructor", "The constructor stores them in a list attribute", "The Hand now has five Cards"],
    "Create the contained objects first, then the container.") + MATCH([
    ["Containment", "A class has an attribute that is an object of another class"], ["Aggregation", "Another name for containment"], ["has a", "The relationship in containment"], ["MyHand.GetCard(2).GetNumber()", "A chained call: the Hand returns a Card, then the Card is asked for its number"], ["Container", "The class that holds the other objects"], ["Contained object", "An object stored as an attribute of another object"]]) + CALC([
    {"q": "A Hand holds Cards numbered [4, 9, 2, 7, 1]. What does MyHand.GetCard(1).GetNumber() return?", "a": 9, "unit": "", "tol": 0.01, "hint": "Position 1 is the second card.", "sol": "<b>9</b>."},
    {"q": "Same Hand: what does MyHand.GetCard(4).GetNumber() return?", "a": 1, "unit": "", "tol": 0.01, "hint": "Position 4 is the last.", "sol": "<b>1</b>."},
    {"q": "How many Card objects must exist before the Hand constructor is called with five parameters?", "a": 5, "unit": "", "tol": 0.01, "hint": "One argument per parameter.", "sol": "<b>5</b>."},
    {"q": "A Library holds 12 Book objects. How many objects exist in total including the Library?", "a": 13, "unit": "", "tol": 0.01, "hint": "The 12 books plus the Library.", "sol": "<b>13</b>."}]) + MCQ([
    ("What is containment?", ["A child class takes its parent's methods", "A class has an attribute that is an object of another class", "Data is hidden", "A method has many forms"], 1, "Has a."),
    ("Which is a containment relationship?", ["Parrot and Animal", "Hand and Card", "Dog and Animal", "Manager and Employee"], 1, "A Hand has Cards."),
    ("Which must happen first?", ["The Hand is created, then the Cards", "The Cards are created, then the Hand", "Either order", "The Hand is deleted"], 1, "The Cards are passed in to the Hand's constructor."),
    ("What does MyHand.GetCard(2).GetNumber() do?", ["Asks the Hand for its number", "Gets the third Card, then asks that Card for its number", "Gets the second Card", "Creates a new Card"], 1, "Left to right."),
    ("Another name for containment is...", ["Overriding", "Aggregation", "Polymorphism", "Instantiation"], 1, "The syllabus uses both names.")], "qz1") + CARDS([
    ("Containment", "A class has an attribute that is an object (or array of objects) of another class."), ("Aggregation", "Another name for containment."), ("has a", "The relationship: a Hand has Cards."), ("is a", "Inheritance, not containment."),
    ("Create contained first", "Cards first, then the Hand that holds them."), ("Chained call", "MyHand.GetCard(2).GetNumber()"), ("Container", "The class holding the objects, such as Hand."), ("Contained", "The objects held, such as Card.")])

real = RWNOTE + (
    rw("Cards, hands and a deck", "A Hand holds five Cards and asks each one for its number and colour. A Deck holds many Cards. The Cards know nothing about the Hand.", "classic containment: objects working through their methods.") +
    rw("A school and its classes", "A School object holds Class objects and each Class holds Student objects. A report asks the School, then the Class, then the Student.", "objects inside objects, with a chain of calls.") +
    rw("A car and its parts", "A Car has an Engine, four Wheels and a Radio. Each part is its own class with its own methods.", "'has a' for each part.") +
    rw("A linked list", "A LinkedList holds Node objects, and each Node holds data and a pointer to the next Node.", "data structures are often built from containment."))

review = (
    req("2 marks", "State", "What is meant by containment (aggregation)?", "Say what the class holds.", mks(["One class contains / has an attribute that is an object of another class", "a 'has a' relationship, for example a Hand holds Card objects"])) +
    req("2 marks", "Explain", "Explain why the Card objects must be created before the Hand object.", "Link to the constructor.", mks(["The Hand's constructor takes the Card objects as parameters", "so they have to exist before they can be passed in"])) +
    req("4 marks", "Write", "Write the class <code>Hand</code> in Python with a constructor taking five Card objects stored in a private list, and a method <code>GetCard</code> that returns the card at a given position.", "List attribute, five parameters, getter with a position.", pc('''class Hand:
    # Cards : ARRAY[0:4] OF Card
    def __init__(self, Card1, Card2, Card3, Card4, Card5):
        self.__Cards = [Card1, Card2, Card3, Card4, Card5]
    def GetCard(self, Position):
        return self.__Cards[Position]'''), "A getter with no position, so it returns the whole list.") +
    req("3 marks", "Write", "Write one statement that prints the colour of the second card in <code>MyHand</code>.", "Index 1 is the second card.", pc('''print(MyHand.GetCard(1).GetColour())'''), "Using GetCard(2), which is the third card."))

tipsl = [("Say has a.", "A Hand has Cards. Use that wording in your answer."), ("Contained objects first.", "Create them, then the container."), ("Chain left to right.", "MyHand.GetCard(2).GetNumber(): Hand first, then Card."), ("Count from 0.", "The last of five is position 4."), ("Don't use inheritance.", "A Hand is not a Card.")]
sents = [("Define it", "Containment means a class has an attribute that is an object of another class, for example a Hand that contains Card objects."), ("Describe the order", "The Card objects are created first and passed to the Hand's constructor."), ("Describe a chain", "GetCard returns a Card object, and GetNumber is then called on that Card.")]

finish("ac20r6", "ac-20-1-2-containment", "Containment: Objects Inside Objects",
       "What containment (aggregation) is, how a Hand holds Cards, the order objects are created in, how to chain calls through a contained object, and how it differs from inheritance; animations, labs and review questions.",
       learn, watch, explore, practise("cl", "o", "m", "c", "q"), real, review, tipsl, sents, stA + stB + lab)
