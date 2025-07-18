import unittest
from solution import Solution

class TestKClosestPoints(unittest.TestCase):
    def setUp(self):
        self.solver = Solution()

    def assertPointsEqual(self, result, expected):
        self.assertEqual(sorted(map(tuple, result)), sorted(map(tuple, expected)))

    def test_example1(self):
        points = [[1,3],[-2,2]]
        k = 1
        expected = [[-2,2]]
        result = self.solver.kClosest(points, k)
        self.assertPointsEqual(result, expected)

    def test_example2(self):
        points = [[3,3],[5,-1],[-2,4]]
        k = 2
        expected = [[3,3],[-2,4]]
        result = self.solver.kClosest(points, k)
        self.assertPointsEqual(result, expected)

    def test_all_points(self):
        points = [[1,1],[2,2],[3,3]]
        k = 3
        expected = [[1,1],[2,2],[3,3]]
        result = self.solver.kClosest(points, k)
        self.assertPointsEqual(result, expected)

    def test_negative_coordinates(self):
        points = [[-5,-4],[2,-1],[-3,3]]
        k = 2
        expected = [[2,-1],[-3,3]]
        result = self.solver.kClosest(points, k)
        self.assertPointsEqual(result, expected)

    def test_duplicates(self):
        points = [[1,1],[1,1],[2,2]]
        k = 2
        expected = [[1,1],[1,1]]
        result = self.solver.kClosest(points, k)
        self.assertPointsEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
