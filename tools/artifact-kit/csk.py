"""Shared pieces for the IGCSE Computer Science (0478) exam technique pages: source labels, exam table, code blocks, trace-table and truth-table helpers."""
import html as _h
from as6k import *

_CM = {"m": "Feb/March", "s": "May/June", "w": "Oct/Nov"}
EYC = "IGCSE Computer Science · 0478 · Exam technique"


def CP(code, q):
    """Source line for a written question: CP('w24_21', '6(a)') -> 'Based on Oct/Nov 2024 · 0478/21 · Q6(a)'."""
    ser, var = code.split("_")
    return f"Based on {_CM[ser[0]]} 20{ser[1:]} · 0478/{var} · Q{q}"


def clabel(code, q):
    ser, var = code.split("_")
    return f"{_CM[ser[0]]} 20{ser[1:]} ({var}) Q{q}"


CSKEY = '<div class="key"><span class="k"><i></i>Technical knowledge (K)</span><span class="a"><i></i>Applied to the context (A)</span></div>\n'


def ceq(src, marks, q, bullets, plan, ans=None):
    """One reworded exam question, like syl.eq but with a two-colour key (technical term / applied to the scenario)."""
    h = f'  <details class="eq"><summary>{src} <span class="mark">{marks}</span> {q}</summary><div class="body">\n'
    h += '    <div class="tip"><b class="h">What the mark scheme wants</b>\n      <ul>\n' + "".join(f"        <li>{b}</li>\n" for b in bullets) + '      </ul></div>\n'
    h += f'    <div class="tip"><b class="h">Plan</b>{plan}</div>\n'
    if ans:
        h += "    " + CSKEY + '    <div class="ans">\n'
        for para in ans:
            h += "    <p>" + " ".join(f'<span class="mk {k}" data-t="{k.upper()}">{t}</span>' for k, t in para) + "</p>\n"
        h += "    </div>\n"
    return h + "  </div></details>\n"


def crows(items):
    """Header rows for the exam table from (code, part, marks) items actually shown, so counts and sources match."""
    p1 = [(c, q, m) for c, q, m in items if c.split("_")[1][0] == "1"]
    p2 = [(c, q, m) for c, q, m in items if c.split("_")[1][0] == "2"]
    rows = []
    for name, grp in (("Paper 1 written questions", p1), ("Paper 2 written questions", p2)):
        if grp:
            rows.append((name, f"{len(grp)} shown below", "; ".join(f"{clabel(c, q)} [{m}]" for c, q, m in grp)))
    return rows


def cs_exam(title, intro, rows, qs, pre=""):
    t = f'  <h2>Past paper questions on {title}</h2>\n  <p>{intro}</p>\n  <div class="tw"><table class="t">\n    <tr><th>Type</th><th>Examples found</th><th>Where</th></tr>\n'
    t += "".join(f"    <tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>\n" for a, b, c in rows) + "  </table></div>\n"
    t += pre + '  <h2>Written questions (reworded)</h2>\n  <p>The wording, context and figures are our own, so they are safe to set as practice. The source paper is named for reference. Mark scheme points are in our own words. Open a question, plan an answer, then read the mark scheme points.</p>\n' + "".join(qs)
    return t


def code(lines, start=1, label=None):
    """Static pseudocode block with line numbers. lines: list of strings (kept as written)."""
    body = "".join(f'<span class="ln">{_h.escape(l) or " "}</span>' for l in lines)
    cap = f'<p class="note" style="margin:6px 0 2px">{label}</p>' if label else ""
    return f'{cap}<div class="code"><pre class="cp" style="counter-reset:l {start - 1}">{body}</pre></div>\n'


def qc(lines):
    """Pseudocode shown inside a question summary (escaped, numbered like the exam's own line numbers are not)."""
    return '<pre class="cp" style="margin:8px 0">' + "".join(f'<span class="ln">{_h.escape(l) or " "}</span>' for l in lines) + "</pre>"


def table(heads, rows, cls="t"):
    h = '<div class="tw"><table class="' + cls + '">\n    <tr>' + "".join(f"<th>{x}</th>" for x in heads) + "</tr>\n"
    h += "".join("    <tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>\n" for r in rows)
    return h + "  </table></div>\n"


def bits(n, w=8):
    return format(n, f"0{w}b")


# Small shared JS: render a truth table from an inputs list and an evaluator.
TTJS = '''
function ttHtml(names, out, f, hl = {}) {
  const n = names.length, rows = [];
  for (let i = 0; i < 1 << n; i++) { const v = names.map((_, k) => (i >> (n - 1 - k)) & 1); rows.push(v.concat(f(...v) ? 1 : 0)); }
  return `<div class="tw"><table class="t mx"><tr>${names.concat(out).map((h) => `<th>${h}</th>`).join("")}</tr>${rows.map((r, i) => `<tr>${r.map((c, k) => `<td class="${k === n ? (c ? "on" : "z") : ""}">${c}</td>`).join("")}</tr>`).join("")}</table></div>`;
}
function ttRows(names, f) {
  const n = names.length, rows = [];
  for (let i = 0; i < 1 << n; i++) { const v = names.map((_, k) => (i >> (n - 1 - k)) & 1); rows.push(f(...v) ? 1 : 0); }
  return rows;
}
'''

PICKJS = '''
function pick(id, items, render) {
  const B = $("#" + id + "B"), O = $("#" + id + "O");
  B.innerHTML = items.map((t, i) => `<button class="b" data-i="${i}">${t.label}</button>`).join("");
  const show = (i) => { $$("button", B).forEach((b, k) => b.classList.toggle("pri", k === i)); O.innerHTML = render(items[i]); };
  $$("button", B).forEach((b) => (b.onclick = () => show(+b.dataset.i)));
  show(0);
}
const scoreBar = (m, max) => `<div style="background:var(--soft);border-radius:7px;height:14px;margin:6px 0 2px"><div class="bar ${m === max ? "b3" : m === 0 ? "b2" : "b4"}" style="width:${Math.max(2, (m / max) * 100)}%"></div></div><small>${m} of ${max} marks</small>`;
'''
