import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertTrue(
            self.sol.isSubsequence("abc", "ahbgdc")
        )

    def test_example2(self):
        self.assertFalse(
            self.sol.isSubsequence("axc", "ahbgdc")
        )

    def test_example3(self):
        self.assertTrue(
            self.sol.isSubsequence("node", "neetcode")
        )

    def test_empty_s(self):
        # Empty string is always a subsequence
        self.assertTrue(
            self.sol.isSubsequence("", "anything")
        )

    def test_empty_t(self):
        # Only empty s can be subsequence of empty t
        self.assertFalse(
            self.sol.isSubsequence("a", "")
        )
        self.assertTrue(
            self.sol.isSubsequence("", "")
        )

    def test_same_strings(self):
        self.assertTrue(
            self.sol.isSubsequence("abc", "abc")
        )

    def test_repeated_characters(self):
        self.assertTrue(
            self.sol.isSubsequence("aaa", "aaaaaa")
        )
        self.assertFalse(
            self.sol.isSubsequence("aaaaaa", "aaa")
        )

    def test_non_subsequence_cases(self):
        self.assertFalse(
            self.sol.isSubsequence("abc", "acb")  # order matters
        )
        self.assertFalse(
            self.sol.isSubsequence("leetcode", "letcod")  # missing chars
        )


if __name__ == "__main__":
    unittest.main()
