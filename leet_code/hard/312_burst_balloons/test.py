import unittest

from solution import Solution


class TestMaxCoins(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertFalse(self.solution.isMatch("aa", "a"))

    def test_example_2(self):
        self.assertTrue(self.solution.isMatch("aa", "a*"))

    def test_example_3(self):
        self.assertTrue(self.solution.isMatch("ab", ".*"))

    def test_example_4(self):
        self.assertFalse(self.solution.isMatch("aa", ".b"))

    def test_example_5(self):
        self.assertTrue(self.solution.isMatch("nnn", "n*"))

    def test_example_6(self):
        self.assertTrue(self.solution.isMatch("xyz", ".*z"))


if __name__ == "__main__":
    unittest.main()
