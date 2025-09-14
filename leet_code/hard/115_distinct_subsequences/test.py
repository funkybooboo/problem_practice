import unittest

from solution import Solution

class TestNumDistinct(unittest.TestCase):
    def test_example1(self):
        sol = Solution()
        result = sol.numDistinct("rabbbit", "rabbit")
        expected = 3
        self.assertEqual(result, expected)

    def test_example2(self):
        sol = Solution()
        result = sol.numDistinct("babgbag", "bag")
        expected = 5
        self.assertEqual(result, expected)

    def test_empty_t(self):
        sol = Solution()
        result = sol.numDistinct("abc", "")
        expected = 0  # Only one subsequence: the empty string
        self.assertEqual(result, expected)

    def test_empty_s(self):
        sol = Solution()
        result = sol.numDistinct("", "a")
        expected = 0
        self.assertEqual(result, expected)

    def test_both_empty(self):
        sol = Solution()
        result = sol.numDistinct("", "")
        expected = 0
        self.assertEqual(result, expected)

    def test_no_match(self):
        sol = Solution()
        result = sol.numDistinct("abc", "def")
        expected = 0
        self.assertEqual(result, expected)

    def test_single_char_match(self):
        sol = Solution()
        result = sol.numDistinct("aaa", "a")
        expected = 3
        self.assertEqual(result, expected)

    def test_longer_t_than_s(self):
        sol = Solution()
        result = sol.numDistinct("a", "aa")
        expected = 0
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
