import unittest
from solution import Solution, ListNode


class TestMergeKLists(unittest.TestCase):

    def test_1(self):
        lists = [
            ListNode.from_list([1, 4, 5]),
            ListNode.from_list([1, 3, 4]),
            ListNode.from_list([2, 6]),
        ]
        merged = Solution().mergeKLists(lists)
        self.assertEqual(ListNode.to_list(merged), [1, 1, 2, 3, 4, 4, 5, 6])

    def test_2(self):
        lists = []
        merged = Solution().mergeKLists(lists)
        self.assertEqual(ListNode.to_list(merged), [])

    def test_3(self):
        lists = [ListNode.from_list([])]
        merged = Solution().mergeKLists(lists)
        self.assertEqual(ListNode.to_list(merged), [])

    def test_4(self):
        lists = [ListNode.from_list([1, 2, 3])]
        merged = Solution().mergeKLists(lists)
        self.assertEqual(ListNode.to_list(merged), [1, 2, 3])

    def test_5(self):
        lists = [ListNode.from_list([]), ListNode.from_list([]), ListNode.from_list([])]
        merged = Solution().mergeKLists(lists)
        self.assertEqual(ListNode.to_list(merged), [])

    def test_6(self):
        # All lists have one element
        lists = [
            ListNode.from_list([5]),
            ListNode.from_list([1]),
            ListNode.from_list([3]),
        ]
        merged = Solution().mergeKLists(lists)
        self.assertEqual(ListNode.to_list(merged), [1, 3, 5])

    def test_7(self):
        # Some lists are empty
        lists = [
            ListNode.from_list([]),
            ListNode.from_list([2]),
            ListNode.from_list([]),
            ListNode.from_list([1]),
        ]
        merged = Solution().mergeKLists(lists)
        self.assertEqual(ListNode.to_list(merged), [1, 2])

    def test_8(self):
        # Lists with duplicate values
        lists = [
            ListNode.from_list([1, 3, 5]),
            ListNode.from_list([1, 3, 5]),
            ListNode.from_list([1, 3, 5]),
        ]
        merged = Solution().mergeKLists(lists)
        self.assertEqual(ListNode.to_list(merged), [1, 1, 1, 3, 3, 3, 5, 5, 5])

    def test_9(self):
        # Lists with negative and positive numbers
        lists = [
            ListNode.from_list([-10, -5, 0]),
            ListNode.from_list([-6, 2, 4]),
            ListNode.from_list([-1, 1, 3]),
        ]
        merged = Solution().mergeKLists(lists)
        self.assertEqual(ListNode.to_list(merged), [-10, -6, -5, -1, 0, 1, 2, 3, 4])

    def test_10(self):
        # Large number of very short lists
        lists = [ListNode.from_list([i]) for i in range(20, 0, -1)]  # 20 down to 1
        merged = Solution().mergeKLists(lists)
        self.assertEqual(ListNode.to_list(merged), list(range(1, 21)))


if __name__ == "__main__":
    unittest.main()
