import unittest
from solution import Solution


class TestPermutations(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def assertPermutationsEqual(self, result, expected):
        """
        Compare two lists of permutations regardless of the order in which
        the permutations appear. Each permutation (which is a list) must
        match exactly (order matters inside each permutation), but the
        collection of permutations can be in any order.
        """
        # Convert each permutation (list) into a tuple so that we can use sets
        result_set = {tuple(perm) for perm in result}
        expected_set = {tuple(perm) for perm in expected}

        self.assertEqual(
            result_set, expected_set, msg=f"\nResult:   {result}\nExpected: {expected}"
        )

    def test_example1(self):
        nums = [1, 2, 3]
        expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        result = self.solution.permute(nums)
        self.assertPermutationsEqual(result, expected)

    def test_example2(self):
        nums = [0, 1]
        expected = [[0, 1], [1, 0]]
        result = self.solution.permute(nums)
        self.assertPermutationsEqual(result, expected)

    def test_example3(self):
        nums = [1]
        expected = [[1]]
        result = self.solution.permute(nums)
        self.assertPermutationsEqual(result, expected)

    def test_unsorted_input(self):
        nums = [3, 1, 2]
        # Even if the input is not sorted, the permutations should still cover all orderings
        expected = [[3, 1, 2], [3, 2, 1], [1, 3, 2], [1, 2, 3], [2, 3, 1], [2, 1, 3]]
        result = self.solution.permute(nums)
        self.assertPermutationsEqual(result, expected)

    def test_length_six_max(self):
        nums = [1, 2, 3, 4, 5, 6]
        # For length 6, there are 720 permutations. We won't list them all explicitly,
        # but we can verify the count and a couple of sample entries.
        result = self.solution.permute(nums)
        self.assertEqual(
            len(result), 720, msg=f"Expected 720 permutations, got {len(result)}"
        )

        # Check that a few known permutations are present
        sample_perms = {(1, 2, 3, 4, 5, 6), (6, 5, 4, 3, 2, 1), (1, 3, 2, 5, 4, 6)}
        result_set = {tuple(perm) for perm in result}
        for sample in sample_perms:
            self.assertIn(sample, result_set, msg=f"Missing permutation: {sample}")


if __name__ == "__main__":
    unittest.main()
