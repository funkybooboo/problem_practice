import unittest

from solution import Solution

class TestSolution(unittest.TestCase):

    def test_example_1(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected_output = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        solution = Solution()
        self.assertEqual(solution.spiralOrder(matrix), expected_output)

    def test_example_2(self):
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
        expected_output = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
        solution = Solution()
        self.assertEqual(solution.spiralOrder(matrix), expected_output)

    def test_example_3(self):
        matrix = [[1, 2], [3, 4]]
        expected_output = [1, 2, 4, 3]
        solution = Solution()
        self.assertEqual(solution.spiralOrder(matrix), expected_output)

    def test_example_4(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected_output = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        solution = Solution()
        self.assertEqual(solution.spiralOrder(matrix), expected_output)

    def test_example_5(self):
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
        expected_output = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
        solution = Solution()
        self.assertEqual(solution.spiralOrder(matrix), expected_output)

if __name__ == "__main__":
    unittest.main()
