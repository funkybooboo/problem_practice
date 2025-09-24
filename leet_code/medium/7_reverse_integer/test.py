import unittest
from solution import Solution

class TestSolution(unittest.TestCase):

    def test_reverse_positive(self):
        sol = Solution()
        self.assertEqual(sol.reverse(123), 321)
        self.assertEqual(sol.reverse(120), 21)
        self.assertEqual(sol.reverse(1234), 4321)

    def test_reverse_negative(self):
        sol = Solution()
        self.assertEqual(sol.reverse(-123), -321)
        self.assertEqual(sol.reverse(-1234), -4321)

    def test_reverse_out_of_range(self):
        sol = Solution()
        self.assertEqual(sol.reverse(1234236467), 0)

if __name__ == "__main__":
    unittest.main()
