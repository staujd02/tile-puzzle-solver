from tile import Tile
from mover import Mover
from queue import PriorityQueue
from metrics import Metrics

class Solver():

    def gofH(self, tile):
        return self.metrics.manhattan(tile) + self.metrics.subset(tile) + self.metrics.displaced(tile)

    def expand(self, tile):
        for outcome in Mover.possible_moves(tile):
            if(outcome.layout == Tile().layout):
                return outcome.history
            if (self.original.layout != outcome.layout):
                self.queue.insert(outcome, self.gofH(outcome) + len(tile.history))

    def solvable(self, tile):
        mylist = []
        sum = 0
        for row in tile.layout:
            for num in row:
                if num != 0:
                    mylist.append(num)
        for indx, num in enumerate(mylist):
            for rest in mylist[indx+1:8]:
                if num > rest:
                    sum += 1
        return sum % 2 == 1

    def solve(self, tile):
        self.queue = PriorityQueue()
        self.metrics = Metrics()
        if not self.solvable(tile):
            raise "Puzzle is not solvable"
        self.original = tile
        self.queue.insert(self.original, 1)
        while(True):
            next = self.queue.pop()
            if(next.layout == Tile().layout):
                next.history.append(Tile().layout)
                return next.history
            res = self.expand(next)
            if res != None:
                res.append(Tile().layout)
                return res