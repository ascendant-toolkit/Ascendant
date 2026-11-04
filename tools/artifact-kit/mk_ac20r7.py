"""20.1.2 extra resource: writing a binary tree with classes. Run: python3 tools/artifact-kit/mk_ac20r7.py"""
from ac20r import *

learn = '''
  <div class="card big"><h3>This page in five sentences</h3>
  <p>A <b>binary tree</b> is a structure where each item, a <b>node</b>, can point to at most two others: a <b>left</b> child and a <b>right</b> child. In a <b>binary search tree</b> every value in the left part is smaller than the node and every value in the right part is larger or equal, so searching can ignore half the tree at each step. In an object-oriented program it is written as two classes: a <b>Node</b> that holds one value and two pointers, and a <b>Tree</b> that holds the root node. Writing it uses every idea from the earlier pages: a <b>constructor</b>, <b>private</b> data, <b>getters and setters</b>, <b>containment</b>, and, for a variation, <b>inheritance</b>.</p></div>

  <h2>1 · Words to know</h2>
  <div class="tw"><table class="t">
    <tr><th>Term</th><th>Meaning</th></tr>
    <tr><td>Node</td><td>One item in the tree: a value and two pointers</td></tr>
    <tr><td>Root</td><td>The top node; the only one nothing points to</td></tr>
    <tr><td>Left / right pointer</td><td>Where the left and right child are, or <code>None</code> (<code>NULL</code> in pseudocode) if there is none</td></tr>
    <tr><td>Leaf</td><td>A node with no children: both pointers are empty</td></tr>
    <tr><td>Subtree</td><td>A node and everything below it</td></tr>
  </table></div>
  <p class="note">The rule used on this page: a new value smaller than the node goes left; a value equal or larger goes right.</p>

  <h2>2 · Which concept does what</h2>
  <div class="tw"><table class="t">
    <tr><th>Concept</th><th>Where it appears in the tree</th></tr>
    <tr><td>Constructor</td><td><code>Node(NewData)</code> sets the value and starts both pointers empty. <code>Tree()</code> starts with no root</td></tr>
    <tr><td>Encapsulation</td><td>Data and pointers are private. Other code uses the methods</td></tr>
    <tr><td>Getters and setters</td><td><code>GetData</code>, <code>GetLeft</code>, <code>GetRight</code>, <code>SetLeft</code>, <code>SetRight</code></td></tr>
    <tr><td>Containment</td><td>The Tree <b>has</b> a root Node, and each Node <b>has</b> a left and right Node</td></tr>
    <tr><td>Inheritance</td><td>A <code>CountTree</code> <b>is a</b> Tree that also counts its insertions</td></tr>
    <tr><td>Polymorphism</td><td><code>Insert()</code> is called the same way on a Tree or a CountTree, and each does its own version</td></tr>
  </table></div>

  <h2>3 · The Node class</h2>
  ''' + both('''class Node:
    # Data : INTEGER
    # LeftPointer : Node
    # RightPointer : Node
    def __init__(self, NewData):
        self.__Data = NewData
        self.__LeftPointer = None
        self.__RightPointer = None

    def GetData(self):
        return self.__Data
    def GetLeft(self):
        return self.__LeftPointer
    def GetRight(self):
        return self.__RightPointer
    def SetLeft(self, NewLeft):
        self.__LeftPointer = NewLeft
    def SetRight(self, NewRight):
        self.__RightPointer = NewRight''', '''CLASS Node
  PRIVATE Data : INTEGER
  PRIVATE LeftPointer : Node
  PRIVATE RightPointer : Node
  PUBLIC PROCEDURE NEW(NewData : INTEGER)
    Data <- NewData
    LeftPointer <- NULL
    RightPointer <- NULL
  ENDPROCEDURE
  PUBLIC FUNCTION GetData() RETURNS INTEGER
    RETURN Data
  ENDFUNCTION
  PUBLIC FUNCTION GetLeft() RETURNS Node
    RETURN LeftPointer
  ENDFUNCTION
  PUBLIC FUNCTION GetRight() RETURNS Node
    RETURN RightPointer
  ENDFUNCTION
  PUBLIC PROCEDURE SetLeft(NewLeft : Node)
    LeftPointer <- NewLeft
  ENDPROCEDURE
  PUBLIC PROCEDURE SetRight(NewRight : Node)
    RightPointer <- NewRight
  ENDPROCEDURE
ENDCLASS''') + '''
  <p>The constructor takes only the value. The two pointers are <b>fixed starting values</b>: a new node has no children yet. The setters exist so the Tree can attach children later, because the Node's pointers are private.</p>

  <h2>4 · The Tree class: constructor and Insert</h2>
  ''' + both('''class Tree:
    # Root : Node
    def __init__(self):
        self.__Root = None

    def Insert(self, NewData):
        NewNode = Node(NewData)
        if self.__Root is None:
            self.__Root = NewNode
        else:
            Current = self.__Root
            Placed = False
            while not Placed:
                if NewData < Current.GetData():
                    if Current.GetLeft() is None:
                        Current.SetLeft(NewNode)
                        Placed = True
                    else:
                        Current = Current.GetLeft()
                else:
                    if Current.GetRight() is None:
                        Current.SetRight(NewNode)
                        Placed = True
                    else:
                        Current = Current.GetRight()''', '''CLASS Tree
  PRIVATE Root : Node
  PUBLIC PROCEDURE NEW()
    Root <- NULL
  ENDPROCEDURE
  PUBLIC PROCEDURE Insert(NewData : INTEGER)
    NewNode <- NEW Node(NewData)
    IF Root = NULL
      THEN
        Root <- NewNode
      ELSE
        Current <- Root
        Placed <- FALSE
        WHILE Placed = FALSE
          IF NewData < Current.GetData()
            THEN
              IF Current.GetLeft() = NULL
                THEN
                  Current.SetLeft(NewNode)
                  Placed <- TRUE
                ELSE
                  Current <- Current.GetLeft()
              ENDIF
            ELSE
              IF Current.GetRight() = NULL
                THEN
                  Current.SetRight(NewNode)
                  Placed <- TRUE
                ELSE
                  Current <- Current.GetRight()
              ENDIF
          ENDIF
        ENDWHILE
    ENDIF
  ENDPROCEDURE
ENDCLASS''') + '''
  <p>Notice what the Tree never does: it never touches <code>__Data</code> or a pointer directly. It calls <code>GetData()</code>, <code>GetLeft()</code> and <code>SetLeft()</code>. That is encapsulation at work. The new node is created <b>before</b> it is attached, as in containment.</p>

  <h2>5 · Search and in-order traversal</h2>
  ''' + both('''    def Search(self, Target):
        Current = self.__Root
        while Current is not None:
            if Target == Current.GetData():
                return True
            elif Target < Current.GetData():
                Current = Current.GetLeft()
            else:
                Current = Current.GetRight()
        return False

    def InOrder(self):
        self.__TraverseFrom(self.__Root)

    def __TraverseFrom(self, ThisNode):
        if ThisNode is not None:
            self.__TraverseFrom(ThisNode.GetLeft())
            print(ThisNode.GetData())
            self.__TraverseFrom(ThisNode.GetRight())''', '''  PUBLIC FUNCTION Search(Target : INTEGER) RETURNS BOOLEAN
    Current <- Root
    WHILE Current <> NULL
      IF Target = Current.GetData()
        THEN
          RETURN TRUE
        ELSE
          IF Target < Current.GetData()
            THEN
              Current <- Current.GetLeft()
            ELSE
              Current <- Current.GetRight()
          ENDIF
      ENDIF
    ENDWHILE
    RETURN FALSE
  ENDFUNCTION

  PUBLIC PROCEDURE InOrder()
    CALL TraverseFrom(Root)
  ENDPROCEDURE

  PRIVATE PROCEDURE TraverseFrom(ThisNode : Node)
    IF ThisNode <> NULL
      THEN
        CALL TraverseFrom(ThisNode.GetLeft())
        OUTPUT ThisNode.GetData()
        CALL TraverseFrom(ThisNode.GetRight())
    ENDIF
  ENDPROCEDURE''') + '''
  <p>These two methods belong inside <code>Tree</code>. In-order visits the left subtree, then the node, then the right subtree, so a search tree prints in sorted order. The helper is private: outside code calls <code>InOrder()</code>, and the recursion inside is hidden.</p>

  <h2>6 · Using the tree</h2>
  <div class="code">''' + pc('''MyTree = Tree()
for Value in [50, 30, 70, 20, 40, 60]:
    MyTree.Insert(Value)
print(MyTree.Search(60))   # True
print(MyTree.Search(45))   # False
MyTree.InOrder()           # 20 30 40 50 60 70, one per line''') + '''</div>

  <h2>7 · A child class: CountTree</h2>
  <p>A tree that also counts how many values have been inserted. It inherits everything and <b>overrides</b> <code>Insert</code>, calling the parent's version first.</p>
  ''' + both('''class CountTree(Tree):
    # Count : INTEGER
    def __init__(self):
        super().__init__()
        self.__Count = 0

    def Insert(self, NewData):
        super().Insert(NewData)
        self.__Count = self.__Count + 1

    def GetCount(self):
        return self.__Count''', '''CLASS CountTree INHERITS Tree
  PRIVATE Count : INTEGER
  PUBLIC PROCEDURE NEW()
    SUPER.NEW()
    Count <- 0
  ENDPROCEDURE
  PUBLIC PROCEDURE Insert(NewData : INTEGER)
    SUPER.Insert(NewData)
    Count <- Count + 1
  ENDPROCEDURE
  PUBLIC FUNCTION GetCount() RETURNS INTEGER
    RETURN Count
  ENDFUNCTION
ENDCLASS''') + '''
  <p>The child's constructor calls the parent's first (so the root is set up), then sets its own attribute. Because both classes have <code>Insert</code>, code that holds a list of trees can call <code>Insert</code> on each without checking which kind it is: polymorphism.</p>
'''

watch = '''
  <h2>1 · Inserting six values</h2><p>Press Play, or click the steps.</p><div id="stA"></div>
  <h2>2 · Searching for 60, and for 45</h2><div id="stB"></div>
  <h2>3 · In-order traversal</h2><div id="stC"></div>
  <h2>4 · The objects behind the picture</h2><div id="stD"></div>
'''

PAR = {30: 50, 70: 50, 20: 30, 40: 30, 60: 70, 80: 70}
POS = {50: (380, 40), 30: (230, 105), 70: (530, 105), 20: (150, 170), 40: (310, 170), 60: (450, 170), 80: (610, 170)}


def tree(vals, hl=None, path=(), extra=()):
    o = []
    for v in vals:
        if v in PAR and PAR[v] in vals:
            o.append(dict(k="edge", a=[*POS[PAR[v]], *POS[v]]))
    for v in vals:
        o.append(dict(k="node", x=POS[v][0], y=POS[v][1], v=v, c="f3" if v == hl else "f2" if v in path else "f1"))
    return o + list(extra)


FULL = [50, 30, 70, 20, 40, 60]
msg = lambda s: txt(20, 238, s, "sm", 1)

stA = stepper("stA", "Insert 50, 30, 70, 20, 40, 60", 760, 255, [
    ("The tree is empty: <code>Root</code> is <code>None</code>. <code>Insert(50)</code> makes a Node and, because there is no root, stores it as the Root.", tree([50], 50, (), [msg("Insert(50): Root is None, so 50 becomes the Root")])),
    ("<code>Insert(30)</code>: 30 is less than 50, so go left. The left pointer is empty, so <code>SetLeft</code> attaches the new node.", tree([50, 30], 30, (50,), [msg("30 < 50: left. Left of 50 is empty: SetLeft")])),
    ("<code>Insert(70)</code>: 70 is not less than 50, so go right. The right pointer is empty: <code>SetRight</code>.", tree([50, 30, 70], 70, (50,), [msg("70 >= 50: right. Right of 50 is empty: SetRight")])),
    ("<code>Insert(20)</code>: less than 50, go left to 30; less than 30, go left. Empty, so attach with <code>SetLeft</code> on the node 30.", tree([50, 30, 70, 20], 20, (50, 30), [msg("20 < 50: left. 20 < 30: left. Empty: SetLeft on 30")])),
    ("<code>Insert(40)</code>: less than 50, go left to 30; not less than 30, go right. Empty: <code>SetRight</code> on 30.", tree([50, 30, 70, 20, 40], 40, (50, 30), [msg("40 < 50: left. 40 >= 30: right. Empty: SetRight on 30")])),
    ("<code>Insert(60)</code>: not less than 50, go right to 70; less than 70, go left. Empty: <code>SetLeft</code> on 70.", tree(FULL, 60, (50, 70), [msg("60 >= 50: right. 60 < 70: left. Empty: SetLeft on 70")])),
    ("Done. Everything to the left of a node is smaller and everything to the right is larger or equal.", tree(FULL, None, (), [msg("left smaller, right larger or equal, at every node")]))])

stB = stepper("stB", "Search follows one path", 760, 255, [
    ("<code>Search(60)</code> starts at the root. <code>Current</code> is the node 50.", tree(FULL, 50, (), [msg("Target 60. Current = 50")])),
    ("60 is not equal to 50 and is larger, so <code>Current = Current.GetRight()</code>. Half the tree is ignored.", tree(FULL, 70, (50,), [msg("60 > 50: go right. Current = 70")])),
    ("60 is less than 70, so <code>Current = Current.GetLeft()</code>.", tree(FULL, 60, (50, 70), [msg("60 < 70: go left. Current = 60")])),
    ("60 equals the data in the current node: <b>True</b> after three comparisons.", tree(FULL, 60, (50, 70), [msg("60 = 60: return True")])),
    ("<code>Search(45)</code>: 45 < 50 left to 30; 45 >= 30 right to 40; 45 >= 40 right, but the right pointer of 40 is empty.", tree(FULL, 40, (50, 30), [msg("45: 50 left, 30 right, 40 right: pointer is None")])),
    ("<code>Current</code> is now <code>None</code>, so the loop ends and the method returns <b>False</b>.", tree(FULL, None, (50, 30, 40), [msg("Current is None: return False")]))])

ordr = lambda l: txt(20, 238, "output: " + " ".join(str(x) for x in l), "lbl bd", 1)
stC = stepper("stC", "In-order traversal", 760, 255, [
    ("<code>InOrder()</code> calls the private helper with the root. Rule: left subtree first, then this node, then the right subtree.", tree(FULL, 50, (), [ordr([])])),
    ("From 50 go left to 30, then left to 20. Node 20 has no left child, so the left call ends at once.", tree(FULL, 20, (50, 30), [ordr([])])),
    ("Now 20 is printed. Its right call also ends at once.", tree(FULL, 20, (50, 30), [ordr([20])])),
    ("Back at 30: the left subtree is done, so print 30, then go right to 40 and print it.", tree(FULL, 40, (50,), [ordr([20, 30, 40])])),
    ("Back at 50: the whole left subtree is done, so print 50.", tree(FULL, 50, (), [ordr([20, 30, 40, 50])])),
    ("Go right to 70, then left to 60. Print 60.", tree(FULL, 60, (70,), [ordr([20, 30, 40, 50, 60])])),
    ("Back at 70: print 70. The values came out in sorted order.", tree(FULL, 70, (), [ordr([20, 30, 40, 50, 60, 70])]))])

TR = cls(20, 20, 180, "MyTree (Tree)", ["__Root: Node 50"], "f1", 22)
N50 = lambda c="f1": cls(260, 20, 240, "Node 50", ["__Data: 50", "__LeftPointer: Node 30", "__RightPointer: Node 70"], c, 22)
N30 = cls(40, 150, 250, "Node 30", ["__Data: 30", "__LeftPointer: Node 20", "__RightPointer: Node 40"], "f1", 22)
N70 = cls(400, 150, 260, "Node 70", ["__Data: 70", "__LeftPointer: Node 60", "__RightPointer: None"], "f1", 22)
stD = stepper("stD", "Containment: objects holding objects", 760, 290, [
    ("The Tree object has one attribute, <code>__Root</code>. Its value is another object: a Node.", [TR, N50("f3"), arr(202, 52, 256, 52, "r")]),
    ("That Node has a value and two pointer attributes, which are also Nodes (or <code>None</code>).", [TR, N50("f2"), arr(202, 52, 256, 52, "r"), txt(520, 60, "has-a: three attributes", "sm")]),
    ("Follow the left pointer to another Node object, and the right pointer to a second one.", [TR, N50(), arr(202, 52, 256, 52, "r"), N30, N70, arr(300, 130, 220, 148, "d"), arr(440, 130, 520, 148, "d")]),
    ("The tree diagram is these objects joined by pointers. Node 70's right pointer is <code>None</code>: no right child.", [TR, N50(), arr(202, 52, 256, 52, "r"), N30, N70, arr(300, 130, 220, 148, "d"), arr(440, 130, 520, 148, "d"), txt(400, 275, "None means no child", "lbl bd t3")])])

explore = '''
  <h2>Lab 1 · Build your own tree</h2>
  <p>Insert values and watch where each one lands. Then search for a value or print the tree in order.</p>
  <div class="card"><div class="btnrow"><label>Value <input id="tV" type="number" value="25" style="width:5rem"></label><button class="b pri" id="tI">Insert</button><button class="b" id="tS">Search</button><button class="b" id="tO">InOrder()</button><button class="b" id="tX">New tree</button></div>
    <div id="tD"></div><div class="verdict" id="tL"></div></div>

  <h2>Lab 2 · Spot the mistake</h2>
  <div class="card"><div id="eB" class="btnrow"></div><div id="eO"></div></div>
'''

lab = r'''
(function () {
  let root, n, hl, msg;
  const reset = () => { root = null; n = 0; hl = []; msg = "Insert some values. The tree starts empty."; [50, 30, 70].forEach((v) => ins(v)); hl = []; msg = "A starter tree of 50, 30 and 70. Insert more values."; draw(); };
  const ins = (v) => {
    const node = { v, l: null, r: null }; n++; hl = [];
    if (!root) { root = node; hl = [v]; return "Root is empty, so " + v + " becomes the Root."; }
    let c = root, said = [];
    for (;;) {
      hl.push(c.v);
      if (v < c.v) { said.push(v + " < " + c.v + ": left"); if (!c.l) { c.l = node; hl.push(v); return said.join(", ") + ". Left of " + c.v + " is empty: SetLeft."; } c = c.l; }
      else { said.push(v + " >= " + c.v + ": right"); if (!c.r) { c.r = node; hl.push(v); return said.join(", ") + ". Right of " + c.v + " is empty: SetRight."; } c = c.r; }
    }
  };
  const draw = () => {
    let idx = 0, maxd = 0; const all = [];
    const place = (nd, d) => { if (!nd) return; place(nd.l, d + 1); nd.i = idx++; nd.d = d; maxd = Math.max(maxd, d); all.push(nd); place(nd.r, d + 1); };
    place(root, 0);
    const sp = Math.min(60, 700 / Math.max(idx, 1)), X = (nd) => 380 - ((idx - 1) * sp) / 2 + nd.i * sp, Y = (nd) => 32 + nd.d * 58;
    let s = "";
    all.forEach((nd) => { if (nd.l) s += SV.line(X(nd), Y(nd), X(nd.l), Y(nd.l), "ax"); if (nd.r) s += SV.line(X(nd), Y(nd), X(nd.r), Y(nd.r), "ax"); });
    all.forEach((nd) => { s += SV.circle(X(nd), Y(nd), 21, "cell") + SV.circle(X(nd), Y(nd), 21, hl.includes(nd.v) ? "f3" : "f1", { opacity: 0.6 }) + SV.circle(X(nd), Y(nd), 21, "ax", { fill: "none" }) + SV.text(X(nd), Y(nd) + 6, nd.v, "lbl bd", { "text-anchor": "middle" }); });
    $("#tD").innerHTML = `<svg viewBox="0 0 760 ${60 + maxd * 58 + 20}" style="width:100%;height:auto">${s}</svg>`;
    $("#tL").textContent = msg;
  };
  const val = () => parseInt($("#tV").value, 10);
  $("#tI").onclick = () => { const v = val(); if (isNaN(v)) { msg = "Type a whole number first."; } else if (n >= 13) { msg = "That is enough nodes for this lab. Press New tree."; } else msg = ins(v); draw(); };
  $("#tS").onclick = () => {
    const v = val(); hl = []; if (isNaN(v)) { msg = "Type a whole number first."; draw(); return; }
    let c = root, said = [];
    while (c) { hl.push(c.v); if (v === c.v) { msg = "Visited " + hl.join(", ") + ": found " + v + ". Search returns True."; draw(); return; } said.push(c.v); c = v < c.v ? c.l : c.r; }
    msg = "Visited " + said.join(", ") + ": reached an empty pointer. Search returns False."; draw();
  };
  $("#tO").onclick = () => { const out = []; const go = (nd) => { if (nd) { go(nd.l); out.push(nd.v); go(nd.r); } }; go(root); hl = out.slice(); msg = "InOrder() prints: " + out.join(" ") + ". Always sorted."; draw(); };
  $("#tX").onclick = reset; reset();
})();

btnTable("eB", "eO", [
  ["Node constructor without pointers", "def __init__(self, NewData): self.__Data = NewData", "GetLeft() fails: the pointer attributes were never created", "Set __LeftPointer and __RightPointer to None in the constructor"],
  ["Reaching into the Node", "Current.__LeftPointer = NewNode  # inside Tree", "The pointer is private to Node, so Tree cannot use it directly", "Current.SetLeft(NewNode)"],
  ["No setters for the pointers", "class Node with GetLeft but no SetLeft", "The Tree has no way to attach a new node", "Add SetLeft and SetRight"],
  ["Attaching the data, not a node", "Current.SetLeft(NewData)", "The pointer now holds a number, not a Node, so GetLeft().GetData() fails", "Create NewNode = Node(NewData) and attach that"],
  ["Forgetting the empty tree", "Current = self.__Root; Current.GetData()  # Root is None", "AttributeError on an empty tree", "Test self.__Root is None first"],
  ["Child with no parent constructor", "class CountTree(Tree): def __init__(self): self.__Count = 0", "The Root attribute is never created, so Insert fails", "super().__init__() first"],
  ["Using the wrong comparison", "if NewData > Current.GetData(): go left", "The tree is built the wrong way round and search fails", "Smaller goes left, larger or equal goes right"]
], ["Mistake", "Code", "What goes wrong", "Fix"]);
''' + CLASSIFY("cl1", "Which concept does each line show?", ["Constructor", "Getter or setter", "Containment", "Inheritance", "Encapsulation (private)"],
    [("def __init__(self, NewData):", 0), ("def GetLeft(self): return self.__LeftPointer", 1), ("self.__Root = NewNode", 2), ("class CountTree(Tree):", 3), ("self.__LeftPointer = None", 4), ("def SetRight(self, NewRight):", 1), ("super().__init__()", 3), ("Tree holds a Root that is a Node object", 2), ("self.__Count = 0 inside CountTree's constructor", 0), ("Pointers can only be changed through SetLeft and SetRight", 4)],
    "Constructor sets starting values; getters and setters give controlled access; containment is an attribute that is an object; inheritance is the child taking the parent; private data is encapsulation.") + ORDER(
    "Put the steps of Insert in order for a tree that already has a root.",
    ["Create the new Node from the value", "Start Current at the Root", "Compare the value with Current's data", "Move to the left or right child if it is not empty", "Repeat until the chosen child is empty", "Attach the new Node with SetLeft or SetRight"],
    "Create, start at the root, compare, move, repeat, attach.") + MATCH([
    ["Root", "The top node of the tree"], ["Leaf", "A node whose two pointers are both empty"], ["Left pointer", "The attribute that refers to the left child Node, or None"], ["In-order traversal", "Left subtree, then the node, then the right subtree"], ["Binary search tree", "Smaller values to the left, larger or equal to the right"], ["Null / None", "A pointer that does not refer to any node"]]) + CALC([
    {"q": "Values 50, 30, 70, 20, 40, 60 are inserted in that order. What is the left child of 70?", "a": 60, "unit": "", "tol": 0.01, "hint": "60 >= 50 goes right; 60 < 70 goes left.", "sol": "<b>60</b>."},
    {"q": "Same tree: how many leaf nodes are there?", "a": 3, "unit": "", "tol": 0.01, "hint": "Nodes with no children: 20, 40, 60.", "sol": "<b>3</b>."},
    {"q": "Same tree: how many nodes are compared when searching for 60, counting 60 itself?", "a": 3, "unit": "", "tol": 0.01, "hint": "The path is 50, 70, 60.", "sol": "<b>3</b>."},
    {"q": "Same tree: what is the third value printed by InOrder()?", "a": 40, "unit": "", "tol": 0.01, "hint": "Sorted order is 20, 30, 40, 50, 60, 70.", "sol": "<b>40</b>."},
    {"q": "Same tree: how many levels does it have, counting the root as level 1?", "a": 3, "unit": "", "tol": 0.01, "hint": "50; then 30 and 70; then 20, 40 and 60.", "sol": "<b>3</b>."},
    {"q": "A CountTree is created and the values 8, 3, 10 are inserted. What does GetCount() return?", "a": 3, "unit": "", "tol": 0.01, "hint": "One count per Insert call.", "sol": "<b>3</b>."}]) + MCQ([
    ("Why does Node have SetLeft and SetRight?", ["Python requires setters", "The pointers are private, so the Tree needs a way to attach children", "To print the node", "To delete the tree"], 1, "Private pointers are changed only through methods."),
    ("A new Node's LeftPointer and RightPointer are set to...", ["The root", "None (NULL)", "0", "The data"], 1, "A new node has no children yet."),
    ("Which relationship is Tree to Node?", ["Tree is a Node", "Tree has a Node (containment)", "Node inherits from Tree", "No relationship"], 1, "The Tree's attribute is a Node object."),
    ("Why does CountTree call super().__init__() first?", ["To print a message", "So the inherited Root attribute is created", "To delete the parent", "To count nodes"], 1, "The parent constructor sets the inherited attributes."),
    ("What does in-order traversal of a binary search tree produce?", ["Random order", "Values in sorted order", "Values in reverse insertion order", "Only the leaves"], 1, "Left, node, right gives sorted order."),
    ("Insert is defined in both Tree and CountTree. Calling Insert on either without checking its type is an example of...", ["Containment", "Polymorphism", "Encapsulation only", "Recursion"], 1, "Same call, different behaviour per class.")], "qz1") + CARDS([
    ("Node", "A value plus a left and right pointer. Private data, getters and setters."), ("Tree", "Holds the Root node. Has Insert, Search and InOrder."), ("Root", "The top node; the Tree's only direct link."), ("Leaf", "A node with no children."),
    ("Insert rule", "Smaller goes left; larger or equal goes right."), ("Search", "Follow one path; stop at the value or at an empty pointer."), ("In-order", "Left, node, right: sorted output."), ("Why classes?", "Constructor, private pointers with getters and setters, containment.")])

real = RWNOTE + (
    rw("A sorted contact list", "A phone stores names in a tree so searching does not have to check every contact. Each step of a search throws away about half of the remaining names.", "search follows one path down the tree.") +
    rw("A database index", "A database keeps an index so it can find a record without reading the whole table. Many indexes use tree structures like this one.", "trees keep data in order for fast searching.") +
    rw("A game's decision tree", "A computer opponent asks a yes or no question at each node, then follows the left or right branch to the next question.", "left and right pointers as two choices.") +
    rw("A file system", "Folders contain folders and files, so a folder object holds other objects. A binary tree is the same idea with at most two children.", "containment: objects inside objects."))

review = (
    req("5 marks", "Write", "A binary tree node stores an integer <code>Data</code> and two pointers, <code>LeftPointer</code> and <code>RightPointer</code>, all private. Write the class <code>Node</code> with a constructor that takes the data and sets both pointers to empty.", "Header, three attribute comments, constructor with self, data assigned, both pointers set to None.", pc('''class Node:
    # Data : INTEGER
    # LeftPointer : Node
    # RightPointer : Node
    def __init__(self, NewData):
        self.__Data = NewData
        self.__LeftPointer = None
        self.__RightPointer = None'''), "Making the pointers parameters. A new node has no children, so they start as None.") +
    req("4 marks", "Write", "Add getters for <code>Data</code> and <code>LeftPointer</code> and a setter for <code>LeftPointer</code> to the class.", "Getters return; the setter assigns.", pc('''    def GetData(self):
        return self.__Data

    def GetLeft(self):
        return self.__LeftPointer

    def SetLeft(self, NewLeft):
        self.__LeftPointer = NewLeft'''), "Printing in a getter.") +
    req("2 marks", "Explain", "Explain why the Tree class uses <code>Current.SetLeft(NewNode)</code> rather than changing the left pointer directly.", "Link to encapsulation.", mks(["The pointer is a private attribute of Node, so only Node's methods can change it", "this keeps the data hidden / lets Node control how it is changed"])) +
    req("6 marks", "Write", "Write the method <code>Search(self, Target)</code> in the class <code>Tree</code>. It returns True if the value is in the tree and False if it is not.", "Start at the root, loop while the current node exists, compare, move left or right, return False at the end.", pc('''def Search(self, Target):
    Current = self.__Root
    while Current is not None:
        if Target == Current.GetData():
            return True
        elif Target < Current.GetData():
            Current = Current.GetLeft()
        else:
            Current = Current.GetRight()
    return False'''), "Using <code>Current.__Data</code>, which is private to Node.") +
    req("2 marks", "State", "Which two classes show containment in this program, and what does each contain?", "Name both relationships.", mks(["Tree contains the root Node", "each Node contains (points to) a left and a right Node"])) +
    req("4 marks", "Write", "Write the class <code>CountTree</code> that inherits from <code>Tree</code>, has a private integer <code>Count</code> starting at 0, and overrides <code>Insert</code> to add 1 to Count after inserting.", "Parent in brackets, constructor calls the parent, Insert calls the parent version then adds 1.", pc('''class CountTree(Tree):
    # Count : INTEGER
    def __init__(self):
        super().__init__()
        self.__Count = 0

    def Insert(self, NewData):
        super().Insert(NewData)
        self.__Count = self.__Count + 1'''), "Forgetting super().Insert(NewData), so nothing is ever inserted."))

tipsl = [("Create the node first.", "Make the Node from the value, then find where to attach it."), ("Never touch the pointers directly.", "From Tree, always use GetLeft, GetRight, SetLeft and SetRight."), ("Check for empty first.", "An empty tree has Root = None. Handle it before looping."), ("Smaller left, larger or equal right.", "State the rule you are using in a comment."), ("Pointers start empty.", "A new Node's two pointers are None, not parameters."), ("Child tree: parent first.", "super().__init__() then your own attributes.")]
sents = [("Describe the Node", "Each node stores a value and a left and right pointer, which are private and accessed through getters and setters."), ("Describe the Tree", "The Tree has a root attribute that is a Node, and each Node can contain further Nodes."), ("Describe a search", "Compare the target with the current node, move left if smaller and right if larger, until it is found or the pointer is empty.")]

js7 = r'''
const _scene0 = sceneItem;
sceneItem = (o) => {
  if (o.k === "edge") return SV.line(o.a[0], o.a[1], o.a[2], o.a[3], "ax");
  if (o.k === "node") return SV.circle(o.x, o.y, 22, "cell") + SV.circle(o.x, o.y, 22, o.c, { opacity: 0.6 }) + SV.circle(o.x, o.y, 22, "ax", { fill: "none" }) + SV.text(o.x, o.y + 6, String(o.v), "lbl bd", { "text-anchor": "middle" });
  return _scene0(o);
};
'''

NOTE7 = ("Binary trees are tested in the data structures part of the syllabus (19.1). Writing one as classes combines that with the class skills in 20.1.2 and 20.1.3, which is how Paper 4 sets programming tasks. No single past paper question is quoted on this page; for real questions see the 19.1 binary tree page and the 20.1.3 page.")

finish("ac20r7", "ac-20-1-2-writing-a-binary-tree", "Writing a Binary Tree with Classes",
       "A Node class and a Tree class: constructors, private pointers with getters and setters, containment, a CountTree child class and polymorphism; insert, search and in-order traversal with animations, a tree-building lab and review questions.",
       learn, watch, explore, practise("cl", "o", "m", "c", "q"), real, review, tipsl, sents, js7 + stA + stB + stC + stD + lab, NOTE7, "20.1.2 and 19.1")
