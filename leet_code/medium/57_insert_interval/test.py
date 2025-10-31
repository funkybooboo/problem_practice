import unittest

from solution import Solution


class TestInsertInterval(unittest.TestCase):

    def test_1(self):
        intervals = [[1, 3], [6, 9]]
        newInterval = [2, 5]
        expected_output = [[1, 5], [6, 9]]
        self.assertEqual(Solution().insert(intervals, newInterval), expected_output)

    def test_2(self):
        intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
        newInterval = [4, 8]
        expected_output = [[1, 2], [3, 10], [12, 16]]
        self.assertEqual(Solution().insert(intervals, newInterval), expected_output)

    def test_3(self):
        intervals = []
        newInterval = [5, 7]
        expected_output = [[5, 7]]
        self.assertEqual(Solution().insert(intervals, newInterval), expected_output)

    def test_4(self):
        intervals = [[1, 5]]
        newInterval = [6, 8]
        expected_output = [[1, 5], [6, 8]]
        self.assertEqual(Solution().insert(intervals, newInterval), expected_output)

    def test_5(self):
        intervals = [[1, 5], [10, 12]]
        newInterval = [2, 6]
        expected_output = [[1, 6], [10, 12]]
        self.assertEqual(Solution().insert(intervals, newInterval), expected_output)


if __name__ == "__main__":
    unittest.main()
