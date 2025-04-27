from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

    @staticmethod
    def to_list(head: 'Node') -> list[int]:
        """Converts linked list to a Python list (only using .next)."""
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result

    @staticmethod
    def from_list(values: list[int]) -> 'Node':
        """Converts a Python list into a linked list (only using .next)."""
        dummy = Node(0)
        current = dummy
        for val in values:
            current.next = Node(val)
            current = current.next
        return dummy.next


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        old_to_new = {None: None}
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            copy = old_to_new[curr]
            copy.next   = old_to_new[curr.next]
            copy.random = old_to_new[curr.random]
            curr = curr.next

        return old_to_new[head]
