"""Coding Exercise: Lowest Common Ancestor of a BST
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the defenition of LCA on wikipedia:  “The lowest common ancestor is defined between two nodes p
and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”"""

# Your existing code
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowestCommonAncestor(root, p, q):
    node = root
    while node:
        if p.val > node.val and q.val > node.val:
            node = node.right
        elif p.val < node.val and q.val < node.val:
            node = node.left
        else:
            return node

# -----------------------------
# Build the BST from the example
# -----------------------------
root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)

root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)

root.right.left = TreeNode(7)
root.right.right = TreeNode(9)

# Pick nodes for testing
p = root.left        # Node 2
q = root.right       # Node 8

# Test 1
lca = lowestCommonAncestor(root, p, q)
print("LCA of 2 and 8 is:", lca.val)

# Test 2
p2 = root.left       # Node 2
q2 = root.left.right # Node 4
lca2 = lowestCommonAncestor(root, p2, q2)
print("LCA of 2 and 4 is:", lca2.val)
