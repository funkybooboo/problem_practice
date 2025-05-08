from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def from_list(lst):
        """
        Build a tree from a level-order list of values (use None for missing nodes).
        Returns the root TreeNode or None if the list is empty.
        """
        if not lst:
            return None

        root = TreeNode(lst[0])
        queue = deque([root])
        i = 1
        while queue and i < len(lst):
            node = queue.popleft()
            # left child
            if i < len(lst) and lst[i] is not None:
                node.left = TreeNode(lst[i])
                queue.append(node.left)
            i += 1
            # right child
            if i < len(lst) and lst[i] is not None:
                node.right = TreeNode(lst[i])
                queue.append(node.right)
            i += 1

        return root

    @staticmethod
    def to_list(root):
        """
        Serialize a tree into a level-order list of values, using None for missing nodes.
        Trailing None values are trimmed.
        """
        if not root:
            return []

        result = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)

        # remove trailing Nones
        while result and result[-1] is None:
            result.pop()

        return result


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return max(left_depth, right_depth) + 1
