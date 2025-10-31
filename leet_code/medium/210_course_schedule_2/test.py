import unittest

from solution import Solution


class TestCourseOrder(unittest.TestCase):

    def test_valid_order_1(self):
        # Test case 1: Example where prerequisites are [[1,0]] (1 depends on 0)
        num_courses = 2
        prerequisites = [[1, 0]]
        expected_output = [0, 1]
        self.assertEqual(
            Solution().findOrder(num_courses, prerequisites), expected_output
        )

    def test_valid_order_2(self):
        # Test case 2: Example where prerequisites are [[1,0],[2,0],[3,1],[3,2]]
        num_courses = 4
        prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
        expected_output = [0, 1, 2, 3]  # One possible correct order
        self.assertTrue(
            Solution().findOrder(num_courses, prerequisites) == expected_output
            or Solution().findOrder(num_courses, prerequisites) == [0, 2, 1, 3]
        )  # Another possible correct order

    def test_no_prerequisites(self):
        # Test case 3: No prerequisites
        num_courses = 1
        prerequisites = []
        expected_output = [0]
        self.assertEqual(
            Solution().findOrder(num_courses, prerequisites), expected_output
        )

    def test_cycle_in_prerequisites(self):
        # Test case 4: A cycle in the prerequisites (impossible to complete)
        num_courses = 2
        prerequisites = [[1, 0], [0, 1]]  # A cycle: 1 -> 0 -> 1
        expected_output = []
        self.assertEqual(
            Solution().findOrder(num_courses, prerequisites), expected_output
        )

    def test_more_complex_cycle(self):
        # Test case 5: A more complex cycle
        num_courses = 4
        prerequisites = [[1, 0], [2, 1], [3, 2], [0, 3]]  # 1 -> 0 -> 1 (cycle)
        expected_output = []
        self.assertEqual(
            Solution().findOrder(num_courses, prerequisites), expected_output
        )

    def test_multiple_valid_orders(self):
        # Test case 6: Multiple valid orders
        num_courses = 3
        prerequisites = [[1, 0], [2, 1]]
        # Possible orders: [0, 1, 2] or [0, 2, 1]
        valid_orders = [[0, 1, 2], [0, 2, 1]]
        self.assertIn(Solution().findOrder(num_courses, prerequisites), valid_orders)


if __name__ == "__main__":
    unittest.main()
