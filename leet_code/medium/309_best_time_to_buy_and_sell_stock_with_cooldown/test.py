import unittest

from solution import Solution

class TestAddFunction(unittest.TestCase):

    def test_1(self):
        result = Solution().maxProfit([1, 2, 3, 0, 2])
        self.assertEqual(result, 3)

    def test_2(self):
        result = Solution().maxProfit([1])
        self.assertEqual(result, 0)

    def test_3(self):
        result = Solution().maxProfit([7, 1, 5, 3, 6, 4])
        self.assertEqual(result, 5)

    def test_4(self):
        result = Solution().maxProfit([1, 2, 4, 2, 5, 7, 2, 4, 9, 0])
        self.assertEqual(result, 11)

    def test_5(self):
        result = Solution().maxProfit([3, 3, 5, 0, 0, 3, 1, 4])
        self.assertEqual(result, 6)

if __name__ == "__main__":
    unittest.main()
