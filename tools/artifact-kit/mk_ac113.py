"""A Level CS syllabus 1.1.3: character sets (ASCII, extended ASCII, Unicode). Run: python3 tools/artifact-kit/mk_ac113.py"""
from ak import *

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>A <b>character set</b> is the list of characters a computer can use, with a unique binary code for each one. <b>ASCII</b> uses 7 bits (128 characters), <b>extended ASCII</b> uses 8 bits (256 characters) and <b>Unicode</b> uses up to 32 bits, enough for every writing system plus symbols and emojis. To store text, each character is replaced by its code and the codes are stored in the same order as the characters in the word. Unicode can represent far more characters but needs more bits per character, so text files are bigger. You are not expected to memorise any codes, but you must be able to work with them once the question gives you a starting value.</p></div>

  <h2>1 · What a character set is</h2>
  <p>A computer only stores binary, so every letter, digit, punctuation mark and symbol needs a number. A character set fixes which number belongs to which character, so the sender and receiver agree. Without agreement the same bits would show different characters.</p>
  <div class="tw"><table class="t">
    <tr><th>Character set</th><th>Bits per character</th><th>Number of characters</th><th>What it covers</th></tr>
    <tr><td><b>ASCII</b> (American Standard Code for Information Interchange)</td><td>7</td><td>128 (2<sup>7</sup>)</td><td>English letters in upper and lower case, digits 0 to 9, punctuation and control codes</td></tr>
    <tr><td><b>Extended ASCII</b></td><td>8</td><td>256 (2<sup>8</sup>)</td><td>ASCII plus 128 more: accented letters, some symbols and box characters</td></tr>
    <tr><td><b>Unicode</b></td><td>16 or 32 (up to 32)</td><td>Over a million possible codes</td><td>Almost every language, mathematical and other symbols, emojis</td></tr>
  </table></div>
  <ul>
    <li><b>ASCII is a subset of Unicode.</b> The first 128 Unicode codes are the same as ASCII, so plain English text is compatible.</li>
    <li><b>Unicode encodings:</b> the syllabus asks about Unicode as a set. In practice UTF-8 uses 8 to 32 bits per character, UTF-16 uses 16 or 32, and UTF-32 always uses 32. Exam answers say "16 or 32 bits" or "up to 32 bits".</li>
    <li><b>Other character sets</b> exist, and a question that asks you to "identify one other character set" accepts extended ASCII, or another valid set such as UTF-8 or ISO 8859-1.</li>
  </ul>

  <h2>2 · How a word is stored</h2>
  <ol>
    <li>Split the word into characters: C, l, o, c, k.</li>
    <li>Replace each character with its unique code: 67, 108, 111, 99, 107.</li>
    <li>Write each code in binary using the bits per character: 1000011, 1101100 ...</li>
    <li>Store the binary codes <b>in sequence</b>, in the same order as the letters in the word.</li>
  </ol>
  <div class="tw"><table class="t mono">
    <tr><th>Character</th><th>Denary</th><th>Hex</th><th>7-bit ASCII</th><th>8-bit</th></tr>
    <tr><td>A</td><td>65</td><td>41</td><td>100 0001</td><td>0100 0001</td></tr>
    <tr><td>Z</td><td>90</td><td>5A</td><td>101 1010</td><td>0101 1010</td></tr>
    <tr><td>a</td><td>97</td><td>61</td><td>110 0001</td><td>0110 0001</td></tr>
    <tr><td>0 (the digit character)</td><td>48</td><td>30</td><td>011 0000</td><td>0011 0000</td></tr>
    <tr><td>1 (the digit character)</td><td>49</td><td>31</td><td>011 0001</td><td>0011 0001</td></tr>
  </table></div>
  <ul>
    <li><b>Codes run in order.</b> If A is 65 then B is 66. If a is 97 then f is 102. A question usually gives you one code and asks for another by counting along.</li>
    <li><b>Upper case and lower case differ by 32,</b> which is a single bit (the 32 column): A = 0100 0001 and a = 0110 0001.</li>
    <li><b>The character '5' is not the number 5.</b> The digit character '1' has the code 49 (hex 31), so '5' is 53. The numeric value 5 would be stored as 0000 0101.</li>
    <li>Unicode values are normally written in <b>hexadecimal</b>. To convert, use the hex rules from syllabus 1.1.1: hex 2140 = 2 × 4096 + 1 × 256 + 4 × 16 = <b>8512</b>.</li>
  </ul>

  <h2>3 · ASCII or Unicode: the comparison</h2>
  <div class="tw"><table class="t">
    <tr><th></th><th>ASCII (and extended ASCII)</th><th>Unicode</th></tr>
    <tr><td>Characters</td><td>128 or 256, mostly English and Western European letters</td><td>A much wider range: many languages, symbols, emojis</td></tr>
    <tr><td>Bits per character</td><td>7 or 8</td><td>16 or 32 (up to 32)</td></tr>
    <tr><td>File size for the same text</td><td>Smaller</td><td>Larger, because each character needs more bits</td></tr>
    <tr><td>Languages</td><td>One main language (English); extended ASCII adds some accents</td><td>Every language can be represented in one document</td></tr>
    <tr><td>Similarity</td><td colspan="2">Both give every character its own unique binary code. Both are character sets that map characters to codes.</td></tr>
  </table></div>
  <div class="tip"><b class="h">Exam tip</b>For "advantages of Unicode over ASCII" write the range: more characters, so more languages, and symbols such as emojis. Only saying "it uses more bits" is a feature, not an advantage. Add the consequence: it needs more storage.</div>

  <h2>4 · Text file size</h2>
  <p>The size of plain text is the number of characters multiplied by the bits per character. 2000 characters in 7-bit ASCII is 14 000 bits (1750 bytes). In 8-bit extended ASCII it is 16 000 bits (2000 bytes). In 16-bit Unicode it is 32 000 bits (4000 bytes). A text file's size is not changed by the language, only by the character set and the number of characters.</p>

  <h2>5 · Common ways to lose marks</h2>
  <ul>
    <li>Saying "ASCII has fewer characters" without a number or a comparison with Unicode.</li>
    <li>Writing that each word has one code. Each <b>character</b> has its own code, and the codes are stored in order.</li>
    <li>Confusing the digit character with the number it names.</li>
    <li>Quoting the wrong bits: ASCII is 7, extended ASCII is 8.</li>
    <li>Giving a similarity that is really a difference, for example "both use 8 bits". Ask whether it is true of both.</li>
  </ul>
'''

watch = '''
  <h2>1 · How the word "Clock" is stored</h2>
  <p>Press Play, or click the numbered steps. Each letter becomes a code, then binary, in order.</p>
  <div id="stA"></div>
  <h2>2 · The same text, three character sets</h2>
  <div id="stB"></div>
  <h2>3 · Upper case and lower case: one bit apart</h2>
  <div id="stC"></div>
'''

explore = '''
  <h2>Lab 1 · Type some text</h2>
  <p>Type up to 12 characters. See each code in denary, hexadecimal and binary, and the storage needed in each character set. Characters outside a set show as not available.</p>
  <div class="card"><input id="tx" type="text" maxlength="12" value="Clock 5" style="width:100%;font:600 1.1rem var(--mono);padding:8px 10px;border-radius:8px;border:1px solid var(--line);background:var(--surface);color:var(--ink)" aria-label="Text to encode">
    <div id="txT" style="margin-top:12px"></div>
    <div class="readout"><div><small>7-bit ASCII</small><strong id="x1"></strong></div><div><small>8-bit extended ASCII</small><strong id="x2"></strong></div><div><small>16-bit Unicode</small><strong id="x3"></strong></div></div>
    <div class="verdict" id="xv"></div></div>

  <h2>Lab 2 · Walk along the code table</h2>
  <p>Drag to move along the printable ASCII codes. Notice that the codes run in order and that upper case is 32 below lower case.</p>
  <div class="card"><div class="grid2"><div><div id="cs"></div>
    <div class="readout"><div><small>Character</small><strong id="k1"></strong></div><div><small>Denary / hex</small><strong id="k2"></strong></div><div><small>7-bit binary</small><strong id="k3"></strong></div></div>
    <div class="verdict" id="kv"></div></div>
    <div><svg id="kS" viewBox="0 0 420 200" role="img" aria-label="The character and its bits"></svg></div></div></div>

  <h2>Lab 3 · How big is the text file?</h2>
  <p>Choose a character set and the number of characters. The size follows from characters × bits per character.</p>
  <div class="card"><div class="grid2"><div><div id="fb" class="btnrow"></div><div id="fs"></div>
    <div class="readout"><div><small>Bits</small><strong id="f1"></strong></div><div><small>Bytes</small><strong id="f2"></strong></div><div><small>Kibibytes</small><strong id="f3"></strong></div></div>
    <div class="verdict" id="fv"></div></div>
    <div><svg id="fS" viewBox="0 0 420 200" role="img" aria-label="Bars comparing file size in three character sets"></svg></div></div></div>
'''

practise = '''
  <h2>1 · Which character set does each statement describe?</h2><div id="cl1" class="card"></div>
  <h2>2 · Similarity or difference?</h2><div id="cl2" class="card"></div>
  <h2>3 · Put the steps for storing a word in order</h2><div id="o1" class="card"></div>
  <h2>4 · Match the term to its meaning</h2><div id="m1" class="card"></div>
  <h2>5 · Calculations</h2><div id="c1"></div>
  <h2>6 · Multiple choice</h2><div id="qz1"></div>
'''

real = RWNOTE + (
rw("Text messages that cost more", "A standard text message was designed around a small character set, with room for 160 characters. A message that includes a character outside that set, such as an emoji, switches to a 16-bit encoding and the limit falls to 70 characters.", "a bigger code per character means fewer characters in the same space: the cost of Unicode.") +
rw("Garbled characters on a web page", "A page saved with one character set and opened with another shows strange symbols where accents or quotes should be. Browsers are told which set to use so every code is read the way it was written.", "the sender and receiver must use the same character set, or the same bits show different characters.") +
rw("One page, many languages", "A single Unicode document can show English, Arabic and Japanese side by side, because each character in all three has its own code. An 8-bit set cannot hold all of them.", "an advantage of Unicode over ASCII: a much wider range of characters and languages.") +
rw("Emojis", "Every emoji is a Unicode character with its own code, written in hexadecimal. Different phones draw the picture differently, but they send the same code.", "Unicode includes symbols and emojis; ASCII does not.") +
rw("Why ASCII is still everywhere", "The first 128 Unicode codes match ASCII, so a plain English text file saved in ASCII is also valid Unicode. Programming languages, email headers and many protocols still rely on that.", "ASCII is a subset of Unicode, so it is compatible.")
)

items = [("s21_12", "6", 6), ("w22_11", "1(c)", 3), ("s24_13", "1(d)", 3), ("s26_11", "1(a)(ii)", 3), ("s22_13", "1(a)", 5), ("s25_11", "3(b)(i)-(iii)", 4), ("s25_13", "1(c)(i)", 2)]

exam = aexam("character sets",
  "Seven questions from the 2021 to 2026 Paper 1 papers. The marks are for precise comparisons (both sides, with a number where one exists) and for showing that each character has its own code stored in order. The words and figures here are changed from the originals.",
  items, [
  ceq(AP("s21_12", "6"), "[6]", "A computer uses the ASCII character set. (a) State the number of characters that can be represented by ASCII and by extended ASCII. (b) Explain how the word 'TREE' is represented by ASCII. (c) The Unicode value for the character '3' is denary 51. Write the hexadecimal value for '3', and the denary value for the character '8'.",
      ["ASCII 128 (2 to the power 7) and extended ASCII 256 (2 to the power 8).", "Each character has its own unique code, each letter is replaced by its code, and the codes are stored in the order of the letters.", "Hexadecimal 33, and denary 56."],
      "<p>(c) 51 = 3 × 16 + 3, so 33. Characters are in order, so '8' is five above '3': 56.</p>",
      [[("k", "ASCII can represent 128 characters and extended ASCII 256. "), ("a", "T, R, E and E each have a unique code (84, 82, 69, 69). Each letter is replaced by its code and the codes are stored in sequence, in the same order as the letters in 'TREE'. '3' is 33 in hexadecimal, and '8' is 56.")]]) +
  ceq(AP("w22_11", "1(c)"), "[3]", "Give one similarity and two differences between the ASCII and Unicode character sets.",
      ["One similarity: both give each character a unique code, or both can use 8 bits, or Unicode includes all ASCII characters.", "Two differences, each with both sides: Unicode uses more bits per character (up to 32) whereas ASCII uses 7 or 8; Unicode represents a wider range of characters and languages whereas ASCII represents one language."],
      "<p>One of each. Put both sets in every difference.</p>",
      [[("k", "Similarity: both represent each character with its own unique binary code. Difference 1: Unicode can use up to 32 bits per character whereas ASCII uses 7 or 8. Difference 2: Unicode can represent many languages and symbols whereas ASCII represents mainly English characters.")]]) +
  ceq(AP("s24_13", "1(d)"), "[3]", "(i) State the number of bits each character set allocates to each character: ASCII, extended ASCII, Unicode. (ii) Explain how the word 'Plane' is represented by a character set.",
      ["ASCII 7, extended ASCII 8, Unicode 16 or 32 (accept up to 32). One mark if all three are right.", "Each character has a unique binary code, and the codes are stored in sequence."],
      "<p>Part (ii) is two marks: the unique code for each character, and the order. A list of the five codes is a good example.</p>",
      [[("k", "ASCII 7 bits, extended ASCII 8 bits, Unicode 16 or 32 bits. "), ("a", "'Plane' has five characters. Each has a unique binary code (P is 80, l is 108, a is 97, n is 110, e is 101) and the five codes are stored in sequence.")]]) +
  ceq(AP("s26_11", "1(a)(ii)"), "[3]", "Identify one other character set and explain how it is different from Unicode.",
      ["One mark for a valid set: ASCII, extended ASCII, or another valid character set.", "Up to two marks for differences: fewer bits per character, fewer different characters, usually one language only."],
      "<p>Name it, then give two differences with Unicode on one side: ASCII uses 7 bits whereas Unicode uses more; ASCII represents fewer characters.</p>",
      [[("k", "ASCII. It uses 7 bits per character whereas Unicode uses up to 32. ASCII can represent only 128 characters, mostly English, whereas Unicode can represent characters from many languages and symbols.")]]) +
  ceq(AP("s22_13", "1(a)"), "[5]", "(i) Describe what is meant by a character set. (ii) Identify two character sets and state one difference between them.",
      ["Character set: all the characters the computer can use or represent, with each character given a unique number or binary code.", "Two sets named, for example ASCII and Unicode, and one difference such as 7 against 16 bits or 128 against more characters."],
      "<p>(i) Two points: the characters available, and a unique code for each. (ii) Name two, then compare them.</p>",
      [[("k", "A character set is the set of all characters a computer can represent, where each character is given its own unique binary code. ASCII and extended ASCII are two character sets: ASCII uses 7 bits per character whereas extended ASCII uses 8.")]]) +
  ceq(AP("s25_11", "3(b)(i)-(iii)"), "[4]", "Text is stored using Unicode. (i) Give two advantages of Unicode instead of ASCII. (ii) A Unicode character has the binary value 0010 0111 0110 1111. Convert it into denary. (iii) A Unicode character has the hexadecimal value 2141. Convert it into denary.",
      ["Any two: a wider range of characters, so characters from more languages; symbols such as emojis.", "10 095.", "8513."],
      "<p>(ii) Group into hex first: 0010 0111 0110 1111 = 276F = 2 × 4096 + 7 × 256 + 6 × 16 + 15. (iii) 2141 = 2 × 4096 + 1 × 256 + 4 × 16 + 1.</p>",
      [[("k", "(i) A wider range of characters can be represented, so characters from more languages, and symbols such as emojis. (ii) 0010 0111 0110 1111 is 276F in hexadecimal, which is 8192 + 1792 + 96 + 15 = 10 095. (iii) 2141 = 8192 + 256 + 64 + 1 = 8513.")]]) +
  ceq(AP("s25_13", "1(c)(i)"), "[2]", "Give two characteristics of the Unicode character set.",
      ["Any two: it uses 8, 16 or 32 bits per character, up to 2 to the power of those bits different characters, it represents every language and characters such as emojis."],
      "<p>Characteristics are facts about the set: number of bits, range of characters.</p>",
      [[("k", "Each character is stored using 16 or 32 bits, so a very large number of different characters can be represented, including every language and symbols such as emojis.")]])
])

tips = tips_html([
  ("Give the numbers.", "ASCII is 7 bits and 128 characters, extended ASCII is 8 bits and 256 characters, Unicode is 16 or 32 bits."),
  ("Both sides in a difference.", "'Unicode uses more bits' is half an answer. Add 'than ASCII, which uses 7 or 8'."),
  ("Code, then order.", "For 'how is a word represented', say each character has a unique code and the codes are stored in sequence."),
  ("Count along the table.", "Given one code, others follow in order: A, B, C are 65, 66, 67 and a is 32 higher than A."),
  ("Digit characters are not numbers.", "The character '1' is code 49, not the value 1."),
  ("Advantage plus cost.", "Unicode: more characters and languages, but more storage per character."),
], [
  ("how a word is stored", "Each character is replaced by its unique binary code and the codes are stored in sequence, in the same order as the characters."),
  ("an advantage of Unicode", "A much wider range of characters can be represented, so many languages and symbols such as emojis can be used."),
  ("a drawback of Unicode", "Each character needs more bits, so a text file takes more storage than the same text in ASCII."),
  ("a similarity", "Both character sets give each character its own unique binary code."),
], [("State", "A short fact such as the number of bits."), ("Identify", "Name the character set or value asked for."), ("Describe", "Say what is stored and in what order."), ("Explain", "Give the reasons: why it is stored this way."), ("Give", "Recall a fact or example from memory.")]) + FC

js = AKJS + r'''
const CODE = (c) => c.codePointAt(0);
(function () {
  const w = "Clock", cs = w.split("");
  const draw = (s) => {
    let o = "";
    cs.forEach((c, i) => {
      const v = clamp01(s.k - i), x = 40 + i * 140;
      o += boxRow([{ t: c, c: "f1", v: 1 }], x + 30, 24, 60, 50, 0, { fs: 26 });
      if (v > 0) {
        o += SV.line(x + 60, 78, x + 60, 100, "dash", op(v)) + SV.text(x + 60, 118, CODE(c), "lbl bd t3", { "text-anchor": "middle", style: "font-size:22px", ...op(v) });
        o += SV.text(x + 60, 146, bin(CODE(c), 7), "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:17px", ...op(v) });
      }
    });
    const f = clamp01(s.f);
    if (f > 0) o += SV.text(380, 196, cs.map((c) => bin(CODE(c), 7)).join(" "), "lbl bd t3", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:15px", ...op(f) });
    return o;
  };
  const steps = [{ cap: "The word <b>Clock</b> has five characters. Each one needs its own code.", s: {} }];
  cs.forEach((c, i) => steps.push({ cap: `<b>${c}</b> has the unique code <b>${CODE(c)}</b>, which is <b>${bin(CODE(c), 7)}</b> in 7 bits.`, s: { k: i + 1 } }));
  steps.push({ cap: "The five codes are stored <b>in sequence</b>, in the same order as the letters: 35 bits in 7-bit ASCII.", s: { k: 5, f: 1 } });
  Lib.stepper($("#stA"), { w: 760, h: 214, label: "Storing the word Clock as ASCII codes", base: { k: 0, f: 0 }, draw, tween: 600, dwell: 3600, steps });
})();

(function () {
  const t = "Hello", n = t.length, sets = [["7-bit ASCII", 7, "f1"], ["8-bit extended ASCII", 8, "f2"], ["16-bit Unicode", 16, "f3"]];
  const draw = (s) => {
    let o = SV.text(30, 30, "Storage for the five-character word 'Hello'", "lbl bd");
    sets.forEach((q, i) => {
      const v = clamp01(s.k - i), y = 56 + i * 56, bits = n * q[1];
      if (v > 0) o += SV.text(30, y + 14, q[0], "sm", op(v)) + SV.rect(200, y, (bits / 80) * 480 * v, 26, q[2], { rx: 6, ...op(0.7) }) + SV.text(210 + (bits / 80) * 480 * v, y + 18, bits + " bits", "lbl bd", op(v));
    });
    return o;
  };
  Lib.stepper($("#stB"), { w: 760, h: 230, label: "Bits needed for the same word in three character sets", base: { k: 0 }, draw, tween: 700, dwell: 4000, steps: [
    { cap: "The word <b>Hello</b> has 5 characters. The storage needed is characters × bits per character.", s: { k: 0 } },
    { cap: "7-bit ASCII: 5 × 7 = <b>35 bits</b>.", s: { k: 1 } },
    { cap: "8-bit extended ASCII: 5 × 8 = <b>40 bits</b>.", s: { k: 2 } },
    { cap: "16-bit Unicode: 5 × 16 = <b>80 bits</b>. More characters are available, but the same text takes more than twice the space of 7-bit ASCII.", s: { k: 3 } }] });
})();

(function () {
  const A = bin(65, 8), a = bin(97, 8);
  const draw = (s) => {
    const row = (str, y, lab, v, diff) => v > 0 ? SV.text(30, y + 30, lab, "lbl bd", op(v)) + boxRow(str.split("").map((t, i) => ({ t, c: diff && i === 2 ? "f3" : "f1", top: v > 0 ? [128, 64, 32, 16, 8, 4, 2, 1][i] : undefined, v })), 130, y, 64, 44, 16, { fs: 20 }) : "";
    let o = row(A, 36, "A = 65", 1, s.d) + row(a, 116, "a = 97", clamp01(s.k), s.d);
    if (s.d > 0.5) o += SV.text(380, 206, "Only the 32 column differs, so a = A + 32", "lbl bd t3", { "text-anchor": "middle" });
    return o;
  };
  Lib.stepper($("#stC"), { w: 760, h: 224, label: "Upper case and lower case differ by one bit", base: { k: 0, d: 0 }, draw, tween: 600, dwell: 4000, steps: [
    { cap: "The upper case letter <b>A</b> has the code 65 = 0100 0001.", s: {} },
    { cap: "The lower case letter <b>a</b> has the code 97 = 0110 0001.", s: { k: 1 } },
    { cap: "Compare the bits: only the <b>32</b> column is different. Lower case is always upper case plus 32 in ASCII.", s: { k: 1, d: 1 } }] });
})();

/* Lab 1 */
(function () {
  const inp = $("#tx");
  const paint = () => {
    const cs = [...inp.value].slice(0, 12), codes = cs.map(CODE);
    $("#txT").innerHTML = `<div class="tw"><table class="t mono"><tr><th>Character</th><th>Denary</th><th>Hex</th><th>Binary</th></tr>${cs.map((c, i) => `<tr><td>${esc(c === " " ? "(space)" : c)}</td><td>${codes[i]}</td><td>${hx(codes[i], codes[i] > 255 ? 4 : 2)}</td><td>${bin(codes[i], codes[i] > 255 ? 16 : codes[i] > 127 ? 8 : 7)}</td></tr>`).join("")}</table></div>`;
    const n = cs.length, mx = Math.max(0, ...codes);
    $("#x1").textContent = mx < 128 ? n * 7 + " bits" : "not available"; $("#x2").textContent = mx < 256 ? n * 8 + " bits" : "not available"; $("#x3").textContent = n * 16 + " bits";
    $("#xv").textContent = !n ? "Type something." : mx < 128 ? "Every character is in ASCII, so all three sets can store this text. Unicode costs more bits for the same characters." : mx < 256 ? "At least one character is outside 7-bit ASCII but inside extended ASCII." : "At least one character needs Unicode: 7-bit and 8-bit sets have no code for it.";
  };
  inp.addEventListener("input", paint); paint();
})();

/* Lab 2 */
Lib.slider($("#cs"), { id: "csl", label: "Code ", min: 32, max: 126, value: 65, fmt: (x) => x, onInput: (n) => {
  const c = String.fromCharCode(n), other = /[a-z]/.test(c) ? n - 32 : /[A-Z]/.test(c) ? n + 32 : null;
  $("#k1").textContent = n === 32 ? "(space)" : c; $("#k2").textContent = n + " / " + hx(n); $("#k3").textContent = bin(n, 7);
  $("#kv").textContent = other ? `The ${/[a-z]/.test(c) ? "upper" : "lower"} case version is ${String.fromCharCode(other)} (code ${other}). The codes differ by 32.` : /[0-9]/.test(c) ? `The digit character ${c} has the code ${n}. The number ${c} would be stored as ${bin(+c, 8)}.` : "Codes run in order along the table.";
  $("#kS").innerHTML = boxRow([{ t: n === 32 ? "␣" : c, c: "f1" }], 170, 20, 80, 70, 0, { fs: 36 }) + boxRow(bin(n, 7).split("").map((t, i) => ({ t, c: t === "1" ? "f2" : "f3", top: [64, 32, 16, 8, 4, 2, 1][i] })), 20, 130, 48, 44, 6, { fs: 18 });
} });

/* Lab 3 */
(function () {
  let bits = 7, chars = 2000;
  const sets = [["7-bit ASCII", 7], ["8-bit extended ASCII", 8], ["16-bit Unicode", 16], ["32-bit Unicode", 32]];
  const paint = () => {
    $$("#fb button").forEach((b, i) => b.classList.toggle("pri", sets[i][1] === bits));
    const tot = chars * bits;
    $("#f1").textContent = tot.toLocaleString("en-GB"); $("#f2").textContent = (tot / 8).toLocaleString("en-GB"); $("#f3").textContent = Lib.fmtN(tot / 8 / 1024, 2);
    $("#fv").textContent = `${chars.toLocaleString("en-GB")} characters × ${bits} bits = ${tot.toLocaleString("en-GB")} bits, which is ${(tot / 8).toLocaleString("en-GB")} bytes.`;
    let o = "";
    sets.forEach((s, i) => { const w = (chars * s[1]) / (chars * 32) * 300; o += SV.text(20, 36 + i * 44, s[0], "sm") + SV.rect(150, 20 + i * 44, w, 26, s[1] === bits ? "f2" : "f3", { rx: 6, ...op(0.7) }); });
    $("#fS").innerHTML = o;
  };
  $("#fb").innerHTML = sets.map((s, i) => `<button class="b" data-i="${i}">${s[0]}</button>`).join("");
  $$("#fb button").forEach((b) => (b.onclick = () => { bits = sets[+b.dataset.i][1]; paint(); }));
  Lib.slider($("#fs"), { id: "fsl", label: "Characters ", min: 100, max: 10000, step: 100, value: chars, fmt: (x) => x.toLocaleString("en-GB"), onInput: (v) => { chars = v; paint(); } });
})();
''' + CLASSIFY("cl1", "Which character set does each statement describe?", ["ASCII", "Extended ASCII", "Unicode"],
  [("Uses 7 bits per character", 0), ("Can represent 128 characters", 0), ("Uses 8 bits per character", 1), ("Can represent 256 characters", 1), ("Uses 16 or 32 bits per character", 2), ("Can show characters from many languages in one document", 2), ("Includes emojis", 2), ("Adds accented letters to the basic English set", 1)],
  "Count the bits: 7, 8, then 16 or 32.") + CLASSIFY("cl2", "Is each statement a similarity or a difference between ASCII and Unicode?", ["Similarity", "Difference"],
  [("Each character has its own unique code", 0), ("Unicode needs more bits per character", 1), ("Both are character sets", 0), ("Unicode can represent more languages", 1), ("The first 128 Unicode codes match ASCII", 0), ("A text file in Unicode is usually larger", 1)],
  "A similarity is true of both. A difference names what is different between them.") + ORDER(
  "Put the steps for storing the word 'TREE' in order.",
  ["Split the word into characters: T, R, E, E", "Look up the unique code for each character", "Write each code in binary", "Store the binary codes one after another", "Keep the same order as the letters in the word"],
  "Split, look up, convert, store, in order.") + MATCH([
  ["Character set", "All the characters a computer can use, each with a unique code"], ["ASCII", "7 bits per character, 128 characters"], ["Extended ASCII", "8 bits per character, 256 characters"], ["Unicode", "Up to 32 bits per character, a very wide range of characters"], ["Unique code", "A different binary number for each character"]]) + CALC([
  {"q": "How many different characters can 7 bits represent?", "a": 128, "unit": "", "tol": 0.01, "hint": "2^7.", "sol": "<b>128</b>."},
  {"q": "How many different characters can 8 bits represent?", "a": 256, "unit": "", "tol": 0.01, "hint": "2^8.", "sol": "<b>256</b>."},
  {"q": "In ASCII, the letter 'A' has the code 65. What is the code for 'K'?", "a": 75, "unit": "", "tol": 0.01, "hint": "K is ten letters after A.", "sol": "<b>75</b>."},
  {"q": "In ASCII, 'a' has the code 97. What is the code for 'f'?", "a": 102, "unit": "", "tol": 0.01, "hint": "f is five letters after a.", "sol": "<b>102</b>."},
  {"q": "A text file has 3000 characters in 8-bit extended ASCII. How many bytes is that?", "a": 3000, "unit": "bytes", "tol": 0.01, "hint": "8 bits = 1 byte per character.", "sol": "<b>3000</b> bytes."},
  {"q": "The same 3000 characters are stored in 16-bit Unicode. How many bytes?", "a": 6000, "unit": "bytes", "tol": 0.01, "hint": "3000 × 16 ÷ 8.", "sol": "<b>6000</b> bytes."},
  {"q": "A Unicode character has the hexadecimal value 0044. Convert it into denary.", "a": 68, "unit": "", "tol": 0.01, "hint": "4 × 16 + 4.", "sol": "<b>68</b>."},
  {"q": "The digit character '1' has the code 49. What is the code for '7'?", "a": 55, "unit": "", "tol": 0.01, "hint": "49 + 6.", "sol": "<b>55</b>."}]) + MCQ([
  ("How many bits does ASCII use for each character?", ["5", "7", "16", "32"], 1, "Standard ASCII uses 7 bits."),
  ("Which statement about Unicode is correct?", ["It can only represent English", "It has fewer characters than extended ASCII", "It can represent characters from many languages", "It always uses 8 bits"], 2, "Unicode has a very wide range of characters."),
  ("What is stored for each character in a word?", ["The word's code", "A unique binary code for the character", "Its position in the alphabet only", "The picture of the letter"], 1, "Each character has its own unique code, stored in sequence."),
  ("Why does a text file in Unicode usually take more storage than the same text in ASCII?", ["Unicode uses more characters", "Each Unicode character needs more bits", "Unicode compresses text", "ASCII uses 16 bits"], 1, "More bits per character means more bits in the file."),
  ("Which is true of both ASCII and Unicode?", ["They use the same number of bits", "Each character has a unique code", "They can show emojis", "They have exactly 128 characters"], 1, "Both are character sets mapping each character to a unique code."),
  ("In ASCII, 'A' is 65 and 'a' is 97. What does this tell you?", ["Lower case letters are earlier in the table", "The codes for upper and lower case differ by 32", "The codes are random", "Letters have no order"], 1, "97 − 65 = 32, one bit difference.")], "qz1") + CARDS([
  ("Character set", "All the characters a computer can represent, each with a unique code."), ("ASCII", "7 bits, 128 characters."), ("Extended ASCII", "8 bits, 256 characters."), ("Unicode", "16 or 32 bits (up to 32). Many languages, symbols, emojis."),
  ("Stored in sequence", "The codes are stored in the same order as the characters."), ("A to a", "Upper case + 32 = lower case."), ("Unicode advantage", "Wider range of characters and languages."), ("Unicode cost", "More bits per character, larger files.")])

build("ac113", "ac-1-1-3-character-sets", "Character Sets: ASCII, Extended ASCII and Unicode", EYA("1.1.3"),
  "What a character set is, how a word is stored as codes in sequence, ASCII against extended ASCII against Unicode, text file sizes, and seven questions from the 2021 to 2026 papers.",
  dict(sub=CBK("Chapter 1 · Information representation, section 1.1 Data representation"), **tabs(learn, watch, explore, practise, real, exam, tips)), js)
