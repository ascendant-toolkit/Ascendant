"""AS CS chapter 12 helpers: structure chart and state-transition diagram drawers."""
import math
from ascs import *

_N = [0]
_DEF0 = '<defs><marker id="ah" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L8,4 L0,8 z" style="fill:var(--ink,currentColor)"/></marker><marker id="ahs" viewBox="0 0 8 8" refX="1" refY="4" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L8,4 L0,8 z" style="fill:var(--ink,currentColor)"/></marker></defs>'

def _defs():
    _N[0] += 1; i = _N[0]
    return i, _DEF0.replace('id="ah"', f'id="ah{i}"').replace('id="ahs"', f'id="ahs{i}"')

def sc(nodes, links, w=520, h=300, cap="Structure chart"):
    """nodes: {id: (label, cx, cy)}; links: [(parent, child, flags, arrows)] flags in {'sel','it'} (on the parent, drawn once);
    arrows: [(dir, kind, label, t, side)] dir down/up/both, kind data/flag, t position along the link, side -1 left / +1 right."""
    BW, BH = 104, 30
    mid, dfs = _defs()
    o = f'<svg viewBox="0 0 {w} {h}" style="width:{w}px;max-width:100%;display:block" role="img" aria-label="{cap}">' + dfs
    drawn = set()
    for p, c, flags, arrows in links:
        px, py = nodes[p][1], nodes[p][2] + BH / 2
        cx, cy = nodes[c][1], nodes[c][2] - BH / 2
        o += f'<line class="w" x1="{px}" y1="{py}" x2="{cx}" y2="{cy}"/>'
        dx, dy = cx - px, cy - py; L = math.hypot(dx, dy); ux, uy = dx / L, dy / L; nx, ny = -uy, ux
        if nx < 0: nx, ny = -nx, -ny
        for d, kind, lab, t, side in arrows:
            mx, my = px + dx * t + side * 18 * nx, py + dy * t + side * 18 * ny
            a, b = (mx - ux * 12, my - uy * 12), (mx + ux * 12, my + uy * 12)
            if d == "up": a, b = b, a
            head = f' marker-end="url(#ah{mid})"' if d != "both" else f' marker-end="url(#ah{mid})" marker-start="url(#ahs{mid})"'
            o += f'<line class="ax" x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}"{head}/>'
            tail = a if d != "both" else (mx - ux * 12, my - uy * 12)
            fill = "var(--ink,currentColor)" if kind == "flag" else "var(--surface)"
            o += f'<circle class="ax" cx="{tail[0] + (ux * 0 if d != "up" else 0):.1f}" cy="{tail[1]:.1f}" r="3.5" style="fill:{fill}"/>'
            if lab:
                lx, ly = mx + side * (9 + abs(ux) * 14) * nx, my + side * (9 + abs(ux) * 14) * ny + 3
                o += f'<text class="sm" x="{lx:.1f}" y="{ly:.1f}" text-anchor="{"end" if side < 0 else "start"}" style="font-size:10px;font-weight:700">{lab}</text>'
        if p not in drawn:
            drawn.add(p)
            if "sel" in flags: o += f'<polygon class="ax" style="fill:var(--surface)" points="{px - 10},{py} {px},{py - 7} {px + 10},{py} {px},{py + 7}"/>'
    for p, c, flags, arrows in links:
        pass
    for n, (lab, cx, cy) in nodes.items():
        o += f'<rect class="ax" style="fill:var(--surface)" x="{cx - BW / 2}" y="{cy - BH / 2}" width="{BW}" height="{BH}"/><text class="lbl" x="{cx}" y="{cy + 4}" text-anchor="middle" style="font-size:11px">{lab}</text>'
    # selection diamonds and iteration arcs are re-drawn on top of the boxes
    done = set()
    for p, c, flags, arrows in links:
        if p in done: continue
        done.add(p)
        kids = [x[1] for x in links if x[0] == p]
        px, py = nodes[p][1], nodes[p][2] + BH / 2
        if "sel" in flags: o += f'<polygon class="ax" style="fill:var(--surface)" points="{px - 10},{py} {px},{py - 7} {px + 10},{py} {px},{py + 7}"/>'
        if "it" in flags:
            xs = [nodes[k][1] for k in kids]; span = min(30, (max(xs) - min(xs)) / 2 - 4) if len(xs) > 1 else 24
            o += f'<path class="ax" fill="none" d="M{px - span},{py + 13} Q{px},{py + 30} {px + span},{py + 13}" marker-end="url(#ah{mid})"/>'
    return o + "</svg>"

def sc_html(*a, **k):
    return f'<div class="circ">{sc(*a, **k)}</div>'

def std(nodes, edges, w=520, h=260, cap="State-transition diagram"):
    """nodes: {id: (cx, cy, kind)} kind s state, f final state, d start dot; edges: [(a, b, label, ctrl, (lx, ly))] where ctrl is a bend point or None
    for a straight line, or 'loop' for a self transition drawn above the state; label position is (lx, ly) with text-anchor middle."""
    R = 26
    mid, dfs = _defs()
    o = f'<svg viewBox="0 0 {w} {h}" style="width:{w}px;max-width:100%;display:block" role="img" aria-label="{cap}">' + dfs
    def rad(k): return 5 if k == "d" else R + (4 if k == "f" else 0)
    for a, b, lab, ctrl, (lx, ly) in edges:
        ax, ay, ak = nodes[a]; bx, by, bk = nodes[b]
        if ctrl == "loop":
            o += f'<path class="w" fill="none" marker-end="url(#ah{mid})" d="M{ax - 12},{ay - R + 2} C{ax - 34},{ay - R - 34} {ax + 34},{ay - R - 34} {ax + 12},{ay - R + 2}"/>'
        elif ctrl == "loopd":
            o += f'<path class="w" fill="none" marker-end="url(#ah{mid})" d="M{ax - 12},{ay + R - 2} C{ax - 34},{ay + R + 34} {ax + 34},{ay + R + 34} {ax + 12},{ay + R - 2}"/>'
        else:
            tx, ty = (ctrl if ctrl else (bx, by))
            ux, uy = tx - ax, ty - ay; L = math.hypot(ux, uy); sx, sy = ax + ux / L * rad(ak), ay + uy / L * rad(ak)
            vx, vy = (tx - bx, ty - by) if ctrl else (ax - bx, ay - by); M = math.hypot(vx, vy); ex, ey = bx + vx / M * (rad(bk) + 2), by + vy / M * (rad(bk) + 2)
            if ctrl: o += f'<path class="w" fill="none" marker-end="url(#ah{mid})" d="M{sx:.1f},{sy:.1f} Q{tx},{ty} {ex:.1f},{ey:.1f}"/>'
            else: o += f'<line class="w" marker-end="url(#ah{mid})" x1="{sx:.1f}" y1="{sy:.1f}" x2="{ex:.1f}" y2="{ey:.1f}"/>'
        if lab: o += f'<text class="sm" x="{lx}" y="{ly}" text-anchor="middle" style="font-size:10px;font-weight:700">{lab}</text>'
    for n, (cx, cy, k) in nodes.items():
        if k == "d": o += f'<circle cx="{cx}" cy="{cy}" r="5" style="fill:var(--ink,currentColor)"/>'; continue
        o += f'<circle class="ax" data-n="{n}" style="fill:var(--surface)" cx="{cx}" cy="{cy}" r="{R}"/>'
        if k == "f": o += f'<circle class="ax" fill="none" cx="{cx}" cy="{cy}" r="{R - 5}"/>'
        parts = n.split(" ") if len(n) >= 8 else [n]
        for i, t in enumerate(parts): o += f'<text class="lbl" x="{cx}" y="{cy + 4 + (i - (len(parts) - 1) / 2) * 12:.1f}" text-anchor="middle" style="font-size:10px">{t}</text>'
    return o + "</svg>"

def std_html(*a, **k):
    return f'<div class="circ">{std(*a, **k)}</div>'
