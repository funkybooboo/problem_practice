import unittest
from solution import Solution


class TestFindItinerary(unittest.TestCase):
    def setUp(self):
        self.sln = Solution()

    def test_example1(self):
        tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
        expected = ["JFK", "MUC", "LHR", "SFO", "SJC"]
        self.assertEqual(self.sln.findItinerary(tickets), expected)

    def test_example2(self):
        tickets = [
            ["JFK", "SFO"],
            ["JFK", "ATL"],
            ["SFO", "ATL"],
            ["ATL", "JFK"],
            ["ATL", "SFO"],
        ]
        expected = ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]
        self.assertEqual(self.sln.findItinerary(tickets), expected)

    def test_duplicate_edges(self):
        # Two identical JFK->A tickets plus one A->JFK
        tickets = [["JFK", "A"], ["JFK", "A"], ["A", "JFK"]]
        expected = ["JFK", "A", "JFK", "A"]
        self.assertEqual(self.sln.findItinerary(tickets), expected)

    def test_forced_choice_non_lex(self):
        # Picking "KUL" first strands the trip; correct path must pick "NRT" first
        tickets = [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]
        expected = ["JFK", "NRT", "JFK", "KUL"]
        self.assertEqual(self.sln.findItinerary(tickets), expected)

    def test_lex_order_preferred(self):
        # Both paths valid; must choose lexicographically smallest at each step
        tickets = [["JFK", "AAA"], ["AAA", "JFK"], ["JFK", "BBB"]]
        expected = ["JFK", "AAA", "JFK", "BBB"]
        self.assertEqual(self.sln.findItinerary(tickets), expected)

    def test_use_all_tickets_once(self):
        # Ensure every ticket is used exactly once in a slightly larger graph
        tickets = [
            ["JFK", "SFO"],
            ["JFK", "ATL"],
            ["ATL", "ORD"],
            ["ORD", "JFK"],
            ["SFO", "ATL"],
        ]
        expected = ["JFK", "ATL", "ORD", "JFK", "SFO", "ATL"]
        self.assertEqual(self.sln.findItinerary(tickets), expected)


if __name__ == "__main__":
    unittest.main()
