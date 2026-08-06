from typing import Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val: int = val
        self.left: Optional["TreeNode"] = left
        self.right: Optional["TreeNode"] = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        # lst = left subtree
        # rst = right subtree
        def f(lst_node: Optional[TreeNode], rst_node: Optional[TreeNode]) -> bool:
            if not lst_node and not rst_node:
                return True
            if not lst_node and rst_node:
                return False
            if lst_node and not rst_node:
                return False
            if lst_node.val != rst_node.val:
                return False

            return f(lst_node.left, rst_node.right) and f(lst_node.right, rst_node.left)

        return f(root.left, root.right)
