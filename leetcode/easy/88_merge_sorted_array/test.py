import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        solution = Solution()
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3
        solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1, 2, 2, 3, 5, 6])

    def test_example_2(self):
        solution = Solution()
        nums1 = [1]
        m = 1
        nums2 = []
        n = 0
        solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1])

    def test_example_3(self):
        solution = Solution()
        nums1 = [0]
        m = 0
        nums2 = [1]
        n = 1
        solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1])

    def test_example_4(self):
        solution = Solution()
        nums1 = [10, 20, 20, 40, 0, 0]
        m = 4
        nums2 = [1, 2]
        n = 2
        solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1, 2, 10, 20, 20, 40])

    def test_example_5(self):
        solution = Solution()
        nums1 = [0, 0]
        m = 0
        nums2 = [1, 2]
        n = 2
        solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1, 2])


if __name__ == "__main__":
    unittest.main()
