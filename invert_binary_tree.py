# 3 лаба, 2 рівень, 3 варіант

class BinaryTree:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

root = BinaryTree(3)
root.left = BinaryTree(9)
root.right = BinaryTree(20)
root.left.left = BinaryTree(12)
root.left.right = BinaryTree(14)

def invert_binary_tree(tree) -> BinaryTree:
    if tree:
        tree.left, tree.right = tree.right, tree.left
        invert_binary_tree(tree.left)
        invert_binary_tree(tree.right)
    return tree
