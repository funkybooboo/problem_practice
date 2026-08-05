from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        def f(node: ListNode, next: Optional[ListNode]) -> None:
            if not next:
                return
            if node.val == next.val:
                node.next = next.next
                f(node, next.next)
                return
            f(next, next.next)

        f(head, head.next)
        return head
