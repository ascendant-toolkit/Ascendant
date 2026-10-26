"""A Level CS syllabus 20.1.4: declarative programming (facts, rules, goals). Run: python3 tools/artifact-kit/mk_ac2014.py"""
from ak20 import *

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p><b>Declarative programming</b> tells the computer <i>what</i> is true and what answer is wanted, not <i>how</i> to find it. A program is a set of <b>facts</b> (things that are true) and <b>rules</b> (things that are true if other things are true), which together form a <b>knowledge base</b>. You run it by asking a <b>goal</b> (a query): the system searches the facts and rules and returns every answer that satisfies it. Names that start with a lower-case letter are <b>constants</b>; names that start with a capital letter are <b>variables</b> that the system fills in. In the exam you write extra facts from a description, say what a goal returns, and write a rule or a goal using AND and NOT.</p></div>

  <h2>1 · What declarative means</h2>
  <div class="tw"><table class="t">
    <tr><th></th><th>Imperative</th><th>Declarative</th></tr>
    <tr><td>You write</td><td>The steps, in order</td><td>Facts and rules, then a goal</td></tr>
    <tr><td>Who decides how?</td><td>The programmer</td><td>The system, by searching the knowledge base</td></tr>
    <tr><td>Finding the domestic cats</td><td>Loop through every cat, test its type, add it to a list</td><td><code>type(Pet, domestic).</code></td></tr>
    <tr><td>Typical use</td><td>Most programs</td><td>Questions over knowledge: expert systems, databases, family trees</td></tr>
  </table></div>
  <p>Declarative languages are <b>logic</b> programming (facts, rules and goals, such as Prolog) or <b>functional</b> programming (the program is built by applying functions to arguments). The exam uses the logic style.</p>

  <h2>2 · Facts</h2>
  <p>A fact is a <b>predicate</b> with arguments in brackets and a full stop. The meaning of each argument depends on its position, and you decide the order, so be consistent.</p>
  <div class="tw"><table class="t">
    <tr><th>Fact</th><th>Meaning</th></tr>
    <tr><td><code>type(leopard, wild).</code></td><td>A leopard is a type of wild cat</td></tr>
    <tr><td><code>hair(lion, short).</code></td><td>A lion has short hair</td></tr>
    <tr><td><code>customer(petrov).</code></td><td>Petrov is a customer</td></tr>
    <tr><td><code>owns(projector, petrov).</code></td><td>Petrov owns a projector (device first, owner second)</td></tr>
  </table></div>
  <p><b>One-argument facts</b> such as <code>customer(petrov).</code> say that something is a member of a kind. They matter: rules use them to say what kind of thing a variable can be.</p>
  <div class="tip"><b class="h">Adding facts from a description</b>"Betty is a customer who owns a large TV and wants a Blu-ray player." This needs one fact for each statement: <code>customer(betty).</code> <code>owns(large_tv, betty).</code> <code>wants(bluray_player, betty).</code> Use the exact constants already in the knowledge base (<code>large_tv</code>, <code>bluray_player</code>), the same argument order, and lower case. A brand-new person or item also needs its "is a" fact (<code>customer(betty).</code>), and the mark scheme counts it.</div>

  <h2>3 · Goals and variables</h2>
  <p>A <b>goal</b> asks a question. Put a <b>variable</b> (capital first letter) where you want the answer. The system tries every fact with the same predicate, keeps the ones that match, and returns all the values the variable can take, in the order of the facts.</p>
  <div class="tw"><table class="t">
    <tr><th>Goal</th><th>Returns</th></tr>
    <tr><td><code>hair(Cat, medium)</code></td><td>Cat = leopard, cheetah, savannah</td></tr>
    <tr><td><code>type(Pet, domestic)</code></td><td>Pet = persian</td></tr>
    <tr><td><code>hair(lion, short)</code></td><td>true (no variable: a yes/no question)</td></tr>
    <tr><td><code>hair(Cat, purple)</code></td><td>false (nothing matches)</td></tr>
  </table></div>
  <p>A goal can have <b>several conditions</b> joined with <code>,</code> (AND). The <b>same variable</b> in two conditions links them: it must take one value that satisfies both.</p>
  <pre class="plain">spots(WildSpotty, yes), type(WildSpotty, wild)

spots(_, yes): leopard, cheetah, savannah
type(_, wild): leopard, lion, cheetah
Both:          leopard, cheetah</pre>

  <h2>4 · Rules</h2>
  <p>A <b>rule</b> says that something is true <b>if</b> other conditions are true. It has a head (what is being defined), the word <code>IF</code>, and a body of conditions joined with <code>AND</code> (or a comma), and <code>NOT</code> for "is not true".</p>
  <pre class="plain">may_buy_device(D, A)
   IF device(D) AND customer(A) AND NOT owns(D, A).

may_buy_device(D, A) IF device(D), customer(A), NOT owns(D, A).    // same rule</pre>
  <p>Read it as: <i>D may be available for A to buy if D is a device and A is a customer and A does not own D.</i> The three marks for the conditions come from <b>device(D)</b>, <b>customer(A)</b> and <b>owns(D, A)</b>, and a fourth for correct operators and punctuation.</p>
  <ul>
    <li>List <b>one condition for each "is a" in the sentence</b>, then the extra condition.</li>
    <li>Put <code>NOT</code> before the condition that must fail, and put the "is a" conditions <b>first</b>, so the variables are filled in before NOT is tested.</li>
    <li>The mark scheme accepts <code>,</code> for AND and, for SWISH Prolog, <code>\\+</code> for NOT. It does not accept extra lines of code.</li>
  </ul>
  <div class="tw"><table class="t">
    <tr><th>Exam notation</th><th>Prolog</th></tr>
    <tr><td><code>father(X, Y) IF male(X) AND parent(X, Y).</code></td><td><code>father(X, Y) :- male(X), parent(X, Y).</code></td></tr>
    <tr><td><code>NOT owns(D, A)</code></td><td><code>\\+ owns(D, A)</code></td></tr>
  </table></div>

  <h2>5 · How the system answers</h2>
  <ol>
    <li>Take the first condition and look through the facts for matches. Each match fills the variables.</li>
    <li>For each match, test the next condition using the values already filled in.</li>
    <li>A <b>NOT</b> condition succeeds only if the fact is <b>not</b> found.</li>
    <li>Every way of satisfying all the conditions is an answer. If none exists the answer is false.</li>
  </ol>

  <h2>6 · Common ways to lose marks</h2>
  <ul>
    <li>Writing a constant with a capital letter (<code>Betty</code>) or a variable with a lower-case one. Capital means variable.</li>
    <li>Leaving out the "is a" fact for a new person or item, or the full stop at the end of a fact.</li>
    <li>Changing the argument order from the one in the knowledge base.</li>
    <li>In a rule, forgetting a condition (for example <code>customer(A)</code>), or putting NOT on the wrong one.</li>
    <li>Listing results in the goal answer that do not match, or leaving some out. Check every fact with that predicate.</li>
    <li>Adding extra lines or text to a rule or goal that asks for a single line.</li>
    <li>Describing declarative as "no loops". Say it states <b>what</b> is wanted using facts and rules, and the system works out how.</li>
  </ul>
'''

watch = '''
  <h2>1 · How a goal is matched against the facts</h2>
  <p>Press Play, or click the steps. The goal <code>hair(Cat, medium)</code> is tried against every <code>hair</code> fact.</p>
  <div id="stA"></div>
  <h2>2 · Two conditions with one variable</h2>
  <div id="stB"></div>
  <h2>3 · Evaluating a rule with NOT</h2>
  <div id="stC"></div>
  <h2>4 · Imperative or declarative?</h2>
  <div id="stD"></div>
'''

explore = '''
  <h2>Lab 1 · Ask the knowledge base a goal</h2>
  <p>Choose a knowledge base, then type a goal or pick an example. Variables start with a capital letter. Join conditions with a comma.</p>
  <div class="card"><div id="kB" class="btnrow"></div><div id="kF"></div>
    <div class="btnrow" id="kE"></div>
    <p><input id="kQ" type="text" style="width:100%;padding:8px;border:1px solid var(--line);border-radius:8px;font:500 .95rem var(--mono)" aria-label="Goal"></p>
    <div class="btnrow"><button class="b pri" id="kR">Run the goal</button></div>
    <div class="verdict" id="kV"></div></div>

  <h2>Lab 2 · Evaluate a rule</h2>
  <p>A rule is true for every combination of values that satisfies all its conditions. Edit the conditions to see the answers change.</p>
  <div class="card"><div id="rB" class="btnrow"></div><p><code id="rH"></code> IF</p>
    <p><input id="rQ" type="text" style="width:100%;padding:8px;border:1px solid var(--line);border-radius:8px;font:500 .95rem var(--mono)" aria-label="Rule conditions"></p>
    <div class="btnrow"><button class="b pri" id="rR">Evaluate the rule</button></div>
    <div id="rO"></div><div class="verdict" id="rV"></div></div>

  <h2>Lab 3 · Mistakes in facts, goals and rules</h2>
  <div class="card"><div id="eB" class="btnrow"></div><div id="eO"></div></div>
'''

practise = '''
  <h2>1 · Fact, goal or rule?</h2><div id="cl1" class="card"></div>
  <h2>2 · Constant or variable?</h2><div id="cl2" class="card"></div>
  <h2>3 · Put the steps of answering a goal in order</h2><div id="o1" class="card"></div>
  <h2>4 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>5 · What does the goal return? (count the answers)</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("An expert system", "A medical or car-repair helper holds facts about symptoms and rules such as 'the fault may be the battery if the lights are dim and the engine does not turn'. The user states what they see and the system reasons its way to answers.", "declarative systems are used where knowledge is a set of facts and rules and the answer is found by search.") +
rw("A family tree", "Facts say who is a parent of whom. A rule defines grandparent as a parent of a parent, and the same rule answers for any family without a loop being written.", "rules built from other rules and facts: describe the relationship once.") +
rw("A database query", "SQL is also declarative: SELECT name FROM Cat WHERE type = 'domestic' says what rows are wanted, not how to scan the table.", "like a goal, it states the result wanted and the system works out how.") +
rw("A timetable or planning tool", "Facts say which teachers can teach which subjects and which rooms are free. A rule defines when a lesson may be placed. The system tries combinations to find one that satisfies every rule.", "searching for answers that satisfy all conditions at once.") +
rw("A shop recommendation rule", "may_buy(Device, Customer) IF device(Device) AND customer(Customer) AND NOT owns(Device, Customer) finds everything a customer does not already own.", "NOT is used for 'does not already have' conditions.")
)

where = [
  ("M/J 2022", "31, 33", "2(a), (b), (c)", "2 + 1 + 1 + 2", "Cats: add facts, result of a goal, write two goals"),
  ("M/J 2022", "32", "2(a), (b), (c)", "2 + 1 + 4", "School: add facts, result of a goal, goal with a shared variable"),
  ("O/N 2023", "31, 33", "11(a), (b), (c)", "3 + 1 + 4", "Subjects: add facts, result of a goal, write a rule with NOT"),
  ("O/N 2023", "32", "11(a), (b), (c)", "4 + 1 + 4", "Hobbies: add facts, result of a goal, write a rule with NOT"),
  ("M/J 2024", "31, 33", "8(a), (b), (c)", "3 + 1 + 4", "Car features: add facts, result of a goal, write a rule with NOT"),
  ("M/J 2024", "32", "10(a), (b), (c)", "4 + 1 + 4", "Beach activities: add facts, result of a goal, write a rule with NOT"),
  ("M/J 2026", "31", "11(a), (b), (c)", "3 + 1 + 4", "Home cinema: add facts, result of a goal, write a rule with NOT")]

past = '''  <p class="note">A declarative question has appeared in Paper 3 in May/June 2022, Oct/Nov 2023, May/June 2024 and May/June 2026, always in the same three parts: add facts, give the result of a goal, write a rule or goal. Declarative programming has not been asked in Paper 4. (Paper 3 questions on the paradigm in general are on the first page of this chapter.) The knowledge bases are shortened to the facts the question needs; check the original paper for all the clauses. Questions are reworded from the papers.</p>

  <h3>Cats and the school: facts, goals and a shared variable</h3>
''' + peq(SRC("s22", "31, 33", "Q2"), "2 + 1 + 1 + 2 marks", "Write",
  "A declarative language represents facts about cats." + qcode('''01 type(leopard, wild).
02 type(lion, wild).
03 type(cheetah, wild).
04 type(savannah, hybrid).
05 type(persian, domestic).
07 hair(leopard, medium).
08 hair(lion, short).
09 hair(cheetah, medium).
10 hair(savannah, medium).
11 hair(persian, long).
13 spots(leopard, yes).
14 spots(lion, no).
15 spots(cheetah, yes).
16 spots(savannah, yes).
17 spots(persian, no).''') + "Clause 01 means a leopard is a type of wild cat; 08, a lion has short hair; 16, a savannah has spots. (a) A caracal is a wild cat with short hair. Write the additional clauses 18 and 19. (b) Using the variable Cat, the goal <code>hair(Cat, medium)</code> returns Cat = leopard, cheetah, savannah. Write the result of the goal <code>hair(Cat, long)</code>. (c)(i) Write the goal, using the variable Pet, to find all the domestic cats. (ii) Write the goal, using the variable WildSpotty, to find all the wild cats with spots.",
  "(a) two clauses, one for the type and one for the hair. (c)(ii) needs two conditions sharing one variable.",
  "<p><b>(a)</b> " + mks(["type(caracal, wild).", "hair(caracal, short)."]) + " <b>(b)</b> " + mks(["Cat = persian"], "a") + "</p><p><b>(c)(i)</b> " + mks(["type(Pet, domestic)."], "a") + " <b>(c)(ii)</b> " + mks(["spots(WildSpotty, yes)", ", type(WildSpotty, wild)."], "a") + "</p>",
  "Writing the facts with capital letters or changing the argument order, for example <code>wild(caracal).</code>.") + peq(SRC("s22", "32", "Q2"), "2 + 1 + 4 marks", "Write",
  "A declarative language represents facts about a school." + qcode('''01 teaches(alan, mathematics).      06 studies(ahmed, history).
02 teaches(ioana, geography).      07 studies(freya, history).
03 teaches(nina, history).         08 studies(kim, history).
04 teaches(alan, statistics).      09 studies(freya, geography).
                                   10 studies(hua, mathematics).
14 tutors(alan, kim).              11 studies(hua, statistics).
15 tutors(alan, hua).              12 studies(hua, geography).
16 tutors(alan, freya).
17 tutors(nina, ahmed).''') + "(a) Sam studies history and Nina is his tutor. Write the additional clauses 18 and 19. (b) Using the variable Student, the goal <code>studies(Student, history)</code> returns Student = freya, ahmed, kim. Write the result of the goal <code>studies(Student, geography)</code>. (c) Write the goal, using the variable X, to find all the students who have a tutor that teaches them. For example, Hua has Alan for a tutor and is also taught mathematics by Alan.",
  "(c) Three conditions: a teacher R teaches a subject S, X studies S, and R tutors X. One mark each for X, two other variables in the right places, three clauses, and syntax.",
  "<p><b>(a)</b> " + mks(["studies(sam, history).", "tutors(nina, sam)."]) + " <b>(b)</b> " + mks(["Student = freya, hua (either order)"], "a") + "</p><p><b>(c)</b> Four marks: " + mks(["correct use of X", "two other variables in correct positions", "three correct clauses in any order", "correct syntax"]) + "</p>" + qcode('''teaches(R, S), studies(X, S), tutors(R, X).'''),
  "Using different variable names for the subject in the teaches and studies conditions, so the two are not linked.") + '''
  <h3>Writing rules with NOT</h3>
''' + peq(SRC("w23", "31, 33", "Q11"), "3 + 1 + 4 marks", "Write",
  "A declarative language represents subjects that students can choose to study. Students must choose two subjects." + qcode('''01 subject(mathematics).   09 student(tomaz).      15 choice1(tomaz, mathematics).
02 subject(physics).       10 student(josephine).  16 choice1(teresa, chemistry).
03 subject(chemistry).     11 student(elspeth).    17 choice1(pietre, mathematics).
04 subject(computer_science). 12 student(nico).    18 choice1(nico, mathematics).
05 subject(geography).     13 student(teresa).     19 choice1(elspeth, chemistry).
06 subject(history).       14 student(pietre).     20 choice2(tomaz, computer_science).
07 subject(english).                               21 choice2(nico, geography).
08 subject(biology).''') + "(a) Anthony is a student who would like to study history and geography. Write the additional clauses 22 to 24. (b) Using the variable X, the goal <code>choice1(X, chemistry)</code> returns X = teresa, elspeth. Write the result of the goal <code>choice1(X, mathematics)</code>. (c) N may choose S if N is a student and S is a subject and N has not chosen S as the first choice. Write this as a rule: <code>may_choose_subject(N, S) IF ...</code>",
  "(a) A new student needs a student fact as well as the two choices. (c) Two 'is a' conditions and one NOT.",
  "<p><b>(a)</b> " + mks(["student(anthony).", "choice1(anthony, history).", "choice2(anthony, geography)."]) + " <b>(b)</b> " + mks(["X = tomaz, pietre, nico"], "a") + "</p><p><b>(c)</b> Four marks: " + mks(["student(N)", "subject(S)", "choice1(N, S) (with NOT)", "all operators correct, with no additional code"]) + "</p>" + qcode('''may_choose_subject(N, S)
   IF student(N) AND subject(S) AND NOT choice1(N, S)'''),
  "Writing choice1(anthony, geography). He chooses history first and geography second, so geography is choice2.") + peq(SRC("w23", "32", "Q11"), "4 + 1 + 4 marks", "Write",
  "A declarative language represents facts about people and their hobbies." + qcode('''01 hobby(music).        07 person(toby).      13 enjoys(natasha, travelling).
02 hobby(caving).       08 person(natasha).   14 enjoys(toby, climbing).
03 hobby(climbing).     09 person(fatima).    15 enjoys(nina, climbing).
04 hobby(camping).      10 person(joseph).    16 enjoys(elijah, camping).
05 hobby(baking).       11 person(elijah).    17 enjoys(fatima, baking).
06 hobby(travelling).   12 person(nina).      18 enjoys(joseph, camping).
                                              19 dislikes(toby, caving).''') + "(a) Carlos is a person who enjoys the hobby of cycling but does not like music. Write the additional clauses 20 to 23. (b) Using the variable P, the goal <code>enjoys(P, camping)</code> returns P = elijah, joseph. Write the result of <code>enjoys(P, climbing)</code>. (c) N is a person who might enjoy H if H is a hobby and N does not dislike H. Write this as a rule: <code>might_enjoy(N, H)</code>.",
  "(a) cycling is a new hobby, so it needs its own hobby fact. (c) NOT goes on the dislikes condition.",
  "<p><b>(a)</b> " + mks(["person(carlos).", "hobby(cycling).", "enjoys(carlos, cycling).", "dislikes(carlos, music)."]) + " <b>(b)</b> " + mks(["P = toby, nina"], "a") + "</p><p><b>(c)</b> Four marks: " + mks(["person(N)", "hobby(H)", "dislikes(N, H) (with NOT)", "all operators correct, no additional code"]) + "</p>" + qcode('''might_enjoy(N, H)
   IF person(N) AND hobby(H) AND NOT dislikes(N, H)'''),
  "Leaving out hobby(cycling). The hobby is new, and music already exists, so only cycling needs the fact.") + peq(SRC("s24", "31, 33", "Q8"), "3 + 1 + 4 marks", "Write",
  "A declarative language represents the features that are available and unavailable on different body styles of a car." + qcode('''01 feature(sunroof).            10 bodystyle(saloon).        15 available(sunroof, hatchback).
02 feature(automatic_tailgate). 11 bodystyle(hatchback).     16 available(sunroof, minivan).
03 feature(heated_seats).       12 bodystyle(estate).        17 available(reversing_camera, hatchback).
04 feature(extra_seats).        13 bodystyle(minivan).       18 available(extra_seats, minivan).
05 feature(reversing_camera).   14 bodystyle(convertible).   19 available(reversing_camera, saloon).
06 feature(dashboard_camera).                                20 unavailable(sunroof, convertible).
07 feature(air_conditioning).                                 21 unavailable(automatic_tailgate, saloon).
08 feature(heated_windscreen).                                22 unavailable(extra_seats, hatchback).
09 feature(satnav).''') + "(a) Sliding doors is a feature that is available on a minivan but unavailable on a hatchback. Write the additional clauses 23 to 25. (b) Using the variable Options, the goal <code>available(Options, saloon)</code> returns Options = reversing_camera. Write the result of <code>available(Options, hatchback)</code>. (c) F may be available for B if F is a feature and B is a body style and F is not unavailable for that body style. Write this as a rule: <code>may_choose_option(F, B) IF ...</code>",
  "(a) three facts: the new feature, where it is available, where it is unavailable. (c) the NOT is on unavailable(F, B).",
  "<p><b>(a)</b> " + mks(["feature(sliding_doors).", "available(sliding_doors, minivan).", "unavailable(sliding_doors, hatchback)."]) + " <b>(b)</b> " + mks(["Options = sunroof, reversing_camera"], "a") + "</p><p><b>(c)</b> Four marks: " + mks(["feature(F)", "bodystyle(B)", "unavailable(F, B) (with NOT)", "all operators and punctuation correct (a comma is allowed for AND), no additional code"]) + "</p>" + qcode('''may_choose_option(F, B)
   IF feature(F) AND bodystyle(B) AND NOT unavailable(F, B).'''),
  "Writing the rule with <code>available(F, B)</code>. The rule is about features that are <i>not unavailable</i>, which includes those with no entry at all.") + peq(SRC("s24", "32", "Q10"), "4 + 1 + 4 marks", "Write",
  "A declarative language allows clients to choose daily activities at the beach." + qcode('''01 activity(paddleboarding).   06 client(stevie).    16 choice(petra, rowing).
02 activity(sailing).          07 client(antonio).   17 choice(frankie, sailing).
03 activity(rowing).           08 client(henry).     18 choice(erik, sailing).
04 activity(kayaking).         09 client(eliza).     19 choice(eliza, rowing).
05 activity(jetskiing).        10 client(rebeka).    20 choice(stevie, jetskiing).
                               ...                   21 choice(henry, sailing).
                               15 client(frankie).   22 done(henry, jetskiing).
                                                     23 done(rebeka, jetskiing).
                                                     24 done(antonio, kayaking).''') + "(a) Jane is a client who would like to choose the activity surfing and she has already done sailing. Write the additional clauses 25 to 28. (b) Using the variable List, the goal <code>choice(List, rowing)</code> returns List = petra, eliza. Write the result of <code>choice(List, sailing)</code>. (c) C is a client who would like to choose A if A is an activity and C has not already done A. Write this as a rule: <code>may_choose_activity(C, A) IF ...</code>",
  "Surfing is a new activity: it needs an activity fact as well as Jane's choice.",
  "<p><b>(a)</b> " + mks(["client(jane).", "activity(surfing).", "choice(jane, surfing).", "done(jane, sailing)."]) + " <b>(b)</b> " + mks(["List = frankie, erik, henry"], "a") + "</p><p><b>(c)</b> Four marks: " + mks(["client(C)", "activity(A)", "done(C, A) (with NOT)", "all operators and punctuation correct, no additional code"]) + "</p>" + qcode('''may_choose_activity(C, A)
   IF client(C) AND activity(A) AND NOT done(C, A).'''),
  "Missing one of the four facts. Check the description for each thing it names: a new client, a new activity, a choice and a done.") + peq(SRC("s26", "31", "Q11"), "3 + 1 + 4 marks", "Write",
  "A declarative language shows which home cinema devices customers already have and which devices they want." + qcode('''01 device(projector).        10 customer(petrov).     16 owns(projector, petrov).
02 device(large_tv).         11 customer(margaret).   17 owns(media_player, petrov).
03 device(medium_tv).        12 customer(steffan).    18 owns(projector, susan).
04 device(bluray_player).    13 customer(susan).      19 owns(projector, sammy).
05 device(amplifier).        14 customer(allan).      20 owns(media_player, allan).
06 device(media_player).     15 customer(sammy).      21 owns(bluray_player, steffan).
07 device(main_speakers).                              22 wants(main_speakers, margaret).
08 device(centre_speaker).                             23 wants(surround_speakers, susan).
09 device(surround_speakers).                          24 wants(medium_tv, steffan).''') + "(a) Betty is a customer who owns a large TV and wants a Blu-ray player. Write the additional facts 25 to 27. (b) Using the variable Owner, the goal <code>owns(media_player, Owner)</code> returns Owner = petrov, allan. Write the result of <code>owns(projector, Owner)</code>. (c) D may be available for A to buy if D is a device and A is a customer and A does not own that device. Write this as a rule: <code>may_buy_device(D, A) IF ...</code>",
  "Use the device names already given (large_tv, bluray_player). Betty is a new customer.",
  "<p><b>(a)</b> " + mks(["customer(betty).", "owns(large_tv, betty).", "wants(bluray_player, betty)."]) + " <b>(b)</b> " + mks(["Owner = petrov, susan, sammy (any order)"], "a") + "</p><p><b>(c)</b> Four marks: " + mks(["device(D)", "customer(A)", "owns(D, A) (with NOT)", "all conditions and punctuation correct (a comma for AND is accepted; \\+ is accepted for NOT)"]) + "</p>" + qcode('''may_buy_device(D, A)
   IF device(D) AND customer(A) AND NOT owns(D, A).'''),
  "Reversing the arguments to <code>owns(A, D)</code>. The knowledge base has the device first, so the rule must too.")

review = req("2 marks", "Distinguish", "Distinguish between a fact and a rule.", "One mark each.",
  "<p>" + mks(["A fact states something that is true, e.g. type(lion, wild).", "A rule states something is true if other conditions are true, using IF with AND and NOT."]) + "</p>", None) + req("3 marks", "Write", "Using the cats knowledge base, write the facts for Margay, a wild cat with medium hair and spots.", "Three facts: type, hair, spots.",
  "<p>" + mks(["type(margay, wild).", "hair(margay, medium).", "spots(margay, yes)."]) + "</p>", "Writing <code>spots(margay, spots)</code>. The second argument is yes or no.") + req("2 marks", "Write", "Using the cats knowledge base, write a goal to find all cats with short hair, and say what it returns.", "Use a variable.",
  "<p>" + mks(["hair(Cat, short)", "Cat = lion"]) + "</p>", None) + req("4 marks", "Write", "Using the cinema facts, write a rule: D is wanted by C if C is a customer and D is a device and C wants D and C does not own D. Name the rule needs_device(D, C).", "Three 'is a' style conditions and a NOT.",
  "<p>" + mks(["customer(C)", "device(D)", "wants(D, C)", "NOT owns(D, C), with correct operators"]) + "</p>" + qcode('''needs_device(D, C)
   IF customer(C) AND device(D) AND wants(D, C) AND NOT owns(D, C).'''), None) + req("3 marks", "Explain", "Explain the difference between imperative and declarative programming using the problem 'find all domestic cats'.", "How versus what.",
  "<p>" + mks(["Imperative: write the steps, such as a loop through every cat that tests the type and adds matches to a list.", "Declarative: state what is wanted with a goal, type(Pet, domestic), using the facts.", "The declarative system works out how to find the answers itself."]) + "</p>", None) + req("2 marks", "Describe", "Describe what the goal <code>owns(projector, Owner), customer(Owner)</code> does.", "Two conditions sharing the variable Owner.",
  "<p>" + mks(["It finds each Owner who owns a projector", "and keeps only those who are customers."]) + "</p>", None)

exam = exam20("Part 1 is the real 9618 declarative programming questions (Paper 3), which follow one pattern every time. Part 2 is a set of review questions for practice; they are not in exam format.", where, past, review)

tips = tips_html([
  ("Match the knowledge base.", "Use the same predicate names, argument order and constants. Copy a similar fact and change the values."),
  ("One fact per statement.", "Count the things the description says, and write a fact for each, including the 'is a' fact for anything new."),
  ("Capital means variable.", "betty is a constant; Betty is a variable. Never capitalise a constant."),
  ("Results come in order.", "List the answers in the order the facts appear, and check every fact with that predicate."),
  ("Rules: one condition per 'is a'.", "device(D) AND customer(A) AND the extra condition. NOT only on the one that must fail."),
  ("Reuse the variable to link.", "The same variable name in two conditions makes them apply to the same thing."),
  ("Do not add extra lines.", "A one-line rule or goal gets no mark for extra code."),
], [
  ("what declarative programming is", "The program states what result is wanted using facts and rules, and the system works out how to find it."),
  ("what a fact is", "A statement that is true, written as a predicate with arguments, such as owns(projector, petrov)."),
  ("what a rule is", "A statement that is true if its conditions are true, written head IF condition AND condition."),
  ("what a goal does", "It is a query: the system returns every set of values that makes it true."),
], [("Write", "Produce the clauses, goal or rule asked for, with the correct syntax."), ("State / Give the result", "List the values returned by the goal."), ("Describe", "Say what declarative means and how it differs from imperative.")]) + FC

js = AKJS + AK20JS + r'''
/* a small logic engine: facts are {p, args}; goals are {p, args, neg} */
const KBS = {
  cats: ["type(leopard, wild)", "type(lion, wild)", "type(cheetah, wild)", "type(savannah, hybrid)", "type(persian, domestic)", "hair(leopard, medium)", "hair(lion, short)", "hair(cheetah, medium)", "hair(savannah, medium)", "hair(persian, long)", "spots(leopard, yes)", "spots(lion, no)", "spots(cheetah, yes)", "spots(savannah, yes)", "spots(persian, no)"],
  school: ["teaches(alan, mathematics)", "teaches(ioana, geography)", "teaches(nina, history)", "teaches(alan, statistics)", "studies(ahmed, history)", "studies(freya, history)", "studies(kim, history)", "studies(freya, geography)", "studies(hua, mathematics)", "studies(hua, statistics)", "studies(hua, geography)", "tutors(alan, kim)", "tutors(alan, hua)", "tutors(alan, freya)", "tutors(nina, ahmed)"],
  cinema: ["device(projector)", "device(large_tv)", "device(medium_tv)", "device(bluray_player)", "device(amplifier)", "device(media_player)", "device(main_speakers)", "customer(petrov)", "customer(margaret)", "customer(steffan)", "customer(susan)", "customer(allan)", "customer(sammy)", "owns(projector, petrov)", "owns(media_player, petrov)", "owns(projector, susan)", "owns(projector, sammy)", "owns(media_player, allan)", "owns(bluray_player, steffan)", "wants(main_speakers, margaret)", "wants(medium_tv, steffan)"],
  hobbies: ["hobby(music)", "hobby(caving)", "hobby(climbing)", "hobby(camping)", "hobby(baking)", "person(toby)", "person(natasha)", "person(fatima)", "person(joseph)", "person(elijah)", "person(nina)", "enjoys(natasha, travelling)", "enjoys(toby, climbing)", "enjoys(nina, climbing)", "enjoys(elijah, camping)", "enjoys(fatima, baking)", "enjoys(joseph, camping)", "dislikes(toby, caving)"]
};
const isVar = (a) => /^[A-Z_]/.test(a);
function parseOne(s) {
  const m = s.trim().replace(/\.$/, "").match(/^(NOT\s+|\\\+\s*)?([a-z][A-Za-z0-9_]*)\(([^()]*)\)$/);
  if (!m) return null;
  return { neg: !!m[1], p: m[2], args: m[3].split(",").map((x) => x.trim()) };
}
function parseGoals(s) {
  s = s.replace(/\bAND\b/g, ",").trim().replace(/\.$/, ""); const parts = []; let d = 0, cur = "";
  for (const ch of s) { if (ch === "(") d++; if (ch === ")") d--; if (ch === "," && d === 0) { parts.push(cur); cur = ""; } else cur += ch; }
  if (cur.trim()) parts.push(cur);
  const g = parts.map(parseOne); return g.some((x) => !x) || !g.length ? null : g;
}
const kbOf = (name) => KBS[name].map(parseOne);
function solve(KB, goals, env) {
  if (!goals.length) return [env];
  const g = goals[0];
  if (g.neg) { const r = solve(KB, [{ ...g, neg: false }], env); return r.length ? [] : solve(KB, goals.slice(1), env); }
  let out = [];
  for (const f of KB) {
    if (f.p !== g.p || f.args.length !== g.args.length) continue;
    const e = { ...env }; let ok = true;
    for (let i = 0; i < g.args.length && ok; i++) { const a = g.args[i]; if (isVar(a)) { if (a in e) ok = e[a] === f.args[i]; else e[a] = f.args[i]; } else ok = a === f.args[i]; }
    if (ok) out = out.concat(solve(KB, goals.slice(1), e));
  }
  return out;
}
const varsOf = (goals) => { const v = []; goals.forEach((g) => !g.neg && g.args.forEach((a) => isVar(a) && !v.includes(a) && v.push(a))); return v; };
const uniq = (a) => a.filter((x, i) => a.indexOf(x) === i);

/* ---- animations ---- */
(function () {
  const facts = [["leopard", "medium"], ["lion", "short"], ["cheetah", "medium"], ["savannah", "medium"], ["persian", "long"]];
  const draw = (s) => {
    const k = Math.round(s.i); let o = SV.text(30, 28, "hair(Cat, medium)  ← the goal", "lbl bd", { style: "font-family:var(--mono);font-size:16px" });
    const found = [];
    facts.forEach((f, i) => {
      const y = 50 + i * 38, tried = k > i, ok = f[1] === "medium";
      if (tried && ok) found.push(f[0]);
      o += SV.rect(30, y, 300, 32, !tried ? "cell" : ok ? "cell-ok" : "cell-no", { rx: 6, ...op(tried || k === i ? 1 : 0.7) }) + SV.text(44, y + 21, "hair(" + f[0] + ", " + f[1] + ").", "lbl", { style: "font-family:var(--mono);font-size:15px" });
      if (tried) o += SV.text(310, y + 22, ok ? "✓" : "✗", "lbl bd " + (ok ? "t3" : "t2"), { "text-anchor": "end", style: "font-size:18px" });
    });
    o += SV.text(400, 70, "Cat =", "lbl bd", { style: "font-size:17px" }) + SV.text(460, 70, found.join(", "), "lbl bd t3", { style: "font-family:var(--mono);font-size:17px" });
    if (k >= 5) o += SV.text(400, 100, "all matches returned, in fact order", "sm");
    return o;
  };
  Lib.stepper($("#stA"), { w: 760, h: 260, label: "Matching a goal against the facts", base: { i: 0 }, draw, tween: 350, dwell: 2600, steps: [
    { cap: "The goal <code>hair(Cat, medium)</code> has a variable, <b>Cat</b>, and a constant, <b>medium</b>. The system tries each <code>hair</code> fact in turn.", s: { i: 0 } },
    { cap: "<code>hair(leopard, medium)</code> matches: medium = medium, so Cat = <b>leopard</b>.", s: { i: 1 } },
    { cap: "<code>hair(lion, short)</code>: short is not medium. No match.", s: { i: 2 } },
    { cap: "<code>hair(cheetah, medium)</code> matches: Cat = <b>cheetah</b>.", s: { i: 3 } },
    { cap: "<code>hair(savannah, medium)</code> matches: Cat = <b>savannah</b>.", s: { i: 4 } },
    { cap: "<code>hair(persian, long)</code> does not match. The goal returns <b>leopard, cheetah, savannah</b>.", s: { i: 5 } }] });
})();

(function () {
  const A = ["leopard", "cheetah", "savannah"], B = ["leopard", "lion", "cheetah"];
  const draw = (s) => {
    const k = Math.round(s.i); let o = SV.text(30, 26, "spots(WildSpotty, yes), type(WildSpotty, wild)", "lbl bd", { style: "font-family:var(--mono);font-size:15px" });
    const col = (x, title, items, hl, v) => { let t = SV.text(x, 70, title, "sm", op(v)); items.forEach((it, i) => { t += SV.rect(x, 80 + i * 36, 180, 30, hl.includes(it) ? "cell-ok" : "cell", { rx: 6, ...op(v) }) + SV.text(x + 12, 101 + i * 36, it, "lbl", { style: "font-family:var(--mono);font-size:15px", ...op(v) }); }); return t; };
    o += col(30, "spots(X, yes) gives", A, k >= 3 ? ["leopard", "cheetah"] : [], k >= 1 ? 1 : 0);
    o += col(280, "type(X, wild) gives", B, k >= 3 ? ["leopard", "cheetah"] : [], k >= 2 ? 1 : 0);
    if (k >= 3) o += SV.text(520, 100, "X must satisfy both:", "lbl bd") + SV.text(520, 130, "leopard", "lbl bd t3", { style: "font-family:var(--mono);font-size:18px" }) + SV.text(520, 160, "cheetah", "lbl bd t3", { style: "font-family:var(--mono);font-size:18px" });
    return o;
  };
  Lib.stepper($("#stB"), { w: 760, h: 200, label: "Two conditions sharing a variable", base: { i: 0 }, draw, tween: 400, dwell: 3200, steps: [
    { cap: "Find the wild cats with spots. The variable <b>WildSpotty</b> appears in both conditions, so it must be the <b>same cat</b> in both.", s: { i: 0 } },
    { cap: "The first condition, <code>spots(WildSpotty, yes)</code>, is satisfied by leopard, cheetah and savannah.", s: { i: 1 } },
    { cap: "The second, <code>type(WildSpotty, wild)</code>, is satisfied by leopard, lion and cheetah.", s: { i: 2 } },
    { cap: "Only values that satisfy <b>both</b> are answers: <b>leopard, cheetah</b>. The comma means AND.", s: { i: 3 } }] });
})();

(function () {
  const rows = [
    ["device(D)", "D = projector", "found: device(projector)", 1],
    ["customer(A)", "A = betty", "found: customer(betty)", 1],
    ["NOT owns(D, A)", "owns(projector, betty)?", "not found, so NOT succeeds", 1],
  ];
  const rows2 = [["device(D)", "D = projector", "found", 1], ["customer(A)", "A = petrov", "found", 1], ["NOT owns(D, A)", "owns(projector, petrov)?", "found, so NOT fails", 0]];
  const draw = (s) => {
    const k = Math.round(s.i), R = k >= 4 ? rows2 : rows, n = k >= 4 ? k - 4 : k; let o = SV.text(30, 26, "may_buy_device(D, A) IF device(D), customer(A), NOT owns(D, A).", "lbl bd", { style: "font-family:var(--mono);font-size:14px" });
    o += SV.text(30, 52, k >= 4 ? "Try A = petrov (who owns a projector)" : "Try D = projector, A = betty", "sm");
    R.forEach((r, i) => { if (n <= i) return; const ok = r[3] === 1; o += SV.rect(30, 66 + i * 42, 700, 34, ok ? "cell-ok" : "cell-no", { rx: 6 }) + SV.text(44, 88 + i * 42, r[0], "lbl bd", { style: "font-family:var(--mono);font-size:14px" }) + SV.text(250, 88 + i * 42, r[1], "lbl", { style: "font-family:var(--mono);font-size:14px" }) + SV.text(520, 88 + i * 42, r[2], "lbl"); });
    if (n >= 3) o += SV.text(30, 220, k >= 4 ? "A condition failed: the rule is FALSE for this pair" : "All three conditions succeed: the rule is TRUE, so Betty may buy a projector", "lbl bd " + (k >= 4 ? "t2" : "t3"));
    return o;
  };
  Lib.stepper($("#stC"), { w: 760, h: 240, label: "Evaluating a rule with NOT", base: { i: 0 }, draw, tween: 300, dwell: 3000, steps: [
    { cap: "A rule is true when <b>every condition</b> is true. Betty is a new customer who owns nothing. Try D = projector and A = betty.", s: { i: 0 } },
    { cap: "<code>device(D)</code>: the fact <code>device(projector)</code> exists, so this is true.", s: { i: 1 } },
    { cap: "<code>customer(A)</code>: <code>customer(betty)</code> exists, so this is true.", s: { i: 2 } },
    { cap: "<code>NOT owns(D, A)</code>: the system looks for <code>owns(projector, betty)</code>. It is <b>not found</b>, so NOT succeeds. All true: Betty may buy a projector.", s: { i: 3 } },
    { cap: "Now try A = petrov, who owns a projector. The first two conditions are true again.", s: { i: 6 } },
    { cap: "<code>owns(projector, petrov)</code> <b>is</b> found, so <code>NOT owns(...)</code> fails and the rule is <b>false</b> for this pair: Petrov already owns one.", s: { i: 7 } }] });
})();

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); let o = "";
    o += SV.rect(20, 20, 350, 200, "f1", { rx: 10, ...op(0.2) }) + SV.text(195, 44, "Imperative: how", "lbl bd", { "text-anchor": "middle" });
    o += SV.rect(390, 20, 350, 200, "f2", { rx: 10, ...op(0.2) }) + SV.text(565, 44, "Declarative: what", "lbl bd", { "text-anchor": "middle" });
    const imp = ["pets = []", "for cat in cats:", "    if cat.type == \"domestic\":", "        pets.append(cat)"];
    imp.forEach((l, i) => { if (k >= 1) o += SV.text(36, 80 + i * 26, l, "lbl", { style: "font-family:var(--mono);font-size:14px;white-space:pre" }); });
    if (k >= 2) o += SV.text(565, 100, "type(Pet, domestic).", "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:18px" });
    if (k >= 3) o += SV.text(36, 200, "You write the steps", "sm") + SV.text(410, 200, "You state the goal; the system searches the facts", "sm");
    return o;
  };
  Lib.stepper($("#stD"), { w: 760, h: 240, label: "Imperative against declarative", base: { i: 0 }, draw, tween: 300, dwell: 3000, steps: [
    { cap: "The problem: find all the domestic cats.", s: { i: 0 } },
    { cap: "<b>Imperative</b>: write the steps. Make a list, loop through every cat, test the type, add it if it matches.", s: { i: 1 } },
    { cap: "<b>Declarative</b>: state what you want as a goal. <code>type(Pet, domestic)</code> says 'find every Pet that is a domestic type'.", s: { i: 2 } },
    { cap: "The programmer states <i>what</i>; the system works out <i>how</i> by searching the facts and rules.", s: { i: 3 } }] });
})();

/* ---- Lab 1 ---- */
(function () {
  let kb = "cats";
  const names = [["cats", "Cats"], ["school", "School"], ["cinema", "Home cinema"], ["hobbies", "Hobbies"]];
  const ex = { cats: ["hair(Cat, medium)", "type(Pet, domestic)", "spots(WildSpotty, yes), type(WildSpotty, wild)", "hair(lion, short)", "hair(Cat, purple)"], school: ["studies(Student, geography)", "teaches(alan, Subject)", "teaches(R, S), studies(X, S), tutors(R, X)"], cinema: ["owns(projector, Owner)", "owns(media_player, Owner)", "customer(C), NOT owns(projector, C)"], hobbies: ["enjoys(P, camping)", "enjoys(P, climbing), person(P)", "person(P), NOT enjoys(P, climbing)"] };
  const paint = () => {
    $$("#kB button").forEach((b, i) => b.classList.toggle("pri", names[i][0] === kb));
    $("#kF").innerHTML = '<div class="code"><pre class="cp">' + KBS[kb].map((f) => `<span class="ln">${f}.</span>`).join("") + "</pre></div>";
    $("#kE").innerHTML = ex[kb].map((e, i) => `<button class="b" data-i="${i}">${e}</button>`).join("");
    $$("#kE button").forEach((b) => (b.onclick = () => { $("#kQ").value = ex[kb][+b.dataset.i]; run(); }));
    $("#kQ").value = ex[kb][0]; run();
  };
  const run = () => {
    const g = parseGoals($("#kQ").value), out = $("#kV");
    if (!g) { out.textContent = "That is not a valid goal. Use the form predicate(argument, argument), with commas between conditions."; return; }
    const bad = g.find((x) => x.neg && x.args.some((a) => isVar(a)) && !g.some((y) => !y.neg && y.args.some((a) => x.args.includes(a))));
    if (bad) { out.textContent = "Put the condition that gives the variable a value before the NOT condition."; return; }
    const sol = solve(kbOf(kb), g, {}), vs = varsOf(g);
    if (!sol.length) { out.textContent = "false: no values make the goal true."; return; }
    if (!vs.length) { out.textContent = "true"; return; }
    out.innerHTML = vs.map((v) => "<b>" + v + "</b> = " + uniq(sol.map((e) => e[v])).join(", ")).join("<br>");
  };
  $("#kB").innerHTML = names.map((n, i) => `<button class="b" data-i="${i}">${n[1]}</button>`).join("");
  $$("#kB button").forEach((b) => (b.onclick = () => { kb = names[+b.dataset.i][0]; paint(); }));
  $("#kR").onclick = run; $("#kQ").addEventListener("keydown", (e) => { if (e.key === "Enter") run(); });
  paint();
})();

/* ---- Lab 2 ---- */
(function () {
  const rules = [
    ["cats", "wild_spotty(X)", "spots(X, yes), type(X, wild)"],
    ["school", "student_of_own_tutor(X)", "teaches(R, S), studies(X, S), tutors(R, X)"],
    ["cinema", "may_buy_device(D, A)", "device(D), customer(A), NOT owns(D, A)"],
    ["hobbies", "might_enjoy(N, H)", "person(N), hobby(H), NOT dislikes(N, H)"]
  ];
  let cur = 2;
  const paint = () => {
    $$("#rB button").forEach((b, i) => b.classList.toggle("pri", i === cur));
    $("#rH").textContent = rules[cur][1]; $("#rQ").value = rules[cur][2]; run();
  };
  const run = () => {
    const g = parseGoals($("#rQ").value), o = $("#rO"), v = $("#rV");
    if (!g) { o.innerHTML = ""; v.textContent = "Check the conditions: predicate(arguments), separated by commas."; return; }
    const vars = rules[cur][1].match(/\(([^)]*)\)/)[1].split(",").map((s) => s.trim());
    const sol = solve(kbOf(rules[cur][0]), g, {}), rows = uniq(sol.map((e) => vars.map((x) => e[x]).join("|"))).map((r) => r.split("|"));
    o.innerHTML = '<div class="tw"><table class="t mono"><tr>' + vars.map((x) => `<th>${x}</th>`).join("") + "</tr>" + rows.slice(0, 12).map((r) => "<tr>" + r.map((c) => `<td>${c}</td>`).join("") + "</tr>").join("") + "</table></div>";
    v.textContent = rows.length ? `The rule is true for ${rows.length} combination${rows.length === 1 ? "" : "s"}${rows.length > 12 ? " (first 12 shown)" : ""}.` : "The rule is not true for any combination.";
  };
  $("#rB").innerHTML = rules.map((r, i) => `<button class="b" data-i="${i}">${r[0]}</button>`).join("");
  $$("#rB button").forEach((b) => (b.onclick = () => { cur = +b.dataset.i; paint(); }));
  $("#rR").onclick = run; paint();
})();

btnTable("eB", "eO", [
  ["Capital letter on a constant", "customer(Betty).", "Betty is read as a variable, so the fact means 'every thing is a customer'", "customer(betty)."],
  ["Missing 'is a' fact", "owns(large_tv, betty). (and nothing else)", "Betty is never declared a customer, so a rule using customer(A) cannot find her", "customer(betty). owns(large_tv, betty)."],
  ["Wrong argument order", "owns(betty, large_tv).", "Does not match the other facts, which have the device first", "owns(large_tv, betty)."],
  ["Unlinked variables", "teaches(R, S), studies(X, T), tutors(R, X)", "S and T are different variables, so the subject is not linked", "teaches(R, S), studies(X, S), tutors(R, X)"],
  ["NOT first", "NOT owns(D, A), device(D), customer(A)", "D and A have no values yet when NOT is tested", "device(D), customer(A), NOT owns(D, A)"],
  ["Missing a condition", "may_buy_device(D, A) IF device(D) AND NOT owns(D, A)", "A is never said to be a customer", "add customer(A)"],
  ["Missing full stop or extra text", "type(caracal, wild)", "Each clause ends with a full stop", "type(caracal, wild)."]
], ["Mistake", "Example", "What goes wrong", "Fix"]);
''' + CLASSIFY("cl1", "Is each clause a fact, a rule or a goal?", ["Fact", "Rule", "Goal"],
  [("type(caracal, wild).", 0), ("hair(Cat, long)", 2), ("may_buy_device(D, A) IF device(D) AND customer(A) AND NOT owns(D, A).", 1), ("customer(betty).", 0), ("owns(projector, Owner)", 2), ("might_enjoy(N, H) IF person(N), hobby(H), NOT dislikes(N, H).", 1), ("studies(sam, history).", 0), ("spots(X, yes), type(X, wild)", 2)],
  "Facts end with a full stop and have no variables. Rules have IF. Goals have variables and ask a question.") + CLASSIFY("cl2", "Is each name a constant or a variable?", ["Constant", "Variable"],
  [("leopard", 0), ("Cat", 1), ("domestic", 0), ("WildSpotty", 1), ("Owner", 1), ("projector", 0), ("D", 1), ("yes", 0)],
  "Lower-case first letter: constant. Capital first letter: variable.") + ORDER(
  "Put the steps for answering a goal in order.",
  ["Take the first condition of the goal", "Look through the facts for ones that match", "Fill in the variables from each match", "Test the next condition using those values", "Return every set of values that satisfies all the conditions"],
  "Match, fill, test the next, collect all.") + MATCH([
  ["Fact", "A statement that is true, with a full stop"], ["Rule", "True if its conditions are true: IF with AND and NOT"], ["Goal", "A query the system tries to satisfy"], ["Variable", "A name starting with a capital that the system fills in"], ["Knowledge base", "All the facts and rules together"]]) + CALC([
  {"q": "Cats knowledge base: how many cats does hair(Cat, medium) return?", "a": 3, "unit": "", "tol": 0.01, "hint": "leopard, cheetah, savannah.", "sol": "<b>3</b>."},
  {"q": "Cats: how many cats does spots(Cat, yes) return?", "a": 3, "unit": "", "tol": 0.01, "hint": "leopard, cheetah, savannah.", "sol": "<b>3</b>."},
  {"q": "Cats: how many does spots(Cat, yes), type(Cat, wild) return?", "a": 2, "unit": "", "tol": 0.01, "hint": "Both conditions: leopard and cheetah.", "sol": "<b>2</b>."},
  {"q": "Cinema: how many customers does owns(projector, Owner) return?", "a": 3, "unit": "", "tol": 0.01, "hint": "petrov, susan, sammy.", "sol": "<b>3</b>."},
  {"q": "School: how many students does studies(Student, history) return?", "a": 3, "unit": "", "tol": 0.01, "hint": "ahmed, freya, kim.", "sol": "<b>3</b>."},
  {"q": "A knowledge base has 5 devices and 4 customers, and one owns fact. How many (device, customer) pairs satisfy device(D), customer(A), NOT owns(D, A)?", "a": 19, "unit": "", "tol": 0.01, "hint": "5 × 4 = 20 pairs, minus the one that is owned.", "sol": "<b>19</b>."}]) + MCQ([
  ("What does a declarative program state?", ["The steps to follow", "What result is wanted, using facts and rules", "The machine code", "The loop to repeat"], 1, "Declarative says what, not how."),
  ("Which is a variable?", ["betty", "projector", "Owner", "yes"], 2, "A capital first letter makes it a variable."),
  ("Which rule is correct for: D may be bought by A if D is a device, A is a customer and A does not own D?", ["may_buy(D, A) IF device(D) AND customer(A) AND owns(D, A)", "may_buy(D, A) IF device(D) AND customer(A) AND NOT owns(D, A)", "may_buy(D, A) IF NOT owns(D, A)", "may_buy(D, A) IF device(D) OR customer(A)"], 1, "Two 'is a' conditions and a NOT."),
  ("A new customer, Zoe, owns a tablet. Which facts are needed?", ["owns(tablet, zoe).", "customer(zoe). owns(tablet, zoe).", "customer(Zoe). owns(tablet, Zoe).", "zoe(customer). owns(zoe, tablet)."], 1, "Declare the customer, then what she owns, in the knowledge base's order."),
  ("What does NOT owns(D, A) mean in a rule?", ["A owns D", "The fact owns(D, A) cannot be found", "D is a device", "A is a customer"], 1, "NOT succeeds when the fact is not found."),
  ("Which language type is Prolog?", ["Low-level", "Imperative", "Object-oriented", "Declarative (logic)"], 3, "Facts, rules and goals.")], "qz1") + CARDS([
  ("Declarative programming", "States what is wanted using facts and rules; the system works out how."), ("Fact", "A true statement: type(lion, wild)."), ("Rule", "True if conditions are true: head IF cond AND cond."), ("Goal", "A query: hair(Cat, medium)."),
  ("Variable", "Capital first letter. Filled in by the system."), ("Constant", "Lower-case first letter. A specific value."), ("AND", "A comma between conditions: all must be true."), ("NOT", "Succeeds if the fact is not found.")])

build("ac2014", "ac-20-1-4-declarative-programming", "Declarative Programming: Facts, Rules and Goals", EYA("20.1.4"),
  "Facts, rules, goals and variables in a logic language; adding facts from a description, giving the result of a goal, and writing rules with AND and NOT; animations, a goal engine you can query, and every declarative question from the 2021 to 2026 Paper 3 papers.",
  dict(sub=CBK("Chapter 20 · Further programming, section 20.1 Programming paradigms"), **tabs(learn, watch, explore, practise, real, exam, tips)), js)
