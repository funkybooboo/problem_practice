import unittest
from solution import Solution


class TestHammingWeight(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.hammingWeight(11), 3)

    def test_example_2(self):
        self.assertEqual(self.solution.hammingWeight(128), 1)

    def test_example_3(self):
        self.assertEqual(self.solution.hammingWeight(2147483645), 30)

    def test_example_4(self):
        self.assertEqual(
            self.solution.hammingWeight(int("00000000000000000000000000010111", 2)), 4
        )

    def test_example_5(self):
        self.assertEqual(
            self.solution.hammingWeight(int("01111111111111111111111111111101", 2)), 30
        )


if __name__ == "__main__":
    unittest.main()
