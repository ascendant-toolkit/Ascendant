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
  const keys = [3003, 1029, 7630], loc = [3, 4, 0];
  const draw = (s) => {
    const k = Math.round(s.i); let o = SV.text(30, 26, "Hash(Key) = Key MOD 5", "lbl bd", { style: "font-family:var(--mono);font-size:15px" });
    for (let i = 0; i < 5; i++) { const idx = loc.indexOf(i); const filled = idx >= 0 && idx < k; o += memCell(430, 20 + i * 44, i, filled ? keys[idx] : "", filled && idx === k - 1 ? "cell-warn" : "f3", 1, 280, 38); }
    if (k >= 1) o += SV.text(30, 70, keys[k - 1] + " MOD 5 = " + loc[k - 1], "lbl", { style: "font-family:var(--mono);font-size:16px" }) + SV.text(30, 100, "store at location " + loc[k - 1], "lbl bd t3", { style: "font-size:15px" });
    return o;
  };
  Lib.stepper($("#stA"), { w: 760, h: 240, label: "Storing records using MOD 5", base: { i: 0 }, draw, tween: 250, dwell: 2600, steps: [
    { cap: "The table has locations 0 to 4. The algorithm divides the key by 5 and uses the <b>remainder</b>.", s: { i: 0 } },
    { cap: "Key 3003: 3003 MOD 5 = 3, so the record is stored at location 3.", s: { i: 1 } },
    { cap: "Key 1029: 1029 MOD 5 = 4, so location 4.", s: { i: 2 } },
    { cap: "Key 7630: 7630 MOD 5 = 0, so location 0. Each key goes straight to its own address.", s: { i: 3 } }] });
})();

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); let o = SV.text(30, 26, "Hash(Key) = Key MOD 5", "lbl bd", { style: "font-family:var(--mono);font-size:15px" });
    const cells = ["7630", "", "", "3003", "1029"]; if (k >= 1) cells[1] = k >= 3 ? "1055" : cells[1];
    for (let i = 0; i < 5; i++) o += memCell(430, 20 + i * 44, i, cells[i], (k === 2 && i === 0) || (k === 3 && i === 1) ? "cell-warn" : i === 1 && k >= 3 ? "cell-ok" : "f3", 1, 280, 38);
    if (k >= 1) o += SV.text(30, 70, "New key 1055: 1055 MOD 5 = 0", "lbl", { style: "font-family:var(--mono);font-size:15px" });
    if (k >= 2) o += SV.text(30, 100, "location 0 holds 7630: COLLISION", "lbl bd t2", { style: "font-size:15px" });
    if (k >= 3) o += SV.text(30, 130, "search on linearly: location 1 is free", "lbl", { style: "font-size:15px" }) + SV.text(30, 160, "store 1055 at location 1", "lbl bd t3", { style: "font-size:15px" });
    return o;
  };
  Lib.stepper($("#stB"), { w: 760, h: 240, label: "A collision resolved by linear probing", base: { i: 0 }, draw, tween: 250, dwell: 3000, steps: [
    { cap: "Locations 0, 3 and 4 are already in use. A new record with key <b>1055</b> arrives.", s: { i: 0 } },
    { cap: "1055 MOD 5 = 0, the same hash value as the key 7630 that is already stored.", s: { i: 1 } },
    { cap: "Location 0 is occupied by a different key: a <b>collision</b>. Two records cannot share an address.", s: { i: 2 } },
    { cap: "<b>Linear probing</b>: look at the next location, 1. It is free, so 1055 is stored there.", s: { i: 3 } }] });
})();

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); let o = SV.text(30, 26, "Find key 1055", "lbl bd", { style: "font-family:var(--mono);font-size:15px" });
    const cells = ["7630", "1055", "", "3003", "1029"];
    for (let i = 0; i < 5; i++) o += memCell(430, 20 + i * 44, i, cells[i], (k >= 2 && k <= 3 && i === 0) || (k >= 3 && i === 1) ? (i === 1 && k >= 4 ? "cell-ok" : "cell-warn") : "f3", 1, 280, 38);
    if (k >= 1) o += SV.text(30, 66, "1055 MOD 5 = 0: go to location 0", "lbl", { style: "font-size:15px" });
    if (k >= 2) o += SV.text(30, 96, "key there is 7630, not 1055: no match", "lbl bd t2", { style: "font-size:15px" });
    if (k >= 3) o += SV.text(30, 126, "carry on linearly: location 1", "lbl", { style: "font-size:15px" });
    if (k >= 4) o += SV.text(30, 156, "key 1055 matches: found after 2 reads", "lbl bd t3", { style: "font-size:15px" });
    return o;
  };
  Lib.stepper($("#stC"), { w: 760, h: 240, label: "Finding a record that collided", base: { i: 0 }, draw, tween: 250, dwell: 3000, steps: [
    { cap: "The same record is looked up later.", s: { i: 0 } },
    { cap: "Calculate the hash again: <b>1055 MOD 5 = 0</b>.", s: { i: 1 } },
    { cap: "The record at location 0 has the key 7630, which does not match. The record may have been moved by a collision.", s: { i: 2 } },
    { cap: "Follow the <b>same method</b> used when it was stored: search on linearly to location 1.", s: { i: 3 } },
    { cap: "The key matches, so the record is found. If an empty location had been reached first, the record would not be in the file.", s: { i: 4 } }] });
})();

(function () {
  const draw = (s) => {
    const k = Math.round(s.i); let o = SV.text(30, 22, "Main file", "sm") + SV.text(450, 22, "Overflow area", "sm");
    const main = ["7630", "", "", "3003", "1029"];
    for (let i = 0; i < 5; i++) o += memCell(30, 30 + i * 40, i, main[i], k === 1 && i === 0 ? "cell-warn" : "f3", 1, 280, 34);
    const over = k >= 2 ? ["1055"] : []; if (k >= 3) over.push("2310");
    for (let i = 0; i < 3; i++) o += memCell(450, 30 + i * 40, "o" + i, over[i] || "", i < over.length ? "cell-ok" : "f3", 1, 260, 34);
    if (k >= 1) o += SV.text(450, 182, "keys 1055 and 2310 both hash to location 0", "sm");
    if (k >= 2) o += arrow(318, 50, 440, 50, "r", "c2", 1) ;
    return o;
  };
  Lib.stepper($("#stD"), { w: 760, h: 240, label: "An overflow area", base: { i: 0 }, draw, tween: 250, dwell: 3000, steps: [
    { cap: "Instead of searching on in the main file, a separate <b>overflow area</b> can hold the records that collide.", s: { i: 0 } },
    { cap: "Key 1055 hashes to 0, which is taken by 7630: a collision.", s: { i: 1 } },
    { cap: "1055 is stored in the next free space of the overflow area.", s: { i: 2 } },
    { cap: "Another collision with location 0 goes in the next overflow space. To find 1055 or 2310, check location 0 first, then search the overflow area linearly.", s: { i: 3 } }] });
})();

/* Lab 1 */
(function () {
  let size = 7, meth = 0, tab, over;
  const sizes = [5, 7, 11], meths = ["Linear probing", "Overflow area"];
  const reset = () => { tab = Array(size).fill(null); over = []; paint("Store some keys to see collisions."); };
  const paint = (msg) => {
    $$("#hZ button").forEach((b, i) => b.classList.toggle("pri", sizes[i] === size)); $$("#hM button").forEach((b, i) => b.classList.toggle("pri", i === meth));
    $("#hT").innerHTML = '<div class="tw"><table class="t mono"><tr><th>Location</th>' + tab.map((_, i) => `<td>${i}</td>`).join("") + "</tr><tr><th>Key</th>" + tab.map((k) => `<td>${k === null ? "" : k}</td>`).join("") + "</tr></table></div>" + (meth === 1 ? '<div class="tw"><table class="t mono"><tr><th>Overflow area</th>' + (over.length ? over.map((k) => `<td>${k}</td>`).join("") : "<td>(empty)</td>") + "</tr></table></div>" : "");
    $("#hV").textContent = msg;
  };
  const store = (key) => {
    const h = key % size;
    if (tab.includes(key) || over.includes(key)) return "Key " + key + " is already stored.";
    if (tab[h] === null) { tab[h] = key; return key + " MOD " + size + " = " + h + ": location " + h + " is free, so it is stored there."; }
    if (meth === 1) { over.push(key); return key + " MOD " + size + " = " + h + ": location " + h + " holds " + tab[h] + ". COLLISION: stored in the overflow area."; }
    for (let i = 1; i < size; i++) { const j = (h + i) % size; if (tab[j] === null) { tab[j] = key; return key + " MOD " + size + " = " + h + ": location " + h + " holds " + tab[h] + ". COLLISION: next free location is " + j + ", so it is stored there."; } }
    return "The table is full.";
  };
  const find = (key) => {
    const h = key % size; let reads = 1;
    if (tab[h] === key) return key + " MOD " + size + " = " + h + ": found at location " + h + " after 1 read.";
    if (meth === 1) { const i = over.indexOf(key); if (i >= 0) return "Location " + h + " holds a different key, so the overflow area is searched: found at overflow position " + i + " after " + (1 + i + 1) + " reads."; return "Not at location " + h + " and not in the overflow area: the record is not in the file."; }
    for (let i = 1; i < size; i++) { const j = (h + i) % size; reads++; if (tab[j] === key) return key + " hashes to " + h + " but is at location " + j + ": found after " + reads + " reads."; if (tab[j] === null) return "An empty location was reached after " + reads + " reads: the record is not in the file."; }
    return "Not found.";
  };
  $("#hZ").innerHTML = sizes.map((s) => `<button class="b">Table size ${s}</button>`).join(""); $("#hM").innerHTML = meths.map((m) => `<button class="b">${m}</button>`).join("");
  $$("#hZ button").forEach((b, i) => (b.onclick = () => { size = sizes[i]; reset(); })); $$("#hM button").forEach((b, i) => (b.onclick = () => { meth = i; reset(); }));
  $("#hS").onclick = () => { const k = parseInt($("#hK").value, 10); if (isNaN(k)) return; paint(store(k)); };
  $("#hF").onclick = () => { const k = parseInt($("#hK").value, 10); if (isNaN(k)) return; paint(find(k)); };
  $("#hR").onclick = reset; reset();
})();

/* Lab 2 */
(function () {
  let key = 1029, size = 5;
  const paint = () => { const q = Math.floor(key / size); $("#c1").textContent = key % size; $("#c2").textContent = key + " = " + size + " × " + q + " + " + (key % size); };
  Lib.slider($("#cK"), { id: "cks", label: "Key ", min: 1000, max: 9999, value: key, fmt: (x) => x, onInput: (v) => { key = v; paint(); } });
  Lib.slider($("#cZ"), { id: "czs", label: "Table size (MOD) ", min: 2, max: 13, value: size, fmt: (x) => x, onInput: (v) => { size = v; paint(); } });
  paint();
})();

btnTable("eB", "eO", [
  ["Linear probing", "Go to the next location after the hashed one, and onwards, until a free one is found; store there", "Start at the hashed location and search linearly until the key matches; an empty location means not found", "No extra area needed; clusters can form and slow searches"],
  ["Overflow area", "Store the record in the next free space of a separate overflow area", "If the hashed location holds another key, search the overflow area linearly", "Main file stays tidy; the overflow area has to be searched in order"],
  ["Chaining", "Each location refers to a chain of items; add the record to that chain", "Search the chain at the hashed location", "A location can hold many items; chains need extra space for references"]
], ["Method", "Storing a record", "Finding a record", "Notes"]);
Lib.classify($("#cl1"), { prompt: "True or false for hashing?", buckets: [{"label": "Describes hashing"}, {"label": "Does not describe hashing"}], items: [{"text": "A formula applied to the key field to give an address", "b": 0}, {"text": "The same key always gives the same address", "b": 0}, {"text": "Two keys can give the same hash value", "b": 0}, {"text": "The records are stored in key order", "b": 1}, {"text": "It is used to give direct access to a random file", "b": 0}, {"text": "It encrypts the record so it cannot be read", "b": 1}], done: "Hashing calculates an address from the key. It does not sort or encrypt." });
Lib.classify($("#cl2"), { prompt: "Is the step part of storing a record or finding a record?", buckets: [{"label": "Storing"}, {"label": "Finding"}], items: [{"text": "Calculate the hash of the key and go to that location", "b": 0}, {"text": "Write the record at the first free location after a collision", "b": 0}, {"text": "Compare the key at the location with the one searched for", "b": 1}, {"text": "Search the overflow area until the key matches", "b": 1}, {"text": "Search linearly for the next available space", "b": 0}, {"text": "An empty location means the record is not in the file", "b": 1}], done: "Storing looks for a free place. Finding looks for the matching key." });
Lib.order($("#o1"), { prompt: "Put the steps for storing a record when a collision occurs in order.", items: ["Apply the hashing algorithm to the key", "Go to the location calculated", "Find that the location is already used by another record (a collision)", "Search linearly for the next free location", "Store the record there"], done: "Hash, go, collision, search on, store." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Hashing algorithm", "A formula applied to the key to give an address"], ["Hash value", "The location calculated from a key"], ["Collision", "Two different keys giving the same hash value"], ["Linear probing", "Storing in the next free location after the hashed one"], ["Overflow area", "A separate area for records whose location is taken"]], done: "Learn these terms." });
Lib.calc($("#c1"), { qs: [
  {"q": "Hash(Key) = Key MOD 5. What is the hash value of 1029?", "a": 4, "unit": "", "tol": 0.01, "hint": "1029 = 5 × 205 + 4.", "sol": "<b>4</b>."},
  {"q": "Hash(Key) = Key MOD 3. What is the hash value of 1025?", "a": 2, "unit": "", "tol": 0.01, "hint": "1025 = 3 × 341 + 2.", "sol": "<b>2</b>."},
  {"q": "Hash(Key) = Key MOD 7. What is the hash value of 3003?", "a": 0, "unit": "", "tol": 0.01, "hint": "3003 = 7 × 429.", "sol": "<b>0</b>."},
  {"q": "Hash(Key) = Key MOD 10. What is the hash value of 7845?", "a": 5, "unit": "", "tol": 0.01, "hint": "The last digit.", "sol": "<b>5</b>."},
  {"q": "With MOD 5, keys 12 and 27 are stored. At which location is 27 stored if linear probing is used and location 2 is taken by 12?", "a": 3, "unit": "", "tol": 0.01, "hint": "27 MOD 5 = 2 (taken), so the next free location is 3.", "sol": "<b>3</b>."},
  {"q": "A table has 11 locations. What is the largest hash value that Key MOD 11 can give?", "a": 10, "unit": "", "tol": 0.01, "hint": "Remainders run 0 to 10.", "sol": "<b>10</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What is a hashing algorithm?", opts: ["A way to sort records", "A formula that calculates an address from the key field", "A kind of encryption", "A file type"], a: 1, why: "It gives the address where the record is stored or found." },
  { q: "What is a collision?", opts: ["A corrupted record", "Two different keys giving the same hash value", "A full disk", "A deleted record"], a: 1, why: "The location is already in use." },
  { q: "Which is a way to deal with a collision?", opts: ["Delete the record", "Store it in the next free location or an overflow area", "Change the key", "Sort the file"], a: 1, why: "Linear probing or an overflow area." },
  { q: "What does 3003 MOD 5 equal?", opts: ["600", "3", "5", "0"], a: 1, why: "The remainder after dividing 3003 by 5." },
  { q: "How is a record found after a collision?", opts: ["Search the whole file from the start", "Search on linearly from the hashed location (or the overflow area) until the key matches", "Calculate a new key", "It cannot be found"], a: 1, why: "Use the same method used to store it." },
  { q: "Hashing gives direct access to which file organisation?", opts: ["Serial", "Random", "Text", "None"], a: 1, why: "Random files use a hash to find the address." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Hashing algorithm", "A formula applied to the key to calculate an address."],
  ["MOD", "Remainder after integer division. Gives 0 to size - 1."],
  ["Collision", "Two keys give the same hash value; the location is used."],
  ["Linear probing", "Store in the next free location; find by searching on linearly."],
  ["Overflow area", "Separate area for colliding records; search it linearly."],
  ["Chaining", "A location holds a chain of items."],
  ["Good hash", "Fast, consistent, spreads keys evenly."],
  ["Used for", "Direct access to random files."],
] });
