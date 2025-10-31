import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [1, 1, 2]
        result = self.solution.permuteUnique(nums)
        expected = [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
        self.assertEqual(sorted(result), sorted(expected))

    def test_example_2(self):
        nums = [1, 2, 3]
        result = self.solution.permuteUnique(nums)
        expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        self.assertEqual(sorted(result), sorted(expected))

    def test_example_3(self):
        # This is identical to example 1
        nums = [1, 1, 2]
        result = self.solution.permuteUnique(nums)
        expected = [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
        self.assertEqual(sorted(result), sorted(expected))

    def test_example_4(self):
        nums = [2, 2]
        result = self.solution.permuteUnique(nums)
        expected = [[2, 2]]
        self.assertEqual(sorted(result), sorted(expected))


if __name__ == "__main__":
    unittest.main()
