import unittest
from solution import Solution, Interval

class TestCanAttendMeetings(unittest.TestCase):

    def test_1(self):
        intervals = [Interval(0, 30), Interval(5, 10), Interval(15, 20)]
        result = Solution().canAttendMeetings(intervals)
        self.assertFalse(result)

    def test_2(self):
        intervals = [Interval(5, 8), Interval(9, 15)]
        result = Solution().canAttendMeetings(intervals)
        self.assertTrue(result)

    def test_3(self):
        intervals = [Interval(1, 5), Interval(6, 8)]
        result = Solution().canAttendMeetings(intervals)
        self.assertTrue(result)

    def test_4(self):
        intervals = [Interval(1, 5), Interval(2, 6)]
        result = Solution().canAttendMeetings(intervals)
        self.assertFalse(result)

    def test_5(self):
        intervals = [Interval(0, 10), Interval(11, 20), Interval(21, 30)]
        result = Solution().canAttendMeetings(intervals)
        self.assertTrue(result)

    def test_6(self):
        intervals = [Interval(0, 10), Interval(10, 20), Interval(20, 30)]
        result = Solution().canAttendMeetings(intervals)
        self.assertFalse(result)

    def test_7(self):
        intervals = []
        result = Solution().canAttendMeetings(intervals)
        self.assertTrue(result)

    def test_8(self):
        intervals = [Interval(0, 0)]
        result = Solution().canAttendMeetings(intervals)
        self.assertTrue(result)

    def test_9(self):
        intervals = [Interval(0, 10), Interval(0, 5)]
        result = Solution().canAttendMeetings(intervals)
        self.assertFalse(result)

    def test_10(self):
        intervals = [Interval(0, 10), Interval(5, 15)]
        result = Solution().canAttendMeetings(intervals)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
