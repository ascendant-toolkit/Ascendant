"""A Level CS syllabus 20.1.2: object-oriented programming, terminology and class design. Run: python3 tools/artifact-kit/mk_ac2012.py"""
from ak20 import *

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>In <b>object-oriented programming (OOP)</b> a program is built from <b>objects</b>, each created from a <b>class</b> that defines its <b>properties</b> (attributes) and <b>methods</b>. A <b>constructor</b> sets up a new object, and <b>encapsulation</b> keeps the properties private so they can only be read or changed through <b>getters</b> and <b>setters</b>. <b>Inheritance</b> lets a new class take the properties and methods of a parent class, and <b>polymorphism</b> lets the same method name behave differently in different classes. When one class holds objects of another, that is <b>containment (aggregation)</b>. To solve a problem you decide the classes, their properties and their methods before writing any code; the next page turns the designs into working code.</p></div>

  <h2>1 · The terms you must know</h2>
  <div class="tw"><table class="t">
    <tr><th>Term</th><th>Meaning</th><th>Example</th></tr>
    <tr><td><b>Class</b></td><td>A template that defines the properties and methods that its objects will have</td><td><code>Pet</code></td></tr>
    <tr><td><b>Object / instance</b></td><td>One occurrence of a class, with its own values. Creating it is <b>instantiation</b></td><td>The pet called Rex</td></tr>
    <tr><td><b>Property / attribute</b></td><td>A data item stored in an object, with a data type</td><td><code>PetName : STRING</code></td></tr>
    <tr><td><b>Method</b></td><td>A procedure or function defined in the class that acts on the object's properties</td><td><code>GetPetName()</code></td></tr>
    <tr><td><b>Constructor</b></td><td>The method that runs when an object is created and sets its starting values</td><td><code>NEW(...)</code>, Python <code>__init__</code></td></tr>
    <tr><td><b>Encapsulation</b></td><td>Putting the properties and methods together in a class and hiding the data, so it can only be reached through the class's own methods</td><td>Properties declared <code>PRIVATE</code></td></tr>
    <tr><td><b>Getter</b></td><td>A method that returns the value of a property</td><td><code>GetPetName()</code></td></tr>
    <tr><td><b>Setter</b></td><td>A method that updates the value of a property</td><td><code>SetPetName(NewName)</code></td></tr>
    <tr><td><b>Inheritance</b></td><td>A new (child, derived) class takes the properties and methods of a parent (base, super) class and can add its own or override methods</td><td><code>Parrot</code> inherits from <code>Animal</code></td></tr>
    <tr><td><b>Polymorphism</b></td><td>Methods with the same name are redefined in derived classes, so the same call behaves differently depending on the object</td><td><code>Description()</code> in Animal and in Parrot</td></tr>
    <tr><td><b>Containment (aggregation)</b></td><td>One class contains objects of another class: a "has a" relationship</td><td>A <code>Hand</code> holds <code>Card</code> objects</td></tr>
  </table></div>

  <h2>2 · Why encapsulation?</h2>
  <p>If every part of a program can change an object's data directly, any bug or careless line can corrupt it. With <b>private</b> properties the only way in is through the methods, so the class can check values (a priority must be 1 to 5), a property can be made read-only by providing a getter but no setter, and the inside of the class can change without breaking the rest of the program. The mark scheme answer is short: <b>so the attributes can only be accessed using the class's own methods</b>.</p>

  <h2>3 · Class diagrams</h2>
  <p>A class diagram is a box in three parts: the class name, the properties with their data types, and the methods. Exams ask you to <b>complete</b> one from a description. The pattern is nearly always the same:</p>
  <ul>
    <li>one property for each data item, with a sensible name and the right data type (STRING, INTEGER, DATE, BOOLEAN, REAL)</li>
    <li>a <b>constructor</b> if the question says objects are created with their values set</li>
    <li>a <b>setter</b> for each property that can change: <code>SetPriority(Urgency : INTEGER)</code>, with a parameter and its data type</li>
    <li>a <b>getter</b> for each property that has to be read: <code>GetPriority()</code>, with no parameter</li>
    <li>names that match the property they work with (<code>Priority</code>, <code>SetPriority</code>, <code>GetPriority</code>)</li>
  </ul>
  <pre class="plain">             Pet
PetID : STRING
PetName : STRING
DateRegistered : DATE
Constructor()
SetPetID(APetID : STRING)
SetDateRegistered(RegDate : DATE)
GetPetName()</pre>
  <p>For <b>inheritance</b>, draw the child classes below the parent with an arrow pointing up to it. Show only what is new in the child: properties it adds, and methods it adds or overrides (such as its own constructor). Do not repeat what it inherits.</p>

  <h2>4 · Designing classes to solve a problem</h2>
  <ol>
    <li><b>Find the things</b> the problem talks about (customers, vehicles, yarn). Each kind of thing is a class.</li>
    <li><b>List the data</b> each one stores. Each item is a property with a data type.</li>
    <li><b>List what each one does</b>: displays itself, changes its stock, moves. Each action is a method.</li>
    <li><b>Look for sharing.</b> If several classes share properties and methods and one "is a" kind of the other, put the shared parts in a parent class (inheritance). If one thing "has" others inside it, use containment.</li>
    <li><b>Decide access.</b> Make properties private and add getters and setters only where they are needed.</li>
  </ol>
  <div class="tip"><b class="h">Is a, or has a?</b>A Parrot <i>is an</i> Animal: inheritance. A Hand <i>has</i> Cards: containment. If you can put "is a" between the two names and it makes sense, it is inheritance.</div>

  <h2>5 · Pseudocode for a class</h2>
  <p>Cambridge pseudocode declares a class like this. Python does the same job with <code>class</code> and <code>__init__</code>; the next page covers it.</p>
  <div class="code">''' + pc('''CLASS Animal
   PRIVATE Name : STRING
   PRIVATE Size : INTEGER
   PUBLIC PROCEDURE NEW(NewName : STRING, NewSize : INTEGER)
      Name ← NewName
      Size ← NewSize
   ENDPROCEDURE
   PUBLIC FUNCTION GetName() RETURNS STRING
      RETURN Name
   ENDFUNCTION
   PUBLIC PROCEDURE SetSize(NewSize : INTEGER)
      Size ← NewSize
   ENDPROCEDURE
ENDCLASS

CLASS Parrot INHERITS Animal
   PRIVATE WingSpan : INTEGER
   PUBLIC PROCEDURE NEW(NewName : STRING, NewSize : INTEGER, NewSpan : INTEGER)
      SUPER.NEW(NewName, NewSize)
      WingSpan ← NewSpan
   ENDPROCEDURE
ENDCLASS

MyBird ← NEW Parrot("Chewie", 1, 30)''') + '''</div>

  <h2>6 · Common ways to lose marks</h2>
  <ul>
    <li>Defining encapsulation as "hiding things". Say the properties and methods are in one class and the data can only be reached through the class's own methods.</li>
    <li>Mixing up <b>class</b> (the template) and <b>object</b> (an instance of it).</li>
    <li>Writing a setter with no parameter, or a getter with one. A setter takes the new value; a getter takes nothing.</li>
    <li>Giving a getter or setter a name that does not match its property.</li>
    <li>Repeating the parent's properties in the child class diagram, or drawing the arrow the wrong way.</li>
    <li>Describing polymorphism as "many classes". It is the same method name redefined, with different behaviour, in derived classes.</li>
  </ul>
'''

watch = '''
  <h2>1 · One class, many objects</h2>
  <p>Press Play, or click the steps. The class is the template; each object has its own values.</p>
  <div id="stA"></div>
  <h2>2 · Encapsulation: private data, public methods</h2>
  <div id="stB"></div>
  <h2>3 · Inheritance: the yarn shop</h2>
  <p>From the May/June 2022 question: three types of yarn share most of their data.</p>
  <div id="stC"></div>
  <h2>4 · Polymorphism: same call, different behaviour</h2>
  <div id="stD"></div>
  <h2>5 · Containment: a hand has cards</h2>
  <div id="stE"></div>
'''

explore = '''
  <h2>Lab 1 · Public or private?</h2>
  <p>A Pet object stores an age. Choose how the property is declared, then try to read it and to set it to an impossible value.</p>
  <div class="card"><div id="vB" class="btnrow"></div><div class="btnrow"><button class="b" id="vR">Read Age directly</button><button class="b" id="vG">Call GetAge()</button><button class="b" id="vN">Set Age to 25 directly</button><button class="b" id="vS">Call SetAge(25)</button><button class="b" id="vC">Call SetAge(-3)</button></div>
    <div class="readout"><div><small>Age stored</small><strong id="v1"></strong></div></div><div class="verdict" id="vv"></div></div>

  <h2>Lab 2 · What does each class have?</h2>
  <p>Choose a yarn class. The table shows what it inherits and what it adds, using the class diagram from the exam.</p>
  <div class="card"><div id="iB" class="btnrow"></div><div id="iO"></div></div>

  <h2>Lab 3 · The terms in an exam answer</h2>
  <div class="card"><div id="eB" class="btnrow"></div><div id="eO"></div></div>
'''

practise = '''
  <h2>1 · Attribute, method, getter, setter or constructor?</h2><div id="cl1" class="card"></div>
  <h2>2 · Inheritance or containment?</h2><div id="cl2" class="card"></div>
  <h2>3 · Put the steps of class design in order</h2><div id="o1" class="card"></div>
  <h2>4 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>5 · Count the members</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("A school management system", "Student, Teacher and Substitute can share a parent class Person with a name and a telephone number, and each adds its own data. Records are private and changed through setters, so a telephone number is always stored in the same format.", "inheritance for shared data, encapsulation for safe changes, setters that check values.") +
rw("A video game", "Every character has a position and a name, but a magic character also has spells and a bike character has a speed. They inherit from Character, and each overrides a method such as Move() to behave in its own way.", "polymorphism: one call to Move() on a list of characters does the right thing for each.") +
rw("A card game", "A Hand object contains five Card objects, and the game can ask each card for its number and colour through getters without ever touching the card's private data.", "containment (a Hand has Cards) and getters.") +
rw("A bank account", "Balance is private. You cannot set it to any number you like: Deposit() and Withdraw() are the only ways in, and Withdraw() refuses to go below the overdraft limit.", "encapsulation protects the data; methods enforce the rules.") +
rw("A medical records system", "An Appointment records the patient, doctor, treatments and medications. The date seen has a setter and a getter, but the patient number is set once and only read, so it has a getter but no setter.", "choose getters and setters to match what is allowed to change.")
)

where = [
  ("M/J 2022", "31, 33", "7(a), 7(b)", "5 + 6", "Complete a class inheritance diagram; describe properties, methods, inheritance"),
  ("M/J 2022", "32", "1(c)", "1 + 2", "Declare a private property; explain why properties are private"),
  ("O/N 2022", "31, 33", "11(a), 11(b)", "3 + 5", "Define instance, inheritance, polymorphism; complete the Car class in pseudocode"),
  ("O/N 2022", "32", "10(a), 10(b)", "3 + 3", "Define encapsulation, getter, setter; complete the SubstituteTeacher diagram"),
  ("M/J 2023", "32", "4", "4", "Match four OOP terms to descriptions"),
  ("O/N 2024", "31, 33", "9(a), 9(b)", "1 + 5", "Why private attributes; complete the Pet class diagram"),
  ("M/J 2025", "31", "11(a), 11(b)", "5 + 1 + 2", "Complete the Appointment diagram; name encapsulation; describe inheritance"),
  ("M/J 2025", "32", "12(a), 12(b)", "5 + 1 + 2", "Complete the Patient diagram; name instance; describe polymorphism"),
  ("M/J 2025", "33", "5", "4", "Complete a table of OOP terms and descriptions"),
  ("M/J 2026", "32", "11(a), 11(b)", "5 + 4", "Write pseudocode for the Node class; complete a table including aggregation and inheritance")]

DIAG1 = '''                    Yarn
         Name : STRING
         Colour : STRING
         BatchCode : STRING
         Weight : INTEGER
         NumberBalls : INTEGER
         Type : STRING
         Constructor()
         EditNumberBalls()
         YarnInfo()

   Acrylic           Wool              Mix
                                       Percentage : INTEGER
                                       Constructor()
                                       YarnInfo()
   Constructor()     Constructor()'''

past = '''  <p class="note">Class diagrams, the OOP terms and pseudocode for a class are tested in Paper 3. Writing the classes as program code is tested in Paper 4 (next page). Questions below are reworded from the papers; check the original paper and mark scheme for the exact wording.</p>

  <h3>Class diagrams</h3>
''' + peq(SRC("s22", "31, 33", "Q7(a), (b)"), "5 + 6 marks", "Complete / Describe",
  "A program for a shop that sells knitting yarn uses OOP. There are three types of yarn: acrylic, wool and mix. Each stores a name, colour, batch code, weight, number of balls in stock (can be edited) and type of yarn. Acrylic can be soft or not soft. Wool can be lamb, merino or alpaca. Mix contains a percentage of acrylic. Each type has a method that displays all the information about the yarn. (a) Complete the class inheritance diagram below to show the properties, methods and inheritance. (b) Describe what is meant by the terms properties, methods and inheritance." + qcode(DIAG1),
  "Add only what is new in each child class. Soft is a BOOLEAN; the wool type is a STRING. Acrylic and Wool also need YarnInfo(). Arrows from every child to Yarn.",
  "<p><b>(a)</b> Five marks: " + mks(["Acrylic has an attribute Soft : BOOLEAN", "Wool has an attribute for the wool type with a suitable data type", "Acrylic and Wool both have the method YarnInfo()", "at least one child inherits from Yarn (one arrow correct)", "all three children inherit from Yarn (all arrows correct)"]) + "</p>" + qcode('''                    Yarn
         (Name, Colour, BatchCode, Weight, NumberBalls, Type,
          Constructor(), EditNumberBalls(), YarnInfo())
           ^               ^                  ^
   Acrylic         Wool                Mix
   Soft : BOOLEAN  WoolType : STRING   Percentage : INTEGER
   Constructor()   Constructor()       Constructor()
   YarnInfo()      YarnInfo()          YarnInfo()''') + "<p><b>(b)</b> Two marks each, up to 6: " + mks(["Properties: the data items / attributes", "with their data types", "defined in a class"], "a") + " " + mks(["Methods: the procedures or functions", "that act on the properties / implement the behaviours of the class"], "a") + " " + mks(["Inheritance: the methods and properties of one (parent / super) class", "are made available to, or reused by, another (derived / child) class"], "a") + "</p>",
  "Drawing the arrows from Yarn down to the children. The arrow points from the child to the parent it inherits from.") + peq(SRC("w24", "31, 33", "Q9"), "1 + 5 marks", "State / Complete",
  "A veterinary surgery wants a class for individual pets. Some of the attributes are PetID (STRING, unique ID assigned at registration), PetType (STRING), OwnerTelephone (STRING) and DateRegistered (DATE). (a) State one reason why the attributes would be declared as PRIVATE. (b) Complete the class diagram for Pet to include: an attribute and data type for the name of the pet; an attribute and data type for the name of the owner; a method to create a Pet object and set attributes at registration; a method to assign a pet ID; a method to assign the date of registration; a method to return the pet name; a method to return the owner's telephone number.",
  "Two new attributes, a constructor, two setters, two getters. Setters take a parameter with a data type; getters take none.",
  "<p><b>(a)</b> " + mks(["So the attributes can only be accessed using the class's own methods / within the class."]) + "</p><p><b>(b)</b> Five marks: " + mks(["two correct attributes with sensible names and data types", "a constructor is present", "two correct setters with exact names and parameters with data types", "two correct getters with appropriate names", "the name used for the pet-name getter matches the attribute"], "a") + "</p>" + qcode('''                    Pet
PetID : STRING
PetType : STRING
OwnerTelephone : STRING
DateRegistered : DATE
PetName : STRING
OwnerName : STRING
Constructor()
SetPetID(APetID : STRING)
SetDateRegistered(RegDate : DATE)
GetPetName()
GetOwnerTelephone()'''),
  "Giving the getters parameters, or forgetting the data type on a setter parameter.") + peq(SRC("s25", "31", "Q11"), "5 + 1 + 2 marks", "Complete / Identify / Describe",
  "A medical centre uses objects of the class Appointment. Attributes given: DateSeen (DATE), Treatments (STRING), Medications (STRING). Patients are identified by a unique 8-digit number beginning with the year of birth, for example 20108989. Doctors are identified by their name, for example A N Other. (a) Complete the class diagram for Appointment to include: an attribute and data type for the patient; an attribute and data type for the doctor; methods to assign the date seen, treatments and medications; methods to return the date seen and the patient and doctor attributes. (b) (i) Identify the OOP feature whose function includes restricting external access to the data. (ii) Describe what is meant by inheritance.",
  "The 8-digit number is stored as an INTEGER; the doctor's name is a STRING. Check you have a setter for each assign and a getter for each return.",
  "<p><b>(a)</b> Five marks: " + mks(["two correct attributes (PatientID : INTEGER, Doctor : STRING)", "SetTreatments() and SetMedications() seen", "with appropriate STRING parameters", "GetPatientID() and GetDoctor() seen", "SetDateSeen() and GetDateSeen() fully correct, with a DATE parameter"]) + "</p>" + qcode('''                 Appointment
DateSeen : DATE
PatientID : INTEGER
Doctor : STRING
Treatments : STRING
Medications : STRING
SetDateSeen(NewDate : DATE)
SetPatientID(PatientNumber : INTEGER)
SetDoctor(DoctorID : STRING)
SetTreatments(NewTreatments : STRING)
SetMedications(NewMedications : STRING)
GetDateSeen()
GetPatientID()
GetDoctor()''') + "<p><b>(b)(i)</b> " + mks(["Encapsulation"], "a") + " <b>(ii)</b> " + mks(["A derived class takes the properties / methods", "of a parent (super / base) class", "and these can also be extended, used or overridden in the subclass"], "a") + " (maximum 2)</p>",
  "Storing the patient number as a STRING without a reason. The question says it is an 8-digit number, and INTEGER is what the mark scheme gives.") + peq(SRC("s25", "32", "Q12"), "5 + 1 + 2 marks", "Complete / Identify / Describe",
  "A medical clinic uses objects of the class Patient to assign a priority and a doctor to a patient. Attributes given: PatientID (STRING), Name (STRING, full name surname first), DoctorID (STRING). Treatment is prioritised with a numeric scale of 1 to 5. (a) Complete the class diagram for Patient to include: an attribute and data type for the date of birth; an attribute and data type for the priority; methods to assign the patient ID, priority and doctor ID; methods to return the patient ID, date of birth and the priority. (b) (i) Identify the OOP term described as 'an occurrence of an object'. (ii) Describe what is meant by polymorphism.",
  "Priority 1 to 5 is an INTEGER. Name the setter and getter after the attribute.",
  "<p><b>(a)</b> Five marks: " + mks(["DateOfBirth : DATE and a priority attribute with an INTEGER type", "SetPatientID() and SetDoctorID() seen", "with appropriate STRING parameters", "GetPatientID() and GetDateOfBirth() seen", "setter and getter for Priority fully correct, matching the attribute, with an INTEGER parameter"]) + "</p>" + qcode('''                 Patient
PatientID : STRING
Name : STRING
DateOfBirth : DATE
Priority : INTEGER
DoctorID : STRING
SetPatientID(PatientNumber : STRING)
SetDateOfBirth(DOB : DATE)
SetPriority(Urgency : INTEGER)
SetDoctorID(DocID : STRING)
GetPatientID()
GetDateOfBirth()
GetPriority()''') + "<p><b>(b)(i)</b> " + mks(["Instance (or instantiation)"], "a") + " <b>(ii)</b> " + mks(["Methods with the same name are redefined / behave differently", "in derived (inherited) classes / subclasses"], "a") + "</p>",
  "Describing polymorphism as 'having many forms' without saying the same method name is redefined in derived classes.") + '''
  <h3>Defining the terms</h3>
''' + peq(SRC("w22", "31, 33", "Q11(a)"), "3 marks", "Define",
  "Define these OOP terms: instance, inheritance, polymorphism.",
  "One mark each. Use the words occurrence of an object, parent class and redefined.",
  "<p>" + mks(["Instance: an occurrence of an object / a specific object based on the class / an instantiation of a class", "Inheritance: the capability of defining a new class that has all the attributes and methods of a parent class", "Polymorphism: the same method takes on different behaviours depending on which class is instantiated / methods can be redefined for derived classes"]) + "</p>",
  "Defining an instance as 'a class'. An instance is an object made from a class.") + peq(SRC("w22", "32", "Q10(a)"), "3 marks", "Define",
  "Define these OOP terms: encapsulation, getter, setter.",
  "One mark each.",
  "<p>" + mks(["Encapsulation: putting properties and methods inside a class, so sensitive data is hidden by keeping the values inside the class", "Getter: a method used to return the value of a property", "Setter: a method used to update the value of a property"]) + "</p>",
  "Writing that a getter 'gets the data' with no mention that it is a method that returns a property's value.") + peq(SRC("s23", "32", "Q4"), "4 marks", "Match",
  "Draw one line from each OOP term to its most appropriate description. Terms: encapsulation, getters, polymorphism, setters. Descriptions: (A) methods used to return the value of a property; (B) the process of putting data and methods together as a single unit; (C) methods used to update the value of a property; (D) allows methods to be redefined for derived classes; (E) enables the defining of a new class that inherits from a parent class.",
  "Four terms, five descriptions: one description (inheritance) is not asked for.",
  "<p>" + mks(["Encapsulation matches (B) data and methods together as a single unit", "Getters match (A) return the value of a property", "Polymorphism matches (D) methods redefined for derived classes", "Setters match (C) update the value of a property"]) + "</p><p>Description (E) describes inheritance, which is the odd one out.</p>",
  "Matching setters to the description of getters. Setters change a value; getters return it.") + peq(SRC("s25", "33", "Q5"), "4 marks", "Complete",
  "Complete the table by filling in the missing OOP terms and descriptions. Known: a method that accesses the value of a property (term missing); a method that changes the value of a property (term missing); Object (description missing); Method (description missing).",
  "One mark each (maximum 4).",
  "<p>" + mks(["Getter: a method that accesses the value of a property", "Setter: a method that changes the value of a property", "Object: an instantiation / instance of a class", "Method: a programmed function / procedure / subroutine defined as part of a class"]) + "</p>",
  None) + peq(SRC("s26", "32", "Q11(b)"), "4 marks", "Complete",
  "Complete the table of OOP terms and descriptions. Terms given: aggregation, inheritance. Descriptions given: 'a method used to change values in private attributes in a class' (term missing) and 'an occurrence of a class during the execution of a program' (term missing). Write the missing terms and the missing descriptions for aggregation and inheritance.",
  "Aggregation is a has-a relationship. Inheritance is an is-a relationship where the child reuses the parent.",
  "<p>" + mks(["Setter: a method used to change values in private attributes in a class", "Instance / object: an occurrence of a class during the execution of a program", "Aggregation: one class or object contains another / a hierarchy of nested objects / a 'has a' relationship", "Inheritance: a class takes the attributes and methods of another (parent) class"]) + "</p>",
  "Describing aggregation as inheritance. Aggregation is 'has a', inheritance is 'is a'.") + peq(SRC("s22", "32", "Q1(c)"), "1 + 2 marks", "Write / Explain",
  "A program is rewritten using OOP. The record type BuildingRecord becomes the class BuildingClass, with properties BuildingID, BuildingGroup, OwnerName, BuildingAddress, DateLastSold and PriceLastSold, all PRIVATE, for example <code>PRIVATE PriceLastSold : REAL</code>. (i) Write the declaration in pseudocode for OwnerName as PRIVATE. (ii) Explain why the properties have been set to PRIVATE.",
  "(i) follow the example. (ii) say who can reach the data and what that protects.",
  "<p><b>(i)</b> " + mks(["PRIVATE OwnerName : STRING"]) + "</p><p><b>(ii)</b> " + mks(["To ensure the attributes can only be accessed by the class's own methods", "so that the data cannot be changed by mistake or by other parts of the program (it is protected / encapsulated)"], "a") + "</p>",
  "Leaving out the data type, or writing PUBLIC.") + '''
  <h3>Writing a class in pseudocode</h3>
''' + peq(SRC("w22", "31, 33", "Q11(b)"), "5 marks", "Complete",
  "In OOP, a class contains attributes and methods. Complete the pseudocode for the class Car to enable objects to be created. The class needs string attributes for the make, model, body type and fuel type, and an integer attribute for the number of cars of that type built. The attributes must be available only through the methods of the class." + qcode('''CLASS ...
   PRIVATE Make : STRING
   PRIVATE ...
   PUBLIC PROCEDURE New(CarMake : STRING, ... ,
      Make ← ...
      Model ← ...
   ...'''),
  "Private for all five. The constructor sets the attributes from its parameters. Use the same identifiers in the declarations and the assignments.",
  "<p>Five marks: " + mks(["CLASS Car and ENDCLASS", "four declarations using the identifiers used in the assignments", "constructor header using CarBodyType", "two assignments using CarMake", "the constructor identifier for the model and the identifier in the Model assignment match"]) + "</p>" + pc('''CLASS Car
   PRIVATE Make : STRING
   PRIVATE Model : STRING
   PRIVATE BodyType : STRING
   PRIVATE Fuel : STRING
   PRIVATE NumberBuilt : INTEGER
   PUBLIC PROCEDURE NEW(CarMake : STRING, CarModel : STRING, CarBodyType : STRING)
      Make ← CarMake
      Model ← CarModel
      BodyType ← CarBodyType
      Fuel ← ""
      NumberBuilt ← 0
   ENDPROCEDURE
ENDCLASS'''),
  "Using a parameter name in the declaration (PRIVATE CarMake) or leaving the model assignment using a different name from the parameter.") + peq(SRC("s26", "32", "Q11(a)"), "5 marks", "Write",
  "Object-oriented programming is used to design a class called Node. A partial design includes the STRING attribute Content and the INTEGER attribute Pointer, together with their getters and setters. The class also includes a constructor with two parameters to set the values of these attributes. Write pseudocode statements to declare the Node class, its attributes and the constructor.",
  "Class and ENDCLASS, two private attributes, a public constructor with two parameters, two assignments.",
  "<p>Five marks: " + mks(["CLASS Node and ENDCLASS", "attribute declarations (Content : STRING, Pointer : INTEGER) before the constructor", "the constructor started and ended as PUBLIC PROCEDURE NEW ... ENDPROCEDURE", "two parameters with appropriate names and data types", "the parameters assigned to the attributes"]) + "</p>" + pc('''CLASS Node
   PRIVATE Content : STRING
   PRIVATE Pointer : INTEGER
   PUBLIC PROCEDURE NEW(NewContent : STRING, NewPointer : INTEGER)
      Content ← NewContent
      Pointer ← NewPointer
   ENDPROCEDURE
ENDCLASS'''),
  "Using the attribute names for the parameters, so the assignment does nothing useful in some languages.") + '''
  <h3>Getters and setters in a diagram</h3>
''' + peq(SRC("w22", "32", "Q10(b)"), "3 marks", "Complete",
  "A school's OOP program stores the details of substitute teachers: full name, telephone number and whether they are in school today, for example SubName: Sarah Jones, Telephone: 01223658721, InSchool: TRUE. Complete the diagram for the object SubstituteTeacher, including appropriate properties and their getters and setters." + qcode('''            SubstituteTeacher
SubName : STRING
InSchool : BOOLEAN
SetTelephone(Tel : STRING)'''),
  "Complete the three properties first, then one setter and one getter for each.",
  "<p>Three marks: " + mks(["properties correct (the missing Telephone : STRING)", "setters correct for all three", "getters correct for all three"]) + "</p>" + qcode('''            SubstituteTeacher
SubName : STRING
Telephone : STRING
InSchool : BOOLEAN
SetSubName(StaffName : STRING)
SetTelephone(Tel : STRING)
SetInSchool(Present : BOOLEAN)
GetSubName()
GetTelephone()
GetInSchool()'''),
  "Storing the telephone number as an INTEGER. The leading 0 would be lost, so it is a STRING.")

review = req("2 marks", "State", "State two benefits of keeping the properties of a class private.", "Think about protection and control.",
  "<p>" + mks(["The data can only be changed through the class's methods, so it cannot be corrupted by other parts of the program.", "The class can validate values in its setters, and can be changed internally without affecting other code."]) + "</p>", None) + req("3 marks", "Complete", "A class Book has the properties Title (STRING), Pages (INTEGER) and OnLoan (BOOLEAN). The title never changes after the book is created. Write the class diagram.", "A property that never changes has a getter but no setter.",
  "<p>" + mks(["three properties with correct data types", "a constructor, and setters for Pages and OnLoan only", "getters for all three"]) + "</p>" + qcode('''                  Book
Title : STRING
Pages : INTEGER
OnLoan : BOOLEAN
Constructor()
SetPages(NewPages : INTEGER)
SetOnLoan(Status : BOOLEAN)
GetTitle()
GetPages()
GetOnLoan()'''), "Adding SetTitle(). The question says the title never changes.") + req("2 marks", "Distinguish", "Distinguish between a class and an object.", "Template against occurrence.",
  "<p>" + mks(["A class is a template that defines the properties and methods.", "An object is an instance of the class: one occurrence with its own values."]) + "</p>", None) + req("3 marks", "Explain", "A class Vehicle has child classes Car and Lorry. Explain how inheritance helps the programmer.", "What is written once, and where it is reused.",
  "<p>" + mks(["Properties and methods common to all vehicles are written once, in Vehicle.", "Car and Lorry reuse them, so less code is written and tested.", "Each child adds only what is different, or overrides a method, and a change to Vehicle reaches both."]) + "</p>", None) + req("2 marks", "Identify", "A Garage class holds a list of Vehicle objects. State the OOP relationship and say why it is not inheritance.", "Has a, or is a?",
  "<p>" + mks(["Containment (aggregation): a Garage has vehicles.", "A Garage is not a kind of Vehicle, so the 'is a' test of inheritance fails."]) + "</p>", None) + req("3 marks", "Describe", "Class Shape has a method Area() returning 0. Circle and Rectangle each define their own Area(). Describe how this shows polymorphism.", "Same name, different behaviour.",
  "<p>" + mks(["Circle and Rectangle both have a method called Area().", "Each redefines (overrides) the method in the parent class.", "Calling Area() on a Circle or on a Rectangle runs the version for that class, giving different results."]) + "</p>", None)

exam = exam20("Part 1 is real 9618 questions on OOP terminology and class design (Paper 3), 2021 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", where, past, review)

tips = tips_html([
  ("Use the exact definitions.", "Instance: an occurrence of an object. Inheritance: a new class takes the properties and methods of a parent class. Polymorphism: the same method is redefined in derived classes."),
  ("Setters take, getters give.", "SetX(NewValue : TYPE) has a parameter. GetX() has none and returns the value."),
  ("Match the names.", "Property Priority, setter SetPriority, getter GetPriority. The mark scheme checks that they match."),
  ("Read the data types from the text.", "A number with a leading zero or a unique ID is usually a STRING. A scale of 1 to 5 is an INTEGER."),
  ("Private is the default.", "If the question says attributes must be private, say so in the declaration, and say why: only reached by the class's own methods."),
  ("Draw inheritance arrows upward.", "Child to parent, and show only the new members."),
], [
  ("what encapsulation does", "The properties are private, so they can only be accessed through the class's own methods."),
  ("what inheritance means", "A derived class takes the properties and methods of a parent class, and can extend or override them."),
  ("what polymorphism means", "A method with the same name is redefined in a derived class, so it behaves differently for different objects."),
  ("what a setter does", "It is a method that updates the value of a private property, and it can check the value first."),
], [("State / Identify", "Give the term or the one fact asked for."), ("Define", "Give the exact meaning, using the standard words."), ("Describe", "Say what it is and what it does, in two or three points."), ("Complete", "Fill in the diagram or pseudocode with names and data types that match.")]) + FC

js = AKJS + AK20JS + r'''
/* class box: x, y, w, title, rows (strings), v (opacity), cls fill */
function classBox(x, y, w, title, rows, v = 1, cls = "f1", lh = 20) {
  const h = 30 + rows.length * lh + 8;
  let o = SV.rect(x, y, w, h, "cell", { rx: 6, ...op(v) }) + SV.rect(x, y, w, 28, cls, { rx: 6, ...op(v * 0.6) }) + SV.text(x + w / 2, y + 19, title, "lbl bd", { "text-anchor": "middle", style: "font-size:15px", ...op(v) });
  rows.forEach((r, i) => { o += SV.text(x + 8, y + 46 + i * lh, r, "sm", { style: "font-family:var(--mono);font-size:11.5px", ...op(v) }); });
  return o;
}

(function () {
  const objs = [["Rex", "Dog", "2021"], ["Tilly", "Cat", "2023"], ["Kiwi", "Parrot", "2024"]];
  const draw = (s) => {
    const k = Math.round(s.i); let o = classBox(20, 30, 210, "class Pet", ["PetName : STRING", "PetType : STRING", "YearBorn : INTEGER", "Constructor()", "GetPetName()"], 1, "f1");
    objs.forEach((ob, n) => {
      const v = k > n ? 1 : 0, x = 280 + n * 160;
      if (v) { o += classBox(x, 60, 140, n === 1 && k === 4 ? "object p2" : "object p" + (n + 1), ["PetName: " + (n === 1 && k === 4 ? "Mittens" : ob[0]), "PetType: " + ob[1], "YearBorn: " + ob[2]], 1, "f2", 24) + SV.line(230, 100, x, 110, "dash", op(0.6)); }
    });
    if (k >= 1) o += SV.text(20, 22, "template", "sm");
    if (k >= 4) o += SV.text(440, 38, "p2 changed; p1 and p3 are not affected", "sm");
    return o;
  };
  Lib.stepper($("#stA"), { w: 760, h: 230, label: "One class and three objects", base: { i: 0 }, draw, tween: 500, dwell: 3800, steps: [
    { cap: "The <b>class</b> Pet is a template: it lists the properties and methods every pet will have. It holds no particular pet's data.", s: { i: 0 } },
    { cap: "<code>p1 ← NEW Pet(\"Rex\", \"Dog\", 2021)</code> runs the <b>constructor</b> and creates an <b>object</b>, an <b>instance</b> of Pet, with its own values.", s: { i: 1 } },
    { cap: "A second instance with different values. Each object has its own copy of the properties.", s: { i: 2 } },
    { cap: "A third. Creating objects from a class is called <b>instantiation</b>.", s: { i: 3 } },
    { cap: "Changing p2's name changes only p2. The objects share the class's methods but not their data.", s: { i: 4 } }] });
})();

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); let o = "";
    o += SV.rect(30, 50, 170, 140, "cell", { rx: 8 }) + SV.text(115, 40, "rest of the program", "sm", { "text-anchor": "middle" }) + SV.text(115, 110, "main program", "lbl bd", { "text-anchor": "middle" });
    o += SV.rect(390, 30, 340, 195, "f2", { rx: 10, ...op(0.18) }) + SV.rect(390, 30, 340, 195, "ax", { rx: 10, fill: "none" }) + SV.text(560, 22, "object of class Pet", "sm", { "text-anchor": "middle" });
    o += memCell(440, 60, "Age", k >= 3 ? 12 : 4, k >= 1 ? "cell-ok" : "f3", 1, 160) + SV.text(440, 52, "PRIVATE Age : INTEGER", "sm");
    o += SV.rect(360, 60, 18, 40, "cell-no", { rx: 3, ...op(k >= 1 ? 1 : 0) });
    o += SV.rect(440, 112, 170, 34, "f1", { rx: 6, ...op(0.55) }) + SV.text(525, 134, "GetAge()", "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:13px" });
    o += SV.rect(440, 156, 170, 34, "f1", { rx: 6, ...op(0.55) }) + SV.text(525, 178, "SetAge(n)", "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:13px" });
    if (k === 2) o += arrow(200, 90, 355, 80, "r", "c3", 1) + SV.text(210, 80, "pet.Age ✗", "lbl bd c3") + SV.text(210, 130, "blocked: the property is private", "sm");
    if (k === 3) o += arrow(200, 120, 440, 128, "r", "c1", 1) + SV.text(210, 112, "pet.GetAge()", "lbl bd") + arrow(525, 100, 525, 110, "d", "c2", 1);
    if (k === 4) o += arrow(200, 120, 440, 172, "r", "c1", 1) + SV.text(210, 112, "pet.SetAge(12)", "lbl bd") + SV.text(560, 212, "SetAge checks 0 to 30, then stores 12", "sm", { "text-anchor": "middle" });
    if (k === 5) o += arrow(200, 120, 440, 172, "r", "c1", 1) + SV.text(210, 112, "pet.SetAge(-3)", "lbl bd") + SV.text(560, 212, "rejected: -3 is not valid, Age stays 12", "sm", { "text-anchor": "middle" });
    return o;
  };
  Lib.stepper($("#stB"), { w: 760, h: 240, label: "Encapsulation with a getter and a setter", base: { i: 0 }, draw, tween: 500, dwell: 3800, steps: [
    { cap: "A Pet object stores an <b>Age</b>. The programmer declares it <code>PRIVATE</code> and writes two public methods.", s: { i: 0 } },
    { cap: "Because Age is private, a wall surrounds it. Only methods of the class can reach it.", s: { i: 1 } },
    { cap: "Code outside the class that tries to read or write <code>Age</code> directly is <b>blocked</b>.", s: { i: 2 } },
    { cap: "The <b>getter</b> <code>GetAge()</code> is the allowed way to read the value.", s: { i: 3 } },
    { cap: "The <b>setter</b> <code>SetAge(n)</code> is the allowed way to change it. The method can check the value first.", s: { i: 4 } },
    { cap: "A silly value is rejected, so the data stays valid. That is the point of <b>encapsulation</b>.", s: { i: 5 } }] });
})();

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); let o = "";
    o += classBox(230, 10, 300, "Yarn (parent)", ["Name, Colour, BatchCode : STRING", "Weight, NumberBalls : INTEGER", "Type : STRING", "Constructor()  EditNumberBalls()", "YarnInfo()"], 1, "f1", 19);
    const kids = [["Acrylic", "Soft : BOOLEAN", "Constructor()", "YarnInfo()"], ["Wool", "WoolType : STRING", "Constructor()", "YarnInfo()"], ["Mix", "Percentage : INTEGER", "Constructor()", "YarnInfo()  (overrides)"]];
    kids.forEach((c, n) => {
      const v = k > n ? 1 : 0, x = 20 + n * 245; if (!v) return;
      o += classBox(x, 160, 225, c[0] + " (child)", [c[1], c[2], c[3]], 1, ["f2", "f3", "f4"][n], 19) + arrow(x + 112, 160, 380, 142, "u", "c1", 1);
    });
    return o;
  };
  Lib.stepper($("#stC"), { w: 760, h: 270, label: "Inheritance with three child classes", base: { i: 0 }, draw, tween: 500, dwell: 4000, steps: [
    { cap: "The <b>parent class</b> Yarn holds everything the three types share: name, colour, batch code, weight, number of balls, type, and the methods.", s: { i: 0 } },
    { cap: "<b>Acrylic</b> inherits all of it and adds only what is new: <code>Soft : BOOLEAN</code>. The arrow points from the child to the parent.", s: { i: 1 } },
    { cap: "<b>Wool</b> inherits the same and adds its own <code>WoolType</code> (lamb, merino or alpaca).", s: { i: 2 } },
    { cap: "<b>Mix</b> adds <code>Percentage</code> of acrylic. Each child has its own constructor and its own <code>YarnInfo()</code> because each shows extra data. Nothing in Yarn is written three times.", s: { i: 3 } }] });
})();

(function () {
  const animals = [["Dog", "Woof"], ["Cat", "Meow"], ["Cow", "Moo"]];
  const draw = (s) => {
    const k = Math.round(s.i); let o = "";
    o += codeList(20, 30, ["FOR EACH a IN Animals", "   OUTPUT a.Speak()", "NEXT a"], k === 0 ? -1 : 1, 1, 34, 230);
    animals.forEach((a, n) => {
      const x = 310 + n * 140, on = k === n + 1;
      o += classBox(x, 40, 120, a[0], ["Speak()"], 1, on ? "f3" : "f1", 20);
      if (k > n) o += SV.text(x + 60, 140, '"' + a[1] + '"', "lbl bd", { "text-anchor": "middle", style: "font-size:20px" }) + arrow(x + 60, 100, x + 60, 124, "d", "c2", 1);
    });
    if (k === 4) o += SV.text(310, 190, "one call, three different results", "lbl bd t3");
    return o;
  };
  Lib.stepper($("#stD"), { w: 760, h: 215, label: "Polymorphism: the same method call", base: { i: 0 }, draw, tween: 400, dwell: 3200, steps: [
    { cap: "Dog, Cat and Cow each <b>redefine</b> the method <code>Speak()</code>. The loop calls the same method name on every object.", s: { i: 0 } },
    { cap: "On the Dog object, <code>Speak()</code> runs the Dog version.", s: { i: 1 } },
    { cap: "On the Cat object, the same call runs the Cat version.", s: { i: 2 } },
    { cap: "On the Cow object, the Cow version.", s: { i: 3 } },
    { cap: "That is <b>polymorphism</b>: the same method name, redefined in derived classes, behaves differently depending on the object.", s: { i: 4 } }] });
})();

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); let o = "";
    o += classBox(30, 20, 200, "Card", ["Number : INTEGER", "Colour : STRING", "GetNumber()", "GetColour()"], 1, "f2");
    if (k >= 1) {
      o += SV.rect(300, 20, 430, 150, "cell", { rx: 8 }) + SV.rect(300, 20, 430, 28, "f1", { rx: 8, ...op(0.6) }) + SV.text(515, 39, "object of class Hand", "lbl bd", { "text-anchor": "middle", style: "font-size:15px" });
      for (let c = 0; c < 5; c++) o += SV.rect(315 + c * 82, 64, 70, 70, "f2", { rx: 6, ...op(0.45) }) + SV.text(350 + c * 82, 92, "Card", "sm", { "text-anchor": "middle" }) + SV.text(350 + c * 82, 112, (c + 1) + " red", "sm", { "text-anchor": "middle", style: "font-size:11px" });
      o += SV.text(315, 156, "Cards : ARRAY[0:9] OF Card", "sm", { style: "font-family:var(--mono);font-size:11.5px" });
    }
    if (k >= 2) o += SV.text(30, 200, "Hand HAS Cards: containment (aggregation)", "lbl bd t3") + SV.text(30, 226, "Parrot IS AN Animal: inheritance", "lbl bd t1", op(k >= 3 ? 1 : 0.3));
    return o;
  };
  Lib.stepper($("#stE"), { w: 760, h: 240, label: "Containment: a hand of cards", base: { i: 0 }, draw, tween: 500, dwell: 3800, steps: [
    { cap: "A <b>Card</b> class stores a number and a colour.", s: { i: 0 } },
    { cap: "A <b>Hand</b> object holds an array of <b>Card</b> objects. The Hand class has a property whose type is another class.", s: { i: 1 } },
    { cap: "This is <b>containment (aggregation)</b>: a Hand <i>has</i> cards.", s: { i: 2 } },
    { cap: "Compare inheritance: a Parrot <i>is an</i> Animal. Ask 'has a' or 'is a' to choose between them.", s: { i: 3 } }] });
})();

/* Lab 1 */
(function () {
  let priv = true, age = 4;
  const paint = (msg) => {
    $$("#vB button").forEach((b, i) => b.classList.toggle("pri", (i === 0) === priv));
    $("#v1").textContent = age; $("#vv").textContent = msg || (priv ? "Age is PRIVATE: only GetAge() and SetAge() can reach it." : "Age is PUBLIC: any code can reach it directly.");
  };
  $("#vB").innerHTML = '<button class="b">PRIVATE Age</button><button class="b">PUBLIC Age</button>';
  $$("#vB button").forEach((b, i) => (b.onclick = () => { priv = i === 0; paint(); }));
  $("#vR").onclick = () => paint(priv ? "Blocked: Age is private, so outside code cannot read it directly." : "Read directly: " + age + ". It works, but nothing protects the data.");
  $("#vG").onclick = () => paint("GetAge() returns " + age + ". This is the allowed way to read a private property.");
  $("#vN").onclick = () => { if (priv) return paint("Blocked: outside code cannot set a private property directly."); age = 25; paint("Age is now 25. Directly set, so no check was made."); };
  $("#vS").onclick = () => { age = 25; paint("SetAge(25): checked (0 to 30 is allowed) and stored. Age is 25."); };
  $("#vC").onclick = () => paint(priv ? "SetAge(-3): the setter rejects it, so Age stays " + age + ". The setter protects the data." : "SetAge(-3): the setter rejects it. But with a PUBLIC Age, outside code could still set -3 directly, which is why properties are made private.");
  paint();
})();

/* Lab 2 */
(function () {
  const parent = ["Name, Colour, BatchCode : STRING", "Weight, NumberBalls, Type", "EditNumberBalls()"];
  const rows = [
    ["Yarn (parent)", "Everything: Name, Colour, BatchCode, Weight, NumberBalls, Type and the methods Constructor(), EditNumberBalls(), YarnInfo()", "Nothing: this is the parent class", "Nothing to override"],
    ["Acrylic", "All of Yarn: " + parent.join("; "), "Soft : BOOLEAN; its own Constructor()", "YarnInfo(), to show the Soft value as well"],
    ["Wool", "All of Yarn: " + parent.join("; "), "WoolType : STRING; its own Constructor()", "YarnInfo(), to show the wool type"],
    ["Mix", "All of Yarn: " + parent.join("; "), "Percentage : INTEGER; its own Constructor()", "YarnInfo(), to show the percentage of acrylic"]
  ];
  btnTable("iB", "iO", rows, ["Class", "Inherited", "Adds", "Overrides"]);
})();

btnTable("eB", "eO", [
  ["Class", "A template that defines the properties and methods of its objects", "Pet", "Calling it 'an object'"],
  ["Object / instance", "One occurrence of a class, with its own values", "p1 ← NEW Pet(...)", "Saying an instance is a class"],
  ["Constructor", "The method that runs when an object is created and sets its starting values", "PUBLIC PROCEDURE NEW(...)", "Forgetting it takes parameters for the values"],
  ["Encapsulation", "Properties and methods together in one class; data private and reached only through the class's own methods", "PRIVATE Age : INTEGER", "'Hiding' without saying how it is accessed"],
  ["Getter / setter", "A getter returns the value of a property; a setter updates it", "GetAge() / SetAge(n)", "Giving a getter a parameter"],
  ["Inheritance", "A derived class takes the properties and methods of a parent class", "CLASS Parrot INHERITS Animal", "Arrows the wrong way round"],
  ["Polymorphism", "A method with the same name is redefined in derived classes, so behaviour differs by class", "Speak() in Dog and Cat", "Writing 'many forms' only"],
  ["Containment (aggregation)", "A class contains objects of another class: 'has a'", "Hand contains Cards", "Confusing it with inheritance"]
], ["Term", "Meaning", "Example", "Trap"]);
''' + CLASSIFY("cl1", "What kind of class member is each item?", ["Attribute", "Constructor", "Getter", "Setter", "Method (other)"],
  [("PetName : STRING", 0), ("NEW(NewName : STRING)", 1), ("GetPetName()", 2), ("SetPetName(NewName : STRING)", 3), ("EditNumberBalls()", 4), ("YearBorn : INTEGER", 0), ("__init__(self, name)", 1), ("GetYearBorn()", 2), ("SetPriority(Urgency : INTEGER)", 3), ("Description()", 4)],
  "Attributes have a data type and no brackets. Getters start Get and take nothing. Setters start Set and take the new value. The constructor creates the object.") + CLASSIFY("cl2", "Is the relationship inheritance (is a) or containment (has a)?", ["Inheritance", "Containment"],
  [("A Parrot and an Animal", 0), ("A Hand and its Cards", 1), ("A Manager and an Employee", 0), ("A Library and its Books", 1), ("A Car and its Engine", 1), ("A Helicopter and a Vehicle", 0), ("A Garage and its Cars", 1), ("A Circle and a Shape", 0)],
  "Try 'is a': a Parrot is an Animal. Try 'has a': a Hand has Cards.") + ORDER(
  "Put the steps for designing classes in order.",
  ["Find the things the problem describes: each kind is a class", "List the data each class stores, with data types", "List the actions each class performs: its methods", "Look for shared parts and put them in a parent class", "Make the properties private and add getters and setters where needed"],
  "Things, data, actions, sharing, access.") + MATCH([
  ["Constructor", "Sets up a new object when it is created"], ["Getter", "Returns the value of a property"], ["Setter", "Updates the value of a property"], ["Polymorphism", "The same method redefined in derived classes"], ["Instance", "An occurrence of an object made from a class"]]) + CALC([
  {"q": "A class has 6 properties, all private, all of which must be readable from outside. How many getters are needed?", "a": 6, "unit": "", "tol": 0.01, "hint": "One getter per readable property.", "sol": "<b>6</b>."},
  {"q": "A class has 6 properties. The ID never changes; the other 5 can be updated. How many setters?", "a": 5, "unit": "", "tol": 0.01, "hint": "No setter for the ID.", "sol": "<b>5</b>."},
  {"q": "Yarn has 6 properties and 3 methods. Mix inherits from Yarn and adds 1 property. How many properties does a Mix object have?", "a": 7, "unit": "", "tol": 0.01, "hint": "Inherited plus new.", "sol": "<b>7</b>."},
  {"q": "A Hand contains 5 Card objects. Each Card has 2 properties. How many Card properties exist across the hand?", "a": 10, "unit": "", "tol": 0.01, "hint": "5 × 2.", "sol": "<b>10</b>."},
  {"q": "Classes: Animal, Dog, Cat, Cow, with Dog, Cat and Cow inheriting from Animal. How many inheritance arrows are drawn?", "a": 3, "unit": "", "tol": 0.01, "hint": "One from each child.", "sol": "<b>3</b>."},
  {"q": "Three objects are created from the class Pet. How many classes are there?", "a": 1, "unit": "", "tol": 0.01, "hint": "Many objects, one class.", "sol": "<b>1</b>."}]) + MCQ([
  ("What is encapsulation?", ["Writing code in a class", "Keeping data private so it can only be accessed through the class's own methods", "Creating an object", "Copying a class"], 1, "Data and methods together, with the data reached only through methods."),
  ("What is a setter?", ["A method that returns a property", "A method that updates the value of a property", "A method that creates an object", "A private property"], 1, "A setter updates; a getter returns."),
  ("In a class diagram, which is a getter?", ["SetPriority(Urgency : INTEGER)", "GetPriority()", "Priority : INTEGER", "Constructor()"], 1, "Getters take no parameter and start with Get."),
  ("What does polymorphism mean?", ["A class has many objects", "A method is redefined in derived classes, behaving differently", "A class has many properties", "A property has many types"], 1, "Same method name, different behaviour."),
  ("Which relationship is containment?", ["A Parrot is an Animal", "A Hand has Cards", "A Manager is an Employee", "A Circle is a Shape"], 1, "Has a."),
  ("What is an instance?", ["A template", "A type of method", "An occurrence of an object created from a class", "A private property"], 2, "Instances are created from classes.")], "qz1") + CARDS([
  ("Class", "A template for objects: their properties and methods."), ("Object / instance", "One occurrence of a class, with its own values."), ("Constructor", "Sets up a new object. NEW in pseudocode, __init__ in Python."), ("Encapsulation", "Data private; accessed only by the class's own methods."),
  ("Getter", "Method that returns the value of a property."), ("Setter", "Method that updates the value of a property."), ("Inheritance", "A derived class takes properties and methods of a parent class."), ("Polymorphism", "Same method name redefined in derived classes."), ("Containment", "One class holds objects of another: has a.")])

build("ac2012", "ac-20-1-2-oop-terminology-class-design", "Object-Oriented Programming: Terminology and Class Design", EYA("20.1.2"),
  "Classes, objects, encapsulation, getters and setters, inheritance, polymorphism and containment; how to read, complete and design class diagrams; animations, labs and the real past paper questions on OOP.",
  dict(sub=CBK("Chapter 20 · Further programming, section 20.1 Programming paradigms"), **tabs(learn, watch, explore, practise, real, exam, tips)), js)
