import unittest

from solution import Solution


class TestAddFunction(unittest.TestCase):

    def test_1(self):
        result = Solution().search([4, 5, 6, 7, 0, 1, 2], 0)
        self.assertEqual(result, 4)

    def test_2(self):
        result = Solution().search([4, 5, 6, 7, 0, 1, 2], 3)
        self.assertEqual(result, -1)

    def test_3(self):
        result = Solution().search([1], 0)
        self.assertEqual(result, -1)

    def test_4(self):
        result = Solution().search([3, 4, 5, 6, 1, 2], 1)
        self.assertEqual(result, 4)

    def test_5(self):
        result = Solution().search([3, 5, 6, 0, 1, 2], 4)
        self.assertEqual(result, -1)


if __name__ == "__main__":
    unittest.main()
