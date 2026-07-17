import unittest
from solution import Solution


class TestLadderLength(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
        expected = 5
        result = self.solution.ladderLength(beginWord, endWord, wordList)
        self.assertEqual(expected, result)

    def test_example2(self):
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot", "dot", "dog", "lot", "log"]
        expected = 0
        result = self.solution.ladderLength(beginWord, endWord, wordList)
        self.assertEqual(expected, result)

    def test_direct_connection(self):
        beginWord = "a"
        endWord = "c"
        wordList = ["a", "b", "c"]
        expected = 2
        result = self.solution.ladderLength(beginWord, endWord, wordList)
        self.assertEqual(expected, result)

    def test_no_path(self):
        beginWord = "game"
        endWord = "math"
        wordList = ["gave", "gape", "gate", "mate", "math"]
        expected = 4
        result = self.solution.ladderLength(beginWord, endWord, wordList)
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
