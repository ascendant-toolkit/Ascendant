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
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "tools"))
import econ_past  # noqa: E402
import ig_past  # noqa: E402
import igcs_past  # noqa: E402
import extra_lessons  # noqa: E402
import keywords  # noqa: E402
import reword  # noqa: E402
import split_full  # noqa: E402

from site_data import A_CS_MOVED, A_ECON_MOVED, ARTIFACTS, COURSES, PADDLE, LANDING_PAGE, SITE_TAGLINE, SITE_TITLE

ROOT = Path(__file__).parent
OUT = ROOT / "docs"
SRC = ROOT / "artifacts_src"

NAV = [
    ("home", "Home", ""),
    ("ig-econ", "IG Econ", "ig-econ/"),
    ("ig-cs", "IG CS", "ig-cs/"),
    ("a-econ", "A Econ", "a-econ/"),
    ("a-cs", "A CS", "a-cs/"),
    ("pricing", "Plans", "pricing/"),
    ("dashboard", "Dashboard", "dashboard/"),
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


SITE_URL = "https://ascendant.academy/"
SITE_DESC = "Interactive Cambridge IGCSE and A-Level Economics and Computer Science lessons with marked assessments, model answers and progress tracking."
PRIVATE = {"dashboard", "profile", "plan", "progress", "assess", "tests"}
SITEMAP = []


def seo_head(title, body, path):
    """Description, canonical and social tags. Description comes from the page's lead paragraph."""
    m = re.search(r'<p class="lead">(.*?)</p>', body, re.S)
    desc = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", m.group(1))).strip() if m else ""
    desc = html.unescape(desc)
    if len(desc) < 25:
        desc = SITE_DESC
    desc = desc[:157].rsplit(" ", 1)[0] + "…" if len(desc) > 160 else desc
    url = SITE_URL + path.lstrip("/")
    if path.split("/")[0] in PRIVATE:
        return '<meta name="robots" content="noindex">\n'
    SITEMAP.append(url)
    t, d = esc(title), esc(desc)
    ld = []
    org = {"@type": "Organization", "name": SITE_TITLE, "url": SITE_URL, "logo": SITE_URL + "assets/apple-touch-icon.png"}
    if path.strip("/") == "":
        ld += [{"@context": "https://schema.org", **org},
               {"@context": "https://schema.org", "@type": "WebSite", "name": SITE_TITLE, "url": SITE_URL}]
    elif path.strip("/") in COURSES:
        ld.append({"@context": "https://schema.org", "@type": "Course", "name": html.unescape(title.split(" · ")[0]),
                   "description": desc, "provider": org, "url": url})
    qa = re.findall(r"<details><summary>(.*?)</summary><p>(.*?)</p></details>", body, re.S)
    if qa:
        clean = lambda x: html.unescape(re.sub(r"<[^>]+>", "", x)).strip()
        ld.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": clean(q), "acceptedAnswer": {"@type": "Answer", "text": clean(a)}} for q, a in qa]})
    ldh = "".join(f'<script type="application/ld+json">{json.dumps(o, ensure_ascii=False).replace("</", "<\\/")}</script>' for o in ld)
    return (ldh + f'<meta name="description" content="{d}">\n<link rel="canonical" href="{url}">\n'
            f'<meta property="og:type" content="website"><meta property="og:site_name" content="{esc(SITE_TITLE)}">'
            f'<meta property="og:title" content="{t}"><meta property="og:description" content="{d}">'
            f'<meta property="og:url" content="{url}"><meta property="og:image" content="{SITE_URL}assets/og.jpg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">'
            f'<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{t}"><meta name="twitter:description" content="{d}">\n')


def layout(title, body, path, active, crumbs=None, accent=None, auth=False, extra=""):
    root = rel_root(path)
    nav = "".join(
        f'<a href="{root}{href}"{" class=on aria-current=page" if key == active else ""}{f" data-course={key}" if key in COURSES else ""}>{label}</a>'
        for key, label, href in NAV
    )
    nav += f'<a class="join" href="{root}pricing/">Sign in / up</a>'
    crumb_html = ""
    if crumbs:
        parts = []
        for label, href in crumbs:
            parts.append(f'<a href="{root}{href}">{esc(label)}</a>' if href is not None else f"<span>{esc(label)}</span>")
        crumb_html = f'<nav class="crumbs" aria-label="Breadcrumb">{"<i>/</i>".join(parts)}</nav>'
    acc = f' data-accent="{accent}"' if accent else ""
    gate = []  # course and chapter pages only list lesson titles; the lessons themselves are gated by their own shells
    full_title = SITE_TITLE if title == SITE_TITLE else f"{title} · {SITE_TITLE}"
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(full_title)}</title>
{seo_head(full_title, body, path)}<link rel="stylesheet" href="{root}assets/style.css">
{favicon_links(root)}{THEME_HEAD}{GATE_HEAD if gate else ""}</head>
<body{acc}>
<a class="skip" href="#main">Skip to content</a>
<header class="site">
<div class="bar">
<a class="brand" href="{root}"><img class="mark" src="{root}assets/logo.svg" alt="" width="34" height="34"><span>{esc(SITE_TITLE)}</span></a>
<button class="theme" type="button" aria-label="Toggle dark mode"></button>
<button class="menu" aria-label="Menu" aria-expanded="false" aria-controls="main-nav">Menu</button>
<nav class="main" id="main-nav" aria-label="Main">{nav}</nav>
</div>
</header>
<main id="main" tabindex="-1">
{crumb_html}
{body}
</main>
<footer class="site"><p><a href="{root}schools/">For schools</a> · <a href="{root}contact/">Contact</a> · <a href="{root}terms/">Terms</a> · <a href="{root}privacy/">Privacy</a> · <a href="{root}refunds/">Refunds</a> · <a href="mailto:{SUPPORT_EMAIL}">{SUPPORT_EMAIL}</a></p><p>Independent revision resource for Cambridge IGCSE and A-Level. Not affiliated with or endorsed by Cambridge University Press &amp; Assessment.</p></footer>
<script src="{root}assets/site.js"></script>
{auth_scripts(root, gate)}{extra}{CF_BEACON}
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
    """Syllabus order. The leading number in the description wins over a vaguer or wrong `at`;
    an explicit `.99` stays last in its section, a more specific `at` is kept."""
    at = a.get("at") or ""
    m = re.match(r"(\d+(?:\.\d+)*)\b", a.get("desc", ""))
    d = m.group(1) if m else ""
    if d and (not at or not (at == d or at.startswith(d + ".") or at.endswith(".99"))):
        at = d
    return [int(x) for x in at.split(".")] if at else [10**6]


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
    tt = TOPIC_TESTS.get(info["path"].rstrip("/"))
    ttblock = (f'<section class="card block ttest" data-test="{tt["id"]}"><div class="row"><h2>Topic test</h2><span class="hint">{tt["marks"]} marks</span></div>'
               f'<p class="hint">{tt["mcq_n"]} multiple choice questions and written questions in exam style. Take it when you finish the chapter, as often as you like.</p>'
               f'<p><a class="btn" href="{rel_root(info["path"])}tests/?t={tt["id"]}">Take the topic test</a> <span class="hint ttscore"></span></p></section>') if tt else ""
    body = (ttblock + '<div class="tabs chtabs" role="tablist">'
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


# Cloudflare Web Analytics (cookie-free). Paste the site token from Cloudflare > Analytics & Logs > Web Analytics here; empty = no script,
# and the privacy notice then says nothing about analytics. The token is public (it ships in every page).
CF_BEACON_TOKEN = "fac8709a88264e1f8c717fe556bd9f5a"
CF_BEACON = (f'<script defer src="https://static.cloudflareinsights.com/beacon.min.js" data-cf-beacon=\'{{"token": "{CF_BEACON_TOKEN}"}}\'></script>'
             if CF_BEACON_TOKEN else "")
SUPPORT_EMAIL = "support@ascendant.academy"
SUPPORT_LINK = f'<a href="mailto:{SUPPORT_EMAIL}">{SUPPORT_EMAIL}</a>'
NUM_WORDS = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten"}
N_FREE = len([a for a in ARTIFACTS if a.get("tier") == "free"])
FREE_WORD = NUM_WORDS.get(N_FREE, str(N_FREE))

HOME_FAQ = [
    ("Who is it for?", "Cambridge IGCSE and A-Level students in Economics and Computer Science, the teachers who teach them, and schools and tutors who want one place for lessons, practice and progress."),
    ("Which exam board is this for?", "Cambridge International only: " + ", ".join(f"{lvl} {subj} {code}" for _, lvl, subj, code in SYLLABI[:-1]) + f" and {SYLLABI[-1][1]} {SYLLABI[-1][2]} {SYLLABI[-1][3]}."),
    ("Can I try it first?", f"Yes. {FREE_WORD.capitalize()} full sample lessons open with no account, so you can judge the quality before paying anything."),
    ("Does it replace classroom teaching?", "No. It is built to support teachers: ready-made lessons and practice to use in class, and a way for students to revise and learn independently at home."),
    ("Can my school or tutoring business use it?", "Yes. Schools and tutors get a licence for a set number of students, free teacher accounts, and dashboards to see each student's progress. See the plans page or get in touch."),
    ("Does it work on a phone?", "Yes. Every page works on phones, tablets and laptops, in light or dark mode."),
    ("Is this official Cambridge material?", "No. This is an independent resource and is not endorsed by or affiliated with Cambridge University Press &amp; Assessment. Cambridge IGCSE and Cambridge International AS &amp; A Level are trademarks of their owners."),
]

# Hero visual: a demand curve that shifts right while the equilibrium dot follows it.
HERO_CHART = """<svg class="lp-chart" viewBox="0 0 320 240" role="img" aria-label="Supply and demand diagram with the demand curve shifting right">
<line x1="40" y1="20" x2="40" y2="205" class="ax"/><line x1="40" y1="205" x2="300" y2="205" class="ax"/>
<text x="14" y="30" class="lb">P</text><text x="292" y="224" class="lb">Q</text>
<line x1="70" y1="190" x2="270" y2="40" class="sup"/><text x="262" y="34" class="lb s">S</text>
<g><line x1="60" y1="45" x2="220" y2="185" class="dem0"/>
<line x1="60" y1="45" x2="220" y2="185" class="dem"><animateTransform attributeName="transform" type="translate" values="0 0;48 0;48 0;0 0;0 0" keyTimes="0;.3;.7;.9;1" dur="7s" repeatCount="indefinite"/></line>
<text x="206" y="204" class="lb d">D</text></g>
<circle r="6" class="eq"><animateMotion dur="7s" repeatCount="indefinite" keyTimes="0;.3;.7;.9;1" calcMode="linear" path="M 153.8 127 L 179.7 107.7 L 179.7 107.7 L 153.8 127 L 153.8 127"/></circle>
</svg>"""

HERO_CODE = """<pre class="lp-code" aria-label="Pseudocode trace example"><span class="c">// trace it, line by line</span>
<b>FOR</b> i <b>&larr;</b> 1 <b>TO</b> 3
   total <b>&larr;</b> total + i
<b>NEXT</b> i
<span class="c">i = 3, total = 6</span></pre>"""


NOTIFY = """<section class="sec" id="notify" aria-labelledby="nf"><div class="free-card"><h2 id="nf">Get launch news</h2>
<p class="lede">Leave your email and we will tell you when paid plans open, plus any launch offers.</p>
<form class="joinform notifyform" novalidate>
<label>Email<input name="email" type="email" autocomplete="email" maxlength="254" required></label>
<label>I am a<select name="role"><option value="student">Student</option><option value="parent">Parent</option><option value="teacher">Teacher</option></select></label>
<input name="website" tabindex="-1" autocomplete="off" aria-hidden="true" style="position:absolute;left:-9999px;opacity:0">
<label class="chk consent"><input type="checkbox" name="consent" required> Email me about launch and new content. No spam, and you can opt out any time.</label>
<button class="btn" type="submit">Notify me</button><p class="msg" hidden role="status"></p></form></div></section>"""


def build_home():
    r = ""
    cards = []
    total = len({a["slug"] for a in ARTIFACTS})
    chapters = 0
    for ckey, lvl, subj, code in SYLLABI:
        c = COURSES[ckey]
        n, chs = course_stats(ckey)
        chapters += chs
        cards.append(f'<a class="card course syl" data-accent="{c["accent"]}" data-home-course="{ckey}" href="{ckey}/"><span class="tag">{lvl}</span>'
                     f'<span class="t">{subj}</span><span class="code">Cambridge {code}</span>'
                     f'<span class="sub">{SYL_BLURB[ckey]}</span>'
                     f'<span class="count">{plural(n, "activity")} across {chs} chapters</span></a>')
    nsyl = NUM_WORDS.get(len(SYLLABI), str(len(SYLLABI))).capitalize()
    by_slug = {a["slug"]: a for a in ARTIFACTS}
    pick = [("ig-econ", "IGCSE Economics", "ig-market-equilibrium"), ("a-econ", "A-Level Economics", "market-structures-lab"),
            ("ig-cs", "IGCSE Computer Science", "ig-cs-programming-concepts"), ("a-cs", "A-Level Computer Science", "insertion-sort")]
    samples_html = "".join(
        f'<a class="card" data-accent="{COURSES[ck]["accent"]}" href="artifacts/{sl}/#learn"><span class="tag">{lab}</span>'
        f'<span class="t">{esc(by_slug[sl]["title"])}</span><span class="sub">{esc(by_slug[sl].get("desc", ""))}</span>'
        f'<span class="count">{"Opens now, no account" if by_slug[sl].get("public") else "Free account"}</span></a>'
        for ck, lab, sl in pick)
    tabs = "".join(f'<li><b>{t}</b><span>{d}</span></li>' for t, d in TABS)
    faq = "".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in HOME_FAQ)
    steps = [("Pick your plan", f"Start free with {FREE_WORD} sample lessons, or choose the plan for your subject. Schools and tutors get a licence for their students."),
             ("Sign in anywhere", "Your account follows you from school to home, on any phone, tablet or laptop."),
             ("Learn, practise, track", "Work through each chapter, take the assessments, and watch your progress build on your dashboard.")]
    steps_html = "".join(f'<li><span class="n">{i}</span><div><b>{t}</b><p>{d}</p></div></li>' for i, (t, d) in enumerate(steps, 1))
    body = f"""<section class="lp-hero"><div class="lp-copy"><p class="kicker">Cambridge IGCSE and A-Level</p>
<h1 id="lp-title">A teaching and learning toolkit: for everyone</h1>
<p class="lp-sub">Students &middot; Tutors &middot; Teachers &middot; Schools</p>
<p class="lead">Your syllabus, fully resourced, chapter by chapter: with animated explainers, hands-on activities, exam questions with model answers, marked assessments and progress tracking, all in one place.</p>
<p class="cta"><a class="btn" id="joinbtn" href="pricing/">Sign up</a><a class="btn ghost" id="sample" href="#samples">Try a free lesson</a><a class="btn ghost" id="signin" href="profile/">Sign in</a></p>
<ul class="lp-stats"><li><b>{total}</b><span>interactive activities</span></li><li><b>{chapters}</b><span>chapters</span></li><li><b>{len(SYLLABI)}</b><span>Cambridge syllabuses</span></li></ul></div>
<div class="lp-visual" aria-hidden="false"><div class="lp-pane lp-pane-a"><span class="lp-tag">Economics &middot; Explore</span>{HERO_CHART}<p>Shift the curves and watch the market move.</p></div>
<div class="lp-pane lp-pane-b"><span class="lp-tag">Computer Science &middot; Watch</span>{HERO_CODE}<p>Step through code and see every value change.</p></div></div></section>

<section class="sec" aria-labelledby="val"><h2 id="val">Everything a department needs, ready to teach</h2>
<p class="lede">Spend less time building and marking resources. Every chapter arrives fully resourced, and every student's progress is easy to see.</p>
<div class="lp-compare">
<div class="lp-col"><span class="lp-tag">In the classroom</span><b class="lp-pt">Ready to teach</b><p>Lessons, animations and interactive labs for the whole syllabus, with a delivery mode for teaching from the front.</p></div>
<div class="lp-col"><span class="lp-tag">Assessment</span><b class="lp-pt">Marked for you</b><p>Short assessments are marked instantly with feedback, so teachers get their time back.</p></div>
<div class="lp-col"><span class="lp-tag">Progress</span><b class="lp-pt">See who is keeping up</b><p>Class dashboards show what each student has finished and how they scored.</p></div>
<div class="lp-col"><span class="lp-tag">At home</span><b class="lp-pt">Learning that carries on</b><p>Students pick up where they left off on any device, for revision and independent study.</p></div></div></section>

<section class="sec" aria-labelledby="stu"><h2 id="stu">Everything a student needs, to learn and revise</h2>
<p class="lede">Clear explanations, plenty of practice and honest feedback, for every chapter of the syllabus.</p>
<div class="lp-compare">
<div class="lp-col"><span class="lp-tag">Understand</span><b class="lp-pt">Learn it properly</b><p>Plain-English explanations and step-by-step animations that show how each idea works.</p></div>
<div class="lp-col"><span class="lp-tag">Practise</span><b class="lp-pt">Hands-on activities</b><p>Sliders, simulations, drag-and-drop and quick quizzes, with instant feedback as you go.</p></div>
<div class="lp-col"><span class="lp-tag">Exam ready</span><b class="lp-pt">Questions with model answers</b><p>Past-paper style questions with mark scheme points, plus marked assessments that show what to fix.</p></div>
<div class="lp-col"><span class="lp-tag">Progress</span><b class="lp-pt">Know where you stand</b><p>Your dashboard tracks every lesson and score, and takes you straight back to where you left off.</p></div></div></section>

<section class="sec" aria-labelledby="syl"><h2 id="syl">{nsyl} Cambridge syllabuses</h2>
<p class="lede">Built chapter by chapter against the syllabus.</p><div class="grid two">{"".join(cards)}</div>
<p class="hint" id="homehint" hidden>Sign in on the <a href="profile/">Profile</a> page to open your courses.</p></section>

<section class="sec" aria-labelledby="ins"><h2 id="ins">What is in every chapter</h2>
<p class="lede">Chapters share the same seven tabs, so you always know where to find things.</p><ul class="tabsum">{tabs}</ul></section>

<section class="sec" aria-labelledby="who"><h2 id="who">Built for the way you study or teach</h2>
<div class="lp-who">
<article class="card" data-accent="teal"><h3 class="t">Students</h3><p class="sub">Learn from home or school, take marked assessments with instant feedback, and see exactly what is left to cover.</p><a class="go" href="pricing/">Student plans →</a></article>
<article class="card" data-accent="indigo"><h3 class="t">Teachers</h3><p class="sub">Ready-made lessons for the whole syllabus, class progress at a glance, and a delivery mode for the classroom. Less time building resources.</p><a class="go" href="pricing/">Teacher plan →</a></article>
<article class="card" data-accent="plum"><h3 class="t">Schools and tutors</h3><p class="sub">One licence for your students, free teacher accounts, and dashboards to see who is keeping up. Invoiced annually.</p><a class="go" href="schools/">School licences →</a></article></div></section>

<section class="sec" aria-labelledby="how"><h2 id="how">How it works</h2><ol class="steps">{steps_html}</ol></section>

<section class="sec lp-final" id="samples"><h2>Try a free lesson</h2>
<p class="lede">Pick your subject. Every sample opens straight away, no account needed.</p>
<div class="grid">{samples_html}</div>
<p class="cta"><a class="btn ghost" href="pricing/">See plans</a></p></section>

{NOTIFY}
<section class="sec" aria-labelledby="fq"><h2 id="fq">Questions</h2><div class="faq">{faq}</div></section>"""
    write("index.html", layout(SITE_TITLE, body, "", "home", extra='<script src="assets/home.js"></script><script src="assets/notify.js"></script>'))


def build_contact():
    """Contact form at /contact/. Messages land in the contact_messages table (admins read them in Supabase)."""
    topics = [("password", "Password or sign-in help"), ("subjects", "Change subjects, class or seats"),
              ("school", "Licence for a school or tutor"), ("billing", "Billing or refunds"), ("other", "Something else")]
    roles = [("student", "Student"), ("parent", "Parent"), ("teacher", "Teacher"), ("school", "School administrator"), ("tutor", "Tutor")]
    opt = lambda items: "".join(f'<option value="{k}">{v}</option>' for k, v in items)
    body = (head("Contact", "Questions about your account, a licence or anything else. We reply by email.", "Get in touch")
            + '<section class="sec" style="margin-top:8px"><div class="free-card"><form id="contactform" class="joinform" novalidate>'
            f'<p class="hint">Prefer email? Write to {SUPPORT_LINK}.</p>'
            '<p class="hint">Students in a school: your teacher can reset your password and change your subjects first. Teachers: ask your school administrator. '
            'Tutors and schools can message us here, and so can students without a school or tutor.</p>'
            '<label>Name<input name="name" autocomplete="name" maxlength="120" required></label>'
            '<label>Email<input name="email" type="email" autocomplete="email" maxlength="254" required></label>'
            f'<label>I am a<select name="role">{opt(roles)}</select></label>'
            '<label>School or organisation (if any)<input name="org" maxlength="160"></label>'
            f'<label>Topic<select name="topic">{opt(topics)}</select></label>'
            '<label>Message<textarea name="message" rows="6" maxlength="4000" required></textarea></label>'
            '<input name="website" tabindex="-1" autocomplete="off" aria-hidden="true" style="position:absolute;left:-9999px;opacity:0">'
            '<button class="btn" type="submit">Send message</button><p class="msg" id="contactmsg" hidden></p></form></div></section>')
    write("contact/index.html", layout("Contact", body, "contact/", "contact", [("Home", ""), ("Contact", None)],
                                       extra='<script src="../assets/contact.js"></script>'))


LEGAL_UPDATED = "15 November 2026"

LEGAL = {
    "terms": ("Terms of service", "The rules for using Ascendant, in plain English.", [
        ("Who we are", "Ascendant is an independent revision resource for Cambridge IGCSE and A-Level Economics and Computer Science. It is not affiliated with or endorsed by Cambridge University Press &amp; Assessment. You can reach us through the <a href=\"../contact/\">contact form</a>."),
        ("Your account", "You need an account to track progress and to use paid lessons. Keep your password private. Accounts are for one person: please do not share logins or the lesson content. If you are under 16, ask a parent or guardian to set up the account and any purchase."),
        ("What you are buying", "A paid plan gives you access to the lessons, assessments and practice for the subjects and tier you chose, for as long as your plan is active. Plans renew automatically each month or year until you cancel. Content is updated and improved over time, and we may add, change or retire individual items."),
        ("Prices, payment and tax", "Prices are shown in US dollars. Prices include VAT and sales tax, so the price you see is the price you pay. At checkout you are charged in your local currency. Our order process is conducted by our online reseller Paddle.com Market Limited. Paddle is the merchant of record for all orders: it sells the plan to you, handles payment, tax, invoices and refunds, and its <a href=\"https://www.paddle.com/legal/checkout-buyer-terms\">checkout buyer terms</a> apply to the purchase alongside these terms."),
        ("Cancelling", "Cancel at any time from your Paddle receipt email or by contacting us. You keep access until the end of the period you have paid for, then the plan stops and you are not charged again. Refunds are covered in the <a href=\"../refunds/\">refund policy</a>."),
        ("Acceptable use", "Use the site for your own revision or teaching. Do not copy, resell, scrape or redistribute the lessons, assessments or answer material, and do not try to break or bypass the site's access controls."),
        ("Our content and your results", "The lessons are our own work, built around the published Cambridge syllabi. We take care to be accurate, but we cannot guarantee any exam result or that the material is free of errors. Always check the official syllabus and mark schemes for your exam series."),
        ("Schools and tutors", "Licences for schools and tutors run for the agreed term and are covered by the licence terms agreed when you sign up, alongside these terms."),
        ("Changes and ending access", "We may update these terms; the date at the top shows the latest version. We may suspend an account that breaks these terms. Nothing in these terms limits any legal rights you have as a consumer."),
    ]),
    "privacy": ("Privacy notice", "What we collect, why, and who handles it.", [
        ("What we collect", "Your name, email address, the subjects you study, your progress and assessment attempts, any message you send through the contact form, and your email and role (student, parent or teacher) if you join the launch-news list. If you buy a plan, Paddle collects your payment details and billing address; we receive your email, the plan and the payment status, but never your card number."),
        ("Why we use it", "To run your account, unlock the lessons you have paid for, show your progress, reply to your messages and send account emails such as password resets. If you join the launch-news list, we use your email only to tell you about paid plans, launch offers and new content, and you can ask to be removed at any time. We do not sell your data and we do not use it for advertising."),
        ("Who handles it", "Supabase hosts our database and logins. Paddle processes payments as merchant of record. Resend delivers our account emails. GitHub hosts the website. Each handles data only to provide its service."),
        ("Cookies and storage", "We use your browser's local storage to keep you signed in and remember your progress. We do not use advertising or cross-site tracking cookies." + (" To see which pages are used, we use Cloudflare Web Analytics, which does not use cookies or local storage and does not build profiles of individual visitors." if CF_BEACON_TOKEN else "")),
        ("How long we keep it", "While your account exists. Payment records are kept as long as tax and accounting rules require. Ask us to delete your account and we will remove your data, except records we are legally required to keep."),
        ("Your rights", "You can ask to see, correct or delete the personal data we hold about you, or to object to how we use it. Use the <a href=\"../contact/\">contact form</a> and choose the topic that fits, or email <a href=\"mailto:support@ascendant.academy\">support@ascendant.academy</a>. Students in a school may also be able to ask their teacher to correct details."),
        ("Children", "Many of our students are under 18. Younger students should use the site with a parent or guardian's agreement, and any purchase should be made by an adult."),
    ]),
    "refunds": ("Refund policy", "How refunds and cancellations work.", [
        ("14-day money-back guarantee", "There is a 14-day money-back guarantee on your first purchase. If it is not for you, get in touch within two weeks of buying and we will refund it in full, no questions asked."),
        ("Monthly plans", "Cancel at any time and you are not charged again. You keep access until the end of the month you have paid for. After the first 14 days, monthly payments are not refunded."),
        ("Annual plans", "After the first 14 days an annual plan is non-refundable and you keep full access until it ends. If you have a genuine reason, get in touch: any goodwill refund is worked out at the standard monthly price for the months you have used, not the discounted annual rate."),
        ("Schools and tutors", "Licences are annual commitments with no mid-term refunds. Schools get a 30-day evaluation instead. After that the licence runs for the agreed term."),
        ("How to ask", "Use the <a href=\"../contact/\">contact form</a> and choose Billing or refunds, email <a href=\"mailto:support@ascendant.academy\">support@ascendant.academy</a>, or reply to your Paddle receipt. Approved refunds go back to your original payment method and your access ends when the refund is made."),
        ("Your legal rights", "This policy does not affect any rights you have under consumer law."),
    ]),
}


def build_legal():
    """Terms, privacy and refund pages at /terms/, /privacy/, /refunds/. Paddle requires all three on the site to approve the domain."""
    for slug, (title, lead, sections) in LEGAL.items():
        parts = "".join(f'<h2>{esc(h)}</h2><p>{t}</p>' for h, t in sections)
        body = (head(title, lead, "Legal") + f'<section class="sec" style="max-width:720px"><p class="hint">Last updated {LEGAL_UPDATED}</p>{parts}</section>')
        write(f"{slug}/index.html", layout(title, body, f"{slug}/", slug, [("Home", ""), (title, None)]))


def build_schools():
    """For-schools page at /schools/, written for heads of department and finance."""
    r = "../"
    contact = f"{r}contact/?topic=school&amp;role=school"
    tiles = [("Free teacher accounts", "Every teacher on your licence gets full access to the subjects you buy, plus class progress dashboards. No per-teacher charge."),
             ("Pay per subject", "Departments buy only the subjects they teach. Add a subject, or more students, at any renewal."),
             ("One clear invoice", "A single annual invoice per school. No student payments, no card forms for families, no surprises mid-year."),
             ("You control the roster", "Your teachers add and remove students, reset logins and move students between subjects without contacting us.")]
    tiles_html = "".join(f'<div class="lp-col"><b class="lp-pt">{t}</b><p>{d}</p></div>' for t, d in tiles)
    steps = [("Tell us your subjects and numbers", "Send a short message with the subjects and roughly how many students take each."),
             ("Start a 30-day evaluation", "Your teachers try the full platform with their classes before you commit."),
             ("Receive one annual invoice", "Pay once for the year. Your teachers add their students and begin straight away.")]
    steps_html = "".join(f'<li><span class="n">{i}</span><div><b>{t}</b><p>{d}</p></div></li>' for i, (t, d) in enumerate(steps, 1))
    faq = [("What does a seat cover?", "One student in one subject for a year, with every lesson, interactive activity, marked assessment and progress report for that subject."),
           ("Is there a minimum order?", "Licences start at 25 students per subject."),
           ("Can different departments buy separately?", "Yes. Each subject can be bought and invoiced on its own, so a department can decide for itself."),
           ("What if a student changes subject?", "Your teachers can move a student between the subjects on your licence from their dashboard, within the seats you have bought for each."),
           ("What happens at renewal or if we stop?", "Licences are annual commitments with no mid-term refunds. If a licence ends, students keep their progress and lose access to the lessons."),
           ("Do you offer a refund?", "Schools get a 30-day evaluation instead. After that the licence runs for the agreed term.")]
    faq_html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faq)
    calc = ("""<div class="free-card" id="calc"><h2>Estimate your cost</h2>
<div class="joinform"><label>Students in each subject<input id="calc-n" type="number" min="25" value="30" step="1"></label>
<label>Number of subjects<select id="calc-s"><option>1</option><option>2</option><option>3</option><option>4</option></select></label></div>
<p class="lp-big" id="calc-out" style="margin:16px 0 4px"></p><p class="hint" id="calc-sub"></p></div>
<script>(function(){var n=document.getElementById('calc-n'),s=document.getElementById('calc-s'),o=document.getElementById('calc-out'),u=document.getElementById('calc-sub');
function f(){var a=Math.max(25,parseInt(n.value,10)||25),b=parseInt(s.value,10),t=a*b*50;
o.textContent='$'+t.toLocaleString('en-US')+' a year';u.textContent=a+' students x '+b+' subject'+(b>1?'s':'')+' x $50. Teachers are free. Prices in USD.';}
n.addEventListener('input',f);s.addEventListener('change',f);f();})();</script>""")
    body = (head("Ascendant for schools", "A complete Cambridge Economics and Computer Science resource for your department: ready-made lessons, marked assessments and progress you can see.", "Schools")
            + '<p class="cta" style="margin-top:0"><a class="btn" href="' + contact + '">Talk to us</a><a class="btn ghost" href="' + r + 'pricing/">See all plans</a></p>'
            + '<section class="sec"><h2>$50 per student, per subject, per year</h2>'
            '<p class="lede">Simple to budget and easy to split between departments. A department with 30 students on one subject pays $1,500 for the year.</p>'
            f'<div class="lp-compare">{tiles_html}</div></section>'
            f'<section class="sec">{calc}</section>'
            f'<section class="sec"><h2>How it works</h2><ol class="steps">{steps_html}</ol></section>'
            f'<section class="sec"><h2>Questions</h2><div class="faq">{faq_html}</div></section>'
            '<section class="sec lp-final"><div class="free-card"><h2>Talk to us</h2><p class="lede">Tell us your subjects and student numbers and we will send a quote and start your evaluation.</p>'
            f'<p class="cta"><a class="btn" href="{contact}">Contact us</a></p></div></section>')
    write("schools/index.html", layout("For schools", body, "schools/", "schools", [("Home", ""), ("For schools", None)]))


def build_other_profile():
    ph = lambda t, s: f'<div class="card empty slim"><span class="t">{t}</span><span class="sub">{s}</span><span class="count zero">Coming soon</span></div>'
    body = (head("Other", "Things that sit outside the exam courses.", "Extras")
            + '<div class="grid">' + ph("Study tips", "How to revise, plan and manage exam season.")
            + ph("Extra-curricular activities", "Clubs, competitions and projects.") + ph("Side projects", "Things built for fun.") + "</div>")
    write("other/index.html", layout("Other", body, "other/", "other", [("Home", ""), ("Other", None)]))

    body = (head("Profile", "Sign in, or manage your details, subjects and progress.", "Account")
            + '<div id="profile-root"><noscript>This page needs JavaScript.</noscript></div>')
    write("profile/index.html", layout("Profile", body, "profile/", "profile", [("Home", ""), ("Profile", None)],
                                       auth=True, extra=_scripts("roster", "profile")))


def _scripts(*names):
    """Script tags for pages one level below the site root (assets/<name>.js), in the order given."""
    return "".join(f'<script src="../assets/{n}.js"></script>' for n in names)


def build_plan():
    """My plan at /plan/: the plans the signed-in user holds. plan.js decides what to show by who pays
    (individual, school or tutor licence, or a student whose school or tutor pays)."""
    body = ('<div id="plan-root"><noscript>This page needs JavaScript.</noscript><p class="hint">Loading your plan…</p></div>')
    write("plan/index.html", layout("My plan", body, "plan/", "plan", [("Home", ""), ("My plan", None)],
                                    auth=True, extra=_scripts("roster", "plan")))


def build_dashboard():
    """Post-login dashboard at /dashboard/. An auth shell that dashboard.js fills: students get their own progress
    (whoami, loadProgress, my_attempts, catalog); teachers, tutors and admins get the teacher dashboard (teacher.js);
    signed-out visitors are sent to sign in."""
    body = ('<div id="dashboard-root"><noscript>This page needs JavaScript to show your dashboard.</noscript>'
            '<p class="hint">Loading your dashboard…</p></div>')
    write("dashboard/index.html", layout("Dashboard", body, "dashboard/", "dashboard",
                                          [("Home", ""), ("Dashboard", None)], auth=True,
                                          extra=_scripts("trackerkit", "roster", "teacher", "dashboard")))


def build_pricing():
    """Plans and pricing page at /pricing/. Prices are USD; Lemon Squeezy converts and handles VAT.
    Buy buttons go live as CHECKOUT_URLS (site_data.py) are filled; until then they point at the join form."""
    r = "../"
    join = f"{r}profile/"

    sub_names = {"ig-econ": "IGCSE Economics", "ig-cs": "IGCSE Computer Science",
                 "a-econ": "A-Level Economics", "a-cs": "A-Level Computer Science"}
    pp = PADDLE["prices"]
    live = bool(PADDLE["token"])

    def has_ids(plan):
        v = pp.get(plan, {})
        flat = [v] if "m" in v else list(v.values())
        return live and any(x.get("m") or x.get("y") for x in flat)

    def buy(plan, label, per_subject=False):
        if not has_ids(plan):
            return f'<a class="btn ghost" href="{join}">Available at launch</a>'
        sel = ""
        if per_subject:
            opts = "".join(f'<option value="{k}">{esc(v)}</option>' for k, v in sub_names.items())
            sel = f'<select class="subj" aria-label="Subject" data-plan="{plan}">{opts}</select>'
        return f'<div class="buyrow">{sel}<button type="button" class="btn cta-buy" data-plan="{plan}">{label}</button></div>'

    def price(y, m):
        return (f'<p class="price" data-y="{y}" data-m="{m}">'
                f'<span class="amt">${y}</span><span class="per">/year</span></p>')

    def feats(items):
        return '<ul class="feat">' + "".join(f"<li>{esc(t)}</li>" for t in items) + "</ul>"

    def plan(name, price_html, tagline, items, cta, cls="", accent="", badge=""):
        acc = f' data-accent="{accent}"' if accent else ""
        bdg = f'<span class="badge">{esc(badge)}</span>' if badge else ""
        return (f'<article class="plan {cls}"{acc}>{bdg}<h2>{esc(name)}</h2>{price_html}'
                f'<p class="tagline">{esc(tagline)}</p>{feats(items)}<div class="act">{cta}</div></article>')

    free = plan("Free", '<p class="price"><span class="amt">$0</span><span class="per">forever</span></p>',
                "Try the lessons before you pay anything.",
                [f"{FREE_WORD.capitalize()} full sample lessons, no account needed", "Interactive charts and code walkthroughs", "A free account saves your progress"],
                f'<a class="btn ghost" href="{join}">Create a free account</a>')
    basic = plan("Basic", price(100, 10), "One subject, the whole syllabus to learn from.",
                 ["Learn, Watch, Explore and Real world in every chapter", "Every animation and interactive tool",
                  "All chapters and levels in that subject", "Learn on any device"], buy("basic", "Choose Basic", True))
    full = plan("Full", price(200, 20), "Everything for one subject: learn it, then practise it for the exam.",
                ["Everything in Basic", "Practise, Exam questions and Tips & keywords in every chapter",
                 "Unit assessments and topic tests", "Multiple choice marked instantly, written answers self-marked against the mark scheme",
                 "Exam-technique packs", "Priority support"],
                buy("full", "Get Full", True), cls="featured", accent="teal", badge="Most popular")
    allp = plan("All-Access", price(300, 30), "Your choice of four subjects, at all levels, every feature.",
                ["Everything in Full", "Your choice of four subjects, at all levels, every feature", "Priority support",
                 "New content and features as they are added"],
                buy("all", "Go All-Access"))
    teacher = plan("Teacher", price(500, 50), "One teacher, every subject and level.",
                   ["Full content for up to four subjects, at every level", "Mark schemes, model answers and answer keys for every topic test",
                    "Lesson-delivery mode for the classroom", "Add a school licence when you want student seats"],
                   buy("teacher", "Choose Teacher"))
    school = plan("School", '<p class="price"><span class="amt">$50</span><span class="per">/student / subject / year</span></p>',
                  "Whole-school access, managed centrally.",
                  ["Choose the subjects each student takes", "Free teacher accounts and class dashboards",
                   "Seats per subject, from 25, invoiced annually"], f'<a class="btn" href="{r}contact/?topic=school&amp;role=school">Talk to us</a>')

    cycle = ('<div class="cycle" role="group" aria-label="Billing period">'
             '<button type="button" data-cycle="y" class="on" aria-pressed="true">Annual <span class="save">save ~17%</span></button>'
             '<button type="button" data-cycle="m" aria-pressed="false">Monthly</button></div>')
    faq = [("What is the difference between Basic and Full?",
            "Basic is for learning: the Learn, Watch, Explore and Real world sections of every chapter. Full adds the exam side: Practise, "
            "Exam questions, Tips and keywords, unit assessments and topic tests. Every chapter is built the same way, so you always know where things are."),
           ("How does the marking work?",
            "Multiple choice and number questions are marked instantly, so you know straight away whether you were right. Longer written answers "
            "are self-marked against the mark scheme. Comparing your answer with how the marks are awarded is one of the best ways to learn what "
            "examiners reward and how to move up a grade."),
           ("Will more be added?",
            "Yes. We keep expanding the content, the subjects and the features, and your plan covers what is added to it. Homework tracking is planned and is not available yet."),
           ("What does priority support mean?",
            "Messages from Full and All-Access members are answered before the others. Write to support@ascendant.academy or use the contact form on the website."),
           ("Can I cancel any time?",
            "Yes. Cancel whenever you like and you keep access until the end of the period you have paid for. "
            "Monthly plans stop at the next month, annual plans run to the end of the year, and there are no further charges."),
           ("Do you offer refunds?",
            "There is a 14-day money-back guarantee on your first purchase. If it is not for you, get in touch within "
            "two weeks and we will refund it in full, no questions asked."),
           ("What if I change my mind part-way through an annual plan?",
            "After the first 14 days an annual plan is non-refundable and you keep full access until it ends. If you have a "
            "genuine reason, get in touch: any goodwill refund is worked out at the standard monthly price for the months "
            "you have used, not the discounted annual rate."),
           ("Which currency am I charged in?",
            "Prices are shown in US dollars. Prices include VAT and sales tax, so there is nothing added at checkout. You are billed in your local "
            "currency and the tax is handled for you."),
           ("Why is annual cheaper?",
            "Paying for the year up front saves you around 17% against paying monthly: roughly two months free.")]
    faq_html = "".join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in faq)

    body = (
        '<section class="hero"><p class="kicker">Cambridge IGCSE &amp; A-Level · Economics &amp; Computer Science</p>'
        "<h1>One platform instead of a shelf of resources.</h1>"
        '<p class="lead">The full syllabus as interactive lessons, with assessments, model answers, exam practice and '
        "progress tracking in one place: the explaining, practising and marking, built for "
        "Cambridge Economics and Computer Science.</p></section>"
        f"{cycle}"
        '<p id="paid" class="paid" hidden role="status"><strong>Payment successful.</strong> New here? Open the email we sent you and choose '
        '<strong>Create your account</strong> (check spam or junk). Already have an account? <a href="../profile/">Sign in</a>.</p>'
        # Shown over the page the moment checkout completes, so a new buyer cannot miss the next step.
        '<dialog id="paid-pop" class="paid-pop" aria-labelledby="paid-h"><div class="tick" aria-hidden="true">&#10003;</div>'
        '<h2 id="paid-h">Payment successful</h2>'
        '<div id="paid-new"><p class="big">One step left: <strong>create your account</strong>.</p>'
        '<p>We are emailing <strong id="paid-email">the address you paid with</strong>. Open that email and choose '
        '<strong>Create your account</strong> to set your password.</p>'
        '<p class="hint">It can take a minute or two. Check your spam or junk folder. Already had an account with this email? Just sign in.</p>'
        '<p><a class="btn" href="../profile/">Go to sign in</a></p></div>'
        '<div id="paid-in" hidden><p class="big">Thank you. Your new plan is being added to your account.</p>'
        '<p class="hint">It usually appears within a minute or two. If it does not, email ' + SUPPORT_LINK + '.</p>'
        '<p><a class="btn" href="../plan/">Go to My plan</a></p></div>'
        '<form method="dialog"><button class="btn ghost">Close</button></form></dialog>'
        f'<div class="plans-wrap">{free}{basic}{full}{allp}</div>'
        '<section class="sec" aria-labelledby="ts"><h2 id="ts">For teachers and schools</h2>'
        '<p class="lede">Teach with it in the classroom, or roll it out across a whole school.</p>'
        f'<div class="plans-wrap plans-two">{teacher}{school}</div></section>'
        '<p class="hint">Prices in USD per subject (except All-Access, Teacher and School). Converted to your local '
        "currency at checkout. VAT and sales tax are included in the prices shown, with nothing added at checkout.</p>"
        '<p class="hint">Paid plans renew automatically each month or year until you cancel. Payments are processed by '
        'Paddle, our reseller and merchant of record. See the <a href="../terms/">terms</a> and <a href="../refunds/">refund policy</a>.</p>'
        + NOTIFY +
        f'<section class="sec" aria-labelledby="rf"><h2 id="rf">Plans, billing and refunds</h2>'
        f'<div class="faq">{faq_html}</div></section>')

    cfg = json.dumps({"env": PADDLE["env"], "token": PADDLE["token"], "prices": pp}, separators=(",", ":"))
    paddle_js = '<script src="https://cdn.paddle.com/paddle/v2/paddle.js"></script>' if live else ""
    script = (paddle_js + "<script>(function(){"
              f"var CFG={cfg},cycle='y';"
              "function pid(plan,subj){var v=CFG.prices[plan]||{};if(subj)v=v[subj]||{};return v[cycle]||'';}"
              "function sync(){"
              "document.querySelectorAll('.cta-buy').forEach(function(b){var s=document.querySelector('.subj[data-plan='+b.dataset.plan+']');"
              "var ok=!!pid(b.dataset.plan,s&&s.value);b.disabled=!ok;b.title=ok?'':'Not available for this choice yet';});}"
              "function set(c){cycle=c;"
              "document.querySelectorAll('.cycle button').forEach(function(b){b.classList.toggle('on',b.dataset.cycle===c);b.setAttribute('aria-pressed',b.dataset.cycle===c);});"
              "document.querySelectorAll('.price[data-y]').forEach(function(p){"
              "p.querySelector('.amt').textContent='$'+(c==='y'?p.dataset.y:p.dataset.m);"
              "p.querySelector('.per').textContent=c==='y'?'/year':'/month';});sync();}"
              "document.querySelectorAll('.cycle button').forEach(function(b){b.addEventListener('click',function(){set(b.dataset.cycle);});});"
              "document.querySelectorAll('.subj').forEach(function(s){s.addEventListener('change',sync);});"
              "async function showPaid(email){"
              "var s=null;try{s=window.Site&&await Site.session();}catch(e){}"
              "document.getElementById('paid').hidden=false;"
              "document.getElementById('paid-new').hidden=!!s;document.getElementById('paid-in').hidden=!s;"
              "if(email)document.getElementById('paid-email').textContent=email;"
              "document.getElementById('paid-pop').showModal();}"
              "window.showPaid=showPaid;"
              "if(CFG.token&&window.Paddle){"
              "if(CFG.env==='sandbox')Paddle.Environment.set('sandbox');"
              "Paddle.Initialize({token:CFG.token,eventCallback:function(e){if(e.name==='checkout.completed'){"
              "Paddle.Checkout.close();showPaid(e.data&&e.data.customer&&e.data.customer.email);}}});"
              "document.querySelectorAll('.cta-buy').forEach(function(b){b.addEventListener('click',async function(){"
              "var s=document.querySelector('.subj[data-plan='+b.dataset.plan+']'),id=pid(b.dataset.plan,s&&s.value);if(!id)return;"
              "var o={items:[{priceId:id,quantity:1}]};"
              "try{var ses=window.Site&&await Site.session();if(ses&&ses.user.email)o.customer={email:ses.user.email};}catch(e){}"
              "Paddle.Checkout.open(o);});});sync();}"
              "})();</script>")
    write("pricing/index.html", layout("Plans", body, "pricing/", "pricing", [("Home", ""), ("Plans", None)], extra=script + '<script src="../assets/notify.js"></script>'))


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
                                             "tier": arts[x].get("tier", "basic"), "chapterTitle": f"{c['title']}: {ch['title']}"})
                for x in sl:
                    if x not in slugs:
                        slugs.append(x)
                items.append({"label": ch["label"], "title": ch["title"], "url": chapter_info[(ckey, key)]["path"], "slugs": sl, "all": allsl})
            groups.append({"title": title, "chapters": items})
        courses[ckey] = {"title": c["title"], "accent": c["accent"], "url": f"{ckey}/", "groups": groups, "slugs": slugs}
    for x, a in arts.items():
        artifacts.setdefault(x, {"title": a["title"], "url": f"artifacts/{x}/", "role": "review" if is_review(a) else "resource", "tier": a.get("tier", "basic"), "chapterTitle": a["title"]})
    order = [a["slug"] for a in ARTIFACTS]
    assessed = {k: {"pass": v["pass_pct"], "n": len(v["questions"])} for k, v in ASSESSED.items()}
    write("assets/catalog.json", json.dumps({"courses": courses, "artifacts": artifacts, "order": order, "assessed": assessed,
                                               "tests": {k: {"title": v["title"], "marks": v["marks"]} for k, v in TOPIC_TESTS.items()}}, separators=(",", ":")))


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


# Topic tests: topic_tests/<name>.json, one per chapter. 10 MCQ + written questions self-marked against mark points.
# Same rule as assessments: keys stay on this machine (git-ignored) and go to the database through a seed file.
TOPIC_TESTS = {}
for f in sorted((ROOT / "topic_tests").glob("*.json")) if (ROOT / "topic_tests").is_dir() else []:
    d = json.loads(f.read_text(encoding="utf-8"))
    assert d["id"] in {i["path"].rstrip("/") for i in chapter_info.values()}, f"{f.name}: no such chapter {d['id']}"
    ids = [q["id"] for q in d["questions"]]
    assert len(ids) == len(set(ids)), f"{f.name}: duplicate question ids"
    for q in d["questions"]:
        assert q["type"] in ("mcq", "written") and q.get("marks", 0) >= 1, f"{f.name} {q['id']}"
        if q["type"] == "mcq":
            assert q["marks"] == 1 and len(q["opts"]) == 4 and 0 <= int(q["ans"]) < 4, f"{f.name} {q['id']}"
        else:
            assert sum(p["m"] for p in q["points"]) >= q["marks"], f"{f.name} {q['id']}: mark points add up to less than the marks"
    d["mcq_n"] = sum(1 for q in d["questions"] if q["type"] == "mcq")
    d["marks"] = sum(q["marks"] for q in d["questions"])
    TOPIC_TESTS[d["id"]] = d


def build_topic_tests():
    page = (head("Topic test", "Check what you know on this topic. Take it as often as you like: every attempt is saved to your progress.", "Students")
            + '<div id="tt-root"><noscript>This page needs JavaScript.</noscript></div>')
    write("tests/index.html", layout("Topic test", page, "tests/", "dashboard", [("Home", ""), ("Dashboard", "dashboard/"), ("Topic test", None)],
                                     auth=True, extra='<script src="../assets/topictest.js"></script>'))
    page = (head("Test tracker", "Every topic test you have taken, with your scores over time.", "Students")
            + '<div id="tr-root"><noscript>This page needs JavaScript.</noscript></div>')
    write("progress/index.html", layout("Test tracker", page, "progress/", "dashboard", [("Home", ""), ("Dashboard", "dashboard/"), ("Test tracker", None)],
                                        auth=True, extra=_scripts("trackerkit", "tracker")))
    seed = ["-- Generated by build.py from topic_tests/*.json. Run schema.sql first. Safe to run again: it replaces the questions.\n"]
    for d in TOPIC_TESTS.values():
        body = json.dumps(d["questions"], ensure_ascii=False)
        assert "$q$" not in body
        seed.append(f"insert into public.topic_tests (id, title, questions) values ('{d['id']}', $q${d['title']}$q$, $q${body}$q$::jsonb)\n"
                    f"on conflict (id) do update set title = excluded.title, questions = excluded.questions, updated_at = now();\n")
    (ROOT / "supabase" / "topic_tests_seed.sql").write_text("\n".join(seed), encoding="utf-8")


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


# Sign-up nudge for public sample lessons: shown only to signed-out visitors, dismissible for the session.
PUBLIC_CTA_CSS = ("<style id=pub-cta-css>.pub-cta{position:fixed;left:12px;bottom:12px;z-index:2147482999;max-width:330px;box-sizing:border-box;"
                  "padding:14px 36px 14px 16px;background:#fff;color:#16202a;border:1px solid #d9d4c9;border-radius:12px;"
                  "box-shadow:0 6px 24px rgba(0,0,0,.18);font:14px/1.45 -apple-system,Segoe UI,sans-serif}"
                  ".pub-cta b{display:block;font-size:15px;margin-bottom:2px}.pub-cta p{margin:0 0 10px}"
                  ".pub-cta a{display:inline-block;padding:7px 14px;border-radius:8px;background:#2b5d7c;color:#fff;text-decoration:none;font-weight:600}"
                  ".pub-cta button{position:absolute;top:4px;right:6px;border:0;background:none;color:inherit;font-size:20px;line-height:1;cursor:pointer;opacity:.6}"
                  "@media (prefers-color-scheme:dark){:root:not([data-theme=light]) .pub-cta{background:#1b232b;color:#e8edf0;border-color:#2c3842}"
                  ":root:not([data-theme=light]) .pub-cta a{background:#7fb6d6;color:#12171c}}"
                  ":root[data-theme=dark] .pub-cta{background:#1b232b;color:#e8edf0;border-color:#2c3842}:root[data-theme=dark] .pub-cta a{background:#7fb6d6;color:#12171c}"
                  "@media (max-width:600px){.pub-cta{left:8px;right:8px;max-width:none;bottom:60px}}</style>")


def public_cta(home_href):
    return (PUBLIC_CTA_CSS + f'<div class="pub-cta" id="pub-cta" hidden><button type="button" aria-label="Close" '
            f'onclick="this.parentNode.hidden=true;try{{sessionStorage.setItem(\'pubcta\',1)}}catch(e){{}}">&times;</button>'
            f'<b>This is a free sample lesson</b><p>Plans unlock every chapter in your syllabus, with exam questions, progress tracking and topic tests.</p>'
            f'<a href="{home_href}pricing/">See plans</a></div>'
            "<script>window.addEventListener('load',function(){var c=document.getElementById('pub-cta');try{if(sessionStorage.getItem('pubcta'))return}catch(e){}"
            "var show=function(){c.hidden=false};if(!window.Site||!Site.sb){setTimeout(show,6000);return}Site.session().then(function(s){if(!s)setTimeout(show,6000)}).catch(function(){})})</script>")


def inject_pill(text, back_href, back_label, home_href, slug, courses, review=True, crumbs=None, public=False):
    done_btn = f'<button data-done-slug="{slug}" hidden></button><button data-role-toggle="{slug}" hidden></button><button data-role-delete="{slug}" hidden></button><button data-role-restore="{slug}" hidden></button>'
    pill = (f'{PILL_CSS}<div class="site-pill"><button type="button" class="pill-more" aria-label="Menu" onclick="this.parentNode.classList.toggle(&#39;open&#39;)">☰</button><a href="{back_href}">← {esc(back_label)}</a>'
            f'<a href="{home_href}">Home</a><button type="button" title="Light / dark" onclick="{THEME_CLICK}">◐</button>{done_btn}</div>'
            f'{auth_scripts(home_href, courses)}{TAB_SCROLL}{PILL_JS}{TOP_RESET}{SVGFIX}' + (public_cta(home_href) if public else ''))
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


def shell_page(slug, title, courses, tier, split=False):
    r = "../../"
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title><meta name="robots" content="noindex">{favicon_links(r)}{THEME_HEAD}
<style>body{{margin:0;background:#f6f4ef;color:#5a6772;font:16px/1.5 -apple-system,Segoe UI,sans-serif}}#gate-msg{{padding:18vh 20px;text-align:center}}
@media (prefers-color-scheme:dark){{:root:not([data-theme=light]) body{{background:#12171c;color:#9aa8b2}}}}:root[data-theme=dark] body{{background:#12171c;color:#9aa8b2}}</style></head>
<body><p id="gate-msg">Opening lesson…</p>
<script src="{r}assets/config.js"></script>
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
<script src="{r}assets/app.js"></script>
<script src="{r}assets/gateload.js" data-slug="{slug}" data-courses="{",".join(courses)}" data-tier="{tier}"{' data-split="1"' if split else ''}></script>
</body></html>
"""


def build_artifacts():
    master = gate_master()
    seed = []
    n_split, n_whole = [], []
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
                page = f.read_text(encoding="utf-8")
                if rel.name == "index.html":
                    page = reword.apply(keywords.apply(extra_lessons.apply(econ_past.apply(ig_past.apply(igcs_past.apply(page, a["src"]), a["src"]), a["src"]), a["src"]), a["src"]))
                content = bust(inject_pill(page, back, label, depth_root, a["slug"], courses, is_review(a), crumbs, bool(a.get("public"))))
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
            tier = a.get("tier", "basic")
            split = split_full.split(index) if tier == "basic" else None
            (dest / "payload.full.bin").unlink(missing_ok=True)
            if split:  # Practise, Exam questions and Tips & keywords go in a second payload under a Full-only key
                index = split[0]
                (dest / "payload.full.bin").write_bytes(encrypt_payload(master, a["slug"] + ":full", split[1]))
                n_split.append(a["slug"])
            else:
                if tier == "basic":
                    n_whole.append(a["slug"])
            (dest / "payload.bin").write_bytes(encrypt_payload(master, a["slug"], {"index": index, "files": bundle}))
            (dest / "index.html").write_text(bust(shell_page(a["slug"], a["title"], courses, tier, bool(split))), encoding="utf-8")
        if courses:
            seed.append((a["slug"], courses, a.get("tier", "basic")))
    print(f"Full-panel split: {len(n_split)} lessons split, {len(n_whole)} basic lessons left whole: {', '.join(n_whole)}")
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


def write_paddle_seed():
    """supabase/paddle_prices_seed.sql: what each Paddle price id grants. Price ids are public, so this file is committed."""
    rows = []
    for plan, tier in (("basic", "basic"), ("full", "full")):
        for subj, v in PADDLE["prices"][plan].items():
            rows += [(v[c], subj, tier, c, "student") for c in "my" if v[c]]
    v = PADDLE["prices"]["all"]
    rows += [(v[c], "school-all", "vip", c, "student") for c in "my" if v[c]]
    v = PADDLE["prices"]["teacher"]
    rows += [(v[c], None, "full", c, "teacher") for c in "my" if v[c]]
    lines = ["-- Written by build.py from site_data.PADDLE. Safe to rerun: maps each Paddle price id to what it grants (schema.sql, v11)."]
    if rows:
        lines.append("insert into public.paddle_prices (price_id, product, tier, period, kind) values")
        lines.append(",\n".join("  ('%s', %s, '%s', '%s', '%s')" % (i, "null" if p is None else "'%s'" % p, t, c, k) for i, p, t, c, k in rows))
        lines.append("on conflict (price_id) do update set product = excluded.product, tier = excluded.tier, period = excluded.period, kind = excluded.kind;")
        lines.append("delete from public.paddle_prices where price_id not in (%s);" % ",".join("'%s'" % r[0] for r in rows))
    else:
        lines.append("-- No Paddle price ids set yet.")
    (ROOT / "supabase" / "paddle_prices_seed.sql").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    shutil.copytree(ROOT / "assets", OUT / "assets")
    (OUT / ".nojekyll").write_text("")
    (OUT / "CNAME").write_text("ascendant.academy\n")
    SITEMAP.clear()
    build_home()
    if LANDING_PAGE:
        build_landing()
    build_courses()
    build_other_profile()
    build_contact()
    build_legal()
    build_schools()
    build_dashboard()
    build_pricing()
    build_plan()
    write_paddle_seed()
    build_catalog()
    build_assessments()
    build_topic_tests()
    build_artifacts()
    urls = sorted(set(SITEMAP))
    (OUT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                                     + "".join(f"<url><loc>{u}</loc></url>\n" for u in urls) + "</urlset>\n")
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}sitemap.xml\n")
    n = sum(1 for _ in OUT.rglob("index.html"))
    print(f"Built {n} index pages, {len(ARTIFACTS)} artifacts -> {OUT}")


if __name__ == "__main__":
    main()
