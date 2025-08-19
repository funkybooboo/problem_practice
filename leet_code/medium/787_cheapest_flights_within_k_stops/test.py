import unittest
from solution import Solution

class TestFindCheapestPrice(unittest.TestCase):
    def test_example_1(self):
        n = 4
        flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
        src = 0
        dst = 3
        k = 1
        expected_output = 700
        self.assertEqual(Solution().findCheapestPrice(n, flights, src, dst, k), expected_output)

    def test_example_2(self):
        n = 3
        flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
        src = 0
        dst = 2
        k = 1
        expected_output = 200
        self.assertEqual(Solution().findCheapestPrice(n, flights, src, dst, k), expected_output)

    def test_example_3(self):
        n = 3
        flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
        src = 0
        dst = 2
        k = 0
        expected_output = 500
        self.assertEqual(Solution().findCheapestPrice(n, flights, src, dst, k), expected_output)

    def test_no_flights(self):
        n = 2
        flights = []
        src = 0
        dst = 1
        k = 0
        expected_output = -1
        self.assertEqual(Solution().findCheapestPrice(n, flights, src, dst, k), expected_output)

    def test_max_stops(self):
        n = 5
        flights = [[0, 1, 100], [1, 2, 200], [2, 3, 300], [3, 4, 400]]
        src = 0
        dst = 4
        k = 3
        expected_output = 1000
        self.assertEqual(Solution().findCheapestPrice(n, flights, src, dst, k), expected_output)

    def test_no_path(self):
        n = 4
        flights = [[0, 1, 100], [1, 2, 200], [2, 3, 300]]
        src = 0
        dst = 3
        k = 0
        expected_output = -1
        self.assertEqual(Solution().findCheapestPrice(n, flights, src, dst, k), expected_output)

if __name__ == '__main__':
    unittest.main()
