import unittest
from solution import RandomizedSet

class TestRandomizedSet(unittest.TestCase):

    def test_example_1(self):
        randomizedSet = RandomizedSet()
        self.assertTrue(randomizedSet.insert(1))  # Inserts 1 to the set. Returns true as 1 was inserted successfully.
        self.assertFalse(randomizedSet.remove(2))  # Returns false as 2 does not exist in the set.
        self.assertTrue(randomizedSet.insert(2))  # Inserts 2 to the set, returns true. Set now contains [1,2].
        self.assertIn(randomizedSet.getRandom(), [1, 2])  # getRandom() should return either 1 or 2 randomly.
        self.assertTrue(randomizedSet.remove(1))  # Removes 1 from the set, returns true. Set now contains [2].
        self.assertFalse(randomizedSet.insert(2))  # 2 was already in the set, so return false.
        self.assertEqual(randomizedSet.getRandom(), 2)  # Since 2 is the only number in the set, getRandom() will always return 2.

    def test_example_2(self):
        randomizedSet = RandomizedSet()
        self.assertTrue(randomizedSet.insert(1))  # Inserts 1 to the set. Returns true as 1 was inserted successfully.
        self.assertFalse(randomizedSet.remove(2))  # Returns false as 2 does not exist in the set.
        self.assertTrue(randomizedSet.insert(2))  # Inserts 2 to the set, returns true. Set now contains [1,2].
        self.assertIn(randomizedSet.getRandom(), [1, 2])  # getRandom() should return either 1 or 2 randomly.
        self.assertTrue(randomizedSet.remove(1))  # Removes 1 from the set, returns true. Set now contains [2].
        self.assertFalse(randomizedSet.insert(2))  # 2 was already in the set, so return false.
        self.assertEqual(randomizedSet.getRandom(), 2)  # Since 2 is the only number in the set, getRandom() will always return 2.

if __name__ == '__main__':
    unittest.main()
