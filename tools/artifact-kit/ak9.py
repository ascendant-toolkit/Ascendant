"""AS CS chapter 9 helpers: a small program-flowchart drawer (terminator, process, input/output, decision, subroutine call) with orthogonal arrows."""
from ascs import *

_KW = {"term": (110, 30), "proc": (170, 40), "io": (170, 40), "dec": (150, 62), "call": (170, 40)}

def flow(nodes, edges, w=520, h=420, cap="Flowchart"):
    """nodes: {id: (kind, label, cx, cy)}; edges: [(a, pa, b, pb, via, label, label_xy)] with ports t/b/l/r and via = [(x, y)...]."""
    def box(n):
        k, lab, cx, cy = nodes[n][:4]; ww, hh = _KW[k]
        if len(nodes[n]) > 4: ww, hh = nodes[n][4]
        return k, lab, cx, cy, ww, hh

    def port(n, p):
        k, lab, cx, cy, ww, hh = box(n)
        return {"t": (cx, cy - hh / 2), "b": (cx, cy + hh / 2), "l": (cx - ww / 2, cy), "r": (cx + ww / 2, cy)}[p]
    o = f'<svg viewBox="0 0 {w} {h}" style="width:{w}px;max-width:100%;display:block" role="img" aria-label="{cap}"><defs><marker id="ah" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L8,4 L0,8 z" style="fill:var(--ink,currentColor)"/></marker></defs>'
    for a, pa, b, pb, via, lab, lxy in edges:
        pts = [port(a, pa)] + list(via) + [port(b, pb)]
        o += '<polyline class="w" fill="none" marker-end="url(#ah)" points="' + " ".join(f"{x:.0f},{y:.0f}" for x, y in pts) + '"/>'
        if lab: o += f'<text class="sm" x="{lxy[0]}" y="{lxy[1]}" style="font-size:10px;font-weight:700">{lab}</text>'
    for n in nodes:
        k, lab, cx, cy, ww, hh = box(n); x, y = cx - ww / 2, cy - hh / 2
        st = 'class="ax" style="fill:var(--surface)"'
        if k == "term": o += f'<rect {st} x="{x}" y="{y}" width="{ww}" height="{hh}" rx="{hh / 2}"/>'
        elif k == "proc": o += f'<rect {st} x="{x}" y="{y}" width="{ww}" height="{hh}"/>'
        elif k == "call": o += f'<rect {st} x="{x}" y="{y}" width="{ww}" height="{hh}"/><line class="ax" x1="{x + 8}" y1="{y}" x2="{x + 8}" y2="{y + hh}"/><line class="ax" x1="{x + ww - 8}" y1="{y}" x2="{x + ww - 8}" y2="{y + hh}"/>'
        elif k == "io": o += f'<polygon {st} points="{x + 14},{y} {x + ww},{y} {x + ww - 14},{y + hh} {x},{y + hh}"/>'
        else: o += f'<polygon {st} points="{cx},{y} {x + ww},{cy} {cx},{y + hh} {x},{cy}"/>'
        lines = lab.split("\n"); fs = 10 if k != "dec" else 10
        for i, t in enumerate(lines):
            o += f'<text class="lbl" x="{cx}" y="{cy + 3.5 + (i - (len(lines) - 1) / 2) * 12:.1f}" text-anchor="middle" style="font-size:{fs}px">{t}</text>'
    return o + "</svg>"

def flow_html(*a, **k):
    return f'<div class="circ">{flow(*a, **k)}</div>'
