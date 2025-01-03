import unittest

from solution import Solution


class TestAddFunction(unittest.TestCase):

    def test_exist(self):
        nums = [1, 3, 5, 6]
        target = 5
        self.assertEqual(Solution().searchInsert(nums, target), 2)

    def test_non_exist_front(self):
        nums = [1, 3, 5, 6]
        target = 2
        self.assertEqual(Solution().searchInsert(nums, target), 1)

    def test_non_exist_end(self):
        nums = [1, 3, 5, 6]
        target = 7
        self.assertEqual(Solution().searchInsert(nums, target), 4)

    def test_non_exist_zero(self):
        nums = [1, 3, 5, 6]
        target = 0
        self.assertEqual(Solution().searchInsert(nums, target), 0)


if __name__ == '__main__':
    unittest.main()
