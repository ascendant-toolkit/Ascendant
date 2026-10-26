"""A Level CS syllabus 13.1.2: composite user-defined types (record, set, class) and choosing a type. Run: python3 tools/artifact-kit/mk_ac1312.py"""
from ak20 import *

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>A <b>composite</b> user-defined type is built from other types and holds more than one value under a single identifier. A <b>record</b> groups <b>fields</b> of different types (a pet's name, age and gender), written between <code>TYPE</code> and <code>ENDTYPE</code> with a <code>DECLARE</code> for each field, and you reach a field with dot notation. A <b>set</b> is an unordered collection of unique values of one type, which supports union, intersection and difference. A <b>class</b> bundles fields with the methods that act on them, and its instances are objects. The skill the exam tests is to <b>choose and design</b> the right type: pick the fields, give each the most appropriate data type, and reuse an enumerated type where the values come from a fixed list.</p></div>

  <h2>1 · Records</h2>
  <p>A record holds the data about <b>one thing</b>, one field for each item. The fields can have different types, including an enumerated type you have declared earlier.</p>
  <div class="code">''' + pc('''TYPE Aircraft = (C300, C350, D242, E757, X380)      // an enumerated type used below

TYPE Flight
   DECLARE FlightNumber : STRING
   DECLARE Destination : STRING
   DECLARE DepartureDate : DATE
   DECLARE AircraftType : Aircraft                  // a field whose type is the enumerated type
ENDTYPE

DECLARE Flight1 : Flight                            // a variable that holds one record
Flight1.FlightNumber ← "XA782"                      // dot notation: variable.field
Flight1.Destination ← "Cambridge"
Flight1.DepartureDate ← 12/12/2022
Flight1.AircraftType ← C350                         // an enumerated value, no quotation marks''') + '''</div>
  <ul>
    <li>A <b>declaration</b> of the type only describes it. <b>DECLARE Flight1 : Flight</b> creates the variable.</li>
    <li>Each field is assigned separately with <b>variable.field</b>.</li>
    <li>Strings go in double quotation marks, characters in single quotation marks, dates are written as given, and enumerated values have no quotation marks.</li>
    <li>For many records use an array: <code>DECLARE Flights : ARRAY[1:50] OF Flight</code> and <code>Flights[3].Gate ← "N03"</code>.</li>
    <li>A type can be changed. To make a field's values come from a fixed list, declare an enumerated type and replace that field's declaration: <code>DECLARE Gate : GateID</code>. A range can also be stated: <code>DECLARE NumberOfCopies : 1 .. 10</code>.</li>
  </ul>
  <div class="code">''' + pc('''from dataclasses import dataclass
from datetime import date

@dataclass
class Flight:                           # Python's closest equivalent of a record
    FlightNumber: str
    Destination: str
    DepartureDate: date
    AircraftType: str

Flight1 = Flight("XA782", "Cambridge", date(2022, 12, 12), "C350")
print(Flight1.Destination)''') + '''</div>

  <h2>2 · Choosing the data type for each field</h2>
  <div class="tw"><table class="t">
    <tr><th>The data item</th><th>Type</th><th>Reason</th></tr>
    <tr><td>Name, address, title, an identity code with letters and digits (<code>SB2789</code>), a telephone number</td><td><b>STRING</b></td><td>Text, or digits that are not used in arithmetic. A telephone number has a leading 0 that an integer would lose</td></tr>
    <tr><td>A year, a count, a running time in minutes, a position</td><td><b>INTEGER</b></td><td>Whole numbers</td></tr>
    <tr><td>A price, a frequency, a fee</td><td><b>REAL</b></td><td>Has a fractional part</td></tr>
    <tr><td>Yes or no: fees paid, is a primary colour</td><td><b>BOOLEAN</b></td><td>Two possible values</td></tr>
    <tr><td>A date of birth, date of departure</td><td><b>DATE</b></td><td>A calendar date</td></tr>
    <tr><td>A single letter such as M or F</td><td><b>CHAR</b></td><td>One character</td></tr>
    <tr><td>A field with a fixed list of choices (format: DVD, Blu-ray, 4K; taxi code)</td><td><b>Enumerated type</b></td><td>The type only allows the listed values</td></tr>
  </table></div>
  <div class="tip"><b class="h">Naming and order</b>Use a field name that says what it holds (<code>DateOfDeparture</code>), start with <code>TYPE Name</code> and finish with <code>ENDTYPE</code>, and put <code>DECLARE</code> on every field. Use the most appropriate type for each one: the mark scheme checks them one by one.</div>

  <h2>3 · Set types</h2>
  <p>A <b>set</b> is a composite type for a collection of values that are all of <b>one data type</b>. The elements are <b>unordered</b>, there are <b>no duplicates</b>, and <b>set operations</b> such as union and intersection can be applied. The declaration gives the type of the members; <code>DEFINE</code> then gives a variable its values.</p>
  <div class="code">''' + pc('''TYPE Numbers = SET OF INTEGER
DEFINE EvenNumbers (2, 4, 6, 8, 10, 12) : Numbers

TYPE SymbolSet = SET OF CHAR
DEFINE Operators ('+', '-', '*', '/', '^') : SymbolSet''') + '''</div>
  <div class="tw"><table class="t">
    <tr><th>Operation</th><th>Result</th><th>Example with A = {1, 2, 3} and B = {3, 4}</th></tr>
    <tr><td><b>Union</b></td><td>Everything in either set</td><td>{1, 2, 3, 4}</td></tr>
    <tr><td><b>Intersection</b></td><td>Only what is in both</td><td>{3}</td></tr>
    <tr><td><b>Difference</b> (A − B)</td><td>In A but not in B</td><td>{1, 2}</td></tr>
    <tr><td><b>Membership</b></td><td>Is a value in the set?</td><td>2 is in A: TRUE</td></tr>
  </table></div>
  <div class="code">''' + pc('''A = {1, 2, 3}
B = {3, 4}
print(A | B)          # union: {1, 2, 3, 4}
print(A & B)          # intersection: {3}
print(A - B)          # difference: {1, 2}
print(2 in A)         # membership: True''') + '''</div>

  <h2>4 · Class / object as a composite type</h2>
  <p>A <b>class</b> is a composite type that holds <b>fields and the methods</b> that work on them. Each object made from it is an instance. Unlike a record, a class can keep its data private and be extended by inheritance. This is covered fully in the OOP pages of chapter 20.</p>

  <h2>5 · Defining a composite type</h2>
  <p><i>A composite type refers to at least one other data type in its definition; it holds several values under a single identifier. The data types can be primitive or user-defined.</i> An example answer is: a record, a set, or a class/object.</p>

  <h2>6 · Common ways to lose marks</h2>
  <ul>
    <li>Leaving out <code>ENDTYPE</code>, or <code>DECLARE</code> on a field.</li>
    <li>Using a STRING for a number that is used in calculations, or an INTEGER for a telephone number or an identity code.</li>
    <li>Not using the enumerated type that the question tells you to use for a field.</li>
    <li>Forgetting to declare a variable of the record type before assigning to it, or writing the field name without the variable name.</li>
    <li>Quotation marks round an enumerated value, or no quotation marks round a string.</li>
    <li>Describing a set as "an ordered list". It is unordered, with no repeats.</li>
    <li>For a set: leaving out <code>SET OF</code>, <code>DEFINE</code>, the values in brackets, or the <code>: type</code> at the end.</li>
  </ul>
'''

watch = '''
  <h2>1 · Building and filling a record</h2>
  <p>Press Play, or click the steps.</p>
  <div id="stA"></div>
  <h2>2 · An array of records</h2>
  <div id="stB"></div>
  <h2>3 · Set operations</h2>
  <div id="stC"></div>
  <h2>4 · Choosing the type for each field</h2>
  <div id="stD"></div>
'''

explore = '''
  <h2>Lab 1 · Set operations</h2>
  <p>Click numbers to put them in set A or set B, then choose an operation. Duplicates can never occur in a set.</p>
  <div class="card"><div class="btnrow" id="sA"></div><div class="btnrow" id="sB"></div><div class="btnrow" id="sO"></div><div class="readout"><div><small>Set A</small><strong id="s1"></strong></div><div><small>Set B</small><strong id="s2"></strong></div><div><small>Result</small><strong id="s3"></strong></div></div><div class="verdict" id="sV"></div></div>

  <h2>Lab 2 · Choose the type for each field</h2>
  <p>For each field of the record, choose the most appropriate type. The answer is checked against the mark scheme's choices.</p>
  <div class="card"><div id="tB" class="btnrow"></div><div id="tO"></div><div class="verdict" id="tV"></div></div>

  <h2>Lab 3 · Spot the mistake in a record declaration</h2>
  <div class="card"><div id="mB" class="btnrow"></div><div id="mO"></div></div>
'''

practise = '''
  <h2>1 · Which data type fits the field?</h2><div id="cl1" class="card"></div>
  <h2>2 · Record, set or class?</h2><div id="cl2" class="card"></div>
  <h2>3 · Put the steps for creating and using a record in order</h2><div id="o1" class="card"></div>
  <h2>4 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>5 · Set results and counts</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("A school's student records", "Each student is a record with name, date of birth, form, a Boolean for permission to go on trips, and a field of type Subject for the favourite subject. An array holds the whole year group.", "records group different types of data for one item; arrays hold many records.") +
rw("Airport departures board", "Each flight is a record: flight number, destination, date, gate and airline. The gate is an enumerated type because only certain gates exist.", "a record with an enumerated field.") +
rw("Followers and common interests", "A social network can treat each person's interests as a set. The intersection of two people's sets shows what they have in common and the union shows everything either likes.", "set operations: union and intersection.") +
rw("A game character", "A Character has a name, position and strength together with methods to move and fight. It is made as a class so each character is an object with its own data.", "a class is a composite type with methods.") +
rw("A video library", "A video record has an identity code (STRING), title, year (INTEGER), purchase date (DATE), format and running time. The format is chosen from a fixed list, so it is a good enumerated type.", "choose the most appropriate type for each field.")
)

where = [
  ("M/J 2021", "31, 32, 33", "2(c)", "4", "Declare the composite type ClubMeet using two enumerated types"),
  ("M/J 2022", "31, 33", "1", "2 + 1 + 2 + 3", "LibraryRecord: assign fields, change a field to a range and an array, define composite"),
  ("M/J 2022", "32", "1(a), (b)", "2 + 3", "BuildingRecord: assign fields and add an enumerated type"),
  ("O/N 2022", "31, 33", "3(d)", "1 + 3", "Declare a Pet record variable and store a pet"),
  ("O/N 2022", "32", "4", "2 + 4 + 1 + 3", "Declare the Aircraft enumerated type, the Flight record, a variable and assign it"),
  ("M/J 2023", "32", "6(a)", "4", "Declare the composite type TAppointments"),
  ("M/J 2024", "31, 33", "3(b)", "4", "Declare the record type FootballClub"),
  ("M/J 2024", "32", "3(b)", "4", "Declare the set type EvenNumbers"),
  ("O/N 2024", "31, 33", "6", "3 + 4", "Describe the set type; declare SymbolSet"),
  ("M/J 2025", "31", "1", "2 + 4", "Declare the enumerated Vehicle and the composite Booking"),
  ("M/J 2025", "32", "1", "3 + 2 + 1", "Departure record: assign values, declare GateID, change the field"),
  ("M/J 2025", "33", "1(a), (b)", "4 + 2", "Declare VideoLibrary; choose an enumerated field"),
  ("O/N 2025", "31", "1", "1 + 2 + 2 + 1", "ClubMember record variable, assignments and an enumerated Activity"),
  ("O/N 2025", "32", "1", "1 + 2 + 2 + 1", "Car record variable, assignments and an enumerated Body"),
  ("O/N 2025", "33", "1(b)", "4", "Declare ColourData using an enumerated Spectrum")]

past = '''  <p class="note">Declaring a record and giving it values is asked in almost every Paper 3, with enumerated fields and sets, so the exam tab here is long. The enumerated types and pointer types used are on the previous page. Questions are reworded from the papers; check the original paper and mark scheme for the exact wording.</p>

  <h3>Declaring a record type</h3>
''' + peq(SRC("s21", "31, 32, 33", "Q2(c)"), "4 marks", "Define",
  "Define, using pseudocode, the composite data type ClubMeet. This will hold data about club members that includes: first name and last name; the two days they attend, one on a school day and one not on a school day. Use the enumerated types you created in part (b): SchoolDay = (Monday ... Friday) and WeekEnd = (Saturday, Sunday).",
  "Four fields, with the two day fields using the enumerated types.",
  "<p>Four marks: " + mks(["TYPE ClubMeet and ENDTYPE correct", "DECLARE FirstName and DECLARE LastName with the correct data types", "DECLARE Schoolday with the type SchoolDay", "DECLARE Weekend with the type WeekEnd"]) + "</p>" + pc('''TYPE ClubMeet
   DECLARE FirstName : STRING
   DECLARE LastName : STRING
   DECLARE Schoolday : SchoolDay
   DECLARE Weekend : WeekEnd
ENDTYPE'''),
  "Giving the day fields type STRING instead of the enumerated types the question tells you to use.") + peq(SRC("s24", "31, 33", "Q3(b)"), "4 marks", "Write",
  "Write pseudocode statements to declare the record data type FootballClub to hold data about football clubs in a league, to include: name of team; date team joined the league; main telephone number; name of the manager; number of members; current position in the league.",
  "Six fields. One mark for the TYPE and ENDTYPE, then one for every two correct declarations.",
  "<p>" + mks(["TYPE FootballClub and ENDTYPE correct", "two correct declarations", "two more correct declarations", "the last two correct declarations"]) + "</p>" + pc('''TYPE FootballClub
   DECLARE TeamName : STRING
   DECLARE DateOfJoining : DATE
   DECLARE MainTelephone : STRING
   DECLARE ManagerName : STRING
   DECLARE NumberOfMembers : INTEGER
   DECLARE LeaguePosition : INTEGER
ENDTYPE'''),
  "Storing the telephone number as an INTEGER. A telephone number is a STRING.") + peq(SRC("s23", "32", "Q6(a)"), "4 marks", "Write",
  "Write pseudocode statements to declare the composite data type TAppointments to hold data about patients for a dental clinic. It will include for each patient: name (first name and last name); date of birth; telephone number; date of last appointment; date of next appointment; all treatments are complete (yes or no).",
  "The 'yes or no' is a BOOLEAN. Dates are DATE. Names can be separate fields or one.",
  "<p>One mark for TYPE ... ENDTYPE and one for every two correct declarations: " + mks(["TYPE TAppointments and ENDTYPE", "declarations for the name fields", "date of birth and telephone number", "last appointment, next appointment and the BOOLEAN"]) + "</p>" + pc('''TYPE TAppointments
   DECLARE Name : STRING
   DECLARE DateOfBirth : DATE
   DECLARE Telephone : STRING
   DECLARE LastAppointment : DATE
   DECLARE NextAppointment : DATE
   DECLARE TreatmentsComplete : BOOLEAN
ENDTYPE'''),
  "Using STRING for the yes or no field. A two-valued choice is a BOOLEAN.") + peq(SRC("s25", "33", "Q1(a), (b)"), "4 + 2 marks", "Write / Identify",
  "A programmer is writing a program to manage a video library. (a) Write pseudocode statements to declare the composite data type VideoLibrary to hold data about each video, including: identity code (any combination of letters and numbers); title; year released; date purchased; format (for example DVD, Blu-ray, 4K, MP4); running time (minutes). Use the most appropriate data type in each case. (b) Identify one field in VideoLibrary that could be an efficient enumerated data type and give a reason for your choice.",
  "(a) check each type. (b) the field with a fixed range of values.",
  "<p><b>(a)</b> Four marks: " + mks(["TYPE VideoLibrary and ENDTYPE correct", "DECLARE used correctly for every field", "the three STRING fields correct", "the other three fields correct (INTEGER, DATE, INTEGER)"]) + "</p>" + pc('''TYPE VideoLibrary
   DECLARE VideoID : STRING
   DECLARE Title : STRING
   DECLARE ReleaseYear : INTEGER
   DECLARE PurchaseDate : DATE
   DECLARE VideoFormat : STRING
   DECLARE RunningTime : INTEGER
ENDTYPE''') + "<p><b>(b)</b> " + mks(["VideoFormat", "because this field can have a fixed range of possible values"], "a") + "</p>", None) + peq(SRC("w25", "33", "Q1(b)"), "4 marks", "Write",
  "ColourData is a composite data type to store definitions of colours. Write pseudocode statements to declare ColourData to hold these fields (example data in brackets): ColourCode (XYZ12345), Colour (Red), Wavelength (650), Frequency (4.62), PrimaryColour (Yes). Use the most appropriate data type in each case, including the enumerated data type Spectrum for the colour.",
  "XYZ12345 is a STRING. 650 is whole. 4.62 has a fractional part. Yes or No is a BOOLEAN.",
  "<p>Four marks: " + mks(["TYPE ColourData and ENDTYPE correct", "DECLARE used correctly in all the declarations", "correct use of Spectrum for the colour", "the other four declarations correct (STRING, INTEGER, REAL, BOOLEAN)"]) + "</p>" + pc('''TYPE ColourData
   DECLARE ColourCode : STRING
   DECLARE Colour : Spectrum
   DECLARE Wavelength : INTEGER
   DECLARE Frequency : REAL
   DECLARE PrimaryColour : BOOLEAN
ENDTYPE'''),
  "Using INTEGER for Frequency (4.62 has a fractional part) or STRING for the Yes/No.") + peq(SRC("s25", "31", "Q1"), "2 + 4 marks", "Write",
  "A programmer is writing a program to manage bookings for a small taxi company. (a) Write a pseudocode statement to declare the enumerated data type Vehicle to hold the identity code of each taxi: M100, M230, T101, T102, T120, T150. (b) Write pseudocode statements to declare the composite data type Booking to hold: booking number (any combination of letters and numbers); destination; client name; client telephone number; date of departure; address for pick-up; the identity code of the taxi used. Use the most appropriate data type in each case, including the enumerated type from part (a).",
  "Seven fields; the taxi field has the enumerated type.",
  "<p><b>(a)</b> " + mks(["TYPE Vehicle =", "(M100, M230, T101, T102, T120, T150)"]) + "</p><p><b>(b)</b> Four marks: " + mks(["TYPE Booking and ENDTYPE correct", "DECLARE used correctly for every field", "any four fields correct", "the remaining fields correct"]) + "</p>" + pc('''TYPE Vehicle = (M100, M230, T101, T102, T120, T150)

TYPE Booking
   DECLARE BookingNumber : STRING
   DECLARE Destination : STRING
   DECLARE ClientName : STRING
   DECLARE ClientTelephone : STRING
   DECLARE DateOfDeparture : DATE
   DECLARE PickupAddress : STRING
   DECLARE TaxiUsed : Vehicle
ENDTYPE'''),
  "Using INTEGER for the booking number. It can contain letters, so it is a STRING.") + peq(SRC("w22", "32", "Q4"), "2 + 4 + 1 + 3 marks", "Write",
  "A program to manage regular flight details at an airport requires some user-defined data types. (a) Write pseudocode statements to declare the enumerated data type Aircraft: C300, C350, D242, E757, X380. (b) Write pseudocode statements to declare the composite data type Flight to hold: flight number (any combination of letters and numbers); destination; date of departure; type of aircraft used. Use the enumerated type from (a). (c)(i) Write the statement to set up a variable for one record of Flight. (ii) Store in it: flight number XA782, destination Cambridge, date of departure 12/12/2022, type of aircraft C350. Use the field names you created in (b).",
  "(c)(ii) one assignment for each field, with the enumerated value unquoted.",
  "<p><b>(a)</b> " + mks(["TYPE Aircraft =", "(C300, C350, D242, E757, X380)"]) + " <b>(b)</b> Four marks: " + mks(["TYPE Flight and ENDTYPE", "FlightNumber and Destination as STRING", "DepartureDate as DATE", "AircraftType as Aircraft"], "a") + " <b>(c)(i)</b> " + mks(["DECLARE Flight1 : Flight"]) + "</p>" + pc('''TYPE Aircraft = (C300, C350, D242, E757, X380)

TYPE Flight
   DECLARE FlightNumber : STRING
   DECLARE Destination : STRING
   DECLARE DepartureDate : DATE
   DECLARE AircraftType : Aircraft
ENDTYPE

DECLARE Flight1 : Flight
Flight1.FlightNumber ← "XA782"
Flight1.Destination ← "Cambridge"
Flight1.DepartureDate ← 12/12/2022
Flight1.AircraftType ← C350''') + "<p><b>(c)(ii)</b> Three marks: " + mks(["both string values assigned correctly", "the date assigned correctly", "the enumerated value assigned correctly"], "a") + "</p>", None) + '''
  <h3>Giving a record values, and changing its type</h3>
''' + peq(SRC("w22", "31, 33", "Q3(d)"), "1 + 3 marks", "Write",
  "The composite data type Pet stores data about the pets of a group of students. Its fields are PetName (String), AnimalType (String), PetAge (Integer), PetGender (Char) and OwnerName (String). (i) Write the pseudocode statement to set up a variable for one record of the composite data type Pet. (ii) Write pseudocode to store the details of this pet in the variable: PetName Tibbles, AnimalType Cat, PetAge 8, PetGender M, OwnerName Jasmine Smith.",
  "DECLARE the variable first. Strings in double quotation marks, the CHAR in single quotation marks.",
  "<p><b>(i)</b> " + mks(["DECLARE Pet1 : Pet"]) + " <b>(ii)</b> " + mks(["all string values assigned correctly", "the char value assigned correctly", "the integer value assigned correctly"], "a") + "</p>" + pc('''DECLARE Pet1 : Pet
Pet1.PetName ← "Tibbles"
Pet1.AnimalType ← "Cat"
Pet1.PetAge ← 8
Pet1.PetGender ← 'M'
Pet1.OwnerName ← "Jasmine Smith"'''),
  "Writing the field without the variable name, for example <code>PetName ← \"Tibbles\"</code>.") + peq(SRC("s22", "31, 33", "Q1"), "2 + 1 + 2 + 3 marks", "Write / Explain",
  "The data type LibraryRecord is defined in pseudocode with the fields Title (STRING), Fiction (BOOLEAN), Author (STRING) and NumberOfCopies (INTEGER). A variable LibraryBook is declared as <code>DECLARE LibraryBook : LibraryRecord</code>. (a) Write pseudocode statements to assign A Level Computer Science to Title of LibraryBook, and FALSE to Fiction of LibraryBook. (b)(i) The value for NumberOfCopies must be between 1 and 10 inclusive. Write the updated line of the type definition. (ii) Every copy of every book has an accession number (an integer). Each library record will include one or more accession numbers. Write the extra line needed in the type definition. (c) A record is a user-defined composite data type. Explain what is meant by a user-defined composite data type, including an example of another.",
  "(b)(i) a range. (b)(ii) an array whose size is the number of copies. (c) refers to other types; an example such as class, set.",
  "<p><b>(a)</b> " + mks(["LibraryBook.Title ← \"A Level Computer Science\"", "LibraryBook.Fiction ← FALSE"]) + " <b>(b)(i)</b> " + mks(["DECLARE NumberOfCopies : 1 .. 10"], "a") + " <b>(ii)</b> " + mks(["DECLARE AccessionNumber : ARRAY[1:NumberOfCopies] OF INTEGER (two marks)"]) + "</p><p><b>(c)</b> " + mks(["A data type constructed by a programmer, not a primitive type", "that references at least one other data type, which may be primitive or user-defined", "Example: class / object / set"], "a") + "</p>", None) + peq(SRC("s22", "32", "Q1(a), (b)"), "2 + 3 marks", "Write",
  "The data type BuildingRecord has the fields BuildingID (INTEGER), BuildingGroup (STRING), OwnerName, BuildingAddress (STRING), DateLastSold (DATE) and PriceLastSold (REAL), and a variable BuildingRegister is declared. (a) Write pseudocode to assign 1067 to the BuildingID of BuildingRegister and house to its BuildingGroup. (b) BuildingGroup is changed to an enumerated type BuildingType with values house, bungalow, apartment and farm. (i) Write the type declaration for BuildingType. (ii) Write the new declaration for BuildingGroup. (iii) Write the new statement to assign house to BuildingGroup of BuildingRegister.",
  "After the change the value is no longer a string, so it loses its quotation marks.",
  "<p><b>(a)</b> " + mks(["BuildingRegister.BuildingID ← 1067", "BuildingRegister.BuildingGroup ← \"house\""]) + "</p><p><b>(b)</b> " + mks(["TYPE BuildingType = (house, bungalow, apartment, farm)", "DECLARE BuildingGroup : BuildingType", "BuildingRegister.BuildingGroup ← house"], "a") + "</p>", "Keeping the quotation marks round <code>house</code> in (iii). It is now an enumerated value.") + peq(SRC("w25", "31", "Q1"), "1 + 2 + 2 + 1 marks", "Write",
  "The composite record data type ClubMember has the fields Code (INTEGER), LastName, FirstName, Telephone (STRING), JoinDate (DATE), Fees (REAL) and FeesPaid (BOOLEAN). (a)(i) Write the statement to set up a variable for one record of ClubMember. (ii) Assign 984632 to Code and TRUE to FeesPaid. (b) An enumerated type Activity is needed so a new field Choice can be added. (i) Write the type declaration of Activity to hold: Badminton, Football, Golf, Snooker, Swimming, Tennis. (ii) Write the new statement required to declare Choice in ClubMember.",
  "Declare, assign, declare the enumerated type, then add the field using it.",
  "<p><b>(a)</b> " + mks(["DECLARE Member1 : ClubMember"]) + " " + mks(["Member1.Code ← 984632", "Member1.FeesPaid ← TRUE"], "a") + "</p><p><b>(b)</b> " + mks(["TYPE Activity =", "(Badminton, Football, Golf, Snooker, Swimming, Tennis)"]) + " " + mks(["DECLARE Choice : Activity"], "a") + "</p>", None) + peq(SRC("w25", "32", "Q1"), "1 + 2 + 2 + 1 marks", "Write",
  "The composite data type Car has the fields RegNumber, Make, Model, BodyStyle, Colour (all STRING), IntoStock (DATE) and Price (REAL). (a)(i) Set up a variable for one record of Car. (ii) Assign \"Blue\" to Colour and 21/10/2025 to IntoStock. (b) BodyStyle changes to an enumerated type, Body. (i) Declare Body to hold: Convertible, Hatchback, Saloon, SUV. (ii) Write the new statement to replace the declaration of BodyStyle in Car.",
  "The same pattern as the club member: declare, assign, new type, new field.",
  "<p><b>(a)</b> " + mks(["DECLARE Car1 : Car"]) + " " + mks(["Car1.Colour ← \"Blue\"", "Car1.IntoStock ← 21/10/2025"], "a") + "</p><p><b>(b)</b> " + mks(["TYPE Body =", "(Convertible, Hatchback, Saloon, SUV)"]) + " " + mks(["DECLARE BodyStyle : Body"], "a") + "</p>", None) + peq(SRC("s25", "32", "Q1"), "3 + 2 + 1 marks", "Write",
  "The composite record data type Departure represents flights from Cambridge Airport with the fields FlightNumber, Destination, Gate, Airline (STRING) and FlightDate (DATE). A variable Flight1 is declared. (a) Store these details in Flight1: SB2789, Dublin, 30/07/2025, gate N03, Cambridge Airways. (b) The data type for Gate is changed to an enumerated data type, GateID. (i) Declare GateID to hold the gate codes N01, N02, N03, W01, W02, W03, W04. (ii) Write the new statement to replace the declaration of Gate in Departure.",
  "Before the change the gate is a string. The change replaces only the declaration of Gate.",
  "<p><b>(a)</b> " + mks(["Flight1 used with the given field names", "the four string values assigned correctly", "the date assigned correctly"]) + "</p>" + pc('''Flight1.FlightNumber ← "SB2789"
Flight1.Destination ← "Dublin"
Flight1.FlightDate ← 30/07/2025
Flight1.Gate ← "N03"
Flight1.Airline ← "Cambridge Airways"''') + "<p><b>(b)</b> " + mks(["TYPE GateID =", "(N01, N02, N03, W01, W02, W03, W04)"], "a") + " " + mks(["DECLARE Gate : GateID"], "a") + "</p>", None) + '''
  <h3>Set types</h3>
''' + peq(SRC("w24", "31, 33", "Q6"), "3 + 4 marks", "Describe / Write",
  "(a) Describe the user-defined data type set. (b) Write pseudocode statements to declare the set data type SymbolSet, to hold the following set of mathematical operators, using the variable Operators: + – * / ^",
  "(a) composite, unordered, set operations, one data type. (b) TYPE ... SET OF, DEFINE, the values, and the type.",
  "<p><b>(a)</b> Any three: " + mks(["A set is a composite data type", "which includes a list of unordered elements", "set theory operations such as intersection and union can be applied to the elements", "the type of data is part of the definition and all elements have the same data type"]) + "</p><p><b>(b)</b> Four marks: " + mks(["TYPE SymbolSet =", "SET OF CHAR", "DEFINE Operators", "(the values in brackets) : SymbolSet"], "a") + "</p>" + pc('''TYPE SymbolSet = SET OF CHAR
DEFINE Operators ('+', '-', '*', '/', '^') : SymbolSet'''),
  "Writing the values as strings in double quotation marks, or leaving out the <code>: SymbolSet</code> at the end of DEFINE.") + peq(SRC("s24", "32", "Q3(b)"), "4 marks", "Write",
  "Write pseudocode statements to declare the set data type EvenNumbers to hold this set of even numbers between 2 and 12: 2, 4, 6, 8, 10, 12.",
  "Two statements: the TYPE with SET OF, and DEFINE.",
  "<p>Four marks: " + mks(["the TYPE statement fully correct", "DEFINE EvenNumbers", "the correct list of values in brackets", "the set identifier from the TYPE statement used after the colon"]) + "</p>" + pc('''TYPE Numbers = SET OF INTEGER
DEFINE EvenNumbers (2, 4, 6, 8, 10, 12) : Numbers'''), "Defining the set as an ARRAY. A set is a different composite type.")

review = req("3 marks", "Write", "A shop records each product: product code (letters and digits), name, price, number in stock and whether it is on offer. Write the pseudocode to declare the record type Product.", "Choose each type from the data.",
  "<p>" + mks(["TYPE Product and ENDTYPE correct", "ProductCode and Name as STRING; Price as REAL; Stock as INTEGER", "OnOffer as BOOLEAN"]) + "</p>" + pc('''TYPE Product
   DECLARE ProductCode : STRING
   DECLARE Name : STRING
   DECLARE Price : REAL
   DECLARE NumberInStock : INTEGER
   DECLARE OnOffer : BOOLEAN
ENDTYPE'''), "Using INTEGER for ProductCode. Codes contain letters.") + req("3 marks", "Write", "Declare an enumerated type Size (Small, Medium, Large) and add a field Size : Size... Write the declaration of the record Shirt with fields Colour (STRING) and Size (the enumerated type), a variable MyShirt, and assign Blue and Large.", "Enumerated first, then the record that uses it.",
  "<p>" + mks(["TYPE Size = (Small, Medium, Large)", "TYPE Shirt with Colour : STRING and ChosenSize : Size, and DECLARE MyShirt : Shirt", "MyShirt.Colour ← \"Blue\" and MyShirt.ChosenSize ← Large (no quotation marks)"]) + "</p>" + pc('''TYPE Size = (Small, Medium, Large)

TYPE Shirt
   DECLARE Colour : STRING
   DECLARE ChosenSize : Size
ENDTYPE

DECLARE MyShirt : Shirt
MyShirt.Colour ← "Blue"
MyShirt.ChosenSize ← Large'''), None) + req("3 marks", "State", "A is the set {1, 2, 3, 4} and B is the set {3, 4, 5}. State the union, the intersection and the difference A − B.", "Unique values only.",
  "<p>" + mks(["Union: {1, 2, 3, 4, 5}", "Intersection: {3, 4}", "A − B: {1, 2}"]) + "</p>", None) + req("2 marks", "Distinguish", "Distinguish between a record and a set.", "Think about types, order and duplicates.",
  "<p>" + mks(["A record holds fields of different data types for one item, each accessed by name.", "A set holds unordered, unique values that all have the same data type, and supports union and intersection."]) + "</p>", None) + req("3 marks", "Explain", "A programmer stores a person's date of birth in a STRING field, and their telephone number in an INTEGER field. Explain why a different choice would be better for each.", "What can be done with a DATE; what is lost in an integer.",
  "<p>" + mks(["A DATE field can be compared and used in calculations such as age, which a string cannot.", "A telephone number may start with 0, which an INTEGER drops.", "The telephone number is not used in arithmetic, so a STRING is the appropriate type."]) + "</p>", None) + req("2 marks", "Write", "Write the statement to declare an array of 30 Product records called Stock, and the statement to set the price of the fifth to 2.50.", "Array of the record type, dot notation on the element.",
  "<p>" + mks(["DECLARE Stock : ARRAY[1:30] OF Product", "Stock[5].Price ← 2.50"]) + "</p>", None)

exam = exam20("Part 1 is real 9618 questions on composite user-defined types: records, sets and choosing the data types (Paper 3), 2021 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", where, past, review)

tips = tips_html([
  ("Check every field's type.", "Text and codes: STRING. Whole numbers: INTEGER. Fractions: REAL. Yes or no: BOOLEAN. Dates: DATE. Fixed lists: enumerated."),
  ("Telephone numbers and codes are STRINGs.", "They are not used in calculations, and may start with 0 or hold letters."),
  ("TYPE ... ENDTYPE, DECLARE on each line.", "One mark for the frame, then marks for the fields."),
  ("Declare the variable first.", "DECLARE Pet1 : Pet, then assign each field as Pet1.Field."),
  ("Use the type you are told to use.", "If the question says use the enumerated type, a STRING field loses the mark."),
  ("Sets: SET OF, DEFINE, values, type.", "Four things in two statements."),
], [
  ("what a composite type is", "A type that refers to other data types in its definition and holds several values under a single identifier."),
  ("what a set is", "A composite type holding unordered, unique values of one data type, with set operations such as union."),
  ("what a record is", "A composite type grouping fields of different data types under one identifier."),
  ("how to choose a type", "Use the most appropriate type for what the field holds and how it will be used."),
], [("Write pseudocode", "Use exactly the TYPE, DECLARE and ENDTYPE forms."), ("Describe", "Say what it is and what it holds."), ("Define", "Give the exact meaning, using the standard terms."), ("Identify", "Name one field and give a reason.")]) + FC

js = AKJS + AK20JS + r'''
function classBox(x, y, w, title, rows, v = 1, cls = "f1", lh = 20) {
  const h = 30 + rows.length * lh + 8;
  let o = SV.rect(x, y, w, h, "cell", { rx: 6, ...op(v) }) + SV.rect(x, y, w, 28, cls, { rx: 6, ...op(v * 0.6) }) + SV.text(x + w / 2, y + 19, title, "lbl bd", { "text-anchor": "middle", style: "font-size:15px", ...op(v) });
  rows.forEach((r, i) => { o += SV.text(x + 8, y + 46 + i * lh, r, "sm", { style: "font-family:var(--mono);font-size:11.5px", ...op(v) }); });
  return o;
}

(function () {
  const vals = ["\"XA782\"", "\"Cambridge\"", "12/12/2022", "C350"];
  const draw = (s) => {
    const k = Math.round(s.i); const f = ["FlightNumber", "Destination", "DepartureDate", "AircraftType"], t = ["STRING", "STRING", "DATE", "Aircraft"];
    let o = classBox(20, 20, 280, "TYPE Flight", f.map((n, i) => n + " : " + t[i]), 1, "f1", 24);
    if (k >= 1) o += classBox(380, 20, 340, "Flight1 : Flight", f.map((n, i) => n + " = " + (k > i + 1 ? vals[i] : "?")), 1, "f2", 24) + SV.line(300, 70, 380, 70, "dash", op(0.6));
    return o;
  };
  Lib.stepper($("#stA"), { w: 760, h: 200, label: "A record type and a record variable", base: { i: 0 }, draw, tween: 300, dwell: 3000, steps: [
    { cap: "The <b>TYPE</b> statement describes a record: a name and a field for each item, each with its data type. It creates no data yet.", s: { i: 0 } },
    { cap: "<code>DECLARE Flight1 : Flight</code> creates a variable that can hold one record. Its fields are empty.", s: { i: 1 } },
    { cap: "<code>Flight1.FlightNumber ← \"XA782\"</code>: dot notation assigns one field.", s: { i: 2 } },
    { cap: "<code>Flight1.Destination ← \"Cambridge\"</code>.", s: { i: 3 } },
    { cap: "<code>Flight1.DepartureDate ← 12/12/2022</code> (a DATE, no quotation marks).", s: { i: 4 } },
    { cap: "<code>Flight1.AircraftType ← C350</code>: an enumerated value, so no quotation marks. The record is complete.", s: { i: 5 } }] });
})();

(function () {
  const rows = [["SB2789", "Dublin", "N03"], ["BA104", "Paris", "W01"], ["XA782", "Cambridge", "N01"]];
  const draw = (s) => {
    const k = Math.round(s.i); let o = SV.text(30, 24, "Flights : ARRAY[1:3] OF Flight", "lbl bd", { style: "font-family:var(--mono);font-size:14px" });
    o += SV.text(30, 56, "index", "sm") + SV.text(100, 56, "FlightNumber", "sm") + SV.text(260, 56, "Destination", "sm") + SV.text(420, 56, "Gate", "sm");
    rows.forEach((r, i) => { const y = 66 + i * 40; o += SV.rect(30, y, 640, 34, k === i + 1 ? "cell-warn" : "cell", { rx: 6 }) + SV.text(44, y + 22, String(i + 1), "lbl", { style: "font-family:var(--mono)" }) + SV.text(100, y + 22, r[0], "lbl", { style: "font-family:var(--mono)" }) + SV.text(260, y + 22, r[1], "lbl", { style: "font-family:var(--mono)" }) + SV.text(420, y + 22, k === 4 && i === 1 ? "W04" : r[2], "lbl" + (k === 4 && i === 1 ? " bd t3" : ""), { style: "font-family:var(--mono)" }); });
    if (k === 1) o += SV.text(30, 206, "Flights[1].Destination  →  \"Dublin\"", "lbl bd", { style: "font-family:var(--mono);font-size:14px" });
    if (k === 4) o += SV.text(30, 206, "Flights[2].Gate ← W04   changes one field of one record", "lbl bd t3", { style: "font-family:var(--mono);font-size:14px" });
    return o;
  };
  Lib.stepper($("#stB"), { w: 760, h: 230, label: "An array of records", base: { i: 0 }, draw, tween: 250, dwell: 2800, steps: [
    { cap: "An <b>array of records</b> stores many flights: every element is a whole record.", s: { i: 0 } },
    { cap: "<code>Flights[1].Destination</code>: the array element first, then the field.", s: { i: 1 } },
    { cap: "<code>Flights[2]</code> is the record for BA104.", s: { i: 2 } },
    { cap: "A loop can visit each record in turn: <code>FOR i ← 1 TO 3</code>.", s: { i: 3 } },
    { cap: "A field can be changed on its own: <code>Flights[2].Gate ← W04</code>.", s: { i: 4 } }] });
})();

(function () {
  const A = [1, 2, 3], B = [3, 4];
  const draw = (s) => {
    const k = Math.round(s.i); let o = SV.circle(260, 120, 90, "f1", op(0.3)) + SV.circle(420, 120, 90, "f2", op(0.3)) + SV.text(200, 36, "A = {1, 2, 3}", "lbl bd") + SV.text(380, 36, "B = {3, 4}", "lbl bd");
    const items = { 1: [210, 120], 2: [240, 165], 3: [340, 120], 4: [470, 120] }, hit = (n) => k === 0 ? false : k === 1 ? true : k === 2 ? n === 3 : n === 1 || n === 2;
    [1, 2, 3, 4].forEach((n) => { const p = items[n]; o += SV.circle(p[0], p[1], 20, hit(n) ? "dot3" : "dot1", op(hit(n) ? 1 : 0.25)) + SV.text(p[0], p[1] + 6, String(n), "lbl bd", { "text-anchor": "middle", style: "fill:#fff;font-size:17px" }); });
    const caps = ["", "A ∪ B = {1, 2, 3, 4}", "A ∩ B = {3}", "A − B = {1, 2}"];
    if (k >= 1) o += SV.text(560, 130, caps[k], "lbl bd t3", { style: "font-size:17px" });
    return o;
  };
  Lib.stepper($("#stC"), { w: 760, h: 240, label: "Set operations", base: { i: 0 }, draw, tween: 250, dwell: 3200, steps: [
    { cap: "Two sets. The number 3 is in both. In a set the order does not matter and no value appears twice.", s: { i: 0 } },
    { cap: "<b>Union</b>: everything that is in A or in B (or both). 3 is listed once.", s: { i: 1 } },
    { cap: "<b>Intersection</b>: only the values that are in both sets.", s: { i: 2 } },
    { cap: "<b>Difference</b> A − B: the values in A that are not in B.", s: { i: 3 } }] });
})();

(function () {
  const rows = [["VideoID  (SB2789 style code)", "STRING", "letters and digits"], ["Title", "STRING", "text"], ["ReleaseYear", "INTEGER", "whole number"], ["PurchaseDate", "DATE", "a calendar date"], ["VideoFormat  (DVD, Blu-ray, 4K)", "Enumerated", "fixed list of values"], ["RunningTime  (minutes)", "INTEGER", "whole number"]];
  const draw = (s) => {
    const k = Math.round(s.i); let o = SV.text(30, 24, "TYPE VideoLibrary", "lbl bd", { style: "font-family:var(--mono);font-size:15px" });
    rows.forEach((r, i) => { const y = 38 + i * 34; o += SV.rect(30, y, 700, 30, k > i ? "f3" : "cell", { rx: 6, ...op(k > i ? 1 : 0.7) }) + SV.text(44, y + 20, r[0], "lbl", { style: "font-family:var(--mono);font-size:13px" }); if (k > i) o += SV.text(380, y + 20, r[1], "lbl bd", { style: "font-family:var(--mono);font-size:13px" }) + SV.text(500, y + 20, r[2], "sm"); });
    return o;
  };
  Lib.stepper($("#stD"), { w: 760, h: 258, label: "Choosing a data type for each field", base: { i: 0 }, draw, tween: 250, dwell: 2600, steps: [
    { cap: "Each field needs the most appropriate type. Read what the data looks like and how it will be used.", s: { i: 0 } },
    { cap: "An identity code mixes letters and digits: <b>STRING</b>.", s: { i: 1 } },
    { cap: "A title is text: <b>STRING</b>.", s: { i: 2 } },
    { cap: "A year is a whole number: <b>INTEGER</b>.", s: { i: 3 } },
    { cap: "A purchase date: <b>DATE</b>.", s: { i: 4 } },
    { cap: "The format has only a few possible values, DVD, Blu-ray, 4K and MP4: an <b>enumerated</b> type is efficient and safe.", s: { i: 5 } },
    { cap: "A running time in minutes: <b>INTEGER</b>.", s: { i: 6 } }] });
})();

/* Lab 1: set operations */
(function () {
  const N = [1, 2, 3, 4, 5, 6, 7, 8]; let A = [1, 2, 3], B = [3, 4, 5], op = 0;
  const ops = ["Union", "Intersection", "Difference A − B", "Difference B − A"];
  const paint = () => {
    const mk = (id, S, which) => { $("#" + id).innerHTML = '<span style="align-self:center;margin-right:6px"><b>' + which + "</b></span>" + N.map((n) => `<button class="b${S.includes(n) ? " pri" : ""}" data-n="${n}">${n}</button>`).join(""); $$("#" + id + " button").forEach((b) => (b.onclick = () => { const n = +b.dataset.n; const i = S.indexOf(n); if (i >= 0) S.splice(i, 1); else S.push(n); paint(); })); };
    mk("sA", A, "A"); mk("sB", B, "B");
    $("#sO").innerHTML = ops.map((o, i) => `<button class="b${i === op ? " pri" : ""}" data-i="${i}">${o}</button>`).join(""); $$("#sO button").forEach((b) => (b.onclick = () => { op = +b.dataset.i; paint(); }));
    const srt = (a) => a.slice().sort((x, y) => x - y), fmt = (a) => "{" + srt(a).join(", ") + "}";
    const res = op === 0 ? [...new Set([...A, ...B])] : op === 1 ? A.filter((n) => B.includes(n)) : op === 2 ? A.filter((n) => !B.includes(n)) : B.filter((n) => !A.includes(n));
    $("#s1").textContent = fmt(A); $("#s2").textContent = fmt(B); $("#s3").textContent = fmt(res);
    $("#sV").textContent = ["Union: every value that is in A or in B, each listed once.", "Intersection: only the values in both sets.", "A − B: values in A that are not in B.", "B − A: values in B that are not in A."][op];
  };
  paint();
})();

/* Lab 2 */
(function () {
  const sc = [
    ["Booking", [["BookingNumber (letters and digits)", "STRING"], ["DateOfDeparture", "DATE"], ["ClientTelephone", "STRING"], ["TaxiUsed (M100, M230, T101 ...)", "Enumerated"]]],
    ["ColourData", [["ColourCode (XYZ12345)", "STRING"], ["Wavelength (650)", "INTEGER"], ["Frequency (4.62)", "REAL"], ["PrimaryColour (Yes or No)", "BOOLEAN"]]],
    ["ClubMember", [["Code (984632)", "INTEGER"], ["JoinDate", "DATE"], ["Fees (12.50)", "REAL"], ["FeesPaid (yes or no)", "BOOLEAN"]]]
  ];
  const T = ["STRING", "INTEGER", "REAL", "BOOLEAN", "DATE", "CHAR", "Enumerated"]; let cur = 0, pick = [];
  const paint = () => {
    $$("#tB button").forEach((b, i) => b.classList.toggle("pri", i === cur));
    $("#tO").innerHTML = '<div class="tw"><table class="t"><tr><th>Field</th><th>Choose the type</th></tr>' + sc[cur][1].map((f, i) => `<tr><td><code>${f[0]}</code></td><td>${T.map((t) => `<button class="b${pick[i] === t ? " pri" : ""}" data-i="${i}" data-t="${t}">${t}</button>`).join(" ")}</td></tr>`).join("") + "</table></div>";
    $$("#tO button").forEach((b) => (b.onclick = () => { pick[+b.dataset.i] = b.dataset.t; paint(); }));
    const done = sc[cur][1].every((f, i) => pick[i]); const ok = sc[cur][1].filter((f, i) => pick[i] === f[1]).length;
    $("#tV").innerHTML = done ? (ok === sc[cur][1].length ? "All four are the most appropriate types." : `${ok} of ${sc[cur][1].length} correct. Check: text and codes are STRING, whole numbers INTEGER, fractions REAL, yes/no BOOLEAN, fixed lists are enumerated.`) : "Choose a type for every field.";
  };
  $("#tB").innerHTML = sc.map((s, i) => `<button class="b" data-i="${i}">${s[0]}</button>`).join("");
  $$("#tB button").forEach((b) => (b.onclick = () => { cur = +b.dataset.i; pick = []; paint(); })); paint();
})();

(function () {
  const rows = [
    ["TYPE Pet\n   DECLARE PetName : STRING\n   DECLARE PetAge : INTEGER", "No ENDTYPE: the definition is never closed", "Add ENDTYPE"],
    ["TYPE Pet\n   PetName : STRING\nENDTYPE", "Each field needs the word DECLARE", "DECLARE PetName : STRING"],
    ["DECLARE Pet1 : Pet\nPetName ← \"Tibbles\"", "The field is not tied to the variable", "Pet1.PetName ← \"Tibbles\""],
    ["Pet1.PetAge ← \"8\"", "PetAge is an INTEGER, so no quotation marks", "Pet1.PetAge ← 8"],
    ["Flight1.AircraftType ← \"C350\"", "AircraftType is enumerated: no quotation marks", "Flight1.AircraftType ← C350"],
    ["DEFINE Operators ('+', '-') : SymbolSet\n(no TYPE statement before it)", "The set type was never declared", "TYPE SymbolSet = SET OF CHAR first"]
  ];
  const paint = (i) => { $$("#mB button").forEach((b, k) => b.classList.toggle("pri", k === i)); const r = rows[i]; $("#mO").innerHTML = '<div class="tw"><table class="t"><tr><th>Mistake</th><th>What is wrong</th><th>Correct</th></tr><tr><td><pre class="plain">' + r[0].replace(/&/g, "&amp;").replace(/</g, "&lt;") + "</pre></td><td>" + r[1] + "</td><td><code>" + r[2] + "</code></td></tr></table></div>"; };
  $("#mB").innerHTML = rows.map((r, i) => `<button class="b" data-i="${i}">Mistake ${i + 1}</button>`).join("");
  $$("#mB button").forEach((b) => (b.onclick = () => paint(+b.dataset.i))); paint(0);
})();
''' + CLASSIFY("cl1", "Which data type is best for each field?", ["STRING", "INTEGER", "REAL", "BOOLEAN", "DATE", "Enumerated"],
  [("A telephone number such as 01223 658721", 0), ("A running time in minutes", 1), ("A price of 12.99", 2), ("Fees paid: yes or no", 3), ("Date of departure", 4), ("Format: DVD, Blu-ray, 4K or MP4", 5), ("An identity code SB2789", 0), ("Year released", 1), ("A frequency of 4.62", 2), ("Number of members", 1)],
  "Codes and phone numbers are STRING. Whole numbers: INTEGER. With a fraction: REAL. Two values: BOOLEAN. Calendar: DATE. A fixed list: enumerated.") + CLASSIFY("cl2", "Is it a record, a set or a class?", ["Record", "Set", "Class / object"],
  [("Fields of different types about one flight", 0), ("Unordered unique values of one type, with union and intersection", 1), ("Fields and the methods that act on them, with objects as instances", 2), ("TYPE Pet ... ENDTYPE", 0), ("TYPE Numbers = SET OF INTEGER", 1), ("A Parrot inherits from Animal", 2)],
  "Record: fields. Set: unique unordered, one type. Class: fields plus methods.") + ORDER(
  "Put the steps for creating and using a record in order.",
  ["Write the TYPE statement with a DECLARE for each field", "End it with ENDTYPE", "DECLARE a variable of the new type", "Assign each field with variable.field", "Use the fields in the program"],
  "Type, ENDTYPE, variable, assign, use.") + MATCH([
  ["Record", "A composite type with fields of different types"], ["Set", "Unordered, unique values of one type"], ["Union", "Everything in either set"], ["Intersection", "Only what is in both sets"], ["Class", "A composite type holding fields and methods"]]) + CALC([
  {"q": "A = {1, 2, 3, 4, 5} and B = {4, 5, 6}. How many values are in the union?", "a": 6, "unit": "", "tol": 0.01, "hint": "1, 2, 3, 4, 5, 6.", "sol": "<b>6</b>."},
  {"q": "A = {1, 2, 3, 4, 5} and B = {4, 5, 6}. How many values are in the intersection?", "a": 2, "unit": "", "tol": 0.01, "hint": "4 and 5.", "sol": "<b>2</b>."},
  {"q": "A = {1, 2, 3, 4, 5} and B = {4, 5, 6}. How many values are in A − B?", "a": 3, "unit": "", "tol": 0.01, "hint": "1, 2, 3.", "sol": "<b>3</b>."},
  {"q": "A record type has 6 fields. How many DECLARE statements are inside the TYPE ... ENDTYPE?", "a": 6, "unit": "", "tol": 0.01, "hint": "One for each field.", "sol": "<b>6</b>."},
  {"q": "An array holds 30 records and each record has 5 fields. How many individual field values are there?", "a": 150, "unit": "", "tol": 0.01, "hint": "30 × 5.", "sol": "<b>150</b>."},
  {"q": "A set is defined as {2, 4, 6, 8, 10, 12}. How many values does it hold?", "a": 6, "unit": "", "tol": 0.01, "hint": "Count them.", "sol": "<b>6</b>."}]) + MCQ([
  ("What is a record?", ["An ordered list of one type", "A composite type with fields, which may have different types", "A pointer", "A loop"], 1, "Fields grouped under one identifier."),
  ("Which data type should hold a telephone number?", ["INTEGER", "STRING", "REAL", "BOOLEAN"], 1, "It is not used in arithmetic and may start with 0."),
  ("Which statement is true of a set?", ["It is ordered", "It can contain duplicates", "Its elements are unordered and unique and have one data type", "It holds fields of different types"], 2, "Those are the characteristics."),
  ("Which line assigns a value to a field of the record variable Pet1?", ["PetName ← \"Tibbles\"", "Pet1.PetName ← \"Tibbles\"", "Pet.PetName ← \"Tibbles\"", "Pet1(PetName) ← \"Tibbles\""], 1, "variable.field."),
  ("Which set operation gives the values in both sets?", ["Union", "Intersection", "Difference", "Membership"], 1, "Intersection."),
  ("A field has the fixed values DVD, Blu-ray and 4K. What is the best type?", ["STRING", "INTEGER", "An enumerated type", "REAL"], 2, "A fixed list is an enumerated type.")], "qz1") + CARDS([
  ("Composite type", "Refers to other types; holds several values under one identifier."), ("Record", "Fields of different types. TYPE ... ENDTYPE with DECLARE."), ("Set", "Unordered, unique values of one type. TYPE S = SET OF ... DEFINE ..."), ("Class", "Fields and methods; objects are instances."),
  ("Dot notation", "Variable.Field ← value"), ("Union / intersection", "Either set / both sets."), ("Choosing types", "STRING text and codes, INTEGER whole, REAL fraction, BOOLEAN yes/no, DATE, enumerated list."), ("Array of records", "Flights[2].Gate")])

build("ac1312", "ac-13-1-2-composite-types", "User-defined Types: Records, Sets and Classes", EYA("13.1.2"),
  "Composite types: records with dot notation, sets and their operations, classes; how to choose the right data type for each field; animations, labs and the real 9618 declaration questions from 2021 to 2026.",
  dict(sub=CBK("Chapter 13 · Data representation, section 13.1 User-defined data types"), **tabs(learn, watch, explore, practise, real, exam, tips)), js)
