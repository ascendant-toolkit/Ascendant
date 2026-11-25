"""8.1.7 Library routines: MOD, DIV, ROUND, RANDOM."""
from p814k import *

CH_PS = ["INPUT Cents", "Coins50 ← DIV(Cents, 50)", "Left ← MOD(Cents, 50)", "Coins10 ← DIV(Left, 10)", "Left ← MOD(Left, 10)", "OUTPUT Coins50, Coins10, Left"]
CH_PY = ["cents = int(input())", "coins50 = cents // 50", "left = cents % 50", "coins10 = left // 10", "left = left % 10", "print(coins50, coins10, left)"]
AV_PS = ["INPUT Total", "INPUT Number", "Average ← Total / Number", "Rounded ← ROUND(Average, 2)", "OUTPUT Rounded"]
AV_PY = ["total = float(input())", "number = int(input())", "average = total / number", "rounded = round(average, 2)", "print(rounded)"]
DI_PS = ["Sixes ← 0", "FOR Throw ← 1 TO 4", "    Dice ← ROUND(RANDOM() * 5, 0) + 1", "    OUTPUT Dice", "    IF Dice = 6", "      THEN", "        Sixes ← Sixes + 1", "    ENDIF", "NEXT Throw", 'OUTPUT "Sixes: ", Sixes']
DI_PY = ["import random", "sixes = 0", "for throw in range(1, 5):", "    dice = random.randint(1, 6)", "    print(dice)", "    if dice == 6:", "        sixes = sixes + 1", 'print("Sixes:", sixes)']


def anim_change():
    r = R(["Cents", "Coins50", "Coins10", "Left"])
    r.f("A machine gives change using as few coins as possible. The change is 185 cents.", [0], [], inp=[185])
    r.v["Cents"] = 185; r.f("<b>INPUT Cents</b>: 185.", [0], [0], hl=["Cents"], inp=[])
    r.v["Coins50"] = 185 // 50; r.f("<b>DIV(185, 50)</b> = 3. Three 50c coins fit (150).", [1], [1], hl=["Coins50"], note="DIV(185, 50) = 3", nc="t4")
    r.v["Left"] = 185 % 50; r.f("<b>MOD(185, 50)</b> = 35. This is what is <b>left over</b>.", [2], [2], hl=["Left"], note="MOD(185, 50) = 35", nc="t4")
    r.v["Coins10"] = 35 // 10; r.f("<b>DIV(35, 10)</b> = 3 ten-cent coins.", [3], [3], hl=["Coins10"], note="DIV(35, 10) = 3", nc="t4")
    r.v["Left"] = 35 % 10; r.f("<b>MOD(35, 10)</b> = 5 cents remain.", [4], [4], hl=["Left"], note="MOD(35, 10) = 5", nc="t4")
    r.out.append("3 3 5"); r.f("<b>OUTPUT</b>: 3 fifties, 3 tens and 5 cents. 150 + 30 + 5 = 185.", [5], [5])
    return r.js()


def anim_avg():
    r = R(["Total", "Number", "Average", "Rounded"])
    r.f("Work out an average and show it neatly. The user types 200, then 7.", [0], [], inp=[200, 7])
    r.v["Total"] = 200; r.f("<b>INPUT Total</b>: 200.", [0], [0], hl=["Total"], inp=[7])
    r.v["Number"] = 7; r.f("<b>INPUT Number</b>: 7.", [1], [1], hl=["Number"], inp=[])
    r.v["Average"] = round(200 / 7, 5); r.f("<b>200 / 7</b> gives a long decimal.", [2], [2], hl=["Average"])
    r.v["Rounded"] = round(200 / 7, 2); r.f("<b>ROUND(Average, 2)</b> keeps <b>2 decimal places</b>. The third decimal is 1, so it rounds down to 28.57.", [3], [3], hl=["Rounded"])
    r.out.append(str(r.v["Rounded"])); r.f("<b>OUTPUT Rounded</b>. Average itself has not changed.", [4], [4])
    return r.js()


def anim_dice():
    samples = [0.62, 0.97, 0.08, 0.93]; r = R(["Throw", "Dice", "Sixes"]); c = 0
    r.v["Sixes"] = 0; r.f("<b>Sixes ← 0</b>. A dice is thrown 4 times. The random values here are examples: a real run gives different ones.", [0], [1], hl=["Sixes"])
    for i, x in enumerate(samples):
        d = int(x * 5 + 0.5) + 1; r.v["Throw"] = i + 1; r.v["Dice"] = d
        r.f(f"<b>RANDOM()</b> gives {x}. {x} × 5 = {x * 5:.2f}, ROUND to 0 places = {d - 1}, then + 1 = <b>{d}</b>.", [1, 2], [2, 3], hl=["Throw", "Dice"], note=f"ROUND({x} * 5, 0) + 1 = {d}", nc="t4")
        r.out.append(str(d)); ok = d == 6
        r.f(f"OUTPUT {d}. Is Dice = 6?", [3, 4], [4, 5], cond=(f"{d} = 6", ok))
        if ok:
            c += 1; r.v["Sixes"] = c; r.f(f"TRUE, so <b>Sixes ← {c}</b>.", [6], [6], hl=["Sixes"])
    r.out.append(f"Sixes: {c}"); r.f(f"After the loop, output the count: <b>{c}</b>.", [9], [7])
    return r.js()


learn = '''
  <h2>8.1.7 Library routines</h2>
  <p>A <span class="kw">library routine</span> is a <b>ready-written, tested</b> procedure or function that comes with the programming language. You call it by name and give it the values it needs. You need to know four: <b>MOD</b>, <b>DIV</b>, <b>ROUND</b> and <b>RANDOM</b>.</p>
  <div class="tip"><b class="h">Why use them?</b>They save time, they have already been tested (so fewer errors), programmers do not need to know how they work inside, and they make code shorter and easier to read.</div>

  <div class="tw"><table class="t">
    <tr><th>Routine</th><th>Returns</th><th>Example</th><th>Result</th><th>Python</th></tr>
    <tr><td>DIV(X, Y)</td><td>whole number of times Y goes into X</td><td>DIV(17, 5)</td><td>3</td><td>17 // 5</td></tr>
    <tr><td>MOD(X, Y)</td><td>remainder after X is divided by Y</td><td>MOD(17, 5)</td><td>2</td><td>17 % 5</td></tr>
    <tr><td>ROUND(Value, Places)</td><td>Value rounded to that many decimal places</td><td>ROUND(7.4682, 2)</td><td>7.47</td><td>round(7.4682, 2)</td></tr>
    <tr><td>RANDOM()</td><td>a random number from 0 to 1</td><td>RANDOM()</td><td>e.g. 0.6182</td><td>random.random()</td></tr>
  </table></div>

  <h3>DIV and MOD</h3>
  <p>17 ÷ 5 is <b>3 remainder 2</b>: DIV gives the 3 and MOD gives the 2. You met these as operators in 8.1.4, where they are written <span class="ln2">17 DIV 5</span> and <span class="ln2">17 MOD 5</span>. Both ways of writing them mean the same thing.</p>
  <div class="tw"><table class="t">
    <tr><th>Job</th><th>Code</th></tr>
    <tr><td>Is N even?</td><td>MOD(N, 2) = 0</td></tr>
    <tr><td>Is N a multiple of 5?</td><td>MOD(N, 5) = 0</td></tr>
    <tr><td>Last digit of N</td><td>MOD(N, 10)</td></tr>
    <tr><td>Remove the last digit</td><td>DIV(N, 10)</td></tr>
    <tr><td>Full boxes of 12, and items left</td><td>DIV(N, 12) and MOD(N, 12)</td></tr>
  </table></div>

  <h3>ROUND</h3>
  <p>The second value is the number of <b>decimal places</b>. Look at the next digit: 5 or more rounds up, 4 or less rounds down. <span class="ln2">ROUND(X, 0)</span> gives a whole number.</p>
  <div id="cdR" class="code"></div>
  <div class="tip"><b class="h">Python difference</b>Python's <code>round()</code> sends an exact half to the nearest <b>even</b> number, so <code>round(2.5)</code> is 2. In the exam, round halves up.</div>

  <h3>RANDOM</h3>
  <p><span class="ln2">RANDOM()</span> gives a decimal between 0 and 1. To get a whole number in a range, <b>multiply</b> to stretch it, <b>ROUND</b> to make it whole, then <b>add</b> to move the start.</p>
  <div class="tw"><table class="t">
    <tr><th>Wanted</th><th>Expression</th></tr>
    <tr><td>0 to 10</td><td>ROUND(RANDOM() * 10, 0)</td></tr>
    <tr><td>1 to 6</td><td>ROUND(RANDOM() * 5, 0) + 1</td></tr>
    <tr><td>50 to 100</td><td>ROUND(RANDOM() * 50, 0) + 50</td></tr>
    <tr><td>Low to High</td><td>ROUND(RANDOM() * (High − Low), 0) + Low</td></tr>
  </table></div>
  <p>With this method the two end values come up about half as often as the others. That is fine for the exam. In Python, <code>random.randint(1, 6)</code> gives each whole number from 1 to 6 equally, and needs <code>import random</code>.</p>
  <div id="cdD" class="code"></div>
'''

watch = '''  <h2>1 · Giving change with DIV and MOD</h2><div id="aC"></div>
  <h2>2 · Rounding an average</h2><div id="aA"></div>
  <h2>3 · Throwing a dice with RANDOM</h2><div id="aD"></div>
'''

explore = '''  <h2>Lab 1 · DIV and MOD splitter</h2>
  <p>Share a number of items into boxes. Each filled box counts towards DIV; loose items are MOD.</p>
  <div class="card"><div id="s1"></div><div id="s2"></div><div class="readout"><div><small>DIV</small><strong id="ld"></strong></div><div><small>MOD</small><strong id="lm"></strong></div></div><div id="boxes" style="margin:10px 0"></div><div class="verdict" id="lv" aria-live="polite"></div></div>

  <h2>Lab 2 · ROUND</h2>
  <div class="card"><div id="s3"></div><div id="s4"></div><div class="readout"><div><small>Value</small><strong id="rv0"></strong></div><div><small>Rounded</small><strong id="rv1"></strong></div></div><div class="verdict" id="rv2" aria-live="polite"></div></div>

  <h2>Lab 3 · Random range builder</h2>
  <p>Choose a lowest and highest value, then roll many times. Check that nothing lands outside the range.</p>
  <div class="card"><div id="s5"></div><div id="s6"></div><div id="xcode"></div><div class="row"><button class="b pri" id="roll1">Roll once</button><button class="b" id="roll600">Roll 600 times</button></div><div class="verdict" id="xv" aria-live="polite"></div><div id="bars"></div></div>
'''

practise = '''  <h2>1 · Which routine?</h2>
  <div id="cl1" class="card"></div>
  <h2>2 · Match the call to the result</h2>
  <div id="m1" class="card"></div>
  <h2>3 · Calculate</h2>
  <div id="c1"></div>
  <h2>4 · Multiple choice</h2>
  <div id="qz1"></div>
'''

real = (rw("A vending machine", "To give change, the machine finds how many of each coin fit, then what is left.", "DIV for the number of coins, MOD for the amount remaining.")
        + rw("A shop receipt", "A discount can produce many decimal places, but a price is shown with two.", "ROUND(Price, 2) before output.")
        + rw("A board game app", "Each turn needs an unpredictable dice score from 1 to 6.", "RANDOM stretched, rounded and shifted into the range.")
        + rw("A music shuffle button", "The player picks a track number it cannot predict from the length of the playlist.", "RANDOM to choose a whole number between 1 and the number of songs."))

ex = [
    eq(1, "State", 2, "State what is meant by a <b>library routine</b> and give one example.", "Ready-made.",
       mk(1, "A pre-written (and tested) procedure / function that can be called in a program") + " " + mk(2, "e.g. MOD, DIV, ROUND or RANDOM"),
       "Giving a keyword such as IF or FOR as an example."),
    eq(2, "State", 2, "State two benefits of using library routines.", "Think time and errors.",
       mk(1, "Saves time, as the code does not need to be written") + " " + mk(2, "Already tested, so less likely to contain errors"),
       "Writing \"it is better\" without saying how."),
    eq(3, "Give", 4, "Give the value of: DIV(29, 4), MOD(29, 4), ROUND(13.4673, 2) and ROUND(8.62, 0).", "Whole times, remainder, decimal places.",
       mk(1, "7") + " " + mk(2, "1") + " " + mk(3, "13.47") + " " + mk(4, "9"),
       "Giving 7.25 for DIV. DIV only returns the whole part."),
    eq(4, "Write", 3, "Write pseudocode to input a whole number and output \"Even\" or \"Odd\".", "Use MOD.",
       mk(1, "INPUT Number") + " " + mk(2, "IF MOD(Number, 2) = 0") + " " + mk(3, 'correct output in each branch, closed with ENDIF')
       + ac(["INPUT Number", "IF MOD(Number, 2) = 0", "  THEN", '    OUTPUT "Even"', "  ELSE", '    OUTPUT "Odd"', "ENDIF"]),
       "Using DIV(Number, 2) = 0, which does not test the remainder."),
    eq(5, "Write", 4, "Eggs are packed in boxes of 6. Write pseudocode to input the number of eggs and output the number of full boxes and the number of eggs left over.", "One DIV and one MOD.",
       mk(1, "INPUT Eggs") + " " + mk(2, "Boxes ← DIV(Eggs, 6)") + " " + mk(3, "Left ← MOD(Eggs, 6)") + " " + mk(4, "OUTPUT Boxes and Left")
       + ac(["INPUT Eggs", "Boxes ← DIV(Eggs, 6)", "Left ← MOD(Eggs, 6)", "OUTPUT Boxes, Left"]),
       "Using Eggs / 6, which gives a decimal number of boxes."),
    eq(6, "Write", 3, "Write a statement that stores a random whole number from 1 to 100 in Secret, and explain what each part does.", "Stretch, round, shift.",
       mk(1, "RANDOM() * 99 gives a value from 0 to 99") + " " + mk(2, "ROUND(..., 0) makes it a whole number") + " " + mk(3, "+ 1 moves the range to 1 to 100")
       + ac(["Secret ← ROUND(RANDOM() * 99, 0) + 1"]),
       "Using RANDOM() * 100 + 1, which can give 101."),
    eq(7, "State", 2, "State the smallest and the largest value that can be stored in X.", "Try RANDOM() as 0 and as 1.",
       mk(1, "Smallest: 10") + " " + mk(2, "Largest: 30"),
       "Saying 0 and 20, forgetting to add 10.", pre=qc(["X ← ROUND(RANDOM() * 20, 0) + 10"])),
    eq(8, "Write", 6, "Write pseudocode for a guessing game. The program picks a random whole number from 1 to 10. The user keeps guessing until correct. Output the number of guesses taken.", "Pick the number once, before the loop.",
       mk(1, "Secret ← ROUND(RANDOM() * 9, 0) + 1 before the loop") + " " + mk(2, "Guesses ← 0 before the loop") + " " + mk(3, "REPEAT with INPUT Guess inside") + " " + mk(4, "add 1 to Guesses inside the loop") + " " + mk(5, "UNTIL Guess = Secret") + " " + mk(6, "OUTPUT Guesses after the loop")
       + ac(["Secret ← ROUND(RANDOM() * 9, 0) + 1", "Guesses ← 0", "REPEAT", "    INPUT Guess", "    Guesses ← Guesses + 1", "UNTIL Guess = Secret", "OUTPUT Guesses"]),
       "Generating a new random number inside the loop, so the target keeps moving."),
    eq(9, "Write", 5, "Write a function DigitSum that takes a two-digit whole number and returns the sum of its two digits. Show a call that outputs the result for 47.", "DIV for the tens digit, MOD for the units digit.",
       mk(1, "FUNCTION DigitSum(Number : INTEGER) RETURNS INTEGER ... ENDFUNCTION") + " " + mk(2, "Tens ← DIV(Number, 10)") + " " + mk(3, "Units ← MOD(Number, 10)") + " " + mk(4, "RETURN Tens + Units") + " " + mk(5, "OUTPUT DigitSum(47)")
       + ac(["FUNCTION DigitSum(Number : INTEGER) RETURNS INTEGER", "    DECLARE Tens : INTEGER", "    DECLARE Units : INTEGER", "    Tens ← DIV(Number, 10)", "    Units ← MOD(Number, 10)", "    RETURN Tens + Units", "ENDFUNCTION", "", "OUTPUT DigitSum(47)"]),
       "Swapping DIV and MOD."),
    eq(10, "Write", 5, "Write pseudocode to input 5 prices, total them, and output the average rounded to 2 decimal places.", "Round once, at the end.",
       mk(1, "Total ← 0 before the loop") + " " + mk(2, "loop 5 times with INPUT Price") + " " + mk(3, "Total ← Total + Price") + " " + mk(4, "Average ← ROUND(Total / 5, 2) after the loop") + " " + mk(5, "OUTPUT Average")
       + ac(["Total ← 0", "FOR Count ← 1 TO 5", "    INPUT Price", "    Total ← Total + Price", "NEXT Count", "Average ← ROUND(Total / 5, 2)", "OUTPUT Average"]),
       "Rounding inside the loop, or leaving out the number of decimal places."),
]

tipshtml = tips([
    "<b>DIV = how many whole times. MOD = what is left.</b>",
    "<b>MOD(N, X) = 0 means N divides exactly by X.</b>",
    "<b>ROUND needs two values:</b> what to round, and how many decimal places.",
    "<b>RANDOM range:</b> ROUND(RANDOM() * (High − Low), 0) + Low. Check both ends.",
    "<b>A library routine returns a value</b>, so store it, output it or use it in a condition.",
    "<b>In Python, import random first.</b>",
])

page("8.1.7 · Library routines", "Library Routines", "MOD, DIV, ROUND and RANDOM: ready-made tools you can call in any program.",
     "A <span class=\"kw\">library routine</span> is code somebody else has already <b>written and tested</b>. You just call it. <b>DIV</b> and <b>MOD</b> split numbers, <b>ROUND</b> tidies decimals and <b>RANDOM</b> makes results unpredictable.",
     learn, watch, explore, practise, real, "".join(ex), tipshtml, "p817")

js = []
consts = ", ".join(f"{n} = {json.dumps(v, ensure_ascii=False)}" for n, v in [("CH_PS", CH_PS), ("CH_PY", CH_PY), ("AV_PS", AV_PS), ("AV_PY", AV_PY), ("DI_PS", DI_PS), ("DI_PY", DI_PY)])
js.append(f'''
const {consts};
tr($("#aC"), {{ label: "DIV and MOD", title: "Giving change", pseudo: CH_PS, py: CH_PY, frames: {anim_change()} }});
tr($("#aA"), {{ label: "ROUND", title: "Rounding an average", pseudo: AV_PS, py: AV_PY, frames: {anim_avg()} }});
tr($("#aD"), {{ label: "RANDOM", title: "Throwing a dice", pseudo: DI_PS, py: DI_PY, frames: {anim_dice()} }});
Lib.codePanel($("#cdR"), {{ pseudo: ["OUTPUT ROUND(3.14159, 2)    // 3.14", "OUTPUT ROUND(3.14159, 3)    // 3.142", "OUTPUT ROUND(9.7, 0)        // 10"], py: ["print(round(3.14159, 2))    # 3.14", "print(round(3.14159, 3))    # 3.142", "print(round(9.7))           # 10"] }});
Lib.codePanel($("#cdD"), {{ pseudo: ["Dice ← ROUND(RANDOM() * 5, 0) + 1", "OUTPUT Dice"], py: ["import random", "dice = random.randint(1, 6)", "print(dice)"] }});
''')

js.append(r'''
/* ---------- Lab 1 ---------- */
(() => {
  let a, b;
  const upd = () => { if (!a || !b) return; const n = a.get(), s = b.get(), q = Math.floor(n / s), m = n % s;
    $("#ld").textContent = q; $("#lm").textContent = m;
    const box = (k, full) => `<span style="display:inline-block;border:2px ${full ? "solid var(--good)" : "dashed var(--warn)"};border-radius:8px;padding:2px 6px;margin:0 6px 6px 0;letter-spacing:2px">${"●".repeat(k)}</span>`;
    $("#boxes").innerHTML = Array(q).fill(box(s, true)).join("") + (m ? box(m, false) : "");
    $("#lv").innerHTML = `${n} items in boxes of ${s}: <b>DIV(${n}, ${s}) = ${q}</b> full boxes and <b>MOD(${n}, ${s}) = ${m}</b> left over. Check: ${q} × ${s} + ${m} = ${n}.`; };
  a = Lib.slider($("#s1"), { id: "dn", label: "Items ", min: 0, max: 60, value: 29, onInput: upd });
  b = Lib.slider($("#s2"), { id: "ds", label: "Items per box ", min: 2, max: 12, value: 4, onInput: upd });
  upd();
})();

/* ---------- Lab 2 ---------- */
(() => {
  let a, b;
  const upd = () => { if (!a || !b) return; const v = a.get(), p = b.get(), k = 10 ** (4 - p), out = (Math.floor(v / k + 0.5) / 10 ** p).toFixed(p), val = (v / 10000).toFixed(4), digit = p < 4 ? Math.floor(v / (k / 10)) % 10 : null;
    $("#rv0").textContent = val; $("#rv1").textContent = out;
    $("#rv2").innerHTML = `<b>ROUND(${val}, ${p})</b> = ${out}. ` + (digit === null ? "There are no digits to remove." : `The first digit removed is ${digit}, so it rounds <b>${digit >= 5 ? "up" : "down"}</b>.`); };
  a = Lib.slider($("#s3"), { id: "rn", label: "Value ", min: 0, max: 200000, value: 74682, fmt: (v) => (v / 10000).toFixed(4), onInput: upd });
  b = Lib.slider($("#s4"), { id: "rp", label: "Decimal places ", min: 0, max: 4, value: 2, onInput: upd });
  upd();
})();

/* ---------- Lab 3 ---------- */
(() => {
  let a, b;
  const range = () => { const lo = a.get(), hi = lo + b.get(); return [lo, hi]; };
  const upd = () => { if (!a || !b) return; const [lo, hi] = range();
    Lib.codePanel($("#xcode"), { pseudo: [`Number ← ROUND(RANDOM() * ${hi - lo}, 0) + ${lo}`], py: ["import random", `number = random.randint(${lo}, ${hi})`] });
    $("#xv").innerHTML = `Range: <b>${lo} to ${hi}</b>.`; $("#bars").innerHTML = ""; };
  const one = () => { const [lo, hi] = range(); return Math.round(Math.random() * (hi - lo)) + lo; };
  a = Lib.slider($("#s5"), { id: "xl", label: "Lowest value ", min: 0, max: 20, value: 1, onInput: upd });
  b = Lib.slider($("#s6"), { id: "xs", label: "Size of range (highest − lowest) ", min: 1, max: 10, value: 5, onInput: upd });
  $("#roll1").onclick = () => { $("#xv").innerHTML = `Number = <b>${one()}</b>`; $("#bars").innerHTML = ""; };
  $("#roll600").onclick = () => { const [lo, hi] = range(), n = {}; for (let i = 0; i < 600; i++) { const x = one(); n[x] = (n[x] || 0) + 1; } const top = Math.max(...Object.values(n));
    $("#bars").innerHTML = Array.from({ length: hi - lo + 1 }, (_, i) => { const c = n[lo + i] || 0; return `<div style="display:flex;align-items:center;gap:8px;margin:3px 0;font-family:var(--mono);font-size:.85rem"><span style="width:2.5em;text-align:right">${lo + i}</span><span style="height:14px;border-radius:4px;background:var(--accent);width:${(c / top) * 70}%"></span><span>${c}</span></div>`; }).join("");
    $("#xv").innerHTML = `600 rolls, all between <b>${lo}</b> and <b>${hi}</b>. The two end values appear about half as often.`; };
  upd();
})();

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Which routine does each job need?", buckets: [{ label: "DIV" }, { label: "MOD" }, { label: "ROUND" }, { label: "RANDOM" }], items: [
  { text: "How many whole weeks in a number of days", b: 0 }, { text: "Number of full teams of 5", b: 0 },
  { text: "Test whether a number is odd", b: 1 }, { text: "Get the last digit of a number", b: 1 },
  { text: "Show a price with 2 decimal places", b: 2 }, { text: "Give a measurement to the nearest whole number", b: 2 },
  { text: "Shuffle which question appears next", b: 3 }, { text: "Simulate tossing a coin", b: 3 }],
  done: "DIV: whole times. MOD: remainder. ROUND: decimal places. RANDOM: unpredictable." });
Lib.match($("#m1"), { prompt: "Drag each result to its call.", pairs: [["DIV(38, 5)", "7"], ["MOD(38, 5)", "3"], ["ROUND(38.456, 1)", "38.5"], ["ROUND(38.456, 0)", "38"], ["MOD(40, 5)", "0"]] });
Lib.calc($("#c1"), { qs: [
  { q: "DIV(100, 7)", a: 14, sol: "7 × 14 = 98, so 14 whole times." },
  { q: "MOD(100, 7)", a: 2, sol: "100 − 98 = 2." },
  { q: "MOD(3, 10)", a: 3, sol: "10 goes into 3 zero times, so 3 is left." },
  { q: "ROUND(46.2951, 2)", a: 46.3, tol: 0.001, sol: "The third decimal is 5, so 46.29 rounds up to 46.30." },
  { q: "DIV(MOD(257, 100), 10)", a: 5, sol: "MOD(257, 100) = 57, then DIV(57, 10) = 5." },
  { q: "Largest value of ROUND(RANDOM() * 8, 0) + 2", a: 10, sol: "RANDOM() up to 1: 8 + 2 = 10." }] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What does RANDOM() return?", opts: ["A number between 0 and 1", "A whole number between 1 and 10", "The remainder of a division", "A number rounded to 2 places"], a: 0, why: "Stretch and round it to get other ranges." },
  { q: "What is the 2 in ROUND(X, 2)?", opts: ["The number of decimal places", "The number to divide by", "The number of digits in total", "The number of times to round"], a: 0, why: "ROUND(value, places)." },
  { q: "Which expression is TRUE when N is a multiple of 3?", opts: ["MOD(N, 3) = 0", "DIV(N, 3) = 0", "MOD(3, N) = 0", "ROUND(N, 3) = 0"], a: 0, why: "No remainder means it divides exactly." },
  { q: "Why use a library routine?", opts: ["It is already written and tested", "It makes variables global", "It removes the need to call it", "It stops all run-time errors"], a: 0, why: "Saves time and reduces errors." },
  { q: "Which gives a whole number from 5 to 15?", opts: ["ROUND(RANDOM() * 10, 0) + 5", "ROUND(RANDOM() * 15, 0) + 5", "ROUND(RANDOM() * 5, 0) + 15", "RANDOM() * 10 + 5"], a: 0, why: "Range size 10, starting at 5." }] });
Lib.cards($("#fc1"), { cards: [
  ["Library routine", "A pre-written, tested procedure or function you can call."],
  ["DIV", "Returns the whole number part of a division."],
  ["MOD", "Returns the remainder of a division."],
  ["ROUND", "Rounds a value to a given number of decimal places."],
  ["RANDOM", "Returns a random number between 0 and 1."]] });
''')
write_js("p817", js)
