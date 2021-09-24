from solver import Solver
from tile import Tile
import random
import timeit
import time

def prettify(layout):
    print("=============")
    print("| " + str(layout[0][0]) + " | " + str(layout[0][1]) + " | " + str(layout[0][2]) + " |")
    print("| " + str(layout[1][0]) + " | " + str(layout[1][1]) + " | " + str(layout[1][2]) + " |")
    print("| " + str(layout[2][0]) + " | " + str(layout[2][1]) + " | " + str(layout[2][2]) + " |")
    print("=============")

def shortPrintPretty(theList):
    prettify(theList[0])
    print("     \\/     ")
    print("   ......   ")
    print("     \\/     ")
    prettify(theList[len(theList) // 2])
    print("     \\/     ")
    print("   ......   ")
    print("     \\/     ")
    prettify(theList[len(theList) - 1])
    print("Steps to solve: " + str(len(theList)))

def printPretty(theList):
    for index, layout in enumerate(theList):
        prettify(layout)
        if index != len(theList) - 1:
            print("     \\/     ")
        else:
            print("")
    print("Steps to solve: " + str(len(theList)))

run = Solver().run
solvable = Solver().solvable

# printPretty(run([
#     [1, 2, 3],
#     [8, 0, 4],
#     [6, 7, 5]
# ]))
# print("")
# printPretty(run([
#     [2, 3, 5],
#     [4, 8, 1],
#     [0, 7, 6]
# ]))

def prepTest():
    new = range(9) 
    random.shuffle(new)
    layout = [
        new[0:3], 
        new[3:6],
        new[6:9]
    ]
    return layout

def runTest(layoutList):
    for layout in layoutList:
        try:
            run(layout)
        except:
            pass

def canBeSolved(layout):
    t = Tile()
    t.layout = layout
    return solvable(t)


print("Steps, Time")

for x in range(1):
    start = 1000
    random.seed(time.time())
    for count in range(start):
        test = prepTest()
        if not canBeSolved(test):
            continue
        trash = lambda : None
        myTest = lambda: run(test)
        steps = len(run(test))
        stopwatch = timeit.timeit(myTest, trash, time.time, 1)
        print(str(steps) + ", " +  str(stopwatch))

# for tests in range(50):
#     new = range(9) 
#     random.shuffle(new)
#     layout = [
#         new[0:3], 
#         new[3:6],
#         new[6:9]
#     ]
#     try:
#         shortPrintPretty(run(layout))
#         print("")
#     except:
#         print("Unsolvable:")
#         prettify(layout)
#         print("")