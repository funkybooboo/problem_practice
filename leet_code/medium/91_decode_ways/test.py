import unittest
from solution import Solution

class TestNumDecodings(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.numDecodings("12"), 2)
        # "AB" (1 2) and "L" (12)

    def test_example_2(self):
        self.assertEqual(self.solution.numDecodings("226"), 3)
        # "BZ" (2 26), "VF" (22 6), "BBF" (2 2 6)

    def test_example_3(self):
        self.assertEqual(self.solution.numDecodings("06"), 0)
        # Invalid due to leading zero

    def test_single_digit(self):
        self.assertEqual(self.solution.numDecodings("1"), 1)
        # "A"

    def test_invalid_zero(self):
        self.assertEqual(self.solution.numDecodings("0"), 0)
        # "0" is not valid

    def test_multiple_zeros(self):
        self.assertEqual(self.solution.numDecodings("100"), 0)
        # "10" is valid, but "0" at end is not

    def test_long_valid(self):
        self.assertEqual(self.solution.numDecodings("11106"), 2)
        # "AAJF" (1 1 10 6) and "KJF" (11 10 6)

    def test_large_number_of_ways(self):
        self.assertEqual(self.solution.numDecodings("1111111111"), 89)
        # Fibonacci-like growth in decoding combinations

if __name__ == "__main__":
    unittest.main()
