import unittest

from solution import Solution


class TestAddFunction(unittest.TestCase):

    def test_1(self):
        result = Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
        self.assertEqual(result, 49)

    def test_2(self):
        result = Solution().maxArea([1, 1])
        self.assertEqual(result, 1)


if __name__ == "__main__":
    unittest.main()
