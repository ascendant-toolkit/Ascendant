"""Split a lesson into a Basic part and the Full-only panels (practise, exam, tips).

Full panels' HTML and the script statements that fill them (Lib.quiz($("#qz1"), ...)) move to a second payload
that is encrypted under a Full-only key, so a Basic account never receives the practice content.
split(html) returns None when a lesson doesn't have the standard layout; those stay whole.
"""
import re

FULL = ("practise", "exam", "tips")
PANEL = r'<section id="%s" role="tabpanel"[^>]*>(.*?)\n</section>'


def _end(js, i):
    """Index just past the statement starting at i: bracket-balanced, string-aware, ends at a ';' at depth 0."""
    depth, n, q = 0, len(js), None
    while i < n:
        c = js[i]
        if q:
            if c == "\\":
                i += 1
            elif c == q:
                q = None
        elif c in "\"'`":
            q = c
        elif c in "([{":
            depth += 1
        elif c in ")]}":
            depth -= 1
        elif c == ";" and depth == 0:
            return i + 1
        i += 1
    return None


def split(html):
    panels, ids = {}, set()
    for p in FULL:
        m = re.search(PANEL % p, html, re.S)
        if not m or "<section" in m.group(1):
            return None
        panels[p] = m.group(1)
        ids |= set(re.findall(r'\bid="([^"]+)"', m.group(1)))
    scripts = list(re.finditer(r"<script>(.*?)</script>", html, re.S))
    if not scripts:
        return None
    sm = max(scripts, key=lambda m: len(m.group(1)))  # the lesson's own script; the pill/tab helpers are tiny
    js = sm.group(1)
    alt = "|".join(map(re.escape, ids))
    ref = re.compile(r"""\$\(\s*["']#(?:%s)["']|getElementById\(\s*["'](?:%s)["']""" % (alt, alt)) if ids else None
    moved, out, pos = [], [], 0
    # Statements start at the beginning of a line; take every one that mentions a Full panel id.
    for m in re.finditer(r"^(?=\S)", js, re.M):
        s = m.start()
        if s < pos:
            continue
        e = _end(js, s)
        if e is None:
            continue
        stmt = js[s:e]
        if ref and ref.search(stmt) and re.match(r"\s*(Lib\.\w+|[A-Za-z_$][\w$]*)\s*\(", stmt):
            out.append(js[pos:s])
            moved.append(stmt)
            pos = e
            continue
    out.append(js[pos:])
    rest = "".join(out).rstrip() + "\n/*@@FULL@@*/\n"
    if ref and ref.search(rest):
        return None  # something else still touches the Full panels: leave the lesson whole
    stub = '\n<div class="fulllock" data-lock="%s"></div>\n'
    base = html
    for p in FULL:
        base = re.sub(PANEL % p, lambda m, p=p: m.group(0).replace(m.group(1), stub % p), base, count=1, flags=re.S)
    base = base.replace(sm.group(1), rest, 1)
    return base, {"panels": panels, "js": "\n".join(moved)}
