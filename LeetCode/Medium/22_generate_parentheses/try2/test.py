import unittest

from solution import Solution


class TestAddFunction(unittest.TestCase):

    def test_1(self):
        result = Solution().generateParenthesis(3)
        self.assertEqual(result, ["((()))","(()())","(())()","()(())","()()()"])

    def test_2(self):
        result = Solution().generateParenthesis(1)
        self.assertEqual(result, ["()"])


if __name__ == '__main__':
    unittest.main()
