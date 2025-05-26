from typing import Optional, List, Union
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


class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return "[]"

        result: List[str] = []
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node is not None:
                # store as string
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("null")

        # remove trailing "null"s that aren’t needed to reconstruct the shape
        while result and result[-1] == "null":
            result.pop()

        return "[" + ",".join(result) + "]"

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # basic sanity checks
        if not data or data[0] != "[" or data[-1] != "]":
            return None

        body = data[1:-1].strip()
        if not body:
            # "[]" or "[   ]" -> empty tree
            return None

        tokens = [tok.strip() for tok in body.split(",")]
        # parse into values, using None for "null"
        values: List[Union[int, None]] = [
            None if tok == "null" else int(tok)
            for tok in tokens
        ]

        # first value must be non-null
        if not values or values[0] is None:
            return None

        root = TreeNode(values[0])
        queue = deque([root])
        i = 1
        n = len(values)

        # build tree level-by-level
        while queue and i < n:
            node = queue.popleft()
            # left child
            if i < n and values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1
            # right child
            if i < n and values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1

        return root
