import unittest
from try3.solution import Solution


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        solution = Solution()
        nums = [5, 2, 3, 1]
        expected_output = [1, 2, 3, 5]
        self.assertEqual(solution.sortArray(nums), expected_output)

    def test_example_2(self):
        solution = Solution()
        nums = [5, 1, 1, 2, 0, 0]
        expected_output = [0, 0, 1, 1, 2, 5]
        self.assertEqual(solution.sortArray(nums), expected_output)

    def test_example_3(self):
        solution = Solution()
        nums = [10, 9, 1, 1, 1, 2, 3, 1]
        expected_output = [1, 1, 1, 1, 2, 3, 9, 10]
        self.assertEqual(solution.sortArray(nums), expected_output)

    def test_example_4(self):
        solution = Solution()
        nums = [5, 10, 2, 1, 3]
        expected_output = [1, 2, 3, 5, 10]
        self.assertEqual(solution.sortArray(nums), expected_output)


if __name__ == "__main__":
    unittest.main()
