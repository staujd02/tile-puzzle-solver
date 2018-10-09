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

    # When the empty square is in the rightmost column
    def test_move_right_yields_nothing(self):
        expectedTile = [
            [1, 2, 3], 
            [8, 4, 0], 
            [7, 6, 5]
        ]
        self.assertEqual(move_right(tile()), expectedTile)

    # When the empty square is in the middle
    def test_move_right_gives_a_board_with_a_square_in_the_left(self):
        expectedTile = [
            [1, 2, 3], 
            [8, 4, 0], 
            [7, 6, 5]
        ]
        self.assertEqual(move_right(tile()), expectedTile)

    def test_mover_returns_all_the_possible_next_moves(self):
        moveStates = [
            [[1, 0, 3], [8, 2, 4], [7, 6, 5]],
            [[1, 2, 3], [0, 8, 4], [7, 6, 5]],
            [[1, 2, 3], [8, 4, 0], [7, 6, 5]],
            [[1, 2, 3], [8, 6, 4], [7, 0, 5]]
        ]
        self.assertEqual(mover(tile()), moveStates)

    # When the open tile is in the middle row   
    def test_move_down_gives_a_board_with_the_open_tile_in_the_bottom(self):
        expectedTile = [
            [1, 2, 3], 
            [8, 6, 4], 
            [7, 0, 5]
        ]
        self.assertEqual(move_down(tile()), expectedTile)

    # When the open tile is in the bottom row   
    def test_move_down_yields_nothing(self):
        self.assertEqual(move_down(move_down(tile())), None)

    # When the open tile is in the top row   
    def test_move_down_has_the_empty_row_in_the_middle(self):
        expectedTile = [
            [1, 2, 3], 
            [8, 0, 4], 
            [7, 6, 5]
        ]
        self.assertEqual(move_down(move_up(tile())), expectedTile)

    def test_move_up_gives_a_board_when_the_blank_was_moved_up(self):
        expectedTile = [
            [1, 0, 3], 
            [8, 2, 4], 
            [7, 6, 5]
        ]
        self.assertEqual(move_up(tile()), expectedTile)

    # When the open tile is in the bottom row
    def test_move_up_gives_a_board_with_the_blank_in_the_middle(self):
        inital = tile()
        swap = list(inital[1])
        inital[1] = list(inital[2])
        inital[2] = swap
        expectedTile = [
            [1, 2, 3], 
            [7, 0, 5],
            [8, 6, 4] 
        ]
        self.assertEqual(move_up(inital), expectedTile)

    # When the empty square is in the top row 
    def test_move_up_yields_nothing(self):
        self.assertEqual(move_up(move_up(tile())), None)
    
    def test_mover_returns_all_the_possible_next_moves_for_edges(self):
        moveStates = [
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
                [7, 8, 4],
                [0, 6, 5]
            ]
        ]
        self.assertEqual(mover(mover(tile())[2]), moveStates)
