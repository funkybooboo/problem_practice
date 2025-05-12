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
    def lowestCommonAncestor(self, root: 'TreeNode',
         p: 'TreeNode|int',
         q: 'TreeNode|int'
     ) -> 'TreeNode':
        path_p = self._get_path_to(root, p)
        path_q = self._get_path_to(root, q)

        return self._get_lca(path_p, path_q)

    @staticmethod
    def _get_lca(a: list['TreeNode'], b: list['TreeNode']) -> 'TreeNode':
        seen = set(b)
        for x in a:
            if x in seen:
                return x
        # LeetCode guarantees p and q are in the tree, so we never really hit this.
        return None

    def _get_path_to(self, root: 'TreeNode', target: 'TreeNode|int') -> list['TreeNode']:
        if not root:
            return []

        # normalize to a value to compare against .val
        tgt_val = getattr(target, 'val', target)

        if root.val == tgt_val:
            return [root]

        # search left
        left_path = self._get_path_to(root.left, target)
        if left_path:
            left_path.append(root)
            return left_path

        # search right
        right_path = self._get_path_to(root.right, target)
        if right_path:
            right_path.append(root)
            return right_path

        return []
