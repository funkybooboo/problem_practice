import unittest

from solution import Solution


class TestAddFunction(unittest.TestCase):

    def test_1(self):
        result = Solution().maxProfit([7, 1, 5, 3, 6, 4])
        self.assertEqual(result, 5)

    def test_2(self):
        result = Solution().maxProfit([7, 6, 4, 3, 1])
        self.assertEqual(result, 0)

    def test_3(self):
        result = Solution().maxProfit([10, 1, 5, 6, 7, 1])
        self.assertEqual(result, 6)

    def test_4(self):
        result = Solution().maxProfit([10, 8, 7, 5, 2])
        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
