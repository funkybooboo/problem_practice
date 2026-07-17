import unittest
from solution import Solution


class TestCoinChange(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        coins = [1, 2, 5]
        amount = 11
        self.assertEqual(self.solution.coinChange(coins, amount), 3)  # 5 + 5 + 1

    def test_example_2(self):
        coins = [2]
        amount = 3
        self.assertEqual(self.solution.coinChange(coins, amount), -1)

    def test_example_3(self):
        coins = [1]
        amount = 0
        self.assertEqual(self.solution.coinChange(coins, amount), 0)

    def test_large_amount(self):
        coins = [1, 2, 5]
        amount = 100
        self.assertEqual(self.solution.coinChange(coins, amount), 20)

    def test_unreachable_amount(self):
        coins = [5, 10]
        amount = 3
        self.assertEqual(self.solution.coinChange(coins, amount), -1)

    def test_single_coin(self):
        coins = [7]
        amount = 14
        self.assertEqual(self.solution.coinChange(coins, amount), 2)


if __name__ == "__main__":
    unittest.main()
