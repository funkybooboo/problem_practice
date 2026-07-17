import unittest
from solution import Solution, Node
from collections import deque


def build_graph(adj_list):
    """
    Build and return the graph Node reference for adj_list.
    adj_list is a list of lists of ints, 1-indexed by node value.
    Returns None if adj_list is empty.
    """
    if not adj_list:
        return None
    # Create all nodes
    nodes = {i + 1: Node(i + 1) for i in range(len(adj_list))}
    # Populate neighbors
    for i, nbrs in enumerate(adj_list, start=1):
        nodes[i].neighbors = [nodes[j] for j in nbrs]
    return nodes[1]


def graph_to_adj_list(node):
    """
    Given a Node reference, BFS the connected component,
    and return a sorted adjacency list representation.
    Returns [] if node is None.
    """
    if node is None:
        return []
    visited = {}
    q = deque([node])
    visited[node.val] = node
    while q:
        cur = q.popleft()
        for nbr in cur.neighbors:
            if nbr.val not in visited:
                visited[nbr.val] = nbr
                q.append(nbr)
    # Build adjacency list in order of vals 1..max
    max_val = max(visited)
    result = []
    for v in range(1, max_val + 1):
        if v in visited:
            nbr_vals = sorted(n.val for n in visited[v].neighbors)
            result.append(nbr_vals)
        else:
            # If a val is missing (shouldn't happen in a connected graph), put empty
            result.append([])
    return result


class TestCloneGraph(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        adj = [[2, 4], [1, 3], [2, 4], [1, 3]]
        src = build_graph(adj)
        clone = self.sol.cloneGraph(src)
        out = graph_to_adj_list(clone)
        self.assertEqual(out, adj)

    def test_example2_single_no_neighbors(self):
        adj = [[]]
        src = build_graph(adj)
        clone = self.sol.cloneGraph(src)
        out = graph_to_adj_list(clone)
        self.assertEqual(out, adj)

    def test_empty_graph(self):
        adj = []
        src = build_graph(adj)
        clone = self.sol.cloneGraph(src)
        out = graph_to_adj_list(clone)
        self.assertEqual(out, [])

    def test_two_node_chain(self):
        # extra test: 1--2
        adj = [[2], [1]]
        src = build_graph(adj)
        clone = self.sol.cloneGraph(src)
        out = graph_to_adj_list(clone)
        self.assertEqual(out, adj)


if __name__ == "__main__":
    unittest.main()
