const op = (v) => ({ opacity: Math.max(0, Math.min(1, v)) });
const halo = { style: "paint-order:stroke;stroke:var(--surface);stroke-width:5px" };
const arrow = (x1, y1, x2, y2, dir, cls, v) => `<g style="opacity:${Math.max(0, Math.min(1, v))}">${SV.line(x1, y1, x2, y2, cls, { "stroke-width": 2.5 })}${SV.arrowHead(x2, y2, dir, cls === "c2" ? "dot2" : cls === "c3" ? "dot3" : cls === "c4" ? "dot4" : "dot1")}</g>`;
const axes = (x0, y0, x1, y1, xl, yl) => SV.line(x0, y0, x1, y0) + SV.line(x0, y0, x0, y1) + SV.text(x1, y0 + 26, xl, "sm", { "text-anchor": "end" }) + SV.text(x0 + 6, y1 - 6, yl, "sm");
const tag = (x, y, t, c, v = 1, a = "start") => SV.text(x, y, t, "lbl bd " + c, { "text-anchor": a, ...halo, ...op(v) });
/* click a button, show its row of results */
function btnTable(btnId, outId, rows, heads) {
  const box = $("#" + btnId), out = $("#" + outId); if (!box || !out) return;
  box.innerHTML = rows.map((r, i) => `<button class="b" data-i="${i}">${r[0]}</button>`).join("");
  const show = (i) => { const r = rows[i]; $$("button", box).forEach((b, k) => b.classList.toggle("pri", k === i)); out.innerHTML = `<div class="tw"><table class="t"><tr>${heads.map((h) => `<th>${h}</th>`).join("")}</tr><tr>${r.map((c, k) => `<td>${k ? c : "<b>" + c + "</b>"}</td>`).join("")}</tr></table></div>`; };
  $$("button", box).forEach((b) => (b.onclick = () => show(+b.dataset.i))); show(0);
}

const bin = (n, w = 8) => n.toString(2).padStart(w, "0");
const hx = (n, w = 2) => n.toString(16).toUpperCase().padStart(w, "0");
const grp4 = (s) => s.replace(/(.{4})(?=.)/g, "$1 ");
const clamp01 = (v) => Math.max(0, Math.min(1, v));
/* row of boxes: items [{t, c, v}] t text, c fill class, v opacity */
function boxRow(items, x0, y, w = 64, h = 52, gap = 10, o = {}) {
  let s = "";
  items.forEach((it, i) => {
    const x = x0 + i * (w + gap), v = it.v === undefined ? 1 : it.v;
    if (v <= 0) return;
    s += SV.rect(x, y, w, h, it.c || "f3", { rx: 8, ...op(v * (it.c ? 0.55 : 0.18)) }) + SV.rect(x, y, w, h, "ax", { rx: 8, fill: "none", ...op(v) });
    s += SV.text(x + w / 2, y + h / 2 + 8, it.t, "lbl bd", { "text-anchor": "middle", style: "font-size:" + (o.fs || 22) + "px;font-family:var(--mono)", ...op(v) });
    if (it.top !== undefined) s += SV.text(x + w / 2, y - 8, it.top, "sm", { "text-anchor": "middle", ...op(v) });
    if (it.bot !== undefined) s += SV.text(x + w / 2, y + h + 18, it.bot, "sm", { "text-anchor": "middle", ...op(v) });
  });
  return s;
}

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
Lib.classify($("#cl1"), { prompt: "Which character set does each statement describe?", buckets: [{"label": "ASCII"}, {"label": "Extended ASCII"}, {"label": "Unicode"}], items: [{"text": "Uses 7 bits per character", "b": 0}, {"text": "Can represent 128 characters", "b": 0}, {"text": "Uses 8 bits per character", "b": 1}, {"text": "Can represent 256 characters", "b": 1}, {"text": "Uses 16 or 32 bits per character", "b": 2}, {"text": "Can show characters from many languages in one document", "b": 2}, {"text": "Includes emojis", "b": 2}, {"text": "Adds accented letters to the basic English set", "b": 1}], done: "Count the bits: 7, 8, then 16 or 32." });
Lib.classify($("#cl2"), { prompt: "Is each statement a similarity or a difference between ASCII and Unicode?", buckets: [{"label": "Similarity"}, {"label": "Difference"}], items: [{"text": "Each character has its own unique code", "b": 0}, {"text": "Unicode needs more bits per character", "b": 1}, {"text": "Both are character sets", "b": 0}, {"text": "Unicode can represent more languages", "b": 1}, {"text": "The first 128 Unicode codes match ASCII", "b": 0}, {"text": "A text file in Unicode is usually larger", "b": 1}], done: "A similarity is true of both. A difference names what is different between them." });
Lib.order($("#o1"), { prompt: "Put the steps for storing the word 'TREE' in order.", items: ["Split the word into characters: T, R, E, E", "Look up the unique code for each character", "Write each code in binary", "Store the binary codes one after another", "Keep the same order as the letters in the word"], done: "Split, look up, convert, store, in order." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Character set", "All the characters a computer can use, each with a unique code"], ["ASCII", "7 bits per character, 128 characters"], ["Extended ASCII", "8 bits per character, 256 characters"], ["Unicode", "Up to 32 bits per character, a very wide range of characters"], ["Unique code", "A different binary number for each character"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "How many different characters can 7 bits represent?", "a": 128, "unit": "", "tol": 0.01, "hint": "2^7.", "sol": "<b>128</b>."},
  {"q": "How many different characters can 8 bits represent?", "a": 256, "unit": "", "tol": 0.01, "hint": "2^8.", "sol": "<b>256</b>."},
  {"q": "In ASCII, the letter 'A' has the code 65. What is the code for 'K'?", "a": 75, "unit": "", "tol": 0.01, "hint": "K is ten letters after A.", "sol": "<b>75</b>."},
  {"q": "In ASCII, 'a' has the code 97. What is the code for 'f'?", "a": 102, "unit": "", "tol": 0.01, "hint": "f is five letters after a.", "sol": "<b>102</b>."},
  {"q": "A text file has 3000 characters in 8-bit extended ASCII. How many bytes is that?", "a": 3000, "unit": "bytes", "tol": 0.01, "hint": "8 bits = 1 byte per character.", "sol": "<b>3000</b> bytes."},
  {"q": "The same 3000 characters are stored in 16-bit Unicode. How many bytes?", "a": 6000, "unit": "bytes", "tol": 0.01, "hint": "3000 × 16 ÷ 8.", "sol": "<b>6000</b> bytes."},
  {"q": "A Unicode character has the hexadecimal value 0044. Convert it into denary.", "a": 68, "unit": "", "tol": 0.01, "hint": "4 × 16 + 4.", "sol": "<b>68</b>."},
  {"q": "The digit character '1' has the code 49. What is the code for '7'?", "a": 55, "unit": "", "tol": 0.01, "hint": "49 + 6.", "sol": "<b>55</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "How many bits does ASCII use for each character?", opts: ["5", "7", "16", "32"], a: 1, why: "Standard ASCII uses 7 bits." },
  { q: "Which statement about Unicode is correct?", opts: ["It can only represent English", "It has fewer characters than extended ASCII", "It can represent characters from many languages", "It always uses 8 bits"], a: 2, why: "Unicode has a very wide range of characters." },
  { q: "What is stored for each character in a word?", opts: ["The word's code", "A unique binary code for the character", "Its position in the alphabet only", "The picture of the letter"], a: 1, why: "Each character has its own unique code, stored in sequence." },
  { q: "Why does a text file in Unicode usually take more storage than the same text in ASCII?", opts: ["Unicode uses more characters", "Each Unicode character needs more bits", "Unicode compresses text", "ASCII uses 16 bits"], a: 1, why: "More bits per character means more bits in the file." },
  { q: "Which is true of both ASCII and Unicode?", opts: ["They use the same number of bits", "Each character has a unique code", "They can show emojis", "They have exactly 128 characters"], a: 1, why: "Both are character sets mapping each character to a unique code." },
  { q: "In ASCII, 'A' is 65 and 'a' is 97. What does this tell you?", opts: ["Lower case letters are earlier in the table", "The codes for upper and lower case differ by 32", "The codes are random", "Letters have no order"], a: 1, why: "97 − 65 = 32, one bit difference." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Character set", "All the characters a computer can represent, each with a unique code."],
  ["ASCII", "7 bits, 128 characters."],
  ["Extended ASCII", "8 bits, 256 characters."],
  ["Unicode", "16 or 32 bits (up to 32). Many languages, symbols, emojis."],
  ["Stored in sequence", "The codes are stored in the same order as the characters."],
  ["A to a", "Upper case + 32 = lower case."],
  ["Unicode advantage", "Wider range of characters and languages."],
  ["Unicode cost", "More bits per character, larger files."],
] });
