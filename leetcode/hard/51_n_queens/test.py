import unittest

from solution import Solution


class TestNQueens(unittest.TestCase):

    def test_n_1(self):
        sol = Solution()
        result = sol.solveNQueens(1)
        expected = [["Q"]]
        self.assertEqual(result, expected)

    def test_n_2(self):
        sol = Solution()
        result = sol.solveNQueens(2)
        expected = []
        self.assertEqual(result, expected)

    def test_n_3(self):
        sol = Solution()
        result = sol.solveNQueens(3)
        expected = []
        self.assertEqual(result, expected)

    def test_n_4(self):
        sol = Solution()
        result = sol.solveNQueens(4)
        expected = [
            [".Q..", "...Q", "Q...", "..Q."],
            ["..Q.", "Q...", "...Q", ".Q.."],
        ]
        # Order of the two valid boards may vary
        self.assertCountEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
