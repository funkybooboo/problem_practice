import unittest

from solution import Solution


class TestAddFunction(unittest.TestCase):

    def test_1(self):
        result = Solution().productExceptSelf([1, 2, 3, 4])
        self.assertEqual(result, [24, 12, 8, 6])

    def test_2(self):
        result = Solution().productExceptSelf([-1, 1, 0, -3, 3])
        self.assertEqual(result, [0, 0, 9, 0, 0])

    def test_3(self):
        result = Solution().productExceptSelf([1, 2, 4, 6])
        self.assertEqual(result, [48, 24, 12, 8])

    def test_4(self):
        result = Solution().productExceptSelf([-1, 0, 1, 2, 3])
        self.assertEqual(result, [0, -6, 0, 0, 0])


if __name__ == "__main__":
    unittest.main()
