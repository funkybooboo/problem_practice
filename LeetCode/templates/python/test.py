import unittest

from solution import Solution


class TestAddFunction(unittest.TestCase):

    def test_add_positive_numbers(self):
        result = Solution().add(2, 3)
        self.assertEqual(result, 5)  # Test that 2 + 3 equals 5

    def test_add_negative_numbers(self):
        result = Solution().add(-2, -3)
        self.assertEqual(result, -5)  # Test that -2 + -3 equals -5

    def test_add_mixed_numbers(self):
        result = Solution().add(-2, 3)
        self.assertEqual(result, 1)  # Test that -2 + 3 equals 1

    def test_add_zero(self):
        result = Solution().add(0, 0)
        self.assertEqual(result, 0)  # Test that 0 + 0 equals 0


if __name__ == "__main__":
    unittest.main()
