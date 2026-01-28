import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_true(self):
        self.assertTrue(self.solution.canPlaceFlowers([1, 0, 0, 0, 1], 1))

    def test_example_false(self):
        self.assertFalse(self.solution.canPlaceFlowers([1, 0, 0, 0, 1], 2))

    def test_empty_n_zero(self):
        self.assertTrue(self.solution.canPlaceFlowers([0], 0))

    def test_single_empty_can_place(self):
        self.assertTrue(self.solution.canPlaceFlowers([0], 1))

    def test_single_filled_cannot_place(self):
        self.assertFalse(self.solution.canPlaceFlowers([1], 1))

    def test_all_empty_even_length(self):
        self.assertTrue(self.solution.canPlaceFlowers([0, 0, 0, 0], 2))
        self.assertFalse(self.solution.canPlaceFlowers([0, 0, 0, 0], 3))

    def test_all_empty_odd_length(self):
        self.assertTrue(self.solution.canPlaceFlowers([0, 0, 0], 2))
        self.assertFalse(self.solution.canPlaceFlowers([0, 0, 0], 3))

    def test_no_space_between_existing_flowers(self):
        self.assertFalse(self.solution.canPlaceFlowers([1, 0, 1, 0, 1], 1))

    def test_space_at_start(self):
        self.assertTrue(self.solution.canPlaceFlowers([0, 0, 1], 1))
        self.assertFalse(self.solution.canPlaceFlowers([0, 0, 1], 2))

    def test_space_at_end(self):
        self.assertTrue(self.solution.canPlaceFlowers([1, 0, 0], 1))
        self.assertFalse(self.solution.canPlaceFlowers([1, 0, 0], 2))

    def test_large_n_zero(self):
        self.assertTrue(self.solution.canPlaceFlowers([1, 0, 1, 0, 1], 0))

    def test_alternating_pattern(self):
        self.assertFalse(self.solution.canPlaceFlowers([0, 1, 0, 1, 0, 1, 0], 1))

    def test_long_run_of_zeros_between_ones(self):
        self.assertTrue(self.solution.canPlaceFlowers([1, 0, 0, 0, 0, 0, 1], 2))
        self.assertFalse(self.solution.canPlaceFlowers([1, 0, 0, 0, 0, 0, 1], 3))

    def test_max_length_edge(self):
        flowerbed = [0] * 20000
        self.assertTrue(self.solution.canPlaceFlowers(flowerbed, 10000))
        self.assertFalse(self.solution.canPlaceFlowers(flowerbed, 10001))


if __name__ == "__main__":
    unittest.main()

