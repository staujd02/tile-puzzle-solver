import unittest
from solver import Solver
from tile import Tile

class Solver_Test(unittest.TestCase):

    def setUp(self):
        self.solver = Solver()

    def test_that_solver_can_solve_a_simple_puzzle(self):
        tile = Tile()
        tile.layout = [
            [1, 0, 3],
            [8, 2, 4],
            [7, 6, 5],
        ] 
        self.assertEqual(self.solver.solve(tile), [Tile().layout])
    
    def test_that_solver_can_solve_a_two_step_puzzle(self):
        tile = Tile()
        tile.layout = [
            [1, 3, 0],
            [8, 2, 4],
            [7, 6, 5],
        ]
        pattern = [
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
            [[1, 3, 0],
            [8, 2, 4],
            [7, 6, 5],], 

            [[1, 0, 3],
            [8, 2, 4],
            [7, 6, 5],], 
            
            Tile().layout
        ]
        self.assertEqual(self.solver.solve(tile), pattern)