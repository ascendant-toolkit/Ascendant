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

/* ---- a small SQL engine: SELECT (joins, WHERE, GROUP BY, ORDER BY, aggregates), INSERT, UPDATE, DELETE, CREATE TABLE/DATABASE, ALTER TABLE ---- */
const SQL = (function () {
  function tok(s) {
    const t = []; let i = 0;
    while (i < s.length) { const c = s[i];
      if (/\s/.test(c)) { i++; continue; }
      if (c === "'" || c === '"') { let j = i + 1, v = ""; while (j < s.length && s[j] !== c) v += s[j++]; t.push({ k: "s", v }); i = j + 1; continue; }
      if (c === "#") { let j = i + 1, v = ""; while (j < s.length && s[j] !== "#") v += s[j++]; t.push({ k: "s", v }); i = j + 1; continue; }
      if (/[0-9]/.test(c)) { let j = i; while (j < s.length && /[0-9.]/.test(s[j])) j++; t.push({ k: "n", v: parseFloat(s.slice(i, j)) }); i = j; continue; }
      if (/[A-Za-z_]/.test(c)) { let j = i; while (j < s.length && /[A-Za-z0-9_.]/.test(s[j])) j++; t.push({ k: "w", v: s.slice(i, j) }); i = j; continue; }
      const two = s.slice(i, i + 2); if (["<=", ">=", "<>", "!=", "=="].includes(two)) { t.push({ k: "o", v: two }); i += 2; continue; }
      t.push({ k: "o", v: c }); i++; }
    return t;
  }
  const U = (x) => String(x).toUpperCase();
  function P(toks) { let p = 0; const peek = () => toks[p], next = () => toks[p++]; const isW = (w) => peek() && peek().k === "w" && U(peek().v) === w; const eatW = (w) => { if (isW(w)) { p++; return true; } return false; }; const isO = (o) => peek() && peek().k === "o" && peek().v === o; const eatO = (o) => { if (isO(o)) { p++; return true; } return false; };
    const need = (w) => { if (!eatW(w)) throw new Error("Expected " + w + (peek() ? " near '" + peek().v + "'" : " at the end")); };
    const needO = (o) => { if (!eatO(o)) throw new Error("Expected '" + o + "'" + (peek() ? " near '" + peek().v + "'" : " at the end")); };
    function value() { const t = next(); if (!t) throw new Error("Unexpected end"); if (t.k === "n") return { c: "lit", v: t.v }; if (t.k === "s") return { c: "lit", v: t.v }; if (t.k === "w") { const u = U(t.v); if (u === "TRUE") return { c: "lit", v: true }; if (u === "FALSE") return { c: "lit", v: false }; if (u === "NULL") return { c: "lit", v: null }; if (["COUNT", "SUM", "AVG", "MIN", "MAX"].includes(u) && isO("(")) { next(); let arg; if (eatO("*")) arg = { c: "star" }; else arg = value(); needO(")"); return { c: "agg", f: u, a: arg }; } return { c: "col", n: t.v }; } if (t.k === "o" && t.v === "(") { const e = cond(); needO(")"); return e; } if (t.k === "o" && t.v === "-") { const v = value(); return { c: "lit", v: -v.v }; } throw new Error("Unexpected '" + t.v + "'"); }
    function cmp() { if (eatW("NOT")) return { c: "not", a: cmp() }; const a = value(); if (peek() && peek().k === "o" && ["=", "<", ">", "<=", ">=", "<>", "!=", "=="].includes(peek().v)) { const op = next().v; return { c: "cmp", op, a, b: value() }; } if (eatW("LIKE")) return { c: "like", a, b: value() }; if (eatW("BETWEEN")) { const lo = value(); need("AND"); const hi = value(); return { c: "between", a, lo, hi }; } if (eatW("IN")) { needO("("); const l = []; do { l.push(value()); } while (eatO(",")); needO(")"); return { c: "in", a, l }; } if (eatW("IS")) { const n = eatW("NOT"); need("NULL"); return { c: "isnull", a, n }; } return a; }
    function and() { let l = cmp(); while (eatW("AND")) l = { c: "and", a: l, b: cmp() }; return l; }
    function cond() { let l = and(); while (eatW("OR")) l = { c: "or", a: l, b: and() }; return l; }
    function selectStmt() { const q = { t: "select", items: [], from: [], joins: [] }; q.distinct = eatW("DISTINCT"); do { if (eatO("*")) q.items.push({ e: { c: "star" } }); else { const e = value(); let al = null; if (eatW("AS")) { const a = next(); al = a.v; } q.items.push({ e, al }); } } while (eatO(",")); need("FROM"); q.from.push(next().v); while (true) { if (eatO(",")) { q.from.push(next().v); continue; } if (eatW("INNER") || eatW("JOIN")) { eatW("JOIN"); const tn = next().v; need("ON"); q.joins.push({ t: tn, on: cond() }); continue; } break; } if (eatW("WHERE")) q.where = cond(); if (eatW("GROUP")) { need("BY"); q.group = []; do { q.group.push(value()); } while (eatO(",")); } if (eatW("ORDER")) { need("BY"); q.order = []; do { const e = value(); let d = false; if (eatW("DESC")) d = true; else eatW("ASC"); q.order.push({ e, d }); } while (eatO(",")); } return q; }
    return { selectStmt, cond, value, need, needO, eatW, eatO, isW, peek, next, done: () => p >= toks.length, pos: () => p, toks };
  }
  function cellVal(r, name, tabs) { const n = name.toLowerCase(); if (n.includes(".")) { const [t, c] = n.split("."); const k = r[t + "." + c]; if (k !== undefined || (t + "." + c) in r) return r[t + "." + c]; throw new Error("Unknown column " + name); } let hit = null, cnt = 0; for (const k in r) { if (k.split(".")[1] === n) { hit = k; cnt++; } } if (cnt === 0) throw new Error("Unknown column " + name); return r[hit]; }
  function ev(e, r, db) { switch (e.c) { case "lit": return e.v; case "col": return cellVal(r, e.n); case "and": return ev(e.a, r) && ev(e.b, r); case "or": return ev(e.a, r) || ev(e.b, r); case "not": return !ev(e.a, r);
      case "cmp": { let a = ev(e.a, r), b = ev(e.b, r); if (typeof a === "boolean" || typeof b === "boolean") { a = norm(a); b = norm(b); } else if (typeof a === "string" && typeof b === "string") { const da = Date.parse(dfmt(a)), db2 = Date.parse(dfmt(b)); if (!isNaN(da) && !isNaN(db2) && /\d\/\d|\d-\d/.test(a) && /\d\/\d|\d-\d/.test(b)) { a = da; b = db2; } else { a = a.toLowerCase(); b = b.toLowerCase(); } } const o = e.op; return o === "=" || o === "==" ? a === b : o === "<>" || o === "!=" ? a !== b : o === "<" ? a < b : o === ">" ? a > b : o === "<=" ? a <= b : a >= b; }
      case "like": { const a = String(ev(e.a, r)), pat = String(ev(e.b, r)); const rx = new RegExp("^" + pat.replace(/[.+?^${}()|[\]\\]/g, "\\$&").replace(/[%*]/g, ".*").replace(/_/g, ".") + "$", "i"); return rx.test(a); }
      case "between": { const a = ev(e.a, r), lo = ev(e.lo, r), hi = ev(e.hi, r); return a >= lo && a <= hi; } case "in": { const a = ev(e.a, r); return e.l.some((x) => ev(x, r) === a); } case "isnull": { const a = ev(e.a, r); const n = a === null || a === undefined || a === ""; return e.n ? !n : n; } default: throw new Error("Cannot evaluate"); } }
  const norm = (x) => (typeof x === "boolean" ? x : typeof x === "string" ? ["yes", "true", "y"].includes(x.toLowerCase()) : !!x);
  function dfmt(s) { const m = s.match(/^(\d\d)\/(\d\d)\/(\d{4})$/); return m ? m[3] + "-" + m[2] + "-" + m[1] : s; }
  function aggs(e, out) { if (!e) return; if (e.c === "agg") out.push(e); else for (const k of ["a", "b", "lo", "hi"]) if (e[k] && typeof e[k] === "object") aggs(e[k], out); }
  function exprName(e) { return e.c === "col" ? e.n.split(".").pop() : e.c === "agg" ? e.f + "(" + (e.a.c === "star" ? "*" : e.a.n || "") + ")" : e.c === "lit" ? String(e.v) : "expr"; }
  function evalAgg(e, rows) { if (e.c === "agg") { if (e.a.c === "star") return rows.length; const v = rows.map((r) => ev(e.a, r)).filter((x) => x !== null && x !== undefined && x !== ""); if (e.f === "COUNT") return v.length; if (!v.length) return null; if (e.f === "SUM") return Math.round(v.reduce((a, b) => a + Number(b), 0) * 1e6) / 1e6; if (e.f === "AVG") return Math.round(v.reduce((a, b) => a + Number(b), 0) / v.length * 1e6) / 1e6; if (e.f === "MIN") return v.reduce((a, b) => (a < b ? a : b)); return v.reduce((a, b) => (a > b ? a : b)); } return ev(e, rows[0] || {}); }
  function tbl(db, n) { const k = Object.keys(db.tables).find((x) => x.toLowerCase() === n.toLowerCase()); if (!k) throw new Error("No table named " + n); return db.tables[k]; }
  function rowsOf(db, name) { const t = tbl(db, name); const nm = name.toLowerCase(); return t.rows.map((r) => { const o = {}; t.cols.forEach((c, i) => (o[nm + "." + c.toLowerCase()] = r[i])); return o; }); }
  function run(db, sql) {
    sql = sql.trim().replace(/;+\s*$/, ""); const P0 = P(tok(sql)); const first = P0.peek() && U(P0.peek().v);
    if (first === "SELECT") { P0.next(); const q = P0.selectStmt(); if (!P0.done()) throw new Error("Unexpected '" + P0.peek().v + "'"); return select(db, q); }
    if (first === "INSERT") { P0.next(); P0.need("INTO"); const tn = P0.next().v; const t = tbl(db, tn); let cols = null; if (P0.eatO("(")) { cols = []; do { cols.push(P0.next().v); } while (P0.eatO(",")); P0.needO(")"); } P0.need("VALUES"); P0.needO("("); const vals = []; do { vals.push(P0.value().v); } while (P0.eatO(",")); P0.needO(")"); const row = t.cols.map(() => null); (cols || t.cols).forEach((c, i) => { const ix = t.cols.findIndex((x) => x.toLowerCase() === c.toLowerCase()); if (ix < 0) throw new Error("No column " + c); row[ix] = vals[i]; }); if (vals.length !== (cols || t.cols).length) throw new Error("The number of values does not match the number of columns"); t.rows.push(row); return { msg: "1 row inserted into " + tn + "." }; }
    if (first === "DELETE") { P0.next(); P0.need("FROM"); const tn = P0.next().v; const t = tbl(db, tn); let w = null; if (P0.eatW("WHERE")) w = P0.cond(); const keep = [], before = t.rows.length; const all = rowsOf(db, tn); t.rows = t.rows.filter((r, i) => !(w ? ev(w, all[i]) : true)); return { msg: before - t.rows.length + " row(s) deleted from " + tn + "." }; }
    if (first === "UPDATE") { P0.next(); const tn = P0.next().v; const t = tbl(db, tn); P0.need("SET"); const sets = []; do { const c = P0.next().v; P0.needO("="); sets.push([c, P0.value()]); } while (P0.eatO(",")); let w = null; if (P0.eatW("WHERE")) w = P0.cond(); const all = rowsOf(db, tn); let n = 0; t.rows.forEach((r, i) => { if (!w || ev(w, all[i])) { sets.forEach(([c, v]) => { const ix = t.cols.findIndex((x) => x.toLowerCase() === c.toLowerCase()); if (ix < 0) throw new Error("No column " + c); r[ix] = ev(v, all[i]); }); n++; } }); return { msg: n + " row(s) updated in " + tn + "." }; }
    if (first === "CREATE") { P0.next(); if (P0.eatW("DATABASE")) { const n = P0.next().v; return { msg: "Database " + n + " created." }; } P0.need("TABLE"); const tn = P0.next().v; P0.needO("("); const cols = []; while (true) { if (P0.isW("PRIMARY") || P0.isW("FOREIGN")) { let d = 0; while (!P0.done()) { const t = P0.peek(); if (t.v === "(") d++; if (t.v === ")") { if (d === 0) break; d--; } if (t.v === "," && d === 0) break; P0.next(); } } else { const c = P0.next().v; cols.push(c); let d = 0; while (!P0.done()) { const t = P0.peek(); if (t.v === "(") d++; if (t.v === ")") { if (d === 0) break; d--; } if (t.v === "," && d === 0) break; P0.next(); } } if (!P0.eatO(",")) break; } P0.needO(")"); db.tables[tn] = { cols, rows: [] }; return { msg: "Table " + tn + " created with " + cols.length + " column(s)." }; }
    if (first === "ALTER") { P0.next(); P0.need("TABLE"); const tn = P0.next().v; const t = tbl(db, tn); P0.need("ADD"); if (P0.isW("FOREIGN") || P0.isW("PRIMARY")) return { msg: "Key added to " + tn + "." }; const added = []; do { const c = P0.next().v; added.push(c); while (!P0.done() && !(P0.peek().v === ",")) P0.next(); } while (P0.eatO(",")); added.forEach((c) => { t.cols.push(c); t.rows.forEach((r) => r.push(null)); }); return { msg: "Added " + added.join(", ") + " to " + tn + "." }; }
    throw new Error("Not a statement I can run: start with SELECT, INSERT, UPDATE, DELETE, CREATE or ALTER.");
  }
  function select(db, q) {
    let rows = rowsOf(db, q.from[0]); for (let i = 1; i < q.from.length; i++) { const r2 = rowsOf(db, q.from[i]); const out = []; rows.forEach((a) => r2.forEach((b) => out.push(Object.assign({}, a, b)))); rows = out; }
    q.joins.forEach((j) => { const r2 = rowsOf(db, j.t); const out = []; rows.forEach((a) => r2.forEach((b) => { const m = Object.assign({}, a, b); if (ev(j.on, m)) out.push(m); })); rows = out; });
    if (q.where) rows = rows.filter((r) => ev(q.where, r));
    const hasAgg = q.items.some((it) => { const o = []; aggs(it.e, o); return o.length; });
    let cols, res;
    const expand = () => { const cs = [], ex = []; q.items.forEach((it) => { if (it.e.c === "star") { q.from.concat(q.joins.map((j) => j.t)).forEach((tn) => tbl(db, tn).cols.forEach((c) => { cs.push(c); ex.push({ c: "col", n: tn + "." + c }); })); } else { cs.push(it.al || exprName(it.e)); ex.push(it.e); } }); return [cs, ex]; };
    const resolve = (e) => { if (e.c === "col" && !e.n.includes(".")) { const it = q.items.find((x) => x.al && x.al.toLowerCase() === e.n.toLowerCase()); if (it) return it.e; } return e; };
    if (hasAgg || q.group) {
      const groups = new Map(); rows.forEach((r) => { const key = (q.group || []).map((g) => String(ev(g, r))).join("|"); if (!groups.has(key)) groups.set(key, []); groups.get(key).push(r); }); if (!q.group && !groups.size) groups.set("", []);
      const [cs, ex] = expand(); cols = cs; res = [...groups.values()].map((g) => ({ vals: ex.map((e) => evalAgg(e, g)), sample: g[0] || {}, grp: g }));
      if (q.order) res.sort((A, B) => { for (const o of q.order) { const oe = resolve(o.e); const a = oe.c === "agg" ? evalAgg(oe, A.grp) : ev(oe, A.sample), b = oe.c === "agg" ? evalAgg(oe, B.grp) : ev(oe, B.sample); if (a < b) return o.d ? 1 : -1; if (a > b) return o.d ? -1 : 1; } return 0; });
      res = res.map((x) => x.vals);
    } else {
      if (q.order) rows = rows.slice().sort((A, B) => { for (const o of q.order) { const oe = resolve(o.e); const a = ev(oe, A), b = ev(oe, B); if (a < b) return o.d ? 1 : -1; if (a > b) return o.d ? -1 : 1; } return 0; });
      const [cs, ex] = expand(); cols = cs; res = rows.map((r) => ex.map((e) => ev(e, r)));
    }
    if (q.distinct) { const seen = new Set(); res = res.filter((r) => { const k = JSON.stringify(r); if (seen.has(k)) return false; seen.add(k); return true; }); }
    return { cols, rows: res };
  }
  return { run };
})();
function sqlLab(el, tables, start, opts) {
  opts = opts || {}; const root = typeof el === "string" ? $(el) : el; const db = { tables: JSON.parse(JSON.stringify(tables)) }; const orig = JSON.stringify(tables);
  root.innerHTML = '<div data-sch></div><textarea data-q rows="' + (opts.rows || 5) + '" style="width:100%;font:13px/1.4 ui-monospace,Menlo,monospace;padding:8px;border:1px solid var(--border);border-radius:8px;background:var(--surface);color:inherit" spellcheck="false"></textarea><div class="btnrow"><button data-run>Run</button><button data-reset>Reset the database</button></div><div data-out></div>';
  const q = root.querySelector("[data-q]"), out = root.querySelector("[data-out]"), sch = root.querySelector("[data-sch]"); q.value = start || "";
  const fmt = (v) => (v === null || v === undefined ? "NULL" : v === true ? "TRUE" : v === false ? "FALSE" : v);
  const showTables = () => { sch.innerHTML = '<p class="note" style="margin:0 0 6px">Tables: ' + Object.entries(db.tables).map(([n, t]) => "<b>" + n + "</b>(" + t.cols.join(", ") + ") " + t.rows.length + " rows").join(" · ") + "</p>"; };
  const go = () => { try { const r = SQL.run(db, q.value); if (r.cols) { out.innerHTML = '<div class="tw"><table class="t mono"><tr>' + r.cols.map((c) => "<th>" + c + "</th>").join("") + "</tr>" + r.rows.map((x) => "<tr>" + x.map((v) => "<td>" + fmt(v) + "</td>").join("") + "</tr>").join("") + "</table></div><p class=\"note\">" + r.rows.length + " row(s)</p>"; } else out.innerHTML = '<div class="verdict">' + r.msg + "</div>"; showTables(); } catch (e) { out.innerHTML = '<div class="verdict" style="border-color:var(--bad)"><b>Error:</b> ' + e.message + "</div>"; } };
  root.querySelector("[data-run]").onclick = go; root.querySelector("[data-reset]").onclick = () => { db.tables = JSON.parse(orig); showTables(); out.innerHTML = ""; };
  showTables(); if (opts.auto !== false && start) go();
}
const DBT = {"STUDENT": {"cols": ["StudentID", "FirstName", "LastName"], "rows": [[12, "Ayo", "Bell"], [13, "Cam", "Diaz"]]}};
(function () {
  const draw = (s) => { const k = Math.round(s.i); const L = ["CREATE TABLE CAR(", "  CarReg VARCHAR(6) NOT NULL,", "  Make VARCHAR(20),", "  Electric BOOLEAN,", "  PRIMARY KEY (CarReg)", ");"]; let o = ""; L.forEach((l, i) => { o += SV.rect(20, 10 + i * 26, 300, 22, i === k ? "f3" : i < k ? "f1" : "cell", { rx: 4 }) + SV.text(28, 26 + i * 26, l, "lbl", { style: "font-size:12px" }); });
    o += SV.text(340, 60, ["table name and bracket", "text field, a value is required", "text field", "yes/no field", "the key", "closing bracket and semicolon"][k], "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stA"), { w: 560, h: 175, label: "CREATE TABLE", base: { i: 0 }, draw, tween: 100, dwell: 2000, steps: ["CREATE TABLE names the table and opens a bracket.", "Each field has a name and a type; NOT NULL means a value is required.", "Fields are separated by commas.", "BOOLEAN stores yes or no.", "PRIMARY KEY names the unique identifier, in brackets.", "Close the bracket and end with a semicolon."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); let o = SV.text(20, 20, "BORROW", "lbl bd") + SV.rect(20, 28, 140, 26, "cell", { rx: 4 }) + SV.text(28, 46, "BorrowID", "lbl", { style: "font-size:12px" }) + SV.rect(165, 28, 140, 26, "cell", { rx: 4 }) + SV.text(173, 46, "CustomerID", "lbl", { style: "font-size:12px" }); if (k >= 1) o += SV.rect(310, 28, 140, 26, "f1", { rx: 4 }) + SV.text(318, 46, "Returned (new)", "lbl", { style: "font-size:12px" });
    o += SV.text(20, 90, k >= 1 ? "ALTER TABLE BORROW ADD Returned BOOLEAN;" : "ALTER TABLE adds a field to an existing table", "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stB"), { w: 480, h: 110, label: "ALTER TABLE", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: ["The table has two fields.", "<b>ALTER TABLE ... ADD</b> creates a new field; existing records keep their data."].map((c, i) => ({ cap: c, s: { i } })) });
})();
(function () {
  const draw = (s) => { const k = Math.round(s.i); const B = (x, t, on) => SV.rect(x, 30, 170, 44, on ? "f3" : "cell", { rx: 8 }) + SV.text(x + 85, 57, t, "lbl bd", { "text-anchor": "middle", style: "font-size:12px" }); let o = B(20, "CUSTOMER(CustomerID)", true) + B(300, "SHOP_ORDER(CustomerID)", k >= 1); if (k >= 1) o += SV.path("M190,52 H300", "ax"); o += SV.text(20, 110, ["", "FOREIGN KEY (CustomerID)", "REFERENCES CUSTOMER(CustomerID)"][Math.min(k, 2)], "lbl bd t3", { style: "font-size:13px" }); return o; };
  Lib.stepper($("#stC"), { w: 520, h: 130, label: "Foreign key", base: { i: 0 }, draw, tween: 100, dwell: 2600, steps: ["CustomerID is the primary key of CUSTOMER.", "In SHOP_ORDER, <b>FOREIGN KEY (CustomerID)</b> marks the field as a foreign key...", "...<b>REFERENCES CUSTOMER(CustomerID)</b> names the table and field it links to."].map((c, i) => ({ cap: c, s: { i } })) });
})();
sqlLab("#ddl", DBT, "CREATE TABLE TEST(\nTestID VARCHAR(5) NOT NULL,\nDescription VARCHAR(30),\nTotalMarks INTEGER,\nPRIMARY KEY (TestID)\n);", { rows: 7 });
btnTable("tB", "tO", [
  ["A100, B245 (codes)", "VARCHAR(4)", "Text, may have letters"],
  ["Quantity 3, 1, 5", "INTEGER", "Whole numbers"],
  ["Price 22.50", "REAL", "Decimals"],
  ["Paid TRUE/FALSE", "BOOLEAN", "Two values"],
  ["13:00", "TIME", "A time of day"]
], ["Sample data", "Type", "Why"]);
btnTable("eB", "eO", [
  ["PRIMARY KEY CharacterID", "PRIMARY KEY (CharacterID)", "Brackets needed"],
  ["FOREIGN KEY (PlayerID)", "...REFERENCES PLAYER(PlayerID)", "Name the table and field"],
  ["SubjectCode VARCHAR NONULL", "SubjectCode VARCHAR NOT NULL", "Spelling"],
  ["SubjectName VARCHAR", "SubjectName VARCHAR,", "A comma is missing"]
], ["Faulty line", "Correct line", "Why"]);
Lib.classify($("#cl1"), { prompt: "Which data type suits the field?", buckets: [{"label": "VARCHAR / CHAR"}, {"label": "INTEGER"}, {"label": "REAL"}, {"label": "BOOLEAN"}, {"label": "DATE"}], items: [{"text": "A registration number such as A123AA", "b": 0}, {"text": "The number of items ordered", "b": 1}, {"text": "A price such as 22.50", "b": 2}, {"text": "Whether a deposit has been paid", "b": 3}, {"text": "The date of birth", "b": 4}, {"text": "A postcode", "b": 0}], done: "Match the sample data." });
Lib.classify($("#cl2"), { prompt: "Is the DDL fragment correct or does it contain an error?", buckets: [{"label": "Correct"}, {"label": "Error"}], items: [{"text": "CREATE DATABASE SHOP;", "b": 0}, {"text": "CREATE DATA BASE SHOP;", "b": 1}, {"text": "PRIMARY KEY (OrderNo)", "b": 0}, {"text": "PRIMARY KEY OrderNo", "b": 1}, {"text": "FOREIGN KEY (ShipID) REFERENCES SHIP(ShipID)", "b": 0}, {"text": "FOREIGN KEY (ShipID)", "b": 1}], done: "The key needs brackets; REFERENCES needs table and field." });
Lib.match($("#m1"), { prompt: "Match the term to its meaning.", pairs: [["CREATE TABLE", "Defines a new table"], ["ALTER TABLE ... ADD", "Adds a field to an existing table"], ["NOT NULL", "A value must be entered"], ["PRIMARY KEY", "Identifies each record uniquely"], ["REFERENCES", "Names the table and field a foreign key links to"]], done: "Learn these terms." });
Lib.order($("#o1"), { prompt: "Put the parts of CREATE TABLE in order.", items: ["CREATE TABLE and the table name, then an opening bracket", "Each field with its data type, separated by commas", "NOT NULL constraints where needed", "PRIMARY KEY and FOREIGN KEY lines", "A closing bracket and a semicolon"], done: "Name, fields, constraints, keys, close." });
Lib.calc($("#c1"), { qs: [
  {"q": "A table has fields ID, Name and Age. How many commas are needed in the field list of CREATE TABLE if the PRIMARY KEY line is also listed after the last field?", "a": 3, "unit": "", "tol": 0.01, "hint": "Between each of the 4 items.", "sol": "<b>3</b>."},
  {"q": "A table has a composite key (PartID, RepairNumber). How many fields are named in PRIMARY KEY (...)?", "a": 2, "unit": "", "tol": 0.01, "hint": "Two.", "sol": "<b>2</b>."},
  {"q": "VARCHAR(5) can hold at most how many characters?", "a": 5, "unit": "", "tol": 0.01, "hint": "The number in brackets.", "sol": "<b>5</b>."},
  {"q": "How many ALTER TABLE statements are needed to add one field to one table?", "a": 1, "unit": "", "tol": 0.01, "hint": "One.", "sol": "<b>1</b>."},
  {"q": "A database has 4 tables, each created with one CREATE TABLE. How many CREATE statements in total including CREATE DATABASE?", "a": 5, "unit": "", "tol": 0.01, "hint": "4 + 1.", "sol": "<b>5</b>."},
] });
Lib.quiz($("#qz1"), { qs: [
  { q: "DDL stands for:", opts: ["Data Definition Language", "Data Delete Language", "Database Design List", "Data Display Layer"], a: 0, why: "Definition." },
  { q: "A new field is added with:", opts: ["ALTER TABLE ... ADD", "INSERT", "UPDATE", "SELECT"], a: 0, why: "ALTER." },
  { q: "A price such as 12.50 is:", opts: ["REAL", "BOOLEAN", "DATE", "CHAR(1)"], a: 0, why: "REAL." },
  { q: "A foreign key uses:", opts: ["REFERENCES", "WHERE", "ORDER BY", "GROUP BY"], a: 0, why: "REFERENCES." },
  { q: "NOT NULL means:", opts: ["A value is required", "The field is a key", "The field is empty", "The field is a date"], a: 0, why: "Required." },
  { q: "A code like A123AA is stored as:", opts: ["VARCHAR or CHAR", "INTEGER", "BOOLEAN", "REAL"], a: 0, why: "Text." },
] });
Lib.cards($("#fc1"), { cards: [
  ["CREATE DATABASE", "Defines a new database."],
  ["CREATE TABLE", "Brackets, fields, types, keys."],
  ["ALTER TABLE", "ADD a field or a foreign key."],
  ["PRIMARY KEY (a)", "Unique identifier; brackets."],
  ["FOREIGN KEY ... REFERENCES t(f)", "Links to another table."],
  ["NOT NULL", "Value required."],
  ["VARCHAR(n)", "Text up to n characters."],
  ["Data types", "CHAR VARCHAR BOOLEAN INTEGER REAL DATE TIME."],
] });
