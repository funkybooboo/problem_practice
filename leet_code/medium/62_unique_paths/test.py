import unittest

from solution import Solution

class TestUniquePaths(unittest.TestCase):

    def test_1(self):
        result = Solution().uniquePaths(3, 7)
        self.assertEqual(result, 28)

    def test_2(self):
        result = Solution().uniquePaths(3, 2)
        self.assertEqual(result, 3)

    def test_3(self):
        result = Solution().uniquePaths(7, 3)
        self.assertEqual(result, 28)

    def test_4(self):
        result = Solution().uniquePaths(2, 3)
        self.assertEqual(result, 3)

    def test_5(self):
        result = Solution().uniquePaths(1, 1)
        self.assertEqual(result, 1)

    def test_6(self):
        result = Solution().uniquePaths(1, 10)
        self.assertEqual(result, 1)

    def test_7(self):
        result = Solution().uniquePaths(10, 1)
        self.assertEqual(result, 1)

    def test_8(self):
        result = Solution().uniquePaths(5, 5)
        self.assertEqual(result, 70)

    def test_9(self):
        result = Solution().uniquePaths(10, 10)
        self.assertEqual(result, 48620)

    def test_10(self):
        result = Solution().uniquePaths(20, 20)
        self.assertEqual(result, 35345263800)

if __name__ == "__main__":
    unittest.main()
