import unittest
from solution import Solution

class TestMinCostClimbingStairs(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        cost = [10, 15, 20]
        expected = 15
        self.assertEqual(self.solution.minCostClimbingStairs(cost), expected)

    def test_example_2(self):
        cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
        expected = 6
        self.assertEqual(self.solution.minCostClimbingStairs(cost), expected)

    def test_min_length(self):
        cost = [0, 0]
        expected = 0
        self.assertEqual(self.solution.minCostClimbingStairs(cost), expected)

    def test_all_same_cost(self):
        cost = [5, 5, 5, 5]
        expected = 10  # path: 0 → 2 → 4 (top)
        self.assertEqual(self.solution.minCostClimbingStairs(cost), expected)

    def test_alternating_costs(self):
        cost = [1, 100, 1, 100, 1]
        expected = 3  # path: 0 → 2 → 4 (top)
        self.assertEqual(self.solution.minCostClimbingStairs(cost), expected)

    def test_long_list(self):
        cost = [1] * 1000
        expected = 500  # Best path is to always jump 2 steps
        self.assertEqual(self.solution.minCostClimbingStairs(cost), expected)

if __name__ == "__main__":
    unittest.main()
