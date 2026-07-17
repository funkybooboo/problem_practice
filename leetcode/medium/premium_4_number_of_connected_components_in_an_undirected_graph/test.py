import unittest
from solution import Solution


class TestCountComponents(unittest.TestCase):
    def test_single_component(self):
        # One connected component
        self.assertEqual(Solution().countComponents(3, [[0, 1], [0, 2]]), 1)

    def test_two_components(self):
        # Two separate components: 0-1-2 and 4-5, 3 is isolated
        self.assertEqual(
            Solution().countComponents(6, [[0, 1], [1, 2], [2, 3], [4, 5]]), 2
        )

    def test_disconnected_nodes(self):
        # No edges: each node is its own component
        self.assertEqual(Solution().countComponents(4, []), 4)

    def test_fully_connected_graph(self):
        # All nodes are connected
        self.assertEqual(Solution().countComponents(4, [[0, 1], [1, 2], [2, 3]]), 1)

    def test_multiple_isolated_components(self):
        # Nodes 0-1, 2-3, 4, 5-6
        self.assertEqual(Solution().countComponents(7, [[0, 1], [2, 3], [5, 6]]), 4)

    def test_single_node(self):
        # Only one node
        self.assertEqual(Solution().countComponents(1, []), 1)


if __name__ == "__main__":
    unittest.main()
