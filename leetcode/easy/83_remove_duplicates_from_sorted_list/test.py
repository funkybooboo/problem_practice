import unittest
from solution import Solution, ListNode


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def _create_linked_list(self, values):
        """Helper to create a linked list from a list of values."""
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    def _linked_list_to_list(self, head):
        """Helper to convert linked list back to Python list."""
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result

    def test_example_one(self):
        # Input: [1,1,2] -> Output: [1,2]
        head = self._create_linked_list([1, 1, 2])
        result = self.sol.deleteDuplicates(head)
        self.assertEqual(self._linked_list_to_list(result), [1, 2])

    def test_example_two(self):
        # Input: [1,1,2,3,3] -> Output: [1,2,3]
        head = self._create_linked_list([1, 1, 2, 3, 3])
        result = self.sol.deleteDuplicates(head)
        self.assertEqual(self._linked_list_to_list(result), [1, 2, 3])

    def test_empty_list(self):
        # Input: [] -> Output: []
        head = self._create_linked_list([])
        result = self.sol.deleteDuplicates(head)
        self.assertIsNone(result)

    def test_single_node(self):
        # Input: [1] -> Output: [1]
        head = self._create_linked_list([1])
        result = self.sol.deleteDuplicates(head)
        self.assertEqual(self._linked_list_to_list(result), [1])

    def test_all_duplicates(self):
        # Input: [1,1,1,1] -> Output: [1]
        head = self._create_linked_list([1, 1, 1, 1])
        result = self.sol.deleteDuplicates(head)
        self.assertEqual(self._linked_list_to_list(result), [1])

    def test_no_duplicates(self):
        # Input: [1,2,3,4,5] -> Output: [1,2,3,4,5]
        head = self._create_linked_list([1, 2, 3, 4, 5])
        result = self.sol.deleteDuplicates(head)
        self.assertEqual(self._linked_list_to_list(result), [1, 2, 3, 4, 5])

    def test_multiple_duplicates(self):
        # Input: [1,1,2,2,3,3,4,4] -> Output: [1,2,3,4]
        head = self._create_linked_list([1, 1, 2, 2, 3, 3, 4, 4])
        result = self.sol.deleteDuplicates(head)
        self.assertEqual(self._linked_list_to_list(result), [1, 2, 3, 4])

    def test_negative_values(self):
        # Input: [-3,-3,-2,-1,-1,0,0] -> Output: [-3,-2,-1,0]
        head = self._create_linked_list([-3, -3, -2, -1, -1, 0, 0])
        result = self.sol.deleteDuplicates(head)
        self.assertEqual(self._linked_list_to_list(result), [-3, -2, -1, 0])

    def test_duplicates_at_end(self):
        # Input: [1,2,3,3,3] -> Output: [1,2,3]
        head = self._create_linked_list([1, 2, 3, 3, 3])
        result = self.sol.deleteDuplicates(head)
        self.assertEqual(self._linked_list_to_list(result), [1, 2, 3])

    def test_duplicates_at_start(self):
        # Input: [1,1,1,2,3] -> Output: [1,2,3]
        head = self._create_linked_list([1, 1, 1, 2, 3])
        result = self.sol.deleteDuplicates(head)
        self.assertEqual(self._linked_list_to_list(result), [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
