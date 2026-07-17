import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(
            self.sol.replaceElements([17, 18, 5, 4, 6, 1]),
            [18, 6, 6, 6, 1, -1]
        )

    def test_example2(self):
        self.assertEqual(
            self.sol.replaceElements([400]),
            [-1]
        )

    def test_example3(self):
        self.assertEqual(
            self.sol.replaceElements([2, 4, 5, 3, 1, 2]),
            [5, 5, 3, 2, 2, -1]
        )

    def test_example4(self):
        self.assertEqual(
            self.sol.replaceElements([3, 3]),
            [3, -1]
        )

    def test_sorted_decreasing(self):
        # worst case for many approaches
        self.assertEqual(
            self.sol.replaceElements([9, 7, 5, 3, 1]),
            [7, 5, 3, 1, -1]
        )

    def test_sorted_increasing(self):
        self.assertEqual(
            self.sol.replaceElements([1, 2, 3, 4, 5]),
            [5, 5, 5, 5, -1]
        )

    def test_all_same(self):
        self.assertEqual(
            self.sol.replaceElements([7, 7, 7]),
            [7, 7, -1]
        )


if __name__ == "__main__":
    unittest.main()
