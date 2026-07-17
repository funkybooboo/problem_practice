import unittest
from solution import Solution


class TestNumberOfIslands(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
        expected = 1
        result = self.solution.numIslands(grid)
        self.assertEqual(result, expected)

    def test_example2(self):
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
        expected = 3
        result = self.solution.numIslands(grid)
        self.assertEqual(result, expected)

    def test_empty_grid(self):
        grid = []
        expected = 0
        result = self.solution.numIslands(grid)
        self.assertEqual(result, expected)

    def test_no_land(self):
        grid = [["0", "0", "0"], ["0", "0", "0"]]
        expected = 0
        result = self.solution.numIslands(grid)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
