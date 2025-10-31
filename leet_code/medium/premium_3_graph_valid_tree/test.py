import unittest
from solution import Solution


class TestValidTree(unittest.TestCase):
    def test_example1_valid_tree(self):
        # Example 1:
        # n = 5, edges form a connected acyclic graph
        n = 5
        edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
        self.assertTrue(Solution().validTree(n, edges))

    def test_example2_cycle_present(self):
        # Example 2:
        # n = 5, edges contain a cycle (1–2–3–1)
        n = 5
        edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
        self.assertFalse(Solution().validTree(n, edges))

    def test_no_edges_disconnected_if_n_gt_1(self):
        # No edges: valid only if n == 1, otherwise disconnected
        self.assertFalse(Solution().validTree(2, []))
        self.assertFalse(Solution().validTree(5, []))

    def test_single_node(self):
        # Single node with no edges is a valid tree
        self.assertTrue(Solution().validTree(1, []))

    def test_fully_connected_cycle(self):
        # n = 3, fully connected graph has a cycle
        n = 3
        edges = [[0, 1], [1, 2], [2, 0]]
        self.assertFalse(Solution().validTree(n, edges))

    def test_disconnected_components(self):
        # Two separate edges: disconnected components
        n = 4
        edges = [[0, 1], [2, 3]]
        self.assertFalse(Solution().validTree(n, edges))

    def test_large_acyclic_graph(self):
        # Larger acyclic graph
        n = 6
        edges = [[0, 1], [0, 2], [1, 3], [2, 4], [2, 5]]
        self.assertTrue(Solution().validTree(n, edges))

    def test_large_graph_with_cycle(self):
        # Larger graph that has a cycle
        n = 6
        edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 1], [4, 5]]
        self.assertFalse(Solution().validTree(n, edges))


if __name__ == "__main__":
    unittest.main()
