import unittest
from solution import Solution


class TestSubsets(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def assertSubsetsEqual(self, result, expected):
        """
        Compare two lists of subsets regardless of the order of subsets
        and order within each subset.
        """
        normalized_result = [tuple(sorted(sub)) for sub in result]
        normalized_expected = [tuple(sorted(sub)) for sub in expected]
        self.assertCountEqual(
            normalized_result,
            normalized_expected,
            msg=f"\nResult:   {result}\nExpected: {expected}",
        )

    def test_example1(self):
        # Example 1 from prompt: nums = [1,2,2]
        nums = [1, 2, 2]
        expected = [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]
        result = self.solution.subsetsWithDup(nums)
        self.assertSubsetsEqual(result, expected)

    def test_example2(self):
        # Example 2 from prompt: nums = [0]
        nums = [0]
        expected = [[], [0]]
        result = self.solution.subsetsWithDup(nums)
        self.assertSubsetsEqual(result, expected)

    def test_size_limits(self):
        # Minimal and small arbitrary cases (no duplicates)
        nums = [5]
        expected = [[], [5]]
        result = self.solution.subsetsWithDup(nums)
        self.assertSubsetsEqual(result, expected)

        nums = [-1, 0]
        expected = [[], [-1], [0], [-1, 0]]
        result = self.solution.subsetsWithDup(nums)
        self.assertSubsetsEqual(result, expected)

    def test_all_duplicates(self):
        # All elements the same: nums = [2,2,2]
        nums = [2, 2, 2]
        expected = [[], [2], [2, 2], [2, 2, 2]]
        result = self.solution.subsetsWithDup(nums)
        self.assertSubsetsEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
