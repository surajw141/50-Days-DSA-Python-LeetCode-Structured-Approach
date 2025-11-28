"""Coding Exercise: Lowest Common ancestor of a Binary Tree
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia:  “The lowest common ancestor is defined between
two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to
be a descendant of itself).”"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def lowestCommonAncestor(root, p, q):
    #p and q are nodes
    if root is None or root == p or root == q:
        return root
    
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    
    if left and right:
        return root  # If p and q are on different sides of the root
    
    return left if left else right  # If p and q are on the same side of the root


# Build the example tree:

root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

# References to nodes
p = root.left              # Node 5
q = root.right             # Node 1
p2 = root.left             # Node 5
q2 = root.left.right.right # Node 4

# Run tests
lca1 = lowestCommonAncestor(root, p, q)
lca2 = lowestCommonAncestor(root, p2, q2)

print("LCA of 5 and 1:", lca1.val)
print("LCA of 5 and 4:", lca2.val)
