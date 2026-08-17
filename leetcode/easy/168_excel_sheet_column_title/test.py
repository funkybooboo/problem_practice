import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_one(self):
        self.assertEqual(self.sol.convertToTitle(1), "A")

    def test_example_two(self):
        self.assertEqual(self.sol.convertToTitle(28), "AB")

    def test_example_three(self):
        self.assertEqual(self.sol.convertToTitle(701), "ZY")

    def test_single_letter_z(self):
        self.assertEqual(self.sol.convertToTitle(26), "Z")

    def test_double_letters_aa(self):
        self.assertEqual(self.sol.convertToTitle(27), "AA")

    def test_double_letters_az(self):
        self.assertEqual(self.sol.convertToTitle(52), "AZ")

    def test_double_letters_ba(self):
        self.assertEqual(self.sol.convertToTitle(53), "BA")

    def test_double_letters_zz(self):
        self.assertEqual(self.sol.convertToTitle(702), "ZZ")

    def test_triple_letters_aaa(self):
        self.assertEqual(self.sol.convertToTitle(703), "AAA")

    def test_large_number(self):
        # 2^31 - 1 = 2147483647
        self.assertEqual(self.sol.convertToTitle(2147483647), "FXSHRXW")


if __name__ == "__main__":
    unittest.main()
