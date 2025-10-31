import unittest
from solution import Solution


class TestSurroundedRegions(unittest.TestCase):
    def test_example1(self):
        board = [
            ["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "O", "X"],
            ["X", "O", "X", "X"],
        ]
        expected = [
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "O", "X", "X"],
        ]
        Solution().solve(board)
        self.assertEqual(board, expected)

    def test_example2(self):
        board = [["X"]]
        expected = [["X"]]
        Solution().solve(board)
        self.assertEqual(board, expected)

    def test_no_surrounded(self):
        board = [["O", "O", "O"], ["O", "X", "O"], ["O", "O", "O"]]
        # all Os touch the edge, so none should be flipped
        expected = [["O", "O", "O"], ["O", "X", "O"], ["O", "O", "O"]]
        Solution().solve(board)
        self.assertEqual(board, expected)

    def test_all_surrounded(self):
        board = [
            ["X", "X", "X", "X", "X"],
            ["X", "O", "O", "O", "X"],
            ["X", "O", "X", "O", "X"],
            ["X", "O", "O", "O", "X"],
            ["X", "X", "X", "X", "X"],
        ]
        # the entire inner region is surrounded
        expected = [
            ["X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X"],
        ]
        Solution().solve(board)
        self.assertEqual(board, expected)

    def test_single_row(self):
        board = [["O", "X", "O", "O", "X"]]
        # single-row regions always touch the edge; no flips
        expected = [["O", "X", "O", "O", "X"]]
        Solution().solve(board)
        self.assertEqual(board, expected)

    def test_single_col(self):
        board = [["O"], ["X"], ["O"], ["O"], ["X"]]
        expected = [["O"], ["X"], ["O"], ["O"], ["X"]]
        Solution().solve(board)
        self.assertEqual(board, expected)


if __name__ == "__main__":
    unittest.main()
