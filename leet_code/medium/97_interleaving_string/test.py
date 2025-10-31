import unittest

from solution import Solution


class TestIsInterleave(unittest.TestCase):

    def test_1(self):
        result = Solution().isInterleave("aabcc", "dbbca", "aadbbcbcac")
        self.assertEqual(result, True)

    def test_2(self):
        result = Solution().isInterleave("aabcc", "dbbca", "aadbbbaccc")
        self.assertEqual(result, False)

    def test_3(self):
        result = Solution().isInterleave("", "", "")
        self.assertEqual(result, True)

    def test_4(self):
        result = Solution().isInterleave("abc", "", "abc")
        self.assertEqual(result, True)

    def test_5(self):
        result = Solution().isInterleave("", "xyz", "xyz")
        self.assertEqual(result, True)

    def test_6(self):
        result = Solution().isInterleave("aabc", "abad", "aabadabc")
        self.assertEqual(result, True)

    def test_7(self):
        result = Solution().isInterleave("aabc", "abad", "abaadabc")
        self.assertEqual(result, True)


if __name__ == "__main__":
    unittest.main()
