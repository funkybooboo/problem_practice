import unittest
from solution import Solution

class TestCanFinish(unittest.TestCase):
    def test_simple_possible(self):
        # Example 1: 2 courses, one prerequisite 1 → 0
        self.assertTrue(Solution().canFinish(2, [[1, 0]]))

    def test_simple_impossible(self):
        # Example 2: 2 courses, circular prerequisites 1 → 0 and 0 → 1
        self.assertFalse(Solution().canFinish(2, [[1, 0], [0, 1]]))

    def test_no_prerequisites(self):
        # With no prerequisites, you can always finish
        self.assertTrue(Solution().canFinish(5, []))
        self.assertTrue(Solution().canFinish(1, []))

    def test_larger_graphs(self):
        # A larger acyclic graph
        self.assertTrue(Solution().canFinish(
            5,
            [[1, 0], [2, 0], [3, 1], [3, 2], [4, 3]]
        ))
        # A larger graph with a cycle
        self.assertFalse(Solution().canFinish(
            4,
            [[1, 0], [2, 1], [3, 2], [1, 3]]
        ))

if __name__ == '__main__':
    unittest.main()
