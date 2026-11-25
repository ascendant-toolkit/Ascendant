"""Python answers used by pp19.py (real Paper 4 questions). pp19_check.py runs every one."""

C = {}

C["linear_s21"] = '''
def linearSearch(searchValue):
    for x in range(0, 10):
        if arrayData[x] == searchValue:
            return True
    return False
'''

C["find_w22"] = '''
def FindValues():
    DataToFind = 0
    while DataToFind < 1 or DataToFind > 100:
        DataToFind = int(input("Enter a number between 1 and 100 "))
    Total = 0
    for X in range(0, 100):
        if DataArray[X] == DataToFind:
            Total = Total + 1
    return Total
'''

C["find_s26"] = '''
def FindWords():
    WordFind = input("Enter the word you want to find ").lower()
    Counter = 0
    for x in range(15):
        if DataArray[x] == WordFind:
            Counter = Counter + 1
    print("It was found", Counter, "times")
'''

C["bs2d_s22"] = '''
def BinarySearch(SearchArray, Lower, Upper, SearchValue):
    if Upper >= Lower:
        Mid = (Lower + Upper) // 2
        if SearchArray[0][Mid] == SearchValue:
            return Mid
        elif SearchArray[0][Mid] > SearchValue:
            return BinarySearch(SearchArray, Lower, Mid - 1, SearchValue)
        else:
            return BinarySearch(SearchArray, Mid + 1, Upper, SearchValue)
    return -1
'''

C["bs_s24_41"] = '''
def BinarySearch(DataToFind):
    First = 0
    Last = NumberItems - 1
    while First <= Last:
        MidValue = (First + Last) // 2
        if DataToFind == DataStored[MidValue]:
            return MidValue
        if DataToFind < DataStored[MidValue]:
            Last = MidValue - 1
        else:
            First = MidValue + 1
    return -1
'''

C["bs_s24_42"] = '''
def BinarySearch(IntegerArray, First, Last, ToFind):
    if First > Last:
        return -1
    Middle = (First + Last) // 2
    if IntegerArray[Middle] == ToFind:
        return Middle
    elif IntegerArray[Middle] > ToFind:
        return BinarySearch(IntegerArray, First, Middle - 1, ToFind)
    else:
        return BinarySearch(IntegerArray, Middle + 1, Last, ToFind)
'''

C["bs_s25"] = '''
def Search(DataArray, ItemToFind):
    Low = 0
    High = len(DataArray) - 1
    while Low <= High:
        Middle = (Low + High) // 2
        if DataArray[Middle] < ItemToFind:
            Low = Middle + 1
        elif DataArray[Middle] > ItemToFind:
            High = Middle - 1
        else:
            return Middle
    return -1
'''

C["bs_w25"] = '''
def RecursiveBinarySearch(DataArray, Lower, Upper, DataToFind):
    if Upper >= Lower:
        Middle = (Lower + Upper) // 2
        if DataArray[Middle] == DataToFind:
            return Middle
        elif DataArray[Middle] > DataToFind:
            return RecursiveBinarySearch(DataArray, Lower, Middle - 1, DataToFind)
        else:
            return RecursiveBinarySearch(DataArray, Middle + 1, Upper, DataToFind)
    return -1
'''

C["bub_s21"] = '''
def bubbleSort():
    for x in range(0, 10):
        for y in range(0, 9):
            if arrayData[y] < arrayData[y + 1]:
                temp = arrayData[y]
                arrayData[y] = arrayData[y + 1]
                arrayData[y + 1] = temp
'''

C["bub_s22"] = '''
ArrayLength = 10
for X in range(0, ArrayLength):
    for Y in range(0, ArrayLength - 1):
        for Z in range(0, ArrayLength - Y - 1):
            if ArrayData[X][Z] > ArrayData[X][Z + 1]:
                TempValue = ArrayData[X][Z]
                ArrayData[X][Z] = ArrayData[X][Z + 1]
                ArrayData[X][Z + 1] = TempValue
'''

C["bub_w22"] = '''
def BubbleSort():
    for X in range(0, 99):
        for Y in range(0, 99 - X):
            if DataArray[Y] > DataArray[Y + 1]:
                DataArray[Y], DataArray[Y + 1] = DataArray[Y + 1], DataArray[Y]
    print(DataArray)
'''

C["bub_s24"] = '''
def BubbleSort():
    for Pass in range(0, NumberItems - 1):
        for Count in range(0, NumberItems - Pass - 1):
            if DataStored[Count] > DataStored[Count + 1]:
                DataStored[Count], DataStored[Count + 1] = DataStored[Count + 1], DataStored[Count]
'''

C["bub_w24_41"] = '''
def Bubble(DataArray):
    ArrayLength = len(DataArray)
    for x in range(ArrayLength - 1):
        for y in range(0, ArrayLength - x - 1):
            if CompareStrings(DataArray[y], DataArray[y + 1]) == 2:
                DataArray[y], DataArray[y + 1] = DataArray[y + 1], DataArray[y]
    return DataArray
'''

C["bub_w24_42"] = '''
def SortScores(HighScores):
    ArrayLength = len(HighScores)
    for x in range(ArrayLength - 1):
        for y in range(0, ArrayLength - x - 1):
            Level = int(HighScores[y][1])
            NextLevel = int(HighScores[y + 1][1])
            Lower = int(HighScores[y][2]) < int(HighScores[y + 1][2])
            if Level < NextLevel or (Level == NextLevel and Lower):
                HighScores[y], HighScores[y + 1] = HighScores[y + 1], HighScores[y]
    return HighScores
'''

C["bub_w25"] = '''
def BubbleSort(DataArray):
    Swap = True
    while Swap:
        Swap = False
        for y in range(0, len(DataArray) - 1):
            if DataArray[y] > DataArray[y + 1]:
                DataArray[y], DataArray[y + 1] = DataArray[y + 1], DataArray[y]
                Swap = True
    return DataArray
'''

C["bub_s26"] = '''
def SortLength():
    Swap = True
    while Swap:
        Swap = False
        for y in range(14):
            if len(DataArray[y]) > len(DataArray[y + 1]):
                DataArray[y], DataArray[y + 1] = DataArray[y + 1], DataArray[y]
                Swap = True
'''

C["ins_w22"] = '''
def InsertionSort():
    for I in range(1, NumberOfJobs):
        JobNumber = Jobs[I][0]
        Priority = Jobs[I][1]
        Position = I
        while Position > 0 and Jobs[Position - 1][1] > Priority:
            Jobs[Position][0] = Jobs[Position - 1][0]
            Jobs[Position][1] = Jobs[Position - 1][1]
            Position = Position - 1
        Jobs[Position][0] = JobNumber
        Jobs[Position][1] = Priority
'''

C["ins_s24"] = '''
def RecursiveInsertion(IntegerArray, NumberElements):
    if NumberElements <= 1:
        return IntegerArray
    RecursiveInsertion(IntegerArray, NumberElements - 1)
    LastItem = IntegerArray[NumberElements - 1]
    CheckItem = NumberElements - 2
    while CheckItem >= 0 and IntegerArray[CheckItem] >= LastItem:
        IntegerArray[CheckItem + 1] = IntegerArray[CheckItem]
        CheckItem = CheckItem - 1
    IntegerArray[CheckItem + 1] = LastItem
    return IntegerArray

def IterativeInsertion(IntegerArray, NumberElements):
    for Count in range(1, NumberElements):
        LastItem = IntegerArray[Count]
        CheckItem = Count - 1
        while CheckItem >= 0 and IntegerArray[CheckItem] >= LastItem:
            IntegerArray[CheckItem + 1] = IntegerArray[CheckItem]
            CheckItem = CheckItem - 1
        IntegerArray[CheckItem + 1] = LastItem
    return IntegerArray
'''

C["ins_s25"] = '''
def InsertionSort(DataArray):
    for X in range(1, len(DataArray)):
        CurrentValue = DataArray[X]
        Y = X - 1
        while Y >= 0 and CurrentValue < DataArray[Y]:
            DataArray[Y + 1] = DataArray[Y]
            Y = Y - 1
        DataArray[Y + 1] = CurrentValue
    return DataArray
'''

C["ins_s26"] = '''
def InsertionSort(TheData):
    for x in range(1, len(TheData)):
        Temp = TheData[x]
        y = x - 1
        while y >= 0 and Temp < TheData[y]:
            TheData[y + 1] = TheData[y]
            y = y - 1
        TheData[y + 1] = Temp
    return TheData
'''

# ---------------- binary trees stored in a 2D array
C["add_w21"] = '''
def AddNode(ArrayNodes, RootPointer, FreeNode):
    NodeData = int(input("Enter the data "))
    if FreeNode <= 19:
        ArrayNodes[FreeNode][0] = -1
        ArrayNodes[FreeNode][1] = NodeData
        ArrayNodes[FreeNode][2] = -1
        if RootPointer == -1:
            RootPointer = 0
        else:
            Placed = False
            CurrentNode = RootPointer
            while not Placed:
                if NodeData < ArrayNodes[CurrentNode][1]:
                    if ArrayNodes[CurrentNode][0] == -1:
                        ArrayNodes[CurrentNode][0] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][0]
                else:
                    if ArrayNodes[CurrentNode][2] == -1:
                        ArrayNodes[CurrentNode][2] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][2]
        FreeNode = FreeNode + 1
    else:
        print("Tree is full")
    return ArrayNodes, RootPointer, FreeNode
'''

C["in_w21"] = '''
def InOrder(ArrayNodes, Node):
    if ArrayNodes[Node][0] != -1:
        InOrder(ArrayNodes, ArrayNodes[Node][0])
    print(ArrayNodes[Node][1])
    if ArrayNodes[Node][2] != -1:
        InOrder(ArrayNodes, ArrayNodes[Node][2])
'''

C["search_w22"] = '''
def SearchValue(Root, ValueToFind):
    if Root == -1:
        return -1
    if ArrayNodes[Root][1] == ValueToFind:
        return Root
    if ArrayNodes[Root][1] == -1:
        return -1
    if ArrayNodes[Root][1] > ValueToFind:
        return SearchValue(ArrayNodes[Root][0], ValueToFind)
    return SearchValue(ArrayNodes[Root][2], ValueToFind)
'''

C["post_w22"] = '''
def PostOrder(Root):
    if ArrayNodes[Root][0] != -1:
        PostOrder(ArrayNodes[Root][0])
    if ArrayNodes[Root][2] != -1:
        PostOrder(ArrayNodes[Root][2])
    print(ArrayNodes[Root][1])
'''

C["add_s26"] = '''
def AddNode(NodeData):
    global FirstFreeNodePointer, TreeRootPointer
    if FirstFreeNodePointer > 99:
        print("The tree is full")
        return
    BinaryTree[FirstFreeNodePointer] = [-1, NodeData, -1]
    if TreeRootPointer == -1:
        TreeRootPointer = 0
    else:
        Placed = False
        CurrentNode = TreeRootPointer
        while not Placed:
            if NodeData < BinaryTree[CurrentNode][1]:
                Side = 0
            else:
                Side = 2
            if BinaryTree[CurrentNode][Side] == -1:
                BinaryTree[CurrentNode][Side] = FirstFreeNodePointer
                Placed = True
            else:
                CurrentNode = BinaryTree[CurrentNode][Side]
    FirstFreeNodePointer = FirstFreeNodePointer + 1
'''

C["in_s26"] = '''
def InOrder(TheRoot):
    if BinaryTree[TheRoot][0] != -1:
        InOrder(BinaryTree[TheRoot][0])
    print(BinaryTree[TheRoot][1])
    if BinaryTree[TheRoot][2] != -1:
        InOrder(BinaryTree[TheRoot][2])
'''

C["add_w25"] = '''
def AddNode(NodeData):
    global FreeNode, RootPointer
    if FreeNode > 49:
        print("The tree is full")
        return
    TreeArray[FreeNode] = [-1, NodeData, -1]
    if RootPointer == -1:
        RootPointer = 0
    else:
        Placed = False
        CurrentNode = RootPointer
        while not Placed:
            if NodeData < TreeArray[CurrentNode][1]:
                Side = 0
            else:
                Side = 2
            if TreeArray[CurrentNode][Side] == -1:
                TreeArray[CurrentNode][Side] = FreeNode
                Placed = True
            else:
                CurrentNode = TreeArray[CurrentNode][Side]
    FreeNode = FreeNode + 1
'''

# ---------------- binary trees as objects
C["node_s24"] = '''
class Node:
    def __init__(self, PData):
        self.__LeftPointer = -1    # INTEGER
        self.__Data = PData        # INTEGER
        self.__RightPointer = -1   # INTEGER
'''

C["getset_s24"] = '''
    def GetLeft(self):
        return self.__LeftPointer
    def GetRight(self):
        return self.__RightPointer
    def GetData(self):
        return self.__Data

    def SetLeft(self, NewLeft):
        self.__LeftPointer = NewLeft
    def SetRight(self, NewRight):
        self.__RightPointer = NewRight
    def SetData(self, NewData):
        self.__Data = NewData
'''

C["tree_s24"] = '''
class TreeClass:
    def __init__(self):
        self.__Tree = []           # ARRAY[0:19] OF Node
        self.__FirstNode = -1      # INTEGER
        self.__NumberNodes = 0     # INTEGER
        for x in range(20):
            self.__Tree.append(Node(-1))

    def InsertNode(self, NewNode):
        self.__Tree[self.__NumberNodes] = NewNode
        if self.__NumberNodes == 0:
            self.__FirstNode = 0
        else:
            Current = self.__FirstNode
            while Current != -1:
                Previous = Current
                GoLeft = NewNode.GetData() < self.__Tree[Current].GetData()
                if GoLeft:
                    Current = self.__Tree[Current].GetLeft()
                else:
                    Current = self.__Tree[Current].GetRight()
            if GoLeft:
                self.__Tree[Previous].SetLeft(self.__NumberNodes)
            else:
                self.__Tree[Previous].SetRight(self.__NumberNodes)
        self.__NumberNodes = self.__NumberNodes + 1

    def OutputTree(self):
        if self.__NumberNodes == 0:
            print("No nodes")
        else:
            for x in range(self.__NumberNodes):
                print(self.__Tree[x].GetLeft(), self.__Tree[x].GetData(), self.__Tree[x].GetRight())
'''

C["node_s25"] = '''
class Node:
    def __init__(self, pNodeData):
        self.__NodeData = pNodeData   # INTEGER
        self.__LeftNode = None        # Node
        self.__RightNode = None       # Node

    def GetLeft(self):
        return self.__LeftNode
    def GetRight(self):
        return self.__RightNode
    def GetData(self):
        return self.__NodeData

    def SetLeft(self, NewNode):
        self.__LeftNode = NewNode
    def SetRight(self, NewNode):
        self.__RightNode = NewNode
'''

C["tree_s25"] = '''
class Tree:
    def __init__(self, pFirstNode):
        self.__FirstNode = pFirstNode   # Node

    def GetRootNode(self):
        return self.__FirstNode

    def Insert(self, NewNode):
        CurrentNode = self.__FirstNode
        while True:
            if NewNode.GetData() < CurrentNode.GetData():
                if CurrentNode.GetLeft() == None:
                    CurrentNode.SetLeft(NewNode)
                    return
                CurrentNode = CurrentNode.GetLeft()
            else:
                if CurrentNode.GetRight() == None:
                    CurrentNode.SetRight(NewNode)
                    return
                CurrentNode = CurrentNode.GetRight()
'''

C["out_s25"] = '''
def OutputInOrder(RootNode):
    if RootNode.GetLeft() != None:
        OutputInOrder(RootNode.GetLeft())
    print(RootNode.GetData())
    if RootNode.GetRight() != None:
        OutputInOrder(RootNode.GetRight())
'''

# ---------------- OOP: Employee / Manager and the two Character games
C["emp"] = '''
class Employee:
    def __init__(self, PayP, NumberP, TitleP):
        self.__HourlyPay = PayP            # REAL
        self.__EmployeeNumber = NumberP    # STRING
        self.__JobTitle = TitleP           # STRING
        self.__PayYear2022 = []            # ARRAY[0:51] OF REAL
        for x in range(52):
            self.__PayYear2022.append(0.0)
'''

C["emp_methods"] = '''
    def GetEmployeeNumber(self):
        return self.__EmployeeNumber

    def SetPay(self, WeekNumber, Hours):
        self.__PayYear2022[WeekNumber - 1] = Hours * self.__HourlyPay

    def GetTotalPay(self):
        Total = 0
        for x in range(52):
            Total = Total + self.__PayYear2022[x]
        return Total
'''

C["mgr"] = '''
class Manager(Employee):
    def __init__(self, BonusP, PayP, NumberP, TitleP):
        super().__init__(PayP, NumberP, TitleP)
        self.__BonusValue = BonusP   # REAL
'''

C["mgr_pay"] = '''
    def SetPay(self, WeekNumber, Hours):
        Hours = Hours * (1 + self.__BonusValue / 100)
        super().SetPay(WeekNumber, Hours)
'''

C["char41"] = '''
class Character:
    def __init__(self, NameP, XPositionP, YPositionP):
        self.__Name = NameP              # STRING
        self.__XPosition = XPositionP    # INTEGER
        self.__YPosition = YPositionP    # INTEGER
'''

C["char41_methods"] = '''
    def GetXPosition(self):
        return self.__XPosition
    def GetYPosition(self):
        return self.__YPosition

    def SetXPosition(self, Value):
        self.__XPosition = self.__XPosition + Value
        if self.__XPosition > 10000:
            self.__XPosition = 10000
        elif self.__XPosition < 0:
            self.__XPosition = 0

    def SetYPosition(self, Value):
        self.__YPosition = self.__YPosition + Value
        if self.__YPosition > 10000:
            self.__YPosition = 10000
        elif self.__YPosition < 0:
            self.__YPosition = 0

    def Move(self, Direction):
        if Direction == "up":
            self.SetYPosition(10)
        elif Direction == "down":
            self.SetYPosition(-10)
        elif Direction == "left":
            self.SetXPosition(-10)
        else:
            self.SetXPosition(10)
'''

C["bike"] = '''
class BikeCharacter(Character):
    def __init__(self, NameP, XPositionP, YPositionP):
        super().__init__(NameP, XPositionP, YPositionP)
'''

C["bike_move"] = '''
    def Move(self, Direction):
        if Direction == "up":
            self.SetYPosition(20)
        elif Direction == "down":
            self.SetYPosition(-20)
        elif Direction == "left":
            self.SetXPosition(-20)
        else:
            self.SetXPosition(20)
'''

C["char42"] = '''
class Character:
    def __init__(self, NameP, BirthP, IntelligenceP, SpeedP):
        self.__CharacterName = NameP          # STRING
        self.__DateOfBirth = BirthP           # DATE
        self.__Intelligence = IntelligenceP   # REAL
        self.__Speed = SpeedP                 # INTEGER
'''

C["char42_methods"] = '''
    def GetIntelligence(self):
        return self.__Intelligence
    def GetName(self):
        return self.__CharacterName

    def SetIntelligence(self, NewValue):
        self.__Intelligence = NewValue

    def Learn(self):
        self.__Intelligence = self.__Intelligence * 1.1

    def ReturnAge(self):
        return 2023 - self.__DateOfBirth.year
'''

C["magic"] = '''
class MagicCharacter(Character):
    def __init__(self, ElementP, NameP, BirthP, IntelligenceP, SpeedP):
        super().__init__(NameP, BirthP, IntelligenceP, SpeedP)
        self.__Element = ElementP   # STRING
'''

C["magic_learn"] = '''
    def Learn(self):
        if self.__Element == "fire" or self.__Element == "water":
            self.SetIntelligence(self.GetIntelligence() * 1.2)
        elif self.__Element == "earth":
            self.SetIntelligence(self.GetIntelligence() * 1.3)
        else:
            self.SetIntelligence(self.GetIntelligence() * 1.1)
'''
