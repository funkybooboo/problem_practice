from typing import List, Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

    @staticmethod
    def from_list(values: List[int]) -> Optional['ListNode']:
        if not values:
            return None

        head = current = ListNode(values[0])
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    @staticmethod
    def to_list(head: Optional['ListNode']) -> List[int]:
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        return values

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        # Step 1: Collect nodes in an array
        nodes = []
        current = head
        while current:
            nodes.append(current)
            current = current.next

        # Step 2: Reorder using two pointers
        left, right = 0, len(nodes) - 1
        while left < right:
            nodes[left].next = nodes[right]
            left += 1
            if left == right:
                break
            nodes[right].next = nodes[left]
            right -= 1

        # Step 3: Terminate the reordered list properly
        nodes[left].next = None
