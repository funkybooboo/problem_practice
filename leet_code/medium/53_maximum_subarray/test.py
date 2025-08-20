import unittest
from solution import Solution

class TestMaxSubArray(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)

    def test_example_2(self):
        self.assertEqual(Solution().maxSubArray([1]), 1)

    def test_example_3(self):
        self.assertEqual(Solution().maxSubArray([5, 4, -1, 7, 8]), 23)

    def test_single_element_array(self):
        self.assertEqual(Solution().maxSubArray([-1]), -1)

    def test_all_negative_numbers(self):
        self.assertEqual(Solution().maxSubArray([-1, -2, -3, -4]), -1)

    def test_all_positive_numbers(self):
        self.assertEqual(Solution().maxSubArray([1, 2, 3, 4]), 10)

    def test_mixed_numbers(self):
        self.assertEqual(Solution().maxSubArray([-2, 3, -1, 4, -1, 2, 1, -5, 4]), 8)

if __name__ == '__main__':
    unittest.main()
