import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    # Example test cases from problem description
    def test_example_one(self):
        nums1 = [4, 1, 2]
        nums2 = [1, 3, 4, 2]
        expected = [-1, 3, -1]
        self.assertEqual(self.sol.nextGreaterElement(nums1, nums2), expected)

    def test_example_two(self):
        nums1 = [2, 4]
        nums2 = [1, 2, 3, 4]
        expected = [3, -1]
        self.assertEqual(self.sol.nextGreaterElement(nums1, nums2), expected)

    # Edge case: single element in nums1
    def test_single_element_nums1(self):
        nums1 = [1]
        nums2 = [1, 2]
        expected = [2]
        self.assertEqual(self.sol.nextGreaterElement(nums1, nums2), expected)

    # Edge case: single element in both arrays
    def test_single_element_both(self):
        nums1 = [1]
        nums2 = [1]
        expected = [-1]
        self.assertEqual(self.sol.nextGreaterElement(nums1, nums2), expected)

    # Edge case: nums1 equals nums2
    def test_nums1_equals_nums2(self):
        nums1 = [1, 2, 3]
        nums2 = [1, 2, 3]
        expected = [2, 3, -1]
        self.assertEqual(self.sol.nextGreaterElement(nums1, nums2), expected)

    # Edge case: all elements have no next greater element
    def test_all_no_next_greater(self):
        nums1 = [5, 4, 3]
        nums2 = [5, 4, 3, 2, 1]
        expected = [-1, -1, -1]
        self.assertEqual(self.sol.nextGreaterElement(nums1, nums2), expected)

    # Edge case: all elements have next greater element
    def test_all_have_next_greater(self):
        nums1 = [1, 2, 3]
        nums2 = [1, 2, 3, 4, 5]
        expected = [2, 3, 4]
        self.assertEqual(self.sol.nextGreaterElement(nums1, nums2), expected)

    # Boundary: minimum values (0)
    def test_minimum_values(self):
        nums1 = [0]
        nums2 = [0, 1]
        expected = [1]
        self.assertEqual(self.sol.nextGreaterElement(nums1, nums2), expected)

    # Boundary: maximum values (10^4)
    def test_maximum_values(self):
        nums1 = [10000]
        nums2 = [9999, 10000]
        expected = [-1]
        self.assertEqual(self.sol.nextGreaterElement(nums1, nums2), expected)

    # Boundary: maximum length (nums2 = 1000, nums1 subset)
    def test_large_arrays(self):
        nums2 = list(range(1000))
        nums1 = [0, 500, 999]
        expected = [1, 501, -1]
        self.assertEqual(self.sol.nextGreaterElement(nums1, nums2), expected)

    # Domain-specific: element at end of nums2
    def test_element_at_end_of_nums2(self):
        nums1 = [5]
        nums2 = [1, 2, 3, 4, 5]
        expected = [-1]
        self.assertEqual(self.sol.nextGreaterElement(nums1, nums2), expected)

    # Domain-specific: element at beginning of nums2
    def test_element_at_beginning_of_nums2(self):
        nums1 = [1]
        nums2 = [1, 2, 3, 4, 5]
        expected = [2]
        self.assertEqual(self.sol.nextGreaterElement(nums1, nums2), expected)

    # Domain-specific: descending order in nums2
    def test_descending_order_nums2(self):
        nums1 = [3, 2, 1]
        nums2 = [5, 4, 3, 2, 1]
        expected = [-1, -1, -1]
        self.assertEqual(self.sol.nextGreaterElement(nums1, nums2), expected)

    # Domain-specific: ascending order in nums2
    def test_ascending_order_nums2(self):
        nums1 = [1, 3, 5]
        nums2 = [1, 2, 3, 4, 5]
        expected = [2, 4, -1]
        self.assertEqual(self.sol.nextGreaterElement(nums1, nums2), expected)

    # Domain-specific: nums1 in reverse order of appearance in nums2
    def test_nums1_reverse_order(self):
        nums1 = [5, 3, 1]
        nums2 = [1, 2, 3, 4, 5]
        expected = [-1, 4, 2]
        self.assertEqual(self.sol.nextGreaterElement(nums1, nums2), expected)

    # Domain-specific: next greater element is immediately after
    def test_next_greater_immediate(self):
        nums1 = [1, 2, 3]
        nums2 = [1, 2, 3, 4]
        expected = [2, 3, 4]
        self.assertEqual(self.sol.nextGreaterElement(nums1, nums2), expected)

    # Domain-specific: next greater element is far away
    def test_next_greater_far_away(self):
        nums1 = [1]
        nums2 = [1, 0, 0, 0, 0, 2]
        expected = [2]
        self.assertEqual(self.sol.nextGreaterElement(nums1, nums2), expected)

    # Domain-specific: mixed pattern with peaks and valleys
    def test_mixed_pattern(self):
        nums1 = [3, 1, 5, 7, 2]
        nums2 = [1, 3, 5, 2, 7, 4, 6]
        expected = [5, 3, 7, -1, 7]
        self.assertEqual(self.sol.nextGreaterElement(nums1, nums2), expected)

    # Domain-specific: multiple smaller elements before next greater
    def test_multiple_smaller_before_greater(self):
        nums1 = [10]
        nums2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11]
        expected = [11]
        self.assertEqual(self.sol.nextGreaterElement(nums1, nums2), expected)

    # Domain-specific: alternating high and low values
    def test_alternating_values(self):
        nums1 = [1, 5, 2, 6]
        nums2 = [1, 5, 2, 6, 3, 7]
        expected = [5, 6, 6, 7]
        self.assertEqual(self.sol.nextGreaterElement(nums1, nums2), expected)

if __name__ == "__main__":
    unittest.main()
