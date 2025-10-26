import unittest
from solution import Solution, ListNode


class TestSolution(unittest.TestCase):
    def list_to_linkedlist(self, lst):
        """Helper function to convert a list to a linked list"""
        if not lst:
            return None
        head = ListNode(lst[0])
        current = head
        for val in lst[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    def linkedlist_to_list(self, head):
        """Helper function to convert a linked list to a list"""
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result

    def test_example_1(self):
        """Test case: Remove 6 from [1,2,6,3,4,5,6]"""
        solution = Solution()
        head = self.list_to_linkedlist([1, 2, 6, 3, 4, 5, 6])
        result = solution.removeElements(head, 6)
        self.assertEqual(self.linkedlist_to_list(result), [1, 2, 3, 4, 5])

    def test_example_2(self):
        """Test case: Remove 1 from empty list"""
        solution = Solution()
        head = self.list_to_linkedlist([])
        result = solution.removeElements(head, 1)
        self.assertEqual(self.linkedlist_to_list(result), [])

    def test_example_3(self):
        """Test case: Remove all elements [7,7,7,7] when val = 7"""
        solution = Solution()
        head = self.list_to_linkedlist([7, 7, 7, 7])
        result = solution.removeElements(head, 7)
        self.assertEqual(self.linkedlist_to_list(result), [])

    def test_example_4(self):
        """Test case: Remove 2 from [2,1,4,1,2,3]"""
        solution = Solution()
        head = self.list_to_linkedlist([2, 1, 4, 1, 2, 3])
        result = solution.removeElements(head, 2)
        self.assertEqual(self.linkedlist_to_list(result), [1, 4, 1, 3])

    def test_example_5(self):
        """Test case: Remove all elements [1,1] when val = 1"""
        solution = Solution()
        head = self.list_to_linkedlist([1, 1])
        result = solution.removeElements(head, 1)
        self.assertEqual(self.linkedlist_to_list(result), [])


if __name__ == "__main__":
    unittest.main()
