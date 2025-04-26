import unittest

from solution import Solution


class TestAddFunction(unittest.TestCase):

    def test_1(self):
        result = Solution().characterReplacement("ABAB", 2)
        self.assertEqual(result, 4)

    def test_2(self):
        result = Solution().characterReplacement("AABABBA", 1)
        self.assertEqual(result, 4)

    def test_3(self):
        result = Solution().characterReplacement("XYYX", 2)
        self.assertEqual(result, 4)

    def test_4(self):
        result = Solution().characterReplacement("AAABABB", 1)
        self.assertEqual(result, 5)


if __name__ == "__main__":
    unittest.main()
