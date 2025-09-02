import unittest

from solution import Solution

class TestEraseOverlapIntervals(unittest.TestCase):

    def test_example_1(self):
        intervals = [[1,2],[2,3],[3,4],[1,3]]
        result = Solution().eraseOverlapIntervals(intervals)
        self.assertEqual(result, 1)

    def test_example_2(self):
        intervals = [[1,2],[1,2],[1,2]]
        result = Solution().eraseOverlapIntervals(intervals)
        self.assertEqual(result, 2)

    def test_example_3(self):
        intervals = [[1,2],[2,3]]
        result = Solution().eraseOverlapIntervals(intervals)
        self.assertEqual(result, 0)

    def test_empty_intervals(self):
        intervals = []
        result = Solution().eraseOverlapIntervals(intervals)
        self.assertEqual(result, 0)

    def test_single_interval(self):
        intervals = [[1, 2]]
        result = Solution().eraseOverlapIntervals(intervals)
        self.assertEqual(result, 0)

    def test_overlapping_intervals(self):
        intervals = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6]]
        result = Solution().eraseOverlapIntervals(intervals)
        self.assertEqual(result, 4)

    def test_non_overlapping_intervals(self):
        intervals = [[1, 2], [3, 4], [5, 6]]
        result = Solution().eraseOverlapIntervals(intervals)
        self.assertEqual(result, 0)

    def test_intervals_with_same_start(self):
        intervals = [[1, 3], [1, 2], [1, 4]]
        result = Solution().eraseOverlapIntervals(intervals)
        self.assertEqual(result, 2)

    def test_intervals_with_same_end(self):
        intervals = [[2, 3], [1, 3], [1, 4]]
        result = Solution().eraseOverlapIntervals(intervals)
        self.assertEqual(result, 2)

if __name__ == "__main__":
    unittest.main()
