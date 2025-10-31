from typing import Optional, List
from collections import deque


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

    @staticmethod
    def from_list(values: List[Optional[int]]) -> Optional["TreeNode"]:
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
    def to_list(root: Optional["TreeNode"]) -> List[Optional[int]]:
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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # If you want None -> 0
        if not root:
            return 0

        def helper(node: Optional[TreeNode]) -> tuple[int, float] | tuple[int, int]:
            """
            Returns a tuple (best_branch_sum, best_path_sum) where:
              - best_branch_sum is the maximum sum of a path starting at `node` and going down
              - best_path_sum is the maximum sum of any path anywhere in this subtree
            """
            if not node:
                # No branch, and no path at all (−inf so it never wins)
                return 0, float("-inf")

            # Recurse
            left_branch, left_best = helper(node.left)
            right_branch, right_best = helper(node.right)

            # Best single‐branch path including this node
            best_branch = max(node.val, node.val + left_branch, node.val + right_branch)

            # Best full path that *could* split at this node
            best_split = node.val + max(left_branch, 0) + max(right_branch, 0)

            # The best path in this subtree is the max of
            #   1) best so far in left subtree
            #   2) best so far in right subtree
            #   3) the split‐through‐this‐node path
            best_path = max(left_best, right_best, best_split)

            return best_branch, best_path

        # We only care about the overall best_path
        _, overall_best = helper(root)
        return overall_best
