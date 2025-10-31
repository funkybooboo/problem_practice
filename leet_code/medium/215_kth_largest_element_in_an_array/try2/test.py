import unittest
from solution import Solution


class TestFindKthLargest(unittest.TestCase):
    def setUp(self):
        self.solver = Solution()

    def test_example1(self):
        nums = [3, 2, 1, 5, 6, 4]
        k = 2
        expected = 5
        self.assertEqual(self.solver.findKthLargest(nums, k), expected)

    def test_example2(self):
        nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
        k = 4
        expected = 4
        self.assertEqual(self.solver.findKthLargest(nums, k), expected)

    def test_single_element(self):
        nums = [10]
        k = 1
        expected = 10
        self.assertEqual(self.solver.findKthLargest(nums, k), expected)

    def test_all_same(self):
        nums = [2, 2, 2, 2, 2]
        k = 3
        expected = 2
        self.assertEqual(self.solver.findKthLargest(nums, k), expected)

    def test_negative_numbers(self):
        nums = [-1, -2, -3, -4, -5]
        k = 3
        expected = -3
        self.assertEqual(self.solver.findKthLargest(nums, k), expected)

    def test_large_input(self):
        nums = list(range(1, 100001))  # 1 to 100,000
        k = 1
        expected = 100000
        self.assertEqual(self.solver.findKthLargest(nums, k), expected)


if __name__ == "__main__":
    unittest.main()
