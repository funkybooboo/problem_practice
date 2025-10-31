import unittest
from solution import Solution


class TestCountPalindromicSubstrings(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_single_characters(self):
        self.assertEqual(self.solution.countSubstrings("abc"), 3)
        # Each letter is a palindrome: "a", "b", "c"

    def test_repeated_characters(self):
        self.assertEqual(self.solution.countSubstrings("aaa"), 6)
        # "a", "a", "a", "aa", "aa", "aaa"

    def test_mixed(self):
        self.assertEqual(self.solution.countSubstrings("aba"), 4)
        # "a", "b", "a", "aba"

    def test_empty_string(self):
        self.assertEqual(self.solution.countSubstrings(""), 0)

    def test_no_duplicates(self):
        self.assertEqual(self.solution.countSubstrings("abcd"), 4)
        # Just single letters

    def test_palindrome_in_middle(self):
        self.assertEqual(self.solution.countSubstrings("abccba"), 9)
        # "a", "b", "c", "c", "b", "a", "cc", "bccb", "abccba"


if __name__ == "__main__":
    unittest.main()
