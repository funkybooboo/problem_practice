import unittest
from solution import Solution


class TestAppendCharacters(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    # ---- Provided Examples ----

    def test_example_1(self):
        s = "coaching"
        t = "coding"
        self.assertEqual(self.solution.appendCharacters(s, t), 4)

    def test_example_2(self):
        s = "abcde"
        t = "a"
        self.assertEqual(self.solution.appendCharacters(s, t), 0)

    def test_example_3(self):
        s = "z"
        t = "abcde"
        self.assertEqual(self.solution.appendCharacters(s, t), 5)

    # ---- Basic Edge Cases ----

    def test_identical_strings(self):
        s = "abc"
        t = "abc"
        self.assertEqual(self.solution.appendCharacters(s, t), 0)

    def test_no_common_characters(self):
        s = "aaa"
        t = "bbb"
        self.assertEqual(self.solution.appendCharacters(s, t), 3)

    def test_t_longer_than_s_with_partial_match(self):
        s = "abc"
        t = "abcd"
        self.assertEqual(self.solution.appendCharacters(s, t), 1)

    def test_s_single_character(self):
        s = "a"
        t = "a"
        self.assertEqual(self.solution.appendCharacters(s, t), 0)

    def test_s_single_character_no_match(self):
        s = "a"
        t = "b"
        self.assertEqual(self.solution.appendCharacters(s, t), 1)

    # ---- Subsequence Behavior ----

    def test_t_is_subsequence_with_gaps(self):
        s = "axbxcxd"
        t = "abcd"
        self.assertEqual(self.solution.appendCharacters(s, t), 0)

    def test_t_matches_prefix_only(self):
        s = "abc"
        t = "abxyz"
        self.assertEqual(self.solution.appendCharacters(s, t), 3)

    def test_t_matches_suffix_only(self):
        s = "xyzabc"
        t = "abc"
        self.assertEqual(self.solution.appendCharacters(s, t), 0)

    # ---- Repeated Characters ----

    def test_repeated_characters_in_s(self):
        s = "aaaaa"
        t = "aaa"
        self.assertEqual(self.solution.appendCharacters(s, t), 0)

    def test_repeated_characters_in_t(self):
        s = "aaa"
        t = "aaaaaa"
        self.assertEqual(self.solution.appendCharacters(s, t), 3)

    # ---- Large Input Sanity Checks ----

    def test_large_no_overlap(self):
        s = "a" * 100000
        t = "b" * 100000
        self.assertEqual(self.solution.appendCharacters(s, t), 100000)

    def test_large_full_match(self):
        s = "a" * 100000
        t = "a" * 100000
        self.assertEqual(self.solution.appendCharacters(s, t), 0)


if __name__ == "__main__":
    unittest.main()

