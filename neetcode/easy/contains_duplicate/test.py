import unittest

from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()
        return super().setUp()

    def test_does_contain_duplicates(self) -> None:
        self.assertEqual(self.sol.hasDuplicate([1, 2, 3, 3]), True)

    def test_does_not_contain_duplicates(self) -> None:
        self.assertEqual(self.sol.hasDuplicate([1, 2, 3, 4]), False)


if __name__ == "__main__":
    unittest.main()
