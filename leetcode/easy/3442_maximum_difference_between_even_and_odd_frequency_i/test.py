import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(self.sol.maxDifference("aaaaabbc"), 3)
        self.assertEqual(self.sol.maxDifference("abcabcab"), 1)

    def test_min_length_valid_case(self):
        s = "aab"  # a=2 even, b=1 odd
        self.assertEqual(self.sol.maxDifference(s), -1)

    def test_two_chars_both_valid(self):
        s = "aaab"  # a=3 odd, b=1 odd → invalid by constraints but still compute via rule (no even)
        # skip expectation via helper only when both exist; here force a valid variant
        s = "aaabb"  # a=3 odd, b=2 even
        self.assertEqual(self.sol.maxDifference(s), 1)

    def test_multiple_odds_and_evens(self):
        s = "aaabbbbccdde"  # a=3, e=1 odd; b=4, c=2, d=2 even → 3-2=1
        self.assertEqual(self.sol.maxDifference(s), 1)

    def test_large_gap(self):
        s = "aaaaaaaaabbbbcc"  # a=9 odd, b=4 even, c=2 even → 9-2=7
        self.assertEqual(self.sol.maxDifference(s), 7)

    def test_many_letters(self):
        s = "abcdefghijklmnopqrstuvwxyz" + "aabbccddeeff"  # f = 2 (even)
        self.assertEqual(self.sol.maxDifference(s), 3)

    def test_all_even_except_one(self):
        s = "aabbccddeeffg"  # g=1 odd, others even → 1-2 = -1
        self.assertEqual(self.sol.maxDifference(s), -1)

    def test_all_odd_except_one(self):
        s = "aaabbbcccdd"  # d=2 even; a,b,c=3 odd → 3-2=1
        self.assertEqual(self.sol.maxDifference(s), 1)

    def test_negative_result(self):
        s = "aaabbbbbbbb"  # a=3 odd, b=8 even → 3-8 = -5
        self.assertEqual(self.sol.maxDifference(s), -5)

    def test_max_length_string(self):
        s = "a" * 51 + "b" * 48 + "c"  # len=100; a=51 odd, b=48 even, c=1 odd → 51-48=3
        self.assertEqual(self.sol.maxDifference(s), 3)

    def test_random_like_distribution(self):
        s = "aaabccccddeeeeeffggh"  # compute via helper oracle
        self.assertEqual(self.sol.maxDifference(s), 3)


if __name__ == "__main__":
    unittest.main()

