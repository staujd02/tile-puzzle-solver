from solver import Solver
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

random.seed(4)

randList = []

for test in range(10):
    new = range(9) 
    random.shuffle(new)
    layout = [
        new[0:3], 
        new[3:6],
        new[6:9]
    ]
    randList.append(layout)

def runTest():
    for layout in randList:
        try:
            run(layout)
        except:
            pass

x = lambda : None
print(timeit.timeit(runTest, x, time.time, 10))

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