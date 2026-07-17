import unittest
from solution import Codec, TreeNode


class TestCodec(unittest.TestCase):
    def setUp(self):
        self.codec = Codec()

    def is_same_tree(self, p, q):
        """Recursively check if two binary trees are identical."""
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right)

    def test_round_trip_simple(self):
        # simple three-node tree [1,2,3]
        root = TreeNode.from_list([1, 2, 3])
        data = self.codec.serialize(root)
        new_root = self.codec.deserialize(data)
        self.assertTrue(self.is_same_tree(root, new_root))

    def test_round_trip_full(self):
        # example from problem: [1,2,3,null,null,4,5]
        root = TreeNode.from_list([1, 2, 3, None, None, 4, 5])
        data = self.codec.serialize(root)
        new_root = self.codec.deserialize(data)
        self.assertTrue(self.is_same_tree(root, new_root))

    def test_empty_tree(self):
        # empty tree should round-trip to None
        root = None
        data = self.codec.serialize(root)
        new_root = self.codec.deserialize(data)
        self.assertIsNone(new_root)

    def test_single_node(self):
        # single node tree
        root = TreeNode.from_list([42])
        data = self.codec.serialize(root)
        new_root = self.codec.deserialize(data)
        self.assertTrue(self.is_same_tree(root, new_root))

    def test_negative_and_zero_values(self):
        # test with zero and negative values
        root = TreeNode.from_list([0, -10, 10])
        data = self.codec.serialize(root)
        new_root = self.codec.deserialize(data)
        self.assertTrue(self.is_same_tree(root, new_root))


if __name__ == "__main__":
    unittest.main()
