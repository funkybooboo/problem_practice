import unittest

from solution import DetectSquares

class TestSolution(unittest.TestCase):

    def test_example_1(self):
        detectSquares = DetectSquares()
        detectSquares.add([3, 10])
        detectSquares.add([11, 2])
        detectSquares.add([3, 2])
        self.assertEqual(detectSquares.count([11, 10]), 1)
        self.assertEqual(detectSquares.count([14, 8]), 0)
        detectSquares.add([11, 2])
        self.assertEqual(detectSquares.count([11, 10]), 2)

    def test_example_2(self):
        countSquares = DetectSquares()
        countSquares.add([1, 1])
        countSquares.add([2, 2])
        countSquares.add([1, 2])
        self.assertEqual(countSquares.count([2, 1]), 1)
        self.assertEqual(countSquares.count([3, 3]), 0)
        countSquares.add([2, 2])
        self.assertEqual(countSquares.count([2, 1]), 2)

if __name__ == "__main__":
    unittest.main()
