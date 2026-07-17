import unittest
from solution import Solution, ListNode


class TestReverseKGroup(unittest.TestCase):

    def test_1(self):
        head = ListNode.from_list([1, 2, 3, 4, 5])
        result = Solution().reverseKGroup(head, 2)
        self.assertEqual(ListNode.to_list(result), [2, 1, 4, 3, 5])

    def test_2(self):
        head = ListNode.from_list([1, 2, 3, 4, 5])
        result = Solution().reverseKGroup(head, 3)
        self.assertEqual(ListNode.to_list(result), [3, 2, 1, 4, 5])

    def test_3(self):
        head = ListNode.from_list([1])
        result = Solution().reverseKGroup(head, 1)
        self.assertEqual(ListNode.to_list(result), [1])

    def test_4(self):
        head = ListNode.from_list([1, 2])
        result = Solution().reverseKGroup(head, 2)
        self.assertEqual(ListNode.to_list(result), [2, 1])

    def test_5(self):
        head = ListNode.from_list([1, 2, 3])
        result = Solution().reverseKGroup(head, 1)
        self.assertEqual(ListNode.to_list(result), [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
