import unittest

from solution import Solution


class TestAddFunction(unittest.TestCase):

    def test_1(self):
        result = Solution().minEatingSpeed([3,6,7,11], 8)
        self.assertEqual(result, 4)

    def test_2(self):
        result = Solution().minEatingSpeed([30,11,23,4,20], 5)
        self.assertEqual(result, 30)

    def test_3(self):
        result = Solution().minEatingSpeed([30,11,23,4,20], 6)
        self.assertEqual(result, 23)

    def test_4(self):
        result = Solution().minEatingSpeed([1,4,3,2], 9)
        self.assertEqual(result, 2)

    def test_5(self):
        result = Solution().minEatingSpeed([25,10,23,4], 4)
        self.assertEqual(result, 25)


if __name__ == "__main__":
    unittest.main()
