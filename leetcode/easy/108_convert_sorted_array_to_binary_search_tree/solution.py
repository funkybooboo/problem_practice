from typing import List, Optional


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
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def f(l: int, r: int) -> Optional[TreeNode]:
            if l > r:
                return None

            m = (l + r) // 2
            n = TreeNode(nums[m])
            n.left = f(l, m - 1)
            n.right = f(m + 1, r)
            return n

        return f(0, len(nums) - 1)
