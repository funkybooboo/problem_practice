import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_one(self):
        target = 7
        nums = [2, 3, 1, 2, 4, 3]
        self.assertEqual(self.sol.minSubArrayLen(target, nums), 2)

    def test_example_two(self):
        target = 4
        nums = [1, 4, 4]
        self.assertEqual(self.sol.minSubArrayLen(target, nums), 1)

    def test_example_three(self):
        target = 11
        nums = [1, 1, 1, 1, 1, 1, 1, 1]
        self.assertEqual(self.sol.minSubArrayLen(target, nums), 0)

    def test_single_element_equals_target(self):
        target = 5
        nums = [5]
        self.assertEqual(self.sol.minSubArrayLen(target, nums), 1)

    def test_single_element_less_than_target(self):
        target = 10
        nums = [5]
        self.assertEqual(self.sol.minSubArrayLen(target, nums), 0)

    def test_entire_array_sum_equals_target(self):
        target = 10
        nums = [1, 2, 3, 4]
        self.assertEqual(self.sol.minSubArrayLen(target, nums), 4)

    def test_subarray_at_beginning(self):
        target = 6
        nums = [6, 1, 2, 3]
        self.assertEqual(self.sol.minSubArrayLen(target, nums), 1)

    def test_subarray_at_end(self):
        target = 6
        nums = [1, 2, 3, 6]
        self.assertEqual(self.sol.minSubArrayLen(target, nums), 1)

    def test_minimum_target(self):
        target = 1
        nums = [1, 2, 3]
        self.assertEqual(self.sol.minSubArrayLen(target, nums), 1)

    def test_all_elements_same(self):
        target = 9
        nums = [3, 3, 3, 3]
        self.assertEqual(self.sol.minSubArrayLen(target, nums), 3)

    def test_large_numbers(self):
        target = 100
        nums = [1, 2, 3, 50, 50]
        self.assertEqual(self.sol.minSubArrayLen(target, nums), 2)

    def test_two_element_subarray(self):
        target = 5
        nums = [1, 2, 2, 3, 1]
        self.assertEqual(self.sol.minSubArrayLen(target, nums), 2)


if __name__ == "__main__":
    unittest.main()
