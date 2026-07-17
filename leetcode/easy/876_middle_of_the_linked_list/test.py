import unittest
from solution import Solution, ListNode


def build_linked_list(values):
    head = current = ListNode(values[0])
    for v in values[1:]:
        current.next = ListNode(v)
        current = current.next
    return head


def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


class TestSolution(unittest.TestCase):
    def test_example1(self):
        # Odd number of nodes
        head = build_linked_list([1, 2, 3, 4, 5])
        result = Solution().middleNode(head)
        self.assertEqual(linked_list_to_list(result), [3, 4, 5])

    def test_example2(self):
        # Even number of nodes
        head = build_linked_list([1, 2, 3, 4, 5, 6])
        result = Solution().middleNode(head)
        self.assertEqual(linked_list_to_list(result), [4, 5, 6])

    def test_single_node(self):
        head = build_linked_list([1])
        result = Solution().middleNode(head)
        self.assertEqual(linked_list_to_list(result), [1])

    def test_two_nodes(self):
        head = build_linked_list([1, 2])
        result = Solution().middleNode(head)
        # Should return the second middle (node with value 2)
        self.assertEqual(linked_list_to_list(result), [2])

    def test_three_nodes(self):
        head = build_linked_list([10, 20, 30])
        result = Solution().middleNode(head)
        self.assertEqual(linked_list_to_list(result), [20, 30])

    def test_long_list(self):
        values = list(range(1, 11))  # [1,2,3,4,5,6,7,8,9,10]
        head = build_linked_list(values)
        result = Solution().middleNode(head)
        # 10 elements → middle should be element 6 (second middle)
        self.assertEqual(linked_list_to_list(result), [6, 7, 8, 9, 10])

    def test_repeated_values(self):
        head = build_linked_list([5, 5, 5, 5, 5, 5, 5])
        result = Solution().middleNode(head)
        # 7 elements → middle is 4th node
        self.assertEqual(linked_list_to_list(result), [5, 5, 5, 5])


if __name__ == "__main__":
    unittest.main()
