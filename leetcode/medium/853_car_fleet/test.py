import unittest

from solution import Solution


class TestAddFunction(unittest.TestCase):

    def test_1(self):
        result = Solution().carFleet(10, [1, 4], [3, 2])
        self.assertEqual(result, 1)

    def test_2(self):
        result = Solution().carFleet(10, [4, 1, 0, 7], [2, 2, 1, 1])
        self.assertEqual(result, 3)

    def test_3(self):
        result = Solution().carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3])
        self.assertEqual(result, 3)

    def test_4(self):
        result = Solution().carFleet(10, [3], [3])
        self.assertEqual(result, 1)

    def test_5(self):
        result = Solution().carFleet(100, [0, 2, 4], [4, 2, 1])
        self.assertEqual(result, 1)


if __name__ == "__main__":
    unittest.main()
