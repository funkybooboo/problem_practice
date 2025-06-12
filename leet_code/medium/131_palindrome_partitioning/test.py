import unittest
from solution import Solution

class TestPalindromePartitioning(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def assertPartitionsEqual(self, result, expected):
        """
        Compare two lists of palindrome partitions regardless of order.
        """
        normalized_result = sorted([tuple(partition) for partition in result])
        normalized_expected = sorted([tuple(partition) for partition in expected])
        self.assertEqual(
            normalized_result,
            normalized_expected,
            msg=f"\nResult:   {result}\nExpected: {expected}"
        )

    def test_example1(self):
        s = "aab"
        expected = [["a", "a", "b"], ["aa", "b"]]
        result = self.solution.partition(s)
        self.assertPartitionsEqual(result, expected)

    def test_example2(self):
        s = "a"
        expected = [["a"]]
        result = self.solution.partition(s)
        self.assertPartitionsEqual(result, expected)

    def test_all_same_characters(self):
        s = "aaa"
        expected = [["a", "a", "a"], ["aa", "a"], ["a", "aa"], ["aaa"]]
        result = self.solution.partition(s)
        self.assertPartitionsEqual(result, expected)

    def test_mixed_case(self):
        s = "racecar"
        expected = [["r", "a", "c", "e", "c", "a", "r"],
                    ["r", "a", "cec", "a", "r"],
                    ["r", "aceca", "r"],
                    ["racecar"]]
        result = self.solution.partition(s)
        self.assertPartitionsEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
