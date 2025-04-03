import unittest

from solution import Solution


class TestAddFunction(unittest.TestCase):

    def test_1(self):
        result = Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)
        self.assertEqual(result, True)

    def test_2(self):
        result = Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13)
        self.assertEqual(result, False)

    def test_3(self):
        result = Solution().searchMatrix([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 10)
        self.assertEqual(result, True)

    def test_4(self):
        result = Solution().searchMatrix([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 15)
        self.assertEqual(result, False)

    def test_5(self):
        result = Solution().searchMatrix([[1],[3]], 2)
        self.assertEqual(result, False)



if __name__ == "__main__":
    unittest.main()
