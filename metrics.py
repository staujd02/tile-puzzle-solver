from tile import Tile

class Metrics(object):

    def displaced(self, tile):
        goal = Tile.tile() 
        total = 0
        for rowIndex, row in enumerate(tile):
            for squareIndex, square in enumerate(row):
                if square != 0 and square != goal[rowIndex][squareIndex]:
                    total += 1
        return total

    def transform(self, tile):
        result = [[],[],[]]
        for i in range(len(tile)):
            for j in range(len(tile[0])):
                result[i].append(tile[j][i])
        return result

    def listMatches(self, tile, goal):
        matches = [False, False, False]
        for index, row in enumerate(tile):
            if(goal[index] == row):
                matches[index] = True
        return matches

    def subset(self, tile):
        goal = Tile.tile()
        rowMatches = self.listMatches(tile, goal)
        columnMatches = self.listMatches(
            self.transform(tile), self.transform(goal)
        )
        for one in [0, 2]:
            for two in [0, 2]:
                if(columnMatches[one] and rowMatches[two]):
                    return 0
        return 1

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
        for rowIndex, row in enumerate(tile):
            for squareIndex, square in enumerate(row):
                sum += self.distance(square, rowIndex, squareIndex, goalDef)
        return sum