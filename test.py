import unittest
from main import *


class Tile_Tests(unittest.TestCase):
    def test_a_tile_is_a_3_by_3_tile(self):
        self.assertEquals(len(tile()), 3)
        self.assertEquals(len(tile()[1]), 3)
        self.assertEquals(len(tile()[2]), 3)

    def test_a_tile_is_composed_of_numbers(self):
        for target_list in tile():
            for element in target_list:
                self.assertTrue(isinstance(element, int))

    def test_a_tile_by_default_is_the_goal_state(self):
        goalTile = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
        self.assertEqual(tile(), goalTile)


class Mover_Tests(unittest.TestCase):
    def test_mover_returns_all_the_possible_next_moves(self):
        moveStates = [
            [[1, 0, 3], [8, 2, 4], [7, 6, 5]],
            [[1, 2, 3], [0, 8, 4], [7, 6, 5]],
            [[1, 2, 3], [8, 4, 0], [7, 6, 5]],
            [[1, 2, 3], [8, 6, 4], [7, 0, 5]]
        ]
        self.assertEqual(mover(tile()), moveStates)

    def test_mover_returns_all_the_possible_next_moves_for_edges(self):
        moveStates = [
            [
                [1, 2, 3],
                [0, 8, 4],
                [7, 6, 5]
            ],
            [
                [0, 2, 3],
                [1, 8, 4],
                [7, 6, 5]
            ],
            [
                [1, 2, 3],
                [8, 0, 4],
                [7, 6, 5]
            ],
            [
                [1, 2, 3],
                [0, 8, 4],
                [7, 6, 5]
            ]
        ]
        self.assertEqual(mover(mover(tile())[2]), moveStates)
