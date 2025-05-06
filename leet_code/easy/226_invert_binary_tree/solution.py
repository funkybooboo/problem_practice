from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
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
            current = queue.popleft()

            if i < len(values) and values[i] is not None:
                current.left = TreeNode(values[i])
                queue.append(current.left)
            i += 1

            if i < len(values) and values[i] is not None:
                current.right = TreeNode(values[i])
                queue.append(current.right)
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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.helper(root)
        return root

    def helper(self, root: Optional[TreeNode]) -> None:
        if not root:
            return None
        node = root.left
        root.left = root.right
        root.right = node
        self.helper(root.left)
        self.helper(root.right)

