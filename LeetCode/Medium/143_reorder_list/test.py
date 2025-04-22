import unittest
from solution import Solution, ListNode

class TestReorderList(unittest.TestCase):

    def test_1(self):
        head = ListNode.from_list([1, 2, 3, 4])
        Solution().reorderList(head)
        self.assertEqual(ListNode.to_list(head), [1, 4, 2, 3])

    def test_2(self):
        head = ListNode.from_list([1, 2, 3, 4, 5])
        Solution().reorderList(head)
        self.assertEqual(ListNode.to_list(head), [1, 5, 2, 4, 3])

    def test_3(self):
        head = ListNode.from_list([2, 4, 6, 8])
        Solution().reorderList(head)
        self.assertEqual(ListNode.to_list(head), [2, 8, 4, 6])

    def test_4(self):
        head = ListNode.from_list([2, 4, 6, 8, 10])
        Solution().reorderList(head)
        self.assertEqual(ListNode.to_list(head), [2, 10, 4, 8, 6])

    def test_5(self):
        head = ListNode.from_list([1])
        Solution().reorderList(head)
        self.assertEqual(ListNode.to_list(head), [1])

if __name__ == "__main__":
    unittest.main()
