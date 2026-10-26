"""AS CS chapter 4.2/4.3 helpers: an emulator for the Cambridge 9618 assembly instruction set, trace-table HTML and bit-manipulation maths."""
from ascs import *

def val(tok):
    tok = tok.strip()
    if tok[0] == "#": return int(tok[1:])
    if tok[0] == "B": return int(tok[1:], 2)
    if tok[0] == "&": return int(tok[1:], 16)
    return None

def run(prog, mem, acc=0, ix=0, start=None, inputs=(), maxsteps=200, stop_at=None):
    """prog: {addr: 'OP operand'}; mem: {addr: int}. Returns (rows, state). rows: dict(addr, ins, acc, ix, mem(copy), out)."""
    m = dict(mem); pc = start if start is not None else min(prog); flag = False; rows = []; inp = list(inputs); out = ""
    for _ in range(maxsteps):
        ins = prog[pc]; parts = ins.split(None, 1); op = parts[0]; a = parts[1] if len(parts) > 1 else None
        nxt = max(k for k in prog if k <= pc) if False else None
        keys = sorted(prog); nxt = keys[keys.index(pc) + 1] if keys.index(pc) + 1 < len(keys) else None
        o = ""
        imm = val(a) if a else None
        def rd(): return m[int(a)]
        if op == "LDM": acc = imm
        elif op == "LDD": acc = rd()
        elif op == "LDI": acc = m[m[int(a)]]
        elif op == "LDX": acc = m[int(a) + ix]
        elif op == "LDR": ix = imm
        elif op == "MOV": ix = acc
        elif op == "STO": m[int(a)] = acc
        elif op == "ADD": acc += imm if imm is not None else rd()
        elif op == "SUB": acc -= imm if imm is not None else rd()
        elif op == "INC":
            if a == "IX": ix += 1
            else: acc += 1
        elif op == "DEC":
            if a == "IX": ix -= 1
            else: acc -= 1
        elif op == "CMP": flag = acc == (imm if imm is not None else rd())
        elif op == "JPE": nxt = int(a) if flag else nxt
        elif op == "JPN": nxt = int(a) if not flag else nxt
        elif op == "JMP": nxt = int(a)
        elif op == "IN": acc = ord(inp.pop(0))
        elif op == "OUT": o = chr(acc); out += o
        elif op == "AND": acc &= imm if imm is not None else rd()
        elif op == "OR": acc |= imm if imm is not None else rd()
        elif op == "XOR": acc ^= imm if imm is not None else rd()
        elif op == "LSL": acc = (acc << imm) & 255
        elif op == "LSR": acc = acc >> imm
        elif op == "END": nxt = None
        rows.append(dict(addr=pc, ins=ins, acc=acc, ix=ix, mem=dict(m), out=o))
        if nxt is None: break
        pc = nxt
    return rows, dict(acc=acc, ix=ix, mem=m, out=out)

def trace_html(rows, mem0, cols, acc0=None, ix0=None, show_ix=True, show_out=False, title=True):
    """Trace table: initial row then one row per instruction; unchanged cells blank like the paper's mark scheme."""
    head = "<tr><th>Instruction address</th><th>ACC</th>" + "".join(f"<th>{c}</th>" for c in cols) + ("<th>IX</th>" if show_ix else "") + ("<th>Output</th>" if show_out else "") + "</tr>"
    h = '<div class="tw"><table class="t mono">' + head
    h += "<tr><td></td><td>" + ("" if acc0 is None else acc0) + "</td>" + "".join(f"<td>{mem0[c]}</td>" for c in cols) + (f"<td>{ix0 if ix0 is not None else ''}</td>" if show_ix else "") + ("<td></td>" if show_out else "") + "</tr>"
    pm = dict(mem0); pacc = acc0; pix = ix0
    for r in rows:
        cells = [f"<td>{r['addr']}</td>", f"<td>{r['acc'] if r['acc'] != pacc else ''}</td>"]
        for c in cols: cells.append(f"<td>{r['mem'][c] if r['mem'][c] != pm[c] else ''}</td>")
        if show_ix: cells.append(f"<td>{r['ix'] if r['ix'] != pix else ''}</td>")
        if show_out: cells.append(f"<td>{r['out']}</td>")
        h += "<tr>" + "".join(cells) + "</tr>"; pm = r["mem"]; pacc = r["acc"]; pix = r["ix"]
    return h + "</table></div>"

def b8(n): return format(n & 255, "08b")
def sp(s): return s[:4] + " " + s[4:]

def result_table(items):
    """items: list of (before_bits, instruction, after_bits) -> HTML."""
    h = '<div class="tw"><table class="t mono"><tr><th>ACC before</th><th>Instruction</th><th>ACC after</th></tr>'
    for b, i, a in items: h += f"<tr><td>{b}</td><td>{i}</td><td><b>{a}</b></td></tr>"
    return h + "</table></div>"

def acc_after(before, ins, mem=None):
    """Run a single bit instruction on an 8-bit string; returns 8-bit string with a space after bit 4."""
    rows, st = run({0: ins}, mem or {}, acc=int(before.replace(" ", ""), 2))
    return sp(b8(st["acc"]))
