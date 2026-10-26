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

/* memory cell: address on the left, value in the box */
function memCell(x, y, addr, val, cls = "f3", v = 1, w = 150, h = 40) {
  return SV.rect(x, y, w, h, cls, { rx: 6, ...op(v * 0.55) }) + SV.rect(x, y, w, h, "ax", { rx: 6, fill: "none", ...op(v) }) +
    SV.text(x + 10, y + h / 2 + 6, String(addr), "sm", { style: "font-family:var(--mono)", ...op(v) }) +
    SV.text(x + w - 12, y + h / 2 + 7, String(val), "lbl bd", { "text-anchor": "end", style: "font-family:var(--mono);font-size:17px", ...op(v) });
}
function regBox(x, y, name, val, cls = "f2", v = 1, w = 120, h = 46) {
  return SV.rect(x, y, w, h, cls, { rx: 8, ...op(v * 0.55) }) + SV.rect(x, y, w, h, "ax", { rx: 8, fill: "none", ...op(v) }) +
    SV.text(x + 10, y - 7, name, "sm", op(v)) + SV.text(x + w / 2, y + h / 2 + 7, String(val), "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:19px", ...op(v) });
}
/* a list of code lines; hl is the highlighted index (or -1) */
function codeList(x, y, lines, hl, v = 1, lh = 30, w = 230) {
  return lines.map((l, i) => SV.rect(x, y + i * lh, w, lh - 4, i === hl ? "cell-warn" : "cell", { rx: 4, ...op(v) }) + SV.text(x + 10, y + i * lh + 18, l, "lbl", { style: "font-family:var(--mono);font-size:14px;white-space:pre", ...op(v) })).join("");
}

(function () {
  const recs = [4090, 1203, 7731, 2650, 5112];
  const draw = (s) => {
    const k = Math.round(s.i); let o = SV.text(30, 24, "File (records in the order they arrive)", "sm");
    recs.forEach((r, i) => { o += SV.rect(30 + i * 138, 34, 124, 50, i < Math.min(k, 5) ? "f3" : "cell", { rx: 8, ...op(i < k ? 1 : 0.35) }) + SV.text(92 + i * 138, 66, String(r), "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:17px", ...op(i < k ? 1 : 0.35) }); });
    if (k >= 1 && k <= 5) o += SV.text(30, 110, "newest record is appended to the end: " + recs[k - 1], "lbl bd", { style: "font-size:14px" });
    if (k >= 6) { o += SV.text(30, 110, "Search for 2650: read 4090, 1203, 7731, then 2650", "lbl bd", { style: "font-size:14px" }); [0, 1, 2, 3].forEach((i) => (o += SV.rect(30 + i * 138, 130, 124, 8, i === 3 ? "cell-ok" : "cell-warn", { rx: 3 }))); o += SV.text(30, 166, "4 records read: no order to use, so it could not stop early", "sm"); }
    return o;
  };
  Lib.stepper($("#stA"), { w: 760, h: 190, label: "A serial file", base: { i: 0 }, draw, tween: 250, dwell: 2400, steps: [
    { cap: "A <b>serial</b> file is empty. Records are written as they arrive.", s: { i: 0 } },
    { cap: "The first record, 4090, is appended.", s: { i: 1 } },
    { cap: "1203 is appended after it. Each new record goes at the <b>end</b>, whatever its key.", s: { i: 2 } },
    { cap: "7731 is appended.", s: { i: 3 } },
    { cap: "2650 is appended.", s: { i: 4 } },
    { cap: "5112 is appended. The records are in <b>chronological</b> order, not key order.", s: { i: 5 } },
    { cap: "To find 2650 the program reads from the start, one record after another. With no key order it cannot predict where 2650 is.", s: { i: 6 } }] });
})();

(function () {
  const recs = [1203, 2650, 4090, 5112, 7731];
  const draw = (s) => {
    const k = Math.round(s.i); let o = SV.text(30, 24, "File (records in key order)", "sm");
    recs.forEach((r, i) => { o += SV.rect(30 + i * 138, 34, 124, 50, k >= 1 && i === Math.min(k, 3) - 1 ? "cell-warn" : "f3", { rx: 8 }) + SV.text(92 + i * 138, 66, String(r), "lbl bd", { "text-anchor": "middle", style: "font-family:var(--mono);font-size:17px" }); });
    if (k >= 1) o += SV.text(30, 112, "Search for 3000", "lbl bd", { style: "font-size:15px" });
    if (k >= 1) o += SV.text(30, 140, "1203 < 3000: carry on" + (k >= 2 ? "     2650 < 3000: carry on" : ""), "lbl", { style: "font-family:var(--mono);font-size:14px" });
    if (k >= 3) o += SV.text(30, 168, "4090 > 3000: the key has been passed, so 3000 is not in the file", "lbl bd t2", { style: "font-size:14px" }) + SV.text(30, 196, "stop: 3 records read (the end of the file was never reached)", "sm");
    return o;
  };
  Lib.stepper($("#stB"), { w: 760, h: 215, label: "A sequential file search that stops early", base: { i: 0 }, draw, tween: 250, dwell: 2800, steps: [
    { cap: "In a <b>sequential</b> file the records are in order of the key field.", s: { i: 0 } },
    { cap: "Search for 3000: start at the beginning. 1203 is smaller than 3000, so carry on.", s: { i: 1 } },
    { cap: "2650 is smaller too, so carry on.", s: { i: 2 } },
    { cap: "4090 is <b>greater</b> than 3000. Because the file is in key order, 3000 cannot be further on, so the search stops.", s: { i: 3 } }] });
})();

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); let o = SV.text(30, 28, "Key: 4719", "lbl bd", { style: "font-family:var(--mono);font-size:16px" });
    if (k >= 1) o += SV.text(30, 62, "Hash(4719) = 4719 MOD 11 = 6", "lbl", { style: "font-family:var(--mono);font-size:15px" });
    if (k >= 2) o += SV.text(30, 92, "go straight to location 6", "lbl bd t3", { style: "font-size:15px" });
    for (let i = 0; i < 11; i++) o += memCell(430, 14 + i * 21, i, i === 6 && k >= 3 ? "4719 Hall" : i === 2 ? "1202 Ito" : i === 9 ? "7745 Ray" : "", i === 6 && k >= 2 ? "cell-warn" : "f3", 1, 280, 19);
    if (k >= 3) o += SV.text(30, 124, "record read: 1 record accessed", "lbl bd t3", { style: "font-size:15px" });
    return o;
  };
  Lib.stepper($("#stC"), { w: 760, h: 250, label: "Direct access to a random file", base: { i: 0 }, draw, tween: 250, dwell: 2800, steps: [
    { cap: "A <b>random</b> file has locations 0 to 10. Records are not in key order; each is at an address worked out from its key.", s: { i: 0 } },
    { cap: "To find key 4719, apply the <b>hashing algorithm</b> to the key: 4719 MOD 11 = 6.", s: { i: 1 } },
    { cap: "Go <b>directly</b> to location 6.", s: { i: 2 } },
    { cap: "The record is there. Only one record was read, however large the file.", s: { i: 3 } }] });
})();

(function () {
  const idx = [[1203, 0], [2650, 1], [4090, 2], [5112, 3], [7731, 4]];
  const draw = (s) => {
    const k = Math.round(s.i); let o = SV.text(30, 24, "Index (keys and addresses)", "sm") + SV.text(360, 24, "Sequential file", "sm");
    idx.forEach((r, i) => { o += SV.rect(30, 34 + i * 38, 260, 32, k === 2 && r[0] === 5112 ? "cell-warn" : "cell", { rx: 6 }) + SV.text(44, 56 + i * 38, r[0] + "  →  address " + r[1], "lbl", { style: "font-family:var(--mono);font-size:14px" }); });
    [1203, 2650, 4090, 5112, 7731].forEach((r, i) => { o += SV.rect(360, 34 + i * 38, 200, 32, k === 3 && r === 5112 ? "cell-ok" : "f3", { rx: 6 }) + SV.text(374, 56 + i * 38, "address " + i + ":  " + r, "lbl", { style: "font-family:var(--mono);font-size:14px" }); });
    if (k >= 1) o += SV.text(590, 70, "Find 5112", "lbl bd", { style: "font-size:16px" });
    if (k >= 2) o += SV.text(590, 100, "index gives address 3", "lbl", { style: "font-size:14px" });
    if (k >= 3) o += SV.text(590, 130, "read address 3: found", "lbl bd t3", { style: "font-size:14px" });
    return o;
  };
  Lib.stepper($("#stD"), { w: 760, h: 240, label: "A sequential file with an index", base: { i: 0 }, draw, tween: 250, dwell: 2800, steps: [
    { cap: "A sequential file can also be accessed <b>directly</b> if an <b>index</b> of all the key fields is kept with the address of each record.", s: { i: 0 } },
    { cap: "To find 5112, search the index (it is small and in key order).", s: { i: 1 } },
    { cap: "The index gives the address where 5112 is stored: address 3.", s: { i: 2 } },
    { cap: "Read that address directly. The records before it in the file were never read.", s: { i: 3 } }] });
})();

/* Lab 1 */
(function () {
  const keys = [4090, 1203, 7731, 2650, 5112, 8844, 3377, 6021, 9150, 1998, 7010, 2301]; let org = 0, target = 2650;
  const orgs = ["Serial", "Sequential", "Random (direct)"];
  const sorted = keys.slice().sort((a, b) => a - b);
  const ex = [2650, 9150, 3000, 1203];
  const run = () => {
    if (org === 0) { const i = keys.indexOf(target); return i >= 0 ? { n: i + 1, ok: true, why: "Records are read from the start until the key is found." } : { n: keys.length, ok: false, why: "Not in the file: every record had to be read, because a serial file has no order to stop on." }; }
    if (org === 1) { let n = 0; for (const k of sorted) { n++; if (k === target) return { n, ok: true, why: "Records are read in key order from the start until the key is found." }; if (k > target) return { n, ok: false, why: "The key was passed (" + k + " > " + target + "), so the search stopped without reading the rest." }; } return { n, ok: false, why: "End of file reached." }; }
    const i = keys.indexOf(target); return { n: 1, ok: i >= 0, why: "Hash the key, SEEK straight to the location, read one record" + (i >= 0 ? "." : ": the location is empty or holds another key, so the record is not in the file.") };
  };
  const paint = () => {
    $$("#oB button").forEach((b, i) => b.classList.toggle("pri", i === org)); $$("#oK button").forEach((b, i) => b.classList.toggle("pri", ex[i] === target));
    const L = org === 1 ? sorted : keys, r = run();
    $("#oF").innerHTML = '<div class="tw"><table class="t mono"><tr>' + L.map((k, i) => `<td style="${i < r.n && org !== 2 ? "background:var(--warn-soft);font-weight:700" : ""}">${k}</td>`).join("") + "</tr></table></div>";
    $("#o1").textContent = r.n; $("#o2").textContent = r.ok ? "found" : "not found"; $("#oV").textContent = r.why;
  };
  $("#oB").innerHTML = orgs.map((o, i) => `<button class="b" data-i="${i}">${o}</button>`).join("");
  $("#oK").innerHTML = ex.map((k) => `<button class="b">Find ${k}</button>`).join("");
  $$("#oB button").forEach((b) => (b.onclick = () => { org = +b.dataset.i; paint(); })); $$("#oK button").forEach((b, i) => (b.onclick = () => { target = ex[i]; paint(); }));
  paint();
})();

/* Lab 2 */
(function () {
  const q = [
    ["A log of every sensor reading, processed once at the end of the day", "Serial organisation, sequential access", ["Serial organisation, sequential access", "Random organisation, direct access", "Sequential organisation, direct access"], "Readings arrive in time order and everything is read in one pass."],
    ["An airline booking system fetching one seat record among millions", "Random organisation, direct access", ["Serial organisation, sequential access", "Random organisation, direct access", "Sequential organisation, sequential access"], "One record quickly: calculate its location and go there."],
    ["A bank processing every account in account-number order each night", "Sequential organisation, sequential access", ["Random organisation, direct access", "Sequential organisation, sequential access", "Serial organisation, direct access"], "Ordered records processed in a batch."],
    ["A large ordered customer file where individual customers are looked up often", "Sequential organisation, direct access with an index", ["Serial organisation, sequential access", "Sequential organisation, direct access with an index", "Random organisation, sequential access"], "An index lets an ordered file be accessed directly."]
  ]; let cur = 0, pick = null;
  const paint = () => {
    $$("#qB button").forEach((b, i) => b.classList.toggle("pri", i === cur));
    const Q = q[cur]; $("#qO").innerHTML = `<p><b>${Q[0]}</b></p><div class="btnrow">` + Q[2].map((o, i) => `<button class="b${pick === o ? " pri" : ""}" data-o="${i}">${o}</button>`).join("") + '</div><div class="verdict">' + (pick === null ? "Choose an answer." : pick === Q[1] ? "Correct. " + Q[3] : "Not the best choice. " + Q[3]) + "</div>";
    $$("#qO button").forEach((b) => (b.onclick = () => { pick = Q[2][+b.dataset.o]; paint(); }));
  };
  $("#qB").innerHTML = q.map((x, i) => `<button class="b" data-i="${i}">Situation ${i + 1}</button>`).join("");
  $$("#qB button").forEach((b) => (b.onclick = () => { cur = +b.dataset.i; pick = null; paint(); })); paint();
})();

btnTable("eB", "eO", [
  ["Serial", "Records in the order added (chronological)", "Append to the end", "Read from the start to the end; cannot stop early", "Logs, backups, batch files, temporary transaction files"],
  ["Sequential", "Records in order of a key field", "Create a new version of the file with the record inserted", "Read in key order; stop when found or the key is passed", "Ordered master files, payroll, bills, batch processing"],
  ["Random", "At an address calculated from the key using a hashing algorithm", "Store at the calculated location (handle collisions)", "Direct access: calculate the location and go there", "Databases, booking systems, operating system file management"]
], ["Organisation", "How records are stored", "Adding a record", "Finding a record", "Typical uses"]);
Lib.classify($("#cl1"), { prompt: "Which file organisation does each statement describe?", buckets: [{"label": "Serial"}, {"label": "Sequential"}, {"label": "Random"}], items: [{"text": "Records are in the order they were added", "b": 0}, {"text": "Records are ordered on a key field", "b": 1}, {"text": "The location is calculated from the key using a hash function", "b": 2}, {"text": "New records are appended to the end", "b": 0}, {"text": "A new version of the file is created to insert a record", "b": 1}, {"text": "Records can be updated directly in place", "b": 2}, {"text": "Suits a data log", "b": 0}, {"text": "Suits a booking system", "b": 2}], done: "Serial: chronological. Sequential: key order. Random: calculated location." });
Lib.classify($("#cl2"), { prompt: "Which access method is it?", buckets: [{"label": "Sequential access"}, {"label": "Direct access"}], items: [{"text": "Start at the beginning and check each record in turn", "b": 0}, {"text": "Use an index to find the address of a record", "b": 1}, {"text": "Apply a hashing algorithm to the key to find the address", "b": 1}, {"text": "Stop when the key of the current record is greater than the target", "b": 0}, {"text": "A record is found without reading the others", "b": 1}, {"text": "Check every record until the end of the file", "b": 0}], done: "Sequential: one after another from the start. Direct: straight to the record." });
Lib.order($("#o1"), { prompt: "Put the steps of a sequential search of a key-ordered file in order.", items: ["Open the file and start at the first record", "Read the next record", "If its key equals the target, the record is found", "If its key is greater than the target, stop: it is not in the file", "Otherwise go back and read the next record"], done: "Start, read, compare, stop or repeat." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Serial file", "Records stored in the order they were added"], ["Sequential file", "Records stored in order of a key field"], ["Random file", "Records stored at a location calculated from the key"], ["Direct access", "Finding a record without reading the others"], ["Index", "A list of keys with the address of each record"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "A serial file holds 1000 records. The record wanted is the 640th. How many records are read to find it?", "a": 640, "unit": "", "tol": 0.01, "hint": "Read from the start.", "sol": "<b>640</b>."},
  {"q": "A serial file holds 1000 records and the key is not in the file. How many records are read to find that out?", "a": 1000, "unit": "", "tol": 0.01, "hint": "No order to stop on.", "sol": "<b>1000</b>."},
  {"q": "A sequential file has the keys 10, 20, 30, 40, 50, 60. How many records are read when searching for 35?", "a": 4, "unit": "", "tol": 0.01, "hint": "10, 20, 30, then 40 is greater than 35.", "sol": "<b>4</b>."},
  {"q": "A sequential file has the keys 10, 20, 30, 40, 50, 60. How many records are read when searching for 60?", "a": 6, "unit": "", "tol": 0.01, "hint": "The last one.", "sol": "<b>6</b>."},
  {"q": "A random file uses Hash(Key) = Key MOD 7. At which location is key 52?", "a": 3, "unit": "", "tol": 0.01, "hint": "7 × 7 = 49, remainder 3.", "sol": "<b>3</b>."},
  {"q": "How many records are read after the hash to retrieve a record in a random file with no collision?", "a": 1, "unit": "", "tol": 0.01, "hint": "Direct access.", "sol": "<b>1</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which organisation stores records in the order they were added?", opts: ["Sequential", "Serial", "Random", "Indexed"], a: 1, why: "Serial files are chronological." },
  { q: "Which organisation orders records on a key field?", opts: ["Serial", "Sequential", "Random", "Direct"], a: 1, why: "Sequential files use a key." },
  { q: "What is needed for direct access to a sequential file?", opts: ["A hash function", "An index", "A second file", "Nothing"], a: 1, why: "An index of keys and addresses." },
  { q: "What is needed for direct access to a random file?", opts: ["An index", "A hashing algorithm", "Sorting", "Compression"], a: 1, why: "The hash gives the address." },
  { q: "A sequential search of a key-ordered file stops early when...", opts: ["the file is empty", "the current key is greater than the target", "the first record is read", "it can never stop early"], a: 1, why: "The key has been passed." },
  { q: "Which method suits a bank processing all accounts in account-number order?", opts: ["Direct access", "Sequential access", "Hashing", "Random access"], a: 1, why: "Batch processing of an ordered file." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Serial", "Records in the order added. Append to the end."],
  ["Sequential", "Records in key order. New version of the file to insert."],
  ["Random", "Location calculated from the key with a hash."],
  ["Sequential access", "From the start, one after another."],
  ["Direct access", "Straight to the record without reading the others."],
  ["Index", "Keys with addresses: direct access to a sequential file."],
  ["Stop early", "Sequential file: key exceeded."],
  ["Examples", "Serial log, sequential payroll, random bookings."],
] });
