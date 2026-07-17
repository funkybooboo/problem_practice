import unittest

from solution import Solution


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        s = "(()"
        expected_output = 2
        solution = Solution()
        self.assertEqual(solution.longestValidParentheses(s), expected_output)

    def test_example_2(self):
        s = ")()())"
        expected_output = 4
        solution = Solution()
        self.assertEqual(solution.longestValidParentheses(s), expected_output)

    def test_example_3(self):
        s = ""
        expected_output = 0
        solution = Solution()
        self.assertEqual(solution.longestValidParentheses(s), expected_output)

    def test_case_4(self):
        s = "(()(()"
        expected_output = 2
        solution = Solution()
        self.assertEqual(solution.longestValidParentheses(s), expected_output)

    def test_case_5(self):
        s = "(()()"
        expected_output = 4
        solution = Solution()
        self.assertEqual(solution.longestValidParentheses(s), expected_output)

    def test_case_6(self):
        s = "()(()"
        expected_output = 2
        solution = Solution()
        self.assertEqual(solution.longestValidParentheses(s), expected_output)

    def test_case_7(self):
        s = "()()"
        expected_output = 4
        solution = Solution()
        self.assertEqual(solution.longestValidParentheses(s), expected_output)

    def test_case_8(self):
        s = "(((()"
        expected_output = 2
        solution = Solution()
        self.assertEqual(solution.longestValidParentheses(s), expected_output)

    def test_case_9(self):
        s = "())"
        expected_output = 2
        solution = Solution()
        self.assertEqual(solution.longestValidParentheses(s), expected_output)

    def test_case_10(self):
        s = "()(()()"
        expected_output = 4
        solution = Solution()
        self.assertEqual(solution.longestValidParentheses(s), expected_output)

    def test_case_11(self):
        s = "((()))"
        expected_output = 6
        solution = Solution()
        self.assertEqual(solution.longestValidParentheses(s), expected_output)


if __name__ == "__main__":
    unittest.main()
