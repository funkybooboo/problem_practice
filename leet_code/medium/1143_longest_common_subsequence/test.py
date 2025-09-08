import unittest

from solution import Solution


class TestLongestCommonSubsequence(unittest.TestCase):

    def test_1(self):
        result = Solution().longestCommonSubsequence("abcde", "ace")
        self.assertEqual(result, 3)

    def test_2(self):
        result = Solution().longestCommonSubsequence("abc", "abc")
        self.assertEqual(result, 3)

    def test_3(self):
        result = Solution().longestCommonSubsequence("abc", "def")
        self.assertEqual(result, 0)

    def test_4(self):
        result = Solution().longestCommonSubsequence("abcde", "aec")
        self.assertEqual(result, 2)

    def test_5(self):
        result = Solution().longestCommonSubsequence("abcde", "bcde")
        self.assertEqual(result, 4)

if __name__ == "__main__":
    unittest.main()