"""Runs every Python answer in pp19_code.py against test data. python3 tools/artifact-kit/pp19_check.py"""
import builtins, contextlib, datetime, io, random, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from pp19_code import C

used = set()


def load(*keys, **glob):
    used.update(keys)
    ns = dict(glob)
    exec("".join(C[k] for k in keys), ns)
    return ns


def output(fn, *args):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        fn(*args)
    return buf.getvalue().split()


data = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]
ns = load("linear_s21", arrayData=data)
assert ns["linearSearch"](21) and not ns["linearSearch"](99)

nums = [random.randint(1, 100) for _ in range(99)] + [61]
ns = load("find_w22", DataArray=nums, input=lambda p: "61")
assert ns["FindValues"]() == nums.count(61)

words = ["one", "two"] * 7 + ["one"]
ns = load("find_s26", DataArray=words, input=lambda p: "ONE")
assert output(ns["FindWords"])[3] == "8"

for n in range(1, 25):
    a = sorted(random.sample(range(200), n))
    calls = [
        lambda v: load("bs2d_s22")["BinarySearch"]([a], 0, n - 1, v),
        lambda v: load("bs_s24_41", DataStored=a, NumberItems=n)["BinarySearch"](v),
        lambda v: load("bs_s24_42")["BinarySearch"](a, 0, n - 1, v),
        lambda v: load("bs_s25")["Search"](a, v),
        lambda v: load("bs_w25")["RecursiveBinarySearch"](a, 0, n - 1, v),
    ]
    for f in calls:
        assert all(f(v) == i for i, v in enumerate(a))
        assert f(-5) == f(500) == f(a[0] + 0.5) == -1

for _ in range(50):
    a = random.sample(range(100), 10)
    ns = load("bub_s21", arrayData=a[:])
    ns["bubbleSort"]()
    assert ns["arrayData"] == sorted(a, reverse=True)
    grid = [random.sample(range(100), 10) for _ in range(10)]
    ns = load("bub_s22", ArrayData=[r[:] for r in grid])
    assert ns["ArrayData"] == [sorted(r) for r in grid]
    big = [random.randint(1, 100) for _ in range(100)]
    ns = load("bub_w22", DataArray=big[:])
    output(ns["BubbleSort"])
    assert ns["DataArray"] == sorted(big)
    ns = load("bub_s24", DataStored=a[:], NumberItems=10)
    ns["BubbleSort"]()
    assert ns["DataStored"] == sorted(a)
    assert load("bub_w25")["BubbleSort"](a[:]) == sorted(a)
    assert load("ins_s25")["InsertionSort"](a[:]) == sorted(a)
    ns = load("ins_s24")
    assert ns["RecursiveInsertion"](a[:], 10) == sorted(a) == ns["IterativeInsertion"](a[:], 10)
    s = ["".join(random.choice("abc") for _ in range(random.randint(1, 5))) + str(i) for i in range(15)]
    assert load("ins_s26")["InsertionSort"](s[:]) == sorted(s)
    ns = load("bub_s26", DataArray=s[:])
    ns["SortLength"]()
    assert [len(x) for x in ns["DataArray"]] == sorted(len(x) for x in s)
    cmp = lambda x, y: 1 if x < y else 2
    assert load("bub_w24_41", CompareStrings=cmp)["Bubble"](s[:]) == sorted(s)
    hs = [[str(i), str(random.randint(1, 5)), str(random.randint(1, 30))] for i in range(7)]
    got = load("bub_w24_42")["SortScores"]([r[:] for r in hs])
    key = lambda r: (-int(r[1]), -int(r[2]))
    assert [key(r) for r in got] == sorted(key(r) for r in hs)
    jobs = [[i, random.randint(1, 10)] for i in range(10)]
    ns = load("ins_w22", Jobs=[r[:] for r in jobs], NumberOfJobs=10)
    ns["InsertionSort"]()
    assert ns["Jobs"] == sorted(jobs, key=lambda r: r[1])

values = [10, 5, 15, 8, 12, 6, 20, 11, 9, 4]
it = iter(values)
ns = load("add_w21", "in_w21", input=lambda p: str(next(it)))
arr, root, free = [[0, 0, 0] for _ in range(20)], -1, 0
for _ in values:
    arr, root, free = ns["AddNode"](arr, root, free)
assert arr[0] == [1, 10, 2] and arr[1] == [9, 5, 3]   # first rows of the mark-scheme output
assert output(ns["InOrder"], arr, root) == [str(v) for v in sorted(values)]

tree = [[1, 20, 5], [2, 15, -1], [-1, 3, 3], [-1, 9, 4], [-1, 10, -1], [-1, 58, -1], [-1, -1, -1]]
ns = load("search_w22", "post_w22", ArrayNodes=tree)
assert ns["SearchValue"](0, 15) == 1 and ns["SearchValue"](0, 99) == -1
assert output(ns["PostOrder"], 0) == "10 9 3 15 58 20".split()

ns = load("add_s26", "in_s26", BinaryTree=[[-1, -1, -1] for _ in range(100)], TreeRootPointer=-1, FirstFreeNodePointer=0)
values = [50, 26, 120, 236, 2, 16, 67, 49, 165, 15]
for v in values:
    ns["AddNode"](v)
assert output(ns["InOrder"], 0) == [str(v) for v in sorted(values)]

ns = load("add_w25", TreeArray=[[-1, -1, -1] for _ in range(50)], RootPointer=-1, FreeNode=0)
for v in [20, 30, 10]:
    ns["AddNode"](v)
assert ns["TreeArray"][0] == [2, 20, 1]

ns = load("node_s24", "getset_s24", "tree_s24")
t = ns["TreeClass"]()
assert output(t.OutputTree) == ["No", "nodes"]
for v in [10, 11, 5, 1, 20, 7, 15]:
    t.InsertNode(ns["Node"](v))
assert output(t.OutputTree)[:6] == "2 10 1 -1 11 4".split()

ns = load("node_s25", "tree_s25", "out_s25")
t = ns["Tree"](ns["Node"](10))
for v in [20, 5, 15, 7]:
    t.Insert(ns["Node"](v))
assert output(ns["OutputInOrder"], t.GetRootNode()) == "5 7 10 15 20".split()

ns = load("emp", "emp_methods", "mgr", "mgr_pay")
m = ns["Manager"](10.0, 20.0, "02586", "Manager")
m.SetPay(1, 10)
assert abs(m.GetTotalPay() - 220) < 1e-9 and m.GetEmployeeNumber() == "02586"

ns = load("char41", "char41_methods", "bike", "bike_move")
j, k = ns["Character"]("Jack", 50, 50), ns["BikeCharacter"]("Karla", 100, 50)
j.Move("right")
k.Move("down")
assert (j.GetXPosition(), j.GetYPosition(), k.GetXPosition(), k.GetYPosition()) == (60, 50, 100, 30)

ns = load("char42", "char42_methods", "magic", "magic_learn")
f = ns["MagicCharacter"]("fire", "Light", datetime.date(2018, 3, 3), 75, 22)
f.Learn()
assert abs(f.GetIntelligence() - 90) < 1e-9 and f.ReturnAge() == 5

assert used == set(C), set(C) - used
print("all", len(C), "answers pass")
