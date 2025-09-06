import unittest
from solution import Solution

class TestMinInterval(unittest.TestCase):
    def setUp(self):
        self.sln = Solution()

    def test_example1(self):
        intervals = [[1, 4], [2, 4], [3, 6], [4, 4]]
        queries = [2, 3, 4, 5]
        expected = [3, 3, 1, 4]
        self.assertEqual(self.sln.minInterval(intervals, queries), expected)

    def test_example2(self):
        intervals = [[2, 3], [2, 5], [1, 8], [20, 25]]
        queries = [2, 19, 5, 22]
        expected = [2, -1, 4, 6]
        self.assertEqual(self.sln.minInterval(intervals, queries), expected)

    def test_no_intervals(self):
        intervals = []
        queries = [1, 2, 3]
        expected = []
        self.assertEqual(self.sln.minInterval(intervals, queries), expected)

    def test_single_interval(self):
        intervals = [[1, 5]]
        queries = [2, 6, 1]
        expected = [5, -1, 5]
        self.assertEqual(self.sln.minInterval(intervals, queries), expected)

    def test_overlapping_intervals(self):
        intervals = [[1, 5], [2, 6], [3, 7]]
        queries = [2, 4, 8]
        expected = [5, 5, -1]
        self.assertEqual(self.sln.minInterval(intervals, queries), expected)

    def test_all_queries_outside_intervals(self):
        intervals = [[1, 3], [5, 7]]
        queries = [0, 4, 8]
        expected = [-1, -1, -1]
        self.assertEqual(self.sln.minInterval(intervals, queries), expected)

if __name__ == "__main__":
    unittest.main()
