import unittest

from solution import Solution


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        solution = Solution()
        grid = [[1, 0], [0, 1]]
        self.assertEqual(solution.countServers(grid), 0)

    def test_example_2(self):
        solution = Solution()
        grid = [[1, 0], [1, 1]]
        self.assertEqual(solution.countServers(grid), 3)

    def test_example_3(self):
        solution = Solution()
        grid = [[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
        self.assertEqual(solution.countServers(grid), 4)

    def test_example_5(self):
        solution = Solution()
        grid = [[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
        self.assertEqual(solution.countServers(grid), 4)

    def test_example_6(self):
        solution = Solution()
        grid = [[1, 0], [1, 1]]
        self.assertEqual(solution.countServers(grid), 3)


if __name__ == "__main__":
    unittest.main()
