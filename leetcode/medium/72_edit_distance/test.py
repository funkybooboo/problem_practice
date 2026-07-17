import unittest
from solution import Solution


class TestMinDistance(unittest.TestCase):
    def test_example_1(self):
        word1 = "horse"
        word2 = "ros"
        result = Solution().minDistance(word1, word2)
        self.assertEqual(result, 3)

    def test_example_2(self):
        word1 = "intention"
        word2 = "execution"
        result = Solution().minDistance(word1, word2)
        self.assertEqual(result, 5)

    def test_empty_word1(self):
        word1 = ""
        word2 = "abc"
        result = Solution().minDistance(word1, word2)
        self.assertEqual(result, 3)

    def test_empty_word2(self):
        word1 = "abc"
        word2 = ""
        result = Solution().minDistance(word1, word2)
        self.assertEqual(result, 3)

    def test_both_empty(self):
        word1 = ""
        word2 = ""
        result = Solution().minDistance(word1, word2)
        self.assertEqual(result, 0)

    def test_same_words(self):
        word1 = "abc"
        word2 = "abc"
        result = Solution().minDistance(word1, word2)
        self.assertEqual(result, 0)

    def test_single_difference(self):
        word1 = "abc"
        word2 = "ab"
        result = Solution().minDistance(word1, word2)
        self.assertEqual(result, 1)

    def test_replace_all(self):
        word1 = "abc"
        word2 = "def"
        result = Solution().minDistance(word1, word2)
        self.assertEqual(result, 3)

    def test_insert_and_replace(self):
        word1 = "abcd"
        word2 = "bcda"
        result = Solution().minDistance(word1, word2)
        self.assertEqual(result, 2)


if __name__ == "__main__":
    unittest.main()
