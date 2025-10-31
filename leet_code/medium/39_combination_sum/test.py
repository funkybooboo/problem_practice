import unittest
from solution import Solution


class TestCombinationSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def assertCombinationsEqual(self, result, expected):
        """
        Compare two lists of combinations regardless of the order of combinations
        and the order within each combination.
        """
        normalized_result = [tuple(sorted(comb)) for comb in result]
        normalized_expected = [tuple(sorted(comb)) for comb in expected]
        self.assertCountEqual(
            normalized_result,
            normalized_expected,
            msg=f"\nResult:   {result}\nExpected: {expected}",
        )

    def test_example1(self):
        candidates = [2, 3, 6, 7]
        target = 7
        expected = [[2, 2, 3], [7]]
        result = self.solution.combinationSum(candidates, target)
        self.assertCombinationsEqual(result, expected)

    def test_example2(self):
        candidates = [2, 3, 5]
        target = 8
        expected = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
        result = self.solution.combinationSum(candidates, target)
        self.assertCombinationsEqual(result, expected)

    def test_example3(self):
        candidates = [2]
        target = 1
        expected = []
        result = self.solution.combinationSum(candidates, target)
        self.assertCombinationsEqual(result, expected)

    def test_single_candidate_equal_target(self):
        candidates = [7]
        target = 7
        expected = [[7]]
        result = self.solution.combinationSum(candidates, target)
        self.assertCombinationsEqual(result, expected)

    def test_single_candidate_multiple_usage(self):
        candidates = [3]
        target = 9
        expected = [[3, 3, 3]]
        result = self.solution.combinationSum(candidates, target)
        self.assertCombinationsEqual(result, expected)

    def test_unsorted_candidates(self):
        candidates = [7, 3, 2]
        target = 7
        expected = [[2, 2, 3], [7]]
        result = self.solution.combinationSum(candidates, target)
        self.assertCombinationsEqual(result, expected)

    def test_no_combination(self):
        candidates = [5, 10]
        target = 3
        expected = []
        result = self.solution.combinationSum(candidates, target)
        self.assertCombinationsEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
