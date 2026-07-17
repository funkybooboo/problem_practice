import unittest
from solution import Solution


class TestDominantOnes(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        s = "00011"
        expected = 5
        self.assertEqual(self.sol.numberOfSubstrings(s), expected)

    def test_example2(self):
        s = "101101"
        expected = 16
        self.assertEqual(self.sol.numberOfSubstrings(s), expected)

    # ---- Edge cases ----

    def test_single_zero(self):
        s = "0"
        # zeros = 1, ones = 0 → 0 >= 1^2 -> False
        self.assertEqual(self.sol.numberOfSubstrings(s), 0)

    def test_single_one(self):
        s = "1"
        # zeros = 0, ones = 1 → 1 >= 0^2 -> True
        self.assertEqual(self.sol.numberOfSubstrings(s), 1)

    def test_all_zeroes(self):
        s = "0000"
        # No substring has ones ≥ zeros² except empty (not counted)
        self.assertEqual(self.sol.numberOfSubstrings(s), 0)

    def test_all_ones(self):
        s = "11111"
        # Every substring works because zeros = 0 → ones ≥ 0
        n = len(s)
        expected = n * (n + 1) // 2   # 15
        self.assertEqual(self.sol.numberOfSubstrings(s), expected)

    def test_mixed_small(self):
        s = "010"
        # Substrings:
        # "0" -> 0>=1? no
        # "1" -> 1>=0? yes
        # "0" -> no
        # "01" -> ones=1 zeros=1 → 1>=1? yes
        # "10" -> ones=1 zeros=1 → yes
        # "010" -> ones=1 zeros=2 → 1>=4? no
        expected = 3
        self.assertEqual(self.sol.numberOfSubstrings(s), expected)

    def test_large_random_like(self):
        s = "001011"
        # Brute force result should be 10
        self.assertEqual(self.sol.numberOfSubstrings(s), 10)


if __name__ == "__main__":
    unittest.main()
