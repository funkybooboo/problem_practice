import unittest
from solution import Solution

class TestSolution(unittest.TestCase):

    def test_example_1(self):
        nums = [3, 0, 1]
        expected_output = 2
        self.assertEqual(Solution().missingNumber(nums), expected_output)

    def test_example_2(self):
        nums = [0, 1]
        expected_output = 2
        self.assertEqual(Solution().missingNumber(nums), expected_output)

    def test_example_3(self):
        nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
        expected_output = 8
        self.assertEqual(Solution().missingNumber(nums), expected_output)

    def test_example_4(self):
        nums = [1, 2, 3]
        expected_output = 0
        self.assertEqual(Solution().missingNumber(nums), expected_output)

    def test_example_5(self):
        nums = [0, 2]
        expected_output = 1
        self.assertEqual(Solution().missingNumber(nums), expected_output)

if __name__ == "__main__":
    unittest.main()
