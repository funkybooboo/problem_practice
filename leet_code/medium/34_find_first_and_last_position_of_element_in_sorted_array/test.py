import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_example_1(self):
        nums = [5, 7, 7, 8, 8, 10]
        target = 8
        expected_output = [3, 4]
        solution = Solution()
        self.assertEqual(solution.searchRange(nums, target), expected_output)

    def test_example_2(self):
        nums = [5, 7, 7, 8, 8, 10]
        target = 6
        expected_output = [-1, -1]
        solution = Solution()
        self.assertEqual(solution.searchRange(nums, target), expected_output)

    def test_example_3(self):
        nums = []
        target = 0
        expected_output = [-1, -1]
        solution = Solution()
        self.assertEqual(solution.searchRange(nums, target), expected_output)

    def test_single_element(self):
        nums = [5]
        target = 5
        expected_output = [0, 0]
        solution = Solution()
        self.assertEqual(solution.searchRange(nums, target), expected_output)

    def test_no_target(self):
        nums = [1, 2, 3, 4, 5]
        target = 6
        expected_output = [-1, -1]
        solution = Solution()
        self.assertEqual(solution.searchRange(nums, target), expected_output)

    def test_target_at_start(self):
        nums = [5, 7, 7, 8, 8, 10]
        target = 5
        expected_output = [0, 0]
        solution = Solution()
        self.assertEqual(solution.searchRange(nums, target), expected_output)

    def test_target_at_end(self):
        nums = [5, 7, 7, 8, 8, 10]
        target = 10
        expected_output = [5, 5]
        solution = Solution()
        self.assertEqual(solution.searchRange(nums, target), expected_output)

    def test_all_elements_same(self):
        nums = [5, 5, 5, 5, 5]
        target = 5
        expected_output = [0, 4]
        solution = Solution()
        self.assertEqual(solution.searchRange(nums, target), expected_output)

    def test_empty_array(self):
        nums = []
        target = 1
        expected_output = [-1, -1]
        solution = Solution()
        self.assertEqual(solution.searchRange(nums, target), expected_output)

    def test_single_element_not_target(self):
        nums = [5]
        target = 6
        expected_output = [-1, -1]
        solution = Solution()
        self.assertEqual(solution.searchRange(nums, target), expected_output)

    def test_large_array(self):
        nums = list(range(1000000))
        target = 500000
        expected_output = [500000, 500000]
        solution = Solution()
        self.assertEqual(solution.searchRange(nums, target), expected_output)

if __name__ == '__main__':
    unittest.main()
