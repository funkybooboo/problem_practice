import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_example_1(self):
        self.assertEqual(self.s.asteroidCollision([5, 10, -5]), [5, 10])

    def test_example_2(self):
        self.assertEqual(self.s.asteroidCollision([8, -8]), [])

    def test_example_3(self):
        self.assertEqual(self.s.asteroidCollision([10, 2, -5]), [10])

    def test_example_4(self):
        self.assertEqual(self.s.asteroidCollision([3, 5, -6, 2, -1, 4]), [-6, 2, 4])

    def test_no_collision(self):
        self.assertEqual(self.s.asteroidCollision([1, 2, 3]), [1, 2, 3])

    def test_all_explode(self):
        self.assertEqual(self.s.asteroidCollision([1, -1]), [])

    def test_chain_collision(self):
        self.assertEqual(self.s.asteroidCollision([5, 4, 3, -10]), [-10])

    def test_large_left_collision(self):
        self.assertEqual(self.s.asteroidCollision([-10, -5, 3]), [-10, -5, 3])

    def test_large_right_collision(self):
        self.assertEqual(self.s.asteroidCollision([3, -5, -10]), [-5, -10])

    def test_mixed(self):
        self.assertEqual(self.s.asteroidCollision([-2, -1, 1, 2]), [-2, -1, 1, 2])


if __name__ == "__main__":
    unittest.main()
