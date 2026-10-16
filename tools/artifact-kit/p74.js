const GOOD = "var(--good)", BAD = "var(--bad)", ACC = "var(--accent)", MUT = "var(--muted)", WARN = "var(--warn)";
const note = (x, y, t, cls = "", anchor = "middle") => SV.text(x, y, t, "lbl bd " + cls, { "text-anchor": anchor });
const sm = (x, y, t, anchor = "middle") => SV.text(x, y, t, "sm", { "text-anchor": anchor });
const panel = (x, y, w, h, title, col, o = 1) => SV.rect(x, y, w, h, "", { rx: 12, style: `fill:var(--surface);stroke:${col};stroke-width:3`, opacity: o }) + (title ? SV.text(x + w / 2, y + 22, title, "lbl bd", { "text-anchor": "middle", style: `fill:${col}` }) : "");
const arr = (x1, y1, x2, y2, col, dash) => SV.line(x1, y1, x2, y2, "", { style: `stroke:${col};stroke-width:3;${dash ? "stroke-dasharray:7 6" : ""}` });
const chip = (x, y, w, t, col) => SV.rect(x, y, w, 26, "", { rx: 13, style: `fill:${col}` }) + SV.text(x + w / 2, y + 18, t, "lbl bd", { "text-anchor": "middle", style: "fill:#fff;font-size:12px" });
const range = (a, b) => { const r = []; for (let i = a; i <= b; i++) r.push(i); return r; };
/* select-one-per-row chooser. items: [text, correctOption] */
function chooser(el, v, opts, items, ph) {
  el.innerHTML = items.map((s) => `<div class="r" data-a="${esc(s[1])}"><span class="q">${s[0]}</span><select class="sel" aria-label="${esc(s[0].replace(/<[^>]+>/g, ""))}"><option value="">${ph || "Choose…"}</option>${opts.map((x) => `<option>${esc(x)}</option>`).join("")}</select></div>`).join("");
  v.textContent = "Choose an answer for each row.";
  $$(".r", el).forEach((r) => $("select", r).addEventListener("change", (e) => { r.classList.remove("ok", "no"); if (e.target.value) r.classList.add(e.target.value === r.dataset.a ? "ok" : "no"); v.textContent = `${$$(".r.ok", el).length} of ${$$(".r", el).length} correct. Red means a different answer fits better.`; }));
}
const VCH = ["Range check", "Length check", "Type check", "Presence check", "Format check", "Check digit", "Visual check", "Double entry check"];
/* ---------- 1. validating an age ---------- */
const AGE = [["", "", [null, null, null]], ["abc", "abc", [1, 0, null]], ["150", "150", [1, 1, 0]], ["25", "25", [1, 1, 1]]];
function ageChart(s) {
  const k = Math.round(s.k), val = ["", "abc", "150", "25"][k], res = [[null, null, null], [1, 0, null], [1, 1, 0], [1, 1, 1]][k];
  let o = panel(20, 20, 300, 150, "Enter your age", ACC) + SV.rect(50, 70, 240, 44, "", { rx: 8, style: `fill:var(--soft);stroke:${k === 3 ? GOOD : k >= 1 ? BAD : MUT};stroke-width:3` }) + SV.text(170, 99, val || "…", "lbl bd", { "text-anchor": "middle", style: "font-size:18px;font-family:var(--mono)" });
  o += sm(170, 150, k === 0 ? "The program waits for input" : k === 3 ? "Accepted" : "Rejected: try again");
  ["Presence check: not empty", "Type check: an integer", "Range check: 0 to 120"].forEach((t, i) => { const r = res[i], y = 50 + i * 60, col = r === null ? MUT : r ? GOOD : BAD;
    o += SV.rect(380, y, 350, 46, "", { rx: 10, style: `fill:var(--surface);stroke:${col};stroke-width:${r === null ? 2 : 3}` }) + SV.text(400, y + 29, t, "lbl bd", { "text-anchor": "start", style: r === null ? "fill:var(--muted)" : "" }) + SV.text(705, y + 31, r === null ? "" : r ? "✓" : "✗", "lbl bd", { "text-anchor": "middle", style: `font-size:22px;fill:${col}` }); });
  return o;
}
Lib.stepper($("#stA"), { w: 760, h: 215, label: "Validation checks on an age field", base: { k: 0 }, tween: 1, dwell: 3600, draw: ageChart, steps: [
  { cap: "A form asks for an age. The program will run <b>validation checks</b> on whatever is typed.", s: { k: 0 } },
  { cap: "The user types <b>abc</b>. It is not empty, but it is <b>not an integer</b>, so the <b>type check fails</b>. An error message is shown.", s: { k: 1 } },
  { cap: "The user types <b>150</b>. It is an integer, but it is <b>outside the range 0 to 120</b>, so the <b>range check fails</b>.", s: { k: 2 } },
  { cap: "The user types <b>25</b>. It passes the presence, type and range checks, so it is <b>accepted</b>.", s: { k: 3 } },
] });

/* ---------- 2. double entry ---------- */
function deChart(s) {
  const k = Math.round(s.k), a = "Tr0ub4dor", b = k === 0 ? "" : k === 1 ? "Tr0ub4der" : a;
  let o = panel(20, 25, 330, 110, "Enter password", ACC) + SV.text(185, 95, k >= 0 ? a : "", "lbl bd", { "text-anchor": "middle", style: "font-size:18px;font-family:var(--mono)" });
  o += panel(410, 25, 330, 110, "Enter it again", k === 0 ? MUT : k === 1 ? BAD : GOOD, k === 0 ? 0.4 : 1) + (k ? SV.text(575, 95, b, "lbl bd", { "text-anchor": "middle", style: "font-size:18px;font-family:var(--mono)" }) : "");
  o += note(380, 185, k === 0 ? "First entry stored" : k === 1 ? "The two entries are different: ask the user to try again" : "Both entries match: accepted", k === 1 ? "t2" : k === 2 ? "t3" : "t1");
  if (k === 1) o += SV.text(575, 125, "e instead of o", "sm", { "text-anchor": "middle" });
  return o;
}
Lib.stepper($("#stB"), { w: 760, h: 210, label: "Double entry verification of a password", base: { k: 0 }, tween: 1, dwell: 3600, draw: deChart, steps: [
  { cap: "The user types a new password. The program stores it and asks for it <b>again</b>.", s: { k: 0 } },
  { cap: "The second entry has a typing mistake. The program <b>compares the two entries</b>: they are different, so the user must try again.", s: { k: 1 } },
  { cap: "This time both entries are identical, so the program accepts the password. This is a <b>double entry check</b>.", s: { k: 2 } },
] });

/* ---------- 3. valid but wrong ---------- */
function vwChart(s) {
  const k = Math.round(s.k);
  let o = panel(20, 25, 220, 120, "Paper form", MUT) + SV.text(130, 100, "Age: 25", "lbl bd", { "text-anchor": "middle", style: "font-size:20px" });
  o += panel(290, 25, 220, 120, "Typed into the program", k >= 1 ? (k >= 3 ? BAD : ACC) : MUT, k >= 1 ? 1 : 0.4) + (k >= 1 ? SV.text(400, 100, "Age: 52", "lbl bd", { "text-anchor": "middle", style: "font-size:20px;font-family:var(--mono)" }) : "");
  o += panel(550, 25, 190, 120, "Validation", k >= 2 ? GOOD : MUT, k >= 2 ? 1 : 0.4) + (k >= 2 ? SV.text(645, 95, "✓ in range", "lbl bd t3", { "text-anchor": "middle", style: "font-size:16px" }) + sm(645, 118, "accepted") : "");
  if (k >= 3) o += arr(130, 145, 130, 185, BAD, 1) + arr(400, 145, 400, 185, BAD, 1) + note(265, 215, "Visual check: 25 ≠ 52. The mistake is found!", "t2");
  else o += note(380, 215, k === 0 ? "The form says 25" : k === 1 ? "A typing mistake: 52 instead of 25" : "52 is a reasonable age, so validation cannot spot the error", k === 2 ? "t4" : "t1");
  return o;
}
Lib.stepper($("#stC"), { w: 760, h: 245, label: "Data that is valid but wrong", base: { k: 0 }, tween: 1, dwell: 3800, draw: vwChart, steps: [
  { cap: "The person's real age, on the paper form, is <b>25</b>.", s: { k: 0 } },
  { cap: "The data entry clerk makes a typing mistake and enters <b>52</b>.", s: { k: 1 } },
  { cap: "<b>Validation</b> passes it: 52 is an integer in the range 0 to 120. Validation only checks data is <b>reasonable</b>, not correct.", s: { k: 2 } },
  { cap: "A <b>verification</b> check (a visual check comparing the screen with the form) spots that 52 does not match 25.", s: { k: 3 } },
] });

/* ---------- Learn code ---------- */
Lib.codePanel($("#cdVal"), { pseudo: ["REPEAT", "    INPUT Mark", "    IF Mark < 0 OR Mark > 100", "      THEN", '        OUTPUT "Mark must be 0 to 100"', "    ENDIF", "UNTIL Mark >= 0 AND Mark <= 100"], py: ["while True:", "    mark = int(input())", "    if 0 <= mark <= 100:", "        break", '    print("Mark must be 0 to 100")'] });

/* ---------- Lab 1 ---------- */
(() => {
  const C = {
    "Range check": ["Whole number from 1 to 100", (v) => { if (!/^-?\d+$/.test(v)) return [0, "not a whole number, so it cannot be in the range"]; const n = +v; return n >= 1 && n <= 100 ? [1, `${n} is between 1 and 100`] : [0, `${n} is outside 1 to 100`]; }, "Test the boundaries: 0, 1, 100, 101."],
    "Length check": ["Password of 8 to 12 characters", (v) => (v.length >= 8 && v.length <= 12 ? [1, `${v.length} characters, which is between 8 and 12`] : [0, `${v.length} characters; it must be 8 to 12`]), "Passing says nothing about whether the password is strong."],
    "Type check": ["Age must be an integer", (v) => (/^-?\d+$/.test(v.trim()) ? [1, "it is a whole number"] : [0, "it contains something other than digits"]), "\"25\" and \"250\" both pass: only the type is checked."],
    "Presence check": ["The field must not be empty", (v) => (v.trim().length ? [1, "something has been entered"] : [0, "the field is empty"]), "Any text passes, even nonsense."],
    "Format check": ["Product code: 2 capital letters then 3 digits (e.g. AB123)", (v) => (/^[A-Z]{2}\d{3}$/.test(v) ? [1, "matches the pattern LLDDD"] : [0, "does not match two capital letters followed by three digits"]), "ZZ999 passes the format check even if no such product exists."],
  };
  const sel = $("#vt"), inp = $("#vi"), rule = $("#vrule"), vv = $("#vv");
  sel.innerHTML = Object.keys(C).map((k) => `<option>${k}</option>`).join("");
  function upd() { const c = C[sel.value], r = c[1](inp.value); rule.textContent = "Rule: " + c[0]; vv.innerHTML = (r[0] ? `<span class="okf">Accepted</span> ` : `<span class="flag">Rejected</span> `) + r[1] + `.<br><span class="note">${c[2]}</span>`; }
  sel.onchange = () => { inp.value = ({ "Range check": "42", "Length check": "hello123", "Type check": "25", "Presence check": "", "Format check": "AB123" })[sel.value]; upd(); }; inp.addEventListener("input", upd); upd();
})();

/* ---------- Lab 2 ---------- */
(() => {
  const inp = $("#ci"), t = $("#ct"), v = $("#cv");
  function upd() {
    const s = inp.value.replace(/\D/g, ""); inp.value !== s && (inp.value = s);
    if (s.length < 12) { t.innerHTML = ""; v.textContent = "Type at least 12 digits."; return; }
    const d = s.slice(0, 12).split("").map(Number), w = d.map((_, i) => (i % 2 ? 3 : 1)), p = d.map((x, i) => x * w[i]), sum = p.reduce((a, b) => a + b, 0), chk = (10 - (sum % 10)) % 10;
    t.innerHTML = `<tr><th>Digit</th>${d.map((x) => `<td>${x}</td>`).join("")}</tr><tr><th>Weight</th>${w.map((x) => `<td>${x}</td>`).join("")}</tr><tr><th>Product</th>${p.map((x) => `<td>${x}</td>`).join("")}</tr>`;
    if (s.length === 12) v.innerHTML = `Total = <b>${sum}</b>. Last digit of the total is ${sum % 10}, so the check digit = (10 − ${sum % 10}) ${sum % 10 === 0 ? "gives 10, which is written as <b>0</b>" : `= <b>${chk}</b>`}. The full ISBN is <b>${s}${chk}</b>.`;
    else v.innerHTML = +s[12] === chk ? `<span class="okf">Valid</span> The calculated check digit is ${chk}, which matches the last digit.` : `<span class="flag">Invalid</span> The calculated check digit is ${chk} but the number ends in ${s[12]}. A digit was entered wrongly.`;
  }
  inp.addEventListener("input", upd); upd();
})();

/* ---------- Lab 3 ---------- */
chooser($("#sn"), $("#sv"), VCH, [
  ["Make sure the email box has not been left blank", "Presence check"], ["Check a phone number has exactly 10 digits", "Length check"], ["Check a month is from 1 to 12", "Range check"], ["Check the age field contains a number, not text", "Type check"],
  ["Check a date is typed as DD/MM/YYYY", "Format check"], ["Catch a mistyped digit in a barcode number", "Check digit"], ["Ask the user to type their new password twice", "Double entry check"], ["The user reads their typed details against the paper form", "Visual check"],
]);

/* ---------- Practise ---------- */
Lib.classify($("#cl1"), { prompt: "Is each statement about validation or verification?", buckets: [{ label: "Validation" }, { label: "Verification" }], items: [
  { text: "Checks the data is reasonable", b: 0 },
  { text: "Done automatically by the program", b: 0 },
  { text: "A range check", b: 0 },
  { text: "A presence check", b: 0 },
  { text: "A check digit", b: 0 },
  { text: "Checks the data was entered correctly", b: 1 },
  { text: "Compares what was typed with the original", b: 1 },
  { text: "Double entry check", b: 1 },
  { text: "Visual check", b: 1 },
], done: "Reasonable against matches the source." });

Lib.match($("#m1"), { prompt: "Match each check to an example.", pairs: [
  ["Range check", "Month must be from 1 to 12"],
  ["Length check", "Password must be at least 8 characters"],
  ["Type check", "Age must be a whole number"],
  ["Presence check", "The username box cannot be empty"],
  ["Format check", "A date written as DD/MM/YYYY"],
  ["Check digit", "The last digit of a barcode"]
] });

Lib.order($("#o1"), { prompt: "Put the steps of a double entry check in order.", items: [
  "The user enters the data",
  "The user enters the data a second time",
  "The program compares the two entries",
  "If they match, the data is accepted",
  "If they differ, the user is asked to enter them again"
], done: "Enter, enter again, compare, accept or retry." });

Lib.calc($("#c1"), { qs: [
  { q: "ISBN-13: the 12 digits 978030640615 give a total of 93. What is the check digit?", a: 7, sol: "Last digit of 93 is 3. 10 − 3 = 7.", hint: "10 minus the last digit of the total." },
  { q: "The first 12 digits of an ISBN-13 give a total of 80. What is the check digit?", a: 0, sol: "The last digit is 0, so 10 − 0 = 10, which is written as 0." },
  { q: "The first 12 digits of an ISBN-13 give a total of 64. What is the check digit?", a: 6, sol: "10 − 4 = 6." },
  { q: "An ISBN-13 digit 7 is multiplied by weight 3. What is the product?", a: 21, sol: "7 × 3 = 21." },
  { q: "A password must be at least 8 and at most 12 characters. How many different lengths are accepted?", a: 5, sol: "8, 9, 10, 11 and 12: 5 lengths." }
] });

Lib.quiz($("#qz1"), { qs: [
  { q: "Which check ensures a field is not left empty?", opts: ["Presence check", "Range check", "Format check", "Visual check"], a: 0, why: "A presence check." },
  { q: "Which is verification?", opts: ["Range check", "Double entry check", "Type check", "Length check"], a: 1, why: "Double entry compares two entries." },
  { q: "A user enters 150 for age. Which check would reject it (range 0 to 120)?", opts: ["Range check", "Type check", "Presence check", "Format check"], a: 0, why: "150 is outside the range." },
  { q: "Why can valid data still be wrong?", opts: ["Validation only checks it is reasonable", "Validation is random", "Verification is always wrong", "Data cannot be wrong"], a: 0, why: "52 is a valid age even if the person is 25." },
  { q: "How is a check digit used?", opts: ["It is a random number", "It is recalculated and compared when the number is entered", "It checks the length", "It encrypts the number"], a: 1, why: "The calculation is repeated and the result compared." },
  { q: "Which check compares what was typed with the source document?", opts: ["Visual check", "Format check", "Length check", "Range check"], a: 0, why: "A visual check reads the screen against the original." }
] });

Lib.cards($("#fc1"), { cards: [
  ["Validation", "An automatic check that data is reasonable and meets rules."],
  ["Verification", "A check that data was entered correctly (matches the source)."],
  ["Range check", "Checks a value is between a lowest and highest allowed value."],
  ["Length check", "Checks the data has the right number of characters."],
  ["Type check", "Checks the data is of the right data type."],
  ["Presence check", "Checks the field has not been left empty."],
  ["Format check", "Checks the data matches a set pattern."],
  ["Check digit", "A digit calculated from the other digits and added to the end of a number."],
  ["Visual check", "Reading the entered data on screen and comparing it with the original."],
  ["Double entry check", "Entering data twice and comparing the two entries."]
] });
