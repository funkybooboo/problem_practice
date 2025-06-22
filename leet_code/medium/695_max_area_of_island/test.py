import unittest
from solution import Solution

class TestMaxAreaOfIsland(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        # LeetCode Example 1: returns the largest 4-directionally connected area of 1's → 6
        grid = [
            [0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0],
        ]
        expected = 6
        result = self.solution.maxAreaOfIsland(grid)
        self.assertEqual(result, expected)

    def test_example2(self):
        # LeetCode Example 2: all water, so area = 0
        grid = [[0,0,0,0,0,0,0,0]]
        expected = 0
        result = self.solution.maxAreaOfIsland(grid)
        self.assertEqual(result, expected)

    def test_empty_grid(self):
        # edge case: nothing at all
        grid = []
        expected = 0
        result = self.solution.maxAreaOfIsland(grid)
        self.assertEqual(result, expected)

    def test_no_land(self):
        # all zeroes
        grid = [
            [0,0,0],
            [0,0,0]
        ]
        expected = 0
        result = self.solution.maxAreaOfIsland(grid)
        self.assertEqual(result, expected)

    def test_single_cell_land(self):
        # smallest possible land
        grid = [[1]]
        expected = 1
        result = self.solution.maxAreaOfIsland(grid)
        self.assertEqual(result, expected)

    def test_multiple_islands(self):
        # two islands: size 3 and size 4 → should pick 4
        grid = [
            [1,0,1,1,1],
            [1,0,0,0,0],
            [1,1,1,0,1],
            [0,0,0,0,1]
        ]
        # Island A (top-left 1's) has area 5; Island B (right-side) has area 3 → max = 5
        expected = 5
        result = self.solution.maxAreaOfIsland(grid)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
