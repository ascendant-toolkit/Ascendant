"""20.1.2 extra resource: polymorphism. Run: python3 tools/artifact-kit/mk_ac20r5.py"""
from ac20r import *

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p><b>Polymorphism</b> means "many forms". Several classes have a method with the <b>same name</b>, and each class gives it its <b>own behaviour</b>. The code that calls the method does not need to know which class the object belongs to: it makes the same call and the object responds in its own way. It is built on <b>inheritance</b>, with a child <b>overriding</b> a method of its parent. The advantage is that one loop can handle a whole list of different objects.</p></div>

  <h2>1 · One method name, different results</h2>
  ''' + both('''class Animal:
    def __init__(self, pName):
        self.__Name = pName
    def GetName(self):
        return self.__Name
    def Description(self):
        return self.__Name + " is an animal"

class Parrot(Animal):
    def Description(self):
        return self.GetName() + " is a parrot that squawks"

class Dog(Animal):
    def Description(self):
        return self.GetName() + " is a dog that barks"

Zoo = [Animal("Generic"), Parrot("Polly"), Dog("Rex")]
for Item in Zoo:
    print(Item.Description())''', '''CLASS Animal
  PRIVATE Name : STRING
  PUBLIC FUNCTION GetName() RETURNS STRING
    RETURN Name
  ENDFUNCTION
  PUBLIC FUNCTION Description() RETURNS STRING
    RETURN Name & " is an animal"
  ENDFUNCTION
ENDCLASS

CLASS Parrot INHERITS Animal
  PUBLIC FUNCTION Description() RETURNS STRING
    RETURN GetName() & " is a parrot that squawks"
  ENDFUNCTION
ENDCLASS

CLASS Dog INHERITS Animal
  PUBLIC FUNCTION Description() RETURNS STRING
    RETURN GetName() & " is a dog that barks"
  ENDFUNCTION
ENDCLASS''') + '''
  <div class="code">''' + pc('''Generic is an animal
Polly is a parrot that squawks
Rex is a dog that barks''') + '''</div>
  <p>The loop calls <code>Item.Description()</code> every time. It never tests what kind of animal it has. Each object runs the version from its own class.</p>

  <h2>2 · Polymorphism and overriding: how they fit</h2>
  <div class="tw"><table class="t">
    <tr><th>Term</th><th>What it is</th></tr>
    <tr><td>Overriding</td><td>The <b>mechanism</b>: a child class redefines a parent's method, keeping the name.</td></tr>
    <tr><td>Polymorphism</td><td>The <b>effect</b>: the same call behaves differently depending on the object it is made on.</td></tr>
  </table></div>

  <h2>3 · Why it helps</h2>
  <div class="grid2">
    <div class="card"><h3>No chains of IF</h3><p>Without it the loop would need a test for each kind of animal and a different call for each.</p></div>
    <div class="card"><h3>New classes cost nothing</h3><p>Add a Cat class with its own Description(). The loop does not change at all.</p></div>
  </div>
'''

watch = '''
  <h2>1 · One call, three behaviours</h2><p>Press Play, or click the steps.</p><div id="stA"></div>
  <h2>2 · Adding a new class</h2><div id="stB"></div>
'''

LOOP = "for Item in Zoo:  print(Item.Description())"
Z = lambda hl: [cls(30 + i * 235, 40, 215, n, ["Description()"], "f3" if i == hl else "f1", 22) for i, n in enumerate(["Animal", "Parrot", "Dog"])]
stA = stepper("stA", "A loop over a list of objects", 760, 225, [
    ("A list holds three objects of different classes. The loop calls <code>Item.Description()</code> on each.", Z(-1) + [txt(30, 150, LOOP, "sm", 1)]),
    ("First object is an Animal: its <code>Description()</code> runs.", Z(0) + [txt(30, 150, "Item.Description()  ->  Generic is an animal", "lbl bd t3")]),
    ("Second is a Parrot. The same call, but Parrot's version runs.", Z(1) + [txt(30, 150, "Item.Description()  ->  Polly is a parrot that squawks", "lbl bd t3")]),
    ("Third is a Dog. Same call again, Dog's version.", Z(2) + [txt(30, 150, "Item.Description()  ->  Rex is a dog that barks", "lbl bd t3")]),
    ("One line of code, three different results: that is polymorphism.", Z(-1) + [txt(30, 150, "same call, different behaviour", "lbl bd t3")])])

W = lambda n, hl: [cls(30 + i * (700 // n), 40, 700 // n - 20, k, ["Description()"], "f3" if i == hl else "f1", 22) for i, k in enumerate(["Animal", "Parrot", "Dog", "Cat"][:n])]
stB = stepper("stB", "A new class, the loop unchanged", 760, 225, [
    ("The loop works for Animal, Parrot and Dog.", W(3, -1) + [txt(30, 150, LOOP, "sm", 1)]),
    ("A new class <code>Cat(Animal)</code> is written with its own <code>Description()</code>.", W(4, 3) + [txt(30, 150, LOOP, "sm", 1)]),
    ("A Cat is added to the list. The loop code is exactly the same.", W(4, 3) + [txt(30, 150, "Item.Description()  ->  Tilly is a cat that purrs", "lbl bd t3"), txt(30, 185, "loop code unchanged", "sm")])])

explore = '''
  <h2>Lab 1 · Fill the zoo and run the loop</h2>
  <p>Add animals to the list, then run the loop. Notice that the loop code never changes.</p>
  <div class="card"><div class="btnrow"><button class="b" id="zA">Add Animal</button><button class="b" id="zP">Add Parrot</button><button class="b" id="zD">Add Dog</button><button class="b" id="zC">Add Cat</button><button class="b" id="zR">Clear</button></div>
    <div id="zL"></div><div class="btnrow"><button class="b pri" id="zGo">Run the loop</button></div><div id="zO"></div></div>

  <h2>Lab 2 · Spot the mistake</h2>
  <div class="card"><div id="eB" class="btnrow"></div><div id="eO"></div></div>
'''

lab = r'''
(function () {
  const say = { Animal: " is an animal", Parrot: " is a parrot that squawks", Dog: " is a dog that barks", Cat: " is a cat that purrs" };
  const names = { Animal: "Generic", Parrot: "Polly", Dog: "Rex", Cat: "Tilly" }; let zoo = [];
  const paint = () => { $("#zL").innerHTML = codeHTML(["Zoo = [" + zoo.map((k) => k + '("' + names[k] + '")').join(", ") + "]", "for Item in Zoo:", "    print(Item.Description())"]); };
  [["zA", "Animal"], ["zP", "Parrot"], ["zD", "Dog"], ["zC", "Cat"]].forEach(([id, k]) => ($("#" + id).onclick = () => { zoo.push(k); paint(); }));
  $("#zR").onclick = () => { zoo = []; $("#zO").innerHTML = ""; paint(); };
  $("#zGo").onclick = () => { $("#zO").innerHTML = '<div class="verdict">' + (zoo.length ? zoo.map((k) => esc(names[k] + say[k])).join("<br>") : "The list is empty, so nothing is printed.") + "</div>"; };
  paint();
})();

btnTable("eB", "eO", [
  ["Different method names", "Parrot.ParrotDescription() and Dog.DogDescription()", "No polymorphism: the caller has to know which name to use for which class", "Same name, Description(), in each class"],
  ["Testing the type", "if type(Item) == Parrot: ... elif type(Item) == Dog: ...", "The code has to change for every new class", "Item.Description() and let the object decide"],
  ["Misspelling the name", "def Descripton(self): ...  # in Parrot", "The spelling differs, so it is a new method and the parent's still runs", "Match the name exactly"],
  ["Confusing it with inheritance", "'Polymorphism is when a class takes its parent's methods'", "That is inheritance", "Same method name, different behaviour per class"],
  ["Only one class", "A single Animal class with Description()", "There is no variety, so nothing is polymorphic", "At least two classes with the method"]
], ["Mistake", "Code or answer", "What goes wrong", "Fix"]);
''' + CLASSIFY("cl1", "Which idea is described?", ["Inheritance", "Overriding", "Polymorphism"],
    [("A Parrot gets Name and Sound from Animal", 0), ("Parrot defines Description() with the same name as Animal's", 1), ("One loop calls Description() on a list holding Animals, Parrots and Dogs", 2), ("class Dog(Animal):", 0), ("The same call gives different results depending on the object", 2), ("A child redefines a parent's method", 1), ("A child class is written without repeating the shared attributes", 0), ("A new class is added and the loop is not changed", 2)],
    "Inheritance shares code; overriding replaces a method; polymorphism is the effect of one call giving different behaviours.") + ORDER(
    "Put the steps in order: what happens when the loop calls Item.Description() on a Dog.",
    ["The loop takes the next object from the list", "It calls Item.Description()", "Python looks in the object's own class, Dog", "Dog has a Description(), so it runs", "The Dog's text is printed"],
    "Take, call, look in own class, run, print.") + MATCH([
    ["Polymorphism", "The same method call behaves differently for objects of different classes"], ["Overriding", "A child redefines a method with the same name as the parent's"], ["Inheritance", "A child takes the parent's attributes and methods"], ["Base class", "The class that inherited methods come from"], ["Same name, different behaviour", "The key idea of polymorphism"]]) + MCQ([
    ("What does polymorphism mean?", ["One class inside another", "Same method name, different behaviour in different classes", "Hiding data", "Copying a class"], 1, "Many forms."),
    ("Which makes polymorphism possible in the exam?", ["Overriding a method in a child class", "Making attributes public", "A longer constructor", "Using print"], 0, "The child redefines the parent's method."),
    ("A list holds Animal, Parrot and Dog objects. Item.Description() is called for each. What happens?", ["An error", "Each object runs its own class's version", "Only Animal's version runs", "The first object's version runs for all"], 1, "That is polymorphism."),
    ("What is the main advantage?", ["Faster programs", "New classes can be added without changing the calling code", "Data is hidden", "Less memory"], 1, "The loop does not need to know the type."),
    ("Which is an example of the same method name in two classes with different behaviour?", ["GetName in Animal and Dog, inherited", "Description in Parrot and Dog, each written differently", "__init__ in Animal only", "Fetch in Dog only"], 1, "Same name, different behaviour.")], "qz1") + CARDS([
    ("Polymorphism", "Same method name; each class behaves in its own way."), ("Overriding", "A child redefines a parent's method."), ("Inheritance", "Child takes the parent's attributes and methods."), ("Why use polymorphism?", "One loop works for many classes; new classes need no changes."),
    ("Description() example", "Animal, Parrot and Dog each print their own text."), ("Not polymorphism", "Different method names for each class."), ("Not polymorphism", "A chain of IFs testing the class."), ("Many forms", "The meaning of the word polymorphism.")])

real = RWNOTE + (
    rw("A drawing program", "Every shape has Draw(). A Circle draws a circle and a Square draws a square. The program loops over the shapes and calls Draw() on each.", "same call, different drawing.") +
    rw("Payments", "Card, Cash and Voucher each have Pay(amount). The till calls Pay() without needing to know which type the customer used.", "new payment types can be added later.") +
    rw("A game with enemies", "Every enemy has Attack(). A Goblin hits, a Dragon breathes fire. The game loop calls Attack() on each enemy.", "one loop, many behaviours.") +
    rw("Sound on a phone", "Play() works the same for a song, a podcast and a video. Each type plays itself in its own way.", "common name, different behaviour."))

review = (
    req("2 marks", "State", "What is meant by polymorphism?", "Same name, different behaviour.", mks(["Methods with the same name are defined in different classes (derived classes)", "so the same call behaves differently depending on the object"])) +
    req("3 marks", "Explain", "Animal, Parrot and Dog each have a <code>Description()</code> method that gives different text. Explain how this is an example of polymorphism.", "Name the idea and use the example.", mks(["The same method name, Description(), is used in each class", "each class gives its own version", "so calling Description() on an object gives the result for that object's class"])) +
    req("3 marks", "Write", "Write the Python for <code>Cat</code>, a child of <code>Animal</code>, with a <code>Description()</code> that returns the name followed by <code>\" is a cat\"</code>. Assume Animal has <code>GetName()</code>.", "Header with parent, same method name, return with concatenation.", pc('''class Cat(Animal):
    def Description(self):
        return self.GetName() + " is a cat"'''), "Calling the method <code>CatDescription</code> instead of <code>Description</code>.") +
    req("2 marks", "Explain", "Give one advantage of polymorphism.", "Be specific.", mks(["The same code (a loop) can be used for objects of different classes", "so new classes can be added without changing the code that calls the method"])))

tipsl = [("Same name, different behaviour.", "Both halves are needed."), ("Overriding is the how.", "Polymorphism is the result."), ("Use the example.", "Name Description() in Animal, Parrot and Dog when you explain."), ("Say 'depending on the object'.", "The class of the object decides."), ("Don't mix it up.", "Not inheritance, not encapsulation, not containment.")]
sents = [("Define it", "Polymorphism means methods with the same name are redefined in derived classes, so the same call behaves differently depending on the object."), ("Use an example", "Description() is defined in Animal and Parrot, so calling it on a Parrot gives the Parrot's text."), ("Give a benefit", "A loop can call the method on every object without checking its class.")]

finish("ac20r5", "ac-20-1-2-polymorphism", "Polymorphism: One Call, Many Behaviours",
       "What polymorphism means, how it follows from overriding, how one loop handles a list of different objects, and how it looks in Python and exam pseudocode; animations, labs and review questions.",
       learn, watch, explore, practise("cl", "o", "m", "q"), real, review, tipsl, sents, stA + stB + lab)
