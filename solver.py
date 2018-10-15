from tile import Tile
from mover import Mover
from queue import PriorityQueue
from metrics import Metrics

class Solver():

    # def gofH(self, tile):
    #     return self.metrics.manhattan(tile) + self.metrics.subset(tile) + self.metrics.displaced(tile)

    def solve(self, tile):
        # self.queue = PriorityQueue()
        # self.metrics = Metrics()
        # original = tile
        # self.queue.insert(original, 1)
        # for expansion in Mover.possible_moves(original):
        #     self.queue.insert(expansion, distance + self.gofH(expansion))
        # while(True):
        #     next = self.queue.pop()
        #     if(next == Tile.tile()):
        #         pass
        #     if(next == tile):
        #         pass
        #     pass
        for solutions in Mover.possible_moves(tile):
            if(solutions.layout == Tile().layout):
                return [solutions.layout]
            for nestedSolutions in Mover.possible_moves(solutions):
                if(nestedSolutions.layout == Tile().layout):
                     return [solutions.layout, nestedSolutions.layout]
                if(nestedSolutions.layout == tile.layout):
                    continue
                for NnestedSolutions in Mover.possible_moves(nestedSolutions):
                    if(NnestedSolutions.layout == Tile().layout):
                        return [solutions.layout, nestedSolutions.layout, NnestedSolutions.layout]