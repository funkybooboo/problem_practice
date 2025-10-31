import unittest
from solution import Solution


class TestMaxProductSubarray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [2, 3, -2, 4]
        expected = 6  # Subarray [2, 3]
        self.assertEqual(self.solution.maxProduct(nums), expected)

    def test_example_2(self):
        nums = [-2, 0, -1]
        expected = 0  # Subarray [0]
        self.assertEqual(self.solution.maxProduct(nums), expected)

    def test_all_positive(self):
        nums = [1, 2, 3, 4]
        expected = 24  # Entire array
        self.assertEqual(self.solution.maxProduct(nums), expected)

    def test_all_negative_even_count(self):
        nums = [-1, -2, -3, -4]
        expected = 24  # Entire array
        self.assertEqual(self.solution.maxProduct(nums), expected)

    def test_all_negative_odd_count(self):
        nums = [-1, -2, -3]
        expected = 6  # Subarray [-1, -2, -3]
        self.assertEqual(self.solution.maxProduct(nums), expected)

    def test_with_zeros(self):
        nums = [-2, 0, -1, 0, -3, 4]
        expected = 4  # Subarray [4]
        self.assertEqual(self.solution.maxProduct(nums), expected)

    def test_single_element(self):
        nums = [-5]
        expected = -5
        self.assertEqual(self.solution.maxProduct(nums), expected)

    def test_mixed_with_zero(self):
        nums = [0, 2, -1, 4, -3, 2]
        expected = 48  # Subarray [2, -1, 4, -3, 2]
        self.assertEqual(self.solution.maxProduct(nums), expected)


if __name__ == "__main__":
    unittest.main()
