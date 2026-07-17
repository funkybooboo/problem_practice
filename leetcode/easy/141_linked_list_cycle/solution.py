from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    @staticmethod
    def from_list(values):
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    def to_list(self):
        values = []
        current = self
        while current:
            values.append(current.val)
            current = current.next
        return values

    @staticmethod
    def to_list_with_cycle(values, pos):
        """
        Creates a linked list from values and introduces a cycle at index `pos`.
        :param values: list of node values
        :param pos: index to which the last node should point (or -1 for no cycle)
        :return: head of the linked list
        """
        if not values:
            return None

        head = ListNode(values[0])
        current = head
        nodes = [head]

        for val in values[1:]:
            node = ListNode(val)
            current.next = node
            current = node
            nodes.append(node)

        if pos != -1:
            current.next = nodes[pos]

        return head


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        if head.next is head:
            return True

        nodes = set()

        current = head
        while current:
            if current in nodes:
                return True
            nodes.add(current)
            current = current.next

        return False
