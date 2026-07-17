import unittest
from solution import Solution


class TestTreasureDistances(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.INF = 2147483647

    def test_example1(self):
        grid = [
            [self.INF, -1, 0, self.INF],
            [self.INF, self.INF, self.INF, -1],
            [self.INF, -1, self.INF, -1],
            [0, -1, self.INF, self.INF],
        ]
        expected = [[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]]
        self.solution.islandsAndTreasure(grid)
        self.assertEqual(grid, expected)

    def test_example2(self):
        grid = [[0, -1], [self.INF, self.INF]]
        expected = [[0, -1], [1, 2]]
        self.solution.islandsAndTreasure(grid)
        self.assertEqual(grid, expected)

    def test_empty_grid(self):
        grid = []
        expected = []
        self.solution.islandsAndTreasure(grid)
        self.assertEqual(grid, expected)

    def test_no_treasure(self):
        grid = [[self.INF, -1, self.INF], [self.INF, self.INF, -1]]
        # no 0’s => all INF should remain INF
        expected = [[self.INF, -1, self.INF], [self.INF, self.INF, -1]]
        self.solution.islandsAndTreasure(grid)
        self.assertEqual(grid, expected)


if __name__ == "__main__":
    unittest.main()
