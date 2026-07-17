from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def from_list(values):
        """Create a linked list from a list of values and return the head."""
        dummy = ListNode()
        current = dummy
        for val in values:
            current.next = ListNode(val)
            current = current.next
        return dummy.next

    @staticmethod
    def to_list(head):
        """Convert a linked list to a Python list of values."""
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        c = 0
        while l1 or l2 or c:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0

            r = a + b + c
            c = r // 10
            r = r % 10

            current.next = ListNode(r)

            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
