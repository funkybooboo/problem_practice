import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        ops = ["5","2","C","D","+"]
        self.assertEqual(self.sol.calPoints(ops), 30)

    def test_example2(self):
        ops = ["5","-2","4","C","D","9","+","+"]
        self.assertEqual(self.sol.calPoints(ops), 27)

    def test_example3(self):
        ops = ["1","C"]
        self.assertEqual(self.sol.calPoints(ops), 0)

    def test_example4(self):
        ops = ["1","2","+","C","5","D"]
        self.assertEqual(self.sol.calPoints(ops), 18)

    def test_example5(self):
        ops = ["5","D","+","C"]
        self.assertEqual(self.sol.calPoints(ops), 15)


if __name__ == "__main__":
    unittest.main()
