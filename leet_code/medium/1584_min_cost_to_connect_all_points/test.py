import unittest
from solution import Solution

class TestMinCostConnectPoints(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
        self.assertEqual(self.solution.minCostConnectPoints(points), 20)

    def test_example2(self):
        points = [[3,12],[-2,5],[-4,1]]
        self.assertEqual(self.solution.minCostConnectPoints(points), 18)

    def test_single_point(self):
        points = [[42, -17]]
        self.assertEqual(self.solution.minCostConnectPoints(points), 0)

    def test_two_points(self):
        points = [[-1, -1], [2, 3]]
        # | -1 - 2 | + | -1 - 3 | = 3 + 4 = 7
        self.assertEqual(self.solution.minCostConnectPoints(points), 7)

    def test_small_grid_square(self):
        # A 2x2 grid: MST should pick three unit edges -> cost = 3
        points = [[0,0], [0,1], [1,0], [1,1]]
        self.assertEqual(self.solution.minCostConnectPoints(points), 3)

    def test_colinear_points(self):
        # Optimal is to connect in order along the line: 0-2 (2), 2-3 (1) => total 3
        points = [[0,0], [2,0], [3,0]]
        self.assertEqual(self.solution.minCostConnectPoints(points), 3)

    def test_large_coordinates(self):
        # Two far-apart points
        points = [[0,0], [10**6, 10**6]]
        self.assertEqual(self.solution.minCostConnectPoints(points), 2 * 10**6)

    def test_mixed_negative_positive(self):
        # A simple shape where it's optimal to chain through middle points
        points = [[-3,-3], [-1,-1], [2,0], [4,1]]
        # One optimal MST: (-3,-3)->(-1,-1)=4, (-1,-1)->(2,0)=3, (2,0)->(4,1)=3 => 10
        self.assertEqual(self.solution.minCostConnectPoints(points), 11)

if __name__ == '__main__':
    unittest.main()
