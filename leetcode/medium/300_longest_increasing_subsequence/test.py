import unittest
from solution import Solution


class TestLengthOfLIS(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [10, 9, 2, 5, 3, 7, 101, 18]
        expected = 4
        self.assertEqual(self.solution.lengthOfLIS(nums), expected)

    def test_example_2(self):
        nums = [0, 1, 0, 3, 2, 3]
        expected = 4
        self.assertEqual(self.solution.lengthOfLIS(nums), expected)

    def test_example_3(self):
        nums = [7, 7, 7, 7, 7, 7, 7]
        expected = 1
        self.assertEqual(self.solution.lengthOfLIS(nums), expected)

    def test_strictly_increasing(self):
        nums = [1, 2, 3, 4, 5]
        expected = 5
        self.assertEqual(self.solution.lengthOfLIS(nums), expected)

    def test_strictly_decreasing(self):
        nums = [5, 4, 3, 2, 1]
        expected = 1
        self.assertEqual(self.solution.lengthOfLIS(nums), expected)

    def test_mixed_values(self):
        nums = [3, 5, 6, 2, 5, 4, 19, 5, 6, 7, 12]
        expected = 6  # [3, 5, 6, 19, 6, 12] or similar
        self.assertEqual(self.solution.lengthOfLIS(nums), expected)

    def test_single_element(self):
        nums = [10]
        expected = 1
        self.assertEqual(self.solution.lengthOfLIS(nums), expected)

    def test_empty_list(self):
        nums = []
        expected = 0
        self.assertEqual(self.solution.lengthOfLIS(nums), expected)


if __name__ == "__main__":
    unittest.main()
