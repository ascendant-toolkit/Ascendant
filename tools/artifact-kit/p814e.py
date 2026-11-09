"""8.1.4 String handling."""
from p814k import *

FN_PS = ['Word ← "Computer"', "OUTPUT LENGTH(Word)", "OUTPUT UCASE(Word)", "OUTPUT SUBSTRING(Word, 4, 3)", 'OUTPUT Word & "s"']
FN_PY = ['word = "Computer"', "print(len(word))", "print(word.upper())", "print(word[3:6])", 'print(word + "s")']
CT_PS = ['Word ← "elephant"', "Count ← 0", "FOR Index ← 1 TO LENGTH(Word)", "    Letter ← SUBSTRING(Word, Index, 1)", '    IF Letter = "e"', "      THEN", "        Count ← Count + 1", "    ENDIF", "NEXT Index", "OUTPUT Count"]
CT_PY = ['word = "elephant"', "count = 0", "for index in range(1, len(word) + 1):", "    letter = word[index - 1]", '    if letter == "e":', "        count = count + 1", "print(count)"]
RV_PS = ['Word ← "STAR"', 'Reverse ← ""', "FOR Index ← 1 TO LENGTH(Word)", "    Reverse ← SUBSTRING(Word, Index, 1) & Reverse", "NEXT Index", "OUTPUT Reverse"]
RV_PY = ['word = "STAR"', 'reverse = ""', "for index in range(1, len(word) + 1):", "    reverse = word[index - 1] + reverse", "print(reverse)"]


def anim_fn():
    w = "Computer"; ch = list(w); r = R(["Word"])
    r.v["Word"] = w; r.f("<b>Word ← \"Computer\"</b>. A string is a row of characters. In pseudocode the first character is <b>position 1</b>.", [0], [0], hl=["Word"], cells=ch)
    r.out.append("8"); r.f("<b>LENGTH(Word)</b> counts every character: <b>8</b>.", [1], [1], cells=ch, cc={i: "cur" for i in range(8)})
    r.out.append("COMPUTER"); r.f("<b>UCASE(Word)</b> gives the whole string in capitals. Word itself is not changed.", [2], [2], cells=ch, cc={i: "cur" for i in range(8)})
    r.out.append("put"); r.f("<b>SUBSTRING(Word, 4, 3)</b>: start at position <b>4</b> and take <b>3</b> characters: p, u, t.", [3], [3], cells=ch, cc={3: "cur", 4: "cur", 5: "cur"})
    r.out.append("Computers"); r.f("<b>&amp;</b> joins two strings together (<span class=\"kw\">concatenation</span>): \"Computer\" & \"s\".", [4], [4], cells=ch + ["s"], cc={8: "ok"})
    return r.js()


def anim_ct():
    w = "elephant"; ch = list(w); r = R(["Index", "Letter", "Count"])
    r.v["Count"] = 0; r.f("<b>Count ← 0</b>. The loop will look at each letter from position 1 to LENGTH(Word) = 8.", [0, 1], [0, 1], hl=["Count"], cells=ch)
    c = 0; seen = {}
    for i, l in enumerate(ch):
        r.v["Index"] = i + 1; r.v["Letter"] = l
        r.f(f"Index {i + 1}. <b>Letter ← SUBSTRING(Word, {i + 1}, 1)</b> takes one character: \"{l}\".", [2, 3], [2, 3], hl=["Index", "Letter"], cells=ch, cc={**seen, i: "cur"})
        hit = l == "e"
        r.f(f"Is \"{l}\" = \"e\"?", [4], [4], cells=ch, cc={**seen, i: "cur"}, cond=(f'"{l}" = "e"', hit))
        if hit:
            c += 1; r.v["Count"] = c
            r.f(f"TRUE, so <b>Count ← Count + 1</b> = <b>{c}</b>.", [6], [5], hl=["Count"], cells=ch, cc={**seen, i: "ok"}, cond=(f'"{l}" = "e"', True))
            seen[i] = "ok"
        else:
            pass
    r.out.append(str(c)); r.f(f"The loop ends. <b>OUTPUT Count</b>: the letter \"e\" appears <b>{c}</b> times.", [9], [6], hl=["Count"], cells=ch, cc={k: v for k, v in seen.items() if v == "ok"})
    return r.js()


def anim_rv():
    w = "STAR"; ch = list(w); r = R(["Index", "Reverse"])
    r.v["Reverse"] = ""; r.f("<b>Reverse ← \"\"</b>: an empty string to build the answer in.", [0, 1], [0, 1], hl=["Reverse"], cells=ch)
    rev = ""
    for i, l in enumerate(ch):
        r.v["Index"] = i + 1; rev = l + rev; r.v["Reverse"] = rev
        r.f(f"Index {i + 1}: take \"{l}\" and join it on the <b>front</b> of Reverse. Reverse is now <b>\"{rev}\"</b>.", [2, 3], [2, 3], hl=["Index", "Reverse"], cells=ch, cc={i: "cur"})
    r.out.append(rev); r.f(f"<b>OUTPUT Reverse</b>: {rev}. Each new letter was added in front of the last one.", [5], [4], hl=["Reverse"], cells=ch)
    return r.js()


learn = '''
  <h2>8.1.4 String handling</h2>
  <p>A <span class="kw">string</span> is text: a row of <span class="kw">characters</span> such as letters, digits, spaces and symbols. <span class="kw">String handling</span> means using built-in operations to measure, cut up, change and join strings. In Cambridge pseudocode the <b>first character is position 1</b>.</p>
  <div id="cdStr" class="code"></div>

  <h3>The four operations</h3>
  <div class="tw"><table class="t">
    <tr><th>Operation</th><th>Pseudocode</th><th>Result for "Computer"</th><th>Python</th></tr>
    <tr><td>Length</td><td>LENGTH(Word)</td><td>8</td><td>len(word)</td></tr>
    <tr><td>Substring (start, how many)</td><td>SUBSTRING(Word, 4, 3)</td><td>"put"</td><td>word[3:6]</td></tr>
    <tr><td>Upper case</td><td>UCASE(Word)</td><td>"COMPUTER"</td><td>word.upper()</td></tr>
    <tr><td>Lower case</td><td>LCASE(Word)</td><td>"computer"</td><td>word.lower()</td></tr>
    <tr><td>Join (concatenate)</td><td>Word &amp; "s"</td><td>"Computers"</td><td>word + "s"</td></tr>
  </table></div>
  <div class="warn"><b class="h">Positions start at 1 in pseudocode, 0 in Python</b>SUBSTRING(Word, 1, 1) is the <b>first</b> letter. In Python the first letter is <code>word[0]</code>. The <b>last</b> letter is at position <code>LENGTH(Word)</code>. Python slices <code>word[start:end]</code> stop <b>before</b> the end, so SUBSTRING(Word, 4, 3) is <code>word[3:6]</code>.</div>
  <ul>
    <li><b>Spaces count as characters.</b> LENGTH("Good day") is 8.</li>
    <li><b>The original string is not changed.</b> UCASE(Word) gives a new value. To keep it, store it: <code>Big ← UCASE(Word)</code>.</li>
    <li><b>Strings are compared exactly.</b> "a" and "A" are <b>different</b>. Convert both with UCASE or LCASE before comparing if case should not matter.</li>
  </ul>

  <h3>Looking at every character</h3>
  <p>Put SUBSTRING inside a <b>FOR loop</b> that runs from 1 to LENGTH(Word). Each repeat takes one character (<code>SUBSTRING(Word, Index, 1)</code>). You can then <b>count</b> letters with an IF, or <b>build</b> a new string.</p>
  <div id="cdLoop" class="code"></div>

  <h3>Building a string</h3>
  <p>Start with an empty string <code>""</code> and add to it with <b>&amp;</b>. Joining each new character on the <b>front</b> reverses the string.</p>
  <div id="cdBuild" class="code"></div>
'''

watch = '''  <h2>1 · LENGTH, UCASE, SUBSTRING and joining</h2><div id="aF"></div>
  <h2>2 · Counting a letter in a word</h2><div id="aC"></div>
  <h2>3 · Reversing a string</h2><div id="aR"></div>
'''

explore = '''  <h2>Lab 1 · String toolbox</h2>
  <p>Type a word or phrase. Choose where SUBSTRING starts and how many characters it takes. The characters it takes are highlighted.</p>
  <div class="card"><input class="ipin" id="ti" type="text" value="Computer Science" maxlength="20" aria-label="Text" spellcheck="false"><div id="s1"></div><div id="s2"></div><div id="tcells" class="mac" aria-label="Characters"></div><div class="tw"><table class="t mono" id="tt"></table></div></div>

  <h2>Lab 2 · Build a username</h2>
  <p>Programs often join pieces of strings together. Type a first name and a surname.</p>
  <div class="card"><div class="row"><input class="ipin" id="un1" type="text" value="Maria" maxlength="14" aria-label="First name" spellcheck="false" style="width:200px"><input class="ipin" id="un2" type="text" value="Gonzalez" maxlength="14" aria-label="Surname" spellcheck="false" style="width:200px"></div><div id="ucode"></div><div class="tw"><table class="t mono" id="ut"></table></div></div>

  <h2>Lab 3 · Letter counter</h2>
  <p>Type a word and one letter to count. This is the loop from the animation, running on your word.</p>
  <div class="card"><div class="row"><input class="ipin" id="lw" type="text" value="banana" maxlength="16" aria-label="Word" spellcheck="false" style="width:240px"><input class="ipin" id="ll" type="text" value="a" maxlength="1" aria-label="Letter" spellcheck="false" style="width:70px"></div><div id="lcells" class="mac"></div><div class="verdict" id="lv" aria-live="polite"></div></div>
'''

practise = '''  <h2>1 · Match the expression to its result</h2>
  <div id="m1" class="card"></div>
  <h2>2 · Reverse a word, in order</h2>
  <div id="o1" class="card"></div>
  <h2>3 · What does it give?</h2>
  <p class="note">Type the answer. For text results, type the letters without quote marks.</p>
  <div id="c1"></div>
  <h2>4 · Multiple choice</h2>
  <div id="qz1"></div>
'''

real = (rw("A username generator", "A school system makes each username from the first letter of a first name and the surname, in lower case.", "SUBSTRING takes the letter, &amp; joins the pieces, LCASE makes it lower case.")
        + rw("Password rules", "A website refuses a password shorter than 8 characters.", "LENGTH gives the number of characters; compare it with 8.")
        + rw("A search box", "Searching for \"phone\" should also find \"Phone\". The program changes both to the same case before comparing.", "UCASE or LCASE removes the effect of capital letters in comparisons.")
        + rw("A word counter", "A text editor counts the spaces in a document to estimate how many words it has.", "a loop with SUBSTRING and a counter, as in the letter-counting program.")
        )

ex = [
    eq(1, "State", 3, "State the value returned by each of these. (a) LENGTH(\"Good day\") (b) SUBSTRING(\"Computer\", 4, 3) (c) UCASE(\"cat\") &amp; \"s\"", "Spaces count. Positions start at 1.",
       mk(1, "(a) 8") + " " + mk(2, "(b) \"put\"") + " " + mk(3, "(c) \"CATs\""),
       "Writing 7 for (a). The space is a character. For (b) starting at position 3 or counting from 0."),
    eq(2, "Write", 3, "Write pseudocode to input a word, then output the word in upper case and the number of characters in it.", "Input, then two functions in OUTPUT.",
       mk(1, "INPUT Word (into a suitable variable)") + " " + mk(2, "OUTPUT UCASE(Word)") + " " + mk(3, "OUTPUT LENGTH(Word)")
       + ac(["INPUT Word", "OUTPUT UCASE(Word)", "OUTPUT LENGTH(Word)"]),
       "Writing LENGTH Word or UCASE Word without brackets. The functions need (Word)."),
    eq(3, "Write", 4, "Write pseudocode to input a word and output its first letter and its last letter.", "The last position is LENGTH(Word).",
       mk(1, "INPUT Word") + " " + mk(2, "SUBSTRING(Word, 1, 1) for the first letter") + " " + mk(3, "SUBSTRING(Word, LENGTH(Word), 1) for the last letter") + " " + mk(4, "both letters output")
       + ac(["INPUT Word", "OUTPUT SUBSTRING(Word, 1, 1)", "OUTPUT SUBSTRING(Word, LENGTH(Word), 1)"]),
       "Using SUBSTRING(Word, 0, 1). Positions start at <b>1</b>."),
    eq(4, "Write", 5, "Write pseudocode to input a name and output it with a capital first letter and all other letters in lower case.", "Two pieces: the first letter and the rest.",
       mk(1, "INPUT Name") + " " + mk(2, "First ← UCASE(SUBSTRING(Name, 1, 1))") + " " + mk(3, "Rest ← LCASE(SUBSTRING(Name, 2, LENGTH(Name) - 1))") + " " + mk(4, "joined with &amp;") + " " + mk(5, "OUTPUT of the joined result")
       + ac(["INPUT Name", "First ← UCASE(SUBSTRING(Name, 1, 1))", "Rest ← LCASE(SUBSTRING(Name, 2, LENGTH(Name) - 1))", "OUTPUT First & Rest"]),
       "Taking LENGTH(Name) characters for the rest. That reads past the end. The rest has <b>one fewer</b>."),
    eq(5, "Write", 6, "Write pseudocode to input a word and a letter, then count how many times the letter appears in the word, and output the count.", "A loop through every position, a test, and a counter.",
       mk(1, "INPUT Word and INPUT Letter") + " " + mk(2, "Count ← 0 before the loop") + " " + mk(3, "FOR Index ← 1 TO LENGTH(Word)") + " " + mk(4, "IF SUBSTRING(Word, Index, 1) = Letter") + " " + mk(5, "THEN Count ← Count + 1 ... ENDIF") + " " + mk(6, "OUTPUT Count after the loop")
       + ac(["INPUT Word", "INPUT Letter", "Count ← 0", "FOR Index ← 1 TO LENGTH(Word)", "    IF SUBSTRING(Word, Index, 1) = Letter", "      THEN", "        Count ← Count + 1", "    ENDIF", "NEXT Index", "OUTPUT Count"]),
       "Taking the whole word, SUBSTRING(Word, Index, LENGTH(Word)), instead of <b>1</b> character."),
    eq(6, "Write", 4, "A password must have at least 8 characters. Write pseudocode that keeps asking for a password until it is long enough, then outputs \"Accepted\".", "At least once, so REPEAT ... UNTIL.",
       mk(1, "REPEAT") + " " + mk(2, "INPUT Password inside the loop") + " " + mk(3, "UNTIL LENGTH(Password) >= 8") + " " + mk(4, "OUTPUT \"Accepted\" after the loop")
       + ac(["REPEAT", "    INPUT Password", "UNTIL LENGTH(Password) >= 8", 'OUTPUT "Accepted"']),
       "Writing UNTIL LENGTH(Password) &lt; 8. UNTIL stops when the condition is TRUE."),
    eq(7, "Complete", 3, "The code is run with Word = \"CAT\". Complete the table to show Reverse after each repeat and state the output.", "Each new letter goes on the front.",
       mk(1, "Index 1: Reverse = \"C\"; index 2: \"AC\"") + " " + mk(2, "Index 3: \"TAC\"") + " " + mk(3, "OUTPUT TAC"),
       "Adding each letter to the <b>end</b>. This code joins it on the front, which reverses the word.",
       pre=qc(['Reverse ← ""', "FOR Index ← 1 TO LENGTH(Word)", "    Reverse ← SUBSTRING(Word, Index, 1) & Reverse", "NEXT Index", "OUTPUT Reverse"])),
    eq(8, "Write", 5, "A product code has 6 characters. Write pseudocode to input a code and output \"Valid\" only if it has exactly 6 characters and its first character is \"X\". Otherwise output \"Invalid\".", "Two tests, one inside the other.",
       mk(1, "INPUT Code") + " " + mk(2, "IF LENGTH(Code) = 6") + " " + mk(3, "nested IF SUBSTRING(Code, 1, 1) = \"X\"") + " " + mk(4, "OUTPUT \"Valid\" only inside both") + " " + mk(5, "OUTPUT \"Invalid\" in both ELSE parts")
       + ac(["INPUT Code", "IF LENGTH(Code) = 6", "  THEN", '    IF SUBSTRING(Code, 1, 1) = "X"', "      THEN", '        OUTPUT "Valid"', "      ELSE", '        OUTPUT "Invalid"', "    ENDIF", "  ELSE", '    OUTPUT "Invalid"', "ENDIF"]),
       "Comparing with the lower-case \"x\". A string comparison is exact."),
    eq(9, "Write", 6, "Write pseudocode to input a sentence, count the number of spaces in it, and output how many words it contains (the number of spaces plus 1).", "Combine: a loop, SUBSTRING, an IF and a counter.",
       mk(1, "INPUT Sentence") + " " + mk(2, "Spaces ← 0 before the loop") + " " + mk(3, "FOR Index ← 1 TO LENGTH(Sentence)") + " " + mk(4, "IF SUBSTRING(Sentence, Index, 1) = \" \" THEN Spaces ← Spaces + 1") + " " + mk(5, "Words ← Spaces + 1 after the loop") + " " + mk(6, "OUTPUT Words")
       + ac(["INPUT Sentence", "Spaces ← 0", "FOR Index ← 1 TO LENGTH(Sentence)", '    IF SUBSTRING(Sentence, Index, 1) = " "', "      THEN", "        Spaces ← Spaces + 1", "    ENDIF", "NEXT Index", "Words ← Spaces + 1", "OUTPUT Words"]),
       "Outputting Spaces, which is one fewer than the number of words."),
]
exam = "".join(ex)

tipshtml = tips([
    "<b>Positions start at 1</b> in pseudocode. The last character is at LENGTH(Word).",
    "<b>SUBSTRING(Word, start, how many)</b>: say where to start, then how many characters.",
    "<b>Spaces are characters</b> and count in LENGTH.",
    "<b>Use &amp; to join strings.</b> Start from \"\" when you build a string in a loop.",
    "<b>Strings compare exactly.</b> \"a\" is not \"A\". Use UCASE or LCASE first if case should not matter.",
    "<b>To check every letter, loop FOR Index ← 1 TO LENGTH(Word)</b> and take SUBSTRING(Word, Index, 1).",
])

page("8.1.4 · String handling", "String Handling", "Measuring, slicing, changing and joining text: LENGTH, SUBSTRING, UCASE, LCASE and concatenation.",
     "A <span class=\"kw\">string</span> is a row of characters. Built-in functions can <b>measure</b> it (LENGTH), <b>cut</b> pieces from it (SUBSTRING), <b>change its case</b> (UCASE, LCASE) and <b>join</b> strings (&amp;).",
     learn, watch, explore, practise, real, exam, tipshtml, "p814e")

js = []
js.append(f'''
const FN_PS = {json.dumps(FN_PS, ensure_ascii=False)}, FN_PY = {json.dumps(FN_PY, ensure_ascii=False)};
const CT_PS = {json.dumps(CT_PS, ensure_ascii=False)}, CT_PY = {json.dumps(CT_PY, ensure_ascii=False)};
const RV_PS = {json.dumps(RV_PS, ensure_ascii=False)}, RV_PY = {json.dumps(RV_PY, ensure_ascii=False)};
tr($("#aF"), {{ label: "String functions", title: "String functions", pseudo: FN_PS, py: FN_PY, dwell: 2400, frames: {anim_fn()} }});
tr($("#aC"), {{ label: "Counting a letter", title: "Count the letter e", pseudo: CT_PS, py: CT_PY, dwell: 1300, frames: {anim_ct()} }});
tr($("#aR"), {{ label: "Reversing a string", title: "Reverse a string", pseudo: RV_PS, py: RV_PY, dwell: 2000, frames: {anim_rv()} }});
Lib.codePanel($("#cdStr"), {{ pseudo: FN_PS, py: FN_PY }});
Lib.codePanel($("#cdLoop"), {{ pseudo: CT_PS, py: CT_PY }});
Lib.codePanel($("#cdBuild"), {{ pseudo: RV_PS, py: RV_PY }});
''')

js.append(r'''
const cellsHtml = (s, hi) => [...s].map((c, i) => `<span class="${hi(i) ? "m1" : ""}" title="position ${i + 1}">${esc(c === " " ? "␣" : c)}<small style="display:block;font:600 .6rem var(--sans);color:var(--muted);text-align:center">${i + 1}</small></span>`).join("");
/* ---------- Lab 1 ---------- */
(() => {
  let a, b; const inp = $("#ti");
  const upd = () => {
    if (!a || !b) return; const s = inp.value, n = s.length;
    if (!n) { $("#tcells").innerHTML = ""; $("#tt").innerHTML = ""; return; }
    const st = Math.min(a.get(), n), ln = b.get(), sub = s.substr(st - 1, ln);
    $("#tcells").innerHTML = cellsHtml(s, (i) => i >= st - 1 && i < st - 1 + ln);
    $("#tt").innerHTML = `<tr><th>Pseudocode</th><th>Result</th><th>Python</th></tr><tr><td>LENGTH(Text)</td><td>${n}</td><td>len(text)</td></tr><tr><td>UCASE(Text)</td><td>"${esc(s.toUpperCase())}"</td><td>text.upper()</td></tr><tr><td>LCASE(Text)</td><td>"${esc(s.toLowerCase())}"</td><td>text.lower()</td></tr><tr><td>SUBSTRING(Text, ${st}, ${ln})</td><td>"${esc(sub)}"</td><td>text[${st - 1}:${st - 1 + ln}]</td></tr>`;
  };
  a = Lib.slider($("#s1"), { id: "ts", label: "Start position ", min: 1, max: 20, value: 3, onInput: upd });
  b = Lib.slider($("#s2"), { id: "tl", label: "How many characters ", min: 1, max: 10, value: 4, onInput: upd });
  inp.addEventListener("input", upd); upd();
})();

/* ---------- Lab 2 ---------- */
(() => {
  const f = $("#un1"), s = $("#un2");
  const upd = () => {
    const F = f.value, S = s.value;
    Lib.codePanel($("#ucode"), { pseudo: ["Username ← LCASE(SUBSTRING(First, 1, 1) & Surname)", "Initials ← UCASE(SUBSTRING(First, 1, 1) & SUBSTRING(Surname, 1, 1))", 'Greeting ← "Hello " & First & " " & Surname'], py: ["username = (first[0] + surname).lower()", "initials = (first[0] + surname[0]).upper()", 'greeting = "Hello " + first + " " + surname'] });
    if (!F || !S) { $("#ut").innerHTML = "<tr><td>Type a first name and a surname.</td></tr>"; return; }
    $("#ut").innerHTML = `<tr><th>Variable</th><th>Value</th></tr><tr><td>Username</td><td>"${esc((F[0] + S).toLowerCase())}"</td></tr><tr><td>Initials</td><td>"${esc((F[0] + S[0]).toUpperCase())}"</td></tr><tr><td>Greeting</td><td>"${esc("Hello " + F + " " + S)}"</td></tr><tr><td>LENGTH(Surname)</td><td>${S.length}</td></tr>`;
  };
  f.addEventListener("input", upd); s.addEventListener("input", upd); upd();
})();

/* ---------- Lab 3 ---------- */
(() => {
  const w = $("#lw"), l = $("#ll");
  const upd = () => { const W = w.value, L = l.value; if (!W) { $("#lcells").innerHTML = ""; $("#lv").textContent = "Type a word."; return; }
    let c = 0; [...W].forEach((x) => { if (x === L) c++; });
    $("#lcells").innerHTML = cellsHtml(W, (i) => L && W[i] === L);
    $("#lv").innerHTML = L ? `The loop checks ${W.length} positions. <b>${L}</b> matches ${c} time${c === 1 ? "" : "s"}, so <b>Count = ${c}</b>.${/[A-Z]/.test(W + L) ? " Capital and lower-case letters are different characters." : ""}` : "Type one letter to count."; };
  w.addEventListener("input", upd); l.addEventListener("input", upd); upd();
})();

/* ---------- Practise ---------- */
Lib.match($("#m1"), { prompt: "Match each expression to what it gives.", pairs: [
  ['LENGTH("Hello")', "5"], ['UCASE("hi")', '"HI"'], ['SUBSTRING("Computer", 1, 3)', '"Com"'], ['"Good" & "Day"', '"GoodDay"'], ['LCASE("ABC")', '"abc"'], ['SUBSTRING("Computer", 8, 1)', '"r"']],
  done: "Positions start at 1, and & joins." });
Lib.order($("#o1"), { prompt: "Put the lines of the reverse program in order.", items: ['Word ← "STAR"', 'Reverse ← ""', "FOR Index ← 1 TO LENGTH(Word)", "Reverse ← SUBSTRING(Word, Index, 1) & Reverse", "NEXT Index", "OUTPUT Reverse"], done: "Set up, empty string, loop, join on the front, end loop, output." });
Lib.calc($("#c1"), { qs: [
  { q: "What is LENGTH(\"Good morning\")?", a: 12, sol: "Good (4) + space (1) + morning (7) = 12." },
  { q: "What is SUBSTRING(\"Computer\", 4, 3)? Type the letters.", t: ["PUT"], ph: "letters", sol: "Start at position 4 (p) and take 3: put." },
  { q: "SUBSTRING(Word, 1, 1) with Word = \"Python\" gives which letter?", t: ["P"], ph: "letter", sol: "Position 1 is the first letter." },
  { q: "FOR Index ← 1 TO LENGTH(\"banana\"). How many times does the loop run?", a: 6, sol: "LENGTH(\"banana\") is 6." },
  { q: "The loop counts how many times \"a\" appears in \"banana\". What is Count at the end?", a: 3, sol: "b-a-n-a-n-a: three a's." },
  { q: "In Python, which index is the same as pseudocode position 5?", a: 4, sol: "Python starts at 0, so position 5 is index 4." }] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What does LENGTH(\"hi there\") return?", opts: ["8", "7", "2", "9"], a: 0, why: "The space counts as a character." },
  { q: "In pseudocode, the first character of a string is at position...", opts: ["1", "0", "-1", "LENGTH"], a: 0, why: "Cambridge pseudocode starts at 1. Python starts at 0." },
  { q: "Which symbol joins two strings in pseudocode?", opts: ["&", "+", "*", "/"], a: 0, why: "& is concatenation." },
  { q: "SUBSTRING(\"Computer\", 2, 3) is...", opts: ["\"omp\"", "\"Com\"", "\"mpu\"", "\"ompu\""], a: 0, why: "Start at 2 (o), take 3: omp." },
  { q: "Are \"a\" and \"A\" equal in a comparison?", opts: ["No, they are different characters", "Yes", "Only in Python", "Only in a FOR loop"], a: 0, why: "Use UCASE or LCASE first to ignore case." }] });
Lib.cards($("#fc1"), { cards: [
  ["String", "A sequence of characters, for example \"Hello\"."],
  ["Character", "A single letter, digit, space or symbol."],
  ["LENGTH", "A function that gives the number of characters in a string."],
  ["SUBSTRING", "A function that takes part of a string: SUBSTRING(String, start, how many)."],
  ["UCASE / LCASE", "Functions that give the string in upper case or in lower case."],
  ["Concatenation", "Joining strings together, using & in pseudocode."],
  ["Position", "The place of a character in a string. It starts at 1 in pseudocode."],
  ["Empty string", "A string with no characters, written \"\"."]] });
''')
write_js("p814e", js)
