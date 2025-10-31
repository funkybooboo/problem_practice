import unittest
from solution import Solution


class TestIsNStraightHand(unittest.TestCase):
    def test_example_1(self):
        # Example 1: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
        self.assertTrue(Solution().isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3))

    def test_example_2(self):
        # Example 2: hand = [1,2,3,4,5], groupSize = 4
        self.assertFalse(Solution().isNStraightHand([1, 2, 3, 4, 5], 4))

    def test_single_element(self):
        # Single element array, always can form a group of size 1
        self.assertTrue(Solution().isNStraightHand([10], 1))

    def test_unreachable_group(self):
        # Array where it's impossible to form groups of the given size
        self.assertFalse(Solution().isNStraightHand([1, 2, 3, 4, 5, 6, 7, 8, 9], 4))

    def test_all_reachable(self):
        # Array where all elements can form groups of the given size
        self.assertTrue(Solution().isNStraightHand([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))

    def test_zero_group_size(self):
        # Group size of 1, always possible
        self.assertTrue(Solution().isNStraightHand([1, 2, 3, 4, 5], 1))

    def test_mixed_groups(self):
        # Array that can form mixed groups of the given size
        self.assertTrue(
            Solution().isNStraightHand(
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 3
            )
        )


if __name__ == "__main__":
    unittest.main()
