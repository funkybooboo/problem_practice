import unittest
from solution import Solution


class TestFindTargetSumWays(unittest.TestCase):
    def test_example_1(self):
        # Example: nums = [1,1,1,1,1], target = 3
        self.assertEqual(Solution().findTargetSumWays([1, 1, 1, 1, 1], 3), 5)

    def test_example_2(self):
        # Example: nums = [1], target = 1
        self.assertEqual(Solution().findTargetSumWays([1], 1), 1)

    def test_all_zeros_nonzero_target(self):
        # nums has all zeros, target not zero
        self.assertEqual(Solution().findTargetSumWays([0, 0, 0, 0], 1), 0)

    def test_all_zeros_zero_target(self):
        # nums has all zeros, target is zero, 2^n possible combinations
        self.assertEqual(Solution().findTargetSumWays([0, 0, 0, 0], 0), 16)

    def test_large_single_element_positive(self):
        self.assertEqual(Solution().findTargetSumWays([1000], 1000), 1)

    def test_large_single_element_negative(self):
        self.assertEqual(Solution().findTargetSumWays([1000], -1000), 1)

    def test_mixed_nums(self):
        self.assertEqual(Solution().findTargetSumWays([2, 1], 1), 1)

    def test_zero_and_one(self):
        self.assertEqual(Solution().findTargetSumWays([0, 0, 1], 1), 4)

    def test_negative_target(self):
        self.assertEqual(Solution().findTargetSumWays([1, 2, 3], -2), 1)

    def test_empty_array(self):
        # By problem's constraints, nums will have at least one element,
        # but for completeness, check behavior for empty list
        self.assertEqual(Solution().findTargetSumWays([], 0), 1)

    def test_cannot_reach_target(self):
        self.assertEqual(Solution().findTargetSumWays([1, 2, 7], 11), 0)

    def test_larger_case(self):
        self.assertEqual(Solution().findTargetSumWays([1, 2, 3, 4, 5], 3), 3)


if __name__ == "__main__":
    unittest.main()
