import unittest
from solution import Solution

class TestOrangesRotting(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        grid = [
            [2, 1, 1],
            [1, 1, 0],
            [0, 1, 1]
        ]
        expected = 4
        result = self.solution.orangesRotting(grid)
        self.assertEqual(result, expected)

    def test_example2(self):
        grid = [
            [2, 1, 1],
            [0, 1, 1],
            [1, 0, 1]
        ]
        expected = -1
        result = self.solution.orangesRotting(grid)
        self.assertEqual(result, expected)

    def test_example3(self):
        grid = [
            [0, 2]
        ]
        expected = 0
        result = self.solution.orangesRotting(grid)
        self.assertEqual(result, expected)

    def test_all_rotten(self):
        grid = [
            [2, 2],
            [2, 2]
        ]
        expected = 0
        result = self.solution.orangesRotting(grid)
        self.assertEqual(result, expected)

    def test_all_fresh(self):
        grid = [
            [1, 1],
            [1, 1]
        ]
        expected = -1
        result = self.solution.orangesRotting(grid)
        self.assertEqual(result, expected)

    def test_no_oranges(self):
        grid = [
            [0, 0],
            [0, 0]
        ]
        expected = 0
        result = self.solution.orangesRotting(grid)
        self.assertEqual(result, expected)

    def test_single_fresh_no_rotten(self):
        grid = [
            [1]
        ]
        expected = -1
        result = self.solution.orangesRotting(grid)
        self.assertEqual(result, expected)

    def test_single_rotten_no_fresh(self):
        grid = [
            [2]
        ]
        expected = 0
        result = self.solution.orangesRotting(grid)
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
