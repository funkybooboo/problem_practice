import unittest

from solution import Solution


class TestAddFunction(unittest.TestCase):

    def test_1(self):
        result = Solution().largestRectangleArea([2, 1, 5, 6, 2, 3])
        self.assertEqual(result, 10)

    def test_2(self):
        result = Solution().largestRectangleArea([2, 4])
        self.assertEqual(result, 4)


if __name__ == "__main__":
    unittest.main()
