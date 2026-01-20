import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def assertUnorderedEqual(self, result, expected):
        self.assertEqual(sorted(result), sorted(expected))

    def test_example_1(self):
        words = ["mass", "as", "hero", "superhero"]
        expected = ["as", "hero"]
        self.assertUnorderedEqual(self.s.stringMatching(words), expected)

    def test_example_2(self):
        words = ["leetcode", "et", "code"]
        expected = ["et", "code"]
        self.assertUnorderedEqual(self.s.stringMatching(words), expected)

    def test_example_3(self):
        words = ["blue", "green", "bu"]
        expected = []
        self.assertUnorderedEqual(self.s.stringMatching(words), expected)

    def test_single_word(self):
        words = ["alone"]
        expected = []
        self.assertUnorderedEqual(self.s.stringMatching(words), expected)

    def test_two_words_no_match(self):
        words = ["abc", "def"]
        expected = []
        self.assertUnorderedEqual(self.s.stringMatching(words), expected)

    def test_two_words_with_match(self):
        words = ["abc", "b"]
        expected = ["b"]
        self.assertUnorderedEqual(self.s.stringMatching(words), expected)

    def test_multiple_substrings_of_one_word(self):
        words = ["aaaa", "a", "aa", "aaa"]
        expected = ["a", "aa", "aaa"]
        self.assertUnorderedEqual(self.s.stringMatching(words), expected)

    def test_chain_substrings(self):
        words = ["abcd", "bcd", "cd", "d"]
        expected = ["bcd", "cd", "d"]
        self.assertUnorderedEqual(self.s.stringMatching(words), expected)

    def test_overlapping_but_not_substring(self):
        words = ["abc", "cab", "bc"]
        expected = ["bc"]
        self.assertUnorderedEqual(self.s.stringMatching(words), expected)

    def test_all_words_same_length_no_match(self):
        words = ["abc", "def", "ghi"]
        expected = []
        self.assertUnorderedEqual(self.s.stringMatching(words), expected)

    def test_longest_word_only_container(self):
        words = ["x" * 30, "x" * 29, "x" * 10]
        expected = ["x" * 29, "x" * 10]
        self.assertUnorderedEqual(self.s.stringMatching(words), expected)

    def test_order_independence(self):
        words = ["superhero", "hero", "mass", "as"]
        expected = ["hero", "as"]
        self.assertUnorderedEqual(self.s.stringMatching(words), expected)

    def test_repeated_pattern_strings(self):
        words = ["abab", "ab", "bab", "b"]
        expected = ["ab", "bab", "b"]
        self.assertUnorderedEqual(self.s.stringMatching(words), expected)

    def test_substring_at_start_and_end(self):
        words = ["testing", "test", "ing", "sting"]
        expected = ["test", "ing", "sting"]
        self.assertUnorderedEqual(self.s.stringMatching(words), expected)


if __name__ == "__main__":
    unittest.main()

