"""A Level CS syllabus 20.1.3: object-oriented programming in code (Python). Run: python3 tools/artifact-kit/mk_ac2013.py"""
from ak20 import *

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>Paper 4 asks you to write the classes you designed as <b>Python program code</b>: a class with private attributes and a constructor, its <b>getters and setters</b>, a method that does a calculation, then a <b>child class</b> that inherits from it and <b>overrides</b> a method. In Python a class is declared with <code>class</code>, the constructor is <code>__init__(self, ...)</code>, and an attribute is private when its name starts with two underscores. A child class is declared with the parent in brackets and calls the parent's constructor so the inherited attributes are set. Objects are created by calling the class like a function, and objects can hold other objects (containment). The mark schemes reward the same moves every time, so learn the pattern.</p></div>

  <h2>1 · A class in Python</h2>
  <p>Python does not declare attributes. They are created when the constructor assigns them, so the exam asks you to <b>include attribute declarations using comments</b> to show the name and data type. Double underscores make an attribute private.</p>
  <div class="code">''' + pc('''class Pet:
    # PetName : STRING
    # YearBorn : INTEGER
    def __init__(self, NewName, NewYear):
        self.__PetName = NewName        # private attribute
        self.__YearBorn = NewYear

    def GetPetName(self):               # getter: no parameter, returns the value
        return self.__PetName

    def SetYearBorn(self, NewYear):     # setter: takes the new value
        self.__YearBorn = NewYear

MyPet = Pet("Rex", 2021)                # creates an object by calling the class
print(MyPet.GetPetName())               # Rex''') + '''</div>
  <ul>
    <li><b><code>self</code></b> is the object the method is running on. It is the first parameter of every method, and every attribute is <code>self.Name</code>. You do not pass it when you call: <code>MyPet.GetPetName()</code>.</li>
    <li><b><code>__init__</code></b> is the constructor. It takes the starting values as parameters and assigns them to the attributes.</li>
    <li>A <b>private</b> attribute (<code>self.__PetName</code>) cannot be reached from outside the class as <code>MyPet.__PetName</code>; use the getter.</li>
    <li>Parameter names should differ from attribute names (<code>NewName</code>, not <code>PetName</code>) so it is clear which is which.</li>
  </ul>

  <h2>2 · Getters and setters</h2>
  <p>A <b>getter</b> returns a private attribute and takes no parameter. A <b>setter</b> assigns a parameter to the attribute and returns nothing. A setter can check the value first.</p>
  <div class="code">''' + pc('''def GetHorizontalPosition(self):
    return self.__HorizontalPosition

def SetCurrentSpeed(self, CSP):
    self.__CurrentSpeed = CSP

def SetPriority(self, Urgency):
    if Urgency >= 1 and Urgency <= 5:       # validate before storing
        self.__Priority = Urgency''') + '''</div>
  <p>Write one getter for each attribute that must be readable and one setter for each that may change. Do not return from a setter, and do not print in a getter.</p>

  <h2>3 · A method that does work</h2>
  <p>The long Paper 4 questions add a method that changes the object's state with a limit, such as a speed that cannot exceed a maximum. Read the bullets and turn each into a line.</p>
  <div class="code">''' + pc('''def IncreaseSpeed(self):
    self.__CurrentSpeed = self.__CurrentSpeed + self.__IncreaseAmount
    if self.__CurrentSpeed > self.__MaxSpeed:          # cannot exceed the maximum
        self.__CurrentSpeed = self.__MaxSpeed
    self.__HorizontalPosition = self.__HorizontalPosition + self.__CurrentSpeed   # in all cases''') + '''</div>
  <p>The mark scheme gives separate marks for: adding the increase, checking the limit and limiting the speed, and adding the <i>updated</i> speed to the position <b>in every case</b>, not only when the limit is reached.</p>

  <h2>4 · Inheritance in Python</h2>
  <p>Put the parent in brackets. In the child's constructor, call the parent's constructor so the inherited attributes are set, then set the child's own attributes.</p>
  <div class="code">''' + pc('''class Animal:
    def __init__(self, pName, pSound):
        self.Name = pName
        self.Sound = pSound

class Parrot(Animal):                       # Parrot inherits from Animal
    # WingSpan : INTEGER
    def __init__(self, pName, pSound, pWingSpan):
        super().__init__(pName, pSound)     # parent constructor sets Name and Sound
        self.WingSpan = pWingSpan
        self.NumberWords = 0

    def ChangeNumberWords(self, Change):    # a method only Parrots have
        self.NumberWords = self.NumberWords + Change''') + '''</div>
  <p><code>Animal.__init__(self, pName, pSound)</code> does the same as <code>super().__init__(pName, pSound)</code>; both are accepted. A child does not repeat the parent's attributes or methods.</p>
  <div class="warn"><b class="h">Private and inheritance</b>A double-underscore attribute in the parent is not directly visible in the child class. To change it from the child, call the parent's methods (its setters, or its own method) instead of using <code>self.__Attribute</code>.</div>

  <h2>5 · Overriding and polymorphism</h2>
  <p>A child that defines a method with the <b>same name</b> as the parent's <b>overrides</b> it: Python looks in the child's class first. The parent's version can still be used with <code>super()</code>.</p>
  <div class="code">''' + pc('''class Animal:
    def Description(self):
        return "The animal's name is " + self.Name

class Parrot(Animal):
    def Description(self):                   # overrides Animal.Description
        return super().Description() + ". It can say " + str(self.NumberWords) + " words."

Zoo = [Animal("Teddy"), Parrot("Chewie")]
for A in Zoo:
    print(A.Description())                   # each object runs its own version: polymorphism''') + '''</div>

  <h2>6 · Containment: objects inside objects</h2>
  <p>An attribute can be another object, or an array of objects. A Hand holding five Cards creates the Cards first and passes them to the Hand's constructor. The getter returns the object at a position.</p>
  <div class="code">''' + pc('''class Hand:
    # Cards : ARRAY[0:9] OF Card
    # FirstCard : INTEGER
    # NumberCards : INTEGER
    def __init__(self, Card1, Card2, Card3, Card4, Card5):
        self.__Cards = []
        self.__Cards.append(Card1)
        self.__Cards.append(Card2)
        self.__Cards.append(Card3)
        self.__Cards.append(Card4)
        self.__Cards.append(Card5)
        self.__FirstCard = 0
        self.__NumberCards = 5

    def GetCard(self, Position):
        return self.__Cards[Position]''') + '''</div>

  <h2>7 · The pattern of a Paper 4 OOP question</h2>
  <div class="tw"><table class="t">
    <tr><th>Part</th><th>What it asks</th><th>Marks come from</th></tr>
    <tr><td>(a)(i) Declare the class</td><td>Class, private attributes with types, constructor with parameters</td><td>class header; attributes (comments in Python); constructor header taking the right number of parameters; every parameter assigned</td></tr>
    <tr><td>(a)(ii) Getters</td><td>A method for each value to return</td><td>header with no parameter and returns the attribute, for each getter</td></tr>
    <tr><td>(a)(iii) Setters</td><td>A method for each value to change</td><td>header taking a parameter; assigns it to the attribute</td></tr>
    <tr><td>(a)(iv) A method</td><td>A calculation with a limit or condition</td><td>one mark per bullet in the question</td></tr>
    <tr><td>(b) Child class</td><td>Inherits, new attributes, own constructor, overrides a method</td><td>class header with the parent; parent constructor called; new attributes assigned; override uses the same name</td></tr>
  </table></div>

  <h2>8 · Common ways to lose marks</h2>
  <ul>
    <li>Forgetting <code>self</code> in a method header or in front of an attribute.</li>
    <li>Not calling the parent constructor, so the inherited attributes are never set.</li>
    <li>A constructor with too few parameters: it must take every value the question says is passed in.</li>
    <li>Returning in a setter or printing in a getter.</li>
    <li>Writing <code>MaxSpeed</code> instead of <code>self.__MaxSpeed</code> inside a method.</li>
    <li>Concatenating a number to a string without <code>str()</code>.</li>
    <li>Not shortening the "Description" string exactly as the format in the question, including spaces and units.</li>
    <li>Leaving out the attribute-declaration comments when the question asks for them.</li>
  </ul>
'''

watch = '''
  <h2>1 · Creating an object</h2>
  <p>Press Play, or click the steps.</p>
  <div id="stA"></div>
  <h2>2 · A child class and the parent constructor</h2>
  <div id="stB"></div>
  <h2>3 · Which method runs? Overriding</h2>
  <div id="stC"></div>
  <h2>4 · A method with a limit: IncreaseSpeed</h2>
  <p>A vehicle has MaxSpeed 100 and IncreaseAmount 40. The speed is limited; the position always grows.</p>
  <div id="stD"></div>
'''

explore = '''
  <h2>Lab 1 · Run IncreaseSpeed</h2>
  <p>Set the vehicle's maximum speed and increase amount, then call <code>IncreaseSpeed()</code> repeatedly. For a helicopter, also set the vertical change and maximum height.</p>
  <div class="card"><div id="lM"></div><div id="lI"></div><div class="btnrow"><button class="b" id="lH">Helicopter: off</button></div><div id="lV"></div><div id="lX"></div>
    <div class="btnrow"><button class="b pri" id="lGo">Call IncreaseSpeed()</button><button class="b" id="lRe">New object</button></div>
    <div id="lT"></div><div class="verdict" id="lv"></div></div>

  <h2>Lab 2 · Build the Python class</h2>
  <p>Pick a scenario and choose which getters and setters to include. The code is written the way a mark scheme expects it.</p>
  <div class="card"><div id="gB" class="btnrow"></div><div id="gC"></div><div id="gO"></div></div>

  <h2>Lab 3 · Spot the mistake</h2>
  <div class="card"><div id="eB" class="btnrow"></div><div id="eO"></div></div>
'''

practise = '''
  <h2>1 · What is this line of Python doing?</h2><div id="cl1" class="card"></div>
  <h2>2 · Put the steps for writing a child class in order</h2><div id="o1" class="card"></div>
  <h2>3 · Match the Python to its meaning</h2><div id="m1" class="card"></div>
  <h2>4 · Trace the object</h2><div id="c1"></div>
  <h2>5 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("A game with different characters", "Every character has a position and moves with a method. A bike character moves faster and a magic character has spells. They inherit the position and Move() from Character and override what is different.", "inheritance with overriding: write the common part once.") +
rw("Cards, hands and a deck", "A Hand holds Card objects and asks them for their number and colour through getters. The Hand never needs to know how a Card stores its data.", "containment and getters: objects work together through their methods.") +
rw("A medical appointment system", "Appointment objects are created with the patient, doctor and date. Treatments and medications are added later with setters, and reports read them with getters.", "constructor to create, setters to update, getters to report.") +
rw("A linked list or a tree", "A Node class holds the data and a pointer, and a LinkedList or Tree class holds the nodes. Many Paper 4 data structure questions are written as classes.", "the same class skills apply to data structures: Node, LinkedList, Tree.") +
rw("A zoo of animals", "A list of Animal, Parrot and Dog objects can all be asked for a Description(). Each prints its own version without the code checking which kind it is.", "polymorphism: the loop calls one method name and each object responds in its own way.")
)

where = [
  ("M/J 2023", "41, 43", "2(a), 2(b)", "5 + 3 + 3 + 3 + 5 + 4", "Vehicle class, getters, setters, IncreaseSpeed(); child class Helicopter with an overridden method"),
  ("O/N 2022", "41, 43", "2(a), 2(b)", "5 + 3 + 6 + 2", "Card class with getters; Hand class that contains five Cards"),
  ("O/N 2022", "42", "2(a), 2(b), 2(c)", "4 + 3 + 2", "Character class, three getters, ChangePosition()"),
  ("M/J 2025", "42", "3(a), 3(b)", "4 + 3 + 4 + 2", "Animal class and Description(); child class Parrot with an overridden Description()")]

past = '''  <p class="note">Writing classes as program code is tested in Paper 4 and appears in every Paper 4 from May/June 2021 to Oct/Nov 2025, as the second or third question: class declarations such as TreasureChest, Balloon, Card, Picture, Character, Tree, Node, Horse, Train, Bird and BoardObject, several with a child class. The four below show the skills at full length. Past paper mark schemes list Python, VB.NET and Java; only Python is shown here. Questions are reworded from the papers; check the original paper and mark scheme for the exact wording.</p>

  <h3>Vehicle and Helicopter: a class, its methods and a child class</h3>
''' + peq(SRC("s23", "41, 43", "Q2(a)"), "5 + 3 + 3 + 3 marks", "Write",
  "A computer game includes different vehicles. The class Vehicle is written with OOP." + qcode('''Vehicle
ID : STRING                   stores the identification name
MaxSpeed : INTEGER            stores the maximum speed
CurrentSpeed : INTEGER        stores the current speed
IncreaseAmount : INTEGER      stores the amount CurrentSpeed increases by
HorizontalPosition : INTEGER  stores the horizontal position
Constructor()                 initialises ID, MaxSpeed and IncreaseAmount to the
                              parameter values; initialises CurrentSpeed and
                              HorizontalPosition to 0
GetCurrentSpeed()             returns the current speed
GetIncreaseAmount()           returns the increase amount
GetMaxSpeed()                 returns the maximum speed
GetHorizontalPosition()       returns the horizontal position
SetCurrentSpeed()             assigns the parameter to the current speed
SetHorizontalPosition()       assigns the parameter to the horizontal position
IncreaseSpeed()               calculates and stores the new speed and horizontal
                              position of the vehicle''') + "(i) Write program code to declare the class Vehicle and its constructor. All attributes must be private. If you are writing in Python, include attribute declarations using comments. (ii) Write program code for the get methods GetCurrentSpeed(), GetIncreaseAmount(), GetMaxSpeed() and GetHorizontalPosition(). (iii) Write program code for the set methods SetCurrentSpeed() and SetHorizontalPosition(). (iv) The method IncreaseSpeed() adds IncreaseAmount to the current speed, then adds the updated current speed to the horizontal position. The current speed of a vehicle cannot exceed its maximum speed. Write program code for IncreaseSpeed().",
  "Five attributes with comments, a constructor taking ID, MaxSpeed and IncreaseAmount (three parameters), and the two starting values set to 0. In (iv) the position is added in every case, after the speed is limited.",
  "<p><b>(i)</b> Five marks: " + mks(["class header", "five private attribute declarations with data types", "constructor header taking at least three parameters", "assigning ID, MaxSpeed and IncreaseAmount to the parameters", "assigning CurrentSpeed and HorizontalPosition to 0"]) + "</p>" + pc('''class Vehicle:
    # self.__ID : STRING
    # self.__MaxSpeed : INTEGER
    # self.__CurrentSpeed : INTEGER
    # self.__IncreaseAmount : INTEGER
    # self.__HorizontalPosition : INTEGER
    def __init__(self, IDP, MaxSpeedP, IncreaseAmountP):
        self.__ID = IDP
        self.__MaxSpeed = MaxSpeedP
        self.__IncreaseAmount = IncreaseAmountP
        self.__CurrentSpeed = 0
        self.__HorizontalPosition = 0''') + "<p><b>(ii)</b> Three marks: " + mks(["one get method with no parameter", "that returns the attribute without overwriting it", "three further correct get methods"], "a") + "</p>" + pc('''    def GetCurrentSpeed(self):
        return self.__CurrentSpeed

    def GetIncreaseAmount(self):
        return self.__IncreaseAmount

    def GetMaxSpeed(self):
        return self.__MaxSpeed

    def GetHorizontalPosition(self):
        return self.__HorizontalPosition''', 11) + "<p><b>(iii)</b> Three marks: " + mks(["a set method taking a parameter", "that assigns the parameter to the attribute", "the second correct set method"], "a") + "</p>" + pc('''    def SetCurrentSpeed(self, CSP):
        self.__CurrentSpeed = CSP

    def SetHorizontalPosition(self, HPP):
        self.__HorizontalPosition = HPP''', 22) + "<p><b>(iv)</b> Three marks: " + mks(["method header with no parameter, adding IncreaseAmount to CurrentSpeed", "checking if MaxSpeed is exceeded and limiting the speed to it", "adding the updated CurrentSpeed to HorizontalPosition in all cases"]) + "</p>" + pc('''    def IncreaseSpeed(self):
        self.__CurrentSpeed = self.__CurrentSpeed + self.__IncreaseAmount
        if self.__CurrentSpeed > self.__MaxSpeed:
            self.__CurrentSpeed = self.__MaxSpeed
        self.__HorizontalPosition = self.__HorizontalPosition + self.__CurrentSpeed''', 28),
  "Putting the position update inside the <code>if</code>, so it only happens when the speed is capped. Also forgetting <code>self.</code> in front of an attribute.") + peq(SRC("s23", "41, 43", "Q2(b)"), "5 + 4 marks", "Write",
  "The child class Helicopter inherits from the parent class Vehicle. A helicopter also has a vertical position and changes it when it increases speed." + qcode('''Helicopter
VerticalPosition : INTEGER   stores the vertical position
VerticalChange : INTEGER     stores the amount VerticalPosition changes by
MaxHeight : INTEGER          stores the maximum height the helicopter can reach
Constructor()                takes the ID, maximum speed, increase amount, vertical
                             change and maximum height as parameters;
                             initialises the vertical position to 0
GetVerticalPosition()        returns the vertical position
IncreaseSpeed()              changes the current speed, horizontal and vertical
                             position of the helicopter''') + "(i) Write program code to declare the class Helicopter and its constructor. All attributes must be private. If you are writing in Python, include attribute declarations using comments. (ii) The Helicopter method IncreaseSpeed() overrides the method from the parent class and: adds the amount of vertical change to the vertical position; adds IncreaseAmount to the current speed; adds the updated current speed to the horizontal position. The vertical position cannot exceed the maximum height. The current speed cannot exceed the maximum speed. Write program code for IncreaseSpeed().",
  "(i) Inherit from Vehicle, set only the three new attributes, and pass the other values up to the parent constructor. (ii) The parent already does the speed and horizontal position, so reuse it.",
  "<p><b>(i)</b> Five marks: " + mks(["class header inheriting from Vehicle", "three private attribute declarations with data types", "constructor with at least five parameters", "calling the parent constructor with the right parameters", "initialising VerticalPosition to 0 and assigning VerticalChange and MaxHeight"]) + "</p>" + pc('''class Helicopter(Vehicle):
    # self.__VerticalPosition : INTEGER
    # self.__VerticalChange : INTEGER
    # self.__MaxHeight : INTEGER
    def __init__(self, IDP, MaxSpeedP, IncreaseAmountP, VertChangeP, MaxHeightP):
        Vehicle.__init__(self, IDP, MaxSpeedP, IncreaseAmountP)
        self.__VerticalPosition = 0
        self.__VerticalChange = VertChangeP
        self.__MaxHeight = MaxHeightP''') + "<p><b>(ii)</b> Up to four marks: " + mks(["method header (overriding) with no parameter", "adding the vertical change to the vertical position", "limiting it to the maximum height", "repeating or calling the parent's code for the horizontal increase, in every case"], "a") + "</p>" + pc('''    def IncreaseSpeed(self):
        self.__VerticalPosition = self.__VerticalPosition + self.__VerticalChange
        if self.__VerticalPosition > self.__MaxHeight:
            self.__VerticalPosition = self.__MaxHeight
        Vehicle.IncreaseSpeed(self)      # speed, limit and horizontal position as before''', 10),
  "Writing the Helicopter attributes as part of Vehicle, or copying all the Vehicle code into Helicopter. Inherit and call the parent's constructor and method.") + '''
  <h3>Card and Hand: containment</h3>
''' + peq(SRC("w22", "41, 43", "Q2"), "5 + 3 + 6 + 2 marks", "Write",
  "A program uses a set of cards and is written with OOP. It has two classes, Card and Hand." + qcode('''Card
Number : INTEGER    stores the card number from 1 to 5 inclusive
Colour : STRING     stores the card colour: red, blue or yellow
Constructor()       takes a number and colour as parameters and sets the
                    private values to these parameters
GetNumber()         returns the card number
GetColour()         returns the card colour

Hand
Cards : ARRAY[0:9] OF Card   1D array of type Card
FirstCard : INTEGER          position of the first card in the hand
NumberCards : INTEGER        number of cards in the hand
Constructor()                takes five card objects as parameters, assigns each
                             card to the array Cards[], initialises FirstCard to 0
                             and NumberCards to 5
GetCard()                    takes an index as a parameter and returns the card at
                             that index in the array''') + "(a)(i) Write program code to declare the class Card, its attributes and constructor. All attributes must be private. In Python, include attribute declarations using comments. (ii) Write program code for the class methods GetNumber() and GetColour(). (b)(i) Write program code to declare the class Hand, its attributes and constructor. (ii) Write program code for the method GetCard().",
  "Card is a plain class. Hand's constructor takes five Card objects and puts them in the array. The array is a private attribute and GetCard() returns the object at the index.",
  "<p><b>(a)(i)</b> Five marks: " + mks(["class Card declaration", "private attributes: Number as integer, Colour as string", "constructor header", "taking two parameters", "assigning the parameters to the attributes"]) + "</p>" + pc('''class Card:
    # Number : INTEGER
    # Colour : STRING
    def __init__(self, Number1, Colour1):
        self.__Number = Number1
        self.__Colour = Colour1''') + "<p><b>(a)(ii)</b> Three marks: " + mks(["one get method, no parameters", "returning the value", "the second correct get method"], "a") + "</p>" + pc('''    def GetNumber(self):
        return self.__Number

    def GetColour(self):
        return self.__Colour''', 6) + "<p><b>(b)(i)</b> Six marks: " + mks(["class Hand declaration", "private FirstCard and NumberCards as integers", "private array Cards of type Card with 10 elements", "constructor with five Card objects as parameters", "assigning each Card parameter to the array", "initialising FirstCard to 0 and NumberCards to 5"]) + "</p>" + pc('''class Hand:
    # Cards : ARRAY[0:9] OF Card
    # FirstCard : INTEGER
    # NumberCards : INTEGER
    def __init__(self, Card1, Card2, Card3, Card4, Card5):
        self.__Cards = []
        self.__Cards.append(Card1)
        self.__Cards.append(Card2)
        self.__Cards.append(Card3)
        self.__Cards.append(Card4)
        self.__Cards.append(Card5)
        self.__FirstCard = 0
        self.__NumberCards = 5''') + "<p><b>(b)(ii)</b> Two marks: " + mks(["GetCard() header taking an integer parameter", "returning the card at the parameter index in the array"], "a") + "</p>" + pc('''    def GetCard(self, Position):
        return self.__Cards[Position]''', 11),
  "Storing five separate attributes instead of one array, or making GetCard() print the card instead of returning it.") + '''
  <h3>Character: a class and its methods</h3>
''' + peq(SRC("w22", "42", "Q2"), "4 + 3 + 2 marks", "Write",
  "A computer game has characters." + qcode('''Character
Name : STRING         stores the name of the character
XCoordinate : INTEGER stores the x coordinate
YCoordinate : INTEGER stores the y coordinate
Constructor()         initialises Name, XCoordinate and YCoordinate from the
                      values passed as parameters
GetName()             returns the name of the character
GetX()                returns the x coordinate of the character
GetY()                returns the y coordinate of the character
ChangePosition()      takes XChange as an integer parameter and adds it to the
                      x coordinate; takes YChange as an integer parameter and
                      adds it to the y coordinate''') + "(a) Write program code to declare the class Character and its constructor. All attributes must be private. In Python, include attribute declarations using comments. (b) Write program code for the three get methods. (c) Write program code for the method ChangePosition().",
  "Three attributes, a constructor with three parameters, three getters, and a method that adds to the stored values (not replaces).",
  "<p><b>(a)</b> Four marks: " + mks(["class declaration for Character", "three private attributes with data types", "constructor taking three parameters", "assigning the parameters to all three attributes"]) + "</p>" + pc('''class Character:
    # Name : STRING
    # XCoordinate : INTEGER
    # YCoordinate : INTEGER
    def __init__(self, Namep, Xcoord, Ycoord):
        self.__Name = Namep
        self.__XCoordinate = Xcoord
        self.__YCoordinate = Ycoord''') + "<p><b>(b)</b> Three marks: " + mks(["a get method header with no parameters", "returning the correct value", "the second and third get methods correct"], "a") + "</p>" + pc('''    def GetName(self):
        return self.__Name

    def GetX(self):
        return self.__XCoordinate

    def GetY(self):
        return self.__YCoordinate''', 8) + "<p><b>(c)</b> Two marks: " + mks(["method header taking two integer parameters", "adding both parameters to the existing x and y values"]) + "</p>" + pc('''    def ChangePosition(self, XChange, YChange):
        self.__XCoordinate = self.__XCoordinate + XChange
        self.__YCoordinate = self.__YCoordinate + YChange''', 17),
  "Assigning the parameter instead of adding it, so the character jumps to the new value instead of moving by it.") + '''
  <h3>Animal and Parrot: overriding a method</h3>
''' + peq(SRC("s25", "42", "Q3"), "4 + 3 + 4 + 2 marks", "Write",
  "A program stores data about animals using OOP." + qcode('''Animal
Name : String          stores the name of the animal
Sound : String         stores the sound the animal makes
Size : Integer         size, 1 (smallest) to 10 (largest)
Intelligence : Integer intelligence, 1 (least) to 10 (most)
Constructor()          initialises all attributes to its parameter values
Description()          returns a string message that contains the data from
                       the attributes

Parrot (inherits from Animal; overrides Description())
WingSpan : Integer     the width of the wings to the nearest cm
NumberWords : Integer  the number of words the parrot can speak
Constructor()          calls the parent constructor using its parameter values;
                       initialises WingSpan and NumberWords to its parameters
ChangeNumberWords()    takes an integer parameter and adds it to the number
                       currently in NumberWords''') + "(a)(i) Write program code to declare the class Animal and its constructor. (ii) Description() returns a string in the format: <i>The animal's name is Teddy, it makes a Bark, its size is 4 and its intelligence level is 6</i>. Write program code for Description(). (b)(i) Write program code to declare the class Parrot, its constructor and the method ChangeNumberWords(). (ii) Description() in Parrot returns the same message followed by: <i>. It has a wingspan of 30cm and can say 29 words.</i> Write program code for Description().",
  "Four parameters, four attributes. The strings must match the format exactly and the integers need str(). The child calls the parent constructor with four values, then sets its own two.",
  "<p><b>(a)(i)</b> Four marks: " + mks(["class header", "four attributes with appropriate data types", "constructor header taking at least four parameters", "assigning each parameter to its attribute"]) + "</p>" + pc('''class Animal:
    def __init__(self, pName, pSound, pSize, pIntelligence):
        self.Name = pName                 # string
        self.Sound = pSound               # string
        self.Size = pSize                 # integer
        self.Intelligence = pIntelligence # integer''') + "<p><b>(a)(ii)</b> Three marks: " + mks(["Description() header with no parameter", "concatenating the attributes with the given message", "returning the created message"], "a") + "</p>" + pc('''    def Description(self):
        Message = ("The animal's name is " + self.Name + ", it makes a " + self.Sound +
                   ", its size is " + str(self.Size) + " and its intelligence level is " +
                   str(self.Intelligence))
        return Message''', 6) + "<p><b>(b)(i)</b> Four marks: " + mks(["class header inheriting from Animal", "constructor taking six parameters and calling the parent constructor with four", "WingSpan and NumberWords defined and assigned", "ChangeNumberWords() taking a parameter and adding it to NumberWords"]) + "</p>" + pc('''class Parrot(Animal):
    def __init__(self, pName, pSound, pSize, pIntelligence, pWingSpan, pNumberWords):
        super().__init__(pName, pSound, pSize, pIntelligence)
        self.WingSpan = pWingSpan         # integer
        self.NumberWords = pNumberWords   # integer

    def ChangeNumberWords(self, Change):
        self.NumberWords = self.NumberWords + Change''') + "<p><b>(b)(ii)</b> Two marks: " + mks(["Description() header, no parameters, overriding the parent method", "concatenating and returning the correct string"], "a") + "</p>" + pc('''    def Description(self):
        Message = (super().Description() + ". It has a wingspan of " +
                   str(self.WingSpan) + "cm and can say " + str(self.NumberWords) + " words.")
        return Message''', 8),
  "Forgetting <code>str()</code> around the integer attributes, which causes a type error when joining text and numbers.")

review = req("3 marks", "Write", "A class Book stores a Title (STRING) and Pages (INTEGER), both private. The constructor takes both values. Write the class in Python, with a getter for each attribute.", "Class header, constructor with two parameters, two getters.",
  "<p>" + mks(["class header and the attribute comments", "constructor taking two parameters and assigning both to private attributes", "two getters, each with no parameter, returning the attribute"]) + "</p>" + pc('''class Book:
    # Title : STRING
    # Pages : INTEGER
    def __init__(self, NewTitle, NewPages):
        self.__Title = NewTitle
        self.__Pages = NewPages

    def GetTitle(self):
        return self.__Title

    def GetPages(self):
        return self.__Pages'''), "Naming the parameters the same as the attributes without <code>self.</code>, so nothing is stored.") + req("2 marks", "Write", "Add a setter SetPages() to the Book class that only accepts a positive number of pages.", "A setter that checks before it stores.",
  "<p>" + mks(["method header taking a parameter", "stores the parameter only if it is greater than 0"]) + "</p>" + pc('''    def SetPages(self, NewPages):
        if NewPages > 0:
            self.__Pages = NewPages'''), None) + req("4 marks", "Write", "EBook inherits from Book and adds a private attribute SizeMB (INTEGER). Write the class and its constructor, which takes the title, the number of pages and the size.", "Parent in brackets, parent constructor, own attribute.",
  "<p>" + mks(["class header with Book as the parent", "constructor taking three parameters", "calling the parent constructor with the title and pages", "assigning SizeMB to a private attribute"]) + "</p>" + pc('''class EBook(Book):
    # SizeMB : INTEGER
    def __init__(self, NewTitle, NewPages, NewSize):
        super().__init__(NewTitle, NewPages)
        self.__SizeMB = NewSize'''), "Calling <code>Book.__init__(NewTitle)</code> with too few arguments, or not calling it at all.") + req("2 marks", "Write", "Write the statements to create an EBook called MyBook with the title \"Algorithms\", 320 pages and 5 MB, and output its title.", "Create with the class name, then use a getter.",
  "<p>" + mks(["MyBook = EBook(\"Algorithms\", 320, 5)", "print(MyBook.GetTitle())"]) + "</p>" + pc('''MyBook = EBook("Algorithms", 320, 5)
print(MyBook.GetTitle())'''), "Writing <code>MyBook.__Title</code>: a private attribute cannot be reached directly.") + req("3 marks", "Write", "Shape has a method Area() that returns 0. Circle inherits from Shape, has a private Radius set by its constructor, and overrides Area() to return 3.14 × Radius × Radius. Write both classes.", "Override by using the same name in the child.",
  "<p>" + mks(["Shape with Area() returning 0", "Circle inheriting from Shape with a constructor setting Radius", "Circle.Area() with the same name returning the calculation"]) + "</p>" + pc('''class Shape:
    def Area(self):
        return 0

class Circle(Shape):
    # Radius : REAL
    def __init__(self, NewRadius):
        self.__Radius = NewRadius

    def Area(self):
        return 3.14 * self.__Radius * self.__Radius'''), None)

exam = exam20("Part 1 is real 9618 questions where classes are written as program code (Paper 4), 2022 to 2025. Part 2 is a set of review questions for practice; they are not in exam format.", where, past, review)

tips = tips_html([
  ("Start every method with self.", "def GetName(self): and self.__Name inside. A missing self is the commonest slip."),
  ("Copy the attribute names exactly.", "The question gives the names. Use them with the same spelling and data type in the comments."),
  ("Count the constructor parameters.", "Every value the question says is passed in is a parameter; the others are set to 0 or empty."),
  ("Getters return, setters assign.", "No printing in a getter and no return in a setter."),
  ("Child classes: parent first.", "Put the parent in brackets, call its constructor, then set only the new attributes."),
  ("Join text and numbers with str().", "Description() questions are mostly string concatenation. Match the format, spaces and units."),
  ("Use the bullets as a checklist.", "Each bullet in a method description is a mark: one line of code for each."),
], [
  ("create an object", "MyPet = Pet(\"Rex\", 2021) calls the constructor and returns a new object."),
  ("call the parent constructor", "super().__init__(pName, pSound) sets the inherited attributes."),
  ("override a method", "The child defines a method with the same name as the parent's, so the child's version runs."),
  ("make an attribute private", "Start its name with two underscores: self.__Name."),
], [("Write program code", "Produce working Python in the form the question describes."), ("Declare the class", "Class header, attributes (comments), constructor."), ("Rewrite", "Same job in a new form; here, often iterative into recursive or a class into methods."), ("Test your program", "Run it and show the output, which you copy into the evidence document.")]) + FC

js = AKJS + AK20JS + r'''
function classBox(x, y, w, title, rows, v = 1, cls = "f1", lh = 20) {
  const h = 30 + rows.length * lh + 8;
  let o = SV.rect(x, y, w, h, "cell", { rx: 6, ...op(v) }) + SV.rect(x, y, w, 28, cls, { rx: 6, ...op(v * 0.6) }) + SV.text(x + w / 2, y + 19, title, "lbl bd", { "text-anchor": "middle", style: "font-size:15px", ...op(v) });
  rows.forEach((r, i) => { o += SV.text(x + 8, y + 46 + i * lh, r, "sm", { style: "font-family:var(--mono);font-size:11.5px", ...op(v) }); });
  return o;
}

(function () {
  const L = ["MyPet = Pet(\"Rex\", 2021)", "", "def __init__(self, NewName, NewYear):", "    self.__PetName = NewName", "    self.__YearBorn = NewYear"];
  const draw = (s) => {
    const k = Math.round(s.i); let o = codeList(20, 20, [L[0], L[2], L[3], L[4]], k === 0 ? 0 : k === 1 ? 1 : k === 2 ? 2 : k === 3 ? 3 : -1, 1, 34, 350);
    if (k >= 1) o += classBox(420, 20, 300, k >= 5 ? "object stored in MyPet" : "self (a new, empty object)", ["__PetName: " + (k >= 3 ? "\"Rex\"" : "?"), "__YearBorn: " + (k >= 4 ? "2021" : "?")], 1, k >= 5 ? "f3" : "f1", 24);
    if (k >= 2) o += SV.text(20, 175, "parameters: NewName = \"Rex\", NewYear = 2021", "sm", { style: "font-family:var(--mono)" });
    if (k >= 5) o += SV.text(420, 165, "MyPet now refers to the object", "lbl bd t3");
    return o;
  };
  Lib.stepper($("#stA"), { w: 760, h: 200, label: "Creating an object from a class", base: { i: 0 }, draw, tween: 450, dwell: 3600, steps: [
    { cap: "The statement <code>Pet(\"Rex\", 2021)</code> calls the class like a function. Python makes a new, empty object.", s: { i: 0 } },
    { cap: "It runs <code>__init__</code> on the new object. Inside, the object is called <b>self</b>.", s: { i: 1 } },
    { cap: "The arguments become the parameters <code>NewName</code> and <code>NewYear</code>.", s: { i: 2 } },
    { cap: "<code>self.__PetName = NewName</code> creates the first private attribute on the object.", s: { i: 3 } },
    { cap: "<code>self.__YearBorn = NewYear</code> creates the second. The constructor has finished.", s: { i: 4 } },
    { cap: "The finished object is stored in <code>MyPet</code>. Each time the class is called a separate object is made.", s: { i: 5 } }] });
})();

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); let o = "";
    o += classBox(20, 20, 300, "Parrot.__init__ (child)", ["super().__init__(...)  # call parent", "self.WingSpan = pWingSpan", "self.NumberWords = pNumberWords"], 1, k === 1 || k === 4 ? "f3" : "f1", 20);
    if (k >= 2 && k <= 2) o += classBox(20, 140, 300, "Animal.__init__ (parent)", ["self.Name = pName", "self.Sound = pSound", "self.Size = pSize", "self.Intelligence = pIntelligence"], 1, "f3", 20) + arrow(170, 100, 170, 136, "d", "c1", 1);
    const rows = ["Name: " + (k >= 2 ? "\"Chewie\"" : "?"), "Sound: " + (k >= 2 ? "\"Squawk\"" : "?"), "Size: " + (k >= 2 ? "1" : "?"), "Intelligence: " + (k >= 2 ? "10" : "?"), "WingSpan: " + (k >= 4 ? "30" : "?"), "NumberWords: " + (k >= 4 ? "29" : "?")];
    o += classBox(440, 20, 290, k >= 5 ? "complete Parrot object" : "self (Parrot object)", rows, 1, k >= 5 ? "f3" : "f2", 24);
    if (k >= 2) o += SV.text(440, 226, "inherited attributes (from Animal) set first", "sm") + SV.text(440, 244, "then the Parrot's own attributes", "sm", op(k >= 4 ? 1 : 0.3));
    return o;
  };
  Lib.stepper($("#stB"), { w: 760, h: 262, label: "Building a Parrot object", base: { i: 0 }, draw, tween: 450, dwell: 3800, steps: [
    { cap: "<code>Parrot(\"Chewie\", \"Squawk\", 1, 10, 30, 29)</code> makes an empty Parrot object and runs Parrot's constructor on it.", s: { i: 0 } },
    { cap: "The first line of the child's constructor calls the <b>parent's constructor</b> with the four inherited values.", s: { i: 1 } },
    { cap: "<code>Animal.__init__</code> runs on the same object and sets Name, Sound, Size and Intelligence.", s: { i: 2 } },
    { cap: "It finishes, and control returns to the Parrot constructor.", s: { i: 3 } },
    { cap: "Now the child sets its <b>own</b> attributes: WingSpan and NumberWords.", s: { i: 4 } },
    { cap: "One object has all six attributes. If the parent constructor were never called, the first four would not exist.", s: { i: 5 } }] });
})();

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); let o = "";
    o += classBox(30, 20, 250, "class Animal", ["Description()  # version A"], 1, k === 2 ? "f3" : "f1", 20);
    o += classBox(330, 20, 380, "class Parrot(Animal)", k === 3 ? ["# no Description() here", "ChangeNumberWords()"] : ["Description()  # version B", "ChangeNumberWords()"], 1, k === 1 ? "f3" : "f2", 20);
    o += arrow(330, 52, 284, 52, "l", "c1", 0.8);
    const call = k === 1 ? "bird.Description()" : k === 2 ? "animal.Description()" : k === 3 ? "bird.Description()" : "";
    if (call) o += SV.text(30, 160, call, "lbl bd", { style: "font-family:var(--mono);font-size:17px" });
    if (k === 1) o += SV.text(30, 190, "bird is a Parrot: look in Parrot first, found: run version B", "lbl bd t3");
    if (k === 2) o += SV.text(30, 190, "animal is an Animal: run version A", "lbl bd t3");
    if (k === 3) o += SV.text(30, 190, "not in Parrot: look in the parent, Animal: run version A", "lbl bd t3");
    return o;
  };
  Lib.stepper($("#stC"), { w: 760, h: 215, label: "Method lookup when a child overrides a method", base: { i: 0 }, draw, tween: 400, dwell: 3600, steps: [
    { cap: "Animal defines <code>Description()</code>. Parrot inherits from Animal.", s: { i: 0 } },
    { cap: "Parrot defines its own <code>Description()</code>, so it <b>overrides</b> the parent's. A call on a Parrot object finds the child's version first.", s: { i: 1 } },
    { cap: "A call on a plain Animal object runs the Animal version.", s: { i: 2 } },
    { cap: "If Parrot did not define the method, Python would search up to the parent and <b>inherit</b> that version.", s: { i: 3 } }] });
})();

(function () {
  const L = ["speed = speed + 40", "if speed > 100:", "    speed = 100", "position = position + speed"];
  const rows = [["1", "40", "no", "40", "40"], ["2", "80", "no", "80", "120"], ["3", "120", "yes", "100", "220"], ["4", "140", "yes", "100", "320"]];
  const draw = (s) => {
    const k = Math.round(s.i); let o = codeList(20, 20, L, k === 0 ? -1 : (k % 2 === 1 ? 0 : 3), 1, 34, 250);
    o += SV.text(310, 36, "call", "sm") + SV.text(360, 36, "speed + 40", "sm") + SV.text(470, 36, "over 100?", "sm") + SV.text(570, 36, "speed", "sm") + SV.text(650, 36, "position", "sm");
    rows.forEach((r, i) => {
      if (k < i + 1) return;
      const on = k === i + 1; r.forEach((c, j) => { o += SV.text([310, 360, 470, 570, 650][j], 66 + i * 34, c, on ? "lbl bd" : "lbl", { style: "font-family:var(--mono);font-size:15px", ...(r[2] === "yes" && j === 3 ? { fill: "var(--warn)" } : {}) }); });
    });
    return o;
  };
  Lib.stepper($("#stD"), { w: 760, h: 215, label: "Four calls of IncreaseSpeed", base: { i: 0 }, draw, tween: 300, dwell: 2800, steps: [
    { cap: "Start: speed 0, position 0, <code>MaxSpeed</code> 100, <code>IncreaseAmount</code> 40. Each call runs the four lines.", s: { i: 0 } },
    { cap: "Call 1: 0 + 40 = 40, not over 100, speed 40. Position 0 + 40 = <b>40</b>.", s: { i: 1 } },
    { cap: "Call 2: 80. Position 40 + 80 = <b>120</b>.", s: { i: 2 } },
    { cap: "Call 3: 80 + 40 = 120, over 100, so the speed is limited to <b>100</b>. The position still grows: 120 + 100 = <b>220</b>.", s: { i: 3 } },
    { cap: "Call 4: the speed stays at 100 and the position goes up by 100 again: <b>320</b>. The limit applies to the speed, never to the position.", s: { i: 4 } }] });
})();

/* Lab 1 */
(function () {
  let max = 100, inc = 40, heli = false, vch = 15, mh = 40, spd, hp, vp, calls;
  const reset = () => { spd = 0; hp = 0; vp = 0; calls = []; paint(); };
  const paint = () => {
    $("#lH").textContent = "Helicopter: " + (heli ? "on" : "off"); $("#lH").classList.toggle("pri", heli);
    $("#lV").style.display = heli ? "" : "none"; $("#lX").style.display = heli ? "" : "none";
    $("#lT").innerHTML = '<div class="tw"><table class="t mono"><tr><th>Call</th><th>CurrentSpeed</th><th>HorizontalPosition</th>' + (heli ? "<th>VerticalPosition</th>" : "") + "</tr>" + calls.map((c, i) => `<tr><td>${i + 1}</td><td>${c[0]}${c[3] ? " (limited)" : ""}</td><td>${c[1]}</td>${heli ? `<td>${c[2]}${c[4] ? " (limited)" : ""}</td>` : ""}</tr>`).join("") + "</table></div>";
    $("#lv").textContent = calls.length ? "The speed stops rising at MaxSpeed (" + max + "), but the position keeps increasing by the current speed each call." : "Press Call IncreaseSpeed() to run the method.";
  };
  $("#lGo").onclick = () => {
    spd += inc; let lim = false; if (spd > max) { spd = max; lim = true; }
    hp += spd; let vlim = false; if (heli) { vp += vch; if (vp > mh) { vp = mh; vlim = true; } }
    calls.push([spd, hp, vp, lim, vlim]); if (calls.length > 10) calls.shift(); paint();
  };
  $("#lRe").onclick = reset; $("#lH").onclick = () => { heli = !heli; reset(); };
  Lib.slider($("#lM"), { id: "lms", label: "MaxSpeed ", min: 20, max: 200, value: max, fmt: (x) => x, onInput: (v) => { max = v; reset(); } });
  Lib.slider($("#lI"), { id: "lis", label: "IncreaseAmount ", min: 5, max: 80, value: inc, fmt: (x) => x, onInput: (v) => { inc = v; reset(); } });
  Lib.slider($("#lV"), { id: "lvs", label: "VerticalChange ", min: 1, max: 30, value: vch, fmt: (x) => x, onInput: (v) => { vch = v; reset(); } });
  Lib.slider($("#lX"), { id: "lxs", label: "MaxHeight ", min: 10, max: 100, value: mh, fmt: (x) => x, onInput: (v) => { mh = v; reset(); } });
  reset();
})();

/* Lab 2: class builder */
(function () {
  const sc = [
    { name: "Pet", attrs: [["PetID", "STRING"], ["PetName", "STRING"], ["DateRegistered", "DATE"]] },
    { name: "Card", attrs: [["Number", "INTEGER"], ["Colour", "STRING"]] },
    { name: "Appointment", attrs: [["DateSeen", "DATE"], ["PatientID", "INTEGER"], ["Doctor", "STRING"], ["Treatments", "STRING"]] }
  ];
  let cur = 0, pick = {};
  const key = (i, t) => cur + "_" + i + t;
  const paint = () => {
    $$("#gB button").forEach((b, i) => b.classList.toggle("pri", i === cur));
    const s = sc[cur];
    $("#gC").innerHTML = '<div class="tw"><table class="t"><tr><th>Attribute</th><th>Getter</th><th>Setter</th></tr>' + s.attrs.map((a, i) => `<tr><td><code>${a[0]} : ${a[1]}</code></td><td><label><input type="checkbox" data-k="${i}g" ${pick[key(i, "g")] ? "checked" : ""}> Get${a[0]}</label></td><td><label><input type="checkbox" data-k="${i}s" ${pick[key(i, "s")] ? "checked" : ""}> Set${a[0]}</label></td></tr>`).join("") + "</table></div>";
    $$("#gC input").forEach((c) => (c.onchange = () => { pick[cur + "_" + c.dataset.k] = c.checked; paint(); }));
    const par = (a) => "New" + a[0], L = [`class ${s.name}:`];
    s.attrs.forEach((a) => L.push(`    # ${a[0]} : ${a[1]}`));
    L.push(`    def __init__(self, ${s.attrs.map(par).join(", ")}):`);
    s.attrs.forEach((a) => L.push(`        self.__${a[0]} = New${a[0]}`));
    s.attrs.forEach((a, i) => {
      if (pick[key(i, "g")]) L.push("", `    def Get${a[0]}(self):`, `        return self.__${a[0]}`);
      if (pick[key(i, "s")]) L.push("", `    def Set${a[0]}(self, New${a[0]}):`, `        self.__${a[0]} = New${a[0]}`);
    });
    const esc = (t) => t.replace(/&/g, "&amp;").replace(/</g, "&lt;");
    $("#gO").innerHTML = '<div class="code"><pre class="cp">' + L.map((l) => `<span class="ln">${esc(l) || " "}</span>`).join("") + "</pre></div>";
  };
  $("#gB").innerHTML = sc.map((s, i) => `<button class="b" data-i="${i}">${s.name}</button>`).join("");
  $$("#gB button").forEach((b) => (b.onclick = () => { cur = +b.dataset.i; paint(); }));
  paint();
})();

btnTable("eB", "eO", [
  ["Missing self", "def GetName(): return self.__Name", "TypeError: the method is given the object but has nowhere to put it", "def GetName(self):"],
  ["No parent constructor", "class Parrot(Animal): def __init__(self, n, w): self.WingSpan = w", "AttributeError when Name is used: the inherited attributes were never set", "super().__init__(n) as the first line of the child's constructor"],
  ["Attribute without self", "def __init__(self, NewName): __Name = NewName", "The value is a local variable, forgotten when the constructor ends", "self.__Name = NewName"],
  ["Number joined to text", "return \"Size \" + self.Size", "TypeError: cannot join a string and an integer", "return \"Size \" + str(self.Size)"],
  ["Return in a setter", "def SetAge(self, a): return a", "The attribute is never changed", "self.__Age = a"],
  ["Calling private from outside", "print(MyPet.__Name)", "AttributeError: a private attribute is not directly reachable", "print(MyPet.GetName())"],
  ["Overwriting instead of adding", "self.__X = XChange", "The object jumps to the new value instead of moving by it", "self.__X = self.__X + XChange"]
], ["Mistake", "Code", "What goes wrong", "Fix"]);
''' + CLASSIFY("cl1", "What does each line of Python do?", ["Declare a class", "Constructor", "Getter", "Setter", "Create an object", "Call the parent constructor", "Override a method"],
  [("class Vehicle:", 0), ("def __init__(self, NewID, NewMax):", 1), ("def GetMaxSpeed(self):", 2), ("def SetCurrentSpeed(self, CSP):", 3), ("Car1 = Vehicle(\"V1\", 120)", 4), ("super().__init__(pName, pSound)", 5), ("class Parrot(Animal):", 0), ("def Description(self): # in Parrot, also in Animal", 6), ("return self.__HorizontalPosition", 2), ("self.__CurrentSpeed = CSP", 3)],
  "class declares, __init__ is the constructor, Get returns, Set assigns, calling the class creates, super().__init__ calls the parent, and the same method name in the child overrides.") + ORDER(
  "Put the steps for writing a child class in order.",
  ["Write the class header with the parent in brackets", "Add attribute comments for the new attributes only", "Write the constructor taking the parent's values and the new ones", "Call the parent constructor with the inherited values", "Assign the new attributes", "Write or override the methods that are different"],
  "Header, comments, constructor, parent call, new attributes, methods.") + MATCH([
  ["self", "The object the method is running on"], ["__init__", "The constructor, called when an object is created"], ["self.__Name", "A private attribute"], ["super().__init__(...)", "Calls the parent class constructor"], ["Same method name in the child", "Overrides the parent's method"]]) + CALC([
  {"q": "A vehicle starts with speed 0 and position 0, IncreaseAmount 30 and MaxSpeed 100. After 2 calls to IncreaseSpeed(), what is the CurrentSpeed?", "a": 60, "unit": "", "tol": 0.01, "hint": "30, then 60.", "sol": "<b>60</b>."},
  {"q": "Same vehicle: what is the HorizontalPosition after 2 calls?", "a": 90, "unit": "", "tol": 0.01, "hint": "Position 30, then 30 + 60.", "sol": "<b>90</b>."},
  {"q": "Same vehicle: what is the CurrentSpeed after 5 calls?", "a": 100, "unit": "", "tol": 0.01, "hint": "30, 60, 90, 120 limited to 100, 100.", "sol": "<b>100</b>."},
  {"q": "Same vehicle: what is the HorizontalPosition after 4 calls?", "a": 280, "unit": "", "tol": 0.01, "hint": "30 + 60 + 90 + 100.", "sol": "<b>280</b>."},
  {"q": "NumberWords is 29. ChangeNumberWords(5) is called twice. What is NumberWords?", "a": 39, "unit": "", "tol": 0.01, "hint": "29 + 5 + 5.", "sol": "<b>39</b>."},
  {"q": "A Character is at x = 10. ChangePosition(4, 0) then ChangePosition(-7, 3) are called. What is the x coordinate?", "a": 7, "unit": "", "tol": 0.01, "hint": "10 + 4 - 7.", "sol": "<b>7</b>."}]) + MCQ([
  ("What is the constructor in Python called?", ["__new__", "__init__", "constructor", "init"], 1, "__init__ with two underscores each side."),
  ("What makes an attribute private?", ["The word private", "Two underscores at the start of its name", "Capital letters", "A comment"], 1, "self.__Name is private."),
  ("What does super().__init__(...) do?", ["Deletes the parent", "Calls the parent constructor", "Creates a new class", "Overrides a method"], 1, "It sets the inherited attributes."),
  ("What is wrong with: def GetAge(): return self.__Age", ["Nothing", "It is missing self as a parameter", "It should print", "__Age is public"], 1, "Every method needs self."),
  ("A child class has a method with the same name as its parent's. What is this called?", ["Inheritance", "Overriding", "Encapsulation", "Containment"], 1, "The child version runs for child objects."),
  ("How is an object created from the class Hand?", ["Hand.new()", "MyHand = Hand(Card1, Card2, Card3, Card4, Card5)", "class MyHand", "create Hand"], 1, "Call the class like a function with the constructor's arguments.")], "qz1") + CARDS([
  ("class Name:", "Declares a class."), ("__init__(self, ...)", "The constructor. Assigns the parameters to attributes."), ("self.__Attr", "A private attribute."), ("Getter", "def GetX(self): return self.__X"),
  ("Setter", "def SetX(self, v): self.__X = v"), ("class Child(Parent):", "Child inherits from Parent."), ("super().__init__(...)", "Calls the parent constructor."), ("Override", "Same method name in the child class.")])

build("ac2013", "ac-20-1-3-oop-in-python", "Object-Oriented Programming: Writing Classes in Python", EYA("20.1.3"),
  "Declaring classes with private attributes and constructors, getters and setters, a method with a limit, child classes that call the parent constructor and override a method, and containment; animations, labs and the real Paper 4 questions.",
  dict(sub=CBK("Chapter 20 · Further programming, section 20.1 Programming paradigms"), **tabs(learn, watch, explore, practise, real, exam, tips)), js)
