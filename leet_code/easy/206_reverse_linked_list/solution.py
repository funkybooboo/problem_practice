# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional, List


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev

    # Helper for testing - converts list to linked list
    @staticmethod
    def from_list(values: List[int]) -> Optional[ListNode]:
        head = current = None
        for val in reversed(values):
            head = ListNode(val, current)
            current = head
        return head

    # Helper for testing - converts linked list to list
    @staticmethod
    def to_list(node: Optional[ListNode]) -> List[int]:
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result
