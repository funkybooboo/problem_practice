import unittest
from solution import Solution


class TestForeignDictionary(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        words = ["z", "o"]
        expected = "zo"
        result = self.solution.foreignDictionary(words)
        self.assertEqual(result, expected, msg=f"Expected {expected} but got {result}")

    def test_example2(self):
        words = ["hrn", "hrf", "er", "enn", "rfnn"]
        expected = "hernf"
        result = self.solution.foreignDictionary(words)
        self.assertIn(
            result,
            ["hernf", "hefnr", "herfn", "hfrne"],
            msg=f"Expected one of ['hernf', 'hefnr', 'herfn', 'hfrne'] but got {result}",
        )

    def test_invalid_order(self):
        words = ["abc", "ab"]
        expected = ""
        result = self.solution.foreignDictionary(words)
        self.assertEqual(result, expected, msg=f"Expected {expected} but got {result}")

    def test_single_word(self):
        words = ["a"]
        expected = "a"
        result = self.solution.foreignDictionary(words)
        self.assertEqual(result, expected, msg=f"Expected {expected} but got {result}")

    def test_multiple_valid_orders(self):
        words = ["wrt", "wrf", "er", "ett", "rftt"]
        expected = "wertf"
        result = self.solution.foreignDictionary(words)
        self.assertIn(
            result,
            ["wertf", "wfret", "wfetr"],
            msg=f"Expected one of ['wertf', 'wfret', 'wfetr'] but got {result}",
        )


if __name__ == "__main__":
    unittest.main()
