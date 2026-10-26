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

/* circuit drawer: geom comes from ak15.circuit(); vals colours the wires */
function circEval(G, inp, st) {
  const v = Object.assign({}, inp); G.net.forEach(([n]) => v[n] = (st && st[n]) || 0);
  for (let k = 0; k < 8; k++) G.net.forEach(([n, t, s]) => {
    const a = s.map((x) => v[x]); let base = t, neg = false;
    if (t !== "NOT" && t[0] === "N") { base = t.slice(1); neg = true; }
    let r = base === "AND" ? a.every((x) => x) : base === "OR" ? a.some((x) => x) : base === "XOR" ? a.reduce((p, x) => p + x, 0) % 2 === 1 : !a[0];
    r = (neg ? !r : r) ? 1 : 0; v[n] = r;
  });
  return v;
}
function circInner(G, vals, opt) {
  opt = opt || {};
  const cl = (s) => (vals ? (vals[s] ? "w on" : "w off") : "w"); let o = "";
  G.wires.forEach((w) => { o += `<path class="${cl(w.s)}" d="${w.d}"/>`; if (w.dot) o += `<circle class="dot" cx="${w.dot[0]}" cy="${w.dot[1]}" r="3.2"/>`; });
  G.outs.forEach((w) => o += `<path class="${cl(w.s)}" d="${w.d}"/>`);
  G.gates.forEach((g) => { o += g.svg; if (!G.outset.includes(g.n)) o += `<text class="sm" x="${g.ox + 4}" y="${g.cy - 7}">${g.n}${vals && opt.vals ? " = " + vals[g.n] : ""}</text>`; });
  G.inputs.forEach((i) => o += `<text class="lbl bd" x="2" y="${i.y + 4}">${i.n}${vals ? " " + vals[i.n] : ""}</text>`);
  G.outs.forEach((w) => o += `<text class="lbl bd" x="${w.x + 6}" y="${w.y + 4}">${w.s}${vals ? " = " + vals[w.s] : ""}</text>`);
  return o;
}
function circFit(G, vals, W, opt) {
  const k = Math.min(2.2, (W - 20) / G.w), dx = (W - G.w * k) / 2;
  return `<g transform="translate(${dx.toFixed(1)},6) scale(${k.toFixed(3)})">` + circInner(G, vals, opt) + "</g>";
}
function circSvg(G, vals, opt) {
  return `<svg viewBox="0 0 ${G.w} ${G.h}" style="width:${Math.round(G.w * 1.2)}px;max-width:100%;display:block">` + circInner(G, vals, opt) + "</svg>";
}
/* toggle lab: one button per input, live circuit and a table of every row with the current one highlighted */
function circLab(el, G, work, outs) {
  const ins = G.in; let cur = ins.map(() => 0);
  const root = typeof el === "string" ? $(el) : el;
  root.innerHTML = '<div class="btnrow" data-b></div><div data-s></div><div data-t></div>';
  const bw = root.querySelector("[data-b]"), sw = root.querySelector("[data-s]"), tw = root.querySelector("[data-t]");
  function paint() {
    const inp = {}; ins.forEach((n, i) => inp[n] = cur[i]);
    const v = circEval(G, inp);
    sw.innerHTML = circSvg(G, v, { vals: true });
    bw.querySelectorAll("button").forEach((b, i) => { b.textContent = ins[i] + " = " + cur[i]; b.className = cur[i] ? "on" : ""; });
    const cols = ins.concat(work, outs); let h = '<div class="tw"><table class="t mono"><tr>' + cols.map((c) => `<th>${c}</th>`).join("") + "</tr>";
    for (let m = 0; m < 1 << ins.length; m++) {
      const b = ins.map((_, i) => (m >> (ins.length - 1 - i)) & 1), iv = {}; ins.forEach((n, i) => iv[n] = b[i]);
      const r = circEval(G, iv), on = b.every((x, i) => x === cur[i]);
      h += `<tr style="${on ? "background:var(--accent-soft);font-weight:700" : ""}">` + b.map((x) => `<td>${x}</td>`).join("") + work.concat(outs).map((n) => `<td>${r[n]}</td>`).join("") + "</tr>";
    }
    tw.innerHTML = h + "</table></div>";
  }
  ins.forEach((n, i) => { const b = document.createElement("button"); b.onclick = () => { cur[i] ^= 1; paint(); }; bw.appendChild(b); });
  paint();
}

/* ---- Boolean helpers (same notation and logic as the Python side) ---- */
function obJS(s) {
  const neg = (i) => { if (s[i] === "~") { const [h, j] = neg(i + 1); return ['<span class="ob">' + h + "</span>", j]; } if (s[i] === "(") { const [h, j] = seq(i + 1); return ['<span class="ob">' + h + "</span>", j + 1]; } return ['<span class="ob">' + s[i] + "</span>", i + 1]; };
  const seq = (i) => { let o = ""; while (i < s.length && s[i] !== ")") { if (s[i] === "~") { const [h, j] = neg(i + 1); o += h; i = j; } else if (s[i] === "(") { const [h, j] = seq(i + 1); o += "(" + h + ")"; i = j + 1; } else { o += s[i]; i++; } } return [o, i]; };
  return seq(0)[0];
}
const bitsOf = (m, nv) => Array.from({ length: nv }, (_, i) => (m >> (nv - 1 - i)) & 1);
function coverOf(pat, nv) { const r = []; for (let m = 0; m < 1 << nv; m++) { const b = bitsOf(m, nv); if ([...pat].every((p, i) => p === "-" || +p === b[i])) r.push(m); } return r; }
function termOf(pat, names) { const t = [...pat].map((p, i) => (p === "1" ? names[i] : p === "0" ? "~" + names[i] : "")).filter((x) => x); return t.length ? t.join(".") : "1"; }
function primeCover(mins, nv) {
  const ms = new Set(mins), pats = []; const gen = (p) => { if (p.length === nv) { pats.push(p); return; } ["0", "1", "-"].forEach((c) => gen(p + c)); }; gen("");
  const ok = pats.filter((p) => { const c = coverOf(p, nv); return c.length && c.every((m) => ms.has(m)); });
  const cv = {}; ok.forEach((p) => cv[p] = new Set(coverOf(p, nv)));
  const primes = ok.filter((p) => !ok.some((q) => q !== p && cv[q].size > cv[p].size && [...cv[p]].every((m) => cv[q].has(m))));
  let best = null;
  for (let k = 1; k <= primes.length && !best; k++) { const pick = (start, chosen) => { if (chosen.length === k) { const u = new Set(); chosen.forEach((p) => cv[p].forEach((m) => u.add(m))); if (u.size === ms.size && [...ms].every((m) => u.has(m))) { const lit = chosen.reduce((a, p) => a + [...p].filter((c) => c !== "-").length, 0); if (!best || lit < best.lit) best = { lit, chosen: chosen.slice() }; } return; } for (let i = start; i < primes.length; i++) { chosen.push(primes[i]); pick(i + 1, chosen); chosen.pop(); } }; pick(0, []); }
  return best ? best.chosen.map((p) => ({ pat: p, cells: coverOf(p, nv) })) : [];
}
function sopJS(mins, names) { if (!mins.length) return "0"; return [...mins].sort((a, b) => a - b).map((m) => termOf(bitsOf(m, names.length).join(""), names)).join(" + "); }
function simpJS(mins, names) { const nv = names.length; if (!mins.length) return "0"; if (mins.length === 1 << nv) return "1"; return primeCover(mins, nv).map((g) => termOf(g.pat, names)).join(" + "); }
const GRAYS = ["00", "01", "11", "10"], KCOL = ["var(--accent)", "var(--bad)", "var(--good)", "var(--warn)", "var(--k)", "var(--n)"];
/* K-map table as HTML; mins is the set of ones, groups a list of cell lists to ring, click a cell with data-m */
function kmapJS(mins, names, groups, clickable) {
  const nv = names.length, ms = new Set(mins);
  const cols = nv === 4 ? GRAYS : nv === 3 ? GRAYS : ["0", "1"], rows = nv === 4 ? GRAYS : nv === 3 ? ["0", "1"] : ["0", "1"];
  const corner = nv === 4 ? names[2] + names[3] + " \\ " + names[0] + names[1] : nv === 3 ? names[0] + " \\ " + names[1] + names[2] : names[1] + " \\ " + names[0];
  let h = '<div class="tw"><table class="km"><tr><th>' + corner + "</th>" + cols.map((c) => "<th>" + c + "</th>").join("") + "</tr>";
  rows.forEach((r) => { h += "<tr><th>" + r + "</th>"; cols.forEach((c) => { const m = parseInt(nv === 3 ? r + c : c + r, 2); const gi = (groups || []).map((g, k) => (g.includes(m) ? k : -1)).filter((k) => k >= 0); const sh = gi.map((k, j) => "inset 0 0 0 " + (3 + 3 * j) + "px " + KCOL[k % 6]).join(","); h += '<td data-m="' + m + '"' + (sh ? ' style="box-shadow:' + sh + '"' : "") + (clickable ? ' class="clk"' : "") + '><span class="v">' + (ms.has(m) ? 1 : 0) + '</span><span class="n">' + m + "</span></td>"; }); h += "</tr>"; });
  return h + "</table></div>";
}
function kgroupsJS(mins, names) {
  const nv = names.length, cov = (mins.length && mins.length < 1 << nv) ? primeCover(mins, nv) : [];
  const leg = cov.map((g, i) => '<span class="kg" style="--c:' + KCOL[i % 6] + '">' + obJS(termOf(g.pat, names)) + "</span>").join(" ");
  return kmapJS(mins, names, cov.map((g) => g.cells), true) + '<p class="kleg">' + (cov.length ? "Groups: " + leg : mins.length ? "Every cell is 1: the output is always 1." : "No 1s: the output is always 0.") + "</p>";
}
const GD = {"w": 382, "h": 172.0, "inputs": [{"n": "A", "y": 24}, {"n": "B", "y": 78}, {"n": "C", "y": 132}], "gates": [{"n": "G1", "x": 94, "cy": 51.0, "h": 42, "svg": "<path class=\"ax\" style=\"fill:var(--surface)\" d=\"M94,30.0 Q126.4,30.0 148,51.0 Q126.4,72.0 94,72.0 Q109.12,51.0 94,30.0 Z\"/><path class=\"ax\" d=\"M87,30.0 Q99,51.0 87,72.0\"/>", "ox": 148}, {"n": "G2", "x": 94, "cy": 132.0, "h": 32, "svg": "<path class=\"ax\" style=\"fill:var(--surface)\" d=\"M94,116.0 L140,132.0 L94,148.0 Z\"/><circle class=\"ax\" style=\"fill:var(--surface)\" cx=\"144\" cy=\"132.0\" r=\"4\"/>", "ox": 148}, {"n": "X", "x": 212, "cy": 91.5, "h": 42, "svg": "<path class=\"ax\" style=\"fill:var(--surface)\" d=\"M212,70.5 H239.0 A27.0,21.0 0 0 1 239.0,112.5 H212 Z\"/>", "ox": 266}], "wires": [{"d": "M58,24 H82 V40.0 H92.48571428571428", "s": "A", "dot": null}, {"d": "M58,78 H77 V62.0 H92.48571428571428", "s": "B", "dot": null}, {"d": "M58,132 H82 V132.0 H94", "s": "C", "dot": null}, {"d": "M148,51.0 H200 V80.5 H212", "s": "G1", "dot": null}, {"d": "M148,132.0 H195 V102.5 H212", "s": "G2", "dot": null}, {"d": "M50,24 H58", "s": "A", "dot": null}, {"d": "M50,78 H58", "s": "B", "dot": null}, {"d": "M50,132 H58", "s": "C", "dot": null}], "outs": [{"d": "M266,91.5 H296", "s": "X", "x": 296, "y": 91.5}], "outset": ["X"], "net": [["G1", "XOR", ["A", "B"]], ["G2", "NOT", ["C"]], ["X", "AND", ["G1", "G2"]]], "in": ["A", "B", "C"]}, GG = {"w": 500, "h": 226.0, "inputs": [{"n": "T", "y": 24}, {"n": "W", "y": 78}, {"n": "R", "y": 132}, {"n": "M", "y": 186}], "gates": [{"n": "G1", "x": 94, "cy": 78.0, "h": 32, "svg": "<path class=\"ax\" style=\"fill:var(--surface)\" d=\"M94,62.0 L140,78.0 L94,94.0 Z\"/><circle class=\"ax\" style=\"fill:var(--surface)\" cx=\"144\" cy=\"78.0\" r=\"4\"/>", "ox": 148}, {"n": "G2", "x": 94, "cy": 132.0, "h": 32, "svg": "<path class=\"ax\" style=\"fill:var(--surface)\" d=\"M94,116.0 L140,132.0 L94,148.0 Z\"/><circle class=\"ax\" style=\"fill:var(--surface)\" cx=\"144\" cy=\"132.0\" r=\"4\"/>", "ox": 148}, {"n": "G3", "x": 94, "cy": 186.0, "h": 32, "svg": "<path class=\"ax\" style=\"fill:var(--surface)\" d=\"M94,170.0 L140,186.0 L94,202.0 Z\"/><circle class=\"ax\" style=\"fill:var(--surface)\" cx=\"144\" cy=\"186.0\" r=\"4\"/>", "ox": 148}, {"n": "G4", "x": 212, "cy": 159.0, "h": 42, "svg": "<path class=\"ax\" style=\"fill:var(--surface)\" d=\"M212,138.0 Q244.4,138.0 266,159.0 Q244.4,180.0 212,180.0 Q227.12,159.0 212,138.0 Z\"/>", "ox": 266}, {"n": "X", "x": 330, "cy": 87.0, "h": 56, "svg": "<path class=\"ax\" style=\"fill:var(--surface)\" d=\"M330,59.0 H357.0 A27.0,28.0 0 0 1 357.0,115.0 H330 Z\"/>", "ox": 384}], "wires": [{"d": "M58,78 H82 V78.0 H94", "s": "W", "dot": null}, {"d": "M58,132 H82 V132.0 H94", "s": "R", "dot": null}, {"d": "M58,186 H82 V186.0 H94", "s": "M", "dot": null}, {"d": "M148,132.0 H200 V148.0 H217.4857142857143", "s": "G2", "dot": null}, {"d": "M148,186.0 H195 V170.0 H217.4857142857143", "s": "G3", "dot": null}, {"d": "M58,24 H318 V69.0 H330", "s": "T", "dot": null}, {"d": "M148,78.0 H313 V87.0 H330", "s": "G1", "dot": null}, {"d": "M266,159.0 H308 V105.0 H330", "s": "G4", "dot": null}, {"d": "M50,24 H58", "s": "T", "dot": null}, {"d": "M50,78 H58", "s": "W", "dot": null}, {"d": "M50,132 H58", "s": "R", "dot": null}, {"d": "M50,186 H58", "s": "M", "dot": null}], "outs": [{"d": "M384,87.0 H414", "s": "X", "x": 414, "y": 87.0}], "outset": ["X"], "net": [["G1", "NOT", ["W"]], ["G2", "NOT", ["R"]], ["G3", "NOT", ["M"]], ["G4", "OR", ["G2", "G3"]], ["X", "AND", ["T", "G1", "G4"]]], "in": ["T", "W", "R", "M"]}, GW = {"w": 618, "h": 198.0, "inputs": [{"n": "A", "y": 24}, {"n": "B", "y": 78}, {"n": "C", "y": 132}], "gates": [{"n": "G1", "x": 94, "cy": 24.0, "h": 32, "svg": "<path class=\"ax\" style=\"fill:var(--surface)\" d=\"M94,8.0 L140,24.0 L94,40.0 Z\"/><circle class=\"ax\" style=\"fill:var(--surface)\" cx=\"144\" cy=\"24.0\" r=\"4\"/>", "ox": 148}, {"n": "G2", "x": 94, "cy": 78.0, "h": 32, "svg": "<path class=\"ax\" style=\"fill:var(--surface)\" d=\"M94,62.0 L140,78.0 L94,94.0 Z\"/><circle class=\"ax\" style=\"fill:var(--surface)\" cx=\"144\" cy=\"78.0\" r=\"4\"/>", "ox": 148}, {"n": "G3", "x": 212, "cy": 51.0, "h": 42, "svg": "<path class=\"ax\" style=\"fill:var(--surface)\" d=\"M212,30.0 H239.0 A27.0,21.0 0 0 1 239.0,72.0 H212 Z\"/>", "ox": 266}, {"n": "G4", "x": 94, "cy": 118.0, "h": 32, "svg": "<path class=\"ax\" style=\"fill:var(--surface)\" d=\"M94,102.0 L140,118.0 L94,134.0 Z\"/><circle class=\"ax\" style=\"fill:var(--surface)\" cx=\"144\" cy=\"118.0\" r=\"4\"/>", "ox": 148}, {"n": "G5", "x": 94, "cy": 158.0, "h": 32, "svg": "<path class=\"ax\" style=\"fill:var(--surface)\" d=\"M94,142.0 L140,158.0 L94,174.0 Z\"/><circle class=\"ax\" style=\"fill:var(--surface)\" cx=\"144\" cy=\"158.0\" r=\"4\"/>", "ox": 148}, {"n": "G6", "x": 212, "cy": 138.0, "h": 42, "svg": "<path class=\"ax\" style=\"fill:var(--surface)\" d=\"M212,117.0 H239.0 A27.0,21.0 0 0 1 239.0,159.0 H212 Z\"/>", "ox": 266}, {"n": "G7", "x": 330, "cy": 94.5, "h": 42, "svg": "<path class=\"ax\" style=\"fill:var(--surface)\" d=\"M330,73.5 Q362.4,73.5 384,94.5 Q362.4,115.5 330,115.5 Q345.12,94.5 330,73.5 Z\"/>", "ox": 384}, {"n": "X", "x": 448, "cy": 94.5, "h": 32, "svg": "<path class=\"ax\" style=\"fill:var(--surface)\" d=\"M448,78.5 L494,94.5 L448,110.5 Z\"/><circle class=\"ax\" style=\"fill:var(--surface)\" cx=\"498\" cy=\"94.5\" r=\"4\"/>", "ox": 502}], "wires": [{"d": "M58,24 H82 V24.0 H94", "s": "A", "dot": null}, {"d": "M58,78 H82 V78.0 H94", "s": "B", "dot": null}, {"d": "M148,24.0 H200 V40.0 H212", "s": "G1", "dot": null}, {"d": "M148,78.0 H195 V62.0 H212", "s": "G2", "dot": null}, {"d": "M58,78 H82 V118.0 H94", "s": "B", "dot": null}, {"d": "M58,132 H82 V158.0 H94", "s": "C", "dot": null}, {"d": "M148,118.0 H200 V127.0 H212", "s": "G4", "dot": null}, {"d": "M148,158.0 H195 V149.0 H212", "s": "G5", "dot": null}, {"d": "M266,51.0 H318 V83.5 H335.48571428571427", "s": "G3", "dot": null}, {"d": "M266,138.0 H313 V105.5 H335.48571428571427", "s": "G6", "dot": null}, {"d": "M384,94.5 H436 V94.5 H448", "s": "G7", "dot": null}, {"d": "M50,24 H58", "s": "A", "dot": null}, {"d": "M50,78 H58", "s": "B", "dot": null}, {"d": "M50,132 H58", "s": "C", "dot": null}], "outs": [{"d": "M502,94.5 H532", "s": "X", "x": 532, "y": 94.5}], "outset": ["X"], "net": [["G1", "NOT", ["A"]], ["G2", "NOT", ["B"]], ["G3", "AND", ["G1", "G2"]], ["G4", "NOT", ["B"]], ["G5", "NOT", ["C"]], ["G6", "AND", ["G4", "G5"]], ["G7", "OR", ["G3", "G6"]], ["X", "NOT", ["G7"]]], "in": ["A", "B", "C"]};

(function () {
  const cases = [[0, 1, 0], [1, 1, 0], [1, 0, 1], [0, 0, 0]];
  const draw = (s) => { const [a, b, c] = cases[Math.round(s.i)]; return circFit(GD, circEval(GD, { A: a, B: b, C: c }), 560, { vals: true }); };
  Lib.stepper($("#stA"), { w: 560, h: Math.round(GD.h * 2.2) + 12, label: "X = (A XOR B) AND NOT C", base: { i: 0 }, draw, tween: 150, dwell: 2400, steps: cases.map(([a, b, c], i) => { const x = (a ^ b) & (c ? 0 : 1); return { cap: `A = ${a}, B = ${b}, C = ${c}: A XOR B = <b>${a ^ b}</b>, NOT C = <b>${c ? 0 : 1}</b>, so X = <b>${x}</b>.`, s: { i } }; }) });
})();
(function () {
  const cases = [{ T: 1, W: 0, R: 0, M: 0 }, { T: 1, W: 1, R: 0, M: 0 }, { T: 1, W: 0, R: 1, M: 1 }, { T: 1, W: 0, R: 1, M: 0 }];
  const note = ["Hot, wind acceptable, no rain: the window opens.", "Hot but the wind is too high: the window stays closed.", "Rain detected and override on: closed.", "Rain detected but override off: the window opens."];
  const draw = (s) => circFit(GG, circEval(GG, cases[Math.round(s.i)]), 560, { vals: true });
  Lib.stepper($("#stB"), { w: 560, h: Math.round(GG.h * 2.2) + 12, label: "Greenhouse window", base: { i: 0 }, draw, tween: 150, dwell: 2600, steps: cases.map((c, i) => ({ cap: note[i], s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const v = circEval(GW, { A: 0, B: 1, C: 0 }); Object.keys(v).forEach((n) => { if (!["A", "B", "C"].includes(n) && k < 3) v[n] = 0; }); return circFit(GW, v, 600, { vals: true }); };
  Lib.stepper($("#stC"), { w: 600, h: Math.round(GW.h * 2) + 12, label: "NOT ((NOT A AND NOT B) OR (NOT B AND NOT C))", base: { i: 0 }, draw, tween: 150, dwell: 2800, steps: [
    { cap: "X = NOT ((NOT A AND NOT B) OR (NOT B AND NOT C)). Inputs A = 0, B = 1, C = 0.", s: { i: 0 } },
    { cap: "The outermost operator is NOT, so that is the final gate. Inside it is an OR.", s: { i: 1 } },
    { cap: "The OR takes two ANDs. Each AND takes two NOT gates.", s: { i: 2 } },
    { cap: "The whole circuit gives X = <b>1</b> for A = 0, B = 1, C = 0.", s: { i: 3 } }] });
})();
circLab("#labD", GD, [], ["X"]);
circLab("#labG", GG, [], ["X"]);
btnTable("gB", "gO", [
  ["NOT", "Inverts the input", "0 → 1, 1 → 0", "One input only"],
  ["AND", "1 only when both inputs are 1", "0 0 0 1", "All inputs 1"],
  ["OR", "0 only when both inputs are 0", "0 1 1 1", "Any input 1"],
  ["NAND", "0 only when both inputs are 1", "1 1 1 0", "AND then NOT"],
  ["NOR", "1 only when both inputs are 0", "1 0 0 0", "OR then NOT"],
  ["XOR", "1 when the inputs are different", "0 1 1 0", "Different"]
], ["Gate", "Output is", "Output for AB = 00, 01, 10, 11", "Remember"]);
Lib.classify($("#cl1"), { prompt: "Which gate does the description give?", buckets: [{"label": "AND"}, {"label": "OR"}, {"label": "XOR"}, {"label": "NAND"}, {"label": "NOR"}], items: [{"text": "Output is 1 only when both inputs are 1", "b": 0}, {"text": "Output is 0 only when both inputs are 0", "b": 1}, {"text": "Output is 1 when the inputs are different", "b": 2}, {"text": "Output is 0 only when both inputs are 1", "b": 3}, {"text": "Output is 1 only when both inputs are 0", "b": 4}, {"text": "A car starts only if the key is turned AND the brake is pressed", "b": 0}], done: "AND all, OR any, XOR different, NAND not AND, NOR not OR." });
Lib.classify($("#cl2"), { prompt: "Is the output of X = (A XOR B) AND NOT C equal to 1 or 0?", buckets: [{"label": "X = 1"}, {"label": "X = 0"}], items: [{"text": "A=0, B=1, C=0", "b": 0}, {"text": "A=1, B=1, C=0", "b": 1}, {"text": "A=1, B=0, C=0", "b": 0}, {"text": "A=0, B=1, C=1", "b": 1}, {"text": "A=0, B=0, C=0", "b": 1}, {"text": "A=1, B=0, C=1", "b": 1}], done: "The inputs must differ and C must be 0." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["NAND", "Output is 0 when both inputs are 1, otherwise 1"], ["NOR", "Output is 1 when both inputs are 0, otherwise 0"], ["XOR", "Output is 1 when the inputs are different"], ["OR", "Output is 0 when both inputs are 0, otherwise 1"], ["NOT", "Output is the opposite of the input"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the steps for drawing a circuit from an expression in order.", items: ["Identify the outermost operator: it is the final gate", "Draw the gates for the brackets that feed it", "Connect each gate to its inputs or to the gates inside its brackets", "Add every NOT as a gate on the correct wire", "Check that the number of gates equals the number of operators"], done: "Outermost, inner, connect, NOT, count." });
Lib.calc($("#c1"), { qs: [
  {"q": "How many rows does the truth table for a 4-input circuit have?", "a": 16, "unit": "", "tol": 0.01, "hint": "2^4.", "sol": "<b>16</b>."},
  {"q": "In X = (A XOR B) AND NOT C, for how many of the 8 rows is X = 1?", "a": 2, "unit": "", "tol": 0.01, "hint": "010 and 100.", "sol": "<b>2</b>."},
  {"q": "How many gates are in the circuit for X = NOT ((A AND B) OR (C AND D))?", "a": 4, "unit": "", "tol": 0.01, "hint": "Two ANDs, one OR, one NOT.", "sol": "<b>4</b>."},
  {"q": "For A=1, B=1 what is A NAND B (1 or 0)?", "a": 0, "unit": "", "tol": 0.01, "hint": "AND is 1, then NOT.", "sol": "<b>0</b>."},
  {"q": "A 3-input AND gate is given 1, 1, 0. What is the output?", "a": 0, "unit": "", "tol": 0.01, "hint": "All must be 1.", "sol": "<b>0</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "Which gate gives 1 for different inputs?", opts: ["XOR", "AND", "NOR", "NAND"], a: 0, why: "XOR." },
  { q: "NOR outputs 1 when:", opts: ["Both inputs are 0", "Both are 1", "Either input is 1", "Inputs differ"], a: 0, why: "Both inputs 0." },
  { q: "How many gates are needed for X = (A AND B) OR NOT C?", opts: ["3", "2", "4", "1"], a: 0, why: "AND, NOT, OR." },
  { q: "NAND is the same as:", opts: ["AND followed by NOT", "OR followed by NOT", "XOR", "NOT followed by AND"], a: 0, why: "AND then NOT." },
  { q: "The working space column is used for:", opts: ["Intermediate results", "The final answer only", "Input names", "Row numbers"], a: 0, why: "Intermediate values." },
  { q: "Which expression is 1 only for 001 and 111?", opts: ["NOT (A XOR B) AND C", "A OR C", "A NAND B", "NOT C"], a: 0, why: "A equals B and C is 1." },
] });
Lib.cards($("#fc1"), { cards: [
  ["NOT", "Inverts."],
  ["AND", "1 only if all inputs are 1."],
  ["OR", "0 only if all inputs are 0."],
  ["XOR", "1 if the inputs differ."],
  ["NAND", "0 only if both inputs are 1."],
  ["NOR", "1 only if both inputs are 0."],
  ["Truth table", "Every input combination and the output."],
  ["Working space", "Holds intermediate results."],
] });
