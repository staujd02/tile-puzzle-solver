import unittest

from tile import Tile
from mover import Mover
from metrics import Metrics

class Metric_Tests(unittest.TestCase):

    def setUp(self):
        self.metrics = Metrics()
        self.tile = Tile.tile()
    
    def test_evaluations_exist(self):
        self.assertNotEqual(Metrics, None) 

    # When the tile is one step away
    def test_displaced_tiles_yields_one(self):
        tile = Mover.move_left(Tile.duplicate(self.tile))
        self.assertEqual(self.metrics.displaced(tile), 1)
    
    # When the tile is two steps away
    def test_displaced_tiles_yields_two(self):
        tile = Mover.move_left(Tile.duplicate(self.tile))
        tile = Mover.move_up(tile)
        self.assertEqual(self.metrics.displaced(tile), 2)
    
    # When no corners are solved
    def test_corner_yields_one(self):
        tile = [
            [2, 5, 6],
            [1, 7, 8],
            [3, 4, 0]
        ] 
        self.assertEqual(self.metrics.subset(tile), 1)
    
    # When upper left corner is solved
    def test_corner_yields_zero(self):
        tile = [
            [1, 2, 3],
            [8, 5, 6],
            [7, 4, 0]
        ] 
        self.assertEqual(self.metrics.subset(tile), 0)
    
    # When bottom right corner is solved
    def test_corner_yields_zero_again(self):
        tile = [
            [2, 0, 3],
            [8, 1, 4],
            [7, 6, 5]
        ] 
        self.assertEqual(self.metrics.subset(tile), 0)

    # When one tile is out of place
    def test_manhattan_distance_yields_one(self):
        tile = Mover.move_down(Tile.tile())
        self.assertEqual(self.metrics.manhattan(tile), 1)

    def test_manhattan_distance_yields_zero(self):
        self.assertEqual(self.metrics.manhattan(Tile.tile()), 0)

    # When 14 tiles are out of place 
    def test_manhattan_distance_yields_fourteen(self):
        tile = [
            [2, 4, 0],
            [8, 6, 7],
            [5, 1, 3],
        ]
        self.assertEqual(self.metrics.manhattan(tile), 14)

    # When two tiles are out of place 
    def test_manhattan_distance_yields_two(self):
        tile = [
            [1, 3, 0],
            [8, 2, 4],
            [7, 6, 5],
        ]
        self.assertEqual(self.metrics.manhattan(tile), 2)