import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        sol = Solution()
        nums = [4, 3, 2, 7, 8, 2, 3, 1]
        expected_output = [2, 3]
        self.assertEqual(sol.findDuplicates(nums), expected_output)

    def test_example_2(self):
        sol = Solution()
        nums = [1, 1, 2]
        expected_output = [1]
        self.assertEqual(sol.findDuplicates(nums), expected_output)

    def test_example_3(self):
        sol = Solution()
        nums = [1]
        expected_output = []
        self.assertEqual(sol.findDuplicates(nums), expected_output)


if __name__ == "__main__":
    unittest.main()
