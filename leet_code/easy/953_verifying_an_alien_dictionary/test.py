import unittest

from solution import Solution


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        solution = Solution()
        words = ["hello", "leetcode"]
        order = "hlabcdefgijkmnopqrstuvwxyz"
        self.assertTrue(solution.isAlienSorted(words, order))

    def test_example_2(self):
        solution = Solution()
        words = ["word", "world", "row"]
        order = "worldabcefghijkmnpqstuvxyz"
        self.assertFalse(solution.isAlienSorted(words, order))

    def test_example_3(self):
        solution = Solution()
        words = ["apple", "app"]
        order = "abcdefghijklmnopqrstuvwxyz"
        self.assertFalse(solution.isAlienSorted(words, order))

    def test_example_4(self):
        solution = Solution()
        words = ["dag", "disk", "dog"]
        order = "hlabcdefgijkmnopqrstuvwxyz"
        self.assertTrue(solution.isAlienSorted(words, order))

    def test_example_5(self):
        solution = Solution()
        words = ["neetcode", "neet"]
        order = "worldabcefghijkmnpqstuvxyz"
        self.assertFalse(solution.isAlienSorted(words, order))


if __name__ == "__main__":
    unittest.main()
