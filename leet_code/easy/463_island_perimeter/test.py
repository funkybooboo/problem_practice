import unittest

from solution import Solution


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        solution = Solution()
        grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
        self.assertEqual(solution.islandPerimeter(grid), 16)

    def test_example_2(self):
        solution = Solution()
        grid = [[1]]
        self.assertEqual(solution.islandPerimeter(grid), 4)

    def test_example_3(self):
        solution = Solution()
        grid = [[1, 0]]
        self.assertEqual(solution.islandPerimeter(grid), 4)

    def test_example_4(self):
        solution = Solution()
        grid = [[1, 1, 0, 0], [1, 0, 0, 0], [1, 1, 1, 0], [0, 0, 1, 1]]
        self.assertEqual(solution.islandPerimeter(grid), 18)


if __name__ == "__main__":
    unittest.main()
