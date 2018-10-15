import unittest
from tile import Tile 
from mover import Mover 

class Mover_Tests(unittest.TestCase):

    def test_mover_appends_tile_history(self):
        tile = Tile()
        tile.history = [[
            [1, 2, 3], 
            [8, 0, 4], 
            [7, 6, 5]
        ]]
        tile.layout = [
            [1, 2, 3], 
            [8, 4, 0], 
            [7, 6, 5]
        ]
        expected = [
            [[1, 2, 3], 
            [8, 0, 4], 
            [7, 6, 5]],
            [[1, 2, 3], 
            [8, 4, 0], 
            [7, 6, 5]]
        ]
        self.assertEqual(Mover.move_up(tile).history, expected)
        pass

    # When the empty square is in the rightmost column
    def test_move_right_yields_nothing(self):
        layout = [
            [1, 2, 3], 
            [8, 4, 0], 
            [7, 6, 5]
        ]
        self.assertEqual(Mover.move_right(Tile()).layout, layout)

    # When the empty square is in the middle
    def test_move_right_gives_a_board_with_a_square_in_the_left(self):
        layout = [
            [1, 2, 3], 
            [8, 4, 0], 
            [7, 6, 5]
        ]
        self.assertEqual(Mover.move_right(Tile()).layout, layout)

    def test_move_left_gives_a_board_with_a_square_in_the_leftmost_row(self):
        layout = [
            [1, 2, 3], 
            [0, 8, 4], 
            [7, 6, 5]
        ]
        self.assertEqual(Mover.move_left(Tile()).layout, layout)

    def test_mover_returns_all_the_possible_next_moves(self):
        moveStates = [
            [[1, 0, 3], [8, 2, 4], [7, 6, 5]],
            [[1, 2, 3], [0, 8, 4], [7, 6, 5]],
            [[1, 2, 3], [8, 4, 0], [7, 6, 5]],
            [[1, 2, 3], [8, 6, 4], [7, 0, 5]]
        ]
        results = [] 
        for tile in Mover.possible_moves(Tile()):
            results.append(tile.layout)
        self.assertEqual(results, moveStates)

    # When the open tile is in the middle row   
    def test_move_down_gives_a_board_with_the_open_tile_in_the_bottom(self):
        layout = [
            [1, 2, 3], 
            [8, 6, 4], 
            [7, 0, 5]
        ]
        self.assertEqual(Mover.move_down(Tile()).layout, layout)

    # When the open tile is in the bottom row   
    def test_move_down_yields_nothing(self):
        self.assertEqual(Mover.move_down(Mover.move_down(Tile())), None)

    # When the open tile is in the top row   
    def test_move_down_has_the_empty_row_in_the_middle(self):
        expectedTile = [
            [1, 2, 3], 
            [8, 0, 4], 
            [7, 6, 5]
        ]
        self.assertEqual(Mover.move_down(Mover.move_up(Tile())).layout, expectedTile)

    def test_move_up_gives_a_board_when_the_blank_was_moved_up(self):
        expectedTile = [
            [1, 0, 3], 
            [8, 2, 4], 
            [7, 6, 5]
        ]
        self.assertEqual(Mover.move_up(Tile()).layout, expectedTile)

    # When the open tile is in the bottom row
    def test_move_up_gives_a_board_with_the_blank_in_the_middle(self):
        inital = Tile()
        swap = list(inital.layout[1])
        inital.layout[1] = list(inital.layout[2])
        inital.layout[2] = swap
        expectedTile = [
            [1, 2, 3], 
            [7, 0, 5],
            [8, 6, 4] 
        ]
        self.assertEqual(Mover.move_up(inital).layout, expectedTile)

    # When the empty square is in the top row 
    def test_move_up_yields_nothing(self):
        self.assertEqual(Mover.move_up(Mover.move_up(Tile())), None)
    
    def test_mover_returns_all_the_possible_next_moves_for_edges(self):
        moveStates = [
            [[0, 2, 3], [1, 8, 4], [7, 6, 5]],
            [[1, 2, 3], [8, 0, 4], [7, 6, 5]],
            [[1, 2, 3], [7, 8, 4], [0, 6, 5]]
        ]
        target = Tile()
        target = Mover.move_left(target)
        results = [] 
        for tile in Mover.possible_moves(target):
            results.append(tile.layout)
        self.assertEqual(results, moveStates)
