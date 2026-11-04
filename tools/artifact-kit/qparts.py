"""Puts each sub-question, (a) (b) (c) and (i) (ii) (iii), on its own line inside exam question summaries.
Used by assemble.py for A Level CS pages (slugs starting ac-)."""
import re

_SUM = re.compile(r'(<summary>.*?<span class="mark">[^<]*</span>)(.*?)(</summary>)', re.S)
_MARK = re.compile(r'(?:(?<=^)|(?<=[\s>]))\((?:[a-h]|i{1,3}|iv|v|vi{0,3}|ix|x)\)(?=\s)')
_ROMAN = re.compile(r'^\((?:i{1,3}|iv|v|vi{0,3}|ix|x)\)$')


def _split(text):
    # leave code blocks alone, split only the prose around them
    segs = re.split(r'(<pre.*?</pre>)', text, flags=re.S)
    toks = []
    for s in segs:
        if s.startswith('<pre'):
            toks.append(('code', s))
            continue
        pos = 0
        for m in _MARK.finditer(s):
            if m.start() > pos:
                toks.append(('text', s[pos:m.start()]))
            toks.append(('mark', m.group(0)))
            pos = m.end()
        toks.append(('text', s[pos:]))
    return toks


def fix_summary(m):
    head, text, tail = m.groups()
    if not _MARK.search(re.sub(r'<pre.*?</pre>', '', text, flags=re.S)):
        return m.group(0)
    lines, cur, cls = [], '', 'qi'
    for kind, t in _split(text):
        if kind == 'mark':
            if cur.strip():
                lines.append((cls, cur.strip()))
            cls = 'qp sub' if _ROMAN.match(t) else 'qp'
            cur = t + ' '
        else:
            cur += t.lstrip() if cur.endswith(') ') else t
    if cur.strip():
        lines.append((cls, cur.strip()))
    body = ''.join(f'<span class="{c}">{t}</span>' for c, t in lines)
    return f'{head}<span class="qb">{body}</span>{tail}'


def split_parts(html):
    return _SUM.sub(fix_summary, html)


CSS = '''
details.eq>summary .qb{flex-basis:100%;display:block}
details.eq>summary .qp,details.eq>summary .qi{display:block;margin-top:6px}
details.eq>summary .qp.sub{margin-left:1.6em}
'''
