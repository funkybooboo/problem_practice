import unittest
from solution import Solution

class TestLastStoneWeight(unittest.TestCase):

    def test_example_1(self):
        sol = Solution()
        stones = [2, 7, 4, 1, 8, 1]
        self.assertEqual(sol.lastStoneWeight(stones), 1)

    def test_example_2(self):
        sol = Solution()
        stones = [1]
        self.assertEqual(sol.lastStoneWeight(stones), 1)

    def test_all_equal(self):
        sol = Solution()
        stones = [5, 5, 5, 5]
        self.assertEqual(sol.lastStoneWeight(stones), 0)

    def test_two_stones_different(self):
        sol = Solution()
        stones = [9, 3]
        self.assertEqual(sol.lastStoneWeight(stones), 6)

    def test_large_input(self):
        sol = Solution()
        stones = [31] * 30
        self.assertEqual(sol.lastStoneWeight(stones), 31 if 30 % 2 == 1 else 0)

if __name__ == "__main__":
    unittest.main()
