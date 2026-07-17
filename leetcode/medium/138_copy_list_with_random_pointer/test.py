import unittest
from solution import Solution, Node


def build_linked_list_with_random(arr):
    """Use Node.from_list for next pointers, then manually fix random pointers."""
    if not arr:
        return None

    # Build basic linked list using your static method
    head = Node.from_list([val for val, _ in arr])

    # Collect all nodes into a list
    nodes = []
    current = head
    while current:
        nodes.append(current)
        current = current.next

    # Set random pointers manually
    for i, (_, random_idx) in enumerate(arr):
        if random_idx is not None:
            nodes[i].random = nodes[random_idx]

    return head


def serialize_linked_list(head):
    """Serialize the linked list to [[val, random_index], ...] format."""
    if not head:
        return []

    node_to_index = {}
    nodes = []
    current = head
    index = 0
    while current:
        node_to_index[current] = index
        nodes.append(current)
        current = current.next
        index += 1

    result = []
    for node in nodes:
        random_idx = node_to_index.get(node.random, None)
        result.append([node.val, random_idx])

    return result


class TestCopyRandomList(unittest.TestCase):

    def test_1(self):
        input_list = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
        head = build_linked_list_with_random(input_list)
        copied_head = Solution().copyRandomList(head)
        result = serialize_linked_list(copied_head)
        self.assertEqual(result, input_list)

    def test_2(self):
        input_list = [[1, 1], [2, 1]]
        head = build_linked_list_with_random(input_list)
        copied_head = Solution().copyRandomList(head)
        result = serialize_linked_list(copied_head)
        self.assertEqual(result, input_list)

    def test_3(self):
        input_list = [[3, None], [3, 0], [3, None]]
        head = build_linked_list_with_random(input_list)
        copied_head = Solution().copyRandomList(head)
        result = serialize_linked_list(copied_head)
        self.assertEqual(result, input_list)

    def test_4(self):
        input_list = []
        head = build_linked_list_with_random(input_list)
        copied_head = Solution().copyRandomList(head)
        result = serialize_linked_list(copied_head)
        self.assertEqual(result, input_list)


if __name__ == "__main__":
    unittest.main()
