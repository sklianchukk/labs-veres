import unittest
import invert_binary_tree

class TestLab3(unittest.TestCase):
    def test_invert_binary_tree(self):
        root = invert_binary_tree.BinaryTree(3)
        root.left = invert_binary_tree.BinaryTree(9)
        root.right = invert_binary_tree.BinaryTree(20)
        root.left.left = invert_binary_tree.BinaryTree(12)
        root.left.right = invert_binary_tree.BinaryTree(14)

        invert_binary_tree.invert_binary_tree(root)

        self.assertEqual(root.value, 3)
        self.assertEqual(root.left.value, 20)
        self.assertEqual(root.right.value, 9)
        self.assertEqual(root.right.left.value, 14)
        self.assertEqual(root.right.right.value, 12)

if __name__ == "__main__":
    unittest.main()
