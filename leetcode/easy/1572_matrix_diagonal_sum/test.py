import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_example1(self):
        mat = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        self.assertEqual(Solution().diagonalSum(mat), 25)

    def test_example2(self):
        mat = [
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1]
        ]
        self.assertEqual(Solution().diagonalSum(mat), 8)

    def test_example3(self):
        mat = [[5]]
        self.assertEqual(Solution().diagonalSum(mat), 5)

    def test_example4(self):
        mat = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        self.assertEqual(Solution().diagonalSum(mat), 25)

    def test_example5(self):
        mat = [
            [2, 1, 3, 4],
            [1, 2, 9, 8],
            [10, 11, 2, 3],
            [2, 2, 2, 2]
        ]
        self.assertEqual(Solution().diagonalSum(mat), 34)

    def test_example6(self):
        mat = [[1]]
        self.assertEqual(Solution().diagonalSum(mat), 1)


if __name__ == "__main__":
    unittest.main()
