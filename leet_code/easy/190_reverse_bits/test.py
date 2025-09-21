import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_example_1(self):
        sol = Solution()
        self.assertEqual(sol.reverseBits(43261596), 964176192)

    def test_example_2(self):
        sol = Solution()
        self.assertEqual(sol.reverseBits(2147483644), 1073741822)

if __name__ == "__main__":
    unittest.main()
