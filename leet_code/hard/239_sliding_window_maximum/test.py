import unittest

from solution import Solution


class TestAddFunction(unittest.TestCase):
    def test_1(self):
        result = Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
        self.assertEqual([3, 3, 5, 5, 6, 7], result)

    def test_2(self):
        result = Solution().maxSlidingWindow([1], 1)
        self.assertEqual([1], result)

    def test_3(self):
        result = Solution().maxSlidingWindow([1, 2, 1, 0, 4, 2, 6], 3)
        self.assertEqual([2, 2, 4, 4, 6], result)

    def test_4(self):
        result = Solution().maxSlidingWindow([1, -1], 1)
        self.assertEqual([1, -1], result)


if __name__ == "__main__":
    unittest.main()
