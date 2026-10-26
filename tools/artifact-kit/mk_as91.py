"""AS CS 9.1: abstraction and decomposition. Run: python3 tools/artifact-kit/mk_as91.py"""
from ascs import *

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p><b>Abstraction</b> is the process of <b>filtering out information that is not necessary</b> for the task and keeping only what is needed, which makes the problem easier to design, implement and solve; an <b>abstract model</b> of a car hire system keeps car and customer IDs, dates and cost, but not the car's colour or the customer's favourite music. <b>Decomposition</b> is <b>breaking down a problem into sub-problems</b> (smaller parts or steps) so each can be understood and solved, which leads to the idea of <b>program modules</b> (procedures and functions), each of which can be tested separately or given to a different team. In the exam, <b>abstraction</b> questions ask what data to store and what processes (operations) are needed; <b>decomposition</b> questions give a scenario and ask for named sub-modules with their use. Name each module like a function (<span class="mono">GetOverdueLoan()</span>) and say what it does in the scenario. Never answer with general statements only: the marks are for scenario-specific modules and data.</p></div>

  <h2>1 · Abstraction</h2>
  <ul>
    <li><b>Definition:</b> filtering out (removing) information or data that is not necessary for the task, and keeping only what is needed.</li>
    <li><b>Advantage:</b> makes the solution easier to design, implement and solve.</li>
    <li><b>Abstract model for car hire:</b> data stored each time a car is hired: car ID or registration; customer ID or name; start date of hire; return date or number of days; cost of hire. Not stored: the car's colour, the customer's hobbies.</li>
    <li><b>Operations (processes) for the data:</b> input customer details, input car details, create or start a hire, return a car or end a hire, check or change the car's status, cancel a hire, process payment or calculate hire cost.</li>
  </ul>
  <p>When asked which items a new module needs, choose each item and <b>justify it from the scenario</b>: the mobile phone number is needed to send the text message; the name to personalise it; the exercise interest to decide whether the member is interested.</p>

  <h2>2 · Decomposition</h2>
  <ul>
    <li><b>Definition:</b> breaking down a problem or task into sub-problems (smaller parts or steps), in order to understand or solve it more easily, leading to the idea of a program made of modules that can be assigned to teams.</li>
    <li><b>Benefits:</b> each module is easier to code, test and debug; different programmers can work on different modules; modules can be reused.</li>
    <li><b>Types of module:</b> a <b>procedure</b> does a task; a <b>function</b> <b>returns a value</b>.</li>
  </ul>
  <p>Example: a program that emails students with an overdue book is decomposed into <span class="mono">GetOverdueLoan()</span> (identifies an overdue book), <span class="mono">IdentifyStudent()</span> (identifies the student), <span class="mono">GetStudentEmail()</span>, <span class="mono">CreateEmail()</span> and <span class="mono">SendEmail()</span>.</p>
  <div class="tw"><table class="t">
    <tr><th>Scenario</th><th>Sub-modules and their use</th></tr>
    <tr><td>Cinema seat booking</td><td>Search for films being shown; search for available seats; calculate the cost of a booking; book a number of seats for a screening</td></tr>
    <tr><td>Donate to charity on a phone</td><td>SelectCharity() lets the user choose; SpecifyAmountAndType() single or regular payment; MakePayment(); ValidatePayment(); AddDonorDetails()</td></tr>
    <tr><td>Loyalty card</td><td>ScanCard() reads the bar code; GetPoints(); CalculatePoints() after a purchase; UpdatePoints(); GetDiscount() or ExchangePoints()</td></tr>
  </table></div>

  <h2>Common ways to lose marks</h2>
  <ul>
    <li>Describing decomposition without saying "sub-problems" and "modules".</li>
    <li>Describing abstraction as "hiding detail from the user". It filters out unnecessary information so the problem is easier to solve.</li>
    <li>Giving modules that are not specific to the scenario, such as "input" and "output".</li>
    <li>Naming a module with no use. Give the name and say what it does.</li>
    <li>Listing items that are not needed for the task, or repeating the same item twice (hire date and hire date).</li>
  </ul>
'''

watch = '''
  <h2>1 · Abstraction filters out detail</h2>
  <div id="stA"></div>
  <h2>2 · Decomposing a problem into modules</h2>
  <div id="stB"></div>
  <h2>3 · Modules that return a value</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Build an abstract model</h2>
  <p>Tick the items a car hire system needs. Unnecessary items are filtered out.</p>
  <div class="card"><div id="aB" class="btnrow"></div><div id="aV" class="verdict"></div></div>
  <h2>Lab 2 · Decompose the problem</h2>
  <div class="card"><div id="dB" class="btnrow"></div><div id="dO"></div></div>
  <h2>Lab 3 · Procedure or function?</h2>
  <div class="card"><div id="pB" class="btnrow"></div><div id="pO"></div></div>
'''

_pr, _prjs = PR(["Abstraction or decomposition?", "Needed or not needed?", "Match the term to its meaning", "Put the decomposition steps in order", "Working out", "Multiple choice"],
  ("Abstraction or decomposition?", ["Abstraction", "Decomposition"], [("Filtering out information that is not necessary", 0), ("Breaking a problem into sub-problems", 1), ("Leads to program modules", 1), ("Keeps only the data needed for the task", 0), ("Makes the problem easier to solve by removing detail", 0), ("Assigns parts of a problem to different teams", 1)], "Abstraction removes; decomposition splits."),
  ("For a car hire system, is the item needed in the abstract model?", ["Needed", "Not needed"], [("Start date of hire", 0), ("The car's paint colour", 1), ("Customer ID", 0), ("The customer's favourite music", 1), ("Cost of hire", 0), ("The driver's shoe size", 1)], "Keep only what the task needs."),
  [["Abstraction", "Filtering out unnecessary information"], ["Decomposition", "Breaking a problem into sub-problems"], ["Module", "A procedure or function that does one part of the job"], ["Function", "A module that returns a value"], ["Abstract model", "A simplified version holding only the needed data"]],
  ("Put the decomposition steps in order.", ["State the whole problem", "Break it into sub-problems", "Give each sub-problem a module name and a use", "Code and test each module separately", "Combine the modules into the program"], "Problem, split, name, test, combine."),
  [{"q": "A program is split into 6 modules. Four programmers each take an equal share of 6 modules as evenly as possible; at most how many modules does one programmer have?", "a": 2, "unit": "", "tol": 0.01, "hint": "6 ÷ 4 rounded up.", "sol": "<b>2</b>."}, {"q": "A car hire record keeps 5 data items instead of 25 because of abstraction. What percentage is kept?", "a": 20, "unit": "%", "tol": 0.1, "hint": "5 ÷ 25.", "sol": "<b>20</b>%."}, {"q": "How many sub-modules did the library overdue-email example use (GetOverdueLoan, IdentifyStudent, GetStudentEmail, CreateEmail, SendEmail)?", "a": 5, "unit": "", "tol": 0.01, "hint": "Count.", "sol": "<b>5</b>."}, {"q": "A decomposed program has 8 modules and each takes 3 hours to test. How many hours to test them all?", "a": 24, "unit": "h", "tol": 0.01, "hint": "8 × 3.", "sol": "<b>24</b>."}, {"q": "Two of the 5 data items stored per hire are dates. How many items are not dates?", "a": 3, "unit": "", "tol": 0.01, "hint": "5 − 2.", "sol": "<b>3</b>."}],
  [("Abstraction:", ["Removes unnecessary detail", "Adds more data", "Splits a problem", "Compiles code"], 0, "Removes."), ("Decomposition:", ["Breaks a problem into sub-problems", "Removes data", "Draws a flowchart", "Encrypts"], 0, "Breaks down."), ("A function:", ["Returns a value", "Never returns", "Is a data item", "Is a file"], 0, "Returns a value."), ("An advantage of abstraction:", ["Easier to design and solve", "Slower program", "More memory", "More errors"], 0, "Easier."), ("Decomposition leads to:", ["Program modules", "Larger files", "Fewer tests", "A single module"], 0, "Modules."), ("An abstract model keeps:", ["Only what the task needs", "Everything", "Nothing", "Only dates"], 0, "Only what is needed.")],
  [("Abstraction", "Filter out what is not necessary."), ("Decomposition", "Break into sub-problems."), ("Module", "A procedure or function."), ("Function", "Returns a value."), ("Procedure", "Does a task; no return value."), ("Abstract model", "Only the needed data."), ("Scenario-specific", "Name modules for the scenario."), ("Advantage", "Easier to design, test, share.")])

real = RWNOTE + (
rw("A map", "A tube map filters out streets and distances and keeps stations and connections: an abstract model for planning a journey.", "abstraction.") +
rw("Building a school app", "Timetable, attendance and messages are built by different teams as separate modules, then joined: decomposition.", "decomposition.") +
rw("A game character", "A game keeps position, health and score for a character, not the hair colour of the player: only the data the game logic needs.", "abstraction.") +
rw("Cooking a big meal", "You split it into starter, main, pudding and plan each separately: breaking a problem into sub-problems.", "decomposition.") +
rw("A bank app", "Login, balance, transfer and statement are separate modules; the transfer module returns success or failure: a function.", "modules and functions.")
)

where = [
  ("O/N 2021", "22", "1(a)", "2", "Describe decomposition"),
  ("O/N 2022", "21", "2", "3 + 2", "Explain abstraction and state four items stored for a car hire; two operations"),
  ("M/J 2022", "21", "3", "3 + 1", "Describe three program modules for a cinema booking; the module that returns a value"),
  ("O/N 2022", "23", "2", "3", "Three program modules for a charity donation app"),
  ("M/J 2023", "21", "7(a)", "3", "Three modules for emailing students with overdue books"),
  ("M/J 2024", "21", "7(a)", "1 + 3 + 2", "An advantage of abstraction; three items needed with justification; two operations"),
  ("M/J 2024", "22", "7(a)", "3", "Three sub-modules to text members on a waiting list"),
  ("O/N 2024", "23", "7(b)", "4", "Four sub-modules for a loyalty card module"),
  ("M/J 2025", "21", "1(c)", "3", "Describe decomposition for a stock control program"),
  ("M/J 2026", "22", "2", "1 + 2 + 2", "The purpose of abstraction; four items stored for a tool hire; two processes")]

past = '''  <p class="note">These are Paper 2 questions: the answers are short written descriptions rather than code. Questions are reworded from the papers; check the original paper and mark scheme for the exact wording. In decomposition answers the name and the use are the marks, so each module needs both.</p>
''' + peq(SRC("w21", "22", "Q1(a)"), "2 marks", "Describe",
  "A programmer applies decomposition to a problem that she has been asked to solve. Describe decomposition.", "Break into sub-problems, to explain or understand it, leading to modules.",
  "<p>Any two: " + mks(["Breaking down a problem or task into sub-problems, steps or smaller parts", "in order to explain or understand it, or to make it easier to solve", "leading to the concept of program modules, or assigning parts of the problem to teams"]) + "</p>", None) + peq(SRC("w22", "21", "Q2"), "3 + 2 marks", "Explain / State",
  "A system is being developed to help manage a car hire business. A customer may hire a car for a number of days. An abstract model needs to be produced. (a) Explain the process of abstraction and state four items of data that should be stored each time a car is hired. (b) Identify two operations that would be required to process the car hire data.", "Filter out unnecessary data; car, customer, dates, cost.",
  "<p><b>(a)</b> " + mks(["Abstraction filters out information or data that is not necessary for the task (or keeps only what is necessary)", "Two of: car details (ID, registration, type); customer details (ID, name, address, licence); start date of hire; return date or number of days; cost of hire", "Two more of those items"]) + " (one mark for the explanation, one for each pair of items)</p><p><b>(b)</b> Any two: " + mks(["Input customer details", "Input car details", "Create or start a hire", "Return car or end a hire", "Change or check car status", "Cancel a hire", "Process payment or calculate the hire cost"], "a") + "</p>", "Stating items such as the car's colour. Abstraction filters those out.") + peq(SRC("s22", "21", "Q3"), "3 + 1 marks", "Describe / Identify",
  "A cinema manager wants a program to allow users to book seats. The cinema has several screens, each showing a different film. (a) Decomposition will be used to break the problem down into sub-problems. Describe three program modules that could be used in the design. (b) Two types of program module may be used. Identify the type that should be used to return a value.", "Search films, search seats, cost, book. Function.",
  "<p><b>(a)</b> One mark for each description of an appropriate sub-problem: " + mks(["Allows the user to search for films being shown, or enter the name of the film they want to see", "Allows the user to search for available seats", "Calculates the cost of a booking", "Books a given number of seats for a particular screening"]) + " (any three)</p><p><b>(b)</b> " + mks(["Function"], "a") + "</p>", None) + peq(SRC("w22", "23", "Q2"), "3 marks", "Identify / Describe",
  "A smartphone program will allow users to send money to the charity of their choice. Decomposition will be used to break the problem into sub-problems. Identify three program modules that could be used in the design and describe their use.", "Name and use for three.",
  "<p>One mark for a name and one for its use, max 3: " + mks(["SelectCharity(): allows the user to choose a particular charity", "SpecifyAmountAndType(): allows the user to specify a single or regular payment", "MakePayment(): makes the payment to the charity", "ValidatePayment(): validates payment details by accessing the bank computer", "AddBankAccountDetails(): the account the donation is taken from", "AddDonorDetails(): the user's name and contact details"]) + "</p>", None) + peq(SRC("s23", "21", "Q7(a)"), "3 marks", "Identify / Describe",
  "A school library system uses text files for students, books and loans. A new module generates emails to each student who has an overdue book. Decomposition will be used. Identify three program modules that could be used in the design and describe their use.", "Overdue loan, student, email address, create, send.",
  "<p>One mark for name and use, max 3: " + mks(["GetOverdueLoan(): identifies an overdue book", "IdentifyStudent(): identifies the student with an overdue book", "GetStudentEmail(): gets the email address of the student", "CreateEmail(): generates an email to the student", "SendEmail(): sends the email"]) + "</p>", None) + peq(SRC("s24", "21", "Q7(a)"), "1 + 3 + 2 marks", "State / Identify",
  "A fitness club's new module sends personalised text messages to each member who has expressed an interest in an exercise class; members reply to join or send STOP to opt out. The club stores name, home address, email address, mobile number, date of birth and exercise interests. Abstraction filters out unnecessary information. (i) State one advantage of applying abstraction. (ii) Identify three items required by the module and justify each. (iii) Identify two operations when the module receives a text back.", "Easier to design. Mobile number, name, exercise interest. Add to list, remove from list.",
  "<p><b>(i)</b> " + mks(["To make the solution easier to design, implement or solve"]) + "</p><p><b>(ii)</b> One mark per item and justification: " + mks(["Mobile phone number: to send the text message", "Name: to personalise the text message", "Exercise interest: to determine whether this member would be interested"], "a") + "</p><p><b>(iii)</b> Any two: " + mks(["Add a member to the list of those interested in the new class", "Remove the member from future text messages", "Read or process the message", "Identify who it is from"], "b") + "</p>", "Choosing the home address or date of birth. They are not needed to send a text message.") + peq(SRC("s24", "22", "Q7(a)"), "3 marks", "Identify / Describe",
  "When a space becomes available in a full class, a new module will send a text message to each member on the waiting list. Decomposition will be used to break the new module into sub-modules. Identify three sub-modules and describe their use.", "Identify a member, get phone number, create, send.",
  "<p>One mark for name and use, max 3: " + mks(["IdentifyMember(): identifies a member who has expressed an interest in the class", "GetMemberPhoneNumber(): gets the member's mobile number", "CreateMessage(): generates a text message to the member", "SendMessage(): sends the text message to a member on the waiting list"]) + "</p>", None) + peq(SRC("w24", "23", "Q7(b)"), "4 marks", "Identify / Describe",
  "A coffee shop gives each customer a loyalty card showing a unique customer ID as a bar code. The system scans the bar code, calculates points and adds them to the customer's total; the customer can exchange points for a discount. Decomposition will break the new module into sub-modules. Identify four sub-modules and describe their use.", "Scan, get points, calculate, update, discount.",
  "<p>One mark for name and use, max 4: " + mks(["ScanCard() or GetID(): reads the bar code and gets the customer ID", "GetPoints(): gets the number of points the customer has", "CalculatePoints(): calculates points following a purchase", "UpdatePoints(): updates the customer's total points", "ExchangePoints() or UpdateCard(): reduces the number of loyalty points", "GetDiscount() or CalculateDiscount(): calculates the discount", "ShowDiscount(): displays the discount"]) + "</p>", None) + peq(SRC("s25", "21", "Q1(c)"), "3 marks", "Describe",
  "Decomposition has been used to design the program to help the shop manager control the stock. Describe decomposition.", "Sub-problems; understand stock control; modules; easier to test. Mention the stock control.",
  "<p>Any three (max 2 if there is no mention of stock control): " + mks(["Breaking down a problem into sub-problems", "in order to explain or understand how the stock can be managed in more detail", "leading to the program being designed as a series of modules, procedures or functions, or by example of stock control modules", "making the program easier to test and debug"]) + "</p>", "Writing a general definition with no mention of stock control.") + peq(SRC("s26", "22", "Q2"), "1 + 2 + 2 marks", "Explain / State",
  "A new system helps manage a tool hire business where a customer hires a tool for half a day or a full day. An abstract model is required. (a) Explain the purpose of abstraction. (b) State four items of data stored each time a tool is hired. (c) The system processes the tool hire data; one process is to cancel a booking. State two other processes.", "Filter out; tool, customer, date, length, cost. Search, record booking, return.",
  "<p><b>(a)</b> " + mks(["To filter out information that is not necessary for the task, or to keep only what is necessary"]) + "</p><p><b>(b)</b> One mark for each two items: " + mks(["Tool ID, name or type", "Customer ID, name or address", "Hire ID", "Hire date", "Hire time", "Full or half day", "Cost of hire", "Payment details"], "a") + " (any four items)</p><p><b>(c)</b> Any two: " + mks(["Input customer details or tool ID", "Search for the required tool, or check it is available or returned", "Record, amend or create a tool booking, or record that a tool is returned", "Calculate the time the tool has to be returned"], "b") + "</p>", "Giving 'Customer' or 'Quantity' on its own. Name an actual data item.")

review = req("3 marks", "Identify", "A school trip system will send a reminder to parents about a trip. Identify three sub-modules and describe their use.", "Name and use.", "<p>" + mks(["GetTripDetails(): reads the date and place of the trip", "GetParentContact(): gets the contact details for each student's parent", "SendReminder(): sends the reminder message"]) + "</p>", None) + req("2 marks", "Explain", "Explain what is meant by abstraction using a food delivery app as an example.", "Filter out; keep.", "<p>" + mks(["Abstraction keeps only the data needed, such as the address, order items and cost", "and filters out information that is not needed, such as the driver's favourite music"]) + "</p>", None) + req("3 marks", "State", "State three items an abstract model for a library loan should store.", "Book, member, dates.", "<p>" + mks(["Book ID or title", "Member ID", "Date borrowed and due date"]) + "</p>", None) + req("2 marks", "State", "State two benefits of decomposing a large program into modules.", "Test, teams.", "<p>" + mks(["Each module is easier to code, test and debug", "Different programmers or teams can work on different modules"]) + "</p>", None) + req("1 mark", "Identify", "Identify the type of module that returns a value.", "Function.", "<p>" + mks(["Function"]) + "</p>", None)

tips = tips_html([
  ("Abstraction: filter out.", "Keep only what the task needs."),
  ("Decomposition: break into sub-problems.", "Leads to modules."),
  ("Module: name and use.", "Both marks, with the scenario."),
  ("Justify each item from the scenario.", "Mobile number: to send the text."),
  ("Function returns a value.", "Procedure does not."),
  ("Mention the scenario.", "Max 2 if you do not."),
], [("abstraction", "Filtering out information that is not necessary."), ("decomposition", "Breaking a problem into sub-problems."), ("a module", "A procedure or function."), ("an abstract model", "A simplified version holding only the needed data.")],
  [("State", "Short answer."), ("Describe", "Several points."), ("Identify", "Name and use."), ("Explain", "Reasons as well.")]) + FC

js = AKJS + AK20JS + r'''
(function () {
  const draw = (s) => { const k = Math.round(s.i); const items = ["car ID", "start date", "cost", "paint colour", "driver's music", "shoe size"]; let o = ""; items.forEach((t, i) => { const keep = i < 3; o += SV.rect(20 + (i % 3) * 170, 20 + Math.floor(i / 3) * 40, 150, 30, k >= 1 ? (keep ? "f1" : "cell") : "cell", { rx: 5, ...(k >= 1 && !keep ? op(0.3) : {}) }) + SV.text(95 + (i % 3) * 170, 40 + Math.floor(i / 3) * 40, t, "lbl", { "text-anchor": "middle", style: "font-size:12px" }); });
    o += SV.text(20, 125, ["a lot of information about each hire", "abstraction filters out what is not needed...", "...leaving the abstract model: easier to design and solve"][Math.min(k, 2)], "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stA"), { w: 520, h: 145, label: "Abstraction", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: ["Lots of information could be recorded about a car hire.", "<b>Abstraction</b> filters out what the task does not need.", "The <b>abstract model</b> keeps car, date and cost."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const m = ["GetOverdueLoan()", "IdentifyStudent()", "GetStudentEmail()", "CreateEmail()", "SendEmail()"]; let o = SV.rect(150, 10, 220, 30, "f3", { rx: 6 }) + SV.text(260, 30, "Email students with overdue books", "lbl bd", { "text-anchor": "middle", style: "font-size:11px" }); m.forEach((t, i) => { if (k >= 1) o += SV.path(`M260,40 L${60 + i * 100},70`, "ax", { style: "opacity:.4" }) + SV.rect(5 + i * 100, 70, 96, 30, i < k ? "f1" : "cell", { rx: 5 }) + SV.text(53 + i * 100, 89, t, "lbl", { "text-anchor": "middle", style: "font-size:9.5px" }); });
    o += SV.text(20, 130, ["one big problem", "split into sub-problems", "each module named for what it does", "", ""][Math.min(k, 2)], "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stB"), { w: 520, h: 145, label: "Decomposition", base: { i: 0 }, draw, tween: 100, dwell: 2200, steps: ["One large problem.", "<b>Decomposition</b> splits it into sub-problems.", "Each one becomes a module...", "...with its own name and use.", "Each module can be coded and tested separately."].map((c, i) => ({ cap: c, s: { i: Math.min(i, 5) } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const B = (x, t, on) => SV.rect(x, 40, 170, 40, on ? "f3" : "cell", { rx: 8 }) + SV.text(x + 85, 65, t, "lbl bd", { "text-anchor": "middle", style: "font-size:11px" }); let o = B(20, "SendEmail(student)", true) + B(300, "IsOverdue(loan)", k >= 1);
    o += SV.text(20, 110, ["a procedure does a task", "a function returns a value (TRUE or FALSE)", ""][Math.min(k, 2)], "lbl bd t3", { style: "font-size:13px" }); if (k >= 1) o += SV.text(300, 100, "returns TRUE", "sm"); return o; };
  Lib.stepper($("#stC"), { w: 520, h: 130, label: "Procedure and function", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: ["A <b>procedure</b> carries out a task.", "A <b>function</b> returns a value."].map((c, i) => ({ cap: c, s: { i } })) });
})();

(function () {
  const items = [["car ID", 1], ["customer ID", 1], ["start date", 1], ["return date", 1], ["cost", 1], ["car's colour", 0], ["customer's hobbies", 0], ["driver's music taste", 0]]; const sel = new Set(); const bar = $("#aB");
  const paint = () => { const ok = [...sel].filter((i) => items[i][1]).length, bad = [...sel].filter((i) => !items[i][1]).length; $("#aV").innerHTML = sel.size ? `You kept <b>${ok}</b> needed item(s)` + (bad ? ` and <b>${bad}</b> unnecessary one(s) that abstraction would filter out.` : ".") + (ok === 5 && !bad ? " That is the abstract model: only what the car hire task needs." : "") : "Click items to include them in the model."; };
  items.forEach(([t], i) => { const b = document.createElement("button"); b.textContent = t; b.onclick = () => { sel.has(i) ? sel.delete(i) : sel.add(i); b.className = sel.has(i) ? "on" : ""; paint(); }; bar.appendChild(b); }); paint();
})();
btnTable("dB", "dO", [
  ["Cinema booking", "SearchFilms(), SearchSeats(), CalculateCost(), BookSeats()", "Sub-problems of booking"],
  ["Charity donation app", "SelectCharity(), SpecifyAmount(), MakePayment(), ValidatePayment()", "Steps of a donation"],
  ["Loyalty card", "ScanCard(), GetPoints(), CalculatePoints(), UpdatePoints()", "Steps of a purchase"],
  ["Overdue book email", "GetOverdueLoan(), IdentifyStudent(), CreateEmail(), SendEmail()", "Steps to email a student"]
], ["Problem", "Modules", "Why"]);
btnTable("pB", "pO", [
  ["Display the discount on screen", "Procedure", "Does a task"],
  ["Calculate the cost of a booking and give it back", "Function", "Returns a value"],
  ["Check whether a seat is free (TRUE/FALSE)", "Function", "Returns a Boolean"],
  ["Send an email", "Procedure", "Does a task"]
], ["Module", "Type", "Why"]);
''' + _prjs

finish("as-9-1-abstraction-decomposition", "as91", "Abstraction and Decomposition",
  "Abstraction as filtering out unnecessary information, decomposition into sub-problems and modules, and how to answer the scenario questions, with animations, labs and the real Paper 2 questions from 2021 to 2026.",
  "9.1", "9 · Algorithm design and problem-solving", "section 9.1 Computational thinking skills", learn, watch, explore, _pr, real, where, past, review,
  "Part 1 is real 9618 questions on abstraction and decomposition (Paper 2), 2021 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", tips, js)
