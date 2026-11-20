"""Split a lesson into a Basic part and the Full-only panels (practise, exam questions, tips).

Full panels' HTML and the script statements that fill them (Lib.quiz($("#qz1"), ...), drill IIFEs, helper
functions only they use) move to a second payload under a Full-only key, so a Basic account never receives the
practice content. split(html) returns None when a lesson can't be split safely; those stay whole.
"""
import re

FULL = ("practise", "exam", "tips", "past", "bank")  # panel ids that belong to Full when a lesson has them
OPEN = r'<section id="%s" role="tabpanel"[^>]*>'
DECL = re.compile(r"^(?:async\s+)?(?:function\*?|class)\s+([\w$]+)|^(?:const|let|var)\s+([\w$]+)")


def _panel(html, pid):
    """(start, end) of the whole <section> for panel pid, matching nested sections; None if absent."""
    m = re.search(OPEN % pid, html)
    if not m:
        return None
    depth, pos = 1, m.end()
    for t in re.finditer(r"<section\b|</section>", html[pos:]):
        depth += 1 if t.group(0) == "<section" else -1
        if depth == 0:
            return m.start(), pos + t.end()
    return None


def _end(js, i):
    """Index just past the statement starting at i: bracket-balanced, aware of strings, template literals, comments
    and regex literals. Declarations of functions and classes end at their closing brace; everything else at a ';'
    at depth 0."""
    head = re.match(r"(?:async\s+)?(?:function\*?|class)\b", js[i:])
    blk = None if head else re.match(r"(?:if|for|while|try|switch)\b|\{", js[i:])
    n, depth, seen, prev = len(js), 0, False, ""
    tpl = []  # brace depths at which a template literal's ${ ... } was entered
    while i < n:
        c = js[i]
        if c == "/" and js[i + 1:i + 2] == "/":
            i = js.find("\n", i)
            if i < 0:
                return None
            continue
        if c == "/" and js[i + 1:i + 2] == "*":
            i = js.find("*/", i + 2)
            if i < 0:
                return None
            i += 2
            continue
        if c in "\"'":
            j = i + 1
            while j < n and js[j] != c:
                j += 2 if js[j] == "\\" else 1
            i, prev = j + 1, "x"
            continue
        if c == "`" or (c == "}" and tpl and tpl[-1] == depth):
            if c == "}":
                tpl.pop()
                depth -= 1
            j, step = i + 1, 1
            while j < n and js[j] != "`":
                if js[j] == "\\":
                    j += 2
                elif js[j] == "$" and js[j + 1:j + 2] == "{":
                    depth += 1
                    tpl.append(depth)
                    step = 2
                    break
                else:
                    j += 1
            i, prev = j + step, "x"
            continue
        if c == "/" and (prev == "" or prev in "(,=:[!&|?{};+-*%<>~^"):
            j = i + 1
            cls = False
            while j < n and js[j] != "\n":
                if js[j] == "\\":
                    j += 1
                elif js[j] == "[":
                    cls = True
                elif js[j] == "]":
                    cls = False
                elif js[j] == "/" and not cls:
                    break
                j += 1
            i, prev = j + 1, "x"
            continue
        if c in "([{":
            depth += 1
            seen = seen or c == "{"
        elif c in ")]}":
            depth -= 1
            if head and seen and depth == 0 and c == "}":
                return i + 1
            if blk and depth == 0 and c == "}" and not re.match(r"\s*(?:else|catch|finally|while)\b", js[i + 1:]):
                return i + 1
        elif c == ";" and depth == 0 and not head:
            return i + 1
        if not c.isspace():
            prev = c
        i += 1
    return None


def split(html):
    spans = {p: _panel(html, p) for p in FULL}
    spans = {p: s for p, s in spans.items() if s}
    if not {"practise"} & set(spans):
        return None
    panels, ids = {}, set()
    for p, (a, b) in spans.items():
        inner = re.match(OPEN % p, html[a:b]).end()
        panels[p] = html[a + inner:b - len("</section>")]
        ids |= set(re.findall(r'\bid="([^"]+)"', panels[p]))
    # An id that is also used outside the Full panels (a duplicate) is resolved by the first match, which is outside.
    outside = html
    for a, b in sorted(spans.values(), reverse=True):
        outside = outside[:a] + outside[b:]
    ids = {i for i in ids if f'id="{i}"' not in outside}
    scripts = list(re.finditer(r"<script>(.*?)</script>", html, re.S))
    if not scripts:
        return None
    sm = max(scripts, key=lambda m: len(m.group(1)))
    js = sm.group(1)
    alt = "|".join(map(re.escape, ids)) or "(?!)"
    # An id is referenced as $("#id"), $("id"), getElementById("id") or inside a selector string ("#id .x"); ids that are
    # also used outside the Full panels were excluded above.
    ref = re.compile(r"""\$\(\s*["']#?(?:%s)["']\s*\)|getElementById\(\s*["'](?:%s)["']|["'`][^"'`\n]*#(?:%s)(?![\w-])|[\w$]\(\s*["'](?:%s)["']\s*,""" % (alt, alt, alt, alt))
    stmts, cur = [], 0
    skip = re.compile(r"(?:\s+|//[^\n]*|/\*.*?\*/)*", re.S)
    while True:
        cur = skip.match(js, cur).end()
        if cur >= len(js):
            break
        e = _end(js, cur)
        if e is None:
            return None  # can't tell where statements end: leave the lesson whole
        stmts.append([cur, e, bool(ref.search(js[cur:e]))])
        cur = e
    # Statements that use a moved helper or constant (renderBank(); ...) must move with it.
    names, done = [], set()
    while True:
        for st in stmts:
            if st[2] and id(st) not in done:
                done.add(id(st))
                d = DECL.match(js[st[0]:st[1]])
                if d:
                    names.append(d.group(1) or d.group(2))
        pat = re.compile(r"(?<![\w$.])(?:%s)(?![\w$])" % "|".join(map(re.escape, names))) if names else None
        grew = False
        for st in stmts:
            if pat and not st[2] and pat.search(js[st[0]:st[1]]):
                st[2] = grew = True
        if not grew:
            break
    moved, out, pos = [], [], 0
    for a0, e0, mv in stmts:
        if mv:
            out.append(js[pos:a0])
            moved.append(js[a0:e0])
            pos = e0
    out.append(js[pos:])
    rest = "".join(out)
    if ref.search(rest):
        return None
    rest = rest.rstrip() + "\n/*@@FULL@@*/\n"
    base = html
    for p, (a, b) in sorted(spans.items(), key=lambda kv: -kv[1][0]):
        o = re.match(OPEN % p, base[a:b]).group(0)
        base = base[:a] + o + '\n<div class="fulllock" data-lock="%s"></div>\n</section>' % p + base[b:]
    base = base.replace(sm.group(1), rest, 1)
    return base, {"panels": panels, "js": "\n".join(moved)}
