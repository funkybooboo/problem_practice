import unittest
from solution import Solution


class TestCountSeniors(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example_1(self):
        details = [
            "7868190130M7522",
            "5303914400F9211",
            "9273338290F4010",
        ]
        self.assertEqual(self.s.countSeniors(details), 2)

    def test_example_2(self):
        details = [
            "1313579440F2036",
            "2921522980M5644",
        ]
        self.assertEqual(self.s.countSeniors(details), 0)

    def test_exactly_60_not_counted(self):
        details = [
            "1234567890M6001",
            "0987654321F5902",
        ]
        self.assertEqual(self.s.countSeniors(details), 0)

    def test_above_60_boundary(self):
        details = [
            "1234567890M6101",
            "0987654321F6002",
            "1111111111O6203",
        ]
        self.assertEqual(self.s.countSeniors(details), 2)

    def test_all_seniors(self):
        details = [
            "0000000000M9901",
            "1111111111F8802",
            "2222222222O7703",
        ]
        self.assertEqual(self.s.countSeniors(details), 3)

    def test_single_passenger_senior(self):
        details = ["9999999999F6501"]
        self.assertEqual(self.s.countSeniors(details), 1)

    def test_single_passenger_not_senior(self):
        details = ["9999999999F1801"]
        self.assertEqual(self.s.countSeniors(details), 0)

    def test_mixed_genders_and_ages(self):
        details = [
            "1357913579M4510",
            "2468024680F6711",
            "1122334455O7312",
            "9988776655M5913",
        ]
        self.assertEqual(self.s.countSeniors(details), 2)

    def test_minimum_age(self):
        details = [
            "1231231231M0001",
            "3213213213F0102",
        ]
        self.assertEqual(self.s.countSeniors(details), 0)

    def test_maximum_age(self):
        details = [
            "5555555555M9901",
            "6666666666F9902",
        ]
        self.assertEqual(self.s.countSeniors(details), 2)


if __name__ == "__main__":
    unittest.main()

