import unittest

from solution import Solution


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        solution = Solution()
        nums = [1, 1, 1]
        k = 2
        expected_output = 2
        self.assertEqual(solution.subarraySum(nums, k), expected_output)

    def test_example_2(self):
        solution = Solution()
        nums = [1, 2, 3]
        k = 3
        expected_output = 2
        self.assertEqual(solution.subarraySum(nums, k), expected_output)

    def test_example_3(self):
        solution = Solution()
        nums = [2, -1, 1, 2]
        k = 2
        expected_output = 4
        self.assertEqual(solution.subarraySum(nums, k), expected_output)

    def test_example_4(self):
        solution = Solution()
        nums = [4, 4, 4, 4, 4, 4]
        k = 4
        expected_output = 6
        self.assertEqual(solution.subarraySum(nums, k), expected_output)

if __name__ == '__main__':
    unittest.main()
