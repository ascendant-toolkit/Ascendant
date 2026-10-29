"""Builds the static site into docs/ from site_data.py and artifacts_src/.

Run: python3 build.py
GitHub Pages serves the docs/ folder.
"""
import base64
import gzip
import hashlib
import hmac
import html
import json
import os
import re
import shutil
from pathlib import Path

from site_data import A_CS_MOVED, A_ECON_MOVED, ARTIFACTS, COURSES, INVESTING, LANDING_PAGE, SITE_TAGLINE, SITE_TITLE

ROOT = Path(__file__).parent
OUT = ROOT / "docs"
SRC = ROOT / "artifacts_src"

NAV = [
    ("home", "Home", ""),
    ("ig-econ", "IG Econ", "ig-econ/"),
    ("ig-cs", "IG CS", "ig-cs/"),
    ("a-econ", "A Econ", "a-econ/"),
    ("a-cs", "A CS", "a-cs/"),
    ("investing", "Investing", "investing/"),
    ("other", "Other", "other/"),
    ("profile", "Profile", "profile/"),
]

esc = html.escape


STAMP = str(int(__import__("time").time()))


def bust(text):
    """Version the site's own css/js so browsers fetch fresh copies after each build."""
    return re.sub(r'(assets/[\w.-]+\.(?:js|css))(")', r"\1?v=" + STAMP + r"\2", text)


def write(rel, content):
    if rel.endswith(".html"):
        content = bust(content)
    p = OUT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")


def rel_root(path):
    """Relative prefix back to site root for a page at path like 'a-cs/as/ch-01/'."""
    depth = len([x for x in path.split("/") if x])
    return "../" * depth


def layout(title, body, path, active, crumbs=None, accent=None, auth=False, extra=""):
    root = rel_root(path)
    nav = "".join(
        f'<a href="{root}{href}"{" class=on aria-current=page" if key == active else ""}{f" data-course={key}" if key in COURSES else ""}{" data-admin hidden" if key == "investing" else ""}>{label}</a>'
        for key, label, href in NAV
    )
    crumb_html = ""
    if crumbs:
        parts = []
        for label, href in crumbs:
            parts.append(f'<a href="{root}{href}">{esc(label)}</a>' if href is not None else f"<span>{esc(label)}</span>")
        crumb_html = f'<nav class="crumbs" aria-label="Breadcrumb">{"<i>/</i>".join(parts)}</nav>'
    acc = f' data-accent="{accent}"' if accent else ""
    gate = [active] if active in COURSES else (["admin"] if active == "investing" else [])
    full_title = SITE_TITLE if title == SITE_TITLE else f"{title} · {SITE_TITLE}"
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(full_title)}</title>
<link rel="stylesheet" href="{root}assets/style.css">
{favicon_links(root)}{THEME_HEAD}{GATE_HEAD if gate else ""}</head>
<body{acc}>
<header class="site">
<div class="bar">
<a class="brand" href="{root}"><img class="mark" src="{root}assets/logo.svg" alt="" width="34" height="34"><span>{esc(SITE_TITLE)}</span></a>
<button class="theme" type="button" aria-label="Toggle dark mode"></button>
<button class="menu" aria-label="Menu" aria-expanded="false">Menu</button>
<nav class="main" aria-label="Main">{nav}</nav>
</div>
</header>
<main>
{crumb_html}
{body}
</main>
<footer class="site"><p>Independent revision resource for Cambridge IGCSE and A-Level. Not affiliated with or endorsed by Cambridge University Press &amp; Assessment.</p></footer>
<script src="{root}assets/site.js"></script>
{auth_scripts(root, gate)}{extra}
</body></html>
"""


def favicon_links(root):
    return (f'<link rel="icon" type="image/svg+xml" href="{root}assets/favicon.svg">'
            f'<link rel="icon" type="image/png" sizes="48x48" href="{root}assets/favicon-48.png">'
            f'<link rel="apple-touch-icon" href="{root}assets/apple-touch-icon.png">\n')


THEME_HEAD = ('<script>try{var t=localStorage.getItem("site.theme");if(t)document.documentElement.setAttribute("data-theme",t)}catch(e){}</script>')
GATE_HEAD = ('<script>document.documentElement.classList.add("gated")</script>'
             '<style>html.gated{visibility:hidden!important}</style>')


def auth_scripts(root, gate=()):
    return (f'<script src="{root}assets/config.js"></script>'
            '<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>'
            f'<script src="{root}assets/app.js"></script>'
            f'<script src="{root}assets/gate.js" data-courses="{",".join(gate)}"></script>')


def plural(n, word):
    if word == "activity":
        return f"{n} activit{'y' if n == 1 else 'ies'}"
    return f"{n} {word}{'' if n == 1 else 's'}"


# Index chapters -> path, and artifacts -> chapters.
chapter_info = {}  # (course, key) -> dict(path, title, crumbs, chapter)
for ckey, c in COURSES.items():
    if c["kind"] == "chapters":
        for ch in c["chapters"]:
            chapter_info[(ckey, ch["id"])] = {"path": f"{ckey}/{ch['id']}/", "ch": ch, "parents": []}
    elif c["kind"] == "sections":
        for sec in c["sections"]:
            for ch in sec["chapters"]:
                chapter_info[(ckey, ch["id"])] = {
                    "path": f"{ckey}/{sec['id']}/{ch['id']}/", "ch": ch,
                    "parents": [(f"Topic {sec['n']}: {sec['title']}", f"{ckey}/{sec['id']}/")],
                }
    else:
        for lv in c["levels"]:
            for ch in lv["chapters"]:
                chapter_info[(ckey, f"{lv['id']}/{ch['id']}")] = {
                    "path": f"{ckey}/{lv['id']}/{ch['id']}/", "ch": ch,
                    "parents": [(lv["title"], f"{ckey}/{lv['id']}/")],
                }

# Investing: a single flat page, so one pseudo-chapter that points at the topic page itself.
chapter_info[("investing", "all")] = {"path": "investing/", "ch": {"n": None, "label": "★", "title": "Investing", "group": None}, "parents": []}

by_chapter = {}
for a in ARTIFACTS:
    a["slug"] = a["src"]
    for place in a["places"]:
        assert place in chapter_info, f"Unknown placement {place} for {a['src']}"
        by_chapter.setdefault(place, []).append(a)
    assert (SRC / a["src"] / "index.html").exists(), a["src"]


def is_review(a):
    return a.get("role") == "review"


def at_key(a):
    return [int(x) for x in a["at"].split(".")] if a.get("at") else [10**6]


for _l in by_chapter.values():
    _l.sort(key=at_key)  # stable, so unplaced resources keep their listed order


def count(keys, review=None):
    seen = {a["slug"] for k in keys for a in by_chapter.get(k, []) if review is None or is_review(a) == review}
    return len(seen)


def card(href, label, title, sub="", n=None, group=None, res=None):
    badge = ""
    if n is not None:
        badge = f'<span class="count{" zero" if n == 0 else ""}">{plural(n, "activity")}</span>'
        if n == 0:
            badge = '<span class="count zero">Coming soon</span>'
    if res is not None:
        rev, extra = res
        parts = ([f"{rev} review"] if rev else []) + ([plural(extra, "resource")] if extra else [])
        badge = f'<span class="count">{" · ".join(parts)}</span>' if parts else '<span class="count zero">Coming soon</span>'
        n = rev + extra
    subh = f'<span class="sub">{esc(sub)}</span>' if sub else ""
    return (f'<a class="card{" empty" if n == 0 else ""}" href="{href}">'
            f'<span class="num">{esc(label)}</span><span class="t">{esc(title)}</span>{subh}{badge}</a>')


def chapter_grid(ckey, prefix, chapters, root_key=lambda ch: ch["id"], grouped=False):
    """Grid of chapter cards; hrefs are relative to the page (chapter id folder)."""
    def one(ch):
        k = [(ckey, root_key(ch))]
        return card(f"{ch['id']}/", ch["label"], ch["title"], res=(count(k, True), count(k, False)))

    if not grouped:
        return f'<div class="grid">{"".join(one(ch) for ch in chapters)}</div>'
    out, current, cards = [], object(), []
    for ch in chapters:
        if ch["group"] != current:
            if cards:
                out.append(f'<div class="grid">{"".join(cards)}</div>')
            current = ch["group"]
            if current:
                out.append(f'<h2 class="group">{esc(current)}</h2>')
            cards = []
        cards.append(one(ch))
    out.append(f'<div class="grid">{"".join(cards)}</div>')
    return "".join(out)


def head(title, lead, kicker=None):
    k = f'<p class="kicker">{esc(kicker)}</p>' if kicker else ""
    return f'<section class="hero small">{k}<h1>{esc(title)}</h1><p class="lead">{esc(lead)}</p></section>'


def chapter_label(ch, fallback):
    """'Syllabus 7.7' for syllabus-numbered chapters, 'Chapter 5' for coursebook-numbered ones."""
    if not ch["n"]:
        return fallback
    return f"{'Syllabus' if ch.get('syl') else 'Chapter'} {ch['label']}"


def chapter_page(ckey, key):
    info = chapter_info[(ckey, key)]
    c, ch = COURSES[ckey], info["ch"]
    arts = by_chapter.get((ckey, key), [])
    label = chapter_label(ch, "Exam preparation")
    revs = [a for a in arts if is_review(a)]
    ress = [a for a in arts if not is_review(a)]

    def cardh(a):
        u = f'{rel_root(info["path"])}artifacts/{a["slug"]}/'
        return (f'<div class="card art" data-slug="{a["slug"]}" data-role="{"review" if is_review(a) else "resource"}" data-ord="{arts.index(a)}">'
                f'<span class="tag">{esc(a["kind"])}</span><a class="t" href="{u}">{esc(a["title"])}</a><span class="sub">{esc(a["desc"])}</span>'
                f'<span class="foot"><a class="go" href="{u}">Open →</a><button class="done" data-done-slug="{a["slug"]}" hidden></button></span>'
                f'<span class="adm"><button class="mini roletog" data-role-toggle="{a["slug"]}" hidden></button>'
                f'<button class="mini danger roledel" data-role-delete="{a["slug"]}" hidden></button>'
                f'<button class="mini restore" data-role-restore="{a["slug"]}" hidden></button></span></div>')

    def panel(lst, review):
        msg = "No chapter review yet. It is on its way." if review else "No extra resources for this chapter yet."
        return (f'<div class="placeholder emptymsg"{" hidden" if lst else ""}><p>{msg}</p></div>'
                f'<div class="grid arts">{"".join(cardh(a) for a in lst)}</div>')

    first = "res" if ress and not revs else "rev"
    body = ('<div class="tabs chtabs" role="tablist">'
            f'<button role="tab" data-t="rev" class="{"on" if first == "rev" else ""}">Chapter review (<span>{len(revs)}</span>)</button>'
            f'<button role="tab" data-t="res" class="{"on" if first == "res" else ""}">Resources (<span>{len(ress)}</span>)</button><button role="tab" data-t="del" hidden>Deleted (<span>0</span>)</button></div>'
            f'<div class="tabpanel" data-p="rev"{" hidden" if first != "rev" else ""}>{panel(revs, True)}</div>'
            f'<div class="tabpanel" data-p="res"{" hidden" if first != "res" else ""}>'
            f'<p class="hint">Extra activities that deepen understanding or give more support. Shown in {"syllabus" if ch.get("syl") else "coursebook"} order.</p>{panel(ress, False)}</div>'
            '<div class="tabpanel" data-p="del" hidden><p class="hint">Deleted: hidden from students and progress. Only you can see this tab.</p><div class="grid arts"></div></div>')
    crumbs = [("Home", ""), (c["title"], f"{ckey}/")] + [(l, h) for l, h in info["parents"]] + [(f"{label}", None)]
    write(info["path"] + "index.html",
          layout(f"{ch['title']}", head(ch["title"], ch.get("cb", ""), f"{c['title']} · {label}") + body,
                 info["path"], ckey, crumbs, c["accent"], auth=True, extra=f'<script src="{rel_root(info["path"])}assets/chapter.js"></script>'))
    return info


def build_courses():
    for ckey, c in COURSES.items():
        crumbs = [("Home", ""), (c["title"], None)]
        if c["kind"] == "chapters":
            grid = chapter_grid(ckey, ckey, c["chapters"], grouped=any(ch["group"] for ch in c["chapters"]))
            write(f"{ckey}/index.html", layout(c["title"], head(c["title"], c["blurb"], "Course") + grid, f"{ckey}/", ckey, crumbs, c["accent"]))
            for ch in c["chapters"]:
                chapter_page(ckey, ch["id"])
        elif c["kind"] == "sections":
            cards = []
            for sec in c["sections"]:
                keys = [(ckey, ch["id"]) for ch in sec["chapters"]]
                cards.append(card(f"{sec['id']}/", str(sec["n"]), sec["title"], plural(len(sec["chapters"]), "chapter"), count(keys)))
                sub_crumbs = [("Home", ""), (c["title"], f"{ckey}/"), (f"Topic {sec['n']}", None)]
                grid = chapter_grid(ckey, ckey, sec["chapters"])
                write(f"{ckey}/{sec['id']}/index.html",
                      layout(sec["title"], head(sec["title"], f"Topic {sec['n']} of the {c['title']} syllabus.", c["title"]) + grid,
                             f"{ckey}/{sec['id']}/", ckey, sub_crumbs, c["accent"]))
                for ch in sec["chapters"]:
                    chapter_page(ckey, ch["id"])
            write(f"{ckey}/index.html", layout(c["title"], head(c["title"], c["blurb"], "Course") + f'<div class="grid">{"".join(cards)}</div>',
                                               f"{ckey}/", ckey, crumbs, c["accent"]))
        else:
            cards = []
            for lv in c["levels"]:
                keys = [(ckey, f"{lv['id']}/{ch['id']}") for ch in lv["chapters"]]
                cards.append(card(f"{lv['id']}/", "AS" if lv["id"] == "as" else "A2", lv["title"], lv["blurb"], count(keys)))
                grouped = any(ch["group"] for ch in lv["chapters"])
                grid = chapter_grid_levels(ckey, lv, grouped)
                sub_crumbs = [("Home", ""), (c["title"], f"{ckey}/"), (lv["title"], None)]
                write(f"{ckey}/{lv['id']}/index.html",
                      layout(f"{lv['title']}", head(f"{c['title']}: {lv['title']}", lv["blurb"] + ".", c["title"]) + grid,
                             f"{ckey}/{lv['id']}/", ckey, sub_crumbs, c["accent"]))
                for ch in lv["chapters"]:
                    chapter_page(ckey, f"{lv['id']}/{ch['id']}")
            if ckey in ("a-econ", "a-cs"):
                for old_path, new_path in (A_ECON_MOVED if ckey == "a-econ" else A_CS_MOVED).items():
                    target = "../" + new_path.split("/", 1)[1] + "/"
                    write(f"{ckey}/{old_path}/index.html",
                          '<!doctype html><meta charset="utf-8"><title>Moved</title>'
                          f'<meta http-equiv="refresh" content="0; url={target}"><link rel="canonical" href="{target}">'
                          f'<p>This chapter is now numbered as in the syllabus. <a href="{target}">Continue</a>.</p>')
            write(f"{ckey}/index.html", layout(c["title"], head(c["title"], c["blurb"], "Course") + f'<div class="grid two">{"".join(cards)}</div>',
                                               f"{ckey}/", ckey, crumbs, c["accent"]))


def chapter_grid_levels(ckey, lv, grouped):
    def one(ch):
        k = [(ckey, f"{lv['id']}/{ch['id']}")]
        return card(f"{ch['id']}/", ch["label"], ch["title"], sub=ch.get("cb", ""), res=(count(k, True), count(k, False)))
    if not grouped:
        return f'<div class="grid">{"".join(one(ch) for ch in lv["chapters"])}</div>'
    out, current, cards = [], object(), []
    for ch in lv["chapters"]:
        if ch["group"] != current:
            if cards:
                out.append(f'<div class="grid">{"".join(cards)}</div>')
            current = ch["group"]
            out.append(f'<h2 class="group">{esc(current or "")}</h2>')
            cards = []
        cards.append(one(ch))
    out.append(f'<div class="grid">{"".join(cards)}</div>')
    return "".join(out)


SYLLABI = [
    ("a-econ", "A-Level", "Economics", "9708"),
    ("a-cs", "A-Level", "Computer Science", "9618"),
    ("ig-econ", "IGCSE", "Economics", "0455"),
    ("ig-cs", "IGCSE", "Computer Science", "0478"),
]

SYL_BLURB = {
    "a-econ": "AS and A Level, from basic economic problems to the macroeconomy and international trade.",
    "a-cs": "AS and A Level, from data representation and hardware to algorithms, recursion and data structures.",
    "ig-econ": "Six topics of the syllabus, from the basic economic problem to the global economy.",
    "ig-cs": "Ten coursebook chapters, from data representation to programming, databases and Boolean logic.",
}

TABS = [
    ("Learn", "The chapter in plain English, built around what the exam rewards."),
    ("Watch", "Step-by-step animations that show how a diagram or process works."),
    ("Explore", "Sliders and simulations: change an input and see what moves."),
    ("Practise", "Drag-and-drop, ordering and quick quizzes with instant feedback."),
    ("Real world", "Current examples, and where each one fits in an exam answer."),
    ("Exam questions", "Past-paper style questions with model answers and mark scheme points."),
    ("Tips and keywords", "Common mistakes, command words and the key terms to know."),
]

FAQ = [
    ("Is it really free?", "Yes, for now. Everything on the site is open to registered members at no cost. Paid plans may be introduced later, and anyone on the list will be told first."),
    ("Which exam board is this for?", "Cambridge International only: IGCSE Economics 0455, IGCSE Computer Science 0478, A-Level Economics 9708 and A-Level Computer Science 9618."),
    ("How do I get access?", "Fill in the form above with your email and the subjects you study. Access is set up by hand for each subject and level, and you will get an email when it is ready."),
    ("Why only my own subjects?", "Each account is set up for the courses you actually take, so the site stays uncluttered. If you add a subject later, ask and it can be added."),
    ("Is this official Cambridge material?", "No. This is an independent resource and is not endorsed by or affiliated with Cambridge University Press &amp; Assessment. Cambridge IGCSE and Cambridge International AS &amp; A Level are trademarks of their owners."),
    ("Does it work on a phone?", "Yes. Every page works on phones, tablets and laptops, in light or dark mode."),
]


def course_stats(ckey):
    keys = [k for k in by_chapter if k[0] == ckey]
    return count(keys), sum(1 for k in keys if by_chapter[k])


def build_landing():
    """Sales-style landing page. Not built unless LANDING_PAGE is True in site_data.py; then it lives at /welcome/."""
    r = "../"
    mkt, mine = [], []
    for ckey, lvl, subj, code in SYLLABI:
        c = COURSES[ckey]
        n, chs = course_stats(ckey)
        stat = f"{plural(n, 'activity')} across {chs} chapters" if n else "In preparation"
        mkt.append(f'<article class="card syl" data-accent="{c["accent"]}"><span class="tag">{lvl}</span>'
                   f'<h3 class="t">{subj}</h3><span class="code">Cambridge {code}</span>'
                   f'<span class="sub">{SYL_BLURB[ckey]}</span>'
                   f'<span class="count">{stat}</span></article>')
        mine.append(f'<a class="card course" data-accent="{c["accent"]}" data-course="{ckey}" href="{r}{ckey}/"><span class="num">{esc(c["nav"])}</span>'
                    f'<span class="t">{esc(c["title"])}</span><span class="sub">{esc(c["blurb"])}</span>'
                    f'<span class="count">{plural(n, "activity")}</span></a>')
    total = len({a["slug"] for a in ARTIFACTS if any(p[0] in COURSES for p in a["places"])})
    tabs = "".join(f'<li><b>{t}</b><span>{d}</span></li>' for t, d in TABS)
    steps = [("Join", "Add your email and the subjects you study."),
             ("Get set up", "Your access is created for your subjects and level, and you are emailed when it is ready."),
             ("Learn and practise", "Work through chapters, take the short assessments and track your progress.")]
    steps_html = "".join(f'<li><span class="n">{i}</span><div><b>{t}</b><p>{d}</p></div></li>' for i, (t, d) in enumerate(steps, 1))
    faq = "".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in FAQ)
    subj_chks = "".join(f'<label class="chk"><input type="checkbox" name="subjects" value="{ck}"> {lvl} {subj}</label>' for ck, lvl, subj, _ in SYLLABI)
    body = f"""<div id="mine" class="mine" hidden>
<section class="hero small"><p class="kicker">Welcome back</p><h1>Your courses</h1></section>
<div class="grid two">{"".join(mine)}</div>
<p class="hint"><a href="{r}profile/">Profile and progress</a></p></div>
<div id="pitch">
<section class="hero"><p class="kicker">Cambridge IGCSE and A-Level</p>
<h1>Economics and Computer Science, made interactive.</h1>
<p class="lead">Animated explainers, hands-on activities, exam questions with model answers and quick assessments, built chapter by chapter for the Cambridge syllabuses.</p>
<p class="cta"><span class="free">Free for now!</span><a class="btn" href="#join">Join free</a><a class="btn ghost" href="{r}profile/">Sign in</a></p>
<p class="stat">{total} activities and counting</p></section>
<section class="sec" aria-labelledby="syl"><h2 id="syl">Four Cambridge syllabuses</h2>
<p class="lede">Built chapter by chapter against the syllabus, with A-Level first.</p>
<div class="grid two">{"".join(mkt)}</div></section>
<section class="sec" id="inside" aria-labelledby="ins"><h2 id="ins">What is in a chapter</h2>
<p class="lede">Chapter reviews share the same seven tabs, so you always know where to find things.</p>
<ul class="tabsum">{tabs}</ul></section>
<section class="sec" aria-labelledby="how"><h2 id="how">How it works</h2><ol class="steps">{steps_html}</ol></section>
<section class="sec join" id="join" aria-labelledby="jn"><div class="free-card"><span class="free">Free for now!</span>
<h2 id="jn">Get free access</h2>
<p class="lede">Everything is open to members at no cost while the site grows. Tell me what you study and I will set up your access by email.</p>
<form id="joinform" class="joinform" novalidate>
<label>Name<input name="name" autocomplete="name" maxlength="120" required></label>
<label>Email<input name="email" type="email" autocomplete="email" maxlength="254" required></label>
<label>I am a<select name="role"><option value="student">Student</option><option value="parent">Parent</option><option value="teacher">Teacher</option></select></label>
<fieldset><legend>Subjects</legend><div class="chks">{subj_chks}</div></fieldset>
<label class="chk consent"><input type="checkbox" name="consent" required> I am happy to be emailed about my access and about new content. No spam, and you can opt out any time.</label>
<button class="btn" type="submit">Join free</button><p class="msg" id="joinmsg" hidden></p></form></div></section>
<section class="sec" aria-labelledby="fq"><h2 id="fq">Questions</h2><div class="faq">{faq}</div></section>
<section class="sec" aria-labelledby="ab"><h2 id="ab">About</h2>
<p class="lede">Built by a practising Economics and Computer Science teacher, to give students the explanations and practice that were missing from their revision.</p></section>
</div>"""
    write("welcome/index.html", layout(SITE_TITLE, body, "welcome/", "home", extra='<script src="../assets/home.js"></script>'))


def build_home():
    cards = []
    total = len({a["slug"] for a in ARTIFACTS})
    for ckey, _, _, _ in SYLLABI:
        c = COURSES[ckey]
        n = len({a["slug"] for a in ARTIFACTS if any(p[0] == ckey for p in a["places"])})
        cards.append(f'<a class="card course" data-accent="{c["accent"]}" data-home-course="{ckey}" href="{ckey}/"><span class="num">{esc(c["nav"])}</span>'
                     f'<span class="t">{esc(c["title"])}</span><span class="sub">{esc(c["blurb"])}</span>'
                     f'<span class="count">{plural(n, "activity")}</span></a>')
    sample = next(a for a in ARTIFACTS if a.get("public"))
    body = (f'<section class="hero"><p class="kicker">GCSE and A-Level</p><h1>Economics and Computer Science, made interactive.</h1>'
            f'<p class="lead">{esc(SITE_TAGLINE)}</p><p class="stat">{total} activities and counting</p></section>'
            f'<div class="grid two">{"".join(cards)}</div>'
            '<p class="hint" id="homehint" hidden>Sign in on the <a href="profile/">Profile</a> page with the account your teacher set up to open your courses.</p>'
            f'<div class="grid two more">'
            f'<a class="card slim" id="sample" hidden href="artifacts/{sample["slug"]}/#learn"><span class="t">Try a sample lesson</span><span class="sub">{esc(sample["title"])}: open it without signing in.</span></a>'
            f'<a class="card slim" href="investing/" data-admin hidden data-accent="{INVESTING["accent"]}"><span class="t">Investing</span><span class="sub">{esc(INVESTING["blurb"])}</span></a>'
            '<a class="card slim" href="other/"><span class="t">Other</span><span class="sub">Study tips, extra-curricular activities and side projects.</span></a>'
            '<a class="card slim" href="profile/"><span class="t">Profile</span><span class="sub">Student accounts, progress and scores.</span></a>'
            '</div>')
    write("index.html", layout(SITE_TITLE, body, "", "home", extra='<script src="assets/home.js"></script>'))


def build_investing():
    arts = by_chapter.get(("investing", "all"), [])
    if arts:
        items = "".join(
            f'<div class="card art"><span class="tag">{esc(a["kind"])}</span>'
            f'<a class="t" href="../artifacts/{a["slug"]}/">{esc(a["title"])}</a><span class="sub">{esc(a["desc"])}</span>'
            f'<span class="foot"><a class="go" href="../artifacts/{a["slug"]}/">Open →</a></span></div>' for a in arts)
        grid = f'<div class="grid arts">{items}</div>'
    else:
        grid = '<div class="placeholder"><p>The first lessons are on their way.</p></div>'
    write("investing/index.html", layout("Investing", head(INVESTING["title"], INVESTING["blurb"], "Topic") + grid,
                                         "investing/", "investing", [("Home", ""), ("Investing", None)], INVESTING["accent"]))


def build_other_profile():
    ph = lambda t, s: f'<div class="card empty slim"><span class="t">{t}</span><span class="sub">{s}</span><span class="count zero">Coming soon</span></div>'
    body = (head("Other", "Things that sit outside the exam courses.", "Extras")
            + '<div class="grid">' + ph("Study tips", "How to revise, plan and manage exam season.")
            + ph("Extra-curricular activities", "Clubs, competitions and projects.") + ph("Side projects", "Things built for fun.") + "</div>")
    write("other/index.html", layout("Other", body, "other/", "other", [("Home", ""), ("Other", None)]))

    body = (head("Profile", "Your details, subjects and progress.", "Students")
            + '<div id="profile-root"><noscript>This page needs JavaScript.</noscript></div>')
    write("profile/index.html", layout("Profile", body, "profile/", "profile", [("Home", ""), ("Profile", None)],
                                       auth=True, extra='<script src="../assets/profile.js"></script>'))


def build_catalog():
    """Machine-readable course map used by the profile page for progress."""
    arts = {a["slug"]: a for a in ARTIFACTS}
    courses, artifacts = {}, {}
    for ckey, c in COURSES.items():
        if c["kind"] == "chapters":
            raw = [("Chapters", [(ch, ch["id"]) for ch in c["chapters"]])]
        elif c["kind"] == "sections":
            raw = [(f"Topic {sec['n']}: {sec['title']}", [(ch, ch["id"]) for ch in sec["chapters"]]) for sec in c["sections"]]
        else:
            raw = [(lv["title"], [(ch, f"{lv['id']}/{ch['id']}") for ch in lv["chapters"]]) for lv in c["levels"]]
        groups, slugs = [], []
        for title, chs in raw:
            items = []
            for ch, key in chs:
                allsl = [a["slug"] for a in by_chapter.get((ckey, key), [])]
                sl = [a["slug"] for a in by_chapter.get((ckey, key), []) if is_review(a)]
                for x in allsl:
                    artifacts.setdefault(x, {"title": arts[x]["title"], "url": f"artifacts/{x}/", "role": "review" if is_review(arts[x]) else "resource",
                                             "tier": arts[x].get("tier", "full"), "chapterTitle": f"{c['title']}: {ch['title']}"})
                for x in sl:
                    if x not in slugs:
                        slugs.append(x)
                items.append({"label": ch["label"], "title": ch["title"], "url": chapter_info[(ckey, key)]["path"], "slugs": sl, "all": allsl})
            groups.append({"title": title, "chapters": items})
        courses[ckey] = {"title": c["title"], "accent": c["accent"], "url": f"{ckey}/", "groups": groups, "slugs": slugs}
    for x, a in arts.items():
        artifacts.setdefault(x, {"title": a["title"], "url": f"artifacts/{x}/", "role": "review" if is_review(a) else "resource", "tier": a.get("tier", "full"), "chapterTitle": a["title"]})
    order = [a["slug"] for a in ARTIFACTS]
    assessed = {k: {"pass": v["pass_pct"], "n": len(v["questions"])} for k, v in ASSESSED.items()}
    write("assets/catalog.json", json.dumps({"courses": courses, "artifacts": artifacts, "order": order, "assessed": assessed}, separators=(",", ":")))


PILL_CSS = ("<style id=site-pill>.site-pill{position:fixed;right:12px;bottom:12px;opacity:.8;z-index:2147483000;display:flex;gap:2px;"
            "font:600 13px/1 -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:rgba(20,24,28,.88);"
            "border-radius:999px;padding:4px;box-shadow:0 2px 10px rgba(0,0,0,.25)}.site-pill a{color:#fff;text-decoration:none;"
            "padding:8px 12px;border-radius:999px;white-space:nowrap}.site-pill a:hover,.site-pill button:hover{background:rgba(255,255,255,.18)}.site-pill button{font:inherit;color:#fff;background:transparent;border:0;border-left:1px solid rgba(255,255,255,.25);border-radius:0 999px 999px 0;padding:8px 12px;cursor:pointer}.site-pill button.is-done{color:#7be0a0}"
            "@media print{.site-pill{display:none}}"
            # Phones: collapse to a small round button so the pill never sits over lesson content.
            ".site-pill .pill-more{display:none}"
            "@media(max-width:700px){body{padding-bottom:64px}.site-pill{right:8px;bottom:8px;opacity:.6;flex-wrap:wrap;justify-content:flex-end;max-width:calc(100vw - 16px)}"
            ".site-pill>*:not(.pill-more){display:none}.site-pill.open{opacity:.95}.site-pill.open>*:not(.pill-more):not([hidden]){display:inline-block}"
            ".site-pill .pill-more{display:block;border:0;border-radius:999px;width:36px;height:36px;padding:0;text-align:center;font-size:18px}.site-pill.open .pill-more{border-left:0}}</style>")


THEME_CLICK = ("var r=document.documentElement,d=(r.getAttribute('data-theme')||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'))==='dark'?'light':'dark';"
               "r.setAttribute('data-theme',d);try{localStorage.setItem('site.theme',d)}catch(e){}")


# Assessments: assessments/<slug>.json. Answer keys never reach the site; they go into supabase/assessments_seed.sql.
ASSESSED = {}
for f in sorted((ROOT / "assessments").glob("*.json")):
    d = json.loads(f.read_text(encoding="utf-8"))
    assert d["slug"] in {a["slug"] for a in ARTIFACTS}, f"{f.name}: no such artifact"
    ids = [q["id"] for q in d["questions"]]
    assert len(ids) == len(set(ids)), f"{f.name}: duplicate question ids"
    for q in d["questions"]:
        assert q["type"] in ("mcq", "num", "text") and q.get("marks", 0) >= 1, f"{f.name} {q['id']}"
        if q["type"] == "mcq":
            assert 0 <= int(q["ans"]) < len(q["opts"]), f"{f.name} {q['id']}"
        if q["type"] == "text":
            assert q["marks"] <= len(q["groups"]), f"{f.name} {q['id']}: more marks than groups"
    ASSESSED[d["slug"]] = d


def build_assessments():
    page = (head("Assessment", "Answer from memory, then submit to see your score and feedback.", "Students")
            + '<div id="assess-root"><noscript>This page needs JavaScript.</noscript></div>')
    write("assess/index.html", layout("Assessment", page, "assess/", "profile", [("Home", ""), ("Profile", "profile/"), ("Assessment", None)],
                                      auth=True, extra='<script src="../assets/assessment.js"></script>'))
    seed = ["-- Generated by build.py from assessments/*.json. Run schema.sql first. Safe to run again: it replaces the questions.\n"]
    for d in ASSESSED.values():
        body = json.dumps(d["questions"], ensure_ascii=False)
        assert "$q$" not in body
        seed.append(f"insert into public.assessments (slug, title, pass_pct, questions) values "
                    f"('{d['slug']}', $q${d['title']}$q$, {d['pass_pct']}, $q${body}$q$::jsonb)\n"
                    f"on conflict (slug) do update set title = excluded.title, pass_pct = excluded.pass_pct, "
                    f"questions = excluded.questions, updated_at = now();\n")
    (ROOT / "supabase" / "assessments_seed.sql").write_text("\n".join(seed), encoding="utf-8")


# Sticky tab bars keep the old scroll position after a click, so the new panel opens part-way down.
# This returns the page to the top whenever a tab inside a sticky or fixed bar is clicked.
PILL_JS = ("<script>document.addEventListener('click',function(e){var p=document.querySelector('.site-pill.open');if(p&&!p.contains(e.target))p.classList.remove('open')});"
           "addEventListener('scroll',function(){var p=document.querySelector('.site-pill.open');if(p)p.classList.remove('open')},{passive:true});</script>")

TAB_SCROLL = ("<script>document.addEventListener('click',function(e){var t=e.target.closest("
              "'[role=tab],.tab,.tabbar button,.tabs button,.section-tabs button,[data-tab],[data-panel-tab]');if(!t)return;"
              "var n=t,s=false;while(n&&n!==document.body){var p=getComputedStyle(n).position;if(p==='sticky'||p==='fixed'){s=true;break}n=n.parentElement}"
              "if(s)setTimeout(function(){window.scrollTo(0,0)},30)});</script>")


# A #tab hash in the URL makes the browser jump to that panel, so artifacts opened part-way down. Always start at the top.
TOP_RESET = ("<script>(function(){try{history.scrollRestoration='manual'}catch(e){}var go=true;function up(){if(go)scrollTo(0,0)}"
             "['wheel','touchstart','keydown','mousedown'].forEach(function(k){addEventListener(k,function(){go=false},{once:true,passive:true})});"
             "up();addEventListener('load',up);setTimeout(up,150);setTimeout(up,500)})();</script>")


CRUMB_CSS = ("<style id=site-crumbs>.lesson-crumbs{display:flex;flex-wrap:wrap;gap:6px;align-items:center;padding:8px 16px;"
             "font:500 13px/1.3 -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:#f1eee7;color:#5a6772;border-bottom:1px solid rgba(0,0,0,.08)}"
             ".lesson-crumbs a{color:#0b6b66;text-decoration:none}.lesson-crumbs a:hover{text-decoration:underline}.lesson-crumbs i{font-style:normal;opacity:.5}"
             ".lesson-crumbs span{color:#2b3640;font-weight:600}"
             "@media (prefers-color-scheme:dark){:root:not([data-theme=light]) .lesson-crumbs{background:#1a2128;color:#9aa8b2;border-color:rgba(255,255,255,.1)}"
             ":root:not([data-theme=light]) .lesson-crumbs a{color:#5fd1c9}:root:not([data-theme=light]) .lesson-crumbs span{color:#e6edf2}}"
             ":root[data-theme=dark] .lesson-crumbs{background:#1a2128;color:#9aa8b2;border-color:rgba(255,255,255,.1)}:root[data-theme=dark] .lesson-crumbs a{color:#5fd1c9}:root[data-theme=dark] .lesson-crumbs span{color:#e6edf2}"
             "@media print{.lesson-crumbs{display:none}}</style>")


def crumb_bar(crumbs, root):
    parts = [f'<a href="{root}{h}">{esc(l)}</a>' if h is not None else f"<span>{esc(l)}</span>" for l, h in crumbs]
    return f'{CRUMB_CSS}<nav class="lesson-crumbs" aria-label="Breadcrumb">{"<i>/</i>".join(parts)}</nav>'


SVGFIX = '<script>' + (ROOT / 'tools' / 'artifact-kit' / 'svgfix.js').read_text(encoding='utf-8') + '</script>'


def inject_pill(text, back_href, back_label, home_href, slug, courses, review=True, crumbs=None):
    done_btn = f'<button data-done-slug="{slug}" hidden></button><button data-role-toggle="{slug}" hidden></button><button data-role-delete="{slug}" hidden></button><button data-role-restore="{slug}" hidden></button>'
    pill = (f'{PILL_CSS}<div class="site-pill"><button type="button" class="pill-more" aria-label="Menu" onclick="this.parentNode.classList.toggle(&#39;open&#39;)">☰</button><a href="{back_href}">← {esc(back_label)}</a>'
            f'<a href="{home_href}">Home</a><button type="button" title="Light / dark" onclick="{THEME_CLICK}">◐</button>{done_btn}</div>'
            f'{auth_scripts(home_href, courses)}{TAB_SCROLL}{PILL_JS}{TOP_RESET}{SVGFIX}')
    head = favicon_links(home_href) + THEME_HEAD + GATE_HEAD
    text = text.replace("<head>", "<head>" + head, 1) if "<head>" in text else head + text
    if crumbs:
        m = re.search(r"<body[^>]*>", text)
        bar = crumb_bar(crumbs, home_href)
        text = text[:m.end()] + bar + text[m.end():] if m else bar + text
    if "</body>" in text:
        i = text.rfind("</body>")
        return text[:i] + pill + text[i:]
    return text + pill


# Locked lessons: every artifact that belongs to a course is published as an encrypted payload plus a small shell page
# that fetches its key from Supabase (artifact_key). See README "Locked lessons". GATE=off builds plain, open pages.
GATE_SECRET = ROOT / ".gate_secret"
TEXT_EXT = {".html", ".htm", ".css"}


def gate_master():
    if os.environ.get("GATE", "").lower() == "off":
        return None
    if not GATE_SECRET.exists():
        raise SystemExit("No .gate_secret. Run: python3 tools/gate_secret.py   (or build open pages with GATE=off python3 build.py)")
    return GATE_SECRET.read_text().strip()


def lesson_key(master, slug):
    return hmac.new(master.encode(), f"artifact:{slug}".encode(), hashlib.sha256).digest()


def encrypt_payload(master, slug, payload):
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM
    key = lesson_key(master, slug)
    plain = gzip.compress(json.dumps(payload, ensure_ascii=False).encode("utf-8"), mtime=0)
    iv = hmac.new(key, b"iv" + hashlib.sha256(plain).digest(), hashlib.sha256).digest()[:12]  # same content, same file: tidy git diffs
    return iv + AESGCM(key).encrypt(iv, plain, None)


def shell_page(slug, title, courses, tier):
    r = "../../"
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title>{favicon_links(r)}{THEME_HEAD}
<style>body{{margin:0;background:#f6f4ef;color:#5a6772;font:16px/1.5 -apple-system,Segoe UI,sans-serif}}#gate-msg{{padding:18vh 20px;text-align:center}}
@media (prefers-color-scheme:dark){{:root:not([data-theme=light]) body{{background:#12171c;color:#9aa8b2}}}}:root[data-theme=dark] body{{background:#12171c;color:#9aa8b2}}</style></head>
<body><p id="gate-msg">Opening lesson…</p>
<script src="{r}assets/config.js"></script>
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
<script src="{r}assets/app.js"></script>
<script src="{r}assets/gateload.js" data-slug="{slug}" data-courses="{",".join(courses)}" data-tier="{tier}"></script>
</body></html>
"""


def build_artifacts():
    master = gate_master()
    seed = []
    for a in ARTIFACTS:
        first = a["places"][0]
        info = chapter_info[first]
        ch = info["ch"]
        src, dest = SRC / a["src"], OUT / "artifacts" / a["slug"]
        depth_root = "../../"
        back = depth_root + info["path"] + ("" if is_review(a) else "#res")
        label = chapter_label(ch, ch["title"])
        ckey0 = first[0]
        crumbs = [("Home", "")]
        if ckey0 in COURSES:
            crumbs.append((COURSES[ckey0]["title"], f"{ckey0}/"))
        crumbs += list(info["parents"]) + [(label, info["path"]), (a["title"], None)]
        courses = [] if a.get("public") else sorted({c for c, _ in a["places"] if c in COURSES})
        locked = bool(master and courses)
        bundle = {}
        for f in src.rglob("*"):
            if f.is_dir():
                continue
            rel = f.relative_to(src)
            if f.suffix == ".html":
                content = bust(inject_pill(f.read_text(encoding="utf-8"), back, label, depth_root, a["slug"], courses, is_review(a), crumbs))
            elif f.suffix in TEXT_EXT:
                content = f.read_text(encoding="utf-8")
            else:
                content = None
            target = dest / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            if locked and content is not None:
                assert len(rel.parts) == 1, f"Locked lessons only bundle top-level files: {a['src']}/{rel}"
                bundle[rel.name] = content
            elif content is not None:
                target.write_text(content, encoding="utf-8")
            else:
                shutil.copy2(f, target)
        if locked:
            index = bundle.pop("index.html")
            (dest / "payload.bin").write_bytes(encrypt_payload(master, a["slug"], {"index": index, "files": bundle}))
            (dest / "index.html").write_text(bust(shell_page(a["slug"], a["title"], courses, a.get("tier", "full"))), encoding="utf-8")
        if courses:
            seed.append((a["slug"], courses, a.get("tier", "full")))
    lines = ["-- Written by build.py. Safe to rerun: lists the locked lessons, which courses unlock each and the lowest tier that opens it (see schema.sql, v7).",
             "insert into public.artifact_courses (slug, courses, min_tier) values"]
    lines.append(",\n".join("  ('%s', array[%s], '%s')" % (s, ",".join("'%s'" % c for c in cs), t) for s, cs, t in seed))
    lines.append("on conflict (slug) do update set courses = excluded.courses, min_tier = excluded.min_tier;")
    lines.append("delete from public.artifact_courses where slug not in (%s);" % ",".join("'%s'" % s for s, _, _ in seed))
    seed_file = ROOT / "supabase" / "artifact_access_seed.sql"
    text = "\n".join(lines) + "\n"
    if not seed_file.exists() or seed_file.read_text(encoding="utf-8") != text:
        print("NOTE: supabase/artifact_access_seed.sql changed. Paste it into the Supabase SQL Editor so students can open new or moved lessons.")
    seed_file.write_text(text, encoding="utf-8")


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    shutil.copytree(ROOT / "assets", OUT / "assets")
    (OUT / ".nojekyll").write_text("")
    build_home()
    if LANDING_PAGE:
        build_landing()
    build_courses()
    build_investing()
    build_other_profile()
    build_catalog()
    build_assessments()
    build_artifacts()
    n = sum(1 for _ in OUT.rglob("index.html"))
    print(f"Built {n} index pages, {len(ARTIFACTS)} artifacts -> {OUT}")


if __name__ == "__main__":
    main()
