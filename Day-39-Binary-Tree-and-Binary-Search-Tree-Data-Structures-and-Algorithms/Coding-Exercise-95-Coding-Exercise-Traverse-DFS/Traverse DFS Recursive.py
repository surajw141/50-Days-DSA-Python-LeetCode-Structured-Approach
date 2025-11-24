"""Question :Traverse BST

Write a 3 instance methods for a Binary Search Tree class to traverse the BST.



1. Method 1: traverse the tree depth first – In-order and return an array that contains all the values of the BST.

2. Method 2 : traverse the tree depth first – Pre-order and return an array that contains all the values of the BST.

3. Method 3 : traverse the tree depth first – Post-order and return an array that contains all the values of the BST."""

# --- your classes (unchanged) ---
from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # helper insert method for testing
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
            return

        cur = self.root
        while True:
            if value < cur.value:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = Node(value)
                    return
            else:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = Node(value)
                    return

    def dfs_in_order(self):
        res = []
        if not self.root: return res
        def inorder(node):
            if node.left: inorder(node.left)
            res.append(node.value)
            if node.right: inorder(node.right)
        inorder(self.root)
        return res

    def dfs_pre_order(self):
        res = []
        if not self.root: return res
        def preorder(node):
            res.append(node.value)
            if node.left: preorder(node.left)
            if node.right: preorder(node.right)
        preorder(self.root)
        return res

    def dfs_post_order(self):
        res = []
        if not self.root: return res
        def postorder(node):
            if node.left: postorder(node.left)
            if node.right: postorder(node.right)
            res.append(node.value)
        postorder(self.root)
        return res

# --- Testing the BST traversal methods ---

bst = BinarySearchTree()

# Insert values
for val in [10, 5, 15, 2, 7, 12, 20]:
    bst.insert(val)

print("In-order:   ", bst.dfs_in_order())    # Expected: [2, 5, 7, 10, 12, 15, 20]
print("Pre-order:  ", bst.dfs_pre_order())   # Expected: [10, 5, 2, 7, 15, 12, 20]
print("Post-order: ", bst.dfs_post_order())  # Expected: [2, 7, 5, 12, 15, 20, 10]
