"""AS CS 12.1: program development life cycle. Run: python3 tools/artifact-kit/mk_as121.py"""
from ascs import *

def pc(text, label=None): return code(text.strip("\n").split("\n"), label=label)
def tbl(head, rows, cls="t"):
    return '<div class="tw"><table class="%s"><tr>%s</tr>%s</table></div>' % (cls, "".join("<th>%s</th>" % h for h in head), "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % c for c in r) for r in rows))

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>The <b>program development life cycle</b> splits a project into stages: <b>analysis</b> (what is needed), <b>design</b> (how it will work), <b>coding</b> (writing it), <b>testing</b> (does it work) and <b>maintenance</b> (keeping it working). In the <b>waterfall</b> model each stage is finished before the next starts, with the result of one stage passing down to the next and the option of returning to a previous stage. In <b>iterative</b> models, including <b>Rapid Application Development (RAD)</b>, working prototypes are built early and improved in cycles with the client involved throughout. Different life cycles exist because projects differ in size, in how clear the requirements are, and in how much the client will be involved. A life cycle makes a project easier to plan, manage and cost because each stage has clear deliverables.</p></div>

  <h2>1 · The stages and what happens in each</h2>
  ''' + tbl(["Stage", "Typical activities", "Output"], [
    ["<b>Analysis</b>", "Study the current system; interview managers and staff, survey users, observe the system in use; feasibility study; decide the life cycle; write the requirements", "Problem definition, requirements specification, documents about the current system (ER or data flow diagrams)"],
    ["<b>Design</b>", "Choose data structures, records and file structures; algorithms, flowcharts and pseudocode; program structure (modules, structure charts, state-transition diagrams); use of library routines; user interface and report layouts; test plan; choice of language and environment", "Design documents and a test plan"],
    ["<b>Coding</b>", "Write the program in a programming language from the design; use an IDE; fix syntax errors", "Working program code"],
    ["<b>Testing</b>", "Walkthroughs, dry runs with trace tables, running the program with test data; unit, integration, alpha, beta and acceptance testing", "Test results; a list of faults"],
    ["<b>Maintenance</b>", "Corrective (fix errors), adaptive (new hardware, rules, requirements) and perfective (improve it)", "An updated program"]]) + '''
  <p>Questions give an activity and ask for its stage. Useful anchors: <b>interviewing the client</b> or a <b>feasibility study</b> = analysis; <b>an identifier table</b>, <b>a flowchart</b>, <b>defining records and file structures</b>, <b>choosing a data structure</b> = design; <b>implementing an algorithm</b> or <b>syntax errors occur</b> = coding; <b>a trace table</b>, <b>a walkthrough</b>, <b>test plan results</b> = testing; <b>modifying the program for new hardware</b> = maintenance.</p>

  <h2>2 · Waterfall</h2>
  <ul>
    <li>The stages run in sequence: analysis, design, coding, testing, maintenance. The result of one stage is the input to the next.</li>
    <li><b>Downward arrows</b>: the result of one stage is passed on as the input to the next. <b>Upward arrows</b>: more work is needed at a previous stage to complete the current one (a design fault found in coding).</li>
    <li><b>Good:</b> predictable for budget and timeline; all requirements are identified before coding; each stage has clear documents.</li>
    <li><b>Poor:</b> no working software until late, so slow to market; late changes to requirements are hard to include; needs high involvement from the client at the start.</li>
  </ul>

  <h2>3 · Iterative and Rapid Application Development (RAD)</h2>
  <ul>
    <li>Work is divided into small increments or modules; each cycle produces a <b>prototype</b> that the client reviews, then improves.</li>
    <li><b>Principles:</b> modules developed in parallel or as prototypes; minimal detailed planning, so requirements can change; flexible; small releases each adding functionality; the client is involved at all stages.</li>
    <li><b>Benefits compared with waterfall:</b> quicker development and delivery of usable modules, a prototype at an early stage, easier to change requirements, early review and closer co-operation with the client.</li>
    <li><b>Drawbacks:</b> cost and time are difficult to estimate, documentation is often left out, and the client needs to be available (they may keep changing their mind).</li>
  </ul>
  ''' + tbl(["Scenario", "Better model", "Reason"], [["The client is unclear about the details and wants to see an early version", "Iterative / RAD", "a prototype early for the client to review"], ["The requirements are likely to change and being first to market matters", "Iterative / RAD", "quick delivery and easy changes"], ["A large project with fixed, well understood requirements and a fixed budget", "Waterfall", "predictable cost and timeline, no late changes"]]) + '''

  <h2>4 · Why a life cycle is used</h2>
  <p>It breaks a large problem into stages that are easier to manage, plan and cost; each stage has clear deliverables; teams can be allocated by stage or module. The choice of life cycle depends on the complexity of the problem, the size and skills of the team, the budget and time available, how fixed the requirements are, and how much the client will be involved.</p>

  <h2>Common ways to lose marks</h2>
  <ul>
    <li>Putting a design activity (identifier table, choice of data structure) under analysis or coding.</li>
    <li>Describing a model without a reason: for the scenario, say what it provides (a prototype early, changes easier).</li>
    <li>Saying "faster" for waterfall or RAD without saying why.</li>
    <li>Mixing up the arrows: down passes results on; up means returning to an earlier stage.</li>
  </ul>
'''

watch = '''
  <h2>1 · The waterfall model</h2>
  <div id="stA"></div>
  <h2>2 · Iteration and prototypes</h2>
  <div id="stB"></div>
'''

explore = '''
  <h2>Lab 1 · Which stage?</h2>
  <p>Click an activity to see its stage.</p>
  <div class="card"><div id="stB1" class="btnrow"></div><div id="stO1"></div></div>
  <h2>Lab 2 · Waterfall or RAD?</h2>
  <div class="card"><div id="wrB" class="btnrow"></div><div id="wrO"></div></div>
  <h2>Lab 3 · Change the requirement</h2>
  <p>The client changes the requirements part-way through. How much is redone?</p>
  <div class="card"><div class="btnrow"><label>Stage when the change arrives <select id="rq_st"><option value="1">After design</option><option value="2" selected>After coding</option><option value="3">After testing</option></select></label></div><div id="rqV"></div></div>
'''

_pr, _prjs = PR(["Which stage?", "Which model?", "Match the stage to its output", "Put the stages in order", "Working out", "Multiple choice"],
  ("Which stage of the life cycle?", ["Analysis", "Design", "Coding", "Testing", "Maintenance"], [("The client is interviewed about problems with the current system", 0), ("An identifier table is produced", 1), ("An algorithm is implemented in a programming language", 2), ("A trace table is produced", 3), ("The program is modified to run on new hardware", 4), ("Records and file structures are defined", 1)], "Find out, plan, write, check, keep up to date."),
  ("Which model fits the description?", ["Waterfall", "Iterative / RAD"], [("Each stage is finished before the next starts", 0), ("A prototype is produced at an early stage", 1), ("The client reviews each increment", 1), ("All requirements are identified before coding", 0), ("Late changes to requirements are hard to include", 0), ("Minimal detailed planning, so changes are easy", 1)], "Sequence: waterfall. Prototypes: RAD."),
  [["Analysis", "Requirements specification"], ["Design", "Algorithms, data structures and test plan"], ["Coding", "The program code"], ["Testing", "Test results and a fault list"], ["Maintenance", "An updated program"]],
  ("Put the waterfall stages in order.", ["Analysis", "Design", "Coding", "Testing", "Maintenance"], "A, D, C, T, M."),
  [{"q": "How many stages does the life cycle in this page have?", "a": 5, "unit": "", "tol": 0.01, "hint": "Analysis to maintenance.", "sol": "<b>5</b>."}, {"q": "A project has 12 modules developed in 4 equal parallel teams. How many modules does each team build?", "a": 3, "unit": "", "tol": 0.01, "hint": "12 ÷ 4.", "sol": "<b>3</b>."}, {"q": "A waterfall project has 5 stages of 2 months each. How many months until all stages are complete?", "a": 10, "unit": "", "tol": 0.01, "hint": "5 × 2.", "sol": "<b>10</b>."}, {"q": "A RAD project delivers a prototype every 3 weeks. How many prototypes are there in 15 weeks?", "a": 5, "unit": "", "tol": 0.01, "hint": "15 ÷ 3.", "sol": "<b>5</b>."}, {"q": "A feasibility study is part of which stage? (1 analysis, 2 design, 3 coding)", "a": 1, "unit": "", "tol": 0.01, "hint": "Done first.", "sol": "<b>1</b>: analysis."}],
  [("Which is a design activity?", ["Choosing a data structure", "Interviewing the client", "Fixing a syntax error", "Running beta testing"], 0, "Design."), ("The model with a prototype early:", ["Iterative / RAD", "Waterfall", "Neither", "Both"], 0, "RAD."), ("A drawback of RAD:", ["Cost and time are hard to estimate", "No prototypes", "Needs all requirements first", "No client contact"], 0, "Hard to estimate."), ("Upward arrows in the waterfall model mean:", ["Return to a previous stage", "Skip a stage", "Finish the project", "Cancel"], 0, "Rework."), ("A feasibility study belongs to:", ["Analysis", "Coding", "Testing", "Maintenance"], 0, "Analysis."), ("A trace table is produced in:", ["Testing", "Analysis", "Coding", "Maintenance"], 0, "Testing.")],
  [("Analysis", "Find out what is needed."), ("Design", "Plan how it will work."), ("Coding", "Write the program."), ("Testing", "Check it works."), ("Maintenance", "Keep it working."), ("Waterfall", "Stages in sequence."), ("RAD", "Prototypes and cycles."), ("Prototype", "An early working version.")])

real = RWNOTE + (
rw("A large bank system", "Requirements are fixed by law, cost has to be predictable, and each stage is signed off before the next: waterfall.", "waterfall.") +
rw("A start-up's new app", "It releases a basic version quickly, listens to users and adds features every few weeks.", "iterative / RAD.") +
rw("A school website", "The principal has ideas but not the details, so a first version is built and changed after review.", "prototype and iteration.") +
rw("A game after release", "Bugs are fixed with updates (corrective), and support for a new console is added later (adaptive).", "maintenance.")
)

where = [
  ("M/J 2022", "22", "1(b)", "4", "Name the life cycle stage for four activities"),
  ("M/J 2022", "23", "8", "3 + 2 + 1", "Complete a waterfall diagram; the meaning of its arrows; another model"),
  ("M/J 2023", "21", "5(a)", "2 + 1", "Two reasons waterfall is unsuitable for a changing website; a better model"),
  ("O/N 2021", "22", "2(b)", "2 + 3", "A suitable method for a client who is unclear on details; three design activities"),
  ("O/N 2022", "23", "1(b)(c)", "1 + 1 + 1 + 3", "A benefit of a life cycle; an analysis document; RAD principle, benefits and drawback"),
  ("O/N 2024", "21", "5(a)", "5", "Name the life cycle stage for five activities"),
  ("M/J 2025", "22", "1(a)", "1 + 1", "Why different life cycles exist; a consideration in choosing the language"),
  ("M/J 2026", "21", "3", "3 + 6", "Analysis activities; complete a summary of the development of a system"),
  ("M/J 2026", "23", "3", "4 + 4 + 3", "Complete a summary; two teams' life cycle models; design activities")]

past = '''  <p class="note">Life cycle questions are short and repeat. Learn the activities for each stage and the two models. The testing and maintenance terms that appear in the summary questions are on the next two pages (12.3.1 and 12.3.2).</p>
''' + peq(SRC("s22", "22", "Q1(b)"), "4 marks", "Complete",
  "Complete the table by writing the life cycle stage for each activity: an identifier table is produced; syntax errors can occur; the developer discusses the program requirements with the customer; a trace table is produced.", "Plan, write, find out, check.",
  "<p>One mark per row:" + tbl(["Activity", "Life cycle stage"], [["An identifier table is produced", "Design"], ["Syntax errors can occur", "Coding"], ["The developer discusses the program requirements with the customer", "Analysis"], ["A trace table is produced", "Testing"]]) + "</p>", "Putting a trace table under coding because the code is being run: a trace table checks that the algorithm works, which is testing.") + peq(SRC("w24", "21", "Q5(a)"), "5 marks", "Complete",
  "Complete the table by writing the name of the life cycle stage for each activity: the walkthrough method is used; an algorithm is implemented in a programming language; the client is interviewed about problems with the current system; the program is modified to run on new hardware; records and file structures are defined.", "Check, write, find out, keep up to date, plan.",
  "<p>One mark per row:" + tbl(["Activity", "Name of life cycle stage"], [["The walkthrough method is used", "Testing"], ["An algorithm is implemented in a programming language", "Coding"], ["The client is interviewed about problems with the current system", "Analysis"], ["The program is modified to run on new hardware", "Maintenance"], ["Records and file structures are defined", "Design"]]) + "</p>", None) + peq(SRC("s22", "23", "Q8"), "3 + 2 + 1 marks", "Complete / Explain / Identify",
  "A diagram shows the incomplete waterfall model with boxes labelled Analysis (first) and Maintenance (last) and empty boxes between. (a) Complete the diagram. (b) Explain the meaning of the downward and upward arrows. (c) Identify another type of model for the program development life cycle.", "Analysis, Design, Coding, Testing, Maintenance, with an arrow down and an arrow up between each pair.",
  "<p><b>(a)</b> " + mks(["At least three intermediate shapes, with at least one valid stage name", "Up and down arrows between each pair of shapes", "Design, Coding, Testing labels in the correct sequence"]) + "</p><p>Analysis → Design → Coding → Testing → Maintenance, with an up arrow and a down arrow between each pair.</p><p><b>(b)</b> " + mks(["Downward arrows: the result from one stage is the input passed to the next", "Upward arrows: more work is required at a previous stage to complete the current stage"], "a") + "</p><p><b>(c)</b> " + mks(["Iterative / Rapid Application Development (RAD)"], "a") + "</p>", "Drawing arrows in one direction only. Waterfall allows the return to an earlier stage.") + peq(SRC("s23", "21", "Q5(a)"), "2 + 1 marks", "Give / Identify",
  "Several companies are developing websites to market a new games console. The first company with a website that demonstrates the interactive features will have an advantage, and the requirements are likely to change as more information about the console is made available. One company uses the waterfall model. (i) Give two reasons why this may not be the most appropriate model. (ii) Identify a more appropriate model.", "No working software until late. Changes are slow to include.",
  "<p><b>(i)</b> Any two: " + mks(["No working software until late in the life cycle, so slower to market than the competitors (it does not allow early prototypes)", "More difficult and slower to cope with changes to the requirements", "Needs high involvement and feedback from the stakeholders or client"], "b") + "</p><p><b>(ii)</b> " + mks(["Iterative / Rapid Application Development (RAD)"], "a") + "</p>", None) + peq(SRC("w21", "22", "Q2(b)"), "2 + 3 marks", "Identify / State",
  "A company is developing a website for a school. The principal has some ideas about its appearance but is unclear about the details and would like to see an initial version. (i) Identify a suitable life cycle method and give a reason. (ii) The project has reached the design stage: state three activities that take place during the design stage.", "Prototype at an early stage. Data structures, algorithms, modules, interface.",
  "<p><b>(i)</b> " + mks(["Life cycle method: iterative / Rapid Application Development (RAD)", "Reason: it provides a working model (prototype) at an early stage for the principal to approve or review"], "a") + "</p><p><b>(ii)</b> Any three decisions made about: " + mks(["The data structures", "Algorithms, flowcharts or pseudocode", "The program structure (modules), library routines or the allocation of modules to a team", "The user interface or web page layout and content", "The testing method or test plan", "The choice of programming language or environment"], "b") + "</p>", "Describing the activity of a different stage, such as interviewing the principal (analysis).") + peq(SRC("w22", "23", "Q1(b)(c)"), "1 + 1 + 1 + 3 marks", "State / Give",
  "A designer is developing a website with a development life cycle. (b)(i) State one benefit of a life cycle. (ii) State one document that may be produced from the analysis stage. (c) The program is developed using Rapid Application Development (RAD). (i) State one principle of RAD. (ii) Give two benefits and one drawback of its use compared with the waterfall life cycle.", "Manage, plan; requirements; prototypes, parallel; quick, early review; hard to cost.",
  "<p><b>(b)(i)</b> " + mks(["It is easier to manage, plan and cost, or clear deliverables are produced at the end of each stage"], "a") + " <b>(ii)</b> " + mks(["The problem definition, the requirements specification, or documents about the current system (ER diagram, data flow diagram, feasibility study)"], "a") + "</p><p><b>(c)(i)</b> One of: " + mks(["Modules are developed in parallel or as prototypes", "Minimal detailed planning, which allows for changes", "A flexible development process", "Small incremental releases, each adding functionality", "The client is involved at all stages"], "a") + "</p><p><b>(ii)</b> Benefits (max 2): " + mks(["Quicker development, with many areas worked on at the same time", "A prototype is produced early", "Easier to change requirements, or quicker delivery of usable modules", "Early review and closer co-operation between client and developers"], "b") + " Drawback (max 1): " + mks(["Difficult to estimate cost or time", "Documentation is often omitted", "Lack of client availability, or the client can keep changing their mind"], "c") + "</p>", None) + peq(SRC("s25", "22", "Q1(a)"), "1 + 1 marks", "Explain / State",
  "A program is being developed to control the production line in a factory. (i) Explain the need for different program development life cycles. (ii) Coding is a stage in a life cycle. State one consideration that would influence the choice of programming language.", "The best approach depends on the project. Language suits the problem.",
  "<p><b>(i)</b> " + mks(["The choice of life cycle depends on the approach or method required to produce the program (or one factor such as the need for early prototypes, the complexity of the problem, the skills of the team, the budget, time and size of team, or how much the client is involved)"], "a") + "</p><p><b>(ii)</b> " + mks(["Which programming language would best suit the problem being solved (control of the production line)"], "a") + "</p>", None) + peq(SRC("s26", "21", "Q3(a)"), "3 marks", "State",
  "A business operates five call centres and the software in each is to be replaced by a new system developed by a software company. The analysis stage included a feasibility study. State three other activities carried out during the analysis stage.", "Find out about the current system and write the requirements.",
  "<p>Any three: " + mks(["Investigate the current system (or other similar systems)", "Discussions or interviews with managers", "Discussions or interviews with the staff who operate the system", "A survey of employees or customers (or a focus group)", "Observe the current system in use", "Produce the requirements specification", "Decide on the life cycle to be used"], "b") + "</p>", "Naming design activities such as drawing a flowchart.") + peq(SRC("s26", "23", "Q3"), "4 + 4 + 3 marks", "Complete / Identify / State",
  "A company wants to replace the point-of-sale software in each shop. (a) Complete the summary: the initial ___ stage is carried out by studying in detail the current system; a design for the new system is produced; after design and coding it is installed in only two shops and ___ testing is carried out; the final stage uses ___ testing to test all programs on the company's hardware and the company approves the new system; after installing it in all shops, unexpected bugs are reported and ___ maintenance has to be carried out. (b) Team A did the screen designs and outputs and involved the company at the earliest stage; Team B used a more traditional approach with an agreed sequence. Identify the life cycle model of each team and describe one additional feature of each. (c) State three design-stage activities.", "Analysis, beta, acceptance, corrective. RAD and waterfall.",
  "<p><b>(a)</b> One mark per gap: analysis; beta; acceptance; corrective.</p><p><b>(b)</b> Team A: " + mks(["Rapid Application Development (RAD) or iterative"], "a") + " plus one feature (max 2 marks): " + mks(["Large project broken into smaller steps", "All stakeholders or users involved at all stages", "Constant discussion between the client and the team", "A prototype available at an early stage", "More readily allows changes to the requirements", "Minimal planning required", "Modules developed in parallel"], "b") + " Team B: " + mks(["Waterfall"], "c") + " plus one feature (max 2 marks): " + mks(["The next stage does not start until the current stage is complete", "More predictable for budget and timeline", "All requirements identified before coding", "Late changes cannot be accommodated"], "d") + "</p><p><b>(c)</b> Any three: " + mks(["Produce flowcharts, structure charts, state-transition diagrams, structured English or ER diagrams", "Consider data storage (hardware, database, files)", "Design input screens, output screens or reports", "Select the programming language to be used"], "e") + "</p>", None)

review = req("5 marks", "Complete", "Name the stage of the life cycle for each activity: surveying staff; drawing a flowchart; writing the code; checking the output against the test plan; fixing a fault found after release.", "Analysis, design, coding, testing, maintenance.", "<p>" + mks(["Analysis", "Design", "Coding", "Testing", "Maintenance"]) + "</p>", None) + req("3 marks", "Describe", "Describe the waterfall model.", "Sequence, outputs, return to a previous stage.", "<p>" + mks(["The stages (analysis, design, coding, testing, maintenance) follow one another in sequence", "The output of each stage is the input to the next", "It is possible to return to an earlier stage to correct a fault"]) + "</p>", None) + req("3 marks", "Explain", "Explain why a RAD life cycle would suit a client who is unsure of their requirements.", "Prototype and feedback.", "<p>" + mks(["A prototype is built early", "The client reviews it and gives feedback", "Requirements are changed in the next iteration"]) + "</p>", None) + req("2 marks", "State", "State two documents produced in the analysis stage.", "The requirements.", "<p>" + mks(["The problem definition (requirements specification)", "The feasibility study, or a diagram of the current system"]) + "</p>", None) + req("2 marks", "Give", "Give two disadvantages of the waterfall model.", "Late and rigid.", "<p>" + mks(["No working software until late", "Changes to the requirements are hard to include"]) + "</p>", None)

tips = tips_html([
  ("Anchor each stage.", "Interview: analysis. Flowchart: design. Code: coding. Trace table: testing. New hardware: maintenance."),
  ("Prototype early.", "That is the reason for RAD in a scenario question."),
  ("Mention the scenario.", "Use the facts given: requirements change, client unclear."),
  ("Two arrow directions.", "Down passes on; up returns."),
  ("RAD drawbacks.", "Cost and time are hard to estimate; documentation is often missing."),
  ("Design is wider than you think.", "Data structures, algorithms, modules, interface, test plan."),
], [("analysis", "Finding out what is needed."), ("a prototype", "An early working version used to get feedback."), ("the waterfall model", "A life cycle with stages in sequence."), ("RAD", "Rapid Application Development: prototypes and iteration.")],
  [("State", "A short answer."), ("Identify", "Name it."), ("Explain", "Give a reason."), ("Complete", "Fill the table or diagram.")]) + FC

js = AKJS + AK20JS + r'''
(function () {
  const N = ["Analysis", "Design", "Coding", "Testing", "Maintenance"];
  const draw = (s) => { const k = Math.round(s.i); let o = ""; N.forEach((n, i) => { const y = 6 + i * 40; o += SV.rect(40, y, 150, 24, i === k ? "f3" : i < k ? "f1" : "cell", { rx: 5 }) + SV.text(115, y + 17, n, "lbl bd", { "text-anchor": "middle", style: "font-size:12px" }); if (i < N.length - 1) o += SV.text(85, y + 38, "↓", "lbl bd t3", { "text-anchor": "middle", style: "font-size:13px" }) + SV.text(145, y + 38, "↑", "lbl bd t2", { "text-anchor": "middle", style: "font-size:13px" }); }); return o; };
  Lib.stepper($("#stA"), { w: 230, h: 210, label: "Waterfall", base: { i: 0 }, draw, tween: 100, dwell: 2000, steps: ["Analysis: find out what is needed.", "Design: plan how it will work.", "Coding: write the program.", "Testing: check it works.", "Maintenance: keep it working. The up arrows allow a return to an earlier stage."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = ""; for (let i = 0; i < 4; i++) { const x = 10 + i * 90; o += SV.rect(x, 12, 80, 40, i < k ? "f3" : "cell", { rx: 6 }) + SV.text(x + 40, 36, "Version " + (i + 1), "lbl bd", { "text-anchor": "middle", style: "font-size:12px" }); if (i < 3) o += SV.text(x + 82, 36, "→", "lbl", { style: "font-size:14px" }); } o += SV.text(10, 78, ["The client has some ideas.", "Prototype 1: the client reviews it.", "Prototype 2: with the feedback built in.", "Prototype 3: more features.", "Final version: agreed with the client."][k], "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stB"), { w: 380, h: 94, label: "Iteration", base: { i: 0 }, draw, tween: 100, dwell: 2000, steps: ["Start with the client's ideas.", "Build the first prototype.", "Improve it from the feedback.", "Add more features.", "Repeat until the client is happy."].map((c, i) => ({ cap: c, s: { i } })) });
})();
btnTable("stB1", "stO1", [
  ["Interviewing the client about the current system", "Analysis", "finding out"],
  ["Defining records and file structures", "Design", "planning how it works"],
  ["Implementing an algorithm in a language", "Coding", "writing"],
  ["Using a walkthrough or a trace table", "Testing", "checking"],
  ["Modifying the program for new hardware", "Maintenance", "after release"],
  ["Choosing a data structure", "Design", "decided in design"]
], ["Activity", "Stage", "Why"]);
btnTable("wrB", "wrO", [
  ["Requirements likely to change; first to market wins", "Iterative / RAD", "prototype early, changes easy"],
  ["Large project, fixed requirements, fixed budget", "Waterfall", "predictable cost and time"],
  ["Principal unclear on details, wants to see an early version", "Iterative / RAD", "client reviews a prototype"],
  ["All requirements are signed off before coding starts", "Waterfall", "no late changes"]
], ["Scenario", "Model", "Why"]);
(function () {
  const sel = $("#rq_st"); const paint = () => { const k = +sel.value; const wf = k === 1 ? "design, coding and testing may need to be redone" : k === 2 ? "the design, the code and the testing may need to be redone" : "almost everything is redone, and the product may already be released"; const rad = "only the current prototype is changed, in the next cycle"; $("#rqV").innerHTML = `<div class="tw"><table class="t"><tr><th>Model</th><th>Effect of the change</th></tr><tr><td>Waterfall</td><td>${wf}</td></tr><tr><td>Iterative / RAD</td><td>${rad}</td></tr></table></div><div class="verdict">A change late in a waterfall project is expensive; an iterative project absorbs it in the next prototype.</div>`; };
  sel.onchange = paint; paint();
})();
''' + _prjs

finish("as-12-1-program-development-life-cycle", "as121", "Development Life Cycle",
  "The stages of the program development life cycle, the waterfall and iterative or RAD models, and choosing a model for a scenario, with animations, labs and the real Paper 2 questions from 2021 to 2026.",
  "12.1", "12 · Software development", "section 12.1 Program development life cycle", learn, watch, explore, _pr, real, where, past, review,
  "Part 1 is real 9618 questions on the program development life cycle (Paper 2), 2021 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", tips, js)
