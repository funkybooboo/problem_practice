from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        def helper(node: TreeNode) -> bool:
            if node.left and node.right:
                if node.val == 2:
                    return helper(node.left) or helper(node.right)
                else:  # root.val == 3:
                    return helper(node.left) and helper(node.right)
            else:  # no children
                return node.val == 1

        return helper(root)
