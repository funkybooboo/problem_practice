import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        nums = [1, 2, 1]
        expected = [1, 2, 1, 1, 2, 1]
        self.assertEqual(self.sol.getConcatenation(nums), expected)

    def test_example_2(self):
        nums = [1, 3, 2, 1]
        expected = [1, 3, 2, 1, 1, 3, 2, 1]
        self.assertEqual(self.sol.getConcatenation(nums), expected)

    def test_example_3(self):
        nums = [1, 4, 1, 2]
        expected = [1, 4, 1, 2, 1, 4, 1, 2]
        self.assertEqual(self.sol.getConcatenation(nums), expected)

    def test_example_4(self):
        nums = [22, 21, 20, 1]
        expected = [22, 21, 20, 1, 22, 21, 20, 1]
        self.assertEqual(self.sol.getConcatenation(nums), expected)

    def test_single_element(self):
        nums = [5]
        expected = [5, 5]
        self.assertEqual(self.sol.getConcatenation(nums), expected)

    def test_two_elements(self):
        nums = [7, 8]
        expected = [7, 8, 7, 8]
        self.assertEqual(self.sol.getConcatenation(nums), expected)

    def test_repeated_values(self):
        nums = [3, 3, 3]
        expected = [3, 3, 3, 3, 3, 3]
        self.assertEqual(self.sol.getConcatenation(nums), expected)

    def test_large_values(self):
        nums = [1000, 999]
        expected = [1000, 999, 1000, 999]
        self.assertEqual(self.sol.getConcatenation(nums), expected)

    def test_longer_array(self):
        nums = list(range(10))
        expected = nums + nums
        self.assertEqual(self.sol.getConcatenation(nums), expected)


if __name__ == "__main__":
    unittest.main()
