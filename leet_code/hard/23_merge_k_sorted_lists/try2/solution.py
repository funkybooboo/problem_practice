import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def from_list(values):
        """Creates a linked list from a list of values and returns the head."""
        dummy = ListNode()
        current = dummy
        for val in values:
            current.next = ListNode(val)
            current = current.next
        return dummy.next

    @staticmethod
    def to_list(head):
        """Converts a linked list to a list of values starting from the given head."""
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        return values


class NodeWrapper:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        dummy = ListNode()
        current = dummy
        minHeap = []

        for node in lists:
            if node:
                heapq.heappush(minHeap, NodeWrapper(node))

        while minHeap:
            nodeWrapper = heapq.heappop(minHeap)
            current.next = nodeWrapper.node
            current = current.next

            if nodeWrapper.node.next:
                heapq.heappush(minHeap, NodeWrapper(nodeWrapper.node.next))

        return dummy.next
