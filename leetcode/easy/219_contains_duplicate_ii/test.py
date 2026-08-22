import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_one(self):
        # Duplicate at distance exactly 3 (indices 0 and 3)
        self.assertTrue(self.sol.containsNearbyDuplicate([1, 2, 3, 1], 3))

    def test_example_two(self):
        # Duplicate at distance 1 (indices 2 and 3)
        self.assertTrue(self.sol.containsNearbyDuplicate([1, 0, 1, 1], 1))

    def test_example_three(self):
        # Duplicates exist but all are farther than k=2 apart
        self.assertFalse(self.sol.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))

    def test_no_duplicates(self):
        # No duplicates at all
        self.assertFalse(self.sol.containsNearbyDuplicate([1, 2, 3, 4, 5], 3))

    def test_duplicate_exactly_k_apart(self):
        # Duplicate at distance exactly equal to k
        self.assertTrue(self.sol.containsNearbyDuplicate([1, 2, 1], 2))

    def test_duplicate_just_outside_range(self):
        # Duplicate at distance k+1 (should be false)
        self.assertFalse(self.sol.containsNearbyDuplicate([1, 2, 3, 1], 2))

    def test_single_element(self):
        # Single element, no possible duplicate
        self.assertFalse(self.sol.containsNearbyDuplicate([1], 1))

    def test_k_is_zero(self):
        # k=0 means indices must be same, but they must be distinct
        self.assertFalse(self.sol.containsNearbyDuplicate([1, 1], 0))

    def test_large_k(self):
        # k larger than array length
        self.assertTrue(self.sol.containsNearbyDuplicate([1, 2, 3, 1], 10))

    def test_multiple_duplicates_some_in_range(self):
        # First duplicate out of range, second in range
        self.assertFalse(self.sol.containsNearbyDuplicate([1, 2, 3, 1, 2], 2))

    def test_negative_numbers(self):
        # Works with negative numbers
        self.assertTrue(self.sol.containsNearbyDuplicate([-1, -1], 1))

    def test_mixed_positive_negative(self):
        # Same value appearing as positive and negative (different values)
        self.assertFalse(self.sol.containsNearbyDuplicate([1, -1], 1))

    def test_same_value_repeated(self):
        # Same value appears multiple times
        self.assertTrue(self.sol.containsNearbyDuplicate([1, 1, 1, 1], 2))

    def test_consecutive_duplicates(self):
        # Adjacent duplicates (distance 1)
        self.assertTrue(self.sol.containsNearbyDuplicate([1, 1, 2, 2, 3, 3], 1))

    def test_large_numbers(self):
        # Large integer values
        self.assertTrue(self.sol.containsNearbyDuplicate([10**9, 10**9], 1))

    def test_far_apart_duplicates_only(self):
        # Duplicates only at far distances
        self.assertFalse(self.sol.containsNearbyDuplicate([1, 2, 3, 4, 1], 3))


if __name__ == "__main__":
    unittest.main()
