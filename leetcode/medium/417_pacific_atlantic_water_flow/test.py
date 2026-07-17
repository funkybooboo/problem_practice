import unittest
from solution import Solution


class TestPacificAtlantic(unittest.TestCase):
    def setUp(self):
        self.solver = Solution()

    def assertCoordsEqual(self, result, expected):
        # compare as sorted lists of tuples for order‐independence
        result_set = sorted((r, c) for r, c in result)
        expected_set = sorted((r, c) for r, c in expected)
        self.assertEqual(result_set, expected_set)

    def test_example1(self):
        heights = [
            [1, 2, 2, 3, 5],
            [3, 2, 3, 4, 4],
            [2, 4, 5, 3, 1],
            [6, 7, 1, 4, 5],
            [5, 1, 1, 2, 4],
        ]
        expected = [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
        result = self.solver.pacificAtlantic(heights)
        self.assertCoordsEqual(result, expected)

    def test_example2(self):
        heights = [[1]]
        expected = [[0, 0]]
        result = self.solver.pacificAtlantic(heights)
        self.assertCoordsEqual(result, expected)

    def test_all_same_height(self):
        # if all heights equal, every cell reaches both oceans
        m, n = 3, 4
        heights = [[7] * n for _ in range(m)]
        expected = [[r, c] for r in range(m) for c in range(n)]
        result = self.solver.pacificAtlantic(heights)
        self.assertCoordsEqual(result, expected)

    def test_single_row(self):
        # single row: cells can flow left/up (Pacific) and right/down (Atlantic)
        heights = [[1, 2, 3, 4]]
        expected = [[0, c] for c in range(4)]
        result = self.solver.pacificAtlantic(heights)
        self.assertCoordsEqual(result, expected)

    def test_single_column(self):
        heights = [[1], [2], [3], [4]]
        expected = [[r, 0] for r in range(4)]
        result = self.solver.pacificAtlantic(heights)
        self.assertCoordsEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
