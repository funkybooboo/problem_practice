import unittest
from solution import Solution

class TestLongestPalindrome(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        s = "babad"
        result = self.solution.longestPalindrome(s)
        self.assertIn(result, ["bab", "aba"])  # both are valid

    def test_example_2(self):
        s = "cbbd"
        result = self.solution.longestPalindrome(s)
        self.assertEqual(result, "bb")

    def test_single_character(self):
        s = "a"
        result = self.solution.longestPalindrome(s)
        self.assertEqual(result, "a")

    def test_all_same_characters(self):
        s = "aaaaa"
        result = self.solution.longestPalindrome(s)
        self.assertEqual(result, "aaaaa")

    def test_no_palindromes_longer_than_one(self):
        s = "abc"
        result = self.solution.longestPalindrome(s)
        self.assertIn(result, ["a", "b", "c"])  # any one-character result is valid

    def test_even_length_palindrome(self):
        s = "abccba"
        result = self.solution.longestPalindrome(s)
        self.assertEqual(result, "abccba")

    def test_odd_length_palindrome(self):
        s = "racecar"
        result = self.solution.longestPalindrome(s)
        self.assertEqual(result, "racecar")

    def test_palindrome_in_middle(self):
        s = "xyzracecarabc"
        result = self.solution.longestPalindrome(s)
        self.assertEqual(result, "racecar")

if __name__ == "__main__":
    unittest.main()
