from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def from_list(items: List[int]) -> Optional["ListNode"]:
        dummy = ListNode()
        current = dummy
        for item in items:
            current.next = ListNode(item)
            current = current.next
        return dummy.next

    @staticmethod
    def to_list(node: Optional["ListNode"]) -> List[int]:
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        dummy = ListNode(-1)
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        current.next = list1 if list1 else list2
        return dummy.next
