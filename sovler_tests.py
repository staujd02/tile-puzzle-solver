import unittest
from solver import Solver
from tile import Tile

class Solver_Test(unittest.TestCase):

    def setUp(self):
        self.solver = Solver()

    def test_solver_can_take_a_layout_and_solve_it(self):
        layout = [
            [1, 0, 3],
            [8, 2, 4],
            [7, 6, 5],
        ] 
        self.assertEqual(self.solver.run(layout), [layout, Tile().layout])

    def test_solver_rejects_an_invalid_puzzle_setup(self):
        error = False
        tile = Tile()
        tile.layout = [
            [1, 2, 3],
            [8, 0, 4],
            [7, 5, 6],
        ] 
        try:
            self.solver.solve(tile)
        except:
            error = True
        self.assertEqual(error, True)

    def test_that_solver_can_solve_a_simple_puzzle(self):
        tile = Tile()
        tile.layout = [
            [1, 0, 3],
            [8, 2, 4],
            [7, 6, 5],
        ] 
        self.assertEqual(self.solver.solve(tile), [tile.layout, Tile().layout])
    
    def test_that_solver_can_solve_a_two_step_puzzle(self):
        tile = Tile()
        tile.layout = [
            [1, 3, 0],
            [8, 2, 4],
            [7, 6, 5],
        ]
        pattern = [
            tile.layout,
            [[1, 0, 3],
            [8, 2, 4],
            [7, 6, 5],], 
            Tile().layout
        ]
        self.assertEqual(self.solver.solve(tile), pattern)
    
    def test_that_solver_can_solve_a_three_step_puzzle(self):
        tile = Tile()
        tile.layout = [
            [1, 3, 4],
            [8, 2, 0],
            [7, 6, 5],
        ]
        pattern = [
            tile.layout,
            [[1, 3, 0],
            [8, 2, 4],
            [7, 6, 5],], 

            [[1, 0, 3],
            [8, 2, 4],
            [7, 6, 5],], 
            
            Tile().layout
        ]
        self.assertEqual(self.solver.solve(tile), pattern)