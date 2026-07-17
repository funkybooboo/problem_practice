import unittest

from solution import Solution


class TestAddFunction(unittest.TestCase):

    def test_1(self):
        result = Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
        self.assertEqual(result, [1, 1, 4, 2, 1, 1, 0, 0])

    def test_2(self):
        result = Solution().dailyTemperatures([30, 40, 50, 60])
        self.assertEqual(result, [1, 1, 1, 0])

    def test_3(self):
        result = Solution().dailyTemperatures([30, 60, 90])
        self.assertEqual(result, [1, 1, 0])


if __name__ == "__main__":
    unittest.main()
