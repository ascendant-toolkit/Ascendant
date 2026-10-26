"""AS CS 3.2.1 helpers: expression trees to auto-laid-out circuits, with truth-table checking against mark schemes."""
from ascs import *
from ak15 import *

def AND(*a): return ("AND",) + a
def OR(*a): return ("OR",) + a
def XOR(a, b): return ("XOR", a, b)
def NAND(a, b): return ("NAND", a, b)
def NOR(a, b): return ("NOR", a, b)
def NOT(a): return ("NOT", a)

def ev(t, v):
    if isinstance(t, str): return v[t]
    k, *a = t; a = [ev(x, v) for x in a]
    r = {"AND": all(a), "OR": any(a), "XOR": sum(a) % 2 == 1, "NAND": not all(a), "NOR": not any(a), "NOT": not a[0]}[k]
    return int(r)

def table(t, ins):
    return [ev(t, dict(zip(ins, bits(m, len(ins))))) for m in range(1 << len(ins))]

def check(t, ins, expected, tag):
    got = table(t, ins)
    assert got == expected, f"{tag}: {got} != {expected}"

def net(t, ins, out="X", ystep=54):
    gates = []
    iy = {n: 24 + i * ystep for i, n in enumerate(ins)}
    cnt = [0]
    def walk(x, root=False):
        if isinstance(x, str): return x, None
        k, *kids = x
        res = [walk(c) for c in kids]
        srcs = [r[0] for r in res]
        lv = 1 + max([r[1] for r in res if r[1] is not None], default=-1)
        cnt[0] += 1
        name = out if root else f"G{cnt[0]}"
        gates.append([name, k, srcs, lv, 0])
        return name, lv
    walk(t, True)
    ypos = dict(iy)
    for lv in range(max(g[3] for g in gates) + 1):
        col = [g for g in gates if g[3] == lv]
        for g in col: g[4] = sum(ypos[s] for s in g[2]) / len(g[2])
        col.sort(key=lambda g: g[4])
        for i in range(1, len(col)):
            gap = 40 if col[i][1] == "NOT" or col[i - 1][1] == "NOT" else 58
            if col[i][4] - col[i - 1][4] < gap: col[i][4] = col[i - 1][4] + gap
        for g in col: ypos[g[0]] = g[4]
    return circuit([(n, iy[n]) for n in ins], [tuple(g) for g in gates], outs=[out])

def ttab(t, ins, out="X"):
    rows = [bits(m, len(ins)) + [table(t, ins)[m]] for m in range(1 << len(ins))]
    return ttable(ins, [out], rows)
