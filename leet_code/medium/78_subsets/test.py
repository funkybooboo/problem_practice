import unittest
from solution import Solution


class TestSubsets(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def assertSubsetsEqual(self, result, expected):
        """
        Compare two lists of subsets regardless of order of subsets
        and order within each subset.
        """
        # Normalize each subset by sorting, then compare as multisets of tuples
        normalized_result = [tuple(sorted(sub)) for sub in result]
        normalized_expected = [tuple(sorted(sub)) for sub in expected]
        self.assertCountEqual(
            normalized_result,
            normalized_expected,
            msg=f"\nResult:   {result}\nExpected: {expected}",
        )

    def test_example1(self):
        nums = [1, 2, 3]
        expected = [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
        result = self.solution.subsets(nums)
        self.assertSubsetsEqual(result, expected)

    def test_example2(self):
        nums = [0]
        expected = [[], [0]]
        result = self.solution.subsets(nums)
        self.assertSubsetsEqual(result, expected)

    def test_size_limits(self):
        # Test the minimal and a small arbitrary case
        nums = [5]
        expected = [[], [5]]
        result = self.solution.subsets(nums)
        self.assertSubsetsEqual(result, expected)

        nums = [-1, 0]
        expected = [[], [-1], [0], [-1, 0]]
        result = self.solution.subsets(nums)
        self.assertSubsetsEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
