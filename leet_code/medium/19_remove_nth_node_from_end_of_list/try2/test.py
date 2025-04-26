import unittest
from solution import Solution, ListNode

class TestReorderList(unittest.TestCase):

    def test_1(self):
        head = ListNode.from_list([1,2,3,4,5])
        Solution().removeNthFromEnd(head, 2)
        self.assertEqual(ListNode.to_list(head), [1,2,3,5])

    def test_2(self):
        head = ListNode.from_list([1,2])
        Solution().removeNthFromEnd(head, 1)
        self.assertEqual(ListNode.to_list(head), [1])

if __name__ == "__main__":
    unittest.main()
