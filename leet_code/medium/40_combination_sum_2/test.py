import unittest
from solution import Solution

class TestCombinationSum2(unittest.TestCase):
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
            msg=f"\nResult:   {result}\nExpected: {expected}"
        )

    def test_example1(self):
        candidates = [10, 1, 2, 7, 6, 1, 5]
        target = 8
        expected = [
            [1, 1, 6],
            [1, 2, 5],
            [1, 7],
            [2, 6]
        ]
        result = self.solution.combinationSum2(candidates, target)
        self.assertCombinationsEqual(result, expected)

    def test_example2(self):
        candidates = [2, 5, 2, 1, 2]
        target = 5
        expected = [
            [1, 2, 2],
            [5]
        ]
        result = self.solution.combinationSum2(candidates, target)
        self.assertCombinationsEqual(result, expected)

    def test_single_candidate_equal_target(self):
        candidates = [7]
        target = 7
        expected = [[7]]
        result = self.solution.combinationSum2(candidates, target)
        self.assertCombinationsEqual(result, expected)

    def test_single_candidate_not_equal_target(self):
        candidates = [3]
        target = 1
        expected = []
        result = self.solution.combinationSum2(candidates, target)
        self.assertCombinationsEqual(result, expected)

    def test_no_combination(self):
        candidates = [5, 10, 12]
        target = 3
        expected = []
        result = self.solution.combinationSum2(candidates, target)
        self.assertCombinationsEqual(result, expected)

    def test_empty_candidates(self):
        candidates = []
        target = 5
        expected = []
        result = self.solution.combinationSum2(candidates, target)
        self.assertCombinationsEqual(result, expected)

    def test_multiple_combinations(self):
        candidates = [3, 1, 3, 5, 1, 1]
        target = 5
        expected = [
            [1, 1, 3],
            [5]
        ]
        result = self.solution.combinationSum2(candidates, target)
        self.assertCombinationsEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
