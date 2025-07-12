import unittest
from solution import Solution

class TestFindRedundantConnection(unittest.TestCase):
    def test_example_1(self):
        # Input: [[1,2],[1,3],[2,3]] — the cycle is formed by [2,3]
        self.assertEqual(Solution().findRedundantConnection([[1, 2], [1, 3], [2, 3]]), [2, 3])

    def test_example_2(self):
        # Input: [[1,2],[2,3],[3,4],[1,4],[1,5]] — the cycle is formed by [1,4]
        self.assertEqual(Solution().findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]), [1, 4])

    def test_small_triangle(self):
        # Simple triangle: all 3 nodes form a cycle
        self.assertEqual(Solution().findRedundantConnection([[1, 2], [2, 3], [3, 1]]), [3, 1])

    def test_larger_cycle(self):
        # A longer chain that forms a cycle at the end
        self.assertEqual(Solution().findRedundantConnection([[1, 2], [2, 3], [3, 4], [4, 5], [2, 5]]), [2, 5])

    def test_early_cycle(self):
        # The cycle is introduced early, but we return the last edge that completes it
        self.assertEqual(Solution().findRedundantConnection([[1, 2], [1, 3], [2, 3], [3, 4]]), [2, 3])

if __name__ == '__main__':
    unittest.main()
