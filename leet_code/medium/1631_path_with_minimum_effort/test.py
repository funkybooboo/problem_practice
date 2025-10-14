import unittest
from solution import Solution

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        heights = [[1,2,2],[3,8,2],[5,3,5]]
        expected = 2
        self.assertEqual(self.solution.minimumEffortPath(heights), expected)

    def test_example_2(self):
        heights = [[1,2,3],[3,8,4],[5,3,5]]
        expected = 1
        self.assertEqual(self.solution.minimumEffortPath(heights), expected)

    def test_example_3(self):
        heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
        expected = 0
        self.assertEqual(self.solution.minimumEffortPath(heights), expected)

    def test_example_4(self):
        heights = [
            [1,1,1],
            [3,2,4],
            [2,5,4]
        ]
        expected = 2
        self.assertEqual(self.solution.minimumEffortPath(heights), expected)

    def test_example_5(self):
        heights = [
            [1,1,1],
            [1,1,2],
            [6,5,2]
        ]
        expected = 1
        self.assertEqual(self.solution.minimumEffortPath(heights), expected)

if __name__ == '__main__':
    unittest.main()
