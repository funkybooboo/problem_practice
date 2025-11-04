import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example_1(self):
        nums = [0, 1, 0, 3, 12]
        self.s.moveZeroes(nums)
        self.assertEqual(nums, [1, 3, 12, 0, 0])

    def test_example_2(self):
        nums = [0]
        self.s.moveZeroes(nums)
        self.assertEqual(nums, [0])

    def test_example_3(self):
        nums = [0, 0, 1, 2, 0, 5]
        self.s.moveZeroes(nums)
        self.assertEqual(nums, [1, 2, 5, 0, 0, 0])

    def test_example_4(self):
        nums = [0, 1, 0]
        self.s.moveZeroes(nums)
        self.assertEqual(nums, [1, 0, 0])

    def test_no_zeros(self):
        nums = [1, 2, 3, 4]
        self.s.moveZeroes(nums)
        self.assertEqual(nums, [1, 2, 3, 4])

    def test_all_zeros(self):
        nums = [0, 0, 0, 0]
        self.s.moveZeroes(nums)
        self.assertEqual(nums, [0, 0, 0, 0])

    def test_mixed_start_end(self):
        nums = [1, 0, 2, 0, 3, 0, 4]
        self.s.moveZeroes(nums)
        self.assertEqual(nums, [1, 2, 3, 4, 0, 0, 0])

    def test_single_element_nonzero(self):
        nums = [5]
        self.s.moveZeroes(nums)
        self.assertEqual(nums, [5])

    def test_large_input(self):
        nums = [0] * 5000 + [1] * 5000
        expected = [1] * 5000 + [0] * 5000
        self.s.moveZeroes(nums)
        self.assertEqual(nums, expected)


if __name__ == "__main__":
    unittest.main()
