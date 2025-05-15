from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def from_list(values: List[Optional[int]]) -> Optional['TreeNode']:
        if not values or values[0] is None:
            return None

        root = TreeNode(values[0])
        queue = deque([root])
        i = 1

        while queue and i < len(values):
            node = queue.popleft()
            if i < len(values) and values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1
            if i < len(values) and values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1

        return root

    @staticmethod
    def to_list(root: Optional['TreeNode']) -> List[Optional[int]]:
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

        while result and result[-1] is None:
            result.pop()

        return result


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right_most = []

        def helper(root: Optional[TreeNode], level: int):
            if not root:
                return

            # If we're visiting this level for the first time,
            # it means this node is the rightmost node at this level
            if level == len(right_most):
                right_most.append(root.val)

            # Traverse right subtree first to ensure rightmost nodes are visited before left ones
            helper(root.right, level + 1)

            # Then traverse left subtree
            helper(root.left, level + 1)

        helper(root, 0)

        return right_most
