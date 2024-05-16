import unittest
from src.invert_binary_tree import invert_binary_tree, BinaryTree

class TestLab3(unittest.TestCase):
    def test_invert_binary_tree(self):
        root = BinaryTree(3)
        root.left = BinaryTree(9)
        root.right = BinaryTree(20)
        root.left.left = BinaryTree(12)
        root.left.right = BinaryTree(14)

        invert_binary_tree(root)

        self.assertEqual(root.value, 3)
        self.assertEqual(root.left.value, 20)
        self.assertEqual(root.right.value, 9)
        self.assertEqual(root.right.left.value, 14)
        self.assertEqual(root.right.right.value, 12)

if __name__ == "__main__":
    unittest.main()
