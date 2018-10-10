import unittest
from tile import Tile 

class Tile_Tests(unittest.TestCase):
    def test_a_tile_is_a_3_by_3_tile(self):
        self.assertEquals(len(Tile.tile()), 3)
        self.assertEquals(len(Tile.tile()[1]), 3)
        self.assertEquals(len(Tile.tile()[2]), 3)

    def test_a_tile_is_composed_of_numbers(self):
        for target_list in Tile.tile():
            for element in target_list:
                self.assertTrue(isinstance(element, int))

    def test_a_tile_by_default_is_the_goal_state(self):
        goalTile = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
        self.assertEqual(Tile.tile(), goalTile)