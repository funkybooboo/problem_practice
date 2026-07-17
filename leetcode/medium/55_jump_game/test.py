import unittest
from solution import Solution


class TestCanJump(unittest.TestCase):
    def test_example_1(self):
        # Example 1: nums = [2,3,1,1,4]
        self.assertTrue(Solution().canJump([2, 3, 1, 1, 4]))

    def test_example_2(self):
        # Example 2: nums = [3,2,1,0,4]
        self.assertFalse(Solution().canJump([3, 2, 1, 0, 4]))

    def test_single_element(self):
        # Single element array, always reachable
        self.assertTrue(Solution().canJump([10]))

    def test_unreachable_end(self):
        # Array where the last index is unreachable
        self.assertFalse(Solution().canJump([0, 1, 2, 0, 0, 0, 0]))

    def test_all_reachable(self):
        # Array where all elements are 1, making the last index reachable
        self.assertTrue(Solution().canJump([1, 1, 1, 1, 1]))

    def test_zero_jumps(self):
        # Array with all zeros, only the first element is reachable
        self.assertFalse(Solution().canJump([0, 0, 0, 0, 0]))

    def test_zero_gap(self):
        # Array with all zeros, only the first element is reachable
        self.assertTrue(Solution().canJump([4, 0, 0, 0, 1]))


if __name__ == "__main__":
    unittest.main()
