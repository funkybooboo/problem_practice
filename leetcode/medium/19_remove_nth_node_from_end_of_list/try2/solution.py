from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    @staticmethod
    def from_list(values: List[int]) -> Optional["ListNode"]:
        if not values:
            return None

        head = current = ListNode(values[0])
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    @staticmethod
    def to_list(head: Optional["ListNode"]) -> List[int]:
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        return values


class Solution:
    def rec(self, head, n):
        if not head:
            return None

        head.next = self.rec(head.next, n)
        n[0] -= 1
        if n[0] == 0:
            return head.next
        return head

    def removeNthFromEnd(self, head, n):
        return self.rec(head, [n])
