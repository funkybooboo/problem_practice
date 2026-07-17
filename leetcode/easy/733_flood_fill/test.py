import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        image = [[1,1,1],[1,1,0],[1,0,1]]
        expected = [[2,2,2],[2,2,0],[2,0,1]]
        self.assertEqual(self.s.floodFill(image, 1, 1, 2), expected)

    def test_example2(self):
        image = [[0,0,0],[0,0,0]]
        expected = [[0,0,0],[0,0,0]]
        self.assertEqual(self.s.floodFill(image, 0, 0, 0), expected)

    def test_single_pixel(self):
        image = [[1]]
        expected = [[2]]
        self.assertEqual(self.s.floodFill(image, 0, 0, 2), expected)

    def test_no_change_same_color(self):
        image = [[1,1,1],[1,1,1]]
        expected = [[1,1,1],[1,1,1]]
        self.assertEqual(self.s.floodFill(image, 0, 0, 1), expected)

    def test_edge_pixel(self):
        image = [[1,1,0],[1,0,0]]
        expected = [[2,2,0],[2,0,0]]
        self.assertEqual(self.s.floodFill(image, 0, 0, 2), expected)

    def test_diagonal_not_filled(self):
        image = [[1,0,1],[0,1,0],[1,0,1]]
        expected = [[2,0,1],[0,1,0],[1,0,1]]
        self.assertEqual(self.s.floodFill(image, 0, 0, 2), expected)


if __name__ == "__main__":
    unittest.main()
