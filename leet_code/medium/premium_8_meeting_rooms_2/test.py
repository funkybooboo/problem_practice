import unittest
from solution import Solution, Interval


class TestMinMeetingRooms(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        intervals = [Interval(0, 40), Interval(5, 10), Interval(15, 20)]
        expected = 2
        self.assertEqual(self.solution.minMeetingRooms(intervals), expected)

    def test_example_2(self):
        intervals = [Interval(4, 9)]
        expected = 1
        self.assertEqual(self.solution.minMeetingRooms(intervals), expected)

    def test_no_intervals(self):
        intervals = []
        expected = 0
        self.assertEqual(self.solution.minMeetingRooms(intervals), expected)

    def test_single_interval(self):
        intervals = [Interval(1, 5)]
        expected = 1
        self.assertEqual(self.solution.minMeetingRooms(intervals), expected)

    def test_overlapping_intervals(self):
        intervals = [Interval(1, 5), Interval(2, 6), Interval(8, 10)]
        expected = 2
        self.assertEqual(self.solution.minMeetingRooms(intervals), expected)

    def test_non_overlapping_intervals(self):
        intervals = [Interval(1, 3), Interval(4, 6), Interval(7, 9)]
        expected = 1
        self.assertEqual(self.solution.minMeetingRooms(intervals), expected)

    def test_max_intervals(self):
        intervals = [Interval(i, i + 1) for i in range(500)]
        expected = 1
        self.assertEqual(self.solution.minMeetingRooms(intervals), expected)

    def test_large_intervals(self):
        intervals = [Interval(0, 1000000), Interval(1, 1000000)]
        expected = 2
        self.assertEqual(self.solution.minMeetingRooms(intervals), expected)


if __name__ == "__main__":
    unittest.main()
