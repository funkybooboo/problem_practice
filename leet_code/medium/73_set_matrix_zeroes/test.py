import unittest

from solution import Solution

class TestSolution(unittest.TestCase):

    def test_example_1(self):
        matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        Solution().setZeroes(matrix)
        expected = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
        self.assertEqual(matrix, expected)

    def test_example_2(self):
        matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
        Solution().setZeroes(matrix)
        expected = [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
        self.assertEqual(matrix, expected)

    def test_example_3(self):
        matrix = [[0, 1], [1, 0]]
        Solution().setZeroes(matrix)
        expected = [[0, 0], [0, 0]]
        self.assertEqual(matrix, expected)

    def test_example_4(self):
        matrix = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
        Solution().setZeroes(matrix)
        expected = [[1, 0, 3], [0, 0, 0], [6, 0, 8]]
        self.assertEqual(matrix, expected)

if __name__ == "__main__":
    unittest.main()
