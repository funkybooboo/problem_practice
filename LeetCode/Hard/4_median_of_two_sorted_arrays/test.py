import unittest

from solution import Solution


class TestAddFunction(unittest.TestCase):

    def test_1(self):
        result = Solution().findMedianSortedArrays([1,3], [2])
        self.assertEqual(result, 2.00000)

    def test_2(self):
        result = Solution().findMedianSortedArrays([1,2], [3,4])
        self.assertEqual(result, 2.5)

if __name__ == "__main__":
    unittest.main()
