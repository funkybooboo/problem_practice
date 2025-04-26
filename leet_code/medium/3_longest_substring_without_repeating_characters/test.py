import unittest

from solution import Solution


class TestAddFunction(unittest.TestCase):

    def test_1(self):
        result = Solution().lengthOfLongestSubstring("abcabcbb")
        self.assertEqual(result, 3)

    def test_2(self):
        result = Solution().lengthOfLongestSubstring("bbbbb")
        self.assertEqual(result, 1)

    def test_3(self):
        result = Solution().lengthOfLongestSubstring("pwwkew")
        self.assertEqual(result, 3)


if __name__ == "__main__":
    unittest.main()
