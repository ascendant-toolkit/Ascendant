"""20.1.2 extra resource: encapsulation. Run: python3 tools/artifact-kit/mk_ac20r2.py"""
from ac20r import *

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p><b>Encapsulation</b> means two things at once: the <b>attributes and the methods are bundled together in one class</b>, and the <b>data is hidden</b> so it can only be reached through the class's own methods. The attributes are declared <b>private</b>; the methods that other code is allowed to use are <b>public</b>. Outside code has to ask the object, using a getter, rather than reaching in and taking the value. The class can check values on the way in, so the object stays valid. The inside of the class can later change without breaking the code that uses it.</p></div>

  <h2>1 · Private and public</h2>
  ''' + both('''class Pet:
    # PetName : STRING
    # Age : INTEGER
    def __init__(self, NewName, NewAge):
        self.__PetName = NewName    # private
        self.__Age = NewAge         # private

    def GetAge(self):               # public
        return self.__Age
    def SetAge(self, NewAge):       # public
        if NewAge >= 0 and NewAge <= 40:
            self.__Age = NewAge''', '''CLASS Pet
  PRIVATE PetName : STRING
  PRIVATE Age : INTEGER
  PUBLIC PROCEDURE NEW(NewName : STRING, NewAge : INTEGER)
    PetName <- NewName
    Age <- NewAge
  ENDPROCEDURE
  PUBLIC FUNCTION GetAge() RETURNS INTEGER
    RETURN Age
  ENDFUNCTION
  PUBLIC PROCEDURE SetAge(NewAge : INTEGER)
    IF NewAge >= 0 AND NewAge <= 40
      THEN
        Age <- NewAge
    ENDIF
  ENDPROCEDURE
ENDCLASS''') + '''
  <div class="tw"><table class="t">
    <tr><th></th><th>Private</th><th>Public</th></tr>
    <tr><td>Who can use it</td><td>Only code inside the class</td><td>Any code</td></tr>
    <tr><td>Python</td><td>Name starts with two underscores: <code>self.__Age</code></td><td>Ordinary name: <code>GetAge</code></td></tr>
    <tr><td>Pseudocode</td><td><code>PRIVATE</code></td><td><code>PUBLIC</code></td></tr>
    <tr><td>Normally used for</td><td>Attributes</td><td>Methods</td></tr>
  </table></div>

  <h2>2 · Reaching a private attribute</h2>
  <div class="code">''' + pc('''MyPet = Pet("Rex", 3)
print(MyPet.__Age)       # AttributeError: not reachable from outside
print(MyPet.GetAge())    # 3: ask the object through its public method''') + '''</div>
  <p>Python does not lock the attribute: the double underscore renames it behind the scenes. For the exam, treat a double-underscore attribute as private and always go through a method.</p>

  <h2>3 · Why hide the data?</h2>
  <div class="grid2">
    <div class="card"><h3>Protect the data</h3><p>No code can set an age of -5 by accident, because the only way in is <code>SetAge</code>, which checks the value.</p></div>
    <div class="card"><h3>Change the inside safely</h3><p>If Age is later stored as a birth year, only the class changes. Code that calls <code>GetAge()</code> keeps working.</p></div>
    <div class="card"><h3>One place to look</h3><p>Everything that can change a Pet is written in the Pet class, so bugs are easier to find.</p></div>
    <div class="card"><h3>Simple to use</h3><p>The rest of the program only needs to know the public methods, not how the data is stored.</p></div>
  </div>
  <p class="note">Encapsulation is about the <b>data hiding</b>. Getters and setters are the controlled doorway; they have their own page.</p>
'''

watch = '''
  <h2>1 · Reaching in is blocked, asking is allowed</h2><p>Press Play, or click the steps.</p><div id="stA"></div>
  <h2>2 · The setter checks the value</h2><div id="stB"></div>
'''

pet = lambda age: ['__PetName: "Rex"', "__Age: " + age]
stA = stepper("stA", "Direct access against a method call", 760, 235, [
    ("A Pet object holds two private attributes. They are inside the class boundary.", [cls(30, 20, 300, "Pet object (private data)", pet("3"), "f1", 24), txt(30, 150, "outside code", "lbl bd"), txt(30, 175, 'MyPet = Pet("Rex", 3)', "sm", 1)]),
    ("Outside code tries <code>print(MyPet.__Age)</code>. It reaches straight for the attribute.", [cls(30, 20, 300, "Pet object (private data)", pet("3"), "f1", 24), txt(380, 60, "print(MyPet.__Age)", "lbl bd", 1), arr(375, 55, 335, 55, "l"), txt(380, 100, "blocked: AttributeError", "lbl bd t3")]),
    ("Instead it calls the public method <code>GetAge()</code>. The call goes to the object's own code.", [cls(30, 20, 300, "Pet object (private data)", pet("3"), "f1", 24), cls(380, 20, 330, "public methods", ["GetAge()", "SetAge(NewAge)"], "f2", 24), txt(380, 150, "print(MyPet.GetAge())", "lbl bd", 1)]),
    ("The method is inside the class, so it can read <code>self.__Age</code> and return the value.", [cls(30, 20, 300, "Pet object (private data)", pet("3"), "f3", 24), cls(380, 20, 330, "public methods", ["GetAge()", "SetAge(NewAge)"], "f2", 24), arr(375, 90, 335, 90, "l"), txt(380, 150, "returns 3", "lbl bd t3")])])

SA = ["SetAge(5)", "if NewAge >= 0 and NewAge <= 40:", "    self.__Age = NewAge"]
SB = ["SetAge(-5)", "if NewAge >= 0 and NewAge <= 40:", "    self.__Age = NewAge"]
stB = stepper("stB", "SetAge only accepts 0 to 40", 760, 235, [
    ("<code>MyPet.SetAge(5)</code>: the setter checks the value before changing anything.", [code(20, 20, SA, 0, 330, 34), cls(420, 20, 300, "Pet", pet("3"), "f1", 24)]),
    ("5 is between 0 and 40, so the test passes.", [code(20, 20, SA, 1, 330, 34), cls(420, 20, 300, "Pet", pet("3"), "f1", 24), txt(20, 150, "0 <= 5 <= 40: True", "lbl bd t3")]),
    ("The age is stored.", [code(20, 20, SA, 2, 330, 34), cls(420, 20, 300, "Pet", pet("5"), "f3", 24)]),
    ("<code>MyPet.SetAge(-5)</code>: the test fails, so the assignment is skipped.", [code(20, 20, SB, 1, 330, 34), cls(420, 20, 300, "Pet", pet("5"), "f1", 24), txt(20, 150, "0 <= -5 <= 40: False", "lbl bd t3")]),
    ("The age is still 5. The object cannot be put into an invalid state from outside.", [code(20, 20, SB, -1, 330, 34), cls(420, 20, 300, "Pet", pet("5"), "f3", 24)])])

explore = '''
  <h2>Lab 1 · Try to change the age</h2>
  <p>Choose how the class is written, then try to set the age. See what the object ends up holding.</p>
  <div class="card"><div class="btnrow"><button class="b pri" id="nP">Private attribute + checking setter</button><button class="b" id="nU">Public attribute, no hiding</button></div>
    <div class="btnrow"><label>New age <input type="range" id="nR" min="-10" max="60" value="5"> <b id="nV">5</b></label><button class="b pri" id="nGo">Set the age</button></div><div id="nC"></div><div class="verdict" id="nL"></div></div>

  <h2>Lab 2 · Spot the mistake</h2>
  <div class="card"><div id="eB" class="btnrow"></div><div id="eO"></div></div>
'''

lab = r'''
(function () {
  let priv = true, age = 3, msg = "Press Set the age.";
  const paint = () => {
    $("#nP").classList.toggle("pri", priv); $("#nU").classList.toggle("pri", !priv);
    $("#nV").textContent = $("#nR").value;
    $("#nC").innerHTML = codeHTML(priv
      ? ["MyPet.SetAge(" + $("#nR").value + ")", "", "def SetAge(self, NewAge):", "    if NewAge >= 0 and NewAge <= 40:", "        self.__Age = NewAge"]
      : ["MyPet.Age = " + $("#nR").value, "", "# Age is public: any code can set any value"]);
    $("#nL").textContent = "Age is now " + age + ". " + msg;
  };
  const set = () => { const v = +$("#nR").value; if (!priv) { age = v; msg = v < 0 || v > 40 ? "The object now holds an impossible age, and nothing stopped it." : "Accepted."; } else if (v >= 0 && v <= 40) { age = v; msg = "The setter accepted the value."; } else msg = "The setter rejected " + v + ", so the age did not change."; paint(); };
  $("#nP").onclick = () => { priv = true; age = 3; msg = "Press Set the age."; paint(); };
  $("#nU").onclick = () => { priv = false; age = 3; msg = "Press Set the age."; paint(); };
  $("#nR").oninput = paint; $("#nGo").onclick = set; paint();
})();

btnTable("eB", "eO", [
  ["Making the attribute public", "self.Age = NewAge  # then MyPet.Age = -5", "Any code can set an invalid value; the data is not protected", "self.__Age = NewAge, with GetAge and SetAge"],
  ["Printing the private attribute", "print(MyPet.__Age)", "AttributeError from outside the class", "print(MyPet.GetAge())"],
  ["Making methods private", "def __GetAge(self): ...", "Outside code cannot call it, so the doorway is shut", "def GetAge(self): ..."],
  ["Setter with no check", "def SetAge(self, a): self.__Age = a", "Hidden, but anything is accepted, so the hiding achieves little", "Test the value before assigning"],
  ["Confusing it with inheritance", "'Encapsulation is when a child class takes the parent's methods'", "That is inheritance. Encapsulation is bundling and hiding", "Bundle attributes and methods; hide the data"]
], ["Mistake", "Code or answer", "What goes wrong", "Fix"]);
''' + CLASSIFY("cl1", "Should it be private or public?", ["Private", "Public"],
    [("self.__Age", 0), ("def GetAge(self):", 1), ("self.__PetName", 0), ("def SetAge(self, NewAge):", 1), ("The attribute MaxSpeed", 0), ("The method IncreaseSpeed()", 1), ("An attribute holding a patient's treatments", 0), ("A method that returns the patient's ID", 1)],
    "Attributes are normally private; the methods that other code needs are public.") + ORDER(
    "Put these in order: how outside code safely changes a private attribute.",
    ["Outside code calls the public setter", "The setter receives the new value", "The setter checks the value is valid", "If valid, the setter assigns it to the private attribute", "The object now holds the new value"],
    "Call, receive, check, assign, updated.") + MATCH([
    ["Encapsulation", "Bundling attributes and methods in a class and hiding the data"], ["Private", "Can only be used by code inside the class"], ["Public", "Can be used by any code"], ["Data hiding", "Outside code cannot read or change an attribute directly"], ["__Age", "A Python private attribute"], ["PRIVATE", "Pseudocode keyword for a private attribute"]]) + MCQ([
    ("What does encapsulation mean?", ["A child takes the parent's methods", "Bundling attributes and methods together and hiding the data", "Many classes with one method name", "One class containing another"], 1, "Bundle and hide."),
    ("Why are attributes usually private?", ["To make the program faster", "So they can only change through the class's methods", "So they use less memory", "Because Python requires it"], 1, "Protects the data and lets the class check values."),
    ("MyPet.__Age raises an error from outside the class. Why?", ["The pet does not exist", "The attribute is private", "Age is a string", "It needs brackets"], 1, "Private attributes are not accessible directly."),
    ("Which is the best way to read a private attribute?", ["Make it public", "Call a getter method", "Copy the class", "Use print on the class"], 1, "Go through a public method."),
    ("A setter checks the new value. What does this protect?", ["The method name", "The object from holding an invalid value", "The constructor", "The class name"], 1, "Validation keeps the object valid.")], "qz1") + CARDS([
    ("Encapsulation", "Attributes and methods bundled in a class; data hidden behind methods."), ("Private", "Only code inside the class can use it."), ("Public", "Any code can use it."), ("Data hiding", "The data is reached only through the class's methods."),
    ("self.__Name", "Python private attribute."), ("PRIVATE / PUBLIC", "Pseudocode access keywords."), ("Validation in a setter", "Check the value before storing it."), ("Why encapsulate?", "Protect data, change the inside safely, simpler to use.")])

real = RWNOTE + (
    rw("A bank account", "The balance is private. You cannot set it to any figure; you can only call deposit and withdraw, which check the amount.", "private data with checking methods.") +
    rw("A car's speedometer", "You read the speed through the dial. You do not reach into the engine to take the value, and the engine design can change without changing the dial.", "hidden inside, simple public interface.") +
    rw("A game score", "A game keeps the score private so no other part of the program can cheat by setting it directly. Only AddPoints() changes it.", "only the class's methods change the data.") +
    rw("A school record", "A student's grades are private. A getter reports them and a setter checks they are between 0 and 100 before storing.", "validation in a setter."))

review = (
    req("2 marks", "State", "What is meant by encapsulation?", "Say both parts: bundling and hiding.", mks(["Attributes and methods are put together in a class", "the data is hidden (private) so it can only be accessed through the class's methods"]), "Writing only 'hiding data' and missing the bundling.") +
    req("2 marks", "Explain", "A class stores a customer's balance as a private attribute. Explain one benefit of this.", "Give the benefit and say why it is a benefit.", mks(["Other code cannot change the balance directly", "so it cannot be set to an invalid value / only changed through the class's methods"]), "Saying 'it is more secure' without saying what is protected.") +
    req("3 marks", "Complete", "A class diagram shows Pet with Age, a method GetAge and a method SetAge. Which should be PRIVATE and which PUBLIC? Explain.", "Attributes private, methods public.", mks(["Age is PRIVATE", "GetAge and SetAge are PUBLIC", "so outside code reads and changes Age only through the methods"])) +
    req("3 marks", "Write", "Write the Python for a setter <code>SetPages</code> in a class <code>Book</code> that only accepts a value greater than 0.", "Check, then assign.", pc('''def SetPages(self, NewPages):
    if NewPages > 0:
        self.__Pages = NewPages'''), "Assigning first and checking afterwards."))

tipsl = [("Two parts.", "Bundling attributes and methods, and hiding the data. Say both."), ("Attributes private, methods public.", "Unless the question says otherwise."), ("Name the benefit.", "Protects the data, allows validation, lets the inside change."), ("Never print a private attribute.", "Call its getter."), ("Don't confuse the three.", "Encapsulation hides, inheritance reuses, polymorphism gives one name many behaviours.")]
sents = [("Define it", "Encapsulation puts the attributes and methods in one class and hides the data, so it is only accessed through the methods."), ("Give a benefit", "The data cannot be changed to an invalid value because it can only be changed through the setter, which validates it."), ("Describe access", "The attribute is private, so another class has to call the public getter to read it.")]

finish("ac20r2", "ac-20-1-2-encapsulation", "Encapsulation: Hiding the Data",
       "What encapsulation means, private and public in Python and pseudocode, how outside code gets at hidden data, and why hiding it is useful; animations, labs and review questions.",
       learn, watch, explore, practise("cl", "o", "m", "q"), real, review, tipsl, sents, stA + stB + lab)
