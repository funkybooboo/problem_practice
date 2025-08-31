import unittest

from solution import Solution

class TestMergeIntervals(unittest.TestCase):

    def test_1(self):
        intervals = [[1,3],[2,6],[8,10],[15,18]]
        expected_output = [[1,6],[8,10],[15,18]]
        result = Solution().merge(intervals)
        self.assertEqual(result, expected_output)

    def test_2(self):
        intervals = [[1,4],[4,5]]
        expected_output = [[1,5]]
        result = Solution().merge(intervals)
        self.assertEqual(result, expected_output)

    def test_3(self):
        intervals = [[4,7],[1,4]]
        expected_output = [[1,7]]
        result = Solution().merge(intervals)
        self.assertEqual(result, expected_output)

    def test_4(self):
        intervals = [[1,10],[2,9],[3,8],[4,7],[5,6]]
        expected_output = [[1,10]]
        result = Solution().merge(intervals)
        self.assertEqual(result, expected_output)

    def test_5(self):
        intervals = [[1,1],[2,2],[3,3],[4,4]]
        expected_output = [[1,1],[2,2],[3,3],[4,4]]
        result = Solution().merge(intervals)
        self.assertEqual(result, expected_output)

if __name__ == "__main__":
    unittest.main()
