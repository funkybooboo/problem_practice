import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [1, 1, 0, 1, 1, 1]
        self.assertEqual(self.solution.findMaxConsecutiveOnes(nums), 3)

    def test_example_2(self):
        nums = [1, 0, 1, 1, 0, 1]
        self.assertEqual(self.solution.findMaxConsecutiveOnes(nums), 2)

    def test_single_one(self):
        nums = [1]
        self.assertEqual(self.solution.findMaxConsecutiveOnes(nums), 1)

    def test_single_zero(self):
        nums = [0]
        self.assertEqual(self.solution.findMaxConsecutiveOnes(nums), 0)

    def test_all_ones(self):
        nums = [1, 1, 1, 1, 1]
        self.assertEqual(self.solution.findMaxConsecutiveOnes(nums), 5)

    def test_all_zeros(self):
        nums = [0, 0, 0, 0]
        self.assertEqual(self.solution.findMaxConsecutiveOnes(nums), 0)

    def test_ones_at_start(self):
        nums = [1, 1, 1, 0, 0]
        self.assertEqual(self.solution.findMaxConsecutiveOnes(nums), 3)

    def test_ones_at_end(self):
        nums = [0, 0, 1, 1, 1]
        self.assertEqual(self.solution.findMaxConsecutiveOnes(nums), 3)

    def test_alternating(self):
        nums = [1, 0, 1, 0, 1, 0, 1]
        self.assertEqual(self.solution.findMaxConsecutiveOnes(nums), 1)

    def test_multiple_runs(self):
        nums = [0, 1, 1, 0, 1, 1, 1, 0, 1]
        self.assertEqual(self.solution.findMaxConsecutiveOnes(nums), 3)

    def test_large_input(self):
        nums = [1] * 100000
        self.assertEqual(self.solution.findMaxConsecutiveOnes(nums), 100000)

if __name__ == "__main__":
    unittest.main()
