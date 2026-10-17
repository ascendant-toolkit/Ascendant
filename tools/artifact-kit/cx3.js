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

function chainDraw(nodes, k) {
  const H = 40, G = 16; let o = "";
  nodes.forEach((t, i) => {
    const v = Math.max(0, Math.min(1, k - i)); if (v <= 0) return;
    const y = 8 + i * (H + G);
    o += SV.rect(30, y, 700, H, ["f1", "f2", "f3"][i % 3], { rx: 8, ...op(0.55 * v) }) + SV.text(380, y + 25, t, "lbl bd", { "text-anchor": "middle", ...op(v) });
    if (i > 0) o += SV.poly([[373, y - 10], [387, y - 10], [380, y - 2]], "dot4", op(v));
  });
  return o;
}
function chainStep(el, label, nodes, caps) {
  Lib.stepper($(el), { w: 760, h: 16 + nodes.length * 56, label, base: { k: 0 }, draw: (s) => chainDraw(nodes, s.k), tween: 700, dwell: 5200, steps: nodes.map((n, i) => ({ cap: caps[i], s: { k: i + 1 } })) });
}
function chooser(p, items, tmpl, lab = "Strength of the case") {
  const show = (i) => {
    const it = items[i]; $$("#" + p + "B button").forEach((b, k) => b.classList.toggle("pri", k === i));
    $("#" + p + "1").textContent = it[1]; $("#" + p + "2").textContent = it[2]; $("#" + p + "3").textContent = it[3]; $("#" + p + "v").textContent = tmpl(it);
    const w = (it[4] / 5) * 340;
    $("#" + p + "S").innerHTML = SV.text(210, 60, it[0], "lbl bd", { "text-anchor": "middle", style: "font-size:20px" }) + SV.rect(40, 100, 340, 18, "f3", { rx: 9, ...op(0.2) }) + SV.rect(40, 100, w, 18, "f1", { rx: 9, ...op(0.7) }) + SV.text(210, 146, lab + ": " + it[4] + " out of 5", "sm", { "text-anchor": "middle" });
  };
  $("#" + p + "B").innerHTML = items.map((t, i) => `<button class="b" data-i="${i}">${t[0]}</button>`).join("");
  $$("#" + p + "B button").forEach((b) => (b.onclick = () => show(+b.dataset.i)));
  show(0);
}

function pick(id, items, render) {
  const B = $("#" + id + "B"), O = $("#" + id + "O");
  B.innerHTML = items.map((t, i) => `<button class="b" data-i="${i}">${t.label}</button>`).join("");
  const show = (i) => { $$("button", B).forEach((b, k) => b.classList.toggle("pri", k === i)); O.innerHTML = render(items[i]); };
  $$("button", B).forEach((b) => (b.onclick = () => show(+b.dataset.i)));
  show(0);
}
const scoreBar = (m, max) => `<div style="background:var(--soft);border-radius:7px;height:14px;margin:6px 0 2px"><div class="bar ${m === max ? "b3" : m === 0 ? "b2" : "b4"}" style="width:${Math.max(2, (m / max) * 100)}%"></div></div><small>${m} of ${max} marks</small>`;

/* ---- flowchart builder ---- */
const FCN = [
  { t: "t", l: "START" }, { t: "p", l: "Total ← 0" }, { t: "p", l: "Count ← 1" }, { t: "i", l: "OUTPUT 'Enter a mark (0 to 100)'" }, { t: "i", l: "INPUT Mark" },
  { t: "p", l: "Total ← Total + Mark" }, { t: "p", l: "Count ← Count + 1" }, { t: "d", l: "Count > 30 ?" }, { t: "i", l: "OUTPUT 'The total is ', Total" }, { t: "t", l: "STOP" }
];
(() => { let y = 12; FCN.forEach((n) => { n.h = n.t === "d" ? 56 : 34; n.y = y; n.m = y + n.h / 2; y += n.h + 22; }); })();
const FCH = FCN[FCN.length - 1].y + 50;
function fcDraw(k) {
  let o = ""; const cx = 300;
  FCN.forEach((n, i) => {
    const v = Math.max(0, Math.min(1, k - i)); if (v <= 0) return;
    const w = n.t === "t" ? 140 : n.t === "d" ? 230 : 280, x = cx - w / 2, a = op(0.55 * v);
    if (n.t === "t") o += SV.rect(x, n.y, w, n.h, "f1", { rx: 17, ...a });
    else if (n.t === "p") o += SV.rect(x, n.y, w, n.h, "f2", { rx: 3, ...a });
    else if (n.t === "i") o += SV.poly([[x + 14, n.y], [x + w + 14, n.y], [x + w - 14, n.y + n.h], [x - 14, n.y + n.h]], "f3", a);
    else o += SV.poly([[cx, n.y], [cx + w / 2, n.m], [cx, n.y + n.h], [cx - w / 2, n.m]], "f1", a);
    o += SV.text(cx, n.m + 4, n.l, "lbl", { "text-anchor": "middle", style: "font-size:12.5px;font-family:var(--mono)", ...op(v) });
    if (i > 0) o += SV.line(cx, FCN[i - 1].y + FCN[i - 1].h, cx, n.y - 6, "ax", { "stroke-width": 2, ...op(v) }) + `<g style="opacity:${v}">${SV.arrowHead(cx, n.y, "d", "dot4")}</g>`;
    if (n.t === "d") {
      o += SV.text(cx + 8, n.y + n.h + 14, "Yes", "sm bd", op(v)) + SV.text(cx + w / 2 + 6, n.m - 6, "No", "sm bd", op(v));
      const t = FCN[3], bx = cx + 190, ty = t.m;
      o += SV.line(cx + w / 2, n.m, bx, n.m, "ax", { "stroke-width": 2, ...op(v) }) + SV.line(bx, n.m, bx, ty, "ax", { "stroke-width": 2, ...op(v) }) + SV.line(bx, ty, cx + 148, ty, "ax", { "stroke-width": 2, ...op(v) }) + `<g style="opacity:${v}">${SV.arrowHead(cx + 141, ty, "l", "dot4")}</g>`;
    }
  });
  return o;
}
Lib.stepper($("#stA"), { w: 600, h: FCH, label: "Building a flowchart for a count-controlled totalling loop", base: { k: 0 }, draw: (s) => fcDraw(s.k), tween: 500, dwell: 5000, steps: [
  { cap: "<b>Terminators.</b> The flowchart starts with a rounded box labelled START, and ends with one labelled STOP.", s: { k: 1 } },
  { cap: "<b>Initialise.</b> Set <b>Total</b> to 0 (total initialised) and <b>Count</b> to 1 (loop initialisation) before the loop. An unset total is a common slip.", s: { k: 3 } },
  { cap: "<b>Input with a prompt.</b> The prompt and the INPUT are both input/output boxes (parallelograms).", s: { k: 5 } },
  { cap: "<b>Totalling.</b> A process box adds the new mark to the total.", s: { k: 6 } },
  { cap: "<b>Loop incrementation.</b> A second process box adds 1 to the counter.", s: { k: 7 } },
  { cap: "<b>Loop termination.</b> A decision diamond asks whether the count has passed 30. <b>No</b> loops back to the prompt; <b>Yes</b> leaves the loop. Both exits are labelled.", s: { k: 8 } },
  { cap: "<b>Output with a message, and a fully correct chart.</b> After the loop, output the total with a message, then STOP. Every line has an arrow, every exit a label.", s: { k: 10 } }
] });

chainStep("#stB", "Finding four errors in a range-checking algorithm", ["Structure: REPEAT must end with UNTIL, not WHILE: line 19", "Names: INPUT Temp, but the rest uses Temperature: line 03", "Conditions: IF Temperature = 999 only runs for the stop value: should be <> : line 04", "Operators: >= 35.0 OR <= 38.0 is true for every number: should be AND: line 14"], [
  "<b>Structure first:</b> match every opening keyword with its closing keyword.", "<b>Names:</b> compare each variable with the declarations and the other lines.", "<b>Conditions:</b> test the stopping value with a quick example.", "<b>Operators:</b> a range needs AND. Four errors, each written once, with line number and correction."]);
chainStep("#stC", "Test data for a limit of 80", ["The rule: whole numbers not greater than 80 are accepted", "80: the largest accepted value, at the limit (boundary or extreme data)", "81: the smallest rejected value, just above the limit (boundary or abnormal data)", "Write the value, accepted or rejected, and the reason for each"], [
  "<b>Read the rule</b> and find the limit.", "<b>Accepted end:</b> the limit itself.", "<b>Rejected end:</b> the next value outside it.", "<b>Marks:</b> one for each value and one for each reason."]);

/* ---- trace lab ---- */
function traceLab() {
  const A = (() => { const rows = []; [5, 6, -1].forEach((v) => { rows.push({ ln: 1, v: { Value: v } }); if (v !== -1) { let ans = v; rows[rows.length - 1].v.Answer = ans; rows[rows.length - 1].ln = 4; for (let c = v - 1; c >= 1; c--) { ans *= c; rows.push({ ln: 6, v: { Count: c, Answer: ans } }); } rows[rows.length - 1].v.OUTPUT = ans; rows[rows.length - 1].ln = 8; } }); return rows; })();
  const B = (() => { const rows = []; [34.22, 36.1, 37.4, 38.0, 999].forEach((t) => { rows.push({ ln: 1, v: { OUTPUT: "(Please enter temperature)" } }); const r = { ln: 2, v: { Temperature: t } }; if (t !== 999) r.v.OUTPUT = t > 38.0 ? "Temperature too high" : t < 35.0 ? "Temperature too low" : "Temperature normal"; rows.push(r); }); return rows; })();
  const C = (() => { const rows = [{ ln: 0, v: { Largest: 0 } }]; let big = 0; [7, 3, 9, 4, 8].forEach((n, i) => { const r = { ln: 2, v: { Index: i + 1, Number: n } }; if (n > big) { big = n; r.v.Largest = n; r.ln = 5; } rows.push(r); }); rows.push({ ln: 8, v: { OUTPUT: big } }); return rows; })();
  const T = [
    { label: "Product of descending numbers", cols: ["Value", "Count", "Answer", "OUTPUT"], rows: A, note: "Input 5, 6, −1, 20, 9, 4. After −1 the algorithm stops, so 20, 9 and 4 are never read.",
      code: ["REPEAT", "    INPUT Value", "    IF Value <> -1", "      THEN", "        Answer ← Value", "        FOR Count ← Value - 1 TO 1 STEP -1", "            Answer ← Answer * Count", "        NEXT Count", "        OUTPUT Answer", "    ENDIF", "UNTIL Value = -1"] },
    { label: "Temperature check", cols: ["Temperature", "OUTPUT"], rows: B, note: "Input 34.22, 36.1, 37.4, 38.0, 999, −1. The prompt is recorded as an output; the −1 after 999 is never read.",
      code: ["REPEAT", "    OUTPUT \"Please enter temperature \"", "    INPUT Temperature", "    IF Temperature <> 999", "      THEN", "        IF Temperature > 38.0", "          THEN OUTPUT \"Temperature too high\"", "        ENDIF", "        IF Temperature < 35.0", "          THEN OUTPUT \"Temperature too low\"", "        ENDIF", "        IF Temperature >= 35.0 AND Temperature <= 38.0", "          THEN OUTPUT \"Temperature normal\"", "        ENDIF", "    ENDIF", "UNTIL Temperature = 999"] },
    { label: "Largest of five numbers", cols: ["Largest", "Index", "Number", "OUTPUT"], rows: C, note: "Input 7, 3, 9, 4, 8. Largest is initialised to 0 before the loop, which is why the first row is there.",
      code: ["Largest ← 0", "FOR Index ← 1 TO 5", "    INPUT Number", "    IF Number > Largest", "      THEN", "        Largest ← Number", "    ENDIF", "NEXT Index", "OUTPUT Largest"] }
  ];
  const B_ = $("#trB"), O = $("#trO");
  let cur = 0, k = 0;
  const draw = () => {
    const t = T[cur], shown = t.rows.slice(0, k);
    $$(".ln", O).forEach((l) => l.classList.remove("on"));
    if (k > 0) { const l = $(`.ln[data-k="${t.rows[k - 1].ln}"]`, O); l && l.classList.add("on"); }
    $("#trT", O).innerHTML = `<tr>${t.cols.map((c) => `<th>${c}</th>`).join("")}</tr>` + shown.map((r) => `<tr>${t.cols.map((c) => `<td>${r.v[c] === undefined ? "" : r.v[c]}</td>`).join("")}</tr>`).join("");
    $("#trV", O).textContent = k === 0 ? "Press Next row. " + t.note : k >= t.rows.length ? "Finished: " + t.rows.length + " rows. " + t.note : "Row " + k + " of " + t.rows.length + ".";
  };
  const build = () => {
    const t = T[cur];
    O.innerHTML = `<div class="grid2"><div class="code"><pre class="cp">${t.code.map((l, i) => `<span class="ln" data-k="${i}">${esc(l)}</span>`).join("")}</pre></div><div><div class="tw"><table class="t mx" id="trT"></table></div><div class="row"><button class="b" data-a="back">◀ Back</button> <button class="b pri" data-a="next">Next row ▶</button> <button class="b" data-a="reset">↻ Reset</button></div><div class="verdict" id="trV"></div></div></div>`;
    $("[data-a=next]", O).onclick = () => { k = Math.min(T[cur].rows.length, k + 1); draw(); };
    $("[data-a=back]", O).onclick = () => { k = Math.max(0, k - 1); draw(); };
    $("[data-a=reset]", O).onclick = () => { k = 0; draw(); };
    draw();
  };
  B_.innerHTML = T.map((t, i) => `<button class="b${i ? "" : " pri"}" data-i="${i}">${t.label}</button>`).join("");
  $$("button", B_).forEach((b) => (b.onclick = () => { cur = +b.dataset.i; k = 0; $$("button", B_).forEach((x) => x.classList.toggle("pri", x === b)); build(); }));
  build();
}
traceLab();

pick("td", [
  { label: "Whole number 1 to 80", rows: [["40", "Normal", "Accepted", "A typical valid value"], ["1", "Extreme / boundary", "Accepted", "The smallest accepted value"], ["80", "Extreme / boundary", "Accepted", "The largest accepted value, at the limit"], ["0", "Boundary / abnormal", "Rejected", "The first value below the range"], ["81", "Boundary / abnormal", "Rejected", "The first value above the range"], ["\"ten\"", "Abnormal", "Rejected", "The wrong data type"]] },
  { label: "Password 8 to 20 characters", rows: [["12 characters", "Normal", "Accepted", "A typical valid length"], ["8 characters", "Extreme / boundary", "Accepted", "The shortest accepted"], ["20 characters", "Extreme / boundary", "Accepted", "The longest accepted"], ["7 characters", "Boundary / abnormal", "Rejected", "The first length that is too short"], ["21 characters", "Boundary / abnormal", "Rejected", "The first length that is too long"], ["no characters", "Abnormal", "Rejected", "Presence check: nothing entered"]] },
  { label: "Temperature 35.0 to 38.0", rows: [["36.5", "Normal", "Accepted", "A typical valid value"], ["35.0", "Extreme / boundary", "Accepted", "The lowest accepted"], ["38.0", "Extreme / boundary", "Accepted", "The highest accepted"], ["34.9", "Boundary / abnormal", "Rejected", "The first value below"], ["38.1", "Boundary / abnormal", "Rejected", "The first value above"], ["\"hot\"", "Abnormal", "Rejected", "The wrong data type"]] },
  { label: "Ribbon 1.0 to 5.0 m", rows: [["3.0", "Normal", "Accepted", "Valid length"], ["1.0", "Extreme / boundary", "Accepted", "The shortest accepted"], ["5.0", "Extreme / boundary", "Accepted", "The longest accepted"], ["0.9", "Boundary / abnormal", "Rejected", "Just below"], ["5.1", "Boundary / abnormal", "Rejected", "Just above"], ["−1", "Abnormal", "Rejected", "A negative length cannot exist"]] }
], (it) => `<div class="tw"><table class="t"><tr><th>Value</th><th>Type</th><th>Result</th><th>Reason</th></tr>${it.rows.map((r) => `<tr><td><b>${r[0]}</b></td><td>${r[1]}</td><td>${r[2]}</td><td>${r[3]}</td></tr>`).join("")}</table></div><p>For a limit, a pair of values (the last accepted and the first rejected) is boundary data. Each answer needs the value, whether it is accepted or rejected, and the reason.</p>`);

pick("fx", [
  { label: "x is greater than y", bad: "IF x is greater than y", good: "IF X > Y", why: "The syllabus says precision is required: the symbol must be used." },
  { label: "= to assign", bad: "Total = Total + 1", good: "Total ← Total + 1", why: "= tests equality; ← assigns a value." },
  { label: "PRINT", bad: "PRINT Total", good: "OUTPUT Total", why: "A pseudocode question uses the syllabus keyword OUTPUT." },
  { label: "WHILE after REPEAT", bad: "REPEAT … WHILE Mark = 99", good: "REPEAT … UNTIL Mark = 99", why: "REPEAT ends with UNTIL. WHILE starts a pre-condition loop." },
  { label: "ENDCASE for IF", bad: "IF A > B … ENDCASE", good: "IF A > B … ENDIF", why: "IF closes with ENDIF; ENDCASE closes CASE." },
  { label: "Range with OR", bad: "IF Mark >= 0 OR Mark <= 20", good: "IF Mark >= 0 AND Mark <= 20", why: "Every number is either at least 0 or at most 20, so OR accepts everything." },
  { label: "Array called Array", bad: "Array[Index] ← 5", good: "Marks[Index] ← 5", why: "The report says Array is not a meaningful identifier." },
  { label: "Loop counter as STRING", bad: "DECLARE Counter : STRING", good: "DECLARE Counter : INTEGER", why: "A FOR loop counter must be an INTEGER." },
  { label: "Swap uses wrong index", bad: "ItemList[Counter] ← Temp", good: "ItemList[Counter + 1] ← Temp", why: "The second half of a swap writes to the next element, or the first value is overwritten." }
], (it) => `<div class="grid2"><div><small>Faulty</small><p><code>${it.bad}</code></p></div><div><small>Corrected</small><p><code>${it.good}</code></p></div></div><div class="verdict">${it.why}</div>`);

pick("vv", [
  { label: "Visual check", k: "Verification", d: "The user looks at what was entered and confirms it is correct, or corrects it.", s: "A visual check means looking at the data entered to confirm it is correct or to find errors." },
  { label: "Double entry check", k: "Verification", d: "The data is entered twice and the computer compares the two copies.", s: "In a double entry check the data is entered twice and compared; if they do not match, an error has been made and re-entry is requested." },
  { label: "Range check", k: "Validation", d: "Checks that a value lies between a lowest and highest value.", s: "A range check tests that the number is between the lowest and highest acceptable values." },
  { label: "Length check", k: "Validation", d: "Checks the number of characters is allowed.", s: "A length check tests that the data has an acceptable number of characters." },
  { label: "Type check", k: "Validation", d: "Checks the data is of the right data type, such as a whole number.", s: "A type check tests that the data is the right type, for example that it is a whole number." },
  { label: "Presence check", k: "Validation", d: "Checks that something has been entered.", s: "A presence check tests that data has been entered and the field has not been left empty." },
  { label: "Format check", k: "Validation", d: "Checks the data follows a set pattern.", s: "A format check tests that the data matches a pattern, such as two letters followed by four digits." },
  { label: "Check digit", k: "Validation", d: "A digit calculated from the other digits and checked after input.", s: "A check digit is calculated from the other digits and recalculated after input; if the two differ, an error has occurred." }
], (it) => `<p><b>${it.k}</b></p><p>${it.d}</p><div class="verdict">${it.s}</div>`);
Lib.classify($("#cl1"), { prompt: "Is each check validation or verification?", buckets: [{"label": "Validation"}, {"label": "Verification"}], items: [{"text": "Range check", "b": 0}, {"text": "Double entry check", "b": 1}, {"text": "Length check", "b": 0}, {"text": "Visual check", "b": 1}, {"text": "Presence check", "b": 0}, {"text": "Type check", "b": 0}, {"text": "Format check", "b": 0}, {"text": "Check digit", "b": 0}], done: "Verification is the visual check and the double entry check. The other checks in the syllabus are validation." });
Lib.classify($("#cl2"), { prompt: "Which flowchart symbol does each step use?", buckets: [{"label": "Terminator"}, {"label": "Process"}, {"label": "Input or output"}, {"label": "Decision"}], items: [{"text": "START", "b": 0}, {"text": "STOP", "b": 0}, {"text": "Total ← Total + Number", "b": 1}, {"text": "Count ← Count + 1", "b": 1}, {"text": "INPUT Password", "b": 2}, {"text": "OUTPUT 'Accepted'", "b": 2}, {"text": "Is Length >= 8 ?", "b": 3}, {"text": "Is Count > 50 ?", "b": 3}], done: "A terminator marks the start and end; a process assigns or calculates; input/output covers prompts and messages; a decision has two exits." });
Lib.order($("#o1"), { prompt: "Put the steps for completing a trace table in order.", items: ["Write a column for each variable and one for the output", "Take the first input and write it in its column", "Follow the lines in order and write each new value in a row", "Write any output without quotation marks", "Stop when the stopping condition is met"], done: "Headings, first input, follow the lines, outputs, stop." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Normal data", "Data that should be accepted"], ["Abnormal data", "Data that should be rejected"], ["Extreme data", "The largest or smallest acceptable value"], ["Boundary data", "The largest or smallest accepted value and the matching rejected value"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "Paper 2 has 75 marks in 105 minutes. The final question is 15 marks and should take 30 minutes. How many minutes a mark for the other 60 marks?", "a": 1.25, "unit": "min", "tol": 0.01, "hint": "(105 − 30) ÷ 60.", "sol": "<b>1.25 minutes</b>."},
  {"q": "Trace: Total ← 0, then FOR Index ← 1 TO 4 with Total ← Total + Index. What is Total at the end?", "a": 10, "unit": "", "tol": 0.01, "hint": "1 + 2 + 3 + 4.", "sol": "<b>10</b>."},
  {"q": "A FOR loop runs FOR Count ← 3 TO 1 STEP -1 with Answer starting at 3 and Answer ← Answer * Count. What is Answer at the end?", "a": 18, "unit": "", "tol": 0.01, "hint": "3 × 3 × 2 × 1.", "sol": "<b>18</b>."},
  {"q": "A limit is 'whole numbers not greater than 60'. What is the smallest rejected value?", "a": 61, "unit": "", "tol": 0.01, "hint": "One above the limit.", "sol": "<b>61</b>."},
  {"q": "A flowchart scores one mark each for: terminators, loop set-up, input with prompt, total, output with message and a fully correct chart. How many marks if everything is correct except the arrows and labels?", "a": 5, "unit": "", "tol": 0.01, "hint": "The last point is the correct chart overall.", "sol": "<b>5</b> of 6 (the final mark needs correct arrows and labels)."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "A question asks for pseudocode. Which answer can earn marks?", opts: ["Python code using print", "OUTPUT with ← for assignment", "A paragraph of English", "A flowchart"], a: 1, why: "Use the syllabus pseudocode." },
  { q: "In a trace table, what should you do when the stopping value is processed?", opts: ["Carry on with the next input", "Make no further entries", "Cross out the table", "Write the stopping value twice"], a: 1, why: "Once the stopping condition has been met, no further entries should be made." },
  { q: "Which pair is boundary data for a limit of 80?", opts: ["80 and 40", "80 and 81", "0 and 1", "79 and 78"], a: 1, why: "The last accepted value and the first rejected value." },
  { q: "Which check is verification?", opts: ["Range check", "Presence check", "Double entry check", "Format check"], a: 2, why: "Visual and double entry checks are verification." },
  { q: "Why do flowchart flow lines need arrowheads?", opts: ["To look neat", "They show the direction of control", "They are decisions", "They are terminators"], a: 1, why: "Lines without arrows lose a mark." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Pseudocode", "OUTPUT, ←, ENDIF. No program code."],
  ["Initialise", "Total ← 0 before the loop."],
  ["Trace table", "Every assignment; no quotes; stop at stop."],
  ["Errors", "Structure, names, operators; line and correction."],
  ["Flowchart", "Terminator, process, input/output, decision; arrows."],
  ["Boundary data", "Last accepted and first rejected."],
  ["Verification", "Visual and double entry."],
  ["Bubble sort", "Flag, and a shrinking inner limit."],
] });
