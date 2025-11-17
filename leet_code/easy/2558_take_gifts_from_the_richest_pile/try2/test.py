import unittest
from try2.solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example_1(self):
        gifts = [25, 64, 9, 4, 100]
        k = 4
        expected = 29
        self.assertEqual(self.s.pickGifts(gifts, k), expected)

    def test_example_2(self):
        gifts = [1, 1, 1, 1]
        k = 4
        expected = 4
        self.assertEqual(self.s.pickGifts(gifts, k), expected)

    def test_example_3_duplicate(self):
        gifts = [25, 64, 9, 4, 100]
        k = 4
        expected = 29
        self.assertEqual(self.s.pickGifts(gifts, k), expected)

    def test_single_element(self):
        gifts = [100]
        k = 3  # 100 → 10 → 3 → 1
        expected = 1
        self.assertEqual(self.s.pickGifts(gifts, k), expected)

    def test_k_zero(self):
        gifts = [10, 20, 30]
        k = 0
        expected = sum(gifts)
        self.assertEqual(self.s.pickGifts(gifts, k), expected)

    def test_many_operations_until_all_1(self):
        gifts = [2, 3, 4]
        k = 10  # excess operations won't change once all ≤ 1
        # operations:
        # 4→2, 3→1, 2→1, then all are 1
        expected = 1 + 1 + 1
        self.assertEqual(self.s.pickGifts(gifts, k), expected)


if __name__ == "__main__":
    unittest.main()
