import unittest
from solution import Solution


class TestHouseRobber(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [2, 3, 2]
        expected = 3  # Can't rob both 1st and last. Best is house 2.
        self.assertEqual(self.solution.rob(nums), expected)

    def test_example_2(self):
        nums = [1, 2, 3, 1]
        expected = 4  # Rob house 2 and 4 (2 + 1) or 1 and 3 (1 + 3)
        self.assertEqual(self.solution.rob(nums), expected)

    def test_example_3(self):
        nums = [1, 2, 3]
        expected = 3  # Rob house 2 or 3, best is house 3
        self.assertEqual(self.solution.rob(nums), expected)

    def test_single_house(self):
        nums = [10]
        expected = 10
        self.assertEqual(self.solution.rob(nums), expected)

    def test_two_houses(self):
        nums = [2, 3]
        expected = 3
        self.assertEqual(self.solution.rob(nums), expected)

    def test_three_houses(self):
        nums = [2, 1, 1]
        expected = 2  # Can't rob house 1 and 3 together
        self.assertEqual(self.solution.rob(nums), expected)

    def test_all_zero(self):
        nums = [0, 0, 0, 0]
        expected = 0
        self.assertEqual(self.solution.rob(nums), expected)

    def test_alternating_large_small(self):
        nums = [100, 1, 100, 1, 100]
        expected = 200  # Rob 1st and 3rd or 3rd and 5th, can't rob 1st and 5th
        self.assertEqual(self.solution.rob(nums), expected)

    def test_increasing(self):
        nums = [1, 2, 3, 4, 5]
        expected = 8  # Rob 2 + 4 or 1 + 3 + 5 excluding 1st or last
        self.assertEqual(self.solution.rob(nums), expected)

    def test_decreasing(self):
        nums = [9, 8, 7, 6, 5]
        expected = 16  # Rob 1st, 3rd or 2nd, 4th, can't rob both 1st and last
        self.assertEqual(self.solution.rob(nums), expected)

    def test_long_list(self):
        nums = [1, 2] * 50
        expected = 100  # Can't take both first and last (which are 1s), take max of [0:-1] or [1:]
        self.assertEqual(self.solution.rob(nums), expected)


if __name__ == "__main__":
    unittest.main()
