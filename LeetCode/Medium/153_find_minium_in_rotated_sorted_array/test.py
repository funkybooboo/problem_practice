import unittest

from solution import Solution


class TestAddFunction(unittest.TestCase):

    def test_1(self):
        result = Solution().findMin([3,4,5,1,2])
        self.assertEqual(result, 1)

    def test_2(self):
        result = Solution().findMin([4,5,6,7,0,1,2])
        self.assertEqual(result, 0)

    def test_3(self):
        result = Solution().findMin([11,13,15,17])
        self.assertEqual(result, 11)

    def test_4(self):
        result = Solution().findMin([3,4,5,6,1,2])
        self.assertEqual(result, 1)

    def test_5(self):
        result = Solution().findMin([4,5,0,1,2,3])
        self.assertEqual(result, 0)

    def test_6(self):
        result = Solution().findMin([4,5,6,7])
        self.assertEqual(result, 4)

    def test_7(self):
        result = Solution().findMin([0,1,2,4,5,6,7])
        self.assertEqual(result, 0)



if __name__ == "__main__":
    unittest.main()
