import unittest

from solution import Solution

class TestSolution(unittest.TestCase):
    def test_example_1(self):
        sol = Solution()
        self.assertEqual(sol.multiply("2", "3"), "6")

    def test_example_2(self):
        sol = Solution()
        self.assertEqual(sol.multiply("123", "456"), "56088")

    def test_example_3(self):
        sol = Solution()
        self.assertEqual(sol.multiply("3", "4"), "12")

    def test_example_4(self):
        sol = Solution()
        self.assertEqual(sol.multiply("111", "222"), "24642")

if __name__ == "__main__":
    unittest.main()
