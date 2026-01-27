import unittest
from solution import Solution


class TestIsomorphicStrings(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_basic_true(self):
        self.assertTrue(self.sol.isIsomorphic("egg", "add"))

    def test_basic_false(self):
        self.assertFalse(self.sol.isIsomorphic("foo", "bar"))

    def test_example_paper_title(self):
        self.assertTrue(self.sol.isIsomorphic("paper", "title"))

    def test_single_character(self):
        self.assertTrue(self.sol.isIsomorphic("a", "b"))
        self.assertTrue(self.sol.isIsomorphic("a", "a"))

    def test_same_strings(self):
        self.assertTrue(self.sol.isIsomorphic("abc", "abc"))

    def test_repeated_pattern_true(self):
        self.assertTrue(self.sol.isIsomorphic("abab", "cdcd"))

    def test_repeated_pattern_false(self):
        self.assertFalse(self.sol.isIsomorphic("abab", "cddc"))

    def test_many_to_one_mapping_invalid(self):
        self.assertFalse(self.sol.isIsomorphic("ab", "aa"))

    def test_self_mapping_allowed(self):
        self.assertTrue(self.sol.isIsomorphic("aa", "aa"))

    def test_order_preserved(self):
        self.assertTrue(self.sol.isIsomorphic("abc", "bca"))

    def test_ascii_characters(self):
        self.assertTrue(self.sol.isIsomorphic("!@!", "#$#"))
        self.assertFalse(self.sol.isIsomorphic("!@!", "###"))

    def test_long_string_simple(self):
        s = "a" * 50000
        t = "b" * 50000
        self.assertTrue(self.sol.isIsomorphic(s, t))

    def test_long_string_false(self):
        s = "a" * 49999 + "b"
        t = "c" * 50000
        self.assertFalse(self.sol.isIsomorphic(s, t))

    def test_bidirectional_conflict(self):
        self.assertFalse(self.sol.isIsomorphic("abc", "dee"))

    def test_numeric_characters(self):
        self.assertTrue(self.sol.isIsomorphic("121", "343"))
        self.assertFalse(self.sol.isIsomorphic("121", "345"))


if __name__ == "__main__":
    unittest.main()

