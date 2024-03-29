from tile import Tile

class Metrics(object):

    def displaced(self, tile):
        goal = Tile() 
        total = 0
        for rowIndex, row in enumerate(tile.layout):
            for squareIndex, square in enumerate(row):
                if square != 0 and square != goal.layout[rowIndex][squareIndex]:
                    total += 1
        return total

    def transform(self, tile):
        result = [[],[],[]]
        for i in range(len(tile.layout)):
            for j in range(len(tile.layout[0])):
                result[i].append(tile.layout[j][i])
        t = Tile()
        t.layout = result
        return t

    def listMatches(self, tile, goal):
        matches = [False, False, False]
        for index, row in enumerate(tile.layout):
            if(goal.layout[index] == row):
                matches[index] = True
        return matches

    def subset(self, tile):
        return 0
        # res = 2
        # goal = Tile()
        # rowMatches = self.listMatches(tile, goal)
        # columnMatches = self.listMatches(
        #     self.transform(tile), self.transform(goal)
        # )
        # if(columnMatches[0] and columnMatches[2] and rowMatches[0] and rowMatches[2]):
        #     return 0
        # for one in [0, 2]:
        #     for two in [0, 2]:
        #         if(columnMatches[one] and rowMatches[two]):
        #             return 1
        # return res 

    def goalCorrdinates(self):
        return { 1: [0, 0], 2: [0, 1], 3: [0, 2],
            4: [1, 2], 5: [2, 2], 6: [2, 1],
            7: [2, 0], 8: [1, 0] } 
        
    def distance(self, square, rowIndex, squareIndex, goalDef):
        if(square == 0):
            return 0
        corr = goalDef[square]
        return abs(corr[0] - rowIndex) + abs(corr[1] - squareIndex)

    def manhattan(self, tile):
        goalDef = self.goalCorrdinates()
        sum = 0
        for rowIndex, row in enumerate(tile.layout):
            for squareIndex, square in enumerate(row):
                sum += self.distance(square, rowIndex, squareIndex, goalDef)
        return sum