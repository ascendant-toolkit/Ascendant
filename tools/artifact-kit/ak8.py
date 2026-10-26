"""AS CS chapter 8 helpers: ER-diagram drawer, sqlite checking of answer SQL, and a small in-page SQL engine (SELECT, INSERT, UPDATE, DELETE, CREATE, ALTER)."""
import sqlite3
import re
from ascs import *

# ---------------------------------------------------------------- ER diagrams (static SVG)
def er(ents, rels, w=480, h=None, bw=150, bh=34, cap="E-R diagram"):
    """ents: {name: (x, y)} top-left; rels: [(a, b, 'M:1')] - the symbols are drawn at each end (1 = bar, M = crow's foot)."""
    h = h or max(y for x, y in ents.values()) + bh + 16
    o = f'<svg viewBox="0 0 {w} {h}" style="width:{w}px;max-width:100%;display:block" role="img" aria-label="{cap}">'
    ctr = {n: (x + bw / 2, y + bh / 2) for n, (x, y) in ents.items()}

    def edge(n, tx, ty):
        cx, cy = ctr[n]; dx, dy = tx - cx, ty - cy
        if abs(dx) * bh > abs(dy) * bw:
            s = 1 if dx > 0 else -1
            return cx + s * bw / 2, cy + dy * (bw / 2) / abs(dx), (s, 0)
        s = 1 if dy > 0 else -1
        return cx + dx * (bh / 2) / abs(dy), cy + s * bh / 2, (0, s)

    def mark(px, py, d, kind):
        # d points away from the box; symbol is drawn on the line a little away from the box
        dx, dy = d; nx, ny = -dy, dx
        if kind == "1":
            bx, by = px + dx * 12, py + dy * 12
            return f'<line class="w" x1="{bx + nx * 7:.1f}" y1="{by + ny * 7:.1f}" x2="{bx - nx * 7:.1f}" y2="{by - ny * 7:.1f}"/>'
        fx, fy = px + dx * 14, py + dy * 14
        return "".join(f'<line class="w" x1="{fx:.1f}" y1="{fy:.1f}" x2="{px + nx * k:.1f}" y2="{py + ny * k:.1f}"/>' for k in (-8, 0, 8))
    for a, b, kind in rels:
        ka, kb = kind.split(":")
        ax, ay, da = edge(a, *ctr[b]); bx, by, db = edge(b, *ctr[a])
        o += f'<line class="w" x1="{ax:.1f}" y1="{ay:.1f}" x2="{bx:.1f}" y2="{by:.1f}"/>' + mark(ax, ay, da, ka) + mark(bx, by, db, kb)
    for n, (x, y) in ents.items():
        o += f'<rect class="ax" style="fill:var(--surface)" x="{x}" y="{y}" width="{bw}" height="{bh}" rx="4"/><text class="lbl bd" x="{x + bw / 2}" y="{y + bh / 2 + 4}" text-anchor="middle" style="font-size:11px">{n}</text>'
    return o + "</svg>"

def er_html(*a, **k):
    return f'<div class="circ">{er(*a, **k)}</div>'

# ---------------------------------------------------------------- sqlite checking
class DB:
    """Builds an in-memory sqlite database from 'TABLE(col, col, ...)' strings and runs EXPLAIN on answer SQL."""
    def __init__(self, *schemas):
        self.c = sqlite3.connect(":memory:")
        for s in schemas:
            m = re.match(r"(\w+)\((.*)\)\s*$", s.strip(), re.S)
            cols = ", ".join(x.strip().replace(" ", "") for x in m.group(2).replace("\n", " ").split(","))
            self.c.execute(f'CREATE TABLE "{m.group(1)}" ({cols})')

    def ok(self, sql):
        try:
            self.c.execute("EXPLAIN " + sql)
        except Exception as e:
            raise AssertionError(f"{e}: {sql}")
        return sql

def sqlblock(text):
    return code(text.strip("\n").split("\n"))

SQLJS = r'''
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
'''
