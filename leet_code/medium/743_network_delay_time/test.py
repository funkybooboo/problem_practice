import unittest
from solution import Solution

class TestNetworkDelayTime(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
        n = 4
        k = 2
        expected = 2
        self.assertEqual(self.solution.networkDelayTime(times, n, k), expected)

    def test_example_2(self):
        times = [[1, 2, 1]]
        n = 2
        k = 1
        expected = 1
        self.assertEqual(self.solution.networkDelayTime(times, n, k), expected)

    def test_example_3(self):
        times = [[1, 2, 1]]
        n = 2
        k = 2
        expected = -1
        self.assertEqual(self.solution.networkDelayTime(times, n, k), expected)

    def test_disconnected_graph(self):
        times = [[1, 2, 1], [2, 3, 2]]
        n = 4
        k = 1
        expected = -1
        self.assertEqual(self.solution.networkDelayTime(times, n, k), expected)

    def test_single_node(self):
        times = []
        n = 1
        k = 1
        expected = 0
        self.assertEqual(self.solution.networkDelayTime(times, n, k), expected)

    def test_multiple_paths(self):
        times = [[1, 2, 1], [1, 3, 4], [2, 3, 1]]
        n = 3
        k = 1
        expected = 2  # 1→2 (1), 2→3 (1), total 2
        self.assertEqual(self.solution.networkDelayTime(times, n, k), expected)

    def test_cycle(self):
        times = [[1, 2, 1], [2, 3, 1], [3, 1, 1]]
        n = 3
        k = 1
        expected = 2  # 1→2→3
        self.assertEqual(self.solution.networkDelayTime(times, n, k), expected)

if __name__ == "__main__":
    unittest.main()
