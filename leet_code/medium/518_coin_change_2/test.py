import unittest

from solution import Solution


class TestChangeFunction(unittest.TestCase):

    def test_1(self):
        result = Solution().change(5, [1, 2, 5])
        self.assertEqual(result, 4)

    def test_2(self):
        result = Solution().change(3, [2])
        self.assertEqual(result, 0)

    def test_3(self):
        result = Solution().change(10, [10])
        self.assertEqual(result, 1)

    def test_4(self):
        result = Solution().change(0, [1, 2, 5])
        self.assertEqual(result, 1)

    def test_5(self):
        result = Solution().change(10, [1, 2, 5])
        self.assertEqual(result, 10)

    def test_6(self):
        result = Solution().change(10, [2, 5, 10])
        self.assertEqual(result, 3)

    def test_7(self):
        result = Solution().change(5, [1, 3, 4])
        self.assertEqual(result, 3)

    def test_8(self):
        result = Solution().change(10, [1, 3, 4])
        self.assertEqual(result, 8)

    def test_9(self):
        result = Solution().change(1, [1, 2, 3])
        self.assertEqual(result, 1)

    def test_10(self):
        result = Solution().change(2, [1, 2, 3])
        self.assertEqual(result, 2)


if __name__ == "__main__":
    unittest.main()
