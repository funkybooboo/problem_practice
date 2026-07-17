import unittest

from solution import Solution


class TestAddFunction(unittest.TestCase):

    def test_1(self):
        result = Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
        self.assertEqual(6, result)

    def test_2(self):
        result = Solution().trap([4, 2, 0, 3, 2, 5])
        self.assertEqual(9, result)

    def test_3(self):
        result = Solution().trap([0, 2, 0, 3, 1, 0, 1, 3, 2, 1])
        self.assertEqual(9, result)

    def test_4(self):
        result = Solution().trap([0, 1, 0, 0, 0, 0, 0, 0, 1, 0])
        self.assertEqual(6, result)

    def test_5(self):
        result = Solution().trap([0, 0, 0, 0, 0, 0, 0, 0, 1, 0])
        self.assertEqual(0, result)

    def test_6(self):
        result = Solution().trap([0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
        self.assertEqual(0, result)

    def test_7(self):
        result = Solution().trap([1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(0, result)

    def test_8(self):
        result = Solution().trap([0, 1, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(0, result)


if __name__ == "__main__":
    unittest.main()
