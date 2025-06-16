import unittest
from solution import Solution

class TestLetterCombinations(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def assertCombinationsEqual(self, result, expected):
        """
        Compare two lists of strings regardless of order.
        """
        self.assertCountEqual(
            result,
            expected,
            msg=f"\nResult:   {result}\nExpected: {expected}"
        )

    def test_example1(self):
        digits = "23"
        expected = [
            "ad", "ae", "af",
            "bd", "be", "bf",
            "cd", "ce", "cf"
        ]
        result = self.solution.letterCombinations(digits)
        self.assertCombinationsEqual(result, expected)

    def test_example2(self):
        digits = ""
        expected = []
        result = self.solution.letterCombinations(digits)
        self.assertCombinationsEqual(result, expected)

    def test_example3(self):
        digits = "2"
        expected = ["a", "b", "c"]
        result = self.solution.letterCombinations(digits)
        self.assertCombinationsEqual(result, expected)

    def test_multiple_digits(self):
        digits = "79"
        # 7 maps to pqrs, 9 maps to wxyz → 4 * 4 = 16 combinations
        expected = [
            "pw", "px", "py", "pz",
            "qw", "qx", "qy", "qz",
            "rw", "rx", "ry", "rz",
            "sw", "sx", "sy", "sz"
        ]
        result = self.solution.letterCombinations(digits)
        self.assertCombinationsEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
