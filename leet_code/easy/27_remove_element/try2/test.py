import unittest
from solution import Solution

class TestRemoveElement(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def assertValidResult(self, nums, val, k, expected_remaining):
        # k must match expected count
        self.assertEqual(k, len(expected_remaining))
        # First k elements, when sorted, must match expected_remaining sorted
        self.assertEqual(sorted(nums[:k]), sorted(expected_remaining))
        # No element equal to val should appear in first k positions
        for i in range(k):
            self.assertNotEqual(nums[i], val)

    def test_empty_array(self):
        nums = []
        val = 1
        k = self.sol.removeElement(nums, val)
        self.assertValidResult(nums, val, k, [])

    def test_single_element_equal_val(self):
        nums = [5]
        val = 5
        k = self.sol.removeElement(nums, val)
        self.assertValidResult(nums, val, k, [])

    def test_single_element_not_equal_val(self):
        nums = [5]
        val = 3
        k = self.sol.removeElement(nums, val)
        self.assertValidResult(nums, val, k, [5])

    def test_all_elements_equal_val(self):
        nums = [2, 2, 2, 2]
        val = 2
        k = self.sol.removeElement(nums, val)
        self.assertValidResult(nums, val, k, [])

    def test_no_elements_equal_val(self):
        nums = [1, 3, 5, 7]
        val = 2
        k = self.sol.removeElement(nums, val)
        self.assertValidResult(nums, val, k, [1, 3, 5, 7])

    def test_example_1(self):
        nums = [3, 2, 2, 3]
        val = 3
        k = self.sol.removeElement(nums, val)
        self.assertValidResult(nums, val, k, [2, 2])

    def test_example_2(self):
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        val = 2
        k = self.sol.removeElement(nums, val)
        self.assertValidResult(nums, val, k, [0, 1, 0, 3, 4])

    def test_mixed_positions(self):
        nums = [1, 2, 3, 2, 4, 2, 5]
        val = 2
        k = self.sol.removeElement(nums, val)
        self.assertValidResult(nums, val, k, [1, 3, 4, 5])

    def test_val_not_in_range_of_nums(self):
        nums = [0, 0, 0]
        val = 100
        k = self.sol.removeElement(nums, val)
        self.assertValidResult(nums, val, k, [0, 0, 0])

    def test_nums_length_max(self):
        nums = [i % 5 for i in range(100)]
        val = 3
        expected = [x for x in nums if x != val]
        k = self.sol.removeElement(nums, val)
        self.assertValidResult(nums, val, k, expected)

if __name__ == "__main__":
    unittest.main()

