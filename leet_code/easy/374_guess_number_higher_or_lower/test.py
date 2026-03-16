import unittest
from solution import Solution
import solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1_pick_6_from_10(self):
        """Example 1: n=10, pick=6"""
        solution._pick = 6
        self.assertEqual(self.sol.guessNumber(10), 6)

    def test_example_2_pick_1_from_1(self):
        """Example 2: n=1, pick=1 (single element)"""
        solution._pick = 1
        self.assertEqual(self.sol.guessNumber(1), 1)

    def test_example_3_pick_1_from_2(self):
        """Example 3: n=2, pick=1 (first element)"""
        solution._pick = 1
        self.assertEqual(self.sol.guessNumber(2), 1)

    def test_pick_last_element(self):
        """Pick is the last element in range"""
        solution._pick = 10
        self.assertEqual(self.sol.guessNumber(10), 10)

    def test_pick_first_element(self):
        """Pick is the first element (1)"""
        solution._pick = 1
        self.assertEqual(self.sol.guessNumber(100), 1)

    def test_pick_middle_element(self):
        """Pick is exactly in the middle"""
        solution._pick = 50
        self.assertEqual(self.sol.guessNumber(100), 50)

    def test_small_range_pick_2_from_2(self):
        """Small range: n=2, pick=2"""
        solution._pick = 2
        self.assertEqual(self.sol.guessNumber(2), 2)

    def test_large_range_pick_near_start(self):
        """Large range with pick near start"""
        solution._pick = 5
        self.assertEqual(self.sol.guessNumber(1000), 5)

    def test_large_range_pick_near_end(self):
        """Large range with pick near end"""
        solution._pick = 995
        self.assertEqual(self.sol.guessNumber(1000), 995)

    def test_medium_range_pick_lower_quarter(self):
        """Pick in lower quarter of range"""
        solution._pick = 25
        self.assertEqual(self.sol.guessNumber(100), 25)

    def test_medium_range_pick_upper_quarter(self):
        """Pick in upper quarter of range"""
        solution._pick = 75
        self.assertEqual(self.sol.guessNumber(100), 75)

    def test_very_large_range(self):
        """Test with very large n value (near constraint limit)"""
        solution._pick = 1000000
        self.assertEqual(self.sol.guessNumber(2000000), 1000000)

    def test_consecutive_calls_different_picks(self):
        """Ensure solution works correctly across multiple calls"""
        solution._pick = 7
        self.assertEqual(self.sol.guessNumber(10), 7)

        solution._pick = 3
        self.assertEqual(self.sol.guessNumber(10), 3)

        solution._pick = 10
        self.assertEqual(self.sol.guessNumber(10), 10)


if __name__ == "__main__":
    unittest.main()
