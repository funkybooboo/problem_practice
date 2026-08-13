from typing import Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        minimum_depth: int = 100000

        def f(node: Optional[TreeNode], depth: int) -> None:
            nonlocal minimum_depth

            if not node:
                return
            if not node.left and not node.right and depth < minimum_depth:
                minimum_depth = depth

            if node.left:
                f(node.left, depth + 1)
            if node.right:
                f(node.right, depth + 1)

        f(root, 1)

        return minimum_depth
