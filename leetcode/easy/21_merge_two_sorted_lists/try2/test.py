import unittest
from solution import ListNode, Solution


class TestMergeTwoLists(unittest.TestCase):

    def test_1(self):
        list1 = ListNode.from_list([1, 2, 4])
        list2 = ListNode.from_list([1, 3, 4])
        result = Solution.mergeTwoLists(list1, list2)
        self.assertEqual(ListNode.to_list(result), [1, 1, 2, 3, 4, 4])

    def test_2(self):
        list1 = ListNode.from_list([])
        list2 = ListNode.from_list([])
        result = Solution.mergeTwoLists(list1, list2)
        self.assertEqual(ListNode.to_list(result), [])

    def test_3(self):
        list1 = ListNode.from_list([])
        list2 = ListNode.from_list([0])
        result = Solution.mergeTwoLists(list1, list2)
        self.assertEqual(ListNode.to_list(result), [0])

    def test_4(self):
        list1 = ListNode.from_list([1, 2, 4])
        list2 = ListNode.from_list([1, 3, 5])
        result = Solution.mergeTwoLists(list1, list2)
        self.assertEqual(ListNode.to_list(result), [1, 1, 2, 3, 4, 5])

    def test_5(self):
        list1 = ListNode.from_list([])
        list2 = ListNode.from_list([1, 2])
        result = Solution.mergeTwoLists(list1, list2)
        self.assertEqual(ListNode.to_list(result), [1, 2])


if __name__ == "__main__":
    unittest.main()
