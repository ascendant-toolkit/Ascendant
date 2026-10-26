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
const DSYM = "<div class=\"synd\"><svg viewBox=\"0 0 150 230\" style=\"width:158px;max-width:100%;display:block\" role=\"img\" aria-label=\"symbol\"><text class=\"lbl bd\" x=\"4\" y=\"14\">symbol</text><path class=\"ax\" d=\"M4,37 L34,37\"/><path class=\"ax\" style=\"fill:var(--ink)\" d=\"M34,37 L27,33.5 L27,40.5 Z\"/><path class=\"ax\" d=\"M34,37 L34,205\"/><path class=\"ax\" d=\"M104,37 L104,205\"/><rect class=\"ax\" style=\"fill:var(--surface)\" x=\"52.0\" y=\"22\" width=\"34\" height=\"30\" rx=\"15\"/><text class=\"lbl\" x=\"69.0\" y=\"42\" text-anchor=\"middle\">$</text><path class=\"ax\" d=\"M34,37 L52.0,37\"/><path class=\"ax\" style=\"fill:var(--ink)\" d=\"M52.0,37 L45.0,33.5 L45.0,40.5 Z\"/><path class=\"ax\" d=\"M86.0,37 L104,37\"/><rect class=\"ax\" style=\"fill:var(--surface)\" x=\"52.0\" y=\"64\" width=\"34\" height=\"30\" rx=\"15\"/><text class=\"lbl\" x=\"69.0\" y=\"84\" text-anchor=\"middle\">%</text><path class=\"ax\" d=\"M34,79 L52.0,79\"/><path class=\"ax\" style=\"fill:var(--ink)\" d=\"M52.0,79 L45.0,75.5 L45.0,82.5 Z\"/><path class=\"ax\" d=\"M86.0,79 L104,79\"/><rect class=\"ax\" style=\"fill:var(--surface)\" x=\"52.0\" y=\"106\" width=\"34\" height=\"30\" rx=\"15\"/><text class=\"lbl\" x=\"69.0\" y=\"126\" text-anchor=\"middle\">&</text><path class=\"ax\" d=\"M34,121 L52.0,121\"/><path class=\"ax\" style=\"fill:var(--ink)\" d=\"M52.0,121 L45.0,117.5 L45.0,124.5 Z\"/><path class=\"ax\" d=\"M86.0,121 L104,121\"/><rect class=\"ax\" style=\"fill:var(--surface)\" x=\"52.0\" y=\"148\" width=\"34\" height=\"30\" rx=\"15\"/><text class=\"lbl\" x=\"69.0\" y=\"168\" text-anchor=\"middle\">@</text><path class=\"ax\" d=\"M34,163 L52.0,163\"/><path class=\"ax\" style=\"fill:var(--ink)\" d=\"M52.0,163 L45.0,159.5 L45.0,166.5 Z\"/><path class=\"ax\" d=\"M86.0,163 L104,163\"/><rect class=\"ax\" style=\"fill:var(--surface)\" x=\"52.0\" y=\"190\" width=\"34\" height=\"30\" rx=\"15\"/><text class=\"lbl\" x=\"69.0\" y=\"210\" text-anchor=\"middle\">#</text><path class=\"ax\" d=\"M34,205 L52.0,205\"/><path class=\"ax\" style=\"fill:var(--ink)\" d=\"M52.0,205 L45.0,201.5 L45.0,208.5 Z\"/><path class=\"ax\" d=\"M86.0,205 L104,205\"/><path class=\"ax\" d=\"M104,37 L142,37\"/><path class=\"ax\" style=\"fill:var(--ink)\" d=\"M142,37 L135,33.5 L135,40.5 Z\"/></svg></div>", DNUM = "<div class=\"synd\"><svg viewBox=\"0 0 235 135\" style=\"width:247px;max-width:100%;display:block\" role=\"img\" aria-label=\"number\"><text class=\"lbl bd\" x=\"4\" y=\"14\">number</text><path class=\"ax\" d=\"M4,37 L34,37\"/><path class=\"ax\" style=\"fill:var(--ink)\" d=\"M34,37 L27,33.5 L27,40.5 Z\"/><rect class=\"ax\" style=\"fill:var(--surface)\" x=\"34\" y=\"22\" width=\"44\" height=\"30\"/><text class=\"lbl\" x=\"56.0\" y=\"42\" text-anchor=\"middle\">odd</text><path class=\"ax\" d=\"M102,37 L102,110\"/><path class=\"ax\" d=\"M189.2,37 L189.2,110\"/><path class=\"ax\" d=\"M102,37 L189.2,37\"/><path class=\"ax\" style=\"fill:var(--ink)\" d=\"M189.2,37 L182.2,33.5 L182.2,40.5 Z\"/><rect class=\"ax\" style=\"fill:var(--surface)\" x=\"123.6\" y=\"53\" width=\"44\" height=\"30\"/><text class=\"lbl\" x=\"145.6\" y=\"73\" text-anchor=\"middle\">odd</text><path class=\"ax\" d=\"M102,68 L123.6,68\"/><path class=\"ax\" style=\"fill:var(--ink)\" d=\"M123.6,68 L116.6,64.5 L116.6,71.5 Z\"/><path class=\"ax\" d=\"M167.6,68 L189.2,68\"/><rect class=\"ax\" style=\"fill:var(--surface)\" x=\"120.0\" y=\"95\" width=\"51.2\" height=\"30\"/><text class=\"lbl\" x=\"145.6\" y=\"115\" text-anchor=\"middle\">even</text><path class=\"ax\" d=\"M102,110 L120.0,110\"/><path class=\"ax\" style=\"fill:var(--ink)\" d=\"M120.0,110 L113.0,106.5 L113.0,113.5 Z\"/><path class=\"ax\" d=\"M171.2,110 L189.2,110\"/><path class=\"ax\" d=\"M78,37 L102,37\"/><path class=\"ax\" style=\"fill:var(--ink)\" d=\"M102,37 L95,33.5 L95,40.5 Z\"/><path class=\"ax\" d=\"M189.2,37 L227.2,37\"/><path class=\"ax\" style=\"fill:var(--ink)\" d=\"M227.2,37 L220.2,33.5 L220.2,40.5 Z\"/></svg></div>", DWORD = "<div class=\"synd\"><svg viewBox=\"0 0 258 104\" style=\"width:271px;max-width:100%;display:block\" role=\"img\" aria-label=\"word\"><text class=\"lbl bd\" x=\"4\" y=\"14\">word</text><path class=\"ax\" d=\"M4,37 L34,37\"/><path class=\"ax\" style=\"fill:var(--ink)\" d=\"M34,37 L27,33.5 L27,40.5 Z\"/><path class=\"ax\" d=\"M34,37 L34,79\"/><path class=\"ax\" d=\"M212.0,37 L212.0,79\"/><rect class=\"ax\" style=\"fill:var(--surface)\" x=\"89.6\" y=\"22\" width=\"66.8\" height=\"30\"/><text class=\"lbl\" x=\"123.0\" y=\"42\" text-anchor=\"middle\">letter</text><path class=\"ax\" d=\"M34,37 L89.6,37\"/><path class=\"ax\" style=\"fill:var(--ink)\" d=\"M89.6,37 L82.6,33.5 L82.6,40.5 Z\"/><path class=\"ax\" d=\"M156.39999999999998,37 L212.0,37\"/><rect class=\"ax\" style=\"fill:var(--surface)\" x=\"52.0\" y=\"64\" width=\"51.2\" height=\"30\"/><text class=\"lbl\" x=\"77.6\" y=\"84\" text-anchor=\"middle\">word</text><rect class=\"ax\" style=\"fill:var(--surface)\" x=\"127.2\" y=\"64\" width=\"66.8\" height=\"30\"/><text class=\"lbl\" x=\"160.6\" y=\"84\" text-anchor=\"middle\">letter</text><path class=\"ax\" d=\"M103.2,79 L127.2,79\"/><path class=\"ax\" style=\"fill:var(--ink)\" d=\"M127.2,79 L120.2,75.5 L120.2,82.5 Z\"/><path class=\"ax\" d=\"M34,79 L52.0,79\"/><path class=\"ax\" style=\"fill:var(--ink)\" d=\"M52.0,79 L45.0,75.5 L45.0,82.5 Z\"/><path class=\"ax\" d=\"M194.0,79 L212.0,79\"/><path class=\"ax\" d=\"M212.0,37 L250.0,37\"/><path class=\"ax\" style=\"fill:var(--ink)\" d=\"M250.0,37 L243.0,33.5 L243.0,40.5 Z\"/></svg></div>", DCODE = "<div class=\"synd\"><svg viewBox=\"0 0 455 93\" style=\"width:478px;max-width:100%;display:block\" role=\"img\" aria-label=\"code\"><text class=\"lbl bd\" x=\"4\" y=\"14\">code</text><path class=\"ax\" d=\"M4,37 L34,37\"/><path class=\"ax\" style=\"fill:var(--ink)\" d=\"M34,37 L27,33.5 L27,40.5 Z\"/><rect class=\"ax\" style=\"fill:var(--surface)\" x=\"34\" y=\"22\" width=\"66.8\" height=\"30\"/><text class=\"lbl\" x=\"67.4\" y=\"42\" text-anchor=\"middle\">letter</text><rect class=\"ax\" style=\"fill:var(--surface)\" x=\"124.8\" y=\"22\" width=\"66.8\" height=\"30\"/><text class=\"lbl\" x=\"158.2\" y=\"42\" text-anchor=\"middle\">number</text><path class=\"ax\" d=\"M100.8,37 L124.8,37\"/><path class=\"ax\" style=\"fill:var(--ink)\" d=\"M124.8,37 L117.8,33.5 L117.8,40.5 Z\"/><path class=\"ax\" d=\"M215.6,37 L215.6,68\"/><path class=\"ax\" d=\"M318.4,37 L318.4,68\"/><path class=\"ax\" d=\"M215.6,37 L318.4,37\"/><path class=\"ax\" style=\"fill:var(--ink)\" d=\"M318.4,37 L311.4,33.5 L311.4,40.5 Z\"/><rect class=\"ax\" style=\"fill:var(--surface)\" x=\"233.6\" y=\"53\" width=\"66.8\" height=\"30\"/><text class=\"lbl\" x=\"267.0\" y=\"73\" text-anchor=\"middle\">number</text><path class=\"ax\" d=\"M215.6,68 L233.6,68\"/><path class=\"ax\" style=\"fill:var(--ink)\" d=\"M233.6,68 L226.6,64.5 L226.6,71.5 Z\"/><path class=\"ax\" d=\"M300.4,68 L318.4,68\"/><path class=\"ax\" d=\"M191.6,37 L215.6,37\"/><path class=\"ax\" style=\"fill:var(--ink)\" d=\"M215.6,37 L208.6,33.5 L208.6,40.5 Z\"/><rect class=\"ax\" style=\"fill:var(--surface)\" x=\"342.4\" y=\"22\" width=\"66.8\" height=\"30\"/><text class=\"lbl\" x=\"375.79999999999995\" y=\"42\" text-anchor=\"middle\">symbol</text><path class=\"ax\" d=\"M318.4,37 L342.4,37\"/><path class=\"ax\" style=\"fill:var(--ink)\" d=\"M342.4,37 L335.4,33.5 L335.4,40.5 Z\"/><path class=\"ax\" d=\"M409.2,37 L447.2,37\"/><path class=\"ax\" style=\"fill:var(--ink)\" d=\"M447.2,37 L440.2,33.5 L440.2,40.5 Z\"/></svg></div>";

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
  const run = (str, cap0) => { const E = [["letter", /[ADPRY]/], ["digit", /[0-9]/], ["symbol", /[$%&@#]/]];
    const steps = [{ i: 0, cap: cap0 }]; let e = 0, ok = true, doneChars = [];
    for (let i = 0; i < str.length && ok; i++) { const c = str[i]; let m = -1; for (let j = e; j < 3; j++) if (E[j][1].test(c) && (j === e || doneChars.length)) { m = j; break; }
      if (m < 0) { steps.push({ i: i + 1, bad: i, cap: `<b>${c}</b>: no route allows this here. ` + (E[0][1].test(c) || E[1][1].test(c) ? "The diagram only moves forward through letters, then digits, then symbols; after a symbol no letters or digits are allowed." : "It is not one of the allowed characters.") + " The string is <b>invalid</b>." }); ok = false; break; }
      e = m; doneChars.push([c, m]); steps.push({ i: i + 1, cap: `<b>${c}</b> matches <b>${E[m][0]}</b>.` }); }
    return { steps, E }; };
  const make = (el, str, cap0) => { const { steps } = run(str, cap0), E = ["letter", "digit", "symbol"], R = [/[ADPRY]/, /[0-9]/, /[$%&@#]/];
    const assign = []; let e = 0; for (const c of str) { let m = -1; for (let j = e; j < 3; j++) if (R[j].test(c)) { m = j; break; } if (m < 0) { assign.push(-1); break; } e = m; assign.push(m); }
    const draw = (s) => { const k = Math.round(s.i); let o = SV.text(20, 22, "password", "lbl bd");
      E.forEach((n, j) => { const used = assign.slice(0, k).some((a) => a === j), cur = k > 0 && assign[k - 1] === j; o += SV.rect(30 + j * 190, 34, 130, 40, cur ? "cell-warn" : used ? "cell-ok" : "cell", { rx: 4 }) + SV.text(95 + j * 190, 59, n + " (one or more)", "lbl", { "text-anchor": "middle", style: "font-size:12px" }); if (j < 2) o += SV.path("M" + (160 + j * 190) + ",54 H" + (220 + j * 190), "ax"); });
      o += SV.text(20, 118, "string", "sm"); [...str].forEach((c, i) => { const bad = assign[i] === -1; const on = i < k; o += SV.rect(20 + i * 52, 126, 46, 40, on ? (bad ? "cell-no" : "cell-ok") : "cell", { rx: 6, ...op(on ? 1 : 0.4) }) + SV.text(43 + i * 52, 153, c, "lbl bd", { "text-anchor": "middle", style: "font-size:18px;font-family:var(--mono)" }); });
      return o; };
    Lib.stepper(el, { w: 640, h: 190, label: "Syntax diagram path", base: { i: 0 }, draw, tween: 120, dwell: 1900, steps: steps.map((x) => ({ cap: x.cap, s: { i: x.i } })) }); };
  make($("#stA"), "DPAD99$", "String <b>DPAD99$</b>: does the password diagram accept it? It needs letters, then digits, then symbols.");
  make($("#stB"), "DAD#95", "String <b>DAD#95</b>: follow it through the same diagram.");
})();
(function () {
  const steps = [["&lt;word&gt;", "Start with the rule &lt;word&gt;."], ["&lt;word&gt;&lt;letter&gt;", "Use the second alternative: &lt;word&gt; ::= &lt;word&gt;&lt;letter&gt;. One more letter will be added."], ["&lt;word&gt;&lt;letter&gt;&lt;letter&gt;", "Use the second alternative again for the &lt;word&gt;."], ["&lt;letter&gt;&lt;letter&gt;&lt;letter&gt;", "Use the first alternative: &lt;word&gt; ::= &lt;letter&gt;. This <b>ends</b> the recursion."], ["A B C", "Replace each &lt;letter&gt; with a terminal from &lt;letter&gt; ::= A | B | C. The string <b>ABC</b> is valid."]];
  const draw = (s) => { const k = Math.round(s.i); let o = SV.text(20, 22, "<word> ::= <letter> | <word><letter>", "lbl bd", { style: "font-family:var(--mono);font-size:14px" }); steps.slice(0, k + 1).forEach(([t], i) => { const txt = t.replace(/&lt;/g, "<").replace(/&gt;/g, ">"); o += SV.rect(20, 44 + i * 46, 440, 38, i === k ? "cell-warn" : "cell-ok", { rx: 6 }) + SV.text(34, 69 + i * 46, (i ? "→  " : "") + txt, "lbl", { style: "font-family:var(--mono);font-size:15px" }); }); return o; };
  Lib.stepper($("#stC"), { w: 520, h: 290, label: "Derivation", base: { i: 0 }, draw, tween: 120, dwell: 2600, steps: steps.map((x, i) => ({ cap: x[1], s: { i } })) });
})();

const GR = {
  "Password (M/J 2023)": { re: /^([ADPRY]+)([0-9]+)([$%&@#]+)$/, d: "letters A D P R Y, then digits, then symbols $ % & @ #", parts: ["letter", "digit", "symbol"], ex: "DPAD99$" },
  "Variable (M/J 2023, P32)": { re: /^([ACEGIKMOQSUWY]+)([0-9]?)$/, d: "one or more letters (A C E G I K M O Q S U W Y), then at most one digit", parts: ["letters", "optional digit"], ex: "UWY" },
  "Number (O/N 2024)": { re: /^([13579])([0-9]?)$/, d: "an odd digit, then optionally one more digit (odd or even)", parts: ["odd", "optional digit"], ex: "135" },
  "Passcode (M/J 2025)": { re: /^([ACEGJ])((?:[bdfhk]|[$@#&%]|[0-9])+)$/, d: "uppercase (A C E G J), then one or more lowercase (b d f h k), symbols or digits", parts: ["uppercase", "rest"], ex: "J%d7" }
};
(function () {
  const b = $("#vB"), inp = $("#vI"); let cur = Object.keys(GR)[0];
  const paint = () => { const g = GR[cur]; const s = inp.value; $("#vD").innerHTML = `<p><b>${cur}:</b> ${g.d}.</p>`; let r = g.re.test(s); let why = "";
    if (!r) { if (!s) why = "The string is empty."; else { const first = s[0]; if (cur.startsWith("Password") && !/[ADPRY]/.test(first)) why = "It must begin with a letter A, D, P, R or Y."; else if (cur.startsWith("Variable") && !/[ACEGIKMOQSUWY]/.test(first)) why = "It must begin with a letter from the diagram."; else if (cur.startsWith("Number") && !/[13579]/.test(first)) why = "It must begin with an odd digit."; else if (cur.startsWith("Number") && s.length > 2) why = "At most two digits are allowed."; else if (cur.startsWith("Passcode") && !/[ACEGJ]/.test(first)) why = "It must begin with an uppercase letter from the diagram."; else why = "A character is not allowed where it appears, or a required part is missing or out of order."; } }
    $("#vV").innerHTML = r ? `<b style="color:var(--good)">${s}</b> is <b>valid</b>.` : `<b style="color:var(--bad)">${s || "(empty)"}</b> is <b>invalid</b>. ${why}`;
    b.querySelectorAll("button").forEach((x) => (x.className = x.dataset.k === cur ? "on" : "")); };
  Object.keys(GR).forEach((k) => { const x = document.createElement("button"); x.textContent = k; x.dataset.k = k; x.onclick = () => { cur = k; inp.value = GR[k].ex; paint(); }; b.appendChild(x); });
  inp.oninput = paint; paint();
})();
const BN = [["Choice of symbols", "&lt;symbol&gt; ::= $ | % | &amp; | @ | #", "SYMBOL"], ["Optional digit", "&lt;number&gt; ::= &lt;odd&gt; | &lt;odd&gt;&lt;even&gt; | &lt;odd&gt;&lt;odd&gt;", "NUMBER"], ["One or more letters", "&lt;word&gt; ::= &lt;letter&gt; | &lt;word&gt;&lt;letter&gt;", "WORD"], ["Sequence", "&lt;code&gt; ::= &lt;letter&gt;&lt;number&gt;&lt;symbol&gt; | &lt;letter&gt;&lt;number&gt;&lt;number&gt;&lt;symbol&gt;", "CODE"]];
(function () {
  const DG = { SYMBOL: DSYM, NUMBER: DNUM, WORD: DWORD, CODE: DCODE }; const b = $("#bB");
  const show = (i) => { $("#bO").innerHTML = `<h3>${BN[i][0]}</h3><pre class="plain">${BN[i][1]}</pre>` + DG[BN[i][2]]; b.querySelectorAll("button").forEach((x, j) => (x.className = j === i ? "on" : "")); };
  BN.forEach((o, i) => { const x = document.createElement("button"); x.textContent = o[0]; x.onclick = () => show(i); b.appendChild(x); }); show(0);
})();
Lib.classify($("#cl1"), { prompt: "Is it a terminal or a non-terminal?", buckets: [{"label": "Terminal"}, {"label": "Non-terminal"}], items: [{"text": "$", "b": 0}, {"text": "&lt;digit&gt;", "b": 1}, {"text": "A", "b": 0}, {"text": "&lt;password&gt;", "b": 1}, {"text": "7", "b": 0}, {"text": "&lt;code&gt;", "b": 1}], done: "Terminals are the characters themselves; non-terminals are names of rules in angle brackets." });
Lib.classify($("#cl2"), { prompt: "Which BNF feature does it use?", buckets: [{"label": "Alternatives (|)"}, {"label": "Sequence"}, {"label": "Recursion"}], items: [{"text": "&lt;bit&gt; ::= 0 | 1", "b": 0}, {"text": "&lt;pair&gt; ::= &lt;letter&gt;&lt;digit&gt;", "b": 1}, {"text": "&lt;word&gt; ::= &lt;letter&gt; | &lt;word&gt;&lt;letter&gt;", "b": 2}, {"text": "&lt;sign&gt; ::= + | -", "b": 0}, {"text": "&lt;code&gt; ::= &lt;digit&gt;&lt;code&gt; | &lt;digit&gt;", "b": 2}, {"text": "&lt;id&gt; ::= &lt;letter&gt;&lt;digit&gt;&lt;digit&gt;", "b": 1}], done: "| for choices, side by side for sequence, own name for repetition." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["Rounded box", "A terminal that appears as written"], ["Rectangle", "A non-terminal: the name of another rule"], ["Loop back", "One or more repeats"], ["Bypass line", "An optional element"], ["::=", "Is defined as"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the steps for drawing a syntax diagram in order.", items: ["Write the name of the rule at the top left", "Draw the elements in order", "Add a choice where the description says or", "Add loops for repetition and bypasses for options", "Check that every line has an arrow"], done: "Name, order, choices, loops and bypasses, arrows." });
Lib.calc($("#c1"), { qs: [
  {"q": "In the password diagram (one or more letters, one or more digits, one or more symbols) what is the smallest number of characters in a valid password?", "a": 3, "unit": "", "tol": 0.01, "hint": "One of each.", "sol": "<b>3</b>."},
  {"q": "A number is an odd digit followed by an optional digit (odd or even). How many different lengths of valid number are there?", "a": 2, "unit": "", "tol": 0.01, "hint": "One or two digits.", "sol": "<b>2</b>."},
  {"q": "&lt;number&gt; ::= &lt;odd&gt; | &lt;odd&gt;&lt;even&gt; | &lt;odd&gt;&lt;odd&gt; with 5 odd digits and 5 even digits: how many one-digit numbers are valid?", "a": 5, "unit": "", "tol": 0.01, "hint": "Any odd digit.", "sol": "<b>5</b>."},
  {"q": "The same rule: how many two-digit numbers are valid (5 × (5 + 5))?", "a": 50, "unit": "", "tol": 0.01, "hint": "Odd then any digit.", "sol": "5 × 10 = <b>50</b>."},
  {"q": "How many alternatives does &lt;word&gt; ::= &lt;letter&gt; | &lt;word&gt;&lt;letter&gt; have?", "a": 2, "unit": "", "tol": 0.01, "hint": "Count the |.", "sol": "<b>2</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "What does ::= mean in BNF?", opts: ["Equals zero", "Is defined as", "Is not", "Repeat"], a: 1, why: "Is defined as." },
  { q: "How is repetition written in BNF?", opts: ["With a star", "With recursion", "With a loop symbol", "It cannot be written"], a: 1, why: "A rule that uses its own name." },
  { q: "A rectangle in a syntax diagram is:", opts: ["A terminal", "A non-terminal", "An error", "An arrow"], a: 1, why: "The name of another rule." },
  { q: "A bypass line in a syntax diagram makes an element:", opts: ["Repeat", "Optional", "Compulsory", "Invalid"], a: 1, why: "Optional." },
  { q: "Why is DAD#95 invalid for letters, digits, then symbols?", opts: ["It is too long", "The symbol comes before the digits", "It has no letters", "It has no digits"], a: 1, why: "Wrong order." },
  { q: "Which stage of compilation uses the grammar?", opts: ["Syntax analysis", "Lexical analysis", "Code generation", "Linking"], a: 0, why: "Syntax analysis." },
] });
Lib.cards($("#fc1"), { cards: [
  ["Syntax diagram", "Boxes and arrows showing allowed structure."],
  ["BNF", "Text notation: <name> ::= definition."],
  ["|", "Or: a choice between alternatives."],
  ["Recursion", "A rule that uses its own name to repeat."],
  ["Terminal", "A character that appears as written."],
  ["Non-terminal", "A named rule in angle brackets."],
  ["Loop", "One or more repeats."],
  ["Bypass", "Optional element."],
] });
