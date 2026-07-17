import unittest

from solution import Solution


class TestAddFunction(unittest.TestCase):

    def test_1(self):
        result = Solution().threeSum([-1, 0, 1, 2, -1, -4])
        self.assertEqual(result, [[-1, -1, 2], [-1, 0, 1]])

    def test_2(self):
        result = Solution().threeSum([0, 1, 1])
        self.assertEqual(result, [])

    def test_3(self):
        result = Solution().threeSum([0, 0, 0])
        self.assertEqual(result, [[0, 0, 0]])


if __name__ == "__main__":
    unittest.main()
