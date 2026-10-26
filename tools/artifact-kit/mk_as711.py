"""AS CS 7.1.1: ethics, professional bodies, copyright and software licences. Run: python3 tools/artifact-kit/mk_as711.py"""
from ascs import *

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p><b>Ethics</b> is about acting responsibly and fairly towards colleagues, clients and the public. A programmer who joins a <b>professional ethical body</b> (such as the BCS, ACM or IEEE) follows <b>ethical guidelines</b>, gains recognition, and gets help, support and training. <b>Copyright</b> gives the author the legal right to control copying, changing and selling a program, so it protects their intellectual property and lets them take legal action against theft. A <b>software licence</b> states what users may do with the software: <b>commercial</b> (pay, no source code, no copying), <b>shareware</b> (free trial, then pay), <b>freeware</b> (free to use, source not available) and <b>open source / free software</b> (source code available, users may edit and redistribute, as defined by the Open Source Initiative and the Free Software Foundation). Exam answers name the licence and give reasons that fit the scenario.</p></div>

  <h2>1 · Acting ethically</h2>
  <div class="tw"><table class="t">
    <tr><th>Toward</th><th>A programmer should</th><th>Why</th></tr>
    <tr><td><b>Colleagues</b></td><td>Treat colleagues fairly and avoid discrimination; accept and offer critique; credit their contributions; help and train them</td><td>So technical work improves and colleagues feel valued and respected; a team works best when its members feel valued</td></tr>
    <tr><td><b>The public</b></td><td>Maintain their health, safety and welfare; be honest and realistic in claims about the software; keep the public's data secure; not spread malware</td><td>So that nobody is endangered and public trust is maintained</td></tr>
    <tr><td><b>Clients and the company</b></td><td>Act in the best interest of the product, the client and the profession; report errors found</td><td>An unreported error may make the product fail, let the client down and harm the profession</td></tr>
  </table></div>
  <p>Students on a school network should also respect privacy, not copy work that is not their own, not use social networking inappropriately or cyberbully, follow the school rules for the network, use it only for legitimate purposes and not hack other computers.</p>

  <h2>2 · Professional ethical bodies</h2>
  <p>Benefits of joining: there are <b>ethical guidelines to follow</b> (so clients and staff know the standards, and the programmer does not have to decide what is ethical because it is written down); clients know the programmer is <b>reputable</b> (there may be a test for entry), which gives <b>recognition</b> of skills; the body gives <b>help and support</b>, such as legal advice; and it runs <b>training courses</b> to keep skills up to date. Not joining may mean no legal advice if action is taken, fewer networking opportunities (and so contacts and jobs), less training and no clear ethical guidelines, possibly leading to unethical actions.</p>

  <h2>3 · Copyright</h2>
  <p>Copyright gives the owner legal recognition as the author and the right to stop others copying, changing or selling the program without permission. A programmer should copyright their program <b>to identify themselves as the owner</b> (formal recognition of ownership), <b>to allow legal consequences</b> if anyone steals or copies it, and to restrict competition.</p>

  <h2>4 · Software licences</h2>
  <div class="tw"><table class="t">
    <tr><th>Licence</th><th>Source code</th><th>Cost and use</th><th>Benefits</th></tr>
    <tr><td><b>Commercial</b></td><td>Not available; users cannot legally change or share it</td><td>A fee is charged before use; no free trial; limits on use (number of installs)</td><td>The developer earns a fee; support and maintenance (updates, bug fixes) usually provided; usually well tested; the program is copyrighted</td></tr>
    <tr><td><b>Shareware</b></td><td>Not available</td><td>Free trial (maybe with limited features or a time limit), then pay</td><td>Users can test before buying; no initial cost; the word spreads; the developer gets feedback and bug reports; income from users who buy</td></tr>
    <tr><td><b>Freeware</b></td><td>Not available</td><td>Free to use; usually cannot be changed or sold</td><td>Spreads widely at no cost to the user</td></tr>
    <tr><td><b>Open Source Initiative (OSI)</b></td><td>Available; users can edit and redistribute</td><td>Often free of charge; developer can still sell support and updates</td><td>Users can customise it, report and fix errors, add features and collaborate</td></tr>
    <tr><td><b>Free Software Foundation (FSF)</b></td><td>Available; users can run, study, change and redistribute</td><td>Free to use as freedom (not necessarily no cost)</td><td>As open source; the code stays free for others</td></tr>
  </table></div>
  <p>Choosing a licence: sell to the public and keep the code private: <b>commercial</b> (or shareware to let people try first). A business that needs to modify the code and pays for maintenance: <b>open source (OSI) or FSF</b>. A program whose wrong output could cause harm (such as one that reads allergen labels): an open licence is not appropriate because changed code might output wrong results, so people could buy the wrong item.</p>

  <h2>Common ways to lose marks</h2>
  <ul>
    <li>Naming a licence without reasons that fit the scenario (paying customers, a business that edits the code).</li>
    <li>Saying "open source is free" and stopping. The key idea is that the source code is available and can be edited and redistributed.</li>
    <li>Giving 'to protect the program' as the only benefit of copyright. Say it identifies the owner and allows legal action.</li>
    <li>Writing general statements about ethics, such as "act honestly", with no link to colleagues or the public.</li>
    <li>Mixing shareware (trial then pay) with freeware (free, no trial).</li>
  </ul>
'''

watch = '''
  <h2>1 · Copyright and a licence</h2>
  <div id="stA"></div>
  <h2>2 · What each licence lets the user do</h2>
  <div id="stB"></div>
  <h2>3 · Choosing a licence</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Licence chooser</h2>
  <p>Tick what the developer wants and see which licences fit.</p>
  <div class="card"><div id="lB" class="btnrow"></div><div id="lV" class="verdict"></div></div>
  <h2>Lab 2 · Ethical or not?</h2>
  <div class="card"><div id="eB" class="btnrow"></div><div id="eO"></div></div>
  <h2>Lab 3 · Licence features</h2>
  <div class="card"><div id="fB" class="btnrow"></div><div id="fO"></div></div>
'''

_pr, _prjs = PR(["Which licence?", "Ethical or unethical?", "Match the licence to its description", "Put the shareware steps in order", "Working out", "Multiple choice"],
  ("Which licence does the statement describe?", ["Commercial", "Shareware", "Open source / free software"], [("A fee is charged and the source code cannot be accessed", 0), ("Users can try the software before buying it", 1), ("Users can access and alter the source code", 2), ("Users can redistribute the software", 2), ("Users always get a trial period", 1), ("Users must always pay before they can use it", 0)], "Commercial: pay. Shareware: trial. Open source: edit."),
  ("Ethical or unethical for a programmer?", ["Ethical", "Unethical"], [("Crediting a colleague's contribution", 0), ("Hiding an error found in tested code to avoid trouble", 1), ("Making honest claims about what the software can do", 0), ("Copying a classmate's program as your own", 1), ("Keeping customers' data secure", 0), ("Using the school network to hack another computer", 1)], "Honest, fair, safe: ethical."),
  [["Commercial licence", "A fee, no source code, users cannot copy or change it"], ["Shareware", "Free trial, then the user pays"], ["Freeware", "Free to use, source code not available"], ["Open Source Initiative", "Source code available to edit and redistribute"], ["Copyright", "The legal right of the author to control copying and selling"]],
  ("Put the shareware process in order.", ["The developer releases a trial version", "The user tries it free of charge", "The user decides whether it meets their needs", "The user pays for the full version", "The developer receives income"], "Release, try, decide, pay, income."),
  [{"q": "A shareware trial lasts 30 days. A user starts on 1 March (day 1). On which day of March does the trial end (day 30)?", "a": 30, "unit": "", "tol": 0.01, "hint": "Day 30.", "sol": "<b>30</b> March."}, {"q": "A program sells for £20 and 5000 users buy it. How much income in pounds?", "a": 100000, "unit": "£", "tol": 0.5, "hint": "20 × 5000.", "sol": "<b>£100 000</b>."}, {"q": "10% of 8000 trial users buy the £15 full version. How much income in pounds?", "a": 12000, "unit": "£", "tol": 0.5, "hint": "800 × 15.", "sol": "<b>£12 000</b>."}, {"q": "A team has 4 programmers and an ethical body fee is £60 each per year. Total in pounds?", "a": 240, "unit": "£", "tol": 0.5, "hint": "4 × 60.", "sol": "<b>£240</b>."}, {"q": "How many licence types are in the Learn tab table?", "a": 5, "unit": "", "tol": 0.01, "hint": "Commercial, shareware, freeware, OSI, FSF.", "sol": "<b>5</b>."}],
  [("Shareware gives:", ["A free trial then payment", "No payment ever", "Source code", "No copyright"], 0, "Trial then pay."), ("Open source means:", ["The source code is available to edit", "The program is always free", "The program has no author", "No licence"], 0, "Source code available."), ("Copyright allows the author to:", ["Take legal action against copying", "Stop all use", "Ignore the law", "Avoid testing"], 0, "Legal action."), ("A professional ethical body provides:", ["Guidelines, support and training", "A compiler", "Free software", "A server"], 0, "Guidelines."), ("A commercial licence:", ["Does not allow users to change the code", "Gives the source code", "Is always free", "Allows free copying"], 0, "No changes."), ("Acting ethically toward the public includes:", ["Keeping data secure", "Hiding errors", "Copying code", "Overstating features"], 0, "Data security.")],
  [("Ethics", "Acting fairly and responsibly."), ("Ethical body", "Guidelines, recognition, support, training."), ("Copyright", "Owner's legal rights; legal action."), ("Commercial", "Fee; no source code; no copying."), ("Shareware", "Trial then pay."), ("Freeware", "Free; no source code."), ("Open source", "Source code available; edit and redistribute."), ("FSF / OSI", "Two open licence bodies.")])

real = RWNOTE + (
rw("A game with a free level", "You play the first level free and pay to unlock the rest: the shareware idea, so you can try before you buy.", "shareware.") +
rw("A browser anyone can improve", "The source code is public, so volunteers fix bugs and add features: open source.", "open source licence.") +
rw("Photos and music online", "Copying someone's work without permission is a breach of copyright and the owner can take action.", "copyright.") +
rw("A software engineer's code of conduct", "Members of the BCS agree to put the public interest first and keep their skills up to date.", "professional ethical body.") +
rw("A paid app with updates", "You pay once or subscribe, you cannot see the code, and the developer fixes bugs: a commercial licence.", "commercial licence.")
)

where = [
  ("M/J 2021", "12", "2(a), (c)", "2 + 4", "Why Aisha must act ethically toward her team; tick the licences that match four statements"),
  ("O/N 2021", "11, 13", "4(a), (b), (c)", "3 + 2 + 2", "Benefits of joining an ethical body; acting ethically with an unfamiliar IDE; why hiding an error is unethical"),
  ("M/J 2022", "11", "5(b)", "2", "Two types of licence that let others edit and redistribute"),
  ("O/N 2022", "13", "8(a)", "2 + 2", "Why some programs use an open source licence; how a programmer benefits from a commercial licence"),
  ("M/J 2023", "13", "5(b)", "4", "The most appropriate licence for a game sold to the public"),
  ("O/N 2023", "13", "6", "2 + 4", "Benefits of shareware; why join a professional ethical body"),
  ("O/N 2024", "11", "7", "2 + 2", "Benefits of shareware and commercial licences"),
  ("O/N 2024", "12", "5(a), (b)", "4 + 3 + 2", "Ethics toward colleagues and the public; a licence for modifiable code; why copyright"),
  ("O/N 2024", "13", "5", "3 + 3", "Name the licence from three statements; why join an ethical body"),
  ("M/J 2025", "12", "3(c)", "3 + 3", "Features of a commercial licence; why open source is not appropriate"),
  ("M/J 2025", "13", "3(d)", "3", "Consequences of not joining a professional ethical body"),
  ("O/N 2025", "11", "8(b)", "3", "Ethical considerations for a student on the school network"),
  ("O/N 2025", "13", "8(c)", "2", "Two licences that allow editing and redistribution of an OS")]

past = '''  <p class="note">The licence and ethical body questions repeat the same mark points year after year, so the lists on the Learn tab cover most of them. Questions are reworded from the papers; check the original paper and mark scheme for the exact wording.</p>
''' + peq(SRC("s21", "12", "Q2(a)(c)"), "2 + 4 marks", "Explain / Tick",
  "(a) Explain the reasons why it is important that Aisha acts ethically in relation to her team members. (c) The final game is released under a licence. Tick one or more boxes in each row to identify the licence(s) each statement describes (columns: commercial software, Free Software Foundation, Open Source Initiative, shareware). The user can edit the source code; the user must always pay before being able to use the software; the user can redistribute the software; the user always gets a trial period.", "Valued team, best work. Edit and redistribute: FSF and OSI; pay: commercial; trial: shareware.",
  "<p><b>(a)</b> Any two: " + mks(["To make sure the team members feel valued", "To get the best work out of the team", "To enable them to work well together", "To enable them to create the best product for the client"]) + "</p><p><b>(c)</b> " + mks(["Edit the source code: Free Software Foundation and Open Source Initiative", "Always pay: commercial software", "Redistribute: Free Software Foundation and Open Source Initiative", "Trial period: shareware"], "a") + "</p>", None) + peq(SRC("w21", "11/13", "Q4(a)(b)(c)"), "3 + 2 + 2 marks", "Describe / Explain",
  "(a) Francis has been advised to join a professional ethical body. Describe the benefits to Francis. (b)(i) He is unfamiliar with the IDE. Describe the ways in which Francis can act ethically. (c) Francis finds an error in part of the program that has already been tested but decides not to tell anyone. Explain the reasons why Francis acted unethically.", "Guidelines, recognition, support, training. Tell the manager; research; training. Best interest of the product, client, profession, company.",
  "<p><b>(a)</b> Any three: " + mks(["He has ethical guidelines to follow so clients and other staff know the standards being applied", "He does not have to decide what is ethical because it is written down", "Clients and staff know he is reputable, with recognition of his skills and knowledge", "They provide help and support, for example legal advice", "They run training courses to keep his skills up to date"]) + "</p><p><b>(b)(i)</b> Any two: " + mks(["Tell the manager he has not used it and how he will get up to date", "Perform his own research on how to use it", "Explain that he needs additional training or ask to be booked on a training course", "Ask for a mentor or to shadow someone", "Practise at home before starting"], "a") + "</p><p><b>(c)</b> Any two: " + mks(["He did not act in the best interest of the product, because it might fail", "He did not act in the best interest of the client, who has been let down", "He did not act in the best interest of the profession", "He did not act in the best interest of the company: not correcting the error early could lead to later problems"], "b") + "</p>", None) + peq(SRC("s22", "11", "Q5(b)"), "2 marks", "Identify",
  "The programmer wants to allow users to edit, improve and redistribute the program. Identify two different types of software licence that the programmer could use.", "Open Source Initiative; Free Software Foundation.",
  "<p>" + mks(["Open Source Initiative", "Free Software Foundation"]) + "</p>", None) + peq(SRC("w22", "13", "Q8(a)"), "2 + 2 marks", "Explain",
  "(i) Explain why some programs are distributed under an open source licence. (ii) Explain how a programmer benefits from distributing a program under a commercial licence.", "Customise, report errors, add features, collaborate. Copyrighted, protects code, prevents copies, fee.",
  "<p><b>(i)</b> Any two: " + mks(["To allow users to customise the code", "To allow errors to be reported, identified or fixed by users", "To allow additional features to be added to the code", "To allow for collaboration"]) + "</p><p><b>(ii)</b> Any two: " + mks(["Enables the program to be copyrighted", "Prevents illegal changes to the program and protects the source code", "Prevents illegal copies of the program being made", "A fee can be charged for the program"], "a") + "</p>", None) + peq(SRC("s23", "13", "Q5(b)"), "4 marks", "Identify / Justify",
  "A programmer is developing a computer game to sell to the public. Identify the most appropriate type of software licence for the game and justify your choice.", "Commercial or shareware.",
  "<p>One mark for the licence and one for each point (max 3). " + mks(["Commercial: the user has to pay so the programmer gains an income", "Commercial: enables the program to be copyrighted so the user cannot legally edit it and the programmer can take legal action against copying", "Shareware: the user can try the program free and then pay for the full game, so more people experience it and are more likely to buy"]) + "</p>", None) + peq(SRC("w23", "13", "Q6"), "2 + 4 marks", "State / Explain",
  "(a) State two benefits to a programmer of distributing a program using a shareware licence. (b) Explain why it is important for a programmer to join a professional ethical body.", "Trial, feedback, income, copyright. Guidelines, reputable, entry requirement, support, training.",
  "<p><b>(a)</b> Any two: " + mks(["Users can trial the program and may offer constructive feedback", "More people might try the program because the trial is free", "Bugs can be found and corrected on a wide range of systems", "Users who find the trial useful will buy the program, so the programmer gets income", "Allows the program to be copyrighted, protecting intellectual property"]) + "</p><p><b>(b)</b> Any four: " + mks(["The programmer has ethical guidelines to follow, so purchasers know the standards being applied", "so the programmer does not have to decide what is ethical", "Clients know the programmer is reputable, with recognition of their skills", "There may be an entry requirement or exam, so clients know they are competent", "The body provides help and support, such as legal advice", "The body runs training courses to keep skills up to date"], "a") + "</p>", None) + peq(SRC("w24", "11", "Q7"), "2 + 2 marks", "Give",
  "Software is distributed with a licence. (a) Give two benefits of distributing software using a shareware licence. (b) Give two benefits of using a commercial software licence.", "Trial, no initial cost, word spreads, feedback. Fee, support, well tested.",
  "<p><b>(a)</b> Any two: " + mks(["The user can trial the program before purchasing to see whether it meets their needs", "There is no initial cost", "Users who try the software may spread the word, so the developer gets more custom", "The developer can get feedback to improve the program"]) + "</p><p><b>(b)</b> Any two: " + mks(["The owner or developer can earn a fee", "Comprehensive support is usually offered, so problems can be easily solved", "The software is usually well tested, so there are few bugs"], "a") + "</p>", None) + peq(SRC("w24", "12", "Q5"), "4 + 3 + 2 marks", "Explain / Identify",
  "(a) Explain the reasons why a programmer needs to act ethically towards colleagues and the public. (b)(i) A program's source code can be modified by the business, which pays the programmer for maintenance and security updates. Identify a suitable licence and describe the reasons. (ii) Explain the reasons why the programmer should copyright their program.", "Fair, credit, critique. Health, safety, honest, data. OSI or FSF.",
  "<p><b>(a)</b> Max 2 each: " + mks(["Colleagues: treat colleagues fairly and avoid discrimination", "Colleagues: be prepared to accept or offer critique so technical work can be improved", "Colleagues: credit their contributions so they feel valued", "The public: maintain their health, safety and welfare so as not to endanger anyone", "The public: be honest and realistic in claims about the software so public trust is maintained", "The public: maintain the security of the public's data"]) + "</p><p><b>(b)(i)</b> " + mks(["Open Source Initiative or Free Software Foundation", "Allows the source code to be examined so the business can adapt it to their needs", "Allows the programmer to earn money for the software and updates"], "a") + "</p><p><b>(ii)</b> Any two: " + mks(["To identify themselves as the owner or author, and gain formal recognition of ownership", "To allow legal consequences if anyone steals or copies it", "To restrict competition"], "b") + "</p>", None) + peq(SRC("w24", "13", "Q5"), "3 + 3 marks", "Complete / Explain",
  "(a) Complete the table by writing the type of licence each statement describes: a fee is charged, the source code cannot be accessed, no free trial; users can try the software before buying it and may not access all features; software is usually free of charge and users can access and alter the source code. (b) Explain the reasons why it is important for the programmer to join a professional ethical body.", "Commercial; shareware; open source or free software.",
  "<p><b>(a)</b> " + mks(["Commercial", "Shareware", "Open source (or free software)"]) + "</p><p><b>(b)</b> Any three: " + mks(["The body has ethical guidelines to follow, so clients and staff know the standards being applied", "so the programmer does not have to decide what is ethical", "Clients and staff know the programmer is reputable, with recognition of their skills", "The body provides help and support, such as legal advice", "The body runs training courses to keep their skills up to date"], "a") + "</p>", None) + peq(SRC("s25", "12", "Q3(c)"), "3 + 3 marks", "Describe / Explain",
  "A computer program that reads and translates words on products is released under a commercial software licence. (i) Describe the features of a commercial software licence. (ii) Explain the reasons why an open source software licence might not be appropriate for the program.", "Fee, no source code, rights protected, limits, support. Source code changed, wrong output, wrong item.",
  "<p><b>(i)</b> Any three: " + mks(["The program is usually sold for a fee", "Users have no access to the source code", "It protects the intellectual rights of the developer", "Users cannot legally alter or share the program", "There are limitations on use, such as the number of installs", "Support and maintenance are usually provided"]) + "</p><p><b>(ii)</b> Any three: " + mks(["The source code would be accessible so it could be changed", "which might lead to the program outputting an incorrect response", "so people could purchase the wrong item", "which might have serious consequences, for example allergies"], "a") + "</p>", None) + peq(SRC("s25", "13", "Q3(d)"), "3 marks", "Describe",
  "Describe the possible consequences of the programmer not joining a professional ethical body.", "No legal advice, fewer contacts, less training, no guidelines.",
  "<p>Any three: " + mks(["There is no or limited access to legal advice in case action is taken against them", "There are fewer networking opportunities, so they could miss out on contacts or jobs", "There would be less access to training", "There would be no clear ethical guidelines or people to discuss ethical problems with", "possibly leading to inappropriate or unethical actions"]) + "</p>", None) + peq(SRC("w25", "11", "Q8(b)"), "3 marks", "Give",
  "Give three other ethical considerations for a student using their personal computer to connect to the school network (other than the risk of spreading malware).", "Privacy, no cyberbullying, no copying, school rules, legitimate use, no hacking.",
  "<p>Any three: " + mks(["Students should consider privacy issues", "Students should not make inappropriate use of social networking or engage in cyberbullying", "Students should not copy work that is not their own", "Students should abide by the school rules or guidelines for accessing the network", "Students should only use the school network for legitimate purposes", "Students should not hack other computers"]) + "</p>", None) + peq(SRC("w25", "13", "Q8(c)"), "2 marks", "Identify",
  "A programmer is developing an Operating System. Identify two types of software licence the programmer can use to allow other people to edit and redistribute the OS.", "OSI and FSF.",
  "<p>" + mks(["Open Source (Initiative)", "Free Software (Foundation)"]) + "</p>", None)

review = req("3 marks", "Explain", "Explain why a software company might choose a shareware licence for a new photo editor.", "Trial, buy, copyright.", "<p>" + mks(["Users can try it free, so more people use it", "those who find it useful pay for the full version, giving the company income", "the program is still copyrighted, so the code cannot legally be changed"]) + "</p>", None) + req("2 marks", "State", "State two benefits to a team of belonging to a professional ethical body.", "Guidelines, training.", "<p>" + mks(["Ethical guidelines to follow", "Training courses, help and support such as legal advice"]) + "</p>", None) + req("2 marks", "Explain", "Explain why a programmer who finds a security flaw in their company's software should report it.", "Public data, trust.", "<p>" + mks(["Customers' data could be put at risk if it is not fixed", "acting honestly protects public trust and the company's reputation"]) + "</p>", None) + req("3 marks", "Describe", "Describe three features of an open source software licence.", "Source code, edit, redistribute.", "<p>" + mks(["The source code is available", "Users can edit the program to their needs", "Users can redistribute it"]) + "</p>", None) + req("2 marks", "Explain", "Explain why copyright matters to a student who writes a program for a competition.", "Owner, action.", "<p>" + mks(["It identifies them as the owner of the program", "and lets them take legal action if someone copies or sells it"]) + "</p>", None)

tips = tips_html([
  ("Match the licence to the scenario.", "Pay and private: commercial. Edit: open."),
  ("Shareware: trial then pay.", "Not 'free'."),
  ("Open source: edit and redistribute.", "Name OSI and FSF."),
  ("Ethics: colleagues, public, client.", "Give a reason for each."),
  ("Ethical body: four benefits.", "Guidelines, reputable, support, training."),
  ("Copyright: owner and legal action.", "Two marks."),
], [("an ethical body", "A professional organisation with a code of conduct."), ("copyright", "The author's legal right to control copying."), ("shareware", "Software with a free trial then payment."), ("open source", "Software whose source code is available to edit.")],
  [("Identify", "Name it."), ("Explain", "Reasons as well."), ("Describe", "Several points."), ("Give", "Reasons or examples.")]) + FC

js = AKJS + AK20JS + r'''
(function () {
  const draw = (s) => { const k = Math.round(s.i); const B = (x, t, on) => SV.rect(x, 40, 130, 44, on ? "f3" : "cell", { rx: 8 }) + SV.text(x + 65, 67, t, "lbl bd", { "text-anchor": "middle", style: "font-size:12px" }); let o = B(20, "Programmer writes", true) + B(190, "Copyright", k >= 1) + B(360, "Licence", k >= 2) + SV.path("M150,62 H190", "ax") + SV.path("M320,62 H360", "ax");
    o += SV.text(260, 125, ["", "the author owns the work", "the licence says what users may do", ""][k], "lbl bd t3", { "text-anchor": "middle", style: "font-size:13px" }); return o; };
  Lib.stepper($("#stA"), { w: 540, h: 140, label: "Copyright", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: ["A programmer writes a program.", "<b>Copyright</b> gives them legal recognition as the owner.", "A <b>licence</b> sets out what users may do with it."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const rows = [["Commercial", [0, 0, 0, 1]], ["Shareware", [0, 0, 1, 1]], ["Open source", [1, 1, 0, 0]]]; const heads = ["edit source", "redistribute", "free trial", "must pay"];
  const draw = (s) => { const k = Math.round(s.i); let o = ""; heads.forEach((h, j) => o += SV.text(160 + j * 95, 18, h, "sm", { "text-anchor": "middle" })); rows.forEach(([n, v], i) => { o += SV.text(10, 50 + i * 34, n, "lbl bd", { style: "font-size:13px" }); v.forEach((x, j) => o += SV.rect(125 + j * 95, 32 + i * 34, 70, 28, i < k ? (x ? "f1" : "cell") : "cell", { rx: 5 }) + (i < k ? SV.text(160 + j * 95, 51 + i * 34, x ? "yes" : "no", "lbl", { "text-anchor": "middle", style: "font-size:12px" }) : "")); }); return o; };
  Lib.stepper($("#stB"), { w: 520, h: 140, label: "Licences", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: ["Compare what each licence allows.", "<b>Commercial</b>: no editing or redistributing, no trial, must pay.", "<b>Shareware</b>: a free trial, then pay; source not available.", "<b>Open source</b>: edit and redistribute the source code."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const sc = [["A business that wants to modify the code and pays for updates", "open source (OSI or FSF)"], ["A game sold to the public", "commercial or shareware"], ["A program that reads allergen labels", "commercial: no one can change the output"]][Math.min(k, 2)]; let o = SV.rect(20, 30, 480, 40, "cell", { rx: 6 }) + SV.text(30, 56, sc[0], "lbl", { style: "font-size:13px" }) + SV.rect(20, 90, 480, 40, "f1", { rx: 6 }) + SV.text(30, 116, "licence: " + sc[1], "lbl bd", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stC"), { w: 520, h: 150, label: "Choosing", base: { i: 0 }, draw, tween: 100, dwell: 2800, steps: ["The developer's business customer wants to edit the code: choose <b>open source</b>.", "A game sold to the public: <b>commercial</b> (or shareware for a trial).", "A program where wrong output could cause harm: not open source."].map((c, i) => ({ cap: c, s: { i } })) });
})();

(function () {
  const opts = [["wants income per copy", 0], ["wants users to try first", 1], ["wants users to edit the code", 2], ["code must stay private", 3]]; const sel = new Set();
  const paint = () => { let fit = ["Commercial", "Shareware", "Freeware", "Open source (OSI)", "Free software (FSF)"].filter((l) => { if (sel.has(0) && ["Freeware", "Open source (OSI)", "Free software (FSF)"].includes(l)) return false; if (sel.has(1) && l !== "Shareware") return false; if (sel.has(2) && !(l.startsWith("Open") || l.startsWith("Free software"))) return false; if (sel.has(3) && (l.startsWith("Open") || l.startsWith("Free software"))) return false; return true; });
    $("#lV").innerHTML = sel.size ? (fit.length ? "Fits: <b>" + fit.join(", ") + "</b>." : "No licence fits all of those at once.") : "Choose what the developer wants."; };
  const bar = $("#lB"); opts.forEach(([t, i]) => { const b = document.createElement("button"); b.textContent = t; b.onclick = () => { sel.has(i) ? sel.delete(i) : sel.add(i); b.className = sel.has(i) ? "on" : ""; paint(); }; bar.appendChild(b); }); paint();
})();
btnTable("eB", "eO", [
  ["Crediting a colleague's idea in a report", "Ethical", "Treat colleagues fairly and credit their work"],
  ["Hiding a bug so the release date is met", "Unethical", "Not in the best interest of the client"],
  ["Telling users honestly what the app cannot do", "Ethical", "Honest claims maintain public trust"],
  ["Selling users' data without telling them", "Unethical", "Does not protect the public's data"],
  ["Asking for training before using a new tool", "Ethical", "Acting competently"]
], ["Action", "Verdict", "Why"]);
btnTable("fB", "fO", [
  ["A fee is charged; source code cannot be accessed", "Commercial", "No free trial"],
  ["Try before buying; some features may be locked", "Shareware", "Free trial then pay"],
  ["Source code can be altered and redistributed", "Open source / FSF", "Collaboration"],
  ["Only the author may copy or change it", "Copyright", "Legal protection"]
], ["Statement", "Licence", "Key point"]);
''' + _prjs

finish("as-7-1-1-ethics-copyright-licences", "as711", "Ethics, Copyright and Software Licences",
  "Acting ethically toward colleagues, clients and the public, professional ethical bodies, copyright, and the commercial, shareware, freeware, open source and free software licences, with animations, a licence chooser and the real Paper 1 questions from 2021 to 2026.",
  "7.1.1", "7 · Ethics and ownership", "section 7.1 Ethics and ownership", learn, watch, explore, _pr, real, where, past, review,
  "Part 1 is real 9618 questions on ethics, copyright and software licences (Paper 1), 2021 to 2026. Part 2 is a set of review questions for practice; they are not in exam format.", tips, js)
