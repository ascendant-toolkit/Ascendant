"""Shared pieces for the A Level Computer Science (9618) section 15.2 pages (Boolean algebra and logic circuits):
overbar notation, truth tables, sum-of-products, Quine-McCluskey grouping, Karnaugh map tables and a netlist-based circuit drawer.
Notation: '~A' puts a bar over A, '~(A+B)' over the whole group, '~~A' nests. '.' is AND and '+' is OR, as in the paper."""
import itertools
import json
from ak20 import *

# ---------------------------------------------------------------- notation

def ob(s):
    """'~A.~B.C + ~(A+B)' -> HTML with overbars."""
    def neg(i):
        if s[i] == "~":
            inner, i = neg(i + 1)
            return f'<span class="ob">{inner}</span>', i
        if s[i] == "(":
            inner, i = seq(i + 1)
            return f'<span class="ob">{inner}</span>', i + 1
        return f'<span class="ob">{s[i]}</span>', i + 1

    def seq(i):
        out = ""
        while i < len(s) and s[i] != ")":
            if s[i] == "~":
                h, i = neg(i + 1)
                out += h
            elif s[i] == "(":
                inner, i = seq(i + 1)
                out += "(" + inner + ")"
                i += 1
            else:
                out += s[i]
                i += 1
        return out, i

    return seq(0)[0]


def bx(s):
    """Inline expression in a monospace-ish span."""
    return f'<span class="bx">{ob(s)}</span>'


# ---------------------------------------------------------------- logic maths

def bits(n, nv):
    return [(n >> (nv - 1 - i)) & 1 for i in range(nv)]


def term(pat, names):
    """Implicant pattern '1-0-' -> '~A.C'... literal string in the ~ notation."""
    parts = []
    for ch, nm in zip(pat, names):
        if ch == "1":
            parts.append(nm)
        elif ch == "0":
            parts.append("~" + nm)
    return ".".join(parts) if parts else "1"


def sop(mins, names):
    """Full sum-of-products: one term per minterm, in row order."""
    nv = len(names)
    return " + ".join(term("".join(map(str, bits(m, nv))), names) for m in sorted(mins))


def _covers(pat, nv):
    return {m for m in range(1 << nv) if all(p == "-" or int(p) == b for p, b in zip(pat, bits(m, nv)))}


def prime_cover(mins, nv):
    """Smallest set of prime implicants covering mins (fewest groups, then fewest literals). Returns [(pattern, cells)]."""
    mins = set(mins)
    pats = ["".join(p) for p in itertools.product("01-", repeat=nv)]
    ok = [p for p in pats if _covers(p, nv) <= mins and _covers(p, nv)]
    primes = [p for p in ok if not any(q != p and _covers(p, nv) < _covers(q, nv) for q in ok)]
    best = None
    for k in range(1, len(primes) + 1):
        for combo in itertools.combinations(primes, k):
            if set().union(*[_covers(p, nv) for p in combo]) == mins:
                lit = sum(sum(c != "-" for c in p) for p in combo)
                if best is None or lit < best[0]:
                    best = (lit, combo)
        if best:
            break
    return [(p, sorted(_covers(p, nv))) for p in (best[1] if best else [])]


def simplified(mins, names):
    """Simplified sum-of-products from the K-map groups."""
    nv = len(names)
    if not mins:
        return "0"
    if len(mins) == 1 << nv:
        return "1"
    return " + ".join(term(p, names) for p, _ in prime_cover(mins, nv))


def mins_of(fn, nv):
    return [m for m in range(1 << nv) if fn(*bits(m, nv))]


# ---------------------------------------------------------------- tables

def ttable(names, cols, rows, mono=True):
    """Truth table. cols = extra column headers, rows = list of (inputs..., outputs...) already complete."""
    h = '<div class="tw"><table class="t mono"><tr>' + "".join(f"<th>{ob(n)}</th>" for n in list(names) + list(cols)) + "</tr>"
    for r in rows:
        h += "<tr>" + "".join(f"<td>{v}</td>" for v in r) + "</tr>"
    return h + "</table></div>"


def tt_from_fn(names, outs):
    """outs = {name: fn(*bits)}; returns the table with the input columns first."""
    nv = len(names)
    rows = [bits(m, nv) + [int(f(*bits(m, nv))) for f in outs.values()] for m in range(1 << nv)]
    return ttable(names, list(outs), rows)


def tt_from_mins(names, out, mins):
    nv = len(names)
    rows = [bits(m, nv) + [int(m in mins)] for m in range(1 << nv)]
    return ttable(names, [out], rows)


GRAY = ["00", "01", "11", "10"]


def kmap(mins, names, groups=None, blank=False, layout=False):
    """K-map as an HTML table. 4 variables: AB across, CD down; 3: AB across, C down; 2: A across, B down.
    groups = list of cell-lists to ring (colours rotate); None means no rings."""
    nv = len(names)
    if nv == 4:
        cols, rows = GRAY, GRAY
        corner = f"{names[2]}{names[3]} \\ {names[0]}{names[1]}"
    elif nv == 3:
        cols, rows = GRAY, ["0", "1"]
        corner = f"{names[0]} \\ {names[1]}{names[2]}"
    else:
        cols, rows = ["0", "1"], ["0", "1"]
        corner = f"{names[1]} \\ {names[0]}"
    cols_n = len(cols)

    def idx(c, r):
        return int(r + c, 2) if nv == 3 else int(c + r, 2)

    cols_c = ["var(--accent)", "var(--bad)", "var(--good)", "var(--warn)", "var(--k)", "var(--n)"]
    h = '<div class="tw"><table class="km"><tr><th>' + corner + "</th>" + "".join(f"<th>{c}</th>" for c in cols) + "</tr>"
    for r in rows:
        h += f"<tr><th>{r}</th>"
        for c in cols:
            m = idx(c, r)
            sh = []
            if groups:
                gi = [k for k, g in enumerate(groups) if m in g]
                sh = [f"inset 0 0 0 {3 + 3 * j}px {cols_c[k % len(cols_c)]}" for j, k in enumerate(gi)]
            st = f' style="box-shadow:{",".join(sh)}"' if sh else ""
            if layout:
                h += f'<td><span class="num">{m}</span></td>'
                continue
            h += f'<td{st}><span class="v">{"" if blank else int(m in mins)}</span><span class="n">{m}</span></td>'
        h += "</tr>"
    return h + "</table></div>"


def kgroups(mins, names):
    """K-map with the optimal groups ringed and a legend line giving each group's term."""
    nv = len(names)
    cov = prime_cover(mins, nv)
    leg = " ".join(f'<span class="kg" style="--c:{["var(--accent)", "var(--bad)", "var(--good)", "var(--warn)", "var(--k)", "var(--n)"][i % 6]}">{ob(term(p, names))}</span>' for i, (p, _) in enumerate(cov))
    return kmap(mins, names, [g for _, g in cov]) + f'<p class="kleg">Groups: {leg}</p>'


# ---------------------------------------------------------------- circuit drawer

W_G = 54


def _kind(k):
    k = k.upper()
    return {"NAND": ("AND", 1), "NOR": ("OR", 1), "XNOR": ("XOR", 1), "NOT": ("NOT", 1)}.get(k, (k, 0))


def _gh(kind, n):
    return 32 if kind == "NOT" else max(40, 14 * n + 14)


def _pins(cy, n, h):
    if n == 1:
        return [cy]
    top = cy - h / 2 + 10
    gap = (h - 20) / (n - 1)
    return [top + i * gap for i in range(n)]


def _gate_path(base, x, cy, h):
    y = cy - h / 2
    w = W_G
    if base == "AND":
        return f"M{x},{y} H{x + w / 2} A{w / 2},{h / 2} 0 0 1 {x + w / 2},{y + h} H{x} Z"
    if base in ("OR", "XOR"):
        return f"M{x},{y} Q{x + w * .6},{y} {x + w},{cy} Q{x + w * .6},{y + h} {x},{y + h} Q{x + w * .28},{cy} {x},{y} Z"
    return f"M{x},{cy - 16} L{x + w - 8},{cy} L{x},{cy + 16} Z"


def circuit(inputs, gates, outs=None, x0=94, colw=118, pad=26, feedback=None):
    """Netlist drawing. inputs = [(name, y)], gates = [(name, TYPE, [sources], col, cy)], outs = names to extend and label (default: gates nobody reads).
    feedback = {(gate, pinindex): ymid} routes that wire through a horizontal channel at ymid (used for latches).
    Returns the geometry dict used by circ_svg() and the JS drawer."""
    feedback = feedback or {}
    g = {n: (t, s, c, cy) for n, t, s, c, cy in gates}
    readers = {}
    for n, t, s, c, cy in gates:
        for src in s:
            readers[src] = readers.get(src, 0) + 1
    if outs is None:
        outs = [n for n, *_ in gates if n not in readers]
    iy = dict(inputs)
    pos = {}
    shapes = []
    for n, t, s, c, cy in gates:
        base, neg = _kind(t)
        h = _gh(base, len(s))
        x = x0 + c * colw
        ox = x + W_G + (8 if neg else 0)
        pos[n] = (ox, cy)
        pins = _pins(cy, len(s), h)
        d = _gate_path(base, x, cy, h)
        extra = ""
        if base == "XOR":
            extra = f'<path class="ax" d="M{x - 7},{cy - h / 2} Q{x + 5},{cy} {x - 7},{cy + h / 2}"/>'
        bub = f'<circle class="ax" style="fill:var(--surface)" cx="{x + W_G + 4}" cy="{cy}" r="4"/>' if neg else ""
        if base == "NOT":
            bub = f'<circle class="ax" style="fill:var(--surface)" cx="{x + W_G - 4}" cy="{cy}" r="4"/>'
            ox = x + W_G
            pos[n] = (ox, cy)
        shapes.append((n, x, cy, h, pins, f'<path class="ax" style="fill:var(--surface)" d="{d}"/>{extra}{bub}', base))
    wires = []
    for n, x, cy, h, pins, svg, base in shapes:
        t, s, c, _ = g[n]
        for k, src in enumerate(s):
            if src in iy:
                sx, sy = 58, iy[src]
            else:
                sx, sy = pos[src]
            tx = x
            if base in ("OR", "XOR"):
                dep = 0.14 * W_G * (1 - ((pins[k] - cy) / (h / 2)) ** 2)
                tx = x + dep - (7 if base == "XOR" else 0)
            ty = pins[k]
            mx = x - 12 - 5 * k
            if (n, k) in feedback:
                ym = feedback[(n, k)]
                d = f"M{sx},{sy} H{sx + 14} V{ym} H{mx} V{ty} H{tx}"
            else:
                d = f"M{sx},{sy} H{mx} V{ty} H{tx}"
            wires.append({"d": d, "s": src, "dot": [mx, sy] if (readers.get(src, 0) > 1 and src not in iy) else None})
    for nm, y in inputs:
        wires.append({"d": f"M50,{y} H58", "s": nm, "dot": None})
    out_wires = []
    xmax = max(p[0] for p in pos.values())
    for o in outs:
        ox, oy = pos[o]
        out_wires.append({"d": f"M{ox},{oy} H{xmax + 30}", "s": o, "x": xmax + 30, "y": oy})
    W = xmax + 30 + 86
    H = max([cy + h / 2 for _, _, cy, h, _, _, _ in shapes] + [y for _, y in inputs]) + 24
    return {"w": W, "h": H, "inputs": [{"n": n, "y": y} for n, y in inputs], "gates": [{"n": n, "x": x, "cy": cy, "h": h, "svg": svg, "ox": pos[n][0]} for n, x, cy, h, pins, svg, base in shapes],
            "wires": wires, "outs": out_wires, "outset": set(outs),
            "net": [[n, t, s] for n, t, s, c, cy in gates], "in": [n for n, _ in inputs]}


def circ_svg(geom, vals=None, label_gates=True, cap=""):
    """Static SVG of a circuit geometry. vals (dict name -> 0/1) colours wires."""
    def cls(s):
        if not vals:
            return "w"
        return "w on" if vals.get(s) else "w off"

    o = f'<svg viewBox="0 0 {geom["w"]} {geom["h"]}" style="width:{geom["w"] * 1.2:.0f}px;max-width:100%;display:block" role="img" aria-label="{cap}">'
    for w in geom["wires"]:
        o += f'<path class="{cls(w["s"])}" d="{w["d"]}"/>'
        if w["dot"]:
            o += f'<circle class="dot" cx="{w["dot"][0]}" cy="{w["dot"][1]}" r="3.2"/>'
    for w in geom["outs"]:
        o += f'<path class="{cls(w["s"])}" d="{w["d"]}"/>'
    for g in geom["gates"]:
        o += g["svg"]
        if label_gates and g["n"] not in geom["outset"]:
            o += f'<text class="sm" x="{g["ox"] + 4}" y="{g["cy"] - 7}">{g["n"]}</text>'
    for i in geom["inputs"]:
        o += f'<text class="lbl bd" x="2" y="{i["y"] + 4}">{i["n"]}</text>'
    for w in geom["outs"]:
        o += f'<text class="lbl bd" x="{w["x"] + 6}" y="{w["y"] + 4}">{w["s"]}</text>'
    return o + "</svg>"


def circ_html(geom, vals=None, cap=""):
    return f'<div class="circ">{circ_svg(geom, vals, cap=cap)}</div>'


def gjson(geom):
    """Geometry for the JS drawer (sets turned into lists)."""
    d = dict(geom)
    d["outset"] = sorted(geom["outset"])
    return json.dumps(d)


def evalnet(geom, inp, state=None):
    """Evaluate a netlist for input dict inp. Returns dict of every signal. Feedback nets iterate from state."""
    v = dict(inp)
    for n, *_ in geom["net"]:
        v[n] = (state or {}).get(n, 0)
    for _ in range(8):
        for n, t, s in geom["net"]:
            a = [v[x] for x in s]
            t = t.upper()
            if t.startswith("N") and t != "NOT":
                base = t[1:]
            else:
                base = t
            if base == "AND":
                r = int(all(a))
            elif base == "OR":
                r = int(any(a))
            elif base == "XOR":
                r = sum(a) % 2
            else:
                r = 1 - a[0]
            if t in ("NAND", "NOR", "XNOR"):
                r = 1 - r
            v[n] = r
    return v


def circ_table(geom, work=(), outs=None, extra=None):
    """Truth table by evaluating the netlist: input columns, working columns, output columns."""
    ins = geom["in"]
    outs = outs or sorted(geom["outset"], key=lambda n: [g[0] for g in geom["net"]].index(n))
    rows = []
    for m in range(1 << len(ins)):
        b = bits(m, len(ins))
        v = evalnet(geom, dict(zip(ins, b)))
        rows.append(b + [v[w] for w in work] + [v[o] for o in outs])
    return ttable(ins, list(work) + list(outs), rows), rows


AK15JS = r'''
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
'''

AK15JS += r'''
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
'''

AK15CSS = r'''
.ob{display:inline-block;border-top:1.5px solid currentColor;line-height:1.05;padding-top:0}
.bx{font-family:var(--mono);font-size:.92em;white-space:nowrap}
svg .w{stroke:var(--muted);stroke-width:2;fill:none}
svg .w.on{stroke:var(--good);stroke-width:3.2}
svg .w.off{stroke:var(--muted);stroke-width:2;opacity:.75}
svg .dot{fill:var(--ink)}
.circ{margin:8px 0}
table.km{border-collapse:collapse;margin:8px 0;font-family:var(--mono)}
table.km th{padding:6px 12px;font:700 .8rem var(--mono);color:var(--muted);text-align:center}
table.km td{width:62px;height:46px;border:1px solid var(--line);text-align:center;position:relative;background:var(--surface)}
table.km td .v{font-size:1.15rem;font-weight:700}
table.km td .n{position:absolute;right:4px;bottom:1px;font-size:.62rem;color:var(--muted)}
.kleg{font-size:.9rem}.kg{display:inline-block;border:2.5px solid var(--c);border-radius:6px;padding:1px 8px;margin-right:6px;font-family:var(--mono)}
'''

def same(f, g, nv):
    """Brute-force check that two Boolean functions agree on every input."""
    return all(f(*bits(m, nv)) == g(*bits(m, nv)) for m in range(1 << nv))


def chk(mins, names, expected):
    """Assert the K-map groups match the mark scheme's terms (order ignored)."""
    got = {term(p, names) for p, _ in prime_cover(mins, len(names))}
    assert got == set(expected), (mins, got, expected)
