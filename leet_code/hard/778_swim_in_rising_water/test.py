import unittest
from solution import Solution

class TestSwimInWater(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        grid = [[0, 2], [1, 3]]
        expected = 3
        result = self.solution.swimInWater(grid)
        self.assertEqual(result, expected, msg=f"Expected {expected} but got {result}")

    def test_example2(self):
        grid = [
            [0, 1, 2, 3, 4],
            [24, 23, 22, 21, 5],
            [12, 13, 14, 15, 16],
            [11, 17, 18, 19, 20],
            [10, 9, 8, 7, 6]
        ]
        expected = 16
        result = self.solution.swimInWater(grid)
        self.assertEqual(result, expected, msg=f"Expected {expected} but got {result}")

    def test_single_cell(self):
        grid = [[0]]
        expected = 0
        result = self.solution.swimInWater(grid)
        self.assertEqual(result, expected, msg=f"Expected {expected} but got {result}")

    def test_diagonal_path(self):
        grid = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        expected = 9
        result = self.solution.swimInWater(grid)
        self.assertEqual(result, expected, msg=f"Expected {expected} but got {result}")

    def test_all_same_elevation(self):
        grid = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]
        expected = 1
        result = self.solution.swimInWater(grid)
        self.assertEqual(result, expected, msg=f"Expected {expected} but got {result}")

    def test_increasing_elevation(self):
        grid = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8]
        ]
        expected = 8
        result = self.solution.swimInWater(grid)
        self.assertEqual(result, expected, msg=f"Expected {expected} but got {result}")

    def test_decreasing_elevation(self):
        grid = [
            [8, 7, 6],
            [5, 4, 3],
            [2, 1, 0]
        ]
        expected = 8
        result = self.solution.swimInWater(grid)
        self.assertEqual(result, expected, msg=f"Expected {expected} but got {result}")

    def test_random_elevation(self):
        grid = [
            [5, 3, 2],
            [4, 1, 6],
            [7, 8, 9]
        ]
        expected = 9
        result = self.solution.swimInWater(grid)
        self.assertEqual(result, expected, msg=f"Expected {expected} but got {result}")

if __name__ == "__main__":
    unittest.main()
