import unittest
from tile import Tile 

class Tile_Tests(unittest.TestCase):
    def test_a_tile_is_a_3_by_3_tile(self):
        self.assertEquals(len(Tile().layout), 3)
        self.assertEquals(len(Tile().layout[1]), 3)
        self.assertEquals(len(Tile().layout[2]), 3)

    def test_a_tile_has_a_history_that_starts_empty(self):
        self.assertEqual(Tile().history, [])

    def test_a_tile_is_composed_of_numbers(self):
        for target_list in Tile().layout:
            for element in target_list:
                self.assertTrue(isinstance(element, int))

    def test_a_tile_by_default_is_the_goal_state(self):
        goalTile = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
        self.assertEqual(Tile().layout, goalTile)