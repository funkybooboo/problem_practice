import unittest
from solution import Solution


class TestWordBreak(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        s = "leetcode"
        wordDict = ["leet", "code"]
        self.assertTrue(self.solution.wordBreak(s, wordDict))

    def test_example_2(self):
        s = "applepenapple"
        wordDict = ["apple", "pen"]
        self.assertTrue(self.solution.wordBreak(s, wordDict))

    def test_example_3(self):
        s = "catsandog"
        wordDict = ["cats", "dog", "sand", "and", "cat"]
        self.assertFalse(self.solution.wordBreak(s, wordDict))

    def test_reuse_words(self):
        s = "appleapple"
        wordDict = ["apple"]
        self.assertTrue(self.solution.wordBreak(s, wordDict))

    def test_single_character(self):
        s = "a"
        wordDict = ["a"]
        self.assertTrue(self.solution.wordBreak(s, wordDict))

    def test_empty_string(self):
        s = ""
        wordDict = ["a", "b"]
        self.assertTrue(self.solution.wordBreak(s, wordDict))  # edge case: empty string

    def test_no_possible_segmentation(self):
        s = "abcd"
        wordDict = ["a", "abc", "b", "cd"]
        self.assertTrue(self.solution.wordBreak(s, wordDict))  # valid: a + b + cd

    def test_long_word_dict(self):
        s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
        wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa"]
        self.assertFalse(self.solution.wordBreak(s, wordDict))


if __name__ == "__main__":
    unittest.main()
