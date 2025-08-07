import unittest
from solution import Solution

class TestCanPartition(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [1, 5, 11, 5]
        expected = True
        self.assertEqual(self.solution.canPartition(nums), expected)

    def test_example_2(self):
        nums = [1, 2, 3, 5]
        expected = False
        self.assertEqual(self.solution.canPartition(nums), expected)

    def test_single_element(self):
        nums = [1]
        expected = False
        self.assertEqual(self.solution.canPartition(nums), expected)

    def test_all_same_elements_even(self):
        nums = [2, 2, 2, 2]
        expected = True
        self.assertEqual(self.solution.canPartition(nums), expected)

    def test_all_same_elements_odd(self):
        nums = [3, 3, 3]
        expected = False
        self.assertEqual(self.solution.canPartition(nums), expected)

    def test_large_input_true(self):
        nums = [1] * 100 + [2] * 50
        expected = True
        self.assertEqual(self.solution.canPartition(nums), expected)

    def test_large_input_false(self):
        nums = [1] * 199 + [99]
        expected = True
        self.assertEqual(self.solution.canPartition(nums), expected)

    def test_zeroes(self):
        nums = [0, 0, 0, 0]
        expected = True
        self.assertEqual(self.solution.canPartition(nums), expected)

if __name__ == "__main__":
    unittest.main()
