import unittest
from solution import Solution

class TestMergeTriplets(unittest.TestCase):
    def test_example_1(self):
        triplets = [[2, 5, 3], [1, 8, 4], [1, 7, 5]]
        target = [2, 7, 5]
        self.assertTrue(Solution().mergeTriplets(triplets, target))

    def test_example_2(self):
        triplets = [[3, 4, 5], [4, 5, 6]]
        target = [3, 2, 5]
        self.assertFalse(Solution().mergeTriplets(triplets, target))

    def test_example_3(self):
        triplets = [[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]]
        target = [5, 5, 5]
        self.assertTrue(Solution().mergeTriplets(triplets, target))

    def test_single_triplet(self):
        triplets = [[1, 1, 1]]
        target = [1, 1, 1]
        self.assertTrue(Solution().mergeTriplets(triplets, target))

    def test_multiple_possible_targets(self):
        triplets = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
        target = [2, 3, 4]
        self.assertTrue(Solution().mergeTriplets(triplets, target))

    def test_impossible_target(self):
        triplets = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
        target = [5, 5, 5]
        self.assertFalse(Solution().mergeTriplets(triplets, target))

    def test_large_input(self):
        triplets = [[1, 1, 1] for _ in range(100000)]
        target = [1, 1, 1]
        self.assertTrue(Solution().mergeTriplets(triplets, target))

if __name__ == '__main__':
    unittest.main()
