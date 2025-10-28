import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        solution = Solution()
        chars = ["a", "a", "b", "b", "c", "c", "c"]
        result = solution.compress(chars)
        self.assertEqual(result, 6)
        self.assertEqual(chars[:6], ["a", "2", "b", "2", "c", "3"])

    def test_example_2(self):
        solution = Solution()
        chars = ["a"]
        result = solution.compress(chars)
        self.assertEqual(result, 1)
        self.assertEqual(chars[:1], ["a"])

    def test_example_3(self):
        solution = Solution()
        chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
        result = solution.compress(chars)
        self.assertEqual(result, 4)
        self.assertEqual(chars[:4], ["a", "b", "1", "2"])

    def test_example_4(self):
        solution = Solution()
        chars = ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"]
        result = solution.compress(chars)
        self.assertEqual(result, 3)
        self.assertEqual(chars[:3], ["a", "1", "1"])

    def test_example_5(self):
        solution = Solution()
        chars = ["A"]
        result = solution.compress(chars)
        self.assertEqual(result, 1)
        self.assertEqual(chars[:1], ["A"])

    def test_example_6(self):
        solution = Solution()
        chars = ["1", "1", "2"]
        result = solution.compress(chars)
        self.assertEqual(result, 3)
        self.assertEqual(chars[:3], ["1", "2", "2"])


if __name__ == '__main__':
    unittest.main()
