import unittest

from solution import Solution


class TestAddFunction(unittest.TestCase):
    def test_1(self):
        result = Solution().search([-1, 0, 3, 5, 9, 12], 9)
        self.assertEqual(4, result)

    def test_2(self):
        result = Solution().search([-1, 0, 3, 5, 9, 12], 2)
        self.assertEqual(-1, result)

    def test_3(self):
        result = Solution().search([-1, 0, 2, 4, 6, 8], 4)
        self.assertEqual(3, result)

    def test_4(self):
        result = Solution().search([-1, 0, 2, 4, 6, 8], 3)
        self.assertEqual(-1, result)


if __name__ == "__main__":
    unittest.main()
