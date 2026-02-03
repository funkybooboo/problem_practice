import unittest
from solution import Solution


class TestMajorityElement(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_single_element(self):
        self.assertEqual(self.solution.majorityElement([1]), 1)

    def test_simple_majority(self):
        self.assertEqual(self.solution.majorityElement([3, 2, 3]), 3)

    def test_majority_at_end(self):
        self.assertEqual(self.solution.majorityElement([1, 2, 3, 3, 3]), 3)

    def test_majority_at_start(self):
        self.assertEqual(self.solution.majorityElement([4, 4, 4, 2, 3]), 4)

    def test_majority_in_middle(self):
        self.assertEqual(self.solution.majorityElement([1, 2, 2, 2, 3]), 2)

    def test_with_negative_numbers(self):
        self.assertEqual(self.solution.majorityElement([-1, -1, -1, 2, 3]), -1)

    def test_all_same_elements(self):
        self.assertEqual(self.solution.majorityElement([7, 7, 7, 7]), 7)

    def test_large_input(self):
        nums = [5] * 50000 + [3] * 10
        self.assertEqual(self.solution.majorityElement(nums), 5)

    def test_alternating_with_majority(self):
        nums = [1, 2] * 10 + [1] * 5
        self.assertEqual(self.solution.majorityElement(nums), 1)

    def test_majority_with_large_values(self):
        self.assertEqual(
            self.solution.majorityElement([10**9, 10**9, -10**9]),
            10**9,
        )


if __name__ == "__main__":
    unittest.main()

