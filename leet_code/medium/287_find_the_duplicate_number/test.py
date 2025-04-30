import unittest

from solution import Solution


class TestAddFunction(unittest.TestCase):

    def test_1(self):
        result = Solution().findDuplicate([1,3,4,2,2])
        self.assertEqual(result, 2)

    def test_2(self):
        result = Solution().findDuplicate([3,1,3,4,2])
        self.assertEqual(result, 3)

    def test_3(self):
        result = Solution().findDuplicate([3,3,3,3,3])
        self.assertEqual(result, 3)

if __name__ == "__main__":
    unittest.main()
