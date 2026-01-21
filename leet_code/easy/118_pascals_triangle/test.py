import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_num_rows_one(self):
        self.assertEqual(self.sol.generate(1), [[1]])

    def test_num_rows_two(self):
        self.assertEqual(self.sol.generate(2), [[1], [1, 1]])

    def test_num_rows_three(self):
        self.assertEqual(
            self.sol.generate(3),
            [[1], [1, 1], [1, 2, 1]]
        )

    def test_num_rows_five(self):
        self.assertEqual(
            self.sol.generate(5),
            [
                [1],
                [1, 1],
                [1, 2, 1],
                [1, 3, 3, 1],
                [1, 4, 6, 4, 1],
            ]
        )

    def test_num_rows_max_constraint(self):
        result = self.sol.generate(30)
        self.assertEqual(len(result), 30)
        self.assertEqual(result[0], [1])
        self.assertEqual(result[1], [1, 1])
        self.assertEqual(result[-1][0], 1)
        self.assertEqual(result[-1][-1], 1)

    def test_pascal_property(self):
        num_rows = 10
        triangle = self.sol.generate(num_rows)
        for r in range(2, num_rows):
            for c in range(1, len(triangle[r]) - 1):
                self.assertEqual(
                    triangle[r][c],
                    triangle[r - 1][c - 1] + triangle[r - 1][c]
                )

    def test_row_lengths(self):
        num_rows = 10
        triangle = self.sol.generate(num_rows)
        for i, row in enumerate(triangle):
            self.assertEqual(len(row), i + 1)

    def test_invalid_zero_rows(self):
        self.assertEqual(self.sol.generate(0), [])

if __name__ == "__main__":
    unittest.main()

