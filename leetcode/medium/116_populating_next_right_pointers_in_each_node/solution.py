from typing import Optional, Dict


class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        m: Dict[int, Node] = {}

        def dfs(depth: int, node: Node) -> None:
            if not node:
                return

            if depth not in m:
                m[depth] = node
            else:
                m[depth].next = node
                m[depth] = node

            dfs(depth + 1, node.left)
            dfs(depth + 1, node.right)

        dfs(0, root)
        return root
