import unittest
from solution import Solution

class TestHouseRobber(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [1, 2, 3, 1]
        expected = 4  # Rob house 1 and 3 (1 + 3)
        self.assertEqual(self.solution.rob(nums), expected)

    def test_example_2(self):
        nums = [2, 7, 9, 3, 1]
        expected = 12  # Rob house 1, 3, and 5 (2 + 9 + 1)
        self.assertEqual(self.solution.rob(nums), expected)

    def test_single_house(self):
        nums = [10]
        expected = 10
        self.assertEqual(self.solution.rob(nums), expected)

    def test_two_houses(self):
        nums = [2, 3]
        expected = 3  # Choose the house with more money
        self.assertEqual(self.solution.rob(nums), expected)

    def test_three_houses(self):
        nums = [2, 1, 1]
        expected = 3  # Rob house 1 and 3 (2 + 1)
        self.assertEqual(self.solution.rob(nums), expected)

    def test_all_zero(self):
        nums = [0, 0, 0, 0]
        expected = 0
        self.assertEqual(self.solution.rob(nums), expected)

    def test_alternating_large_small(self):
        nums = [100, 1, 100, 1, 100]
        expected = 300  # Rob houses 1, 3, and 5
        self.assertEqual(self.solution.rob(nums), expected)

    def test_increasing(self):
        nums = [1, 2, 3, 4, 5]
        expected = 9  # Rob house 1, 3, and 5 (1+3+5)
        self.assertEqual(self.solution.rob(nums), expected)

    def test_decreasing(self):
        nums = [9, 8, 7, 6, 5]
        expected = 21  # Rob house 1, 3, and 5 (9+7+5)
        self.assertEqual(self.solution.rob(nums), expected)

    def test_long_list(self):
        nums = [1, 2] * 50  # Alternating pattern
        expected = 100  # Rob every other house with value 2
        self.assertEqual(self.solution.rob(nums), expected)

if __name__ == "__main__":
    unittest.main()
