import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.findJudge(2, [[1, 2]]), 2)

    def test_example2(self):
        self.assertEqual(self.s.findJudge(3, [[1, 3], [2, 3]]), 3)

    def test_example3(self):
        self.assertEqual(self.s.findJudge(3, [[1, 3], [2, 3], [3, 1]]), -1)

    def test_example4(self):
        self.assertEqual(self.s.findJudge(4, [[1, 3], [4, 3], [2, 3]]), 3)

    def test_example5(self):
        self.assertEqual(self.s.findJudge(3, [[1, 3], [2, 3], [3, 1], [3, 2]]), -1)


if __name__ == "__main__":
    unittest.main()
