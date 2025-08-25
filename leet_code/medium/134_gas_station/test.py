import unittest
from solution import Solution

class TestCanCompleteCircuit(unittest.TestCase):
    def test_example_1(self):
        # Example 1: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
        self.assertEqual(Solution().canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]), 3)

    def test_example_2(self):
        # Example 2: gas = [2,3,4], cost = [3,4,3]
        self.assertEqual(Solution().canCompleteCircuit([2, 3, 4], [3, 4, 3]), -1)

    def test_single_element(self):
        # Single element array, always reachable
        self.assertEqual(Solution().canCompleteCircuit([10], [10]), 0)

    def test_unreachable_end(self):
        # Array where the last index is unreachable
        self.assertEqual(Solution().canCompleteCircuit([0, 1, 2, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1]), -1)

    def test_all_reachable(self):
        # Array where all elements are 1, making the last index reachable
        self.assertEqual(Solution().canCompleteCircuit([1, 1, 1, 1, 1], [1, 1, 1, 1, 1]), 0)

    def test_zero_jumps(self):
        # Array with all zeros, only the first element is reachable
        self.assertEqual(Solution().canCompleteCircuit([0, 0, 0, 0, 0], [1, 1, 1, 1, 1]), -1)

    def test_zero_gap(self):
        # Array with all zeros, only the first element is reachable
        self.assertEqual(Solution().canCompleteCircuit([4, 0, 0, 0, 1], [1, 1, 1, 1, 1]), 0)

if __name__ == '__main__':
    unittest.main()
